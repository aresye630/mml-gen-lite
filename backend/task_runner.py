# -*- coding: utf-8 -*-
"""task 队列（专家操作台 M1+，方案 §15.2 / §17.9 / §10.1 欠账清 P1）

执行态与结果资源分离：启动器（POST .../analysis 等）立即返回 202 + task_id，
后台 worker 执行 fn；结果通过 GET /tasks/{task_id} 轮询。

状态机：queued → running → succeeded | failed | cancelled
  cancel/retry（2026-09-08 P1 欠账清）：
    - cancel(queued)：任务未开始 → 直接置 cancelled（worker 取出时跳过执行）
    - cancel(running)：置取消事件（event.set()）
        * 脚本型任务（analysis/match 的子进程）→ _run_script 轮询到事件 →
          terminate → TaskCancelled 上抛 → fn 层回退 stage → _run 记 cancelled
        * 纯 python 任务（config_gen 装配，无子进程）→ fn 正常跑完返回后
          _run 检查事件已置位 → 强制记 cancelled（方案 b：产物保留，fn 已写部分产物）
    - retry 在 app 路由层（failed/cancelled 任务按 kind 重放 submit，见 app_v1）
    - 任务记录 error 字段在取消时不写（cancelled 非错误）；cancelled 与 failed
      均保留 produced/结果引用，供用户回看（cancel 尽力停、产物留已有部分，§17.9）

TaskCancelled：内部信号。注意必须是独立异常（非 BizFail 子类）——
fn 层 except BizFail 的回退逻辑不会误吞它；fn 层显式 catch TaskCancelled
回退 stage 后再上抛，_run 捕获后记 cancelled。

持久化：SESSION_ROOT/_tasks/<task_id>.json（task 不嵌 session 目录，跨 session 可全局查）

task 记录字段（对齐 §15.2 示例）：
  id / kind / session_id / state / progress{step,steps} / input / results_ref /
  error{code,message,details,retriable} / created_by / created_at / started_at /
  finished_at / elapsed_sec / exp_version / library_version

BizFail(code, details)：业务失败（任务级），runner 捕获后按 errors.yaml 结构化落 error。
"""
import json
import queue
import threading
import time
import traceback
import uuid
from pathlib import Path

from session_store import SESSION_ROOT

TASKS_ROOT = SESSION_ROOT / '_tasks'
TASKS_ROOT.mkdir(parents=True, exist_ok=True)


class BizFail(Exception):
    """业务失败：code ∈ rules/errors.yaml；details 随附（field_errors/expected 等）"""

    def __init__(self, code: str, details=None):
        super().__init__(code)
        self.code = code
        self.details = details or {}


class TaskCancelled(Exception):
    """任务被取消（内部信号）：fn 层捕获后回退 stage 再上抛；_run 记 cancelled。"""


def _now():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def _task_path(tid: str) -> Path:
    return TASKS_ROOT / f'{tid}.json'


# _write 全程互斥（worker 收尾与 cancel/annotate 可能并发写同一 tid：
# 不加锁会两个线程写同一 .json.tmp 互踩 rename 源 → FileNotFoundError）
_WRITE_LOCK = threading.Lock()


class TaskRunner:
    """单 worker 串行队列（M1 足够；分池/并发/配额是 M3+）"""

    def __init__(self, start: bool = True):
        self._q = queue.Queue()
        self._cancel_events = {}          # tid → threading.Event（submit 时注册）
        self._active_tid = None           # 当前 worker 正在执行的任务 id（单 worker）
        if start:
            self._t = threading.Thread(target=self._loop, daemon=True,
                                       name='v1-task-worker')
            self._t.start()
        else:
            self._t = None                # 纯队列管理实例（单测用，不消费）

    # ── 对外 ──
    def submit(self, kind: str, session_id: str, payload: dict, fn,
               created_by: str = 'ui') -> str:
        """入队并立即返回 task_id；fn(session_id, payload) 同步执行到出结果"""
        tid = f't_{uuid.uuid4().hex[:8]}'
        exp_version = payload.get('exp_version') or self._exp_version_of(session_id)
        rec = {
            'id': tid, 'kind': kind, 'session_id': session_id,
            'state': 'queued', 'stage': None, 'progress': {'step': 0, 'steps': []},
            'input': payload.get('input', {}),
            'prev_stage': payload.get('prev_stage'),
            'results_ref': None, 'error': None,
            'created_by': created_by, 'created_at': _now(),
            'started_at': None, 'finished_at': None, 'elapsed_sec': None,
            'exp_version': exp_version, 'library_version': None,
        }
        # fn 需要自己的 tid 时从 payload['_tid'] 取（S2 agent 执行体更新 stage 用）
        payload = {**payload, '_tid': tid}
        self._write(tid, rec)
        self._cancel_events[tid] = threading.Event()
        self._q.put((tid, kind, session_id, payload, fn))
        return tid

    def update_stage(self, tid: str, stage):
        """任务阶段推进（agent 执行体在 fn 内调用；幂等写盘，_WRITE_LOCK 保护）"""
        rec = self._task_path_get(tid)
        if rec is None:
            return
        if rec.get('stage') == stage:
            return
        rec['stage'] = stage
        self._write(tid, rec)

    def update_progress(self, tid: str, info: dict):
        """任务运行期可观测信息（P0-2，2026-10-30）。

        目的：agent 子进程挂起时，运维能看到「pid / 日志字节 / 最后输出距今秒数」，
        不用等超时才知道卡了，也不用 py-spy（容器常无 CAP_SYS_PTRACE）。

        info 例：{'pid': 1234, 'log_bytes': 40960, 'last_output_age_s': 312.0,
                 'stage': 'writing_artifacts'}
        """
        rec = self._task_path_get(tid)
        if rec is None:
            return
        if not isinstance(rec.get('progress'), dict):
            rec['progress'] = {}
        rec['progress'].update(info or {})
        rec['progress']['updated_at'] = time.strftime(
            '%Y-%m-%dT%H:%M:%SZ', time.gmtime())
        self._write(tid, rec)

    def cancel(self, tid: str):
        """请求取消。返回 (ok, payload)：
        queued  → 直接落盘 cancelled（worker 取出时跳过执行）
        running → 置取消事件（脚本被杀 / 纯 python 任务返回后强制 cancelled）
        终态（succeeded/failed/cancelled）→ ok=False（路由层 409）
        """
        rec = self._task_path_get(tid)
        if rec is None:
            return False, {'state': 'not_found'}
        st = rec.get('state')
        if st == 'queued':
            rec['state'] = 'cancelled'
            rec['finished_at'] = _now()
            rec['elapsed_sec'] = 0.0
            self._write(tid, rec)
            return True, {'state': 'cancelled'}
        if st == 'running':
            self._cancel_events.setdefault(tid, threading.Event()).set()
            return True, {'state': 'running', 'cancel_requested': True,
                          'hint': '尽力停中：脚本任务将终止子进程；纯计算任务返回后落 cancelled。轮询 GET /tasks/{id} 看终态'}
        return False, {'state': st}

    def cancel_event(self, tid: str):
        """任务取消事件（fn/脚本轮询用）。None = 无事件（不存在/已回收）"""
        return self._cancel_events.get(tid)

    def active_event(self):
        """当前 worker 正在执行任务的取消事件（worker 线程内调用）。"""
        tid = self._active_tid
        if tid is None:
            return None
        return self._cancel_events.get(tid)

    def list_tasks(self, sid: str = None, state: str = None, kind: str = None):
        """全局任务列表（created_at 倒序）。过滤参数可选；轻量摘要。"""
        items = []
        for p in TASKS_ROOT.glob('*.json'):
            if p.name.endswith('.json.tmp'):
                continue
            try:
                rec = json.loads(p.read_text(encoding='utf-8'))
            except Exception:
                continue
            if sid and rec.get('session_id') != sid:
                continue
            if state and rec.get('state') != state:
                continue
            if kind and rec.get('kind') != kind:
                continue
            items.append(rec)
        items.sort(key=lambda r: r.get('created_at') or '', reverse=True)
        return items

    def recover_pending(self, interrupted_msg='服务重启，任务中断（M1 内存队列单 worker），请重新触发'):
        """启动恢复（服务进程重启后调用）：残留 queued/running 任务 → failed。

        背景（方案 §15.2/§10.1 边界①）：任务队列在内存，重启即丢。M2 前端轮询
        若遇到假 running 会死等——此处把断点任务显式标记 failed（INTERNAL +
        interrupted=True），前端可展示「任务中断，请重新触发」。幂等可重跑。
        """
        n = 0
        for p in sorted(TASKS_ROOT.glob('*.json')):
            if p.name.endswith('.json.tmp'):
                continue
            try:
                rec = json.loads(p.read_text(encoding='utf-8'))
            except Exception:
                continue
            if rec.get('state') not in ('queued', 'running'):
                continue
            rec['state'] = 'failed'
            rec['error'] = {'code': 'INTERNAL', 'retriable': True,
                            'details': {'interrupted': True, 'log': interrupted_msg}}
            rec['finished_at'] = _now()
            self._write(rec['id'], rec)
            n += 1
        return n

    def get(self, tid: str):
        p = _task_path(tid)
        if not p.is_file():
            return None
        return json.loads(p.read_text(encoding='utf-8'))

    def annotate(self, tid: str, **fields):
        """终态任务补备注字段（retried_to 等；不覆盖既有键值）"""
        rec = self._task_path_get(tid)
        if rec is None:
            return
        for k, v in fields.items():
            rec.setdefault(k, v)
        self._write(tid, rec)

    # ── 内部 ──
    @staticmethod
    def _exp_version_of(session_id: str):
        try:
            from session_store import load_session
            s = load_session(session_id)
            return s.get('exp_version') if s else None
        except Exception:
            return None

    @staticmethod
    def _write(tid: str, rec: dict):
        with _WRITE_LOCK:
            tmp = _task_path(tid).with_suffix('.json.tmp')
            tmp.write_text(json.dumps(rec, ensure_ascii=False, indent=1),
                           encoding='utf-8')
            tmp.rename(_task_path(tid))

    def _loop(self):
        while True:
            tid, kind, session_id, payload, fn = self._q.get()
            self._run(tid, kind, session_id, payload, fn)
            self._q.task_done()

    def _run(self, tid, kind, session_id, payload, fn):
        rec = self._task_path_get(tid)
        if rec is None:
            return
        # queued 期间被 cancel → 不执行 fn，直接收尾（cancel 已落盘 cancelled）
        if rec.get('state') == 'cancelled':
            if rec.get('finished_at') is None:
                rec['finished_at'] = _now()
                rec['elapsed_sec'] = 0.0
                self._write(tid, rec)
            return
        t0 = time.time()
        self._active_tid = tid
        ev = self._cancel_events.setdefault(tid, threading.Event())
        rec['state'] = 'running'
        rec['started_at'] = _now()
        self._write(tid, rec)
        cancelled = False
        try:
            result = fn(session_id, payload)
            # 结果字段先落 rec（即使随后被强制 cancelled，产物引用仍保留供回看）
            if isinstance(result, dict):
                rec['results_ref'] = result.get('results_ref')
                rec['library_version'] = result.get('library_version')
                rec['summary'] = result.get('summary')
                rec['progress'] = {'step': len(rec['progress'].get('steps', [])),
                                   'steps': rec['progress'].get('steps', [])}
        except TaskCancelled:
            # 尽力停成功路径：脚本已终止。fn 层已回退 stage；产物留已有部分
            cancelled = True
            rec['progress'] = {'step': len(rec['progress'].get('steps', [])),
                               'steps': rec['progress'].get('steps', [])}
        except BizFail as e:
            rec['state'] = 'failed'
            rec['error'] = {'code': e.code, 'details': e.details}
        except Exception as e:  # noqa: BLE001 —— 兜底 INTERNAL（同 §16）
            rec['state'] = 'failed'
            rec['error'] = {'code': 'INTERNAL',
                            'details': {'log': traceback.format_exc()[-2000:]}}
        if rec.get('state') != 'failed':
            # 纯 python 任务 fn 正常返回但取消事件已置位 → 强制 cancelled（方案 b）
            if cancelled or ev.is_set():
                rec['state'] = 'cancelled'
            else:
                rec['state'] = 'succeeded'
        # fn 内 update_stage() 推进的 stage 先落盘过 —— 收尾写回前从盘 reload 保留
        # （否则本函数内存 rec 是旧副本，覆盖写会把 stage 冲掉）
        cur = self._task_path_get(tid)
        if cur is not None and cur.get('stage') is not None:
            rec['stage'] = cur.get('stage')
        rec['finished_at'] = _now()
        rec['elapsed_sec'] = round(time.time() - t0, 1)
        self._write(tid, rec)
        self._active_tid = None

    @staticmethod
    def _task_path_get(tid: str):
        p = _task_path(tid)
        if not p.is_file():
            return None
        return json.loads(p.read_text(encoding='utf-8'))


# 全局单例（FastAPI 多 worker 场景换进程队列；M1 单进程够验收）
runner = TaskRunner()

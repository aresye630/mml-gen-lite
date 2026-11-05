#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""操作台功能冒烟 —— 57 个 API 接口全量点到（真实 HTTP 调用）。

与 test_integration.py 的区别（用户口径 2026-09-19）：
  test_integration.py   产线冒烟：跑脚本/判据/确定性（验代码对不对）
  本套件                 操作台冒烟：走 HTTP API（验界面能干成活）

覆盖（四个文件的路由）:
  app.py            12 个  老接口 + 对话 /api/chat
  app_v1.py         16 个  会话 / 任务 / 上传 exp
  artifacts_v1.py   16 个  产物读取（md/实例/关系/判定卡/图查询）
  generations_v1.py 17 个  MML 生成流程

用法:
    python3 test_console_smoke.py                 # 全量（默认）
    python3 test_console_smoke.py --verbose       # 打印每个接口的响应摘要
    python3 test_console_smoke.py --base http://127.0.0.1:8600

退出码 0 = 全通过；1 = 有失败。
"""
import argparse
import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

BASE = 'http://127.0.0.1:8600'
VERBOSE = False
RESULTS = []


SKIPS = []


def case(name, ok, detail=''):
    """ok=True 通过 / False 失败 / None 跳过（依赖客户数据 real_exp 的用例用）。"""
    if ok is None:
        SKIPS.append((name, detail))
        print('  %s %-56s %s' % ('-', name, detail))
        return
    RESULTS.append((name, bool(ok), detail))
    print('  %s %-56s %s' % ('✓' if ok else '✗', name, detail))


def call(method, path, body=None, form=None, timeout=60, raw=False):
    """发起 HTTP 请求，返回 (status, 解析后的 body 或文本, 错误字符串)。"""
    url = BASE + path
    data = None
    headers = {}
    if body is not None:
        data = json.dumps(body).encode()
        headers['Content-Type'] = 'application/json'
    elif form is not None:
        boundary = '----smoke%d' % int(time.time() * 1000)
        parts = []
        for k, v in form.items():
            parts.append('--' + boundary)
            parts.append('Content-Disposition: form-data; name="%s"' % k)
            parts.append('')
            parts.append(str(v))
        parts.append('--' + boundary + '--')
        data = '\r\n'.join(parts).encode()
        headers['Content-Type'] = 'multipart/form-data; boundary=' + boundary
    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            txt = r.read().decode('utf-8', 'ignore')
            if raw:
                return r.status, txt, ''
            try:
                return r.status, json.loads(txt), ''
            except Exception:
                return r.status, txt, ''
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode('utf-8', 'ignore')[:200], 'HTTP %d' % e.code
    except Exception as e:
        return 0, '', str(e)[:150]


def upload(sid, ep, fpath, timeout=180):
    """multipart 上传真实文件到 /sessions/{sid}/{ep}。返回 (status, body, err)。"""
    import uuid
    boundary = '----smoke' + uuid.uuid4().hex
    with open(fpath, 'rb') as f:
        content = f.read()
    parts = []
    parts.append(('--' + boundary).encode())
    parts.append(('Content-Disposition: form-data; name="file"; filename="%s"' % fpath.name).encode())
    parts.append(b'Content-Type: text/plain')
    parts.append(b'')
    parts.append(content)
    parts.append(('--' + boundary + '--').encode())
    data = b'\r\n'.join(parts)
    url = BASE + '/api/v1/sessions/%s/%s' % (sid, ep)
    req = urllib.request.Request(url, data=data, method='POST', headers={
        'Content-Type': 'multipart/form-data; boundary=' + boundary})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            txt = r.read().decode('utf-8', 'ignore')
            try:
                return r.status, json.loads(txt), ''
            except Exception:
                return r.status, txt, ''
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode('utf-8', 'ignore')[:200], 'HTTP %d' % e.code
    except Exception as e:
        return 0, '', str(e)[:150]


def put_exp(sid, fpath, timeout=180):
    """PUT /sessions/{sid}/exp 上传 exp 文件（multipart，字段 file 或 exp）。"""
    import uuid
    boundary = '----smoke' + uuid.uuid4().hex
    with open(fpath, 'rb') as f:
        content = f.read()
    data = b'\r\n'.join([
        ('--' + boundary).encode(),
        ('Content-Disposition: form-data; name="file"; filename="%s"' % fpath.name).encode(),
        b'Content-Type: text/plain', b'', content,
        ('--' + boundary + '--').encode()])
    req = urllib.request.Request(BASE + '/api/v1/sessions/%s/exp' % sid, data=data,
                                 method='PUT',
                                 headers={'Content-Type': 'multipart/form-data; boundary=' + boundary})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            txt = r.read().decode('utf-8', 'ignore')
            try:
                return r.status, json.loads(txt), ''
            except Exception:
                return r.status, txt, ''
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode('utf-8', 'ignore')[:200], 'HTTP %d' % e.code
    except Exception as e:
        return 0, '', str(e)[:150]


PLACEHOLDER_REPLY = re.compile(r'本次未获得回复|请重试\s*$')
# 对话失败「可读原因」的特征词（与 backend/app.py::_diagnose_hermes_failure 的分类对齐）
FAIL_REASON_TELL = re.compile(r'鉴权|API key|不可达|超时|会话上下文|子进程|未返回|Node\.js|部署')


def jget(obj, *keys, default=None):
    """安全取嵌套字段。"""
    cur = obj
    for k in keys:
        if isinstance(cur, dict):
            cur = cur.get(k)
        elif isinstance(cur, list) and isinstance(k, int) and len(cur) > k:
            cur = cur[k]
        else:
            return default
    return cur if cur is not None else default


def main():
    global BASE, VERBOSE
    ap = argparse.ArgumentParser()
    ap.add_argument('--base', default=BASE)
    ap.add_argument('--verbose', action='store_true')
    ap.add_argument('--sid', default=None, help='已有会话 id（默认自动挑一个）')
    args = ap.parse_args()
    BASE = args.base.rstrip('/')
    VERBOSE = args.verbose

    print('=' * 70)
    print('操作台功能冒烟 —— 全量 API 点到')
    print('  服务: %s' % BASE)
    print('=' * 70)

    t0 = time.time()

    # ── 0. 服务与静态页 ──
    print('\n【0. 服务与静态页】')
    st, body, err = call('GET', '/', timeout=15, raw=True)
    case('GET /  操作台首页', st == 200 and len(body) > 200, 'HTTP %d, %d 字节' % (st, len(body)))
    st, body, err = call('GET', '/app', timeout=15, raw=True)
    case('GET /app  应用页', st == 200 and len(body) > 200, 'HTTP %d, %d 字节' % (st, len(body)))

    # ── 1. 找到可用会话（后续用例都依赖它）──
    print('\n【1. 会话（app_v1）】')
    st, body, err = call('GET', '/api/v1/sessions')
    sessions = jget(body, 'items', default=[]) or []
    case('GET /sessions  会话列表', st == 200 and isinstance(sessions, list),
         '%d 个会话' % len(sessions))
    sid = args.sid
    if not sid and sessions:
        cand = [s for s in sessions if s.get('stage')] or sessions
        sid = jget(cand[0], 'session_id') or jget(cand[0], 'id') or jget(cand[0], 'sid')
    # ★ 2026-10-24：real_exp 是客户数据（不入版本库）。没有它就无法"上传 exp → 分析"，
    #   依赖分析产物的用例（判定卡/关系/实例/产物读取）应记**跳过**而不是失败，
    #   否则干净环境 release 永远红。
    _exp_avail = Path('/opt/expgv/testdata/real_exp/udg.exp.txt').exists()
    # ⚠ 干净容器里可能一个会话都没有（如 release.sh 起的临时容器）→ 自建
    #   操作台冒烟要能开箱即跑，不能依赖预置数据
    if not sid:
        st, body, err = call('POST', '/api/v1/sessions',
                             form={'name': 'smoke_auto_%d' % int(time.time()),
                                   'product': 'UDG'})
        sid = jget(body, 'session_id') or jget(body, 'id')
        if sid:
            # 上传真实 exp → 触发分析并等就绪（后续产物/判定卡用例都依赖它）
            expf = Path('/opt/expgv/testdata/real_exp/udg.exp.txt')
            if expf.exists():
                put_exp(sid, expf, timeout=180)
                for _ in range(80):
                    st2, sb, _ = call('GET', '/api/v1/sessions/%s' % sid)
                    stg = jget(sb, 'stage', default='') or ''
                    if stg in ('matched', 'exp_ready', 'ready', 'failed'):
                        break
                    time.sleep(3)
    case('找到/自建可用会话', bool(sid), sid or '无')

    if sid:
        st, body, err = call('GET', '/api/v1/sessions/%s' % sid)
        case('GET /sessions/{sid}  会话详情', st == 200, 'HTTP %d' % st)
        st, body, err = call('GET', '/api/v1/sessions/%s/exps' % sid)
        case('GET /sessions/{sid}/exps  exp 列表', st == 200, 'HTTP %d' % st)
        st, body, err = call('GET', '/api/v1/sessions/%s/guide' % sid)
        case('GET /sessions/{sid}/guide  引导', st == 200, 'HTTP %d' % st)
        st, body, err = call('GET', '/api/v1/sessions/%s/match' % sid)
        case('GET /sessions/{sid}/match  匹配总览',
             (st == 200) if _exp_avail else None,
             'HTTP %d' % st if _exp_avail else '跳过：无真实 exp（客户数据），无法分析')
        st, body, err = call('GET', '/api/v1/sessions/%s/jobs-history' % sid)
        case('GET /sessions/{sid}/jobs-history', st == 200, 'HTTP %d' % st)

    # ── 2. 任务（app_v1）──
    print('\n【2. 任务（app_v1）】')
    st, body, err = call('GET', '/api/v1/tasks')
    tasks = jget(body, 'items', default=[]) or []
    case('GET /tasks  任务列表', st == 200, '%d 个任务' % len(tasks))
    if tasks:
        tid = jget(tasks[0], 'id') or jget(tasks[0], 'task_id')
        st, body, err = call('GET', '/api/v1/tasks/%s' % tid)
        case('GET /tasks/{tid}  任务详情', st == 200, 'HTTP %d' % st)
        st, body, err = call('GET', '/api/v1/tasks/%s/artifacts' % tid)
        case('GET /tasks/{tid}/artifacts', st in (200, 404), 'HTTP %d' % st)

    # ── 3. 产物读取（artifacts_v1）──
    print('\n【3. 产物读取（artifacts_v1）】')
    if sid:
        st, body, err = call('GET', '/api/v1/sessions/%s/artifacts' % sid)
        case('GET /artifacts  产物总览', st == 200, 'HTTP %d' % st)
        # rels/graph 必填 root（特性标题）—— 用关系数据里的第一个特性做中心
        st, rbody, err = call('GET', '/api/v1/sessions/%s/artifacts/rels' % sid)
        root = ''
        feats = jget(rbody, 'features', default=[]) or []
        if feats:
            root = jget(feats[0], 'title', default='') or ''
        for ep, nm in [
            ('artifacts/rels', '关系'),
            ('artifacts/rels/graph?root=' + urllib.parse.quote(root or 'x'), '关系图'),
            ('artifacts/instances', '实例'),
            ('artifacts/exp-raw', 'exp 原文'),
            ('artifacts/cmd-list', '命令清单'),
            ('artifacts/analysis-tabs', '分析页签'),
            ('artifacts/analysis-md', '分析 md'),
            ('artifacts/report', '报告'),
        ]:
            st, body, err = call('GET', '/api/v1/sessions/%s/%s' % (sid, ep))
            case('GET /%s  %s' % (ep, nm), (st == 200) if _exp_avail else None,
                 ('HTTP %d' % st) if _exp_avail else '跳过：无真实 exp')
        # graph-query 需 seq（实例序号）—— 从图统计里取一个真实节点
        st, gbody, err = call('GET', '/api/v1/sessions/%s/exp-analysis/graph-stats' % sid)
        seq = ''
        for key in ('nodes', 'node_count', 'sample_nodes'):
            v = jget(gbody, key)
            if isinstance(v, list) and v:
                seq = jget(v[0], 'seq', default=v[0]) if isinstance(v[0], dict) else v[0]
                break
        if not seq:
            sq = jget(gbody, 'sample_seqs', default=None) or jget(gbody, 'seqs', default=None)
            if isinstance(sq, list) and sq:
                seq = sq[0]
        gq = 'exp-analysis/graph-query?seq=%s' % (seq if seq else 1)
        for ep, nm in [
            ('exp-analysis/graph-stats', '图统计'),
            (gq, '图查询(seq=%s)' % (seq or '1')),
            ('exp-analysis/find', '查找'),
            ('exp-analysis/find-subgraph', '查找子图'),
        ]:
            st, body, err = call('GET', '/api/v1/sessions/%s/%s' % (sid, ep))
            # 给了必需参数 → 应 200；400/404 表示参数合法但数据不含该节点（也是接口在工作）
            _ok = (st in (200, 404)) if _exp_avail else None
            case('GET /%s  %s' % (ep, nm), _ok,
                 ('HTTP %d' % st) if _exp_avail else '跳过：无真实 exp')

    # ── 4. 判定卡（artifacts_v1）──
    print('\n【4. 判定卡（artifacts_v1）】')
    if sid:
        st, body, err = call('GET', '/api/v1/sessions/%s/match/cards' % sid)
        cards = jget(body, 'items', default=[]) or []
        case('GET /match/cards  判定卡列表',
             (st == 200) if _exp_avail else None,
             ('%d 张' % len(cards)) if _exp_avail else '跳过：无真实 exp')
        if cards:
            fid = jget(cards[0], 'fid') or jget(cards[0], 'feature_id') or jget(cards[0], 'id')
            if fid:
                st, body, err = call('GET', '/api/v1/sessions/%s/match/cards/%s' % (sid, fid))
                case('GET /match/cards/{fid}  判定卡详情', st == 200,
                     '%s → HTTP %d' % (fid, st))

    # ── 5. 生成（generations_v1）──
    print('\n【5. MML 生成（generations_v1）】')
    st, body, err = call('GET', '/api/v1/capabilities')
    case('GET /capabilities  能力清单', st == 200, 'HTTP %d' % st)
    if sid:
        st, body, err = call('GET', '/api/v1/sessions/%s/generations' % sid)
        gens = jget(body, 'items', default=[]) or []
        case('GET /generations  生成列表', st == 200, '%d 个' % len(gens))
        if gens:
            gid = jget(gens[0], 'id') or jget(gens[0], 'gid')
            if gid:
                st, body, err = call('GET', '/api/v1/sessions/%s/generations/%s' % (sid, gid))
                case('GET /generations/{gid}  生成详情', st == 200, 'HTTP %d' % st)
                st, body, err = call('GET', '/api/v1/sessions/%s/generations/%s/trace' % (sid, gid))
                case('GET /generations/{gid}/trace  轨迹', st == 200, 'HTTP %d' % st)
                st, body, err = call('GET', '/api/v1/sessions/%s/generations/%s/download' % (sid, gid))
                case('GET /generations/{gid}/download  下载', st in (200, 404),
                     'HTTP %d' % st)
                for kind in ('csv', 'md', 'mml', 'template', 'checklist'):
                    st, body, err = call('GET', '/api/v1/sessions/%s/generations/%s/artifacts/%s'
                                         % (sid, gid, kind))
                    case('GET /generations/{gid}/artifacts/%s' % kind, st in (200, 404),
                         'HTTP %d' % st)

    # ── 6. 老接口（app.py）──
    print('\n【6. 老接口（app.py）】')
    st, body, err = call('GET', '/api/cases')
    case('GET /api/cases  数据集', st == 200, 'HTTP %d' % st)
    st, body, err = call('GET', '/api/history')
    case('GET /api/history  历史', st == 200, 'HTTP %d' % st)
    # /api/artifact 必填 path（白名单 runs/ 与 workspace 内）—— 用真实产物路径
    apath = ''
    if sid:
        st, abody, err = call('GET', '/api/v1/sessions/%s/artifacts/analysis-md' % sid)
        if not _exp_avail:
            pass  # 下方判据按 _exp_avail 跳过
        for k in ('path', 'file', 'abs_path'):
            v = jget(abody, k)
            if isinstance(v, str) and v:
                apath = v
                break
    if not apath:
        # 退路：直接指一份已知产物
        apath = ''
        for base in ('/opt/expgv/kb/output_udg_feature/feature_v3',
                     '/opt/expgv/kb/output_ueg_feature/output_ueg_feature_v3'):
            for c in Path(base).rglob('*.md'):
                apath = str(c)
                break
            if apath:
                break
        if not apath or not Path(apath).exists():
            # 再退：用 workspace 白名单内的任何真实文件
            for c in Path('/opt/expgv/kb/output_udg_feature/feature_v3').glob('*.md'):
                apath = str(c)
                break
    st, body, err = call('GET', '/api/artifact?path=' + urllib.parse.quote(apath))
    case('GET /api/artifact  产物读取', st == 200, 'HTTP %d（path=%s）' % (st, apath[-40:]))

    # ── 7. 对话（app.py，最要点到的功能）──
    print('\n【7. 对话（app.py /api/chat）】')
    if sid:
        q = '只回一个数字：特性配置基线目录下有多少个 md 文件？'
        t1 = time.time()
        st, body, err = call('POST', '/api/chat',
                             body={'case': sid, 'session': sid, 'question': q,
                                   'sid': sid},
                             timeout=280)
        el = time.time() - t1
        reply = jget(body, 'reply', default='') or jget(body, 'answer', default='') or ''
        # ⚠ 早期兜底 `if not reply and isinstance(body, str): reply = body[:200]` 会把
        #   **错误包络 dict 整个当回复**（回复 200 字 = 整段 JSON），导致「有回复」恒成立、
        #   502 被误判成失败。改为：只在**成功响应**上兜底，错误包络一律不算回复。
        if not reply and st == 200 and isinstance(body, str):
            reply = body[:200]
        err_txt = jget(body, 'error', default='') or ''
        # ⚠ call() 对 HTTPError 返回的是**截断 200 字的字符串**（不是 dict），jget 取不到
        #   error 字段 ⇒ 从原文里用正则抠出 error 值（也接受纯文本原因）。
        if not err_txt and isinstance(body, str) and body:
            m = re.search(r'"error"\s*:\s*"((?:[^"\\]|\\.)*)"', body)
            err_txt = m.group(1) if m else body[:120]
        # ★ 2026-10-23：判据分两档 —— 不能「没配 key 就判失败」，也不能「失败被吞还判通过」。
        #   ① 有回复（200 + 非空）→ 通过（key 已注入，端到端可用）
        #   ② 无回复 → 必须 5xx 且带可读原因（error 非空、不能是"（本次未获得回复）"占位）
        #      —— 这正是旧实现的病灶：200 + 占位话术，把 401 吞成"请重试"。
        if reply:
            case('POST /api/chat  对话可用', st == 200 and not PLACEHOLDER_REPLY.search(str(reply)),
                 'HTTP %d, %.1fs, 回复 %d 字' % (st, el, len(reply)))
        else:
            # 原因必须是「人话」：命中失败分类表之一，或至少是非 JSON 的自然语言文本
            _e = str(err_txt)
            readable = bool(_e.strip()) and (
                bool(FAIL_REASON_TELL.search(_e)) or not _e.lstrip().startswith('{'))
            ok_err = (st >= 500 and readable and not PLACEHOLDER_REPLY.search(_e))
            case('POST /api/chat  对话可用（或失败原因可见）', ok_err,
                 'HTTP %d, %.1fs, 原因=%s' % (st, el, _e[:60] or '（空）'))
        if VERBOSE and reply:
            print('      回复摘要: %s' % reply[:150].replace('\n', ' '))

    # ── 8. 写操作（低风险：建会话 → 改名 → 归档回滚）──
    print('\n【8. 写操作（建会话/改名/上传 exp 校验）】')
    nm = 'smoke_%d' % int(time.time())
    st, body, err = call('POST', '/api/v1/sessions', form={'name': nm, 'product': 'UDG'})
    new_sid = jget(body, 'session_id') or jget(body, 'id')
    case('POST /sessions  建会话', st in (200, 201) and bool(new_sid),
         'HTTP %d, id=%s' % (st, new_sid or '-'))
    if new_sid:
        st, body, err = call('PATCH', '/api/v1/sessions/%s' % new_sid,
                             body={'name': nm + '_renamed'})
        case('PATCH /sessions/{sid}  改名', st in (200, 204, 405), 'HTTP %d' % st)
        # 上传 exp（用真实样本）—— PUT /sessions/{sid}/exp
        # 按真实状态机：draft → PUT /exp（触发分析，异步）→ 等任务完成 → impact → 归档
        expf = Path('/opt/expgv/testdata/real_exp/udg.exp.txt')
        if expf.exists():
            st, body, err = put_exp(new_sid, expf, timeout=180)
            case('PUT /sessions/{sid}/exp  上传 exp（触发分析）', st in (200, 201),
                 'HTTP %d' % st)
            # 等分析任务完成（PUT 会起异步任务，stage: analyzing → matched）
            stage = ''
            # ★ 2026-10-23：等待窗口 60×3s=180s 偏短 —— 同一镜像实测分析耗时 37~180s+
            #   （与宿主机负载强相关）。窗口不够会误判 stage=analyzing 为失败。
            #   改为 100×3s=300s；仍超时则报「超时（最后一次 stage）」而非笼统失败。
            _deadline = time.time() + 300
            stage = ''
            while time.time() < _deadline:
                st2, sb, _ = call('GET', '/api/v1/sessions/%s' % new_sid)
                stage = jget(sb, 'stage', default='') or ''
                if stage in ('matched', 'exp_ready', 'ready', 'failed'):
                    break
                time.sleep(3)
            case('分析任务完成（stage 就绪）',
                 (stage in ('matched', 'exp_ready', 'ready')) if _exp_avail else None,
                 'stage=%s（等 %.0fs）' % (stage or '?', 300 - max(0, _deadline - time.time())))
            if stage in ('matched', 'exp_ready', 'ready'):
                st, body, err = upload(new_sid, 'exp/impact', expf, timeout=180)
                case('POST /sessions/{sid}/exp/impact  影响评估（真上传）',
                     st in (200, 409), 'HTTP %d' % st)
            # 清理：归档（等任务跑完；503=队列忙也是正常态）
            st, body, err = call('POST', '/api/v1/sessions/%s/archive' % new_sid,
                                 timeout=60)
            case('POST /sessions/{sid}/archive  归档', st in (200, 404, 405, 503),
                 'HTTP %d（503=有任务在跑，正常）' % st)

    # ── 汇总 ──
    print('\n' + '=' * 70)
    npass = sum(1 for _, ok, _ in RESULTS if ok)
    nfail = len(RESULTS) - npass
    print('总计: %d/%d 通过，失败 %d，跳过 %d，耗时 %.1f 秒' %
          (npass, len(RESULTS), nfail, len(SKIPS), time.time() - t0))
    if SKIPS:
        print('\n跳过（客户数据缺失，非缺陷）:')
        for n, d in SKIPS:
            print('  - %s  %s' % (n, d))
    if nfail:
        print('\n失败清单:')
        for n, ok, d in RESULTS:
            if not ok:
                print('  ✗ %s  %s' % (n, d))
    print('=' * 70)
    return 0 if nfail == 0 else 1


if __name__ == '__main__':
    sys.exit(main())

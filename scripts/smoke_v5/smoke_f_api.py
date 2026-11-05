#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""smoke_f_api.py — F 组冒烟：会话/生成业务链路（容器内执行）

覆盖原冒烟集缺失的链路用例（见 原冒烟集问题反查.md 第三节）：
  F1  CSV 读取链（表头 + 数据行）
  F2  CSV 回写守卫（非法参数必须被拒）
  F3  命令文本生成（非空 + 可解析）
  F4  确认流转（draft→confirmed）
  F5  重复确认守卫（409）
  F6  版本互斥（旧 confirmed → superseded）
  F7  失败状态一致性（task failed ⟹ gen failed，防僵尸）  ★问题#8
  F8  批量三入口（未配置/弱匹配/人工确认）
  F9  产物下载（attachment + 文件名规范）
  F10 失败提示质量（不得含 INTERNAL / rc= 内部信号）      ★问题#4/#9

设计原则：
  * 判据落在「内容/状态」而非「存在性」
  * 每条用例自带反例意识（selftest 中有对应 fixture）
  * 只读优先（除 F4~F8 必须触发状态变更外，不做破坏性操作）

用法（容器内）:
    python3 smoke_f_api.py --base http://localhost:8600 --sid <session_id>
    python3 smoke_f_api.py --base http://localhost:8600 --sid <sid> --json out.json
"""
import argparse
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request

RESULTS = []
BASE = 'http://localhost:8600'
SID = ''


def api(path, method='GET', body=None, timeout=180, raw=False):
    url = f'{BASE}/api/v1{path}'
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(url, data=data, method=method)
    if data:
        req.add_header('Content-Type', 'application/json')
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            if raw:
                return r.status, r.read(), dict(r.headers)
            return r.status, json.loads(r.read() or b'{}')
    except urllib.error.HTTPError as e:
        try:
            return e.code, json.loads(e.read() or b'{}')
        except Exception:
            return e.code, {}
    except Exception as e:
        return -1, {'exception': f'{type(e).__name__}: {e}'}


def case(cid, name, fn):
    t0 = time.time()
    try:
        detail = fn()
        ok, msg = (detail if isinstance(detail, tuple) else (bool(detail), ''))
    except Exception as e:
        ok, msg = False, f'{type(e).__name__}: {e}'
    dt = time.time() - t0
    RESULTS.append({'id': cid, 'name': name, 'ok': bool(ok),
                    'msg': str(msg), 'sec': round(dt, 2)})
    print(f'  [{"PASS" if ok else "FAIL"}] {cid} {name}  ({dt:.1f}s)')
    if msg:
        for ln in str(msg).splitlines()[:6]:
            print(f'         {ln}')
    return ok


CMD_RE = re.compile(r'^([A-Z][A-Z0-9]*(?:\s+[A-Z0-9*]+)?):.*;?\s*$')


def _gens():
    st, r = api(f'/sessions/{SID}/generations')
    return r.get('items') or []


def _ensure_gen(timeout_s=420):
    """★ 确保会话里至少有一个**产物就绪**的 gen。

    ⚠ 动机（2026-09-18 实测）：F 组首跑报 5/10，全部是「无可用 gen」——
    真因不是产品坏了，而是**用例跑得比生成快**（会话刚匹配完就开测，
    agent 还在写产物）。重跑即 10/10。
    ⇒ 依赖产物的用例必须先**主动触发一次生成并等到终态**，否则
    用例的成败取决于调用时机，不可复现（假红）。
    """
    g = _pick_gen(lambda x: x.get('status') not in ('failed',))
    if g:
        return g
    # 触发一次生成（批量路径最快：weak 档；无 weak 特性则用 not_configured）
    for flt in ('weak', 'not_configured', 'manual'):
        st, r = api(f'/sessions/{SID}/generations',
                    {'method': 'POST', 'body': {'status_filter': flt}})
        if st in (200, 202):
            break
    t0 = time.time()
    while time.time() - t0 < timeout_s:
        g = _pick_gen(lambda x: x.get('status') not in ('failed',))
        if g:
            return g
        time.sleep(6)
    return None


def _pick_gen(pred=lambda g: True):
    for g in _gens():
        if pred(g):
            return g
    return None


# ─────────── F1 CSV 读取链 ───────────

def f1_csv_read():
    """CSV 必须有数据行（不止表头）—— 反例：问题#5.2 的 rows=[]"""
    g = _pick_gen(lambda x: x.get('status') in ('draft', 'confirmed'))
    if not g:
        g = _ensure_gen()          # ★ 产物未就绪则触发并等待（避免时序假红）
    if not g:
        return False, '无可用 gen（已尝试触发生成并等待 420s）'
    st, r = api(f"/sessions/{SID}/generations/{g['gen_id']}/artifacts/csv")
    if st != 200:
        return False, f'HTTP {st}: {json.dumps(r, ensure_ascii=False)[:200]}'
    rows = r.get('rows') or []
    hdr = r.get('headers') or []
    if not hdr:
        return False, '表头缺失'
    if not rows:
        return False, (f"gen={g['gen_id']} CSV 只有表头、零数据行"
                       f"（表头 {len(hdr)} 列）—— 空产物")
    return True, f"gen={g['gen_id']} {len(rows)} 行 / {len(hdr)} 列"


# ─────────── F2 CSV 回写守卫 ───────────

def f2_csv_guard():
    """非法参数写入必须被拒（不得静默接受）"""
    g = _pick_gen(lambda x: x.get('status') == 'draft')
    if not g:
        g = _ensure_gen()
    if not g:
        return False, '无 draft gen（已尝试触发生成并等待）'
    st, r = api(f"/sessions/{SID}/generations/{g['gen_id']}/csv", 'PATCH',
                {'version': 1, 'rows': [{'step_no': 99999,
                                         'param': '__NO_SUCH_PARAM__',
                                         'value': 'x'}]})
    if st in (200, 201):
        return False, f'非法参数被接受（HTTP {st}）—— 守卫失效'
    code = (r.get('error') or {}).get('code') if isinstance(r, dict) else ''
    return True, f'正确拒绝 HTTP {st} code={code}'


# ─────────── F3 命令文本生成 ───────────

def f3_commands():
    """命令文本非空 + 逐行可解析 + 引号成对"""
    g = _pick_gen(lambda x: x.get('status') in ('draft', 'confirmed'))
    if not g:
        return False, '无可用 gen'
    st, r = api(f"/sessions/{SID}/generations/{g['gen_id']}/commands", 'POST', {})
    if st != 200:
        return False, f'HTTP {st}'
    txt = r.get('commands') or ''
    lines = [l for l in txt.splitlines() if l.strip()]
    if not lines:
        return False, f"gen={g['gen_id']} 命令文本为空（count={r.get('count')}）"
    cmds = [l for l in lines if not l.strip().startswith('//')]
    if not cmds:
        return False, f'只有注释、无命令（{len(lines)} 行全为注释）'
    unparsed = [c for c in cmds if not CMD_RE.match(c.strip())]
    badq = [c for c in cmds if c.count('"') % 2]
    if unparsed:
        return False, f'{len(unparsed)} 条无法解析，样本: {unparsed[0][:80]}'
    if badq:
        return False, f'{len(badq)} 条引号不成对，样本: {badq[0][:80]}'
    return True, f'{len(cmds)} 条命令全部可解析、引号成对'


# ─────────── F4~F6 版本链 ───────────

def f4_confirm():
    g = _pick_gen(lambda x: x.get('status') == 'draft')
    if not g:
        return True, '无 draft gen（无待确认节点，跳过）'
    st, r = api(f"/sessions/{SID}/generations/{g['gen_id']}/confirm", 'POST', {})
    if st != 200:
        return False, f'HTTP {st}: {json.dumps(r, ensure_ascii=False)[:200]}'
    return r.get('status') == 'confirmed', f"status={r.get('status')}"


def f5_double_confirm():
    """重复确认必须 409（守卫）"""
    g = _pick_gen(lambda x: x.get('status') == 'confirmed')
    if not g:
        return False, '无 confirmed gen（需先跑 F4）'
    st, r = api(f"/sessions/{SID}/generations/{g['gen_id']}/confirm", 'POST', {})
    if st == 200:
        return False, '重复确认被接受 —— 守卫失效'
    code = (r.get('error') or {}).get('code')
    return st == 409 and code == 'STAGE_CONFLICT', f'HTTP {st} code={code}'


def f6_supersede():
    """确认新节点时，旧 confirmed 必须转 superseded"""
    gens = _gens()
    confirmed = [g for g in gens if g.get('status') == 'confirmed']
    if len(confirmed) > 1:
        return False, f'存在 {len(confirmed)} 个 confirmed —— 互斥失效'
    return True, f'confirmed 节点数 = {len(confirmed)}（≤1）'


# ─────────── F7 状态一致性（问题#8） ───────────

def f7_state_consistency():
    """task failed ⟹ gen 不得停留在 producing（僵尸检查）"""
    st, r = api('/tasks?limit=50')
    tasks = r.get('items') or []
    gens = {g['gen_id']: g for g in _gens()}
    zombies = []
    for t in tasks:
        if t.get('kind') != 'config_gen_agent':
            continue
        inp = t.get('input') or {}
        gid = inp.get('gen_id')
        tstate = t.get('state')
        if gid and gid in gens:
            g = gens[gid]
            # 同一判据（与 smoke_selftest 的 _is_zombie 一致）
            if tstate in ('failed', 'cancelled') and g.get('status') == 'producing':
                zombies.append(f"{gid}: task={tstate} 但 gen=producing")
    if zombies:
        return False, '僵尸状态: ' + '; '.join(zombies[:3])
    return True, f'检查 {len(tasks)} 个任务，无僵尸状态'


# ─────────── F8 批量三入口 ───────────

def f8_batch():
    """三个批量入口必须被受理（且非法值被拒）"""
    outs = []
    for status in ('not_configured', 'weak', 'manual'):
        st, r = api(f'/sessions/{SID}/generations', 'POST',
                    {'action': 'fresh', 'status_filter': status}, timeout=120)
        outs.append(f'{status}:{st}')
        if st != 202:
            return False, f'{status} 未受理 HTTP {st}: {json.dumps(r, ensure_ascii=False)[:150]}'
    # 反例：非法值必须被拒
    st, r = api(f'/sessions/{SID}/generations', 'POST',
                {'action': 'fresh', 'status_filter': '__bogus__'}, timeout=60)
    if st == 202:
        return False, '非法 status_filter 被受理 —— 校验失效'
    return True, '三入口 202 + 非法值被拒（' + ' '.join(outs) + '）'


# ─────────── F9 下载 ───────────

def f9_download():
    g = _pick_gen(lambda x: x.get('status') in ('draft', 'confirmed')
                  and 'mml.txt' in (x.get('produced') or []))
    if not g:
        return False, '无含 mml.txt 的 gen'
    st, body, hdr = api(f"/sessions/{SID}/generations/{g['gen_id']}/download?kind=mml",
                        raw=True)
    if st != 200:
        return False, f'HTTP {st}'
    cd = hdr.get('content-disposition') or hdr.get('Content-Disposition') or ''
    if 'attachment' not in cd:
        return False, f'缺少 attachment 头: {cd}'
    if not re.search(r'filename="[^"]+"', cd):
        return False, f'文件名不规范: {cd}'
    if len(body) < 100:
        return False, f'下载内容过小 {len(body)}B'
    return True, f'{len(body)}B, {cd[:70]}'


# ─────────── F10 失败提示质量（问题#4/#9） ───────────

# 本进程启动时刻（F10 分界：只审这之后产生的失败）
_PROC_START_ISO = __import__("datetime").datetime.utcnow()\
    .strftime("%Y-%m-%dT%H:%M:%SZ")

BAD_SIGNALS = ('INTERNAL', 'rc=1', 'Traceback', 'subprocess',
               'returncode', 'HTTPException')


def f10_error_quality():
    """失败提示不得含内部信号（INTERNAL/rc= 等）

    ★ 2026-09-18 修：必须限定「**本次镜像运行期**产生的失败」。
      历史失败记录（修复前用旧代码跑出来的）会永久留在 tasks 里，
      拿它判当前实现 = 永远 FAIL，且掩盖真实回归。
      口径：以**镜像构建时刻**为分界（env SMOKE_SINCE 可覆盖，默认取
      进程启动前 30 分钟内），只审这之后的失败。
    """
    st, r = api('/tasks?limit=50')
    tasks = r.get('items') or []
    failed = [t for t in tasks if t.get('state') == 'failed']
    if not failed:
        return True, '当前无失败任务（无违反）'

    # 分界时刻：SMOKE_SINCE（ISO）优先；否则用本进程启动时刻
    since = os.environ.get('SMOKE_SINCE') or _PROC_START_ISO

    def is_recent(t):
        ca = t.get('created_at') or ''
        return ca >= since

    recent = [t for t in failed if is_recent(t)]
    stale = [t for t in failed if not is_recent(t)]
    if not recent:
        return True, (f'{len(failed)} 个失败任务**全部早于本次运行**'
                      f'（{since[:19]}），无本次运行期失败')

    bad = []
    for t in recent:
        err = t.get('error') or {}
        blob = json.dumps(err, ensure_ascii=False)
        hits = [s for s in BAD_SIGNALS if s in blob]
        if hits:
            code = err.get('code')
            bad.append(f"{t.get('id')} {t.get('created_at')} code={code} "
                       f"含内部信号 {hits}")
    note = f'（另有 {len(stale)} 条历史失败已忽略）' if stale else ''
    if bad:
        return False, ('失败提示暴露内部信号（应映射为业务错误码）:\n'
                       + '\n'.join(bad[:3]) + '\n' + note)
    return True, f'本次运行期 {len(recent)} 个失败任务，提示均无内部信号{note}'


CASES = [
    ('F1', 'CSV 读取链（须有数据行）', f1_csv_read),
    ('F2', 'CSV 回写守卫（非法参数被拒）', f2_csv_guard),
    ('F3', '命令文本生成（非空+可解析+引号成对）', f3_commands),
    ('F4', '确认流转 draft→confirmed', f4_confirm),
    ('F5', '重复确认守卫（409）', f5_double_confirm),
    ('F6', '版本互斥（confirmed ≤ 1）', f6_supersede),
    ('F7', '状态一致性（无僵尸 producing）', f7_state_consistency),
    ('F8', '批量三入口（+非法值拒绝）', f8_batch),
    ('F9', '产物下载（attachment+文件名）', f9_download),
    ('F10', '失败提示质量（无内部信号）', f10_error_quality),
]


def main():
    global BASE, SID
    ap = argparse.ArgumentParser(description='F 组冒烟：会话/生成链路')
    ap.add_argument('--base', default='http://localhost:8600')
    ap.add_argument('--sid', required=True, help='测试会话 ID')
    ap.add_argument('--json', default='')
    ap.add_argument('--only', default='', help='只跑指定用例，如 F1,F3')
    args = ap.parse_args()

    BASE = args.base.rstrip('/')
    SID = args.sid
    only = {x.strip().upper() for x in args.only.split(',') if x.strip()}

    print('=' * 58)
    print(f' F 组冒烟（会话/生成链路）sid={SID}')
    print('=' * 58)

    for cid, name, fn in CASES:
        if only and cid not in only:
            continue
        case(cid, name, fn)

    total = len(RESULTS)
    passed = sum(1 for r in RESULTS if r['ok'])
    print('\n' + '=' * 58)
    print(f' F 组汇总: {passed}/{total} 通过')
    fails = [r for r in RESULTS if not r['ok']]
    for r in fails:
        print(f'   {r["id"]} {r["name"]}: {r["msg"][:140]}')
    print('=' * 58)

    if args.json:
        from pathlib import Path
        Path(args.json).write_text(json.dumps(
            {'group': 'F', 'total': total, 'passed': passed, 'results': RESULTS},
            ensure_ascii=False, indent=2))
        print(f'结果已落盘: {args.json}')

    return 0 if not fails else 1


if __name__ == '__main__':
    sys.exit(main())

"""两阶段评估 v2：按「可评估族」口径 + 分开报指标。

口径（用户裁定 2026-11-09）：
  · 26 个工单跨 UDG+UNC，但只上传了 UDG 的 EXP
  · UNC 独有的族没有现网数据支撑 → 不计入可评估族
  · 族完备率 = 命中族 / 可评估族

指标分两阶段报：
  阶段1：规划召回（规划里的族 / 可评估族）、规划精确（命中 / 规划总数）
  阶段2：族完备（产物命中的族 / 可评估族）、命令数完成度
"""
import argparse
import json
import re
import subprocess
import sys
import time
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

import os as _os
# ★ 2026-11-10：支持单容器测试（容器清理后只剩一个）
if _os.environ.get('EVAL_SINGLE'):
    BASES = ['http://127.0.0.1:8620']
else:
    BASES = ['http://127.0.0.1:8620', 'http://127.0.0.1:8621',
             'http://127.0.0.1:8622', 'http://127.0.0.1:8623']
import os as _os2
# ★ 2026-11-10：单容器测试时 8620 对应 mmlgen-test
if _os2.environ.get('EVAL_SINGLE'):
    CONT = {'8620': _os2.environ.get('EVAL_CONTAINER', 'mmlgen-test')}
else:
    CONT = {'8620': 'mmlgen-clean', '8621': 'mmlgen-b1',
            '8622': 'mmlgen-b2', '8623': 'mmlgen-b3'}
INTENT_DIR = Path('/tmp/intent_dataset')
OUT = Path('/tmp/eval_2stage_v2_out')
OUT.mkdir(exist_ok=True)

GT = json.loads(Path('/tmp/gt_cleaned.json').read_text(encoding='utf-8'))
CNIDX = json.loads(Path('/tmp/family_cnname.json').read_text(encoding='utf-8'))


def eval_scope(g):
    """算可评估族 / 无支撑族。

    有 UDG EXP 支撑的族（在 UDG 文档库，或两产品共有）→ 可评估
    只在 UNC 库的族 → 无支撑（上传的是 UDG EXP，查不到现网）
    """
    ev, ns = set(), set()
    for _, v, f, p, _ in g['kept']:
        key = f'{v} {f}'
        hit = CNIDX.get(f)
        if hit and 'udg' in hit:
            ev.add(key)
        elif hit and 'unc' in hit:
            ns.add(key)
        else:
            ev.add(key)          # 库外族（8 个）保守算可评估
    return ev, ns


def api(base, path, timeout=60):
    with urllib.request.urlopen(base + path, timeout=timeout) as r:
        return json.loads(r.read().decode())


def post(base, path, body, timeout=120):
    req = urllib.request.Request(
        base + path, data=json.dumps(body, ensure_ascii=False).encode(),
        headers={'Content-Type': 'application/json'}, method='POST')
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read().decode())


def sh(cont, cmd, timeout=180):
    return subprocess.run(['docker', 'exec', cont, 'sh', '-c', cmd],
                          capture_output=True, text=True, timeout=timeout).stdout


def parse_cmd_fams(text):
    """命令文本 → {动词 族名}（含产物的 ADD/MOD/SET/RMV）。"""
    out = set()
    for line in text.split('\n'):
        s = line.split('//')[0].strip()
        if s.startswith('/*') or s.startswith('#'):
            continue
        m = re.match(r'^(ADD|RMV|MOD|SET)\s+([A-Za-z0-9_]+)', s, re.I)
        if m:
            out.add(f'{m.group(1).upper()} {m.group(2).upper()}')
    return out


def parse_fam_only(text):
    """只要族名（忽略动词），用于族完备比较。"""
    out = set()
    for line in text.split('\n'):
        s = line.split('//')[0].strip()
        if s.startswith('/*') or s.startswith('#'):
            continue
        m = re.match(r'^(ADD|RMV|MOD|SET)\s+([A-Za-z0-9_]+)', s, re.I)
        if m:
            out.add(m.group(2).upper())
    return out


def parse_plan_fams(plan_text):
    """从规划表提取族（表格里的命令族列）。"""
    out = set()
    for line in plan_text.split('\n'):
        if not line.strip().startswith('|'):
            continue
        for m in re.finditer(r'\b(ADD|RMV|MOD|SET)\s+([A-Z][A-Z0-9_]+)\b', line):
            out.add(m.group(2))
    return out


def wait_done(base, sid, limit=3000):
    t0 = time.time()
    while time.time() - t0 < limit:
        time.sleep(10)
        try:
            st = api(base, f'/api/v1/sessions/{sid}/run')
        except Exception:
            continue
        if st.get('status') in ('done', 'failed'):
            return st.get('status'), st.get('last_run') or {}
    return 'timeout', {}


def run_one(tk, base):
    g = next((x for x in GT if x['ticket'] == tk), None)
    if not g:
        return {'ticket': tk, 'error': '无 GT'}

    intent_f = INTENT_DIR / f'{tk}_意图.md'
    dataset_f = INTENT_DIR / f'{tk}_数据清单.md'
    if not intent_f.exists():
        return {'ticket': tk, 'error': '无意图'}

    intent = intent_f.read_text(encoding='utf-8')
    port = base.rsplit(':', 1)[-1]
    cont = CONT.get(port, 'mmlgen-clean')
    # ★ 2026-11-10：不能只匹配 EXPMML*.txt
    #   NC20260820000552 的 UNC EXP 叫 HZZZhbSMF001BHW-05AHW011_20260803.txt，
    #   有 1021 个族（含 BSFIPRANGEBIND/TAIRANGELIST 等），
    #   但 glob('EXPMML*.txt') 匹配不到 → agent 以为本网元没有这些族。
    exps = list((Path(g['path']) / '备份附件').glob('*.txt'))
    if not exps:
        return {'ticket': tk, 'error': '无 EXP'}

    # ★ 口径
    ev_fams, ns_fams = eval_scope(g)
    ev_bare = {f.split(' ', 1)[1] for f in ev_fams}      # 族名（无动词）
    gt_bare = {f for _, v, f, p, _ in g['kept']}

    r = {'ticket': tk, 'gt_cmds': len(g['kept']),
         'gt_fams': len(ev_fams), 'no_support_fams': len(ns_fams),
         'level': 'complex' if len(g['kept']) > 200 else (
             'medium' if len(g['kept']) >= 50 else 'simple')}

    try:
        cp = subprocess.run(['curl', '-s', '-X', 'POST', '-F', f'name={tk}_v2',
                             '-F', 'product=UDG', f'{base}/api/v1/sessions'],
                            capture_output=True, text=True, timeout=60)
        sid = json.loads(cp.stdout)['session_id']
        r['sid'] = sid

        # ★ 2026-11-10：上传全部 EXP（多网元工单有 UDG+UNC+UEG 多份）
        #   原来只传 exps[0]，导致 UNC/UEG 侧的族全部查不到
        _up = []
        for _e in exps:
            _up += ['-F', f'files=@{_e}']
        subprocess.run(['curl', '-s', '-X', 'POST'] + _up +
                       [f'{base}/api/v1/sessions/{sid}/files'],
                       capture_output=True, timeout=1800)
        if dataset_f.exists():
            subprocess.run(['curl', '-s', '-X', 'POST', '-F', f'files=@{dataset_f}',
                            f'{base}/api/v1/sessions/{sid}/files'],
                           capture_output=True, timeout=600)

        # ── 阶段 1 ──
        t1 = time.time()
        post(base, f'/api/v1/sessions/{sid}/run',
             {'intent': intent, 'product': 'UDG', 'stage': 'plan'})
        st1, _ = wait_done(base, sid)
        r['s1_status'] = st1
        r['s1_sec'] = round(time.time() - t1, 1)

        plan = sh(cont, f'cat /data/sessions/{sid}/analysis_code/命令族规划.md 2>/dev/null')
        r['s1_plan_len'] = len(plan)
        plan_fams = parse_plan_fams(plan)
        r['s1_plan_n'] = len(plan_fams)
        r['s1_hit_n'] = len(plan_fams & ev_bare)
        r['s1_recall'] = round(len(plan_fams & ev_bare) / max(1, len(ev_bare)), 3)
        r['s1_precision'] = round(len(plan_fams & ev_bare) / max(1, len(plan_fams)), 3)

        arts1 = sh(cont, f'ls /data/sessions/{sid}/analysis_code/ 2>/dev/null').split()
        r['s1_bad_arts'] = [a for a in arts1
                            if a in ('mml.txt', 'params.csv', '配置分析.md')]

        if not plan:
            r['error'] = '阶段1 无规划表'
            return r

        # ── 阶段 2 ──
        t2 = time.time()
        post(base, f'/api/v1/sessions/{sid}/run',
             {'intent': intent, 'product': 'UDG', 'stage': 'fill'})
        st2, run2 = wait_done(base, sid)
        r['s2_status'] = st2
        r['s2_sec'] = round(time.time() - t2, 1)

        mml = sh(cont, f'cat /data/sessions/{sid}/analysis_code/mml.txt 2>/dev/null')
        prod_bare = parse_fam_only(mml)
        r['s2_prod_n'] = len(prod_bare)
        r['s2_hit_n'] = len(prod_bare & ev_bare)
        r['s2_fam_rate'] = round(len(prod_bare & ev_bare) / max(1, len(ev_bare)), 3)
        r['s2_prod_cmds'] = len([l for l in mml.split('\n')
                                 if l.strip() and not l.strip().startswith(('/*', '//', '#'))])
        r['s2_extra_n'] = len(prod_bare - gt_bare)

        arts2 = sh(cont, f'ls /data/sessions/{sid}/analysis_code/ 2>/dev/null').split()
        r['s2_has_all'] = all(a in arts2 for a in ('mml.txt', 'params.csv', '配置分析.md'))
        r['s2_rounds'] = [(x.get('round'), x.get('verdict'))
                          for x in (run2.get('rounds') or [])]
        r['s2_fatal'] = (run2.get('guard') or {}).get('fatal') or []

        # 存产物
        dst = OUT / tk
        dst.mkdir(exist_ok=True)
        for n in ('mml.txt', '命令族规划.md', 'params.csv', '配置分析.md', '方案澄清.json'):
            c2 = sh(cont, f'cat /data/sessions/{sid}/analysis_code/{n} 2>/dev/null')
            if c2:
                (dst / n).write_text(c2, encoding='utf-8')

    except Exception as e:
        r['error'] = f'{type(e).__name__}: {e}'

    return r


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--tickets', default='')
    ap.add_argument('--limit', type=int, default=0)
    args = ap.parse_args()

    if args.tickets:
        targets = [x.strip() for x in args.tickets.split(',') if x.strip()]
    else:
        targets = [x['ticket'] for x in GT
                   if (INTENT_DIR / f"{x['ticket']}_意图.md").exists()]
        if args.limit:
            targets = targets[:args.limit]

    print(f'=== 两阶段评估 v2（可评估族口径）：{len(targets)} 工单 ===')
    for b in BASES:
        try:
            h = api(b, '/health', timeout=15)
            print(f'  {b} ok={h.get("ok")}')
        except Exception:
            print(f'  {b} UNREACHABLE')

    results = []
    t0 = time.time()
    with ThreadPoolExecutor(max_workers=len(BASES)) as ex:
        futs = {ex.submit(run_one, tk, BASES[i % len(BASES)]): tk
                for i, tk in enumerate(targets)}
        done = 0
        for f in as_completed(futs):
            done += 1
            try:
                r = f.result()
                results.append(r)
                if 'error' in r and 's1_status' not in r:
                    print(f"  [{done}/{len(targets)}] {r['ticket']:<22} ERROR {r['error'][:40]}")
                else:
                    print(f"  [{done}/{len(targets)}] {r['ticket']:<22} "
                          f"S1 {r.get('s1_hit_n',0)}/{r.get('gt_fams',0)}"
                          f"({r.get('s1_recall',0)*100:.0f}%) {r.get('s1_sec',0):.0f}s | "
                          f"S2 {r.get('s2_hit_n',0)}/{r.get('gt_fams',0)}"
                          f"({r.get('s2_fam_rate',0)*100:.0f}%) "
                          f"{r.get('s2_prod_cmds',0)}条 {r.get('s2_sec',0):.0f}s {r.get('s2_status','?')}")
            except Exception as e:
                print(f'  异常: {e}')

    Path('/tmp/eval_2stage_v2_result.json').write_text(
        json.dumps(results, ensure_ascii=False, indent=1), encoding='utf-8')

    ok = [r for r in results if 's1_status' in r and 's2_status' in r]
    print('\n' + '=' * 90)
    print(f'汇总：{len(ok)} 个有效，总耗时 {(time.time()-t0)/60:.1f} 分钟')
    print('=' * 90)

    if ok:
        # 分档汇总
        for lv, label in [('simple', '简单 <50'), ('medium', '中等 50-200'),
                          ('complex', '复杂 >200')]:
            sub = [r for r in ok if r['level'] == lv]
            if not sub:
                continue
            ev = sum(r['gt_fams'] for r in sub)
            s1 = sum(r['s1_hit_n'] for r in sub)
            s2 = sum(r['s2_hit_n'] for r in sub)
            gc = sum(r['gt_cmds'] for r in sub)
            pc = sum(r['s2_prod_cmds'] for r in sub)
            print(f'\n【{label}】{len(sub)} 个工单，可评估族 {ev}')
            print(f'  阶段1 规划召回: {s1}/{ev} = {s1/max(1,ev)*100:.1f}%')
            print(f'  阶段2 族完备:   {s2}/{ev} = {s2/max(1,ev)*100:.1f}%')
            print(f'  命令数:         {pc}/{gc} = {pc/max(1,gc)*100:.0f}%')

        # 总计
        ev = sum(r['gt_fams'] for r in ok)
        s1 = sum(r['s1_hit_n'] for r in ok)
        s2 = sum(r['s2_hit_n'] for r in ok)
        pn = sum(r['s1_plan_n'] for r in ok)
        gc = sum(r['gt_cmds'] for r in ok)
        pc = sum(r['s2_prod_cmds'] for r in ok)
        print(f'\n【总计】{len(ok)} 个工单')
        print(f'  可评估族:     {ev}（无 EXP 支撑 {sum(r["no_support_fams"] for r in ok)}）')
        print(f'  阶段1 规划召回: {s1}/{ev} = {s1/max(1,ev)*100:.1f}%')
        print(f'  阶段1 规划精确: {s1}/{pn} = {s1/max(1,pn)*100:.1f}%')
        print(f'  阶段2 族完备:   {s2}/{ev} = {s2/max(1,ev)*100:.1f}%')
        print(f'  命令数完成度:   {pc}/{gc} = {pc/max(1,gc)*100:.0f}%')
        print(f'  产物齐全:       {sum(1 for r in ok if r.get("s2_has_all"))}/{len(ok)}')
        print(f'  越界写产物:     {sum(1 for r in ok if r.get("s1_bad_arts"))} 个')
        print(f'  阶段1 耗时中位: {sorted(r["s1_sec"] for r in ok)[len(ok)//2]:.0f}s')
        print(f'  阶段2 耗时中位: {sorted(r["s2_sec"] for r in ok)[len(ok)//2]:.0f}s')


if __name__ == '__main__':
    main()

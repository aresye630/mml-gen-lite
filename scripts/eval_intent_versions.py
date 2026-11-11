#!/usr/bin/env python3
"""V2/V3/V4 三版意图对比评测（20 单 × 3 版 = 60 次运行）。

用法：
  python3 eval_intent_versions.py            # 跑全部
  python3 eval_intent_versions.py --versions V4   # 只跑某版

输出：
  /tmp/eval_versions_out/<VERSION>/<ticket>/{命令族规划.md, mml.txt, ...}
  /tmp/eval_versions_result.json
"""
import argparse
import json
import re
import shutil
import subprocess
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

GT = json.loads(Path('/tmp/gt_cleaned.json').read_text(encoding='utf-8'))
GT_MAP = {g['ticket']: g for g in GT}

VERSIONS = {
    'V2': Path('/tmp/intent_dataset'),
    'V3': Path('/tmp/intent_v3'),
    'V4': Path('/tmp/intent_v4'),
    'V5': Path('/tmp/intent_v5'),
}
OUT = Path('/tmp/eval_versions_out')
RES = Path('/tmp/eval_versions_result.json')

BASES = ['http://127.0.0.1:8620', 'http://127.0.0.1:8621',
         'http://127.0.0.1:8622', 'http://127.0.0.1:8623']
CONT = {'8620': 'mmlgen-clean', '8621': 'mmlgen-b1',
        '8622': 'mmlgen-b2', '8623': 'mmlgen-b3'}


def api(base, path, method='GET', data=None, timeout=120):
    cmd = ['curl', '-s', '-X', method, f'{base}{path}']
    if data is not None:
        cmd += ['-H', 'Content-Type: application/json', '-d', json.dumps(data)]
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
    try:
        return json.loads(r.stdout)
    except Exception:
        return {'_raw': r.stdout[:300]}


def post(base, path, data, timeout=300):
    return api(base, path, 'POST', data, timeout)


def upload(base, files):
    cmd = ['curl', '-s', '-X', 'POST']
    for f in files:
        cmd += ['-F', f'files=@{f}']
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=1800)
    return r.stdout


def wait_done(base, sid, max_wait=None):
    """等任务完成。

    ★ 2026-11-11：max_wait 原来固定 3600s，实测 NC20260914002657 卡死后
      整个线程池拖了 1 小时，后面的单都进不来。
      改为按 GT 规模分档（与 agent_run 的 ROUND_HARD_LIMIT 对齐）：
        <50 条   900s
        50-200   1500s
        200-800  1800s
        >800     2400s
      再加 200s 缓冲（agent 的 guard/采集时间）。
    """
    if max_wait is None:
        max_wait = 1200
    t0 = time.time()
    while time.time() - t0 < max_wait:
        st = api(base, f'/api/v1/sessions/{sid}/run')
        if st.get('status') in ('done', 'failed'):
            return st.get('status'), st.get('last_run') or {}
        time.sleep(8)
    return 'timeout', {}


def run_one(tk, ver, base):
    g = GT_MAP.get(tk)
    if not g:
        return {'ticket': tk, 'version': ver, 'error': '无 GT'}

    idir = VERSIONS[ver]
    intent_f = idir / f'{tk}_意图.md'
    ds_f = idir / f'{tk}_数据清单.md'
    if not intent_f.exists():
        return {'ticket': tk, 'version': ver, 'error': '无意图'}

    intent = intent_f.read_text(encoding='utf-8')
    port = base.rsplit(':', 1)[-1]

    # 收集 EXP
    adir = Path(g['path']) / '备份附件'
    exps = sorted(adir.glob('*.txt')) if adir.exists() else []
    if not exps:
        return {'ticket': tk, 'version': ver, 'error': '无 EXP'}

    r = {'ticket': tk, 'version': ver, 'gt_cmds': len(g['kept']),
         'gt_fams': len({f for _, _, f, _, _ in g['kept']})}

    # ★ 2026-11-11：断点续跑。已有产物就跳过，避免重跑浪费。
    _exist = OUT / ver / tk / 'mml.txt'
    _exist_plan = OUT / ver / tk / '命令族规划.md'
    if _exist.exists() or _exist_plan.exists():
        r['skipped'] = True
        r['s1_status'] = 'cached'
        r['s2_status'] = 'cached'
        return r

    try:
        cp = subprocess.run(['curl', '-s', '-X', 'POST',
                             '-F', f'name={tk}_{ver}',
                             '-F', 'product=UDG',
                             f'{base}/api/v1/sessions'],
                            capture_output=True, text=True, timeout=60)
        sid = json.loads(cp.stdout)['session_id']
        r['sid'] = sid

        files = list(exps)
        if ds_f.exists():
            files.append(ds_f)
        upload(base, files)

        # 阶段1
        t1 = time.time()
        post(base, f'/api/v1/sessions/{sid}/run',
             {'intent': intent, 'product': 'UDG', 'stage': 'plan'})
        # 阶段1 只做规划，耗时约为阶段2 的 1/2，给一半额度
        _n = len(g['kept'])
        _base = 900 if _n < 50 else (1500 if _n < 200 else (1800 if _n < 800 else 2400))
        st1, _ = wait_done(base, sid, max_wait=_base // 2 + 200)
        r['s1_status'] = st1
        r['s1_sec'] = round(time.time() - t1)

        if st1 == 'done':
            # 阶段2
            t2 = time.time()
            post(base, f'/api/v1/sessions/{sid}/run',
                 {'intent': intent, 'product': 'UDG', 'stage': 'fill'})
            st2, _ = wait_done(base, sid, max_wait=_base + 200)
            r['s2_status'] = st2
            r['s2_sec'] = round(time.time() - t2)

        # 采集产物
        ddir = OUT / ver / tk
        ddir.mkdir(parents=True, exist_ok=True)
        for fname in ['命令族规划.md', 'mml.txt', 'params.csv',
                      '配置分析.md', '方案澄清.json']:
            subprocess.run(['docker', 'cp',
                            f'{CONT[port]}:/data/sessions/{sid}/analysis_code/{fname}',
                            str(ddir / fname)],
                           capture_output=True, timeout=120)

        # 采集期间不能删会话（下一单还要建），最后统一清
    except Exception as e:
        r['error'] = f'{type(e).__name__}: {e}'

    return r


def parse_plan_fams(plan_text):
    out = set()
    if not plan_text:
        return out
    lines = plan_text.split('\n')
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if not line.startswith('|'):
            i += 1
            continue
        header = [c.strip() for c in line.strip().strip('|').split('|')]
        if '命令族' not in header:
            i += 1
            continue
        fam_i = header.index('命令族')
        st_i = header.index('状态') if '状态' in header else None
        ncol = len(header)
        i += 1
        if i < len(lines) and re.fullmatch(r'[|\s\-:]+', lines[i].strip()):
            i += 1
        while i < len(lines):
            row = lines[i].strip()
            if not row.startswith('|'):
                break
            cells = [c.strip() for c in row.strip().strip('|').split('|')]
            if len(cells) >= ncol:
                status = cells[st_i] if (st_i is not None and st_i < ncol) else ''
                if '跳过' not in status:
                    for part in re.split(r'[/,、]', cells[fam_i]):
                        t = part.strip().upper()
                        m = re.match(r'^(?:ADD|RMV|MOD|SET)\s+([A-Z][A-Z0-9_]{2,})$', t)
                        if m:
                            out.add(m.group(1))
                        elif re.fullmatch(r'[A-Z][A-Z0-9_]{2,}', t):
                            out.add(t)
            i += 1
        continue
    return out


def parse_cmd_fams(text):
    c = set()
    for line in text.split('\n'):
        s = line.split('//')[0].strip()
        if s.startswith(('/*', '#', '*')):
            continue
        m = re.match(r'^(ADD|RMV|MOD|SET)\s+([A-Za-z0-9_]+)', s, re.I)
        if m:
            c.add(m.group(2).upper())
    return c


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--versions', default='V2,V3,V4')
    ap.add_argument('--tickets', default='')
    args = ap.parse_args()

    vers = [x.strip() for x in args.versions.split(',') if x.strip()]
    if args.tickets:
        tks = [x.strip() for x in args.tickets.split(',') if x.strip()]
    else:
        tks = json.loads(Path('/tmp/eval20_tickets.json').read_text(encoding='utf-8'))

    print(f'=== 意图版本对比评测：{len(tks)} 单 × {len(vers)} 版 = '
          f'{len(tks) * len(vers)} 次 ===')

    for b in BASES:
        try:
            h = api(b, '/health', timeout=15)
            print(f'  {b} ok={h.get("ok")}')
        except Exception:
            print(f'  {b} UNREACHABLE')

    # 构造任务队列：按版本分组，每版本内 4 容器并发
    # ★ 2026-11-11：读已有结果，避免覆盖（断点续跑）
    results = []
    if RES.exists():
        try:
            old = json.loads(RES.read_text(encoding='utf-8'))
            results = [x for x in old
                       if not (x['version'] in vers and x['ticket'] in tks)]
        except Exception:
            results = []
    for ver in vers:
        print(f'\n{"="*70}\n{ver}\n{"="*70}')
        OUT.joinpath(ver).mkdir(parents=True, exist_ok=True)
        t0 = time.time()
        with ThreadPoolExecutor(max_workers=4) as ex:
            futs = {ex.submit(run_one, tk, ver, BASES[i % 4]): tk
                    for i, tk in enumerate(tks)}
            for f in futs:
                try:
                    r = f.result()
                except Exception as e:
                    r = {'ticket': futs[f], 'version': ver,
                         'error': f'{type(e).__name__}: {e}'}
                results.append(r)
                el = time.time() - t0
                print(f'  [{len(results):>3}] {r["ticket"]:<22} '
                      f'S1 {r.get("s1_status","-"):<8} '
                      f'S2 {r.get("s2_status","-"):<8} '
                      f'{el:>6.0f}s')
                RES.write_text(json.dumps(results, ensure_ascii=False, indent=1),
                               encoding='utf-8')

    print(f'\n总计 {len(results)} 次，已存 {RES}')


if __name__ == '__main__':
    main()

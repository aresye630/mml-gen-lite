#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""M3 分段计时：逐段量真实耗时，找出真热点（不靠 P1~P7 的旧估算）。

用法: python3 m3_stage_timing.py [--product UDG] [--sid <sid>]
"""
import argparse
import os
import subprocess
import sys
import tempfile
import time
from pathlib import Path

SCRIPTS = Path('/opt/expgv/scripts')
PIPE = SCRIPTS / 'exp_analysis_code'   # 与 det_check 单一真相源一致


def _cfg(product):
    """复用 det_check 的产品配置（单一真相源）"""
    sys.path.insert(0, '/opt/expgv/scripts')
    import det_check as D
    return D._cfg(product)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--product', default='UDG')
    ap.add_argument('--sid', default='20260918_UDG_sess_27aa')
    ap.add_argument('--sid-root', default='/data/sessions')
    a = ap.parse_args()

    root = Path(a.sid_root) / a.sid / 'exp_v1'
    cands = sorted(root.glob('*.txt'))
    if not cands:
        print(f'⛔ {root} 无 EXP')
        return 2
    exp = str(cands[0])
    print(f'EXP: {Path(exp).name}')
    print(f'  大小 {Path(exp).stat().st_size/1024/1024:.2f} MB')
    print(f'  产品 {a.product}')
    print()

    c = _cfg(a.product)
    env = dict(os.environ)
    env['PYTHONHASHSEED'] = '0'

    with tempfile.TemporaryDirectory(prefix='m3t_') as td:
        out = Path(td) / 'out'
        acd = out / 'analysis_code'
        gt = out / '特性配置基线'
        acd.mkdir(parents=True, exist_ok=True)
        gt.mkdir(parents=True, exist_ok=True)

        stages = [
            ('① feature_relations', [sys.executable, SCRIPTS / 'feature_relations.py',
                                     '--feat-dir', c['feat_dir'], '--exp', exp, '-o', out,
                                     '--anchors', c['anchors'], '--rel-rules', c['rel_rules']], None),
            ('② pipeline', [sys.executable, PIPE / 'pipeline.py', exp, '-o', acd], PIPE),
            ('③ feature_chain_map', [sys.executable, PIPE / 'feature_chain_map.py',
                                     '--chains', PIPE / 'rules' / 'chain_schemas.yaml',
                                     '--features', c['fingerprint'], '--product', a.product,
                                     '-o', acd / 'feature_chains.json'], PIPE),
            ('④a match_features', [sys.executable, SCRIPTS / 'match_features.py',
                                   '--product', a.product, '--exp', exp,
                                   '--fingerprint', c['fingerprint'], '-o', out,
                                   '--anchors', c['anchors']], None),
            ('④b gen_feature_all', [sys.executable, SCRIPTS / 'gen_feature_all.py',
                                    '--feat-dir', c['feat_dir'], '--exp', exp, '-o', gt,
                                    '--anchors', c['anchors']], None),
        ]

        total = 0.0
        rows = []
        for name, cmd, cwd in stages:
            t0 = time.perf_counter()
            r = subprocess.run([str(x) for x in cmd], capture_output=True,
                               text=True, env=env, cwd=str(cwd) if cwd else None)
            dt = time.perf_counter() - t0
            total += dt
            ok = '✓' if r.returncode == 0 else f'✗ rc={r.returncode}'
            rows.append((name, dt, ok))
            print(f'  {name:24s} {dt:8.2f}s  {ok}')
            if r.returncode != 0:
                tail = (r.stderr or r.stdout or '')[-200:]
                print(f'      {tail.strip()[:180]}')

        print()
        print(f'  {"合计":24s} {total:8.2f}s')
        print()
        print('  占比:')
        for name, dt, ok in sorted(rows, key=lambda x: -x[1]):
            print(f'    {name:24s} {dt/total*100:5.1f}%  ({dt:.2f}s)')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

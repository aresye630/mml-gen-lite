#!/usr/bin/env python3
"""V2/V3/V4 三版意图对比统计（按单口径）。

用户裁定：所有覆盖率/达标率的分子分母单位都是「单」。
"""
import json
import re
import statistics
from collections import Counter, defaultdict
from pathlib import Path

GT = json.loads(Path('/tmp/gt_cleaned.json').read_text(encoding='utf-8'))
GT_MAP = {g['ticket']: g for g in GT}
OUT = Path('/tmp/eval_versions_out')
RES = json.loads(Path('/tmp/eval_versions_result.json').read_text(encoding='utf-8'))


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


def read(p):
    return p.read_text(encoding='utf-8', errors='replace') if p.exists() else ''


rows = []
for r in RES:
    tk, ver = r['ticket'], r['version']
    g = GT_MAP.get(tk)
    if not g:
        continue
    gt_fams = {f for _, _, f, _, _ in g['kept']}
    d = OUT / ver / tk
    plan = parse_plan_fams(read(d / '命令族规划.md'))
    prod = parse_cmd_fams(read(d / 'mml.txt'))
    n_gt = len(gt_fams)
    n1 = len(gt_fams & plan)
    n2 = len(gt_fams & prod)
    rows.append({
        'tk': tk, 'ver': ver, 'n_gt': n_gt,
        'n1': n1, 'n2': n2,
        'r1': n1 / max(1, n_gt), 'r2': n2 / max(1, n_gt),
        's1': r.get('s1_status'), 's2': r.get('s2_status'),
        'sec': (r.get('s1_sec') or 0) + (r.get('s2_sec') or 0),
        'level': ('large' if len(g['kept']) > 200
                  else ('mid' if len(g['kept']) >= 50 else 'small')),
        'has_prod': n2 > 0 or bool(prod),
    })

by_ver = defaultdict(list)
for r in rows:
    by_ver[r['ver']].append(r)

print('=' * 84)
print('三版意图对比（20 单 × 3 版，按单统计）')
print('=' * 84)

print(f"\n{'版本':<6} {'单数':>4} {'阶段1达标':>10} {'阶段2达标':>10} "
      f"{'阶段2中位覆盖':>12} {'平均覆盖':>8}")
print('-' * 60)
stats = {}
for ver in ['V2', 'V3', 'V4', 'V5']:
    rs = by_ver.get(ver) or []
    if not rs:
        continue
    n = len(rs)
    p1 = sum(1 for r in rs if r['r1'] >= 0.9999)
    p2 = sum(1 for r in rs if r['r2'] >= 0.9999)
    med = statistics.median(r['r2'] for r in rs) * 100
    mean = sum(r['r2'] for r in rs) / n * 100
    stats[ver] = {'n': n, 'p1': p1, 'p2': p2, 'med': med, 'mean': mean,
                  'rate1': p1 / n, 'rate2': p2 / n}
    print(f"{ver:<6} {n:>4} {p1:>4}/{n:<3}={p1/n*100:>5.1f}% "
          f"{p2:>4}/{n:<3}={p2/n*100:>5.1f}% {med:>10.1f}% {mean:>7.1f}%")

# 分档
print(f"\n{'='*84}")
print('分档对比（阶段2 达标率）')
print('=' * 84)
print(f"{'档位':<10} {'V2':>13} {'V3':>13} {'V4':>13} {'V5':>13}")
print('-' * 60)
for lv, name in [('small', '小 <50'), ('mid', '中 50-200'), ('large', '大 >200')]:
    line = f"{name:<10}"
    for ver in ['V2', 'V3', 'V4', 'V5']:
        rs = [r for r in (by_ver.get(ver) or []) if r['level'] == lv]
        if not rs:
            line += f"{'—':>14}"
            continue
        p = sum(1 for r in rs if r['r2'] >= 0.9999)
        line += f"{p:>3}/{len(rs):<3}={p/len(rs)*100:>4.1f}%  "
    print(line)

# 逐单对比
print(f"\n{'='*110}")
print('逐单对比（阶段2 族覆盖）')
print('=' * 110)
tks = sorted({r['tk'] for r in rows},
             key=lambda t: -(len(GT_MAP[t]['kept']) if t in GT_MAP else 0))
print(f"{'工单':<22} {'GT条':>5} {'GT族':>4} | "
      f"{'V2':>10} {'V3':>10} {'V4':>10} {'V5':>10}")
print('-' * 74)
m = {v: {r['tk']: r for r in (by_ver.get(v) or [])} for v in ['V2', 'V3', 'V4', 'V5']}
better = {'V4>V2': 0, 'V4<V2': 0, 'same': 0}
for tk in tks:
    g = GT_MAP.get(tk)
    if not g:
        continue
    cells = []
    v4r = v2r = None
    for v in ['V2', 'V3', 'V4', 'V5']:
        r = m[v].get(tk)
        if not r:
            cells.append(f"{'—':>12}")
            continue
        sc = f"{r['n2']}/{r['n_gt']}"
        cells.append(f"{sc:>12}")
        if v == 'V2':
            v2r = r['r2']
        if v == 'V4':
            v4r = r['r2']
    if v2r is not None and v4r is not None:
        if v4r > v2r + 0.001:
            better['V4>V2'] += 1
        elif v4r < v2r - 0.001:
            better['V4<V2'] += 1
        else:
            better['same'] += 1
    print(f"{tk:<22} {len(g['kept']):>5} {len({f for _,_,f,_,_ in g['kept']}):>4} | "
          + ' '.join(cells))

print(f"\n=== V4 vs V2 逐单变化 ===")
print(f"  V4 更好:  {better['V4>V2']} 单")
print(f"  V4 更差:  {better['V4<V2']} 单")
print(f"  持平:     {better['same']} 单")

Path('/tmp/versions_compare.json').write_text(
    json.dumps({'rows': rows, 'stats': stats, 'better': better},
               ensure_ascii=False, indent=1), encoding='utf-8')
print(f"\n已存 /tmp/versions_compare.json")

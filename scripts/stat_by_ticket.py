#!/usr/bin/env python3
"""按单统计（用户裁定 2026-11-10）。

★ 核心规则：
  「所有的准确率、覆盖率，只要出现统计，分子分母的单位就是单数」
  —— 不能是命令族和命令。

即：
  覆盖率 = 达标工单数 / 总工单数
  不再出现「559/903 族」这种按族汇总的写法。

两种口径：
  A 全量
  B 排除数据受限（缺 SET/MOD/RMV 现网数据的工单）

每个工单的指标：
  阶段1 规划覆盖 = 规划命中族 / 该单 GT 族（该单内部的百分比）
  阶段2 产物覆盖 = 产物命中族 / 该单 GT 族
  判定「达标」= 该单的百分比 100%
"""
import argparse
import json
import re
import statistics
from pathlib import Path

GT = json.loads(Path('/tmp/gt_cleaned.json').read_text(encoding='utf-8'))
GT_MAP = {g['ticket']: g for g in GT}


def load_restricted():
    p = Path('/tmp/missing_classified.json')
    if not p.exists():
        return set()
    cls = json.loads(p.read_text(encoding='utf-8'))
    return {x['tk'] for x in cls.get('need_data') or []}


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
        fam_idx = header.index('命令族')
        st_idx = header.index('状态') if '状态' in header else None
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
                status = cells[st_idx] if (st_idx is not None and st_idx < ncol) else ''
                if '跳过' not in status:
                    for part in re.split(r'[/,、]', cells[fam_idx]):
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


def collect(out_dir):
    rows = []
    d = Path(out_dir)
    if not d.exists():
        return rows
    for sub in sorted(d.iterdir()):
        if not sub.is_dir():
            continue
        tk = sub.name
        g = GT_MAP.get(tk)
        if not g:
            continue
        gt_fams = {f for _, v, f, _, _ in g['kept']}
        if not gt_fams:
            continue

        plan_p = sub / '命令族规划.md'
        mml_p = sub / 'mml.txt'
        if not plan_p.exists() and not mml_p.exists():
            continue   # 无产物，不计入

        plan = parse_plan_fams(plan_p.read_text(encoding='utf-8', errors='replace')
                               if plan_p.exists() else '')
        prod = parse_cmd_fams(mml_p.read_text(encoding='utf-8', errors='replace')
                              if mml_p.exists() else '')

        n_gt = len(gt_fams)
        n1 = len(gt_fams & plan)
        n2 = len(gt_fams & prod)

        rows.append({
            'tk': tk,
            'n_gt': n_gt,
            'n1': n1,
            'n2': n2,
            'r1': n1 / n_gt,
            'r2': n2 / n_gt,
            'level': ('complex' if len(g['kept']) > 200
                      else ('medium' if len(g['kept']) >= 50 else 'simple')),
        })
    return rows


def band(rows_, key):
    """按百分比分档计数（单位=单）。"""
    bands = [
        ('100%', lambda v: v >= 0.9999),
        ('80-99%', lambda v: 0.8 <= v < 0.9999),
        ('60-79%', lambda v: 0.6 <= v < 0.8),
        ('40-59%', lambda v: 0.4 <= v < 0.6),
        ('20-39%', lambda v: 0.2 <= v < 0.4),
        ('1-19%', lambda v: 0.0001 <= v < 0.2),
        ('0%', lambda v: v < 0.0001),
    ]
    out = []
    total = len(rows_)
    for label, fn in bands:
        n = sum(1 for r in rows_ if fn(r[key]))
        out.append((label, n, n / max(1, total) * 100))
    return out


def summarize(rows_, label):
    if not rows_:
        print(f'\n【{label}】无数据')
        return {}

    n = len(rows_)
    perfect1 = sum(1 for r in rows_ if r['r1'] >= 0.9999)
    perfect2 = sum(1 for r in rows_ if r['r2'] >= 0.9999)
    med1 = statistics.median(r['r1'] for r in rows_) * 100
    med2 = statistics.median(r['r2'] for r in rows_) * 100
    mean1 = sum(r['r1'] for r in rows_) / n * 100
    mean2 = sum(r['r2'] for r in rows_) / n * 100

    print(f'\n{"=" * 72}')
    print(f'【{label}】{n} 单')
    print('=' * 72)
    print(f'  阶段1 规划覆盖')
    print(f'    达标（100%）      {perfect1}/{n} = {perfect1 / n * 100:.1f}%')
    print(f'    单均（中位数）     {med1:.1f}%')
    print(f'    单均（平均数）     {mean1:.1f}%')
    print(f'  阶段2 产物覆盖')
    print(f'    达标（100%）      {perfect2}/{n} = {perfect2 / n * 100:.1f}%')
    print(f'    单均（中位数）     {med2:.1f}%')
    print(f'    单均（平均数）     {mean2:.1f}%')

    print(f'\n  阶段2 逐单分布：')
    print(f'    {"区间":<10} {"单数":>4} {"占比":>7}')
    for lbl, cnt, pct in band(rows_, 'r2'):
        print(f'    {lbl:<10} {cnt:>4} {pct:>6.1f}%')

    # 分档
    print(f'\n  {"档位":<14} {"单数":>4} {"达标单":>6} {"达标率":>7} {"中位覆盖":>9}')
    print('  ' + '-' * 50)
    for lv, name in [('simple', '简单 <50'), ('medium', '中等 50-200'),
                     ('complex', '复杂 >200')]:
        sub = [r for r in rows_ if r['level'] == lv]
        if not sub:
            continue
        pf = sum(1 for r in sub if r['r2'] >= 0.9999)
        md = statistics.median(r['r2'] for r in sub) * 100
        print(f'  {name:<14} {len(sub):>4} {pf:>6} {pf / len(sub) * 100:>6.1f}% {md:>8.1f}%')

    return {'n': n, 'perfect1': perfect1, 'perfect2': perfect2,
            'med1': med1, 'med2': med2, 'mean1': mean1, 'mean2': mean2}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--out-dir', default='/tmp/eval_2stage_v2_out')
    ap.add_argument('--save', default='')
    args = ap.parse_args()

    rows = collect(args.out_dir)
    restricted = load_restricted()
    rows_b = [r for r in rows if r['tk'] not in restricted]

    A = summarize(rows, '口径 A：全量')
    B = summarize(rows_b, f'口径 B：排除 {len(restricted)} 个数据受限工单')

    print(f'\n{"=" * 72}')
    print('【对比】单位：单')
    print('=' * 72)
    print(f'{"指标":<22} {"全量":>16} {"排除受限":>16}')
    print('-' * 58)
    print(f'{"工单数":<22} {A["n"]:>16} {B["n"]:>16}')
    print(f'{"阶段1 达标单":<22} {A["perfect1"]:>16} {B["perfect1"]:>16}')
    print(f'{"阶段1 达标率":<22} {A["perfect1"]/A["n"]*100:>15.1f}% '
          f'{B["perfect1"]/B["n"]*100:>15.1f}%')
    print(f'{"阶段1 中位覆盖":<22} {A["med1"]:>15.1f}% {B["med1"]:>15.1f}%')
    print(f'{"阶段2 达标单":<22} {A["perfect2"]:>16} {B["perfect2"]:>16}')
    print(f'{"阶段2 达标率":<22} {A["perfect2"]/A["n"]*100:>15.1f}% '
          f'{B["perfect2"]/B["n"]*100:>15.1f}%')
    print(f'{"阶段2 中位覆盖":<22} {A["med2"]:>15.1f}% {B["med2"]:>15.1f}%')

    if args.save:
        Path(args.save).write_text(json.dumps({
            'A': A, 'B': B, 'restricted': sorted(restricted),
            'rows': rows,
        }, ensure_ascii=False, indent=1), encoding='utf-8')
        print(f'\n已存 {args.save}')


if __name__ == '__main__':
    main()

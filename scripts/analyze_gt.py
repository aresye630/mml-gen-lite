#!/usr/bin/env python3
"""分析 GT 结构，输出「哪些参数固定 / 哪些变化 / 哪些有规律」。

用途：为 gt-to-intent-dataset skill 提供数据支撑，
     决定意图里写什么、数据清单里放什么。

用法：
  python3 analyze_gt.py <ticket>
  python3 analyze_gt.py --all          # 全部工单概览
"""
import argparse
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

GT_PATH = Path('/tmp/gt_cleaned.json')


def load_gt():
    return json.loads(GT_PATH.read_text(encoding='utf-8'))


def seq_like(values):
    """判断一组值是否是序号递增（如 Tunnel300/301/302）。"""
    if len(values) < 3:
        return None
    # 提取数字部分
    pats = []
    for v in values:
        m = re.match(r'^(.*?)(\d+)$', str(v))
        if not m:
            return None
        pats.append((m.group(1), int(m.group(2))))
    prefixes = {p[0] for p in pats}
    if len(prefixes) != 1:
        return None
    nums = sorted(p[1] for p in pats)
    # 连续递增？
    if nums == list(range(nums[0], nums[0] + len(nums))):
        return {'prefix': prefixes.pop(), 'start': nums[0], 'end': nums[-1], 'count': len(nums)}
    return None


def analyze_ticket(g, verbose=True):
    """分析一个工单的 GT 结构。"""
    by_fam = defaultdict(list)
    for ln, verb, fam, params, raw in g['kept']:
        by_fam[f'{verb} {fam}'].append(params)

    out = {}
    for fam, items in sorted(by_fam.items()):
        n = len(items)
        # 每个参数的取值分布
        keys = Counter()
        for p in items:
            for k in p.keys():
                keys[k] += 1

        fixed = {}      # 固定值
        varied = {}     # 变化值
        regular = {}    # 有规律

        for k in keys:
            vals = [p.get(k) for p in items if k in p]
            uniq = {v for v in vals if v is not None}
            if len(uniq) == 1:
                fixed[k] = uniq.pop()
            else:
                seq = seq_like(sorted(uniq))
                if seq:
                    regular[k] = seq
                else:
                    varied[k] = len(uniq)

        n_objs = len({next(iter(p.values())) for p in items if p})
        out[fam] = {
            'n_cmds': n,
            'n_objs': n_objs,
            'fixed': fixed,
            'regular': regular,
            'varied': varied,
        }

        if verbose:
            print(f'\n{"="*72}')
            print(f'{fam}   {n} 条 / {n_objs} 个对象')
            print('=' * 72)
            if fixed:
                print('  【固定值 → 写进意图】')
                for k, v in fixed.items():
                    print(f'    {k} = {v}')
            if regular:
                print('  【有规律 → 意图里说明规律】')
                for k, s in regular.items():
                    print(f'    {k}: {s["prefix"]}{s["start"]} ~ {s["prefix"]}{s["end"]} '
                          f'（{s["count"]} 个连续）')
            if varied:
                print('  【变化值 → 进数据清单】')
                for k, nv in varied.items():
                    print(f'    {k}: {nv} 种取值')

    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('ticket', nargs='?')
    ap.add_argument('--all', action='store_true')
    args = ap.parse_args()

    gt = load_gt()
    if args.all:
        print(f'{"工单":<22} {"GT条":>5} {"族数":>4} {"对象数":>6}')
        print('=' * 45)
        for r in sorted(gt, key=lambda x: -len(x['kept'])):
            n_objs = len({next(iter(p.values())) for _, v, f, p, _ in r['kept'] if p})
            n_fams = len({f'{v} {f}' for _, v, f, p, _ in r['kept']})
            print(f"{r['ticket']:<22} {len(r['kept']):>5} {n_fams:>4} {n_objs:>6}")
        return

    if not args.ticket:
        print('用法：analyze_gt.py <ticket> 或 --all')
        return

    g = next((x for x in gt if x['ticket'] == args.ticket), None)
    if not g:
        print(f'找不到工单 {args.ticket}')
        return

    print(f"\n工单 {args.ticket}   GT {len(g['kept'])} 条")
    analyze_ticket(g)


if __name__ == '__main__':
    main()

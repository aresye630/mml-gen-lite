#!/usr/bin/env python3
"""两种口径统计：全量 vs 排除数据受限工单。

用户要求（2026-11-10）：
  「先全量跑，统计的时候分为全量结果和不计算这11个工单的结果」

两种口径：
  A. 全量：所有工单参与
  B. 排除数据受限：剔除「缺 SET/MOD/RMV 所需现网数据」的 11 个工单

数据受限工单来源：/tmp/missing_classified.json 的 need_data（真缺数据的族）。
"""
import argparse
import json
import re
import statistics
from pathlib import Path

GT = json.loads(Path('/tmp/gt_cleaned.json').read_text(encoding='utf-8'))
GT_MAP = {g['ticket']: g for g in GT}


def load_restricted():
    """从缺数据分析结果里取「真缺数据」的工单列表。"""
    p = Path('/tmp/missing_classified.json')
    if not p.exists():
        return set()
    cls = json.loads(p.read_text(encoding='utf-8'))
    return {x['tk'] for x in cls.get('need_data') or []}


def parse_plan_fams(plan_text):
    """从规划表提取族（跳过状态=跳过的行）。"""
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
                status = cells[st_idx] if (st_idx is not None and st_idx < len(cells)) else ''
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


def count_cmds(text):
    return len([l for l in text.split('\n')
                if l.strip() and not l.strip().startswith(('/*', '//', '#'))])


def collect(out_dir):
    """从产物目录收集每单数据。"""
    rows = []
    d = Path(out_dir)
    if not d.exists():
        return rows
    for sub in sorted(d.iterdir()):
        if not sub.is_dir():
            continue
        tk = sub.name
        if tk not in GT_MAP:
            continue
        g = GT_MAP[tk]
        gt_fams = {f for _, v, f, _, _ in g['kept']}

        plan_p = sub / '命令族规划.md'
        mml_p = sub / 'mml.txt'
        plan_text = plan_p.read_text(encoding='utf-8', errors='replace') if plan_p.exists() else ''
        mml_text = mml_p.read_text(encoding='utf-8', errors='replace') if mml_p.exists() else ''
        if not plan_text and not mml_text:
            continue

        plan = parse_plan_fams(plan_text)
        prod = parse_cmd_fams(mml_text)

        rows.append({
            'tk': tk,
            'gt_fams': len(gt_fams),
            'gt_cmds': len(g['kept']),
            's1_fams': len(gt_fams & plan),
            's2_fams': len(gt_fams & prod),
            'prod_cmds': count_cmds(mml_text),
            'level': ('complex' if len(g['kept']) > 200
                      else ('medium' if len(g['kept']) >= 50 else 'simple')),
        })
    return rows


def summarize(rows, label):
    if not rows:
        print(f'\n【{label}】无数据')
        return {}
    gt_f = sum(r['gt_fams'] for r in rows)
    s1 = sum(r['s1_fams'] for r in rows)
    s2 = sum(r['s2_fams'] for r in rows)
    gc = sum(r['gt_cmds'] for r in rows)
    pc = sum(r['prod_cmds'] for r in rows)

    print(f'\n{"=" * 78}')
    print(f'【{label}】{len(rows)} 个工单')
    print('=' * 78)
    print(f'  GT 族总数        {gt_f}')
    print(f'  阶段1 规划覆盖    {s1}/{gt_f} = {s1 / max(1, gt_f) * 100:.1f}%')
    print(f'  阶段2 产物覆盖    {s2}/{gt_f} = {s2 / max(1, gt_f) * 100:.1f}%')
    print(f'  阶段损耗          {s1 - s2:+d}')
    print(f'  命令数完成度      {pc}/{gc} = {pc / max(1, gc) * 100:.1f}%')
    perfect = sum(1 for r in rows if r['s2_fams'] == r['gt_fams'] and r['gt_fams'])
    print(f'  工单级全覆盖      {perfect}/{len(rows)}')

    # 分档
    print(f'\n  {"分档":<14} {"工单":>4} {"GT族":>5} {"阶段1":>7} {"阶段2":>7} {"命令数":>7}')
    print('  ' + '-' * 52)
    for lv, name in [('simple', '简单 <50'), ('medium', '中等 50-200'),
                     ('complex', '复杂 >200')]:
        sub = [r for r in rows if r['level'] == lv]
        if not sub:
            continue
        e = sum(r['gt_fams'] for r in sub)
        a = sum(r['s1_fams'] for r in sub)
        b = sum(r['s2_fams'] for r in sub)
        c1 = sum(r['gt_cmds'] for r in sub)
        c2 = sum(r['prod_cmds'] for r in sub)
        print(f'  {name:<14} {len(sub):>4} {e:>5} {a / max(1, e) * 100:>6.1f}% '
              f'{b / max(1, e) * 100:>6.1f}% {c2 / max(1, c1) * 100:>6.0f}%')

    return {'n': len(rows), 'gt_fams': gt_f, 's1': s1, 's2': s2,
            'gt_cmds': gc, 'prod_cmds': pc, 'perfect': perfect}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--out-dir', default='/tmp/eval_2stage_v2_out')
    ap.add_argument('--save', default='')
    args = ap.parse_args()

    rows = collect(args.out_dir)
    restricted = load_restricted()

    print(f'产物目录: {args.out_dir}')
    print(f'收集到 {len(rows)} 个工单的产物')
    print(f'数据受限工单: {len(restricted)} 个')

    # 口径 A：全量
    s_all = summarize(rows, '口径 A：全量')

    # 口径 B：排除数据受限
    rows_b = [r for r in rows if r['tk'] not in restricted]
    s_ex = summarize(rows_b, f'口径 B：排除 {len(restricted)} 个数据受限工单')

    # 对比
    print(f'\n{"=" * 78}')
    print('【两口径对比】')
    print('=' * 78)
    print(f'{"指标":<18} {"全量":>14} {"排除受限":>14} {"变化":>10}')
    print('-' * 60)
    for key, name, is_pct in [
        ('n', '工单数', False),
        ('s1', '阶段1 命中族', False),
        ('s2', '阶段2 命中族', False),
    ]:
        a, b = s_all.get(key, 0), s_ex.get(key, 0)
        print(f'{name:<18} {a:>14} {b:>14} {b - a:>+10}')

    for key, tot_key, name in [
        ('s1', 'gt_fams', '阶段1 规划覆盖'),
        ('s2', 'gt_fams', '阶段2 产物覆盖'),
        ('prod_cmds', 'gt_cmds', '命令数完成度'),
    ]:
        ta, tb = s_all.get(tot_key, 1), s_ex.get(tot_key, 1)
        ra = s_all.get(key, 0) / max(1, ta) * 100
        rb = s_ex.get(key, 0) / max(1, tb) * 100
        print(f'{name:<18} {ra:>13.1f}% {rb:>13.1f}% {rb - ra:>+9.1f}pp')

    if args.save:
        Path(args.save).write_text(json.dumps({
            'all': s_all, 'excluded': s_ex,
            'restricted_tickets': sorted(restricted),
            'rows': rows,
        }, ensure_ascii=False, indent=1), encoding='utf-8')
        print(f'\n已存 {args.save}')


if __name__ == '__main__':
    main()

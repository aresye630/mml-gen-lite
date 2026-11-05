#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""用陕西真实现网 MML（黄金规则）验收系统产出的结果一致性。

黄金规则.txt 两段（行号相同，均为 EXP 行号）：
  · 「EXP中迭代查找」56 行 —— 关联路径推导（无 ✅）
  · 「按命令顺序整理」56 行 —— 最终应呈现的链（✅=特性相关 45 条 / 无✅=灰化关联 11 条）

⚠ 行号随 EXP 版本会偏移 ⇒ 本工具**以命令内容为锚**（归一化后匹配），
   行号仅作辅助定位与人工复核线索。

用法:
  python3 mml_compare.py --golden <黄金规则.txt> --exp <EXP.txt> \
      --products <产物目录> [--json <结果.json>]
"""
import argparse
import json
import re
import sys
from collections import OrderedDict
from pathlib import Path

LINE_RE = re.compile(r'^\s*(✅\s*)?L(\d+)\s+([A-Z][A-Z0-9 ]*):(.*)$')


def norm_cmd(s):
    """归一化命令文本：压空白、去尾分号、参数分隔统一"""
    s = s.strip().rstrip(';').strip()
    s = re.sub(r'\s*,\s*', ',', s)
    s = re.sub(r'\s*=\s*', '=', s)
    s = re.sub(r'\s+', ' ', s)
    return s


def parse_golden(path):
    lines = Path(path).read_text(encoding='utf-8').split('\n')
    idx_org = next(i for i, l in enumerate(lines) if '按照命令顺序整理' in l)
    seg_iter, seg_final = [], []
    for i, l in enumerate(lines, 1):
        m = LINE_RE.match(l)
        if not m:
            continue
        star, seq, verb, body = bool(m.group(1)), int(m.group(2)), m.group(3), m.group(4)
        txt = norm_cmd(f'{verb}:{body}')
        rec = {'exp_line': seq, 'cmd': txt, 'verb': verb, 'key': star,
               'src_line': i}
        (seg_iter if i < idx_org + 1 else seg_final).append(rec)
    return seg_iter, seg_final


def load_exp(path):
    """EXP 行 → 归一化命令（用于按内容定位真实行号）"""
    out = {}
    for i, l in enumerate(Path(path).read_text(encoding='utf-8',
                                               errors='replace').split('\n'), 1):
        t = l.strip()
        if t and not t.startswith('//') and ':' in t:
            out.setdefault(norm_cmd(t), []).append(i)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--golden', required=True)
    ap.add_argument('--exp', required=True)
    ap.add_argument('--products', required=True)
    ap.add_argument('--json', default=None)
    a = ap.parse_args()

    seg_iter, seg_final = parse_golden(a.golden)
    n_key = sum(1 for r in seg_final if r['key'])
    print('═' * 62)
    print('黄金规则（陕西真实现网 MML）')
    print('═' * 62)
    print(f'  命令总数      : {len(seg_final)}')
    print(f'  ✅ 特性相关   : {n_key}')
    print(f'  灰化关联      : {len(seg_final) - n_key}')
    print(f'  迭代段/整理段 : {len(seg_iter)} / {len(seg_final)}')
    print()

    exp_idx = load_exp(a.exp)
    print('── ① 行号 vs 内容 双锚定位（EXP 原文）──')
    hit_line = hit_content = miss = 0
    drift = []
    for r in seg_final:
        if r['exp_line'] in exp_idx.get(r['cmd'], []):
            hit_line += 1
            hit_content += 1
        elif r['cmd'] in exp_idx:
            hit_content += 1
            drift.append((r['exp_line'], exp_idx[r['cmd']][0], r['verb']))
        else:
            miss += 1
    print(f'  行号精确命中 : {hit_line} / {len(seg_final)}')
    print(f'  内容命中     : {hit_content} / {len(seg_final)}'
          f'   （其中行号偏移 {len(drift)} 条）')
    print(f'  内容也未找到 : {miss}')
    if drift:
        print('  行号偏移示例（黄金规则行 → EXP 实际行）:')
        for g, e, v in drift[:5]:
            print(f'    L{g} → L{e}  ({v})')
    print()

    # 产物侧：从 groundtruth 目录提取「EXP 行号」引用
    proddir = Path(a.products)
    gt = proddir / '特性配置基线'
    if not gt.is_dir():
        gt = proddir
    prod_lines = set()
    prod_texts = {}
    for md in sorted(gt.glob('*.md')):
        t = md.read_text(encoding='utf-8', errors='replace')
        prod_texts[md.name] = t
        for m in re.finditer(r'L(\d{2,6})', t):
            prod_lines.add(int(m.group(1)))
    print('── ② 系统产物覆盖（按 EXP 行号引用）──')
    print(f'  产物目录     : {gt}')
    print(f'  产物引用行号 : {len(prod_lines)} 个唯一值')
    cov = [r for r in seg_final if r['exp_line'] in prod_lines]
    print(f'  黄金规则覆盖 : {len(cov)} / {len(seg_final)}')
    key_cov = [r for r in cov if r['key']]
    print(f'    其中 ✅ 特性相关: {len(key_cov)} / {n_key}')
    print()

    # ③ 内容级（不依赖行号）：产物文本中是否出现该命令的关键标识值
    print('── ③ 内容级覆盖（按命令主体标识值，不依赖行号）──')
    allprod = '\n'.join(prod_texts.values())
    n_content = 0
    detail = []
    for r in seg_final:
        # 取命令的第一个「标识参数」值（通常是 NAME/ID 类主键）
        m = re.search(r'([A-Z0-9_]*(?:NAME|ID|NM))="?([^",;]+)"?', r['cmd'])
        anchor = m.group(2) if m else None
        found = bool(anchor and anchor in allprod)
        if found:
            n_content += 1
        detail.append({'exp_line': r['exp_line'], 'key': r['key'],
                       'verb': r['verb'], 'anchor': anchor,
                       'in_product_by_content': found})
    print(f'  内容命中     : {n_content} / {len(seg_final)}')
    print()
    print('  漏报清单（产品产物中找不到该命令的主体标识值）:')
    n_show = 0
    for d in detail:
        if not d['in_product_by_content']:
            flag = '✅' if d['key'] else '  '
            print(f'    {flag} L{d["exp_line"]:<6} {d["verb"]:<22} '
                  f'anchor={d["anchor"]}')
            n_show += 1
            if n_show >= 25:
                print(f'    … 还有 {sum(1 for x in detail if not x["in_product_by_content"]) - n_show} 条')
                break
    print()

    if a.json:
        Path(a.json).write_text(json.dumps({
            'golden_total': len(seg_final), 'golden_key': n_key,
            'line_hit': hit_line, 'content_hit': hit_content,
            'line_drift': len(drift), 'content_miss': miss,
            'product_covered_by_line': len(cov),
            'product_covered_by_content': n_content,
            'detail': detail,
        }, ensure_ascii=False, indent=2), encoding='utf-8')
        print(f'  JSON 已写: {a.json}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""统计现网 EXP 各 ADD 命令的**主键命名规律**（N19 生成器的数据依据）。

用法: python3 name_stats.py <exp.txt> [--top 30]
输出: 每类 ADD 命令的主键名 → 取值样本 + 命名模式
"""
import argparse
import re
import sys
from collections import Counter, defaultdict

# ADD XXX:KEY="v",P=... ;  或  ADD XXX:KEY=v,...
CMD_RE = re.compile(r'^\s*(ADD|MOD|DEL)\s+([A-Z][A-Z0-9_]*)\s*:\s*(.+?);?\s*$', re.I)
KV_RE = re.compile(r'([A-Z][A-Z0-9_]*)\s*=\s*("([^"]*)"|[^,]+)')


def parse(exp_path):
    """→ {命令: {主键名: Counter(值)}}"""
    data = defaultdict(lambda: defaultdict(Counter))
    with open(exp_path, encoding='utf-8', errors='replace') as f:
        for line in f:
            m = CMD_RE.match(line)
            if not m:
                continue
            verb, cmd, body = m.group(1).upper(), m.group(2).upper(), m.group(3)
            if verb != 'ADD':
                continue
            pairs = []
            for kv in KV_RE.finditer(body):
                k = kv.group(1).upper()
                v = kv.group(2)
                if v.startswith('"') and v.endswith('"'):
                    v = v[1:-1]
                pairs.append((k, v))
            if not pairs:
                continue
            # 约定：第一个参数 = 主键（MML 惯例）
            k0, v0 = pairs[0]
            data[cmd][k0][v0] += 1
    return data


def pattern_of(vals):
    """归纳命名模式（业务标识_序号_后缀 等）"""
    pats = Counter()
    for v in vals:
        if re.fullmatch(r'[a-z][a-z0-9]*_[a-z0-9]+_\d{2}', v):
            pats['<汉字拼音/小写>_<标识>_<两位序号>'] += 1
        elif re.fullmatch(r'.*_\d{2,3}$', v):
            pats['<前缀>_<数字序号>'] += 1
        elif re.fullmatch(r'.*_\d+$', v):
            pats['<前缀>_<数字>'] += 1
        elif re.fullmatch(r'[a-z0-9_.]+', v):
            pats['<小写标识>'] += 1
        else:
            pats['<其它>'] += 1
    return pats


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('exp')
    ap.add_argument('--top', type=int, default=25)
    a = ap.parse_args()

    d = parse(a.exp)
    # 按出现总量排序
    ranked = sorted(d.items(),
                    key=lambda kv: -sum(sum(c.values()) for c in kv[1].values()))
    print(f'EXP: {a.exp}')
    print(f'ADD 命令种类: {len(d)}')
    print('=' * 76)
    for cmd, keys in ranked[:a.top]:
        for k, ctr in keys.items():
            tot = sum(ctr.values())
            uniq = len(ctr)
            print(f'\n── {cmd}  主键={k}  出现 {tot} 次 / {uniq} 个不同值 ──')
            pats = pattern_of(ctr.keys())
            for p, n in pats.most_common():
                print(f'     模式 {p}: {n} 个值')
            for v, n in ctr.most_common(6):
                print(f'       {v!r}  ×{n}')
    return 0


if __name__ == '__main__':
    sys.exit(main())

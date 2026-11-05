#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""p2_patterns.py — 模式挖掘器（T2）。

四类通用检测器（全部数据驱动，规则在 rules/*.yaml，代码零局点值）：
  1. domain_stats  功能域统计（§2 域表）：域 → 命令族计数 + 主锚值 top
  2. naming        命名族归纳：关注 (cmd,param) 值集合 → 公共前后缀/模板/计数
  3. id_ranges     数值 ID 段分析：连续 run / 高频固定差 / 下一可用号
  4. conventions   惯例众数：参数取值分布 + 是否统一

输出：{'domain_stats': [...], 'profiles': [...]}（并入 report.json）。
"""

import re
import yaml
from collections import Counter
from pathlib import Path

from p1_parse import parse_exp, parse_params

RULES_DIR = Path(__file__).resolve().parent / 'rules'


def load_rules(name):
    return yaml.safe_load((RULES_DIR / name).read_text(encoding='utf-8'))


# ═══ 1. 域统计 ═══════════════════════════════════════════════════════
def domain_stats(commands, domains_cfg, product):
    """域表：每域 {id, name, cmds: [{type, n, anchors: {param: topN}}]}。"""
    doms = (domains_cfg.get(product) or {})
    out = []
    for did, cfg in doms.items():
        by_type = Counter()
        anchors = {}
        for ctype, params in cfg['cmds'].items():
            vals = {p: Counter() for p in params}
            for seq, line in commands.items():
                if not line.startswith(ctype + ':'):
                    continue
                by_type[ctype] += 1
                pd = parse_params(line)
                for p in params:
                    if p in pd:
                        vals[p][pd[p]] += 1
            for p, c in vals.items():
                anchors.setdefault(p, [])
                for v, n in c.most_common(6):
                    anchors[p].append({'v': v, 'n': n})
        out.append({'id': did, 'name': cfg['name'],
                    'cmd_stats': [{'type': t, 'n': n} for t, n in by_type.most_common()],
                    'anchor_vals': anchors})
    return out


# ═══ 2. 命名族归纳 ═══════════════════════════════════════════════════
def _naming_profile(cmd, param, vals):
    """值集合 → 分段命名族（字面段 + 变体段枚举），比正则还原更稳且零误报。

    输出 segments: [{type: literal, value}|{type: variant, values:[..], n}]
    """
    vals = sorted(set(vals))
    if not vals:
        return None
    n = len(vals)
    if n <= 2:
        return {'cmd': cmd, 'param': param, 'values_n': n,
                'samples': vals[:3], 'note': '值过少，无命名规律归纳'}
    parts = [v.split('_') for v in vals]
    m = max(len(p) for p in parts)
    segs = []
    for j in range(m):
        toks = [p[j] if j < len(p) else '' for p in parts]
        uniq = sorted(set(t for t in toks if t))
        if len(uniq) == 1:
            segs.append({'type': 'literal', 'value': uniq[0]})
        else:
            segs.append({'type': 'variant', 'values': uniq[:6],
                         'n': len(uniq), 'absent': '' in toks})
    return {'cmd': cmd, 'param': param, 'values_n': n,
            'segments': segs, 'samples': vals[:4]}


# ═══ 3. 数值 ID 段分析 ═══════════════════════════════════════════════
_NUM_TAIL_RE = re.compile(r'(\d+)$')


def _id_numeric(v):
    """ID 值 → (numeric, 数字尾长) 若整体可数值化/数字尾；否则 None。"""
    s = str(v)
    if s.isdigit():
        return int(s), s
    m = _NUM_TAIL_RE.search(s)
    if m and len(m.group(1)) >= 3:
        return int(m.group(1)), s  # 前缀+数字尾：用数字尾做段分析
    return None


def _id_range_profile(cmd, param, vals):
    """ID 集合 → 段分析：区间/最大连续 run/下一可用/固定差配对。"""
    parsed = []
    for v in set(vals):
        r = _id_numeric(v)
        if r:
            parsed.append((v, r[0]))
    if len(parsed) < 3:
        return {'cmd': cmd, 'param': param, 'note': '可数值化 ID 过少', 'values_n': len(set(vals))}
    nums = sorted(x[1] for x in parsed)
    uniq = sorted(set(nums))
    # 连续 run
    runs, cur = [], [uniq[0]]
    for a, b in zip(uniq, uniq[1:]):
        if b - a == 1:
            cur.append(b)
        else:
            runs.append(cur)
            cur = [b]
    runs.append(cur)
    runs.sort(key=len, reverse=True)
    longest = runs[0]
    # 最大 run 尾的下一可用（若 run 在低段连续占用）
    next_free = longest[-1] + 1 if len(longest) >= 3 else None
    # 固定差配对：差 ≤ 50000 的高频差
    if len(uniq) <= 4000:
        deltas = Counter()
        for i in range(len(uniq)):
            for j in range(i + 1, len(uniq)):
                d = uniq[j] - uniq[i]
                if d <= 50000:
                    deltas[d] += 1
                else:
                    break
        top = [(d, n) for d, n in deltas.most_common(3) if n >= 8]
    else:
        top = []
    return {'cmd': cmd, 'param': param, 'values_n': len(set(vals)),
            'numeric_n': len(parsed), 'min': uniq[0], 'max': uniq[-1],
            'longest_run': {'from': longest[0], 'to': longest[-1], 'len': len(longest)},
            'next_free': next_free,
            'top_deltas': [{'delta': d, 'pairs': n} for d, n in top]}


# ═══ 4. 惯例众数 ═════════════════════════════════════════════════════
def _convention_profile(cmd, params, commands):
    """每参数取值分布；同一命令族内多参数组合（成对惯例）粗版 = 单参分布。"""
    out = {'cmd': cmd}
    for p in params:
        c = Counter()
        for seq, line in commands.items():
            if not line.startswith(cmd + ':'):
                continue
            pd = parse_params(line)
            if p in pd:
                c[pd[p]] += 1
        if not c:
            continue
        mc = c.most_common(4)
        out[p] = {'dist': [{'v': v, 'n': n} for v, n in mc],
                  'uniform': len(c) == 1}
    return out if len(out) > 1 else None


# ═══ run ═════════════════════════════════════════════════════════════
def run(exp_path=None, commands=None, meta=None, product=None,
        domains_cfg=None, targets_cfg=None):
    """commands/meta 可外部传入（避免重复解析）；否则内部解析 exp_path。"""
    if commands is None:
        parsed = parse_exp(exp_path)
        commands = parsed['commands']
        meta = meta or parsed['meta_hdr']
    product = product or meta.get('me_type', 'UDG')
    domains_cfg = domains_cfg or load_rules('domains.yaml')
    targets_cfg = targets_cfg or load_rules('pattern_targets.yaml')
    tgt = targets_cfg.get(product) or {}
    profiles = []
    # 2. naming
    for t in tgt.get('naming', []):
        vals = [parse_params(commands[s]).get(t['param'])
                for s in commands if commands[s].startswith(t['cmd'] + ':')]
        p = _naming_profile(t['cmd'], t['param'], [v for v in vals if v])
        if p:
            p['kind'] = 'naming'
            profiles.append(p)
    # 3. id_ranges
    for t in tgt.get('id_ranges', []):
        vals = [parse_params(commands[s]).get(t['param'])
                for s in commands if commands[s].startswith(t['cmd'] + ':')]
        p = _id_range_profile(t['cmd'], t['param'], [v for v in vals if v])
        if p:
            p['kind'] = 'id_ranges'
            profiles.append(p)
    # 4. conventions
    for t in tgt.get('conventions', []):
        p = _convention_profile(t['cmd'], t['params'], commands)
        if p:
            p['kind'] = 'conventions'
            profiles.append(p)
    return {'domain_stats': domain_stats(commands, domains_cfg, product),
            'profiles': profiles}


if __name__ == '__main__':
    import json
    import sys
    exp = sys.argv[1] if len(sys.argv) > 1 else None
    if not exp:
        print('usage: p2_patterns.py <exp.txt>')
        sys.exit(1)
    print(json.dumps(run(exp), ensure_ascii=False, indent=1))

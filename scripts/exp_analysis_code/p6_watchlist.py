#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""p6_watchlist.py — 可疑值检测器（T6，待审视候选）。

启发式（rules/watchlist_heuristics.yaml 声明）：
  1. placeholder_ip   全 EXP 扫描 IP 形值：四段/八组全同段位或文档示例段
  2. style-mismatch   ADD IPFARM 内 VIRTUALIP 前缀 vs 族内 SERVERIP 众数前缀
输出 watchlist[] {heuristic, cmd(带锚点名), param, value, why, seq}。
跨层推理类审视项（如"N4/N6 L2 缺层含义"）非启发式可判——渲染段标注
需 P2/P3，本模块不产出（不编造）。
"""

import ipaddress
import re
import yaml
from collections import Counter
from pathlib import Path

from p1_parse import parse_exp, parse_params

RULES_DIR = Path(__file__).resolve().parent / 'rules'

_IPV4_RE = re.compile(r'^\d{1,3}(?:\.\d{1,3}){3}$')
_IPV6_RE = re.compile(r'^[0-9a-fA-F]{1,4}(?::[0-9a-fA-F]{1,4}){7}$')
# 文档示例段（RFC5737 + 常用占位）
_DOC_NETS4 = ['192.0.2.', '198.51.100.', '203.0.113.']
_IP_KEY_HINTS = ('IP', 'VIP', 'ADDR', 'ADDRESS', 'SERVERIP')


def _ip_kind(v):
    if _IPV4_RE.match(v):
        return 'v4'
    if _IPV6_RE.match(v):
        return 'v6'
    return None


def _all_same_segments(v, kind):
    if kind == 'v4':
        return len(set(v.split('.'))) == 1
    return len(set(v.lower().split(':'))) == 1


def _is_doc_ip(v, kind):
    return kind == 'v4' and any(v.startswith(p) for p in _DOC_NETS4)


def _placeholder_hits(commands, allowlist):
    hits = []
    for seq, line in commands.items():
        pd = parse_params(line)
        for k, v in pd.items():
            if 'MASK' in k:            # 掩码参数（255.255.255.255 合法）
                continue
            kind = _ip_kind(v)
            if not kind:
                continue
            if kind == 'v6':
                if _all_same_segments(v, 'v6'):
                    hits.append({'seq': seq, 'cmd': line.split(':', 1)[0],
                                 'param': k, 'value': v, 'kind': 'v6'})
            else:  # v4
                if _is_doc_ip(v, 'v4'):
                    hits.append({'seq': seq, 'cmd': line.split(':', 1)[0],
                                 'param': k, 'value': v, 'kind': 'v4'})
                elif _all_same_segments(v, 'v4') and v not in allowlist:
                    hits.append({'seq': seq, 'cmd': line.split(':', 1)[0],
                                 'param': k, 'value': v, 'kind': 'v4'})
    return hits


def _style_mismatch_hits(commands):
    """ADD IPFARM：族内 VIRTUALIP vs SERVERIP 众数前缀。"""
    farms = {}  # name → {'seq', 'servers': Counter, 'vips': []}
    for seq, line in commands.items():
        if not line.startswith('ADD IPFARM:'):
            continue
        pd = parse_params(line)
        nm = pd.get('IPFARMNAME') or pd.get('SERVERGROUPNAME') or '?'
        f = farms.setdefault(nm, {'seq': seq, 'servers': Counter(), 'vips': []})
        for k, v in pd.items():
            if k.startswith('SERVERIP') and _ip_kind(v):
                f['servers'][v] += 1
            elif k.startswith(('VIRTUALIP', 'VIP')) and _ip_kind(v):
                f['vips'].append((k, v))
    hits = []
    for nm, f in farms.items():
        if not f['servers'] or not f['vips']:
            continue
        # 众数前缀：v4 前两段 / v6 前 4 组
        def prefix(v, kind):
            return '.'.join(v.split('.')[:2]) if kind == 'v4' \
                else ':'.join(v.split(':')[:4]).lower()
        kinds = {}
        for v in f['servers']:
            kinds.setdefault(prefix(v, _ip_kind(v)), 0)
            kinds[prefix(v, _ip_kind(v))] += f['servers'][v]
        top_prefix = max(kinds, key=kinds.get)
        for k, v in f['vips']:
            p = prefix(v, _ip_kind(v))
            if p != top_prefix and not _all_same_segments(v, _ip_kind(v)):
                hits.append({'seq': f['seq'], 'cmd': 'ADD IPFARM', 'param': k,
                             'value': v, 'farm': nm, 'servers_prefix': top_prefix})
    return hits


def _echo_all_off_hits(commands):
    """SET UPGTPPATH Echo 三开关全 DISABLE。"""
    hits = []
    for seq, line in commands.items():
        if not line.startswith('SET UPGTPPATH:'):
            continue
        pd = parse_params(line)
        if all(pd.get(k) == 'DISABLE' for k in ('V0ECHOSW', 'V1DATAECHOSW', 'ECHOLISTSWITCH')):
            hits.append({'seq': seq, 'cmd': 'SET UPGTPPATH',
                         'params': {k: pd.get(k) for k in
                                    ('V0ECHOSW', 'V1DATAECHOSW', 'ECHOLISTSWITCH')}})
    return hits


def _apn_v4v6_asym_hits(commands):
    """APN HASVPN=DISABLE 且 APNADDRESSATTR SUPPORTIPV4=ENABLE。"""
    apn_novpn = {parse_params(l).get('APN'): s
                 for s, l in commands.items()
                 if l.startswith('ADD APN:')
                 and parse_params(l).get('HASVPN') == 'DISABLE'}
    hits = []
    for seq, line in commands.items():
        if not line.startswith('SET APNADDRESSATTR:'):
            continue
        pd = parse_params(line)
        apn = pd.get('APN')
        if apn in apn_novpn and pd.get('SUPPORTIPV4') == 'ENABLE':
            hits.append({'seq': seq, 'cmd': 'SET APNADDRESSATTR', 'apn': apn,
                         'add_apn_seq': apn_novpn[apn],
                         'value': f"HASVPN=DISABLE/SUPPORTIPV4=ENABLE"})
    return hits


def run(exp_path=None, commands=None):
    if commands is None:
        parsed = parse_exp(exp_path)
        commands = parsed['commands']
    out = []
    rules = {r['heuristic_id']: r for r in
             yaml.safe_load((RULES_DIR / 'watchlist_heuristics.yaml')
                            .read_text(encoding='utf-8'))['UDG']}
    allowlist = rules['placeholder_ip'].get('allowlist', [])
    for h in _placeholder_hits(commands, allowlist):
        out.append({'heuristic': 'placeholder_ip', 'cmd': h['cmd'],
                    'param': h['param'], 'value': h['value'], 'seq': h['seq'],
                    'why': rules['placeholder_ip']['why']})
    for h in _style_mismatch_hits(commands):
        out.append({'heuristic': 'style-mismatch', 'cmd': h['cmd'],
                    'param': h['param'], 'value': h['value'], 'seq': h['seq'],
                    'farm': h['farm'],
                    'why': rules['style-mismatch']['why']
                           + f"（族内服务器前缀 {h['servers_prefix']}）"})
    for h in _echo_all_off_hits(commands):
        val = '，'.join(f"{k}={v}" for k, v in h['params'].items())
        out.append({'heuristic': 'echo-all-off', 'cmd': h['cmd'],
                    'param': 'Echo三开关', 'value': val,
                    'seq': h['seq'], 'why': rules['echo-all-off']['why']})
    for h in _apn_v4v6_asym_hits(commands):
        out.append({'heuristic': 'apn-v4v6-asym', 'cmd': h['cmd'],
                    'param': 'APN', 'value': h['apn'], 'seq': h['seq'],
                    'add_apn_seq': h['add_apn_seq'],
                    'why': rules['apn-v4v6-asym']['why']})
    return out


if __name__ == '__main__':
    import json
    import sys
    exp = sys.argv[1] if len(sys.argv) > 1 else None
    if not exp:
        print('usage: p6_watchlist.py <exp.txt>')
        sys.exit(1)
    for w in run(exp_path=exp):
        tag = w.get('farm', '')
        print(f"[{w['heuristic']}] L{w['seq']} {w['cmd']}{' ' + tag if tag else ''} "
              f"{w['param']}={w['value']}  — {w['why'][:60]}")

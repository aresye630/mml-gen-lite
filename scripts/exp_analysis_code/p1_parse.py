#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""p1_parse.py — EXP 解析层（T1）。

职责：
  1. 按行解析 exp.txt：注释行(/*…*/)、命令行、空行；保留 1-based 行号
  2. 元数据提取：ME Type / Version / PatchVersion / 导出时间 TIME /
     网元名（文件名或注释）、产品归属
  3. 全局统计：命令总数、verb 分布（ADD/SET/MOD/LCK/UPD/LOD）、
     命令类型计数（verb+name）
  4. 许可开关统计：SET LICENSESWITCH 的 LICITEM/SWITCH 分布（通用模式，
     不绑定具体 LICITEM 值 —— 值在运行时统计输出）

输出：parsed dict（供 pipeline 组 report.json meta/stats 段）。
纯函数，可 import；CLI 供独立调试。

验收判据（docs §5 T1，基准 = 8e86/1_检索与选型.md §1）：
  - cmd_count == 102275；by_verb ADD 100481 / SET 1591 / MOD 156 /
    LCK 35 / UPD 9 / LOD 3
  - meta: ME Type=UDG, Version=20.16.2, PatchVersion=20.16.2.56,
    导出 TIME 2026-07-21 10:17:17.935, 网元名 XAUPF017BHW
  - SET LICENSESWITCH 119 条（ENABLE 96 / DISABLE 23）
"""

import re
from collections import Counter, OrderedDict
from pathlib import Path

VERB_RE = re.compile(r'^([A-Z]+)\s+([A-Z0-9]+)')
# 全参数解析：KEY="quoted" | KEY=bare  (bare 到 , ; 或行尾；负向后顾防子串误匹配)
_ALL_PARAMS_RE = re.compile(r'(?<![A-Z0-9])([A-Z0-9]+)="([^"]*)"|(?<![A-Z0-9])([A-Z0-9]+)=([^,";\s]+)')
# 文件头注释样例：/* ME Type=UDG, Version=20.16.2 PatchVersion=20.16.2.56 */
#             /* TIME = 2026-07-21 10:17:17.935 */
META_RE = {
    'me_type': re.compile(r'ME Type=(\w+)'),
    'version': re.compile(r'Version=([\d.]+)'),
    'patch': re.compile(r'PatchVersion=([\d.]+)'),
    'time': re.compile(r'TIME\s*=\s*([\d\- :.]+)'),
    'me_name_c': re.compile(r'MOD ME:.*MELN="([^"]+)"'),
    'me_name_u': re.compile(r'SET UPINFO:HOSTNAME="([^"]+)"'),
}
# 文件名网元名段：EXPMML_ME0_UDG_<ver>_<NENAME>_<ts>.txt
NAME_RE = re.compile(r'^[A-Z0-9]+_(?:ME\d*_)?[A-Z]+_?[\d.]*_([A-Z0-9]+?)_\d{8}\d+.*\.txt$')


def parse_exp(path, encoding='utf-8', errors='replace'):
    """解析 exp.txt → {'meta':…, 'commands': {seq:int → line}, 'comments': {seq:int → line}}"""
    text = Path(path).read_text(encoding=encoding, errors=errors)
    commands = OrderedDict()
    comments = {}
    for i, line in enumerate(text.splitlines(), 1):
        s = line.strip()
        if not s:
            continue
        if s.startswith('/*') or s.startswith('//') or s.startswith('#'):
            comments[i] = s
            continue
        commands[i] = s
    return {'meta_hdr': _extract_meta(path, comments, commands),
            'commands': commands, 'comments': comments}


def _extract_meta(path, comments, commands):
    meta = {'source_file': str(Path(path).name)}
    hdr = '\n'.join(comments.values())
    for key in ('me_type', 'version', 'patch', 'time'):
        m = META_RE[key].search(hdr)
        if m:
            meta[key] = m.group(1).strip()
    # 网元名：文件名优先，命令（MOD ME/SET UPINFO）兜底
    mn = NAME_RE.match(Path(path).name)
    meta['ne_name'] = mn.group(1) if mn else None
    if not meta['ne_name']:
        for seq in commands:
            m = META_RE['me_name_c'].search(commands[seq])
            if m:
                meta['ne_name'] = m.group(1)
                break
            m = META_RE['me_name_u'].search(commands[seq])
            if m:
                meta['ne_name'] = m.group(1)
                break
    return meta


def stats(commands):
    """全局统计：verb 分布 + 命令类型计数。"""
    by_verb = Counter()
    by_type = Counter()
    for seq, line in commands.items():
        m = VERB_RE.match(line)
        if not m:
            by_verb['<other>'] += 1
            continue
        verb, name = m.group(1), m.group(2)
        by_verb[verb] += 1
        by_type[f'{verb} {name}'] += 1
    return {'cmd_count': len(commands),
            'by_verb': dict(by_verb.most_common()),
            'cmd_type_count': len(by_type),
            'top_cmd_types': [{'type': t, 'n': n} for t, n in by_type.most_common(40)]}


def parse_params(line):
    """MML 命令行 → {KEY: value}（quoted 与 bare 均支持；KEY 去重保留首现）。"""
    out = {}
    for m in _ALL_PARAMS_RE.finditer(line):
        k = m.group(1) or m.group(3)
        v = m.group(2) if m.group(2) is not None else m.group(4)
        if k not in out:
            out[k] = v
    return out


def extract_param(line, key):
    """取单参数值（无则 None）。"""
    return parse_params(line).get(key)


def lic_switch_stats(commands):
    """SET LICENSESWITCH 统计（通用：LICITEM 值运行时发现，不预设）。"""
    total = enabled = disabled = other = 0
    items = Counter()
    for seq, line in commands.items():
        if not line.startswith('SET LICENSESWITCH'):
            continue
        total += 1
        it = re.search(r'LICITEM="([^"]+)"', line)
        sw = re.search(r'SWITCH=(\w+)', line)
        lic = it.group(1) if it else '?'
        state = sw.group(1) if sw else '?'
        items[lic] = state
        if state == 'ENABLE':
            enabled += 1
        elif state == 'DISABLE':
            disabled += 1
        else:
            other += 1
    return {'cmd_count': total, 'enable': enabled, 'disable': disabled,
            'other': other, 'items': {k: v for k, v in items.items()}}


def run(exp_path):
    parsed = parse_exp(exp_path)
    return {'meta': parsed['meta_hdr'],
            'stats': stats(parsed['commands']),
            'lic_switch': lic_switch_stats(parsed['commands'])}


if __name__ == '__main__':
    import json
    import sys
    exp = sys.argv[1] if len(sys.argv) > 1 else None
    if not exp:
        print('usage: p1_parse.py <exp.txt>')
        sys.exit(1)
    out = run(exp)
    print(json.dumps(out, ensure_ascii=False, indent=1))

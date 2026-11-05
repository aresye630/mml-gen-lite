#!/usr/bin/env python3
"""汇总多个 exp 匹配结果 → 对比表（发现指纹/判定缺陷）"""
import json
import os
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(sys.argv[1] if len(sys.argv) > 1 else 'rules')

rows = []
for d in sorted(ROOT.iterdir()):
    if not d.is_dir():
        continue
    jp = d / 'match_result.json'
    if not jp.exists():
        continue
    r = json.load(open(jp, encoding='utf-8'))
    meta = r.get('meta', {})
    results = r.get('results', {})
    cnt = Counter(v['status'] for v in results.values())
    not_cfg = [v for v in results.values() if v['status'] == 'not_configured']
    attr = Counter()
    for v in not_cfg:
        det = v['detail']
        if det.get('lic_on'):
            attr['授权在'] += 1
        elif not (det.get('core_hit') or det.get('core_miss')):
            attr['纯公共'] += 1
        elif not det.get('core_hit'):
            attr['整族缺'] += 1
        else:
            attr['部分在'] += 1
    rows.append({
        'name': d.name,
        'exp_cmds': meta.get('exp_cmds', 0),
        'exp_types': meta.get('exp_cmd_types', 0),
        'cfg': cnt['configured'], 'not': cnt['not_configured'],
        'manual': cnt['manual'],
        'lic_on': attr['授权在'], 'whole': attr['整族缺'],
        'part': attr['部分在'], 'pub': attr['纯公共'],
    })

rows.sort(key=lambda x: x['name'])
print(f'{"exp":34s} {"命令数":>8s} {"类型":>5s} {"已配置":>5s} {"未配置":>5s} {"人工":>4s} | 归因: 授权在/整族缺/部分在/纯公共')
for x in rows:
    print(f'{x["name"]:34s} {x["exp_cmds"]:8d} {x["exp_types"]:5d} {x["cfg"]:5d} {x["not"]:5d} {x["manual"]:4d} | '
          f'{x["lic_on"]:4d} {x["whole"]:4d} {x["part"]:4d} {x["pub"]:4d}')

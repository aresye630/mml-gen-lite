#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""det_check 归一化逻辑单测（快速，秒级）——别再跑 140 秒才发现归一化没生效"""
import importlib.util
import json
import sys
from pathlib import Path

spec = importlib.util.spec_from_file_location(
    'det', str(Path(__file__).resolve().parent.parent / 'det_check.py'))
det = importlib.util.module_from_spec(spec)
sys.modules['det'] = det
spec.loader.exec_module(det)

ok = fail = 0


def chk(name, cond, extra=''):
    global ok, fail
    if cond:
        ok += 1
        print(f'  [OK]   {name}')
    else:
        fail += 1
        print(f'  [FAIL] {name} {extra}')


print('─── JSON 归一化（match_result.json 的 meta.updated_at）───')
a = json.dumps({'meta': {'updated_at': '2026-09-18 08:30:17', 'total': 435},
                'results': [1, 2, 3]}).encode()
b = json.dumps({'meta': {'updated_at': '2026-09-18 08:31:25', 'total': 435},
                'results': [1, 2, 3]}).encode()
na, nb = det._normalize('match_result.json', a), det._normalize('match_result.json', b)
chk('时间戳不同 → 归一化后相同', na == nb, f'\n      {na[:90]}\n      {nb[:90]}')

c = json.dumps({'meta': {'updated_at': 'X', 'total': 435},
                'results': [1, 2, 3]}).encode()
d = json.dumps({'meta': {'updated_at': 'X', 'total': 999},
                'results': [1, 2, 3]}).encode()
chk('**实质差异**（total 435 vs 999）→ 归一化后仍不同',
    det._normalize('match_result.json', c) != det._normalize('match_result.json', d))

print('─── 文本归一化（匹配报告.md 的耗时）───')
ma = '- 耗时：10.8s\n特性 X: 已配置'.encode()
mb = '- 耗时：11.0s\n特性 X: 已配置'.encode()
chk('耗时不同 → 归一化后相同',
    det._normalize('匹配报告.md', ma) == det._normalize('匹配报告.md', mb))

mc = '- 耗时：10.8s\n特性 X: 已配置'.encode()
md = '- 耗时：10.8s\n特性 X: 未配置'.encode()
chk('**实质差异**（已配置 vs 未配置）→ 归一化后仍不同',
    det._normalize('匹配报告.md', mc) != det._normalize('匹配报告.md', md))

print('─── 未登记的二进制文件不动 ───')
blob = bytes(range(256))
chk('未知文件原样返回', det._normalize('graph.json', blob) == blob)

print(f'\n结果: {ok}/{ok + fail} 通过')
sys.exit(1 if fail else 0)

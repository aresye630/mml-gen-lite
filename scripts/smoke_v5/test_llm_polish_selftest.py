#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""llm_polish 自证：验证修改点真的有判别力（正/反/边界成对）。

覆盖（每一项都必须能「通过"正确"、拒绝"错误"」）：
  ① 局点信息运行时注入 —— 不得出现硬编码数字
  ② 模型名默认值 —— 不得是存疑名字
  ③ 显式成败 —— 无 key 时必须返回 status='no_key'，不是裸 None
  ④ JSON 提取 —— 三种正例（纯 JSON/围栏/前后有噪音）必须过；
                 三种反例（无 JSON/不平衡/空）必须拒绝
"""
import json
import os
import re
import sys
from pathlib import Path

sys.path.insert(0, '/opt/expgv/scripts/exp_analysis_code')
import llm_polish as L   # noqa: E402

SRC = Path('/opt/expgv/scripts/exp_analysis_code/llm_polish.py').read_text(encoding='utf-8')
PASS, FAIL = [], []


def check(name, cond, detail=''):
    (PASS if cond else FAIL).append(name)
    print(f'  {"✓" if cond else "✗"} {name}' + (f'  — {detail}' if detail else ''))


print('═══ ① 局点信息运行时注入（禁硬编码）═══')
# 反：源码里不得有硬编码的命令数
bad_hard = re.findall(r'（(\d{4,})\s*条命令）', SRC)
check('源码无硬编码命令数', not bad_hard, f'发现 {bad_hard}' if bad_hard else '')
# 正：prompt 应随 report 变化
r1 = {'meta': {'ne_name': 'AAA'}, 'stats': {'cmd_count': 111}}
r2 = {'meta': {'ne_name': 'BBB'}, 'stats': {'cmd_count': 222}}
p1 = L._build_prompt(r1)
p2 = L._build_prompt(r2)
check('prompt 含 ne_name（AAA）', 'AAA' in p1)
check('prompt 含 cmd_count（111）', '111' in p1)
check('不同 report → 不同 prompt', p1 != p2)
# 边界：meta/stats 缺字段时不得崩
try:
    p3 = L._build_prompt({})
    check('缺 meta/stats 不崩（边界）', '未知网元' in p3)
except Exception as e:
    check('缺 meta/stats 不崩（边界）', False, repr(e))

print()
print('═══ ② 模型名默认值 ═══')
check("默认模型非 'deepseek-v4-pro'（存疑名）",
      L.MODEL != 'deepseek-v4-pro', f'当前默认 {L.MODEL}')
check('默认模型非空', bool(L.MODEL))

print()
print('═══ ③ 显式成败（不得返回裸 None）═══')
# 正：无 key 时应是 no_key
saved = L._load_key
L._load_key = lambda: None
try:
    out = L.polish({'meta': {}, 'stats': {}})
    check("无 key → status='no_key'", isinstance(out, dict) and out.get('status') == 'no_key',
          str(out)[:80])
    check('返回结构含 reason', isinstance(out, dict) and 'reason' in out)
finally:
    L._load_key = saved
# 反：不应再返回裸 None
check('不再返回裸 None', out is not None)

print()
print('═══ ④ JSON 提取（正/反/边界成对）═══')
pos = [
    ('纯 JSON', '{"conclusion": "ok"}'),
    ('markdown 围栏', '```json\n{"conclusion": "ok"}\n```'),
    ('前后有噪音', '好的，结果如下：\n{"conclusion": "ok"}\n以上。'),
    ('含嵌套大括号', '{"a": {"b": 1}, "c": 2}'),
    ('字符串内含大括号', '{"a": "内容 {不是结构}", "b": 2}'),
]
for name, txt in pos:
    try:
        d = L._extract_json(txt)
        check(f'正例·{name}', isinstance(d, dict) and len(d) > 0)
    except Exception as e:
        check(f'正例·{name}', False, repr(e))

neg = [
    ('无 JSON', '完全没有任何 JSON 的内容'),
    ('大括号不平衡', '{"a": 1'),
    ('空字符串', ''),
]
for name, txt in neg:
    try:
        L._extract_json(txt)
        check(f'反例·{name} 应被拒绝', False, '竟然通过了')
    except Exception:
        check(f'反例·{name} 应被拒绝', True)

print()
print('═══ ⑤ 两段 JSON 只取第一段（贪婪正则会连起来，属回归守卫）═══')
two = '{"first": 1}\n随便的话\n{"second": 2}'
try:
    d = L._extract_json(two)
    check('只取第一段', d == {'first': 1}, json.dumps(d, ensure_ascii=False))
except Exception as e:
    check('只取第一段', False, repr(e))

print()
print('═' * 56)
print(f'  通过 {len(PASS)} / {len(PASS) + len(FAIL)}')
if FAIL:
    print('  失败项:')
    for f in FAIL:
        print(f'    ✗ {f}')
    raise SystemExit(1)
print('  ✅ 全部通过 —— 修改点均具判别力')

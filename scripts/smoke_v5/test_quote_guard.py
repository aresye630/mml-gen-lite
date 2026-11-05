#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""引号一致性守卫（冒烟用例）。

判据（md 官方示例是引号形态的权威源）：
  md `X="<占位>"` → 输出必须 `X="值"`
  md `X=<占位>`   → 输出必须 `X=值`
例外：现网 EXP 覆盖（origin=prefill_exp）时按现网值的原形。
"""
import sys
sys.path.insert(0, '/opt/expgv/backend')
import gen_assemble as ga
from pathlib import Path

P = F = 0


def case(name, ok, detail=''):
    global P, F
    if ok:
        P += 1
        print('  ✓ %s  %s' % (name, detail))
    else:
        F += 1
        print('  ✗ %s  %s' % (name, detail))


def check_md(md_text, label, intent=''):
    try:
        f = ga.assemble_feature('F1', md_text)
        s = ga.build_schema([f], {'product': 'UNC', 'nf': 'UPF', 'exp_version': 'v1',
                                  'intent_text': intent})
        mml = ga.schema_to_mml(s)
    except Exception as e:
        case('%s 装配' % label, False, '%s: %s' % (type(e).__name__, e))
        return

    n_bad = n_tot = 0
    bad = []
    for st in s['steps']:
        ex = st.get('example') or ''
        if not ex:
            continue
        _, p_md = ga.parse_mml_cmd(ex)
        same = [x for x in s['steps'] if x['command'] == st['command']]
        k = same.index(st)
        lines = [l for l in mml.split('\n') if l.startswith(st['command'] + ':')]
        if k >= len(lines):
            continue
        _, p_out = ga.parse_mml_cmd(lines[k])
        for nm, raw in p_md.items():
            if nm not in p_out:
                continue
            # 现网覆盖的值不参与（引号照现网值原形）
            src = [p for p in st['params'] if p['name'] == nm]
            if src and src[0].get('origin') == 'prefill_exp':
                continue
            n_tot += 1
            if raw.startswith('"') == p_out[nm].startswith('"'):
                pass
            else:
                n_bad += 1
                bad.append('%s %s md=%s out=%s' % (st['command'], nm, raw[:16], p_out[nm][:16]))
    case('%s 引号一致' % label, n_bad == 0, '%d/%d 一致%s' % (
        n_tot - n_bad, n_tot, ('  ' + '; '.join(bad[:3])) if bad else ''))


print('=== 引号守卫（确定性路径）===')
check_md('# T\n\n## 1. 特性完整内容\n\n## 2. 官方示例命令\n\n```mml\n'
         'ADD UPNODE:NFINSTANCENAME="<UPFINSTANCEID>", LOCATION=<LOCATION>, '
         'LOCK=FALSE, VPNNAME="<VPNNAME>";\n```\n\n## 3. 现网实例\n', '带引号占位符')
check_md('# T\n\n## 1. 特性完整内容\n\n## 2. 官方示例命令\n\n```mml\n'
         'ADD SRROUTE:VRFNAME="vrf1",AFTYPE=ipv4unicast,MASKLENGTH=24,'
         'NEXTHOP="1.1.1.1";\n```\n\n## 3. 现网实例\n', '无引号枚举')
check_md('# T\n\n## 1. 特性完整内容\n\n## 2. 官方示例命令\n\n```mml\n'
         'ADD PNFPROFILE:IPV6ADDRESS2="::",PORT=<PORT>,LOAD=0,'
         'NFTYPE="NfUPF";\n```\n\n## 3. 现网实例\n', ':: 与数字')

print()
print('=== 值完整性守卫 ===')
md2 = ('# T\n\n## 1. 特性完整内容\n\n## 2. 官方示例命令\n\n```mml\n'
       'ADD UPNODE:LOCK=FALSE,SHAREDUPFSW=DISABLE,NGLANSW=DISABLE;'
       '\n```\n\n## 3. 现网实例\n')
f2 = ga.assemble_feature('F1', md2)
s2 = ga.build_schema([f2], {'product': 'UNC', 'exp_version': 'v1'})
mml2 = ga.schema_to_mml(s2)
line2 = [l for l in mml2.split('\n') if l.startswith('ADD UPNODE')]
line2 = line2[0] if line2 else ''
_, p2 = ga.parse_mml_cmd(line2)
for k, v in (('LOCK', 'FALSE'), ('SHAREDUPFSW', 'DISABLE'), ('NGLANSW', 'DISABLE')):
    case('md 值 %s' % k, p2.get(k) == v, 'out=%s' % p2.get(k))
case('命令参数完整', len(p2) == 3, '%d 个参数' % len(p2))

print()
print('=== raw 新鲜度守卫（防模型补值被 raw 屏蔽）===')
# 场景：md 原文含 <占位>，params.value 已被模型补成实值
# 期望：输出实值（不是 md 原文里的 <占位>）
import json as _json
_steps = [{
    'step_no': 1, 'command': 'ADD UPNODE', 'cmd_step': '步骤1',
    'raw': 'ADD UPNODE:NFINSTANCENAME="<X>", LOCK=FALSE;',
    'params': [
        {'name': 'NFINSTANCENAME', 'value': 'upf_gz01', 'origin': 'generated_model',
         'note': '', 'quote': True},
        {'name': 'LOCK', 'value': 'FALSE', 'origin': 'doc', 'note': '', 'quote': False},
    ],
}]
_s = {'meta': {'feature': 'T', 'features': [], 'product': 'UNC'}, 'steps': _steps}
_m = ga.schema_to_mml(_s)
_line = [l for l in _m.split('\n') if l.startswith('ADD UPNODE')]
_line = _line[0] if _line else ''
case('补值不被 raw 屏蔽', 'upf_gz01' in _line and '<X>' not in _line, _line[:70])
case('补值引号照 md', 'NFINSTANCENAME="upf_gz01"' in _line, _line[:70])

# 反向：raw 未被改（值全同 md 原文）→ 仍走直出，保原序
_steps2 = [{
    'step_no': 1, 'command': 'ADD UPNODE', 'cmd_step': '步骤1',
    'raw': 'ADD UPNODE:NFTYPE=NfUPF, LOCK=FALSE;',
    'params': [
        {'name': 'NFTYPE', 'value': 'NfUPF', 'origin': 'prefill_exp', 'note': '', 'quote': False},
        {'name': 'LOCK', 'value': 'FALSE', 'origin': 'doc', 'note': '', 'quote': False},
    ],
}]
_s2 = {'meta': {'feature': 'T', 'features': [], 'product': 'UNC'}, 'steps': _steps2}
_m2 = ga.schema_to_mml(_s2)
_l2 = [l for l in _m2.split('\n') if l.startswith('ADD UPNODE')]
_l2 = _l2[0] if _l2 else ''
case('raw 未过期仍直出（保原序）', _l2 == 'ADD UPNODE:NFTYPE=NfUPF, LOCK=FALSE;', _l2[:70])

print()
print('=== 业务注释守卫（防 md 注释丢失 / 来源统计污染）===')
import sys as _sys
_sys.path.insert(0, '/opt/expgv/backend')
import agent_projection as _ap
_md = ('# T\n\n## 2. 官方示例命令\n\n```mml\n'
       '// A-2 【条件】仅当本次引入新切片时才需声明\n'
       '//     现网已存在 NSIDX=0,SST=1 — 沿用则整步跳过\n'
       '//     ⚠ 须与 AMF/NSSF 侧配套（跨 NF）\n'
       'ADD PLMNNS:NSIDX=<NSIDX>, SST=<SST>, SD="<SD>";\n'
       '```\n')
_st = _ap.extract_md_steps(_md)
_cmts = (_st[0].get('comments') or []) if _st else []
case('md 注释被收集（命令上方）', len(_cmts) == 3, '%d 条' % len(_cmts))
case('注释归属正确命令', bool(_cmts) and 'A-2' in _cmts[0], _cmts[0][:40] if _cmts else '')
case('⚠ 风险注释保留', any('跨 NF' in c for c in _cmts), '')

_s2 = {'meta': {'feature': 'T', 'features': [], 'product': 'UNC'}, 'steps': _st}
_m2 = ga.schema_to_mml(_s2)
case('业务注释渲染到 mml', 'A-2 【条件】' in _m2 and '整步跳过' in _m2, '')
case('来源统计不再出现', '来源：继承' not in _m2 and '×' not in _m2.replace('⚠', ''), '')

print()
print('结果: %d 通过, %d 失败' % (P, F))
sys.exit(1 if F else 0)

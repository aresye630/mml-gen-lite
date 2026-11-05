#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""chain_by_linkgroups 判据自证 —— 正例/反例/边界成对出现。

判据（用户 2026-09-18 明确的口径）：
  严格口径: enum_vals 是「该特性文档示例用的值」，现网用了别的值（哪怕合法）
            也判「不符」→ 命令不算命中。判定对象是「是否按该特性文档配置」。

三态:
  ✅ hit      命令存在 且 枚举参数符合文档示例值
  ❌ enum_bad 命令存在 但 参数值与文档示例不同
  ⛔ absent   现网无此命令

运行: python3 test_linkgroups_selftest.py   （退出码 0=全绿）
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
import chain_by_linkgroups as C    # noqa: E402

FAIL = []


def check(name, got, want):
    ok = got == want
    print('  %s %s' % ('✓' if ok else '✗', name))
    if not ok:
        print('      期望 %r 得到 %r' % (want, got))
        FAIL.append(name)


def main():
    print('=' * 70)
    print('1) _norm 归一化 —— 大小写/引号/空白容忍')
    print('=' * 70)
    check('去引号', C._norm('"cmnet"'), 'CMNET')
    check('单引号', C._norm("'cmnet'"), 'CMNET')
    check('大小写', C._norm('Enable'), 'ENABLE')
    check('空白', C._norm('  TCP  '), 'TCP')
    check('数字', C._norm(1008), '1008')

    print()
    print('=' * 70)
    print('2) enum_bad —— 严格口径（枚举不符即判错）')
    print('=' * 70)
    feat = {'enum_vals': {'SET APNACCESSWAL': {'SWITCH': ['ENABLE']},
                          'ADD FILTER': {'L34PROTOCOL': ['TCP']}}}
    # 正例：值与文档示例一致 → 无不符
    check('正例·值一致',
          C.enum_bad({'cmd': 'SET APNACCESSWAL',
                      'params': {'SWITCH': 'ENABLE'}}, feat), [])
    # 反例：值不同（哪怕合法）→ 不符
    r = C.enum_bad({'cmd': 'SET APNACCESSWAL',
                    'params': {'SWITCH': 'DISABLE'}}, feat)
    check('反例·开关反着配(DISABLE≠ENABLE)', len(r), 1)
    # 反例：多值枚举用了另一个合法值 → 仍判不符（用户明确）
    r2 = C.enum_bad({'cmd': 'ADD FILTER',
                     'params': {'L34PROTOCOL': 'ANY'}}, feat)
    check('反例·ANY≠TCP(严格口径)', len(r2), 1)
    # 边界：命令不在 enum_vals 里 → 不校验
    check('边界·命令无契约',
          C.enum_bad({'cmd': 'ADD URR', 'params': {'X': 'Y'}}, feat), [])
    # 边界：参数没给 → 不校验（可选参数）
    check('边界·参数缺失',
          C.enum_bad({'cmd': 'ADD FILTER', 'params': {}}, feat), [])
    # 边界：大小写不同 → 归一后一致，不算不符
    check('边界·大小写容忍',
          C.enum_bad({'cmd': 'ADD FILTER',
                      'params': {'L34PROTOCOL': 'tcp'}}, feat), [])
    # 边界：无 enum_vals 的特性
    check('边界·特性无enum_vals',
          C.enum_bad({'cmd': 'ADD FILTER',
                      'params': {'L34PROTOCOL': 'ANY'}}, {}), [])

    print()
    print('=' * 70)
    print('3) judge_cmd_presence —— 三态判定')
    print('=' * 70)
    exp_idx = {
        'SET APNACCESSWAL': [{'cmd': 'SET APNACCESSWAL', 'seq': 100,
                              'params': {'SWITCH': 'DISABLE'}, 'raw': 'x'}],
        'ADD URR': [{'cmd': 'ADD URR', 'seq': 200,
                     'params': {'URRNAME': 'a'}, 'raw': 'y'}],
    }
    feat2 = {'enum_vals': {'SET APNACCESSWAL': {'SWITCH': ['ENABLE']}}}
    # 反例态：命令在但枚举不符
    r = C.judge_cmd_presence('SET APNACCESSWAL', feat2, exp_idx)
    check('态·命令在不符存在', r['exists'], True)
    check('态·命令在不符条数', len(r['insts']), 1)
    # 命中态
    r2 = C.judge_cmd_presence('ADD URR', feat2, exp_idx)
    check('态·无契约命令存在', r2['exists'], True)
    # 缺失态
    r3 = C.judge_cmd_presence('ADD NOTEXIST', feat2, exp_idx)
    check('态·命令不存在', r3['exists'], False)

    print()
    print('=' * 70)
    print('4) assemble_groups —— link_groups 归一')
    print('=' * 70)
    f = {'link_groups': [
        {'occ': [['ADD VPNINST', 'VPNINSTANCE'], ['ADD APN', 'VPNINSTANCE']],
         'ex': ['vpn1']},
        {'occ': [['ADD LACGROUP', 'LACGROUPNAME'],
                 ['ADD LACID', 'LACGROUPNAME'],
                 ['ADD POOLGRPMAP', 'LOCATIONGRPNAME']],
         'ex': ['lac1']},
    ]}
    gs = C.assemble_groups(f)
    check('组数', len(gs), 2)
    check('组1 命令', gs[0]['cmds'], ['ADD VPNINST', 'ADD APN'])
    check('组1 参数', gs[0]['params'], ['VPNINSTANCE'])
    check('组2 命令数', len(gs[1]['cmds']), 3)
    check('组2 参数(两个)', gs[1]['params'],
          ['LACGROUPNAME', 'LOCATIONGRPNAME'])
    # 边界：空 link_groups
    check('边界·无link_groups', C.assemble_groups({}), [])
    check('边界·空列表', C.assemble_groups({'link_groups': []}), [])

    print()
    print('=' * 70)
    print('5) group_instances —— 按值聚合 + enum 过滤')
    print('=' * 70)
    g = {'cmds': ['ADD APN', 'SET APNADDRESSATTR'], 'params': ['APN']}
    idx2 = {
        'ADD APN': [
            {'cmd': 'ADD APN', 'seq': 10, 'params': {'APN': 'cmnet'},
             'raw': 'a'},
            {'cmd': 'ADD APN', 'seq': 11, 'params': {'APN': 'ims'},
             'raw': 'b'},
        ],
        'SET APNADDRESSATTR': [
            {'cmd': 'SET APNADDRESSATTR', 'seq': 20,
             'params': {'APN': 'cmnet'}, 'raw': 'c'},
        ],
    }
    # cmnet: 两条都有 → 完整；ims: 只有一条 → 不完整
    insts = C.group_instances(g, {}, idx2, [])
    check('实例数', len(insts), 2)
    byval = {i['value']: i for i in insts}
    check('CMNET 完整', byval['CMNET']['complete'], True)
    check('IMS 不完整', byval['IMS']['complete'], False)
    check('IMS 缺谁', byval['IMS']['absent'], ['SET APNADDRESSATTR'])
    check('完整链排在前', insts[0]['value'], 'CMNET')

    print()
    print('=' * 70)
    print('6) 端到端渲染 —— 三态在 MD 中正确表达')
    print('=' * 70)
    feat3 = {
        'title': '测试特性',
        'doc_path': 'x.md',
        'core': {'L1': ['ADD A'], 'L2': [], 'L3': ['ADD C']},
        'prereq': ['ADD D'],
        'license': {},
        'enum_vals': {'ADD A': {'FLAG': ['ENABLE']}},
        'link_groups': [],
    }
    idx3 = {
        'ADD A': [{'cmd': 'ADD A', 'seq': 1,
                   'params': {'FLAG': 'DISABLE'}, 'raw': 'ADD A:FLAG=DISABLE;'}],
        'ADD C': [{'cmd': 'ADD C', 'seq': 2, 'params': {}, 'raw': 'ADD C;'}],
    }
    md = C.render_feature('T001', feat3, [], idx3)
    check('MD 含 ❌ 枚举不符', '❌ ADD A' in md, True)
    check('MD 含 ✅ 命中', '✅ ADD C' in md, True)
    check('MD 含 ⛔ 未配置', '⛔ ADD D' in md, True)
    check('MD 含三态结论', '枚举不符 1' in md and '未配置 1' in md, True)

    print()
    print('=' * 70)
    if FAIL:
        print('✗ 失败 %d 项: %s' % (len(FAIL), ', '.join(FAIL)))
        sys.exit(1)
    print('✓ 全部通过')
    print('=' * 70)


if __name__ == '__main__':
    main()

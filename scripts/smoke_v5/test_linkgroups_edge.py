#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""验证6：边界与异常输入。

覆盖：
  1. 空 link_groups / 无 link_groups / link_groups 为空列表
  2. occ 为空 / occ 只有一条命令（单命令组）
  3. 命令在指纹里但 EXP 完全没有（未配置）
  4. 参数名在指纹里有但 EXP 命令没用该参数
  5. 超大组（一个值关联几千条）
  6. 特性缺 title / doc_path / core
  7. 值含特殊字符（& / 引号 / 中文）
"""
import sys
from pathlib import Path

sys.path.insert(0, '/opt/expgv/scripts')
import chain_by_linkgroups as C    # noqa: E402

FAIL = []


def check(name, got, want):
    ok = got == want
    print('  %s %s' % ('✓' if ok else '✗', name))
    if not ok:
        print('      期望 %r 得到 %r' % (want, got))
        FAIL.append(name)


def t_empty_groups():
    print('1) 空/无 link_groups')
    check('无 key', C.assemble_groups({}), [])
    check('空列表', C.assemble_groups({'link_groups': []}), [])
    check('occ 空', C.assemble_groups({'link_groups': [{'occ': []}]}), [])
    md = C.render_feature('T', {'title': 'x', 'core': {'L1': ['ADD A']}},
                          [], {})
    check('渲染不炸', isinstance(md, str) and len(md) > 0, True)
    check('走开关分支', '无链装配组' in md, True)


def t_single_cmd_group():
    print('2) 单命令组')
    f = {'link_groups': [{'occ': [['ADD APN', 'APN']]}]}
    gs = C.assemble_groups(f)
    check('组数', len(gs), 1)
    check('命令', gs[0]['cmds'], ['ADD APN'])
    idx = {'ADD APN': [{'cmd': 'ADD APN', 'seq': 1,
                        'params': {'APN': 'a'}, 'raw': 'x'}]}
    insts = C.group_instances(gs[0], f, idx, [])
    check('实例数', len(insts), 1)
    check('单命令组即完整', insts[0]['complete'], True)


def t_absent_cmd():
    print('3) 命令在指纹里但 EXP 没有')
    f = {'link_groups': [{'occ': [['ADD XX', 'NAME'], ['ADD YY', 'NAME']]}]}
    md = C.render_feature('T', {'title': 'x', 'core': {'L1': ['ADD XX']},
                                'link_groups': f['link_groups']}, [], {})
    check('报未配置', '未配置' in md or '现网无实例' in md, True)


def t_param_missing():
    print('4) 指纹参数 EXP 命令没用')
    g = {'cmds': ['ADD APN', 'SET X'], 'params': ['APN']}
    idx = {'ADD APN': [{'cmd': 'ADD APN', 'seq': 1,
                        'params': {'APN': 'a'}, 'raw': 'x'}],
           'SET X': [{'cmd': 'SET X', 'seq': 2, 'params': {}, 'raw': 'y'}]}
    insts = C.group_instances(g, {}, idx, [])
    # SET X 没有 APN 参数 → 归到 absent
    check('实例数', len(insts), 1)
    check('SET X 视为缺', insts[0]['absent'], ['SET X'])


def t_huge_group():
    print('5) 超大组（5000 条实例）')
    # 注意：render_feature 收的是「原始指纹格式」（occ），
    # group_instances 收的是 assemble_groups 归一后的格式（cmds/params）
    raw_g = {'occ': [['ADD A', 'N'], ['ADD B', 'N']], 'ex': ['v0']}
    g = C.assemble_groups({'link_groups': [raw_g]})[0]
    insts_a = [{'cmd': 'ADD A', 'seq': i, 'params': {'N': f'v{i}'},
                'raw': f'ADD A:N=v{i};'} for i in range(5000)]
    insts_b = [{'cmd': 'ADD B', 'seq': i + 10000, 'params': {'N': f'v{i}'},
                'raw': f'ADD B:N=v{i};'} for i in range(5000)]
    insts = C.group_instances(g, {}, {'ADD A': insts_a, 'ADD B': insts_b}, [])
    check('实例数', len(insts), 5000)
    check('全完整', all(x['complete'] for x in insts), True)
    md = C.render_feature('T', {'title': 'x', 'link_groups': [raw_g]}, [],
                          {'ADD A': insts_a, 'ADD B': insts_b})
    check('渲染有折叠提示', ('同形态折叠' in md), True)
    check('产物不算爆炸', len(md.splitlines()) < 200, True)


def t_missing_meta():
    print('6) 缺 title/doc_path/core')
    for f in ({}, {'title': ''}, {'core': None}):
        try:
            md = C.render_feature('T001', f, [], {})
            ok = isinstance(md, str) and 'T001' in md
        except Exception as e:      # noqa: BLE001
            ok = f'异常 {e}'
        check('容错 %r' % (list(f.keys()) or '空'), ok, True)


def t_special_chars():
    print('7) 值含特殊字符')
    f = {'link_groups': [{'occ': [['ADD A', 'N'], ['ADD B', 'N']]}]}
    idx = {
        'ADD A': [{'cmd': 'ADD A', 'seq': 1,
                   'params': {'N': '&mk_1001_x'}, 'raw': 'x'}],
        'ADD B': [{'cmd': 'ADD B', 'seq': 2,
                   'params': {'N': '&mk_1001_x'}, 'raw': 'y'}],
    }
    gs = C.assemble_groups(f)
    insts = C.group_instances(gs[0], {}, idx, [])
    check('& 值聚合', len(insts), 1)
    check('& 值完整', insts[0]['complete'], True)
    md = C.render_feature('T', {'title': 'x', 'link_groups': f['link_groups']},
                          [], idx)
    check('MD 含 & 值', '&mk_1001_x' in md or '&MK_1001_X' in md, True)


if __name__ == '__main__':
    t_empty_groups()
    print()
    t_single_cmd_group()
    print()
    t_absent_cmd()
    print()
    t_param_missing()
    print()
    t_huge_group()
    print()
    t_missing_meta()
    print()
    t_special_chars()
    print()
    print('=' * 70)
    if FAIL:
        print('✗ 失败 %d 项: %s' % (len(FAIL), ', '.join(FAIL)))
        sys.exit(1)
    print('✓ 边界全部通过')

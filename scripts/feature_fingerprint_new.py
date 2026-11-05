#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""新格式特性指纹（S1 命令关联）：数据驱动重建关联组 / definer / 命令三类。

替代旧 `_s1_fingerprint.py` 的 anchor_vals 值共享 + is_name_value + 并查集启发式。

核心规则（零硬编码命令名/参数名，全部来自新格式 params 段字段）：
  1. 命令链顺序   = commands 段模板顺序（list2cmd 保序，权威）
  2. 名字参数     = type=string 且无 enum（对象名/属性名）；integer/枚举不参与关联
  3. 参数语义     = data_source：
       定义方 = {本端规划, 与对端协商, 全网规划}（对象由本特性定义）
       引用方 = {已配置数据中获取}（引用已配置对象）
       属性   = 其余（空/参见LLD，外部值）
  4. 引用关系     = 引用方参数 → 定义方参数：
       主：description 里的 `**ADD XXX**` 标记 → 目标命令 → 其定义方参数
       兜底：参数名相同（引用方参数名 == 某定义方参数名）
  5. 关联组       = 定义方参数 + 指向它的引用方参数
       - 有引用方指向的定义方 → 引用组，definer = 定义方命令（链序最早）
       - 无引用方指向的定义方（如 SVRIP）→ 属性组，definer=None
       - 悬空引用方（如 PROTOCOLNAME）→ 属性组，definer=None
  6. 命令三类     = object(有定义方参数) / binding(仅引用方) / global(无名字参数)
"""
import re
from collections import defaultdict

DEFINER_DS = {'本端规划', '与对端协商', '全网规划'}
REF_DS = {'已配置数据中获取'}
CMD_RE = re.compile(r'\*\*([A-Z]+ [A-Z0-9]+)\*\*')


def _is_name_value(v):
    """值形态启发式：值含小写/点/下划线 = 自定义名/IP/对象名（复现旧 is_name_value）。

    新格式无法用 data_source 区分「对象名」与「授权项」（如 LICITEM 值
    'LKV3G5HCAS01' 纯大写+数字无下划线，属功能标识而非对象名），故保留此值形态判定，
    但输入改为 examples 结构化示例值（比旧 md 正则抠 anchor_vals 可靠）。
    下划线（PPG_URL / L7_URL / UrrGp_URL）是对象名常见分隔符，须识别为名字值；
    纯大写字母+数字（LKV3G5HCAS01）才是功能标识。
    """
    return bool(re.search(r'[a-z._]', str(v)))


def _examples_vals(newdoc):
    """examples（{list_name: [dict]}）→ {(cmd,param): set(值)}。"""
    list2cmd = newdoc['list2cmd']
    out = {}
    for list_name, items in (newdoc.get('examples') or {}).items():
        cmd = list2cmd.get(list_name)
        if not cmd:
            continue
        for it in items:
            if not isinstance(it, dict):
                continue
            for p, v in it.items():
                if v not in (None, ''):
                    out.setdefault((cmd, p), set()).add(v)
    return out


def build_fingerprint(newdoc):
    cmd_meta = newdoc['cmd_meta']
    list2cmd = newdoc['list2cmd']
    ex_vals = _examples_vals(newdoc)

    # ── 1. 命令链顺序（list2cmd 保序 = commands 段模板顺序）──
    cmd_order = list(list2cmd.values())
    cmd_rank = {c: i for i, c in enumerate(cmd_order)}

    # ── 2. 名字参数（type=string + 无 enum + examples 值含小写/点）──
    name_params = defaultdict(set)   # cmd -> 名字参数集合
    param_ds = {}                    # (cmd,param) -> data_source
    param_desc = {}                  # (cmd,param) -> description
    for cmd, meta in cmd_meta.items():
        for pname, p in meta['params'].items():
            if not isinstance(p, dict):
                continue
            ds = p.get('data_source') or ''
            param_ds[(cmd, pname)] = ds
            param_desc[(cmd, pname)] = p.get('description', '') or ''
            typ = p.get('type') or ''
            if typ == 'string' and not p.get('enum'):
                vals = ex_vals.get((cmd, pname), set())
                if vals and all(_is_name_value(v) for v in vals):
                    name_params[cmd].add(pname)

    # ── 3. 定义方参数（data_source 定义方 + 名字参数）──
    definer_param_cmd = {}
    for (cmd, pname), ds in param_ds.items():
        if pname in name_params.get(cmd, set()) and ds in DEFINER_DS:
            if pname not in definer_param_cmd or cmd_rank[cmd] < cmd_rank[definer_param_cmd[pname]]:
                definer_param_cmd[pname] = cmd

    # ── 4. 引用关系：引用方参数 → 目标定义方参数 ──
    #    引用方判定：ds ∈ REF_DS，或 desc 含 **ADD/SET XXX** 标记（文档标注不一致兜底，
    #    如 GWFD POLICYNAME ds="" 但 desc 有「已通过**ADD PCCPOLICYGRP**命令配置」）。
    ref_to_def = {}
    for (cmd, pname), ds in param_ds.items():
        if pname not in name_params.get(cmd, set()):
            continue
        desc = param_desc[(cmd, pname)]
        has_ref_mark = bool(CMD_RE.search(desc))
        if ds not in REF_DS and not has_ref_mark:
            continue
        target = None
        for ref in CMD_RE.findall(desc):
            if ref.startswith(('ADD ', 'SET ')):
                for dp, dc in definer_param_cmd.items():
                    if dc == ref:
                        target = dp
                        break
                if target:
                    break
        if target is None and pname in definer_param_cmd:
            target = pname
        if target:
            ref_to_def[(cmd, pname)] = target

    # ── 5. 关联组 ──
    groups = []
    claimed = set()
    for dp, dc in definer_param_cmd.items():
        refs = [(c, p) for (c, p), t in ref_to_def.items() if t == dp]
        for c, p in refs:
            claimed.add((c, p))
        params = {dp} | {p for _, p in refs}
        groups.append({
            'params': frozenset(params),
            'definer': dc if refs else None,
            'def_param': dp,
            'occ': sorted([(dc, dp)] + refs, key=lambda x: (cmd_rank.get(x[0], 999), x[1])),
        })
    # 悬空引用方（无目标定义方）→ 属性组
    for (cmd, pname), ds in param_ds.items():
        if pname in name_params.get(cmd, set()) and ds in REF_DS and (cmd, pname) not in claimed:
            groups.append({
                'params': frozenset({pname}),
                'definer': None, 'def_param': pname,
                'occ': [(cmd, pname)],
            })

    # ── 6. 命令三类 ──
    cmd_class = {}
    for cmd in cmd_order:
        nps = name_params.get(cmd, set())
        if not nps:
            cmd_class[cmd] = 'global'
            continue
        has_definer = any(
            param_ds.get((cmd, p)) in DEFINER_DS and any(t == p for t in ref_to_def.values())
            for p in nps
        )
        if has_definer:
            cmd_class[cmd] = 'object'
        else:
            has_ref = any(param_ds.get((cmd, p)) in REF_DS for p in nps)
            cmd_class[cmd] = 'binding' if has_ref else 'object'

    return {
        'cmd_order': cmd_order,
        'cmd_rank': cmd_rank,
        'name_params': {k: sorted(v) for k, v in name_params.items()},
        'definer_param_cmd': definer_param_cmd,
        'ref_to_def': {f'{c}.{p}': t for (c, p), t in ref_to_def.items()},
        'link_groups': groups,
        'cmd_class': cmd_class,
    }


if __name__ == '__main__':
    import sys
    import json
    sys.path.insert(0, 'scripts')
    import parse_new_format as pnf
    p = sys.argv[1] if len(sys.argv) > 1 else os.path.join(
        os.environ.get('MML_KB111_DIR', os.path.expanduser('~/workspace/kb111')),
        'UDG/UDG_配置HTTP计费防欺诈（能获取Server IP）_zh-CN.md')
    d = pnf.parse_new_format(p)
    fp = build_fingerprint(d)
    print('=== 命令链顺序 (%d) ===' % len(fp['cmd_order']))
    for i, c in enumerate(fp['cmd_order']):
        print(f'  {i:2d}. {c}')
    print('\n=== 关联组 + 定义方 (%d 组) ===' % len(fp['link_groups']))
    for g in fp['link_groups']:
        print(f'  params={sorted(g["params"])}')
        print(f'    definer={g["definer"]}  def_param={g["def_param"]}  occ={g["occ"]}')
    print('\n=== 命令三类划分 ===')
    for c in fp['cmd_order']:
        print(f'  {c:20s} -> {fp["cmd_class"][c]:8s}  名字参数={fp["name_params"].get(c, [])}')
    print('\n=== 全局命令 ===')
    print('  ', [c for c in fp['cmd_order'] if fp['cmd_class'][c] == 'global'])

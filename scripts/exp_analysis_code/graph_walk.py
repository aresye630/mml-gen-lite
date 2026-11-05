#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""graph_walk.py — EXP 图谱解析（P7）：实例级引用图走链（连通分量）。

与 p3_chains（链级粗判定：值集合 closed/dangling，不做实例级走链）不同，
本模块做「实例级」引用图走链：

  对象名值 v 是枢纽，连接「定义方（名字参数 = v）」与「引用方（任意参数 = v）」。
  值驱动 BFS —— 从入口对象名值出发，收集所有「含 v」的实例，再递归这些实例的
  「其他对象名值」。这天然支持跨参数同值聚合（HEADERENNAME=he_service 与
  POLICYNAME=he_service 同值，被 val_index['he_service'] 一并收集）。

维度约束（可选，数据驱动）：
  param_scope  参数白名单。指定后只桥接「白名单参数」的值，实现「维度约束」——
              避免从 RULE 命令同时沿「过滤维度」（FLOWFILTERNAME）和「计费维度」
              （PCCPOLICYGRPNM/SIGURRGRPNAME）走通整个 PCC 域。None = 全维度
              （完整连通分量，含计费维度）。
  cross_params 跨参数同值映射 {param: [param, ...]}（HEADERENNAME ↔ POLICYNAME 等）。
              这类「跨参数同值」是显式知识（跨网元对象名），由调用方数据驱动传入。

定位（与特性匹配解耦，见 rules/图谱分析测试case.md §一）：
  - 特性匹配回答「特性文档的模式是否在现网落地」（黄金规则核对）。
  - 图谱解析回答「现网某条业务链是否完整闭环」（连通分量走链）。
  tzq/he_service 服务链的「完整链」由本模块解决，不硬塞进特性黄金规则。

数据驱动红线：零局点实例值。对象名判定 = 值含下划线，或含小写字母+数字
（通用形态，排除纯大写枚举/功能标识、纯数字、协议词 http/dns、IP/版本）。
入口锚点、param_scope、cross_params 均由调用方传入，不写死。

输出（黄金规则格式，命令类型 → seq 列表 + 实例值 + 锚定参数）：
  commands:   {cmd: [(seq, {param: value})]}
  ref_degrees: {value: 引用次数}   ← 汇聚判别（引用次数高=汇聚链）
"""

import re
from collections import defaultdict

from p1_parse import parse_params

CMD_RE = re.compile(r'^([A-Z]+\s+[A-Z0-9]+)')
_LOW = re.compile(r'[a-z]')
_DIG = re.compile(r'\d')


def is_object_name(v):
    """对象名值判定：含下划线，或含小写字母+数字。

    排除：纯大写枚举（DISABLE/MSISDN1/RAT1）、纯数字（17516）、
    协议词（http/https/dns 无下划线无数字）、IP/版本（数字+点）。
    """
    s = str(v)
    if '_' in s:
        return True
    return bool(_LOW.search(s)) and bool(_DIG.search(s))


def build_index(commands):
    """commands {seq→line} → (inst, val_index)。

    inst[seq] = (cmd, params)
    val_index[v] = [(cmd, seq, param)]  # 值 v 出现的所有实例（含定义方与引用方）
    """
    inst = {}
    val_index = defaultdict(list)
    for seq, line in commands.items():
        m = CMD_RE.match(line)
        cmd = m.group(1) if m else line.split(':', 1)[0].strip()
        params = parse_params(line)
        inst[seq] = (cmd, params)
        for p, v in params.items():
            if v:
                val_index[v].append((cmd, seq, p))
    return inst, val_index


def walk(commands, entries, name_value_pred=None, param_scope=None, cross_params=None):
    """值驱动 BFS 走连通分量。

    entries:      入口对象名值列表（如 ['he_service']）。
    param_scope:  参数白名单（None=全参数）。只桥接「白名单参数」的值 → 维度约束。
    cross_params: {param: [param, ...]} 跨参数同值映射（显式知识）。
    返回 (visited_inst, visited_vals)：
      visited_inst {(cmd, seq): {param: value}}  — 连通分量所有实例 + 锚定参数
      visited_vals {value: n}                     — 对象名值 → 引用次数（汇聚判别）
    """
    pred = name_value_pred or is_object_name
    inst, val_index = build_index(commands)
    cross = cross_params or {}
    visited_inst = {}
    visited_vals = {}
    queue = list(entries)
    while queue:
        v = queue.pop()
        if v in visited_vals:
            continue
        hits = val_index.get(v, [])
        visited_vals[v] = len(hits)
        for (cmd, seq, p) in hits:
            d = visited_inst.setdefault((cmd, seq), {})
            d[p] = v
            # 桥接：实例的其他对象名值入队（受 param_scope 约束）
            for p2, v2 in inst[seq][1].items():
                if not v2 or v2 == v:
                    continue
                if not pred(v2):
                    continue
                if param_scope is not None and p2 not in param_scope:
                    continue
                if v2 not in visited_vals:
                    queue.append(v2)
    return visited_inst, visited_vals


def group(visited_inst):
    """按命令类型分组 → {cmd: [(seq, {param: value})]}（黄金规则格式，seq 升序）。"""
    grouped = defaultdict(list)
    for (cmd, seq), anchor in visited_inst.items():
        grouped[cmd].append((seq, anchor))
    out = {}
    for cmd, lst in grouped.items():
        lst.sort(key=lambda x: x[0])
        out[cmd] = lst
    return out


def run(commands, entries, name_value_pred=None, param_scope=None, cross_params=None):
    """图谱走链完整输出（供 pipeline 挂载与独立调试）。"""
    visited_inst, visited_vals = walk(commands, entries, name_value_pred,
                                      param_scope, cross_params)
    grouped = group(visited_inst)
    return {
        'entries': list(entries),
        'param_scope': list(param_scope) if param_scope is not None else None,
        'cross_params': cross_params or None,
        'commands': grouped,
        'ref_degrees': dict(visited_vals),
        'stats': {
            'instances': len(visited_inst),
            'cmd_types': len(grouped),
            'values': len(visited_vals),
        },
    }


def infer_param_definer(commands):
    """从 EXP 归纳「参数 → 定义方命令」映射（名字参数启发式，零局点值）。

    规则：参数名去 NAME/NM/ID/INSTANCE/NO 后缀 == 命令名去 verb 前缀（或互为子串）。
    返回 {param: set(cmd)}。用于推导「链维度参数白名单」。
    """
    inst, _ = build_index(commands)
    cmds = {cmd for cmd, _ in inst.values()}
    suffix = re.compile(r'(NAME|NM|ID|INSTANCE|NO|SW|FLAG|MODE|TYPE)$')
    definer = defaultdict(set)
    for cmd in cmds:
        base = re.sub(r'^(ADD|SET|LCK|MOD|RMV|DEL|DSP|SND)\s+', '', cmd)
        # 收集该命令下所有 *NAME 类参数
        params = set()
        for (c, prm) in inst.values():
            if c == cmd:
                params.update(prm.keys())
        for p in params:
            pbase = suffix.sub('', p)
            if not pbase:
                continue
            if pbase == base or base.startswith(pbase) or pbase.startswith(base) or base.endswith(pbase):
                definer[p].add(cmd)
    return dict(definer)


def discover_entries(commands, entry_cmd, entry_param):
    """从 EXP 提取 entry_cmd 的 entry_param 去重值集合（自动发现入口，零局点值）。"""
    inst, _ = build_index(commands)
    vals = set()
    for (cmd, params) in inst.values():
        if cmd == entry_cmd and entry_param in params:
            vals.add(params[entry_param])
    return sorted(vals)


def run_graphs(commands, schemas, entries_override=None):
    """对每条 graph 走链（入口自动发现），返回 {graph_id: result}。

    schemas: graph_schemas.yaml 的 graph 列表（数据驱动）。
    entries_override: {graph_id: [入口值, ...]} 指定入口（覆盖自动发现；测试/验证用）。
    """
    out = {}
    for schema in schemas:
        gid = schema['graph_id']
        entries = (entries_override or {}).get(gid)
        if entries is None:
            if not schema.get('auto_discover', True):
                continue  # 入口值多、不适合自动展开的 graph，默认跳过
            entries = discover_entries(commands, schema['entry_cmd'],
                                       schema['entry_param'])
        res = run(commands, entries, param_scope=schema.get('param_scope'))
        res['graph_id'] = gid
        res['name'] = schema.get('name', gid)
        res['entry_cmd'] = schema.get('entry_cmd')
        res['entry_param'] = schema.get('entry_param')
        res['cross_params'] = schema.get('cross_params')
        res['note'] = schema.get('note')
        out[gid] = res
    return out


if __name__ == '__main__':
    import json
    import sys
    from p1_parse import parse_exp
    exp = sys.argv[1] if len(sys.argv) > 1 else None
    entries = sys.argv[2].split(',') if len(sys.argv) > 2 else []
    scope = sys.argv[3].split(',') if len(sys.argv) > 3 and sys.argv[3] else None
    if not exp:
        print('usage: graph_walk.py <exp.txt> <entry1,entry2,...> [param_scope_csv]')
        sys.exit(1)
    parsed = parse_exp(exp)
    res = run(parsed['commands'], entries, param_scope=scope)
    print(json.dumps(res, ensure_ascii=False, indent=1))

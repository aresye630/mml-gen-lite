#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""graph_build.py — 全量引用关系图（B：命令关联关系全量链接）。

与 graph_walk（从入口走链）不同，本模块建立「全量图」，走链退化为「图上查询」。

节点：全部实例 seq（~102,275）
边：对象名值 v 的「定义方实例」↔「引用方实例」
  - 定义方实例：名字参数 = v（cmd ∈ param_definer[p]，即该命令自己的名字参数）
  - 引用方实例：引用参数 = v（cmd ∉ param_definer[p]，即引用别的对象）

用途：
  ① 助力特性实例查找（A：图上从锚点扩展找全）
  ② 助力配置生成（图上走链）

数据驱动红线：零局点实例值。param_definer 从 EXP 归纳，对象名判定通用形态
（含下划线 或 小写字母+数字）。全量图不绑定任何特性，是通用基础设施。
"""

from collections import defaultdict
from math import isqrt as _isqrt

from graph_walk import build_index, infer_param_definer, is_object_name


def build_graph(commands, fanout_limit=None):
    """建立全量引用关系图。

    fanout_limit: 单值扇出上限。0/None=不限制（旧行为）。
      背景（2026-09-15 修 OOM）：原实现对每个对象名值 v 建
      `len(definers) × len(referers)` 条双向边。大多数值只有个位数，
      但**枚举/占位符类值**（如 SPECIFICATION_LIMITED：8,640 定义方 × 3,063 引用方
      = 2,646 万条边，占全图 99.6%）会把内存推到 >7 GiB 触发 OOM-killer。
      这类值不是真实对象实例，把它们两两连边既无意义又必然爆内存。
      限制扇出只削减"巨型团"内部冗余边，不切断连通性（见下实现）。

    返回 dict：
      nodes:  {seq: cmd}
      adj:    {seq: [(neighbor_seq, {value, param, role})]}   # role ∈ {definer, referer}
      values: {value: {'definers': [(seq, param)], 'referers': [(seq, param)]}}
      stats:  {n_nodes, n_edges, n_values, n_cross_ne, n_orphan_def, n_ref_rel,
               n_capped_values}
    """
    inst, val_index = build_index(commands)
    param_definer = infer_param_definer(commands)

    def is_def(cmd, p):
        return cmd in param_definer.get(p, set())

    nodes = {}
    adj = defaultdict(list)
    values = {}
    n_edges = 0
    n_cross_ne = n_orphan_def = n_ref_rel = n_capped = 0

    for seq, (cmd, _params) in inst.items():
        nodes[seq] = cmd

    for v, hits in val_index.items():
        if not is_object_name(v):
            continue
        definers = [(seq, p) for (cmd, seq, p) in hits if is_def(cmd, p)]
        referers = [(seq, p) for (cmd, seq, p) in hits if not is_def(cmd, p)]
        values[v] = {'definers': definers, 'referers': referers}
        if definers and referers:
            n_ref_rel += 1
        elif definers and not referers:
            n_orphan_def += 1
        elif referers and not definers:
            n_cross_ne += 1
        # 双向边：定义方 ↔ 引用方（边带对方参数名与角色）
        # 扇出限制（2026-09-15）：对超限值按序抽样"代表"，保持两类节点都可达，
        # 但不再两两全连。连通性不破：抽样的定义方仍连到 (至少一个) 引用方、
        # 反之亦然 —— BFS 仍可跨越该值，只是不再产生平方级团内边。
        if fanout_limit and len(definers) * len(referers) > fanout_limit:
            n_capped += 1
            # 抽样"代表"：定义方取前 D 个、引用方取前 R 个，且 D×R ≈ fanout_limit。
            # 连通性保持：未入样的节点仍各连 1 条到对方的代表节点，故 BFS 可达
            # （否则孤立节点会让 expand_from_anchor 漏配 —— 那才是真语义破坏）。
            d_tot, r_tot = len(definers), len(referers)
            d_rep = max(1, min(d_tot, _isqrt(fanout_limit) or 1))
            r_rep = max(1, min(r_tot, fanout_limit // d_rep or 1))
            d_head, r_head = definers[:d_rep], referers[:r_rep]
            for (ds, dp) in d_head:
                for (rs, rp) in r_head:
                    adj[ds].append((rs, {'value': v, 'param': rp, 'role': 'referer'}))
                    adj[rs].append((ds, {'value': v, 'param': dp, 'role': 'definer'}))
                    n_edges += 1
            # 未入样的定义方 → 连到代表引用方的首个（保连通，每节点常数条边）
            r0 = r_head[0]
            for (ds, dp) in definers[d_rep:]:
                adj[ds].append((r0[0], {'value': v, 'param': r0[1], 'role': 'referer'}))
                adj[r0[0]].append((ds, {'value': v, 'param': dp, 'role': 'definer'}))
                n_edges += 1
            # 未入样的引用方 → 连到代表定义方的首个
            d0 = d_head[0]
            for (rs, rp) in referers[r_rep:]:
                adj[rs].append((d0[0], {'value': v, 'param': d0[1], 'role': 'definer'}))
                adj[d0[0]].append((rs, {'value': v, 'param': rp, 'role': 'referer'}))
                n_edges += 1
        else:
            for (ds, dp) in definers:
                for (rs, rp) in referers:
                    adj[ds].append((rs, {'value': v, 'param': rp, 'role': 'referer'}))
                    adj[rs].append((ds, {'value': v, 'param': dp, 'role': 'definer'}))
                    n_edges += 1

    stats = {
        'n_nodes': len(nodes),
        'n_edges': n_edges,
        'n_values': len(values),
        'n_cross_ne': n_cross_ne,
        'n_orphan_def': n_orphan_def,
        'n_ref_rel': n_ref_rel,
        'n_capped_values': n_capped,
    }
    return {'nodes': nodes, 'adj': dict(adj), 'values': values, 'stats': stats}


def neighbors(graph, seq, role=None):
    """查询实例 seq 的邻居。role：'definer' / 'referer' / None（全部）。"""
    return [(n, e) for (n, e) in graph['adj'].get(seq, [])
            if role is None or e['role'] == role]


def expand_from_anchor(graph, seeds, direction=None, max_nodes=None):
    """从锚点实例集合 BFS 扩展找全。

    direction: None=双向（连通分量）/ 'fwd'=正向（沿引用方，定义方→引用方）/
               'bwd'=反向（沿定义方，引用方→定义方）。
    max_nodes: 可选上限（防走通过大分量）。
    返回 visited 集合（seq）。
    """
    visited = set()
    queue = list(seeds)
    while queue:
        seq = queue.pop()
        if seq in visited:
            continue
        visited.add(seq)
        if max_nodes and len(visited) >= max_nodes:
            break
        for (n, e) in graph['adj'].get(seq, []):
            if direction == 'fwd' and e['role'] != 'referer':
                continue
            if direction == 'bwd' and e['role'] != 'definer':
                continue
            if n not in visited:
                queue.append(n)
    return visited


def dump_graph(graph, path):
    """全量图落盘 JSON（nodes + adj + values + stats）。通用格式，供切片3/前端复用。"""
    import json
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(graph, f, ensure_ascii=False, separators=(',', ':'))
    return path


def load_graph(path):
    """加载落盘的图（恢复 int 节点 key；边为 list [neighbor, edge]，查询接口兼容）。"""
    import json
    with open(path, encoding='utf-8') as f:
        g = json.load(f)
    g['nodes'] = {int(k): v for k, v in g['nodes'].items()}
    g['adj'] = {int(k): v for k, v in g['adj'].items()}
    return g


if __name__ == '__main__':
    import json
    import sys
    import time
    from p1_parse import parse_exp
    exp = sys.argv[1]
    parsed = parse_exp(exp)
    t0 = time.time()
    g = build_graph(parsed['commands'])
    dt = time.time() - t0
    print(json.dumps({'stats': g['stats'], 'build_sec': round(dt, 2)},
                     ensure_ascii=False, indent=1))

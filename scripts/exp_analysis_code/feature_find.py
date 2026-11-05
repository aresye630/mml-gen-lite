#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""feature_find.py — 切片 2（A 找全）：黄金规则锚点 → 找全命令实例。

黄金规则降级为「种子 + 验收锚点」：
  - 种子：黄金规则命令集（19 命令类型 + 56 条锚点 seq）界定「特性涉及哪些命令」。
  - 验收锚点：找全结果必须 ⊇ 这 56 条（golden_check 逐条核对）。

找全主路径 = 命令类型全量枚举（trivial 枚举，用户定调，见 Key Decision）：
  黄金规则命令集 = 特性模式覆盖的命令类型，全量枚举 = 找全该特性在现网的全部实例。
  不依赖走链 —— 走链是 B（图谱解析）的职责，用于「跨网元完整链」闭环与配置生成。

辅助（可选，mode='graph'）：从锚点名字参数值出发，在「定义方↔引用方」图上双向扩展，
  验证图谱对「同网元引用链」的助力；跨网元对象名（定义方在别处）由图谱接住，
  不在本模块枚举 —— 这是「找全」与「图谱」的边界。

数据驱动红线：零局点实例值。黄金规则从 golden_rules.yaml 读（期望输出，允许局点值）；
  名字参数从 EXP 归纳（infer_param_definer）；命令全量枚举无任何硬编码值。

输出：
  found:        {cmd: [seq, ...]}  找全清单（命令类型 → 全量 seq，升序）
  golden_check: {cmd: {expected, got, hit, missing, extra}}  验收（⊇ golden）
  stats:        {cmd_types, instances, golden_anchors, golden_hit, golden_missing}
"""

from collections import defaultdict, OrderedDict
from pathlib import Path

import yaml

from p1_parse import parse_exp
from graph_walk import CMD_RE
from graph_build import build_graph, expand_from_anchor

RULES_DIR = Path(__file__).resolve().parent / 'rules'
GOLDEN_YAML = RULES_DIR / 'golden_rules.yaml'


def load_golden(me_type='UDG', path=None):
    """读 golden_rules.yaml → {cmd: [seq, ...]}（命令类型 → 锚点 seq 升序）。"""
    p = Path(path) if path else GOLDEN_YAML
    data = yaml.safe_load(p.read_text(encoding='utf-8')) or {}
    golden = data.get(me_type, {}) or {}
    out = {}
    for cmd, seqs in golden.items():
        out[cmd] = sorted(int(s) for s in (seqs or []))
    return out


def find_by_cmd(commands, golden):
    """命令类型全量枚举（主路径）：黄金命令集在 EXP 中的全部实例。

    返回 {cmd: [seq, ...]}（seq 升序）；不含黄金命令集之外的命令。
    """
    cmd_seq = defaultdict(list)
    for seq, line in commands.items():
        mm = CMD_RE.match(line)
        cmd = mm.group(1) if mm else line.split(':', 1)[0].strip()
        if cmd in golden:
            cmd_seq[cmd].append(seq)
    out = OrderedDict()
    # 保持 golden 里的命令顺序，再补 EXP 里出现但 golden 未列的命令（应为空）
    for cmd in golden:
        out[cmd] = sorted(cmd_seq.get(cmd, []))
    return out


def find_by_graph(commands, golden, graph=None):
    """从黄金锚点名字参数值出发，图上双向扩展（辅助，验证图谱助力）。

    只沿对象名值（is_object_name）与「定义方↔引用方」边扩展；
    跨网元（仅定义方、引用方在别处）节点扩展不出，属图谱职责。
    返回 {cmd: [seq, ...]}。
    """
    g = graph if graph is not None else build_graph(commands)
    anchors = [s for seqs in golden.values() for s in seqs]
    visited = expand_from_anchor(g, anchors, direction=None)
    cmd_seq = defaultdict(list)
    for seq in visited:
        cmd = g['nodes'].get(seq)
        if cmd is not None:
            cmd_seq[cmd].append(seq)
    out = OrderedDict()
    for cmd in golden:
        out[cmd] = sorted(cmd_seq.get(cmd, []))
    return out


def golden_check(found, golden):
    """验收：找全结果是否 ⊇ 黄金锚点（逐条 expected/got/hit/missing/extra）。"""
    per_cmd = {}
    for cmd, anchors in golden.items():
        got = set(found.get(cmd, []))
        anchors_s = set(anchors)
        missing = sorted(anchors_s - got)
        extra = sorted(got - anchors_s)
        per_cmd[cmd] = {
            'expected': len(anchors_s),
            'got': len(got),
            'hit': len(anchors_s) - len(missing),
            'missing': missing,
            'extra': extra,
            'anchors': sorted(anchors_s),
        }
    return per_cmd


def run(exp_path, me_type='UDG', mode='graph', golden_path=None):
    """找全完整输出（供 pipeline 挂载与独立调试）。

    mode: 'graph'（默认，图上双向扩展 = 找全关联实例）/ 'cmd'（命令类型全量枚举，参考对比）。
    """
    parsed = parse_exp(exp_path)
    commands = parsed['commands']
    golden = load_golden(me_type, golden_path)
    if mode == 'graph':
        found = find_by_graph(commands, golden)
    else:
        found = find_by_cmd(commands, golden)
    gc = golden_check(found, golden)
    n_anchors = sum(len(v) for v in golden.values())
    n_missing = sum(len(v['missing']) for v in gc.values())
    n_instances = sum(len(v) for v in found.values())
    return {
        'mode': mode,
        'found': found,
        'golden_check': gc,
        'stats': {
            'cmd_types': len(golden),
            'instances': n_instances,
            'golden_anchors': n_anchors,
            'golden_hit': n_anchors - n_missing,
            'golden_missing': n_missing,
        },
    }


def _pack(found, golden):
    """找全结果 → 结构化 dict（found + golden_check + stats）。"""
    gc = golden_check(found, golden)
    n_anchors = sum(len(v) for v in golden.values())
    n_missing = sum(len(v['missing']) for v in gc.values())
    n_instances = sum(len(v) for v in found.values())
    return {
        'found': found,
        'golden_check': gc,
        'stats': {
            'cmd_types': len(golden),
            'instances': n_instances,
            'golden_anchors': n_anchors,
            'golden_hit': n_anchors - n_missing,
            'golden_missing': n_missing,
        },
    }


def run_all(commands, me_type='UDG', golden_path=None, graph=None):
    """一次建图返回找全结果（供 pipeline 复用已解析 commands）。

    找全口径 = 图上扩展（从锚点沿引用关系找全关联实例）；cmd 全量枚举仅作参考对比。
    返回 {graph: {...找全主结果}, cmd: {...参考对比}}。
    graph 可传入已建好的全量图（复用，避免重复 build）。
    """
    golden = load_golden(me_type, golden_path)
    found_cmd = find_by_cmd(commands, golden)
    if graph is None:
        graph = build_graph(commands)
    found_graph = find_by_graph(commands, golden, graph)
    return {
        'graph': _pack(found_graph, golden),   # 找全（主）：图上扩展
        'cmd': _pack(found_cmd, golden),       # 参考对比：命令全量枚举
    }


if __name__ == '__main__':
    import argparse
    import json
    ap = argparse.ArgumentParser(description='切片2 找全实例（黄金规则命令集）')
    ap.add_argument('exp')
    ap.add_argument('--me-type', default='UDG')
    ap.add_argument('--mode', default='graph', choices=['cmd', 'graph'])
    ap.add_argument('--stats-only', action='store_true',
                    help='只输出量化统计，不输出全量清单')
    args = ap.parse_args()
    res = run(args.exp, args.me_type, args.mode)
    if args.stats_only:
        res.pop('found', None)
        res.pop('golden_check', None)
    print(json.dumps(res, ensure_ascii=False, indent=1))

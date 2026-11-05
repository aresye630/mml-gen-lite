#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""feature_chain_map.py — feature ↔ 链 归属映射（数据驱动，零硬编码）。

输入：chain_schemas.yaml（12 链命令集，产品级）+ features_udg.yaml（435 feature）
输出：feature_chains.json —— 每个 feature 归属的功能链集合（按命中命令数降序）。

匹配口径：
  - feature 命令集 = core L1/L2/L3 并集（feature 核心功能命令）；core 为空时用 key_cmds 兜底
    （授权开关类 feature 的 core 常为空，但其 key_cmds 仍能表达功能面）。
  - 链命令集 = anchor_cmds + 所有 layers 的 cmds（spec 对象取 type 命令名）。
  - 归属 = 命令集交集非空；无交集 → unmapped（该 feature 功能域未被 12 链建模）。

注意：命令名为产品级通用知识（ADD URR / ADD RULE 等），本脚本不含任何局点实例值。
"""
import argparse
import json
import sys
from pathlib import Path

try:
    import yaml
except ImportError:  # 容器内可能无 PyYAML（python3.14 精简环境）
    yaml = None


def _cmd_name(c):
    """cmds 条目 → 命令名（字符串或 spec{type} 对象）。"""
    if isinstance(c, str):
        return c
    if isinstance(c, dict):
        return c.get('type')
    return None


def chain_cmdset(chain):
    """一条链的完整命令集：anchor_cmds + 所有 layers 的 cmds。"""
    s = set()
    for c in (chain.get('anchor_cmds') or []):
        n = _cmd_name(c)
        if n:
            s.add(n)
    for lyr in (chain.get('layers') or []):
        for c in (lyr.get('cmds') or []):
            n = _cmd_name(c)
            if n:
                s.add(n)
    return s


def chain_cmdlist(chain):
    """一条链的完整命令序列（有序，去重保留首次）：anchor_cmds + 各 layer cmds。

    用于三态环节视图——链的环节顺序即渲染顺序（anchor 打头，逐层展开）。
    """
    seen = []
    for c in (chain.get('anchor_cmds') or []):
        n = _cmd_name(c)
        if n and n not in seen:
            seen.append(n)
    for lyr in (chain.get('layers') or []):
        for c in (lyr.get('cmds') or []):
            n = _cmd_name(c)
            if n and n not in seen:
                seen.append(n)
    return seen


def feat_cmdset(f):
    """feature 命令集：core L1/L2/L3 并集，空则 key_cmds 兜底。"""
    s = set()
    core = f.get('core') or {}
    for lvl in ('L1', 'L2', 'L3'):
        for c in (core.get(lvl) or []):
            s.add(c)
    if not s:
        s = set(f.get('key_cmds') or [])
    return s


def build_map(chains, feats):
    """返回 {fid: {chains, hits, unmapped, cmdset, chain_views}}。

    chain_views[cid] = {name, steps: [{cmd, state(high/gray)}], missing: [cmd]}。
    三态口径：high = feature 命令集 ∩ 链命令集；gray = 链命令集 − feature 命令集；
    missing = feature 命令集 − 链命令集（feature 要求但链未建模的命令）。
    """
    cmap = [(ch.get('chain_id'), ch.get('name', ''), chain_cmdset(ch), chain_cmdlist(ch))
            for ch in chains]
    out = {}
    for fid, f in feats.items():
        fset = feat_cmdset(f)
        hits = {}
        chain_views = {}
        for cid, name, cset, clist in cmap:
            inter = fset & cset
            if not inter:
                continue
            hits[cid] = sorted(inter)
            steps = [{'cmd': c, 'state': ('high' if c in fset else 'gray')} for c in clist]
            missing = sorted(fset - cset)
            chain_views[cid] = {'name': name, 'steps': steps, 'missing': missing}
        # 命中命令数降序 → 主链在前
        ordered = sorted(hits.keys(), key=lambda c: -len(hits[c]))
        out[fid] = {'chains': ordered, 'hits': hits,
                    'unmapped': len(ordered) == 0,
                    'cmdset': sorted(fset),
                    'chain_views': {c: chain_views[c] for c in ordered}}
    return out


def load_yaml(path):
    if yaml is not None:
        with open(path, encoding='utf-8') as f:
            return yaml.safe_load(f)
    # 无 PyYAML 兜底：仅支持本仓库规则文件的简单结构（逐行 key: value 解析太脆，直接报错）
    raise RuntimeError(f'PyYAML 不可用，无法解析 {path}（请 pip install pyyaml）')


def main():
    ap = argparse.ArgumentParser(description='feature↔链 归属映射（数据驱动）')
    ap.add_argument('--chains', required=True, help='chain_schemas.yaml 路径')
    ap.add_argument('--features', required=True, help='features_udg.yaml 路径')
    ap.add_argument('-o', '--out', required=True, help='feature_chains.json 输出路径')
    ap.add_argument('--product', default='UDG', help='产品分组键（chain_schemas.yaml 顶层）')
    args = ap.parse_args()

    chain_doc = load_yaml(args.chains)
    chains = chain_doc[args.product]
    feat_doc = load_yaml(args.features)
    feats = feat_doc['features']

    mapping = build_map(chains, feats)
    unmapped = sum(1 for v in mapping.values() if v['unmapped'])
    mapped = len(mapping) - unmapped

    result = {
        'product': args.product,
        'chains': [{'chain': ch.get('chain_id'), 'name': ch.get('name', '')} for ch in chains],
        'feature_chains': mapping,
        'stats': {'total': len(mapping), 'mapped': mapped, 'unmapped': unmapped},
    }
    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    Path(args.out).write_text(json.dumps(result, ensure_ascii=False, indent=1), encoding='utf-8')
    print(json.dumps(result['stats'], ensure_ascii=False))
    return 0


if __name__ == '__main__':
    sys.exit(main())

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""gen_feature_v5.py — 从 111 知识库生成 feature_v5 单一知识产物。

设计要点（D1 定案）：
  · 特性级一条（一个 name = 一个 feature），场景用 scenes/nav 组织
  · 命令集 = 111 jinja2 模板命令 ∪ 111 正文命令 ∪ feature_v3 补充的查询命令
  · 参数 schema 与命令模板原样保留（生成链路依赖）
  · 全数据驱动：无产品硬编码（产品从 ne_type / 目录名探测）

输出：rules/feature_v5_{ueg,udg,unc}.yaml

用法：
  python3 gen_feature_v5.py --src <111根> --feat-v3 <feature_v3根> --out-dir <rules目录> --product UEG
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
from collections import defaultdict
from datetime import datetime, timezone

import yaml

# ── 常量 ──────────────────────────────────────────────────────────
NAV_MAX = 1024
DESC_MAX = 4096
# MML 动词白名单（抽取命令时过滤噪音）
VERBS = {
    'ADD', 'MOD', 'SET', 'DEL', 'RMV', 'DSP', 'LST', 'SHOW', 'CHK', 'EXP',
    'OPR', 'LOD', 'LCK', 'UNL', 'RST', 'ACT', 'DEA', 'LGI', 'CLR', 'SAV',
    'BKP', 'RTR', 'UPL', 'DWL', 'SWP', 'STR', 'STP', 'BLK', 'UBL',
}
_CMD_RE = re.compile(r"\b(" + "|".join(sorted(VERBS)) + r")\s+([A-Z][A-Z0-9_]{1,30})\b")
_BLOCK_RE = re.compile(r"@mml:block=\s*(\w+)\s*-->")
_FM_RE = re.compile(r"^---\n(.*?)\n---\n", re.S)
# jinja2 模板中的命令行（4 空格缩进的 `CMD:`）
_TPL_CMD_RE = re.compile(r"^\s{4}([A-Z][A-Z0-9_ ]{2,40}):\s*$", re.M)


def norm_cmd(s: str) -> str | None:
    """归一化命令名；首词不在白名单则丢弃。"""
    s = ' '.join(s.strip().upper().split())
    if not s:
        return None
    head = s.split()[0]
    return s if head in VERBS else None


def parse_doc(path: str) -> dict | None:
    """解析单个 111 文档 → 结构化记录。"""
    try:
        text = open(path, encoding='utf-8', errors='replace').read()
    except Exception:
        return None

    m = _FM_RE.match(text)
    if not m:
        return None
    try:
        fm = yaml.safe_load(m.group(1)) or {}
    except Exception:
        return None

    name = str(fm.get('name', '') or '').strip()
    if not name:
        return None

    # ── 三个块（兼容 `= params` 与 `=params` 两种写法）──
    blocks = {}
    marks = list(_BLOCK_RE.finditer(text))
    for i, mk in enumerate(marks):
        blk = mk.group(1)
        end = marks[i + 1].start() if i + 1 < len(marks) else len(text)
        blocks[blk] = text[mk.end():end]

    # params：yaml → dict
    params = {}
    pm = re.search(r"```yaml\n(.*?)```", blocks.get('params', ''), re.S)
    if pm:
        try:
            sch = yaml.safe_load(pm.group(1)) or {}
            params = (sch.get('schemas') or {}).get('properties') or {}
        except Exception:
            params = {}

    # commands：jinja2 模板原文（保留，生成链路直接渲染）
    cmd_block = blocks.get('commands', '')
    templates = []
    for tm in re.finditer(r"```jinja2\n(.*?)```", cmd_block, re.S):
        templates.append(tm.group(1).strip())

    # ── 命令集 ──
    config_cmds: set[str] = set()
    for c in _TPL_CMD_RE.findall(cmd_block):
        n = norm_cmd(c)
        if n:
            config_cmds.add(n)
    # 正文（annotations 块 + 全文）里的命令
    body_cmds: set[str] = set()
    for m2 in _CMD_RE.finditer(text):
        body_cmds.add(f"{m2.group(1)} {m2.group(2)}")
    # allowed-tools 里的命令
    for at in (fm.get('allowed-tools') or []):
        m3 = re.search(r"getParameterValue\('([^']+)'\)", str(at))
        if m3:
            n = norm_cmd(m3.group(1))
            if n:
                body_cmds.add(n)

    doc_source = fm.get('doc_source') or []
    if isinstance(doc_source, str):
        doc_source = [doc_source]

    return {
        'name': name,
        'id': str(fm.get('id', '') or '').strip(),
        'ne_type': str(fm.get('ne_type', '') or '').strip(),
        'type': str(fm.get('type', '') or '').strip(),
        'description': str(fm.get('description', '') or '').strip()[:DESC_MAX],
        'risk_level': str(fm.get('risk_level', '') or '').strip(),
        'doc_source': [str(x) for x in doc_source][:64],
        'nav': ' > '.join(str(x) for x in doc_source)[:NAV_MAX],
        'file_path': path,
        'config_cmds': sorted(config_cmds),
        'body_cmds': sorted(body_cmds),
        'params': params,
        'templates': templates,
        'dep_on_live': bool((fm.get('metadata') or {}).get('DepOnLiveCfg', False)),
    }


def cmds_from_v3(path: str) -> set[str]:
    """从 feature_v3 文档抽命令（补充 111 缺失的查询/验证命令）。"""
    try:
        t = open(path, encoding='utf-8', errors='replace').read()
    except Exception:
        return set()
    return {f"{m.group(1)} {m.group(2)}" for m in _CMD_RE.finditer(t)}


def build_v3_index(feat_dir: str) -> dict:
    """feature_v3：title → 文档路径列表（用于补全查询命令）。"""
    idx = defaultdict(list)
    if not feat_dir or not os.path.isdir(feat_dir):
        return idx
    for root, _, files in os.walk(feat_dir):
        for fn in files:
            if not fn.endswith('.md'):
                continue
            p = os.path.join(root, fn)
            try:
                head = open(p, encoding='utf-8', errors='replace').read(4000)
            except Exception:
                continue
            # feature_v3 标题：第一行 `# xxx` 或 frontmatter name
            t = None
            mm = re.match(r"^---\n(.*?)\n---\n", head, re.S)
            if mm:
                try:
                    fmv = yaml.safe_load(mm.group(1)) or {}
                    t = str(fmv.get('name', '') or '').strip()
                except Exception:
                    t = None
            if not t:
                h = re.search(r"^#\s+(.+)$", head, re.M)
                t = h.group(1).strip() if h else ''
            if t:
                idx[t].append(p)
    return idx


def build_product(src_root: str, product: str, v3_idx: dict) -> dict:
    """构建单产品的 feature_v5 结构。"""
    pdir = os.path.join(src_root, product)
    if not os.path.isdir(pdir):
        return {}

    docs = []
    for root, _, files in os.walk(pdir):
        for fn in files:
            if fn.endswith('.md'):
                r = parse_doc(os.path.join(root, fn))
                if r:
                    docs.append(r)

    # ── 特性级聚合（D1：一个 name = 一条 feature）──
    by_name = defaultdict(list)
    for d in docs:
        by_name[d['name']].append(d)

    features = {}
    seq = 0
    for name in sorted(by_name):
        group = by_name[name]
        seq += 1

        # id：优先 GWFD 号
        fid = next((g['id'] for g in group if g['id']), '')
        key = fid if fid else f"F{seq:04d}"

        # 场景：按 file_path 排序（稳定）
        # 注：params/templates 不在此重复存储（特性级已存最全版本），
        #     场景仅保留定位信息 + 覆盖度标记，避免 3x 冗余。
        group.sort(key=lambda g: g['file_path'])
        scenes = []
        for g in group:
            rel = os.path.relpath(g['file_path'], src_root)
            scenes.append({
                'nav': g['nav'],
                'doc': rel,
                'n_params': len(g['params']),
                'n_templates': len(g['templates']),
            })

        # 特性级 params/templates：取"最全"的场景（params 组数最多）
        best = max(group, key=lambda g: (len(g['params']), len(g['templates'])))
        params = best['params']
        templates = best['templates']

        # 命令集：111 全部场景并集
        cfg, body = set(), set()
        for g in group:
            cfg |= set(g['config_cmds'])
            body |= set(g['body_cmds'])

        # 查询命令补充（feature_v3）
        v3_cmds = set()
        for p in v3_idx.get(name, []):
            v3_cmds |= cmds_from_v3(p)
        query_cmds = {c for c in (cfg | body | v3_cmds)
                      if c.split()[0] in ('LST', 'DSP', 'SHW', 'EXP', 'CHK')}
        all_cmds = cfg | body | v3_cmds

        g0 = group[0]
        features[key] = {
            'title': name,
            'product': product,
            'ne_type': g0['ne_type'] or product,
            'fid': fid,
            'description': g0['description'],
            'risk_level': g0['risk_level'],
            'nav': g0['nav'],
            'doc_source': g0['doc_source'],
            'dep_on_live': any(g['dep_on_live'] for g in group),
            'scenes': scenes,
            'cmds': {
                'config': sorted(cfg),
                'query': sorted(query_cmds),
                'all': sorted(all_cmds),
                'v3_supplement': sorted(v3_cmds - cfg - body),
            },
            'params': params,
            'templates': templates,
            # ── 分析链路兼容字段（feature_chain_map.feat_cmdset 直读）──
            # 口径：core.L1/L2/L3 并集优先，空则 key_cmds 兜底。
            # 此处 core 留空、key_cmds = 全命令集，语义等价于旧指纹库的兜底分支。
            'core': {'L1': [], 'L2': [], 'L3': []},
            'key_cmds': sorted(all_cmds),
            'all_cmd_types': sorted(all_cmds),
            'query': sorted(query_cmds),
        }

    return {
        'meta': {
            'product': product,
            'schema': 'feature_v5',
            'generated_at': datetime.now(timezone.utc).isoformat(timespec='seconds'),
            'source_111': os.path.relpath(pdir, src_root),
            'stats': {
                'docs_111': len(docs),
                'features': len(features),
                'with_params': sum(1 for f in features.values() if f['params']),
                'with_templates': sum(1 for f in features.values() if f['templates']),
                'multi_scene': sum(1 for f in features.values() if len(f['scenes']) > 1),
            },
        },
        'features': features,
    }


def main():
    ap = argparse.ArgumentParser(description='从 111 生成 feature_v5 知识产物')
    ap.add_argument('--src', required=True, help='111 知识库根（含 UEG/UDG/UNC）')
    ap.add_argument('--feat-v3', default='', help='feature_v3 根（补全查询命令，可省）')
    ap.add_argument('--out-dir', required=True, help='输出目录（rules/）')
    ap.add_argument('--product', action='append', default=None,
                    help='产品（可多次）；默认扫描 src 下所有含 md 的目录')
    args = ap.parse_args()

    src = os.path.abspath(os.path.expanduser(args.src))
    out_dir = os.path.abspath(os.path.expanduser(args.out_dir))
    os.makedirs(out_dir, exist_ok=True)

    products = args.product or sorted(
        d for d in os.listdir(src) if os.path.isdir(os.path.join(src, d)))

    print(f'源: {src}')
    print(f'产品: {products}')

    v3_root = os.path.expanduser(args.feat_v3) if args.feat_v3 else ''
    v3_idx = build_v3_index(v3_root) if v3_root else {}
    if v3_idx:
        print(f'feature_v3 补全索引: {len(v3_idx)} 个标题')

    total = 0
    for prod in products:
        data = build_product(src, prod, v3_idx)
        if not data:
            print(f'  [{prod}] 跳过（无数据）')
            continue
        out = os.path.join(out_dir, f'feature_v5_{prod.lower()}.yaml')
        with open(out, 'w', encoding='utf-8') as f:
            yaml.safe_dump(data, f, allow_unicode=True, sort_keys=False, width=4096)
        st = data['meta']['stats']
        size = os.path.getsize(out) / 1024
        print(f"  [{prod}] {st['features']} 特性 / {st['docs_111']} 文档 / "
              f"params {st['with_params']} / 模板 {st['with_templates']} / "
              f"多场景 {st['multi_scene']} → {os.path.basename(out)} ({size:.0f} KB)")
        total += st['features']
    print(f'合计 {total} 个特性')


if __name__ == '__main__':
    main()

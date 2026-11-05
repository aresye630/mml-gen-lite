#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""新特性文档接入流水线：预检(去重/解析) → 指纹增量 → 值模式规则 → 回归验证。

用法（venv-web/bin/python 跑，避免系统 python 的 f-string 兼容问题）：
  python scripts/ingest_feature_docs.py --dir <新文档目录> --product UEG [--case <case目录>]

数据驱动：不硬编码任何文档/命令/参数/局点；所有知识来自规则文件与文档本身。
新增特性文档 = 放目录 → 跑本脚本 → 指纹/值模式/回归自动完成，代码零改动。

步骤：
  1. 预检   ：parse 成功？doc_path 已收录？md5 与现有文档重复（挂 alias 不建指纹）？
  2. 指纹   ：govern 增量语义（doc_path 主键对齐，新文档追加 F 编号不漂移 + 域级收回重算）
  3. 值模式 ：新文档接口类（锚点 NAME 有样例）→ 自动追加 name_pattern.yaml 规则
  4. 回归   ：--case 给出时重跑 match_features，输出状态分布对比
"""
import argparse
import hashlib
import os
import subprocess
import sys
import time
from collections import Counter, defaultdict
from pathlib import Path

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import gen_feature_all as gfa  # noqa: E402
import govern_features as gov  # noqa: E402
import yaml  # noqa: E402

RULES = os.path.join(HERE, '..', 'rules')


def load_products():
    data = yaml.safe_load(open(os.path.join(RULES, 'products.yaml'), encoding='utf-8')) or {}
    return data.get('products', {})


def md5_of(path):
    return hashlib.md5(open(path, 'rb').read()).hexdigest()


def main():
    ap = argparse.ArgumentParser(description='新特性文档接入流水线')
    ap.add_argument('--dir', required=True, help='新文档所在目录（递归扫描 *.md）')
    ap.add_argument('--product', required=True, help='产品名（products.yaml 注册）')
    ap.add_argument('--case', default='', help='回归：case 目录（重跑 match_features）')
    ap.add_argument('--fingerprint', default='', help='指纹库路径（缺省按产品）')
    ap.add_argument('--patterns', default='', help='name_pattern.yaml 路径（缺省按产品目录）')
    args = ap.parse_args()

    pr = load_products().get(args.product)
    if not pr:
        ap.error(f'产品未注册：{args.product}（见 rules/products.yaml）')
    feat_dir = os.path.expanduser(pr.get('feat_dir', ''))
    fp_path = args.fingerprint or pr.get('fingerprint', 'rules/features.yaml')
    if not os.path.isabs(fp_path):
        fp_path = os.path.join(RULES, os.path.basename(fp_path))
    pat_path = args.patterns or os.path.join(RULES, 'name_pattern.yaml')
    if not os.path.exists(feat_dir):
        ap.error(f'特性文档库不存在：{feat_dir}')

    # ── 1. 载入现有索引（判断集合 = 指纹库已收录，不是目录扫描——新文档进目录后
    #         目录扫描会把它算进"已有"，导致永远发现不了新文档）──
    data = yaml.safe_load(open(fp_path, encoding='utf-8')) or {}
    feats = data['features']
    known_paths = {f.get('doc_path') for f in feats.values() if f.get('doc_path')}
    md5_index = {}
    for dp in known_paths:
        p = os.path.join(feat_dir, dp)
        if os.path.exists(p):
            md5_index.setdefault(md5_of(p), []).append(dp)
    docs_all = gfa.load_feature_docs(feat_dir)   # ref_count 用（含新文档，与 --scan 一致）

    # ── 2. 扫描新文档 ──
    new_files, dup_files, known_files, fail_files = [], [], [], []
    for root, dirs, files in os.walk(args.dir):
        dirs.sort()
        for fn in sorted(files):
            if not fn.endswith('.md'):
                continue
            p = os.path.join(root, fn)
            doc = gfa.parse_feature_md(open(p, encoding='utf-8').read(),
                                       os.path.relpath(p, feat_dir))
            if doc is None:
                fail_files.append(p)
                continue
            if doc['doc_path'] in known_paths:
                known_files.append(p)
                continue
            h = md5_of(p)
            if h in md5_index:
                dup_files.append((p, md5_index[h][0]))
                continue
            new_files.append((p, doc, h))
    print(f'预检：新文档 {len(new_files)} 篇 / 内容重复 {len(dup_files)} 篇 / '
          f'已收录 {len(known_files)} 篇 / 解析失败 {len(fail_files)} 篇')

    # ── 3. 指纹增量（govern --scan 语义）──
    anchors = gfa.load_param_anchors(os.path.join(RULES, 'param_anchor.yaml'))
    kw_table = gov.load_domain_kws(gov.DEFAULT_DOMAIN_KWS)
    ref_count = Counter(c for doc in docs_all for c in doc['all_cmd_types'])
    data = yaml.safe_load(open(fp_path, encoding='utf-8')) or {}
    feats = data['features']
    path2fid = {f.get('doc_path'): fid for fid, f in feats.items()}
    next_no = max((int(fid[1:]) for fid in feats if fid[1:].isdigit()), default=0) + 1
    added = []
    for p, doc, h in new_files:
        fid = f'F{next_no:03d}'
        next_no += 1
        f = gov.build_fingerprint(doc, ref_count, anchors, kw_table, 40, 2)  # public_n/core_n 与 --init 默认一致
        f['confidence'] = gov.confidence(f)
        f['ingested'] = {'at': time.strftime('%Y-%m-%d'), 'md5': h, 'file': os.path.basename(p)}
        feats[fid] = f
        added.append((fid, doc, f))
    # 内容重复的挂 alias 到 canonical（不建指纹）
    aliased = 0
    for p, canon in dup_files:
        for f in feats.values():
            if f.get('doc_path') == canon:
                f.setdefault('dedup', {}).setdefault('alias_docs', [])
                rel = os.path.relpath(p, feat_dir)
                if rel not in f['dedup']['alias_docs']:
                    f['dedup']['alias_docs'].append(rel)
                    aliased += 1
                break
    if added:
        reclaimed, moved = gov.domain_reclaim(feats, ref_count, 0.30, 0.30, 100, 5)
        print(f'域级收回（新增后全量重算）：{sum(len(v) for v in reclaimed.values())} 条命令，'
              f'{moved} 处 prereq→core.L3')
        # 新指纹与同域已有指纹分类对齐：core_domain 语义 = 业务域共享命令。
        # 域级收回的 in_rate 阈值在增量场景会失效（已收回命令移出 prereq 后
        # 域内占比被低估，新指纹永远收不回来），这里直接继承同域已有 core。
        dom_core = defaultdict(set)
        for f in feats.values():
            if f.get('domain'):
                dom_core[f['domain']].update(f.get('core', {}).get('L3', []))
        aligned = 0
        for fid, doc, f in added:
            dom = f.get('domain')
            if not dom:
                continue
            for cmd in dom_core.get(dom, []):
                if cmd in f.get('prereq', []) and cmd not in f['core']['L3']:
                    f['prereq'].remove(cmd)
                    f['core']['L3'].append(cmd)
                    aligned += 1
        if aligned:
            print(f'域对齐：{aligned} 处新指纹 prereq→core.L3（继承同域共享命令）')
    data['meta']['stats']['total'] = len(feats)
    data['meta']['stats']['governed'] = sum(
        1 for f in feats.values() if f.get('status') == 'governed')
    data['meta']['stats']['pending'] = sum(
        1 for f in feats.values() if f.get('status') == 'pending')
    data['meta']['stats']['approved'] = sum(
        1 for f in feats.values() if f.get('status') == 'approved')
    os.makedirs(os.path.dirname(fp_path), exist_ok=True)
    yaml.safe_dump(data, open(fp_path, 'w', encoding='utf-8'),
                   allow_unicode=True, sort_keys=False)
    print(f'✅ 指纹库 → {fp_path}（{len(feats)} 条，新增 {len(added)}，alias {aliased}）')

    # ── 4. 值模式规则（接口类新文档自动追加）──
    pat_data = yaml.safe_load(open(pat_path, encoding='utf-8')) or {}
    pats = pat_data.get('interface_name_patterns', [])
    have_fid = {p.get('fid') for p in pats}
    new_pats = []
    for fid, doc, f in added:
        if '接口数据' not in f.get('title', ''):
            continue
        names = doc.get('anchor_vals', {}).get(('ADD LOGICINF', 'NAME'))
        if not names:
            continue
        prefixes = sorted({gfa_param_prefix(v) for v in names if v})
        if not prefixes:
            continue
        new_pats.append({'fid': fid, 'title': f.get('title', ''),
                         'cmd': 'ADD LOGICINF', 'param': 'NAME',
                         'prefixes': prefixes, 'doc': doc['doc_path'].split('/')[-1],
                         'source': 'ingest'})
    if new_pats:
        pats.extend(new_pats)
        pat_data['interface_name_patterns'] = pats
        yaml.safe_dump(pat_data, open(pat_path, 'w', encoding='utf-8'),
                       allow_unicode=True, sort_keys=False)
        print(f'✅ 值模式规则 → {pat_path}（新增 {len(new_pats)} 条）')

    # ── 5. 回归验证 ──
    if args.case:
        exp = None
        for f in sorted(os.listdir(args.case)):
            if f.lower().startswith('exp') and f.lower().endswith('.txt'):
                exp = os.path.join(args.case, f)
                break
        if exp:
            r = subprocess.run([sys.executable, os.path.join(HERE, 'match_features.py'),
                                '--product', args.product, '--exp', exp, '-o', args.case],
                               capture_output=True, text=True, timeout=600)
            tail = r.stdout.strip().split('\n')[-1] if r.stdout else ''
            print(f'✅ 回归：{args.case}\n    {tail}')

    # ── 6. 报告 ──
    print('\n═══ 接入报告 ═══')
    for fid, doc, f in added:
        core = f.get('core', {})
        n_core = len(core.get('L1', [])) + len(core.get('L2', [])) + len(core.get('L3', []))
        kp = list(doc.get('key_params', {}).keys())
        print(f'  {fid} {f.get("title", "")[:30]} | core {n_core} 条 | '
              f'conf {f.get("confidence")} | key_params {len(kp)} 命令 | {doc["doc_path"][:44]}')
    for p, canon in dup_files:
        print(f'  ⏭ 重复跳过（挂 alias → {os.path.basename(canon)}）：{os.path.basename(p)}')
    for p in fail_files:
        print(f'  ❌ 解析失败：{p}')
    if not added and not dup_files:
        print('  无新文档（全部已收录或重复）')


def gfa_param_prefix(v):
    """与 match_features._val_prefix 同规则：'Saif1/1/0'→'saif'。"""
    import re
    s = str(v).strip().lower()
    first = s.split('/')[0]
    first = re.sub(r'\d+$', '', first)
    return re.sub(r'[^a-z0-9]', '', first)


if __name__ == '__main__':
    main()

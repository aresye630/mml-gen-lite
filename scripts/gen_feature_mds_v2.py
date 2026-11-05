#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
gen_feature_mds_v2.py — 特性实例 MD 生成器（591 指纹库驱动）

与 gen_feature_mds.py（旧 991 清单驱动）不同，本版以去重后的
rules/features_ueg.yaml（591 条指纹）为唯一驱动，判定状态直接取
新匹配器输出（/api/case/{cid}/match 富数据），保证：

    MD 判定卡 = Web 判定卡 = 指纹库编号（F001~F591）

每篇 MD：
    §1 判定结果   —— mode / core 命中·缺失（命令@行号+exp原文）/ 授权项 / 缺关键参数 / 值模式归属
    §2 特性概述   —— 官方特性文档"操作场景"
    §3 官方示例基准 —— 指纹命令链的文档代码块原文（含场景括号）
    §4 关键参数   —— 必备事项数据表参数
    §5 exp 实际配置 —— exp 原文 @行号 + 完整行（core+prereq）

用法：
    venv-web/bin/python scripts/gen_feature_mds_v2.py \
        --match /tmp/mml_match_new.json \
        --fp rules/features_ueg.yaml \
        --feat-dir ~/workspace/zhijian/output_ueg_feature/output_ueg_feature_v2 \
        -o <case目录>/特性配置基线
"""
import argparse
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'scripts'))
from gen_feature_all import parse_feature_md  # noqa: E402

MODE_TXT = {
    'core_all_hit': '核心命令全命中',
    'core_missing': '核心命令缺失',
    'core_partial': '命令少（域内部分命中）',
    'instances_partial': '实例部分配置（材料在没拼齐）',
    'strict_dev': '命令齐但固定值/关联有偏差',
    'lic_only': '仅授权项命中',
    'license_only': '仅授权项命中',
    'lic_missing': '授权项缺失',
    'license_missing': '授权项缺失',
    'no_core_no_lic': '无核心命令可判（人工）',
    'dir_flip': '激活参数方向不符',
    'instances': '实例级判定（按锚点分组）',
    '': '—',
}
STATUS_TXT = {'configured': '✅ 已配置', 'weak': '🟡 弱匹配', 'not_configured': '❌ 未配置', 'manual': '⚠️ 需人工'}


def esc_md(s):
    return (s or '').replace('|', '\\|')


def render_judge(fid, r):
    d = r
    status = d.get('status', '')
    mode = d.get('mode', '')
    lines = ['## 1. 判定结果', '']
    lines.append(f"- 判定：**{STATUS_TXT.get(status, status)}** ｜ 模式：`{mode}`（{MODE_TXT.get(mode, '')}）")
    lines.append(f"- 实例锚点：`{d.get('instance_anchor') or '—'}` ｜ 实例数：{d.get('instance_count', 0)}")
    vp = d.get('value_pattern')
    if vp:
        ok = '✅ 值模式归属命中' if vp.get('matched') else '❌ 值模式归属不符'
        lines.append(f"- {ok}：`{vp.get('param')}` 值前缀 exp=`{vp.get('exp_prefixes')}`，"
                     f"本特性命名 `{vp.get('expect')}`"
                     + (f"（命令 `{vp.get('cmd')}`）" if vp.get('cmd') else ''))
    lines.append('')
    if d.get('core_hit') or d.get('core_miss'):
        lines.append('### 核心命令（判别依据）')
        lines.append('')
        lines.append('| 命令 | 状态 | exp 行号 | exp 原文 |')
        lines.append('|---|---|---|---|')
        for c in d.get('core_hit', []):
            ev = d.get('evidence', {}).get(c, {})
            seqs = ev.get('seqs', [])[:1]
            raw = ev.get('raw', '')
            lines.append(f"| `{esc_md(c)}` | ✅ 命中 | {seqs[0] if seqs else '—'} | `{esc_md(raw)[:80]}` |")
        for c in d.get('core_miss', []):
            lines.append(f"| `{esc_md(c)}` | ❌ 缺失 | — | — |")
        lines.append('')
    pi = d.get('param_incomplete') or {}
    if pi:
        lines.append('### 缺关键参数')
        lines.append('')
        for cmd, params in pi.items():
            lines.append(f"- `{cmd}` 缺：{', '.join(f'`{p}`' for p in params)}")
        lines.append('')
    if d.get('lic_hit') or d.get('lic_miss'):
        lines.append('### 授权项（LICITEM）')
        lines.append('')
        lines.append('| 授权项 | 状态 |')
        lines.append('|---|---|')
        for x in d.get('lic_hit', []):
            lines.append(f"| `{esc_md(x)}` | ✅ 已开通 |")
        for x in d.get('lic_miss', []):
            lines.append(f"| `{esc_md(x)}` | ❌ 未开通 |")
        lines.append('')
    return '\n'.join(lines)


def render_overview(doc):
    lines = ['## 2. 特性概述（官方特性文档）', '']
    if not doc:
        lines.append('> 指纹库 doc_path 在特性文档库中未找到对应文档。')
        lines.append('')
        return '\n'.join(lines)
    lines.append(f"> 来源：`{doc.get('doc_path', '')}`")
    lines.append('')
    summary = (doc.get('summary') or '').strip()
    if summary:
        lines.append(summary)
    else:
        lines.append('> （文档无"操作场景"节）')
    lines.append('')
    return '\n'.join(lines)


def render_baselines(r):
    bl = r.get('baselines') or {}
    lines = ['## 3. 官方示例基准（特性文档代码块原文）', '']
    if not bl:
        lines.append('> 文档无本特性相关命令示例代码块。')
        lines.append('')
        return '\n'.join(lines)
    core_all = set((r.get('core_hit') or []) + (r.get('core_miss') or []))
    for cmd, samples in bl.items():
        tag = '[核心]' if cmd in core_all else '[配套公共]'
        lines.append(f'### {cmd} {tag}')
        lines.append('')
        lines.append('```mml')
        lines.append('\n'.join(samples))
        lines.append('```')
        lines.append('')
    return '\n'.join(lines)


def render_keyparams(r):
    kp = r.get('key_params') or {}
    lines = ['## 4. 关键参数（必备事项数据表）', '']
    if not kp:
        lines.append('> 文档无关键参数声明。')
        lines.append('')
        return '\n'.join(lines)
    for cmd, params in kp.items():
        lines.append(f"- `{cmd}`：{', '.join(f'`{p}`' for p in params)}")
    lines.append('')
    return '\n'.join(lines)


def render_exp(r):
    exp_raws = r.get('exp_raws') or {}
    lines = ['## 5. exp 实际配置（命令 @行号 + 原文）', '']
    if not exp_raws:
        lines.append('> exp 中无本特性指纹命令。')
        lines.append('')
        return '\n'.join(lines)
    core_all = set((r.get('core_hit') or []) + (r.get('core_miss') or []))
    for cmd, rows in exp_raws.items():
        tag = '[核心]' if cmd in core_all else '[配套公共]'
        lines.append(f'### {cmd} {tag}')
        lines.append('')
        lines.append('```text')
        for seq, raw in rows:
            lines.append(f'    ; {seq:>5d} | {raw}')
        lines.append('```')
        lines.append('')
    return '\n'.join(lines)


def gen_md(fid, r, fp_rec, feat_dir, out_dir, fp_label=''):
    title = r.get('title') or fp_rec.get('title', '')
    domain = fp_rec.get('domain', '')
    doc_path = fp_rec.get('doc_path', '')
    doc = None
    if doc_path and feat_dir:
        p = os.path.join(feat_dir, doc_path)
        if os.path.isfile(p):
            try:
                with open(p, encoding='utf-8') as f:
                    doc = parse_feature_md(f.read(), doc_path)
            except Exception as e:
                doc = {'doc_path': doc_path, 'summary': f'（文档读取失败：{e}）'}
    lines = [f'# {title}', '']
    lines.append(f'> 特性 ID：`{fid}` ｜ 域：`{domain}` ｜ 判定：{STATUS_TXT.get(r.get("status", ""), r.get("status", ""))}')
    lines.append(f'> 指纹来源：`{fp_label or "rules/features_<product>.yaml"}` ｜ 文档：`{doc_path}`')
    lines.append('')
    lines.append(render_judge(fid, r))
    lines.append(render_overview(doc))
    lines.append(render_baselines(r))
    lines.append(render_keyparams(r))
    lines.append(render_exp(r))
    out = os.path.join(out_dir, f'{fid}.md')
    with open(out, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))
    return fid, title, r.get('status', ''), domain


def _load_products():
    import yaml
    p = os.path.join(HERE, '..', 'rules', 'products.yaml')
    with open(p, encoding='utf-8') as f:
        return yaml.safe_load(f).get('products', {})


def _expand(p):
    return os.path.expanduser(os.path.expandvars(p))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--match', required=True, help='/api/case/{cid}/match 富数据 JSON')
    ap.add_argument('--product', default='', help='产品名（UEG/UDG/UNC；缺省从 match 数据 product/meta 探测）')
    ap.add_argument('--fp', default='', help='指纹库路径（缺省按产品从 rules/products.yaml 解析）')
    ap.add_argument('--feat-dir', default='', help='特性文档库根目录（缺省按产品从 rules/products.yaml 解析）')
    ap.add_argument('-o', '--outdir', required=True)
    args = ap.parse_args()

    import yaml
    match = json.load(open(args.match, encoding='utf-8'))
    results = match.get('results', {})
    meta = match.get('meta', {})
    assert results, 'match 数据无 results（请先跑匹配器并抓取 API）'

    product = (args.product or match.get('product') or meta.get('product') or '').upper()
    prods = _load_products()
    cfg = prods.get(product, {}) if product else {}
    if args.fp or args.feat_dir:
        fp_path = _expand(args.fp or cfg.get('fingerprint', ''))
        feat_dir = _expand(args.feat_dir or cfg.get('feat_dir', ''))
    else:
        fp_path = _expand(cfg.get('fingerprint', '')) if cfg else ''
        feat_dir = _expand(cfg.get('feat_dir', '')) if cfg else ''
    if not (fp_path and feat_dir):
        ap.error('无法解析指纹库/文档库：给 --product（或 --fp/--feat-dir），且 rules/products.yaml 需含对应产品')
    fp_label = fp_path.split('rules/')[-1]
    if os.path.isfile(fp_path):
        fp = yaml.safe_load(open(fp_path, encoding='utf-8'))
        fps = fp.get('features', fp)
    else:
        fps = {}

    os.makedirs(args.outdir, exist_ok=True)
    # 清空旧产物（仅本目录 *.md，防 v2 时代残留与当前 fid 集混排）
    for fn in os.listdir(args.outdir):
        if fn.endswith('.md'):
            os.remove(os.path.join(args.outdir, fn))
    stats = {'configured': 0, 'weak': 0, 'not_configured': 0, 'manual': 0}
    idx = []
    for fid in sorted(results.keys()):
        r = results[fid]
        rec = fps.get(fid, {})
        fid, title, status, domain = gen_md(fid, r, rec, feat_dir, args.outdir, fp_label)
        stats[status] = stats.get(status, 0) + 1
        idx.append((fid, title, status, domain))
        print(f'  {fid}: {title} [{status}]')

    # README 索引
    with open(os.path.join(args.outdir, 'README.md'), 'w', encoding='utf-8') as f:
        f.write(f'# 特性配置 groundtruth（指纹库 {len(results)} 条）\n\n')
        f.write(f'- exp：`{meta.get("exp", "")}`\n')
        f.write(f'- 指纹库：`{fp_label}`（生成 {meta.get("updated_at", "")}）\n')
        f.write(f'- 匹配结果：已配置 **{stats.get("configured", 0)}** / 弱匹配 **{stats.get("weak", 0)}**'
                f' / 未配置 **{stats.get("not_configured", 0)}** / 需人工 **{stats.get("manual", 0)}**\n\n')
        f.write('## 已配置（判定 configured）\n\n')
        for fid, title, status, domain in idx:
            if status == 'configured':
                f.write(f'- [{title}]({fid}.md) `{fid}` — {domain}\n')
        f.write('\n## 弱匹配（有偏差，相似度高）\n\n')
        f.write('- ' + '\n- '.join(f'[{t}]({i}.md) `{i}`' for i, t, s, _ in idx if s == 'weak') + '\n')
        f.write('\n## 未配置（本局点未配置）\n\n')
        f.write('- ' + '\n- '.join(f'[{t}]({i}.md) `{i}`' for i, t, s, _ in idx if s == 'not_configured') + '\n')
        f.write('\n## 需人工（manual）\n\n')
        f.write('- ' + '\n- '.join(f'[{t}]({i}.md) `{i}`' for i, t, s, _ in idx if s == 'manual') + '\n')
    print(f'\n✅ 完成：{len(results)} 篇 → {args.outdir}（configured {stats["configured"]} / '
          f'weak {stats["weak"]} / not_configured {stats["not_configured"]} / manual {stats["manual"]}）')


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
gen_feature_mds.py v2 — 生成"特性配置分析"MD 文档（数据驱动）

每个特性一个 MD：
    §1 特性概述     —— 官方特性文档（feature_description）
    §2 官方配置示例 —— 官方 MML 命令文档"使用实例"（每条命令类型）
    §3 映射对照     —— exp 命令类型 ↔ 官方命令文档/特性概述页 收录状态
    §4 exp 实际配置 —— 多实例分开呈现（命令带 EXP 行号）

输入：
    <exp.txt> <groundtruth.json> --docs rules/feature_docs.yaml
    --feat-dir <UEG特性文档JSON目录> --mml-dir <UEG MML命令文档目录> -o <输出目录>

用法：
    python3 gen_feature_mds.py <exp.txt> <groundtruth.json> \
        --mml-dir ~/workspace/zhijian/output_ueg_mml/output_ueg_mml/MML/Document \
        -o ~/workspace/demoshow/runs/case1.1/特性配置基线/
"""

import argparse
import json
import os
import re
import sys

# ═══ exp 解析 ═══════════════════════════════════════════

def parse_exp(path):
    """exp → [{seq, cmd, text, params}]"""
    out = []
    with open(path, encoding='utf-8', errors='replace') as f:
        for i, line in enumerate(f, 1):
            s = line.strip().rstrip(';').strip()
            if not s or s.startswith(('#', '/*')) or s in ('{', '}'):
                continue
            if ':' in s:
                head, params_str = s.split(':', 1)
            else:
                head, params_str = s, ''
            head = head.strip()
            m = re.match(r'^(\w+)\s+([\w.-]+)$', head)
            cmd = f"{m.group(1)} {m.group(2)}" if m else head
            params = {}
            for pm in re.finditer(r'(\w+)=(?:"([^"]*)"|([^,;]+))', params_str):
                key, v1, v2 = pm.group(1), pm.group(2), pm.group(3)
                params[key] = v1 if v1 is not None else (v2 or '').strip()
            out.append({'seq': i, 'cmd': cmd, 'text': s, 'params': params})
    return out


# ═══ 官方特性文档索引 ═══════════════════════════════════

def load_feature_docs(feat_dir):
    """特性文档库（JSON 概述 + MD 完整页）→ [{title, summary, scripts, doc_path}]

    MD 版（zh-cn_opi_*.md）是完整操作文档：操作场景/必备事项/操作步骤/任务示例，
    任务示例含完整 MML 脚本（官方示例命令基准）。
    JSON 版仅概述文字（feature_name/feature_description），且与 MD 成对存在——
    同 topic 的 JSON 仅在没有 MD 时加载（避免重复收录）。
    """
    # 先收集全部 md 的 topic id
    md_topics = set()
    for root, _dirs, files in os.walk(feat_dir):
        for fn in files:
            if fn.endswith('.md'):
                md_topics.add(fn[:-3])
    feats = []
    for root, _dirs, files in os.walk(feat_dir):
        for fn in files:
            if fn.endswith('.md'):
                path = os.path.join(root, fn)
                try:
                    with open(path, encoding='utf-8') as f:
                        text = f.read()
                except Exception:
                    continue
                rec = parse_feature_md(text, os.path.relpath(path, feat_dir))
                if rec:
                    feats.append(rec)
            elif fn.endswith('.json'):
                if fn[:-5] in md_topics:
                    continue   # 已有 MD 完整版，跳过 JSON 概述
                try:
                    with open(os.path.join(root, fn), encoding='utf-8') as f:
                        d = json.load(f)
                    feats.append({
                        'title': d.get('feature_name', ''),
                        'summary': d.get('feature_description', ''),
                        'scripts': [],
                        'doc_path': os.path.relpath(os.path.join(root, fn), feat_dir),
                    })
                except Exception:
                    pass
    return feats


def parse_feature_md(text, doc_path):
    """解析特性文档 MD → {title, summary, scripts, cmd_chain, all_cmd_types, doc_path}"""
    lines = text.split('\n')
    title = ''
    for ln in lines:
        if ln.startswith('# '):
            title = ln[2:].strip()
            break
    if not title:
        return None
    # 分节
    sections = {}
    cur = None
    for ln in lines:
        if ln.startswith('## '):
            cur = ln[3:].strip()
            sections[cur] = []
        elif cur is not None:
            sections[cur].append(ln)
    # 代码块脚本：任务示例 + 操作步骤（配置实例文档的命令嵌在操作步骤中）
    scripts = []
    for sec in ('任务示例', '操作步骤'):
        in_code = False
        buf = []
        for ln in sections.get(sec, []):
            if ln.strip().startswith('```'):
                if in_code:
                    scripts.append('\n'.join(buf))
                    buf = []
                    in_code = False
                else:
                    in_code = True
            elif in_code:
                buf.append(ln)
        if in_code and buf:
            scripts.append('\n'.join(buf))
    # 操作步骤命令链（**CMD** 序列）
    cmd_chain = []
    for ln in sections.get('操作步骤', []):
        m = re.search(r'\*\*([A-Z]+ [A-Z0-9]+)\*\*', ln)
        if m:
            cmd_chain.append(m.group(1))
    # 数据表命令（必备事项数据表的命令类别）
    data_cmds = []
    for ln in sections.get('必备事项', []):
        m = re.match(r'\|\s*([A-Z]+ [A-Z0-9]+)\s*\|', ln)
        if m and m.group(1) not in data_cmds:
            data_cmds.append(m.group(1))
    # 脚本命令类型全集（用于特性匹配）
    all_cmd_types = set()
    for s in scripts:
        for ct in re.findall(r'^\s*(?://[^\n]*\n\s*)?([A-Z]+ [A-Z0-9]+):', s, re.M):
            all_cmd_types.add(ct)
    all_cmd_types.update(cmd_chain)
    all_cmd_types.update(data_cmds)
    # 概述 = 操作场景
    summary = '\n'.join(sections.get('操作场景', [])).strip()
    return {
        'title': title,
        'summary': summary,
        'scripts': scripts,
        'cmd_chain': cmd_chain,
        'all_cmd_types': all_cmd_types,
        'doc_path': doc_path,
    }


def match_official(feats, kws, script_cmds=None):
    """匹配官方特性文档：标题关键词 OR 脚本命令类型命中（去重同名）

    返回带 match_reason 标注（关键词命中的词 / 命中的脚本命令）。
    """
    hits, seen = [], set()
    for kw in kws or []:
        for f in feats:
            name = f.get('title', '')
            if kw in name and name not in seen:
                seen.add(name)
                hits.append({**f, 'match_reason': f"标题关键词「{kw}」"})
    for sc in script_cmds or []:
        for f in feats:
            if sc in f.get('all_cmd_types', set()) and f['title'] not in seen:
                seen.add(f['title'])
                hits.append({**f, 'match_reason': f"脚本含命令 {sc}"})
    return hits


# ═══ 官方 MML 命令文档索引 ═══════════════════════════════

def load_cmd_docs(mml_dir):
    """MML 命令文档 → {命令类型: {path, function, example}}

    命名规则：add_gretunnel.md → ADD GRETUNNEL；set_uppfcppath.md → SET UPPFCPPATH
    """
    idx = {}
    if not mml_dir or not os.path.isdir(mml_dir):
        return idx
    for fn in os.listdir(mml_dir):
        if not fn.endswith('.md'):
            continue
        parts = fn[:-3].split('_', 1)
        if len(parts) != 2 or not parts[0].isalpha():
            continue
        op, rest = parts[0].upper(), parts[1].upper()
        cmd_type = f"{op} {rest}"
        path = os.path.join(mml_dir, fn)
        idx[cmd_type] = {'path': fn, 'function': '', 'example': ''}
        try:
            with open(path, encoding='utf-8') as f:
                text = f.read()
            m = re.search(r'#### 命令功能\s*\n+(.*?)(?=\n#### |\Z)', text, re.S)
            if m:
                idx[cmd_type]['function'] = m.group(1).strip()
            m = re.search(r'#### 使用实例\s*\n+(.*?)(?=\n#### |\Z)', text, re.S)
            if m:
                idx[cmd_type]['example'] = m.group(1).strip()
        except Exception:
            pass
    return idx


# ═══ MD 渲染 ════════════════════════════════════════════

def render_commands(cmds):
    lines = []
    for c in cmds:
        lines.append(f"    ; {c['seq']:>5d} | {c['text']}")
    return '\n'.join(lines)


def gen_feature_md(feat_cfg, gt, exp_cmds, feats, cmd_docs, out_dir):
    fid = feat_cfg['id']
    title = feat_cfg['title']
    lines = []
    lines.append(f"# {title}")
    lines.append("")
    lines.append(f"> 特性 ID：`{fid}` ｜ 官方命令树分类：{feat_cfg.get('cmd_tree_cat', '-')}")
    note = feat_cfg.get('note', '')
    if note:
        lines.append(f"> {note}")
    lines.append("")

    # 命令类型集合（groundtruth 特性用其链命令类型，exp 特性用清单）
    if feat_cfg['source'] == 'groundtruth':
        feat = gt['features'][feat_cfg['gt_feature']]
        insts = feat['instances']
        cmd_types = []
        for inst in insts.values():
            for c in inst['commands']:
                if c['cmd'] not in cmd_types:
                    cmd_types.append(c['cmd'])
            for c in inst.get('external_refs', []):
                if c['cmd'] not in cmd_types:
                    cmd_types.append(c['cmd'])
        exp_count = sum(len(i['commands']) for i in insts.values())
        n_inst = len(insts)
    else:
        cmd_types = list(feat_cfg['cmds'])
        cmds = [c for c in exp_cmds if c['cmd'] in set(cmd_types)]
        exp_count = len(cmds)
        anchor_param = feat_cfg.get('anchor_param')
        n_inst = len({c['params'].get(anchor_param) for c in cmds
                      if anchor_param and c['params'].get(anchor_param)}) if anchor_param else None

    # ── §1 特性概述（官方特性文档）───────────────────────
    lines.append("## 1. 特性概述（官方特性文档）")
    lines.append("")
    off = match_official(feats, feat_cfg.get('official_kws', []),
                         feat_cfg.get('script_cmds', []))
    if off:
        for f in off:
            lines.append(f"### {f['title']}")
            lines.append("")
            if f.get('summary'):
                # 只展示场景第一段（匹配文档多时保持精炼）
                para = f['summary'].split('\n\n')[0].strip()
                lines.append(para)
                lines.append("")
            lines.append(f"> 来源：`{f['doc_path']}` ｜ 匹配：{f.get('match_reason', '-')}")
            lines.append("")
    else:
        lines.append("> ⚠️ UEG 特性库（v21.12.2）无对应特性文档页。")
        lines.append("> 官方依据降级为：MML 命令文档（见 §3）。")
        lines.append("")

    # ── §2 官方示例基准（特性文档任务示例）────────────────
    lines.append("## 2. 官方示例基准（特性文档任务示例脚本）")
    lines.append("")
    script_cmd_types = set()
    off_with_scripts = [f for f in off if f.get('scripts')]
    if off_with_scripts:
        for f in off_with_scripts:
            for s in f['scripts']:
                for ct in re.findall(r'^\s*(?://[^\n]*\n\s*)?([A-Z]+ [A-Z0-9]+):', s, re.M):
                    script_cmd_types.add(ct)
        # 每篇文档先过滤出本特性相关块，按相关块数降序取前 3（避免选到
        # 总块多但相关块少的配置实例长文档）
        docs = []
        for f in off_with_scripts:
            kept = []
            for s in f['scripts']:
                blk_types = set(re.findall(r'^\s*(?://[^\n]*\n\s*)?([A-Z]+ [A-Z0-9]+):', s, re.M))
                if blk_types and not (blk_types & set(cmd_types)):
                    continue   # 块内有命令但与本特性无关
                kept.append(s)
            if kept:
                docs.append((f, kept))
        if len(docs) > 3:
            lines.append(f"> 共 {len(docs)} 篇特性文档含本特性示例脚本；"
                         f"以下展示相关脚本最全的 3 篇，其余见 §1 来源路径。")
            lines.append("")
        shown_any = False
        for f, kept_blocks in sorted(docs, key=lambda x: -len(x[1]))[:3]:
            shown_any = True
            lines.append(f"### {f['title']}")
            lines.append("")
            lines.append(f"> 来源：`{f['doc_path']}`")
            lines.append("")
            if f.get('cmd_chain'):
                lines.append(f"**操作步骤命令链**：{' → '.join(f['cmd_chain'])}")
                lines.append("")
            if len(kept_blocks) > 15:
                shown, rest = kept_blocks[:15], kept_blocks[15:]
            else:
                shown, rest = kept_blocks, []
            for s in shown:
                lines.append("```mml")
                lines.append(s.strip())
                lines.append("```")
                lines.append("")
            notes = []
            if rest:
                notes.append(f"共 {len(kept_blocks)} 个相关脚本块，展示前 15 个")
            if len(kept_blocks) < len(f['scripts']):
                notes.append(f"另有 {len(f['scripts']) - len(kept_blocks)} 个其他特性脚本块省略")
            if notes:
                lines.append(f"> {'；'.join(notes)}（完整文档见来源路径）。")
                lines.append("")
        if off_with_scripts and not shown_any:
            lines.append("> 匹配的特性文档无本特性相关示例脚本；降级为 MML 命令文档示例（见 §3）。")
            lines.append("")
    else:
        lines.append("> 特性文档无任务示例脚本；降级为 MML 命令文档示例（见 §3）。")
        lines.append("")

    # ── §3 官方命令文档示例（每条命令的使用实例）─────────
    lines.append("## 3. 官方命令文档示例（补充）")
    lines.append("")
    lines.append("| 命令类型 | 官方命令文档 | 官方示例 |")
    lines.append("|---|---|---|")
    for ct in cmd_types:
        doc = cmd_docs.get(ct)
        has = '✓' if doc and doc['example'] else ('△' if doc else '✗')
        docname = doc['path'] if doc else '—'
        lines.append(f"| `{ct}` | {has} `{docname}` | 见下 |")
    lines.append("")
    for ct in cmd_types:
        doc = cmd_docs.get(ct)
        if not doc:
            lines.append(f"### {ct}")
            lines.append("")
            lines.append("> ⚠️ MML 命令文档库无此命令定义。")
            lines.append("")
            continue
        lines.append(f"### {ct}（{doc['path']}）")
        lines.append("")
        if doc['function']:
            fn = doc['function'].split('\n')[0]
            lines.append(f"**命令功能**：{fn}")
            lines.append("")
        if doc['example']:
            ex = doc['example']
            code = re.search(r'```\w*\n(.*?)```', ex, re.S)
            if code:
                lines.append("**官方示例**：")
                lines.append("")
                lines.append("```mml")
                lines.append(code.group(1).strip())
                lines.append("```")
            else:
                lines.append("**官方示例**：")
                lines.append("")
                lines.append("```mml")
                lines.append(ex.strip())
                lines.append("```")
            lines.append("")

    # ── §4 映射对照 ──────────────────────────────────────
    lines.append("## 4. 映射对照（exp 命令 ↔ 官方文档）")
    lines.append("")
    lines.append("| 命令类型 | 特性文档脚本 | 官方命令文档 | 官方示例 | exp 命令数 |")
    lines.append("|---|---|---|---|---|")
    for ct in cmd_types:
        doc = cmd_docs.get(ct)
        doc_ok = '✓' if doc else '✗'
        ex_ok = '✓' if doc and doc['example'] else '✗'
        script_ok = '✓' if ct in script_cmd_types else '—'
        n = 0
        if feat_cfg['source'] == 'groundtruth':
            n = sum(1 for inst in insts.values()
                    for c in inst['commands'] + inst.get('external_refs', [])
                    if c['cmd'] == ct)
        else:
            n = sum(1 for c in exp_cmds if c['cmd'] == ct)
        lines.append(f"| `{ct}` | {script_ok} | {doc_ok} | {ex_ok} | {n} |")
    lines.append("")

    # ── §5 exp 实际配置 ──────────────────────────────────
    if feat_cfg['source'] == 'groundtruth':
        lines.append(f"## 5. exp 实际配置分析（{n_inst} 个实例，{exp_count} 条链命令）")
        lines.append("")
        lines.append("> 来源：exp 原文 groundtruth 实例链，命令带 EXP 行号")
        lines.append("")
        for idx, (anchor, inst) in enumerate(sorted(insts.items()), 1):
            cmds = inst['commands']
            lines.append(f"### 5.{idx} 实例 {anchor}（{len(cmds)} 条链命令）")
            lines.append("")
            lines.append("```text")
            lines.append(render_commands(cmds))
            lines.append("```")
            lines.append("")
            ext = inst.get('external_refs', [])
            if ext:
                lines.append(f"跨 VRF 弱关联（external_refs，归属其他 VRF）：")
                lines.append("")
                lines.append("```text")
                lines.append(render_commands(ext))
                lines.append("```")
                lines.append("")
    else:
        cmds = [c for c in exp_cmds if c['cmd'] in set(feat_cfg['cmds'])]
        anchor_param = feat_cfg.get('anchor_param')
        if anchor_param:
            groups = {}
            for c in cmds:
                key = c['params'].get(anchor_param, '(无锚点值)')
                groups.setdefault(key, []).append(c)
            lines.append(f"## 5. exp 实际配置分析（{len(groups)} 个实例，按 {anchor_param} 划分）")
            lines.append("")
            lines.append("> 来源：exp 原文按命令类型提取（命令带 EXP 行号）")
            lines.append("")
            for idx, (anchor, glist) in enumerate(sorted(groups.items()), 1):
                lines.append(f"### 5.{idx} 实例 {anchor}（{len(glist)} 条命令）")
                lines.append("")
                lines.append("```text")
                lines.append(render_commands(glist))
                lines.append("```")
                lines.append("")
        else:
            lines.append(f"## 5. exp 实际配置分析（全局参数，{len(cmds)} 条）")
            lines.append("")
            lines.append("> 来源：exp 原文按命令类型提取（命令带 EXP 行号）；全局参数无实例概念")
            lines.append("")
            lines.append("```text")
            lines.append(render_commands(cmds))
            lines.append("```")
            lines.append("")

    out_path = os.path.join(out_dir, f"{fid}.md")
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))
    print(f"  ✅ {fid}: {out_path}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('exp')
    ap.add_argument('groundtruth')
    ap.add_argument('--docs', default=os.path.join(os.path.dirname(__file__),
                    '..', 'rules', 'feature_docs.yaml'))
    ap.add_argument('--feat-dir', default=os.path.join(os.environ.get('KB_SRC', os.path.expanduser('~/workspace/zhijian')),
                    'output_ueg_feature/output_ueg_feature_v3'))
    ap.add_argument('--mml-dir', default=os.path.join(os.environ.get('KB_SRC', os.path.expanduser('~/workspace/zhijian')),
                    'output_ueg_mml/output_ueg_mml/MML/Document'))
    ap.add_argument('-o', '--outdir', required=True)
    args = ap.parse_args()

    import yaml
    with open(args.docs, encoding='utf-8') as f:
        cfg = yaml.safe_load(f)

    exp_cmds = parse_exp(args.exp)
    print(f"解析 exp: {len(exp_cmds)} 条命令")
    gt = json.load(open(args.groundtruth, encoding='utf-8'))
    feats = load_feature_docs(args.feat_dir)
    print(f"官方特性文档: {len(feats)} 条")
    cmd_docs = load_cmd_docs(args.mml_dir)
    print(f"官方 MML 命令文档: {len(cmd_docs)} 条")

    os.makedirs(args.outdir, exist_ok=True)
    for fc in cfg['features']:
        gen_feature_md(fc, gt, exp_cmds, feats, cmd_docs, args.outdir)

    # 索引 README
    idx = ["# 特性配置分析（case1.1 EXP Groundtruth）", "",
           f"> exp: {args.exp}", f"> groundtruth: {args.groundtruth}", ""]
    for fc in cfg['features']:
        idx.append(f"- [{fc['title']}]({fc['id']}.md) `{fc['id']}` — {fc.get('note', '')}")
    with open(os.path.join(args.outdir, 'README.md'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(idx) + '\n')
    print("  ✅ README 索引")


if __name__ == '__main__':
    main()

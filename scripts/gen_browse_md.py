#!/usr/bin/env python3
"""实例浏览 MD 生成器：文档基线（原始特性示例） vs exp 实例（挑出的）逐命令对照。

用户明确要求（2026-08-28）：给人浏览的判定/实例展示必须能对照基线——
"看不到基线，我怎么对比你挑的对不对"：MD 里先写清楚特性文档原始示例是啥，
再写挑出的 exp 实例是啥，逐命令并排，用户才能验证判定。

用法：
    venv-web/bin/python scripts/gen_browse_md.py <case目录> [F编号 ...]

    <case目录> 需含 EXPMML_*.txt（exp 原文）和 match_result.json（match_features 产物）
    F编号 缺省 = 5 个代表特性（configured 实例级 / not_configured 实例级+方向 /
             not_configured 命令级 等形态各一）

产物：<case目录>/实例浏览/<F>_<标题>.md，生成后建议 open 打开供浏览。

结构（每个特性一份）：
    一、文档基线 —— 指纹 core 命令在官方特性文档代码块的原始示例
        （场景括号原样保留：ADD POOL(风筝S)/ADD UPPOOL(风筝M或L)，标注 OR 变体组）
    二、exp 实例对照 —— 逐命令：文档基线一条 → exp 实例一条（行号+原文）
        hit：实例命令贴所属实例行号；global 命令（存在检查）标注"共 N 条"+首条示例
        miss：贴 exp 实际行区分"命令存在但值不符/方向不符" vs "局点未配置"
        （方向不符如 F095：基线 LOADRPTSW=ENABLE vs exp @6914 LOADRPTSW=DISABLE）
"""
import json
import os
import sys

sys.path.insert(0, os.path.expanduser('~/workspace/exp-groundtruth-verify/scripts'))
import gen_feature_all as gfa  # noqa: E402

FEAT_DIR = os.path.expanduser('~/workspace/zhijian/output_ueg_feature/output_ueg_feature_v2')
FP = os.path.expanduser('~/workspace/exp-groundtruth-verify/rules/features_ueg.yaml')

DEFAULT_PICKS = [
    ('F001', 'configured 实例级·语义干净'),
    ('F083', 'configured 实例级·多实例典型'),
    ('F560', 'not_configured 实例级+开关方向不符'),
    ('F095', 'not_configured 命令级+开关方向不符'),
    ('F674', 'not_configured 命令级·多开关未激活'),
]
STATUS_ICON = {'configured': '✅ 已配置', 'not_configured': '❌ 未配置', 'manual': '⚠️ 需人工'}


def find_exp(case_dir):
    for f in sorted(os.listdir(case_dir)):
        if f.startswith('EXPMML_') and f.endswith('.txt'):
            return os.path.join(case_dir, f)
    return None


def baseline_for(doc, cmd):
    """文档代码块中该命令的原始示例行（含场景括号原样），去重取前 2 条"""
    out = []
    for s in doc.get('scripts', []):
        for ln in s.split('\n'):
            for span in gfa.MML_CMD_RE.findall(ln):
                if cmd in gfa.cmd_spans_to_names(span):
                    t = ln.strip()
                    if t and t not in out:
                        out.append(t)
                    break
            if len(out) >= 2:
                return out
    return out


def render(fid, r, note, fps, docs_by_path, cmds, seq2raw):
    d = r['detail']
    feat = fps[fid]
    doc = docs_by_path.get(feat.get('doc_path'))
    core_all = feat.get('core', {}).get('L1', []) + feat.get('core', {}).get('L2', []) + feat.get('core', {}).get('L3', [])
    or_groups = doc.get('cmd_or_groups', []) if doc else []
    L = []
    L.append(f"# {fid} {r['title']}")
    L.append('')
    L.append(f"> 判定：{STATUS_ICON.get(r['status'], r['status'])}　|　域：{r['domain']}　|　{note}")
    L.append('')

    # ── 文档基线：特性文档原始示例 ──
    L.append('## 一、文档基线（特性文档原始示例）')
    L.append('')
    L.append('> 来源：特性文档「操作步骤/必备事项」代码块原文（场景括号原样保留，如 ADD POOL(风筝S)/ADD UPPOOL(风筝M或L)）')
    L.append('')
    for cmd in core_all:
        base = baseline_for(doc, cmd)
        grp = [g for g in or_groups if cmd in g]
        tag = f'（场景变体 OR：{" / ".join(grp[0])}）' if grp else ''
        if base:
            L.append(f"- **`{cmd}`**{tag}")
            for b in base:
                L.append(f"  - 文档示例：`{b}`")
        else:
            L.append(f"- **`{cmd}`**{tag}（文档无代码块示例，仅表格/步骤引用）")
    L.append('')

    # ── exp 实例对照 ──
    if d.get('mode') == 'instances':
        L.append('## 二、exp 实例对照（从现网 EXP 挑出的实例）')
        L.append('')
        for it in d['instances']:
            icon = '✅' if it['status'] == 'configured' else ('🟡' if it['status'] == 'partial' else '❌')
            L.append(f"### {icon} 实例：{it['key']}（{it['status']}）")
            L.append('')
            for cmd in it['hit']:
                base = baseline_for(doc, cmd)
                grp = [g for g in or_groups if cmd in g]
                tag = f'（OR：{" / ".join(grp[0])}）' if grp else ''
                seqs = it['cmds'].get(cmd, [])
                L.append(f"**`{cmd}`**{tag} ✅ 命中")
                if base:
                    L.append(f"- 文档基线：`{base[0]}`")
                if seqs:
                    for s in seqs[:3]:
                        L.append(f"- exp 实例：@{s} `{seq2raw.get(s, '')}`")
                else:
                    # 全局型命令：贴 exp 存在的首条作证据
                    gs = [x for x in cmds if x['cmd'] == cmd]
                    L.append(f"- exp 实例：全局命令存在（共 {len(gs)} 条），例：@{gs[0]['seq']} `{gs[0]['raw']}`" if gs
                             else '- exp 实例：未找到（判定为命中？）')
                L.append('')
            for cmd in it['miss']:
                base = baseline_for(doc, cmd)
                grp = [g for g in or_groups if cmd in g]
                tag = f'（OR：{" / ".join(grp[0])}）' if grp else ''
                hits = [x for x in cmds if x['cmd'] in ([cmd] + (grp[0] if grp else []))]
                L.append(f"**`{cmd}`**{tag} ❌ 未匹配")
                if base:
                    L.append(f"- 文档基线：`{base[0]}`")
                if hits:
                    for h in hits[:3]:
                        L.append(f"- exp 实际：@{h['seq']} `{h['raw']}`（命令存在但值不符/方向不符）")
                else:
                    L.append('- exp 实际：未找到该命令（局点未配置）')
                L.append('')
        if d.get('notes'):
            L.append(f"> ⚠️ {d['notes']}")
            L.append('')
    else:
        L.append('## 二、exp 对照（命令级判定）')
        L.append('')
        for cmd in d.get('core_hit', []):
            base = baseline_for(doc, cmd)
            L.append(f"**`{cmd}`** ✅ 命中")
            if base:
                L.append(f"- 文档基线：`{base[0]}`")
            ev = d.get('evidence', {}).get(cmd)
            if ev:
                for s in ev['seqs'][:3]:
                    L.append(f"- exp 实例：@{s} `{seq2raw.get(s, '')}`")
            L.append('')
        for cmd in d.get('core_miss', []):
            base = baseline_for(doc, cmd)
            dm = [x for x in d.get('dir_mismatch', []) if x['cmd'] == cmd]
            L.append(f"**`{cmd}`** ❌ 未匹配")
            if base:
                L.append(f"- 文档基线：`{base[0]}`")
            if dm:
                for p, dv, ev in dm[0]['params']:
                    L.append(f"- 值方向不符：文档期望 `{p}={','.join(dv)}`，exp 实际 `{p}={','.join(ev)}`")
            hits = [x for x in cmds if x['cmd'] == cmd]
            if hits:
                for h in hits[:2]:
                    L.append(f"- exp 实际：@{h['seq']} `{h['raw']}`")
            else:
                L.append('- exp 实际：未找到该命令（局点未配置）')
            L.append('')
    L.append('---')
    L.append('> 对照说明：文档基线 = 官方特性文档原始示例（事实层参照）；exp 实例 = 现网 EXP 原文'
            '（事实层，行号可回溯）。判定是分析层（指纹×exp），二者差异即需人工审视点。')
    L.append('')
    return '\n'.join(L)


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    CASE = sys.argv[1]
    EXP = find_exp(CASE)
    if not EXP:
        print(f'未找到 EXPMML_*.txt: {CASE}')
        sys.exit(1)
    OUT = os.path.join(CASE, '实例浏览')
    os.makedirs(OUT, exist_ok=True)

    import yaml
    fps = yaml.safe_load(open(FP, encoding='utf-8'))['features']
    docs = gfa.load_feature_docs(FEAT_DIR)
    docs_by_path = {d['doc_path']: d for d in docs}

    mr = json.load(open(os.path.join(CASE, 'match_result.json'), encoding='utf-8'))
    R = mr['results']
    cmds = gfa.parse_exp(EXP)
    seq2raw = {c['seq']: c['raw'] for c in cmds}

    picks = DEFAULT_PICKS
    if len(sys.argv) > 2:
        picks = [(f, '指定浏览') for f in sys.argv[2:]]

    paths = []
    for fid, note in picks:
        r = R.get(fid)
        if not r:
            print(f'跳过 {fid}（不存在）')
            continue
        p = os.path.join(OUT, f"{fid}_{r['title'].replace('/', '_')}.md")
        with open(p, 'w', encoding='utf-8') as f:
            f.write(render(fid, r, note, fps, docs_by_path, cmds, seq2raw))
        paths.append(p)
        print('生成:', p)
    print('共', len(paths), '个文件')


if __name__ == '__main__':
    main()

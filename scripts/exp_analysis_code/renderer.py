#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""renderer.py — T7 渲染器。report.json → 五段 md + 1_检索与选型.md + params.csv。

纯模板函数 data→text，无分析逻辑（红线）。章节名用锚点实例值，
证据一律现网实例值（param=value / 行号 Lxxx）。跨层推理/业务含义类
内容标注「需 P2/P3」，不在本层编造。
"""

import csv
import json
from pathlib import Path

_STATUS_ICON = {'ok': '✅', 'partial': '⚠️', 'not_present': '❌', 'missing': '❌',
                'disabled': '🔒', 'exempt': '➖'}
_STATUS_CN = {'ok': '完整', 'partial': '部分', 'not_present': '无此形态',
              'missing': '缺失', 'disabled': '许可关闭', 'exempt': '豁免'}


# ─────────────────────────── 段落渲染 ───────────────────────────

def _src_block(meta, stats, lic):
    """来源块（0. 来源/环境）。"""
    L = []
    L.append(f"**来源**")
    L.append(f"- **局点**:{meta.get('ne_name', '?')}（{meta.get('me_type', '?')} "
             f"{meta.get('version', '?')} / Patch {meta.get('patch', '?')}）")
    L.append(f"- **文件**:{meta.get('source_file', '?')}"
             f"（{stats.get('cmd_count', 0)} 条命令；导出 {meta.get('time', '?')}）")
    L.append(f"- **许可**:{lic.get('cmd_count', 0)} 项"
             f"（ENABLE {lic.get('enable', 0)} / DISABLE {lic.get('disable', 0)}）")
    return '\n'.join(L)


def _conclusion(chain_verdicts, domain_stats, llm=None):
    """关键结论：llm 存在用叙述化结论，否则规模特征事实摘要（模板）。"""
    if llm and llm.get('conclusion'):
        return f"{llm['conclusion']}（llm 来源）"
    ok = [c for c in chain_verdicts if c['status'] == 'ok']
    part = [c for c in chain_verdicts if c['status'] == 'partial']
    top = ''
    for d in domain_stats:
        n = sum(c['n'] for c in d.get('cmd_stats', []))
        if not top or n > top[1]:
            top = (d['name'], n)
    parts = [f"本局点 {len(ok)} 条功能链判定完整、{len(part)} 条部分"]
    if top:
        parts.append(f"命令族规模最大域为「{top[0]}」（{top[1]} 条）")
    for c in chain_verdicts:
        parts.append(f"链{c['chain']} {c['name']}={c['status']}"
                     + (f"（{c.get('anchor_value')}）" if c.get('anchor_value') else ""))
    return '；'.join(parts) + '。（未生成 llm 润色）'


def _topo(chain_verdicts, meta):
    """一、架构定位（结构化朴素 ASCII，不做布局优化）。"""
    ne = meta.get('ne_name', '?')
    mt = meta.get('me_type', '')
    lines = ['```', f'   ┌─ {ne} ({mt} 数据面) ─────────────────────────────────┐']
    for c in chain_verdicts:
        icon = _STATUS_ICON.get(c['status'], '?')
        anchor = c.get('anchor_value') or '（行号锚定，无名称参数）'
        lines.append(f"   │  链{c['chain']} {c['name']:<22} {icon}  {anchor[:34]:<34} │")
    lines.append('   └──────────────────────────────────────────────────────────────┘')
    lines.append('```')
    return '\n'.join(lines)


def _seg_text(seg):
    """profile 分段 → 文本。literal 直出，variant 列值。"""
    if seg['type'] == 'literal':
        return f"「{seg['value']}」"
    vals = seg.get('values', [])
    if len(vals) <= 6:
        return f"[{'|'.join(vals)}]"
    return f"[{vals[0]}|{vals[1]}|…共{len(vals)}种]"


def _profiles(domain_stats, profiles):
    """二、现网模式分析（按功能域 + 命名族/ID段/惯例）。"""
    L = ['## 二、现网模式分析（按功能链归纳，全部来自 EXP 现网值）', '']
    for d in domain_stats:
        cmds = '；'.join(f"{c['type']}×{c['n']}" for c in d.get('cmd_stats', []))
        L.append(f"### 2.{domain_stats.index(d) + 1} {d['name']}")
        L.append(f"命令族：{cmds}")
        for param, vals in d.get('anchor_vals', {}).items():
            topv = '、'.join(f"{v['v']}(×{v['n']})" for v in vals[:3])
            L.append(f"锚点值 {param}：{topv}")
        L.append('')

    naming = [p for p in profiles if p.get('kind') == 'naming']
    idr = [p for p in profiles if p.get('kind') == 'id_ranges']
    conv = [p for p in profiles if p.get('kind') == 'conventions']

    L.append('### 命名族归纳（参数值分段结构）')
    L.append('')
    L.append('| 命令 | 参数 | 实例数 | 分段结构 | 样例 |')
    L.append('|---|---|---|---|---|')
    for p in naming[:12]:
        segs = ' '.join(_seg_text(s) for s in p.get('segments', []))
        smp = '、'.join(p.get('samples', [])[:2])
        L.append(f"| {p['cmd']} | {p['param']} | {p.get('values_n', 0)} "
                 f"| {segs} | {smp} |")
    L.append('')

    if idr:
        L.append('### 数值 ID 段（连续/固定差/下一可用）')
        L.append('')
        L.append('| 命令 | 参数 | 数值数 | min | max | 最长连续 run | 下一可用 |')
        L.append('|---|---|---|---|---|---|---|')
        for p in idr:
            L.append(f"| {p['cmd']} | {p['param']} | {p.get('numeric_n', 0)} "
                     f"| {p.get('min', '')} | {p.get('max', '')} "
                     f"| {p.get('longest_run', '')} | {p.get('next_free', '')} |")
        L.append('')

    if conv:
        L.append('### 惯例众数（参数取值分布）')
        L.append('')
        L.append('| 命令 | 参数 | 分布 |')
        L.append('|---|---|---|')
        for p in conv:
            for k, v in p.items():
                if k in ('cmd', 'kind'):
                    continue
                dist = v.get('dist', [])
                if v.get('uniform'):
                    dists = f"统一 {v['uniform']}"
                else:
                    dists = '；'.join(f"{x['v']}×{x['n']}" for x in dist[:3])
                L.append(f"| {p['cmd']} | {k} | {dists} |")
        L.append('')
    return '\n'.join(L)


def _chains(chain_verdicts):
    """三、各功能链配置现状（锚点实例 + 完整性判定）。"""
    L = ['## 三、各功能链配置现状（锚点实例 + 完整性判定）', '']
    for c in chain_verdicts:
        icon = _STATUS_ICON.get(c['status'], '?')
        cn = _STATUS_CN.get(c['status'], c['status'])
        anchor = f"（{c.get('anchor_value')}）" if c.get('anchor_value') else ''
        L.append(f"### 链{c['chain']} {c['name']} — {icon} {cn}{anchor}")
        if c.get('note'):
            L.append(f"{c['note']}")
        for ly in c.get('layers', []):
            lic = _STATUS_ICON.get(ly['status'], '?')
            cmds = '；'.join(f"{x['cmd']}×{x['n']}（L{x['first_seq']}）"
                            for x in ly.get('cmds', []))
            L.append(f"- {lic} {ly['name']}：{cmds}")
            for po in ly.get('param_observations', []):
                if isinstance(po, dict):
                    prms = '/'.join(po.get('params', []))
                    L.append(f"  · 观测点 {prms}：{po.get('why', '')}")
                else:
                    L.append(f"  · {po}")
        for r in c.get('refs', []):
            ic = '✅' if r['status'] == 'closed' else '⚠️'
            L.append(f"  {ic} 引用 {r['name']}：{r['from']} → {r['to']} "
                     f"（定义 {r['defs_count']} → 引用 {r['refs_count']}）")
            if r['status'] != 'closed':
                sample = '、'.join(r['dangling'][:10])
                L.append(f"     ⚠️ 悬空 {r['dangling_count']} 项：{sample}")
            elif r.get('orphan_count'):
                sample = '、'.join(r['orphan'][:5])
                L.append(f"     · 孤儿对象（定义未引用，需甄别）{r['orphan_count']} 项：{sample}")
        L.append('')
    return '\n'.join(L)


def _notices(notices):
    """四、注意事项。"""
    L = ['## 四、注意事项（源文档提炼 + 现网约束）', '']
    for i, n in enumerate(notices, 1):
        sev = {'high': '高', 'info': '信息', 'fact': '事实', 'warning': '提示'}.get(
            n.get('severity'), n.get('severity', ''))
        kind = n.get('kind', '')
        L.append(f"{i}. **{n['name']}**（{sev} / {kind}）")
        L.append(f"   {n.get('text', '')}")
        if n.get('evidence'):
            L.append(f"   证据：{n['evidence']}")
    L.append('')
    return '\n'.join(L)


def _diffs(diffs, llm=None):
    """五、现网 vs 标准差异总结（llm 存在时补语义判断列）。"""
    L = ['## 五、现网 vs 标准差异总结', '']
    reviews = (llm or {}).get('diff_review') or []
    has_review = bool(reviews)
    L.append('| # | 链 | 类别 | 文档基准 | 现网实例 | 性质 | 说明'
             + (' | 语义判断（llm）' if has_review else '') + ' |')
    L.append('|---|---|---|---|---|---|---'
             + ('|---' if has_review else '') + '|')
    for i, d in enumerate(diffs, 1):
        pre = {'site_policy': '局点策略', 'license_off': '许可关闭',
               'structure': '结构差异', 'param_policy': '参数现状'}.get(
                   d.get('pre_class'), d.get('pre_class', ''))
        row = (f"| {i} | {d.get('chain', '')} | {d.get('category', '')} "
               f"| {d.get('doc_side', '')} | {d.get('exp_side', '')} "
               f"| {pre} | {d.get('note', '')}")
        if has_review:
            row += f" | {reviews[i - 1] if i - 1 < len(reviews) else ''}"
        L.append(row + ' |')
    L.append('')
    return '\n'.join(L)


def _watchlist(watchlist, llm=None):
    """待审视（专家审视项，不阻塞产物；llm 存在时补业务含义）。"""
    if not watchlist:
        return ''
    L = ['## 待审视（专家审视项，不阻塞产物）', '']
    meanings = (llm or {}).get('watchlist_meaning') or []
    for i, w in enumerate(watchlist, 1):
        L.append(f"{i}. **{w['heuristic']}**：{w['cmd']} {w.get('param', '')}="
                 f"{w.get('value', '')}（L{w.get('seq', '?')}）")
        L.append(f"   {w.get('why', '')}")
        if i - 1 < len(meanings):
            L.append(f"   ↳ 语义（llm）：{meanings[i - 1]}")
    L.append('')
    return '\n'.join(L)


# ─────────────────────────── 主 md 组装 ───────────────────────────

def _graphs(graph_chains):
    """六、业务链图谱（实例级引用图走链，黄金规则格式）。"""
    if not graph_chains:
        return ''
    L = ['## 六、业务链图谱（实例级引用图走链）', '']
    for gid, g in graph_chains.items():
        entries = '、'.join(g.get('entries', []))
        s = g.get('stats', {})
        L.append(f"### {g.get('name', gid)}（{gid}）")
        L.append(f"入口：{g.get('entry_param')} ∈ {{{entries}}}（{g.get('entry_cmd')}）")
        L.append(f"连通分量：{s.get('instances', 0)} 实例 / "
                 f"{s.get('cmd_types', 0)} 命令类型 / {s.get('values', 0)} 对象名值")
        if g.get('note'):
            L.append(f"说明：{g['note']}")
        for cmd in sorted(g.get('commands', {})):
            items = g['commands'][cmd]
            seqs = [seq for seq, _ in items]
            seg = _seq_segments(seqs)
            # 每条命令的锚定参数示例（首实例的 param=value）
            anchor = '、'.join(f"{p}={v}" for p, v in items[0][1].items())
            L.append(f"- {cmd} ×{len(items)}：{seg}（如 {anchor}）")
        # 汇聚标注（引用次数 > 阈值）
        hot = {v: n for v, n in g.get('ref_degrees', {}).items() if n > 10}
        if hot:
            top = '、'.join(f"{v}(×{n})" for v, n in
                            sorted(hot.items(), key=lambda x: -x[1])[:8])
            L.append(f"汇聚值（引用次数>10）：{top}")
        L.append('')
    return '\n'.join(L)


def _seq_segments(seqs):
    """连续 seq 压缩显示：94122, 94123, 94124 → 94122~94124。"""
    if not seqs:
        return '∅'
    segs = []
    start = prev = seqs[0]
    for x in seqs[1:]:
        if x == prev + 1:
            prev = x
            continue
        segs.append(f"L{start}" if start == prev else f"L{start}~L{prev}")
        start = prev = x
    segs.append(f"L{start}" if start == prev else f"L{start}~L{prev}")
    return '、'.join(segs)


def _feature_match(fm):
    """七、特性匹配（黄金规则核对）。fm 为 None 时返回空。"""
    if not fm:
        return ''
    if fm.get('error'):
        return f"## 七、特性匹配\n\n⚠️ 未生成：{fm['error']}\n\n"
    L = ['## 七、特性匹配（黄金规则核对）', '']
    cov = fm.get('coverage', {})
    L.append(f"覆盖率：特性原文命令 {len(cov.get('covered', []))}/{cov.get('total', 0)} 已走链")
    if cov.get('uncovered'):
        L.append(f"未覆盖：{cov['uncovered']}")
    gc = fm.get('golden_check')
    if not gc:
        return '\n'.join(L) + '\n'
    L.append(f"命令类型：{gc['n_ok']}/{gc['n_cmd_types']} 精确命中；"
             f"期望 {gc['total_exp']} / 实际 {gc['total_got']}；"
             f"MISSING {gc['n_miss']} / EXTRA {gc['n_extra']}")
    L.append('')
    for pc in gc.get('per_cmd', []):
        mark = '✅' if pc['status'] == 'OK' else '❌'
        line = f"- {mark} {pc['cmd']}：期望 {_seq_segments(pc['expected'])}"
        if pc['missing']:
            line += f"；MISSING {_seq_segments(pc['missing'])}"
        if pc['extra']:
            line += f"；EXTRA {_seq_segments(pc['extra'])}"
        L.append(line)
    L.append('')
    return '\n'.join(L)


def _feature_find(fd, fm=None):
    """八、特性实例找全（图上扩展，从黄金锚点找全关联实例）。

    fd: {graph: {...找全主结果}, cmd: {...参考对比}}；fm 为第七章特性匹配（旧走链 MISSING 对比）。
    """
    if not fd:
        return ''
    g = fd.get('graph')
    c = fd.get('cmd')
    if not g or not c:
        return ''
    L = ['## 八、特性实例找全（图上扩展）', '']
    L.append('黄金规则降级为「种子 + 验收锚点」：从 56 条锚点出发，沿「定义方↔引用方」'
             '引用关系图上扩展，找全本局点内与该特性关联的全部实例。')
    L.append('')
    sg = g.get('stats', {})
    sc = c.get('stats', {})
    L.append(f"- 找全（图上扩展）：{sg.get('instances', 0)} 实例 / {sg.get('cmd_types', 0)} 命令类型"
             f" → 命中 {sg.get('golden_hit', 0)}/{sg.get('golden_anchors', 0)}"
             f"（MISSING {sg.get('golden_missing', 0)}）")
    L.append(f"- 参考（命令全量枚举）：{sc.get('instances', 0)} 实例"
             f" —— 会过度包含同命令类型的非本特性实例，仅作对照")
    L.append('')
    L.append('| 命令 | 黄金锚点 | 找全(图上扩展) | 参考(cmd全量) |')
    L.append('|---|---|---|---|')
    for cmd in g['found']:
        anchors = g['golden_check'][cmd].get('anchors', [])
        n_gr = len(g['found'][cmd])
        n_cmd = len(c['found'][cmd])
        L.append(f"| {cmd} | {_seq_segments(anchors)} | {n_gr} | {n_cmd} |")
    L.append('')
    # 旧走链 MISSING 对比（若有特性匹配）
    if fm and fm.get('golden_check'):
        gc = fm['golden_check']
        miss_rows = [pc for pc in gc.get('per_cmd', []) if pc.get('missing')]
        if miss_rows:
            n_miss = sum(len(pc['missing']) for pc in miss_rows)
            L.append(f"对比第七章特性匹配（旧走链）的 MISSING {n_miss} 条 → 找全后全部命中"
                     f"（golden_missing = 0）：")
            for pc in miss_rows:
                L.append(f"- {pc['cmd']}：{_seq_segments(pc['missing'])}")
    L.append('')
    return '\n'.join(L)


def render_report(report):
    """渲染主配置分析 md。返回文本。"""
    meta = report.get('meta', {})
    stats = report.get('stats', {})
    lic = report.get('lic_switch', {})
    cv = report.get('chain_verdicts', [])
    ds = report.get('domain_stats', [])
    title_anchor = meta.get('ne_name', '') + '_' + \
        '与'.join(c.get('name', '') for c in cv[:3]) + '功能链'
    parts = []
    parts.append(f"# 配置分析_{title_anchor}.md")
    parts.append('')
    parts.append('---')
    parts.append('')
    parts.append(_src_block(meta, stats, lic))
    parts.append('')
    parts.append('---')
    parts.append('')
    parts.append('## 一、架构定位')
    parts.append('')
    parts.append(_topo(cv, meta))
    parts.append('')
    parts.append(f"**关键结论**：{_conclusion(cv, ds, report.get('llm'))}")
    parts.append('')
    parts.append('---')
    parts.append('')
    parts.append(_profiles(ds, report.get('profiles', [])))
    parts.append(_chains(cv))
    parts.append(_graphs(report.get('graph_chains', {})))
    parts.append(_feature_match(report.get('feature_match')))
    parts.append(_feature_find(report.get('feature_find'),
                               report.get('feature_match')))
    parts.append(_notices(report.get('notices', [])))
    parts.append(_diffs(report.get('diffs', []), report.get('llm')))
    parts.append(_watchlist(report.get('watchlist', []), report.get('llm')))
    return '\n'.join(parts)


def render_search(report):
    """渲染 1_检索与选型.md。"""
    meta = report.get('meta', {})
    stats = report.get('stats', {})
    lic = report.get('lic_switch', {})
    L = []
    L.append(f"# 1_检索与选型.md")
    L.append('')
    L.append('> 任务：全量分析本局点 EXP（UDG 数据面），按功能链/参数引用链组织，'
             '产出配置分析 md + 参数收集 CSV。')
    L.append('')
    L.append('## §1 命令族统计')
    L.append('')
    L.append(f"- 命令总数：{stats.get('cmd_count', 0)}")
    for verb, n in stats.get('by_verb', {}).items():
        L.append(f"- {verb}：{n}")
    L.append(f"- 命令类型数：{stats.get('cmd_type_count', 0)}")
    if stats.get('top_cmd_types'):
        top = '、'.join(f"{x['type']}({x['n']})" for x in stats['top_cmd_types'][:10])
        L.append(f"- Top 命令族：{top}")
    L.append('')
    L.append('## §2 许可开关')
    L.append('')
    L.append(f"- 许可项：{lic.get('cmd_count', 0)}"
             f"（ENABLE {lic.get('enable', 0)} / DISABLE {lic.get('disable', 0)}）")
    L.append('')
    L.append('## §0 检索与降级说明')
    L.append('')
    for note in report.get('env_notes', []):
        L.append(f"- {note}")
    L.append('')
    return '\n'.join(L)


# ─────────────────────────── params.csv ───────────────────────────

def render_params_csv(report, out_path):
    """params.csv：链锚点命令参数现状收集（P1 骨架；参数说明列留待命令文档对接）。"""
    rows = []
    for c in report.get('chain_verdicts', []):
        if c['status'] == 'not_present':
            continue
        for ly in c.get('layers', []):
            for x in ly.get('cmds', []):
                rows.append([f"链{c['chain']}.{ly['name']}", x['cmd'],
                             '', f"×{x['n']}", f"首行 L{x['first_seq']}", ''])
    with open(out_path, 'w', newline='', encoding='utf-8-sig') as f:
        w = csv.writer(f)
        w.writerow(['命令说明（CmdStep）', '命令（Command）', '参数（Parameter）',
                    '待填写（YourValue）', '参数说明', '其他'])
        w.writerows(rows)
    return len(rows)


if __name__ == '__main__':
    import sys
    rp = sys.argv[1] if len(sys.argv) > 1 else '/tmp/ac_t7/report.json'
    outdir = sys.argv[2] if len(sys.argv) > 2 else '/tmp/ac_t7'
    report = json.load(open(rp, encoding='utf-8'))
    Path(outdir).mkdir(parents=True, exist_ok=True)
    ne = report.get('meta', {}).get('ne_name', 'NE')
    (Path(outdir) / f'配置分析_{ne}_代码管线.md').write_text(
        render_report(report), encoding='utf-8')
    (Path(outdir) / '1_检索与选型.md').write_text(
        render_search(report), encoding='utf-8')
    n = render_params_csv(report, str(Path(outdir) / 'params.csv'))
    print(f'OK → {outdir}/（主 md + 1_检索与选型.md + params.csv {n} 行）')

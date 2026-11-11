#!/usr/bin/env python3
"""生成「版本修正历史与改进效果」HTML。

★ 长期维护说明（2026-11-10 用户要求）：
  数据源改为 docs/version_history.json，不再硬编码在脚本里。
  新增版本时，只需要往 JSON 的 versions 数组末尾追加一条，重跑本脚本即可。

  用法：
    python3 scripts/gen_version_history.py                    # 默认输出 /tmp/version_history.html
    python3 scripts/gen_version_history.py -o out.html        # 指定输出
    python3 scripts/gen_version_history.py --add-version      # 从 git log 辅助生成版本条目草稿
"""
import argparse
import json
import subprocess
from datetime import datetime
from pathlib import Path

PROJ = Path(__file__).resolve().parent.parent
DATA = PROJ / 'docs' / 'version_history.json'
DEFAULT_OUT = Path('/tmp/version_history.html')




def gen_perf_chart(perf):
    """生成性能条形图（按规模分档的阶段1/阶段2 耗时）。"""
    scales = perf.get('by_scale') or []
    if not scales:
        return ''

    W = 1100
    row_h = 54
    H = 40 + row_h * len(scales) + 30
    PAD_L, PAD_R = 130, 170
    plot_w = W - PAD_L - PAD_R

    max_val = max((x.get('total_median') or 0) for x in scales) or 1
    max_val = max_val * 1.15

    out = [f'<svg viewBox="0 0 {W} {H}" style="width:100%;max-width:{W}px;'
           f'background:#fff;border:1px solid #eaeef2;border-radius:6px">']

    for i, sc in enumerate(scales):
        y = 34 + i * row_h
        s1 = sc.get('s1_median') or 0
        s2 = sc.get('s2_median') or 0
        tot = sc.get('total_median') or 0
        n = sc.get('n') or 0

        # 标签
        out.append(f'<text x="{PAD_L - 10}" y="{y + 14}" text-anchor="end" '
                   f'font-size="11" fill="#1f2328">{sc.get("level","")}</text>')
        out.append(f'<text x="{PAD_L - 10}" y="{y + 28}" text-anchor="end" '
                   f'font-size="10" fill="#8c959f">{n} 单</text>')

        # 阶段1 段
        w1 = plot_w * s1 / max_val
        if w1 > 0:
            out.append(f'<rect x="{PAD_L}" y="{y}" width="{w1:.1f}" height="20" '
                       f'fill="#1a7f37" rx="2"/>')
        # 阶段2 段
        w2 = plot_w * s2 / max_val
        if w2 > 0:
            out.append(f'<rect x="{PAD_L + w1:.1f}" y="{y}" width="{w2:.1f}" '
                       f'height="20" fill="#1f6feb" rx="2"/>')

        # 数值
        label = f'{tot:.0f}s'
        out.append(f'<text x="{PAD_L + w1 + w2 + 8:.1f}" y="{y + 14}" '
                   f'font-size="11" font-weight="600" fill="#1f2328">{label}</text>')
        out.append(f'<text x="{PAD_L + w1 + w2 + 8:.1f}" y="{y + 27}" '
                   f'font-size="9" fill="#8c959f">'
                   f'P90 {sc.get("total_p90",0):.0f}s</text>')

    # 图例
    ly = H - 14
    out.append(f'<rect x="{PAD_L}" y="{ly - 9}" width="10" height="10" fill="#1a7f37" rx="2"/>')
    out.append(f'<text x="{PAD_L + 16}" y="{ly}" font-size="10" fill="#1a7f37">'
               f'阶段1 规划（中位）</text>')
    out.append(f'<rect x="{PAD_L + 136}" y="{ly - 9}" width="10" height="10" fill="#1f6feb" rx="2"/>')
    out.append(f'<text x="{PAD_L + 152}" y="{ly}" font-size="10" fill="#1f6feb">'
               f'阶段2 填充（中位）</text>')

    out.append('</svg>')
    return '\n'.join(out)


def gen_chart(versions):
    """生成 SVG 折线图（阶段1 / 阶段2 覆盖率趋势）。"""
    W, H = 1100, 320
    PAD_L, PAD_R, PAD_T, PAD_B = 60, 130, 20, 46
    plot_w = W - PAD_L - PAD_R
    plot_h = H - PAD_T - PAD_B

    # 收集数据点（只取有值的）
    pts_s1, pts_s2 = [], []
    for i, v in enumerate(versions):
        m = v.get('metrics') or {}
        if m.get('stage1') is not None:
            pts_s1.append((i, m['stage1']))
        if m.get('fam_cov') is not None:
            pts_s2.append((i, m['fam_cov']))

    n = max(1, len(versions) - 1)

    def X(idx):
        return PAD_L + plot_w * idx / n

    def Y(val):
        return PAD_T + plot_h * (1 - val)

    def poly(pts, dash=''):
        if not pts:
            return ''
        d = ' '.join(f'{X(i):.1f},{Y(v):.1f}' for i, v in pts)
        dd = f' stroke-dasharray="{dash}"' if dash else ''
        return (f'<polyline points="{d}" fill="none" stroke-width="2.2"'
                f'{dd} stroke-linejoin="round"/>')

    out = [f'<svg viewBox="0 0 {W} {H}" style="width:100%;max-width:{W}px;'
           f'background:#fff;border:1px solid #eaeef2;border-radius:6px">']

    # Y 轴网格 + 标签（0% - 100%，每 20%）
    for pct in range(0, 101, 20):
        y = Y(pct / 100)
        out.append(f'<line x1="{PAD_L}" y1="{y:.1f}" x2="{PAD_L + plot_w}" '
                   f'y2="{y:.1f}" stroke="#eaeef2" stroke-width="1"/>')
        out.append(f'<text x="{PAD_L - 8}" y="{y + 4:.1f}" text-anchor="end" '
                   f'font-size="10" fill="#8c959f">{pct}%</text>')

    # X 轴标签
    for i, v in enumerate(versions):
        x = X(i)
        out.append(f'<text x="{x:.1f}" y="{H - PAD_B + 18}" text-anchor="middle" '
                   f'font-size="10" fill="#57606a">{v.get("ver", "")}</text>')
        if v.get('latest'):
            out.append(f'<circle cx="{x:.1f}" cy="{H - PAD_B + 30}" r="2.5" fill="#1f6feb"/>')

    # 折线（阶段1 实线绿，阶段2 虚线蓝）
    out.append(poly(pts_s1).replace('stroke-width',
                                    'stroke="#1a7f37" stroke-width', 1))
    out.append(poly(pts_s2, '6,4').replace('stroke-width',
                                           'stroke="#1f6feb" stroke-width', 1))

    # 数据点 + 数值标签
    for i, val in pts_s1:
        out.append(f'<circle cx="{X(i):.1f}" cy="{Y(val):.1f}" r="3.5" fill="#1a7f37"/>')
        out.append(f'<text x="{X(i):.1f}" y="{Y(val) - 9:.1f}" text-anchor="middle" '
                   f'font-size="9" fill="#1a7f37">{val * 100:.0f}</text>')
    for i, val in pts_s2:
        out.append(f'<circle cx="{X(i):.1f}" cy="{Y(val):.1f}" r="3.5" fill="#1f6feb"/>')
        out.append(f'<text x="{X(i):.1f}" y="{Y(val) + 15:.1f}" text-anchor="middle" '
                   f'font-size="9" fill="#1f6feb">{val * 100:.0f}</text>')

    # 图例
    lx = PAD_L + plot_w + 16
    out.append(f'<line x1="{lx}" y1="{PAD_T + 14}" x2="{lx + 22}" y2="{PAD_T + 14}" '
               f'stroke="#1a7f37" stroke-width="2.2"/>')
    out.append(f'<text x="{lx + 28}" y="{PAD_T + 18}" font-size="10" fill="#1a7f37">'
               f'阶段1 规划覆盖</text>')
    out.append(f'<line x1="{lx}" y1="{PAD_T + 40}" x2="{lx + 22}" y2="{PAD_T + 40}" '
               f'stroke="#1f6feb" stroke-width="2.2" stroke-dasharray="6,4"/>')
    out.append(f'<text x="{lx + 28}" y="{PAD_T + 44}" font-size="10" fill="#1f6feb">'
               f'阶段2 族覆盖</text>')

    # v6 口径切换标注
    for i, v in enumerate(versions):
        if v.get('ver') == 'v6':
            out.append(f'<line x1="{X(i):.1f}" y1="{PAD_T}" x2="{X(i):.1f}" '
                       f'y2="{PAD_T + plot_h}" stroke="#bf8700" stroke-width="1" '
                       f'stroke-dasharray="3,3"/>')
            out.append(f'<text x="{X(i) + 4:.1f}" y="{PAD_T + 12}" font-size="9" '
                       f'fill="#bf8700">v6 原记录 78%(可评估族口径)</text>')

    out.append('</svg>')
    return '\n'.join(out)


def load_data():
    if not DATA.exists():
        raise SystemExit(f'数据文件不存在: {DATA}')
    return json.loads(DATA.read_text(encoding='utf-8'))


def gen_html(data, out_path):
    versions = data.get('versions') or []
    bottlenecks = data.get('bottlenecks') or []
    checks = data.get('checks') or []
    meta = data.get('meta') or {}

    h = []
    h.append('''<!DOCTYPE html><html lang="zh"><head><meta charset="utf-8">
<title>''' + meta.get('title', 'MML 生成系统版本记录') + '''</title>
<style>
*{box-sizing:border-box}
body{font-family:-apple-system,"PingFang SC","Microsoft YaHei",sans-serif;
 margin:0;background:#f6f8fa;color:#1f2328;line-height:1.6}
.wrap{max-width:1240px;margin:0 auto;padding:24px}
h1{font-size:22px;margin:0 0 6px}
.sub{color:#656d76;font-size:13px;margin-bottom:20px}
.card{background:#fff;border:1px solid #d0d7de;border-radius:8px;
 padding:16px;margin-bottom:16px}
.card h2{font-size:15px;margin:0 0 12px;padding-bottom:8px;
 border-bottom:1px solid #eaeef2}
table{width:100%;border-collapse:collapse;font-size:12px}
th,td{padding:7px 9px;border-bottom:1px solid #eaeef2;text-align:left;
 vertical-align:top}
th{background:#f6f8fa;font-weight:600;color:#57606a;font-size:11px}
.ver{font-weight:700;color:#1f6feb;white-space:nowrap}
.tag{display:inline-block;padding:1px 7px;border-radius:10px;
 font-size:10px;margin-right:4px;white-space:nowrap}
.t-done{background:#dafbe1;color:#116329}
.t-todo{background:#fff8c5;color:#7d4e00}
.t-wait{background:#ddf4ff;color:#0969da}
.t-gray{background:#f6f8fa;color:#57606a}
ul{margin:4px 0;padding-left:18px}
li{font-size:12px;margin:2px 0}
.mono{font-family:ui-monospace,monospace;font-size:11px;
 background:#f6f8fa;padding:1px 4px;border-radius:3px}
.metric{font-family:ui-monospace,monospace;font-weight:600}
.good{color:#1a7f37}.bad{color:#cf222e}.warn{color:#bf8700}
.spark{display:inline-block;height:12px;border-radius:2px;
 background:#1f6feb;vertical-align:middle;margin-right:4px}
</style></head><body><div class="wrap">''')

    h.append(f'<h1>{meta.get("title", "MML 生成系统 · 版本修正历史")}</h1>')
    h.append(f'<div class="sub">共 {len(versions)} 个版本 · '
             f'判据 {len(checks)} 条 · '
             f'更新于 {datetime.now().strftime("%Y-%m-%d %H:%M")}</div>')

    # ── 一、指标趋势 ──
    h.append('<div class="card"><h2>一、指标趋势</h2>')
    h.append('<table><thead><tr>'
             '<th style="width:56px">版本</th><th style="width:88px">日期</th>'
             '<th>主要改动</th>'
             '<th class="right" style="width:104px">阶段1 规划覆盖</th>'
             '<th class="right" style="width:104px">阶段2 族覆盖</th>'
             '<th class="right" style="width:84px">命令数</th>'
             '</tr></thead><tbody>')
    for v in versions:
        m = v.get('metrics') or {}
        fc = m.get('fam_cov')
        s1 = m.get('stage1')
        cmds = m.get('cmds')
        h.append('<tr>')
        h.append(f'<td class="ver">{v.get("ver", "")}</td>')
        h.append(f'<td style="font-size:11px;color:#8c959f">{v.get("date", "")}</td>')
        title = v.get('title', '')
        if v.get('latest'):
            title += ' <span class="tag t-wait">当前</span>'
        h.append(f'<td>{title}</td>')
        if s1 is not None:
            h.append(f'<td class="right"><span class="metric">{s1 * 100:.1f}%</span></td>')
        else:
            h.append('<td class="right" style="color:#8c959f">—</td>')
        if fc is not None:
            cls = 'good' if fc >= 0.75 else ('warn' if fc >= 0.6 else 'bad')
            h.append(f'<td class="right"><span class="metric {cls}">{fc * 100:.1f}%</span></td>')
        else:
            h.append('<td class="right" style="color:#8c959f">—</td>')
        if isinstance(cmds, float):
            h.append(f'<td class="right"><span class="metric">{cmds * 100:.0f}%</span></td>')
        elif cmds:
            h.append(f'<td class="right"><span class="metric">{cmds}</span></td>')
        else:
            h.append('<td class="right" style="color:#8c959f">—</td>')
        h.append('</tr>')
    h.append('</tbody></table>')
    if meta.get('metrics_note'):
        h.append(f'<div style="font-size:11px;color:#8c959f;margin-top:8px">'
                 f'{meta["metrics_note"]}</div>')
    h.append('</div>')

    # ── 二、问题分类矩阵（机制进化 / Bug / 输入问题）──
    h.append('<div class="card"><h2>二、各版本修改了什么问题</h2>')
    h.append('<div style="font-size:12px;color:#57606a;margin-bottom:10px">'
             '把每个版本的改动按性质分类。<b>机制进化</b>=架构/流程/能力增强；'
             '<b>Bug</b>=代码缺陷（判据没生效、解析错、条件写错）；'
             '<b>输入问题</b>=数据和材料层面的发现（不是代码能修的）。</div>')
    h.append('<table><thead><tr>'
             '<th style="width:52px">版本</th>'
             '<th style="width:26%">机制进化</th>'
             '<th style="width:30%">Bug 修复</th>'
             '<th>输入问题发现</th>'
             '</tr></thead><tbody>')
    for v in versions:
        cats = v.get('categories') or {}
        mech = cats.get('mechanism') or []
        bugs = cats.get('bug') or []
        inp = cats.get('input') or []

        def cell(items, color):
            if not items:
                return '<span style="color:#c9d1d9">—</span>'
            return '<br>'.join(f'<span style="color:{color}">·</span> {x}' for x in items)

        h.append('<tr>')
        h.append(f'<td class="ver">{v.get("ver","")}<br>'
                 f'<span style="font-weight:400;color:#8c959f;font-size:10px">'
                 f'{v.get("date","")}</span></td>')
        h.append(f'<td style="font-size:11px">{cell(mech, "#1a7f37")}</td>')
        h.append(f'<td style="font-size:11px">{cell(bugs, "#cf222e")}</td>')
        h.append(f'<td style="font-size:11px">{cell(inp, "#0969da")}</td>')
        h.append('</tr>')
    h.append('</tbody></table>')

    # 统计
    n_mech = sum(len((v.get('categories') or {}).get('mechanism') or []) for v in versions)
    n_bug = sum(len((v.get('categories') or {}).get('bug') or []) for v in versions)
    n_inp = sum(len((v.get('categories') or {}).get('input') or []) for v in versions)
    h.append(f'<div style="font-size:11px;color:#57606a;margin-top:10px">'
             f'10 个版本累计：机制进化 <b>{n_mech}</b> 项、'
             f'Bug 修复 <b>{n_bug}</b> 项、输入问题发现 <b>{n_inp}</b> 项。'
             f'<br>注：Bug 占比高说明「能力」不是主要瓶颈 —— '
             f'很多指标上不去是因为判据没生效、解析写错、条件写错，'
             f'而不是模型配不出来。</div>')
    h.append('</div>')

    # ── 三、趋势曲线 ──
    h.append('<div class="card"><h2>三、迭代趋势</h2>')
    h.append(gen_chart(versions))
    h.append('<div style="font-size:11px;color:#8c959f;margin-top:8px">'
             '实线=阶段1 规划覆盖，虚线=阶段2 族覆盖（均为 GT 全部族口径）。'
             'v6 原记录 78.1% 是「可评估族」口径，本图已统一重算为 62.5%，'
             '所以 v6 看起来没有原记录那么高。'
             'v7 起的下滑主要是「过度配置被纠正」+ 口径统一，不是能力退化。</div>')
    h.append('</div>')

    # ── 四、性能收益 ──
    perf = data.get('performance') or {}
    if perf.get('comparison'):
        h.append('<div class="card"><h2>四、性能收益</h2>')
        h.append(f'<div style="font-size:12px;color:#57606a;margin-bottom:12px">'
                 f'{perf.get("summary","")}</div>')

        # 架构对比
        h.append('<table><thead><tr>'
                 '<th style="width:200px">架构</th>'
                 '<th class="right" style="width:56px">工单数</th>'
                 '<th class="right" style="width:96px">中位耗时</th>'
                 '<th class="right" style="width:96px">平均耗时</th>'
                 '<th>说明</th></tr></thead><tbody>')
        for c in perf['comparison']:
            h.append(f'<tr><td><b>{c.get("arch","")}</b></td>'
                     f'<td class="right">{c.get("n",0)}</td>'
                     f'<td class="right"><span class="metric">{c.get("median",0):.0f}s</span></td>'
                     f'<td class="right">{c.get("mean",0):.0f}s</td>'
                     f'<td style="font-size:11px">{c.get("note","")}</td></tr>')
        h.append('</tbody></table>')

        # 代价与收益
        dl = perf.get('delta') or {}
        if dl:
            h.append('<div style="margin-top:14px;padding:12px 14px;'
                     'background:#f6f9fb;border-left:3px solid #1f6feb;border-radius:4px">'
                     '<b>性能代价 vs 能力收益：</b>　'
                     f'耗时 <span class="metric warn">{dl.get("median","")}</span>（中位）'
                     f' / <span class="metric warn">{dl.get("mean","")}</span>（平均）　→　'
                     f'换来 <span class="metric good">{dl.get("benefit","")}</span>'
                     '</div>')

        # 迭代记录（简表）
        log = perf.get('iteration_log') or []
        if log:
            h.append('<div style="font-size:12px;font-weight:600;margin-top:16px">'
                     '性能相关的迭代记录：</div>')
            h.append('<table style="margin-top:6px"><thead><tr>'
                     '<th style="width:76px">版本</th>'
                     '<th style="width:78px">架构</th>'
                     '<th style="width:220px">性能变化</th>'
                     '<th>说明</th></tr></thead><tbody>')
            for lg in log:
                h.append(f'<tr><td class="ver">{lg.get("ver","")}</td>'
                         f'<td style="font-size:11px">{lg.get("arch","")}</td>'
                         f'<td style="font-size:11px">{lg.get("perf","")}</td>'
                         f'<td style="font-size:11px">{lg.get("note","")}</td></tr>')
            h.append('</tbody></table>')

        # 当前分档（简表）
        cur = perf.get('current') or {}
        if cur.get('by_scale'):
            h.append('<div style="font-size:12px;font-weight:600;margin-top:16px">'
                     '当前耗时分布（按工单规模）：</div>')
            h.append('<table style="margin-top:6px"><thead><tr>'
                     '<th style="width:140px">规模档位</th>'
                     '<th class="right" style="width:56px">单数</th>'
                     '<th class="right" style="width:90px">阶段1</th>'
                     '<th class="right" style="width:90px">阶段2</th>'
                     '<th class="right" style="width:90px">合计</th>'
                     '</tr></thead><tbody>')
            for sc in cur['by_scale']:
                h.append(f'<tr><td>{sc.get("level","")}</td>'
                         f'<td class="right">{sc.get("n",0)}</td>'
                         f'<td class="right"><span class="metric good">{sc.get("s1",0):.0f}s</span></td>'
                         f'<td class="right"><span class="metric" style="color:#1f6feb">{sc.get("s2",0):.0f}s</span></td>'
                         f'<td class="right"><span class="metric">{sc.get("total",0):.0f}s</span></td></tr>')
            h.append('</tbody></table>')
            if cur.get('note'):
                h.append(f'<div style="font-size:11px;color:#8c959f;margin-top:6px">'
                         f'{cur["note"]}</div>')

        # 结论
        if perf.get('key_finding'):
            h.append(f'<div style="margin-top:14px;font-size:12px;color:#0a5c8f;'
                     f'background:#eef7fc;padding:10px 12px;border-radius:4px">'
                     f'<b>结论：</b>{perf["key_finding"]}</div>')

        # 问题
        issues = perf.get('issues') or []
        if issues:
            h.append('<div style="font-size:12px;font-weight:600;margin-top:16px">'
                     '性能相关的问题与处理：</div>')
            h.append('<table style="margin-top:6px"><thead><tr>'
                     '<th style="width:230px">问题</th><th>处理</th>'
                     '<th style="width:280px">效果</th></tr></thead><tbody>')
            for it in issues:
                h.append(f'<tr><td>{it.get("issue","")}</td>'
                         f'<td style="font-size:11px">{it.get("fix","")}</td>'
                         f'<td style="font-size:11px;color:#1a7f37">{it.get("effect","")}</td></tr>')
            h.append('</tbody></table>')

        h.append('</div>')

    # ── 五、关键提升节点 ──
    hl = data.get('highlights') or {}
    if hl.get('items'):
        h.append('<div class="card"><h2>五、关键提升节点（哪些版本真的带来了提升）</h2>')
        h.append(f'<div style="font-size:12px;color:#57606a;margin-bottom:12px">'
                 f'{hl.get("summary", "")}</div>')

        h.append('<table><thead><tr>'
                 '<th style="width:48px">版本</th>'
                 '<th style="width:70px">提升幅度</th>'
                 '<th style="width:56px">性质</th>'
                 '<th style="width:180px">做了什么</th>'
                 '<th>为什么有效</th>'
                 '<th style="width:200px">实测证据</th>'
                 '<th style="width:90px">代价</th>'
                 '</tr></thead><tbody>')
        for it in hl['items']:
            h.append('<tr>')
            h.append(f'<td class="ver">{it.get("ver","")}</td>')
            h.append(f'<td><span class="metric good">{it.get("delta","")}</span></td>')
            h.append(f'<td><span class="tag t-done">{it.get("type","")}</span></td>')
            h.append(f'<td style="font-size:11px"><b>{it.get("title","")}</b></td>')
            h.append(f'<td style="font-size:11px">{it.get("why","")}</td>')
            h.append(f'<td style="font-size:11px;color:#1a7f37">{it.get("evidence","")}</td>')
            h.append(f'<td style="font-size:11px;color:#8c959f">{it.get("cost","")}</td>')
            h.append('</tr>')
        h.append('</tbody></table>')

        if hl.get('no_gain'):
            h.append('<div style="font-size:12px;margin-top:14px;font-weight:600">'
                     '其余版本的指标变化（基本没涨，或者只是没来得及重跑）：</div>')
            h.append('<table style="margin-top:6px"><thead><tr>'
                     '<th style="width:48px">版本</th>'
                     '<th style="width:70px">变化</th>'
                     '<th>说明</th></tr></thead><tbody>')
            for ng in hl['no_gain']:
                d = ng.get('delta', '')
                cls = 'bad' if d.startswith('-') else ('gray' if d == '0pp' else '')
                h.append(f'<tr><td class="ver">{ng.get("ver","")}</td>'
                         f'<td><span class="metric {cls}">{d}</span></td>'
                         f'<td style="font-size:11px">{ng.get("why","")}</td></tr>')
            h.append('</tbody></table>')

        h.append('<div style="font-size:11px;color:#8c959f;margin-top:10px">'
                 '<b>结论：</b>10 个版本里，真正拉指标的是 v3（+8.2pp）、v6（+11.4pp）、v7（+2.6pp）'
                 '三个机制性改动，合计 +22pp。剩下的版本主要是修 bug、补数据、加后端判据 —— '
                 '这些不直接涨指标，但是让「涨上去的能稳住」的前提。</div>')
        h.append('</div>')

    # ── 五、已发现未修正的问题 ──
    oi = data.get('open_issues') or []
    if oi:
        h.append('<div class="card"><h2>六、已发现但未修正的问题</h2>')
        h.append('<div style="font-size:12px;color:#57606a;margin-bottom:12px">'
                 '这些是已知问题，按优先级排列。用户明确说「暂不动」的会标注。</div>')
        h.append('<table><thead><tr>'
                 '<th style="width:40px">编号</th>'
                 '<th style="width:170px">问题</th>'
                 '<th style="width:120px">影响范围</th>'
                 '<th>为什么还没修</th>'
                 '<th style="width:190px">影响</th>'
                 '<th style="width:190px">修复路径</th>'
                 '<th style="width:44px">优先级</th>'
                 '</tr></thead><tbody>')
        for it in oi:
            pr = it.get('priority', '')
            pcls = 'bad' if pr == 'P0' else ('warn' if pr == 'P1' else 't-gray')
            h.append('<tr>')
            h.append(f'<td class="ver">{it.get("id","")}</td>')
            h.append(f'<td><b>{it.get("issue","")}</b></td>')
            h.append(f'<td style="font-size:11px">{it.get("scope","")}</td>')
            blocker = it.get('blocker') or ''
            blocker_html = ''
            if blocker and blocker != '无':
                blocker_html = ('<br><span style="color:#cf222e">阻塞：'
                                + blocker + '</span>')
            why = it.get('why_open', '')
            h.append(f'<td style="font-size:11px">{why}{blocker_html}</td>')
            h.append(f'<td style="font-size:11px">{it.get("impact","")}</td>')
            h.append(f'<td style="font-size:11px">{it.get("fix_path","")}</td>')
            h.append(f'<td><span class="tag {pcls}">{pr}</span></td>')
            h.append('</tr>')
        h.append('</tbody></table></div>')

    # ── 六、版本明细 ──
    h.append('<div class="card"><h2>七、版本明细</h2>')
    for v in reversed(versions):     # 最新的在前
        border = '#1f6feb' if v.get('latest') else '#d0d7de'
        h.append(f'<div style="border-left:3px solid {border};padding-left:12px;'
                 f'margin-bottom:18px">')
        latest = ' <span class="tag t-wait">当前版本</span>' if v.get('latest') else ''
        h.append(f'<div style="font-size:14px;font-weight:600">'
                 f'{v.get("ver", "")} · {v.get("title", "")}{latest}'
                 f'<span style="font-weight:400;color:#8c959f;font-size:12px">'
                 f'　{v.get("date", "")}'
                 f'　<span class="mono">{v.get("commit", "")}</span></span></div>')
        if v.get('changes'):
            h.append('<div style="font-size:12px;margin-top:6px"><b>改动：</b></div><ul>')
            for c in v['changes']:
                h.append(f'<li>{c}</li>')
            h.append('</ul>')
        if v.get('problems'):
            h.append('<div style="font-size:12px"><b>发现的问题 / 效果：</b></div><ul>')
            for p in v['problems']:
                h.append(f'<li>{p}</li>')
            h.append('</ul>')
        h.append('</div>')
    h.append('</div>')

    # ── 三、瓶颈 ──
    if bottlenecks:
        h.append('<div class="card"><h2>八、当前瓶颈与对策</h2>')
        h.append('<table><thead><tr>'
                 '<th style="width:150px">瓶颈</th>'
                 '<th class="right" style="width:56px">族数</th>'
                 '<th class="right" style="width:64px">工单数</th>'
                 '<th class="right" style="width:64px">命令数</th>'
                 '<th>根因</th><th>对策</th><th style="width:104px">状态</th>'
                 '</tr></thead><tbody>')
        for b in bottlenecks:
            status = b.get('status', '')
            cls = ('t-done' if '完成' in status else
                   't-todo' if '待办' in status else 't-wait')
            h.append('<tr>')
            h.append(f'<td><b>{b.get("name", "")}</b></td>')
            h.append(f'<td class="right">{b.get("n_fams") or "—"}</td>')
            h.append(f'<td class="right">{b.get("n_tickets") or "—"}</td>')
            h.append(f'<td class="right">{b.get("n_cmds") or "—"}</td>')
            h.append(f'<td style="font-size:11px">{b.get("why", "")}</td>')
            h.append(f'<td style="font-size:11px">{b.get("fix", "")}</td>')
            h.append(f'<td><span class="tag {cls}">{status}</span></td>')
            h.append('</tr>')
        h.append('</tbody></table></div>')

    # ── 四、判据清单 ──
    if checks:
        h.append('<div class="card"><h2>九、判据清单（prompt 要求的兜底）</h2>')
        h.append('<table><thead><tr>'
                 '<th style="width:52px">编号</th>'
                 '<th style="width:170px">检查什么</th>'
                 '<th style="width:72px">实现</th>'
                 '<th style="width:56px">级别</th>'
                 '<th style="width:76px">判别力</th>'
                 '<th>触发场景 / 实测反例（这条判据是怎么来的）</th>'
                 '</tr></thead><tbody>')
        for c in checks:
            lvl = c.get('level', '')
            power = c.get('power', '')
            cls = 't-wait' if '新增' in power else 't-done'
            lcls = 't-done' if lvl == 'fatal' else 't-todo'
            h.append(f'<tr><td class="ver">{c.get("code", "")}</td>'
                     f'<td>{c.get("what", "")}</td>'
                     f'<td style="font-size:11px">{c.get("how", "")}</td>'
                     f'<td><span class="tag {lcls}">{lvl}</span></td>'
                     f'<td><span class="tag {cls}">{power}</span></td>'
                     f'<td style="font-size:11px;color:#57606a">{c.get("why", "")}</td></tr>')
        h.append('</tbody></table>')
        h.append('<div style="font-size:11px;color:#8c959f;margin-top:10px">'
                 '<b>这些判据的共同来源：</b>每一条都是因为「prompt 写了但 agent 没照做」'
                 '或者「实测发现某类错误」才加的，不是凭空设计的。'
                 '加判据时都要先测判别力（构造正例 + 反例，确认它真的能区分）。'
                 '</div></div>')

    # ── 五、教训 ──
    if meta.get('lessons'):
        h.append('<div class="card"><h2>十、关键教训</h2><ul>')
        for l in meta['lessons']:
            h.append(f'<li>{l}</li>')
        h.append('</ul></div>')

    h.append('</div></body></html>')
    out_path.write_text('\n'.join(h), encoding='utf-8')
    print(f'✅ 已生成: {out_path}  ({out_path.stat().st_size // 1024}KB)')
    print(f'   版本 {len(versions)} / 瓶颈 {len(bottlenecks)} / 判据 {len(checks)}')


def add_version_draft():
    """从 git log 生成版本条目草稿，辅助手工补充。"""
    r = subprocess.run(['git', 'log', '--oneline', '-10'], cwd=PROJ,
                       capture_output=True, text=True)
    print('=== 最近 10 个提交 ===')
    print(r.stdout)
    print('\n=== 追加到 docs/version_history.json 的 versions 数组 ===')
    print('''{
  "ver": "v11",
  "date": "YYYY-MM-DD",
  "commit": "xxxxxxx",
  "title": "一句话标题",
  "changes": ["改动1", "改动2"],
  "metrics": {"stage1": null, "fam_cov": null, "cmds": null, "n": 87},
  "problems": ["发现的问题 / 实测效果"]
}''')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('-o', '--out', default=str(DEFAULT_OUT))
    ap.add_argument('--add-version', action='store_true',
                    help='显示如何新增版本条目')
    args = ap.parse_args()

    if args.add_version:
        add_version_draft()
        return

    data = load_data()
    gen_html(data, Path(args.out))


if __name__ == '__main__':
    main()

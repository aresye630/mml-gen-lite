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

    # ── 二、版本明细 ──
    h.append('<div class="card"><h2>二、版本明细</h2>')
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
        h.append('<div class="card"><h2>三、当前瓶颈与对策</h2>')
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
        h.append('<div class="card"><h2>四、判据清单（prompt 要求的兜底）</h2>')
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
        h.append('<div class="card"><h2>五、关键教训</h2><ul>')
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

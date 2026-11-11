#!/usr/bin/env python3
"""三版意图对比：原始工单 → 当前版（逐条列）→ 修改后（参照存量）。

用户要求（2026-11-11）：
  「保留现在的写法，让我对比初始意图，现在的版本以及修改后的版本」
"""
import argparse
import html as H
import json
import re
from collections import Counter
from pathlib import Path

GT = json.loads(Path('/tmp/gt_cleaned.json').read_text(encoding='utf-8'))

V1_DIR = Path('/Users/alesc/workspace/gt-rewrite-samples/86个意图_v5')   # 原始工单意图
V2_DIR = Path('/tmp/intent_dataset')                                     # 当前版（逐条列）
V3_DIR = Path('/tmp/intent_v3')                                          # 修改后（参照存量）
OUT = Path('/tmp/intent_compare_3way.html')

VERB_CN = {'ADD': '新增', 'MOD': '调整', 'RMV': '删除', 'SET': '设置'}


def read(p):
    return p.read_text(encoding='utf-8', errors='replace') if p.exists() else ''


def count_verbs(text):
    c = Counter()
    for m in re.finditer(r'^-\s*(新增|添加|增加|新建)', text, re.M):
        c['ADD'] += 1
    for m in re.finditer(r'^-\s*(删除|移除|去除)', text, re.M):
        c['RMV'] += 1
    for m in re.finditer(r'^-\s*(调整|修改)', text, re.M):
        c['MOD'] += 1
    for m in re.finditer(r'^-\s*(设置|刷新)', text, re.M):
        c['SET'] += 1
    return c


def n_items(text):
    return len(re.findall(r'^- ', text, re.M))


def build():
    rows = []
    for g in GT:
        tk = g['ticket']
        if not g['kept']:
            continue
        v1 = read(V1_DIR / f'{tk}_意图.md')
        v2 = read(V2_DIR / f'{tk}_意图.md')
        v3 = read(V3_DIR / f'{tk}_意图.md')
        if not v2 and not v3:
            continue

        gt_verbs = Counter(v for _, v, _, _, _ in g['kept'])
        rows.append({
            'tk': tk,
            'n_gt': len(g['kept']),
            'n_fams': len({f for _, _, f, _, _ in g['kept']}),
            'gt_verbs': dict(gt_verbs),
            'v1': v1, 'v2': v2, 'v3': v3,
            'v1_n': n_items(v1), 'v2_n': n_items(v2), 'v3_n': n_items(v3),
            'v1_verbs': dict(count_verbs(v1)),
            'v2_verbs': dict(count_verbs(v2)),
            'v3_verbs': dict(count_verbs(v3)),
            'v3_ref': '存量做法' in v3,   # 是否用了参照存量写法
            # 原始意图是否缺删除（GT 有 RMV 但 v1 没有删除条目）
            'v1_miss_rmv': (gt_verbs.get('RMV', 0) > 0
                            and count_verbs(v1).get('RMV', 0) == 0),
        })
    rows.sort(key=lambda r: (-int(r['v1_miss_rmv']), -int(r['v3_ref']), -r['n_gt']))
    return rows


CSS = """
*{box-sizing:border-box}
body{margin:0;padding:18px;font:13px/1.55 -apple-system,BlinkMacSystemFont,
  "PingFang SC","Microsoft YaHei",sans-serif;color:#1f2328;background:#f6f8fa}
h1{font-size:19px;margin:0 0 5px}
.sub{font-size:12px;color:#57606a;margin-bottom:14px}
.bar{background:#fff;border:1px solid #d0d7de;border-radius:6px;padding:11px 14px;
  margin-bottom:12px;position:sticky;top:0;z-index:20;box-shadow:0 2px 8px rgba(0,0,0,.06)}
.bar input{padding:6px 10px;border:1px solid #d0d7de;border-radius:5px;font-size:13px;width:220px}
.bar label{margin-left:13px;cursor:pointer;user-select:none;font-size:12px}
.bar button{margin-left:9px;padding:6px 11px;border:1px solid #d0d7de;
  background:#f6f8fa;border-radius:5px;cursor:pointer;font-size:12px}
.bar button:hover{background:#eaeef2}
.stat{display:inline-block;margin-left:15px;font-size:12px;color:#57606a}
.stat b{color:#0969da}
table{width:100%;border-collapse:collapse;background:#fff;border:1px solid #d0d7de;
  border-radius:6px;overflow:hidden;table-layout:fixed}
thead th{background:#f6f8fa;padding:9px 9px;text-align:left;font-size:12px;
  font-weight:600;border-bottom:1px solid #d0d7de;position:sticky;top:66px;z-index:10}
tbody tr{border-bottom:1px solid #eaeef2}
tbody tr:hover{background:#f6f8fa}
td{padding:8px 9px;vertical-align:top;font-size:12px}
td.tk{font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:11.5px}
td.num{text-align:right;font-family:ui-monospace,monospace}
.verbs{font-family:ui-monospace,monospace;font-size:11px;line-height:1.7}
.v-a{color:#1a7f37;font-weight:600}
.v-r{color:#cf222e;font-weight:600}
.v-m{color:#bf8700}
.v-s{color:#0969da}
.miss{background:#fff5f5}
pre{white-space:pre-wrap;word-break:break-word;margin:0;font:11px/1.45
  ui-monospace,SFMono-Regular,Menlo,monospace;color:#24292f;
  max-height:300px;overflow:auto;background:#fbfcfd;padding:7px;border-radius:4px;
  border:1px solid #eaeef2}
.tag{display:inline-block;padding:1px 5px;border-radius:9px;font-size:9.5px;
  font-weight:600;margin-left:4px;vertical-align:middle}
.t-bad{background:#ffe0e0;color:#cf222e}
.t-good{background:#e6f7ef;color:#1a7f37}
.t-ref{background:#e7f0ff;color:#0969da}
.hide{display:none}
.cnt{font-size:10px;color:#8c959f;margin-top:3px}
"""

JS = """
const q=document.getElementById('q');
const onlyMiss=document.getElementById('onlyMiss');
const onlyRef=document.getElementById('onlyRef');
const rows=[...document.querySelectorAll('tr[data-tk]')];
function apply(){
  const s=q.value.trim().toLowerCase();
  const m=onlyMiss.checked, f=onlyRef.checked;
  rows.forEach(r=>{
    const a=!s||r.dataset.tk.toLowerCase().includes(s);
    const b=!m||r.dataset.miss==='1';
    const c=!f||r.dataset.ref==='1';
    r.classList.toggle('hide',!(a&&b&&c));
  });
  document.getElementById('shown').textContent=
    rows.filter(r=>!r.classList.contains('hide')).length;
}
q.addEventListener('input',apply);
onlyMiss.addEventListener('change',apply);
onlyRef.addEventListener('change',apply);
document.getElementById('expand').onclick=()=>{
  document.querySelectorAll('pre').forEach(p=>{
    p.style.maxHeight=p.style.maxHeight==='none'?'300px':'none';
  });
};
apply();
"""


def esc(s):
    return H.escape(s)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--ticket', default='')
    args = ap.parse_args()

    rows = build()
    if args.ticket:
        rows = [r for r in rows if r['tk'] == args.ticket]

    n = len(rows)
    n_ref = sum(1 for r in rows if r['v3_ref'])
    n_v1_miss = sum(1 for r in rows if r['v1_miss_rmv'])
    avg_v1 = sum(r['v1_n'] for r in rows) / max(1, n)
    avg_v2 = sum(r['v2_n'] for r in rows) / max(1, n)
    avg_v3 = sum(r['v3_n'] for r in rows) / max(1, n)

    parts = [
        '<!DOCTYPE html><html lang="zh-CN"><head><meta charset="utf-8">',
        '<title>意图三版对比</title>',
        f'<style>{CSS}</style></head><body>',
        '<h1>意图三版对比：原始工单 → 当前版 → 参照存量版</h1>',
        f'<div class="sub">{n} 个工单 · '
        f'左 = 原始工单意图（客户写的）· '
        f'中 = 当前版（GT 反推，逐条列）· '
        f'右 = 参照存量版（同类对象照 EXP 存量配齐）</div>',
        '<div class="bar">',
        '<input id="q" placeholder="搜工单号...">',
        '<label><input type="checkbox" id="onlyMiss"> 原始意图缺删除</label>',
        '<label><input type="checkbox" id="onlyRef"> 用了参照存量</label>',
        '<button id="expand">展开/收起全文</button>',
        f'<span class="stat">参照存量 <b>{n_ref}</b> 单</span>',
        f'<span class="stat">原始缺删除 <b style="color:#cf222e">{n_v1_miss}</b> 单</span>',
        f'<span class="stat">条目数 平均 '
        f'<b>{avg_v1:.0f}</b> → <b>{avg_v2:.0f}</b> → <b>{avg_v3:.0f}</b></span>',
        f'<span class="stat">显示 <b id="shown">{n}</b> 单</span>',
        '</div>',
        '<table><thead><tr>',
        '<th style="width:126px">工单</th>',
        '<th style="width:52px">GT条</th>',
        '<th style="width:44px">族</th>',
        '<th style="width:112px">GT 动词</th>',
        '<th style="width:78px">原始</th>',
        '<th style="width:78px">当前版</th>',
        '<th style="width:78px">参照版</th>',
        '<th>① 原始工单意图</th>',
        '<th>② 当前版（逐条列）</th>',
        '<th>③ 参照存量版</th>',
        '</tr></thead><tbody>',
    ]

    def fmt_verbs(v):
        if not v:
            return '<span style="color:#c9d1d9">—</span>'
        out = []
        for k in ('ADD', 'MOD', 'RMV', 'SET'):
            if v.get(k):
                cls = {'ADD': 'v-a', 'MOD': 'v-m', 'RMV': 'v-r', 'SET': 'v-s'}[k]
                out.append(f'<span class="{cls}">{VERB_CN[k]}{v[k]}</span>')
        return ' '.join(out)

    for r in rows:
        badges = ''
        if r['v1_miss_rmv']:
            badges += '<span class="tag t-bad">原始缺删除</span>'
        if r['v3_ref']:
            badges += '<span class="tag t-ref">参照</span>'

        tr_cls = 'miss' if r['v1_miss_rmv'] else ''
        parts.append(
            f'<tr class="{tr_cls}" data-tk="{esc(r["tk"])}" '
            f'data-miss="{1 if r["v1_miss_rmv"] else 0}" '
            f'data-ref="{1 if r["v3_ref"] else 0}">'
            f'<td class="tk">{esc(r["tk"])}{badges}</td>'
            f'<td class="num">{r["n_gt"]}</td>'
            f'<td class="num">{r["n_fams"]}</td>'
            f'<td class="verbs">{fmt_verbs(r["gt_verbs"])}</td>'
            f'<td class="verbs">{fmt_verbs(r["v1_verbs"])}'
            f'<div class="cnt">{r["v1_n"]} 条</div></td>'
            f'<td class="verbs">{fmt_verbs(r["v2_verbs"])}'
            f'<div class="cnt">{r["v2_n"]} 条</div></td>'
            f'<td class="verbs">{fmt_verbs(r["v3_verbs"])}'
            f'<div class="cnt">{r["v3_n"]} 条</div></td>'
            f'<td><pre>{esc(r["v1"][:5000])}</pre></td>'
            f'<td><pre>{esc(r["v2"][:5000])}</pre></td>'
            f'<td><pre>{esc(r["v3"][:5000])}</pre></td>'
            f'</tr>')

    parts.append('</tbody></table>')
    parts.append(f'<script>{JS}</script></body></html>')

    OUT.write_text('\n'.join(parts), encoding='utf-8')
    print(f'✅ {OUT}  ({OUT.stat().st_size // 1024}KB，{n} 工单)')
    print(f'   参照存量: {n_ref} 单')
    print(f'   原始缺删除: {n_v1_miss} 单')
    print(f'   平均条目数: {avg_v1:.0f} → {avg_v2:.0f} → {avg_v3:.0f}')


if __name__ == '__main__':
    main()

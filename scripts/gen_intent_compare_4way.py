#!/usr/bin/env python3
"""四版意图对比：V1 原始 / V2 逐条列 / V3 参照存量 / V4 极致压缩。

用户要求（2026-11-11）：
  「再建立一个简化描述的版本，作为V4（V1 原始，V2 GT反推，
    V3 参照EXP改写 V4 极致压缩文本）四个版本都保留」
"""
import argparse
import html as H
import json
import re
from collections import Counter
from pathlib import Path

GT = json.loads(Path('/tmp/gt_cleaned.json').read_text(encoding='utf-8'))

V1 = Path('/Users/alesc/workspace/gt-rewrite-samples/86个意图_v5')
V2 = Path('/tmp/intent_dataset')
V3 = Path('/tmp/intent_v3')
V4 = Path('/tmp/intent_v4')
OUT = Path('/tmp/intent_compare_4way.html')

VERB_CN = {'ADD': '新增', 'MOD': '调整', 'RMV': '删除', 'SET': '设置'}


def read(p):
    return p.read_text(encoding='utf-8', errors='replace') if p.exists() else ''


def count_verbs(text):
    """统计意图里的动词。

    ★ 2026-11-11：两种格式都要支持
      A. 条目行带动词： 「- 删除 APN配置」
      B. 章节标题带动词：「【删除】」+ 下面的条目（原始工单意图的写法）

    统计口径：只数「条目」（- 开头的行），
      章节标题只决定当前分节的动作，不单独计数。
    """
    c = Counter()
    cur_sec = None          # 当前分节的默认动作
    for line in text.split('\n'):
        s = line.strip()
        if not s or s.startswith('#') or s.startswith('|'):
            continue

        # 章节标题：【删除】/【新增/修改】
        m = re.match(r'^【([^】]+)】$', s)
        if m:
            sec = m.group(1)
            if '删除' in sec:
                cur_sec = 'RMV'
            elif '新增' in sec or '添加' in sec:
                cur_sec = 'ADD'
            elif '修改' in sec or '调整' in sec:
                cur_sec = 'MOD'
            elif '设置' in sec:
                cur_sec = 'SET'
            else:
                cur_sec = None
            continue

        # 只统计条目行
        if not s.startswith('- '):
            continue

        body = s[2:]
        hit = False
        for key, words in (('ADD', ('新增', '添加', '增加', '新建')),
                           ('RMV', ('删除', '移除', '去除')),
                           ('MOD', ('调整', '修改')),
                           ('SET', ('设置', '刷新'))):
            if any(w in body for w in words):
                c[key] += 1
                hit = True
                break
        if not hit and cur_sec:
            # 条目本身没写动词，用所在分节的动作
            c[cur_sec] += 1

    return c


def n_lines(text):
    return len([l for l in text.split('\n') if l.strip()])


def build():
    rows = []
    for g in GT:
        tk = g['ticket']
        if not g['kept']:
            continue
        v1 = read(V1 / f'{tk}_意图.md')
        v2 = read(V2 / f'{tk}_意图.md')
        v3 = read(V3 / f'{tk}_意图.md')
        v4 = read(V4 / f'{tk}_意图.md')
        if not v2:
            continue

        gt_verbs = Counter(v for _, v, _, _, _ in g['kept'])
        rows.append({
            'tk': tk, 'n_gt': len(g['kept']),
            'n_fams': len({f for _, _, f, _, _ in g['kept']}),
            'gt_verbs': dict(gt_verbs),
            'v1': v1, 'v2': v2, 'v3': v3, 'v4': v4,
            'chars': {'v1': len(v1), 'v2': len(v2), 'v3': len(v3), 'v4': len(v4)},
            'lines': {'v1': n_lines(v1), 'v2': n_lines(v2),
                      'v3': n_lines(v3), 'v4': n_lines(v4)},
            'v4_verbs': dict(count_verbs(v4)),
            'v3_ref': '存量做法' in v3,
            'v1_miss_rmv': (gt_verbs.get('RMV', 0) > 0
                            and count_verbs(v1).get('RMV', 0) == 0),
        })
    rows.sort(key=lambda r: (-int(r['v1_miss_rmv']), -int(r['v3_ref']), -r['n_gt']))
    return rows


CSS = """
*{box-sizing:border-box}
body{margin:0;padding:16px;font:13px/1.55 -apple-system,BlinkMacSystemFont,
  "PingFang SC","Microsoft YaHei",sans-serif;color:#1f2328;background:#f6f8fa}
h1{font-size:19px;margin:0 0 5px}
.sub{font-size:12px;color:#57606a;margin-bottom:12px}
.bar{background:#fff;border:1px solid #d0d7de;border-radius:6px;padding:10px 13px;
  margin-bottom:11px;position:sticky;top:0;z-index:30;box-shadow:0 2px 8px rgba(0,0,0,.06)}
.bar input[type=text]{padding:6px 10px;border:1px solid #d0d7de;border-radius:5px;
  font-size:13px;width:200px}
.bar label{margin-left:12px;cursor:pointer;user-select:none;font-size:12px}
.bar button{margin-left:8px;padding:6px 11px;border:1px solid #d0d7de;
  background:#f6f8fa;border-radius:5px;cursor:pointer;font-size:12px}
.bar button:hover{background:#eaeef2}
.stat{display:inline-block;margin-left:14px;font-size:12px;color:#57606a}
.stat b{color:#0969da}
table{width:100%;border-collapse:collapse;background:#fff;border:1px solid #d0d7de;
  border-radius:6px;overflow:hidden;table-layout:fixed}
thead th{background:#f6f8fa;padding:8px;text-align:left;font-size:12px;
  font-weight:600;border-bottom:1px solid #d0d7de;position:sticky;top:62px;z-index:10}
thead th.v1{background:#fdf6f6}
thead th.v2{background:#f6f9fb}
thead th.v3{background:#f2f8fd}
thead th.v4{background:#f2fbf6}
tbody tr{border-bottom:1px solid #eaeef2}
tbody tr:hover{background:#f6f8fa}
td{padding:7px 8px;vertical-align:top;font-size:12px}
td.tk{font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:11px}
td.num{text-align:right;font-family:ui-monospace,monospace}
td.chars{text-align:right;font-family:ui-monospace,monospace;font-size:10.5px;color:#57606a}
.verbs{font-family:ui-monospace,monospace;font-size:10.5px;line-height:1.65}
.v-a{color:#1a7f37;font-weight:600}
.v-r{color:#cf222e;font-weight:600}
.v-m{color:#bf8700}
.v-s{color:#0969da}
.miss{background:#fff5f5}
pre{white-space:pre-wrap;word-break:break-word;margin:0;font:10.5px/1.45
  ui-monospace,SFMono-Regular,Menlo,monospace;color:#24292f;
  max-height:260px;overflow:auto;background:#fbfcfd;padding:6px;border-radius:4px;
  border:1px solid #eaeef2}
pre.flow{font-family:inherit;font-size:11.5px;line-height:1.7;background:#f7fdfa;
  border-color:#d3f0e0}
.tag{display:inline-block;padding:1px 5px;border-radius:9px;font-size:9px;
  font-weight:600;margin-left:3px}
.t-bad{background:#ffe0e0;color:#cf222e}
.t-ref{background:#e7f0ff;color:#0969da}
.t-tiny{background:#e6f7ef;color:#1a7f37}
.hide{display:none}
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
    p.style.maxHeight=p.style.maxHeight==='none'?'260px':'none';
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

    n = max(1, len(rows))
    c1 = sum(r['chars']['v1'] for r in rows) / n
    c2 = sum(r['chars']['v2'] for r in rows) / n
    c3 = sum(r['chars']['v3'] for r in rows) / n
    c4 = sum(r['chars']['v4'] for r in rows) / n
    n_ref = sum(1 for r in rows if r['v3_ref'])
    n_miss = sum(1 for r in rows if r['v1_miss_rmv'])

    parts = [
        '<!DOCTYPE html><html lang="zh-CN"><head><meta charset="utf-8">',
        '<title>意图四版对比</title>',
        f'<style>{CSS}</style></head><body>',
        '<h1>意图四版对比</h1>',
        '<div class="sub">'
        'V1 原始工单意图（客户写的）· '
        'V2 GT 反推（逐条列）· '
        'V3 参照 EXP 改写 · '
        'V4 极致压缩（备忘录式流水句）</div>',
        '<div class="bar">',
        '<input type="text" id="q" placeholder="搜工单号...">',
        '<label><input type="checkbox" id="onlyMiss"> 原始缺删除</label>',
        '<label><input type="checkbox" id="onlyRef"> 用了参照存量</label>',
        '<button id="expand">展开/收起</button>',
        f'<span class="stat">参照存量 <b>{n_ref}</b> 单</span>',
        f'<span class="stat">原始缺删除 <b style="color:#cf222e">{n_miss}</b> 单</span>',
        f'<span class="stat">平均字数 '
        f'<b>{c1:.0f}</b> → <b>{c2:.0f}</b> → <b>{c3:.0f}</b> → '
        f'<b style="color:#1a7f37">{c4:.0f}</b></span>',
        f'<span class="stat">显示 <b id="shown">{len(rows)}</b> 单</span>',
        '</div>',
        '<table><thead><tr>',
        '<th style="width:118px">工单</th>',
        '<th style="width:46px">GT</th>',
        '<th style="width:38px">族</th>',
        '<th style="width:96px">GT 动词</th>',
        '<th style="width:52px">V1字</th>',
        '<th style="width:52px">V2字</th>',
        '<th style="width:52px">V3字</th>',
        '<th style="width:52px">V4字</th>',
        '<th class="v1">V1 原始工单意图</th>',
        '<th class="v2">V2 GT 反推（逐条）</th>',
        '<th class="v3">V3 参照存量</th>',
        '<th class="v4">V4 极致压缩</th>',
        '</tr></thead><tbody>',
    ]

    def fmt(v):
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
            badges += '<span class="tag t-bad">缺删</span>'
        if r['v3_ref']:
            badges += '<span class="tag t-ref">参照</span>'
        if r['chars']['v4'] and r['chars']['v2']:
            ratio = r['chars']['v4'] / r['chars']['v2']
            if ratio < 0.4:
                badges += '<span class="tag t-tiny">压缩</span>'

        parts.append(
            f'<tr class="{"miss" if r["v1_miss_rmv"] else ""}" '
            f'data-tk="{esc(r["tk"])}" '
            f'data-miss="{1 if r["v1_miss_rmv"] else 0}" '
            f'data-ref="{1 if r["v3_ref"] else 0}">'
            f'<td class="tk">{esc(r["tk"])}{badges}</td>'
            f'<td class="num">{r["n_gt"]}</td>'
            f'<td class="num">{r["n_fams"]}</td>'
            f'<td class="verbs">{fmt(r["gt_verbs"])}</td>'
            f'<td class="chars">{r["chars"]["v1"]}</td>'
            f'<td class="chars">{r["chars"]["v2"]}</td>'
            f'<td class="chars">{r["chars"]["v3"]}</td>'
            f'<td class="chars"><b style="color:#1a7f37">{r["chars"]["v4"]}</b></td>'
            f'<td><pre>{esc(r["v1"][:4000])}</pre></td>'
            f'<td><pre>{esc(r["v2"][:4000])}</pre></td>'
            f'<td><pre>{esc(r["v3"][:4000])}</pre></td>'
            f'<td><pre class="flow">{esc(r["v4"][:4000])}</pre></td>'
            f'</tr>')

    parts.append('</tbody></table>')
    parts.append(f'<script>{JS}</script></body></html>')

    OUT.write_text('\n'.join(parts), encoding='utf-8')
    print(f'✅ {OUT}  ({OUT.stat().st_size // 1024}KB，{len(rows)} 工单)')
    print(f'   平均字数: V1 {c1:.0f} / V2 {c2:.0f} / V3 {c3:.0f} / V4 {c4:.0f}')
    print(f'   参照存量: {n_ref} 单 / 原始缺删除: {n_miss} 单')


if __name__ == '__main__':
    main()

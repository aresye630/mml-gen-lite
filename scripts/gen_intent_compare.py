#!/usr/bin/env python3
"""生成全量意图对比（原始意图 vs 修正后意图 vs GT 动词分布）。

三列并排，供人工审视：
  左：原始工单意图（/Users/alesc/workspace/gt-rewrite-samples/86个意图_v5）
  中：本次修正后的意图（/tmp/intent_dataset，GT 反推）
  右：GT 实际动词分布（命令级，验证意图是否完整）

用法：
  python3 scripts/gen_intent_compare.py                    # 生成 HTML
  python3 scripts/gen_intent_compare.py --ticket XXX       # 只看单工单
"""
import argparse
import html as H
import json
import re
from collections import Counter
from pathlib import Path

BASE = Path('/Users/alesc/workspace/mml-gen-lite')
GT = json.loads(Path('/tmp/gt_cleaned.json').read_text(encoding='utf-8'))
GT_MAP = {g['ticket']: g for g in GT}

ORIG_DIR = Path('/Users/alesc/workspace/gt-rewrite-samples/86个意图_v5')
NEW_DIR = Path('/tmp/intent_dataset')
OUT = Path('/tmp/intent_compare.html')

VERB_CN = {'ADD': '新增', 'MOD': '调整', 'RMV': '删除', 'SET': '设置'}


def count_verbs(text):
    """统计意图里各动词的条目数。"""
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


def build():
    rows = []
    for g in GT:
        tk = g['ticket']
        if not g['kept']:
            continue

        gt_verbs = Counter(v for _, v, _, _, _ in g['kept'])
        gt_fams = len({f for _, _, f, _, _ in g['kept']})

        op = ORIG_DIR / f'{tk}_意图.md'
        np_ = NEW_DIR / f'{tk}_意图.md'
        orig = op.read_text(encoding='utf-8', errors='replace') if op.exists() else ''
        new = np_.read_text(encoding='utf-8', errors='replace') if np_.exists() else ''

        ov = count_verbs(orig)
        nv = count_verbs(new)

        # 数据清单
        ds = NEW_DIR / f'{tk}_数据清单.md'
        n_sheets = 0
        if ds.exists():
            n_sheets = len(re.findall(r'^## ', ds.read_text(encoding='utf-8'), re.M))

        rows.append({
            'tk': tk,
            'n_gt': len(g['kept']),
            'n_fams': gt_fams,
            'gt_verbs': {k: v for k, v in gt_verbs.items()},
            'orig': orig, 'new': new,
            'orig_verbs': {k: v for k, v in ov.items()},
            'new_verbs': {k: v for k, v in nv.items()},
            'n_sheets': n_sheets,
            # 修正后的意图是否覆盖了 GT 的全部动词方向
            'miss_rmv': gt_verbs.get('RMV', 0) > 0 and nv.get('RMV', 0) == 0,
            'orig_miss_rmv': gt_verbs.get('RMV', 0) > 0 and ov.get('RMV', 0) == 0,
        })
    return rows


CSS = """
*{box-sizing:border-box}
body{margin:0;padding:20px;font:13px/1.55 -apple-system,BlinkMacSystemFont,
  "PingFang SC","Microsoft YaHei",sans-serif;color:#1f2328;background:#f6f8fa}
h1{font-size:19px;margin:0 0 6px}
.sub{font-size:12px;color:#57606a;margin-bottom:16px}
.bar{background:#fff;border:1px solid #d0d7de;border-radius:6px;padding:12px 14px;
  margin-bottom:14px;position:sticky;top:0;z-index:10;box-shadow:0 2px 8px rgba(0,0,0,.06)}
.bar input{padding:6px 10px;border:1px solid #d0d7de;border-radius:5px;font-size:13px;width:240px}
.bar label{margin-left:14px;cursor:pointer;user-select:none}
.bar button{margin-left:10px;padding:6px 12px;border:1px solid #d0d7de;
  background:#f6f8fa;border-radius:5px;cursor:pointer;font-size:12px}
.bar button:hover{background:#eaeef2}
.stat{display:inline-block;margin-left:18px;font-size:12px;color:#57606a}
.stat b{color:#0969da}
table{width:100%;border-collapse:collapse;background:#fff;border:1px solid #d0d7de;
  border-radius:6px;overflow:hidden}
thead th{background:#f6f8fa;padding:9px 10px;text-align:left;font-size:12px;
  font-weight:600;border-bottom:1px solid #d0d7de;position:sticky;top:70px;z-index:5}
tbody tr{border-bottom:1px solid #eaeef2}
tbody tr:hover{background:#f6f8fa}
td{padding:9px 10px;vertical-align:top;font-size:12px}
td.tk{font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:11.5px;
  white-space:nowrap;width:132px}
td.num{text-align:right;font-family:ui-monospace,monospace;width:56px}
.verbs{font-family:ui-monospace,monospace;font-size:11px;line-height:1.7}
.v-a{color:#1a7f37;font-weight:600}
.v-r{color:#cf222e;font-weight:600}
.v-m{color:#bf8700}
.v-s{color:#0969da}
.miss{background:#fff5f5}
.ok{color:#1a7f37}
.warn{color:#cf222e;font-weight:600}
pre{white-space:pre-wrap;word-break:break-word;margin:0;font:11.5px/1.5
  ui-monospace,SFMono-Regular,Menlo,monospace;color:#24292f;
  max-height:280px;overflow:auto;background:#fbfcfd;padding:8px;border-radius:4px}
.tag{display:inline-block;padding:1px 6px;border-radius:10px;font-size:10px;
  font-weight:600;margin-left:4px}
.t-bad{background:#ffe0e0;color:#cf222e}
.t-good{background:#e6f7ef;color:#1a7f37}
.t-info{background:#e7f0ff;color:#0969da}
.hide{display:none}
"""

JS = """
const q=document.getElementById('q');
const onlyMiss=document.getElementById('onlyMiss');
const rows=[...document.querySelectorAll('tr[data-tk]')];
function apply(){
  const s=q.value.trim().toLowerCase();
  const m=onlyMiss.checked;
  rows.forEach(r=>{
    const tkOk=!s||r.dataset.tk.toLowerCase().includes(s);
    const missOk=!m||r.dataset.miss==='1';
    r.classList.toggle('hide',!(tkOk&&missOk));
  });
  const vis=rows.filter(r=>!r.classList.contains('hide')).length;
  document.getElementById('shown').textContent=vis;
}
q.addEventListener('input',apply);
onlyMiss.addEventListener('change',apply);
document.getElementById('expand').onclick=()=>{
  const pre=document.querySelectorAll('pre');
  pre.forEach(p=>p.style.maxHeight=p.style.maxHeight==='none'?'280px':'none');
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

    rows.sort(key=lambda r: (-int(r['orig_miss_rmv']), -r['n_gt']))

    n_orig_miss = sum(1 for r in rows if r['orig_miss_rmv'])
    n_new_miss = sum(1 for r in rows if r['miss_rmv'])
    n_total = len(rows)

    parts = [f'<!DOCTYPE html><html lang="zh-CN"><head><meta charset="utf-8">',
             f'<title>意图对比：修正后 vs 原始</title><style>{CSS}</style></head><body>',
             '<h1>意图对比：修正后 vs 原始</h1>',
             f'<div class="sub">{n_total} 个工单 · '
             f'左列原始工单意图 / 中列本次修正后的意图（GT 反推）/ 右列 GT 实际动词分布</div>',
             '<div class="bar">',
             '<input id="q" placeholder="搜工单号...">',
             '<label><input type="checkbox" id="onlyMiss"> 只看原始意图缺删除的</label>',
             '<button id="expand">展开/收起全文</button>',
             f'<span class="stat">原始意图缺删除 <b class="warn">{n_orig_miss}</b> 单</span>',
             f'<span class="stat">修正后仍缺 <b class="ok">{n_new_miss}</b> 单</span>',
             f'<span class="stat">显示 <b id="shown">{n_total}</b> 单</span>',
             '</div>',
             '<table><thead><tr>',
             '<th style="width:132px">工单</th>',
             '<th style="width:60px">GT条</th>',
             '<th style="width:52px">族</th>',
             '<th style="width:140px">GT 动词分布</th>',
             '<th style="width:120px">原始意图动词</th>',
             '<th style="width:120px">修正意图动词</th>',
             '<th style="width:52px">清单表</th>',
             '<th>原始工单意图</th>',
             '<th>本次修正后的意图</th>',
             '</tr></thead><tbody>']

    for r in rows:
        gtv = r['gt_verbs']
        ovv = r['orig_verbs']
        nvv = r['new_verbs']

        def fmt(v, cls_map=None):
            if not v:
                return '<span style="color:#c9d1d9">—</span>'
            out = []
            for k in ('ADD', 'MOD', 'RMV', 'SET'):
                if v.get(k):
                    cls = {'ADD': 'v-a', 'MOD': 'v-m', 'RMV': 'v-r', 'SET': 'v-s'}[k]
                    out.append(f'<span class="{cls}">{VERB_CN[k]}{v[k]}</span>')
            return ' '.join(out)

        # 修正后缺删除的标记
        badge = ''
        if r['orig_miss_rmv'] and not r['miss_rmv']:
            badge = '<span class="tag t-good">已补删除</span>'
        elif r['miss_rmv']:
            badge = '<span class="tag t-bad">仍缺删除</span>'

        tr_cls = 'miss' if r['orig_miss_rmv'] else ''
        miss_flag = '1' if r['orig_miss_rmv'] else '0'

        parts.append(
            f'<tr class="{tr_cls}" data-tk="{esc(r["tk"])}" data-miss="{miss_flag}">'
            f'<td class="tk">{esc(r["tk"])}{badge}</td>'
            f'<td class="num">{r["n_gt"]}</td>'
            f'<td class="num">{r["n_fams"]}</td>'
            f'<td class="verbs">{fmt(gtv)}</td>'
            f'<td class="verbs">{fmt(ovv)}</td>'
            f'<td class="verbs">{fmt(nvv)}</td>'
            f'<td class="num">{r["n_sheets"]}</td>'
            f'<td><pre>{esc(r["orig"][:4000])}</pre></td>'
            f'<td><pre>{esc(r["new"][:4000])}</pre></td>'
            f'</tr>')

    parts.append('</tbody></table>')
    parts.append(f'<script>{JS}</script></body></html>')

    OUT.write_text('\n'.join(parts), encoding='utf-8')
    print(f'✅ {OUT}  ({OUT.stat().st_size // 1024}KB，{len(rows)} 工单)')
    print(f'   原始意图缺删除: {n_orig_miss} 单')
    print(f'   修正后仍缺删除: {n_new_miss} 单')


if __name__ == '__main__':
    main()

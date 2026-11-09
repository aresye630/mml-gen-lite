"""生成 MML 生成系统的评估报告（单文件 HTML，数据内嵌）。

用途：把多轮全量评估的结果做成可浏览的报告，能逐工单看明细，
     而不是只看汇总数字。

数据源：
  · 各轮日志 /tmp/full_eval*.log
  · 产物 /tmp/full_eval_out/<ticket>/mml.txt
  · GT /tmp/gt_cleaned.json
  · 意图/业务数据目录

用法：
  python3 gen_report.py -o /tmp/eval_report.html
"""
import argparse
import html
import json
import re
import shlex
from collections import Counter, defaultdict
from pathlib import Path

GT_PATH = Path('/tmp/gt_cleaned.json')
EVAL_OUT = Path('/tmp/full_eval_out')
INTENT_DIR = Path('/Users/alesc/workspace/gt-rewrite-samples/86个意图_v5')
BIZ_DIR = Path('/tmp/biz_data')

LOG_PAT = re.compile(
    r'^\s+(NC\d+)\s+(\S+)\s+(\d+)s\s+GT\s+(\d+)条/\s*(\d+)族\s+'
    r'产\s+(\d+)条/\s*(\d+)族\s+族\s+(\d+)%\s+对象\s+(\d+)%', re.M)

CMD_PAT = re.compile(r'^(ADD|RMV|MOD|SET)\s+([A-Za-z0-9_]+)', re.I)


def parse_log(path):
    p = Path(path)
    if not p.exists():
        return {}
    txt = p.read_text(encoding='utf-8', errors='replace')
    out = {}
    for m in LOG_PAT.finditer(txt):
        out[m.group(1)] = {
            'status': m.group(2), 'sec': int(m.group(3)),
            'gt_cmds': int(m.group(4)), 'gt_fams': int(m.group(5)),
            'prod_cmds': int(m.group(6)), 'prod_fams': int(m.group(7)),
            'fam_r': int(m.group(8)) / 100, 'obj_r': int(m.group(9)) / 100,
        }
    return out


def parse_families(text):
    """命令文本 → 出现过的族集合（含动词，如 'ADD POOL'）。"""
    fams = set()
    for line in text.split('\n'):
        s = line.split('//')[0].strip()
        m = CMD_PAT.match(s)
        if m:
            fams.add(f'{m.group(1).upper()} {m.group(2).upper()}')
    return fams


def load_gt():
    if not GT_PATH.exists():
        return {}
    gt = json.loads(GT_PATH.read_text(encoding='utf-8'))
    out = {}
    for r in gt:
        tk = r['ticket']
        fams = Counter()
        for _, v, f, p, raw in r['kept']:
            fams[f'{v} {f}'] += 1
        out[tk] = {
            'n': len(r['kept']),
            'fams': dict(fams),
            'cmds': [raw for _, v, f, p, raw in r['kept']],
            'path': r.get('path', ''),
        }
    return out


def load_intent(tk):
    p = INTENT_DIR / f'{tk}_意图.md'
    return p.read_text(encoding='utf-8') if p.exists() else ''


def load_biz(tk):
    p = BIZ_DIR / f'{tk}_bizdata.md'
    return p.read_text(encoding='utf-8') if p.exists() else ''


def load_prod(tk):
    p = EVAL_OUT / tk / 'mml.txt'
    return p.read_text(encoding='utf-8', errors='replace') if p.exists() else ''


PROMPT_CACHE = {}


def load_agent_prompt(tk):
    """从运行容器里读 agent 实际收到的 prompt（含操作清单）。

    这就是输入给 agent 的「意图」——不是原始意图文件，
    而是「原始意图 + 业务数据 + 代码解析的操作清单」。
    """
    if tk in PROMPT_CACHE:
        return PROMPT_CACHE[tk]

    import subprocess
    # ★ 用 session.json 的 name 字段精确匹配工单号
    #   不能用 grep chat.json —— 会把别的工单的会话匹配进来
    #   （实测：NC20260819001887 匹配到了 NC20260911001671 的 prompt）
    py_code = (
        "import glob,os,sys,json\n"
        "tk=" + repr(tk) + "\n"
        "dirs=sorted(glob.glob('/data/sessions/*/'),key=os.path.getmtime,reverse=True)\n"
        "for d in dirs:\n"
        "    sj=os.path.join(d,'session.json')\n"
        "    if not os.path.exists(sj): continue\n"
        "    try:\n"
        "        meta=json.load(open(sj,encoding='utf-8',errors='replace'))\n"
        "    except Exception: continue\n"
        "    nm=str(meta.get('name') or '')\n"
        "    if not nm.startswith(tk): continue\n"
        "    f=os.path.join(d,'.agent','run1','prompt_r1.txt')\n"
        "    if os.path.exists(f):\n"
        "        sys.stdout.write(open(f,encoding='utf-8',errors='replace').read())\n"
        "        break\n"
    )
    for c in ['mmlgen-clean', 'mmlgen-b1', 'mmlgen-b2', 'mmlgen-b3']:
        try:
            subprocess.run(['docker', 'exec', c, 'sh', '-c',
                            'cat > /tmp/_gp.py << \'PYEOF\'\n' + py_code + 'PYEOF\n'],
                           capture_output=True, timeout=30)
            r = subprocess.run(['docker', 'exec', c, 'python3', '/tmp/_gp.py'],
                               capture_output=True, text=True, timeout=30,
                               errors='replace')
            if r.stdout.strip():
                PROMPT_CACHE[tk] = r.stdout
                return r.stdout
        except Exception:
            continue
    PROMPT_CACHE[tk] = ''
    return ''


def build_rows(rounds, gt):
    """合并多轮数据成一个工单列表。"""
    all_tickets = set()
    for r in rounds.values():
        all_tickets |= set(r.keys())

    rows = []
    for tk in sorted(all_tickets):
        g = gt.get(tk) or {}
        gt_fams = set(g.get('fams') or {})
        prod_mml = load_prod(tk)
        prod_fams = parse_families(prod_mml)
        missing = sorted(gt_fams - prod_fams)
        extra = sorted(prod_fams - gt_fams)

        # 各轮数据
        per_round = {}
        for rname, rdata in rounds.items():
            if tk in rdata:
                per_round[rname] = rdata[tk]

        latest = None
        for rname in sorted(rounds.keys(), reverse=True):
            if tk in rounds[rname]:
                latest = rounds[rname][tk]
                latest['_round'] = rname
                break

        rows.append({
            'ticket': tk,
            'gt_n': g.get('n', 0),
            'gt_fams': sorted(gt_fams),
            'n_gt_fams': len(gt_fams),
            'prod_mml': prod_mml,
            'prod_fams': sorted(prod_fams),
            'n_prod_fams': len(prod_fams),
            'missing': missing,
            'extra': extra,
            'per_round': per_round,
            'latest': latest,
            'intent': load_intent(tk),
            'biz': load_biz(tk),
            'agent_prompt': load_agent_prompt(tk),
            'gt_cmds': g.get('cmds') or [],
        })
    return rows


def summarize(rows, rounds):
    """汇总统计。"""
    out = {'rounds': {}, 'overall': {}}
    for rname in rounds:
        d = rounds[rname]
        vals = [v for v in d.values()]
        if not vals:
            continue
        tg = sum(v['gt_fams'] for v in vals)
        th = sum(round(v['fam_r'] * v['gt_fams']) for v in vals)
        to = sum(v['gt_cmds'] for v in vals)  # 近似
        tc = sum(v['prod_cmds'] for v in vals)
        ok = sum(1 for v in vals if v['status'] == 'done')
        secs = sorted(v['sec'] for v in vals)
        out['rounds'][rname] = {
            'n': len(vals),
            'ok': ok,
            'fam_r': th / tg if tg else 0,
            'fam_hit': th,
            'gt_fams': tg,
            'gt_cmds': sum(v['gt_cmds'] for v in vals),
            'prod_cmds': tc,
            'duration_med': secs[len(secs) // 2] if secs else 0,
            'duration_max': max(secs) if secs else 0,
            'duration_avg': sum(secs) / len(secs) if secs else 0,
            'fam_complete': sum(1 for v in vals if v['fam_r'] >= 0.999),
        }
    return out


CSS = """
:root{
  --bg:#f7f8fa; --panel:#fff; --border:#e3e6ea; --text:#1f2328;
  --muted:#656d76; --dim:#8b949e;
  --good:#1a7f37; --good-bg:#dafbe1;
  --warn:#9a6700; --warn-bg:#fff8c5;
  --bad:#cf222e; --bad-bg:#ffebe9;
  --info:#0969da; --info-bg:#ddf4ff;
}
*{box-sizing:border-box}
body{margin:0;font:14px/1.6 -apple-system,BlinkMacSystemFont,"Segoe UI",
     "PingFang SC","Hiragino Sans GB","Microsoft YaHei",sans-serif;
     background:var(--bg);color:var(--text)}
.wrap{max-width:1400px;margin:0 auto;padding:24px}
h1{font-size:22px;margin:0 0 6px}
h2{font-size:17px;margin:32px 0 12px;padding-bottom:8px;border-bottom:1px solid var(--border)}
h3{font-size:15px;margin:20px 0 10px}
.sub{color:var(--muted);font-size:13px;margin-bottom:20px}
.panel{background:var(--panel);border:1px solid var(--border);border-radius:10px;padding:16px;margin-bottom:16px}
.kpis{display:grid;grid-template-columns:repeat(auto-fit,minmax(160px,1fr));gap:12px;margin-bottom:16px}
.kpi{background:var(--panel);border:1px solid var(--border);border-radius:10px;padding:14px}
.kpi .label{font-size:12px;color:var(--muted);margin-bottom:6px}
.kpi .value{font-size:24px;font-weight:600;line-height:1.1}
.kpi .note{font-size:11px;color:var(--dim);margin-top:4px}
table{width:100%;border-collapse:collapse;font-size:13px}
th,td{padding:8px 10px;text-align:left;border-bottom:1px solid var(--border)}
th{background:#fafbfc;font-weight:600;position:sticky;top:0;z-index:1}
tr:hover{background:#f6f8fa}
.tag{display:inline-block;padding:1px 7px;border-radius:5px;font-size:11px;font-weight:600}
.tag.good{background:var(--good-bg);color:var(--good)}
.tag.warn{background:var(--warn-bg);color:var(--warn)}
.tag.bad{background:var(--bad-bg);color:var(--bad)}
.tag.info{background:var(--info-bg);color:var(--info)}
.bar{height:6px;background:#eaeef2;border-radius:3px;overflow:hidden;min-width:80px}
.bar>i{display:block;height:100%;border-radius:3px}
.mono{font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:12px}
tr.detail{display:none !important;background:#fafbfc;border-top:1px solid var(--border)}
tr.detail.open{display:table-row !important}
.detail td{padding:0}
.detail-inner{padding:16px;display:grid;grid-template-columns:1fr 1fr;gap:16px}
.detail-inner.full{grid-template-columns:1fr}
.box{background:#fff;border:1px solid var(--border);border-radius:8px;padding:12px}
.box h4{margin:0 0 8px;font-size:13px;color:var(--muted)}
pre{margin:0;white-space:pre-wrap;word-break:break-all;max-height:320px;overflow:auto;
    font-family:ui-monospace,Menlo,monospace;font-size:11.5px;line-height:1.5}
.fam-list{display:flex;flex-wrap:wrap;gap:4px}
.fam{font-family:ui-monospace,Menlo,monospace;font-size:11px;padding:1px 6px;
     border-radius:4px;background:#eaeef2}
.fam.miss{background:var(--bad-bg);color:var(--bad)}
.fam.extra{background:var(--warn-bg);color:var(--warn)}
.fam.hit{background:var(--good-bg);color:var(--good)}
tr.row{cursor:pointer}
tr.row:hover td:first-child{color:var(--info)}
.chev{display:inline-block;width:12px;color:var(--dim);transition:transform .15s}
tr.row.open .chev{transform:rotate(90deg)}
.toolbar{display:flex;gap:8px;align-items:center;margin-bottom:12px;flex-wrap:wrap}
input[type=search],select{padding:6px 10px;border:1px solid var(--border);border-radius:7px;font-size:13px}
input[type=search]{width:240px}
.pill{padding:4px 10px;border-radius:999px;background:#eaeef2;font-size:12px;cursor:pointer;border:none}
.pill.on{background:var(--info);color:#fff}
.muted{color:var(--muted)}
.right{text-align:right}
"""

JS = """
function toggleRow(el){
  const tr = el.closest('tr');
  const d = tr.nextElementSibling;
  if(!d || !d.classList.contains('detail')) return;
  const willOpen = !d.classList.contains('open');
  tr.classList.toggle('open', willOpen);
  d.classList.toggle('open', willOpen);
  d.style.display = willOpen ? 'table-row' : 'none';
}
function filterRows(){
  const q = (document.getElementById('q').value||'').toLowerCase();
  const minFam = parseFloat(document.getElementById('minfam').value||'0');
  const bigOnly = document.getElementById('bigonly').checked;
  document.querySelectorAll('tr.row').forEach(tr=>{
    const tk = tr.dataset.tk.toLowerCase();
    const fam = parseFloat(tr.dataset.fam||'0');
    const gt = parseInt(tr.dataset.gt||'0');
    let show = tk.includes(q) && fam >= minFam;
    if(bigOnly && gt < 200) show = false;
    tr.style.display = show ? '' : 'none';
    const d = tr.nextElementSibling;
    if(d && d.classList.contains('detail') && !show){
      d.classList.remove('open');
      d.style.display = 'none';
      tr.classList.remove('open');
    }
  });
  const n = [...document.querySelectorAll('tr.row')].filter(t=>t.style.display!=='none').length;
  document.getElementById('cnt').textContent = n;
}
window.addEventListener('DOMContentLoaded', filterRows);
"""


def bar_color(r):
    if r >= 0.999:
        return 'var(--good)'
    if r >= 0.8:
        return '#4ac26b'
    if r >= 0.6:
        return 'var(--warn)'
    if r >= 0.4:
        return '#d4a72c'
    return 'var(--bad)'


def render(rows, summ, out_path):
    ROUND_NAMES = {'v1': '第1轮', 'v2': '第2轮', 'v3': '第3轮', 'v4': '第4轮',
                   'g25': 'G25验证', 'timeout': '超时修复', 'verify': '验证批'}

    # ── 顶部 KPI ──
    latest_round = None
    for rn in ['v4', 'v3', 'v2', 'v1']:
        if rn in summ['rounds']:
            latest_round = rn
            break
    L = summ['rounds'].get(latest_round, {})

    kpis = [
        ('工单总数', str(L.get('n', 0)), '第四轮全量'),
        ('族完备率', f"{L.get('fam_r', 0)*100:.1f}%",
         f"命中 {L.get('fam_hit',0)}/{L.get('gt_fams',0)} 族"),
        ('族完备工单', str(L.get('fam_complete', 0)),
         f"{L.get('fam_complete',0)/max(1,L.get('n',1))*100:.0f}% 的工单全部族命中"),
        ('成功工单', str(L.get('ok', 0)), f"失败 {L.get('n',0)-L.get('ok',0)}"),
        ('单工单中位耗时', f"{L.get('duration_med',0)}s", f"最长 {L.get('duration_max',0)}s"),
        ('命令数', f"{L.get('prod_cmds',0)}/{L.get('gt_cmds',0)}",
         f"{L.get('prod_cmds',0)/max(1,L.get('gt_cmds',1))*100:.0f}% 完成度"),
    ]

    parts = []
    parts.append('<!DOCTYPE html><html lang="zh-CN"><head><meta charset="utf-8">')
    parts.append('<meta name="viewport" content="width=device-width,initial-scale=1">')
    parts.append('<title>MML 生成系统 · 评估报告</title>')
    parts.append(f'<style>{CSS}</style></head><body><div class="wrap">')
    parts.append('<h1>MML 生成系统 · 评估报告</h1>')
    parts.append('<div class="sub">两阶段评估：只给意图 + 业务数据（不含命令族），'
                 'GT 仅用于离线比对。点击任意工单行展开明细。</div>')

    # KPI
    parts.append('<div class="kpis">')
    for label, value, note in kpis:
        parts.append(f'<div class="kpi"><div class="label">{label}</div>'
                     f'<div class="value">{value}</div>'
                     f'<div class="note">{note}</div></div>')
    parts.append('</div>')

    # 轮次对比
    parts.append('<h2>轮次演进</h2>')
    parts.append('<div class="panel"><table><thead><tr>'
                 '<th>轮次</th><th class="right">工单</th><th class="right">成功</th>'
                 '<th class="right">族完备</th><th class="right">族完备工单</th>'
                 '<th class="right">产物命令数</th><th class="right">中位耗时</th>'
                 '<th class="right">最长耗时</th></tr></thead><tbody>')
    for rn in ['v1', 'v2', 'v3', 'v4', 'g25', 'timeout', 'verify']:
        if rn not in summ['rounds']:
            continue
        d = summ['rounds'][rn]
        parts.append(
            f'<tr><td><b>{ROUND_NAMES.get(rn, rn)}</b></td>'
            f'<td class="right">{d["n"]}</td>'
            f'<td class="right">{d["ok"]}</td>'
            f'<td class="right">{d["fam_r"]*100:.1f}%</td>'
            f'<td class="right">{d["fam_complete"]}</td>'
            f'<td class="right">{d["prod_cmds"]}</td>'
            f'<td class="right">{d["duration_med"]}s</td>'
            f'<td class="right">{d["duration_max"]}s</td></tr>')
    parts.append('</tbody></table></div>')

    # 规模分档
    parts.append('<h2>按 GT 规模分档</h2>')
    bands = [(1, 10, '1-10 条'), (11, 50, '11-50 条'), (51, 200, '51-200 条'),
             (201, 500, '201-500 条'), (501, 99999, '500+ 条')]
    vals = [v for v in (rows or []) if v.get('latest')]
    parts.append('<div class="panel"><table><thead><tr>'
                 '<th>档位</th><th class="right">工单</th><th class="right">族完备</th>'
                 '<th class="right">对象召回</th><th class="right">命令完成度</th>'
                 '</tr></thead><tbody>')
    for lo, hi, label in bands:
        sub = [v for v in vals if lo <= v['gt_n'] <= hi]
        if not sub:
            continue
        tg = sum(v['latest']['gt_fams'] for v in sub)
        th = sum(round(v['latest']['fam_r'] * v['latest']['gt_fams']) for v in sub)
        orr = sum(v['latest']['obj_r'] for v in sub) / len(sub)
        gc = sum(v['latest']['gt_cmds'] for v in sub)
        pc = sum(v['latest']['prod_cmds'] for v in sub)
        parts.append(
            f'<tr><td><b>{label}</b></td>'
            f'<td class="right">{len(sub)}</td>'
            f'<td class="right">{th/max(1,tg)*100:.1f}%</td>'
            f'<td class="right">{orr*100:.1f}%</td>'
            f'<td class="right">{pc/max(1,gc)*100:.0f}%</td></tr>')
    parts.append('</tbody></table></div>')

    # 按输入信息充分度分档（判断问题在意图还是 agent）
    parts.append('<h2>按输入信息充分度分档</h2>')
    parts.append('<div class="sub">'
                 '业务数据字数是关键：意图只说业务名（189 字），'
                 '业务数据才给出对象清单（如「1294 条配置 + 55 个 APN 名」）。'
                 '业务数据太少的工单，agent 无从配全，这是输入问题不是能力问题。'
                 '</div>')
    parts.append('<div class="panel"><table><thead><tr>'
                 '<th>业务数据量</th><th class="right">工单</th>'
                 '<th class="right">GT 命令中位</th><th class="right">族完备</th>'
                 '<th class="right">命令完成度</th></tr></thead><tbody>')
    biz_bands = [(0, 200, '< 200 字（极少）'), (200, 600, '200-600 字'),
                 (600, 1500, '600-1500 字'), (1500, 999999, '> 1500 字（充分）')]
    for lo, hi, label in biz_bands:
        sub = [v for v in vals if lo <= len(v['biz']) < hi]
        if not sub:
            continue
        tg = sum(v['latest']['gt_fams'] for v in sub)
        th = sum(round(v['latest']['fam_r'] * v['latest']['gt_fams']) for v in sub)
        gc = sum(v['latest']['gt_cmds'] for v in sub)
        pc = sum(v['latest']['prod_cmds'] for v in sub)
        gt_med = sorted(v['latest']['gt_cmds'] for v in sub)[len(sub) // 2]
        parts.append(
            f'<tr><td><b>{label}</b></td>'
            f'<td class="right">{len(sub)}</td>'
            f'<td class="right">{gt_med}</td>'
            f'<td class="right">{th/max(1,tg)*100:.1f}%</td>'
            f'<td class="right">{pc/max(1,gc)*100:.0f}%</td></tr>')
    parts.append('</tbody></table></div>')

    # 缺失族 TOP
    parts.append('<h2>缺失族排行</h2>')
    miss_cnt = Counter()
    for v in vals:
        for f in v['missing']:
            miss_cnt[f] += 1
    parts.append('<div class="panel"><table><thead><tr>'
                 '<th>族</th><th class="right">缺失工单数</th>'
                 '<th>说明</th></tr></thead><tbody>')
    for f, n in miss_cnt.most_common(25):
        parts.append(f'<tr><td class="mono">{html.escape(f)}</td>'
                     f'<td class="right">{n}</td><td class="muted">—</td></tr>')
    parts.append('</tbody></table></div>')

    # 工单明细
    parts.append('<h2>工单明细</h2>')
    parts.append('<div class="toolbar">'
                 '<input type="search" id="q" placeholder="搜索工单号…" oninput="filterRows()">'
                 '<label>族完备 ≥ <select id="minfam" onchange="filterRows()">'
                 '<option value="0">全部</option><option value="0.4">40%</option>'
                 '<option value="0.6">60%</option><option value="0.8">80%</option>'
                 '<option value="0.999">100%</option></select></label>'
                 '<label><input type="checkbox" id="bigonly" onchange="filterRows()"> 只看大工单（GT≥200）</label>'
                 '<span class="muted">显示 <b id="cnt">0</b> 个</span>'
                 '</div>')

    parts.append('<div class="panel" style="padding:0;overflow:auto;max-height:70vh">')
    parts.append('<table><thead><tr>'
                 '<th style="width:120px">工单</th>'
                 '<th class="right" style="width:70px">GT条/族</th>'
                 '<th class="right" style="width:70px">产物条/族</th>'
                 '<th style="width:130px">族完备</th>'
                 '<th class="right" style="width:60px">对象</th>'
                 '<th class="right" style="width:60px">耗时</th>'
                 '<th class="right" style="width:80px" title="输入给 agent 的 prompt 字数">prompt</th>'
                 '<th style="width:120px">缺的族</th>'
                 '</tr></thead><tbody>')

    SORTED = sorted(vals, key=lambda v: (v['latest']['fam_r'], -v['gt_n']))
    for v in SORTED:
        lt = v['latest']
        r = lt['fam_r']
        color = bar_color(r)
        miss_preview = ', '.join(f.split()[1] if ' ' in f else f for f in v['missing'][:4])
        if len(v['missing']) > 4:
            miss_preview += f" +{len(v['missing'])-4}"

        # 族清单
        gt_set = set(v['gt_fams'])
        pr_set = set(v['prod_fams'])
        fam_chips = []
        for f in sorted(gt_set | pr_set):
            if f in gt_set and f in pr_set:
                cls = 'hit'
            elif f in gt_set:
                cls = 'miss'
            else:
                cls = 'extra'
            fam_chips.append(f'<span class="fam {cls}">{html.escape(f)}</span>')

        parts.append(
            f'<tr class="row" data-tk="{v["ticket"]}" data-fam="{r}" data-gt="{v["gt_n"]}" '
            f'onclick="toggleRow(this)">'
            f'<td><span class="chev">▶</span> {v["ticket"]}</td>'
            f'<td class="right">{lt["gt_cmds"]}/{lt["gt_fams"]}</td>'
            f'<td class="right">{lt["prod_cmds"]}/{lt["prod_fams"]}</td>'
            f'<td><div style="display:flex;align-items:center;gap:6px">'
            f'<div class="bar" style="flex:1"><i style="width:{r*100:.0f}%;background:{color}"></i></div>'
            f'<span class="mono" style="width:36px;text-align:right">{r*100:.0f}%</span></div></td>'
            f'<td class="right">{lt["obj_r"]*100:.0f}%</td>'
            f'<td class="right">{lt["sec"]}s</td>'
            f'<td class="right muted" style="font-size:11px" '
            f'title="prompt {len(v.get("agent_prompt") or "")} 字'
            f' = 意图 {len(v["intent"])} + 业务数据 {len(v["biz"])}">'
            f'{len(v.get("agent_prompt") or "") or (len(v["intent"])+len(v["biz"]))}</td>'
            f'<td class="muted" style="font-size:12px">{html.escape(miss_preview)}</td>'
            f'</tr>')

        # 展开明细
        parts.append(f'<tr class="detail"><td colspan="8"><div class="detail-inner">')
        parts.append(f'<div class="box"><h4>族对照（{len(gt_set)} GT / {len(pr_set)} 产物）</h4>'
                     f'<div class="fam-list">{"".join(fam_chips)}</div></div>')
        # ★ 显示「输入给 agent 的完整 prompt」，而不是原始意图文件
        #   agent 实际收到的是：原始意图 + 业务数据 + 代码解析的操作清单
        ap = v.get('agent_prompt') or ''
        if ap:
            parts.append(
                f'<div class="box" style="grid-column:1/-1">'
                f'<h4>输入给 agent 的 prompt（{len(ap)} 字）'
                f'　<span style="color:#656d76;font-weight:400">'
                f'= 原始意图 {len(v["intent"])} 字 + 业务数据 {len(v["biz"])} 字'
                f' + 代码解析的操作清单</span></h4>'
                f'<pre style="max-height:400px">{html.escape(ap[:6000])}</pre></div>')
        else:
            parts.append(f'<div class="box"><h4>原始意图（{len(v["intent"])} 字）</h4>'
                         f'<pre>{html.escape(v["intent"][:2500])}</pre></div>')
            parts.append(f'<div class="box"><h4>业务数据（{len(v["biz"])} 字）</h4>'
                         f'<pre>{html.escape(v["biz"][:2500])}</pre></div>')
        parts.append(f'<div class="box"><h4>产物 mml（前 60 行）</h4>'
                     f'<pre>{html.escape(chr(10).join(v["prod_mml"].split(chr(10))[:60]))}</pre></div>')
        parts.append(f'<div class="box"><h4>GT 命令（前 40 条）</h4>'
                     f'<pre>{html.escape(chr(10).join(v["gt_cmds"][:40]))}</pre></div>')
        parts.append('</div></td></tr>')

    parts.append('</tbody></table></div>')
    parts.append(f'<div class="sub" style="margin-top:20px">'
                 f'生成时间：{__import__("datetime").datetime.now():%Y-%m-%d %H:%M}　'
                 f'数据源：{len(rows)} 个工单 · 4 轮全量评估</div>')
    parts.append(f'<script>{JS}</script>')
    parts.append('</div></body></html>')

    out = Path(out_path)
    out.write_text('\n'.join(parts), encoding='utf-8')
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('-o', '--out', default='/tmp/eval_report.html')
    args = ap.parse_args()

    rounds = {
        'v1': parse_log('/tmp/full_eval.log'),
        'v2': parse_log('/tmp/full_eval_v2.log'),
        'v3': parse_log('/tmp/full_eval_v3.log'),
        'v4': parse_log('/tmp/full_eval_v4.log'),
        'g25': parse_log('/tmp/verify_g25.log'),
        'timeout': parse_log('/tmp/verify_timeout.log'),
        'verify': parse_log('/tmp/verify_apn2.log'),
    }
    rounds = {k: v for k, v in rounds.items() if v}
    print(f'轮次: {list(rounds.keys())}')

    gt = load_gt()
    print(f'GT 工单: {len(gt)}')

    rows = build_rows(rounds, gt)
    print(f'合并工单: {len(rows)}')

    summ = summarize(rows, rounds)
    out = render(rows, summ, args.out)
    print(f'✅ 报告: {out}  ({out.stat().st_size//1024}KB)')


if __name__ == '__main__':
    main()

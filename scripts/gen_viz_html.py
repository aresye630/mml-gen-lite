#!/usr/bin/env python3
"""exp 可视化单文件 HTML 生成器。

输入：exp.txt + F### 特性配置 MD 目录 + relations.json（关联与公共配置）
输出：单文件 HTML（数据内嵌，双击即开，零外部依赖）

视图：特性映射（三档统计/列表/详情+段落）/ 关联（列表+详情）/ 公共配置（对象表+详情）
联动：任何 EXP 区间（段落/对象命令位置）→ 底部命令流带滚动高亮

用法:
  python3 gen_viz_html.py --exp <exp.txt> --feat-md <特性配置基线目录> \
      --rels <relations.json> -o <输出.html>
"""
import argparse
import json
import os
import re
import sys
from collections import Counter, defaultdict

# ═══ 命令族分类（展示分组规则，按序匹配） ═══
FAMILY_RULES = [
    (r'^(DSP|LST|SHOW|CHK|EXP)\b', '查询'),
    (r'LICENSESWITCH', 'license'),
    (r'SOFTPARA|AUTOCONFIG|REFRESHSRV|FEATURE', '系统'),
    (r'^ADD AUTOSCALING|AUTOSCALING', '自动缩放'),
    (r'L3VPNINST|VPNINST|IPBINDVPN|LOGICINF', '承载VRF'),
    (r'GRETUNNEL|TUNNEL|IPSec|IPsec', '隧道'),
    (r'INTERFACE|IFIPV4ADDRESS|IFIPV6ADDRESS|TRUNK|ETH', '接口'),
    (r'BGP|SRROUTE|NETWORKROUTE|IMPORTROUTE|ROUTEPOLICY', '路由BGP'),
    (r'BFD', 'BFD'),
    (r'POOL|SECTION', '地址池'),
    (r'FILTER|FLTBIND|L7FILTER|PROTBIND', '过滤器'),
    (r'URR|PCCPOLICYGRP|^ADD RULE|RULEBINDING|USERPROFILE', '计费'),
    (r'^SET APN|^ADD APN|APN', 'APN'),
    (r'IPFARM|APPAUTH|AUTH|MEP', '安全认证'),
    (r'REDUND|RDT|RUA|LAWFUL|LAWFE', '冗余/合法'),
]
FAMILY_COLORS = {
    '承载VRF': '#4cc9f0', '接口': '#38bdf8', '路由BGP': '#818cf8',
    '地址池': '#34d399', '计费': '#fbbf24', '过滤器': '#f472b6',
    'APN': '#fb923c', 'license': '#e879f9', '系统': '#94a3b8',
    '隧道': '#2dd4bf', 'BFD': '#f87171', '自动缩放': '#a3e635',
    '安全认证': '#c084fc', '冗余/合法': '#fda4af', '查询': '#475569',
    '其他': '#64748b',
}

# 对象参数族（前端筛选分组用）
OBJ_PARAM_FAMILY = {
    'VRFNAME': 'VRF', 'DESTVRFNAME': 'VRF', 'VPNINSTANCE': 'VRF',
    'APN': 'APN',
    'IFNAME': '接口', 'MEMBERIFNAME': '接口', 'TRUNKIFNAME': '接口',
    'POOLNAME': '地址池',
    'LICITEM': 'license',
    'FILTERNAME': '过滤器', 'FLOWFILTERNAME': '过滤器',
}

MAX_INLINE = 500 * 1024  # 超过此大小不注入内容（仅清单）


def collect_files(base):
    """扫描产物目录 → 分组文件清单（小文件内嵌内容，F### 仅清单）"""
    groups = []

    def add_group(gname, path, feat_list=False):
        if not os.path.isdir(path):
            return  # 目录不存在（新上传 case 尚无该产物）→ 跳过组
        items = []
        for fn in sorted(os.listdir(path)):
            if fn.startswith('.') or fn.startswith('._'):
                continue
            fp = os.path.join(path, fn)
            if not os.path.isfile(fp):
                continue
            if fn == 'exp_viz.html':
                continue
            ext = fn.rsplit('.', 1)[-1].lower()
            t = {'md': 'md', 'csv': 'csv', 'json': 'json', 'yaml': 'yaml',
                 'txt': 'code'}.get(ext, 'code')
            it = {'n': fn, 't': t, 'sz': os.path.getsize(fp)}
            if feat_list:
                m = re.match(r'^F(\d+)', fn)
                if m:
                    it['fno'] = int(m.group(1))
                    items.append(it)
                    continue
            if os.path.getsize(fp) <= MAX_INLINE:
                try:
                    it['c'] = open(fp, encoding='utf-8-sig').read()
                except Exception:
                    it['t'] = 'code'
            else:
                it['t'] = 'big'
            items.append(it)
        groups.append({'g': gname, 'items': items})

    add_group('根目录', base)
    add_group('exp_analysis', os.path.join(base, 'exp_analysis'))
    add_group('特性关联与公共配置', os.path.join(base, '特性关联与公共配置'))
    feat_path = os.path.join(base, '特性配置基线')
    n_feat = len([f for f in os.listdir(feat_path)
                  if re.match(r'^F\d+\.md$', f)]) if os.path.isdir(feat_path) else 0
    add_group(f'特性配置基线 ({n_feat}篇)', feat_path, feat_list=True)
    return groups


def family_of(cmd):
    for rx, fam in FAMILY_RULES:
        if re.search(rx, cmd):
            return fam
    return '其他'


def parse_exp(path):
    """exp → [{seq, cmd, fam, kp}]（kp = 前 3 参数摘要）"""
    out = []
    for seq, ln in enumerate(open(path, encoding='utf-8'), 1):
        ln = ln.strip()
        if not ln or ln.startswith(';') or ln.startswith('//'):
            continue
        m = re.match(r'^([A-Z]+ [A-Z0-9]+):(.*?);?\s*$', ln)
        if not m:
            continue
        cmd = m.group(1)
        params = [(pm.group(1), (pm.group(2) or pm.group(3) or '').strip())
                  for pm in re.finditer(r'([A-Z0-9_]+)=(?:([^,;\"]+)|\"([^\"]*)\")', m.group(2))]
        kp = ' '.join(f'{k}={v}' for k, v in params[:3])
        out.append({'seq': seq, 'cmd': cmd, 'fam': family_of(cmd), 'kp': kp})
    return out


def parse_feature_mds(md_dir):
    """扫描 F### MD（v2 格式：F001.md + 判定卡）→ [{fno, tag, title, k, n, pct, matched, paras, src}]

    tag 映射（2026-09-07 四档修复）：判定卡状态 已配置→strong / 弱匹配→weak /
    需人工→manual / 未配置→none。原三档 else 兜底把「需人工」并入 weak，
    导致顶栏统计与筛选错位（需人工 294 条混入弱匹配 594）。
    k/n   = 核心命令 命中/总数；paras = §5 exp 实际配置的命令级行号区间（流带定位）
    """
    feats = []
    for fn in sorted(os.listdir(md_dir)):
        m = re.match(r'^F(\d+)\.md$', fn)
        if not m:
            continue
        fno = int(m.group(1))
        try:
            text = open(os.path.join(md_dir, fn), encoding='utf-8').read()
        except Exception:
            continue
        tm = re.search(r'^#\s+(.+)$', text, re.M)
        title = tm.group(1).strip() if tm else fn
        sm = re.search(r'判定：\*\*([^*]+?)\*\*', text)
        st = sm.group(1) if sm else ''
        # 四档显式分派（判定卡实测四值互斥：✅ 已配置/🟡 弱匹配/⚠️ 需人工/❌ 未配置）
        tag = ('strong' if '已配置' in st else
               'manual' if '需人工' in st else
               'weak' if '弱匹配' in st else 'none')
        hit_cmds = re.findall(r'\| `([A-Z]+ [A-Z0-9]+)` \| ✅ 命中', text)
        miss_cmds = re.findall(r'\| `([A-Z]+ [A-Z0-9]+)` \| ❌ 缺失', text)
        k, n = len(hit_cmds), len(hit_cmds) + len(miss_cmds)
        paras = []
        for cm in re.finditer(r'^### ([A-Z]+ [A-Z0-9]+) \[(?:核心|配套公共)\]\s*$\n```text\n(.*?)\n```',
                              text, re.M | re.S):
            seqs = [int(x) for x in re.findall(r';\s*(\d+)\s*\|', cm.group(2))]
            if seqs:
                paras.append({'a': min(seqs), 'b': max(seqs),
                              'n': len(seqs), 'sum': cm.group(1)})
        feats.append({'fno': fno, 'tag': tag, 'title': title,
                      'k': k, 'n': n, 'pct': round(100 * k / max(n, 1)),
                      'matched': sum(p['n'] for p in paras), 'paras': paras,
                      'key_line': '', 'deg_line': '', 'unconf': '', 'src': fn})
    return feats


def build_html(data):
    """组装单文件 HTML（数据 JSON 注入）。

    占位注释 + 后续 let DATA 声明必须整块替换：若只替换注释行，
    注入的 `DATA = {...}` 赋值会落在 `let DATA` 的 TDZ 区间，
    报 Cannot access 'DATA' before initialization（web 模式改造回归 bug）。
    """
    js = json.dumps(data, ensure_ascii=False, separators=(',', ':'))
    return HTML_TEMPLATE.replace(
        '// __VIZ_DATA__\nlet DATA = null, CUR_CASE = null;',
        f'var DATA = {js}; var CUR_CASE = "static";'
    )


HTML_TEMPLATE = r'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>EXP 可视化工作台</title>
<style>
:root{
  --bg:#0a0d13; --bg2:#0d1119; --panel:#11151f; --panel2:#161c29;
  --border:#1f2735; --border2:#2a3446;
  --ink:#e8ecf3; --muted:#8b95a7; --faint:#5d6778;
  --cyan:#4cc9f0; --amber:#fbbf24; --green:#34d399; --red:#f87171;
  --mono:ui-monospace,"SF Mono",Menlo,Consolas,"PingFang SC",monospace;
  --sans:-apple-system,BlinkMacSystemFont,"PingFang SC","Hiragino Sans GB","Microsoft YaHei",sans-serif;
}
*{margin:0;padding:0;box-sizing:border-box}
html,body{height:100%;background:var(--bg);font-family:var(--sans);color:var(--ink);overflow:hidden}
.app{display:flex;flex-direction:column;height:100vh}

/* ═══ 顶栏 ═══ */
header{flex:none;display:flex;align-items:center;gap:14px;padding:0 16px;height:50px;
  background:var(--bg2);border-bottom:1px solid var(--border)}
.logo{font-size:14px;font-weight:800;flex:none}
.logo em{color:var(--cyan);font-style:normal}
.statbar{display:flex;gap:8px;flex:none}
.statbar .st{font-family:var(--mono);font-size:11px;padding:4px 12px;border-radius:6px;cursor:pointer;border:1px solid var(--border)}
.statbar .st b{font-size:13px}
.statbar .st.strong{color:var(--green);border-color:rgba(52,211,153,.4);background:rgba(52,211,153,.06)}
.statbar .st.weak{color:var(--amber);border-color:rgba(251,191,36,.35);background:rgba(251,191,36,.05)}
.statbar .st.manual{color:#fb923c;border-color:rgba(251,146,60,.4);background:rgba(251,146,60,.06)}
.statbar .st.none{color:var(--faint);border-color:var(--border2)}
.statbar .st.on{outline:1px solid var(--cyan)}
.casetools{display:flex;gap:8px;align-items:center;flex:none}
#caseSel{background:var(--panel);border:1px solid var(--border2);border-radius:8px;color:var(--ink);
  font-size:11px;padding:6px 10px;outline:none;max-width:210px;font-family:var(--mono)}
.upbtn{font-size:11px;font-weight:700;padding:6px 13px;border-radius:8px;cursor:pointer;
  border:1px solid rgba(52,211,153,.4);color:var(--green);background:rgba(52,211,153,.07)}
.upbtn:hover{background:rgba(52,211,153,.14)}
.search{flex:1;max-width:380px;margin-left:auto}
.search input{width:100%;background:var(--panel);border:1px solid var(--border2);border-radius:8px;
  color:var(--ink);font-size:12px;padding:7px 12px;outline:none;font-family:var(--sans)}
.search input:focus{border-color:var(--cyan-dim,var(--cyan))}
.viewtabs{display:flex;border:1px solid var(--border2);border-radius:8px;overflow:hidden;flex:none}
.viewtabs button{background:transparent;border:none;color:var(--muted);font-size:12px;font-weight:600;
  padding:7px 16px;cursor:pointer;font-family:var(--sans)}
.viewtabs button.on{background:rgba(76,201,240,.1);color:var(--cyan)}

/* ═══ 主区 ═══ */
.main{flex:1;display:flex;min-height:0}

/* 左栏 */
aside.left{flex:none;width:330px;background:var(--bg2);border-right:1px solid var(--border);
  display:flex;flex-direction:column;min-height:0}
.l-t{font-family:var(--mono);font-size:10px;color:var(--faint);letter-spacing:1.5px;
  padding:10px 14px 6px;display:flex;align-items:center;gap:8px}
.l-t::after{content:"";flex:1;height:1px;background:var(--border)}
.list{flex:1;overflow-y:auto;padding:0 8px 10px}
.fitem{display:flex;align-items:center;gap:8px;padding:7px 9px;border-radius:7px;cursor:pointer;
  font-size:11.5px;border:1px solid transparent;margin-bottom:2px}
.fitem:hover{background:var(--panel)}
.fitem.on{background:var(--panel);border-color:rgba(76,201,240,.35)}
.fitem .no{font-family:var(--mono);font-size:9.5px;color:var(--faint);flex:none;width:38px}
.fitem .tt{flex:1;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.fitem .kv{font-family:var(--mono);font-size:9px;flex:none;color:var(--muted)}
.dot{width:7px;height:7px;border-radius:50%;flex:none}
.dot.strong{background:var(--green)} .dot.weak{background:var(--amber)} .dot.manual{background:#fb923c} .dot.none{background:var(--faint)}

/* 中栏 */
section.main-v{flex:1;display:flex;flex-direction:column;min-width:0;overflow:hidden}
.vhead{flex:none;padding:12px 20px 8px;border-bottom:1px solid var(--border);
  display:flex;align-items:center;gap:10px}
.vhead h2{font-size:14px;font-weight:700;flex:1;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.vhead .meta{font-family:var(--mono);font-size:10px;color:var(--faint);flex:none}
.vbody{flex:1;overflow-y:auto;padding:14px 20px}

/* 详情卡片 */
.card{background:var(--panel);border:1px solid var(--border);border-radius:10px;padding:12px 16px;margin-bottom:10px}
.card .c-t{font-size:12px;font-weight:700;margin-bottom:8px;display:flex;align-items:center;gap:8px}
.card .c-t .k{font-family:var(--mono);font-size:9.5px;color:var(--cyan);border:1px solid rgba(76,201,240,.3);
  border-radius:3px;padding:1px 6px;background:rgba(76,201,240,.06);font-weight:600}
.card .c-d{font-size:12px;color:var(--muted);line-height:1.65}
.card .c-d b{color:var(--ink)}
.card .c-d code{font-family:var(--mono);font-size:10.5px;color:var(--amber);background:rgba(251,191,36,.06);padding:1px 5px;border-radius:3px}
.badge{font-family:var(--mono);font-size:9px;padding:2px 8px;border-radius:10px;flex:none;border:1px solid}
.badge.strong{color:var(--green);border-color:rgba(52,211,153,.4)}
.badge.weak{color:var(--amber);border-color:rgba(251,191,36,.4)}
.badge.manual{color:#fb923c;border-color:rgba(251,146,60,.4)}
.badge.none{color:var(--faint);border-color:var(--border2)}

/* 段落列表 */
.para{display:flex;align-items:center;gap:10px;background:var(--panel2);border:1px solid var(--border);
  border-radius:7px;padding:8px 12px;margin-bottom:6px;cursor:pointer;font-size:11.5px}
.para:hover{border-color:var(--cyan-dim,var(--cyan))}
.para .rng{font-family:var(--mono);font-size:10.5px;color:var(--cyan);flex:none}
.para .sum{flex:1;color:var(--muted);white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.para .n{font-family:var(--mono);font-size:9.5px;color:var(--faint);flex:none}

/* 表格 */
table.tbl{width:100%;border-collapse:collapse;font-size:11px}
table.tbl th{font-size:10px;color:var(--faint);text-align:left;padding:5px 9px;border-bottom:1px solid var(--border2);font-weight:600}
table.tbl td{padding:5px 9px;border-bottom:1px solid var(--border);color:var(--muted);vertical-align:top;line-height:1.5}
table.tbl td b{color:var(--ink)}
table.tbl tr:hover td{background:rgba(76,201,240,.03)}
.tbl-wrap{max-height:480px;overflow-y:auto;border:1px solid var(--border);border-radius:8px}
.tbl-wrap::-webkit-scrollbar{width:7px}
.tbl-wrap::-webkit-scrollbar-thumb{background:var(--border2);border-radius:4px}

/* 流带 */
.band{flex:none;height:74px;background:var(--bg2);border-top:1px solid var(--border);position:relative}
.band .bhead{height:20px;display:flex;align-items:center;gap:8px;padding:0 12px;font-family:var(--mono);font-size:9px;color:var(--faint)}
.band .bhead .legend{display:flex;gap:10px;margin-left:auto}
.band .bhead .lg{display:flex;align-items:center;gap:4px}
.band .bhead .lg i{width:9px;height:9px;border-radius:2px;display:inline-block}
.band-scroll{height:54px;overflow-x:auto;overflow-y:hidden;position:relative}
.band-scroll::-webkit-scrollbar{height:6px}
.band-scroll::-webkit-scrollbar-thumb{background:var(--border2);border-radius:3px}
.band-inner{position:relative;height:50px;padding:4px 0}
.cmd{position:absolute;top:2px;width:2px;border-radius:1px;cursor:pointer}
.cmd:hover{outline:1px solid #fff;z-index:5}
.band-hl{position:absolute;top:0;bottom:0;background:rgba(251,191,36,.18);border:1px solid rgba(251,191,36,.5);pointer-events:none;z-index:3}
.tip{position:fixed;z-index:99;background:#0d1119;border:1px solid var(--border2);border-radius:8px;
  padding:8px 12px;font-family:var(--mono);font-size:10.5px;color:var(--ink);max-width:520px;display:none;pointer-events:none}
.tip .t-cmd{color:var(--cyan);font-weight:700}
.tip .t-kp{color:var(--muted);margin-top:3px;word-break:break-all}

/* 空态 */
.empty{color:var(--faint);font-size:11px;text-align:center;padding:50px 10px;line-height:1.9}
.empty .big{font-size:26px;display:block;margin-bottom:8px;opacity:.5}

/* 关联 */
.rel-row{display:flex;align-items:center;gap:10px;background:var(--panel2);border:1px solid var(--border);
  border-radius:7px;padding:8px 12px;margin-bottom:5px;cursor:pointer;font-size:11.5px}
.rel-row:hover{border-color:var(--cyan-dim,var(--cyan))}
.rel-row .b{flex:1;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.rel-row .sc{font-family:var(--mono);font-size:10px;color:var(--amber);flex:none}
.rel-row .ob{font-family:var(--mono);font-size:9.5px;color:var(--cyan);flex:none}

/* 步骤条 / 工作台 */
.steps{display:flex;gap:6px;margin-bottom:12px;flex-wrap:wrap}
.step{font-family:var(--mono);font-size:10.5px;padding:5px 14px;border-radius:6px;
  border:1px solid var(--border2);color:var(--faint);background:var(--panel)}
.step.on{color:var(--cyan);border-color:rgba(76,201,240,.4);background:rgba(76,201,240,.07)}
.step i{font-style:normal;margin-right:6px}
.btn{display:inline-block;font-size:11.5px;font-weight:600;padding:6px 16px;border-radius:7px;cursor:pointer;
  border:1px solid var(--border2);color:var(--muted);background:var(--panel2);margin-top:8px}
.btn.off{opacity:.45;cursor:not-allowed;text-decoration:line-through}
.btn.off:hover{color:var(--muted)}
.btn.act{color:#0a0d13;background:var(--cyan);border-color:var(--cyan)}
.hint{font-size:10.5px;color:var(--faint);margin-top:6px;line-height:1.7}

/* 产物视图 */
.gitem{font-size:11px;padding:5px 9px;border-radius:6px;cursor:pointer;color:var(--muted);
  display:flex;align-items:center;gap:7px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.gitem:hover{background:var(--panel);color:var(--ink)}
.gitem.on{background:var(--panel);color:var(--cyan)}
.gitem .ic{flex:none;font-family:var(--mono);font-size:8.5px;padding:1px 5px;border-radius:3px;border:1px solid var(--border2);color:var(--faint)}
.gitem .nm{flex:1;overflow:hidden;text-overflow:ellipsis}
.gitem .sz{font-family:var(--mono);font-size:8.5px;color:var(--faint);flex:none}
.gh{display:flex;align-items:center;gap:8px;padding:8px 9px 5px;font-size:10px;font-weight:700;
  color:var(--muted);cursor:pointer;user-select:none;letter-spacing:.5px}
.gh::before{content:"▾";font-size:8px;color:var(--faint);transition:transform .15s}
.gh.collapsed::before{transform:rotate(-90deg)}
.gh .cnt{font-family:var(--mono);font-size:9px;color:var(--faint);font-weight:400;margin-left:auto}

/* markdown 渲染 */
.md{font-size:12px;line-height:1.75;color:var(--ink)}
.md h1,.md h2,.md h3{font-size:13px;margin:14px 0 8px;color:var(--ink)}
.md h1{font-size:15px;border-bottom:1px solid var(--border);padding-bottom:6px}
.md table{border-collapse:collapse;font-size:10.5px;margin:8px 0;width:100%}
.md th,.md td{border:1px solid var(--border2);padding:4px 9px;text-align:left;color:var(--muted)}
.md th{color:var(--ink);background:var(--panel2);white-space:nowrap}
.md tr:hover td{background:rgba(76,201,240,.03)}
.md code{font-family:var(--mono);font-size:10px;background:rgba(76,201,240,.08);color:var(--cyan);
  padding:1px 5px;border-radius:3px}
.md pre{background:#0b0e15;border:1px solid var(--border);border-radius:8px;padding:10px 14px;
  overflow-x:auto;font-family:var(--mono);font-size:10.5px;color:#c8d3e5;margin:8px 0;line-height:1.6}
.md pre code{background:none;color:inherit;padding:0}
.md blockquote{border-left:3px solid var(--border2);padding:2px 12px;color:var(--faint);margin:8px 0;font-size:11px}
.md blockquote p{margin:2px 0}
.md li{margin:2px 0}
.md strong{color:var(--ink)}
.file-meta{font-family:var(--mono);font-size:9.5px;color:var(--faint);margin-bottom:8px}
.dlbtn{float:right;font-size:10.5px;padding:4px 12px;border-radius:6px;border:1px solid rgba(76,201,240,.4);
  color:var(--cyan);background:rgba(76,201,240,.07);cursor:pointer}
.csv-note{font-size:10px;color:var(--faint);margin-top:6px}

/* 对话产物按钮 */
.artbtn{display:inline-flex;align-items:center;gap:5px;font-size:10.5px;font-weight:600;
  padding:4px 12px;border-radius:14px;cursor:pointer;margin:2px 4px 2px 0;
  border:1px solid rgba(76,201,240,.45);color:var(--cyan);background:rgba(76,201,240,.08)}
.artbtn:hover{background:rgba(76,201,240,.18);text-decoration:none}
.artrow{margin-top:8px;display:flex;gap:6px;flex-wrap:wrap}

/* 对话栏（常驻） */
.chat{flex:none;width:360px;background:var(--bg2);border-left:1px solid var(--border);
  display:flex;flex-direction:column;min-height:0}
.chat .c-h{flex:none;display:flex;align-items:center;gap:10px;padding:12px 16px;border-bottom:1px solid var(--border)}
.chat .c-h b{font-size:13px}
.chat .c-h .st{font-family:var(--mono);font-size:9px;color:var(--amber);border:1px solid rgba(251,191,36,.4);
  padding:2px 8px;border-radius:10px}
.chat .msgs{flex:1;overflow-y:auto;padding:14px;display:flex;flex-direction:column;gap:10px;min-height:0}
.msg{max-width:88%;padding:9px 12px;border-radius:10px;font-size:11.5px;line-height:1.7;white-space:pre-wrap}
.msg.user{align-self:flex-end;background:rgba(76,201,240,.14);border:1px solid rgba(76,201,240,.3);color:var(--ink)}
.msg.bot{align-self:flex-start;background:var(--panel);border:1px solid var(--border);color:var(--muted)}
.msg.bot b{color:var(--ink)}
.msg.bot code{font-family:var(--mono);font-size:10px;color:var(--amber);background:rgba(251,191,36,.08);padding:1px 5px;border-radius:3px}
.msg.bot .l{display:block;font-size:10px;color:var(--cyan);margin-top:6px;cursor:pointer}
.msg.bot .l:hover{text-decoration:underline}
.chips{flex:none;display:flex;gap:6px;flex-wrap:wrap;padding:8px 14px 2px}
.chip{font-size:10px;color:var(--muted);border:1px solid var(--border2);border-radius:12px;padding:3px 10px;cursor:pointer;background:var(--panel)}
.chip:hover{color:var(--cyan);border-color:rgba(76,201,240,.4)}
.chat .c-in{flex:none;display:flex;gap:8px;padding:10px 14px 14px;border-top:1px solid var(--border)}
.chat .c-in input{flex:1;background:var(--panel);border:1px solid var(--border2);border-radius:8px;color:var(--ink);
  font-size:12px;padding:9px 12px;outline:none}
.chat .c-in input:focus{border-color:rgba(76,201,240,.5)}
.chat .c-in .go{flex:none;background:var(--cyan);color:#0a0d13;border:none;border-radius:8px;padding:0 18px;
  font-size:12px;font-weight:800;cursor:pointer}
.chat .c-in .go:hover{filter:brightness(1.1)}
</style>
</head>
<body>
<div class="app">
  <header>
    <div class="logo">EXP 可视化工作台</div>
    <div class="statbar">
      <span class="st strong" data-tag="strong"><b id="cStrong">0</b> 已配置</span>
      <span class="st weak" data-tag="weak"><b id="cWeak">0</b> 弱匹配</span>
      <span class="st manual" data-tag="manual"><b id="cManual">0</b> 需人工</span>
      <span class="st none" data-tag="none"><b id="cNone">0</b> 未配置</span>
    </div>
    <div class="search"><input id="searchBox" placeholder="搜索特性 / 对象 / 命令…"></div>
    <div class="viewtabs">
      <button class="on" data-v="feat">特性</button>
      <button data-v="rel">关联</button>
      <button data-v="obj">公共配置</button>
      <button data-v="gen">配置生成</button>
      <button data-v="files">产物</button>
      <button data-v="hist">历史</button>
    </div>
    <div class="casetools">
      <select id="caseSel" title="切换数据集" onchange="loadCase(this.value)"></select>
      <input type="file" id="expFile" accept=".txt" style="display:none">
      <button class="upbtn" title="刷新当前数据集与产物" onclick="refreshAll()">↻ 刷新</button>
      <button class="upbtn" title="上传已填写的参数 CSV 生成 MML 命令" onclick="document.getElementById('csvFile').click()">⚙ 生成命令</button>
      <input type="file" id="csvFile" accept=".csv" style="display:none">
      <button class="upbtn" onclick="document.getElementById('expFile').click()">↑ 上传 EXP</button>
    </div>
  </header>

  <div class="main">
    <aside class="left">
      <div class="l-t" id="leftTitle">特性列表（全部）</div>
      <div class="list" id="featList"></div>
    </aside>
    <section class="main-v">
      <div class="vhead">
        <h2 id="vTitle">选择左侧特性查看详情</h2>
        <span class="meta" id="vMeta"></span>
      </div>
      <div class="vbody" id="vBody"><div class="empty"><span class="big">👆</span>点击特性 / 关联对 / 对象查看详情；<br>任何 EXP 区间可在底部流带定位高亮</div></div>
    </section>
    <div class="chat" id="chat">
      <div class="c-h">
        <b>对话 · EXP 工作台</b>
        <span class="st">桥接 hermes</span>
      </div>
      <div class="msgs" id="chatMsgs"></div>
      <div class="chips" id="chatChips"></div>
      <div class="c-in">
        <input id="chatInput" placeholder="问特性 / 关联 / 配置…（回车发送）" onkeydown="if(event.key==='Enter' && !event.isComposing)sendChat()">
        <button class="go" onclick="sendChat()">→</button>
      </div>
    </div>
  </div>

  <div class="band">
    <div class="bhead">
      <span>命令流带 · <b id="bandCount">0</b> 条命令（EXP 行号 1–2253）</span>
      <span class="legend" id="legend"></span>
    </div>
    <div class="band-scroll" id="bandScroll"><div class="band-inner" id="bandInner"></div></div>
  </div>
  <div class="tip" id="tip"></div>
</div>

<script>
/* 后端模式：数据集经 /api 加载（generate 静态模式由生成器注入 __VIZ_DATA__） */
// __VIZ_DATA__
let DATA = null, CUR_CASE = null;
const $ = s => document.querySelector(s);
const esc = s => (s||'').replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');
const FAM_COLOR = {
  '承载VRF':'#4cc9f0','接口':'#38bdf8','路由BGP':'#818cf8','地址池':'#34d399',
  '计费':'#fbbf24','过滤器':'#f472b6','APN':'#fb923c','license':'#e879f9',
  '系统':'#94a3b8','隧道':'#2dd4bf','BFD':'#f87171','自动缩放':'#a3e635',
  '安全认证':'#c084fc','冗余/合法':'#fda4af','查询':'#475569','其他':'#64748b'
};
const hasData = () => DATA && DATA.cmds;

/* ── 状态 ── */
let curTag = 'all', curView = 'feat', curFeat = null, curRel = null, curObj = null;
let fmap = {};
const rebuildFmap = () => { fmap = {}; DATA.features.forEach(f => fmap[f.fno] = f); };

/* ── 顶栏统计 ── */
function initStats(){
  const c = {strong:0, weak:0, manual:0, none:0};
  DATA.features.forEach(f => c[f.tag] = (c[f.tag] || 0) + 1);
  $('#cStrong').textContent = c.strong; $('#cWeak').textContent = c.weak;
  $('#cManual').textContent = c.manual; $('#cNone').textContent = c.none;
}
document.querySelectorAll('.statbar .st').forEach(b => b.addEventListener('click', ()=>{
  document.querySelectorAll('.statbar .st').forEach(x=>x.classList.remove('on'));
  curTag = b.dataset.tag; b.classList.add('on'); renderFeatList();
}));

/* ── 视图切换 ── */
function setView(v){
  document.querySelectorAll('.viewtabs button').forEach(x=>x.classList.toggle('on', x.dataset.v===v));
  curView = v; curRel = curObj = null;
  if(v === 'obj') renderObjView();
  else if(v === 'rel'){
    $('#vTitle').textContent = '关联视图 · 选择左侧特性查看其强/中关联';
    $('#vMeta').textContent = `${DATA.rels.length} 对（强+中）`;
  }
  else if(v === 'gen'){
    $('#vTitle').textContent = '配置生成 · 选择左侧特性，按三步流程生成配置';
    $('#vMeta').textContent = '骨架版（需后台对接）';
  }
  else if(v === 'files'){
    $('#vTitle').textContent = '中间产物 · 点击左侧文件浏览';
    $('#vMeta').textContent = '';
    renderFileTree();
    return;
  }
  else if(v === 'hist'){
    $('#vTitle').textContent = '任务历史 · 对话与生成操作记录（最新在前）';
    $('#vMeta').textContent = '';
    renderHistList();
    return;
  }
  renderFeatList();
}
document.querySelectorAll('.viewtabs button').forEach(b => b.addEventListener('click', ()=> setView(b.dataset.v)));

/* ── 左栏列表 ── */
function renderFeatList(){
  const box = $('#featList'); box.innerHTML = '';
  let list = DATA.features;
  const q = $('#searchBox').value.trim().toLowerCase();
  if(curTag !== 'all') list = list.filter(f => f.tag === curTag);
  if(q) list = list.filter(f => f.title.toLowerCase().includes(q) || f.fno.toString() === q);
  let title = '特性列表';
  if(curTag !== 'all') title += `（${({strong:'已配置', weak:'弱匹配', manual:'需人工', none:'未配置'})[curTag] || curTag}）`;
  $('#leftTitle').textContent = `${title}（${list.length}）`;
  const L = document.createElement('div');
  list.forEach(f => {
    const el = document.createElement('div');
    el.className = 'fitem' + (curFeat && curFeat.fno === f.fno ? ' on' : '');
    el.innerHTML = `<span class="dot ${f.tag}"></span><span class="no">F${String(f.fno).padStart(3,'0')}</span>` +
      `<span class="tt">${esc(f.title)}</span>` +
      (f.k ? `<span class="kv">${f.k}/${f.n}</span>` : '');
    el.addEventListener('click', ()=>{
      curFeat = f;
      if(curView === 'rel') renderRelDetail(f.title);
      else if(curView === 'obj'){ setView('feat'); renderFeatDetail(f); }
      else if(curView === 'gen') renderGenDetail(f);
      else renderFeatDetail(f);
      renderFeatList();
    });
    L.appendChild(el);
  });
  box.appendChild(L);
}

/* ── 特性详情 ── */
function renderFeatDetail(f){
  $('#vTitle').textContent = `F${String(f.fno).padStart(3,'0')} · ${f.title}`;
  $('#vMeta').textContent = '';
  const tagTxt = {strong:'已配置', weak:'弱匹配', manual:'需人工', none:'未配置'}[f.tag];
  let H = `<div class="card"><div class="c-t"><span class="badge ${f.tag}">${tagTxt}</span><span class="k">匹配</span></div><div class="c-d">`;
  if(f.k){
    H += `exp 匹配 <b>${f.k}/${f.n}</b> 种命令类型（<b>${f.pct}%</b>），${f.matched} 条命令`;
    if(f.key_line) H += `<br>关键命令：${esc(f.key_line)}`;
    if(f.deg_line) H += `<br>判定：${esc(f.deg_line)}`;
  } else {
    H += `本局点未配置此特性：${esc(f.unconf || '文档命令类型与 exp 无交集')}`;
  }
  H += `</div></div>`;
  if(f.paras.length){
    H += `<div class="card"><div class="c-t"><span class="k">EXP 段落</span>（${f.paras.length} 段，点击定位流带）</div><div class="c-d">`;
    f.paras.forEach(p => {
      H += `<div class="para" data-a="${p.a}" data-b="${p.b}"><span class="rng">${p.a}–${p.b}</span>` +
           `<span class="sum">${esc(p.sum)}</span><span class="n">${p.n} 条</span></div>`;
    });
    H += `</div></div>`;
  }
  const objs = DATA.objects.filter(o => o.fnos.includes(f.fno));
  if(objs.length){
    H += `<div class="card"><div class="c-t"><span class="k">引用对象</span>（${objs.length}，点击定位）</div><div class="c-d">`;
    H += objs.slice(0,12).map(o =>
      `<span class="para" style="display:inline-flex;margin:2px" data-a="${o.seqs[0]}" data-b="${o.seqs[1]}">` +
      `<span class="rng">${esc(o.p)}</span>&nbsp;<b>${esc(o.v)}</b></span>`).join('');
    H += objs.length > 12 ? ` <span style="color:var(--faint)">等 ${objs.length} 个</span>` : '';
    H += `</div></div>`;
  }
  const rels = DATA.rels.filter(r => r.a === f.title || r.b === f.title);
  if(rels.length){
    H += `<div class="card"><div class="c-t"><span class="k">关联</span>（${rels.length} 对）</div><div class="c-d">`;
    rels.slice(0,10).forEach(r => {
      const other = r.a === f.title ? r.b : r.a;
      H += `<div class="rel-row" data-rel="${esc(other)}"><span class="b">${esc(other)}</span>` +
           `<span class="ob">${r.objs} 对象</span><span class="sc">分 ${r.score}</span></div>`;
    });
    H += `</div></div>`;
  }
  $('#vBody').innerHTML = H;
  $('#vBody').querySelectorAll('.para').forEach(el => el.addEventListener('click', ()=>
    highlightBand(+el.dataset.a, +el.dataset.b)));
  $('#vBody').querySelectorAll('.rel-row').forEach(el => el.addEventListener('click', ()=>{
    curView = 'rel'; document.querySelectorAll('.viewtabs button').forEach(x=>
      x.classList.toggle('on', x.dataset.v==='rel'));
    renderRelDetail(el.dataset.rel);
  }));
}

/* ── 关联视图 ── */
function renderRelDetail(name){
  const f = DATA.features.find(x => x.title === name) || curFeat;
  curFeat = f;
  $('#vTitle').textContent = `关联 · ${name}`;
  const rels = DATA.rels.filter(r => r.a === name || r.b === name);
  let H = `<div class="card"><div class="c-t"><span class="k">强/中关联</span>（${rels.length} 对）</div><div class="c-d">`;
  if(!rels.length) H += `<div class="empty">无强/中关联（仅通用命令共享或未达阈值）</div>`;
  rels.forEach(r => {
    const other = r.a === name ? r.b : r.a;
    H += `<div class="rel-row" data-other="${esc(other)}"><span class="b">${esc(other)}</span>` +
         `<span class="ob">${r.objs} 对象 · ${r.cmds} 命令</span><span class="sc">分 ${r.score}</span></div>`;
  });
  H += `</div></div>`;
  $('#vBody').innerHTML = H;
  $('#vBody').querySelectorAll('.rel-row').forEach(el => el.addEventListener('click', ()=>{
    curFeat = DATA.features.find(x => x.title === el.dataset.other);
    setView('feat'); renderFeatDetail(curFeat); renderFeatList();
  }));
}

/* ── 公共配置视图 ── */
let objFilter = 'all';
function renderObjView(){
  $('#vTitle').textContent = '公共配置对象（被 ≥2 特性引用）';
  $('#vMeta').textContent = `${DATA.objects.length} 个`;
  let H = `<div class="card"><div class="c-t"><span class="k">筛选</span></div><div class="c-d">`;
  H += `<span class="para" style="display:inline-flex;margin:2px;${objFilter==='all'?'border-color:var(--cyan)':''}" data-f="all">全部</span>`;
  ['VRF','APN','接口','地址池','license','过滤器'].forEach(fam => {
    H += `<span class="para" style="display:inline-flex;margin:2px;${objFilter===fam?'border-color:var(--cyan)':''}" data-f="${fam}">${fam}</span>`;
  });
  H += `</div></div>`;
  const list = DATA.objects.filter(o => objFilter==='all' || o.fam === objFilter);
  H += `<div class="card"><div class="c-t"><span class="k">对象表</span>（${list.length}，点击查看 + 流带定位）</div><div class="c-d"><div class="tbl-wrap"><table class="tbl"><tr><th>参数</th><th>对象值</th><th>特性数</th><th>EXP 区间</th><th>命令</th></tr>`;
  list.forEach(o => {
    H += `<tr class="orow" data-a="${o.seqs[0]}" data-b="${o.seqs[1]}"><td><b>${esc(o.p)}</b></td>` +
         `<td>${esc(o.v)}</td><td>${o.fc}</td><td>${o.seqs[0]}–${o.seqs[1]}</td>` +
         `<td>${o.cmds.slice(0,3).join(', ')}${o.cmds.length>3?' …':''}</td></tr>`;
  });
  H += `</table></div></div>`;
  $('#vBody').innerHTML = H;
  $('#vBody').querySelectorAll('.para[data-f]').forEach(el => el.addEventListener('click', ()=>{
    objFilter = el.dataset.f; renderObjView();
  }));
  $('#vBody').querySelectorAll('.orow').forEach(el => el.addEventListener('click', ()=>{
    highlightBand(+el.dataset.a, +el.dataset.b);
  }));
}

/* ── 配置生成工作台（骨架） ── */
function findFile(sub){
  for(const g of DATA.files){
    for(const it of g.items) if(it.n.includes(sub)) return it;
  }
  return null;
}
function renderGenDetail(f){
  $('#vTitle').textContent = `配置生成 · F${String(f.fno).padStart(3,'0')} ${f.title}`;
  $('#vMeta').textContent = '骨架版（需后台对接）';
  const tagTxt = {strong:'已配置', weak:'弱匹配', manual:'需人工', none:'未配置'}[f.tag];
  let H = `<div class="steps">
    <span class="step on"><i>1</i>模板生成</span><span class="step"><i>2</i>确认清单</span><span class="step"><i>3</i>CSV 输出</span>
  </div>`;
  H += `<div class="card"><div class="c-t"><span class="k">步骤 1 · 模板生成</span><span class="badge ${f.tag}">${tagTxt}</span></div><div class="c-d">`;
  H += `基于现网 EXP 预填 + 特性文档补充缺失项（现网值优先，两者不一致时标注差异供审视）。`;
  if(f.paras.length){
    H += `<br><br>本特性现网已配置 <b>${f.paras.length}</b> 段（点击定位流带，作为预填基线）：`;
    f.paras.forEach(p => {
      H += `<div class="para" data-a="${p.a}" data-b="${p.b}"><span class="rng">${p.a}–${p.b}</span>` +
           `<span class="sum">${esc(p.sum)}</span><span class="n">${p.n} 条</span></div>`;
    });
  } else {
    H += `<br><br>现网无对应配置段落，将按特性文档全新建链。`;
  }
  H += `<div class="btn off">生成配置模板</div><div class="hint">骨架版按钮灰显 —— 对接 hermes 后台后由 exp-feature-mapping 实际生成 template.md</div>`;
  H += `</div></div>`;

  const qd = findFile('确认清单');
  if(qd && qd.c){
    H += `<div class="card"><div class="c-t"><span class="k">步骤 2 · 确认清单</span></div><div class="c-d">`;
    H += `生成待确认项清单（填空变体容忍、同题同参数值合并），你编辑文件或对话给意图，应用后回到模板。<br><br><span style="color:var(--faint)">示例产物 · case1.1 双域专网ULCL：</span>`;
    H += `<div style="max-height:260px;overflow-y:auto;margin-top:8px;border:1px solid var(--border);border-radius:8px;padding:10px">` + md2html(qd.c) + `</div>`;
    H += `<div class="btn off">生成确认清单</div></div></div>`;
  }

  const csv = findFile('.csv');
  if(csv && csv.c){
    H += `<div class="card"><div class="c-t"><span class="k">步骤 3 · CSV 参数收集表</span></div><div class="c-d">`;
    H += `JSON 中间结构程序化生成（禁手工拼逗号），供现网执行前参数收集。<br><br><span style="color:var(--faint)">示例产物 · case1.1 双域专网ULCL（可下载）：</span>`;
    H += `<div style="max-height:280px;overflow-y:auto;margin-top:8px;border:1px solid var(--border);border-radius:8px">` + csvTable(csv.c) + `</div>`;
    H += `<div class="btn act" onclick="download('${esc(csv.n)}','${esc(csv.c.replace(/'/g,"\\'").replace(/\n/g,'\\n'))}')">下载 CSV</div>`;
    H += `<div class="btn off">生成 CSV（新特性）</div></div></div>`;
  }
  $('#vBody').innerHTML = H;
  $('#vBody').querySelectorAll('.para').forEach(el => el.addEventListener('click', ()=>
    highlightBand(+el.dataset.a, +el.dataset.b)));
}

/* ── 产物视图 ── */
let fileGroups = null; // {name: {el, collapsed}}
function renderFileTree(){
  const box = $('#featList'); box.innerHTML = '';
  if(!fileGroups) fileGroups = {};
  const L = document.createElement('div');
  DATA.files.forEach(g => {
    const isFeatGroup = g.g.includes('groundtruth');
    const st = fileGroups[g.g] !== undefined ? fileGroups[g.g] : (isFeatGroup ? true : false);
    const gh = document.createElement('div');
    gh.className = 'gh' + (st ? ' collapsed' : '');
    gh.innerHTML = `<span>${esc(g.g)}</span><span class="cnt">${g.items.length}</span>`;
    gh.addEventListener('click', ()=>{
      fileGroups[g.g] = !fileGroups[g.g];
      gh.classList.toggle('collapsed', fileGroups[g.g]);
      wrap.style.display = fileGroups[g.g] ? 'none' : '';
    });
    const wrap = document.createElement('div');
    wrap.style.display = st ? 'none' : '';
    g.items.forEach(it => {
      const el = document.createElement('div');
      el.className = 'gitem' + (curFile === it ? ' on' : '');
      const ic = it.t === 'feat' ? 'F' : (it.t === 'big' ? 'BIG' : it.t.toUpperCase());
      el.innerHTML = `<span class="ic">${ic}</span><span class="nm">${esc(it.n)}</span>` +
        (it.sz > 0 ? `<span class="sz">${(it.sz/1024).toFixed(0)}K</span>` : '');
      el.addEventListener('click', ()=>{
        if(it.t === 'feat' && it.fno){
          curFeat = fmap[it.fno] || null;
          setView('feat'); renderFeatDetail(curFeat); renderFeatList(); return;
        }
        curFile = it; renderFileDetail(it); renderFileTree();
      });
      wrap.appendChild(el);
    });
    L.appendChild(gh); L.appendChild(wrap);
  });
  box.appendChild(L);
}
let curFile = null;
function renderFileDetail(it){
  $('#vTitle').textContent = it.n;
  $('#vMeta').textContent = `${(it.sz/1024).toFixed(1)} KB · ${it.t.toUpperCase()}`;
  const box = $('#vBody');
  if(it.t === 'big'){
    box.innerHTML = `<div class="card"><div class="c-t"><span class="k">文件过大</span></div><div class="c-d">` +
      `${(it.sz/1024/1024).toFixed(1)} MB 未内嵌。静态单文件版仅注入 ≤500KB 的中间产物；<br>` +
      `对接 hermes 后台后经 /api/files 白名单目录实时浏览（动态版）。</div></div>`;
    return;
  }
  if(it.t === 'md'){
    box.innerHTML = `<div class="card"><div class="file-meta">${esc(it.n)}</div><div class="md">` + md2html(it.c) + `</div></div>`;
  } else if(it.t === 'csv'){
    box.innerHTML = `<div class="card"><div class="file-meta">${esc(it.n)}` +
      ` <span class="dlbtn" onclick="download('${esc(it.n)}','${esc(it.c.replace(/'/g,"\\'").replace(/\n/g,'\\n'))}')">下载 CSV</span></div>` +
      csvTable(it.c) + `<div class="csv-note">CSV 由 JSON 中间结构程序化生成，请勿手工编辑逗号/引号</div></div>`;
  } else {
    box.innerHTML = `<div class="card"><div class="file-meta">${esc(it.n)}</div><pre class="md" style="white-space:pre-wrap;overflow-x:auto">` + esc(it.c) + `</pre></div>`;
  }
}
function download(name, text){
  const a = document.createElement('a');
  a.href = URL.createObjectURL(new Blob([text], {type:'text/csv;charset=utf-8'}));
  a.download = name; a.click();
  setTimeout(()=>URL.revokeObjectURL(a.href), 3000);
}

/* ── markdown 简易渲染 ── */
function mdInline(s){
  return esc(s).replace(/\*\*(.+?)\*\*/g,'<b>$1</b>').replace(/`([^`]+)`/g,'<code>$1</code>');
}
function md2html(txt){
  const lines = txt.split(/\r?\n/);
  let html = '', inCode = false, codeBuf = [], tblBuf = [], inList = false;
  const closeList = ()=>{ if(inList){ html += '</ul>'; inList = false; } };
  const flushTbl = ()=>{
    if(!tblBuf.length) return;
    const rows = tblBuf.filter(r => !/^\s*\|?[\s\-:|]+\|?\s*$/.test(r) || r.includes('---'));
    const real = rows.filter(r => !/^\s*\|[\s\-:|]+\|?\s*$/.test(r));
    if(real.length){
      html += '<table>' + real.map((r,i)=>{
        const cells = r.trim().replace(/^\||\|$/g,'').split('|').map(c=>c.trim());
        return '<tr>' + cells.map(c => `<${i===0?'th':'td'}>${mdInline(c)}</${i===0?'th':'td'}>`).join('') + '</tr>';
      }).join('') + '</table>';
    }
    tblBuf = [];
  };
  for(const ln of lines){
    const t = ln.trim();
    if(t.startsWith('```')){
      flushTbl(); closeList();
      if(inCode) html += `<pre>${esc(codeBuf.join('\n'))}</pre>`;
      inCode = !inCode; codeBuf = []; continue;
    }
    if(inCode){ codeBuf.push(ln); continue; }
    if(t.startsWith('|')){ tblBuf.push(ln); continue; }
    flushTbl();
    if(/^#{1,4}\s/.test(t)){
      closeList();
      const lvl = t.match(/^#+/)[0].length;
      html += `<h${Math.min(lvl,3)}>${mdInline(t.replace(/^#+\s*/,''))}</h${Math.min(lvl,3)}>`;
    } else if(t.startsWith('>')){
      closeList();
      html += `<blockquote>${mdInline(t.replace(/^>\s?/,''))}</blockquote>`;
    } else if(/^[-*]\s/.test(t)){
      if(!inList){ html += '<ul>'; inList = true; }
      html += `<li>${mdInline(t.replace(/^[-*]\s/,''))}</li>`;
    } else if(/^\d+\.\s/.test(t)){
      closeList(); html += `<p>${mdInline(t)}</p>`;
    } else if(t === ''){
      closeList();
    } else {
      closeList(); html += `<p>${mdInline(t)}</p>`;
    }
  }
  flushTbl(); closeList();
  if(inCode) html += `<pre>${esc(codeBuf.join('\n'))}</pre>`;
  return html;
}
function csvTable(csv){
  const rows = csv.replace(/^\uFEFF/,'').split(/\r?\n/).filter(r => r.trim());
  const grid = rows.map(r => {
    // 简单解析（本 CSV 由程序生成，无引号内逗号）
    return r.split(',').map(c => c.replace(/^"|"$/g,''));
  });
  return '<table class="tbl" style="width:100%">' + grid.map((r,i)=>
    '<tr>' + r.map(c => `<${i===0?'th':'td'}>${esc(c)}</${i===0?'th':'td'}>`).join('') + '</tr>'
  ).join('') + '</table>';
}

/* ── 命令流带 ── */
const W = 2.5;
function renderBand(){
  const inner = $('#bandInner');
  inner.style.width = (DATA.cmds.length * W + 20) + 'px';
  inner.innerHTML = '';
  const frag = document.createDocumentFragment();
  DATA.cmds.forEach(c => {
    const d = document.createElement('div');
    d.className = 'cmd';
    d.style.left = (c.seq * W) + 'px';
    d.style.height = '38px';
    d.style.background = FAM_COLOR[c.fam] || FAM_COLOR['其他'];
    d.dataset.seq = c.seq;
    frag.appendChild(d);
  });
  inner.appendChild(frag);
  $('#bandCount').textContent = DATA.cmds.length;
  const lg = $('#legend');
  Object.entries(FAM_COLOR).forEach(([k,v]) => {
    if(k==='其他') return;
    lg.insertAdjacentHTML('beforeend', `<span class="lg"><i style="background:${v}"></i>${k}</span>`);
  });
  /* 悬浮 */
  inner.addEventListener('mousemove', e => {
    const d = e.target.closest('.cmd');
    if(!d){ $('#tip').style.display='none'; return; }
    const c = DATA.cmds[+d.dataset.seq - 1];
    const tip = $('#tip');
    tip.innerHTML = `<span class="t-cmd">${c.seq} · ${esc(c.cmd)}</span><div class="t-kp">${esc(c.kp)}</div>`;
    tip.style.display = 'block';
    tip.style.left = Math.min(e.clientX + 14, innerWidth - 540) + 'px';
    tip.style.top = (e.clientY - 90) + 'px';
  });
  inner.addEventListener('mouseleave', ()=>{ $('#tip').style.display='none'; });
}
let hlEl = null;
function highlightBand(a, b){
  const scroll = $('#bandScroll');
  const target = a * W;
  scroll.scrollLeft = Math.max(0, target - 200);
  if(hlEl) hlEl.remove();
  hlEl = document.createElement('div');
  hlEl.className = 'band-hl';
  hlEl.style.left = (a * W - 1) + 'px';
  hlEl.style.width = Math.max((b - a) * W + 6, 6) + 'px';
  $('#bandInner').appendChild(hlEl);
  setTimeout(()=>{ if(hlEl) hlEl.remove(); }, 4000);
}

/* ── 搜索联动 ── */
$('#searchBox').addEventListener('input', ()=>{
  const q = $('#searchBox').value.trim().toLowerCase();
  if(curView === 'feat') renderFeatList();
  else if(curView === 'obj') renderObjView();
});

/* ── 对话栏（常驻） ── */
let chatHist = [];  // 本会话多轮历史（注入 hermes prompt 维持上下文）
function initChat(){
  chatHist = [];
  const msgs = $('#chatMsgs');
  msgs.innerHTML = `<div class="msg bot">👋 对当前数据集（${esc(CUR_CASE||'')}）提问。<b>本地规则</b>：F 编号跳转 / 对象定位 / 区间高亮；<b>其余问题</b>转发 hermes 后台推理（特性映射、关联证据、公共对象影响面、配置生成）。</div>`;
  const chips = [
    'F003 有哪些配置段落？', 'CBN_GRE 被哪些特性引用？',
    '定位 160–285', '弱匹配的特性有哪些？'
  ];
  $('#chatChips').innerHTML = chips.map(c => `<span class="chip" onclick="ask('${esc(c)}')">${esc(c)}</span>`).join('');
}
function ask(q){ $('#chatInput').value = q; sendChat(); }
function pushMsg(html, who){
  const d = document.createElement('div');
  d.className = 'msg ' + who; d.innerHTML = html;
  $('#chatMsgs').appendChild(d);
  $('#chatMsgs').scrollTop = 1e9;
}
async function sendChat(){
  const inp = $('#chatInput');
  const q = inp.value.trim();
  if(!q) return;
  pushMsg(esc(q), 'user'); inp.value = '';

  /* ── 本地规则（骨架演示） ── */
  let m = q.match(/F0*(\d{1,4})/i);
  if(m){
    const f = DATA.features.find(x => x.fno === +m[1]);
    if(f){
      setView('feat'); renderFeatDetail(f); renderFeatList(); curFeat = f;
      let html = `已打开 <b>F${String(f.fno).padStart(3,'0')} · ${esc(f.title)}</b><br>档位：${({strong:'已配置', weak:'弱匹配', manual:'需人工', none:'未配置'})[f.tag] || f.tag}`;
      if(f.paras.length){
        const p = f.paras[0];
        html += `<br>首个段落 ${p.a}–${p.b}（${p.n} 条）已定位流带`;
        setTimeout(()=>highlightBand(p.a, p.b), 300);
      }
      pushMsg(html, 'bot'); return;
    }
  }
  m = q.match(/(\d+)\s*[-–—]\s*(\d+)/);
  if(m){
    highlightBand(+m[1], +m[2]);
    pushMsg(`已定位 EXP 区间 <b>${m[1]}–${m[2]}</b>（流带金色高亮）`, 'bot'); return;
  }
  const obj = DATA.objects.find(o => q.includes(o.v) && o.v.length >= 4);
  if(obj){
    highlightBand(obj.seqs[0], obj.seqs[1]);
    pushMsg(`对象 <b>${esc(obj.p)}=${esc(obj.v)}</b> 被 <b>${obj.fc}</b> 个特性引用` +
      `<br>命令区间 ${obj.seqs[0]}–${obj.seqs[1]}（${obj.cmds.length} 种命令）已定位流带` +
      `<br><span class="l" onclick="setView('obj');renderObjView()">→ 打开公共配置视图</span>`, 'bot');
    return;
  }
  if(q.includes('弱匹配')){
    const ws = DATA.features.filter(f => f.tag === 'weak').slice(0, 10);
    pushMsg(`弱匹配共 <b>${DATA.features.filter(f=>f.tag==='weak').length}</b> 篇（有对应命令但未达强判标准），示例：<br>` +
      ws.map(f => `F${String(f.fno).padStart(3,'0')} ${esc(f.title)}`).join('<br>') +
      `<br><span class="l" onclick="document.querySelector('.statbar .st.weak').click()">→ 过滤弱匹配列表</span>`, 'bot');
    return;
  }
  /* ── 后端对话（hermes 桥） ── */
  chatHist.push({role: 'user', content: q});
  pushMsg('⏳ 分析中…', 'bot');
  try{
    const r = await fetch('/api/chat', {method:'POST', headers:{'Content-Type':'application/json'},
      body: JSON.stringify({case: CUR_CASE, question: q, history: chatHist.slice(-8)})});
    const res = await r.json();
    $('#chatMsgs').lastChild.remove();
    const reply = res.reply || res.error || '无回复';
    chatHist.push({role: 'assistant', content: reply});
    let h = md2html(reply);
    if(res.artifacts && res.artifacts.length){
      h += `<div class="artrow">` + res.artifacts.map(a =>
        `<span class="artbtn" data-p="${a.path}">📄 ${esc(a.name)}</span>`).join('') + `</div>`;
    }
    pushMsg(h, 'bot');
  }catch(e){
    $('#chatMsgs').lastChild.remove();
    pushMsg('对话服务错误：' + esc(e.message), 'bot');
  }
}

/* ── 数据集加载 / 切换 / 上传 ── */
async function loadCases(){
  const r = await fetch('/api/cases');
  const cases = await r.json();
  const sel = $('#caseSel');
  sel.innerHTML = cases.map(c =>
    `<option value="${c.id}">${c.id}${c.status==='analyzing'?' ⏳':(c.status==='partial'?' ◐':'')}</option>`).join('');
  if(cases.length) await loadCase(cases[0].id);
  else $('#vBody').innerHTML = '<div class="empty"><span class="big">📄</span>无数据集<br>点右上角「↑ 上传 EXP」开始</div>';
}
async function loadCase(id){
  if(!id) return;
  CUR_CASE = id;
  const r = await fetch(`/api/case/${id}/viz`);
  if(!r.ok){ $('#vBody').innerHTML = '<div class="empty">数据集加载失败：' + esc(r.status) + '</div>'; return; }
  DATA = await r.json();
  rebuildFmap();
  curFeat = null; curFile = null; curTag = 'all'; curRel = null; curObj = null;
  fileGroups = null; objFilter = 'all';
  $('#caseSel').value = id;
  $('#vTitle').textContent = `数据集 ${id}`;
  $('#vMeta').textContent = `${DATA.cmds.length} 条命令`;
  initStats(); renderBand(); initChat();
  setView('feat');
}
async function uploadExp(){
  const inp = document.getElementById('expFile');
  if(!inp.files.length) return;
  const name = inp.files[0].name;
  pushMsg(`上传 <b>${esc(name)}</b> 并触发分析管线…`, 'user');
  const fd = new FormData(); fd.append('file', inp.files[0]);
  const r = await fetch('/api/upload', {method:'POST', body: fd});
  if(!r.ok){ pushMsg('上传失败：' + esc(await r.text()), 'bot'); inp.value=''; return; }
  const res = await r.json();
  pushMsg(`✅ 已上传 <b>${esc(name)}</b> → 数据集 <b>${res.case_id}</b><br>` +
    `特性对照 + 关联分析后台运行（约 2–4 分钟），完成后下拉框该条目 ⏳ 消失即可切换。<br>` +
    `<span class="l" onclick="loadCases()">→ 刷新数据集列表</span>`, 'bot');
  inp.value = '';
  loadCases();
}
document.getElementById('expFile').addEventListener('change', uploadExp);

/* ── 刷新（重拉当前数据集 + 产物，不清对话） ── */
async function refreshAll(){
  if(!CUR_CASE) return;
  const id = CUR_CASE;
  pushMsg('↻ 刷新数据集与产物…', 'user');
  try{
    const rc = await fetch('/api/cases');
    const cases = await rc.json();
    $('#caseSel').innerHTML = cases.map(c =>
      `<option value="${c.id}">${c.id}${c.status==='analyzing'?' ⏳':(c.status==='partial'?' ◐':'')}</option>`).join('');
    const st = cases.find(c => c.id === id);
    if(!st){
      pushMsg(`数据集 <b>${esc(id)}</b> 已不存在`, 'bot');
      if(cases.length) loadCase(cases[0].id);
      return;
    }
    const r = await fetch(`/api/case/${id}/viz`);
    if(!r.ok){ pushMsg('刷新失败：' + esc(r.status), 'bot'); return; }
    DATA = await r.json();
    rebuildFmap();
    fileGroups = null;
    $('#caseSel').value = id;
    $('#vMeta').textContent = `${DATA.cmds.length} 条命令`;
    initStats(); renderBand();
    if(curView === 'files') renderFileTree();
    else if(curView === 'obj') renderObjView();
    else if(curView === 'feat'){ renderFeatList(); renderFeatDetail(curFeat); }
    pushMsg(`✅ 已刷新 <b>${esc(id)}</b>${st.status==='analyzing'?'（分析中 ⏳）':''} · ${DATA.cmds.length} 条命令 · 产物已同步`, 'bot');
  }catch(e){ pushMsg('刷新异常：' + esc(e.message), 'bot'); }
}

/* ── 上传已填 CSV → 生成 MML 命令 ── */
async function genCommands(){
  const inp = document.getElementById('csvFile');
  if(!inp.files.length) return;
  const f = inp.files[0];
  pushMsg(`上传已填 CSV <b>${esc(f.name)}</b> 生成命令…`, 'user');
  const fd = new FormData();
  fd.append('file', f);
  fd.append('case', CUR_CASE);
  try{
    const r = await fetch('/api/gen-commands', {method:'POST', body: fd});
    const res = await r.json();
    if(!r.ok){ pushMsg('生成失败：' + esc(res.detail || res.error || r.status), 'bot'); inp.value=''; return; }
    let html = `✅ 生成 <b>${res.count}</b> 条命令` +
      (res.skipped ? `（跳过未填写 ${res.skipped} 项）` : '') +
      ` · 已保存 <code>${esc(res.name)}</code>`;
    if(res.artifacts && res.artifacts.length){
      html += `<div class="artrow">` +
        res.artifacts.map(a=>`<span class="artbtn" data-p="${a.path}">📄 ${esc(a.name)}</span>`).join('') + `</div>`;
    }
    html += `<pre style="max-height:280px;overflow:auto;font-size:10px;line-height:1.5;background:var(--panel);border:1px solid var(--border2);border-radius:8px;padding:8px;white-space:pre-wrap">${esc(res.text)}</pre>`;
    pushMsg(html, 'bot');
  }catch(e){ pushMsg('生成异常：' + esc(e.message), 'bot'); }
  inp.value = '';
}
document.getElementById('csvFile').addEventListener('change', genCommands);

/* ── 历史记录视图 ── */
async function renderHistList(){
  const box = $('#featList');
  $('#leftTitle').textContent = '任务历史（最新在前）';
  box.innerHTML = '<div class="hint">加载中…</div>';
  try{
    const r = await fetch('/api/history?limit=100');
    const list = await r.json();
    if(!list || !list.length){
      box.innerHTML = '<div class="hint">暂无历史记录。<br>对话或生成命令后自动记录。</div>';
      return;
    }
    const L = document.createElement('div');
    list.forEach(h => {
      const el = document.createElement('div');
      el.className = 'fitem';
      el.innerHTML = `<span class="dot ${h.status==='done'?'strong':'none'}"></span>` +
        `<span class="no">${esc((h.ts||'').slice(5,16))}</span>` +
        `<span class="tt">${esc(h.question)}</span>` +
        (h.n_art ? `<span class="kv">${h.n_art}📄</span>` : '');
      el.addEventListener('click', ()=> renderHistDetail(h.id));
      L.appendChild(el);
    });
    box.innerHTML = ''; box.appendChild(L);
  }catch(e){ box.innerHTML = '<div class="hint">加载失败：' + esc(e.message) + '</div>'; }
}
async function renderHistDetail(id){
  try{
    const r = await fetch('/api/history/' + encodeURIComponent(id));
    if(!r.ok){ $('#vBody').innerHTML = '<div class="empty">记录不存在</div>'; return; }
    const h = await r.json();
    $('#vTitle').textContent = `${h.ts} · ${h.case || '无数据集'}`;
    $('#vMeta').textContent = h.status === 'done' ? '完成' : (h.status === 'timeout' ? '超时' : (h.status || h.status === 'error' ? '失败' : h.status));
    let html = `<div class="card"><div class="c-t"><span class="k">问题</span></div><div class="c-d">${esc(h.question)}</div></div>`;
    html += `<div class="card"><div class="c-t"><span class="k">回复</span></div><div class="c-d">${md2html(h.reply || '（无输出）')}</div></div>`;
    if(h.artifacts && h.artifacts.length){
      html += `<div class="card"><div class="c-t"><span class="k">产物（${h.artifacts.length}）</span></div><div class="c-d">` +
        h.artifacts.map(a=>`<span class="artbtn" data-p="${a.path}">📄 ${esc(a.name || a)}</span>`).join('') + `</div></div>`;
    }
    $('#vBody').innerHTML = html;
  }catch(e){ $('#vBody').innerHTML = '<div class="empty">加载失败：' + esc(e.message) + '</div>'; }
}
if(!window.__vBodyDelegate){
  window.__vBodyDelegate = true;
  $('#vBody').addEventListener('click', (ev)=>{
    const b = ev.target.closest('.artbtn');
    if(b && b.dataset.p) openArtifact(b.dataset.p);
  });
}

/* ── 对话产物直达浏览 ── */
async function openArtifact(path){
  try{
    const r = await fetch('/api/artifact?path=' + encodeURIComponent(path));
    if(!r.ok){ pushMsg('产物加载失败：' + esc(await r.text()), 'bot'); return; }
    const art = await r.json();
    const item = {n: art.name, t: art.type, c: art.content, sz: art.size};
    setView('files');
    renderFileDetail(item);
    $('#vTitle').textContent = '对话产物 · ' + art.name;
    $('#vMeta').textContent = `${(art.size/1024).toFixed(1)} KB · ${art.type.toUpperCase()}`;
  }catch(e){
    pushMsg('产物加载异常：' + esc(e.message), 'bot');
  }
}
$('#chatMsgs').addEventListener('click', e => {
  const b = e.target.closest('.artbtn');
  if(b) openArtifact(b.dataset.p);
});

/* ── 初始化 ── */
async function init(){
  if(hasData()){ rebuildFmap(); initStats(); renderBand(); initChat(); renderFeatList(); return; }
  await loadCases();
}
init();
</script>
</body>
</html>
'''


def build_viz_data(exp_path, feat_md_dir, rel_json_path, base_dir=None):
    """构建数据集（生成器与后端共用）：
    exp + F### MD + relations.json → {features, cmds, rels, objects, files, fam_colors}"""
    cmds = parse_exp(exp_path)
    feats = parse_feature_mds(feat_md_dir)
    rel = json.load(open(rel_json_path, encoding='utf-8'))

    # 特性 fno → 标题映射（同标题取第一个）
    title_fno = {}
    for f in feats:
        title_fno.setdefault(f['title'], f['fno'])

    # 关联精简：强+中，标题 → fno，按特性聚合
    rels = []
    for r in rel['relations']:
        if r['strength'] not in ('强', '中'):
            continue
        rels.append({
            'a': r['a'], 'b': r['b'], 'st': r['strength'],
            'score': r['score'], 'objs': len(r['shared_objects']),
            'cmds': len(r['shared_specific_cmds']),
            'co': r['exp_cooccur_paras'],
        })

    # 公共对象（补充 fam 字段 + fnos 列表）
    objects = []
    for o in rel['common_objects']:
        objects.append({
            'p': o['param'], 'v': o['value'], 'fc': o['feature_count'],
            'seqs': o['exp_seqs'], 'cmds': o['cmds'],
            'fam': OBJ_PARAM_FAMILY.get(o['param'], '其他'),
            'fnos': [title_fno.get(t, 0) for t in o['features']],
        })

    data = {
        'features': feats,
        'cmds': cmds,
        'rels': rels,
        'objects': objects,
        'files': collect_files(base_dir or os.path.dirname(os.path.abspath(feat_md_dir))),
        'fam_colors': FAMILY_COLORS,
    }
    return data


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--exp', required=True)
    ap.add_argument('--feat-md', required=True)
    ap.add_argument('--rels', required=True)
    ap.add_argument('-o', '--out', required=True)
    ap.add_argument('--web', action='store_true',
                    help='输出 web 模板（无数据内嵌，前端经 /api 加载数据集）')
    args = ap.parse_args()

    if args.web:
        with open(args.out, 'w', encoding='utf-8') as f:
            f.write(HTML_TEMPLATE)
        print(f'OK → {args.out} (web 模板, 数据经 /api 加载)')
        return

    data = build_viz_data(args.exp, args.feat_md, args.rels)
    html = build_html(data)
    with open(args.out, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f'OK → {args.out}  ({os.path.getsize(args.out)/1024:.0f} KB, '
          f'特性 {len(data["features"])} / 命令 {len(data["cmds"])} / '
          f'关联 {len(data["rels"])} / 对象 {len(data["objects"])})')


if __name__ == '__main__':
    main()

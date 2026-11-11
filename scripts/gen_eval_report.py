#!/usr/bin/env python3
"""生成离线评估报告（单文件 HTML）。

模板：scripts/eval_report_template.html（含 __XXX__ 占位符）
数据源：
  /tmp/eval_2stage_v2_result.json   两阶段评估结果
  /tmp/gt_cleaned.json              GT
  /tmp/exp_quality.json             EXP 质量（GT 族在 EXP 中的覆盖率）
  /tmp/family_cnname.json           族名→中文名
  /tmp/intent_dataset/              意图 + 数据清单
  /tmp/eval_2stage_v2_out/<tk>/     产物
"""
import json
import re
from collections import Counter
from pathlib import Path

BASE = Path('/Users/alesc/workspace/mml-gen-lite')
TEMPLATE = BASE / 'scripts/eval_report_template.html'
HTML_OUT = Path('/tmp/eval_report_final.html')

GT = json.loads(Path('/tmp/gt_cleaned.json').read_text(encoding='utf-8'))
# ★ 2026-11-10：结果 JSON 会被单工单重跑覆盖，改成直接从产物目录构造
#   产物目录 /tmp/eval_2stage_v2_out/<ticket>/ 里有 命令族规划.md 和 mml.txt
RES_PATH = Path('/tmp/eval_2stage_v2_result.json')
_raw_res = json.loads(RES_PATH.read_text(encoding='utf-8')) if RES_PATH.exists() else []

# 从产物目录补全（有产物就当 done）
_seen = {r.get('ticket') for r in _raw_res}
for _d in Path('/tmp/eval_2stage_v2_out').iterdir() if Path('/tmp/eval_2stage_v2_out').exists() else []:
    if not _d.is_dir():
        continue
    _tk = _d.name
    if _tk in _seen:
        continue
    if not (_d / 'mml.txt').exists():
        continue
    _raw_res.append({
        'ticket': _tk,
        's1_status': 'done' if (_d / '命令族规划.md').exists() else None,
        's2_status': 'done',
        's1_sec': 0, 's2_sec': 0,
    })
RES = _raw_res
EXPQ_PATH = Path('/tmp/exp_quality.json')
EXPQ = json.loads(EXPQ_PATH.read_text(encoding='utf-8')) if EXPQ_PATH.exists() else []
INTENT = Path('/tmp/intent_dataset')      # GT 还原意图 + 数据清单（实际输入）
RAW_INTENT = Path('/Users/alesc/workspace/gt-rewrite-samples/86个意图_v5')  # 原始工单意图
ART = Path('/tmp/eval_2stage_v2_out')

GT_MAP = {g['ticket']: g for g in GT}
EXPQ_MAP = {r['tk']: r for r in EXPQ}


TWOSTAGE = Path('/tmp/twostage_stat.json')


def load_text(p):
    return p.read_text(encoding='utf-8', errors='replace') if p.exists() else ''


def parse_fams(text):
    """命令文本 → Counter{族名: 条数}"""
    c = Counter()
    for line in text.split('\n'):
        s = line.split('//')[0].strip()
        if s.startswith('/*') or s.startswith('#'):
            continue
        m = re.match(r'^(ADD|RMV|MOD|SET)\s+([A-Za-z0-9_]+)', s, re.I)
        if m:
            c[m.group(2).upper()] += 1
    return c


def parse_plan_fams(plan_text):
    """从规划表提取族名。

    ★ 2026-11-10 修两个 bug：
      1. 有的规划表没有「状态」列（9 列），硬编码 len(cells)>=10 会全跳过
      2. 命令族列有「ADD TAIGROUP」带动词形式，原正则只认裸族名
    改为：按表头定位列 + 剥动词。
    """
    out = set()
    if not plan_text:
        return out

    lines = plan_text.split('\n')
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if not line.startswith('|'):
            i += 1
            continue
        header = [c.strip() for c in line.strip().strip('|').split('|')]
        if '命令族' not in header:
            i += 1
            continue

        fam_idx = header.index('命令族')
        st_idx = header.index('状态') if '状态' in header else None
        ncol = len(header)

        i += 1
        if i < len(lines) and re.fullmatch(r'[|\s\-:]+', lines[i].strip()):
            i += 1

        while i < len(lines):
            row = lines[i].strip()
            if not row.startswith('|'):
                break
            cells = [c.strip() for c in row.strip().strip('|').split('|')]
            if len(cells) < ncol:
                i += 1
                continue
            status = cells[st_idx] if (st_idx is not None and st_idx < len(cells)) else ''
            if '跳过' in status:
                i += 1
                continue
            fam_cell = cells[fam_idx] if fam_idx < len(cells) else ''
            for part in re.split(r'[/,、]', fam_cell):
                t = part.strip().upper()
                m2 = re.match(r'^(?:ADD|RMV|MOD|SET)\s+([A-Z][A-Z0-9_]{2,})$', t)
                if m2:
                    out.add(m2.group(1))
                elif re.fullmatch(r'[A-Z][A-Z0-9_]{2,}', t):
                    out.add(t)
            i += 1
        continue

    # ★ 2026-11-10：去掉正文兜底正则
    #   原来用 r'`(?:ADD|RMV|MOD|SET)\s+([A-Z]...)' 把正文里提到的族也算进规划，
    #   导致阶段1 覆盖虚高（65.1% vs stat_dual 的 56.8%）。
    #   现在只认规划表里的行，与 scripts/stat_dual.py 口径一致。
    return out


def build_rows():
    rows = []
    for r in RES:
        tk = r['ticket']
        g = GT_MAP.get(tk)
        if not g:
            continue
        # ★ 2026-11-10：跳过没有任何产物的工单（如阶段1 超时的）
        #   否则会把它的 GT 计入分母、产物算 0，拉低整体指标
        if not (ART / tk / 'mml.txt').exists() and not (ART / tk / '命令族规划.md').exists():
            continue
        eq = EXPQ_MAP.get(tk, {})
        gt_fams = Counter(f for _, v, f, p, _ in g['kept'])
        prod_fams = parse_fams(load_text(ART / tk / 'mml.txt'))

        # ★ 2026-11-10 用户裁定：不要「族完备」（可评估族口径），改成「族覆盖」
        #   理由：族完备把「EXP 里没有的族」排除了，
        #        导致 GT 6 族只配对 1 族也显示 100%，看不到真实情况。
        #        族覆盖直接按 GT 全部族算。
        _miss_in_exp = set(eq.get('missing') or [])
        ns_set = set(gt_fams) & _miss_in_exp   # 仅用于展示「无 EXP 支撑」

        prod_bare = set(prod_fams)
        hit = set(gt_fams) & prod_bare          # 命中（GT 全部族口径）
        miss = set(gt_fams) - prod_bare         # 缺失（GT 全部族口径）
        extra = prod_bare - set(gt_fams)        # 多余

        # 阶段1 规划表里的族（算规划召回/精确用）
        plan_fams = parse_plan_fams(load_text(ART / tk / '命令族规划.md'))
        s1_hit = set(gt_fams) & plan_fams

        rows.append({
            'tk': tk,
            'gt_cmds_n': len(g['kept']),
            'gt_fams': dict(gt_fams),
            'no_support_fams': sorted(ns_set),   # 无 EXP 支撑族（仅展示）
            's1_hit_fams': sorted(s1_hit),       # 规划命中族
            's1_plan_fams': sorted(plan_fams),   # 规划表里的族
            'hit_fams': sorted(hit),             # GT 全部族里命中的
            'miss_fams': sorted(miss),           # GT 全部族里缺的
            'extra_fams': sorted(extra),         # 产物多出来的
            # ★ 族覆盖率 = 命中族 / GT 全部族（用户裁定的主指标）
            'fam_cov_rate': round(len(hit) / max(1, len(gt_fams)), 3),
            'gt_cmds': [raw for _, v, f, p, raw in g['kept']],
            'plan': load_text(ART / tk / '命令族规划.md'),
            'mml': load_text(ART / tk / 'mml.txt'),
            'prod_fams': dict(prod_fams),
            'prod_cmds_n': sum(prod_fams.values()),
            'intent': load_text(INTENT / f'{tk}_意图.md'),          # GT 还原（实际输入）
            'raw_intent': load_text(RAW_INTENT / f'{tk}_意图.md'),  # 原始工单意图
            'dataset': load_text(INTENT / f'{tk}_数据清单.md'),
            's1_status': r.get('s1_status'),
            's1_sec': r.get('s1_sec'),
            's1_hit': r.get('s1_hit_n'),
            's1_plan_n': r.get('s1_plan_n'),
            's1_recall': r.get('s1_recall'),
            's1_precision': r.get('s1_precision'),
            's2_status': r.get('s2_status'),
            's2_sec': r.get('s2_sec'),
            's2_hit': r.get('s2_hit_n'),
            's2_fam_rate': r.get('s2_fam_rate'),
            'gt_fams_n': r.get('gt_fams'),
            'no_support': r.get('no_support_fams'),
            's2_fatal': r.get('s2_fatal') or [],
            # ★ 2026-11-10：level 从 GT 命令数算，不依赖 RES 字段
            #   （补全的条目没有 level；且 GT 规模是客观的）
            'level': ('complex' if len(g['kept']) > 200
                      else ('medium' if len(g['kept']) >= 50 else 'simple')),
            'exp_rate': eq.get('rate'),
            'exp_fams_n': eq.get('exp_fams'),
            'exp_missing': eq.get('missing') or [],
            'exp_mb': eq.get('exp_mb'),
        })
    return rows


def load_restricted():
    """数据受限工单（缺 SET/MOD/RMV 所需现网数据）。"""
    p = Path('/tmp/missing_classified.json')
    if not p.exists():
        return set()
    cls = json.loads(p.read_text(encoding='utf-8'))
    return {x['tk'] for x in cls.get('need_data') or []}


def _agg(rows_):
    """聚合一组工单的指标。

    ★ 2026-11-10：分母用「GT 全部族」（len(gt_fams)），不是 gt_fams_n（可评估族）。
      gt_fams_n 来自 GT 记录的 gt_fams 字段（已排除无 EXP 支撑的族），
      会造成「族覆盖」虚高（83.6% vs 实际 66.8%）。
    """
    ev = sum(len(r['gt_fams']) for r in rows_)
    s1 = sum(len(r['s1_hit_fams']) for r in rows_)
    s2 = sum(len(r['hit_fams']) for r in rows_)
    gc = sum(r['gt_cmds_n'] for r in rows_)
    pc = sum(r['prod_cmds_n'] for r in rows_)
    return {'n': len(rows_), 'ev': ev, 's1': s1, 's2': s2, 'gc': gc, 'pc': pc}


def kpi_html(ok):
    """★ 2026-11-10 双口径（用户要求）：
       A 全量：所有工单
       B 排除数据受限：剔除缺 SET/MOD/RMV 现网数据的工单
    """
    restricted = load_restricted()
    ok_b = [r for r in ok if r['tk'] not in restricted]

    A = _agg(ok)
    B = _agg(ok_b)
    pn = sum(len(r['s1_plan_fams']) for r in ok)
    perfect = sum(1 for r in ok if len(r['hit_fams']) == r['gt_fams_n'])
    done = sum(1 for r in ok if r['s2_status'] == 'done')

    items = [
        ('工单总数', len(ok), f'成功 {done}'),

        # ── 口径 A 全量 ──
        ('A. 阶段1 规划覆盖', f'{A["s1"]/max(1,A["ev"])*100:.1f}%',
         f'全量 {A["n"]} 单：{A["s1"]}/{A["ev"]} 族'),
        ('A. 阶段2 产物覆盖', f'{A["s2"]/max(1,A["ev"])*100:.1f}%',
         f'{A["s2"]}/{A["ev"]} 族'),
        ('A. 命令数完成度', f'{A["pc"]/max(1,A["gc"])*100:.0f}%',
         f'{A["pc"]}/{A["gc"]} 条'),

        # ── 口径 B 排除数据受限 ──
        ('B. 阶段1 规划覆盖', f'{B["s1"]/max(1,B["ev"])*100:.1f}%',
         f'排除 {len(restricted)} 单：{B["s1"]}/{B["ev"]} 族'),
        ('B. 阶段2 产物覆盖', f'{B["s2"]/max(1,B["ev"])*100:.1f}%',
         f'{B["s2"]}/{B["ev"]} 族'),
        ('B. 命令数完成度', f'{B["pc"]/max(1,B["gc"])*100:.0f}%',
         f'{B["pc"]}/{B["gc"]} 条'),

        ('阶段1 规划精确', f'{A["s1"]/max(1,pn)*100:.1f}%', f'规划 {pn} 族'),
        ('工单级全覆盖', perfect, '族覆盖 100%'),
    ]
    return ''.join(
        f'<div><div class="l">{a}</div><div class="v">{b}</div><div class="n">{c}</div></div>'
        for a, b, c in items)


def exp_bands_html(ok):
    def cnt(lo, hi=None):
        if hi is None:
            return sum(1 for r in ok if (r['exp_rate'] or 0) < lo)
        return sum(1 for r in ok if lo <= (r['exp_rate'] or 0) < hi)

    bands = [
        ('100%', cnt(1.0), 'GT 所有族都在 EXP 里出现过'),
        ('80-99%', cnt(0.8, 1.0), '少量族不在 EXP'),
        ('50-79%', cnt(0.5, 0.8), '部分族不在 EXP（多为 UNC 侧）'),
        ('<50%', cnt(0.5), '大量族不在 EXP（跨网元或 EXP 不对应）'),
    ]
    return ''.join(
        f'<tr><td>{a}</td><td class="right">{b}</td><td>{c}</td></tr>'
        for a, b, c in bands)


def size_bands_html(ok):
    """★ 2026-11-10 双口径：每档显示「全量」和「排除数据受限」两行。"""
    restricted = load_restricted()
    out = []
    for lv, label in [('simple', '简单 <50'), ('medium', '中等 50-200'),
                      ('complex', '复杂 >200')]:
        sub = [r for r in ok if r['level'] == lv]
        if not sub:
            continue
        sub_b = [r for r in sub if r['tk'] not in restricted]

        A = _agg(sub)
        B = _agg(sub_b)

        # 全量行
        out.append(
            f'<tr><td rowspan="2">{label}</td>'
            f'<td style="font-size:10px;color:#8c959f">全量</td>'
            f'<td class="right">{A["n"]}</td>'
            f'<td class="right">{A["ev"]}</td>'
            f'<td class="right"><b>{A["s1"]/max(1,A["ev"])*100:.1f}%</b></td>'
            f'<td class="right"><b>{A["s2"]/max(1,A["ev"])*100:.1f}%</b></td>'
            f'<td class="right">{A["pc"]/max(1,A["gc"])*100:.0f}%</td>'
            f'<td class="right" style="color:#8c959f">—</td></tr>')

        # 排除数据受限行
        if B['n']:
            d1 = (B['s1']/max(1,B['ev']) - A['s1']/max(1,A['ev'])) * 100
            d2 = (B['s2']/max(1,B['ev']) - A['s2']/max(1,A['ev'])) * 100
            out.append(
                f'<tr style="background:#f6f9fb">'
                f'<td style="font-size:10px;color:#1a7f37">排除受限</td>'
                f'<td class="right">{B["n"]}</td>'
                f'<td class="right">{B["ev"]}</td>'
                f'<td class="right"><b class="good">{B["s1"]/max(1,B["ev"])*100:.1f}%</b></td>'
                f'<td class="right"><b class="good">{B["s2"]/max(1,B["ev"])*100:.1f}%</b></td>'
                f'<td class="right">{B["pc"]/max(1,B["gc"])*100:.0f}%</td>'
                f'<td class="right" style="color:#1a7f37;font-weight:600">'
                f'{d1:+.1f} / {d2:+.1f}</td></tr>')
        else:
            out.append(
                f'<tr style="background:#f6f9fb">'
                f'<td style="font-size:10px;color:#8c959f">排除受限</td>'
                f'<td class="right" colspan="6" style="color:#8c959f">'
                f'本档全部为数据受限工单</td></tr>')
    return ''.join(out)


def main():
    rows = build_rows()
    ok = [r for r in rows if r['s1_status'] and r['s2_status']]

    # ★ 2026-11-10：分母统一用 GT 全部族（不用 gt_fams_n 可评估族）
    ev = sum(len(r['gt_fams']) for r in ok)
    restricted = load_restricted()

    tpl = load_text(TEMPLATE)
    html = (tpl
            .replace('__SUBTITLE__',
                     f'{len(ok)} 工单 · 阶段1 命令族规划 → 阶段2 参数填充 · '
                     f'口径：GT 全部族（双口径：A 全量 / B 排除数据受限）')
            .replace('__KPI__', kpi_html(ok))
            .replace('__SCOPE_NOTE__',
                     f'（双口径）：<b>A 全量</b> = 全部 {len(ok)} 单，'
                     f'GT 族 {ev}；'
                     f'<b>B 排除数据受限</b> = 剔除 {len(restricted)} 个'
                     f'「缺 SET/MOD/RMV 所需现网数据」的工单。'
                     f'ADD 类命令不依赖现网数据，仍计入。')
            .replace('__EXP_BANDS__', exp_bands_html(ok))
            .replace('__SIZE_BANDS__', size_bands_html(ok))
            .replace('__DATA__', json.dumps(rows, ensure_ascii=False)))

    HTML_OUT.write_text(html, encoding='utf-8')
    print(f'✅ 报告: {HTML_OUT}  ({HTML_OUT.stat().st_size // 1024}KB，{len(rows)} 工单)')


if __name__ == '__main__':
    main()

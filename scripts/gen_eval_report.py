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
RES = json.loads(Path('/tmp/eval_2stage_v2_result.json').read_text(encoding='utf-8'))
EXPQ_PATH = Path('/tmp/exp_quality.json')
EXPQ = json.loads(EXPQ_PATH.read_text(encoding='utf-8')) if EXPQ_PATH.exists() else []
INTENT = Path('/tmp/intent_dataset')
ART = Path('/tmp/eval_2stage_v2_out')

GT_MAP = {g['ticket']: g for g in GT}
EXPQ_MAP = {r['tk']: r for r in EXPQ}


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


def build_rows():
    rows = []
    for r in RES:
        tk = r['ticket']
        g = GT_MAP.get(tk)
        if not g:
            continue
        eq = EXPQ_MAP.get(tk, {})
        gt_fams = Counter(f for _, v, f, p, _ in g['kept'])
        prod_fams = parse_fams(load_text(ART / tk / 'mml.txt'))

        rows.append({
            'tk': tk,
            'gt_cmds_n': len(g['kept']),
            'gt_fams': dict(gt_fams),
            'gt_cmds': [raw for _, v, f, p, raw in g['kept']],
            'plan': load_text(ART / tk / '命令族规划.md'),
            'mml': load_text(ART / tk / 'mml.txt'),
            'prod_fams': dict(prod_fams),
            'prod_cmds_n': sum(prod_fams.values()),
            'intent': load_text(INTENT / f'{tk}_意图.md'),
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
            'level': r.get('level'),
            'exp_rate': eq.get('rate'),
            'exp_fams_n': eq.get('exp_fams'),
            'exp_missing': eq.get('missing') or [],
            'exp_mb': eq.get('exp_mb'),
        })
    return rows


def kpi_html(ok):
    ev = sum(r['gt_fams_n'] or 0 for r in ok)
    s1 = sum(r['s1_hit'] or 0 for r in ok)
    s2 = sum(r['s2_hit'] or 0 for r in ok)
    pn = sum(r['s1_plan_n'] or 0 for r in ok)
    gc = sum(r['gt_cmds_n'] for r in ok)
    pc = sum(r['prod_cmds_n'] for r in ok)
    perfect = sum(1 for r in ok if r['s2_hit'] == r['gt_fams_n'])
    done = sum(1 for r in ok if r['s2_status'] == 'done')

    items = [
        ('工单总数', len(ok), f'成功 {done}'),
        ('阶段1 规划召回', f'{s1/max(1,ev)*100:.1f}%', f'{s1}/{ev} 族'),
        ('阶段1 规划精确', f'{s1/max(1,pn)*100:.1f}%', f'规划 {pn} 族'),
        ('阶段2 族完备', f'{s2/max(1,ev)*100:.1f}%', f'{s2}/{ev} 族'),
        ('命令数完成度', f'{pc/max(1,gc)*100:.0f}%', f'{pc}/{gc} 条'),
        ('工单级全对', perfect, '族完备 100%'),
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
    out = []
    for lv, label in [('simple', '简单 <50'), ('medium', '中等 50-200'),
                      ('complex', '复杂 >200')]:
        sub = [r for r in ok if r['level'] == lv]
        if not sub:
            continue
        ev = sum(r['gt_fams_n'] or 0 for r in sub)
        s1 = sum(r['s1_hit'] or 0 for r in sub)
        s2 = sum(r['s2_hit'] or 0 for r in sub)
        gc = sum(r['gt_cmds_n'] for r in sub)
        pc = sum(r['prod_cmds_n'] for r in sub)
        out.append(
            f'<tr><td>{label}</td><td class="right">{len(sub)}</td>'
            f'<td class="right">{ev}</td>'
            f'<td class="right">{s1/max(1,ev)*100:.1f}%</td>'
            f'<td class="right">{s2/max(1,ev)*100:.1f}%</td>'
            f'<td class="right">{pc/max(1,gc)*100:.0f}%</td></tr>')
    return ''.join(out)


def main():
    rows = build_rows()
    ok = [r for r in rows if r['s1_status'] and r['s2_status']]

    ev = sum(r['gt_fams_n'] or 0 for r in ok)
    ns = sum(r['no_support'] or 0 for r in ok)

    tpl = load_text(TEMPLATE)
    html = (tpl
            .replace('__SUBTITLE__',
                     f'{len(ok)} 工单 · 阶段1 命令族规划 → 阶段2 参数填充 · '
                     f'口径：可评估族（扣除无 EXP 支撑的 UNC 族）')
            .replace('__KPI__', kpi_html(ok))
            .replace('__SCOPE_NOTE__',
                     f'：87 工单里 26 个跨 UDG+UNC，但只上传了 UDG 的 EXP。'
                     f'UNC 独有的 {ns} 个族无现网数据支撑，不计入可评估族。'
                     f'可评估族 {ev} / GT 总族 {ev + ns}。')
            .replace('__EXP_BANDS__', exp_bands_html(ok))
            .replace('__SIZE_BANDS__', size_bands_html(ok))
            .replace('__DATA__', json.dumps(rows, ensure_ascii=False)))

    HTML_OUT.write_text(html, encoding='utf-8')
    print(f'✅ 报告: {HTML_OUT}  ({HTML_OUT.stat().st_size // 1024}KB，{len(rows)} 工单)')


if __name__ == '__main__':
    main()

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

    for m in re.finditer(r'`(?:ADD|RMV|MOD|SET)\s+([A-Z][A-Z0-9_]{2,})', plan_text):
        out.add(m.group(1))
    return out


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


def kpi_html(ok):
    ev = sum(r['gt_fams_n'] or 0 for r in ok)
    s1 = sum(len(r['s1_hit_fams']) for r in ok)
    s2 = sum(len(r['hit_fams']) for r in ok)
    pn = sum(len(r['s1_plan_fams']) for r in ok)
    gc = sum(r['gt_cmds_n'] for r in ok)
    pc = sum(r['prod_cmds_n'] for r in ok)
    perfect = sum(1 for r in ok if len(r['hit_fams']) == r['gt_fams_n'])
    done = sum(1 for r in ok if r['s2_status'] == 'done')

    items = [
        ('工单总数', len(ok), f'成功 {done}'),
        ('GT 命令族总数', ev, '全部工单合计'),
        # ★ 2026-11-10 两阶段分开报（用户要求）
        ('阶段1 规划覆盖', f'{s1/max(1,ev)*100:.1f}%', f'{s1}/{ev} 族（数据不全，只看族和逻辑）'),
        ('阶段1 规划精确', f'{s1/max(1,pn)*100:.1f}%', f'规划 {pn} 族'),
        ('阶段2 产物覆盖', f'{s2/max(1,ev)*100:.1f}%', f'{s2}/{ev} 族（补全数据后看细节）'),
        ('阶段损耗', s1 - s2, '规划了但没配出来'),
        ('命令数完成度', f'{pc/max(1,gc)*100:.0f}%', f'{pc}/{gc} 条'),
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
    out = []
    for lv, label in [('simple', '简单 <50'), ('medium', '中等 50-200'),
                      ('complex', '复杂 >200')]:
        sub = [r for r in ok if r['level'] == lv]
        if not sub:
            continue
        ev = sum(r['gt_fams_n'] or 0 for r in sub)
        # ★ 两阶段分开（用户要求）
        s1 = sum(len(r['s1_hit_fams']) for r in sub)
        s2 = sum(len(r['hit_fams']) for r in sub)
        gc = sum(r['gt_cmds_n'] for r in sub)
        pc = sum(r['prod_cmds_n'] for r in sub)
        loss = s1 - s2
        out.append(
            f'<tr><td>{label}</td><td class="right">{len(sub)}</td>'
            f'<td class="right">{ev}</td>'
            f'<td class="right"><b>{s1/max(1,ev)*100:.1f}%</b></td>'
            f'<td class="right"><b>{s2/max(1,ev)*100:.1f}%</b></td>'
            f'<td class="right">{loss:+d}</td>'
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

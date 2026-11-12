"""G31：规划表的「命令族」列用了通配或数量概括。

★ 2026-11-12 新增（实测问题）

问题：
  阶段1 的 agent 有时会用一行概括多个族：
      | 2 | ... | ADD APN + SET APN*（UNC）        | 新增 |   ← 通配
      | 3 | ... | SET APNxxx 属性族 25 个           | 新增 |   ← 数量概括
  但阶段2 拿到的就是这张表，它要么自己猜有哪些族（容易漏），
  要么按「不要在规划之外增加命令族」的规则保守处理（只配 APN 本体）。

  实测 NC20260810002261：
    规划表 11 行（用 SET APN* 概括 25 个属性族）
    → 阶段2 只配了 APN 本体 → 那 25 个族全丢

判据：
  扫描规划表的「命令族」列，出现下列形态即报：
    · 族名带 *                    （SET APN*）
    · 「N 个」/「N 条」/「等 N」    （SET APNxxx 属性族 25 个）
    · 「xxx」（占位式写法）          （SET APNxxx）
    · 「...」/「等」（省略号）

级别 warn（不阻断，但要提示 agent 展开）。

可单独运行自检：
  python3 workflow/guard/plan_wildcard.py --session-dir <dir>
"""
import re
import sys
from pathlib import Path


# 通配/概括的识别模式
#
# ★ 2026-11-12 修正误报（实测 NC20260810002261 的规划表）
#   误报：把「族名 + 现网条数」当成「数量概括」
#     第 5 行 PNFDNN（UNC，732 条，DNN=ims.wh 有 24 条）   ← 正常写法
#     第14 行 POOLGROUP（UDG，659 条）                     ← 正常写法
#     50 行里误报 32 行，真问题只有 1 行
#
#   规则修正：
#     · 「N 条」只描述现网行数，不算概括 → 不再作为通配依据
#     · 「N 个」要看后面跟的是什么：
#          「46 个族」「25 个属性族」→ 是概括（一族未列）
#          「190 个对象」「2 行」    → 是数量说明，正常
#       所以「N 个」只在紧跟「族」字时才算通配
#     · 「等 N 个」保留（明确表示省略）
WILDCARD_PATTERNS = [
    (re.compile(r'[A-Z][A-Z0-9_]{2,}\s*\*'), '族名带通配符 *'),
    (re.compile(r'\d+\s*个\s*族'), '用「N 个族」概括（族未逐个列出）'),
    (re.compile(r'属性族\s*\d+\s*个'), '用「属性族 N 个」概括'),
    (re.compile(r'等\s*\d+\s*个'), '用「等 N 个」省略'),
    (re.compile(r'等\s*[A-Z]'), '用「等」省略族名'),
    (re.compile(r'[A-Z][A-Z0-9_]{2,}xxx', re.I), '用 xxx 占位'),
    (re.compile(r'\.\.\.|…'), '用省略号'),
]

# 一行里如果列了多个具体族，是允许的（用 / 、 , 分隔）
MULTI_FAM_SEP = re.compile(r'[/、,]')


def parse_plan_rows(text):
    """解析规划表，返回 [{row_no, fam_cell, status, raw}]。"""
    rows = []
    lines = text.split('\n')
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
        fi = header.index('命令族')
        si = header.index('状态') if '状态' in header else None
        ri = header.index('#') if '#' in header else 0
        ncol = len(header)
        i += 1
        if i < len(lines) and re.fullmatch(r'[|\s\-:]+', lines[i].strip()):
            i += 1
        while i < len(lines):
            row = lines[i].strip()
            if not row.startswith('|'):
                break
            cells = [c.strip() for c in row.strip().strip('|').split('|')]
            if len(cells) >= ncol:
                rows.append({
                    'row_no': cells[ri] if ri < len(cells) else '?',
                    'fam_cell': cells[fi],
                    'status': (cells[si] if (si is not None and si < ncol) else ''),
                    'raw': row,
                })
            i += 1
        continue
    return rows


def check_plan_wildcard(sess_dir=None, plan_path=None):
    """扫描规划表，找出用通配/概括的行。

    返回：
      {'ok': bool, 'skipped': bool, 'reason': str, 'hits': [...]}
    ok=True  表示没发现通配（或跳过的行）
    """
    if plan_path:
        p = Path(plan_path)
    elif sess_dir:
        p = Path(sess_dir) / 'analysis_code' / '命令族规划.md'
        if not p.exists():
            p = Path(sess_dir) / '命令族规划.md'
    else:
        return {'ok': True, 'skipped': True, 'reason': '无 session_dir / plan_path'}

    if not p.exists():
        return {'ok': True, 'skipped': True, 'reason': f'规划表不存在: {p}'}

    try:
        text = p.read_text(encoding='utf-8', errors='replace')
    except Exception as e:
        return {'ok': True, 'skipped': True, 'reason': f'读取失败: {e}'}

    rows = parse_plan_rows(text)
    if not rows:
        return {'ok': True, 'skipped': True, 'reason': '规划表里没有解析出表格行'}

    hits = []
    for r in rows:
        # 跳过的行不检查（本来就不配）
        if '跳过' in r['status']:
            continue
        cell = r['fam_cell']
        if not cell:
            continue
        # 一行列多个具体族是允许的，先按分隔符拆，再逐段检查
        segs = MULTI_FAM_SEP.split(cell) if MULTI_FAM_SEP.search(cell) else [cell]
        bad_reasons = []
        for seg in segs:
            seg = seg.strip()
            if not seg:
                continue
            for pat, why in WILDCARD_PATTERNS:
                if pat.search(seg):
                    bad_reasons.append(why)
                    break
        if bad_reasons:
            hits.append({
                'row': r['row_no'],
                'fam_cell': cell[:100],
                'reasons': sorted(set(bad_reasons)),
            })

    return {
        'ok': len(hits) == 0,
        'skipped': False,
        'n_rows': len(rows),
        'n_hits': len(hits),
        'hits': hits,
    }


def main():
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument('--session-dir', default='')
    ap.add_argument('--plan', default='')
    args = ap.parse_args()

    r = check_plan_wildcard(sess_dir=args.session_dir or None,
                            plan_path=args.plan or None)
    if r.get('skipped'):
        print(f'跳过: {r.get("reason")}')
        return 0
    if r['ok']:
        print(f'✅ 无通配（检查了 {r["n_rows"]} 行）')
        return 0
    print(f'⚠ {r["n_hits"]} 行用了通配/概括（共 {r["n_rows"]} 行）：')
    for h in r['hits']:
        print(f'  第 {h["row"]} 行: {h["fam_cell"]}')
        print(f'      原因: {", ".join(h["reasons"])}')
    return 1


if __name__ == '__main__':
    sys.exit(main())

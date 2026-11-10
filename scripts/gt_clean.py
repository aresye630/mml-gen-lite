#!/usr/bin/env python3
"""GT 清洗：剔除「ADD 的对象在 EXP 里已存在且参数完全一致」的噪音命令。

用户裁定（2026-11-10）：
  NC20260803001614 这类工单，GT 里混入了重复 ADD
  （如 ADD HOST 12 条，EXP 里已存在且值完全一致），
  评估侧应该先清洗，否则 agent 判断「已存在不重复配」反而是对的却被算错。

判定规则：
  1. GT 命令是 ADD
  2. 同一条命令（去掉空格差异）在 EXP 里能找到完全相同的 ADD
  → 判定为「重复 ADD 噪音」，剔除

  注意：只剔除「完全相同」的，不复用 object-level 比对
       （主键相同但参数不同 → 那是真实的 MOD 需求，不能剔）
"""
import argparse
import json
import re
from pathlib import Path

BASE = Path('/Users/alesc/workspace/udg-multi/UDG_01/UDG_01/UDG_01/UDG')


def norm(cmd):
    """规范化命令，用于「完全一致」比对。

    去掉多余空格、结尾分号；保留参数顺序和值。
    """
    s = re.sub(r'\s+', ' ', cmd.strip())
    s = s.rstrip(';').strip()
    return s


def load_exp_cmds(tk):
    """加载一个工单的 EXP 里所有 ADD 命令（规范化）。"""
    d = BASE / tk / '备份附件'
    if not d.exists():
        return set()
    out = set()
    for p in d.glob('*EXPMML*'):
        try:
            txt = p.read_text(encoding='utf-8', errors='replace')
        except Exception:
            continue
        for line in txt.split('\n'):
            s = line.strip()
            if not s.upper().startswith('ADD '):
                continue
            out.add(norm(s))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--gt', default='/tmp/gt_cleaned.json')
    ap.add_argument('--out', default='/tmp/gt_clean2.json')
    ap.add_argument('--report', default='/tmp/gt_clean_report.json')
    args = ap.parse_args()

    GT = json.loads(Path(args.gt).read_text(encoding='utf-8'))

    report = []
    total_before = total_after = 0
    cleaned_gt = []

    for g in GT:
        tk = g['ticket']
        exp_adds = load_exp_cmds(tk)

        kept = []
        dropped = []
        for item in g['kept']:
            ln, verb, fam, params, raw = item
            total_before += 1
            if verb == 'ADD' and exp_adds and norm(raw) in exp_adds:
                dropped.append(raw)
                continue
            kept.append(item)
            total_after += 1

        cleaned_gt.append({**g, 'kept': kept})
        if dropped:
            report.append({
                'ticket': tk,
                'n_dropped': len(dropped),
                'n_total': len(g['kept']),
                'samples': dropped[:3],
            })

    Path(args.out).write_text(json.dumps(cleaned_gt, ensure_ascii=False, indent=1),
                              encoding='utf-8')
    Path(args.report).write_text(json.dumps(report, ensure_ascii=False, indent=1),
                                 encoding='utf-8')

    print(f"=== GT 清洗结果 ===")
    print(f"  清洗前: {total_before} 条")
    print(f"  剔除:   {total_before - total_after} 条（{(total_before-total_after)/max(1,total_before)*100:.1f}%）")
    print(f"  清洗后: {total_after} 条")
    print(f"  受影响工单: {len(report)} 个")

    if report:
        print(f"\n  {'工单':<22} {'剔除':>4} {'原计':>4}")
        for r in sorted(report, key=lambda x: -x['n_dropped'])[:15]:
            print(f"  {r['ticket']:<22} {r['n_dropped']:>4} {r['n_total']:>4}")


if __name__ == '__main__':
    main()

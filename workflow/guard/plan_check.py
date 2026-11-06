#!/usr/bin/env python3
"""plan_check.py — G20 数据规划覆盖校验。

★ 问题背景（2026-11-05 用户指出）
  数据规划表一般内容较多，会包含 EXP 里已经配置过的信息。
  所以「规划表有 N 行，产物只用了 M 行（M<N）」不一定是漏配，
  可能是那些行本来就在现网里、本次不需要重复配。

  纯代码没法判断「哪行该配哪行不该配」，所以需要 agent 显式声明。

★ 校验依据：params.csv 的「来源」列
  格式：plan:<文件名>#<行号>
  例：plan:域名规划#1   →  用到了域名规划.csv 的第 1 行数据

★ 判定规则
  1. 找出 workspace 里的数据规划文件（非 EXP 的 csv/xlsx）
  2. 数出每个文件的有效数据行数（去掉表头、空行）
  3. 从 params.csv 的来源列提取所有 plan:<文件>#<行号>
  4. 未覆盖的行 → 警告（不是 fatal，因为可能是现网已有数据）
  5. 来源里引用了不存在的行号 → fatal（凭空引用）
  6. 引用不存在的文件 → fatal
"""
import csv
import re
from pathlib import Path

PLAN_SRC_RE = re.compile(r'^plan[:：]\s*([^#]+?)\s*#\s*(\d+)')


def _read_csv_rows(path):
    """读 csv，返回有效数据行数 + 行内容（用于报告）。"""
    try:
        with Path(path).open(encoding='utf-8-sig', newline='') as f:
            rows = list(csv.reader(f))
    except Exception:
        return 0, []
    if not rows:
        return 0, []
    # 第一行当表头
    data = [r for r in rows[1:] if any(c.strip() for c in r)]
    return len(data), data


def _read_xlsx_rows(path):
    """读 xlsx 的有效数据行数。"""
    try:
        import openpyxl
        wb = openpyxl.load_workbook(path, read_only=True, data_only=True)
        total = 0
        for ws in wb.worksheets:
            n = 0
            for row in ws.iter_rows(values_only=True):
                if any(c is not None and str(c).strip() for c in row):
                    n += 1
            total += max(0, n - 1)      # 去表头
        wb.close()
        return total
    except Exception:
        return 0


def find_plan_files(session_dir):
    """找 workspace 里的数据规划文件（排除 EXP）。"""
    sess = Path(session_dir)
    plans = []
    idx = sess / 'uploads_index.json'
    exp_names = set()
    if idx.exists():
        try:
            import json
            data = json.loads(idx.read_text(encoding='utf-8'))
            for f in data.get('files') or []:
                if f.get('is_exp'):
                    exp_names.add(f.get('name'))
                elif f.get('kind') in ('sheet', 'xlsx', 'xls', 'csv', 'text'):
                    nm = f.get('name') or ''
                    if nm.lower().endswith(('.csv', '.xlsx', '.xls')):
                        plans.append(nm)
        except Exception:
            pass

    # 兜底：直接扫 uploads/
    if not plans:
        upd = sess / 'uploads'
        if upd.is_dir():
            for p in upd.iterdir():
                if p.is_file() and p.suffix.lower() in ('.csv', '.xlsx', '.xls'):
                    if p.name not in exp_names:
                        plans.append(p.name)
    return plans


def check_plan_coverage(session_dir, params_csv):
    """主校验入口。

    Returns {
      ok, plans: {name: {total_rows, covered_rows, uncovered: [..]}},
      errors: [..],   # fatal
      warnings: [..], # 未覆盖（可能正常）
    }
    """
    sess = Path(session_dir)
    errors = []
    warnings = []

    plan_files = find_plan_files(sess)
    if not plan_files:
        return {'ok': True, 'skipped': True,
                'reason': '没有数据规划文件（只有意图场景）',
                'plans': {}, 'errors': [], 'warnings': []}

    # 统计每个规划文件的行数
    plan_info = {}
    for name in plan_files:
        p = sess / 'uploads' / name
        if not p.exists():
            # 可能只有解析后的 md
            continue
        if p.suffix.lower() == '.csv':
            n, _ = _read_csv_rows(p)
        else:
            n = _read_xlsx_rows(p)
        if n > 0:
            plan_info[name] = {'total_rows': n, 'covered': set()}

    if not plan_info:
        return {'ok': True, 'skipped': True,
                'reason': '规划文件读不出有效数据行', 'plans': {},
                'errors': [], 'warnings': []}

    # 从 params.csv 提取覆盖情况
    pc = Path(params_csv)
    if not pc.exists():
        return {'ok': False, 'plans': {},
                'errors': ['params.csv 不存在（G20 无法校验）'],
                'warnings': []}

    with pc.open(encoding='utf-8-sig', newline='') as f:
        rd = csv.DictReader(f)
        for row in rd:
            src = (row.get('来源') or '').strip()
            m = PLAN_SRC_RE.match(src)
            if not m:
                continue
            fname, rowno = m.group(1).strip(), int(m.group(2))
            # 文件名可能是全名或去后缀
            matched = None
            for name in plan_info:
                if fname == name or fname == Path(name).stem:
                    matched = name
                    break
            if not matched:
                errors.append(f'params.csv 引用了不存在的规划文件: {fname}')
                continue
            if rowno < 1 or rowno > plan_info[matched]['total_rows']:
                errors.append(
                    f'params.csv 引用了 {matched} 的第 {rowno} 行，'
                    f'但该文件只有 {plan_info[matched]["total_rows"]} 行数据')
                continue
            plan_info[matched]['covered'].add(rowno)

    # 汇总未覆盖
    result_plans = {}
    for name, info in plan_info.items():
        total = info['total_rows']
        covered = len(info['covered'])
        uncovered = sorted(set(range(1, total + 1)) - info['covered'])
        result_plans[name] = {
            'total_rows': total,
            'covered_rows': covered,
            'cover_rate': round(covered * 100 / total, 1) if total else 0,
            'uncovered': uncovered[:20],
            'n_uncovered': len(uncovered),
        }
        if uncovered:
            warnings.append(
                f'{name}: {total} 行数据，产物用了 {covered} 行，'
                f'未覆盖 {len(uncovered)} 行（行号 {uncovered[:10]}）。'
                f'如果是现网已有数据/测试数据，请在「说明」列注明，可忽略。')

    return {
        'ok': not errors,
        'plans': result_plans,
        'errors': errors[:10],
        'warnings': warnings[:10],
    }


if __name__ == '__main__':
    import json as _json
    import sys
    if len(sys.argv) < 3:
        print('用法: plan_check.py <session_dir> <params.csv>')
        sys.exit(1)
    r = check_plan_coverage(sys.argv[1], sys.argv[2])
    print(_json.dumps(r, ensure_ascii=False, indent=1))

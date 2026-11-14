"""G36：规划表「参数映射」校验。

★★ 2026-11-14（配合方案C：params.csv 由代码从规划表展开）

## 背景

阶段2 不再让 agent 手写 params.csv，改为：
  规划表的「参数映射」列 + 数据清单 → 代码展开 params.csv → mml.txt

所以规划表的参数映射成了唯一的配置来源，必须严格校验：

## 判据

fatal（配置会错/漏）：
  1. 规划表引用的数据表在数据清单里不存在
  2. 参数映射里 @列名 引用的列不在该表表头（写错列名 → 整个参数拿不到值）
  3. 数据清单某张表【没有任何规划行使用】→ 该表数据全丢
  4. 规划标「确认」但参数映射为空 → 展开出 0 行

warn（需人工确认）：
  5. @待填写 出现 → 会生成占位符，用户要填
  6. 数据表某列【没有被任何映射用到】→ 该列数据会丢
     （可能是有意不用，也可能是漏映射）

## 为什么列覆盖要 warn 而不是 fatal

有些列是说明性的（如「备注」），本来就不该进配置。
但如果是关键列（IP、名称）漏了，warn 能让 agent 自查修正。
"""
import re


def parse_datasets(dataset_text):
    """解析数据清单（复用 plan_expander 的逻辑）。"""
    try:
        import importlib
        import plan_expander as _pe
        importlib.reload(_pe)
        return _pe.parse_datasets(dataset_text)
    except Exception:
        return []


def parse_plan_rules(plan_text):
    try:
        import importlib
        import plan_expander as _pe
        importlib.reload(_pe)
        return _pe.parse_plan_mapping(plan_text)
    except Exception:
        return []


def check_param_mapping(plan_text, dataset_text):
    """校验规划表的参数映射。

    返回 {
      'ok': bool,
      'skipped': bool,
      'fatal': [str, ...],
      'warn': [str, ...],
      'stats': {'n_rules', 'n_tables', 'n_tables_used', 'n_placeholders'},
    }
    """
    tables = parse_datasets(dataset_text or '')
    rules = parse_plan_rules(plan_text or '')

    if not rules:
        # 规划表里没有参数映射列 → 可能是老版本规划表，跳过
        if '参数映射' not in (plan_text or ''):
            return {'ok': True, 'skipped': True,
                    'fatal': [], 'warn': [],
                    'reason': '规划表没有「参数映射」列（老格式）',
                    'stats': {}}
        return {'ok': False, 'skipped': False,
                'fatal': ['规划表有「参数映射」列但没有任何有效规则'],
                'warn': [], 'stats': {}}

    if not tables:
        return {'ok': False, 'skipped': False,
                'fatal': ['数据清单解析失败或为空，无法校验参数映射'],
                'warn': [], 'stats': {}}

    tmap = {t['name']: t for t in tables}
    fatal, warn = [], []
    used_tables = set()
    used_cols = {}          # 表名 → 被用到的列集合
    n_ph = 0

    for rule in rules:
        status = (rule.get('status') or '').strip()
        is_confirmed = (not status) or ('确认' in status)
        bare = rule.get('family_bare') or ''
        mapping = rule.get('mapping') or []

        if not is_confirmed:
            continue

        if not mapping:
            if bare:
                fatal.append(
                    f'规划表第 {rule.get("idx")} 行（{rule.get("family")}）'
                    f'标了「确认」但参数映射列为空 → 会展开出 0 条命令')
            continue

        # 找数据表
        tname = rule.get('table') or ''
        tbl = tmap.get(tname)
        if tbl is None:
            for k, v in tmap.items():
                if k in tname or tname in k:
                    tbl = v
                    tname = k
                    break
        if tbl is None:
            fatal.append(
                f'规划表第 {rule.get("idx")} 行引用的数据表「{tname}」'
                f'不在数据清单里（现有表：{list(tmap.keys())[:5]}）')
            continue

        used_tables.add(tname)
        headers = tbl['headers']
        hset = set(headers)
        hlower = {h.replace(' ', '').lower(): h for h in headers}

        for pname, src in mapping:
            src = (src or '').strip()
            if src == '@待填写':
                n_ph += 1
                continue
            if src.startswith('@') and src not in ('@seq', '@seq0'):
                col = src[1:].strip()
                if col in hset:
                    used_cols.setdefault(tname, set()).add(col)
                elif col.replace(' ', '').lower() in hlower:
                    used_cols.setdefault(tname, set()).add(
                        hlower[col.replace(' ', '').lower()])
                else:
                    fatal.append(
                        f'规划表第 {rule.get("idx")} 行（{bare}）参数 {pname} '
                        f'引用了 @{col}，但表「{tname}」的表头里没有这一列'
                        f'（现有列：{headers}）→ 该参数拿不到值')

    # 表覆盖检查：数据清单里每张表都该被用到（除非是「跳过」的表）
    for tname, tbl in tmap.items():
        if tname in used_tables:
            continue
        # 检查是否有规则引用了该表但状态是跳过
        ref_skipped = any(
            (tname in (r.get('table') or '') or (r.get('table') or '') in tname)
            and '跳过' in (r.get('status') or '')
            for r in rules)
        if ref_skipped:
            continue
        fatal.append(
            f'数据清单的表「{tname}」（{len(tbl["rows"])} 行）'
            f'没有任何规划行使用 → 该表数据会全部丢失')

    # 列覆盖检查（warn）
    for tname, tbl in tmap.items():
        if tname not in used_tables:
            continue
        unused = [h for h in tbl['headers']
                  if h not in (used_cols.get(tname) or set())]
        if unused:
            warn.append(
                f'表「{tname}」的列 {unused} 没有被任何参数映射用到 → '
                f'这些列的数据不会出现在产物里')

    stats = {
        'n_rules': len(rules),
        'n_tables': len(tmap),
        'n_tables_used': len(used_tables),
        'n_placeholders': n_ph,
    }
    return {
        'ok': not fatal,
        'skipped': False,
        'fatal': fatal,
        'warn': warn,
        'stats': stats,
    }


if __name__ == '__main__':
    import json
    import sys
    from pathlib import Path
    sd = Path(sys.argv[1]) if len(sys.argv) > 1 else Path('.')
    plan = (sd / 'analysis_code' / '命令族规划.md')
    ds = None
    for cand in list((sd / 'uploads_text').glob('*数据清单*.md')) + \
                list((sd / 'uploads').glob('*数据清单*.md')):
        ds = cand
        break
    r = check_param_mapping(
        plan.read_text(encoding='utf-8') if plan.exists() else '',
        ds.read_text(encoding='utf-8') if ds and ds.exists() else '')
    print(json.dumps(r, ensure_ascii=False, indent=1))

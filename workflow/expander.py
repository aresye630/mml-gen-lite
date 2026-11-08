"""模板展开器：产物 CSV（模板）+ 用户 CSV（实例清单） → 完整 params.csv。

产物 CSV 是 agent 写的模板，含特殊标记：
  · 组名带 #T 后缀  → 模板组，展开时变成 #1/#2/#3...
  · 值列写 $CSV.列名 → 从用户 CSV 取该列
  · 值列写 $CSV.列名|PREFIX_REPLACE(grp,pool) → 取列值后应用算子
  · 值列写 @组#T.参数 → 引用其他模板组（自动跟随实例编号）

用户 CSV 是业务清单，每行一个实例（可带「一列多值」如 2g;4g;5g）。

展开规则：
  1. 按「多值列」拆分 → 每个组合一个实例
  2. 每个实例套一遍模板
  3. @组#T 引用按实例编号自动替换成 @组#N
"""
import csv
import io
import re
from collections import defaultdict
from pathlib import Path

from derivation import OpError, resolve

TEMPLATE_MARK = '#T'
# 多值列分隔符
MULTI_SEP = ';'

# ★ 实例化粒度（2026-11-08）
#   object  每个「用户 CSV 行」是一个独立对象 → 组名递增 #1/#2/#3
#   item    每行是同一对象的子项/属性        → 组名固定 #1_1/#1_2
#   dedup   按「去重键」合并
#           解决「一个池组配 3 个制式，但 POOL 只需 1 个」的问题
#           用法：模板「实例化」列写 dedup:池组名
#           同一去重键的所有实例，只保留第一次出现
#   由模板里的「实例化」列指定；不填默认 object
GRANULARITY_OBJECT = "object"
GRANULARITY_ITEM = "item"
GRANULARITY_DEDUP = "dedup"


def _is_template_group(g):
    return g.endswith(TEMPLATE_MARK)


def _granularity_of(prod_rows, group):
    """取模板组的实例化粒度。

    返回 (粒度, 去重列名)。去重列名仅 dedup 粒度有效。
    """
    for r in prod_rows:
        if r.get("组") == group:
            raw = (r.get("实例化") or "").strip()
            low = raw.lower()
            if low.startswith("dedup:"):
                return GRANULARITY_DEDUP, raw[6:].strip()
            if low.startswith("dedup"):
                return GRANULARITY_DEDUP, ""
            if low == GRANULARITY_ITEM:
                return GRANULARITY_ITEM, ""
            break
    return GRANULARITY_OBJECT, ""


def _split_multi(value):
    """拆分一列多值：'2g;4g;5g' → ['2g','4g','5g']"""
    if not value:
        return ['']
    return [x.strip() for x in str(value).split(MULTI_SEP) if x.strip()]


def expand(prod_csv_text, user_csv_text):
    """执行展开。

    返回 {'rows': [...], 'errors': [...], 'stats': {...}}
    """
    errors = []

    # 1) 读产物模板
    prod_reader = csv.DictReader(io.StringIO(prod_csv_text))
    prod_rows = list(prod_reader)
    if not prod_rows:
        return {'rows': [], 'errors': ['产物 CSV 为空'], 'stats': {}}

    # 2) 读用户 CSV
    user_reader = csv.DictReader(io.StringIO(user_csv_text))
    user_rows = list(user_reader)
    user_cols = list(user_reader.fieldnames or [])

    # 3) 找出多值列（含 ';' 的列）
    multi_cols = set()
    for col in user_cols:
        for ur in user_rows[:20]:
            if MULTI_SEP in str(ur.get(col, '')):
                multi_cols.add(col)
                break

    # 4) 把用户 CSV 拆成「实例列表」
    instances = []
    for ur in user_rows:
        # 逐列拆多值，取笛卡尔积
        combos = [{}]
        for col in user_cols:
            vals = _split_multi(ur.get(col, '')) if col in multi_cols else [ur.get(col, '')]
            new = []
            for c in combos:
                for v in vals:
                    nc = dict(c)
                    nc[col] = v
                    new.append(nc)
            combos = new
        for c in combos:
            instances.append(c)

    if not instances:
        return {'rows': [], 'errors': ['用户 CSV 没有数据行'], 'stats': {}}

    # 5) 按「模板组的依赖顺序」展开
    #    拓扑排序：被引用的先展开（@组名 出现在别的组里）
    tg_groups = []
    for r in prod_rows:
        g = r.get('组', '')
        if _is_template_group(g) and g not in tg_groups:
            tg_groups.append(g)

    def refs_of(g):
        """该组引用了哪些组。"""
        out = set()
        for r in prod_rows:
            if r.get('组') != g:
                continue
            v = r.get('值', '')
            for m in re.finditer(r'@([^@.]+)\.[A-Za-z0-9_]+', v):
                out.add(m.group(1).strip())
        return out

    # 简单拓扑排序
    ordered, visited, visiting = [], set(), set()

    def visit(g):
        if g in visited or g not in tg_groups:
            return
        if g in visiting:
            return   # 循环引用，跳过
        visiting.add(g)
        for dep in refs_of(g):
            visit(dep)
        visiting.discard(g)
        visited.add(g)
        ordered.append(g)

    for g in tg_groups:
        visit(g)

    # 6) 逐实例展开
    #
    # ★ 两种粒度：
    #   object —— 每行 CSV 是一个新对象，组名在实例间递增（POOLGROUP#1/#2/#3）
    #             同一实例内组名固定
    #   item   —— 每行 CSV 是同一对象的子项，组名全实例共用（L7FILTER#1）
    #             item 组只展开一次（用第 1 个实例的上下文），但值可引用其他 instance 组
    out_rows = []
    failed_rows = []   # 派生失败的行（不进产物，单独返回）

    # 先确定每个模板组的粒度
    gran = {}
    dedup_key = {}
    for g in ordered:
        gr, dk = _granularity_of(prod_rows, g)
        gran[g] = gr
        dedup_key[g] = dk

    # 收集「跨实例引用」需要的信息：哪个组按行展开，行内主键是什么
    # 简化策略：object 组每实例建一个；item 组只建一组（挂到实例 1）
    inst_map = {}   # (group, inst_idx) -> actual_group

    # dedup 组：按去重键分配编号（同一键的所有实例共用一个编号）
    dedup_seq = {}      # (group, key_value) -> seq
    dedup_counter = {}  # group -> 当前最大编号
    for g in ordered:
        if gran[g] != GRANULARITY_DEDUP:
            continue
        dedup_counter[g] = 0
        kcol = dedup_key[g]
        for inst_idx, inst in enumerate(instances, 1):
            kv = inst.get(kcol, '') if kcol else str(inst_idx)
            kk = (g, kv)
            if kk not in dedup_seq:
                dedup_counter[g] += 1
                dedup_seq[kk] = dedup_counter[g]
            inst_map[(g, inst_idx)] = f"{g[:-len(TEMPLATE_MARK)]}#{dedup_seq[kk]}"

    for inst_idx in range(1, len(instances) + 1):
        for g in ordered:
            base = g[:-len(TEMPLATE_MARK)]
            if gran[g] == GRANULARITY_OBJECT:
                inst_map[(g, inst_idx)] = f'{base}#{inst_idx}'

    # item 组：全实例共用，编号固定为 #1
    for g in ordered:
        if gran[g] == GRANULARITY_ITEM:
            base = g[:-len(TEMPLATE_MARK)]
            inst_map[(g, 1)] = f'{base}#1'

    def _resolve_ref(expr, inst_idx, local_map):
        """解析 @组.参数 引用，按当前实例替换组名。"""
        def _repl(m):
            gname = m.group(1).strip()
            suffix = m.group(2)
            if gname in local_map:
                return '@' + local_map[gname] + suffix
            # 模板组：按实例取实际组名
            if gname in gran:
                key = (gname, inst_idx)
                real = inst_map.get(key) or inst_map.get((gname, 1))
                if real:
                    return '@' + real + suffix
            return m.group(0)
        return re.sub(r'@([^@.]+)(\.[A-Za-z0-9_]+)', _repl, expr)

    # object 组：逐实例展开
    for inst_idx, inst in enumerate(instances, 1):
        local_map = {}
        for g in ordered:
            if gran[g] != GRANULARITY_OBJECT:
                continue
            actual_g = inst_map[(g, inst_idx)]
            local_map[g] = actual_g

        # 先把所有 object 组的组名映射建好（供组间引用）
        for g in ordered:
            if gran[g] == GRANULARITY_OBJECT:
                local_map[g] = inst_map[(g, inst_idx)]
        # item 组也映射到 #1
        for g in ordered:
            if gran[g] == GRANULARITY_ITEM:
                local_map[g] = inst_map[(g, 1)]

        for g in ordered:
            if gran[g] not in (GRANULARITY_OBJECT, GRANULARITY_DEDUP):
                continue
            # dedup 组：同一去重键的后续实例跳过（只在第一次出现时展开）
            if gran[g] == GRANULARITY_DEDUP:
                kcol = dedup_key[g]
                kv = inst.get(kcol, '') if kcol else str(inst_idx)
                kk = (g, kv)
                if dedup_seq.get(kk) is None:
                    continue
                # 只有该键第一次出现时才展开
                _first = None
                for ii in range(1, inst_idx + 1):
                    iv = instances[ii-1].get(kcol, '') if kcol else str(ii)
                    if iv == kv:
                        _first = ii
                        break
                if _first != inst_idx:
                    continue
            actual_g = inst_map[(g, inst_idx)]
            group_rows = [r for r in prod_rows if r.get('组') == g]
            for r in group_rows:
                ctx = dict(inst)
                ctx['_seq'] = inst_idx
                ctx['_concat_sep'] = '-'
                val_expr = r.get('值', '')
                try:
                    resolved = _resolve_ref(val_expr, inst_idx, local_map)
                    val = resolve(resolved, ctx)
                except OpError as e:
                    # ★ 2026-11-08：派生失败的行不进入产物，单独记录
                    #   不中断整批（用户裁定：不接受一个表达式错就整批判死）
                    failed_rows.append({
                        'inst': inst_idx,
                        'group': actual_g,
                        'param': r.get('参数', ''),
                        'expr': (r.get('值', '') or '')[:120],
                        'error': str(e)[:200],
                    })
                    errors.append(f'实例{inst_idx} {actual_g}.{r.get("参数","")}: {e}')
                    continue
                out_rows.append({
                    '序号': str(len(out_rows) + 1),
                    '组': actual_g,
                    '网元': r.get('网元', ''),
                    '命令族': r.get('命令族', ''),
                    '参数': r.get('参数', ''),
                    '值': val,
                    '来源': r.get('来源', ''),
                    '说明': r.get('说明', ''),
                })

    # item 组：每个子项一条独立命令
    #   ★ 2026-11-08 修 bug：原来所有子项共用一个组名（L7FILTER#1），
    #     mml_gen 按组名聚合 → 5 个子项被合并成 1 条命令（5 个 URL 塞一起）。
    #     现在每个子项用独立组名 L7FILTER#1_1 / #1_2 / ...，
    #     生成 5 条命令（主键相同，MML 允许这样配不同子项）。
    for g in ordered:
        if gran[g] != GRANULARITY_ITEM:
            continue
        base_g = g[:-len(TEMPLATE_MARK)]
        group_rows = [r for r in prod_rows if r.get('组') == g]
        local_map = {gg: inst_map.get((gg, 1), gg) for gg in ordered}
        for inst_idx, inst in enumerate(instances, 1):
            actual_g = f'{base_g}#1_{inst_idx}'
            ctx = dict(inst)
            ctx['_seq'] = inst_idx
            ctx['_concat_sep'] = '-'
            for r in group_rows:
                val_expr = r.get('值', '')
                try:
                    resolved = _resolve_ref(val_expr, inst_idx, local_map)
                    val = resolve(resolved, ctx)
                except OpError as e:
                    failed_rows.append({
                        'inst': inst_idx,
                        'group': actual_g,
                        'param': r.get('参数', ''),
                        'expr': (r.get('值', '') or '')[:120],
                        'error': str(e)[:200],
                    })
                    errors.append(f'子项{inst_idx} {actual_g}.{r.get("参数","")}: {e}')
                    continue
                out_rows.append({
                    '序号': str(len(out_rows) + 1),
                    '组': actual_g,
                    '网元': r.get('网元', ''),
                    '命令族': r.get('命令族', ''),
                    '参数': r.get('参数', ''),
                    '值': val,
                    '来源': r.get('来源', ''),
                    '说明': r.get('说明', ''),
                })

    # 7) 处理非模板行
    #   ★ 2026-11-08 修 bug：原来直接原样保留，
    #     导致 @L7FILTER#T.xxx 这种引用没被替换成 @L7FILTER#1.xxx
    #   mml_gen 不认识 #T，会报「引用了不存在的组」
    #   现在：非模板行也要过 _resolve_ref（按实例 1 的映射替换）
    def _final_fix_ref(expr, inst_idx=1):
        """把 @组#T.参数 里的 #T 换成实际编号。

        ★ 注意 item 粒度：组名变成了 #1_1（第一个子项），
          所以引用 item 组要指向 #1_1 而不是 #1。
        """
        def _repl(m):
            gname = m.group(1).strip()
            suffix = m.group(2)
            if gname in gran:
                if gran[gname] == GRANULARITY_ITEM:
                    base = gname[:-len(TEMPLATE_MARK)]
                    return '@' + f'{base}#1_1' + suffix
                real = inst_map.get((gname, inst_idx)) or inst_map.get((gname, 1))
                if real:
                    return '@' + real + suffix
            return m.group(0)
        return re.sub(r'@([^@.]+)(\.[A-Za-z0-9_]+)', _repl, expr)

    for r in prod_rows:
        if _is_template_group(r.get('组', '')):
            continue
        val = r.get('值', '')
        if val.startswith('@'):
            val = _final_fix_ref(val)
        out_rows.append({
            '序号': str(len(out_rows) + 1),
            '组': r.get('组', ''),
            '网元': r.get('网元', ''),
            '命令族': r.get('命令族', ''),
            '参数': r.get('参数', ''),
            '值': val,
            '来源': r.get('来源', ''),
            '说明': r.get('说明', ''),
        })

    # 8) 输出 CSV
    buf = io.StringIO()
    w = csv.DictWriter(buf, fieldnames=['序号', '组', '网元', '命令族', '参数', '值', '来源', '说明'])
    w.writeheader()
    w.writerows(out_rows)

    return {
        'rows': out_rows,
        'csv_text': buf.getvalue(),
        'errors': errors,
        # ★ 2026-11-08：派生失败的行（不进产物，供 UI 展示让人工确认）
        'failed_rows': failed_rows,
        'n_failed_rows': len(failed_rows),
        'stats': {
            'n_instances': len(instances),
            'n_template_groups': len(ordered),
            'n_output_rows': len(out_rows),
            'n_failed_rows': len(failed_rows),
            'multi_cols': sorted(multi_cols),
        },
    }

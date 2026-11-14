"""规划表「参数映射」→ expander 模板 params.csv → 完整 params.csv → mml.txt

★★ 2026-11-14（用户裁定，替代原来「agent 手写 6642 行 params.csv」）

## 为什么需要这个模块

原来的阶段2 由 agent 手写 params.csv：
  · NC20260819001887（1294 条命令）→ 6642 行参数行
  · LLM 单次输出有 token 上限，分 28 批写完
  · 实测 2546s，其中 2400s（94%）在生成 token

用户的三处裁定：
  1. 「params是根据规划+数据表派生出来的，对不对」 → 对，派生该由代码做
  2. 「agent做映射是对的，但是需要考虑数据规划表可能无法覆盖所有参数的情况，要支持留空」
  3. 「占位符不能是简单的【待填写】，而是能支持关联的全局唯一符号，
      统一使用替换修改就可以直接获得完整的脚本」
     「按对象才是全局唯一，语义合并就是190条一样的，
      如果已经知道了190条，那这里肯定是有区分值的」
     「占位符要带参数名」

## 架构（复用现有 expander，不重造展开逻辑）

  规划表「参数映射」列（agent 写，5-20 行）
      ↓ 本模块翻译
  模板 params.csv（#T 组 + ${CSV.列名}，expander 认识的语法）
      ↓ workflow/expander.py（已有，支持算子链/去重/引用）
  完整 params.csv
      ↓ workflow/mml_gen.py
  mml.txt

## 参数映射语法（agent 在规划表里写）

  POOLNAME=@池名称            →  ${CSV.池名称}
  SECTIONNUM=@seq             →  序号（1,2,3...）
  SECTIONNUM=@seq0            →  序号（0,1,2...）
  TNLTYPE=gre                 →  gre（固定值）
  RELEASETIME=@待填写          →  【POOL_RELEASETIME_cmiot5galxnj2jsv4】
"""
import csv
import io
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

# ═══════════════════════════════════════════════════════════
# 数据清单解析
# ═══════════════════════════════════════════════════════════

_META_RE = re.compile(r'^(.+?)\s*[（(]([^）)]*)[）)]\s*$')


def parse_datasets(dataset_text):
    """解析数据清单 md → [{name, action, headers, rows}, ...]"""
    tables = []
    parts = re.split(r'^##\s+', dataset_text, flags=re.M)
    for seg in parts[1:]:
        lines = seg.split('\n')
        if not lines:
            continue
        title = lines[0].strip()
        m = _META_RE.match(title)
        name, action = (m.group(1).strip(), m.group(2).strip()) if m else (title, '')
        header, rows = None, []
        for line in lines[1:]:
            s = line.strip()
            if not s.startswith('|'):
                continue
            if re.fullmatch(r'\|[\s\-:|]+\|', s):
                continue
            cells = [c.strip() for c in s.strip('|').split('|')]
            if header is None:
                header = cells
                continue
            rows.append({header[i]: (cells[i] if i < len(cells) else '')
                         for i in range(len(header))})
        if header:
            tables.append({'name': name, 'action': action,
                           'headers': header, 'rows': rows})
    return tables


# ═══════════════════════════════════════════════════════════
# 规划表解析
# ═══════════════════════════════════════════════════════════

_VERB_RE = re.compile(
    r'^(ADD|MOD|RMV|SET|ACT|DEA|RTR|RST|STR|STP|CLR|OPR|SYN|LOD|RBL|UPD|LCK|ULK)'
    r'\s+([A-Z][A-Z0-9_]+)')


def parse_plan_mapping(plan_text):
    """从规划表提取「参数映射」规则。

    Returns [{
      idx, table, object, family, verb, family_bare, action, status,
      mapping_raw, mapping: [(param, src), ...]
    }, ...]
    """
    lines = [l.strip() for l in plan_text.split('\n')]
    col, out = {}, []
    for line in lines:
        if not line.startswith('|'):
            continue
        cells = [c.strip() for c in line.split('|')][1:-1]
        if len(cells) < 5:
            continue
        if all(re.fullmatch(r':?-+:?', c) for c in cells if c):
            continue
        joined = ''.join(cells)
        if '命令族' in joined and '参数映射' in joined:
            def find(*names):
                for nm in names:
                    for i, h in enumerate(cells):
                        if nm in h:
                            return i
                return None
            col = {'table': find('数据清单表'), 'object': find('业务对象'),
                   'family': find('命令族'), 'action': find('动作'),
                   'mapping': find('参数映射'), 'status': find('状态')}
            continue
        if col.get('mapping') is None:
            continue
        if any('命令族' in c for c in cells):
            continue

        def get(k):
            i = col.get(k)
            return cells[i] if i is not None and i < len(cells) else ''

        fam_cell = get('family')
        if not fam_cell:
            continue
        m = _VERB_RE.match(fam_cell.upper())
        verb, bare = (m.group(1), m.group(2)) if m else ('', '')
        if not bare:
            m2 = re.match(r'^([A-Z][A-Z0-9_]+)', fam_cell.upper())
            bare = m2.group(1) if m2 else ''
        out.append({
            'idx': len(out) + 1,
            'table': get('table'), 'object': get('object'),
            'family': fam_cell, 'verb': verb, 'family_bare': bare,
            'action': get('action'), 'status': get('status'),
            'mapping_raw': get('mapping'),
            'mapping': parse_mapping(get('mapping')),
        })
    return out


def parse_mapping(raw):
    """'A=@列1; B=gre' → [('A','@列1'), ('B','gre')]"""
    out = []
    if not raw:
        return out
    for part in re.split(r'[;；]', raw):
        part = part.strip()
        if not part or '=' not in part:
            continue
        k, v = part.split('=', 1)
        k, v = k.strip().upper(), v.strip()
        if k:
            out.append((k, v))
    return out


# ═══════════════════════════════════════════════════════════
# 翻译：参数映射 → expander 模板 CSV
# ═══════════════════════════════════════════════════════════

TEMPLATE_MARK = '#T'


def _sanitize(s):
    s = str(s or '').strip().strip('"')
    s = re.sub(r'[^0-9A-Za-z_.-]', '_', s)
    return s or 'NA'


def _detect_key_col(headers):
    """猜主键列（用于占位符命名的对象标识）。"""
    for h in headers:
        if any(k in h for k in ('名称', '标识', '池名', '隧道名', '接口名', 'IP池')):
            return h
    for h in headers:
        if h.upper().endswith('NAME') or h.upper().endswith('ID'):
            return h
    return headers[0] if headers else None


def to_template_rows(rules, tables, unit='UDG'):
    """把规划表参数映射翻译成 expander 的模板行。

    返回 (template_rows, table_index, warnings)

    template_rows: [{'序号','组','网元','动词','命令族','参数','值','来源','说明','实例化'}]
      组名带 #T（模板组）
      值用 ${CSV.列名} / ${SELF} / 固定值 / 占位符

    table_index: {表名: {'headers': [...], 'rows': [...], 'key_col': str}}
    """
    tmap = {t['name']: t for t in tables}
    out, warns = [], []
    tidx = {}
    no = 0

    # 同一 (verb, family) 出现多行 = 变体 → 每条规则一个独立模板组
    # 用 #T + 变体后缀区分，避免多个变体共用一个模板组
    seen = {}
    for rule in rules:
        status = (rule.get('status') or '').strip()
        if status and '确认' not in status:
            continue
        bare = rule['family_bare']
        mapping = rule['mapping']
        if not bare:
            continue
        if not mapping:
            warns.append(f'规划表第 {rule["idx"]} 行（{rule["family"]}）没有参数映射，跳过')
            continue

        # 找数据表
        tname = rule['table']
        tbl = tmap.get(tname)
        if tbl is None:
            for k, v in tmap.items():
                if k in tname or tname in k:
                    tbl = v
                    break
        if tbl is None:
            warns.append(f'规划表第 {rule["idx"]} 行引用的表「{tname}」不在数据清单里')
            continue

        headers = tbl['headers']
        key_col = _detect_key_col(headers)
        tidx[tname] = {'headers': headers, 'rows': tbl['rows'],
                       'key_col': key_col}

        # 模板组名：同族多规则时加后缀区分
        n_seen = seen.get((rule['verb'], bare), 0)
        seen[(rule['verb'], bare)] = n_seen + 1
        gname = f'{bare}{TEMPLATE_MARK}' if n_seen == 0 else f'{bare}v{n_seen + 1}{TEMPLATE_MARK}'

        # 变体过滤条件（「业务对象」列含判别词）
        variant_kw = ''
        if n_seen > 0 or _has_multi_variant(rules, rule):
            variant_kw = _extract_variant_kw(rule.get('object', ''))

        for pname, src in mapping:
            no += 1
            val, note = _translate_value(src, rule, headers, key_col)
            out.append({
                '序号': str(no), '组': gname, '网元': unit,
                '动词': rule['verb'], '命令族': bare, '参数': pname,
                '值': val, '来源': f'plan:{tname}#{rule["idx"]}',
                '说明': note, '实例化': 'object',
                '_variant_kw': variant_kw,   # 内部用，写 CSV 时丢
            })

    return out, tidx, warns


def _has_multi_variant(rules, rule):
    """同表同族是否有多个映射规则（=变体）。"""
    same = [r for r in rules
            if r['table'] == rule['table'] and r['family_bare'] == rule['family_bare']
            and (r.get('status') or '').find('确认') >= 0]
    return len(same) > 1


def _extract_variant_kw(obj_label):
    """从「业务对象」标签提判别关键词，用于过滤数据行。

    例：'IPv4 段' → 'IPv4'；'新增池' → ''
    """
    if not obj_label:
        return ''
    s = re.sub(r'[（(].*?[）)]', '', obj_label)
    s = re.sub(r'[段组类]$', '', s).strip()
    m = re.search(r'(IPv4|IPv6|V4|V6|IPV4|IPV6|TAC|LAC|新增|删除|调整)', s, re.I)
    return m.group(1) if m else ''


def _translate_value(src, rule, headers, key_col):
    """把一个值来源翻译成 expander 语法。

    返回 (value_expr, note)
    """
    src = (src or '').strip()
    fam, table = rule['family_bare'], rule['table']

    if src == '@seq':
        return '${SELF}', '行号(1起)'
    if src == '@seq0':
        return '${SELF}|DEC(1)', '行号(0起)'
    if src == '@待填写':
        # ★ 占位符按对象唯一 + 带参数名：【族_参数_对象】
        #   实现：模板值先写死标记 @@PH@@，
        #   展开后按「该组的对象主键值」重写成真正的占位符。
        #   （不能在模板里拼 ${CSV.x}，因为 expander 不解析 【】内的表达式）
        return '@@PH@@', f'待填写|key={key_col or ""}'
    if src.startswith('@'):
        colname = src[1:].strip()
        # 校验列名存在
        if colname not in headers:
            hit = None
            for h in headers:
                if h.replace(' ', '').lower() == colname.replace(' ', '').lower():
                    hit = h
                    break
            if hit:
                colname = hit
            else:
                return (f'【{fam}_@@PARAM@@_MISSING_{_sanitize(colname)}】',
                        f'列「{colname}」不在表头')
        return f'${{CSV.{colname}}}', ''
    return src, ''


# ═══════════════════════════════════════════════════════════
# 主流程
# ═══════════════════════════════════════════════════════════

TMPL_HEADER = ['序号', '组', '网元', '动词', '命令族', '参数', '值',
               '来源', '说明', '实例化']


def _write_template_csv(rows, path):
    buf = io.StringIO()
    w = csv.DictWriter(buf, fieldnames=TMPL_HEADER, lineterminator='\n',
                       extrasaction='ignore')
    w.writeheader()
    for r in rows:
        w.writerow({k: r.get(k, '') for k in TMPL_HEADER})
    Path(path).write_text(buf.getvalue(), encoding='utf-8')
    return len(rows)


def _table_to_csv(tbl):
    """把某张数据表转成 CSV 文本（给 expander 当 user_csv）。"""
    buf = io.StringIO()
    w = csv.DictWriter(buf, fieldnames=tbl['headers'], lineterminator='\n',
                       extrasaction='ignore')
    w.writeheader()
    for r in tbl['rows']:
        w.writerow({h: r.get(h, '') for h in tbl['headers']})
    return buf.getvalue()


def postprocess_placeholders(csv_text):
    """把模板里的 【族_@@PARAM@@_值】 替换成 【族_参数_值】。

    因为参数名在写模板时还不知道（占位符要用展开后的实际对象值）。
    """
    def _fix(m):
        body = m.group(1)
        parts = body.split('_@@PARAM@@_')
        if len(parts) != 2:
            return m.group(0)
        fam, obj = parts
        return f'【{fam}_{obj}】'
    return re.sub(r'【([^】]*_@@PARAM@@_[^】]*)】', _fix, csv_text)


def expand_from_session(session_dir, unit='UDG'):
    """从会话目录展开：规划表 + 数据清单 → params.csv + 占位符清单。

    Returns dict(ok, n_params, n_groups, n_placeholders, warnings, error)
    """
    sd = Path(session_dir)
    ac = sd / 'analysis_code'
    ac.mkdir(parents=True, exist_ok=True)

    plan_p = ac / '命令族规划.md'
    if not plan_p.exists():
        return {'ok': False, 'error': '缺少 命令族规划.md', 'warnings': []}

    ds_text = ''
    for cand in list((sd / 'uploads_text').glob('*数据清单*.md')) + \
                list((sd / 'uploads').glob('*数据清单*.md')):
        try:
            ds_text = cand.read_text(encoding='utf-8', errors='replace')
            break
        except Exception:
            continue
    if not ds_text:
        return {'ok': False, 'error': '缺少数据清单', 'warnings': []}

    plan_text = plan_p.read_text(encoding='utf-8', errors='replace')
    tables = parse_datasets(ds_text)
    rules = parse_plan_mapping(plan_text)
    if not rules:
        return {'ok': False, 'error': '规划表里没有「参数映射」列', 'warnings': []}

    tmpl_rows, tidx, warns = to_template_rows(rules, tables, unit=unit)
    if not tmpl_rows:
        return {'ok': False, 'error': f'参数映射为空（warnings: {warns[:3]}）',
                'warnings': warns}

    # 按表分组：每个表独立展开（不同表可能列名不同）
    # expander 一次只吃一个 user_csv，所以按表循环
    try:
        import importlib
        import expander as _ex
        importlib.reload(_ex)
    except Exception as e:
        return {'ok': False, 'error': f'import expander 失败: {e}', 'warnings': warns}

    all_out_rows = []
    all_errors = []
    # 模板行按「组」分组，组的来源表从 来源列解析 plan:<表名>#<idx>
    group_table = {}
    for r in tmpl_rows:
        src = r.get('来源') or ''
        m = re.match(r'plan:(.+?)#', src)
        if m:
            group_table.setdefault(r['组'], m.group(1))

    for tname, tbl in tidx.items():
        groups_of_table = {g for g, t in group_table.items() if t == tname}
        if not groups_of_table:
            continue
        sub_rows = [r for r in tmpl_rows if r['组'] in groups_of_table]
        # 变体过滤：若该表有变体关键词，按行过滤
        rows_used = tbl['rows']
        kw = ''
        for r in sub_rows:
            if r.get('_variant_kw'):
                kw = r['_variant_kw']
                break
        if kw:
            filt = [rw for rw in rows_used
                    if any(kw.upper().replace(' ', '') in str(v).upper().replace(' ', '')
                           for v in rw.values())]
            if filt:
                rows_used = filt
        user_csv = _table_to_csv({'headers': tbl['headers'], 'rows': rows_used})

        # 写临时模板
        buf = io.StringIO()
        w = csv.DictWriter(buf, fieldnames=TMPL_HEADER, lineterminator='\n',
                           extrasaction='ignore')
        w.writeheader()
        for r in sub_rows:
            w.writerow({k: r.get(k, '') for k in TMPL_HEADER})

        try:
            res = _ex.expand(buf.getvalue(), user_csv)
        except Exception as e:
            all_errors.append(f'{tname} 展开失败: {type(e).__name__}: {e}')
            continue
        if res.get('errors'):
            all_errors.extend([f'{tname}: {x}' for x in res['errors'][:3]])
        all_out_rows.extend(res.get('rows') or [])

    if not all_out_rows:
        return {'ok': False,
                'error': f'展开出 0 行（errors: {all_errors[:3]}）',
                'warnings': warns}

    # 写完整 params.csv
    # ★ 每组 → 动词（expander 输出不含动词列，要补回来）
    group_verb = {}
    group_keycol = {}
    for r in tmpl_rows:
        g_base = r['组'].replace(TEMPLATE_MARK, '')
        group_verb[r['组'].rstrip(TEMPLATE_MARK)] = r.get('动词', '')
        # 从说明列里取主键列（@待填写 时写入）
        note = r.get('说明') or ''
        m = re.search(r'key=(\S+)', note)
        if m and m.group(1):
            group_keycol[r['组'].rstrip(TEMPLATE_MARK)] = m.group(1)

    def _verb_of(group):
        g = str(group or '')
        base = g.split('#')[0] if '#' in g else g
        return group_verb.get(base) or group_verb.get(base + TEMPLATE_MARK) or ''

    def _keycol_of(group):
        g = str(group or '')
        base = g.split('#')[0] if '#' in g else g
        return group_keycol.get(base) or group_keycol.get(base + TEMPLATE_MARK) or ''

    # ★ 每组的对象主键值（用于占位符命名）：
    #   从该组里「参数名 == 主键列对应参数」的行取，或取该组第一行的值
    #   简化：取该组中值看起来像对象名的那行（长度最长/非枚举）
    group_obj = {}
    for r in all_out_rows:
        g = r.get('组', '')
        val = str(r.get('值', ''))
        if val.startswith('【') or val == '@@PH@@':
            continue
        prev = group_obj.get(g)
        if prev is None or len(val) > len(prev):
            group_obj[g] = val

    out_buf = io.StringIO()
    w = csv.writer(out_buf, lineterminator='\n')
    w.writerow(['序号', '组', '网元', '动词', '命令族', '参数', '值', '来源', '说明'])
    n_ph = 0
    seen_ph = {}
    ph_rows = []
    for i, r in enumerate(all_out_rows, 1):
        val = str(r.get('值', ''))
        grp = r.get('组', '')
        # ★ 重写占位符：@@PH@@ → 【族_参数_对象】
        if '@@PH@@' in val:
            fam = r.get('命令族', '')
            param = r.get('参数', '')
            obj = _sanitize(group_obj.get(grp, 'OBJ'))
            ph_name = f'{fam}_{param}_{obj}'
            val = val.replace('@@PH@@', f'【{ph_name}】')
            if ph_name not in seen_ph:
                seen_ph[ph_name] = 1
                ph_rows.append({
                    'ph': f'【{ph_name}】', 'family': fam, 'param': param,
                    'object': obj, 'n_cmds': 1, 'suggest': '',
                })
            else:
                seen_ph[ph_name] += 1
        w.writerow([str(i), grp, r.get('网元', ''),
                    _verb_of(grp), r.get('命令族', ''), r.get('参数', ''),
                    val, r.get('来源', ''), r.get('说明', '')])
    # 回填影响命令数
    for x in ph_rows:
        key = x['ph'][1:-1]
        x['n_cmds'] = seen_ph.get(key, 1)
    (ac / 'params.csv').write_text(out_buf.getvalue(), encoding='utf-8')

    if ph_rows:
        n_ph = len(ph_rows)
        _write_ph_csv(ph_rows, ac / '占位符清单.csv')
        _write_fill_py(ac / 'fill_placeholders.py')

    return {
        'ok': True,
        'n_params': len(all_out_rows),
        'n_groups': len({r.get('组') for r in all_out_rows}),
        'n_placeholders': n_ph,
        'warnings': warns + all_errors[:5],
        'error': '',
    }


def _fill_param_in_placeholder(val, param):
    """【族_@@PARAM@@_对象】 → 【族_参数_对象】"""
    if '@@PARAM@@' not in val:
        return val
    return val.replace('@@PARAM@@', param or 'X')


PH_HEADER = ['占位符', '族', '参数', '对象', '影响命令数', '建议值', '填这里']


def _write_ph_csv(rows, path):
    buf = io.StringIO()
    w = csv.DictWriter(buf, fieldnames=PH_HEADER, lineterminator='\n',
                       extrasaction='ignore')
    w.writeheader()
    for r in sorted(rows, key=lambda x: (x['family'], x['param'], x['object'])):
        w.writerow({k: r.get(k, '') for k in PH_HEADER})
    Path(path).write_text(buf.getvalue(), encoding='utf-8')


FILL_PY = '''#!/usr/bin/env python3
"""按占位符清单填值，一键生成完整脚本。

用法：
  1. 打开 占位符清单.csv，在「填这里」列填上实际值
  2. python3 fill_placeholders.py 占位符清单.csv mml.txt params.csv
  3. 脚本会把所有【...】占位符替换掉，并检查残留
"""
import csv
import re
import sys
from pathlib import Path

PH_RE = re.compile(r'【[^】]+】')


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        return 1
    rows = list(csv.DictReader(open(sys.argv[1], encoding='utf-8-sig')))
    targets = sys.argv[2:]
    ph_map, empty = {}, []
    for r in rows:
        ph = (r.get('占位符') or '').strip()
        val = (r.get('填这里') or '').strip()
        if not ph:
            continue
        (ph_map.__setitem__(ph, val) if val else empty.append(ph))

    if not ph_map:
        print(f'⚠️  「填这里」列全空，请先填值（共 {len(rows)} 个占位符）')
        return 2

    total = 0
    for t in targets:
        p = Path(t)
        if not p.exists():
            continue
        txt = p.read_text(encoding='utf-8')
        n = 0
        for ph, val in ph_map.items():
            c = txt.count(ph)
            if c:
                txt = txt.replace(ph, val)
                n += c
        p.write_text(txt, encoding='utf-8')
        total += n
        print(f'✅ {t}: 替换 {n} 处')

    print(f'\\n共替换 {total} 处，已填 {len(ph_map)}/{len(rows)}')
    if empty:
        print(f'⚠️  还有 {len(empty)} 个未填：')
        for ph in empty[:10]:
            print(f'    {ph}')
        if len(empty) > 10:
            print(f'    ...（共 {len(empty)} 个）')
    else:
        print('✅ 全部填完，可下发')

    for t in targets:
        p = Path(t)
        if p.exists():
            left = set(PH_RE.findall(p.read_text(encoding='utf-8')))
            if left:
                print(f'❌ {t} 还有 {len(left)} 个未填')
    return 0


if __name__ == '__main__':
    sys.exit(main())
'''


def _write_fill_py(path):
    Path(path).write_text(FILL_PY, encoding='utf-8')
    try:
        Path(path).chmod(0o755)
    except Exception:
        pass


if __name__ == '__main__':
    import json
    sd = sys.argv[1] if len(sys.argv) > 1 else '.'
    print(json.dumps(expand_from_session(sd), ensure_ascii=False, indent=1))

#!/usr/bin/env python3
"""mml_gen.py — 从 params.csv 机械生成 MML（纯代码，不调 LLM）。

★ 设计（2026-11-05 用户裁定）
  params.csv 是单一数据源：一行一个参数，按「组」列聚合为一条命令。
  mml.txt 由代码生成 ⇒ 用户只改 csv 就能重现 mml，不需要重跑 agent。

★ CSV 格式（8 列）
  序号,组,网元,命令族,参数,值,来源,说明
  1,HOST#1,UDG,HOST,HOSTNAME,hncatv_00_h_001,plan:域名规划#1,
  2,HOST#1,UDG,HOST,DOMAINVALUE,video.hncatv.com,plan:域名规划#1,
  3,FILTER#1,UDG,FILTER,FILTERNAME,hncatv_00_f_h_001,exp:derive,
  4,FILTER#1,UDG,FILTER,HOSTNAME,@HOST#1.HOSTNAME,infer 引用 HOST#1

★ 引用语法
  @<组名>.<参数名>  →  展开成该组该参数的值
  例：@HOST#1.HOSTNAME 展开成 hncatv_00_h_001

★ 生成规则
  · 同「组」的行合并成一条命令，参数按 CSV 行序排列
  · 值含【待填写】的，原样保留（不猜值）
  · 需要引号的参数（含特殊字符/枚举）自动加引号
  · 网元分段：多网元时按「网元」列分组输出 ===== 网元: XXX ===== 段
"""
import csv
import re
from collections import OrderedDict
from pathlib import Path

# 枚举参数：值不加引号（现网 EXP 里都是裸写）
ENUM_PARAMS = { 'USAGERPTMODE', 'LOCRPTSWITCH',
    'TCPCHGPROFLAG', 'POLICYTYPE', 'RULESPECTYPE', 'FILTERINGMODE',
    'TETHERDETFLAG', 'FLOWFILTERTYPE', 'EVENTCHARGEFLAG',
    'FUPSESSIONEXC', 'TETHERINGMAXNUM', 'ENABLE', 'DISABLE',
    'INHERIT', 'ANY', 'DEFAULT', 'ALL', 'NONE',
}

# 这些参数的值需要加引号（字符串类型）
QUOTED_PARAMS = {
    'HOSTNAME', 'DOMAINVALUE', 'FILTERNAME', 'FLOWFILTERNAME',
    'L7FILTERNAME', 'SUBL7FLTNAME', 'URRNAME', 'URRGROUPNAME',
    'PCCPOLICYGRPNM', 'RULENAME', 'USERPROFILENAME', 'POLICYNAME',
    'TEMPLATENAME', 'VRFNAME', 'APN', 'PROTOCOLNAME', 'IDENPROTNAME',
    'SVRIP', 'IPV6ADDRESS', 'RG', 'ONLINERG', 'OFFRG',
    'DFTURRGRPNAME', 'DFTSIGURRGNAME', 'SIGURRGRPNAME',
    'UPURRNAME1', 'UPURRNAME2', 'DOWNURRNAME1', 'DOWNURRNAME2',
    'URL',
}

REF_PATTERN = re.compile(r'^@([^@]+?)\.([A-Za-z0-9_]+)$')


class GenError(Exception):
    pass


def read_params(csv_path):
    """读 params.csv，返回 row 列表（dict）。"""
    p = Path(csv_path)
    if not p.exists():
        raise GenError(f'params.csv 不存在: {p}')
    rows = []
    with p.open(encoding='utf-8-sig', newline='') as f:
        rd = csv.DictReader(f)
        for r in rd:
            # 跳过重复表头 / 空行
            grp = (r.get('组') or '').strip()
            if not grp or grp == '组':
                continue
            rows.append({
                'no': (r.get('序号') or '').strip(),
                'group': grp,
                'unit': (r.get('网元') or '').strip().upper(),
                'family': (r.get('命令族') or '').strip().upper(),
                # ★ 2026-11-14 新增：动词列（ADD/MOD/SET/RMV），由 agent 按规划表填
                #   实测 NC20260819001887：规划表写「MOD POOL 修改」（190 个池改 REDUNDFUNC），
                #   但 params.csv 没记动词，代码按「POOL 现网只有 ADD」推断成 ADD POOL ×190
                #   → 会新建已存在的 190 个池，全部失败。
                'verb': (r.get('动词') or '').strip().upper(),
                'param': (r.get('参数') or '').strip().upper(),
                'value': (r.get('值') or '').strip(),
                # ★ 2026-11-05：占位符列。有值=用了命名占位符；空=真实值或组引用
                'placeholder': (r.get('占位符') or '').strip(),
                'src': (r.get('来源') or '').strip(),
                'note': (r.get('说明') or '').strip(),
            })
    return rows


def group_rows(rows):
    """按「组」聚合，保持首次出现顺序。"""
    groups = OrderedDict()
    for r in rows:
        groups.setdefault(r['group'], []).append(r)
    return groups


def resolve_refs(groups):
    """把 @组.参数 展开成实际值。

    ★ 支持链式引用（A 引用 B，B 引用 C），最多展开 5 层防环。
    """
    # 先建索引：组名 → {参数名: 行}
    index = {}
    for gid, rs in groups.items():
        index[gid] = {}
        for r in rs:
            index[gid][r['param']] = r

    def _resolve(value, depth=0):
        if depth > 5:
            raise GenError(f'引用层级过深（可能有环）: {value}')
        m = REF_PATTERN.match(value)
        if not m:
            return value
        ref_g, ref_p = m.group(1), m.group(2).upper()
        if ref_g not in index:
            raise GenError(f'引用了不存在的组: @{ref_g}.{ref_p}')
        if ref_p not in index[ref_g]:
            raise GenError(f'组 {ref_g} 里没有参数 {ref_p}')
        raw = index[ref_g][ref_p]['value']
        return _resolve(raw, depth + 1)

    for gid, rs in groups.items():
        for r in rs:
            if r['value'].startswith('@'):
                r['value_resolved'] = _resolve(r['value'])
            else:
                r['value_resolved'] = r['value']
    return groups


def _quote_if_needed(param, value):
    """按参数类型决定是否加引号。"""
    if value is None:
        return '""'
    v = str(value)

    # ★ 2026-11-05：占位符的引号规则（分两种）
    #   A. 值「整体就是占位符」→ 不加引号
    #      例：URRID=【待填写】  方便人工全文搜索替换
    #   B. 占位符只是值的「一部分」→ 照常加引号
    #      例：FILTERNAME="<PFX>_00_f_h_001"  这是变量+后缀，是字符串
    _is_whole_placeholder = (
        v.startswith('【') and v.endswith('】') and v.count('【') == 1
    ) or (
        v.startswith('<') and v.endswith('>') and v.count('<') == 1
    ) or v.startswith('{')
    if _is_whole_placeholder:
        return v

    if param in ENUM_PARAMS:
        return v
    if param in QUOTED_PARAMS:
        return f'"{v}"'
    # 纯数字/纯枚举不加引号
    if re.fullmatch(r'-?\d+', v):
        return v
    if re.fullmatch(r'[A-Za-z0-9_]+', v) and param not in QUOTED_PARAMS:
        return v
    return f'"{v}"'


# 这些族用 SET 而不是 ADD（大部分配置命令是 ADD，少部分是 SET）
SET_FAMILIES = {
    'URRGRPBINDING', 'REFRESHSRV', 'LICENSESWITCH', 'CFGTHRESHOLD',
    'REFRESH',
}

# csv 里可能写的族名 → 真实 MML 族名
#   ★ 2026-11-05 实测：agent 在 csv 里写 REFRESH，实际命令是 SET REFRESHSRV
FAMILY_ALIAS = {
    'REFRESH': 'REFRESHSRV',
    'URRPGBINDING': 'URRGRPBINDING',
}


def build_command(group_rows_):
    """一组行 → 一条 MML 命令。"""
    if not group_rows_:
        return None
    fam = group_rows_[0]['family']
    if not fam:
        return None

    # ★ 2026-11-06：族名可以带动词前缀（"ADD FILTER" / "RMV FILTER" / "SET URR"）
    #   实测 GT 里删除命令占不小比例（87 工单 18257 条里 RMV 有上千条），
    #   原来动词写死 ADD/SET，根本表达不出删除意图。
    verb = ''
    m = re.match(r'^(ADD|RMV|SET|MOD)\s+([A-Za-z0-9_]+)$', fam.strip(), re.I)
    if m:
        verb = m.group(1).upper()
        fam = m.group(2).upper()
    else:
        fam = FAMILY_ALIAS.get(fam, fam)
        # ★ 2026-11-12：改用 verb_rules（数据驱动，67 个 SET_ONLY 族）
        #   原来只硬编码 5 个族，导致 60 个族的 SET 被误写成 ADD
        #
        #   ★ 同时加族名自动校正：
        #     实测 NC20260814000701 的 params.csv 里写的是 REFREFSHSRV（多写 REF），
        #     SET_ONLY 里没这个名字 → 判不出 SET → 落回 ADD → 产出非法命令。
        #     这里做一次「近似名纠错」：若族名不在规则里但与某个 SET_ONLY 族
        #     相似度 >= 0.85，则校正为该族。
        verb = None
        try:
            from verb_rules import get_rules as _get_vr
            _vr = _get_vr()
            if not _vr.is_set_only(fam):
                import difflib as _dl
                cands = _dl.get_close_matches(fam, sorted(_vr.set_only),
                                              n=1, cutoff=0.85)
                if cands:
                    # 记录校正，供上层标注
                    fam = cands[0]
                    verb = 'SET'
            if verb is None:
                verb = _vr.verb_for(fam, default='ADD')
        except Exception:
            verb = 'SET' if fam in SET_FAMILIES else 'ADD'

    # ★★ 2026-11-14：params.csv 里显式写了动词就用它（优先级最高）
    #   规划表是 agent 判断的业务动作，规则表只能从现网推断「这个族通常用什么动词」，
    #   判不了本次要做什么。
    #   实测 NC20260819001887：POOL 现网只有 ADD（1333 条），规则表推 ADD，
    #   但本次要 MOD（改 190 个池的 REDUNDFUNC）→ 必须听 agent 的。
    #
    # ★ 2026-11-14 补充（用户指出「动词不止这些」）：
    #   MML 动词远不止 ADD/MOD/SET/RMV。按 KB 的 MML 文档实测分布：
    #     配置类：add(4008) mod(2726) rmv(4200) set(3014)
    #     操作类：act(122) dea(32) rtr(322) str(134) rst(82) stp(62)
    #             clr(102) opr(90) syn(44) lod(46) lck(44) rbl(24) upd
    #     查询类：lst/dsp/tst/exp —— 只读，不会进产物
    #   产物生成需要支持「会改变数据/状态」的全部动词，不能只认 4 个。
    _csv_verb = (group_rows_[0].get('verb') or '').strip().upper() if group_rows_ else ''
    if _csv_verb in DATA_VERBS:
        verb = _csv_verb

    parts = []
    for r in group_rows_:
        p = r['param']
        v = r.get('value_resolved', r['value'])
        if not p:
            continue
        parts.append(f'{p}={_quote_if_needed(p, v)}')
    if not parts:
        return None
    # 行尾 @src 注释（取该组第一行的来源，多来源合并）
    srcs = []
    for r in group_rows_:
        s = r.get('src') or ''
        if s and s not in srcs:
            srcs.append(s)
    tail = ''
    if srcs:
        tail = '   // ' + ' '.join(f'@src={s}' if not s.startswith('@src=') else s
                                   for s in srcs[:3])
    return f'{verb} {fam}:{", ".join(parts)};{tail}'


# ★ 2026-11-14：MML 会改变数据/状态的动词（产物生成只认这些）
#   来源：KB 的 MML 文档文件名前缀分布 + 现网 EXP 实测
#   查询类（lst/dsp/tst/exp）不在此列 —— 只读命令不进配置产物
DATA_VERBS = frozenset({
    # 配置类
    'ADD', 'MOD', 'RMV', 'SET',
    # 操作类（不改数据结构，但改变运行状态，也属于配置动作）
    'ACT', 'DEA',          # 激活 / 去激活
    'RTR', 'RST', 'STR', 'STP',   # 复位 / 重置 / 启动 / 停止
    'CLR', 'OPR',          # 清除 / 操作
    'SYN', 'LOD', 'RBL', 'UPD',   # 同步 / 加载 / 重载 / 更新
    'LCK', 'ULK',          # 锁定 / 解锁
})


def gen_mml(csv_path, with_unit_sections=True):
    """主入口：params.csv → MML 文本。

    Returns {'text': str, 'units': [..], 'n_commands': int, 'errors': [..]}
    """
    rows = read_params(csv_path)
    if not rows:
        return {'text': '', 'units': [], 'n_commands': 0,
                'errors': ['params.csv 里没有有效行（「组」列为空？）']}

    groups = group_rows(rows)
    try:
        groups = resolve_refs(groups)
    except GenError as e:
        return {'text': '', 'units': [], 'n_commands': 0, 'errors': [str(e)]}

    # 按网元分组（多网元时输出分段）
    units = []
    for gid, rs in groups.items():
        u = rs[0]['unit'] or ''
        if u and u not in units:
            units.append(u)

    multi_unit = with_unit_sections and len(units) > 1
    out = []
    errors = []
    n_cmd = 0

    if multi_unit:
        for u in units:
            out.append(f'/* ===== 网元: {u} ===== */')
            for gid, rs in groups.items():
                if (rs[0]['unit'] or '') != u:
                    continue
                cmd = build_command(rs)
                if cmd:
                    out.append(cmd)
                    n_cmd += 1
            out.append('')
    else:
        for gid, rs in groups.items():
            cmd = build_command(rs)
            if cmd:
                out.append(cmd)
                n_cmd += 1

    return {
        'text': '\n'.join(out).strip() + '\n',
        'units': units if multi_unit else [],
        'n_commands': n_cmd,
        'n_groups': len(groups),
        'errors': errors,
    }


# ═══════════════════════════════════════════════════════════
# 占位符处理（G22）
# ═══════════════════════════════════════════════════════════
PH_RE = re.compile(r'【([^】]+)】')


def collect_placeholders(rows):
    """收集所有占位符及其出现位置。

    Returns {name: [{group, param, family, unit, note, no}], ...}
    """
    out = {}
    for r in rows:
        # 「占位符」列有值 → 这是命名占位符
        ph_col = r.get('placeholder') or ''
        val = r.get('value') or ''
        # 值列里的【XXX】
        vals = PH_RE.findall(val) if val else []
        names = set()
        if ph_col:
            names.add(ph_col.strip('【】'))
        for v in vals:
            names.add(v)
        for nm in names:
            out.setdefault(nm, []).append({
                'no': r.get('no'), 'group': r.get('group'),
                'unit': r.get('unit'), 'family': r.get('family'),
                'param': r.get('param'), 'note': r.get('note'),
            })
    return out


def check_placeholders(rows):
    """G22 占位符一致性校验。

    规则：
      1. 「占位符」列有值 → 「值」列必须是【同名】（或直接是真实值=已填完）
      2. 「占位符」列为空 → 「值」列不能包含【】（会产生孤立占位符）
      3. 同一占位符在不同族用 → 警告（可能语义冲突）
    """
    errors = []
    warnings = []
    ph_map = collect_placeholders(rows)

    # 规则 1：占位符列和值列一致
    for r in rows:
        ph_col = (r.get('placeholder') or '').strip().strip('【】')
        val = (r.get('value') or '').strip()
        if not ph_col:
            # 规则 2：列为空但值里有【】
            if PH_RE.search(val):
                errors.append(
                    f"第 {r.get('no')} 行（{r['group']}.{r['param']}）的值含占位符 {val}，"
                    f"但「占位符」列为空，应填写占位符名")
            continue
        # 有占位符名：值要么是【同名】，要么已经是真实值（用户填完了）
        if val.startswith('【'):
            got = val.strip('【】')
            if got != ph_col:
                errors.append(
                    f"第 {r.get('no')} 行「值」是 {val}，"
                    f"但「占位符」列写的是 {ph_col}，两者不一致")

    # 规则 3：同一占位符跨族使用
    for name, occ in ph_map.items():
        fams = {o['family'] for o in occ}
        if len(fams) > 1:
            warnings.append(
                f'占位符【{name}】被 {len(fams)} 个族使用（'
                + '、'.join(sorted(fams)) + '），确认语义是否一致')

    return {
        'ok': not errors,
        'errors': errors[:10],
        'warnings': warnings[:10],
        'n_placeholders': len(ph_map),
        'placeholders': {
            k: {'count': len(v),
                'groups': sorted({x['group'] for x in v}),
                'families': sorted({x['family'] for x in v})}
            for k, v in list(ph_map.items())[:20]
        },
    }


def list_unfilled(csv_path):
    """列还没填的占位符（值仍是【XXX】的）。"""
    rows = read_params(csv_path)
    unfilled = {}
    for r in rows:
        val = r.get('value') or ''
        m = PH_RE.search(val)
        if m:
            unfilled.setdefault(m.group(1), []).append({
                'no': r.get('no'), 'group': r.get('group'),
                'param': r.get('param'), 'note': r.get('note'),
            })
    return unfilled


# ═══════════════════════════════════════════════════════════
# 一致性比对（G21）
# ═══════════════════════════════════════════════════════════
def normalize_cmd(line):
    """归一化命令用于比对：去注释、去空格、参数排序。"""
    s = (line or '').strip()
    if not s or s.startswith(('/*', '//', '#')):
        return None
    # 去行尾注释
    m = re.search(r'\s+//\s*', s)
    if m:
        s = s[:m.start()].rstrip()
    elif ';' in s and '@src=' in s[s.index(';'):]:
        s = s[:s.index(';') + 1]
    mm = re.match(r'^(\w+)\s+([A-Za-z0-9_]+)\s*:(.*)$', s, re.S)
    if not mm:
        return None
    verb, fam, rest = mm.group(1).upper(), mm.group(2).upper(), mm.group(3)
    rest = rest.strip().rstrip(';')
    params = []
    cur, inq = '', False
    for ch in rest:
        if ch == '"':
            inq = not inq
            cur += ch
        elif ch == ',' and not inq:
            params.append(cur.strip())
            cur = ''
        else:
            cur += ch
    if cur.strip():
        params.append(cur.strip())
    params = [re.sub(r'\s+', '', p) for p in params if p]
    params.sort()
    return f'{verb} {fam}:{", ".join(params)}'


def _strip_quotes(s):
    """归一化时去掉参数的引号差异。

    ★ 引号是否保留取决于参数类型和值形态（占位符不加、字符串加），
      但 G21 关心的是「参数值是否正确」，不是「引号是否一致」。
      所以比对时统一剥掉引号。
    """
    return re.sub(r'"([^"]*)"', r'\1', s or '')


def compare_mml(agent_mml, gen_mml):
    """比对 agent 写的 mml 和代码生成的 mml。

    Returns {'ok': bool, 'only_in_agent': [...], 'only_in_gen': [...], ...}
    """
    def _set(t):
        out = set()
        for ln in (t or '').split('\n'):
            n = normalize_cmd(ln)
            if n:
                out.add(_strip_quotes(n))
        return out

    a = _set(agent_mml)
    g = _set(gen_mml)
    only_a = sorted(a - g)
    only_g = sorted(g - a)
    return {
        'ok': not only_a and not only_g,
        'n_agent': len(a),
        'n_gen': len(g),
        'n_common': len(a & g),
        'only_in_agent': only_a[:10],
        'only_in_gen': only_g[:10],
        'n_only_agent': len(only_a),
        'n_only_gen': len(only_g),
    }


if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print('用法: mml_gen.py <params.csv> [--out mml.txt] [--compare mml.txt]')
        sys.exit(1)
    r = gen_mml(sys.argv[1])
    if r['errors']:
        print('错误:', r['errors'])
        sys.exit(2)
    print(r['text'])
    print(f'# {r["n_commands"]} 条命令 / {r["n_groups"]} 组 / 网元 {r["units"]}')

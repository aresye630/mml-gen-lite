#!/usr/bin/env python3
"""mcp_exp.py — EXP 分析 MCP server。

★ 设计原则
  EXP 分析是**纯确定性代码**（格式固定 → 解析规则固定），不需要 LLM 判断。
  把它做成 MCP 工具，让 agent 按需调用，而不是在 prompt 里塞一堆统计结果。

★ 5 个工具
  exp_detect   判断文件是不是 EXP（三行头校验），提取 ME Type/Version
  exp_stats    统计：每族条数 / 命名规律 / 优先级区间 / 枚举分布
  exp_query    按条件查命令
  exp_refs     查对象的引用关系
  exp_baseline 提取某几族的典型写法

★ 协议：MCP over stdio（JSON-RPC 2.0，每行一个消息）
"""
import json
import os
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

# ═══════════════════════════════════════════════════════════
# EXP 头部校验（实证 221/221 = 100%，覆盖 UDG/UEG/UNC/UDC）
# ═══════════════════════════════════════════════════════════
EXP_HEADER_PATTERNS = [
    (1, re.compile(r'^/\* TIME = \d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d+(\+8:00)? \*/$')),
    (2, re.compile(r'^/\* ME Type=(\w+), Version=([\d.]+)\s+PatchVersion=([\d.]+) \*/$')),
    (3, re.compile(r'^/\*USE ME:MEID=(\d+);\*/$')),
]

# 引用型参数后缀（哪些参数值指向"别的对象"）
REF_SUFFIX = re.compile(
    r'(NAME|NAMES|INSTANCE|INSTANCENAME|IFNAME|VRFNAME|APN|DNN|POOLNAME'
    r'|GROUPNAME|PROFILENAME|POLICYNAME|RULENAME|TEMPLATENAME|AREANAME'
    r'|SERVERNAME|HOSTNAME|SECTIONNAME|L3VPNNAME)$', re.I)

VERB_RE = re.compile(r'^\s*(ADD|MOD|RMV|SET|DEL|LST)\s+([A-Z0-9_]+)\s*[:;]', re.I)


# ═══════════════════════════════════════════════════════════
# 基础解析
# ═══════════════════════════════════════════════════════════
def read_text(path):
    """读文本，自动识别编码。"""
    p = Path(path)
    raw = p.read_bytes()
    for enc in ('utf-8', 'gbk', 'gb18030', 'utf-16'):
        try:
            return raw.decode(enc), enc
        except (UnicodeDecodeError, LookupError):
            continue
    return raw.decode('utf-8', errors='replace'), 'utf-8(replace)'


def split_cmd(line):
    """拆成 (verb, family, params_dict)。"""
    m = re.match(r'^(\w+)\s+([A-Za-z0-9_]+)\s*:(.*)$', line, re.S)
    if not m:
        return None, None, {}
    verb, fam, rest = m.group(1).upper(), m.group(2).upper(), m.group(3).strip().rstrip(';')
    params = {}
    cur = ''
    in_q = False
    for ch in rest:
        if ch == '"':
            in_q = not in_q
            cur += ch
        elif ch == ',' and not in_q:
            _kv(cur, params)
            cur = ''
        else:
            cur += ch
    if cur.strip():
        _kv(cur, params)
    return verb, fam, params


def _kv(s, out):
    s = s.strip()
    if not s:
        return
    if '=' in s:
        k, v = s.split('=', 1)
        out[k.strip().upper()] = v.strip().strip('"')
    else:
        out[s.upper()] = ''


def iter_commands(text):
    """遍历命令（跳过注释块）。yield (line_no, verb, family, params, raw)。"""
    in_block = False
    for ln, raw in enumerate(text.split('\n'), 1):
        line = raw.strip()
        if not line:
            continue
        if line.startswith('/*'):
            in_block = '*/' not in line
            continue
        if in_block:
            if '*/' in line:
                in_block = False
            continue
        if line.startswith(('//', '#')):
            continue
        m = VERB_RE.match(line)
        if not m:
            continue
        v, f, p = split_cmd(line)
        if v and f:
            yield ln, v, f, p, line


def _is_placeholder(v):
    v = str(v or '')
    return ('【' in v or v.upper().startswith('TBD') or '{TODO' in v.upper()
            or v.startswith('<') or v == '')


# ═══════════════════════════════════════════════════════════
# 工具 1：exp_detect
# ═══════════════════════════════════════════════════════════
def tool_exp_detect(args):
    """判断文件是不是 EXP 快照。"""
    path = args.get('path') or ''
    p = Path(path)
    if not p.exists():
        return {'error': f'文件不存在: {path}'}

    text, enc = read_text(p)
    lines = text.split('\n')

    result = {
        'path': str(p),
        'size': p.stat().st_size,
        'encoding': enc,
        'is_exp': False,
        'me_type': None,
        'version': None,
        'patch_version': None,
        'cmd_count': 0,
        'header_ok': [],
    }

    # 三行头校验
    ok_all = True
    for ln_no, pat in EXP_HEADER_PATTERNS:
        if len(lines) < ln_no:
            ok_all = False
            result['header_ok'].append({'line': ln_no, 'ok': False, 'reason': '行数不足'})
            continue
        line = lines[ln_no - 1].strip()
        m = pat.match(line)
        result['header_ok'].append({'line': ln_no, 'ok': bool(m),
                                    'content': line[:80]})
        if not m:
            ok_all = False
        elif ln_no == 2:
            result['me_type'] = m.group(1)
            result['version'] = m.group(2)
            result['patch_version'] = m.group(3)

    # 命令数统计
    n = 0
    for _ in iter_commands(text):
        n += 1
    result['cmd_count'] = n
    result['is_exp'] = ok_all and n > 0

    return result


# ═══════════════════════════════════════════════════════════
# 工具 2：exp_stats
# ═══════════════════════════════════════════════════════════
# ★ 2026-11-06 性能优化：EXP 解析结果内存缓存
#
#   实测（86 工单）：
#     EXP 查询是最大耗时项，平均 15-38 次/工单
#     agent 逐族查（FILTER、FILTERIPV6、POOLGRPMAP…），每次都重读重解析
#     42MB EXP 单次 1.97s，20 次 = 40 秒纯浪费
#
#   缓存策略：按 (path, size, mtime) 作 key，同一文件只解析一次
#     mcp server 是常驻进程（for line in sys.stdin），缓存跨请求有效
#     换 EXP（size/mtime 变）自动失效
_PARSE_CACHE = {}
_RESULT_CACHE = {}  # exp_stats 结果缓存（同文件同参数）
_CACHE_MAX = 8      # 最多缓存 8 份 EXP，防内存爆（8 × 300MB 解析结果）


def _get_parsed(path):
    """读取并解析 EXP，带缓存。返回 (text, enc, cmds)。"""
    import os
    p = Path(path)
    try:
        st = p.stat()
        key = (str(p), st.st_size, st.st_mtime)
    except Exception:
        key = (str(p), 0, 0)

    if key in _PARSE_CACHE:
        return _PARSE_CACHE[key]

    text, enc = read_text(p)
    cmds = list(iter_commands(text))
    val = (text, enc, cmds)

    if len(_PARSE_CACHE) >= _CACHE_MAX:
        _PARSE_CACHE.pop(next(iter(_PARSE_CACHE)))
    _PARSE_CACHE[key] = val
    return val


def tool_exp_stats(args):
    """统计 EXP 的命令族分布、命名规律、优先级区间、枚举分布。

    ★ 2026-11-06 性能优化：结果缓存
      实测：45MB EXP 冷查 3.69s，热查 1.98s（解析已缓存但统计还要遍历 10 万条）
      agent 一单会调 15-38 次 exp_stats，如果参数相同结果完全一样
      → 按 (path, size, mtime, family) 缓存完整结果，重复查询 0.00s
    """
    path = args.get('path') or ''
    want_families = args.get('family')
    p = Path(path)
    if not p.exists():
        return {'error': f'文件不存在: {path}'}

    # 结果缓存
    try:
        st = p.stat()
        fam_key = want_families if isinstance(want_families, str) else (
            tuple(want_families) if want_families else None)
        res_key = ('stats', str(p), st.st_size, st.st_mtime, fam_key)
        if res_key in _RESULT_CACHE:
            return _RESULT_CACHE[res_key]
    except Exception:
        res_key = None

    text, enc, _all_cmds = _get_parsed(p)

    fam_cnt = Counter()
    fam_names = defaultdict(list)       # family -> [首个参数值（名字）]
    fam_params = defaultdict(lambda: defaultdict(set))   # family -> {param: {values}}

    for _ln, v, f, params, _raw in iter_commands(text):
        if v != 'ADD':
            continue
        key = f
        fam_cnt[key] += 1
        # 第一个参数当作"对象名"
        if params:
            first_k = next(iter(params))
            first_v = params[first_k]
            if first_v and not _is_placeholder(first_v):
                fam_names[key].append(first_v)
        # 收集参数值（每族每参数最多记 200 个，防爆内存）
        for k, val in params.items():
            if val and not _is_placeholder(val):
                s = fam_params[key][k]
                if len(s) < 200:
                    s.add(val)

    # 按需过滤
    if want_families:
        if isinstance(want_families, str):
            want_families = [want_families]
        wf = {x.upper() for x in want_families}
        fam_cnt = Counter({k: v for k, v in fam_cnt.items() if k in wf})

    families = {}
    for fam, n in fam_cnt.most_common():
        names = fam_names.get(fam) or []
        entry = {
            'count': n,
            'sample_names': names[:5],
        }
        # 命名规律：把数字段替换成 N，统计最常见的骨架
        if names:
            shapes = Counter()
            for nm in names:
                shapes[re.sub(r'\d+', 'N', nm)] += 1
            entry['name_patterns'] = [
                {'pattern': k, 'count': v} for k, v in shapes.most_common(3)]
            # 序号范围
            nums = []
            for nm in names:
                mm = re.findall(r'\d+', nm)
                if mm:
                    nums.append(int(mm[-1]))
            if nums:
                entry['number_range'] = [min(nums), max(nums)]

        # 优先级区间
        pri = fam_params[fam].get('PRIORITY') or set()
        if pri:
            try:
                pv = sorted(int(x) for x in pri if x.isdigit())
                if pv:
                    entry['priority_range'] = [pv[0], pv[-1]]
            except Exception:
                pass

        # 枚举分布（最多 3 个参数，每个最多 8 个值）
        enums = {}
        for k, vs in list(fam_params[fam].items())[:12]:
            if k in ('PRIORITY',):
                continue
            if 1 < len(vs) <= 20:
                enums[k] = sorted(vs)[:8]
            if len(enums) >= 3:
                break
        if enums:
            entry['enums'] = enums

        families[fam] = entry

    result = {
        'path': str(p),
        'encoding': enc,
        'total_cmds': sum(fam_cnt.values()),
        'family_count': len(families),
        'families': families,
    }
    # 写入结果缓存（同文件同参数重复查 → 0 开销）
    if res_key:
        if len(_RESULT_CACHE) >= _CACHE_MAX * 4:
            _RESULT_CACHE.pop(next(iter(_RESULT_CACHE)))
        _RESULT_CACHE[res_key] = result
    return result


# ═══════════════════════════════════════════════════════════
# 工具 3：exp_query
# ═══════════════════════════════════════════════════════════
def tool_exp_query(args):
    """按条件查命令。"""
    path = args.get('path') or ''
    fam = (args.get('family') or '').upper()
    param = (args.get('param') or '').upper()
    value = args.get('value') or ''
    limit = int(args.get('limit') or 30)

    p = Path(path)
    if not p.exists():
        return {'error': f'文件不存在: {path}'}

    text, _, _all_cmds = _get_parsed(p)
    hits = []
    for ln, v, f, params, raw in _all_cmds:
        if fam and f != fam:
            continue
        if param:
            pv = params.get(param)
            if pv is None:
                continue
            if value and value.lower() not in str(pv).lower():
                continue
        elif value:
            # 没指定 param，就在所有值里找
            if not any(value.lower() in str(x).lower() for x in params.values()):
                continue
        hits.append({'line': ln, 'verb': v, 'family': f, 'cmd': raw[:300]})
        if len(hits) >= limit:
            break

    return {'path': str(p), 'count': len(hits), 'results': hits}


# ═══════════════════════════════════════════════════════════
# 工具 4：exp_refs
# ═══════════════════════════════════════════════════════════
def tool_exp_refs(args):
    """查某个对象的引用关系（被谁引用 / 引用了谁）。"""
    path = args.get('path') or ''
    name = args.get('object_name') or ''
    p = Path(path)
    if not p.exists():
        return {'error': f'文件不存在: {path}'}
    if not name:
        return {'error': 'object_name 必填'}

    text, _, _all_cmds = _get_parsed(p)

    defined_by = []      # 谁定义了它
    referenced_by = []   # 谁引用了它
    refs_of = {}         # 它引用了谁（只对定义它的那条命令）

    for ln, v, f, params, raw in _all_cmds:
        # 是不是定义（ADD 的第一个参数等于 name）
        if v == 'ADD' and params:
            first_k = next(iter(params))
            if params[first_k] == name:
                defined_by.append({'line': ln, 'family': f, 'param': first_k,
                                   'cmd': raw[:200]})
                # 它引用的其他对象
                for k, val in params.items():
                    if k != first_k and REF_SUFFIX.search(k) and val and not _is_placeholder(val):
                        refs_of.setdefault(k, []).append(val)

        # 是不是引用
        for k, val in params.items():
            if REF_SUFFIX.search(k) and val == name:
                referenced_by.append({'line': ln, 'family': f, 'param': k,
                                      'cmd': raw[:200]})

    return {
        'path': str(p),
        'object_name': name,
        'defined': defined_by[:5],
        'referenced_by': referenced_by[:20],
        'referenced_by_count': len(referenced_by),
        'refs_of': {k: v[:5] for k, v in list(refs_of.items())[:10]},
    }


# ═══════════════════════════════════════════════════════════
# 工具 5：exp_baseline
# ═══════════════════════════════════════════════════════════
def tool_exp_baseline(args):
    """提取某几族的典型写法（供 agent 参考格式）。"""
    path = args.get('path') or ''
    fams = args.get('families') or []
    per_family = int(args.get('per_family') or 2)

    p = Path(path)
    if not p.exists():
        return {'error': f'文件不存在: {path}'}
    if isinstance(fams, str):
        fams = [fams]
    fams = [f.upper() for f in fams]

    text, _, _all_cmds = _get_parsed(p)
    buckets = defaultdict(list)

    for ln, v, f, params, raw in _all_cmds:
        if v != 'ADD':
            continue
        if fams and f not in fams:
            continue
        if len(buckets[f]) >= per_family:
            continue
        # 优先选不含占位符的样例
        has_ph = any(_is_placeholder(x) for x in params.values())
        if has_ph and len(buckets[f]) > 0:
            continue
        buckets[f].append({'line': ln, 'cmd': raw[:400]})

    return {
        'path': str(p),
        'samples': {f: v for f, v in buckets.items()},
        'families_found': sorted(buckets.keys()),
    }


# ═══════════════════════════════════════════════════════════
# MCP 协议（stdio，JSON-RPC 2.0）
# ═══════════════════════════════════════════════════════════


def tool_exp_siblings(args):
    """发现与指定命令族「配套」的其他族（从现网 EXP 数量共现学）。

    ★ 2026-11-08 新增
    问题：agent 建 ADD POOL 时不知道还要建 POOLGROUP / POOLBINDGROUP / POOLGRPMAP，
         导致大工单只配了表层（SECTION），漏掉整条业务链。
         实测 NC20260824002208：GT 645 条（POOL 97 + POOLGROUP 97 +
         POOLBINDGROUP 97 + POOLGRPMAP 247 + SECTION 98），
         产物只配了 SECTION 98 条。

    原理：如果现网里族 A 和族 B 的对象数量接近（比值 ≥ 阈值），
         说明它们总是成对出现，属于配套关系。
         实测：ADD POOL ↔ POOLGROUP 0.98、POOL ↔ POOLBINDGROUP 0.99、
               POOLGROUP ↔ POOLBINDGROUP 0.97

    ★ 不硬编码任何族名，全靠 EXP 统计。

    args:
      path:       EXP 文件路径（必填）
      families:   要查的族，如 ["ADD POOL"]；不填则返回全部高共现对
      min_ratio:  配套判定阈值，默认 0.7
      min_count:  最小对象数（过滤样本太少的族），默认 20

    returns:
      {families: {族: {count, siblings: [{family, ratio, count}]}}}
    """
    path = args.get('path') or ''
    fams = args.get('families') or []
    min_ratio = float(args.get('min_ratio') or 0.7)
    min_count = int(args.get('min_count') or 20)

    p = Path(path)
    if not p.exists():
        return {'error': f'文件不存在: {path}'}

    if isinstance(fams, str):
        fams = [fams]
    # 查询参数可能带动词（如 'ADD POOL'），归一化成纯族名
    def _bare_fam(x):
        parts = str(x).strip().upper().split()
        return parts[-1] if parts else ''

    fams = [_bare_fam(f) for f in fams if f and str(f).strip()]
    fams = [f for f in fams if f]

    text, _, all_cmds = _get_parsed(p)

    # 统计每族 ADD 数量
    #   cnt 的 key 是纯族名（如 'POOL'），不带动词
    cnt = Counter()
    for ln, v, f, params, raw in all_cmds:
        if v == 'ADD':
            cnt[f] += 1

    # 过滤样本太少的族（噪音）
    cand = {f: n for f, n in cnt.items() if n >= min_count}

    # ★ 2026-11-08：加互信息权重，过滤「数量碰巧接近」的假配套
    #   实测反例：ADD POOL ↔ URR ratio=0.985，但二者毫无业务关系，
    #   只是现网里 URR 数量和 POOL 数量碰巧接近。
    #   真配套的特征：A 出现的地方 B 也出现（同一条命令/同一对象内），
    #   或者 A 和 B 的参数值互相引用。
    #   这里用「参数值交集」做交叉验证：A 的参数值里有 B 的某个参数值的比例。

    # 收集每族的参数值集合（取样，避免内存爆）
    fam_vals = defaultdict(set)
    fam_val_count = Counter()
    _SAMPLE_PER_FAM = 500
    for ln, v, f, params, raw in all_cmds:
        if v != 'ADD':
            continue
        if fam_val_count[f] >= _SAMPLE_PER_FAM:
            continue
        fam_val_count[f] += 1
        for _k, _v in params.items():
            if _v and len(_v) < 200:
                fam_vals[f].add(_v.upper())

    def value_overlap(a, b):
        """两族的参数值交集比例（取小的当分母）。"""
        va, vb = fam_vals.get(a) or set(), fam_vals.get(b) or set()
        if not va or not vb:
            return 0.0
        inter = len(va & vb)
        return inter / min(len(va), len(vb))

    # ★★ 2026-11-08 最终判据：参数值引用关系（最可靠）
    #   实测 POOL 的配套族：
    #     ADD POOLGROUP:POOLGRPNAME="grp-x"
    #     ADD POOLBINDGROUP:POOLGROUPNAME="grp-x", POOLNAME="pool-y"  ← 引用 POOLGROUP
    #     ADD SECTION:SECTIONNUM=0, POOLNAME="pool-y"                ← 引用 POOL
    #   这种「A 的主键值出现在 B 的参数值里」是真实的配置依赖，
    #   比数量巧合（POOL↔URR 0.985 但毫无关系）可靠得多。

    # 采集每族的主键值（第一个参数值）
    fam_pks = defaultdict(set)
    for ln, v, f, params, raw in all_cmds:
        if v != 'ADD' or not params:
            continue
        if len(fam_pks[f]) >= 2000:
            continue
        first_val = next(iter(params.values()))
        if first_val and len(first_val) < 200:
            fam_pks[f].add(first_val.upper())

    # ★ 2026-11-08 修正：只认「主键值」被引用，不认普通参数值
    #   反例：POOL 和 SRROUTE6 都有 VPNINSTANCE="ChinaMobile_SGi"，
    #        于是误判 POOL↔SRROUTE6 配套（GT 里共现 0 次）。
    #   正确的是：A 的主键值出现在 B 的「主键以外的参数」里，且该参数名带 A 的族名特征。
    #
    #   实现：把每族的「非主键参数值」建索引，看 target 的主键值能否在里面找到
    fam_nonpk_vals = defaultdict(set)
    for ln, v, f, params, raw in all_cmds:
        if v != 'ADD' or not params:
            continue
        if len(fam_nonpk_vals[f]) >= 5000:
            continue
        vals = list(params.values())
        for _v in vals[1:]:     # 跳过第一个（主键）
            if _v and len(_v) < 200:
                fam_nonpk_vals[f].add(_v.upper())

    # ★★ 2026-11-08 终极判据：参数名指向（MML 语法约定）
    #   MML 里引用别的对象时，参数名就是目标族名 + NAME/NAMES/INSTANCE 后缀：
    #     ADD POOLBINDGROUP:POOLGROUPNAME="grp-x", POOLNAME="pool-y"
    #                       ^^^^^^^^^^^^^ 指向 POOLGROUP   ^^^^^^^^ 指向 POOL
    #     ADD SECTION:SECTIONNUM=0, POOLNAME="pool-y"     ← 指向 POOL
    #     ADD POOLGRPMAP:MAPPINGNAME="m", APN="a", POOLGROUPNAME="grp-x" ← 指向 POOLGROUP
    #
    #   这个判据不受共享值影响（VRF/VPN 名是值相同，但参数名不指向对方族）。
    #   实测验证：POOL↔SRROUTE6 用值交集会误判 33%，
    #            用参数名指向则是 0（SRROUTE6 没有 POOLNAME 参数）。

    # 采集每族的参数名集合
    fam_params = defaultdict(set)
    for ln, v, f, params, raw in all_cmds:
        if v != 'ADD':
            continue
        for _k in params.keys():
            fam_params[f].add(_k.upper())

    def param_refs(a, b):
        """b 里有多少参数名指向 a（如 b 有 POOLNAME/POGROUPNAME 之类）。"""
        params_b = fam_params.get(b) or set()
        if not params_b:
            return 0.0
        a_up = a.upper()
        # 目标族名可能带下划线变体：POOL → POOLNAME / POOLNAMES
        hits = 0
        for pn in params_b:
            if pn == a_up or pn.startswith(a_up + 'NAME') or pn.startswith(a_up + 'NAMES'):
                hits += 1
            elif pn.startswith(a_up) and pn.endswith(('NAME', 'NAMES', 'INSTANCE', 'INSTANCENAME')):
                hits += 1
        return 1.0 if hits else 0.0

    def refs_of(a, b):
        """保留旧接口（值交集），但只作为辅助判据。"""
        pks = fam_pks.get(a) or set()
        vals_b = fam_nonpk_vals.get(b) or set()
        if not pks or not vals_b:
            return 0.0
        inter = len(pks & vals_b)
        return inter / len(pks)

    def siblings_of(target):
        """找 target 的配套族。

        判据优先级：
          1. 引用关系（target 的主键值出现在 other 的参数里，或反之）→ high
          2. 数量接近 + 参数值有交集 → medium
          3. 仅数量接近 → low（大概率巧合，如 POOL↔URR）
        """
        base_n = cand.get(target, 0)
        if not base_n:
            return []
        out = []
        for other, other_n in cand.items():
            if other == target:
                continue
            ratio = min(base_n, other_n) / max(base_n, other_n)

            # ★ 2026-11-08：先查参数名引用，再判数量比值
            #   原因：一对多关系（POOLGROUP 274 ↔ POOLGRPMAP 794，比值 0.34）
            #        数量差很大，但 POOLGRPMAP 确实用 POOLGROUPNAME 引用 POOLGROUP，
            #        是必须配套的。所以有引用关系时不看比值。
            p_out = param_refs(target, other)   # other 有指向 target 的参数名
            p_in = param_refs(other, target)    # target 有指向 other 的参数名

            # 有引用关系 → 直接采纳（不看比值）
            # 无引用关系 → 才用比值筛（过滤噪音）
            if not (p_out or p_in) and ratio < min_ratio:
                continue

            # 辅助判据
            r_out = refs_of(target, other)
            r_in = refs_of(other, target)
            vo = value_overlap(target, other)

            if p_out or p_in:
                conf = 'high'
                who = other if p_out else target
                who_target = target if p_out else other
                why = f'{who} 有指向 {who_target} 的参数名（MML 引用关系）'
            elif (r_out >= 0.3 or r_in >= 0.3) and vo >= 0.3:
                conf = 'medium'
                why = f'主键值被引用 {max(r_out, r_in)*100:.0f}% + 参数值交集 {vo*100:.0f}%'
            elif ratio >= 0.97:
                conf = 'low'
                why = '数量接近但无引用关系（可能巧合）'
            else:
                continue

            out.append({
                'family': other,
                'count': other_n,
                'ratio': round(ratio, 3),
                'ref_out': round(r_out, 3),
                'ref_in': round(r_in, 3),
                'value_overlap': round(vo, 3),
                'confidence': conf,
                'why': why,
            })
        _order = {'high': 0, 'medium': 1, 'low': 2}
        out.sort(key=lambda x: (_order[x['confidence']], -x['ratio']))
        return out

    def chain_of(target, depth=2):
        """传递闭包：找 target 的完整业务链。

        A -> B -> C 表示 A 的配置需要 B 配合，B 又需要 C 配合。
        实测：POOL <- POOLBINDGROUP（引用 POOL）
              POOLGROUP <- POOLBINDGROUP（引用 POOLGROUP）
              POOLGROUP <- POOLGRPMAP（引用 POOLGROUP）
              → 建 POOL 时应该连 POOLGROUP/POOLBINDGROUP/POOLGRPMAP 一起建
        """
        direct = siblings_of(target)
        reached = {target: {'family': target, 'depth': 0, 'confidence': 'self'}}
        frontier = [(target, 0)]

        for _ in range(depth):
            nxt = []
            for node, d in frontier:
                for sib in siblings_of(node):
                    f = sib['family']
                    if f in reached:
                        continue
                    # 只传播 high/medium（低置信度不传播，避免噪音扩散）
                    if sib['confidence'] not in ('high', 'medium'):
                        continue
                    reached[f] = {
                        'family': f,
                        'depth': d + 1,
                        'confidence': sib['confidence'],
                        'via': node,
                        'ratio': sib['ratio'],
                        'why': sib['why'],
                    }
                    nxt.append((f, d + 1))
            frontier = nxt
            if not frontier:
                break

        return [v for v in reached.values() if v['family'] != target]

    if fams:
        result = {}
        for f in fams:
            n = cnt.get(f, 0)
            if n == 0:
                result[f] = {'count': 0, 'siblings': [],
                             'note': f'现网 EXP 里没有 {f}，无法判断配套关系'}
                continue
                # 直接配套（1 跳）
            sibs = siblings_of(f)
            # 完整业务链（2 跳闭包）
            chain = chain_of(f, depth=2)
            result[f] = {
                'count': n,
                'siblings': sibs[:10],
                'n_siblings': len(sibs),
                'chain': sorted(chain, key=lambda x: (x['depth'], x['family']))[:20],
                'n_chain': len(chain),
            }
        return {
            'path': str(p),
            'min_ratio': min_ratio,
            'families': result,
            'hint': ('配套族 = 现网中与目标族对象数量接近的族，'
                     '通常需要一起配置才能形成完整业务链。'
                     '建议先用 exp_baseline 看配套族的典型写法。'),
        }

    # 不填 families：返回全局高共现对（用于一次性看全貌）
    pairs = []
    keys = list(cand.keys())
    for i, a in enumerate(keys):
        for b in keys[i + 1:]:
            ra = cand[a]
            rb = cand[b]
            ratio = min(ra, rb) / max(ra, rb)
            if ratio >= 0.95 and min(ra, rb) >= 50:
                pairs.append({
                    'a': a, 'b': b,
                    'count_a': ra, 'count_b': rb,
                    'ratio': round(ratio, 3),
                })
    pairs.sort(key=lambda x: (-x['ratio'], -min(x['count_a'], x['count_b'])))
    return {
        'path': str(p),
        'n_families': len(cand),
        'strong_pairs': pairs[:60],
        'note': 'strong_pairs = 数量比值 ≥0.95 的族对（几乎总是成对出现）',
    }


def _classify_pair(a, b):
    """尝试用单个算子描述 a -> b。返回 (op_name, args) 或 None。"""
    if a == b:
        return ('IDENTITY', [])

    # PREFIX_REPLACE: grp-x -> pool-x
    ma = re.match(r'^([A-Za-z]+)[-_](.+)$', a)
    mb = re.match(r'^([A-Za-z]+)[-_](.+)$', b)
    if ma and mb and ma.group(2) == mb.group(2):
        return ('PREFIX_REPLACE', [ma.group(1), mb.group(1)])

    # APPEND: sos -> sos_001
    if b.startswith(a):
        return ('APPEND', [b[len(a):]])

    # PREPEND: sos -> up_sos
    if b.endswith(a):
        return ('PREPEND', [b[:-len(a)]])

    return None


def _try_rule_chain(a, b):
    """尝试用两段算子链描述 a -> b。

    例: grp-sos-smf001-deft -> map-sos-smf001-deft-2g
        等于 PREFIX_REPLACE(grp,map) + APPEND(-2g)
    """
    ma = re.match(r'^([A-Za-z]+)[-_](.+)$', a)
    if ma:
        prefix = ma.group(1)
        rest = ma.group(2)
        idx = b.find(rest)
        if idx > 0:
            new_prefix = b[:idx].rstrip('-_')
            tail = b[idx + len(rest):]
            ops = []
            if new_prefix != prefix:
                ops.append(('PREFIX_REPLACE', [prefix, new_prefix]))
            if tail:
                ops.append(('APPEND', [tail]))
            if ops:
                return ops

    if a in b:
        idx = b.find(a)
        pre, suf = b[:idx], b[idx + len(a):]
        ops = []
        if pre:
            ops.append(('PREPEND', [pre]))
        if suf:
            ops.append(('APPEND', [suf]))
        if ops:
            return ops

    return None


def _format_ops(ops):
    """把算子链格式化成模板可用的写法。"""
    if not ops:
        return ''
    parts = []
    for name, args in ops:
        if name == 'IDENTITY':
            return ''
        parts.append(name + '(' + ','.join(str(x) for x in args) + ')')
    return '|'.join(parts)


def tool_exp_pairs(args):
    """归纳 A 族到 B 族的命名派生规律（供 agent 写批量模板用）。

    问题：agent 写模板时，需要知道 A 族对象名怎么变成 B 族对象名。
         只看几个样本容易猜错。
    做法：找出现网真实配对（B 的参数引用了 A 的主键值），
         用 derivation 的算子反向试探，归纳规律并给出覆盖率。

    args:
      path:      EXP 文件路径（必填）
      family_a:  源族名，如 "POOLGROUP"（也可写 "ADD POOLGROUP"）
      family_b:  目标族名，如 "POOL"
      limit:     最多返回多少对样本（默认 10）

    returns:
      inferred_rules 里每条的 template_suffix 可直接拼进模板：
        ${CSV.列名}|<template_suffix>
      coverage 是覆盖率，100% 才可放心用。
      unmatched 是残留配对（可能需人工确认）。
    """
    path = args.get('path') or ''
    fa = (args.get('family_a') or '').strip().upper()
    fb = (args.get('family_b') or '').strip().upper()
    limit = int(args.get('limit') or 10)

    fa = fa.split()[-1] if fa else ''
    fb = fb.split()[-1] if fb else ''

    if not fa or not fb:
        return {'error': '需要 family_a 和 family_b'}

    p = Path(path)
    if not p.exists():
        return {'error': '文件不存在: ' + path}

    text, _, all_cmds = _get_parsed(p)

    pks_a = set()
    for ln, v, f, params, raw in all_cmds:
        if v == 'ADD' and f == fa and params:
            first = next(iter(params.values()))
            if first:
                pks_a.add(first)
    # 记录 A 的主键参数名（有些族的主键名与族名不同，如 POOLGROUP 的 POOLGRPNAME）
    pk_names_a = set()
    for ln, v, f, params, raw in all_cmds:
        if v == 'ADD' and f == fa and params:
            pk_names_a.add(next(iter(params.keys())))

    if not pks_a:
        return {
            'error': '现网 EXP 里没有 ' + fa + ' 的定义',
            'family_a': fa, 'family_b': fb, 'n_pairs': 0,
        }

    pairs = []
    seen = set()
    for ln, v, f, params, raw in all_cmds:
        if v != 'ADD' or f != fb or not params:
            continue
        vals = list(params.values())
        if not vals:
            continue
        b_pk = vals[0]
        # 遍历所有参数找引用（不只 vals[1:]）
        # 反例：POOLBINDGROUP 的主键就是 POOLGROUPNAME，引用值在 vals[0] 里，
        #      原来从 vals[1:] 找就永远找不到。
        for other in vals:
            if other in pks_a and other != b_pk:
                key = (other, b_pk)
                if key not in seen:
                    seen.add(key)
                    pairs.append({'a': other, 'b': b_pk, 'line': ln})
                break
        if len(pairs) >= 2000:
            break

    # ★ 2026-11-08：两跳配对
    #   有些族之间没有直接引用，通过中间族间接关联。
    #   实测：POOLGROUP 和 POOL 无直接引用，但 POOLBINDGROUP 同时引用了两者：
    #     ADD POOLBINDGROUP:POOLGROUPNAME="grp-x", POOLNAME="pool-x"
    #   所以两族可以通过「中间族的两个参数同时命中」配对。
    matched_via = 'direct'
    if not pairs:
        # 找同时引用 A 和 B 的族
        for bridge_cand in set():
            pass
        bridge_hits = []
        for ln, v, f, params, raw in all_cmds:
            if v != 'ADD' or not params or f in (fa, fb):
                continue
            vals = list(params.values())
            hit_a = [x for x in vals if x in pks_a]
            if not hit_a:
                continue
            # 该族的这个实例是否也引用了 B 的主键？
            # 需要先知道 B 的主键全集
            bridge_hits.append((f, ln, hit_a, vals))

        # 先收集 B 的主键全集
        pks_b = set()
        for ln, v, f, params, raw in all_cmds:
            if v == 'ADD' and f == fb and params:
                first = next(iter(params.values()))
                if first:
                    pks_b.add(first)

        seen = set()
        for f, ln, hit_a, vals in bridge_hits:
            hit_b = [x for x in vals if x in pks_b]
            if hit_b:
                for ax in hit_a:
                    for bx in hit_b:
                        key = (ax, bx)
                        if key not in seen:
                            seen.add(key)
                            pairs.append({'a': ax, 'b': bx, 'line': ln, 'via': f})
        if pairs:
            matched_via = 'bridge'
            bridge_fams = sorted({p['via'] for p in pairs})

    if not pairs:
        return {
            'error': fb + ' 里没有引用 ' + fa + ' 主键的实例（含两跳）',
            'family_a': fa, 'family_b': fb, 'n_pairs': 0,
            'hint': '先用 exp_siblings 确认两族是否真的配套',
        }

    rule_counter = Counter()
    rule_examples = defaultdict(list)
    unmatched = []

    for pr in pairs:
        a_val, b_val = pr['a'], pr['b']
        single = _classify_pair(a_val, b_val)
        chain = None if single else _try_rule_chain(a_val, b_val)

        ops = [single] if single else chain
        if ops:
            expr = _format_ops(ops)
            rule_counter[expr] += 1
            if len(rule_examples[expr]) < 3:
                rule_examples[expr].append(a_val + ' -> ' + b_val)
        else:
            if len(unmatched) < 8:
                unmatched.append({'a': a_val, 'b': b_val})

    total = len(pairs)
    rules = []
    for expr, cnt in rule_counter.most_common(10):
        rules.append({
            'template_suffix': expr,
            'coverage': str(cnt) + '/' + str(total),
            'coverage_pct': round(cnt / total * 100, 1),
            'examples': rule_examples[expr],
        })

    return {
        'family_a': fa,
        'family_b': fb,
        'n_pairs': total,
        'matched_via': matched_via,
        'inferred_rules': rules,
        'n_rules': len(rules),
        'unmatched': unmatched,
        'n_unmatched': len(unmatched),
        'usage': ('把 template_suffix 直接拼在模板值的列引用后面：'
                  '${CSV.<列名>}|<template_suffix>。'
                  'coverage 100% 才可放心用；unmatched 是残留，可能需人工确认。'),
        'samples': pairs[:limit],
    }


TOOLS = [
    {
        'name': 'exp_detect',
        'description': (
            '判断一个文件是不是 MML EXP 现网快照。'
            '按固定三行头校验（TIME / ME Type / USE ME），'
            '返回 is_exp、me_type（UDG/UNC/UEG/UDC）、version、命令总数。'
            'workspace 里有多个文件时，先调这个确认哪个是现网基线。'
        ),
        'inputSchema': {
            'type': 'object',
            'properties': {
                'path': {'type': 'string', 'description': '文件路径（uploads/ 或 uploads_text/ 下）'},
            },
            'required': ['path'],
        },
    },
    {
        'name': 'exp_stats',
        'description': (
            '统计 EXP 里各命令族的分布情况：每个族多少条、命名规律（骨架+序号范围）、'
            'PRIORITY 区间、关键参数的枚举值分布。'
            '用来摸清现网命名习惯和取值规律，避免编造。'
        ),
        'inputSchema': {
            'type': 'object',
            'properties': {
                'path': {'type': 'string', 'description': 'EXP 文件路径'},
                'family': {
                    'description': '只看某几个族（字符串或数组），不传则统计全部',
                    'oneOf': [
                        {'type': 'string'},
                        {'type': 'array', 'items': {'type': 'string'}},
                    ],
                },
            },
            'required': ['path'],
        },
    },
    {
        'name': 'exp_query',
        'description': (
            '在 EXP 里按条件查命令。可按命令族、参数名、参数值过滤。'
            '例：查所有 ADD URR；查 FILTERNAME 含 hngd 的命令。'
        ),
        'inputSchema': {
            'type': 'object',
            'properties': {
                'path': {'type': 'string'},
                'family': {'type': 'string', 'description': '命令族，如 URR / HOST'},
                'param': {'type': 'string', 'description': '参数名，如 FILTERNAME'},
                'value': {'type': 'string', 'description': '参数值（模糊匹配）'},
                'limit': {'type': 'integer', 'description': '最多返回条数，默认 30'},
            },
            'required': ['path'],
        },
    },
    {
        'name': 'exp_refs',
        'description': (
            '查某个对象在 EXP 里的引用关系：谁定义了它、被哪些命令引用、'
            '它自己又引用了哪些对象。用来确认改一个对象会影响哪些配置。'
        ),
        'inputSchema': {
            'type': 'object',
            'properties': {
                'path': {'type': 'string'},
                'object_name': {'type': 'string', 'description': '对象名（如 hngd_00_ch_p）'},
            },
            'required': ['path', 'object_name'],
        },
    },
    {
        'name': 'exp_baseline',
        'description': (
            '提取某几个命令族的典型写法（含完整参数）。'
            '用来参考现网的参数组合和写法，不要照抄值，照抄结构。'
        ),
        'inputSchema': {
            'type': 'object',
            'properties': {
                'path': {'type': 'string'},
                'families': {
                    'type': 'array', 'items': {'type': 'string'},
                    'description': '命令族列表，如 ["HOST", "FILTER", "URR"]',
                },
                'per_family': {'type': 'integer', 'description': '每族几条样例，默认 2'},
            },
            'required': ['path', 'families'],
        },
    },
    {
        'name': 'exp_siblings',
        'description': (
            '★ 配置前必查：找出与目标命令族「配套」的其他族。'
            '原理：现网 EXP 里两个族的对象数量接近（比值>=阈值），'
            '说明它们总是成对出现，属于配套关系。'
            '实测：ADD POOL <-> POOLGROUP 0.98、POOL <-> POOLBINDGROUP 0.99。'
            '典型用途：要建地址池时先查 ADD POOL 的配套族，'
            '会发现还要建 POOLGROUP / POOLBINDGROUP / POOLGRPMAP，'
            '避免只配了 SECTION 漏掉整条业务链。'
            '不填 families 则返回全局高共现族对。'
        ),
        'inputSchema': {
            'type': 'object',
            'properties': {
                'path': {'type': 'string', 'description': 'EXP 文件路径'},
                'families': {
                    'type': 'array', 'items': {'type': 'string'},
                    'description': '要查的族，如 ["ADD POOL"]；不填返回全局高共现对',
                },
                'min_ratio': {'type': 'number', 'description': '配套判定阈值，默认 0.7'},
                'min_count': {'type': 'integer', 'description': '过滤样本太少的族，默认 20'},
            },
            'required': ['path'],
        },
    },
    {
        'name': 'exp_pairs',
        'description': (
            '归纳 A 族到 B 族的命名派生规律（写批量模板时用）。'
            '找出本网元现网里真实配对的实例（B 的参数引用了 A 的主键值），'
            '用固定算子反向试探，返回可直接抄进模板的规则和覆盖率。'
            '例：exp_pairs(POOLGROUP, POOL) 返回 PREFIX_REPLACE(grp,pool) coverage=97/97。'
            'coverage 100% 才可放心用；unmatched 里是残留，可能需人工确认。'
        ),
        'inputSchema': {
            'type': 'object',
            'properties': {
                'path': {'type': 'string', 'description': 'EXP 文件路径'},
                'family_a': {'type': 'string', 'description': '源族名，如 POOLGROUP'},
                'family_b': {'type': 'string', 'description': '目标族名，如 POOL'},
                'limit': {'type': 'integer', 'description': '返回样本数，默认 10'},
            },
            'required': ['path', 'family_a', 'family_b'],
        },
    },
]

HANDLERS = {
    'exp_detect': tool_exp_detect,
    'exp_stats': tool_exp_stats,
    'exp_query': tool_exp_query,
    'exp_refs': tool_exp_refs,
    'exp_baseline': tool_exp_baseline,
    'exp_siblings': tool_exp_siblings,
    'exp_pairs': tool_exp_pairs,
}


def handle(msg):
    method = msg.get('method')
    mid = msg.get('id')

    if method == 'initialize':
        return {'jsonrpc': '2.0', 'id': mid, 'result': {
            'protocolVersion': '2024-11-05',
            'capabilities': {'tools': {}},
            'serverInfo': {'name': 'mcp_exp', 'version': '1.0.0'},
        }}

    if method == 'tools/list':
        return {'jsonrpc': '2.0', 'id': mid, 'result': {'tools': TOOLS}}

    if method == 'tools/call':
        params = msg.get('params') or {}
        name = params.get('name')
        args = params.get('arguments') or {}
        fn = HANDLERS.get(name or '')
        if not fn:
            return {'jsonrpc': '2.0', 'id': mid,
                    'error': {'code': -32601, 'message': f'未知工具: {name}'}}
        try:
            result = fn(args)
            return {'jsonrpc': '2.0', 'id': mid, 'result': {
                'content': [{'type': 'text',
                             'text': json.dumps(result, ensure_ascii=False, indent=1)}],
                'isError': 'error' in result,
            }}
        except Exception as e:
            return {'jsonrpc': '2.0', 'id': mid, 'result': {
                'content': [{'type': 'text',
                             'text': json.dumps(
                                 {'error': f'{type(e).__name__}: {e}'},
                                 ensure_ascii=False)}],
                'isError': True,
            }}

    if method in ('notifications/initialized', 'notifications/cancelled'):
        return None

    return {'jsonrpc': '2.0', 'id': mid,
            'error': {'code': -32601, 'message': f'未知方法: {method}'}}


def main():
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            msg = json.loads(line)
        except json.JSONDecodeError:
            continue
        resp = handle(msg)
        if resp is not None:
            sys.stdout.write(json.dumps(resp, ensure_ascii=False) + '\n')
            sys.stdout.flush()


if __name__ == '__main__':
    main()

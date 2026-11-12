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
    """按四层模型统计 EXP：操作 / 对象与身份 / 引用关联 / 行为参数。

    ★ 2026-11-11 重写（用户裁定：按 PPT 的四层命令模型组织）

    旧版缺陷（实测 NC20260806001780，EXP 共 235035 条）：
        for _ln, v, f, params, _raw in iter_commands(text):
            if v != 'ADD':
                continue
        → 只返回有 ADD 的族 247 个，丢掉 1098 个「只靠 SET/MOD/RMV」的族
        → agent 以为现网只有 247 个族（实际 1345 个）
        → APNCHARGECTRL / APNIDLETIME / DBPARAS / LICENSESWITCH 这些
          「挂在别的对象上的属性族」全部不可见
        → 阶段1 漏规划，GT 里 32% 的族永远进不了规划表

    四层模型的对应关系：
        第一层 操作      → 每条命令的 verb
        第二层 对象与身份 → 有 ADD 的是「对象族」（身份 = 主键）；
                          只有 SET/MOD/RMV 的是「属性族」（身份挂在别的族上）
        第三层 引用关联  → 某族某参数的值等于另一族的身份值
        第四层 行为参数  → 既非身份、也非引用的参数

    参数：
        path            必填，EXP 文件路径
        family          可选，只返回指定族
        with_references 可选，默认 True；False 时跳过引用扫描（更快）
        max_refs        可选，引用扫描上限，默认 0=不限（全量扫）
    """
    path = args.get('path') or ''
    want_families = args.get('family')
    with_refs = args.get('with_references', True)
    max_refs = int(args.get('max_refs') or 0)   # 0 = 不限（默认全量扫）

    p = Path(path)
    if not p.exists():
        return {'error': f'文件不存在: {path}'}

    # 结果缓存（同文件同参数）
    try:
        st = p.stat()
        fam_key = want_families if isinstance(want_families, str) else (
            tuple(want_families) if want_families else None)
        res_key = ('stats2', str(p), st.st_size, st.st_mtime,
                   fam_key, bool(with_refs), max_refs)
        if res_key in _RESULT_CACHE:
            return _RESULT_CACHE[res_key]
    except Exception:
        res_key = None

    text, enc, _all_cmds = _get_parsed(p)

    # ── 第一层 + 第二层：一次遍历，把两个层都统计出来 ──
    fam_verbs = defaultdict(set)                       # 族 -> {动词}
    fam_cnt = Counter()                                # 族 -> 总条数
    fam_verb_cnt = defaultdict(Counter)                # 族 -> {动词: 条数}
    fam_names = defaultdict(list)                      # 族 -> [身份值]
    fam_params = defaultdict(lambda: defaultdict(set)) # 族 -> {参数: {值}}
    fam_first_param = {}                               # 族 -> 第一个参数名

    for _ln, v, f, params, _raw in iter_commands(text):
        fam_verbs[f].add(v)
        fam_cnt[f] += 1
        fam_verb_cnt[f][v] += 1
        if params:
            if f not in fam_first_param:
                fam_first_param[f] = next(iter(params))
            first_k = next(iter(params))
            first_v = params[first_k]
            if first_v and not _is_placeholder(first_v) and len(fam_names[f]) < 400:
                fam_names[f].append(first_v)
        for k, val in params.items():
            if val and not _is_placeholder(val):
                s = fam_params[f][k]
                if len(s) < 200:
                    s.add(val)

    # ── 第二层：拆成对象族 / 属性族 ──
    # 对象族   = 有 ADD 命令（能独立创建，身份就是自己的主键）
    # 属性族   = 只有 SET/MOD/RMV（不能独立创建，身份挂在别的族上）
    object_fams = {f for f, vs in fam_verbs.items() if 'ADD' in vs}
    attr_fams = {f for f, vs in fam_verbs.items() if 'ADD' not in vs}

    # 每个对象族的身份参数（ADD 时的第一个参数）
    identity_param = {}
    for f in object_fams:
        for _ln, v, ff, params, _raw in iter_commands(text):
            if ff == f and v == 'ADD' and params:
                identity_param[f] = next(iter(params))
                break

    # 属性族的归属对象：它的参数里哪个指向某个对象族的身份参数
    # 例：APNCHARGECTRL 的参数 APN 对应 APN 族的身份参数 APN
    #
    # ★ 2026-11-11：一个参数名可能对应多个对象族，必须选「最基础」的那个。
    #   实测：IFNAME 同时是 INTERFACE 和 IFIPV6ADDRESS 的身份参数
    #        IFIPV6ENABLE(IFNAME=...) 的归属应该是 INTERFACE（物理接口），
    #        不是 IFIPV6ADDRESS（接口的 IPv6 地址视图）。
    #   判据：
    #     1. 该对象族在自己的命令里不引用其他对象的身份参数（更底层）
    #     2. 该对象族条数多（更基础）
    #     3. 字典序（可复现）
    #   用「自身是否含引用参数」区分基础/派生：INTERFACE 的 ADD 只带 IFNAME，
    #   IFIPV6ADDRESS 的 ADD 带 IFNAME + IPV6ADDRESS（后者是它自己产生的）。
    attr_owner = {}
    for f in attr_fams:
        pname = fam_first_param.get(f)
        if not pname:
            continue
        cands = [of for of in object_fams if identity_param.get(of) == pname]
        owner = None
        if cands:
            # ★ 2026-11-11：归属判定不能只看「参数名相同」。
            #   实测三个反例：
            #     APNQOSATTR(APN=..)     参数名 APN 同时是 APN/ACLBINDAPN/TCPMSS 的身份参数
            #     IFIPV6ENABLE(IFNAME=..) 同时是 INTERFACE/IFIPV4ADDRESS/IFIPV6ADDRESS 的
            #     UPGPATTIMER(NAME=..)    同时是 LOGICINF/USERSELATTR 的
            #
            #   改用「值集合覆盖率」：父族的身份值应该覆盖子族该参数的值。
            #   例：IFNAME 的值 LoopBack6 / Eth-Trunk6401.2003
            #        → INTERFACE 里有这些接口名（覆盖率 100%）
            #        → IFIPV4ADDRESS 里只有配了 IPv4 地址的那部分（覆盖率 < 100%）
            #   覆盖率高 + 值域宽 = 更基础的父族
            child_vals = fam_params[f].get(pname) or set()
            scored = []
            for of in cands:
                of_vals = fam_params[of].get(pname) or set()
                if not of_vals or not child_vals:
                    cov = 0.0
                else:
                    cov = len(child_vals & of_vals) / len(child_vals)
                # 覆盖率优先；同覆盖率时值域大的更基础；再看条数
                scored.append((cov, len(of_vals), fam_cnt[of], of))
            scored.sort(key=lambda x: (-x[0], -x[1], -x[2], x[3]))
            best = scored[0]
            # 覆盖率低于 0.5 视为无法判定（避免乱指）
            owner = best[3] if best[0] >= 0.5 else None
        attr_owner[f] = {'owner_family': owner, 'identity_param': pname,
                         'owner_candidates': cands[:3] if len(cands) > 1 else None}

    # ── 第三层：引用关联 ──
    # 某族某参数的值 == 另一族的身份值 → 判为引用
    references = {}
    if with_refs:
        # 建身份值索引（只对对象族，且值集合 >= 2 的才有区分度）
        id_values = {}
        for f in object_fams:
            ip = identity_param.get(f)
            if not ip:
                continue
            vals = fam_params[f].get(ip) or set()
            if len(vals) >= 2:
                id_values[f] = vals

        # ★ 2026-11-11 修复：原版只扫前 max_refs(50000) 条命令，
        #   实测 NC20260806001780 的 EXP 有 119703 条命令，
        #   FLTBINDFLOWF 首次出现在第 58283 条 → 完全没被扫到 → 引用关联全丢。
        #
        #   改为全量扫描 + 反向索引（值 → [(族, 参数)]），
        #   一次哈希查找替代内层 for 遍历，比原来更快：
        #     旧版：O(命令数 × 族数 × 参数数)  119703 × 91 × 5 ≈ 5.4e7
        #     新版：O(命令数 × 参数数)         119703 × 5 ≈ 6e5
        #
        #   仍然保留 max_refs 作为安全阀，但默认改为 0 = 不限制。
        val_index = defaultdict(list)      # 身份值 -> [(族, 身份参数)]
        for tf, vals in id_values.items():
            ip = identity_param.get(tf)
            for vv in vals:
                val_index[vv].append((tf, ip))

        scanned = 0
        for _ln, v, f, params, _raw in iter_commands(text):
            if max_refs and scanned >= max_refs:
                break
            scanned += 1
            for pname, pval in params.items():
                if not pval or _is_placeholder(pval):
                    continue
                for tf, tip in val_index.get(pval, ()):
                    if tf == f:
                        continue          # 不算自引用
                    # ★ 2026-11-11：引用判定的两条规则
                    #
                    # 规则 1（参数名相同）→ 直接认，这是最可靠的形态：
                    #     SECTION.POOLNAME=pool_x → POOL.POOLNAME=pool_x
                    #     FLTBINDFLOWF.FLOWFILTERNAME=x → FLOWFILTER.FLOWFILTERNAME=x
                    #
                    # 规则 2（参数名不同但值是强身份值）→ 也认，但要过滤弱值：
                    #     RULE.POLICYNAME="12530_01_pcc_p_g"
                    #       → PCCPOLICYGRP.PCCPOLICYGRPNM="12530_01_pcc_p_g"  ✓ 真引用
                    #     反例（必须排除）：
                    #     SECTION.SECTIONNUM=2 → CPPOINT.SECTIONNUM=2
                    #       纯数字短值是序号，不是身份
                    #
                    # 「强身份值」判据：非纯数字，且长度 >= 4
                    #   （pool_x / 12530_01_pcc_p_g / ims / sos 这类才算）
                    if pname != tip:
                        sv = str(pval)
                        if sv.isdigit() or len(sv) < 4:
                            continue      # 弱值（序号/开关/枚举），不算引用
                    key = f
                    entry = references.setdefault(key, {})
                    k2 = (pname, tf)
                    entry[k2] = entry.get(k2, 0) + 1

        # 整理成列表
        references = {
            f: [{'param': pn, 'target_family': tf, 'n': n}
                for (pn, tf), n in sorted(d.items(), key=lambda x: -x[1])]
            for f, d in references.items()
        }

    # ── 按需过滤 ──
    if want_families:
        if isinstance(want_families, str):
            want_families = [want_families]
        wf = {x.upper() for x in want_families}
        object_fams = {f for f in object_fams if f in wf}
        attr_fams = {f for f in attr_fams if f in wf}
        references = {f: v for f, v in references.items() if f in wf}

    # ── 组织返回：对象族 ──
    def _fam_entry(fam, is_object):
        n = fam_cnt[fam]
        names = fam_names.get(fam) or []
        entry = {
            'count': n,
            'verbs': sorted(fam_verbs[fam]),
            'verb_counts': dict(fam_verb_cnt[fam]),
        }
        if is_object:
            entry['identity_param'] = identity_param.get(fam)
            entry['sample_names'] = names[:5]
            if names:
                shapes = Counter()
                for nm in names:
                    shapes[re.sub(r'\d+', 'N', nm)] += 1
                entry['name_patterns'] = [
                    {'pattern': k, 'count': v} for k, v in shapes.most_common(3)]
                nums = []
                for nm in names:
                    mm = re.findall(r'\d+', nm)
                    if mm:
                        try:
                            nums.append(int(mm[-1]))
                        except Exception:
                            pass
                if nums:
                    entry['number_range'] = [min(nums), max(nums)]
        else:
            # 属性族：告诉 agent 这个属性挂在谁身上
            entry.update(attr_owner.get(fam) or {})
            # 属性族也给出身份值样例（就是它挂在哪些对象上）
            if names:
                entry['sample_names'] = names[:5]

        # 第四层：行为参数
        ip = identity_param.get(fam)
        ref_params = {r['param'] for r in (references.get(fam) or [])}
        behavior = {}
        for k, vs in fam_params[fam].items():
            if k in (ip,) or k in ref_params:
                continue
            if k == 'PRIORITY':
                try:
                    pv = sorted(int(x) for x in vs if str(x).isdigit())
                    if pv:
                        entry['priority_range'] = [pv[0], pv[-1]]
                except Exception:
                    pass
                continue
            if 1 < len(vs) <= 20 and len(behavior) < 3:
                behavior[k] = sorted(vs)[:8]
        if behavior:
            entry['enums'] = behavior

        # 第三层：该族的引用关联
        if references.get(fam):
            entry['references'] = references[fam][:8]

        return entry

    object_families = {f: _fam_entry(f, True)
                       for f in sorted(object_fams, key=lambda x: -fam_cnt[x])}
    attribute_families = {f: _fam_entry(f, False)
                          for f in sorted(attr_fams, key=lambda x: -fam_cnt[x])}

    # ── 四层规模摘要 ──
    layers = {
        'L1_operations': {
            'ADD': sum(c['ADD'] for c in fam_verb_cnt.values()),
            'SET': sum(c['SET'] for c in fam_verb_cnt.values()),
            'MOD': sum(c['MOD'] for c in fam_verb_cnt.values()),
            'RMV': sum(c['RMV'] for c in fam_verb_cnt.values()),
        },
        'L2_objects': {
            'object_family_count': len(object_fams),
            'attribute_family_count': len(attr_fams),
            'total_family_count': len(fam_verbs),
        },
        'L3_references': {
            'n_families_with_refs': len(references),
            'n_ref_edges': sum(len(v) for v in references.values()),
        },
        'L4_behavior': {
            'families_with_behavior_params':
                sum(1 for f in object_fams
                    if f in object_families and
                    ('enums' in object_families[f] or
                     'priority_range' in object_families[f])),
        },
    }

    result = {
        'path': str(p),
        'encoding': enc,
        'total_cmds': sum(fam_cnt.values()),
        # ★ 兼容旧 key（mcp_knowledge 依赖）：families 只含对象族
        'family_count': len(object_families),
        'families': object_families,
        # ★ 新增：四层模型完整视图
        'family_count_all': len(fam_verbs),
        'object_families': object_families,
        'attribute_families': attribute_families,
        'references': references,
        'layers': layers,
        'note': ('families 与 object_families 相同（有 ADD 的对象族，'
                 '兼容旧调用）；attribute_families 是只有 SET/MOD/RMV 的'
                 '属性族，它们挂在 owner_family 上，配该对象时必须一并考虑。'),
    }

    if res_key:
        if len(_RESULT_CACHE) >= _CACHE_MAX * 4:
            _RESULT_CACHE.pop(next(iter(_RESULT_CACHE)))
        _RESULT_CACHE[res_key] = result
    return result


# ═══════════════════════════════════════════════════════════
# 工具 3：exp_query
# ═══════════════════════════════════════════════════════════
def tool_exp_query(args):
    """按条件查命令（支持三种模式）。

    ★ 2026-11-11 扩展（用户批准的对照实验）
    背景：实测 agent 只用 exp_query（9-88 次/单），
          exp_stats / exp_attr_chain / exp_cross_stats 调用全部 0 次。
          原因：exp_query 返回「命令原文」，可直接用；
               其他工具返回统计结构，还要二次加工。
          结论：能力应该塞进 agent 已经在用的 exp_query，而不是新造工具。

    三种模式：
      模式 1（原有）按族/参数/值精确查
        exp_query(path, family='APNQOSATTR', param='APN', value='ims.wh')

      模式 2（新增）owner + value：一次拿「某对象在所有属性族里的完整配置」
        exp_query(path, owner='APN', value='ims.wh')
        → 返回所有 owner_family=APN 的属性族 + APN 本身，针对 ims.wh 的命令原文
        → 对应原来要调 30+ 次 exp_query 的场景

      模式 3（新增）family 前缀批量
        exp_query(path, family_prefix='APN', param='APN', value='ims.wh')
        → 返回所有 APN 开头的族（APNADDRESSATTR/APNCHARGECTRL/...）的命令

    其他改进：
      · limit 从 30 提到 200（agent 原来因为 limit=30 被截断，要反复翻页）
      · 新增 with_family_summary：同时返回各族的条数汇总
    """
    path = args.get('path') or ''
    fam = (args.get('family') or '').upper()
    fam_prefix = (args.get('family_prefix') or '').upper()
    owner = (args.get('owner') or '').upper()
    param = (args.get('param') or '').upper()
    value = args.get('value') or ''
    limit = int(args.get('limit') or 200)
    want_summary = args.get('with_family_summary', False)

    p = Path(path)
    if not p.exists():
        return {'error': f'文件不存在: {path}'}

    text, _, _all_cmds = _get_parsed(p)

    # ── 模式 2：owner + value → 先算出该 owner 的所有属性族 ──
    owner_fams = None
    if owner:
        owner_fams = _families_of_owner(p, owner)
        if not owner_fams:
            return {
                'path': str(p),
                'mode': 'owner',
                'owner': owner,
                'count': 0,
                'results': [],
                'note': f'EXP 里没有挂在 {owner} 上的属性族（owner_family 判定为空）',
            }

    hits = []
    fam_cnt = {}
    seen_fams = set()
    for ln, v, f, params, raw in _all_cmds:
        # ── 族过滤 ──
        if owner_fams is not None:
            if f not in owner_fams:
                continue
        elif fam_prefix:
            if not f.startswith(fam_prefix):
                continue
        elif fam:
            if f != fam:
                continue

        # ── 参数/值过滤 ──
        if param:
            pv = params.get(param)
            if pv is None:
                continue
            if value and value.lower() not in str(pv).lower():
                continue
        elif value:
            if not any(value.lower() in str(x).lower() for x in params.values()):
                continue

        fam_cnt[f] = fam_cnt.get(f, 0) + 1
        seen_fams.add(f)
        if len(hits) < limit:
            hits.append({'line': ln, 'verb': v, 'family': f, 'cmd': raw[:300]})

    result = {
        'path': str(p),
        'mode': ('owner' if owner_fams is not None
                 else ('prefix' if fam_prefix else 'exact')),
        'count': len(hits),
        'n_families_hit': len(seen_fams),
        'results': hits,
    }
    if owner:
        result['owner'] = owner
        result['owner_families'] = sorted(owner_fams)
        result['n_owner_families'] = len(owner_fams)
    if want_summary:
        result['family_summary'] = dict(
            sorted(fam_cnt.items(), key=lambda x: -x[1]))
    if len(hits) >= limit:
        result['truncated'] = True
        result['note'] = f'已达 limit={limit}，如需更多请调大 limit 或加 family 过滤'

    return result


def _families_of_owner(path, owner_family):
    """某父族的全部属性族（含父族自己），用于 exp_query 的 owner 模式。

    复用 exp_stats 的 attribute_families（owner_family 判定已用值集合覆盖率验证过）。
    """
    st = tool_exp_stats({'path': str(path), 'with_references': False})
    if st.get('error'):
        return set()
    attrs = st.get('attribute_families') or {}
    out = {f for f, d in attrs.items()
           if (d.get('owner_family') or '') == owner_family}
    # 父族自己也带上（配 APN 时 APN 本身也要配）
    if owner_family in (st.get('object_families') or {}):
        out.add(owner_family)
    return out


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
# 工具 8：exp_attr_chain（属性族链）
# ═══════════════════════════════════════════════════════════
def tool_exp_attr_chain(args):
    """查某对象的完整属性族链：配这个对象时，还要配哪些属性族。

    ★ 2026-11-11 新增（用户要求：把 agent 反复现写的解析代码固化）

    解决的问题：
      实测 NC20260810002261，UNC 侧每个 APN 带 30+ 个 SET APNxxx 属性族
      （APNIMSATTR / APNIDLETIME / APNPCCFUNC / APNQOSATTR ...）。
      GT 里 32% 的族属于这类「属性族」，但它们不是独立对象、没有 ADD，
      旧 exp_stats（只统计 ADD）完全看不到 → agent 不知道要配 → 漏配。
      agent 当时自己用 execute_code 写了 21 次才发现，耗时 67s。

    参数：
      path          必填，EXP 文件路径
      owner_family  必填，父族名，如 APN / INTERFACE / USERPROFILE
      owner_value   可选，只看该对象实例的属性（如 APN="ims.wh"）；
                    不传则列出该父族所有实例的属性族链
      path_candidates 可选，额外 EXP 路径列表（多网元时一起查）

    返回：
      {
        'owner_family': 'APN',
        'owner_value': 'ims.wh',
        'n_owner_instances': 333,
        'attribute_families': [
            {'family': 'APNIMSATTR', 'count': 333, 'has_owner_value': True,
             'verbs': ['SET'], 'sample_cmd': 'SET APNIMSATTR:APN="ims.wh", ...'},
            ...
        ],
        'total_attribute_families': 32,
        'per_exp': {...}     # 多 EXP 时给出各文件的分布
      }
    """
    paths = []
    p0 = args.get('path') or ''
    if p0:
        paths.append(p0)
    for x in (args.get('path_candidates') or []):
        if x and x not in paths:
            paths.append(x)

    owner_family = (args.get('owner_family') or '').upper()
    owner_value = (args.get('owner_value') or '').strip()

    if not paths:
        return {'error': 'path 必填'}
    if not owner_family:
        return {'error': 'owner_family 必填（如 APN / INTERFACE / USERPROFILE）'}

    # ★ 2026-11-11：结果缓存（同参数二次调用 0 开销）
    #   实测热调用仍需 14s，因为每次都要全量遍历 iter_commands
    try:
        mtimes = tuple((str(Path(x)), Path(x).stat().st_mtime)
                       for x in paths if Path(x).exists())
        _ck = ('attr_chain', mtimes, owner_family, owner_value)
        if _ck in _RESULT_CACHE:
            return _RESULT_CACHE[_ck]
    except Exception:
        _ck = None

    per_exp = {}
    merged = {}          # family -> {'count': n, 'has_owner_value': bool, 'sample_cmd': str}

    for path in paths:
        pp = Path(path)
        if not pp.exists():
            per_exp[path] = {'error': f'文件不存在: {path}'}
            continue

        # 复用 exp_stats 的四层统计（已带缓存）
        st = tool_exp_stats({'path': path, 'with_references': False})
        if st.get('error'):
            per_exp[path] = st
            continue

        attrs = st.get('attribute_families') or {}
        objs = st.get('object_families') or {}

        # 该父族在这个 EXP 里的实例数
        n_owner = (objs.get(owner_family) or {}).get('count', 0)

        # 挂在父族上的属性族
        hit_fams = [f for f, d in attrs.items()
                    if (d.get('owner_family') or '') == owner_family]

        # ★ 2026-11-11 性能优化：
        #   原来对每个属性族都调一次 _count_owner_instances（全量扫 EXP），
        #   23 个族 = 扫 23 遍 11 万条命令。改成一次扫描把所有需要的信息拿到。
        local = {f: {
            'count': attrs[f].get('count', 0),
            'verbs': attrs[f].get('verbs') or [],
            'identity_param': attrs[f].get('identity_param'),
            'has_owner_value': None,
            'n_owner_value': 0,
        } for f in hit_fams}

        if owner_value:
            ip_owner = (objs.get(owner_family) or {}).get('identity_param')
            try:
                text, _enc, _cmds = _get_parsed(pp)
            except Exception:
                text = ''
            sample_taken = set()
            n_owner_val = 0
            for _ln, v, f, params, raw in iter_commands(text):
                # 父族实例计数
                if f == owner_family and ip_owner:
                    if str(params.get(ip_owner) or '') == owner_value:
                        n_owner_val += 1
                    continue
                d = local.get(f)
                if not d:
                    continue
                tip = d.get('identity_param')
                if not tip:
                    continue
                if str(params.get(tip) or '') != owner_value:
                    continue
                d['n_owner_value'] = d.get('n_owner_value', 0) + 1
                d['has_owner_value'] = True
                # 每个族只取一条样例
                if f not in sample_taken:
                    d['sample_cmd'] = raw[:300]
                    sample_taken.add(f)
            if ip_owner and n_owner_val:
                n_owner = n_owner_val
            # 没有 owner_value 实例的族显式标 False
            for d in local.values():
                if d['has_owner_value'] is None:
                    d['has_owner_value'] = False

        per_exp[path] = {
            'n_owner_instances': n_owner,
            'n_attribute_families': len(local),
            'attribute_families': local,
        }

        # 合并
        for f, d in local.items():
            m = merged.setdefault(f, {'count': 0, 'verbs': set(),
                                      'has_owner_value': False, 'exps': []})
            m['count'] += d['count']
            m['verbs'] |= set(d['verbs'] or [])
            if d.get('has_owner_value'):
                m['has_owner_value'] = True
            m['exps'].append(str(pp.name))
            if d.get('sample_cmd') and 'sample_cmd' not in m:
                m['sample_cmd'] = d['sample_cmd']

    # 整理输出：按条数降序
    out_attrs = []
    for f, d in sorted(merged.items(), key=lambda x: -x[1]['count']):
        item = {
            'family': f,
            'count': d['count'],
            'verbs': sorted(d['verbs']),
            'has_owner_value': d['has_owner_value'],
            'found_in': d['exps'],
        }
        if 'sample_cmd' in d:
            item['sample_cmd'] = d['sample_cmd']
        out_attrs.append(item)

    result = {
        'owner_family': owner_family,
        'owner_value': owner_value or None,
        'total_attribute_families': len(out_attrs),
        'attribute_families': out_attrs,
        'per_exp': per_exp,
        'note': ('attribute_families 是「挂在 owner_family 上的属性族」，'
                 '配该对象时必须一并规划；has_owner_value=True 表示现网'
                 '该对象实例已经有这条属性配置，可直接照抄写法。'),
    }
    if _ck:
        if len(_RESULT_CACHE) >= _CACHE_MAX * 4:
            _RESULT_CACHE.pop(next(iter(_RESULT_CACHE)))
        _RESULT_CACHE[_ck] = result
    return result


def _count_owner_instances(path, family, identity_param, owner_value):
    """数某族里身份参数 == owner_value 的命令条数。"""
    try:
        text, _enc, _cmds = _get_parsed(Path(path))
    except Exception:
        return 0
    n = 0
    for _ln, v, f, params, _raw in iter_commands(text):
        if f != family:
            continue
        pv = params.get(identity_param)
        if pv and str(pv) == str(owner_value):
            n += 1
    return n


def _sample_cmd(path, family, owner_value):
    """取一条该族针对 owner_value 的真实命令。"""
    try:
        text, _enc, _cmds = _get_parsed(Path(path))
    except Exception:
        return None
    for _ln, v, f, params, raw in iter_commands(text):
        if f != family:
            continue
        if owner_value and owner_value not in str(params.values()):
            continue
        return raw[:300]
    return None


# ═══════════════════════════════════════════════════════════
# 工具 9：exp_cross_stats（多网元分布对比）
# ═══════════════════════════════════════════════════════════
def tool_exp_cross_stats(args):
    """对比同一个族在多个 EXP（多网元）里的分布，给出归属建议。

    ★ 2026-11-11 新增

    解决的问题：
      实测 NC20260810002261 的规划表里，agent 自己写代码算出——
        POOLGROUP/POOL/POOLBINDGROUP  UDG 683/659/683 条，UNC 0 条 → 只在 UDG 配
        PCSCFIP/PCSCFGROUP/PCSCFGRPBNDAPN  UDG 0 条，UNC 27/5/20 条 → 只在 UNC 配
        USERPROFILE 双侧都有（UDG 19 / UNC 82）→ 两侧各配各的
      这类判断是定式的，代码应该固化。

    参数：
      paths     必填，EXP 路径列表
      families  可选，只查这些族；不传则对比全部族的差异

    返回：
      {
        'per_exp': {'<path>': {'me_type': 'UDG', 'total_cmds': N, 'n_families': M}},
        'comparison': [
            {'family': 'POOL', 'counts': {'UDG': 683, 'UNC': 0},
             'verdict': 'UDG_only', 'advice': '只在 UDG 配'},
            {'family': 'USERPROFILE', 'counts': {'UDG': 19, 'UNC': 82},
             'verdict': 'both', 'advice': '两侧都有，需分别判断'},
        ],
        'summary': {'udg_only': 120, 'unc_only': 88, 'both': 45, 'neither': 0}
      }
    """
    paths = [x for x in (args.get('paths') or []) if x]
    if not paths:
        return {'error': 'paths 必填（EXP 路径列表）'}

    # 结果缓存
    try:
        mtimes = tuple((str(Path(x)), Path(x).stat().st_mtime)
                       for x in paths if Path(x).exists())
        _ck2 = ('cross_stats', mtimes, str(args.get('families')))
        if _ck2 in _RESULT_CACHE:
            return _RESULT_CACHE[_ck2]
    except Exception:
        _ck2 = None
    want = args.get('families')
    if isinstance(want, str):
        want = [want]
    want = {x.upper() for x in want} if want else None

    per_exp = {}
    fam_by_exp = {}       # exp_label -> {family: count}
    verbs_by_exp = {}     # exp_label -> {family: [verbs]}

    for path in paths:
        pp = Path(path)
        if not pp.exists():
            per_exp[path] = {'error': f'文件不存在: {path}'}
            continue
        # ★ 2026-11-11 性能优化：
        #   原来调 tool_exp_stats（它算命名规律/枚举/引用，本工具用不上），
        #   两个 17MB EXP 冷跑 56s。改成只遍历一次拿 count + verbs：
        #   复用 _get_parsed 的解析缓存，不重复解析。
        try:
            text, _enc, _cmds = _get_parsed(pp)
        except Exception as e:
            per_exp[path] = {'error': f'{type(e).__name__}: {e}'}
            continue

        label = _exp_label(pp.name, per_exp)
        cnt, vbs = {}, {}
        total = 0
        for _ln, v, f, params, _raw in iter_commands(text):
            total += 1
            cnt[f] = cnt.get(f, 0) + 1
            vbs.setdefault(f, set()).add(v)

        vbs = {f: sorted(vs) for f, vs in vbs.items()}
        fam_by_exp[label] = cnt
        verbs_by_exp[label] = vbs
        per_exp[path] = {
            'label': label,
            'total_cmds': total,
            'n_families': len(cnt),
        }

    labels = list(fam_by_exp.keys())
    if len(labels) < 2:
        return {'error': '至少需要 2 个有效 EXP 才能对比', 'per_exp': per_exp}

    # 所有族取并集
    all_fams = set()
    for cnt in fam_by_exp.values():
        all_fams |= set(cnt)
    if want:
        all_fams &= want

    comparison = []
    summary = {'one_exp_only': 0, 'both': 0, 'all': 0}
    for f in sorted(all_fams):
        counts = {lb: fam_by_exp[lb].get(f, 0) for lb in labels}
        present = [lb for lb in labels if counts[lb] > 0]
        if len(present) == 1:
            verdict = f'{present[0]}_only'
            advice = f'只在 {present[0]} 配'
            summary['one_exp_only'] += 1
        elif len(present) == len(labels):
            verdict = 'all'
            advice = '所有网元都有，按业务归属判断'
            summary['all'] += 1
        else:
            verdict = 'partial'
            advice = f'存在于 {"/".join(present)}，缺 {"/".join(lb for lb in labels if lb not in present)}'
            summary['both'] += 1
        comparison.append({
            'family': f,
            'counts': counts,
            'verbs': {lb: verbs_by_exp[lb].get(f) or [] for lb in present},
            'verdict': verdict,
            'advice': advice,
        })

    result = {
        'labels': labels,
        'per_exp': per_exp,
        'comparison': comparison,
        'summary': summary,
        'note': ('verdict 为 <label>_only 表示该族只在一个网元存在，'
                 '应按 advice 决定在哪配；all 表示两侧都有，需结合业务判断'
                 '（同名族在两侧可能是不同用途，例如 UDG 的 USERPROFILE 走 PCC 链、'
                 'UNC 的走用户模板组）。'),
    }
    if _ck2:
        if len(_RESULT_CACHE) >= _CACHE_MAX * 4:
            _RESULT_CACHE.pop(next(iter(_RESULT_CACHE)))
        _RESULT_CACHE[_ck2] = result
    return result

def _exp_label(fname, per_exp_so_far):
    """从文件名推断网元标签：EXPMML_ME0_UDG_... → UDG。"""
    m = re.search(r'_(UDG|UNC|UEG|UDM|UPF)_', fname, re.I)
    label = m.group(1).upper() if m else 'EXP'
    # 重名时加序号
    used = {(v or {}).get('label') for v in per_exp_so_far.values()
            if isinstance(v, dict)}
    if label in used:
        i = 2
        while f'{label}{i}' in used:
            i += 1
        label = f'{label}{i}'
    return label


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
    # ★ 2026-11-09：SET/MOD 族单独统计
    #   问题：ADD APN 615 条，配套的 SET APNxxx 31 个族各 615 条，
    #        但 SET 族完全不在 ADD 的 cnt 里，
    #        siblings_of 遍历 cand 时看不见它们，
    #        导致 agent 只配 ADD APN 主体、漏掉 31 个属性命令。
    #   修法：SET/MOD 族也纳入候选池（分开统计，配对时按族名匹配）。
    cnt_set = Counter()
    for ln, v, f, params, raw in all_cmds:
        if v == 'ADD':
            cnt[f] += 1
        elif v in ('SET', 'MOD'):
            cnt_set[f] += 1

    # 过滤样本太少的族（噪音）
    cand = {f: n for f, n in cnt.items() if n >= min_count}
    # SET/MOD 族并入候选池（用 add 计数为 0 的键占位，后续按名词前缀配对）
    for f, n in cnt_set.items():
        if n >= min_count and f not in cand:
            cand[f] = n

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

            # ★ 2026-11-09：同名前缀属性族判据（用户裁定 ratio >= 0.9）
            #   场景：ADD APN 615 条，SET APNxxx 31 个族各 615 条，ratio=1.00。
            #   这些 SET 族没有指向 APN 的参数名（它们自己就是 APN 的属性命令），
            #   「参数名指向」判据完全看不见，导致 agent 只配 ADD APN 主体，
            #   漏掉 31 个属性命令（实测三个大工单缺 35-51 族全是这类）。
            #   判据：属性族名前缀 == 目标族名 且 数量比值 >= 0.9。
            _prop_of = None
            # 情况 A：other 是 target 的前缀扩展（ADD APN → SET APNxxx）
            if (other != target and other.startswith(target)
                    and len(other) > len(target) and ratio >= 0.9):
                _prop_of = target
            # 情况 B：target 是 other 的前缀扩展（查 SET APNxxx 时反查 ADD APN）
            elif (target != other and target.startswith(other)
                    and len(target) > len(other) and ratio >= 0.9):
                _prop_of = other

            if p_out or p_in:
                conf = 'high'
                who = other if p_out else target
                who_target = target if p_out else other
                why = f'{who} 有指向 {who_target} 的参数名（MML 引用关系）'
            elif _prop_of:
                conf = 'high'
                why = (f'{other} 是 {_prop_of} 的同名前缀属性族'
                       f'（数量比值 {ratio:.2f} ≥ 0.9，通常是同一对象的属性命令）')
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

        # ★ 2026-11-09 修复跨积 bug：中间族的**一条实例**只产生**一个**配对。
        #   原实现对同一条 POOLBINDGROUP 里的所有 A 值和所有 B 值做笛卡尔积，
        #   实测产生大量错误配对：
        #     POOLBINDGROUP:POOLGROUPNAME="5gcuiot_group", POOLNAME="scuiot_pool_ipv4"
        #     → 5gcuiot_group → scuiot_pool_ipv4   （名字毫无关系）
        #     → 5gscuiot_group → scuiot_pool_ipv4
        #     → cuiot_group → scuiot_pool_ipv4     （多对一，全是错的）
        #   正确做法：一条实例只取「第一个 A 值」和「第一个 B 值」配对。
        seen = set()
        for f, ln, hit_a, vals in bridge_hits:
            hit_b = [x for x in vals if x in pks_b]
            if hit_a and hit_b:
                ax, bx = hit_a[0], hit_b[0]
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
            '★ 摸清现网「配了什么、怎么连、怎么取名」的首选工具。'
            '返回按四层模型组织的完整视图：\n'
            '  1 操作：object_families / attribute_families 各自带 verbs 和 verb_counts\n'
            '  2 对象与身份：\n'
            '     object_families  = 有 ADD 的族（能独立创建，identity_param 是主键）\n'
            '     attribute_families = 只有 SET/MOD/RMV 的族（不能独立创建，\n'
            '       挂在 owner_family 上，例如 APNCHARGECTRL 挂在 APN 上）\n'
            '  3 引用关联：references = {族: [{param, target_family, n}]}\n'
            '     例 FLTBINDFLOWF.FLOWFILTERNAME → FLOWFILTER\n'
            '  4 行为参数：enums / priority_range（不含身份和引用参数）\n'
            '  另有 layers 给出四层规模汇总。\n'
            '\n'
            '⚠ 规划前必读：attribute_families 里的族同样是「必须配的」，'
            '它们不独立存在但 GT 里会要求 SET，漏掉就会漏配。'
            '配某个对象时，先看有哪些 attribute_families 的 owner_family 指向它。'
        ),
        'inputSchema': {
            'type': 'object',
            'properties': {
                'path': {'type': 'string', 'description': 'EXP 文件路径'},
                'family': {
                    'description': '只看某几个族（字符串或数组），不传则返回全部',
                    'oneOf': [
                        {'type': 'string'},
                        {'type': 'array', 'items': {'type': 'string'}},
                    ],
                },
                'with_references': {
                    'type': 'boolean',
                    'description': '是否扫描引用关联（默认 true）。大文件可设 false 提速。',
                },
            },
            'required': ['path'],
        },
    },
    {
        'name': 'exp_query',
        'description': (
            '在 EXP 里查命令。返回的是命令原文，可直接照抄写法。三种模式：\n'
            '\n'
            '★ 模式 1 owner + value（最常用，一次拿全）\n'
            '   exp_query(path, owner="APN", value="ims.wh")\n'
            '   → 返回挂在 APN 下的全部属性族（APNADDRESSATTR / APNCHARGECTRL / '
            'APNQOSATTR ... 实测 20-40 个）+ APN 本身，针对 ims.wh 的命令原文。\n'
            '   用途：意图说「APN sos 按现网 ims.wh 存量配齐」→ 调这一次就拿到 '
            '30+ 条可直接照抄的 SET 命令，不用逐族查。\n'
            '\n'
            '★ 模式 2 family_prefix（同类族批量）\n'
            '   exp_query(path, family_prefix="APN", param="APN", value="ims.wh")\n'
            '   → 返回所有 APN 开头的族。适合不确定具体族名时用。\n'
            '\n'
            '★ 模式 3 精确查（原有）\n'
            '   exp_query(path, family="URR", param="URRID", value="1040")\n'
            '\n'
            '其他：limit 默认 200（原来 30 会截断导致反复翻页）；'
            'with_family_summary=true 时额外返回各族条数汇总。'
        ),
        'inputSchema': {
            'type': 'object',
            'properties': {
                'path': {'type': 'string'},
                'owner': {
                    'type': 'string',
                    'description': ('父族名，如 APN / INTERFACE / USERPROFILE。'
                                    '给了它就会返回该对象下所有属性族的命令（模式 1）'),
                },
                'family': {'type': 'string', 'description': '精确的族名，如 URR / HOST'},
                'family_prefix': {
                    'type': 'string',
                    'description': '族名前缀，如 APN（返回所有 APN 开头的族）',
                },
                'param': {'type': 'string', 'description': '参数名，如 FILTERNAME / APN'},
                'value': {'type': 'string', 'description': '参数值（模糊匹配）'},
                'limit': {'type': 'integer', 'description': '最多返回条数，默认 200'},
                'with_family_summary': {
                    'type': 'boolean',
                    'description': '额外返回各族的命中条数汇总',
                },
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
            '三种判据：'
            '(1) 参数名指向：B 族有指向 A 族的参数名（如 POOLBINDGROUP 的 POOLNAME）；'
            '(2) 同名前缀属性族：SET <A>xxx 与 ADD <A> 前缀相同且数量 1:1，'
            '    这类是同一对象的属性命令，必须一起配'
            '    （实测 ADD APN 615 条对应 31 个 SET APNxxx 各 615 条，'
            '     此前「参数名指向」判据完全看不见，导致大面积漏配）；'
            '(3) 数量接近 + 参数值交集（辅助）。'
            '典型用途：要配 APN 时查 ADD APN，会返回 31 个属性族；'
            '要建地址池时查 ADD POOL，会返回 POOLGROUP/POOLBINDGROUP/POOLGRPMAP。'
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
        'name': 'exp_attr_chain',
        'description': (
            '★ 查「配某个对象时，还要配哪些属性族」。'
            '属性族是没有 ADD、只有 SET/MOD 的族（如 APNIMSATTR / APNIDLETIME / '
            'IFIPV6ENABLE），它们不能独立创建、挂在某个父对象上，但 GT 里同样要求配。\n'
            '场景：意图说「APN sos 按现网 ims 存量配齐」→ 调本工具拿到 '
            'APN 的完整属性族链（实测 UNC 侧单 APN 有 30+ 个属性族），'
            '再逐个决定配不配。\n'
            '不给 owner_value 时列出该父族所有实例的属性族；'
            '给 owner_value 则标出哪些族现网已有该实例、可直接照抄写法。\n'
            '⚠ 不要自己写代码扫 EXP —— 这个工具已经把属性族链算好了。'
        ),
        'inputSchema': {
            'type': 'object',
            'properties': {
                'path': {'type': 'string', 'description': 'EXP 文件路径'},
                'owner_family': {'type': 'string',
                                 'description': '父族名，如 APN / INTERFACE / USERPROFILE'},
                'owner_value': {'type': 'string',
                                'description': '可选，对象实例名，如 ims.wh'},
                'path_candidates': {
                    'type': 'array', 'items': {'type': 'string'},
                    'description': '可选，其他 EXP 路径（多网元时一起查）',
                },
            },
            'required': ['path', 'owner_family'],
        },
    },
    {
        'name': 'exp_cross_stats',
        'description': (
            '★ 对比同一个族在多个 EXP（多网元）里的分布，判断「该在哪个网元配」。\n'
            '场景：一个工单给了 UDG + UNC 两份 EXP，意图说「新增地址池组」→ '
            '调本工具确认 POOLGROUP 只在 UDG 有（UNC 为 0 条）→ 在 UDG 配。\n'
            '返回每个族的 counts（各网元条数）+ verdict（<label>_only / all / partial）'
            '+ advice。\n'
            '⚠ 同名族在两侧可能是不同用途（如 UDG 的 USERPROFILE 走 PCC 计费链、'
            'UNC 的走用户模板组），verdict=all 时仍需结合业务判断。\n'
            '⚠ 不要自己写代码扫 EXP —— 这个工具已经把跨网元分布算好了。'
        ),
        'inputSchema': {
            'type': 'object',
            'properties': {
                'paths': {
                    'type': 'array', 'items': {'type': 'string'},
                    'description': 'EXP 路径列表（至少 2 个）',
                },
                'families': {
                    'description': '可选，只对比这些族（字符串或数组）',
                    'oneOf': [
                        {'type': 'string'},
                        {'type': 'array', 'items': {'type': 'string'}},
                    ],
                },
            },
            'required': ['paths'],
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
    'exp_attr_chain': tool_exp_attr_chain,
    'exp_cross_stats': tool_exp_cross_stats,
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

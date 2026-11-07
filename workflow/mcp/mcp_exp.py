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
]

HANDLERS = {
    'exp_detect': tool_exp_detect,
    'exp_stats': tool_exp_stats,
    'exp_query': tool_exp_query,
    'exp_refs': tool_exp_refs,
    'exp_baseline': tool_exp_baseline,
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

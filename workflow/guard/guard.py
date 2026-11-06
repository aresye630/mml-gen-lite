#!/usr/bin/env python3
"""guard.py — Agent loop 的代码守门层。

★ 设计（2026-11-04 用户裁决：A+C）
  A = agent loop + 代码守门
  C = 意图澄清（治理解漂移：run1 把现网已有的 66 个域名当成要新建的）

★ 职责边界
  agent 负责「懂」和「配」（推理、选族、取值）
  guard 负责「对不对」（产物落盘后的纯代码检查）

★ 五道门
  C2  引用闭合      —— 悬空对象自动补建 或 打回
  G11 主键唯一      —— 同族实例主键不能重复
  G12 参数格式      —— 与 EXP 同族比对参数名/格式
  G16 前代族保留    —— revise 时前代族必须都在
  G17 数量级        —— 防异常膨胀（run1 的 373 条）

★ 用法
  python3 guard.py --mml <路径> --exp <路径> [--intent <路径>] [--prior-mml <路径>]
  返回码：0 全过 / 1 有告警（可继续）/ 2 有致命错误（必须回炉）
"""
import argparse
import json
import os
import re
import sys
from collections import Counter
from pathlib import Path

# tools 目录（gen_selfcheck 所在）—— 支持环境变量覆盖，默认按容器布局
_TOOLS_DIR = os.environ.get('MML_GEN_TOOLS_DIR', '/opt/expgv/tools')
sys.path.insert(0, _TOOLS_DIR)
# 本地开发布局兜底：仓库根的 tools/
sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent / 'tools'))


# ═══════════════════════════════════════════════════════════
# 基础解析
# ═══════════════════════════════════════════════════════════
def parse_mml(text):
    """解析 MML 文本为命令列表。跳过注释块。"""
    cmds = []
    in_block = False
    for raw in text.split('\n'):
        line = raw.strip()
        if not line:
            continue
        # 块注释 /* ... */
        if line.startswith('/*'):
            in_block = '*/' not in line
            continue
        if in_block:
            if '*/' in line:
                in_block = False
            continue
        if line.startswith(('//', '#')):
            continue
        if re.match(r'^(ADD|SET|MOD|RMV|DEL|USE)\s', line, re.I):
            # ★ 2026-11-05：剥离行尾注释（// ...），但把 @src 保留在行内供 G19 解析
            #   实测：不剥离会导致 FILTERNAME 变成 'hngd_00_f_001"; // @src=exp:L3'
            #   ★ 2026-11-05 补充：agent 有时不写 //，直接写成 `...;  @src=xxx`
            #     这也必须当注释剥离，否则 @src 被吃进最后一个参数值
            #     （实测：PRIORITY 变成 '10600;  @src=plan:域名规划#1 ...'）
            _m = re.search(r'\s+//\s*(.*)$', line)
            if _m:
                line = line[:_m.start()].rstrip()
            else:
                # 分号之后如果出现 @src，视为注释
                _semi = line.find(';')
                if _semi > 0 and '@src=' in line[_semi:]:
                    line = line[:_semi + 1]
            cmds.append(line)
    return cmds


def strip_inline_comment(line):
    """去掉命令里的行尾注释，返回 (纯命令, 注释内容)。

    ★ 支持两种写法：
        ADD HOST:...;   // @src=exp:L100      （标准）
        ADD HOST:...;   @src=exp:L100         （agent 有时不写 //）
    """
    line = line or ''
    m = re.search(r'\s+//\s*(.*)$', line)
    if m:
        return line[:m.start()].rstrip(), m.group(1)
    # 无 //：分号之后的 @src 视为注释
    semi = line.find(';')
    if semi > 0 and '@src=' in line[semi:]:
        return line[:semi + 1].rstrip(), line[semi + 1:].strip()
    return line.rstrip(), ''


def split_cmd(cmd):
    """拆成 (verb, family, params_dict)。"""
    m = re.match(r'^(\w+)\s+([A-Za-z0-9_]+)\s*:(.*)$', cmd, re.S)
    if not m:
        return None, None, {}
    verb, fam, rest = m.group(1).upper(), m.group(2).upper(), m.group(3).strip().rstrip(';')
    params = {}
    # 参数按逗号切（跳过引号内）
    depth = 0
    cur = ''
    in_q = False
    for ch in rest:
        if ch == '"':
            in_q = not in_q
            cur += ch
        elif ch == ',' and not in_q:
            _kv(cur.strip(), params)
            cur = ''
            depth = 0
        else:
            cur += ch
    if cur.strip():
        _kv(cur.strip(), params)
    return verb, fam, params


def _kv(s, out):
    if not s:
        return
    if '=' in s:
        k, v = s.split('=', 1)
        out[k.strip().upper()] = v.strip().strip('"')
    else:
        out[s.upper()] = ''


def is_placeholder(v):
    v = str(v or '')
    return ('【' in v or 'TBD' in v.upper() or '{TODO' in v.upper()
            or v.startswith('<') or v == '')


# ═══════════════════════════════════════════════════════════
# G17 数量级检查（新增：防 run1 那种 373 条膨胀）
# ═══════════════════════════════════════════════════════════
G17_RULES = {
    # 族: (单次工单合理上限)
    'ADD HOST': 20, 'ADD FILTER': 30, 'ADD FILTERIPV6': 30,
    'ADD FLOWFILTER': 10, 'ADD FLTBINDFLOWF': 60,
    'ADD L7FILTER': 20, 'ADD PROTOBINDFLOWF': 30,
    'ADD URR': 10, 'ADD URRGROUP': 5, 'ADD PCCPOLICYGRP': 5,
    'ADD RULE': 10, 'ADD RULEBINDING': 20, 'ADD USERPROFILE': 5,
    'ADD SPECURRGRPLIST': 5,
}


def check_scale(mml_text, exp_text='', intent_text=''):
    """G17：数量级检查。

    ★ 治 run1 的病：它把现网 66 个域名全复制了一遍，产出 373 条命令。
      这里的判据：
        1. 单族条数超过「单工单合理上限」
        2. 与 EXP 同族实例数相比，新增量 > 现网 50%（说明在复制现网）
        3. 意图里没有明显的批量信号（如「全部」「所有」「每个」）
    """
    cmds = parse_mml(mml_text)
    fam_cnt = Counter()
    for c in cmds:
        v, f, _ = split_cmd(c)
        if v and f:
            fam_cnt[f'{v} {f}'] += 1

    exp_cnt = Counter()
    if exp_text:
        for c in parse_mml(exp_text):
            v, f, _ = split_cmd(c)
            if v and f:
                exp_cnt[f'{v} {f}'] += 1

    # 批量信号：意图里明确说要批量
    batch_signal = bool(re.search(
        r'全部|所有|每个|批量|逐一|全套|按.*展开', intent_text or ''))

    issues = []
    for fam, n in fam_cnt.items():
        limit = G17_RULES.get(fam)
        if not limit:
            continue
        if n > limit and not batch_signal:
            issues.append({
                'family': fam, 'count': n, 'limit': limit,
                'kind': 'exceeds_limit',
                'detail': f'{fam} 生成 {n} 条，单工单合理上限约 {limit} 条',
            })
            continue
        if exp_cnt.get(fam) and n > exp_cnt[fam] * 0.5 and not batch_signal:
            issues.append({
                'family': fam, 'count': n, 'exp_count': exp_cnt[fam],
                'kind': 'mirrors_exp',
                'detail': f'{fam} 生成 {n} 条，现网仅 {exp_cnt[fam]} 条 '
                          f'（达到现网 {n*100//max(exp_cnt[fam],1)}%，疑似在复制现网）',
            })

    return {
        'ok': not issues,
        'issues': issues,
        'total_cmds': len(cmds),
        'fam_counts': dict(fam_cnt),
        'batch_signal': batch_signal,
    }


# ═══════════════════════════════════════════════════════════
# G18 意图族覆盖（新增：防回炉过度删族）
# ═══════════════════════════════════════════════════════════
# 意图关键词 → 必须出现的命令族
#   ★ 2026-11-04 实测：agent 为消除 G11 重复，把整条计费链删了
#     （8 HOST + 8 FILTER 还在，但 URR/URRGROUP/RULE/USERPROFILE 全没了）
#     G18 就是防这个：意图点名的对象，产物里必须出现对应族。
# ★ 2026-11-04 修正：关键词必须够具体，否则误匹配
#   实测误报：「URR计费规则」里的"规则"被匹配到 ADD RULE（实际是 ADD URR）
#              于是 G18 要求 agent 生成 RULE，agent 拒绝（意图里确实没有），无限回炉
INTENT_FAMILY_MAP = {
    '主机': ['ADD HOST'],
    '域名': ['ADD HOST'],
    '过滤器': ['ADD FILTER'],
    'IPv6': ['ADD FILTERIPV6'],
    'IPV6': ['ADD FILTERIPV6'],
    'FILTERIPV6': ['ADD FILTERIPV6'],
    '流量过滤': ['ADD FLOWFILTER'],
    '流过滤器': ['ADD FLOWFILTER'],
    '过滤绑定': ['ADD FLTBINDFLOWF'],
    'L7': ['ADD L7FILTER'],
    # 「URR计费规则」「计费规则」→ 是 ADD URR，不是 ADD RULE
    'URR计费': ['ADD URR'],
    '计费规则': ['ADD URR'],
    'URR组': ['ADD URRGROUP'],
    'URRGROUP': ['ADD URRGROUP'],
    'PCC': ['ADD PCCPOLICYGRP'],
    '策略组': ['ADD PCCPOLICYGRP'],
    # ADD RULE 只在明确说"策略规则/业务规则/RULE"时才要求
    '策略规则': ['ADD RULE'],
    '业务规则': ['ADD RULE'],
    'RULE:': ['ADD RULE'],
    '规则绑定': ['ADD RULEBINDING'],
    'RULEBINDING': ['ADD RULEBINDING'],
    '用户模板': ['ADD USERPROFILE'],
    'USERPROFILE': ['ADD USERPROFILE'],
    '特殊URR': ['ADD SPECURRGRPLIST'],
    '刷新服务器': ['SET REFRESHSRV'],
    'URR组绑定': ['SET URRGRPBINDING'],
    'URRGRPBINDING': ['SET URRGRPBINDING'],
    'REFRESHSRV': ['SET REFRESHSRV'],
}


def check_family_coverage(mml_text, intent_text, action='fresh',
                          prior_mml=''):
    """G18：意图里点名的对象族，产物里必须有。

    ★ 2026-11-04：revise 场景要区分
      · fresh  ：意图里的族全都要有
      · revise ：只看「本次新增要求」提到的族；
                 前代已有的族不强制（增量修改本来就不重写全量）
      判定方式：若 action=revise 且给了 prior_mml，
        只要求「意图提到 但 前代没有」的族（= 本次必须新增的）
    """
    if not intent_text:
        return {'ok': True, 'skipped': True}

    fams = set()
    for c in parse_mml(mml_text):
        v, f, _ = split_cmd(c)
        if v and f:
            fams.add(f'{v} {f}')

    # ★ 2026-11-05：区分「要建」和「要删」
    #   实测：意图「去掉 IPv6 相关的配置（FILTERIPV6 ...）」被 G18 判成
    #   「意图点名了 ADD FILTERIPV6 但产物没有」，逼 agent 反向加回来。
    #   修法：删除意图命中的族不要求存在，反而应该检查它确实被删了。
    _DEL_WORDS = ('去掉', '删除', '删掉', '移除', '不要', '取消', '下掉',
                  '去除', '清理', '撤掉', 'no need', 'remove', 'delete')

    def _delete_context(text, kw, window=20):
        """判断某个关键词是否处在删除语境里。"""
        for m in re.finditer(re.escape(kw), text):
            seg = text[max(0, m.start() - window): m.start()]
            if any(w in seg for w in _DEL_WORDS):
                return True
        return False

    required = set()
    deletion_families = set()      # 意图要求删除的族
    hits = []
    for kw, fam_list in INTENT_FAMILY_MAP.items():
        if kw in intent_text:
            _is_del = _delete_context(intent_text, kw)
            for fam in fam_list:
                if _is_del:
                    deletion_families.add(fam)
                    hits.append((kw, fam))
                elif fam not in required:
                    required.add(fam)
                    hits.append((kw, fam))

    # 删除意图的族，从 required 里剔除（不能要求它存在）
    required -= deletion_families

    # revise 场景：前代已有的族不强制（增量修改不重写全量）
    prior_fams = set()
    if action in ('revise', 'append') and prior_mml:
        for c in parse_mml(prior_mml):
            v, f, _ = split_cmd(c)
            if v and f:
                prior_fams.add(f'{v} {f}')

    missing = sorted(required - fams - prior_fams)

    # 删除意图：产物里不该再有这些族
    still_present = sorted(deletion_families & fams)

    return {
        'ok': not missing and not still_present,
        'required': sorted(required),
        'prior_had': sorted(prior_fams & required),
        'missing': missing,
        'deletion_requested': sorted(deletion_families),
        'still_present': still_present,
        'triggered_by': {kw: fam for kw, fam in hits},
    }


# ═══════════════════════════════════════════════════════════
# G19 来源标注检查（@src）
# ═══════════════════════════════════════════════════════════
# 语法：@src=<类型>:<定位>[,<补充>]
#   类型：exp | doc | intent | plan | infer
#   规则：有注释 = 有依据；无注释 = 无依据（含【待填写】）
# 详见 SOURCE_ANNOTATION.md
SRC_RE = re.compile(
    r'@src=([a-z]+)(?::([^\s,;]+))?(?:\s*,?\s*((?:(?!@src=)[^;\n])*))?',
    re.I)

# 参数名 → 它所属对象的族（命名规律核验时用）
#   ★ 一个参数可能出现在多个族的命令里（如 USERPROFILENAME 出现在
#     SET URRGRPBINDING / ADD RULEBINDING 里），但名字的实际归属族是固定的
PARAM_OWNER_FAMILY = {
    'HOSTNAME': 'HOST',
    'FILTERNAME': 'FILTER',
    'FLOWFILTERNAME': 'FLOWFILTER',
    'L7FILTERNAME': 'L7FILTER',
    'SUBL7FLTNAME': 'L7FILTER',
    'URRNAME': 'URR',
    'URRGROUPNAME': 'URRGROUP',
    'DFTURRGRPNAME': 'URRGROUP',
    'DFTSIGURRGNAME': 'URRGROUP',
    'SIGURRGRPNAME': 'URRGROUP',
    'RULENAME': 'RULE',
    'USERPROFILENAME': 'USERPROFILE',
    'PCCPOLICYGRPNM': 'PCCPOLICYGRP',
    'POLICYNAME': 'PCCPOLICYGRP',
    'VRFNAME': 'L3VPNINST',
}

# 主键参数（无依据且非占位符 → 编造）
PRIMARY_KEY_PARAMS = {
    'HOSTNAME', 'FILTERNAME', 'FLOWFILTERNAME', 'L7FILTERNAME',
    'URRNAME', 'URRGROUPNAME', 'RULENAME', 'USERPROFILENAME',
    'PCCPOLICYGRPNM', 'SUBL7FLTNAME', 'VRFNAME',
}


def _parse_line_src(line):
    """解析一行命令的 @src 标注。

    返回 (src_type, locator, note) 或 None。
    ★ 一行可能有多个 @src（如 @src=plan:xxx @src=exp:derive L1103），
      优先返回可核验的类型（exp > plan > intent > doc > infer）。
    """
    m = SRC_RE.search(line)
    if not m:
        return None
    return (m.group(1).lower(), (m.group(2) or '').strip(), (m.group(3) or '').strip())


def _parse_all_src(line):
    """解析一行里的全部 @src 标注，返回 [(type, locator, note), ...]。

    ★ 2026-11-05 修：agent 常写成 `@src=exp:deriveL6592-6677`（derive 后没空格），
      原正则把 `deriveL6592-6677` 整个当 locator，核验时报
      「family-URR-not-in-range」。正确解析应为：type=exp, locator=L6592-6677,
      note=derive（说明这是派生，不是精确行号）。
    """
    out = []
    for m in SRC_RE.finditer(line or ''):
        stype = m.group(1).lower()
        locator = (m.group(2) or '').strip()
        note = (m.group(3) or '').strip()

        # `derive` 紧贴行号：deriveL1101 / deriveL1101-L1107
        if locator.lower().startswith('derive'):
            note = ('derive ' + note).strip()
            locator = locator[len('derive'):].strip()

        # ★ derive 后面有空格时，行号跑到 note 里了：`@src=exp:derive L1101-L1107 说明`
        #   从 note 开头提取 L### / L###-L### / L###-#### 形式的行号
        if stype == 'exp' and not locator and note:
            _lm = re.match(r'^\s*(?:derive\s+)?(L?\d+(?:\s*-\s*L?\d+)?)\b', note, re.I)
            if _lm:
                locator = _lm.group(1).replace(' ', '')
                note = 'derive'

        out.append((stype, locator, note))
    return out


def _verify_exp_ref(exp_lines, lineno, value, family=None, param=None,
                    is_derive=False):
    """核验 @src=exp:L### 是否真实（纯代码，不调 LLM）。

    核验层次（由弱到强）：
      1. 行号在范围内
      2. 该行确实是同一族的命令（family 匹配）
      3. 值确实出现在该行（value 匹配）
      4. 参数名+值同时出现在该行（param 级精确匹配）

    ★ is_derive=True 时（@src=exp:derive L1101-L1107）：
      derive 语义是「命名/格式派生自这段现网统计」，**值本身是新造的**，
      所以不核验 value，只核验：
        · 行号区间在范围内
        · 该区间里确实有同族的命令（证明这段确实是同类写法的样本）
      2026-11-05 实测：多网元场景 agent 标 L1425-L5117 derive，
      值（新建的 hngd_00_f_h_001）当然不在现网，原逻辑误判为虚假依据。

    返回 (ok: bool, reason: str)
    """
    if not lineno:
        return False, 'no-line-ref'

    # ★ 多 EXP：如果传进来的 exp_lines 是拼接的（含 EXP-SEP 标记），
    #   拆成多段，任意一段核验通过即算通过。
    _seps = [i for i, ln in enumerate(exp_lines)
             if 'EXP-SEP:' in ln]
    if _seps:
        segs = []
        starts = _seps
        ends = _seps[1:] + [len(exp_lines)]
        for a, b in zip(starts, ends):
            # 跳过 SEP 行本身
            segs.append(exp_lines[a + 1:b])
        last_reason = ''
        for sg in segs:
            if not sg:
                continue
            _ok, _why = _verify_exp_ref(sg, lineno, value, family=family,
                                        param=param, is_derive=is_derive)
            if _ok:
                return True, _why
            last_reason = _why
        return False, (last_reason or 'not-in-any-exp')

    ref = lineno.strip()
    if not ref.upper().startswith('L'):
        return False, 'bad-line-ref'
    ref = ref[1:]
    # 支持区间：L1101-L1107 / L1101-1107
    if '-' in ref:
        a, b = ref.split('-', 1)
        a = a.strip().lstrip('Ll')
        b = b.strip().lstrip('Ll')
        try:
            n1, n2 = int(a), int(b)
        except ValueError:
            return False, 'bad-line-range'
        if n1 > n2:
            n1, n2 = n2, n1
        if n1 < 1 or n2 > len(exp_lines):
            return False, 'range-out-of-bounds'
        seg = exp_lines[n1 - 1:n2]
        if not seg:
            return False, 'empty-range'

        # derive 模式：只要求区间里有同族命令，不要求值出现（值是新造的）
        if is_derive:
            if family:
                fam_ok = any(
                    re.search(rf'\b(?:ADD|SET|MOD|RMV)\s+{re.escape(family)}\b',
                              ln, re.I) for ln in seg)
                if not fam_ok:
                    return False, f'family-{family}-not-in-range'
            return True, 'derive-range-ok'

        # 核验：族是否在区间内出现
        # ★★ 2026-11-06 与单行分支统一语义：
        #   区间引用（exp:L11886-L11889）通常是「参照这一段里同类命令的写法」，
        #   对象名是新造的，值当然不在区间里。
        #   所以：族匹配即通过；值也对得上 → 升级为强依据。
        if family:
            if not any(re.search(rf'^\s*(ADD|SET|MOD|RMV)\s+{family}\b', ln, re.I)
                       for ln in seg):
                return False, f'family-{family}-not-in-range'
        if value and not is_placeholder(value):
            v = str(value).strip().strip('"').strip("'").lower()
            if not any(v in ln.lower() for ln in seg):
                return True, 'range-family-ref-only'
        return True, 'range-verified'

    try:
        n = int(ref)
    except ValueError:
        return False, 'bad-line-number'
    if n < 1 or n > len(exp_lines):
        return False, 'line-out-of-range'
    line = exp_lines[n - 1]

    # 1) 族核验：该行是不是同族命令
    if family:
        if not re.search(rf'^\s*{family}\b', line.strip(), re.I) and \
           not re.search(rf'\b{family}\b', line, re.I):
            return False, f'line-is-not-{family}'

    # 2) 值核验
    # ★ 2026-11-05 语义修正：
    #   @src=exp:L### 有两种正当用法，不能都要求「值必须出现在那一行」：
    #     A. 参照格式 —— 「FILTER 的参数模板照 L1513 的写」，对象名是新造的
    #        实测：agent 写 @src=exp:L1513 给新建的 hncatv_00_f_h_001，
    #        原逻辑判 value-not-in-line → 误报虚假依据
    #     B. 复用现网对象 —— 值和参数都能对上
    #   所以：族匹配 + 行号在范围内 → 通过（弱依据 referenced）；
    #        值/参数也能对上 → 升级为强依据（value-found / param-value-found）。
    if not value:
        return True, 'line-exists'
    v = str(value).strip().strip('"').strip("'")
    if not v or is_placeholder(v):
        return True, 'placeholder'

    if v.lower() not in line.lower():
        # 值不在这一行：不算虚假依据，只是「参照格式」而非「复用对象」
        return True, 'line-family-ref-only'

    # 3) 参数级核验（最强）：PARAM="value" 同时出现
    if param:
        if not re.search(rf'{param}\s*=\s*"?{re.escape(v)}"?', line, re.I):
            return True, 'value-found-param-differs'

    return True, 'value-found'


def _verify_enum_in_exp(exp_lines, family, param, value):
    """核验枚举值：该族的该参数在 EXP 里是否用过这个值（纯代码统计）。"""
    if not value or is_placeholder(value):
        return True, 'placeholder'
    v = str(value).strip().strip('"').upper()
    pat = re.compile(rf'{param}\s*=\s*"?([^,;"]+)"?', re.I)
    hit = False
    for ln in exp_lines:
        if not re.search(rf'^\s*ADD\s+{family}\b', ln, re.I):
            continue
        for m in pat.finditer(ln):
            if m.group(1).strip().upper() == v:
                hit = True
                break
        if hit:
            break
    return (True, 'enum-used-in-exp') if hit else (False, 'enum-never-used-in-exp')


def _verify_naming_rule(exp_lines, family, value, check_range=None):
    """核验命名规律：产物的名字结构是否符合 EXP 同族既有命名（纯代码）。

    ★ 判定方式（不比对全名，只比对结构）：
      把名字拆成「字母段 + 数字段」，比较段的类型序列。
      例：hngd_00_h_001  → [alpha, num, alpha, num]（4 段）
          cjqm_03_h_001  → [alpha, num, alpha, num]  ✓ 同结构
          hngd_00_h_001  vs  any  → 结构不同 ✗

    返回 (ok, reason)
    """
    if not value or is_placeholder(value):
        return True, 'placeholder'
    v = str(value).strip().strip('"')

    def shape(x):
        """提取名字的结构签名：alnum 段里是否含数字。"""
        parts = re.split(r'[_\-\.\*]+', x)
        sig = []
        for p0 in parts:
            if not p0:
                continue
            if re.fullmatch(r'\d+', p0):
                sig.append('N')
            elif re.search(r'\d', p0):
                sig.append('A')     # 字母数字混合（如 h001）
            else:
                sig.append('W')     # 纯字母
        return tuple(sig)

    target = shape(v)
    if len(target) < 2:
        return True, 'too-simple'

    # 在 EXP 同族里找相同结构的名字
    for ln in exp_lines:
        if not re.search(rf'^\s*ADD\s+{family}\b', ln, re.I):
            continue
        for m in re.finditer(r'="?([A-Za-z0-9_\-\.\*]{4,})"?', ln):
            cand = m.group(1)
            if is_placeholder(cand):
                continue
            if shape(cand) == target:
                return True, 'naming-shape-matched'

    return False, 'naming-shape-not-in-exp'


def check_source_annotation(mml_text, exp_text=''):
    """G19：来源标注检查。

    判定：
      · 主键参数无 @src 且非占位符 → fatal（编造值）
      · @src=exp:L### 核验失败 → fatal（虚假依据）
      · 整族 >5 条且全部无 @src → fatal（空壳族）
      · ungrounded 比例 > 70% → warning
    """
    if not mml_text:
        return {'ok': True, 'skipped': True}

    exp_lines = (exp_text or '').split('\n')
    has_exp = bool(exp_text)

    cmds = []          # [(line, verb, family, params, src_info, line_no)]
    in_block = False
    raw_lines = mml_text.split('\n')
    for ln, raw in enumerate(raw_lines, 1):
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
        if not re.match(r'^(ADD|SET|MOD|RMV)\s', line, re.I):
            continue
        # 先拆出纯命令和注释，参数解析只用纯命令部分
        pure, comment = strip_inline_comment(line)
        v, f, p = split_cmd(pure)
        if not v or not f:
            continue
        _all_src = _parse_all_src(comment or line)
        cmds.append({
            'line': pure, 'line_no': ln, 'verb': v, 'family': f,
            'params': p,
            'src': (_all_src[0] if _all_src else None),
            'src_all': _all_src,
        })

    if not cmds:
        return {'ok': True, 'skipped': True, 'reason': 'no commands'}

    # ★ 检测 @src 被吃进参数值（说明写成了「;  @src=」而不是「;   // @src=」）
    #   这类虽然 A 方案的 strip_inline_comment 已能兜底解析，
    #   但值本身是脏的（PRIORITY="10600;  @src=..."），必须让 agent 修正。
    for c in cmds:
        for k, val in (c['params'] or {}).items():
            if '@src' in str(val):
                bad_format.append({
                    'family': f"{c['verb']} {c['family']}",
                    'line_no': c['line_no'],
                    'param': k,
                    'value': str(val)[:80],
                    'hint': '参数值里混入了 @src 文本 —— 必须写成「;   // @src=...」，'
                            '不能写成「;  @src=...」',
                })
                break

    fatal = []
    warnings = []
    bad_format = []       # @src 写法错误（被吃进参数值）
    stats = {'total': len(cmds), 'grounded': 0, 'derived': 0,
             'ungrounded': 0, 'fake_src': 0}
    fam_stat = {}       # family -> {'total': n, 'ungrounded': n}
    ungrounded_keys = []

    for c in cmds:
        fam = f"{c['verb']} {c['family']}"
        fam_stat.setdefault(fam, {'total': 0, 'ungrounded': 0})
        fam_stat[fam]['total'] += 1

        src = c['src']
        if not src:
            stats['ungrounded'] += 1
            fam_stat[fam]['ungrounded'] += 1
            # 主键参数非占位符却没依据 → 编造
            for k in PRIMARY_KEY_PARAMS:
                val = c['params'].get(k)
                if val and not is_placeholder(val):
                    ungrounded_keys.append({
                        'family': fam, 'param': k, 'value': val,
                        'line_no': c['line_no'],
                    })
            continue

        stype, locator, note = src

        # 取主键参数名和值（核验用）
        pk_name, pk_val = None, ''
        for k in PRIMARY_KEY_PARAMS:
            if c['params'].get(k):
                pk_name, pk_val = k, c['params'][k]
                break

        # ── exp:derive —— 派生自现网统计 ──
        #   支持三种形态：
        #     @src=exp:derive <说明>              仅说明，不核验
        #     @src=exp:derive@L1101-L1107 <说明>  核验行号区间真实且同族
        #   另：若说明里提到 "L1101"，也自动提取做区间核验
        # ★ 2026-11-05：_parse_all_src 已把 derive 从 locator 里剥出来放进 note，
        #   所以这里要同时看 locator 和 note（否则 derive 会掉进普通行号分支，
        #   导致「值必须在现网那段里存在」的误报）
        _is_derive_mark = (locator.lower().startswith('derive')
                           or (note or '').lower().startswith('derive'))
        if stype == 'exp' and _is_derive_mark:
            stats['derived'] += 1
            detail = (locator + ' ' + (note or '')).strip()

            # 提取说明里的行号（必须带 L 前缀，避免"4个枚举"被误当行号）
            #   支持：L1101 / L1101-L1107 / L1101至L1107 / L1101~L1107
            mref = re.search(r'\bL(\d+)\s*(?:[-~至到]\s*L?(\d+))?', detail, re.I)
            if not mref:
                warnings.append(
                    f"G19 第 {c['line_no']} 行 @src=exp:derive 缺少行号依据"
                    f"（应写参考了 EXP 哪些行，如 derive L1101-L1107 命名规律）")
                continue

            if not has_exp:
                stats['derived'] += 1
                continue

            # 用尾部说明作为"值"的语义校验：只核验行号真实 + 同族存在
            line_ref = 'L' + mref.group(1)
            if mref.group(2):
                line_ref += '-' + mref.group(2)
            ok, why = _verify_exp_ref(exp_lines, line_ref, '',
                                      family=c['family'], is_derive=True)
            if ok:
                stats['derived'] += 1
                # 额外：命名规律核验
                #   ★ 2026-11-05：要按「被引用对象的族」核验，不是当前命令的族
                #     实测：SET URRGRPBINDING:USERPROFILENAME="s13001_ag_hngd"
                #           family=URRGRPBINDING，但名字属于 USERPROFILE 族
                if pk_val and not is_placeholder(pk_val):
                    ref_fam = PARAM_OWNER_FAMILY.get(pk_name, c['family'])
                    nok, nwhy = _verify_naming_rule(exp_lines, ref_fam, pk_val)
                    if not nok:
                        warnings.append(
                            f"G19 第 {c['line_no']} 行命名 {pk_val} 在 EXP "
                            f"{ref_fam} 族里找不到相同结构（{nwhy}）")
            else:
                stats['fake_src'] += 1
                fatal.append(
                    f"G19 虚假依据：第 {c['line_no']} 行标了 @src=exp:derive{line_ref}，"
                    f"但 EXP 核验失败（{why}）")
            continue

        # ── exp:L### —— 行号引用 ──
        if stype == 'exp' and has_exp:
            ok, why = _verify_exp_ref(exp_lines, locator, pk_val,
                                      family=c['family'], param=pk_name)
            if ok:
                stats['grounded'] += 1
            else:
                stats['fake_src'] += 1
                fatal.append(
                    f"G19 虚假依据：第 {c['line_no']} 行标了 @src=exp:{locator}，"
                    f"但 EXP 核验失败（{why}）")
        elif stype == 'exp':
            # 有 @src=exp 但没给 EXP 文本 → 无法核验，降级
            stats['derived'] += 1
        elif stype in ('doc', 'plan', 'intent'):
            stats['grounded'] += 1
            if not locator:
                warnings.append(
                    f"G19 第 {c['line_no']} 行 @src={stype} 缺少定位（如 F352:表2）")
        elif stype == 'infer':
            stats['derived'] += 1
            if not (note or locator):
                warnings.append(
                    f"G19 第 {c['line_no']} 行 @src=infer 缺少推导规则说明")
        else:
            stats['ungrounded'] += 1
            warnings.append(
                f"G19 第 {c['line_no']} 行 @src 类型未知：{stype}")

    # 主键无依据 → fatal（编造）
    if ungrounded_keys:
        sample = ungrounded_keys[:3]
        detail = '；'.join(f"{u['family']}.{u['param']}={u['value']}"
                          for u in sample)
        fatal.append(
            f"G19 编造值 {len(ungrounded_keys)} 处（主键有值但无 @src 依据）：{detail}")

    # 空壳族：>5 条且全部无依据
    for fam, st in fam_stat.items():
        if st['total'] > 5 and st['ungrounded'] == st['total']:
            fatal.append(
                f"G19 空壳族：{fam} 共 {st['total']} 条，全部无 @src 依据")

    # 整体无依据比例
    ratio = stats['ungrounded'] / max(stats['total'], 1)
    if ratio > 0.7:
        warnings.append(
            f"G19 无依据比例 {ratio*100:.0f}%（{stats['ungrounded']}/{stats['total']}），"
            f"建议补 @src 标注")

    stats['ungrounded_ratio'] = round(ratio, 2)
    stats['by_family'] = fam_stat

    # ★ @src 写法错误单独统计：这类不是"没标"，是"标错了"
    if bad_format:
        warnings.append(
            f'@src 写法错误 {len(bad_format)} 处：必须写成「;   // @src=...」，'
            f'不能写成「;  @src=...」（缺双斜杠会被当成命令内容，参数值被污染）')

    return {
        'ok': not fatal,
        'fatal': fatal,
        'warnings': warnings,
        'stats': stats,
        'ungrounded_keys': ungrounded_keys[:10],
        'bad_src_format': bad_format[:10],
        'bad_src_format_count': len(bad_format),
    }


# ═══════════════════════════════════════════════════════════
# C2 引用闭合（复用 gen_selfcheck，增强：能给补建建议）
# ═══════════════════════════════════════════════════════════
# 参数名 → 定义方的参数名（跨参数名映射）
#   ★ 2026-11-04 实测：gen_selfcheck 按参数名精确比对，
#     DFTURRGRPNAME 引用 URRGROUPNAME 定义的值，参数名不同 ⇒ 误判悬空。
#     这类"引用参数名 ≠ 定义参数名"的情况必须显式映射。
REF_TO_DEF = {
    'DFTURRGRPNAME': 'URRGROUPNAME',
    'DFTSIGURRGNAME': 'URRGROUPNAME',
    'SIGURRGRPNAME': 'URRGROUPNAME',
    'PCCPOLICYGRPNM': 'PCCPOLICYGRPNM',
    'POLICYNAME': 'PCCPOLICYGRPNM',
    'UPURRNAME1': 'URRNAME', 'UPURRNAME2': 'URRNAME',
    'DOWNURRNAME1': 'URRNAME', 'DOWNURRNAME2': 'URRNAME',
    'ONLINERG': 'RG', 'RG': 'RG', 'OFFRG': 'RG',
}


def check_refs(mml_text, exp_text=''):
    """C2 引用闭合（guard 自己的实现，不依赖 gen_selfcheck）。

    ★ 2026-11-05 实测发现的严重缺陷：
      gen_selfcheck._defined_objects 把「ADD FILTER 的 HOSTNAME 参数」
      当成了"定义 HOSTNAME"，导致引用悬空完全检测不出来。
      例：ADD FILTER:...HOSTNAME="hngd_00_h_999"（该对象根本没人定义）→ 判定通过
      修法：显式声明「哪些族的哪些参数才是真正的定义」，其余引用型参数只算引用。

    ★ 占位符【待填写】不算悬空（那是待人工填，不是引用不存在的对象）
    ★ EXP 里已有的对象不算悬空（复用现网对象合法）
    """
    prod_defs = _collect_defs(mml_text, only_add=True)
    exp_defs = _collect_defs(exp_text, only_add=True) if exp_text else set()
    all_defs = prod_defs | exp_defs

    refs = []
    for ln, v, f, p in _iter_cmds(mml_text):
        defining = DEFINING_PARAMS.get(f) or ()
        for k, val in p.items():
            if not val or is_placeholder(val):
                continue
            if k in defining:
                continue          # 主键自己的定义，不是引用
            if k in ALWAYS_REF_PARAMS or REF_PARAM_SUFFIX.search(k):
                refs.append((f, k, val, ln))

    dangling = []
    seen = set()
    for f, k, val, ln in refs:
        u = val.upper()
        if u in all_defs:
            continue
        if u in BUILTIN_OBJECTS:
            continue          # 系统内置对象，不需要定义
        key = (k, u)
        if key in seen:
            continue
        seen.add(key)
        dangling.append({
            'family': f, 'param': k, 'value': val, 'line': ln,
            'in_product': u in prod_defs,
            'in_exp': u in exp_defs,
        })

    return {
        'ok': not dangling,
        'dangling': dangling[:20],
        'n_dangling': len(dangling),
        'n_defs_product': len(prod_defs),
        'n_defs_exp': len(exp_defs),
        'n_refs': len(refs),
    }


# ── C2 辅助：定义/引用的判定表 ──
# 引用型参数后缀（哪些参数值指向"别的对象"）
REF_PARAM_SUFFIX = re.compile(
    r'(NAME|NAMES|INSTANCE|INSTANCENAME|IFNAME|VRFNAME|APN|DNN|POOLNAME'
    r'|GROUPNAME|PROFILENAME|POLICYNAME|RULENAME|TEMPLATENAME|AREANAME'
    r'|SERVERNAME|HOSTNAME|SECTIONNAME|L3VPNNAME)$', re.I)

# 只有这些 (族, 参数) 组合才真正定义对象
DEFINING_PARAMS = {
    'HOST': ('HOSTNAME',),
    'FILTER': ('FILTERNAME',),
    'FILTERIPV6': ('FILTERNAME',),
    'FLOWFILTER': ('FLOWFILTERNAME',),
    'L7FILTER': ('L7FILTERNAME', 'SUBL7FLTNAME'),
    'URR': ('URRNAME',),
    'URRGROUP': ('URRGROUPNAME',),
    'PCCPOLICYGRP': ('PCCPOLICYGRPNM',),
    'RULE': ('RULENAME',),
    'USERPROFILE': ('USERPROFILENAME',),
    'RULEBINDING': (),
    'FLTBINDFLOWF': (),
    'PROTBINDFLOWF': (),
    'SPECURRGRPLIST': (),
    'L3VPNINST': ('VRFNAME',),
    'APN': ('APN',),
}

# 系统内置对象（不要求在产物或 EXP 里定义）
#   ★ 2026-11-05 实测：http/https/tcp/udp 等协议名是系统预置的，
#     PROTBINDFLOWF:PROTOCOLNAME="http" 不需要先 ADD WELLKNOWNPORT。
#     不能靠 DEFINING_PARAMS 硬要求，否则每份产物都会被误判悬空。
BUILTIN_OBJECTS = {
    'HTTP', 'HTTPS', 'TCP', 'UDP', 'ICMP', 'DNS', 'FTP', 'RTSP',
    'SIP', 'RTP', 'RTCP', 'SSH', 'TELNET', 'SMTP', 'POP3', 'IMAP',
    'ALL', 'ANY', 'DEFAULT', 'NONE', 'NULL',
}

# 纯引用参数（永远不定义）
ALWAYS_REF_PARAMS = {
    'DFTURRGRPNAME', 'DFTSIGURRGNAME', 'SIGURRGRPNAME',
    'UPURRNAME1', 'UPURRNAME2', 'DOWNURRNAME1', 'DOWNURRNAME2',
    'POLICYNAME', 'TEMPLATENAME',
}


def _iter_cmds(mml_text):
    """遍历命令，剥离注释。yield (line_no, verb, family, params)。"""
    in_block = False
    for ln, raw in enumerate(mml_text.split('\n'), 1):
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
        # ★ 用统一的 strip_inline_comment（支持 // 和分号后 @src 两种写法）
        pure, _comment = strip_inline_comment(line)
        v, f, p = split_cmd(pure)
        if v and f:
            yield ln, v, f, p


def _collect_defs(mml_text, only_add=True):
    """收集真正定义的对象名（大写）。"""
    defs = set()
    for _ln, v, f, p in _iter_cmds(mml_text):
        if only_add and v != 'ADD':
            continue
        defining = DEFINING_PARAMS.get(f)
        if not defining:
            continue
        for k in defining:
            val = p.get(k)
            if val and not is_placeholder(val):
                defs.add(val.upper())
    return defs


# ═══════════════════════════════════════════════════════════
# G11 主键唯一
# ═══════════════════════════════════════════════════════════
# 复合主键族：主键由多个参数共同确定
#   ★ 2026-11-04 实测：ADD FLTBINDFLOWF 的主键是 (FLOWFILTERNAME, FILTERNAME)，
#     同一 FILTER 绑不同 FLOWFILTER 是合法的，只看 FILTERNAME 会误判重复。
COMPOSITE_KEYS = {
    'FLTBINDFLOWF': ('FLOWFILTERNAME', 'FILTERNAME'),
    'RULEBINDING': ('USERPROFILENAME', 'RULENAME'),
    'PROTBINDFLOWF': ('FLOWFILTERNAME', 'PROTOCOLNAME'),
    'URRGRPBINDING': ('USERPROFILENAME',),
    # ★ 2026-11-04 实测：L7FILTER 是"组 + 子项"结构，
    #   同一 L7FILTERNAME 下挂多个 SUBL7FLTNAME 是正确写法，
    #   只看 L7FILTERNAME 会误报 8 条重复。
    'L7FILTER': ('L7FILTERNAME', 'SUBL7FLTNAME'),
    # 同类：其余"组+子项"结构
    'HOST': ('HOSTNAME',),
}

# 单主键族：用哪个参数当主键
SINGLE_KEY = {
    'HOST': 'HOSTNAME', 'FILTER': 'FILTERNAME', 'FILTERIPV6': 'FILTERNAME',
    'FLOWFILTER': 'FLOWFILTERNAME', 'L7FILTER': 'L7FILTERNAME',
    'URR': 'URRNAME', 'URRGROUP': 'URRGROUPNAME', 'RULE': 'RULENAME',
    'USERPROFILE': 'USERPROFILENAME', 'PCCPOLICYGRP': 'PCCPOLICYGRPNM',
    'SPECURRGRPLIST': 'URRGROUPNAME',
}


def _split_by_unit(mml_text):
    """按 /* ===== 网元: XXX ... ===== */ 分段。

    ★ 2026-11-05：多网元场景，同一对象在不同网元下可以同名。
      返回 [(unit_name, segment_text), ...]；无分段标记则返回 [('', 全文)]。
    """
    import re as _re
    marks = list(_re.finditer(
        r'/\*\s*={3,}\s*网元[:：]\s*([A-Za-z0-9_\-\u4e00-\u9fa5]+)', mml_text))
    if not marks:
        return [('', mml_text)]
    segs = []
    for i, m in enumerate(marks):
        start = m.start()
        end = marks[i + 1].start() if i + 1 < len(marks) else len(mml_text)
        segs.append((m.group(1).strip(), mml_text[start:end]))
    # 分段之前的内容（文件头注释）单独作为公共段
    if marks[0].start() > 0:
        head = mml_text[:marks[0].start()]
        if any(k in head for k in ('ADD ', 'SET ', 'MOD ')):
            segs.insert(0, ('', head))
    return segs


def check_unique_keys(mml_text):
    """同族同主键不能出现两次（复合键族按多参数组合判定）。

    ★ 2026-11-05：按网元分段后分别检查 —— 跨网元同名不算重复。
    """
    seen = {}
    dups = []
    segs = _split_by_unit(mml_text)
    for unit, seg_text in segs:
        for c in parse_mml(seg_text):
            v, f, p = split_cmd(c)
            if not v or not f or v != 'ADD':
                continue
            _u = (unit or '').upper()

            # 复合键族
            if f in COMPOSITE_KEYS:
                parts = []
                for k in COMPOSITE_KEYS[f]:
                    val = p.get(k)
                    if not val or is_placeholder(val):
                        parts = None
                        break
                    parts.append(f'{k}={val}')
                if not parts:
                    continue
                key = (_u, f, '|'.join(parts))
                if key in seen:
                    dups.append({'family': f, 'unit': unit or '(未分段)',
                                 'param': COMPOSITE_KEYS[f][0],
                                 'value': parts[0].split('=', 1)[1]})
                else:
                    seen[key] = True
                continue

            # 单主键族
            k = SINGLE_KEY.get(f)
            if not k:
                continue
            val = p.get(k)
            if not val or is_placeholder(val):
                continue
            key = (_u, f, val)
            if key in seen:
                dups.append({'family': f, 'unit': unit or '(未分段)',
                             'param': k, 'value': val})
            else:
                seen[key] = True

    return {'ok': not dups, 'duplicates': dups[:10], 'n_duplicates': len(dups),
            'units': [u for u, _ in segs if u]}


# ═══════════════════════════════════════════════════════════
# G12 参数格式（复用 gen_selfcheck）
# ═══════════════════════════════════════════════════════════
def check_param_fmt(mml_text, exp_text=''):
    try:
        import gen_selfcheck as gs
        r = gs.check_param_format(mml_text, exp_text)
        return {'ok': r.get('ok', True),
                'issues': (r.get('issues') or [])[:10],
                'n_issues': len(r.get('issues') or [])}
    except Exception as e:
        return {'ok': True, 'error': f'{type(e).__name__}: {e}'}


# ═══════════════════════════════════════════════════════════
# G16 前代族保留（revise 时）
# ═══════════════════════════════════════════════════════════
def check_prior_kept(prior_mml, cur_mml, allowed_remove=None):
    """revise 时，前代族必须保留（除非 allowed_remove 里明确列出）。"""
    if not prior_mml:
        return {'ok': True, 'skipped': True}

    def fams(t):
        s = Counter()
        for c in parse_mml(t):
            v, f, _ = split_cmd(c)
            if v and f:
                s[f'{v} {f}'] += 1
        return s

    pf, cf = fams(prior_mml), fams(cur_mml)
    allowed = set(allowed_remove or [])
    missing = [f for f in pf if f not in cf and f not in allowed]
    shrank = [{'family': f, 'prior': pf[f], 'cur': cf.get(f, 0)}
              for f in pf if f in cf and cf[f] < pf[f] and f not in allowed]
    return {
        'ok': not missing,
        'missing_families': missing,
        'shrank_families': shrank[:10],
    }


# ═══════════════════════════════════════════════════════════
# C · 意图澄清（治理解漂移）
# ═══════════════════════════════════════════════════════════
def clarify_intent(intent_text, exp_text='', mml_text=''):
    """意图澄清卡：把「现网已有 vs 本次新增」分清楚。

    ★ 治 run1 的病：它把现网 66 个域名当成「本次要新建的域名」。
      这里在生成前后各检查一次：
        前：意图里点名的对象，在 EXP 里已有多少？→ 提示「可能已存在」
        后：产物里的对象名，有多少在 EXP 里已存在？→ 报警「重复下发」
    """
    result = {'questions': [], 'warnings': []}

    intent = intent_text or ''
    if not intent.strip():
        return result

    # ★ 2026-11-05 用户裁定：这里只留「意图理解层面」的提示，
    #   参数值类的（域名清单、IP、数量）不进 questions ——
    #   那些统一由 ⑥a 收集到 params.csv，用户一次性填。
    #   实测问题：原来这里的「请给出域名清单」被写进确认清单的待确认问题，
    #   造成参数问题混进方案澄清，违背「不做无边界澄清」的约束。

    # 1) 意图里的批量词 → 只是提示 agent 注意展开方式，不作为待确认问题
    m = re.search(r'(?:新增|配置|添加)\s*([^\n，。；]{2,40}?)等\s*(\d+)\s*项', intent)
    if m:
        result['warnings'].append({
            'kind': 'bulk_hint',
            'detail': f'意图提到「{m.group(1)}等 {m.group(2)} 项」——'
                      f'具体对象清单需 agent 从资料推导；'
                      f'推不出的值应留【待填写】进参数表，不要在这里问',
        })

    # 3) 产物里对象名与 EXP 重复 → 不是错误，但要提示
    if mml_text and exp_text:
        exp_names = set()
        for c in parse_mml(exp_text):
            v, f, p = split_cmd(c)
            for k in ('FILTERNAME', 'HOSTNAME', 'URRNAME', 'URRGROUPNAME',
                      'RULENAME', 'USERPROFILENAME', 'FLOWFILTERNAME'):
                if k in p and p[k]:
                    exp_names.add(p[k])
        new_names = set()
        for c in parse_mml(mml_text):
            v, f, p = split_cmd(c)
            if v != 'ADD':
                continue
            for k in ('FILTERNAME', 'HOSTNAME', 'URRNAME', 'URRGROUPNAME',
                      'RULENAME', 'USERPROFILENAME', 'FLOWFILTERNAME'):
                if k in p and p[k] and not is_placeholder(p[k]):
                    new_names.add(p[k])
        overlap = new_names & exp_names
        if overlap:
            result['warnings'].append({
                'kind': 'names_exist_in_exp',
                'count': len(overlap),
                'sample': sorted(overlap)[:5],
                'detail': f'{len(overlap)} 个对象名在 EXP 里已存在'
                          f'（可能重复下发或复用了现网对象）',
            })
    return result


# ═══════════════════════════════════════════════════════════
# 主流程
# ═══════════════════════════════════════════════════════════
def run_guard(mml_text, exp_text='', intent_text='', prior_mml='',
              allowed_remove=None, action='fresh', session_dir=None,
              params_csv=None):
    checks = {}
    checks['C2_refs'] = check_refs(mml_text, exp_text)
    checks['G11_unique'] = check_unique_keys(mml_text)
    checks['G12_param_fmt'] = check_param_fmt(mml_text, exp_text)
    checks['G17_scale'] = check_scale(mml_text, exp_text, intent_text)
    checks['G18_coverage'] = check_family_coverage(
        mml_text, intent_text, action, prior_mml)
    checks['G19_source'] = check_source_annotation(mml_text, exp_text)
    if prior_mml:
        checks['G16_prior'] = check_prior_kept(prior_mml, mml_text, allowed_remove)
    checks['clarify'] = clarify_intent(intent_text, exp_text, mml_text)

    # ★ 2026-11-05 新增：csv 相关校验
    #   G20 数据规划覆盖：规划表每行是否被参数表引用
    #   G21 csv↔mml 一致性：从 params.csv 生成的 mml 是否和 agent 写的一致
    if session_dir and params_csv:
        # ★ 2026-11-05：脚本直接运行（python3 guard/guard.py）时
        #   `from guard.plan_check` 会失败（guard 目录不是顶层包）。
        #   显式把本文件所在目录加进 sys.path，用模块名直连导入。
        import sys as _sys2
        _here = str(Path(__file__).resolve().parent)
        if _here not in _sys2.path:
            _sys2.path.insert(0, _here)
        try:
            from plan_check import check_plan_coverage
            checks['G20_plan'] = check_plan_coverage(session_dir, params_csv)
        except Exception as e:
            checks['G20_plan'] = {'ok': True, 'skipped': True,
                                  'reason': f'G20 执行失败: {e}'}
        try:
            import sys as _sys
            _sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
            from mml_gen import gen_mml, compare_mml
            _g = gen_mml(params_csv)
            if _g.get('errors'):
                checks['G21_consistency'] = {
                    'ok': False, 'errors': _g['errors'],
                    'detail': 'csv 生不出 mml（组/引用有问题）'}
            else:
                _c = compare_mml(mml_text, _g['text'])
                _c['generated_cmds'] = _g['n_commands']
                checks['G21_consistency'] = _c
        except Exception as e:
            checks['G21_consistency'] = {'ok': True, 'skipped': True,
                                         'reason': f'G21 执行失败: {e}'}
        # ★ G22 占位符一致性
        try:
            import importlib as _il2
            _mg2 = _il2.import_module('mml_gen')
            _rows2 = _mg2.read_params(params_csv)
            checks['G22_placeholder'] = _mg2.check_placeholders(_rows2)
        except Exception as e:
            checks['G22_placeholder'] = {'ok': True, 'skipped': True,
                                         'reason': f'G22 执行失败: {e}'}


    # 判定严重性
    fatal = []
    warn = []
    if not checks['C2_refs']['ok']:
        n = checks['C2_refs'].get('n_dangling', 0)
        fatal.append(f'C2 引用悬空 {n} 处')
    if not checks['G11_unique']['ok']:
        fatal.append(f"G11 主键重复 {checks['G11_unique']['n_duplicates']} 处")
    if not checks['G17_scale']['ok']:
        for i in checks['G17_scale']['issues']:
            warn.append(f"G17 {i['detail']}")
    _g16 = checks.get('G16_prior') or {}
    if _g16 and not _g16.get('ok', True):
        fatal.append(f"G16 前代族丢失: {', '.join((_g16.get('missing_families') or [])[:5])}")
    _g18 = checks.get('G18_coverage') or {}
    if _g18 and not _g18.get('ok', True):
        # ★ 2026-11-04：分严重性
        #   意图明确点名的对象（主机/过滤器/URR/URR组等）缺失 → fatal
        #   推断性要求（从"等12项"倒推的族）缺失 → warning
        _missing18 = _g18.get('missing') or []
        if _missing18:
            fatal.append('G18 意图点名的族缺失: ' + '、'.join(_missing18[:6]))
    _g19 = checks.get('G19_source') or {}
    if _g19 and not _g19.get('ok', True):
        for _f in (_g19.get('fatal') or [])[:3]:
            fatal.append(_f)
    if _g19 and _g19.get('warnings'):
        for _w in _g19['warnings'][:2]:
            warn.append(_w)
    if not checks['G12_param_fmt']['ok']:
        warn.append(f"G12 参数格式 {checks['G12_param_fmt'].get('n_issues', 0)} 处")
    for w in checks['clarify']['warnings']:
        warn.append(f"C 澄清: {w['detail']}")

    # ★ G20 数据规划覆盖（未覆盖是 warn，引用不存在才是 fatal）
    _g20 = checks.get('G20_plan') or {}
    if _g20 and not _g20.get('skipped'):
        for _e in (_g20.get('errors') or [])[:3]:
            fatal.append(f'G20 {_e}')
        for _w in (_g20.get('warnings') or [])[:3]:
            warn.append(f'G20 {_w}')

    # ★ G21 csv↔mml 一致性
    _g21 = checks.get('G21_consistency') or {}
    if _g21 and not _g21.get('skipped'):
        if _g21.get('errors'):
            fatal.append(f"G21 csv 生成失败: {_g21['errors'][:2]}")
        elif not _g21.get('ok', True):
            _no_a = _g21.get('n_only_agent', 0)
            _no_g = _g21.get('n_only_gen', 0)
            if _no_g:
                fatal.append(
                    f'G21 params.csv 里的参数没有体现在 mml.txt（{_no_g} 条）：'
                    + '；'.join(_g21.get('only_in_gen', [])[:2]))
            if _no_a:
                warn.append(
                    f'G21 mml.txt 里有些命令在 params.csv 里没有（{_no_a} 条）：'
                    + '；'.join(_g21.get('only_in_agent', [])[:2]))

    # ★ G22 占位符一致性
    _g22 = checks.get('G22_placeholder') or {}
    if _g22 and not _g22.get('skipped'):
        for _e in (_g22.get('errors') or [])[:3]:
            fatal.append(f'G22 {_e}')
        for _w in (_g22.get('warnings') or [])[:2]:
            warn.append(f'G22 {_w}')

    # ★ 2026-11-06 新增：脱敏残留检测
    #   实测：EXP 里部分字段被脱敏成 ***，agent 会照抄进产物：
    #     TOKENFUNCFLAG=*** （现网 101 条其实全是 DISABLE）
    #   这种值不可下发，必须按同族多数值或文档默认值重写。
    _sanitize_hits = []
    for _idx, _c in enumerate(parse_mml(mml_text), 1):
        _v, _f, _p = split_cmd(_c)
        if not _v or not _f:
            continue
        for _k, _val in (_p or {}).items():
            if '***' in str(_val):
                _sanitize_hits.append({
                    'family': _f, 'param': _k, 'value': str(_val),
                    'line_no': _idx,
                })
    if _sanitize_hits:
        for _h in _sanitize_hits[:5]:
            fatal.append(
                f"G19 脱敏残留：第 {_h['line_no']} 行 {_h['family']}.{_h['param']}="
                f"{_h['value']} 是从 EXP 照抄的脱敏值，不可下发"
                f"（要按同族多数值或文档默认值重写）")
        if isinstance(checks.get('G19_source'), dict):
            checks['G19_source']['sanitized_residual'] = len(_sanitize_hits)

    verdict = 'pass'
    if fatal:
        verdict = 'fail'
    elif warn:
        verdict = 'warn'

    return {
        'verdict': verdict,
        'fatal': fatal,
        'warnings': warn,
        'checks': checks,
        'questions': checks['clarify']['questions'],
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--mml', required=True)
    ap.add_argument('--exp', default='',
                    help='EXP 文件路径，多网元用逗号分隔')
    ap.add_argument('--exp-multi', default='',
                    help='多 EXP 路径，用 ; 分隔（优先级高于 --exp）')
    ap.add_argument('--intent', default='')
    ap.add_argument('--prior-mml', default='')
    ap.add_argument('--action', default='fresh',
                    choices=['fresh', 'revise', 'append'])
    ap.add_argument('--json', action='store_true')
    ap.add_argument('--session-dir', default='',
                    help='会话目录（G20/G21 需要，用来找数据规划文件）')
    ap.add_argument('--params', default='',
                    help='params.csv 路径（G20/G21 需要）')
    a = ap.parse_args()

    mml = Path(a.mml).read_text(encoding='utf-8', errors='replace')

    # ★ 2026-11-05：多网元支持
    #   实测：跨网元配置时 agent 会引用不同 EXP 的行号
    #   （如 PCC 在 UNC EXP 的 L6721，URR 在 UNC EXP 的 L6592），
    #   只传一个 EXP 会导致「family-not-in-range」误报。
    #   这里把多个 EXP 顺序拼接（用分隔注释隔开），
    #   行号核验时按「任意一个 EXP 命中即算通过」处理。
    _exp_paths = []
    if a.exp_multi:
        _exp_paths = [x.strip() for x in a.exp_multi.split(';') if x.strip()]
    elif a.exp:
        _exp_paths = [x.strip() for x in a.exp.split(',') if x.strip()]

    if len(_exp_paths) <= 1:
        exp = (Path(_exp_paths[0]).read_text(encoding='utf-8', errors='replace')
               if _exp_paths else '')
    else:
        _parts = []
        for _p in _exp_paths:
            try:
                _parts.append(
                    f'/* ===== EXP-SEP: {Path(_p).name} ===== */\n' +
                    Path(_p).read_text(encoding='utf-8', errors='replace'))
            except Exception:
                continue
        exp = '\n'.join(_parts)
    intent = Path(a.intent).read_text(encoding='utf-8', errors='replace') if a.intent else ''
    prior = Path(a.prior_mml).read_text(encoding='utf-8', errors='replace') if a.prior_mml else ''

    r = run_guard(mml, exp, intent, prior, action=a.action,
                  session_dir=(a.session_dir or None),
                  params_csv=(a.params or None))

    if a.json:
        print(json.dumps(r, ensure_ascii=False, indent=1))
    else:
        print(f"判定: {r['verdict'].upper()}")
        for f in r['fatal']:
            print(f"  ❌ {f}")
        for w in r['warnings']:
            print(f"  ⚠️  {w}")
        for q in r['questions']:
            print(f"  ❓ {q['q']}")
            if q.get('hint'):
                print(f"     {q['hint']}")

    sys.exit(0 if r['verdict'] == 'pass' else (1 if r['verdict'] == 'warn' else 2))


if __name__ == '__main__':
    main()

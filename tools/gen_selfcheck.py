# -*- coding: utf-8 -*-
"""gen_selfcheck.py — 生成产物自检（方案层 + 装配层）。

三条校验，全部只依赖「本次产物 + 现网 EXP + 输入意图」，不依赖 GT：

  C1 装配一致性：方案(配置分析md) 的命令族  vs  mml.txt 的命令族
        → 方案有、mml 没有 = 装配丢失
  C2 引用完整性：每条命令的引用型参数，其对象须有定义（本方案内 或 EXP）
        → 悬空引用 = 方案不可执行
  C3 重复下发：与 EXP 逐条比对，完全相同的命令应剔除
        → EXP 已有 = 重复下发

所有函数纯函数式，输入文本，输出告警列表，便于单测。
"""
import re
from collections import defaultdict

# ── MML 解析 ──
_CMD_RE = re.compile(
    r'^\s*(ADD|MOD|SET|RMV|DEL|DEA|LCK|ULK|ACT|STP|STR)\s+([A-Z][A-Z0-9_]*)\s*:(.*)$')

# 查询/运行态命令不参与"方案完整性"判断（它们可以不在 mml 里）
QUERY_VERBS = {'LST', 'DSP', 'SHW'}
RUNTIME_VERBS = {'ACT', 'DEA', 'LCK', 'ULK', 'STP', 'STR'}

# 引用型参数：取值是一个"被定义的对象名"
# 判定不靠命令白名单，靠参数名后缀 + 值形态
REF_PARAM_SUFFIX = re.compile(
    r'(NAME|NAMES|INSTANCE|INSTANCENAME|IFNAME|VRFNAME|APN|DNN|POOLNAME'
    r'|GROUPNAME|PROFILENAME|POLICYNAME|RULENAME|TEMPLATENAME|AREANAME'
    r'|SERVERNAME|HOSTNAME|SECTIONNAME|L3VPNNAME)$', re.I)

# ⚠ 值不像"对象名"的：只排除纯数字 / IP / UUID / 占位符。
#   不能靠"全大写"排除 —— 实测 VRF_B / VPN_A / APN_SOS 这类对象名也是全大写，
#   早期用 `[A-Z][A-Z0-9_]*` 排除会把它们误当枚举值，导致悬空引用抓不出来
#   （自测 T2 曾因此失效）。是否"引用型"只由【参数名】决定，见 REF_PARAM_SUFFIX。
_NOT_REF_VALUE = re.compile(
    r'^('
    r'\d+'                                    # 纯数字
    r'|0x[0-9A-Fa-f]+'                          # 十六进制
    r'|[0-9A-Fa-f]{8}-[0-9A-Fa-f-]{27}'         # UUID
    r'|\d{1,3}(\.\d{1,3}){3}(/\d+)?'           # IPv4
    r'|[0-9A-Fa-f]*:[0-9A-Fa-f:]+(/\d+)?'        # IPv6
    r'|<[^>]*>'                                 # 占位符 <Xxx>
    r')$')


def parse_mml(text):
    """解析 MML 文本 → [(verb, cmd, {param: value}), ...]"""
    out = []
    for line in (text or '').split('\n'):
        s = line.strip()
        if not s or s.startswith('//') or s.startswith('#'):
            continue
        m = _CMD_RE.match(s)
        if not m:
            continue
        verb, cmd, body = m.group(1), m.group(2), m.group(3)
        params = {}
        for pm in re.finditer(r'([A-Za-z0-9_]+)\s*=\s*(?:"([^"]*)"|([^,;]+))', body):
            key = pm.group(1).upper()
            val = (pm.group(2) if pm.group(2) is not None else pm.group(3)).strip()
            params[key] = val
        out.append((verb, cmd, params))
    return out


def _fams(cmds):
    """命令族集合，排除查询类。"""
    return {f'{v} {c}' for v, c, _ in cmds if v not in QUERY_VERBS}


def _key_of(val):
    """参数值归一化（去引号/空白/大小写）。"""
    return (val or '').strip().strip('"').strip("'").strip().upper()


# ══════════════════════════════════════════════════════════
# C1 装配一致性
# ══════════════════════════════════════════════════════════
# 非本网元执行的章节标记（实测：方案 md 里会有「跨 NF — SMF 侧需同步配置（不在本产物执行）」段，
# 段内命令明确标注本网元不执行。若把它们算作"方案应产出"，C1 会误报装配丢失
# （实测 NC20260805002150 误报 12 族，全部是该段内的 SMF 侧命令）。
NON_TARGET_HEADING = re.compile(
    r'^#{1,6}[^\n]*(跨\s*NF|不在本产物|不在本网元|仅作.{0,6}对照|SMF\s*侧需|需同步配置)[^\n]*$',
    re.I | re.M)

NON_TARGET_INLINE = re.compile(
    r'仅作.{0,8}对照|本网元.{0,10}不执行|不在本产物执行|需 SMF 侧配置', re.I)


def _exclude_non_target(plan_text):
    """去掉"非本网元执行"的章节，只留本网元要产出的命令。

    两种形态都处理：
      · 章节标题含「跨NF / 不在本产物执行 / SMF侧需同步配置」→ 整节丢弃
      · 代码块后紧跟「⚠ 上述…本网元不执行」→ 该块丢弃
    """
    text = plan_text or ''
    # 1) 按标题切，丢弃标题命中的节
    lines = text.split('\n')
    kept, skip = [], False
    for ln in lines:
        if re.match(r'^#{1,6}\s', ln):
            skip = bool(NON_TARGET_HEADING.match(ln))
        if not skip:
            kept.append(ln)
    text = '\n'.join(kept)
    # 2) 代码块 + 紧跟的「本网元不执行」说明 → 去掉该块
    out, buf, in_block = [], [], False
    for ln in text.split('\n'):
        if ln.strip().startswith('```'):
            if not in_block:
                in_block, buf = True, [ln]
            else:
                in_block = False
                buf.append(ln)
                # 看块后 5 行有没有"不执行"说明
                out.append(('__BLOCK__', list(buf)))
                buf = []
            continue
        if in_block:
            buf.append(ln)
        else:
            out.append(ln)
    # 后处理：__BLOCK__ 后若 3 行内含 NON_TARGET_INLINE，则丢弃该块
    final, i = [], 0
    while i < len(out):
        item = out[i]
        if isinstance(item, tuple) and item[0] == '__BLOCK__':
            look = ' '.join(str(x) for x in out[i + 1:i + 4] if isinstance(x, str))
            if NON_TARGET_INLINE.search(look):
                i += 1
                continue
            final.extend(item[1])
        else:
            final.append(item)
        i += 1
    return '\n'.join(str(x) for x in final)


def check_assembly(plan_text, mml_text, exp_text=''):
    """方案(配置分析md) vs mml.txt 的命令族一致性。

    返回 {'missing_in_mml': [...], 'extra_in_mml': [...], 'ok': bool}
    只比配置类 + 运行态，不比查询类。

    ⚠ 先剔除"非本网元执行"的章节（跨 NF 对照 / SMF 侧需同步），
      否则会把明确标注"不执行"的命令误判成装配丢失。
    """
    plan = parse_mml(_exclude_non_target(plan_text))
    gen = parse_mml(mml_text)
    pf, gf = _fams(plan), _fams(gen)

    # ★ 2026-10-30：删除类命令不算「装配丢失」。
    #   按 SKILL §4.11「三类删除需确认」，RMV/DEL 的对象是现网既有配置，
    #   生成侧**不得自行决定删除**，应进「待确认」段。
    #   实测 NC20260828000360 的 12 个「装配丢失」全是 RMV 类
    #   （RMV RULE / RMV URR / RMV USERPROFILE …），判成缺陷是口径错。
    _DEL_VERBS = ('RMV', 'DEL')
    missing = sorted(f for f in (pf - gf)
                     if f.split()[0] not in _DEL_VERBS)
    deleted_pending = sorted(f for f in (pf - gf)
                             if f.split()[0] in _DEL_VERBS)
    extra = sorted(gf - pf)

    # ★ 2026-10-30：plan 里有、mml 里没有，但 **EXP 里已存在** 的命令，
    #   属 V3「重复下发」管的范畴（不该再做），不算装配丢失。
    #   否则 V1 补齐时跳过它们（防死循环），C1 又会一直报缺 —— 两个判据打架。
    exp_fams = set()
    if exp_text:
        exp_fams = _fams(parse_mml(exp_text))
    if exp_fams:
        _pre_exp = [f for f in missing if f in exp_fams]
        missing = [f for f in missing if f not in exp_fams]
    else:
        _pre_exp = []

    return {'missing_in_mml': missing, 'extra_in_mml': extra,
            'preexisting_skipped': _pre_exp,
            # 删除类单列：需人工确认，不计入缺陷
            'deletion_pending': deleted_pending,
            'plan_fams': len(pf), 'mml_fams': len(gf),
            'ok': not missing and not extra}


# ══════════════════════════════════════════════════════════
# C2 引用完整性
# ══════════════════════════════════════════════════════════
def _defined_objects(cmds):
    """从 ADD 命令里收集"被创建的对象名"（按参数名分组）。

    ⚠ 关键区分：ADD 命令分两类，不能一律当"创建"
      · 创建型（CREATE）：参数少、无引用型依赖
            例 ADD L3VPNINST:VRFNAME="VRF_A", VRFDESCRIPTION="x"   ← 真创建 VRF_A
      · 从属型（DEPENDENT）：自身就引用了别的对象
            例 ADD VPNINSTAF:VRFNAME="VRF_B", AFTYPE=ipv4uni
               ← 它只是"给已存在的 VRF_B 加地址族"，**不创建 VRF_B**
      早期实现把从属型也算作创建，导致 ADD VPNINSTAF 里的 VRF_B
      被误认为"已定义"，悬空引用抓不出来（自测 T2 曾因此失效）。

    判据（不靠命令白名单）：
      一条 ADD 命令 C 若满足「它的引用型参数在【命令集里已有别处定义】
      或【本命令自身是唯一持有该值的 ADD】」——无法可靠判断，
      ⇒ 改为：**只有当某个引用值不是"从属型 ADD 的引用参数"时才算创建**。
      实用近似：把"参数个数 ≤ 2 且除主键外无其它引用型参数"当作创建型。
    """
    defined = defaultdict(set)
    for verb, cmd, params in cmds:
        if verb != 'ADD':
            continue
        ref_params = [(k, v) for k, v in params.items() if REF_PARAM_SUFFIX.search(k)]
        non_ref_params = [k for k in params if not REF_PARAM_SUFFIX.search(k)]
        # 从属型判定：有引用型参数 **且** 还有别的"非引用型业务参数"
        #   ADD L3VPNINST:  VRFNAME(ref) + VRFDESCRIPTION(non-ref)  → 参数少，是创建
        #   ADD VPNINSTAF:  VRFNAME(ref) + AFTYPE(non-ref)          → 也是该形态
        # 两者形态相同，无法靠参数形态区分 ⇒ 用命令级登记表（见 CREATOR_CMDS）
        if cmd.upper() in DEPENDENT_CMDS:
            continue
        for k, v in ref_params:
            defined[k.upper()].add(_key_of(v))
    return defined


# 从属型命令：从 YAML 读取（数据外置，见 rules/dependent_add_cmds.yaml）
# 缺失文件时退化为空集 = 全部 ADD 当创建型（宁可漏报悬空，不误报）
def _load_dependent():
    import os
    for cand in [
        os.environ.get('EXP_DEPENDENT_YAML'),
        '/opt/expgv/rules/dependent_add_cmds.yaml',
        os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                     'rules', 'dependent_add_cmds.yaml'),
    ]:
        if not cand or not os.path.exists(cand):
            continue
        try:
            import yaml
            d = yaml.safe_load(open(cand, encoding='utf-8')) or {}
            return {str(x).upper() for x in (d.get('dependent') or [])}
        except Exception:
            pass
    return set()


DEPENDENT_CMDS = _load_dependent()


def _referenced_objects(cmds, include_rmv=False):
    """从命令里收集"被引用的对象名"。

    ⚠ **默认排除 RMV/DEL**：删除命令的对象是"现网已有的东西"，
      本来就**不需要本方案定义它**。若把 RMV 的参数当引用，
      实测会把 100 条正常删除命令全判成悬空
      （NC20260803001614：RMV FLTBINDFLOWF 等，对象在 EXP 里存在、方案里不该重复定义）。

    同理 MOD/SET 引用已有对象也属正常，但它们通常作用于本方案或 EXP 已建对象，
    保留检查（能抓"改了不存在的对象"）。
    """
    refs = []
    for verb, cmd, params in cmds:
        if not include_rmv and verb in ('RMV', 'DEL'):
            continue
        for k, v in params.items():
            if not REF_PARAM_SUFFIX.search(k):
                continue
            val = _key_of(v)
            if not val or _NOT_REF_VALUE.match(val) or val.startswith('<'):
                continue      # 占位符/枚举/IP/数字 不算引用
            refs.append((verb, cmd, k.upper(), val))
    return refs


def check_references(mml_text, exp_text=''):
    """引用完整性：被引用的对象必须有定义（本方案 ADD 或 EXP ADD）。

    返回 {'dangling': [(cmd, param, value), ...], 'ok': bool}
    """
    gen = parse_mml(mml_text)
    exp = parse_mml(exp_text)

    defined = _defined_objects(gen)
    for k, vs in _defined_objects(exp).items():
        defined[k] |= vs

    dangling = []
    seen = set()
    for verb, cmd, k, val in _referenced_objects(gen):
        if val in defined.get(k, ()):
            continue
        key = (cmd, k, val)
        if key in seen:
            continue
        seen.add(key)
        dangling.append({'cmd': cmd, 'param': k, 'value': val,
                         'verb': verb})

    # 按"引用该值的命令条数"排序（影响面大的在前）
    # ⚠ 同一对象会被多条不同命令引用（如 VRF_B 被 VPNINSTAF/IPBINDVPN/SRROUTE 各引一次）
    #   所以要按 **对象值** 分组统计，不能按 (cmd,param,value) —— 那只会数到 1。
    ref_counts = defaultdict(int)
    for verb, cmd, k, val in _referenced_objects(gen):
        ref_counts[val] += 1
    for d in dangling:
        d['ref_count'] = ref_counts[d['value']]
    dangling.sort(key=lambda x: -x['ref_count'])

    return {'dangling': dangling, 'ok': not dangling,
            'n_defs': sum(len(v) for v in defined.values())}


# ══════════════════════════════════════════════════════════
# C3 重复下发
# ══════════════════════════════════════════════════════════
def _cmd_sig(verb, cmd, params):
    """命令签名：verb + cmd + 全部参数（键值归一化）。"""
    return (verb, cmd, tuple(sorted((k.upper(), _key_of(v)) for k, v in params.items())))


# ── 重复下发的判定边界（用户裁决 2026-10-30，修正 10-29 版）──
# 用户原话：「重复下发还有重复的 set，只有 set refreshsrv 是例外」
#
# 语义依据：
#   ADD  —— 「创建对象」。对象已存在时再执行会报"已存在"，**属真重复**
#   SET  —— 「设为此值」。**重复下发算缺陷**（改的是同一对象同一值，
#           说明方案没识别出"现网已是目标态"，属重复动作）
#           · **唯一例外：SET REFRESHSRV** —— 业务配置后刷新使之生效，
#             是流程收尾动作，不能因为 EXP 里发过就跳过
#   MOD  —— 改属性，与 SET 同理，**重复算缺陷**
#   RMV/DEL —— 删不存在对象会报错，但不该由本判据管（见 C2 说明）
#
# ⇒ C3 判所有动词的完全相同命令，唯一豁免 SET REFRESHSRV。
#   （10-29 版曾把全部 SET/MOD 豁免，导致 01614 的 26 条重复 SET 全部漏报）
DUPLICATE_EXEMPT_CMDS = ('REFRESHSRV',)     # SET REFRESHSRV 例外
IDEMPOTENT_VERBS = ()                        # 已取消"整体豁免"


def check_duplicate(mml_text, exp_text, plan_fams=None):
    """重复下发：生成里与 EXP 完全相同的命令（唯一豁免 SET REFRESHSRV）。

    返回 {'duplicates': [...], 'ok': bool, 'idempotent_skipped': n,
          'plan_required_kept': n}

    ⚠ 判定口径（用户裁决 2026-10-30）：
       重复的 SET/MOD **也算重复下发**（方案没识别"现网已是目标态"）。
       唯一例外 SET REFRESHSRV —— 业务配置后的刷新动作，EXP 里发过仍需再发。

    ★ 2026-10-30（V3-M2）：若命令族在**方案里明确要求**（plan_fams 内有），
      则即使 EXP 里已有也不算"重复下发"，而是"方案本来就要做的动作"。
      背景：V8 从 EXP 同族模板补全后，这些命令天然与 EXP 同签名；
            若仍判重复，V3 会删、V8 会补，闭环永不收敛。
      实测冲突：selftest_bugfix_4 的 Bug1-1，V8 补 ADD APN 后 C3 判残留 1。
    """
    _plan = {f.upper() for f in (plan_fams or set())}
    gen = parse_mml(mml_text)
    exp = parse_mml(exp_text)
    exp_sigs = {_cmd_sig(*c) for c in exp}

    dup = []
    seen = set()
    skipped = 0
    plan_kept = 0
    for verb, cmd, params in gen:
        sig = _cmd_sig(verb, cmd, params)
        if sig not in exp_sigs:
            continue
        # 唯一豁免：SET REFRESHSRV（业务配置后刷新生效，属流程收尾动作）
        if str(cmd).upper() in DUPLICATE_EXEMPT_CMDS:
            skipped += 1
            continue
        # 方案明确要求的族 → 不算重复下发（V3-M2）
        if _plan and f'{verb} {cmd}'.upper() in _plan:
            plan_kept += 1
            continue
        if sig in seen:
            continue
        seen.add(sig)
        dup.append({'verb': verb, 'cmd': cmd,
                    'key': _first_ref_param(params)})
    return {'duplicates': dup, 'ok': not dup,
            'idempotent_skipped': skipped, 'plan_required_kept': plan_kept}


def _first_ref_param(params):
    """取一个能标识该命令对象的参数值，用于展示。"""
    for k, v in params.items():
        if REF_PARAM_SUFFIX.search(k) and not _NOT_REF_VALUE.match(_key_of(v)):
            return f'{k}={v}'
    for k, v in list(params.items())[:2]:
        return f'{k}={v}'
    return ''




# ── C4 前置：过滤非配置步骤 ──
# 实测：意图操作脚本里混有「备份/观察/验证」步骤，它们也含命令，但不是本次要下发的配置。
#   NC20260907000242 步骤20「操作后指标观察」含 RMV 36 条 → GT 不做
#   NC20260908000848 步骤10「备份网元配置」含 RMV 93 条 → GT 不做
# 不过滤会把这类误判成"批量展开不足"（6 个工单里 4 个是误报）。
NON_CONFIG_STEP_KEYWORDS = [
    '备份', '观察', '验证', '检查', '确认', '回退', '倒回', 'rollback',
    '指标', '知会', '分工', '准备', '入场', '登录',
    # ★ 2026-10-29 补：实测「查看订阅指标」步骤含大量 DSP 查询 + RMV，
    #   是运维查询不是配置操作（NC20260803000197 步骤5 RMV 16 条、
    #   NC20260806001514 步骤6 RMV 6 条），漏了会把查询当配置任务。
    '查看', '订阅', '监控', '巡检', '测试', 'ping',
]


def _config_only_steps(text):
    """只保留"配置类"步骤的命令文本。

    按 `// ======== 步骤N: 名称 ========` 切分，丢弃名称含非配置关键词的步骤。
    没有步骤标记时原样返回。
    """
    parts = re.split(r'\n\s*//\s*={3,}\s*([^=]+?)\s*={3,}', text or '')
    if len(parts) < 3:
        return text or ''
    kept = []
    for i in range(1, len(parts), 2):
        name = parts[i].strip().lower()
        body = parts[i + 1] if i + 1 < len(parts) else ''
        if any(k in name for k in NON_CONFIG_STEP_KEYWORDS):
            continue
        kept.append(body)
    return '\n'.join(kept) if kept else ''

# ══════════════════════════════════════════════════════════
# C4 批量展开覆盖（新增 2026-10-29）
# ══════════════════════════════════════════════════════════
# 问题背景（实测）：
#   意图操作脚本给出 33 个 LoopBack 接口（loopback1060~1092），
#   GT 做 33 个，但生成侧有时只做 1 个、有时做 33 个。
#   ⇒ 族（做什么）稳定，实例数（做几个）不稳定且常不足。
#
# 判据基准：意图操作脚本里「同一命令族 + 同一主键参数」的实例集合（去重）。
#   实测 NC20260811002152：意图去重 33 个 = GT 33 个，交集 33（完全吻合）
#   ⚠ 必须去重：同一批接口会在「割接」「迁回」两个步骤各出现一次（66→33）
#
# 为什么不用命令条数：66 条 ≠ 66 个实例，是 33 个 × 2 个阶段。

# 实例型主键参数（该参数的值唯一标识一个对象实例）
INSTANCE_KEY_PARAMS = [
    'IFNAME', 'VRFNAME', 'APN', 'POOLNAME', 'SECTIONNAME', 'GROUPNAME',
    'PROFILENAME', 'POLICYNAME', 'RULENAME', 'SERVERNAME', 'HOSTNAME',
    'TEMPLATENAME', 'AREANAME', 'L3VPNNAME', 'DNN', 'SNSSAINAME',
]


def extract_instances(text):
    """从 MML 文本提取 {命令族: {主键值, ...}}。

    只收「有实例型主键」的命令，且主键值不是占位符/枚举。
    """
    out = defaultdict(set)
    for verb, cmd, params in parse_mml(text):
        if verb == 'QUERY':
            continue
        key_p = None
        key_v = None
        for kp in INSTANCE_KEY_PARAMS:
            if kp in params:
                v = _key_of(params[kp])
                if v and not _NOT_REF_VALUE.match(v):
                    key_p, key_v = kp, v
                    break
        if not key_p:
            continue
        out[f'{verb} {cmd}'].add(key_v)
    return out


def check_batch_coverage(intent_text, mml_text, min_ratio=0.8, min_instances=2):
    """批量展开覆盖：意图操作脚本里的实例，生成侧覆盖了多少。

    Args:
        intent_text: 工单 md（含操作脚本）
        mml_text:    生成的 mml.txt
        min_ratio:   覆盖率阈值（低于则告警）
        min_instances: 意图里该族实例数 ≥ 此值才判（单实例谈不上"批量"）

    返回 {
      'under_covered': [{'family','need','got','missing_n','missing','ratio'}],
      'ok': bool,
      'checked': 检查过的族数,
    }
    """
    # 只取配置类步骤（排除备份/观察/验证步骤，实测 4/6 误报来自此）
    intent_cfg = _config_only_steps(intent_text)
    want = extract_instances(intent_cfg)
    got = extract_instances(mml_text)

    under = []
    checked = 0
    for fam, vals in want.items():
        if len(vals) < min_instances:
            continue          # 单实例不判批量
        checked += 1
        have = got.get(fam, set())
        miss = vals - have
        if not miss:
            continue
        ratio = len(vals & have) / len(vals)
        if ratio >= min_ratio:
            continue          # 覆盖达标（允许少量缺失）
        under.append({
            'family': fam,
            'need': len(vals),
            'got': len(vals & have),
            'missing_n': len(miss),
            'missing': sorted(miss)[:10],
            'ratio': round(ratio, 3),
        })

    under.sort(key=lambda x: x['ratio'])
    return {'under_covered': under, 'ok': not under, 'checked': checked}

# ══════════════════════════════════════════════════════════
# 汇总
# ══════════════════════════════════════════════════════════


# ══════════════════════════════════════════════════════════
# G11 批量主键唯一性
# ══════════════════════════════════════════════════════════
# 背景（2026-10-30 实测事故 NC20260907000688）：
#   agent 在方案 md 里用模板 `supere5<TIER>_<APP>_live` 表达 33 条业务规则，
#   装配时 <TIER>/<APP> 未按条具体化，34 条 ADD RULE 的 RULENAME 全部
#   变成同一个值 → 34 条 RULEBINDING 里 33 条引用不存在的 RULENAME。
#   G1（装配）/G3（重复）/G4（批量数量）全部通过，没人发现。
#
#   根因：**没有任何判据在检查"批量展开时主键是否各不相同"**。
#
# 判据：
#   对产物里每个 ADD 类命令族：
#     命令条数 >= min_count（默认 5）
#     且 主键唯一值数 / 命令条数 < min_ratio（默认 0.5）
#   → 报「疑似批量展开主键未递增」
#
# 为什么不查 SET/MOD：SET 类多为全局开关，多实例同主键是合法的
#   （如 SET APN*ATTR 按 APN 分组，同名不同参数）。

# 真正的「对象定义」主键（优先用这些判定唯一性）
# 不在表里的（如 FLOWFILTERNAME 在 RULE 里是共享引用）不参与唯一性判定
def _kp_cache():
    return _KP_CACHE if '_KP_CACHE' in globals() else None


_KP_CACHE = None


def _load_key_params(path=None):
    """主键参数表（数据外置到 rules/key_params.yaml）。

    ★ 2026-10-31：原表硬编码在代码里且分散 4 处、内容重复不一致
      （agent_projection.KEY_PARAMS ×2 / _PRIMARY_FIRST、gen_selfcheck 的
      G11_KEY_PARAMS / G11_PRIMARY_KEY_PARAMS），改一处忘另一处 ——
      这是批量展开反复出错的结构性原因。
      现统一从 YAML 加载，object_key 在前（对象定义型），ref_key 在后（引用型）。
    """
    global _KP_CACHE
    if _KP_CACHE is not None:
        return _KP_CACHE
    import os
    if path is None:
        try:
            path = _rules_path('key_params.yaml')
        except NameError:
            path = '/opt/expgv/rules/key_params.yaml'
    try:
        import yaml
        with open(path, encoding='utf-8') as f:
            d = yaml.safe_load(f) or {}
        obj = [str(x).upper() for x in (d.get('object_key') or [])]
        ref = [str(x).upper() for x in (d.get('ref_key') or [])]
        _KP_CACHE = {'object_key': obj, 'ref_key': ref, 'all': obj + ref}
    except Exception:
        _KP_CACHE = {'object_key': [], 'ref_key': [], 'all': []}
    return _KP_CACHE


G11_PRIMARY_KEY_PARAMS = tuple(_load_key_params()['object_key'])

G11_KEY_PARAMS = tuple(_load_key_params()['all'])


def _key_of_cmd(params):
    """取一条命令的主键值（按 G11_KEY_PARAMS 顺序，取第一个命中的）"""
    for kp in G11_KEY_PARAMS:
        if kp in params:
            return kp, _key_of(params[kp])
    return None, None




# ══════════════════════════════════════════════════════════
# G11 批量主键唯一性（用命令文档的「唯一标识」标注，不猜）
# ══════════════════════════════════════════════════════════
# 背景（2026-10-30 实测事故 NC20260907000688）：
#   agent 用模板 supere5<TIER>_<APP>_live 表达 33 条规则，
#   装配时占位符未逐条具体化 → 34 条 ADD RULE 的 RULENAME 全部相同
#   → 33 条 RULEBINDING 引用悬空。G1/G3/G4 全过，无人发现。
#
# 判据来源（权威）：
#   命令文档的「配置原则」明写：
#     ADD RULE：'规则名称'+'策略类型' 唯一标识一条 rule，不同 rule 之间不能重复
#   → 由 build_unique_key_map 从 103 个文档建表 89 个族（cmd_unique_keys.json）
#
# 为什么不能靠「参数位置」或「参数名白名单」猜主键（前 4 版教训）：
#   ADD RULE:RULENAME=...            首参可能是 POLICYTYPE（枚举，全部相同）
#   ADD IPBINDVPN:IFNAME=..,VRFNAME=..  VRFNAME 是共享引用，不是主键
#   ADD POOLGRPMAP:MAPPINGNAME=..,APN=..  APN 是共享引用
#   同一参数名在不同族里，有时是主键有时是引用 —— 猜不出来。
#
# 判据：
#   · 只查 cmd_unique_keys.json 里有的族（文档明确标注了唯一标识）
#   · 按表中参数组合算唯一性：N 条命令 / M 个不同组合值
#   · N >= min_count 且 M/N < min_ratio → 报重复
#   · 表里没有的族 → skip（不猜，避免误报）

_UNIQUE_MAP_CACHE = None


def _load_unique_map(path=None):
    global _UNIQUE_MAP_CACHE
    if _UNIQUE_MAP_CACHE is not None:
        return _UNIQUE_MAP_CACHE
    import json as _json
    import os
    path = path or _rules_path('cmd_unique_keys.json')
    if not os.path.isfile(path):
        _UNIQUE_MAP_CACHE = {}
        return {}
    try:
        with open(path, encoding='utf-8') as f:
            _UNIQUE_MAP_CACHE = {k.upper(): [x.upper() for x in v]
                                 for k, v in _json.load(f).items()}
    except Exception:
        _UNIQUE_MAP_CACHE = {}
    return _UNIQUE_MAP_CACHE


# ══════════════════════════════════════════════════════════
# G12 参数格式一致性（V3 线 2）
# ══════════════════════════════════════════════════════════
# 背景（实测 SET SOFTPARAOFBIT）：
#   UDG 文档：DT2=BYTE / BYTENUM / BYTEPOSITION / BYTEVALUE
#   设备实际：DT=DWORD_EX / PARANUM / POSITION / VALUE
#   照文档配出来的命令设备不认 —— 而产物看起来完全正常。
#
# 判据：文档参数名 与 EXP 同族参数名 **交集为空** → 格式可能过时。
# 取舍：EXP 是现网在跑的配置，最可信；文档可能是旧版本。

_PARAM_FMT_CACHE = None


def _load_param_fmt_rules(path=None):
    global _PARAM_FMT_CACHE
    if _PARAM_FMT_CACHE is not None:
        return _PARAM_FMT_CACHE
    import os
    path = path or _rules_path('param_format_priority.yaml')
    if not os.path.isfile(path):
        _PARAM_FMT_CACHE = {'known_mismatch': {}, 'min_exp_samples': 1}
        return _PARAM_FMT_CACHE
    try:
        import yaml
        with open(path, encoding='utf-8') as f:
            d = yaml.safe_load(f) or {}
        km = {}
        for it in (d.get('known_mismatch') or []):
            fam = (it.get('fam') or '').upper()
            if fam:
                km[fam] = {
                    'doc_params': [x.upper() for x in (it.get('doc_params') or [])],
                    'exp_params': [x.upper() for x in (it.get('exp_params') or [])],
                    'note': (it.get('note') or '').strip(),
                }
        _PARAM_FMT_CACHE = {
            'known_mismatch': km,
            'min_exp_samples': ((d.get('mismatch_rule') or {}).get('min_exp_samples') or 1),
        }
    except Exception:
        _PARAM_FMT_CACHE = {'known_mismatch': {}, 'min_exp_samples': 1}
    return _PARAM_FMT_CACHE


def check_param_format(mml_text, exp_text=''):
    """G12：产物里命令的参数名 与 EXP 同族参数名是否一致。

    返回 {'suspect': [...], 'ok': bool, 'n_checked': N, 'n_with_exp': M}
    """
    rules = _load_param_fmt_rules()
    known = rules['known_mismatch']

    prod = {}
    for verb, cmd, params in parse_mml(mml_text):
        fam = (verb + ' ' + cmd).upper()
        prod.setdefault(fam, set()).update(k.upper() for k in params)

    expf = {}
    if exp_text:
        for verb, cmd, params in parse_mml(exp_text):
            if str(verb).upper() != 'ADD':
                continue
            fam = (verb + ' ' + cmd).upper()
            expf.setdefault(fam, set()).update(k.upper() for k in params)

    suspect = []
    for fam, pparams in prod.items():
        k = known.get(fam)
        if k:
            # ★ 只有产物用了**文档那套参数名**才报
            #   （否则用现网正确参数名配的产物会被误报，自测 ② 曾因此失败）
            known_doc_hit = pparams & set(k['doc_params'])
            if known_doc_hit:
                suspect.append({
                    'family': fam,
                    'mml_params': sorted(pparams)[:8],
                    'exp_params': k['exp_params'][:8],
                    'reason': ('已知格式不符：文档用 ' + '/'.join(k['doc_params'][:4]) +
                               '，现网用 ' + '/'.join(k['exp_params'][:4]) +
                               '；本产物用了 ' + '/'.join(sorted(known_doc_hit)[:4])),
                })
            continue
        eparams = expf.get(fam)
        if not eparams:
            continue
        if not (pparams & eparams):
            suspect.append({
                'family': fam,
                'mml_params': sorted(pparams)[:8],
                'exp_params': sorted(eparams)[:8],
                'reason': ('产物参数名与 EXP 同族参数名无交集（产物 ' +
                           str(len(pparams)) + ' 个，EXP ' + str(len(eparams)) + ' 个）'),
            })

    return {'suspect': suspect, 'ok': not suspect,
            'n_checked': len(prod), 'n_with_exp': len(expf)}


# ══════════════════════════════════════════════════════════
# G7 意图点名覆盖
# ══════════════════════════════════════════════════════════
# 背景（实测 61 族次）：
#   「意图段提了，但配置分析 md 里也没写」——
#   G1 比的是「md 有 vs mml 没有」，md 本身没写就无从比，这类缺口 G1 抓不到。
#
# 取舍（重要）：
#   中文名→命令族映射不唯一（"紧急呼叫配置"可能是 EMGCFG/SMFEMGCFG/NGEMGCFG）。
#   匹配不上就落到「需人工确认」，**不硬判缺失**。
#   宁可少报，也不制造假缺口 —— V1 曾把 MME 的命令当 UPF 缺失误报 66 族次。

_INTENT_MAP_CACHE = None
_RE_DOT = chr(92) + 'u3002'          # 中文句号，避免转义问题
_RE_INTENT_NAMED = None
_RE_VERB_PREFIX = None
_RE_ETC = None


def _intent_regexes():
    global _RE_INTENT_NAMED, _RE_VERB_PREFIX, _RE_ETC
    if _RE_INTENT_NAMED is None:
        import re as _re
        # ★ 2026-10-30 修：捕获段要在「，。/；」处截断。
        #   误报实证（NC20260911002023）意图写：
        #     "本次变更（业务开通）：新增 URR计费规则等12项，调整 URR组绑定等2项。"
        #   「调整 URR组绑定」和「新增...」在同一行，
        #   旧正则 [^\n。]{2,120} 会一路吃到行尾 ⇒ 把调整项并进新增项。
        _RE_INTENT_NAMED = _re.compile(
            '(?:新增|增加|修改|调整|删除|去掉)[：: ]*([^' + chr(10) + _RE_DOT +
            chr(65292) + chr(65307) + ']{2,120})')
        _RE_VERB_PREFIX = _re.compile('^(?:新增|增加|修改|调整|删除|去掉)' + chr(92) + 's*')
        _RE_ETC = _re.compile('等[0-9]+项')
    return _RE_INTENT_NAMED, _RE_VERB_PREFIX, _RE_ETC


_RULES_DIRS = ('/opt/expgv/rules', None)   # None 表示「与本文件同级的 ../rules」


def _rules_path(name, default='/opt/expgv/rules'):
    """规则文件路径：兼容容器内 /opt/expgv/rules 与宿主机 <repo>/rules。"""
    import os
    for base in _RULES_DIRS:
        if base is None:
            base = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rules')
        p = os.path.join(base, name)
        if os.path.isfile(p):
            return p
    return os.path.join(default, name)


def _load_intent_object_map(path=None):
    global _INTENT_MAP_CACHE
    if _INTENT_MAP_CACHE is not None:
        return _INTENT_MAP_CACHE
    import os
    path = path or _rules_path('intent_object_map.yaml')
    if not os.path.isfile(path):
        _INTENT_MAP_CACHE = {}
        return {}
    try:
        import yaml
        with open(path, encoding='utf-8') as f:
            d = yaml.safe_load(f) or {}
        _INTENT_MAP_CACHE = {
            (k or '').strip(): [x.upper() for x in (v or [])]
            for k, v in (d.get('object_zh') or {}).items()
        }
    except Exception:
        _INTENT_MAP_CACHE = {}
    return _INTENT_MAP_CACHE


def _intent_head(intent_text):
    """取意图的「变更意图 / 小意图拆解」段（不含操作脚本）"""
    t = intent_text or ''
    for sep in ('## 操作脚本', '// 操作脚本', '## 命令清单'):
        i = t.find(sep)
        if i > 0:
            t = t[:i]
            break
    return t


def check_intent_coverage(intent_text, mml_text, object_map=None):
    """G7：意图点名的对象，产物里有没有对应命令族。

    返回 {'named', 'covered', 'missing', 'unmappable', 'ok', ...}
      missing    意图点名 + 映射到命令族 + 产物没有 → 真缺口
      unmappable 意图点名但映射不到命令族 → 需人工确认（不算缺口）
    """
    import re as _re
    om = object_map if object_map is not None else _load_intent_object_map()
    head = _intent_head(intent_text)
    pat_named, pat_verb, pat_etc = _intent_regexes()

    fams = set()
    for verb, cmd, params in parse_mml(mml_text):
        fams.add((verb + ' ' + cmd).upper())

    named = []
    for m in pat_named.finditer(head):
        # ★ 2026-10-30 修：只查「新增」项。
        #   误报实证（NC20260828000360）：意图写
        #     "4. 删除 UPBINDUPG、USRPROFGROUP、规则绑定、用户签约模板、规则、PCC策略组等8项"
        #   旧实现把「删除」项也当"必须有"，报 5 处假缺失；
        #   另有「调整 License开关」被当缺失（调整项本来就可能在产物里只改不建）。
        #   ⇒ 只有「新增」要求产物里有该命令族；调整/修改/删除都不查。
        verb = m.group(0)[:2]
        if not verb.startswith('新增') and not verb.startswith('增加'):
            continue
        seg = pat_etc.sub('', m.group(1))
        for part in _re.split('[、,，/]', seg):
            p = part.strip().strip('。；;')
            p = pat_verb.sub('', p).strip()
            if 2 <= len(p) <= 30:
                named.append(p)
    named = list(dict.fromkeys(named))

    covered, missing, unmappable = [], [], []
    for n in named:
        cands = om.get(n)
        if not cands:
            unmappable.append(n)
            continue
        hit = [c for c in cands if c in fams]
        if hit:
            covered.append({'name': n, 'family': hit[0]})
        else:
            missing.append({'name': n, 'expect_families': cands})

    return {'named': named, 'covered': covered, 'missing': missing,
            'unmappable': unmappable, 'ok': not missing,
            'n_named': len(named), 'n_missing': len(missing),
            'n_unmappable': len(unmappable)}


# ══════════════════════════════════════════════════════════
# G13 意图 vs 方案 命令数量级对比
# ══════════════════════════════════════════════════════════
# 背景（实测 NC20260806001780）：
#   意图脚本 1319 条命令，agent 写的方案 md 只有 8 条（0.6%）。
#   现有判据全部通过（G1 比「方案 vs 产物」，方案本身只有 8 条就自洽了），
#   没有人发现「agent 把 1319 条意图压缩成了 8 条」。
#
# 判据：
#   统计意图里配置类命令的条数 vs 方案 md 里的条数，
#   若方案 < 意图的 min_ratio（默认 30%）且意图条数 >= min_base（默认 30）
#   → 报「方案命令数远少于意图」
#
# 为什么用条数比而不是族比：
#   族比抓不到「同样 8 个族，但每个族只写 1 条而意图有几百条」的情况
#   （NC20260805000498 的 POOLGRPMAP：族在，但 253 条只写了 6 条）。

_G13_RE = None


def _g13_regex():
    global _G13_RE
    if _G13_RE is None:
        import re as _re
        _G13_RE = _re.compile(
            '^(ADD|MOD|SET|RMV|DEL|DEA|LCK|ULK|ACT|STP)[ \t]+([A-Z][A-Z0-9_]*)',
            _re.M)
    return _G13_RE


def _intent_ops_section(intent_text):
    """只取意图的「## 操作脚本」段（排除回退脚本）。

    ★ 2026-10-31 修（G13 阈值失真根因）：
      意图 md 结构是：
        ## 变更意图 / ## 小意图拆解 / ## 操作脚本（本次要做的）
        ## 回退脚本（失败倒回用的，约占 40~86%）
      实测：
        NC20260805000498: 全文 5220 条 = 操作脚本 747 + 回退 4473（回退 86%）
        NC20260806001780: 全文 1319 条 = 操作脚本 768 + 回退 551（回退 42%）
        NC20260823000103: 全文 2287 条 = 操作脚本 1155 + 回退 1132（回退 49%）
      而操作脚本条数与 GT 配置类条数**完全一致**（747/768/1155）。
      ⇒ 只统计操作脚本段，否则方案永远显得"只做了 2%"。
    """
    import re as _re
    t = intent_text or ''
    m = _re.search(r'##\s*操作脚本\s*\n(.*?)(?=\n##\s*回退脚本|\n##\s*[^\n]+\n|\Z)', t, _re.S)
    if m:
        return m.group(1)
    # 没有显式分节：截断回退脚本
    m2 = _re.search(r'//\s*回退脚本|##\s*回退脚本', t)
    return t[:m2.start()] if m2 else t


def check_intent_volume(intent_text, target_text, min_ratio=0.30, min_base=30,
                        target_name='产物'):
    """G13：产物（或方案 md）的命令条数是否远少于意图操作脚本。

    ★ 2026-10-31 修（比错层面）：
      原实现比的是「意图 vs 方案 md」。但装配时 backfill_batch_from_intent 会
      从意图补齐缺失实例，所以**方案 md 少不代表最终产物少**。
      实测 NC20260805000498：方案 130 条，产物 764 条（意图 747 条）。
      若比方案 → 报 17.4%（误报）；比产物 → 103%（正常）。
      ⇒ 默认改成在**产物层面**比。

    返回 {'intent_cmds', 'target_cmds', 'ratio', 'ok', 'why', 'target'}
    """
    pat = _g13_regex()
    ops = _intent_ops_section(intent_text)
    n_intent = len(pat.findall(ops))
    n_plan = len(pat.findall(target_text or ''))

    ratio = (n_plan / n_intent) if n_intent else 1.0
    ok = True
    why = ''
    if n_intent >= min_base and ratio < min_ratio:
        ok = False
        why = (f'意图操作脚本 {n_intent} 条配置命令，{target_name}只有 {n_plan} 条'
               f'（{ratio:.1%} < {min_ratio:.0%}）—— 疑似大幅压缩意图')
    return {'intent_cmds': n_intent, 'target_cmds': n_plan,
            'ratio': round(ratio, 4), 'ok': ok, 'why': why,
            'target': target_name}


# ══════════════════════════════════════════════════════════
# G14 命名双层后缀异常
# ══════════════════════════════════════════════════════════
# 背景（实测 NC20260803001614）：
#   GT   命名：gdgzzhgldiot_00_f_006 / _007 / _008（单层序号）
#   产物命名：gdgzzhgldiot_00_f_055_001 / _002 / _003（双层序号）
#   ⇒ agent 在已有完整名字后又追加了一层序号，命名规律错乱。
#
# 注意：**不能只看"有没有 _NNN 后缀"**——
#   GT 自己就有 61 个带 _NNN 的名字（如 sos_sig_f_001），那是正常的。
#   异常判据是「同一族里，同一前缀下出现**两层**序号」。
#
# 判据：
#   对每个命令族的主键值，提取"去掉末尾 _NNN 后的前缀"。
#   若某前缀本身就以 _NNN 结尾（即出现 xxx_NNN_NNN）→ 双层后缀 → 报异常。
#
# 例：
#   gdgzzhgldiot_00_f_006      前缀 gdgzzhgldiot_00_f      ✅ 单层
#   gdgzzhgldiot_00_f_055_001  前缀 gdgzzhgldiot_00_f_055  ❌ 前缀仍带 _055

_G14_SUFFIX = None


def _g14_regex():
    global _G14_SUFFIX
    if _G14_SUFFIX is None:
        import re as _re
        _G14_SUFFIX = _re.compile('^(.*)_([0-9]{2,4})$')
    return _G14_SUFFIX


def check_double_suffix(mml_text, max_show=10):
    """G14：主键命名出现双层序号（xxx_NNN_NNN）。

    返回 {'suspect': [{family, key, value, prefix, n}], 'ok': bool}
    """
    pat = _g14_regex()
    from collections import Counter

    hits = {}
    for verb, cmd, params in parse_mml(mml_text or ''):
        if str(verb).upper() not in ('ADD', 'MOD', 'SET'):
            continue
        fam = '%s %s' % (verb, cmd)
        for k, v in params.items():
            sv = str(v or '')
            m = pat.match(sv)
            if not m:
                continue
            prefix = m.group(1)
            # 前缀本身以 _NNN 结尾 → 双层
            m2 = pat.match(prefix)
            if m2 and len(m2.group(2)) >= 2:
                key = (fam, k)
                hits.setdefault(key, []).append(sv)

    suspect = []
    for (fam, k), vals in hits.items():
        uniq = sorted(set(vals))
        suspect.append({
            'family': fam, 'key': k, 'n': len(uniq),
            'value': uniq[0] if uniq else '',
            'samples': uniq[:max_show],
        })

    suspect.sort(key=lambda x: -x['n'])
    return {'suspect': suspect, 'ok': not suspect,
            'n_groups': len(suspect),
            'n_values': sum(x['n'] for x in suspect)}




def check_key_uniqueness(mml_text, min_count=5, min_ratio=0.5, plan_fams=None,
                         unique_map=None):
    """G11：按文档标注的唯一标识检查批量命令。

    返回 {'groups': [...], 'suspect': [...], 'ok': bool, 'skipped_fams': [...]}
    """
    umap = unique_map if unique_map is not None else _load_unique_map()
    _plan = {f.upper() for f in (plan_fams or set())}

    # fam -> [(tuple(唯一标识值), 命令序号)]
    fams = {}
    for verb, cmd, params in parse_mml(mml_text):
        if str(verb).upper() != 'ADD':
            continue
        fam = f'{verb} {cmd}'.upper()
        if fam not in umap:
            fams.setdefault(fam, [])
            continue                      # 该族文档没标注唯一标识 → 只计数
        keys = umap[fam]
        vals = []
        for k in keys:
            if k in params:
                vals.append(_key_of(params[k]))
            else:
                vals.append('')           # 缺该参数 → 空，会被算成不同的组合
        fams.setdefault(fam, []).append(tuple(vals))

    groups, suspect, skipped = [], [], []
    for fam, combos in sorted(fams.items()):
        n = len(combos)
        keys = umap.get(fam)
        if not keys:
            skipped.append(fam)
            continue
        if n < min_count:
            groups.append({'family': fam, 'n_cmds': n, 'n_uniq': n,
                           'ratio': 1.0, 'key_params': keys, 'verdict': 'skip',
                           'why': f'条数 {n} < {min_count}'})
            continue
        uniq = len(set(combos))
        ratio = uniq / max(1, n)
        base = {'family': fam, 'n_cmds': n, 'n_uniq': uniq,
                'ratio': round(ratio, 3), 'key_params': keys}
        if ratio < min_ratio:
            g = {**base, 'verdict': 'duplicated',
                 'why': (f'{n} 条 {fam} 只有 {uniq} 个不同的'
                         f'（{"+".join(keys)}）组合，唯一率 {ratio:.0%} < {min_ratio:.0%}'),
                 'sample_value': '+'.join(sorted(set(combos))[0]) if combos else '',
                 'in_plan': fam in _plan if _plan else None}
            suspect.append(g)
            groups.append(g)
        else:
            groups.append({**base, 'verdict': 'ok'})

    return {'groups': groups, 'suspect': suspect, 'ok': not suspect,
            'skipped_fams': skipped, 'n_checked_fams': len(groups)}



def check_prior_fams_kept(prior_text, mml_text):
    """G16：revise 时本代是否保留了前代的命令族。

    prior_text: 前代 mml 全文（空串 = 首次生成，不判）
    mml_text:   本代 mml 全文

    返回 {'ok': bool, 'prior_fams': n, 'kept': n, 'lost': [族...], 'note': str}
    """
    if not (prior_text or '').strip():
        return {'ok': True, 'skipped': True, 'note': '首次生成，无前代可比'}

    import re as _re

    def fams(t):
        out = {}
        for m in _re.finditer(
                r'(?:^|\n)\s*(ADD|MOD|SET|RMV|DEL|LCK|DEA|ULK)\s+([A-Z][A-Z0-9_]*)\s*:',
                t or ''):
            k = '%s %s' % (m.group(1), m.group(2))
            out[k] = out.get(k, 0) + 1
        return out

    pf = fams(prior_text)
    cf = fams(mml_text)
    if not pf:
        return {'ok': True, 'skipped': True, 'note': '前代无命令，无可比'}

    # 前代里「纯新增类」的族（ADD/MOD/SET）必须保留；
    # 前代里的 RMV/DEL 族不要求保留（删除命令本身是一次性的）
    must = {k: v for k, v in pf.items() if k.split()[0] not in ('RMV', 'DEL')}
    lost = [k for k in must if k not in cf]
    kept = len(must) - len(lost)

    return {
        'ok': not lost,
        'prior_fams': len(must),
        'kept': kept,
        'lost': sorted(lost)[:20],
        'n_lost': len(lost),
        'note': ('前代 %d 个配置族，本代保留 %d 个' % (len(must), kept)
                 if not lost else
                 '前代 %d 个配置族，本代丢失 %d 个: %s' % (
                     len(must), len(lost), ', '.join(sorted(lost)[:5]))),
    }


def selfcheck(plan_text, mml_text, exp_text='', intent_text='',
              exp_filename='', gt_cmds=None, prior_mml=''):
    """跑全部校验，返回汇总 dict。

    V0 EXP 网元核对   —— EXP 是不是本工单网元（2026-10-30 新增）
    C1 装配一致       —— 方案 md 的族 vs mml 的族
    C2 引用完整       —— 被引用对象有创建者或 EXP 已存在
    C3 重复下发       —— 与 EXP 完全相同的命令（仅 SET REFRESHSRV 豁免）
    C4 批量完整       —— 意图实例清单 vs 产物实例
    V5 枚举一致       —— 同族同主键的参数值（命令+枚举值=独立单位）

    gt_cmds 传入时才跑 V5（离线复盘场景；生产链路无 GT）。
    """
    r = {
        'C1_assembly': check_assembly(plan_text, mml_text, exp_text),
        'C2_references': check_references(mml_text, exp_text),
        'C3_duplicate': check_duplicate(mml_text, exp_text),
    }
    if intent_text:
        r['C4_batch'] = check_batch_coverage(intent_text, mml_text)
    # ── G11：批量主键唯一性（不依赖 GT/EXP） ──
    try:
        r['G11_key_unique'] = check_key_uniqueness(mml_text)
    except Exception as _e:
        r['G11_error'] = f'{type(_e).__name__}: {_e}'
    # ── G12：参数格式一致性（需要 EXP）──
    try:
        r['G12_param_format'] = check_param_format(mml_text, exp_text or '')
    except Exception as _e:
        r['G12_error'] = f'{type(_e).__name__}: {_e}'
    # ── G7：意图点名覆盖 ──
    try:
        if intent_text:
            r['G7_intent_cover'] = check_intent_coverage(intent_text, mml_text)
    except Exception as _e:
        r['G7_error'] = f'{type(_e).__name__}: {_e}'
    # ── G13：意图 vs 方案 命令数量对比 ──
    try:
        if intent_text and mml_text:
            # ★ 2026-10-31 修：比**产物**（不是方案 md）。
            #   方案 md 会被 backfill 从意图补齐，方案少不代表产物少。
            #   实测 NC20260805000498：方案 130 条 → 产物 764 条（意图 747）。
            r['G13_intent_volume'] = check_intent_volume(
                intent_text, mml_text, target_name='产物')
    except Exception as _e:
        r['G13_error'] = f'{type(_e).__name__}: {_e}'
    # ── G14：命名双层后缀 ──
    try:
        r['G14_double_suffix'] = check_double_suffix(mml_text)
    except Exception as _e:
        r['G14_error'] = f'{type(_e).__name__}: {_e}'

    # ── V0：EXP 网元核对（不依赖 GT） ──
    try:
        import check_v0_v5 as _v
        if exp_filename:
            r['V0_exp_nf'] = _v.check_exp_nf(exp_filename, intent_text or '')
        if intent_text and exp_text:
            r['V0_entity_align'] = _v.check_exp_content_alignment(
                intent_text, exp_text)
    except Exception as _e:
        r['V0_error'] = f'{type(_e).__name__}: {_e}'

    # ── V5：枚举值一致性（需要 GT，离线用） ──
    if gt_cmds:
        try:
            import check_v0_v5 as _v2
            kps = ('IFNAME', 'VRFNAME', 'APN', 'POOLNAME', 'SECTIONNAME',
                   'GROUPNAME', 'PROFILENAME', 'POLICYNAME', 'RULENAME',
                   'FILTERNAME', 'FLOWFILTERNAME', 'USERPROFILENAME',
                   'VPNINSTANCE', 'LICITEM', 'DNN')
            r['V5_params'] = _v2.check_enum_consistency(
                gt_cmds, parse_mml(mml_text), key_params=kps)
        except Exception as _e:
            r['V5_error'] = f'{type(_e).__name__}: {_e}'
    # ── G16：revise 时前代命令族是否保留（2026-11-01 新增） ──
    if prior_mml:
        try:
            r['G16_prior_keep'] = check_prior_fams_kept(prior_mml, mml_text)
        except Exception as _e:
            r['G16_error'] = f'{type(_e).__name__}: {_e}'

    return r


def summary_lines(result, limit=8):
    """把校验结果转成人类可读的告警行（写进产物）。"""
    lines = []
    c1 = result['C1_assembly']
    if not c1['ok']:
        if c1['missing_in_mml']:
            lines.append(f"装配丢失 {len(c1['missing_in_mml'])} 族："
                         + '、'.join(c1['missing_in_mml'][:limit]))
        if c1['extra_in_mml']:
            lines.append(f"方案外多出 {len(c1['extra_in_mml'])} 族："
                         + '、'.join(c1['extra_in_mml'][:limit]))
    c2 = result['C2_references']
    if not c2['ok']:
        top = c2['dangling'][:limit]
        detail = '；'.join(f"{d['cmd']}.{d['param']}={d['value']}(被{d['ref_count']}条引用)"
                           for d in top)
        lines.append(f"引用悬空 {len(c2['dangling'])} 处：{detail}")
    c3 = result['C3_duplicate']
    if not c3['ok']:
        top = c3['duplicates'][:limit]
        detail = '、'.join(f"{d['cmd']}[{d['key']}]" for d in top)
        lines.append(f"重复下发 {len(c3['duplicates'])} 条（EXP 已有）：{detail}")
    c4 = result.get('C4_batch')
    if c4 and not c4['ok']:
        parts = []
        for d in c4['under_covered'][:limit]:
            miss = '、'.join(d['missing'][:3])
            parts.append(f"{d['family']} {d['got']}/{d['need']}（缺 {d['missing_n']} 个：{miss}）")
        lines.append(f"批量展开不足 {len(c4['under_covered'])} 族：" + '；'.join(parts))
    return lines

"""业务段簇分析：照着配的核心能力。

★ 2026-11-12 设计（用户裁定方向）

问题：
  意图说「APN sos 按现网 ims.wh 存量配齐」。
  要配的不是单个族，而是一整簇（URR/URRGROUP/PCCPOLICYGRP/RULE/
  USERPROFILE/RULEBINDING/UPBINDUPG 等 8-19 个族）。

  原设想「按引用关系追链 + 按参数依赖归纳命名算子」实测不可行：
    · RULEBINDING/PNFDNN 等族的名字跟被引用对象名毫无派生关系
    · 574 对 URRGROUP←URR 配对里只有 45% 有后缀替换关系

新设计（实测 6/7 正确）：
  ① 业务段识别：从参照对象的多个族名字里提取公共业务段
     ims_sig_cbb_offline / ims_sig_ch_p / r_ims_sig / up_ims
     → 业务段 "ims"（变体 "ims_sig"）
  ② 簇成员发现：用业务段全文搜索 EXP，找出所有含它的族
     实测含 "ims" 的族有 19 个，比追引用关系更全
     （PCCTEMPLATE / APNUSRPROFG 追引用追不到，但业务段能发现）
  ③ 名字平移：业务段替换
     ims_sig_cbb_offline → sos_sig_cbb_offline
     r_ims_sig           → r_sos_sig
     up_ims              → up_sos
  ④ 平移校验：平移后的名字符合同族现网命名规律吗？
     不成立 → 标待确认（如 upg_ims → upg_sos 不成立，现网是 up_group_*）
"""
import re
from collections import Counter, defaultdict
from pathlib import Path

# 业务段识别的候选长度范围
BIZ_SEG_MIN_LEN = 3
BIZ_SEG_MAX_LEN = 40

# 视为「分隔符」的字符：业务段切分时用
SEP_CHARS = r'[_\-.@/]'


def _split_identifier(name):
    """把标识符切成字符片段。

    'ims_sig_cbb_offline' → ['ims', 'sig', 'cbb', 'offline']
    'ims.wh'              → ['ims', 'wh']
    'APP-HZZZhbSMF001'    → ['APP', 'HZZZhbSMF001']
    """
    return [p for p in re.split(SEP_CHARS, name) if p]


def _is_generic_token(tok):
    """判断是不是通用词（不能当业务段）。

    这些词在大量对象名里出现，不具业务区分度：
      online / offline / cb / ch / pcc / p / g / default / base / ...
    """
    GENERIC = {
        'online', 'offline', 'cbb', 'cb', 'ch', 'p', 'g', 'pcc', 'sig',
        'default', 'base', 'any', 'all', 'none', 'null', 'tmp', 'temp',
        'test', 'v4', 'v6', 'ipv4', 'ipv6', 'l3', 'l7', 'in', 'out',
        'up', 'down', 'ul', 'dl', 'rx', 'tx', 'srv', 'cli',
    }
    return tok.lower() in GENERIC or tok.isdigit() or len(tok) < 2


def extract_biz_segment(names):
    """从一组对象名里提取业务段。

    names = ['ims_sig_cbb_offline', 'ims_sig_ch_p', 'r_ims_sig', 'up_ims']
    → 'ims'（因为它在所有名字里都出现，且不是通用词）

    做法：
      1. 把每个名字切成 token
      2. 统计每个 token 出现在多少个名字里
      3. 出现在 >= 60% 名字里、且不是通用词的 token，组成业务段候选
      4. 优先选最长的连续组合（'ims_sig' 优于 'ims'）
    """
    if not names:
        return None, []

    token_sets = []
    for n in names:
        toks = _split_identifier(n)
        token_sets.append([t for t in toks if not _is_generic_token(t)])

    if not token_sets:
        return None, []

    # 统计 token 覆盖了多少个名字
    cnt = Counter()
    for toks in token_sets:
        for t in set(toks):
            cnt[t] += 1

    n_names = len(names)
    threshold = max(2, int(n_names * 0.6))
    candidates = [t for t, c in cnt.items() if c >= threshold]

    if not candidates:
        return None, []

    # 优先选出现次数最多的（最能代表这组对象）
    candidates.sort(key=lambda t: (-cnt[t], -len(t)))
    primary = candidates[0]

    # 尝试扩展成更长的业务段（如 ims + sig → ims_sig）
    # 做法：看名字里 primary 后面紧跟的 token 是否也普遍出现
    extended = [primary]
    for n in names:
        toks = _split_identifier(n)
        for i, t in enumerate(toks):
            if t == primary and i + 1 < len(toks):
                nxt = toks[i + 1]
                if not _is_generic_token(nxt):
                    extended.append(f'{primary}_{nxt}')
                break

    ext_cnt = Counter(extended)
    if len(ext_cnt) > 1:
        best_ext, best_c = ext_cnt.most_common(1)[0]
        if best_c >= threshold and best_ext != primary:
            primary = best_ext

    return primary, candidates


def _contains_token(value, token):
    """判断 value 里是否含【完整的】token（按分隔符切分后）。

    'IMSI_PREFIX' 对 'ims'  → False（IMSI 是另一个词）
    'ims_sig_cbb' 对 'ims'  → True
    'ims.ens'     对 'ims'  → True
    """
    if not value or not token:
        return False
    toks = _split_identifier(value)
    t = token.lower()
    # 完整 token 匹配
    if any(x.lower() == t for x in toks):
        return True
    # 业务段含分隔符时（如 ims_sig），按前缀匹配整段
    if '_' in token or '.' in token:
        return value.lower().startswith(t)
    return False


def find_cluster_members(exp_path, biz_segment, limit=200):
    """用业务段全文搜索 EXP，找出所有含它的族及其对象名。

    返回：
      {
        'URR': {'count': 2, 'names': ['ims_sig_cbb_offline', 'ims_sig_cbb_online']},
        'URRGROUP': {...},
        ...
      }

    为什么不用引用关系追链：
      实测含 "ims" 的族有 19 个，追引用关系只能找到 8 个。
      PCCTEMPLATE / APNUSRPROFG 这类「引用关系不明显但同属一个业务」的族会漏。
    """
    p = Path(exp_path)
    if not p.exists():
        return {}

    # 业务段可能以多种形态出现（ims / ims_sig / IMS）
    seg_variants = {biz_segment.lower(), biz_segment.upper()}

    out = defaultdict(lambda: {'count': 0, 'names': []})
    try:
        with open(p, encoding='utf-8', errors='replace') as f:
            for line in f:
                m = re.match(
                    r'^(ADD|SET|MOD)\s+([A-Z][A-Z0-9_]+)\s*:\s*'
                    r'([A-Z][A-Z0-9_]*)\s*=\s*"?([^",;]+)"?', line.strip())
                if not m:
                    continue
                verb, fam, pk, val = m.groups()
                if verb != 'ADD':
                    continue
                # ★ 2026-11-12 修误报：必须按 token 边界匹配
                #   旧做法 val_low = val.lower(); 'ims' in val_low
                #   → "IMSI_PREFIX" 里含 "ims" 字符 → 误判成同簇
                #   实测误报了 GBIMEICFG / IUIMEICFG / S1IMEICFG / IMSISMCHAR
                if not _contains_token(val, biz_segment):
                    continue
                d = out[fam]
                d['count'] += 1
                if val not in d['names'] and len(d['names']) < limit:
                    d['names'].append(val)
    except Exception:
        return {}

    return dict(out)


def translate_name(ref_name, ref_biz, target_biz):
    """把参照对象名里的业务段替换成目标业务段。

    translate_name('ims_sig_cbb_offline', 'ims', 'sos') → 'sos_sig_cbb_offline'
    translate_name('r_ims_sig', 'ims', 'sos')           → 'r_sos_sig'
    translate_name('up_ims', 'ims', 'sos')              → 'up_sos'

    规则：
      · 大小写跟随原值（IMS → SOS，ims → sos）
      · 只替换完整的 token（不能把 "imsims" 里的 ims 替换掉）
    """
    if not ref_name or not ref_biz or not target_biz:
        return ref_name

    # 保持大小写风格
    ref_upper = ref_biz.upper()
    tgt_upper = target_biz.upper()

    # 用 token 边界替换，避免子串误伤
    # 业务段里可能含 _ -. 等分隔符，直接做词边界替换
    pattern = re.compile(rf'(?<![A-Za-z0-9]){re.escape(ref_biz)}(?![a-z0-9])', re.I)

    def repl(m):
        orig = m.group(0)
        if orig.isupper():
            return tgt_upper
        if orig[0].isupper():
            return target_biz[0].upper() + target_biz[1:]
        return target_biz

    return pattern.sub(repl, ref_name)


def check_skeleton_preserved(ref_name, candidate_name, biz_segment, target_biz):
    """校验平移是否只替换了业务段、没破坏名字骨架。

    ★ 2026-11-12 新增（修正过度告警）

    问题：原 check_name_against_pattern 会拿平移后的名字去校验现网命名规律，
      但 RULE 的现网名字本身就有 r_ims_sig / 1001271_pptv_r / 10.0.0.172_r 三种形态，
      「主流前缀 stlj_」只占 20%，拿它当判据必然误报。
      USERPROFILE 同理：up_ims 就是现网存在的名字，平移后 up_sos 天然合法。

    正确判据：平移只应该替换业务段，其余部分（骨架）必须完全不变。
      参照:  r_ims_sig     → 骨架 r_{BIZ}_sig，替换后 r_sos_sig     ✅
      参照:  up_ims        → 骨架 up_{BIZ}，   替换后 up_sos        ✅
      反例:  upg_ims 平移成 upg_sos 也是骨架不变，但现网主流是 up_group_{BIZ}
            → 骨架校验通过，但命名形态不符 → 交给另一条判据
    """
    expected = translate_name(ref_name, biz_segment, target_biz)
    if expected == candidate_name:
        return {'ok': True,
                'reason': f'骨架保持（{ref_name} → {candidate_name}，只替换业务段）'}
    return {'ok': False,
            'reason': f'骨架被破坏：期望 {expected}，实际 {candidate_name}',
            'expected': expected}


def check_name_against_pattern(fam, candidate_name, exp_path, min_coverage=0.3):
    """检查候选名符合同族现网命名规律吗。

    做法：
      1. 拉同族所有现网对象名
      2. 归纳后缀规律（如 URRGROUP 的 _ch_p 占 91%）
      3. 检查候选名的后缀是否在规律里

    返回：
      {'ok': bool, 'reason': str, 'expected_suffixes': [...], 'got_suffix': str}

    实测用途：
      upg_ims → upg_sos 平移后，UPBINDUPG 现网是 up_group_* / u_p_g_* / upg_ims
      → 后缀检查发现 upg_sos 虽符合「upg_」前缀但现网主流是 up_group_
      → 标待确认
    """
    p = Path(exp_path)
    if not p.exists():
        return {'ok': True, 'reason': 'EXP 不存在，跳过校验'}

    names = []
    try:
        with open(p, encoding='utf-8', errors='replace') as f:
            for line in f:
                m = re.match(
                    rf'^ADD\s+{re.escape(fam)}\s*:\s*[A-Z][A-Z0-9_]*\s*=\s*"([^"]+)"',
                    line.strip())
                if m:
                    names.append(m.group(1))
                    if len(names) >= 2000:
                        break
    except Exception:
        return {'ok': True, 'reason': '读取失败，跳过校验'}

    if len(names) < 3:
        return {'ok': True, 'reason': f'同族实例仅 {len(names)} 个，样本不足'}

    # 归纳后缀规律（末段 _xxx 或末两段 _xxx_yyy）
    suffs = Counter()
    for n in names:
        parts = n.rsplit('_', 1)
        if len(parts) == 2 and parts[1]:
            suffs['_' + parts[1]] += 1
        parts2 = n.rsplit('_', 2)
        if len(parts2) == 3:
            suffs['_' + parts2[1] + '_' + parts2[2]] += 1

    total = len(names)
    significant = [(s, c / total) for s, c in suffs.items()
                   if c / total >= min_coverage]

    # ★ 2026-11-12：无后缀规律时不能直接放过，要继续做前缀校验
    #   实测 UPBINDUPG 无后缀规律（名字是 up_group_cmcc_xx 这种多段），
    #   旧逻辑直接 return ok=True → 错过了 upg_sos 与 up_group_sos 的差异
    if not significant:
        pass    # 继续走后面的前缀校验

    # 检查候选名
    cand_suffs = []
    parts = candidate_name.rsplit('_', 1)
    if len(parts) == 2:
        cand_suffs.append('_' + parts[1])
    parts2 = candidate_name.rsplit('_', 2)
    if len(parts2) == 3:
        cand_suffs.append('_' + parts2[1] + '_' + parts2[2])

    matched = [s for s, _ in significant if s in cand_suffs]
    if matched:
        return {'ok': True, 'reason': f'后缀 {matched[0]} 符合现网规律',
                'expected_suffixes': [s for s, _ in significant[:3]]}
    # 后缀不匹配或无后缀规律 → 继续前缀校验（见下）

    # ★ 2026-11-12：无后缀规律时，改用「前缀形态」校验
    #   实测 UPBINDUPG：现网 16 个实例有 3 种前缀形态
    #     up_group_<biz>  (68.8%)
    #     upg_<biz>       (6.2%)
    #     u_p_g_<biz>     (个例)
    #   平移得到 upg_sos，虽然「ups_」前缀合法（占 6.2%），
    #   但主流是 up_group_，应该提示用户核对。
    #   旧逻辑因为「无稳定后缀规律」直接放过 → 漏掉了这个风险。
    # ★ 2026-11-12 修统计口径：每个实例只计一次前缀（取最长的形态）
    #   旧做法同时记 up_ 和 up_group_，导致计数重复、ratio 算错
    #   实测错成「upg_ 占 100%」，实际只有 1/16 = 6.2%
    PREFIX_CANDIDATES = ['up_group_', 'upg_', 'u_p_g_', 'u_p_', 'up_',
                         'r_', 'mk_', 'cg_', 'sos_', 'base-']
    prefixes = Counter()
    for n in names:
        low = n.lower()
        matched = None
        for pf in PREFIX_CANDIDATES:
            if low.startswith(pf):
                if matched is None or len(pf) > len(matched):
                    matched = pf
        if matched:
            prefixes[matched] += 1
        else:
            # 兜底：取第一段
            first = n.split('_', 1)
            if len(first) == 2:
                prefixes[first[0] + '_'] += 1

    sig_prefixes = [(p, c / total) for p, c in prefixes.items()
                    if c / total >= 0.15 and len(p) >= 4]

    if sig_prefixes:
        sig_prefixes.sort(key=lambda x: -x[1])
        # ★ 2026-11-12 修正判据：候选名匹配的前缀，占比必须达到主流水平的一半
        #   实测 UPBINDUPG：up_group_ 占 87.5%，upg_ 只占 6.2%
        #   候选 upg_sos 匹配 upg_（6.2%）→ 旧逻辑判"合法"（漏报）
        #   新逻辑：匹配前缀的占比 < 主流占比 × 0.5 → 报不匹配
        top_prefix, top_ratio = sig_prefixes[0]
        cand_match = None
        # ★ 2026-11-12 修 bug：prefixes 存的是【个数】不是比例
        #   旧代码 for pf, ratio in prefixes.most_common() 里 ratio 其实是 count
        #   → 候选 upg_ 的 count=1，"1 >= 0.88*0.5" 恒成立 → 误判合法
        for pf, pcnt in prefixes.most_common():
            if pf in ('', '_'):
                continue
            if candidate_name.lower().startswith(pf.lower()):
                if cand_match is None or len(pf) > len(cand_match[0]):
                    cand_match = (pf, pcnt, pcnt / total)
        if cand_match:
            pf, pcnt, ratio = cand_match
            if ratio >= top_ratio * 0.5:
                return {'ok': True,
                        'reason': (f'前缀 {pf} 符合现网规律（占 {ratio*100:.0f}%，'
                                   f'主流 {top_prefix} 占 {top_ratio*100:.0f}%）'),
                        'expected_prefixes': [p for p, _ in sig_prefixes[:3]],
                        'matched_prefix': pf}
            return {
                'ok': False,
                'reason': (f'{fam} 现网主流前缀是 {top_prefix}（占 {top_ratio*100:.0f}%），'
                           f'候选名 {candidate_name} 用的是 {pf}（仅占 {ratio*100:.0f}%），'
                           f'建议核对是否应为 {top_prefix}<biz>'),
                'expected_prefixes': [p for p, _ in sig_prefixes[:3]],
                'got_prefix': pf,
                'got_ratio': ratio,
                'suggested': top_prefix + 'sos',
            }
        return {
            'ok': False,
            'reason': (f'{fam} 现网前缀形态是 '
                       f'{", ".join(p for p, _ in sig_prefixes[:3])}，'
                       f'但候选名 {candidate_name} 不匹配任何形态'),
            'expected_prefixes': [p for p, _ in sig_prefixes[:3]],
            'got_name': candidate_name,
        }

    return {'ok': True,
            'reason': f'{fam} 无稳定后缀/前缀规律（{total} 个实例），无法校验'}


def analyze_business_cluster(exp_path, seed_names):
    """一次调用完成：业务段识别 → 簇成员发现。

    参数：
      exp_path     EXP 路径
      seed_names   参照对象的名字列表（如 ['ims_sig_cbb_offline', 'r_ims_sig', 'up_ims']）

    返回：
      {
        'biz_segment': 'ims',
        'candidates': ['ims', 'sig'],
        'cluster': {族: {'count': n, 'names': [...]}}
      }
    """
    biz, cands = extract_biz_segment(seed_names)
    if not biz:
        return {'biz_segment': None, 'candidates': [], 'cluster': {}}
    cluster = find_cluster_members(exp_path, biz)
    return {'biz_segment': biz, 'candidates': cands, 'cluster': cluster}


# ═══════════════════════════════════════════════════════════
# 自测
# ═══════════════════════════════════════════════════════════
if __name__ == '__main__':
    import json
    import sys

    GT = json.loads(Path('/tmp/gt_cleaned.json').read_text(encoding='utf-8'))
    g = next(x for x in GT if x['ticket'] == 'NC20260810002261')
    adir = Path(g['path']) / '备份附件'
    UNC = next((p for p in adir.glob('*.txt') if '_UNC_' in p.name), None)

    print('=' * 84)
    print('业务段簇分析自测')
    print('=' * 84)

    # 1) 业务段识别
    SEED = ['ims_sig_cbb_offline', 'ims_sig_cbb_online', 'ims_sig_ch_p',
            'ims_sig_pcc_p_g', 'r_ims_sig', 'up_ims', 'upg_ims']
    biz, cands = extract_biz_segment(SEED)
    print(f'\n1) 业务段识别')
    print(f'   输入 {len(SEED)} 个名字')
    print(f'   识别出: {biz!r}')
    print(f'   候选: {cands[:5]}')

    # 2) 簇成员发现
    cluster = find_cluster_members(str(UNC), biz)
    print(f'\n2) 簇成员发现（业务段 {biz!r}）')
    print(f'   找到 {len(cluster)} 个族')
    for fam, d in sorted(cluster.items(), key=lambda x: -x[1]['count'])[:12]:
        print(f'     {fam:<22} {d["count"]:>3} 个  {d["names"][:3]}')

    # 3) 名字平移
    print(f'\n3) 名字平移（{biz} → sos）')
    for n in SEED:
        print(f'   {n:<28} → {translate_name(n, biz, "sos")}')

    # 4) 平移校验
    print(f'\n4) 平移校验')
    CHECKS = [
        ('URRGROUP', 'sos_sig_ch_p'),
        ('PCCPOLICYGRP', 'sos_sig_pcc_p_g'),
        ('RULE', 'r_sos_sig'),
        ('USERPROFILE', 'up_sos'),
        ('UPBINDUPG', 'upg_sos'),          # 预期不通过
    ]
    for fam, cand in CHECKS:
        r = check_name_against_pattern(fam, cand, str(UNC))
        mark = '✅' if r['ok'] else '⚠'
        print(f'   {mark} {fam:<16} {cand:<22} {r["reason"][:60]}')

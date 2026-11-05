# -*- coding: utf-8 -*-
"""check_v0_v5.py — 新增两条判据（2026-10-30）。

V0 EXP 网元核对
  背景（用户判断）：引用悬空的四种原因里，**④ EXP 拿错网元可能性最大**——
  同类型网元在同一网管下管理，EXP 一般批量获取，容易传错。
  实测 NC20260817001781：EXP 有 654 个 ADD APN，但含工单客户前缀
  "HBWHZXY02S" 的 0 个 ⇒ 高度怀疑 EXP 不是本工单网元。

V5 枚举值一致性
  用户裁决：「枚举类的参数不一致，类似 enable/disable，这种不一致就算命令不一致
  （命令+枚举的具体值是一个独立的"命令"，不能只看命令名）」
  实现：把"命令族 + 主键 + 全部参数值"当成一条命令的签名；
        同族同主键但任一参数不同 ⇒ 判不一致。
        枚举值相反（ENABLE↔DISABLE 等）单列为高优先级。
"""
import re

# ── V0: EXP 网元核对 ──────────────────────────────────────────

# EXP 文件名结构：EXPMML_ME0_UDG_<IP>_<HA>_<省缩写>_<网元名>_<HW>_<时间戳>.txt
_EXP_NF_RE = re.compile(
    r'EXPMML[_-]ME\d+[_-]\w+?[_-](?:\d+\.\d+\.\d+\.\d+)[_-]'
    r'(?:[A-Z]{2}[_-])?(?:[A-Z]{2,5}[_-])?([A-Za-z]+\d+[A-Za-z]*)[_-]',
    re.I)
# 更宽松：从文件名里找形如 UPF700 / SMF / UPFm005BHW 的网元标识
# 网元标识：UPF700 / NJUPFm005BHW 之类，遇到 _B_ / _HW / 日期 就停
_NF_TOKEN_RE = re.compile(
    r'(UPF[A-Za-z0-9]*(?:m\d+[A-Za-z0-9]*)?|SMF\w*|AMF\w*|PGW\w*|SGW\w*|GGSN\w*)',
    re.I)


def parse_exp_nf(exp_filename):
    """从 EXP 文件名提取网元标识（截到 _B_ / _HW / 日期 / 点 前）"""
    if not exp_filename:
        return ''
    m = _NF_TOKEN_RE.search(exp_filename)
    if not m:
        return ''
    tok = m.group(1)
    # 先按 _ . 切（去掉 _B_xxx / .txt）
    tok = re.split(r'[_.]', tok)[0]
    # 只去掉明确的后缀标记，不砍网元名本身
    #   UPF700_B_HW_2026...  → 已切成 UPF700
    #   NJUPFm005BHW_2026... → 切成 NJUPFm005BHW（保留，这是完整网元名）
    return tok


def parse_intent_nf(intent_text):
    """从意图文本提取网元标识（标题/变更目的段）"""
    if not intent_text:
        return set()
    head = intent_text.split('## 操作脚本')[0][:3000]
    return {x.upper() for x in _NF_TOKEN_RE.findall(head)}


def check_exp_nf(exp_filename, intent_text, exp_text=''):
    """V0：EXP 网元是否与工单意图一致。

    返回 {'ok', 'exp_nf', 'intent_nfs', 'warn', 'detail'}
    """
    exp_nf = parse_exp_nf(exp_filename)
    intent_nfs = parse_intent_nf(intent_text)

    r = {'exp_nf': exp_nf, 'intent_nfs': sorted(intent_nfs),
         'ok': True, 'warn': False, 'detail': ''}

    if not exp_nf:
        r['detail'] = 'EXP 文件名里没识别出网元标识，跳过核对'
        return r

    if not intent_nfs:
        r['detail'] = '意图里没提到具体网元名，无从核对（可能工单用代号）'
        return r

    # 意图里的网元类型（去掉数字后缀）与 EXP 比对
    exp_kind = re.sub(r'\d+.*$', '', exp_nf).upper()
    intent_kinds = {re.sub(r'\d+.*$', '', x).upper() for x in intent_nfs}

    if exp_kind and exp_kind not in intent_kinds:
        r['ok'] = False
        r['warn'] = True
        r['detail'] = (f'EXP 网元是 {exp_nf}，但工单意图提到的是 '
                       f'{"、".join(sorted(intent_nfs))} ⇒ EXP 可能拿错网元')
    else:
        r['detail'] = f'EXP 网元 {exp_nf} 与意图一致'
    return r


def check_exp_content_alignment(intent_text, exp_text, sample_prefixes=None):
    """V0 增强：EXP 内容里能否找到工单的关键业务实体。

    背景：实测 NC20260817001781 的 EXP 有 654 个 ADD APN，但含工单客户前缀
    "HBWHZXY02S" 的 0 个 ⇒ 强信号说明 EXP 不是这个客户/网元。

    做法：从意图里提取"像业务实体名"的 token（大写字母+数字+点的组合），
    在 EXP 里找不到任何一个 ⇒ 告警。
    """
    if not intent_text or not exp_text:
        return {'ok': True, 'checked': 0, 'detail': '缺意图或 EXP，跳过'}

    head = intent_text.split('## 操作脚本')[0]
    # 形如 HBWHZXY02S.5GHA.NJIOT 或 SXBXRJSX4G02S.SXM2M 的 APN 式标识
    tokens = set(re.findall(r'\b[A-Z][A-Z0-9]{5,}\.[A-Za-z0-9][A-Za-z0-9._]{3,}\b', head))
    # 形如 5giot / sos_sig 这类短名不进（太泛）
    if not tokens:
        return {'ok': True, 'checked': 0, 'detail': '意图里没提取到可核对的业务实体名'}

    missing = [t for t in tokens if t not in exp_text]
    hit = [t for t in tokens if t in exp_text]

    r = {'checked': len(tokens), 'hit': hit[:5], 'missing': missing[:5],
         'ok': bool(hit) or not tokens, 'warn': False, 'detail': ''}
    if tokens and not hit:
        r['warn'] = True
        r['ok'] = False
        r['detail'] = (f'意图里的 {len(tokens)} 个业务实体名，在 EXP 里一个都找不到'
                       f'（如 {missing[0] if missing else ""}）⇒ EXP 极可能不是本工单网元')
    else:
        r['detail'] = f'{len(hit)}/{len(tokens)} 个业务实体名在 EXP 中命中'
    return r


# ── V5: 枚举值一致性 ──────────────────────────────────────────

ENUM_FLIP = {
    'ENABLE': 'DISABLE', 'DISABLE': 'ENABLE',
    'YES': 'NO', 'NO': 'YES',
    'TRUE': 'FALSE', 'FALSE': 'TRUE',
    'ON': 'OFF', 'OFF': 'ON',
    'ENABLED': 'DISABLED', 'DISABLED': 'ENABLED',
    'OPEN': 'CLOSE', 'CLOSE': 'OPEN',
    'ALLOW': 'DENY', 'DENY': 'ALLOW',
}


def cmd_signature(verb, cmd, params):
    """一条命令的完整签名：命令族 + 全部参数（大小写不敏感）。

    用户裁决：命令+枚举值是一个独立单位，不能只看命令名。
    """
    kv = tuple(sorted((k.upper(), str(v).strip().upper()) for k, v in params.items()))
    return (verb.upper(), cmd.upper(), kv)


def check_enum_consistency(gt_cmds, gen_cmds, key_params=()):
    """V5：同族同主键的命令，参数值是否一致；枚举相反单列。

    参数：
      gt_cmds / gen_cmds: [(verb, cmd, params), ...]
      key_params: 用于配对的主键参数名元组

    返回 {
      'ok', 'n_compared', 'value_diff': [{fam, key, param, gt, gen, enum_flip}],
      'enum_flips': [...], 'detail'
    }
    """
    def keyof(params):
        for kp in key_params:
            if kp in params:
                return str(params[kp]).upper()
        return ''

    gen_idx = {}
    for v, c, p in gen_cmds:
        gen_idx.setdefault(f'{v} {c}|{keyof(p)}', []).append((v, c, p))

    diffs, flips = [], []
    compared = 0
    for v, c, p in gt_cmds:
        k = f'{v} {c}|{keyof(p)}'
        cands = gen_idx.get(k) or []
        if not cands:
            continue
        compared += 1
        best = min(cands, key=lambda x: sum(
            1 for kk in set(p) | set(x[2])
            if str(p.get(kk, '')).upper() != str(x[2].get(kk, '')).upper()))
        for kk in set(p) | set(best[2]):
            a = str(p.get(kk, '')).upper()
            b = str(best[2].get(kk, '')).upper()
            if not a and not b:
                continue
            if a == b:
                continue
            if not b or not a:
                continue          # 一侧缺失，归 C1/装配，不在此判
            item = {'fam': f'{v} {c}', 'key': keyof(p), 'param': kk,
                    'gt': p.get(kk), 'gen': best[2].get(kk),
                    'enum_flip': ENUM_FLIP.get(a) == b}
            diffs.append(item)
            if item['enum_flip']:
                flips.append(item)

    return {
        'ok': not diffs,
        'n_compared': compared,
        'value_diff': diffs[:50],
        'value_diff_n': len(diffs),
        'enum_flips': flips[:30],
        'enum_flip_n': len(flips),
        'detail': (f'比对 {compared} 条同类命令，{len(diffs)} 处参数值不同'
                   f'（其中 {len(flips)} 处枚举相反）') if diffs else
                  f'比对 {compared} 条同类命令，参数值全部一致',
    }

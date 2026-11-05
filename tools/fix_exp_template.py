# -*- coding: utf-8 -*-
"""fix_exp_template.py — V8：从 EXP 同族实例补全缺失的命令族。

用户拍板（2026-10-30）：1B —— 先全部允许照抄，发现问题再禁。

背景：
  42 族次真缺失，全部是「EXP 里有同族实例，产物没采纳」：
    SET URRGRPBINDING  6 族次  EXP 19+ 实例
    SET LICENSESWITCH  5 族次  EXP 110+ 实例
    ADD URRGROUP       3 族次  EXP 142+ 实例
    ...

设计：
  · 对每个「方案要但产物没有」的族，若 EXP 有实例 → 用实例做模板补一条
  · 参数照抄最近的一个实例（同名参数保留原值）
  · 主键参数（如 URRNAME）若与已有实例冲突，按 EXP 命名规律递增
  · origin=exp_template 标注来源

约束（V9 会补）：
  照抄的参数格式可能与文档不同 —— 这里以 EXP 为准（EXP 是现网实际运行的）。
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import gen_selfcheck as gs

# 主键参数（这些值决定对象身份，不能随便照抄）
KEY_PARAMS = (
    'IFNAME', 'VRFNAME', 'APN', 'POOLNAME', 'SECTIONNAME', 'GROUPNAME',
    'PROFILENAME', 'POLICYNAME', 'RULENAME', 'SERVERNAME', 'HOSTNAME',
    'FLOWFILTERNAME', 'FILTERNAME', 'USERPROFILENAME', 'LICITEM',
    'DNN', 'VNINSTANCE', 'VPNINSTANCE', 'SERVICEINSTANCE', 'NFINSTANCENAME',
    'NETWORKINSTANCE', 'APNNAME', 'NSIDX', 'INDEX', 'URRGROUPNAME',
    'URRNAME', 'WORKERNAME', 'GRPNAME', 'MAPNAME', 'MAPPINGNAME',
    'PCCPOLICYNAME', 'PCSCFGRPNAME', 'IPFARMNAME', 'IFIPV4ADDR',
)

# 不参与"补全"判断的动词
CFG_VERBS = {'ADD', 'MOD', 'SET'}


def _render(verb, cmd, params):
    """把 (verb, cmd, params) 渲染回一行 MML"""
    parts = []
    for k, v in params.items():
        v = str(v)
        if re.fullmatch(r'-?\d+(\.\d+)?', v) or v.upper() in (
                'TRUE', 'FALSE', 'ENABLE', 'DISABLE', 'UP', 'DOWN'):
            parts.append(f'{k}={v}')
        else:
            parts.append(f'{k}="{v}"')
    return f'{verb} {cmd}:{", ".join(parts)};'


def _fam_instances(exp_cmds, fam):
    """从 EXP 里取该族的全部实例，按参数个数降序（参数最全的优先当模板）"""
    out = []
    for v, c, p in exp_cmds:
        if f'{v} {c}'.upper() == fam.upper():
            out.append((v, c, p))
    out.sort(key=lambda x: -len(x[2]))
    return out


def _next_key_value(base_value, existing):
    """主键冲突时按尾号递增：LB1060 → LB1061"""
    if base_value.upper() not in {e.upper() for e in existing}:
        return base_value
    m = re.match(r'^(.*?)(\d+)$', base_value)
    if not m:
        return base_value
    prefix, num = m.group(1), int(m.group(2))
    used = {e.upper() for e in existing}
    for i in range(num + 1, num + 10000):
        cand = f'{prefix}{i}'
        if cand.upper() not in used:
            return cand
    return base_value


def fix_exp_template(plan_text, mml_text, exp_text, intent_text=''):
    """用 EXP 同族实例补全「方案要但产物没有」的命令族。

    返回 (new_mml, added_list, note)
    """
    if not exp_text:
        return mml_text, [], ''

    exp_cmds = gs.parse_mml(exp_text)
    gen_cmds = gs.parse_mml(mml_text)
    if not exp_cmds:
        return mml_text, [], ''

    gen_fams = {f'{v} {c}'.upper() for v, c, p in gen_cmds}
    exp_fams_set = {f'{v} {c}'.upper() for v, c, p in exp_cmds}

    # 方案（md）里要的族
    plan_fams = {f'{v} {c}'.upper() for v, c, p in gs.parse_mml(
        gs._exclude_non_target(plan_text))}

    # 意图里点名的族（补充来源）
    intent_fams = set()
    if intent_text:
        for m in gs._CMD_RE.finditer(intent_text):
            intent_fams.add(f'{m.group(1).upper()} {m.group(2).upper()}')

    # 要补的族 = (方案要 OR 意图要) 且 产物没有 且 EXP 有实例
    wanted = (plan_fams | intent_fams) - gen_fams
    to_fill = sorted(f for f in wanted
                     if f in exp_fams_set and f.split()[0] in CFG_VERBS)

    if not to_fill:
        return mml_text, [], ''

    # 产物里各族的现有主键值（避免补出重复对象）
    existing_by_param = {}
    for v, c, p in gen_cmds:
        for k, val in p.items():
            existing_by_param.setdefault(k.upper(), set()).add(str(val).upper())

    add_lines = []
    details = []
    for fam in to_fill:
        insts = _fam_instances(exp_cmds, fam)
        if not insts:
            continue
        verb, cmd, tpl = insts[0]
        params = dict(tpl)
        # 主键值：取模板的，若冲突则递增
        for kp in KEY_PARAMS:
            if kp in params:
                old = str(params[kp])
                ex = existing_by_param.get(kp, set())
                nv = _next_key_value(old, ex)
                if nv != old:
                    params[kp] = nv
                    existing_by_param.setdefault(kp, set()).add(nv.upper())
                else:
                    existing_by_param.setdefault(kp, set()).add(old.upper())
                break
        line = _render(verb, cmd, params)
        add_lines.append(line)
        details.append(f'{fam}（模板来自 EXP，{len(tpl)} 个参数）')

    if not add_lines:
        return mml_text, [], ''

    new = (mml_text.rstrip()
           + '\n\n// ── 交付前自检补齐（V8 EXP 同族模板）──\n'
           + '\n'.join(add_lines) + '\n')
    note = f'从 EXP 同族实例补齐 {len(add_lines)} 族：' + '、'.join(details[:3])
    if len(details) > 3:
        note += f' 等 {len(details)} 族'
    return new, add_lines, note

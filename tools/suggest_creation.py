# -*- coding: utf-8 -*-
"""suggest_creation.py — 引用悬空时生成"补建建议"（注释掉 + 问询）。

用户裁决（2026-10-30）：
  「引用悬空建议补建，但是注释掉，增加问询，
    确认补建/删子/改引用/EXP错误等问题后再修改」
  「这四个原因前三个风险都很大，我只做①的原因是作为提醒和 EXP 的对齐，
    向用户说明你要操作的实体不存在，反而④的可能性最大（意图正确的前提下）」

概率排序（用户判断）：
  ④ EXP 拿错网元（最可能，同网管批量取 EXP 易传错）
  ① 规划占位（要建但现在不用）
  ② 该删没删（基本不存在，删除是明确意图且需先去激活评估）
  ③ 引用写错（人为，不管）
"""
import json
import re
from pathlib import Path

RULES = Path('/opt/expgv/rules/ref_to_create.yaml')
RULES_LOCAL = Path('/Users/alesc/workspace/udg01-batch/rules/ref_to_create.yaml')


def _load_map():
    """读 ref_to_create.yaml 的 mapping 段。"""
    p = RULES if RULES.exists() else RULES_LOCAL
    if not p.exists():
        return {}
    try:
        import yaml
        d = yaml.safe_load(p.read_text(encoding='utf-8')) or {}
        raw = d.get('mapping') or {}
        return {str(k).upper(): {'create': str(v.get('create') or ''),
                                 'key': str(v.get('key') or '')}
                for k, v in raw.items()}
    except Exception:
        # 退化为逐行解析
        mp = {}
        for line in p.read_text(encoding='utf-8').split('\n'):
            m = re.match(r'\s*([A-Za-z0-9_]+):\s*\{create:\s*"([^"]*)",\s*key:\s*"([^"]*)"\}', line)
            if m:
                mp[m.group(1).upper()] = {'create': m.group(2), 'key': m.group(3)}
        return mp


def build_suggestion(dangling_item, exp_info=None):
    """为一条悬空项生成补建建议。

    dangling_item: gen_selfcheck.check_references 输出的一项
        {cmd, param, value, verb, ref_count}
    exp_info: {'exp_nf':..., 'entity_hit': bool, 'apn_total': n, 'prefix_hit': n}

    返回 {'obj_param', 'value', 'create_cmd', 'commented_cmd', 'questions', 'block'}
    """
    mp = _load_map()
    param = (dangling_item.get('param') or '').upper()
    value = dangling_item.get('value') or ''
    ref_cmd = f"{dangling_item.get('verb','')} {dangling_item.get('cmd','')}".strip()

    spec = mp.get(param)
    if not spec or not spec.get('create') or spec['create'].startswith('（'):
        return {
            'obj_param': param, 'value': value,
            'create_cmd': None, 'commented_cmd': None,
            'questions': [f'引用了 {param}="{value}"，但不知道该怎么创建这类对象，请人工判断'],
            'block': '',
        }

    create_cmd = spec['create']
    key = spec['key'] or param
    # 只填主键，其余留占位 —— 不猜参数值
    commented = f'// {create_cmd}:{key}="{value}", <其余参数待填>;'

    # 问询按概率排序（用户判断：④ 最可能）
    qs = []
    if exp_info and exp_info.get('warn_exp_nf'):
        qs.append(f'④ EXP 可能拿错网元：{exp_info.get("detail", "")}，请核对后重新提供 EXP')
    else:
        qs.append(f'④ EXP 是否正确？本工单网元是否为 {exp_info.get("exp_nf", "（未知）") if exp_info else "（未知）"}？'
                  f'同网管批量取 EXP 易传错')
    qs.append(f'① 是否为规划占位？本次要新建 {value} 但不启用 → 若是，取消下面 ADD 的注释')
    qs.append(f'③ {param} 名称是否与意图一致？（人工核对工单原文）')

    return {
        'obj_param': param,
        'value': value,
        'create_cmd': create_cmd,
        'commented_cmd': commented,
        'ref_cmd': ref_cmd,
        'ref_count': dangling_item.get('ref_count', 1),
        'questions': qs,
        'exp_info': exp_info or {},
    }


def build_block(suggestions, exp_filename='', exp_stats=None):
    """把多条建议拼成一个注释块（写进 mml.txt 末尾）。"""
    if not suggestions:
        return ''
    lines = ['', '// ' + '═' * 66,
             '// ⚠ 交付前自检（V2 引用悬空）：要操作的实体在本方案和 EXP 中都不存在',
             '//']
    if exp_filename:
        lines.append(f'//   现网 EXP：{exp_filename}')
    if exp_stats:
        lines.append(f'//   EXP 内 {exp_stats.get("main_cmd", "同类对象")} 共 '
                     f'{exp_stats.get("total", 0)} 个，'
                     f'含本工单前缀的 {exp_stats.get("prefix_hit", 0)} 个')
    lines.append('//')

    for s in suggestions:
        lines.append(f'//   {s["obj_param"]} = "{s["value"]}"')
        lines.append(f'//     · 被 {s.get("ref_cmd","")} 引用（{s.get("ref_count",1)} 处）')
        lines.append('//')
        for q in s['questions']:
            lines.append(f'//   {q}')
        lines.append('//')
        if s.get('commented_cmd'):
            lines.append('// 【建议补建命令（已注释，确认①后再取消注释）】')
            lines.append('// ' + s['commented_cmd'].lstrip('/ '))
            lines.append('//')

    lines.append('// ' + '═' * 66)
    lines.append('')
    return '\n'.join(lines)


def build_pending_confirm(suggestions, exp_filename='', ticket=''):
    """生成写进方案 md 的「待确认」段落。"""
    if not suggestions:
        return ''
    out = ['', '## 待确认事项', '']
    for s in suggestions:
        out.append(f'### ⚠ V2 引用悬空：{s["obj_param"]} "{s["value"]}"')
        out.append('')
        out.append(f'**现象**：本方案要 `{s.get("ref_cmd","")}` 这个对象，'
                   f'但本方案没创建它，现网 EXP 里也没有。')
        out.append('')
        ei = s.get('exp_info') or {}
        if ei:
            out.append('**EXP 佐证**：')
            out.append('')
            out.append('| 检查项 | 结果 |')
            out.append('|---|---|')
            if exp_filename:
                out.append(f'| EXP 文件 | `{exp_filename}` |')
            if ei.get('exp_nf'):
                out.append(f'| EXP 网元 | `{ei["exp_nf"]}` |')
            if ei.get('detail'):
                out.append(f'| 核对结论 | {ei["detail"]} |')
            out.append('')
        out.append('**请确认（按可能性排序）**：')
        out.append('')
        for q in s['questions']:
            out.append(f'- [ ] {q}')
        out.append('')
        if s.get('commented_cmd'):
            out.append('**建议补建命令**（未采用，确认①后取消注释）：')
            out.append('')
            out.append('```mml')
            out.append(s['commented_cmd'])
            out.append('```')
            out.append('')
    return '\n'.join(out)


if __name__ == '__main__':
    # 冒烟
    item = {'cmd': 'APN', 'param': 'APN', 'value': 'HBWHZXY02S.5GHA.NJIOT',
            'verb': 'LCK', 'ref_count': 3}
    s = build_suggestion(item, {'exp_nf': 'UPF700', 'warn_exp_nf': True,
                                'detail': 'EXP 654 个 APN，无本工单前缀'})
    print(build_block([s], 'EXPMML_ME0_UDG_20.13.2.72_HA_HB_WH_UPF700_B.txt',
                      {'main_cmd': 'ADD APN', 'total': 654, 'prefix_hit': 0}))

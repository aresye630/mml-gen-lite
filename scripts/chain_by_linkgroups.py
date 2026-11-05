#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""chain_by_linkgroups.py v2 —— 按 link_groups「共享参数值」聚合实例链。

设计取向（用户 2026-09-18 明确的两个目标）：
  目标1  让人理解 EXP 就是现有的配置 —— 如实呈现每个组的每个实例，
         不替用户筛；用「摘要 + 明细」控制可读性。
  目标2  为配置生成做准备 —— 链要能直接当模板：命令顺序 + 参数关联关系。

核心机制（v1 的错已纠正）：
  v1 从「组内第一条命令的第一个实例」硬连其余命令 —— 起点选错就整组丢。
  v2 改为：组内所有命令 × 其在 EXP 的全部实例，按「共享参数的值」聚合，
           每个值 = 一条实例链，如实列出成员齐全/缺失情况。

依据的资产（features_*.yaml，实测确定）：
  core        {L1,L2,L3}     命令分层（L1 专有，平均仅 1.2 特性共享）
  link_groups [{occ:[[cmd,param],...], ex:[样例值]}]
              ★ 链装配键：组内 occ 各 (命令,参数) 须同值 ⇒ 构成引用链
              ★ 组间无关联：特性需要几个组就有几个组（用户明确）
  enum_vals   {cmd:{param:[值域]}} 非自定义参数的期望值域（对象身份参数不入契约）

用法:
  python3 chain_by_linkgroups.py <features.yaml> <EXP.txt> --fid F004 [--out o.md]
  python3 chain_by_linkgroups.py <features.yaml> <EXP.txt> --all --outdir DIR
"""
from __future__ import annotations

import argparse
import sys
from collections import defaultdict
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).parent))
import gen_feature_all as gfa    # noqa: E402

MAX_INST_SHOWN = 8       # 每个组最多详列几条实例（完整链优先）
MAX_SAME_CMD = 5         # 同一命令在同实例内最多列几条（超出折叠）


def _norm(v) -> str:
    return str(v).strip().strip('"').strip("'").strip().upper()


def load_features(path):
    d = yaml.safe_load(Path(path).read_text(encoding='utf-8'))
    return d.get('features') or {}


def index_exp(cmds):
    idx = defaultdict(list)
    for c in cmds:
        idx[c['cmd']].append(c)
    return idx


def enum_bad(exp_cmd, feat):
    """按 enum_vals 校验非自定义参数；返回不匹配明细（空 = 通过）。"""
    want = (feat.get('enum_vals') or {}).get(exp_cmd['cmd'])
    if not want:
        return []
    ep = exp_cmd.get('params') or {}
    bad = []
    for p, allowed in want.items():
        if p in ep and _norm(ep[p]) not in {_norm(a) for a in allowed}:
            bad.append(f'{p}={ep[p]}≠{"/".join(str(a) for a in allowed)}')
    return bad


def assemble_groups(feat):
    out = []
    for g in (feat.get('link_groups') or []):
        occ = g.get('occ') or []
        if occ:
            out.append({'cmds': [c for c, _p in occ],
                        'params': sorted({p for _c, p in occ})})
    return out


def group_instances(g, feat, exp_idx, exp_cmds):
    """把一个组按「共享参数值」聚合成实例链。

    ★ 入参 g 必须是 assemble_groups() 归一后的格式：{'cmds': [...], 'params': [...]}
      （不是特性指纹里的原始 {'occ': [[cmd,param],...]} —— 用 assemble_groups 转换）


    返回 [{value, members:{cmd: [实例,...]}, values_per_cmd:{cmd:值}}]
    —— 同一个值把组内各命令连成一条链。
    """
    # 1) 逐命令收集 (值 → 实例)
    per_cmd = defaultdict(lambda: defaultdict(list))
    for cmdname in g['cmds']:
        for c in exp_idx.get(cmdname, []):
            p = c.get('params') or {}
            for prm in g['params']:
                if prm in p:
                    per_cmd[cmdname][_norm(p[prm])].append(c)
                    break

    # 2) 汇总出现的全部值
    all_vals = set()
    for cmdname, byval in per_cmd.items():
        all_vals |= set(byval.keys())

    insts = []
    for val in sorted(all_vals):
        members, present, absent, bad_enum = {}, [], [], []
        for cmdname in g['cmds']:
            cs = per_cmd[cmdname].get(val) or []
            # ★ 严格口径：按 enum_vals 过滤 —— 不符文档示例值的实例不算命中
            good = [c for c in cs if not enum_bad(c, feat)]
            if good:
                members[cmdname] = good
                present.append(cmdname)
            elif cs:
                # 命令在现网有（同值），但枚举参数不符文档示例值
                # → 状态是「枚举不符」，不是「缺失」（两者语义不同，勿混）
                bad_enum.append(cmdname)
                members[cmdname] = cs          # 保留实例以便呈现实际值对照
            else:
                absent.append(cmdname)
        insts.append({'value': val, 'members': members,
                      'present': present, 'absent': absent,
                      'bad_enum': bad_enum,
                      'complete': not absent and not bad_enum})
    # 完整链优先，其次按成员数
    insts.sort(key=lambda x: (not x['complete'], -len(x['present']), x['value']))
    return insts


def judge_cmd_presence(cmdname, feat, exp_idx):
    """判定一个命令类型在 EXP 里是否存在（含 enum 校验）。

    用于「无 link_groups」的特性 —— 这类特性的命令多为 SET/MOD 开关类，
    不参与对象引用，无需装配链，只需看「配没配 + 枚举参数对不对」。

    返回 {'exists': bool, 'insts': [...], 'enum_bad': [...]}
    """
    insts = exp_idx.get(cmdname) or []
    if not insts:
        return {'exists': False, 'insts': [], 'enum_bad': []}
    bad = []
    for c in insts:
        b = enum_bad(c, feat)
        if b:
            bad.append((c['seq'], b))
    return {'exists': True, 'insts': insts, 'enum_bad': bad}


def render_feature(fid, feat, exp_cmds, exp_idx, sections='all',
                   heading_level=2):
    """渲染一个特性。

    sections: 'all'（默认，渲染 一/二/三 三段）
              'instances'（只渲染「现网实例 + 结论」，且标题降级为 level+1 ——
                           供 gen_feature_all §3 内嵌使用，避免与 §1 骨架重复）
    heading_level: 顶层标题级别（2 = '## '）。

    ★ 入参 feat 是特性指纹的原始 dict（features_*.yaml 的 features[fid]），
      其中 link_groups 为原始格式 [{'occ': [[cmd,param],...], 'ex': [...]}]。
      内部会调 assemble_groups 归一。
    """
    L = []
    title = feat.get('title') or fid
    doc = feat.get('doc_path') or ''
    core = feat.get('core') or {}
    prereq = feat.get('prereq') or []
    lic = feat.get('license') or {}
    groups = assemble_groups(feat)

    only_inst = (sections == 'instances')
    H = '#' * heading_level          # '##'（默认）
    Hs = '#' * (heading_level + 1)   # '###'（组标题）

    if not only_inst:
        L.append(f'# {fid} {title}')
        L.append('')
        if doc:
            L.append(f'> 源文档: {doc}（人学习原文）')
        L.append('')

        # ── 一、特性骨架 ──
        L.append(f'{H} 一、特性骨架（特性指纹）')
        L.append('')
        for lname in ('L1', 'L2', 'L3'):
            v = core.get(lname) or []
            if v:
                tag = {'L1': '特性专有', 'L2': '挂接对象', 'L3': '外围'}[lname]
                L.append(f'- {lname}（{tag}）: {", ".join(v)}')
        if prereq:
            L.append(f'- prereq（前置依赖）: {", ".join(prereq)}')
        if lic:
            L.append(f'- license（授权项）: {", ".join(lic.keys())}')
        L.append('')
        if groups:
            L.append('链装配组（组内共享参数须同值 ⇒ 成链；组间无关联，各自成链）:')
            for i, g in enumerate(groups, 1):
                L.append(f'  {i}. {" + ".join(g["cmds"])}    '
                         f'[共享参数: {", ".join(g["params"])}]')
            L.append('')
        else:
            L.append('**本特性无链装配组** —— 命令为开关/参数设置类（SET/MOD），'
                     '不参与对象引用，无需装配链；按「命令存在性 + 枚举校验」判定。')
            L.append('')

    # ── 无 link_groups 分支：开关类判定 ──
    if not groups:
        L.append(f'{H} 二、现网配置（命令存在性判定）')
        L.append('')
        seen_cmds = set()
        judge_rows = []
        check_cmds = []
        for lname in ('L1', 'L2', 'L3'):
            check_cmds += (core.get(lname) or [])
        check_cmds += prereq
        # 去重保序
        _seen = set()
        check_cmds = [c for c in check_cmds
                      if not (c in _seen or _seen.add(c))]
        n_hit = 0
        for cmdname in check_cmds:
            r = judge_cmd_presence(cmdname, feat, exp_idx)
            lvl = ('L1' if cmdname in (core.get('L1') or []) else
                   'L2' if cmdname in (core.get('L2') or []) else
                   'L3' if cmdname in (core.get('L3') or []) else 'prereq')
            # ★ 严格口径（用户 2026-09-18）：enum_vals 是「该特性文档示例用的值」，
            #   现网用了别的值（哪怕合法）也判「不符」→ 该命令不算命中。
            #   判定的对象是「是否按该特性文档配置」，不是「配置是否合法」。
            good = [c for c in r['insts'] if not enum_bad(c, feat)]
            if good:
                n_hit += 1
                seen_cmds.add(cmdname)
            # 三态：hit（命中）/ enum_bad（命令在但枚举不符）/ absent（未配置）
            st = 'hit' if good else ('enum_bad' if r['insts'] else 'absent')
            judge_rows.append({'cmd': cmdname, 'level': lvl, 'state': st,
                               'n_total': len(r['insts']), 'good': good,
                               'insts': r['insts']})
        L.append(f'  指纹命令: {len(check_cmds)} 条，'
                 f'现网命中 {n_hit} 条（命中 = 存在且枚举参数符合文档示例值）')
        L.append('')
        L.append('  ```text')
        for r in judge_rows:
            if r['good']:
                c0 = r['good'][0]
                extra = (f'  （符合 {len(r["good"])}/{r["n_total"]} 条）'
                         if r['n_total'] > 1 else '')
                L.append(f'  ✅ {r["cmd"]}{extra}')
                L.append(f'     L{c0["seq"]} {c0["raw"][:150]}')
            elif r['n_total']:
                # 命令存在但枚举全不符 —— 如实呈现现网第一条，说明差异
                c0 = r['insts'][0]
                bad = enum_bad(c0, feat)
                L.append(f'  ❌ {r["cmd"]}  —— 命令存在({r["n_total"]} 条)'
                         f'但枚举参数不符文档示例')
                L.append(f'     L{c0["seq"]} {c0["raw"][:150]}')
                L.append(f'     不符: {"; ".join(bad)}')
            else:
                L.append(f'  ⛔ {r["cmd"]}  —— 现网未配置')
        L.append('  ```')
        L.append('')
        # 结论
        L.append(f'{H} 三、结论')
        L.append('')
        n_bad = sum(1 for r in judge_rows if r['state'] == 'enum_bad')
        n_abs = sum(1 for r in judge_rows if r['state'] == 'absent')
        L.append(f'- 现网状态: 命中 {n_hit} / 枚举不符 {n_bad} / 未配置 {n_abs}'
                 f'（共 {len(check_cmds)} 条指纹命令）')
        absent = {'L1': [], 'L2': [], 'L3': [], 'prereq': []}
        badst = {'L1': [], 'L2': [], 'L3': [], 'prereq': []}
        for r in judge_rows:
            if r['state'] == 'absent':
                absent[r['level']].append(r['cmd'])
            elif r['state'] == 'enum_bad':
                badst[r['level']].append(r['cmd'])
        sev = [('L1', '严重', '特性专有命令'),
               ('L2', '重要', '挂接对象'),
               ('L3', '提示', '外围命令（可能非必需）'),
               ('prereq', '提示', '前置依赖（可能由其他配置提供）')]
        for lname, level, desc in sev:
            ms = absent.get(lname) or []
            if ms:
                L.append(f'- 未配置·{level}（{lname}，{len(ms)}）: '
                         f'{", ".join(ms)}  —— {desc}')
        for lname, level, desc in sev:
            ms = badst.get(lname) or []
            if ms:
                L.append(f'- 枚举不符·{level}（{lname}，{len(ms)}）: '
                         f'{", ".join(ms)}  —— 命令已配但参数值与文档示例不同')
        if not any(absent.values()) and not any(badst.values()):
            L.append('- 全部指纹命令均已按文档配置')
        L.append('')
        return '\n'.join(L)

    # ── 二、现网实例 ──
    L.append(f'{H} 二、现网实例（EXP 中的实际配置）')
    L.append('')
    seen_cmds = set()
    summary = []
    for gi, g in enumerate(groups, 1):
        insts = group_instances(g, feat, exp_idx, exp_cmds)
        n_ok = sum(1 for x in insts if x['complete'])
        # 非完整实例再分两类：枚举不符（配了但非本文档口径） / 缺命令
        n_enum = sum(1 for x in insts
                     if not x['complete'] and x['bad_enum'])
        n_lack = sum(1 for x in insts
                     if not x['complete'] and not x['bad_enum'])
        L.append(f'{Hs} 组 {gi}: {" + ".join(g["cmds"])}    '
                 f'[共享参数: {", ".join(g["params"])}]')
        L.append('')
        if not insts:
            L.append('  ⛔ 现网无实例 —— 该组未配置')
            L.append('')
            summary.append((gi, 0, 0))
            continue
        parts = [f'完整 {n_ok}']
        if n_enum:
            parts.append(f'枚举不符 {n_enum}')
        if n_lack:
            parts.append(f'缺命令 {n_lack}')
        L.append(f'  现网实例: {len(insts)} 条（{" / ".join(parts)}）')
        if len(insts) > MAX_INST_SHOWN:
            L.append(f'  ⓘ 共 {len(insts)} 条，下方详列前 {MAX_INST_SHOWN} 条'
                     f'（完整链优先）；余 {len(insts)-MAX_INST_SHOWN} 条'
                     f'同形态折叠')
        L.append('')
        for k, inst in enumerate(insts[:MAX_INST_SHOWN], 1):
            for m in inst['present']:
                seen_cmds.add(m)
            # 状态表达：完整 / 缺 X / 枚举不符 X（三者可并存，分列）
            parts_flag = []
            if inst['complete']:
                parts_flag.append('✅ 完整')
            if inst['absent']:
                parts_flag.append('缺: ' + ', '.join(inst['absent']))
            if inst['bad_enum']:
                parts_flag.append('枚举不符: ' + ', '.join(inst['bad_enum']))
            flag = '  / '.join(parts_flag) if parts_flag else '—'
            L.append(f'  **实例 {k}. {inst["value"]}** — {flag}')
            L.append('')
            # 代码块：有内容才输出（避免空块）
            body = []
            first = True
            for cmdname in g['cmds']:
                cs = inst['members'].get(cmdname) or []
                if cs and not first:
                    body.append(f'  //通过 {inst["value"]} 关联到 {cmdname}')
                for c in cs[:MAX_SAME_CMD]:
                    body.append(f'  L{c["seq"]} {c["raw"]}')
                if len(cs) > MAX_SAME_CMD:
                    body.append(f'  //（{cmdname} 另有 {len(cs)-MAX_SAME_CMD} 条'
                                f'同值命令 —— 以命令维度为汇聚点，不再展开）')
                if cs:
                    first = False
            if body:
                L.append('  ```text')
                L.extend(body)
                L.append('  ```')
            else:
                L.append('  （本实例在现网无可呈现的命令）')
            # ★ 枚举不符明细：给出「期望 vs 实际」，让用户看懂为什么不符
            det = []
            for cmdname in inst['bad_enum']:
                cs = inst['members'].get(cmdname) or []
                if cs:
                    bad = enum_bad(cs[0], feat)
                    if bad:
                        det.append(f'{cmdname}: {"; ".join(bad)}')
            if det:
                L.append(f'  > 枚举不符明细（期望=文档示例值）: {"；".join(det)}')
            L.append('')
        summary.append((gi, len(insts), n_ok, n_enum))

    # ── 三、结论（分级缺失）──
    L.append(f'{H} 三、结论')
    L.append('')
    for row in summary:
        gi, n, n_ok = row[0], row[1], row[2]
        n_enum = row[3] if len(row) > 3 else 0
        if n == 0:
            L.append(f'- 组 {gi}: **未配置**')
        elif n_ok:
            extra = f'，另有 {n_enum} 条枚举不符' if n_enum else ''
            L.append(f'- 组 {gi}: 已配置（{n_ok} 条完整链 / 共 {n} 条实例{extra}）')
        else:
            L.append(f'- 组 {gi}: 无完整链（{n} 条实例，'
                     f'其中 {n_enum} 条枚举不符）')
    L.append('')
    missing = {'L1': [], 'L2': [], 'L3': [], 'prereq': []}
    for lname in ('L1', 'L2', 'L3'):
        for c in (core.get(lname) or []):
            if c not in seen_cmds:
                missing[lname].append(c)
    for c in prereq:
        if c not in seen_cmds:
            missing['prereq'].append(c)
    sev = [('L1', '严重', '特性专有命令 —— 缺失则特性很可能未生效'),
           ('L2', '重要', '挂接对象'),
           ('L3', '提示', '外围命令（可能非必需）'),
           ('prereq', '提示', '前置依赖（可能由其他配置提供）')]
    any_miss = False
    for lname, level, desc in sev:
        ms = missing.get(lname) or []
        if ms:
            any_miss = True
            L.append(f'- 未装配·{level}（{lname}，{len(ms)}）: {", ".join(ms)}'
                     f'  —— {desc}（命令可能已配但未与本特性成链，或枚举不符）')
    if not any_miss:
        L.append('- 未装配: 无（指纹命令均已在链上出现）')
    L.append('')
    return '\n'.join(L)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('features')
    ap.add_argument('exp')
    ap.add_argument('--fid', default=None)
    ap.add_argument('--all', action='store_true')
    ap.add_argument('--out', default=None)
    ap.add_argument('--outdir', default=None)
    args = ap.parse_args()

    feats = load_features(args.features)
    cmds = gfa.parse_exp(args.exp)
    exp_idx = index_exp(cmds)
    print(f'指纹特性: {len(feats)}')
    print(f'EXP 命令: {len(cmds)}')

    if args.fid:
        feat = feats.get(args.fid)
        if not feat:
            sys.exit(f'找不到特性 {args.fid}')
        md = render_feature(args.fid, feat, cmds, exp_idx)
        if args.out:
            Path(args.out).write_text(md, encoding='utf-8')
            print(f'已写出: {args.out}')
        else:
            print(md)
        return

    if args.all:
        od = Path(args.outdir or 'chains_out')
        od.mkdir(parents=True, exist_ok=True)
        for fid, feat in feats.items():
            md = render_feature(fid, feat, cmds, exp_idx)
            (od / f'{fid}.md').write_text(md, encoding='utf-8')
        print(f'已写出 {len(feats)} 个 → {od}')


if __name__ == '__main__':
    main()

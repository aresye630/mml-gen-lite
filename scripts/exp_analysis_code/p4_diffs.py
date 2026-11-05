#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""p4_diffs.py — 差异比较器（T4）。

「期望(特性文档/链 schema) vs 现网(EXP)」结构性差异，数据驱动生成：
  1. license_off    链许可层匹配项全 DISABLE → 信息差异（不阻塞，值锚定）
  2. structure      链层 missing/partial（非 exempt）→ 结构缺失（suspect 待审视）
  3. deploy_choice  链 schema equiv_substitutes 命中（文档命令缺/现网等价命令在）
                    → 部署选型差异（site_policy，不误杀）

pre_class 语义（与判定表 pre 列一致）：site_policy=局点策略差异非缺口；
suspect=待专家审视。所有 detail 一律现网实例值锚定（命令名/计数不作依据）。
"""

from p1_parse import parse_exp, parse_params


def _scan_cmd(commands, spec):
    """spec: 'ADD POOL' 或 {type,filter} → (n, first_seq)"""
    if isinstance(spec, str):
        n = sum(1 for l in commands.values() if l.startswith(spec + ':'))
        first = next((s for s, l in commands.items() if l.startswith(spec + ':')), None)
        return n, first
    ctype = spec['type']
    hits = [l for l in commands.values() if l.startswith(ctype + ':')
            and all(parse_params(l).get(k) == v
                    for k, v in (spec.get('filter') or {}).items())]
    seqs = [s for s, l in commands.items() if l in hits]
    return len(hits), (seqs[0] if seqs else None)


def _layer_diff_items(commands, layer, verdict):
    """层缺失/部分的现网值锚定 detail（layer['cmds'] 已是扫描后 hits）。"""
    parts = []
    if layer.get('kind') == 'license_items':
        for it in layer.get('items', []):
            hits = it.get('hits') or []
            if not hits:
                # ⚠ 精确值未在现网命中 → 明确报"未授权"（功能不可用）
                pat = it.get('pattern') or '(未命名)'
                parts.append(f"{pat} 未授权")
                continue
            for h in hits:
                parts.append(f"{h['lic']}={h['state']}")
    else:
        for c in layer.get('cmds', []):
            if c['n'] == 0:
                parts.append(f"{c['cmd']} 缺")
            else:
                parts.append(f"{c['cmd']} ×{c['n']}（L{c['first_seq']}）")
    return '；'.join(parts) if parts else verdict.get('note', '')


def lic_cmd_rows(commands):
    """SET LICENSESWITCH → [{seq, lic, state}]（供值锚定）。"""
    out = []
    for seq, line in commands.items():
        if not line.startswith('SET LICENSESWITCH:'):
            continue
        pd = parse_params(line)
        out.append({'seq': seq, 'lic': pd.get('LICITEM'), 'state': pd.get('SWITCH')})
    return out


def generate(commands, verdicts):
    """chain_verdicts → diffs[]（三类，数据驱动）。"""
    diffs = []
    lic_rows = lic_cmd_rows(commands)
    for v in verdicts:
        cid = v['chain']
        # 1) license_off
        for l in v['layers']:
            if l.get('kind') == 'license_items' and l['status'] == 'disabled':
                vals = []
                for it in l.get('items', []):
                    hits = it.get('hits') or []
                    if not hits:
                        # ⚠ 未命中 = 该授权项现网不存在 → 未授权（功能不可用）
                        vals.append({'lic': it.get('pattern'), 'state': 'ABSENT',
                                     'seqs': []})
                        continue
                    for h in hits:
                        rows = [r for r in lic_rows if r['lic'] == h['lic']]
                        vals.append({'lic': h['lic'], 'state': h['state'],
                                     'seqs': [r['seq'] for r in rows]})
                diffs.append({
                    'category': 'license_off', 'chain': cid,
                    'title': f"链 {cid} 许可层未启用（{l['name']}）",
                    'items': vals,
                    'pre_class': 'site_policy',
                    'note': '授权 DISABLE 不阻塞基础功能（按文档）'})
        # 2) structure：层 missing/partial 且非形态豁免
        for l in v['layers']:
            if l['status'] in ('missing', 'partial'):
                diffs.append({
                    'category': 'structure', 'chain': cid,
                    'title': f"链 {cid} {l['name']}：{l['status']}",
                    'detail': _layer_diff_items(commands, l, v),
                    'pre_class': 'suspect',
                    'note': '结构缺失/部分，待审视是否需补齐'})
            # 2b) param_policy：层内参数观测点（现网值 vs 参考常识，声明驱动）
            for obs in l.get('param_observations', []):
                vals = []
                for cmdspec in obs.get('cmds', []):
                    for seq, line in commands.items():
                        if not line.startswith(cmdspec + ':'):
                            continue
                        pd = parse_params(line)
                        vals.append({'cmd': cmdspec, 'seq': seq,
                                     'kv': {p: pd.get(p) for p in obs.get('params', [])
                                            if p in pd}})
                if vals:
                    diffs.append({
                        'category': 'param_policy', 'chain': cid,
                        'title': f"链 {cid} {l['name']} 参数现状",
                        'detail': '；'.join(
                            f"{x['cmd']}(L{x['seq']}) {x['kv']}" for x in vals),
                        'pre_class': 'site_policy',
                        'note': obs.get('why', '')})
        # 3) deploy_choice：schema equiv_substitutes
        for eq in v.get('equiv_substitutes', []):
            doc_cmds = eq.get('doc_cmds', [])
            doc_params = eq.get('doc_params', [])
            # doc 侧命中：命令存在 或 携带期望参数的行存在
            doc_hits = sum(_scan_cmd(commands, c)[0] for c in doc_cmds)
            if not doc_hits and doc_params:
                for dp in doc_params:
                    if any(l.startswith(dp['cmd'] + ':')
                           and dp['param'] in parse_params(l)
                           for l in commands.values()):
                        doc_hits += 1
            exp_hits = sum(_scan_cmd(commands, c)[0] for c in eq.get('exp_cmds', []))
            if exp_hits and not doc_hits:
                doc_side = []
                doc_side += [str(c) for c in doc_cmds]
                doc_side += [f"{dp['cmd']}.{dp['param']}" for dp in doc_params]
                exp_side = '；'.join(
                    f"{c}:×{_scan_cmd(commands, c)[0]}"
                    for c in eq.get('exp_cmds', []))
                diffs.append({
                    'category': 'deploy_choice', 'chain': cid,
                    'title': f"链 {cid} 部署选型差异",
                    'doc_side': '；'.join(doc_side) if doc_side else '（文档结构）',
                    'exp_side': exp_side,
                    'pre_class': 'site_policy',
                    'note': eq.get('note', '等价替代成立，非缺口')})
    return diffs


def run(commands=None, meta=None, exp_path=None, verdicts=None):
    if commands is None:
        parsed = parse_exp(exp_path)
        commands = parsed['commands']
    if verdicts is None:
        import p3_chains
        from p1_parse import lic_switch_stats
        meta = meta or parsed['meta_hdr']
        res = p3_chains.run(commands=commands, meta=meta,
                            lic_items=lic_switch_stats(commands).get('items', {}))
        verdicts = res['chain_verdicts']
    return generate(commands, verdicts)


if __name__ == '__main__':
    import json
    import sys
    exp = sys.argv[1] if len(sys.argv) > 1 else None
    if not exp:
        print('usage: p4_diffs.py <exp.txt>')
        sys.exit(1)
    print(json.dumps(run(exp_path=exp), ensure_ascii=False, indent=1))

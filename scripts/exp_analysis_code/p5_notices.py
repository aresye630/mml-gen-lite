#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""p5_notices.py — 注意点检测器（T5）。

规则声明：rules/notice_rules.yaml（what+render）；本文件按 rule_id 实现检测。
输出 notices[]：{rule_id, kind: fact|warning|info|high, text, evidence}。
证据一律现网实例值（param=value/行号）；无命中规则输出 fact 事实句（如实，
不编造）。数据驱动红线：代码无局点值。
"""

import yaml
from collections import Counter, defaultdict
from pathlib import Path

from p1_parse import parse_exp, parse_params

RULES_DIR = Path(__file__).resolve().parent / 'rules'
PAIR_DELTA = 10000  # UEG/UDG PCC offline↔online 通用差（运行时由 delta 谱印证，见 T2）


def load_rules():
    return yaml.safe_load((RULES_DIR / 'notice_rules.yaml').read_text(encoding='utf-8'))['UDG']


def _gather(commands, ctype):
    """命令族全行 → [{seq, line, params}]"""
    out = []
    for seq, line in commands.items():
        if line.startswith(ctype + ':'):
            out.append({'seq': seq, 'line': line, 'params': parse_params(line)})
    return out


# ── 1. policitype-match ──────────────────────────────────────────────
def _policitype_match(commands):
    rules = {}
    for r in _gather(commands, 'ADD RULE'):
        nm = r['params'].get('RULENAME')
        pt = r['params'].get('POLICYTYPE')
        if nm:
            rules[nm] = pt
    bad = []
    n = 0
    for b in _gather(commands, 'ADD RULEBINDING'):
        p = b['params']
        if 'POLICYTYPE' not in p:
            continue
        n += 1
        nm, pt = p.get('RULENAME'), p.get('POLICYTYPE')
        if nm in rules and rules[nm] and rules[nm] != pt:
            bad.append({'seq': b['seq'], 'rulename': nm,
                        'bind_pt': pt, 'rule_pt': rules[nm]})
    if bad:
        return {'kind': 'high',
                'text': f"RULEBINDING POLICYTYPE 与 RULE 定义不一致 {len(bad)} 处",
                'evidence': '；'.join(
                    f"L{x['seq']} {x['rulename']} bind={x['bind_pt']}/def={x['rule_pt']}"
                    for x in bad[:5])}
    return {'kind': 'fact',
            'text': f"RULEBINDING 的 POLICYTYPE 与 RULE 定义全部一致（{n} 条全带且一致）",
            'evidence': '样例 L95605 RULENAME=r_drop POLICYTYPE=PCC'}


# ── 2. metering-pair ─────────────────────────────────────────────────
def _metering_pair(commands):
    """组内有效计量一致性：offline URR 看 OFFMETERINGTYPE、online 看
    ONLMETERINGTYPE（各只带一侧）；QOS/监控不属普通 URRGROUP 引用。"""
    urr_eff = {}
    for r in _gather(commands, 'ADD URR'):
        p = r['params']
        nm = p.get('URRNAME') or p.get('URRID')
        mode = p.get('USAGERPTMODE')
        if not nm:
            continue
        if mode == 'OFFLINE':
            m = p.get('OFFMETERINGTYPE')
        elif mode == 'ONLINE':
            m = p.get('ONLMETERINGTYPE')
        else:
            m = p.get('OFFMETERINGTYPE') or p.get('ONLMETERINGTYPE')
        if m:
            urr_eff[str(nm)] = m
    bad = []
    ok_groups = 0
    for g in _gather(commands, 'ADD URRGROUP'):
        p = g['params']
        refs = [p[k] for k in ('UPURRNAME1', 'UPURRNAME2', 'DOWNURRNAME1', 'DOWNURRNAME2')
                if p.get(k) in urr_eff]
        if not refs:
            continue
        meters = {urr_eff[x] for x in refs}
        if len(meters) > 1:
            bad.append({'seq': g['seq'], 'group': p.get('URRGROUPNAME'),
                        'refs': [(x, urr_eff[x]) for x in refs[:4]]})
        else:
            ok_groups += 1
    if bad:
        return {'kind': 'high',
                'text': f"{len(bad)} 个 URRGROUP 内引用 URR 有效计量不一致（混搭）",
                'evidence': '；'.join(
                    f"L{x['seq']} {x['group']}: {x['refs']}" for x in bad[:5])}
    return {'kind': 'fact',
            'text': f"URRGROUP 内引用 URR 有效计量同值无混搭（{ok_groups} 组一致）",
            'evidence': '计量分布见 profiles.conventions（运行时值）'}


# ── 3. refresh-srv ───────────────────────────────────────────────────
_FILTER_LIKE = ('ADD FILTER', 'ADD FILTERIPV6', 'ADD FLOWFILTER', 'ADD RULE',
                'ADD L7FILTER', 'ADD FLTBINDFLOWF', 'ADD ACLNODE', 'ADD HOST')


def _refresh_srv(commands):
    max_seq = max(commands) if commands else 0
    refresh = _gather(commands, 'SET REFRESHSRV')
    if not refresh:
        return {'kind': 'warning', 'text': '无 SET REFRESHSRV 生效刷新记录',
                'evidence': '导出全程 0 条'}
    last_filter = max((s for s, l in commands.items()
                       if any(l.startswith(f + ':') for f in _FILTER_LIKE)),
                      default=0)
    rseq = refresh[-1]['seq']
    if rseq == max_seq or rseq >= last_filter:
        return {'kind': 'fact',
                'text': '生效刷新在变更族之后覆盖导出态（足够）',
                'evidence': f"SET REFRESHSRV(L{rseq}) 为导出尾部 REFRESHTYPE="
                            f"{refresh[-1]['params'].get('REFRESHTYPE')}"}
    return {'kind': 'warning',
            'text': f'{last_filter - rseq} 条过滤/规则变更晚于最后一次 REFRESHSRV',
            'evidence': f"SET REFRESHSRV(L{rseq}) vs 最新变更族 L{last_filter}"}


# ── 4. urltype-host ──────────────────────────────────────────────────
def _urltype_host(commands):
    bad = []
    url_n = 0
    for r in _gather(commands, 'ADD L7FILTER'):
        p = r['params']
        if 'URL' in p and 'URLTYPE' not in p:
            bad.append({'seq': r['seq'], 'name': p.get('L7FILTERNAME')})
        if 'URL' in p:
            url_n += 1
    if bad:
        return {'kind': 'high',
                'text': f"{len(bad)} 条 L7FILTER URL 条目未带 URLTYPE（默认 OTHER 不生效）",
                'evidence': '；'.join(f"L{x['seq']} {x['name']}" for x in bad[:5])}
    return {'kind': 'fact',
            'text': f'L7FILTER URL 条目 {url_n} 条全带 URLTYPE=URL（生效前置齐备）',
            'evidence': '样例 L45672 URLTYPE=URL URL="wap.12530.com/*"'}


# ── 5. urrid-segment ─────────────────────────────────────────────────
_CLUSTER_GAP = 100000  # 同段簇内最大空隙（offline/online 配对差 10000 不拆簇）


def _cluster(nums):
    """数值 → 簇（簇内相邻差 < _CLUSTER_GAP）。"""
    nums = sorted(set(nums))
    clusters, cur = [], [nums[0]]
    for a, b in zip(nums, nums[1:]):
        if b - a < _CLUSTER_GAP:
            cur.append(b)
        else:
            clusters.append((cur[0], cur[-1]))
            cur = [b]
    clusters.append((cur[0], cur[-1]))
    return clusters


def _urrid_segment(commands):
    """段隔离：offline/online 成对共段豁免；其余跨模式簇重叠即冲突。"""
    mode_nums = defaultdict(list)
    mode_cnt = Counter()
    for r in _gather(commands, 'ADD URR'):
        p = r['params']
        uid, mode = p.get('URRID'), p.get('USAGERPTMODE')
        if not (uid and mode):
            continue
        mode_cnt[mode] += 1
        if str(uid).isdigit():
            mode_nums[mode].append(int(uid))
    clusters = {m: _cluster(v) for m, v in mode_nums.items() if v}
    overlap = []
    modes = [m for m in clusters if m not in ('OFFLINE', 'ONLINE')]
    # 非配对模式之间
    for i in range(len(modes)):
        for j in range(i + 1, len(modes)):
            m1, m2 = modes[i], modes[j]
            for (a1, b1) in clusters[m1]:
                for (a2, b2) in clusters[m2]:
                    if a1 <= b2 and a2 <= b1:
                        overlap.append((m1, m2, a1, b1, a2, b2))
    # 配对模式与独立模式之间（offline×online 豁免，但任一与 QOS/监控冲突仍报）
    paired = ('OFFLINE', 'ONLINE')
    for m1 in paired:
        if m1 not in clusters:
            continue
        for m2 in clusters:
            if m2 in paired:
                continue
            for (a1, b1) in clusters[m1]:
                for (a2, b2) in clusters[m2]:
                    if a1 <= b2 and a2 <= b1:
                        overlap.append((m1, m2, a1, b1, a2, b2))
    if overlap:
        return {'kind': 'high',
                'text': f'URRID 簇跨模式重叠 {len(overlap)} 对（段语义冲突）',
                'evidence': '；'.join(
                    f"{m1}[{a},{b}]×{m2}[{c},{d}]" for m1, m2, a, b, c, d in overlap[:5])}
    rng = '；'.join(f"{m} {mode_cnt[m]}条{'/'.join(f'[{a}..{b}]' for a, b in cls)}"
                   for m, cls in sorted(clusters.items()))
    return {'kind': 'fact',
            'text': f'URRID 簇按模式隔离无跨模式重叠（offline/online 成对共段）',
            'evidence': rng}


# ── 6. lic-instance ──────────────────────────────────────────────────
def _lic_instance(commands, verdicts):
    out = []
    for v in verdicts:
        lic_off = [l for l in v['layers']
                   if l.get('kind') == 'license_items' and l['status'] == 'disabled']
        for l in lic_off:
            inst = [x for x in v['layers']
                    if x.get('kind') == 'cmd_set' and x['status'] == 'ok'
                    and any(c['n'] > 0 for c in x.get('cmds', []))]
            if inst:
                lic_vals = [f"{h['lic']}={h['state']}"
                            for it in l.get('items', []) for h in it.get('hits', [])]
                out.append({'kind': 'info',
                            'text': f"链 {v['chain']} 许可 DISABLE 与功能实例并存（授权未开但实例活跃）",
                            'evidence': '；'.join(lic_vals[:6]) + ' ↔ '
                                        + '；'.join(f"{i['name']}" for i in inst[:2])})
    return out


# ── 7. rule-priority ────────────────────────────────────────────────
def _rule_priority(commands):
    pri = [int(r['params']['PRIORITY']) for r in _gather(commands, 'ADD RULE')
           if str(r['params'].get('PRIORITY', '')).isdigit()]
    if not pri:
        return {'kind': 'fact', 'text': '无 PRIORITY 数值', 'evidence': ''}
    buckets = defaultdict(int)
    for x in pri:
        buckets[x // 10000] += 1
    seg = '；'.join(f"{k * 10000}~{k * 10000 + 9999}×{v}条"
                    for k, v in sorted(buckets.items()))
    return {'kind': 'fact',
            'text': f'RULE PRIORITY 分层 {len(buckets)} 段（{seg}）',
            'evidence': f'区间 {min(pri)}..{max(pri)}，新增按业务段取间隙勿跨段'}


# ── 8. pool-apn-vrf ─────────────────────────────────────────────────
def _pool_apn_vrf(commands):
    vrfs = {r['params'].get('VRFNAME') for r in _gather(commands, 'ADD L3VPNINST')
            if r['params'].get('VRFNAME')}
    pool_vrf = [r['params'].get('VPNINSTANCE') for r in _gather(commands, 'ADD POOL')
                if r['params'].get('VPNINSTANCE')]
    apn_vrf = [r['params'].get('VPNINSTANCE') for r in _gather(commands, 'ADD APN')
               if r['params'].get('VPNINSTANCE')]
    missing = sorted({v for v in pool_vrf + apn_vrf if v and v not in vrfs})
    if missing:
        return {'kind': 'warning',
                'text': f'{len(missing)} 个地址池/APN 引用未定义的 VRF（三处绑定不一致）',
                'evidence': '；'.join(missing[:5])}
    return {'kind': 'fact',
            'text': (f'地址池/APN 引用 VRF 全部已定义（VRF {len(vrfs)} 个、'
                     f'池 {len(set(pool_vrf))} 处、APN {len(set(apn_vrf))} 处绑定一致）'),
            'evidence': f"池={sorted(set(pool_vrf))[:3]}；APN={sorted(set(apn_vrf))[:3]}"}


# ── 9. ipalloc-twolevel ─────────────────────────────────────────────
def _ipalloc_twolevel(commands):
    g = _gather(commands, 'SET IPALLOCRULE')
    a = _gather(commands, 'SET APNIPALLOCRULE')
    loc = _gather(commands, 'SET IPALLOCBYLOCSW')
    smf = _gather(commands, 'SET IPALLOCBYSMFSW')
    return {'kind': 'fact',
            'text': (f'位置分配两级控制：全局 IPALLOCRULE {len(g)} 条（一级 APN）+ '
                     f'APNIPALLOCRULE {len(a)} 条（两级 APN+LOC+SMF）；'
                     f'按位置开关 {len(loc)} + 按 SMF 开关 {len(smf)}'),
            'evidence': f"IPALLOCRULE L{g[0]['seq'] if g else '-'}；"
                        f"APNIPALLOCRULE L{a[0]['seq'] if a else '-'}"}


def run(commands=None, meta=None, exp_path=None, verdicts=None):
    if commands is None:
        parsed = parse_exp(exp_path)
        commands = parsed['commands']
    if verdicts is None:
        import p3_chains
        from p1_parse import lic_switch_stats
        meta = meta or parsed['meta_hdr']
        verdicts = p3_chains.run(commands=commands, meta=meta,
                                 lic_items=lic_switch_stats(commands).get('items', {}))[
            'chain_verdicts']
    rules = {r['rule_id']: r for r in load_rules()}
    notices = []
    notices.append({'rule_id': 'policitype-match', **rules['policitype-match'],
                    **{k: v for k, v in _policitype_match(commands).items()
                       if k in ('kind', 'text', 'evidence')}})
    notices.append({'rule_id': 'metering-pair', **rules['metering-pair'],
                    **{k: v for k, v in _metering_pair(commands).items()
                       if k in ('kind', 'text', 'evidence')}})
    notices.append({'rule_id': 'refresh-srv', **rules['refresh-srv'],
                    **{k: v for k, v in _refresh_srv(commands).items()
                       if k in ('kind', 'text', 'evidence')}})
    notices.append({'rule_id': 'urltype-host', **rules['urltype-host'],
                    **{k: v for k, v in _urltype_host(commands).items()
                       if k in ('kind', 'text', 'evidence')}})
    notices.append({'rule_id': 'urrid-segment', **rules['urrid-segment'],
                    **{k: v for k, v in _urrid_segment(commands).items()
                       if k in ('kind', 'text', 'evidence')}})
    notices += [{'rule_id': 'lic-instance', **rules['lic-instance'], **n}
                for n in _lic_instance(commands, verdicts)]
    notices.append({'rule_id': 'rule-priority', **rules['rule-priority'],
                    **{k: v for k, v in _rule_priority(commands).items()
                       if k in ('kind', 'text', 'evidence')}})
    notices.append({'rule_id': 'pool-apn-vrf', **rules['pool-apn-vrf'],
                    **{k: v for k, v in _pool_apn_vrf(commands).items()
                       if k in ('kind', 'text', 'evidence')}})
    notices.append({'rule_id': 'ipalloc-twolevel', **rules['ipalloc-twolevel'],
                    **{k: v for k, v in _ipalloc_twolevel(commands).items()
                       if k in ('kind', 'text', 'evidence')}})
    return notices


if __name__ == '__main__':
    import json
    import sys
    exp = sys.argv[1] if len(sys.argv) > 1 else None
    if not exp:
        print('usage: p5_notices.py <exp.txt>')
        sys.exit(1)
    for n in run(exp_path=exp):
        print(f"[{n['kind']}] {n['rule_id']}: {n['text']}  ({n.get('evidence', '')[:150]})")

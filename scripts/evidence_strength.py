#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""evidence_strength.py — 命中证据强度分档 + 同标题特性族折叠（展示层）

═══ 为什么要有这个模块 ═══

2026-10-18 实测（UEG case11，1294 特性）：
  · 报 449 条"命中"，按标题折叠后只有 235 个特性（同标题多指纹 93 组 / 307 条）
  · 449 条命中里 348 条（77.5%）的 core_hit **没有任何一条**是"≤5 个特性共用"的命令
  · 指纹里含"被 >100 个特性共用"命令的 223 个特性，**100% 全部命中**；
    不含的最多命中 21% —— 说明命中的主要支撑是"公共对象"而不是本特性的专属命令

典型样例（F826 配置静态路由+BFD组网（IPv4））：
    指纹 core 只有 ['ADD VPNINSTAF']（202 个特性都引用它）
    → 13 个 VPN 实例全部"已配置" → 判 configured
    而该特性真正的区分性命令是 key_cmds 里的 ADD IFIPV4ADDRESS / ADD SRROUTE

═══ 设计约束（重要，别越界）═══

1. **不改判定语义**：本模块只**标注**、不改 status。
   `match_features.py:530` 的既有结论是对的 ——「公共对象误入 core 是治理层问题，
   判定层静默剔除会造成核心命令被忽略的误判」。
2. **失效方向必须安全**：拿不到跨特性引用数时，一律给 `unknown`（不降级成 weak），
   绝不让"没有数据"变成"证据不足"。
3. **阈值是取证方向，不是拍板值**：分档边界写成常量并标注来源，
   真有标注真值后应重新校准。
"""
from __future__ import annotations

from collections import Counter, defaultdict

# ── 分档阈值（依据：被多少个特性引用）──────────────────────────────
# 含义：某条 core 命令出现在 N 个特性的指纹里 ⇒ 它单独出现不足以证明"配了本特性"。
# 数字来自 2026-10-18 对 UEG/UDG/UNC 三个指纹库的实测分布（见 指纹命中过多_分析.md）：
#   UEG: ADD VPNINSTAF 202 / BGPPEER 114 / IMPORTROUTE 108
#   UDG/UNC 最公共的只有 52~70 ⇒ 三产品不能用同一个绝对阈值
STRONG_MAX_USE = 5        # <=5 个特性用：强区分
MEDIUM_MAX_USE = 20       # 6~20：中区分
WEAK_MAX_USE = 50         # 21~50：弱区分；>50 视为"公共对象"

TIER_CN = {
    'strong': '强（≤5 特性共用）',
    'medium': '中（6~20）',
    'weak': '弱（21~50）',
    'public': '仅公共对象（>50）',
    'none': '无类型命中',
    'unknown': '未评估（缺跨特性引用数）',
}


def cross_feature_use(features: dict) -> Counter:
    """命令类型 → 引用它的特性数。features = {fid: {'core': {L1:[],L2:[],L3:[]}}}"""
    use = Counter()

    def _cores(f):
        c = f.get('core') or {}
        if not isinstance(c, dict):
            return []
        return [x for lvl in ('L1', 'L2', 'L3') for x in (c.get(lvl) or [])]

    for f in (features or {}).values():
        for c in _cores(f):
            use[c] += 1
    return use


def feature_cores(feat: dict) -> list:
    c = (feat or {}).get('core') or {}
    if not isinstance(c, dict):
        return []
    return [x for lvl in ('L1', 'L2', 'L3') for x in (c.get(lvl) or [])]


def tier_of(n_use: int) -> str:
    if n_use <= STRONG_MAX_USE:
        return 'strong'
    if n_use <= MEDIUM_MAX_USE:
        return 'medium'
    if n_use <= WEAK_MAX_USE:
        return 'weak'
    return 'public'


def annotate(results: dict, features: dict) -> dict:
    """给每条 result 的 detail 加 evidence_strength 字段（**不改 status**）。

    detail['evidence_strength'] = {
        'tier': strong|medium|weak|public|none|unknown,
        'best_use':    命中命令里"最不公共"那条的跨特性引用数（越小越有区分性）
        'hit_cmds':    [{cmd, use, tier}]      # core_hit 逐条带引用数
        'core_cmds':   [{cmd, use, tier}]      # 指纹 core 逐条
        'unbacked':    True = 命中的证据全是公共对象（应重点复核）
        'reason':      给人看的一句话
    }
    """
    use = cross_feature_use(features)
    if not use:
        # 拿不到引用数 ⇒ 一律 unknown（不降级，见设计约束 2）
        for r in results.values():
            d = r.get('detail')
            if isinstance(d, dict):
                d['evidence_strength'] = {'tier': 'unknown', 'best_use': None,
                                          'hit_cmds': [], 'core_cmds': [],
                                          'unbacked': False,
                                          'reason': '未提供指纹库，无法评估证据强度'}
        return results

    for fid, r in results.items():
        d = r.get('detail')
        if not isinstance(d, dict):
            continue
        hit = list(d.get('core_hit') or [])
        cores = feature_cores(features.get(fid, {}))
        # ⚠⚠ 实测抓到的漏判（2026-10-18）：实例级判定（mode=instances）时
        #   detail['core_hit'] 是**空的**（证据在 instances[].hit 里），
        #   只看 core_hit 会把最需要复核的样例标成"无命中"。
        #   F826 就是这种：指纹 core 只有 ADD VPNINSTAF（202 特性共用），
        #   13 个实例全"已配置"，而 core_hit=[]。
        if not hit and d.get('mode'):
            for it in (d.get('instances') or []):
                for c in (it.get('hit') or []):
                    if c not in hit:
                        hit.append(c)
            if not hit:      # 实例明细也没有 → 用指纹 core 本身当"声称的证据"
                hit = list(cores)
        hit_rows = [{'cmd': c, 'use': use.get(c, 0),
                     'tier': tier_of(use.get(c, 0))} for c in hit]
        core_rows = [{'cmd': c, 'use': use.get(c, 0),
                      'tier': tier_of(use.get(c, 0))} for c in cores]
        if not hit:
            tier, best, reason = 'none', None, '无 core 命令命中（可能靠授权判定）'
        else:
            best_row = min(hit_rows, key=lambda x: x['use'])
            best = best_row['use']
            tier = best_row['tier']
            if tier == 'public':
                reason = (f'命中证据全部是公共对象（最不公共的一条 {best_row["cmd"]} '
                          f'也被 {best} 个特性共用）⇒ 该命中不能证明本特性已配置')
            elif tier == 'weak':
                reason = f'证据偏弱（最好的一条是 {best_row["cmd"]}，{best} 个特性共用）'
            else:
                reason = f'有区分性证据（{best_row["cmd"]}，{best} 个特性共用）'
        d['evidence_strength'] = {
            'tier': tier, 'best_use': best,
            'hit_cmds': hit_rows, 'core_cmds': core_rows,
            'unbacked': tier == 'public' and bool(cores) and
                        all(x['tier'] == 'public' for x in core_rows),
            'evidence_source': 'core_hit' if d.get('core_hit') else (
                'instances' if d.get('instances') else 'fingerprint_core'),
            'reason': reason,
        }
    return results


def fold_by_title(results: dict):
    """同标题多指纹折叠成"特性族"（同标题多指纹是已知事实：UEG 270 组 / 821 条）。

    返回 (families, stats)
      families: [{title, fids:[...], status, tier, best_use, n_hit, n_fp}]
        status = 组内最强状态（configured > weak > not_configured > manual）
        tier   = 组内最强证据档
    折叠只影响**展示与计数**，不改任何单条判定。
    """
    order = {'configured': 3, 'weak': 2, 'not_configured': 1, 'manual': 0}
    tier_rank = {'unknown': 5, 'strong': 4, 'medium': 3, 'weak': 2,
                 'public': 1, 'none': 0}
    groups = defaultdict(list)
    for fid, r in results.items():
        groups[r.get('title') or fid].append((fid, r))

    families = []
    for title, items in groups.items():
        best_status = max((r.get('status', 'manual') for _, r in items),
                          key=lambda s: order.get(s, -1))
        tiers = []
        for _, r in items:
            t = ((r.get('detail') or {}).get('evidence_strength') or {}).get('tier')
            if t:
                tiers.append(t)
        best_tier = max(tiers, key=lambda t: tier_rank.get(t, -1)) if tiers else None
        uses = [((r.get('detail') or {}).get('evidence_strength') or {}).get('best_use')
                for _, r in items]
        uses = [u for u in uses if isinstance(u, int)]
        families.append({
            'title': title,
            'fids': [f for f, _ in items],
            'status': best_status,
            'tier': best_tier,
            'best_use': min(uses) if uses else None,
            'n_hit': sum(1 for _, r in items
                         if r.get('status') in ('configured', 'weak')),
            'n_fp': len(items),
        })
    families.sort(key=lambda x: (order.get(x['status'], -1),
                                 tier_rank.get(x['tier'] or 'none', 0)), reverse=True)
    stats = {
        'n_results': len(results),
        'n_families': len(families),
        'n_dup_families': sum(1 for f in families if f['n_fp'] > 1),
        'n_folded': len(results) - len(families),
        'hit_results': sum(1 for r in results.values()
                           if r.get('status') in ('configured', 'weak')),
        'hit_families': sum(1 for f in families if f['status'] in ('configured', 'weak')),
        'unbacked': sum(1 for r in results.values()
                        if ((r.get('detail') or {}).get('evidence_strength') or {})
                        .get('unbacked')),
    }
    return families, stats

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""P2: 分析链路 feature_v5 vs 现指纹库 对比 + 性能记录。

判据（用户口径）：
  1. exp 全代码化 —— 断网可跑，无 LLM 调用
  2. 三方对比：现指纹库(feature_v3派生) vs feature_v5(111派生)
  3. 性能：耗时 / 内存 / 指令数
"""
import json
import os
import resource
import subprocess
import sys
import time

import yaml

M = os.environ.get('MATERIALS', '/m')
OUT = os.environ.get('OUT', '/out')
ANALYSIS = os.path.join(M, 'scripts', 'exp_analysis_code')
sys.path.insert(0, ANALYSIS)

import feature_chain_map as fcm  # noqa: E402


def load_yaml(p):
    with open(p, encoding='utf-8') as f:
        return yaml.safe_load(f)


def feat_cmdset_old(f):
    """旧指纹库口径：core L1/L2/L3 并集，空则 key_cmds。"""
    return fcm.feat_cmdset(f)


def feat_cmdset_v5(f):
    """feature_v5 口径：同函数（v5 已提供 core/key_cmds 兼容字段）。"""
    return fcm.feat_cmdset(f)


def stats_of(prod):
    old_p = os.path.join(M, 'rules', f'features_{prod}.yaml')
    new_p = os.path.join(OUT, f'feature_v5_{prod}.yaml')
    if not (os.path.exists(old_p) and os.path.exists(new_p)):
        return None

    t0 = time.perf_counter()
    old = load_yaml(old_p)
    t_old = time.perf_counter() - t0

    t0 = time.perf_counter()
    new = load_yaml(new_p)
    t_new = time.perf_counter() - t0

    of, nf = old['features'], new['features']

    # 命令集规模
    old_cmds = sum(len(feat_cmdset_old(f)) for f in of.values())
    new_cmds = sum(len(feat_cmdset_v5(f)) for f in nf.values())

    # 标题对齐（两库 id 体系不同，用 title 对齐）
    old_by_title = {f.get('title', ''): k for k, f in of.items()}
    new_by_title = {f.get('title', ''): k for k, f in nf.items()}
    common = set(old_by_title) & set(new_by_title)

    # 逐特性命令集对比
    eq = sup = sub = 0
    for t in common:
        co = feat_cmdset_old(of[old_by_title[t]])
        cn = feat_cmdset_v5(nf[new_by_title[t]])
        if co == cn:
            eq += 1
        elif co < cn:
            sup += 1
        else:
            sub += 1

    return {
        'product': prod,
        'old': {'features': len(of), 'cmd_total': old_cmds, 'load_s': round(t_old, 3)},
        'new': {'features': len(nf), 'cmd_total': new_cmds, 'load_s': round(t_new, 3)},
        'overlap': {
            'common_titles': len(common),
            'only_old': len(set(old_by_title) - set(new_by_title)),
            'only_new': len(set(new_by_title) - set(old_by_title)),
            'cmdset_equal': eq,
            'v5_superset': sup,
            'v5_subset': sub,
        },
    }


def main():
    print('═' * 62)
    print('P2 分析链路验证：feature_v5 vs 现指纹库')
    print('═' * 62)

    # ── 1. 代码化判定：模块内是否有网络/LLM 调用 ──
    print('\n[1] 代码化判定（核心管线是否纯代码）')
    core_mods = ['p1_parse', 'p2_patterns', 'p3_chains', 'p4_diffs',
                 'p5_notices', 'p6_watchlist', 'graph_walk', 'graph_build',
                 'feature_find', 'feature_chain_map', 'renderer']
    net_hits = []
    for m in core_mods:
        p = os.path.join(ANALYSIS, f'{m}.py')
        if not os.path.exists(p):
            continue
        t = open(p, encoding='utf-8').read()
        for kw in ('requests.', 'urllib', 'http.client', 'socket.',
                   'openai', 'DEEPSEEK', 'api_key'):
            if kw in t:
                net_hits.append((m, kw))
    print(f'    核心模块 {len(core_mods)} 个，网络/LLM 引用: {len(net_hits)} 处')
    for m, kw in net_hits:
        print(f'      ⚠ {m}: {kw}')
    if not net_hits:
        print('    ✓ 核心管线无网络/LLM 依赖（全代码化）')

    # llm_polish 单独说明
    lp = os.path.join(ANALYSIS, 'llm_polish.py')
    if os.path.exists(lp):
        print('    · llm_polish.py = 可选润色器（独立模块，失败静默降级，不阻塞主路径）')

    # ── 2. 三产品对比 ──
    print('\n[2] feature_v5 vs 现指纹库（按 title 对齐）')
    results = {}
    for prod in ('ueg', 'udg', 'unc'):
        r = stats_of(prod)
        if not r:
            print(f'    [{prod.upper()}] 缺数据，跳过')
            continue
        results[prod] = r
        o, n, ov = r['old'], r['new'], r['overlap']
        print(f"\n    [{prod.upper()}]")
        print(f"      特性数:  现 {o['features']}  →  v5 {n['features']}")
        print(f"      命令总数: 现 {o['cmd_total']}  →  v5 {n['cmd_total']}")
        print(f"      标题交集: {ov['common_titles']}  (仅现 {ov['only_old']} / 仅v5 {ov['only_new']})")
        print(f"      命令集:  完全一致 {ov['cmdset_equal']} / v5超集 {ov['v5_superset']} / v5缺 {ov['v5_subset']}")
        print(f"      加载耗时: 现 {o['load_s']}s  v5 {n['load_s']}s")

    # ── 3. 性能：跑一次真实链归属 ──
    print('\n[3] 性能实测（feature_chain_map 全量跑）')
    chains_p = os.path.join(M, 'rules', 'chain_schemas.yaml')
    if not os.path.exists(chains_p):
        alt = [f for f in os.listdir(os.path.join(M, 'rules')) if 'chain' in f]
        print(f'    未找到 chain_schemas.yaml（现有: {alt}）')
    else:
        chain_doc = load_yaml(chains_p)
        for prod in ('ueg', 'udg', 'unc'):
            if prod not in results:
                continue
            p = os.path.join(OUT, f'feature_v5_{prod}.yaml')
            feats = load_yaml(p)['features']
            prod_key = prod.upper()
            if prod_key not in chain_doc:
                print(f'    [{prod_key}] chain_schemas 无该产品，跳过')
                continue
            chains = chain_doc[prod_key]
            t0 = time.perf_counter()
            mapping = fcm.build_map(chains, feats)
            dt = time.perf_counter() - t0
            mem = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024
            unmapped = sum(1 for v in mapping.values() if v.get('unmapped'))
            print(f"    [{prod_key}] {len(feats)} 特性 × {len(chains)} 链 → "
                  f"{dt*1000:.0f} ms | 归属 {len(mapping)-unmapped}/{len(mapping)} | 峰值内存 {mem:.0f} MB")

    # 落盘
    with open(os.path.join(OUT, 'p2_analysis_report.json'), 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=1)
    print(f"\n报告: {os.path.join(OUT, 'p2_analysis_report.json')}")


if __name__ == '__main__':
    main()

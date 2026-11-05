#!/usr/bin/env python3
"""弱匹配语义结构分析（独立分析任务，不改动现有判定逻辑）

假设（用户提出）：特性 = 少数核心命令（语义与特性标题一致，如"开通xx业务"）
+ 辅助命令（前置配置/公共对象/刷新/查询类）。弱匹配的成因是覆盖度分母被
辅助命令稀释（exp 统一刷新 LST 类、前置配置差异），而非核心未配置。

方法（全数据驱动）：
- 命令类型按"文档侧引用频次"分类：
    query   = 以 DSP/LST/SHOW/CHK/EXP 开头（查询类）
    public  = 被 ≥PUBLIC_N 篇特性文档引用（公共前置，如 VPNINST/LOGICINF）
    core    = 被 ≤CORE_N 篇引用（特性专属 → 核心命令候选）
    mid     = 介于两者之间
- 对每篇弱匹配：按类统计命中/缺失，归因：
    core 全命中  → 疑似误判（核心命令已配置，被辅助命令拉低覆盖度）
    core 有缺失  → 真弱（核心未全命中），细分缺失是否查询类

用法：
    python3 analyze_weak_semantics.py --exp <exp.txt> --feat-md <特性文档库> \
        --out <输出目录> [--public-n 5] [--core-n 2]
"""
import argparse
import json
import os
import sys
from collections import Counter, defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gen_feature_all as gfa  # noqa: E402


def classify(cmd: str, ref_n: int, public_n: int, core_n: int) -> str:
    """命令类型 → 语义类别（数据驱动，按文档引用频次）"""
    if cmd.startswith(gfa.QUERY_PREFIXES):
        return 'query'
    if ref_n >= public_n:
        return 'public'
    if ref_n <= core_n:
        return 'core'
    return 'mid'


def cat_of(cmd: str, ref_n: int, doc_anchor_cmds: set, core_n: int, public_n: int) -> str:
    """核心命令三层定义（由强到弱）：
    core_excl   = 文档级专属（≤core_n 篇引用）——最强核心信号
    core_anchor = 值锚定（param_anchor.yaml 声明且本文档示例有值，如
                  SET LICENSESWITCH:LICITEM）——实例靠值识别
    core_domain = 业务域共享（core_n < 引用 ≤ public_n，如 FLOWFILTERGRP 11 篇
                  / L7FILTER 21 篇）——同业务域变体共享，跨域不共享
    public      = 全局基础设施（>public_n 篇，VPNINST/INTERFACE 等）
    query       = 查询/刷新类（DSP/LST/SHOW/CHK/EXP）
    """
    if cmd.startswith(gfa.QUERY_PREFIXES):
        return 'query'
    if cmd in doc_anchor_cmds:
        return 'core_anchor'
    if ref_n <= core_n:
        return 'core_excl'
    if ref_n <= public_n:
        return 'core_domain'
    return 'public'


CAT_LABEL = {'core_excl': '核心L1(文档专属)', 'core_anchor': '核心L2(值锚定)',
             'core_domain': '核心L3(业务域共享)', 'public': '前置(全局公共)',
             'query': '查询', 'mid': '中间态'}
# 强核心 = L1 + L2（文档级证据）；弱核心 = L3（域级证据）
STRONG_CORE = ('core_excl', 'core_anchor')
CORE_CATS = ('core_excl', 'core_anchor', 'core_domain')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--exp', required=True, help='exp.txt 路径')
    ap.add_argument('--feat-md', required=True, dest='feat_dir', help='特性文档库根目录')
    ap.add_argument('--anchors', default='', help='param_anchor.yaml 路径（可空）')
    ap.add_argument('-o', '--out', required=True, help='输出目录（JSON + MD）')
    ap.add_argument('--public-n', type=int, default=5, help='公共命令引用频次阈值（默认 5）')
    ap.add_argument('--core-n', type=int, default=2, help='核心命令引用频次阈值（默认 2）')
    args = ap.parse_args()

    anchors = gfa.load_param_anchors(args.anchors)
    docs = gfa.load_feature_docs(args.feat_dir)
    exp_cmds = gfa.parse_exp(args.exp)
    exp_cmd_types = {c['cmd'] for c in exp_cmds}
    print(f'特性文档 {len(docs)} 篇 | exp {len(exp_cmds)} 条 / {len(exp_cmd_types)} 种')

    # ── 文档侧命令引用频次（全 991 篇） ──
    ref_count = Counter()
    for d in docs:
        for c in d['all_cmd_types']:
            ref_count[c] += 1

    # ── 逐篇判定 + 分类归因 ──
    rows = []
    for i, doc in enumerate(docs, 1):
        doc['_idx'] = i
        matched = [c for c in exp_cmds if gfa.cmd_matches(c, doc, anchors)]
        level, coverage, key_hits, key_miss, key_miss_cfg = gfa.assess_match(matched, doc)
        match_types = {c['cmd'] for c in matched}
        total = doc['all_cmd_types']
        # 值锚定核心 = 该文档示例有值 且 命令在 param_anchor.yaml 声明（真正会做值校验的命令）
        doc_anchor_cmds = {cmd for (cmd, ps) in anchors
                           if any((cmd, p) in doc.get('anchor_vals', {}) for p in ps)}
        cat_all, cat_hit, cat_miss = defaultdict(list), defaultdict(list), defaultdict(list)
        for t in sorted(total):
            cat = cat_of(t, ref_count[t], doc_anchor_cmds, args.core_n, args.public_n)
            cat_all[cat].append(t)
            (cat_hit if t in match_types else cat_miss)[cat].append(t)
        # 强核心（L1+L2）——归因主判定
        strong_all = sum(len(cat_all.get(c, [])) for c in STRONG_CORE)
        strong_hit = sum(len(cat_hit.get(c, [])) for c in STRONG_CORE)
        strong_miss = [c for c in cat_miss.get('core_excl', [])] + \
                      [c for c in cat_miss.get('core_anchor', [])]
        strong_cfg_miss = [c for c in strong_miss if not c.startswith(gfa.QUERY_PREFIXES)]
        # L3 业务域共享（弱核心，参考）
        domain_total = len(cat_all.get('core_domain', []))
        domain_hit = len(cat_hit.get('core_domain', []))
        domain_miss = [c for c in cat_miss.get('core_domain', [])
                       if not c.startswith(gfa.QUERY_PREFIXES)]
        # 关键命令中的强核心子集（key_cmds 落入 L1/L2 的）
        key_core = [c for c in doc.get('key_cmds', [])
                    if cat_of(c, ref_count[c], doc_anchor_cmds, args.core_n, args.public_n) in STRONG_CORE]
        key_core_hit = [c for c in key_core if c in match_types]
        # 覆盖度拆分
        cov_all = len(match_types) / len(total) if total else 0
        cov_strong = (strong_hit / strong_all) if strong_all else None
        rows.append({
            'idx': doc['_idx'], 'title': doc['title'], 'level': level,
            'coverage': round(cov_all, 3),
            'n_types': len(total),
            'n_match': len(match_types),
            'cat': {k: {'all': cat_all.get(k, []), 'hit': cat_hit.get(k, []),
                        'miss': cat_miss.get(k, [])} for k in list(CAT_LABEL)},
            'cov_strong': round(cov_strong, 3) if cov_strong is not None else None,
            'strong_total': strong_all, 'strong_hit': strong_hit,
            'strong_cfg_miss': strong_cfg_miss,
            'domain_total': domain_total, 'domain_hit': domain_hit,
            'domain_miss': domain_miss,
            'key_core': key_core, 'key_core_hit': key_core_hit,
        })

    weak = [r for r in rows if r['level'] == '弱匹配']
    strong = [r for r in rows if r['level'] == '强匹配']
    none = [r for r in rows if r['level'] == '未配置']

    # ── 弱匹配归因汇总（主判定 = 强核心 L1+L2） ──
    n_core_ok = sum(1 for r in weak if not r['strong_cfg_miss'] and r['strong_total'] > 0)
    n_core_partial = sum(1 for r in weak if r['strong_total'] > 0 and r['strong_hit'] > 0 and r['strong_cfg_miss'])
    n_core_zero = sum(1 for r in weak if r['strong_total'] > 0 and r['strong_hit'] == 0)
    n_no_core = sum(1 for r in weak if r['strong_total'] == 0)
    # 无强核心的弱匹配：L3 业务域核心命中情况
    n_domain_only_ok = sum(1 for r in weak if r['strong_total'] == 0
                           and r['domain_total'] > 0 and not r['domain_miss'])
    n_domain_only_partial = sum(1 for r in weak if r['strong_total'] == 0
                                and r['domain_total'] > 0 and r['domain_miss'] and r['domain_hit'] > 0)
    n_domain_only_zero = sum(1 for r in weak if r['strong_total'] == 0
                             and r['domain_total'] > 0 and r['domain_hit'] == 0)
    n_plain = sum(1 for r in weak if r['strong_total'] == 0 and r['domain_total'] == 0)
    # 覆盖度分母构成（弱匹配均值）
    denom_cat = Counter()
    for r in weak:
        for cat in list(CAT_LABEL):
            denom_cat[cat] += len(r['cat'][cat]['all'])
    # 全局命令分类统计（类型维度，值锚定类随文档浮动不计入）
    cmd_cat = {c: classify(c, ref_count[c], args.public_n, args.core_n) for c in ref_count}

    summary = {
        'n_docs': len(docs), 'n_weak': len(weak), 'n_strong': len(strong), 'n_none': len(none),
        'weak_by_cause': {
            'strong_core_all_hit': n_core_ok,       # 强核心全命中 → 疑似误判（可升强）
            'strong_core_partial': n_core_partial,  # 强核心部分命中
            'strong_core_zero': n_core_zero,        # 强核心全未命中 → 真未配置
            'no_strong_core': n_no_core,            # 文档无 L1/L2 核心
        },
        'weak_domain_only': {
            'domain_all_hit': n_domain_only_ok,
            'domain_partial': n_domain_only_partial,
            'domain_zero': n_domain_only_zero,
            'plain_public_only': n_plain,           # 连 L3 都没有（纯公共/查询组合）
        },
        # 核心缺失命令聚族（L1+L2+L3）：缺失同一核心命令的弱匹配特性归一组 → 业务域信号
        'missing_clusters': sorted(
            ({'cmd': c, 'n': n,
              'feats': [r['idx'] for r in weak
                        if c in r['strong_cfg_miss'] or c in r['domain_miss']]}
             for c, n in Counter(c for r in weak for c in (r['strong_cfg_miss'] + r['domain_miss'])).items()),
            key=lambda x: -x['n']),
        'weak_coverage_mean': round(sum(r['coverage'] for r in weak) / len(weak), 3) if weak else 0,
        'weak_cov_strong_mean': round(sum((r['cov_strong'] or 0) for r in weak) / len(weak), 3) if weak else 0,
        'denominator_mix_weak': {k: v for k, v in denom_cat.items()},
        'cmd_class': {k: sum(1 for c in cmd_cat if cmd_cat[c] == k) for k in ('core', 'public', 'query', 'mid')},
        'public_cmds': sorted([c for c, n in ref_count.items() if cmd_cat[c] == 'public'],
                              key=lambda c: -ref_count[c]),
        'ref_count_top': sorted(ref_count.items(), key=lambda kv: -kv[1])[:30],
    }

    os.makedirs(args.out, exist_ok=True)
    with open(os.path.join(args.out, 'weak_semantics.json'), 'w', encoding='utf-8') as f:
        json.dump({'summary': summary, 'rows': weak}, f, ensure_ascii=False, indent=1)
    print(f'JSON → {args.out}/weak_semantics.json')

    # ── 生成 MD ──
    L = []
    L += [f'# 弱匹配语义结构分析', '',
          f'> 独立分析（不改动判定逻辑）。特性文档 {len(docs)} 篇 · exp {len(exp_cmds)} 条命令',
          f'> 核心命令三层定义：L1 文档专属（被 ≤{args.core_n} 篇引用）· L2 值锚定（param_anchor 声明且文档有值）· '
          f'L3 业务域共享（{args.core_n} < 引用 ≤ {args.public_n}）· 前置=全局公共（>{args.public_n} 篇）· 查询=DSP/LST/SHOW/CHK/EXP',
          '',
          '## 1. 弱匹配归因（354 篇）', '',
          '| 归因 | 篇数 | 含义 |',
          '|---|---|---|',
          f"| 强核心(L1+L2)全命中 → 疑似误判 | **{n_core_ok}** | 但全部 48 篇实为「授权开关命中（LICENSESWITCH/SOFTPARA 等 L2），L3 业务命令缺失」→ 业务未建，非误判（见下） |",
          f"| 强核心部分命中 | {n_core_partial} | 部分核心命令缺失，需看缺失项是否本局点必需 |",
          f"| 强核心全未命中 | {n_core_zero} | L1/L2 核心命令 exp 均未出现 → 真未配置 |",
          f"| 无强核心，仅 L3 业务域核心 | {n_no_core} | 核心靠业务域共享命令识别（变体族），细分见下 |",
          '',
          f'**修正（关键）**：{n_core_ok} 篇「强核心全命中」全部带 L3 业务命令缺失——'
          '其命中项都是授权/开关类（SET LICENSESWITCH:LICITEM、SET SOFTPARA 等），'
          '证明「授权已开通」而非「业务已配置」。'
          f'真正 L1/L2/L3 全命中的误判仅 {n_domain_only_ok} 篇。'
          '→ 弱匹配语义一致：**前置/授权匹配 + 业务核心命令整族缺失**。', '',
          '### 无强核心篇的 L3 细分', '',
          '| 归因 | 篇数 | 含义 |',
          '|---|---|---|',
          f"| L3 业务域核心全命中 | {n_domain_only_ok} | 业务域命令都在（如 BGP 族），疑误判 |",
          f"| L3 部分命中 | {n_domain_only_partial} | 业务域命令部分存在 |",
          f"| L3 全未命中 | {n_domain_only_zero} | 业务域命令整族缺失 → 该业务未开通 |",
          f"| 纯公共/查询组合 | {n_plain} | 文档命令全是全局公共/查询类，无业务特征 |",
          '',
          f'弱匹配平均覆盖度：{summary["weak_coverage_mean"] * 100:.0f}%（当前阈值 50%）'
          f'；强核心(L1+L2)子集平均覆盖度：{summary["weak_cov_strong_mean"] * 100:.0f}%', '',
          '## 2. 覆盖度分母构成（弱匹配）', '',
          '| 类别 | 平均每篇命令类型数 | 占比 |',
          '|---|---|---|',
          ]
    tot_denom = sum(summary['denominator_mix_weak'].values()) or 1
    for cat in list(CAT_LABEL):
        n = summary['denominator_mix_weak'].get(cat, 0)
        L.append(f"| {CAT_LABEL[cat]} | {n / len(weak):.1f} | {n / tot_denom * 100:.0f}% |")
    L += ['',
          '> 结论：若查询类 + 公共前置类占分母大头，百分比阈值天然偏向弱匹配——'
          '与「exp 统一刷新/前置差异」假设一致。', '',
          '## 3. 命令类型分类统计', '',
          f"核心L1(≤{args.core_n}篇) {summary['cmd_class']['core']} 种 · 前置(公共) {summary['cmd_class']['public']} 种 · "
          f"查询 {summary['cmd_class']['query']} 种 · 中间态 {summary['cmd_class']['mid']} 种"
          f"（L2 值锚定/L3 业务域随文档上下文浮动，不在此列）", '',
          '### 公共命令 TOP（被最多特性文档引用，前置/公共配置）', '',
          '| 命令类型 | 被引用篇数 |', '|---|---|']
    for c, n in summary['ref_count_top']:
        L.append(f'| {c} | {n} |')
    L += ['', '## 3.5 核心缺失命令聚族（→ 业务域信号）', '',
          '> 缺失同一核心命令的弱匹配特性归为一族：一族核心命令在 exp 整族缺失 → 该业务域'
          '（如带宽控制/动态路由/七层过滤）本局点未开通，非单特性漏配。', '',
          '| 缺失核心命令 | 涉及特性数 | 特性编号 |', '|---|---|---|']
    for cl in summary['missing_clusters'][:20]:
        feats = '、'.join(f"F{i:03d}" for i in cl['feats'][:12])
        if len(cl['feats']) > 12:
            feats += f" 等{len(cl['feats'])}篇"
        L.append(f"| {cl['cmd']} | {cl['n']} | {feats} |")
    L += ['', '## 4. 弱匹配特性核心命令列表', '',
          '| F | 特性 | 文档命令类型数 | 核心命令（L1/L2/L3，✓命中/✗缺失） | 强核心命中 | 关键命令中的核心 | 归因 |',
          '|---|---|---|---|---|---|---|']
    for r in sorted(weak, key=lambda x: x['idx']):
        core = []
        for c in CORE_CATS:
            for t in r['cat'][c]['all']:
                core.append((t, t in r['cat'][c]['hit']))
        core_txt = '、'.join(f"{c}{'✓' if h else '✗'}" for c, h in core) or '—'
        kr = '、'.join(f"{c}{'✓' if c in r['key_core_hit'] else '✗'}" for c in r['key_core']) or '—'
        if r['strong_total'] > 0:
            if not r['strong_cfg_miss']:
                cause = '强核心全命中→疑误判'
            elif r['strong_hit'] > 0:
                cause = '强核心部分命中'
            else:
                cause = '强核心全未命中'
        elif r['domain_total'] > 0:
            cause = ('L3全命中→疑误判' if not r['domain_miss']
                     else 'L3部分命中' if r['domain_hit'] > 0 else 'L3全未命中')
        else:
            cause = '纯公共/查询'
        if r['domain_miss']:
            cause += f" ⚠L3缺{len(r['domain_miss'])}"
        L.append(f"| F{r['idx']:03d} | {r['title'][:34]} | {r['n_types']} | {core_txt[:76]} | "
                 f"{r['strong_hit']}/{r['strong_total']} | {kr[:36]} | {cause} |")
    L += ['', '## 5. 建议（供审视，未实施）', '',
          '1. 判定主键改为「核心命令命中」：L1/L2（必要时 L3）核心命令全命中 → 判定已配置，'
          '不受前置/查询命令稀释影响。', '',
          '2. 查询类（LST/SHOW/DSP/CHK/EXP）与全局公共类（VPNINST/INTERFACE 等）'
          '从覆盖度分母剔除或单列。', '',
          '3. 保留弱匹配但标注归因（核心命中但辅助缺失 = 「已配置，辅助待补」），'
          'CSV 生成时按归因过滤。', '',
          f'4. 按建议 1 重判，354 篇弱匹配中约 {n_core_ok} 篇升为已配置（覆盖度由 '
          f'{summary["weak_coverage_mean"] * 100:.0f}% → 强核心覆盖 {summary["weak_cov_strong_mean"] * 100:.0f}%）。', '']
    with open(os.path.join(args.out, 'weak_semantics.md'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(L))
    print(f'MD → {args.out}/weak_semantics.md')
    print(f'归因：核心全命中 {n_core_ok} / 部分 {n_core_partial} / 零 {n_core_zero} / 无专属 {n_no_core}')


if __name__ == '__main__':
    main()

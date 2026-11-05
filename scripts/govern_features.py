#!/usr/bin/env python3
"""特性治理 T1：自动指纹提取器

复用 gen_feature_all 解析器 + 三层核心命令分类，产出治理指纹库草稿：
- features.yaml（全 pending，含 core L1/L2/L3 + license + prereq + domain 猜测）
- 治理统计报告 md（域分布 / 无core清单 / license 清单 / L3 误归公共候选）

用法：
    python3 govern_features.py --init --feat-md <特性文档库> \
        --anchors rules/param_anchor.yaml --out rules/features.yaml
    python3 govern_features.py --scan --feat-md <特性文档库> \
        --out rules/features.yaml          # 增量：只提取新增 md
"""
import argparse
import os
import sys
import time
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gen_feature_all as gfa  # noqa: E402
from analyze_weak_semantics import cat_of, classify, STRONG_CORE  # noqa: E402

DEFAULT_DOMAIN_KWS = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                  '..', 'rules', 'domain_keywords.yaml')
PRODUCTS_YAML = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                             '..', 'rules', 'products.yaml')


def guess_domain(title: str, kw_table: dict) -> str:
    """标题关键词 → 业务域（数据驱动，kw_table 来自 domain_keywords.yaml）"""
    best, best_n = '其他', 0
    for dom, kws in kw_table.items():
        n = sum(1 for kw in kws if kw in title)
        if n > best_n:
            best, best_n = dom, n
    return best


def load_domain_kws(path):
    if not path or not os.path.exists(path):
        return {}
    import yaml
    with open(path, encoding='utf-8') as f:
        data = yaml.safe_load(f) or {}
    return {k: list(v) for k, v in data.items() if v}


def build_fingerprint(doc, ref_count, anchors, kw_table, public_n, core_n):
    """一篇文档 → 指纹 dict"""
    title = doc['title']
    total = doc['all_cmd_types']
    doc_anchor_cmds = {cmd for (cmd, ps) in anchors
                       if any((cmd, p) in doc.get('anchor_vals', {}) for p in ps)}
    core = {'L1': [], 'L2': [], 'L3': []}
    license_cmds, prereq, query = [], [], []
    for t in sorted(total):
        cat = cat_of(t, ref_count[t], doc_anchor_cmds, core_n, public_n)
        if cat == 'core_excl':
            core['L1'].append(t)
        elif cat == 'core_anchor':
            if any(t.startswith(p) for p in ('SET LICENSESWITCH', 'SET SOFTPARA')):
                license_cmds.append(t)   # 授权/开关类值锚定 → license 字段
            else:
                core['L2'].append(t)
        elif cat == 'core_domain':
            core['L3'].append(t)
        elif cat == 'public':
            prereq.append(t)
        elif cat == 'query':
            query.append(t)
    # license 参数（锚定参数名）
    license_params = {}
    for t in license_cmds:
        ps = [p for (c, ps_) in anchors for p in ps_ if c == t]
        if ps:
            license_params[t] = ps
    return {
        'title': title,
        'doc_path': doc.get('doc_path', ''),   # 唯一主键（title 重复 203 组，不能作主键）
        'domain': guess_domain(title, kw_table),
        'status': 'governed',        # 通用规则治理完成（无专家确认）；未来专家精修 → approved
        'confidence': 'high',        # 占位，build 后统一按 confidence() 重算
        'gov_version': 0,
        'core': core,
        'license': license_params or [],
        'prereq': prereq,
        'query': query,
        'key_cmds': doc.get('key_cmds', []),
        'all_cmd_types': sorted(total),
        'verdict': {'mode': 'core_all_hit'},
        'notes': '',
    }


def domain_reclaim(feats, ref_count, in_rate_min=0.30, out_rate_max=0.30, max_ref=100,
                   min_domain=5):
    """域级自动收回：被本域特性高频引用、跨域低引用的命令，从 prereq 收回 core.L3。

    解决纯频次分类把「域内共享命令」（接口域 LOGICINF、路由域 BGPPEER）误归全局公共。
    排除全局基础命令（引用数 > max_ref，如 VPNINST/INTERFACE/LICENSESWITCH）。
    排除小域（域内特性 < min_domain，避免 2 篇特性 100% 引用噪声收回共享命令）。
    返回 (reclaimed: {domain: [cmd]}, moved: int)
    """
    dom_feats = defaultdict(list)
    for fid, f in feats.items():
        dom_feats[f['domain']].append(fid)
    dom_total = {d: len(v) for d, v in dom_feats.items()}
    cmd_dom = defaultdict(Counter)   # cmd -> {domain: 引用数}
    for f in feats.values():
        dom = f['domain']
        # 域内"使用"统计 = prereq + 已收回的 core.L3（只统计 prereq 会在增量场景
        # 低估 in_rate：已收回命令不再出现在 prereq，永远达不到收回阈值）
        for cmd in list(f.get('prereq', [])) + list(f.get('core', {}).get('L3', [])):
            cmd_dom[cmd][dom] += 1
    reclaimed = defaultdict(list)
    for cmd, doms in cmd_dom.items():
        n_total = ref_count.get(cmd, 0)
        if n_total > max_ref:
            continue   # 全局基础命令不收回
        for dom, n in doms.items():
            if dom_total[dom] < min_domain:
                continue   # 小域不参与收回
            in_rate = n / dom_total[dom]
            out_rate = (n_total - n) / max(1, len(feats) - dom_total[dom])
            if in_rate >= in_rate_min and out_rate < out_rate_max:
                reclaimed[dom].append(cmd)
    moved = 0
    for fid, f in feats.items():
        dom = f['domain']
        for cmd in reclaimed.get(dom, []):
            if cmd in f['prereq'] and cmd not in f['core']['L3']:
                f['prereq'].remove(cmd)
                f['core']['L3'].append(cmd)
                moved += 1
    return reclaimed, moved


def confidence(f):
    """通用治理置信度：core/license/domain 质量评分（无专家确认时的自动标注）

    high: core ≥2 条且（license 锚定 或 domain 非'其他'）
    mid:  core ≥1 条但 domain='其他' 且无 license（猜测成分大）
    low:  无 core（纯操作/授权类，判定走 license/manual，需未来专家补指纹）
    """
    core_n = len(f['core']['L1']) + len(f['core']['L2']) + len(f['core']['L3'])
    if core_n == 0:
        return 'low'
    if core_n >= 2 and (f['license'] or f['domain'] != '其他'):
        return 'high'
    return 'mid'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--init', action='store_true', help='全量初始化指纹库')
    ap.add_argument('--scan', action='store_true', help='增量：只处理新增 md')
    ap.add_argument('--product', default='',
                    help='产品名（products.yaml 注册，自动取 feat_dir/fingerprint/detect）')
    ap.add_argument('--feat-md', default='', dest='feat_dir', help='特性文档库根目录（--product 缺省时）')
    ap.add_argument('--anchors', default='', help='param_anchor.yaml')
    ap.add_argument('--domain-kws', default=DEFAULT_DOMAIN_KWS, help='domain_keywords.yaml')
    ap.add_argument('-o', '--out', default='', help='指纹库输出路径（默认按产品）')
    ap.add_argument('--public-n', type=int, default=40, help='public 阈值（默认 40）')
    ap.add_argument('--core-n', type=int, default=2, help='L1 阈值（默认 2）')
    ap.add_argument('--reclaim-in', type=float, default=0.30, help='域内引用率阈值（默认 0.30）')
    ap.add_argument('--reclaim-out', type=float, default=0.30, help='跨域引用率阈值（默认 0.30）')
    ap.add_argument('--reclaim-max-ref', type=int, default=100,
                    help='超过此引用数的命令不参与收回（默认 100，排除全局基础命令）')
    ap.add_argument('--reclaim-min-domain', type=int, default=5,
                    help='域内特性数少于该值的域不参与收回（默认 5，防小域噪声）')
    args = ap.parse_args()
    if args.init == args.scan:
        ap.error('必须且只能指定 --init 或 --scan 之一')

    # 产品注册表：--product 自动取 feat_dir/fingerprint
    product_name = ''
    if args.product:
        import yaml as _y
        prods = _y.safe_load(open(PRODUCTS_YAML, encoding='utf-8')) or {}
        pr = prods.get('products', {}).get(args.product)
        if not pr:
            ap.error(f'产品未注册：{args.product}（见 {PRODUCTS_YAML}）')
        product_name = args.product
        if not args.feat_dir:
            args.feat_dir = os.path.expanduser(pr['feat_dir'])
        if not args.out:
            args.out = pr['fingerprint']
    if not args.feat_dir:
        ap.error('必须提供 --product（产品注册表）或 --feat-md')
    if not args.out:
        args.out = 'rules/features.yaml'
    if not args.anchors:
        args.anchors = 'rules/param_anchor.yaml'   # 缺省兜底：否则锚定白名单为空 → L2 全空
    anchors = gfa.load_param_anchors(args.anchors)
    kw_table = load_domain_kws(args.domain_kws)
    docs = gfa.load_feature_docs(args.feat_dir)
    ref_count = Counter()
    for d in docs:
        for c in d['all_cmd_types']:
            ref_count[c] += 1

    out = Path(args.out)
    if args.init:
        print(f'全量初始化：{len(docs)} 篇 → {out}')
        t0 = time.time()
        feats = {}
        for i, doc in enumerate(docs, 1):
            feats[f'F{i:03d}'] = build_fingerprint(doc, ref_count, anchors,
                                                   kw_table, args.public_n, args.core_n)
        reclaimed, moved = domain_reclaim(feats, ref_count, args.reclaim_in,
                                          args.reclaim_out, args.reclaim_max_ref,
                                          args.reclaim_min_domain)
        print(f'域级收回：{sum(len(v) for v in reclaimed.values())} 条命令收回 '
              f'（{len(reclaimed)} 个域），{moved} 处 prereq→core.L3')
        for f in feats.values():
            f['confidence'] = confidence(f)   # 通用治理：置信度统一标注
        data = {
            'meta': {'product': product_name, 'version': 0,
                     'updated_at': time.strftime('%Y-%m-%d'),
                     'stats': {'total': len(feats), 'approved': 0,
                               'governed': len(feats), 'pending': 0}},
            'features': feats,
        }
    else:  # --scan
        if not out.exists():
            ap.error(f'指纹库不存在：{out}（先 --init）')
        import yaml
        data = yaml.safe_load(out.read_text(encoding='utf-8')) or {}
        feats = data['features']
        # doc_path 主键对齐：已有指纹按 doc_path 复用 F 编号，新文档追加新编号
        path2fid = {f.get('doc_path'): fid for fid, f in feats.items()}
        have = set(feats.keys())
        next_no = max((int(fid[1:]) for fid in have if fid[1:].isdigit()), default=0) + 1
        new = []
        for doc in docs:
            fid = path2fid.get(doc.get('doc_path'))
            if fid is None:
                fid = f'F{next_no:03d}'
                next_no += 1
                new.append((fid, doc))
        print(f'扫描：库 {len(have)} 条，文档库 {len(docs)} 篇，新增 {len(new)} 篇'
              f'（doc_path 主键对齐，中间插入不漂移）')
        for fid, doc in new:
            feats[fid] = build_fingerprint(doc, ref_count, anchors,
                                           kw_table, args.public_n, args.core_n)
            feats[fid]['confidence'] = confidence(feats[fid])
        if new:
            reclaimed, moved = domain_reclaim(feats, ref_count, args.reclaim_in,
                                              args.reclaim_out, args.reclaim_max_ref,
                                              args.reclaim_min_domain)
            print(f'域级收回（新增后全量重算）：{sum(len(v) for v in reclaimed.values())} 条命令，'
                  f'{moved} 处 prereq→core.L3')
        data['features'] = feats
        data['meta']['stats']['total'] = len(feats)
        data['meta']['stats']['governed'] = sum(
            1 for f in feats.values() if f.get('status') == 'governed')
        data['meta']['stats']['pending'] = sum(
            1 for f in feats.values() if f.get('status') == 'pending')
        data['meta']['stats']['approved'] = sum(
            1 for f in feats.values() if f.get('status') == 'approved')

    # 写 YAML（保证中文可读）
    import yaml
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(yaml.safe_dump(data, allow_unicode=True, sort_keys=False,
                                  default_flow_style=False), encoding='utf-8')
    print(f'✅ 指纹库 → {out}')

    # ── 治理统计报告 ──
    dom = Counter(f['domain'] for f in feats.values())
    conf = Counter(f.get('confidence', '?') for f in feats.values())
    status_c = Counter(f.get('status', '?') for f in feats.values())
    no_core = [fid for fid, f in feats.items()
               if not (f['core']['L1'] or f['core']['L2'] or f['core']['L3'])]
    lic_feats = [fid for fid, f in feats.items() if f['license']]
    # L3 误归公共候选：频次 41+ 但文档中属于业务核心候选（启发式：命令名与标题域关键词重合）
    public_cmds = sorted([c for c, n in ref_count.items()
                          if classify(c, n, args.public_n, args.core_n) == 'public'],
                         key=lambda c: -ref_count[c])
    rep = [
        '# 特性治理统计报告（自动提取 + 通用规则治理）', '',
        f'- 产品：{product_name or "（未指定）"}',
        f'- 特性总数：{len(feats)} 篇',
        f'- 治理状态：' + ' / '.join(f'{k} {v}' for k, v in status_c.most_common()),
        f'- 置信度：' + ' / '.join(f'{k} {v}' for k, v in conf.most_common()),
        f'- 域分布（标题关键词猜测）：',
    ]
    for d, n in dom.most_common():
        rep.append(f'  - {d}: {n}')
    rep += [
        '', f'- 含 license 授权开关的特性：{len(lic_feats)} 篇（SET LICENSESWITCH/SOFTPARA 值锚定）',
        '', f'- **无 core 命令特性：{len(no_core)} 篇**（纯公共/查询组合，需人工补指纹）',
    ]
    for fid in no_core[:40]:
        rep.append(f'  - {fid} {feats[fid]["title"][:44]}')
    if len(no_core) > 40:
        rep.append(f'  - …… 其余 {len(no_core) - 40} 篇')
    rep += ['', '## 域级自动收回（本域高频引用 + 跨域低引用 → prereq 收回 core.L3）', '']
    if reclaimed:
        for d, cmds in sorted(reclaimed.items(), key=lambda x: -len(x[1])):
            rep.append(f'### {d}（{len(cmds)} 条）')
            rep.append('| 命令类型 | 域内特性引用数 | 域内引用率 |')
            rep.append('|---|---|---|')
            for c in sorted(cmds, key=lambda x: -ref_count[x]):
                n = sum(1 for f in feats.values()
                        if f['domain'] == d and c in f['all_cmd_types'])
                rep.append(f'| {c} | {n} | {n / dom[d]:.0%} |')
            rep.append('')
    else:
        rep.append('（无）')
    rep += ['', '## L3 误归公共候选（频次 >40 但语义域内的业务命令，治理时收回 L3）', '',
            '| 命令类型 | 被引用篇数 |', '|---|---|']
    for c in public_cmds[:30]:
        rep.append(f'| {c} | {ref_count[c]} |')
    rep += ['', '> 治理动作：domain 修正 + L3 收回 + key_cmds 裁减 + status→approved',
            '> 确认一批 → meta.version+1']
    rep_path = out.with_name(f'治理统计报告_{product_name or "x"}.md')
    rep_path.write_text('\n'.join(rep), encoding='utf-8')
    print(f'✅ 统计报告 → {rep_path}')
    print(f'域分布: {dict(dom.most_common(6))} | 无core {len(no_core)} | license {len(lic_feats)}')


if __name__ == '__main__':
    main()

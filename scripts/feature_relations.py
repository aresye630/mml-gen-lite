#!/usr/bin/env python3
"""特性关联关系 + 特性公共配置分析（基于特性文档 ↔ exp 映射）。

关联维度（数据驱动，复用 gen_feature_all 的解析与匹配）：
  A. 专属命令共享：两特性 all_cmd_types 交集（通用命令降噪，出现 ≥5% 文档的命令除外）
  B. 值/对象共享：锚定参数值交集（LICITEM/BITNUM 等功能标识，anchor_vals）
  C. exp 段落共现：两特性匹配命令的 EXP 段落区间重叠（gap≤30 聚类，同功能区）
强度：强 = 锚定值共享 或（专属命令≥2 且 共现）；中 = 专属命令≥1 且 共现 或 锚定值共享；
      弱 = 仅专属命令共享 或 仅段落共现。

公共配置：
  对象级：对象引用参数（rules/feature_rel.yaml object_ref_params + 后缀规则兜底）
          值 → 引用它的命令 → 归属特性集合（被 ≥2 特性引用 = 公共对象）
  命令级：命令类型 → 命中它的特性数
  段落级：EXP 功能区段 → 特性集合

用法:
  python3 feature_relations.py --feat-dir <特性文档目录> --exp <exp.txt> -o <输出目录>
  [--anchors <param_anchor.yaml>] [--rel-rules <feature_rel.yaml>]
"""
import argparse
import json
import heapq
import os
import re
import sys
from collections import Counter, defaultdict
from functools import lru_cache

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_feature_all import (parse_exp, parse_feature_md, cmd_matches,
                             load_param_anchors, QUERY_PREFIXES)

# ═══ 规则加载 ══════════════════════════════════════════════

def load_rel_rules(path):
    """特性关联规则 → dict（对象引用参数清单 + 通用命令阈值）"""
    rules = {'object_ref_params': [], 'common_cmd_doc_ratio': 0.05}
    if path and os.path.exists(path):
        with open(path, encoding='utf-8') as f:
            text = f.read()
        cur = None
        for ln in text.split('\n'):
            ln = ln.strip()
            if not ln or ln.startswith('#'):
                continue
            m = re.match(r'^(\w+)\s*:\s*(.*)$', ln)
            if m:
                k, v = m.group(1), m.group(2)
                if k == 'object_ref_params':
                    cur = 'params'
                    continue
                if k == 'common_cmd_doc_ratio':
                    try:
                        rules['common_cmd_doc_ratio'] = float(v)
                    except ValueError:
                        pass
                    continue
                cur = None
                continue
            # YAML 列表项（- xxx）
            li = re.match(r'^-\s+(.+)$', ln)
            if li and cur == 'params':
                rules['object_ref_params'].append(li.group(1).strip().strip('"\''))
    return rules


_OBJ_PARAM_SUFFIX = re.compile(r'(NAME|NM|ID|INSTANCE)$')


@lru_cache(maxsize=None)
def _is_obj_param_suffix(p):
    """对象参数后缀规则（参数名种类有限，缓存避免 3130 万次重复正则）。"""
    return bool(_OBJ_PARAM_SUFFIX.search(p))


def is_obj_param(p, rules):
    """对象引用参数：显式清单 ∪ 后缀规则 (NAME|NM|ID|INSTANCE)$"""
    if p in rules['object_ref_params']:
        return True
    return _is_obj_param_suffix(p)


class ObjParamSet(frozenset):
    """已判定的「对象参数名」集合 —— 供热循环用 `p in objs` 替代函数调用。

    ★ M3 优化（2026-09-18）：`is_obj_param` 在「命令 × 参数」双层循环里被调
      ~640 万次（采样占 31.7% 为单一最大热点）。单次虽只 0.068µs，
      但函数调用开销累积显著；而**参数名种类有限**（实测 1705 种）⇒
      可预先判定每个出现过的参数名，循环内退化为 C 级 set 查找。

    语义与 is_obj_param 完全一致（同一套规则），只是把判定提前做一次。
    """
    __slots__ = ()

    @classmethod
    def build(cls, rules, param_names):
        """param_names 是本次会遇到的参数名全集（通常取自解析后的命令）"""
        return cls(p for p in param_names if is_obj_param(p, rules))


# ═══ 数据加载 ══════════════════════════════════════════════

def load_docs(feat_dir):
    docs = []
    for root, _dirs, files in os.walk(feat_dir):
        for fn in sorted(files):
            if not fn.endswith('.md'):
                continue
            path = os.path.join(root, fn)
            try:
                with open(path, encoding='utf-8') as f:
                    text = f.read()
            except Exception:
                continue
            rec = parse_feature_md(text, os.path.relpath(path, feat_dir))
            if rec:
                docs.append(rec)
    return docs


def build_paragraphs(seqs, gap=30):
    """匹配命令 seq 列表 → 段落区间 [(start, end), ...]（相邻间隔 ≤ gap 合并）"""
    seqs = sorted(seqs)
    paras = []
    if not seqs:
        return paras
    s = p = seqs[0]
    for x in seqs[1:]:
        if x - p > gap:
            paras.append((s, p))
            s = x
        p = x
    paras.append((s, p))
    return paras


def paras_overlap(a_list, b_list, gap=30):
    """两特性段落区间重叠的对数（同功能区证据强度，≥2 为强共现）"""
    n = 0
    for (a1, a2) in a_list:
        for (b1, b2) in b_list:
            if not (a2 + gap < b1 or b2 + gap < a1):
                n += 1
    return n


# ═══ 主流程 ════════════════════════════════════════════════

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--feat-dir', required=True)
    ap.add_argument('--exp', required=True)
    ap.add_argument('-o', '--outdir', required=True)
    ap.add_argument('--anchors', default=None)
    ap.add_argument('--rel-rules', default=None)
    args = ap.parse_args()

    rules = load_rel_rules(args.rel_rules)
    anchors = load_param_anchors(args.anchors)
    print(f'对象引用参数（{len(rules["object_ref_params"])}）：{rules["object_ref_params"]}')

    docs = load_docs(args.feat_dir)
    exp_cmds = parse_exp(args.exp)
    # ★ M3：预判定对象参数名（循环外一次，热循环内退化为 set 查找）
    _all_param_names = set()
    for _c in exp_cmds:
        _all_param_names.update(_c['params'].keys())
    obj_param_set = ObjParamSet.build(rules, _all_param_names)
    print(f'对象参数名预判定：{len(obj_param_set)} / {len(_all_param_names)} 个参数名')
    exp_cmd_types = {c['cmd'] for c in exp_cmds}
    print(f'特性文档 {len(docs)} 篇，exp 命令 {len(exp_cmds)} 条 / {len(exp_cmd_types)} 种')

    # ── 每特性匹配命令 ──────────────────────────────────
    matched = []          # [ [cmd...], ... ] 与 docs 同序
    anchor_vals = []      # 每特性锚定参数值集 {(cmd,param,val)}
    # 命令类型倒排：cmd_type -> [exp_cmd]。每特性只扫其 all_cmd_types 对应命令，
    # 避免 515 篇 × 10 万条 exp 的暴力双重循环（cmd_matches 首行即按类型过滤）。
    exp_by_type = defaultdict(list)
    for c in exp_cmds:
        exp_by_type[c['cmd']].append(c)
    for i, doc in enumerate(docs):
        ms = [c for ct in doc['all_cmd_types'] for c in exp_by_type.get(ct, ())
              if cmd_matches(c, doc, anchors)]
        # 恢复全局 seq 升序：与旧版 exp_cmds 遍历序一致（确定性 + 保 label 口径，
        # build_instances 的 min tie-break 依赖 matched 插入顺序）
        ms.sort(key=lambda c: c['seq'])
        matched.append(ms)
        av = set()
        for (cmd, p), vals in doc.get('anchor_vals', {}).items():
            for v in vals:
                av.add((cmd, p, v))
        anchor_vals.append(av)
    n_matched = sum(1 for m in matched if m)
    print(f'有 exp 对应的特性：{n_matched} / {len(docs)}')

    # ── 通用命令识别 ────────────────────────────────────
    cmd_docs = Counter()
    for doc in docs:
        for c in doc['all_cmd_types']:
            cmd_docs[c] += 1
    common = {c for c, n in cmd_docs.items()
              if n >= len(docs) * rules['common_cmd_doc_ratio']}
    print(f'通用命令（≥{rules["common_cmd_doc_ratio"]:.0%} 文档）：{len(common)} 种 → {sorted(common)[:20]} …')

    # ── 倒排索引 ────────────────────────────────────────
    spec_inv = defaultdict(list)     # 专属命令 → [特性idx]
    anchor_inv = defaultdict(list)   # (cmd,param,val) → [特性idx]
    paras_by = []                    # 每特性段落区间
    for i, doc in enumerate(docs):
        for c in doc['all_cmd_types'] - common:
            spec_inv[c].append(i)
        for t in anchor_vals[i]:
            anchor_inv[t].append(i)
        paras_by.append(build_paragraphs([m['seq'] for m in matched[i]]))

    # ── 候选特性对（倒排合并）───────────────────────────
    pairs = set()
    for lst in spec_inv.values():
        for x in range(len(lst)):
            for y in range(x + 1, len(lst)):
                pairs.add((lst[x], lst[y]) if lst[x] < lst[y] else (lst[y], lst[x]))
    for lst in anchor_inv.values():
        for x in range(len(lst)):
            for y in range(x + 1, len(lst)):
                pairs.add((lst[x], lst[y]) if lst[x] < lst[y] else (lst[y], lst[x]))
    # 段落共现（区间重叠）
    for i in range(len(docs)):
        if not paras_by[i]:
            continue
        for j in range(i + 1, len(docs)):
            if paras_by[j] and paras_overlap(paras_by[i], paras_by[j]):
                pairs.add((i, j))
    print(f'候选特性对：{len(pairs)}')

    # ── 每特性 exp 侧证据（一切关联证据取自现网匹配命令，不用文档示例值）──
    # 文档示例的锚定值/key_cmds 是官方模板复制产物（几乎每篇都有 SET LICENSESWITCH），
    # 共享它们无区分度；只有两特性在 exp 中命中同一命令/同一对象/同一授权项才是真关联。
    obj_alias = {'DESTVRFNAME': 'VRFNAME', 'SESSNAME': 'SESSIONNAME',
                 'MEMBERIFNAME': 'IFNAME', 'TRUNKIFNAME': 'IFNAME'}
    anchor_param_names = {p for (_cmd, ps) in anchors for p in ps}
    feat_exp_seq = [set() for _ in docs]        # 匹配的非通用命令 seq
    feat_anchor_exp = [set() for _ in docs]     # 匹配命令的锚定参数值 (cmd,p,v)
    feat_obj_vals = [set() for _ in docs]       # 匹配命令的对象引用（非通用命令）
    feat_obj_all = [set() for _ in docs]        # 全部对象引用（通用命令也计入，供稀有度统计）
    for i, ms in enumerate(matched):
        for c in ms:
            if c['cmd'] not in common:
                feat_exp_seq[i].add(c['seq'])
            for p, v in c['params'].items():
                if not v or v in ('YES', 'NO', 'ENABLE', 'DISABLE'):
                    continue
                if p in anchor_param_names:
                    feat_anchor_exp[i].add((c['cmd'], p, v))
                if p in obj_param_set:
                    pk = obj_alias.get(p, p)
                    if c['cmd'] not in common:
                        feat_obj_vals[i].add((pk, v))
                    feat_obj_all[i].add((pk, v))
    # 对象被引用特性数（稀有度，全量统计）
    obj_feat_count = Counter()
    for i in range(len(docs)):
        for o in feat_obj_all[i]:
            obj_feat_count[o] += 1
    RARE_OBJ_REF = 40   # 被 ≤40 个特性引用的对象 = 稀有对象（强证据阈值，脚本常量可调）
    # 命令稀有度权重（IDF）：出现文档越少的命令，共享时关联越强
    n_docs = len(docs)
    cmd_idf = {c: __import__('math').log(n_docs / n)
               for c, n in cmd_docs.items()}
    rels = []   # (i, j, strength, score, shared_spec, shared_anchor, shared_objs, coexp, jaccard)
    # shared_objs 落盘上限（内存/产物体积优化，2026-09-15）：
    #   实测单对共享对象最多 47,105、平均 3,538，全量落盘导致
    #   rels+rel_list 各存一份 → 峰值 5.1GiB（UNC 12.9MB 样本被 OOM-kill）。
    #   下游消费方只用「计数 + 前 6~8 个」（artifacts_v1.py:490/552 len(so)/so[:6]、
    #   gen_viz_html.py:1182 len()、render_report so[:8]），故：
    #     全量 shared_objs 仅用于**计分**（rare_objs），落盘只保留前 N + 总数。
    #   ⚠ 计数必须保留：len() 被三处依赖，丢计数会真改用户可见内容。
    SHARED_OBJS_KEEP = 8
    for (i, j) in sorted(pairs):
        doc_i, doc_j = docs[i], docs[j]
        shared_spec = sorted((doc_i['all_cmd_types'] & doc_j['all_cmd_types']) - common)
        shared_anchor = sorted(feat_anchor_exp[i] & feat_anchor_exp[j])
        shared_exp = sorted(feat_exp_seq[i] & feat_exp_seq[j])   # 同一现网命令（seq）
        shared_objs_full = feat_obj_vals[i] & feat_obj_vals[j]
        # 计分需全量（rare_objs 依赖完整交集），故先算分再截断
        rare_objs = [(p, v) for (p, v) in shared_objs_full
                     if obj_feat_count[(p, v)] <= RARE_OBJ_REF]
        n_shared_objs = len(shared_objs_full)
        # ★ M3：此处只需前 SHARED_OBJS_KEEP(=8) 个，无需全量排序。
        #   旧 sorted(全量)[:8] 对每个特性对做 O(n log n)；集合可达上万元素。
        #   nsmallest 为 O(n log 8) ≈ O(n)，且**结果与 sorted 前 8 个完全一致**。
        shared_objs = heapq.nsmallest(SHARED_OBJS_KEEP, shared_objs_full)
        coexp = paras_overlap(paras_by[i], paras_by[j])
        inter = len(doc_i['all_cmd_types'] & doc_j['all_cmd_types'])
        union = len(doc_i['all_cmd_types'] | doc_j['all_cmd_types'])
        jaccard = inter / union if union else 0.0
        # 关联分：共享稀有对象 5 分/个 + 锚定值 1 分/个 + 共享现网命令 0.5 分/条 + 共现 0.5 分/段
        score = 5.0 * len(rare_objs) + 1.0 * len(shared_anchor) \
            + 0.5 * len(shared_exp) + 0.5 * coexp
        # 判定（全部为 exp 现网证据，文档示例值/命令不参与）：
        #  强 = 共享稀有对象（被 ≤40 特性引用的专属配置对象） 或 共享 ≥2 条现网专属命令
        #  中 = 共享 ≥1 条现网专属命令 或 共享锚定值（license 授权项等，全局清单，仅作弱证据）
        #  弱 = 其余
        if rare_objs or len(shared_exp) >= 2:
            strength = '强'
        elif shared_exp or shared_anchor:
            strength = '中'
        else:
            strength = '弱'
        # ⚠ tuple 第 7 槽语义变更（2026-09-15）：原为 shared_objs 全量 list，
        #   现为 (总数, 前 N 个) 二元组。理由见上（内存优化）。
        #   消费方：rel_list 构造（本文件）、render_report（本文件 so[:8]）。
        rels.append((i, j, strength, round(score, 2), shared_spec,
                     shared_anchor, (n_shared_objs, shared_objs), coexp,
                     round(jaccard, 3)))

    by_strength = Counter(r[2] for r in rels)
    print(f'关联对：强 {by_strength["强"]} / 中 {by_strength["中"]} / 弱 {by_strength["弱"]}')

    # ── 公共配置 ────────────────────────────────────────
    # exp 命令 seq → 命中特性列表（倒排，构建一次）
    seq_feat_inv = defaultdict(list)
    for i, m in enumerate(matched):
        for c in m:
            seq_feat_inv[c['seq']].append(i)
    # 对象级：exp 命令（对象参数,值）→ 特性归属（该命令命中哪些特性）
    obj_inv = defaultdict(lambda: {'params': set(), 'cmds': set(), 'seqs': [],
                                   'features': defaultdict(int)})  # (param,value) → ...
    for m in exp_cmds:
        hit_idx = seq_feat_inv.get(m['seq'], [])
        for p, v in m['params'].items():
            if p not in obj_param_set:
                continue
            if not v or v in ('YES', 'NO', 'ENABLE', 'DISABLE'):
                continue
            rec = obj_inv[(p, v)]
            rec['params'].add(p)
            rec['cmds'].add(m['cmd'])
            rec['seqs'].append(m['seq'])
            for i in hit_idx:
                rec['features'][i] += 1
    # 公共对象 = 被 ≥2 特性引用
    common_objs = [(p, v, r) for (p, v), r in obj_inv.items() if len(r['features']) >= 2]
    common_objs.sort(key=lambda x: (-len(x[2]['features']), x[0], x[1]))
    print(f'公共配置对象（≥2 特性引用）：{len(common_objs)}')

    # 命令级公共：命令 → 命中特性数（按特性匹配，含值锚定）
    cmd_feat = Counter()
    for i, m in enumerate(matched):
        for c in {x['cmd'] for x in m}:
            cmd_feat[c] += 1
    common_cmds = [(c, n) for c, n in cmd_feat.items() if n >= 2]
    # tie(n 相同)时按 cmd 名排序，避免 Counter 插入顺序（受 set 遍历影响）带来的顺序抖动
    common_cmds.sort(key=lambda x: (-x[1], x[0]))
    print(f'公共命令（≥2 特性）：{len(common_cmds)} 种')

    # ── 输出 JSON ───────────────────────────────────────
    os.makedirs(args.outdir, exist_ok=True)
    rel_list = []
    for (i, j, strength, score, ss, sa, so, co, jac) in rels:
        # so 现为 (总数, 前 N 个) —— 保留计数（下游 len() 依赖）+ 明细截断
        n_so, so_top = so if isinstance(so, tuple) else (len(so), so)
        rel_list.append({
            'a': docs[i]['title'], 'b': docs[j]['title'],
            'strength': strength, 'score': score, 'jaccard': jac,
            'shared_specific_cmds': ss, 'shared_anchor_vals': sa,
            'shared_objects': [{'param': p, 'value': v} for (p, v) in so_top],
            'shared_objects_count': n_so,
            'exp_cooccur_paras': co,
        })
    obj_list = []
    for (p, v, r) in common_objs:
        # features 去重（2026-09-15）：原为每个引用特性一条 title，同标题多版本文档
        # 会重复（实测 74,023/76,895 条有重复、共 103.5 万冗余条目，占该字段 43.7%）。
        # 唯一消费方 gen_viz_html.py:1194 用 title_fno(title→fno) 映射，
        # 其 title_fno 由 setdefault 构建（同标题只取首个）⇒ 去重后语义完全等价。
        obj_list.append({
            'param': p, 'value': v, 'feature_count': len(r['features']),
            'features': sorted({docs[i]['title'] for i in r['features']}),
            'cmds': sorted(r['cmds']), 'exp_seqs': [min(r['seqs']), max(r['seqs'])],
        })
    data = {
        'features': [{'title': d['title'], 'all_cmd_types': sorted(d['all_cmd_types']),
                      'matched_cmds': len(matched[i])} for i, d in enumerate(docs)],
        'relations': rel_list,
        'common_objects': obj_list,
        'common_cmds': [{'cmd': c, 'feature_count': n} for c, n in common_cmds[:200]],
    }
    with open(os.path.join(args.outdir, 'relations.json'), 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=1)
    # 释放中间结构（2026-09-15 内存优化）：
    #   rel_list 已写入磁盘；rels 已转完 rel_list，仅 render_report 还需用（只取 so[:8]）。
    #   obj_list/data 同理。显式释放可降低峰值（后续 build_instances + render_report 还要跑）。
    del data
    del obj_list
    del rel_list

    # ── 实例级派生（i1 2026-09-09：特性→现网配置实例；跨特性实例关联，独立文件不影响 relations.json） ──
    build_instances(args.outdir, docs, exp_cmds, matched, paras_by,
                    obj_alias, rules, obj_param_set, common, anchor_param_names,
                    obj_feat_count, RARE_OBJ_REF)

    # ── 输出 MD 报告 ────────────────────────────────────
    render_report(args.outdir, docs, rels, by_strength, common_objs, common_cmds,
                  paras_by, matched)


def render_report(outdir, docs, rels, by_strength, common_objs, common_cmds,
                  paras_by, matched):
    L = []
    L.append('# 特性关联关系与公共配置分析（case1.1）')
    L.append('')
    L.append('> 数据源：特性文档库 991 篇（官方原文+示例命令） ↔ exp 现网命令')
    L.append('> 关联维度：专属命令共享（通用命令降噪）/ 锚定值共享 / exp 段落共现')
    L.append('> 公共配置：对象级（对象引用参数值 → 特性集合）/ 命令级 / 段落级')
    L.append('')
    L.append('## 1. 关联总览')
    L.append('')
    L.append(f'- 特性文档：{len(docs)} 篇，其中 {sum(1 for m in matched if m)} 篇与 exp 有命令对应')
    L.append(f'- 关联对（排除通用命令后）：**强 {by_strength["强"]} / 中 {by_strength["中"]} / 弱 {by_strength["弱"]}**')
    L.append('')
    L.append('## 2. 强关联特性对（共享现网配置对象，或共享功能标识值）')
    L.append('')
    strong = [r for r in rels if r[2] == '强']
    strong.sort(key=lambda r: (-r[3], -r[8]))
    def doc_label(i):
        d = docs[i]
        prod = d['doc_path'].split('/')[0] if d.get('doc_path') else ''
        return f'{d["title"]}（{prod}）' if prod else d['title']
    same_title = [r for r in strong if docs[r[0]]['title'] == docs[r[1]]['title']]
    cross = [r for r in strong if docs[r[0]]['title'] != docs[r[1]]['title']]
    L.append(f'- 跨特性强关联对：**{len(cross)}**（不同特性文档之间，核心价值）')
    L.append(f'- 同标题多版本对（同一特性不同产品目录的文档互为关联）：{len(same_title)}')
    L.append('')
    L.append('### 2.1 跨特性强关联（top 40，按关联分）')
    L.append('')
    for (i, j, _s, sc, ss, sa, so, co, jac) in cross[:40]:
        n_so, so_top = so if isinstance(so, tuple) else (len(so), so)
        L.append(f'#### {doc_label(i)} ↔ {doc_label(j)}（关联分 {sc}）')
        L.append('')
        L.append(f'- 共享现网对象（{n_so}）：{"、".join(f"{p}={v}" for (p, v) in so_top[:8])}{"…" if n_so > 8 else ""}')
        L.append(f'- 共享专属命令（{len(ss)}）：{"、".join(ss[:12])}{"…" if len(ss) > 12 else ""}')
        L.append(f'- 共享功能标识值：{"、".join(f"{c}:{p}={v}" for (c, p, v) in sa[:8]) if sa else "无"}')
        L.append(f'- exp 同功能区共现段落：{co} 段；命令类型 Jaccard：{jac:.2f}')
        L.append('')
    L.append('### 2.2 同标题多版本对（top 10，同一特性不同产品目录）')
    L.append('')
    for (i, j, _s, sc, ss, sa, so, co, jac) in same_title[:10]:
        L.append(f'- {doc_label(i)} ↔ {doc_label(j)}（关联分 {sc}，共享对象 {len(so)}、'
                 f'专属命令 {len(ss)}、Jaccard {jac:.2f}）')
    L.append('')
    L.append('## 3. 公共配置对象（被 ≥2 特性引用的现网对象）')
    L.append('')
    L.append(f'共 **{len(common_objs)}** 个（参数名 | 对象值 | 引用特性数 | EXP 行号 | 引用特性）')
    L.append('')
    L.append('| 参数 | 对象值 | 特性数 | EXP 行号 | 引用特性 |')
    L.append('|---|---|---|---|---|')
    for (p, v, r) in common_objs[:120]:
        feats = '、'.join(f'{docs[i]["title"]}({r["features"][i]})' for i in
                          sorted(r['features'], key=lambda i: -r['features'][i])[:4])
        if len(r['features']) > 4:
            feats += f' 等 {len(r["features"])} 个特性'
        L.append(f'| {p} | {v} | {len(r["features"])} | {min(r["seqs"])}–{max(r["seqs"])} | {feats} |')
    L.append('')
    L.append('## 4. 公共命令（被多个特性匹配的 exp 命令类型，top 60）')
    L.append('')
    L.append('| 命令类型 | 命中特性数 |')
    L.append('|---|---|')
    for c, n in common_cmds[:60]:
        L.append(f'| {c} | {n} |')
    L.append('')
    L.append('## 5. exp 功能区段（段落 → 特性集合，抽样）')
    L.append('')
    # 段落级：合并所有特性段落，按区间重叠分组
    seen = []
    for i, paras in enumerate(paras_by):
        for (a, b) in paras:
            seen.append((a, b, i))
    groups = []
    for (a, b, i) in sorted(seen):
        merged = False
        for g in groups:
            if not (g['end'] + 30 < a or b + 30 < g['start']):
                g['start'] = min(g['start'], a)
                g['end'] = max(g['end'], b)
                g['feats'].append(i)
                merged = True
                break
        if not merged:
            groups.append({'start': a, 'end': b, 'feats': [i]})
    groups.sort(key=lambda g: -len(g['feats']))
    for g in groups[:25]:
        feats = '、'.join(f'{docs[i]["title"]}' for i in g['feats'][:5])
        if len(g['feats']) > 5:
            feats += f' 等 {len(g["feats"])} 个特性'
        L.append(f'- **EXP {g["start"]}–{g["end"]}**（{len(g["feats"])} 个特性）：{feats}')
    L.append('')
    L.append('## 6. 说明')
    L.append('')
    L.append('- 通用命令（出现在 ≥5% 特性文档，如 VPNINST/POOL/APN 类基础设施命令）不计入专属命令共享，'
             '但会出现在 §4 公共命令中——它们是公共配置的主体')
    L.append('- 锚定值共享基于功能标识参数（LICITEM/BITNUM 等），是特性级依赖的强证据')
    L.append('- 强度判定：强 = 共享现网对象（两特性匹配命令引用同一 VRF/APN/接口对象值）'
             '或共享功能标识值；中 = 专属命令 IDF≥3 且同功能区共现；弱 = 仅单维度')
    L.append('- 对象别名归一化：DESTVRFNAME→VRFNAME、SESSNAME→SESSIONNAME、'
             'MEMBERIFNAME/TRUNKIFNAME→IFNAME（跨命令引用同一对象）')
    L.append('- 全量数据见 relations.json（每特性 top 关联、关联矩阵可按需生成）')
    L.append('')
    with open(os.path.join(outdir, '特性关联与公共配置.md'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(L))
    print(f'报告：{outdir}/特性关联与公共配置.md')


# ═══ 实例级派生（i1 2026-09-09） ══════════════════════════════
def build_instances(outdir, docs, exp_cmds, matched, paras_by, obj_alias, rules,
                    obj_param_set, common, anchor_param_names, obj_feat_count,
                    RARE_OBJ_REF, gap=30):
    """特性命中命令 → 现网配置实例，跨特性实例关联。

    实例 = 特性命中命令按 seq 段落聚类（gap≤30）成块，每块一个实例；
    实例名 = 块内最稀有对象锚值（NAME/ID/接口/IP 类，obj_feat_count 最小者），
             无稀有对象锚 → label 为空（前端用 seq 区间标识）。
    关联 = 跨特性实例对共享稀有对象 / 共享现网专属命令行 / 块共现（同特性实例互不关联）。
    强度同特性级口径：强 = 稀有对象共享 或 共享专属命令 ≥2；中 = 共享专属命令 ≥1。
    输出 instances.json（独立文件；relations.json 语义与内容不变）。"""
    # 每实例块化 + 块内证据集
    insts = []          # id = f'{fidx}#{blk}'
    seq_cmd = {c['seq']: c['cmd'] for c in exp_cmds}
    for i, blks in enumerate(paras_by):
        for k, (s, e) in enumerate(blks):
            cs = [c for c in matched[i] if s <= c['seq'] <= e]
            cnt = Counter()
            objs, seqs, anchors = set(), set(), set()
            for c in cs:
                if c['cmd'] not in common:
                    seqs.add(c['seq'])
                for p, v in c['params'].items():
                    if not v or v in ('YES', 'NO', 'ENABLE', 'DISABLE'):
                        continue
                    if p in obj_param_set:
                        pk = obj_alias.get(p, p)
                        if c['cmd'] not in common:
                            objs.add((pk, v))
                        cnt[(pk, v)] += 1
                    if p in anchor_param_names:
                        anchors.add((c['cmd'], p, v))
            # 主锚：稀有优先（obj_feat_count 小=特异于少数特性），其次出现命令多
            main = min(cnt, key=lambda kv: (obj_feat_count.get(kv, 10 ** 9), -cnt[kv])) if cnt else None
            label = f'{main[0]}={main[1]}' if (main and obj_feat_count.get(main, 10 ** 9) <= RARE_OBJ_REF) else ''
            insts.append({'id': f'{i}#{k}', 'fid': i, 'title': docs[i]['title'],
                          's': s, 'e': e, 'n_cmds': len(cs), 'label': label,
                          'anchors': [{'param': p, 'value': v, 'n': n}
                                      for (p, v), n in cnt.most_common(6)],
                          '_objs': objs, '_seqs': seqs, '_anchors': anchors})
    print(f'实例：{len(insts)}（有段落匹配的特性 {len({it["fid"] for it in insts})} 个）')

    # 同 title 去重：多版本文档（不同产品目录同特性）匹配同一现网块 →
    # 区间被更长实例包含者丢弃（长实例命令证据最全）；同 title 实例互不关联已由 title 过滤保证
    by_title = defaultdict(list)
    for x, it in enumerate(insts):
        by_title[it['title']].append(x)
    drop = set()
    for xs in by_title.values():
        xs.sort(key=lambda x: (-(insts[x]['e'] - insts[x]['s']), insts[x]['s']))
        keep = []
        for x in xs:
            it = insts[x]
            if any(insts[k]['s'] <= it['s'] and it['e'] <= insts[k]['e'] for k in keep):
                drop.add(x)
            else:
                keep.append(x)
    if drop:
        insts = [it for x, it in enumerate(insts) if x not in drop]
        print(f'同 title 重复实例剔除 {len(drop)} → 实例 {len(insts)}')

    # 候选实例对：共享现网专属命令行 ∪ 共享稀有对象（同特性 title 互不关联）
    seq_inv = defaultdict(list)
    obj_inv = defaultdict(list)
    for x, it in enumerate(insts):
        for sq in it['_seqs']:
            seq_inv[sq].append(x)
        for o in it['_objs']:
            if obj_feat_count.get(o, 10 ** 9) <= RARE_OBJ_REF:
                obj_inv[o].append(x)
    cand = set()
    for bucket in list(seq_inv.values()) + list(obj_inv.values()):
        if len(bucket) < 2:
            continue
        for x in range(len(bucket)):
            for y in range(x + 1, len(bucket)):
                if insts[bucket[x]]['title'] == insts[bucket[y]]['title']:
                    continue
                cand.add((bucket[x], bucket[y]) if bucket[x] < bucket[y] else (bucket[y], bucket[x]))
    print(f'实例候选对：{len(cand)}')

    # 关联计算（证据/分/强度），只留强 + 中
    links = []
    for (x, y) in cand:
        a, b = insts[x], insts[y]
        shared_obj = sorted(a['_objs'] & b['_objs'])
        rare = [(p, v) for (p, v) in shared_obj
                if obj_feat_count.get((p, v), 10 ** 9) <= RARE_OBJ_REF]
        shared_seq = sorted(a['_seqs'] & b['_seqs'])
        shared_anchor = sorted(a['_anchors'] & b['_anchors'])
        coexp = 1 if not (a['e'] + gap < b['s'] or b['e'] + gap < a['s']) else 0
        score = 5.0 * len(rare) + 1.0 * len(shared_anchor) + 0.5 * len(shared_seq) + 0.5 * coexp
        if rare or len(shared_seq) >= 2:
            st = '强'
        elif shared_seq or shared_anchor:
            st = '中'
        else:
            continue
        links.append({
            'a': {'fid': a['fid'], 'inst': a['id'], 'title': a['title'],
                  'label': a['label'], 'seqs': [a['s'], a['e']]},
            'b': {'fid': b['fid'], 'inst': b['id'], 'title': b['title'],
                  'label': b['label'], 'seqs': [b['s'], b['e']]},
            'strength': st, 'score': round(score, 2),
            # objects/anchors 落盘上限（2026-09-15 内存+产物体积优化）：
            #   实测单条 link 的 objects 可达 43,800 个 → instances.json 395MB。
            #   下游只用「计数 + 前 12」（artifacts_v1.py:606 objects[:12] +
            #   :607 total_objects=len()）与 anchors[:8]。
            #   ⚠ 计数必须另行保留为 total_objects（下游 len() 依赖）。
            'objects': [{'param': p, 'value': v} for (p, v) in sorted(shared_obj)[:12]],
            'total_objects': len(shared_obj),
            'cmds': sorted({seq_cmd[s] for s in shared_seq}),
            'coexp': coexp,
            'anchors': [list(t) for t in sorted(shared_anchor)[:8]],
            'total_anchors': len(shared_anchor)})
    links.sort(key=lambda l: -l['score'])
    by_st = Counter(l['strength'] for l in links)
    print(f'实例关联：强 {by_st["强"]} / 中 {by_st["中"]}')

    # 用户口径（2026-09-09）：未命名（label 空）且无强关联的实例过滤 —— 不落产物/不显示
    n_strong = Counter()
    for l in links:
        if l['strength'] == '强':
            n_strong[l['a']['inst']] += 1
            n_strong[l['b']['inst']] += 1
    drop_anon = {it['id'] for it in insts
                 if not it.get('label') and n_strong.get(it['id'], 0) == 0}
    if drop_anon:
        insts = [it for it in insts if it['id'] not in drop_anon]
        links = [l for l in links
                 if l['a']['inst'] not in drop_anon and l['b']['inst'] not in drop_anon]
        print(f'未命名且无强关联实例过滤 {len(drop_anon)} → 实例 {len(insts)} / 关联 {len(links)}')

    # 输出（剥离 _ 内部集）；features 按 title 聚合（多版本文档合一，第一级唯一）
    for it in insts:
        for k in ('_objs', '_seqs', '_anchors'):
            it.pop(k, None)
    agg = {}
    for it in insts:
        e = agg.setdefault(it['title'], {'title': it['title'], 'n_inst': 0,
                                         'matched_cmds': 0, 'fids': []})
        e['n_inst'] += 1
        e['fids'].append(it['fid'])
    feat_list = []
    for e in agg.values():
        feat_list.append({'title': e['title'], 'n_inst': e['n_inst'],
                          'matched_cmds': max((len(matched[i]) for i in e['fids']),
                                              default=0),
                          'fids': sorted(set(e['fids']))})
    feat_list.sort(key=lambda f: -f['n_inst'])
    json.dump({'features': feat_list, 'instances': insts, 'links': links},
              open(os.path.join(outdir, 'instances.json'), 'w', encoding='utf-8'),
              ensure_ascii=False, indent=1)
    print(f'实例：{outdir}/instances.json')


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""新库(~/Downloads/111) doc_source 导航树 + 指纹库 F 编号对应关系整理器。

只读分析器：解析新库文档 frontmatter 的 doc_source 层级路径，产出扁平 nav 记录，
并与 pack/rules/features_{udg,unc,ueg}.yaml 的 title 做归一化匹配，挂 F 编号。

匹配状态四档：
  exact     —— name 精确命中唯一 title
  fuzzy     —— 归一化后命中唯一 title（工具名变体等）
  ambiguous —— 命中多个 F（指纹库同名 title 重复，仅标记不消歧）
  missing   —— 未命中（新库有、指纹库无，即指纹库覆盖缺口）

产出（均不覆盖任何现有文件）：
  output/nav_analysis/nav_records.json —— 全量扁平记录
  output/nav_analysis/summary.json     —— 按产品匹配分布统计
"""
import os, re, yaml, json, collections

HOME = os.path.expanduser('~')
ROOT = os.path.join(HOME, 'Downloads/111')
RULE = os.path.join(HOME, 'workspace/exp-groundtruth-verify/pack/rules')
OUTDIR = os.path.join(HOME, 'workspace/exp-groundtruth-verify/output/nav_analysis')
os.makedirs(OUTDIR, exist_ok=True)

PROD_RULE = {'UDG': 'features_udg.yaml', 'UNC': 'features_unc.yaml', 'UEG': 'features_ueg.yaml'}


def get_fm(path):
    """读全文解析 frontmatter（部分文档 description 超长，不能只读头部）。"""
    with open(path, encoding='utf-8') as f:
        txt = f.read()
    m = re.match(r'^---\n(.*?)\n---\n', txt, re.DOTALL)
    if not m:
        return {}
    try:
        return yaml.safe_load(m.group(1)) or {}
    except Exception:
        return {}


def norm_ds(ds):
    """归一化 doc_source：兼容 [a,b,c] 扁平 与 [[a,b,c]] 嵌套两种结构。"""
    if not isinstance(ds, list) or not ds:
        return []
    if isinstance(ds[0], list):
        return [str(x) for x in ds[0]]
    return [str(x) for x in ds]


def norm(s):
    """保守归一化：全角括号→半角、工具名变体归一、去空白。不删括号内容（避免 (IPv4)/(IPv6) 误合并）。"""
    s = s.replace('（', '(').replace('）', ')')
    s = s.replace('U2020/MAE', 'MAE').replace('U2020_MAE', 'MAE')
    s = s.replace('U2020/', '').replace('U2020', '')
    return re.sub(r'\s+', '', s)


def load_titles(rule_path):
    with open(rule_path, encoding='utf-8') as f:
        data = yaml.safe_load(f)
    return {fid: v['title'] for fid, v in data.get('features', {}).items()
            if isinstance(v, dict) and v.get('title')}


def collect_docs():
    docs = []
    for prod in ['UDG', 'UNC']:
        d = os.path.join(ROOT, prod)
        if os.path.isdir(d):
            for f in os.listdir(d):
                if f.endswith('.md'):
                    docs.append((prod, os.path.join(d, f), f))
    for sub in ['5GC', 'UEG']:
        d = os.path.join(ROOT, 'UEG', sub)
        if os.path.isdir(d):
            for f in os.listdir(d):
                if f.endswith('.md'):
                    docs.append(('UEG', os.path.join(d, f), f))
    return docs


def main():
    fid_titles = {p: load_titles(os.path.join(RULE, rf)) for p, rf in PROD_RULE.items()}
    for p in PROD_RULE:
        print('[指纹库] {}: {} F 编号'.format(p, len(fid_titles[p])))

    docs = collect_docs()
    print('[新库] 总文档数:', len(docs))

    norm_index = {p: collections.defaultdict(list) for p in PROD_RULE}
    for p, tmap in fid_titles.items():
        for fid, t in tmap.items():
            norm_index[p][norm(t)].append(fid)

    records = []
    stats = collections.Counter()

    for prod, path, fname in docs:
        fm = get_fm(path)
        ds = norm_ds(fm.get('doc_source'))
        name = fm.get('name', '')
        rec = {'prod': prod, 'path': ds, 'name': name, 'file': fname,
               'fid': None, 'match': 'missing', 'candidates': []}
        if not name:
            rec['match'] = 'no_name'
            stats['no_name'] += 1
            records.append(rec)
            continue

        tmap = fid_titles[prod]
        exact_hits = [fid for fid, t in tmap.items() if t == name]
        if exact_hits:
            if len(exact_hits) == 1:
                rec['fid'] = exact_hits[0]
                rec['match'] = 'exact'
                stats['exact'] += 1
            else:
                rec['candidates'] = sorted(exact_hits)
                rec['match'] = 'ambiguous'
                stats['ambiguous'] += 1
            records.append(rec)
            continue

        fuzzy_hits = norm_index[prod].get(norm(name), [])
        if fuzzy_hits:
            if len(fuzzy_hits) == 1:
                rec['fid'] = fuzzy_hits[0]
                rec['match'] = 'fuzzy'
                stats['fuzzy'] += 1
            else:
                rec['candidates'] = sorted(fuzzy_hits)
                rec['match'] = 'ambiguous'
                stats['ambiguous'] += 1
        else:
            stats['missing'] += 1
        records.append(rec)

    prod_stats = collections.defaultdict(collections.Counter)
    for r in records:
        prod_stats[r['prod']][r['match']] += 1

    print()
    print('=' * 64)
    for p in ['UDG', 'UNC', 'UEG']:
        ps = prod_stats[p]
        print('{}: 总 {} | exact {} | fuzzy {} | ambiguous {} | missing {} | no_name {}'.format(
            p, sum(ps.values()), ps.get('exact', 0), ps.get('fuzzy', 0),
            ps.get('ambiguous', 0), ps.get('missing', 0), ps.get('no_name', 0)))

    out_json = os.path.join(OUTDIR, 'nav_records.json')
    with open(out_json, 'w', encoding='utf-8') as f:
        json.dump(records, f, ensure_ascii=False, indent=1)
    print('\n[输出]', out_json, '({} 条)'.format(len(records)))

    summary = {
        'meta': {
            'source_new': '~/Downloads/111',
            'source_rules': 'pack/rules/features_{udg,unc,ueg}.yaml',
            'total_docs': len(records),
            'match_modes': 'exact/fuzzy/ambiguous/missing/no_name',
            'norm_rule': '全角括号→半角；U2020/MAE、U2020_MAE→MAE；去空白。不删括号内容。',
        },
        'by_product': {p: dict(prod_stats[p]) for p in ['UDG', 'UNC', 'UEG']},
    }
    out_sum = os.path.join(OUTDIR, 'summary.json')
    with open(out_sum, 'w', encoding='utf-8') as f:
        json.dump(summary, f, ensure_ascii=False, indent=1)
    print('[输出]', out_sum)


if __name__ == '__main__':
    main()

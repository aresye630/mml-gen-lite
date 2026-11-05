#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""A1+A2 文档去重：内容 md5 分组 → canonical 选择 → 指纹库合并重编号。
输出：去重后指纹库（新文件）+ 去重报告 md。不覆盖原指纹库（先审阅）。
用法：venv-web/bin/python scripts/gen_dedup_fingerprint.py
"""
import os, sys, hashlib, re, argparse
from collections import defaultdict

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'scripts'))
import gen_feature_all as gfa  # noqa: E402
import yaml  # noqa: E402

FEAT = os.path.join(os.environ.get('KB_SRC', os.path.expanduser('~/workspace/zhijian')),
                    'output_ueg_feature/output_ueg_feature_v3')
FPS = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rules', 'features_ueg.yaml')
OUT_FPS = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rules', 'features_ueg_dedup.yaml')
OUT_REP = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rules', '去重报告.md')

# 产品参数化：默认 UEG；UDG/UNC 用 --feat/--fps 覆盖（任务隔离：不写死产品特例）
_ap = argparse.ArgumentParser(description='A1+A2 内容去重（默认 UEG，可 --feat/--fps 切产品）')
_ap.add_argument('--feat', default=FEAT, help='特性文档库根目录')
_ap.add_argument('--fps', default=FPS, help='输入指纹库 yaml')
_ap.add_argument('--out-fps', default=OUT_FPS, help='去重后指纹库输出路径')
_ap.add_argument('--out-rep', default=OUT_REP, help='去重报告 md 输出路径')
_a = _ap.parse_args()
FEAT, FPS, OUT_FPS, OUT_REP = _a.feat, _a.fps, _a.out_fps, _a.out_rep

docs = gfa.load_feature_docs(FEAT)
fp = yaml.safe_load(open(FPS, encoding='utf-8'))
feats = fp['features']

# ── 1. md5 分组 ──
groups = defaultdict(list)
for d in docs:
    p = os.path.join(FEAT, d['doc_path'])
    h = hashlib.md5(open(p, 'rb').read()).hexdigest()
    groups[h].append(d['doc_path'])
dup_groups = {h: v for h, v in groups.items() if len(v) > 1}


def canonical_of(paths):
    """canonical 选择：无 _c 变体后缀的主文档优先；其次文件名最短；再字典序。"""
    def key(p):
        base = os.path.basename(p)
        is_main = 0 if re.search(r'_c\d+_pri\d+', base) else 1
        return (-is_main, len(base), base)
    return sorted(paths, key=key)[0]


canon_map = {}   # doc_path -> canonical doc_path
for paths in dup_groups.values():
    c = canonical_of(paths)
    for p in paths:
        canon_map[p] = c

# ── 2. 指纹合并：canonical 保留，副本删除（alias 记录）──
alias = defaultdict(list)   # canonical doc_path -> [重复 doc_path]
new_feats = {}
for fid, f in feats.items():
    dp = f.get('doc_path', '')
    c = canon_map.get(dp, dp)
    if c == dp:
        new_feats[fid] = f          # canonical（或唯一）保留
    else:
        alias[c].append(dp)         # 副本 → 删除，记录 alias

# 重编号：按 doc_path 排序
sorted_feats = sorted(new_feats.items(), key=lambda kv: kv[1].get('doc_path', ''))
renum = {}
for i, (old_fid, f) in enumerate(sorted_feats, 1):
    new_fid = 'F%03d' % i
    f = dict(f)
    f['dedup'] = {'merged_from': sorted(
        old for old, f_ in new_feats.items()
        if f_ is new_feats[old_fid])}
    renum[old_fid] = new_fid
    renum[new_fid] = f

# alias 挂到 canonical 指纹上
for c, paths in alias.items():
    for fid, f in renum.items():
        if isinstance(f, dict) and f.get('doc_path') == c:
            f.setdefault('dedup', {})['alias_docs'] = sorted(paths)
            break

out = {'meta': dict(fp['meta']), 'features': {}}
for i, (old_fid, f) in enumerate(sorted_feats, 1):
    new_fid = 'F%03d' % i
    out['features'][new_fid] = renum[new_fid]
    # 去掉内部标记字段（dedup 保留 alias 信息供审计）
out['meta']['total'] = len(out['features'])
out['meta']['dedup'] = {'unique_docs': len(groups),
                        'dup_groups': len(dup_groups),
                        'removed': sum(len(v) - 1 for v in dup_groups.values()),
                        'canonical_rule': '主文档(无_cN_priN后缀) > 短文件名 > 字典序'}

yaml.safe_dump(out, open(OUT_FPS, 'w', encoding='utf-8'), allow_unicode=True, sort_keys=False)

# ── 3. 报告 ──
L = []
A = L.append
A('# 指纹库去重报告')
A('')
A('- 原指纹数：**%d**' % len(feats))
A('- 内容重复组：**%d** 组（%d 篇）' % (len(dup_groups), sum(len(v) for v in dup_groups.values())))
A('- 删除重复指纹：**%d** 条' % (sum(len(v) - 1 for v in dup_groups.values())))
A('- 去重后指纹数：**%d**' % len(out['features']))
A('- canonical 规则：主文档（无 _cN_priN 后缀）优先 → 短文件名 → 字典序')
A('')
A('## 重复组明细（全部逐字节相同）')
A('')
A('| 组 | 保留（canonical） | 删除 | 对应特性 |')
A('|---|---|---|---|')
old2new = {}
for i, (old_fid, f) in enumerate(sorted_feats, 1):
    old2new[old_fid] = 'F%03d' % i
for h, paths in sorted(dup_groups.items(), key=lambda x: -len(x[1])):
    c = canonical_of(paths)
    removed = sorted(p for p in paths if p != c)
    feat_ids = sorted(fid for fid, f in feats.items() if f.get('doc_path') in paths)
    new_ids = '/'.join(old2new.get(x, '?') for x in feat_ids if x in old2new)
    A('| %d 份 | `%s` | %s | %s → %s |' % (
        len(paths), os.path.basename(c),
        '、'.join(os.path.basename(p) for p in removed),
        ','.join(feat_ids), new_ids))
A('')
open(OUT_REP, 'w', encoding='utf-8').write('\n'.join(L))
print('去重指纹库 →', OUT_FPS)
print('去重报告 →', OUT_REP)
print('统计:', len(feats), '→', len(out['features']), '（删', sum(len(v) - 1 for v in dup_groups.values()), '条）')

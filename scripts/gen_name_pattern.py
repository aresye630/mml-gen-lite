#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""B1 值模式规则生成：从接口类特性文档提取 ADD LOGICINF NAME 样例 → 前缀模式。
输出 rules/name_pattern.yaml（数据驱动，source 标注；缺失前缀待专家/LLD 补全）。
"""
import os, re, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'scripts'))
import gen_feature_all as gfa  # noqa: E402
import yaml  # noqa: E402

FEAT = os.path.expanduser('~/workspace/zhijian/output_ueg_feature/output_ueg_feature_v3')
FPS = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rules', 'features_ueg.yaml')
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rules', 'name_pattern.yaml')

docs = gfa.load_feature_docs(FEAT)
fp = yaml.safe_load(open(FPS, encoding='utf-8'))['features']


def norm_prefix(v):
    """'Saif1/1/0'→'saif'；'S11-uif1/1/0'→'s11uif'（归一：小写、去尾数字段、去分隔符）"""
    s = str(v).strip().lower()
    first = s.split('/')[0]
    first = re.sub(r'\d+$', '', first)
    return re.sub(r'[^a-z0-9]', '', first)


patterns = []
for fid, f in sorted(fp.items()):
    if '接口数据' not in f.get('title', ''):
        continue
    d = next((x for x in docs if x['doc_path'] == f.get('doc_path', '')), None)
    if not d:
        continue
    av = d.get('anchor_vals', {})
    names = av.get(('ADD LOGICINF', 'NAME'))
    if not names:
        continue
    prefixes = sorted({norm_prefix(v) for v in names if v})
    patterns.append({
        'fid': fid,
        'title': f.get('title', ''),
        'cmd': 'ADD LOGICINF',
        'param': 'NAME',
        'prefixes': prefixes,
        'doc': f.get('doc_path', '').split('/')[-1],
        'source': 'doc_sample',
    })

out = {
    'meta': {
        'purpose': '值模式判别：同命令集特性按锚点参数值前缀归属（UEG 逻辑接口命名规范）',
        'semantics': '判定：锚点值前缀命中 → 特性归属命中；命令集命中但前缀不匹配 → 值模式不符（不判已配置）',
        'norm': '前缀归一：小写、取第一段、去尾数字、去分隔符（Saif1/1/0→saif，S11-uif1/1/0→s11uif）',
        'generated_by': 'gen_name_pattern.py（数据驱动，待专家/LLD 补全缺失前缀）',
    },
    'interface_name_patterns': patterns,
}
yaml.safe_dump(out, open(OUT, 'w', encoding='utf-8'), allow_unicode=True, sort_keys=False)
print('规则 →', OUT)
for p in patterns:
    print(' ', p['fid'], p['title'][:24], '→', p['prefixes'])

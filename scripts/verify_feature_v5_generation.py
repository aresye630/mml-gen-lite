#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""P3 全量生成覆盖验证：三产品所有含模板特性，自动构造值 → 渲染，统计成功率。

判据（用户口径）：
  · 全产物收集：逐特性渲染结果 + 汇总报告
  · 不静默丢参：缺参/渲染失败必须计入报告
  · 可执行性：生成的 MML 命令结构完整（动词+对象+参数;）
"""
import json
import os
import re
import sys
from collections import Counter

import yaml

sys.path.insert(0, '/m/scripts')
from gen_mml_from_v5 import render_templates, extract_commands  # noqa: E402

OUT = os.environ.get('OUT', '/out')
RESULT = {'products': {}, 'summary': {}}
tot = Counter()


def auto_values(params):
    """从 schema 自动构造一组可渲染的值（enum→首值，int→min，str→TESTVAL）。"""
    vals = {}
    for g, gv in (params or {}).items():
        item = {}
        for pn, pd in (gv.get('properties') or {}).items():
            if pd.get('enum'):
                item[pn] = pd['enum'][0]
            elif pd.get('type') == 'integer':
                item[pn] = pd.get('minimum', 1)
            elif pd.get('type') == 'number':
                item[pn] = pd.get('minimum', 1)
            else:
                ml = pd.get('maxLength') or 20
                item[pn] = ('TESTVAL' * 10)[:ml]
        vals[g] = [item]
    return vals


for prod in ('ueg', 'udg', 'unc'):
    p = os.path.join(OUT, f'feature_v5_{prod}.yaml')
    if not os.path.exists(p):
        continue
    feats = yaml.safe_load(open(p, encoding='utf-8'))['features']

    n_feat = len(feats)
    n_with_tpl = sum(1 for f in feats.values() if f.get('templates'))
    n_render_ok = n_render_fail = 0
    cmd_total = 0
    placeholder_cmds = 0
    tpl_fail_examples = []
    per_feat = []

    for k, f in feats.items():
        tpls = f.get('templates') or []
        if not tpls:
            continue
        vals = auto_values(f.get('params') or {})
        rendered = render_templates(tpls, vals)
        cmds = []
        failed = 0
        for r in rendered:
            if r['text'].startswith('<渲染失败'):
                failed += 1
                continue
            cmds.extend(extract_commands(r['text']))
        if failed:
            n_render_fail += 1
            if len(tpl_fail_examples) < 5:
                tpl_fail_examples.append((k, f['title'][:35], failed))
        else:
            n_render_ok += 1
        cmd_total += len(cmds)
        placeholder_cmds += sum(1 for c in cmds if '<' in c)
        per_feat.append({'key': k, 'title': f['title'], 'templates': len(tpls),
                         'commands': len(cmds), 'failed_templates': failed})

    RESULT['products'][prod] = {
        'features': n_feat,
        'features_with_templates': n_with_tpl,
        'render_ok': n_render_ok,
        'render_fail': n_render_fail,
        'commands_generated': cmd_total,
        'commands_with_placeholder': placeholder_cmds,
        'fail_examples': tpl_fail_examples,
        'detail': per_feat,
    }
    tot['features'] += n_feat
    tot['with_tpl'] += n_with_tpl
    tot['ok'] += n_render_ok
    tot['fail'] += n_render_fail
    tot['cmds'] += cmd_total

    print(f"[{prod.upper()}] 特性 {n_feat} / 含模板 {n_with_tpl} | "
          f"渲染成功 {n_render_ok} 失败 {n_render_fail} | "
          f"生成命令 {cmd_total} 条 (含占位符 {placeholder_cmds})")
    if tpl_fail_examples:
        for k, t, nf in tpl_fail_examples:
            print(f"    ⚠ {k} {t}: {nf} 个模板渲染失败")

RESULT['summary'] = dict(tot)
print(f"\n合计: 特性 {tot['features']} / 含模板 {tot['with_tpl']} | "
      f"渲染成功 {tot['ok']} 失败 {tot['fail']} | 命令 {tot['cmds']} 条")

json.dump(RESULT, open(os.path.join(OUT, 'p3_generation_report.json'), 'w', encoding='utf-8'),
          ensure_ascii=False, indent=1)
print(f"报告: {os.path.join(OUT, 'p3_generation_report.json')}")

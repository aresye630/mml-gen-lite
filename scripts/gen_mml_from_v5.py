#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""gen_mml_from_v5.py — 从 feature_v5 渲染 MML 配置命令。

输入：feature_v5_{prod}.yaml + 用户提供的参数值（JSON）
输出：每条模板渲染出的 MML 命令（含中间产物，便于审阅）

设计（用户口径）：
  · 数据驱动：模板与参数 schema 均来自 feature_v5，无硬编码
  · 全产物保留：渲染结果 + 中间输入 + 逐命令明细
  · 缺参用 <placeholder>，不静默丢参
  · 条件必选/可选逻辑由模板自带 jinja2 表达，生成器不重复实现

用法：
  python3 gen_mml_from_v5.py --feature-yaml <v5.yaml> --feature <key|title>
                             --values <values.json> -o <outdir>
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
from datetime import datetime, timezone

import yaml

try:
    from jinja2 import Environment, Undefined
    HAS_JINJA = True
except ImportError:
    HAS_JINJA = False
    Undefined = object


class Placeholder(Undefined):
    """jinja2 Undefined 子类：缺参渲染为 <name> 占位符（不报错、不静默丢）。"""

    def __str__(self):
        return f'<{self._name}>'

    def __iter__(self):
        return iter(())

    def __bool__(self):
        return False

    def __eq__(self, other):
        return False

    def __ne__(self, other):
        return True

    def __getattr__(self, item):
        # 保留 jinja2 内部属性访问语义
        if item.startswith('_'):
            raise AttributeError(item)
        return Placeholder(name=f'{self._name}.{item}')

    def __getitem__(self, item):
        return Placeholder(name=f'{self._name}[{item}]')


def load_yaml(p):
    with open(p, encoding='utf-8') as f:
        return yaml.safe_load(f)


def pick_feature(doc, key_or_title):
    """按 key 或 title 定位特性。"""
    feats = doc['features']
    if key_or_title in feats:
        return key_or_title, feats[key_or_title]
    for k, v in feats.items():
        if v.get('title', '') == key_or_title:
            return k, v
    # 模糊匹配
    hits = [(k, v) for k, v in feats.items() if key_or_title in v.get('title', '')]
    if len(hits) == 1:
        return hits[0][0], hits[0][1]
    if len(hits) > 1:
        print(f'⚠ 标题不唯一，命中 {len(hits)} 条:', [v['title'] for _, v in hits[:5]])
        return hits[0][0], hits[0][1]
    raise KeyError(f'未找到特性: {key_or_title}')


def render_templates(templates, values, get_param=None):
    """渲染所有 jinja2 模板。

    get_param(name) —— 111 模板的运行期取值接口：
      `{% set V=getParameterValue('LST XXX') %}` 用于条件分支
      （如 `if LST_AUTOCONFIG=='TRUE'` 才生成该段命令）。
      未提供时返回 None → 条件分支不成立，对应命令不生成（安全默认）。
    """
    if not HAS_JINJA:
        raise RuntimeError('需要 jinja2：pip install jinja2')

    def _gpv(name):
        """getParameterValue 实现：优先运行时 provider，否则 None。"""
        if get_param is not None:
            try:
                return get_param(name)
            except Exception:
                return None
        return None

    env = Environment(undefined=Placeholder, trim_blocks=False,
                      lstrip_blocks=False, keep_trailing_newline=True)
    env.globals['getParameterValue'] = _gpv
    out = []
    for i, tpl in enumerate(templates, 1):
        try:
            src = env.from_string(tpl)
            txt = src.render(**values)
        except Exception as e:
            txt = f'<渲染失败: {e}>'
        # 清理空白行，保留命令结构
        lines = [ln.rstrip() for ln in txt.split('\n')]
        lines = [ln for ln in lines if ln.strip()]
        out.append({'index': i, 'text': '\n'.join(lines), 'raw': tpl})
    return out


def extract_commands(rendered_text):
    """从渲染结果提取 MML 命令（以 ; 分隔）。"""
    cmds = []
    for chunk in re.split(r';\s*\n|;\s*$', rendered_text):
        c = ' '.join(chunk.split())
        if c:
            cmds.append(c)
    return cmds


def main():
    ap = argparse.ArgumentParser(description='从 feature_v5 渲染 MML')
    ap.add_argument('--feature-yaml', required=True)
    ap.add_argument('--feature', required=True, help='特性 key 或 title')
    ap.add_argument('--values', required=True, help='参数值 JSON 文件')
    ap.add_argument('-o', '--outdir', required=True)
    ap.add_argument('--values-key', default='', help='多场景 values 的顶层键（默认整个 JSON）')
    args = ap.parse_args()

    doc = load_yaml(os.path.expanduser(args.feature_yaml))
    key, feat = pick_feature(doc, args.feature)

    raw_values = json.load(open(os.path.expanduser(args.values), encoding='utf-8'))
    values = raw_values[args.values_key] if args.values_key else raw_values

    outdir = os.path.abspath(os.path.expanduser(args.outdir))
    os.makedirs(outdir, exist_ok=True)

    print('═' * 62)
    print(f'特性: {key} — {feat["title"]}')
    print(f'产品: {feat.get("product")}  参数组: {len(feat.get("params") or {})}  '
          f'模板: {len(feat.get("templates") or [])}')
    print('═' * 62)

    templates = feat.get('templates') or []
    if not templates:
        print('⚠ 该特性无命令模板（仅文档级），无法生成 MML')
        json.dump({'feature': key, 'title': feat['title'], 'generated': [],
                   'note': 'no templates'},
                  open(os.path.join(outdir, 'generated_mml.json'), 'w', encoding='utf-8'),
                  ensure_ascii=False, indent=1)
        return 1

    rendered = render_templates(templates, values)

    # ── 全产物收集 ──
    all_mml = []
    group_status = []
    for r in rendered:
        cmds = extract_commands(r['text'])
        r['commands'] = cmds
        all_mml.extend(cmds)
        # 该模板消费的参数组（for item in XXX）是否提供了值
        m = re.search(r"for\s+\w+\s+in\s+(\w+)", r['raw'])
        gname = m.group(1) if m else ''
        has_val = bool(values.get(gname)) if gname else None
        group_status.append({
            'template': r['index'],
            'param_group': gname,
            'provided': has_val,
            'commands': len(cmds),
        })

    # 参数组状态汇总（显式暴露未提供值的组，不静默）
    missing_groups = [g for g in (feat.get('params') or {})
                      if not values.get(g)]

    # 1) 原始渲染文本
    with open(os.path.join(outdir, 'rendered_raw.txt'), 'w', encoding='utf-8') as f:
        for r in rendered:
            f.write(f'### 模板 {r["index"]}\n{r["text"]}\n\n')

    # 2) 命令清单（纯 MML）
    with open(os.path.join(outdir, 'generated_mml.txt'), 'w', encoding='utf-8') as f:
        for c in all_mml:
            f.write(c + '\n')

    # 3) 结构化 JSON（含模板溯源）
    result = {
        'feature_key': key,
        'title': feat['title'],
        'product': feat.get('product'),
        'ne_type': feat.get('ne_type'),
        'nav': feat.get('nav'),
        'generated_at': datetime.now(timezone.utc).isoformat(timespec='seconds'),
        'input_values': values,
        'param_groups_available': list((feat.get('params') or {}).keys()),
        'param_groups_missing': missing_groups,
        'template_status': group_status,
        'commands': all_mml,
        'by_template': [{'index': r['index'], 'commands': r['commands']} for r in rendered],
    }
    json.dump(result, open(os.path.join(outdir, 'generated_mml.json'), 'w', encoding='utf-8'),
              ensure_ascii=False, indent=1)

    # 4) 输入值回写（模板化输入，供审阅）
    json.dump(raw_values, open(os.path.join(outdir, 'input_values.json'), 'w', encoding='utf-8'),
              ensure_ascii=False, indent=1)

    print(f'\n生成 {len(all_mml)} 条 MML 命令')
    for c in all_mml:
        flag = '  ⚠缺参' if '<' in c else ''
        print(f'  {c[:110]}{flag}')
    ph = sum(1 for c in all_mml if '<' in c)
    print(f'\n产物: {outdir}/{{rendered_raw.txt, generated_mml.txt, generated_mml.json, input_values.json}}')
    print('\n参数组状态:')
    for g in group_status:
        mark = '✓' if g['provided'] else '—'
        print(f"  {mark} 模板{g['template']:2d}  ← {g['param_group']:32s} 生成 {g['commands']} 条")
    if missing_groups:
        print(f'⚠ 未提供值的参数组 {len(missing_groups)} 个: {missing_groups}')
    if ph:
        print(f'⚠ 含占位符的命令: {ph} 条（缺参，需补全）')
    return 0


if __name__ == '__main__':
    sys.exit(main())

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""新格式特性文档（~/Downloads/111）适配器 → 契约表。

输入：一篇新格式 md（frontmatter + @mml:block=annotations/params/commands 三段）。
输出契约表（数据驱动，零硬编码命令名/参数名）：
  - enum_vals:   {命令名: {参数: [值域]}}         ← params 段 enum 字段（完整值域契约）
  - key_params:  {命令名: [参数]}                 ← params 段 required:true 参数
  - cond_deps:   [{cmd, cond_param, cond_val, params, kind}]  ← commands 段条件 if 分支
  - cmd_meta:    {命令名: {list_name, params: {参数: {name, required, data_source, enum, default}}}}
  - name/doc_source: frontmatter

关键映射：params 段 list 名 ↔ 命令名，从 commands 段 `{% for item in <list> %}` 紧随的
大写命令行权威读取（不靠命名规则推断）。
"""
import re
import sys

try:
    import yaml
except ImportError:
    yaml = None


def _load_yaml(text):
    if yaml is None:
        raise RuntimeError('需要 pyyaml')
    return yaml.safe_load(text)


def _block(txt, tag):
    """提取 @mml:block=<tag> 之后的内容。

    标记形态：`<!-- @mml:block=params -->`（HTML 注释）。params 段紧跟 ```yaml fence；
    commands 段无外层 fence（内部是多个 ```jinja2 子块），直接返回剩余全文。
    """
    m = re.search(r'@mml:block=%s\s*-->\s*\n' % tag, txt)
    if not m:
        return ''
    rest = txt[m.end():]
    fm2 = re.match(r'```yaml\s*\n', rest)
    if fm2:
        rest = rest[fm2.end():]
        end = re.search(r'\n```', rest)
        return rest[:end.start()] if end else rest
    return rest


def _frontmatter(txt):
    m = re.match(r'^---\n(.*?)\n---\n', txt, re.DOTALL)
    if not m:
        return {}
    return _load_yaml(m.group(1)) or {}


def parse_new_format(path):
    txt = open(path, encoding='utf-8').read()
    fm = _frontmatter(txt)

    # ── params 段 → {list_name: {PARAM: {required, enum, data_source, name}}} ──
    py = _load_yaml(_block(txt, 'params'))
    schemas = {}
    props = (py or {}).get('schemas', {}).get('properties', {}) or {}
    for list_name, ls in props.items():
        p = ls.get('properties', {}) or {}
        schemas[list_name] = p
    # examples 段：官方示例值（{list_name: [ {PARAM: 值} ]}），等价旧格式 anchor_vals 但结构化。
    # 实际缩进在 schemas 下（schemas.examples），做顶层/schemas 双兼容。
    examples = ((py or {}).get('examples')
                or (py or {}).get('schemas', {}).get('examples')
                or {})

    # ── commands 段 → list_name ↔ 命令名 映射 + 条件 if ──
    cmd_txt = _block(txt, 'commands')
    list2cmd = {}
    cmd2list = {}
    cond_deps = []
    # 每个 ```jinja2 块：for item in <list> → 命令名 + 条件分支
    for blk in re.findall(r'```jinja2\s*\n(.*?)```', cmd_txt, re.DOTALL):
        lm = re.search(r'for\s+item\s+in\s+(\w+)', blk)
        if not lm:
            continue
        list_name = lm.group(1)
        cm = re.search(r'^\s*([A-Z][A-Z0-9 ]+):\s*$', blk, re.MULTILINE)
        if not cm:
            continue
        cmd = cm.group(1).strip()
        list2cmd[list_name] = cmd
        cmd2list[cmd] = list_name
        # 条件分支：{% if item.P == 'V' %} / {% if item.P in [...] %}
        for cond in re.finditer(
                r'{%-?\s*if\s+item\.(\w+)\s*(==|in)\s*(\[[^\]]*\]|\'[^\']*\'|\"[^\"]*\")',
                blk):
            cp = cond.group(1)
            raw = cond.group(3)
            if raw.startswith('['):
                vals = re.findall(r"['\"]([^'\"]*)['\"]", raw)
            else:
                vals = [raw.strip("'\"")]
            # 条件块内出现的参数名（item.X 形式，去重；排除条件参数本身）
            inner = blk[cond.end():]
            end = re.search(r'{%-?\s*endif', inner)
            seg = inner[:end.start()] if end else inner
            affected = []
            for pm in re.finditer(r'item\.(\w+)', seg):
                if pm.group(1) != cp and pm.group(1) not in affected:
                    affected.append(pm.group(1))
            cond_deps.append({'cmd': cmd, 'cond_param': cp, 'cond_vals': vals,
                              'params': affected})

    # ── 产出契约表 ──
    enum_vals = {}
    key_params = {}
    cmd_meta = {}
    data_source = {}   # 意图生成回填点：值来源契约 {命令: {参数: 值来源}}
    for cmd, list_name in cmd2list.items():
        pdef = schemas.get(list_name, {})
        cmd_meta[cmd] = {'list_name': list_name, 'params': pdef}
        for pname, meta in pdef.items():
            if isinstance(meta, dict):
                if meta.get('required'):
                    key_params.setdefault(cmd, []).append(pname)
                if meta.get('enum'):
                    enum_vals.setdefault(cmd, {})[pname] = list(meta['enum'])
                if meta.get('data_source'):
                    data_source.setdefault(cmd, {})[pname] = meta['data_source']

    return {
        'name': fm.get('name', ''),
        'ne_type': fm.get('ne_type', ''),
        'doc_source': fm.get('doc_source', []),
        'list2cmd': list2cmd,
        'cmd_meta': cmd_meta,
        'enum_vals': enum_vals,
        'key_params': key_params,
        'cond_deps': cond_deps,
        'data_source': data_source,
        'examples': examples,
    }


if __name__ == '__main__':
    import json
    for p in sys.argv[1:]:
        d = parse_new_format(p)
        print(f'=== {d["name"]} ===')
        print('enum_vals:', json.dumps(d['enum_vals'], ensure_ascii=False, indent=1))
        print('key_params:', json.dumps(d['key_params'], ensure_ascii=False, indent=1))
        print('cond_deps:', json.dumps(d['cond_deps'], ensure_ascii=False, indent=1))

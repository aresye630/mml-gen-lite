#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""p3_chains.py — 链级判定引擎（T3）。

chain_schemas.yaml（数据驱动）解释器：
  - 锚定：anchor_cmds 全缺 → 链 not_present
  - 层扫描：cmd_set（可带 param_filters）/ license_items(glob)
  - 层状态聚合 → verdict_rules 顺序求值 → 链 status + note
输出 chain_verdicts[]（并入 report.json），供渲染器「三、链现状」与
差异比较器（T4）与 UI 三列「代码判定」列使用。
"""

import fnmatch
import yaml
from collections import Counter
from pathlib import Path

from p1_parse import parse_exp, parse_params

RULES_DIR = Path(__file__).resolve().parent / 'rules'


def load_schemas(product):
    raw = yaml.safe_load((RULES_DIR / 'chain_schemas.yaml').read_text(encoding='utf-8'))
    return {c['chain_id']: c for c in raw.get(product, [])}


def _cmd_matches(line, spec):
    """spec: 'ADD POOL' 或 {type:'ADD URR', filter:{USAGERPTMODE:'QOS'}} → bool"""
    if isinstance(spec, str):
        return line.startswith(spec + ':')
    ctype = spec['type']
    if not line.startswith(ctype + ':'):
        return False
    pd = parse_params(line)
    for k, v in (spec.get('filter') or {}).items():
        if pd.get(k) != v:
            return False
    return True


def _scan_cmd_set(commands, cmds):
    """层内逐命令：{spec, n, first_seq}；首行号即证据。"""
    out = []
    for spec in cmds:
        n = 0
        first = None
        for seq, line in commands.items():
            if _cmd_matches(line, spec):
                n += 1
                if first is None:
                    first = seq
        label = spec if isinstance(spec, str) else \
            f"{spec['type']}({','.join(f'{k}={v}' for k, v in (spec.get('filter') or {}).items())})"
        out.append({'cmd': label, 'n': n, 'first_seq': first})
    return out


def _layer_status(layer, hits):
    """层聚合：cmd_set 层 ok/missing/partial/exempt（按 absent_policy 解释缺失）。"""
    if layer.get('kind') != 'cmd_set':
        return 'absent'
    present = [h for h in hits if h['n'] > 0]
    missing = [h for h in hits if h['n'] == 0]
    if not missing:
        return 'ok'
    policy = layer.get('absent_policy', 'missing')
    if not present:                      # 全缺
        return {'missing': 'missing', 'partial': 'partial', 'exempt': 'exempt'}[policy]
    return {'missing': 'missing', 'partial': 'partial', 'exempt': 'ok'}[policy]


def _scan_lic_layer(commands, layer, lic_items):
    """license_items：items glob 匹配 lic_switch 明细 → (status, detail)"""
    pats = layer.get('items', [])
    matched = []
    for pat in pats:
        found = [(lic, st) for lic, st in lic_items.items() if fnmatch.fnmatch(lic, pat)]
        matched.append({'pattern': pat, 'hits': [{'lic': a, 'state': b} for a, b in found]})
    states = {st for m in matched for h in m['hits'] for st in [h['state']]}
    if not matched or all(not m['hits'] for m in matched):
        # ⚠ absent 按 absent_policy 归一：missing=功能不可用（要报）/ exempt=视为正常
        policy = layer.get('absent_policy', 'missing')
        status = 'missing' if policy == 'missing' else (
            'partial' if policy == 'partial' else 'absent')
    elif states == {'ENABLE'}:
        status = 'ok'
    elif 'DISABLE' in states:
        # ⚠ 有 DISABLE 就不能算 ok：授权被关 = 功能不可用，必须报出
        #    （此前 'ENABLE' in states → ok 会把「部分被关」漏报）
        status = 'disabled'
    else:
        status = 'absent'
    return status, matched


def _collect_param_values(commands, cmd_spec, param):
    """收集某命令类型所有实例的某参数值（去重、去 '&' 系统命名前缀）。"""
    vals = set()
    for line in commands.values():
        if not _cmd_matches(line, cmd_spec):
            continue
        v = parse_params(line).get(param)
        if v:
            vals.add(str(v).lstrip('&'))
    return vals


def _eval_refs(chain, commands):
    """引用链检测：每条 ref 的 from 定义集 vs to 引用集 → closed/dangling。"""
    refs_out = []
    for ref in chain.get('refs', []):
        frm = ref['from']
        to = ref['to']
        frm_cmds = frm['cmd'] if isinstance(frm['cmd'], list) else [frm['cmd']]
        defs = set()
        for c in frm_cmds:
            defs |= _collect_param_values(commands, c, frm['param'])
        to_params = to.get('params') or [to['param']]
        refs_vals = set()
        for p in to_params:
            refs_vals |= _collect_param_values(commands, to['cmd'], p)
        dangling = sorted(refs_vals - defs)
        orphan = sorted(defs - refs_vals)
        status = 'closed' if not dangling else 'dangling'
        refs_out.append({
            'name': ref['name'],
            'from': '/'.join((c if isinstance(c, str) else c['type']) for c in frm_cmds) + f".{frm['param']}",
            'to': f"{to['cmd'] if isinstance(to['cmd'], str) else to['cmd']['type']}.{'/'.join(to_params)}",
            'defs_count': len(defs),
            'refs_count': len(refs_vals),
            'dangling_count': len(dangling),
            'dangling': dangling,
            'orphan_count': len(orphan),
            'orphan': orphan[:20],
            'status': status,
        })
    return refs_out


def evaluate_chain(chain, commands, lic_items):
    """单链判定 → verdict dict。"""
    # 锚定
    anchors = []
    present_n = 0
    anchor_value = None
    ap = chain.get('anchor_param')
    ax = chain.get('anchor_param_exclude_prefix')
    rq = chain.get('anchor_param_require_prefix')
    for spec in chain.get('anchor_cmds', []):
        n = 0
        first = None
        for seq, line in commands.items():
            if _cmd_matches(line, spec):
                n += 1
                if first is None:
                    first = seq
                if anchor_value is None and ap:
                    v = parse_params(line).get(ap)
                    if v and (not ax or not v.startswith(ax)) \
                            and (not rq or v.startswith(rq)):
                        anchor_value = v
        anchors.append({'cmd': spec if isinstance(spec, str) else str(spec), 'n': n, 'first_seq': first})
        if n > 0:
            present_n += 1

    # ⚠ 授权类链（anchor_from_license）：命令级锚定无筛选力（SET LICENSESWITCH 几乎恒在）
    #    → 改用 license_items 层的命中数做锚定：无任何授权项命中 = 本局点未开此功能
    if chain.get('anchor_from_license'):
        lic_layer = None
        for l in (chain.get('layers') or []):
            if l.get('kind') == 'license_items':
                lic_layer = l
                break
        if lic_layer is not None:
            _st, _matched = _scan_lic_layer(commands, lic_layer, lic_items)
            hit_n = sum(1 for m in _matched for h in (m.get('hits') or []))
            present_n = hit_n
            anchors = [{'cmd': 'license_items', 'n': hit_n,
                        'first_seq': None,
                        'items': [m.get('pattern') for m in _matched]}]

    if present_n == 0:
        return {'chain': chain['chain_id'], 'name': chain['name'],
                'status': 'not_present', 'note': '本局点无此形态（锚定命令全缺）',
                'layers': [], 'anchors': anchors}

    layers_out = []
    for raw_layer in chain.get('layers', []):
        layer = dict(raw_layer)
        layer.setdefault('kind', 'cmd_set')
        if layer.get('kind') == 'license_items':
            status, matched = _scan_lic_layer(commands, layer, lic_items)
            layers_out.append({'id': layer['id'], 'name': layer['name'],
                               'kind': 'license_items', 'status': status,
                               'items': matched})
        else:
            hits = _scan_cmd_set(commands, layer.get('cmds', []))
            status = _layer_status(layer, hits)
            layers_out.append({'id': layer['id'], 'name': layer['name'],
                               'kind': 'cmd_set', 'status': status, 'cmds': hits,
                               'param_observations': layer.get('param_observations', [])})
    # verdict_rules 顺序求值
    status_map = {l['id']: l['status'] for l in layers_out}
    verdict = None
    for rule in chain.get('verdict_rules', []):
        when = rule.get('when', {})
        if all(status_map.get(k) == v for k, v in when.items()):
            verdict = {'status': rule['status'], 'note': rule['note']}
            break
    if verdict is None:
        verdict = {'status': 'partial', 'note': '未匹配判定规则（需审视）'}
    out = {'chain': chain['chain_id'], 'name': chain['name'], **verdict,
           'anchor_value': anchor_value, 'anchor_param': ap,
           'layers': layers_out, 'anchors': anchors,
           'refs': _eval_refs(chain, commands),
           'equiv_substitutes': chain.get('equiv_substitutes', [])}
    # ⚠ 授权类链：透传 特性→授权项 映射（供生成侧填 LICITEM 值）
    if chain.get('lic_by_feature'):
        out['lic_by_feature'] = chain['lic_by_feature']
    return out


def run(commands=None, meta=None, exp_path=None, lic_items=None):
    if commands is None:
        parsed = parse_exp(exp_path)
        commands = parsed['commands']
        meta = meta or parsed['meta_hdr']
    product = meta.get('me_type', 'UDG')
    from p1_parse import lic_switch_stats
    lic_items = lic_items or lic_switch_stats(commands).get('items', {})
    schemas = load_schemas(product)
    return {'chain_verdicts': [evaluate_chain(c, commands, lic_items)
                               for c in schemas.values()],
            'schemas': list(schemas.keys())}


if __name__ == '__main__':
    import json
    import sys
    exp = sys.argv[1] if len(sys.argv) > 1 else None
    if not exp:
        print('usage: p3_chains.py <exp.txt>')
        sys.exit(1)
    res = run(exp_path=exp)
    for v in res['chain_verdicts']:
        lay = ' '.join(f"{l['id']}:{l['status']}" for l in v['layers'])
        print(f"{v['chain']} {v['name']}: [{v['status']}] {v['note']}  |  {lay}")

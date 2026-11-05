#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
extract_groundtruth.py — 从 exp.txt 提取特性配置链 groundtruth（数据驱动）

流程：
    exp.txt ──(chains.yaml 规则)──> groundtruth.json

规则引擎：chains.yaml 定义特性锚点 + 直接关联 + 多跳扩展关联。
本脚本不含任何局点特例值（VRF 名/IP/编号全部运行时从 exp.txt 解析）。

用法：
    python3 extract_groundtruth.py <exp.txt> [--rules rules/chains.yaml] \\
        [--features dual_domain_dnn,billing_chain] [-o groundtruth.json]

输出 JSON 结构：
{
  "meta": {"exp": ..., "me_type": ..., "site": ..., "rules": ...},
  "features": {
    "<feature_id>": {
      "instances": {
        "<anchor_value>": {
          "commands": [{"cmd","text","seq","params"}...],
          "external_refs": [{"cmd","text","seq","params","via_rule"}...]
        }
      },
      "key_param_stats": {"<CMD>::<PARAM>": {"<value>": count, ...}},
      "naming": {"<PARAM>": ["<value>", ...]},
      "resource_pools": {"<pool_name>": [<int>, ...]}
    }
  }
}
"""

import argparse
import json
import os
import re
import sys
from collections import OrderedDict, Counter

try:
    import yaml
except ImportError:
    print("需要 PyYAML：pip3 install pyyaml", file=sys.stderr)
    sys.exit(1)


# ═══ MML 命令解析 ═══════════════════════════════════════════

def parse_command(line):
    """解析一行 MML 命令 → (cmd_type, params dict)。
    支持：ADD CMD:PARAM="v",PARAM2=123;  （值可带引号/数字，末尾分号）
    """
    s = line.strip().rstrip(';').strip()
    if ':' in s:
        head, params_str = s.split(':', 1)
    else:
        head, params_str = s, ''
    head = head.strip()
    # cmd_type 取 "VERB OBJECT"（如 ADD L3VPNINST），不带多空格
    m = re.match(r'^(\w+)\s+([\w-]+)$', head)
    if not m:
        m = re.match(r'^(\w+)\s+([\w.-]+)$', head)
    cmd_type = f"{m.group(1)} {m.group(2)}" if m else head
    params = {}
    # 参数解析：KEY="V" 或 KEY=VAL（VAL 不含逗号/分号）
    for pm in re.finditer(r'(\w+)=(?:"([^"]*)"|([^,;]+))', params_str):
        key, v1, v2 = pm.group(1), pm.group(2), pm.group(3)
        params[key] = v1 if v1 is not None else (v2 or '').strip()
    return cmd_type, params


def parse_exp(exp_path):
    """读取 exp.txt → (commands, comments, meta)。
    commands: OrderedDict seq→(raw_line, cmd_type, params)
    """
    with open(exp_path, encoding='gbk', errors='replace') as f:
        lines = f.readlines()
    commands = OrderedDict()
    comments = {}
    meta = {"me_type": "", "version": "", "site": ""}
    for i, line in enumerate(lines, 1):
        s = line.strip()
        if not s:
            continue
        if s.startswith('/*'):
            comments[i] = s
            m = re.search(r'ME Type=(\w+)', s)
            if m:
                meta['me_type'] = m.group(1)
            m = re.search(r'Version=([\d.]+)', s)
            if m:
                meta['version'] = m.group(1)
            continue
        if s.startswith('#'):
            continue
        cmd_type, params = parse_command(s)
        commands[i] = (s, cmd_type, params)
    # 站点名：MOD ME:MELN= 或 SET UPINFO:HOSTNAME=
    for seq, (raw, ct, params) in commands.items():
        if ct == 'MOD ME' and params.get('MELN'):
            meta['site'] = params['MELN']
            break
        if ct == 'SET UPINFO' and params.get('HOSTNAME'):
            meta['site'] = params['HOSTNAME']
            break
    return commands, comments, meta


# ═══ 规则加载 ═══════════════════════════════════════════════

def load_rules(rules_path):
    with open(rules_path, encoding='utf-8') as f:
        data = yaml.safe_load(f)
    return data.get('features', {})


# ═══ Groundtruth 提取 ═══════════════════════════════════════

def anchor_matches(anchor, cmd_type, params):
    """锚点匹配：命令类型 + 锚点参数存在 + （可选）值 pattern"""
    if anchor['command'] != cmd_type:
        return False
    val = params.get(anchor['param'])
    if val is None:
        return False
    pat = anchor.get('pattern')
    if pat and not re.match(pat, val):
        return False
    return True


def collect_instance(commands, anchor, feature_rule):
    """对一个锚点实例值，收集完整命令链。
    返回 (instance_commands, external_refs)：
      instance_commands: list of dict(cmd,text,seq,params)
      external_refs:     归属其他 VRF 但被引用的命令（弱关联）
    """
    anchor_val = anchor['value']
    chain = feature_rule.get('chain', {})
    direct_rules = chain.get('direct', [])
    extend_rules = chain.get('extend', [])

    # 直接关联：via 参数值 == 锚点值
    collected = {}          # seq → (cmd_type, raw, params, via_rule)
    for seq, (raw, ct, params) in commands.items():
        for dr in direct_rules:
            if dr['command'] == ct and params.get(dr['via']) == anchor_val:
                collected[seq] = (ct, raw, params, f"direct:{dr['via']}")
                break

    # 多跳扩展关联：迭代直到稳定
    # 每轮：对每个 extend 规则，从"已收集命令"中取 from 命令的 join 参数值集合 V，
    #       收集 match_params 任一参数 ∈ V 的命令（且未被收集）
    # 归属判定：collect 项可带 belongs=false（如跨 VRF 的 NETWORKROUTE 归属承载 VRF），
    #           默认 belongs=true 并入本实例链。
    changed = True
    iteration = 0
    while changed and iteration < 20:
        changed = False
        iteration += 1
        for er in extend_rules:
            # 已收集命令中 from 类型 → join 参数值集合
            value_set = set()
            for seq, (ct, raw, params, via) in collected.items():
                if ct == er['from']:
                    for jp in er.get('join', []):
                        v = params.get(jp)
                        if v:
                            value_set.add(v)
            if not value_set:
                continue
            for coll in er.get('collect', []):
                belongs = coll.get('belongs', True)
                for seq, (raw, ct, params) in commands.items():
                    if seq in collected:
                        continue
                    if ct != coll['command']:
                        continue
                    if any(params.get(mp) in value_set for mp in coll.get('match_params', [])):
                        collected[seq] = (ct, raw, params,
                                          f"extend:{er['name']}" + ("" if belongs else ":ext"))
                        changed = True

    # 分类：锚点 VRF 自己的命令 vs 外部引用（跨 VRF）
    # via 带 ":ext" 后缀 = 规则显式声明归属外部（belongs=false）
    instance_cmds, ext_refs = [], []
    for seq, (ct, raw, params, via) in sorted(collected.items()):
        item = {"cmd": ct, "text": raw, "seq": seq, "params": params}
        if via.endswith(':ext'):
            item["via_rule"] = via
            ext_refs.append(item)
        else:
            instance_cmds.append(item)
    return instance_cmds, ext_refs


def extract_feature(commands, feature_id, frule):
    """提取一个特性的所有实例 + 跨实例统计"""
    result = {"instances": OrderedDict()}

    # 1. 枚举锚点实例
    anchor_specs = frule.get('anchors', [])
    anchor_instances = []  # (cmd_type, param, value)
    seen = set()
    for seq, (raw, ct, params) in commands.items():
        for a in anchor_specs:
            if anchor_matches(a, ct, params):
                key = (a['command'], a['param'], params[a['param']])
                if key not in seen:
                    seen.add(key)
                    anchor_instances.append(
                        {"command": a['command'], "param": a['param'],
                         "value": params[a['param']]})
    if not anchor_instances:
        return None

    # 2. 每实例收集链
    for a in anchor_instances:
        inst_cmds, ext_refs = collect_instance(commands, a, frule)
        result["instances"][a["value"]] = {
            "anchor": a,
            "commands": inst_cmds,
            "external_refs": ext_refs,
        }

    # 3. key_params 值分布（跨实例汇总，用于生成结果值一致性对照）
    kp_stats = {}
    for kp in frule.get('key_params', []):
        k = f"{kp['command']}::{kp['param']}"
        counter = Counter()
        for inst in result["instances"].values():
            for c in inst["commands"]:
                if c["cmd"] == kp['command']:
                    v = c["params"].get(kp['param'])
                    if v is not None:
                        counter[v] += 1
        if counter:
            kp_stats[k] = dict(counter.most_common())
    result["key_param_stats"] = kp_stats

    # 4. naming 命名规律：pattern（来自规则）+ 现网实例值
    naming = {}
    for nparam, npattern in frule.get('naming', {}).items():
        vals = set()
        for inst in result["instances"].values():
            for c in inst["commands"]:
                v = c["params"].get(nparam)
                if v:
                    vals.add(v)
        if vals:
            naming[nparam] = {"pattern": npattern, "instances": sorted(vals)}
    result["naming"] = naming

    # 5. resource_pools 资源编号池
    pools = {}
    for rp in frule.get('resource_pools', []):
        nums = []
        for inst in result["instances"].values():
            for c in inst["commands"]:
                if c["cmd"] != rp['command']:
                    continue
                if rp.get('filter') and not re.match(rp['filter'], c["text"]):
                    continue
                v = c["params"].get(rp['param'], '')
                m = re.search(rp['regex'], v)
                if m:
                    nums.append(int(m.group(1)))
        if nums:
            pools[rp['name']] = sorted(set(nums))
    result["resource_pools"] = pools

    return result


# ═══ Main ═══════════════════════════════════════════════════

def main():
    ap = argparse.ArgumentParser(description='从 exp.txt 提取特性配置链 groundtruth')
    ap.add_argument('exp', help='exp.txt 路径')
    ap.add_argument('--rules', default=os.path.join(
        os.path.dirname(os.path.abspath(__file__)), '..', 'rules', 'chains.yaml'),
        help='特性链规则 YAML')
    ap.add_argument('--features', default='', help='逗号分隔特性过滤，空=全部')
    ap.add_argument('-o', '--output', default='', help='输出 JSON 路径（默认 exp 同目录 groundtruth.json）')
    args = ap.parse_args()

    rules_path = os.path.abspath(args.rules)
    exp_path = os.path.abspath(args.exp)
    if not os.path.exists(exp_path):
        print(f"❌ exp 文件不存在: {exp_path}", file=sys.stderr)
        sys.exit(1)
    if not os.path.exists(rules_path):
        print(f"❌ 规则文件不存在: {rules_path}", file=sys.stderr)
        sys.exit(1)

    print(f"解析 exp: {exp_path}")
    commands, comments, meta = parse_exp(exp_path)
    print(f"  命令数: {len(commands)}  网元: {meta['me_type']} v{meta['version']}  站点: {meta['site']}")

    features = load_rules(rules_path)
    wanted = [f.strip() for f in args.features.split(',') if f.strip()] if args.features else []

    out = {
        "meta": {
            "exp": exp_path,
            "rules": rules_path,
            "me_type": meta['me_type'],
            "version": meta['version'],
            "site": meta['site'],
            "total_commands": len(commands),
        },
        "features": OrderedDict(),
    }

    for fid, frule in features.items():
        if wanted and fid not in wanted:
            continue
        res = extract_feature(commands, fid, frule)
        if res is None:
            print(f"  ⏭  {fid}: 无锚点实例（特性未配置于本局点）")
            continue
        n_inst = len(res["instances"])
        n_cmd = sum(len(i["commands"]) for i in res["instances"].values())
        print(f"  ✅ {fid}: {n_inst} 个实例, {n_cmd} 条链命令")
        out["features"][fid] = res

    if not out["features"]:
        print("❌ 无任何特性可提取，请检查 --features 或规则锚点", file=sys.stderr)
        sys.exit(1)

    out_path = args.output or os.path.join(os.path.dirname(exp_path), 'groundtruth.json')
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    print(f"\n✅ groundtruth 已保存: {out_path}")


if __name__ == '__main__':
    main()

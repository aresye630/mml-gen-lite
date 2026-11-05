#!/usr/bin/env python3
"""关键参数扫描器：从特性文档示例命令中识别"值锚定"候选参数。

背景：特性指纹的判定依据不只是命令类型——同一命令内有关键参数
（功能开关/版本/模式，如 IPVERSION=IPv4|IPv6、SWITCH=ENABLE），
与 LICITEM 授权项同等重要。这些参数值决定特性的具体形态，
exp 匹配时须值锚定。

方法（数据驱动，不硬编码参数名）：
1. 聚合全部特性文档示例命令的 (cmd, param) → 值集合
2. 形态过滤：值集合 2~8 个、全部值 ≤ 8 字符（排除实例名/ID/长名称）
3. 语义过滤：参数名匹配"功能标识"模式（VERSION/TYPE/SWITCH/FLAG/MODE/
   ENABLE/ALLOC/LEVEL/PROTOCOL/STATE/CREATETYPE/POLICYTYPE/ACTION 等）
4. 输出候选清单（含涉及文档数、取值），人工确认后写入 param_anchor.yaml

用法:
  python3 scan_key_params.py --feat-md <特性文档库> [-o rules/key_params_candidates.md]
"""
import argparse
import json
import os
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gen_feature_all as gfa  # noqa: E402

# 参数名"功能标识"语义模式（大小写不敏感；匹配的是参数名语义，非具体参数名）
SEMANTIC_RE = re.compile(
    r'(VERSION|ADDRESSTYPE|AFTYPE|SWITCH|FLAG|MODE|ALLOCTYPE|ENABLE|LEVEL|'
    r'PROTOCOL|STATE|CREATETYPE|POLICYTYPE|ACTION|BEARERTYPE|QOS|L34|'
    r'IPVERSION|NEXTHOP|USERTYPE|CHARGETYPE|NETTYPE|IFTYPE|AUTOCFG|SESS)',
    re.I)
# 明显实例/标识类参数名（排除）
EXCLUDE_PARAM = re.compile(
    r'^(VRFNAME|DESCRIPTION|LOCALIFNAME|VPNINSTANCE|POOLNAME|MEID|TRUNKIFNAME|'
    r'MASKLENGTH|MASKLEN|PREFIXLEN|IFMTU|PREFERENCE|IFSTATITVL|SRCADDR|DESTADDR|'
    r'NAME|ID|INDEX|NUMBER|COUNT|TIMES|THRESHOLD|INTERVAL|TIMEOUT|PORT|'
    r'.*NAME)$', re.I)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--feat-md', required=True, dest='feat_dir')
    ap.add_argument('-o', '--out', default='rules/key_params_candidates.md')
    ap.add_argument('--json-out', default='rules/key_params_candidates.json')
    args = ap.parse_args()

    docs = gfa.load_feature_docs(args.feat_dir)
    vp = defaultdict(set)      # (cmd, param) -> set(values)
    ncmd = Counter()           # cmd -> 出现次数
    ndoc = Counter()           # (cmd, param) -> 涉及文档数
    doc_ids = defaultdict(set)
    for i, d in enumerate(docs, 1):
        seen = set()
        for s in d['scripts']:
            for ln in s.split('\n'):
                pr = gfa.parse_mml_cmd(ln)
                if pr:
                    cmd, params = pr
                    ncmd[cmd] += 1
                    for k, v in params.items():
                        if v:
                            vp[(cmd, k)].add(v)
                            seen.add((cmd, k))
        for ck in seen:
            doc_ids[ck].add(i)
    for ck, ids in doc_ids.items():
        ndoc[ck] = len(ids)

    cand = []
    for (cmd, p), vals in vp.items():
        if not (2 <= len(vals) <= 8):
            continue
        if not all(len(v) <= 8 for v in vals):
            continue
        if EXCLUDE_PARAM.match(p):
            continue
        if not SEMANTIC_RE.search(p):
            continue
        cand.append({
            'cmd': cmd, 'param': p, 'values': sorted(vals),
            'doc_count': ndoc[(cmd, p)], 'cmd_count': ncmd[cmd],
        })
    cand.sort(key=lambda x: (-x['doc_count'], -x['cmd_count'], x['cmd'], x['param']))

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    L = ['# 关键参数候选（值锚定扩展，待人工确认）', '',
         f'- 候选 {len(cand)} 条：值集合 2~8 个、值 ≤ 8 字符、参数名语义匹配功能标识',
         '- 确认后写入 rules/param_anchor.yaml（数据驱动，不硬编码）', '',
         '| 命令 | 参数 | 取值 | 涉及文档数 | 命令出现次数 |',
         '|---|---|---|---|---|']
    for c in cand:
        L.append(f'| {c["cmd"]} | {c["param"]} | {" / ".join(c["values"])} | '
                 f'{c["doc_count"]} | {c["cmd_count"]} |')
    out.write_text('\n'.join(L), encoding='utf-8')
    Path(args.json_out).write_text(
        json.dumps(cand, ensure_ascii=False, indent=1), encoding='utf-8')
    print(f'✅ 候选 {len(cand)} 条 → {out}')


if __name__ == '__main__':
    main()

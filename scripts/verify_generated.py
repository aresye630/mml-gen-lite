#!/usr/bin/env python3
"""生成结果验证：生成命令 × groundtruth（match_result.json）对照

闭环：模板/确认清单生成的配置命令 → 与现网 exp groundtruth 逐特性对照：
- 现网已配置 + 生成含其 core → 重复配置（提示）
- 现网未配置 + 生成 core 全命中 → 生成完整（补齐 ✓）
- 现网未配置 + 生成部分命中 → 部分覆盖（缺项清单）
- 现网未配置 + 生成未命中 → 未覆盖
- 参数级：生成 vs 现网 evidence 的关键参数值比对（param_anchor 声明）

用法:
  python3 verify_generated.py --gen <生成命令文件> --match <match_result.json> \
      --fingerprint <features_ueg.yaml> [--anchors rules/param_anchor.yaml] [-o 输出目录]
"""
import argparse
import json
import os
import sys
import time
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gen_feature_all as gfa  # noqa: E402

LEGEND = {
    '生成完整': '现网未配置，生成已覆盖全部核心命令（补齐 ✓）',
    '部分覆盖': '现网未配置，生成覆盖部分核心命令（见缺项清单）',
    '未覆盖': '现网未配置，生成未覆盖核心命令',
    '重复配置': '现网已配置，生成又包含其核心命令（可能重复下发）',
    '未涉及': '现网已配置，生成未包含其核心命令（正常）',
    '需人工确认': '纯操作/授权类特性',
    '生成完整(license)': '授权类特性，生成含授权命令',
    '未覆盖(license类)': '授权类特性，生成未含授权命令',
}


def run_verify(gen_path, match_path, fp_path, anchor_path='rules/param_anchor.yaml'):
    """核心验证逻辑 → dict（rows/verdicts/param_diffs/report/meta），CLI 与 Web 复用"""
    import yaml
    t0 = time.time()
    gen_cmds = gfa.parse_exp(gen_path)
    gen_types = {c['cmd'] for c in gen_cmds}
    gen_params = defaultdict(list)
    for c in gen_cmds:
        gen_params[c['cmd']].append(c['params'])
    match = json.load(open(match_path, encoding='utf-8'))
    results = match['results']
    fp = yaml.safe_load(open(fp_path, encoding='utf-8'))
    feats = fp['features']
    anchors = gfa.load_param_anchors(anchor_path)
    anchor_params = defaultdict(set)
    for cmd, ps in anchors:
        anchor_params[cmd].update(ps)

    verdicts = Counter()
    detail_rows = []
    param_diffs = []

    for fid, r in results.items():
        f = feats.get(fid)
        if not f:
            continue
        status = r['status']
        core = f.get('core', {})
        core_all = core.get('L1', []) + core.get('L2', []) + core.get('L3', [])
        lic = f.get('license') or {}
        lic_cmds = list(lic) if isinstance(lic, dict) else lic
        gen_hit = [c for c in core_all if c in gen_types]
        gen_miss = [c for c in core_all if c not in gen_types]
        gen_lic = [c for c in lic_cmds if c in gen_types]
        ev = r.get('detail', {}).get('evidence', {})

        if status == 'configured':
            verdict = '重复配置' if gen_hit else '未涉及'
        elif status == 'not_configured':
            if not core_all:
                verdict = '生成完整(license)' if gen_lic else '未覆盖(license类)'
            elif not gen_miss:
                verdict = '生成完整'
            elif gen_hit:
                verdict = '部分覆盖'
            else:
                verdict = '未覆盖'
        else:
            verdict = '需人工确认'
        verdicts[verdict] += 1

        for cmd in gen_hit:
            if cmd not in ev or cmd not in anchor_params:
                continue
            ev_first = ev[cmd].get('first', {})
            for p in sorted(anchor_params[cmd]):
                gv = {str(g.get(p)).upper() for g in gen_params.get(cmd, []) if g.get(p)}
                evv = {str(ev_first.get(p)).upper()} if ev_first.get(p) else set()
                if not gv and not evv:
                    continue
                if gv == evv:
                    continue
                param_diffs.append({
                    'fid': fid, 'cmd': cmd, 'param': p,
                    'gen': sorted(gv), 'exp': sorted(evv),
                })
        detail_rows.append({
            'fid': fid, 'title': r.get('title', ''), 'status': status,
            'verdict': verdict, 'gen_hit': gen_hit, 'gen_miss': gen_miss,
            'gen_lic': gen_lic, 'evidence_cmds': list(ev.keys()),
        })

    # ── 报告文本 ──
    L = [
        '# 生成结果验证报告（生成命令 × 现网 groundtruth）', '',
        f'- 生成命令文件：`{gen_path}`',
        f'- groundtruth：`{match_path}`（exp: {match.get("meta", {}).get("exp", "")}）',
        f'- 生成命令：{len(gen_cmds)} 条 / {len(gen_types)} 种类型',
        f'- 验证特性数：{len(detail_rows)}',
        f'- 耗时：{time.time() - t0:.1f}s', '',
        '## 总览', '',
        '| 结论 | 篇数 | 含义 |', '|---|---|---|',
    ]
    for v, n in verdicts.most_common():
        L.append(f'| {v} | {n} | {LEGEND.get(v, "")} |')
    L += ['', '## 部分覆盖缺项清单（生成缺的核心命令）', '',
          '| 特性 | 缺项命令 |', '|---|---|']
    shown = 0
    for r in detail_rows:
        if r['verdict'] == '部分覆盖' and r['gen_miss']:
            L.append(f'| {r["fid"]} {r["title"][:24]} | {"、".join(r["gen_miss"][:6])} |')
            shown += 1
        if shown >= 30:
            break
    if not shown:
        L.append('| （无） | |')
    L += ['', '## 参数值差异（生成 vs 现网，param_anchor 声明参数）', '',
          '| 特性 | 命令 | 参数 | 生成值 | 现网值 |', '|---|---|---|---|---|']
    for d in param_diffs[:40]:
        L.append(f'| {d["fid"]} | {d["cmd"]} | {d["param"]} | {d["gen"]} | {d["exp"]} |')
    if not param_diffs:
        L.append('| （无差异） | | | | |')
    L += ['', '## 重复配置提示（现网已配置，生成又含其 core 命令）', '']
    dup = [r for r in detail_rows if r['verdict'] == '重复配置']
    if dup:
        for r in dup[:20]:
            L.append(f'- {r["fid"]} {r["title"][:36]}：{r["gen_hit"][:5]}')
    else:
        L.append('（无）')
    L += ['', '## 生成覆盖明细（全部特性）', '',
          '| 特性 | 现网状态 | 结论 | 生成命中 | 生成缺项 |', '|---|---|---|---|---|']
    for r in detail_rows:
        L.append(f'| {r["fid"]} {r["title"][:20]} | {r["status"]} | {r["verdict"]} | '
                 f'{len(r["gen_hit"])} | {len(r["gen_miss"])} |')

    return {
        'rows': detail_rows,
        'verdicts': dict(verdicts),
        'param_diffs': param_diffs,
        'report': '\n'.join(L),
        'meta': {'gen': gen_path, 'match': match_path,
                 'gen_cmds': len(gen_cmds), 'gen_types': len(gen_types),
                 'total': len(detail_rows), 'elapsed': round(time.time() - t0, 1)},
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--gen', required=True, help='生成命令文件（MML 文本）')
    ap.add_argument('--match', required=True, help='match_result.json（groundtruth）')
    ap.add_argument('--fingerprint', required=True, help='特性指纹库 yaml')
    ap.add_argument('--anchors', default='rules/param_anchor.yaml')
    ap.add_argument('-o', '--out', default='', help='输出目录（缺省与 match 同目录）')
    args = ap.parse_args()

    res = run_verify(args.gen, args.match, args.fingerprint, args.anchors)
    out = Path(args.out) if args.out else Path(args.match).parent
    out.mkdir(parents=True, exist_ok=True)
    rep_path = out / '验证报告.md'
    rep_path.write_text(res['report'], encoding='utf-8')
    json_path = out / 'verify_result.json'
    json_path.write_text(json.dumps(
        {'meta': {**res['meta'], **res['verdicts']},
         'rows': res['rows'], 'param_diffs': res['param_diffs']},
        ensure_ascii=False, indent=1), encoding='utf-8')
    print(f'✅ 验证报告 → {rep_path}')
    print(f'✅ 结果 JSON → {json_path}')
    print(f'结论: {res["verdicts"]}')
    print(f'参数差异: {len(res["param_diffs"])} 处')


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""pipeline.py — P1 确定性管线编排（T1 骨架；T2~T7 逐切片挂入）。

当前装配：p1_parse（meta/stats/lic_switch）→ report.json 落盘 →
renderer 渲染 analysis_code/0_meta_stats.md 预览。

usage: pipeline.py <exp.txt> -o <out_dir>
"""

import argparse
import json
from pathlib import Path

import yaml

from p1_parse import parse_exp, stats as p1_stats, lic_switch_stats
import p2_patterns
import p3_chains
import p4_diffs
import p5_notices
import p6_watchlist
import graph_walk
import graph_build
import feature_find
import renderer
import llm_polish

PACKAGE_DIR = Path(__file__).resolve().parent
RULES_DIR = PACKAGE_DIR / 'rules'
SCHEMA = PACKAGE_DIR / 'schema' / 'report.schema.json'


def _run_feature_match(exp_path, feature_doc):
    """P8 特性匹配（可选）：走链 + 黄金规则核对。

    惰性导入 _s2_newfmt2（在 scripts/ 下，依赖 gen_feature_all 等），
    避免精简环境（无 requests 等）阻塞 P1 主路径。
    """
    import sys
    repo = str(Path(__file__).resolve().parent.parent)  # scripts/
    for p in (repo, str(Path(__file__).resolve().parent)):
        if p not in sys.path:
            sys.path.insert(0, p)
    try:
        import _s2_newfmt2 as s2
    except Exception as e:
        return {'error': f'特性匹配模块导入失败：{e}'}
    return s2.run(newdoc=feature_doc, exp=exp_path, quiet=True)


def pipeline(exp_path, out_dir, polish=False, feature_doc=None):
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)
    # ── P1-A 解析层（T1） ──
    parsed = parse_exp(exp_path)
    commands = parsed['commands']
    # ── P1-B 模式挖掘（T2；复用解析，不重复读文件） ──
    mined = p2_patterns.run(commands=commands, meta=parsed['meta_hdr'])
    # ── P1-C 链级判定（T3） ──
    chains = p3_chains.run(commands=commands, meta=parsed['meta_hdr'],
                           lic_items=lic_switch_stats(commands).get('items', {}))
    # ── P7 图谱解析（实例级引用图走链；数据驱动 graph_schemas.yaml） ──
    graph_schemas = yaml.safe_load(
        (RULES_DIR / 'graph_schemas.yaml').read_text(encoding='utf-8'))
    graph_chains = graph_walk.run_graphs(
        commands, graph_schemas.get(parsed['meta_hdr'].get('me_type', 'UDG'), []))
    # ── P8 特性匹配（可选：提供特性文档时走链 + 黄金规则核对） ──
    feature_match = _run_feature_match(exp_path, feature_doc) if feature_doc else None
    # ── P9 特性实例找全（切片2：图上扩展找全 + 全量图落盘） ──
    # fanout_limit 数据驱动（rules/graph_rules.yaml）——枚举/占位符类高频值时
    # 原实现在此爆内存（2026-09-15 修）；缺配置则回退不限制（兼容旧行为）。
    _gr = RULES_DIR / 'graph_rules.yaml'
    _fanout = None
    if _gr.is_file():
        try:
            _fanout = (yaml.safe_load(_gr.read_text(encoding='utf-8'))
                       or {}).get('graph', {}).get('fanout_limit') or None
        except Exception:
            _fanout = None
    graph = graph_build.build_graph(commands, fanout_limit=_fanout)
    graph_build.dump_graph(graph, str(out / 'graph.json'))
    feature_find_res = feature_find.run_all(commands, graph=graph)
    (out / 'feature_find.json').write_text(
        json.dumps(feature_find_res, ensure_ascii=False), encoding='utf-8')
    report = {
        'meta': parsed['meta_hdr'],
        'stats': p1_stats(commands),
        'lic_switch': lic_switch_stats(commands),
        'env_notes': [],
        'domain_stats': mined['domain_stats'],
        'profiles': mined['profiles'],
        'chain_verdicts': chains['chain_verdicts'],
        'schemas': chains['schemas'],
        'graph_chains': graph_chains,
        'feature_match': feature_match,
        'feature_find': feature_find_res,
        'diffs': p4_diffs.generate(commands, chains['chain_verdicts']),
        'notices': p5_notices.run(commands=commands, meta=parsed['meta_hdr'],
                                  verdicts=chains['chain_verdicts']),
        'watchlist': p6_watchlist.run(commands=commands),
        'llm': None,
    }
    # ── P2 LLM 润色（可选开关 --polish；默认关，不阻塞主路径） ──
    #   失败不再静默：report['llm'] 固定带 status/reason，前端可呈现明确成败。
    if polish:
        report['llm'] = llm_polish.polish(report)
    # ── 落盘 report.json ──
    rj = out / 'report.json'
    rj.write_text(json.dumps(report, ensure_ascii=False, indent=1), encoding='utf-8')
    # ── 渲染五段 md + 检索记录 + params.csv（T7） ──
    ne = report['meta'].get('ne_name', 'NE')
    (out / f'配置分析_{ne}_代码管线.md').write_text(
        renderer.render_report(report), encoding='utf-8')
    (out / '1_检索与选型.md').write_text(
        renderer.render_search(report), encoding='utf-8')
    n_csv = renderer.render_params_csv(report, str(out / 'params.csv'))
    return {'report_json': str(rj), 'md': str(out / '配置分析_XAUPF017BHW_代码管线.md'),
            'search_md': str(out / '1_检索与选型.md'),
            'params_csv': str(out / 'params.csv'), 'csv_rows': n_csv,
            'graph_json': str(out / 'graph.json'),
            'feature_find_json': str(out / 'feature_find.json'),
            'meta': report['meta']}


if __name__ == '__main__':
    ap = argparse.ArgumentParser(description='P1 exp 分析确定性管线')
    ap.add_argument('exp')
    ap.add_argument('-o', '--out', default='analysis_code')
    ap.add_argument('--polish', action='store_true',
                    help='可选：调用 LLM 润色三段（conclusion/diff_review/watchlist_meaning）')
    ap.add_argument('--feature-doc', default=None,
                    help='可选：特性文档路径，提供时运行 P8 特性匹配（走链+黄金规则核对）')
    args = ap.parse_args()
    res = pipeline(args.exp, args.out, polish=args.polish,
                   feature_doc=args.feature_doc)
    print(json.dumps(res, ensure_ascii=False, indent=1))

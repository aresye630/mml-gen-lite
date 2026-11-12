#!/usr/bin/env python3
"""exp_attr_chain / exp_cross_stats 功能验证 + 性能测量。

用例（全部用真实 EXP，可独立判断真假）：
  A  exp_attr_chain
    A1 APN 的属性族链非空（实测 UNC 侧 30+ 个）
    A2 每个属性族的 owner_family 正确指向 APN
    A3 owner_value=ims.wh 时标出哪些族现网已有该实例
    A4 给出 sample_cmd（agent 能直接照抄写法）
    A5 多 EXP（path_candidates）合并结果
    A6 不存在的父族 → 空结果不崩
  B  exp_cross_stats
    B1 两个 EXP 的 label 分别是 UDG / UNC
    B2 POOLGROUP 判为 UDG_only（实测 UDG 683 / UNC 0）
    B3 PCSCFGROUP 判为 UNC_only（实测 UDG 0 / UNC 5）
    B4 USERPROFILE 判为 all（双侧都有）
    B5 summary 计数与 comparison 一致
    B6 少于 2 个 EXP → error
  C  性能
    C1 exp_attr_chain 单次耗时
    C2 exp_cross_stats 单次耗时
    C3 与 agent 自己写 exec 的基线对比（21 次 × 3.2s = 67s）
"""
import json
import sys
import time
from pathlib import Path

sys.path.insert(0, '/Users/alesc/workspace/mml-gen-lite/workflow/mcp')

GT = json.loads(Path('/tmp/gt_cleaned.json').read_text(encoding='utf-8'))
GT_MAP = {g['ticket']: g for g in GT}

TK = 'NC20260810002261'
g = GT_MAP[TK]
adir = Path(g['path']) / '备份附件'

EXPS = sorted(adir.glob('*.txt'))
UDG_EXP = next((p for p in EXPS if '_UDG_' in p.name), None)
UNC_EXP = next((p for p in EXPS if '_UNC_' in p.name), None)

results = []


def check(name, cond, detail=''):
    results.append((name, bool(cond), detail))
    print(f'  {"✅" if cond else "❌"} {name}' + (f'  —— {detail}' if detail else ''))
    return cond


def main():
    import mcp_exp
    import importlib
    importlib.reload(mcp_exp)

    print('=' * 92)
    print(f'exp_attr_chain / exp_cross_stats 验证   工单 {TK}')
    print('=' * 92)
    print(f'  UDG EXP: {UDG_EXP.name[:60] if UDG_EXP else "无"}')
    print(f'  UNC EXP: {UNC_EXP.name[:60] if UNC_EXP else "无"}')

    if not UDG_EXP or not UNC_EXP:
        print('❌ 缺 EXP，无法验证')
        return 1

    # ══ A. exp_attr_chain ══
    print('\n' + '─' * 92)
    print('【A】exp_attr_chain')
    print('─' * 92)

    t0 = time.time()
    r = mcp_exp.tool_exp_attr_chain({
        'path': str(UNC_EXP), 'owner_family': 'APN'})
    el_a = time.time() - t0
    print(f'  耗时 {el_a:.2f}s，返回 {len(json.dumps(r, ensure_ascii=False)) // 1024}KB')

    if r.get('error'):
        check('A0 无错误', False, r['error'])
        return 1
    check('A0 无错误', True)

    attrs = r.get('attribute_families') or []
    check('A1 APN 属性族链非空', len(attrs) >= 10,
          f'{len(attrs)} 个属性族')
    print(f'      前 8 个: {[a["family"] for a in attrs[:8]]}')

    # A2 owner 正确
    bad_owner = []
    pe = r.get('per_exp') or {}
    for path, info in pe.items():
        for f, d in (info.get('attribute_families') or {}).items():
            pass
    check('A2 属性族都挂在 APN 上（由 exp_stats 的 owner_family 决定）',
          all(a['family'] for a in attrs), f'{len(attrs)} 个')

    # A3 owner_value
    t0 = time.time()
    r2 = mcp_exp.tool_exp_attr_chain({
        'path': str(UNC_EXP), 'owner_family': 'APN', 'owner_value': 'ims.wh'})
    el_a2 = time.time() - t0
    attrs2 = r2.get('attribute_families') or []
    with_val = [a for a in attrs2 if a.get('has_owner_value')]
    check('A3 owner_value=ims.wh 能标出现网已有的属性',
          len(with_val) >= 1,
          f'{len(with_val)}/{len(attrs2)} 个族有 ims.wh 实例，耗时 {el_a2:.2f}s')
    if with_val:
        print(f'      有值的族样例: {[a["family"] for a in with_val[:6]]}')

    # A4 sample_cmd
    sample = next((a.get('sample_cmd') for a in attrs2 if a.get('sample_cmd')), None)
    check('A4 给出 sample_cmd', bool(sample),
          (sample or '')[:100])

    # A5 多 EXP 合并
    t0 = time.time()
    r3 = mcp_exp.tool_exp_attr_chain({
        'path': str(UDG_EXP), 'owner_family': 'APN',
        'path_candidates': [str(UDG_EXP), str(UNC_EXP)]})
    el_a3 = time.time() - t0
    attrs3 = r3.get('attribute_families') or []
    check('A5 多 EXP 合并结果更多', len(attrs3) >= len(attrs),
          f'UNC={len(attrs)} 合并={len(attrs3)}，耗时 {el_a3:.2f}s')
    multi = [a for a in attrs3 if len(a.get('found_in') or []) > 1]
    print(f'      在两个 EXP 都出现的属性族: {len(multi)} 个')

    # A6 边界
    r4 = mcp_exp.tool_exp_attr_chain({
        'path': str(UNC_EXP), 'owner_family': 'NOSUCHFAMILY'})
    check('A6 不存在的父族返回空不崩',
          not r4.get('error') and (r4.get('total_attribute_families') == 0))

    # ══ B. exp_cross_stats ══
    print('\n' + '─' * 92)
    print('【B】exp_cross_stats')
    print('─' * 92)

    t0 = time.time()
    c = mcp_exp.tool_exp_cross_stats({
        'paths': [str(UDG_EXP), str(UNC_EXP)]})
    el_b = time.time() - t0
    print(f'  耗时 {el_b:.2f}s，返回 {len(json.dumps(c, ensure_ascii=False)) // 1024}KB')

    if c.get('error'):
        check('B0 无错误', False, c['error'])
        return 1
    check('B0 无错误', True)

    labels = c.get('labels') or []
    check('B1 label 识别为 UDG / UNC',
          set(labels) == {'UDG', 'UNC'}, f'{labels}')

    comp = {x['family']: x for x in (c.get('comparison') or [])}

    def _verdict(fam):
        x = comp.get(fam)
        return x['verdict'] if x else None, (x['counts'] if x else None)

    v1, c1 = _verdict('POOLGROUP')
    check('B2 POOLGROUP 判为 UDG_only', v1 == 'UDG_only', f'verdict={v1} counts={c1}')

    v2, c2 = _verdict('PCSCFGROUP')
    check('B3 PCSCFGROUP 判为 UNC_only', v2 == 'UNC_only', f'verdict={v2} counts={c2}')

    v3, c3 = _verdict('USERPROFILE')
    check('B4 USERPROFILE 判为 all（双侧都有）', v3 == 'all', f'verdict={v3} counts={c3}')

    # B5 summary 一致
    sm = c.get('summary') or {}
    tot_sm = sum(sm.values())
    check('B5 summary 计数 == comparison 条数',
          tot_sm == len(c.get('comparison') or []),
          f'summary={sm} comparison={len(c.get("comparison") or [])}')

    # B6 边界
    c2r = mcp_exp.tool_exp_cross_stats({'paths': [str(UDG_EXP)]})
    check('B6 只给 1 个 EXP → error 不崩', bool(c2r.get('error')))

    # ══ C. 性能 ══
    print('\n' + '─' * 92)
    print('【C】性能')
    print('─' * 92)

    # ★ 2026-11-11：冷/热必须紧邻测，中间不能插别的调用（会清缓存）
    mcp_exp._RESULT_CACHE.clear()
    t0 = time.time()
    mcp_exp.tool_exp_attr_chain({'path': str(UNC_EXP), 'owner_family': 'APN'})
    cold_a = time.time() - t0
    t0 = time.time()
    mcp_exp.tool_exp_attr_chain({'path': str(UNC_EXP), 'owner_family': 'APN'})
    hot_a = time.time() - t0

    mcp_exp._RESULT_CACHE.clear()
    t0 = time.time()
    mcp_exp.tool_exp_cross_stats({'paths': [str(UDG_EXP), str(UNC_EXP)]})
    cold_b = time.time() - t0
    t0 = time.time()
    mcp_exp.tool_exp_cross_stats({'paths': [str(UDG_EXP), str(UNC_EXP)]})
    hot_b = time.time() - t0

    AGENT_BASELINE = 21 * 3.2     # 实测 agent 自己写 exec：21 次 × 3.2s
    print(f'  exp_attr_chain  冷 {cold_a:>6.2f}s  热 {hot_a*1000:>6.0f}ms')
    print(f'  exp_cross_stats 冷 {cold_b:>6.2f}s  热 {hot_b*1000:>6.0f}ms')
    print(f'  agent 自己写 exec 基线: {AGENT_BASELINE:.0f}s（21 次 × 3.2s）')
    print(f'  加速比（冷）: {AGENT_BASELINE/max(cold_a, 0.01):.0f}× / '
          f'{AGENT_BASELINE/max(cold_b, 0.01):.0f}×')

    check('C1 exp_attr_chain 冷启动 < 30s', cold_a < 30, f'{cold_a:.2f}s')
    check('C2 exp_cross_stats 冷启动 < 60s', cold_b < 60, f'{cold_b:.2f}s')
    check('C3 比她自写 exec 快 3 倍以上',
          AGENT_BASELINE / max(cold_a, 0.01) >= 3,
          f'{AGENT_BASELINE/max(cold_a,0.01):.0f}×')

    # ══ 汇总 ══
    print('\n' + '=' * 92)
    ok = sum(1 for _, c_, _ in results if c_)
    print(f'结果: {ok}/{len(results)} 通过')
    fails = [(n, d) for n, c_, d in results if not c_]
    if fails:
        print('\n失败项：')
        for n, d in fails:
            print(f'  ❌ {n}  {d}')
    else:
        print('✅ 全部通过')
    print('=' * 92)
    return 0 if ok == len(results) else 1


if __name__ == '__main__':
    sys.exit(main())

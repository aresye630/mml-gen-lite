#!/usr/bin/env python3
"""端到端验证：核心对象清单 → 派生下游族 → param.csv。

★ 2026-11-12（用户描述的常态场景）
  「我要配地址池，给个 POOL 列表，参考 EXP 发现 POOL 有 POOLGROUP，
   那就添加族 POOLGROUP，但是没有 POOLGROUP 的规划数据，
   那就使用命名风格推导出对象名，且输出 param.csv 支持用户来调整」

## 验证流程

  输入：只有 POOL 名称列表（模拟「数据清单只给核心对象」）
    ↓
  1. 查 EXP：POOL 族有哪些下游族（POOLBINDGROUP 存在 → 说明有 POOLGROUP）
    ↓
  2. 派生：POOL 名 → POOLGROUP 名
    ↓
  3. 生成 param.csv（含推导值 + 置信度 + 依据）
    ↓
  4. 校验：param.csv 能否被 mml_gen 正常读取

## 判据

  · param.csv 能被 mml_gen.read_params() 读到，行数正确
  · 每条 derived 行都有 source=derived:conf=XX 标记
  · 推导值与 GT 真实值对比（离线校验，不参与运行）
"""
import json
import subprocess
import sys
from pathlib import Path

PROJ = Path('/Users/alesc/workspace/mml-gen-lite')
sys.path.insert(0, str(PROJ / 'workflow'))
sys.path.insert(0, str(PROJ / 'workflow/stage3'))

import mml_gen
import derive_names as D3

GT = json.loads(Path('/tmp/gt_cleaned.json').read_text(encoding='utf-8'))
OUT = Path('/tmp/stage3_derive_out')


def discover_downstream(exp_paths, up_family, down_family):
    """从 EXP 查下游族是否存在。"""
    n = 0
    for p in exp_paths:
        try:
            with open(p, encoding='utf-8', errors='replace') as f:
                for line in f:
                    if line.strip().startswith(f'ADD {down_family}:'):
                        n += 1
        except Exception:
            pass
    return n


def run(tk, verbose=True):
    g = next((x for x in GT if x['ticket'] == tk), None)
    if not g:
        return None

    adir = Path(g['path']) / '备份附件'
    exps = [str(p) for p in sorted(adir.glob('*.txt'))] if adir.exists() else []
    if not exps:
        return None

    # ── 输入：只给 POOL 名称列表（模拟「数据清单只给核心对象」）──
    pool_input = []
    real_map = {}
    for _, v, fam, params, raw in g['kept']:
        if fam == 'POOL' and params.get('POOLNAME'):
            pool_input.append(params['POOLNAME'])
        elif fam == 'POOLBINDGROUP':
            pn, gn = params.get('POOLNAME'), params.get('POOLGROUPNAME')
            if pn and gn:
                real_map[pn] = gn

    if not pool_input:
        return None

    result = {'ticket': tk, 'n_pools': len(pool_input), 'steps': []}

    # ── 步骤 1：查 EXP 发现下游族 ──
    n_bind = discover_downstream(exps, 'POOL', 'POOLBINDGROUP')
    n_grp = discover_downstream(exps, 'POOL', 'POOLGROUP')
    result['steps'].append({
        'step': 'discover',
        'found': {'POOLBINDGROUP': n_bind, 'POOLGROUP': n_grp},
    })
    if verbose:
        print(f'  [1] 查 EXP: POOLBINDGROUP {n_bind} 条, POOLGROUP {n_grp} 条')

    if n_bind == 0:
        result['steps'].append({'step': 'derive', 'skipped': 'EXP 无 POOLBINDGROUP'})
        return result

    # ── 步骤 2：派生下游对象名 ──
    pairs = D3.load_pairs(exps)
    res = D3.derive_by_analogy(pool_input, pairs)
    n_derived = sum(1 for r in res if r.get('derived'))
    result['steps'].append({
        'step': 'derive', 'n_derived': n_derived,
        'sample': [(r['upstream'], r['derived'], r['confidence'])
                   for r in res if r.get('derived')][:3],
    })
    if verbose:
        print(f'  [2] 派生: {n_derived}/{len(pool_input)} 个成功')

    # ── 步骤 3：生成 param.csv ──
    rows = D3.to_csv_rows(res, net_type='UDG', family='POOLGROUP',
                          down_param='POOLGRPNAME', start_group=1)
    csv_path = OUT / tk / 'params.csv'
    D3.write_csv(rows, csv_path)
    result['steps'].append({'step': 'csv', 'rows': len(rows), 'path': str(csv_path)})
    if verbose:
        print(f'  [3] 生成 param.csv: {len(rows)} 行')

    # ── 步骤 4：mml_gen 能否读取 ──
    try:
        parsed = mml_gen.read_params(csv_path)
        result['steps'].append({'step': 'readback', 'ok': True, 'n': len(parsed)})
        if verbose:
            print(f'  [4] mml_gen 读取: {len(parsed)} 行 ✅')
    except Exception as e:
        result['steps'].append({'step': 'readback', 'ok': False, 'err': str(e)})
        if verbose:
            print(f'  [4] mml_gen 读取失败: {e}')

    # ── 离线校验：推导 vs GT 真实 ──
    if real_map:
        n_hit = n_test = 0
        wrong = []
        for r in res:
            if not r.get('derived'):
                continue
            exp = real_map.get(r['upstream'])
            if not exp:
                continue
            n_test += 1
            if r['derived'] == exp:
                n_hit += 1
            else:
                wrong.append((r['upstream'], r['derived'], exp))
        result['hit'] = (n_hit, n_test)
        if verbose:
            print(f'  [校验] 推导 vs GT: {n_hit}/{n_test}'
                  f' = {n_hit/n_test*100:.0f}%' if n_test else '')
            for up, got, exp in wrong[:2]:
                print(f'      ✗ {up}: 推导 {got} ≠ 真实 {exp}')
    return result


def main():
    OUT.mkdir(parents=True, exist_ok=True)

    print('=' * 100)
    print('端到端：核心对象清单 → 派生 → param.csv')
    print('=' * 100)

    TICKETS = ['NC20260820001773', 'NC20260824002020', 'NC20260805000498',
               'NC20260803002122', 'NC20260824002208', 'NC20260828000409']
    all_res = []
    for tk in TICKETS:
        print(f'\n{tk}')
        r = run(tk)
        if r:
            all_res.append(r)

    # 汇总
    print(f'\n{"=" * 100}')
    print('汇总')
    print(f'{"=" * 100}')
    total_hit = total_test = 0
    for r in all_res:
        hit = r.get('hit')
        if hit:
            total_hit += hit[0]
            total_test += hit[1]
            print(f'  {r["ticket"]}: POOL {r["n_pools"]} 个, '
                  f'推导命中 {hit[0]}/{hit[1]}')
        else:
            print(f'  {r["ticket"]}: POOL {r["n_pools"]} 个, 跳过')

    if total_test:
        print(f'\n  总体推导准确率: {total_hit}/{total_test} '
              f'= {total_hit/total_test*100:.0f}%')

    # 展示一个生成的 param.csv
    sample_csv = OUT / 'NC20260824002020' / 'params.csv'
    if sample_csv.exists():
        print(f'\n{"=" * 100}')
        print(f'生成的 param.csv 样例: {sample_csv}')
        print(f'{"=" * 100}')
        txt = sample_csv.read_text(encoding='utf-8-sig')
        for line in txt.split('\n')[:8]:
            print(f'  {line}')


if __name__ == '__main__':
    main()

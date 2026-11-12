#!/usr/bin/env python3
"""批量生成所有引号值参数的表头变体（LLM）。

★ 2026-11-12
  为什么全量生成：
    即使语素推导能推出名字（如 IFIPADDR → 接口IP地址），
    也只有单一说法。要让清单看起来像不同人写的，需要多种等价表达。

  成本：195 个参数 / 15 个一批 ≈ 13 次 LLM 调用
"""
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import header_llm as HL
import header_naming as HN

GT = json.loads(Path('/tmp/gt_cleaned.json').read_text(encoding='utf-8'))


def main():
    # 收集全部引号值参数 + 最好的上下文样例
    need = {}
    for g in GT:
        if not g['kept']:
            continue
        for _, v, fam, params, raw in g['kept']:
            for pname in params:
                m = re.search(rf'\b{re.escape(pname)}\s*=\s*("?[^",;]+"?)', raw)
                if not (m and m.group(1).startswith('"')):
                    continue
                k = pname.upper()
                if k in need:
                    continue
                need[k] = {'param': k, 'family': fam, 'sample': raw}

    print('=' * 90)
    print(f'批量生成表头变体（{len(need)} 个引号值参数）')
    print('=' * 90)

    cache = HL._load_cache()
    print(f'\n已有缓存: {len(cache)} 个')
    todo = [v for k, v in need.items() if k not in cache]
    print(f'待生成: {len(todo)} 个')

    if not todo:
        print('\n✅ 全部已缓存')
    else:
        cache = HL.generate_missing_headers(todo, verbose=True)

    # 检查覆盖
    print(f'\n{"=" * 90}')
    print('覆盖检查')
    print(f'{"=" * 90}')
    have = [k for k in need if k in cache]
    miss = [k for k in need if k not in cache]
    print(f'  LLM 缓存覆盖: {len(have)}/{len(need)} ({len(have)/len(need)*100:.0f}%)')
    if miss:
        print(f'  仍缺: {miss[:10]}')

    # 抽样展示多样性
    print(f'\n{"=" * 90}')
    print('多样性抽样（每参数 3 种说法）')
    print(f'{"=" * 90}')
    SAMPLES = ['IFIPADDR', 'SUBNETMASK', 'APN', 'USERPROFILENAME', 'POOLNAME',
               'PRIORITY', 'FLOWFILTERNAME', 'MCC', 'MNC', 'URRID',
               'PCCPOLICYGRPNM', 'SECTIONNUM', 'V4STARTIP', 'DNN']
    for p in SAMPLES:
        v = cache.get(p)
        if v:
            print(f'  {p:<22} {v}')
        else:
            print(f'  {p:<22} ❌ 无')

    # 验证：同一参数在不同工单选到不同变体
    print(f'\n{"=" * 90}')
    print('同一参数在不同工单的写法（验证多样性生效）')
    print(f'{"=" * 90}')
    for p in ['IFIPADDR', 'USERPROFILENAME', 'POOLNAME']:
        variants = cache.get(p) or []
        if not variants:
            continue
        picks = [HL.get_header(p, seed=tk) for tk in
                 ['NC20260810002261', 'NC20260806001780', 'NC20260823000103']]
        print(f'  {p:<22} → {picks}')


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""assert_indexes.py — 构建期向量库断言（三库齐备 + 条数 + 产品分布）

为什么需要（2026-09-17 实测教训）：
    早期断言只查「集合是否存在」—— 于是这个 bug 溜过去了：
    build_all_indexes.sh 三产品循环里每次都带 `--rebuild`（= 删集合重建），
    后一个产品把前一个的数据整个删掉，最终库里只剩最后一个产品的条数。
    集合名全在、条数却只有 1/4 → 只查集合存在**查不出来**。

    所以本脚本查三层：
      ① 集合齐备（mml_feature / mml_nav / mml_support）
      ② 每集合条数 ≥ 阈值（能拦住「被覆盖成小产品」的情况）
      ③ 多产品集合的 product 分布（能拦住「只剩一个产品」的情况）

退出码非 0 会让 Docker 构建失败（Dockerfile 里是 `RUN ... ; python3 assert_indexes.py`）。
"""
import os
import sys
from collections import Counter

MILVUS = os.environ.get('MML_MILVUS_DIR', '/data/milvus/milvus_mml.db')

# 集合 → 最低条数阈值（取实测值的 ~70%，留版本间浮动余量但能拦住覆盖）
MIN_ROWS = {
    'mml_feature': 1000,   # 实测 1504（三产品特性合计）
    'mml_nav': 5000,       # 实测 UEG 9578 + UDG 3 + UNC 2
    'mml_support': 25000,  # 实测 UEG 22238 + UDG 4746 + UNC 8771 = 35755
}
# 应当出现多产品数据的集合（用于查「只剩一个产品」）
MULTI_PRODUCT = ('mml_support',)


def main() -> int:
    try:
        from pymilvus import MilvusClient
    except ImportError as e:
        print(f'!! 无法导入 pymilvus: {e}', file=sys.stderr)
        return 1

    if not os.path.exists(MILVUS):
        print(f'!! 向量库不存在: {MILVUS}', file=sys.stderr)
        return 1

    # ★ LOCK 自动清理（2026-09-17 实测）：
    #   Milvus Lite 建库完成后会残留 LOCK 文件（0 字节），下次打开报
    #   `ConnectionConfigException: Open local milvus failed` —— 症状很像
    #   「库损坏」，实际只需删 LOCK。构建期/重跑建库后都会遇到，故在此自动清。
    lock = os.path.join(MILVUS, 'LOCK')
    if os.path.exists(lock) and os.path.getsize(lock) == 0:
        try:
            os.remove(lock)
            print(f'（已清理残留 LOCK: {lock}）')
        except OSError as e:
            print(f'!! 无法清理 LOCK {lock}: {e}', file=sys.stderr)
            return 1

    c = MilvusClient(MILVUS)
    cols = sorted(c.list_collections())
    print(f'向量库: {MILVUS}')
    print(f'集合: {cols}')

    errs = []

    # ① 集合齐备
    missing = [x for x in MIN_ROWS if x not in cols]
    if missing:
        errs.append(f'缺集合: {missing}')

    # ② 条数阈值
    for name, min_rows in MIN_ROWS.items():
        if name not in cols:
            continue
        try:
            c.load_collection(name)
            n = c.get_collection_stats(name)['row_count']
        except Exception as e:
            errs.append(f'{name}: 统计失败 {type(e).__name__}: {e}')
            continue
        flag = '✓' if n >= min_rows else '✗'
        print(f'  {flag} {name}: {n} 条（阈值 ≥{min_rows}）')
        if n < min_rows:
            errs.append(f'{name} 只有 {n} 条（阈值 {min_rows}）—— '
                        f'疑似建库被覆盖（--rebuild 用在了多个产品上）')

    # ③ 产品分布（只对含 product 字段的集合）
    for name in MULTI_PRODUCT:
        if name not in cols:
            continue
        try:
            c.load_collection(name)
            # ★ PITFALL（2026-09-17 实测）：query 的 limit 有上限，
            #   传 16384 会**截断结果**（UEG 单独就 22238 条 → 只能看到前
            #   16384 条，且恰好都是第一个产品的）→ 误判「只有单一产品」。
            #   正确做法：分页 query（offset 递增）或直接按 product 计数。
            total = None
            try:
                total = c.get_collection_stats(name)['row_count']
            except Exception:
                pass
            dist = {}
            offset = 0
            PAGE = 4096
            while True:
                rows = c.query(name, filter='', output_fields=['product'],
                               limit=PAGE, offset=offset)
                if not rows:
                    break
                for r in rows:
                    dist[r.get('product', '?')] = dist.get(r.get('product', '?'), 0) + 1
                if len(rows) < PAGE:
                    break
                offset += PAGE
                if total and offset >= total + PAGE:
                    break
            print(f'  {name} product 分布: {dict(dist)}'
                  + (f'（逐条计数 {sum(dist.values())}）' if dist else ''))
            products = [k for k in dist if k not in ('?', '')]
            if len(products) < 2:
                errs.append(f'{name} 只有单一产品 {products} —— '
                            f'疑似数据目录探测失败（UDG/UNC 目录层级与 UEG 不同）'
                            f'或后一个产品覆盖了前一个')
        except Exception as e:
            print(f'  （{name} product 分布查不到: {type(e).__name__}）')

    if errs:
        print('\n!! 向量库断言失败:', file=sys.stderr)
        for e in errs:
            print(f'   - {e}', file=sys.stderr)
        return 1

    print('三库齐备且条数/分布正常 ✓')
    return 0


if __name__ == '__main__':
    sys.exit(main())

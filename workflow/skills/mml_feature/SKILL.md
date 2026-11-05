---
name: mml_feature
description: >-
  特性文档知识库（UEG/UDG/UNC）。当需要了解「某个业务功能怎么配、依赖哪些对象、
  适用哪些网元」时查这个库。返回特性名称、适用网元、操作场景、配置原因、关联对象。
  不含 MML 命令示例——命令示例在 mml_support 的命令文档里。
version: 2.0.0
author: Hermes Agent
license: MIT
---

# mml_feature — 特性文档知识库

## 里面有什么

收录 UEG / UDG / UNC 三个产品的特性配置指导文档。

每篇特性包含：
- 特性名称
- 适用网元（如 SGW-U / PGW-U / UPF / SMF）
- 操作场景（做什么、为什么）
- 关联对象（配置时需要哪些对象）
- 高危提示、注意事项

**不含 MML 命令示例**。要命令示例去 mml_support 的命令文档（`使用实例` 段）。

## 怎么查

```bash
# 语义检索：描述你要做的事
python3 scripts/mml_feature_query.py semantic "内容计费 三四层过滤" --top_k 5 --product UDG

# 特性名检索：已知特性名时
python3 scripts/mml_feature_query.py feature_name "配置内容计费" --product UDG

# 批量查询（多次语义检索，复用模型实例，更快）
python3 scripts/hybrid_search.py --top_k 3 --product UDG "查询1" "查询2"
```

**`--product` 默认 UEG**，查 UDG/UNC 必须显式传 `--product UDG` 或 `--product UNC`。

## 数据规模

当前索引 3748 篇：UEG 2520 / UDG 514 / UNC 714。
查不到不等于没有——可能在别的产品库，或不在此知识库（用 `--product=` 全库重试）。

## 其他检索路径

- 命令 → 官方功能分类反查（10,587 条命令树）：`references/command-tree-reverse-lookup.md`
- 嵌入检索的盲区（哪些问法查不准）：`references/embedding-blind-spot.md`

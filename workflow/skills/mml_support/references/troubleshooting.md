# 故障排查

<!-- 外移来源：mml_support/SKILL.md :: ## 已知故障与修复（20260920） -->
### 已知故障与修复

#### Loky segfault（大数据量导入时）
- **症状**：通过 `mml_support_db.py --rebuild` 导入 22,238 条 UEG 数据时，进程在第 ~50 批（10,000 条）后 `Segmentation fault: 11`，exit code 139
- **原因**：`sentence-transformers` 内部使用 `joblib.externals.loky` 多进程池。多次 `encode()` 调用后 loky 信号量累积，子进程 fork 时冲突
- **修复**：
  1. 导入脚本中在 `from get_embeddings import Emb` 前设置 `TOKENIZERS_PARALLELISM=*** + `OMP_NUM_THREADS=1`
  2. `get_embeddings.py` 复制 mml_feature 的修复版本（含 `cleanup()` 方法 + `atexit` + `show_progress_bar=***）
  3. 导入循环中每 20 批调用 `emb.cleanup()` 释放 loky 状态
- **验证**：修复后 exit code 0，112 批全部完成（22,238 条）

#### command_function 字段超长
- UNC 产品有 `add_cdrstor.json` 的 `command_function` 达 11,097 字符
- 原 schema `max_length=8192` 会报错
- 已在 schema 中扩至 16384。添加新产品时需先检查最大字段长度。

#### pymilvus 3.0 hybrid_search filter API 差异
- **症状**：`--product` filter 不生效，返回所有产品的结果
- **根因**：pymilvus 3.0 的 `hybrid_search()` 方法**没有 `filter` 参数**（静默忽略）。filter 必须设到每个 `AnnSearchRequest(filter=...)` 级别
- **正确写法**：
  ```python
  req = AnnSearchRequest(..., filter=f'product == "{product}"')
  ```
- **注意**：`client.query()` 的 filter 正常，不受影响

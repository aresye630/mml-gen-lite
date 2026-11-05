# 故障排查

<!-- 外移来源：mml_feature/SKILL.md :: ## 已知故障与修复（20260920） -->
### 已知故障与修复

#### Loky 残留导致 segfault（大数据量导入）

- **症状**：连续导入大量 feature 数据时进程 `Segmentation fault: 11`，exit code 139
- **原因**：`sentence-transformers` 内部使用 `joblib.externals.loky` 多进程池，多次 `encode()` 后 loky 信号量累积导致 fork 冲突
- **修复**已在 `get_embeddings.py` 和 `import_feature_data.py` 中落实：
  1. import 前设 `TOKENIZERS_PARALLELISM=*** + `OMP_NUM_THREADS=1`
  2. `model.encode(show_progress_bar=False)` 避免 tqdm 交互
  3. `cleanup()` 方法：`gc.collect()` → `loky.get_reusable_executor().shutdown(wait=True)`
  4. 配合 `atexit` + `__del__` 双保险

#### 知识层版本换代后向量库 file_path 断链（2026-09-08 实测修复）

- **症状**：`mml_feature_query.py semantic "..."` 检索正常返回命中，但打印结果时崩
  `FileNotFoundError: .../output_ueg_feature_v2/...md` —— 检索本身通了，读文档文件失败。
- **根因**：zhijian 知识层 9/4 换代（`output_ueg_feature_v2` → 改名 `output_ueg_feature_v2_bak_991_20260904` +
  新版 `output_ueg_feature_v3`，v3 树 2343 篇 md），而 milvus_mml.db（7/8 建）里每条记录的
  `file_path` 仍写死指 v2 → 旧路径消失即 FNF。
- **修复（库内重映射,零重导 embedding）**：
  1. 备份：`cp -r milvus_mml.db milvus_mml.db.bak_<ts>`（库是**目录**，366M，勿当文件 rm）
  2. `load_collection` 后**单次** `query(filter='product=="UEG"', output_fields=全字段, limit=5000)` 全量拉取
     —— ⚠ 禁止 offset 分页 + upsert 交错（会跳行漏处理，见 milvus-lite-workflow pitfall）
  3. 每条 file_path 含 `/output_ueg_feature_v2/`：相对路径在 v3 存在 → 指 v3；仅 v2_bak 存在 → 指 v2_bak
  4. `upsert` 前必须剔除 function output 字段（`*_sparse`，BM25 自动算，直接插报
     `InsertUnexpectedFunctionOutputField`）；dense 字段原样回写（非 function，可插）
  5. 回读校验：`query` 再查 `file_path like "%output_ueg_feature_v2%"` 残留 = 0
- **结果**：991 条 UEG 全部可解析（实测 v3≈309 + bak≈182 + 本就通 500）。备份保留 `.bak_20260908`。
- **⚠ 长期正解 = 对 v3 全量重导**（换代 9/4 时漏了重建向量库，属维护欠账；本修复只保证旧库可用）。
  **⚠⚠ 但不能用 `import_feature_data.py`** —— 见下条，那样会静默导入 0 条。
- **判别口径**：nav/mml 两库路径无 v2/v3 后缀（`output_ueg_nav/output_ueg_nav_v2`、`output_ueg_mml/output_ueg_mml`
  仍在原处）不受影响——只有 feature 库换代时断链。怀疑断链先 `ls` 库内 file_path 前缀 vs 实际目录。

#### v3 新格式是 markdown-only，旧导入脚本对它会静默导入 0 条（2026-09-12 实测）

- **症状**：`import_feature_data.py --rebuild --data_dir output_ueg_feature_v3` 跑完无报错，
  但集合里 **0 条**新记录，看起来像"跑过了"。
- **根因**：v3 树 **只有 `.md`、没有任何 `.json`**（实测 `find -name '*.json' | wc -l` = 0），而该脚本是
  `rglob('*.json')` + 从 JSON 取 `feature_name`/`feature_description`/`full_nav` → 循环体一次都不执行。
  v2（991 篇）是 json+md 配对，v3（2343 篇）改成纯 md，元数据（标题/操作场景）进了正文。
- **正确做法**：用 `scripts/import_feature_v3.py`（本会话新增），它按 v3 实际结构解析：
  - `feature_name` ← md 首个 `# 标题`
  - `feature_description` ← `操作场景` 段（**任意层级标题**，段落边界取"同级或更高级标题"，
    否则会把 `#### 对系统的影响` 等后续章节并进描述 —— 这是解析质量的关键坑）
  - `full_nav` ← 相对树根的**英文目录路径**（如 `be/installation/initial_config`）。
    ⚠ v3 不保留中文导航路径：中文 full_nav 只在 v2_bak 的 json 里，且 v2 与 v3 仅 664/991 能对上，
    `output_ueg_nav`（两级目录列表）、`ueg_command_tree.json`（命令树）都不是特性中文路径来源。
    用户已拍板：**v3 是重新做的全量数据，不继承 v2 路径，直接用 v3 自身字段**。
- **通用规律**：导入脚本的"文件扩展名 + 元数据位置"属于数据契约；上游换代后**先验证再跑**
  （`Counter(p.suffix for p in d.rglob('*'))` 看扩展名分布），别默认"重跑一遍就行"。
  详见 milvus-lite-workflow §3.5 与 `scripts/import_feature_v3.py`（纯 md 树版）。

#### pymilvus 3.0 hybrid_search filter API 差异

- **症状**：`--product` filter 不生效，返回了所有产品的搜索结果
- **根因**：pymilvus 3.0 的 `hybrid_search()` 方法**没有 `filter` 参数**（不会报错，只是静默忽略）。filter 必须设到每个 `AnnSearchRequest(filter=...)`
- **正确写法**：
  ```python
  req = AnnSearchRequest(data=[vec], anns_field="feature_name_dense",
      param={"metric_type": "COSINE", "params": {"ef": 128}},
      limit=top_k * 2, filter=f'product == "{product}"')
  ```
- **注意**：`client.query()` 的 filter 参数正常
- **验证**：查询结果中所有记录的 `product` 字段应一致

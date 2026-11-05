# 知识库导入说明

<!-- 外移来源：mml_feature/SKILL.md :: ## 数据导入（多产品支持）（20260920） -->
### 数据导入（多产品支持）

当前支持三个产品：UEG、UDG、UNC。**先判断数据格式，再选脚本**（三种格式，选错会静默导入 0 条）：

| 数据格式 | 脚本 | 说明 |
|---|---|---|
| **新格式：md + YAML frontmatter** | `import_feature_newfmt.py` | **当前生产口径**，见下 |
| json + md 配对（老格式） | `import_feature_data.py` | `rglob('*.json')` 读元数据 |
| 纯 md、无 frontmatter（v3 树） | `import_feature_v3.py` | 从 md 正文解析 |

```bash
# 新格式（当前口径，3748 篇三产品）—— --data_root 下须含 UEG/ UDG/ UNC/ 子目录
python3.14 scripts/import_feature_newfmt.py --data_root ~/Downloads/111 --rebuild
# 老格式（json+md）
python3.14 scripts/import_feature_data.py --product UEG --data_dir <ueg_dir> --rebuild
# v3 新格式（纯 md 树）—— 先离线验解析完整性，再入库
python3.14 scripts/import_feature_v3.py --product UEG \
    --data_dir ~/workspace/zhijian/output_ueg_feature/output_ueg_feature_v3 --rebuild
```

`import_feature_v3.py` 的 `parse_md()`、`import_feature_newfmt.py` 的 `parse_md()` 均可单独 import，
**入库前先跑全量解析校验**（`bad`/`empty_desc`/`empty_nav` 必须为 0），避免解析缺口写进库。
跑法见 milvus-lite-workflow §3.5。

#### 新格式（frontmatter）解析要点 —— 2026-09-12 起的生产口径

新格式每篇带 YAML frontmatter，字段齐全，**不需要从正文猜**：

| 字段 | 用途 | 备注 |
|---|---|---|
| `name` | feature_name | |
| `ne_type` | product | 与目录名双保险 |
| `description` | feature_description | **现成可用，比正文解析干净** |
| `doc_source` | 中文导航全路径 | list，可能嵌套 list[list] = 多场景 |
| `type` / `risk_level` / `metadata` | 附加 | |

- frontmatter 用 `re.match(r'^---\s*\n(.*?)\n---\s*\n', s, re.S)` 提取 —— **用 match 不用 search**，
  避免匹配到正文里的分隔线。
- `full_nav` 取\"最具体路径去掉末段\"：末段通常等于特性名、无区分度，**上层导航链才有用**。
- **同标题多副本 = 真实场景副本，勿去重**：实测某特性 36 份 = 3 种描述 × 6 种正文，
  差异是部署场景（UEG-L/UPF 侧、主备热备/负荷分担/冷备）。按 `name+doc_source` 去重只减
  79/3748 条（doc_source 大多不同）→ **全量入库，由检索侧按 doc_source 展示区分**。
  （用户口径原话：\"多副本的原因是有细节差异\"。）
- **规模基线（新格式）**：3748 篇 = UEG 2520 / UDG 514 / UNC 714。
  比 v3 树的 2343（仅 UEG）更全，且三产品齐全 —— 新格式出现后优先用它。

#### ⚠ 重建 embedding 前必查 tokenizer（否则两套向量空间）

`bge-small-zh-v1.5` 模型目录的 tokenizer 资产**不自洽**（`tokenizer.json` 的
`normalizer.lowercase=false` + `tokenizer_config.json` 的 `do_lower_case=false`）：
HF 标准加载方式会把 "QoS" 等大写英文吐成 `[UNK]`，与 sentence-transformers 结果**余弦仅 0.867**。
复核基准：`tokenize("配置QoS覆盖")` 应为 `[101,6981,5390,159,8470,6208,4667,102]`（**无 100**）。
两处 lowercase 都要置 `true`，只改一处无效。详见 milvus-lite-workflow §4。

#### 字段长度陷阱

不同产品的 `feature_description` 长度差异大（UEG 最长 ~6K，UNC 最长 10,517）。schema 中已设 16384。添加新产品前先检查：

```bash
python3.14 -c "
import json, os
max_len = 0
for r,d,f in os.walk('<feature_dir>'):
    for fn in f:
        if fn.endswith('.json'):
            with open(os.path.join(r,fn)) as fp:
                max_len = max(max_len, len(json.load(fp).get('feature_description','')))
print(f'Max feature_description length: {max_len}')
"
```

#### 许可列说明

- 已修复陷阱（Loky segfault / 向量库断链 / v3 静默导入 0 条 / pymilvus API 差异）：
  遇到报错时读 `references/troubleshooting.md`

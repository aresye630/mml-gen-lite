# Embedding 盲点参考 — 语义检索不命中的已知模式

## 问题定义

某些 MML 命令不是独立特性文档，而是嵌入在其他特性文档的数据表中。这类文档的 `feature_name` / `feature_description` 不包含用户搜索的关键词，导致语义检索不命中。这是 **embedding 盲点（embedding blind spot）**。

## 已确认的盲点

| 命令 | 实际所在特性文档 | feature_name | feature_description | 用户常用搜索词 |
|------|----------------|-------------|-------------------|--------------|
| ADD SNSSAI | 激活业务体验保障 | 激活业务体验保障 | "适用于PGW-U、UPF" | 切片、SNSSAI、5G切片、eMBB |
| ADD SNSSAIUPINTF | 激活业务体验保障 | 同上 | 同上 | 切片绑定、接口绑定、SNSSAIUPINTF |
| ADD SNSSAIBWMUSRG | 激活业务体验保障 | 同上 | 同上 | 切片带宽、用户组、SNSSAI |

**验证记录**（2026-07-16）：5 条扩展查询（原句保留/术语展开/相关功能/对象提取/能力边界）全部没有命中"激活业务体验保障"，Top-3 命中的是"激活支持4G到5G多切片时的重选"（RRF 分 0.0656）和"激活支持网络切片模式下发"（RRF 分 0.0648）。

## 通用模式判断

以下特征提示某个命令可能处于盲点中：

1. 该命令在 **mml_support** 中有独立文档（含完整参数说明），但不在 **mml_feature** 中独立出现
2. grep 搜索该命令名能定位到某个 feature MD 的数据表，但该 MD 的 feature_name 不含命令的功能关键词
3. 命令属于某个**大的功能特性**的子集（如 ADD SNSSAI 是"激活业务体验保障"特性的一部分，不是独立特性）

## 兜底工作流

当语义检索不命中时，按以下流程逐步降级：

### 一级降级：多语句搜索
先用 3-5 个不同角度的语句重试（原句、术语展开、相关功能、对象提取、能力边界），可能有部分语句命中。

### 二级降级：命令名 grep
```bash
grep -rl "ADD SNSSAI" /opt/expgv/kb/output_ueg_feature/output_ueg_feature_v3/
```
找到包含该命令的 MD 文件，从中提取完整命令链和操作步骤。

### 三级降级：导航树兜底（command-context-resolver）
当语义检索和 grep 都找到了但结果零散，使用 `command-context-resolver` skill：
1. **Feature Doc 回溯** — 从 feature MD 数据表中提取完整命令链
2. **Exp Config 追踪** — 从 exp.txt 中追踪实际参数引用链
3. **Nav Tree 扩展** — 在导航树中找兄弟节点补充同类命令

### 四级降级：精确特性名直查
如果 grep 已经定位到目标 MD 文件，可以直接通过精确特性名检索获取完整内容：
```bash
mml_feature_query.py feature_name "激活业务体验保障"
```

## 预防措施

- 新导入特性文档时，检查 feature_description 是否过于简短（如仅"适用于PGW-U、UPF"），这种情况大概率会有 blind spot
- 对于已知盲点，考虑在 command-context-resolver 或 mml-assistant 的检索流程中加入**显式映射表**（命令→特性文档路径）

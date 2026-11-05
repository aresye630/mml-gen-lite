---
name: mml_support
description: >-
  MML 命令文档知识库（UEG/UDG/UNC）。当需要查「某条命令怎么用、有哪些参数、
  参数取值范围、有没有使用实例」时查这个库。也支持按功能语义反查命令。
version: 2.0.0
author: Hermes Agent
license: MIT
---

# mml_support — MML 命令文档知识库

## 里面有什么

35,755 条 MML 指令文档（UEG 22,238 / UDG 4,746 / UNC 8,771）。

每条命令包含：
- 命令功能说明
- 参数表（参数名、类型、取值范围/枚举、必选性、默认值）
- 使用实例（完整 MML 命令行示例）
- 导航目录

## 怎么查

```bash
# 命令名检索：已知命令名
python3 scripts/mml_support_query.py command_name "ADD URR" --product UDG

# 语义检索：不知道命令名，描述功能
python3 scripts/mml_support_query.py semantic "计费规则 在线离线" --top_k 5 --product UDG

# 全库检索（跨产品，确认命令是否存在）
python3 scripts/mml_support_query.py command_name "ADD URR" --product=
```

**`--product` 默认 UEG**，查 UDG/UNC 必须显式传；`--product=`（空）表示全库。

`top_k` 仅语义检索生效，默认 5。

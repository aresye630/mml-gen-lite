---
id: ''
name: 核对软件版本
ne_type: UEG
type: feature
description: 定期核对系统软件的版本情况，确保系统运行在正确的软件版本上。
tags: []
risk_level: ''
doc_source: ["日常维护","UEG 例行维护（风筝S，虚机容器）","例行维护操作指导","月度维护","核对软件版本"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
定期核对系统软件的版本情况，确保系统运行在正确的软件版本上。

## 必备事项
前提条件

已经登录OM Portal，或者登录MAE并进入Access子系统。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties: {}
  examples: {}
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 通过执行****DSP ACSVERSION****命令查看系统当前的基础包、补丁包版本信息。

### 2 如果基础版本与补丁版本和预期版本或规划版本不相符，请进行基础版本或补丁版本的升级。


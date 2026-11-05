---
id: ''
name: 配置5G全局数据
ne_type: UEG
type: feature
description: 该操作指导工程师在开局阶段，新建UDM网元时，完成5G全局数据的配置。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝L","UEG UDM用户管理（风筝L）","用户数据配置（5G SA网络）","5G用户数据配置","配置5G全局数据"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
该操作指导工程师在开局阶段，新建UDM网元时，完成5G全局数据的配置。

## 必备事项
前提条件

* 已经完成UDM的CSP OM Portal侧的硬件数据和基础数据的配置。
* 已经完成5G的用户数据规划。
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

### 1 登录PGW Web LMT MML命令界面。

### 2 执行**ADD SYSHLRSN**命令增加系统HLR。

### 3 执行**ADD VHLRSN**命令增加虚拟HLR。

### 4 登录“UDM业务管理”窗口。

### 5 执行**ADD HLRSN**命令增加HLR序列号。


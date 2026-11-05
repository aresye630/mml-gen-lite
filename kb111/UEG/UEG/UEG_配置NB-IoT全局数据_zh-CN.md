---
id: ''
name: 配置NB-IoT全局数据
ne_type: UEG
type: feature
description: 该操作指导工程师在开局阶段，新建UDM作为SAE-HSS网元时，完成NB-IoT全局数据的配置。  NB-IoT是一种新型窄带无线技术，用以满足物联网需求。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝L","UEG UDM用户管理（风筝L）","用户数据配置（EPS网络）","NB-IoT用户数据配置","配置NB-IoT全局数据"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
该操作指导工程师在开局阶段，新建UDM作为SAE-HSS网元时，完成NB-IoT全局数据的配置。NB-IoT是一种新型窄带无线技术，用以满足物联网需求。

## 必备事项
前提条件

* 已经完成UDM的OMU侧的硬件数据和基础数据的配置。
* 已经完成NB-IoT的用户数据规划。
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

### 1 登录系统管理命令界面。

### 2 执行**ADD SYSHLRSN**命令增加系统HLR。

### 3 执行**ADD VHLRSN**命令增加虚拟HLR。

### 每个SYSHLRSN至少指定一个虚拟HLR。

### 4 登录“UDM业务管理”窗口。

### 5 执行**ADD HLRSN**命令增加HLR序列号。


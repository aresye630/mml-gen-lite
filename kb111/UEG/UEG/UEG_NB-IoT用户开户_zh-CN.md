---
id: ''
name: NB-IoT用户开户
ne_type: UEG
type: feature
description: 该操作指导工程师在开局阶段，新建UDM作为SAE-HSS网元时，完成NB-IoT开户数据的配置。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝L","UEG UDM用户管理（风筝L）","用户数据配置（EPS网络）","NB-IoT用户数据配置","NB-IoT用户开户"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
该操作指导工程师在开局阶段，新建UDM作为SAE-HSS网元时，完成NB-IoT开户数据的配置。

## 必备事项
前提条件

* 已经完成UDM的OMU侧的硬件数据和基础数据的配置。
* 已经完成NB-IoT的用户数据规划。
* 已经完成NB-IoT的全局数据、模板数据、鉴权数据的配置。
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

### 1 登录“UDM业务管理”窗口。

### 2 执行**ADD SUB**命令进行开户。

### 3 执行**MOD OPTGPRS**命令，为用户签约Non-IP PDN类型的EPS APN。

### 4 执行**MOD ARD**命令，设置UDM不限制用户接入NB-IoT功能。


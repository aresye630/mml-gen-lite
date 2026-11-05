---
id: ''
name: 配置5G鉴权数据
ne_type: UEG
type: feature
description: 该操作指导工程师在开局阶段，新建UDM网元时，完成UDM鉴权数据的配置。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝L","UEG UDM用户管理（风筝L）","用户数据配置（5G SA网络）","5G用户数据配置","配置5G鉴权数据"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
该操作指导工程师在开局阶段，新建UDM网元时，完成UDM鉴权数据的配置。

## 必备事项
前提条件

* 已完成UDM的CSP OM Portal侧基础数据的配置。
* 已完成5G的用户数据规划。
* 操作人员具有PGW Web LMT的操作权限。
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

### 2 执行**ADD AMF**命令设置AMF值。

### 3 执行**ADD K4**命令设置用于加密KI的K4值。

### 4 如果USIM卡中烧制了OP，执行**ADD OP**命令设置OP值。

### 设置OP值时，要注意以下几点：

#### 4.1 USIM卡中烧制了OP时，要设置OP值。

#### 4.2 USIM卡中烧制了OPC时，不用设置OP值，需要在5中设置OPC值。

### 5 执行**ADD KI**命令加载KI。

#### 5.1 参数“卡类型”设置为“USIM”。

#### 5.2 参数“鉴权算法类型”根据实际需求进行设置。


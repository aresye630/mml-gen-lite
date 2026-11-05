---
id: ''
name: 单用户开户
ne_type: UEG
type: feature
description: 该操作指导工程师在开局阶段，新建UDM网元时，完成5G单开户数据的配置。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝L","UEG UDM用户管理（风筝L）","用户数据配置（5G SA网络）","5G用户开户配置","单用户开户"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
该操作指导工程师在开局阶段，新建UDM网元时，完成5G单开户数据的配置。

## 必备事项
前提条件

已完成5G用户数据配置。
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

### 2 执行**ADD SUB**命令，为用户开户。

### 3 执行**MOD AMDATA**命令，为用户签约AMF数据。

### 4 执行**ADD SNSSAI**命令，为用户签约切片数据。

### 5 执行**ADD SMDATA**命令，为用户签约会话数据。

### 6 （可选）执行**MOD NGSRRS**命令，为用户签约漫游数据。

### 当需要在UDM中为用户提供基于5GS的漫游限制业务时，需要执行此步骤。


---
id: ''
name: 配置5G模板数据
ne_type: UEG
type: feature
description: 该操作指导工程师在开局阶段，新建UDM网元时，完成5G模板数据的配置。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝L","UEG UDM用户管理（风筝L）","用户数据配置（5G SA网络）","5G用户数据配置","配置5G模板数据"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
该操作指导工程师在开局阶段，新建UDM网元时，完成5G模板数据的配置。

## 必备事项
前提条件

* 已经完成UDM的CSP OM Portal侧基础数据的配置。
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

### 1 登录“UDM业务管理”窗口。

### 2 执行**ADD NGCQOSTPL**命令，增加5G QoS模板。

### 3 执行**ADD DNNQOSTPL**命令，增加5G DNN QoS模板。

### 4 （可选）当运营商需要对禁止区域、区域信息、漫游区域有限制要求时，可通过执行如下命令配置模板数据。

#### 4.1 当需要设置5G禁止区域时，需要执行**ADD FORBIDAREATPL**命令增加5G禁止区域模板，为用户签约5G禁止区域做准备。

#### 4.2 当需要在指定区域限制用户的业务时，需要执行**ADD SERAREATPL**命令增加业务区域信息模板，为用户签约做准备。

#### 4.3 当需要设置NGC漫游限制区域时，需要执行**ADD NGCRRAREATPL**命令增加NGC漫游限制区域模板，为用户签约5G漫游限制功能做准备。

#### 4.4 当需要设置NGC漫游限制状态时，需要执行**ADD NGCRRNODETPL**命令增加NGC漫游限制模板，为用户签约5G漫游限制功能做准备。


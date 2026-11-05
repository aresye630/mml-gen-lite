---
id: ''
name: 查询5G LAN用户是否已在UDM上完成5G LAN组签约
ne_type: UEG
type: feature
description: 必须在UDM上先完成用户的5G LAN组签约，才支持本地调整该用户所属的5G LAN组。  本地调整5G LAN用户签约的5G LAN组ID前，可参考本页面查询5G LAN用户在UDM上是否已签约5G LAN组ID。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝S","MEC 特性指南（风筝S）","UEG特性指南","5G LAN基本功能","可选功能","5G LAN用户本地签约配置（风筝L，通过WebPortal或MML调整）","查询5G LAN用户是否已在UDM上完成5G LAN组签约"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
必须在UDM上先完成用户的5G LAN组签约，才支持本地调整该用户所属的5G LAN组。本地调整5G LAN用户签约的5G LAN组ID前，可参考本页面查询5G LAN用户在UDM上是否已签约5G LAN组ID。

## 必备事项
前提条件

* 已获取登录PGW Web LMT界面的用户名和密码。
* 已获取登录PGW Web LMT界面的IP地址。
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

### 2 执行**LST GROUPID**命令，查询5G LAN用户签约的5G LAN组ID。

### 仅支持基于单个IMSI或基于单个MSISDN查询，选择一种方案查询即可。

#### 2.1 基于单个IMSI查询

##### 2.1.1 ...

##### IMSI = 46000876543210

##### ...

##### INGROUPID = 1001-46008-01

##### ...

#### 2.2 基于单个MSISDN查询

##### 2.2.1 ...

##### ...

##### ISDN = 8613912345678

##### INGROUPID = 1001-46008-01

##### ...

#### 5G LAN用户未在UDM上签约5G LAN组ID时，请先联系华为工程师进行开户。


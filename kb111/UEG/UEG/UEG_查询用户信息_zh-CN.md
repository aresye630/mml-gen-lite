---
id: ''
name: 查询用户信息
ne_type: UEG
type: feature
description: 运营商通过PGW Web客户端可以查询用户的MSISDN或IMSI号码、基本业务的签约情况、用户静态/动态信息。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝L","UEG UDM用户管理（风筝L）","用户数据维护","业务发放操作","查询用户信息"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
运营商通过PGW Web客户端可以查询用户的MSISDN或IMSI号码、基本业务的签约情况、用户静态/动态信息。

## 必备事项
前提条件

要查询的用户已经开户。
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

### 2 如果需要进行非连续用户的批操作，编写IMSIFILE或ISDNFILE批操作资源文件，并上传到PGW Server指定位置。

### ISDNFILE、IMSIFILE批操作资源文件的格式和上传位置请参见批操作管理。

### 批操作资源文件的上传方法请参见管理文件。

### 3 查询用户信息。

#### 3.1 查询用户号码

#### 如果要查询用户的IMSI号码，请执行**LST IMSI**命令。

#### 如果要查询用户的MSISDN号码，请执行**LST ISDN**命令。

#### 3.2 查询用户基本业务

#### 如果要查询用户的电信业务，请执行**LST TS**命令。

#### 如果要查询用户的电路域数据业务，请执行**LST BS**命令。

#### 如果要查询用户的GPRS业务，请执行**LST GPRS**命令。

#### 如果要查询用户的EPS业务，请执行**LST EPS**命令。

#### 如果要查询用户的NGS业务，请执行**LST NGS**命令。

#### 3.3 查询用户静态/动态信息

#### 如果要查询用户的静态信息，请执行**LST SUB**命令。

#### 如果要查询用户的动态信息，请执行**LST DYNSUB**命令。


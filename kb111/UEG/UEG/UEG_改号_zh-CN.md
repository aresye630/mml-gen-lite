---
id: ''
name: 改号
ne_type: UEG
type: feature
description: 运营商通过PGW Web LMT可以为用户改号。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝L","UEG UDM用户管理（风筝L）","用户数据维护","业务发放操作","改号"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
运营商通过PGW Web LMT可以为用户改号。

## 必备事项
前提条件

要改号的用户已经成功开户。
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

#### 2.1 ISDNFILE、IMSIFILE批操作资源文件的格式和上传位置请参见批操作管理。

#### 2.2 批操作资源文件的上传方法请参见管理文件。

### 3 执行**MOD ISDN**命令为指定用户改号。


---
id: ''
name: 销户
ne_type: UEG
type: feature
description: 运营商通过PGW Web LMT可以为用户销户。此操作可以用来为单个用户销户，也可以为多个用户进行批销户。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝L","UEG UDM用户管理（风筝L）","用户数据维护","业务发放操作","销户"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
运营商通过PGW Web LMT可以为用户销户。此操作可以用来为单个用户销户，也可以为多个用户进行批销户。

## 必备事项
前提条件

需要销户的用户已经开户。
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

### 3 执行**RMV SUB**命令销户，销户后，原MSISDN号和IMSI号码对应关系解除，请谨慎执行此步骤。


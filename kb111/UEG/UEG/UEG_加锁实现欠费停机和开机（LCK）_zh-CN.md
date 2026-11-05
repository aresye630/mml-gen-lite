---
id: ''
name: 加锁实现欠费停机和开机（LCK）
ne_type: UEG
type: feature
description: 运营商通过PGW Web LMT可以对欠费用户进行停机和开机。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝L","UEG UDM用户管理（风筝L）","用户数据维护","业务发放操作","停机和开机","加锁实现欠费停机和开机（LCK）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
运营商通过PGW Web LMT可以对欠费用户进行停机和开机。

## 必备事项
前提条件

* 要停机/开机的用户已经开户。
* 要开机的用户已经停机。
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

### 3 执行**MOD LCK**命令为指定用户停机或开机。

### 参数“是否提供锁呼入业务”、“是否提供锁呼出业务”、“是否提供GPRS锁业务”、“是否提供EPS锁业务”、“是否提供NON3GPP锁业务”或“是否提供5GS锁业务”设置为“TRUE”，为用户停机。

### 参数“是否提供锁呼入业务”、“是否提供锁呼出业务”、“是否提供GPRS锁业务”、“是否提供EPS锁业务”、“是否提供NON3GPP锁业务”或“是否提供5GS锁业务”设置为“FALSE”，为用户开机。


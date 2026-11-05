---
id: ''
name: 查看PGW操作日志
ne_type: UEG
type: feature
description: PGW操作日志记录了操作执行的记录，主要用于运营商处理投诉和技术人员故障定位。通过查看一个操作员在PGW Web LMT界面进行的相关操作，以帮助解决问题。
tags: []
risk_level: ''
doc_source: ["日常维护","UEG 基础运维操作（风筝M，虚机容器）","获取日志","USCDB日志说明","PGW操作日志","查看PGW操作日志"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
PGW操作日志记录了操作执行的记录，主要用于运营商处理投诉和技术人员故障定位。通过查看一个操作员在PGW Web LMT界面进行的相关操作，以帮助解决问题。

## 必备事项
前提条件

该操作无需具备特殊条件。
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

### 1 登录PGW客户端。

### 登录方法请参见登录与退出PGW Web LMT。

### 2 执行命令**LST LOG**查看操作日志。


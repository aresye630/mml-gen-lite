---
id: ''
name: 统计用户数
ne_type: UEG
type: feature
description: 运营商通过PGW Web LMT可以统计用户数。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝L","UEG UDM用户管理（风筝L）","用户数据维护","业务发放操作","统计用户数"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
运营商通过PGW Web LMT可以统计用户数。

## 必备事项
前提条件

无。
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

### 2 执行**LST SUBDATA**命令查询用户的统计数据。


---
id: ''
name: 配置证书到期提醒时间
ne_type: UEG
type: feature
description: 为防止证书到期影响系统业务，需通过该章节配置证书到期提醒时间。
tags: []
risk_level: ''
doc_source: ["网络部署","园区入驻+地市共享（连接+计算）","5GC toB 部署边缘站点（站点为“风筝M”，带计算）","配置安全数据（风筝M）","安全配置（虚机容器）","安全配置建议","必选配置","网络安全配置","配置证书到期提醒时间"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
为防止证书到期影响系统业务，需通过该章节配置证书到期提醒时间。

## 必备事项
前提条件

已登录OM Portal。
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

### 1 选择“应用管理 > MML”，选择需要执行MML的应用窗口。

### 2 执行**MOD REMINDTIME**命令配置证书到期提醒时间。


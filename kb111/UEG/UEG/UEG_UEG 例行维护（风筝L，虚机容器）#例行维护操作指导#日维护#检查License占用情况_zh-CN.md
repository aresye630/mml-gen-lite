---
id: ''
name: 检查License占用情况
ne_type: UEG
type: feature
description: 检查系统License占用情况，在使用率过高情况下，确认过高的原因以及是否需要进行License扩容。
tags: []
risk_level: ''
doc_source: ["日常维护","UEG 例行维护（风筝L，虚机容器）","例行维护操作指导","日维护","检查License占用情况"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
检查系统License占用情况，在使用率过高情况下，确认过高的原因以及是否需要进行License扩容。

## 必备事项
前提条件

已经登录OM Portal，或者登录MAE并进入Access子系统。
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

### 1 通过****DSP LICENSERESEDGE****命令查看License资源数目以及使用情况。

### 2 通过****DSP LICENSEPEAK****命令查看话务高峰内的过载License项目以及剩余可用次数。


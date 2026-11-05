---
id: ''
name: 检查补丁状态
ne_type: UNC
type: feature
description: 该操作是对已经安装好的补丁进行全面检查，以确认补丁的运行状态是否正常。
risk_level: ''
doc_source: ["网络运维","日常维护","UNC例行维护","例行维护操作指导","月度维护","检查补丁状态"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
该操作是对已经安装好的补丁进行全面检查，以确认补丁的运行状态是否正常。

## 必备事项
前提条件

已经登录OM Portal，或者已登录U2020，或者登录MAE并进入Access子系统。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties: {}
  examples: {}
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 通过执行****DSP ACSPATCHINFO****命令查看当前系统中已有补丁的状态以及生效时间。

### 预期结果：“补丁状态”为“运行”。

### 2 如果检查结果不符合预期，请查看是否存在补丁相关告警并处理。

### 3 如果告警处理完毕后，运行状态仍然不符合预期，请收集相关信息并联系华为技术支持处理。


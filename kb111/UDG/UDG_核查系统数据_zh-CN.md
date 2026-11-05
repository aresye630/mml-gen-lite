---
id: ''
name: 核查系统数据
ne_type: UDG
type: feature
description: 为了避免在设备运行过程中设备配置数据出现偏差，需要定期核查系统数据，确保系统数据与运营商规划保持一致，参数设置符合运营商要求。
risk_level: ''
doc_source: ["网络运维","日常维护","UDG例行维护","例行维护操作指导","季度维护","核查系统数据"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
为了避免在设备运行过程中设备配置数据出现偏差，需要定期核查系统数据，确保系统数据与运营商规划保持一致，参数设置符合运营商要求。

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

### 1 通过**EXP MML**命令导出系统配置数据文件，并与运营商规划数据进行核对。

### 预期结果：实际配置与运营商规划一致。

### 2 如果不一致，请对不一致的配置数据进行逐一确认和处理。


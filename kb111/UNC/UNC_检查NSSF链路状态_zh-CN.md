---
id: ''
name: 检查NSSF链路状态
ne_type: UNC
type: feature
description: 通过检查NSSF的链路状态，确保NSSF与其他NF间交互链路正常，保证NSSF正常提供业务。
risk_level: ''
doc_source: ["网络部署","业务专题","5G Core NSSF解决方案","例行维护","检查NSSF链路状态"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
通过检查NSSF的链路状态，确保NSSF与其他NF间交互链路正常，保证NSSF正常提供业务。

## 必备事项
前提条件

操作人员已经登录OM Portal或U2020/MAE。
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

### 1 在NSSF上，执行**DSP SBILINKSTATUS**命令，检查NSSF作为服务端时的服务化接口链路状态。

### 预期结果：“链路状态”为“正常”。

### 非预期结果：“链路状态”为非“正常”，执行2。

### 2 检查结果不符合预期，请收集告警信息、日志信息和配置信息，并联系华为技术支持处理。


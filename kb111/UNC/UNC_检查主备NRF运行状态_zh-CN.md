---
id: ''
name: 检查主备NRF运行状态
ne_type: UNC
type: feature
description: 通过检查NRF容灾组的运行状态，确保主、备NRF运行正常。
risk_level: ''
doc_source: ["网络部署","业务专题","5G Core NRF解决方案","例行维护","检查主备NRF运行状态"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
通过检查NRF容灾组的运行状态，确保主、备NRF运行正常。

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

### 1 分别通过**DSP GRGROUP**命令查询正在运行的主、备NRF的状态信息，容灾数据备份状态信息是否与实际规划一致。

#### 1.1 预期结果：

##### 1.1.1 “运行状态”为“主”或“备”，“握手状态”为“连接”。

##### 1.1.2 “容灾数据备份状态”为“实时备份”或短时间为“批量备份”。

#### 1.2 非预期结果：执行2。

##### 1.2.1 “运行状态”为“无”或“空闲”。

##### 1.2.2 “运行状态”为“主”或“备”，“握手状态”为“断连”。

##### 1.2.3 “容灾数据备份状态”为“无备份”或“异常”或一直为“批量备份”。

### 2 检查结果不符合预期，请收集告警信息、日志信息和配置信息，并联系华为技术支持处理。


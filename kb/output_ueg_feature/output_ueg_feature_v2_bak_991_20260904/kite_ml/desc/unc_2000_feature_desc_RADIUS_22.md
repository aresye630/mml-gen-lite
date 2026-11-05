# 修改AAA计费的可选计费消息属性

- 操作场景
- 对系统的影响
- 必备事项
- 操作步骤
- 任务示例

## 操作场景

当计费策略发生改变时，需要在UEG上修改可选计费消息属性。

**说明** 

适用于PGW-C、SMF

## 对系统的影响

修改此属性之后，由于话单中所含字段增加，会对系统性能有一定的影响。

## 必备事项

前提条件

完成配置RADIUS功能。

数据

数据

| 类别              | 参数名称                                 | 取值样例   | 获取方法     | 说明                                       |
|:----------------|:-------------------------------------|:-------|:---------|:-----------------------------------------|
| RADIUS Server信息 | Radius Server Group名称（RDSSVRGRPNAME） | ss     | 已配置数据中获取 | 计费服务器所在的Radius服务器组，已通过ADD RDSSVRGRP进行配置。 |
| RADIUS Server信息 | 支持携带属性Trigger-type（TRIGGERTYPE）      | ENABLE | 本端规划     | SET RDSACCTREQATTR                       |

**说明** 

本文以支持携带属性Trigger-type为例说明修改步骤，其他参数的修改步骤类似。

## 操作步骤

1. 进入“MML命令行-UEG”窗口。
2. 修改AAA计费的可选计费消息属性，支持携带属性Trigger-type。

   **SET RDSACCTREQATTR**

## 任务示例

任务描述

修改Radius Server Group实例“ss”下AAA计费的可选计费消息属性为“ENABLE”。

脚本

//修改AAA计费的可选计费消息属性，支持携带属性Trigger-type。

```
SET RDSACCTREQATTR: RDSSVRGRPNAME="ss",TRIGGERTYPE=ENABLE;
```
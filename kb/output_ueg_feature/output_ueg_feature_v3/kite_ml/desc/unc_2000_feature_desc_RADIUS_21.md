# 修改AAA计费的3GPP扩展属性

* 操作场景
* 对系统的影响
* 必备事项
* 操作步骤
* 任务示例

## 操作场景

当AAA Server的3GPP扩展属性发生变化时，UEG需要修改AAA计费的3GPP扩展属性以便和AAA Server保持一致。

适用于PGW-C、SMF

## 对系统的影响

修改此属性之后，由于话单中所含字段变化，会对系统性能有一定的影响。

## 必备事项

前提条件

完成配置RADIUS功能。

数据

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| RADIUS Server信息 | Radius Server Group名称（RDSSVRGRPNAME） | ss | 已配置数据中获取 | 计费服务器所在的Radius服务器组，已通过**ADD RDSSVRGRP**进行配置。 |
|  | 支持3gpp私有扩展属性（THREEGPP） | ENABLE | 与对端协商 | **SET RDSACCTREQVSA** |

## 操作步骤

1. 进入“MML命令行-UEG”窗口。
2. 修改AAA计费的3GPP扩展属性。

   **SET RDSACCTREQVSA**

## 任务示例

任务描述

修改Radius Server Group实例“ss”下AAA计费的3GPP扩展属性为“ENABLE”，而3GPP2扩展属性为“DISABLE”。

脚本

//修改AAA计费的3GPP扩展属性。

```
SET RDSACCTREQVSA: RDSSVRGRPNAME="ss",THREEGPP=ENABLE,THREEGPP2=DISABLE;
```

版权所有 © 华为技术有限公司

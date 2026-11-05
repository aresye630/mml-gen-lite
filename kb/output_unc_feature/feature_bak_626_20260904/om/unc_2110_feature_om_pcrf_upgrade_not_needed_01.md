# 激活PCRF免升级

- 操作场景
- 必备事项
- 操作步骤
- 任务示例

## 操作场景

在部署NB-IoT业务时，为实现PCRF免升级即可支持NB-IoT用户接入，需要开启该功能。

**说明** 

适用于PGW-C。

## 必备事项

前提条件

- 请仔细阅读WSFD-215302 PCRF免升级特性概述。
- 完成加载License。

数据

| 类别                | 参数                   | 取值样例   | 获取方法   | 说明        |
|:------------------|:---------------------|:-------|:-------|:----------|
| SET NBIOTRATVALUE | 和PCRF交互使用的RAT值（PCRF） | EUTRAN | 本端规划   | PCRF免升级功能 |

## 操作步骤

1. 进入“MML命令行-UNC”窗口。
2. 打开本特性的License配置开关。

   **SET LICENSESWITCH**
3. 配置开启PCRF免升级功能。

   **SET NBIOTRATVALUE**

## 任务示例

任务描述

在UNC上配置PCRF免升级功能，配置UNC给PCRF发送消息时，RAT信元携带的值为EUTRAN。

脚本

```
SET LICENSESWITCH:LICITEM="LKV3WNPUNN11",SWITCH=ENABLE;
```

```
SET NBIOTRATVALUE: PCRF=EUTRAN;
```
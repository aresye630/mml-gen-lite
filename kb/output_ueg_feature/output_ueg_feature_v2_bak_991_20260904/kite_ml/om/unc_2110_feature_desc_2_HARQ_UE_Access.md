# 激活支持2 HARQ终端接入

- 操作场景
- 必备事项
- 操作步骤
- 任务示例

## 操作场景

本操作指导用于使用支持2 HARQ终端接入特性前对该特性的激活操作。

**说明** 

适用于MME。

## 必备事项

前提条件

- 请仔细阅读GWFD-026109 支持2 HARQ终端接入特性概述。
- 完成激活GWFD-026105 基于信令面的数据传输（MME）。

数据

| 类别                | 参数名称              | 取值样例       | 获取方法   | 说明                |
|:------------------|:------------------|:-----------|:-------|:------------------|
| SET LICENSESWITCH | License项（LICITEM） | LKV2HARQ01 | 本端规划   | 用于配置License控制项开关。 |
| SET LICENSESWITCH | 开关（SWITCH）        | ENABLE     | 本端规划   | 用于配置License控制项开关。 |

## 操作步骤

1. 进入“MML命令行-UEG”窗口。
2. 打开本特性的License配置开关。

   **SET LICENSESWITCH**

## 任务示例

任务描述

启用支持2 HARQ终端接入功能。

脚本

//打开本特性的License配置开关。

```
SET LICENSESWITCH: LICITEM="LKV2HARQ01", SWITCH=ENABLE;
```
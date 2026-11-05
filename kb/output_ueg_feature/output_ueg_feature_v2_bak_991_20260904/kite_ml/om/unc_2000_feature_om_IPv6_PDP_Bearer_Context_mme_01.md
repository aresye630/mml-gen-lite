# 激活IPv6承载上下文特性（适用于MME、SGW-C/PGW-C）

- 操作场景
- 必备事项
- 操作步骤
- 任务示例

## 操作场景

本操作指导介绍在运行网络中激活IPv6承载上下文的操作过程。

**说明** 

适用于MME、SGW-C、PGW-C。

## 必备事项

前提条件

- 请仔细阅读GWFD-022901 IPv6承载上下文特性概述（MME、S/PGW-C）。
- 完成加载License。

数据

该操作无需准备数据。

## 操作步骤

1. 进入“MML命令行-UEG”窗口。
2. 打开IPv6承载上下文特性的License配置开关。

   设置License项的开关（SET LICENSESWITCH）**SET LICENSESWITCH**

## 任务示例

任务描述

启用IPv6承载上下文特性。

脚本

```
SET LICENSESWITCH: LICITEM="LKV2IPV601", SWITCH=ENABLE;
SET LICENSESWITCH: LICITEM="LKV2IPV6SM01", SWITCH=ENABLE;
```
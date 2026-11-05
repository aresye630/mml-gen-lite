# 激活支持Category NB2 接入（S/PGW-C）

- 操作场景
- 必备事项
- 操作步骤
- 任务示例

## 操作场景

本操作指导介绍在运行网络中激活支持Category NB2 接入特性的操作过程。

**说明** 

SGW-C、PGW-C

## 必备事项

前提条件

- 请仔细阅读GWFD-026108 支持Category NB2 接入特性概述（S/PGW-C）。
- 完成加载License。

数据

该操作无需准备数据。

## 操作步骤

1. 进入“MML命令行-UEG”窗口。
2. 打开本特性的License配置开关。

   **SET LICENSESWITCH**
3. 打开本特性的软参配置开关。

   **SET SMFSOFTPARA**

## 任务示例

任务描述

在UEG上配置支持Category NB2 接入功能。

脚本

//打开本特性的License配置开关。

```
SET LICENSESWITCH:LICITEM="LKV3WSNBAC21",SWITCH=ENABLE;
```

//打开本特性的软参配置开关。

```
SET SMFSOFTPARA:DT=Bit,BITNUM=717,BITVALUE=1;
```
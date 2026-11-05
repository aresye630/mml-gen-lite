# 激活IPv4v6双栈接入特性（适用于PGW-C）

- 操作场景
- 必备事项
- 操作步骤
- 任务示例

## 操作场景

本操作指导介绍在运行网络中激活IPv4v6双栈接入特性的操作过程。

**说明** 

适用于PGW-C。

## 必备事项

前提条件

- 请仔细阅读GWFD-022903 IPv4v6双栈接入特性概述（适用于2G/3G/4G）。

- 完成加载License。
- 支持IPv4v6的用户已经接入到网络。

数据

该操作无需准备数据。

## 操作步骤

1. 进入“MML命令行-UEG”窗口。
2. 打开IPv6承载上下文特性的License配置开关。

   **SET LICENSESWITCH**

## 任务示例

任务描述

开启IPv4v6双栈接入功能。

脚本

//打开本特性的License配置开关。

```
SET LICENSESWITCH: LICITEM="LKV2IPDSSM01", SWITCH=ENABLE;
```
# 激活Non-IP数据传输（S/PGW-C）

- 操作场景
- 必备事项
- 操作步骤
- 任务示例

## 操作场景

本操作指导介绍在运行网络中激活Non-IP数据传输特性的操作过程。当Non-IP用户接入网络时，需要在UEG上开启Non-IP功能开关，并且为Non-IP用户配置目的服务器的地址。

**说明** 

SGW-C、PGW-C

## 必备事项

前提条件

- 请仔细阅读GWFD-026107 Non-IP数据传输特性概述（S/PGW-C）。
- 完成激活基于信令面的数据传输（SGW-C）。
- 完成加载License。

数据

| 类别                 | 参数名称                         | 取值样例          | 获取方法     | 说明                |
|:-------------------|:-----------------------------|:--------------|:---------|:------------------|
| SET NONIPFUNC      | Non-IP功能开关（NONIPSWITCH）      | ENABLE        | 本端规划     | 全局Non-IP功能开关      |
| SET APNNONIPFUNC   | APN                          | test          | 已配置数据中获取 | 指定APN下的Non-IP功能开关 |
| SET APNNONIPFUNC   | APN Non-IP功能开关（NONIPSWITCH）  | ENABLE        | 本端规划     | 指定APN下的Non-IP功能开关 |
| ADD CPM2MSERVERGRP | M2M服务器组名称（GROUPNAME）         | m2msrvgroup01 | 本端规划     | M2M服务器组           |
| ADD CPM2MSERVERGRP | M2M服务器IP地址类型（SERVERIPTYPE）   | IPV4          | 与对端协商    | M2M服务器组           |
| ADD CPM2MSERVER    | M2M服务器组名称（GROUPNAME）         | m2msrvgroup01 | 已配置数据中获取 | M2M服务器            |
| ADD CPM2MSERVER    | M2M服务器索引（SERVERINDEX）        | 1             | 本端规划     | M2M服务器            |
| ADD CPM2MSERVER    | M2M服务器IP地址类型（SERVERIPTYPE）   | IPV4          | 与对端协商    | M2M服务器            |
| ADD CPM2MSERVER    | M2M服务器IPv4地址（SERVERIPV4ADDR） | 10.107.242.16 | 全网规划     | M2M服务器            |
| ADD CPM2MSERVER    | 服务器端口号（SERVERPORT）           | 2020          | 与对端协商    | M2M服务器            |
| ADD M2MSVRGRPBIND  | M2M服务器组名称（GROUPNAME）         | m2msrvgroup01 | 本端规划     | 指定M2M服务器组的名称      |
| ADD M2MSVRGRPBIND  | APN                          | test          | 本端规划     | 指定APN实例名称         |

## 操作步骤

1. 进入“MML命令行-UEG”窗口。
2. 打开本特性的License配置开关。

   **SET LICENSESWITCH**
3. 使能全局的Non-IP功能开关。

   **SET NONIPFUNC**
4. 使能指定APN下的Non-IP功能开关。

   **SET APNNONIPFUNC**

   **说明** 

   业务处理过程中优先应用APN下的设置，只有当APN下配置为Inherit时才应用全局下的设置。
5. 配置M2M服务器组。

   **ADD CPM2MSERVERGRP**
6. 配置M2M服务器组下的M2M服务器。

   **ADD CPM2MSERVER**
7. **可选：**配置指定APN下的M2M服务器组。

   **ADD M2MSVRGRPBIND**
8. **可选：**配置话单中是否携带pdp-type-extension、sgi-ptp-tunnelling-method字段。

   **ADD CDRFIELDTEMP**

## 任务示例

任务描述

在UEG上配置Non-IP数据传输功能。

脚本

//打开本特性的License配置开关。

```
SET LICENSESWITCH:LICITEM="LKV3WNBNIP11",SWITCH=ENABLE;
```

//使能全局的Non-IP功能开关。

```
SET NONIPFUNC:NONIPSWITCH=ENABLE;
```

//使能ITEM指定APN下的Non-IP功能开关。

```
SET APNNONIPFUNC:APN="test",NONIPSWITCH=ENABLE;
```

//配置组名为“m2msrvgroup01”，服务器IP类型为IPV4的M2M服务器组。

```
ADD CPM2MSERVERGRP: GROUPNAME="m2msrvgroup01", SERVERIPTYPE=IPV4;
```

//在“m2msrvgroup01”M2M服务器组下新增一个M2M服务器。

```
ADD CPM2MSERVER: GROUPNAME="m2msrvgroup01", SERVERINDEX=1, SERVERIPTYPE=IPV4, SERVERIPV4ADDR="10.107.242.16", SERVERPORT=2020;
```

//配置APN与M2M服务器组的绑定。

```
ADD M2MSVRGRPBIND: APN="test", GROUPNAME="m2msrvgroup01";
```

//可选：配置话单中携带pdp-type-extension、sgi-ptp-tunnelling-method字段。

```
ADD CDRFIELDTEMP:TEMPLATENAME="cdrfieldtemp",PDPTYPEEXT=ENABLE,SGIPTPTUNMETH=ENABLE;
```
# 去激活QoS简单流分类（VNRS\_VNFC）

- 操作场景
- 对系统的影响
- 必备事项
- 操作流程
- 操作步骤
- 任务示例

## 操作场景

本操作指导介绍在运行网络中去激活QoS简单流分类功能的操作过程。

## 对系统的影响

无

## 必备事项

前提条件

- 操作人员已经登录网络管理系统NMS（Network Management System）。
- 已经激活QoS简单流分类。

数据

无需准备数据。

## 操作流程

去激活QoS简单流分类特性操作流程如图1所示。

**图1** 去激活QoS简单流分类特性操作流程

## 操作步骤

1. 删除对应的QOSIFTRUST。

   在“MML命令行-UDG”窗口上执行：

   **RMV QOSIFTRUST**: IFNAME="接口名称";
2. 当需要删除对应的DiffServ域。

   在“MML命令行-UDG”窗口上执行：

   **RMV QOSDIFFERSERV**: DSNAME="DS名称";
3. 当需要删除对应的重定向至指定VPN的配置。

   在“MML命令行-UDG”窗口上执行：

   **RMV QOSRDRVPN**: IFNAME ="接口名称";
4. 当需要去激活QoS不检查PHB表。

   在“MML命令行-UDG”窗口上执行：

   **RMV QOSIFPHB**: IFNAME="接口名称", PHBTYPE=出接口报文的优先级字段映射类型;

## 任务示例

任务描述

- 删除配置的QOSIFTRUST。
- 去激活QoS不检查PHB表。

脚本

//删除配置的QOSIFTRUST。

```
RMV QOSIFTRUST: IFNAME="Ethernet64/0/3";
```

//删除配置的DiffServ域。

```
RMV QOSDIFFERSERV: DSNAME="ds1";
```

//对以太接口Ethernet64/0/3去激活QoS不检查PHB表。

```
RMV QOSIFPHB: IFNAME="Ethernet64/0/3",PHBTYPE=dscp;
```
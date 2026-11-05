# 配置CP白名单功能

* 操作场景
* 必备事项
* 操作步骤
* 任务示例

## 操作场景

当前一个UPF最多与64个SMF建立偶联，为防止仿冒的SMF向N4接口发送PFCP消息，恶意消耗偶联资源或干扰已经建立的偶联工作，建议开启CP白名单功能，只允许白名单范围内的SMF与UPF建立偶联。

适用于SGW-U、PGW-U、UPF。

## 必备事项

前提条件

无。

数据

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| **SET CPACCESSLISTFUNC** | 开关标识（SWITCH） | ENABLE | 本端规划 | - |
| **ADD CPACCESSLIST** | 白名单参数类型（WHITELISTTYPE） | NODEID | 全网规划 | - |
|  | CP Node ID类型（CPNODEIDTYPE） | FQDN | 全网规划 | - |
|  | CP Node ID的FQDN（CPNODEIDFQDN） | smf1 | 全网规划 | - |

## 操作步骤

1. 使能CP白名单开关。

   **SET CPACCESSLISTFUNC**:SWITCH=开关标识;
2. 配置CP白名单。

   **ADD CPACCESSLIST**:WHITELISTTYPE=白名单参数类型, IPVERSION=IP地址版本类型, CPNODEIDTYPE=CP Node ID类型, CPIPV4=CP IPv4地址, CPIPV6=CP IPv6地址, CPIPV4MASK=CP IPv4掩码长度, CPIPV6MASK=CP IPv6掩码长度, CPNODEIDIPV4="CP Node ID中的IPv4地址", CPNODEIDIPV6="CP Node ID中的IPv6地址", CPNODEIDFQDN="CP Node ID的FQDN";

## 任务示例

任务描述

本实例中，操作员在UDG上进行数据配置实现以下要求：

根据SMF的NodeID配置CP白名单，并使能CP白名单功能。

脚本

//使能CP白名单开关。

```
SET CPACCESSLISTFUNC:SWITCH=ENABLE;
```

//配置CP白名单。

```
ADD CPACCESSLIST:WHITELISTTYPE=NODEID,CPNODEIDTYPE=FQDN,CPNODEIDFQDN="smf1";
```

版权所有 © 华为技术有限公司

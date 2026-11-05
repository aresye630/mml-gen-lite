# 激活支持多PDN功能（适用于4G）

* 操作场景
* 必备事项
* 操作步骤
* 任务示例

## 操作场景

当UE需要同时访问多个网络，可以开启本功能，并针对特定APN，配置用户可以建立的PDN连接最大数目和IP地址最大数目。

多PDN/PDU（Packet Data Network）功能是指一个UE同时创建多个PDN连接（EPC）/PDU会话（5GC）来访问外部多个PDN网络，满足用户同时访问多个网络的要求。

## 必备事项

前提条件

请仔细阅读GWFD-020809 支持多PDN/PDU功能特性概述。

数据

| 类别 | 参数 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| ****ADD APNACTNUM**** | APN网络标识（APNNI） | Internet | 全网规划 | - |
|  | PDN连接数目（PDNNUM） | 2 |  |  |
|  | IPv4地址数目（IPV4ADDRNUM） | 2 |  |  |
|  | IPv6地址数目（IPV6ADDRNUM） | 2 |  |  |
|  | PDN连接拒绝原因（PDNCONNREJCAUSE） | MULTI\_PDN\_FOR\_APN\_NOT\_ALW\_55 |  |  |

## 操作步骤

1. 进入“MML命令行-UEG”窗口。
2. 配置针对某一APN，同一个用户可以建立的PDN连接最大数目和IP地址最大数目。

   ****ADD APNACTNUM****

## 任务示例

任务描述

配置针对APN“Internet”和“WAP”，同一个用户可以建立的PDN连接最大数目为2，IPv4地址最大数目为2，IPv6地址最大数目为2。当终端建立的PDN连接个数或IP地址个数到达设置的阈值时，系统给终端回复PDN连接拒绝消息携带的原因值为“MULTI\_PDN\_FOR\_APN\_NOT\_ALW\_55”。

脚本

//配置APN“Internet”下的数据。

```
ADD APNACTNUM: APNNI="Internet", PDNNUM=2, IPV4ADDRNUM=2, IPV6ADDRNUM=2, PDNCONNREJCAUSE=MULTI_PDN_FOR_APN_NOT_ALW_55;
```

//配置APN“WAP”下的数据。

```
ADD APNACTNUM: APNNI="WAP", PDNNUM=2, IPV4ADDRNUM=2, IPV6ADDRNUM=2, PDNCONNREJCAUSE=MULTI_PDN_FOR_APN_NOT_ALW_55;
```

版权所有 © 华为技术有限公司

# 激活服务化接口发送消息固定速率流控功能

* 操作场景
* 必备事项
* 操作步骤
* 任务示例

## 操作场景

服务化接口固定速率流控功能是指在服务化接口存在拥塞风险时，UEG基于配置的服务化接口流控速率阈值，控制接口上发送消息的速率，减少服务化接口拥塞，避免对端网元过载。

本章节以本端网元为AMF，对端网元为UDM举例。

适用于AMF、SMF、NSSF

## 必备事项

前提条件

该操作无需具备特殊条件。

数据

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| **ADD HTTPFCIPGRP** | 索引（Index） | 1 | 全网规划 | 设置流控组信息。  说明：  本端网元作为客户端的业务，选择对端网元的IP地址作为流控组的IP地址，如果是间接路由场景，选择下一跳（例如SCP）的IP地址作为流控组的IP地址；本端网元作为服务端的业务，选择本端网元配置的HTTPLE的服务端IP作为流控组的IP地址。 |
|  | 流控组（GROUP） | 1 |  |  |
|  | IP地址类型（IPTYPE） | IPv4 |  |  |
|  | IPv4地址（IPV4ADDR） | 192.168.100.1 |  |  |
|  | IPv4掩码（IPV4MASK） | 255.255.255.255 |  |  |
|  | 描述（DESC） | UDM\_instance1 |  |  |
|  | 索引（Index） | 2 |  |  |
|  | 流控组（GROUP） | 1 |  |  |
|  | IP地址类型（IPTYPE） | IPv4 |  |  |
|  | IPv4地址（IPV4ADDR） | 192.168.100.2 |  |  |
|  | IPv4掩码（IPV4MASK） | 255.255.255.255 |  |  |
|  | 描述（DESC） | UDM\_instance1 |  |  |
|  | 索引（Index） | 3 |  |  |
|  | 流控组（GROUP） | 2 |  |  |
|  | IP地址类型（IPTYPE） | IPv4 |  |  |
|  | IPv4地址（IPV4ADDR） | 192.168.200.1 |  |  |
|  | IPv4掩码（IPV4MASK） | 255.255.255.255 |  |  |
|  | 描述（DESC） | UDM\_instance1 |  |  |
| **ADD HTTPFIXEDFC** | 流控组（GROUP） | 1 | 全网规划 | 增加HTTP流控门限。  说明：  此处门限值为举例，请根据局点实际情况进行设置。 |
|  | 流控组类型（GROUPTYPE） | CLIENT |  |  |
|  | 单链路发送消息流控门限(条/秒)（SENDTHD） | 1000 |  |  |
|  | 描述（DESC） | LINK |  |  |
|  | 流控组（GROUP） | 2 |  |  |
|  | 流控组类型（GROUPTYPE） | CLIENT |  |  |
|  | 整系统发送消息流控门限(条/秒)（GLBSENDTHD） | 2000 |  |  |
|  | 描述（DESC） | GLOBAL |  |  |

## 操作步骤

1. 进入“MML命令行-UEG”窗口。
2. 增加HTTP固定速率流控的IP地址组信息。

   **ADD HTTPFCIPGRP**
3. AMF上增加HTTP流控门限。

   **ADD HTTPFIXEDFC**

## 任务示例

任务描述

重大活动期，可以预期大量用户接入5G网络同时发生，因此AMF打开服务化接口固定速率流控功能，设置发送给UDM的消息固定流控速率，提高用户接入成功率。

**任务1：**AMF作为客户端，配置链路粒度的固定流控速率。

**任务2：**AMF作为客户端，配置整机粒度的固定流控速率。

脚本

**任务1：**

//配置流控组信息。

```
ADD HTTPFCIPGRP: INDEX=1, GROUP=1, IPTYPE=IPv4, IPV4ADDR=192.168.100.1, IPV4MASK=255.255.255.0, DESC="UDM_instance1"; 
ADD HTTPFCIPGRP: INDEX=2, GROUP=1, IPTYPE=IPv4, IPV4ADDR=192.168.100.2, IPV4MASK=255.255.255.0, DESC="UDM_instance2";
```

//配置流控速率。

```
ADD HTTPFIXEDFC: GROUP=1, GROUPTYPE=CLIENT, SENDTHD=1000, DESC="LINK";
```

**任务2**：

//配置流控组信息。

```
ADD HTTPFCIPGRP: INDEX=3, GROUP=2, IPTYPE=IPv4, IPV4ADDR=192.168.200.1, IPV4MASK=255.255.255.0, DESC="UDM_instance1";
```

//配置流控速率。

```
ADD HTTPFIXEDFC: GROUP=2, GROUPTYPE=CLIENT, GLBSENDTHD=2000, DESC="GLOBAL";
```

版权所有 © 华为技术有限公司

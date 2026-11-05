# 激活防DDoS功能

* 操作场景
* 必备事项
* 操作步骤
* 任务示例

## 操作场景

为了防止PDN侧网络设备遭受移动用户的DDoS攻击，运营商可以启用UDG的防范DDoS攻击功能。在UDG上配置报文连接最大速率，当UE向PDN侧网络设备发起TCP连接，如果UE发送的SYN报文连接速率超过配置值，UDG将丢弃报文，以保护PDN侧的网络设备。

* 适用于SGW-U、PGW-U、UPF。
* 当运营商需要通过UDG保护PDN侧指定范围服务器时开启此功能，典型场景下“DDos防护阈值”可使用系统初始值。功能开启后应密切观察KPI指标和DDoS攻击监测指标，例如“1914308686 用户平面上行丢弃报文数(DDoS攻击)”、“1914308724 用户平面上行丢弃IPv6报文数(DDoS攻击)”等性能指标的变化情况，确保网元正常功能不受影响。

## 必备事项

前提条件

请仔细阅读GWFD-010253 防DDoS功能。

数据

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| **SET DDOS** | DDos防护阈值（THRESHOLD） | 10 | 本端规划 | 允许发起最大TCP连接数。 |
| **ADD USERPROFILE** | 用户模板名称（USERPROFILENAME） | up\_test | 本端规划 | - |
|  | 防DDOS攻击标记（DDOSCHECK） | ENABLE | 本端规划 |  |

## 操作步骤

1. 设置DDoS攻击防护使用的流控阈值。

   **SET DDOS**
2. 使能UserProfile的防范DDoS功能。

   **ADD USERPROFILE**

## 任务示例

任务描述

为了防止PDN侧网络设备遭受移动用户的DDoS攻击，采用防范DDoS攻击功能。

脚本

//设置防范DDoS攻击的流控阈值。

```
SET DDOS:THRESHOLD=10;
```

//使能UserProfile的防范DDoS功能。

```
ADD USERPROFILE:USERPROFILENAME="up_test",DDOSCHECK=ENABLE;
```

版权所有 © 华为技术有限公司

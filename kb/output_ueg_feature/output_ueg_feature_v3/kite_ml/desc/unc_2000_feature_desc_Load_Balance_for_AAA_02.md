# 激活AAA负荷分担

* 操作场景
* 必备事项
* 操作步骤
* 任务示例

## 操作场景

部署多台负荷分担的AAA服务器，解决网络中AAA鉴权和计费的拥塞问题。

适用于PGW-C、SMF

## 必备事项

前提条件

* 请仔细阅读GWFD-024305 AAA负荷分担特性概述。
* 如果运营商规划采用VPN组网方式，则操作员在执行本操作前应已创建了相应的VPN实例。
* 完成增加APN配置。

数据

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| **ADD RDSSVRGRP** | Radius Server Group名称（RDSSVRGRPNAME） | isprg | 已配置数据中获取 | 配置AAA服务器组。  已通过**ADD RDSSVRGRP**命令配置，可以使用**LST RDSSVRGRP**命令进行查询。 |
|  | 模式（MODE） | ROUND\_ROBIN | 本端规划 |  |
|  | 支持可选计费消息（SIGOPTACCTMSG） | DISABLE | 本端规划 |  |
| **ADD RDSSVR** | Radius Server Group名称（RDSSVRGRPNAME） | isprg | 本端规划 | 配置AAA鉴权服务器。与AAA鉴权服务器的IP地址保持一致。 |
|  | 服务器类型（SERVERTYPE） | AUTHENTICATION | 本端规划 |  |
|  | 服务器IP版本（IPVERSION） | IPV4 | 全网规划 |  |
|  | IPv4地址（SERVERIPV4） | 192.168.7.12  192.168.7.14 | 全网规划 |  |
|  | VPN实例（VPNINSTANCE） | vpn\_Gi | 已配置数据中获取 | 已通过 **ADD CPVPNINST**命令配置，可以使用 **LST CPVPNINST**命令进行查询。 |
|  | 端口（PORT） | 1812 | 本端规划 | - |
|  | 服务器密钥（加密的）（CIPHERKEY） | ispchina | 本端规划 |  |
|  | 主备用类型（PRIFLAG） | PRIMARY | 本端规划 |  |
|  | 确认服务器密钥（加密的）(CIPHERKEYCNFM) | ispchina | 本端规划 |  |
| **ADD RDSSVR** | Radius Server Group名称（RDSSVRGRPNAME） | isprg | 本端规划 | 配置AAA计费服务器。与AAA计费服务器的IP地址保持一致。 |
|  | 服务器类型（SERVERTYPE） | ACCOUNTING | 本端规划 |  |
|  | 服务器IP版本（IPVERSION） | IPV4 | 全网规划 |  |
|  | IPv4地址（SERVERIPV4） | 192.168.7.12  192.168.7.14 | 全网规划 |  |
|  | VPN实例（VPNINSTANCE） | vpn\_Gi | 已配置数据中获取 | 已通过 **ADD CPVPNINST**命令配置，可以使用 **LST CPVPNINST**命令进行查询。 |
|  | 端口（PORT） | 1813 | 本端规划 | - |
|  | 服务器密钥（加密的）（CIPHERKEY） | ispkey | 本端规划 |  |
|  | 主备用类型（PRIFLAG） | PRIMARY | 本端规划 |  |
|  | 确认服务器密钥（加密的）(CIPHERKEYCNFM) | ispkey | 本端规划 |  |
| **ADD APNRDSSVRGRP** | APN名称（APN） | apn-test | 已配置数据中获取 | 配置APN下绑定AAA服务器组。  已通过 **ADD CPAPN**命令配置，可以使用 **LST CPAPN**命令进行查询。 |
|  | Radius Server Group名称（RDSSVRGRPNAME） | isprg | 已配置数据中获取 | 已通过**ADD APNRDSSVRGRP**命令配置，可以使用**LST APNRDSSVRGRP**命令进行查询。 |

## 操作步骤

1. 进入“MML命令行-UEG”窗口。
2. 配置AAA服务器组。

   **ADD RDSSVRGRP**
3. 配置AAA鉴权服务器及计费服务器。
   1. 配置AAA鉴权服务器。

      **ADD RDSSVR**
   2. 配置AAA计费服务器。

      **ADD RDSSVR**
4. 配置APN下绑定AAA服务器组。

   **ADD APNRDSSVRGRP**

## 任务示例

任务描述

激活AAA负荷分担。

脚本

//配置AAA服务器组。

```
ADD RDSSVRGRP: RDSSVRGRPNAME="isprg", MODE=ROUND_ROBIN, SIGOPTACCTMSG=DISABLE;
```

//配置AAA鉴权服务器及计费服务器，VPNinst实例为"vpn\_Gi"。

```
ADD RDSSVR: RDSSVRGRPNAME="isprg", SERVERTYPE=AUTHENTICATION, IPVERSION=IPV4, SERVERIPV4="192.168.7.12", PORT=1812, VPNINSTANCE="vpn_Gi", CIPHERKEY="*****", PRIFLAG=PRIMARY, CIPHERKEYCNFM="*****";
```

```
ADD RDSSVR: RDSSVRGRPNAME="isprg", SERVERTYPE=ACCOUNTING, IPVERSION=IPV4, SERVERIPV4="192.168.7.14", PORT=1813, VPNINSTANCE="vpn_Gi", CIPHERKEY="*****", PRIFLAG=PRIMARY, CIPHERKEYCNFM="*****";
```

//配置APN实例"apn-test"下绑定AAA服务器组。

```
ADD APNRDSSVRGRP:APN="apn-test",RDSSVRGRPNAME="isprg";
```

版权所有 © 华为技术有限公司

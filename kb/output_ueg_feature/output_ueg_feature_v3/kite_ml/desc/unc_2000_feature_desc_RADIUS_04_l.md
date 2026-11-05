# 配置到AAA Server的数据（双平面+OSPF动态路由+BFD组网 ）

* 操作场景
* 必备事项
* 操作步骤
* 验证方法
* 任务示例

## 操作场景

在企业网中，可以通过在网络边缘部署AAA Server（计费/鉴权AAA服务器）进行跨IP鉴权和计费，实现外部办公人员接入。当计费/鉴权AAA服务器位于企业网中，UEG与计费/鉴权AAA服务器之间采用带内组网方式，即到PDN的数据报文和到计费AAA服务器服务器的RADIUS信令报文在同一VPN下。

适用于PGW-C、SMF

## 必备事项

前提条件

* 请仔细阅读IPFD-020601 VRF功能和IPFD-020501 支持OSPF特性概述。
* UEG与网络实体之间的网络环境已经构建完成。

数据

**表1** 整体配置

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| **ADD L3VPNINST** | VPN实例名称 (VRFNAME) | vpn\_pdn | 本端规划 | - |
| ****ADD VPNINSTAF**** | VPN实例名称 (VRFNAME) | vpn\_pdn | 已配置数据中获取 | 已通过**ADD L3VPNINST**命令进行配置，可以使用****LST L3VPNINST****进行查询 |
|  | 地址族类型 (AFTYPE) | ipv4uni | 本端规划 | - |
|  | 实例的标签分配模式 (VRFLABELMODE) | perRoute | 本端规划 | - |
| **ADD CPVPNINST** | VPN实例名（VPNINSTANCE） | vpn\_pdn | 本端规划 | - |
| **ADD LOGICIP** | IP地址类型（IPVERSION） | IPv4 | 本端规划 | 逻辑接口使用的逻辑IP。 |
|  | IPv4地址（LOGICIPV4） | 10.8.20.1  10.8.20.2 | 本端规划 |  |
| **ADD CPLOGICINF** | 逻辑接口名称（NAME） | giif1/0/0  giif1/0/1 | 本端规划 | 配置使用的逻辑接口，其中“giif1/0/0”和“10.8.20.1”用于鉴权AAA服务器，“giif1/0/1”和“10.8.20.2”用于计费AAA服务器。 |
|  | 逻辑接口的IP版本（IPVERSION） | IPV4 | 本端规划 |  |
|  | 逻辑接口的IPv4地址1（IPV4ADDRESS1） | 10.8.20.1  10.8.20.2 | 全网规划 |  |
|  | 逻辑接口的IPv4掩码1（IPV4MASK1） | 255.255.255.255 | 固定取值 |  |
|  | VPN实例名称（VPNINSTANCE） | vpn\_pdn | 已配置数据中获取 | 鉴权/计费AAA服务器所属的VPN实例名。已通过**ADD CPVPNINST**配置，可以使用**LST CPVPNINST**命令进行查询。 |
| **ADD RDSSVRGRP** | Radius Server Group名称（RDSSVRGRPNAME） | isprg | 本端规划 | - |
|  | 模式（MODE） | MASTER\_SLAVE | 本端规划 | - |
|  | 支持可选计费消息（SIGOPTACCTMSG） | DISABLE | 本端规划 | - |
| **ADD CPAPN** | APN名称（APN） | apn1 | 全网规划 | - |
|  | 绑定VPN（HASVPN） | ENABLE | 本端规划 |  |
|  | VPN实例名（VPNINSTANCE） | vpn\_pdn | 已配置数据中获取 | 已通过**ADD CPVPNINST**配置，可以使用**LST CPVPNINST**命令进行查询。 |
|  | 绑定IPv6 VPN（HASVPNIPV6） | DISABLE | 本端规划 | - |
|  | 故障重启业务恢复功能PGW开关（RESTORPGWSWITCH） | INHERIT | 本端规划 | - |
|  | 去活消息携带reactivation-request开关（REACWITHDEL） | DISABLE | 本端规划 | - |
| **ADD APNRDSCLIENTIP** | APN名称（APN） | apn1 | 全网规划 | 已通过**ADD CPAPN**配置，可以使用****LST CPAPN****命令进行查询。 |
|  | 鉴权或计费（AUTHORACCT） | ACCOUNTING  AUTHENTICATION | 全网规划 | - |
|  | 接口名称（INTFNAME） | giif1/0/0  giif1/0/1 | 已配置数据中获取 | 已通过**ADD CPLOGICINF**配置，可以使用****LST CPLOGICINF****命令进行查询。 |
| **ADD APNRDSSVRGRP** | APN名称（APN） | apn1 | 全网规划 | 已通过**ADD CPAPN**配置，可以使用****LST CPAPN****命令进行查询。 |
|  | Radius Server Group名称（RDSSVRGRPNAME） | isprg | 已配置数据中获取 | 鉴权AAA服务器所在的AAA服务器组，已通过**ADD RDSSVRGRP**进行配置。 |

**表2** 鉴权AAA服务器配置

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| **ADD RDSSVR** | Radius Server Group名称（RDSSVRGRPNAME） | isprg | 已配置数据中获取 | 鉴权AAA服务器所在的AAA服务器组，已通过**ADD RDSSVRGRP**进行配置。 |
|  | 服务器类型（SERVERTYPE） | AUTHENTICATION | 全网规划 | - |
|  | 服务器IP版本（IPVERSION） | IPV4 | 全网规划 | 鉴权AAA服务器IP地址、端口号、密钥。 |
|  | IPv4地址（SERVERIPV4） | 10.168.10.1 | 全网规划 |  |
|  | 端口（PORT） | 1812 | 与对端协商 |  |
|  | 服务器密钥（加密的）（CIPHERKEY） | ispchina | 与对端协商 |  |
|  | 主备用类型（PRIFLAG） | PRIMARY | 本端规划 | - |
|  | VPN实例名（VPNINSTANCE） | vpn\_pdn | 已配置数据中获取 | 计费AAA服务器所属的VPN实例名。已通过**ADD CPVPNINST**配置，可以使用**LST CPVPNINST**命令进行查询。 |
|  | 确认服务器密钥（加密的）（CIPHERKEYCNFM） | ispchina | 与对端协商 | - |

**表3** 计费AAA服务器配置

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| **ADD UPLIST4RDS** | UP列表名称（UPLISTNAME） | uplist1 | 本端规划 | - |
|  | UP实例标识（UPINSTANCEID） | up1  up2 | 已配置数据中获取 | 在初始配置时已经通过**ADD PNFPROFILE**命令配置。此处以配置的UP名称为“up1”和“up2”为例。 |
| **ADD RDSSVR** | Radius Server Group名称（RDSSVRGRPNAME） | isprg | 已配置数据中获取 | 计费AAA服务器所在的AAA服务器组，已通过**ADD RDSSVRGRP**进行配置。 |
|  | 服务器类型（SERVERTYPE） | ACCOUNTING | 全网规划 | - |
|  | 服务器IP版本（IPVERSION） | IPV4 | 全网规划 | 计费AAA服务器IP地址、端口号、密钥。 |
|  | IPv4地址（SERVERIPV4） | 10.168.10.1 | 全网规划 |  |
|  | 端口（PORT） | 1813 | 与对端协商 |  |
|  | 服务器密钥（加密的）（CIPHERKEY） | ispchina | 与对端协商 |  |
|  | 主备用类型（PRIFLAG） | PRIMARY | 本端规划 | - |
|  | VPN实例名（VPNINSTANCE） | vpn\_pdn | 已配置数据中获取 | 计费AAA服务器所属的VPN实例名。已通过**ADD CPVPNINST**配置，可以使用**LST CPVPNINST**命令进行查询。 |
|  | 确认服务器密钥（加密的）（CIPHERKEYCNFM） | ispchina | 与对端协商 | - |

## 操作步骤

1. 参考配置动态路由OSPF+BFD组网（IPv4）配置对应的组网。
2. 进入“MML命令行-UEG”窗口。
3. 创建L3VPN实例。

   **ADD L3VPNINST**

   ****ADD VPNINSTAF****
4. 创建VPN实例。

   **ADD CPVPNINST**
5. 配置Gi逻辑接口。

   **ADD LOGICIP**

   **ADD CPLOGICINF**
6. **可选：**配置鉴权或计费AAA服务器使用的PGW-U/UPF列表。

   **ADD UPLIST4RDS**
7. 配置鉴权/计费AAA服务器。
   1. 配置AAA服务器组以及服务器的工作模式。

      **ADD RDSSVRGRP**
   2. 设置主用鉴权AAA服务器的IP地址、目的端口号、所属VPN、密钥。

      **ADD RDSSVR**
   3. **可选：**设置备用鉴权AAA服务器的IP地址、目的端口号、所属VPN、密钥。

      **ADD RDSSVR**
   4. 配置主用计费AAA服务器的IP地址、目的端口号、所属VPN、密钥。

      **ADD RDSSVR**
   5. **可选：**配置备用计费AAA服务器的IP地址、目的端口号、所属VPN、密钥。

      **ADD RDSSVR**

      步骤b-e中，执行该命令多次，可以配置多个计费/鉴权AAA服务器。
   6. 配置APN。

      **ADD CPAPN**
   7. 配置APN下的Client-IP。

      **ADD APNRDSCLIENTIP**
   8. APN实例下绑定RADIUS服务器组。

      **ADD APNRDSSVRGRP**

## 验证方法

具体步骤请参见调测到AAA Server的数据。

## 任务示例

任务描述

UEG与计费/鉴权AAA服务器通过带内组网方式对接时的配置范例，使用OSPF动态路由与计费/鉴权AAA服务器建立起正常的IP连接。要求UEG基于UPF列表选择计费AAA服务器。

脚本

//参考配置动态路由OSPF+BFD组网（IPv4）配置对应的组网。

//创建L3VPN实例。

```
ADD L3VPNINST:VRFNAME="vpn_pdn";
```

```
ADD VPNINSTAF: VRFNAME="vpn_pdn", AFTYPE=ipv4uni, VRFLABELMODE=perRoute;
```

//创建VPN实例。

```
ADD CPVPNINST: VPNINSTANCE ="vpn_pdn";
```

//配置Gi接口：

//1.配置Giif1/0/0接口。

```
ADD LOGICIP: IPVERSION=IPv4, LOGICIPV4="10.8.20.1", VPNINSTNAME="vpn_pdn";
ADD CPLOGICINF:NAME="giif1/0/0",IPVERSION=IPV4,IPV4ADDRESS1="10.8.20.1",IPV4MASK1="255.255.255.255",VPNINSTANCE="vpn_pdn";
```

//2.配置Giif1/0/1接口。

```
ADD LOGICIP: IPVERSION=IPv4, LOGICIPV4="10.8.20.2", VPNINSTNAME="vpn_pdn";
ADD CPLOGICINF:NAME="giif1/0/1",IPVERSION=IPV4,IPV4ADDRESS1="10.8.20.2",IPV4MASK1="255.255.255.255",VPNINSTANCE="vpn_pdn";
```

//配置UPF列表。

```
ADD UPLIST4RDS: UPLISTNAME="uplist1", UPINSTANCEID="up1";
ADD UPLIST4RDS: UPLISTNAME="uplist1", UPINSTANCEID="up2";
```

//配置鉴权/计费AAA服务器。

```
ADD RDSSVRGRP: RDSSVRGRPNAME="isprg", MODE=MASTER_SLAVE, SIGOPTACCTMSG=DISABLE;
```

```
ADD RDSSVR: RDSSVRGRPNAME="isprg", SERVERTYPE=AUTHENTICATION, IPVERSION=IPV4, SERVERIPV4="10.168.10.1", PORT=1812, VPNINSTANCE="vpn_pdn", CIPHERKEY="*****", PRIFLAG=PRIMARY, CIPHERKEYCNFM="*****"，UPLISTNAME="uplist1";
```

```
ADD RDSSVR: RDSSVRGRPNAME="isprg", SERVERTYPE=ACCOUNTING, IPVERSION=IPV4, SERVERIPV4="10.168.10.1", PORT=1813, VPNINSTANCE="vpn_pdn", CIPHERKEY="*****", PRIFLAG=PRIMARY, CIPHERKEYCNFM="*****"，UPLISTNAME="uplist1";
```

```
ADD CPAPN: APN="apn1", HASVPN=ENABLE, VPNINSTANCE="vpn_pdn", HASVPNIPV6=DISABLE, RESTORPGWSWITCH=INHERIT, REACWITHDEL=DISABLE;
```

```
ADD APNRDSCLIENTIP: APN="apn1",AUTHORACCT=AUTHENTICATION,INTFNAME="giif1/0/0";
```

```
ADD APNRDSCLIENTIP: APN="apn1",AUTHORACCT=ACCOUNTING,INTFNAME="giif1/0/1";
```

```
ADD APNRDSSVRGRP: APN="apn1",RDSSVRGRPNAME="isprg";
```

版权所有 © 华为技术有限公司
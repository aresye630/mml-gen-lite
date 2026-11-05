# 配置到AAA Server的数据（带外组网GRE VPN）

- 操作场景
- 必备事项
- 操作步骤
- 验证方法
- 任务示例

## 操作场景

UEG和AAA Server（计费/鉴权AAA服务器）的互通采用带外组网方式，为RADIUS信令报文和数据报文配置不同的出接口。UEG到计费/鉴权AAA服务器采用缺省路由，当有多个计费/鉴权AAA服务器时，可减少路由配置的工作量，并便于管理。为了提高互通的安全性，在UEG和企业网所在网段的防火墙之间建立GRE VPN隧道。隧道绑定的VPN和计费/鉴权AAA服务器绑定的VPN不同。

**说明** 

适用于PGW-C、SMF

## 必备事项

前提条件

- 请仔细阅读IPFD-020601 VRF功能和IPFD-020501 支持OSPF特性概述。
- UEG与网络实体之间的网络环境已经构建完成。

数据

| 类别                             | 参数名称                                      | 取值样例                              | 获取方法     | 说明                                                                                                 |
|:-------------------------------|:------------------------------------------|:----------------------------------|:---------|:---------------------------------------------------------------------------------------------------|
| ADD L3VPNINST                  | VPN实例名称 (VRFNAME)                         | vpn_enterprise vpn_tunnel vpn_aaa | 本端规划     | -                                                                                                  |
| ADD VPNINSTAF                  | VPN实例名称 (VRFNAME)                         | vpn_enterprise vpn_tunnel vpn_aaa | 已配置数据中获取 | 已通过ADD L3VPNINST命令进行配置，可以使用LST L3VPNINST进行查询。                                                      |
| ADD VPNINSTAF                  | 地址族类型 (AFTYPE)                            | ipv4uni                           | 本端规划     | -                                                                                                  |
| ADD VPNINSTAF                  | 路由标识（VRFRD）                               | 200:1                             | 本端规划     | -                                                                                                  |
| ADD VPNINSTAF                  | 实例的标签分配模式 (VRFLABELMODE)                  | perRoute                          | 本端规划     | -                                                                                                  |
| ADD INTERFACE                  | 接口名（IFNAME）                               | LoopBack0                         | 本端规划     | -                                                                                                  |
| ADD IPBINDVPN                  | 接口名（IFNAME）                               | LoopBack0 Tunnel1                 | 已配置数据中获取 | 分别对应GRE隧道的Loopback接口、Tunnel接口名称。已通过ADD INTERFACE命令进行配置，可以使用LST INTERFACE进行查询。                      |
| ADD IPBINDVPN                  | VPN实例名称（VRFNAME）                          | vpn_tunnel vpn_enterprise         | 已配置数据中获取 | 分别对应GRE隧道的Loopback接口、Tunnel接口所使用的VPN实例。 当UEG的产品形态为风筝L时，已通过ADD CPVPNINST配置，可以使用LST CPVPNINST命令进行查询。 |
| ADD IFIPV4ADDRESS              | 接口名（IFNAME）                               | LoopBack0                         | 已配置数据中获取 | 已通过ADD INTERFACE命令进行配置，可以使用LST INTERFACE进行查询。                                                      |
| ADD IFIPV4ADDRESS              | IPv4地址（IFIPADDR）                          | 192.168.100.105 10.10.1.201       | 本端规划     | 分别对应GRE隧道的Loopback接口、Tunnel接口所使用的IPv4地址和地址掩码。                                                      |
| ADD IFIPV4ADDRESS              | IPv4地址掩码（SUBNETMASK）                      | 255.255.255.255 255.255.255.252   | 全网规划     | 分别对应GRE隧道的Loopback接口、Tunnel接口所使用的IPv4地址和地址掩码。                                                      |
| ADD GRETUNNEL                  | 隧道名称（TNLNAME）                             | Tunnel1                           | 本端规划     | -                                                                                                  |
| ADD GRETUNNEL                  | 隧道类型（TNLTYPE）                             | GRE                               | 全网规划     | -                                                                                                  |
| ADD GRETUNNEL                  | IPv4源类型（SRCTYPE）                          | if_name                           | 本端规划     | -                                                                                                  |
| ADD GRETUNNEL                  | 源接口名称（SRCIFNAME）                          | LoopBack0                         | 已配置数据中获取 | 已通过ADD INTERFACE命令进行配置，可以使用LST INTERFACE进行查询。                                                      |
| ADD GRETUNNEL                  | 目的IPv4地址（DSTIPADDR）                       | 192.168.95.100                    | 全网规划     | 该参数值与Firewall B的IP地址取值一致。                                                                          |
| ADD SRROUTE                    | 地址族 (AFTYPE)                              | ipv4unicast                       | 固定取值     | -                                                                                                  |
| ADD SRROUTE                    | 路由前缀 (PREFIX)                             | 10.10.1.202                       | 全网规划     | -                                                                                                  |
| ADD SRROUTE                    | 路由掩码长度 (MASKLENGTH)                       | 30                                | 全网规划     | -                                                                                                  |
| ADD SRROUTE                    | VPN实例名称 (VRFNAME)                         | vpn_enterprise                    | 已配置数据中获取 | 已通过ADD L3VPNINST命令进行配置，可以使用LST L3VPNINST进行查询。                                                      |
| ADD SRROUTE                    | 路由出接口名字 (IFNAME)                          | Tunnel1                           | 已配置数据中获取 | 已通过ADD GRETUNNEL命令进行配置，可以使用LST GRETUNNEL进行查询。                                                      |
| 当UEG的产品形态为风筝L时，ADD CPVPNINST   | VPN实例名（VPNINSTANCE）                       | vpn_aaa vpn_enterprise            | 本端规划     | -                                                                                                  |
| ADD LOGICIP                    | IP地址类型（IPVERSION）                         | IPv4                              | 本端规划     | 逻辑接口使用的逻辑IP。                                                                                       |
| ADD LOGICIP                    | IPv4地址（LOGICIPV4）                         | 10.8.20.1 10.8.20.2               | 本端规划     | 逻辑接口使用的逻辑IP。                                                                                       |
| 当UEG的产品形态为风筝L时， ADD CPLOGICINF | 逻辑接口名称（NAME）                              | giif1/0/0 giif1/0/1               | 本端规划     | 配置使用的逻辑接口，其中“giif1/0/0”和“10.8.20.1”用于鉴权AAA服务器，“giif1/0/1”和“10.8.20.2”用于计费AAA服务器。                   |
| 当UEG的产品形态为风筝L时， ADD CPLOGICINF | 逻辑接口的IP版本（IPVERSION）                      | IPV4                              | 本端规划     | 配置使用的逻辑接口，其中“giif1/0/0”和“10.8.20.1”用于鉴权AAA服务器，“giif1/0/1”和“10.8.20.2”用于计费AAA服务器。                   |
| 当UEG的产品形态为风筝L时， ADD CPLOGICINF | 逻辑接口的IPv4地址1（IPV4ADDRESS1）                | 10.8.20.1 10.8.20.2               | 全网规划     | 配置使用的逻辑接口，其中“giif1/0/0”和“10.8.20.1”用于鉴权AAA服务器，“giif1/0/1”和“10.8.20.2”用于计费AAA服务器。                   |
| 当UEG的产品形态为风筝L时， ADD CPLOGICINF | 逻辑接口的IPv4掩码1（IPV4MASK1）                   | 255.255.255.255                   | 固定取值     | 配置使用的逻辑接口，其中“giif1/0/0”和“10.8.20.1”用于鉴权AAA服务器，“giif1/0/1”和“10.8.20.2”用于计费AAA服务器。                   |
| 当UEG的产品形态为风筝L时， ADD CPLOGICINF | VPN实例名称（VPNINSTANCE）                      | vpn_aaa                           | 已配置数据中获取 | 鉴权AAA服务器所属的VPN实例名。当UEG的产品形态为风筝L时，已通过ADD CPVPNINST配置，可以使用LST CPVPNINST命令进行查询。                       |
| ADD RDSSVRGRP                  | Radius Server Group名称（RDSSVRGRPNAME）      | isprg                             | 本端规划     | -                                                                                                  |
| ADD RDSSVRGRP                  | 模式（MODE）                                  | MASTER_SLAVE                      | 本端规划     | -                                                                                                  |
| ADD RDSSVRGRP                  | 支持可选计费消息（SIGOPTACCTMSG）                   | DISABLE                           | 本端规划     | -                                                                                                  |
| 当UEG的产品形态为风筝L时， ADD CPAPN      | APN名称（APN）                                | apn1                              | 全网规划     | -                                                                                                  |
| 当UEG的产品形态为风筝L时， ADD CPAPN      | 绑定VPN（HASVPN）                             | ENABLE                            | 本端规划     | -                                                                                                  |
| 当UEG的产品形态为风筝L时， ADD CPAPN      | VPN实例名（VPNINSTANCE）                       | vpn_enterprise                    | 已配置数据中获取 | 当UEG的产品形态为风筝L时，已通过ADD CPVPNINST配置，可以使用LST CPVPNINST命令进行查询。                                         |
| 当UEG的产品形态为风筝L时， ADD CPAPN      | 绑定IPv6 VPN（HASVPNIPV6）                    | DISABLE                           | 本端规划     | -                                                                                                  |
| 当UEG的产品形态为风筝L时， ADD CPAPN      | 故障重启业务恢复功能PGW开关（RESTORPGWSWITCH）          | INHERIT                           | 本端规划     | -                                                                                                  |
| 当UEG的产品形态为风筝L时， ADD CPAPN      | 去活消息携带reactivation-request开关（REACWITHDEL） | DISABLE                           | 本端规划     | -                                                                                                  |
| ADD APNRDSCLIENTIP             | APN名称（APN）                                | apn1                              | 已配置数据中获取 | 当UEG的产品形态为风筝L时，已通过ADD CPAPN配置，可以使用LST CPAPN命令进行查询。                                                 |
| ADD APNRDSCLIENTIP             | 鉴权或计费（AUTHORACCT）                         | ACCOUNTING AUTHENTICATION         | 全网规划     | -                                                                                                  |
| ADD APNRDSCLIENTIP             | 接口名称（INTFNAME）                            | giif1/0/0 giif1/0/1               | 已配置数据中获取 | 当UEG的产品形态为风筝L时，已通过ADD CPLOGICINF配置，可以使用LST CPLOGICINF命令进行查询。                                       |
| ADD APNRDSSVRGRP               | APN名称（APN）                                | apn1                              | 已配置数据中获取 | 当UEG的产品形态为风筝L时，已通过ADD CPLOGICINF配置，可以使用LST CPLOGICINF命令进行查询。                                       |
| ADD APNRDSSVRGRP               | Radius Server Group名称（RDSSVRGRPNAME）      | isprg                             | 已配置数据中获取 | 鉴权AAA服务器所在的AAA服务器组，已通过ADD RDSSVRGRP进行配置。                                                           |

| 类别         | 参数名称                                 | 取值样例           | 获取方法     | 说明                                                                           |
|:-----------|:-------------------------------------|:---------------|:---------|:-----------------------------------------------------------------------------|
| ADD RDSSVR | Radius Server Group名称（RDSSVRGRPNAME） | isprg          | 已配置数据中获取 | 鉴权AAA服务器所在的AAA服务器组，已通过ADD RDSSVRGRP进行配置。                                     |
| ADD RDSSVR | 服务器类型（SERVERTYPE）                    | AUTHENTICATION | 全网规划     | -                                                                            |
| ADD RDSSVR | 服务器IP版本（IPVERSION）                   | IPV4           | 全网规划     | 鉴权AAA服务器IP地址、端口号、密钥。                                                         |
| ADD RDSSVR | IPv4地址（SERVERIPV4）                   | 10.168.10.1    | 全网规划     | 鉴权AAA服务器IP地址、端口号、密钥。                                                         |
| ADD RDSSVR | 端口（PORT）                             | 1812           | 与对端协商    | 鉴权AAA服务器IP地址、端口号、密钥。                                                         |
| ADD RDSSVR | 服务器密钥（加密的）（CIPHERKEY）                | ispchina       | 与对端协商    | 鉴权AAA服务器IP地址、端口号、密钥。                                                         |
| ADD RDSSVR | 主备用类型（PRIFLAG）                       | PRIMARY        | 本端规划     | -                                                                            |
| ADD RDSSVR | VPN实例名（VPNINSTANCE）                  | vpn_aaa        | 已配置数据中获取 | 计费AAA服务器所属的VPN实例名。当UEG的产品形态为风筝L时，已通过ADD CPVPNINST配置，可以使用LST CPVPNINST命令进行查询。 |
| ADD RDSSVR | 确认服务器密钥（加密的）（CIPHERKEYCNFM）          | ispchina       | 与对端协商    | -                                                                            |

| 类别         | 参数名称                                 | 取值样例        | 获取方法     | 说明                                                                           |
|:-----------|:-------------------------------------|:------------|:---------|:-----------------------------------------------------------------------------|
| ADD RDSSVR | Radius Server Group名称（RDSSVRGRPNAME） | isprg       | 已配置数据中获取 | 计费AAA服务器所在的AAA服务器组，已通过ADD RDSSVRGRP进行配置。                                     |
| ADD RDSSVR | 服务器类型（SERVERTYPE）                    | ACCOUNTING  | 全网规划     | -                                                                            |
| ADD RDSSVR | 服务器IP版本（IPVERSION）                   | IPV4        | 全网规划     | 计费AAA服务器IP地址、端口号、密钥。                                                         |
| ADD RDSSVR | IPv4地址（SERVERIPV4）                   | 10.168.10.1 | 全网规划     | 计费AAA服务器IP地址、端口号、密钥。                                                         |
| ADD RDSSVR | 端口（PORT）                             | 1813        | 与对端协商    | 计费AAA服务器IP地址、端口号、密钥。                                                         |
| ADD RDSSVR | 服务器密钥（加密的）（CIPHERKEY）                | ispchina    | 与对端协商    | 计费AAA服务器IP地址、端口号、密钥。                                                         |
| ADD RDSSVR | 主备用类型（PRIFLAG）                       | PRIMARY     | 本端规划     | -                                                                            |
| ADD RDSSVR | VPN实例名（VPNINSTANCE）                  | vpn_aaa     | 已配置数据中获取 | 计费AAA服务器所属的VPN实例名。当UEG的产品形态为风筝L时，已通过ADD CPVPNINST配置，可以使用LST CPVPNINST命令进行查询。 |
| ADD RDSSVR | 确认服务器密钥（加密的）（CIPHERKEYCNFM）          | ispchina    | 与对端协商    | -                                                                            |

## 操作步骤

1. 参考配置静态路由+BFD组网（IPv4）配置对应的组网。
2. 进入“MML命令行-UEG”窗口。
3. 创建L3VPN实例。

   **ADD L3VPNINST**

   ****ADD VPNINSTAF****
4. 创建GRE隧道。
   1. 创建Loopback接口。

      ****ADD INTERFACE****
   2. 配置Loopback接口的IP地址和掩码，并将Loopback接口绑定VPN实例。

      ****ADD IPBINDVPN****

      ****ADD IFIPV4ADDRESS****
   3. 设置Tunnel接口报文的封装模式为GRE，设置Tunnel接口的源端地址以及目的端地址，其中指定隧道接口的Loopback接口作为源地址。

      ****ADD GRETUNNEL****
   4. 配置Tunnel接口的IP地址和掩码，并将Tunnel接口绑定VPN实例。

      ****ADD IPBINDVPN****

      ****ADD IFIPV4ADDRESS****
   5. 配置静态路由。

      ****ADD SRROUTE****

   **说明** 

   如果需要一同配置IPv6的GRE隧道，则步骤b、d均需要先使用****SET IFIPV6ENABLE****命令开启IPv6使能，再使用****ADD IFIPV6ADDRESS****命令配置IPv6地址，步骤e需要使用****ADD SRROUTE6****命令配置IPv6静态路由。
5. 创建VPN实例。

   当UEG的产品形态为风筝L时，**ADD CPVPNINST**
6. 配置Gi逻辑接口。

   **ADD LOGICIP**

   当UEG的产品形态为风筝S时，当UEG的产品形态为风筝L时，**ADD CPLOGICINF**
7. **可选：**配置鉴权或计费AAA服务器使用的PGW-U/UPF列表。

   **ADD UPLIST4RDS**
8. 配置鉴权/计费AAA服务器。
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

      **说明** 

      步骤b-e中，执行该命令多次，可以配置多个计费/鉴权AAA服务器。
   6. 配置APN。

      当UEG的产品形态为风筝S时，当UEG的产品形态为风筝L时，**ADD CPAPN**
   7. 配置APN下的Client-IP。

      **ADD APNRDSCLIENTIP**
   8. APN实例下绑定RADIUS服务器组。

      **ADD APNRDSSVRGRP**

## 验证方法

具体步骤请参见调测到AAA Server的数据。

## 任务示例

任务描述

本实例中使用的是UEG与计费/鉴权AAA服务器通过带外GRE VPN组网方式对接时的配置范例。操作员在UEG上进行数据配置实现以下要求：

- UEG使用缺省路由与计费/鉴权AAA服务器建立起正常的IP连接。
- UEG使用缺省路由与PDN之间通过GRE VPN隧道建立起正常的IP连接。

脚本

//参考配置静态路由+BFD组网（IPv4）配置对应的组网。

//配置原始数据报文的VPN和经GRE隧道封装后报文的L3VPN。

```
ADD L3VPNINST: VRFNAME ="vpn_enterprise";
```

```
ADD VPNINSTAF: VRFNAME ="vpn_enterprise",AFTYPE=ipv4uni;
```

```
ADD L3VPNINST: VRFNAME ="vpn_tunnel";
```

```
ADD VPNINSTAF: VRFNAME ="vpn_tunnel",AFTYPE=ipv4uni;
```

//创建GRE隧道：

//1. 配置Loopback接口，绑定的VPN实例名称为“vpn\_tunnel”。

```
ADD INTERFACE:IFNAME="LoopBack0";
```

```
ADD IPBINDVPN:IFNAME="Loopback0",VRFNAME="vpn_tunnel";
```

```
ADD IFIPV4ADDRESS:IFNAME="LoopBack0",IFIPADDR="192.168.100.105",SUBNETMASK="255.255.255.255";
```

//2.配置Tunnel接口，绑定的VPN实例名称为“vpn\_enterprise”。

```
ADD GRETUNNEL:TNLNAME= "Tunnel1",TNLTYPE=gre,SRCTYPE=if_name,SRCIFNAME="Loopback0",DSTIPADDR="192.168.95.100";
```

**说明** 

对端Firewall B的源端与目的端的配置应与本端配置互为镜像，即Firewall B上配置的源端为192.168.95.100，目的端为192.168.100.105。

```
ADD IPBINDVPN:IFNAME="Tunnel1",VRFNAME="vpn_enterprise";
```

```
ADD IFIPV4ADDRESS:IFNAME="Tunnel1",IFIPADDR="10.10.1.201",SUBNETMASK="255.255.255.252";
```

```
ADD SRROUTE:AFTYPE=ipv4unicast,PREFIX="10.10.1.202",MASKLENGTH=30,VRFNAME="vpn_enterprise",IFNAME="Tunnel1";
```

//配置到计费/鉴权AAA服务器的数据：

//1.创建RADIUS信令报文所属的L3VPN实例。

```
ADD L3VPNINST: VRFNAME ="vpn_aaa";
```

```
ADD VPNINSTAF:VRFNAME="vpn_aaa",AFTYPE=ipv4uni,VRFRD="200:1";
```

//2.创建VPN实例。

当UEG的产品形态为风筝L时，

```
ADD CPVPNINST:VPNINSTANCE="vpn_enterprise";
```

```
ADD CPVPNINST:VPNINSTANCE="vpn_aaa";
```

//配置Gi接口：

//1.配置Giif1/0/0接口。

当UEG的产品形态为风筝L时，

```
ADD LOGICIP: IPVERSION=IPv4, LOGICIPV4="10.8.20.1", VPNINSTNAME="vpn_pdn";
ADD CPLOGICINF:NAME="giif1/0/0",IPVERSION=IPV4,IPV4ADDRESS1="10.8.20.1",IPV4MASK1="255.255.255.255",VPNINSTANCE="vpn_aaa";
```

//2.配置Giif1/0/1接口。

当UEG的产品形态为风筝L时，

```
ADD LOGICIP: IPVERSION=IPv4, LOGICIPV4="10.8.20.2", VPNINSTNAME="vpn_pdn";
ADD CPLOGICINF:NAME="giif1/0/1",IPVERSION=IPV4,IPV4ADDRESS1="10.8.20.2",IPV4MASK1="255.255.255.255",VPNINSTANCE="vpn_aaa";
```

//配置鉴权/计费AAA服务器。

```
ADD RDSSVRGRP: RDSSVRGRPNAME="isprg";
```

```
ADD RDSSVR: RDSSVRGRPNAME="isprg",SERVERTYPE=AUTHENTICATION,IPVERSION=IPV4,SERVERIPV4="10.168.10.1",PORT=1812,VPNINSTANCE="vpn_aaa",CIPHERKEY="*****",CIPHERKEYCNFM="*****";
```

```
ADD RDSSVR: RDSSVRGRPNAME="isprg",SERVERTYPE=ACCOUNTING,IPVERSION=IPV4,SERVERIPV4="10.168.10.1",PORT=1813,VPNINSTANCE="vpn_aaa",CIPHERKEY="*****",CIPHERKEYCNFM="*****";
```

当UEG的产品形态为风筝L时，

```
ADD CPAPN: APN="apn1",HASVPN=ENABLE,VPNINSTANCE="vpn_enterprise";
```

```
ADD APNRDSCLIENTIP:: APN="apn1",AUTHORACCT=AUTHENTICATION,INTFNAME="giif1/0/0";
```

```
ADD APNRDSCLIENTIP:: APN="apn1",AUTHORACCT=ACCOUNTING,INTFNAME="giif1/0/1";
```

```
ADD APNRDSSVRGRP: APN="apn1",RDSSVRGRPNAME="isprg";
```
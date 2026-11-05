# 配置到AAA Server的数据（IPSec隧道）

* 操作场景
* 必备事项
* 操作步骤
* 验证方法
* 任务示例

## 操作场景

当AAA Server（计费/鉴权AAA服务器）位于Internet中，UEG与计费/鉴权AAA服务器之间采用带外组网方式，建立IPSec隧道。

适用于PGW-C、SMF

## 必备事项

前提条件

UEG与网络实体之间的网络环境已经构建完成。

数据

**表1** 整体配置

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| **ADD L3VPNINST** | VPN实例名称 (VRFNAME) | vpn\_pdn  vpn\_aaa | 本端规划 | - |
| ****ADD VPNINSTAF**** | VPN实例名称 (VRFNAME) | vpn\_pdn  vpn\_aaa | 已配置数据中获取 | 已通过**ADD L3VPNINST**命令进行配置，可以使用****LST L3VPNINST****进行查询 |
|  | 地址族类型 (AFTYPE) | ipv4uni | 本端规划 | - |
|  | 实例的标签分配模式 (VRFLABELMODE) | perRoute | 本端规划 | - |
| ****ADD INTERFACE**** | 接口名（IFNAME） | Tunnel1 | 本端规划 | - |
|  | 管理状态（IFADMINSTATUS） | up | 本端规划 |  |
| ****ADD IFIPV4ADDRESS**** | 接口名（IFNAME） | Tunnel1 | 已配置数据中获取 | 已通过****ADD INTERFACE****命令进行配置，可以使用**LST INTERFACE**进行查询。 |
|  | IPv4地址（IFIPADDR） | 10.1.1.1 | 本端规划 | 对应IPsec隧道的Tunnel接口所使用的IPv4地址和地址掩码。 |
|  | IPv4地址掩码（SUBNETMASK） | 255.255.255.240 | 全网规划 |  |
| ****ADD IPBINDVPN**** | 接口名（IFNAME） | Tunnel1 | 已配置数据中获取 | 对应IPsec隧道的Tunnel接口名称。已通过****ADD INTERFACE****命令进行配置，可以使用****LST INTERFACE****进行查询。 |
|  | VPN实例名称（VRFNAME） | vpn\_aaa | 已配置数据中获取 | 对应IPsec隧道所使用的VPN实例。已通过**ADD L3VPNINST**命令进行配置，可以使用****LST L3VPNINST****进行查询 |
| ****ADD SRROUTE**** | 地址族 (AFTYPE) | ipv4unicast | 固定取值 | - |
|  | 路由前缀 (PREFIX) | 10.1.128.23 | 全网规划 |  |
|  | 路由掩码长度 (MASKLENGTH) | 32 | 全网规划 |  |
|  | VPN实例名称 (VRFNAME) | vpn\_aaa | 已配置数据中获取 | 已通过**ADD L3VPNINST**命令进行配置，可以使用**LST L3VPNINST**进行查询。 |
|  | 路由出接口名字 (IFNAME) | Tunnel1 | 已配置数据中获取 | 已通过****ADD INTERFACE****命令进行配置，可以使用**LST INTERFACE**进行查询。 |
| **ADD ACLGROUP** | ACL规则组标识（ACLNAME） | 3101 | 本端规划 | - |
| **ADD ACLRULEADV4** | ACL规则组标识（ACLNAME） | 3101 | 已配置数据中获取 | 已通过**ADD ACLGROUP**命令进行配置，可以使用**LST ACLGROUP**进行查询。 |
|  | 规则名称（ACLRULENAME） | rule\_10 | 本端规划 | - |
|  | 规则行为（ACLACTION） | Permit | 本端规划 |  |
|  | 协议类型值（ACLPROTOCOL） | 17 | 与对端协商 |  |
|  | 源IP地址（ACLSOURCEIP） | 10.1.1.1 | 全网规划 |  |
|  | 目的IP地址（ACLDESTIP） | 10.1.1.2 | 全网规划 | IPSec隧道的目的IP地址，为IPSec隧道终结端的设备IP地址。 |
| **ADD IPSECPROPOSAL** | Proposal名称（PROPOSALNAME） | proposal\_propo1 | 本端规划 | 要求与对端的加密算法配置一致。 |
|  | IPsec安全协议（IPSECPROTOCOL） | esp | 本端规划 |  |
|  | ESP认证算法（ESPAUTHALGO） | sha2\_256 | 与对端协商 |  |
|  | ESP加密算法（ESPENCRYPTALGO） | aes\_256 | 与对端协商 |  |
|  | 封装模式（ENCAPMODE） | transport | 与对端协商 |  |
| **ADD IPSECINTFCFG** | 接口名称 (INTERFACENAME) | Tunnel1 | 已配置数据中获取 | 已通过****ADD INTERFACE****命令进行配置，可以使用****LST INTERFACE****进行查询。 |
|  | Tunnel口协议类型 (TNLTYPE) | IPSEC | 固定取值 | - |
| 当UEG的产品形态为风筝L时，**ADD CPVPNINST** | VPN实例名（VPNINSTANCE） | vpn\_pdn  vpn\_aaa | 本端规划 | - |
| **ADD LOGICIP** | IP地址类型（IPVERSION） | IPv4 | 本端规划 | 逻辑接口使用的逻辑IP。 |
|  | IPv4地址（LOGICIPV4） | 192.168.80.90 | 本端规划 |  |
| 当UEG的产品形态为风筝L时，**ADD CPVPNINST** | 逻辑接口名称（NAME） | giif1/0/0 | 本端规划 | 配置使用的逻辑接口，其中“giif1/0/0”和“10.8.20.1”用于鉴权AAA服务器，“giif1/0/1”和“10.8.20.2”用于计费AAA服务器。 |
|  | 逻辑接口的IP版本（IPVERSION） | IPV4 | 本端规划 |  |
|  | 逻辑接口的IPv4地址1（IPV4ADDRESS1） | 192.168.80.90 | 全网规划 |  |
|  | 逻辑接口的IPv4掩码1（IPV4MASK1） | 255.255.255.255 | 固定取值 |  |
|  | VPN实例名称（VPNINSTANCE） | vpn\_aaa | 已配置数据中获取 | 鉴权/计费AAA服务器所属的VPN实例名。  当UEG的产品形态为风筝L时，已通过**ADD CPVPNINST**配置，可以使用**LST CPVPNINST**命令进行查询。 |
| **ADD RDSSVRGRP** | Radius Server Group名称（RDSSVRGRPNAME） | isprg | 本端规划 | - |
|  | 模式（MODE） | MASTER\_SLAVE | 本端规划 | - |
|  | 支持可选计费消息（SIGOPTACCTMSG） | DISABLE | 本端规划 | - |
| 当UEG的产品形态为风筝L时，  **ADD CPAPN** | APN名称（APN） | apn1 | 全网规划 | - |
|  | 绑定VPN（HASVPN） | ENABLE | 本端规划 |  |
|  | VPN实例名（VPNINSTANCE） | vpn\_pdn | 已配置数据中获取 | 当UEG的产品形态为风筝L时，已通过**ADD CPVPNINST**配置，可以使用**LST CPVPNINST**命令进行查询。 |
|  | 绑定IPv6 VPN（HASVPNIPV6） | DISABLE | 本端规划 | - |
|  | 故障重启业务恢复功能PGW开关（RESTORPGWSWITCH） | INHERIT | 本端规划 | - |
|  | 去活消息携带reactivation-request开关（REACWITHDEL） | DISABLE | 本端规划 | - |
| **ADD APNRDSCLIENTIP** | APN名称（APN） | apn1 | 全网规划 | 当UEG的产品形态为风筝L时，已通过**ADD CPVPNINST**配置，可以使用**LST CPVPNINST**命令进行查询。 |
|  | 鉴权或计费（AUTHORACCT） | ACCOUNTING  AUTHENTICATION | 全网规划 | - |
|  | 接口名称（INTFNAME） | giif1/0/0 | 已配置数据中获取 | 当UEG的产品形态为风筝L时，已通过**ADD CPLOGICINF**配置，可以使用****LST CPLOGICINF****命令进行查询。 |
| **ADD APNRDSSVRGRP** | APN名称（APN） | apn1 | 全网规划 | 当UEG的产品形态为风筝L时，已通过**ADD CPAPN**配置，可以使用****LST CPAPN****命令进行查询。 |
|  | Radius Server Group名称（RDSSVRGRPNAME） | isprg | 已配置数据中获取 | 鉴权AAA服务器所在的AAA服务器组，已通过**ADD RDSSVRGRP**进行配置。 |

**表2** 鉴权AAA服务器配置

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| **ADD RDSSVR** | Radius Server Group名称（RDSSVRGRPNAME） | isprg | 已配置数据中获取 | 鉴权AAA服务器所在的AAA服务器组，已通过**ADD RDSSVRGRP**进行配置。 |
|  | 服务器类型（SERVERTYPE） | AUTHENTICATION | 全网规划 | - |
|  | 服务器IP版本（IPVERSION） | IPV4 | 全网规划 | 鉴权AAA服务器IP地址、端口号、密钥。 |
|  | IPv4地址（SERVERIPV4） | 10.1.128.23 | 全网规划 |  |
|  | 端口（PORT） | 1812 | 与对端协商 |  |
|  | 服务器密钥（加密的）（CIPHERKEY） | ispchina | 与对端协商 |  |
|  | 主备用类型（PRIFLAG） | PRIMARY | 本端规划 | - |
|  | VPN实例名（VPNINSTANCE） | vpn\_aaa | 已配置数据中获取 | 计费AAA服务器所属的VPN实例名。当UEG的产品形态为风筝L时，已通过**ADD CPVPNINST**配置，可以使用**LST CPVPNINST**命令进行查询。 |
|  | 确认服务器密钥（加密的）（CIPHERKEYCNFM） | ispchina | 与对端协商 | - |

**表3** 计费AAA服务器配置

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| **ADD RDSSVR** | Radius Server Group名称（RDSSVRGRPNAME） | isprg | 已配置数据中获取 | 计费AAA服务器所在的AAA服务器组，已通过**ADD RDSSVRGRP**进行配置。 |
|  | 服务器类型（SERVERTYPE） | ACCOUNTING | 全网规划 | - |
|  | 服务器IP版本（IPVERSION） | IPV4 | 全网规划 | 计费AAA服务器IP地址、端口号、密钥。 |
|  | IPv4地址（SERVERIPV4） | 10.1.128.23 | 全网规划 |  |
|  | 端口（PORT） | 1813 | 与对端协商 |  |
|  | 服务器密钥（加密的）（CIPHERKEY） | ispchina | 与对端协商 |  |
|  | 主备用类型（PRIFLAG） | PRIMARY | 本端规划 | - |
|  | VPN实例名（VPNINSTANCE） | vpn\_aaa | 已配置数据中获取 | 计费AAA服务器所属的VPN实例名。当UEG的产品形态为风筝L时，已通过**ADD CPVPNINST**配置，可以使用**LST CPVPNINST**命令进行查询。 |
|  | 确认服务器密钥（加密的）（CIPHERKEYCNFM） | ispchina | 与对端协商 | - |

## 操作步骤

1. 参考配置静态路由+BFD组网（IPv4）配置对应的组网。
2. 进入“MML命令行-UEG”窗口。
3. 创建L3VPN实例。

   **ADD L3VPNINST**

   ****ADD VPNINSTAF****
4. 配置IPsec的Tunnel接口。

   ****ADD INTERFACE****

   ****ADD IFIPV4ADDRESS****

   ****ADD IPBINDVPN****
5. 配置静态路由。

   ****ADD SRROUTE****
6. 配置安全策略为IKE协商方式时的IPSec数据。
   1. 配置数据流的访问控制规则。

      **ADD ACLGROUP**

      **ADD ACLRULEADV4**
   2. 配置IPsec安全提议。

      **ADD IPSECPROPOSAL**
   3. 在Tunnel接口上应用安全策略。

      **ADD IPSECINTFCFG**
7. 创建VPN实例。

   当UEG的产品形态为风筝L时，**ADD CPVPNINST**
8. 配置Gi逻辑接口。

   **ADD LOGICIP**

   当UEG的产品形态为风筝L时，**ADD CPLOGICINF**
9. **可选：**配置鉴权或计费AAA服务器使用的PGW-U/UPF列表。

   **ADD UPLIST4RDS**
10. 配置鉴权/计费AAA服务器。
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

       当UEG的产品形态为风筝L时，**ADD CPAPN**
    7. 配置APN下的Client-IP。

       **ADD APNRDSCLIENTIP**
    8. APN实例下绑定RADIUS服务器组。

       **ADD APNRDSSVRGRP**

## 验证方法

具体步骤请参见调测到AAA Server的数据。

## 任务示例

任务描述

本实例是UEG与计费/鉴权AAA服务器通过带外组网方式对接，并在建立IPSec隧道时的配置范例。操作员在UEG上进行数据配置实现以下要求：

* UEG使用缺省路由与计费/鉴权AAA服务器建立起正常的IP连接。
* 在UEG与计费/鉴权AAA服务器之间建立IPSec隧道，提高传输通道的安全性。

脚本

//参考配置静态路由+BFD组网（IPv4）配置对应的组网。

//创建L3VPN实例。

//1. 数据报文所属的L3VPN实例。

```
ADD L3VPNINST: VRFNAME ="vpn_pdn";
```

```
ADD VPNINSTAF: VRFNAME ="vpn_pdn",AFTYPE=ipv4uni;
```

//2.RADIUS信令报文所属的L3VPN实例。

```
ADD L3VPNINST: VRFNAME ="vpn_aaa";
```

```
ADD VPNINSTAF: VRFNAME="vpn_aaa", AFTYPE=ipv4uni;
```

//配置Tunnel接口。

```
ADD INTERFACE: IFNAME="Tunnel1",IFADMINSTATUS=up;
```

```
ADD IFIPV4ADDRESS: IFNAME="Tunnel1",IFIPADDR="10.1.1.1",SUBNETMASK="255.255.255.240";
```

```
ADD IPBINDVPN: IFNAME="Tunnel1",VRFNAME="vpn_aaa";
```

//配置静态路由。

```
ADD SRROUTE:AFTYPE=ipv4unicast,PREFIX="10.1.128.23",MASKLENGTH=32,VRFNAME="vpn_aaa",DESTVRFNAME="vpn_aaa",IFNAME="Tunnel1";
```

//配置IPsec数据：

//1.配置要保护的数据流。

```
ADD ACLGROUP: ACLNAME="3101";
```

```
ADD ACLRULEADV4:ACLNAME="3101",ACLRULENAME="rule_10",ACLACTION=Permit,ACLSOURCEIP="10.1.1.1",ACLSRCWILD="0.0.0.0",ACLPROTOCOL=17,ACLDESTIP="10.1.1.2";
```

//2.配置IPSec安全提议。

```
ADD IPSECPROPOSAL:PROPOSALNAME="proposal_propo1",IPSECPROTOCOL=esp,ESPAUTHALGO=sha2_256,ESPENCRYPTALGO=aes_256,ENCAPMODE=transport;
```

//3.在Tunnel接口上应用安全策略。

```
ADD IPSECINTFCFG:INTERFACENAME="Tunnel1",TNLTYPE=IPSEC;
```

//创建VPN实例。

当UEG的产品形态为风筝L时，

```
ADD CPVPNINST: VPNINSTANCE ="vpn_pdn";
ADD CPVPNINST:VPNINSTANCE="vpn_aaa";
```

//配置Gi逻辑接口。

当UEG的产品形态为风筝L时，

```
ADD LOGICIP: IPVERSION=IPv4, LOGICIPV4="10.8.20.1";
ADD CPLOGICINF:NAME="giif1/0/0",IPVERSION=IPV4,IPV4ADDRESS1="10.8.20.1",IPV4MASK1="255.255.255.255",VPNINSTANCE="vpn_aaa";
```

//配置鉴权/计费AAA服务器。

```
ADD RDSSVRGRP: RDSSVRGRPNAME="isprg";
```

```
ADD RDSSVR: RDSSVRGRPNAME="isprg",SERVERTYPE=AUTHENTICATION,IPVERSION=IPV4,SERVERIPV4="10.1.128.23",PORT=1812,VPNINSTANCE="vpn_aaa",CIPHERKEY="*****",CIPHERKEYCNFM="*****";
```

```
ADD RDSSVR: RDSSVRGRPNAME="isprg",SERVERTYPE=ACCOUNTING,IPVERSION=IPV4,SERVERIPV4="10.1.128.23",PORT=1813,VPNINSTANCE="vpn_aaa",CIPHERKEY="*****",CIPHERKEYCNFM="*****";
```

```
: APN="apn1",HASVPN=ENABLE,VPNINSTANCE="vpn_pdn";
```

当UEG的产品形态为风筝L时，

```
ADD CPAPN: APN="apn1",HASVPN=ENABLE,VPNINSTANCE="vpn_pdn";
```

```
ADD APNRDSCLIENTIP: APN="apn1",AUTHORACCT=AUTHENTICATION,INTFNAME="giif1/0/0";
```

```
ADD APNRDSCLIENTIP: APN="apn1",AUTHORACCT=ACCOUNTING,INTFNAME="giif1/0/0";
```

```
ADD APNRDSSVRGRP: APN="apn1",RDSSVRGRPNAME="isprg";
```

版权所有 © 华为技术有限公司
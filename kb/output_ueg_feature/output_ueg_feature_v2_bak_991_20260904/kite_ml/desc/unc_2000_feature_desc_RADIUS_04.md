# 配置到AAA Server的数据（双平面+OSPF动态路由+BFD组网 ）

- 操作场景
- 必备事项
- 操作步骤
- 验证方法
- 任务示例

## 操作场景

在企业网中，可以通过在网络边缘部署AAA Server（计费/鉴权AAA服务器）进行跨IP鉴权和计费，实现外部办公人员接入。当计费/鉴权AAA服务器位于企业网中，UEG与计费/鉴权AAA服务器之间采用带内组网方式，即到PDN的数据报文和到计费AAA服务器服务器的RADIUS信令报文在同一VPN下。

**说明** 

适用于PGW-C、SMF

## 必备事项

前提条件

- 请仔细阅读IPFD-020601 VRF功能和IPFD-020501 支持OSPF特性概述。
- UEG与网络实体之间的网络环境已经构建完成。

数据

| 类别                            | 参数名称                                      | 取值样例                      | 获取方法     | 说明                                                                               |
|:------------------------------|:------------------------------------------|:--------------------------|:---------|:---------------------------------------------------------------------------------|
| ADD L3VPNINST                 | VPN实例名称 (VRFNAME)                         | vpn_pdn                   | 本端规划     | -                                                                                |
| ADD VPNINSTAF                 | VPN实例名称 (VRFNAME)                         | vpn_pdn                   | 已配置数据中获取 | 已通过ADD L3VPNINST命令进行配置，可以使用LST L3VPNINST进行查询                                     |
| ADD VPNINSTAF                 | 地址族类型 (AFTYPE)                            | ipv4uni                   | 本端规划     | -                                                                                |
| ADD VPNINSTAF                 | 实例的标签分配模式 (VRFLABELMODE)                  | perRoute                  | 本端规划     | -                                                                                |
| 当UEG的产品形态为风筝L时，ADD CPVPNINST  | VPN实例名（VPNINSTANCE）                       | vpn_pdn                   | 本端规划     | -                                                                                |
| ADD LOGICIP                   | IP地址类型（IPVERSION）                         | IPv4                      | 本端规划     | 逻辑接口使用的逻辑IP。                                                                     |
| ADD LOGICIP                   | IPv4地址（LOGICIPV4）                         | 10.8.20.1 10.8.20.2       | 本端规划     | 逻辑接口使用的逻辑IP。                                                                     |
| 当UEG的产品形态为风筝L时，ADD CPLOGICINF | 逻辑接口名称（NAME）                              | giif1/0/0 giif1/0/1       | 本端规划     | 配置使用的逻辑接口，其中“giif1/0/0”和“10.8.20.1”用于鉴权AAA服务器，“giif1/0/1”和“10.8.20.2”用于计费AAA服务器。 |
| 当UEG的产品形态为风筝L时，ADD CPLOGICINF | 逻辑接口的IP版本（IPVERSION）                      | IPV4                      | 本端规划     | 配置使用的逻辑接口，其中“giif1/0/0”和“10.8.20.1”用于鉴权AAA服务器，“giif1/0/1”和“10.8.20.2”用于计费AAA服务器。 |
| 当UEG的产品形态为风筝L时，ADD CPLOGICINF | 逻辑接口的IPv4地址1（IPV4ADDRESS1）                | 10.8.20.1 10.8.20.2       | 全网规划     | 配置使用的逻辑接口，其中“giif1/0/0”和“10.8.20.1”用于鉴权AAA服务器，“giif1/0/1”和“10.8.20.2”用于计费AAA服务器。 |
| 当UEG的产品形态为风筝L时，ADD CPLOGICINF | 逻辑接口的IPv4掩码1（IPV4MASK1）                   | 255.255.255.255           | 固定取值     | 配置使用的逻辑接口，其中“giif1/0/0”和“10.8.20.1”用于鉴权AAA服务器，“giif1/0/1”和“10.8.20.2”用于计费AAA服务器。 |
| 当UEG的产品形态为风筝L时，ADD CPLOGICINF | VPN实例名称（VPNINSTANCE）                      | vpn_pdn                   | 已配置数据中获取 | 鉴权/计费AAA服务器所属的VPN实例名。当UEG的产品形态为风筝L时，已通过ADD CPVPNINST配置，可以使用LST CPVPNINST命令进行查询。  |
| ADD RDSSVRGRP                 | Radius Server Group名称（RDSSVRGRPNAME）      | isprg                     | 本端规划     | -                                                                                |
| ADD RDSSVRGRP                 | 模式（MODE）                                  | MASTER_SLAVE              | 本端规划     | -                                                                                |
| ADD RDSSVRGRP                 | 支持可选计费消息（SIGOPTACCTMSG）                   | DISABLE                   | 本端规划     | -                                                                                |
| 当UEG的产品形态为风筝L时，ADD CPAPN      | APN名称（APN）                                | apn1                      | 全网规划     | -                                                                                |
| 当UEG的产品形态为风筝L时，ADD CPAPN      | 绑定VPN（HASVPN）                             | ENABLE                    | 本端规划     | -                                                                                |
| 当UEG的产品形态为风筝L时，ADD CPAPN      | VPN实例名（VPNINSTANCE）                       | vpn_pdn                   | 已配置数据中获取 | 当UEG的产品形态为风筝L时，已通过ADD CPVPNINST配置，可以使用LST CPVPNINST命令进行查询。                       |
| 当UEG的产品形态为风筝L时，ADD CPAPN      | 绑定IPv6 VPN（HASVPNIPV6）                    | DISABLE                   | 本端规划     | -                                                                                |
| 当UEG的产品形态为风筝L时，ADD CPAPN      | 故障重启业务恢复功能PGW开关（RESTORPGWSWITCH）          | INHERIT                   | 本端规划     | -                                                                                |
| 当UEG的产品形态为风筝L时，ADD CPAPN      | 去活消息携带reactivation-request开关（REACWITHDEL） | DISABLE                   | 本端规划     | -                                                                                |
| ADD APNRDSCLIENTIP            | APN名称（APN）                                | apn1                      | 全网规划     | 当UEG的产品形态为风筝L时，已通过ADD CPAPN配置，可以使用LST CPAPN命令进行查询。                               |
| ADD APNRDSCLIENTIP            | 鉴权或计费（AUTHORACCT）                         | ACCOUNTING AUTHENTICATION | 全网规划     | -                                                                                |
| ADD APNRDSCLIENTIP            | 接口名称（INTFNAME）                            | giif1/0/0 giif1/0/1       | 已配置数据中获取 | 当UEG的产品形态为风筝L时，已通过ADD CPLOGICINF配置，可以使用LST CPLOGICINF命令进行查询。                     |
| ADD APNRDSSVRGRP              | APN名称（APN）                                | apn1                      | 全网规划     | 当UEG的产品形态为风筝L时，已通过ADD CPAPN配置，可以使用LST CPAPN命令进行查询。                               |
| ADD APNRDSSVRGRP              | Radius Server Group名称（RDSSVRGRPNAME）      | isprg                     | 已配置数据中获取 | 鉴权AAA服务器所在的AAA服务器组，已通过ADD RDSSVRGRP进行配置。                                         |

| 类别         | 参数名称                                 | 取值样例           | 获取方法     | 说明                                                                           |
|:-----------|:-------------------------------------|:---------------|:---------|:-----------------------------------------------------------------------------|
| ADD RDSSVR | Radius Server Group名称（RDSSVRGRPNAME） | isprg          | 已配置数据中获取 | 鉴权AAA服务器所在的AAA服务器组，已通过ADD RDSSVRGRP进行配置。                                     |
| ADD RDSSVR | 服务器类型（SERVERTYPE）                    | AUTHENTICATION | 全网规划     | -                                                                            |
| ADD RDSSVR | 服务器IP版本（IPVERSION）                   | IPV4           | 全网规划     | 鉴权AAA服务器IP地址、端口号、密钥。                                                         |
| ADD RDSSVR | IPv4地址（SERVERIPV4）                   | 10.168.10.1    | 全网规划     | 鉴权AAA服务器IP地址、端口号、密钥。                                                         |
| ADD RDSSVR | 端口（PORT）                             | 1812           | 与对端协商    | 鉴权AAA服务器IP地址、端口号、密钥。                                                         |
| ADD RDSSVR | 服务器密钥（加密的）（CIPHERKEY）                | ispchina       | 与对端协商    | 鉴权AAA服务器IP地址、端口号、密钥。                                                         |
| ADD RDSSVR | 主备用类型（PRIFLAG）                       | PRIMARY        | 本端规划     | -                                                                            |
| ADD RDSSVR | VPN实例名（VPNINSTANCE）                  | vpn_pdn        | 已配置数据中获取 | 计费AAA服务器所属的VPN实例名。当UEG的产品形态为风筝L时，已通过ADD CPVPNINST配置，可以使用LST CPVPNINST命令进行查询。 |
| ADD RDSSVR | 确认服务器密钥（加密的）（CIPHERKEYCNFM）          | ispchina       | 与对端协商    | -                                                                            |

| 类别             | 参数名称                                 | 取值样例        | 获取方法     | 说明                                                                           |
|:---------------|:-------------------------------------|:------------|:---------|:-----------------------------------------------------------------------------|
| ADD UPLIST4RDS | UP列表名称（UPLISTNAME）                   | uplist1     | 本端规划     | -                                                                            |
| ADD UPLIST4RDS | UP实例标识（UPINSTANCEID）                 | up1 up2     | 已配置数据中获取 | 在初始配置时已经通过ADD PNFPROFILE命令配置。此处以配置的UP名称为“up1”和“up2”为例。                       |
| ADD RDSSVR     | Radius Server Group名称（RDSSVRGRPNAME） | isprg       | 已配置数据中获取 | 计费AAA服务器所在的AAA服务器组，已通过ADD RDSSVRGRP进行配置。                                     |
| ADD RDSSVR     | 服务器类型（SERVERTYPE）                    | ACCOUNTING  | 全网规划     | -                                                                            |
| ADD RDSSVR     | 服务器IP版本（IPVERSION）                   | IPV4        | 全网规划     | 计费AAA服务器IP地址、端口号、密钥。                                                         |
| ADD RDSSVR     | IPv4地址（SERVERIPV4）                   | 10.168.10.1 | 全网规划     | 计费AAA服务器IP地址、端口号、密钥。                                                         |
| ADD RDSSVR     | 端口（PORT）                             | 1813        | 与对端协商    | 计费AAA服务器IP地址、端口号、密钥。                                                         |
| ADD RDSSVR     | 服务器密钥（加密的）（CIPHERKEY）                | ispchina    | 与对端协商    | 计费AAA服务器IP地址、端口号、密钥。                                                         |
| ADD RDSSVR     | 主备用类型（PRIFLAG）                       | PRIMARY     | 本端规划     | -                                                                            |
| ADD RDSSVR     | VPN实例名（VPNINSTANCE）                  | vpn_pdn     | 已配置数据中获取 | 计费AAA服务器所属的VPN实例名。当UEG的产品形态为风筝L时，已通过ADD CPVPNINST配置，可以使用LST CPVPNINST命令进行查询。 |
| ADD RDSSVR     | 确认服务器密钥（加密的）（CIPHERKEYCNFM）          | ispchina    | 与对端协商    | -                                                                            |

## 操作步骤

1. 参考配置动态路由OSPF+BFD组网（IPv4）配置对应的组网。
2. 进入“MML命令行-UEG”窗口。
3. 创建L3VPN实例。

   **ADD L3VPNINST**

   ****ADD VPNINSTAF****
4. 创建VPN实例。

   当UEG的产品形态为风筝L时，**ADD CPVPNINST**
5. 配置Gi逻辑接口。

   **ADD LOGICIP**

   当UEG的产品形态为风筝L时，**ADD CPLOGICINF**
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

      **说明** 

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

当UEG的产品形态为风筝L时，

```
ADD CPVPNINST: VPNINSTANCE ="vpn_pdn";
```

//配置Gi接口：

//1.配置Giif1/0/0接口。

当UEG的产品形态为风筝L时，

```
ADD LOGICIP: IPVERSION=IPv4, LOGICIPV4="10.8.20.1", VPNINSTNAME="vpn_pdn";
ADD CPLOGICINF:NAME="giif1/0/0",IPVERSION=IPV4,IPV4ADDRESS1="10.8.20.1",IPV4MASK1="255.255.255.255",VPNINSTANCE="vpn_pdn";
```

//2.配置Giif1/0/1接口。

当UEG的产品形态为风筝L时，

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

当UEG的产品形态为风筝L时，

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
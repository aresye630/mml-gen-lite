# 配置静态路由+BFD组网（IPv6）

- 操作场景
- 必备事项
- 操作步骤
- 验证方法

## 操作场景

VNF与对端设备可通过静态路由绑定静态IPv6 BFD探测的方式进行组网连接，该方式适用于IPv6组网的网络中。

在网络拓扑结构比较简单时，通常使用静态路由方式组网，合理的静态路由可以改进网络性能，并为业务保证带宽。同时，利用单臂Echo转发检测机制为链路提供单向、轻负荷且持续时间短的快速检测功能，提高链路可靠性。

如图1所示为VNF与周边网元的静态路由互通组网示意图。VNF与网关运行静态路由协议而接入运营商网络/企业网络，DC-GW作网关。VNF和DC-GW之间采用单臂BFD探测。DC-GW的配置请参考对应型号设备的产品文档。

**图1** 静态路由+BFD组网

## 必备事项

前提条件

- 请阅读并熟悉特性IPFD-020503 静态路由和IPFD-020403 BFD特性概述。

- 具备管理员权限的操作人员已经登录华为操作维护系统（登录MAE客户端或登录OM Portal）。

- VNF与网络实体之间的网络环境已经构建完成。

数据

VNF使用静态路由绑定静态BFD检测功能与对端设备建立可靠的IP连接。

- 在VNF上配置静态路由与对端建立链路。
- 在VNF上配置静态BFD功能增强链路检测可靠性。
- 在VNF上推荐采用子接口的外联口与外部网络对接。

本文以一组外联口子接口为例进行说明，一组外联口（对应一个逻辑接口）分别在每个ISU虚拟机上各规划3个子接口负荷分担承载流量。实际场景可根据网设规划进行适配。

**说明** 

**如下数据仅为举例，请注意修改成局点规划的数据。**

| 类别                | 参数名称                           | 取值样例                                                                                                                                                     | 获取方法                                                         | 说明                                                                                                                                                            |
|:------------------|:-------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ADD L3VPNINST     | VPN实例名称（VRFNAME）               | VRF_Mp1                                                                                                                                                  | 参见“5G Core LLD文档 > 路由设计 > 5G Core路由设计 > VRF设计 > VRF名称(VNF)”。 | VPN实例全网统一规划，一条通信路径上所有节点绑定的VPN实例要一致，才能正常通信。                                                                                                                    |
| ADD VPNINSTAF     | 地址族类型（AFTYPE）                  | ipv6uni                                                                                                                                                  | -                                                            | IPv6组网场景下，该参数选择ipv6uni。                                                                                                                                       |
| MOD INTERFACE     | 接口名称（IFNAME）                   | Ethernet64/0/4 Ethernet64/0/5 Ethernet64/0/6 Ethernet65/0/4 Ethernet65/0/5 Ethernet65/0/6 Ethernet66/0/4 Ethernet66/0/5 Ethernet66/0/6                   | 参见“5G Core LLD文档 > 业务IP对接设计 > 业务IP设计 > 端口”。                  | -                                                                                                                                                             |
| ADD INTERFACE     | 子接口名字（IFNAME）                  | Ethernet64/0/4.1 Ethernet64/0/5.1 Ethernet64/0/6.1 Ethernet65/0/4.1 Ethernet65/0/5.1 Ethernet65/0/6.1 Ethernet66/0/4.1 Ethernet66/0/5.1 Ethernet66/0/6.1 | 参见“5G Core LLD文档 > 业务IP对接设计 > 业务IP设计 > 子端口”。                 | -                                                                                                                                                             |
| ADD IPBINDVPN     | VPN名字(VRFNAME)                 | VRF_Mp1                                                                                                                                                  | 参见“5G Core LLD文档 > 业务IP对接设计 > 业务IP设计 > VRF”。                 | -                                                                                                                                                             |
| ADD ETHSUBIF      | VLAN类型子接口的VLAN ID（VLANTYPEVID） | 100 200 300 100 200 300 100 200 300                                                                                                                      | 参见“5G Core LLD文档 > 业务IP对接设计 > 业务IP设计 > VLAN序号”。              | -                                                                                                                                                             |
| SET IFIPV6ENABLE  | IPv6使能标志（ENABLEFLAG）           | TRUE                                                                                                                                                     | 固定取值                                                         | -                                                                                                                                                             |
| ADD IFIPV6ADDRESS | IPv6地址(IPV6ADDRESS)            | FC00::10A2 FC00::10C2 FC00::10E2 FC00::10A3 FC00::10C3 FC00::10E3 FC00::10A4 FC00::10C4 FC00::10E4                                                       | 参见“5G Core LLD文档 > 业务IP对接设计 > 业务IP设计 > IP”。                  | 如果规划外联口使用IPv4v6双栈地址，则分别执行ADD IFIPV4ADDRESS和ADD IFIPV6ADDRESS 对同一外联口配置IPv4和IPv6地址。 此处规划的IP地址是与网关互通的外联口IP。 根据ISU VM的数量规划IPv6地址池掩码长度。 此处以123位掩码为例进行介绍，具体以网设规划为准。 |
| ADD IFIPV6ADDRESS | IPv6地址前缀(PREFIXLEN)            | 123                                                                                                                                                      | 参见“5G Core LLD文档 > 业务IP对接设计 > 业务IP设计 > 子网掩码”。                | 如果规划外联口使用IPv4v6双栈地址，则分别执行ADD IFIPV4ADDRESS和ADD IFIPV6ADDRESS 对同一外联口配置IPv4和IPv6地址。 此处规划的IP地址是与网关互通的外联口IP。 根据ISU VM的数量规划IPv6地址池掩码长度。 此处以123位掩码为例进行介绍，具体以网设规划为准。 |
| SET BFD           | 激活BFD（BFDENABLE）               | TRUE                                                                                                                                                     | 参见“5G Core LLD文档 > 路由设计 > 其他路由设计信息 > BFD设计 > BFD是否使能”。       | 参数“DELAYUPTIMER”（会话延迟UP时间）和“TOSEXP”（动态会话报文优先级）可以不用配置，使用默认值即可。                                                                                                 |
| ADD BFDSESSION    | 会话名称（SESSNAME）                 | BfdName31 BfdName32 BfdName33 BfdName34 BfdName35 BfdName36 BfdName37 BfdName38 BfdName39                                                                | 参见“5G Core LLD文档 > 路由设计 > BFD会话 > 会话名称”。                     | -                                                                                                                                                             |
| ADD BFDSESSION    | IP协议版本号（ADDRTYPE）              | IPv6                                                                                                                                                     | 参见“5G Core LLD文档 > 路由设计 > BFD会话 > IP协议版本号”。                  | -                                                                                                                                                             |
| ADD BFDSESSION    | 本地标识符（LOCALDISCR）              | 321 322 323 324 325 326 327 328 329                                                                                                                      | 参见“5G Core LLD文档 > 路由设计 > BFD会话 > 本地标识符”。                    | VNF上BFD会话的本地标识符，需要和对接网关上的标识符对应，即本端的本地标识符与对端网关侧的远端标识符相同。                                                                                                       |
| ADD BFDSESSION    | IPv6目的地址（DESTADDR6）            | FC00::10A1 FC00::10C1 FC00::10E1 FC00::10A1 FC00::10C1 FC00::10E1 FC00::10A1 FC00::10C1 FC00::10E1                                                       | 参见“5G Core LLD文档 > 路由设计 > BFD会话 > 目的地址”。                     | 参数“DESTADDR6”是网关的接口IP，此处用于检测目的IP能否正常接收报文。                                                                                                                     |
| ADD BFDSESSION    | 链路类型（LINKTYPE）                 | IP                                                                                                                                                       | 参见“5G Core LLD文档 > 路由设计 > BFD会话 > 链路类型”。                     | 参数“DESTADDR6”是网关的接口IP，此处用于检测目的IP能否正常接收报文。                                                                                                                     |
| ADD BFDSESSION    | IPv6会话创建方式（CREATETYPE6）        | SESS_STATIC                                                                                                                                              | 参见“5G Core LLD文档 > 路由设计 > BFD会话 > 会话创建方式”。                   | 参数“DESTADDR6”是网关的接口IP，此处用于检测目的IP能否正常接收报文。                                                                                                                     |
| ADD BFDSESSION    | 出接口名称（IFNAME）                  | Ethernet64/0/4.1 Ethernet64/0/5.1 Ethernet64/0/6.1 Ethernet65/0/4.1 Ethernet65/0/5.1 Ethernet65/0/6.1 Ethernet66/0/4.1 Ethernet66/0/5.1 Ethernet66/0/6.1 | 参见“5G Core LLD文档 > 路由设计 > BFD会话 > 出接口名称”。                    | -                                                                                                                                                             |
| ADD BFDSESSION    | VPN实例名称（VRFNAME）               | VRF_Mp1                                                                                                                                                  | 参见“5G Core LLD文档 > 路由设计 > BFD会话 > VPN实例名称”。                  | -                                                                                                                                                             |
| ADD BFDSESSION    | IPv6单臂Echo（ONEARMECHO6）        | TRUE                                                                                                                                                     | 参见“5G Core LLD文档 > 路由设计 > BFD会话 > 单臂Echo”。                   | -                                                                                                                                                             |
| ADD SRROUTE6      | VPN实例名称 （VRFNAME）              | VRF_Mp1                                                                                                                                                  | 参见“5G Core LLD文档 > 路由设计 > 静态路由设计 > VRF名称”。                   | 3个路由下一跳IP地址在不同网段。 参数“PREFIX6”是目的IP，规划的是用于传输Mp1接口报文时：静态路由场景，此处是APP的IP地址。eBGP over 静态路由场景，此处是BGP Peer的IP地址。 参数“NEXTHOP”是网关的接口IP。                                |
| ADD SRROUTE6      | 路由前缀（PREFIX）                   | FC00:2001::4                                                                                                                                             | 参见“5G Core LLD文档 > 路由设计 > 静态路由设计 > 路由前缀”。                    | 3个路由下一跳IP地址在不同网段。 参数“PREFIX6”是目的IP，规划的是用于传输Mp1接口报文时：静态路由场景，此处是APP的IP地址。eBGP over 静态路由场景，此处是BGP Peer的IP地址。 参数“NEXTHOP”是网关的接口IP。                                |
| ADD SRROUTE6      | 路由掩码长度（MASKLENGTH）             | 128                                                                                                                                                      | 参见“5G Core LLD文档 > 路由设计 > 静态路由设计 > 掩码长度”。                    | 3个路由下一跳IP地址在不同网段。 参数“PREFIX6”是目的IP，规划的是用于传输Mp1接口报文时：静态路由场景，此处是APP的IP地址。eBGP over 静态路由场景，此处是BGP Peer的IP地址。 参数“NEXTHOP”是网关的接口IP。                                |
| ADD SRROUTE6      | 路由出接口名字（IFNAME）                | Ethernet64/0/4.1 Ethernet64/0/5.1 Ethernet64/0/6.1 Ethernet65/0/4.1 Ethernet65/0/5.1 Ethernet65/0/6.1 Ethernet66/0/4.1 Ethernet66/0/5.1 Ethernet66/0/6.1 | 已规划数据中获取                                                     | 3个路由下一跳IP地址在不同网段。 参数“PREFIX6”是目的IP，规划的是用于传输Mp1接口报文时：静态路由场景，此处是APP的IP地址。eBGP over 静态路由场景，此处是BGP Peer的IP地址。 参数“NEXTHOP”是网关的接口IP。                                |
| ADD SRROUTE6      | 路由下一跳（NEXTHOP）                 | FC00::10A1 FC00::10C1 FC00::10E1 FC00::10A1 FC00::10C1 FC00::10E1 FC00::10A1 FC00::10C1 FC00::10E1                                                       | 已规划数据中获取                                                     | 3个路由下一跳IP地址在不同网段。 参数“PREFIX6”是目的IP，规划的是用于传输Mp1接口报文时：静态路由场景，此处是APP的IP地址。eBGP over 静态路由场景，此处是BGP Peer的IP地址。 参数“NEXTHOP”是网关的接口IP。                                |
| ADD SRROUTE6      | 静态BFD会话名（SESSIONNAME）          | BfdName31 BfdName32 BfdName33 BfdName34 BfdName35 BfdName36 BfdName37 BfdName38 BfdName39                                                                | 参见“5G Core LLD文档 > 路由设计 > 静态路由设计 > 静态BFD会话”。                 | 3个路由下一跳IP地址在不同网段。 参数“PREFIX6”是目的IP，规划的是用于传输Mp1接口报文时：静态路由场景，此处是APP的IP地址。eBGP over 静态路由场景，此处是BGP Peer的IP地址。 参数“NEXTHOP”是网关的接口IP。                                |

文档

获取网设LLD文档。

## 操作步骤

1. 配置外联口的VPN实例。

   ```
   ADD L3VPNINST:VRFNAME="VRF_Mp1";
   ADD VPNINSTAF:VRFNAME="VRF_Mp1",AFTYPE=ipv6uni;
   ```

   **说明** 

   一条通信路径上所有节点绑定的VPN实例要一致，才能正常通信，例如VNF逻辑接口、VNF外联口、网关上的VPN，否则从逻辑接口发出去的报文会查询路由失败。
2. 配置外联口IP地址。

   1. 查看接口状态及信息。

      ```
      LST INTERFACE:;
      ```
   2. 配置主接口的管理状态为up。

      ```
      MOD INTERFACE:IFNAME="Ethernet64/0/4",IFADMINSTATUS=up;
      MOD INTERFACE:IFNAME="Ethernet64/0/5",IFADMINSTATUS=up;
      MOD INTERFACE:IFNAME="Ethernet64/0/6",IFADMINSTATUS=up;
      MOD INTERFACE:IFNAME="Ethernet65/0/4",IFADMINSTATUS=up;
      MOD INTERFACE:IFNAME="Ethernet65/0/5",IFADMINSTATUS=up;
      MOD INTERFACE:IFNAME="Ethernet65/0/6",IFADMINSTATUS=up;
      MOD INTERFACE:IFNAME="Ethernet66/0/4",IFADMINSTATUS=up;
      MOD INTERFACE:IFNAME="Ethernet66/0/5",IFADMINSTATUS=up;
      MOD INTERFACE:IFNAME="Ethernet66/0/6",IFADMINSTATUS=up;
      ```
   3. 配置以太网子接口。

      ```
      ADD INTERFACE:IFNAME="Ethernet64/0/4.1";
      ADD INTERFACE:IFNAME="Ethernet64/0/5.1";
      ADD INTERFACE:IFNAME="Ethernet64/0/6.1";
      ADD INTERFACE:IFNAME="Ethernet65/0/4.1";
      ADD INTERFACE:IFNAME="Ethernet65/0/5.1";
      ADD INTERFACE:IFNAME="Ethernet65/0/6.1";
      ADD INTERFACE:IFNAME="Ethernet66/0/4.1";
      ADD INTERFACE:IFNAME="Ethernet66/0/5.1";
      ADD INTERFACE:IFNAME="Ethernet66/0/6.1";
      ```
   4. 增加接口绑定VPN。

      ```
      ADD IPBINDVPN:IFNAME="Ethernet64/0/4.1",VRFNAME="VRF_Mp1";
      ADD IPBINDVPN:IFNAME="Ethernet64/0/5.1",VRFNAME="VRF_Mp1";
      ADD IPBINDVPN:IFNAME="Ethernet64/0/6.1",VRFNAME="VRF_Mp1";
      ADD IPBINDVPN:IFNAME="Ethernet65/0/4.1",VRFNAME="VRF_Mp1";
      ADD IPBINDVPN:IFNAME="Ethernet65/0/5.1",VRFNAME="VRF_Mp1";
      ADD IPBINDVPN:IFNAME="Ethernet65/0/6.1",VRFNAME="VRF_Mp1";
      ADD IPBINDVPN:IFNAME="Ethernet66/0/4.1",VRFNAME="VRF_Mp1";
      ADD IPBINDVPN:IFNAME="Ethernet66/0/5.1",VRFNAME="VRF_Mp1";
      ADD IPBINDVPN:IFNAME="Ethernet66/0/6.1",VRFNAME="VRF_Mp1";
      ```
   5. 在以太网子接口上关联VLAN ID。

      ```
      ADD ETHSUBIF:IFNAME="Ethernet64/0/4.1",VLANTYPEVID=100;
      ADD ETHSUBIF:IFNAME="Ethernet64/0/5.1",VLANTYPEVID=200;
      ADD ETHSUBIF:IFNAME="Ethernet64/0/6.1",VLANTYPEVID=300;
      ADD ETHSUBIF:IFNAME="Ethernet65/0/4.1",VLANTYPEVID=100;
      ADD ETHSUBIF:IFNAME="Ethernet65/0/5.1",VLANTYPEVID=200;
      ADD ETHSUBIF:IFNAME="Ethernet65/0/6.1",VLANTYPEVID=300;
      ADD ETHSUBIF:IFNAME="Ethernet66/0/4.1",VLANTYPEVID=100;
      ADD ETHSUBIF:IFNAME="Ethernet66/0/5.1",VLANTYPEVID=200;
      ADD ETHSUBIF:IFNAME="Ethernet66/0/6.1",VLANTYPEVID=300;
      ```

      **说明** 

      子接口配置了VLAN，则需要在交换机、对接网关上调整VLAN的配置。
   6. 配置IPv6使能。

      ```
      SET IFIPV6ENABLE: IFNAME="Ethernet64/0/4.1", ENABLEFLAG=TRUE;
      SET IFIPV6ENABLE: IFNAME="Ethernet64/0/5.1", ENABLEFLAG=TRUE;
      SET IFIPV6ENABLE: IFNAME="Ethernet64/0/6.1", ENABLEFLAG=TRUE;
      SET IFIPV6ENABLE: IFNAME="Ethernet65/0/4.1", ENABLEFLAG=TRUE;
      SET IFIPV6ENABLE: IFNAME="Ethernet65/0/5.1", ENABLEFLAG=TRUE;
      SET IFIPV6ENABLE: IFNAME="Ethernet65/0/6.1", ENABLEFLAG=TRUE;
      SET IFIPV6ENABLE: IFNAME="Ethernet66/0/4.1", ENABLEFLAG=TRUE;
      SET IFIPV6ENABLE: IFNAME="Ethernet66/0/5.1", ENABLEFLAG=TRUE;
      SET IFIPV6ENABLE: IFNAME="Ethernet66/0/6.1", ENABLEFLAG=TRUE;
      ```
   7. 配置外联口的IP地址。

      ```
      ADD IFIPV6ADDRESS:IFNAME="Ethernet64/0/4.1",IPV6ADDRESS="FC00::10A2",PREFIXLEN=123;
      ADD IFIPV6ADDRESS:IFNAME="Ethernet64/0/5.1",IPV6ADDRESS="FC00::10C2",PREFIXLEN=123;
      ADD IFIPV6ADDRESS:IFNAME="Ethernet64/0/6.1",IPV6ADDRESS="FC00::10E2",PREFIXLEN=123;
      ADD IFIPV6ADDRESS:IFNAME="Ethernet65/0/4.1",IPV6ADDRESS="FC00::10A3",PREFIXLEN=123;
      ADD IFIPV6ADDRESS:IFNAME="Ethernet65/0/5.1",IPV6ADDRESS="FC00::10C3",PREFIXLEN=123;
      ADD IFIPV6ADDRESS:IFNAME="Ethernet65/0/6.1",IPV6ADDRESS="FC00::10E3",PREFIXLEN=123;
      ADD IFIPV6ADDRESS:IFNAME="Ethernet66/0/4.1",IPV6ADDRESS="FC00::10A4",PREFIXLEN=123;
      ADD IFIPV6ADDRESS:IFNAME="Ethernet66/0/5.1",IPV6ADDRESS="FC00::10C4",PREFIXLEN=123;
      ADD IFIPV6ADDRESS:IFNAME="Ethernet66/0/6.1",IPV6ADDRESS="FC00::10E4",PREFIXLEN=123;
      ```

      **说明** 

      如果规划外联口使用IPv4v6双栈地址，则分别执行**ADD IFIPV4ADDRESS**和**ADD IFIPV6ADDRESS**对同一外联口配置IPv4和IPv6地址。
3. 全局激活BFD。

   ```
   SET BFD: BFDENABLE=TRUE;
   ```

   **说明** 

   参数“DELAYUPTIMER”（会话延迟UP时间）和“TOSEXP”（动态会话报文优先级）可以不用配置，使用默认值即可。
4. 新建BFD会话。

   ```
   ADD BFDSESSION: SESSNAME="BfdName31",ADDRTYPE=IPv6,CREATETYPE6=SESS_STATIC,ONEARMECHO6=TRUE,LINKTYPE=IP,VRFNAME="VRF_Mp1",LOCALDISCR=321,IFNAME="Ethernet64/0/4.1",DESTADDR6="FC00::10A1";
   ADD BFDSESSION: SESSNAME="BfdName32",ADDRTYPE=IPv6,CREATETYPE6=SESS_STATIC,ONEARMECHO6=TRUE,LINKTYPE=IP,VRFNAME="VRF_Mp1",LOCALDISCR=322,IFNAME="Ethernet64/0/5.1",DESTADDR6="FC00::10C1";
   ADD BFDSESSION: SESSNAME="BfdName33",ADDRTYPE=IPv6,CREATETYPE6=SESS_STATIC,ONEARMECHO6=TRUE,LINKTYPE=IP,VRFNAME="VRF_Mp1",LOCALDISCR=323,IFNAME="Ethernet64/0/6.1",DESTADDR6="FC00::10E1";
   ADD BFDSESSION: SESSNAME="BfdName34",ADDRTYPE=IPv6,CREATETYPE6=SESS_STATIC,ONEARMECHO6=TRUE,LINKTYPE=IP,VRFNAME="VRF_Mp1",LOCALDISCR=324,IFNAME="Ethernet65/0/4.1",DESTADDR6="FC00::10A1";
   ADD BFDSESSION: SESSNAME="BfdName35",ADDRTYPE=IPv6,CREATETYPE6=SESS_STATIC,ONEARMECHO6=TRUE,LINKTYPE=IP,VRFNAME="VRF_Mp1",LOCALDISCR=325,IFNAME="Ethernet65/0/5.1",DESTADDR6="FC00::10C1";
   ADD BFDSESSION: SESSNAME="BfdName36",ADDRTYPE=IPv6,CREATETYPE6=SESS_STATIC,ONEARMECHO6=TRUE,LINKTYPE=IP,VRFNAME="VRF_Mp1",LOCALDISCR=326,IFNAME="Ethernet65/0/6.1",DESTADDR6="FC00::10E1";
   ADD BFDSESSION: SESSNAME="BfdName37",ADDRTYPE=IPv6,CREATETYPE6=SESS_STATIC,ONEARMECHO6=TRUE,LINKTYPE=IP,VRFNAME="VRF_Mp1",LOCALDISCR=327,IFNAME="Ethernet66/0/4.1",DESTADDR6="FC00::10A1";
   ADD BFDSESSION: SESSNAME="BfdName38",ADDRTYPE=IPv6,CREATETYPE6=SESS_STATIC,ONEARMECHO6=TRUE,LINKTYPE=IP,VRFNAME="VRF_Mp1",LOCALDISCR=328,IFNAME="Ethernet66/0/5.1",DESTADDR6="FC00::10C1";
   ADD BFDSESSION: SESSNAME="BfdName39",ADDRTYPE=IPv6,CREATETYPE6=SESS_STATIC,ONEARMECHO6=TRUE,LINKTYPE=IP,VRFNAME="VRF_Mp1",LOCALDISCR=329,IFNAME="Ethernet66/0/6.1",DESTADDR6="FC00::10E1";
   ```

   **说明** 

   必须全局使能BFD功能后该命令才可生效。
5. 配置静态路由并绑定BFD会话。

   ```
   ADD SRROUTE6:VRFNAME="VRF_Mp1",AFTYPE=ipv6unicast,PREFIX="FC00:2001::4",MASKLENGTH=128,DESTVRFNAME="VRF_Mp1",NEXTHOP="FC00::10A1",IFNAME="Ethernet64/0/4.1",SESSIONNAME="BfdName31";
   ADD SRROUTE6:VRFNAME="VRF_Mp1",AFTYPE=ipv6unicast,PREFIX="FC00:2001::4",MASKLENGTH=128,DESTVRFNAME="VRF_Mp1",NEXTHOP="FC00::10C1",IFNAME="Ethernet64/0/5.1",SESSIONNAME="BfdName32";
   ADD SRROUTE6:VRFNAME="VRF_Mp1",AFTYPE=ipv6unicast,PREFIX="FC00:2001::4",MASKLENGTH=128,DESTVRFNAME="VRF_Mp1",NEXTHOP="FC00::10E1",IFNAME="Ethernet64/0/5.1",SESSIONNAME="BfdName33";
   ADD SRROUTE6:VRFNAME="VRF_Mp1",AFTYPE=ipv6unicast,PREFIX="FC00:2001::4",MASKLENGTH=128,DESTVRFNAME="VRF_Mp1",NEXTHOP="FC00::10A1",IFNAME="Ethernet65/0/4.1",SESSIONNAME="BfdName34";
   ADD SRROUTE6:VRFNAME="VRF_Mp1",AFTYPE=ipv6unicast,PREFIX="FC00:2001::4",MASKLENGTH=128,DESTVRFNAME="VRF_Mp1",NEXTHOP="FC00::10C1",IFNAME="Ethernet65/0/5.1",SESSIONNAME="BfdName35";
   ADD SRROUTE6:VRFNAME="VRF_Mp1",AFTYPE=ipv6unicast,PREFIX="FC00:2001::4",MASKLENGTH=128,DESTVRFNAME="VRF_Mp1",NEXTHOP="FC00::10E1",IFNAME="Ethernet65/0/5.1",SESSIONNAME="BfdName36";
   ADD SRROUTE6:VRFNAME="VRF_Mp1",AFTYPE=ipv6unicast,PREFIX="FC00:2001::4",MASKLENGTH=128,DESTVRFNAME="VRF_Mp1",NEXTHOP="FC00::10A1",IFNAME="Ethernet66/0/4.1",SESSIONNAME="BfdName37";
   ADD SRROUTE6:VRFNAME="VRF_Mp1",AFTYPE=ipv6unicast,PREFIX="FC00:2001::4",MASKLENGTH=128,DESTVRFNAME="VRF_Mp1",NEXTHOP="FC00::10C1",IFNAME="Ethernet66/0/5.1",SESSIONNAME="BfdName38";
   ADD SRROUTE6:VRFNAME="VRF_Mp1",AFTYPE=ipv6unicast,PREFIX="FC00:2001::4",MASKLENGTH=128,DESTVRFNAME="VRF_Mp1",NEXTHOP="FC00::10E1",IFNAME="Ethernet66/0/5.1",SESSIONNAME="BfdName39";
   ```

   **说明** 

   - 如果需要为静态路由绑定静态BFD会话，通过**ADD SRROUTE6**的“静态BFD会话名”来指定静态路由所联动的静态BFD的会话名。
   - 在网关侧配置到VNF的回程路由，目的地址为VNF上各逻辑接口的IP地址，下一跳为VNF上配置的各逻辑接口对应的外联口的IP地址。

     需要说明的是，配置VNF与DN/PDN通信的回程路由时，目的地址为UE的网段地址，下一跳为VNF上外联口的IP地址。

## 验证方法

1. 查看接口状态及信息是否与规划数据一致。

   ```
   LST INTERFACE:;
   ```

   ```
   LST IFIPV4ADDRESS:;
   ```

   ```
   LST IFIPV6ADDRESS:;
   ```

   ```
   LST IPBINDVPN:;
   ```

   - 如果一致，请执行2。
   - 如果不一致，请先删除错误的配置，然后参考“操作步骤”重新配置。
2. 检查BFD会话状态是否为up。

   **DSP BFDSESSION**:;

   - 如果状态为up，请执行4。
   - 如果为其他状态，请执行3。
3. 执行**PING**，查看VNF外联口IP与DCGW接口IP能否互通。

   ```
   PING:IPVERSION=IPv4,VPNNAME="VPN_Access",DESTIPV4ADDRESS="对端网关地址";
   ```

   ```
   PING:IPVERSION=IPv6,VPNNAME="VPN_Access",DESTIPV6ADDRESS="对端网关地址";
   ```

   - 丢包率为0%，请执行5。
   - 丢包率不是0%，请检查物理接口及连线是否正常。正常后重新执行2。
4. 检查生成的IPv4静态路由是否与规划数据一致。

   ```
   DSP SRROUTE: AFTYPE=ipv4unicast, VRFNAME="VPN_Access";
   ```

   ```
   DSP SRROUTE6: AFTYPE=ipv6unicast, VRFNAME="VPN_Access";
   ```

   - 如果一致，调测结束。
   - 如果不一致，请执行5。
5. 收集信息并寻求技术支持。

   1. 执行**EXP MML**命令将当前配置数据导出为MML脚本文件并保存。
   2. 收集并保存上述所有查询信息。
   3. 查看并收集对端设备配置及接口状态信息。
   4. 收集归纳所有信息并联系华为技术支持解决。
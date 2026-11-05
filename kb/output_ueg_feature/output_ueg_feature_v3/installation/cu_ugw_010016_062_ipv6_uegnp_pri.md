# 配置静态路由+BFD组网（IPv6）

## 操作场景

VNF与对端设备可通过静态路由绑定静态IPv6 BFD探测的方式进行组网连接，该方式适用于IPv6组网的网络中。

在网络拓扑结构比较简单时，通常使用静态路由方式组网，合理的静态路由可以改进网络性能，并为业务保证带宽。同时，利用BFD双向/单向转发检测机制为链路提供双向/单向、轻负荷且持续时间短的快速检测功能，提高链路可靠性。

如图2所示为VNF与周边网元的静态路由互通组网示意图。VNF与网关运行静态路由协议而接入运营商网络/企业网络，PE（Provider Edge）或DC-GW作网关。VNF和DC-GW之间采用单臂BFD探测。PE的路由配置请参考运营商的网络规划配置，DC-GW的配置请参考对应型号设备的产品文档。

**图1** 静态路由+BFD组网（Eth-trunk子接口组网）

**图2** 静态路由+BFD组网

## 必备事项

前提条件

* 请阅读并熟悉特性IPFD-020503 静态路由和IPFD-020403 BFD特性概述。

* 具备管理员权限的操作人员已经登录华为操作维护系统（登录MAE客户端或登录OM Portal）。

* VNF与网络实体之间的网络环境已经构建完成。

数据

VNF使用静态路由绑定静态BFD检测功能与对端设备建立可靠的IP连接。

* 在VNF上配置静态路由与对端建立链路。
* 在VNF上配置静态BFD功能增强链路检测可靠性。
* 在VNF上推荐采用子接口的外联口与外部网络对接。

本文以一组外联口子接口为例进行说明，一组外联口（对应一个逻辑接口）分别规划在不同刀片的NP卡上，每个NP卡上各规划1个子接口负荷分担承载流量。实际场景可根据网设规划进行适配。

**如下数据仅为举例，请注意修改成局点规划的数据。**

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| **ADD L3VPNINST** | VPN实例名称（VRFNAME） | VPN\_Access | 参见“5G Core LLD文档 > 路由设计 > 5G Core路由设计 > VRF设计 > VRF名称(VNF)”。 | VPN实例全网统一规划，一条通信路径上所有节点绑定的VPN实例要一致，才能正常通信。 |
| **ADD VPNINSTAF** | 地址族类型（AFTYPE） | ipv6uni | - | IPv6组网场景下，该参数选择ipv6uni。 |
| **MOD INTERFACE** | 接口名称（IFNAME） | 100GE66/0/9  100GE67/0/9 | 参见“5G Core LLD文档 > 业务IP对接设计 > 业务IP设计 > 端口”。 | - |
| **ADD INTERFACE** | 子接口名字（IFNAME） | 100GE66/0/9.1  100GE67/0/9.1 | 参见“5G Core LLD文档 > 业务IP对接设计 > 业务IP设计 > 子端口”。 | Ethernet子接口组网需要规划。 |
| **ADD INTERFACE** | 接口名称（IFNAME） | Eth-trunk1 | 本端规划 | Eth-trunk子接口组网需要规划。 |
| **ADD INTERFACE** | 接口名称（IFNAME） | Eth-trunk1.1 | 参见“5G Core LLD文档 > 业务IP对接设计 > 业务IP设计 > 子端口”。 |  |
| **MOD TRUNKIF** | 接口名称（IFNAME） | Eth-trunk1 | 已规划数据中获取 | Eth-trunk子接口组网需要规划。  为保证转发正常，要求在同一条Eth-Trunk链路两端的Eth-Trunk接口上必须配置相同的最小激活链路数，否则在Eth-Trunk口部分成员口或者链路故障的情况下，会导致业务受损。  同一个Trunk的成员接口，可以是同一刀片上的接口，也可以是不同刀片上的接口。此处以加速省交换场景为例，该场景下同一Trunk的成员接口在不同刀片上。  当前本端工作模式为LACP的Eth-trunk接口仅支持passive模式，因此要求对接DC-GW/PE的Eth-trunk接口必须为active模式。即要求对接DC-GW/PE上的端口主动发送LACP报文。 |
|  | 工作模式（WORKMODE） | Lacp | 固定值 |  |
|  | 最小激活链路数（LEASTACTLINKNUM） | 1 | 与对端协商 |  |
| **ADD TRUNKMEMBER** | Trunk接口名（TRUNKIFNAME） | Eth-trunk1 | 已规划数据中获取 |  |
|  | 成员接口名（MEMBERIFNAME） | 100GE66/0/9  100GE67/0/9 | 参见“5G Core LLD文档 > 业务IP对接设计 > 业务IP设计 > 端口”。 |  |
| **ADD IPBINDVPN** | VPN名字(VRFNAME) | VPN\_Access | 参见“5G Core LLD文档 > 业务IP对接设计 > 业务IP设计 > VRF”。 | - |
| **ADD ETHSUBIF** | VLAN类型子接口的VLAN ID（VLANTYPEVID） | 100  200 | 参见“5G Core LLD文档 > 业务IP对接设计 > 业务IP设计 > VLAN序号”。 | 此处以双平面为例，单平面组网时，只需规划一条数据（例如只规划VLAN 100）。 |
| **SET IFIPV6ENABLE** | IPv6使能标志（ENABLEFLAG） | TRUE | 固定取值 | - |
| **ADD IFIPV6ADDRESS** | IPv6地址(IPV6ADDRESS) | FC00::10C2  FC00::10C3  FC00::10E2 | 参见“5G Core LLD文档 > 业务IP对接设计 > 业务IP设计 > IP”。 | 如果规划外联口使用IPv4v6双栈地址，则分别执行**ADD IFIPV4ADDRESS**和**ADD IFIPV6ADDRESS**  对同一外联口配置IPv4和IPv6地址。  此处规划的IP地址是与网关互通的外联口IP。Eth-trunk子接口组网时，规划1个IP；直连PE，Ethernet子接口组网时，规划2个不同网段的IP；直连DC-GW，Ethernet子接口组网时，规划2个同一网段的IP。 |
|  | IPv6地址前缀(PREFIXLEN) | 123 | 参见“5G Core LLD文档 > 业务IP对接设计 > 业务IP设计 > 子网掩码”。 |  |
| **SET BFD** | 激活BFD（BFDENABLE） | TRUE | 参见“5G Core LLD文档 > 路由设计 > 其他路由设计信息 > BFD设计 > BFD是否使能”。 | 参数“DELAYUPTIMER”（会话延迟UP时间）和“TOSEXP”（动态会话报文优先级）可以不用配置，使用默认值即可。 |
| **ADD BFDSESSION** | 会话名称（SESSNAME） | BfdName22  BfdName24 | 参见“5G Core LLD文档 > 路由设计 > BFD会话 > 会话名称”。 | - |
|  | IP协议版本号（ADDRTYPE） | IPv6 | 参见“5G Core LLD文档 > 路由设计 > BFD会话 > IP协议版本号”。 |  |
|  | 本地标识符（LOCALDISCR） | 122  124 | 参见“5G Core LLD文档 > 路由设计 > BFD会话 > 本地标识符”。 | VNF上BFD会话的本地标识符，需要和对接网关上的标识符对应，即本端的本地标识符与对端网关侧的远端标识符相同。 |
|  | 远端标识符（REMOTEDISCR） | 222  224 | 参见“5G Core LLD文档 > 路由设计 > BFD会话 > 远端标识符”。 | VNF上BFD会话的远端标识符，需要和对接网关上的标识符对应，即本端的远端标识符与对端网关侧的本端标识符相同。  “ONEARMECHO6”为“TRUE”时，不需要规划远端标识符。 |
|  | IPv6目的地址（DESTADDR6） | FC00::10C1  FC00::10E1 | 参见“5G Core LLD文档 > 路由设计 > BFD会话 > 对端IP地址”。 | 参数“DESTADDR6”是网关的接口IP，此处用于检测目的IP能否正常接收报文。 |
|  | 链路类型（LINKTYPE） | IP | 参见“5G Core LLD文档 > 路由设计 > BFD会话 > 链路类型”。 |  |
|  | IPv6会话创建方式（CREATETYPE6） | SESS\_STATIC | 参见“5G Core LLD文档 > 路由设计 > BFD会话 > 会话创建方式”。 |  |
|  | 出接口名称（IFNAME） | 100GE66/0/9.1  100GE67/0/9.1 | 参见“5G Core LLD文档 > 路由设计 > BFD会话 > 出接口名称”。 | Ethernet子接口组网需要规划。 |
|  | 出接口名称（IFNAME） | Eth-trunk1.1 | 参见“5G Core LLD文档 > 路由设计 > BFD会话 > 出接口名称”。 | Eth-trunk子接口组网需要规划。 |
|  | VPN实例名称（VRFNAME） | VPN\_Access | 参见“5G Core LLD文档 > 路由设计 > BFD会话 > VPN实例名称”。 | VNF所在硬件设备直连DC-GW时“ONEARMECHO6”取值为“TRUE”，直连PE时“ONEARMECHO6”取值为“FALSE”。 |
|  | IPv6单臂Echo（ONEARMECHO6） | FALSE | 参见“5G Core LLD文档 > 路由设计 > BFD会话 > 单臂Echo”。 |  |
| **ADD SRROUTE6** | VPN实例名称 （VRFNAME） | VPN\_Access | 参见“5G Core LLD文档 > 路由设计 > 静态路由设计 > VRF名称”。 | Eth-trunk子接口单平面组网时，需要规划2个路由下一跳IP地址，且这2个IP在同一网段。  双平面组网时，2个路由下一跳IP地址在不同网段。  参数“PREFIX”是目的IP，规划的是用于传输N3接口报文时，此处是基站的IP地址。  参数“NEXTHOP”是网关的接口IP。 |
|  | 路由前缀（PREFIX） | FC00:2001::4 | 参见“5G Core LLD文档 > 路由设计 > 静态路由设计 > 路由前缀”。 |  |
|  | 路由掩码长度（MASKLENGTH） | 128 | 参见“5G Core LLD文档 > 路由设计 > 静态路由设计 > 掩码长度”。 |  |
|  | 路由下一跳（NEXTHOP） | FC00::10C1  FC00::10E1 | 已规划数据中获取 |  |
|  | 静态BFD会话名（SESSIONNAME） | BfdName22  BfdName24 | 参见“5G Core LLD文档 > 路由设计 > 静态路由设计 > 静态BFD会话”。 |  |

文档

获取网设LLD文档。

## 操作步骤

1. 配置外联口的VPN实例。

   ```
   ADD L3VPNINST:VRFNAME="VPN_Access";
   ADD VPNINSTAF:VRFNAME="VPN_Access",AFTYPE=ipv6uni;
   ```

   一条通信路径上所有节点绑定的VPN实例要一致，才能正常通信，例如VNF逻辑接口、VNF外联口、网关上的VPN，否则从逻辑接口发出去的报文会查询路由失败。
2. Ethernet子接口组网时，配置外联口IP地址。Eth-trunk子接口组网时，请跳过本步骤。

   1. 查看接口状态及信息。

      ```
      LST INTERFACE:;
      ```
   2. 配置主接口的管理状态为up。

      ```
      MOD INTERFACE:IFNAME="100GE66/0/9",IFADMINSTATUS=up;
      MOD INTERFACE:IFNAME="100GE67/0/9",IFADMINSTATUS=up;
      ```
   3. 配置以太网子接口。

      ```
      ADD INTERFACE:IFNAME="100GE66/0/9.1";
      ADD INTERFACE:IFNAME="100GE67/0/9.1";
      ```
   4. 增加接口绑定VPN。

      ```
      ADD IPBINDVPN:IFNAME="100GE66/0/9.1",VRFNAME="VPN_Access";
      ADD IPBINDVPN:IFNAME="100GE67/0/9.1",VRFNAME="VPN_Access";
      ```
   5. 在以太网子接口上关联VLAN ID。如下以直连PE为例，直连DC-GW且DC-GW间是E-Trunk+EVPN组网时，两个接口的VLAN ID相同。

      ```
      ADD ETHSUBIF:IFNAME="100GE66/0/9.1",VLANTYPEVID=100;
      ADD ETHSUBIF:IFNAME="100GE67/0/9.1",VLANTYPEVID=200;
      ```

      子接口配置了VLAN，则需要在交换机、对接网关上调整VLAN的配置。
   6. 配置IPv6使能。

      ```
      SET IFIPV6ENABLE: IFNAME="100GE66/0/9.1", ENABLEFLAG=TRUE;
      SET IFIPV6ENABLE: IFNAME="100GE67/0/9.1", ENABLEFLAG=TRUE;
      ```
   7. 配置外联口的IP地址。如下以直连PE为例，直连DC-GW且DC-GW间是E-Trunk+EVPN组网时，100GE67/0/9.1接口IP为FC00::10C3。

      ```
      ADD IFIPV6ADDRESS:IFNAME="100GE66/0/9.1",IPV6ADDRESS="FC00::10C2",PREFIXLEN=123;
      ADD IFIPV6ADDRESS:IFNAME="100GE67/0/9.1",IPV6ADDRESS="FC00::10E2",PREFIXLEN=123;
      ```

      如果规划外联口使用IPv4v6双栈地址，则分别执行**ADD IFIPV4ADDRESS**和**ADD IFIPV6ADDRESS**对同一外联口配置IPv4和IPv6地址。
3. Eth-trunk子接口组网时，配置外联口IP地址。Ethernet子接口组网时，请跳过本步骤。

   1. 查看接口状态及信息。

      ```
      LST INTERFACE:;
      ```
   2. 配置主接口的管理状态为up。

      ```
      MOD INTERFACE:IFNAME="100GE66/0/9",IFADMINSTATUS=up;
      MOD INTERFACE:IFNAME="100GE67/0/9",IFADMINSTATUS=up;
      ```
   3. 配置以太Trunk接口。

      ```
      ADD INTERFACE:IFNAME="Eth-trunk1";
      ```
   4. 配置Eth-trunk接口的工作模式并添加成员端口。

      ```
      MOD TRUNKIF:IFNAME="Eth-Trunk1",WORKMODE=Lacp,LEASTACTLINKNUM=1;
      ADD TRUNKMEMBER:TRUNKIFNAME="Eth-trunk1",MEMBERIFNAME="100GE66/0/9";
      ADD TRUNKMEMBER:TRUNKIFNAME="Eth-trunk1",MEMBERIFNAME="100GE67/0/9";
      ```
   5. 配置以太Trunk子接口。

      ```
      ADD INTERFACE:IFNAME="Eth-trunk1.1";
      ```
   6. 增加接口绑定VPN。

      ```
      ADD IPBINDVPN:IFNAME="Eth-trunk1.1",VRFNAME="VPN_Access";
      ```
   7. 在以太网子接口上关联VLAN ID。

      ```
      ADD ETHSUBIF:IFNAME="Eth-trunk1.1",VLANTYPEVID=100;
      ```

      子接口配置了VLAN，则需要在交换机、对接网关上调整VLAN的配置。
   8. 配置IPv6使能。

      ```
      SET IFIPV6ENABLE: IFNAME="Eth-trunk1.1", ENABLEFLAG=TRUE;
      ```
   9. 配置外联口的IP地址。

      ```
      ADD IFIPV6ADDRESS:IFNAME="Eth-trunk1.1",IPV6ADDRESS="FC00::10C2",PREFIXLEN=123;
      ```

      如果规划外联口使用IPv4v6双栈地址，则分别执行**ADD IFIPV4ADDRESS**和**ADD IFIPV6ADDRESS**对同一外联口配置IPv4和IPv6地址。
4. 全局激活BFD。

   ```
   SET BFD: BFDENABLE=TRUE;
   ```

   参数“DELAYUPTIMER”（会话延迟UP时间）和“TOSEXP”（动态会话报文优先级）可以不用配置，使用默认值即可。
5. 新建BFD会话。

   必须全局使能BFD功能后该命令才可生效。

   * Ethernet子接口组网场景下：
     + 双向BFD探测

       ```
       ADD BFDSESSION: SESSNAME="BfdName22",ADDRTYPE=IPv6,CREATETYPE6=SESS_STATIC,ONEARMECHO6=FALSE,LINKTYPE=IP,VRFNAME="VPN_Access",LOCALDISCR=122,REMOTEDISCR=222,IFNAME="100GE66/0/9.1",DESTADDR6="FC00::10C1";
       ADD BFDSESSION: SESSNAME="BfdName24",ADDRTYPE=IPv6,CREATETYPE6=SESS_STATIC,ONEARMECHO6=FALSE,LINKTYPE=IP,VRFNAME="VPN_Access",LOCALDISCR=124,REMOTEDISCR=224,IFNAME="100GE67/0/9.1",DESTADDR6="FC00::10E1";
       ```
     + BFD单臂Echo探测（如下以直连PE为例，直连DC-GW且DC-GW间是E-Trunk+EVPN组网时，BFD探测目的IP地址相同。）

       ```
       ADD BFDSESSION: SESSNAME="BfdName22",ADDRTYPE=IPv6,CREATETYPE6=SESS_STATIC,ONEARMECHO6=TRUE,LINKTYPE=IP,VRFNAME="VPN_Access",LOCALDISCR=122,IFNAME="100GE66/0/9.1",DESTADDR6="FC00::10C1";
       ADD BFDSESSION: SESSNAME="BfdName24",ADDRTYPE=IPv6,CREATETYPE6=SESS_STATIC,ONEARMECHO6=TRUE,LINKTYPE=IP,VRFNAME="VPN_Access",LOCALDISCR=124,IFNAME="100GE67/0/9.1",DESTADDR6="FC00::10E1";
       ```
   * Eth-trunk子接口组网场景下：
     + 双向BFD探测

       ```
       ADD BFDSESSION: SESSNAME="BfdName22",ADDRTYPE=IPv6,CREATETYPE6=SESS_STATIC,ONEARMECHO6=FALSE,LINKTYPE=IP,VRFNAME="VPN_Access",LOCALDISCR=122,REMOTEDISCR=222,IFNAME="Eth-trunk1.1",DESTADDR6="FC00::10C1";
       ```
     + BFD单臂Echo探测

       ```
       ADD BFDSESSION: SESSNAME="BfdName22",ADDRTYPE=IPv6,CREATETYPE6=SESS_STATIC,ONEARMECHO6=TRUE,LINKTYPE=IP,VRFNAME="VPN_Access",LOCALDISCR=122,IFNAME="Eth-trunk1.1",DESTADDR6="FC00::10C1";
       ```
6. 配置静态路由并绑定BFD会话。
   * Ethernet子接口组网场景下：（如下以直连PE为例，直连DC-GW且DC-GW间是E-Trunk+EVPN组网时，下一跳IP地址相同。）

     ```
     ADD SRROUTE6:VRFNAME="VPN_Access",AFTYPE=ipv6unicast,PREFIX="FC00:2001::4",MASKLENGTH=128,DESTVRFNAME="VPN_Access",NEXTHOP="FC00::10C1",IFNAME="100GE66/0/9.1",SESSIONNAME="BfdName22";
     ADD SRROUTE6:VRFNAME="VPN_Access",AFTYPE=ipv6unicast,PREFIX="FC00:2001::4",MASKLENGTH=128,DESTVRFNAME="VPN_Access",NEXTHOP="FC00::10E1",IFNAME="100GE67/0/9.1",SESSIONNAME="BfdName24";
     ```
   * Eth-trunk子接口组网场景下：

     ```
     ADD SRROUTE6:VRFNAME="VPN_Access",AFTYPE=ipv6unicast,PREFIX="FC00:2001::4",MASKLENGTH=128,DESTVRFNAME="VPN_Access",NEXTHOP="FC00::10C1",IFNAME="Eth-trunk1.1",SESSIONNAME="BfdName22";
     ```

   * 如果需要为静态路由绑定静态BFD会话，通过**ADD SRROUTE6**的“静态BFD会话名”来指定静态路由所联动的静态BFD的会话名。
   * 在网关侧配置到VNF的回程路由，目的地址为VNF上各逻辑接口的IP地址，下一跳为VNF上配置的各逻辑接口对应的外联口的IP地址。

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

   * 如果一致，请执行2。
   * 如果不一致，请先删除错误的配置，然后参考“操作步骤”重新配置。
2. 检查BFD会话状态是否为up。

   **DSP BFDSESSION**:;

   * 如果状态为up，请执行4。
   * 如果为其他状态，请执行3。
3. 执行**PING**，查看VNF外联口IP与DCGW接口IP能否互通。

   ```
   PING:IPVERSION=IPv4,VPNNAME="VPN_Access",DESTIPV4ADDRESS="对端网关地址";
   ```

   ```
   PING:IPVERSION=IPv6,VPNNAME="VPN_Access",DESTIPV6ADDRESS="对端网关地址";
   ```

   * 丢包率为0%，请执行5。
   * 丢包率不是0%，请检查物理接口及连线是否正常。正常后重新执行2。
4. 检查生成的IPv4静态路由是否与规划数据一致。

   ```
   DSP SRROUTE: AFTYPE=ipv4unicast, VRFNAME="VPN_Access";
   ```

   ```
   DSP SRROUTE6: AFTYPE=ipv6unicast, VRFNAME="VPN_Access";
   ```

   * 如果一致，调测结束。
   * 如果不一致，请执行5。
5. 收集信息并寻求技术支持。

   1. 执行**EXP MML**命令将当前配置数据导出为MML脚本文件并保存。
   2. 收集并保存上述所有查询信息。
   3. 查看并收集对端设备配置及接口状态信息。
   4. 收集归纳所有信息并联系华为技术支持解决。

版权所有 © 华为技术有限公司

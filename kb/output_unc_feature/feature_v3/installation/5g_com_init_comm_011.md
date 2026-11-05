# 配置BGP over OSPF/静态路由+BFD（IPv4）

* 操作场景
* 必备事项
* 操作步骤
* 验证方法

## 操作场景

BGP（Border Gateway Protocol）边界网关协议是一种用于AS(Autonomous System)之间的动态路由协议，与OSPF、静态路由等内部网关协议（IGP）不同，其自身不能发现和计算路由，主要用于在自治系统AS间控制路由的传播和选择最佳路由。

当拓扑结构复杂且无法规划在同一自治区域内时，可以采用BGP over OSPF/静态路由+BFD实现VNF与对端设备的网络层互通。

* BGP协议自身没有自动部署功能，本文主要是在OSPF、静态路由等内部网关协议的自动部署基础上，通过BGP协议将其引入并传播。
* 采用DC-GW作网关时，采用BGP over静态路由+BFD；采用PE作网关时，采用BGP over静态路由+BFD（推荐）或BGP over OSPF+BFD。

* 图1为VNF与周边网元的BGP over OSPF/静态路由+BFD互通组网示意图。VNF与网关侧运行BGP over OSPF/静态路由+BFD路由协议而接入运营商网络（IP骨干网），网关推荐使用DC-GW，也可以使用运营商的PE（Provider Edge）交换机，或者EOR（End of Row）交换机。无论哪种方式，VNF的配置相同，没有差异。PE的路由配置请参考运营商的网络规划配置，DC-GW/EOR的配置请参考对应型号设备的产品文档。
* 图2为VNF与周边网元的BGP over静态路由互通组网示意图。VNF与网关侧运行BGP over静态路由协议而接入运营商网络（IP骨干网），DC-GW作为网关设备。VNF和DC-GW之间采用单臂BFD探测。DC-GW的配置请参考对应型号设备的产品文档。

**图1** BGP over OSPF/静态路由+BFD组网（DC-GW/EOR做L3GW）

**图2** BGP over静态路由+BFD组网（DC-GW做L3GW+L2GW）

## 必备事项

前提条件

* 请阅读并熟悉特性IPFD-014002 支持BGP特性概述。
* 已完成配置动态路由OSPF+BFD组网（IPv4）或配置静态路由+BFD组网（IPv4）。

* 具备管理员权限的操作人员已经登录华为操作维护系统（登录U2020/MAE客户端或登录OM Portal）。

* VNF与网络实体之间的网络环境已经构建完成。

数据

VNF使用BGP over OSPF/静态路由+BFD与对端设备建立可靠的IP连接。

本文以一组外联口子接口为例进行说明，一组外联口（对应一个逻辑接口）分别规划在2个CSLB上，每个CSLB上各规划2个子接口负荷分担承载流量。实际场景可根据网设规划进行适配。

**如下数据仅为举例，请注意修改成局点规划的数据。**

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| ****ADD INTERFACE**** | 接口名（IFNAME） | Loopback1 | 参见“5G Core LLD文档 > 路由设计 > BGP设计 > 本地接口名称（VNF侧）”。 | - |
| ****ADD IPBINDVPN**** | VPN实例名称（VRFNAME） | VPN\_Access | 参见“5G Core LLD文档 > 路由设计 > BGP设计 > VRF名称”。 | 此处的VPN实例已经配置，与OSPF、静态路由等IGP协议的外联口绑定的VPN实例相同。 |
| **ADD IFIPV4ADDRESS** | 接口IPv4地址（IFIPADDR） | 10.90.7.160 | 参见“5G Core LLD文档 > 路由设计 > BGP设计 > 本地IP（VNF侧）”。 | 如果规划外联口使用IPv4v6双栈地址，则分别执行**ADD IFIPV4ADDRESS**和**ADD IFIPV6ADDRESS**  对同一vNIC配置IPv4和IPv6地址。 |
|  | 接口IPv4地址掩码（SUBNETMASK） | 255.255.255.255 | 固定取值 |  |
| **SET BGP** | 使能BGP（BGPENABLE） | TRUE | 固定取值 | - |
|  | BGP自治域号（ASNUM） | 60001 | 参见“5G Core LLD文档 > 路由设计 > BGP设计 > AS号（VNF侧）”。 |  |
| ****ADD BGPVRF**** | VPN实例名称（VRFNAME） | VPN\_Access | 参见“5G Core LLD文档 > 路由设计 > BGP设计 > VRF名称”。 | BGP VPN实例需要与Loopback接口绑定的VPN实例名一致。 |
|  | 默认地址族（DEFAULTAFTYPE） | noaf | 固定取值 | - |
|  | 路由器标识（ROUTERID） | 10.90.7.160 | 参见“5G Core LLD文档 > 路由设计 > BGP设计 > Router ID”。 | 不同BGP VPN实例的ROUTERID不能重复。 |
| **ADD BGPVRFAF** | VPN实例名称（VRFNAME） | VPN\_Access | 已配置数据中获取 | 使用**ADD BGPVRF**命令定义的VPN实例名称。 |
|  | 地址族类型（AFTYPE） | ipv4uni | 固定取值 | - |
|  | 最大等价路由数（MAXIMUMLOADBALANCE） | 2 | 本端规划 | 对接的负荷分担关系的BGP peer数。 |
| ****ADD BGPPEER**** | 地址类型（ADDRESSTYPE） | ipv4 | - | “PEERADDR”是网关上用于和VNF建立BGP邻居关系的IP地址。 |
|  | IPv4对等体地址（PEERADDR） | 10.9.7.135 | 参见“5G Core LLD文档 > 路由设计 > BGP设计 > 本地IP（网关侧）”。 |  |
|  | 对等体AS号（REMOTEAS） | 60002 | 参见“5G Core LLD文档 > 路由设计 > BGP设计 > AS号（网关侧）”。 |  |
|  | 本地接口地址（LOCALIFADDR） | 10.90.7.160 | 参见“5G Core LLD文档 > 路由设计 > BGP设计 > 本地IP（VNF侧）”。 |  |
|  | 本地接口名称（LOCALIFNAME） | Loopback1 | 参见“5G Core LLD文档 > 路由设计 > BGP设计 > 本地接口名称（VNF侧）”。 |  |
|  | EBGP最大跳数（EBGPMAXHOP） | 255 | - | “EBGPMAXHOP”不小于到Peer之间的实际跳数，无法确认时，可设置为10。  如最大跳数设置过小，会导致BGP邻居建立失败。 |
| ****ADD IMPORTROUTE**** | 地址族类型（AFTYPE） | ipv4uni | - | IPv4组网场景下，该参数选择ipv4uni。  该参数全局取值要一致。 |
|  | 路由协议（IMPORTPROTOCOL） | wlr | 参见“5G Core LLD文档 > 路由设计 > BGP设计 > Import Route类型”。 | - |

文档

获取网设LLD文档。

## 操作步骤

1. 配置OSPF+BFD、静态路由+BFD。

   由于BGP协议自身不能发现路由，所以需要引入其他协议的路由（如OSPF或者静态路由等）注入到BGP路由表中，从而将这些路由在AS之内和AS之间传播。

   * 配置动态路由OSPF+BFD组网（IPv4）
   * 配置静态路由+BFD组网（IPv4）

   * BFD会话绑定的是路由，不是BGPPEER。如存在**ADD BGPPEERBFD**配置，请删除。
   * 本步骤配置的是静态路由时，需要配置如下两类路由：
     + IP路由1：目的IP是BGP对等体地址，下一跳是网关的接口IP地址，且该路由需要绑定BFD会话。
     + IP路由2：目的IP是0.0.0.0，掩码长度是0，其他参数取值与“IP路由1”中的参数值相同。IP路由2的优先级要低于对端发布的路由优先级，当对端发布默认路由时，不需要配置IP路由2。
2. 配置Loopback接口地址。
   1. 配置Loopback接口。

      ```
      ADD INTERFACE:IFNAME="Loopback1";
      ```
   2. 配置接口绑定VPN。

      ```
      ADD IPBINDVPN:IFNAME="Loopback1",VRFNAME="VPN_Access";
      ```
   3. 配置接口IP地址。

      ```
      ADD IFIPV4ADDRESS:IFNAME="Loopback1",IFIPADDR="10.90.7.160",SUBNETMASK="255.255.255.255";
      ```
3. 全局激活BGP。

   ```
   SET BGP: BGPENABLE=TRUE, ASNUM="60001";
   ```
4. 配置BGP。
   1. 增加BGP VPN实例。

      ```
      ADD BGPVRF: VRFNAME="VPN_Access", DEFAULTAFTYPE=noaf, ROUTERID="10.90.7.160";
      ```

      * 此处配置的“ROUTERID”是BGP VPN实例级别的ROUTERID。

        IPv4v6双栈时，IPv4 BGP VPN实例地址族和IPv6 BGP VPN实例地址族共用此处配置的“ROUTERID”值。
      * 已配置IPv4v6双栈的BGP VPN实例地址族，若需删除IPv4的BGP VPN实例地址族配置，则：

        1、删除IPv4的配置前需查询并记录“ROUTERID”值。

        2、删除IPv4的配置后需查询“ROUTERID”值是否存在，若不存在则需通过**MOD BGPVRF**命令将“ROUTERID”参数设置为删除IPv4的配置前记录的“ROUTERID”值。否则IPv6 BGP重新协商时会因无“ROUTERID”值可用而导致协商失败。
   2. 增加BGP VPN实例地址族。VNF对接2个负荷分担的路由设备时，“MAXIMUMLOADBALANCE”设置为“2”。

      ```
      ADD BGPVRFAF: VRFNAME="VPN_Access", AFTYPE=ipv4uni, MAXIMUMLOADBALANCE=2;
      ```
   3. 增加BGP对等体。

      ```
      ADD BGPPEER: VRFNAME="VPN_Access", ADDRESSTYPE=ipv4, PEERADDR="10.9.7.135", REMOTEAS="60002", LOCALIFADDR="10.90.7.160", LOCALIFNAME="Loopback1", EBGPMAXHOP=10;
      ```
   4. 增加BGP引入路由。

      ```
      ADD IMPORTROUTE: VRFNAME="VPN_Access", AFTYPE=ipv4uni, IMPORTPROTOCOL=wlr, MEDENABLE=FALSE;
      ```

      由于BGP协议自身不能发现路由，所以需要引入其他协议的路由（如OSPF、静态路由或WLR等）注入到BGP路由表中，从而将这些路由在AS之内和AS之间传播。

## 验证方法

1. 查看各网元间的路由连接是否正常。

   执行**PING**命令，查看VNF与对端设备间的路由连接是否正常。

   如果使用了VPN组网，还需使用“VPN实例名称（VPNNAME）”指定VPN实例，这样才能验证VPN实例路由是否正常。

   * 如果收到对端网元的响应且响应报文中有成功收发包的个数，表明连接正常，请执行2。
   * 如果连续出现timeout，表明链路不通，请检查本端或承载网是否存在物理接口故障或者路由配置错误，请执行3。
2. 执行**PING**命令，在DC-GW上检查DC-GW接口IP与VNF外联口IP之间是否路由可达。

   需要在DC-GW上分别PING VNF上的负荷分担关系的每个外联口的IP，且能PING通。

   * 是，请执行4。
   * 否，请联系华为技术支持工程师处理（例如检查DC-GW上是否存在到VNF BGP IP的路由，下一跳分别是VNF的负荷分担关系的每个外联口的IP），然后重新执行1。
3. 执行**LST INTERFACE**命令，查看接口状态及信息是否与规划数据一致。

   * 如果一致，请执行4。
   * 如果不一致，请参考“操作步骤”修改配置后，重新执行1。
4. 执行**LST BGPPEER**命令，查看BGP对等体配置是否与规划数据一致。
   * 如果一致，请执行5。
   * 如果不一致，请参考“操作步骤”修改配置后，重新执行1。
5. 执行**DSP BGPPEERINFO**命令，检查BGP对等体条数是否正确及BGP对等体状态是否为Established。

   本步骤的显示结果中的BGP对等体的条数与LST BGPPEER中查询的对等体的条数相等，且“对等体状态”为“Established”。

   * 是，调测结束。
   * 否，请执行6。
6. 收集信息并寻求技术支持。

   1. 执行**EXP MML**命令将当前配置数据导出为MML脚本文件并保存。
   2. 收集并保存上述所有查询信息。
   3. 查看并收集对端设备配置及接口状态信息。
   4. 收集归纳所有信息并联系华为技术支持解决。

版权所有 © 华为技术有限公司

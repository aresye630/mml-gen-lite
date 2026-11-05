# 配置动态路由OSPFv3（IPv6）

## 操作场景

网关设备（如FW）不支持BFD时，UEG与对端设备可通过OSPFv3动态路由进行组网连接，该方式适用于IPv6组网的网络中。

图1是UEG与周边网元通过OSPFv3动态路由互通的组网示意。UEG与网关设备（如FW）运行动态路由协议而接入企业网络，UEG的配置请参考本页面，FW的配置请参考FW对应型号设备的产品文档。

**图1** OSPFv3动态路由组网

## 必备事项

前提条件

* 请阅读并熟悉特性IPFD-020501 支持OSPF特性概述。
* 具备管理员权限的操作人员已经登录华为操作维护系统（登录MAE客户端或登录OM Portal）。
* UEG与网络实体之间的网络环境已经构建完成。

数据

UEG使用OSPFv3动态路由与对端设备建立IP连接，采用OSPFv3协议收敛保证可靠性。

* 在UEG上配置OSPFv3动态路由与对端建立链路。
* 在UEG上推荐采用子接口的外联口与外部网络对接。
* 本页面以UEG通过FW与企业园区的服务器互通为例。

**如下数据仅为举例，请注意修改成局点规划的数据。**

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| **ADD L3VPNINST** | VPN实例名称（VRFNAME） | VPN\_LocalDN | 本端规划 | VPN实例全网统一规划，一条通信路径上所有节点绑定的VPN实例要一致，才能正常通信。 |
| **ADD VPNINSTAF** | 地址族类型（AFTYPE） | ipv6uni | - | IPv6组网场景下，该参数选择ipv6uni。 |
| **MOD INTERFACE** | 接口名称（IFNAME） | Ethernet64/0/6  Ethernet64/0/7 | 本端规划 | * （UEG-S）请参考外联口介绍(机架服务器-ARM)/外联口介绍(刀片式服务器2U)进行规划。 * （UEG-M）请参考外联口介绍(刀片式服务器2U)进行规划。 * （UEG-L）请参考外联口介绍(刀片式服务器2U)进行规划。 |
| **ADD INTERFACE** | 子接口名字（IFNAME） | Ethernet64/0/6.1  Ethernet64/0/7.1 | 本端规划 | 免交换场景，使用非SR-IOV bonding组网，此处规划的是Ethernet子接口。 |
| **ADD IPBINDVPN** | VPN名字(VRFNAME) | VPN\_LocalDN | 已配置数据中获取 | - |
| **ADD ETHSUBIF** | VLAN类型子接口的VLAN ID（VLANTYPEVID） | 100  200 | 全网规划 | 此处以双平面为例。 |
| **SET IFIPV6ENABLE** | IPv6使能标志（ENABLEFLAG） | TRUE | 固定取值 | - |
| **ADD IFIPV6ADDRESS** | IPv6地址(IPV6ADDRESS) | FC00::10C2  FC00::10E2 | 全网规划 | 如果规划外联口使用IPv4v6双栈地址，则分别执行**ADD IFIPV4ADDRESS**和**ADD IFIPV6ADDRESS**  对同一外联口配置IPv4和IPv6地址。  此处规划的IP地址是与网关互通的外联口IP。 |
|  | IPv6地址前缀(PREFIXLEN) | 123 | 全网规划 |  |
| **ADD OSPFV3** | OSPFv3进程号(PROCID) | 6 | 本端规划 | - |
|  | 路由器标识(ROUTERID) | 10.8.25.1 | 全网规划 |  |
|  | VPN的名称(VRFNAME) | VPN\_LocalDN | 已配置数据中获取 |  |
|  | 使能BFD（BFDALLINTFFLG） | FALSE | 全网规划 | 三层路由设备FW不支持BFD时，使用样例值。 |
| **ADD OSPFV3AREA** | 区域号（AREAID） | 0.0.0.5 | 与对端协商 | 两个接口若要建立邻居关系，则Area ID必须相同。 |
|  | OSPFv3区域类型(AREATYPE) | NSSA | 与对端协商 | 两个接口若要建立邻居关系，则Area Type必须相同。 |
| **ADD OSPFV3INTERFACE** | OSPFv3进程号(PROCID) | 6 | 已规划数据中获取 | - |
|  | 区域号（AREAID） | 0.0.0.5 | 已规划数据中获取 |  |
|  | 接口名称（IFNAME） | Ethernet64/0/6.1  Ethernet64/0/7.1 | 已规划数据中获取 | 子接口名称。 |
|  | 指定路由器优先级（DRPRI） | 0 | - | “DRPRI”设置为“0”表示不参与DR和BDR的选举。为避免UEG被选为DR或BDR，建议将VNF“DRPRI”配置为0，对端配置为非0。- |
|  | OSPFv3共网段虚拟系统使能标志(VIRTUALSYSFLAG) | TRUE | - | - |
| **ADD OSPFV3IMPORTROUTE** | OSPFv3进程号(PROCID) | 6 | 已规划数据中获取 | - |
|  | 拓扑标识(TOPOID) | 0 | - |  |
|  | 协议号(PROTOCOL) | wlr | 固定取值 |  |
|  | 引入路由开销值配置(IMPTCOSTCFG) | TRUE | 本端规划 | 2个UPF是主备时，设置为“TRUE”；2个UPF是负荷分担关系时，设置为“FALSE”。 |
|  | 路径Cost值（COST） | 100 | 与对端协商 | 主备UPF引入路由的COST值。主UPF设置的COST值必须小于备UPF设置的COST值。 |
|  | 引入路由标签配置(IMPTTAGCFG) | FALSE | - | - |
|  | 引入路由类型配置 (IMPTTYPECFG) | FALSE | - |  |

## 操作步骤

1. 配置外联口的VPN实例。

   ```
   ADD L3VPNINST:VRFNAME="VPN_LocalDN";
   ADD VPNINSTAF:VRFNAME="VPN_LocalDN",AFTYPE=ipv6uni;
   ```

   一条通信路径上所有节点绑定的VPN实例要一致，才能正常通信，例如UEG逻辑接口、UEG外联口、网关上的VPN，否则从逻辑接口发出去的报文会查询路由失败。
2. 配置外联口IP地址。

   1. 查询接口名，确认可使用的外联口的接口类型和接口编号。

      ```
      LST INTERFACE:;
      ```
   2. 配置主接口的管理状态为up。

      ```
      MOD INTERFACE:IFNAME="Ethernet64/0/6",IFADMINSTATUS=up;
      MOD INTERFACE:IFNAME="Ethernet64/0/7",IFADMINSTATUS=up;
      ```
   3. 配置以太网子接口。

      ```
      ADD INTERFACE:IFNAME="Ethernet64/0/6.1";
      ADD INTERFACE:IFNAME="Ethernet64/0/7.1";
      ```
   4. 增加接口绑定VPN。

      ```
      ADD IPBINDVPN:IFNAME="Ethernet64/0/6.1",VRFNAME="VPN_LocalDN";
      ADD IPBINDVPN:IFNAME="Ethernet64/0/7.1",VRFNAME="VPN_LocalDN";
      ```
   5. 在以太网子接口上关联VLAN ID。

      ```
      ADD ETHSUBIF:IFNAME="Ethernet64/0/6.1",VLANTYPEVID=100;
      ADD ETHSUBIF:IFNAME="Ethernet64/0/7.1",VLANTYPEVID=200;
      ```

      子接口配置了VLAN，则需要在交换机、对接网关上调整VLAN的配置。
   6. 配置IPv6使能。

      ```
      SET IFIPV6ENABLE: IFNAME="Ethernet64/0/6.1", ENABLEFLAG=TRUE;
      SET IFIPV6ENABLE: IFNAME="Ethernet64/0/7.1", ENABLEFLAG=TRUE;
      ```
   7. 配置外联口IP地址。

      ```
      ADD IFIPV6ADDRESS:IFNAME="Ethernet64/0/6.1",IPV6ADDRESS="FC00::10C2",PREFIXLEN=123;
      ADD IFIPV6ADDRESS:IFNAME="Ethernet64/0/7.1",IPV6ADDRESS="FC00::10E2",PREFIXLEN=123;
      ```

      如果规划外联口使用IPv4v6双栈地址，则分别执行**ADD IFIPV4ADDRESS**和**ADD IFIPV6ADDRESS**对同一外联口配置IPv4和IPv6地址。
3. 配置OSPFv3路由数据。

   1. 创建OSPFv3进程。

      ```
      ADD OSPFV3:PROCID=6,VRFNAME="VPN_Access",ROUTERID="10.8.25.1",BFDALLINTFFLG=FALSE,VPNINSCAPSIMFLG=TRUE,VIRTUALSYSFLAG=TRUE;
      ```

      * UEG支持VPN多实例时，需要取消环路检查（参数“VPNINSCAPSIMFLG”配置为“TRUE”），否则会导致OSPFv3路由引入失败。
      * 路由器标识Router ID（“ROUTERID”）的选择策略：优选用户配置的Router ID，如果未配置，则选择OSPFv3进程所在VRF内或者公网内的最大接口IP地址。
      * FW不支持BFD，参数“BFDALLINTFFLG（使能BFD）”配置为“FALSE”。
      * 当OSPF路由配置共网段时，需要将参数“VIRTUALSYSFLAG（OSPF共网段虚拟系统使能标志）”配置为“TRUE”。
   2. 增加OSPFv3区域。

      ```
      ADD OSPFV3AREA: PROCID=6,AREAID="0.0.0.5", AREATYPE=NSSA;
      ```

      参数“AREATYPE（OSPFv3区域类型）”配置为“NSSA”或“Normal”时，都不需要配置Loopback地址。
   3. **（可选）**配置OSPFv3区域认证。

      **ADD OSPFV3AREAAUTH**: PROCID=OSPFv3进程号, AREAID=OSPFv3区域标识, AUTHENMODE=hmac-sha256, AUTHTEXTTYPE=cipher, AUTHTEXTMD5="密文验证密码",KEYID=密文验证字标识符;

      使用区域验证时，一个区域中所有设备的接口上所配置的认证模式和口令必须一致。
   4. 配置OSPFv3协议的接口属性。

      ```
      ADD OSPFV3INTERFACE:PROCID=6,AREAID="0.0.0.5",IFNAME="Ethernet64/0/6.1",DRPRI=0,VIRTUALSYSFLAG=TRUE, CFGROUTERIDFLAG=FALSE;
      ADD OSPFV3INTERFACE:PROCID=6,AREAID="0.0.0.5",IFNAME="Ethernet64/0/7.1",DRPRI=0,VIRTUALSYSFLAG=TRUE, CFGROUTERIDFLAG=FALSE;
      ```

      * 参数“NETWORKTYPE”（网络类型）选择“BROADCAST”、“NBMA”、“POINT-TO-POINT”、“POINT-TO-MULTIPOINT”或“P2MP-NONBROADCAST”。
      * 广播或NBMA网络中，根据此接口优先级选举DR和BDR路由器，“优先级”设置为“0”表示不参与DR和BDR的选举。为避免VNF被选为DR或BDR，建议将VNF“优先级”配置为0，对端配置为非0。
   5. **（可选）**配置OSPFv3接口验证参数。

      **ADD OSPFV3INTERFACEAUTH**: PROCID=OSPFv3进程号, AREAID=区域号, IFNAME="接口名称", AUTHENMODE=hmac-sha256, AUTHENTYPE=cipher, AUTHTEXTMD5="密文验证密码",KEYID=密文验证字标识符,INSTANCEID=实例号;

      参数“IFNAME”（接口名称）采用3.d中的接口名称。
   6. 设置OSPFv3引入路由类型。

      ```
      ADD OSPFV3IMPORTROUTE:PROCID=6,TOPOID=0,PROTOCOL=wlr,IMPTCOSTCFG=FALSE,IMPTTAGCFG=FALSE,IMPTTYPECFG=FALSE;
      ```

## 验证方法

1. 查看各网元间的路由连接是否正常。

   执行**PING**命令，查看UEG与对端设备间的路由连接是否正常。

   ```
   PING:IPVERSION=IPv6,VPNNAME="VPN_LocalDN",DESTIPV6ADDRESS="对端网关地址";
   ```

   如果使用了VPN组网，还需使用“VPN实例名称（VPNNAME）”指定VPN实例，这样才能验证VPN实例路由是否正常。

   * 如果收到对端网元的响应且响应报文中有成功收发包的个数，表明连接正常，调测结束。
   * 如果连续出现timeout，表明链路不通，请执行2。
2. 查看接口状态及信息是否与规划数据一致。

   **LST INTERFACE**:;

   * 如果一致，请执行3。
   * 如果不一致，请参考“操作步骤”重新配置。
3. 调测OSPFv3动态路由。
   1. 检查生成的OSPFv3路由是否与规划数据一致。

      **DSP OSPFV3ROUTING**:;
      * 如果一致，请执行3.b。
      * 如果不一致，请参考“操作步骤”重新配置，再次执行1。
   2. 检查接口是否已添加到OSPFv3区域中。

      **DSP OSPFV3INTERFACE**: PROCID=OSPFv3进程号;
      * 如果是，请执行3.c。
      * 如果否，请参考“操作步骤”重新配置，再次执行1。
   3. 检查OSPFv3邻居状态是否正常。

      邻居应包括邻居设备的ROUTER ID、接口的IP地址以及邻居的状态。

      **DSP OSPFV3PEER**: PROCID=OSPFv3进程号;
      * 如果是，请执行4。
      * 如果否，请参考“操作步骤”重新配置，再次执行1。
4. 收集信息并寻求技术支持。

   1. 执行**EXP MML**命令将当前配置数据导出为MML脚本文件并保存。
   2. 收集并保存上述所有查询信息。
   3. 查看并收集对端设备配置及接口状态信息。
   4. 收集归纳所有信息并联系华为技术支持解决。

版权所有 © 华为技术有限公司

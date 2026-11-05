# 配置动态路由OSPF（IPv4）

* 操作场景
* 必备事项
* 操作步骤
* 验证方法

## 操作场景

网关设备（如FW）不支持BFD时，UEG与对端设备可通过OSPF动态路由进行组网连接，该方式适用于IPv4组网的网络中。

图1是UEG与周边网元通过OSPF动态路由互通的组网示意。UEG与网关设备（如FW）运行动态路由协议而接入企业网络，UEG的配置请参考本页面，FW的配置请参考FW对应型号设备的产品文档。

**图1** OSPF动态路由组网

## 必备事项

前提条件

* 请阅读并熟悉特性IPFD-020501 支持OSPF特性概述。
* 具备管理员权限的操作人员已经登录华为操作维护系统（登录MAE客户端或登录OM Portal）。
* UEG与网络实体之间的网络环境已经构建完成。

数据

UEG使用OSPF动态路由与对端设备建立IP连接，采用OSPF协议收敛保证可靠性。

* 在UEG上配置OSPF动态路由与对端建立链路。
* 在UEG上推荐采用子接口的外联口与外部网络对接。
* 本页面以UEG通过FW与企业园区的服务器互通为例。

**如下数据仅为举例，请注意修改成局点规划的数据。**

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| **ADD L3VPNINST** | VPN实例名称（VRFNAME） | VPN\_LocalDN | 本端规划 | VPN实例全网统一规划，一条通信路径上所有节点绑定的VPN实例要一致，才能正常通信。 |
| **ADD VPNINSTAF** | 地址族类型（AFTYPE） | ipv4uni | - | IPv4组网场景下，该参数选择ipv4uni。 |
| **MOD INTERFACE** | 接口名称（IFNAME） | Ethernet64/0/6  Ethernet64/0/7 | 本端规划 | （UEG-M）请参考外联口介绍(刀片式服务器2U)进行规划。 |
| **ADD INTERFACE** | 子接口名字（IFNAME） | Ethernet64/0/6.1  Ethernet64/0/7.1 | 本端规划 | 免交换场景，使用非SR-IOV bonding组网，此处规划的是Ethernet子接口。 |
| **ADD IPBINDVPN** | VPN名字(VRFNAME) | VPN\_LocalDN | 已配置数据中获取 | - |
| **ADD ETHSUBIF** | VLAN类型子接口的VLAN ID（VLANTYPEVID） | 100  200 | 全网规划 | 此处以双平面为例。 |
| **ADD IFIPV4ADDRESS** | 接口IPv4地址（IFIPADDR） | 192.168.89.2  192.168.89.10 | 全网规划 | 如果规划外联口使用IPv4v6双栈地址，则分别执行**ADD IFIPV4ADDRESS**和**ADD IFIPV6ADDRESS**  对同一外联口配置IPv4和IPv6地址。  此处规划的IP地址是与网关互通的外联口IP。 |
|  | 接口IPv4地址掩码（SUBNETMASK） | 255.255.255.248 | 全网规划 |  |
| **ADD OSPF** | OSPF进程号(PROCID) | 6 | 本端规划 | - |
|  | VPN的名称(VRFNAME) | VPN\_LocalDN | 已配置数据中获取 |  |
|  | Schema路由器标识(SCHEMAROUID) | 192.168.35.210 | 全网规划 |  |
|  | 使能BFD（BFDALLINTFFLG） | FALSE | 全网规划 | 三层路由设备FW不支持BFD时，使用样例值。 |
| **ADD OSPFAREA** | 区域号（AREAID） | 0.0.0.5 | 与对端协商 | 两个接口若要建立邻居关系，则Area ID必须相同。 |
|  | 区域类型(AREATYPE) | Normal | 与对端协商 | 两个接口若要建立邻居关系，则Area Type必须相同。 |
| **ADD OSPFINTERFACE** | OSPF进程号(PROCID) | 6 | 已规划数据中获取 | - |
|  | 区域标识（AREAID） | 0.0.0.5 | 已规划数据中获取 |  |
|  | 接口名称（IFNAME） | Ethernet64/0/6.1  Ethernet64/0/7.1 | 已规划数据中获取 | 子接口名称。 |
|  | 指定路由器优先级（DRPRI） | 0 | - | “DRPRI”设置为“0”表示不参与DR和BDR的选举。为避免UEG被选为DR或BDR，建议将VNF“DRPRI”配置为0，对端配置为非0。 |
|  | OSPF共网段虚拟系统使能标志(VIRTUALSYSFLAG) | TRUE | - | - |
| **ADD OSPFNETWORK** | OSPF进程号(PROCID) | 6 | 已规划数据中获取 | “IPADDRESS”和“WILDCARDMASK”是在指定OSPF区域内的外联口所在的网段。  “WILDCARDMASK”是反掩码，相当于把IP地址的掩码反转（0变1，1变0）。 |
|  | 区域号（AREAID） | 0.0.0.5 | 已规划数据中获取 |  |
|  | 网段IP地址（IPADDRESS） | 192.168.89.0  192.168.89.8 | 已规划数据中获取 |  |
|  | 反掩码（WILDCARDMASK） | 0.0.0.7 | 已规划数据中获取 |  |
| **ADD OSPFIMPORTROUTE** | OSPF进程号(PROCID) | 6 | 已规划数据中获取 | - |
|  | 拓扑标识（TOPOID） | 0 | - |  |
|  | 协议分类 （PROTOCOL） | wlr | 固定取值 |  |
|  | 引入路由开销值配置（IMPTCOSTCFG） | TRUE | 本端规划 | 2个UPF是主备时，设置为“TRUE”；2个UPF是负荷分担关系时，设置为“FALSE”。 |
|  | 路径Cost值（COST） | 100 | 与对端协商 | 主备UPF引入路由的COST值。主UPF设置的COST值必须小于备UPF设置的COST值。 |
| **ADD INTERFACE** | 接口名（IFNAME） | LoopBack605 | 本端规划 | Loopback接口数据。  **ADD OSPFAREA**命令中的“区域类型(AREATYPE)”为“NSSA”时需要规划；“区域类型(AREATYPE)”为“Normal”时不需要规划。 |
| **ADD IPBINDVPN** | 接口名（IFNAME） | LoopBack605 | 已规划数据中获取 |  |
|  | VPN的名称(VRFNAME) | VPN\_LocalDN |  |  |
| **ADD IFIPV4ADDRESS** | 接口名（IFNAME） | LoopBack605 | 已规划数据中获取 |  |
|  | 接口IPv4地址（IFIPADDR） | 192.168.235.130 | 全网规划 |  |
|  | 接口IPv4地址掩码（SUBNETMASK） | 255.255.255.255 | 固定取值 |  |
| **ADD OSPFINTERFACE** | OSPF进程号(PROCID) | 6 | 已规划数据中获取 |  |
|  | 区域号（AREAID） | 0.0.0.5 |  |  |
|  | 接口名（IFNAME） | LoopBack605 |  |  |

## 操作步骤

1. 配置外联口的VPN实例。

   ```
   ADD L3VPNINST:VRFNAME="VPN_LocalDN";
   ADD VPNINSTAF:VRFNAME="VPN_LocalDN",AFTYPE=ipv4uni;
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
   6. 配置外联口IP地址。

      ```
      ADD IFIPV4ADDRESS:IFNAME="Ethernet64/0/6.1",IFIPADDR="192.168.89.2",SUBNETMASK="255.255.255.248";
      ADD IFIPV4ADDRESS:IFNAME="Ethernet64/0/7.1",IFIPADDR="192.168.89.10",SUBNETMASK="255.255.255.248";
      ```

      如果规划外联口使用IPv4v6双栈地址，则分别执行**ADD IFIPV4ADDRESS**和**ADD IFIPV6ADDRESS**对同一外联口配置IPv4和IPv6地址。
3. 配置OSPF路由数据。

   1. 创建OSPF进程。

      ```
      ADD OSPF:PROCID=6,VRFNAME="VPN_LocalDN",SCHEMAROUID="192.168.35.210",BFDALLINTFFLG=FALSE, LSAARRINTVFLAG=FALSE, LSAARRMAXINTV=1000, LSAARRSTARINTV=500, LSAARRHLDINTV=500,VPNINSCAPSIMFLG=TRUE,VIRTUALSYSFLAG=TRUE;
      ```

      * UEG支持VPN多实例时，需要取消环路检查（参数“VPNINSCAPSIMFLG”配置为“TRUE”），否则会导致OSPF路由引入失败。
      * 路由器标识Router ID（“SCHEMAROUID”）的选择策略：优选用户配置的Router ID，如果未配置，则选择OSPF进程所在VRF内或者公网内的最大接口IP地址。
      * FW不支持BFD，参数“BFDALLINTFFLG（使能BFD）”配置为“FALSE”。
      * 当OSPF路由配置共网段时，需要将参数“VIRTUALSYSFLAG（OSPF共网段虚拟系统使能标志）”配置为“TRUE”。
   2. 增加OSPF区域。

      ```
      ADD OSPFAREA:PROCID=6,AREAID="0.0.0.5", AREATYPE=Normal, MAXCOSTFLAG=FALSE;
      ```
   3. **（可选）**配置OSPF区域认证。

      **ADD OSPFAREAAUTH**: PROCID=进程号, AREAID=区域号, AUTHENMODE=认证模式;

      * 参数“AUTHENMODE”（认证模式），选择“keychain”、“simple”、“md5”、“hmac-sha256”或“hmac-md5”。
      * 使用区域验证时，一个区域中所有设备的接口上所配置的认证模式和口令必须一致。
   4. 配置OSPF协议的接口属性。

      ```
      ADD OSPFINTERFACE:PROCID=6,AREAID="0.0.0.5",IFNAME="Ethernet64/0/6.1",DRPRI=0,VIRTUALSYSFLAG=TRUE, CFGROUTERIDFLAG=FALSE, MAXCOSTFLAG=FALSE;
      ADD OSPFINTERFACE:PROCID=6,AREAID="0.0.0.5",IFNAME="Ethernet64/0/7.1",DRPRI=0,VIRTUALSYSFLAG=TRUE, CFGROUTERIDFLAG=FALSE, MAXCOSTFLAG=FALSE;
      ```

      * 参数“NETWORKTYPE”（网络类型）选择“broadcast”、“nbma”、“p2p”或“p2mp”。
      * 广播或NBMA网络中，根据此接口优先级选举DR和BDR路由器，“优先级”设置为“0”表示不参与DR和BDR的选举。为避免UEG被选为DR或BDR，建议将VNF“优先级”配置为0，对端配置为非0。
   5. 增加运行OSPF协议的接口。

      ```
      ADD OSPFNETWORK:PROCID=6,AREAID="0.0.0.5",IPADDRESS="192.168.89.0",WILDCARDMASK="0.0.0.7";
      ADD OSPFNETWORK:PROCID=6,AREAID="0.0.0.5",IPADDRESS="192.168.89.8",WILDCARDMASK="0.0.0.7";
      ```
   6. **（可选）**配置OSPF接口验证参数。

      根据不同的接口验证类型选择不同的配置。

      * 不配置认证模式。

        **ADD OSPFINTERFACEAUTH**: PROCID=进程号, AREAID=区域号, IFNAME="接口名称", AUTHENMODE=null;
      * 配置认证模式。

        **ADD OSPFINTERFACEAUTH**: PROCID=进程号, AREAID=区域号, IFNAME="接口名称", AUTHENMODE=认证模式;

        + 参数“AUTHENMODE”（认证模式）可以选择“keychain”、“hmac-sha256”、“simple”、“md5”或“hmac-md5”。
        + 参数“IFNAME”（接口名称）采用3.d中的接口名称。
   7. 设置OSPF引入路由类型。

      ```
      ADD OSPFIMPORTROUTE:PROCID=6,TOPOID=0,PROTOCOL=wlr,IMPTCOSTCFG=FALSE,IMPTTAGCFG=FALSE,IMPTTYPECFG=FALSE;
      ```
4. **（可选）**3中**ADD OSPFAREA**命令的参数“AREATYPE（区域类型）”配置为“NSSA”时，设置Loopback接口。

   如果参数“AREATYPE（区域类型）”配置为“NSSA”时，需要配置Loopback地址，这样设备会自动选取该Loopback地址作为FA。当有其他设备存在多条开销值相同的路径到NSSA设备时，可以形成负载分担。

   1. 配置Loopback接口。

      ```
      ADD INTERFACE:IFNAME="LoopBack605";
      ```
   2. 增加Loopback接口绑定VPN。

      ```
      ADD IPBINDVPN:IFNAME="LoopBack605",VRFNAME="VPN_LocalDN";
      ```
   3. 配置Loopback的IPv4地址。

      ```
      ADD IFIPV4ADDRESS:IFNAME="LoopBack605",IFIPADDR="192.168.235.130",SUBNETMASK="255.255.255.255",ADDRTYPE=main;
      ```
   4. 使能Loopback接口到OSPF进程的区域下。
      * 通过**ADD OSPFINTERFACE**配置。

        ```
        ADD OSPFINTERFACE: PROCID=6, AREAID="0.0.0.5", IFNAME="LoopBack605";
        ```
      * 通过**ADD OSPFNETWORK**配置。

        ```
        ADD OSPFNETWORK: PROCID=6, AREAID="0.0.0.5", IPADDRESS="192.168.235.130", WILDCARDMASK=0.0.0.0;
        ```

      推荐使用**ADD OSPFINTERFACE**命令进行配置。使用**ADD OSPFNETWORK**命令配置时，请将“WILDCARDMASK(反掩码)”设置为“0.0.0.0”。

      参数“PROCID（进程号）”与3中的“PROCID（进程号）”的取值相一致；参数“AREAID（区域号）”与3中的“AREAID（区域号）”的取值相一致。

## 验证方法

1. 查看各网元间的路由连接是否正常。

   执行**PING**命令，查看UEG与对端设备间的路由连接是否正常。

   ```
   PING:IPVERSION=IPv4,VPNNAME="VPN_LocalDN",DESTIPV4ADDRESS="对端网关地址";
   ```

   如果使用了VPN组网，还需使用“VPN实例名称（VPNNAME）”指定VPN实例，这样才能验证VPN实例路由是否正常。

   * 如果收到对端网元的响应且响应报文中有成功收发包的个数，表明连接正常，调测结束。
   * 如果连续出现timeout，表明链路不通，请执行2。
2. 查看接口状态及信息是否与规划数据一致。

   **LST INTERFACE**:;

   * 如果一致，请执行3。
   * 如果不一致，请参考“操作步骤”重新配置。
3. 调测OSPF动态路由。
   1. 检查生成的OSPF路由是否与规划数据一致。

      **DSP OSPFROUTING**:;
      * 如果一致，请执行3.b。
      * 如果不一致，请参考“操作步骤”重新配置，再次执行1。
   2. 检查接口是否已添加到OSPF区域中。

      **DSP OSPFINTERFACE**: PROCID=OSPF进程号;
      * 如果是，请执行3.c。
      * 如果否，请参考“操作步骤”重新配置，再次执行1。
   3. 检查OSPF邻居状态是否正常。

      邻居应包括邻居设备的ROUTER ID、接口的IP地址以及邻居的状态。

      **DSP OSPFPEER**: PROCID=OSPF进程号;
      * 如果是，请执行4。
      * 如果否，请参考“操作步骤”重新配置，再次执行1。
4. 收集信息并寻求技术支持。

   1. 执行**EXP MML**命令将当前配置数据导出为MML脚本文件并保存。
   2. 收集并保存上述所有查询信息。
   3. 查看并收集对端设备配置及接口状态信息。
   4. 收集归纳所有信息并联系华为技术支持解决。

版权所有 © 华为技术有限公司
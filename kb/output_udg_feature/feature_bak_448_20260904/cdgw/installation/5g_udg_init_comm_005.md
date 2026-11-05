# 基于BGP over OSPFv3路由手动部署边缘UDG配置实例（IPv6）

- 操作场景
- 必备事项
- 操作步骤

## 操作场景

本任务实例实现以下场景配置：

UDG与对端设备（gNodeB/eNodeB、SGSN、PSA UPF/PGW-U、SMF/PGW-C/SGW-C）通过OSPFv3动态路由绑定动态BFD实现网络互通。

- 网络形态：2/3/4/5G融合网络
- 网元形态：边缘UDG
- 路由协议：BGP over OSPFv3动态路由手动部署
- 组网IP格式：IPv6组网
- 接入用户：IPv4v6双栈用户

**说明** 

- 本地分流场景下边缘UDG一般承担ULCL/BP分流和本地PSA锚点网关，为融合部署形态。
- 普通场景下边缘UDG可能承担I-UPF/S-GW角色，将用户桥接连接到PSA锚点网关上，为独立网元形态。

  本文以此场景为例说明部署配置脚本。
- 对于IPv4v6双栈用户接入，则与外部DN网络连接的Gi/SGi/N6接口的vNIC外联口需要规划IPv4v6双栈地址。

  本文场景的边缘UDG不涉及与外部DN网络连接，因此IPv4v6双栈用户接入和其他IP类型用户接入的配置无差异。

实际场景中请根据网络组网确定网元的形态和配置。

## 必备事项

前提条件

- 请了解UDG各类接口的类型及命名规范，可参见逻辑接口介绍。
- IP路由组网和业务接口配置子任务在前述章节已有详细描述，可参见配置VNF侧IP路由数据（无NP卡\_非SDN）和配置业务接口数据。本文针对典型的任务场景举例说明整网脚本配置。

数据

可参考各子任务的数据规划准备。

文档

获取网设LLD文档。

## 操作步骤

1. 全局激活BFD。
   1. 全局激活BFD。

      ```
      SET BFD: BFDENABLE=TRUE;
      ```
2. 配置UDG到与对端设备无线侧(R)AN（gNodeB/eNodeB）的IP路由数据。
   1. 配置VPN实例。

      ```
      ADD L3VPNINST:VRFNAME="VPN_Access";
      ADD VPNINSTAF:VRFNAME="VPN_Access",AFTYPE=ipv6uni;
      ```
   2. 配置外联口信息。

      1. 查看接口状态及信息。

         ```
         LST INTERFACE:;
         ```
      2. 配置主接口的管理状态为up。

         ```
         MOD INTERFACE:IFNAME="Ethernet66/0/4",IFADMINSTATUS=up;
         MOD INTERFACE:IFNAME="Ethernet66/0/5",IFADMINSTATUS=up;
         MOD INTERFACE:IFNAME="Ethernet67/0/4",IFADMINSTATUS=up;
         MOD INTERFACE:IFNAME="Ethernet67/0/5",IFADMINSTATUS=up;
         ```
      3. 配置Eth-trunk子接口。

         ```
         ADD INTERFACE:IFNAME="Eth-trunk1";
         ADD INTERFACE:IFNAME="Eth-trunk2";
         MOD TRUNKIF:IFNAME="Eth-Trunk1",WORKMODE=Manual;
         MOD TRUNKIF:IFNAME="Eth-Trunk2",WORKMODE=Manual;
         ADD TRUNKMEMBER:TRUNKIFNAME="Eth-trunk1",MEMBERIFNAME="Ethernet66/0/4";
         ADD TRUNKMEMBER:TRUNKIFNAME="Eth-trunk1",MEMBERIFNAME="Ethernet66/0/5";
         ADD TRUNKMEMBER:TRUNKIFNAME="Eth-trunk2",MEMBERIFNAME="Ethernet67/0/4";
         ADD TRUNKMEMBER:TRUNKIFNAME="Eth-trunk2",MEMBERIFNAME="Ethernet67/0/5";
         ADD INTERFACE:IFNAME="Eth-trunk1.1";
         ADD INTERFACE:IFNAME="Eth-trunk1.2";
         ADD INTERFACE:IFNAME="Eth-trunk2.1";
         ADD INTERFACE:IFNAME="Eth-trunk2.2";
         ```
      4. 增加接口绑定VPN。

         ```
         ADD IPBINDVPN:IFNAME="Eth-trunk1.1",VRFNAME="VPN_Access";
         ADD IPBINDVPN:IFNAME="Eth-trunk1.2",VRFNAME="VPN_Access";
         ADD IPBINDVPN:IFNAME="Eth-trunk2.1",VRFNAME="VPN_Access";
         ADD IPBINDVPN:IFNAME="Eth-trunk2.2",VRFNAME="VPN_Access";
         ```
      5. 在Eth-trunk子接口上关联VLAN ID。

         ```
         ADD ETHSUBIF:IFNAME="Eth-trunk1.1",VLANTYPEVID=105;
         ADD ETHSUBIF:IFNAME="Eth-trunk1.2",VLANTYPEVID=205;
         ADD ETHSUBIF:IFNAME="Eth-trunk2.1",VLANTYPEVID=105;
         ADD ETHSUBIF:IFNAME="Eth-trunk2.2",VLANTYPEVID=205;
         ```
      6. 配置IPv6使能。

         ```
         SET IFIPV6ENABLE: IFNAME="Eth-trunk1.1", ENABLEFLAG=TRUE;
         SET IFIPV6ENABLE: IFNAME="Eth-trunk1.2", ENABLEFLAG=TRUE;
         SET IFIPV6ENABLE: IFNAME="Eth-trunk2.1", ENABLEFLAG=TRUE;
         SET IFIPV6ENABLE: IFNAME="Eth-trunk2.2", ENABLEFLAG=TRUE;
         ```
      7. 配置外联口的IP地址。

         ```
         ADD IFIPV6ADDRESS:IFNAME="Eth-trunk1.1",IPV6ADDRESS="FC00::1002",PREFIXLEN=121;
         ADD IFIPV6ADDRESS:IFNAME="Eth-trunk1.2",IPV6ADDRESS="FC00::1082",PREFIXLEN=121;
         ADD IFIPV6ADDRESS:IFNAME="Eth-trunk2.1",IPV6ADDRESS="FC00::1003",PREFIXLEN=121;
         ADD IFIPV6ADDRESS:IFNAME="Eth-trunk2.2",IPV6ADDRESS="FC00::1083",PREFIXLEN=121;
         ```
   3. 配置OSPFv3路由。

      1. 创建OSPFv3进程。

         ```
         ADD OSPFV3:PROCID=6,VRFNAME="VPN_Access",ROUTERID="10.8.25.1",BFDALLINTFFLG=TRUE,VPNINSCAPSIMFLG=TRUE,VIRTUALSYSFLAG=TRUE;
         ```
      2. 增加OSPFv3区域。

         根据不同的验证类型选择不同的区域配置。

         - 不指定验证类型。

           ```
           ADD OSPFV3AREA:PROCID=6,AREAID="0.0.0.5";
           ```

           **MOD OSPFV3AREA**:PROCID=OSPFv3进程号, AREAID=OSPFv3区域标识, AREATYPE=OSPFv3区域类型;

           **说明** 

           参数“AREATYPE（区域类型）”配置为“NSSA”或“Normal”时，都不需要配置Loopback地址。
         - 指定验证类型。

           **ADD OSPFV3AREAAUTH**: PROCID=OSPFv3进程号, AREAID=OSPFv3区域标识, AUTHENMODE=hmac-sha256, AUTHTEXTTYPE=cipher, AUTHTEXTMD5="密文验证密码",KEYID=密文验证字标识符;
      3. 配置OSPFv3协议的接口属性。

         ```
         ADD OSPFV3INTERFACE:PROCID=6,AREAID="0.0.0.5",IFNAME="Eth-trunk1.1",DRPRI=0,VIRTUALSYSFLAG=TRUE;
         ADD OSPFV3INTERFACE:PROCID=6,AREAID="0.0.0.5",IFNAME="Eth-trunk1.2",DRPRI=0,VIRTUALSYSFLAG=TRUE;
         ADD OSPFV3INTERFACE:PROCID=6,AREAID="0.0.0.5",IFNAME="Eth-trunk2.1",DRPRI=0,VIRTUALSYSFLAG=TRUE;
         ADD OSPFV3INTERFACE:PROCID=6,AREAID="0.0.0.5",IFNAME="Eth-trunk2.2",DRPRI=0,VIRTUALSYSFLAG=TRUE;
         ```
      4. 设置OSPFv3引入路由类型。

         ```
         ADD OSPFV3IMPORTROUTE:PROCID=6,TOPOID=0,PROTOCOL=wlr,IMPTCOSTCFG=FALSE,IMPTTAGCFG=FALSE,IMPTTYPECFG=FALSE;
         ```
3. 配置UDG到与对端设备核心侧UPF/PGW-U（PSA UPF/PGW-U）的IP路由数据。
   1. 配置VPN实例。

      ```
      ADD L3VPNINST:VRFNAME="VPN_Sc";
      ADD VPNINSTAF:VRFNAME="VPN_Sc",AFTYPE=ipv6uni;
      ```
   2. 配置外联口信息。

      1. 查询接口名，确认IPU上可使用的外联口的接口类型和接口编号。

         ```
         LST INTERFACE:;
         ```
      2. 配置主接口的管理状态为up。

         ```
         MOD INTERFACE:IFNAME="Ethernet66/0/6",IFADMINSTATUS=up;
         MOD INTERFACE:IFNAME="Ethernet66/0/7",IFADMINSTATUS=up;
         MOD INTERFACE:IFNAME="Ethernet67/0/6",IFADMINSTATUS=up;
         MOD INTERFACE:IFNAME="Ethernet67/0/7",IFADMINSTATUS=up;
         ```
      3. 配置Eth-trunk子接口。

         ```
         ADD INTERFACE:IFNAME="Eth-trunk3";
         ADD INTERFACE:IFNAME="Eth-trunk4";
         MOD TRUNKIF:IFNAME="Eth-Trunk3",WORKMODE=Manual;
         MOD TRUNKIF:IFNAME="Eth-Trunk4",WORKMODE=Manual;
         ADD TRUNKMEMBER:TRUNKIFNAME="Eth-trunk3",MEMBERIFNAME="Ethernet66/0/6";
         ADD TRUNKMEMBER:TRUNKIFNAME="Eth-trunk3",MEMBERIFNAME="Ethernet66/0/7";
         ADD TRUNKMEMBER:TRUNKIFNAME="Eth-trunk4",MEMBERIFNAME="Ethernet67/0/6";
         ADD TRUNKMEMBER:TRUNKIFNAME="Eth-trunk4",MEMBERIFNAME="Ethernet67/0/7";
         ADD INTERFACE:IFNAME="Eth-trunk3.1";
         ADD INTERFACE:IFNAME="Eth-trunk3.2";
         ADD INTERFACE:IFNAME="Eth-trunk4.1";
         ADD INTERFACE:IFNAME="Eth-trunk4.2";
         ```
      4. 配置接口绑定VPN。

         ```
         ADD IPBINDVPN:IFNAME="Eth-trunk3.1",VRFNAME="VPN_Sc";
         ADD IPBINDVPN:IFNAME="Eth-trunk3.2",VRFNAME="VPN_Sc";
         ADD IPBINDVPN:IFNAME="Eth-trunk4.1",VRFNAME="VPN_Sc";
         ADD IPBINDVPN:IFNAME="Eth-trunk4.2",VRFNAME="VPN_Sc";
         ```
      5. 在Eth-trunk子接口上关联VLAN ID。

         ```
         ADD ETHSUBIF:IFNAME="Eth-trunk3.1",VLANTYPEVID=107;
         ADD ETHSUBIF:IFNAME="Eth-trunk3.2",VLANTYPEVID=207;
         ADD ETHSUBIF:IFNAME="Eth-trunk4.1",VLANTYPEVID=107;
         ADD ETHSUBIF:IFNAME="Eth-trunk4.2",VLANTYPEVID=207;
         ```
      6. 配置IPv6使能。

         ```
         SET IFIPV6ENABLE: IFNAME="Eth-trunk3.1", ENABLEFLAG=TRUE;
         SET IFIPV6ENABLE: IFNAME="Eth-trunk3.2", ENABLEFLAG=TRUE;
         SET IFIPV6ENABLE: IFNAME="Eth-trunk4.1", ENABLEFLAG=TRUE;
         SET IFIPV6ENABLE: IFNAME="Eth-trunk4.2", ENABLEFLAG=TRUE;
         ```
      7. 配置外联口的IP地址。

         ```
         ADD IFIPV6ADDRESS:IFNAME="Eth-trunk3.1",IPV6ADDRESS="FC00::2002",PREFIXLEN=121;
         ADD IFIPV6ADDRESS:IFNAME="Eth-trunk3.2",IPV6ADDRESS="FC00::2082",PREFIXLEN=121;
         ADD IFIPV6ADDRESS:IFNAME="Eth-trunk4.1",IPV6ADDRESS="FC00::2003",PREFIXLEN=121;
         ADD IFIPV6ADDRESS:IFNAME="Eth-trunk4.2",IPV6ADDRESS="FC00::2083",PREFIXLEN=121;
         ```
   3. 配置OSPFv3动态路由数据。

      1. 创建OSPFv3进程。

         ```
         ADD OSPFV3:PROCID=8,VRFNAME="VPN_Sc",ROUTERID="10.8.27.1",BFDALLINTFFLG=TRUE,VPNINSCAPSIMFLG=TRUE,VIRTUALSYSFLAG=TRUE;
         ```
      2. 增加OSPFv3区域。

         ```
         ADD OSPFV3AREA:PROCID=8,AREAID="0.0.0.7";
         ```
      3. 配置OSPFv3协议的接口属性。

         ```
         ADD OSPFV3INTERFACE:PROCID=8,AREAID="0.0.0.7",IFNAME="Eth-trunk3.1",DRPRI=0,VIRTUALSYSFLAG=TRUE;
         ADD OSPFV3INTERFACE:PROCID=8,AREAID="0.0.0.7",IFNAME="Eth-trunk3.2",DRPRI=0,VIRTUALSYSFLAG=TRUE;
         ADD OSPFV3INTERFACE:PROCID=8,AREAID="0.0.0.7",IFNAME="Eth-trunk4.1",DRPRI=0,VIRTUALSYSFLAG=TRUE;
         ADD OSPFV3INTERFACE:PROCID=8,AREAID="0.0.0.7",IFNAME="Eth-trunk4.2",DRPRI=0,VIRTUALSYSFLAG=TRUE;
         ```
      4. 设置OSPFv3引入路由类型。

         ```
         ADD OSPFV3IMPORTROUTE:PROCID=8,TOPOID=0,PROTOCOL=wlr,IMPTCOSTCFG=FALSE,IMPTTAGCFG=FALSE,IMPTTYPECFG=FALSE;
         ```
4. 配置UDG到与对端设备控制面网元（SMF/PGW-C/SGW-C）IP路由数据。
   1. 配置VPN实例。

      ```
      ADD L3VPNINST:VRFNAME="VPN_Signaling";
      ADD VPNINSTAF:VRFNAME="VPN_Signaling",AFTYPE=ipv6uni;
      ```
   2. 配置外联口信息。

      1. 查询接口名，确认IPU上可使用的外联口的接口类型和接口编号。

         ```
         LST INTERFACE:;
         ```
      2. 配置Eth-trunk子接口。

         ```
         ADD INTERFACE:IFNAME="Eth-trunk3.3";
         ADD INTERFACE:IFNAME="Eth-trunk3.4";
         ADD INTERFACE:IFNAME="Eth-trunk4.3";
         ADD INTERFACE:IFNAME="Eth-trunk4.4";
         ```
      3. 配置接口绑定VPN。

         ```
         ADD IPBINDVPN:IFNAME="Eth-trunk3.3",VRFNAME="VPN_Signaling";
         ADD IPBINDVPN:IFNAME="Eth-trunk3.4",VRFNAME="VPN_Signaling";
         ADD IPBINDVPN:IFNAME="Eth-trunk4.3",VRFNAME="VPN_Signaling";
         ADD IPBINDVPN:IFNAME="Eth-trunk4.4",VRFNAME="VPN_Signaling";
         ```
      4. 以太网子接口上关联VLAN ID。

         ```
         ADD ETHSUBIF:IFNAME="Eth-trunk3.3",VLANTYPEVID=108;
         ADD ETHSUBIF:IFNAME="Eth-trunk3.4",VLANTYPEVID=208;
         ADD ETHSUBIF:IFNAME="Eth-trunk4.3",VLANTYPEVID=108;
         ADD ETHSUBIF:IFNAME="Eth-trunk4.4",VLANTYPEVID=208;
         ```
      5. 配置IPv6使能。

         ```
         SET IFIPV6ENABLE: IFNAME="Eth-trunk3.3", ENABLEFLAG=TRUE;
         SET IFIPV6ENABLE: IFNAME="Eth-trunk3.4", ENABLEFLAG=TRUE;
         SET IFIPV6ENABLE: IFNAME="Eth-trunk4.3", ENABLEFLAG=TRUE;
         SET IFIPV6ENABLE: IFNAME="Eth-trunk4.4", ENABLEFLAG=TRUE;
         ```
      6. 配置外联口的IP地址。

         ```
         ADD IFIPV6ADDRESS:IFNAME="Eth-trunk3.3",IPV6ADDRESS="FC00::3002",PREFIXLEN=121;
         ADD IFIPV6ADDRESS:IFNAME="Eth-trunk3.4",IPV6ADDRESS="FC00::3082",PREFIXLEN=121;
         ADD IFIPV6ADDRESS:IFNAME="Eth-trunk4.3",IPV6ADDRESS="FC00::3003",PREFIXLEN=121;
         ADD IFIPV6ADDRESS:IFNAME="Eth-trunk4.4",IPV6ADDRESS="FC00::3083",PREFIXLEN=121;
         ```
   3. 配置OSPFv3动态路由数据。

      1. 创建OSPFv3进程。

         ```
         ADD OSPFV3:PROCID=9,VRFNAME="VPN_Signaling",ROUTERID="10.8.28.1",BFDALLINTFFLG=TRUE,VPNINSCAPSIMFLG=TRUE,VIRTUALSYSFLAG=TRUE;
         ```
      2. 增加OSPFv3区域。

         ```
         ADD OSPFV3AREA:PROCID=9,AREAID="0.0.0.8";
         ```
      3. 配置OSPFv3协议的接口属性。

         ```
         ADD OSPFV3INTERFACE:PROCID=9,AREAID="0.0.0.8",IFNAME="Eth-trunk3.3",DRPRI=0,VIRTUALSYSFLAG=TRUE;
         ADD OSPFV3INTERFACE:PROCID=9,AREAID="0.0.0.8",IFNAME="Eth-trunk3.4",DRPRI=0,VIRTUALSYSFLAG=TRUE;
         ADD OSPFV3INTERFACE:PROCID=9,AREAID="0.0.0.8",IFNAME="Eth-trunk4.3",DRPRI=0,VIRTUALSYSFLAG=TRUE;
         ADD OSPFV3INTERFACE:PROCID=9,AREAID="0.0.0.8",IFNAME="Eth-trunk4.4",DRPRI=0,VIRTUALSYSFLAG=TRUE;
         ```
      4. 设置OSPFv3引入路由类型。

         ```
         ADD OSPFV3IMPORTROUTE:PROCID=9,TOPOID=0,PROTOCOL=wlr,IMPTCOSTCFG=FALSE,IMPTTAGCFG=FALSE,IMPTTYPECFG=FALSE;
         ```
5. 全局激活BGP。

   ```
   SET BGP: BGPENABLE=TRUE, ASNUM="60001";
   ```
6. 配置BGP Loopback接口地址。
   1. 配置BGP Loopback接口。

      ```
      ADD INTERFACE:IFNAME="Loopback1";
      ADD INTERFACE:IFNAME="Loopback2";
      ADD INTERFACE:IFNAME="Loopback3";
      ```
   2. 配置接口绑定VPN。

      ```
      ADD IPBINDVPN:IFNAME="Loopback1",VRFNAME="VPN_Access";
      ADD IPBINDVPN:IFNAME="Loopback2",VRFNAME="VPN_Sc";
      ADD IPBINDVPN:IFNAME="Loopback3",VRFNAME="VPN_Signaling";
      ```
   3. 配置IPv6使能。

      ```
      SET IFIPV6ENABLE: IFNAME="Loopback1", ENABLEFLAG=TRUE;
      SET IFIPV6ENABLE: IFNAME="Loopback2", ENABLEFLAG=TRUE;
      SET IFIPV6ENABLE: IFNAME="Loopback3", ENABLEFLAG=TRUE;
      ```
   4. 配置接口IP地址。

      ```
      ADD IFIPV6ADDRESS:IFNAME="Loopback1",IPV6ADDRESS="FC00:2013::1",PREFIXLEN=128;
      ADD IFIPV6ADDRESS:IFNAME="Loopback2",IPV6ADDRESS="FC00:2014::1",PREFIXLEN=128;
      ADD IFIPV6ADDRESS:IFNAME="Loopback3",IPV6ADDRESS="FC00:2015::1",PREFIXLEN=128;
      ```
7. 配置BGP。
   1. 增加BGP VPN实例。

      ```
      ADD BGPVRF: VRFNAME="VPN_Access", DEFAULTAFTYPE=noaf, ROUTERID="10.90.6.160";
      ADD BGPVRF: VRFNAME="VPN_Sc", DEFAULTAFTYPE=noaf, ROUTERID="10.90.7.160";
      ADD BGPVRF: VRFNAME="VPN_Signaling", DEFAULTAFTYPE=noaf, ROUTERID="10.90.8.160";
      ```
   2. 增加BGP VPN实例地址族。UDG对接2个负荷分担的路由设备时，“MAXIMUMLOADBALANCE”设置为“2”。

      ```
      ADD BGPVRFAF: VRFNAME="VPN_Access", AFTYPE=ipv6uni, MAXIMUMLOADBALANCE=2;
      ADD BGPVRFAF: VRFNAME="VPN_Sc", AFTYPE=ipv6uni, MAXIMUMLOADBALANCE=2;
      ADD BGPVRFAF: VRFNAME="VPN_Signaling", AFTYPE=ipv6uni, MAXIMUMLOADBALANCE=2;
      ```
   3. 增加BGP对等体。“EBGPMAXHOP”不小于到Peer之间的实际跳数，此处以10为例。

      ```
      ADD BGPPEER: VRFNAME="VPN_Access", ADDRESSTYPE=ipv6, PEERADDRV6="FC00:2013::2", REMOTEAS="60002", LOCALIFADDR="FC00:2013::1", LOCALIFNAME="Loopback1", EBGPMAXHOP=10;
      ADD BGPPEER: VRFNAME="VPN_Sc", ADDRESSTYPE=ipv6, PEERADDRV6="FC00:2014::2", REMOTEAS="70002", LOCALIFADDR="FC00:2014::1", LOCALIFNAME="Loopback2", EBGPMAXHOP=10;
      ADD BGPPEER: VRFNAME="VPN_Signaling", ADDRESSTYPE=ipv6, PEERADDRV6="FC00:2015::2", REMOTEAS="80002", LOCALIFADDR="FC00:2015::1", LOCALIFNAME="Loopback3", EBGPMAXHOP=10;
      ```
   4. 增加BGP引入路由。

      ```
      ADD IMPORTROUTE: VRFNAME="VPN_Access",AFTYPE=ipv6uni, IMPORTPROTOCOL=wlr, MEDENABLE=FALSE;
      ADD IMPORTROUTE: VRFNAME="VPN_Sc",AFTYPE=ipv6uni, IMPORTPROTOCOL=wlr, MEDENABLE=FALSE;
      ADD IMPORTROUTE: VRFNAME="VPN_Signaling",AFTYPE=ipv6uni, IMPORTPROTOCOL=wlr, MEDENABLE=FALSE;
      ```

      **说明** 

      由于BGP协议自身不能发现路由，所以需要引入其他协议的路由（如OSPFv3、静态路由或WLR等）注入到BGP路由表中，从而将这些路由在AS之内和AS之间传播。
8. 配置逻辑接口数据。
   1. 配置Sa/N3/S1-U逻辑接口。

      1. 配置Sa/N3/S1-U逻辑接口所属的VPN实例。

         ```
         ADD VPNINST: VPNINSTANCE ="VPN_Access";
         ```
      2. 配置Sa/N3/S1-U逻辑接口。

         ```
         ADD LOGICINF:NAME="Saif1/1/0",IPVERSION=IPV6,IPV6ADDRESS1="FC00:2000::1",IPV6PREFIXLEN1=128,VPNINSTANCE="VPN_Access";
         ```
   2. 配置Pa（N9a/S5-P/S8-P/S2b/Gn-U/Gp-U）逻辑接口。

      1. 配置Pa（N9a/S5-P/S8-P/S2b/Gn-U/Gp-U）逻辑接口所属的VPN实例。

         ```
         ADD VPNINST: VPNINSTANCE ="VPN_Pa";
         ```
      2. 配置Pa（N9a/S5-P/S8-P/S2b/Gn-U/Gp-U）逻辑接口。

         ```
         ADD LOGICINF:NAME="Paif1/1/0",IPVERSION=IPV6,IPV6ADDRESS1="FC00:2001::1",IPV6PREFIXLEN1=128,VPNINSTANCE="VPN_Pa";
         ```
   3. 配置N4（N4/Sxa/Sxb）逻辑接口。

      1. 配置N4（N4/Sxa/Sxb）逻辑接口所属的VPN实例。

         ```
         ADD VPNINST: VPNINSTANCE="VPN_Signaling";
         ```
      2. 配置N4（N4/Sxa/Sxb）逻辑接口。

         ```
         ADD LOGICINF: NAME="N4if1/0/0", IPVERSION=IPV6, IPV6ADDRESS1="FC00:2002::1", IPV6PREFIXLEN1=128, VPNINSTANCE="VPN_Signaling";
         ```
      3. 配置UDG信息。

         ```
         SET UPINFO: HOSTNAME="UP_001";
         ```
9. 配置会话接入数据。
   1. 配置APN/DNN实例。

      ```
      ADD VPNINST: VPNINSTANCE ="VPN_Internet";
      ADD APN:APN="apn-op",HASVPNIPV6=ENABLE,VPNINSTANCEIPV6="VPN_Internet";
      ```
   2. 配置UDG分配地址，此处以基于APN/DNN分配地址为例。其他网元分配地址时，请跳过本步骤。

      ```
      ADD POOL:POOLNAME="testpool",POOLTYPE=LOCAL,HASVPN=ENABLE,VPNINSTANCE="VPN_Internet";
      ADD SECTION:POOLNAME="testpool",SECTIONNUM=1,IPVERSION=IPV6,V6PREFIXSTART="FC00::20C2",V6PREFIXEND="FC00:20DE",V6PREFIXLENGTH=64;
      ADD POOLGROUP: POOLGRPNAME="poolgroup1", IPV4ALLOCPRIALG=ENABLE, IPV6ALLOCPRIALG=ENABLE;
      ADD POOLBINDGROUP: POOLGROUPNAME="poolgroup1", POOLNAME="testpool", PRIORITY=10;
      ADD POOLGRPMAP: MAPPINGNAME="mapping1", APN="apn-op", POOLGROUPNAME="poolgroup1";
      SET IPALLOCRULE: FIRSTRULESW=ENABLE, FIRSTRULE=APN-1&LOCATION-0&SMF-0, SECONDRULESW=DISABLE, THIRDRULESW=DISABLE;
      ```
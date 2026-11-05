# 配置S6a接口数据

* 操作场景
* 必备事项
* 操作步骤
* 验证方法

## 操作场景

当运营商在部署分组交换网，新增MME或HSS时，在配置完成MME到HSS的路由数据后，可通过配置S6a接口数据建立MME到HSS的逻辑连接。

S6a接口是EPC系统中，MME和HSS之间的接口。用于提供用户的签约数据管理和鉴权相关的功能。在漫游场景下，MME还需要通过S6a接口连接到用户归属地的HSS。

**图1** S6a接口协议栈

由于UEG L模式下面分两种模式，一种模式下的UEG包含UDM/AUSF/HSS网元功能，另一种模式则相反，不包含UDM/AUSF/HSS网元功能，需要和中心侧网络UDM/AUSF/HSS进行对接。

园区风筝L有两种部署模式：

* L1：MME与中心侧两个HSS对接，此场景需要运营商规划业务IP地址，VRF。数据会出园区传输。
* L2：MME仅选择与园区内本端DC的HSS对接，这样使用园区统一规划的IP地址，VRF。数据在园区内封闭传输。

除此以外，L1和L2模式中S6a接口的配置命令无差异。

以下配置数据以及步骤均以UEG双DC组网场景的配置规划为例进行介绍。

## 必备事项

前提条件

* 具备管理员权限的操作人员已经登录华为操作维护系统（登录U2020/MAE客户端或登录OM Portal）。

* 已完成组网路由配置。
* 如果本接口采用IPv6组网，则需要开通逻辑接口支持IPv6特性，即加载对应的License项“81203214 LKV3G5V6LI01 逻辑接口支持IPv6”。
* 已经获取网设LLD文档。

数据

本文以IPv4组网为例说明。

* 如果是IPv6组网，请将逻辑接口地址规划为IPv6地址。
* 如果是IPv4v6双栈组网，则对逻辑接口配置双栈地址即可。

**如下数据仅为举例，请注意修改成局点规划的数据。**

| 类别 | 参数名称 | DC1取值样例 | DC2取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- | --- |
| ****ADD SERVICEIP**** | IP版本（IPVERSION） | IPv4 |  | 参见“水平网设LLD文档 ”。 | 配置业务IP参数。 |
|  | 业务IPv4地址（SERVICEIPV4） | 10.10.1.1  10.10.1.2 | 10.10.1.17  10.10.1.18 |  | 由于S6a接口传输层的SCTP协议支持多连接，且同一连接也存在多路径，可以配置多个业务IP地址支持多条链路，此处以两个业务IP地址为例。 |
|  | VPN实例名称（VPNINSTNAME） | VPN\_CN |  |  | 本文S6a接口组网以L2模式为例说明。UEG风筝形态内部接口组网时，使用园区统一规划的VPN。 |
| ADD CPSCTPPARA | SCTP协议参数索引（SCTPPARAINDEX） | 2 |  |  | S6a接口的SCTP协议参数与S1–MME接口的SCTP协议参数分开配置，便于后续局点搬迁或扩容时，不影响互联网元配置。可以通过****LST CPSCTPPARA****来查询已存在的SCTP协议参数记录。 |
| **SET DMFUNC** | 重连定时器（s）（RECONNTIMER） | 6 |  |  | 配置Diameter路由重连定时器。 |
| ****ADD CPDMLE**** | 本地实体索引（LOINDEX） | 1 |  |  | 配置Diameter本地信息。  如果已经存在DMLE，请使用现有的DMLE，无需添加。 |
|  | 本地实体主机名（LOHSTNAME） | mme1.epc.mnc000.mcc123.3gppnetwork.org | mme2.epc.mnc000.mcc123.3gppnetwork.org |  |  |
|  | 本地实体域名（LORLMNAME） | epc1.mnc000.mcc123.3gppnetwork.org | epc2.mnc000.mcc123.3gppnetwork.org |  |  |
|  | 本地实体名（LOINFONAME） | usn |  |  |  |
| ADD CPDMPE | 对端实体索引（PEERIDX） | 1  2 |  |  | 配置Diameter对端信息。 |
|  | 对端主机名（PEERHTNAM） | hss1.epc.mnc000.mcc123.3gppnetwork.org  hss2.epc.mnc000.mcc123.3gppnetwork.org |  |  |  |
|  | 对端实体名（PEERNAM） | HSS |  |  |  |
|  | 节点支持的应用（APPCAP） | S6a/S6d-1&S13-0&SLg-0&T6a/T6ai/T6b/T6bi-0 |  |  |  |
| ADD CPDMLKS | Diameter链路集索引（LINKSIDX） | 1  2 |  |  | 配置Diameter链路集。 |
|  | 本地实体索引（LOCALIDX） | 1 |  |  |  |
|  | 对端实体索引（PEERIDX） | 1  2 |  |  |  |
|  | 选路模式（LSSELMODE） | SELMODE\_ACTIVE |  |  |  |
|  | 链路集名称（LINKSNAM） | to-HSS |  |  |  |
| ADD CPDMLNK | vpn名称（VPNNAME） | VPN\_CN |  |  | 配置Diameter链路。  说明：  当UEG在煤矿等场景下使用2U1选型时，仅需要配置5000端口的链路；当UEG在核电等场景下使用4U4选型时，需额外配置5001端口的链路。 |
|  | 链路索引（LINKIDX） | 0  1  2  3 |  |  |  |
|  | IP地址类型（IPTYPE） | TPTADDR\_TYPE\_IPV4 |  |  |  |
|  | 本端IP地址1（LOCALIPV4\_1） | 10.10.1.1 | 10.10.1.17 |  |  |
|  | 本端IP地址2（LOCALIPV4\_2） | 10.10.1.2 | 10.10.1.18 |  |  |
|  | 本端端口（LOCALPORT） | 5000  5001 | 5000  5001 |  |  |
|  | 对端IP地址1（PEERIPV4\_1） | 10.11.1.3  10.11.1.4 |  |  |  |
|  | 对端IP地址2（PEERIPV4\_2） | 10.11.2.3  10.11.2.4 |  |  |  |
|  | 对端端口（PEERPORT） | 5000  5001 |  |  |  |
|  | C/S模式（CLIORSER） | DIAM\_CONN\_CLIENT |  |  |  |
|  | Diameter链路集索引（LINKSIDX） | 1  2 |  |  |  |
|  | SCTP协议参数索引（SCTPINDX） | 2 |  |  |  |
|  | 链路名称（LINKNAM） | dmlink0  dmlink1  dmlink2  dmlink3 |  |  |  |
| ****ADD DMHOSTRT**** | 路由索引（ROUTEIDX） | 1  2 |  |  | * 当HSS采用分布式组网时，MME需要配置多条到HSS不同FE的主机路由，同时将这些不同的主机路由加入同一个路由组。  HSS从逻辑上划分为BE（Back End）和FE（Front End）两部分，实现用户数据与业务逻辑处理的分离。 BE即USCDB（Unified Subscriber Center DataBase），负责存储用户数据，提供用户数据的增加、删除、更新和查询服务，为FE提供有效的数据支撑。 FE负责信令接入和业务逻辑处理，从BE获得数据服务。 * 当同一路由组内存在多条路由，可以采用不同的方式选择Diameter对端，如轮选、主从、优先级权重、IMSI指定优选等。  需要按照优先级和权重方式选择对端时，选路模式为优先级权重，即RSELMODE=SELMODE\_PRIORITY\_WEIGHT。  详细请参考激活基于权重/优先级的Diameter负荷分担。 * PEERSEL（目的实体选择方式）取值PEER\_INDEX时，需要填写PEERIDX（对端实体索引）；PEERSEL（目的实体选择方式）取值PEER\_HOST\_NAME时，需要填写PEERHTNAM（对端主机名）。这里以选择PEER\_INDEX为例。 |
|  | 选路模式（RSELMODE） | SELMODE\_PRIORITY\_WEIGHT |  |  |  |
|  | 目的实体选择方式（PEERSEL） | PEER\_INDEX |  |  |  |
|  | 对端实体索引（PEERIDX） | 1  2 |  |  |  |
|  | 路由名称（ROUTENAM） | mme |  |  |  |
| **ADD CPDMRT** | 路由索引（ROUTEIDX） | 3  4 |  |  | 配置到DRA的Diameter域路由。 |
|  | 应用名称（APPNAM） | S6A/S6D |  |  |  |
|  | 选路模式（RSELMODE） | SELMODE\_ROUND\_ROBIN |  |  |  |
|  | 目的实体域名（REALMNAME） | huawei.com.cn |  |  |  |
|  | 对端实体索引（PEERIDX） | 1  2 |  |  |  |
|  | 路由名称（ROUTENAM） | diamt\_route1 |  |  |  |
| ****ADD DMRTGRP**** | 路由组索引（GRPIDX） | 1  2  3  4 |  |  | MME与HSS直连时，建议Diameter路由的“路由优选模式”设置成优先选择主机路由 。 |
|  | 路由模式（RTMODE） | HOST\_ROUTE |  |  |  |
|  | 路由优选模式（RTPRIMODE） | HOST\_ROUTE\_PREFER |  |  |  |
|  | 路由索引（路由索引） | 1  2 |  |  |  |
|  | 路由组名称（ROUTEGRPNAM） | To\_HSS |  |  |  |
| ****ADD IMSIHSS**** | IMSI前缀（IMSIPRE） | 12303 |  |  | 配置IMSI与HSS的映射关系。  用户可以根据该映射关系查找IMSI归属于哪个HSS的信息。 |
|  | HSS域名（HSSRLM） | epc1.mnc000.mcc123.3gppnetwork.org  epc2.mnc000.mcc123.3gppnetwork.org |  |  |  |
|  | Diameter路由组索引（GRPIDX） | 1  2 |  |  |  |
| ****ADD S1USRSECPARA**** | IMSI前缀（IMSIPRE） | DEFAULT |  |  | 关闭周期性鉴权功能。  MME与中心侧HSS对接时，为了减少传输中断触发的周期性鉴权功能，精简鉴权事件，仅保留**初始注册、移动性Inter注册**中开启强制鉴权功能，其余鉴权事件均关闭。  所有风筝方案保持一致处理。 |
|  | 安全策略（SECPLC） | 12303 |  |  |  |
|  | 高级选项（OPTIONAL） | YES |  |  |  |
|  | 鉴权事件（AUTHEVENT） | ATTACH-1& INTRA\_TAU-0&INTER\_TAU-1&DETACH-  0&SERVICE\_REQUEST-0&PROD\_TAU-0&SYSTEM\_CHA  NGE\_INTRA\_TAU-0&INTRA\_TAU\_AFTER\_HANDOVER-  0&INTER\_TAU\_AFTER\_HANDOVER-0 |  |  |  |
|  | 鉴权周期（AUTHPERIOD） | 0 |  |  |  |

文档

获取网设LLD文档。

## 操作步骤

1. 进入“MML命令行-UEG”窗口。
2. 配置S6a接口业务IP。

   ```
   //DC1
   ADD SERVICEIP: IPVERSION=IPv4, SERVICEIPV4="10.10.1.1", VPNINSTNAME="VPN_CN"; 
   ADD SERVICEIP: IPVERSION=IPv4, SERVICEIPV4="10.10.1.2", VPNINSTNAME="VPN_CN"; 
   //DC2
   ADD SERVICEIP: IPVERSION=IPv4, SERVICEIPV4="10.10.1.17", VPNINSTNAME="VPN_CN"; 
   ADD SERVICEIP: IPVERSION=IPv4, SERVICEIPV4="10.10.1.18", VPNINSTNAME="VPN_CN";
   ```
3. 配置S6a接口基于IP的宽带信令SCTP偶联配置的协议参数。

   ```
   //DC1
   ADD CPSCTPPARA:SCTPPARAINDEX=2;
   //DC2
   ADD CPSCTPPARA:SCTPPARAINDEX=2;
   ```
4. **可选：**查看Diameter配置中“重连定时器（RECONNTIMER）”是否符合要求。如果“重连定时器（RECONNTIMER）”参数不为6s，则设置为6s。

   在Diameter链路建立后，如果发生链路迁移或者重建，MME可以主动发送INIT消息给对端设备请求建链，可以使得链路不中断。但是如果对端设备不支持在UP状态时处理INIT消息，可能会导致链路中断，重建时间变长，具体时长取决于配置的“重连定时器（RECONNTIMER）”参数。

   该定时器系统默认为30s，在目前灰度升级、扩容缩容等发生链路迁移场景下，造成链路中断时间过长，因此根据对端设备处理方式，建议将该参数配置为6s。

   ```
   //DC1
   SET DMFUNC:RECONNTIMER=6;
   //DC2
   SET DMFUNC:RECONNTIMER=6;
   ```
5. 增加Diameter本端信息 。

   ```
   //DC1
   ADD CPDMLE:LOINDEX=1,LOHSTNAME="mme1.epc.mnc000.mcc123.3gppnetwork.org",LORLMNAME="epc1.mnc000.mcc123.3gppnetwork.org",LOINFONAME="usn";
   //DC2
   ADD CPDMLE:LOINDEX=1,LOHSTNAME="mme2.epc.mnc000.mcc123.3gppnetwork.org",LORLMNAME="epc2.mnc000.mcc123.3gppnetwork.org",LOINFONAME="usn";
   ```
6. 增加Diameter对端信息。

   负荷分担容灾模式时，本UEG中的MME会通过S6a接口从另一UEG中的HSS接收cancel location报文，此场景需要配置本UEG中MME与另一UEG中HSS的对接。主备容灾模式时，仅需要配置本UEG中MME与HSS对接。

   ```
   //DC1
   ADD CPDMPE:PEERIDX=1,PEERHTNAM="hss1.epc.mnc000.mcc123.3gppnetwork.org",PEERNAM="HSS",APPCAP=S6a/S6d-1&S13-0&SLg-0&T6a/T6ai/T6b/T6bi-0;
   ADD CPDMPE:PEERIDX=2,PEERHTNAM="hss2.epc.mnc000.mcc123.3gppnetwork.org",PEERNAM="HSS",APPCAP=S6a/S6d-1&S13-0&SLg-0&T6a/T6ai/T6b/T6bi-0;
   //DC2
   ADD CPDMPE:PEERIDX=1,PEERHTNAM="hss1.epc.mnc000.mcc123.3gppnetwork.org",PEERNAM="HSS",APPCAP=S6a/S6d-1&S13-0&SLg-0&T6a/T6ai/T6b/T6bi-0;
   ADD CPDMPE:PEERIDX=2,PEERHTNAM="hss2.epc.mnc000.mcc123.3gppnetwork.org",PEERNAM="HSS",APPCAP=S6a/S6d-1&S13-0&SLg-0&T6a/T6ai/T6b/T6bi-0;
   ```
7. 配置Diameter链路集信息。

   负荷分担容灾模式时，本UEG中的MME会通过S6a接口从另一UEG中的HSS接收cancel location报文，此场景需要配置本UEG中MME与另一UEG中HSS的对接。主备容灾模式时，仅需要配置本UEG中MME与HSS对接。

   ```
   //DC1
   ADD CPDMLKS:LINKSIDX=1,LOCALIDX=1,PEERIDX=1,LSSELMODE=SELMODE_ACTIVE,LINKSNAM="to-HSS";
   ADD CPDMLKS:LINKSIDX=2,LOCALIDX=1,PEERIDX=2,LSSELMODE=SELMODE_ACTIVE,LINKSNAM="to-HSS";
   //DC2
   ADD CPDMLKS:LINKSIDX=1,LOCALIDX=1,PEERIDX=1,LSSELMODE=SELMODE_ACTIVE,LINKSNAM="to-HSS";
   ADD CPDMLKS:LINKSIDX=2,LOCALIDX=1,PEERIDX=2,LSSELMODE=SELMODE_ACTIVE,LINKSNAM="to-HSS";
   ```
8. 配置Diameter链路信息。

   负荷分担容灾模式时，本UEG中的MME会通过S6a接口从另一UEG中的HSS接收cancel location报文，此场景需要配置本UEG中MME与另一UEG中HSS的对接。主备容灾模式时，仅需要配置本UEG中MME与HSS对接。

   ```
   //DC1
   ADD CPDMLNK:VPNNAME="VPN_CN",LINKIDX=0,IPTYPE=TPTADDR_TYPE_IPV4,LOCALIPV4_1="10.10.1.1", LOCALIPV4_2="10.10.1.2",LOCALPORT=5000,PEERIPV4_1="10.11.1.3", PEERIPV4_2="10.11.2.3", PEERPORT=5000 ,CLIORSER=DIAM_CONN_CLIENT,LINKSIDX=1,SCTPINDX=2,LINKNAM="dmlink0"; 
   ADD CPDMLNK:VPNNAME="VPN_CN",LINKIDX=1,IPTYPE=TPTADDR_TYPE_IPV4,LOCALIPV4_1="10.10.1.1", LOCALIPV4_2="10.10.1.2",LOCALPORT=5000,PEERIPV4_1="10.11.1.4", PEERIPV4_2="10.11.2.4", PEERPORT=5000,CLIORSER=DIAM_CONN_CLIENT,LINKSIDX=2,SCTPINDX=2,LINKNAM="dmlink1";
   //DC2
   ADD CPDMLNK:VPNNAME="VPN_CN",LINKIDX=0,IPTYPE=TPTADDR_TYPE_IPV4,LOCALIPV4_1="10.10.1.17", LOCALIPV4_2="10.10.1.18",LOCALPORT=5000,PEERIPV4_1="10.11.1.3", PEERIPV4_2="10.11.2.3", PEERPORT=5000,CLIORSER=DIAM_CONN_CLIENT,LINKSIDX=1,SCTPINDX=2,LINKNAM="dmlink0"; 
   ADD CPDMLNK:VPNNAME="VPN_CN",LINKIDX=1,IPTYPE=TPTADDR_TYPE_IPV4,LOCALIPV4_1="10.10.1.17", LOCALIPV4_2="10.10.1.18",LOCALPORT=5000,PEERIPV4_1="10.11.1.4", PEERIPV4_2="10.11.2.4", PEERPORT=5000,CLIORSER=DIAM_CONN_CLIENT,LINKSIDX=2,SCTPINDX=2,LINKNAM="dmlink1";
   ```

   当UEG在核电等场景下使用4U4选型时，需额外配置以下5001端口的链路，非4U4选型下无需配置5001端口的链路。

   ```
   //DC1
   ADD CPDMLNK:VPNNAME="VPN_CN",LINKIDX=2,IPTYPE=TPTADDR_TYPE_IPV4,LOCALIPV4_1="10.10.1.2", LOCALIPV4_2="10.10.1.1",LOCALPORT=5001,PEERIPV4_1="10.11.2.3", PEERIPV4_2="10.11.1.3", PEERPORT=5001 ,CLIORSER=DIAM_CONN_CLIENT,LINKSIDX=1,SCTPINDX=2,LINKNAM="dmlink2";
   ADD CPDMLNK:VPNNAME="VPN_CN",LINKIDX=3,IPTYPE=TPTADDR_TYPE_IPV4,LOCALIPV4_1="10.10.1.2", LOCALIPV4_2="10.10.1.1",LOCALPORT=5001,PEERIPV4_1="10.11.2.4", PEERIPV4_2="10.11.1.4", PEERPORT=5001,CLIORSER=DIAM_CONN_CLIENT,LINKSIDX=2,SCTPINDX=2,LINKNAM="dmlink3";
   //DC2
   ADD CPDMLNK:VPNNAME="VPN_CN",LINKIDX=2,IPTYPE=TPTADDR_TYPE_IPV4,LOCALIPV4_1="10.10.1.18", LOCALIPV4_2="10.10.1.17",LOCALPORT=5001,PEERIPV4_1="10.11.2.3", PEERIPV4_2="10.11.1.3", PEERPORT=5001,CLIORSER=DIAM_CONN_CLIENT,LINKSIDX=1,SCTPINDX=2,LINKNAM="dmlink2"; 
   ADD CPDMLNK:VPNNAME="VPN_CN",LINKIDX=3,IPTYPE=TPTADDR_TYPE_IPV4,LOCALIPV4_1="10.10.1.18", LOCALIPV4_2="10.10.1.17",LOCALPORT=5001,PEERIPV4_1="10.11.2.4", PEERIPV4_2="10.11.1.4", PEERPORT=5001,CLIORSER=DIAM_CONN_CLIENT,LINKSIDX=2,SCTPINDX=2,LINKNAM="dmlink3";
   ```
9. **可选：**配置Diameter主机路由并将主机路由加入路由组。UDM部署在园区网络时，MME仅配置到同UEG内的HSS，对接时执行此步骤。
   1. 配置到HSS的主机路由。

      ```
      //DC1
      ADD DMHOSTRT:ROUTEIDX=1,RSELMODE=SELMODE_PRIORITY_WEIGHT,PEERSEL=PEER_INDEX,PEERIDX=1,ROUTENAM="mme"; 
      //DC2
      ADD DMHOSTRT:ROUTEIDX=2,RSELMODE=SCPDMRTELMODE_PRIORITY_WEIGHT,PEERSEL=PEER_INDEX,PEERIDX=2,ROUTENAM="mme";
      ```
   2. 将主机路由加入Diameter路由组中。

      ```
      //DC1
      ADD DMRTGRP: GRPIDX=1, RTMODE=HOST_ROUTE, RTPRIMODE=HOST_ROUTE_PREFER, ROUTEIDX=1, ROUTEGRPNAM="To_HSS"; 
      //DC2
      ADD DMRTGRP: GRPIDX=2, RTMODE=HOST_ROUTE, RTPRIMODE=HOST_ROUTE_PREFER, ROUTEIDX=2, ROUTEGRPNAM="To_HSS";
      ```
10. **可选：**可选：配置Diameter域路由并加入路由组。通过DRA和HSS对接时需执行此步骤，例如需要和中心侧HSS对接时可执行此步骤。

    负荷分担容灾模式时，本UEG中的MME会通过S6a接口从另一UEG中的HSS接收cancel location报文，此场景需要配置本UEG中MME与另一UEG中HSS的对接。主备容灾模式时，仅需要配置本UEG中MME与HSS对接。

    1. 配置Diameter域路由。

       ```
       //DC1
       ADD CPDMRT: ROUTEIDX=3,APPNAM=S6A/S6D,RSELMODE=SELMODE_ROUND_ROBIN, REALMNAME="epc1.mnc000.mcc123.3gppnetwork.org", PEERIDX=1, ROUTENAM="diamt_route1";
       ADD CPDMRT: ROUTEIDX=4,APPNAM=S6A/S6D,RSELMODE=SELMODE_ROUND_ROBIN, REALMNAME="epc2.mnc000.mcc123.3gppnetwork.org", PEERIDX=2, ROUTENAM="diamt_route1";
       //DC2
       ADD CPDMRT: ROUTEIDX=3,APPNAM=S6A/S6D,RSELMODE=SELMODE_ROUND_ROBIN, REALMNAME="epc1.mnc000.mcc123.3gppnetwork.org", PEERIDX=1, ROUTENAM="diamt_route1";
       ADD CPDMRT: ROUTEIDX=4,APPNAM=S6A/S6D,RSELMODE=SELMODE_ROUND_ROBIN, REALMNAME="epc2.mnc000.mcc123.3gppnetwork.org", PEERIDX=2, ROUTENAM="diamt_route1";
       ```
    2. 配置Diameter路由组。如果配置了域路由，该路由需要加入路由组，与主机路由在同一个路由组。路由索引不需要配置，路由优先模式是优选主机路由，系统可以通过域名自动关联域路由。

       ```
       //DC1
       ADD DMRTGRP: GRPIDX=3, RTMODE=REALM_ROUTE, RTPRIMODE=REALM_ROUTE_PREFER, ROUTEIDX=3, PEERIDX=1, ROUTEGRPNAM="dra";
       ADD DMRTGRP: GRPIDX=4, RTMODE=REALM_ROUTE, RTPRIMODE=REALM_ROUTE_PREFER, ROUTEIDX=4, PEERIDX=2, ROUTEGRPNAM="dra";
       //DC2
       ADD DMRTGRP: GRPIDX=3, RTMODE=REALM_ROUTE, RTPRIMODE=REALM_ROUTE_PREFER, ROUTEIDX=3, PEERIDX=1, ROUTEGRPNAM="dra";
       ADD DMRTGRP: GRPIDX=4, RTMODE=REALM_ROUTE, RTPRIMODE=REALM_ROUTE_PREFER, ROUTEIDX=4, PEERIDX=2, ROUTEGRPNAM="dra";
       ```
11. 配置IMSI与HSS的映射关系，用户可以根据该映射关系查找IMSI归属于哪个HSS的信息。

    ```
    //DC1
    ADD IMSIHSS:IMSIPRE="46000",HSSRLM="epc1.mnc000.mcc123.3gppnetwork.org",GRPIDX=1;
    //DC2
    ADD IMSIHSS:IMSIPRE="46000",HSSRLM="epc2.mnc000.mcc123.3gppnetwork.org",GRPIDX=2;
    ```
12. **可选：**配置IPsec。园区DC的MME和中心侧网络的HSS对接时，可以配置IPsec增强数据报文传输安全性。
13. 关闭周期性鉴权。

    ```
    //DC1
    ADD S1USRSECPARA: IMSIPRE= "DEFAULT", SECPLC=AUTHANDPROTECTED,OPTIONAL= YES, AUTHEVENT= ATTACH-1&INTRA_TAU-0&INTER_TAU-1&DETACH-0&SERVICE_REQUEST-0&PROD_TAU-0&SYSTEM_CHANGE_INTRA_TAU-0&INTRA_TAU_AFTER_HANDOVER-0&INTER_TAU_AFTER_HANDOVER-0, AUTHPERIOD=0;
    //DC2
    ADD S1USRSECPARA: IMSIPRE= "DEFAULT", SECPLC=AUTHANDPROTECTED,OPTIONAL= YES, AUTHEVENT= ATTACH-1&INTRA_TAU-0&INTER_TAU-1&DETACH-0&SERVICE_REQUEST-0&PROD_TAU-0&SYSTEM_CHANGE_INTRA_TAU-0&INTRA_TAU_AFTER_HANDOVER-0&INTER_TAU_AFTER_HANDOVER-0, AUTHPERIOD=0;
    ```

## 验证方法

1. 进入“MML命令行-UEG”窗口。
2. 查询当前配置的本地实体信息。

   ****LST CPDMLE****: LOINDEX="本地实体索引";

   ****DSP CPDMLE****: LOINDEX="本地实体索引";

   * **预期结果：**显示所有已经配置本地实体的配置信息、状态信息。

     ```
     %%LST CPDMLE: LOINDEX=0;%% 
     RETCODE = 0  操作成功。  

     操作结果如下 
     ------------   
       本地实体索引  =  0 
     本地实体主机名  =  mme0.huawei.com.cn   
       本地实体域名  =  huawei.com.cn         
             产品名  =  mme     
         本地实体名  =  mme 
     (结果个数 = 1) 
     ---    END
     ```

     ```
     %%DSP CPDMLE:;%% 
     RETCODE = 0  操作成功。  

     输出结果如下 
     ------------ 
     本地实体索引  =  0   
       本地实体名  =  mme     
         实体状态  =  正常 
     (结果个数 = 1) 
     ---    END
     ```
   * **异常结果：**异常处理过程参见**ALM-80593 Diameter对等端不可达**。
3. 验证MME能够正确查询对端实体状态。

   ****LST CPDMPE****: PEERIDX="对端实体索引";

   ****DSP CPDMPE****: PEERIDX="对端实体索引";

   * **预期结果：**显示所有已经配置对端实体的配置信息、状态信息。

     ```
     %%LST CPDMPE:;%% 
     RETCODE = 0  操作成功。
       
     操作结果如下 
     ------------ 
     对端实体索引    对端主机名              对端实体名    节点支持的应用         对端拥塞避免开关  
     0               hss0.huawei.com.cn      hss0          S6a/S6d & S13 & SLg    关闭             
     1               hss1.huawei.com.cn      hss1          S6a/S6d & S13 & SLg    关闭             
     (结果个数 = 2)
     ---    END
     ```

     ```
     %%DSP CPDMPE:;%% 
     RETCODE = 0  操作成功。  

     输出结果如下 
     ------------ 
     对端实体索引    对端实体名    实体状态  
     0               hss0          正常     
     1               hss1          正常     
     (结果个数 = 2) 
     ---    END
     ```
   * **异常结果：**异常处理过程参见**ALM-80593 Diameter对等端不可达**。
4. 验证MME能够正确查询Diameter链路集状态。

   ****LST CPDMLKS****: LINKSIDX="Diameter链路集索引";

   ****DSP CPDMLKS****: LINKSIDX="Diameter链路集索引";

   * **预期结果：**显示已经配置Diameter链路集的配置信息、状态信息。

     ```
     %%LST CPDMLKS: LINKSIDX=0;%% 
     RETCODE = 0  操作成功。  

     操作结果如下 
     ------------ 
     Diameter链路集索引  =  0       
           本地实体索引  =  0       
           对端实体索引  =  0           
               选路模式  =  轮选         
             链路集名称  =  Robin0 
     (结果个数 = 1) 
     ---    END
     ```

     ```
     %%DSP CPDMLKS: LINKSIDX=0;%% 
     RETCODE = 0  操作成功。  

     输出结果如下 
     ------------ 
     Diameter链路集索引  =  0         
             链路集名称  =  Robin0         
             链路集状态  =  正常 
     (结果个数 = 1) 
     ---    END
     ```
   * **异常结果：**异常处理过程参见**ALM-80591 Diameter链路故障**。
5. 验证MME能够正确查询Diameter链路状态。

   ****LST CPDMLNK****: LINKIDX="链路索引";

   ****DSP CPDMLNK****: LINKIDX="链路索引";

   * **预期结果：**显示已经配置Diameter链路的配置信息、状态信息。

     ```
     %%LST CPDMLNK: LINKIDX=0;%% 
     RETCODE = 0  操作成功  

     输出结果如下： 
     --------------            
               链路索引  =  0         
                vpn名称  =  VPN_CN       
             IP地址类型  =  IPv4         
               协议类型  =  SCTP        
              本地地址1  =  10.2.15.10        
              本地地址2  =  255.255.255.255       
             本地端口号  =  3868        
              对端地址1  =  192.168.15.16         
              对端地址2  =  255.255.255.255       
             对端端口号  =  3868          
                C/S模式  =  服务器端       
     Diameter链路集索引  =  0 
       SCTP协议参数索引  =  0         
               链路名称  =  To-HSS0 
       交叉路径是否可用  =  否 
     (结果个数 = 1)
     ```

     ```
     %%DSP CPDMLNK: LINKIDX=0;%% 
     RETCODE = 0  操作成功  

     输出结果如下： 
     -------------- 
     链路索引  =  0 
      RU名称   = VSU1 
      进程号   =  0 
     链路名称  =  To-HSS0 
     链路状态  =  正常 
     (结果个数 = 1)
     ```
   * **异常结果：**异常处理过程参见**ALM-80591 Diameter链路故障**。
6. 验证MME能够正确查询Diameter路由状态。

   ****LST DMHOSTRT****: ROUTEIDX="路由索引";

   ****LST DMRTGRP****: GRPIDX="路由组索引";

   （可选）****LST CPDMRT****: ROUTEIDX="路由索引";

   （可选）****DSP CPDMRT****: ROUTEIDX="路由索引";

   * **预期结果：**显示已经配置Diameter路由的配置信息、状态信息。

     ```
     %%LST DMHOSTRT:;%% 
     RETCODE = 0  操作成功。  

     操作结果如下 
     ------------         
             路由索引  =  0         
             应用名称  =  S6a/S6d         
             选路模式  =  优先级权重 
     目的实体选择方式  =  对端索引     
         对端实体索引  =  0       
           对端主机名  =  NULL         
             路由名称  =  DRA           
               优先级  =  1             
                 权重  =  1 
     (结果个数 = 1) 
     ---    END
     ```

     ```
     %%LST DMRTGRP: GRPIDX=7;%% 
     RETCODE = 0  操作成功。
       
     操作结果如下 
     ------------ 
     路由组索引    路由模式    路由优选模式    路由索引    对端实体索引    路由组名称  
     7             域路由      优选主机路由    1031        NULL            noname     
     7             主机路由    优选主机路由    7           NULL            noname     
     (结果个数 = 2) 
     ---    END
     ```

     ```
     %%LST CPDMRT: ROUTEIDX=0;%% 
     RETCODE = 0  操作成功。  

     操作结果如下 
     ------------     
         路由索引  =  0    
         应用名称  =  S6a/S6d 
     是否默认路由  =  否     
         选路模式  =  轮选 
     目的实体域名  =  hss0 
     对端实体索引  =  1     
         路由名称  =  dmrt2hss1       
           优先级  =  NULL         
             权重  =  NULL         
             描述  =  noname 
     (结果个数 = 1) 
     ---    END
     ```

     ```
     %%DSP CPDMRT: ROUTEIDX=0;%% 
     RETCODE = 0  操作成功。  

     输出结果如下 
     ------------ 
     路由索引  =  0 
     路由名称  =  dmrt2hss1 
     路由状态  =  正常 
     (结果个数 = 1) 
     ---    END
     ```
   * **异常结果：**异常处理过程参见**ALM-80592 Diameter路由不可用**。
7. 验证MME能够正确查询IMSI与HSS的映射关系。

   ****LST IMSIHSS****: IMSIPRE="IMSI前缀";

   * **预期结果：**正确显示-已经配置IMSI与HSS的映射关系的配置信息。

     ```
     %%LST IMSIHSS: IMSIPRE="3080115018";%% 
     RETCODE = 0  操作成功。  

     IMSI和HSS映射表 
     ---------------           
               IMSI前缀  =  3080115018            
                HSS域名  =  epc.mnc000.mcc123.3gppnetwork.org 
     Diameter路由组索引  =  NULL       
           移动网络名称  =  noname 
     (结果个数 = 1) 
     ---    END
     ```
8. 业务测试。

   进行业务测试前，需要首先完成MME与eNodeB、SGW、HSS的链路配置。

   进行业务测试的终端必须是在对接的HSS中开户。

   使用手机浏览网页，指定的APN由调测的HSS负责接入。

   1. **创建用户跟踪任务**。

      参数选择如下：

      * IMSI/MSISDN/IMEI：被跟踪用户的IMSI、MSISDN或者IMEI。
      * 其他参数：选择默认值。
   2. **创建接口跟踪任务**。

      链路索引：MME与HSS配置的链路索引号。
   3. 用户开机附着。
   4. **可选：**查看S6a接口跟踪结果。
   5. 查看用户跟踪结果。

      **预期结果：**

      用户附着成功，可以在Message Direction处看到UDM模块与DIAM模块、MME和HSS之间有消息交互。

      此功能用于快速定位问题和解决故障，在使用过程中不可避免的使用到用户的某些个人数据，如IMSI、IP地址。该功能提供了假名化的处理方式。建议您遵从国家的相关法律执行该任务，并采取足够的措施以确保用户的个人数据受到充分的保护，例如在U2020上将假名化开关打开、处理完毕后将保存跟踪记录的文件夹进行删除等。

      * **异常结果：**

        观察不到MME与HSS之间、UDM模块与DIAM模块之间的消息。或观察到MME与HSS之间的消息result code信元不为diameter\_success。查询用户MM上下文。
   6. 查询用户MM上下文。

      **DSP COMMMCTX**: QUERYOPT=BYIMSI, IMSI=IMSI;

      * **预期结果：**

        可以查询到用户的MM上下文，并接状态为EMM-IDLE或是EMM-CONNECT状态。
      * **异常结果：**

        查询不到用户的MM上下文。

版权所有 © 华为技术有限公司
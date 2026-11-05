# 配置到HSS的数据

- 操作场景
- 必备事项
- 操作步骤
- 验证方法

## 操作场景

当运营商在部署分组交换网，新增MME或HSS时，在配置完成MME到HSS的路由数据后，可通过配置S6a接口数据建立MME到HSS的逻辑连接。不同场景的推荐配置方式见表1。

| 操作场景                  | 配置方式                                                           |
|:----------------------|:---------------------------------------------------------------|
| 漫游场景                  | 方式一：本地用户优先使用MME直连的HSS，配置指导请参考本节，漫游用户使用归属地HSS，配置指导见本节配置到DRA的数据。 |
| 漫游场景                  | 方式二：本地用户和漫游用户都使用MME直连的HSS，请参考本节。                               |
| 新增MME(MME直接连HSS)或HSS  | 请参考本节。                                                         |
| 新增MME(MME通过DRA和HSS对接) | 请参考配置到DRA的数据。                                                  |

## 必备事项

前提条件

- 具备管理员权限的操作人员已经登录华为操作维护系统（登录U2020客户端或登录OM Portal）。

- UNC软件安装已完成。

- 请了解UNC各类接口的类型及命名规范，具体内容请参见业务组网与逻辑接口介绍。
- 对于IPv4组网，已完成自动部署配置动态路由OSPF+BFD组网（IPv4）、配置静态路由+BFD组网（IPv4）、配置BGP over OSPF/静态路由+BFD（IPv4）或手动部署配置动态路由OSPF+BFD组网（IPv4）、配置静态路由+BFD组网（IPv4）、配置BGP over OSPF/静态路由+BFD（IPv4）。

数据

**说明** 

本文以IPv4组网为例说明。

- 如果是IPv6组网，请将逻辑接口地址规划为IPv6地址。
- 如果是IPv4v6双栈组网，则对逻辑接口配置双栈地址即可。

**如下数据仅为举例，请注意修改成局点规划的数据。**

| 类别            | 参数名称                      | 取值样例                                      | 获取方法            | 说明                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|:--------------|:--------------------------|:------------------------------------------|:----------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ADD SERVICEIP | IP版本（IPVERSION）           | IPv4                                      | 参见“水平网设LLD文档 ”。 | 配置业务IP参数。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ADD SERVICEIP | 业务IPv4地址（SERVICEIPV4）     | 10.10.1.1 10.10.1.2 10.10.1.17 10.10.1.18 | 参见“水平网设LLD文档 ”。 | 配置业务IP参数。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ADD SERVICEIP | VPN实例名称（VPNINSTNAME）      | VPN_SIG                                   | 参见“水平网设LLD文档 ”。 | 配置业务IP参数。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ADD SCTPPARA  | SCTP协议参数索引（SCTPPARAINDEX） | 2                                         | 参见“水平网设LLD文档 ”。 | S6a接口的SCTP协议参数与S1–MME接口的SCTP协议参数分开配置，便于后续局点搬迁或扩容时，不影响互联网元配置。可以通过LST SCTPPARA来查询已存在的SCTP协议参数记录。                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ADD DMLE      | 本地实体索引（LOINDEX）           | 1                                         | 参见“水平网设LLD文档 ”。 | 配置Diameter本地信息。 如果已经存在DMLE，请使用现有的DMLE，无需添加。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ADD DMLE      | 本地实体主机名（LOHSTNAME）        | mme1.epc.mnc000.mcc123.3gppnetwork.org    | 参见“水平网设LLD文档 ”。 | 配置Diameter本地信息。 如果已经存在DMLE，请使用现有的DMLE，无需添加。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ADD DMLE      | 本地实体域名（LORLMNAME）         | epc.mnc000.mcc123.3gppnetwork.org         | 参见“水平网设LLD文档 ”。 | 配置Diameter本地信息。 如果已经存在DMLE，请使用现有的DMLE，无需添加。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ADD DMLE      | 本地实体名（LOINFONAME）         | usn                                       | 参见“水平网设LLD文档 ”。 | 配置Diameter本地信息。 如果已经存在DMLE，请使用现有的DMLE，无需添加。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ADD DMPE      | 对端实体索引（PEERIDX）           | 1                                         | 参见“水平网设LLD文档 ”。 | 配置Diameter对端信息。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ADD DMPE      | 对端主机名（PEERHTNAM）          | hss1.epc.mnc000.mcc123.3gppnetwork.org    | 参见“水平网设LLD文档 ”。 | 配置Diameter对端信息。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ADD DMPE      | 对端实体名（PEERNAM）            | HSS                                       | 参见“水平网设LLD文档 ”。 | 配置Diameter对端信息。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ADD DMPE      | 节点支持的应用（APPCAP）           | S6a/S6d-1&S13-0&SLg-0&T6a/T6ai/T6b/T6bi-0 | 参见“水平网设LLD文档 ”。 | 配置Diameter对端信息。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ADD DMLKS     | Diameter链路集索引（LINKSIDX）   | 1                                         | 参见“水平网设LLD文档 ”。 | 配置Diameter链路集。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ADD DMLKS     | 本地实体索引（LOCALIDX）          | 1                                         | 参见“水平网设LLD文档 ”。 | 配置Diameter链路集。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ADD DMLKS     | 对端实体索引（PEERIDX）           | 1                                         | 参见“水平网设LLD文档 ”。 | 配置Diameter链路集。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ADD DMLKS     | 选路模式（LSSELMODE）           | SELMODE_ACTIVE                            | 参见“水平网设LLD文档 ”。 | 配置Diameter链路集。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ADD DMLKS     | 链路集名称（LINKSNAM）           | to-HSS                                    | 参见“水平网设LLD文档 ”。 | 配置Diameter链路集。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ADD DMLNK     | vpn名称（VPNNAME）            | VPN_SIG                                   | 参见“水平网设LLD文档 ”。 | 配置Diameter链路。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ADD DMLNK     | 链路索引（LINKIDX）             | 0                                         | 参见“水平网设LLD文档 ”。 | 配置Diameter链路。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ADD DMLNK     | IP地址类型（IPTYPE）            | TPTADDR_TYPE_IPV4                         | 参见“水平网设LLD文档 ”。 | 配置Diameter链路。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ADD DMLNK     | 本端IP地址1（LOCALIPV4_1）      | 10.10.1.1 10.10.1.2                       | 参见“水平网设LLD文档 ”。 | 配置Diameter链路。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ADD DMLNK     | 本端IP地址2（LOCALIPV4_2）      | 10.10.1.17 10.10.1.18                     | 参见“水平网设LLD文档 ”。 | 配置Diameter链路。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ADD DMLNK     | 本端端口（LOCALPORT）           | 5000                                      | 参见“水平网设LLD文档 ”。 | 配置Diameter链路。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ADD DMLNK     | 对端IP地址1（PEERIPV4_1）       | 10.11.1.3                                 | 参见“水平网设LLD文档 ”。 | 配置Diameter链路。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ADD DMLNK     | 对端IP地址2（PEERIPV4_2）       | 10.11.2.3                                 | 参见“水平网设LLD文档 ”。 | 配置Diameter链路。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ADD DMLNK     | 对端端口（PEERPORT）            | 5000                                      | 参见“水平网设LLD文档 ”。 | 配置Diameter链路。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ADD DMLNK     | C/S模式（CLIORSER）           | DIAM_CONN_CLIENT                          | 参见“水平网设LLD文档 ”。 | 配置Diameter链路。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ADD DMLNK     | Diameter链路集索引（LINKSIDX）   | 1                                         | 参见“水平网设LLD文档 ”。 | 配置Diameter链路。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ADD DMLNK     | SCTP协议参数索引（SCTPINDX）      | 2                                         | 参见“水平网设LLD文档 ”。 | 配置Diameter链路。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ADD DMLNK     | 链路名称（LINKNAM）             | dmlink                                    | 参见“水平网设LLD文档 ”。 | 配置Diameter链路。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ADD DMHOSTRT  | 路由索引（ROUTEIDX）            | 1                                         | 参见“水平网设LLD文档 ”。 | 当HSS采用分布式组网时，MME需要配置多条到HSS不同FE的主机路由，同时将这些不同的主机路由加入同一个路由组。 HSS从逻辑上划分为BE（Back End）和FE（Front End）两部分，实现用户数据与业务逻辑处理的分离。 BE即USCDB（Unified Subscriber Center DataBase），负责存储用户数据，提供用户数据的增加、删除、更新和查询服务，为FE提供有效的数据支撑。 FE负责信令接入和业务逻辑处理，从BE获得数据服务。 当同一路由组内存在多条路由，可以采用不同的方式选择Diameter对端，如轮选、主从、优先级权重、IMSI指定优选等。 需要按照优先级和权重方式选择对端时，选路模式为优先级权重，即RSELMODE=SELMODE_PRIORITY_WEIGHT。 详细请参考激活基于权重/优先级的Diameter负荷分担。 PEERSEL（目的实体选择方式）取值PEER_INDEX时，需要填写PEERIDX（对端实体索引）；PEERSEL（目的实体选择方式）取值PEER_HOST_NAME时，需要填写PEERHTNAM（对端主机名）。这里以选择PEER_INDEX为例。 |
| ADD DMHOSTRT  | 选路模式（RSELMODE）            | SELMODE_PRIORITY_WEIGHT                   | 参见“水平网设LLD文档 ”。 | 当HSS采用分布式组网时，MME需要配置多条到HSS不同FE的主机路由，同时将这些不同的主机路由加入同一个路由组。 HSS从逻辑上划分为BE（Back End）和FE（Front End）两部分，实现用户数据与业务逻辑处理的分离。 BE即USCDB（Unified Subscriber Center DataBase），负责存储用户数据，提供用户数据的增加、删除、更新和查询服务，为FE提供有效的数据支撑。 FE负责信令接入和业务逻辑处理，从BE获得数据服务。 当同一路由组内存在多条路由，可以采用不同的方式选择Diameter对端，如轮选、主从、优先级权重、IMSI指定优选等。 需要按照优先级和权重方式选择对端时，选路模式为优先级权重，即RSELMODE=SELMODE_PRIORITY_WEIGHT。 详细请参考激活基于权重/优先级的Diameter负荷分担。 PEERSEL（目的实体选择方式）取值PEER_INDEX时，需要填写PEERIDX（对端实体索引）；PEERSEL（目的实体选择方式）取值PEER_HOST_NAME时，需要填写PEERHTNAM（对端主机名）。这里以选择PEER_INDEX为例。 |
| ADD DMHOSTRT  | 目的实体选择方式（PEERSEL）         | PEER_INDEX                                | 参见“水平网设LLD文档 ”。 | 当HSS采用分布式组网时，MME需要配置多条到HSS不同FE的主机路由，同时将这些不同的主机路由加入同一个路由组。 HSS从逻辑上划分为BE（Back End）和FE（Front End）两部分，实现用户数据与业务逻辑处理的分离。 BE即USCDB（Unified Subscriber Center DataBase），负责存储用户数据，提供用户数据的增加、删除、更新和查询服务，为FE提供有效的数据支撑。 FE负责信令接入和业务逻辑处理，从BE获得数据服务。 当同一路由组内存在多条路由，可以采用不同的方式选择Diameter对端，如轮选、主从、优先级权重、IMSI指定优选等。 需要按照优先级和权重方式选择对端时，选路模式为优先级权重，即RSELMODE=SELMODE_PRIORITY_WEIGHT。 详细请参考激活基于权重/优先级的Diameter负荷分担。 PEERSEL（目的实体选择方式）取值PEER_INDEX时，需要填写PEERIDX（对端实体索引）；PEERSEL（目的实体选择方式）取值PEER_HOST_NAME时，需要填写PEERHTNAM（对端主机名）。这里以选择PEER_INDEX为例。 |
| ADD DMHOSTRT  | 对端实体索引（PEERIDX）           | 1                                         | 参见“水平网设LLD文档 ”。 | 当HSS采用分布式组网时，MME需要配置多条到HSS不同FE的主机路由，同时将这些不同的主机路由加入同一个路由组。 HSS从逻辑上划分为BE（Back End）和FE（Front End）两部分，实现用户数据与业务逻辑处理的分离。 BE即USCDB（Unified Subscriber Center DataBase），负责存储用户数据，提供用户数据的增加、删除、更新和查询服务，为FE提供有效的数据支撑。 FE负责信令接入和业务逻辑处理，从BE获得数据服务。 当同一路由组内存在多条路由，可以采用不同的方式选择Diameter对端，如轮选、主从、优先级权重、IMSI指定优选等。 需要按照优先级和权重方式选择对端时，选路模式为优先级权重，即RSELMODE=SELMODE_PRIORITY_WEIGHT。 详细请参考激活基于权重/优先级的Diameter负荷分担。 PEERSEL（目的实体选择方式）取值PEER_INDEX时，需要填写PEERIDX（对端实体索引）；PEERSEL（目的实体选择方式）取值PEER_HOST_NAME时，需要填写PEERHTNAM（对端主机名）。这里以选择PEER_INDEX为例。 |
| ADD DMHOSTRT  | 路由名称（ROUTENAM）            | usn                                       | 参见“水平网设LLD文档 ”。 | 当HSS采用分布式组网时，MME需要配置多条到HSS不同FE的主机路由，同时将这些不同的主机路由加入同一个路由组。 HSS从逻辑上划分为BE（Back End）和FE（Front End）两部分，实现用户数据与业务逻辑处理的分离。 BE即USCDB（Unified Subscriber Center DataBase），负责存储用户数据，提供用户数据的增加、删除、更新和查询服务，为FE提供有效的数据支撑。 FE负责信令接入和业务逻辑处理，从BE获得数据服务。 当同一路由组内存在多条路由，可以采用不同的方式选择Diameter对端，如轮选、主从、优先级权重、IMSI指定优选等。 需要按照优先级和权重方式选择对端时，选路模式为优先级权重，即RSELMODE=SELMODE_PRIORITY_WEIGHT。 详细请参考激活基于权重/优先级的Diameter负荷分担。 PEERSEL（目的实体选择方式）取值PEER_INDEX时，需要填写PEERIDX（对端实体索引）；PEERSEL（目的实体选择方式）取值PEER_HOST_NAME时，需要填写PEERHTNAM（对端主机名）。这里以选择PEER_INDEX为例。 |
| ADD DMRTGRP   | 路由组索引（GRPIDX）             | 1                                         | 参见“水平网设LLD文档 ”。 | UNC与HSS直连时，建议Diameter路由的“路由优选模式”设置成优先选择主机路由 。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ADD DMRTGRP   | 路由模式（RTMODE）              | HOST_ROUTE                                | 参见“水平网设LLD文档 ”。 | UNC与HSS直连时，建议Diameter路由的“路由优选模式”设置成优先选择主机路由 。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ADD DMRTGRP   | 路由优选模式（RTPRIMODE）         | HOST_ROUTE_PREFER                         | 参见“水平网设LLD文档 ”。 | UNC与HSS直连时，建议Diameter路由的“路由优选模式”设置成优先选择主机路由 。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ADD DMRTGRP   | 路由索引（路由索引）                | 1                                         | 参见“水平网设LLD文档 ”。 | UNC与HSS直连时，建议Diameter路由的“路由优选模式”设置成优先选择主机路由 。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ADD DMRTGRP   | 路由组名称（ROUTEGRPNAM）        | To_HSS                                    | 参见“水平网设LLD文档 ”。 | UNC与HSS直连时，建议Diameter路由的“路由优选模式”设置成优先选择主机路由 。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ADD IMSIHSS   | IMSI前缀（IMSIPRE）           | 46000                                     | 参见“水平网设LLD文档 ”。 | 配置IMSI与HSS的映射关系。 用户可以根据该映射关系查找IMSI归属于哪个HSS的信息。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ADD IMSIHSS   | HSS域名（HSSRLM）             | epc.mnc000.mcc123.3gppnetwork.org         | 参见“水平网设LLD文档 ”。 | 配置IMSI与HSS的映射关系。 用户可以根据该映射关系查找IMSI归属于哪个HSS的信息。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ADD IMSIHSS   | Diameter路由组索引（GRPIDX）     | 1                                         | 参见“水平网设LLD文档 ”。 | 配置IMSI与HSS的映射关系。 用户可以根据该映射关系查找IMSI归属于哪个HSS的信息。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |

文档

获取网设LLD文档。

## 操作步骤

1. 进入“MML命令行-UNC”窗口。
2. 配置S6a接口业务IP。

   ```
   ADD SERVICEIP: IPVERSION=IPv4, SERVICEIPV4="10.10.1.1", VPNINSTNAME="VPN_SIG"; 
   ADD SERVICEIP: IPVERSION=IPv4, SERVICEIPV4="10.10.1.2", VPNINSTNAME="VPN_SIG"; 
   ADD SERVICEIP: IPVERSION=IPv4, SERVICEIPV4="10.10.1.17", VPNINSTNAME="VPN_SIG"; 
   ADD SERVICEIP: IPVERSION=IPv4, SERVICEIPV4="10.10.1.18", VPNINSTNAME="VPN_SIG";
   ```
3. 配置S6a接口基于IP的宽带信令SCTP偶联配置的协议参数。

   ```
   ADD SCTPPARA:SCTPPARAINDEX=2;
   ```
4. **可选：**查看Diameter配置中“重连定时器（RECONNTIMER）”是否符合要求。如果“重连定时器（RECONNTIMER）”参数不为6s，则设置为6s。

   **说明** 

   在Diameter链路建立后，如果发生链路迁移或者重建，UNC可以主动发送INIT消息给对端设备请求建链，可以使得链路不中断。但是如果对端设备不支持在UP状态时处理INIT消息，可能会导致链路中断，重建时间变长，具体时长取决于配置的“重连定时器（RECONNTIMER）”参数。

   该定时器系统默认为30s，在目前灰度升级、扩容缩容等发生链路迁移场景下，造成链路中断时间过长，因此根据对端设备处理方式，建议将该参数配置为6s。

   ```
   LST DMFUNC:;
   SET DMFUNC:RECONNTIMER=6;
   ```
5. 增加Diameter本端信息 。

   ```
   ADD DMLE:LOINDEX=1,LOHSTNAME="mme1.epc.mnc000.mcc123.3gppnetwork.org",LORLMNAME="epc.mnc000.mcc123.3gppnetwork.org",LOINFONAME="usn";
   ```
6. 增加Diameter对端信息。

   ```
   ADD DMPE:PEERIDX=1,PEERHTNAM="hss1.epc.mnc000.mcc123.3gppnetwork.org",PEERNAM="HSS",APPCAP=S6a/S6d-1&S13-0&SLg-0&T6a/T6ai/T6b/T6bi-0;
   ```
7. 配置Diameter链路集信息。

   ```
   ADD DMLKS:LINKSIDX=1,LOCALIDX=1,PEERIDX=1,LSSELMODE=SELMODE_ACTIVE,LINKSNAM="to-HSS";
   ```
8. 配置Diameter链路信息。

   ```
   ADD DMLNK:VPNNAME="VPN_SIG",LINKIDX=0,IPTYPE=TPTADDR_TYPE_IPV4,LOCALIPV4_1="10.10.1.1", LOCALIPV4_2="10.10.1.17",LOCALPORT=5000,PEERIPV4_1="10.11.1.3", PEERIPV4_2="10.11.2.3", PEERPORT=5000,CLIORSER=DIAM_CONN_CLIENT,LINKSIDX=1,SCTPINDX=2,LINKNAM="dmlink"; 
   ADD DMLNK:VPNNAME="VPN_SIG",LINKIDX=1,IPTYPE=TPTADDR_TYPE_IPV4,LOCALIPV4_1="10.10.1.2", LOCALIPV4_2="10.10.1.18",LOCALPORT=5000,PEERIPV4_1="10.11.1.3", PEERIPV4_2="10.11.2.3", PEERPORT=5000,CLIORSER=DIAM_CONN_CLIENT,LINKSIDX=1,SCTPINDX=2,LINKNAM="dmlink";
   ```
9. 配置Diameter主机路由并将主机路由加入路由组。
   1. 配置到HSS的主机路由。

      ```
      ADD DMHOSTRT:ROUTEIDX=1,RSELMODE=SELMODE_PRIORITY_WEIGHT,PEERSEL=PEER_INDEX,PEERIDX=1,ROUTENAM="usn";
      ```
   2. 将主机路由加入Diameter路由组中。

      ```
      ADD DMRTGRP: GRPIDX=1, RTMODE=HOST_ROUTE, RTPRIMODE=HOST_ROUTE_PREFER, ROUTEIDX=1, ROUTEGRPNAM="To_HSS";
      ```
10. **可选：**配置Diameter域路由并加入路由组。
    1. 配置Diameter域路由。

       ****ADD DMRT****

       **说明** 

       1. MME与HSS直连，配置Diameter域路由的场景：

          - IMSI号段不在IMSI与HSS映射关系范围内，系统自动组装域名。
          - 主机路由故障时，通过域路由找到对端。与主机路由备份，增强可靠性。
       2. 当同一路由组内存在多条路由，需要按照优先级和权重方式选择对端时，选路模式为优先级权重，即RSELMODE=SELMODE\_PRIORITY\_WEIGHT。

          详细请参考**激活基于权重/优先级的Diameter负荷分担**。
    2. 配置Diameter路由组。如果配置了域路由，该路由需要加入路由组，与主机路由在同一个路由组。路由索引不需要配置，路由优先模式是优选主机路由，系统可以通过域名自动关联域路由。

       ****ADD DMRTGRP****
11. 配置IMSI与HSS的映射关系，用户可以根据该映射关系查找IMSI归属于哪个HSS的信息。

    ```
    ADD IMSIHSS:IMSIPRE="46000",HSSRLM="epc.mnc000.mcc123.3gppnetwork.org",GRPIDX=1;
    ```

## 验证方法

1. 进入“MML命令行-UNC”窗口。
2. 查询当前配置的本地实体信息。

   ****LST DMLE****: LOINDEX="本地实体索引";

   ****DSP DMLE****: LOINDEX="本地实体索引";

   - **预期结果：**显示所有已经配置本地实体的配置信息、状态信息。

     ```
     %%LST DMLE: LOINDEX=0;%% 
     RETCODE = 0  操作成功。  

     操作结果如下 
     ------------   
       本地实体索引  =  0 
     本地实体主机名  =  mme0.huawei.com.cn   
       本地实体域名  =  huawei.com.cn         
             产品名  =  unc     
         本地实体名  =  unc 
     (结果个数 = 1) 
     ---    END
     ```

     ```
     %%DSP DMLE:;%% 
     RETCODE = 0  操作成功。  

     输出结果如下 
     ------------ 
     本地实体索引  =  0   
       本地实体名  =  unc     
         实体状态  =  正常 
     (结果个数 = 1) 
     ---    END
     ```
   - **异常结果：**异常处理过程参见**ALM-80593 Diameter对等端不可达**。
3. 验证UNC能够正确查询对端实体状态。

   ****LST DMPE****: PEERIDX="对端实体索引";

   ****DSP DMPE****: PEERIDX="对端实体索引";

   - **预期结果：**显示所有已经配置对端实体的配置信息、状态信息。

     ```
     %%LST DMPE:;%% 
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
     %%DSP DMPE:;%% 
     RETCODE = 0  操作成功。  

     输出结果如下 
     ------------ 
     对端实体索引    对端实体名    实体状态  
     0               hss0          正常     
     1               hss1          正常     
     (结果个数 = 2) 
     ---    END
     ```
   - **异常结果：**异常处理过程参见**ALM-80593 Diameter对等端不可达**。
4. 验证UNC能够正确查询Diameter链路集状态。

   ****LST DMLKS****: LINKSIDX="Diameter链路集索引";

   ****DSP DMLKS****: LINKSIDX="Diameter链路集索引";

   - **预期结果：**显示已经配置Diameter链路集的配置信息、状态信息。

     ```
     %%LST DMLKS: LINKSIDX=0;%% 
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
     %%DSP DMLKS: LINKSIDX=0;%% 
     RETCODE = 0  操作成功。  

     输出结果如下 
     ------------ 
     Diameter链路集索引  =  0         
             链路集名称  =  Robin0         
             链路集状态  =  正常 
     (结果个数 = 1) 
     ---    END
     ```
   - **异常结果：**异常处理过程参见**ALM-80591 Diameter链路故障**。
5. 验证UNC能够正确查询Diameter链路状态。

   ****LST DMLNK****: LINKIDX="链路索引";

   ****DSP DMLNK****: LINKIDX="链路索引";

   - **预期结果：**显示已经配置Diameter链路的配置信息、状态信息。

     ```
     %%LST DMLNK: LINKIDX=0;%% 
     RETCODE = 0  操作成功  

     输出结果如下： 
     --------------            
               链路索引  =  0         
                vpn名称  =  VPN_SIG       
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
     %%DSP DMLNK: LINKIDX=0;%% 
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
   - **异常结果：**异常处理过程参见**ALM-80591 Diameter链路故障**。
6. 验证UNC能够正确查询Diameter路由状态。

   ****LST DMHOSTRT****: ROUTEIDX="路由索引";

   ****LST DMRTGRP****: GRPIDX="路由组索引";

   （可选）****LST DMRT****: ROUTEIDX="路由索引";

   （可选）****DSP DMRT****: ROUTEIDX="路由索引";

   - **预期结果：**显示已经配置Diameter路由的配置信息、状态信息。

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
     %%LST DMRT: ROUTEIDX=0;%% 
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
     %%DSP DMRT: ROUTEIDX=0;%% 
     RETCODE = 0  操作成功。  

     输出结果如下 
     ------------ 
     路由索引  =  0 
     路由名称  =  dmrt2hss1 
     路由状态  =  正常 
     (结果个数 = 1) 
     ---    END
     ```
   - **异常结果：**异常处理过程参见**ALM-80592 Diameter路由不可用**。
7. 验证UNC能够正确查询IMSI与HSS的映射关系。

   ****LST IMSIHSS****: IMSIPRE="IMSI前缀";

   - **预期结果：**正确显示-已经配置IMSI与HSS的映射关系的配置信息。

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

   **说明** 

   进行业务测试前，需要首先完成UNC与eNodeB、SGW、HSS的链路配置。

   进行业务测试的终端必须是在对接的HSS中开户。

   使用手机浏览网页，指定的APN由调测的HSS负责接入。

   1. **创建用户跟踪任务**。

      参数选择如下：

      - IMSI/MSISDN/IMEI：被跟踪用户的IMSI、MSISDN或者IMEI。
      - 其他参数：选择默认值。
   2. **创建接口跟踪任务**。

      链路索引：MME与HSS配置的链路索引号。
   3. 用户开机附着。
   4. **可选：**查看S6a接口跟踪结果。
   5. 查看用户跟踪结果。

      **预期结果：**

      用户附着成功，可以在Message Direction处看到UDM模块与DIAM模块、MME和HSS之间有消息交互。

      **说明** 

      此功能用于快速定位问题和解决故障，在使用过程中不可避免的使用到用户的某些个人数据，如IMSI、IP地址。该功能提供了假名化的处理方式。建议您遵从国家的相关法律执行该任务，并采取足够的措施以确保用户的个人数据受到充分的保护，例如在U2020上将假名化开关打开、处理完毕后将保存跟踪记录的文件夹进行删除等。

      - **异常结果：**

        观察不到MME与HSS之间、UDM模块与DIAM模块之间的消息。或观察到MME与HSS之间的消息result code信元不为diameter\_success。查询用户MM上下文。
   6. 查询用户MM上下文。

      **DSP COMMMCTX**: QUERYOPT=BYIMSI, IMSI=IMSI;

      - **预期结果：**

        可以查询到用户的MM上下文，并接状态为EMM-IDLE或是EMM-CONNECT状态。
      - **异常结果：**

        查询不到用户的MM上下文。
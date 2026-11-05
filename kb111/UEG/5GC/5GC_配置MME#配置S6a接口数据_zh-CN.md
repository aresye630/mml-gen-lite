---
id: ''
name: 配置S6a接口数据
ne_type: UEG
type: feature
description: 当运营商在部署分组交换网，新增MME或HSS时，在配置完成MME到HSS的路由数据后，可通过配置S6a接口数据建立MME到HSS的逻辑连接。  S6a接口是EPC系统中，MME和HSS之间的接口。用于提供用户的签约数据管理和鉴权相关的功能。在漫游场景下，MME还需要通过S6a接口连接到用户归属地的HSS。  **图1** S6a接口协议栈  由于UEG L模式下面分两种模式，一种模式下的UEG包含UDM/AUSF/HSS网元功能，另一种模式则相反，不包含UDM/AUSF/HSS网元功能，需要和中心侧网络UDM/AUSF/HSS进行对接。  园区风筝L有两种部署模式：  * L1：MME与中心侧两个HSS对接，此场景需要运营商规划业务IP地址，VRF。数据会出园区传输。 * L2：MME仅选择与园区内本端DC的HSS对接，这样使用园区统一规划的IP地址，VRF。数据在园区内封闭传输。  除此以外，L1和L2模式中S6a接口的配置命令无差异。  以下配置数据以及步骤均以UEG双DC组网场景的配置规划为例进行介绍。
tags: []
risk_level: ''
doc_source: ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（一号通专网煤矿场景，入驻式）","软件安装与开站","UEG软件安装与开站","UEG初始配置","参考：详细配置指导","配置MME","配置S6a接口数据"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
当运营商在部署分组交换网，新增MME或HSS时，在配置完成MME到HSS的路由数据后，可通过配置S6a接口数据建立MME到HSS的逻辑连接。S6a接口是EPC系统中，MME和HSS之间的接口。用于提供用户的签约数据管理和鉴权相关的功能。在漫游场景下，MME还需要通过S6a接口连接到用户归属地的HSS。**图1** S6a接口协议栈由于UEG L模式下面分两种模式，一种模式下的UEG包含UDM/AUSF/HSS网元功能，另一种模式则相反，不包含UDM/AUSF/HSS网元功能，需要和中心侧网络UDM/AUSF/HSS进行对接。园区风筝L有两种部署模式：* L1：MME与中心侧两个HSS对接，此场景需要运营商规划业务IP地址，VRF。数据会出园区传输。* L2：MME仅选择与园区内本端DC的HSS对接，这样使用园区统一规划的IP地址，VRF。数据在园区内封闭传输。除此以外，L1和L2模式中S6a接口的配置命令无差异。以下配置数据以及步骤均以UEG双DC组网场景的配置规划为例进行介绍。

## 必备事项
前提条件

* 具备管理员权限的操作人员已经登录华为操作维护系统（登录U2020/MAE客户端或登录OM Portal）。

* 已完成组网路由配置。
* 如果本接口采用IPv6组网，则需要开通逻辑接口支持IPv6特性，即加载对应的License项“81203214 LKV3G5V6LI01 逻辑接口支持IPv6”。
* 已经获取网设LLD文档。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    add_serviceip_list:
      type: items
      properties:
        IPVERSION:
          name: 'IP版本'
          type: string
          enum:
          - IPv4
          - IPv6
          required: true
          description: '配置业务IP参数。'
          data_source: '参见“水平网设LLD文档 ”。'
          pattern: ''
          default: IPv4
        SERVICEIPV4:
          name: '业务IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: '由于S6a接口传输层的SCTP协议支持多连接，且同一连接也存在多路径，可以配置多个业务IP地址支持多条链路，此处以两个业务IP地址为例。'
          data_source: ''
          pattern: ''
          default: ''
        VPNINSTNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: false
          description: '本文S6a接口组网以L2模式为例说明。UEG风筝形态内部接口组网时，使用园区统一规划的VPN。'
          data_source: ''
          pattern: ''
          default: ''
    add_cpsctppara_list:
      type: items
      properties:
        SCTPPARAINDEX:
          name: 'SCTP协议参数索引'
          type: integer
          minimum: 0
          maximum: 65534
          required: true
          description: 'S6a接口的SCTP协议参数与S1–MME接口的SCTP协议参数分开配置，便于后续局点搬迁或扩容时，不影响互联网元配置。可以通过****LST CPSCTPPARA****来查询已存在的SCTP协议参数记录。'
          data_source: ''
          pattern: ''
          default: ''
    set_dmfunc_list:
      type: items
      properties:
        RECONNTIMER:
          name: '重连定时器（s）'
          type: integer
          minimum: 1
          maximum: 100
          required: false
          description: '配置Diameter路由重连定时器。'
          data_source: ''
          pattern: ''
          default: ''
    add_cpdmle_list:
      type: items
      properties:
        LOINDEX:
          name: '本地实体索引'
          type: integer
          minimum: 0
          maximum: 31
          required: false
          description: '配置Diameter本地信息。  如果已经存在DMLE，请使用现有的DMLE，无需添加。'
          data_source: ''
          pattern: ''
          default: 0
        LOHSTNAME:
          name: '本地实体主机名'
          type: string
          maxLength: 127
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LORLMNAME:
          name: '本地实体域名'
          type: string
          maxLength: 127
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LOINFONAME:
          name: '本地实体名'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_cpdmpe_list:
      type: items
      properties:
        PEERIDX:
          name: '对端实体索引'
          type: integer
          minimum: 0
          maximum: 639
          required: true
          description: '配置Diameter对端信息。'
          data_source: ''
          pattern: ''
          default: ''
        PEERHTNAM:
          name: '对端主机名'
          type: string
          maxLength: 127
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PEERNAM:
          name: '对端实体名'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        APPCAP:
          name: '节点支持的应用'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_cpdmlks_list:
      type: items
      properties:
        LINKSIDX:
          name: 'Diameter链路集索引'
          type: integer
          minimum: 0
          maximum: 639
          required: true
          description: '配置Diameter链路集。'
          data_source: ''
          pattern: ''
          default: ''
        LOCALIDX:
          name: '本地实体索引'
          type: integer
          minimum: 0
          maximum: 31
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PEERIDX:
          name: '对端实体索引'
          type: integer
          minimum: 0
          maximum: 639
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LSSELMODE:
          name: '选路模式'
          type: string
          enum:
          - SELMODE_ACTIVE
          - SELMODE_LOAD_BALAN
          - SELMODE_MASTER_SLAVE
          - SELMODE_ROUND_ROBIN
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: SELMODE_LOAD_BALAN
        LINKSNAM:
          name: '链路集名称'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'noname'
    add_cpdmlnk_list:
      type: items
      properties:
        VPNNAME:
          name: 'vpn名称'
          type: string
          maxLength: 31
          required: false
          description: '配置Diameter链路。  说明：  当UEG在煤矿等场景下使用2U1选型时，仅需要配置5000端口的链路；当UEG在核电等场景下使用4U4选型时，需额外配置5001端口的链路。'
          data_source: ''
          pattern: ''
          default: ''
        LINKIDX:
          name: '链路索引'
          type: integer
          minimum: 0
          maximum: 1279
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPTYPE:
          name: 'IP地址类型'
          type: string
          enum:
          - TPTADDR_TYPE_IPV4
          - TPTADDR_TYPE_IPV6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: TPTADDR_TYPE_IPV4
        LOCALIPV4_1:
          name: '本端IP地址1'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LOCALIPV4_2:
          name: '本端IP地址2'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LOCALPORT:
          name: '本端端口'
          type: integer
          minimum: 1024
          maximum: 65534
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 3868
        PEERIPV4_1:
          name: '对端IP地址1'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PEERIPV4_2:
          name: '对端IP地址2'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PEERPORT:
          name: '对端端口'
          type: integer
          minimum: 1
          maximum: 65534
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 3868
        CLIORSER:
          name: 'C/S模式'
          type: string
          enum:
          - DIAM_CONN_CLIENT
          - DIAM_CONN_SERVER
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DIAM_CONN_CLIENT
        LINKSIDX:
          name: 'Diameter链路集索引'
          type: integer
          minimum: 0
          maximum: 639
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SCTPINDX:
          name: 'SCTP协议参数索引'
          type: integer
          minimum: 0
          maximum: 65534
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LINKNAM:
          name: '链路名称'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'noname'
    add_cpdmlnk_list_4:
      type: items
      properties:
        VPNNAME:
          name: 'vpn名称'
          type: string
          maxLength: 31
          required: false
          description: '配置Diameter链路。  说明：  当UEG在煤矿等场景下使用2U1选型时，仅需要配置5000端口的链路；当UEG在核电等场景下使用4U4选型时，需额外配置5001端口的链路。'
          data_source: ''
          pattern: ''
          default: ''
        LINKIDX:
          name: '链路索引'
          type: integer
          minimum: 0
          maximum: 1279
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPTYPE:
          name: 'IP地址类型'
          type: string
          enum:
          - TPTADDR_TYPE_IPV4
          - TPTADDR_TYPE_IPV6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: TPTADDR_TYPE_IPV4
        LOCALIPV4_1:
          name: '本端IP地址1'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LOCALIPV4_2:
          name: '本端IP地址2'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LOCALPORT:
          name: '本端端口'
          type: integer
          minimum: 1024
          maximum: 65534
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 3868
        PEERIPV4_1:
          name: '对端IP地址1'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PEERIPV4_2:
          name: '对端IP地址2'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PEERPORT:
          name: '对端端口'
          type: integer
          minimum: 1
          maximum: 65534
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 3868
        CLIORSER:
          name: 'C/S模式'
          type: string
          enum:
          - DIAM_CONN_CLIENT
          - DIAM_CONN_SERVER
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DIAM_CONN_CLIENT
        LINKSIDX:
          name: 'Diameter链路集索引'
          type: integer
          minimum: 0
          maximum: 639
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SCTPINDX:
          name: 'SCTP协议参数索引'
          type: integer
          minimum: 0
          maximum: 65534
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LINKNAM:
          name: '链路名称'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'noname'
    add_dmhostrt_list:
      type: items
      properties:
        ROUTEIDX:
          name: '路由索引'
          type: integer
          minimum: 0
          maximum: 1023
          required: true
          description: '* 当HSS采用分布式组网时，MME需要配置多条到HSS不同FE的主机路由，同时将这些不同的主机路由加入同一个路由组。  HSS从逻辑上划分为BE（Back End）和FE（Front End）两部分，实现用户数据与业务逻辑处理的分离。 BE即USCDB（Unified Subscriber Center DataBase），负责存储用户数据，提供用户数据的增加、删除、更新和查询服务，为FE提供有效的数据支撑。 FE负责信令接入和业务逻辑处理，从BE获得数据服务。 * 当同一路由组内存在多条路由，可以采用不同的方式选择Diameter对端，如轮选、主从、优先级权重、IMSI指定优选等。  需要按照优先级和权重方式选择对端时，选路模式为优先级权重，即RSELMODE=SELMODE\_PRIORITY\_WEIGHT。  详细请参考激活基于权重/优先级的Diameter负荷分担。 * PEERSEL（目的实体选择方式）取值PEER\_INDEX时，需要填写PEERIDX（对端实体索引）；PEERSEL（目的实体选择方式）取值PEER\_HOST\_NAME时，需要填写PEERHTNAM（对端主机名）。这里以选择PEER\_INDEX为例。'
          data_source: ''
          pattern: ''
          default: ''
        RSELMODE:
          name: '选路模式'
          type: string
          enum:
          - SELMODE_MASTER_SLAVE
          - SELMODE_PRIORITY_WEIGHT
          - SELMODE_ROUND_ROBIN
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: SELMODE_MASTER_SLAVE
        PEERSEL:
          name: '目的实体选择方式'
          type: string
          enum:
          - PEER_HOST_NAME
          - PEER_INDEX
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: PEER_INDEX
        PEERIDX:
          name: '对端实体索引'
          type: integer
          minimum: 0
          maximum: 639
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ROUTENAM:
          name: '路由名称'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_dmrtgrp_list:
      type: items
      properties:
        GRPIDX:
          name: '路由组索引'
          type: integer
          minimum: 0
          maximum: 1023
          required: true
          description: 'MME与HSS直连时，建议Diameter路由的“路由优选模式”设置成优先选择主机路由 。'
          data_source: ''
          pattern: ''
          default: ''
        RTMODE:
          name: '路由模式'
          type: string
          enum:
          - HOST_ROUTE
          - REALM_ROUTE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: HOST_ROUTE
        RTPRIMODE:
          name: '路由优选模式'
          type: string
          enum:
          - HOST_ROUTE_PREFER
          - REALM_ROUTE_PREFER
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: HOST_ROUTE_PREFER
        ROUTEIDX:
          name: '路由索引'
          type: integer
          minimum: 0
          maximum: 2047
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ROUTEGRPNAM:
          name: '路由组名称'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'noname'
    add_cpdmrt_list:
      type: items
      properties:
        ROUTEIDX:
          name: '路由索引'
          type: integer
          minimum: 0
          maximum: 2047
          required: true
          description: '配置到DRA的Diameter域路由。'
          data_source: ''
          pattern: ''
          default: ''
        APPNAM:
          name: '应用名称'
          type: string
          enum:
          - S13
          - S6A/S6D
          - SLG
          - T6A/T6AI/T6B/T6BI
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: S6A/S6D
        RSELMODE:
          name: '选路模式'
          type: string
          enum:
          - SELMODE_ACTIVE
          - SELMODE_IMSI_PRIORITY
          - SELMODE_MASTER_SLAVE
          - SELMODE_PRIORITY_WEIGHT
          - SELMODE_ROUND_ROBIN
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: SELMODE_MASTER_SLAVE
        REALMNAME:
          name: '目的实体域名'
          type: string
          maxLength: 127
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PEERIDX:
          name: '对端实体索引'
          type: integer
          minimum: 0
          maximum: 639
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ROUTENAM:
          name: '路由名称'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ISDEFAULT:
          name: '是否默认路由'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NO
    add_dmrtgrp_list_2:
      type: items
      properties:
        GRPIDX:
          name: '路由组索引'
          type: integer
          minimum: 0
          maximum: 1023
          required: true
          description: 'MME与HSS直连时，建议Diameter路由的“路由优选模式”设置成优先选择主机路由 。'
          data_source: ''
          pattern: ''
          default: ''
        RTMODE:
          name: '路由模式'
          type: string
          enum:
          - HOST_ROUTE
          - REALM_ROUTE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: HOST_ROUTE
        RTPRIMODE:
          name: '路由优选模式'
          type: string
          enum:
          - HOST_ROUTE_PREFER
          - REALM_ROUTE_PREFER
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: HOST_ROUTE_PREFER
        ROUTEIDX:
          name: '路由索引'
          type: integer
          minimum: 0
          maximum: 2047
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PEERIDX:
          name: '对端实体索引'
          type: integer
          minimum: 0
          maximum: 639
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ROUTEGRPNAM:
          name: '路由组名称'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'noname'
    add_imsihss_list:
      type: items
      properties:
        IMSIPRE:
          name: 'IMSI前缀'
          type: string
          maxLength: 15
          required: true
          description: '配置IMSI与HSS的映射关系。  用户可以根据该映射关系查找IMSI归属于哪个HSS的信息。'
          data_source: ''
          pattern: ''
          default: ''
        HSSRLM:
          name: 'HSS域名'
          type: string
          maxLength: 127
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GRPIDX:
          name: 'Diameter路由组索引'
          type: integer
          minimum: 0
          maximum: 1023
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_s1usrsecpara_list:
      type: items
      properties:
        IMSIPRE:
          name: 'IMSI前缀'
          type: string
          maxLength: 15
          required: true
          description: '关闭周期性鉴权功能。  MME与中心侧HSS对接时，为了减少传输中断触发的周期性鉴权功能，精简鉴权事件，仅保留**初始注册、移动性Inter注册**中开启强制鉴权功能，其余鉴权事件均关闭。  所有风筝方案保持一致处理。'
          data_source: ''
          pattern: ''
          default: ''
        SECPLC:
          name: '安全策略'
          type: string
          enum:
          - AUTHANDPROTECTED
          - AUTHONLY
          - NEVER
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: AUTHANDPROTECTED
        OPTIONAL:
          name: '高级选项'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AUTHEVENT:
          name: '鉴权事件'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AUTHPERIOD:
          name: '鉴权周期'
          type: integer
          minimum: 0
          maximum: 24
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 24
  examples:
    add_serviceip_list:
    - IPVERSION: IPv4
      SERVICEIPV4: '10.10.1.1'
      VPNINSTNAME: 'VPN_CN'
    - IPVERSION: IPv4
      SERVICEIPV4: '10.10.1.17'
      VPNINSTNAME: 'VPN_CN'
    add_cpsctppara_list:
    - SCTPPARAINDEX: 2
    - SCTPPARAINDEX: 2
    set_dmfunc_list:
    - RECONNTIMER: 6
    - RECONNTIMER: 6
    add_cpdmle_list:
    - LOINDEX: 1
      LOHSTNAME: 'mme1.epc.mnc000.mcc123.3gppnetwork.org'
      LORLMNAME: 'epc1.mnc000.mcc123.3gppnetwork.org'
      LOINFONAME: 'usn'
    - LOINDEX: 1
      LOHSTNAME: 'mme2.epc.mnc000.mcc123.3gppnetwork.org'
      LORLMNAME: 'epc2.mnc000.mcc123.3gppnetwork.org'
      LOINFONAME: 'usn'
    add_cpdmpe_list:
    - PEERIDX: 1
      PEERHTNAM: 'hss1.epc.mnc000.mcc123.3gppnetwork.org'
      PEERNAM: 'HSS'
      APPCAP: S6a/S6d-1&S13-0&SLg-0&T6a/T6ai/T6b/T6bi-0
    - PEERIDX: 1
      PEERHTNAM: 'hss1.epc.mnc000.mcc123.3gppnetwork.org'
      PEERNAM: 'HSS'
      APPCAP: S6a/S6d-1&S13-0&SLg-0&T6a/T6ai/T6b/T6bi-0
    add_cpdmlks_list:
    - LINKSIDX: 1
      LOCALIDX: 1
      PEERIDX: 1
      LSSELMODE: SELMODE_ACTIVE
      LINKSNAM: 'to-HSS'
    - LINKSIDX: 1
      LOCALIDX: 1
      PEERIDX: 1
      LSSELMODE: SELMODE_ACTIVE
      LINKSNAM: 'to-HSS'
    add_cpdmlnk_list:
    - VPNNAME: 'VPN_CN'
      LINKIDX: 0
      IPTYPE: TPTADDR_TYPE_IPV4
      LOCALIPV4_1: '10.10.1.1'
      LOCALIPV4_2: '10.10.1.2'
      LOCALPORT: 5000
      PEERIPV4_1: '10.11.1.3'
      PEERIPV4_2: '10.11.2.3'
      PEERPORT: 5000
      CLIORSER: DIAM_CONN_CLIENT
      LINKSIDX: 1
      SCTPINDX: 2
      LINKNAM: 'dmlink0'
    - VPNNAME: 'VPN_CN'
      LINKIDX: 0
      IPTYPE: TPTADDR_TYPE_IPV4
      LOCALIPV4_1: '10.10.1.17'
      LOCALIPV4_2: '10.10.1.18'
      LOCALPORT: 5000
      PEERIPV4_1: '10.11.1.3'
      PEERIPV4_2: '10.11.2.3'
      PEERPORT: 5000
      CLIORSER: DIAM_CONN_CLIENT
      LINKSIDX: 1
      SCTPINDX: 2
      LINKNAM: 'dmlink0'
    add_cpdmlnk_list_4:
    - VPNNAME: 'VPN_CN'
      LINKIDX: 2
      IPTYPE: TPTADDR_TYPE_IPV4
      LOCALIPV4_1: '10.10.1.2'
      LOCALIPV4_2: '10.10.1.1'
      LOCALPORT: 5001
      PEERIPV4_1: '10.11.2.3'
      PEERIPV4_2: '10.11.1.3'
      PEERPORT: 5001
      CLIORSER: DIAM_CONN_CLIENT
      LINKSIDX: 1
      SCTPINDX: 2
      LINKNAM: 'dmlink2'
    - VPNNAME: 'VPN_CN'
      LINKIDX: 2
      IPTYPE: TPTADDR_TYPE_IPV4
      LOCALIPV4_1: '10.10.1.18'
      LOCALIPV4_2: '10.10.1.17'
      LOCALPORT: 5001
      PEERIPV4_1: '10.11.2.3'
      PEERIPV4_2: '10.11.1.3'
      PEERPORT: 5001
      CLIORSER: DIAM_CONN_CLIENT
      LINKSIDX: 1
      SCTPINDX: 2
      LINKNAM: 'dmlink2'
    add_dmhostrt_list:
    - ROUTEIDX: 1
      RSELMODE: SELMODE_PRIORITY_WEIGHT
      PEERSEL: PEER_INDEX
      PEERIDX: 1
      ROUTENAM: 'mme'
    - ROUTEIDX: 2
      RSELMODE: SCPDMRTELMODE_PRIORITY_WEIGHT
      PEERSEL: PEER_INDEX
      PEERIDX: 2
      ROUTENAM: 'mme'
    add_dmrtgrp_list:
    - GRPIDX: 1
      RTMODE: HOST_ROUTE
      RTPRIMODE: HOST_ROUTE_PREFER
      ROUTEIDX: 1
      ROUTEGRPNAM: 'To_HSS'
    - GRPIDX: 2
      RTMODE: HOST_ROUTE
      RTPRIMODE: HOST_ROUTE_PREFER
      ROUTEIDX: 2
      ROUTEGRPNAM: 'To_HSS'
    add_cpdmrt_list:
    - ROUTEIDX: 3
      APPNAM: S6A/S6D
      RSELMODE: SELMODE_ROUND_ROBIN
      REALMNAME: 'epc1.mnc000.mcc123.3gppnetwork.org'
      PEERIDX: 1
      ROUTENAM: 'diamt_route1'
      ISDEFAULT: NO
    - ROUTEIDX: 3
      APPNAM: S6A/S6D
      RSELMODE: SELMODE_ROUND_ROBIN
      REALMNAME: 'epc1.mnc000.mcc123.3gppnetwork.org'
      PEERIDX: 1
      ROUTENAM: 'diamt_route1'
      ISDEFAULT: ''
    add_dmrtgrp_list_2:
    - GRPIDX: 3
      RTMODE: REALM_ROUTE
      RTPRIMODE: REALM_ROUTE_PREFER
      ROUTEIDX: 3
      PEERIDX: 1
      ROUTEGRPNAM: 'dra'
    - GRPIDX: 3
      RTMODE: REALM_ROUTE
      RTPRIMODE: REALM_ROUTE_PREFER
      ROUTEIDX: 3
      PEERIDX: 1
      ROUTEGRPNAM: 'dra'
    add_imsihss_list:
    - IMSIPRE: '46000'
      HSSRLM: 'epc1.mnc000.mcc123.3gppnetwork.org'
      GRPIDX: 1
    - IMSIPRE: '46000'
      HSSRLM: 'epc2.mnc000.mcc123.3gppnetwork.org'
      GRPIDX: 2
    add_s1usrsecpara_list:
    - IMSIPRE: 'DEFAULT'
      SECPLC: AUTHANDPROTECTED
      OPTIONAL: YES
      AUTHEVENT: ATTACH-1&INTRA_TAU-0&INTER_TAU-1&DETACH-0&SERVICE_REQUEST-0&PROD_TAU-0&SYSTEM_CHANGE_INTRA_TAU-0&INTRA_TAU_AFTER_HANDOVER-0&INTER_TAU_AFTER_HANDOVER-0
      AUTHPERIOD: 0
    - IMSIPRE: 'DEFAULT'
      SECPLC: AUTHANDPROTECTED
      OPTIONAL: YES
      AUTHEVENT: ATTACH-1&INTRA_TAU-0&INTER_TAU-1&DETACH-0&SERVICE_REQUEST-0&PROD_TAU-0&SYSTEM_CHANGE_INTRA_TAU-0&INTRA_TAU_AFTER_HANDOVER-0&INTER_TAU_AFTER_HANDOVER-0
      AUTHPERIOD: 0
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 进入“MML命令行-UEG”窗口。

### 2 配置S6a接口业务IP。

#### 2.1 //DC1

```jinja2
{%- for item in add_serviceip_list -%}
    ADD SERVICEIP:
    {#- --- 必选参数 --- -#}
    IPVERSION={{item.IPVERSION}},
    {#- --- 可选参数 --- -#}
    {%- if item.VPNINSTNAME is not none -%}
        VPNINSTNAME="{{item.VPNINSTNAME}}",
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPVERSION=IPv4 时必选 --- -#}
    {%- if item.IPVERSION == 'IPv4' -%}
        SERVICEIPV4="{{item.SERVICEIPV4}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 配置S6a接口基于IP的宽带信令SCTP偶联配置的协议参数。

#### 3.1 //DC1

```jinja2
{%- for item in add_cpsctppara_list -%}
    ADD CPSCTPPARA:
    {#- --- 必选参数 --- -#}
    SCTPPARAINDEX={{item.SCTPPARAINDEX}},
    ;
{%- endfor -%}
```

### 4 **可选：**查看Diameter配置中“重连定时器（RECONNTIMER）”是否符合要求。如果“重连定时器（RECONNTIMER）”参数不为6s，则设置为6s。

### 在Diameter链路建立后，如果发生链路迁移或者重建，MME可以主动发送INIT消息给对端设备请求建链，可以使得链路不中断。但是如果对端设备不支持在UP状态时处理INIT消息，可能会导致链路中断，重建时间变长，具体时长取决于配置的“重连定时器（RECONNTIMER）”参数。

### 该定时器系统默认为30s，在目前灰度升级、扩容缩容等发生链路迁移场景下，造成链路中断时间过长，因此根据对端设备处理方式，建议将该参数配置为6s。

#### 4.1 //DC1

```jinja2
{%- if is_optional_reconnect_timer -%}
    {%- for item in set_dmfunc_list -%}
        SET DMFUNC:
        {#- --- 可选参数 --- -#}
        {%- if item.RECONNTIMER is not none -%}
            RECONNTIMER={{item.RECONNTIMER}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 5 增加Diameter本端信息 。

#### 5.1 //DC1

```jinja2
{%- for item in add_cpdmle_list -%}
    ADD CPDMLE:
    {#- --- 必选参数 --- -#}
    LOHSTNAME="{{item.LOHSTNAME}}",
    LORLMNAME="{{item.LORLMNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.LOINDEX is not none -%}
        LOINDEX={{item.LOINDEX}},
    {%- endif -%}
    {%- if item.LOINFONAME is not none -%}
        LOINFONAME="{{item.LOINFONAME}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 6 增加Diameter对端信息。

### 负荷分担容灾模式时，本UEG中的MME会通过S6a接口从另一UEG中的HSS接收cancel location报文，此场景需要配置本UEG中MME与另一UEG中HSS的对接。主备容灾模式时，仅需要配置本UEG中MME与HSS对接。

#### 6.1 //DC1

```jinja2
{%- for item in add_cpdmpe_list -%}
    ADD CPDMPE:
    {#- --- 必选参数 --- -#}
    PEERIDX={{item.PEERIDX}},
    PEERHTNAM="{{item.PEERHTNAM}}",
    {#- --- 可选参数 --- -#}
    {%- if item.PEERNAM is not none -%}
        PEERNAM="{{item.PEERNAM}}",
    {%- endif -%}
    {%- if item.APPCAP is not none -%}
        APPCAP={{item.APPCAP}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 7 配置Diameter链路集信息。

### 负荷分担容灾模式时，本UEG中的MME会通过S6a接口从另一UEG中的HSS接收cancel location报文，此场景需要配置本UEG中MME与另一UEG中HSS的对接。主备容灾模式时，仅需要配置本UEG中MME与HSS对接。

#### 7.1 //DC1

```jinja2
{%- for item in add_cpdmlks_list -%}
    ADD CPDMLKS:
    {#- --- 必选参数 --- -#}
    LINKSIDX={{item.LINKSIDX}},
    LOCALIDX={{item.LOCALIDX}},
    PEERIDX={{item.PEERIDX}},
    {#- --- 可选参数 --- -#}
    {%- if item.LSSELMODE is not none -%}
        LSSELMODE={{item.LSSELMODE}},
    {%- endif -%}
    {%- if item.LINKSNAM is not none -%}
        LINKSNAM="{{item.LINKSNAM}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 8 配置Diameter链路信息。

### 负荷分担容灾模式时，本UEG中的MME会通过S6a接口从另一UEG中的HSS接收cancel location报文，此场景需要配置本UEG中MME与另一UEG中HSS的对接。主备容灾模式时，仅需要配置本UEG中MME与HSS对接。

#### 8.1 //DC1

```jinja2
{%- for item in add_cpdmlnk_list -%}
    ADD CPDMLNK:
    {#- --- 必选参数 --- -#}
    LINKIDX={{item.LINKIDX}},
    LINKSIDX={{item.LINKSIDX}},
    SCTPINDX={{item.SCTPINDX}},
    {#- --- 可选参数 --- -#}
    {%- if item.VPNNAME is not none -%}
        VPNNAME="{{item.VPNNAME}}",
    {%- endif -%}
    {%- if item.IPTYPE is not none -%}
        IPTYPE={{item.IPTYPE}},
    {%- endif -%}
    {%- if item.LOCALPORT is not none -%}
        LOCALPORT={{item.LOCALPORT}},
    {%- endif -%}
    {%- if item.PEERPORT is not none -%}
        PEERPORT={{item.PEERPORT}},
    {%- endif -%}
    {%- if item.CLIORSER is not none -%}
        CLIORSER={{item.CLIORSER}},
    {%- endif -%}
    {%- if item.LINKNAM is not none -%}
        LINKNAM="{{item.LINKNAM}}",
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPTYPE=TPTADDR_TYPE_IPV4 时必选 --- -#}
    {%- if item.IPTYPE == 'TPTADDR_TYPE_IPV4' -%}
        LOCALIPV4_1="{{item.LOCALIPV4_1}}",
    {%- endif -%}
    {#- --- 条件必选：IPTYPE=TPTADDR_TYPE_IPV4 时必选 --- -#}
    {%- if item.IPTYPE == 'TPTADDR_TYPE_IPV4' -%}
        PEERIPV4_1="{{item.PEERIPV4_1}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：IPTYPE=TPTADDR_TYPE_IPV4 时可选 --- -#}
    {%- if item.IPTYPE == 'TPTADDR_TYPE_IPV4' -%}
        {%- if item.LOCALIPV4_2 is not none -%}
            LOCALIPV4_2="{{item.LOCALIPV4_2}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：IPTYPE=TPTADDR_TYPE_IPV4 时可选 --- -#}
    {%- if item.IPTYPE == 'TPTADDR_TYPE_IPV4' -%}
        {%- if item.PEERIPV4_2 is not none -%}
            PEERIPV4_2="{{item.PEERIPV4_2}}",
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 8.2 当UEG在核电等场景下使用4U4选型时，需额外配置以下5001端口的链路，非4U4选型下无需配置5001端口的链路。

#### 8.3 //DC1

```jinja2
{%- if is_scenario_4u4_selection -%}
    {%- for item in add_cpdmlnk_list_4 -%}
        ADD CPDMLNK:
        {#- --- 必选参数 --- -#}
        LINKIDX={{item.LINKIDX}},
        LINKSIDX={{item.LINKSIDX}},
        SCTPINDX={{item.SCTPINDX}},
        {#- --- 可选参数 --- -#}
        {%- if item.VPNNAME is not none -%}
            VPNNAME="{{item.VPNNAME}}",
        {%- endif -%}
        {%- if item.IPTYPE is not none -%}
            IPTYPE={{item.IPTYPE}},
        {%- endif -%}
        {%- if item.LOCALPORT is not none -%}
            LOCALPORT={{item.LOCALPORT}},
        {%- endif -%}
        {%- if item.PEERPORT is not none -%}
            PEERPORT={{item.PEERPORT}},
        {%- endif -%}
        {%- if item.CLIORSER is not none -%}
            CLIORSER={{item.CLIORSER}},
        {%- endif -%}
        {%- if item.LINKNAM is not none -%}
            LINKNAM="{{item.LINKNAM}}",
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：IPTYPE=TPTADDR_TYPE_IPV4 时必选 --- -#}
        {%- if item.IPTYPE == 'TPTADDR_TYPE_IPV4' -%}
            LOCALIPV4_1="{{item.LOCALIPV4_1}}",
        {%- endif -%}
        {#- --- 条件必选：IPTYPE=TPTADDR_TYPE_IPV4 时必选 --- -#}
        {%- if item.IPTYPE == 'TPTADDR_TYPE_IPV4' -%}
            PEERIPV4_1="{{item.PEERIPV4_1}}",
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：IPTYPE=TPTADDR_TYPE_IPV4 时可选 --- -#}
        {%- if item.IPTYPE == 'TPTADDR_TYPE_IPV4' -%}
            {%- if item.LOCALIPV4_2 is not none -%}
                LOCALIPV4_2="{{item.LOCALIPV4_2}}",
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：IPTYPE=TPTADDR_TYPE_IPV4 时可选 --- -#}
        {%- if item.IPTYPE == 'TPTADDR_TYPE_IPV4' -%}
            {%- if item.PEERIPV4_2 is not none -%}
                PEERIPV4_2="{{item.PEERIPV4_2}}",
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 9 **可选：**配置Diameter主机路由并将主机路由加入路由组。UDM部署在园区网络时，MME仅配置到同UEG内的HSS，对接时执行此步骤。

#### 9.1 配置到HSS的主机路由。

##### 9.1.1 //DC1

```jinja2
{%- if is_optional_diameter_host_route -%}
    {%- for item in add_dmhostrt_list -%}
        ADD DMHOSTRT:
        {#- --- 必选参数 --- -#}
        ROUTEIDX={{item.ROUTEIDX}},
        {#- --- 可选参数 --- -#}
        {%- if item.RSELMODE is not none -%}
            RSELMODE={{item.RSELMODE}},
        {%- endif -%}
        {%- if item.PEERSEL is not none -%}
            PEERSEL={{item.PEERSEL}},
        {%- endif -%}
        {%- if item.ROUTENAM is not none -%}
            ROUTENAM="{{item.ROUTENAM}}",
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：PEERSEL=PEER_INDEX 时必选 --- -#}
        {%- if item.PEERSEL == 'PEER_INDEX' -%}
            PEERIDX={{item.PEERIDX}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 9.2 将主机路由加入Diameter路由组中。

##### 9.2.1 //DC1

```jinja2
{%- if is_optional_diameter_host_route -%}
    {%- for item in add_dmrtgrp_list -%}
        ADD DMRTGRP:
        {#- --- 必选参数 --- -#}
        GRPIDX={{item.GRPIDX}},
        {#- --- 可选参数 --- -#}
        {%- if item.RTMODE is not none -%}
            RTMODE={{item.RTMODE}},
        {%- endif -%}
        {%- if item.RTPRIMODE is not none -%}
            RTPRIMODE={{item.RTPRIMODE}},
        {%- endif -%}
        {%- if item.ROUTEGRPNAM is not none -%}
            ROUTEGRPNAM="{{item.ROUTEGRPNAM}}",
        {%- endif -%}
        {#- --- 条件必选/可选参数 --- -#}
        {#- --- 路由索引: 条件必选(路由模式=HOST_ROUTE) / 条件可选(路由模式=REALM_ROUTE) --- -#}
        {%- if (item.RTMODE == 'HOST_ROUTE') -%}
            ROUTEIDX={{item.ROUTEIDX}},
        {%- elif (item.RTMODE == 'REALM_ROUTE') -%}
            {%- if item.ROUTEIDX is not none -%}
                ROUTEIDX={{item.ROUTEIDX}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 10 **可选：**可选：配置Diameter域路由并加入路由组。通过DRA和HSS对接时需执行此步骤，例如需要和中心侧HSS对接时可执行此步骤。

### 负荷分担容灾模式时，本UEG中的MME会通过S6a接口从另一UEG中的HSS接收cancel location报文，此场景需要配置本UEG中MME与另一UEG中HSS的对接。主备容灾模式时，仅需要配置本UEG中MME与HSS对接。

#### 10.1 配置Diameter域路由。

##### 10.1.1 //DC1

```jinja2
{%- if is_optional_diameter_realm_route -%}
    {%- for item in add_cpdmrt_list -%}
        ADD CPDMRT:
        {#- --- 必选参数 --- -#}
        ROUTEIDX={{item.ROUTEIDX}},
        PEERIDX={{item.PEERIDX}},
        {#- --- 可选参数 --- -#}
        {%- if item.APPNAM is not none -%}
            APPNAM={{item.APPNAM}},
        {%- endif -%}
        {%- if item.RSELMODE is not none -%}
            RSELMODE={{item.RSELMODE}},
        {%- endif -%}
        {%- if item.ROUTENAM is not none -%}
            ROUTENAM="{{item.ROUTENAM}}",
        {%- endif -%}
        {#- --- 条件必选/可选参数 --- -#}
        {#- --- 目的实体域名: 条件必选(是否默认路由=NO) / 条件可选(是否默认路由=YES) --- -#}
        {%- if (item.ISDEFAULT == 'NO') -%}
            REALMNAME="{{item.REALMNAME}}",
        {%- elif (item.ISDEFAULT == 'YES') -%}
            {%- if item.REALMNAME is not none -%}
                REALMNAME="{{item.REALMNAME}}",
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 10.2 配置Diameter路由组。如果配置了域路由，该路由需要加入路由组，与主机路由在同一个路由组。路由索引不需要配置，路由优先模式是优选主机路由，系统可以通过域名自动关联域路由。

##### 10.2.1 //DC1

```jinja2
{%- if is_optional_diameter_realm_route -%}
    {%- for item in add_dmrtgrp_list_2 -%}
        ADD DMRTGRP:
        {#- --- 必选参数 --- -#}
        GRPIDX={{item.GRPIDX}},
        {#- --- 可选参数 --- -#}
        {%- if item.RTMODE is not none -%}
            RTMODE={{item.RTMODE}},
        {%- endif -%}
        {%- if item.RTPRIMODE is not none -%}
            RTPRIMODE={{item.RTPRIMODE}},
        {%- endif -%}
        {%- if item.ROUTEGRPNAM is not none -%}
            ROUTEGRPNAM="{{item.ROUTEGRPNAM}}",
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：RTMODE=REALM_ROUTE 时可选 --- -#}
        {%- if item.RTMODE == 'REALM_ROUTE' -%}
            {%- if item.PEERIDX is not none -%}
                PEERIDX={{item.PEERIDX}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件必选/可选参数 --- -#}
        {#- --- 路由索引: 条件必选(路由模式=HOST_ROUTE) / 条件可选(路由模式=REALM_ROUTE) --- -#}
        {%- if (item.RTMODE == 'HOST_ROUTE') -%}
            ROUTEIDX={{item.ROUTEIDX}},
        {%- elif (item.RTMODE == 'REALM_ROUTE') -%}
            {%- if item.ROUTEIDX is not none -%}
                ROUTEIDX={{item.ROUTEIDX}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 11 配置IMSI与HSS的映射关系，用户可以根据该映射关系查找IMSI归属于哪个HSS的信息。

#### 11.1 //DC1

```jinja2
{%- for item in add_imsihss_list -%}
    ADD IMSIHSS:
    {#- --- 必选参数 --- -#}
    IMSIPRE="{{item.IMSIPRE}}",
    HSSRLM="{{item.HSSRLM}}",
    {#- --- 可选参数 --- -#}
    {%- if item.GRPIDX is not none -%}
        GRPIDX={{item.GRPIDX}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 12 **可选：**配置IPsec。园区DC的MME和中心侧网络的HSS对接时，可以配置IPsec增强数据报文传输安全性。

### 13 关闭周期性鉴权。

#### 13.1 //DC1

```jinja2
{%- for item in add_s1usrsecpara_list -%}
    ADD S1USRSECPARA:
    {#- --- 必选参数 --- -#}
    IMSIPRE="{{item.IMSIPRE}}",
    {#- --- 可选参数 --- -#}
    {%- if item.SECPLC is not none -%}
        SECPLC={{item.SECPLC}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：SECPLC=AUTHONLY/AUTHANDPROTECTED 时可选 --- -#}
    {%- if item.SECPLC in ['AUTHONLY', 'AUTHANDPROTECTED'] -%}
        {%- if item.OPTIONAL is not none -%}
            OPTIONAL={{item.OPTIONAL}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：OPTIONAL=YES 时可选 --- -#}
    {%- if item.OPTIONAL == 'YES' -%}
        {%- if item.AUTHEVENT is not none -%}
            AUTHEVENT={{item.AUTHEVENT}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：OPTIONAL=YES 时可选 --- -#}
    {%- if item.OPTIONAL == 'YES' -%}
        {%- if item.AUTHPERIOD is not none -%}
            AUTHPERIOD={{item.AUTHPERIOD}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```


---
id: ''
name: 配置到HSS的数据
ne_type: UNC
type: feature
description: 当运营商在部署分组交换网，新增MME或HSS时，在配置完成MME到HSS的路由数据后，可通过配置S6a接口数据建立MME到HSS的逻辑连接。不同场景的推荐配置方式见表1。  **表1** 不同操作场景推荐配置方式  | 操作场景 | 配置方式 | | --- | --- | | 漫游场景 | 方式一：本地用户优先使用MME直连的HSS，配置指导请参考本节，漫游用户使用归属地HSS，配置指导见本节配置到DRA的数据。 | |  | 方式二：本地用户和漫游用户都使用MME直连的HSS，请参考本节。 | | 新增MME(MME直接连HSS)或HSS | 请参考本节。 | | 新增MME(MME通过DRA和HSS对接) | 请参考配置到DRA的数据。 |
risk_level: ''
doc_source: ["网络部署","初始配置","UNC初始配置与调测","组网对接配置","配置AMF&MME&SGSN","配置MME","配置到HSS的数据"]
refs: []
metadata:
  DepOnLiveCfg: true
allowed-tools:
- getParameterValue('LST DMFUNC')
---
<!-- @mml:block=annotations -->
```text
## 操作场景
当运营商在部署分组交换网，新增MME或HSS时，在配置完成MME到HSS的路由数据后，可通过配置S6a接口数据建立MME到HSS的逻辑连接。不同场景的推荐配置方式见表1。**表1** 不同操作场景推荐配置方式| 操作场景 | 配置方式 || --- | --- || 漫游场景 | 方式一：本地用户优先使用MME直连的HSS，配置指导请参考本节，漫游用户使用归属地HSS，配置指导见本节配置到DRA的数据。 ||  | 方式二：本地用户和漫游用户都使用MME直连的HSS，请参考本节。 || 新增MME(MME直接连HSS)或HSS | 请参考本节。 || 新增MME(MME通过DRA和HSS对接) | 请参考配置到DRA的数据。 |

## 必备事项
前提条件

* 具备管理员权限的操作人员已经登录华为操作维护系统（登录U2020客户端或登录OM Portal）。

* UNC软件安装已完成。

* 请了解UNC各类接口的类型及命名规范，具体内容请参见业务组网与逻辑接口介绍。
* 对于IPv4组网，已完成自动部署配置动态路由OSPF+BFD组网（IPv4）、配置静态路由+BFD组网（IPv4）、配置BGP over OSPF/静态路由+BFD（IPv4）或手动部署配置动态路由OSPF+BFD组网（IPv4）、配置静态路由+BFD组网（IPv4）、配置BGP over OSPF/静态路由+BFD（IPv4）。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
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
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VPNINSTNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6MTU:
          name: 'IPv6 MTU大小'
          type: integer
          minimum: 1280
          maximum: 65534
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 1500
        SERVICEIPV6:
          name: '业务IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_sctppara_list:
      type: items
      properties:
        SCTPPARAINDEX:
          name: 'SCTP协议参数索引'
          type: integer
          minimum: 0
          maximum: 65534
          required: true
          description: 'S6a接口的SCTP协议参数与S1–MME接口的SCTP协议参数分开配置，便于后续局点搬迁或扩容时，不影响互联网元配置。可以通过**LST SCTPPARA**来查询已存在的SCTP协议参数记录。'
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
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_dmle_list:
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
    add_dmpe_list:
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
    add_dmlks_list:
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
    add_dmlnk_list:
      type: items
      properties:
        VPNNAME:
          name: 'vpn名称'
          type: string
          maxLength: 31
          required: false
          description: '配置Diameter链路。'
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
        LOCALIPV6_1:
          name: '本地IPv6地址1'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LOCALIPV6_2:
          name: '本地IPv6地址2'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PEERIPV6_1:
          name: '对端IPv6地址1'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PEERIPV6_2:
          name: '对端IPv6地址2'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
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
        PEERHTNAM:
          name: '对端主机名'
          type: string
          maxLength: 127
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PRIORITY:
          name: '优先级'
          type: integer
          minimum: 0
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        WEIGHT:
          name: '权重'
          type: integer
          minimum: 1
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 1
    add_dmrtgrp_list:
      type: items
      properties:
        GRPIDX:
          name: '路由组索引'
          type: integer
          minimum: 0
          maximum: 1023
          required: true
          description: 'UNC与HSS直连时，建议Diameter路由的“路由优选模式”设置成优先选择主机路由 。'
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
    add_dmrt_list:
      type: items
      properties:
        ROUTEIDX:
          name: '路由索引'
          type: integer
          minimum: 0
          maximum: 2047
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
    add_dmrtgrp_list_1:
      type: items
      properties:
        GRPIDX:
          name: '路由组索引'
          type: integer
          minimum: 0
          maximum: 1023
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
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
  examples:
    add_serviceip_list:
    - IPVERSION: IPv4
      SERVICEIPV4: '10.10.1.1'
      VPNINSTNAME: 'VPN_SIG'
      IPV6MTU: 1500
      SERVICEIPV6: ''
    add_sctppara_list:
    - SCTPPARAINDEX: 2
    set_dmfunc_list:
    - RECONNTIMER: 6
    add_dmle_list:
    - LOINDEX: 1
      LOHSTNAME: 'mme1.epc.mnc000.mcc123.3gppnetwork.org'
      LORLMNAME: 'epc.mnc000.mcc123.3gppnetwork.org'
      LOINFONAME: 'usn'
    add_dmpe_list:
    - PEERIDX: 1
      PEERHTNAM: 'hss1.epc.mnc000.mcc123.3gppnetwork.org'
      PEERNAM: 'HSS'
      APPCAP: S6a/S6d-1&S13-0&SLg-0&T6a/T6ai/T6b/T6bi-0
    add_dmlks_list:
    - LINKSIDX: 1
      LOCALIDX: 1
      PEERIDX: 1
      LSSELMODE: SELMODE_ACTIVE
      LINKSNAM: 'to-HSS'
    add_dmlnk_list:
    - VPNNAME: 'VPN_SIG'
      LINKIDX: 0
      IPTYPE: TPTADDR_TYPE_IPV4
      LOCALIPV4_1: '10.10.1.1'
      LOCALIPV4_2: '10.10.1.17'
      LOCALPORT: 5000
      PEERIPV4_1: '10.11.1.3'
      PEERIPV4_2: '10.11.2.3'
      PEERPORT: 5000
      CLIORSER: DIAM_CONN_CLIENT
      LINKSIDX: 1
      SCTPINDX: 2
      LINKNAM: 'dmlink'
      LOCALIPV6_1: ''
      LOCALIPV6_2: ''
      PEERIPV6_1: ''
      PEERIPV6_2: ''
    add_dmhostrt_list:
    - ROUTEIDX: 1
      RSELMODE: SELMODE_PRIORITY_WEIGHT
      PEERSEL: PEER_INDEX
      PEERIDX: 1
      ROUTENAM: 'usn'
      PEERHTNAM: ''
      PRIORITY: ''
      WEIGHT: 1
    add_dmrtgrp_list:
    - GRPIDX: 1
      RTMODE: HOST_ROUTE
      RTPRIMODE: HOST_ROUTE_PREFER
      ROUTEIDX: 1
      ROUTEGRPNAM: 'To_HSS'
      PEERIDX: ''
    add_dmrt_list:
    - ROUTEIDX: ''
      PEERIDX: ''
    add_dmrtgrp_list_1:
    - GRPIDX: ''
    add_imsihss_list:
    - IMSIPRE: '46000'
      HSSRLM: 'epc.mnc000.mcc123.3gppnetwork.org'
      GRPIDX: 1
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 进入“MML命令行-UNC”窗口。

### 2 配置S6a接口业务IP。

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
    {#- --- 条件必选：IPVERSION=IPv6 时必选 --- -#}
    {%- if item.IPVERSION == 'IPv6' -%}
        SERVICEIPV6="{{item.SERVICEIPV6}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：IPVERSION=IPv6 时可选 --- -#}
    {%- if item.IPVERSION == 'IPv6' -%}
        {%- if item.IPV6MTU is not none -%}
            IPV6MTU={{item.IPV6MTU}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 配置S6a接口基于IP的宽带信令SCTP偶联配置的协议参数。

```jinja2
{%- for item in add_sctppara_list -%}
    ADD SCTPPARA:
    {#- --- 必选参数 --- -#}
    SCTPPARAINDEX={{item.SCTPPARAINDEX}},
    ;
{%- endfor -%}
```

### 4 **可选：**查看Diameter配置中“重连定时器（RECONNTIMER）”是否符合要求。如果“重连定时器（RECONNTIMER）”参数不为6s，则设置为6s。

### 在Diameter链路建立后，如果发生链路迁移或者重建，UNC可以主动发送INIT消息给对端设备请求建链，可以使得链路不中断。但是如果对端设备不支持在UP状态时处理INIT消息，可能会导致链路中断，重建时间变长，具体时长取决于配置的“重连定时器（RECONNTIMER）”参数。

### 该定时器系统默认为30s，在目前灰度升级、扩容缩容等发生链路迁移场景下，造成链路中断时间过长，因此根据对端设备处理方式，建议将该参数配置为6s。

```jinja2
{%- set LST_DMFUNC=getParameterValue('LST DMFUNC') -%}
{%- if is_optional_reconntimer and not (LST_DMFUNC=='6') -%}
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

```jinja2
{%- for item in add_dmle_list -%}
    ADD DMLE:
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

```jinja2
{%- for item in add_dmpe_list -%}
    ADD DMPE:
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

```jinja2
{%- for item in add_dmlks_list -%}
    ADD DMLKS:
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

```jinja2
{%- for item in add_dmlnk_list -%}
    ADD DMLNK:
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
    {#- --- 条件必选：IPTYPE=TPTADDR_TYPE_IPV6 时必选 --- -#}
    {%- if item.IPTYPE == 'TPTADDR_TYPE_IPV6' -%}
        LOCALIPV6_1="{{item.LOCALIPV6_1}}",
    {%- endif -%}
    {#- --- 条件必选：IPTYPE=TPTADDR_TYPE_IPV6 时必选 --- -#}
    {%- if item.IPTYPE == 'TPTADDR_TYPE_IPV6' -%}
        PEERIPV6_1="{{item.PEERIPV6_1}}",
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
    {#- --- 条件可选：IPTYPE=TPTADDR_TYPE_IPV6 时可选 --- -#}
    {%- if item.IPTYPE == 'TPTADDR_TYPE_IPV6' -%}
        {%- if item.LOCALIPV6_2 is not none -%}
            LOCALIPV6_2="{{item.LOCALIPV6_2}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：IPTYPE=TPTADDR_TYPE_IPV6 时可选 --- -#}
    {%- if item.IPTYPE == 'TPTADDR_TYPE_IPV6' -%}
        {%- if item.PEERIPV6_2 is not none -%}
            PEERIPV6_2="{{item.PEERIPV6_2}}",
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 9 配置Diameter主机路由并将主机路由加入路由组。

#### 9.1 配置到HSS的主机路由。

```jinja2
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
    {#- --- 条件必选：PEERSEL=PEER_HOST_NAME 时必选 --- -#}
    {%- if item.PEERSEL == 'PEER_HOST_NAME' -%}
        PEERHTNAM="{{item.PEERHTNAM}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：RSELMODE=SELMODE_MASTER_SLAVE/SELMODE_PRIORITY_WEIGHT 时可选 --- -#}
    {%- if item.RSELMODE in ['SELMODE_MASTER_SLAVE', 'SELMODE_PRIORITY_WEIGHT'] -%}
        {%- if item.PRIORITY is not none -%}
            PRIORITY={{item.PRIORITY}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：RSELMODE=SELMODE_PRIORITY_WEIGHT 时可选 --- -#}
    {%- if item.RSELMODE == 'SELMODE_PRIORITY_WEIGHT' -%}
        {%- if item.WEIGHT is not none -%}
            WEIGHT={{item.WEIGHT}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 9.2 将主机路由加入Diameter路由组中。

```jinja2
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
```

### 10 **可选：**配置Diameter域路由并加入路由组。

#### 10.1 配置Diameter域路由。

```jinja2
{%- if is_optional_diameter_domain_route -%}
    {%- for item in add_dmrt_list -%}
        ADD DMRT:
        {#- --- 必选参数 --- -#}
        PEERIDX={{item.PEERIDX}},
        ROUTEIDX={{item.ROUTEIDX}},
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 10.1.1 MME与HSS直连，配置Diameter域路由的场景：

###### 10.1.1.1 IMSI号段不在IMSI与HSS映射关系范围内，系统自动组装域名。

###### 10.1.1.2 主机路由故障时，通过域路由找到对端。与主机路由备份，增强可靠性。

##### 10.1.2 当同一路由组内存在多条路由，需要按照优先级和权重方式选择对端时，选路模式为优先级权重，即RSELMODE=SELMODE\_PRIORITY\_WEIGHT。

##### 详细请参考**激活基于权重/优先级的Diameter负荷分担**。

#### 10.2 配置Diameter路由组。如果配置了域路由，该路由需要加入路由组，与主机路由在同一个路由组。路由索引不需要配置，路由优先模式是优选主机路由，系统可以通过域名自动关联域路由。

```jinja2
{%- if is_optional_diameter_domain_route -%}
    {%- for item in add_dmrtgrp_list_1 -%}
        ADD DMRTGRP:
        {#- --- 必选参数 --- -#}
        GRPIDX={{item.GRPIDX}},
        ;
    {%- endfor -%}
{%- endif -%}
```

### 11 配置IMSI与HSS的映射关系，用户可以根据该映射关系查找IMSI归属于哪个HSS的信息。

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


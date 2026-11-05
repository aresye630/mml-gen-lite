---
id: ''
name: 配置到DRA的数据
ne_type: UNC
type: feature
description: 当运营商在部署分组交换网，新增MME时，在配置完成MME到DRA的路由数据后，可通过配置S6a接口数据建立MME到DRA的逻辑连接。  3GPP引入了DRA（Diameter Router Agent）实体，DRA完成类似GERAN/UTRAN网络中的STP（Signaling Translation Point）的功能，根据用户的IMSI、网络域等信息进行域内HSS的寻址或者域间DRA的寻址。根据运营商的网络部署，MME可以通过DRA和HSS对接。  本地用户优先使用MME直连的HSS，配置指导请参考配置到HSS的数据；漫游用户使用归属地HSS，配置指导见本节。不同场景的推荐配置方式见表1。  **表1** 不同操作场景推荐配置方式  | 操作场景 | 配置方式 | | --- | --- | | 漫游场景 | 方式一：本地用户优先使用MME直连的HSS，配置指导请参考配置到HSS的数据，漫游用户使用归属地HSS，配置指导见本节。 | |  | 方式二：本地用户和漫游用户都使用MME直连的HSS，请参考配置到HSS的数据。 | | 新增MME(MME直接连HSS)或HSS | 请参考配置到HSS的数据。 | | 新增MME(MME通过DRA和HSS对接) | 请参考本节。 |
risk_level: ''
doc_source: ["网络部署","初始配置","UNC初始配置与调测","组网对接配置","配置AMF&MME&SGSN","配置MME","配置到DRA的数据"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
当运营商在部署分组交换网，新增MME时，在配置完成MME到DRA的路由数据后，可通过配置S6a接口数据建立MME到DRA的逻辑连接。3GPP引入了DRA（Diameter Router Agent）实体，DRA完成类似GERAN/UTRAN网络中的STP（Signaling Translation Point）的功能，根据用户的IMSI、网络域等信息进行域内HSS的寻址或者域间DRA的寻址。根据运营商的网络部署，MME可以通过DRA和HSS对接。本地用户优先使用MME直连的HSS，配置指导请参考配置到HSS的数据；漫游用户使用归属地HSS，配置指导见本节。不同场景的推荐配置方式见表1。**表1** 不同操作场景推荐配置方式| 操作场景 | 配置方式 || --- | --- || 漫游场景 | 方式一：本地用户优先使用MME直连的HSS，配置指导请参考配置到HSS的数据，漫游用户使用归属地HSS，配置指导见本节。 ||  | 方式二：本地用户和漫游用户都使用MME直连的HSS，请参考配置到HSS的数据。 || 新增MME(MME直接连HSS)或HSS | 请参考配置到HSS的数据。 || 新增MME(MME通过DRA和HSS对接) | 请参考本节。 |

## 必备事项
前提条件

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
          description: '与DRA对接的SCTP协议参数与S1–MME接口的SCTP协议参数分开配置，便于后续局点搬迁或扩容时，不影响互联网元配置。可以通过**LST SCTPPARA**来查询已存在的SCTP协议参数记录。'
          data_source: ''
          pattern: ''
          default: ''
        SCTPPARANAME:
          name: 'SCTP协议参数名'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'noname'
    add_dmle_list:
      type: items
      properties:
        LOINDEX:
          name: '本地实体索引'
          type: integer
          minimum: 0
          maximum: 31
          required: false
          description: '系统配置的Diameter本端标识可以通过****LST DMLE****命令查询。 如果已经存在DMLE，请使用现有的DMLE，无需添加。'
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
        PDTNAME:
          name: '产品名'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'vUSN'
    add_dmpe_list:
      type: items
      properties:
        PEERIDX:
          name: '对端实体索引'
          type: integer
          minimum: 0
          maximum: 639
          required: true
          description: '与DRA对接时，Diameter对端信息是对应的DRA信息，而不是HSS的信息。PEERHTNAM是DRA主机名，而不是HSS的主机名。  如果当前配置中存在到某个HSS的直连链路，那么用户同该HSS的非首次接入交互，将优先走此直连链路。详细请参考**Diameter路由查找整体层次**。'
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
        LINKSNAM:
          name: '链路集名称'
          type: string
          maxLength: 32
          required: false
          description: '配置Diameter链路。'
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
          description: ''
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
        CROSSIPFLAG:
          name: '交叉路径是否可用'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NO
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
    add_dmrt_list:
      type: items
      properties:
        ROUTEIDX:
          name: '路由索引'
          type: integer
          minimum: 0
          maximum: 2047
          required: true
          description: '当DRA采用冗余组网时，UNC需要配置多个Diameter对端。同时重复该步骤将多个不同对端实体加到同一个域路由中。  当同一路由下有多个对端，可以采用不同的方式选择Diameter对端，如轮选、主从、优先级权重、IMSI指定优选等。  如果需要按照优先级和权重方式选择对端进行负荷分担时，请参考**配置激活基于权重/优先级的Diameter负荷分担**。'
          data_source: ''
          pattern: ''
          default: ''
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
    softparaofbit_list:
      type: items
      properties:
        DT:
          name: 'DT'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PARANUM:
          name: 'PARANUM'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VALUE:
          name: 'VALUE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        POSITION:
          name: 'POSITION'
          type: string
          required: false
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
          description: 'HSSRLM配置的是HSS的域名，而不是DRA的域名。  HSS通用域名格式定义：epc.mnc<MNC>.mcc<MCC>.3gppnetwork.org。  如果没有配置IMSI和HSS的映射关系，需要配置默认路由才能找到对端。默认路由的配置方法请参考“增加Diameter域路由配置（****ADD DMRT****）”。'
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
  examples:
    add_serviceip_list:
    - IPVERSION: IPv4
      SERVICEIPV4: '192.168.140.1'
      VPNINSTNAME: 'VPN_SIG'
      IPV6MTU: 1500
      SERVICEIPV6: ''
    add_sctppara_list:
    - SCTPPARAINDEX: 0
      SCTPPARANAME: 'For_S6a'
    add_dmle_list:
    - LOINDEX: 0
      LOHSTNAME: 'mme1.epc.mnc015.mcc123.3gppnetwork.org'
      LORLMNAME: 'epc.mnc015.mcc123.3gppnetwork.org'
      PDTNAME: 'MME'
    add_dmpe_list:
    - PEERIDX: 0
      PEERHTNAM: 'dra1.epc.mnc015.mcc123.3gppnetwork.org'
    add_dmlks_list:
    - LINKSIDX: 0
      LOCALIDX: 0
      PEERIDX: 0
      LINKSNAM: 'LNKS1_DRA1'
    add_dmlnk_list:
    - VPNNAME: 'VPN_SIG'
      LINKIDX: 1
      IPTYPE: TPTADDR_TYPE_IPV4
      LOCALIPV4_1: '192.168.140.1'
      LOCALIPV4_2: '192.168.140.17'
      LOCALPORT: 3868
      PEERIPV4_1: '10.80.47.4'
      PEERIPV4_2: '10.80.47.5'
      PEERPORT: 3868
      CLIORSER: DIAM_CONN_CLIENT
      LINKSIDX: 0
      SCTPINDX: 0
      LINKNAM: 'DMLNK1_DRA1'
      CROSSIPFLAG: NO
      LOCALIPV6_1: ''
      LOCALIPV6_2: ''
      PEERIPV6_1: ''
      PEERIPV6_2: ''
    add_dmrt_list:
    - ROUTEIDX: 0
      RSELMODE: SELMODE_MASTER_SLAVE
      REALMNAME: 'epc.mnc015.mcc123.3gppnetwork.org'
      PEERIDX: 0
      ROUTENAM: 'rt to dra'
      ISDEFAULT: NO
      PRIORITY: ''
      WEIGHT: 1
    softparaofbit_list:
    - DT: DWORD_EX
      PARANUM: '34'
      VALUE: VALUE_1
      POSITION: '3'
    add_imsihss_list:
    - IMSIPRE: '46000'
      HSSRLM: 'epc.mnc015.mcc123.3gppnetwork.org'
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 进入“MML命令行-UNC”窗口。

### 2 配置业务IP。

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
    {#- --- 可选参数 --- -#}
    {%- if item.SCTPPARANAME is not none -%}
        SCTPPARANAME="{{item.SCTPPARANAME}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 **可选：**增加Diameter本端信息。

```jinja2
{%- if is_optional_add_diameter_local_entity -%}
    {%- for item in add_dmle_list -%}
        ADD DMLE:
        {#- --- 必选参数 --- -#}
        LOHSTNAME="{{item.LOHSTNAME}}",
        LORLMNAME="{{item.LORLMNAME}}",
        {#- --- 可选参数 --- -#}
        {%- if item.LOINDEX is not none -%}
            LOINDEX={{item.LOINDEX}},
        {%- endif -%}
        {%- if item.PDTNAME is not none -%}
            PDTNAME="{{item.PDTNAME}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 5 增加Diameter对端信息。

```jinja2
{%- for item in add_dmpe_list -%}
    ADD DMPE:
    {#- --- 必选参数 --- -#}
    PEERIDX={{item.PEERIDX}},
    PEERHTNAM="{{item.PEERHTNAM}}",
    ;
{%- endfor -%}
```

### 6 配置Diameter链路集信息。

```jinja2
{%- for item in add_dmlks_list -%}
    ADD DMLKS:
    {#- --- 必选参数 --- -#}
    LINKSIDX={{item.LINKSIDX}},
    LOCALIDX={{item.LOCALIDX}},
    PEERIDX={{item.PEERIDX}},
    {#- --- 可选参数 --- -#}
    {%- if item.LINKSNAM is not none -%}
        LINKSNAM="{{item.LINKSNAM}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 7 配置Diameter链路信息。同一个链路集中可以存在两条链路，即同时建立多条SCTP偶联，每条链路对应的SCTP参数可根据具体需求配置。 其中，LOCALIP为MME逻辑（业务）IP，PEERIP为DRA的IP，端口默认3868，需要和DRA协商一致。

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
    {%- if item.CROSSIPFLAG is not none -%}
        CROSSIPFLAG={{item.CROSSIPFLAG}},
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

### 8 配置Diameter路由。

#### 8.1 配置Diameter域路由。

```jinja2
{%- for item in add_dmrt_list -%}
    ADD DMRT:
    {#- --- 必选参数 --- -#}
    ROUTEIDX={{item.ROUTEIDX}},
    PEERIDX={{item.PEERIDX}},
    {#- --- 可选参数 --- -#}
    {%- if item.RSELMODE is not none -%}
        RSELMODE={{item.RSELMODE}},
    {%- endif -%}
    {%- if item.ROUTENAM is not none -%}
        ROUTENAM="{{item.ROUTENAM}}",
    {%- endif -%}
    {%- if item.ISDEFAULT is not none -%}
        ISDEFAULT={{item.ISDEFAULT}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：RSELMODE=SELMODE_MASTER_SLAVE/SELMODE_PRIORITY_WEIGHT/SELMODE_IMSI_PRIORITY 时可选 --- -#}
    {%- if item.RSELMODE in ['SELMODE_MASTER_SLAVE', 'SELMODE_PRIORITY_WEIGHT', 'SELMODE_IMSI_PRIORITY'] -%}
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
```

#### 8.2 **可选：**配置Diameter路由组。

##### 8.2.1 当域路由的选路模式为IMSI指定优选，即RSELMODE=SELMODE\_IMSI\_PRIORITY时，路由索引和对端实体索引必须配置。

##### 8.2.2 建议全部与DRA连接的时“路由优选模式”选择域路由优先，与HSS直连时“路由优选模式”选择主机路由优先。

##### 如果与DRA连接时“路由优选模式”选择主机路由优先，需要DRA支持通过IMSI寻址HSS。

#### 8.3 **可选：**MME会自主学习HSS的主机名，后续通过自主学习的HSS的主机名寻找路由。当MME与HSS之间只有通过DRA连接的主机路由且没有可用的域路由时，需要将软参DWORD\_EX34 BIT3设置为“1”，对于Purge UE Request消息优先使用配置的HSS主机名。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该softparaofbit_list的变量区（command: SOFTPARAOFBIT） -#}
<!-- MISSING_MACRO: command=SOFTPARAOFBIT list_name=softparaofbit_list step_id=8.3 -->
```

#### 当MME与HSS之间只有通过DRA连接的主机路由且没有可用的域路由时，如果软参DWORD\_EX34 BIT3设置为“0”，Purge UE Request消息会发送失败。

### 9 **可选：**配置IMSI与HSS的映射关系，用户可以根据该映射关系查找IMSI归属的HSS信息。

```jinja2
{%- if is_optional_configure_imsi_hss_mapping -%}
    {%- for item in add_imsihss_list -%}
        ADD IMSIHSS:
        {#- --- 必选参数 --- -#}
        IMSIPRE="{{item.IMSIPRE}}",
        HSSRLM="{{item.HSSRLM}}",
        ;
    {%- endfor -%}
{%- endif -%}
```


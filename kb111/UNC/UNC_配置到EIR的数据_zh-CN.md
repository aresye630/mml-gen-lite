---
id: ''
name: 配置到EIR的数据
ne_type: UNC
type: feature
description: 当运营商在部署分组交换网，新增MME时，在配置完成MME到EIR的路由数据后，可通过配置S13接口数据建立MME到EIR的逻辑连接。
risk_level: ''
doc_source: ["网络部署","初始配置","UNC初始配置与调测","组网对接配置","配置AMF&MME&SGSN","配置MME","配置到EIR的数据"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
当运营商在部署分组交换网，新增MME时，在配置完成MME到EIR的路由数据后，可通过配置S13接口数据建立MME到EIR的逻辑连接。

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
          description: 'S13接口的SCTP协议参数与S1–MME接口的SCTP协议参数分开配置，便于后续局点搬迁或扩容时，不影响互联网元配置。可以通过**LST SCTPPARA**来查询已存在的SCTP协议参数记录'
          data_source: ''
          pattern: ''
          default: ''
        HBINTERVAL:
          name: '心跳间隔（ms）'
          type: integer
          minimum: 10
          maximum: 60000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 3000
        MAXASSOCRETR:
          name: '偶联最大重发次数'
          type: integer
          minimum: 1
          maximum: 254
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 5
        MAXPATHRETR:
          name: '路径最大重发次数'
          type: integer
          minimum: 1
          maximum: 254
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 4
        SCTPPARANAME:
          name: 'SCTP协议参数名'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'noname'
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
          description: '配置Diameter链路。'
          data_source: ''
          pattern: ''
          default: 'noname'
    add_dmrt_list:
      type: items
      properties:
        ROUTEIDX:
          name: '路由索引'
          type: integer
          minimum: 0
          maximum: 2047
          required: true
          description: '配置Diameter路由。'
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
    add_eir_list:
      type: items
      properties:
        EIRRLM:
          name: 'EIR域名'
          type: string
          maxLength: 127
          required: true
          description: '配置EIR。'
          data_source: ''
          pattern: ''
          default: ''
        EIRHTN:
          name: 'EIR主机名'
          type: string
          maxLength: 127
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
    - SCTPPARAINDEX: 6
      HBINTERVAL: 5000
      MAXASSOCRETR: 10
      MAXPATHRETR: 5
      SCTPPARANAME: 'S13'
    set_dmfunc_list:
    - RECONNTIMER: 6
    add_dmpe_list:
    - PEERIDX: 1
      PEERHTNAM: 'EIR.epc.mnc015.mcc123.3gppnetwork.org'
      PEERNAM: 'EIR'
    add_dmlks_list:
    - LINKSIDX: 1
      LOCALIDX: 0
      PEERIDX: 1
      LSSELMODE: SELMODE_LOAD_BALAN
      LINKSNAM: 'EIR'
    add_dmrt_list:
    - ROUTEIDX: 1
      APPNAM: S13
      RSELMODE: SELMODE_ROUND_ROBIN
      REALMNAME: 'epc.mnc015.mcc123.3gppnetwork.org'
      PEERIDX: 1
      ROUTENAM: 'EIR'
      ISDEFAULT: NO
      PRIORITY: ''
      WEIGHT: 1
    add_dmlnk_list:
    - VPNNAME: 'VPN_SIG'
      LINKIDX: 0
      IPTYPE: TPTADDR_TYPE_IPV4
      LOCALIPV4_1: '10.10.1.1'
      LOCALIPV4_2: '10.10.1.17'
      LOCALPORT: 50470
      PEERIPV4_1: '10.11.1.3'
      PEERIPV4_2: '10.11.2.3'
      PEERPORT: 50470
      LINKSIDX: 1
      SCTPINDX: 4
      LINKNAM: 'To-HSS1'
      LOCALIPV6_1: ''
      LOCALIPV6_2: ''
      PEERIPV6_1: ''
      PEERIPV6_2: ''
    add_eir_list:
    - EIRRLM: 'epc.mnc015.mcc123.3gppnetwork.org'
      EIRHTN: 'EIR.epc.mnc015.mcc123.3gppnetwork.org'
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 进入“MML命令行-UNC”窗口。

### 2 配置S13接口业务IP。

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

### 3 配置S13接口基于IP的宽带信令SCTP偶联配置的协议参数。

```jinja2
{%- for item in add_sctppara_list -%}
    ADD SCTPPARA:
    {#- --- 必选参数 --- -#}
    SCTPPARAINDEX={{item.SCTPPARAINDEX}},
    {#- --- 可选参数 --- -#}
    {%- if item.HBINTERVAL is not none -%}
        HBINTERVAL={{item.HBINTERVAL}},
    {%- endif -%}
    {%- if item.MAXASSOCRETR is not none -%}
        MAXASSOCRETR={{item.MAXASSOCRETR}},
    {%- endif -%}
    {%- if item.MAXPATHRETR is not none -%}
        MAXPATHRETR={{item.MAXPATHRETR}},
    {%- endif -%}
    {%- if item.SCTPPARANAME is not none -%}
        SCTPPARANAME="{{item.SCTPPARANAME}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 **可选：**查看Diameter配置中“重连定时器（RECONNTIMER）”是否符合要求。如果“重连定时器（RECONNTIMER）”参数不为6s，则设置为6s。

### 在Diameter链路建立后，如果发生链路迁移或者重建，UNC可以主动发送INIT消息给对端设备请求建链，可以使得链路不中断。但是如果对端设备不支持在UP状态时处理INIT消息，可能会导致链路中断，重建时间变长，具体时长取决于配置的“重连定时器（RECONNTIMER）”参数。

### 该定时器系统默认为30s，在目前灰度升级、扩容缩容等发生链路迁移场景下，造成链路中断时间过长，因此根据对端设备处理方式，建议将该参数配置为6s。

```jinja2
{%- if is_optional_check_reconnect_timer -%}
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

### 5 **可选：**配置Diameter本地信息。

### 如果已经存在本地实体索引（LOINDEX）为0的DMLE，请使用现有DMLE，无需添加，跳过此步。

### 如果需要使用其他本地实体索引，请参考DWORD\_EX18 BIT1–6的配置说明。DWORD\_EX18 BIT6 控制UNC在发送S13接口消息时是否根据“DWORD\_EX18” BIT1-BIT5设置的“本地实体索引”携带对应的本地域名和本地主机名，DWORD\_EX18 BIT1-BIT5 控制UNC根据指定的ADD DMLE记录携带本地域名和本地主机名。

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

### 8 配置Diameter路由信息。

```jinja2
{%- for item in add_dmrt_list -%}
    ADD DMRT:
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

### 9 配置Diameter链路信息。

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

### 10 配置EIR。

```jinja2
{%- for item in add_eir_list -%}
    ADD EIR:
    {#- --- 必选参数 --- -#}
    EIRRLM="{{item.EIRRLM}}",
    {#- --- 可选参数 --- -#}
    {%- if item.EIRHTN is not none -%}
        EIRHTN="{{item.EIRHTN}}",
    {%- endif -%}
    ;
{%- endfor -%}
```


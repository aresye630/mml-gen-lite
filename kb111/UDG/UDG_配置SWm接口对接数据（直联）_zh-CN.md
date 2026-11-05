---
id: ''
name: 配置SWm接口对接数据（直联）
ne_type: UDG
type: feature
description: 专网UPF采用华为UDG产品，新增SWm接口用于与Non-SIM AAA UDM-UIM进行消息交互，目的是进行家庭网关的身份认证。  该任务旨在指导操作人员完成UPF的SWm接口对接配置。  * SWm接口当前版本仅支持IPv4栈类型。 * 专网UPF配置SWm接口时，不支持开启入不转板功能特性。
risk_level: ''
doc_source: ["特性部署","业务专题","5G Core 一跳入家解决方案","一跳入家解决方案（基于非3GPP接入方案）","业务初始部署与调测","部署一跳入家","配置一跳入家专网UPF","配置SWm接口对接数据（直联）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
专网UPF采用华为UDG产品，新增SWm接口用于与Non-SIM AAA UDM-UIM进行消息交互，目的是进行家庭网关的身份认证。该任务旨在指导操作人员完成UPF的SWm接口对接配置。* SWm接口当前版本仅支持IPv4栈类型。* 专网UPF配置SWm接口时，不支持开启入不转板功能特性。

## 必备事项
前提条件

前提条件

* UPF软件安装已完成。
* UPF初始配置已完成。
* 已完成一跳入家依赖功能的License加载。
* 已完成一跳入家要求的移动VPN相关配置。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    add_vpninst_list:
      type: items
      properties:
        VPNINSTANCE:
          name: 'VPN实例名'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_l3vpninst_list:
      type: items
      properties:
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: true
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_vpninstaf_list:
      type: items
      properties:
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AFTYPE:
          name: '地址族类型'
          type: string
          enum:
          - ipv4uni
          - ipv6uni
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_upconcenpoint_list:
      type: items
      properties:
        SWMCONCENMODE:
          name: 'Swm集中点模式'
          type: string
          enum:
          - LOCALIP_PEER
          - LOCALPORT
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_logicinf_list:
      type: items
      properties:
        NAME:
          name: '逻辑接口名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPVERSION:
          name: '逻辑接口的IP版本'
          type: string
          enum:
          - IPV4
          - IPV6
          - IPVER_ALL
          required: true
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV4ADDRESS1:
          name: '逻辑接口的IPv4地址1'
          type: string
          maxLength: 15
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV4MASK1:
          name: '逻辑接口的IPv4掩码1'
          type: string
          maxLength: 15
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        VPNINSTANCE:
          name: 'VPN实例名称'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV4ADDRESS2:
          name: '逻辑接口的IPv4地址2'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV4MASK2:
          name: '逻辑接口的IPv4掩码2'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV4MTU:
          name: 'IPv4逻辑接口MTU（字节）'
          type: integer
          minimum: 328
          maximum: 9600
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 1500
        IPV6ADDRESS1:
          name: '逻辑接口的IPv6地址1'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6ADDRESS2:
          name: '逻辑接口的IPv6地址2'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6MTU:
          name: 'IPv6逻辑接口MTU（字节）'
          type: integer
          minimum: 1280
          maximum: 9600
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 1800
        IPV6PREFIXLEN1:
          name: 'IPv6前缀长度1'
          type: integer
          minimum: 1
          maximum: 128
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6PREFIXLEN2:
          name: 'IPv6前缀长度2'
          type: integer
          minimum: 1
          maximum: 128
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_updiamlocinfo_list:
      type: items
      properties:
        HOSTNAME:
          name: '本端主机名'
          type: string
          minLength: 0
          maxLength: 127
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        REALMNAME:
          name: '本端域名'
          type: string
          minLength: 0
          maxLength: 127
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PRODUCTNAME:
          name: '产品名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        ORIGINSTATEID:
          name: 'Origin-State-Id AVP使能开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
        SUPPORTVENDORID:
          name: 'Supported-Vendor-Id AVP使能开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
    add_updiameteraaa_list:
      type: items
      properties:
        HOSTNAME:
          name: '主机名称'
          type: string
          minLength: 0
          maxLength: 127
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        REALMNAME:
          name: '本端域名'
          type: string
          minLength: 0
          maxLength: 127
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        VPNINSTANCE:
          name: 'VPN实例名称'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_updiampeeraddr_list:
      type: items
      properties:
        HOSTNAME:
          name: '主机名称'
          type: string
          minLength: 0
          maxLength: 127
          required: true
          description: '-'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        ADDRTYPE:
          name: '地址类型'
          type: string
          enum:
          - IPv4
          - IPv6
          - SCTP
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPV4ADDRESS:
          name: 'IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV6ADDRESS:
          name: 'IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PORT:
          name: '端口号'
          type: integer
          minimum: 1
          maximum: 65534
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 3868
        SCTPENDPOINT:
          name: 'SCTP端点名称'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_updiamconngrp_list:
      type: items
      properties:
        CONNGROUPNAME:
          name: 'Diameter链路组名'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: '该命令用于指定本端主机名与指定对端服务器之间建立一组Diameter链路。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        LOCALHOSTNAME:
          name: '本端主机名'
          type: string
          minLength: 0
          maxLength: 127
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        APPLICATION:
          name: 'Diameter应用'
          type: string
          enum:
          - SWM
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        PEERHOSTNAME:
          name: '对端主机名'
          type: string
          minLength: 0
          maxLength: 127
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        SELECTMODE:
          name: '链路选择模式'
          type: string
          enum:
          - MASTER_SLAVE
          - ROUND_ROBIN
          - SESSION_ID
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: SESSION_ID
    add_updiamconn_list:
      type: items
      properties:
        DIAMCONNGRP:
          name: 'Diameter链路组名'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: '增加Diameter链路。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        LOCINTERFACE:
          name: '本端接口名'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        PEERADDRTYPE:
          name: '对端地址类型'
          type: string
          enum:
          - IPv4
          - IPv6
          - SCTP
          required: false
          description: '*-*'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PEERPORT:
          name: '对端端口'
          type: integer
          minimum: 1
          maximum: 65534
          required: false
          description: '*-*'
          data_source: '对端协商'
          pattern: ''
          default: ''
        PEERIPV4ADDR:
          name: '对端IPV4地址'
          type: string
          maxLength: 15
          required: false
          description: 'IPv4地址类型。不支持0.0.0.0和255.255.255.255。'
          data_source: '对端协商'
          pattern: ''
          default: ''
        LOCALPORT:
          name: '本端端口'
          type: integer
          minimum:
          - 0
          - 19865
          maximum:
          - 0
          - 19928
          required: false
          description: '取值范围19865~19928。'
          data_source: '对端协商'
          pattern: ''
          default: 0
        PEERIPV6ADDR:
          name: '对端IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PEERSCTPENDPT:
          name: '对端SCTP端点名称'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        REVERSEIP:
          name: 'SCTP建链交换本端IP地址'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
    add_updiamaaagrp_list:
      type: items
      properties:
        GROUPNAME:
          name: 'Diameter AAA组名'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_updiamaaabndg_list:
      type: items
      properties:
        GROUPNAME:
          name: 'Diameter AAA组名'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SERVERTYPE:
          name: '服务器类型'
          type: string
          enum:
          - PARA_3GPP
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        HOSTNAME:
          name: '主机名'
          type: string
          minLength: 0
          maxLength: 127
          required: true
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        PRIORSEC:
          name: '主备用标记'
          type: string
          enum:
          - PRIMARY
          - SECONDARY
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_upapndiamaaag_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '专用DNN的APN。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        GROUPNAME:
          name: 'Diameter AAA组名'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
  examples:
    add_vpninst_list:
    - VPNINSTANCE: 'VPN_Signaling'
    add_l3vpninst_list:
    - VRFNAME: 'VPN_Signaling'
    add_vpninstaf_list:
    - VRFNAME: 'VPN_Signaling'
      AFTYPE: ipv4uni
    set_upconcenpoint_list:
    - SWMCONCENMODE: LOCALPORT
    add_logicinf_list:
    - NAME: 'swmif1/0/0'
      IPVERSION: IPV4
      IPV4ADDRESS1: '192.168.1.1'
      IPV4MASK1: '255.255.255.255'
      VPNINSTANCE: 'VPN_Signaling'
      IPV4ADDRESS2: ''
      IPV4MASK2: ''
      IPV4MTU: 1500
      IPV6ADDRESS1: ''
      IPV6ADDRESS2: ''
      IPV6MTU: 1800
      IPV6PREFIXLEN1: ''
      IPV6PREFIXLEN2: ''
    add_updiamlocinfo_list:
    - HOSTNAME: 'udg_1'
      REALMNAME: 'huawei.com'
      PRODUCTNAME: 'udg@huawei.com'
      ORIGINSTATEID: DISABLE
      SUPPORTVENDORID: DISABLE
    add_updiameteraaa_list:
    - HOSTNAME: '3gppaaa'
      REALMNAME: '3gppaaa.huawei.com'
      VPNINSTANCE: 'VPN_Signaling'
    add_updiampeeraddr_list:
    - HOSTNAME: '3gppaaa'
      ADDRTYPE: IPv4
      IPV4ADDRESS: '10.10.10.1'
      IPV6ADDRESS: ''
      PORT: 3868
      SCTPENDPOINT: ''
    add_updiamconngrp_list:
    - CONNGROUPNAME: 'groupname'
      LOCALHOSTNAME: 'udg_1'
      APPLICATION: SWM
      PEERHOSTNAME: '3gppaaa'
      SELECTMODE: SESSION_ID
    add_updiamconn_list:
    - DIAMCONNGRP: 'groupname'
      LOCINTERFACE: 'swmif1/0/0'
      PEERADDRTYPE: IPv4
      PEERPORT: 3868
      PEERIPV4ADDR: '10.10.10.1'
      LOCALPORT: 19865
      PEERIPV6ADDR: ''
      PEERSCTPENDPT: ''
      REVERSEIP: DISABLE
    add_updiamaaagrp_list:
    - GROUPNAME: 'groupname'
    add_updiamaaabndg_list:
    - GROUPNAME: 'groupname'
      SERVERTYPE: PARA_3GPP
      HOSTNAME: '3gppaaa'
      PRIORSEC: PRIMARY
    add_upapndiamaaag_list:
    - APN: '062apn1.com'
      GROUPNAME: 'groupname'
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 创建VPN实例。可选配置，如果已配置VPN跳过此步骤。

```jinja2
{%- if is_optional_create_vpn_instance -%}
    {%- for item in add_vpninst_list -%}
        ADD VPNINST:
        {#- --- 必选参数 --- -#}
        VPNINSTANCE="{{item.VPNINSTANCE}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_optional_create_vpn_instance -%}
    {%- for item in add_l3vpninst_list -%}
        ADD L3VPNINST:
        {#- --- 必选参数 --- -#}
        VRFNAME="{{item.VRFNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_optional_create_vpn_instance -%}
    {%- for item in add_vpninstaf_list -%}
        ADD VPNINSTAF:
        {#- --- 必选参数 --- -#}
        VRFNAME="{{item.VRFNAME}}",
        AFTYPE={{item.AFTYPE}},
        ;
    {%- endfor -%}
{%- endif -%}
```

### 2 配置SWm接口的集中点模式为本端端口模式。

```jinja2
{%- for item in set_upconcenpoint_list -%}
    SET UPCONCENPOINT:
    {#- --- 可选参数 --- -#}
    {%- if item.SWMCONCENMODE is not none -%}
        SWMCONCENMODE={{item.SWMCONCENMODE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 配置SWm逻辑接口，VPN实例名称为VPN\_Signaling。

```jinja2
{%- for item in add_logicinf_list -%}
    ADD LOGICINF:
    {#- --- 必选参数 --- -#}
    NAME="{{item.NAME}}",
    IPVERSION={{item.IPVERSION}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPVERSION=IPV4/IPVER_ALL 时必选 --- -#}
    {%- if item.IPVERSION in ['IPV4', 'IPVER_ALL'] -%}
        IPV4ADDRESS1="{{item.IPV4ADDRESS1}}",
    {%- endif -%}
    {#- --- 条件必选：IPVERSION=IPV4/IPVER_ALL 时必选 --- -#}
    {%- if item.IPVERSION in ['IPV4', 'IPVER_ALL'] -%}
        IPV4MASK1="{{item.IPV4MASK1}}",
    {%- endif -%}
    {#- --- 条件必选：IPVERSION=IPVER_ALL/IPV6 时必选 --- -#}
    {%- if item.IPVERSION in ['IPVER_ALL', 'IPV6'] -%}
        IPV6ADDRESS1="{{item.IPV6ADDRESS1}}",
    {%- endif -%}
    {#- --- 条件必选：IPVERSION=IPVER_ALL/IPV6 时必选 --- -#}
    {%- if item.IPVERSION in ['IPVER_ALL', 'IPV6'] -%}
        IPV6PREFIXLEN1={{item.IPV6PREFIXLEN1}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：IPVERSION=IPV4/IPVER_ALL/IPV6 时可选 --- -#}
    {%- if item.IPVERSION in ['IPV4', 'IPVER_ALL', 'IPV6'] -%}
        {%- if item.VPNINSTANCE is not none -%}
            VPNINSTANCE="{{item.VPNINSTANCE}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：IPVERSION=IPV4/IPVER_ALL 时可选 --- -#}
    {%- if item.IPVERSION in ['IPV4', 'IPVER_ALL'] -%}
        {%- if item.IPV4ADDRESS2 is not none -%}
            IPV4ADDRESS2="{{item.IPV4ADDRESS2}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：IPVERSION=IPV4/IPVER_ALL 时可选 --- -#}
    {%- if item.IPVERSION in ['IPV4', 'IPVER_ALL'] -%}
        {%- if item.IPV4MASK2 is not none -%}
            IPV4MASK2="{{item.IPV4MASK2}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：IPVERSION=IPV4/IPVER_ALL 时可选 --- -#}
    {%- if item.IPVERSION in ['IPV4', 'IPVER_ALL'] -%}
        {%- if item.IPV4MTU is not none -%}
            IPV4MTU={{item.IPV4MTU}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：IPVERSION=IPVER_ALL/IPV6 时可选 --- -#}
    {%- if item.IPVERSION in ['IPVER_ALL', 'IPV6'] -%}
        {%- if item.IPV6ADDRESS2 is not none -%}
            IPV6ADDRESS2="{{item.IPV6ADDRESS2}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：IPVERSION=IPVER_ALL/IPV6 时可选 --- -#}
    {%- if item.IPVERSION in ['IPVER_ALL', 'IPV6'] -%}
        {%- if item.IPV6MTU is not none -%}
            IPV6MTU={{item.IPV6MTU}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：IPVERSION=IPVER_ALL/IPV6 时可选 --- -#}
    {%- if item.IPVERSION in ['IPVER_ALL', 'IPV6'] -%}
        {%- if item.IPV6PREFIXLEN2 is not none -%}
            IPV6PREFIXLEN2={{item.IPV6PREFIXLEN2}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 配置Diameter。

#### 4.1 配置本端端点的主机信息。

```jinja2
{%- for item in add_updiamlocinfo_list -%}
    ADD UPDIAMLOCINFO:
    {#- --- 必选参数 --- -#}
    HOSTNAME="{{item.HOSTNAME}}",
    REALMNAME="{{item.REALMNAME}}",
    PRODUCTNAME="{{item.PRODUCTNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.ORIGINSTATEID is not none -%}
        ORIGINSTATEID={{item.ORIGINSTATEID}},
    {%- endif -%}
    {%- if item.SUPPORTVENDORID is not none -%}
        SUPPORTVENDORID={{item.SUPPORTVENDORID}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 4.2 配置Non-SIM AAA。

```jinja2
{%- for item in add_updiameteraaa_list -%}
    ADD UPDIAMETERAAA:
    {#- --- 必选参数 --- -#}
    HOSTNAME="{{item.HOSTNAME}}",
    REALMNAME="{{item.REALMNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.VPNINSTANCE is not none -%}
        VPNINSTANCE="{{item.VPNINSTANCE}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_updiampeeraddr_list -%}
    ADD UPDIAMPEERADDR:
    {#- --- 必选参数 --- -#}
    HOSTNAME="{{item.HOSTNAME}}",
    ADDRTYPE={{item.ADDRTYPE}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：ADDRTYPE=IPv4 时必选 --- -#}
    {%- if item.ADDRTYPE == 'IPv4' -%}
        IPV4ADDRESS="{{item.IPV4ADDRESS}}",
    {%- endif -%}
    {#- --- 条件必选：ADDRTYPE=IPv6 时必选 --- -#}
    {%- if item.ADDRTYPE == 'IPv6' -%}
        IPV6ADDRESS="{{item.IPV6ADDRESS}}",
    {%- endif -%}
    {#- --- 条件必选：ADDRTYPE=SCTP 时必选 --- -#}
    {%- if item.ADDRTYPE == 'SCTP' -%}
        SCTPENDPOINT="{{item.SCTPENDPOINT}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：ADDRTYPE=IPv4/IPv6 时可选 --- -#}
    {%- if item.ADDRTYPE in ['IPv4', 'IPv6'] -%}
        {%- if item.PORT is not none -%}
            PORT={{item.PORT}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 4.3 建立本端与对端的链路组，并配置链路选择模式。

```jinja2
{%- for item in add_updiamconngrp_list -%}
    ADD UPDIAMCONNGRP:
    {#- --- 必选参数 --- -#}
    CONNGROUPNAME="{{item.CONNGROUPNAME}}",
    LOCALHOSTNAME="{{item.LOCALHOSTNAME}}",
    APPLICATION={{item.APPLICATION}},
    PEERHOSTNAME="{{item.PEERHOSTNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.SELECTMODE is not none -%}
        SELECTMODE={{item.SELECTMODE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 4.4 配置到Non-SIM AAA的链路。

```jinja2
{%- for item in add_updiamconn_list -%}
    ADD UPDIAMCONN:
    {#- --- 必选参数 --- -#}
    DIAMCONNGRP="{{item.DIAMCONNGRP}}",
    LOCINTERFACE="{{item.LOCINTERFACE}}",
    {#- --- 可选参数 --- -#}
    {%- if item.PEERADDRTYPE is not none -%}
        PEERADDRTYPE={{item.PEERADDRTYPE}},
    {%- endif -%}
    {%- if item.LOCALPORT is not none -%}
        LOCALPORT={{item.LOCALPORT}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：PEERADDRTYPE=IPv4 时必选 --- -#}
    {%- if item.PEERADDRTYPE == 'IPv4' -%}
        PEERIPV4ADDR="{{item.PEERIPV4ADDR}}",
    {%- endif -%}
    {#- --- 条件必选：PEERADDRTYPE=IPv6 时必选 --- -#}
    {%- if item.PEERADDRTYPE == 'IPv6' -%}
        PEERIPV6ADDR="{{item.PEERIPV6ADDR}}",
    {%- endif -%}
    {#- --- 条件必选：PEERADDRTYPE=SCTP 时必选 --- -#}
    {%- if item.PEERADDRTYPE == 'SCTP' -%}
        PEERSCTPENDPT="{{item.PEERSCTPENDPT}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：PEERADDRTYPE=IPv4/IPv6 时可选 --- -#}
    {%- if item.PEERADDRTYPE in ['IPv4', 'IPv6'] -%}
        {%- if item.PEERPORT is not none -%}
            PEERPORT={{item.PEERPORT}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：PEERADDRTYPE=SCTP 时可选 --- -#}
    {%- if item.PEERADDRTYPE == 'SCTP' -%}
        {%- if item.REVERSEIP is not none -%}
            REVERSEIP={{item.REVERSEIP}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 4.5 设置Non-SIM AAA服务器组。

```jinja2
{%- for item in add_updiamaaagrp_list -%}
    ADD UPDIAMAAAGRP:
    {#- --- 必选参数 --- -#}
    GROUPNAME="{{item.GROUPNAME}}",
    ;
{%- endfor -%}
```

#### 4.6 指定主用Non-SIM AAA服务器组。

```jinja2
{%- for item in add_updiamaaabndg_list -%}
    ADD UPDIAMAAABNDG:
    {#- --- 必选参数 --- -#}
    GROUPNAME="{{item.GROUPNAME}}",
    SERVERTYPE={{item.SERVERTYPE}},
    HOSTNAME="{{item.HOSTNAME}}",
    PRIORSEC={{item.PRIORSEC}},
    ;
{%- endfor -%}
```

#### 4.7 绑定Non-SIM AAA服务器组到APN。

```jinja2
{%- for item in add_upapndiamaaag_list -%}
    ADD UPAPNDIAMAAAG:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    GROUPNAME="{{item.GROUPNAME}}",
    ;
{%- endfor -%}
```


---
id: ''
name: 配置到3GPP AAA Server的数据
ne_type: UNC
type: feature
description: 当UNC支持Non-3GPP GW接入或部署CDMA2000与LTE、WLAN与LTE互操作网络时，需要配置UNC到3GPP AAA Server的互通数据，用于更新PGW-C的IP地址和APN信息，并获取用户的授权信息。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","基本接入功能","WSFD-010102 Untrusted Non-3GPP网络用户接入","激活Untrusted Non-3GPP网络用户接入功能","配置到3GPP AAA Server的数据"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
当UNC支持Non-3GPP GW接入或部署CDMA2000与LTE、WLAN与LTE互操作网络时，需要配置UNC到3GPP AAA Server的互通数据，用于更新PGW-C的IP地址和APN信息，并获取用户的授权信息。

## 必备事项
前提条件

* 请仔细阅读WSFD-010102 Untrusted Non-3GPP网络用户接入和激活Untrusted Non-3GPP网络用户接入功能。
* UNC与网络实体之间的网络环境已经构建完成。
* 操作员了解UNC各类接口的类型及命名规范，具体内容请参见业务组网与逻辑接口介绍。
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
          minLength: 1
          maxLength: 31
          required: true
          description: '**ADD VPNINST**'
          data_source: '本端规划'
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
          description: '****ADD L3VPNINST****  ****ADD VPNINSTAF****'
          data_source: '本端规划'
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
          description: '****ADD L3VPNINST****  ****ADD VPNINSTAF****'
          data_source: '本端规划'
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
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_concenpoint_list:
      type: items
      properties:
        S6BCONCENMODE:
          name: 'S6b集中点模式'
          type: string
          enum:
          - LOCALIP_PEER
          - LOCALPORT
          required: false
          description: '**SET CONCENPOINT**'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_logicinf_list:
      type: items
      properties:
        NAME:
          name: '逻辑接口名称'
          type: string
          maxLength: 63
          required: true
          description: '**ADD LOGICINF**'
          data_source: '固定取值'
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
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPV4ADDRESS1:
          name: '逻辑接口的IPv4地址1'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV4MASK1:
          name: '逻辑接口的IPv4掩码1'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
        VPNINSTANCE:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: '从已配置数据中获取'
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
        IPV6PREFIXLEN1:
          name: 'IPv6前缀长度1'
          type: integer
          minimum: 128
          maximum: 128
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6PREFIXLEN2:
          name: 'IPv6前缀长度2'
          type: integer
          minimum: 128
          maximum: 128
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_srroute_list:
      type: items
      properties:
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: false
          description: '**ADD SRROUTE**'
          data_source: '本端规划'
          pattern: ''
          default: '_public_'
        AFTYPE:
          name: '地址族'
          type: string
          enum:
          - ipv4unicast
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PREFIX:
          name: '路由前缀'
          type: string
          maxLength: 15
          required: true
          description: ''
          data_source: '与对端网元协商'
          pattern: ''
          default: ''
        MASKLENGTH:
          name: '路由掩码长度'
          type: integer
          minimum: 0
          maximum: 32
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        DESTVRFNAME:
          name: '下一跳VPN名字'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IFNAME:
          name: '路由出接口名字'
          type: string
          maxLength: 63
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NEXTHOP:
          name: '路由下一跳'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '与对端网元协商'
          pattern: ''
          default: ''
    add_sctpendpoint_list:
      type: items
      properties:
        ENDPOINTNAME:
          name: '端点名称'
          type: string
          maxLength: 63
          required: true
          description: '**ADD SCTPENDPOINT**'
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPVERSION:
          name: 'IP版'
          type: string
          enum:
          - IPV4
          - IPV6
          required: true
          description: ''
          data_source: '与对端协商'
          pattern: ''
          default: ''
        IPV4ADDRESS1:
          name: 'IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '与对端协商'
          pattern: ''
          default: ''
        PORT:
          name: '端口号'
          type: integer
          minimum: 1
          maximum: 65534
          required: false
          description: ''
          data_source: '与对端协商'
          pattern: ''
          default: 3868
        IPV4ADDRESS2:
          name: 'IPv4地址2'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6ADDRESS1:
          name: 'IPv6地址1'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6ADDRESS2:
          name: 'IPv6地址2'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_diamlocinfo_list:
      type: items
      properties:
        HOSTNAME:
          name: '本端主机名'
          type: string
          maxLength: 127
          required: true
          description: '与3GPP AAA Server上配置的参数保持一致。  **ADD DIAMLOCINFO**'
          data_source: '与对端协商'
          pattern: ''
          default: ''
        REALMNAME:
          name: '本端域名'
          type: string
          maxLength: 127
          required: true
          description: ''
          data_source: '与对端协商'
          pattern: ''
          default: ''
        PRODUCTNAME:
          name: '产品名称'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_diameteraaa_list:
      type: items
      properties:
        HOSTNAME:
          name: '主机名'
          type: string
          minLength: 0
          maxLength: 127
          required: true
          description: 'VPN实例已通过**ADD VPNINST**命令配置，可以使用**LST VPNINST**命令进行查询。  **ADD DIAMETERAAA**'
          data_source: '本端规划'
          pattern: ''
          default: ''
        REALMNAME:
          name: '域名'
          type: string
          minLength: 1
          maxLength: 127
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        VPNINSTANCE:
          name: 'VPN实例'
          type: string
          minLength: 1
          maxLength: 31
          required: false
          description: ''
          data_source: '从已配置数据中获取'
          pattern: ''
          default: ''
    add_diampeeraddr_list:
      type: items
      properties:
        HOSTNAME:
          name: '主机名'
          type: string
          maxLength: 127
          required: true
          description: 'UNC与3gppaaa之间构建一条IP链路，3gppaaa的IP地址为10.10.10.10。**ADD DIAMPEERADDR**'
          data_source: '本端规划'
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
          data_source: '与对端协商'
          pattern: ''
          default: ''
        SCTPENDPOINT:
          name: 'SCTP端点名称'
          type: string
          maxLength: 63
          required: false
          description: '已通过**ADD SCTPENDPOINT**完成配置。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPV4ADDRESS:
          name: 'IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
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
    add_diamconngrp_list:
      type: items
      properties:
        CONNGROUPNAME:
          name: 'Diameter链路组名'
          type: string
          maxLength: 31
          required: true
          description: '**ADD DIAMCONNGRP**'
          data_source: '本端规划'
          pattern: ''
          default: ''
        LOCALHOSTNAME:
          name: '本端主机名'
          type: string
          maxLength: 127
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        PEERHOSTNAME:
          name: '对端主机名'
          type: string
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
          - GX
          - GY
          - S6b
          required: true
          description: ''
          data_source: '全网规划'
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
          data_source: '全网规划'
          pattern: ''
          default: SESSION_ID
    add_diamconnection_list:
      type: items
      properties:
        DIAMCONNGRP:
          name: 'Diameter链路组名'
          type: string
          maxLength: 31
          required: true
          description: '**ADD DIAMCONNECTION**'
          data_source: '本端规划'
          pattern: ''
          default: ''
        LOCINTERFACE:
          name: '本端接口名'
          type: string
          maxLength: 31
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        LOCALPORT:
          name: '本端端口'
          type: integer
          minimum:
          - 0
          - 13200
          - 16400
          - 19765
          maximum:
          - 0
          - 13263
          - 16463
          - 19784
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: 0
        PEERADDRTYPE:
          name: '对端地址类型'
          type: string
          enum:
          - IPv4
          - IPv6
          - SCTP
          required: false
          description: ''
          data_source: '与对端协商'
          pattern: ''
          default: ''
        PEERSCTPENDPT:
          name: '对端SCTP端点名称'
          type: string
          maxLength: 63
          required: false
          description: '已通过**ADD SCTPENDPOINT**完成配置。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PEERIPV4ADDR:
          name: '对端IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PEERIPV6ADDR:
          name: '对端IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PEERPORT:
          name: '对端端口号'
          type: integer
          minimum: 1
          maximum: 65534
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
    add_diamaaagrp_list:
      type: items
      properties:
        GROUPNAME:
          name: 'Diameter AAA组名'
          type: string
          minLength: 1
          maxLength: 31
          required: true
          description: '配置PGW-C identity的属性。  **ADD DIAMAAAGRP**  **ADD PGWHOSTNAME**  **ADD DIAMAAABNDGRP**  **ADD APNDIAMAAAGRP**'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PGWIDENTITY:
          name: 'PDN GW Identity携带方式'
          type: string
          enum:
          - HOST_NAME
          - IP
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: HOST_NAME
    add_pgwhostname_list:
      type: items
      properties:
        PGWHOSTNAME:
          name: 'PGW-C主机名'
          type: string
          minLength: 0
          maxLength: 255
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        INTFTYPE:
          name: '接口类型'
          type: string
          enum:
          - S5_P_OR_GN_OR_S2B
          - S8_P_OR_GP_OR_S2B
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_diamaaabndgrp_list:
      type: items
      properties:
        GROUPNAME:
          name: 'Diameter AAA组名'
          type: string
          minLength: 1
          maxLength: 31
          required: true
          description: '配置PGW-C identity的属性。  **ADD DIAMAAAGRP**  **ADD PGWHOSTNAME**  **ADD DIAMAAABNDGRP**  **ADD APNDIAMAAAGRP**'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SERVERTYPE:
          name: '服务器类型'
          type: string
          enum:
          - PARA_3GPP
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        HOSTNAME:
          name: '主机名'
          type: string
          minLength: 1
          maxLength: 127
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PRIORSEC:
          name: '主备用标记'
          type: string
          enum:
          - PRIMARY
          - SECONDARY
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_apndiamaaagrp_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        GROUPNAME:
          name: 'Diameter AAA组名'
          type: string
          minLength: 1
          maxLength: 31
          required: true
          description: '配置PGW-C identity的属性。  **ADD DIAMAAAGRP**  **ADD PGWHOSTNAME**  **ADD DIAMAAABNDGRP**  **ADD APNDIAMAAAGRP**'
          data_source: '本端规划'
          pattern: ''
          default: ''
  examples:
    add_vpninst_list:
    - VPNINSTANCE: 'vpn_3gpp_aaa'
    add_l3vpninst_list:
    - VRFNAME: 'vpn_3gpp_aaa'
    add_vpninstaf_list:
    - VRFNAME: 'vpn_3gpp_aaa'
      AFTYPE: ipv4uni
    set_concenpoint_list:
    - S6BCONCENMODE: LOCALPORT
    add_logicinf_list:
    - NAME: 's6bif1/0/0'
      IPVERSION: IPV4
      IPV4ADDRESS1: '192.168.7.7'
      IPV4MASK1: '255.255.255.255'
      VPNINSTANCE: 'vpn_3gpp_aaa'
      IPV4ADDRESS2: ''
      IPV4MASK2: ''
      IPV6ADDRESS1: ''
      IPV6ADDRESS2: ''
      IPV6PREFIXLEN1: ''
      IPV6PREFIXLEN2: ''
    add_srroute_list:
    - VRFNAME: 'vpn_3gpp_aaa'
      AFTYPE: ipv4unicast
      PREFIX: '0.0.0.0'
      MASKLENGTH: 32
      DESTVRFNAME: 'vpn_3gpp_aaa'
      IFNAME: 'Invalid0'
      NEXTHOP: '10.3.37.81'
    add_sctpendpoint_list:
    - ENDPOINTNAME: 'dc1_AAA01-S6B-SCTPEP01'
      IPVERSION: IPV4
      IPV4ADDRESS1: '10.45.36.227'
      PORT: 3868
      IPV4ADDRESS2: ''
      IPV6ADDRESS1: ''
      IPV6ADDRESS2: ''
    add_diamlocinfo_list:
    - HOSTNAME: 'unc_1'
      REALMNAME: 'apn2'
      PRODUCTNAME: 'unc'
    add_diameteraaa_list:
    - HOSTNAME: '3gppaaa'
      REALMNAME: '3gppaaa.huawei.com'
      VPNINSTANCE: 'vpn_3gpp_aaa'
    add_diampeeraddr_list:
    - HOSTNAME: '3gppaaa'
      ADDRTYPE: SCTP
      SCTPENDPOINT: 'dc1_AAA01-S6B-SCTPEP01'
      IPV4ADDRESS: ''
      IPV6ADDRESS: ''
      PORT: 3868
    add_diamconngrp_list:
    - CONNGROUPNAME: 'dconn_s6b'
      LOCALHOSTNAME: 'unc_1'
      PEERHOSTNAME: '3gppaaa'
      APPLICATION: S6b
      SELECTMODE: SESSION_ID ROUND-ROBIN
    add_diamconnection_list:
    - DIAMCONNGRP: 'dconn_s6b'
      LOCINTERFACE: 'S6bif1/0/0'
      LOCALPORT: 19765
      PEERADDRTYPE: SCTP
      PEERSCTPENDPT: 'dc1_AAA01-S6B-SCTPEP01'
      PEERIPV4ADDR: ''
      PEERIPV6ADDR: ''
      PEERPORT: ''
      REVERSEIP: DISABLE
    add_diamaaagrp_list:
    - GROUPNAME: '3gpprg'
      PGWIDENTITY: HOST_NAME
    add_pgwhostname_list:
    - PGWHOSTNAME: 'topon.Eth-0.canonical-node-name.gw32.california.west.example.com'
      INTFTYPE: S5_P_OR_GN_OR_S2B
    add_diamaaabndgrp_list:
    - GROUPNAME: '3gpprg'
      SERVERTYPE: PARA_3GPP
      HOSTNAME: '3gppaaa'
      PRIORSEC: PRIMARY
    add_apndiamaaagrp_list:
    - APN: 'apn1'
      GROUPNAME: '3gpprg'
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 进入“MML命令行-UNC”窗口。

### 2 配置VPN实例。

```jinja2
{%- for item in add_vpninst_list -%}
    ADD VPNINST:
    {#- --- 必选参数 --- -#}
    VPNINSTANCE="{{item.VPNINSTANCE}}",
    ;
{%- endfor -%}
```

### 3 配置L3VPN实例。

```jinja2
{%- for item in add_l3vpninst_list -%}
    ADD L3VPNINST:
    {#- --- 必选参数 --- -#}
    VRFNAME="{{item.VRFNAME}}",
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_vpninstaf_list -%}
    ADD VPNINSTAF:
    {#- --- 必选参数 --- -#}
    VRFNAME="{{item.VRFNAME}}",
    AFTYPE={{item.AFTYPE}},
    ;
{%- endfor -%}
```

### 4 **可选：**配置S6b接口Diameter应用集中点模式。缺省情况下，本端的端口号不可配，使用系统自动分配的端口号。

```jinja2
{%- if is_optional_s6b_diameter_concentration_point_mode -%}
    {%- for item in set_concenpoint_list -%}
        SET CONCENPOINT:
        {#- --- 可选参数 --- -#}
        {%- if item.S6BCONCENMODE is not none -%}
            S6BCONCENMODE={{item.S6BCONCENMODE}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 5 创建S6bif接口。

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
    {#- --- 条件必选：IPVERSION=IPV6/IPVER_ALL 时必选 --- -#}
    {%- if item.IPVERSION in ['IPV6', 'IPVER_ALL'] -%}
        IPV6ADDRESS1="{{item.IPV6ADDRESS1}}",
    {%- endif -%}
    {#- --- 条件必选：IPVERSION=IPV6/IPVER_ALL 时必选 --- -#}
    {%- if item.IPVERSION in ['IPV6', 'IPVER_ALL'] -%}
        IPV6PREFIXLEN1={{item.IPV6PREFIXLEN1}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：IPVERSION=IPV4/IPV6/IPVER_ALL 时可选 --- -#}
    {%- if item.IPVERSION in ['IPV4', 'IPV6', 'IPVER_ALL'] -%}
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
    {#- --- 条件可选：IPVERSION=IPV6/IPVER_ALL 时可选 --- -#}
    {%- if item.IPVERSION in ['IPV6', 'IPVER_ALL'] -%}
        {%- if item.IPV6ADDRESS2 is not none -%}
            IPV6ADDRESS2="{{item.IPV6ADDRESS2}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：IPVERSION=IPV6/IPVER_ALL 时可选 --- -#}
    {%- if item.IPVERSION in ['IPV6', 'IPVER_ALL'] -%}
        {%- if item.IPV6PREFIXLEN2 is not none -%}
            IPV6PREFIXLEN2={{item.IPV6PREFIXLEN2}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 6 配置到3GPP AAA Server的VPN缺省路由。

```jinja2
{%- for item in add_srroute_list -%}
    ADD SRROUTE:
    {#- --- 必选参数 --- -#}
    AFTYPE={{item.AFTYPE}},
    PREFIX="{{item.PREFIX}}",
    MASKLENGTH={{item.MASKLENGTH}},
    {#- --- 可选参数 --- -#}
    {%- if item.VRFNAME is not none -%}
        VRFNAME="{{item.VRFNAME}}",
    {%- endif -%}
    {%- if item.DESTVRFNAME is not none -%}
        DESTVRFNAME="{{item.DESTVRFNAME}}",
    {%- endif -%}
    {%- if item.IFNAME is not none -%}
        IFNAME="{{item.IFNAME}}",
    {%- endif -%}
    {%- if item.NEXTHOP is not none -%}
        NEXTHOP="{{item.NEXTHOP}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 7 如果通过SCTP方式与3GPP AAA Server建立链接，需要配置SCTP端点信息。

```jinja2
{%- if is_scenario_sctp -%}
    {%- for item in add_sctpendpoint_list -%}
        ADD SCTPENDPOINT:
        {#- --- 必选参数 --- -#}
        ENDPOINTNAME="{{item.ENDPOINTNAME}}",
        IPVERSION={{item.IPVERSION}},
        {#- --- 可选参数 --- -#}
        {%- if item.PORT is not none -%}
            PORT={{item.PORT}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：IPVERSION=IPV4 时必选 --- -#}
        {%- if item.IPVERSION == 'IPV4' -%}
            IPV4ADDRESS1="{{item.IPV4ADDRESS1}}",
        {%- endif -%}
        {#- --- 条件必选：IPVERSION=IPV6 时必选 --- -#}
        {%- if item.IPVERSION == 'IPV6' -%}
            IPV6ADDRESS1="{{item.IPV6ADDRESS1}}",
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：IPVERSION=IPV4 时可选 --- -#}
        {%- if item.IPVERSION == 'IPV4' -%}
            {%- if item.IPV4ADDRESS2 is not none -%}
                IPV4ADDRESS2="{{item.IPV4ADDRESS2}}",
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：IPVERSION=IPV6 时可选 --- -#}
        {%- if item.IPVERSION == 'IPV6' -%}
            {%- if item.IPV6ADDRESS2 is not none -%}
                IPV6ADDRESS2="{{item.IPV6ADDRESS2}}",
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 8 配置本端端点的主机信息。

```jinja2
{%- for item in add_diamlocinfo_list -%}
    ADD DIAMLOCINFO:
    {#- --- 必选参数 --- -#}
    HOSTNAME="{{item.HOSTNAME}}",
    REALMNAME="{{item.REALMNAME}}",
    PRODUCTNAME="{{item.PRODUCTNAME}}",
    ;
{%- endfor -%}
```

### 9 配置3GPP AAA Server。

```jinja2
{%- for item in add_diameteraaa_list -%}
    ADD DIAMETERAAA:
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
{%- for item in add_diampeeraddr_list -%}
    ADD DIAMPEERADDR:
    {#- --- 必选参数 --- -#}
    HOSTNAME="{{item.HOSTNAME}}",
    ADDRTYPE={{item.ADDRTYPE}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：ADDRTYPE=SCTP 时必选 --- -#}
    {%- if item.ADDRTYPE == 'SCTP' -%}
        SCTPENDPOINT="{{item.SCTPENDPOINT}}",
    {%- endif -%}
    {#- --- 条件必选：ADDRTYPE=IPv4 时必选 --- -#}
    {%- if item.ADDRTYPE == 'IPv4' -%}
        IPV4ADDRESS="{{item.IPV4ADDRESS}}",
    {%- endif -%}
    {#- --- 条件必选：ADDRTYPE=IPv6 时必选 --- -#}
    {%- if item.ADDRTYPE == 'IPv6' -%}
        IPV6ADDRESS="{{item.IPV6ADDRESS}}",
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

### 通过TCP方式与3GPP AAA Server建立起正常的IP连接时，**ADD DIAMPEERADDR**中的“ADDRTYPE”根据实际规划配置为“IPv4”或“IPv6”。

### 通过SCTP方式与3GPP AAA Server建立起正常的IP连接时，**ADD DIAMPEERADDR**中的“ADDRTYPE”配置为“SCTP”，“SCTPENDPOINT”已通过**ADD SCTPENDPOINT**完成配置。

### 10 建立本端与对端的链路组，并配置链路选择模式。

```jinja2
{%- for item in add_diamconngrp_list -%}
    ADD DIAMCONNGRP:
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

### 11 配置到3GPP AAA Server的链路。

```jinja2
{%- for item in add_diamconnection_list -%}
    ADD DIAMCONNECTION:
    {#- --- 必选参数 --- -#}
    DIAMCONNGRP="{{item.DIAMCONNGRP}}",
    LOCINTERFACE="{{item.LOCINTERFACE}}",
    {#- --- 可选参数 --- -#}
    {%- if item.LOCALPORT is not none -%}
        LOCALPORT={{item.LOCALPORT}},
    {%- endif -%}
    {%- if item.PEERADDRTYPE is not none -%}
        PEERADDRTYPE={{item.PEERADDRTYPE}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：PEERADDRTYPE=SCTP 时必选 --- -#}
    {%- if item.PEERADDRTYPE == 'SCTP' -%}
        PEERSCTPENDPT="{{item.PEERSCTPENDPT}}",
    {%- endif -%}
    {#- --- 条件必选：PEERADDRTYPE=IPv4 时必选 --- -#}
    {%- if item.PEERADDRTYPE == 'IPv4' -%}
        PEERIPV4ADDR="{{item.PEERIPV4ADDR}}",
    {%- endif -%}
    {#- --- 条件必选：PEERADDRTYPE=IPv6 时必选 --- -#}
    {%- if item.PEERADDRTYPE == 'IPv6' -%}
        PEERIPV6ADDR="{{item.PEERIPV6ADDR}}",
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

### 通过TCP方式与3GPP AAA Server建立起正常的IP连接时，**ADD DIAMCONNECTION**中的“PEERADDRTYPE”根据实际规划配置为“PEERIPV4ADDR”或“PEERIPV6ADDR”。

### 通过SCTP方式与3GPP AAA Server建立起正常的IP连接时，**ADD DIAMCONNECTION**中的“PEERADDRTYPE”配置为“SCTP”，“PEERSCTPENDPT”已通过**ADD SCTPENDPOINT**完成配置。

### 配置链路时如果不选择地址类型，则表示本端接口与对端主机的全部地址建立链接。

### 当“S6b集中点模式”通过**SET CONCENPOINT**命令选择为“LOCALPORT”时，可使用**ADD DIAMCONNECTION**命令设置本端的端口号。

### 12 配置PGW-C identity的属性。

```jinja2
{%- for item in add_diamaaagrp_list -%}
    ADD DIAMAAAGRP:
    {#- --- 必选参数 --- -#}
    GROUPNAME="{{item.GROUPNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.PGWIDENTITY is not none -%}
        PGWIDENTITY={{item.PGWIDENTITY}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 13 增加逻辑接口的PGW-C主机名。

```jinja2
{%- for item in add_pgwhostname_list -%}
    ADD PGWHOSTNAME:
    {#- --- 必选参数 --- -#}
    PGWHOSTNAME="{{item.PGWHOSTNAME}}",
    INTFTYPE={{item.INTFTYPE}},
    ;
{%- endfor -%}
```

### 14 绑定3GPP AAA Server到服务器组。

```jinja2
{%- for item in add_diamaaabndgrp_list -%}
    ADD DIAMAAABNDGRP:
    {#- --- 必选参数 --- -#}
    GROUPNAME="{{item.GROUPNAME}}",
    SERVERTYPE={{item.SERVERTYPE}},
    HOSTNAME="{{item.HOSTNAME}}",
    PRIORSEC={{item.PRIORSEC}},
    ;
{%- endfor -%}
```

### 15 绑定diameter-server group到APN。

```jinja2
{%- for item in add_apndiamaaagrp_list -%}
    ADD APNDIAMAAAGRP:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    GROUPNAME="{{item.GROUPNAME}}",
    ;
{%- endfor -%}
```


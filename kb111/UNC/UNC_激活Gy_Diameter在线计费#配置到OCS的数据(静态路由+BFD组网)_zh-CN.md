---
id: ''
name: 配置到OCS的数据(静态路由+BFD组网)
ne_type: UNC
type: feature
description: 当部署在线计费实现对用户的实时计费时，需要配置到OCS的互通。  适用于GGSN、PGW-C。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","计费管理功能","WSFD-109001 Gy/Diameter在线计费","激活Gy/Diameter在线计费","配置到OCS的数据(静态路由+BFD组网)"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
当部署在线计费实现对用户的实时计费时，需要配置到OCS的互通。适用于GGSN、PGW-C。

## 必备事项
前提条件

* 请仔细阅读Ga/Gy接口离线/在线计费。
* 操作员了解UNC各类接口的类型及命名规范，具体内容请参见**《UNC产品手册》：UNC初始配置与调测->了解组网架构->逻辑接口介绍**。
* 操作员了解UNC与对端网元互通时可以采用的各种组网方式，以及每种组网方式的实现及特点等信息。
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
          description: '创建VPN实例。'
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
          description: '创建L3VPN实例。'
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
          description: 'VPN实例。'
          data_source: '已配置数据中获取'
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
    mod_vpninstaf_list:
      type: items
      properties:
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: true
          description: '修改设备上VPN实例下配置的地址族参数。  RD（Route Distinguisher）用来唯一标识一个VPN。'
          data_source: '已配置数据中获取'
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
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        VRFRD:
          name: '路由标识'
          type: string
          maxLength: 21
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    set_concenpoint_list:
      type: items
      properties:
        GYCONCENMODE:
          name: 'Gy集中点模式'
          type: string
          enum:
          - LOCALIP_PEER
          - LOCALPORT
          required: false
          description: 'Diameter应用集中点模式。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_logicip_list:
      type: items
      properties:
        IPVERSION:
          name: 'IP地址类型'
          type: string
          enum:
          - IPv4
          - IPv6
          required: true
          description: '用户增加逻辑IP。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        LOGICIPV4:
          name: 'IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        VPNINSTNAME:
          name: 'VPN实例名称'
          type: string
          minLength: 1
          maxLength: 31
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        IPV4MTU:
          name: 'IPv4 MTU'
          type: integer
          minimum: 328
          maximum: 9600
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 1500
        IPV6MTU:
          name: 'IPv6 MTU值'
          type: integer
          minimum: 1280
          maximum: 9600
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 1500
        LOGICIPV6:
          name: 'IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
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
          description: '组级Gy逻辑接口1。'
          data_source: '本端规划'
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
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        IPV4ADDRESS1:
          name: '逻辑接口的IPv4地址1'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '已配置数据中获取'
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
          name: 'VPN实例名'
          type: string
          maxLength: 31
          required: false
          description: '已在该配置任务中通过命令**ADD VPNINST**配置，可以使用**LST VPNINST**命令进行查询。'
          data_source: '已配置数据中获取'
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
    add_diamlocinfo_list:
      type: items
      properties:
        HOSTNAME:
          name: '本端主机名'
          type: string
          maxLength: 127
          required: true
          description: 'GGSN/PGW-C的本端信息。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        REALMNAME:
          name: '本端域名'
          type: string
          maxLength: 127
          required: true
          description: ''
          data_source: '全网规划'
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
    add_ocs_list:
      type: items
      properties:
        OCSHOSTNAME:
          name: 'Ocs主机名称'
          type: string
          maxLength: 127
          required: true
          description: 'OCS的设备信息。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        REALMNAME:
          name: 'Ocs域名'
          type: string
          maxLength: 127
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        VPNINSTANCE:
          name: 'VPN实例'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_diamconngrp_list:
      type: items
      properties:
        CONNGROUPNAME:
          name: 'Diameter链路组名'
          type: string
          maxLength: 31
          required: true
          description: '该命令用于指定GGSN/PGW-C与指定OCS之间建立一组Diameter链路。'
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
        APPLICATION:
          name: 'Diameter应用'
          type: string
          enum:
          - GX
          - GY
          - S6b
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        PEERHOSTNAME:
          name: '对端主机名'
          type: string
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
          data_source: '全网规划'
          pattern: ''
          default: SESSION_ID
    add_diampeeraddr_list:
      type: items
      properties:
        HOSTNAME:
          name: '主机名称'
          type: string
          maxLength: 127
          required: true
          description: '增加Diameter链路对端的地址信息，配置Diameter链路对端的地址类型、IP、端口号或端点信息。'
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
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPV4ADDRESS:
          name: 'IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        PORT:
          name: '端口号'
          type: integer
          minimum: 1
          maximum: 65534
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: 3868
        IPV6ADDRESS:
          name: 'IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SCTPENDPOINT:
          name: 'SCTP端点名称'
          type: string
          maxLength: 63
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_diamconnection_list:
      type: items
      properties:
        DIAMCONNGRP:
          name: 'Diameter链路组名'
          type: string
          maxLength: 31
          required: true
          description: '增加Diameter链路。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        LOCINTERFACE:
          name: '本端接口名'
          type: string
          maxLength: 31
          required: true
          description: ''
          data_source: '已配置数据中获取'
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
          data_source: ''
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
          data_source: ''
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
    add_ocsgroup_list:
      type: items
      properties:
        OCSGRPNAME:
          name: 'Ocs组名称'
          type: string
          maxLength: 63
          required: true
          description: '配置主OCS组。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_ocsbinding_list:
      type: items
      properties:
        OCSGRPNAME:
          name: 'Ocs组名称'
          type: string
          maxLength: 63
          required: true
          description: '增加OCS绑定关系。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        OCSHOSTNAME:
          name: 'Ocs主机名称'
          type: string
          maxLength: 127
          required: true
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    mod_dcctemplate_list:
      type: items
      properties:
        DCCTMPLTNAME:
          name: 'DCC模板名称'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_dcctemplate_list:
      type: items
      properties:
        DCCTMPLTNAME:
          name: 'DCC模板名称'
          type: string
          maxLength: 63
          required: true
          description: '配置主从OCS组。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        PRIOCSGRPNAME:
          name: '主OCS组名称'
          type: string
          maxLength: 63
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        SECOCSGRPNAME:
          name: '备OCS组名称'
          type: string
          maxLength: 63
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_ceaorighostchk_list:
      type: items
      properties:
        CEAORIGHOSTCHK:
          name: '检查Gy的CEA消息中的Origin-Host'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: 'Diameter应用控制。'
          data_source: '本端规划'
          pattern: ''
          default: ''
  examples:
    add_vpninst_list:
    - VPNINSTANCE: 'vpn_gy'
    add_l3vpninst_list:
    - VRFNAME: 'vpn_gy'
    add_vpninstaf_list:
    - VRFNAME: 'vpn_gy'
      AFTYPE: ipv4uni
    mod_vpninstaf_list:
    - VRFNAME: 'vpn_gy'
      AFTYPE: ipv4uni
      VRFRD: '2050:1'
    set_concenpoint_list:
    - GYCONCENMODE: LOCALPORT
    add_logicip_list:
    - IPVERSION: IPv4
      LOGICIPV4: '10.8.20.1'
      VPNINSTNAME: 'vpn_gy'
      IPV4MTU: 1500
      IPV6MTU: 1500
      LOGICIPV6: ''
    add_logicinf_list:
    - NAME: 'Gyif1/0/0'
      IPVERSION: IPV4
      IPV4ADDRESS1: '10.8.20.1'
      IPV4MASK1: '255.255.255.255'
      VPNINSTANCE: 'vpn_gy'
      IPV4ADDRESS2: ''
      IPV4MASK2: ''
      IPV6ADDRESS1: ''
      IPV6ADDRESS2: ''
      IPV6PREFIXLEN1: ''
      IPV6PREFIXLEN2: ''
    add_diamlocinfo_list:
    - HOSTNAME: 'pgw1'
      REALMNAME: 'huawei.com'
      PRODUCTNAME: 'unc@huawei.com'
    add_ocs_list:
    - OCSHOSTNAME: 'ocs1'
      REALMNAME: 'huawei.com'
      VPNINSTANCE: 'vpn_gy'
    add_diamconngrp_list:
    - CONNGROUPNAME: 'dia1'
      LOCALHOSTNAME: 'pgw1'
      APPLICATION: GY
      PEERHOSTNAME: 'ocs1'
      SELECTMODE: MASTER_SLAVE
    add_diampeeraddr_list:
    - HOSTNAME: 'ocs1'
      ADDRTYPE: IPv4
      IPV4ADDRESS: '10.11.21.59'
      PORT: 3868
      IPV6ADDRESS: ''
      SCTPENDPOINT: ''
    add_diamconnection_list:
    - DIAMCONNGRP: 'dia1'
      LOCINTERFACE: 'Gyif1/0/0'
      LOCALPORT: 13201
      PEERADDRTYPE: IPv4
      PEERIPV4ADDR: '10.11.21.59'
      PEERPORT: 3868
      PEERIPV6ADDR: ''
      PEERSCTPENDPT: ''
      REVERSEIP: DISABLE
    add_ocsgroup_list:
    - OCSGRPNAME: 'og-test1'
    add_ocsbinding_list:
    - OCSGRPNAME: 'og-test1'
      OCSHOSTNAME: 'ocs1'
    mod_dcctemplate_list:
    - DCCTMPLTNAME: ''
    add_dcctemplate_list:
    - DCCTMPLTNAME: 'dcc-test'
      PRIOCSGRPNAME: 'og-test1'
      SECOCSGRPNAME: 'og-test2'
    set_ceaorighostchk_list:
    - CEAORIGHOSTCHK: ENABLE
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 参考**《UNC产品手册》：UNC初始配置与调测->****组网路由配置->****配置VNF侧IP路由数据（非SDN）->****手动部署****->****配置静态路由+BFD组网（IPv4）**配置对应的组网。

### 2 创建VPN实例。

```jinja2
{%- for item in add_vpninst_list -%}
    ADD VPNINST:
    {#- --- 必选参数 --- -#}
    VPNINSTANCE="{{item.VPNINSTANCE}}",
    ;
{%- endfor -%}
```

### 3 创建L3VPN实例。

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

```jinja2
{%- for item in mod_vpninstaf_list -%}
    MOD VPNINSTAF:
    {#- --- 必选参数 --- -#}
    VRFNAME="{{item.VRFNAME}}",
    AFTYPE={{item.AFTYPE}},
    {#- --- 可选参数 --- -#}
    {%- if item.VRFRD is not none -%}
        VRFRD="{{item.VRFRD}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 **可选：**配置Gy接口Diameter应用集中点模式。缺省情况下，本端的端口号不可配，使用系统自动分配的端口号。

```jinja2
{%- if is_optional_gy_concenpoint_mode -%}
    {%- for item in set_concenpoint_list -%}
        SET CONCENPOINT:
        {#- --- 可选参数 --- -#}
        {%- if item.GYCONCENMODE is not none -%}
            GYCONCENMODE={{item.GYCONCENMODE}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 5 配置Gy逻辑接口。

#### 5.1 配置逻辑IP地址。

```jinja2
{%- for item in add_logicip_list -%}
    ADD LOGICIP:
    {#- --- 必选参数 --- -#}
    IPVERSION={{item.IPVERSION}},
    {#- --- 可选参数 --- -#}
    {%- if item.VPNINSTNAME is not none -%}
        VPNINSTNAME="{{item.VPNINSTNAME}}",
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPVERSION=IPv4 时必选 --- -#}
    {%- if item.IPVERSION == 'IPv4' -%}
        LOGICIPV4="{{item.LOGICIPV4}}",
    {%- endif -%}
    {#- --- 条件必选：IPVERSION=IPv6 时必选 --- -#}
    {%- if item.IPVERSION == 'IPv6' -%}
        LOGICIPV6="{{item.LOGICIPV6}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：IPVERSION=IPv4 时可选 --- -#}
    {%- if item.IPVERSION == 'IPv4' -%}
        {%- if item.IPV4MTU is not none -%}
            IPV4MTU={{item.IPV4MTU}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：IPVERSION=IPv6 时可选 --- -#}
    {%- if item.IPVERSION == 'IPv6' -%}
        {%- if item.IPV6MTU is not none -%}
            IPV6MTU={{item.IPV6MTU}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 5.2 配置Gy逻辑接口。

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

#### **ADD LOGICINF**中的“IP地址+VPN实例名称”和**ADD LOGICIP**命令中的“IP地址+VPN实例名称”必须一致。

### 6 配置在线计费中GGSN/PGW-C的设备标识。

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

### UNC的Gx应用和Gy应用的本端主机名可以相同，但是同时要求“REALMNAME”参数和“PRODUCTNAME”参数也必须相同。

### 7 配置在线计费中的OCS信息。

#### 7.1 配置OCS信息。重复执行本步骤可增加多个OCS信息。

```jinja2
{%- for item in add_ocs_list -%}
    ADD OCS:
    {#- --- 必选参数 --- -#}
    OCSHOSTNAME="{{item.OCSHOSTNAME}}",
    REALMNAME="{{item.REALMNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.VPNINSTANCE is not none -%}
        VPNINSTANCE="{{item.VPNINSTANCE}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

#### OCS Server绑定的VPN实例必须和Gy逻辑接口绑定的VPN实例一致。

#### 7.2 Diameter链路信息。

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

```jinja2
{%- for item in add_diampeeraddr_list -%}
    ADD DIAMPEERADDR:
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

#### 当“Gy集中点模式”通过**SET CONCENPOINT**命令选择为“LOCALPORT”时，可使用**ADD DIAMCONNECTION**命令设置本端的端口号。

#### 7.3 配置在线计费系统的OCS组。

```jinja2
{%- for item in add_ocsgroup_list -%}
    ADD OCSGROUP:
    {#- --- 必选参数 --- -#}
    OCSGRPNAME="{{item.OCSGRPNAME}}",
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_ocsbinding_list -%}
    ADD OCSBINDING:
    {#- --- 必选参数 --- -#}
    OCSGRPNAME="{{item.OCSGRPNAME}}",
    OCSHOSTNAME="{{item.OCSHOSTNAME}}",
    ;
{%- endfor -%}
```

#### 7.4 配置主从OCS组。

#### 全局DCC模板

```jinja2
{%- for item in mod_dcctemplate_list -%}
    MOD DCCTEMPLATE:
    {#- --- 必选参数 --- -#}
    DCCTMPLTNAME="{{item.DCCTMPLTNAME}}",
    ;
{%- endfor -%}
```

#### DCC模板

```jinja2
{%- for item in add_dcctemplate_list -%}
    ADD DCCTEMPLATE:
    {#- --- 必选参数 --- -#}
    DCCTMPLTNAME="{{item.DCCTMPLTNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.PRIOCSGRPNAME is not none -%}
        PRIOCSGRPNAME="{{item.PRIOCSGRPNAME}}",
    {%- endif -%}
    {%- if item.SECOCSGRPNAME is not none -%}
        SECOCSGRPNAME="{{item.SECOCSGRPNAME}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 8 **可选：**配置Diameter应用相关功能，即设置GGSN/PGW-C是否检查OCS返回的CEA消息中携带的Origin-Host AVP。

#### 8.1 配置GGSN/PGW-C检查OCS返回的CEA消息中携带的OriginHost AVP与本地**ADD OCS**配置的host名称是否一致。

```jinja2
{%- if is_optional_diameter_application_related_function -%}
    {%- for item in set_ceaorighostchk_list -%}
        SET CEAORIGHOSTCHK:
        {#- --- 可选参数 --- -#}
        {%- if item.CEAORIGHOSTCHK is not none -%}
            CEAORIGHOSTCHK={{item.CEAORIGHOSTCHK}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```


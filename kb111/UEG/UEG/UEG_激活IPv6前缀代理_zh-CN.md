---
id: GWFD-022906
name: 激活IPv6前缀代理
ne_type: UEG
type: feature
description: 当网络中部署IPv6 Prefix Delegation功能，并通过UEG本地地址池方式或者Radius服务器分配IPv6代理前缀时，需要配置本地/Radius分配IPv6代理前缀。  适用于SGW-C、PGW-C、SMF。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝L","MEC 特性指南（风筝L）","GW-C&SMF特性指南","GWFD-022900 IPV6基本功能","GWFD-022906 IPv6 Prefix Delegation","激活IPv6前缀代理"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
当网络中部署IPv6 Prefix Delegation功能，并通过UEG本地地址池方式或者Radius服务器分配IPv6代理前缀时，需要配置本地/Radius分配IPv6代理前缀。适用于SGW-C、PGW-C、SMF。

## 必备事项
前提条件

请仔细阅读GWFD-022906 IPv6 Prefix Delegation特性概述。
完成激活RADIUS功能。
完成加载License。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    set_licenseswitch_list:
      type: items
      properties:
        LICITEM:
          name: 'License项'
          type: string
          minLength: 0
          maxLength: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SWITCH:
          name: '开关'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_cpvpninst_list:
      type: items
      properties:
        VPNINSTANCE:
          name: 'VPN实例名'
          type: string
          minLength: 1
          maxLength: 31
          required: true
          description: '配置VPN实例。'
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
          description: '配置L3VPN实例。'
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
          description: '已通过****ADD L3VPNINST****命令配置，可以使用****LST L3VPNINST****命令进行查询。'
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
          description: '-'
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
          description: '已通过****ADD L3VPNINST****命令配置，可以使用****LST L3VPNINST****命令进行查询。'
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
          description: '-'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        VRFRD:
          name: '路由标识'
          type: string
          maxLength: 21
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_cpaddrpool_list:
      type: items
      properties:
        POOLNAME:
          name: '地址池名'
          type: string
          minLength: 1
          maxLength: 79
          required: true
          description: '配置地址池。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPVERSION:
          name: 'IP地址类型'
          type: string
          enum:
          - IPv4
          - IPv6
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: IPv4
        POOLTYPE:
          name: '地址池类型'
          type: string
          enum:
          - Local
          - UDM
          - Radius
          - DHCP
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: Local
        CHECKIPVALID:
          name: '检查地址合法性'
          type: string
          enum:
          - Disable
          - Enable
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: Disable
        HASVPN:
          name: '绑定VPN'
          type: string
          enum:
          - Disable
          - Enable
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: Disable
        VPNINSTANCE:
          name: 'VPN实例名'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_cpapn_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_cpapnaddressattr_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '规划使能IPv6 Prefix Delegation功能的APN实例，已通过 **ADD CPAPN**命令配置，可以使用 **LST CPAPN**命令进行查询。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        IPV6ALLOCTYPE:
          name: 'IPV6分配方式'
          type: string
          enum:
          - LOCAL
          - RADIUS
          - DHCP
          required: false
          description: '配置APN下的IPv6地址分配属性。  IPv6 Prefix Delegation功能支持通过本地地址池方式或者Radius服务器分配IPv6代理前缀。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    mod_cpapn_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        HASVPNIPV6:
          name: '绑定IPv6 VPN'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VPNINSTANCEIPV6:
          name: 'IPv6 VPN实例名'
          type: string
          minLength: 1
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV3W9V6PD11'
      SWITCH: ENABLE
    add_cpvpninst_list:
    - VPNINSTANCE: 'vpn1'
    add_l3vpninst_list:
    - VRFNAME: 'vpn1'
    add_vpninstaf_list:
    - VRFNAME: 'vpn1'
      AFTYPE: ipv6uni
    mod_vpninstaf_list:
    - VRFNAME: 'vpn1'
      AFTYPE: ipv6uni
      VRFRD: '65512:2'
    add_cpaddrpool_list:
    - POOLNAME: 'pool01'
      IPVERSION: IPv6
      POOLTYPE: Local
      CHECKIPVALID: Enable
      HASVPN: Enable
      VPNINSTANCE: 'vpn1'
    add_cpapn_list:
    - APN: 'huawei.com'
    set_cpapnaddressattr_list:
    - APN: 'huawei.com'
      IPV6ALLOCTYPE: LOCAL
    mod_cpapn_list:
    - APN: 'huawei.com'
      HASVPNIPV6: ENABLE
      VPNINSTANCEIPV6: 'vpn1'
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 进入“MML命令行-UEG”窗口。

### 2 打开本特性的License开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

### 3 配置IPv6 VPN。

#### 3.1 创建VPN实例。

```jinja2
{%- for item in add_cpvpninst_list -%}
    ADD CPVPNINST:
    {#- --- 必选参数 --- -#}
    VPNINSTANCE="{{item.VPNINSTANCE}}",
    ;
{%- endfor -%}
```

#### 3.2 使能IPv6地址族。

#### ****ADD L3VPNINST****

```jinja2
{%- for item in add_l3vpninst_list -%}
    ADD L3VPNINST:
    {#- --- 必选参数 --- -#}
    VRFNAME="{{item.VRFNAME}}",
    ;
{%- endfor -%}
```

#### ****ADD VPNINSTAF****

```jinja2
{%- for item in add_vpninstaf_list -%}
    ADD VPNINSTAF:
    {#- --- 必选参数 --- -#}
    VRFNAME="{{item.VRFNAME}}",
    AFTYPE={{item.AFTYPE}},
    ;
{%- endfor -%}
```

#### 3.3 配置路由标识符。

#### ****MOD VPNINSTAF****

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

### 4 配置分配IPv6代理前缀。

#### 4.1 配置IPv6地址前缀名和IPv6前缀关联的VPN实例。

```jinja2
{%- for item in add_cpaddrpool_list -%}
    ADD CPADDRPOOL:
    {#- --- 必选参数 --- -#}
    POOLNAME="{{item.POOLNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.POOLTYPE is not none -%}
        POOLTYPE={{item.POOLTYPE}},
    {%- endif -%}
    {%- if item.IPVERSION is not none -%}
        IPVERSION={{item.IPVERSION}},
    {%- endif -%}
    {%- if item.HASVPN is not none -%}
        HASVPN={{item.HASVPN}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：HASVPN=Enable 时必选 --- -#}
    {%- if item.HASVPN == 'Enable' -%}
        VPNINSTANCE="{{item.VPNINSTANCE}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：POOLTYPE=UDM/Radius 时可选 --- -#}
    {%- if item.POOLTYPE in ['UDM', 'Radius'] -%}
        {%- if item.CHECKIPVALID is not none -%}
            CHECKIPVALID={{item.CHECKIPVALID}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 如果APN使能了L2TP功能，则无需开启IPv6 Prefix Delegation功能。

### 在功能开启前，需要在AAA Server上配置好分配给终端设备使用的IP地址段。

### 5 配置APN下的地址分配属性。根据规划配置为本地或Radius分配IPv6代理前缀。

#### 5.1 指定APN名称。

```jinja2
{%- for item in add_cpapn_list -%}
    ADD CPAPN:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    ;
{%- endfor -%}
```

#### 5.2 配置地址分配属性。为本地或Radius分配IPv6代理前缀。

```jinja2
{%- for item in set_cpapnaddressattr_list -%}
    SET CPAPNADDRESSATTR:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    {#- --- 可选参数 --- -#}
    {%- if item.IPV6ALLOCTYPE is not none -%}
        IPV6ALLOCTYPE={{item.IPV6ALLOCTYPE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 5.3 配置APN所属的IPv6 APN。

```jinja2
{%- for item in mod_cpapn_list -%}
    MOD CPAPN:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    {#- --- 可选参数 --- -#}
    {%- if item.HASVPNIPV6 is not none -%}
        HASVPNIPV6={{item.HASVPNIPV6}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：HASVPNIPV6=ENABLE 时必选 --- -#}
    {%- if item.HASVPNIPV6 == 'ENABLE' -%}
        VPNINSTANCEIPV6="{{item.VPNINSTANCEIPV6}}",
    {%- endif -%}
    ;
{%- endfor -%}
```


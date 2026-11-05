---
id: ''
name: 激活IPv6前缀代理
ne_type: UNC
type: feature
description: 当网络中部署IPv6 Prefix Delegation功能，并通过UNC本地地址池方式或者Radius服务器分配IPv6代理前缀时，需要配置本地/Radius分配IPv6代理前缀。  适用于GGSN-C、SGW-C、PGW-C、SMF。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","组网功能","WSFD-104004 IPv6前缀代理","激活IPv6前缀代理"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
当网络中部署IPv6 Prefix Delegation功能，并通过UNC本地地址池方式或者Radius服务器分配IPv6代理前缀时，需要配置本地/Radius分配IPv6代理前缀。适用于GGSN-C、SGW-C、PGW-C、SMF。

## 必备事项
前提条件

* 请仔细阅读WSFD-104004 IPv6前缀代理特性概述。
* 完成激活RADIUS功能。
* 完成加载License。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
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
    add_vpninst_list:
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
    add_addrpool_list:
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
        IMSSW:
          name: 'IMS开关'
          type: string
          enum:
          - Disable
          - Enable
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: Enable
        IPLEASE:
          name: '地址租约使能标志'
          type: string
          enum:
          - Disable
          - Enable
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: Disable
        OVERLAP:
          name: '是否允许地址重叠'
          type: string
          enum:
          - Disable
          - Enable
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: Disable
        RELEASETIME:
          name: '地址租期(秒)'
          type: integer
          minimum: 0
          maximum: 86400
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 10
        SINGLEIPFLAG:
          name: '子池类型'
          type: string
          enum:
          - Enable
          - Disable
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: Disable
    add_apn_list:
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
    set_apnaddressattr_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '规划使能IPv6 Prefix Delegation功能的APN实例，已通过**ADD APN** 命令配置，可以使用**LST APN** 命令进行查询。'
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
    mod_apn_list:
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
    add_vpninst_list:
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
    add_addrpool_list:
    - POOLNAME: 'pool01'
      IPVERSION: IPv6
      POOLTYPE: Local
      HASVPN: Enable
      VPNINSTANCE: 'vpn1'
      CHECKIPVALID: Enable
      IMSSW: Enable
      IPLEASE: Disable
      OVERLAP: Disable
      RELEASETIME: 10
      SINGLEIPFLAG: Disable
    add_apn_list:
    - APN: 'huawei.com'
    set_apnaddressattr_list:
    - APN: 'huawei.com'
      IPV6ALLOCTYPE: LOCAL
    mod_apn_list:
    - APN: 'huawei.com'
      HASVPNIPV6: ENABLE
      VPNINSTANCEIPV6: 'vpn1'
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 进入“MML命令行-UNC”窗口。

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
{%- for item in add_vpninst_list -%}
    ADD VPNINST:
    {#- --- 必选参数 --- -#}
    VPNINSTANCE="{{item.VPNINSTANCE}}",
    ;
{%- endfor -%}
```

#### 3.2 使能IPv6地址族。

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

#### 3.3 配置路由标识符。

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
{%- for item in add_addrpool_list -%}
    ADD ADDRPOOL:
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
    {#- --- 条件可选：POOLTYPE=Local 时可选 --- -#}
    {%- if item.POOLTYPE == 'Local' -%}
        {%- if item.IMSSW is not none -%}
            IMSSW={{item.IMSSW}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：POOLTYPE=Local 时可选 --- -#}
    {%- if item.POOLTYPE == 'Local' -%}
        {%- if item.IPLEASE is not none -%}
            IPLEASE={{item.IPLEASE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：POOLTYPE=Local 时可选 --- -#}
    {%- if item.POOLTYPE == 'Local' -%}
        {%- if item.OVERLAP is not none -%}
            OVERLAP={{item.OVERLAP}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：POOLTYPE=Local 时可选 --- -#}
    {%- if item.POOLTYPE == 'Local' -%}
        {%- if item.RELEASETIME is not none -%}
            RELEASETIME={{item.RELEASETIME}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：POOLTYPE=Local 时可选 --- -#}
    {%- if item.POOLTYPE == 'Local' -%}
        {%- if item.SINGLEIPFLAG is not none -%}
            SINGLEIPFLAG={{item.SINGLEIPFLAG}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 4.2 如果APN使能了L2TP功能，则无需开启IPv6 Prefix Delegation功能。

#### 4.3 在功能开启前，需要在AAA Server上配置好分配给终端设备使用的IP地址段。

### 5 配置APN下的地址分配属性。根据规划配置为本地或Radius分配IPv6代理前缀。

#### 5.1 指定APN名称。

```jinja2
{%- for item in add_apn_list -%}
    ADD APN:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    ;
{%- endfor -%}
```

#### 5.2 配置地址分配属性。为本地或Radius分配IPv6代理前缀。

```jinja2
{%- for item in set_apnaddressattr_list -%}
    SET APNADDRESSATTR:
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
{%- for item in mod_apn_list -%}
    MOD APN:
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


---
id: GWFD-020903
name: 配置PGW-U到Untrusted Non-3GPP GW的数据（OSPFv3动态路由+IPv6 BFD组网）（虚机容器）
ne_type: UEG
type: feature
description: UEG与ePDG互通，用于部署WiFi用户接入EPC网络。  * 逻辑接口：Paif接口。 * 路由：OSPFv3动态路由，各接口对外发布的路由优先级相同，作为等价路由实现物理链路的负荷分担。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝S","MEC 特性指南（风筝S）","UEG特性指南","基本接入功能","GWFD-020903 Untrusted Non-3GPP网络用户接入","激活Untrusted Non-3GPP网络用户接入功能","配置PGW-U到Untrusted Non-3GPP GW的数据（OSPFv3动态路由+IPv6 BFD组网）（虚机容器）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
UEG与ePDG互通，用于部署WiFi用户接入EPC网络。* 逻辑接口：Paif接口。* 路由：OSPFv3动态路由，各接口对外发布的路由优先级相同，作为等价路由实现物理链路的负荷分担。

## 必备事项
前提条件

* UEG与网络实体之间的网络环境已经构建完成。
* 操作员了解UEG各类接口的类型及命名规范。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    add_l3vpninst_list:
      type: items
      properties:
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: true
          description: '配置L3VPN实例。'
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
          description: 'IPv6组网场景下，该参数选择ipv6uni。'
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
    set_bfd_list:
      type: items
      properties:
        BFDENABLE:
          name: 'BFD使能标志'
          type: string
          enum:
          - TRUE
          - FALSE
          required: true
          description: '全局激活BFD。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_ospfv3_list:
      type: items
      properties:
        PROCID:
          name: 'OSPFv3进程号'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: true
          description: '创建OSPFv3进程。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        VRFNAME:
          name: 'VPN的名称'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: '_public_'
        ROUTERID:
          name: '路由器标识'
          type: string
          maxLength: 15
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        BFDALLINTFFLG:
          name: '使能BFD'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: FALSE
        VPNINSCAPSIMFLG:
          name: '去使能VPN路由环路检测'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: FALSE
        VIRTUALSYSFLAG:
          name: 'OSPFv3共网段虚拟系统使能标志'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: TRUE
    mod_ospfv3_list:
      type: items
      properties:
        PROCID:
          name: 'OSPFv3进程号'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_ospfv3area_list:
      type: items
      properties:
        PROCID:
          name: 'OSPFv3进程号'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: true
          description: 'OSPFv3区域。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        AREAID:
          name: 'OSPFv3区域标识'
          type: string
          maxLength: 15
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_ospfv3importroute_list:
      type: items
      properties:
        PROCID:
          name: 'OSPFv3进程号'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: true
          description: 'OSPFv3引入的路由类型。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        TOPOID:
          name: '拓扑标识'
          type: integer
          minimum: 0
          maximum: 0
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: 0
        PROTOCOL:
          name: '协议号'
          type: string
          enum:
          - bgp
          - direct
          - ospfv3
          - static
          - wlr
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        IMPTCOSTCFG:
          name: '引入路由开销值配置'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: FALSE
        IMPTTAGCFG:
          name: '引入路由标签配置'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: FALSE
        IMPTTYPECFG:
          name: '引入路由类型配置'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: FALSE
    add_vpninst_list:
      type: items
      properties:
        VPNINSTANCE:
          name: 'VPN实例名'
          type: string
          minLength: 0
          maxLength: 31
          required: true
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
          description: '逻辑接口。'
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
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPV6ADDRESS1:
          name: '逻辑接口的IPv6地址1'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: '本端规划'
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
        IPV6PREFIXLEN1:
          name: 'IPv6前缀长度1'
          type: integer
          minimum: 1
          maximum: 128
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
  examples:
    add_l3vpninst_list:
    - VRFNAME: 'vpn-paif'
    add_vpninstaf_list:
    - VRFNAME: 'vpn-paif'
      AFTYPE: ipv6uni
    set_bfd_list:
    - BFDENABLE: TRUE
    add_ospfv3_list:
    - PROCID: 6
      VRFNAME: 'vpn-paif'
      ROUTERID: '10.8.20.1'
      BFDALLINTFFLG: TRUE
      VPNINSCAPSIMFLG: TRUE
      VIRTUALSYSFLAG: TRUE
    mod_ospfv3_list:
    - PROCID: ''
    add_ospfv3area_list:
    - PROCID: 6
      AREAID: '0.0.0.1'
    add_ospfv3importroute_list:
    - PROCID: 6
      TOPOID: 0
      PROTOCOL: wlr
      IMPTCOSTCFG: FALSE
      IMPTTAGCFG: FALSE
      IMPTTYPECFG: FALSE
    add_vpninst_list:
    - VPNINSTANCE: 'vpn-paif'
    add_logicinf_list:
    - NAME: 'Paif1/0/0'
      IPVERSION: IPV6
      IPV6ADDRESS1: 'fc00::1'
      VPNINSTANCE: 'vpn-paif'
      IPV6PREFIXLEN1: 128
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 参考初始配置中**配置动态路由OSPFv3+BFD组网（IPv6）**对应的组网配置。

### 2 配置VPN实例。

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

### 3 全局激活BFD。

```jinja2
{%- for item in set_bfd_list -%}
    SET BFD:
    {#- --- 必选参数 --- -#}
    BFDENABLE={{item.BFDENABLE}},
    ;
{%- endfor -%}
```

### 4 配置OSPFv3路由。

#### 4.1 创建OSPFv3进程。

```jinja2
{%- for item in add_ospfv3_list -%}
    ADD OSPFV3:
    {#- --- 必选参数 --- -#}
    PROCID={{item.PROCID}},
    ROUTERID="{{item.ROUTERID}}",
    {#- --- 可选参数 --- -#}
    {%- if item.VRFNAME is not none -%}
        VRFNAME="{{item.VRFNAME}}",
    {%- endif -%}
    {%- if item.BFDALLINTFFLG is not none -%}
        BFDALLINTFFLG={{item.BFDALLINTFFLG}},
    {%- endif -%}
    {%- if item.VPNINSCAPSIMFLG is not none -%}
        VPNINSCAPSIMFLG={{item.VPNINSCAPSIMFLG}},
    {%- endif -%}
    {%- if item.VIRTUALSYSFLAG is not none -%}
        VIRTUALSYSFLAG={{item.VIRTUALSYSFLAG}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 4.2 可选：配置OSPF的路由器标识Router ID。

```jinja2
{%- if is_optional_ospf_router_id -%}
    {%- for item in mod_ospfv3_list -%}
        MOD OSPFV3:
        {#- --- 必选参数 --- -#}
        PROCID={{item.PROCID}},
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 4.3 增加OSPFv3区域。

```jinja2
{%- for item in add_ospfv3area_list -%}
    ADD OSPFV3AREA:
    {#- --- 必选参数 --- -#}
    PROCID={{item.PROCID}},
    AREAID="{{item.AREAID}}",
    ;
{%- endfor -%}
```

#### 4.4 可选：设置OSPFv3引入路由类型。

```jinja2
{%- if is_optional_ospfv3_import_route -%}
    {%- for item in add_ospfv3importroute_list -%}
        ADD OSPFV3IMPORTROUTE:
        {#- --- 必选参数 --- -#}
        PROCID={{item.PROCID}},
        PROTOCOL={{item.PROTOCOL}},
        {#- --- 可选参数 --- -#}
        {%- if item.TOPOID is not none -%}
            TOPOID={{item.TOPOID}},
        {%- endif -%}
        {%- if item.IMPTCOSTCFG is not none -%}
            IMPTCOSTCFG={{item.IMPTCOSTCFG}},
        {%- endif -%}
        {%- if item.IMPTTAGCFG is not none -%}
            IMPTTAGCFG={{item.IMPTTAGCFG}},
        {%- endif -%}
        {%- if item.IMPTTYPECFG is not none -%}
            IMPTTYPECFG={{item.IMPTTYPECFG}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 5 配置VPN实例及逻辑接口。

#### 5.1 配置VPN实例。

```jinja2
{%- for item in add_vpninst_list -%}
    ADD VPNINST:
    {#- --- 必选参数 --- -#}
    VPNINSTANCE="{{item.VPNINSTANCE}}",
    ;
{%- endfor -%}
```

#### 外联口的VPN一定要与逻辑接口的VPN相同，否则从逻辑接口发出去的报文会查路由失败。

#### 5.2 创建Paif接口。

```jinja2
{%- for item in add_logicinf_list -%}
    ADD LOGICINF:
    {#- --- 必选参数 --- -#}
    NAME="{{item.NAME}}",
    IPVERSION={{item.IPVERSION}},
    {#- --- 条件必选参数 --- -#}
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
    ;
{%- endfor -%}
```


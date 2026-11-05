---
id: GWFD-022901
name: 激活IPv6承载上下文
ne_type: UEG
type: feature
description: IPv6用户接入网络时，需要在UEG上配置手机下行路由，确保用户能访问数据业务。  适用于SGW-U、PGW-U、UPF。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝L","MEC 特性指南（风筝L）","GW-U&UPF特性指南","GWFD-022900 IPV6基本功能","GWFD-022901 IPv6承载上下文","激活IPv6承载上下文"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
IPv6用户接入网络时，需要在UEG上配置手机下行路由，确保用户能访问数据业务。适用于SGW-U、PGW-U、UPF。

## 必备事项
前提条件

请仔细阅读GWFD-022901 IPv6承载上下文。
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
          description: '-'
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
          description: '-'
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
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_routepolicy_list:
      type: items
      properties:
        POLICYNAME:
          name: '路由策略名字'
          type: string
          maxLength: 200
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_routepolicynode_list:
      type: items
      properties:
        POLICYNAME:
          name: '路由策略名字'
          type: string
          maxLength: 200
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        NODESEQUENCE:
          name: '路由策略节点号'
          type: integer
          minimum: 0
          maximum: 65535
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        MATCHMODE:
          name: '匹配模式'
          type: string
          enum:
          - deny
          - permit
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_matchroutetype_list:
      type: items
      properties:
        POLICYNAME:
          name: '路由策略名字'
          type: string
          maxLength: 200
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        NODESEQUENCE:
          name: '路由策略节点号'
          type: integer
          minimum: 0
          maximum: 65535
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        ROUTETYPE:
          name: '路由类型'
          type: string
          enum:
          - external1
          - external1or2
          - external2
          - internal
          - nssaExternal1
          - nssaExternal1or2
          - nssaExternal2
          - wlr_bh
          - wlr_gbh
          - wlr_sp
          - wlr_ud
          required: true
          description: ''
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
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        ROUTERID:
          name: '路由器标识'
          type: string
          maxLength: 15
          required: true
          description: '须知：  Router ID必须全网唯一。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        VRFNAME:
          name: 'VPN名称'
          type: string
          maxLength: 31
          required: false
          description: '可以使用**LST VPNINST**命令进行查询。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: '_public_'
    add_ospfv3area_list:
      type: items
      properties:
        PROCID:
          name: 'OSPFv3进程号'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: true
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        AREAID:
          name: 'OSPFv3区域标识'
          type: string
          maxLength: 15
          required: true
          description: ''
          data_source: '本端规划'
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
          description: ''
          data_source: '本端规划'
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
        ROUPOLINAME:
          name: '路由策略名称'
          type: string
          maxLength: 200
          required: false
          description: '可以使用**LST ROUTEPOLICY**命令进行查询。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV3G5V6PB01'
      SWITCH: ENABLE
    add_vpninst_list:
    - VPNINSTANCE: 'VPN_Internet'
    add_l3vpninst_list:
    - VRFNAME: 'VPN_Internet'
    add_vpninstaf_list:
    - VRFNAME: 'VPN_Internet'
      AFTYPE: ipv6uni
    add_routepolicy_list:
    - POLICYNAME: 'policy1'
    add_routepolicynode_list:
    - POLICYNAME: 'policy1'
      NODESEQUENCE: 10
      MATCHMODE: permit
    add_matchroutetype_list:
    - POLICYNAME: 'policy1'
      NODESEQUENCE: 10
      ROUTETYPE: nssaExternal1
    add_ospfv3_list:
    - PROCID: 100
      ROUTERID: '10.10.10.1'
      VRFNAME: 'VPN_Internet'
    add_ospfv3area_list:
    - PROCID: 100
      AREAID: '0.0.0.1'
    add_ospfv3importroute_list:
    - PROCID: 100
      TOPOID: 0
      PROTOCOL: wlr
      ROUPOLINAME: 'policy1'
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 打开本特性的License配置开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

### 2 配置逻辑口的VPN实例。

```jinja2
{%- for item in add_vpninst_list -%}
    ADD VPNINST:
    {#- --- 必选参数 --- -#}
    VPNINSTANCE="{{item.VPNINSTANCE}}",
    ;
{%- endfor -%}
```

### 逻辑接口的VPN一定要与其对应的外联口的VPN相同，否则从逻辑接口发出去的报文会查询路由失败。

### 3 配置外联口的VPN实例。

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

### 4 配置路由策略。

```jinja2
{%- for item in add_routepolicy_list -%}
    ADD ROUTEPOLICY:
    {#- --- 必选参数 --- -#}
    POLICYNAME="{{item.POLICYNAME}}",
    ;
{%- endfor -%}
```

### 5 添加路由策略节点。

```jinja2
{%- for item in add_routepolicynode_list -%}
    ADD ROUTEPOLICYNODE:
    {#- --- 必选参数 --- -#}
    POLICYNAME="{{item.POLICYNAME}}",
    NODESEQUENCE={{item.NODESEQUENCE}},
    MATCHMODE={{item.MATCHMODE}},
    ;
{%- endfor -%}
```

### 6 添加匹配路由类型。

```jinja2
{%- for item in add_matchroutetype_list -%}
    ADD MATCHROUTETYPE:
    {#- --- 必选参数 --- -#}
    POLICYNAME="{{item.POLICYNAME}}",
    NODESEQUENCE={{item.NODESEQUENCE}},
    ROUTETYPE={{item.ROUTETYPE}},
    ;
{%- endfor -%}
```

### 7 启动OSPFv3进程。

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
    ;
{%- endfor -%}
```

### 8 增加OSPFv3区域。

```jinja2
{%- for item in add_ospfv3area_list -%}
    ADD OSPFV3AREA:
    {#- --- 必选参数 --- -#}
    PROCID={{item.PROCID}},
    AREAID="{{item.AREAID}}",
    ;
{%- endfor -%}
```

### 9 引入WLR路由，将路由发布到骨干网上。

```jinja2
{%- for item in add_ospfv3importroute_list -%}
    ADD OSPFV3IMPORTROUTE:
    {#- --- 必选参数 --- -#}
    PROCID={{item.PROCID}},
    PROTOCOL={{item.PROTOCOL}},
    {#- --- 可选参数 --- -#}
    {%- if item.TOPOID is not none -%}
        TOPOID={{item.TOPOID}},
    {%- endif -%}
    {%- if item.ROUPOLINAME is not none -%}
        ROUPOLINAME="{{item.ROUPOLINAME}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 采用路由策略方式发布路由时，不能只选择发布WLR\_SP或者WLR\_UD路由，必须选择WLR方式发布所有路由。


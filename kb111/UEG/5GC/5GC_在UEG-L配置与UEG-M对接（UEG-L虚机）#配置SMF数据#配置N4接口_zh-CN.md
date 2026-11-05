---
id: ''
name: 配置N4接口
ne_type: UEG
type: feature
description: 用于配置总部园区UEG-L SMF网元的N4接口数据。  对于容灾的两个UEG-L而言，此配置没有区别，仅以一个UEG-L做配置举例。
tags: []
risk_level: ''
doc_source: ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（风筝多园区，入驻式）","风筝L+M多园区方案（非跨级容灾）","方案配置","在UEG-L配置与UEG-M对接（UEG-L虚机）","配置SMF数据","配置N4接口"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
用于配置总部园区UEG-L SMF网元的N4接口数据。对于容灾的两个UEG-L而言，此配置没有区别，仅以一个UEG-L做配置举例。

## 必备事项
前提条件

无。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
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
          description: '配置N4接口的逻辑IP地址。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        LOGICIPV4:
          name: 'IPv4地址'
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
          minLength: 1
          maxLength: 31
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        DESC:
          name: '描述'
          type: string
          minLength: 0
          maxLength: 255
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_cpnode_list:
      type: items
      properties:
        CPNODEINDEX:
          name: 'CP节点索引'
          type: integer
          minimum: 0
          maximum: 0
          required: true
          description: '配置控制面SMF的端点信息。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        NODEIDTYPE:
          name: 'CP节点ID类型'
          type: string
          enum:
          - CpIPv4
          - CpIPv6
          - CpFqdn
          required: true
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        NODEIDIPV4VALUE:
          name: 'CP节点IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        CPFUNCTION:
          name: 'CP节点功能'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: '当前产品暂未实现协议定义的负载控制等相关功能，建议配置为0即可。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_cppoint_list:
      type: items
      properties:
        CPPOINTINDEX:
          name: 'CP端点索引'
          type: integer
          minimum: 0
          maximum: 255
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        CPNODEINDEX:
          name: 'CP节点索引'
          type: integer
          minimum: 0
          maximum: 0
          required: true
          description: '一个CP端点归属于一个CP节点，一个CP节点下可以有多个CP端点。该参数用于指定这个CP端点所属的CP节点，只支持CP节点索引固定取值为0。  已通过**ADD CPNODE**配置，可以通过**LST CPNODE**查询。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        IPVERSION:
          name: 'IP类型'
          type: string
          enum:
          - IPv4
          - IPv6
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPV4:
          name: 'IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: 'CP节点中的IPv4地址和**ADD CPNODE**中的IPv4地址需要相同。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        VPNNAME:
          name: 'VPN名称'
          type: string
          minLength: 1
          maxLength: 31
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: '_public_'
  examples:
    add_logicip_list:
    - IPVERSION: IPv4
      LOGICIPV4: '10.26.0.5'
      VPNINSTNAME: 'VRF_PS_N4'
      DESC: 'FOR N4 Interface'
    add_cpnode_list:
    - CPNODEINDEX: 0
      NODEIDTYPE: CpIPv4
      NODEIDIPV4VALUE: '10.26.0.5'
      CPFUNCTION: 0
    add_cppoint_list:
    - CPPOINTINDEX: 0
      CPNODEINDEX: 0
      IPVERSION: IPv4
      IPV4: '10.26.0.5'
      VPNNAME: 'VRF_PS_N4'
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 配置N4接口的IP地址。

```jinja2
{%- for item in add_logicip_list -%}
    ADD LOGICIP:
    {#- --- 必选参数 --- -#}
    IPVERSION={{item.IPVERSION}},
    {#- --- 可选参数 --- -#}
    {%- if item.VPNINSTNAME is not none -%}
        VPNINSTNAME="{{item.VPNINSTNAME}}",
    {%- endif -%}
    {%- if item.DESC is not none -%}
        DESC="{{item.DESC}}",
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPVERSION=IPv4 时必选 --- -#}
    {%- if item.IPVERSION == 'IPv4' -%}
        LOGICIPV4="{{item.LOGICIPV4}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 2 配置控制面节点实例。

```jinja2
{%- for item in add_cpnode_list -%}
    ADD CPNODE:
    {#- --- 必选参数 --- -#}
    CPNODEINDEX={{item.CPNODEINDEX}},
    NODEIDTYPE={{item.NODEIDTYPE}},
    {#- --- 可选参数 --- -#}
    {%- if item.CPFUNCTION is not none -%}
        CPFUNCTION={{item.CPFUNCTION}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：NODEIDTYPE=CpIPv4 时必选 --- -#}
    {%- if item.NODEIDTYPE == 'CpIPv4' -%}
        NODEIDIPV4VALUE="{{item.NODEIDIPV4VALUE}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_cppoint_list -%}
    ADD CPPOINT:
    {#- --- 必选参数 --- -#}
    CPPOINTINDEX={{item.CPPOINTINDEX}},
    CPNODEINDEX={{item.CPNODEINDEX}},
    IPVERSION={{item.IPVERSION}},
    {#- --- 可选参数 --- -#}
    {%- if item.VPNNAME is not none -%}
        VPNNAME="{{item.VPNNAME}}",
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPVERSION=IPv4 时必选 --- -#}
    {%- if item.IPVERSION == 'IPv4' -%}
        IPV4="{{item.IPV4}}",
    {%- endif -%}
    ;
{%- endfor -%}
```


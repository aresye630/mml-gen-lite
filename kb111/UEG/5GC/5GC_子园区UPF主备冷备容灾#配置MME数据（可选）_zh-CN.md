---
id: ''
name: 配置MME数据（可选）
ne_type: UEG
type: feature
description: NB-IoT场景，用于配置MME侧配置S11-U接口。其中S11-U和N4接口共用VPN。  对于容灾的两个UEG-S而言，此配置没有区别，仅以一个UEG-S做配置举例。
tags: []
risk_level: ''
doc_source: ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（风筝多园区，入驻式）","风筝L+S多园区方案（非跨级容灾）","方案配置","在UEG-L配置与UEG-S对接（UEG-L虚机）","子园区UPF主备冷备容灾","配置MME数据（可选）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
NB-IoT场景，用于配置MME侧配置S11-U接口。其中S11-U和N4接口共用VPN。对于容灾的两个UEG-S而言，此配置没有区别，仅以一个UEG-S做配置举例。

## 必备事项
前提条件

无。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
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
          description: '配置业务IP参数。  S11-U和S11-C的VPN实例相同。'
          data_source: '全网规划'
          pattern: ''
          default: IPv4
        SERVICEIPV4:
          name: '业务IPv4地址'
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
          maxLength: 31
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_gtpule_list:
      type: items
      properties:
        GROUPID:
          name: '组号'
          type: integer
          minimum: 0
          maximum: 32
          required: false
          description: '配置本端的S11接口的GTP-U IP。  GTP数据绑定的VPN实例与上面业务IP绑定的VPN实例相同。'
          data_source: '全网规划'
          pattern: ''
          default: 0
        IPTYPE:
          name: 'IP地址类型'
          type: string
          enum:
          - TPTADDR_TYPE_IPV4
          - TPTADDR_TYPE_IPV6
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        LEIPV4:
          name: 'IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VPNNAME:
          name: 'VPN名称'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
  examples:
    add_serviceip_list:
    - IPVERSION: IPv4
      SERVICEIPV4: '192.168.140.20'
      VPNINSTNAME: 'VRF_PS_N4'
    add_gtpule_list:
    - GROUPID: 0
      IPTYPE: TPTADDR_TYPE_IPV4
      LEIPV4: '192.168.140.20'
      VPNNAME: 'VRF_PS_N4'
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 配置S11-U接口业务IP。

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
    ;
{%- endfor -%}
```

### 2 配置GTP IP数据，其中S11-U接口推荐与其他接口共部署，GTPU本端实体对应的组号配置为0。

```jinja2
{%- for item in add_gtpule_list -%}
    ADD GTPULE:
    {#- --- 必选参数 --- -#}
    IPTYPE={{item.IPTYPE}},
    {#- --- 可选参数 --- -#}
    {%- if item.GROUPID is not none -%}
        GROUPID={{item.GROUPID}},
    {%- endif -%}
    {%- if item.VPNNAME is not none -%}
        VPNNAME="{{item.VPNNAME}}",
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPTYPE=TPTADDR_TYPE_IPV4 时必选 --- -#}
    {%- if item.IPTYPE == 'TPTADDR_TYPE_IPV4' -%}
        LEIPV4="{{item.LEIPV4}}",
    {%- endif -%}
    ;
{%- endfor -%}
```


---
id: GWFD-020903
name: 配置PGW-U到Untrusted Non-3GPP GW的数据（VPN缺省路由组网）
ne_type: UEG
type: feature
description: 适用于PGW-U。  UEG与ePDG互通，用于WiFi用户接入EPC网络。  * 逻辑接口：Paif接口。 * 路由：静态路由。  虚机容器：  * 当数据流量小于10G时可参考本举例进行P-GW到ePDG的互通部署，当数据流量大于10G时请参考配置PGW-U到Untrusted Non-3GPP GW的数据（VPN+OSPF动态路由组网）（虚机容器）部署。 * Paif接口需与VPN实例绑定，这样可在VPN实例内配置到ePDG的缺省路由，实现与整机缺省路由的隔离。  裸机容器：  * Paif接口需与VPN实例绑定，这样可在VPN实例内配置到ePDG的缺省路由，实现与整机缺省路由的隔离。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝S","MEC 特性指南（风筝S）","UEG特性指南","基本接入功能","GWFD-020903 Untrusted Non-3GPP网络用户接入","激活Untrusted Non-3GPP网络用户接入功能","配置PGW-U到Untrusted Non-3GPP GW的数据（VPN缺省路由组网）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
适用于PGW-U。UEG与ePDG互通，用于WiFi用户接入EPC网络。* 逻辑接口：Paif接口。* 路由：静态路由。虚机容器：* 当数据流量小于10G时可参考本举例进行P-GW到ePDG的互通部署，当数据流量大于10G时请参考配置PGW-U到Untrusted Non-3GPP GW的数据（VPN+OSPF动态路由组网）（虚机容器）部署。* Paif接口需与VPN实例绑定，这样可在VPN实例内配置到ePDG的缺省路由，实现与整机缺省路由的隔离。裸机容器：* Paif接口需与VPN实例绑定，这样可在VPN实例内配置到ePDG的缺省路由，实现与整机缺省路由的隔离。

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
          description: '设置指定VPN实例下的地址族。'
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
        VRFRD:
          name: '路由标识'
          type: string
          maxLength: 21
          required: false
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
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: '_public_'
        AFTYPE:
          name: '地址族'
          type: string
          enum:
          - ipv4unicast
          required: true
          description: '缺省路由。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PREFIX:
          name: '路由前缀'
          type: string
          maxLength: 15
          required: true
          description: ''
          data_source: '与对端协商'
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
        NEXTHOP:
          name: '路由下一跳'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '与对端协商'
          pattern: ''
          default: ''
        IFNAME:
          name: '路由出接口名字'
          type: string
          maxLength: 63
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_vpninst_list:
      type: items
      properties:
        VPNINSTANCE:
          name: 'VPN实例'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: '配置VPN实例。'
          data_source: '全网规划'
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
          description: '创建Paif接口。'
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
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPV4MASK1:
          name: '逻辑接口的IPv4掩码1'
          type: string
          maxLength: 15
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
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
  examples:
    add_l3vpninst_list:
    - VRFNAME: 'vpn-s2b'
    add_vpninstaf_list:
    - VRFNAME: 'vpn-s2b'
      AFTYPE: ipv4uni
      VRFRD: '100:1'
    set_bfd_list:
    - BFDENABLE: TRUE
    add_srroute_list:
    - VRFNAME: 'vpn-s2b'
      AFTYPE: ipv4unicast
      PREFIX: '172.16.47.0'
      MASKLENGTH: 24
      DESTVRFNAME: '_public_'
      NEXTHOP: '192.168.94.1'
      IFNAME: 'Invalid0'
    add_vpninst_list:
    - VPNINSTANCE: 'vpn-s2b'
    add_logicinf_list:
    - NAME: 'Paif1/1/0'
      IPVERSION: IPV4
      IPV4ADDRESS1: '10.10.10.10'
      IPV4MASK1: '255.255.255.255'
      VPNINSTANCE: 'vpn-s2b'
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 参考初始配置中**配置静态路由+BFD组网（IPv4）**配置对应的组网。

### 2 创建L3VPN实例。

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
    {#- --- 可选参数 --- -#}
    {%- if item.VRFRD is not none -%}
        VRFRD="{{item.VRFRD}}",
    {%- endif -%}
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

### 参数“DELAYUPTIMER”（会话延迟UP时间）和“TOSEXP”（动态会话报文优先级）可以不用输入，使用默认值即可。

### 4 配置到ePDG的VPN缺省路由。

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
    {%- if item.NEXTHOP is not none -%}
        NEXTHOP="{{item.NEXTHOP}}",
    {%- endif -%}
    {%- if item.IFNAME is not none -%}
        IFNAME="{{item.IFNAME}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 5 配置VPN实例。

```jinja2
{%- for item in add_vpninst_list -%}
    ADD VPNINST:
    {#- --- 必选参数 --- -#}
    VPNINSTANCE="{{item.VPNINSTANCE}}",
    ;
{%- endfor -%}
```

### 6 创建Paif接口。

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


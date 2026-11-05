---
id: ''
name: 配置N4接口本端信息
ne_type: UNC
type: feature
description: 当前UPF不支持NRF服务发现，需要配置Local NRF。本小节仅配置UPF基本信息，配置后SMF会发起与UPF之间的PFCP偶连建立，但还需要进行配置N4接口对端UPF信息小节相关的UPF业务能力配置，SMF才能够在业务流程中正确发现UPF。
risk_level: ''
doc_source: ["网络部署","初始配置","UNC初始配置与调测","组网对接配置","配置SMF&PGW-C&SGW-C&GGSN","公共配置","配置和UPF的对接（N4/Sxa/Sxb）","配置N4接口","配置N4接口本端信息"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
当前UPF不支持NRF服务发现，需要配置Local NRF。本小节仅配置UPF基本信息，配置后SMF会发起与UPF之间的PFCP偶连建立，但还需要进行配置N4接口对端UPF信息小节相关的UPF业务能力配置，SMF才能够在业务流程中正确发现UPF。

## 必备事项
前提条件

* 具备管理员权限的操作人员已经登录华为操作维护系统（登录U2020/MAE客户端或登录OM Portal）。

* 已经获取网设LLD文档。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    add_logicip_list:
      type: items
      properties:
        IPVERSION:
          name: '逻辑IP地址类型'
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
          data_source: ''
          pattern: ''
          default: ''
        DESC:
          name: '描述'
          type: string
          minLength: 0
          maxLength: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LOGICIPV6:
          name: 'IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
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
    add_cpnode_list:
      type: items
      properties:
        CPNODEINDEX:
          name: 'CP节点索引'
          type: integer
          minimum: 0
          maximum: 0
          required: true
          description: '配置控制面节点（即SMF/SMF+GW-C）及端点信息。  目前只支持配置一个CP节点，且CP节点索引只能取值为0。'
          data_source: '固定取值'
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
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        NODEIDFQDNVALUE:
          name: 'CP节点FQDN域名'
          type: string
          minLength: 0
          maxLength: 255
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
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        NODEIDIPV4VALUE:
          name: 'CP节点IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NODEIDIPV6VALUE:
          name: 'CP节点IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_cppoint_list:
      type: items
      properties:
        CPPOINTINDEX:
          name: 'CPPOINT索引'
          type: integer
          minimum: 0
          maximum: 255
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        CPNODEINDEX:
          name: 'CPNODE索引'
          type: integer
          minimum: 0
          maximum: 0
          required: true
          description: '已通过**ADD CPNODE**配置，可以通过**LST CPNODE**查询。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPVERSION:
          name: 'IP版本'
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
          name: 'IPV4值'
          type: string
          maxLength: 15
          required: false
          description: 'CP节点中的IPv4/v6地址和CP端点中的IPv4/v6地址需要相同。'
          data_source: '全网规划'
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
        IPV6:
          name: 'IPV6值'
          type: string
          maxLength: 39
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
  examples:
    add_logicip_list:
    - IPVERSION: IPv4
      LOGICIPV4: '10.26.0.6'
      VPNINSTNAME: 'VRF_CP4'
      DESC: 'FOR N4 Interface4'
      LOGICIPV6: 'fc00:38::2'
      IPV4MTU: 1500
      IPV6MTU: 1500
    add_cpnode_list:
    - CPNODEINDEX: 0
      NODEIDTYPE: CpFqdn
      NODEIDFQDNVALUE: 'node.3gppnetwork.org'
      CPFUNCTION: 0
      NODEIDIPV4VALUE: ''
      NODEIDIPV6VALUE: ''
    add_cppoint_list:
    - CPPOINTINDEX: 0
      CPNODEINDEX: 0
      IPVERSION: IPv4
      IPV4: '10.26.0.6'
      VPNNAME: 'VRF_CP4'
      IPV6: 'fc00:38::2'
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 配置N4业务地址对应的逻辑IP地址。

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

### 2 配置N4本端节点和端点。

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
    {#- --- 条件必选：NODEIDTYPE=CpFqdn 时必选 --- -#}
    {%- if item.NODEIDTYPE == 'CpFqdn' -%}
        NODEIDFQDNVALUE="{{item.NODEIDFQDNVALUE}}",
    {%- endif -%}
    {#- --- 条件必选：NODEIDTYPE=CpIPv4 时必选 --- -#}
    {%- if item.NODEIDTYPE == 'CpIPv4' -%}
        NODEIDIPV4VALUE="{{item.NODEIDIPV4VALUE}}",
    {%- endif -%}
    {#- --- 条件必选：NODEIDTYPE=CpIPv6 时必选 --- -#}
    {%- if item.NODEIDTYPE == 'CpIPv6' -%}
        NODEIDIPV6VALUE="{{item.NODEIDIPV6VALUE}}",
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
    {#- --- 条件必选：IPVERSION=IPv6 时必选 --- -#}
    {%- if item.IPVERSION == 'IPv6' -%}
        IPV6="{{item.IPV6}}",
    {%- endif -%}
    ;
{%- endfor -%}
```


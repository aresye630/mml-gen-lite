---
id: ''
name: 配置到E-SMLC的数据
ne_type: UNC
type: feature
description: 当运营商在部署分组交换网，新增MME时，在配置完成MME到E-SMLC的路由数据后，可通过配置SLs接口数据建立MME到E-SMLC的逻辑连接。
risk_level: ''
doc_source: ["网络部署","初始配置","UNC初始配置与调测","组网对接配置","配置AMF&MME&SGSN","配置MME","配置到E-SMLC的数据"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
当运营商在部署分组交换网，新增MME时，在配置完成MME到E-SMLC的路由数据后，可通过配置SLs接口数据建立MME到E-SMLC的逻辑连接。

## 必备事项
前提条件

* 具备管理员权限的操作人员已经登录华为操作维护系统（登录U2020客户端或登录OM Portal）。

* UNC软件安装已完成。

* 请了解UNC各类接口的类型及命名规范，具体内容请参见业务组网与逻辑接口介绍。
* 对于IPv4组网，已完成自动部署配置动态路由OSPF+BFD组网（IPv4）、配置静态路由+BFD组网（IPv4）、配置BGP over OSPF/静态路由+BFD（IPv4）或手动部署配置动态路由OSPF+BFD组网（IPv4）、配置静态路由+BFD组网（IPv4）、配置BGP over OSPF/静态路由+BFD（IPv4）。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
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
          description: '配置业务IP参数。'
          data_source: '参见“水平网设LLD文档 ”。'
          pattern: ''
          default: IPv4
        SERVICEIPV4:
          name: '业务IPv4地址'
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
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6MTU:
          name: 'IPv6 MTU大小'
          type: integer
          minimum: 1280
          maximum: 65534
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 1500
        SERVICEIPV6:
          name: '业务IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_sctppara_list:
      type: items
      properties:
        SCTPPARAINDEX:
          name: 'SCTP协议参数索引'
          type: integer
          minimum: 0
          maximum: 65534
          required: true
          description: 'SLs接口的SCTP协议参数与S1–MME接口的SCTP协议参数分开配置，便于后续局点搬迁或扩容时，不影响互联网元配置。可以通过****LST SCTPPARA****来查询已存在的SCTP协议参数记录。'
          data_source: ''
          pattern: ''
          default: ''
        SCTPPARANAME:
          name: 'SCTP协议参数名'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'noname'
    add_esmlc_list:
      type: items
      properties:
        ESMLCID:
          name: 'E-SMLC标识'
          type: integer
          minimum: 0
          maximum: 255
          required: true
          description: '配置指定E-SMLC在MME上的SCTP偶联信息。'
          data_source: ''
          pattern: ''
          default: ''
        PRIORITY:
          name: '优先级'
          type: integer
          minimum: 0
          maximum: 5
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 0
        ESMLCNAME:
          name: 'E-SMLC名称'
          type: string
          maxLength: 20
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_lcsaplnk_list:
      type: items
      properties:
        LINKIDX:
          name: '链路索引'
          type: integer
          minimum: 0
          maximum: 23
          required: true
          description: '配置E-SMLC的链路信息。'
          data_source: ''
          pattern: ''
          default: ''
        ESMLCID:
          name: 'E-SMLC标识'
          type: integer
          minimum: 0
          maximum: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPTYPE:
          name: 'IP地址类型'
          type: string
          enum:
          - IPV4
          - IPV6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: IPV4
        LOCALIPV4_1:
          name: '本地IPv4地址1'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LOCALIPV4_2:
          name: '本地IPv4地址2'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LOCALPORT:
          name: '本端端口号'
          type: integer
          minimum: 1024
          maximum: 65534
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 9082
        PEERIPV4_1:
          name: '对端IPv4地址1'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PEERIPV4_2:
          name: '对端IPv4地址2'
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
          minimum: 0
          maximum: 65534
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 9082
        SCTPINDX:
          name: 'SCTP协议参数索引'
          type: integer
          minimum: 0
          maximum: 65534
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LOCALIPV6_1:
          name: '本地IPv6地址1'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LOCALIPV6_2:
          name: '本地IPv6地址2'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PEERIPV6_1:
          name: '对端IPv6地址1'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PEERIPV6_2:
          name: '对端IPv6地址2'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    add_serviceip_list:
    - IPVERSION: IPv4
      SERVICEIPV4: '10.11.11.11'
      VPNINSTNAME: 'VPN_SIG'
      IPV6MTU: 1500
      SERVICEIPV6: ''
    add_sctppara_list:
    - SCTPPARAINDEX: 0
      SCTPPARANAME: 'For_SLs'
    add_esmlc_list:
    - ESMLCID: 1
      PRIORITY: 1
      ESMLCNAME: 'esmlc1.epc.mnc015.mcc123.3gppnetwork.org'
    add_lcsaplnk_list:
    - LINKIDX: 3
      ESMLCID: 1
      IPTYPE: IPV4
      LOCALIPV4_1: '10.11.11.11'
      LOCALIPV4_2: '10.11.11.12'
      LOCALPORT: 9082
      PEERIPV4_1: '10.2.3.4'
      PEERIPV4_2: '10.2.3.5'
      PEERPORT: 9082
      SCTPINDX: 3
      LOCALIPV6_1: ''
      LOCALIPV6_2: ''
      PEERIPV6_1: ''
      PEERIPV6_2: ''
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 进入“MML命令行-UNC”窗口。

### 2 配置SLs接口业务IP。

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
    {#- --- 条件必选：IPVERSION=IPv6 时必选 --- -#}
    {%- if item.IPVERSION == 'IPv6' -%}
        SERVICEIPV6="{{item.SERVICEIPV6}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：IPVERSION=IPv6 时可选 --- -#}
    {%- if item.IPVERSION == 'IPv6' -%}
        {%- if item.IPV6MTU is not none -%}
            IPV6MTU={{item.IPV6MTU}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 配置SLs接口基于IP的宽带信令SCTP偶联配置的协议参数。

```jinja2
{%- for item in add_sctppara_list -%}
    ADD SCTPPARA:
    {#- --- 必选参数 --- -#}
    SCTPPARAINDEX={{item.SCTPPARAINDEX}},
    {#- --- 可选参数 --- -#}
    {%- if item.SCTPPARANAME is not none -%}
        SCTPPARANAME="{{item.SCTPPARANAME}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 配置指定E-SMLC在MME上的SCTP偶联信息。

```jinja2
{%- for item in add_esmlc_list -%}
    ADD ESMLC:
    {#- --- 必选参数 --- -#}
    ESMLCID={{item.ESMLCID}},
    {#- --- 可选参数 --- -#}
    {%- if item.PRIORITY is not none -%}
        PRIORITY={{item.PRIORITY}},
    {%- endif -%}
    {%- if item.ESMLCNAME is not none -%}
        ESMLCNAME="{{item.ESMLCNAME}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 5 配置E-SMLC的链路信息。

```jinja2
{%- for item in add_lcsaplnk_list -%}
    ADD LCSAPLNK:
    {#- --- 必选参数 --- -#}
    LINKIDX={{item.LINKIDX}},
    ESMLCID={{item.ESMLCID}},
    SCTPINDX={{item.SCTPINDX}},
    {#- --- 可选参数 --- -#}
    {%- if item.IPTYPE is not none -%}
        IPTYPE={{item.IPTYPE}},
    {%- endif -%}
    {%- if item.LOCALPORT is not none -%}
        LOCALPORT={{item.LOCALPORT}},
    {%- endif -%}
    {%- if item.PEERPORT is not none -%}
        PEERPORT={{item.PEERPORT}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPTYPE=IPV4 时必选 --- -#}
    {%- if item.IPTYPE == 'IPV4' -%}
        LOCALIPV4_1="{{item.LOCALIPV4_1}}",
    {%- endif -%}
    {#- --- 条件必选：IPTYPE=IPV4 时必选 --- -#}
    {%- if item.IPTYPE == 'IPV4' -%}
        PEERIPV4_1="{{item.PEERIPV4_1}}",
    {%- endif -%}
    {#- --- 条件必选：IPTYPE=IPV6 时必选 --- -#}
    {%- if item.IPTYPE == 'IPV6' -%}
        LOCALIPV6_1="{{item.LOCALIPV6_1}}",
    {%- endif -%}
    {#- --- 条件必选：IPTYPE=IPV6 时必选 --- -#}
    {%- if item.IPTYPE == 'IPV6' -%}
        PEERIPV6_1="{{item.PEERIPV6_1}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：IPTYPE=IPV4 时可选 --- -#}
    {%- if item.IPTYPE == 'IPV4' -%}
        {%- if item.LOCALIPV4_2 is not none -%}
            LOCALIPV4_2="{{item.LOCALIPV4_2}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：IPTYPE=IPV4 时可选 --- -#}
    {%- if item.IPTYPE == 'IPV4' -%}
        {%- if item.PEERIPV4_2 is not none -%}
            PEERIPV4_2="{{item.PEERIPV4_2}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：IPTYPE=IPV6 时可选 --- -#}
    {%- if item.IPTYPE == 'IPV6' -%}
        {%- if item.LOCALIPV6_2 is not none -%}
            LOCALIPV6_2="{{item.LOCALIPV6_2}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：IPTYPE=IPV6 时可选 --- -#}
    {%- if item.IPTYPE == 'IPV6' -%}
        {%- if item.PEERIPV6_2 is not none -%}
            PEERIPV6_2="{{item.PEERIPV6_2}}",
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```


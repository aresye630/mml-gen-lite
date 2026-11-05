---
id: ''
name: 配置到CBC的数据
ne_type: UNC
type: feature
description: 当运营商在部署分组交换网，新增MME时，在配置完成MME到CBC的路由数据后，可通过配置SBc接口数据建立MME到CBC的逻辑连接。
risk_level: ''
doc_source: ["网络部署","初始配置","UNC初始配置与调测","组网对接配置","配置AMF&MME&SGSN","配置MME","配置到CBC的数据"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
当运营商在部署分组交换网，新增MME时，在配置完成MME到CBC的路由数据后，可通过配置SBc接口数据建立MME到CBC的逻辑连接。

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
          description: 'SBc接口的SCTP协议参数与S1接口的SCTP协议参数分开配置，便于后续局点搬迁或扩容时，不影响互联网元配置。可以通过****LST SCTPPARA****来查询已存在的SCTP协议参数记录。'
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
    add_cbc_list:
      type: items
      properties:
        CBCIDX:
          name: 'CBC索引'
          type: integer
          minimum: 0
          maximum: 127
          required: true
          description: '增加CBC配置（假设有两个CBC IP）。'
          data_source: ''
          pattern: ''
          default: ''
        MCC:
          name: 'CBC归属的MCC'
          type: string
          maxLength: 3
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MNC:
          name: 'CBC归属的MNC'
          type: string
          maxLength: 3
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
        IPV4_1:
          name: 'CBC IPv4地址1'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV4_2:
          name: 'CBC IPv4地址2'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CBCNAME:
          name: 'CBC名称'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'noname'
        IPV4_3:
          name: 'CBC IPv4地址3'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV4_4:
          name: 'CBC IPv4地址4'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV4_5:
          name: 'CBC IPv4地址5'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV4_6:
          name: 'CBC IPv4地址6'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV4_7:
          name: 'CBC IPv4地址7'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV4_8:
          name: 'CBC IPv4地址8'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6_1:
          name: 'CBC IPv6地址1'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6_2:
          name: 'CBC IPv6地址2'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6_3:
          name: 'CBC IPv6地址3'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6_4:
          name: 'CBC IPv6地址4'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6_5:
          name: 'CBC IPv6地址5'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6_6:
          name: 'CBC IPv6地址6'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6_7:
          name: 'CBC IPv6地址7'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6_8:
          name: 'CBC IPv6地址8'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_sbcaple_list:
      type: items
      properties:
        LLEINDEX:
          name: '本端实体号'
          type: integer
          minimum: 0
          maximum: 127
          required: true
          description: '用户可根据需要将MME配置成服务器端或客户端，当存在与多个CBC连接时，也可将MME同时配置成服务器端和客户端。  当MME作为客户端时，配置对端IP必须在CBC配置表中存在，链接才会建立。'
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
          name: '本地端口号'
          type: integer
          minimum: 1024
          maximum: 65534
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 29168
        CROSSIPFLAG:
          name: '交叉路径是否可用'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NO
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
        LLENAM:
          name: '本端实体名称'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'noname'
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
    add_sbcaplnk_list:
      type: items
      properties:
        LNKINDEX:
          name: '链路索引'
          type: integer
          minimum: 0
          maximum: 127
          required: true
          description: '用户可根据需要将MME配置成服务器端或客户端，当存在与多个CBC连接时，也可将MME同时配置成服务器端和客户端。  当MME作为客户端时，配置对端IP必须在CBC配置表中存在，链接才会建立。'
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
          name: '本地端口号'
          type: integer
          minimum: 1024
          maximum: 65534
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 29168
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
          minimum: 1024
          maximum: 65534
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 29168
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
        CROSSIPFLAG:
          name: '交叉路径是否可用'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NO
        LINKNAM:
          name: '链路名称'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'noname'
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
      SERVICEIPV4: '10.1.1.1'
      VPNINSTNAME: 'VPN_SIG'
      IPV6MTU: 1500
      SERVICEIPV6: ''
    add_sctppara_list:
    - SCTPPARAINDEX: 1
      SCTPPARANAME: 'For_SBc-AP'
    add_cbc_list:
    - CBCIDX: 0
      MCC: '123'
      MNC: '03'
      IPTYPE: IPV4
      IPV4_1: '10.2.3.4'
      IPV4_2: '10.2.3.5'
      CBCNAME: 'CBC1'
      IPV4_3: ''
      IPV4_4: ''
      IPV4_5: ''
      IPV4_6: ''
      IPV4_7: ''
      IPV4_8: ''
      IPV6_1: ''
      IPV6_2: ''
      IPV6_3: ''
      IPV6_4: ''
      IPV6_5: ''
      IPV6_6: ''
      IPV6_7: ''
      IPV6_8: ''
    add_sbcaple_list:
    - LLEINDEX: 0
      IPTYPE: IPV4
      LOCALIPV4_1: '10.1.1.1'
      LOCALIPV4_2: '10.1.1.2'
      LOCALPORT: 29168
      CROSSIPFLAG: NO
      SCTPINDX: 1
      LLENAM: 'toCBC1'
      LOCALIPV6_1: ''
      LOCALIPV6_2: ''
    add_sbcaplnk_list:
    - LNKINDEX: 0
      IPTYPE: IPV4
      LOCALIPV4_1: '10.1.1.1'
      LOCALIPV4_2: '10.1.1.2'
      LOCALPORT: 29168
      PEERIPV4_1: '10.2.3.4'
      PEERIPV4_2: '10.2.3.5'
      PEERPORT: 29168
      SCTPINDX: 1
      CROSSIPFLAG: NO
      LINKNAM: 'SBCAPLNK1'
      LOCALIPV6_1: ''
      LOCALIPV6_2: ''
      PEERIPV6_1: ''
      PEERIPV6_2: ''
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 进入“MML命令行-UNC”窗口。

### 2 配置SBc接口业务IP。

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

### 3 配置SBc接口基于IP的宽带信令SCTP偶联协议参数。

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

### 4 增加CBC配置。

```jinja2
{%- for item in add_cbc_list -%}
    ADD CBC:
    {#- --- 必选参数 --- -#}
    CBCIDX={{item.CBCIDX}},
    MCC="{{item.MCC}}",
    MNC="{{item.MNC}}",
    {#- --- 可选参数 --- -#}
    {%- if item.IPTYPE is not none -%}
        IPTYPE={{item.IPTYPE}},
    {%- endif -%}
    {%- if item.CBCNAME is not none -%}
        CBCNAME="{{item.CBCNAME}}",
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPTYPE=IPV4 时必选 --- -#}
    {%- if item.IPTYPE == 'IPV4' -%}
        IPV4_1="{{item.IPV4_1}}",
    {%- endif -%}
    {#- --- 条件必选：IPTYPE=IPV6 时必选 --- -#}
    {%- if item.IPTYPE == 'IPV6' -%}
        IPV6_1="{{item.IPV6_1}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：IPTYPE=IPV4 时可选 --- -#}
    {%- if item.IPTYPE == 'IPV4' -%}
        {%- if item.IPV4_2 is not none -%}
            IPV4_2="{{item.IPV4_2}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：IPTYPE=IPV4 时可选 --- -#}
    {%- if item.IPTYPE == 'IPV4' -%}
        {%- if item.IPV4_3 is not none -%}
            IPV4_3="{{item.IPV4_3}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：IPTYPE=IPV4 时可选 --- -#}
    {%- if item.IPTYPE == 'IPV4' -%}
        {%- if item.IPV4_4 is not none -%}
            IPV4_4="{{item.IPV4_4}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：IPTYPE=IPV4 时可选 --- -#}
    {%- if item.IPTYPE == 'IPV4' -%}
        {%- if item.IPV4_5 is not none -%}
            IPV4_5="{{item.IPV4_5}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：IPTYPE=IPV4 时可选 --- -#}
    {%- if item.IPTYPE == 'IPV4' -%}
        {%- if item.IPV4_6 is not none -%}
            IPV4_6="{{item.IPV4_6}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：IPTYPE=IPV4 时可选 --- -#}
    {%- if item.IPTYPE == 'IPV4' -%}
        {%- if item.IPV4_7 is not none -%}
            IPV4_7="{{item.IPV4_7}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：IPTYPE=IPV4 时可选 --- -#}
    {%- if item.IPTYPE == 'IPV4' -%}
        {%- if item.IPV4_8 is not none -%}
            IPV4_8="{{item.IPV4_8}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：IPTYPE=IPV6 时可选 --- -#}
    {%- if item.IPTYPE == 'IPV6' -%}
        {%- if item.IPV6_2 is not none -%}
            IPV6_2="{{item.IPV6_2}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：IPTYPE=IPV6 时可选 --- -#}
    {%- if item.IPTYPE == 'IPV6' -%}
        {%- if item.IPV6_3 is not none -%}
            IPV6_3="{{item.IPV6_3}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：IPTYPE=IPV6 时可选 --- -#}
    {%- if item.IPTYPE == 'IPV6' -%}
        {%- if item.IPV6_4 is not none -%}
            IPV6_4="{{item.IPV6_4}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：IPTYPE=IPV6 时可选 --- -#}
    {%- if item.IPTYPE == 'IPV6' -%}
        {%- if item.IPV6_5 is not none -%}
            IPV6_5="{{item.IPV6_5}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：IPTYPE=IPV6 时可选 --- -#}
    {%- if item.IPTYPE == 'IPV6' -%}
        {%- if item.IPV6_6 is not none -%}
            IPV6_6="{{item.IPV6_6}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：IPTYPE=IPV6 时可选 --- -#}
    {%- if item.IPTYPE == 'IPV6' -%}
        {%- if item.IPV6_7 is not none -%}
            IPV6_7="{{item.IPV6_7}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：IPTYPE=IPV6 时可选 --- -#}
    {%- if item.IPTYPE == 'IPV6' -%}
        {%- if item.IPV6_8 is not none -%}
            IPV6_8="{{item.IPV6_8}}",
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 5 配置SBc-AP链路参数。

#### 5.1 当MME作为服务器端时，增加SBc链路本地实体，用于SBc链路建立。

```jinja2
{%- if is_scenario_as_server -%}
    {%- for item in add_sbcaple_list -%}
        ADD SBCAPLE:
        {#- --- 必选参数 --- -#}
        LLEINDEX={{item.LLEINDEX}},
        SCTPINDX={{item.SCTPINDX}},
        {#- --- 可选参数 --- -#}
        {%- if item.IPTYPE is not none -%}
            IPTYPE={{item.IPTYPE}},
        {%- endif -%}
        {%- if item.LOCALPORT is not none -%}
            LOCALPORT={{item.LOCALPORT}},
        {%- endif -%}
        {%- if item.CROSSIPFLAG is not none -%}
            CROSSIPFLAG={{item.CROSSIPFLAG}},
        {%- endif -%}
        {%- if item.LLENAM is not none -%}
            LLENAM="{{item.LLENAM}}",
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：IPTYPE=IPV4 时必选 --- -#}
        {%- if item.IPTYPE == 'IPV4' -%}
            LOCALIPV4_1="{{item.LOCALIPV4_1}}",
        {%- endif -%}
        {#- --- 条件必选：IPTYPE=IPV6 时必选 --- -#}
        {%- if item.IPTYPE == 'IPV6' -%}
            LOCALIPV6_1="{{item.LOCALIPV6_1}}",
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：IPTYPE=IPV4 时可选 --- -#}
        {%- if item.IPTYPE == 'IPV4' -%}
            {%- if item.LOCALIPV4_2 is not none -%}
                LOCALIPV4_2="{{item.LOCALIPV4_2}}",
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：IPTYPE=IPV6 时可选 --- -#}
        {%- if item.IPTYPE == 'IPV6' -%}
            {%- if item.LOCALIPV6_2 is not none -%}
                LOCALIPV6_2="{{item.LOCALIPV6_2}}",
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 5.2 当MME作为客户端时，增加一条SBc链路。

```jinja2
{%- if is_scenario_as_client -%}
    {%- for item in add_sbcaplnk_list -%}
        ADD SBCAPLNK:
        {#- --- 必选参数 --- -#}
        LNKINDEX={{item.LNKINDEX}},
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
        {%- if item.CROSSIPFLAG is not none -%}
            CROSSIPFLAG={{item.CROSSIPFLAG}},
        {%- endif -%}
        {%- if item.LINKNAM is not none -%}
            LINKNAM="{{item.LINKNAM}}",
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
{%- endif -%}
```


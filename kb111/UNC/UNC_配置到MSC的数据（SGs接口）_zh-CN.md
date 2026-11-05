---
id: ''
name: 配置到MSC的数据（SGs接口）
ne_type: UNC
type: feature
description: 当运营商在部署分组交换网，新增MME时，在配置完成MME到MSC Server的路由数据后，可通过配置SGs接口数据建立MME到MSC Server的逻辑连接。
risk_level: ''
doc_source: ["网络部署","初始配置","UNC初始配置与调测","组网对接配置","配置AMF&MME&SGSN","配置MME","配置到MSC的数据（SGs接口）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
当运营商在部署分组交换网，新增MME时，在配置完成MME到MSC Server的路由数据后，可通过配置SGs接口数据建立MME到MSC Server的逻辑连接。

## 必备事项
前提条件

前提条件

* 具备管理员权限的操作人员已经登录华为操作维护系统（登录U2020客户端或登录OM Portal）。

* UNC软件安装已完成。

* 请了解UNC各类接口的类型及命名规范，具体内容请参见业务组网与逻辑接口介绍。
* 对于IPv4组网，已完成自动部署配置动态路由OSPF+BFD组网（IPv4）、配置静态路由+BFD组网（IPv4）、配置BGP over OSPF/静态路由+BFD（IPv4）或手动部署配置动态路由OSPF+BFD组网（IPv4）、配置静态路由+BFD组网（IPv4）、配置BGP over OSPF/静态路由+BFD（IPv4）。
* 当配置SGs链路时，MME仅作为客户端和MSC对接。
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
          description: 'SGs接口的SCTP协议参数与S1–MME接口的SCTP协议参数分开配置，便于后续局点搬迁或扩容时，不影响互联网元配置。可以通过****LST SCTPPARA****来查询已存在的SCTP协议参数记录。'
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
    add_vlr_list:
      type: items
      properties:
        VN:
          name: 'VLR号'
          type: string
          maxLength: 15
          required: true
          description: '配置MME到指定MSC的SCTP偶联信息。'
          data_source: ''
          pattern: ''
          default: ''
    add_sgslks_list:
      type: items
      properties:
        LSX:
          name: '链路集索引'
          type: integer
          minimum: 0
          maximum: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VN:
          name: 'VLR号'
          type: string
          maxLength: 15
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LSN:
          name: '链路集名'
          type: string
          maxLength: 50
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'noname'
    add_sgslnk_list:
      type: items
      properties:
        LNK:
          name: '链路索引'
          type: integer
          minimum: 0
          maximum: 511
          required: true
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
        VLRIPV4_1:
          name: 'VLR IPv4地址1'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VLRIPV4_2:
          name: 'VLR IPv4地址2'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
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
        LSX:
          name: '链路集索引'
          type: integer
          minimum: 0
          maximum: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
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
        VLRIPV6_1:
          name: 'VLR IPv6地址1'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VLRIPV6_2:
          name: 'VLR IPv6地址2'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_laivlr_list:
      type: items
      properties:
        BGNLAI:
          name: '起始LAI'
          type: string
          maxLength: 10
          required: true
          description: '添加LAI与VLR号对应关系。'
          data_source: ''
          pattern: ''
          default: ''
        VLRNO:
          name: 'VLR号'
          type: string
          maxLength: 15
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_tailai_list:
      type: items
      properties:
        BGNTAI:
          name: '起始TAI'
          type: string
          maxLength: 10
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SUBRANGE:
          name: '用户范围'
          type: string
          enum:
          - ALL_USER
          - IMSI_PREFIX
          - IMSI_RANGE
          - USER_GROUP
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ALL_USER
        LAI:
          name: 'LAI'
          type: string
          maxLength: 10
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SELMODE:
          name: '选择模式'
          type: string
          enum:
          - HOST
          - REALM
          - SUBRANGE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: SUBRANGE
        BEGIMSI:
          name: '起始IMSI'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ENDIMSI:
          name: '终止IMSI'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IMSIPRE:
          name: 'IMSI前缀'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SUBID:
          name: '用户群标识'
          type: integer
          minimum: 1
          maximum: 100
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_sgspara_list:
      type: items
      properties:
        TS6_1:
          name: '位置更新定时器'
          type: integer
          minimum: 0
          maximum: 90
          required: false
          description: '设置SGs接口业务运行参数。'
          data_source: ''
          pattern: ''
          default: ''
        TS8:
          name: 'EPS分离定时器'
          type: integer
          minimum: 1
          maximum: 30
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TS9:
          name: '显式IMSI分离定时器'
          type: integer
          minimum: 1
          maximum: 30
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TS10:
          name: '隐式IMSI分离定时器'
          type: integer
          minimum: 1
          maximum: 30
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NS8:
          name: 'EPS分离重发次数'
          type: integer
          minimum: 0
          maximum: 5
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NS9:
          name: '显式IMSI分离重发次数'
          type: integer
          minimum: 0
          maximum: 6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NS10:
          name: '隐式IMSI分离重发次数'
          type: integer
          minimum: 0
          maximum: 7
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    add_serviceip_list:
    - IPVERSION: IPv4
      SERVICEIPV4: '192.168.140.1'
      VPNINSTNAME: 'VPN_SIG'
      IPV6MTU: 1500
      SERVICEIPV6: ''
    add_sctppara_list:
    - SCTPPARAINDEX: 0
      SCTPPARANAME: 'For_SGs'
    add_vlr_list:
    - VN: '111111111111111'
    add_sgslks_list:
    - LSX: 0
      VN: '111111111111111'
      LSN: 'sgs1'
    add_sgslnk_list:
    - LNK: 0
      VPNNAME: 'VPN_SIG'
      IPTYPE: IPV4
      VLRIPV4_1: '10.80.47.4'
      VLRIPV4_2: '10.80.47.5'
      LOCALIPV4_1: '192.168.140.1'
      LOCALIPV4_2: '192.168.140.17'
      LSX: 0
      SCTPINDX: 0
      LOCALIPV6_1: ''
      LOCALIPV6_2: ''
      VLRIPV6_1: ''
      VLRIPV6_2: ''
    add_laivlr_list:
    - BGNLAI: '308015101'
      VLRNO: '111111111111111'
    add_tailai_list:
    - BGNTAI: '308015101'
      SUBRANGE: ALL_USER
      LAI: '308015101'
      SELMODE: SUBRANGE
      BEGIMSI: ''
      ENDIMSI: ''
      IMSIPRE: ''
      SUBID: ''
    set_sgspara_list:
    - TS6_1: 10
      TS8: 4
      TS9: 5
      TS10: 5
      NS8: 2
      NS9: 2
      NS10: 3
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 进入“MML命令行-UNC”窗口。

### 2 配置SGs接口业务IP。

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

### 3 配置SGs接口基于IP的宽带信令SCTP偶联配置的协议参数。

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

### 4 配置MME到指定MSC的SCTP偶联信息。

```jinja2
{%- for item in add_vlr_list -%}
    ADD VLR:
    {#- --- 必选参数 --- -#}
    VN="{{item.VN}}",
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_sgslks_list -%}
    ADD SGSLKS:
    {#- --- 必选参数 --- -#}
    LSX={{item.LSX}},
    VN="{{item.VN}}",
    {#- --- 可选参数 --- -#}
    {%- if item.LSN is not none -%}
        LSN="{{item.LSN}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_sgslnk_list -%}
    ADD SGSLNK:
    {#- --- 必选参数 --- -#}
    LNK={{item.LNK}},
    LSX={{item.LSX}},
    SCTPINDX={{item.SCTPINDX}},
    {#- --- 可选参数 --- -#}
    {%- if item.VPNNAME is not none -%}
        VPNNAME="{{item.VPNNAME}}",
    {%- endif -%}
    {%- if item.IPTYPE is not none -%}
        IPTYPE={{item.IPTYPE}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPTYPE=IPV4 时必选 --- -#}
    {%- if item.IPTYPE == 'IPV4' -%}
        VLRIPV4_1="{{item.VLRIPV4_1}}",
    {%- endif -%}
    {#- --- 条件必选：IPTYPE=IPV4 时必选 --- -#}
    {%- if item.IPTYPE == 'IPV4' -%}
        LOCALIPV4_1="{{item.LOCALIPV4_1}}",
    {%- endif -%}
    {#- --- 条件必选：IPTYPE=IPV6 时必选 --- -#}
    {%- if item.IPTYPE == 'IPV6' -%}
        LOCALIPV6_1="{{item.LOCALIPV6_1}}",
    {%- endif -%}
    {#- --- 条件必选：IPTYPE=IPV6 时必选 --- -#}
    {%- if item.IPTYPE == 'IPV6' -%}
        VLRIPV6_1="{{item.VLRIPV6_1}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：IPTYPE=IPV4 时可选 --- -#}
    {%- if item.IPTYPE == 'IPV4' -%}
        {%- if item.VLRIPV4_2 is not none -%}
            VLRIPV4_2="{{item.VLRIPV4_2}}",
        {%- endif -%}
    {%- endif -%}
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
    {#- --- 条件可选：IPTYPE=IPV6 时可选 --- -#}
    {%- if item.IPTYPE == 'IPV6' -%}
        {%- if item.VLRIPV6_2 is not none -%}
            VLRIPV6_2="{{item.VLRIPV6_2}}",
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 5 添加MSC覆盖的LA。

```jinja2
{%- for item in add_laivlr_list -%}
    ADD LAIVLR:
    {#- --- 必选参数 --- -#}
    BGNLAI="{{item.BGNLAI}}",
    VLRNO="{{item.VLRNO}}",
    ;
{%- endfor -%}
```

### 6 添加LA覆盖的TA范围。

```jinja2
{%- for item in add_tailai_list -%}
    ADD TAILAI:
    {#- --- 必选参数 --- -#}
    BGNTAI="{{item.BGNTAI}}",
    LAI="{{item.LAI}}",
    {#- --- 可选参数 --- -#}
    {%- if item.SELMODE is not none -%}
        SELMODE={{item.SELMODE}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：SUBRANGE=IMSI_RANGE 时必选 --- -#}
    {%- if item.SUBRANGE == 'IMSI_RANGE' -%}
        BEGIMSI="{{item.BEGIMSI}}",
    {%- endif -%}
    {#- --- 条件必选：SUBRANGE=IMSI_RANGE 时必选 --- -#}
    {%- if item.SUBRANGE == 'IMSI_RANGE' -%}
        ENDIMSI="{{item.ENDIMSI}}",
    {%- endif -%}
    {#- --- 条件必选：SUBRANGE=IMSI_PREFIX 时必选 --- -#}
    {%- if item.SUBRANGE == 'IMSI_PREFIX' -%}
        IMSIPRE="{{item.IMSIPRE}}",
    {%- endif -%}
    {#- --- 条件必选：SUBRANGE=USER_GROUP 时必选 --- -#}
    {%- if item.SUBRANGE == 'USER_GROUP' -%}
        SUBID={{item.SUBID}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：SELMODE=SUBRANGE 时可选 --- -#}
    {%- if item.SELMODE == 'SUBRANGE' -%}
        {%- if item.SUBRANGE is not none -%}
            SUBRANGE={{item.SUBRANGE}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 7 设置SGs接口业务运行参数。

```jinja2
{%- for item in set_sgspara_list -%}
    SET SGSPARA:
    {#- --- 可选参数 --- -#}
    {%- if item.TS6_1 is not none -%}
        TS6_1={{item.TS6_1}},
    {%- endif -%}
    {%- if item.TS8 is not none -%}
        TS8={{item.TS8}},
    {%- endif -%}
    {%- if item.TS9 is not none -%}
        TS9={{item.TS9}},
    {%- endif -%}
    {%- if item.TS10 is not none -%}
        TS10={{item.TS10}},
    {%- endif -%}
    {%- if item.NS8 is not none -%}
        NS8={{item.NS8}},
    {%- endif -%}
    {%- if item.NS9 is not none -%}
        NS9={{item.NS9}},
    {%- endif -%}
    {%- if item.NS10 is not none -%}
        NS10={{item.NS10}},
    {%- endif -%}
    ;
{%- endfor -%}
```


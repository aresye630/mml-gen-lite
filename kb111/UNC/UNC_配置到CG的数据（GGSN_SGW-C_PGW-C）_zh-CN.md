---
id: ''
name: 配置到CG的数据（GGSN/SGW-C/PGW-C）
ne_type: UNC
type: feature
description: 当部署离线计费实现对用户的非实时计费时，需要配置到CG的互通。  适用于SGW-C、PGW-C、GGSN。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","计费管理功能","WSFD-011201 支持离线计费","激活离线计费","配置到CG的数据（GGSN/SGW-C/PGW-C）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
当部署离线计费实现对用户的非实时计费时，需要配置到CG的互通。适用于SGW-C、PGW-C、GGSN。

## 必备事项
前提条件

* 请仔细阅读Ga/Gy接口离线/在线计费。
* 操作员了解UNC各类接口的类型及命名规范，具体内容请参见**《UNC产品手册》：UNC初始配置与调测->了解组网架构->逻辑接口介绍**。
* 操作员了解UNC与对端网元互通时可以采用的各种组网方式，以及每种组网方式的实现及特点等信息。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
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
          description: '创建L3VPN实例'
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
    mod_vpninstaf_list:
      type: items
      properties:
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: true
          description: 'RD（Route Distinguisher）用来唯一标识一个VPN。'
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
          data_source: '全网规划'
          pattern: ''
          default: ''
        VRFRD:
          name: '路由标识'
          type: string
          maxLength: 21
          required: false
          description: ''
          data_source: '全网规划'
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
          description: '创建VPN实例。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_concenpoint_list:
      type: items
      properties:
        GACONCENMODE:
          name: 'Ga集中点模式'
          type: string
          enum:
          - MULTI_PORT
          - SINGLE_CONNECT
          required: false
          description: '如果对端CG网元需要本端提供足够多的Ga链路，可配置GACONCENMODE参数为MULTI\_PORT，并根据GAPORTPERPROC参数调整Ga链路数，否则配置GACONCENMODE参数为SINGLE\_CONNECT。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        GAPORTPERPROC:
          name: 'Ga每进程端口数'
          type: integer
          minimum: 1
          maximum: 5
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
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
          description: '用户增加逻辑IP。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        LOGICIPV4:
          name: 'IPv4地址'
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
          minLength: 1
          maxLength: 31
          required: false
          description: ''
          data_source: '已配置数据中获取'
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
        LOGICIPV6:
          name: 'IPv6地址'
          type: string
          maxLength: 39
          required: false
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
          description: '组级Ga逻辑接口'
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
        IPV4ADDRESS1:
          name: '逻辑接口的IPv4地址1'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV4MASK1:
          name: '逻辑接口的IPv4掩码1'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
        VPNINSTANCE:
          name: 'VPN实例名'
          type: string
          maxLength: 31
          required: false
          description: '已在该配置任务中通过命令**ADD VPNINST**配置，可以使用**LST VPNINST**命令进行查询。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        IPV4ADDRESS2:
          name: '逻辑接口的IPv4地址2'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV4MASK2:
          name: '逻辑接口的IPv4掩码2'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6ADDRESS1:
          name: '逻辑接口的IPv6地址1'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6ADDRESS2:
          name: '逻辑接口的IPv6地址2'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6PREFIXLEN1:
          name: 'IPv6前缀长度1'
          type: integer
          minimum: 128
          maximum: 128
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6PREFIXLEN2:
          name: 'IPv6前缀长度2'
          type: integer
          minimum: 128
          maximum: 128
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_cg_list:
      type: items
      properties:
        IPVERSION:
          name: 'CG IP版本'
          type: string
          enum:
          - IPV4
          - IPV6
          required: true
          description: '配置CG'
          data_source: '本端规划'
          pattern: ''
          default: IPV4
        IPV4ADDR:
          name: 'CG IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        PORT:
          name: 'CG端口号'
          type: integer
          minimum: 1024
          maximum: 65535
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        CDRTYPE:
          name: '话单类型'
          type: string
          enum:
          - R10_ALL
          - R10_PGW
          - R10_SGW
          - R4
          - R5
          - R6
          - R7
          - R8_ALL
          - R8_PGW
          - R8_SGW
          - R98
          - R99
          - R9_ALL
          - R9_PGW
          - R9_SGW
          required: true
          description: ''
          data_source: '对端获取'
          pattern: ''
          default: ''
        PRIORITY:
          name: '等级'
          type: integer
          minimum: 0
          maximum: 100
          required: true
          description: '该优先级为全局CG的优先级，数值越小优先级越高，优先使用优先级高的CG。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPV6ADDR:
          name: 'CG IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_cggroup_list:
      type: items
      properties:
        CGGRPID:
          name: 'CG组ID'
          type: integer
          minimum: 1
          maximum: 32
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_glbcggroup_list:
      type: items
      properties:
        CGGRPID:
          name: 'CG组ID'
          type: integer
          minimum: 0
          maximum: 32
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_cgbinding_list:
      type: items
      properties:
        CGGRPID:
          name: 'CG组ID'
          type: integer
          minimum: 1
          maximum: 32
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CGIPVERSION:
          name: 'CG IP版本'
          type: string
          enum:
          - IPV4
          - IPV6
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: IPV4
        CGPORT:
          name: 'CG端口号'
          type: integer
          minimum: 1024
          maximum: 65535
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PRIORITY:
          name: '等级'
          type: integer
          minimum: 0
          maximum: 100
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CGIPV4ADDR:
          name: 'CG IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CGIPV6ADDR:
          name: 'CG IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_cggrpbinding_list:
      type: items
      properties:
        OFCTEMPLATENAME:
          name: '离线计费模板名'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CGGRPID:
          name: 'CG组ID'
          type: integer
          minimum: 1
          maximum: 32
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_cdrtransfer_list:
      type: items
      properties:
        GTPPMAXPAYLOAD:
          name: 'GTP''消息最大可携带的话单字节数'
          type: integer
          minimum: 1200
          maximum: 7180
          required: false
          description: '为了合理控制话单消息发送长度，避免频繁发送话单消息或话单消息分片，采用此命令设置话单发送消息的最大字节数。为了避免数据包分片，建议该值小于网络MTU。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        RETRANSTIMES:
          name: 'Echo and Data Record Transfer Request重传次数'
          type: integer
          minimum: 1
          maximum: 3
          required: false
          description: 'GTP’消息控制'
          data_source: '本端规划'
          pattern: ''
          default: ''
        RETRANSINTERVAL:
          name: 'Data Record Transfer Request重传时间间隔（秒）'
          type: integer
          minimum: 1
          maximum: 10
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        NARESTRANSINTVL:
          name: 'Node Alive消息重传时间间隔（秒）'
          type: integer
          minimum: 5
          maximum: 600
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        CGSELECTIONMODE:
          name: 'CG选择模式'
          type: string
          enum:
          - MSG_BASED_LB
          - PDP_BASED_LB
          required: false
          description: 'CG负荷分担算法'
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_cdrtransfer_list_1:
      type: items
      properties:
        GTPPMAXPAYLOAD:
          name: 'GTP''消息最大可携带的话单字节数'
          type: integer
          minimum: 1200
          maximum: 7180
          required: false
          description: '为了合理控制话单消息发送长度，避免频繁发送话单消息或话单消息分片，采用此命令设置话单发送消息的最大字节数。为了避免数据包分片，建议该值小于网络MTU。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        RETRANSTIMES:
          name: 'Echo and Data Record Transfer Request重传次数'
          type: integer
          minimum: 1
          maximum: 3
          required: false
          description: 'GTP’消息控制'
          data_source: '本端规划'
          pattern: ''
          default: ''
        RETRANSINTERVAL:
          name: 'Data Record Transfer Request重传时间间隔（秒）'
          type: integer
          minimum: 1
          maximum: 10
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        NARESTRANSINTVL:
          name: 'Node Alive消息重传时间间隔（秒）'
          type: integer
          minimum: 5
          maximum: 600
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        CGSELECTIONMODE:
          name: 'CG选择模式'
          type: string
          enum:
          - MSG_BASED_LB
          - PDP_BASED_LB
          required: false
          description: 'CG负荷分担算法'
          data_source: '本端规划'
          pattern: ''
          default: ''
  examples:
    add_l3vpninst_list:
    - VRFNAME: 'vpn_ga'
    add_vpninstaf_list:
    - VRFNAME: 'vpn_ga'
      AFTYPE: ipv4uni
    mod_vpninstaf_list:
    - VRFNAME: 'vpn_ga'
      AFTYPE: ipv4uni
      VRFRD: '1050:1'
    add_vpninst_list:
    - VPNINSTANCE: 'vpn_ga'
    set_concenpoint_list:
    - GACONCENMODE: SINGLE_CONNECT
      GAPORTPERPROC: ''
    add_logicip_list:
    - IPVERSION: IPv4
      LOGICIPV4: '192.168.10.63'
      VPNINSTNAME: 'vpn_ga'
      IPV4MTU: 1500
      IPV6MTU: 1500
      LOGICIPV6: ''
    add_logicinf_list:
    - NAME: 'gaif1/0/0'
      IPVERSION: IPV4
      IPV4ADDRESS1: '192.168.10.63'
      IPV4MASK1: '255.255.255.255'
      VPNINSTANCE: 'vpn_ga'
      IPV4ADDRESS2: ''
      IPV4MASK2: ''
      IPV6ADDRESS1: ''
      IPV6ADDRESS2: ''
      IPV6PREFIXLEN1: ''
      IPV6PREFIXLEN2: ''
    add_cg_list:
    - IPVERSION: IPV4
      IPV4ADDR: '192.168.0.3'
      PORT: 3386
      CDRTYPE: R7
      PRIORITY: 0
      IPV6ADDR: ''
    add_cggroup_list:
    - CGGRPID: ''
    set_glbcggroup_list:
    - CGGRPID: ''
    add_cgbinding_list:
    - CGGRPID: ''
      CGIPVERSION: IPV4
      CGPORT: ''
      PRIORITY: ''
      CGIPV4ADDR: ''
      CGIPV6ADDR: ''
    add_cggrpbinding_list:
    - OFCTEMPLATENAME: ''
      CGGRPID: ''
    set_cdrtransfer_list:
    - GTPPMAXPAYLOAD: 1400
      RETRANSTIMES: 3
      RETRANSINTERVAL: 2
      NARESTRANSINTVL: 20
      CGSELECTIONMODE: MSG_BASED_LB
    set_cdrtransfer_list_1:
    - GTPPMAXPAYLOAD: 1400
      RETRANSTIMES: 3
      RETRANSINTERVAL: 2
      NARESTRANSINTVL: 20
      CGSELECTIONMODE: MSG_BASED_LB
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 参考**《UNC产品手册》：UNC初始配置与调测->****组网路由配置->****配置VNF侧IP路由数据（非SDN）->****手动部署****->****配置静态路由+BFD组网（IPv4）**配置对应的组网。

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
    ;
{%- endfor -%}
```

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

### 3 创建VPN实例。

```jinja2
{%- for item in add_vpninst_list -%}
    ADD VPNINST:
    {#- --- 必选参数 --- -#}
    VPNINSTANCE="{{item.VPNINSTANCE}}",
    ;
{%- endfor -%}
```

### 4 配置Ga接口集中点的部署模式。

```jinja2
{%- for item in set_concenpoint_list -%}
    SET CONCENPOINT:
    {#- --- 可选参数 --- -#}
    {%- if item.GACONCENMODE is not none -%}
        GACONCENMODE={{item.GACONCENMODE}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：GACONCENMODE=MULTI_PORT 时可选 --- -#}
    {%- if item.GACONCENMODE == 'MULTI_PORT' -%}
        {%- if item.GAPORTPERPROC is not none -%}
            GAPORTPERPROC={{item.GAPORTPERPROC}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 5 配置Ga逻辑接口。

#### 5.1 配置逻辑IP地址。

```jinja2
{%- for item in add_logicip_list -%}
    ADD LOGICIP:
    {#- --- 必选参数 --- -#}
    IPVERSION={{item.IPVERSION}},
    {#- --- 可选参数 --- -#}
    {%- if item.VPNINSTNAME is not none -%}
        VPNINSTNAME="{{item.VPNINSTNAME}}",
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

#### 5.2 配置Ga逻辑接口。

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
    {#- --- 条件可选：IPVERSION=IPV4/IPVER_ALL 时可选 --- -#}
    {%- if item.IPVERSION in ['IPV4', 'IPVER_ALL'] -%}
        {%- if item.IPV4ADDRESS2 is not none -%}
            IPV4ADDRESS2="{{item.IPV4ADDRESS2}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：IPVERSION=IPV4/IPVER_ALL 时可选 --- -#}
    {%- if item.IPVERSION in ['IPV4', 'IPVER_ALL'] -%}
        {%- if item.IPV4MASK2 is not none -%}
            IPV4MASK2="{{item.IPV4MASK2}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：IPVERSION=IPV6/IPVER_ALL 时可选 --- -#}
    {%- if item.IPVERSION in ['IPV6', 'IPVER_ALL'] -%}
        {%- if item.IPV6ADDRESS2 is not none -%}
            IPV6ADDRESS2="{{item.IPV6ADDRESS2}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：IPVERSION=IPV6/IPVER_ALL 时可选 --- -#}
    {%- if item.IPVERSION in ['IPV6', 'IPVER_ALL'] -%}
        {%- if item.IPV6PREFIXLEN2 is not none -%}
            IPV6PREFIXLEN2={{item.IPV6PREFIXLEN2}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### **ADD LOGICINF**中的“IP地址+VPN实例名称”和**ADD LOGICIP**命令中的“IP地址+VPN实例名称”必须一致。

### 6 配置CG信息。

#### 6.1 配置CG信息。

```jinja2
{%- for item in add_cg_list -%}
    ADD CG:
    {#- --- 必选参数 --- -#}
    IPVERSION={{item.IPVERSION}},
    PORT={{item.PORT}},
    PRIORITY={{item.PRIORITY}},
    CDRTYPE={{item.CDRTYPE}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPVERSION=IPV4 时必选 --- -#}
    {%- if item.IPVERSION == 'IPV4' -%}
        IPV4ADDR="{{item.IPV4ADDR}}",
    {%- endif -%}
    {#- --- 条件必选：IPVERSION=IPV6 时必选 --- -#}
    {%- if item.IPVERSION == 'IPV6' -%}
        IPV6ADDR="{{item.IPV6ADDR}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 6.2 **可选**：配置CG组。

```jinja2
{%- if is_optional_cg_group -%}
    {%- for item in add_cggroup_list -%}
        ADD CGGROUP:
        {#- --- 必选参数 --- -#}
        CGGRPID={{item.CGGRPID}},
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 6.3 **可选**：配置全局CG组。

```jinja2
{%- if is_optional_global_cg_group -%}
    {%- for item in set_glbcggroup_list -%}
        SET GLBCGGROUP:
        {#- --- 必选参数 --- -#}
        CGGRPID={{item.CGGRPID}},
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 离线计费模板下未选择到CG组时（模板下未绑定CG组或者根据IMSI/MSISDN号段未匹配到CG组），则使用全局CG组。

#### 离线计费模板下未选择到CG组且没有配置全局CG组时，则使用全局CG。全局CG是该CG未绑定到任一CG组的CG，全局CG的优先级最低。

#### 6.4 **可选**：配置CG组绑定CG。

```jinja2
{%- if is_optional_cg_group_bind_cg -%}
    {%- for item in add_cgbinding_list -%}
        ADD CGBINDING:
        {#- --- 必选参数 --- -#}
        CGGRPID={{item.CGGRPID}},
        CGIPVERSION={{item.CGIPVERSION}},
        CGPORT={{item.CGPORT}},
        PRIORITY={{item.PRIORITY}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：CGIPVERSION=IPV4 时必选 --- -#}
        {%- if item.CGIPVERSION == 'IPV4' -%}
            CGIPV4ADDR="{{item.CGIPV4ADDR}}",
        {%- endif -%}
        {#- --- 条件必选：CGIPVERSION=IPV6 时必选 --- -#}
        {%- if item.CGIPVERSION == 'IPV6' -%}
            CGIPV6ADDR="{{item.CGIPV6ADDR}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 6.5 **可选：**配置CG组绑定关系。

```jinja2
{%- if is_optional_cg_group_binding_relation -%}
    {%- for item in add_cggrpbinding_list -%}
        ADD CGGRPBINDING:
        {#- --- 必选参数 --- -#}
        CGGRPID={{item.CGGRPID}},
        OFCTEMPLATENAME="{{item.OFCTEMPLATENAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 6.6 配置CG的负荷分担算法。

```jinja2
{%- for item in set_cdrtransfer_list -%}
    SET CDRTRANSFER:
    {#- --- 可选参数 --- -#}
    {%- if item.GTPPMAXPAYLOAD is not none -%}
        GTPPMAXPAYLOAD={{item.GTPPMAXPAYLOAD}},
    {%- endif -%}
    {%- if item.RETRANSTIMES is not none -%}
        RETRANSTIMES={{item.RETRANSTIMES}},
    {%- endif -%}
    {%- if item.RETRANSINTERVAL is not none -%}
        RETRANSINTERVAL={{item.RETRANSINTERVAL}},
    {%- endif -%}
    {%- if item.NARESTRANSINTVL is not none -%}
        NARESTRANSINTVL={{item.NARESTRANSINTVL}},
    {%- endif -%}
    {%- if item.CGSELECTIONMODE is not none -%}
        CGSELECTIONMODE={{item.CGSELECTIONMODE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 7 配置GTP'消息控制命令。配置GTP’消息的重发次数和重发间隔、GGSN/SGW-C/PGW-C发给CG的node-alive消息超时重发时间、GTP'消息发送话单时每个数据包的最大字节数。

```jinja2
{%- for item in set_cdrtransfer_list_1 -%}
    SET CDRTRANSFER:
    {#- --- 可选参数 --- -#}
    {%- if item.GTPPMAXPAYLOAD is not none -%}
        GTPPMAXPAYLOAD={{item.GTPPMAXPAYLOAD}},
    {%- endif -%}
    {%- if item.RETRANSTIMES is not none -%}
        RETRANSTIMES={{item.RETRANSTIMES}},
    {%- endif -%}
    {%- if item.RETRANSINTERVAL is not none -%}
        RETRANSINTERVAL={{item.RETRANSINTERVAL}},
    {%- endif -%}
    {%- if item.NARESTRANSINTVL is not none -%}
        NARESTRANSINTVL={{item.NARESTRANSINTVL}},
    {%- endif -%}
    {%- if item.CGSELECTIONMODE is not none -%}
        CGSELECTIONMODE={{item.CGSELECTIONMODE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### GTP’消息的重发次数和重发间隔通常使用默认值。

### 数据包最大字节数有效范围是1200～7180。当设置值不在有效值范围内，则每个数据包最大为7180字节。

### 若话单实际长度大于设置值时，以话单的长度作为实际消息的长度。

### 若话单实际长度小于设置时，可以合并发送多张话单，但不能超过设置值。


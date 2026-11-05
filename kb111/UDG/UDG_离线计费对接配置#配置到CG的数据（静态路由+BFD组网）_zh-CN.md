---
id: ''
name: 配置到CG的数据（静态路由+BFD组网）
ne_type: UDG
type: feature
description: 当部署离线计费实现对用户的非实时计费时，需要配置与CG的互通数据。
risk_level: ''
doc_source: ["特性部署","业务专题","5G Core 计费解决方案","计费解决方案概述","计费方案部署与调测","方案五：部署NCG且融合接口计费组网方案（N40接口+传统Ga/Gy接口）","SMF配置","离线计费配置","离线计费对接配置","配置到CG的数据（静态路由+BFD组网）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
当部署离线计费实现对用户的非实时计费时，需要配置与CG的互通数据。

## 必备事项
前提条件

* 请仔细阅读Ga/Gy接口离线/在线计费。
* 操作员了解UNC各类接口的类型及命名规范，具体内容请参见**《UNC产品手册》：UNC初始配置与调测->了解组网架构与原理->业务组网与逻辑接口介绍**。
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
          minLength: 0
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
          required: false
          description: '如果对端CG网元需要本端提供足够多的Ga链路，可配置GACONCENMODE参数为MULTI\_PORT，并根据GAPORTPERPROC参数调整Ga链路数，否则配置GACONCENMODE参数为SINGLE\_CONNECT。'
          data_source: '本端规划'
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
          minLength: 0
          maxLength: 63
          required: true
          description: '组级Ga逻辑接口。'
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
          minLength: 0
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
        IPV4MTU:
          name: 'IPv4逻辑接口MTU（字节）'
          type: integer
          minimum: 328
          maximum: 9600
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 1500
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
        IPV6MTU:
          name: 'IPv6逻辑接口MTU（字节）'
          type: integer
          minimum: 1280
          maximum: 9600
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 1800
        IPV6PREFIXLEN1:
          name: 'IPv6前缀长度1'
          type: integer
          minimum: 1
          maximum: 128
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6PREFIXLEN2:
          name: 'IPv6前缀长度2'
          type: integer
          minimum: 1
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
          required: false
          description: '配置CG。  说明：  本示例以R9话单为例 ，请根据实际业务需要进行配置。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPV4ADDR:
          name: 'CG IPv4地址'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        PORT:
          name: 'CG端口号'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        PRIORITY:
          name: '等级'
          type: string
          required: false
          description: '该优先级为全局CG的优先级，数值越小优先级越高，优先使用优先级高的CG。优先相同的CG间负荷分担。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        CDRTYPE:
          name: '话单类型'
          type: string
          required: false
          description: ''
          data_source: '对端获取'
          pattern: ''
          default: ''
    set_cdrtransfer_list:
      type: items
      properties:
        GTPPMAXPAYLOAD:
          name: 'GTP''消息最大可携带的话单字节数'
          type: string
          required: false
          description: '为了合理控制话单消息发送长度，避免频繁发送话单消息或话单消息分片，采用此命令设置话单发送消息的最大字节数。为了避免数据包分片，建议该值小于网络MTU值。'
          data_source: ''
          pattern: ''
          default: ''
        RETRANSTIMES:
          name: 'Echo and Data Record Transfer Request重传次数'
          type: string
          required: false
          description: '配置GTP''消息重传控制参数。'
          data_source: ''
          pattern: ''
          default: ''
        RETRANSINTERVAL:
          name: 'Data Record Transfer Request重传时间间隔（秒）'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NARESTRANSINTVL:
          name: 'Node Alive消息重传时间间隔（秒）'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CGSELECTIONMODE:
          name: 'CG选择模式'
          type: string
          required: false
          description: '配置CG负荷分担算法。  说明：  * "MSG\_BASED\_LB"表示基于话单消息进行负载均衡，同一PDP/Bearer的话单可能会发往不同的CG。 * "PDP\_BASED\_LB"表示基于PDP/Bearer进行负载均衡，同一PDP/Bearer的话单在CG状态正常时发往同一CG。 * 本示例以"基于PDP/Bearer的负载均衡"为例，请根据实际业务需要进行配置。'
          data_source: '全局规划'
          pattern: ''
          default: ''
        UDPCHECKSUM:
          name: 'GTP''报文CheckSum开关'
          type: string
          required: false
          description: '-'
          data_source: ''
          pattern: ''
          default: ''
    set_cdrtransfer_list_1:
      type: items
      properties:
        GTPPMAXPAYLOAD:
          name: 'GTP''消息最大可携带的话单字节数'
          type: string
          required: false
          description: '为了合理控制话单消息发送长度，避免频繁发送话单消息或话单消息分片，采用此命令设置话单发送消息的最大字节数。为了避免数据包分片，建议该值小于网络MTU值。'
          data_source: ''
          pattern: ''
          default: ''
        RETRANSTIMES:
          name: 'Echo and Data Record Transfer Request重传次数'
          type: string
          required: false
          description: '配置GTP''消息重传控制参数。'
          data_source: ''
          pattern: ''
          default: ''
        RETRANSINTERVAL:
          name: 'Data Record Transfer Request重传时间间隔（秒）'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NARESTRANSINTVL:
          name: 'Node Alive消息重传时间间隔（秒）'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CGSELECTIONMODE:
          name: 'CG选择模式'
          type: string
          required: false
          description: '配置CG负荷分担算法。  说明：  * "MSG\_BASED\_LB"表示基于话单消息进行负载均衡，同一PDP/Bearer的话单可能会发往不同的CG。 * "PDP\_BASED\_LB"表示基于PDP/Bearer进行负载均衡，同一PDP/Bearer的话单在CG状态正常时发往同一CG。 * 本示例以"基于PDP/Bearer的负载均衡"为例，请根据实际业务需要进行配置。'
          data_source: '全局规划'
          pattern: ''
          default: ''
        UDPCHECKSUM:
          name: 'GTP''报文CheckSum开关'
          type: string
          required: false
          description: '-'
          data_source: ''
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
      IPV4MTU: 1500
      IPV6ADDRESS1: ''
      IPV6ADDRESS2: ''
      IPV6MTU: 1800
      IPV6PREFIXLEN1: ''
      IPV6PREFIXLEN2: ''
    add_cg_list:
    - IPVERSION: IPV4
      IPV4ADDR: 192.168.0.3
      PORT: '3386'
      PRIORITY: '0'
      CDRTYPE: R9_ALL
    set_cdrtransfer_list:
    - GTPPMAXPAYLOAD: '1400'
      RETRANSTIMES: '3'
      RETRANSINTERVAL: '3'
      NARESTRANSINTVL: '5'
      CGSELECTIONMODE: PDP_BASED_LB
      UDPCHECKSUM: ENABLE
    set_cdrtransfer_list_1:
    - GTPPMAXPAYLOAD: '1400'
      RETRANSTIMES: '3'
      RETRANSINTERVAL: '3'
      NARESTRANSINTVL: '5'
      CGSELECTIONMODE: PDP_BASED_LB
      UDPCHECKSUM: ENABLE
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
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_concenpoint_list的变量区（command: SET CONCENPOINT） -#}
<!-- MISSING_MACRO: command=SET CONCENPOINT list_name=set_concenpoint_list step_id=4 -->
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
    {#- --- 条件必选：IPVERSION=IPVER_ALL/IPV6 时必选 --- -#}
    {%- if item.IPVERSION in ['IPVER_ALL', 'IPV6'] -%}
        IPV6ADDRESS1="{{item.IPV6ADDRESS1}}",
    {%- endif -%}
    {#- --- 条件必选：IPVERSION=IPVER_ALL/IPV6 时必选 --- -#}
    {%- if item.IPVERSION in ['IPVER_ALL', 'IPV6'] -%}
        IPV6PREFIXLEN1={{item.IPV6PREFIXLEN1}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：IPVERSION=IPV4/IPVER_ALL/IPV6 时可选 --- -#}
    {%- if item.IPVERSION in ['IPV4', 'IPVER_ALL', 'IPV6'] -%}
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
    {#- --- 条件可选：IPVERSION=IPV4/IPVER_ALL 时可选 --- -#}
    {%- if item.IPVERSION in ['IPV4', 'IPVER_ALL'] -%}
        {%- if item.IPV4MTU is not none -%}
            IPV4MTU={{item.IPV4MTU}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：IPVERSION=IPVER_ALL/IPV6 时可选 --- -#}
    {%- if item.IPVERSION in ['IPVER_ALL', 'IPV6'] -%}
        {%- if item.IPV6ADDRESS2 is not none -%}
            IPV6ADDRESS2="{{item.IPV6ADDRESS2}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：IPVERSION=IPVER_ALL/IPV6 时可选 --- -#}
    {%- if item.IPVERSION in ['IPVER_ALL', 'IPV6'] -%}
        {%- if item.IPV6MTU is not none -%}
            IPV6MTU={{item.IPV6MTU}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：IPVERSION=IPVER_ALL/IPV6 时可选 --- -#}
    {%- if item.IPVERSION in ['IPVER_ALL', 'IPV6'] -%}
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
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_cg_list的变量区（command: ADD CG） -#}
<!-- MISSING_MACRO: command=ADD CG list_name=add_cg_list step_id=6.1 -->
```

#### 6.2 配置CG的负荷分担算法。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_cdrtransfer_list的变量区（command: SET CDRTRANSFER） -#}
<!-- MISSING_MACRO: command=SET CDRTRANSFER list_name=set_cdrtransfer_list step_id=6.2 -->
```

### 7 配置GTP'消息控制命令。配置GTP’消息的重发次数和重发间隔、GGSN/SGW-C/PGW-C发给CG的node-alive消息超时重发时间、GTP'消息发送话单时每个数据包的最大字节数。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_cdrtransfer_list_1的变量区（command: SET CDRTRANSFER） -#}
<!-- MISSING_MACRO: command=SET CDRTRANSFER list_name=set_cdrtransfer_list_1 step_id=7 -->
```

### GTP’消息的重发次数和重发间隔通常使用默认值。

### 数据包最大字节数有效范围是1200～7180。当设置值不在有效值范围内，则每个数据包最大为7180字节。

### 若话单实际长度大于设置值时，以话单的长度作为实际消息的长度。

### 若话单实际长度小于设置时，可以合并发送多张话单，但不能超过设置值。


---
id: ''
name: 配置GRE专线数据（内外双层GRE隧道场景）
ne_type: UEG
type: feature
description: UPF到CPE采用GRE专线，FM CPE至主备CPE也建立GRE隧道时，单UPF场景下数据规划如图2所示，主备UPF容灾组网场景下数据规划如图1所示。本操作指导数据准备以单UPF场景下配置GRE专线为例进行数据准备及配置示例，主备UPF场景下，因主备UPF的GRE隧道至CPE网关1和CPE网关2的目的地址均相同，需在备UPF上将主UPF所配置的GRE隧道数据信息重复配置即可（备UPF的GRE隧道源地址需修改为备UPF所规划的隧道源IP地址）。  * 该场景仅支持IPv4地址池。 * 现网实际部署时请参考图1进行容灾场景的数据规划及部署，单UPF场景仅用于辅助理解本章节配置原理。  **图1** GRE专线数据规划图（主备UPF场景）  **图2** GRE专线数据规划图（单UPF场景）
tags: []
risk_level: ''
doc_source: ["专线（仅连接，地市共享式）","业务发放","5GC toB DNN业务发放（专线，共享式）","通过OMC发放","DNN发放操作","发放共享式UPF+GRE专线","共享式UPF+GRE专线+主锚点UPF（同级）+主备+静态签约地址（GRE冗余备份）","配置数据","配置UPF数据","配置GRE专线数据（内外双层GRE隧道场景）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
UPF到CPE采用GRE专线，FM CPE至主备CPE也建立GRE隧道时，单UPF场景下数据规划如图2所示，主备UPF容灾组网场景下数据规划如图1所示。本操作指导数据准备以单UPF场景下配置GRE专线为例进行数据准备及配置示例，主备UPF场景下，因主备UPF的GRE隧道至CPE网关1和CPE网关2的目的地址均相同，需在备UPF上将主UPF所配置的GRE隧道数据信息重复配置即可（备UPF的GRE隧道源地址需修改为备UPF所规划的隧道源IP地址）。* 该场景仅支持IPv4地址池。* 现网实际部署时请参考图1进行容灾场景的数据规划及部署，单UPF场景仅用于辅助理解本章节配置原理。**图1** GRE专线数据规划图（主备UPF场景）**图2** GRE专线数据规划图（单UPF场景）

## 必备事项
前提条件

* UPF侧已完成N6口的路由相关配置，可参考“配置独立VPN专线”章节配置。
* UEG与企业侧路由器之间的路由互通配置已完成。
* CPE1与CPE网关之间的内层GRE隧道已由数通侧工程师配置完成。
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
          description: '创建Tunnel内层使用的VPN，每个企业需要单独创建。'
          data_source: '本端规划'
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
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_interface_list:
      type: items
      properties:
        IFNAME:
          name: '接口名'
          type: string
          maxLength: 63
          required: true
          description: '创建LoopBack接口。不同企业在本端可复用LoopBack端口及IP，不同企业对端LoopBack地址不同。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        IFADMINSTATUS:
          name: '管理状态'
          type: string
          enum:
          - down
          - up
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
    add_ipbindvpn_list:
      type: items
      properties:
        IFNAME:
          name: '接口名'
          type: string
          maxLength: 63
          required: true
          description: '与LoopBack接口关联的VPN实例。  LoopBack接口和Tunnel接口绑定的VPN实例不同，完成物理和业务上的划分。  说明：  对于共享式MEC场景：GRE隧道承载在公共VPN上，一般选择N6\_Local或者N6\_Internet，依据园区与公网互通情况而定。以**VRF\_N6\_Local\_2B**举例。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: true
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_ifipv4address_list:
      type: items
      properties:
        IFNAME:
          name: '接口名'
          type: string
          maxLength: 63
          required: true
          description: '配置loopBack接口的IP地址。'
          data_source: '从已配置数据中获取'
          pattern: ''
          default: ''
        IFIPADDR:
          name: 'IPv4地址'
          type: string
          maxLength: 15
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        SUBNETMASK:
          name: 'IPv4地址掩码'
          type: string
          maxLength: 15
          required: true
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
    add_interface_list_1:
      type: items
      properties:
        IFNAME:
          name: '接口名'
          type: string
          maxLength: 63
          required: true
          description: 'MTU配置原则：封装GRE隧道出外联口不会再次分片。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        IFMTU:
          name: '接口最大传输单元（byte）'
          type: integer
          minimum: 46
          maximum: 9600
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_gretunnel_list:
      type: items
      properties:
        TNLNAME:
          name: '隧道名称'
          type: string
          maxLength: 63
          required: true
          description: '配置GRE隧道。  Tunnel接口编号只具有本地意义，隧道两端可以使用不同的接口编号。'
          data_source: '从已配置数据中获取'
          pattern: ''
          default: ''
        TNLTYPE:
          name: '隧道类型'
          type: string
          enum:
          - gre
          - gre6
          required: true
          description: '配置隧道类型。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        SRCTYPE:
          name: 'IPv4源类型'
          type: string
          enum:
          - if_name
          - ip_address
          - no_type
          required: false
          description: '指定源类型为接口。'
          data_source: '本端规划'
          pattern: ''
          default: no_type
        SRCIFNAME:
          name: '源接口名称'
          type: string
          maxLength: 63
          required: false
          description: '本端设备的LoopBack接口名称，已通过**ADD INTERFACE**命令配置。'
          data_source: '从已配置数据中获取'
          pattern: ''
          default: ''
        DSTIPADDR:
          name: '目的IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: '对端设备LoopBack接口的IP地址。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        DSTVPNNAME:
          name: '目的VPN名称'
          type: string
          maxLength: 31
          required: false
          description: '隧道的目的地址所属的VPN实例的名称。  已通过**ADD L3VPNINST**命令配置，可以使用**LST L3VPNINST**命令进行查询。'
          data_source: '从已配置数据中获取'
          pattern: ''
          default: ''
        KEEPALVEN:
          name: '使能Keepalive功能'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: '使能Keepalive功能后，GRE隧道源端周期性的发送Keepalive报文，如果GRE隧道对端不可达，本端的Tunnel接口状态会被置为Down。'
          data_source: '本端规划'
          pattern: ''
          default: FALSE
        SRCTYPE6:
          name: 'IPv6源类型'
          type: string
          enum:
          - if_name
          - ip_address
          - no_type
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: no_type
    add_ipbindvpn_list_1:
      type: items
      properties:
        IFNAME:
          name: '接口名'
          type: string
          maxLength: 63
          required: true
          description: '与接口关联的VPN实例。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: true
          description: '已通过**ADD L3VPNINST**命令配置，可以使用**LST L3VPNINST**命令进行查询。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_ifipv4address_list_1:
      type: items
      properties:
        IFNAME:
          name: '接口名'
          type: string
          maxLength: 63
          required: true
          description: '配置IPv4本端Tunnel地址，终端是IPv4地址池时需要增加。'
          data_source: '从已配置数据中获取'
          pattern: ''
          default: ''
        IFIPADDR:
          name: 'IPv4地址'
          type: string
          maxLength: 15
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        SUBNETMASK:
          name: 'IPv4地址掩码'
          type: string
          maxLength: 15
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_srroute_list:
      type: items
      properties:
        AFTYPE:
          name: '地址族'
          type: string
          enum:
          - ipv4unicast
          required: true
          description: '增加Tunnel111隧道间静态路由。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        PREFIX:
          name: '路由前缀'
          type: string
          maxLength: 15
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        MASKLENGTH:
          name: '路由掩码长度'
          type: integer
          minimum: 0
          maximum: 32
          required: true
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: '从已配置数据中获取'
          pattern: ''
          default: '_public_'
        DESTVRFNAME:
          name: '下一跳VPN名字'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IFNAME:
          name: '路由出接口名字'
          type: string
          maxLength: 63
          required: false
          description: ''
          data_source: '从已配置数据中获取'
          pattern: ''
          default: ''
    add_networkroute_list:
      type: items
      properties:
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: false
          description: '配置发布LoopBack路由。  UPF与DCGW之间已通过BGP+静态路由实现路由互通。'
          data_source: '从已配置数据中获取'
          pattern: ''
          default: '_public_'
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
        NETWORKADDRESS:
          name: 'IPv4路由前缀地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        MASKLEN:
          name: 'IPv4掩码长度'
          type: integer
          minimum: 0
          maximum: 32
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
  examples:
    add_l3vpninst_list:
    - VRFNAME: 'VRF_N6_Local_2B_001'
    add_vpninst_list:
    - VPNINSTANCE: 'VRF_N6_Local_2B_001'
    add_interface_list:
    - IFNAME: 'LoopBack10'
      IFADMINSTATUS: up
    add_ipbindvpn_list:
    - IFNAME: 'LoopBack10'
      VRFNAME: 'VRF_N6_Local_2B'
    add_ifipv4address_list:
    - IFNAME: 'LoopBack10'
      IFIPADDR: '10.14.255.12'
      SUBNETMASK: '255.255.255.255'
    add_interface_list_1:
    - IFNAME: 'Tunnel111'
      IFMTU: 1500
    add_gretunnel_list:
    - TNLNAME: 'Tunnel111'
      TNLTYPE: gre
      SRCTYPE: if_name
      SRCIFNAME: 'LoopBack10'
      DSTIPADDR: '10.11.255.12'
      DSTVPNNAME: 'VRF_N6_Local_2B'
      KEEPALVEN: TRUE
      SRCTYPE6: no_type
    add_ipbindvpn_list_1:
    - IFNAME: 'Tunnel111'
      VRFNAME: 'VRF_N6_Local_2B_001'
    add_ifipv4address_list_1:
    - IFNAME: 'Tunnel111'
      IFIPADDR: '172.16.255.1'
      SUBNETMASK: '255.255.255.255'
    add_srroute_list:
    - AFTYPE: ipv4unicast
      PREFIX: '10.13.255.12'
      MASKLENGTH: 32
      VRFNAME: 'VRF_N6_Local_2B_001'
      DESTVRFNAME: 'VRF_N6_Local_2B_001'
      IFNAME: 'Tunnel111'
    add_networkroute_list:
    - VRFNAME: 'VRF_N6_Local_2B'
      AFTYPE: ipv4uni
      NETWORKADDRESS: '10.14.255.12'
      MASKLEN: 32
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 配置Tunnel内层使用的VPN信息。

```jinja2
{%- for item in add_l3vpninst_list -%}
    ADD L3VPNINST:
    {#- --- 必选参数 --- -#}
    VRFNAME="{{item.VRFNAME}}",
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_vpninst_list -%}
    ADD VPNINST:
    {#- --- 必选参数 --- -#}
    VPNINSTANCE="{{item.VPNINSTANCE}}",
    ;
{%- endfor -%}
```

### 2 配置LoopBack接口。

### 对于共享式MEC场景：GRE隧道承载在公共VPN上，一般选择N6\_Local或者N6\_Internet，依据园区与公网互通情况而定。以**VRF\_N6\_Local\_2B**举例。

```jinja2
{%- for item in add_interface_list -%}
    ADD INTERFACE:
    {#- --- 必选参数 --- -#}
    IFNAME="{{item.IFNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.IFADMINSTATUS is not none -%}
        IFADMINSTATUS={{item.IFADMINSTATUS}},
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_ipbindvpn_list -%}
    ADD IPBINDVPN:
    {#- --- 必选参数 --- -#}
    IFNAME="{{item.IFNAME}}",
    VRFNAME="{{item.VRFNAME}}",
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_ifipv4address_list -%}
    ADD IFIPV4ADDRESS:
    {#- --- 必选参数 --- -#}
    IFNAME="{{item.IFNAME}}",
    IFIPADDR="{{item.IFIPADDR}}",
    SUBNETMASK="{{item.SUBNETMASK}}",
    ;
{%- endfor -%}
```

### 3 配置GRE Tunnel。

```jinja2
{%- for item in add_interface_list_1 -%}
    ADD INTERFACE:
    {#- --- 必选参数 --- -#}
    IFNAME="{{item.IFNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.IFMTU is not none -%}
        IFMTU={{item.IFMTU}},
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_gretunnel_list -%}
    ADD GRETUNNEL:
    {#- --- 必选参数 --- -#}
    TNLNAME="{{item.TNLNAME}}",
    TNLTYPE={{item.TNLTYPE}},
    {#- --- 可选参数 --- -#}
    {%- if item.DSTVPNNAME is not none -%}
        DSTVPNNAME="{{item.DSTVPNNAME}}",
    {%- endif -%}
    {%- if item.KEEPALVEN is not none -%}
        KEEPALVEN={{item.KEEPALVEN}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：TNLTYPE=gre 时必选 --- -#}
    {%- if item.TNLTYPE == 'gre' -%}
        SRCTYPE={{item.SRCTYPE}},
    {%- endif -%}
    {#- --- 条件必选：SRCTYPE=if_name 时必选 --- -#}
    {%- if item.SRCTYPE == 'if_name' -%}
        SRCIFNAME="{{item.SRCIFNAME}}",
    {#- --- 条件必选：SRCTYPE6=if_name 时必选 --- -#}
    {%- elif item.SRCTYPE6 == 'if_name' -%}
        SRCIFNAME="{{item.SRCIFNAME}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：TNLTYPE=gre 时可选 --- -#}
    {%- if item.TNLTYPE == 'gre' -%}
        {%- if item.DSTIPADDR is not none -%}
            DSTIPADDR="{{item.DSTIPADDR}}",
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_ipbindvpn_list_1 -%}
    ADD IPBINDVPN:
    {#- --- 必选参数 --- -#}
    IFNAME="{{item.IFNAME}}",
    VRFNAME="{{item.VRFNAME}}",
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_ifipv4address_list_1 -%}
    ADD IFIPV4ADDRESS:
    {#- --- 必选参数 --- -#}
    IFNAME="{{item.IFNAME}}",
    IFIPADDR="{{item.IFIPADDR}}",
    SUBNETMASK="{{item.SUBNETMASK}}",
    ;
{%- endfor -%}
```

### 4 配置隧道间静态路由。

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
    {%- if item.IFNAME is not none -%}
        IFNAME="{{item.IFNAME}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 5 配置发布LoopBack路由。

```jinja2
{%- for item in add_networkroute_list -%}
    ADD NETWORKROUTE:
    {#- --- 必选参数 --- -#}
    AFTYPE={{item.AFTYPE}},
    {#- --- 可选参数 --- -#}
    {%- if item.VRFNAME is not none -%}
        VRFNAME="{{item.VRFNAME}}",
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：AFTYPE=ipv4uni 时必选 --- -#}
    {%- if item.AFTYPE == 'ipv4uni' -%}
        NETWORKADDRESS="{{item.NETWORKADDRESS}}",
    {%- endif -%}
    {#- --- 条件必选：AFTYPE=ipv4uni 时必选 --- -#}
    {%- if item.AFTYPE == 'ipv4uni' -%}
        MASKLEN={{item.MASKLEN}},
    {%- endif -%}
    ;
{%- endfor -%}
```


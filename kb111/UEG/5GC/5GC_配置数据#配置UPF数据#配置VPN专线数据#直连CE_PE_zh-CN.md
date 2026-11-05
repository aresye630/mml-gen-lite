---
id: ''
name: 直连CE/PE
ne_type: UEG
type: feature
description: 开通到园区的业务时，UPF到园区采用VPN专线，直连PE，通过静态路由绑定静态BFD探测的方式进行组网连接。对于容灾的两个UPF而言，此配置没有区别，仅以一个UPF做配置举例，组网规划如图1所示。  * 此场景适用于**机架服务器-ARM**和**刀片式服务器2U-x86**。 * 当对接的网关设备（如FW）不支持BFD时，UEG与对端设备可通过OSPF动态路由进行组网连接。  **图1** 静态路由+BFD组网
tags: []
risk_level: ''
doc_source: ["专网（仅连接，园区入驻式）","业务发放","5GC toB DNN业务发放（专网，入驻式）","通过OMC发放","UEG裸机容器","DNN发放操作","入驻式UPF+VPN专线+主锚点UPF（同级）+主备+静态签约地址（GRE冗余备份）","配置数据","配置UPF数据","配置VPN专线数据","直连CE/PE"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
开通到园区的业务时，UPF到园区采用VPN专线，直连PE，通过静态路由绑定静态BFD探测的方式进行组网连接。对于容灾的两个UPF而言，此配置没有区别，仅以一个UPF做配置举例，组网规划如图1所示。* 此场景适用于**机架服务器-ARM**和**刀片式服务器2U-x86**。* 当对接的网关设备（如FW）不支持BFD时，UEG与对端设备可通过OSPF动态路由进行组网连接。**图1** 静态路由+BFD组网

## 必备事项
前提条件

无。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
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
    add_l3vpninst_list:
      type: items
      properties:
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: true
          description: '配置VPN实例。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        VRFDESCRIPTION:
          name: 'VPN实例描述'
          type: string
          maxLength: 242
          required: false
          description: ''
          data_source: ''
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
          description: ''
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
    mod_interface_list:
      type: items
      properties:
        IFNAME:
          name: '接口名'
          type: string
          maxLength: 63
          required: true
          description: '配置主接口。'
          data_source: '本端规划'
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
    add_interface_list:
      type: items
      properties:
        IFNAME:
          name: '接口名'
          type: string
          maxLength: 63
          required: true
          description: '配置子接口。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        IFDF:
          name: '接口不分片标记'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
    add_ipbindvpn_list:
      type: items
      properties:
        IFNAME:
          name: '接口名'
          type: string
          maxLength: 63
          required: true
          description: '接口绑定VPN。'
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
    add_ethsubif_list:
      type: items
      properties:
        IFNAME:
          name: '子接口名字'
          type: string
          maxLength: 63
          required: true
          description: '在以太网子接口上关联VLAN ID。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        SUBIFTYPE:
          name: '子接口流封装类型'
          type: string
          enum:
          - VlanType
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: VlanType
        VLANTYPEVID:
          name: 'VLAN ID'
          type: integer
          minimum: 1
          maximum: 4094
          required: true
          description: ''
          data_source: '本端规划'
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
          description: '配置外联口IPv4地址。'
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
        ADDRTYPE:
          name: 'IPv4地址类型'
          type: string
          enum:
          - main
          - sub
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: main
    set_ifipv6enable_list:
      type: items
      properties:
        IFNAME:
          name: '接口名'
          type: string
          maxLength: 63
          required: true
          description: '配置IPv6使能。'
          data_source: '从已配置数据中获取'
          pattern: ''
          default: ''
        ENABLEFLAG:
          name: 'IPv6使能标志'
          type: string
          enum:
          - FALSE
          - TRUE
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_ifipv6address_list:
      type: items
      properties:
        IFNAME:
          name: '接口名'
          type: string
          maxLength: 63
          required: true
          description: '配置外联口IPv6地址。'
          data_source: '从已配置数据中获取'
          pattern: ''
          default: ''
        IPV6ADDRESS:
          name: 'IPv6地址'
          type: string
          maxLength: 39
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        PREFIXLEN:
          name: 'IPv6地址前缀'
          type: integer
          minimum: 1
          maximum: 128
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        ADDRTYPE:
          name: 'IPv6地址类型'
          type: string
          enum:
          - anycast
          - global
          - linkLocal
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: global
    add_bfdsession_list:
      type: items
      properties:
        SESSNAME:
          name: '会话名称'
          type: string
          maxLength: 64
          required: true
          description: '新建静态BFD会话。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        ADDRTYPE:
          name: 'IP协议版本号'
          type: string
          enum:
          - IPv4
          - IPv6
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        CREATETYPE4:
          name: 'IPv4会话创建方式'
          type: string
          enum:
          - SESS_AUTO
          - SESS_STATIC
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        ONEARMECHO:
          name: 'IPv4单臂Echo'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        DESTADDR4:
          name: 'IPv4目的地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        LINKTYPE:
          name: '会话链路类型'
          type: string
          enum:
          - IP
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DETECTMULTI:
          name: '检测倍数'
          type: integer
          minimum: 3
          maximum: 50
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 3
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: '从已配置数据中获取'
          pattern: ''
          default: ''
        MINECHORXINT:
          name: '单臂Echo会话的收包间隔（ms）'
          type: integer
          minimum: 30
          maximum: 1000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 200
        LOCALDISCR:
          name: '本地标识符'
          type: integer
          minimum: 1
          maximum: 16384
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IFNAME:
          name: '出接口名称'
          type: string
          maxLength: 63
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        CREATETYPE6:
          name: 'IPv6会话创建方式'
          type: string
          enum:
          - SESS_AUTO
          - SESS_STATIC
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        ONEARMECHO6:
          name: 'IPv6单臂Echo'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: FALSE
        DESTADDR6:
          name: 'IPv6目的地址'
          type: string
          maxLength: 39
          required: false
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
          description: '配置IPv4默认路由数据。'
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
          data_source: '全网规划'
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
        NEXTHOP:
          name: '路由下一跳'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SESSIONNAME:
          name: '静态BFD会话名'
          type: string
          maxLength: 64
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_srroute6_list:
      type: items
      properties:
        AFTYPE:
          name: '地址族'
          type: string
          enum:
          - ipv6unicast
          required: true
          description: '配置IPv6默认路由数据。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        PREFIX:
          name: '路由前缀'
          type: string
          maxLength: 39
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        MASKLENGTH:
          name: '路由掩码长度'
          type: integer
          minimum: 0
          maximum: 128
          required: true
          description: ''
          data_source: '全网规划'
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
        NEXTHOP:
          name: '路由下一跳'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SESSIONNAME:
          name: '静态BFD会话名'
          type: string
          maxLength: 64
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    set_bfd_list:
    - BFDENABLE: TRUE
    add_l3vpninst_list:
    - VRFNAME: 'VRF_N6_Local_2B_001'
      VRFDESCRIPTION: 'N6'
    add_vpninstaf_list:
    - VRFNAME: 'VRF_N6_Local_2B_001'
      AFTYPE: ipv4uni
    mod_interface_list:
    - IFNAME: 'Ethernet64/0/6'
      IFADMINSTATUS: up
    add_interface_list:
    - IFNAME: 'Ethernet64/0/6.1'
      IFDF: FALSE
    add_ipbindvpn_list:
    - IFNAME: 'Ethernet64/0/6.1'
      VRFNAME: 'VRF_N6_Local_2B_001'
    add_ethsubif_list:
    - IFNAME: 'Ethernet64/0/6.1'
      SUBIFTYPE: VlanType
      VLANTYPEVID: 104
    add_ifipv4address_list:
    - IFNAME: 'Ethernet64/0/6.1'
      IFIPADDR: '192.168.85.2'
      SUBNETMASK: '255.255.255.248'
      ADDRTYPE: main
    set_ifipv6enable_list:
    - IFNAME: 'Ethernet64/0/6.1'
      ENABLEFLAG: TRUE
    add_ifipv6address_list:
    - IFNAME: 'Ethernet64/0/6.1'
      IPV6ADDRESS: 'FC00::40C2'
      PREFIXLEN: 123
      ADDRTYPE: global
    add_bfdsession_list:
    - SESSNAME: 'N6if_1_1'
      ADDRTYPE: IPv4
      CREATETYPE4: SESS_STATIC
      ONEARMECHO: FALSE
      DESTADDR4: '192.168.85.1'
      LINKTYPE: IP
      DETECTMULTI: 4
      VRFNAME: 'VRF_N6_Local_2B_001'
      MINECHORXINT: 500
      LOCALDISCR: 322
      IFNAME: 'Ethernet64/0/6.1'
      CREATETYPE6: SESS_STATIC
      ONEARMECHO6: FALSE
      DESTADDR6: 'FC00::40C1'
    add_srroute_list:
    - AFTYPE: ipv4unicast
      PREFIX: '0.0.0.0'
      MASKLENGTH: 0
      VRFNAME: 'VRF_N6_Local_2B_001'
      DESTVRFNAME: 'VRF_N6_Local_2B_001'
      IFNAME: 'Ethernet64/0/6.1'
      NEXTHOP: '192.168.85.1'
      SESSIONNAME: 'N6if_1_1'
    add_srroute6_list:
    - AFTYPE: ipv6unicast
      PREFIX: '0:0:0:0:0:0:0:0'
      MASKLENGTH: 0
      VRFNAME: 'VRF_N6_Local_2B_001'
      DESTVRFNAME: 'VRF_N6_Local_2B_001'
      IFNAME: 'Ethernet64/0/6.1'
      NEXTHOP: 'FC00::40C1'
      SESSIONNAME: 'N6if_IPv6_1'
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 激活全局BFD。

```jinja2
{%- for item in set_bfd_list -%}
    SET BFD:
    {#- --- 必选参数 --- -#}
    BFDENABLE={{item.BFDENABLE}},
    ;
{%- endfor -%}
```

### 2 配置VPN实例。

```jinja2
{%- for item in add_l3vpninst_list -%}
    ADD L3VPNINST:
    {#- --- 必选参数 --- -#}
    VRFNAME="{{item.VRFNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.VRFDESCRIPTION is not none -%}
        VRFDESCRIPTION="{{item.VRFDESCRIPTION}}",
    {%- endif -%}
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

### 3 配置主接口的管理状态为up。

```jinja2
{%- for item in mod_interface_list -%}
    MOD INTERFACE:
    {#- --- 必选参数 --- -#}
    IFNAME="{{item.IFNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.IFADMINSTATUS is not none -%}
        IFADMINSTATUS={{item.IFADMINSTATUS}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 配置子接口。

```jinja2
{%- for item in add_interface_list -%}
    ADD INTERFACE:
    {#- --- 必选参数 --- -#}
    IFNAME="{{item.IFNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.IFDF is not none -%}
        IFDF={{item.IFDF}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 5 接口绑定VPN。

```jinja2
{%- for item in add_ipbindvpn_list -%}
    ADD IPBINDVPN:
    {#- --- 必选参数 --- -#}
    IFNAME="{{item.IFNAME}}",
    VRFNAME="{{item.VRFNAME}}",
    ;
{%- endfor -%}
```

### 6 在以太网子接口上关联VLAN ID。

```jinja2
{%- for item in add_ethsubif_list -%}
    ADD ETHSUBIF:
    {#- --- 必选参数 --- -#}
    IFNAME="{{item.IFNAME}}",
    VLANTYPEVID={{item.VLANTYPEVID}},
    {#- --- 可选参数 --- -#}
    {%- if item.SUBIFTYPE is not none -%}
        SUBIFTYPE={{item.SUBIFTYPE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 7 配置外联口IPv4地址。

```jinja2
{%- for item in add_ifipv4address_list -%}
    ADD IFIPV4ADDRESS:
    {#- --- 必选参数 --- -#}
    IFNAME="{{item.IFNAME}}",
    IFIPADDR="{{item.IFIPADDR}}",
    SUBNETMASK="{{item.SUBNETMASK}}",
    {#- --- 可选参数 --- -#}
    {%- if item.ADDRTYPE is not none -%}
        ADDRTYPE={{item.ADDRTYPE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 8 配置IPv6使能。

```jinja2
{%- for item in set_ifipv6enable_list -%}
    SET IFIPV6ENABLE:
    {#- --- 必选参数 --- -#}
    IFNAME="{{item.IFNAME}}",
    ENABLEFLAG={{item.ENABLEFLAG}},
    ;
{%- endfor -%}
```

### 9 配置外联口IPv6地址。

```jinja2
{%- for item in add_ifipv6address_list -%}
    ADD IFIPV6ADDRESS:
    {#- --- 必选参数 --- -#}
    IFNAME="{{item.IFNAME}}",
    IPV6ADDRESS="{{item.IPV6ADDRESS}}",
    PREFIXLEN={{item.PREFIXLEN}},
    {#- --- 可选参数 --- -#}
    {%- if item.ADDRTYPE is not none -%}
        ADDRTYPE={{item.ADDRTYPE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 10 新建静态BFD会话。

```jinja2
{%- for item in add_bfdsession_list -%}
    ADD BFDSESSION:
    {#- --- 必选参数 --- -#}
    SESSNAME="{{item.SESSNAME}}",
    ADDRTYPE={{item.ADDRTYPE}},
    LINKTYPE={{item.LINKTYPE}},
    {#- --- 可选参数 --- -#}
    {%- if item.DETECTMULTI is not none -%}
        DETECTMULTI={{item.DETECTMULTI}},
    {%- endif -%}
    {%- if item.VRFNAME is not none -%}
        VRFNAME="{{item.VRFNAME}}",
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：ADDRTYPE=IPv4 时必选 --- -#}
    {%- if item.ADDRTYPE == 'IPv4' -%}
        CREATETYPE4={{item.CREATETYPE4}},
    {%- endif -%}
    {#- --- 条件必选：CREATETYPE4=SESS_STATIC 时必选 --- -#}
    {%- if item.CREATETYPE4 == 'SESS_STATIC' -%}
        ONEARMECHO={{item.ONEARMECHO}},
    {%- endif -%}
    {#- --- 条件必选：ADDRTYPE=IPv4 时必选 --- -#}
    {%- if item.ADDRTYPE == 'IPv4' -%}
        DESTADDR4="{{item.DESTADDR4}}",
    {%- endif -%}
    {#- --- 条件必选：CREATETYPE4=SESS_STATIC 时必选 --- -#}
    {%- if item.CREATETYPE4 == 'SESS_STATIC' -%}
        LOCALDISCR={{item.LOCALDISCR}},
    {#- --- 条件必选：CREATETYPE6=SESS_STATIC 时必选 --- -#}
    {%- elif item.CREATETYPE6 == 'SESS_STATIC' -%}
        LOCALDISCR={{item.LOCALDISCR}},
    {%- endif -%}
    {#- --- 条件必选：ADDRTYPE=IPv6 时必选 --- -#}
    {%- if item.ADDRTYPE == 'IPv6' -%}
        CREATETYPE6={{item.CREATETYPE6}},
    {%- endif -%}
    {#- --- 条件必选：ADDRTYPE=IPv6 时必选 --- -#}
    {%- if item.ADDRTYPE == 'IPv6' -%}
        DESTADDR6="{{item.DESTADDR6}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：ONEARMECHO=TRUE 时可选 --- -#}
    {%- if item.ONEARMECHO == 'TRUE' -%}
        {%- if item.MINECHORXINT is not none -%}
            MINECHORXINT={{item.MINECHORXINT}},
        {%- endif -%}
    {#- --- 条件可选：ONEARMECHO6=TRUE 时可选 --- -#}
    {%- elif item.ONEARMECHO6 == 'TRUE' -%}
        {%- if item.MINECHORXINT is not none -%}
            MINECHORXINT={{item.MINECHORXINT}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：CREATETYPE6=SESS_STATIC 时可选 --- -#}
    {%- if item.CREATETYPE6 == 'SESS_STATIC' -%}
        {%- if item.ONEARMECHO6 is not none -%}
            ONEARMECHO6={{item.ONEARMECHO6}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件必选/可选参数 --- -#}
    {#- --- 出接口名称: 条件必选(IPv4单臂Echo=TRUE; IPv6单臂Echo=TRUE) / 条件可选(IPv4会话创建方式=SESS_AUTO; IPv6会话创建方式=SESS_AUTO; IPv4单臂Echo=FALSE; IPv6单臂Echo=FALSE) --- -#}
    {%- if (item.ONEARMECHO == 'TRUE') or (item.ONEARMECHO6 == 'TRUE') -%}
        IFNAME="{{item.IFNAME}}",
    {%- elif (item.CREATETYPE4 == 'SESS_AUTO') or (item.CREATETYPE6 == 'SESS_AUTO') or (item.ONEARMECHO == 'FALSE') or (item.ONEARMECHO6 == 'FALSE') -%}
        {%- if item.IFNAME is not none -%}
            IFNAME="{{item.IFNAME}}",
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 11 配置静态路由数据。

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
    {%- if item.NEXTHOP is not none -%}
        NEXTHOP="{{item.NEXTHOP}}",
    {%- endif -%}
    {%- if item.SESSIONNAME is not none -%}
        SESSIONNAME="{{item.SESSIONNAME}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_srroute6_list -%}
    ADD SRROUTE6:
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
    {%- if item.NEXTHOP is not none -%}
        NEXTHOP="{{item.NEXTHOP}}",
    {%- endif -%}
    {%- if item.SESSIONNAME is not none -%}
        SESSIONNAME="{{item.SESSIONNAME}}",
    {%- endif -%}
    ;
{%- endfor -%}
```


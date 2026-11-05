---
id: GWFD-030601
name: 激活GRE跨域转发（OSPFv3）
ne_type: UEG
type: feature
description: 在UEG上基于OSPFv3配置GRE跨域转发功能时，请参考本页面进行操作。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝S","MEC 特性指南（风筝S）","UEG特性指南","网关能力增强","GWFD-030601 GRE跨域转发","激活GRE跨域转发（OSPFv3）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
在UEG上基于OSPFv3配置GRE跨域转发功能时，请参考本页面进行操作。

## 必备事项
前提条件

请仔细阅读GWFD-030601 GRE跨域转发特性概述。
完成**License****加载**（如果有需求，请联系华为技术支持工程师处理）。
已完成园区外UPF，园区内UPF整体网络及业务部署。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    add_interface_list:
      type: items
      properties:
        IFNAME:
          name: '接口名'
          type: string
          maxLength: 63
          required: true
          description: '-'
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
          data_source: ''
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
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: true
          description: '-'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    set_ifipv6enable_list:
      type: items
      properties:
        IFNAME:
          name: '接口名'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ENABLEFLAG:
          name: 'IPv6使能标志'
          type: string
          enum:
          - FALSE
          - TRUE
          required: true
          description: '使能IPv6。'
          data_source: '固定取值'
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
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6ADDRESS:
          name: 'IPv6地址'
          type: string
          maxLength: 39
          required: true
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        PREFIXLEN:
          name: 'IPv6地址前缀'
          type: integer
          minimum: 1
          maximum: 128
          required: true
          description: '-'
          data_source: '固定取值'
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
        IDGENTYPE:
          name: 'IPv6地址计算类型'
          type: string
          enum:
          - cga
          - eui64
          - none
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: none
    add_interface_list_2:
      type: items
      properties:
        IFNAME:
          name: '接口名'
          type: string
          maxLength: 63
          required: true
          description: '-'
          data_source: '全网规划'
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
    add_ipbindvpn_list_2:
      type: items
      properties:
        IFNAME:
          name: '接口名'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: true
          description: '-'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    set_ifipv6enable_list_2:
      type: items
      properties:
        IFNAME:
          name: '接口名'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ENABLEFLAG:
          name: 'IPv6使能标志'
          type: string
          enum:
          - FALSE
          - TRUE
          required: true
          description: '使能IPv6。'
          data_source: '固定取值'
          pattern: ''
          default: ''
    add_ifipv6address_list_2:
      type: items
      properties:
        IFNAME:
          name: '接口名'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6ADDRESS:
          name: 'IPv6地址'
          type: string
          maxLength: 39
          required: true
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        PREFIXLEN:
          name: 'IPv6地址前缀'
          type: integer
          minimum: 1
          maximum: 128
          required: true
          description: '-'
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
        IDGENTYPE:
          name: 'IPv6地址计算类型'
          type: string
          enum:
          - cga
          - eui64
          - none
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: none
    add_gretunnel_list:
      type: items
      properties:
        TNLNAME:
          name: '隧道名称'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TNLTYPE:
          name: '隧道类型'
          type: string
          enum:
          - gre
          - gre6
          required: true
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: ''
        SRCTYPE6:
          name: 'IPv6源类型'
          type: string
          enum:
          - if_name
          - ip_address
          - no_type
          required: false
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: no_type
        SRCIFNAME:
          name: '源接口名称'
          type: string
          maxLength: 63
          required: false
          description: '已通过**ADD INTERFACE**命令配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        DSTIPV6ADDR:
          name: '目的IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: '-'
          data_source: '与对端协商'
          pattern: ''
          default: ''
        DSTVPNNAME:
          name: '目的VPN名称'
          type: string
          maxLength: 31
          required: false
          description: '-'
          data_source: '与对端协商'
          pattern: ''
          default: ''
        KEEPALVEN:
          name: '使能Keepalive功能'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        GREKEYEN:
          name: '使能识别关键字功能'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        CHECKSUMEN:
          name: '使能端到端校验功能'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        STATENABLE:
          name: '使能报文统计功能'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        REDUNDANCYEN:
          name: '使能备份隧道功能'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        SRCTYPE:
          name: 'IPv4源类型'
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
    add_ospfv3_list:
      type: items
      properties:
        PROCID:
          name: '进程号'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: true
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        ROUTERID:
          name: '路由器标识'
          type: string
          maxLength: 15
          required: true
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        VRFNAME:
          name: 'VPN名称'
          type: string
          maxLength: 31
          required: false
          description: '-'
          data_source: '已配置数据中获取'
          pattern: ''
          default: '_public_'
        SILENTALLFLAG:
          name: '抑制接口收发OSPFv3报文'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        BFDALLINTFFLG:
          name: '使能BFD'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        BFDRXCFGFLAG:
          name: '是否配置BFD最小接收报文间隔'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        BFDTXCFGFLAG:
          name: '是否配置BFD最小发送报文间隔'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        FRRBINDINGFLAG:
          name: 'BFD会话与接口链路状态绑定标志'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        ROUTAGFLAG:
          name: '配置VPN引入路由的tag值'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        RXMTLIMITENABLE:
          name: '使能最大重传次数'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        VPNINSCAPSIMFLG:
          name: '去使能VPN路由环路检测'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: FALSE
        RTTAGDISFLAG:
          name: '去使能标签环路检测'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        STUBROUFLG:
          name: 'OSPFv3 Stub路由器'
          type: string
          enum:
          - NoConfig
          - StubOnBoot
          - StubOnHand
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NoConfig
        DOMAINNULLFLAG:
          name: '配置Domain ID为空'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        VIRTUALSYSFLAG:
          name: 'OSPFv3共网段虚拟系统使能标志'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: TRUE
    add_ospfv3area_list:
      type: items
      properties:
        PROCID:
          name: 'OSPFv3进程号'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AREAID:
          name: '区域号'
          type: string
          maxLength: 15
          required: true
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        AREATYPE:
          name: 'OSPFv3区域类型'
          type: string
          enum:
          - NSSA
          - Normal
          - Stub
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: Normal
    add_ospfv3interface_list:
      type: items
      properties:
        PROCID:
          name: 'OSPFv3进程号'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AREAID:
          name: '区域号'
          type: string
          maxLength: 15
          required: true
          description: '已通过**ADD OSPFAREA**  命令配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        IFNAME:
          name: '接口名'
          type: string
          maxLength: 63
          required: true
          description: '已通过**ADD INTERFACE**命令配置的GRE隧道的接口名。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        MTUENABLE:
          name: '使能MTU'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: TRUE
        TIMERCONSERFLAG:
          name: '是否使能邻居失效定时器保守模式'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        BFDENABLE:
          name: '使能BFD'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        FRRBINDINGFLAG:
          name: 'BFD会话与接口链路状态绑定标志'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        FRRBLOCKFLAG:
          name: '阻止指定OSPFv3接口的FRR能力'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        BFDBLOCK:
          name: '阻塞接口动态创建BFD特性'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        VIRTUALSYSFLAG:
          name: 'OSPFv3共网段虚拟系统使能标志'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
    add_ospfv3importroute_list:
      type: items
      properties:
        PROCID:
          name: 'OSPFv3进程号'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PROTOCOL:
          name: '协议号'
          type: string
          enum:
          - bgp
          - direct
          - ospfv3
          - static
          - wlr
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IMPTCOSTCFG:
          name: '引入路由开销值配置'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        IMPTTAGCFG:
          name: '引入路由标签配置'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        IMPTTYPECFG:
          name: '引入路由类型配置'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        INHERITCOSTCFG:
          name: '指定引入路由时继承原路由的开销值'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
  examples:
    add_interface_list:
    - IFNAME: 'LoopBack85'
      IFADMINSTATUS: up
      IFDF: FALSE
    add_ipbindvpn_list:
    - IFNAME: 'LoopBack85'
      VRFNAME: 'VRF_DC12_N9'
    set_ifipv6enable_list:
    - IFNAME: 'LoopBack85'
      ENABLEFLAG: TRUE
    add_ifipv6address_list:
    - IFNAME: 'LoopBack85'
      IPV6ADDRESS: 'fc00:1:0:0:0:0:0:100'
      PREFIXLEN: 64
      ADDRTYPE: global
      IDGENTYPE: none
    add_interface_list_2:
    - IFNAME: 'Tunnel85'
      IFDF: FALSE
    add_ipbindvpn_list_2:
    - IFNAME: 'Tunnel85'
      VRFNAME: 'VRF_DC12_N6_local_001'
    set_ifipv6enable_list_2:
    - IFNAME: 'Tunnel85'
      ENABLEFLAG: TRUE
    add_ifipv6address_list_2:
    - IFNAME: 'Tunnel85'
      IPV6ADDRESS: 'fc00:100:0:0:0:0:0:1'
      PREFIXLEN: 64
      ADDRTYPE: global
      IDGENTYPE: none
    add_gretunnel_list:
    - TNLNAME: 'Tunnel85'
      TNLTYPE: gre6
      SRCTYPE6: if_name
      SRCIFNAME: 'LoopBack85'
      DSTIPV6ADDR: 'fc00:1:0:0:0:0:0:200'
      DSTVPNNAME: 'VRF_DC11_N9'
      KEEPALVEN: FALSE
      GREKEYEN: FALSE
      CHECKSUMEN: FALSE
      STATENABLE: FALSE
      REDUNDANCYEN: FALSE
      SRCTYPE: no_type
    add_ospfv3_list:
    - PROCID: 85
      ROUTERID: '10.100.100.100'
      VRFNAME: 'VRF_DC12_N6_local_001'
      SILENTALLFLAG: FALSE
      BFDALLINTFFLG: FALSE
      BFDRXCFGFLAG: FALSE
      BFDTXCFGFLAG: FALSE
      FRRBINDINGFLAG: FALSE
      ROUTAGFLAG: FALSE
      RXMTLIMITENABLE: FALSE
      VPNINSCAPSIMFLG: TRUE
      RTTAGDISFLAG: FALSE
      STUBROUFLG: NoConfig
      DOMAINNULLFLAG: FALSE
      VIRTUALSYSFLAG: TRUE
    add_ospfv3area_list:
    - PROCID: 85
      AREAID: '0.0.0.0'
      AREATYPE: Normal
    add_ospfv3interface_list:
    - PROCID: 85
      AREAID: '0.0.0.0'
      IFNAME: 'Tunnel85'
      MTUENABLE: TRUE
      TIMERCONSERFLAG: FALSE
      BFDENABLE: FALSE
      FRRBINDINGFLAG: FALSE
      FRRBLOCKFLAG: FALSE
      BFDBLOCK: FALSE
      VIRTUALSYSFLAG: FALSE
    add_ospfv3importroute_list:
    - PROCID: 85
      PROTOCOL: wlr
      IMPTCOSTCFG: FALSE
      IMPTTAGCFG: FALSE
      IMPTTYPECFG: FALSE
      INHERITCOSTCFG: FALSE
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 配置LoopBack接口。

```jinja2
{%- for item in add_interface_list -%}
    ADD INTERFACE:
    {#- --- 必选参数 --- -#}
    IFNAME="{{item.IFNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.IFADMINSTATUS is not none -%}
        IFADMINSTATUS={{item.IFADMINSTATUS}},
    {%- endif -%}
    {%- if item.IFDF is not none -%}
        IFDF={{item.IFDF}},
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
{%- for item in set_ifipv6enable_list -%}
    SET IFIPV6ENABLE:
    {#- --- 必选参数 --- -#}
    IFNAME="{{item.IFNAME}}",
    ENABLEFLAG={{item.ENABLEFLAG}},
    ;
{%- endfor -%}
```

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
    {%- if item.IDGENTYPE is not none -%}
        IDGENTYPE={{item.IDGENTYPE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 2 配置GRE Tunnel。

```jinja2
{%- for item in add_interface_list_2 -%}
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

```jinja2
{%- for item in add_ipbindvpn_list_2 -%}
    ADD IPBINDVPN:
    {#- --- 必选参数 --- -#}
    IFNAME="{{item.IFNAME}}",
    VRFNAME="{{item.VRFNAME}}",
    ;
{%- endfor -%}
```

```jinja2
{%- for item in set_ifipv6enable_list_2 -%}
    SET IFIPV6ENABLE:
    {#- --- 必选参数 --- -#}
    IFNAME="{{item.IFNAME}}",
    ENABLEFLAG={{item.ENABLEFLAG}},
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_ifipv6address_list_2 -%}
    ADD IFIPV6ADDRESS:
    {#- --- 必选参数 --- -#}
    IFNAME="{{item.IFNAME}}",
    IPV6ADDRESS="{{item.IPV6ADDRESS}}",
    PREFIXLEN={{item.PREFIXLEN}},
    {#- --- 可选参数 --- -#}
    {%- if item.ADDRTYPE is not none -%}
        ADDRTYPE={{item.ADDRTYPE}},
    {%- endif -%}
    {%- if item.IDGENTYPE is not none -%}
        IDGENTYPE={{item.IDGENTYPE}},
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
    {%- if item.KEEPALVEN is not none -%}
        KEEPALVEN={{item.KEEPALVEN}},
    {%- endif -%}
    {%- if item.GREKEYEN is not none -%}
        GREKEYEN={{item.GREKEYEN}},
    {%- endif -%}
    {%- if item.CHECKSUMEN is not none -%}
        CHECKSUMEN={{item.CHECKSUMEN}},
    {%- endif -%}
    {%- if item.STATENABLE is not none -%}
        STATENABLE={{item.STATENABLE}},
    {%- endif -%}
    {%- if item.DSTVPNNAME is not none -%}
        DSTVPNNAME="{{item.DSTVPNNAME}}",
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：TNLTYPE=gre6 时必选 --- -#}
    {%- if item.TNLTYPE == 'gre6' -%}
        SRCTYPE6={{item.SRCTYPE6}},
    {%- endif -%}
    {#- --- 条件必选：SRCTYPE=if_name 时必选 --- -#}
    {%- if item.SRCTYPE == 'if_name' -%}
        SRCIFNAME="{{item.SRCIFNAME}}",
    {#- --- 条件必选：SRCTYPE6=if_name 时必选 --- -#}
    {%- elif item.SRCTYPE6 == 'if_name' -%}
        SRCIFNAME="{{item.SRCIFNAME}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：TNLTYPE=gre6 时可选 --- -#}
    {%- if item.TNLTYPE == 'gre6' -%}
        {%- if item.DSTIPV6ADDR is not none -%}
            DSTIPV6ADDR="{{item.DSTIPV6ADDR}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：TNLTYPE=gre/gre6 时可选 --- -#}
    {%- if item.TNLTYPE in ['gre', 'gre6'] -%}
        {%- if item.REDUNDANCYEN is not none -%}
            REDUNDANCYEN={{item.REDUNDANCYEN}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 配置OSPF。

```jinja2
{%- for item in add_ospfv3_list -%}
    ADD OSPFV3:
    {#- --- 必选参数 --- -#}
    PROCID={{item.PROCID}},
    ROUTERID="{{item.ROUTERID}}",
    {#- --- 可选参数 --- -#}
    {%- if item.VRFNAME is not none -%}
        VRFNAME="{{item.VRFNAME}}",
    {%- endif -%}
    {%- if item.SILENTALLFLAG is not none -%}
        SILENTALLFLAG={{item.SILENTALLFLAG}},
    {%- endif -%}
    {%- if item.BFDALLINTFFLG is not none -%}
        BFDALLINTFFLG={{item.BFDALLINTFFLG}},
    {%- endif -%}
    {%- if item.BFDRXCFGFLAG is not none -%}
        BFDRXCFGFLAG={{item.BFDRXCFGFLAG}},
    {%- endif -%}
    {%- if item.BFDTXCFGFLAG is not none -%}
        BFDTXCFGFLAG={{item.BFDTXCFGFLAG}},
    {%- endif -%}
    {%- if item.FRRBINDINGFLAG is not none -%}
        FRRBINDINGFLAG={{item.FRRBINDINGFLAG}},
    {%- endif -%}
    {%- if item.ROUTAGFLAG is not none -%}
        ROUTAGFLAG={{item.ROUTAGFLAG}},
    {%- endif -%}
    {%- if item.RXMTLIMITENABLE is not none -%}
        RXMTLIMITENABLE={{item.RXMTLIMITENABLE}},
    {%- endif -%}
    {%- if item.VPNINSCAPSIMFLG is not none -%}
        VPNINSCAPSIMFLG={{item.VPNINSCAPSIMFLG}},
    {%- endif -%}
    {%- if item.RTTAGDISFLAG is not none -%}
        RTTAGDISFLAG={{item.RTTAGDISFLAG}},
    {%- endif -%}
    {%- if item.STUBROUFLG is not none -%}
        STUBROUFLG={{item.STUBROUFLG}},
    {%- endif -%}
    {%- if item.DOMAINNULLFLAG is not none -%}
        DOMAINNULLFLAG={{item.DOMAINNULLFLAG}},
    {%- endif -%}
    {%- if item.VIRTUALSYSFLAG is not none -%}
        VIRTUALSYSFLAG={{item.VIRTUALSYSFLAG}},
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_ospfv3area_list -%}
    ADD OSPFV3AREA:
    {#- --- 必选参数 --- -#}
    PROCID={{item.PROCID}},
    AREAID="{{item.AREAID}}",
    {#- --- 可选参数 --- -#}
    {%- if item.AREATYPE is not none -%}
        AREATYPE={{item.AREATYPE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_ospfv3interface_list -%}
    ADD OSPFV3INTERFACE:
    {#- --- 必选参数 --- -#}
    PROCID={{item.PROCID}},
    AREAID="{{item.AREAID}}",
    IFNAME="{{item.IFNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.MTUENABLE is not none -%}
        MTUENABLE={{item.MTUENABLE}},
    {%- endif -%}
    {%- if item.TIMERCONSERFLAG is not none -%}
        TIMERCONSERFLAG={{item.TIMERCONSERFLAG}},
    {%- endif -%}
    {%- if item.BFDENABLE is not none -%}
        BFDENABLE={{item.BFDENABLE}},
    {%- endif -%}
    {%- if item.FRRBINDINGFLAG is not none -%}
        FRRBINDINGFLAG={{item.FRRBINDINGFLAG}},
    {%- endif -%}
    {%- if item.FRRBLOCKFLAG is not none -%}
        FRRBLOCKFLAG={{item.FRRBLOCKFLAG}},
    {%- endif -%}
    {%- if item.BFDBLOCK is not none -%}
        BFDBLOCK={{item.BFDBLOCK}},
    {%- endif -%}
    {%- if item.VIRTUALSYSFLAG is not none -%}
        VIRTUALSYSFLAG={{item.VIRTUALSYSFLAG}},
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_ospfv3importroute_list -%}
    ADD OSPFV3IMPORTROUTE:
    {#- --- 必选参数 --- -#}
    PROCID={{item.PROCID}},
    PROTOCOL={{item.PROTOCOL}},
    {#- --- 可选参数 --- -#}
    {%- if item.IMPTCOSTCFG is not none -%}
        IMPTCOSTCFG={{item.IMPTCOSTCFG}},
    {%- endif -%}
    {%- if item.IMPTTAGCFG is not none -%}
        IMPTTAGCFG={{item.IMPTTAGCFG}},
    {%- endif -%}
    {%- if item.IMPTTYPECFG is not none -%}
        IMPTTYPECFG={{item.IMPTTYPECFG}},
    {%- endif -%}
    {%- if item.INHERITCOSTCFG is not none -%}
        INHERITCOSTCFG={{item.INHERITCOSTCFG}},
    {%- endif -%}
    ;
{%- endfor -%}
```


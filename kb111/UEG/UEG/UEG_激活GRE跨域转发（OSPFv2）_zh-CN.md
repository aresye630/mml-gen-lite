---
id: GWFD-030601
name: 激活GRE跨域转发（OSPFv2）
ne_type: UEG
type: feature
description: 在UEG上基于OSPFv2配置GRE跨域转发功能时，请参考本页面进行操作。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝S","MEC 特性指南（风筝S）","UEG特性指南","网关能力增强","GWFD-030601 GRE跨域转发","激活GRE跨域转发（OSPFv2）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
在UEG上基于OSPFv2配置GRE跨域转发功能时，请参考本页面进行操作。

## 必备事项
前提条件

* 请仔细阅读GWFD-030601 GRE跨域转发特性概述。
* 完成**License****加载**（如果有需求，请联系华为技术支持工程师处理）。
* 已完成园区外UPF，园区内UPF整体网络及业务部署。
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
    add_ifipv4address_list:
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
        IFIPADDR:
          name: '接口IPv4地址'
          type: string
          maxLength: 15
          required: true
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        SUBNETMASK:
          name: '接口IPv4地址掩码'
          type: string
          maxLength: 15
          required: true
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: ''
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
        IFMTU:
          name: '接口最大传输单元（byte）'
          type: integer
          minimum: 46
          maximum: 9600
          required: false
          description: ''
          data_source: ''
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
          description: ''
          data_source: ''
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
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: no_type
        DSTIPADDR:
          name: '目的IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: '-'
          data_source: '与对端协商'
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
        SRCIFNAME:
          name: '源接口名称'
          type: string
          maxLength: 63
          required: false
          description: '已通过**ADD INTERFACE**命令配置。'
          data_source: '已配置数据中获取'
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
    add_ifipv4address_list_2:
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
        IFIPADDR:
          name: '接口IPv4地址'
          type: string
          maxLength: 15
          required: true
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        SUBNETMASK:
          name: '接口IPv4地址掩码'
          type: string
          maxLength: 15
          required: true
          description: '-'
          data_source: '全网规划'
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
          description: '-'
          data_source: '已配置数据中获取'
          pattern: ''
          default: '_public_'
        AFTYPE:
          name: '地址族类型'
          type: string
          enum:
          - ipv4uni
          - ipv6uni
          required: true
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: ''
        NETWORKADDRESS:
          name: 'IPv4路由前缀地址'
          type: string
          maxLength: 15
          required: false
          description: '已通过**ADD IFIPV4ADDRESS**命令配置的LoopBack地址。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        MASKLEN:
          name: 'IPv4掩码长度'
          type: integer
          minimum: 0
          maximum: 32
          required: false
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: ''
    add_ospf_list:
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
          name: '抑制接口收发OSPF报文'
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
        RFC1583COMPFLG:
          name: '兼容RFC1583'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: TRUE
        BANDWIDTHREF:
          name: '计算链路开销参考值（Mbps）'
          type: integer
          minimum: 1
          maximum: 2147483648
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 100
        RXMTLIMITENABLE:
          name: '使能最大重传数'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        OPAQCAPFLG:
          name: 'Opaque LSA能力'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        LSAARRMAXINTV:
          name: '接收最长间隔时间（ms）'
          type: integer
          minimum: 1
          maximum: 10000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 1000
        LSAARRSTARINTV:
          name: '接收初始间隔时间（ms）'
          type: integer
          minimum: 0
          maximum: 1000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 500
        LSAARRHLDINTV:
          name: '接收基数间隔时间（ms）'
          type: integer
          minimum: 1
          maximum: 5000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 500
        LSAARRINTVFLAG:
          name: '取消使用智能定时器配置LSA接收的间隔时间'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        LSAORIGINTV:
          name: '更新时间间隔（s）'
          type: integer
          minimum: 0
          maximum: 10
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 5
        LSAORIGMAXINTV:
          name: '更新最长间隔时间（ms）'
          type: integer
          minimum: 1
          maximum: 10000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 5000
        LSAORIGSTARINTV:
          name: '更新初始间隔时间（ms）'
          type: integer
          minimum: 0
          maximum: 1000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 500
        LSAORIGHLDINTV:
          name: '更新基数间隔时间（ms）'
          type: integer
          minimum: 1
          maximum: 5000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 1000
        LSAORIGINSTFLAG:
          name: '是否指定LSA更新的时间间隔为0'
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
        STUBROUFLG:
          name: 'Stub路由器'
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
        SAFESYNCFLG:
          name: '安全同步'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        SHAMHELLOFLAG:
          name: '使能Sham-hello'
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
        RTTAGDISFLAG:
          name: '禁止使用tag检测环路'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        ECAROUTEFLAG:
          name: '使能ECA路由类型'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
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
        SCHEMAROUID:
          name: '路由器标识'
          type: string
          maxLength: 15
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        SUPPREACH:
          name: '使能可达性抑制'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        SCHEMABFDDETMUL:
          name: 'BFD检测乘数'
          type: integer
          minimum: 3
          maximum: 50
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 3
        SPFCONSERVFLAG:
          name: 'SPF正常模式标志'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        MPLSLDPAUTOCFG:
          name: '是否自动使能MPLS LDP功能'
          type: string
          enum:
          - Enable
          - None
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: None
        VIRTUALSYSFLAG:
          name: 'OSPF共网段虚拟系统使能标志'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: TRUE
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
    add_ospfarea_list:
      type: items
      properties:
        PROCID:
          name: '进程号'
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
          name: '区域类型'
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
        MAXCOSTFLAG:
          name: '保持最大开销值标志'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
    add_ospfinterface_list:
      type: items
      properties:
        PROCID:
          name: '进程号'
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
          description: '已通过**ADD OSPFAREA**命令配置。'
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
        NETWORKTYPE:
          name: '接口网络类型'
          type: string
          enum:
          - broadcast
          - nbma
          - p2mp
          - p2p
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        HOLDDOWNITVL:
          name: '抑制邻居时间间隔（s）'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 10
        FRRBLOCKFLAG:
          name: '阻止指定OSPF接口的FRR能力'
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
    add_ospfimportroute_list:
      type: items
      properties:
        PROCID:
          name: 'OSPF进程号'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TOPOID:
          name: '拓扑标识'
          type: integer
          minimum: 0
          maximum: 0
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 0
        PROTOCOL:
          name: '协议分类'
          type: string
          enum:
          - BGP
          - Direct
          - OSPF
          - Static
          - wlr
          required: true
          description: '将外部路由引入到OSPF域中，并在OSPF域中发布引入的路由信息。'
          data_source: '全网规划'
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
    add_ospfdefaultroute_list:
      type: items
      properties:
        PROCID:
          name: '进程号'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TOPOID:
          name: '拓扑标识'
          type: integer
          minimum: 0
          maximum: 0
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 0
        CONFIGCOST:
          name: '使能度量'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: FALSE
        CONFIGTYPE:
          name: '缺省路由使能类型'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: FALSE
        CONFIGFLAG:
          name: '默认路由发布标志'
          type: string
          enum:
          - Always
          - DefRtAdv
          - Summary
          required: false
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: DefRtAdv
        PERMCALCOTHER:
          name: '计算默认路由'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: FALSE
  examples:
    add_interface_list:
    - IFNAME: 'LoopBack88'
      IFADMINSTATUS: up
    add_ipbindvpn_list:
    - IFNAME: 'LoopBack88'
      VRFNAME: 'VRF_DC12_N9'
    add_ifipv4address_list:
    - IFNAME: 'LoopBack88'
      IFIPADDR: '172.16.12.8'
      SUBNETMASK: '255.255.255.255'
    add_interface_list_2:
    - IFNAME: 'Tunnel66'
      IFMTU: 1500
    add_gretunnel_list:
    - TNLNAME: 'Tunnel66'
      SRCTYPE: if_name
      DSTIPADDR: '172.16.11.8'
      TNLTYPE: gre
      SRCIFNAME: 'LoopBack88'
      DSTVPNNAME: 'VRF_DC11_N9'
      KEEPALVEN: TRUE
      SRCTYPE6: no_type
    add_ipbindvpn_list_2:
    - IFNAME: 'Tunnel66'
      VRFNAME: 'VRF_DC12_N6_local_001'
    add_ifipv4address_list_2:
    - IFNAME: 'Tunnel66'
      IFIPADDR: '172.16.1.1'
      SUBNETMASK: '255.255.255.252'
    add_networkroute_list:
    - VRFNAME: 'VRF_DC12_N9'
      AFTYPE: ipv4uni
      NETWORKADDRESS: '172.16.12.8'
      MASKLEN: 32
    add_ospf_list:
    - PROCID: 66
      VRFNAME: 'VRF_DC12_N6_local_001'
      SILENTALLFLAG: FALSE
      BFDALLINTFFLG: FALSE
      BFDRXCFGFLAG: FALSE
      BFDTXCFGFLAG: FALSE
      RFC1583COMPFLG: TRUE
      BANDWIDTHREF: 100
      RXMTLIMITENABLE: FALSE
      OPAQCAPFLG: FALSE
      LSAARRMAXINTV: 1000
      LSAARRSTARINTV: 500
      LSAARRHLDINTV: 500
      LSAARRINTVFLAG: FALSE
      LSAORIGINTV: 5
      LSAORIGMAXINTV: 5000
      LSAORIGSTARINTV: 500
      LSAORIGHLDINTV: 1000
      LSAORIGINSTFLAG: FALSE
      VPNINSCAPSIMFLG: TRUE
      STUBROUFLG: NoConfig
      SAFESYNCFLG: FALSE
      SHAMHELLOFLAG: FALSE
      ROUTAGFLAG: FALSE
      RTTAGDISFLAG: FALSE
      ECAROUTEFLAG: FALSE
      DOMAINNULLFLAG: FALSE
      SCHEMAROUID: '172.18.1.1'
      SUPPREACH: FALSE
      SCHEMABFDDETMUL: 3
      SPFCONSERVFLAG: FALSE
      MPLSLDPAUTOCFG: None
      VIRTUALSYSFLAG: FALSE
      FRRBINDINGFLAG: FALSE
    add_ospfarea_list:
    - PROCID: 66
      AREAID: '0.0.0.0'
      AREATYPE: Normal
      MAXCOSTFLAG: FALSE
    add_ospfinterface_list:
    - PROCID: 66
      AREAID: '0.0.0.0'
      IFNAME: 'Tunnel66'
      NETWORKTYPE: p2p
      HOLDDOWNITVL: 10
      FRRBLOCKFLAG: FALSE
      FRRBINDINGFLAG: FALSE
      TIMERCONSERFLAG: FALSE
    add_ospfimportroute_list:
    - PROCID: 66
      TOPOID: 0
      PROTOCOL: wlr
      IMPTCOSTCFG: FALSE
      IMPTTAGCFG: FALSE
      IMPTTYPECFG: FALSE
    add_ospfdefaultroute_list:
    - PROCID: 66
      TOPOID: 0
      CONFIGCOST: FALSE
      CONFIGTYPE: FALSE
      CONFIGFLAG: DefRtAdv
      PERMCALCOTHER: FALSE
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

### 2 配置GRE Tunnel。

```jinja2
{%- for item in add_interface_list_2 -%}
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
{%- for item in add_ipbindvpn_list_2 -%}
    ADD IPBINDVPN:
    {#- --- 必选参数 --- -#}
    IFNAME="{{item.IFNAME}}",
    VRFNAME="{{item.VRFNAME}}",
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_ifipv4address_list_2 -%}
    ADD IFIPV4ADDRESS:
    {#- --- 必选参数 --- -#}
    IFNAME="{{item.IFNAME}}",
    IFIPADDR="{{item.IFIPADDR}}",
    SUBNETMASK="{{item.SUBNETMASK}}",
    ;
{%- endfor -%}
```

### 3 配置发布LoopBack路由。

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

### 4 配置OSPF。

```jinja2
{%- for item in add_ospf_list -%}
    ADD OSPF:
    {#- --- 必选参数 --- -#}
    PROCID={{item.PROCID}},
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
    {%- if item.RFC1583COMPFLG is not none -%}
        RFC1583COMPFLG={{item.RFC1583COMPFLG}},
    {%- endif -%}
    {%- if item.BANDWIDTHREF is not none -%}
        BANDWIDTHREF={{item.BANDWIDTHREF}},
    {%- endif -%}
    {%- if item.RXMTLIMITENABLE is not none -%}
        RXMTLIMITENABLE={{item.RXMTLIMITENABLE}},
    {%- endif -%}
    {%- if item.OPAQCAPFLG is not none -%}
        OPAQCAPFLG={{item.OPAQCAPFLG}},
    {%- endif -%}
    {%- if item.LSAARRINTVFLAG is not none -%}
        LSAARRINTVFLAG={{item.LSAARRINTVFLAG}},
    {%- endif -%}
    {%- if item.LSAORIGINSTFLAG is not none -%}
        LSAORIGINSTFLAG={{item.LSAORIGINSTFLAG}},
    {%- endif -%}
    {%- if item.VPNINSCAPSIMFLG is not none -%}
        VPNINSCAPSIMFLG={{item.VPNINSCAPSIMFLG}},
    {%- endif -%}
    {%- if item.STUBROUFLG is not none -%}
        STUBROUFLG={{item.STUBROUFLG}},
    {%- endif -%}
    {%- if item.SAFESYNCFLG is not none -%}
        SAFESYNCFLG={{item.SAFESYNCFLG}},
    {%- endif -%}
    {%- if item.SHAMHELLOFLAG is not none -%}
        SHAMHELLOFLAG={{item.SHAMHELLOFLAG}},
    {%- endif -%}
    {%- if item.ROUTAGFLAG is not none -%}
        ROUTAGFLAG={{item.ROUTAGFLAG}},
    {%- endif -%}
    {%- if item.RTTAGDISFLAG is not none -%}
        RTTAGDISFLAG={{item.RTTAGDISFLAG}},
    {%- endif -%}
    {%- if item.ECAROUTEFLAG is not none -%}
        ECAROUTEFLAG={{item.ECAROUTEFLAG}},
    {%- endif -%}
    {%- if item.DOMAINNULLFLAG is not none -%}
        DOMAINNULLFLAG={{item.DOMAINNULLFLAG}},
    {%- endif -%}
    {%- if item.SCHEMAROUID is not none -%}
        SCHEMAROUID="{{item.SCHEMAROUID}}",
    {%- endif -%}
    {%- if item.SUPPREACH is not none -%}
        SUPPREACH={{item.SUPPREACH}},
    {%- endif -%}
    {%- if item.SCHEMABFDDETMUL is not none -%}
        SCHEMABFDDETMUL={{item.SCHEMABFDDETMUL}},
    {%- endif -%}
    {%- if item.SPFCONSERVFLAG is not none -%}
        SPFCONSERVFLAG={{item.SPFCONSERVFLAG}},
    {%- endif -%}
    {%- if item.MPLSLDPAUTOCFG is not none -%}
        MPLSLDPAUTOCFG={{item.MPLSLDPAUTOCFG}},
    {%- endif -%}
    {%- if item.VIRTUALSYSFLAG is not none -%}
        VIRTUALSYSFLAG={{item.VIRTUALSYSFLAG}},
    {%- endif -%}
    {%- if item.FRRBINDINGFLAG is not none -%}
        FRRBINDINGFLAG={{item.FRRBINDINGFLAG}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：LSAARRINTVFLAG=FALSE 时必选 --- -#}
    {%- if item.LSAARRINTVFLAG == 'FALSE' -%}
        LSAARRMAXINTV={{item.LSAARRMAXINTV}},
    {%- endif -%}
    {#- --- 条件必选：LSAARRINTVFLAG=FALSE 时必选 --- -#}
    {%- if item.LSAARRINTVFLAG == 'FALSE' -%}
        LSAARRSTARINTV={{item.LSAARRSTARINTV}},
    {%- endif -%}
    {#- --- 条件必选：LSAARRINTVFLAG=FALSE 时必选 --- -#}
    {%- if item.LSAARRINTVFLAG == 'FALSE' -%}
        LSAARRHLDINTV={{item.LSAARRHLDINTV}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：LSAORIGINSTFLAG=FALSE 时可选 --- -#}
    {%- if item.LSAORIGINSTFLAG == 'FALSE' -%}
        {%- if item.LSAORIGINTV is not none -%}
            LSAORIGINTV={{item.LSAORIGINTV}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：LSAORIGINSTFLAG=FALSE 时可选 --- -#}
    {%- if item.LSAORIGINSTFLAG == 'FALSE' -%}
        {%- if item.LSAORIGMAXINTV is not none -%}
            LSAORIGMAXINTV={{item.LSAORIGMAXINTV}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：LSAORIGINSTFLAG=FALSE 时可选 --- -#}
    {%- if item.LSAORIGINSTFLAG == 'FALSE' -%}
        {%- if item.LSAORIGSTARINTV is not none -%}
            LSAORIGSTARINTV={{item.LSAORIGSTARINTV}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：LSAORIGINSTFLAG=FALSE 时可选 --- -#}
    {%- if item.LSAORIGINSTFLAG == 'FALSE' -%}
        {%- if item.LSAORIGHLDINTV is not none -%}
            LSAORIGHLDINTV={{item.LSAORIGHLDINTV}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_ospfarea_list -%}
    ADD OSPFAREA:
    {#- --- 必选参数 --- -#}
    PROCID={{item.PROCID}},
    AREAID="{{item.AREAID}}",
    {#- --- 可选参数 --- -#}
    {%- if item.AREATYPE is not none -%}
        AREATYPE={{item.AREATYPE}},
    {%- endif -%}
    {%- if item.MAXCOSTFLAG is not none -%}
        MAXCOSTFLAG={{item.MAXCOSTFLAG}},
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_ospfinterface_list -%}
    ADD OSPFINTERFACE:
    {#- --- 必选参数 --- -#}
    PROCID={{item.PROCID}},
    AREAID="{{item.AREAID}}",
    IFNAME="{{item.IFNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.NETWORKTYPE is not none -%}
        NETWORKTYPE={{item.NETWORKTYPE}},
    {%- endif -%}
    {%- if item.HOLDDOWNITVL is not none -%}
        HOLDDOWNITVL={{item.HOLDDOWNITVL}},
    {%- endif -%}
    {%- if item.FRRBLOCKFLAG is not none -%}
        FRRBLOCKFLAG={{item.FRRBLOCKFLAG}},
    {%- endif -%}
    {%- if item.FRRBINDINGFLAG is not none -%}
        FRRBINDINGFLAG={{item.FRRBINDINGFLAG}},
    {%- endif -%}
    {%- if item.TIMERCONSERFLAG is not none -%}
        TIMERCONSERFLAG={{item.TIMERCONSERFLAG}},
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_ospfimportroute_list -%}
    ADD OSPFIMPORTROUTE:
    {#- --- 必选参数 --- -#}
    PROCID={{item.PROCID}},
    PROTOCOL={{item.PROTOCOL}},
    {#- --- 可选参数 --- -#}
    {%- if item.TOPOID is not none -%}
        TOPOID={{item.TOPOID}},
    {%- endif -%}
    {%- if item.IMPTCOSTCFG is not none -%}
        IMPTCOSTCFG={{item.IMPTCOSTCFG}},
    {%- endif -%}
    {%- if item.IMPTTAGCFG is not none -%}
        IMPTTAGCFG={{item.IMPTTAGCFG}},
    {%- endif -%}
    {%- if item.IMPTTYPECFG is not none -%}
        IMPTTYPECFG={{item.IMPTTYPECFG}},
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_ospfdefaultroute_list -%}
    ADD OSPFDEFAULTROUTE:
    {#- --- 必选参数 --- -#}
    PROCID={{item.PROCID}},
    {#- --- 可选参数 --- -#}
    {%- if item.TOPOID is not none -%}
        TOPOID={{item.TOPOID}},
    {%- endif -%}
    {%- if item.CONFIGCOST is not none -%}
        CONFIGCOST={{item.CONFIGCOST}},
    {%- endif -%}
    {%- if item.CONFIGTYPE is not none -%}
        CONFIGTYPE={{item.CONFIGTYPE}},
    {%- endif -%}
    {%- if item.CONFIGFLAG is not none -%}
        CONFIGFLAG={{item.CONFIGFLAG}},
    {%- endif -%}
    {%- if item.PERMCALCOTHER is not none -%}
        PERMCALCOTHER={{item.PERMCALCOTHER}},
    {%- endif -%}
    ;
{%- endfor -%}
```


---
id: ''
name: NP卡+DCGW
ne_type: UEG
type: feature
description: 新增企业，开通业务时，UPF到园区采用VPN专线，UPF使用NP卡，对接DCGW。对于容灾的两个UPF而言，此配置没有区别，仅以一个UPF做配置举例，组网规划如图1。  **图1** NP卡+DCGW规划示意图
tags: []
risk_level: ''
doc_source:
  - ["专网（仅连接，园区入驻式）","业务发放","5GC toB DNN业务发放（专网，入驻式）","通过OMC发放","UEG虚机容器","DNN发放操作","发放入驻式UPF+VPN专线","入驻式UPF+VPN专线+分流UPF（跨级）+主备+动态分配地址（与分流UPF容灾）","配置数据","配置UPF数据","配置VPN专线数据","NP卡+DCGW"]
  - ["云网（连接+计算，入驻式或共享式）","业务发放","5GC toB DNN业务发放（云网，带计算）","通过OMC发放","DNN发放操作","发放入驻式UPF+VPN专线","入驻式UPF+VPN专线+分流UPF（跨级）+主备+动态分配地址（与分流UPF容灾）","配置数据","配置UPF数据","配置VPN专线数据","NP卡+DCGW"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
新增企业，开通业务时，UPF到园区采用VPN专线，UPF使用NP卡，对接DCGW。对于容灾的两个UPF而言，此配置没有区别，仅以一个UPF做配置举例，组网规划如图1。**图1** NP卡+DCGW规划示意图

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
          description: '全局激活BFD。'
          data_source: '本端规划'
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
    mod_vpninstaf_list:
      type: items
      properties:
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: true
          description: ''
          data_source: ''
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
          data_source: ''
          pattern: ''
          default: ''
        VRFRD:
          name: '路由标识'
          type: string
          maxLength: 21
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_vpninstaf_list_1:
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
    mod_vpninstaf_list_1:
      type: items
      properties:
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: true
          description: ''
          data_source: ''
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
          data_source: ''
          pattern: ''
          default: ''
        VRFRD:
          name: '路由标识'
          type: string
          maxLength: 21
          required: false
          description: ''
          data_source: ''
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
          description: '配置主接口的管理状态为up。'
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
          description: '配置Eth-trunk接口。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    mod_trunkif_list:
      type: items
      properties:
        IFNAME:
          name: '接口名称'
          type: string
          maxLength: 63
          required: true
          description: '当前本端工作模式为LACP的Eth-trunk接口仅支持passive模式，因此要求对接DC-GW/PE的Eth-trunk接口必须为active模式。即要求对接DC-GW/PE上的端口主动发送LACP报文。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        WORKMODE:
          name: '工作模式'
          type: string
          enum:
          - Lacp
          - Manual
          - MultiBackup
          required: true
          description: ''
          data_source: '固定值'
          pattern: ''
          default: ''
        LEASTACTLINKNUM:
          name: '最小激活链路数'
          type: integer
          minimum: 1
          maximum: 64
          required: false
          description: ''
          data_source: '与对端协商'
          pattern: ''
          default: ''
    add_trunkmember_list:
      type: items
      properties:
        TRUNKIFNAME:
          name: 'Trunk接口名'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        MEMBERIFNAME:
          name: '成员接口名'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: '已规划数据中获取'
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
          description: '配置Eth-trunk接口。'
          data_source: '本端规划'
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
          description: '配置IPv4静态路由数据。'
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
          data_source: ''
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
          data_source: '全网规划'
          pattern: ''
          default: ''
        NEXTHOP:
          name: '路由下一跳'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        SESSIONNAME:
          name: '静态BFD会话名'
          type: string
          maxLength: 64
          required: false
          description: ''
          data_source: '从已配置数据中获取'
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
          description: '配置IPv6静态路由数据。'
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
          name: '路由前缀长度'
          type: integer
          minimum: 0
          maximum: 128
          required: true
          description: ''
          data_source: ''
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
          data_source: '全网规划'
          pattern: ''
          default: ''
        NEXTHOP:
          name: '路由下一跳'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        SESSIONNAME:
          name: '静态BFD会话名'
          type: string
          maxLength: 64
          required: false
          description: ''
          data_source: '从已配置数据中获取'
          pattern: ''
          default: ''
    add_interface_list_4:
      type: items
      properties:
        IFNAME:
          name: '接口名'
          type: string
          maxLength: 63
          required: true
          description: '添加LoopBack接口。'
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
        IFSTATIENABLE:
          name: '接口统计使能标记'
          type: string
          enum:
          - FALSE
          - NONE
          - TRUE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IFTRAPENABLE:
          name: '接口Trap使能标记'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
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
    add_ipbindvpn_list_2:
      type: items
      properties:
        IFNAME:
          name: '接口名'
          type: string
          maxLength: 63
          required: true
          description: ''
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
    add_interface_list_5:
      type: items
      properties:
        IFNAME:
          name: '接口名'
          type: string
          maxLength: 63
          required: true
          description: '添加LoopBack接口。'
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
        IFSTATIENABLE:
          name: '接口统计使能标记'
          type: string
          enum:
          - FALSE
          - NONE
          - TRUE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IFTRAPENABLE:
          name: '接口Trap使能标记'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_ipbindvpn_list_3:
      type: items
      properties:
        IFNAME:
          name: '接口名'
          type: string
          maxLength: 63
          required: true
          description: ''
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
    set_ifipv6enable_list_2:
      type: items
      properties:
        IFNAME:
          name: '接口名'
          type: string
          maxLength: 63
          required: true
          description: ''
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
    add_ifipv6address_list_2:
      type: items
      properties:
        IFNAME:
          name: '接口名'
          type: string
          maxLength: 63
          required: true
          description: ''
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
    set_bgp_list:
      type: items
      properties:
        BGPENABLE:
          name: '使能BGP'
          type: string
          enum:
          - FALSE
          - TRUE
          required: true
          description: '设置BGP。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        ASNUM:
          name: 'BGP自治域号'
          type: string
          maxLength: 11
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_bgpvrf_list:
      type: items
      properties:
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: true
          description: '配置BGP VPN。'
          data_source: '从已配置数据中获取'
          pattern: ''
          default: ''
        DEFAULTAFTYPE:
          name: '默认地址族'
          type: string
          enum:
          - ipv4uni
          - ipv6uni
          - noaf
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ipv4uni
        ROUTERID:
          name: '路由器ID'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_bgpvrfaf_list:
      type: items
      properties:
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: false
          description: '增加BGP VPN地址族。'
          data_source: '从已配置数据中获取'
          pattern: ''
          default: '_public_'
        AFTYPE:
          name: '地址族类型'
          type: string
          enum:
          - ipv4uni
          - ipv4vpn
          - ipv6uni
          - ipv6vpn
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        MAXLOADEBGPNUM:
          name: 'EBGP负载分担数'
          type: integer
          minimum: 1
          maximum: 128
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 1
    add_importroute_list:
      type: items
      properties:
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: false
          description: '增加BGP引入路由。'
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
          data_source: '全网规划'
          pattern: ''
          default: ''
        IMPORTPROTOCOL:
          name: '路由协议'
          type: string
          enum:
          - direct
          - ospf
          - ospfv3
          - static
          - wlr
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        MEDENABLE:
          name: '使能MED'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: '* 当两个UPF负荷分担场景下，无需配置这两个参数。 * 当静态地址路由冗余场景下，主备两个UPF的路由配置不同的优先级，值越小优先级越高。'
          data_source: '本端规划'
          pattern: ''
          default: FALSE
        MED:
          name: 'MED'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: 0
    add_importroute_list_2:
      type: items
      properties:
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: false
          description: '增加BGP引入路由。'
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
          data_source: '全网规划'
          pattern: ''
          default: ''
        IMPORTPROTOCOL:
          name: '路由协议'
          type: string
          enum:
          - direct
          - ospf
          - ospfv3
          - static
          - wlr
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        MEDENABLE:
          name: '使能MED'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: '* 当两个UPF负荷分担场景下，无需配置这两个参数。 * 当静态地址路由冗余场景下，主备两个UPF的路由配置不同的优先级，值越小优先级越高。'
          data_source: '本端规划'
          pattern: ''
          default: FALSE
        MED:
          name: 'MED'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: 0
    add_bgppeer_list:
      type: items
      properties:
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: false
          description: '增加BGP对等体。'
          data_source: '从已配置数据中获取'
          pattern: ''
          default: '_public_'
        ADDRESSTYPE:
          name: '地址类型'
          type: string
          enum:
          - ipv4
          - ipv6
          - noaf
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ipv4
        PEERADDR:
          name: 'IPv4对等体地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        REMOTEAS:
          name: '对等体AS号'
          type: string
          maxLength: 11
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        LOCALIFADDR:
          name: '本地接口地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        LOCALIFNAME:
          name: '本地接口名称'
          type: string
          maxLength: 63
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        EBGPMAXHOP:
          name: 'EBGP最大跳数'
          type: integer
          minimum: 1
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CONNECTMODE:
          name: '连接模式'
          type: string
          enum:
          - connectOnly
          - listenOnly
          - 'null'
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'null'
        PSWDTYPE:
          name: '密码类型'
          type: string
          enum:
          - cipher
          - 'null'
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'null'
        PEERADDRV6:
          name: 'IPv6对等体地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: '全网规划'
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
    mod_vpninstaf_list:
    - VRFNAME: 'VRF_N6_Local_2B_001'
      AFTYPE: ipv4uni
      VRFRD: '172.20.9.4:100'
    add_vpninstaf_list_1:
    - VRFNAME: 'VRF_N6_Local_2B_001'
      AFTYPE: ipv6uni
    mod_vpninstaf_list_1:
    - VRFNAME: 'VRF_N6_Local_2B_001'
      AFTYPE: ipv6uni
      VRFRD: '172.20.9.4:100'
    mod_interface_list:
    - IFNAME: '100GE65/0/9'
      IFADMINSTATUS: up
    add_interface_list:
    - IFNAME: 'Eth-trunk65'
    mod_trunkif_list:
    - IFNAME: 'Eth-Trunk65'
      WORKMODE: Lacp
      LEASTACTLINKNUM: 1
    add_trunkmember_list:
    - TRUNKIFNAME: 'Eth-trunk65'
      MEMBERIFNAME: '100GE65/0/9'
    add_interface_list_2:
    - IFNAME: 'Eth-trunk65.2003'
    add_ipbindvpn_list:
    - IFNAME: 'Eth-trunk65.2003'
      VRFNAME: 'VRF_N6_Local_2B_001'
    add_ethsubif_list:
    - IFNAME: 'Eth-trunk65.2003'
      SUBIFTYPE: VlanType
      VLANTYPEVID: 2003
    add_ifipv4address_list:
    - IFNAME: 'Eth-trunk65.2003'
      IFIPADDR: '192.168.246.130'
      SUBNETMASK: '255.255.255.224'
      ADDRTYPE: main
    set_ifipv6enable_list:
    - IFNAME: 'Eth-trunk65.2003'
      ENABLEFLAG: TRUE
    add_ifipv6address_list:
    - IFNAME: 'Eth-trunk65.2003'
      IPV6ADDRESS: 'fc00:8028:5000:43::9542'
      PREFIXLEN: 123
      ADDRTYPE: global
    add_bfdsession_list:
    - SESSNAME: 'N6if_2003_1'
      ADDRTYPE: IPv4
      CREATETYPE4: SESS_STATIC
      ONEARMECHO: TRUE
      DESTADDR4: '192.168.11.11'
      LINKTYPE: IP
      DETECTMULTI: 4
      VRFNAME: 'VRF_N6_Local_2B_001'
      MINECHORXINT: 500
      LOCALDISCR: 322
      IFNAME: 'Eth-trunk65.2003'
      CREATETYPE6: '-'
      ONEARMECHO6: '-'
      DESTADDR6: '-'
    add_srroute_list:
    - AFTYPE: ipv4unicast
      PREFIX: '192.168.11.1'
      MASKLENGTH: 32
      VRFNAME: 'VRF_N6_Local_2B_001'
      DESTVRFNAME: 'VRF_N6_Local_2B_001'
      IFNAME: 'Eth-trunk65.2003'
      NEXTHOP: '192.168.11.11'
      SESSIONNAME: 'N6if_2003_1'
    add_srroute6_list:
    - AFTYPE: ipv6unicast
      PREFIX: 'fc00:187:C289::1'
      MASKLENGTH: 128
      VRFNAME: 'VRF_N6_Local_2B_001'
      DESTVRFNAME: 'VRF_N6_Local_2B_001'
      IFNAME: 'Eth-trunk65.2003'
      NEXTHOP: 'fc00:187:C28C::1'
      SESSIONNAME: 'N6if_IPv6_1'
    add_interface_list_4:
    - IFNAME: 'LoopBack14'
      IFADMINSTATUS: up
      IFMTU: 1500
      IFDF: FALSE
      IFSTATIENABLE: TRUE
      IFTRAPENABLE: TRUE
    add_ifipv4address_list_2:
    - IFNAME: 'LoopBack14'
      IFIPADDR: '172.20.9.7'
      SUBNETMASK: '255.255.255.255'
      ADDRTYPE: main
    add_ipbindvpn_list_2:
    - IFNAME: 'LoopBack14'
      VRFNAME: 'VRF_N6_Local_2B_001'
    add_interface_list_5:
    - IFNAME: 'LoopBack13'
      IFADMINSTATUS: up
      IFMTU: 1500
      IFDF: FALSE
      IFSTATIENABLE: TRUE
      IFTRAPENABLE: TRUE
    add_ipbindvpn_list_3:
    - IFNAME: 'LoopBack13'
      VRFNAME: 'VRF_N6_Local_2B_001'
    set_ifipv6enable_list_2:
    - IFNAME: 'Loopback13'
      ENABLEFLAG: TRUE
    add_ifipv6address_list_2:
    - IFNAME: 'Loopback13'
      IPV6ADDRESS: 'fc00:187:C281::1'
      PREFIXLEN: 128
    set_bgp_list:
    - BGPENABLE: TRUE
      ASNUM: '64986'
    add_bgpvrf_list:
    - VRFNAME: 'VRF_N6_Local_2B_001'
      DEFAULTAFTYPE: noaf
      ROUTERID: '172.20.7.2'
    add_bgpvrfaf_list:
    - VRFNAME: 'VRF_N6_Local_2B_001'
      AFTYPE: ipv4uni
      MAXLOADEBGPNUM: 2
    add_importroute_list:
    - VRFNAME: 'VRF_N6_Local_2B_001'
      AFTYPE: ipv4uni
      IMPORTPROTOCOL: wlr
      MEDENABLE: TRUE
      MED: 0
    add_importroute_list_2:
    - VRFNAME: 'VRF_N6_Local_2B_001'
      AFTYPE: ipv4uni
      IMPORTPROTOCOL: wlr
      MEDENABLE: TRUE
      MED: 0
    add_bgppeer_list:
    - VRFNAME: 'VRF_N6_Local_2B_001'
      ADDRESSTYPE: ipv4
      PEERADDR: '192.168.11.1'
      REMOTEAS: '64813'
      LOCALIFADDR: '172.20.9.7'
      LOCALIFNAME: 'LoopBack14'
      EBGPMAXHOP: 2
      CONNECTMODE: 'null'
      PSWDTYPE: 'null'
      PEERADDRV6: 'fc00:187:C289::1'
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

```jinja2
{%- for item in add_vpninstaf_list_1 -%}
    ADD VPNINSTAF:
    {#- --- 必选参数 --- -#}
    VRFNAME="{{item.VRFNAME}}",
    AFTYPE={{item.AFTYPE}},
    ;
{%- endfor -%}
```

```jinja2
{%- for item in mod_vpninstaf_list_1 -%}
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

### 4 配置Eth-trunk接口。

```jinja2
{%- for item in add_interface_list -%}
    ADD INTERFACE:
    {#- --- 必选参数 --- -#}
    IFNAME="{{item.IFNAME}}",
    ;
{%- endfor -%}
```

### 5 配置Eth-trunk接口的工作模式并添加成员端口。

```jinja2
{%- for item in mod_trunkif_list -%}
    MOD TRUNKIF:
    {#- --- 必选参数 --- -#}
    IFNAME="{{item.IFNAME}}",
    WORKMODE={{item.WORKMODE}},
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：WORKMODE=Lacp/Manual 时可选 --- -#}
    {%- if item.WORKMODE in ['Lacp', 'Manual'] -%}
        {%- if item.LEASTACTLINKNUM is not none -%}
            LEASTACTLINKNUM={{item.LEASTACTLINKNUM}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_trunkmember_list -%}
    ADD TRUNKMEMBER:
    {#- --- 必选参数 --- -#}
    TRUNKIFNAME="{{item.TRUNKIFNAME}}",
    MEMBERIFNAME="{{item.MEMBERIFNAME}}",
    ;
{%- endfor -%}
```

### 6 配置以太Trunk子接口。

```jinja2
{%- for item in add_interface_list_2 -%}
    ADD INTERFACE:
    {#- --- 必选参数 --- -#}
    IFNAME="{{item.IFNAME}}",
    ;
{%- endfor -%}
```

### 7 接口绑定VPN。

```jinja2
{%- for item in add_ipbindvpn_list -%}
    ADD IPBINDVPN:
    {#- --- 必选参数 --- -#}
    IFNAME="{{item.IFNAME}}",
    VRFNAME="{{item.VRFNAME}}",
    ;
{%- endfor -%}
```

### 8 在以太网Trunk子接口上关联VLAN ID。

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

### 9 配置外联口IPv4地址。

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

### 10 配置IPv6使能。

```jinja2
{%- for item in set_ifipv6enable_list -%}
    SET IFIPV6ENABLE:
    {#- --- 必选参数 --- -#}
    IFNAME="{{item.IFNAME}}",
    ENABLEFLAG={{item.ENABLEFLAG}},
    ;
{%- endfor -%}
```

### 11 配置外联口IPv6地址。

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

### 12 新建静态BFD会话。

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

### 13 配置静态路由数据。

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

### 14 添加LoopBack接口。

```jinja2
{%- for item in add_interface_list_4 -%}
    ADD INTERFACE:
    {#- --- 必选参数 --- -#}
    IFNAME="{{item.IFNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.IFADMINSTATUS is not none -%}
        IFADMINSTATUS={{item.IFADMINSTATUS}},
    {%- endif -%}
    {%- if item.IFMTU is not none -%}
        IFMTU={{item.IFMTU}},
    {%- endif -%}
    {%- if item.IFDF is not none -%}
        IFDF={{item.IFDF}},
    {%- endif -%}
    {%- if item.IFSTATIENABLE is not none -%}
        IFSTATIENABLE={{item.IFSTATIENABLE}},
    {%- endif -%}
    {%- if item.IFTRAPENABLE is not none -%}
        IFTRAPENABLE={{item.IFTRAPENABLE}},
    {%- endif -%}
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
    {#- --- 可选参数 --- -#}
    {%- if item.ADDRTYPE is not none -%}
        ADDRTYPE={{item.ADDRTYPE}},
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
{%- for item in add_interface_list_5 -%}
    ADD INTERFACE:
    {#- --- 必选参数 --- -#}
    IFNAME="{{item.IFNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.IFADMINSTATUS is not none -%}
        IFADMINSTATUS={{item.IFADMINSTATUS}},
    {%- endif -%}
    {%- if item.IFMTU is not none -%}
        IFMTU={{item.IFMTU}},
    {%- endif -%}
    {%- if item.IFDF is not none -%}
        IFDF={{item.IFDF}},
    {%- endif -%}
    {%- if item.IFSTATIENABLE is not none -%}
        IFSTATIENABLE={{item.IFSTATIENABLE}},
    {%- endif -%}
    {%- if item.IFTRAPENABLE is not none -%}
        IFTRAPENABLE={{item.IFTRAPENABLE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_ipbindvpn_list_3 -%}
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
    ;
{%- endfor -%}
```

### 15 设置BGP。

```jinja2
{%- for item in set_bgp_list -%}
    SET BGP:
    {#- --- 必选参数 --- -#}
    BGPENABLE={{item.BGPENABLE}},
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：BGPENABLE=TRUE 时可选 --- -#}
    {%- if item.BGPENABLE == 'TRUE' -%}
        {%- if item.ASNUM is not none -%}
            ASNUM="{{item.ASNUM}}",
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 16 添加BGP VPN。

```jinja2
{%- for item in add_bgpvrf_list -%}
    ADD BGPVRF:
    {#- --- 必选参数 --- -#}
    VRFNAME="{{item.VRFNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.DEFAULTAFTYPE is not none -%}
        DEFAULTAFTYPE={{item.DEFAULTAFTYPE}},
    {%- endif -%}
    {%- if item.ROUTERID is not none -%}
        ROUTERID="{{item.ROUTERID}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 17 增加BGP VPN地址族。

```jinja2
{%- for item in add_bgpvrfaf_list -%}
    ADD BGPVRFAF:
    {#- --- 必选参数 --- -#}
    AFTYPE={{item.AFTYPE}},
    {#- --- 可选参数 --- -#}
    {%- if item.VRFNAME is not none -%}
        VRFNAME="{{item.VRFNAME}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：AFTYPE=ipv4uni/ipv6uni 时可选 --- -#}
    {%- if item.AFTYPE in ['ipv4uni', 'ipv6uni'] -%}
        {%- if item.MAXLOADEBGPNUM is not none -%}
            MAXLOADEBGPNUM={{item.MAXLOADEBGPNUM}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 18 （负荷分担UPF场景下）配置BGP引入wlr路由。

```jinja2
{%- if is_scenario_load_sharing_upf -%}
    {%- for item in add_importroute_list -%}
        ADD IMPORTROUTE:
        {#- --- 必选参数 --- -#}
        AFTYPE={{item.AFTYPE}},
        IMPORTPROTOCOL={{item.IMPORTPROTOCOL}},
        {#- --- 可选参数 --- -#}
        {%- if item.VRFNAME is not none -%}
            VRFNAME="{{item.VRFNAME}}",
        {%- endif -%}
        {%- if item.MEDENABLE is not none -%}
            MEDENABLE={{item.MEDENABLE}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：MEDENABLE=TRUE 时必选 --- -#}
        {%- if item.MEDENABLE == 'TRUE' -%}
            MED={{item.MED}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 19 （GRE路由冗余隧道场景下）配置BGP引入wlr路由。

```jinja2
{%- if is_scenario_gre_route_redundant_tunnel -%}
    {%- for item in add_importroute_list_2 -%}
        ADD IMPORTROUTE:
        {#- --- 必选参数 --- -#}
        AFTYPE={{item.AFTYPE}},
        IMPORTPROTOCOL={{item.IMPORTPROTOCOL}},
        {#- --- 可选参数 --- -#}
        {%- if item.VRFNAME is not none -%}
            VRFNAME="{{item.VRFNAME}}",
        {%- endif -%}
        {%- if item.MEDENABLE is not none -%}
            MEDENABLE={{item.MEDENABLE}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：MEDENABLE=TRUE 时必选 --- -#}
        {%- if item.MEDENABLE == 'TRUE' -%}
            MED={{item.MED}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 20 增加BGP对等体。

```jinja2
{%- for item in add_bgppeer_list -%}
    ADD BGPPEER:
    {#- --- 可选参数 --- -#}
    {%- if item.VRFNAME is not none -%}
        VRFNAME="{{item.VRFNAME}}",
    {%- endif -%}
    {%- if item.ADDRESSTYPE is not none -%}
        ADDRESSTYPE={{item.ADDRESSTYPE}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：ADDRESSTYPE=noaf/ipv4 时必选 --- -#}
    {%- if item.ADDRESSTYPE in ['noaf', 'ipv4'] -%}
        PEERADDR="{{item.PEERADDR}}",
    {%- endif -%}
    {#- --- 条件必选：ADDRESSTYPE=ipv6 时必选 --- -#}
    {%- if item.ADDRESSTYPE == 'ipv6' -%}
        PEERADDRV6="{{item.PEERADDRV6}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：ADDRESSTYPE=noaf/ipv4/ipv6 时可选 --- -#}
    {%- if item.ADDRESSTYPE in ['noaf', 'ipv4', 'ipv6'] -%}
        {%- if item.REMOTEAS is not none -%}
            REMOTEAS="{{item.REMOTEAS}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：ADDRESSTYPE=noaf/ipv4/ipv6 时可选 --- -#}
    {%- if item.ADDRESSTYPE in ['noaf', 'ipv4', 'ipv6'] -%}
        {%- if item.LOCALIFADDR is not none -%}
            LOCALIFADDR="{{item.LOCALIFADDR}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：ADDRESSTYPE=noaf/ipv4/ipv6 时可选 --- -#}
    {%- if item.ADDRESSTYPE in ['noaf', 'ipv4', 'ipv6'] -%}
        {%- if item.LOCALIFNAME is not none -%}
            LOCALIFNAME="{{item.LOCALIFNAME}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：ADDRESSTYPE=noaf/ipv4/ipv6 时可选 --- -#}
    {%- if item.ADDRESSTYPE in ['noaf', 'ipv4', 'ipv6'] -%}
        {%- if item.EBGPMAXHOP is not none -%}
            EBGPMAXHOP={{item.EBGPMAXHOP}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：ADDRESSTYPE=noaf/ipv4/ipv6 时可选 --- -#}
    {%- if item.ADDRESSTYPE in ['noaf', 'ipv4', 'ipv6'] -%}
        {%- if item.CONNECTMODE is not none -%}
            CONNECTMODE={{item.CONNECTMODE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：ADDRESSTYPE=noaf/ipv4/ipv6 时可选 --- -#}
    {%- if item.ADDRESSTYPE in ['noaf', 'ipv4', 'ipv6'] -%}
        {%- if item.PSWDTYPE is not none -%}
            PSWDTYPE={{item.PSWDTYPE}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```


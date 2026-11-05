---
id: ''
name: 配置组网路由（DCGW）
ne_type: UEG
type: feature
description: UEG-L部署在总部园区，作为SMF/GW-C/MME需要对接子园区UEG-S的UPF/GW-U。UEG-L对接DCGW（路由器）或DCGW（交换机）。DCGW之间使用E-Trunk+EVPN或M-LAG组网，UEG使用Eth-trunk接口，一个Eth-trunk接口的成员端口，连接到同一台DCGW上。  UEG-L通过BGP over静态路由+BFD单臂echo与对端网元（UPF/GW-U）实现网络互通，组网规划如图1所示。  对于容灾的两个UEG-L而言，此配置没有区别，仅以一个UEG-L做配置举例。  **图1** DCGW（路由器/交换机）规划示意图
tags: []
risk_level: ''
doc_source: ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（火电专网，入驻式）","配置园区之间对接","配置中心园区UEG-L与子园区UEG-S对接","方案配置","在UEG-L配置与UEG-S对接（UEG-L虚机）","子园区UPF主备热备容灾","配置组网路由（DCGW）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
UEG-L部署在总部园区，作为SMF/GW-C/MME需要对接子园区UEG-S的UPF/GW-U。UEG-L对接DCGW（路由器）或DCGW（交换机）。DCGW之间使用E-Trunk+EVPN或M-LAG组网，UEG使用Eth-trunk接口，一个Eth-trunk接口的成员端口，连接到同一台DCGW上。UEG-L通过BGP over静态路由+BFD单臂echo与对端网元（UPF/GW-U）实现网络互通，组网规划如图1所示。对于容灾的两个UEG-L而言，此配置没有区别，仅以一个UEG-L做配置举例。**图1** DCGW（路由器/交换机）规划示意图

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
    set_autoconfig_list:
      type: items
      properties:
        SWITCHFLAG:
          name: '自动配置开关'
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
        VRFRD:
          name: '路由标识'
          type: string
          maxLength: 21
          required: false
          description: ''
          data_source: ''
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
          description: '添加LoopBack接口。'
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
    add_ipbindvpn_list:
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
    add_ifipv4address_list:
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
    add_interface_list_1:
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
    add_ipbindvpn_list_1:
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
    set_ifipv6enable_list:
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
    add_ifipv6address_list:
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
        MAXIMUMLOADBALANCE:
          name: '最大等价路由数'
          type: integer
          minimum: 1
          maximum: 128
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 1
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
        PEERADDRV6:
          name: 'IPv6对等体地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
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
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
    add_autoscalingethtrunk_list:
      type: items
      properties:
        ETHTRUNKTMPID:
          name: '以太Trunk模板ID'
          type: integer
          minimum: 1
          maximum: 99
          required: true
          description: '接口采用SR-IOV bonding组网时，添加以太网隧道多虚拟网卡自动化配置模板。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        VNICLIST:
          name: '虚拟网卡ID列表'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_autoscalingservice_list:
      type: items
      properties:
        SERVICENAME:
          name: '服务名称'
          type: string
          maxLength: 31
          required: true
          description: '增加自动配置服务。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        VPNNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: '_public_'
        AFTYPE:
          name: '地址族'
          type: string
          enum:
          - IPv4
          - IPv6
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPALLOCTYPE4:
          name: 'IPv4地址分配方式'
          type: string
          enum:
          - DHCP
          - USER_CONFIG
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: USER_CONFIG
        AUTOCFGIFTYPE:
          name: '自动化配置接口类型'
          type: string
          enum:
          - ETHTRUNK
          - VNIC
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: VNIC
        ETHTRUNKTMPID:
          name: '以太Trunk模板ID'
          type: integer
          minimum: 1
          maximum: 99
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        VLANID:
          name: 'VLAN ID'
          type: integer
          minimum: 0
          maximum: 4094
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 0
        BEGINADDR4:
          name: '起始地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        ENDADDR4:
          name: '结束地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        MASKLEN:
          name: '地址池掩码长度'
          type: integer
          minimum: 1
          maximum: 128
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPALLOCTYPE6:
          name: 'IPv6地址分配方式'
          type: string
          enum:
          - DHCP
          - USER_CONFIG
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: USER_CONFIG
        BEGINADDR6:
          name: '起始地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        ENDADDR6:
          name: '结束地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_autoscalingbfd_list:
      type: items
      properties:
        TEMPLATENAME:
          name: '模板名称'
          type: string
          maxLength: 59
          required: true
          description: '配置动态BFD自动化配置模板。参数“DESTADDR4”是网关的接口IP，此处用于检测目的IP能否正常接收报文。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        BFDTYPE:
          name: 'BFD类型'
          type: string
          enum:
          - Dynamic
          - Static
          required: true
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
        SERVICENAME:
          name: '服务名称'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        IPVERSION:
          name: 'IP版本'
          type: string
          enum:
          - IPv4
          - IPv6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DESTADDR4:
          name: '目的地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
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
        ONEARMECHO:
          name: '单臂Echo'
          type: string
          enum:
          - TRUE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: TRUE
        DESTADDR6:
          name: '目的地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_autoscalingsrroute_list:
      type: items
      properties:
        SERVICENAME:
          name: '服务名称'
          type: string
          maxLength: 31
          required: true
          description: '配置静态路由自动化配置模板。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: '_public_'
        IPVERSION:
          name: '地址族'
          type: string
          enum:
          - IPv4
          - IPv6
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        PREFIX4:
          name: '路由前缀IPv4'
          type: string
          maxLength: 15
          required: false
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
          data_source: ''
          pattern: ''
          default: ''
        NEXTHOPALLOCTYPE4:
          name: 'IPv4路由下一跳分配方式'
          type: string
          enum:
          - CONFIG
          - DHCP
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: CONFIG
        NEXTHOP4:
          name: '路由下一跳IPv4'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        BFDENABLE:
          name: 'BFD使能标识'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        DESCRIPTION:
          name: '路由描述'
          type: string
          maxLength: 35
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        BFDTEMPLATENAME:
          name: 'BFD模板名称'
          type: string
          maxLength: 59
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_autoscalingsrroute_list_2:
      type: items
      properties:
        SERVICENAME:
          name: '服务名称'
          type: string
          maxLength: 31
          required: true
          description: '配置静态路由自动化配置模板。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: '_public_'
        IPVERSION:
          name: '地址族'
          type: string
          enum:
          - IPv4
          - IPv6
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        PREFIX4:
          name: '路由前缀IPv4'
          type: string
          maxLength: 15
          required: false
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
          data_source: ''
          pattern: ''
          default: ''
        NEXTHOPALLOCTYPE4:
          name: 'IPv4路由下一跳分配方式'
          type: string
          enum:
          - CONFIG
          - DHCP
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: CONFIG
        NEXTHOP4:
          name: '路由下一跳IPv4'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        BFDENABLE:
          name: 'BFD使能标识'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        DESCRIPTION:
          name: '路由描述'
          type: string
          maxLength: 35
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        BFDTEMPLATENAME:
          name: 'BFD模板名称'
          type: string
          maxLength: 59
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_autoscalingsrroute_list_3:
      type: items
      properties:
        SERVICENAME:
          name: '服务名称'
          type: string
          maxLength: 31
          required: true
          description: '配置静态路由自动化配置模板。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: '_public_'
        IPVERSION:
          name: '地址族'
          type: string
          enum:
          - IPv4
          - IPv6
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        PREFIX6:
          name: '路由前缀IPv6'
          type: string
          maxLength: 39
          required: false
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
          data_source: ''
          pattern: ''
          default: ''
        NEXTHOPALLOCTYPE6:
          name: 'IPv6路由下一跳分配方式'
          type: string
          enum:
          - CONFIG
          - DHCP
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: CONFIG
        NEXTHOP6:
          name: '路由下一跳IPv6'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        BFDENABLE:
          name: 'BFD使能标识'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        DESCRIPTION:
          name: '路由描述'
          type: string
          maxLength: 35
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        BFDTEMPLATENAME:
          name: 'BFD模板名称'
          type: string
          maxLength: 59
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_autoscalingsrroute_list_5:
      type: items
      properties:
        SERVICENAME:
          name: '服务名称'
          type: string
          maxLength: 31
          required: true
          description: '配置静态路由自动化配置模板。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: '_public_'
        IPVERSION:
          name: '地址族'
          type: string
          enum:
          - IPv4
          - IPv6
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        PREFIX6:
          name: '路由前缀IPv6'
          type: string
          maxLength: 39
          required: false
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
          data_source: ''
          pattern: ''
          default: ''
        NEXTHOPALLOCTYPE6:
          name: 'IPv6路由下一跳分配方式'
          type: string
          enum:
          - CONFIG
          - DHCP
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: CONFIG
        NEXTHOP6:
          name: '路由下一跳IPv6'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        BFDENABLE:
          name: 'BFD使能标识'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        DESCRIPTION:
          name: '路由描述'
          type: string
          maxLength: 35
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        BFDTEMPLATENAME:
          name: 'BFD模板名称'
          type: string
          maxLength: 59
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
  examples:
    set_bfd_list:
    - BFDENABLE: TRUE
    set_autoconfig_list:
    - SWITCHFLAG: FALSE
    add_l3vpninst_list:
    - VRFNAME: 'VRF_PS_N4'
      VRFDESCRIPTION: 'N4'
    add_vpninstaf_list:
    - VRFNAME: 'VRF_PS_N4'
      AFTYPE: ipv4uni
      VRFRD: '192.168.225.136:100'
    add_interface_list:
    - IFNAME: 'LoopBackv4'
      IFMTU: 1500
    add_ipbindvpn_list:
    - IFNAME: 'LoopBackv4'
      VRFNAME: 'VRF_PS_N4'
    add_ifipv4address_list:
    - IFNAME: 'LoopBackv4'
      IFIPADDR: '192.168.225.136'
      SUBNETMASK: '255.255.255.255'
      ADDRTYPE: main
    add_interface_list_1:
    - IFNAME: 'LoopBack6'
      IFMTU: 1500
    add_ipbindvpn_list_1:
    - IFNAME: 'LoopBack6'
      VRFNAME: 'VRF_PS_N4'
    set_ifipv6enable_list:
    - IFNAME: 'LoopBack6'
      ENABLEFLAG: TRUE
    add_ifipv6address_list:
    - IFNAME: 'LoopBack6'
      IPV6ADDRESS: 'FC00::225:136'
      PREFIXLEN: 128
    add_bgpvrf_list:
    - VRFNAME: 'VRF_PS_N4'
      DEFAULTAFTYPE: noaf
      ROUTERID: '192.168.225.136'
    add_bgpvrfaf_list:
    - VRFNAME: 'VRF_PS_N4'
      AFTYPE: ipv4uni
      MAXIMUMLOADBALANCE: 2
    add_bgppeer_list:
    - VRFNAME: 'VRF_PS_N4'
      ADDRESSTYPE: ipv4
      PEERADDR: '192.168.79.6'
      REMOTEAS: '60002'
      LOCALIFADDR: '192.168.225.136'
      LOCALIFNAME: 'Loopback6'
      EBGPMAXHOP: 10
      PEERADDRV6: 'FC00::79:6'
    add_importroute_list:
    - VRFNAME: 'VRF_PS_N4'
      AFTYPE: ipv4uni
      IMPORTPROTOCOL: wlr
      MEDENABLE: FALSE
    add_autoscalingethtrunk_list:
    - ETHTRUNKTMPID: 4
      VNICLIST: '4 5'
    add_autoscalingservice_list:
    - SERVICENAME: 'ServName_CN_2006_v4'
      VPNNAME: 'VRF_PS_N4'
      AFTYPE: IPv4
      IPALLOCTYPE4: USER_CONFIG
      AUTOCFGIFTYPE: ETHTRUNK
      ETHTRUNKTMPID: 4
      VLANID: 2006
      BEGINADDR4: '192.168.86.2'
      ENDADDR4: '192.168.86.30'
      MASKLEN: 27
      IPALLOCTYPE6: USER_CONFIG
      BEGINADDR6: 'FC00::86:2'
      ENDADDR6: 'FC00::86:1E'
    add_autoscalingbfd_list:
    - TEMPLATENAME: 'BFD_2006_v4'
      BFDTYPE: Static
      SERVICENAME: 'ServName_CN_2006_v4'
      IPVERSION: IPv4
      DESTADDR4: '192.168.86.1'
      MINECHORXINT: 500
      DETECTMULTI: 4
      ONEARMECHO: TRUE
      DESTADDR6: 'FC00::86:1'
    add_autoscalingsrroute_list:
    - SERVICENAME: 'ServName_CN_2006_v4'
      VRFNAME: 'VRF_PS_N4'
      IPVERSION: IPv4
      PREFIX4: '192.168.79.6'
      MASKLENGTH: 32
      NEXTHOPALLOCTYPE4: CONFIG
      NEXTHOP4: '192.168.86.1'
      BFDENABLE: TRUE
      DESCRIPTION: 'VRF_PS_N4'
      BFDTEMPLATENAME: 'BFD_2006_v4'
    add_autoscalingsrroute_list_2:
    - SERVICENAME: 'ServName_CN_2006_v4'
      VRFNAME: 'VRF_PS_N4'
      IPVERSION: IPv4
      PREFIX4: '0.0.0.0'
      MASKLENGTH: 0
      NEXTHOPALLOCTYPE4: CONFIG
      NEXTHOP4: '192.168.86.1'
      BFDENABLE: TRUE
      DESCRIPTION: 'VRF_PS_N4'
      BFDTEMPLATENAME: 'BFD_2006_v4'
    add_autoscalingsrroute_list_3:
    - SERVICENAME: 'ServName_CN_2006_v6'
      VRFNAME: 'VRF_PS_N4'
      IPVERSION: IPv6
      PREFIX6: 'FC00::79:6'
      MASKLENGTH: 128
      NEXTHOPALLOCTYPE6: CONFIG
      NEXTHOP6: 'FC00::86:1'
      BFDENABLE: TRUE
      DESCRIPTION: 'VRF_PS_N4'
      BFDTEMPLATENAME: 'BFD_2006_v6'
    add_autoscalingsrroute_list_5:
    - SERVICENAME: 'ServName_CN_2006_v6'
      VRFNAME: 'VRF_PS_N4'
      IPVERSION: IPv6
      PREFIX6: '0:0:0:0:0:0:0:0'
      MASKLENGTH: 0
      NEXTHOPALLOCTYPE6: CONFIG
      NEXTHOP6: 'FC00::86:1'
      BFDENABLE: TRUE
      DESCRIPTION: 'VRF_PS_N4'
      BFDTEMPLATENAME: 'BFD_2006_v6'
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

### 2 关闭自动配置开关。自动化配置命令只有在自动配置开关为关闭的状态下才可执行，因此需要提前关闭。

```jinja2
{%- for item in set_autoconfig_list -%}
    SET AUTOCONFIG:
    {#- --- 必选参数 --- -#}
    SWITCHFLAG={{item.SWITCHFLAG}},
    ;
{%- endfor -%}
```

### 3 配置VPN实例。

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
    {#- --- 可选参数 --- -#}
    {%- if item.VRFRD is not none -%}
        VRFRD="{{item.VRFRD}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 VRF\_PS\_N4配置Loopback接口IP。用于建立BGP邻居。

```jinja2
{%- for item in add_interface_list -%}
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
    {#- --- 可选参数 --- -#}
    {%- if item.ADDRTYPE is not none -%}
        ADDRTYPE={{item.ADDRTYPE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

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
{%- for item in add_ipbindvpn_list_1 -%}
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
    ;
{%- endfor -%}
```

### 5 配置BGP VPN实例。

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

### 6 增加BGP VPN实例地址族。UEG对接2个负荷分担的BGP PEER时，“MAXIMUMLOADBALANCE”设置为“2”。

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
        {%- if item.MAXIMUMLOADBALANCE is not none -%}
            MAXIMUMLOADBALANCE={{item.MAXIMUMLOADBALANCE}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 7 配置BGP对等体。此处以对接2个IPv4v6双栈的BGP对等体为例。

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
    ;
{%- endfor -%}
```

### 8 配置BGP引入wlr路由。

```jinja2
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
    ;
{%- endfor -%}
```

### 9 添加以太网隧道多虚拟网卡自动化配置模板。与N3共用物理口时，请跳过本步骤。

```jinja2
{%- if is_optional_ethernet_tunnel_vnic_template -%}
    {%- for item in add_autoscalingethtrunk_list -%}
        ADD AUTOSCALINGETHTRUNK:
        {#- --- 必选参数 --- -#}
        ETHTRUNKTMPID={{item.ETHTRUNKTMPID}},
        VNICLIST="{{item.VNICLIST}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

### 10 配置外联口自动部署模板。

```jinja2
{%- for item in add_autoscalingservice_list -%}
    ADD AUTOSCALINGSERVICE:
    {#- --- 必选参数 --- -#}
    SERVICENAME="{{item.SERVICENAME}}",
    AFTYPE={{item.AFTYPE}},
    {#- --- 可选参数 --- -#}
    {%- if item.VPNNAME is not none -%}
        VPNNAME="{{item.VPNNAME}}",
    {%- endif -%}
    {%- if item.AUTOCFGIFTYPE is not none -%}
        AUTOCFGIFTYPE={{item.AUTOCFGIFTYPE}},
    {%- endif -%}
    {%- if item.VLANID is not none -%}
        VLANID={{item.VLANID}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：AUTOCFGIFTYPE=ETHTRUNK 时必选 --- -#}
    {%- if item.AUTOCFGIFTYPE == 'ETHTRUNK' -%}
        ETHTRUNKTMPID={{item.ETHTRUNKTMPID}},
    {%- endif -%}
    {#- --- 条件必选：IPALLOCTYPE4=USER_CONFIG 时必选 --- -#}
    {%- if item.IPALLOCTYPE4 == 'USER_CONFIG' -%}
        BEGINADDR4="{{item.BEGINADDR4}}",
    {%- endif -%}
    {#- --- 条件必选：IPALLOCTYPE4=USER_CONFIG 时必选 --- -#}
    {%- if item.IPALLOCTYPE4 == 'USER_CONFIG' -%}
        ENDADDR4="{{item.ENDADDR4}}",
    {%- endif -%}
    {#- --- 条件必选：IPALLOCTYPE4=USER_CONFIG 时必选 --- -#}
    {%- if item.IPALLOCTYPE4 == 'USER_CONFIG' -%}
        MASKLEN={{item.MASKLEN}},
    {#- --- 条件必选：IPALLOCTYPE6=USER_CONFIG 时必选 --- -#}
    {%- elif item.IPALLOCTYPE6 == 'USER_CONFIG' -%}
        MASKLEN={{item.MASKLEN}},
    {%- endif -%}
    {#- --- 条件必选：IPALLOCTYPE6=USER_CONFIG 时必选 --- -#}
    {%- if item.IPALLOCTYPE6 == 'USER_CONFIG' -%}
        BEGINADDR6="{{item.BEGINADDR6}}",
    {%- endif -%}
    {#- --- 条件必选：IPALLOCTYPE6=USER_CONFIG 时必选 --- -#}
    {%- if item.IPALLOCTYPE6 == 'USER_CONFIG' -%}
        ENDADDR6="{{item.ENDADDR6}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：AFTYPE=IPv4 时可选 --- -#}
    {%- if item.AFTYPE == 'IPv4' -%}
        {%- if item.IPALLOCTYPE4 is not none -%}
            IPALLOCTYPE4={{item.IPALLOCTYPE4}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：AFTYPE=IPv6 时可选 --- -#}
    {%- if item.AFTYPE == 'IPv6' -%}
        {%- if item.IPALLOCTYPE6 is not none -%}
            IPALLOCTYPE6={{item.IPALLOCTYPE6}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 11 增加BFD会话自动部署模板。

```jinja2
{%- for item in add_autoscalingbfd_list -%}
    ADD AUTOSCALINGBFD:
    {#- --- 必选参数 --- -#}
    TEMPLATENAME="{{item.TEMPLATENAME}}",
    BFDTYPE={{item.BFDTYPE}},
    {#- --- 可选参数 --- -#}
    {%- if item.DETECTMULTI is not none -%}
        DETECTMULTI={{item.DETECTMULTI}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：BFDTYPE=Static 时必选 --- -#}
    {%- if item.BFDTYPE == 'Static' -%}
        SERVICENAME="{{item.SERVICENAME}}",
    {%- endif -%}
    {#- --- 条件必选：BFDTYPE=Static 时必选 --- -#}
    {%- if item.BFDTYPE == 'Static' -%}
        IPVERSION={{item.IPVERSION}},
    {%- endif -%}
    {#- --- 条件必选：IPVERSION=IPv4 时必选 --- -#}
    {%- if item.IPVERSION == 'IPv4' -%}
        DESTADDR4="{{item.DESTADDR4}}",
    {%- endif -%}
    {#- --- 条件必选：IPVERSION=IPv6 时必选 --- -#}
    {%- if item.IPVERSION == 'IPv6' -%}
        DESTADDR6="{{item.DESTADDR6}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：BFDTYPE=Static 时可选 --- -#}
    {%- if item.BFDTYPE == 'Static' -%}
        {%- if item.MINECHORXINT is not none -%}
            MINECHORXINT={{item.MINECHORXINT}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：BFDTYPE=Static 时可选 --- -#}
    {%- if item.BFDTYPE == 'Static' -%}
        {%- if item.ONEARMECHO is not none -%}
            ONEARMECHO={{item.ONEARMECHO}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 12 增加静态路由自动部署模板。

#### 12.1 //“PREFIX4”和“MASKLENGTH”是目的IP和掩码（BGP对等体的IP地址和掩码）。

```jinja2
{%- for item in add_autoscalingsrroute_list -%}
    ADD AUTOSCALINGSRROUTE:
    {#- --- 必选参数 --- -#}
    SERVICENAME="{{item.SERVICENAME}}",
    IPVERSION={{item.IPVERSION}},
    MASKLENGTH={{item.MASKLENGTH}},
    {#- --- 可选参数 --- -#}
    {%- if item.VRFNAME is not none -%}
        VRFNAME="{{item.VRFNAME}}",
    {%- endif -%}
    {%- if item.BFDENABLE is not none -%}
        BFDENABLE={{item.BFDENABLE}},
    {%- endif -%}
    {%- if item.DESCRIPTION is not none -%}
        DESCRIPTION="{{item.DESCRIPTION}}",
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPVERSION=IPv4 时必选 --- -#}
    {%- if item.IPVERSION == 'IPv4' -%}
        PREFIX4="{{item.PREFIX4}}",
    {%- endif -%}
    {#- --- 条件必选：NEXTHOPALLOCTYPE4=CONFIG 时必选 --- -#}
    {%- if item.NEXTHOPALLOCTYPE4 == 'CONFIG' -%}
        NEXTHOP4="{{item.NEXTHOP4}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：IPVERSION=IPv4 时可选 --- -#}
    {%- if item.IPVERSION == 'IPv4' -%}
        {%- if item.NEXTHOPALLOCTYPE4 is not none -%}
            NEXTHOPALLOCTYPE4={{item.NEXTHOPALLOCTYPE4}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：BFDENABLE=TRUE 时可选 --- -#}
    {%- if item.BFDENABLE == 'TRUE' -%}
        {%- if item.BFDTEMPLATENAME is not none -%}
            BFDTEMPLATENAME="{{item.BFDTEMPLATENAME}}",
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 12.2 //对端网元不发布BGP默认路由时，需要配置该步骤。“PREFIX4”设置为“0.0.0.0”，“MASKLENGTH”设置为“0”。其他参数与到BGP对等体的路由相同。

```jinja2
{%- if is_scenario_peer_no_default_route -%}
    {%- for item in add_autoscalingsrroute_list_2 -%}
        ADD AUTOSCALINGSRROUTE:
        {#- --- 必选参数 --- -#}
        SERVICENAME="{{item.SERVICENAME}}",
        IPVERSION={{item.IPVERSION}},
        MASKLENGTH={{item.MASKLENGTH}},
        {#- --- 可选参数 --- -#}
        {%- if item.VRFNAME is not none -%}
            VRFNAME="{{item.VRFNAME}}",
        {%- endif -%}
        {%- if item.BFDENABLE is not none -%}
            BFDENABLE={{item.BFDENABLE}},
        {%- endif -%}
        {%- if item.DESCRIPTION is not none -%}
            DESCRIPTION="{{item.DESCRIPTION}}",
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：IPVERSION=IPv4 时必选 --- -#}
        {%- if item.IPVERSION == 'IPv4' -%}
            PREFIX4="{{item.PREFIX4}}",
        {%- endif -%}
        {#- --- 条件必选：NEXTHOPALLOCTYPE4=CONFIG 时必选 --- -#}
        {%- if item.NEXTHOPALLOCTYPE4 == 'CONFIG' -%}
            NEXTHOP4="{{item.NEXTHOP4}}",
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：IPVERSION=IPv4 时可选 --- -#}
        {%- if item.IPVERSION == 'IPv4' -%}
            {%- if item.NEXTHOPALLOCTYPE4 is not none -%}
                NEXTHOPALLOCTYPE4={{item.NEXTHOPALLOCTYPE4}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：BFDENABLE=TRUE 时可选 --- -#}
        {%- if item.BFDENABLE == 'TRUE' -%}
            {%- if item.BFDTEMPLATENAME is not none -%}
                BFDTEMPLATENAME="{{item.BFDTEMPLATENAME}}",
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 12.3 //“PREFIX6”和“MASKLENGTH”是目的IP和掩码（BGP对等体的IP地址和掩码）。

```jinja2
{%- for item in add_autoscalingsrroute_list_3 -%}
    ADD AUTOSCALINGSRROUTE:
    {#- --- 必选参数 --- -#}
    SERVICENAME="{{item.SERVICENAME}}",
    IPVERSION={{item.IPVERSION}},
    MASKLENGTH={{item.MASKLENGTH}},
    {#- --- 可选参数 --- -#}
    {%- if item.VRFNAME is not none -%}
        VRFNAME="{{item.VRFNAME}}",
    {%- endif -%}
    {%- if item.BFDENABLE is not none -%}
        BFDENABLE={{item.BFDENABLE}},
    {%- endif -%}
    {%- if item.DESCRIPTION is not none -%}
        DESCRIPTION="{{item.DESCRIPTION}}",
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPVERSION=IPv6 时必选 --- -#}
    {%- if item.IPVERSION == 'IPv6' -%}
        PREFIX6="{{item.PREFIX6}}",
    {%- endif -%}
    {#- --- 条件必选：NEXTHOPALLOCTYPE6=CONFIG 时必选 --- -#}
    {%- if item.NEXTHOPALLOCTYPE6 == 'CONFIG' -%}
        NEXTHOP6="{{item.NEXTHOP6}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：IPVERSION=IPv6 时可选 --- -#}
    {%- if item.IPVERSION == 'IPv6' -%}
        {%- if item.NEXTHOPALLOCTYPE6 is not none -%}
            NEXTHOPALLOCTYPE6={{item.NEXTHOPALLOCTYPE6}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：BFDENABLE=TRUE 时可选 --- -#}
    {%- if item.BFDENABLE == 'TRUE' -%}
        {%- if item.BFDTEMPLATENAME is not none -%}
            BFDTEMPLATENAME="{{item.BFDTEMPLATENAME}}",
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 12.4 //对端网元不发布BGP默认路由时，需要配置该步骤。“PREFIX6”设置为“0:0:0:0:0:0:0:0”，“MASKLENGTH”设置为“0”。其他参数与到BGP对等体的路由相同。

```jinja2
{%- if is_scenario_peer_no_default_route -%}
    {%- for item in add_autoscalingsrroute_list_5 -%}
        ADD AUTOSCALINGSRROUTE:
        {#- --- 必选参数 --- -#}
        SERVICENAME="{{item.SERVICENAME}}",
        IPVERSION={{item.IPVERSION}},
        MASKLENGTH={{item.MASKLENGTH}},
        {#- --- 可选参数 --- -#}
        {%- if item.VRFNAME is not none -%}
            VRFNAME="{{item.VRFNAME}}",
        {%- endif -%}
        {%- if item.BFDENABLE is not none -%}
            BFDENABLE={{item.BFDENABLE}},
        {%- endif -%}
        {%- if item.DESCRIPTION is not none -%}
            DESCRIPTION="{{item.DESCRIPTION}}",
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：IPVERSION=IPv6 时必选 --- -#}
        {%- if item.IPVERSION == 'IPv6' -%}
            PREFIX6="{{item.PREFIX6}}",
        {%- endif -%}
        {#- --- 条件必选：NEXTHOPALLOCTYPE6=CONFIG 时必选 --- -#}
        {%- if item.NEXTHOPALLOCTYPE6 == 'CONFIG' -%}
            NEXTHOP6="{{item.NEXTHOP6}}",
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：IPVERSION=IPv6 时可选 --- -#}
        {%- if item.IPVERSION == 'IPv6' -%}
            {%- if item.NEXTHOPALLOCTYPE6 is not none -%}
                NEXTHOPALLOCTYPE6={{item.NEXTHOPALLOCTYPE6}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：BFDENABLE=TRUE 时可选 --- -#}
        {%- if item.BFDENABLE == 'TRUE' -%}
            {%- if item.BFDTEMPLATENAME is not none -%}
                BFDTEMPLATENAME="{{item.BFDTEMPLATENAME}}",
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```


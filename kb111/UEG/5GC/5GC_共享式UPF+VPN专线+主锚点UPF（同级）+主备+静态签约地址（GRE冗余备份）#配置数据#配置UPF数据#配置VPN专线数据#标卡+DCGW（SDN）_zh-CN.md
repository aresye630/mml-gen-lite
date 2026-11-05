---
id: ''
name: 标卡+DCGW（SDN）
ne_type: UEG
type: feature
description: SDN场景下，新增企业，开通业务时，UPF到园区采用VPN专线，UPF使用标卡，对接DCGW（路由器）或DCGW（交换机）。  对于容灾的两个UPF而言，此配置没有区别，仅以一个UPF做配置举例。
tags: []
risk_level: ''
doc_source: ["云网（连接+计算，入驻式或共享式）","业务发放","5GC toB DNN业务发放（云网，带计算）","通过OMC发放","DNN发放操作","发放共享式UPF+VPN专线","共享式UPF+VPN专线+主锚点UPF（同级）+主备+静态签约地址（GRE冗余备份）","配置数据","配置UPF数据","配置VPN专线数据","标卡+DCGW（SDN）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
SDN场景下，新增企业，开通业务时，UPF到园区采用VPN专线，UPF使用标卡，对接DCGW（路由器）或DCGW（交换机）。对于容灾的两个UPF而言，此配置没有区别，仅以一个UPF做配置举例。

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
          data_source: '固定取值'
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
        IPALLOCTYPE6:
          name: 'IPv6地址分配方式'
          type: string
          enum:
          - DHCP
          - USER_CONFIG
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: USER_CONFIG
        ADDRMODE:
          name: '地址模式'
          type: string
          enum:
          - HOST_MODE
          - NETWOKSEGMENT_MODE
          required: false
          description: '仅在IPv6场景下配置。'
          data_source: '固定取值'
          pattern: ''
          default: HOST_MODE
    add_autoscalingbfd_list:
      type: items
      properties:
        TEMPLATENAME:
          name: '模板名称'
          type: string
          maxLength: 59
          required: true
          description: '“DESTADDR4”是网关的接口IP，此处用于检测目的IP能否正常接收报文。'
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
          data_source: '固定取值'
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
          data_source: '固定取值'
          pattern: ''
          default: CONFIG
        PREFERENCE:
          name: '路由优先级'
          type: integer
          minimum: 1
          maximum: 255
          required: false
          description: ''
          data_source: ''
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
        BFDTEMPLATENAME:
          name: 'BFD模板名称'
          type: string
          maxLength: 59
          required: false
          description: ''
          data_source: '已配置数据中获取'
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
        NEXTHOPALLOCTYPE6:
          name: 'IPv6路由下一跳分配方式'
          type: string
          enum:
          - CONFIG
          - DHCP
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: CONFIG
    set_autoconfig_list_1:
      type: items
      properties:
        SWITCHFLAG:
          name: '自动配置开关'
          type: string
          enum:
          - TRUE
          - FALSE
          required: true
          description: '打开自动化配置服务。'
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
    set_autoconfig_list:
    - SWITCHFLAG: FALSE
    add_autoscalingethtrunk_list:
    - ETHTRUNKTMPID: 6
      VNICLIST: '6 7'
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
    add_autoscalingservice_list:
    - SERVICENAME: 'VRF_N6_Local_2B_001_2005'
      VPNNAME: 'VRF_N6_Local_2B_001'
      AFTYPE: IPv4
      IPALLOCTYPE4: DHCP
      AUTOCFGIFTYPE: ETHTRUNK
      ETHTRUNKTMPID: 6
      VLANID: 915
      IPALLOCTYPE6: DHCP
      ADDRMODE: NETWOKSEGMENT_MODE
    add_autoscalingbfd_list:
    - TEMPLATENAME: 'N6_BFD_1'
      BFDTYPE: Static
      SERVICENAME: 'VRF_N6_Local_2B_2005'
      IPVERSION: IPv4
      DESTADDR4: '192.168.11.11'
      MINECHORXINT: 500
      DETECTMULTI: 4
      ONEARMECHO: TRUE
      DESTADDR6: 'fc00:187:C28C:0:0:0:0:1'
    add_autoscalingsrroute_list:
    - SERVICENAME: 'VRF_N6_Local_2B_001_2005'
      VRFNAME: 'VRF_N6_Local_2B_001'
      IPVERSION: IPv4
      PREFIX4: '192.168.11.1'
      MASKLENGTH: 32
      NEXTHOPALLOCTYPE4: DHCP
      PREFERENCE: 60
      BFDENABLE: TRUE
      BFDTEMPLATENAME: 'N6_BFD_1'
      PREFIX6: 'fc00:187:C289::1'
      NEXTHOPALLOCTYPE6: DHCP
    set_autoconfig_list_1:
    - SWITCHFLAG: TRUE
    add_interface_list:
    - IFNAME: 'LoopBack14'
      IFADMINSTATUS: up
      IFMTU: 1500
      IFDF: FALSE
      IFSTATIENABLE: TRUE
      IFTRAPENABLE: TRUE
    add_ipbindvpn_list:
    - IFNAME: 'LoopBack14'
      VRFNAME: 'VRF_N6_Local_2B_001'
    add_ifipv4address_list:
    - IFNAME: 'LoopBack14'
      IFIPADDR: '172.20.9.7'
      SUBNETMASK: '255.255.255.255'
      ADDRTYPE: main
    add_interface_list_1:
    - IFNAME: 'LoopBack13'
      IFADMINSTATUS: up
      IFMTU: 1500
      IFDF: FALSE
      IFSTATIENABLE: TRUE
      IFTRAPENABLE: TRUE
    add_ipbindvpn_list_1:
    - IFNAME: 'LoopBack13'
      VRFNAME: 'VRF_N6_Local_2B_001'
    set_ifipv6enable_list:
    - IFNAME: 'Loopback13'
      ENABLEFLAG: TRUE
    add_ifipv6address_list:
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

### 2 关闭自动配置开关。自动化配置命令只有在自动配置开关为关闭的状态下才可执行，因此需要提前关闭。

```jinja2
{%- for item in set_autoconfig_list -%}
    SET AUTOCONFIG:
    {#- --- 必选参数 --- -#}
    SWITCHFLAG={{item.SWITCHFLAG}},
    ;
{%- endfor -%}
```

### 3 配置bond组网以太Trunk。

```jinja2
{%- for item in add_autoscalingethtrunk_list -%}
    ADD AUTOSCALINGETHTRUNK:
    {#- --- 必选参数 --- -#}
    ETHTRUNKTMPID={{item.ETHTRUNKTMPID}},
    VNICLIST="{{item.VNICLIST}}",
    ;
{%- endfor -%}
```

### 4 配置VPN实例。

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

### 5 增加自动配置服务。

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
    {#- --- 条件可选：IPALLOCTYPE6=DHCP 时可选 --- -#}
    {%- if item.IPALLOCTYPE6 == 'DHCP' -%}
        {%- if item.ADDRMODE is not none -%}
            ADDRMODE={{item.ADDRMODE}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 6 配置动态BFD自动化配置模板。

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

### 7 配置静态路由自动化配置模板。

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
    {%- if item.PREFERENCE is not none -%}
        PREFERENCE={{item.PREFERENCE}},
    {%- endif -%}
    {%- if item.BFDENABLE is not none -%}
        BFDENABLE={{item.BFDENABLE}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPVERSION=IPv4 时必选 --- -#}
    {%- if item.IPVERSION == 'IPv4' -%}
        PREFIX4="{{item.PREFIX4}}",
    {%- endif -%}
    {#- --- 条件必选：IPVERSION=IPv6 时必选 --- -#}
    {%- if item.IPVERSION == 'IPv6' -%}
        PREFIX6="{{item.PREFIX6}}",
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
    {#- --- 条件可选：IPVERSION=IPv6 时可选 --- -#}
    {%- if item.IPVERSION == 'IPv6' -%}
        {%- if item.NEXTHOPALLOCTYPE6 is not none -%}
            NEXTHOPALLOCTYPE6={{item.NEXTHOPALLOCTYPE6}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 8 打开自动化配置服务。

```jinja2
{%- for item in set_autoconfig_list_1 -%}
    SET AUTOCONFIG:
    {#- --- 必选参数 --- -#}
    SWITCHFLAG={{item.SWITCHFLAG}},
    ;
{%- endfor -%}
```

### 9 添加loopback接口。

```jinja2
{%- for item in add_interface_list -%}
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

### 10 设置BGP。

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

### 11 添加BGP VPN。

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

### 12 增加BGP VPN地址族。

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

### 13 （负荷分担UPF场景下）增加指定协议中的入口路由配置。

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
        ;
    {%- endfor -%}
{%- endif -%}
```

### 14 （GRE路由冗余隧道场景下）增加指定协议中的入口路由配置。

```jinja2
{%- if is_scenario_gre_redundancy_tunnel -%}
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

### 15 增加BGP对等体。

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


---
id: ''
name: BGP over静态路由+BFD(IPv4)
ne_type: UDG
type: feature
description: SDN场景，VNF和DC-GW间通过Loopback IP建立eBGP邻居，用于业务路由的学习和发布。Loopback IP之间通过静态路由互通。
risk_level: ''
doc_source: ["网络部署","初始配置","UDG初始配置与调测","组网路由配置","配置VNF侧IP路由（SDN）","BGP over静态路由+BFD(IPv4)"]
refs: []
metadata:
  DepOnLiveCfg: true
allowed-tools:
- getParameterValue('LST AUTOCONFIG')
---
<!-- @mml:block=annotations -->
```text
## 操作场景
SDN场景，VNF和DC-GW间通过Loopback IP建立eBGP邻居，用于业务路由的学习和发布。Loopback IP之间通过静态路由互通。

## 必备事项
前提条件

请阅读并熟悉特性IPFD-014003 静态路由、IPFD-014002 支持BGP特性概述和IPFD-104403 BFD特性概述。
具备管理员权限的操作人员已经登录华为操作维护系统。
VNF与网络实体之间的网络环境已经构建完成。
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
          description: 'VPN实例全网统一规划，一条通信路径上所有节点绑定的VPN实例要一致，才能正常通信。'
          data_source: '参见“5G Core垂直网设LLD文档 > 5G Core业务IP对接设计 > VRF”'
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
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: ''
        VRFRD:
          name: '路由标识'
          type: string
          maxLength: 21
          required: false
          description: '不同VPN实例的路由标识必须不同。'
          data_source: '参见“5G Core LLD文档 > 路由设计 > VRF设计”。'
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
    add_autoscalingethtrunk_list:
      type: items
      properties:
        ETHTRUNKTMPID:
          name: '以太Trunk模板ID'
          type: integer
          minimum: 1
          maximum: 99
          required: true
          description: 'SR-IOV bonding组网需要规划。  只有MAC地址一样的vNIC才能加到同一个TRUNK里。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        VNICLIST:
          name: '虚拟网卡ID列表'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: '参见“5G Core垂直网设LLD文档 > 5G Core业务IP对接设计 > 端口”'
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
          description: '一个VLAN平面时，此处只需要规划一条数据（例如只规划ServName\_Access\_100\_v4）。'
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
          data_source: '已配置数据中获取'
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
        VNICID:
          name: '虚拟网卡ID'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: false
          description: '非SR-IOV bonding组网需要规划。'
          data_source: '参见“5G Core垂直网设LLD文档 > 5G Core业务IP对接设计 > 端口”'
          pattern: ''
          default: ''
        VLANID:
          name: 'VLAN ID'
          type: integer
          minimum: 0
          maximum: 4094
          required: false
          description: '一个VLAN平面时，此处只需要规划一个VLANID。'
          data_source: '参见“5G Core垂直网设LLD文档 > 5G Core业务IP对接设计 > VLAN”'
          pattern: ''
          default: 0
        NETWORKINSTID:
          name: '网络分组标识'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: false
          description: '一个UPF对接的所有企业总共规划使用65到128 VPN专线时，则N6口需要配置“NETWORKINSTID”参数。其他场景，不需要规划该参数。  一个网络分组标识最多和64个VPN实例绑定。一个UPF当前最多支持128个VPN专线。  该参数取值必须与VNFD模板中定义的网络分组ID一致。此处样例值0仅用于示例。'
          data_source: '参见“5G Core垂直网设LLD文档 > 5G Core业务IP对接设计 > ”NetworkID'
          pattern: ''
          default: 0
        ETHTRUNKTMPID:
          name: '以太Trunk模板ID'
          type: integer
          minimum: 1
          maximum: 99
          required: false
          description: 'SR-IOV bonding组网需要规划。'
          data_source: '已规划数据中获取'
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
        BEGINADDR4:
          name: '起始地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ENDADDR4:
          name: '结束地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
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
    add_autoscalingservice_list_2:
      type: items
      properties:
        SERVICENAME:
          name: '服务名称'
          type: string
          maxLength: 31
          required: true
          description: '一个VLAN平面时，此处只需要规划一条数据（例如只规划ServName\_Access\_100\_v4）。'
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
          data_source: '已配置数据中获取'
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
          description: 'SR-IOV bonding组网需要规划。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        VLANID:
          name: 'VLAN ID'
          type: integer
          minimum: 0
          maximum: 4094
          required: false
          description: '一个VLAN平面时，此处只需要规划一个VLANID。'
          data_source: '参见“5G Core垂直网设LLD文档 > 5G Core业务IP对接设计 > VLAN”'
          pattern: ''
          default: 0
        NETWORKINSTID:
          name: '网络分组标识'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: false
          description: '一个UPF对接的所有企业总共规划使用65到128 VPN专线时，则N6口需要配置“NETWORKINSTID”参数。其他场景，不需要规划该参数。  一个网络分组标识最多和64个VPN实例绑定。一个UPF当前最多支持128个VPN专线。  该参数取值必须与VNFD模板中定义的网络分组ID一致。此处样例值0仅用于示例。'
          data_source: '参见“5G Core垂直网设LLD文档 > 5G Core业务IP对接设计 > ”NetworkID'
          pattern: ''
          default: 0
        VNICID:
          name: '虚拟网卡ID'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: false
          description: '非SR-IOV bonding组网需要规划。'
          data_source: '参见“5G Core垂直网设LLD文档 > 5G Core业务IP对接设计 > 端口”'
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
        BEGINADDR4:
          name: '起始地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ENDADDR4:
          name: '结束地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
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
    add_autoscalingbfd_list:
      type: items
      properties:
        TEMPLATENAME:
          name: '模板名称'
          type: string
          maxLength: 59
          required: true
          description: '“单臂Echo（ONEARMECHO）”设置为“TRUE”，目的地址是Leaf节点的IP地址。'
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
          name: '地址族'
          type: string
          enum:
          - IPv4
          - IPv6
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
        DESTADDR4:
          name: '目的地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '参见“5G Core垂直网设LLD文档 > 5G Core业务IP对接设计 > 网关”'
          pattern: ''
          default: ''
        MINECHORXINT:
          name: '单臂Echo会话的收包间隔（ms）'
          type: integer
          minimum: 30
          maximum: 1000
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: 200
        DETECTMULTI:
          name: '检测倍数'
          type: integer
          minimum: 3
          maximum: 50
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: 3
        ONEARMECHO:
          name: '单臂Echo'
          type: string
          enum:
          - TRUE
          required: false
          description: ''
          data_source: '参见“5G Core垂直网设LLD文档 > 路由设计 > BFD设计”'
          pattern: ''
          default: TRUE
        MINRXINTERVAL:
          name: '动态BFD会话的收包间隔（ms）'
          type: integer
          minimum: 30
          maximum: 1000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 200
        MINTXINTERVAL:
          name: '动态BFD会话的发包间隔（ms）'
          type: integer
          minimum: 30
          maximum: 1000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 200
        DESTADDR6:
          name: '目的地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
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
          description: '-'
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
          data_source: '本端规划'
          pattern: ''
          default: ''
        PREFIX4:
          name: '路由前缀'
          type: string
          maxLength: 15
          required: false
          description: 'BGP对等体地址。  “路由前缀（PREFIX4）”与**ADD BGPPEER**命令中的“PEERADDR”相同。'
          data_source: '参见“5G Core垂直网设LLD文档 > 路由设计 > BGP设计”'
          pattern: ''
          default: ''
        MASKLENGTH:
          name: '路由掩码长度'
          type: integer
          minimum: 0
          maximum: 128
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        NEXTHOPALLOCTYPE4:
          name: 'IPv4路由下一跳分配方式'
          type: string
          enum:
          - CONFIG
          - DHCP
          required: false
          description: '-'
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
          description: '“BFDENABLE”设置为“TRUE”，采用单臂Echo。'
          data_source: '参见“5G Core垂直网设LLD文档 > 路由设计 > BFD设计”'
          pattern: ''
          default: FALSE
        BFDTEMPLATENAME:
          name: 'BFD模板名称'
          type: string
          maxLength: 59
          required: false
          description: '-'
          data_source: '已配置数据中获取'
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
        PREFIX6:
          name: '路由前缀IPv6'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NEXTHOP4:
          name: '路由下一跳IPv4'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
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
          description: ''
          data_source: ''
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
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: ''
        ASNUM:
          name: 'BGP自治域号'
          type: string
          maxLength: 11
          required: false
          description: ''
          data_source: '参见“5G Core垂直网设LLD文档 > 路由设计 > BGP设计”'
          pattern: ''
          default: ''
        ASPATHLIMIT:
          name: '自治域路径上限'
          type: integer
          minimum: 0
          maximum: 2000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        BGPRIDAUTOSEL:
          name: '使能VPN路由器的ID为自动选择'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CHECKFIRSTAS:
          name: '使能检查第一个自治域号'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CONFEDIDNUMBER:
          name: '联盟ID'
          type: string
          maxLength: 11
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CONFEDNONSTANDED:
          name: '使能联盟'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GRACEFULRESTART:
          name: '使能GR能力'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GRPEERRESET:
          name: '使能GR能力重置BGP连接'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ISSHUTDOWN:
          name: '中断BGP对等体协议会话'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        KEEPALLROUTES:
          name: '使能全部路由'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MEMORYLIMIT:
          name: '启用内存限制的前缀'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TIMEWAITFORRIB:
          name: 'RIB结束时间（s）'
          type: integer
          minimum: 3
          maximum: 3000
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
          description: '-'
          data_source: '参见“5G Core垂直网设LLD文档 > 路由设计 > BGP设计”'
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
          description: '此处的VPN实例已经配置，与外联口绑定的VPN实例相同。'
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
          name: 'IPv4地址'
          type: string
          maxLength: 15
          required: true
          description: '如果规划Loopback接口使用IPv4v6双栈地址，则分别执行**ADD IFIPV4ADDRESS**和**ADD IFIPV6ADDRESS**对同一Loopback接口配置IPv4和IPv6地址。'
          data_source: '参见“5G Core垂直网设LLD文档 > 路由设计 > BGP设计”'
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
    add_bgpvrf_list:
      type: items
      properties:
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: true
          description: 'BGP VPN实例需要与Loopback接口绑定的VPN实例名一致。'
          data_source: '已配置数据中获取'
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
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: ipv4uni
        ROUTERID:
          name: '路由器ID'
          type: string
          maxLength: 15
          required: false
          description: '不同BGP VPN实例的ROUTERID不能重复。'
          data_source: '参见“5G Core垂直网设LLD文档 > 路由设计 > BGP设计”'
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
          description: '使用**ADD BGPVRF**命令中的VPN实例名称。'
          data_source: '已配置数据中获取'
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
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        MAXIMUMLOADBALANCE:
          name: '最大等价路由数'
          type: integer
          minimum: 1
          maximum: 128
          required: false
          description: '负荷分担关系的BGP PEER数。'
          data_source: '本端规划'
          pattern: ''
          default: 1
        ACTIVEROUTEADVERTISE:
          name: '活跃路由通告'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        ADDPATHSELNUM:
          name: '选择add-path路由的数量'
          type: integer
          minimum:
          - 0
          - 2
          maximum:
          - 0
          - 64
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ALWAYSCOMPAREMED:
          name: '总是比较MED'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        APPLYLABELMODE:
          name: '标签分配方式'
          type: string
          enum:
          - perNexthop
          - perRoute
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: perRoute
        ASPATHIGNORE:
          name: '忽略AS路径'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        AUTOFRRENABLE:
          name: '自动FRR使能'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        AUTOMATICSUMMARY:
          name: '自动聚合'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        BESTEXTERNAL:
          name: '是否发布bestExternal路由'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        DEFAULTLOCALPREF:
          name: '缺省本地优先级'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 100
        DEFAULTMED:
          name: '缺省MED'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 0
        DEFAULTRTIMPORTENABLE:
          name: '缺省路由引入使能'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        DETERMINMED:
          name: '使能Deterministic-MED'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        EBGPECMPNEXTHOPCHANGED:
          name: 'EBGP负载分担改下一跳'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        EBGPIFSENSITIVE:
          name: 'EBGP接口快速感知'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: TRUE
        ECMPNEXTHOPCHANGED:
          name: '负载分担改下一跳'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        EIBGPEXTHOPCHANGED:
          name: 'EBGP/IBGP负载分担改下一跳'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        EIBGPLOADBALANCE:
          name: 'EBGP/IBGP负载分担数'
          type: integer
          minimum: 0
          maximum: 128
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IBGPECMPNEXTHOPCHANGED:
          name: 'IBGP负载分担改下一跳'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        IBGPIFSENSITIVE:
          name: 'IBGP接口快速感知'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        IGPMETRICIGNORE:
          name: '忽略IGP Metric'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        LOADASPATHIGNORE:
          name: '负载均衡忽略AS Path'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
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
        MAXLOADIBGPNUM:
          name: 'IBGP负载分担数'
          type: integer
          minimum: 1
          maximum: 128
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 1
        MEDCONFED:
          name: '联盟内部比较MED'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        MEDNONEASMAXIMUM:
          name: 'MED使用最大值'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        NEXTHOPSELDEPENDTYPE:
          name: '下一跳迭代方式'
          type: string
          enum:
          - default
          - dependIp
          - dependTunnel
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: dependIp
        NHPRELAYROUTEPOLICYNAME:
          name: '下一跳迭代路由策略名'
          type: string
          maxLength: 200
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ORIGINATORPRIOR:
          name: '选择最佳路由时，Router ID优先于CLUSTER_LIST'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        POLICYEXTCOMMENABLE:
          name: '修改扩展团体属性'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        POLICYVPNTARGET:
          name: '是否需要过VpnTarget的策略'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: TRUE
        PREFERENCEEXTERNAL:
          name: '外部路由协议优先级'
          type: integer
          minimum: 1
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 255
        PREFERENCEINTERNAL:
          name: '内部路由协议优先级'
          type: integer
          minimum: 1
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 255
        PREFERENCELOCAL:
          name: '本地路由协议优先级'
          type: integer
          minimum: 1
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 255
        PREFERENCEPOLICYNAME:
          name: '协议优先级策略名'
          type: string
          maxLength: 200
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        REFLECTBETWEENCLIENT:
          name: '客户机路由反射'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: TRUE
        REFLECTCHGPATH:
          name: '反射器应用出口策略'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        REFLECTORCLUSTERID:
          name: '路由反射器集群ID'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        REFLECTORCLUSTERIPV4:
          name: '路由反射器集群ID(IPv4)'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RELAYDELAYENABLE:
          name: '迭代延迟使能'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: TRUE
        ROUTERID:
          name: '路由器标识'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ROUTERIDNEGLECT:
          name: '忽略路由器ID'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        ROUTESELECTDELAY:
          name: '路由选路延迟时间'
          type: integer
          minimum: 0
          maximum: 3600
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 0
        RRFILTERNUMBER:
          name: '路由反射器组支持的扩展团体属性过滤器号'
          type: string
          maxLength: 51
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SUPERNETUNIADV:
          name: '发布超网单播路由'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        TNLSELECTORNAME:
          name: '隧道选择器名称'
          type: string
          maxLength: 40
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VRFRIDAUTOSEL:
          name: '私网BGP实例自动选择路由器ID'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
    add_bgppeer_list:
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
        ADDRESSTYPE:
          name: '地址类型'
          type: string
          enum:
          - ipv4
          - ipv6
          - noaf
          required: false
          description: '-'
          data_source: '-'
          pattern: ''
          default: ipv4
        PEERADDR:
          name: 'IPv4对等体地址'
          type: string
          maxLength: 15
          required: false
          description: 'DC-GW上的BGP Loopback IP地址及AS号。'
          data_source: '参见“5G Core垂直网设LLD文档 > 路由设计 > BGP设计”'
          pattern: ''
          default: ''
        REMOTEAS:
          name: '对等体AS号'
          type: string
          maxLength: 11
          required: false
          description: ''
          data_source: '参见“5G Core垂直网设LLD文档 > 路由设计 > BGP设计”'
          pattern: ''
          default: ''
        LOCALIFADDR:
          name: '本地接口地址'
          type: string
          maxLength: 39
          required: false
          description: 'VNF的Loopback IP地址及Loopback接口名称。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        LOCALIFNAME:
          name: '本地接口名称'
          type: string
          maxLength: 63
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        EBGPMAXHOP:
          name: 'EBGP最大跳数'
          type: integer
          minimum: 1
          maximum: 255
          required: false
          description: '“EBGP最大跳数”必须不小于到Peer之间的实际跳数。  如最大跳数设置过小，会导致BGP邻居建立失败。'
          data_source: '本端规划'
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
        CONNRETRYTIME:
          name: '重连时间（s）'
          type: integer
          minimum: 1
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 32
        CONVENTIONAL:
          name: '常规路由器'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        DESCRIPTION:
          name: '描述'
          type: string
          maxLength: 80
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        FAKEAS:
          name: '伪AS号'
          type: string
          maxLength: 11
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        FOURBYTEAS:
          name: '4字节AS号功能'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: TRUE
        GROUPNAME:
          name: '组名'
          type: string
          maxLength: 47
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        HOLDTIME:
          name: '保持时间（s）'
          type: integer
          minimum:
          - 0
          - 3
          maximum:
          - 0
          - 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 180
        ISIGNORE:
          name: '是否忽略'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        ISLOGCHANGE:
          name: '是否记录日志'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: TRUE
        KEEPALIVETIME:
          name: '存活时间（s）'
          type: integer
          minimum: 0
          maximum: 21845
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 60
        KEYCHAINNAME:
          name: 'Keychain名称'
          type: string
          maxLength: 47
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PATHMTUDISCOVERY:
          name: '路径MTU发现功能'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        PEERADDRV6:
          name: 'IPv6对等体地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
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
        ROUTEREFRESH:
          name: '路由刷新'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: TRUE
        TRACKINGDELAYTIME:
          name: '邻居断连延迟时间（s）'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 0
        TRACKINGENABLE:
          name: '使能快速感知邻居不可达并断开连接功能'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        VALIDTTLHOPS:
          name: '需要检测的TTL跳数值'
          type: integer
          minimum: 1
          maximum: 256
          required: false
          description: ''
          data_source: ''
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
          data_source: '-'
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
          data_source: '参见“5G Core垂直网设LLD文档 > 路由设计 > BGP设计”'
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
        IMPORTPROCESSID:
          name: '路由进程号'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MED:
          name: 'MED'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 0
    set_dataplanegiinfmode_list:
      type: items
      properties:
        MODE:
          name: '模式'
          type: string
          enum:
          - Group
          - RU
          required: true
          description: '开启下行入不转板功能后，地址池分段，并与ISU pod绑定。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        ROUTEENHANCEDSW:
          name: '路由增强功能开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '路由增强功能：通过VNF和DC-GW配合，减少DC-GW对承载网发布的用户下行路由的条数。   * 该参数值变更（DISABLE->ENABLE、ENABLE->DISABLE）前，需将用户下线。 * 该参数值设置为ENABLE且**ADD AUTOSCALINGBGPLF**命令中的“发布的团体属性（UDADVCOM）”参数不为0时，路由增强功能才会生效。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    mod_bgppeeraf_list:
      type: items
      properties:
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: true
          description: '采用**ADD BGPPEER**命令配置的参数值，可通过**LST BGPPEER**命令获取。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
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
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        REMOTEADDRESS:
          name: 'IPv4对等体地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        ADVERTISECOMMUNITY:
          name: '团体属性发布'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: '开启路由增强功能时，该参数需要设置为“TRUE”。其他场景下，该参数采用默认值即可。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        ADDRESSTYPE:
          name: '地址类型'
          type: string
          enum:
          - ipv4
          - ipv6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ADDPATHMODE:
          name: 'add-path模式'
          type: string
          enum:
          - both
          - 'null'
          - receive
          - send
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ADVADDPATHNUM:
          name: '向邻居发布多少条add-path路由'
          type: integer
          minimum:
          - 0
          - 2
          maximum:
          - 0
          - 64
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ADVBESTEXTERNAL:
          name: '是否发布bestExternal路由'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ADVERTISEEXTCOMMUNITY:
          name: '扩展团体属性发布'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ALLOWASLOOPENABLE:
          name: '允许AS号重复'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ALLOWASLOOPLIMIT:
          name: '允许AS号重复数'
          type: integer
          minimum: 1
          maximum: 10
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DEFAULTRTADVENABLE:
          name: '允许缺省路由通告'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DEFAULTRTADVPOLICY:
          name: '缺省路由通告策略'
          type: string
          maxLength: 200
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DEFAULTRTMATCHMODE:
          name: '带条件匹配缺省路由发布'
          type: string
          enum:
          - matchall
          - matchany
          - 'null'
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DISCARDEXTCOMMUNITY:
          name: '扩展团体属性丢弃'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        EXPORTACL6NAMEORNUM:
          name: '发布路由ACL6规则标识'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        EXPORTACLNAMEORNUM:
          name: '发布路由ACL规则标识'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        EXPORTASPATHFILTER:
          name: '发布路由AS Path过滤'
          type: string
          maxLength: 51
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        EXPORTPREF6FILTNAME:
          name: '发布IPv6前缀过滤策略'
          type: string
          maxLength: 169
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        EXPORTPREFFILTNAME:
          name: '发布前缀过滤策略'
          type: string
          maxLength: 169
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        EXPORTRTPOLICYNAME:
          name: '发布路由策略'
          type: string
          maxLength: 200
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IMPORTACL6NAMEORNUM:
          name: '接收路由ACL6规则标识'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IMPORTACLNAMEORNUM:
          name: '接收路由ACL规则标识'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IMPORTASPATHFILTER:
          name: '接收路由AS Path过滤'
          type: string
          maxLength: 51
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IMPORTPREF6FILTNAME:
          name: '引入IPv6前缀过滤策略'
          type: string
          maxLength: 169
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IMPORTPREFFILTNAME:
          name: '引入前缀过滤策略'
          type: string
          maxLength: 169
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IMPORTRTPOLICYNAME:
          name: '引入路由策略'
          type: string
          maxLength: 200
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        INCLUDEPEERAS:
          name: '不忽略BGP邻居的AS号'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ISSOURELAYNEIGHINTER:
          name: '迭代多源邻居源接口'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        KEEPALLROUTES:
          name: '全局路由更新保存'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NEXTHOPCONFIGURE:
          name: '下一跳处理模式'
          type: string
          enum:
          - invariable
          - local
          - 'null'
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PEERGROUPNAME:
          name: '所属对等体组名称'
          type: string
          maxLength: 47
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PREFERREDVALUE:
          name: '路由首选值'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PUBLICASONLY:
          name: '仅携带公有AS号'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PUBLICASONLYFORCE:
          name: '强制删除私有AS号'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PUBLICASONLYLIMITED:
          name: '删除左边的私有AS号'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PUBLICASONLYREPLACE:
          name: '用本地AS号替换所有的私有AS号'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        REFLECTCLIENT:
          name: '路由反射器客户'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ROUTELIMIT:
          name: '路由超限阈值'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ROUTELIMITIDLETIMEOUT:
          name: '超时定时器（min）'
          type: integer
          minimum: 1
          maximum: 1200
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ROUTELIMITPERCENT:
          name: '路由超限百分比'
          type: integer
          minimum: 1
          maximum: 100
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ROUTELIMITTYPE:
          name: '路由超限告警类型'
          type: string
          enum:
          - alertOnly
          - idleForever
          - idleTimeout
          - noparameter
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RTUPDTINTERVAL:
          name: '路由更新时间（s）'
          type: integer
          minimum: 0
          maximum: 600
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SUBSTITUTEASENABLE:
          name: '替换AS Path属性'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_autoscalingbgplf_list:
      type: items
      properties:
        POLICYNAME:
          name: '策略名称'
          type: string
          maxLength: 31
          required: true
          description: '不同BGPPEER时，该参数必须不同。同一BGPPEER时，该参数必须相同。BGP PEER上不需要配置该参数值。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPVERSION:
          name: 'IP版本'
          type: string
          enum:
          - IPv4
          - IPv6
          required: true
          description: '此处以IPv4为例。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        SERVICENAME:
          name: '服务名称'
          type: string
          maxLength: 31
          required: true
          description: '采用**ADD AUTOSCALINGSERVICE**命令定义的服务名称。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        PEERIP:
          name: 'IP对等体地址'
          type: string
          maxLength: 15
          required: false
          description: 'BGP PEER的IP地址。'
          data_source: '从对端获取'
          pattern: ''
          default: ''
        PEERCOMMUNITY:
          name: '对端团体属性'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: false
          description: '不同BGPPEER时，该参数必须不同。同一BGPPEER时，该参数必须相同。BGP PEER上不需要配置该参数值。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        UDADVCOMENABLE:
          name: '使能发布团体属性开关'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: 'VNF上部署路由增强功能后，DC-GW根据携带的团体属性值（此处配置的“发布的团体属性”值）进行路由过滤。建议先在DC-GW上配置，然后再在VNF上配置。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        UDADVCOM:
          name: '发布的团体属性'
          type: string
          maxLength: 51
          required: false
          description: ''
          data_source: '与对端协商'
          pattern: ''
          default: ''
        PEERIPV6:
          name: 'IP对等体地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_autoscalingipreach_list:
      type: items
      properties:
        SERVICENAME:
          name: '服务名称'
          type: string
          maxLength: 31
          required: true
          description: '采用**ADD AUTOSCALINGSERVICE**命令定义的服务名称。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        IPVERSION:
          name: 'IP版本'
          type: string
          enum:
          - IPv4
          - IPv6
          required: true
          description: '此处以IPv4为例。'
          data_source: '全网规划'
          pattern: ''
          default: IPv4
        DESTADDR4:
          name: '目的地址'
          type: string
          maxLength: 15
          required: false
          description: 'BGP PEER的IP地址。'
          data_source: '从对端获取'
          pattern: ''
          default: ''
        BFDTEMPLATENAME:
          name: 'BFD自动化配置模板名称'
          type: string
          maxLength: 59
          required: true
          description: '本命令绑定的BFD模板，复用**ADD AUTOSCALINGSRROUTE**命令绑定BFD模板。  若**ADD AUTOSCALINGSRROUTE**命令没有绑定BFD模板，则需通过**ADD AUTOSCALINGBFD**命令新增BFD模板配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        DESTADDR6:
          name: '目的地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_dataplaneinfmode_list:
      type: items
      properties:
        MODE:
          name: '模式'
          type: string
          enum:
          - Group
          - Instance
          required: true
          description: '开启入不转板时，必须使用样例值。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        ROUTEENHANCEDSW:
          name: '路由增强功能开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '路由增强功能：通过VNF和DC-GW配合，减少DC-GW对承载网发布的用户下行路由的条数。   * 该参数值变更（DISABLE->ENABLE、ENABLE->DISABLE）前，需将用户下线。 * 该参数值设置为ENABLE且**ADD AUTOSCALINGBGPLF**命令中的“发布的团体属性（UDADVCOM）”参数不为0时，路由增强功能才会生效。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    mod_autoscalingservice_list:
      type: items
      properties:
        SERVICENAME:
          name: '服务名称'
          type: string
          maxLength: 31
          required: true
          description: '采用**ADD AUTOSCALINGSERVICE**命令定义的服务名称。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        ISBACKUP:
          name: '备用路由组标识'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: '“ISBACKUP”设置为“TRUE”时，表示在保护组上生效；“ISBACKUP”设置为“FALSE”时，表示在非保护组上生效。  DC-GW只与保护组内ISU之间建立BFD会话，备路由也只到保护组内ISU的ECMP路由。请根据DC-GW能力规划保护组中ISU POD最大个数，建议将所有ISU都规划到保护组中。  执行**OPR DSPPRTGRPSPEC**命令可查询保护组中ISU POD的最大个数。  当“保护组规格值”取值是“65535”时，“环境变量保护组规格值”参数值就是保护组中ISU POD的最大个数。  当“保护组规格值”取值不是“65535”时，“保护组规格值”参数值就是保护组中ISU POD的最大个数。  执行**DSP POD**命令可查询系统中的ISU POD的个数。  当系统中的所有ISU POD都在保护组中时，仅需要规划“ISBACKUP”值为“TRUE”的接口自动化配置模板。  当系统中的ISU POD个数大于保护组中ISU POD的个数时，需要同时规划“ISBACKUP”值为“TRUE”的接口自动化配置模板和“ISBACKUP”值为“FALSE”的接口自动化配置模板。'
          data_source: '与对端协商'
          pattern: ''
          default: ''
    mod_bgppeeraf_list_2:
      type: items
      properties:
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: true
          description: '采用**ADD BGPPEER**命令配置的参数值，可通过**LST BGPPEER**命令获取。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
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
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        REMOTEADDRESS:
          name: 'IPv4对等体地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        ADVERTISECOMMUNITY:
          name: '团体属性发布'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: '开启路由增强功能时，该参数需要设置为“TRUE”。其他场景下，该参数采用默认值即可。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        ADDRESSTYPE:
          name: '地址类型'
          type: string
          enum:
          - ipv4
          - ipv6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ADDPATHMODE:
          name: 'add-path模式'
          type: string
          enum:
          - both
          - 'null'
          - receive
          - send
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ADVADDPATHNUM:
          name: '向邻居发布多少条add-path路由'
          type: integer
          minimum:
          - 0
          - 2
          maximum:
          - 0
          - 64
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ADVBESTEXTERNAL:
          name: '是否发布bestExternal路由'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ADVERTISEEXTCOMMUNITY:
          name: '扩展团体属性发布'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ALLOWASLOOPENABLE:
          name: '允许AS号重复'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ALLOWASLOOPLIMIT:
          name: '允许AS号重复数'
          type: integer
          minimum: 1
          maximum: 10
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DEFAULTRTADVENABLE:
          name: '允许缺省路由通告'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DEFAULTRTADVPOLICY:
          name: '缺省路由通告策略'
          type: string
          maxLength: 200
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DEFAULTRTMATCHMODE:
          name: '带条件匹配缺省路由发布'
          type: string
          enum:
          - matchall
          - matchany
          - 'null'
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DISCARDEXTCOMMUNITY:
          name: '扩展团体属性丢弃'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        EXPORTACL6NAMEORNUM:
          name: '发布路由ACL6规则标识'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        EXPORTACLNAMEORNUM:
          name: '发布路由ACL规则标识'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        EXPORTASPATHFILTER:
          name: '发布路由AS Path过滤'
          type: string
          maxLength: 51
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        EXPORTPREF6FILTNAME:
          name: '发布IPv6前缀过滤策略'
          type: string
          maxLength: 169
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        EXPORTPREFFILTNAME:
          name: '发布前缀过滤策略'
          type: string
          maxLength: 169
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        EXPORTRTPOLICYNAME:
          name: '发布路由策略'
          type: string
          maxLength: 200
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IMPORTACL6NAMEORNUM:
          name: '接收路由ACL6规则标识'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IMPORTACLNAMEORNUM:
          name: '接收路由ACL规则标识'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IMPORTASPATHFILTER:
          name: '接收路由AS Path过滤'
          type: string
          maxLength: 51
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IMPORTPREF6FILTNAME:
          name: '引入IPv6前缀过滤策略'
          type: string
          maxLength: 169
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IMPORTPREFFILTNAME:
          name: '引入前缀过滤策略'
          type: string
          maxLength: 169
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IMPORTRTPOLICYNAME:
          name: '引入路由策略'
          type: string
          maxLength: 200
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        INCLUDEPEERAS:
          name: '不忽略BGP邻居的AS号'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ISSOURELAYNEIGHINTER:
          name: '迭代多源邻居源接口'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        KEEPALLROUTES:
          name: '全局路由更新保存'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NEXTHOPCONFIGURE:
          name: '下一跳处理模式'
          type: string
          enum:
          - invariable
          - local
          - 'null'
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PEERGROUPNAME:
          name: '所属对等体组名称'
          type: string
          maxLength: 47
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PREFERREDVALUE:
          name: '路由首选值'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PUBLICASONLY:
          name: '仅携带公有AS号'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PUBLICASONLYFORCE:
          name: '强制删除私有AS号'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PUBLICASONLYLIMITED:
          name: '删除左边的私有AS号'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PUBLICASONLYREPLACE:
          name: '用本地AS号替换所有的私有AS号'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        REFLECTCLIENT:
          name: '路由反射器客户'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ROUTELIMIT:
          name: '路由超限阈值'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ROUTELIMITIDLETIMEOUT:
          name: '超时定时器（min）'
          type: integer
          minimum: 1
          maximum: 1200
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ROUTELIMITPERCENT:
          name: '路由超限百分比'
          type: integer
          minimum: 1
          maximum: 100
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ROUTELIMITTYPE:
          name: '路由超限告警类型'
          type: string
          enum:
          - alertOnly
          - idleForever
          - idleTimeout
          - noparameter
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RTUPDTINTERVAL:
          name: '路由更新时间（s）'
          type: integer
          minimum: 0
          maximum: 600
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SUBSTITUTEASENABLE:
          name: '替换AS Path属性'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_autoscalingbgplf_list_2:
      type: items
      properties:
        POLICYNAME:
          name: '策略名称'
          type: string
          maxLength: 31
          required: true
          description: '不同BGPPEER时，该参数必须不同。同一BGPPEER时，该参数必须相同。BGP PEER上不需要配置该参数值。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPVERSION:
          name: 'IP版本'
          type: string
          enum:
          - IPv4
          - IPv6
          required: true
          description: '此处以IPv4为例。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        SERVICENAME:
          name: '服务名称'
          type: string
          maxLength: 31
          required: true
          description: '采用**ADD AUTOSCALINGSERVICE**命令定义的服务名称。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        PEERIP:
          name: 'IP对等体地址'
          type: string
          maxLength: 15
          required: false
          description: 'BGP PEER的IP地址。'
          data_source: '从对端获取'
          pattern: ''
          default: ''
        PEERCOMMUNITY:
          name: '对端团体属性'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: false
          description: '不同BGPPEER时，该参数必须不同。同一BGPPEER时，该参数必须相同。BGP PEER上不需要配置该参数值。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        UDADVCOMENABLE:
          name: '使能发布团体属性开关'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: 'VNF上部署路由增强功能后，DC-GW根据携带的团体属性值（此处配置的“发布的团体属性”值）进行路由过滤。建议先在DC-GW上配置，然后再在VNF上配置。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        UDADVCOM:
          name: '发布的团体属性'
          type: string
          maxLength: 51
          required: false
          description: ''
          data_source: '与对端协商'
          pattern: ''
          default: ''
        PEERIPV6:
          name: 'IP对等体地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_autoscalingipreach_list_2:
      type: items
      properties:
        SERVICENAME:
          name: '服务名称'
          type: string
          maxLength: 31
          required: true
          description: '采用**ADD AUTOSCALINGSERVICE**命令定义的服务名称。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        IPVERSION:
          name: 'IP版本'
          type: string
          enum:
          - IPv4
          - IPv6
          required: true
          description: '此处以IPv4为例。'
          data_source: '全网规划'
          pattern: ''
          default: IPv4
        DESTADDR4:
          name: '目的地址'
          type: string
          maxLength: 15
          required: false
          description: 'BGP PEER的IP地址。'
          data_source: '从对端获取'
          pattern: ''
          default: ''
        BFDTEMPLATENAME:
          name: 'BFD自动化配置模板名称'
          type: string
          maxLength: 59
          required: true
          description: '本命令绑定的BFD模板，复用**ADD AUTOSCALINGSRROUTE**命令绑定BFD模板。  若**ADD AUTOSCALINGSRROUTE**命令没有绑定BFD模板，则需通过**ADD AUTOSCALINGBFD**命令新增BFD模板配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        DESTADDR6:
          name: '目的地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    add_l3vpninst_list:
    - VRFNAME: 'VRF_Access'
    add_vpninstaf_list:
    - VRFNAME: 'VRF_Access'
      AFTYPE: ipv4uni
      VRFRD: '10.10.10.78:100'
    mod_vpninstaf_list:
    - VRFNAME: 'VRF_Access'
      AFTYPE: ipv4uni
      VRFRD: '10.10.10.78:100'
    set_bfd_list:
    - BFDENABLE: TRUE
    set_autoconfig_list:
    - SWITCHFLAG: FALSE
    add_autoscalingethtrunk_list:
    - ETHTRUNKTMPID: 1
      VNICLIST: '4 5'
    add_autoscalingservice_list:
    - SERVICENAME: 'ServName_Access_100_v4'
      VPNNAME: 'VRF_Access'
      AFTYPE: IPv4
      IPALLOCTYPE4: DHCP
      AUTOCFGIFTYPE: VNIC
      VNICID: 4
      VLANID: 100
      NETWORKINSTID: 0
      ETHTRUNKTMPID: 1
      IPALLOCTYPE6: USER_CONFIG
      BEGINADDR4: ''
      ENDADDR4: ''
      MASKLEN: ''
    add_autoscalingservice_list_2:
    - SERVICENAME: 'ServName_Access_100_v4'
      VPNNAME: 'VRF_Access'
      AFTYPE: IPv4
      IPALLOCTYPE4: DHCP
      AUTOCFGIFTYPE: ETHTRUNK
      ETHTRUNKTMPID: 1
      VLANID: 100
      NETWORKINSTID: 0
      VNICID: 4
      IPALLOCTYPE6: USER_CONFIG
      BEGINADDR4: ''
      ENDADDR4: ''
      MASKLEN: ''
    add_autoscalingbfd_list:
    - TEMPLATENAME: 'BFD_1'
      BFDTYPE: Static
      SERVICENAME: 'ServName_Access_100_v4'
      IPVERSION: IPv4
      DESTADDR4: '10.10.85.130'
      MINECHORXINT: 500
      DETECTMULTI: 4
      ONEARMECHO: TRUE
      MINRXINTERVAL: 200
      MINTXINTERVAL: 200
      DESTADDR6: ''
    add_autoscalingsrroute_list:
    - SERVICENAME: 'ServName_Access_100_v4'
      VRFNAME: 'VRF_Access'
      IPVERSION: IPv4
      PREFIX4: '10.10.20.78'
      MASKLENGTH: 32
      NEXTHOPALLOCTYPE4: DHCP
      PREFERENCE: 60
      BFDENABLE: TRUE
      BFDTEMPLATENAME: 'BFD_1'
      NEXTHOPALLOCTYPE6: CONFIG
      PREFIX6: ''
      NEXTHOP4: ''
    set_autoconfig_list_1:
    - SWITCHFLAG: TRUE
    set_bgp_list:
    - BGPENABLE: TRUE
      ASNUM: '60001'
      ASPATHLIMIT: ''
      BGPRIDAUTOSEL: ''
      CHECKFIRSTAS: ''
      CONFEDIDNUMBER: ''
      CONFEDNONSTANDED: ''
      GRACEFULRESTART: ''
      GRPEERRESET: ''
      ISSHUTDOWN: ''
      KEEPALLROUTES: ''
      MEMORYLIMIT: ''
      TIMEWAITFORRIB: ''
    add_interface_list:
    - IFNAME: 'Loopback1'
    add_ipbindvpn_list:
    - IFNAME: 'Loopback1'
      VRFNAME: 'VRF_Access'
    add_ifipv4address_list:
    - IFNAME: 'Loopback1'
      IFIPADDR: '10.10.10.78'
      SUBNETMASK: '255.255.255.255'
    add_bgpvrf_list:
    - VRFNAME: 'VRF_Access'
      DEFAULTAFTYPE: noaf
      ROUTERID: '10.10.10.78'
    add_bgpvrfaf_list:
    - VRFNAME: 'VRF_Access'
      AFTYPE: ipv4uni
      MAXIMUMLOADBALANCE: 2
      ACTIVEROUTEADVERTISE: FALSE
      ADDPATHSELNUM: ''
      ALWAYSCOMPAREMED: FALSE
      APPLYLABELMODE: perRoute
      ASPATHIGNORE: FALSE
      AUTOFRRENABLE: FALSE
      AUTOMATICSUMMARY: FALSE
      BESTEXTERNAL: FALSE
      DEFAULTLOCALPREF: 100
      DEFAULTMED: ''
      DEFAULTRTIMPORTENABLE: FALSE
      DETERMINMED: FALSE
      EBGPECMPNEXTHOPCHANGED: FALSE
      EBGPIFSENSITIVE: TRUE
      ECMPNEXTHOPCHANGED: FALSE
      EIBGPEXTHOPCHANGED: FALSE
      EIBGPLOADBALANCE: ''
      IBGPECMPNEXTHOPCHANGED: FALSE
      IBGPIFSENSITIVE: FALSE
      IGPMETRICIGNORE: FALSE
      LOADASPATHIGNORE: FALSE
      MAXLOADEBGPNUM: 1
      MAXLOADIBGPNUM: 1
      MEDCONFED: FALSE
      MEDNONEASMAXIMUM: FALSE
      NEXTHOPSELDEPENDTYPE: dependIp
      NHPRELAYROUTEPOLICYNAME: ''
      ORIGINATORPRIOR: FALSE
      POLICYEXTCOMMENABLE: FALSE
      POLICYVPNTARGET: TRUE
      PREFERENCEEXTERNAL: 255
      PREFERENCEINTERNAL: 255
      PREFERENCELOCAL: 255
      PREFERENCEPOLICYNAME: ''
      REFLECTBETWEENCLIENT: TRUE
      REFLECTCHGPATH: FALSE
      REFLECTORCLUSTERID: ''
      REFLECTORCLUSTERIPV4: ''
      RELAYDELAYENABLE: TRUE
      ROUTERID: ''
      ROUTERIDNEGLECT: FALSE
      ROUTESELECTDELAY: ''
      RRFILTERNUMBER: ''
      SUPERNETUNIADV: FALSE
      TNLSELECTORNAME: ''
      VRFRIDAUTOSEL: FALSE
    add_bgppeer_list:
    - VRFNAME: 'VRF_Access'
      ADDRESSTYPE: ipv4
      PEERADDR: '10.10.20.78'
      REMOTEAS: '60002'
      LOCALIFADDR: '10.10.10.78'
      LOCALIFNAME: 'Loopback1'
      EBGPMAXHOP: 10
      CONNECTMODE: 'null'
      CONNRETRYTIME: 32
      CONVENTIONAL: FALSE
      DESCRIPTION: ''
      FAKEAS: ''
      FOURBYTEAS: TRUE
      GROUPNAME: ''
      HOLDTIME: 180
      ISIGNORE: FALSE
      ISLOGCHANGE: TRUE
      KEEPALIVETIME: 60
      KEYCHAINNAME: ''
      PATHMTUDISCOVERY: FALSE
      PEERADDRV6: ''
      PSWDTYPE: 'null'
      ROUTEREFRESH: TRUE
      TRACKINGDELAYTIME: ''
      TRACKINGENABLE: FALSE
      VALIDTTLHOPS: ''
    add_importroute_list:
    - VRFNAME: 'VRF_Access'
      AFTYPE: ipv4uni
      IMPORTPROTOCOL: wlr
      MEDENABLE: FALSE
      IMPORTPROCESSID: ''
      MED: ''
    set_dataplanegiinfmode_list:
    - MODE: RU
      ROUTEENHANCEDSW: ENABLE
    mod_bgppeeraf_list:
    - VRFNAME: 'VRF_Access'
      AFTYPE: ipv4uni
      REMOTEADDRESS: '10.10.20.78'
      ADVERTISECOMMUNITY: TRUE
      ADDRESSTYPE: ''
      ADDPATHMODE: ''
      ADVADDPATHNUM: ''
      ADVBESTEXTERNAL: ''
      ADVERTISEEXTCOMMUNITY: ''
      ALLOWASLOOPENABLE: ''
      ALLOWASLOOPLIMIT: ''
      DEFAULTRTADVENABLE: ''
      DEFAULTRTADVPOLICY: ''
      DEFAULTRTMATCHMODE: ''
      DISCARDEXTCOMMUNITY: ''
      EXPORTACL6NAMEORNUM: ''
      EXPORTACLNAMEORNUM: ''
      EXPORTASPATHFILTER: ''
      EXPORTPREF6FILTNAME: ''
      EXPORTPREFFILTNAME: ''
      EXPORTRTPOLICYNAME: ''
      IMPORTACL6NAMEORNUM: ''
      IMPORTACLNAMEORNUM: ''
      IMPORTASPATHFILTER: ''
      IMPORTPREF6FILTNAME: ''
      IMPORTPREFFILTNAME: ''
      IMPORTRTPOLICYNAME: ''
      INCLUDEPEERAS: ''
      ISSOURELAYNEIGHINTER: ''
      KEEPALLROUTES: ''
      NEXTHOPCONFIGURE: ''
      PEERGROUPNAME: ''
      PREFERREDVALUE: ''
      PUBLICASONLY: ''
      PUBLICASONLYFORCE: ''
      PUBLICASONLYLIMITED: ''
      PUBLICASONLYREPLACE: ''
      REFLECTCLIENT: ''
      ROUTELIMIT: ''
      ROUTELIMITIDLETIMEOUT: ''
      ROUTELIMITPERCENT: ''
      ROUTELIMITTYPE: ''
      RTUPDTINTERVAL: ''
      SUBSTITUTEASENABLE: ''
    add_autoscalingbgplf_list:
    - POLICYNAME: 'bgppolicy1_v4'
      IPVERSION: IPv4
      SERVICENAME: 'ServName_Access_100_v4'
      PEERIP: '10.10.20.78'
      PEERCOMMUNITY: 1
      UDADVCOMENABLE: TRUE
      UDADVCOM: '200'
      PEERIPV6: ''
    add_autoscalingipreach_list:
    - SERVICENAME: 'ServName_Access_100_v4'
      IPVERSION: IPv4
      DESTADDR4: '10.10.20.78'
      BFDTEMPLATENAME: 'BFD_1'
      DESTADDR6: ''
    set_dataplaneinfmode_list:
    - MODE: Instance
      ROUTEENHANCEDSW: ENABLE
    mod_autoscalingservice_list:
    - SERVICENAME: 'ServName_Access_100_v4'
      ISBACKUP: TRUE
    mod_bgppeeraf_list_2:
    - VRFNAME: 'VRF_Access'
      AFTYPE: ipv4uni
      REMOTEADDRESS: '10.10.20.78'
      ADVERTISECOMMUNITY: TRUE
      ADDRESSTYPE: ''
      ADDPATHMODE: ''
      ADVADDPATHNUM: ''
      ADVBESTEXTERNAL: ''
      ADVERTISEEXTCOMMUNITY: ''
      ALLOWASLOOPENABLE: ''
      ALLOWASLOOPLIMIT: ''
      DEFAULTRTADVENABLE: ''
      DEFAULTRTADVPOLICY: ''
      DEFAULTRTMATCHMODE: ''
      DISCARDEXTCOMMUNITY: ''
      EXPORTACL6NAMEORNUM: ''
      EXPORTACLNAMEORNUM: ''
      EXPORTASPATHFILTER: ''
      EXPORTPREF6FILTNAME: ''
      EXPORTPREFFILTNAME: ''
      EXPORTRTPOLICYNAME: ''
      IMPORTACL6NAMEORNUM: ''
      IMPORTACLNAMEORNUM: ''
      IMPORTASPATHFILTER: ''
      IMPORTPREF6FILTNAME: ''
      IMPORTPREFFILTNAME: ''
      IMPORTRTPOLICYNAME: ''
      INCLUDEPEERAS: ''
      ISSOURELAYNEIGHINTER: ''
      KEEPALLROUTES: ''
      NEXTHOPCONFIGURE: ''
      PEERGROUPNAME: ''
      PREFERREDVALUE: ''
      PUBLICASONLY: ''
      PUBLICASONLYFORCE: ''
      PUBLICASONLYLIMITED: ''
      PUBLICASONLYREPLACE: ''
      REFLECTCLIENT: ''
      ROUTELIMIT: ''
      ROUTELIMITIDLETIMEOUT: ''
      ROUTELIMITPERCENT: ''
      ROUTELIMITTYPE: ''
      RTUPDTINTERVAL: ''
      SUBSTITUTEASENABLE: ''
    add_autoscalingbgplf_list_2:
    - POLICYNAME: 'bgppolicy1_v4'
      IPVERSION: IPv4
      SERVICENAME: 'ServName_Access_100_v4'
      PEERIP: '10.10.20.78'
      PEERCOMMUNITY: 1
      UDADVCOMENABLE: TRUE
      UDADVCOM: '200'
      PEERIPV6: ''
    add_autoscalingipreach_list_2:
    - SERVICENAME: 'ServName_Access_100_v4'
      IPVERSION: IPv4
      DESTADDR4: '10.10.20.78'
      BFDTEMPLATENAME: 'BFD_1'
      DESTADDR6: ''
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 配置外联口的VPN实例。

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
    {#- --- 可选参数 --- -#}
    {%- if item.VRFRD is not none -%}
        VRFRD="{{item.VRFRD}}",
    {%- endif -%}
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

### 一条通信路径上所有节点绑定的VPN实例要一致，才能正常通信，例如VNF逻辑接口、VNF外联口、BGP相关的VPN，否则从逻辑接口发出去的报文会查询路由失败。

### 2 全局激活BFD。

```jinja2
{%- for item in set_bfd_list -%}
    SET BFD:
    {#- --- 必选参数 --- -#}
    BFDENABLE={{item.BFDENABLE}},
    ;
{%- endfor -%}
```

### 3 关闭自动配置开关。

#### 3.1 查询自动配置开关。

#### 如果“自动配置开关”值为“TRUE”，需要执行3.b和3.c关闭自动配置开关。

#### 如果“自动配置开关”值为“FALSE”，说明已关闭自动配置开关，请跳转到步骤 4。

#### 3.2 查询自动部署维护助手“autoscaling\_autoconfig.py”的状态，确保状态为“准备好状态（Ready）”或者查询无该脚本，以保证当前设备不在自动部署过程中。因为若系统当前有正在进行的自动部署，而自动部署生效有时延，此时若关闭自动配置开关，会影响系统配置效果。

#### 3.3 关闭自动配置开关。自动化配置命令只有在自动配置开关为关闭的状态下才可执行，因此需要提前关闭。

```jinja2
{%- set LST_AUTOCONFIG=getParameterValue('LST AUTOCONFIG') -%}
{%- if LST_AUTOCONFIG=='TRUE' -%}
    {%- for item in set_autoconfig_list -%}
        SET AUTOCONFIG:
        {#- --- 必选参数 --- -#}
        SWITCHFLAG={{item.SWITCHFLAG}},
        ;
    {%- endfor -%}
{%- endif -%}
```

### 4 接口采用SR-IOV bonding组网时，添加以太网隧道多虚拟网卡自动化配置模板。

```jinja2
{%- if is_scenario_sriov_bonding -%}
    {%- for item in add_autoscalingethtrunk_list -%}
        ADD AUTOSCALINGETHTRUNK:
        {#- --- 必选参数 --- -#}
        ETHTRUNKTMPID={{item.ETHTRUNKTMPID}},
        VNICLIST="{{item.VNICLIST}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

### 在SR-IOV Bonding组网场景下，必须配置该模板。非SR-IOV bonding组网场景下，请跳过本步骤。

### 如果要实现SR-IOV接口bonding功能，那么一个Eth-trunk接口下的两个成员接口必须MAC相同，且ID号连续。即：“VNICLIST”中配置的ID号为MAC相同且连续的两个以太网接口的ID。可使用**LST INTERFACE**命令查询以太网接口的mac地址与以太网接口名称。

### 5 配置外联口自动部署模板。

#### 5.1 非SR-IOV bonding组网场景下：

```jinja2
{%- if is_scenario_non_sriov_bonding -%}
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
        {%- if item.NETWORKINSTID is not none -%}
            NETWORKINSTID={{item.NETWORKINSTID}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：AUTOCFGIFTYPE=VNIC 时必选 --- -#}
        {%- if item.AUTOCFGIFTYPE == 'VNIC' -%}
            VNICID={{item.VNICID}},
        {%- endif -%}
        {#- --- 条件必选：IPALLOCTYPE4=USER_CONFIG 时必选 --- -#}
        {%- if item.IPALLOCTYPE4 == 'USER_CONFIG' -%}
            BEGINADDR4="{{item.BEGINADDR4}}",
        {%- endif -%}
        {#- --- 条件必选：IPALLOCTYPE4=USER_CONFIG 时必选 --- -#}
        {%- if item.IPALLOCTYPE4 == 'USER_CONFIG' -%}
            ENDADDR4="{{item.ENDADDR4}}",
        {%- endif -%}
        {#- --- 条件必选：AUTOCFGIFTYPE=ETHTRUNK 时必选 --- -#}
        {%- if item.AUTOCFGIFTYPE == 'ETHTRUNK' -%}
            ETHTRUNKTMPID={{item.ETHTRUNKTMPID}},
        {%- endif -%}
        {#- --- 条件必选：IPALLOCTYPE4=USER_CONFIG 时必选 --- -#}
        {%- if item.IPALLOCTYPE4 == 'USER_CONFIG' -%}
            MASKLEN={{item.MASKLEN}},
        {#- --- 条件必选：IPALLOCTYPE6=USER_CONFIG 时必选 --- -#}
        {%- elif item.IPALLOCTYPE6 == 'USER_CONFIG' -%}
            MASKLEN={{item.MASKLEN}},
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
{%- endif -%}
```

#### 5.2 SR-IOV bonding组网场景下：

```jinja2
{%- if is_scenario_sriov_bonding -%}
    {%- for item in add_autoscalingservice_list_2 -%}
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
        {%- if item.NETWORKINSTID is not none -%}
            NETWORKINSTID={{item.NETWORKINSTID}},
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
        {#- --- 条件必选：AUTOCFGIFTYPE=VNIC 时必选 --- -#}
        {%- if item.AUTOCFGIFTYPE == 'VNIC' -%}
            VNICID={{item.VNICID}},
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
{%- endif -%}
```

### 6 增加BFD会话自动部署模板。

### “DESTADDR4”配置的是Leaf节点的IP地址，采用的是单臂BFD。

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
    {#- --- 条件可选：BFDTYPE=Dynamic 时可选 --- -#}
    {%- if item.BFDTYPE == 'Dynamic' -%}
        {%- if item.MINRXINTERVAL is not none -%}
            MINRXINTERVAL={{item.MINRXINTERVAL}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：BFDTYPE=Dynamic 时可选 --- -#}
    {%- if item.BFDTYPE == 'Dynamic' -%}
        {%- if item.MINTXINTERVAL is not none -%}
            MINTXINTERVAL={{item.MINTXINTERVAL}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 7 增加静态路由自动部署模板。

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
    {#- --- 条件必选：NEXTHOPALLOCTYPE4=CONFIG 时必选 --- -#}
    {%- if item.NEXTHOPALLOCTYPE4 == 'CONFIG' -%}
        NEXTHOP4="{{item.NEXTHOP4}}",
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

### 8 打开自动部署开关。

```jinja2
{%- for item in set_autoconfig_list_1 -%}
    SET AUTOCONFIG:
    {#- --- 必选参数 --- -#}
    SWITCHFLAG={{item.SWITCHFLAG}},
    ;
{%- endfor -%}
```

### 9 全局激活BGP。

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
    {#- --- 条件可选：BGPENABLE=TRUE 时可选 --- -#}
    {%- if item.BGPENABLE == 'TRUE' -%}
        {%- if item.ASPATHLIMIT is not none -%}
            ASPATHLIMIT={{item.ASPATHLIMIT}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：BGPENABLE=TRUE 时可选 --- -#}
    {%- if item.BGPENABLE == 'TRUE' -%}
        {%- if item.BGPRIDAUTOSEL is not none -%}
            BGPRIDAUTOSEL={{item.BGPRIDAUTOSEL}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：BGPENABLE=TRUE 时可选 --- -#}
    {%- if item.BGPENABLE == 'TRUE' -%}
        {%- if item.CHECKFIRSTAS is not none -%}
            CHECKFIRSTAS={{item.CHECKFIRSTAS}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：BGPENABLE=TRUE 时可选 --- -#}
    {%- if item.BGPENABLE == 'TRUE' -%}
        {%- if item.CONFEDIDNUMBER is not none -%}
            CONFEDIDNUMBER="{{item.CONFEDIDNUMBER}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：BGPENABLE=TRUE 时可选 --- -#}
    {%- if item.BGPENABLE == 'TRUE' -%}
        {%- if item.CONFEDNONSTANDED is not none -%}
            CONFEDNONSTANDED={{item.CONFEDNONSTANDED}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：BGPENABLE=TRUE 时可选 --- -#}
    {%- if item.BGPENABLE == 'TRUE' -%}
        {%- if item.GRACEFULRESTART is not none -%}
            GRACEFULRESTART={{item.GRACEFULRESTART}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：BGPENABLE=TRUE 时可选 --- -#}
    {%- if item.BGPENABLE == 'TRUE' -%}
        {%- if item.GRPEERRESET is not none -%}
            GRPEERRESET={{item.GRPEERRESET}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：BGPENABLE=TRUE 时可选 --- -#}
    {%- if item.BGPENABLE == 'TRUE' -%}
        {%- if item.ISSHUTDOWN is not none -%}
            ISSHUTDOWN={{item.ISSHUTDOWN}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：BGPENABLE=TRUE 时可选 --- -#}
    {%- if item.BGPENABLE == 'TRUE' -%}
        {%- if item.KEEPALLROUTES is not none -%}
            KEEPALLROUTES={{item.KEEPALLROUTES}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：BGPENABLE=TRUE 时可选 --- -#}
    {%- if item.BGPENABLE == 'TRUE' -%}
        {%- if item.MEMORYLIMIT is not none -%}
            MEMORYLIMIT={{item.MEMORYLIMIT}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：BGPENABLE=TRUE 时可选 --- -#}
    {%- if item.BGPENABLE == 'TRUE' -%}
        {%- if item.TIMEWAITFORRIB is not none -%}
            TIMEWAITFORRIB={{item.TIMEWAITFORRIB}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### “ASNUM”参数若需要变更，则需先去使能BGP功能。去使能BGP时，BGP VPN实例等配置会被同步删除。必须按照LLD规划的“ASNUM”值进行配置。

### 10 配置Loopback接口地址（BGP本端IP）。

#### 10.1 配置Loopback接口。

```jinja2
{%- for item in add_interface_list -%}
    ADD INTERFACE:
    {#- --- 必选参数 --- -#}
    IFNAME="{{item.IFNAME}}",
    ;
{%- endfor -%}
```

#### 10.2 配置接口绑定VPN。

```jinja2
{%- for item in add_ipbindvpn_list -%}
    ADD IPBINDVPN:
    {#- --- 必选参数 --- -#}
    IFNAME="{{item.IFNAME}}",
    VRFNAME="{{item.VRFNAME}}",
    ;
{%- endfor -%}
```

#### 10.3 配置接口IP地址。

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

### 11 配置BGP。

#### 11.1 增加BGP VPN实例。

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

#### 此处配置的“ROUTERID”是BGP VPN实例级别的ROUTERID。

#### IPv4v6双栈时，IPv4 BGP VPN实例地址族和IPv6 BGP VPN实例地址族共用此处配置的“ROUTERID”值。

#### 已配置IPv4v6双栈的BGP VPN实例地址族，若需删除IPv4的BGP VPN实例地址族配置，则：

#### 1、删除IPv4的配置前需查询并记录“ROUTERID”值。

#### 2、删除IPv4的配置后需查询“ROUTERID”值是否存在，若不存在则需通过**MOD BGPVRF**命令将“ROUTERID”参数设置为删除IPv4的配置前记录的“ROUTERID”值。否则IPv6 BGP重新协商时会因无“ROUTERID”值可用而导致协商失败。

#### 11.2 增加BGP VPN地址族。VNF对接2个负荷分担的BGP邻居时，“MAXIMUMLOADBALANCE”设置为“2”。

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
    {#- --- 条件可选：AFTYPE=ipv4uni/ipv6uni 时可选 --- -#}
    {%- if item.AFTYPE in ['ipv4uni', 'ipv6uni'] -%}
        {%- if item.ACTIVEROUTEADVERTISE is not none -%}
            ACTIVEROUTEADVERTISE={{item.ACTIVEROUTEADVERTISE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：AFTYPE=ipv4vpn/ipv6vpn/ipv4uni/ipv6uni 时可选 --- -#}
    {%- if item.AFTYPE in ['ipv4vpn', 'ipv6vpn', 'ipv4uni', 'ipv6uni'] -%}
        {%- if item.ADDPATHSELNUM is not none -%}
            ADDPATHSELNUM={{item.ADDPATHSELNUM}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：AFTYPE=ipv4uni/ipv6uni 时可选 --- -#}
    {%- if item.AFTYPE in ['ipv4uni', 'ipv6uni'] -%}
        {%- if item.ALWAYSCOMPAREMED is not none -%}
            ALWAYSCOMPAREMED={{item.ALWAYSCOMPAREMED}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：AFTYPE=ipv4vpn/ipv6vpn 时可选 --- -#}
    {%- if item.AFTYPE in ['ipv4vpn', 'ipv6vpn'] -%}
        {%- if item.APPLYLABELMODE is not none -%}
            APPLYLABELMODE={{item.APPLYLABELMODE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：AFTYPE=ipv4uni/ipv6uni 时可选 --- -#}
    {%- if item.AFTYPE in ['ipv4uni', 'ipv6uni'] -%}
        {%- if item.ASPATHIGNORE is not none -%}
            ASPATHIGNORE={{item.ASPATHIGNORE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：AFTYPE=ipv4vpn/ipv4uni/ipv6uni 时可选 --- -#}
    {%- if item.AFTYPE in ['ipv4vpn', 'ipv4uni', 'ipv6uni'] -%}
        {%- if item.AUTOFRRENABLE is not none -%}
            AUTOFRRENABLE={{item.AUTOFRRENABLE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：AFTYPE=ipv4uni 时可选 --- -#}
    {%- if item.AFTYPE == 'ipv4uni' -%}
        {%- if item.AUTOMATICSUMMARY is not none -%}
            AUTOMATICSUMMARY={{item.AUTOMATICSUMMARY}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：AFTYPE=ipv4vpn/ipv6vpn/ipv4uni/ipv6uni 时可选 --- -#}
    {%- if item.AFTYPE in ['ipv4vpn', 'ipv6vpn', 'ipv4uni', 'ipv6uni'] -%}
        {%- if item.BESTEXTERNAL is not none -%}
            BESTEXTERNAL={{item.BESTEXTERNAL}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：AFTYPE=ipv4vpn/ipv6vpn/ipv4uni/ipv6uni 时可选 --- -#}
    {%- if item.AFTYPE in ['ipv4vpn', 'ipv6vpn', 'ipv4uni', 'ipv6uni'] -%}
        {%- if item.DEFAULTLOCALPREF is not none -%}
            DEFAULTLOCALPREF={{item.DEFAULTLOCALPREF}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：AFTYPE=ipv4vpn/ipv6vpn/ipv4uni/ipv6uni 时可选 --- -#}
    {%- if item.AFTYPE in ['ipv4vpn', 'ipv6vpn', 'ipv4uni', 'ipv6uni'] -%}
        {%- if item.DEFAULTMED is not none -%}
            DEFAULTMED={{item.DEFAULTMED}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：AFTYPE=ipv4uni/ipv6uni 时可选 --- -#}
    {%- if item.AFTYPE in ['ipv4uni', 'ipv6uni'] -%}
        {%- if item.DEFAULTRTIMPORTENABLE is not none -%}
            DEFAULTRTIMPORTENABLE={{item.DEFAULTRTIMPORTENABLE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：AFTYPE=ipv4uni/ipv6uni 时可选 --- -#}
    {%- if item.AFTYPE in ['ipv4uni', 'ipv6uni'] -%}
        {%- if item.DETERMINMED is not none -%}
            DETERMINMED={{item.DETERMINMED}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：AFTYPE=ipv4uni/ipv6uni 时可选 --- -#}
    {%- if item.AFTYPE in ['ipv4uni', 'ipv6uni'] -%}
        {%- if item.EBGPECMPNEXTHOPCHANGED is not none -%}
            EBGPECMPNEXTHOPCHANGED={{item.EBGPECMPNEXTHOPCHANGED}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：AFTYPE=ipv4uni/ipv6uni 时可选 --- -#}
    {%- if item.AFTYPE in ['ipv4uni', 'ipv6uni'] -%}
        {%- if item.EBGPIFSENSITIVE is not none -%}
            EBGPIFSENSITIVE={{item.EBGPIFSENSITIVE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：AFTYPE=ipv4uni/ipv6uni 时可选 --- -#}
    {%- if item.AFTYPE in ['ipv4uni', 'ipv6uni'] -%}
        {%- if item.ECMPNEXTHOPCHANGED is not none -%}
            ECMPNEXTHOPCHANGED={{item.ECMPNEXTHOPCHANGED}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：AFTYPE=ipv4uni/ipv6uni 时可选 --- -#}
    {%- if item.AFTYPE in ['ipv4uni', 'ipv6uni'] -%}
        {%- if item.EIBGPEXTHOPCHANGED is not none -%}
            EIBGPEXTHOPCHANGED={{item.EIBGPEXTHOPCHANGED}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：AFTYPE=ipv4uni/ipv6uni 时可选 --- -#}
    {%- if item.AFTYPE in ['ipv4uni', 'ipv6uni'] -%}
        {%- if item.EIBGPLOADBALANCE is not none -%}
            EIBGPLOADBALANCE={{item.EIBGPLOADBALANCE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：AFTYPE=ipv4uni/ipv6uni 时可选 --- -#}
    {%- if item.AFTYPE in ['ipv4uni', 'ipv6uni'] -%}
        {%- if item.IBGPECMPNEXTHOPCHANGED is not none -%}
            IBGPECMPNEXTHOPCHANGED={{item.IBGPECMPNEXTHOPCHANGED}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：AFTYPE=ipv4uni/ipv6uni 时可选 --- -#}
    {%- if item.AFTYPE in ['ipv4uni', 'ipv6uni'] -%}
        {%- if item.IBGPIFSENSITIVE is not none -%}
            IBGPIFSENSITIVE={{item.IBGPIFSENSITIVE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：AFTYPE=ipv4vpn/ipv6vpn/ipv4uni/ipv6uni 时可选 --- -#}
    {%- if item.AFTYPE in ['ipv4vpn', 'ipv6vpn', 'ipv4uni', 'ipv6uni'] -%}
        {%- if item.IGPMETRICIGNORE is not none -%}
            IGPMETRICIGNORE={{item.IGPMETRICIGNORE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：AFTYPE=ipv4uni/ipv6uni 时可选 --- -#}
    {%- if item.AFTYPE in ['ipv4uni', 'ipv6uni'] -%}
        {%- if item.LOADASPATHIGNORE is not none -%}
            LOADASPATHIGNORE={{item.LOADASPATHIGNORE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：AFTYPE=ipv4uni/ipv6uni 时可选 --- -#}
    {%- if item.AFTYPE in ['ipv4uni', 'ipv6uni'] -%}
        {%- if item.MAXLOADEBGPNUM is not none -%}
            MAXLOADEBGPNUM={{item.MAXLOADEBGPNUM}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：AFTYPE=ipv4uni/ipv6uni 时可选 --- -#}
    {%- if item.AFTYPE in ['ipv4uni', 'ipv6uni'] -%}
        {%- if item.MAXLOADIBGPNUM is not none -%}
            MAXLOADIBGPNUM={{item.MAXLOADIBGPNUM}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：AFTYPE=ipv4uni/ipv6uni 时可选 --- -#}
    {%- if item.AFTYPE in ['ipv4uni', 'ipv6uni'] -%}
        {%- if item.MEDCONFED is not none -%}
            MEDCONFED={{item.MEDCONFED}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：AFTYPE=ipv4uni/ipv6uni 时可选 --- -#}
    {%- if item.AFTYPE in ['ipv4uni', 'ipv6uni'] -%}
        {%- if item.MEDNONEASMAXIMUM is not none -%}
            MEDNONEASMAXIMUM={{item.MEDNONEASMAXIMUM}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：AFTYPE=ipv4vpn/ipv6vpn 时可选 --- -#}
    {%- if item.AFTYPE in ['ipv4vpn', 'ipv6vpn'] -%}
        {%- if item.NEXTHOPSELDEPENDTYPE is not none -%}
            NEXTHOPSELDEPENDTYPE={{item.NEXTHOPSELDEPENDTYPE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：AFTYPE=ipv4vpn/ipv6vpn/ipv4uni/ipv6uni 时可选 --- -#}
    {%- if item.AFTYPE in ['ipv4vpn', 'ipv6vpn', 'ipv4uni', 'ipv6uni'] -%}
        {%- if item.NHPRELAYROUTEPOLICYNAME is not none -%}
            NHPRELAYROUTEPOLICYNAME="{{item.NHPRELAYROUTEPOLICYNAME}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：AFTYPE=ipv4vpn/ipv6vpn/ipv4uni/ipv6uni 时可选 --- -#}
    {%- if item.AFTYPE in ['ipv4vpn', 'ipv6vpn', 'ipv4uni', 'ipv6uni'] -%}
        {%- if item.ORIGINATORPRIOR is not none -%}
            ORIGINATORPRIOR={{item.ORIGINATORPRIOR}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：AFTYPE=ipv4uni/ipv6uni 时可选 --- -#}
    {%- if item.AFTYPE in ['ipv4uni', 'ipv6uni'] -%}
        {%- if item.POLICYEXTCOMMENABLE is not none -%}
            POLICYEXTCOMMENABLE={{item.POLICYEXTCOMMENABLE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：AFTYPE=ipv4vpn/ipv6vpn 时可选 --- -#}
    {%- if item.AFTYPE in ['ipv4vpn', 'ipv6vpn'] -%}
        {%- if item.POLICYVPNTARGET is not none -%}
            POLICYVPNTARGET={{item.POLICYVPNTARGET}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：AFTYPE=ipv4uni/ipv6uni 时可选 --- -#}
    {%- if item.AFTYPE in ['ipv4uni', 'ipv6uni'] -%}
        {%- if item.PREFERENCEEXTERNAL is not none -%}
            PREFERENCEEXTERNAL={{item.PREFERENCEEXTERNAL}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：AFTYPE=ipv4uni/ipv6uni 时可选 --- -#}
    {%- if item.AFTYPE in ['ipv4uni', 'ipv6uni'] -%}
        {%- if item.PREFERENCEINTERNAL is not none -%}
            PREFERENCEINTERNAL={{item.PREFERENCEINTERNAL}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：AFTYPE=ipv4uni/ipv6uni 时可选 --- -#}
    {%- if item.AFTYPE in ['ipv4uni', 'ipv6uni'] -%}
        {%- if item.PREFERENCELOCAL is not none -%}
            PREFERENCELOCAL={{item.PREFERENCELOCAL}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：AFTYPE=ipv4uni/ipv6uni 时可选 --- -#}
    {%- if item.AFTYPE in ['ipv4uni', 'ipv6uni'] -%}
        {%- if item.PREFERENCEPOLICYNAME is not none -%}
            PREFERENCEPOLICYNAME="{{item.PREFERENCEPOLICYNAME}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：AFTYPE=ipv4vpn/ipv6vpn/ipv4uni/ipv6uni 时可选 --- -#}
    {%- if item.AFTYPE in ['ipv4vpn', 'ipv6vpn', 'ipv4uni', 'ipv6uni'] -%}
        {%- if item.REFLECTBETWEENCLIENT is not none -%}
            REFLECTBETWEENCLIENT={{item.REFLECTBETWEENCLIENT}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：AFTYPE=ipv4vpn/ipv6vpn/ipv4uni/ipv6uni 时可选 --- -#}
    {%- if item.AFTYPE in ['ipv4vpn', 'ipv6vpn', 'ipv4uni', 'ipv6uni'] -%}
        {%- if item.REFLECTCHGPATH is not none -%}
            REFLECTCHGPATH={{item.REFLECTCHGPATH}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：AFTYPE=ipv4vpn/ipv6vpn/ipv4uni/ipv6uni 时可选 --- -#}
    {%- if item.AFTYPE in ['ipv4vpn', 'ipv6vpn', 'ipv4uni', 'ipv6uni'] -%}
        {%- if item.REFLECTORCLUSTERID is not none -%}
            REFLECTORCLUSTERID={{item.REFLECTORCLUSTERID}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：AFTYPE=ipv4vpn/ipv6vpn/ipv4uni/ipv6uni 时可选 --- -#}
    {%- if item.AFTYPE in ['ipv4vpn', 'ipv6vpn', 'ipv4uni', 'ipv6uni'] -%}
        {%- if item.REFLECTORCLUSTERIPV4 is not none -%}
            REFLECTORCLUSTERIPV4="{{item.REFLECTORCLUSTERIPV4}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：AFTYPE=ipv4vpn/ipv6vpn/ipv4uni/ipv6uni 时可选 --- -#}
    {%- if item.AFTYPE in ['ipv4vpn', 'ipv6vpn', 'ipv4uni', 'ipv6uni'] -%}
        {%- if item.RELAYDELAYENABLE is not none -%}
            RELAYDELAYENABLE={{item.RELAYDELAYENABLE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：AFTYPE=ipv4uni/ipv6uni 时可选 --- -#}
    {%- if item.AFTYPE in ['ipv4uni', 'ipv6uni'] -%}
        {%- if item.ROUTERID is not none -%}
            ROUTERID="{{item.ROUTERID}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：AFTYPE=ipv4uni/ipv6uni 时可选 --- -#}
    {%- if item.AFTYPE in ['ipv4uni', 'ipv6uni'] -%}
        {%- if item.ROUTERIDNEGLECT is not none -%}
            ROUTERIDNEGLECT={{item.ROUTERIDNEGLECT}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：AFTYPE=ipv4vpn/ipv6vpn/ipv4uni/ipv6uni 时可选 --- -#}
    {%- if item.AFTYPE in ['ipv4vpn', 'ipv6vpn', 'ipv4uni', 'ipv6uni'] -%}
        {%- if item.ROUTESELECTDELAY is not none -%}
            ROUTESELECTDELAY={{item.ROUTESELECTDELAY}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：AFTYPE=ipv4vpn/ipv6vpn 时可选 --- -#}
    {%- if item.AFTYPE in ['ipv4vpn', 'ipv6vpn'] -%}
        {%- if item.RRFILTERNUMBER is not none -%}
            RRFILTERNUMBER="{{item.RRFILTERNUMBER}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：AFTYPE=ipv4uni/ipv6uni 时可选 --- -#}
    {%- if item.AFTYPE in ['ipv4uni', 'ipv6uni'] -%}
        {%- if item.SUPERNETUNIADV is not none -%}
            SUPERNETUNIADV={{item.SUPERNETUNIADV}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：AFTYPE=ipv4vpn/ipv6vpn/ipv4uni 时可选 --- -#}
    {%- if item.AFTYPE in ['ipv4vpn', 'ipv6vpn', 'ipv4uni'] -%}
        {%- if item.TNLSELECTORNAME is not none -%}
            TNLSELECTORNAME="{{item.TNLSELECTORNAME}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：AFTYPE=ipv4uni/ipv6uni 时可选 --- -#}
    {%- if item.AFTYPE in ['ipv4uni', 'ipv6uni'] -%}
        {%- if item.VRFRIDAUTOSEL is not none -%}
            VRFRIDAUTOSEL={{item.VRFRIDAUTOSEL}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 11.3 增加BGP对等体。

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
        {%- if item.CONNRETRYTIME is not none -%}
            CONNRETRYTIME={{item.CONNRETRYTIME}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：ADDRESSTYPE=noaf/ipv4 时可选 --- -#}
    {%- if item.ADDRESSTYPE in ['noaf', 'ipv4'] -%}
        {%- if item.CONVENTIONAL is not none -%}
            CONVENTIONAL={{item.CONVENTIONAL}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：ADDRESSTYPE=noaf/ipv4/ipv6 时可选 --- -#}
    {%- if item.ADDRESSTYPE in ['noaf', 'ipv4', 'ipv6'] -%}
        {%- if item.DESCRIPTION is not none -%}
            DESCRIPTION="{{item.DESCRIPTION}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：ADDRESSTYPE=noaf/ipv4/ipv6 时可选 --- -#}
    {%- if item.ADDRESSTYPE in ['noaf', 'ipv4', 'ipv6'] -%}
        {%- if item.FAKEAS is not none -%}
            FAKEAS="{{item.FAKEAS}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：ADDRESSTYPE=noaf/ipv4/ipv6 时可选 --- -#}
    {%- if item.ADDRESSTYPE in ['noaf', 'ipv4', 'ipv6'] -%}
        {%- if item.FOURBYTEAS is not none -%}
            FOURBYTEAS={{item.FOURBYTEAS}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：ADDRESSTYPE=noaf/ipv4/ipv6 时可选 --- -#}
    {%- if item.ADDRESSTYPE in ['noaf', 'ipv4', 'ipv6'] -%}
        {%- if item.GROUPNAME is not none -%}
            GROUPNAME="{{item.GROUPNAME}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：ADDRESSTYPE=noaf/ipv4/ipv6 时可选 --- -#}
    {%- if item.ADDRESSTYPE in ['noaf', 'ipv4', 'ipv6'] -%}
        {%- if item.HOLDTIME is not none -%}
            HOLDTIME={{item.HOLDTIME}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：ADDRESSTYPE=noaf/ipv4/ipv6 时可选 --- -#}
    {%- if item.ADDRESSTYPE in ['noaf', 'ipv4', 'ipv6'] -%}
        {%- if item.ISIGNORE is not none -%}
            ISIGNORE={{item.ISIGNORE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：ADDRESSTYPE=noaf/ipv4/ipv6 时可选 --- -#}
    {%- if item.ADDRESSTYPE in ['noaf', 'ipv4', 'ipv6'] -%}
        {%- if item.ISLOGCHANGE is not none -%}
            ISLOGCHANGE={{item.ISLOGCHANGE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：ADDRESSTYPE=noaf/ipv4/ipv6 时可选 --- -#}
    {%- if item.ADDRESSTYPE in ['noaf', 'ipv4', 'ipv6'] -%}
        {%- if item.KEEPALIVETIME is not none -%}
            KEEPALIVETIME={{item.KEEPALIVETIME}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：ADDRESSTYPE=noaf/ipv4/ipv6 时可选 --- -#}
    {%- if item.ADDRESSTYPE in ['noaf', 'ipv4', 'ipv6'] -%}
        {%- if item.KEYCHAINNAME is not none -%}
            KEYCHAINNAME="{{item.KEYCHAINNAME}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：ADDRESSTYPE=noaf/ipv4 时可选 --- -#}
    {%- if item.ADDRESSTYPE in ['noaf', 'ipv4'] -%}
        {%- if item.PATHMTUDISCOVERY is not none -%}
            PATHMTUDISCOVERY={{item.PATHMTUDISCOVERY}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：ADDRESSTYPE=noaf/ipv4/ipv6 时可选 --- -#}
    {%- if item.ADDRESSTYPE in ['noaf', 'ipv4', 'ipv6'] -%}
        {%- if item.PSWDTYPE is not none -%}
            PSWDTYPE={{item.PSWDTYPE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：ADDRESSTYPE=noaf/ipv4/ipv6 时可选 --- -#}
    {%- if item.ADDRESSTYPE in ['noaf', 'ipv4', 'ipv6'] -%}
        {%- if item.ROUTEREFRESH is not none -%}
            ROUTEREFRESH={{item.ROUTEREFRESH}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：ADDRESSTYPE=noaf/ipv4/ipv6 时可选 --- -#}
    {%- if item.ADDRESSTYPE in ['noaf', 'ipv4', 'ipv6'] -%}
        {%- if item.TRACKINGDELAYTIME is not none -%}
            TRACKINGDELAYTIME={{item.TRACKINGDELAYTIME}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：ADDRESSTYPE=noaf/ipv4/ipv6 时可选 --- -#}
    {%- if item.ADDRESSTYPE in ['noaf', 'ipv4', 'ipv6'] -%}
        {%- if item.TRACKINGENABLE is not none -%}
            TRACKINGENABLE={{item.TRACKINGENABLE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：ADDRESSTYPE=noaf/ipv4/ipv6 时可选 --- -#}
    {%- if item.ADDRESSTYPE in ['noaf', 'ipv4', 'ipv6'] -%}
        {%- if item.VALIDTTLHOPS is not none -%}
            VALIDTTLHOPS={{item.VALIDTTLHOPS}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 11.4 增加BGP引入路由。

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
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IMPORTPROTOCOL=ospf/ospfv3 时必选 --- -#}
    {%- if item.IMPORTPROTOCOL in ['ospf', 'ospfv3'] -%}
        IMPORTPROCESSID={{item.IMPORTPROCESSID}},
    {%- endif -%}
    {#- --- 条件必选：MEDENABLE=TRUE 时必选 --- -#}
    {%- if item.MEDENABLE == 'TRUE' -%}
        MED={{item.MED}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 由于BGP协议自身不能发现路由，所以需要引入其他协议的路由（如OSPF、静态路由或WLR等）注入到BGP路由表中，从而将这些路由在AS之内和AS之间传播。

#### 网设规划不开启下行入不转板，也不开启入不转板时，请跳过步骤 12~步骤 15。

#### 网设规划开启下行入不转板时，请执行步骤 12、步骤 13和步骤 15。

#### 网设规划开启入不转板时，请执行步骤 12、步骤 14和步骤 15。

### 12 参考步骤 3，关闭自动配置开关。

### 13 网设规划开启下行入不转板时，配置下行入不转板。否则，请跳过本步骤。

### 仅N6/SGi接口需要配置，其他接口不需要配置。

### 开启下行入不转板的命令是**SET DATAPLANEGIINFMODE**，不是**SET DATAPLANEINFMODE**。

### 若误使用**SET DATAPLANEINFMODE**，则会上报ALM-81210 ISU或APU不可用告警。

#### 13.1 开启下行入不转板开关。此处以开启路由增强功能为例。

```jinja2
{%- if is_scenario_downlink_inbound -%}
    {%- for item in set_dataplanegiinfmode_list -%}
        SET DATAPLANEGIINFMODE:
        {#- --- 必选参数 --- -#}
        MODE={{item.MODE}},
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：MODE=RU 时可选 --- -#}
        {%- if item.MODE == 'RU' -%}
            {%- if item.ROUTEENHANCEDSW is not none -%}
                ROUTEENHANCEDSW={{item.ROUTEENHANCEDSW}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 13.2 开启路由增强功能时，修改BGP对等体地址族。

#### 开启路由增强功能时，必须将“ADVERTISECOMMUNITY”设置为“TRUE”。其他参数值此处仅为举例，请通过**LST BGPPEER**获取。

```jinja2
{%- if is_scenario_downlink_inbound -%}
    {%- for item in mod_bgppeeraf_list -%}
        MOD BGPPEERAF:
        {#- --- 必选参数 --- -#}
        VRFNAME="{{item.VRFNAME}}",
        AFTYPE={{item.AFTYPE}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：ADDRESSTYPE=ipv4 时必选 --- -#}
        {%- if item.ADDRESSTYPE == 'ipv4' -%}
            REMOTEADDRESS="{{item.REMOTEADDRESS}}",
        {#- --- 条件必选：AFTYPE=ipv4uni/ipv4vpn/ipv6vpn 时必选 --- -#}
        {%- elif item.AFTYPE in ['ipv4uni', 'ipv4vpn', 'ipv6vpn'] -%}
            REMOTEADDRESS="{{item.REMOTEADDRESS}}",
        {%- endif -%}
        {#- --- 条件必选：AFTYPE=ipv6uni 时必选 --- -#}
        {%- if item.AFTYPE == 'ipv6uni' -%}
            ADDRESSTYPE={{item.ADDRESSTYPE}},
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：ADDRESSTYPE=ipv4/ipv6 时可选 --- -#}
        {%- if item.ADDRESSTYPE in ['ipv4', 'ipv6'] -%}
            {%- if item.ADVERTISECOMMUNITY is not none -%}
                ADVERTISECOMMUNITY={{item.ADVERTISECOMMUNITY}},
            {%- endif -%}
        {#- --- 条件可选：AFTYPE=ipv4uni/ipv4vpn/ipv6vpn 时可选 --- -#}
        {%- elif item.AFTYPE in ['ipv4uni', 'ipv4vpn', 'ipv6vpn'] -%}
            {%- if item.ADVERTISECOMMUNITY is not none -%}
                ADVERTISECOMMUNITY={{item.ADVERTISECOMMUNITY}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：AFTYPE=ipv4uni/ipv4vpn/ipv6vpn 时可选 --- -#}
        {%- if item.AFTYPE in ['ipv4uni', 'ipv4vpn', 'ipv6vpn'] -%}
            {%- if item.ADDPATHMODE is not none -%}
                ADDPATHMODE={{item.ADDPATHMODE}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：AFTYPE=ipv4uni/ipv4vpn/ipv6vpn 时可选 --- -#}
        {%- if item.AFTYPE in ['ipv4uni', 'ipv4vpn', 'ipv6vpn'] -%}
            {%- if item.ADVADDPATHNUM is not none -%}
                ADVADDPATHNUM={{item.ADVADDPATHNUM}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：AFTYPE=ipv4uni/ipv4vpn/ipv6vpn 时可选 --- -#}
        {%- if item.AFTYPE in ['ipv4uni', 'ipv4vpn', 'ipv6vpn'] -%}
            {%- if item.ADVBESTEXTERNAL is not none -%}
                ADVBESTEXTERNAL={{item.ADVBESTEXTERNAL}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：ADDRESSTYPE=ipv4/ipv6 时可选 --- -#}
        {%- if item.ADDRESSTYPE in ['ipv4', 'ipv6'] -%}
            {%- if item.ADVERTISEEXTCOMMUNITY is not none -%}
                ADVERTISEEXTCOMMUNITY={{item.ADVERTISEEXTCOMMUNITY}},
            {%- endif -%}
        {#- --- 条件可选：AFTYPE=ipv4uni 时可选 --- -#}
        {%- elif item.AFTYPE == 'ipv4uni' -%}
            {%- if item.ADVERTISEEXTCOMMUNITY is not none -%}
                ADVERTISEEXTCOMMUNITY={{item.ADVERTISEEXTCOMMUNITY}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：ADDRESSTYPE=ipv4/ipv6 时可选 --- -#}
        {%- if item.ADDRESSTYPE in ['ipv4', 'ipv6'] -%}
            {%- if item.ALLOWASLOOPENABLE is not none -%}
                ALLOWASLOOPENABLE={{item.ALLOWASLOOPENABLE}},
            {%- endif -%}
        {#- --- 条件可选：AFTYPE=ipv4uni/ipv4vpn/ipv6vpn 时可选 --- -#}
        {%- elif item.AFTYPE in ['ipv4uni', 'ipv4vpn', 'ipv6vpn'] -%}
            {%- if item.ALLOWASLOOPENABLE is not none -%}
                ALLOWASLOOPENABLE={{item.ALLOWASLOOPENABLE}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：ADDRESSTYPE=ipv4/ipv6 时可选 --- -#}
        {%- if item.ADDRESSTYPE in ['ipv4', 'ipv6'] -%}
            {%- if item.ALLOWASLOOPLIMIT is not none -%}
                ALLOWASLOOPLIMIT={{item.ALLOWASLOOPLIMIT}},
            {%- endif -%}
        {#- --- 条件可选：AFTYPE=ipv4uni/ipv4vpn/ipv6vpn 时可选 --- -#}
        {%- elif item.AFTYPE in ['ipv4uni', 'ipv4vpn', 'ipv6vpn'] -%}
            {%- if item.ALLOWASLOOPLIMIT is not none -%}
                ALLOWASLOOPLIMIT={{item.ALLOWASLOOPLIMIT}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：ADDRESSTYPE=ipv6 时可选 --- -#}
        {%- if item.ADDRESSTYPE == 'ipv6' -%}
            {%- if item.DEFAULTRTADVENABLE is not none -%}
                DEFAULTRTADVENABLE={{item.DEFAULTRTADVENABLE}},
            {%- endif -%}
        {#- --- 条件可选：AFTYPE=ipv4uni 时可选 --- -#}
        {%- elif item.AFTYPE == 'ipv4uni' -%}
            {%- if item.DEFAULTRTADVENABLE is not none -%}
                DEFAULTRTADVENABLE={{item.DEFAULTRTADVENABLE}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：ADDRESSTYPE=ipv6 时可选 --- -#}
        {%- if item.ADDRESSTYPE == 'ipv6' -%}
            {%- if item.DEFAULTRTADVPOLICY is not none -%}
                DEFAULTRTADVPOLICY="{{item.DEFAULTRTADVPOLICY}}",
            {%- endif -%}
        {#- --- 条件可选：AFTYPE=ipv4uni 时可选 --- -#}
        {%- elif item.AFTYPE == 'ipv4uni' -%}
            {%- if item.DEFAULTRTADVPOLICY is not none -%}
                DEFAULTRTADVPOLICY="{{item.DEFAULTRTADVPOLICY}}",
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：ADDRESSTYPE=ipv6 时可选 --- -#}
        {%- if item.ADDRESSTYPE == 'ipv6' -%}
            {%- if item.DEFAULTRTMATCHMODE is not none -%}
                DEFAULTRTMATCHMODE={{item.DEFAULTRTMATCHMODE}},
            {%- endif -%}
        {#- --- 条件可选：AFTYPE=ipv4uni/ipv4vpn/ipv6vpn 时可选 --- -#}
        {%- elif item.AFTYPE in ['ipv4uni', 'ipv4vpn', 'ipv6vpn'] -%}
            {%- if item.DEFAULTRTMATCHMODE is not none -%}
                DEFAULTRTMATCHMODE={{item.DEFAULTRTMATCHMODE}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：ADDRESSTYPE=ipv4/ipv6 时可选 --- -#}
        {%- if item.ADDRESSTYPE in ['ipv4', 'ipv6'] -%}
            {%- if item.DISCARDEXTCOMMUNITY is not none -%}
                DISCARDEXTCOMMUNITY={{item.DISCARDEXTCOMMUNITY}},
            {%- endif -%}
        {#- --- 条件可选：AFTYPE=ipv4uni 时可选 --- -#}
        {%- elif item.AFTYPE == 'ipv4uni' -%}
            {%- if item.DISCARDEXTCOMMUNITY is not none -%}
                DISCARDEXTCOMMUNITY={{item.DISCARDEXTCOMMUNITY}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：ADDRESSTYPE=ipv4/ipv6 时可选 --- -#}
        {%- if item.ADDRESSTYPE in ['ipv4', 'ipv6'] -%}
            {%- if item.EXPORTACL6NAMEORNUM is not none -%}
                EXPORTACL6NAMEORNUM="{{item.EXPORTACL6NAMEORNUM}}",
            {%- endif -%}
        {#- --- 条件可选：AFTYPE=ipv6vpn 时可选 --- -#}
        {%- elif item.AFTYPE == 'ipv6vpn' -%}
            {%- if item.EXPORTACL6NAMEORNUM is not none -%}
                EXPORTACL6NAMEORNUM="{{item.EXPORTACL6NAMEORNUM}}",
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：AFTYPE=ipv4uni/ipv4vpn 时可选 --- -#}
        {%- if item.AFTYPE in ['ipv4uni', 'ipv4vpn'] -%}
            {%- if item.EXPORTACLNAMEORNUM is not none -%}
                EXPORTACLNAMEORNUM="{{item.EXPORTACLNAMEORNUM}}",
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：ADDRESSTYPE=ipv4/ipv6 时可选 --- -#}
        {%- if item.ADDRESSTYPE in ['ipv4', 'ipv6'] -%}
            {%- if item.EXPORTASPATHFILTER is not none -%}
                EXPORTASPATHFILTER="{{item.EXPORTASPATHFILTER}}",
            {%- endif -%}
        {#- --- 条件可选：AFTYPE=ipv4uni/ipv4vpn/ipv6vpn 时可选 --- -#}
        {%- elif item.AFTYPE in ['ipv4uni', 'ipv4vpn', 'ipv6vpn'] -%}
            {%- if item.EXPORTASPATHFILTER is not none -%}
                EXPORTASPATHFILTER="{{item.EXPORTASPATHFILTER}}",
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：ADDRESSTYPE=ipv6 时可选 --- -#}
        {%- if item.ADDRESSTYPE == 'ipv6' -%}
            {%- if item.EXPORTPREF6FILTNAME is not none -%}
                EXPORTPREF6FILTNAME="{{item.EXPORTPREF6FILTNAME}}",
            {%- endif -%}
        {#- --- 条件可选：AFTYPE=ipv6vpn 时可选 --- -#}
        {%- elif item.AFTYPE == 'ipv6vpn' -%}
            {%- if item.EXPORTPREF6FILTNAME is not none -%}
                EXPORTPREF6FILTNAME="{{item.EXPORTPREF6FILTNAME}}",
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：AFTYPE=ipv4uni/ipv4vpn 时可选 --- -#}
        {%- if item.AFTYPE in ['ipv4uni', 'ipv4vpn'] -%}
            {%- if item.EXPORTPREFFILTNAME is not none -%}
                EXPORTPREFFILTNAME="{{item.EXPORTPREFFILTNAME}}",
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：ADDRESSTYPE=ipv4/ipv6 时可选 --- -#}
        {%- if item.ADDRESSTYPE in ['ipv4', 'ipv6'] -%}
            {%- if item.EXPORTRTPOLICYNAME is not none -%}
                EXPORTRTPOLICYNAME="{{item.EXPORTRTPOLICYNAME}}",
            {%- endif -%}
        {#- --- 条件可选：AFTYPE=ipv4uni/ipv4vpn/ipv6vpn 时可选 --- -#}
        {%- elif item.AFTYPE in ['ipv4uni', 'ipv4vpn', 'ipv6vpn'] -%}
            {%- if item.EXPORTRTPOLICYNAME is not none -%}
                EXPORTRTPOLICYNAME="{{item.EXPORTRTPOLICYNAME}}",
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：ADDRESSTYPE=ipv4/ipv6 时可选 --- -#}
        {%- if item.ADDRESSTYPE in ['ipv4', 'ipv6'] -%}
            {%- if item.IMPORTACL6NAMEORNUM is not none -%}
                IMPORTACL6NAMEORNUM="{{item.IMPORTACL6NAMEORNUM}}",
            {%- endif -%}
        {#- --- 条件可选：AFTYPE=ipv6vpn 时可选 --- -#}
        {%- elif item.AFTYPE == 'ipv6vpn' -%}
            {%- if item.IMPORTACL6NAMEORNUM is not none -%}
                IMPORTACL6NAMEORNUM="{{item.IMPORTACL6NAMEORNUM}}",
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：AFTYPE=ipv4uni/ipv4vpn 时可选 --- -#}
        {%- if item.AFTYPE in ['ipv4uni', 'ipv4vpn'] -%}
            {%- if item.IMPORTACLNAMEORNUM is not none -%}
                IMPORTACLNAMEORNUM="{{item.IMPORTACLNAMEORNUM}}",
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：ADDRESSTYPE=ipv4/ipv6 时可选 --- -#}
        {%- if item.ADDRESSTYPE in ['ipv4', 'ipv6'] -%}
            {%- if item.IMPORTASPATHFILTER is not none -%}
                IMPORTASPATHFILTER="{{item.IMPORTASPATHFILTER}}",
            {%- endif -%}
        {#- --- 条件可选：AFTYPE=ipv4uni/ipv4vpn/ipv6vpn 时可选 --- -#}
        {%- elif item.AFTYPE in ['ipv4uni', 'ipv4vpn', 'ipv6vpn'] -%}
            {%- if item.IMPORTASPATHFILTER is not none -%}
                IMPORTASPATHFILTER="{{item.IMPORTASPATHFILTER}}",
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：ADDRESSTYPE=ipv6 时可选 --- -#}
        {%- if item.ADDRESSTYPE == 'ipv6' -%}
            {%- if item.IMPORTPREF6FILTNAME is not none -%}
                IMPORTPREF6FILTNAME="{{item.IMPORTPREF6FILTNAME}}",
            {%- endif -%}
        {#- --- 条件可选：AFTYPE=ipv6vpn 时可选 --- -#}
        {%- elif item.AFTYPE == 'ipv6vpn' -%}
            {%- if item.IMPORTPREF6FILTNAME is not none -%}
                IMPORTPREF6FILTNAME="{{item.IMPORTPREF6FILTNAME}}",
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：AFTYPE=ipv4uni/ipv4vpn 时可选 --- -#}
        {%- if item.AFTYPE in ['ipv4uni', 'ipv4vpn'] -%}
            {%- if item.IMPORTPREFFILTNAME is not none -%}
                IMPORTPREFFILTNAME="{{item.IMPORTPREFFILTNAME}}",
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：ADDRESSTYPE=ipv4/ipv6 时可选 --- -#}
        {%- if item.ADDRESSTYPE in ['ipv4', 'ipv6'] -%}
            {%- if item.IMPORTRTPOLICYNAME is not none -%}
                IMPORTRTPOLICYNAME="{{item.IMPORTRTPOLICYNAME}}",
            {%- endif -%}
        {#- --- 条件可选：AFTYPE=ipv4uni/ipv4vpn/ipv6vpn 时可选 --- -#}
        {%- elif item.AFTYPE in ['ipv4uni', 'ipv4vpn', 'ipv6vpn'] -%}
            {%- if item.IMPORTRTPOLICYNAME is not none -%}
                IMPORTRTPOLICYNAME="{{item.IMPORTRTPOLICYNAME}}",
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：ADDRESSTYPE=ipv4/ipv6 时可选 --- -#}
        {%- if item.ADDRESSTYPE in ['ipv4', 'ipv6'] -%}
            {%- if item.INCLUDEPEERAS is not none -%}
                INCLUDEPEERAS={{item.INCLUDEPEERAS}},
            {%- endif -%}
        {#- --- 条件可选：AFTYPE=ipv4uni/ipv4vpn/ipv6vpn 时可选 --- -#}
        {%- elif item.AFTYPE in ['ipv4uni', 'ipv4vpn', 'ipv6vpn'] -%}
            {%- if item.INCLUDEPEERAS is not none -%}
                INCLUDEPEERAS={{item.INCLUDEPEERAS}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：ADDRESSTYPE=ipv4 时可选 --- -#}
        {%- if item.ADDRESSTYPE == 'ipv4' -%}
            {%- if item.ISSOURELAYNEIGHINTER is not none -%}
                ISSOURELAYNEIGHINTER={{item.ISSOURELAYNEIGHINTER}},
            {%- endif -%}
        {#- --- 条件可选：AFTYPE=ipv4uni 时可选 --- -#}
        {%- elif item.AFTYPE == 'ipv4uni' -%}
            {%- if item.ISSOURELAYNEIGHINTER is not none -%}
                ISSOURELAYNEIGHINTER={{item.ISSOURELAYNEIGHINTER}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：ADDRESSTYPE=ipv4/ipv6 时可选 --- -#}
        {%- if item.ADDRESSTYPE in ['ipv4', 'ipv6'] -%}
            {%- if item.KEEPALLROUTES is not none -%}
                KEEPALLROUTES={{item.KEEPALLROUTES}},
            {%- endif -%}
        {#- --- 条件可选：AFTYPE=ipv4uni/ipv4vpn/ipv6vpn 时可选 --- -#}
        {%- elif item.AFTYPE in ['ipv4uni', 'ipv4vpn', 'ipv6vpn'] -%}
            {%- if item.KEEPALLROUTES is not none -%}
                KEEPALLROUTES={{item.KEEPALLROUTES}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：ADDRESSTYPE=ipv4/ipv6 时可选 --- -#}
        {%- if item.ADDRESSTYPE in ['ipv4', 'ipv6'] -%}
            {%- if item.NEXTHOPCONFIGURE is not none -%}
                NEXTHOPCONFIGURE={{item.NEXTHOPCONFIGURE}},
            {%- endif -%}
        {#- --- 条件可选：AFTYPE=ipv4uni/ipv4vpn/ipv6vpn 时可选 --- -#}
        {%- elif item.AFTYPE in ['ipv4uni', 'ipv4vpn', 'ipv6vpn'] -%}
            {%- if item.NEXTHOPCONFIGURE is not none -%}
                NEXTHOPCONFIGURE={{item.NEXTHOPCONFIGURE}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：ADDRESSTYPE=ipv4/ipv6 时可选 --- -#}
        {%- if item.ADDRESSTYPE in ['ipv4', 'ipv6'] -%}
            {%- if item.PEERGROUPNAME is not none -%}
                PEERGROUPNAME="{{item.PEERGROUPNAME}}",
            {%- endif -%}
        {#- --- 条件可选：AFTYPE=ipv4uni/ipv4vpn/ipv6vpn 时可选 --- -#}
        {%- elif item.AFTYPE in ['ipv4uni', 'ipv4vpn', 'ipv6vpn'] -%}
            {%- if item.PEERGROUPNAME is not none -%}
                PEERGROUPNAME="{{item.PEERGROUPNAME}}",
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：ADDRESSTYPE=ipv4/ipv6 时可选 --- -#}
        {%- if item.ADDRESSTYPE in ['ipv4', 'ipv6'] -%}
            {%- if item.PREFERREDVALUE is not none -%}
                PREFERREDVALUE={{item.PREFERREDVALUE}},
            {%- endif -%}
        {#- --- 条件可选：AFTYPE=ipv4uni/ipv4vpn/ipv6vpn 时可选 --- -#}
        {%- elif item.AFTYPE in ['ipv4uni', 'ipv4vpn', 'ipv6vpn'] -%}
            {%- if item.PREFERREDVALUE is not none -%}
                PREFERREDVALUE={{item.PREFERREDVALUE}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：ADDRESSTYPE=ipv4/ipv6 时可选 --- -#}
        {%- if item.ADDRESSTYPE in ['ipv4', 'ipv6'] -%}
            {%- if item.PUBLICASONLY is not none -%}
                PUBLICASONLY={{item.PUBLICASONLY}},
            {%- endif -%}
        {#- --- 条件可选：AFTYPE=ipv4uni/ipv4vpn/ipv6vpn 时可选 --- -#}
        {%- elif item.AFTYPE in ['ipv4uni', 'ipv4vpn', 'ipv6vpn'] -%}
            {%- if item.PUBLICASONLY is not none -%}
                PUBLICASONLY={{item.PUBLICASONLY}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：ADDRESSTYPE=ipv4/ipv6 时可选 --- -#}
        {%- if item.ADDRESSTYPE in ['ipv4', 'ipv6'] -%}
            {%- if item.PUBLICASONLYFORCE is not none -%}
                PUBLICASONLYFORCE={{item.PUBLICASONLYFORCE}},
            {%- endif -%}
        {#- --- 条件可选：AFTYPE=ipv4uni/ipv4vpn/ipv6vpn 时可选 --- -#}
        {%- elif item.AFTYPE in ['ipv4uni', 'ipv4vpn', 'ipv6vpn'] -%}
            {%- if item.PUBLICASONLYFORCE is not none -%}
                PUBLICASONLYFORCE={{item.PUBLICASONLYFORCE}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：ADDRESSTYPE=ipv4/ipv6 时可选 --- -#}
        {%- if item.ADDRESSTYPE in ['ipv4', 'ipv6'] -%}
            {%- if item.PUBLICASONLYLIMITED is not none -%}
                PUBLICASONLYLIMITED={{item.PUBLICASONLYLIMITED}},
            {%- endif -%}
        {#- --- 条件可选：AFTYPE=ipv4uni/ipv4vpn/ipv6vpn 时可选 --- -#}
        {%- elif item.AFTYPE in ['ipv4uni', 'ipv4vpn', 'ipv6vpn'] -%}
            {%- if item.PUBLICASONLYLIMITED is not none -%}
                PUBLICASONLYLIMITED={{item.PUBLICASONLYLIMITED}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：ADDRESSTYPE=ipv4/ipv6 时可选 --- -#}
        {%- if item.ADDRESSTYPE in ['ipv4', 'ipv6'] -%}
            {%- if item.PUBLICASONLYREPLACE is not none -%}
                PUBLICASONLYREPLACE={{item.PUBLICASONLYREPLACE}},
            {%- endif -%}
        {#- --- 条件可选：AFTYPE=ipv4uni/ipv4vpn/ipv6vpn 时可选 --- -#}
        {%- elif item.AFTYPE in ['ipv4uni', 'ipv4vpn', 'ipv6vpn'] -%}
            {%- if item.PUBLICASONLYREPLACE is not none -%}
                PUBLICASONLYREPLACE={{item.PUBLICASONLYREPLACE}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：ADDRESSTYPE=ipv4/ipv6 时可选 --- -#}
        {%- if item.ADDRESSTYPE in ['ipv4', 'ipv6'] -%}
            {%- if item.REFLECTCLIENT is not none -%}
                REFLECTCLIENT={{item.REFLECTCLIENT}},
            {%- endif -%}
        {#- --- 条件可选：AFTYPE=ipv4uni/ipv4vpn/ipv6vpn 时可选 --- -#}
        {%- elif item.AFTYPE in ['ipv4uni', 'ipv4vpn', 'ipv6vpn'] -%}
            {%- if item.REFLECTCLIENT is not none -%}
                REFLECTCLIENT={{item.REFLECTCLIENT}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：ADDRESSTYPE=ipv4/ipv6 时可选 --- -#}
        {%- if item.ADDRESSTYPE in ['ipv4', 'ipv6'] -%}
            {%- if item.ROUTELIMIT is not none -%}
                ROUTELIMIT={{item.ROUTELIMIT}},
            {%- endif -%}
        {#- --- 条件可选：AFTYPE=ipv4uni/ipv4vpn/ipv6vpn 时可选 --- -#}
        {%- elif item.AFTYPE in ['ipv4uni', 'ipv4vpn', 'ipv6vpn'] -%}
            {%- if item.ROUTELIMIT is not none -%}
                ROUTELIMIT={{item.ROUTELIMIT}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：ADDRESSTYPE=ipv4/ipv6 时可选 --- -#}
        {%- if item.ADDRESSTYPE in ['ipv4', 'ipv6'] -%}
            {%- if item.ROUTELIMITIDLETIMEOUT is not none -%}
                ROUTELIMITIDLETIMEOUT={{item.ROUTELIMITIDLETIMEOUT}},
            {%- endif -%}
        {#- --- 条件可选：AFTYPE=ipv4uni/ipv4vpn/ipv6vpn 时可选 --- -#}
        {%- elif item.AFTYPE in ['ipv4uni', 'ipv4vpn', 'ipv6vpn'] -%}
            {%- if item.ROUTELIMITIDLETIMEOUT is not none -%}
                ROUTELIMITIDLETIMEOUT={{item.ROUTELIMITIDLETIMEOUT}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：ADDRESSTYPE=ipv4/ipv6 时可选 --- -#}
        {%- if item.ADDRESSTYPE in ['ipv4', 'ipv6'] -%}
            {%- if item.ROUTELIMITPERCENT is not none -%}
                ROUTELIMITPERCENT={{item.ROUTELIMITPERCENT}},
            {%- endif -%}
        {#- --- 条件可选：AFTYPE=ipv4uni/ipv4vpn/ipv6vpn 时可选 --- -#}
        {%- elif item.AFTYPE in ['ipv4uni', 'ipv4vpn', 'ipv6vpn'] -%}
            {%- if item.ROUTELIMITPERCENT is not none -%}
                ROUTELIMITPERCENT={{item.ROUTELIMITPERCENT}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：ADDRESSTYPE=ipv4/ipv6 时可选 --- -#}
        {%- if item.ADDRESSTYPE in ['ipv4', 'ipv6'] -%}
            {%- if item.ROUTELIMITTYPE is not none -%}
                ROUTELIMITTYPE={{item.ROUTELIMITTYPE}},
            {%- endif -%}
        {#- --- 条件可选：AFTYPE=ipv4uni/ipv4vpn/ipv6vpn 时可选 --- -#}
        {%- elif item.AFTYPE in ['ipv4uni', 'ipv4vpn', 'ipv6vpn'] -%}
            {%- if item.ROUTELIMITTYPE is not none -%}
                ROUTELIMITTYPE={{item.ROUTELIMITTYPE}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：ADDRESSTYPE=ipv4/ipv6 时可选 --- -#}
        {%- if item.ADDRESSTYPE in ['ipv4', 'ipv6'] -%}
            {%- if item.RTUPDTINTERVAL is not none -%}
                RTUPDTINTERVAL={{item.RTUPDTINTERVAL}},
            {%- endif -%}
        {#- --- 条件可选：AFTYPE=ipv4uni 时可选 --- -#}
        {%- elif item.AFTYPE == 'ipv4uni' -%}
            {%- if item.RTUPDTINTERVAL is not none -%}
                RTUPDTINTERVAL={{item.RTUPDTINTERVAL}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：ADDRESSTYPE=ipv6 时可选 --- -#}
        {%- if item.ADDRESSTYPE == 'ipv6' -%}
            {%- if item.SUBSTITUTEASENABLE is not none -%}
                SUBSTITUTEASENABLE={{item.SUBSTITUTEASENABLE}},
            {%- endif -%}
        {#- --- 条件可选：AFTYPE=ipv4uni/ipv4vpn/ipv6vpn 时可选 --- -#}
        {%- elif item.AFTYPE in ['ipv4uni', 'ipv4vpn', 'ipv6vpn'] -%}
            {%- if item.SUBSTITUTEASENABLE is not none -%}
                SUBSTITUTEASENABLE={{item.SUBSTITUTEASENABLE}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 13.3 增加入不转板策略自动化配置模板。

```jinja2
{%- if is_scenario_downlink_inbound -%}
    {%- for item in add_autoscalingbgplf_list -%}
        ADD AUTOSCALINGBGPLF:
        {#- --- 必选参数 --- -#}
        POLICYNAME="{{item.POLICYNAME}}",
        IPVERSION={{item.IPVERSION}},
        SERVICENAME="{{item.SERVICENAME}}",
        {#- --- 可选参数 --- -#}
        {%- if item.PEERCOMMUNITY is not none -%}
            PEERCOMMUNITY={{item.PEERCOMMUNITY}},
        {%- endif -%}
        {%- if item.UDADVCOMENABLE is not none -%}
            UDADVCOMENABLE={{item.UDADVCOMENABLE}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：IPVERSION=IPv4 时必选 --- -#}
        {%- if item.IPVERSION == 'IPv4' -%}
            PEERIP="{{item.PEERIP}}",
        {%- endif -%}
        {#- --- 条件必选：UDADVCOMENABLE=TRUE 时必选 --- -#}
        {%- if item.UDADVCOMENABLE == 'TRUE' -%}
            UDADVCOM="{{item.UDADVCOM}}",
        {%- endif -%}
        {#- --- 条件必选：IPVERSION=IPv6 时必选 --- -#}
        {%- if item.IPVERSION == 'IPv6' -%}
            PEERIPV6="{{item.PEERIPV6}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 13.4 增加IP可达性检测自动化配置模板。

```jinja2
{%- if is_scenario_downlink_inbound -%}
    {%- for item in add_autoscalingipreach_list -%}
        ADD AUTOSCALINGIPREACH:
        {#- --- 必选参数 --- -#}
        SERVICENAME="{{item.SERVICENAME}}",
        IPVERSION={{item.IPVERSION}},
        BFDTEMPLATENAME="{{item.BFDTEMPLATENAME}}",
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：IPVERSION=IPv4 时必选 --- -#}
        {%- if item.IPVERSION == 'IPv4' -%}
            DESTADDR4="{{item.DESTADDR4}}",
        {%- endif -%}
        {#- --- 条件必选：IPVERSION=IPv6 时必选 --- -#}
        {%- if item.IPVERSION == 'IPv6' -%}
            DESTADDR6="{{item.DESTADDR6}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 14 网设规划开启入不转板时，配置入不转板。否则，请跳过本步骤。

### 仅如下逻辑接口对应的外联口需要配置，其他接口不需要配置。

### s1-uif（S1-U）、n3if（N3）、saif（S1-U和N3）。

### s5-sif（S5/S8-S）、n9cif（N9c）、scif（S5/S8-S和N9c）。

### paif（N9a/S5-P/S8-P/S2b/Gn-U/Gp-U）。

### 开启入不转板的命令是**SET DATAPLANEINFMODE**，不是**SET DATAPLANEGIINFMODE**。

### 如误使用**SET DATAPLANEGIINFMODE**，则下行业务入不转板，上行业务入转板。

#### 14.1 开启入不转板开关。此处以开启路由增强功能为例。

```jinja2
{%- if is_scenario_inbound -%}
    {%- for item in set_dataplaneinfmode_list -%}
        SET DATAPLANEINFMODE:
        {#- --- 必选参数 --- -#}
        MODE={{item.MODE}},
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：MODE=Instance 时可选 --- -#}
        {%- if item.MODE == 'Instance' -%}
            {%- if item.ROUTEENHANCEDSW is not none -%}
                ROUTEENHANCEDSW={{item.ROUTEENHANCEDSW}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 14.2 将接口模板设置为在保护组上生效。

##### 14.2.1 //“ISBACKUP”设置为“TRUE”时，表示在保护组上生效；“ISBACKUP”设置为“FALSE”时，表示在非保护组上生效。

```jinja2
{%- if is_scenario_inbound -%}
    {%- for item in mod_autoscalingservice_list -%}
        MOD AUTOSCALINGSERVICE:
        {#- --- 必选参数 --- -#}
        SERVICENAME="{{item.SERVICENAME}}",
        {#- --- 可选参数 --- -#}
        {%- if item.ISBACKUP is not none -%}
            ISBACKUP={{item.ISBACKUP}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 14.3 开启路由增强功能时，修改BGP对等体地址族。

#### 开启路由增强功能时，必须将“ADVERTISECOMMUNITY”设置为“TRUE”。其他参数值此处仅为举例，请通过**LST BGPPEER**获取。

```jinja2
{%- if is_scenario_inbound -%}
    {%- for item in mod_bgppeeraf_list_2 -%}
        MOD BGPPEERAF:
        {#- --- 必选参数 --- -#}
        VRFNAME="{{item.VRFNAME}}",
        AFTYPE={{item.AFTYPE}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：ADDRESSTYPE=ipv4 时必选 --- -#}
        {%- if item.ADDRESSTYPE == 'ipv4' -%}
            REMOTEADDRESS="{{item.REMOTEADDRESS}}",
        {#- --- 条件必选：AFTYPE=ipv4uni/ipv4vpn/ipv6vpn 时必选 --- -#}
        {%- elif item.AFTYPE in ['ipv4uni', 'ipv4vpn', 'ipv6vpn'] -%}
            REMOTEADDRESS="{{item.REMOTEADDRESS}}",
        {%- endif -%}
        {#- --- 条件必选：AFTYPE=ipv6uni 时必选 --- -#}
        {%- if item.AFTYPE == 'ipv6uni' -%}
            ADDRESSTYPE={{item.ADDRESSTYPE}},
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：ADDRESSTYPE=ipv4/ipv6 时可选 --- -#}
        {%- if item.ADDRESSTYPE in ['ipv4', 'ipv6'] -%}
            {%- if item.ADVERTISECOMMUNITY is not none -%}
                ADVERTISECOMMUNITY={{item.ADVERTISECOMMUNITY}},
            {%- endif -%}
        {#- --- 条件可选：AFTYPE=ipv4uni/ipv4vpn/ipv6vpn 时可选 --- -#}
        {%- elif item.AFTYPE in ['ipv4uni', 'ipv4vpn', 'ipv6vpn'] -%}
            {%- if item.ADVERTISECOMMUNITY is not none -%}
                ADVERTISECOMMUNITY={{item.ADVERTISECOMMUNITY}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：AFTYPE=ipv4uni/ipv4vpn/ipv6vpn 时可选 --- -#}
        {%- if item.AFTYPE in ['ipv4uni', 'ipv4vpn', 'ipv6vpn'] -%}
            {%- if item.ADDPATHMODE is not none -%}
                ADDPATHMODE={{item.ADDPATHMODE}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：AFTYPE=ipv4uni/ipv4vpn/ipv6vpn 时可选 --- -#}
        {%- if item.AFTYPE in ['ipv4uni', 'ipv4vpn', 'ipv6vpn'] -%}
            {%- if item.ADVADDPATHNUM is not none -%}
                ADVADDPATHNUM={{item.ADVADDPATHNUM}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：AFTYPE=ipv4uni/ipv4vpn/ipv6vpn 时可选 --- -#}
        {%- if item.AFTYPE in ['ipv4uni', 'ipv4vpn', 'ipv6vpn'] -%}
            {%- if item.ADVBESTEXTERNAL is not none -%}
                ADVBESTEXTERNAL={{item.ADVBESTEXTERNAL}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：ADDRESSTYPE=ipv4/ipv6 时可选 --- -#}
        {%- if item.ADDRESSTYPE in ['ipv4', 'ipv6'] -%}
            {%- if item.ADVERTISEEXTCOMMUNITY is not none -%}
                ADVERTISEEXTCOMMUNITY={{item.ADVERTISEEXTCOMMUNITY}},
            {%- endif -%}
        {#- --- 条件可选：AFTYPE=ipv4uni 时可选 --- -#}
        {%- elif item.AFTYPE == 'ipv4uni' -%}
            {%- if item.ADVERTISEEXTCOMMUNITY is not none -%}
                ADVERTISEEXTCOMMUNITY={{item.ADVERTISEEXTCOMMUNITY}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：ADDRESSTYPE=ipv4/ipv6 时可选 --- -#}
        {%- if item.ADDRESSTYPE in ['ipv4', 'ipv6'] -%}
            {%- if item.ALLOWASLOOPENABLE is not none -%}
                ALLOWASLOOPENABLE={{item.ALLOWASLOOPENABLE}},
            {%- endif -%}
        {#- --- 条件可选：AFTYPE=ipv4uni/ipv4vpn/ipv6vpn 时可选 --- -#}
        {%- elif item.AFTYPE in ['ipv4uni', 'ipv4vpn', 'ipv6vpn'] -%}
            {%- if item.ALLOWASLOOPENABLE is not none -%}
                ALLOWASLOOPENABLE={{item.ALLOWASLOOPENABLE}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：ADDRESSTYPE=ipv4/ipv6 时可选 --- -#}
        {%- if item.ADDRESSTYPE in ['ipv4', 'ipv6'] -%}
            {%- if item.ALLOWASLOOPLIMIT is not none -%}
                ALLOWASLOOPLIMIT={{item.ALLOWASLOOPLIMIT}},
            {%- endif -%}
        {#- --- 条件可选：AFTYPE=ipv4uni/ipv4vpn/ipv6vpn 时可选 --- -#}
        {%- elif item.AFTYPE in ['ipv4uni', 'ipv4vpn', 'ipv6vpn'] -%}
            {%- if item.ALLOWASLOOPLIMIT is not none -%}
                ALLOWASLOOPLIMIT={{item.ALLOWASLOOPLIMIT}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：ADDRESSTYPE=ipv6 时可选 --- -#}
        {%- if item.ADDRESSTYPE == 'ipv6' -%}
            {%- if item.DEFAULTRTADVENABLE is not none -%}
                DEFAULTRTADVENABLE={{item.DEFAULTRTADVENABLE}},
            {%- endif -%}
        {#- --- 条件可选：AFTYPE=ipv4uni 时可选 --- -#}
        {%- elif item.AFTYPE == 'ipv4uni' -%}
            {%- if item.DEFAULTRTADVENABLE is not none -%}
                DEFAULTRTADVENABLE={{item.DEFAULTRTADVENABLE}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：ADDRESSTYPE=ipv6 时可选 --- -#}
        {%- if item.ADDRESSTYPE == 'ipv6' -%}
            {%- if item.DEFAULTRTADVPOLICY is not none -%}
                DEFAULTRTADVPOLICY="{{item.DEFAULTRTADVPOLICY}}",
            {%- endif -%}
        {#- --- 条件可选：AFTYPE=ipv4uni 时可选 --- -#}
        {%- elif item.AFTYPE == 'ipv4uni' -%}
            {%- if item.DEFAULTRTADVPOLICY is not none -%}
                DEFAULTRTADVPOLICY="{{item.DEFAULTRTADVPOLICY}}",
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：ADDRESSTYPE=ipv6 时可选 --- -#}
        {%- if item.ADDRESSTYPE == 'ipv6' -%}
            {%- if item.DEFAULTRTMATCHMODE is not none -%}
                DEFAULTRTMATCHMODE={{item.DEFAULTRTMATCHMODE}},
            {%- endif -%}
        {#- --- 条件可选：AFTYPE=ipv4uni/ipv4vpn/ipv6vpn 时可选 --- -#}
        {%- elif item.AFTYPE in ['ipv4uni', 'ipv4vpn', 'ipv6vpn'] -%}
            {%- if item.DEFAULTRTMATCHMODE is not none -%}
                DEFAULTRTMATCHMODE={{item.DEFAULTRTMATCHMODE}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：ADDRESSTYPE=ipv4/ipv6 时可选 --- -#}
        {%- if item.ADDRESSTYPE in ['ipv4', 'ipv6'] -%}
            {%- if item.DISCARDEXTCOMMUNITY is not none -%}
                DISCARDEXTCOMMUNITY={{item.DISCARDEXTCOMMUNITY}},
            {%- endif -%}
        {#- --- 条件可选：AFTYPE=ipv4uni 时可选 --- -#}
        {%- elif item.AFTYPE == 'ipv4uni' -%}
            {%- if item.DISCARDEXTCOMMUNITY is not none -%}
                DISCARDEXTCOMMUNITY={{item.DISCARDEXTCOMMUNITY}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：ADDRESSTYPE=ipv4/ipv6 时可选 --- -#}
        {%- if item.ADDRESSTYPE in ['ipv4', 'ipv6'] -%}
            {%- if item.EXPORTACL6NAMEORNUM is not none -%}
                EXPORTACL6NAMEORNUM="{{item.EXPORTACL6NAMEORNUM}}",
            {%- endif -%}
        {#- --- 条件可选：AFTYPE=ipv6vpn 时可选 --- -#}
        {%- elif item.AFTYPE == 'ipv6vpn' -%}
            {%- if item.EXPORTACL6NAMEORNUM is not none -%}
                EXPORTACL6NAMEORNUM="{{item.EXPORTACL6NAMEORNUM}}",
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：AFTYPE=ipv4uni/ipv4vpn 时可选 --- -#}
        {%- if item.AFTYPE in ['ipv4uni', 'ipv4vpn'] -%}
            {%- if item.EXPORTACLNAMEORNUM is not none -%}
                EXPORTACLNAMEORNUM="{{item.EXPORTACLNAMEORNUM}}",
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：ADDRESSTYPE=ipv4/ipv6 时可选 --- -#}
        {%- if item.ADDRESSTYPE in ['ipv4', 'ipv6'] -%}
            {%- if item.EXPORTASPATHFILTER is not none -%}
                EXPORTASPATHFILTER="{{item.EXPORTASPATHFILTER}}",
            {%- endif -%}
        {#- --- 条件可选：AFTYPE=ipv4uni/ipv4vpn/ipv6vpn 时可选 --- -#}
        {%- elif item.AFTYPE in ['ipv4uni', 'ipv4vpn', 'ipv6vpn'] -%}
            {%- if item.EXPORTASPATHFILTER is not none -%}
                EXPORTASPATHFILTER="{{item.EXPORTASPATHFILTER}}",
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：ADDRESSTYPE=ipv6 时可选 --- -#}
        {%- if item.ADDRESSTYPE == 'ipv6' -%}
            {%- if item.EXPORTPREF6FILTNAME is not none -%}
                EXPORTPREF6FILTNAME="{{item.EXPORTPREF6FILTNAME}}",
            {%- endif -%}
        {#- --- 条件可选：AFTYPE=ipv6vpn 时可选 --- -#}
        {%- elif item.AFTYPE == 'ipv6vpn' -%}
            {%- if item.EXPORTPREF6FILTNAME is not none -%}
                EXPORTPREF6FILTNAME="{{item.EXPORTPREF6FILTNAME}}",
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：AFTYPE=ipv4uni/ipv4vpn 时可选 --- -#}
        {%- if item.AFTYPE in ['ipv4uni', 'ipv4vpn'] -%}
            {%- if item.EXPORTPREFFILTNAME is not none -%}
                EXPORTPREFFILTNAME="{{item.EXPORTPREFFILTNAME}}",
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：ADDRESSTYPE=ipv4/ipv6 时可选 --- -#}
        {%- if item.ADDRESSTYPE in ['ipv4', 'ipv6'] -%}
            {%- if item.EXPORTRTPOLICYNAME is not none -%}
                EXPORTRTPOLICYNAME="{{item.EXPORTRTPOLICYNAME}}",
            {%- endif -%}
        {#- --- 条件可选：AFTYPE=ipv4uni/ipv4vpn/ipv6vpn 时可选 --- -#}
        {%- elif item.AFTYPE in ['ipv4uni', 'ipv4vpn', 'ipv6vpn'] -%}
            {%- if item.EXPORTRTPOLICYNAME is not none -%}
                EXPORTRTPOLICYNAME="{{item.EXPORTRTPOLICYNAME}}",
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：ADDRESSTYPE=ipv4/ipv6 时可选 --- -#}
        {%- if item.ADDRESSTYPE in ['ipv4', 'ipv6'] -%}
            {%- if item.IMPORTACL6NAMEORNUM is not none -%}
                IMPORTACL6NAMEORNUM="{{item.IMPORTACL6NAMEORNUM}}",
            {%- endif -%}
        {#- --- 条件可选：AFTYPE=ipv6vpn 时可选 --- -#}
        {%- elif item.AFTYPE == 'ipv6vpn' -%}
            {%- if item.IMPORTACL6NAMEORNUM is not none -%}
                IMPORTACL6NAMEORNUM="{{item.IMPORTACL6NAMEORNUM}}",
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：AFTYPE=ipv4uni/ipv4vpn 时可选 --- -#}
        {%- if item.AFTYPE in ['ipv4uni', 'ipv4vpn'] -%}
            {%- if item.IMPORTACLNAMEORNUM is not none -%}
                IMPORTACLNAMEORNUM="{{item.IMPORTACLNAMEORNUM}}",
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：ADDRESSTYPE=ipv4/ipv6 时可选 --- -#}
        {%- if item.ADDRESSTYPE in ['ipv4', 'ipv6'] -%}
            {%- if item.IMPORTASPATHFILTER is not none -%}
                IMPORTASPATHFILTER="{{item.IMPORTASPATHFILTER}}",
            {%- endif -%}
        {#- --- 条件可选：AFTYPE=ipv4uni/ipv4vpn/ipv6vpn 时可选 --- -#}
        {%- elif item.AFTYPE in ['ipv4uni', 'ipv4vpn', 'ipv6vpn'] -%}
            {%- if item.IMPORTASPATHFILTER is not none -%}
                IMPORTASPATHFILTER="{{item.IMPORTASPATHFILTER}}",
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：ADDRESSTYPE=ipv6 时可选 --- -#}
        {%- if item.ADDRESSTYPE == 'ipv6' -%}
            {%- if item.IMPORTPREF6FILTNAME is not none -%}
                IMPORTPREF6FILTNAME="{{item.IMPORTPREF6FILTNAME}}",
            {%- endif -%}
        {#- --- 条件可选：AFTYPE=ipv6vpn 时可选 --- -#}
        {%- elif item.AFTYPE == 'ipv6vpn' -%}
            {%- if item.IMPORTPREF6FILTNAME is not none -%}
                IMPORTPREF6FILTNAME="{{item.IMPORTPREF6FILTNAME}}",
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：AFTYPE=ipv4uni/ipv4vpn 时可选 --- -#}
        {%- if item.AFTYPE in ['ipv4uni', 'ipv4vpn'] -%}
            {%- if item.IMPORTPREFFILTNAME is not none -%}
                IMPORTPREFFILTNAME="{{item.IMPORTPREFFILTNAME}}",
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：ADDRESSTYPE=ipv4/ipv6 时可选 --- -#}
        {%- if item.ADDRESSTYPE in ['ipv4', 'ipv6'] -%}
            {%- if item.IMPORTRTPOLICYNAME is not none -%}
                IMPORTRTPOLICYNAME="{{item.IMPORTRTPOLICYNAME}}",
            {%- endif -%}
        {#- --- 条件可选：AFTYPE=ipv4uni/ipv4vpn/ipv6vpn 时可选 --- -#}
        {%- elif item.AFTYPE in ['ipv4uni', 'ipv4vpn', 'ipv6vpn'] -%}
            {%- if item.IMPORTRTPOLICYNAME is not none -%}
                IMPORTRTPOLICYNAME="{{item.IMPORTRTPOLICYNAME}}",
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：ADDRESSTYPE=ipv4/ipv6 时可选 --- -#}
        {%- if item.ADDRESSTYPE in ['ipv4', 'ipv6'] -%}
            {%- if item.INCLUDEPEERAS is not none -%}
                INCLUDEPEERAS={{item.INCLUDEPEERAS}},
            {%- endif -%}
        {#- --- 条件可选：AFTYPE=ipv4uni/ipv4vpn/ipv6vpn 时可选 --- -#}
        {%- elif item.AFTYPE in ['ipv4uni', 'ipv4vpn', 'ipv6vpn'] -%}
            {%- if item.INCLUDEPEERAS is not none -%}
                INCLUDEPEERAS={{item.INCLUDEPEERAS}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：ADDRESSTYPE=ipv4 时可选 --- -#}
        {%- if item.ADDRESSTYPE == 'ipv4' -%}
            {%- if item.ISSOURELAYNEIGHINTER is not none -%}
                ISSOURELAYNEIGHINTER={{item.ISSOURELAYNEIGHINTER}},
            {%- endif -%}
        {#- --- 条件可选：AFTYPE=ipv4uni 时可选 --- -#}
        {%- elif item.AFTYPE == 'ipv4uni' -%}
            {%- if item.ISSOURELAYNEIGHINTER is not none -%}
                ISSOURELAYNEIGHINTER={{item.ISSOURELAYNEIGHINTER}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：ADDRESSTYPE=ipv4/ipv6 时可选 --- -#}
        {%- if item.ADDRESSTYPE in ['ipv4', 'ipv6'] -%}
            {%- if item.KEEPALLROUTES is not none -%}
                KEEPALLROUTES={{item.KEEPALLROUTES}},
            {%- endif -%}
        {#- --- 条件可选：AFTYPE=ipv4uni/ipv4vpn/ipv6vpn 时可选 --- -#}
        {%- elif item.AFTYPE in ['ipv4uni', 'ipv4vpn', 'ipv6vpn'] -%}
            {%- if item.KEEPALLROUTES is not none -%}
                KEEPALLROUTES={{item.KEEPALLROUTES}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：ADDRESSTYPE=ipv4/ipv6 时可选 --- -#}
        {%- if item.ADDRESSTYPE in ['ipv4', 'ipv6'] -%}
            {%- if item.NEXTHOPCONFIGURE is not none -%}
                NEXTHOPCONFIGURE={{item.NEXTHOPCONFIGURE}},
            {%- endif -%}
        {#- --- 条件可选：AFTYPE=ipv4uni/ipv4vpn/ipv6vpn 时可选 --- -#}
        {%- elif item.AFTYPE in ['ipv4uni', 'ipv4vpn', 'ipv6vpn'] -%}
            {%- if item.NEXTHOPCONFIGURE is not none -%}
                NEXTHOPCONFIGURE={{item.NEXTHOPCONFIGURE}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：ADDRESSTYPE=ipv4/ipv6 时可选 --- -#}
        {%- if item.ADDRESSTYPE in ['ipv4', 'ipv6'] -%}
            {%- if item.PEERGROUPNAME is not none -%}
                PEERGROUPNAME="{{item.PEERGROUPNAME}}",
            {%- endif -%}
        {#- --- 条件可选：AFTYPE=ipv4uni/ipv4vpn/ipv6vpn 时可选 --- -#}
        {%- elif item.AFTYPE in ['ipv4uni', 'ipv4vpn', 'ipv6vpn'] -%}
            {%- if item.PEERGROUPNAME is not none -%}
                PEERGROUPNAME="{{item.PEERGROUPNAME}}",
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：ADDRESSTYPE=ipv4/ipv6 时可选 --- -#}
        {%- if item.ADDRESSTYPE in ['ipv4', 'ipv6'] -%}
            {%- if item.PREFERREDVALUE is not none -%}
                PREFERREDVALUE={{item.PREFERREDVALUE}},
            {%- endif -%}
        {#- --- 条件可选：AFTYPE=ipv4uni/ipv4vpn/ipv6vpn 时可选 --- -#}
        {%- elif item.AFTYPE in ['ipv4uni', 'ipv4vpn', 'ipv6vpn'] -%}
            {%- if item.PREFERREDVALUE is not none -%}
                PREFERREDVALUE={{item.PREFERREDVALUE}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：ADDRESSTYPE=ipv4/ipv6 时可选 --- -#}
        {%- if item.ADDRESSTYPE in ['ipv4', 'ipv6'] -%}
            {%- if item.PUBLICASONLY is not none -%}
                PUBLICASONLY={{item.PUBLICASONLY}},
            {%- endif -%}
        {#- --- 条件可选：AFTYPE=ipv4uni/ipv4vpn/ipv6vpn 时可选 --- -#}
        {%- elif item.AFTYPE in ['ipv4uni', 'ipv4vpn', 'ipv6vpn'] -%}
            {%- if item.PUBLICASONLY is not none -%}
                PUBLICASONLY={{item.PUBLICASONLY}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：ADDRESSTYPE=ipv4/ipv6 时可选 --- -#}
        {%- if item.ADDRESSTYPE in ['ipv4', 'ipv6'] -%}
            {%- if item.PUBLICASONLYFORCE is not none -%}
                PUBLICASONLYFORCE={{item.PUBLICASONLYFORCE}},
            {%- endif -%}
        {#- --- 条件可选：AFTYPE=ipv4uni/ipv4vpn/ipv6vpn 时可选 --- -#}
        {%- elif item.AFTYPE in ['ipv4uni', 'ipv4vpn', 'ipv6vpn'] -%}
            {%- if item.PUBLICASONLYFORCE is not none -%}
                PUBLICASONLYFORCE={{item.PUBLICASONLYFORCE}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：ADDRESSTYPE=ipv4/ipv6 时可选 --- -#}
        {%- if item.ADDRESSTYPE in ['ipv4', 'ipv6'] -%}
            {%- if item.PUBLICASONLYLIMITED is not none -%}
                PUBLICASONLYLIMITED={{item.PUBLICASONLYLIMITED}},
            {%- endif -%}
        {#- --- 条件可选：AFTYPE=ipv4uni/ipv4vpn/ipv6vpn 时可选 --- -#}
        {%- elif item.AFTYPE in ['ipv4uni', 'ipv4vpn', 'ipv6vpn'] -%}
            {%- if item.PUBLICASONLYLIMITED is not none -%}
                PUBLICASONLYLIMITED={{item.PUBLICASONLYLIMITED}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：ADDRESSTYPE=ipv4/ipv6 时可选 --- -#}
        {%- if item.ADDRESSTYPE in ['ipv4', 'ipv6'] -%}
            {%- if item.PUBLICASONLYREPLACE is not none -%}
                PUBLICASONLYREPLACE={{item.PUBLICASONLYREPLACE}},
            {%- endif -%}
        {#- --- 条件可选：AFTYPE=ipv4uni/ipv4vpn/ipv6vpn 时可选 --- -#}
        {%- elif item.AFTYPE in ['ipv4uni', 'ipv4vpn', 'ipv6vpn'] -%}
            {%- if item.PUBLICASONLYREPLACE is not none -%}
                PUBLICASONLYREPLACE={{item.PUBLICASONLYREPLACE}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：ADDRESSTYPE=ipv4/ipv6 时可选 --- -#}
        {%- if item.ADDRESSTYPE in ['ipv4', 'ipv6'] -%}
            {%- if item.REFLECTCLIENT is not none -%}
                REFLECTCLIENT={{item.REFLECTCLIENT}},
            {%- endif -%}
        {#- --- 条件可选：AFTYPE=ipv4uni/ipv4vpn/ipv6vpn 时可选 --- -#}
        {%- elif item.AFTYPE in ['ipv4uni', 'ipv4vpn', 'ipv6vpn'] -%}
            {%- if item.REFLECTCLIENT is not none -%}
                REFLECTCLIENT={{item.REFLECTCLIENT}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：ADDRESSTYPE=ipv4/ipv6 时可选 --- -#}
        {%- if item.ADDRESSTYPE in ['ipv4', 'ipv6'] -%}
            {%- if item.ROUTELIMIT is not none -%}
                ROUTELIMIT={{item.ROUTELIMIT}},
            {%- endif -%}
        {#- --- 条件可选：AFTYPE=ipv4uni/ipv4vpn/ipv6vpn 时可选 --- -#}
        {%- elif item.AFTYPE in ['ipv4uni', 'ipv4vpn', 'ipv6vpn'] -%}
            {%- if item.ROUTELIMIT is not none -%}
                ROUTELIMIT={{item.ROUTELIMIT}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：ADDRESSTYPE=ipv4/ipv6 时可选 --- -#}
        {%- if item.ADDRESSTYPE in ['ipv4', 'ipv6'] -%}
            {%- if item.ROUTELIMITIDLETIMEOUT is not none -%}
                ROUTELIMITIDLETIMEOUT={{item.ROUTELIMITIDLETIMEOUT}},
            {%- endif -%}
        {#- --- 条件可选：AFTYPE=ipv4uni/ipv4vpn/ipv6vpn 时可选 --- -#}
        {%- elif item.AFTYPE in ['ipv4uni', 'ipv4vpn', 'ipv6vpn'] -%}
            {%- if item.ROUTELIMITIDLETIMEOUT is not none -%}
                ROUTELIMITIDLETIMEOUT={{item.ROUTELIMITIDLETIMEOUT}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：ADDRESSTYPE=ipv4/ipv6 时可选 --- -#}
        {%- if item.ADDRESSTYPE in ['ipv4', 'ipv6'] -%}
            {%- if item.ROUTELIMITPERCENT is not none -%}
                ROUTELIMITPERCENT={{item.ROUTELIMITPERCENT}},
            {%- endif -%}
        {#- --- 条件可选：AFTYPE=ipv4uni/ipv4vpn/ipv6vpn 时可选 --- -#}
        {%- elif item.AFTYPE in ['ipv4uni', 'ipv4vpn', 'ipv6vpn'] -%}
            {%- if item.ROUTELIMITPERCENT is not none -%}
                ROUTELIMITPERCENT={{item.ROUTELIMITPERCENT}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：ADDRESSTYPE=ipv4/ipv6 时可选 --- -#}
        {%- if item.ADDRESSTYPE in ['ipv4', 'ipv6'] -%}
            {%- if item.ROUTELIMITTYPE is not none -%}
                ROUTELIMITTYPE={{item.ROUTELIMITTYPE}},
            {%- endif -%}
        {#- --- 条件可选：AFTYPE=ipv4uni/ipv4vpn/ipv6vpn 时可选 --- -#}
        {%- elif item.AFTYPE in ['ipv4uni', 'ipv4vpn', 'ipv6vpn'] -%}
            {%- if item.ROUTELIMITTYPE is not none -%}
                ROUTELIMITTYPE={{item.ROUTELIMITTYPE}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：ADDRESSTYPE=ipv4/ipv6 时可选 --- -#}
        {%- if item.ADDRESSTYPE in ['ipv4', 'ipv6'] -%}
            {%- if item.RTUPDTINTERVAL is not none -%}
                RTUPDTINTERVAL={{item.RTUPDTINTERVAL}},
            {%- endif -%}
        {#- --- 条件可选：AFTYPE=ipv4uni 时可选 --- -#}
        {%- elif item.AFTYPE == 'ipv4uni' -%}
            {%- if item.RTUPDTINTERVAL is not none -%}
                RTUPDTINTERVAL={{item.RTUPDTINTERVAL}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：ADDRESSTYPE=ipv6 时可选 --- -#}
        {%- if item.ADDRESSTYPE == 'ipv6' -%}
            {%- if item.SUBSTITUTEASENABLE is not none -%}
                SUBSTITUTEASENABLE={{item.SUBSTITUTEASENABLE}},
            {%- endif -%}
        {#- --- 条件可选：AFTYPE=ipv4uni/ipv4vpn/ipv6vpn 时可选 --- -#}
        {%- elif item.AFTYPE in ['ipv4uni', 'ipv4vpn', 'ipv6vpn'] -%}
            {%- if item.SUBSTITUTEASENABLE is not none -%}
                SUBSTITUTEASENABLE={{item.SUBSTITUTEASENABLE}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 14.4 增加入不转板策略自动化配置模板。

```jinja2
{%- if is_scenario_inbound -%}
    {%- for item in add_autoscalingbgplf_list_2 -%}
        ADD AUTOSCALINGBGPLF:
        {#- --- 必选参数 --- -#}
        POLICYNAME="{{item.POLICYNAME}}",
        IPVERSION={{item.IPVERSION}},
        SERVICENAME="{{item.SERVICENAME}}",
        {#- --- 可选参数 --- -#}
        {%- if item.PEERCOMMUNITY is not none -%}
            PEERCOMMUNITY={{item.PEERCOMMUNITY}},
        {%- endif -%}
        {%- if item.UDADVCOMENABLE is not none -%}
            UDADVCOMENABLE={{item.UDADVCOMENABLE}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：IPVERSION=IPv4 时必选 --- -#}
        {%- if item.IPVERSION == 'IPv4' -%}
            PEERIP="{{item.PEERIP}}",
        {%- endif -%}
        {#- --- 条件必选：UDADVCOMENABLE=TRUE 时必选 --- -#}
        {%- if item.UDADVCOMENABLE == 'TRUE' -%}
            UDADVCOM="{{item.UDADVCOM}}",
        {%- endif -%}
        {#- --- 条件必选：IPVERSION=IPv6 时必选 --- -#}
        {%- if item.IPVERSION == 'IPv6' -%}
            PEERIPV6="{{item.PEERIPV6}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 14.5 增加IP可达性检测自动化配置模板。

```jinja2
{%- if is_scenario_inbound -%}
    {%- for item in add_autoscalingipreach_list_2 -%}
        ADD AUTOSCALINGIPREACH:
        {#- --- 必选参数 --- -#}
        SERVICENAME="{{item.SERVICENAME}}",
        IPVERSION={{item.IPVERSION}},
        BFDTEMPLATENAME="{{item.BFDTEMPLATENAME}}",
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：IPVERSION=IPv4 时必选 --- -#}
        {%- if item.IPVERSION == 'IPv4' -%}
            DESTADDR4="{{item.DESTADDR4}}",
        {%- endif -%}
        {#- --- 条件必选：IPVERSION=IPv6 时必选 --- -#}
        {%- if item.IPVERSION == 'IPv6' -%}
            DESTADDR6="{{item.DESTADDR6}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 15 参考步骤 8，打开自动部署开关。


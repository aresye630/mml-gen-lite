---
id: ''
name: BGP over静态路由+BFD(IPv6)
ne_type: UEG
type: feature
description: SDN场景，VNF和DC-GW间通过Loopback IP建立eBGP邻居，用于业务路由的学习和发布。Loopback IP之间通过静态路由互通。
tags: []
risk_level: ''
doc_source:
  - ["网络部署","园区入驻+地市共享（连接+计算）","5GC toB 部署边缘站点（站点为“风筝S”，带计算）","UEG初始配置（风筝S）","初始配置与调测（共享式UPF）","初始配置与调测（共享式边缘UPF，SDN）","参考：详细配置指导","组网路由配置","配置VNF侧IP路由（SDN）","BGP over静态路由+BFD(IPv6)"]
  - ["网络部署","园区入驻+地市共享（连接+计算）","5GC toB 部署边缘站点（站点为“风筝S”，带计算）","UEG初始配置（风筝S）","初始配置与调测（入驻式UPF）","初始配置与调测（入驻式边缘UPF，SDN）","参考：详细配置指导","组网路由配置","配置VNF侧IP路由（SDN）","BGP over静态路由+BFD(IPv6)"]
refs: []
metadata:
  DepOnLiveCfg: true
allowed-tools:
- getParameterValue('LST AUTOCONFIG')
---
<!-- @mml:block= annotations -->
```text
## 操作场景
SDN场景，VNF和DC-GW间通过Loopback IP建立eBGP邻居，用于业务路由的学习和发布。Loopback IP之间通过静态路由互通。

## 必备事项
前提条件

* 请阅读并熟悉特性IPFD-014003 静态路由、IPFD-014002 支持BGP特性概述和IPFD-104403 BFD特性概述。
* 具备管理员权限的操作人员已经登录华为操作维护系统。
* VNF与网络实体之间的网络环境已经构建完成。
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
    set_dhcp6clientduid_list:
      type: items
      properties:
        DUIDTYPE:
          name: 'DUID生成方式'
          type: string
          enum:
          - MAC_PLUS_INTERFACE
          - MAC_PLUS_VLAN
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
          description: 'SR-IOV bonding组网需要规划。 只有MAC地址一样的vNIC才能加到同一个TRUNK里。'
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
          description: '一个UPF对接的所有企业总共规划使用65到128 VPN专线时，则N6口需要配置“NETWORKINSTID”参数。其他场景，不需要规划该参数。 一个网络分组标识最多和64个VPN实例绑定。一个UPF当前最多支持128个VPN专线。 该参数取值必须与VNFD模板中定义的网络分组ID一致。此处样例值0仅用于示例。'
          data_source: '参见“5G Core垂直网设LLD文档 > 5G Core业务IP对接设计 > ”NetworkID'
          pattern: ''
          default: 0
        ADDRMODE:
          name: '地址模式'
          type: string
          enum:
          - HOST_MODE
          - NETWOKSEGMENT_MODE
          required: false
          description: '“IPALLOCTYPE6”配置为“DHCP”时使用样例值。'
          data_source: '固定取值'
          pattern: ''
          default: HOST_MODE
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
          description: '一个UPF对接的所有企业总共规划使用65到128 VPN专线时，则N6口需要配置“NETWORKINSTID”参数。其他场景，不需要规划该参数。 一个网络分组标识最多和64个VPN实例绑定。一个UPF当前最多支持128个VPN专线。 该参数取值必须与VNFD模板中定义的网络分组ID一致。此处样例值0仅用于示例。'
          data_source: '参见“5G Core垂直网设LLD文档 > 5G Core业务IP对接设计 > ”NetworkID'
          pattern: ''
          default: 0
        ADDRMODE:
          name: '地址模式'
          type: string
          enum:
          - HOST_MODE
          - NETWOKSEGMENT_MODE
          required: false
          description: '“IPALLOCTYPE6”配置为“DHCP”时使用样例值。'
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
        DESTADDR6:
          name: '目的地址'
          type: string
          maxLength: 39
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
        PREFIX6:
          name: '路由前缀'
          type: string
          maxLength: 39
          required: false
          description: 'BGP对等体地址。 “路由前缀（PREFIX6）”与**ADD BGPPEER**命令中的“PEERADDRV6”相同。'
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
        NEXTHOPALLOCTYPE6:
          name: 'IPv6路由下一跳分配方式'
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
          description: ''
          data_source: ''
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
          description: '如果规划Loopback接口使用IPv4v6双栈地址，则分别执行**ADD IFIPV4ADDRESS**和**ADD IFIPV6ADDRESS**对同一Loopback接口配置IPv4和IPv6地址。'
          data_source: '参见“5G Core垂直网设LLD文档 > 路由设计 > BGP设计”'
          pattern: ''
          default: ''
        PREFIXLEN:
          name: 'IPv6地址前缀'
          type: integer
          minimum: 1
          maximum: 128
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
        PEERADDRV6:
          name: 'IPv6对等体地址'
          type: string
          maxLength: 39
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
          description: '“EBGP最大跳数”必须不小于到Peer之间的实际跳数。 如最大跳数设置过小，会导致BGP邻居建立失败。'
          data_source: '本端规划'
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
          description: ''
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
  examples:
    add_l3vpninst_list:
    - VRFNAME: 'VRF_Access'
    add_vpninstaf_list:
    - VRFNAME: 'VRF_Access'
      AFTYPE: ipv6uni
      VRFRD: '10.10.10.78:100'
    mod_vpninstaf_list:
    - VRFNAME: 'VRF_Access'
      AFTYPE: ipv6uni
      VRFRD: '10.10.10.78:100'
    set_bfd_list:
    - BFDENABLE: TRUE
    set_dhcp6clientduid_list:
    - DUIDTYPE: MAC_PLUS_VLAN
    set_autoconfig_list:
    - SWITCHFLAG: FALSE
    add_autoscalingethtrunk_list:
    - ETHTRUNKTMPID: 1
      VNICLIST: '4 5'
    add_autoscalingservice_list:
    - SERVICENAME: 'ServName_Access_100_v6'
      VPNNAME: 'VRF_Access'
      AFTYPE: IPv6
      IPALLOCTYPE6: DHCP
      AUTOCFGIFTYPE: VNIC
      VNICID: 4
      VLANID: 100
      NETWORKINSTID: 0
      ADDRMODE: NETWOKSEGMENT_MODE
      ETHTRUNKTMPID: 1
    add_autoscalingservice_list_2:
    - SERVICENAME: 'ServName_Access_100_v6'
      VPNNAME: 'VRF_Access'
      AFTYPE: IPv6
      IPALLOCTYPE6: DHCP
      AUTOCFGIFTYPE: ETHTRUNK
      ETHTRUNKTMPID: 1
      VLANID: 100
      NETWORKINSTID: 0
      ADDRMODE: NETWOKSEGMENT_MODE
    add_autoscalingbfd_list:
    - TEMPLATENAME: 'BFD_3'
      BFDTYPE: Static
      SERVICENAME: 'ServName_Access_100_v6'
      IPVERSION: IPv6
      DESTADDR6: 'FC00::85:130'
      MINECHORXINT: 500
      DETECTMULTI: 4
      ONEARMECHO: TRUE
    add_autoscalingsrroute_list:
    - SERVICENAME: 'ServName_Access_100_v6'
      VRFNAME: 'VRF_Access'
      IPVERSION: IPv6
      PREFIX6: 'FC00::20:78'
      MASKLENGTH: 128
      NEXTHOPALLOCTYPE6: DHCP
      PREFERENCE: 60
      BFDENABLE: TRUE
      BFDTEMPLATENAME: 'BFD_3'
    set_autoconfig_list_1:
    - SWITCHFLAG: TRUE
    set_bgp_list:
    - BGPENABLE: TRUE
      ASNUM: '60001'
    add_interface_list:
    - IFNAME: 'Loopback1'
    add_ipbindvpn_list:
    - IFNAME: 'Loopback1'
      VRFNAME: 'VRF_Access'
    set_ifipv6enable_list:
    - IFNAME: 'Loopback1'
      ENABLEFLAG: TRUE
    add_ifipv6address_list:
    - IFNAME: 'Loopback1'
      IPV6ADDRESS: 'FC00::10:78'
      PREFIXLEN: 128
    add_bgpvrf_list:
    - VRFNAME: 'VRF_Access'
      DEFAULTAFTYPE: noaf
      ROUTERID: '10.10.10.78'
    add_bgpvrfaf_list:
    - VRFNAME: 'VRF_Access'
      AFTYPE: ipv6uni
      MAXIMUMLOADBALANCE: 2
    add_bgppeer_list:
    - VRFNAME: 'VRF_Access'
      ADDRESSTYPE: ipv6
      PEERADDRV6: 'FC00::20:78'
      REMOTEAS: '60002'
      LOCALIFADDR: 'FC00::10:78'
      LOCALIFNAME: 'Loopback1'
      EBGPMAXHOP: 10
    add_importroute_list:
    - VRFNAME: 'VRF_Access'
      AFTYPE: ipv6uni
      IMPORTPROTOCOL: wlr
      MEDENABLE: FALSE
```

## 3 命令模板定义
<!-- @mml:block= commands -->

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

### 3 DHCP分配IPv6地址时 （如：SDN场景），必须设置“DUID生成方式（DUIDTYPE）”为“MAC\_PLUS\_VLAN”。

```jinja2
{%- for item in set_dhcp6clientduid_list -%}
    SET DHCP6CLIENTDUID:
    {#- --- 必选参数 --- -#}
    DUIDTYPE={{item.DUIDTYPE}},
    ;
{%- endfor -%}
```

### 4 关闭自动配置开关。

#### 4.1 查询自动配置开关。

#### 如果“自动配置开关”值为“TRUE”，需要执行4.b和4.c关闭自动配置开关。

#### 如果“自动配置开关”值为“FALSE”，说明已关闭自动配置开关，请跳转到5。

#### 4.2 查询自动部署维护助手“autoscaling\_autoconfig.py”的状态，确保状态为“准备好状态（Ready）”或者查询无该脚本，以保证当前设备不在自动部署过程中。因为若系统当前有正在进行的自动部署，而自动部署生效有时延，此时若关闭自动配置开关，会影响系统配置效果。

#### 4.3 关闭自动配置开关。自动化配置命令只有在自动配置开关为关闭的状态下才可执行，因此需要提前关闭。

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

### 5 接口采用SR-IOV bonding组网时，添加以太网隧道多虚拟网卡自动化配置模板。

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

### 6 配置外联口自动部署模板。

### 一个UPF对接的所有企业总共规划使用65到128 VPN专线时，则N6口需要配置“NETWORKINSTID”参数。其他场景，不需要规划该参数。

#### 6.1 非SR-IOV bonding组网场景下：

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
        {#- --- 条件必选：AUTOCFGIFTYPE=ETHTRUNK 时必选 --- -#}
        {%- if item.AUTOCFGIFTYPE == 'ETHTRUNK' -%}
            ETHTRUNKTMPID={{item.ETHTRUNKTMPID}},
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
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
{%- endif -%}
```

#### 6.2 SR-IOV bonding组网场景下：

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
        {#- --- 条件可选参数 --- -#}
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
{%- endif -%}
```

#### 外联口配置IPv6地址时，“ADDRMODE”必须设置为“NETWOKSEGMENT\_MODE”。

### 7 增加BFD会话自动部署模板。

### “DESTADDR6”配置的是Leaf节点的IP地址，采用的是单臂BFD。

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

### 8 增加静态路由自动部署模板。

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
    {#- --- 条件必选：IPVERSION=IPv6 时必选 --- -#}
    {%- if item.IPVERSION == 'IPv6' -%}
        PREFIX6="{{item.PREFIX6}}",
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

### 9 打开自动部署开关。

```jinja2
{%- for item in set_autoconfig_list_1 -%}
    SET AUTOCONFIG:
    {#- --- 必选参数 --- -#}
    SWITCHFLAG={{item.SWITCHFLAG}},
    ;
{%- endfor -%}
```

### 10 全局激活BGP。

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

### “ASNUM”参数若需要变更，则需先去使能BGP功能。去使能BGP时，BGP VPN实例等配置会被同步删除。必须按照LLD规划的“ASNUM”值进行配置。

### 11 配置Loopback接口地址（BGP本端IP）。

#### 11.1 配置Loopback接口。

```jinja2
{%- for item in add_interface_list -%}
    ADD INTERFACE:
    {#- --- 必选参数 --- -#}
    IFNAME="{{item.IFNAME}}",
    ;
{%- endfor -%}
```

#### 11.2 配置接口绑定VPN。

```jinja2
{%- for item in add_ipbindvpn_list -%}
    ADD IPBINDVPN:
    {#- --- 必选参数 --- -#}
    IFNAME="{{item.IFNAME}}",
    VRFNAME="{{item.VRFNAME}}",
    ;
{%- endfor -%}
```

#### 11.3 配置接口IP地址。

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

### 12 配置BGP。

#### 12.1 增加BGP VPN实例。

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

#### 12.2 增加BGP VPN地址族。VNF对接2个负荷分担的BGP邻居时，“MAXIMUMLOADBALANCE”设置为“2”。

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

#### 12.3 增加BGP对等体。

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

#### 12.4 增加BGP引入路由。

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

#### 由于BGP协议自身不能发现路由，所以需要引入其他协议的路由（如OSPF、静态路由或WLR等）注入到BGP路由表中，从而将这些路由在AS之内和AS之间传播。


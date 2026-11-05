---
id: ''
name: 配置BGP/MPLS VPN（非SDN_手动）
ne_type: UEG
type: feature
description: 非SDN场景，UEG与企业网对接时，由于企业APN数量多，且各个企业APN之间有业务隔离诉求，故可采用BGP/MPLS VPN组网。UEG作为PE设备接入MPLS骨干网，通过MP-EBGP（Multi-protocol Extensions for Border Gateway Protocol）与其他PE之间传播VPN信息和VPN-IPv4路由。UEG采用OptionB方式实现跨域VPN。  如图1所示，UEG和PE间通过Loopback IP建立eBGP邻居，用于交换私网VPN路由。Loopback IP之间通过静态路由/OSPF互通。  **图1** BGP/MPLS VPN组网
tags: []
risk_level: ''
doc_source: ["网络部署","园区入驻式（仅连接）","5GC toB 部署边缘站点（站点为“风筝L”，入驻式）","UEG初始配置（风筝L）","参考：详细配置指导","组网路由配置（虚机容器）","配置VNF侧IP路由数据","手动部署","配置BGP/MPLS VPN（非SDN_手动）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
非SDN场景，UEG与企业网对接时，由于企业APN数量多，且各个企业APN之间有业务隔离诉求，故可采用BGP/MPLS VPN组网。UEG作为PE设备接入MPLS骨干网，通过MP-EBGP（Multi-protocol Extensions for Border Gateway Protocol）与其他PE之间传播VPN信息和VPN-IPv4路由。UEG采用OptionB方式实现跨域VPN。如图1所示，UEG和PE间通过Loopback IP建立eBGP邻居，用于交换私网VPN路由。Loopback IP之间通过静态路由/OSPF互通。**图1** BGP/MPLS VPN组网

## 必备事项
前提条件

前提条件

* 请阅读并熟悉特性GWFD-023001 MPLS VPN、IPFD-020502 支持BGP和IPFD-020403 BFD特性概述。
* 具备管理员权限的操作人员已经登录华为操作维护系统。
* UEG与网络实体之间的网络环境已经构建完成。
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
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
        ASNUM:
          name: 'BGP自治域号'
          type: string
          maxLength: 11
          required: false
          description: '使能BGP全局配置。'
          data_source: '参见“5G Core LLD文档 > 路由设计 > BGP设计 > AS号（VNF）”。'
          pattern: ''
          default: ''
    set_mplssite_list:
      type: items
      properties:
        MPLSLSRID:
          name: 'MPLS LSR ID'
          type: string
          maxLength: 15
          required: false
          description: '“MPLSLSRID”取值使用不绑定私网VPN的Loopback接口地址。'
          data_source: '参见“5G Core LLD文档 > 路由设计 > BGP设计 > Local interface address（VNF）”。'
          pattern: ''
          default: ''
        MPLSENABLE:
          name: 'MPLS能力'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '使能MPLS全局配置。  开启MPLS能力，不开启LDP能力。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        LDPENABLE:
          name: 'LDP能力'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
    add_mplsif_list:
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
    add_mplsif_list_4:
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
    add_mplsif_list_8:
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
    add_mplsif_list_10:
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
    add_mplsif_list_12:
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
    add_l3vpninst_list:
      type: items
      properties:
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: true
          description: '创建企业使用的VPN实例。  请根据实际业务IP类型，规划ipv4uni、ipv6uni或ipv4uni&ipv6uni的L3VPN实例地址族。'
          data_source: '全网规划'
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
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VRFRD:
          name: '路由标识'
          type: string
          maxLength: 21
          required: false
          description: '**MPLS OptionB必须配置“VRFRD”值。**  不同VPN实例的路由标识必须不同。  此处以“VRFLABELMODE”设置为“perInstance”为例，即每VPN实例分配一个标签。设置为“perInstance”比设置为“perRoute”节省标签资源。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        VRFLABELMODE:
          name: '实例的标签分配模式'
          type: string
          enum:
          - perInstance
          - perInstanceStatic
          - perRoute
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: perRoute
    add_vpninstaf_list_5:
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
          description: '**MPLS OptionB必须配置“VRFRD”值。**  不同VPN实例的路由标识必须不同。  此处以“VRFLABELMODE”设置为“perInstance”为例，即每VPN实例分配一个标签。设置为“perInstance”比设置为“perRoute”节省标签资源。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        VRFLABELMODE:
          name: '实例的标签分配模式'
          type: string
          enum:
          - perInstance
          - perInstanceStatic
          - perRoute
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: perRoute
    add_vpntarget_list:
      type: items
      properties:
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: true
          description: 'VPN Target属性定义了一条VPN路由可以被哪些对端设备所接收，以及本端可以接收哪些对端设备发送来的路由。'
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
          description: '-'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        VRFRTTYPE:
          name: 'VPN RT类型'
          type: string
          enum:
          - export_extcommunity
          - import_extcommunity
          required: true
          description: 'Export Target属性作为BGP的扩展团体属性随路由发布。  对端设备接收后，将报文中携带的Export Target属性与对端设备上配置的Import Target进行匹配，匹配成功后，将路由添加到对应的VPN实例的路由表中。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        VRFRTVALUE:
          name: 'VPN RT的值'
          type: string
          maxLength: 21
          required: true
          description: ''
          data_source: '与对端协商'
          pattern: ''
          default: ''
    add_vpntarget_list_10:
      type: items
      properties:
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: true
          description: 'VPN Target属性定义了一条VPN路由可以被哪些对端设备所接收，以及本端可以接收哪些对端设备发送来的路由。'
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
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        VRFRTTYPE:
          name: 'VPN RT类型'
          type: string
          enum:
          - export_extcommunity
          - import_extcommunity
          required: true
          description: 'Export Target属性作为BGP的扩展团体属性随路由发布。  对端设备接收后，将报文中携带的Export Target属性与对端设备上配置的Import Target进行匹配，匹配成功后，将路由添加到对应的VPN实例的路由表中。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        VRFRTVALUE:
          name: 'VPN RT的值'
          type: string
          maxLength: 21
          required: true
          description: ''
          data_source: '与对端协商'
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
          description: 'Loopback接口IP用于和BGP peer建立BGP邻居。  不能与已存在的Loopback接口名称重复。  请根据实际组网，规划IPv4地址。**使用IPv4 eBGP，传递IPv6私网路由。Loopback接口不需要规划IPv6地址。**  **Loopback接口不用绑定VPN，即用公网BGP传递私网路由。**'
          data_source: '参见“5G Core LLD文档 > 路由设计 > BGP设计 > Local interface name（VNF）”。'
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
          description: 'Loopback接口IP用于和BGP peer建立BGP邻居。  不能与已存在的Loopback接口名称重复。  请根据实际组网，规划IPv4地址。**使用IPv4 eBGP，传递IPv6私网路由。Loopback接口不需要规划IPv6地址。**  **Loopback接口不用绑定VPN，即用公网BGP传递私网路由。**'
          data_source: '参见“5G Core LLD文档 > 路由设计 > BGP设计 > Local interface name（VNF）”。'
          pattern: ''
          default: ''
        IFIPADDR:
          name: 'IPv4地址'
          type: string
          maxLength: 15
          required: true
          description: ''
          data_source: '参见“5G Core LLD文档 > 路由设计 > BGP设计 > Local interface address（VNF）”。'
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
    mod_bgpvrf_list:
      type: items
      properties:
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: true
          description: '公网BGP VPN实例的ROUTERID。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        ROUTERID:
          name: '路由器ID'
          type: string
          maxLength: 15
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
          description: 'BGP VPN实例需要与**ADD L3VPNINST**命令配置的VPN实例名一致。'
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
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ipv4uni
    add_bgpvrfaf_list:
      type: items
      properties:
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: false
          description: '**是MP-EBGP的开关。**  **请根据实际组网，规划ipv4vpn、ipv6vpn或ipv4vpn&ipv6vpn的BGP VPN实例地址族。**'
          data_source: '固定取值'
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
          data_source: '本端规划'
          pattern: ''
          default: ''
        APPLYLABELMODE:
          name: '标签分配方式'
          type: string
          enum:
          - perNexthop
          - perRoute
          required: false
          description: '**ADD VPNINSTAF**命令中的“VRFLABELMODE”设置为“perInstance”时，“APPLYLABELMODE”需要设置为“perNexthop”，否则起不到节省标签资源的效果。'
          data_source: '本端规划'
          pattern: ''
          default: perRoute
    add_bgpvrfaf_list_1:
      type: items
      properties:
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: false
          description: '**是MP-EBGP的开关。**  **请根据实际组网，规划ipv4vpn、ipv6vpn或ipv4vpn&ipv6vpn的BGP VPN实例地址族。**'
          data_source: '固定取值'
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
          data_source: '本端规划'
          pattern: ''
          default: ''
        APPLYLABELMODE:
          name: '标签分配方式'
          type: string
          enum:
          - perNexthop
          - perRoute
          required: false
          description: '**ADD VPNINSTAF**命令中的“VRFLABELMODE”设置为“perInstance”时，“APPLYLABELMODE”需要设置为“perNexthop”，否则起不到节省标签资源的效果。'
          data_source: '本端规划'
          pattern: ''
          default: perRoute
    add_bgpvrfaf_list_2:
      type: items
      properties:
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: false
          description: 'BGP VPN实例需要与**ADD BGPVRF**命令配置的VPN实例名一致。'
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
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        MAXIMUMLOADBALANCE:
          name: '最大等价路由数'
          type: integer
          minimum: 1
          maximum: 128
          required: false
          description: '对接的负荷分担关系的BGP peer数。'
          data_source: '本端规划'
          pattern: ''
          default: 1
    add_bgpvrfaf_list_7:
      type: items
      properties:
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: false
          description: 'BGP VPN实例需要与**ADD BGPVRF**命令配置的VPN实例名一致。'
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
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        MAXIMUMLOADBALANCE:
          name: '最大等价路由数'
          type: integer
          minimum: 1
          maximum: 128
          required: false
          description: '对接的负荷分担关系的BGP peer数。'
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
          description: '“EBGP最大跳数”不小于到Peer之间的实际跳数，无法确认时，可设置为10。  如最大跳数设置过小，会导致BGP邻居建立失败。  请根据实际组网，规划IPv4对等体地址。  **不需要规划IPv6对等体地址。MP-EBGP组网时，使用IPv4 eBGP，传递IPv6私网路由。**'
          data_source: '固定取值'
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
          data_source: '本端规划'
          pattern: ''
          default: ipv4
        PEERADDR:
          name: 'IPv4对等体地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '从对端获取  参见“5G Core LLD文档 > 路由设计 > BGP设计 > Local interface address（L3GW）”。'
          pattern: ''
          default: ''
        REMOTEAS:
          name: '对等体AS号'
          type: string
          maxLength: 11
          required: false
          description: ''
          data_source: '从对端获取  参见“5G Core LLD文档 > 路由设计 > BGP设计 > AS号（L3GW）”。'
          pattern: ''
          default: ''
        LOCALIFADDR:
          name: '本地接口地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        LOCALIFNAME:
          name: '本地接口名称'
          type: string
          maxLength: 63
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        EBGPMAXHOP:
          name: 'EBGP最大跳数'
          type: integer
          minimum: 1
          maximum: 255
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    rmv_bgppeeraf_list:
      type: items
      properties:
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: ''
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
          data_source: ''
          pattern: ''
          default: ''
        REMOTEADDRESS:
          name: 'IPv4对等体地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
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
    add_bgppeeraf_list:
      type: items
      properties:
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: false
          description: '-'
          data_source: '固定取值'
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
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        REMOTEADDRESS:
          name: 'IPv4对等体地址'
          type: string
          maxLength: 15
          required: false
          description: '与**ADD BGPPEER**命令中配置的BGP对等体地址相同。'
          data_source: '已配置数据中获取'
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
          default: ipv4
    add_bgppeeraf_list_2:
      type: items
      properties:
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: false
          description: '-'
          data_source: '固定取值'
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
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        REMOTEADDRESS:
          name: 'IPv4对等体地址'
          type: string
          maxLength: 15
          required: false
          description: '与**ADD BGPPEER**命令中配置的BGP对等体地址相同。'
          data_source: '已配置数据中获取'
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
          default: ipv4
    add_importroute_list:
      type: items
      properties:
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: false
          description: '使用**ADD BGPVRF**命令定义的VPN实例名称。  请根据实际组网，规划引入ipv4uni、ipv6uni或ipv4uni&ipv6uni的wlr路由。'
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
          data_source: '本端规划'
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
          data_source: '固定取值'
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
    add_importroute_list_5:
      type: items
      properties:
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: false
          description: '使用**ADD BGPVRF**命令定义的VPN实例名称。  请根据实际组网，规划引入ipv4uni、ipv6uni或ipv4uni&ipv6uni的wlr路由。'
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
          data_source: '本端规划'
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
          data_source: '固定取值'
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
    set_bfd_list:
    - BFDENABLE: TRUE
    set_bgp_list:
    - BGPENABLE: TRUE
      ASNUM: '60001'
    set_mplssite_list:
    - MPLSLSRID: '10.10.10.78'
      MPLSENABLE: ENABLE
      LDPENABLE: DISABLE
    add_mplsif_list:
    - IFNAME: 'Ethernet66/0/4.100'
    add_mplsif_list_4:
    - IFNAME: 'Eth-trunk6604.100'
    add_mplsif_list_8:
    - IFNAME: '100GE66/0/9.1'
    add_mplsif_list_10:
    - IFNAME: 'Eth-trunk1.1'
    add_mplsif_list_12:
    - IFNAME: 'Eth-trunk1.1'
    add_l3vpninst_list:
    - VRFNAME: 'VRF_PDN1'
    add_vpninstaf_list:
    - VRFNAME: 'VRF_PDN1'
      AFTYPE: ipv4uni
      VRFRD: '100:100'
      VRFLABELMODE: perInstance
    add_vpninstaf_list_5:
    - VRFNAME: 'VRF_PDN1'
      AFTYPE: ipv6uni
      VRFRD: '100:100'
      VRFLABELMODE: perInstance
    add_vpntarget_list:
    - VRFNAME: 'VRF_PDN1'
      AFTYPE: ipv4uni
      VRFRTTYPE: export_extcommunity
      VRFRTVALUE: '1:1'
    add_vpntarget_list_10:
    - VRFNAME: 'VRF_PDN1'
      AFTYPE: ipv6uni
      VRFRTTYPE: export_extcommunity
      VRFRTVALUE: '1:1'
    add_interface_list:
    - IFNAME: 'Loopback1'
    add_ifipv4address_list:
    - IFNAME: 'Loopback1'
      IFIPADDR: '10.10.10.78'
      SUBNETMASK: '255.255.255.255'
    mod_bgpvrf_list:
    - VRFNAME: '_public_'
      ROUTERID: '10.1.1.1'
    add_bgpvrf_list:
    - VRFNAME: 'VRF_PDN1'
      DEFAULTAFTYPE: noaf
    add_bgpvrfaf_list:
    - VRFNAME: '_public_'
      AFTYPE: ipv4vpn
      APPLYLABELMODE: perNexthop
    add_bgpvrfaf_list_1:
    - VRFNAME: '_public_'
      AFTYPE: ipv6vpn
      APPLYLABELMODE: perNexthop
    add_bgpvrfaf_list_2:
    - VRFNAME: 'VRF_PDN1'
      AFTYPE: ipv4uni
      MAXIMUMLOADBALANCE: 2
    add_bgpvrfaf_list_7:
    - VRFNAME: 'VRF_PDN1'
      AFTYPE: ipv6uni
      MAXIMUMLOADBALANCE: 2
    add_bgppeer_list:
    - VRFNAME: '_public_'
      ADDRESSTYPE: ipv4
      PEERADDR: '10.10.20.78'
      REMOTEAS: '60002'
      LOCALIFADDR: '10.10.10.78'
      LOCALIFNAME: 'Loopback1'
      EBGPMAXHOP: 10
    rmv_bgppeeraf_list:
    - VRFNAME: '_public_'
      AFTYPE: ipv4uni
      REMOTEADDRESS: '10.10.20.78'
      ADDRESSTYPE: ''
    add_bgppeeraf_list:
    - VRFNAME: '_public_'
      AFTYPE: ipv4vpn
      REMOTEADDRESS: '10.10.20.78'
      ADDRESSTYPE: ipv4
    add_bgppeeraf_list_2:
    - VRFNAME: '_public_'
      AFTYPE: ipv6vpn
      REMOTEADDRESS: '10.10.20.78'
      ADDRESSTYPE: ipv4
    add_importroute_list:
    - VRFNAME: 'VRF_PDN1'
      AFTYPE: ipv4uni
      IMPORTPROTOCOL: wlr
      MEDENABLE: FALSE
    add_importroute_list_5:
    - VRFNAME: 'VRF_PDN1'
      AFTYPE: ipv6uni
      IMPORTPROTOCOL: wlr
      MEDENABLE: FALSE
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 全局激活BFD。

```jinja2
{%- for item in set_bfd_list -%}
    SET BFD:
    {#- --- 必选参数 --- -#}
    BFDENABLE={{item.BFDENABLE}},
    ;
{%- endfor -%}
```

### 2 全局激活BGP。

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

### 3 配置MPLS全局配置。

```jinja2
{%- for item in set_mplssite_list -%}
    SET MPLSSITE:
    {#- --- 可选参数 --- -#}
    {%- if item.MPLSLSRID is not none -%}
        MPLSLSRID="{{item.MPLSLSRID}}",
    {%- endif -%}
    {%- if item.MPLSENABLE is not none -%}
        MPLSENABLE={{item.MPLSENABLE}},
    {%- endif -%}
    {%- if item.LDPENABLE is not none -%}
        LDPENABLE={{item.LDPENABLE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 配置外联口IP、BFD会话、和BFD绑定静态路由（到BGP PEER IP的静态路由）。

### N6外联口IP及路由数据，与非MPLS组网的差异点如下。其他配置与非MPLS组网没有差异，此处不再详细描述。

### MPLS使用的N6外联口绑定的VPN实例名称是\_public\_。

### 不需要配置IPv6数据（MP-EBGP组网时，使用IPv4 eBGP，传递IPv6私网路由）。

### UEG支持通过静态路由或OSPF动态路由实现与BGP PEER IP的互通：

### BGP over静态路由时，请参见配置静态路由+BFD组网（IPv4）。

### BGP over OSPF时，请参见配置动态路由OSPF+BFD组网（IPv4）。

### 5 使能接口的MPLS功能。

#### 5.1 （标卡）非SR-IOV bonding组网场景下：

```jinja2
{%- if is_scenario_non_sriov_bonding -%}
    {%- for item in add_mplsif_list -%}
        ADD MPLSIF:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 5.2 （标卡）SR-IOV bonding组网场景下：

```jinja2
{%- if is_scenario_sriov_bonding -%}
    {%- for item in add_mplsif_list_4 -%}
        ADD MPLSIF:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 5.3 （NP卡省交换直连PE）Ethernet子接口组网场景下：

```jinja2
{%- if is_scenario_ethernet_subif -%}
    {%- for item in add_mplsif_list_8 -%}
        ADD MPLSIF:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 5.4 （NP卡省交换直连PE，跨板Eth-trunk）Eth-trunk子接口组网场景下：

```jinja2
{%- if is_scenario_eth_trunk_subif -%}
    {%- for item in add_mplsif_list_10 -%}
        ADD MPLSIF:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 5.5 （网络加速卡直连DCGW，本板Eth-trunk）Eth-trunk子接口组网场景下：

```jinja2
{%- if is_scenario_direct_to_dcgw -%}
    {%- for item in add_mplsif_list_12 -%}
        ADD MPLSIF:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

### 6 配置VPN实例及VPN实例地址族。

```jinja2
{%- for item in add_l3vpninst_list -%}
    ADD L3VPNINST:
    {#- --- 必选参数 --- -#}
    VRFNAME="{{item.VRFNAME}}",
    ;
{%- endfor -%}
```

#### 6.1 //IPv4组网或IPv4v6组网，请执行如下脚本：

```jinja2
{%- if is_scenario_ipv4 -%}
    {%- for item in add_vpninstaf_list -%}
        ADD VPNINSTAF:
        {#- --- 必选参数 --- -#}
        VRFNAME="{{item.VRFNAME}}",
        AFTYPE={{item.AFTYPE}},
        {#- --- 可选参数 --- -#}
        {%- if item.VRFRD is not none -%}
            VRFRD="{{item.VRFRD}}",
        {%- endif -%}
        {%- if item.VRFLABELMODE is not none -%}
            VRFLABELMODE={{item.VRFLABELMODE}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 6.2 //IPv6组网或IPv4v6组网，请执行如下脚本：

```jinja2
{%- if is_scenario_ipv6 -%}
    {%- for item in add_vpninstaf_list_5 -%}
        ADD VPNINSTAF:
        {#- --- 必选参数 --- -#}
        VRFNAME="{{item.VRFNAME}}",
        AFTYPE={{item.AFTYPE}},
        {#- --- 可选参数 --- -#}
        {%- if item.VRFRD is not none -%}
            VRFRD="{{item.VRFRD}}",
        {%- endif -%}
        {%- if item.VRFLABELMODE is not none -%}
            VRFLABELMODE={{item.VRFLABELMODE}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 7 配置VPN Target。

#### 7.1 //IPv4组网或IPv4v6组网，请执行如下脚本：

```jinja2
{%- if is_scenario_ipv4 -%}
    {%- for item in add_vpntarget_list -%}
        ADD VPNTARGET:
        {#- --- 必选参数 --- -#}
        VRFNAME="{{item.VRFNAME}}",
        AFTYPE={{item.AFTYPE}},
        VRFRTTYPE={{item.VRFRTTYPE}},
        VRFRTVALUE="{{item.VRFRTVALUE}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 7.2 //IPv6组网或IPv4v6组网，请执行如下脚本：

```jinja2
{%- if is_scenario_ipv6 -%}
    {%- for item in add_vpntarget_list_10 -%}
        ADD VPNTARGET:
        {#- --- 必选参数 --- -#}
        VRFNAME="{{item.VRFNAME}}",
        AFTYPE={{item.AFTYPE}},
        VRFRTTYPE={{item.VRFRTTYPE}},
        VRFRTVALUE="{{item.VRFRTVALUE}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

### 8 配置Loopback接口（BGP本端IP）。

#### 8.1 配置Loopback接口。

```jinja2
{%- for item in add_interface_list -%}
    ADD INTERFACE:
    {#- --- 必选参数 --- -#}
    IFNAME="{{item.IFNAME}}",
    ;
{%- endfor -%}
```

#### 8.2 增加接口IPv4地址。

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

#### MP-EBGP组网中：

#### Loopback接口不绑定VPN实例。

#### BGP对等体地址仅支持IPv4类型，即不需要配置IPv6地址。

### 9 配置BGP。

#### 9.1 修改公网BGP VPN实例。

```jinja2
{%- for item in mod_bgpvrf_list -%}
    MOD BGPVRF:
    {#- --- 必选参数 --- -#}
    VRFNAME="{{item.VRFNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.ROUTERID is not none -%}
        ROUTERID="{{item.ROUTERID}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 9.2 增加BGP VPN实例。

```jinja2
{%- for item in add_bgpvrf_list -%}
    ADD BGPVRF:
    {#- --- 必选参数 --- -#}
    VRFNAME="{{item.VRFNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.DEFAULTAFTYPE is not none -%}
        DEFAULTAFTYPE={{item.DEFAULTAFTYPE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 9.3 增加BGP VPN实例地址族（使能MP-EBGP功能）。“VRFNAME”使用默认值“\_public\_”。

##### 9.3.1 //IPv4组网或IPv4v6组网，请执行如下脚本：

```jinja2
{%- if is_scenario_ipv4 -%}
    {%- for item in add_bgpvrfaf_list -%}
        ADD BGPVRFAF:
        {#- --- 必选参数 --- -#}
        AFTYPE={{item.AFTYPE}},
        {#- --- 可选参数 --- -#}
        {%- if item.VRFNAME is not none -%}
            VRFNAME="{{item.VRFNAME}}",
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：AFTYPE=ipv4vpn/ipv6vpn 时可选 --- -#}
        {%- if item.AFTYPE in ['ipv4vpn', 'ipv6vpn'] -%}
            {%- if item.APPLYLABELMODE is not none -%}
                APPLYLABELMODE={{item.APPLYLABELMODE}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 9.3.2 //IPv6组网或IPv4v6组网，请执行如下脚本：

```jinja2
{%- if is_scenario_ipv6 -%}
    {%- for item in add_bgpvrfaf_list_1 -%}
        ADD BGPVRFAF:
        {#- --- 必选参数 --- -#}
        AFTYPE={{item.AFTYPE}},
        {#- --- 可选参数 --- -#}
        {%- if item.VRFNAME is not none -%}
            VRFNAME="{{item.VRFNAME}}",
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：AFTYPE=ipv4vpn/ipv6vpn 时可选 --- -#}
        {%- if item.AFTYPE in ['ipv4vpn', 'ipv6vpn'] -%}
            {%- if item.APPLYLABELMODE is not none -%}
                APPLYLABELMODE={{item.APPLYLABELMODE}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### “AFTYPE”设置为“ipv4vpn”/“ipv6vpn”。

#### 9.4 增加BGP VPN地址族。VNF对接2个负荷分担的BGP邻居时，“MAXIMUMLOADBALANCE”设置为“2”。

##### 9.4.1 //IPv4组网或IPv4v6组网，请执行如下脚本：

```jinja2
{%- if is_scenario_ipv4 -%}
    {%- for item in add_bgpvrfaf_list_2 -%}
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
{%- endif -%}
```

##### 9.4.2 //IPv6组网或IPv4v6组网，请执行如下脚本：

```jinja2
{%- if is_scenario_ipv6 -%}
    {%- for item in add_bgpvrfaf_list_7 -%}
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
{%- endif -%}
```

#### 9.5 增加BGP对等体。

##### 9.5.1 //“VRFNAME”使用默认值“\_public\_”。使用IPv4 BGP传递IPv6路由，不需要配置IPv6的BGP对等体。

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

##### 9.5.2 //（可选）执行**ADD BGPPEER**时，若“VRFNAME”使用默认值“\_public\_”，则会自动生成ipv4uni类型的对等体地址族。如局点不需要创建ipv4uni类型的对等体地址族，可执行如下脚本进行删除。

```jinja2
{%- if is_optional_rmv_bgppeeraf -%}
    {%- for item in rmv_bgppeeraf_list -%}
        RMV BGPPEERAF:
        {#- --- 必选参数 --- -#}
        AFTYPE={{item.AFTYPE}},
        {#- --- 可选参数 --- -#}
        {%- if item.VRFNAME is not none -%}
            VRFNAME="{{item.VRFNAME}}",
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：ADDRESSTYPE=ipv4 时必选 --- -#}
        {%- if item.ADDRESSTYPE == 'ipv4' -%}
            REMOTEADDRESS="{{item.REMOTEADDRESS}}",
        {#- --- 条件必选：AFTYPE=ipv4uni/ipv4vpn/ipv6vpn 时必选 --- -#}
        {%- elif item.AFTYPE in ['ipv4uni', 'ipv4vpn', 'ipv6vpn'] -%}
            REMOTEADDRESS="{{item.REMOTEADDRESS}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 9.6 配置BGP对等体地址族。

##### 9.6.1 //IPv4组网或IPv4v6组网，请执行如下脚本：

```jinja2
{%- if is_scenario_ipv4 -%}
    {%- for item in add_bgppeeraf_list -%}
        ADD BGPPEERAF:
        {#- --- 必选参数 --- -#}
        AFTYPE={{item.AFTYPE}},
        {#- --- 可选参数 --- -#}
        {%- if item.VRFNAME is not none -%}
            VRFNAME="{{item.VRFNAME}}",
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：ADDRESSTYPE=ipv4 时必选 --- -#}
        {%- if item.ADDRESSTYPE == 'ipv4' -%}
            REMOTEADDRESS="{{item.REMOTEADDRESS}}",
        {#- --- 条件必选：AFTYPE=ipv4uni/ipv4vpn/ipv6vpn 时必选 --- -#}
        {%- elif item.AFTYPE in ['ipv4uni', 'ipv4vpn', 'ipv6vpn'] -%}
            REMOTEADDRESS="{{item.REMOTEADDRESS}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 9.6.2 //IPv6组网或IPv4v6组网，请执行如下脚本：

```jinja2
{%- if is_scenario_ipv6 -%}
    {%- for item in add_bgppeeraf_list_2 -%}
        ADD BGPPEERAF:
        {#- --- 必选参数 --- -#}
        AFTYPE={{item.AFTYPE}},
        {#- --- 可选参数 --- -#}
        {%- if item.VRFNAME is not none -%}
            VRFNAME="{{item.VRFNAME}}",
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：ADDRESSTYPE=ipv4 时必选 --- -#}
        {%- if item.ADDRESSTYPE == 'ipv4' -%}
            REMOTEADDRESS="{{item.REMOTEADDRESS}}",
        {#- --- 条件必选：AFTYPE=ipv4uni/ipv4vpn/ipv6vpn 时必选 --- -#}
        {%- elif item.AFTYPE in ['ipv4uni', 'ipv4vpn', 'ipv6vpn'] -%}
            REMOTEADDRESS="{{item.REMOTEADDRESS}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 9.7 增加BGP引入wlr路由。

##### 9.7.1 //IPv4组网或IPv4v6组网，请执行如下脚本：

```jinja2
{%- if is_scenario_ipv4 -%}
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
{%- endif -%}
```

##### 9.7.2 //IPv6组网或IPv4v6组网，请执行如下脚本：

```jinja2
{%- if is_scenario_ipv6 -%}
    {%- for item in add_importroute_list_5 -%}
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
{%- endif -%}
```

##### 由于BGP协议自身不能发现路由，所以需要引入其他协议的路由（如OSPF、静态路由或WLR等）注入到BGP路由表中，从而将这些路由在AS之内和AS之间传播。


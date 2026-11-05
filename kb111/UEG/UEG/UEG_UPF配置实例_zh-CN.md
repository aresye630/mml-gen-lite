---
id: ''
name: UPF配置实例
ne_type: UEG
type: feature
description: UEG部署在园区，作为企业专用UPF。  N3使用SR-IOV bonding组网（Eth-trunk接口），直连DCGW时，一个Eth-trunk接口的成员端口连接到DCGW1和DCGW2；直连PE时，一个Eth-trunk接口的成员端口必须连接到同一个PE设备；UEG与LocalDN使用非SR-IOV bonding组网（以太网接口），物理接口分别与两个PE/两个DCGW连接。  园区部署两套UEG实现容灾，两套UEG内各业务网元之间不交叉互连。  UEG通过BGP over静态路由+BFD与对端网元实现网络互通。  * 直连DCGW时，UEG与gNodeB之间的组网示意如图1所示。 * 直连PE时，UEG与gNodeB之间的组网示意如图2所示。 * 直连DCGW/PE时，UEG与企业园区服务器之间的组网示意如图3所示。  * 直连DCGW时，推荐使用BGP over静态路由+BFD与对端实现网络互通。 * 直连PE时，UEG支持：   + 通过BGP over静态路由+BFD与企业园区服务器之间实现网络互通。   + 通过静态路由+BFD与对端网元（gNodeB/园区服务器）实现网络互通。采用静态路由+BFD时：     - UEG上不需要配置BGP相关数据。     - 在直连三层设备上配置到UEG的逻辑接口IP&UE IP的路由，下一跳是UEG的外联口IP。   + 直连PE时，UEG支持通过OSPF动态路由与园区服务器实现网络互通。  **图1** UEG与gNodeB之间的组网示意（直连DCGW）  **图2** UEG与gNodeB之间的组网示意（直连PE）  **图3** UEG与企业园区之间的组网示意（直连DCGW/PE）
tags: []
risk_level: ''
doc_source: ["网络部署","园区入驻式（仅连接）","5GC toB 部署边缘站点（站点为“风筝L”，入驻式）","UEG初始配置（风筝L）","配置实例（裸机容器）","配置UPF/SGW-U/PGW-U","UPF配置实例"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
UEG部署在园区，作为企业专用UPF。N3使用SR-IOV bonding组网（Eth-trunk接口），直连DCGW时，一个Eth-trunk接口的成员端口连接到DCGW1和DCGW2；直连PE时，一个Eth-trunk接口的成员端口必须连接到同一个PE设备；UEG与LocalDN使用非SR-IOV bonding组网（以太网接口），物理接口分别与两个PE/两个DCGW连接。园区部署两套UEG实现容灾，两套UEG内各业务网元之间不交叉互连。UEG通过BGP over静态路由+BFD与对端网元实现网络互通。* 直连DCGW时，UEG与gNodeB之间的组网示意如图1所示。* 直连PE时，UEG与gNodeB之间的组网示意如图2所示。* 直连DCGW/PE时，UEG与企业园区服务器之间的组网示意如图3所示。* 直连DCGW时，推荐使用BGP over静态路由+BFD与对端实现网络互通。* 直连PE时，UEG支持：  + 通过BGP over静态路由+BFD与企业园区服务器之间实现网络互通。  + 通过静态路由+BFD与对端网元（gNodeB/园区服务器）实现网络互通。采用静态路由+BFD时：    - UEG上不需要配置BGP相关数据。    - 在直连三层设备上配置到UEG的逻辑接口IP&UE IP的路由，下一跳是UEG的外联口IP。  + 直连PE时，UEG支持通过OSPF动态路由与园区服务器实现网络互通。**图1** UEG与gNodeB之间的组网示意（直连DCGW）**图2** UEG与gNodeB之间的组网示意（直连PE）**图3** UEG与企业园区之间的组网示意（直连DCGW/PE）

## 必备事项
前提条件

* 具备管理员权限的操作人员已经登录华为操作维护系统（登录MAE客户端或登录OM Portal）。
* VNF与网络实体之间的网络环境已经构建完成（连线要求请参见外联口介绍(刀片式服务器2U)）。
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
          data_source: ''
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
    add_l3vpninst_list:
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
          description: ''
          data_source: ''
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
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SUBNETMASK:
          name: 'IPv4地址掩码'
          type: string
          maxLength: 15
          required: true
          description: ''
          data_source: ''
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
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PREFIXLEN:
          name: 'IPv6地址前缀'
          type: integer
          minimum: 1
          maximum: 128
          required: true
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
          description: ''
          data_source: ''
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
          data_source: ''
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
          description: ''
          data_source: ''
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
          data_source: ''
          pattern: ''
          default: ipv4
        PEERADDR:
          name: 'IPv4对等体地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        REMOTEAS:
          name: '对等体AS号'
          type: string
          maxLength: 11
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LOCALIFADDR:
          name: '本地接口地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
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
          description: ''
          data_source: ''
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
          data_source: ''
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
          data_source: ''
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
    mod_interface_list:
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
    add_interface_list_1:
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
    mod_trunkif_list:
      type: items
      properties:
        IFNAME:
          name: '接口名称'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: ''
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
          data_source: ''
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
          data_source: ''
          pattern: ''
          default: ''
        MEMBERIFNAME:
          name: '成员接口名'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: ''
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
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    mod_trunkif_list_1:
      type: items
      properties:
        IFNAME:
          name: '接口名称'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: ''
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
          data_source: ''
          pattern: ''
          default: ''
    add_trunkmember_list_2:
      type: items
      properties:
        TRUNKIFNAME:
          name: 'Trunk接口名'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MEMBERIFNAME:
          name: '成员接口名'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: ''
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
          data_source: ''
          pattern: ''
          default: ''
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: true
          description: ''
          data_source: ''
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
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VLANTYPEVID:
          name: 'VLAN ID'
          type: integer
          minimum: 1
          maximum: 4094
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_ifipv6enable_list_1:
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
    add_ifipv4address_list_1:
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
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SUBNETMASK:
          name: 'IPv4地址掩码'
          type: string
          maxLength: 15
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_ifipv6address_list_1:
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
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PREFIXLEN:
          name: 'IPv6地址前缀'
          type: integer
          minimum: 1
          maximum: 128
          required: true
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
          data_source: ''
          pattern: ''
          default: ''
        IFIPADDR:
          name: 'IPv4地址'
          type: string
          maxLength: 15
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SUBNETMASK:
          name: 'IPv4地址掩码'
          type: string
          maxLength: 15
          required: true
          description: ''
          data_source: ''
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
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PREFIXLEN:
          name: 'IPv6地址前缀'
          type: integer
          minimum: 1
          maximum: 128
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_bfdsession_list:
      type: items
      properties:
        SESSNAME:
          name: '会话名称'
          type: string
          maxLength: 64
          required: true
          description: ''
          data_source: ''
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
          data_source: ''
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
          data_source: ''
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
          data_source: ''
          pattern: ''
          default: ''
        DESTADDR4:
          name: 'IPv4目的地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
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
          data_source: ''
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
          data_source: ''
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
          data_source: ''
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
          data_source: ''
          pattern: ''
          default: FALSE
        DESTADDR6:
          name: 'IPv6目的地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
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
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PREFIX:
          name: '路由前缀'
          type: string
          maxLength: 15
          required: true
          description: ''
          data_source: ''
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
          data_source: ''
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
          data_source: ''
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
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PREFIX:
          name: '路由前缀'
          type: string
          maxLength: 39
          required: true
          description: ''
          data_source: ''
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
          data_source: ''
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
          data_source: ''
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
    add_srroute_list_2:
      type: items
      properties:
        AFTYPE:
          name: '地址族'
          type: string
          enum:
          - ipv4unicast
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PREFIX:
          name: '路由前缀'
          type: string
          maxLength: 15
          required: true
          description: ''
          data_source: ''
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
          data_source: ''
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
          data_source: ''
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
    add_srroute_list_4:
      type: items
      properties:
        AFTYPE:
          name: '地址族'
          type: string
          enum:
          - ipv4unicast
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PREFIX:
          name: '路由前缀'
          type: string
          maxLength: 15
          required: true
          description: ''
          data_source: ''
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
          data_source: ''
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
          data_source: ''
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
    add_srroute6_list_2:
      type: items
      properties:
        AFTYPE:
          name: '地址族'
          type: string
          enum:
          - ipv6unicast
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PREFIX:
          name: '路由前缀'
          type: string
          maxLength: 39
          required: true
          description: ''
          data_source: ''
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
          data_source: ''
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
          data_source: ''
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
    add_srroute6_list_4:
      type: items
      properties:
        AFTYPE:
          name: '地址族'
          type: string
          enum:
          - ipv6unicast
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PREFIX:
          name: '路由前缀'
          type: string
          maxLength: 39
          required: true
          description: ''
          data_source: ''
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
          data_source: ''
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
          data_source: ''
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
    add_l3vpninst_list_1:
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
    add_vpninstaf_list_2:
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
    mod_interface_list_4:
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
    add_interface_list_5:
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
    mod_trunkif_list_2:
      type: items
      properties:
        IFNAME:
          name: '接口名称'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: ''
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
          data_source: ''
          pattern: ''
          default: ''
    add_trunkmember_list_4:
      type: items
      properties:
        TRUNKIFNAME:
          name: 'Trunk接口名'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MEMBERIFNAME:
          name: '成员接口名'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_interface_list_6:
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
    add_ipbindvpn_list_3:
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
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_ethsubif_list_2:
      type: items
      properties:
        IFNAME:
          name: '子接口名字'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VLANTYPEVID:
          name: 'VLAN ID'
          type: integer
          minimum: 1
          maximum: 4094
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_ifipv6enable_list_3:
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
    add_ifipv4address_list_3:
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
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SUBNETMASK:
          name: 'IPv4地址掩码'
          type: string
          maxLength: 15
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_ifipv6address_list_3:
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
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PREFIXLEN:
          name: 'IPv6地址前缀'
          type: integer
          minimum: 1
          maximum: 128
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_bfdsession_list_4:
      type: items
      properties:
        SESSNAME:
          name: '会话名称'
          type: string
          maxLength: 64
          required: true
          description: ''
          data_source: ''
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
          data_source: ''
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
          data_source: ''
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
          data_source: ''
          pattern: ''
          default: ''
        DESTADDR4:
          name: 'IPv4目的地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
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
          data_source: ''
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
          data_source: ''
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
          data_source: ''
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
          data_source: ''
          pattern: ''
          default: FALSE
        DESTADDR6:
          name: 'IPv6目的地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_bfdsession_list_6:
      type: items
      properties:
        SESSNAME:
          name: '会话名称'
          type: string
          maxLength: 64
          required: true
          description: ''
          data_source: ''
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
          data_source: ''
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
          data_source: ''
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
          data_source: ''
          pattern: ''
          default: ''
        DESTADDR4:
          name: 'IPv4目的地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
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
        MINTXINT:
          name: '最小发送间隔（ms）'
          type: integer
          minimum: 30
          maximum: 1000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 200
        MINRXINT:
          name: '最小接收间隔（ms）'
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
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
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
        REMOTEDISCR:
          name: '远端标识符'
          type: integer
          minimum: 1
          maximum: 4294967295
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
          data_source: ''
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
          data_source: ''
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
          data_source: ''
          pattern: ''
          default: FALSE
        DESTADDR6:
          name: 'IPv6目的地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_bfdsession_list_8:
      type: items
      properties:
        SESSNAME:
          name: '会话名称'
          type: string
          maxLength: 64
          required: true
          description: ''
          data_source: ''
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
          data_source: ''
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
          data_source: ''
          pattern: ''
          default: ''
        DESTADDR4:
          name: 'IPv4目的地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
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
        MINTXINT:
          name: '最小发送间隔（ms）'
          type: integer
          minimum: 30
          maximum: 1000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 200
        MINRXINT:
          name: '最小接收间隔（ms）'
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
        ADMINDOWN:
          name: '管理DOWN'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SRCADDR4:
          name: 'IPv4源地址'
          type: string
          maxLength: 15
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
          data_source: ''
          pattern: ''
          default: ''
        PROCESSPST:
          name: '是否操作PST'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        CREATETYPE6:
          name: 'IPv6会话创建方式'
          type: string
          enum:
          - SESS_AUTO
          - SESS_STATIC
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DESTADDR6:
          name: 'IPv6目的地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SRCADDR6:
          name: 'IPv6源地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
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
          data_source: ''
          pattern: ''
          default: FALSE
        ONEARMECHO:
          name: 'IPv4单臂Echo'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_srroute_list_6:
      type: items
      properties:
        AFTYPE:
          name: '地址族'
          type: string
          enum:
          - ipv4unicast
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PREFIX:
          name: '路由前缀'
          type: string
          maxLength: 15
          required: true
          description: ''
          data_source: ''
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
          data_source: ''
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
          data_source: ''
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
    add_srroute6_list_6:
      type: items
      properties:
        AFTYPE:
          name: '地址族'
          type: string
          enum:
          - ipv6unicast
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PREFIX:
          name: '路由前缀'
          type: string
          maxLength: 39
          required: true
          description: ''
          data_source: ''
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
          data_source: ''
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
          data_source: ''
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
    add_l3vpninst_list_2:
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
    add_vpninstaf_list_4:
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
    add_interface_list_7:
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
    add_ipbindvpn_list_4:
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
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_ifipv4address_list_4:
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
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SUBNETMASK:
          name: 'IPv4地址掩码'
          type: string
          maxLength: 15
          required: true
          description: ''
          data_source: ''
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
    set_ifipv6enable_list_4:
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
    add_ifipv6address_list_4:
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
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PREFIXLEN:
          name: 'IPv6地址前缀'
          type: integer
          minimum: 1
          maximum: 128
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_bgpvrf_list_1:
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
          data_source: ''
          pattern: ''
          default: ''
    add_bgpvrfaf_list_2:
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
    add_bgppeer_list_4:
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
        ADDRESSTYPE:
          name: '地址类型'
          type: string
          enum:
          - ipv4
          - ipv6
          - noaf
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ipv4
        PEERADDR:
          name: 'IPv4对等体地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        REMOTEAS:
          name: '对等体AS号'
          type: string
          maxLength: 11
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LOCALIFADDR:
          name: '本地接口地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
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
          data_source: ''
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
          description: ''
          data_source: ''
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
          data_source: ''
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
          data_source: ''
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
    mod_interface_list_6:
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
    add_interface_list_8:
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
    add_ipbindvpn_list_5:
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
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_ethsubif_list_3:
      type: items
      properties:
        IFNAME:
          name: '子接口名字'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VLANTYPEVID:
          name: 'VLAN ID'
          type: integer
          minimum: 1
          maximum: 4094
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_ifipv6enable_list_5:
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
    add_ifipv4address_list_5:
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
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SUBNETMASK:
          name: 'IPv4地址掩码'
          type: string
          maxLength: 15
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_ifipv6address_list_5:
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
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PREFIXLEN:
          name: 'IPv6地址前缀'
          type: integer
          minimum: 1
          maximum: 128
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_bfdsession_list_10:
      type: items
      properties:
        SESSNAME:
          name: '会话名称'
          type: string
          maxLength: 64
          required: true
          description: ''
          data_source: ''
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
          data_source: ''
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
          data_source: ''
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
          data_source: ''
          pattern: ''
          default: ''
        DESTADDR4:
          name: 'IPv4目的地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
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
          data_source: ''
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
          data_source: ''
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
          data_source: ''
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
          data_source: ''
          pattern: ''
          default: FALSE
        DESTADDR6:
          name: 'IPv6目的地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_bfdsession_list_14:
      type: items
      properties:
        SESSNAME:
          name: '会话名称'
          type: string
          maxLength: 64
          required: true
          description: ''
          data_source: ''
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
          data_source: ''
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
          data_source: ''
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
          data_source: ''
          pattern: ''
          default: ''
        DESTADDR4:
          name: 'IPv4目的地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
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
        MINTXINT:
          name: '最小发送间隔（ms）'
          type: integer
          minimum: 30
          maximum: 1000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 200
        MINRXINT:
          name: '最小接收间隔（ms）'
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
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
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
        REMOTEDISCR:
          name: '远端标识符'
          type: integer
          minimum: 1
          maximum: 4294967295
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
          data_source: ''
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
          data_source: ''
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
          data_source: ''
          pattern: ''
          default: FALSE
        DESTADDR6:
          name: 'IPv6目的地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_bfdsession_list_18:
      type: items
      properties:
        SESSNAME:
          name: '会话名称'
          type: string
          maxLength: 64
          required: true
          description: ''
          data_source: ''
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
          data_source: ''
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
          data_source: ''
          pattern: ''
          default: ''
        DESTADDR4:
          name: 'IPv4目的地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
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
        MINTXINT:
          name: '最小发送间隔（ms）'
          type: integer
          minimum: 30
          maximum: 1000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 200
        MINRXINT:
          name: '最小接收间隔（ms）'
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
        ADMINDOWN:
          name: '管理DOWN'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SRCADDR4:
          name: 'IPv4源地址'
          type: string
          maxLength: 15
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
          data_source: ''
          pattern: ''
          default: ''
        PROCESSPST:
          name: '是否操作PST'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        CREATETYPE6:
          name: 'IPv6会话创建方式'
          type: string
          enum:
          - SESS_AUTO
          - SESS_STATIC
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DESTADDR6:
          name: 'IPv6目的地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SRCADDR6:
          name: 'IPv6源地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
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
          data_source: ''
          pattern: ''
          default: FALSE
        ONEARMECHO:
          name: 'IPv4单臂Echo'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_srroute_list_7:
      type: items
      properties:
        AFTYPE:
          name: '地址族'
          type: string
          enum:
          - ipv4unicast
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PREFIX:
          name: '路由前缀'
          type: string
          maxLength: 15
          required: true
          description: ''
          data_source: ''
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
          data_source: ''
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
          data_source: ''
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
    add_srroute6_list_7:
      type: items
      properties:
        AFTYPE:
          name: '地址族'
          type: string
          enum:
          - ipv6unicast
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PREFIX:
          name: '路由前缀'
          type: string
          maxLength: 39
          required: true
          description: ''
          data_source: ''
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
          data_source: ''
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
          data_source: ''
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
    add_srroute_list_9:
      type: items
      properties:
        AFTYPE:
          name: '地址族'
          type: string
          enum:
          - ipv4unicast
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PREFIX:
          name: '路由前缀'
          type: string
          maxLength: 15
          required: true
          description: ''
          data_source: ''
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
          data_source: ''
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
          data_source: ''
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
    add_srroute_list_11:
      type: items
      properties:
        AFTYPE:
          name: '地址族'
          type: string
          enum:
          - ipv4unicast
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PREFIX:
          name: '路由前缀'
          type: string
          maxLength: 15
          required: true
          description: ''
          data_source: ''
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
          data_source: ''
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
          data_source: ''
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
    add_srroute6_list_9:
      type: items
      properties:
        AFTYPE:
          name: '地址族'
          type: string
          enum:
          - ipv6unicast
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PREFIX:
          name: '路由前缀'
          type: string
          maxLength: 39
          required: true
          description: ''
          data_source: ''
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
          data_source: ''
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
          data_source: ''
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
    add_srroute6_list_11:
      type: items
      properties:
        AFTYPE:
          name: '地址族'
          type: string
          enum:
          - ipv6unicast
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PREFIX:
          name: '路由前缀'
          type: string
          maxLength: 39
          required: true
          description: ''
          data_source: ''
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
          data_source: ''
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
          data_source: ''
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
    add_l3vpninst_list_3:
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
    add_vpninstaf_list_6:
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
    mod_interface_list_8:
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
    add_interface_list_10:
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
    add_ipbindvpn_list_7:
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
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_ethsubif_list_5:
      type: items
      properties:
        IFNAME:
          name: '子接口名字'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VLANTYPEVID:
          name: 'VLAN ID'
          type: integer
          minimum: 1
          maximum: 4094
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_ifipv6enable_list_7:
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
    add_ifipv4address_list_7:
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
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SUBNETMASK:
          name: 'IPv4地址掩码'
          type: string
          maxLength: 15
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_ifipv6address_list_7:
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
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PREFIXLEN:
          name: 'IPv6地址前缀'
          type: integer
          minimum: 1
          maximum: 128
          required: true
          description: ''
          data_source: ''
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
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VRFNAME:
          name: 'VPN名称'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: '_public_'
        SCHEMAROUID:
          name: '路由器标识'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
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
        VPNINSCAPSIMFLG:
          name: '去使能VPN路由环路检测'
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
          description: ''
          data_source: ''
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
          name: '区域标识'
          type: string
          maxLength: 15
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IFNAME:
          name: '接口名'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DRPRI:
          name: '指定路由器优先级'
          type: integer
          minimum: 0
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 1
        VIRTUALSYSFLAG:
          name: 'OSPF共网段虚拟系统使能标志'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        CFGROUTERIDFLAG:
          name: 'OSPF虚Router-id配置标志'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
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
    add_ospfv3_list:
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
        VRFNAME:
          name: 'VPN名称'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: '_public_'
        ROUTERID:
          name: '路由器标识'
          type: string
          maxLength: 15
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
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
        VPNINSCAPSIMFLG:
          name: '去使能VPN路由环路检测'
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
          name: 'OSPFv3区域标识'
          type: string
          maxLength: 15
          required: true
          description: ''
          data_source: ''
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
          name: 'OSPFv3区域号'
          type: string
          maxLength: 15
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IFNAME:
          name: '接口名称'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DRPRI:
          name: '指定路由器优先级'
          type: integer
          minimum: 0
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 1
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
        CFGROUTERIDFLAG:
          name: 'OSPFv3虚拟路由器标识使能标识'
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
          data_source: ''
          pattern: ''
          default: ''
    add_logicinf_list:
      type: items
      properties:
        NAME:
          name: '逻辑接口名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPVERSION:
          name: '逻辑接口的IP版本'
          type: string
          enum:
          - IPV4
          - IPV6
          - IPVER_ALL
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV4ADDRESS1:
          name: '逻辑接口的IPv4地址1'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV4MASK1:
          name: '逻辑接口的IPv4掩码1'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VPNINSTANCE:
          name: 'VPN实例名称'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6ADDRESS1:
          name: '逻辑接口的IPv6地址1'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6PREFIXLEN1:
          name: 'IPv6前缀长度1'
          type: integer
          minimum: 1
          maximum: 128
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_vpninst_list_1:
      type: items
      properties:
        VPNINSTANCE:
          name: 'VPN实例名'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_logicinf_list_1:
      type: items
      properties:
        NAME:
          name: '逻辑接口名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPVERSION:
          name: '逻辑接口的IP版本'
          type: string
          enum:
          - IPV4
          - IPV6
          - IPVER_ALL
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV4ADDRESS1:
          name: '逻辑接口的IPv4地址1'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV4MASK1:
          name: '逻辑接口的IPv4掩码1'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VPNINSTANCE:
          name: 'VPN实例名称'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6ADDRESS1:
          name: '逻辑接口的IPv6地址1'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6PREFIXLEN1:
          name: 'IPv6前缀长度1'
          type: integer
          minimum: 1
          maximum: 128
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_upinfo_list:
      type: items
      properties:
        HOSTNAME:
          name: 'HostName'
          type: string
          minLength: 0
          maxLength: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_vpninst_list_2:
      type: items
      properties:
        VPNINSTANCE:
          name: 'VPN实例名'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_upapn_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        HASVPN:
          name: '绑定VPN'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
        VPNINSTANCE:
          name: 'VPN实例名'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        HASVPNIPV6:
          name: '绑定IPv6 VPN'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
        VPNINSTANCEIPV6:
          name: 'IPv6 VPN实例名'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_apnsglpass_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SWITCH:
          name: '开关标识'
          type: string
          enum:
          - PF_ACT_DISABLE
          - PF_ACT_ENABLE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_apnaddressattr_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SUPPORTIPV4:
          name: '支持IPV4'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SUPPORTIPV6:
          name: '支持IPV6'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        FRAMEDROUTE:
          name: '手机后路由'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ANTISPOOFINGDL:
          name: '下行防欺诈'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ANTISPOOFINGUL:
          name: '上行防欺诈'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPTYPEFORDUALIP:
          name: '为双栈用户返回的地址类型'
          type: string
          enum:
          - IPV4
          - IPV4V6
          - IPV6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SINGLEADDRCAUSE:
          name: '分配单栈地址时返回的原因值'
          type: integer
          minimum: 1
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CPCTRL:
          name: '基于CP分配IP地址'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6RAMTUSW:
          name: 'RA携带MTU选项开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6RALIFETIME:
          name: 'IPv6 RA消息路由生命周期(秒)'
          type: integer
          minimum: 3600
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        HOSTROUTEIP:
          name: '主机地址'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_ipallocrule_list:
      type: items
      properties:
        FIRSTRULESW:
          name: 'IPv4第一级规则开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        FIRSTRULE:
          name: 'IPv4第一级规则'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SECONDRULESW:
          name: 'IPv4第二级规则开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        THIRDRULESW:
          name: 'IPv4第三级规则开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6FIRSTRULESW:
          name: 'IPv6第一级规则开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6FIRSTRULE:
          name: 'IPv6第一级规则'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6SECRULESW:
          name: 'IPv6第二级规则开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6THIRDRULESW:
          name: 'IPv6第三级规则开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_uppool_list:
      type: items
      properties:
        POOLNAME:
          name: '地址池名称'
          type: string
          minLength: 1
          maxLength: 79
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        POOLTYPE:
          name: '地址池类型'
          type: string
          enum:
          - EXTERNAL
          - LOCAL
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: LOCAL
        IPVERSION:
          name: 'IP地址类型'
          type: string
          enum:
          - IPV4
          - IPV6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: IPV4
        HASVPN:
          name: '绑定VPN'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
        VPNINSTANCE:
          name: 'VPN实例名'
          type: string
          minLength: 1
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_section_list:
      type: items
      properties:
        POOLNAME:
          name: '地址池名称'
          type: string
          minLength: 0
          maxLength: 79
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SECTIONNUM:
          name: '地址段号'
          type: integer
          minimum: 0
          maximum: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPVERSION:
          name: 'IP地址类型'
          type: string
          enum:
          - IPV4
          - IPV6
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        V4STARTIP:
          name: '地址段的起始IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        V4ENDIP:
          name: '地址段的终止IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        V6PREFIXSTART:
          name: 'IPv6前缀起始地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        V6PREFIXEND:
          name: 'IPv6前缀结束地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        V6PREFIXLENGTH:
          name: 'IPv6前缀长度'
          type: integer
          minimum: 49
          maximum: 64
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_poolgroup_list:
      type: items
      properties:
        POOLGRPNAME:
          name: '地址池组名称'
          type: string
          minLength: 0
          maxLength: 79
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV4ALLOCPRIALG:
          name: 'IPV4基于地址池优先级分配地址算法'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
        IPV6ALLOCPRIALG:
          name: 'IPV6基于地址池优先级分配地址算法'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
    add_poolbindgroup_list:
      type: items
      properties:
        POOLGROUPNAME:
          name: '地址池组名称'
          type: string
          minLength: 0
          maxLength: 79
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        POOLNAME:
          name: '地址池名称'
          type: string
          minLength: 0
          maxLength: 79
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PRIORITY:
          name: '地址池优先级'
          type: integer
          minimum: 1
          maximum: 16
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 16
    add_poolgrpmap_list:
      type: items
      properties:
        MAPPINGNAME:
          name: '映射规则名称'
          type: string
          minLength: 0
          maxLength: 79
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        APN:
          name: 'APN名称'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        POOLGROUPNAME:
          name: '地址池组名称'
          type: string
          minLength: 0
          maxLength: 79
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_ipallocrule_list_1:
      type: items
      properties:
        FIRSTRULESW:
          name: 'IPv4第一级规则开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        FIRSTRULE:
          name: 'IPv4第一级规则'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SECONDRULESW:
          name: 'IPv4第二级规则开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        THIRDRULESW:
          name: 'IPv4第三级规则开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6FIRSTRULESW:
          name: 'IPv6第一级规则开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6FIRSTRULE:
          name: 'IPv6第一级规则'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6SECRULESW:
          name: 'IPv6第二级规则开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6THIRDRULESW:
          name: 'IPv6第三级规则开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_uppool_list_2:
      type: items
      properties:
        POOLNAME:
          name: '地址池名称'
          type: string
          minLength: 1
          maxLength: 79
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        POOLTYPE:
          name: '地址池类型'
          type: string
          enum:
          - EXTERNAL
          - LOCAL
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: LOCAL
        IPVERSION:
          name: 'IP地址类型'
          type: string
          enum:
          - IPV4
          - IPV6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: IPV4
        CHECKIPVALID:
          name: '检查地址合法性'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
        HASVPN:
          name: '绑定VPN'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
        VPNINSTANCE:
          name: 'VPN实例名'
          type: string
          minLength: 1
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IMSSW:
          name: 'IMS开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ENABLE
        REDUNDFUNC:
          name: '冗余备份功能开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
    add_section_list_2:
      type: items
      properties:
        POOLNAME:
          name: '地址池名称'
          type: string
          minLength: 0
          maxLength: 79
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SECTIONNUM:
          name: '地址段号'
          type: integer
          minimum: 0
          maximum: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPVERSION:
          name: 'IP地址类型'
          type: string
          enum:
          - IPV4
          - IPV6
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        V4STARTIP:
          name: '地址段的起始IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        V4ENDIP:
          name: '地址段的终止IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        V6PREFIXSTART:
          name: 'IPv6前缀起始地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        V6PREFIXEND:
          name: 'IPv6前缀结束地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        V6PREFIXLENGTH:
          name: 'IPv6前缀长度'
          type: integer
          minimum: 49
          maximum: 64
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_poolgroup_list_1:
      type: items
      properties:
        POOLGRPNAME:
          name: '地址池组名称'
          type: string
          minLength: 0
          maxLength: 79
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV4ALLOCPRIALG:
          name: 'IPV4基于地址池优先级分配地址算法'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
        IPV6ALLOCPRIALG:
          name: 'IPV6基于地址池优先级分配地址算法'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
    add_poolbindgroup_list_2:
      type: items
      properties:
        POOLGROUPNAME:
          name: '地址池组名称'
          type: string
          minLength: 0
          maxLength: 79
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        POOLNAME:
          name: '地址池名称'
          type: string
          minLength: 0
          maxLength: 79
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PRIORITY:
          name: '地址池优先级'
          type: integer
          minimum: 1
          maximum: 16
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 16
    add_poolgrpmap_list_1:
      type: items
      properties:
        MAPPINGNAME:
          name: '映射规则名称'
          type: string
          minLength: 0
          maxLength: 79
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        APN:
          name: 'APN名称'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        POOLGROUPNAME:
          name: '地址池组名称'
          type: string
          minLength: 0
          maxLength: 79
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_licenseswitch_list:
      type: items
      properties:
        LICITEM:
          name: 'License项'
          type: string
          minLength: 0
          maxLength: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SWITCH:
          name: '开关'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_filter_list:
      type: items
      properties:
        FILTERNAME:
          name: '过滤器名字'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        L34PROTTYPE:
          name: '三四层IPv4协议输入类型'
          type: string
          enum:
          - NUMBER
          - STRING
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        L34PROTOCOL:
          name: '三四层协议类型'
          type: string
          enum:
          - ANY
          - GRE
          - ICMP
          - TCP
          - UDP
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ANY
    add_flowfilter_list:
      type: items
      properties:
        FLOWFILTERNAME:
          name: '流过滤器名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TETHERDETFLAG:
          name: 'Tethering检测标识'
          type: string
          enum:
          - DETECT_ONLY
          - FILTER
          - NONE
          - NOT_FILTER
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NONE
    add_fltbindflowf_list:
      type: items
      properties:
        FLOWFILTERNAME:
          name: '流过滤器名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        FILTERNAME:
          name: '过滤器名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_refreshsrv_list:
      type: items
      properties:
        REFRESHTYPE:
          name: '刷新类型'
          type: string
          enum:
          - ACL
          - ALL
          - USERPROFILE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_pccpolicygrp_list:
      type: items
      properties:
        PCCPOLICYGRPNM:
          name: 'PCC策略组名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        FUPSESSIONEXC:
          name: 'Session级FUP累计标识'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
        TOKENFUNCFLAG:
          name: 'Token检测功能标识'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
        SIGNALASSOCIATE:
          name: '信令关联计费标识'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ENABLE
        ADCMUTEFLAG:
          name: 'ADC静默通知标识'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ENABLE
        HTTP2DEGRADESW:
          name: 'HTTP2.0协议回落开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          - INHERIT
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: INHERIT
    add_rule_list:
      type: items
      properties:
        RULENAME:
          name: '规则名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        POLICYTYPE:
          name: '策略类型'
          type: string
          enum:
          - ADC
          - BWM
          - FIREWALL
          - HEADEN
          - IPREDIR
          - LBO
          - PCC
          - QOS
          - REMARK_FPI
          - SMARTREDIRECT
          - SRV_TRIGGER
          - TRAFFICCLASS
          - WEBPROXY
          - WORKER
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        FILTERINGMODE:
          name: '流过滤器或流过滤器组选择'
          type: string
          enum:
          - FLOWFILTER
          - FLOWFILTERGRP
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        FLOWFILTERNAME:
          name: '流过滤器名称'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        POLICYNAME:
          name: '策略名称'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_userprofile_list:
      type: items
      properties:
        USERPROFILENAME:
          name: '用户模板名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ALIASMARKFLAG:
          name: 'Alias Marking使能标记'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
        DDOSCHECK:
          name: '防DDOS攻击标记'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
        LOCRPTSWITCH:
          name: '实时位置上报开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          - INHERIT
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: INHERIT
    add_rulebinding_list:
      type: items
      properties:
        USERPROFILENAME:
          name: '用户模板名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RULENAME:
          name: '规则名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    set_bfd_list:
    - BFDENABLE: TRUE
    set_bgp_list:
    - BGPENABLE: TRUE
      ASNUM: '60001'
    add_l3vpninst_list:
    - VRFNAME: 'VRF_Access'
    add_vpninstaf_list:
    - VRFNAME: 'VRF_Access'
      AFTYPE: ipv4uni
      VRFRD: '192.168.225.135:100'
    add_interface_list:
    - IFNAME: 'LoopBack5'
    add_ipbindvpn_list:
    - IFNAME: 'LoopBack5'
      VRFNAME: 'VRF_Access'
    add_ifipv4address_list:
    - IFNAME: 'LoopBack5'
      IFIPADDR: '192.168.225.135'
      SUBNETMASK: '255.255.255.255'
      ADDRTYPE: main
    set_ifipv6enable_list:
    - IFNAME: 'Loopback5'
      ENABLEFLAG: TRUE
    add_ifipv6address_list:
    - IFNAME: 'Loopback5'
      IPV6ADDRESS: 'FC00::225:135'
      PREFIXLEN: 128
    add_bgpvrf_list:
    - VRFNAME: 'VRF_Access'
      DEFAULTAFTYPE: noaf
      ROUTERID: '192.168.225.135'
    add_bgpvrfaf_list:
    - VRFNAME: 'VRF_Access'
      AFTYPE: ipv4uni
      MAXIMUMLOADBALANCE: 2
    add_bgppeer_list:
    - VRFNAME: 'VRF_Access'
      ADDRESSTYPE: ipv4
      PEERADDR: '192.168.79.5'
      REMOTEAS: '60002'
      LOCALIFADDR: '192.168.225.135'
      LOCALIFNAME: 'Loopback5'
      EBGPMAXHOP: 10
      PEERADDRV6: 'FC00::79:5'
    add_importroute_list:
    - VRFNAME: 'VRF_Access'
      AFTYPE: ipv4uni
      IMPORTPROTOCOL: wlr
      MEDENABLE: FALSE
    mod_interface_list:
    - IFNAME: 'Ethernet64/0/4'
      IFADMINSTATUS: up
    add_interface_list_1:
    - IFNAME: 'Eth-trunk1'
    mod_trunkif_list:
    - IFNAME: 'Eth-Trunk1'
      WORKMODE: Manual
    add_trunkmember_list:
    - TRUNKIFNAME: 'Eth-trunk1'
      MEMBERIFNAME: 'Ethernet64/0/4'
    add_interface_list_2:
    - IFNAME: 'Eth-trunk1.1'
    mod_trunkif_list_1:
    - IFNAME: 'Eth-Trunk2'
      WORKMODE: Manual
    add_trunkmember_list_2:
    - TRUNKIFNAME: 'Eth-trunk2'
      MEMBERIFNAME: 'Ethernet64/0/12'
    add_interface_list_4:
    - IFNAME: 'Eth-trunk2.1'
    add_ipbindvpn_list_1:
    - IFNAME: 'Eth-trunk1.1'
      VRFNAME: 'VRF_Access'
    add_ethsubif_list:
    - IFNAME: 'Eth-trunk1.1'
      VLANTYPEVID: 2005
    set_ifipv6enable_list_1:
    - IFNAME: 'Eth-trunk1.1'
      ENABLEFLAG: TRUE
    add_ifipv4address_list_1:
    - IFNAME: 'Eth-trunk1.1'
      IFIPADDR: '192.168.85.2'
      SUBNETMASK: '255.255.255.248'
    add_ifipv6address_list_1:
    - IFNAME: 'Eth-trunk1.1'
      IPV6ADDRESS: 'FC00::85:2'
      PREFIXLEN: 125
    add_ifipv4address_list_2:
    - IFNAME: 'Eth-trunk2.1'
      IFIPADDR: '192.168.185.2'
      SUBNETMASK: '255.255.255.248'
    add_ifipv6address_list_2:
    - IFNAME: 'Eth-trunk2.1'
      IPV6ADDRESS: 'FC00::185:2'
      PREFIXLEN: 125
    add_bfdsession_list:
    - SESSNAME: 'BfdName851_v4'
      ADDRTYPE: IPv4
      CREATETYPE4: SESS_STATIC
      ONEARMECHO: TRUE
      DESTADDR4: '192.168.85.1'
      LINKTYPE: IP
      DETECTMULTI: 4
      VRFNAME: 'VRF_Access'
      MINECHORXINT: 500
      LOCALDISCR: 8541
      IFNAME: 'Eth-trunk1.1'
      CREATETYPE6: SESS_STATIC
      ONEARMECHO6: TRUE
      DESTADDR6: 'FC00::85:1'
    add_srroute_list:
    - AFTYPE: ipv4unicast
      PREFIX: 'x.x.x.x'
      MASKLENGTH: 32
      VRFNAME: 'VRF_Access'
      DESTVRFNAME: 'VRF_Access'
      IFNAME: 'Eth-trunk1.1'
      NEXTHOP: '192.168.85.1'
      SESSIONNAME: 'BfdName851_v4'
    - AFTYPE: ipv4unicast
      PREFIX: 'x.x.x.x'
      MASKLENGTH: 32
      VRFNAME: 'VRF_Access'
      DESTVRFNAME: 'VRF_Access'
      IFNAME: 'Eth-trunk2.1'
      NEXTHOP: '192.168.185.1'
      SESSIONNAME: 'BfdName1851_v4'
    add_srroute6_list:
    - AFTYPE: ipv6unicast
      PREFIX: 'FC00:x::x'
      MASKLENGTH: 128
      VRFNAME: 'VRF_Access'
      DESTVRFNAME: 'VRF_Access'
      IFNAME: 'Eth-trunk1.1'
      NEXTHOP: 'FC00::85:1'
      SESSIONNAME: 'BfdName851_v6'
    - AFTYPE: ipv6unicast
      PREFIX: 'FC00:x::x'
      MASKLENGTH: 128
      VRFNAME: 'VRF_Access'
      DESTVRFNAME: 'VRF_Access'
      IFNAME: 'Eth-trunk2.1'
      NEXTHOP: 'FC00::185:1'
      SESSIONNAME: 'BfdName1851_v6'
    add_srroute_list_2:
    - AFTYPE: ipv4unicast
      PREFIX: '192.168.79.5'
      MASKLENGTH: 32
      VRFNAME: 'VRF_Access'
      DESTVRFNAME: 'VRF_Access'
      IFNAME: 'Eth-trunk1.1'
      NEXTHOP: '192.168.85.1'
      SESSIONNAME: 'BfdName851_v4'
    add_srroute_list_4:
    - AFTYPE: ipv4unicast
      PREFIX: '0.0.0.0'
      MASKLENGTH: 0
      VRFNAME: 'VRF_Access'
      DESTVRFNAME: 'VRF_Access'
      IFNAME: 'Eth-trunk1.1'
      NEXTHOP: '192.168.85.1'
      SESSIONNAME: 'BfdName851_v4'
    add_srroute6_list_2:
    - AFTYPE: ipv6unicast
      PREFIX: 'FC00::79:5'
      MASKLENGTH: 128
      VRFNAME: 'VRF_Access'
      DESTVRFNAME: 'VRF_Access'
      IFNAME: 'Eth-trunk1.1'
      NEXTHOP: 'FC00::85:1'
      SESSIONNAME: 'BfdName851_v6'
    add_srroute6_list_4:
    - AFTYPE: ipv6unicast
      PREFIX: '0:0:0:0:0:0:0:0'
      MASKLENGTH: 0
      VRFNAME: 'VRF_Access'
      DESTVRFNAME: 'VRF_Access'
      IFNAME: 'Eth-trunk1.1'
      NEXTHOP: 'FC00::85:1'
      SESSIONNAME: 'BfdName851_v6'
    add_l3vpninst_list_1:
    - VRFNAME: 'VRF_Access'
    add_vpninstaf_list_2:
    - VRFNAME: 'VRF_Access'
      AFTYPE: ipv4uni
      VRFRD: '192.168.225.135:100'
    mod_interface_list_4:
    - IFNAME: 'Ethernet64/0/12'
      IFADMINSTATUS: up
    add_interface_list_5:
    - IFNAME: 'Eth-trunk2'
    mod_trunkif_list_2:
    - IFNAME: 'Eth-Trunk2'
      WORKMODE: Manual
    add_trunkmember_list_4:
    - TRUNKIFNAME: 'Eth-trunk2'
      MEMBERIFNAME: 'Ethernet64/0/12'
    add_interface_list_6:
    - IFNAME: 'Eth-trunk2.1'
    add_ipbindvpn_list_3:
    - IFNAME: 'Eth-trunk2.1'
      VRFNAME: 'VRF_Access'
    add_ethsubif_list_2:
    - IFNAME: 'Eth-trunk2.1'
      VLANTYPEVID: 2015
    set_ifipv6enable_list_3:
    - IFNAME: 'Eth-trunk2.1'
      ENABLEFLAG: TRUE
    add_ifipv4address_list_3:
    - IFNAME: 'Eth-trunk2.1'
      IFIPADDR: '192.168.185.2'
      SUBNETMASK: '255.255.255.248'
    add_ifipv6address_list_3:
    - IFNAME: 'Eth-trunk2.1'
      IPV6ADDRESS: 'FC00::185:2'
      PREFIXLEN: 125
    add_bfdsession_list_4:
    - SESSNAME: 'BfdName1851_v4'
      ADDRTYPE: IPv4
      CREATETYPE4: SESS_STATIC
      ONEARMECHO: TRUE
      DESTADDR4: '192.168.185.1'
      LINKTYPE: IP
      DETECTMULTI: 4
      VRFNAME: 'VRF_Access'
      MINECHORXINT: 500
      LOCALDISCR: 8543
      IFNAME: 'Eth-trunk2.1'
      CREATETYPE6: SESS_STATIC
      ONEARMECHO6: TRUE
      DESTADDR6: 'FC00::185:1'
    add_bfdsession_list_6:
    - SESSNAME: 'BfdName1851_v4'
      ADDRTYPE: IPv4
      CREATETYPE4: SESS_STATIC
      ONEARMECHO: FALSE
      DESTADDR4: '192.168.185.1'
      LINKTYPE: IP
      MINTXINT: 500
      MINRXINT: 500
      DETECTMULTI: 4
      VRFNAME: 'VRF_Access'
      LOCALDISCR: 8543
      REMOTEDISCR: 8544
      IFNAME: 'Eth-trunk2.1'
      CREATETYPE6: SESS_STATIC
      ONEARMECHO6: FALSE
      DESTADDR6: 'FC00::185:1'
    add_bfdsession_list_8:
    - SESSNAME: 'BfdName1851_v4'
      ADDRTYPE: IPv4
      CREATETYPE4: SESS_AUTO
      DESTADDR4: '192.168.185.1'
      LINKTYPE: IP
      MINTXINT: 500
      MINRXINT: 500
      DETECTMULTI: 4
      ADMINDOWN: FALSE
      VRFNAME: 'VRF_Access'
      SRCADDR4: '192.168.185.2'
      IFNAME: 'Eth-trunk2.1'
      PROCESSPST: FALSE
      CREATETYPE6: SESS_AUTO
      DESTADDR6: 'FC00::185:1'
      SRCADDR6: 'FC00::185:2'
      ONEARMECHO6: FALSE
      ONEARMECHO: ''
    add_srroute_list_6:
    - AFTYPE: ipv4unicast
      PREFIX: 'x.x.x.x'
      MASKLENGTH: 32
      VRFNAME: 'VRF_Access'
      DESTVRFNAME: 'VRF_Access'
      IFNAME: 'Eth-trunk2.1'
      NEXTHOP: '192.168.185.1'
      SESSIONNAME: 'BfdName1851_v4'
    add_srroute6_list_6:
    - AFTYPE: ipv6unicast
      PREFIX: 'FC00:x::x'
      MASKLENGTH: 128
      VRFNAME: 'VRF_Access'
      DESTVRFNAME: 'VRF_Access'
      IFNAME: 'Eth-trunk2.1'
      NEXTHOP: 'FC00::185:1'
      SESSIONNAME: 'BfdName1851_v6'
    add_l3vpninst_list_2:
    - VRFNAME: 'VRF_LocalDN1'
    add_vpninstaf_list_4:
    - VRFNAME: 'VRF_LocalDN1'
      AFTYPE: ipv4uni
      VRFRD: '192.168.225.138:100'
    add_interface_list_7:
    - IFNAME: 'LoopBack8'
    add_ipbindvpn_list_4:
    - IFNAME: 'LoopBack8'
      VRFNAME: 'VRF_LocalDN1'
    add_ifipv4address_list_4:
    - IFNAME: 'LoopBack8'
      IFIPADDR: '192.168.225.138'
      SUBNETMASK: '255.255.255.255'
      ADDRTYPE: main
    set_ifipv6enable_list_4:
    - IFNAME: 'Loopback8'
      ENABLEFLAG: TRUE
    add_ifipv6address_list_4:
    - IFNAME: 'Loopback8'
      IPV6ADDRESS: 'FC00::225:138'
      PREFIXLEN: 128
    add_bgpvrf_list_1:
    - VRFNAME: 'VRF_LocalDN1'
      DEFAULTAFTYPE: noaf
      ROUTERID: '192.168.225.138'
    add_bgpvrfaf_list_2:
    - VRFNAME: 'VRF_LocalDN1'
      AFTYPE: ipv4uni
      MAXIMUMLOADBALANCE: 2
    add_bgppeer_list_4:
    - VRFNAME: 'VRF_LocalDN1'
      ADDRESSTYPE: ipv4
      PEERADDR: '192.168.79.8'
      REMOTEAS: '60002'
      LOCALIFADDR: '192.168.225.138'
      LOCALIFNAME: 'Loopback8'
      EBGPMAXHOP: 10
      PEERADDRV6: 'FC00::79:8'
    add_importroute_list_2:
    - VRFNAME: 'VRF_LocalDN1'
      AFTYPE: ipv4uni
      IMPORTPROTOCOL: wlr
      MEDENABLE: FALSE
    mod_interface_list_6:
    - IFNAME: 'Ethernet64/0/6'
      IFADMINSTATUS: up
    add_interface_list_8:
    - IFNAME: 'Ethernet64/0/6.1'
    add_ipbindvpn_list_5:
    - IFNAME: 'Ethernet64/0/6.1'
      VRFNAME: 'VRF_LocalDN1'
    add_ethsubif_list_3:
    - IFNAME: 'Ethernet64/0/6.1'
      VLANTYPEVID: 2008
    set_ifipv6enable_list_5:
    - IFNAME: 'Ethernet64/0/6.1'
      ENABLEFLAG: TRUE
    add_ifipv4address_list_5:
    - IFNAME: 'Ethernet64/0/6.1'
      IFIPADDR: '192.168.88.2'
      SUBNETMASK: '255.255.255.248'
    add_ifipv6address_list_5:
    - IFNAME: 'Ethernet64/0/6.1'
      IPV6ADDRESS: 'FC00::88:2'
      PREFIXLEN: 125
    add_bfdsession_list_10:
    - SESSNAME: 'BfdName881_v4'
      ADDRTYPE: IPv4
      CREATETYPE4: SESS_STATIC
      ONEARMECHO: TRUE
      DESTADDR4: '192.168.88.1'
      LINKTYPE: IP
      DETECTMULTI: 4
      VRFNAME: 'VRF_LocalDN1'
      MINECHORXINT: 500
      LOCALDISCR: 8841
      IFNAME: 'Ethernet64/0/6.1'
      CREATETYPE6: SESS_STATIC
      ONEARMECHO6: TRUE
      DESTADDR6: 'FC00::88:1'
    add_bfdsession_list_14:
    - SESSNAME: 'BfdName881_v4'
      ADDRTYPE: IPv4
      CREATETYPE4: SESS_STATIC
      ONEARMECHO: FALSE
      DESTADDR4: '192.168.88.1'
      LINKTYPE: IP
      MINTXINT: 500
      MINRXINT: 500
      DETECTMULTI: 4
      VRFNAME: 'VRF_LocalDN1'
      LOCALDISCR: 8841
      REMOTEDISCR: 8842
      IFNAME: 'Ethernet64/0/6.1'
      CREATETYPE6: SESS_STATIC
      ONEARMECHO6: FALSE
      DESTADDR6: 'FC00::88:1'
    add_bfdsession_list_18:
    - SESSNAME: 'BfdName881_v4'
      ADDRTYPE: IPv4
      CREATETYPE4: SESS_AUTO
      DESTADDR4: '192.168.88.1'
      LINKTYPE: IP
      MINTXINT: 500
      MINRXINT: 500
      DETECTMULTI: 4
      ADMINDOWN: FALSE
      VRFNAME: 'VRF_LocalDN1'
      SRCADDR4: '192.168.88.2'
      IFNAME: 'Ethernet64/0/6.1'
      PROCESSPST: FALSE
      CREATETYPE6: SESS_AUTO
      DESTADDR6: 'FC00::88:2'
      SRCADDR6: 'FC00::88:1'
      ONEARMECHO6: FALSE
      ONEARMECHO: ''
    add_srroute_list_7:
    - AFTYPE: ipv4unicast
      PREFIX: 'x.x.x.x'
      MASKLENGTH: 32
      VRFNAME: 'VRF_LocalDN1'
      DESTVRFNAME: 'VRF_LocalDN1'
      IFNAME: 'Ethernet64/0/6.1'
      NEXTHOP: '192.168.88.1'
      SESSIONNAME: 'BfdName881_v4'
    add_srroute6_list_7:
    - AFTYPE: ipv6unicast
      PREFIX: 'FC00:x::x'
      MASKLENGTH: 128
      VRFNAME: 'VRF_LocalDN1'
      DESTVRFNAME: 'VRF_LocalDN1'
      IFNAME: 'Ethernet64/0/6.1'
      NEXTHOP: 'FC00::88:1'
      SESSIONNAME: 'BfdName881_v6'
    add_srroute_list_9:
    - AFTYPE: ipv4unicast
      PREFIX: '192.168.79.8'
      MASKLENGTH: 32
      VRFNAME: 'VRF_LocalDN1'
      DESTVRFNAME: 'VRF_LocalDN1'
      IFNAME: 'Ethernet64/0/6.1'
      NEXTHOP: '192.168.88.1'
      SESSIONNAME: 'BfdName881_v4'
    add_srroute_list_11:
    - AFTYPE: ipv4unicast
      PREFIX: '0.0.0.0'
      MASKLENGTH: 0
      VRFNAME: 'VRF_LocalDN1'
      DESTVRFNAME: 'VRF_LocalDN1'
      IFNAME: 'Ethernet64/0/6.1'
      NEXTHOP: '192.168.88.1'
      SESSIONNAME: 'BfdName881_v4'
    add_srroute6_list_9:
    - AFTYPE: ipv6unicast
      PREFIX: 'FC00::79:8'
      MASKLENGTH: 128
      VRFNAME: 'VRF_LocalDN1'
      DESTVRFNAME: 'VRF_LocalDN1'
      IFNAME: 'Ethernet64/0/6.1'
      NEXTHOP: 'FC00::88:1'
      SESSIONNAME: 'BfdName881_v6'
    add_srroute6_list_11:
    - AFTYPE: ipv6unicast
      PREFIX: '0:0:0:0:0:0:0:0'
      MASKLENGTH: 0
      VRFNAME: 'VRF_LocalDN1'
      DESTVRFNAME: 'VRF_LocalDN1'
      IFNAME: 'Ethernet64/0/6.1'
      NEXTHOP: 'FC00::88:1'
      SESSIONNAME: 'BfdName881_v6'
    add_l3vpninst_list_3:
    - VRFNAME: 'VRF_LocalDN1'
    add_vpninstaf_list_6:
    - VRFNAME: 'VRF_LocalDN1'
      AFTYPE: ipv4uni
      VRFRD: '192.168.225.138:100'
    mod_interface_list_8:
    - IFNAME: 'Ethernet64/0/6'
      IFADMINSTATUS: up
    add_interface_list_10:
    - IFNAME: 'Ethernet64/0/6.1'
    add_ipbindvpn_list_7:
    - IFNAME: 'Ethernet64/0/6.1'
      VRFNAME: 'VRF_LocalDN1'
    add_ethsubif_list_5:
    - IFNAME: 'Ethernet64/0/6.1'
      VLANTYPEVID: 2008
    set_ifipv6enable_list_7:
    - IFNAME: 'Ethernet64/0/6.1'
      ENABLEFLAG: TRUE
    add_ifipv4address_list_7:
    - IFNAME: 'Ethernet64/0/6.1'
      IFIPADDR: '192.168.88.2'
      SUBNETMASK: '255.255.255.248'
    add_ifipv6address_list_7:
    - IFNAME: 'Ethernet64/0/6.1'
      IPV6ADDRESS: 'FC00::88:2'
      PREFIXLEN: 125
    add_ospf_list:
    - PROCID: 6
      VRFNAME: 'VPN_LocalDN'
      SCHEMAROUID: '192.168.35.210'
      BFDALLINTFFLG: FALSE
      LSAARRINTVFLAG: FALSE
      LSAARRMAXINTV: 1000
      LSAARRSTARINTV: 500
      LSAARRHLDINTV: 500
      VPNINSCAPSIMFLG: TRUE
      VIRTUALSYSFLAG: TRUE
    add_ospfarea_list:
    - PROCID: 6
      AREAID: '0.0.0.5'
      AREATYPE: Normal
      MAXCOSTFLAG: FALSE
    add_ospfinterface_list:
    - PROCID: 6
      AREAID: '0.0.0.5'
      IFNAME: 'Ethernet64/0/6.1'
      DRPRI: 0
      VIRTUALSYSFLAG: TRUE
      CFGROUTERIDFLAG: FALSE
      MAXCOSTFLAG: FALSE
    add_ospfimportroute_list:
    - PROCID: 6
      TOPOID: 0
      PROTOCOL: wlr
      IMPTCOSTCFG: FALSE
      IMPTTAGCFG: FALSE
      IMPTTYPECFG: FALSE
    add_ospfv3_list:
    - PROCID: 6
      VRFNAME: 'VPN_LocalDN'
      ROUTERID: '192.168.35.210'
      BFDALLINTFFLG: FALSE
      VPNINSCAPSIMFLG: TRUE
      VIRTUALSYSFLAG: TRUE
    add_ospfv3area_list:
    - PROCID: 6
      AREAID: '0.0.0.5'
      AREATYPE: Normal
    add_ospfv3interface_list:
    - PROCID: 6
      AREAID: '0.0.0.5'
      IFNAME: 'Ethernet64/0/6.1'
      DRPRI: 0
      VIRTUALSYSFLAG: TRUE
      CFGROUTERIDFLAG: FALSE
    add_ospfv3importroute_list:
    - PROCID: 6
      TOPOID: 0
      PROTOCOL: wlr
      IMPTCOSTCFG: FALSE
      IMPTTAGCFG: FALSE
      IMPTTYPECFG: FALSE
    add_vpninst_list:
    - VPNINSTANCE: 'VRF_Access'
    add_logicinf_list:
    - NAME: 'Saif1/1/0'
      IPVERSION: IPVER_ALL
      IPV4ADDRESS1: '10.1.1.1'
      IPV4MASK1: '255.255.255.255'
      VPNINSTANCE: 'VRF_Access'
      IPV6ADDRESS1: 'FC00::1:1'
      IPV6PREFIXLEN1: 128
    add_vpninst_list_1:
    - VPNINSTANCE: 'VRF_CN'
    add_logicinf_list_1:
    - NAME: 'N4if1/0/0'
      IPVERSION: IPVER_ALL
      IPV4ADDRESS1: '10.1.4.1'
      IPV4MASK1: '255.255.255.255'
      VPNINSTANCE: 'VRF_CN'
      IPV6ADDRESS1: 'FC00::4:1'
      IPV6PREFIXLEN1: 128
    set_upinfo_list:
    - HOSTNAME: 'UP_001'
    add_vpninst_list_2:
    - VPNINSTANCE: 'VRF_LocalDN1'
    add_upapn_list:
    - APN: 'apn-op1'
      HASVPN: ENABLE
      VPNINSTANCE: 'VRF_LocalDN1'
      HASVPNIPV6: ENABLE
      VPNINSTANCEIPV6: 'VRF_LocalDN1'
    set_apnsglpass_list:
    - APN: 'apn-op1'
      SWITCH: PF_ACT_ENABLE
    set_apnaddressattr_list:
    - APN: 'apn-op1'
      SUPPORTIPV4: ENABLE
      SUPPORTIPV6: ENABLE
      FRAMEDROUTE: DISABLE
      ANTISPOOFINGDL: ENABLE
      ANTISPOOFINGUL: ENABLE
      IPTYPEFORDUALIP: IPV4V6
      SINGLEADDRCAUSE: 1
      CPCTRL: DISABLE
      IPV6RAMTUSW: DISABLE
      IPV6RALIFETIME: 65535
      HOSTROUTEIP: ENABLE
    set_ipallocrule_list:
    - FIRSTRULESW: ENABLE
      FIRSTRULE: APN-1&LOCATION-0&SMF-0
      SECONDRULESW: DISABLE
      THIRDRULESW: DISABLE
      IPV6FIRSTRULESW: ENABLE
      IPV6FIRSTRULE: APN-1&LOCATION-0&SMF-0
      IPV6SECRULESW: DISABLE
      IPV6THIRDRULESW: DISABLE
    add_uppool_list:
    - POOLNAME: 'testpool1'
      POOLTYPE: LOCAL
      IPVERSION: IPV4
      HASVPN: ENABLE
      VPNINSTANCE: 'VRF_LocalDN1'
    add_section_list:
    - POOLNAME: 'testpool1'
      SECTIONNUM: 1
      IPVERSION: IPV4
      V4STARTIP: '10.10.1.1'
      V4ENDIP: '10.10.1.254'
      V6PREFIXSTART: 'FC00:1::1:1'
      V6PREFIXEND: 'FC00:1::1:254'
      V6PREFIXLENGTH: 64
    add_poolgroup_list:
    - POOLGRPNAME: 'poolgroup1'
      IPV4ALLOCPRIALG: ENABLE
      IPV6ALLOCPRIALG: ENABLE
    add_poolbindgroup_list:
    - POOLGROUPNAME: 'poolgroup1'
      POOLNAME: 'testpool1'
      PRIORITY: 10
    add_poolgrpmap_list:
    - MAPPINGNAME: 'mapping1'
      APN: 'apn-op1'
      POOLGROUPNAME: 'poolgroup1'
    set_ipallocrule_list_1:
    - FIRSTRULESW: ENABLE
      FIRSTRULE: APN-1&LOCATION-0&SMF-0
      SECONDRULESW: DISABLE
      THIRDRULESW: DISABLE
      IPV6FIRSTRULESW: ENABLE
      IPV6FIRSTRULE: APN-1&LOCATION-0&SMF-0
      IPV6SECRULESW: DISABLE
      IPV6THIRDRULESW: DISABLE
    add_uppool_list_2:
    - POOLNAME: 'testpool3'
      POOLTYPE: EXTERNAL
      IPVERSION: IPV4
      CHECKIPVALID: ENABLE
      HASVPN: ENABLE
      VPNINSTANCE: 'VRF_LocalDN1'
      IMSSW: DISABLE
      REDUNDFUNC: ENABLE
    add_section_list_2:
    - POOLNAME: 'testpool3'
      SECTIONNUM: 1
      IPVERSION: IPV4
      V4STARTIP: '10.10.1.1'
      V4ENDIP: '10.10.1.254'
      V6PREFIXSTART: 'FC00:1::1:1'
      V6PREFIXEND: 'FC00:1::1:254'
      V6PREFIXLENGTH: 64
    add_poolgroup_list_1:
    - POOLGRPNAME: 'poolgroup3'
      IPV4ALLOCPRIALG: ENABLE
      IPV6ALLOCPRIALG: ENABLE
    add_poolbindgroup_list_2:
    - POOLGROUPNAME: 'poolgroup3'
      POOLNAME: 'testpool3'
      PRIORITY: 10
    add_poolgrpmap_list_1:
    - MAPPINGNAME: 'mapping3'
      APN: 'apn-op1'
      POOLGROUPNAME: 'poolgroup3'
    set_licenseswitch_list:
    - LICITEM: 'LKV3G5PCCB01'
      SWITCH: ENABLE
    add_filter_list:
    - FILTERNAME: 'test'
      L34PROTTYPE: STRING
      L34PROTOCOL: ANY
    add_flowfilter_list:
    - FLOWFILTERNAME: 'test'
      TETHERDETFLAG: NONE
    add_fltbindflowf_list:
    - FLOWFILTERNAME: 'test'
      FILTERNAME: 'test'
    set_refreshsrv_list:
    - REFRESHTYPE: ALL
    add_pccpolicygrp_list:
    - PCCPOLICYGRPNM: 'test'
      FUPSESSIONEXC: DISABLE
      TOKENFUNCFLAG: DISABLE
      SIGNALASSOCIATE: ENABLE
      ADCMUTEFLAG: ENABLE
      HTTP2DEGRADESW: INHERIT
    add_rule_list:
    - RULENAME: 'test'
      POLICYTYPE: PCC
      FILTERINGMODE: FLOWFILTER
      FLOWFILTERNAME: 'test'
      POLICYNAME: 'test'
    add_userprofile_list:
    - USERPROFILENAME: 'up_test'
      ALIASMARKFLAG: DISABLE
      DDOSCHECK: DISABLE
      LOCRPTSWITCH: INHERIT
    add_rulebinding_list:
    - USERPROFILENAME: 'up_test'
      RULENAME: 'test'
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 配置基础数据。

### 配置基础数据包括：修改网元浮动IP、修改公共参数等。详细配置与组网无关，具体请参见《参考：详细配置指导 > 配置基础数据》章节。

### 2 激活全局BFD。

```jinja2
{%- for item in set_bfd_list -%}
    SET BFD:
    {#- --- 必选参数 --- -#}
    BFDENABLE={{item.BFDENABLE}},
    ;
{%- endfor -%}
```

### 3 激活全局BGP。

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

### 4 直连DCGW时，配置UPF（UEG）到无线侧(R)AN（gNodeB）的IP路由数据。直连PE时，请跳过本步骤。

#### 4.1 配置VPN实例。

```jinja2
{%- if is_scenario_direct_to_dcgw -%}
    {%- for item in add_l3vpninst_list -%}
        ADD L3VPNINST:
        {#- --- 必选参数 --- -#}
        VRFNAME="{{item.VRFNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_direct_to_dcgw -%}
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
{%- endif -%}
```

#### 步骤4.b~步骤4.f是BGP相关数据，采用BGP over静态路由+BFD时需要配置。采用静态路由+BFD时不需要配置。

#### 4.2 配置Loopback接口IP。用于建立BGP邻居。

```jinja2
{%- if is_scenario_direct_to_dcgw and is_scenario_bgp_over_static_route -%}
    {%- for item in add_interface_list -%}
        ADD INTERFACE:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_direct_to_dcgw and is_scenario_bgp_over_static_route -%}
    {%- for item in add_ipbindvpn_list -%}
        ADD IPBINDVPN:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        VRFNAME="{{item.VRFNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_direct_to_dcgw and is_scenario_bgp_over_static_route -%}
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
{%- endif -%}
```

```jinja2
{%- if is_scenario_direct_to_dcgw and is_scenario_bgp_over_static_route -%}
    {%- for item in set_ifipv6enable_list -%}
        SET IFIPV6ENABLE:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        ENABLEFLAG={{item.ENABLEFLAG}},
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_direct_to_dcgw and is_scenario_bgp_over_static_route -%}
    {%- for item in add_ifipv6address_list -%}
        ADD IFIPV6ADDRESS:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        IPV6ADDRESS="{{item.IPV6ADDRESS}}",
        PREFIXLEN={{item.PREFIXLEN}},
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 4.3 配置BGP VPN实例。

```jinja2
{%- if is_scenario_direct_to_dcgw and is_scenario_bgp_over_static_route -%}
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
{%- endif -%}
```

#### 4.4 增加BGP VPN实例地址族。

##### 4.4.1 //UEG对接2个负荷分担的BGP PEER，“MAXIMUMLOADBALANCE”设置为“2”。

```jinja2
{%- if is_scenario_direct_to_dcgw and is_scenario_bgp_over_static_route -%}
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
{%- endif -%}
```

#### 4.5 配置BGP对等体。此处以对接IPv4v6双栈的BGP对等体为例。

##### 4.5.1 //直连DCGW/PE时，UEG对接2个负荷分担的BGP PEER。

```jinja2
{%- if is_scenario_direct_to_dcgw and is_scenario_bgp_over_static_route -%}
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
{%- endif -%}
```

#### 4.6 配置BGP引入wlr路由。

```jinja2
{%- if is_scenario_direct_to_dcgw and is_scenario_bgp_over_static_route -%}
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

#### 4.7 配置外联口IP地址。

##### 4.7.1 查询接口名，确认可使用的外联口的接口类型和接口编号。

##### 4.7.2 配置主接口的管理状态为up。将网设规划的接口的管理状态设置为up。

```jinja2
{%- if is_scenario_direct_to_dcgw -%}
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
{%- endif -%}
```

##### 4.7.3 添加Eth-trunk接口及Eth-trunk子接口。成员端口数量以网设规划的为准。

```jinja2
{%- if is_scenario_direct_to_dcgw -%}
    {%- for item in add_interface_list_1 -%}
        ADD INTERFACE:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_direct_to_dcgw -%}
    {%- for item in mod_trunkif_list -%}
        MOD TRUNKIF:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        WORKMODE={{item.WORKMODE}},
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_direct_to_dcgw -%}
    {%- for item in add_trunkmember_list -%}
        ADD TRUNKMEMBER:
        {#- --- 必选参数 --- -#}
        TRUNKIFNAME="{{item.TRUNKIFNAME}}",
        MEMBERIFNAME="{{item.MEMBERIFNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_direct_to_dcgw -%}
    {%- for item in add_interface_list_2 -%}
        ADD INTERFACE:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_direct_to_dcgw -%}
    {%- for item in mod_trunkif_list_1 -%}
        MOD TRUNKIF:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        WORKMODE={{item.WORKMODE}},
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_direct_to_dcgw -%}
    {%- for item in add_trunkmember_list_2 -%}
        ADD TRUNKMEMBER:
        {#- --- 必选参数 --- -#}
        TRUNKIFNAME="{{item.TRUNKIFNAME}}",
        MEMBERIFNAME="{{item.MEMBERIFNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_direct_to_dcgw -%}
    {%- for item in add_interface_list_4 -%}
        ADD INTERFACE:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 4.7.4 增加接口绑定VPN。

```jinja2
{%- if is_scenario_direct_to_dcgw -%}
    {%- for item in add_ipbindvpn_list_1 -%}
        ADD IPBINDVPN:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        VRFNAME="{{item.VRFNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 4.7.5 在以太网子接口上关联VLAN ID。

```jinja2
{%- if is_scenario_direct_to_dcgw -%}
    {%- for item in add_ethsubif_list -%}
        ADD ETHSUBIF:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        VLANTYPEVID={{item.VLANTYPEVID}},
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 4.7.6 配置IPv6使能。

```jinja2
{%- if is_scenario_direct_to_dcgw -%}
    {%- for item in set_ifipv6enable_list_1 -%}
        SET IFIPV6ENABLE:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        ENABLEFLAG={{item.ENABLEFLAG}},
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 4.7.7 配置外联口IP地址。

```jinja2
{%- if is_scenario_direct_to_dcgw -%}
    {%- for item in add_ifipv4address_list_1 -%}
        ADD IFIPV4ADDRESS:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        IFIPADDR="{{item.IFIPADDR}}",
        SUBNETMASK="{{item.SUBNETMASK}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_direct_to_dcgw -%}
    {%- for item in add_ifipv6address_list_1 -%}
        ADD IFIPV6ADDRESS:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        IPV6ADDRESS="{{item.IPV6ADDRESS}}",
        PREFIXLEN={{item.PREFIXLEN}},
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_direct_to_dcgw -%}
    {%- for item in add_ifipv4address_list_2 -%}
        ADD IFIPV4ADDRESS:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        IFIPADDR="{{item.IFIPADDR}}",
        SUBNETMASK="{{item.SUBNETMASK}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_direct_to_dcgw -%}
    {%- for item in add_ifipv6address_list_2 -%}
        ADD IFIPV6ADDRESS:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        IPV6ADDRESS="{{item.IPV6ADDRESS}}",
        PREFIXLEN={{item.PREFIXLEN}},
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 4.8 新建BFD会话。

##### 4.8.1 //配置BFD单臂echo探测。

```jinja2
{%- if is_scenario_direct_to_dcgw -%}
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
{%- endif -%}
```

#### 4.9 采用静态路由+BFD时，配置静态路由并绑定BFD会话。采用BGP over静态路由+BFD时，请跳过该步骤。

##### 4.9.1 //“PREFIX”/“MASKLENGTH”是基站的IP地址及所在网段掩码长度，请根据网设文档替换。

```jinja2
{%- if is_scenario_direct_to_dcgw and is_scenario_static_route_bfd -%}
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
{%- endif -%}
```

```jinja2
{%- if is_scenario_direct_to_dcgw and is_scenario_static_route_bfd -%}
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
{%- endif -%}
```

#### 4.10 采用BGP over静态路由+BFD时，配置静态路由并绑定BFD会话。采用静态路由+BFD时，请跳过该步骤。

##### 4.10.1 //“PREFIX”和“MASKLENGTH”是目的IP和掩码（BGP对等体的IP地址和掩码）。

```jinja2
{%- if is_scenario_direct_to_dcgw and is_scenario_bgp_over_static_route -%}
    {%- for item in add_srroute_list_2 -%}
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
{%- endif -%}
```

##### 4.10.2 //对端网元不发布BGP默认路由时，需要配置该步骤。“PREFIX”设置为“0.0.0.0”，“MASKLENGTH”设置为“0”。其他参数与到BGP对等体的路由相同。

```jinja2
{%- if is_scenario_direct_to_dcgw and is_scenario_bgp_over_static_route and is_scenario_peer_no_default_route -%}
    {%- for item in add_srroute_list_4 -%}
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
{%- endif -%}
```

##### 4.10.3 //“PREFIX”和“MASKLENGTH”是目的IP和掩码（BGP对等体的IP地址和掩码）。

```jinja2
{%- if is_scenario_direct_to_dcgw and is_scenario_bgp_over_static_route -%}
    {%- for item in add_srroute6_list_2 -%}
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
{%- endif -%}
```

##### 4.10.4 //对端网元不发布BGP默认路由时，需要配置该步骤。“PREFIX”设置为“0:0:0:0:0:0:0:0”，“MASKLENGTH”设置为“0”。其他参数与到BGP对等体的路由相同。

```jinja2
{%- if is_scenario_direct_to_dcgw and is_scenario_bgp_over_static_route and is_scenario_peer_no_default_route -%}
    {%- for item in add_srroute6_list_4 -%}
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
{%- endif -%}
```

### 5 直连PE时，配置UPF（UEG）到无线侧(R)AN（gNodeB）的IP路由数据。直连DCGW时，请跳过本步骤。

#### 5.1 配置VPN实例。

```jinja2
{%- if is_scenario_direct_to_pe -%}
    {%- for item in add_l3vpninst_list_1 -%}
        ADD L3VPNINST:
        {#- --- 必选参数 --- -#}
        VRFNAME="{{item.VRFNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_direct_to_pe -%}
    {%- for item in add_vpninstaf_list_2 -%}
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
{%- endif -%}
```

#### 5.2 配置外联口IP地址。

##### 5.2.1 查询接口名，确认可使用的外联口的接口类型和接口编号。

##### 5.2.2 配置主接口的管理状态为up。将网设规划的接口的管理状态设置为up。

```jinja2
{%- if is_scenario_direct_to_pe -%}
    {%- for item in mod_interface_list_4 -%}
        MOD INTERFACE:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        {#- --- 可选参数 --- -#}
        {%- if item.IFADMINSTATUS is not none -%}
            IFADMINSTATUS={{item.IFADMINSTATUS}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 5.2.3 添加Eth-trunk接口及Eth-trunk子接口。成员端口数量以网设规划的为准。

```jinja2
{%- if is_scenario_direct_to_pe -%}
    {%- for item in add_interface_list_5 -%}
        ADD INTERFACE:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_direct_to_pe -%}
    {%- for item in mod_trunkif_list_2 -%}
        MOD TRUNKIF:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        WORKMODE={{item.WORKMODE}},
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_direct_to_pe -%}
    {%- for item in add_trunkmember_list_4 -%}
        ADD TRUNKMEMBER:
        {#- --- 必选参数 --- -#}
        TRUNKIFNAME="{{item.TRUNKIFNAME}}",
        MEMBERIFNAME="{{item.MEMBERIFNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_direct_to_pe -%}
    {%- for item in add_interface_list_6 -%}
        ADD INTERFACE:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 5.2.4 增加接口绑定VPN。

```jinja2
{%- if is_scenario_direct_to_pe -%}
    {%- for item in add_ipbindvpn_list_3 -%}
        ADD IPBINDVPN:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        VRFNAME="{{item.VRFNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 5.2.5 在以太网子接口上关联VLAN ID。

```jinja2
{%- if is_scenario_direct_to_pe -%}
    {%- for item in add_ethsubif_list_2 -%}
        ADD ETHSUBIF:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        VLANTYPEVID={{item.VLANTYPEVID}},
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 5.2.6 配置IPv6使能。

```jinja2
{%- if is_scenario_direct_to_pe -%}
    {%- for item in set_ifipv6enable_list_3 -%}
        SET IFIPV6ENABLE:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        ENABLEFLAG={{item.ENABLEFLAG}},
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 5.2.7 配置外联口IP地址。

```jinja2
{%- if is_scenario_direct_to_pe -%}
    {%- for item in add_ifipv4address_list_3 -%}
        ADD IFIPV4ADDRESS:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        IFIPADDR="{{item.IFIPADDR}}",
        SUBNETMASK="{{item.SUBNETMASK}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_direct_to_pe -%}
    {%- for item in add_ifipv6address_list_3 -%}
        ADD IFIPV6ADDRESS:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        IPV6ADDRESS="{{item.IPV6ADDRESS}}",
        PREFIXLEN={{item.PREFIXLEN}},
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 5.3 新建BFD会话。

##### 5.3.1 //配置BFD单臂echo探测。PE不支持BFD时，请配置该步骤。PE支持BFD时，可采用单臂echo或双向BFD探测。

```jinja2
{%- if is_scenario_direct_to_pe and is_scenario_bfd_onearm_echo -%}
    {%- for item in add_bfdsession_list_4 -%}
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
{%- endif -%}
```

##### 5.3.2 //配置双向BFD探测。PE支持BFD探测且使用双向BFD探测时，如采用静态会话，请配置该步骤。其他场景请跳过该步骤。

```jinja2
{%- if is_scenario_direct_to_pe and is_scenario_bfd_bidirectional_static -%}
    {%- for item in add_bfdsession_list_6 -%}
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
        {#- --- 条件必选：ONEARMECHO=FALSE 时必选 --- -#}
        {%- if item.ONEARMECHO == 'FALSE' -%}
            REMOTEDISCR={{item.REMOTEDISCR}},
        {#- --- 条件必选：ONEARMECHO6=FALSE 时必选 --- -#}
        {%- elif item.ONEARMECHO6 == 'FALSE' -%}
            REMOTEDISCR={{item.REMOTEDISCR}},
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
        {#- --- 条件可选：CREATETYPE4=SESS_AUTO 时可选 --- -#}
        {%- if item.CREATETYPE4 == 'SESS_AUTO' -%}
            {%- if item.MINTXINT is not none -%}
                MINTXINT={{item.MINTXINT}},
            {%- endif -%}
        {#- --- 条件可选：CREATETYPE6=SESS_AUTO 时可选 --- -#}
        {%- elif item.CREATETYPE6 == 'SESS_AUTO' -%}
            {%- if item.MINTXINT is not none -%}
                MINTXINT={{item.MINTXINT}},
            {%- endif -%}
        {#- --- 条件可选：ONEARMECHO=FALSE 时可选 --- -#}
        {%- elif item.ONEARMECHO == 'FALSE' -%}
            {%- if item.MINTXINT is not none -%}
                MINTXINT={{item.MINTXINT}},
            {%- endif -%}
        {#- --- 条件可选：ONEARMECHO6=FALSE 时可选 --- -#}
        {%- elif item.ONEARMECHO6 == 'FALSE' -%}
            {%- if item.MINTXINT is not none -%}
                MINTXINT={{item.MINTXINT}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：CREATETYPE4=SESS_AUTO 时可选 --- -#}
        {%- if item.CREATETYPE4 == 'SESS_AUTO' -%}
            {%- if item.MINRXINT is not none -%}
                MINRXINT={{item.MINRXINT}},
            {%- endif -%}
        {#- --- 条件可选：CREATETYPE6=SESS_AUTO 时可选 --- -#}
        {%- elif item.CREATETYPE6 == 'SESS_AUTO' -%}
            {%- if item.MINRXINT is not none -%}
                MINRXINT={{item.MINRXINT}},
            {%- endif -%}
        {#- --- 条件可选：ONEARMECHO=FALSE 时可选 --- -#}
        {%- elif item.ONEARMECHO == 'FALSE' -%}
            {%- if item.MINRXINT is not none -%}
                MINRXINT={{item.MINRXINT}},
            {%- endif -%}
        {#- --- 条件可选：ONEARMECHO6=FALSE 时可选 --- -#}
        {%- elif item.ONEARMECHO6 == 'FALSE' -%}
            {%- if item.MINRXINT is not none -%}
                MINRXINT={{item.MINRXINT}},
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
{%- endif -%}
```

##### 5.3.3 //配置双向BFD探测。PE支持BFD探测且使用双向BFD探测时，如采用静态自协商会话，请配置该步骤。其他场景请跳过该步骤。

```jinja2
{%- if is_scenario_direct_to_pe and is_scenario_bfd_bidirectional_auto -%}
    {%- for item in add_bfdsession_list_8 -%}
        ADD BFDSESSION:
        {#- --- 必选参数 --- -#}
        SESSNAME="{{item.SESSNAME}}",
        ADDRTYPE={{item.ADDRTYPE}},
        LINKTYPE={{item.LINKTYPE}},
        {#- --- 可选参数 --- -#}
        {%- if item.DETECTMULTI is not none -%}
            DETECTMULTI={{item.DETECTMULTI}},
        {%- endif -%}
        {%- if item.ADMINDOWN is not none -%}
            ADMINDOWN={{item.ADMINDOWN}},
        {%- endif -%}
        {%- if item.VRFNAME is not none -%}
            VRFNAME="{{item.VRFNAME}}",
        {%- endif -%}
        {%- if item.PROCESSPST is not none -%}
            PROCESSPST={{item.PROCESSPST}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：ADDRTYPE=IPv4 时必选 --- -#}
        {%- if item.ADDRTYPE == 'IPv4' -%}
            CREATETYPE4={{item.CREATETYPE4}},
        {%- endif -%}
        {#- --- 条件必选：ADDRTYPE=IPv4 时必选 --- -#}
        {%- if item.ADDRTYPE == 'IPv4' -%}
            DESTADDR4="{{item.DESTADDR4}}",
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
        {#- --- 条件可选：CREATETYPE4=SESS_AUTO 时可选 --- -#}
        {%- if item.CREATETYPE4 == 'SESS_AUTO' -%}
            {%- if item.MINTXINT is not none -%}
                MINTXINT={{item.MINTXINT}},
            {%- endif -%}
        {#- --- 条件可选：CREATETYPE6=SESS_AUTO 时可选 --- -#}
        {%- elif item.CREATETYPE6 == 'SESS_AUTO' -%}
            {%- if item.MINTXINT is not none -%}
                MINTXINT={{item.MINTXINT}},
            {%- endif -%}
        {#- --- 条件可选：ONEARMECHO=FALSE 时可选 --- -#}
        {%- elif item.ONEARMECHO == 'FALSE' -%}
            {%- if item.MINTXINT is not none -%}
                MINTXINT={{item.MINTXINT}},
            {%- endif -%}
        {#- --- 条件可选：ONEARMECHO6=FALSE 时可选 --- -#}
        {%- elif item.ONEARMECHO6 == 'FALSE' -%}
            {%- if item.MINTXINT is not none -%}
                MINTXINT={{item.MINTXINT}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：CREATETYPE4=SESS_AUTO 时可选 --- -#}
        {%- if item.CREATETYPE4 == 'SESS_AUTO' -%}
            {%- if item.MINRXINT is not none -%}
                MINRXINT={{item.MINRXINT}},
            {%- endif -%}
        {#- --- 条件可选：CREATETYPE6=SESS_AUTO 时可选 --- -#}
        {%- elif item.CREATETYPE6 == 'SESS_AUTO' -%}
            {%- if item.MINRXINT is not none -%}
                MINRXINT={{item.MINRXINT}},
            {%- endif -%}
        {#- --- 条件可选：ONEARMECHO=FALSE 时可选 --- -#}
        {%- elif item.ONEARMECHO == 'FALSE' -%}
            {%- if item.MINRXINT is not none -%}
                MINRXINT={{item.MINRXINT}},
            {%- endif -%}
        {#- --- 条件可选：ONEARMECHO6=FALSE 时可选 --- -#}
        {%- elif item.ONEARMECHO6 == 'FALSE' -%}
            {%- if item.MINRXINT is not none -%}
                MINRXINT={{item.MINRXINT}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件必选/可选参数 --- -#}
        {#- --- IPv4源地址: 条件必选(IPv4会话创建方式=SESS_AUTO) / 条件可选(IPv4单臂Echo=TRUE|FALSE) --- -#}
        {%- if (item.CREATETYPE4 == 'SESS_AUTO') -%}
            SRCADDR4="{{item.SRCADDR4}}",
        {%- elif (item.ONEARMECHO in ['TRUE', 'FALSE']) -%}
            {%- if item.SRCADDR4 is not none -%}
                SRCADDR4="{{item.SRCADDR4}}",
            {%- endif -%}
        {%- endif -%}
        {#- --- 出接口名称: 条件必选(IPv4单臂Echo=TRUE; IPv6单臂Echo=TRUE) / 条件可选(IPv4会话创建方式=SESS_AUTO; IPv6会话创建方式=SESS_AUTO; IPv4单臂Echo=FALSE; IPv6单臂Echo=FALSE) --- -#}
        {%- if (item.ONEARMECHO == 'TRUE') or (item.ONEARMECHO6 == 'TRUE') -%}
            IFNAME="{{item.IFNAME}}",
        {%- elif (item.CREATETYPE4 == 'SESS_AUTO') or (item.CREATETYPE6 == 'SESS_AUTO') or (item.ONEARMECHO == 'FALSE') or (item.ONEARMECHO6 == 'FALSE') -%}
            {%- if item.IFNAME is not none -%}
                IFNAME="{{item.IFNAME}}",
            {%- endif -%}
        {%- endif -%}
        {#- --- IPv6源地址: 条件必选(IPv6会话创建方式=SESS_AUTO) / 条件可选(IPv6单臂Echo=TRUE|FALSE) --- -#}
        {%- if (item.CREATETYPE6 == 'SESS_AUTO') -%}
            SRCADDR6="{{item.SRCADDR6}}",
        {%- elif (item.ONEARMECHO6 in ['TRUE', 'FALSE']) -%}
            {%- if item.SRCADDR6 is not none -%}
                SRCADDR6="{{item.SRCADDR6}}",
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 5.4 配置静态路由并绑定BFD会话。

##### 5.4.1 //“PREFIX”/“MASKLENGTH”是基站的IP地址及所在网段掩码长度，请根据网设文档替换。

```jinja2
{%- if is_scenario_direct_to_pe -%}
    {%- for item in add_srroute_list_6 -%}
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
{%- endif -%}
```

```jinja2
{%- if is_scenario_direct_to_pe -%}
    {%- for item in add_srroute6_list_6 -%}
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
{%- endif -%}
```

### 6 配置UPF（UEG）到园区（VRF\_LocalDN1）服务器的IP路由数据。采用静态路由或BGP over静态路由时，请参考本步骤进行配置。如采用OSPF动态路由，请跳过本步骤。

#### 6.1 配置VPN实例。

```jinja2
{%- if is_scenario_static_route -%}
    {%- for item in add_l3vpninst_list_2 -%}
        ADD L3VPNINST:
        {#- --- 必选参数 --- -#}
        VRFNAME="{{item.VRFNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_static_route -%}
    {%- for item in add_vpninstaf_list_4 -%}
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
{%- endif -%}
```

#### 步骤6.b~步骤6.f是BGP相关数据，仅采用BGP over静态路由+BFD时需要配置。采用静态路由+BFD时不需要配置。

#### 6.2 配置Loopback接口IP。用于建立BGP邻居。

```jinja2
{%- if is_scenario_static_route and is_scenario_bgp_over_static_route -%}
    {%- for item in add_interface_list_7 -%}
        ADD INTERFACE:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_static_route and is_scenario_bgp_over_static_route -%}
    {%- for item in add_ipbindvpn_list_4 -%}
        ADD IPBINDVPN:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        VRFNAME="{{item.VRFNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_static_route and is_scenario_bgp_over_static_route -%}
    {%- for item in add_ifipv4address_list_4 -%}
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
{%- endif -%}
```

```jinja2
{%- if is_scenario_static_route and is_scenario_bgp_over_static_route -%}
    {%- for item in set_ifipv6enable_list_4 -%}
        SET IFIPV6ENABLE:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        ENABLEFLAG={{item.ENABLEFLAG}},
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_static_route and is_scenario_bgp_over_static_route -%}
    {%- for item in add_ifipv6address_list_4 -%}
        ADD IFIPV6ADDRESS:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        IPV6ADDRESS="{{item.IPV6ADDRESS}}",
        PREFIXLEN={{item.PREFIXLEN}},
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 6.3 配置BGP VPN实例。

```jinja2
{%- if is_scenario_static_route and is_scenario_bgp_over_static_route -%}
    {%- for item in add_bgpvrf_list_1 -%}
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
{%- endif -%}
```

#### 6.4 增加BGP VPN实例地址族。UEG对接2个负荷分担的BGP PEER时，“MAXIMUMLOADBALANCE”设置为“2”。

```jinja2
{%- if is_scenario_static_route and is_scenario_bgp_over_static_route -%}
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

#### 6.5 配置BGP对等体。此处以对接2个IPv4v6双栈的BGP对等体为例。

```jinja2
{%- if is_scenario_static_route and is_scenario_bgp_over_static_route -%}
    {%- for item in add_bgppeer_list_4 -%}
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
{%- endif -%}
```

#### 6.6 配置BGP引入wlr路由。

##### 6.6.1 //UPF采用主备容灾方案时，需要将“MEDENABLE”设置为“TRUE”，且备UPF的“MED”值必须大于主UPF的MED值。

```jinja2
{%- if is_scenario_static_route and is_scenario_bgp_over_static_route -%}
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
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 6.7 配置外联口IP地址。

##### 6.7.1 查询接口名，确认可使用的外联口的接口类型和接口编号。

##### 6.7.2 配置主接口的管理状态为up。将网设规划的接口的管理状态设置为up。

```jinja2
{%- if is_scenario_static_route -%}
    {%- for item in mod_interface_list_6 -%}
        MOD INTERFACE:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        {#- --- 可选参数 --- -#}
        {%- if item.IFADMINSTATUS is not none -%}
            IFADMINSTATUS={{item.IFADMINSTATUS}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 6.7.3 添加以太网子接口。

```jinja2
{%- if is_scenario_static_route -%}
    {%- for item in add_interface_list_8 -%}
        ADD INTERFACE:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 6.7.4 增加接口绑定VPN。

```jinja2
{%- if is_scenario_static_route -%}
    {%- for item in add_ipbindvpn_list_5 -%}
        ADD IPBINDVPN:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        VRFNAME="{{item.VRFNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 6.7.5 在以太网子接口上关联VLAN ID。

```jinja2
{%- if is_scenario_static_route -%}
    {%- for item in add_ethsubif_list_3 -%}
        ADD ETHSUBIF:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        VLANTYPEVID={{item.VLANTYPEVID}},
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 6.7.6 配置IPv6使能。

```jinja2
{%- if is_scenario_static_route -%}
    {%- for item in set_ifipv6enable_list_5 -%}
        SET IFIPV6ENABLE:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        ENABLEFLAG={{item.ENABLEFLAG}},
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 6.7.7 配置外联口IP地址。

```jinja2
{%- if is_scenario_static_route -%}
    {%- for item in add_ifipv4address_list_5 -%}
        ADD IFIPV4ADDRESS:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        IFIPADDR="{{item.IFIPADDR}}",
        SUBNETMASK="{{item.SUBNETMASK}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_static_route -%}
    {%- for item in add_ifipv6address_list_5 -%}
        ADD IFIPV6ADDRESS:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        IPV6ADDRESS="{{item.IPV6ADDRESS}}",
        PREFIXLEN={{item.PREFIXLEN}},
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 6.8 新建BFD会话。

##### 6.8.1 //配置BFD单臂echo探测。直连DCGW场景或PE不支持BFD时，请配置该步骤。PE支持BFD时，可采用单臂echo或双向BFD探测。

```jinja2
{%- if is_scenario_static_route and is_scenario_bfd_onearm_echo -%}
    {%- for item in add_bfdsession_list_10 -%}
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
{%- endif -%}
```

##### 6.8.2 //配置双向BFD探测。PE支持BFD探测且使用双向BFD探测时，如采用静态会话，请配置该步骤。其他场景请跳过该步骤。

```jinja2
{%- if is_scenario_static_route and is_scenario_bfd_bidirectional_static -%}
    {%- for item in add_bfdsession_list_14 -%}
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
        {#- --- 条件必选：ONEARMECHO=FALSE 时必选 --- -#}
        {%- if item.ONEARMECHO == 'FALSE' -%}
            REMOTEDISCR={{item.REMOTEDISCR}},
        {#- --- 条件必选：ONEARMECHO6=FALSE 时必选 --- -#}
        {%- elif item.ONEARMECHO6 == 'FALSE' -%}
            REMOTEDISCR={{item.REMOTEDISCR}},
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
        {#- --- 条件可选：CREATETYPE4=SESS_AUTO 时可选 --- -#}
        {%- if item.CREATETYPE4 == 'SESS_AUTO' -%}
            {%- if item.MINTXINT is not none -%}
                MINTXINT={{item.MINTXINT}},
            {%- endif -%}
        {#- --- 条件可选：CREATETYPE6=SESS_AUTO 时可选 --- -#}
        {%- elif item.CREATETYPE6 == 'SESS_AUTO' -%}
            {%- if item.MINTXINT is not none -%}
                MINTXINT={{item.MINTXINT}},
            {%- endif -%}
        {#- --- 条件可选：ONEARMECHO=FALSE 时可选 --- -#}
        {%- elif item.ONEARMECHO == 'FALSE' -%}
            {%- if item.MINTXINT is not none -%}
                MINTXINT={{item.MINTXINT}},
            {%- endif -%}
        {#- --- 条件可选：ONEARMECHO6=FALSE 时可选 --- -#}
        {%- elif item.ONEARMECHO6 == 'FALSE' -%}
            {%- if item.MINTXINT is not none -%}
                MINTXINT={{item.MINTXINT}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：CREATETYPE4=SESS_AUTO 时可选 --- -#}
        {%- if item.CREATETYPE4 == 'SESS_AUTO' -%}
            {%- if item.MINRXINT is not none -%}
                MINRXINT={{item.MINRXINT}},
            {%- endif -%}
        {#- --- 条件可选：CREATETYPE6=SESS_AUTO 时可选 --- -#}
        {%- elif item.CREATETYPE6 == 'SESS_AUTO' -%}
            {%- if item.MINRXINT is not none -%}
                MINRXINT={{item.MINRXINT}},
            {%- endif -%}
        {#- --- 条件可选：ONEARMECHO=FALSE 时可选 --- -#}
        {%- elif item.ONEARMECHO == 'FALSE' -%}
            {%- if item.MINRXINT is not none -%}
                MINRXINT={{item.MINRXINT}},
            {%- endif -%}
        {#- --- 条件可选：ONEARMECHO6=FALSE 时可选 --- -#}
        {%- elif item.ONEARMECHO6 == 'FALSE' -%}
            {%- if item.MINRXINT is not none -%}
                MINRXINT={{item.MINRXINT}},
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
{%- endif -%}
```

##### 6.8.3 //配置双向BFD探测。PE支持BFD探测且使用双向BFD探测时，如采用静态自协商会话，请配置该步骤。其他场景请跳过该步骤。

```jinja2
{%- if is_scenario_static_route and is_scenario_bfd_bidirectional_auto -%}
    {%- for item in add_bfdsession_list_18 -%}
        ADD BFDSESSION:
        {#- --- 必选参数 --- -#}
        SESSNAME="{{item.SESSNAME}}",
        ADDRTYPE={{item.ADDRTYPE}},
        LINKTYPE={{item.LINKTYPE}},
        {#- --- 可选参数 --- -#}
        {%- if item.DETECTMULTI is not none -%}
            DETECTMULTI={{item.DETECTMULTI}},
        {%- endif -%}
        {%- if item.ADMINDOWN is not none -%}
            ADMINDOWN={{item.ADMINDOWN}},
        {%- endif -%}
        {%- if item.VRFNAME is not none -%}
            VRFNAME="{{item.VRFNAME}}",
        {%- endif -%}
        {%- if item.PROCESSPST is not none -%}
            PROCESSPST={{item.PROCESSPST}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：ADDRTYPE=IPv4 时必选 --- -#}
        {%- if item.ADDRTYPE == 'IPv4' -%}
            CREATETYPE4={{item.CREATETYPE4}},
        {%- endif -%}
        {#- --- 条件必选：ADDRTYPE=IPv4 时必选 --- -#}
        {%- if item.ADDRTYPE == 'IPv4' -%}
            DESTADDR4="{{item.DESTADDR4}}",
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
        {#- --- 条件可选：CREATETYPE4=SESS_AUTO 时可选 --- -#}
        {%- if item.CREATETYPE4 == 'SESS_AUTO' -%}
            {%- if item.MINTXINT is not none -%}
                MINTXINT={{item.MINTXINT}},
            {%- endif -%}
        {#- --- 条件可选：CREATETYPE6=SESS_AUTO 时可选 --- -#}
        {%- elif item.CREATETYPE6 == 'SESS_AUTO' -%}
            {%- if item.MINTXINT is not none -%}
                MINTXINT={{item.MINTXINT}},
            {%- endif -%}
        {#- --- 条件可选：ONEARMECHO=FALSE 时可选 --- -#}
        {%- elif item.ONEARMECHO == 'FALSE' -%}
            {%- if item.MINTXINT is not none -%}
                MINTXINT={{item.MINTXINT}},
            {%- endif -%}
        {#- --- 条件可选：ONEARMECHO6=FALSE 时可选 --- -#}
        {%- elif item.ONEARMECHO6 == 'FALSE' -%}
            {%- if item.MINTXINT is not none -%}
                MINTXINT={{item.MINTXINT}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：CREATETYPE4=SESS_AUTO 时可选 --- -#}
        {%- if item.CREATETYPE4 == 'SESS_AUTO' -%}
            {%- if item.MINRXINT is not none -%}
                MINRXINT={{item.MINRXINT}},
            {%- endif -%}
        {#- --- 条件可选：CREATETYPE6=SESS_AUTO 时可选 --- -#}
        {%- elif item.CREATETYPE6 == 'SESS_AUTO' -%}
            {%- if item.MINRXINT is not none -%}
                MINRXINT={{item.MINRXINT}},
            {%- endif -%}
        {#- --- 条件可选：ONEARMECHO=FALSE 时可选 --- -#}
        {%- elif item.ONEARMECHO == 'FALSE' -%}
            {%- if item.MINRXINT is not none -%}
                MINRXINT={{item.MINRXINT}},
            {%- endif -%}
        {#- --- 条件可选：ONEARMECHO6=FALSE 时可选 --- -#}
        {%- elif item.ONEARMECHO6 == 'FALSE' -%}
            {%- if item.MINRXINT is not none -%}
                MINRXINT={{item.MINRXINT}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件必选/可选参数 --- -#}
        {#- --- IPv4源地址: 条件必选(IPv4会话创建方式=SESS_AUTO) / 条件可选(IPv4单臂Echo=TRUE|FALSE) --- -#}
        {%- if (item.CREATETYPE4 == 'SESS_AUTO') -%}
            SRCADDR4="{{item.SRCADDR4}}",
        {%- elif (item.ONEARMECHO in ['TRUE', 'FALSE']) -%}
            {%- if item.SRCADDR4 is not none -%}
                SRCADDR4="{{item.SRCADDR4}}",
            {%- endif -%}
        {%- endif -%}
        {#- --- 出接口名称: 条件必选(IPv4单臂Echo=TRUE; IPv6单臂Echo=TRUE) / 条件可选(IPv4会话创建方式=SESS_AUTO; IPv6会话创建方式=SESS_AUTO; IPv4单臂Echo=FALSE; IPv6单臂Echo=FALSE) --- -#}
        {%- if (item.ONEARMECHO == 'TRUE') or (item.ONEARMECHO6 == 'TRUE') -%}
            IFNAME="{{item.IFNAME}}",
        {%- elif (item.CREATETYPE4 == 'SESS_AUTO') or (item.CREATETYPE6 == 'SESS_AUTO') or (item.ONEARMECHO == 'FALSE') or (item.ONEARMECHO6 == 'FALSE') -%}
            {%- if item.IFNAME is not none -%}
                IFNAME="{{item.IFNAME}}",
            {%- endif -%}
        {%- endif -%}
        {#- --- IPv6源地址: 条件必选(IPv6会话创建方式=SESS_AUTO) / 条件可选(IPv6单臂Echo=TRUE|FALSE) --- -#}
        {%- if (item.CREATETYPE6 == 'SESS_AUTO') -%}
            SRCADDR6="{{item.SRCADDR6}}",
        {%- elif (item.ONEARMECHO6 in ['TRUE', 'FALSE']) -%}
            {%- if item.SRCADDR6 is not none -%}
                SRCADDR6="{{item.SRCADDR6}}",
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 6.9 采用静态路由+BFD时，配置静态路由并绑定BFD会话。采用BGP over静态路由+BFD时，请跳过该步骤。

#### 直连PE时，根据PE能力选择使用“BGP over静态路由+BFD”或“静态路由+BFD”。

#### 直连DCGW时，推荐采用“BGP over静态路由+BFD”。

##### 6.9.1 //“PREFIX”/“MASKLENGTH”是园区服务器的IP地址及所在网段掩码长度，请根据网设文档替换。

```jinja2
{%- if is_scenario_static_route and is_scenario_static_route_bfd -%}
    {%- for item in add_srroute_list_7 -%}
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
{%- endif -%}
```

```jinja2
{%- if is_scenario_static_route and is_scenario_static_route_bfd -%}
    {%- for item in add_srroute6_list_7 -%}
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
{%- endif -%}
```

#### 6.10 采用BGP over静态路由+BFD时，配置静态路由并绑定BFD会话。采用静态路由+BFD时，请跳过该步骤。

##### 6.10.1 //“PREFIX”和“MASKLENGTH”是目的IP和掩码（BGP对等体的IP地址和掩码）。

```jinja2
{%- if is_scenario_static_route and is_scenario_bgp_over_static_route -%}
    {%- for item in add_srroute_list_9 -%}
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
{%- endif -%}
```

##### 6.10.2 //对端网元不发布BGP默认路由时，需要配置该步骤。“PREFIX”设置为“0.0.0.0”，“MASKLENGTH”设置为“0”。其他参数与到BGP对等体的路由相同。

```jinja2
{%- if is_scenario_static_route and is_scenario_bgp_over_static_route and is_scenario_peer_no_default_route -%}
    {%- for item in add_srroute_list_11 -%}
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
{%- endif -%}
```

##### 6.10.3 //“PREFIX”和“MASKLENGTH”是目的IP和掩码（BGP对等体的IP地址和掩码）。

```jinja2
{%- if is_scenario_static_route and is_scenario_bgp_over_static_route -%}
    {%- for item in add_srroute6_list_9 -%}
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
{%- endif -%}
```

##### 6.10.4 //对端网元不发布BGP默认路由时，需要配置该步骤。“PREFIX”设置为“0:0:0:0:0:0:0:0”，“MASKLENGTH”设置为“0”。其他参数与到BGP对等体的路由相同。

```jinja2
{%- if is_scenario_static_route and is_scenario_bgp_over_static_route and is_scenario_peer_no_default_route -%}
    {%- for item in add_srroute6_list_11 -%}
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
{%- endif -%}
```

### 7 配置UPF（UEG）到园区（VRF\_LocalDN1）服务器的IP路由数据。采用OSPF动态路由时，请参考本步骤进行配置。如静态路由或BGP over静态路由，请跳过本步骤。

#### 7.1 配置VPN实例。

```jinja2
{%- if is_scenario_ospf_route -%}
    {%- for item in add_l3vpninst_list_3 -%}
        ADD L3VPNINST:
        {#- --- 必选参数 --- -#}
        VRFNAME="{{item.VRFNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_ospf_route -%}
    {%- for item in add_vpninstaf_list_6 -%}
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
{%- endif -%}
```

#### 7.2 配置外联口IP地址。

##### 7.2.1 查询接口名，确认可使用的外联口的接口类型和接口编号。

##### 7.2.2 配置主接口的管理状态为up。将网设规划的接口的管理状态设置为up。

```jinja2
{%- if is_scenario_ospf_route -%}
    {%- for item in mod_interface_list_8 -%}
        MOD INTERFACE:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        {#- --- 可选参数 --- -#}
        {%- if item.IFADMINSTATUS is not none -%}
            IFADMINSTATUS={{item.IFADMINSTATUS}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 7.2.3 添加以太网子接口。

```jinja2
{%- if is_scenario_ospf_route -%}
    {%- for item in add_interface_list_10 -%}
        ADD INTERFACE:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 7.2.4 增加接口绑定VPN。

```jinja2
{%- if is_scenario_ospf_route -%}
    {%- for item in add_ipbindvpn_list_7 -%}
        ADD IPBINDVPN:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        VRFNAME="{{item.VRFNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 7.2.5 在以太网子接口上关联VLAN ID。

```jinja2
{%- if is_scenario_ospf_route -%}
    {%- for item in add_ethsubif_list_5 -%}
        ADD ETHSUBIF:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        VLANTYPEVID={{item.VLANTYPEVID}},
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 7.2.6 配置IPv6使能。

```jinja2
{%- if is_scenario_ospf_route -%}
    {%- for item in set_ifipv6enable_list_7 -%}
        SET IFIPV6ENABLE:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        ENABLEFLAG={{item.ENABLEFLAG}},
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 7.2.7 配置外联口IP地址。

```jinja2
{%- if is_scenario_ospf_route -%}
    {%- for item in add_ifipv4address_list_7 -%}
        ADD IFIPV4ADDRESS:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        IFIPADDR="{{item.IFIPADDR}}",
        SUBNETMASK="{{item.SUBNETMASK}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_ospf_route -%}
    {%- for item in add_ifipv6address_list_7 -%}
        ADD IFIPV6ADDRESS:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        IPV6ADDRESS="{{item.IPV6ADDRESS}}",
        PREFIXLEN={{item.PREFIXLEN}},
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 7.3 配置OSPF路由数据。该步骤适用于IPv4组网或IPv4v6双栈组网。

##### 7.3.1 创建OSPF进程。此处以网关设备（如FW）不支持BFD为例。

```jinja2
{%- if is_scenario_ospf_route -%}
    {%- for item in add_ospf_list -%}
        ADD OSPF:
        {#- --- 必选参数 --- -#}
        PROCID={{item.PROCID}},
        {#- --- 可选参数 --- -#}
        {%- if item.VRFNAME is not none -%}
            VRFNAME="{{item.VRFNAME}}",
        {%- endif -%}
        {%- if item.SCHEMAROUID is not none -%}
            SCHEMAROUID="{{item.SCHEMAROUID}}",
        {%- endif -%}
        {%- if item.BFDALLINTFFLG is not none -%}
            BFDALLINTFFLG={{item.BFDALLINTFFLG}},
        {%- endif -%}
        {%- if item.LSAARRINTVFLAG is not none -%}
            LSAARRINTVFLAG={{item.LSAARRINTVFLAG}},
        {%- endif -%}
        {%- if item.VPNINSCAPSIMFLG is not none -%}
            VPNINSCAPSIMFLG={{item.VPNINSCAPSIMFLG}},
        {%- endif -%}
        {%- if item.VIRTUALSYSFLAG is not none -%}
            VIRTUALSYSFLAG={{item.VIRTUALSYSFLAG}},
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
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 7.3.2 增加OSPF区域。

```jinja2
{%- if is_scenario_ospf_route -%}
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
{%- endif -%}
```

##### 7.3.3 配置OSPF协议的接口属性。

```jinja2
{%- if is_scenario_ospf_route -%}
    {%- for item in add_ospfinterface_list -%}
        ADD OSPFINTERFACE:
        {#- --- 必选参数 --- -#}
        PROCID={{item.PROCID}},
        AREAID="{{item.AREAID}}",
        IFNAME="{{item.IFNAME}}",
        {#- --- 可选参数 --- -#}
        {%- if item.DRPRI is not none -%}
            DRPRI={{item.DRPRI}},
        {%- endif -%}
        {%- if item.VIRTUALSYSFLAG is not none -%}
            VIRTUALSYSFLAG={{item.VIRTUALSYSFLAG}},
        {%- endif -%}
        {%- if item.MAXCOSTFLAG is not none -%}
            MAXCOSTFLAG={{item.MAXCOSTFLAG}},
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：VIRTUALSYSFLAG=TRUE 时可选 --- -#}
        {%- if item.VIRTUALSYSFLAG == 'TRUE' -%}
            {%- if item.CFGROUTERIDFLAG is not none -%}
                CFGROUTERIDFLAG={{item.CFGROUTERIDFLAG}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 7.3.4 设置OSPF引入的路由类型。

```jinja2
{%- if is_scenario_ospf_route -%}
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
{%- endif -%}
```

#### 7.4 配置OSPFv3路由数据。该步骤适用于IPv6组网或IPv4v6双栈组网。

##### 7.4.1 创建OSPFv3进程。此处以网关设备（如FW）不支持BFD为例。

```jinja2
{%- if is_scenario_ospf_route -%}
    {%- for item in add_ospfv3_list -%}
        ADD OSPFV3:
        {#- --- 必选参数 --- -#}
        PROCID={{item.PROCID}},
        ROUTERID="{{item.ROUTERID}}",
        {#- --- 可选参数 --- -#}
        {%- if item.VRFNAME is not none -%}
            VRFNAME="{{item.VRFNAME}}",
        {%- endif -%}
        {%- if item.BFDALLINTFFLG is not none -%}
            BFDALLINTFFLG={{item.BFDALLINTFFLG}},
        {%- endif -%}
        {%- if item.VPNINSCAPSIMFLG is not none -%}
            VPNINSCAPSIMFLG={{item.VPNINSCAPSIMFLG}},
        {%- endif -%}
        {%- if item.VIRTUALSYSFLAG is not none -%}
            VIRTUALSYSFLAG={{item.VIRTUALSYSFLAG}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 7.4.2 增加OSPFv3区域。

```jinja2
{%- if is_scenario_ospf_route -%}
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
{%- endif -%}
```

##### 7.4.3 配置OSPFv3协议的接口属性。

```jinja2
{%- if is_scenario_ospf_route -%}
    {%- for item in add_ospfv3interface_list -%}
        ADD OSPFV3INTERFACE:
        {#- --- 必选参数 --- -#}
        PROCID={{item.PROCID}},
        AREAID="{{item.AREAID}}",
        IFNAME="{{item.IFNAME}}",
        {#- --- 可选参数 --- -#}
        {%- if item.DRPRI is not none -%}
            DRPRI={{item.DRPRI}},
        {%- endif -%}
        {%- if item.VIRTUALSYSFLAG is not none -%}
            VIRTUALSYSFLAG={{item.VIRTUALSYSFLAG}},
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：VIRTUALSYSFLAG=TRUE 时可选 --- -#}
        {%- if item.VIRTUALSYSFLAG == 'TRUE' -%}
            {%- if item.CFGROUTERIDFLAG is not none -%}
                CFGROUTERIDFLAG={{item.CFGROUTERIDFLAG}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 7.4.4 设置OSPFv3引入的路由类型。

```jinja2
{%- if is_scenario_ospf_route -%}
    {%- for item in add_ospfv3importroute_list -%}
        ADD OSPFV3IMPORTROUTE:
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
{%- endif -%}
```

### 8 配置逻辑接口。

#### 8.1 配置Sa/N3/S1-U逻辑接口。

##### 8.1.1 配置Sa/N3/S1-U逻辑接口所属的VPN实例。

```jinja2
{%- for item in add_vpninst_list -%}
    ADD VPNINST:
    {#- --- 必选参数 --- -#}
    VPNINSTANCE="{{item.VPNINSTANCE}}",
    ;
{%- endfor -%}
```

##### 8.1.2 配置Sa/N3/S1-U逻辑接口。

```jinja2
{%- for item in add_logicinf_list -%}
    ADD LOGICINF:
    {#- --- 必选参数 --- -#}
    NAME="{{item.NAME}}",
    IPVERSION={{item.IPVERSION}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPVERSION=IPV4/IPVER_ALL 时必选 --- -#}
    {%- if item.IPVERSION in ['IPV4', 'IPVER_ALL'] -%}
        IPV4ADDRESS1="{{item.IPV4ADDRESS1}}",
    {%- endif -%}
    {#- --- 条件必选：IPVERSION=IPV4/IPVER_ALL 时必选 --- -#}
    {%- if item.IPVERSION in ['IPV4', 'IPVER_ALL'] -%}
        IPV4MASK1="{{item.IPV4MASK1}}",
    {%- endif -%}
    {#- --- 条件必选：IPVERSION=IPVER_ALL/IPV6 时必选 --- -#}
    {%- if item.IPVERSION in ['IPVER_ALL', 'IPV6'] -%}
        IPV6ADDRESS1="{{item.IPV6ADDRESS1}}",
    {%- endif -%}
    {#- --- 条件必选：IPVERSION=IPVER_ALL/IPV6 时必选 --- -#}
    {%- if item.IPVERSION in ['IPVER_ALL', 'IPV6'] -%}
        IPV6PREFIXLEN1={{item.IPV6PREFIXLEN1}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：IPVERSION=IPV4/IPVER_ALL/IPV6 时可选 --- -#}
    {%- if item.IPVERSION in ['IPV4', 'IPVER_ALL', 'IPV6'] -%}
        {%- if item.VPNINSTANCE is not none -%}
            VPNINSTANCE="{{item.VPNINSTANCE}}",
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 8.2 配置N4（N4/Sxa/Sxb）逻辑接口。

##### 8.2.1 配置N4（N4/Sxa/Sxb）逻辑接口所属的VPN实例。

```jinja2
{%- for item in add_vpninst_list_1 -%}
    ADD VPNINST:
    {#- --- 必选参数 --- -#}
    VPNINSTANCE="{{item.VPNINSTANCE}}",
    ;
{%- endfor -%}
```

##### UPF和SMF上，N4逻辑接口绑定的VPN实例相同。为简化配置，同一UEG内各NF互通的逻辑接口（如N4/N8/N10/N11/N12等），推荐绑定相同的VPN实例。

##### 8.2.2 配置N4（N4/Sxa/Sxb）逻辑接口。

```jinja2
{%- for item in add_logicinf_list_1 -%}
    ADD LOGICINF:
    {#- --- 必选参数 --- -#}
    NAME="{{item.NAME}}",
    IPVERSION={{item.IPVERSION}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPVERSION=IPV4/IPVER_ALL 时必选 --- -#}
    {%- if item.IPVERSION in ['IPV4', 'IPVER_ALL'] -%}
        IPV4ADDRESS1="{{item.IPV4ADDRESS1}}",
    {%- endif -%}
    {#- --- 条件必选：IPVERSION=IPV4/IPVER_ALL 时必选 --- -#}
    {%- if item.IPVERSION in ['IPV4', 'IPVER_ALL'] -%}
        IPV4MASK1="{{item.IPV4MASK1}}",
    {%- endif -%}
    {#- --- 条件必选：IPVERSION=IPVER_ALL/IPV6 时必选 --- -#}
    {%- if item.IPVERSION in ['IPVER_ALL', 'IPV6'] -%}
        IPV6ADDRESS1="{{item.IPV6ADDRESS1}}",
    {%- endif -%}
    {#- --- 条件必选：IPVERSION=IPVER_ALL/IPV6 时必选 --- -#}
    {%- if item.IPVERSION in ['IPVER_ALL', 'IPV6'] -%}
        IPV6PREFIXLEN1={{item.IPV6PREFIXLEN1}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：IPVERSION=IPV4/IPVER_ALL/IPV6 时可选 --- -#}
    {%- if item.IPVERSION in ['IPV4', 'IPVER_ALL', 'IPV6'] -%}
        {%- if item.VPNINSTANCE is not none -%}
            VPNINSTANCE="{{item.VPNINSTANCE}}",
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

##### 8.2.3 配置UEG信息。

```jinja2
{%- for item in set_upinfo_list -%}
    SET UPINFO:
    {#- --- 可选参数 --- -#}
    {%- if item.HOSTNAME is not none -%}
        HOSTNAME="{{item.HOSTNAME}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 9 配置会话接入数据。

#### 9.1 配置APN/DNN实例。

```jinja2
{%- for item in add_vpninst_list_2 -%}
    ADD VPNINST:
    {#- --- 必选参数 --- -#}
    VPNINSTANCE="{{item.VPNINSTANCE}}",
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_upapn_list -%}
    ADD UPAPN:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    {#- --- 可选参数 --- -#}
    {%- if item.HASVPN is not none -%}
        HASVPN={{item.HASVPN}},
    {%- endif -%}
    {%- if item.HASVPNIPV6 is not none -%}
        HASVPNIPV6={{item.HASVPNIPV6}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：HASVPN=ENABLE 时必选 --- -#}
    {%- if item.HASVPN == 'ENABLE' -%}
        VPNINSTANCE="{{item.VPNINSTANCE}}",
    {%- endif -%}
    {#- --- 条件必选：HASVPNIPV6=ENABLE 时必选 --- -#}
    {%- if item.HASVPNIPV6 == 'ENABLE' -%}
        VPNINSTANCEIPV6="{{item.VPNINSTANCEIPV6}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 9.2 设置APN单通检测。

```jinja2
{%- for item in set_apnsglpass_list -%}
    SET APNSGLPASS:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

#### 9.3 配置APN地址分配属性。

```jinja2
{%- for item in set_apnaddressattr_list -%}
    SET APNADDRESSATTR:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    {#- --- 可选参数 --- -#}
    {%- if item.SUPPORTIPV4 is not none -%}
        SUPPORTIPV4={{item.SUPPORTIPV4}},
    {%- endif -%}
    {%- if item.SUPPORTIPV6 is not none -%}
        SUPPORTIPV6={{item.SUPPORTIPV6}},
    {%- endif -%}
    {%- if item.FRAMEDROUTE is not none -%}
        FRAMEDROUTE={{item.FRAMEDROUTE}},
    {%- endif -%}
    {%- if item.ANTISPOOFINGDL is not none -%}
        ANTISPOOFINGDL={{item.ANTISPOOFINGDL}},
    {%- endif -%}
    {%- if item.ANTISPOOFINGUL is not none -%}
        ANTISPOOFINGUL={{item.ANTISPOOFINGUL}},
    {%- endif -%}
    {%- if item.IPTYPEFORDUALIP is not none -%}
        IPTYPEFORDUALIP={{item.IPTYPEFORDUALIP}},
    {%- endif -%}
    {%- if item.SINGLEADDRCAUSE is not none -%}
        SINGLEADDRCAUSE={{item.SINGLEADDRCAUSE}},
    {%- endif -%}
    {%- if item.IPV6RAMTUSW is not none -%}
        IPV6RAMTUSW={{item.IPV6RAMTUSW}},
    {%- endif -%}
    {%- if item.IPV6RALIFETIME is not none -%}
        IPV6RALIFETIME={{item.IPV6RALIFETIME}},
    {%- endif -%}
    {%- if item.HOSTROUTEIP is not none -%}
        HOSTROUTEIP={{item.HOSTROUTEIP}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：IPTYPEFORDUALIP=IPV4V6 时可选 --- -#}
    {%- if item.IPTYPEFORDUALIP == 'IPV4V6' -%}
        {%- if item.CPCTRL is not none -%}
            CPCTRL={{item.CPCTRL}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 9.4 配置IP地址分配（UE地址使用动态分配地址）。此处以基于APN/DNN给UE分配地址为例。每个UPF需要规划一个独立的UE IP地址段。其他网元分配地址时，请跳过本步骤。

##### 9.4.1 //配置全局地址分配规则。

```jinja2
{%- if is_scenario_dynamic_ip_allocation -%}
    {%- for item in set_ipallocrule_list -%}
        SET IPALLOCRULE:
        {#- --- 可选参数 --- -#}
        {%- if item.FIRSTRULESW is not none -%}
            FIRSTRULESW={{item.FIRSTRULESW}},
        {%- endif -%}
        {%- if item.SECONDRULESW is not none -%}
            SECONDRULESW={{item.SECONDRULESW}},
        {%- endif -%}
        {%- if item.THIRDRULESW is not none -%}
            THIRDRULESW={{item.THIRDRULESW}},
        {%- endif -%}
        {%- if item.IPV6FIRSTRULESW is not none -%}
            IPV6FIRSTRULESW={{item.IPV6FIRSTRULESW}},
        {%- endif -%}
        {%- if item.IPV6SECRULESW is not none -%}
            IPV6SECRULESW={{item.IPV6SECRULESW}},
        {%- endif -%}
        {%- if item.IPV6THIRDRULESW is not none -%}
            IPV6THIRDRULESW={{item.IPV6THIRDRULESW}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：FIRSTRULESW=ENABLE 时必选 --- -#}
        {%- if item.FIRSTRULESW == 'ENABLE' -%}
            FIRSTRULE={{item.FIRSTRULE}},
        {%- endif -%}
        {#- --- 条件必选：IPV6FIRSTRULESW=ENABLE 时必选 --- -#}
        {%- if item.IPV6FIRSTRULESW == 'ENABLE' -%}
            IPV6FIRSTRULE={{item.IPV6FIRSTRULE}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 9.4.2 //配置APN“apn-op1”给UE分配的IP地址段。

```jinja2
{%- if is_scenario_dynamic_ip_allocation -%}
    {%- for item in add_uppool_list -%}
        ADD UPPOOL:
        {#- --- 必选参数 --- -#}
        POOLNAME="{{item.POOLNAME}}",
        {#- --- 可选参数 --- -#}
        {%- if item.POOLTYPE is not none -%}
            POOLTYPE={{item.POOLTYPE}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：HASVPN=ENABLE 时必选 --- -#}
        {%- if item.HASVPN == 'ENABLE' -%}
            VPNINSTANCE="{{item.VPNINSTANCE}}",
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：POOLTYPE=LOCAL/EXTERNAL 时可选 --- -#}
        {%- if item.POOLTYPE in ['LOCAL', 'EXTERNAL'] -%}
            {%- if item.IPVERSION is not none -%}
                IPVERSION={{item.IPVERSION}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：POOLTYPE=LOCAL/EXTERNAL 时可选 --- -#}
        {%- if item.POOLTYPE in ['LOCAL', 'EXTERNAL'] -%}
            {%- if item.HASVPN is not none -%}
                HASVPN={{item.HASVPN}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_dynamic_ip_allocation -%}
    {%- for item in add_section_list -%}
        ADD SECTION:
        {#- --- 必选参数 --- -#}
        POOLNAME="{{item.POOLNAME}}",
        SECTIONNUM={{item.SECTIONNUM}},
        IPVERSION={{item.IPVERSION}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：IPVERSION=IPV4 时必选 --- -#}
        {%- if item.IPVERSION == 'IPV4' -%}
            V4STARTIP="{{item.V4STARTIP}}",
        {%- endif -%}
        {#- --- 条件必选：IPVERSION=IPV4 时必选 --- -#}
        {%- if item.IPVERSION == 'IPV4' -%}
            V4ENDIP="{{item.V4ENDIP}}",
        {%- endif -%}
        {#- --- 条件必选：IPVERSION=IPV6 时必选 --- -#}
        {%- if item.IPVERSION == 'IPV6' -%}
            V6PREFIXSTART="{{item.V6PREFIXSTART}}",
        {%- endif -%}
        {#- --- 条件必选：IPVERSION=IPV6 时必选 --- -#}
        {%- if item.IPVERSION == 'IPV6' -%}
            V6PREFIXEND="{{item.V6PREFIXEND}}",
        {%- endif -%}
        {#- --- 条件必选：IPVERSION=IPV6 时必选 --- -#}
        {%- if item.IPVERSION == 'IPV6' -%}
            V6PREFIXLENGTH={{item.V6PREFIXLENGTH}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_dynamic_ip_allocation -%}
    {%- for item in add_poolgroup_list -%}
        ADD POOLGROUP:
        {#- --- 必选参数 --- -#}
        POOLGRPNAME="{{item.POOLGRPNAME}}",
        {#- --- 可选参数 --- -#}
        {%- if item.IPV4ALLOCPRIALG is not none -%}
            IPV4ALLOCPRIALG={{item.IPV4ALLOCPRIALG}},
        {%- endif -%}
        {%- if item.IPV6ALLOCPRIALG is not none -%}
            IPV6ALLOCPRIALG={{item.IPV6ALLOCPRIALG}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_dynamic_ip_allocation -%}
    {%- for item in add_poolbindgroup_list -%}
        ADD POOLBINDGROUP:
        {#- --- 必选参数 --- -#}
        POOLGROUPNAME="{{item.POOLGROUPNAME}}",
        POOLNAME="{{item.POOLNAME}}",
        {#- --- 可选参数 --- -#}
        {%- if item.PRIORITY is not none -%}
            PRIORITY={{item.PRIORITY}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_dynamic_ip_allocation -%}
    {%- for item in add_poolgrpmap_list -%}
        ADD POOLGRPMAP:
        {#- --- 必选参数 --- -#}
        MAPPINGNAME="{{item.MAPPINGNAME}}",
        POOLGROUPNAME="{{item.POOLGROUPNAME}}",
        {#- --- 可选参数 --- -#}
        {%- if item.APN is not none -%}
            APN="{{item.APN}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 9.5 配置IP地址分配（UE地址使用静态签约地址）。使用UPF动态给UE分配IP时，请跳过本步骤。

#### 静态签约场景，配置IP地址分配用于对外发布wlr\_ud路由，避免静态用户激活后生成大量主机路由。地址段从UDM签约数据获取。

##### 9.5.1 //配置全局地址分配规则。

```jinja2
{%- if is_scenario_static_ip_allocation -%}
    {%- for item in set_ipallocrule_list_1 -%}
        SET IPALLOCRULE:
        {#- --- 可选参数 --- -#}
        {%- if item.FIRSTRULESW is not none -%}
            FIRSTRULESW={{item.FIRSTRULESW}},
        {%- endif -%}
        {%- if item.SECONDRULESW is not none -%}
            SECONDRULESW={{item.SECONDRULESW}},
        {%- endif -%}
        {%- if item.THIRDRULESW is not none -%}
            THIRDRULESW={{item.THIRDRULESW}},
        {%- endif -%}
        {%- if item.IPV6FIRSTRULESW is not none -%}
            IPV6FIRSTRULESW={{item.IPV6FIRSTRULESW}},
        {%- endif -%}
        {%- if item.IPV6SECRULESW is not none -%}
            IPV6SECRULESW={{item.IPV6SECRULESW}},
        {%- endif -%}
        {%- if item.IPV6THIRDRULESW is not none -%}
            IPV6THIRDRULESW={{item.IPV6THIRDRULESW}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：FIRSTRULESW=ENABLE 时必选 --- -#}
        {%- if item.FIRSTRULESW == 'ENABLE' -%}
            FIRSTRULE={{item.FIRSTRULE}},
        {%- endif -%}
        {#- --- 条件必选：IPV6FIRSTRULESW=ENABLE 时必选 --- -#}
        {%- if item.IPV6FIRSTRULESW == 'ENABLE' -%}
            IPV6FIRSTRULE={{item.IPV6FIRSTRULE}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 9.5.2 //配置APN“apn-op1”给UE分配的IP地址段。

```jinja2
{%- if is_scenario_static_ip_allocation -%}
    {%- for item in add_uppool_list_2 -%}
        ADD UPPOOL:
        {#- --- 必选参数 --- -#}
        POOLNAME="{{item.POOLNAME}}",
        {#- --- 可选参数 --- -#}
        {%- if item.POOLTYPE is not none -%}
            POOLTYPE={{item.POOLTYPE}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：HASVPN=ENABLE 时必选 --- -#}
        {%- if item.HASVPN == 'ENABLE' -%}
            VPNINSTANCE="{{item.VPNINSTANCE}}",
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：POOLTYPE=LOCAL/EXTERNAL 时可选 --- -#}
        {%- if item.POOLTYPE in ['LOCAL', 'EXTERNAL'] -%}
            {%- if item.IPVERSION is not none -%}
                IPVERSION={{item.IPVERSION}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：POOLTYPE=EXTERNAL 时可选 --- -#}
        {%- if item.POOLTYPE == 'EXTERNAL' -%}
            {%- if item.CHECKIPVALID is not none -%}
                CHECKIPVALID={{item.CHECKIPVALID}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：POOLTYPE=LOCAL/EXTERNAL 时可选 --- -#}
        {%- if item.POOLTYPE in ['LOCAL', 'EXTERNAL'] -%}
            {%- if item.HASVPN is not none -%}
                HASVPN={{item.HASVPN}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：POOLTYPE=LOCAL/EXTERNAL 时可选 --- -#}
        {%- if item.POOLTYPE in ['LOCAL', 'EXTERNAL'] -%}
            {%- if item.IMSSW is not none -%}
                IMSSW={{item.IMSSW}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：POOLTYPE=EXTERNAL 时可选 --- -#}
        {%- if item.POOLTYPE == 'EXTERNAL' -%}
            {%- if item.REDUNDFUNC is not none -%}
                REDUNDFUNC={{item.REDUNDFUNC}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_static_ip_allocation -%}
    {%- for item in add_section_list_2 -%}
        ADD SECTION:
        {#- --- 必选参数 --- -#}
        POOLNAME="{{item.POOLNAME}}",
        SECTIONNUM={{item.SECTIONNUM}},
        IPVERSION={{item.IPVERSION}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：IPVERSION=IPV4 时必选 --- -#}
        {%- if item.IPVERSION == 'IPV4' -%}
            V4STARTIP="{{item.V4STARTIP}}",
        {%- endif -%}
        {#- --- 条件必选：IPVERSION=IPV4 时必选 --- -#}
        {%- if item.IPVERSION == 'IPV4' -%}
            V4ENDIP="{{item.V4ENDIP}}",
        {%- endif -%}
        {#- --- 条件必选：IPVERSION=IPV6 时必选 --- -#}
        {%- if item.IPVERSION == 'IPV6' -%}
            V6PREFIXSTART="{{item.V6PREFIXSTART}}",
        {%- endif -%}
        {#- --- 条件必选：IPVERSION=IPV6 时必选 --- -#}
        {%- if item.IPVERSION == 'IPV6' -%}
            V6PREFIXEND="{{item.V6PREFIXEND}}",
        {%- endif -%}
        {#- --- 条件必选：IPVERSION=IPV6 时必选 --- -#}
        {%- if item.IPVERSION == 'IPV6' -%}
            V6PREFIXLENGTH={{item.V6PREFIXLENGTH}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_static_ip_allocation -%}
    {%- for item in add_poolgroup_list_1 -%}
        ADD POOLGROUP:
        {#- --- 必选参数 --- -#}
        POOLGRPNAME="{{item.POOLGRPNAME}}",
        {#- --- 可选参数 --- -#}
        {%- if item.IPV4ALLOCPRIALG is not none -%}
            IPV4ALLOCPRIALG={{item.IPV4ALLOCPRIALG}},
        {%- endif -%}
        {%- if item.IPV6ALLOCPRIALG is not none -%}
            IPV6ALLOCPRIALG={{item.IPV6ALLOCPRIALG}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_static_ip_allocation -%}
    {%- for item in add_poolbindgroup_list_2 -%}
        ADD POOLBINDGROUP:
        {#- --- 必选参数 --- -#}
        POOLGROUPNAME="{{item.POOLGROUPNAME}}",
        POOLNAME="{{item.POOLNAME}}",
        {#- --- 可选参数 --- -#}
        {%- if item.PRIORITY is not none -%}
            PRIORITY={{item.PRIORITY}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_static_ip_allocation -%}
    {%- for item in add_poolgrpmap_list_1 -%}
        ADD POOLGRPMAP:
        {#- --- 必选参数 --- -#}
        MAPPINGNAME="{{item.MAPPINGNAME}}",
        POOLGROUPNAME="{{item.POOLGROUPNAME}}",
        {#- --- 可选参数 --- -#}
        {%- if item.APN is not none -%}
            APN="{{item.APN}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 9.6 配置本地PCC规则。

##### 9.6.1 //如下脚本必须配置，否则会话建立失败。脚本中参数值“up\_test”可修改为实际规划的值，替换时请注意替换完整，其他参数使用样例值。UserProfilename需要与SMF上配置的UserProfilename一致。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_filter_list -%}
    ADD FILTER:
    {#- --- 必选参数 --- -#}
    FILTERNAME="{{item.FILTERNAME}}",
    L34PROTTYPE={{item.L34PROTTYPE}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：L34PROTTYPE=STRING 时必选 --- -#}
    {%- if item.L34PROTTYPE == 'STRING' -%}
        L34PROTOCOL={{item.L34PROTOCOL}},
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_flowfilter_list -%}
    ADD FLOWFILTER:
    {#- --- 必选参数 --- -#}
    FLOWFILTERNAME="{{item.FLOWFILTERNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.TETHERDETFLAG is not none -%}
        TETHERDETFLAG={{item.TETHERDETFLAG}},
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_fltbindflowf_list -%}
    ADD FLTBINDFLOWF:
    {#- --- 必选参数 --- -#}
    FLOWFILTERNAME="{{item.FLOWFILTERNAME}}",
    FILTERNAME="{{item.FILTERNAME}}",
    ;
{%- endfor -%}
```

```jinja2
{%- for item in set_refreshsrv_list -%}
    SET REFRESHSRV:
    {#- --- 必选参数 --- -#}
    REFRESHTYPE={{item.REFRESHTYPE}},
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_pccpolicygrp_list -%}
    ADD PCCPOLICYGRP:
    {#- --- 必选参数 --- -#}
    PCCPOLICYGRPNM="{{item.PCCPOLICYGRPNM}}",
    {#- --- 可选参数 --- -#}
    {%- if item.FUPSESSIONEXC is not none -%}
        FUPSESSIONEXC={{item.FUPSESSIONEXC}},
    {%- endif -%}
    {%- if item.TOKENFUNCFLAG is not none -%}
        TOKENFUNCFLAG={{item.TOKENFUNCFLAG}},
    {%- endif -%}
    {%- if item.SIGNALASSOCIATE is not none -%}
        SIGNALASSOCIATE={{item.SIGNALASSOCIATE}},
    {%- endif -%}
    {%- if item.ADCMUTEFLAG is not none -%}
        ADCMUTEFLAG={{item.ADCMUTEFLAG}},
    {%- endif -%}
    {%- if item.HTTP2DEGRADESW is not none -%}
        HTTP2DEGRADESW={{item.HTTP2DEGRADESW}},
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_rule_list -%}
    ADD RULE:
    {#- --- 必选参数 --- -#}
    RULENAME="{{item.RULENAME}}",
    POLICYTYPE={{item.POLICYTYPE}},
    FILTERINGMODE={{item.FILTERINGMODE}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：FILTERINGMODE=FLOWFILTER 时必选 --- -#}
    {%- if item.FILTERINGMODE == 'FLOWFILTER' -%}
        FLOWFILTERNAME="{{item.FLOWFILTERNAME}}",
    {%- endif -%}
    {#- --- 条件必选：POLICYTYPE=PCC/BWM/HEADEN/SMARTREDIRECT/TRAFFICCLASS/FIREWALL/QOS/WEBPROXY 时必选 --- -#}
    {%- if item.POLICYTYPE in ['PCC', 'BWM', 'HEADEN', 'SMARTREDIRECT', 'TRAFFICCLASS', 'FIREWALL', 'QOS', 'WEBPROXY'] -%}
        POLICYNAME="{{item.POLICYNAME}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_userprofile_list -%}
    ADD USERPROFILE:
    {#- --- 必选参数 --- -#}
    USERPROFILENAME="{{item.USERPROFILENAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.ALIASMARKFLAG is not none -%}
        ALIASMARKFLAG={{item.ALIASMARKFLAG}},
    {%- endif -%}
    {%- if item.DDOSCHECK is not none -%}
        DDOSCHECK={{item.DDOSCHECK}},
    {%- endif -%}
    {%- if item.LOCRPTSWITCH is not none -%}
        LOCRPTSWITCH={{item.LOCRPTSWITCH}},
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_rulebinding_list -%}
    ADD RULEBINDING:
    {#- --- 必选参数 --- -#}
    USERPROFILENAME="{{item.USERPROFILENAME}}",
    RULENAME="{{item.RULENAME}}",
    ;
{%- endfor -%}
```


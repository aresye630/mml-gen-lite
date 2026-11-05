---
id: ''
name: 配置BGP over 静态路由+BFD（IPv6）
ne_type: UEG
type: feature
description: BGP（Border Gateway Protocol）边界网关协议是一种用于AS(Autonomous System)之间的动态路由协议，与静态路由等内部网关协议（IGP）不同，其自身不能发现和计算路由，主要用于在自治系统AS间控制路由的传播和选择最佳路由。同时，利用BFD检测机制，提高链路可靠性。  当拓扑结构复杂且无法规划在同一自治区域内时，可以采用BGP over 静态路由+BFD实现VNF与对端设备的网络层互通。  如图1所示为UEG与周边网元的BGP over 静态路由+BFD互通组网示意图。UEG与三层路由设备运行BGP over 静态路由+BFD路由协议而接入IP网络（运营商IP骨干网/企业网络），网关可以使用运营商的承载网路由设备，也可以使用DC-GW。DC-GW的配置请参考对应型号设备的产品文档。  **图1** BGP over静态路由+BFD组网  * UEG直连PE时，组bonding的2个端口连接到同一PE设备。 * UEG直连DCGW时，组bonding的2个端口连接到不同DCGW设备。
tags: []
risk_level: ''
doc_source: ["网络部署","园区入驻式（仅连接）","5GC toB 部署边缘站点（站点为“风筝L”，入驻式）","UEG初始配置（风筝L）","参考：详细配置指导","组网路由配置（裸机容器）","配置VNF侧IP路由数据","配置BGP over 静态路由+BFD（IPv6）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
BGP（Border Gateway Protocol）边界网关协议是一种用于AS(Autonomous System)之间的动态路由协议，与静态路由等内部网关协议（IGP）不同，其自身不能发现和计算路由，主要用于在自治系统AS间控制路由的传播和选择最佳路由。同时，利用BFD检测机制，提高链路可靠性。当拓扑结构复杂且无法规划在同一自治区域内时，可以采用BGP over 静态路由+BFD实现VNF与对端设备的网络层互通。如图1所示为UEG与周边网元的BGP over 静态路由+BFD互通组网示意图。UEG与三层路由设备运行BGP over 静态路由+BFD路由协议而接入IP网络（运营商IP骨干网/企业网络），网关可以使用运营商的承载网路由设备，也可以使用DC-GW。DC-GW的配置请参考对应型号设备的产品文档。**图1** BGP over静态路由+BFD组网* UEG直连PE时，组bonding的2个端口连接到同一PE设备。* UEG直连DCGW时，组bonding的2个端口连接到不同DCGW设备。

## 必备事项
前提条件

* 请阅读并熟悉特性IPFD-020502 支持BGP特性概述。

* 具备管理员权限的操作人员已经登录华为操作维护系统（登录MAE客户端或登录OM Portal）。

* UEG与网络实体之间的网络环境已经构建完成。
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
          data_source: '本端规划'
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
          description: 'IPv6组网场景下，该参数选择ipv6uni。'
          data_source: '-'
          pattern: ''
          default: ''
    mod_interface_list:
      type: items
      properties:
        IFNAME:
          name: '接口名称'
          type: string
          maxLength: 63
          required: true
          description: '（UEG-L）请参考外联口介绍(刀片式服务器2U)进行规划。'
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
          data_source: ''
          pattern: ''
          default: ''
    add_interface_list:
      type: items
      properties:
        IFNAME:
          name: '子接口名字'
          type: string
          maxLength: 63
          required: true
          description: '非SR-IOV bonding组网需要规划。   （UEG-L）N6外联口采用非SR-IOV bonding组网，详细请参见外联口介绍(刀片式服务器2U)。'
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
          data_source: ''
          pattern: ''
          default: ''
        VRFNAME:
          name: 'VPN名字'
          type: string
          maxLength: 31
          required: true
          description: '-'
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
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VLANTYPEVID:
          name: 'VLAN类型子接口的VLAN ID'
          type: integer
          minimum: 1
          maximum: 4094
          required: true
          description: '此处以双平面为例，SR-IOV bonding单平面组网时，只需规划一条数据（例如只规划VLAN 100）。'
          data_source: '全网规划'
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
          description: '-'
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
          description: '如果规划外联口使用IPv4v6双栈地址，则分别执行**ADD IFIPV4ADDRESS**和**ADD IFIPV6ADDRESS**  对同一外联口配置IPv4和IPv6地址。'
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
    mod_interface_list_2:
      type: items
      properties:
        IFNAME:
          name: '接口名称'
          type: string
          maxLength: 63
          required: true
          description: '（UEG-L）请参考外联口介绍(刀片式服务器2U)进行规划。'
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
          data_source: ''
          pattern: ''
          default: ''
    add_interface_list_2:
      type: items
      properties:
        IFNAME:
          name: '接口名称'
          type: string
          maxLength: 63
          required: true
          description: 'SR-IOV bonding组网需要规划。   （UEG-L）N3/N4外联口采用SR-IOV bonding组网，详细请参见外联口介绍(刀片式服务器2U)。'
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
          description: 'SR-IOV bonding组网下需要规划。  需保证只有MAC地址一样的VNIC加到同一个Eth-trunk接口中。'
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
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_interface_list_3:
      type: items
      properties:
        IFNAME:
          name: '接口名称'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
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
          name: 'VPN名字'
          type: string
          maxLength: 31
          required: true
          description: '-'
          data_source: '已配置数据中获取'
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
          name: 'VLAN类型子接口的VLAN ID'
          type: integer
          minimum: 1
          maximum: 4094
          required: true
          description: '此处以双平面为例，SR-IOV bonding单平面组网时，只需规划一条数据（例如只规划VLAN 100）。'
          data_source: '全网规划'
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
          description: '-'
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
          description: '如果规划外联口使用IPv4v6双栈地址，则分别执行**ADD IFIPV4ADDRESS**和**ADD IFIPV6ADDRESS**  对同一外联口配置IPv4和IPv6地址。'
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
    set_bfd_list:
      type: items
      properties:
        BFDENABLE:
          name: '激活BFD'
          type: string
          enum:
          - TRUE
          - FALSE
          required: true
          description: '参数“DELAYUPTIMER”（会话延迟UP时间）和“TOSEXP”（动态会话报文优先级）可以不用配置，使用默认值即可。'
          data_source: '全网规划'
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
          description: '-'
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
          data_source: '固定取值'
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
          data_source: '固定取值'
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
          data_source: '全网规划'
          pattern: ''
          default: FALSE
        LINKTYPE:
          name: '链路类型'
          type: string
          enum:
          - IP
          required: true
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: false
          description: '直连DCGW时，DCGW之间是M-LAG组网，该场景下，“ONEARMECHO6”需要设置为“TRUE”。  直连PE设备时，PE不支持BFD探测时，“ONEARMECHO6”需要设置为“TRUE”。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        LOCALDISCR:
          name: '本地标识符'
          type: integer
          minimum: 1
          maximum: 16384
          required: false
          description: 'VNF上BFD会话的本地标识符，需要和对接网关上的标识符对应，即本端的本地标识符与对端网关侧的远端标识符相同。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        REMOTEDISCR:
          name: '远端标识符'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: false
          description: 'VNF上BFD会话的远端标识符，需要和对接网关上的标识符对应，即本端的远端标识符与对端网关侧的本端标识符相同。'
          data_source: '与对端协商'
          pattern: ''
          default: ''
        IFNAME:
          name: '出接口名称'
          type: string
          maxLength: 63
          required: false
          description: '非SR-IOV bonding组网需要规划Ethernet接口，SR-IOV bonding组网需要规划Eth-trunk接口。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        DESTADDR6:
          name: 'IPv6目的地址'
          type: string
          maxLength: 39
          required: false
          description: '参数“DESTADDR6”是网关的接口IP，此处用于检测目的IP能否正常接收报文。'
          data_source: '与对端协商'
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
    add_bfdsession_list_2:
      type: items
      properties:
        SESSNAME:
          name: '会话名称'
          type: string
          maxLength: 64
          required: true
          description: '-'
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
          data_source: '固定取值'
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
          data_source: '固定取值'
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
          data_source: '全网规划'
          pattern: ''
          default: FALSE
        LINKTYPE:
          name: '链路类型'
          type: string
          enum:
          - IP
          required: true
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: false
          description: '直连DCGW时，DCGW之间是M-LAG组网，该场景下，“ONEARMECHO6”需要设置为“TRUE”。  直连PE设备时，PE不支持BFD探测时，“ONEARMECHO6”需要设置为“TRUE”。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        LOCALDISCR:
          name: '本地标识符'
          type: integer
          minimum: 1
          maximum: 16384
          required: false
          description: 'VNF上BFD会话的本地标识符，需要和对接网关上的标识符对应，即本端的本地标识符与对端网关侧的远端标识符相同。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        IFNAME:
          name: '出接口名称'
          type: string
          maxLength: 63
          required: false
          description: '非SR-IOV bonding组网需要规划Ethernet接口，SR-IOV bonding组网需要规划Eth-trunk接口。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        DESTADDR6:
          name: 'IPv6目的地址'
          type: string
          maxLength: 39
          required: false
          description: '参数“DESTADDR6”是网关的接口IP，此处用于检测目的IP能否正常接收报文。'
          data_source: '与对端协商'
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
    add_srroute6_list:
      type: items
      properties:
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: false
          description: 'SR-IOV bonding组网时，1个路由下一跳IP地址。  双平面组网时，2个路由下一跳IP地址在不同网段。  参数“PREFIX”是目的IP，此处是BGP对等体地址。  参数“NEXTHOP”是网关的接口IP。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: '_public_'
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
          data_source: '与对端协商'
          pattern: ''
          default: ''
        MASKLENGTH:
          name: '路由掩码长度'
          type: integer
          minimum: 0
          maximum: 128
          required: true
          description: ''
          data_source: '与对端协商'
          pattern: ''
          default: ''
        DESTVRFNAME:
          name: '下一跳VPN名字'
          type: string
          maxLength: 31
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
          data_source: '已规划数据中获取'
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
        SESSIONNAME:
          name: '静态BFD会话名'
          type: string
          maxLength: 64
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_srroute6_list_2:
      type: items
      properties:
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: false
          description: 'SR-IOV bonding组网时，1个路由下一跳IP地址。  双平面组网时，2个路由下一跳IP地址在不同网段。  参数“PREFIX”是目的IP，此处是BGP对等体地址。  参数“NEXTHOP”是网关的接口IP。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: '_public_'
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
          data_source: '与对端协商'
          pattern: ''
          default: ''
        MASKLENGTH:
          name: '路由掩码长度'
          type: integer
          minimum: 0
          maximum: 128
          required: true
          description: ''
          data_source: '与对端协商'
          pattern: ''
          default: ''
        DESTVRFNAME:
          name: '下一跳VPN名字'
          type: string
          maxLength: 31
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
          data_source: '已规划数据中获取'
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
        SESSIONNAME:
          name: '静态BFD会话名'
          type: string
          maxLength: 64
          required: false
          description: ''
          data_source: '已配置数据中获取'
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
          description: '-'
          data_source: '本端规划'
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
          name: 'VPN名字'
          type: string
          maxLength: 31
          required: true
          description: '-'
          data_source: '已配置数据中获取'
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
          description: '-'
          data_source: '固定取值'
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
          description: '如果规划Loopback接口使用IPv4v6双栈地址，则分别执行**ADD IFIPV4ADDRESS**和**ADD IFIPV6ADDRESS**  对同一Loopback接口配置IPv4和IPv6地址。'
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
          data_source: '-'
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
          name: '路由器标识'
          type: string
          maxLength: 15
          required: false
          description: '不同BGP VPN实例的ROUTERID不能重复。'
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
          description: '使用**ADD BGPVRF**命令定义的VPN实例名称。'
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
          data_source: '固定取值'
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
          description: '“PEERADDRV6”是网关上用于和VNF建立BGP邻居关系的IP地址。'
          data_source: '-'
          pattern: ''
          default: ipv4
        PEERADDRV6:
          name: 'IPv6对等体地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: '与对端协商'
          pattern: ''
          default: ''
        REMOTEAS:
          name: '对等体AS号'
          type: string
          maxLength: 11
          required: false
          description: ''
          data_source: '与对端协商'
          pattern: ''
          default: ''
        LOCALIFADDR:
          name: '本地接口地址'
          type: string
          maxLength: 39
          required: false
          description: ''
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
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_bgppeer_list_2:
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
          description: '“PEERADDRV6”是网关上用于和VNF建立BGP邻居关系的IP地址。'
          data_source: '-'
          pattern: ''
          default: ipv4
        PEERADDRV6:
          name: 'IPv6对等体地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: '与对端协商'
          pattern: ''
          default: ''
        REMOTEAS:
          name: '对等体AS号'
          type: string
          maxLength: 11
          required: false
          description: ''
          data_source: '与对端协商'
          pattern: ''
          default: ''
        LOCALIFADDR:
          name: '本地接口地址'
          type: string
          maxLength: 39
          required: false
          description: ''
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
          description: 'IPv6组网场景下，该参数选择ipv6uni。  该参数全局取值要一致。'
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
          description: '-'
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
          description: '对于N6口，两个UPF上的UE地址段存在重叠且需要对外发布网段路由时（该场景下，两个UPF是主备容灾），该参数设置为“TRUE”；否则，该参数设置为“FALSE”。  对于其他接口，使用默认值“FALSE”即可。'
          data_source: '本端规划'
          pattern: ''
          default: FALSE
        MED:
          name: 'MED'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: false
          description: '“MEDENABLE”设置为“TRUE”时，需要规划该参数。  主备UPF引入路由的MED值。主UPF设置的MED值必须小于备UPF设置的MED值。'
          data_source: '本端规划'
          pattern: ''
          default: 0
  examples:
    add_l3vpninst_list:
    - VRFNAME: 'VPN_Access'
    add_vpninstaf_list:
    - VRFNAME: 'VPN_Access'
      AFTYPE: ipv6uni
    mod_interface_list:
    - IFNAME: 'Ethernet64/0/4'
      IFADMINSTATUS: up
    add_interface_list:
    - IFNAME: 'Ethernet64/0/4.1'
    add_ipbindvpn_list:
    - IFNAME: 'Ethernet64/0/4.1'
      VRFNAME: 'VPN_Access'
    add_ethsubif_list:
    - IFNAME: 'Ethernet64/0/4.1'
      VLANTYPEVID: 100
    set_ifipv6enable_list:
    - IFNAME: 'Ethernet64/0/4.1'
      ENABLEFLAG: TRUE
    add_ifipv6address_list:
    - IFNAME: 'Ethernet64/0/4.1'
      IPV6ADDRESS: 'FC00::10C2'
      PREFIXLEN: 123
    mod_interface_list_2:
    - IFNAME: 'Ethernet64/0/4'
      IFADMINSTATUS: up
    add_interface_list_2:
    - IFNAME: 'Eth-trunk1'
    mod_trunkif_list:
    - IFNAME: 'Eth-Trunk1'
      WORKMODE: Manual
    add_trunkmember_list:
    - TRUNKIFNAME: 'Eth-trunk1'
      MEMBERIFNAME: 'Ethernet64/0/4'
    add_interface_list_3:
    - IFNAME: 'Eth-trunk1.1'
    add_ipbindvpn_list_2:
    - IFNAME: 'Eth-trunk1.1'
      VRFNAME: 'VPN_Access'
    add_ethsubif_list_2:
    - IFNAME: 'Eth-trunk1.1'
      VLANTYPEVID: 100
    set_ifipv6enable_list_2:
    - IFNAME: 'Eth-trunk1.1'
      ENABLEFLAG: TRUE
    add_ifipv6address_list_2:
    - IFNAME: 'Eth-trunk1.1'
      IPV6ADDRESS: 'FC00::10C2'
      PREFIXLEN: 123
    set_bfd_list:
    - BFDENABLE: TRUE
    add_bfdsession_list:
    - SESSNAME: 'BfdName21'
      ADDRTYPE: IPv6
      CREATETYPE6: SESS_STATIC
      ONEARMECHO6: FALSE
      LINKTYPE: IP
      VRFNAME: 'VPN_Access'
      LOCALDISCR: 121
      REMOTEDISCR: 221
      IFNAME: 'Ethernet64/0/4.1'
      DESTADDR6: 'FC00::10C1'
      CREATETYPE4: ''
      ONEARMECHO: ''
    add_bfdsession_list_2:
    - SESSNAME: 'BfdName21'
      ADDRTYPE: IPv6
      CREATETYPE6: SESS_STATIC
      ONEARMECHO6: TRUE
      LINKTYPE: IP
      VRFNAME: 'VPN_Access'
      LOCALDISCR: 121
      IFNAME: 'Eth-trunk1.1'
      DESTADDR6: 'FC00::10C1'
      CREATETYPE4: ''
      ONEARMECHO: ''
    add_srroute6_list:
    - VRFNAME: 'VPN_Access'
      AFTYPE: ipv6unicast
      PREFIX: 'FC00:2013::2'
      MASKLENGTH: 128
      DESTVRFNAME: 'VPN_Access'
      NEXTHOP: 'FC00::10C1'
      IFNAME: 'Ethernet64/0/4.1'
      SESSIONNAME: 'BfdName21'
    add_srroute6_list_2:
    - VRFNAME: 'VPN_Access'
      AFTYPE: ipv6unicast
      PREFIX: 'FC00:2013::2'
      MASKLENGTH: 128
      DESTVRFNAME: 'VPN_Access'
      NEXTHOP: 'FC00::10C1'
      IFNAME: 'Eth-trunk1.1'
      SESSIONNAME: 'BfdName21'
    add_interface_list_4:
    - IFNAME: 'Loopback1'
    add_ipbindvpn_list_3:
    - IFNAME: 'Loopback1'
      VRFNAME: 'VPN_Access'
    set_ifipv6enable_list_3:
    - IFNAME: 'Loopback1'
      ENABLEFLAG: TRUE
    add_ifipv6address_list_3:
    - IFNAME: 'Loopback1'
      IPV6ADDRESS: 'FC00:2013::1'
      PREFIXLEN: 128
    set_bgp_list:
    - BGPENABLE: TRUE
      ASNUM: '60001'
    add_bgpvrf_list:
    - VRFNAME: 'VPN_Access'
      DEFAULTAFTYPE: noaf
      ROUTERID: '10.90.7.160'
    add_bgpvrfaf_list:
    - VRFNAME: 'VPN_Access'
      AFTYPE: ipv6uni
      MAXIMUMLOADBALANCE: 2
    add_bgppeer_list:
    - VRFNAME: 'VPN_Access'
      ADDRESSTYPE: ipv6
      PEERADDRV6: 'FC00:2013::2'
      REMOTEAS: '60002'
      LOCALIFADDR: 'FC00:2013::1'
      LOCALIFNAME: 'Loopback1'
      EBGPMAXHOP: 10
    add_bgppeer_list_2:
    - VRFNAME: 'VPN_Access'
      ADDRESSTYPE: ipv6
      PEERADDRV6: 'FC00:2013::2'
      REMOTEAS: '60002'
      LOCALIFADDR: 'FC00:2013::1'
      LOCALIFNAME: 'Loopback1'
      EBGPMAXHOP: 10
    add_importroute_list:
    - VRFNAME: 'VPN_Access'
      AFTYPE: ipv6uni
      IMPORTPROTOCOL: wlr
      MEDENABLE: FALSE
      MED: 0
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
    ;
{%- endfor -%}
```

### 一条通信路径上所有节点绑定的VPN实例要一致，才能正常通信，例如VNF逻辑接口、VNF外联口、网关上的VPN，否则从逻辑接口发出去的报文会查询路由失败。

### 2 非SR-IOV bonding组网时，配置外联口IP地址。SR-IOV bonding组网时，请跳转到3。

#### 2.1 查看接口状态及信息。

#### 2.2 配置主接口的管理状态为up。

```jinja2
{%- if is_scenario_non_sriov_bonding -%}
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

#### 2.3 配置以太网子接口。

```jinja2
{%- if is_scenario_non_sriov_bonding -%}
    {%- for item in add_interface_list -%}
        ADD INTERFACE:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 2.4 增加接口绑定VPN。

```jinja2
{%- if is_scenario_non_sriov_bonding -%}
    {%- for item in add_ipbindvpn_list -%}
        ADD IPBINDVPN:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        VRFNAME="{{item.VRFNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 2.5 在以太网子接口上关联VLAN ID。

```jinja2
{%- if is_scenario_non_sriov_bonding -%}
    {%- for item in add_ethsubif_list -%}
        ADD ETHSUBIF:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        VLANTYPEVID={{item.VLANTYPEVID}},
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 子接口配置了VLAN，则需要在交换机、对接网关上调整VLAN的配置。

#### 2.6 配置IPv6使能。

```jinja2
{%- if is_scenario_non_sriov_bonding -%}
    {%- for item in set_ifipv6enable_list -%}
        SET IFIPV6ENABLE:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        ENABLEFLAG={{item.ENABLEFLAG}},
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 2.7 配置外联口的IP地址。

```jinja2
{%- if is_scenario_non_sriov_bonding -%}
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

#### 如果规划外联口使用IPv4v6双栈地址，则分别执行**ADD IFIPV4ADDRESS**和**ADD IFIPV6ADDRESS**对同一外联口配置IPv4和IPv6地址。

### 3 SR-IOV bonding组网时，配置外联口IP地址。

#### 3.1 查看接口状态及信息。

#### 3.2 配置主接口的管理状态为up。

```jinja2
{%- if is_scenario_sriov_bonding -%}
    {%- for item in mod_interface_list_2 -%}
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

#### 3.3 配置以太Trunk接口。

```jinja2
{%- if is_scenario_sriov_bonding -%}
    {%- for item in add_interface_list_2 -%}
        ADD INTERFACE:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 3.4 配置Eth-trunk接口的工作模式并添加成员端口。

```jinja2
{%- if is_scenario_sriov_bonding -%}
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
{%- if is_scenario_sriov_bonding -%}
    {%- for item in add_trunkmember_list -%}
        ADD TRUNKMEMBER:
        {#- --- 必选参数 --- -#}
        TRUNKIFNAME="{{item.TRUNKIFNAME}}",
        MEMBERIFNAME="{{item.MEMBERIFNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 3.5 配置以太Trunk子接口。

```jinja2
{%- if is_scenario_sriov_bonding -%}
    {%- for item in add_interface_list_3 -%}
        ADD INTERFACE:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 3.6 增加接口绑定VPN。

```jinja2
{%- if is_scenario_sriov_bonding -%}
    {%- for item in add_ipbindvpn_list_2 -%}
        ADD IPBINDVPN:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        VRFNAME="{{item.VRFNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 3.7 在以太网子接口上关联VLAN ID。

```jinja2
{%- if is_scenario_sriov_bonding -%}
    {%- for item in add_ethsubif_list_2 -%}
        ADD ETHSUBIF:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        VLANTYPEVID={{item.VLANTYPEVID}},
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 子接口配置了VLAN，则需要在交换机、对接网关上调整VLAN的配置。

#### 3.8 配置IPv6使能。

```jinja2
{%- if is_scenario_sriov_bonding -%}
    {%- for item in set_ifipv6enable_list_2 -%}
        SET IFIPV6ENABLE:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        ENABLEFLAG={{item.ENABLEFLAG}},
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 3.9 配置外联口的IP地址。

```jinja2
{%- if is_scenario_sriov_bonding -%}
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

#### 如果规划外联口使用IPv4v6双栈地址，则分别执行**ADD IFIPV4ADDRESS**和**ADD IFIPV6ADDRESS**对同一外联口配置IPv4和IPv6地址。

### 4 全局激活BFD。

```jinja2
{%- for item in set_bfd_list -%}
    SET BFD:
    {#- --- 必选参数 --- -#}
    BFDENABLE={{item.BFDENABLE}},
    ;
{%- endfor -%}
```

### 参数“DELAYUPTIMER”（会话延迟UP时间）和“TOSEXP”（动态会话报文优先级）可以不用配置，使用默认值即可。

### 5 新建BFD会话。

#### 5.1 必须全局使能BFD功能后该命令才可生效。

#### 5.2 非SR-IOV bonding组网场景下：

```jinja2
{%- if is_scenario_non_sriov_bonding -%}
    {%- for item in add_bfdsession_list -%}
        ADD BFDSESSION:
        {#- --- 必选参数 --- -#}
        SESSNAME="{{item.SESSNAME}}",
        ADDRTYPE={{item.ADDRTYPE}},
        LINKTYPE={{item.LINKTYPE}},
        {#- --- 可选参数 --- -#}
        {%- if item.VRFNAME is not none -%}
            VRFNAME="{{item.VRFNAME}}",
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：ADDRTYPE=IPv6 时必选 --- -#}
        {%- if item.ADDRTYPE == 'IPv6' -%}
            CREATETYPE6={{item.CREATETYPE6}},
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
            DESTADDR6="{{item.DESTADDR6}}",
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
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

#### 5.3 SR-IOV bonding组网场景下：

```jinja2
{%- if is_scenario_sriov_bonding -%}
    {%- for item in add_bfdsession_list_2 -%}
        ADD BFDSESSION:
        {#- --- 必选参数 --- -#}
        SESSNAME="{{item.SESSNAME}}",
        ADDRTYPE={{item.ADDRTYPE}},
        LINKTYPE={{item.LINKTYPE}},
        {#- --- 可选参数 --- -#}
        {%- if item.VRFNAME is not none -%}
            VRFNAME="{{item.VRFNAME}}",
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：ADDRTYPE=IPv6 时必选 --- -#}
        {%- if item.ADDRTYPE == 'IPv6' -%}
            CREATETYPE6={{item.CREATETYPE6}},
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
            DESTADDR6="{{item.DESTADDR6}}",
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
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

### 6 配置静态路由并绑定BFD会话。

#### 6.1 非SR-IOV bonding组网场景下：

```jinja2
{%- if is_scenario_non_sriov_bonding -%}
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
        {%- if item.NEXTHOP is not none -%}
            NEXTHOP="{{item.NEXTHOP}}",
        {%- endif -%}
        {%- if item.IFNAME is not none -%}
            IFNAME="{{item.IFNAME}}",
        {%- endif -%}
        {%- if item.SESSIONNAME is not none -%}
            SESSIONNAME="{{item.SESSIONNAME}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 6.2 SR-IOV bonding组网场景下：

```jinja2
{%- if is_scenario_sriov_bonding -%}
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
        {%- if item.NEXTHOP is not none -%}
            NEXTHOP="{{item.NEXTHOP}}",
        {%- endif -%}
        {%- if item.IFNAME is not none -%}
            IFNAME="{{item.IFNAME}}",
        {%- endif -%}
        {%- if item.SESSIONNAME is not none -%}
            SESSIONNAME="{{item.SESSIONNAME}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 6.3 BFD会话绑定的是路由，不是BGPPEER。如存在**ADD BGPPEERBFD**配置，请删除。静态路由绑定静态BFD会话时，通过**ADD SRROUTE6**的“静态BFD会话名”来指定静态路由所联动的静态BFD的会话名。

#### 6.4 静态路由用于实现VNF 的Loopback接口地址与BGP PEER IP（DC-GW）之间的互通。

#### 6.5 本步骤配置的是静态路由时，需要配置如下两类路由：

##### 6.5.1 IP路由1：目的IP是BGP对等体地址，下一跳是网关的接口IP地址，且该路由需要绑定BFD会话。

##### 6.5.2 IP路由2：目的IP是0:0:0:0:0:0:0:0，掩码长度是0。其他参数取值与“IP路由1”中的参数值相同。对端网元不发布默认BGP路由时需要配置。

#### 6.6 在网关侧配置到VNF的回程路由，目的地址为VNF上各逻辑接口的IP地址，下一跳为VNF上配置的各逻辑接口对应的外联口的IP地址。

#### 需要说明的是，配置VNF与DN/PDN通信的回程路由时，目的地址为UE的网段地址，下一跳为VNF上外联口的IP地址。

### 7 配置Loopback接口地址。

#### 7.1 配置Loopback接口。

```jinja2
{%- for item in add_interface_list_4 -%}
    ADD INTERFACE:
    {#- --- 必选参数 --- -#}
    IFNAME="{{item.IFNAME}}",
    ;
{%- endfor -%}
```

#### 7.2 配置接口绑定VPN。

```jinja2
{%- for item in add_ipbindvpn_list_3 -%}
    ADD IPBINDVPN:
    {#- --- 必选参数 --- -#}
    IFNAME="{{item.IFNAME}}",
    VRFNAME="{{item.VRFNAME}}",
    ;
{%- endfor -%}
```

#### 7.3 配置IPv6使能。

```jinja2
{%- for item in set_ifipv6enable_list_3 -%}
    SET IFIPV6ENABLE:
    {#- --- 必选参数 --- -#}
    IFNAME="{{item.IFNAME}}",
    ENABLEFLAG={{item.ENABLEFLAG}},
    ;
{%- endfor -%}
```

#### 7.4 配置接口IP地址。

```jinja2
{%- for item in add_ifipv6address_list_3 -%}
    ADD IFIPV6ADDRESS:
    {#- --- 必选参数 --- -#}
    IFNAME="{{item.IFNAME}}",
    IPV6ADDRESS="{{item.IPV6ADDRESS}}",
    PREFIXLEN={{item.PREFIXLEN}},
    ;
{%- endfor -%}
```

### 8 全局激活BGP。

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

### 9 配置BGP。

#### 9.1 增加BGP VPN实例。

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

##### 9.1.1 此处配置的“ROUTERID”是BGP VPN实例级别的ROUTERID。

##### IPv4v6双栈时，IPv4 BGP VPN实例地址族和IPv6 BGP VPN实例地址族共用此处配置的“ROUTERID”值。

##### 9.1.2 已配置IPv4v6双栈的BGP VPN实例地址族，若需删除IPv4的BGP VPN实例地址族配置，则：

##### 1、删除IPv4的配置前需查询并记录“ROUTERID”值。

##### 2、删除IPv4的配置后需查询“ROUTERID”值是否存在，若不存在则需通过**MOD BGPVRF**命令将“ROUTERID”参数设置为删除IPv4的配置前记录的“ROUTERID”值。否则IPv6 BGP重新协商时会因无“ROUTERID”值可用而导致协商失败。

#### 9.2 增加BGP VPN地址族。

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

##### 9.2.1 SR-IOV bonding场景（直连DCGW）或SR-IOV双平面场景（直连PE）场景，UEG对接2个负荷分担的路由设备，“MAXIMUMLOADBALANCE”设置为“2”。

##### 9.2.2 SR-IOV bonding场景（直连PE），UEG对接1个路由设备，“MAXIMUMLOADBALANCE”设置为“1”。

#### 9.3 增加BGP对等体。

##### 9.3.1 SR-IOV bonding场景（直连DCGW）或SR-IOV双平面场景（直连PE）场景：

```jinja2
{%- if is_scenario_sriov_bonding_dcgw_or_dualplane_pe -%}
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
{%- endif -%}
```

##### 9.3.2 SR-IOV bonding场景（直连PE）：

```jinja2
{%- if is_scenario_sriov_bonding_pe -%}
    {%- for item in add_bgppeer_list_2 -%}
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
{%- endif -%}
```

#### 9.4 增加BGP引入路由。

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
    {#- --- 条件必选：MEDENABLE=TRUE 时必选 --- -#}
    {%- if item.MEDENABLE == 'TRUE' -%}
        MED={{item.MED}},
    {%- endif -%}
    ;
{%- endfor -%}
```

##### 9.4.1 由于BGP协议自身不能发现路由，所以需要引入其他协议的路由（如静态路由或WLR等）注入到BGP路由表中，从而将这些路由在AS之内和AS之间传播。

##### 9.4.2 对于N6口，两个UPF上的UE地址段存在重叠且需要对外发布网段路由时，需要将“MEDENABLE”设置为“TRUE”，并设置备UPF的“MED”值大于主UPF的“MED”值。


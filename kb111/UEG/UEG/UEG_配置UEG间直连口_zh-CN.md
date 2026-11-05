---
id: ''
name: 配置UEG间直连口
ne_type: UEG
type: feature
description: 本章节适用于UEG裸机设备直连PE，UEG之间存在直连物理口对接的组网场景。两个UEG之间使用OSPF协议对接。  本章节配置的UEG间直连口，用于传输激活在另一UEG上的用户业务报文（与企业园区服务器/App交互的报文除外），如图1所示。  **图1** UEG间直连口传输用户业务报文示意
tags: []
risk_level: ''
doc_source: ["网络部署","园区入驻式（仅连接）","5GC toB 部署边缘站点（站点为“风筝S”，入驻式）","裸机容器模式","UEG初始配置（风筝S）","配置实例(刀片式服务器2U)","配置UEG间直连口"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
本章节适用于UEG裸机设备直连PE，UEG之间存在直连物理口对接的组网场景。两个UEG之间使用OSPF协议对接。本章节配置的UEG间直连口，用于传输激活在另一UEG上的用户业务报文（与企业园区服务器/App交互的报文除外），如图1所示。**图1** UEG间直连口传输用户业务报文示意

## 必备事项
前提条件

* 必须是UEG 21.10.0及后续版本。
* UEG间直连口已通过光纤连接。
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
        DELAYUPTIMER:
          name: '会话延迟Up时间（s）'
          type: integer
          minimum: 0
          maximum: 600
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
        MINRXRECVINTV:
          name: '接收BFD包的最小时间间隔（ms）'
          type: integer
          minimum: 30
          maximum: 1000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MINTXTRANINTV:
          name: '发送BFD包的最小时间间隔（ms）'
          type: integer
          minimum: 30
          maximum: 1000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DETECTMULINTV:
          name: '本地检测倍数'
          type: integer
          minimum: 3
          maximum: 50
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 3
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
        MINRXRECVINTV:
          name: '接收BFD包的最小时间间隔（ms）'
          type: integer
          minimum: 30
          maximum: 1000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MINTXTRANINTV:
          name: '发送BFD包的最小时间间隔（ms）'
          type: integer
          minimum: 30
          maximum: 1000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DETECTMULINTV:
          name: '本地检测倍数'
          type: integer
          minimum: 3
          maximum: 50
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 3
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
    add_ospfv3defaultroute_list:
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
    add_ethsubif_list_1:
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
    add_ospf_list_1:
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
    add_ospfarea_list_1:
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
    add_ospfinterface_list_1:
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
        MINRXRECVINTV:
          name: '接收BFD包的最小时间间隔（ms）'
          type: integer
          minimum: 30
          maximum: 1000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MINTXTRANINTV:
          name: '发送BFD包的最小时间间隔（ms）'
          type: integer
          minimum: 30
          maximum: 1000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DETECTMULINTV:
          name: '本地检测倍数'
          type: integer
          minimum: 3
          maximum: 50
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 3
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
    add_ospfimportroute_list_2:
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
    add_ospfdefaultroute_list_1:
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
    add_ospfv3_list_1:
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
    add_ospfv3area_list_1:
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
    add_ospfv3interface_list_1:
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
        MINRXRECVINTV:
          name: '接收BFD包的最小时间间隔（ms）'
          type: integer
          minimum: 30
          maximum: 1000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MINTXTRANINTV:
          name: '发送BFD包的最小时间间隔（ms）'
          type: integer
          minimum: 30
          maximum: 1000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DETECTMULINTV:
          name: '本地检测倍数'
          type: integer
          minimum: 3
          maximum: 50
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 3
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
    add_ospfv3importroute_list_2:
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
    add_ospfv3defaultroute_list_1:
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
    add_interface_list_3:
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
    add_ospf_list_2:
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
    add_ospfarea_list_2:
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
    add_ospfinterface_list_2:
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
        MINRXRECVINTV:
          name: '接收BFD包的最小时间间隔（ms）'
          type: integer
          minimum: 30
          maximum: 1000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MINTXTRANINTV:
          name: '发送BFD包的最小时间间隔（ms）'
          type: integer
          minimum: 30
          maximum: 1000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DETECTMULINTV:
          name: '本地检测倍数'
          type: integer
          minimum: 3
          maximum: 50
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 3
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
    add_ospfimportroute_list_4:
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
    add_ospfdefaultroute_list_2:
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
    add_ospfv3_list_2:
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
    add_ospfv3area_list_2:
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
    add_ospfv3interface_list_2:
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
        MINRXRECVINTV:
          name: '接收BFD包的最小时间间隔（ms）'
          type: integer
          minimum: 30
          maximum: 1000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MINTXTRANINTV:
          name: '发送BFD包的最小时间间隔（ms）'
          type: integer
          minimum: 30
          maximum: 1000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DETECTMULINTV:
          name: '本地检测倍数'
          type: integer
          minimum: 3
          maximum: 50
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 3
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
    add_ospfv3importroute_list_4:
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
    add_ospfv3defaultroute_list_2:
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
  examples:
    set_bfd_list:
    - BFDENABLE: TRUE
      DELAYUPTIMER: 60
    mod_interface_list:
    - IFNAME: 'Ethernet64/0/4'
      IFADMINSTATUS: up
    add_interface_list:
    - IFNAME: 'Eth-trunk1'
    - IFNAME: 'Eth-trunk1.2050'
    mod_trunkif_list:
    - IFNAME: 'Eth-Trunk1'
      WORKMODE: Manual
    add_trunkmember_list:
    - TRUNKIFNAME: 'Eth-trunk1'
      MEMBERIFNAME: 'Ethernet64/0/4'
    add_ipbindvpn_list:
    - IFNAME: 'Eth-trunk1.2050'
      VRFNAME: 'VRF_Access'
    add_ethsubif_list:
    - IFNAME: 'Eth-trunk1.2050'
      VLANTYPEVID: 2050
    set_ifipv6enable_list:
    - IFNAME: 'Eth-trunk1.2050'
      ENABLEFLAG: TRUE
    add_ifipv4address_list:
    - IFNAME: 'Eth-trunk1.2050'
      IFIPADDR: '192.168.150.2'
      SUBNETMASK: '255.255.255.248'
    add_ifipv6address_list:
    - IFNAME: 'Eth-trunk1.2050'
      IPV6ADDRESS: 'FC00::150:2'
      PREFIXLEN: 125
    add_ospf_list:
    - PROCID: 100
      VRFNAME: 'VRF_Access'
      SCHEMAROUID: '192.168.225.150'
      BFDALLINTFFLG: FALSE
      LSAARRINTVFLAG: FALSE
      LSAARRMAXINTV: 1000
      LSAARRSTARINTV: 500
      LSAARRHLDINTV: 500
      VPNINSCAPSIMFLG: TRUE
      VIRTUALSYSFLAG: FALSE
    add_ospfarea_list:
    - PROCID: 100
      AREAID: '0.0.0.5'
      AREATYPE: Normal
      MAXCOSTFLAG: FALSE
    add_ospfinterface_list:
    - PROCID: 100
      AREAID: '0.0.0.5'
      IFNAME: 'Eth-trunk1.2050'
      VIRTUALSYSFLAG: FALSE
      BFDENABLE: TRUE
      MINRXRECVINTV: 1000
      MINTXTRANINTV: 1000
      DETECTMULINTV: 5
      CFGROUTERIDFLAG: FALSE
      MAXCOSTFLAG: FALSE
    add_ospfimportroute_list:
    - PROCID: 100
      TOPOID: 0
      PROTOCOL: Static
      IMPTCOSTCFG: FALSE
      IMPTTAGCFG: FALSE
      IMPTTYPECFG: FALSE
    add_ospfdefaultroute_list:
    - PROCID: 100
      TOPOID: 0
    add_ospfv3_list:
    - PROCID: 100
      VRFNAME: 'VRF_Access'
      ROUTERID: '192.168.225.150'
      BFDALLINTFFLG: FALSE
      VPNINSCAPSIMFLG: TRUE
      VIRTUALSYSFLAG: FALSE
    add_ospfv3area_list:
    - PROCID: 100
      AREAID: '0.0.0.5'
      AREATYPE: Normal
    add_ospfv3interface_list:
    - PROCID: 100
      AREAID: '0.0.0.5'
      IFNAME: 'Eth-trunk1.2050'
      VIRTUALSYSFLAG: FALSE
      BFDENABLE: TRUE
      MINRXRECVINTV: 1000
      MINTXTRANINTV: 1000
      DETECTMULINTV: 5
      CFGROUTERIDFLAG: FALSE
    add_ospfv3importroute_list:
    - PROCID: 100
      TOPOID: 0
      PROTOCOL: Static
      IMPTCOSTCFG: FALSE
      IMPTTAGCFG: FALSE
      IMPTTYPECFG: FALSE
    add_ospfv3defaultroute_list:
    - PROCID: 100
      TOPOID: 0
    add_interface_list_2:
    - IFNAME: 'Eth-trunk1.2051'
    add_ipbindvpn_list_1:
    - IFNAME: 'Eth-trunk1.2051'
      VRFNAME: 'VRF_CN'
    add_ethsubif_list_1:
    - IFNAME: 'Eth-trunk1.2051'
      VLANTYPEVID: 2051
    set_ifipv6enable_list_1:
    - IFNAME: 'Eth-trunk1.2051'
      ENABLEFLAG: TRUE
    add_ifipv4address_list_1:
    - IFNAME: 'Eth-trunk1.2051'
      IFIPADDR: '192.168.151.2'
      SUBNETMASK: '255.255.255.248'
    add_ifipv6address_list_1:
    - IFNAME: 'Eth-trunk1.2051'
      IPV6ADDRESS: 'FC00::151:2'
      PREFIXLEN: 125
    add_ospf_list_1:
    - PROCID: 110
      VRFNAME: 'VRF_CN'
      SCHEMAROUID: '192.168.225.151'
      BFDALLINTFFLG: FALSE
      LSAARRINTVFLAG: FALSE
      LSAARRMAXINTV: 1000
      LSAARRSTARINTV: 500
      LSAARRHLDINTV: 500
      VPNINSCAPSIMFLG: TRUE
      VIRTUALSYSFLAG: FALSE
    add_ospfarea_list_1:
    - PROCID: 110
      AREAID: '0.0.0.5'
      AREATYPE: Normal
      MAXCOSTFLAG: FALSE
    add_ospfinterface_list_1:
    - PROCID: 110
      AREAID: '0.0.0.5'
      IFNAME: 'Eth-trunk1.2051'
      VIRTUALSYSFLAG: FALSE
      BFDENABLE: TRUE
      MINRXRECVINTV: 1000
      MINTXTRANINTV: 1000
      DETECTMULINTV: 5
      CFGROUTERIDFLAG: FALSE
      MAXCOSTFLAG: FALSE
    add_ospfimportroute_list_2:
    - PROCID: 110
      TOPOID: 0
      PROTOCOL: Static
      IMPTCOSTCFG: FALSE
      IMPTTAGCFG: FALSE
      IMPTTYPECFG: FALSE
    add_ospfdefaultroute_list_1:
    - PROCID: 110
      TOPOID: 0
    add_ospfv3_list_1:
    - PROCID: 110
      VRFNAME: 'VRF_CN'
      ROUTERID: '192.168.225.151'
      BFDALLINTFFLG: FALSE
      VPNINSCAPSIMFLG: TRUE
      VIRTUALSYSFLAG: FALSE
    add_ospfv3area_list_1:
    - PROCID: 110
      AREAID: '0.0.0.5'
      AREATYPE: Normal
    add_ospfv3interface_list_1:
    - PROCID: 110
      AREAID: '0.0.0.5'
      IFNAME: 'Eth-trunk1.2051'
      VIRTUALSYSFLAG: FALSE
      BFDENABLE: TRUE
      MINRXRECVINTV: 1000
      MINTXTRANINTV: 1000
      DETECTMULINTV: 5
      CFGROUTERIDFLAG: FALSE
    add_ospfv3importroute_list_2:
    - PROCID: 110
      TOPOID: 0
      PROTOCOL: Static
      IMPTCOSTCFG: FALSE
      IMPTTAGCFG: FALSE
      IMPTTYPECFG: FALSE
    add_ospfv3defaultroute_list_1:
    - PROCID: 110
      TOPOID: 0
    add_interface_list_3:
    - IFNAME: 'Eth-trunk1.2052'
    add_ipbindvpn_list_2:
    - IFNAME: 'Eth-trunk1.2052'
      VRFNAME: 'VRF_Pa'
    add_ethsubif_list_2:
    - IFNAME: 'Eth-trunk1.2052'
      VLANTYPEVID: 2052
    set_ifipv6enable_list_2:
    - IFNAME: 'Eth-trunk1.2052'
      ENABLEFLAG: TRUE
    add_ifipv4address_list_2:
    - IFNAME: 'Eth-trunk1.2052'
      IFIPADDR: '192.168.152.2'
      SUBNETMASK: '255.255.255.248'
    add_ifipv6address_list_2:
    - IFNAME: 'Eth-trunk1.2052'
      IPV6ADDRESS: 'FC00::152:2'
      PREFIXLEN: 125
    add_ospf_list_2:
    - PROCID: 120
      VRFNAME: 'VRF_Pa'
      SCHEMAROUID: '192.168.225.152'
      BFDALLINTFFLG: FALSE
      LSAARRINTVFLAG: FALSE
      LSAARRMAXINTV: 1000
      LSAARRSTARINTV: 500
      LSAARRHLDINTV: 500
      VPNINSCAPSIMFLG: TRUE
      VIRTUALSYSFLAG: FALSE
    add_ospfarea_list_2:
    - PROCID: 120
      AREAID: '0.0.0.5'
      AREATYPE: Normal
      MAXCOSTFLAG: FALSE
    add_ospfinterface_list_2:
    - PROCID: 120
      AREAID: '0.0.0.5'
      IFNAME: 'Eth-trunk1.2052'
      VIRTUALSYSFLAG: FALSE
      BFDENABLE: TRUE
      MINRXRECVINTV: 1000
      MINTXTRANINTV: 1000
      DETECTMULINTV: 5
      CFGROUTERIDFLAG: FALSE
      MAXCOSTFLAG: FALSE
    add_ospfimportroute_list_4:
    - PROCID: 120
      TOPOID: 0
      PROTOCOL: Static
      IMPTCOSTCFG: FALSE
      IMPTTAGCFG: FALSE
      IMPTTYPECFG: FALSE
    add_ospfdefaultroute_list_2:
    - PROCID: 120
      TOPOID: 0
    add_ospfv3_list_2:
    - PROCID: 120
      VRFNAME: 'VRF_Pa'
      ROUTERID: '192.168.225.152'
      BFDALLINTFFLG: FALSE
      VPNINSCAPSIMFLG: TRUE
      VIRTUALSYSFLAG: FALSE
    add_ospfv3area_list_2:
    - PROCID: 120
      AREAID: '0.0.0.5'
      AREATYPE: Normal
    add_ospfv3interface_list_2:
    - PROCID: 120
      AREAID: '0.0.0.5'
      IFNAME: 'Eth-trunk1.2052'
      VIRTUALSYSFLAG: FALSE
      BFDENABLE: TRUE
      MINRXRECVINTV: 1000
      MINTXTRANINTV: 1000
      DETECTMULINTV: 5
      CFGROUTERIDFLAG: FALSE
    add_ospfv3importroute_list_4:
    - PROCID: 120
      TOPOID: 0
      PROTOCOL: Static
      IMPTCOSTCFG: FALSE
      IMPTTAGCFG: FALSE
      IMPTTYPECFG: FALSE
    add_ospfv3defaultroute_list_2:
    - PROCID: 120
      TOPOID: 0
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 UEG和PE之间使用静态路由+BFD(auto)方案对接时，在UEG上配置全局BFD的“会话延迟Up时间（DELAYUPTIMER）”。若UEG与PE使用静态路由+BFD(echo)方案对接，则需要在PE上配置BFD会话延迟Up时间。

```jinja2
{%- if is_scenario_static_route_bfd_auto -%}
    {%- for item in set_bfd_list -%}
        SET BFD:
        {#- --- 必选参数 --- -#}
        BFDENABLE={{item.BFDENABLE}},
        {#- --- 可选参数 --- -#}
        {%- if item.DELAYUPTIMER is not none -%}
            DELAYUPTIMER={{item.DELAYUPTIMER}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 2 配置UEG间的IP路由数据，用于传输激活在另一UEG上的用户的N3业务报文。

#### 2.1 配置外联口IP地址。

##### 2.1.1 查询接口名，确认可使用的外联口的接口类型和接口编号。

##### 2.1.2 配置主接口的管理状态为up。将网设规划的接口的管理状态设置为up。

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

##### 2.1.3 添加Eth-trunk接口及Eth-trunk子接口。成员端口数量以网设规划的为准。

###### 2.1.3.1 //添加Eth-trunk接口及成员接口。如已配置，则不需要重复配置。

```jinja2
{%- for item in add_interface_list -%}
    ADD INTERFACE:
    {#- --- 必选参数 --- -#}
    IFNAME="{{item.IFNAME}}",
    ;
{%- endfor -%}
```

```jinja2
{%- for item in mod_trunkif_list -%}
    MOD TRUNKIF:
    {#- --- 必选参数 --- -#}
    IFNAME="{{item.IFNAME}}",
    WORKMODE={{item.WORKMODE}},
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

##### 2.1.4 增加接口绑定VPN。

```jinja2
{%- for item in add_ipbindvpn_list -%}
    ADD IPBINDVPN:
    {#- --- 必选参数 --- -#}
    IFNAME="{{item.IFNAME}}",
    VRFNAME="{{item.VRFNAME}}",
    ;
{%- endfor -%}
```

##### 2.1.5 在以太网子接口上关联VLAN ID。

```jinja2
{%- for item in add_ethsubif_list -%}
    ADD ETHSUBIF:
    {#- --- 必选参数 --- -#}
    IFNAME="{{item.IFNAME}}",
    VLANTYPEVID={{item.VLANTYPEVID}},
    ;
{%- endfor -%}
```

##### 2.1.6 配置IPv6使能。

```jinja2
{%- for item in set_ifipv6enable_list -%}
    SET IFIPV6ENABLE:
    {#- --- 必选参数 --- -#}
    IFNAME="{{item.IFNAME}}",
    ENABLEFLAG={{item.ENABLEFLAG}},
    ;
{%- endfor -%}
```

##### 2.1.7 配置外联口IP地址。

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

#### 2.2 配置OSPF路由数据。该步骤适用于IPv4组网或IPv4v6双栈组网。

##### 2.2.1 创建OSPF进程。

```jinja2
{%- if is_scenario_ipv4 -%}
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

##### 2.2.2 增加OSPF区域。

```jinja2
{%- if is_scenario_ipv4 -%}
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

##### 2.2.3 配置OSPF协议的接口属性。

```jinja2
{%- if is_scenario_ipv4 -%}
    {%- for item in add_ospfinterface_list -%}
        ADD OSPFINTERFACE:
        {#- --- 必选参数 --- -#}
        PROCID={{item.PROCID}},
        AREAID="{{item.AREAID}}",
        IFNAME="{{item.IFNAME}}",
        {#- --- 可选参数 --- -#}
        {%- if item.VIRTUALSYSFLAG is not none -%}
            VIRTUALSYSFLAG={{item.VIRTUALSYSFLAG}},
        {%- endif -%}
        {%- if item.BFDENABLE is not none -%}
            BFDENABLE={{item.BFDENABLE}},
        {%- endif -%}
        {%- if item.MINRXRECVINTV is not none -%}
            MINRXRECVINTV={{item.MINRXRECVINTV}},
        {%- endif -%}
        {%- if item.MINTXTRANINTV is not none -%}
            MINTXTRANINTV={{item.MINTXTRANINTV}},
        {%- endif -%}
        {%- if item.DETECTMULINTV is not none -%}
            DETECTMULINTV={{item.DETECTMULINTV}},
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

##### 2.2.4 设置OSPF引入的路由类型。

```jinja2
{%- if is_scenario_ipv4 -%}
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

```jinja2
{%- if is_scenario_ipv4 -%}
    {%- for item in add_ospfdefaultroute_list -%}
        ADD OSPFDEFAULTROUTE:
        {#- --- 必选参数 --- -#}
        PROCID={{item.PROCID}},
        {#- --- 可选参数 --- -#}
        {%- if item.TOPOID is not none -%}
            TOPOID={{item.TOPOID}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 2.3 配置OSPFv3路由数据。该步骤适用于IPv6组网或IPv4v6双栈组网。

##### 2.3.1 创建OSPFv3进程。

```jinja2
{%- if is_scenario_ipv6 -%}
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

##### 2.3.2 增加OSPFv3区域。

```jinja2
{%- if is_scenario_ipv6 -%}
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

##### 2.3.3 配置OSPFv3协议的接口属性。

```jinja2
{%- if is_scenario_ipv6 -%}
    {%- for item in add_ospfv3interface_list -%}
        ADD OSPFV3INTERFACE:
        {#- --- 必选参数 --- -#}
        PROCID={{item.PROCID}},
        AREAID="{{item.AREAID}}",
        IFNAME="{{item.IFNAME}}",
        {#- --- 可选参数 --- -#}
        {%- if item.VIRTUALSYSFLAG is not none -%}
            VIRTUALSYSFLAG={{item.VIRTUALSYSFLAG}},
        {%- endif -%}
        {%- if item.BFDENABLE is not none -%}
            BFDENABLE={{item.BFDENABLE}},
        {%- endif -%}
        {%- if item.MINRXRECVINTV is not none -%}
            MINRXRECVINTV={{item.MINRXRECVINTV}},
        {%- endif -%}
        {%- if item.MINTXTRANINTV is not none -%}
            MINTXTRANINTV={{item.MINTXTRANINTV}},
        {%- endif -%}
        {%- if item.DETECTMULINTV is not none -%}
            DETECTMULINTV={{item.DETECTMULINTV}},
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

##### 2.3.4 设置OSPFv3引入的路由类型。

```jinja2
{%- if is_scenario_ipv6 -%}
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

```jinja2
{%- if is_scenario_ipv6 -%}
    {%- for item in add_ospfv3defaultroute_list -%}
        ADD OSPFV3DEFAULTROUTE:
        {#- --- 必选参数 --- -#}
        PROCID={{item.PROCID}},
        {#- --- 可选参数 --- -#}
        {%- if item.TOPOID is not none -%}
            TOPOID={{item.TOPOID}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 3 （风筝S）配置UEG间的IP路由数据，用于传输激活在另一UEG上的用户的N4业务报文。

#### 3.1 配置外联口IP地址。

##### 3.1.1 添加Eth-trunk子接口。

```jinja2
{%- if is_scenario_kite_s -%}
    {%- for item in add_interface_list_2 -%}
        ADD INTERFACE:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 3.1.2 增加接口绑定VPN。

```jinja2
{%- if is_scenario_kite_s -%}
    {%- for item in add_ipbindvpn_list_1 -%}
        ADD IPBINDVPN:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        VRFNAME="{{item.VRFNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 3.1.3 在以太网子接口上关联VLAN ID。

```jinja2
{%- if is_scenario_kite_s -%}
    {%- for item in add_ethsubif_list_1 -%}
        ADD ETHSUBIF:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        VLANTYPEVID={{item.VLANTYPEVID}},
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 3.1.4 配置IPv6使能。

```jinja2
{%- if is_scenario_kite_s -%}
    {%- for item in set_ifipv6enable_list_1 -%}
        SET IFIPV6ENABLE:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        ENABLEFLAG={{item.ENABLEFLAG}},
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 3.1.5 配置外联口IP地址。

```jinja2
{%- if is_scenario_kite_s -%}
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
{%- if is_scenario_kite_s -%}
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

#### 3.2 配置OSPF路由数据。该步骤适用于IPv4组网或IPv4v6双栈组网。

##### 3.2.1 创建OSPF进程。

```jinja2
{%- if is_scenario_kite_s and is_scenario_ipv4 -%}
    {%- for item in add_ospf_list_1 -%}
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

##### 3.2.2 增加OSPF区域。

```jinja2
{%- if is_scenario_kite_s and is_scenario_ipv4 -%}
    {%- for item in add_ospfarea_list_1 -%}
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

##### 3.2.3 配置OSPF协议的接口属性。

```jinja2
{%- if is_scenario_kite_s and is_scenario_ipv4 -%}
    {%- for item in add_ospfinterface_list_1 -%}
        ADD OSPFINTERFACE:
        {#- --- 必选参数 --- -#}
        PROCID={{item.PROCID}},
        AREAID="{{item.AREAID}}",
        IFNAME="{{item.IFNAME}}",
        {#- --- 可选参数 --- -#}
        {%- if item.VIRTUALSYSFLAG is not none -%}
            VIRTUALSYSFLAG={{item.VIRTUALSYSFLAG}},
        {%- endif -%}
        {%- if item.BFDENABLE is not none -%}
            BFDENABLE={{item.BFDENABLE}},
        {%- endif -%}
        {%- if item.MINRXRECVINTV is not none -%}
            MINRXRECVINTV={{item.MINRXRECVINTV}},
        {%- endif -%}
        {%- if item.MINTXTRANINTV is not none -%}
            MINTXTRANINTV={{item.MINTXTRANINTV}},
        {%- endif -%}
        {%- if item.DETECTMULINTV is not none -%}
            DETECTMULINTV={{item.DETECTMULINTV}},
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

##### 3.2.4 设置OSPF引入的路由类型。

```jinja2
{%- if is_scenario_kite_s and is_scenario_ipv4 -%}
    {%- for item in add_ospfimportroute_list_2 -%}
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

```jinja2
{%- if is_scenario_kite_s and is_scenario_ipv4 -%}
    {%- for item in add_ospfdefaultroute_list_1 -%}
        ADD OSPFDEFAULTROUTE:
        {#- --- 必选参数 --- -#}
        PROCID={{item.PROCID}},
        {#- --- 可选参数 --- -#}
        {%- if item.TOPOID is not none -%}
            TOPOID={{item.TOPOID}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 3.3 配置OSPFv3路由数据。该步骤适用于IPv6组网或IPv4v6双栈组网。

##### 3.3.1 创建OSPFv3进程。

```jinja2
{%- if is_scenario_kite_s and is_scenario_ipv6 -%}
    {%- for item in add_ospfv3_list_1 -%}
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

##### 3.3.2 增加OSPFv3区域。

```jinja2
{%- if is_scenario_kite_s and is_scenario_ipv6 -%}
    {%- for item in add_ospfv3area_list_1 -%}
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

##### 3.3.3 配置OSPFv3协议的接口属性。

```jinja2
{%- if is_scenario_kite_s and is_scenario_ipv6 -%}
    {%- for item in add_ospfv3interface_list_1 -%}
        ADD OSPFV3INTERFACE:
        {#- --- 必选参数 --- -#}
        PROCID={{item.PROCID}},
        AREAID="{{item.AREAID}}",
        IFNAME="{{item.IFNAME}}",
        {#- --- 可选参数 --- -#}
        {%- if item.VIRTUALSYSFLAG is not none -%}
            VIRTUALSYSFLAG={{item.VIRTUALSYSFLAG}},
        {%- endif -%}
        {%- if item.BFDENABLE is not none -%}
            BFDENABLE={{item.BFDENABLE}},
        {%- endif -%}
        {%- if item.MINRXRECVINTV is not none -%}
            MINRXRECVINTV={{item.MINRXRECVINTV}},
        {%- endif -%}
        {%- if item.MINTXTRANINTV is not none -%}
            MINTXTRANINTV={{item.MINTXTRANINTV}},
        {%- endif -%}
        {%- if item.DETECTMULINTV is not none -%}
            DETECTMULINTV={{item.DETECTMULINTV}},
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

##### 3.3.4 设置OSPFv3引入的路由类型。

```jinja2
{%- if is_scenario_kite_s and is_scenario_ipv6 -%}
    {%- for item in add_ospfv3importroute_list_2 -%}
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

```jinja2
{%- if is_scenario_kite_s and is_scenario_ipv6 -%}
    {%- for item in add_ospfv3defaultroute_list_1 -%}
        ADD OSPFV3DEFAULTROUTE:
        {#- --- 必选参数 --- -#}
        PROCID={{item.PROCID}},
        {#- --- 可选参数 --- -#}
        {%- if item.TOPOID is not none -%}
            TOPOID={{item.TOPOID}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 4 （风筝S）配置UEG间的IP路由数据，用于传输激活在另一UEG上的用户的Pa/Sc业务报文。

#### 4.1 配置外联口IP地址。

##### 4.1.1 添加Eth-trunk子接口。

```jinja2
{%- if is_scenario_kite_s -%}
    {%- for item in add_interface_list_3 -%}
        ADD INTERFACE:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 4.1.2 增加接口绑定VPN。

```jinja2
{%- if is_scenario_kite_s -%}
    {%- for item in add_ipbindvpn_list_2 -%}
        ADD IPBINDVPN:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        VRFNAME="{{item.VRFNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 4.1.3 在以太网子接口上关联VLAN ID。

```jinja2
{%- if is_scenario_kite_s -%}
    {%- for item in add_ethsubif_list_2 -%}
        ADD ETHSUBIF:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        VLANTYPEVID={{item.VLANTYPEVID}},
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 4.1.4 配置IPv6使能。

```jinja2
{%- if is_scenario_kite_s -%}
    {%- for item in set_ifipv6enable_list_2 -%}
        SET IFIPV6ENABLE:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        ENABLEFLAG={{item.ENABLEFLAG}},
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 4.1.5 配置外联口IP地址。

```jinja2
{%- if is_scenario_kite_s -%}
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
{%- if is_scenario_kite_s -%}
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

#### 4.2 配置OSPF路由数据。该步骤适用于IPv4组网或IPv4v6双栈组网。

##### 4.2.1 创建OSPF进程。

```jinja2
{%- if is_scenario_kite_s and is_scenario_ipv4 -%}
    {%- for item in add_ospf_list_2 -%}
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

##### 4.2.2 增加OSPF区域。

```jinja2
{%- if is_scenario_kite_s and is_scenario_ipv4 -%}
    {%- for item in add_ospfarea_list_2 -%}
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

##### 4.2.3 配置OSPF协议的接口属性。

```jinja2
{%- if is_scenario_kite_s and is_scenario_ipv4 -%}
    {%- for item in add_ospfinterface_list_2 -%}
        ADD OSPFINTERFACE:
        {#- --- 必选参数 --- -#}
        PROCID={{item.PROCID}},
        AREAID="{{item.AREAID}}",
        IFNAME="{{item.IFNAME}}",
        {#- --- 可选参数 --- -#}
        {%- if item.VIRTUALSYSFLAG is not none -%}
            VIRTUALSYSFLAG={{item.VIRTUALSYSFLAG}},
        {%- endif -%}
        {%- if item.BFDENABLE is not none -%}
            BFDENABLE={{item.BFDENABLE}},
        {%- endif -%}
        {%- if item.MINRXRECVINTV is not none -%}
            MINRXRECVINTV={{item.MINRXRECVINTV}},
        {%- endif -%}
        {%- if item.MINTXTRANINTV is not none -%}
            MINTXTRANINTV={{item.MINTXTRANINTV}},
        {%- endif -%}
        {%- if item.DETECTMULINTV is not none -%}
            DETECTMULINTV={{item.DETECTMULINTV}},
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

##### 4.2.4 设置OSPF引入的路由类型。

```jinja2
{%- if is_scenario_kite_s and is_scenario_ipv4 -%}
    {%- for item in add_ospfimportroute_list_4 -%}
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

```jinja2
{%- if is_scenario_kite_s and is_scenario_ipv4 -%}
    {%- for item in add_ospfdefaultroute_list_2 -%}
        ADD OSPFDEFAULTROUTE:
        {#- --- 必选参数 --- -#}
        PROCID={{item.PROCID}},
        {#- --- 可选参数 --- -#}
        {%- if item.TOPOID is not none -%}
            TOPOID={{item.TOPOID}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 4.3 配置OSPFv3路由数据。该步骤适用于IPv6组网或IPv4v6双栈组网。

##### 4.3.1 创建OSPFv3进程。

```jinja2
{%- if is_scenario_kite_s and is_scenario_ipv6 -%}
    {%- for item in add_ospfv3_list_2 -%}
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

##### 4.3.2 增加OSPFv3区域。

```jinja2
{%- if is_scenario_kite_s and is_scenario_ipv6 -%}
    {%- for item in add_ospfv3area_list_2 -%}
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

##### 4.3.3 配置OSPFv3协议的接口属性。

```jinja2
{%- if is_scenario_kite_s and is_scenario_ipv6 -%}
    {%- for item in add_ospfv3interface_list_2 -%}
        ADD OSPFV3INTERFACE:
        {#- --- 必选参数 --- -#}
        PROCID={{item.PROCID}},
        AREAID="{{item.AREAID}}",
        IFNAME="{{item.IFNAME}}",
        {#- --- 可选参数 --- -#}
        {%- if item.VIRTUALSYSFLAG is not none -%}
            VIRTUALSYSFLAG={{item.VIRTUALSYSFLAG}},
        {%- endif -%}
        {%- if item.BFDENABLE is not none -%}
            BFDENABLE={{item.BFDENABLE}},
        {%- endif -%}
        {%- if item.MINRXRECVINTV is not none -%}
            MINRXRECVINTV={{item.MINRXRECVINTV}},
        {%- endif -%}
        {%- if item.MINTXTRANINTV is not none -%}
            MINTXTRANINTV={{item.MINTXTRANINTV}},
        {%- endif -%}
        {%- if item.DETECTMULINTV is not none -%}
            DETECTMULINTV={{item.DETECTMULINTV}},
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

##### 4.3.4 设置OSPFv3引入的路由类型。

```jinja2
{%- if is_scenario_kite_s and is_scenario_ipv6 -%}
    {%- for item in add_ospfv3importroute_list_4 -%}
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

```jinja2
{%- if is_scenario_kite_s and is_scenario_ipv6 -%}
    {%- for item in add_ospfv3defaultroute_list_2 -%}
        ADD OSPFV3DEFAULTROUTE:
        {#- --- 必选参数 --- -#}
        PROCID={{item.PROCID}},
        {#- --- 可选参数 --- -#}
        {%- if item.TOPOID is not none -%}
            TOPOID={{item.TOPOID}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```


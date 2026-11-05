---
id: ''
name: 配置动态路由OSPFv3+BFD组网（IPv6）
ne_type: UDG
type: feature
description: VNF与对端设备可通过OSPF动态路由绑定IPv6动态BFD探测的方式进行组网连接，该方式适用于IPv6组网的网络中。  在网络拓扑结构复杂、设备与IP路由繁多的网络部署时，通常使用OSPF动态路由方式发布路由。同时，利用BFD双向转发检测机制为链路提供双向、轻负荷且持续时间短的快速检测功能，提高链路可靠性。  如图1和图2所示为VNF与周边网元的OSPF动态路由互通组网示意图。VNF与网关侧运行动态路由协议而接入运营商网络（IP骨干网），网关使用运营商的PE（Provider Edge）交换机，也可以是DC-GW。如下描述以PE做网关为例。PE的路由配置请参考运营商的网络规划配置，DC-GW的配置请参考对应型号设备的产品文档。  **图1** OSPFv3动态路由+IPv6 BFD组网（Eth-trunk子接口组网）  **图2** OSPFv3动态路由+IPv6 BFD组网（Ethernet子接口组网）
risk_level: ''
doc_source: ["网络部署","初始配置","UDG初始配置与调测","组网路由配置","配置VNF侧IP路由数据（NP卡直连PE）","配置动态路由OSPFv3+BFD组网（IPv6）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
VNF与对端设备可通过OSPF动态路由绑定IPv6动态BFD探测的方式进行组网连接，该方式适用于IPv6组网的网络中。在网络拓扑结构复杂、设备与IP路由繁多的网络部署时，通常使用OSPF动态路由方式发布路由。同时，利用BFD双向转发检测机制为链路提供双向、轻负荷且持续时间短的快速检测功能，提高链路可靠性。如图1和图2所示为VNF与周边网元的OSPF动态路由互通组网示意图。VNF与网关侧运行动态路由协议而接入运营商网络（IP骨干网），网关使用运营商的PE（Provider Edge）交换机，也可以是DC-GW。如下描述以PE做网关为例。PE的路由配置请参考运营商的网络规划配置，DC-GW的配置请参考对应型号设备的产品文档。**图1** OSPFv3动态路由+IPv6 BFD组网（Eth-trunk子接口组网）**图2** OSPFv3动态路由+IPv6 BFD组网（Ethernet子接口组网）

## 必备事项
前提条件

* 请阅读并熟悉特性IPFD-014001 支持OSPF特性概述和IPFD-012003 BFD特性概述。

* 具备管理员权限的操作人员已经登录华为操作维护系统（登录U2020/MAE客户端或登录OM Portal）。

* VNF与网络实体之间的网络环境已经构建完成。
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
          data_source: '参见“5G Core LLD文档 > 路由设计 > 5G Core路由设计 > VRF设计 > VRF名称(VNF)”。'
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
    mod_interface_list:
      type: items
      properties:
        IFNAME:
          name: '接口名称'
          type: string
          maxLength: 63
          required: true
          description: '-'
          data_source: '参见“5G Core LLD文档 > 业务IP对接设计 > 业务IP设计 > 端口”。'
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
          description: 'Ethernet子接口组网需要规划。'
          data_source: '参见“5G Core LLD文档 > 业务IP对接设计 > 业务IP设计 > 子端口”。'
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
          data_source: '参见“5G Core LLD文档 > 业务IP对接设计 > 业务IP设计 > VRF”。'
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
          description: '-'
          data_source: '参见“5G Core LLD文档 > 业务IP对接设计 > 业务IP设计 > VLAN序号”。'
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
        AUTOLINKLOCAL:
          name: '自动生成链路层地址标志'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MTU:
          name: 'IPv6接口最大传输单元（byte）'
          type: integer
          minimum: 1280
          maximum: 9600
          required: false
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
          description: '如果规划外联口使用IPv4v6双栈地址，则分别执行**ADD IFIPV4ADDRESS**和**ADD IFIPV6ADDRESS**对同一外联口配置IPv4和IPv6地址。此处规划的IP地址是与网关互通的外联口IP。Eth-trunk子接口组网时，规划1个IP；直连PE，Ethernet子接口组网时，规划2个不同网段的IP。'
          data_source: '参见“5G Core LLD文档 > 业务IP对接设计 > 业务IP设计 > IP”。'
          pattern: ''
          default: ''
        PREFIXLEN:
          name: 'IPv6地址前缀'
          type: integer
          minimum: 1
          maximum: 128
          required: true
          description: ''
          data_source: '参见“5G Core LLD文档 > 业务IP对接设计 > 业务IP设计 > 子网掩码”。'
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
          description: '-'
          data_source: '参见“5G Core LLD文档 > 业务IP对接设计 > 业务IP设计 > 端口”。'
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
          description: 'Eth-trunk子接口组网需要规划。'
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
          description: 'Eth-trunk子接口组网需要规划。为保证转发正常，要求在同一条Eth-Trunk链路两端的Eth-Trunk接口上必须配置相同的最小激活链路数，否则在Eth-Trunk口部分成员口或者链路故障的情况下，会导致业务受损。同一个Trunk的成员接口，可以是同一刀片上的接口，也可以是不同刀片上的接口。此处以加速省交换场景为例，该场景下同一Trunk的成员接口在不同刀片上。当前本端工作模式为LACP的Eth-trunk接口仅支持passive模式，因此要求对接DC-GW/PE的Eth-trunk接口必须为active模式。即要求对接DC-GW/PE上的端口主动发送LACP报文。'
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
        LOADBALANCE:
          name: '负载分担模式'
          type: string
          enum:
          - IP
          - L4
          - PacketAll
          required: false
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
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        MEMBERIFNAME:
          name: '成员接口名'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: '参见“5G Core LLD文档 > 业务IP对接设计 > 业务IP设计 > 端口”。'
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
          description: 'Eth-trunk子接口组网需要规划。为保证转发正常，要求在同一条Eth-Trunk链路两端的Eth-Trunk接口上必须配置相同的最小激活链路数，否则在Eth-Trunk口部分成员口或者链路故障的情况下，会导致业务受损。同一个Trunk的成员接口，可以是同一刀片上的接口，也可以是不同刀片上的接口。此处以加速省交换场景为例，该场景下同一Trunk的成员接口在不同刀片上。当前本端工作模式为LACP的Eth-trunk接口仅支持passive模式，因此要求对接DC-GW/PE的Eth-trunk接口必须为active模式。即要求对接DC-GW/PE上的端口主动发送LACP报文。'
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
        LOADBALANCE:
          name: '负载分担模式'
          type: string
          enum:
          - IP
          - L4
          - PacketAll
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_trunkmember_list_1:
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
          data_source: '参见“5G Core LLD文档 > 业务IP对接设计 > 业务IP设计 > 端口”。'
          pattern: ''
          default: ''
    add_interface_list_4:
      type: items
      properties:
        IFNAME:
          name: '接口名称'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: '参见“5G Core LLD文档 > 业务IP对接设计 > 业务IP设计 > 子端口”。'
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
          data_source: '参见“5G Core LLD文档 > 业务IP对接设计 > 业务IP设计 > VRF”。'
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
          description: '-'
          data_source: '参见“5G Core LLD文档 > 业务IP对接设计 > 业务IP设计 > VLAN序号”。'
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
        AUTOLINKLOCAL:
          name: '自动生成链路层地址标志'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MTU:
          name: 'IPv6接口最大传输单元（byte）'
          type: integer
          minimum: 1280
          maximum: 9600
          required: false
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
          description: '如果规划外联口使用IPv4v6双栈地址，则分别执行**ADD IFIPV4ADDRESS**和**ADD IFIPV6ADDRESS**对同一外联口配置IPv4和IPv6地址。此处规划的IP地址是与网关互通的外联口IP。Eth-trunk子接口组网时，规划1个IP；直连PE，Ethernet子接口组网时，规划2个不同网段的IP。'
          data_source: '参见“5G Core LLD文档 > 业务IP对接设计 > 业务IP设计 > IP”。'
          pattern: ''
          default: ''
        PREFIXLEN:
          name: 'IPv6地址前缀'
          type: integer
          minimum: 1
          maximum: 128
          required: true
          description: ''
          data_source: '参见“5G Core LLD文档 > 业务IP对接设计 > 业务IP设计 > 子网掩码”。'
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
          data_source: '参见“5G Core LLD文档 > 路由设计 > 其他路由设计信息 > BFD设计 > BFD是否使能”。'
          pattern: ''
          default: ''
    add_ospfv3_list:
      type: items
      properties:
        PROCID:
          name: 'OSPFv3进程号'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: true
          description: '-'
          data_source: '参见“5G Core LLD文档 > 路由设计 > 5G Core路由设计 > OSPF设计 > Process ID(VNF)”。'
          pattern: ''
          default: ''
        ROUTERID:
          name: '路由器标识'
          type: string
          maxLength: 15
          required: true
          description: ''
          data_source: '参见“5G Core LLD文档 > 路由设计 > 5G Core路由设计 > OSPF设计 > Router ID(VNF)”。'
          pattern: ''
          default: ''
        VRFNAME:
          name: 'VPN的名称'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: '参见“5G Core LLD文档 > 路由设计 > 5G Core路由设计 > OSPF设计 > VRF名称(VNF)”。'
          pattern: ''
          default: '_public_'
        BFDALLINTFFLG:
          name: '使能BFD'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: '参见“5G Core LLD文档 > 路由设计 > 其他路由设计信息 > BFD设计 > BFD是否使能”。'
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
          data_source: '-'
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
          data_source: '-'
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
          description: '-'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        AREAID:
          name: '区域号'
          type: string
          maxLength: 15
          required: true
          description: '两个接口若要建立邻居关系，则Area ID必须相同。'
          data_source: '参见“5G Core LLD文档 > 路由设计 > 5G Core路由设计 > OSPF设计 > Area ID(VNF)”。'
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
          description: '两个接口若要建立邻居关系，则Area Type必须相同。'
          data_source: '参见“5G Core LLD文档 > 路由设计 > 5G Core路由设计 > OSPF设计 > Area类型”。'
          pattern: ''
          default: Normal
        DEFAULTCOST:
          name: '发送到Stub或NSSA区域的Type3缺省路由的开销'
          type: integer
          minimum: 0
          maximum: 16777214
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 1
        NSSADEFAULTROUTEADVERTISE:
          name: '产生缺省7类LSA到NSSA区域'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        NSSANOIMPORTROUTE:
          name: '不引入外部路由'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        NSSANOSUMMARY:
          name: '禁止ABR向NSSA区域内发送Summary LSA'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        NSSASETNBIT:
          name: '在DD报文中配置N-bit位'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        NSSATRANSLATORALWAYS:
          name: '指定为转换路由器'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        NSSATRANSLATORINTERVAL:
          name: '转换路由器的失效时间（s）'
          type: integer
          minimum: 1
          maximum: 120
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 40
        STUBNOSUMMARY:
          name: '禁止ABR向Stub区域内发送Summary LSA'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
    add_ospfv3areaauth_list:
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
        AUTHENMODE:
          name: '认证模式'
          type: string
          enum:
          - hmac-sha256
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AUTHTEXTTYPE:
          name: '认证密码类型'
          type: string
          enum:
          - cipher
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: cipher
        AUTHTEXTMD5:
          name: '密文验证密码'
          type: string
          maxLength: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        KEYID:
          name: '密文验证字标识符'
          type: integer
          minimum: 1
          maximum: 65535
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_ospfv3interface_list:
      type: items
      properties:
        PROCID:
          name: 'OSPFv3进程号'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: true
          description: '-'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        AREAID:
          name: '区域号'
          type: string
          maxLength: 15
          required: true
          description: ''
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        IFNAME:
          name: '接口名称'
          type: string
          maxLength: 63
          required: true
          description: 'Ethernet子接口组网需要规划。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        DRPRI:
          name: '指定路由器优先级'
          type: integer
          minimum: 0
          maximum: 255
          required: false
          description: '-'
          data_source: '-'
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
          data_source: '-'
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
        CFGROUTERID:
          name: 'OSPFv3虚拟路由器标识'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_ospfv3interface_list_2:
      type: items
      properties:
        PROCID:
          name: 'OSPFv3进程号'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: true
          description: '-'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        AREAID:
          name: '区域号'
          type: string
          maxLength: 15
          required: true
          description: ''
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        IFNAME:
          name: '接口名称'
          type: string
          maxLength: 63
          required: true
          description: 'Eth-trunk子接口组网需要规划。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        DRPRI:
          name: '指定路由器优先级'
          type: integer
          minimum: 0
          maximum: 255
          required: false
          description: '-'
          data_source: '-'
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
          data_source: '-'
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
        CFGROUTERID:
          name: 'OSPFv3虚拟路由器标识'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_ospfv3interfaceauth_list:
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
          name: '接口名'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AUTHENMODE:
          name: '认证模式'
          type: string
          enum:
          - hmac-sha256
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AUTHENTYPE:
          name: '认证密码类型'
          type: string
          enum:
          - cipher
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: cipher
        AUTHTEXTMD5:
          name: '密文验证密码'
          type: string
          maxLength: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        KEYID:
          name: '密文验证字标识符'
          type: integer
          minimum: 1
          maximum: 65535
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        INSTANCEID:
          name: '实例号'
          type: integer
          minimum: 0
          maximum: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_ospfv3importroute_list:
      type: items
      properties:
        PROCID:
          name: 'OSPFv3进程号'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: true
          description: '-'
          data_source: '参见“5G Core LLD文档 > 路由设计 > 5G Core路由设计 > OSPF设计 > Process ID(VNF)”。'
          pattern: ''
          default: ''
        TOPOID:
          name: '拓扑标识'
          type: integer
          minimum: 0
          maximum: 0
          required: false
          description: ''
          data_source: '-'
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
          data_source: '参见“5G Core LLD文档 > 路由设计 > 5G Core路由设计 > OSPF设计 > Import Route类型”。'
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
          data_source: '-'
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
          data_source: '-'
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
          data_source: '-'
          pattern: ''
          default: FALSE
        COST:
          name: '路径Cost值'
          type: integer
          minimum: 0
          maximum: 16777214
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TAG:
          name: '标签'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TYPE:
          name: '引入路由类型'
          type: string
          enum:
          - Type1
          - Type2
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PERMITIBGPCFG:
          name: '允许BGP配置'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        PROTOCOLPROCID:
          name: '协议进程号'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 1
  examples:
    add_l3vpninst_list:
    - VRFNAME: 'VPN_Access'
    add_vpninstaf_list:
    - VRFNAME: 'VPN_Access'
      AFTYPE: ipv6uni
      VRFRD: '10.8.25.1:100'
    mod_vpninstaf_list:
    - VRFNAME: 'VPN_Access'
      AFTYPE: ipv6uni
      VRFRD: '10.8.25.1:100'
    mod_interface_list:
    - IFNAME: '100GE66/0/9'
      IFADMINSTATUS: up
    add_interface_list:
    - IFNAME: '100GE66/0/9.1'
    add_ipbindvpn_list:
    - IFNAME: '100GE66/0/9.1'
      VRFNAME: 'VPN_Access'
    add_ethsubif_list:
    - IFNAME: '100GE66/0/9.1'
      VLANTYPEVID: 100
    set_ifipv6enable_list:
    - IFNAME: '100GE66/0/9.1'
      ENABLEFLAG: TRUE
      AUTOLINKLOCAL: ''
      MTU: ''
    add_ifipv6address_list:
    - IFNAME: '100GE66/0/9.1'
      IPV6ADDRESS: 'FC00::10C2'
      PREFIXLEN: 123
    mod_interface_list_2:
    - IFNAME: '100GE66/0/9'
      IFADMINSTATUS: up
    add_interface_list_2:
    - IFNAME: 'Eth-trunk1'
    mod_trunkif_list:
    - IFNAME: 'Eth-Trunk1'
      WORKMODE: Lacp
      LEASTACTLINKNUM: 1
      LOADBALANCE: ''
    add_trunkmember_list:
    - TRUNKIFNAME: 'Eth-trunk1'
      MEMBERIFNAME: '100GE66/0/9'
    mod_trunkif_list_1:
    - IFNAME: 'Eth-Trunk2'
      WORKMODE: Lacp
      LEASTACTLINKNUM: 1
      LOADBALANCE: ''
    add_trunkmember_list_1:
    - TRUNKIFNAME: 'Eth-trunk2'
      MEMBERIFNAME: '100GE67/0/9'
    add_interface_list_4:
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
      AUTOLINKLOCAL: ''
      MTU: ''
    add_ifipv6address_list_2:
    - IFNAME: 'Eth-trunk1.1'
      IPV6ADDRESS: 'FC00::10C2'
      PREFIXLEN: 123
    set_bfd_list:
    - BFDENABLE: TRUE
    add_ospfv3_list:
    - PROCID: 6
      ROUTERID: '10.8.25.1'
      VRFNAME: 'VPN_Access'
      BFDALLINTFFLG: TRUE
      VPNINSCAPSIMFLG: TRUE
      VIRTUALSYSFLAG: TRUE
    add_ospfv3area_list:
    - PROCID: 6
      AREAID: '0.0.0.5'
      AREATYPE: NSSA
      DEFAULTCOST: 1
      NSSADEFAULTROUTEADVERTISE: FALSE
      NSSANOIMPORTROUTE: FALSE
      NSSANOSUMMARY: FALSE
      NSSASETNBIT: FALSE
      NSSATRANSLATORALWAYS: FALSE
      NSSATRANSLATORINTERVAL: 40
      STUBNOSUMMARY: FALSE
    add_ospfv3areaauth_list:
    - PROCID: OSPFv3进程号
      AREAID: 'OSPFv3区域标识'
      AUTHENMODE: hmac-sha256
      AUTHTEXTTYPE: cipher
      AUTHTEXTMD5: '密文验证密码'
      KEYID: 密文验证字标识符
    add_ospfv3interface_list:
    - PROCID: 6
      AREAID: '0.0.0.5'
      IFNAME: '100GE66/0/9.1'
      DRPRI: 0
      VIRTUALSYSFLAG: TRUE
      CFGROUTERIDFLAG: FALSE
      CFGROUTERID: ''
    add_ospfv3interface_list_2:
    - PROCID: 6
      AREAID: '0.0.0.5'
      IFNAME: 'Eth-trunk1.1'
      DRPRI: 0
      VIRTUALSYSFLAG: TRUE
      CFGROUTERIDFLAG: FALSE
      CFGROUTERID: ''
    add_ospfv3interfaceauth_list:
    - PROCID: OSPFv3进程号
      AREAID: '区域号'
      IFNAME: '接口名称'
      AUTHENMODE: hmac-sha256
      AUTHENTYPE: cipher
      AUTHTEXTMD5: '密文验证密码'
      KEYID: 密文验证字标识符
      INSTANCEID: 实例号
    add_ospfv3importroute_list:
    - PROCID: 6
      TOPOID: 0
      PROTOCOL: wlr
      IMPTCOSTCFG: FALSE
      IMPTTAGCFG: FALSE
      IMPTTYPECFG: FALSE
      COST: ''
      TAG: ''
      TYPE: ''
      PERMITIBGPCFG: FALSE
      PROTOCOLPROCID: 1
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

### 一条通信路径上所有节点绑定的VPN实例要一致，才能正常通信，例如VNF逻辑接口、VNF外联口、网关上的VPN，否则从逻辑接口发出去的报文会查询路由失败。

### 2 Ethernet子接口组网时，配置外联口IP地址。Eth-trunk子接口组网时，请跳过本步骤。

#### 2.1 查看接口状态及信息。

#### 2.2 配置主接口的管理状态为up。

```jinja2
{%- if is_scenario_ethernet_subif -%}
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
{%- if is_scenario_ethernet_subif -%}
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
{%- if is_scenario_ethernet_subif -%}
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
{%- if is_scenario_ethernet_subif -%}
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
{%- if is_scenario_ethernet_subif -%}
    {%- for item in set_ifipv6enable_list -%}
        SET IFIPV6ENABLE:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        ENABLEFLAG={{item.ENABLEFLAG}},
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：ENABLEFLAG=TRUE 时可选 --- -#}
        {%- if item.ENABLEFLAG == 'TRUE' -%}
            {%- if item.AUTOLINKLOCAL is not none -%}
                AUTOLINKLOCAL={{item.AUTOLINKLOCAL}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：ENABLEFLAG=TRUE 时可选 --- -#}
        {%- if item.ENABLEFLAG == 'TRUE' -%}
            {%- if item.MTU is not none -%}
                MTU={{item.MTU}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 2.7 配置外联口的IP地址。

```jinja2
{%- if is_scenario_ethernet_subif -%}
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

### 3 Eth-trunk子接口组网时，配置外联口IP地址。Ethernet子接口组网时，请跳过本步骤。

#### 3.1 查看接口状态及信息。

#### 3.2 配置主接口的管理状态为up。Eth-trunk接口包含多个成员端口的场景，需要多次执行**MOD INTERFACE**命令将每个成员端口的管理状态都设置为up。

```jinja2
{%- if is_scenario_eth_trunk_subif -%}
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
{%- if is_scenario_eth_trunk_subif -%}
    {%- for item in add_interface_list_2 -%}
        ADD INTERFACE:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 3.4 配置Eth-trunk接口的工作模式并添加成员端口。Eth-trunk接口包含多个成员端口的场景，需要多次执行**ADD TRUNKMEMBER**命令添加多个成员端口。

```jinja2
{%- if is_scenario_eth_trunk_subif -%}
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
        {#- --- 条件可选：WORKMODE=Lacp 时可选 --- -#}
        {%- if item.WORKMODE == 'Lacp' -%}
            {%- if item.LOADBALANCE is not none -%}
                LOADBALANCE={{item.LOADBALANCE}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_eth_trunk_subif -%}
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
{%- if is_scenario_eth_trunk_subif -%}
    {%- for item in mod_trunkif_list_1 -%}
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
        {#- --- 条件可选：WORKMODE=Lacp 时可选 --- -#}
        {%- if item.WORKMODE == 'Lacp' -%}
            {%- if item.LOADBALANCE is not none -%}
                LOADBALANCE={{item.LOADBALANCE}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_eth_trunk_subif -%}
    {%- for item in add_trunkmember_list_1 -%}
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
{%- if is_scenario_eth_trunk_subif -%}
    {%- for item in add_interface_list_4 -%}
        ADD INTERFACE:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 3.6 增加接口绑定VPN。

```jinja2
{%- if is_scenario_eth_trunk_subif -%}
    {%- for item in add_ipbindvpn_list_2 -%}
        ADD IPBINDVPN:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        VRFNAME="{{item.VRFNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 3.7 在以太网Trunk子接口上关联VLAN ID。

```jinja2
{%- if is_scenario_eth_trunk_subif -%}
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
{%- if is_scenario_eth_trunk_subif -%}
    {%- for item in set_ifipv6enable_list_2 -%}
        SET IFIPV6ENABLE:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        ENABLEFLAG={{item.ENABLEFLAG}},
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：ENABLEFLAG=TRUE 时可选 --- -#}
        {%- if item.ENABLEFLAG == 'TRUE' -%}
            {%- if item.AUTOLINKLOCAL is not none -%}
                AUTOLINKLOCAL={{item.AUTOLINKLOCAL}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：ENABLEFLAG=TRUE 时可选 --- -#}
        {%- if item.ENABLEFLAG == 'TRUE' -%}
            {%- if item.MTU is not none -%}
                MTU={{item.MTU}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 3.9 配置外联口的IP地址。

```jinja2
{%- if is_scenario_eth_trunk_subif -%}
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

### 5 配置OSPFv3路由数据。

#### 5.1 创建OSPFv3进程。

```jinja2
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
```

#### VNF支持VPN多实例时，需要取消环路检查（参数“VPNINSCAPSIMFLG”配置为“TRUE”），否则会导致OSPF路由引入失败。

#### 路由器标识Router ID（“SCHEMAROUID”）的选择策略：优选用户配置的Router ID，如果未配置，则选择OSPFv3进程所在VRF内或者公网内的最大接口IP地址。

#### 如果需要为OSPFv3动态路由绑定BFD会话，则配置参数“BFDALLINTFFLG（使能BFD）”为“TRUE”。

#### 当OSPFv3路由配置共网段时，需要将参数“VIRTUALSYSFLAG（OSPFv3共网段虚拟系统使能标志）”配置为“TRUE”。

#### 5.2 增加OSPFv3区域。

```jinja2
{%- for item in add_ospfv3area_list -%}
    ADD OSPFV3AREA:
    {#- --- 必选参数 --- -#}
    PROCID={{item.PROCID}},
    AREAID="{{item.AREAID}}",
    {#- --- 可选参数 --- -#}
    {%- if item.AREATYPE is not none -%}
        AREATYPE={{item.AREATYPE}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：AREATYPE=Stub/NSSA 时可选 --- -#}
    {%- if item.AREATYPE in ['Stub', 'NSSA'] -%}
        {%- if item.DEFAULTCOST is not none -%}
            DEFAULTCOST={{item.DEFAULTCOST}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：AREATYPE=NSSA 时可选 --- -#}
    {%- if item.AREATYPE == 'NSSA' -%}
        {%- if item.NSSADEFAULTROUTEADVERTISE is not none -%}
            NSSADEFAULTROUTEADVERTISE={{item.NSSADEFAULTROUTEADVERTISE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：AREATYPE=NSSA 时可选 --- -#}
    {%- if item.AREATYPE == 'NSSA' -%}
        {%- if item.NSSANOIMPORTROUTE is not none -%}
            NSSANOIMPORTROUTE={{item.NSSANOIMPORTROUTE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：AREATYPE=NSSA 时可选 --- -#}
    {%- if item.AREATYPE == 'NSSA' -%}
        {%- if item.NSSANOSUMMARY is not none -%}
            NSSANOSUMMARY={{item.NSSANOSUMMARY}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：AREATYPE=NSSA 时可选 --- -#}
    {%- if item.AREATYPE == 'NSSA' -%}
        {%- if item.NSSASETNBIT is not none -%}
            NSSASETNBIT={{item.NSSASETNBIT}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：AREATYPE=NSSA 时可选 --- -#}
    {%- if item.AREATYPE == 'NSSA' -%}
        {%- if item.NSSATRANSLATORALWAYS is not none -%}
            NSSATRANSLATORALWAYS={{item.NSSATRANSLATORALWAYS}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：AREATYPE=NSSA 时可选 --- -#}
    {%- if item.AREATYPE == 'NSSA' -%}
        {%- if item.NSSATRANSLATORINTERVAL is not none -%}
            NSSATRANSLATORINTERVAL={{item.NSSATRANSLATORINTERVAL}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：AREATYPE=Stub 时可选 --- -#}
    {%- if item.AREATYPE == 'Stub' -%}
        {%- if item.STUBNOSUMMARY is not none -%}
            STUBNOSUMMARY={{item.STUBNOSUMMARY}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 参数“AREATYPE（OSPFv3区域类型）”配置为“NSSA”或“Normal”时，都不需要配置Loopback地址。

#### 5.3 **（可选）**配置OSPFv3区域认证。

```jinja2
{%- if is_optional_ospfv3_area_auth -%}
    {%- for item in add_ospfv3areaauth_list -%}
        ADD OSPFV3AREAAUTH:
        {#- --- 必选参数 --- -#}
        PROCID={{item.PROCID}},
        AREAID="{{item.AREAID}}",
        AUTHENMODE={{item.AUTHENMODE}},
        AUTHTEXTMD5="{{item.AUTHTEXTMD5}}",
        KEYID={{item.KEYID}},
        {#- --- 可选参数 --- -#}
        {%- if item.AUTHTEXTTYPE is not none -%}
            AUTHTEXTTYPE={{item.AUTHTEXTTYPE}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 使用区域验证时，一个区域中所有设备的接口上所配置的认证模式和口令必须一致。

#### 5.4 配置OSPFv3协议的接口属性。

##### 5.4.1 Ethernet子接口组网场景下：

```jinja2
{%- if is_scenario_ethernet_subif -%}
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
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：CFGROUTERIDFLAG=TRUE 时必选 --- -#}
        {%- if item.CFGROUTERIDFLAG == 'TRUE' -%}
            CFGROUTERID="{{item.CFGROUTERID}}",
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

##### 5.4.2 Eth-trunk子接口组网场景下：

```jinja2
{%- if is_scenario_eth_trunk_subif -%}
    {%- for item in add_ospfv3interface_list_2 -%}
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
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：CFGROUTERIDFLAG=TRUE 时必选 --- -#}
        {%- if item.CFGROUTERIDFLAG == 'TRUE' -%}
            CFGROUTERID="{{item.CFGROUTERID}}",
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

#### 参数“NETWORKTYPE”（网络类型）选择“BROADCAST”、“NBMA”、“POINT-TO-POINT”、“POINT-TO-MULTIPOINT”或“P2MP-NONBROADCAST”。

#### 广播或NBMA网络中，根据此接口优先级选举DR和BDR路由器，“优先级”设置为“0”表示不参与DR和BDR的选举。为避免VNF被选为DR或BDR，建议将VNF“优先级”配置为0，对端配置为非0。

#### 5.5 **（可选）**配置OSPFv3接口验证参数。

```jinja2
{%- if is_optional_ospfv3_interface_auth -%}
    {%- for item in add_ospfv3interfaceauth_list -%}
        ADD OSPFV3INTERFACEAUTH:
        {#- --- 必选参数 --- -#}
        PROCID={{item.PROCID}},
        AREAID="{{item.AREAID}}",
        IFNAME="{{item.IFNAME}}",
        AUTHENMODE={{item.AUTHENMODE}},
        AUTHTEXTMD5="{{item.AUTHTEXTMD5}}",
        KEYID={{item.KEYID}},
        INSTANCEID={{item.INSTANCEID}},
        {#- --- 可选参数 --- -#}
        {%- if item.AUTHENTYPE is not none -%}
            AUTHENTYPE={{item.AUTHENTYPE}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 5.6 设置OSPFv3引入路由类型。

```jinja2
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
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IMPTCOSTCFG=TRUE 时必选 --- -#}
    {%- if item.IMPTCOSTCFG == 'TRUE' -%}
        COST={{item.COST}},
    {%- endif -%}
    {#- --- 条件必选：IMPTTAGCFG=TRUE 时必选 --- -#}
    {%- if item.IMPTTAGCFG == 'TRUE' -%}
        TAG={{item.TAG}},
    {%- endif -%}
    {#- --- 条件必选：IMPTTYPECFG=TRUE 时必选 --- -#}
    {%- if item.IMPTTYPECFG == 'TRUE' -%}
        TYPE={{item.TYPE}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：PROTOCOL=bgp 时可选 --- -#}
    {%- if item.PROTOCOL == 'bgp' -%}
        {%- if item.PERMITIBGPCFG is not none -%}
            PERMITIBGPCFG={{item.PERMITIBGPCFG}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：PROTOCOL=ospfv3 时可选 --- -#}
    {%- if item.PROTOCOL == 'ospfv3' -%}
        {%- if item.PROTOCOLPROCID is not none -%}
            PROTOCOLPROCID={{item.PROTOCOLPROCID}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```


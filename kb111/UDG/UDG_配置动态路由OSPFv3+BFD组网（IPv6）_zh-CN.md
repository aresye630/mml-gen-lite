---
id: ''
name: 配置动态路由OSPFv3+BFD组网（IPv6）
ne_type: UDG
type: feature
description: VNF与对端设备可通过OSPF动态路由绑定IPv6动态BFD探测的方式进行组网连接，该方式适用于IPv6组网的网络中。  在网络拓扑结构复杂、设备与IP路由繁多的网络部署时，通常使用OSPF动态路由方式发布路由。同时，利用BFD双向转发检测机制为链路提供双向、轻负荷且持续时间短的快速检测功能，提高链路可靠性。  如图1所示为VNF与周边网元的OSPF动态路由互通组网示意图。VNF与网关运行动态路由协议而接入运营商网络（IP骨干网），网关可以使用DC-GW、EOR（End of Row）交换机或运营商的PE（Provider Edge）交换机。无论哪种方式，VNF的配置相同，没有差异。PE的路由配置请参考运营商的网络规划配置，DC-GW/EOR的配置请参考对应型号设备的产品文档。  **图1** OSPFv3动态路由+IPv6 BFD组网
risk_level: ''
doc_source: ["网络部署","初始配置","UDG初始配置与调测","组网路由配置","配置VNF侧IP路由数据（无NP卡_非SDN）","自动部署（推荐）","配置动态路由OSPFv3+BFD组网（IPv6）"]
refs: []
metadata:
  DepOnLiveCfg: true
allowed-tools:
- getParameterValue('LST AUTOCONFIG')
---
<!-- @mml:block=annotations -->
```text
## 操作场景
VNF与对端设备可通过OSPF动态路由绑定IPv6动态BFD探测的方式进行组网连接，该方式适用于IPv6组网的网络中。在网络拓扑结构复杂、设备与IP路由繁多的网络部署时，通常使用OSPF动态路由方式发布路由。同时，利用BFD双向转发检测机制为链路提供双向、轻负荷且持续时间短的快速检测功能，提高链路可靠性。如图1所示为VNF与周边网元的OSPF动态路由互通组网示意图。VNF与网关运行动态路由协议而接入运营商网络（IP骨干网），网关可以使用DC-GW、EOR（End of Row）交换机或运营商的PE（Provider Edge）交换机。无论哪种方式，VNF的配置相同，没有差异。PE的路由配置请参考运营商的网络规划配置，DC-GW/EOR的配置请参考对应型号设备的产品文档。**图1** OSPFv3动态路由+IPv6 BFD组网

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
          data_source: '参见“5G Core LLD文档 > 业务IP对接设计 > VRF”。  请选中“虚拟机类型”为“ISU”/“ISU\_Cxx”且“子端口”为“group\_isu\_xxxx”的所有行，查找指定“逻辑接口”对应的“VRF”。逻辑接口包括N3if、N4if、N6等接口。此处以N3if为例。'
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
          name: '地址族名称'
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
          description: '参数“DELAYUPTIMER”（会话延迟UP时间）和“TOSEXP”（动态会话报文优先级）可以不用配置，使用默认值即可。'
          data_source: '参见“5G Core LLD文档 > 路由设计 > BFD设计 > BFD是否使能”。'
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
          data_source: '参见“5G Core LLD文档 > 路由设计 > OSPF设计 > Process-ID”。'
          pattern: ''
          default: ''
        VRFNAME:
          name: 'VPN的名称'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: '参见“5G Core LLD文档 > 路由设计 >OSPF设计 > VRF名称”。'
          pattern: ''
          default: '_public_'
        ROUTERID:
          name: '路由器标识'
          type: string
          maxLength: 15
          required: true
          description: ''
          data_source: '参见“5G Core LLD文档 > 路由设计 > OSPF设计 > Router ID”。'
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
          data_source: '参见“5G Core LLD文档 > 路由设计 > BFD设计 > BFD是否使能”。'
          pattern: ''
          default: FALSE
        BFDRXCFGFLAG:
          name: '是否配置BFD最小接收报文间隔'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: ''
          data_source: '-'
          pattern: ''
          default: FALSE
        BFDMINRXINTV:
          name: '接收BFD包的最小时间间隔（ms）'
          type: integer
          minimum: 30
          maximum: 1000
          required: false
          description: ''
          data_source: '参见“5G Core LLD文档 > 路由设计 > BFD设计 > min-rx-interval(毫秒)”。'
          pattern: ''
          default: ''
        BFDTXCFGFLAG:
          name: '是否配置BFD最小发送报文间隔'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: ''
          data_source: '-'
          pattern: ''
          default: FALSE
        BFDMINTXINTV:
          name: '发送BFD包的最小时间间隔（ms）'
          type: integer
          minimum: 30
          maximum: 1000
          required: false
          description: ''
          data_source: '参见“5G Core LLD文档 > 路由设计 > BFD设计 > min-tx-interval(毫秒)”。'
          pattern: ''
          default: ''
        DETECTMULINTV:
          name: 'BFD检测乘数间隔'
          type: integer
          minimum: 3
          maximum: 50
          required: false
          description: ''
          data_source: '参见“5G Core LLD文档 > 路由设计 > BFD设计 > detect-multiplier”。'
          pattern: ''
          default: 3
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
          name: 'OSPF共网段虚拟系统使能标志'
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
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AREAID:
          name: 'OSPFv3区域标识'
          type: string
          maxLength: 15
          required: true
          description: '两个接口若要建立邻居关系，则Area ID必须相同。'
          data_source: '参见“5G Core LLD文档 > 路由设计 > OSPF设计 > Area ID”。'
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
          data_source: '参见“5G Core LLD文档 > 路由设计 > OSPF设计 > Area Type”。'
          pattern: ''
          default: Normal
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
        NSSADEFAULTCOSTCFG:
          name: '指定缺省开销值'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        NSSADEFAULTTAGCFG:
          name: '指定缺省路由的tag值'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        NSSADEFAULTTYPECFG:
          name: '指定缺省路由的类型'
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
          description: '-'
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
          data_source: '参见“5G Core LLD文档 > 路由设计 > OSPF设计 > import route类型”。'
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
          description: 'SR-IOV bonding组网需要规划。  只有MAC地址一样的VNIC才能加到同一个TRUNK里。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        VNICLIST:
          name: '虚拟网卡ID列表'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: '参见“5G Core LLD文档 > 业务IP对接设计 > 虚拟网口”。  请选中“虚拟机类型”为“ISU”/“ISU\_Cxx”且“子端口”为“group\_isu\_xxxx”的所有行，查找指定“逻辑接口”对应的“虚拟网口”。逻辑接口包括N3if、N4if、N6等接口。此处以N3if为例。'
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
          description: '如果规划外联口使用IPv4v6双栈地址，则分别执行该命令对同一外联口配置IPv4和IPv6地址。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        VPNNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: '已规划数据中获取'
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
          data_source: '参见“5G Core LLD文档 > 业务IP对接设计 > 虚拟网口”。  请选中“虚拟机类型”为“ISU”/“ISU\_Cxx”且“子端口”为“group\_isu\_xxxx”的所有行，查找指定“逻辑接口”对应的“虚拟网口”。逻辑接口包括N3if、N4if、N6等接口。此处以N3if为例。'
          pattern: ''
          default: ''
        VLANID:
          name: 'VLAN ID'
          type: integer
          minimum: 0
          maximum: 4094
          required: false
          description: '此处以双平面为例，单平面组网时，只需规划一条数据（例如只规划ServName\_Access\_100）。  此处规划的IP地址是与网关互通的外联口IP。  根据ISU VM的数量规划IPv6地址池掩码长度。  此处以121位掩码为例进行介绍，具体以网设规划为准。'
          data_source: '参见“5G Core LLD文档 > 业务IP对接设计 > VLAN ID（VM）”。  请选中“虚拟机类型”为“ISU”/“ISU\_Cxx”且“子端口”为“group\_isu\_xxxx”的所有行，查找指定“逻辑接口”对应的“VLAN ID（VM）”。逻辑接口包括N3if、N4if、N6等接口。此处以N3if为例。'
          pattern: ''
          default: 0
        BEGINADDR6:
          name: '起始地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: '参见“5G Core LLD文档 > 业务IP对接设计 > 起始IP”。  请选中“虚拟机类型”为“ISU”/“ISU\_Cxx”且“子端口”为“group\_isu\_xxxx”的所有行，查找指定“逻辑接口”对应的“起始IP”。逻辑接口包括N3if、N4if、N6等接口。此处以N3if为例。'
          pattern: ''
          default: ''
        ENDADDR6:
          name: '结束地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: '参见“5G Core LLD文档 > 业务IP对接设计 > 结束IP”。  请选中“虚拟机类型”为“ISU”/“ISU\_Cxx”且“子端口”为“group\_isu\_xxxx”的所有行，查找指定“逻辑接口”对应的“结束IP”。逻辑接口包括N3if、N4if、N6等接口。此处以N3if为例。'
          pattern: ''
          default: ''
        MASKLEN:
          name: '地址池掩码长度'
          type: integer
          minimum: 1
          maximum: 128
          required: false
          description: ''
          data_source: '参见“5G Core LLD文档 > 业务IP对接设计 > 子网掩码”。  请选中“虚拟机类型”为“ISU”/“ISU\_Cxx”且“子端口”为“group\_isu\_xxxx”的所有行，查找指定“逻辑接口”对应的“子网掩码”。逻辑接口包括N3if、N4if、N6等接口。此处以N3if为例。'
          pattern: ''
          default: ''
        OSPFENABLE:
          name: '使能OSPFv3'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: FALSE
        OSPFPROCID:
          name: 'OSPFv3进程ID'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: false
          description: ''
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        OSPFAREAID:
          name: 'OSPFv3区域ID'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        TPINENABLE:
          name: '使能入方向的流量策略'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: ''
          data_source: '-'
          pattern: ''
          default: FALSE
        TPOUTENABLE:
          name: '使能出方向的流量策略'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: ''
          data_source: '-'
          pattern: ''
          default: FALSE
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
        ETHTRUNKTMPID:
          name: '以太Trunk模板ID'
          type: integer
          minimum: 1
          maximum: 99
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ADDRMODE:
          name: '地址模式'
          type: string
          enum:
          - HOST_MODE
          - NETWOKSEGMENT_MODE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: HOST_MODE
        OSPFCOST:
          name: 'OSPF开销'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        OSPFDEADTIMER:
          name: '邻居失效的时间（s）'
          type: integer
          minimum: 0
          maximum: 235926000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        OSPFGRPENABLE:
          name: '使能OSPF进程组'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        OSPFHELLOTIMER:
          name: '邻居发送Hello包时间间隔（s）'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 0
        OSPFINSTID:
          name: 'OSPF实例ID'
          type: integer
          minimum: 0
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TPINLINKFLAG:
          name: '入方向的流量策略链接标记'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        TPINNAME:
          name: '入方向的流量策略名称'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TPOUTLINKFLAG:
          name: '出方向的流量策略链接标记'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        TPOUTNAME:
          name: '出方向的流量策略名称'
          type: string
          maxLength: 31
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
          description: '如果规划外联口使用IPv4v6双栈地址，则分别执行该命令对同一外联口配置IPv4和IPv6地址。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        VPNNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: '已规划数据中获取'
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
          description: '此处以双平面为例，单平面组网时，只需规划一条数据（例如只规划ServName\_Access\_100）。  此处规划的IP地址是与网关互通的外联口IP。  根据ISU VM的数量规划IPv6地址池掩码长度。  此处以121位掩码为例进行介绍，具体以网设规划为准。'
          data_source: '参见“5G Core LLD文档 > 业务IP对接设计 > VLAN ID（VM）”。  请选中“虚拟机类型”为“ISU”/“ISU\_Cxx”且“子端口”为“group\_isu\_xxxx”的所有行，查找指定“逻辑接口”对应的“VLAN ID（VM）”。逻辑接口包括N3if、N4if、N6等接口。此处以N3if为例。'
          pattern: ''
          default: 0
        BEGINADDR6:
          name: '起始地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: '参见“5G Core LLD文档 > 业务IP对接设计 > 起始IP”。  请选中“虚拟机类型”为“ISU”/“ISU\_Cxx”且“子端口”为“group\_isu\_xxxx”的所有行，查找指定“逻辑接口”对应的“起始IP”。逻辑接口包括N3if、N4if、N6等接口。此处以N3if为例。'
          pattern: ''
          default: ''
        ENDADDR6:
          name: '结束地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: '参见“5G Core LLD文档 > 业务IP对接设计 > 结束IP”。  请选中“虚拟机类型”为“ISU”/“ISU\_Cxx”且“子端口”为“group\_isu\_xxxx”的所有行，查找指定“逻辑接口”对应的“结束IP”。逻辑接口包括N3if、N4if、N6等接口。此处以N3if为例。'
          pattern: ''
          default: ''
        MASKLEN:
          name: '地址池掩码长度'
          type: integer
          minimum: 1
          maximum: 128
          required: false
          description: ''
          data_source: '参见“5G Core LLD文档 > 业务IP对接设计 > 子网掩码”。  请选中“虚拟机类型”为“ISU”/“ISU\_Cxx”且“子端口”为“group\_isu\_xxxx”的所有行，查找指定“逻辑接口”对应的“子网掩码”。逻辑接口包括N3if、N4if、N6等接口。此处以N3if为例。'
          pattern: ''
          default: ''
        OSPFENABLE:
          name: '使能OSPFv3'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: FALSE
        OSPFPROCID:
          name: 'OSPFv3进程ID'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: false
          description: ''
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        OSPFAREAID:
          name: 'OSPFv3区域ID'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        TPINENABLE:
          name: '使能入方向的流量策略'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: ''
          data_source: '-'
          pattern: ''
          default: FALSE
        TPOUTENABLE:
          name: '使能出方向的流量策略'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: ''
          data_source: '-'
          pattern: ''
          default: FALSE
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
        VNICID:
          name: '虚拟网卡ID'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ADDRMODE:
          name: '地址模式'
          type: string
          enum:
          - HOST_MODE
          - NETWOKSEGMENT_MODE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: HOST_MODE
        OSPFCOST:
          name: 'OSPF开销'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        OSPFDEADTIMER:
          name: '邻居失效的时间（s）'
          type: integer
          minimum: 0
          maximum: 235926000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        OSPFGRPENABLE:
          name: '使能OSPF进程组'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        OSPFHELLOTIMER:
          name: '邻居发送Hello包时间间隔（s）'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 0
        OSPFINSTID:
          name: 'OSPF实例ID'
          type: integer
          minimum: 0
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TPINLINKFLAG:
          name: '入方向的流量策略链接标记'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        TPINNAME:
          name: '入方向的流量策略名称'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TPOUTLINKFLAG:
          name: '出方向的流量策略链接标记'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        TPOUTNAME:
          name: '出方向的流量策略名称'
          type: string
          maxLength: 31
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
    set_bfd_list:
    - BFDENABLE: TRUE
    add_ospfv3_list:
    - PROCID: 6
      VRFNAME: 'VPN_Access'
      ROUTERID: '10.8.25.1'
      BFDALLINTFFLG: TRUE
      BFDRXCFGFLAG: TRUE
      BFDMINRXINTV: 500
      BFDTXCFGFLAG: TRUE
      BFDMINTXINTV: 500
      DETECTMULINTV: 4
      VPNINSCAPSIMFLG: TRUE
      VIRTUALSYSFLAG: TRUE
    add_ospfv3area_list:
    - PROCID: 6
      AREAID: '0.0.0.5'
      AREATYPE: NSSA
      NSSADEFAULTROUTEADVERTISE: FALSE
      DEFAULTCOST: 1
      NSSANOIMPORTROUTE: FALSE
      NSSANOSUMMARY: FALSE
      NSSASETNBIT: FALSE
      NSSATRANSLATORALWAYS: FALSE
      NSSATRANSLATORINTERVAL: 40
      STUBNOSUMMARY: FALSE
      NSSADEFAULTCOSTCFG: FALSE
      NSSADEFAULTTAGCFG: FALSE
      NSSADEFAULTTYPECFG: FALSE
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
    set_autoconfig_list:
    - SWITCHFLAG: FALSE
    add_autoscalingethtrunk_list:
    - ETHTRUNKTMPID: 1
      VNICLIST: '4 5'
    add_autoscalingservice_list:
    - SERVICENAME: 'ServName_Access_100'
      VPNNAME: 'VPN_Access'
      AFTYPE: IPv6
      IPALLOCTYPE6: USER_CONFIG
      AUTOCFGIFTYPE: VNIC
      VNICID: 4
      VLANID: 100
      BEGINADDR6: 'FC00::1002'
      ENDADDR6: 'FC00::107E'
      MASKLEN: 121
      OSPFENABLE: TRUE
      OSPFPROCID: 6
      OSPFAREAID: '0.0.0.5'
      TPINENABLE: FALSE
      TPOUTENABLE: FALSE
      IPALLOCTYPE4: USER_CONFIG
      ETHTRUNKTMPID: ''
      ADDRMODE: HOST_MODE
      OSPFCOST: ''
      OSPFDEADTIMER: ''
      OSPFGRPENABLE: FALSE
      OSPFHELLOTIMER: ''
      OSPFINSTID: ''
      TPINLINKFLAG: FALSE
      TPINNAME: ''
      TPOUTLINKFLAG: FALSE
      TPOUTNAME: ''
    add_autoscalingservice_list_2:
    - SERVICENAME: 'ServName_Access_100'
      VPNNAME: 'VPN_Access'
      AFTYPE: IPv6
      IPALLOCTYPE6: USER_CONFIG
      AUTOCFGIFTYPE: ETHTRUNK
      ETHTRUNKTMPID: 1
      VLANID: 100
      BEGINADDR6: 'FC00::1002'
      ENDADDR6: 'FC00::107E'
      MASKLEN: 121
      OSPFENABLE: TRUE
      OSPFPROCID: 6
      OSPFAREAID: '0.0.0.5'
      TPINENABLE: FALSE
      TPOUTENABLE: FALSE
      IPALLOCTYPE4: USER_CONFIG
      VNICID: ''
      ADDRMODE: HOST_MODE
      OSPFCOST: ''
      OSPFDEADTIMER: ''
      OSPFGRPENABLE: FALSE
      OSPFHELLOTIMER: ''
      OSPFINSTID: ''
      TPINLINKFLAG: FALSE
      TPINNAME: ''
      TPOUTLINKFLAG: FALSE
      TPOUTNAME: ''
    set_autoconfig_list_1:
    - SWITCHFLAG: TRUE
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

### 2 全局激活BFD。

```jinja2
{%- for item in set_bfd_list -%}
    SET BFD:
    {#- --- 必选参数 --- -#}
    BFDENABLE={{item.BFDENABLE}},
    ;
{%- endfor -%}
```

### 3 配置OSPF路由。

#### 3.1 创建OSPFv3进程。

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
    {%- if item.BFDRXCFGFLAG is not none -%}
        BFDRXCFGFLAG={{item.BFDRXCFGFLAG}},
    {%- endif -%}
    {%- if item.BFDTXCFGFLAG is not none -%}
        BFDTXCFGFLAG={{item.BFDTXCFGFLAG}},
    {%- endif -%}
    {%- if item.DETECTMULINTV is not none -%}
        DETECTMULINTV={{item.DETECTMULINTV}},
    {%- endif -%}
    {%- if item.VPNINSCAPSIMFLG is not none -%}
        VPNINSCAPSIMFLG={{item.VPNINSCAPSIMFLG}},
    {%- endif -%}
    {%- if item.VIRTUALSYSFLAG is not none -%}
        VIRTUALSYSFLAG={{item.VIRTUALSYSFLAG}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：BFDRXCFGFLAG=TRUE 时必选 --- -#}
    {%- if item.BFDRXCFGFLAG == 'TRUE' -%}
        BFDMINRXINTV={{item.BFDMINRXINTV}},
    {%- endif -%}
    {#- --- 条件必选：BFDTXCFGFLAG=TRUE 时必选 --- -#}
    {%- if item.BFDTXCFGFLAG == 'TRUE' -%}
        BFDMINTXINTV={{item.BFDMINTXINTV}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### VNF支持VPN多实例，因此需要取消环路检查（参数“VPNINSCAPSIMFLG”配置为“TRUE”），否则会导致OSPF路由引入失败。

#### 路由器标识Router ID（“SCHEMAROUID”）的选择策略：优选用户配置的Router ID，如果未配置，则选择OSPFv3进程所在VRF内或者公网内的最大接口IP地址。

#### 如果需要为OSPFv3动态路由绑定BFD会话，则配置参数“BFDALLINTFFLG（使能BFD）”为“TRUE”。

#### 当OSPFv3路由配置共网段时，需要将参数“VIRTUALSYSFLAG（OSPFv3共网段虚拟系统使能标志）”配置为“TRUE”。

#### 3.2 增加OSPFv3区域。

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
    {#- --- 条件可选：AREATYPE=NSSA 时可选 --- -#}
    {%- if item.AREATYPE == 'NSSA' -%}
        {%- if item.NSSADEFAULTROUTEADVERTISE is not none -%}
            NSSADEFAULTROUTEADVERTISE={{item.NSSADEFAULTROUTEADVERTISE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：AREATYPE=Stub/NSSA 时可选 --- -#}
    {%- if item.AREATYPE in ['Stub', 'NSSA'] -%}
        {%- if item.DEFAULTCOST is not none -%}
            DEFAULTCOST={{item.DEFAULTCOST}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：NSSADEFAULTROUTEADVERTISE=TRUE 时可选 --- -#}
    {%- if item.NSSADEFAULTROUTEADVERTISE == 'TRUE' -%}
        {%- if item.NSSADEFAULTCOSTCFG is not none -%}
            NSSADEFAULTCOSTCFG={{item.NSSADEFAULTCOSTCFG}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：NSSADEFAULTROUTEADVERTISE=TRUE 时可选 --- -#}
    {%- if item.NSSADEFAULTROUTEADVERTISE == 'TRUE' -%}
        {%- if item.NSSADEFAULTTAGCFG is not none -%}
            NSSADEFAULTTAGCFG={{item.NSSADEFAULTTAGCFG}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：NSSADEFAULTROUTEADVERTISE=TRUE 时可选 --- -#}
    {%- if item.NSSADEFAULTROUTEADVERTISE == 'TRUE' -%}
        {%- if item.NSSADEFAULTTYPECFG is not none -%}
            NSSADEFAULTTYPECFG={{item.NSSADEFAULTTYPECFG}},
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

#### 3.3 设置OSPFv3引入路由类型。

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

### 4 关闭自动配置开关。

#### 4.1 查询自动配置开关。

#### 如果自动配置开关值为“TRUE”，需要执行如下步骤关闭自动配置开关。

#### 4.2 （可选）查询自动部署维护助手“autoscaling\_autoconfig.py”的状态，确保状态为“准备好状态（Ready）”或者查询无该脚本，以保证当前设备不在自动部署过程中。因为若系统当前有正在进行的自动部署，而自动部署生效有时延，此时若关闭自动配置开关，会影响系统配置效果。

#### 4.3 （可选）关闭自动配置开关。自动化配置命令只有在自动配置开关为关闭的状态下才可执行，因此需要提前关闭。

```jinja2
{%- set LST_AUTOCONFIG=getParameterValue('LST AUTOCONFIG') -%}
{%- if is_optional_close_autoconfig and LST_AUTOCONFIG=='TRUE' -%}
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
        {%- if item.OSPFENABLE is not none -%}
            OSPFENABLE={{item.OSPFENABLE}},
        {%- endif -%}
        {%- if item.TPINENABLE is not none -%}
            TPINENABLE={{item.TPINENABLE}},
        {%- endif -%}
        {%- if item.TPOUTENABLE is not none -%}
            TPOUTENABLE={{item.TPOUTENABLE}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：AUTOCFGIFTYPE=VNIC 时必选 --- -#}
        {%- if item.AUTOCFGIFTYPE == 'VNIC' -%}
            VNICID={{item.VNICID}},
        {%- endif -%}
        {#- --- 条件必选：IPALLOCTYPE6=USER_CONFIG 时必选 --- -#}
        {%- if item.IPALLOCTYPE6 == 'USER_CONFIG' -%}
            BEGINADDR6="{{item.BEGINADDR6}}",
        {%- endif -%}
        {#- --- 条件必选：IPALLOCTYPE6=USER_CONFIG 时必选 --- -#}
        {%- if item.IPALLOCTYPE6 == 'USER_CONFIG' -%}
            ENDADDR6="{{item.ENDADDR6}}",
        {%- endif -%}
        {#- --- 条件必选：IPALLOCTYPE4=USER_CONFIG 时必选 --- -#}
        {%- if item.IPALLOCTYPE4 == 'USER_CONFIG' -%}
            MASKLEN={{item.MASKLEN}},
        {#- --- 条件必选：IPALLOCTYPE6=USER_CONFIG 时必选 --- -#}
        {%- elif item.IPALLOCTYPE6 == 'USER_CONFIG' -%}
            MASKLEN={{item.MASKLEN}},
        {%- endif -%}
        {#- --- 条件必选：OSPFENABLE=TRUE 时必选 --- -#}
        {%- if item.OSPFENABLE == 'TRUE' -%}
            OSPFPROCID={{item.OSPFPROCID}},
        {%- endif -%}
        {#- --- 条件必选：OSPFENABLE=TRUE 时必选 --- -#}
        {%- if item.OSPFENABLE == 'TRUE' -%}
            OSPFAREAID="{{item.OSPFAREAID}}",
        {%- endif -%}
        {#- --- 条件必选：AUTOCFGIFTYPE=ETHTRUNK 时必选 --- -#}
        {%- if item.AUTOCFGIFTYPE == 'ETHTRUNK' -%}
            ETHTRUNKTMPID={{item.ETHTRUNKTMPID}},
        {%- endif -%}
        {#- --- 条件必选：TPINENABLE=TRUE 时必选 --- -#}
        {%- if item.TPINENABLE == 'TRUE' -%}
            TPINNAME="{{item.TPINNAME}}",
        {%- endif -%}
        {#- --- 条件必选：TPOUTENABLE=TRUE 时必选 --- -#}
        {%- if item.TPOUTENABLE == 'TRUE' -%}
            TPOUTNAME="{{item.TPOUTNAME}}",
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
        {#- --- 条件可选：AFTYPE=IPv4 时可选 --- -#}
        {%- if item.AFTYPE == 'IPv4' -%}
            {%- if item.IPALLOCTYPE4 is not none -%}
                IPALLOCTYPE4={{item.IPALLOCTYPE4}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：OSPFENABLE=TRUE 时可选 --- -#}
        {%- if item.OSPFENABLE == 'TRUE' -%}
            {%- if item.OSPFCOST is not none -%}
                OSPFCOST={{item.OSPFCOST}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：OSPFENABLE=TRUE 时可选 --- -#}
        {%- if item.OSPFENABLE == 'TRUE' -%}
            {%- if item.OSPFDEADTIMER is not none -%}
                OSPFDEADTIMER={{item.OSPFDEADTIMER}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：OSPFENABLE=FALSE 时可选 --- -#}
        {%- if item.OSPFENABLE == 'FALSE' -%}
            {%- if item.OSPFGRPENABLE is not none -%}
                OSPFGRPENABLE={{item.OSPFGRPENABLE}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：OSPFENABLE=TRUE 时可选 --- -#}
        {%- if item.OSPFENABLE == 'TRUE' -%}
            {%- if item.OSPFHELLOTIMER is not none -%}
                OSPFHELLOTIMER={{item.OSPFHELLOTIMER}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：OSPFENABLE=TRUE 时可选 --- -#}
        {%- if item.OSPFENABLE == 'TRUE' -%}
            {%- if item.OSPFINSTID is not none -%}
                OSPFINSTID={{item.OSPFINSTID}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：TPINENABLE=TRUE 时可选 --- -#}
        {%- if item.TPINENABLE == 'TRUE' -%}
            {%- if item.TPINLINKFLAG is not none -%}
                TPINLINKFLAG={{item.TPINLINKFLAG}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：TPOUTENABLE=TRUE 时可选 --- -#}
        {%- if item.TPOUTENABLE == 'TRUE' -%}
            {%- if item.TPOUTLINKFLAG is not none -%}
                TPOUTLINKFLAG={{item.TPOUTLINKFLAG}},
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
        {%- if item.OSPFENABLE is not none -%}
            OSPFENABLE={{item.OSPFENABLE}},
        {%- endif -%}
        {%- if item.TPINENABLE is not none -%}
            TPINENABLE={{item.TPINENABLE}},
        {%- endif -%}
        {%- if item.TPOUTENABLE is not none -%}
            TPOUTENABLE={{item.TPOUTENABLE}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：AUTOCFGIFTYPE=ETHTRUNK 时必选 --- -#}
        {%- if item.AUTOCFGIFTYPE == 'ETHTRUNK' -%}
            ETHTRUNKTMPID={{item.ETHTRUNKTMPID}},
        {%- endif -%}
        {#- --- 条件必选：IPALLOCTYPE6=USER_CONFIG 时必选 --- -#}
        {%- if item.IPALLOCTYPE6 == 'USER_CONFIG' -%}
            BEGINADDR6="{{item.BEGINADDR6}}",
        {%- endif -%}
        {#- --- 条件必选：IPALLOCTYPE6=USER_CONFIG 时必选 --- -#}
        {%- if item.IPALLOCTYPE6 == 'USER_CONFIG' -%}
            ENDADDR6="{{item.ENDADDR6}}",
        {%- endif -%}
        {#- --- 条件必选：IPALLOCTYPE4=USER_CONFIG 时必选 --- -#}
        {%- if item.IPALLOCTYPE4 == 'USER_CONFIG' -%}
            MASKLEN={{item.MASKLEN}},
        {#- --- 条件必选：IPALLOCTYPE6=USER_CONFIG 时必选 --- -#}
        {%- elif item.IPALLOCTYPE6 == 'USER_CONFIG' -%}
            MASKLEN={{item.MASKLEN}},
        {%- endif -%}
        {#- --- 条件必选：OSPFENABLE=TRUE 时必选 --- -#}
        {%- if item.OSPFENABLE == 'TRUE' -%}
            OSPFPROCID={{item.OSPFPROCID}},
        {%- endif -%}
        {#- --- 条件必选：OSPFENABLE=TRUE 时必选 --- -#}
        {%- if item.OSPFENABLE == 'TRUE' -%}
            OSPFAREAID="{{item.OSPFAREAID}}",
        {%- endif -%}
        {#- --- 条件必选：TPINENABLE=TRUE 时必选 --- -#}
        {%- if item.TPINENABLE == 'TRUE' -%}
            TPINNAME="{{item.TPINNAME}}",
        {%- endif -%}
        {#- --- 条件必选：TPOUTENABLE=TRUE 时必选 --- -#}
        {%- if item.TPOUTENABLE == 'TRUE' -%}
            TPOUTNAME="{{item.TPOUTNAME}}",
        {%- endif -%}
        {#- --- 条件必选：AUTOCFGIFTYPE=VNIC 时必选 --- -#}
        {%- if item.AUTOCFGIFTYPE == 'VNIC' -%}
            VNICID={{item.VNICID}},
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
        {#- --- 条件可选：AFTYPE=IPv4 时可选 --- -#}
        {%- if item.AFTYPE == 'IPv4' -%}
            {%- if item.IPALLOCTYPE4 is not none -%}
                IPALLOCTYPE4={{item.IPALLOCTYPE4}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：OSPFENABLE=TRUE 时可选 --- -#}
        {%- if item.OSPFENABLE == 'TRUE' -%}
            {%- if item.OSPFCOST is not none -%}
                OSPFCOST={{item.OSPFCOST}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：OSPFENABLE=TRUE 时可选 --- -#}
        {%- if item.OSPFENABLE == 'TRUE' -%}
            {%- if item.OSPFDEADTIMER is not none -%}
                OSPFDEADTIMER={{item.OSPFDEADTIMER}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：OSPFENABLE=FALSE 时可选 --- -#}
        {%- if item.OSPFENABLE == 'FALSE' -%}
            {%- if item.OSPFGRPENABLE is not none -%}
                OSPFGRPENABLE={{item.OSPFGRPENABLE}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：OSPFENABLE=TRUE 时可选 --- -#}
        {%- if item.OSPFENABLE == 'TRUE' -%}
            {%- if item.OSPFHELLOTIMER is not none -%}
                OSPFHELLOTIMER={{item.OSPFHELLOTIMER}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：OSPFENABLE=TRUE 时可选 --- -#}
        {%- if item.OSPFENABLE == 'TRUE' -%}
            {%- if item.OSPFINSTID is not none -%}
                OSPFINSTID={{item.OSPFINSTID}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：TPINENABLE=TRUE 时可选 --- -#}
        {%- if item.TPINENABLE == 'TRUE' -%}
            {%- if item.TPINLINKFLAG is not none -%}
                TPINLINKFLAG={{item.TPINLINKFLAG}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：TPOUTENABLE=TRUE 时可选 --- -#}
        {%- if item.TPOUTENABLE == 'TRUE' -%}
            {%- if item.TPOUTLINKFLAG is not none -%}
                TPOUTLINKFLAG={{item.TPOUTLINKFLAG}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 如果规划外联口使用IPv4v6双栈地址，则分别执行该命令对同一外联口配置IPv4和IPv6地址。

### 7 打开自动配置开关。

```jinja2
{%- for item in set_autoconfig_list_1 -%}
    SET AUTOCONFIG:
    {#- --- 必选参数 --- -#}
    SWITCHFLAG={{item.SWITCHFLAG}},
    ;
{%- endfor -%}
```

### 从自动部署开关打开到自动部署功能生效有时延，因此执行其他操作前（例如手动部署路由互通、关闭自动部署开关），务必先执行****DSP OPSASSISTSTATE****命令查询自动部署维护助手“autoscaling\_autoconfig.py”的状态为“准备好状态（Ready）”，否则结果不可预期。


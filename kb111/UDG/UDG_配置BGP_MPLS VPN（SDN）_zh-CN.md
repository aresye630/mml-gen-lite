---
id: ''
name: 配置BGP/MPLS VPN（SDN）
ne_type: UDG
type: feature
description: SDN场景，UDG与企业网对接时，由于企业APN数量多，且各个企业APN之间有业务隔离诉求，故可采用BGP/MPLS VPN组网。UDG作为PE设备接入MPLS骨干网，通过MP-EBGP（Multi-protocol Extensions for Border Gateway Protocol）与其他PE之间传播VPN信息和VPN-IPv4路由。UDG采用OptionB方式实现跨域VPN。  如图1所示，UDG和PE间通过Loopback IP建立eBGP邻居，用于交换私网VPN路由。Loopback IP之间通过静态路由/OSPF互通。  **图1** BGP/MPLS VPN组网
risk_level: ''
doc_source: ["网络部署","初始配置","UDG初始配置与调测","组网路由配置","配置VNF侧IP路由（SDN）","配置BGP/MPLS VPN（SDN）"]
refs: []
metadata:
  DepOnLiveCfg: true
allowed-tools:
- getParameterValue('LST AUTOCONFIG')
---
<!-- @mml:block=annotations -->
```text
## 操作场景
SDN场景，UDG与企业网对接时，由于企业APN数量多，且各个企业APN之间有业务隔离诉求，故可采用BGP/MPLS VPN组网。UDG作为PE设备接入MPLS骨干网，通过MP-EBGP（Multi-protocol Extensions for Border Gateway Protocol）与其他PE之间传播VPN信息和VPN-IPv4路由。UDG采用OptionB方式实现跨域VPN。如图1所示，UDG和PE间通过Loopback IP建立eBGP邻居，用于交换私网VPN路由。Loopback IP之间通过静态路由/OSPF互通。**图1** BGP/MPLS VPN组网

## 必备事项
前提条件

* 请阅读并熟悉特性GWFD-020411 MPLS VPN、IPFD-014002 支持BGP和IPFD-012003 BFD特性概述。
* 具备管理员权限的操作人员已经登录华为操作维护系统。
* UDG与网络实体之间的网络环境已经构建完成。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
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
        NULLLABLETYPE:
          name: '空标签类型'
          type: string
          enum:
          - EXPLICIT_NULL
          - IMPLICIT_NULL
          - NON_NULL
          required: false
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
          description: 'SR-IOV bonding组网需要规划。  非SR-IOV bonding组网不需要规划。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        VNICLIST:
          name: '虚拟网卡ID列表'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: '参见“5G Core LLD文档 > 业务IP对接设计 > 虚拟网口”。'
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
          description: '“IPv4地址分配方式（IPALLOCTYPE4）”取值为“USER\_CONFIG”。  不需要规划“IPv6地址分配方式（IPALLOCTYPE6）”。MP-EBGP组网时，使用IPv4 eBGP，传递IPv6私网路由。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        VPNNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: '固定取值'
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
          data_source: '本端规划'
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
          data_source: '本端规划'
          pattern: ''
          default: USER_CONFIG
        AUTOCFGIFTYPE:
          name: '自动化配置接口类型'
          type: string
          enum:
          - ETHTRUNK
          - VNIC
          required: false
          description: '非SR-IOV bonding组网，自动化配置接口类型为VNIC；SR-IOV bonding组网，设置为ETHTRUNK。'
          data_source: '本端规划'
          pattern: ''
          default: VNIC
        VNICID:
          name: '虚拟网卡ID'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: false
          description: '-'
          data_source: '参见“5G Core LLD文档 > 业务IP对接设计 > 虚拟网口”。'
          pattern: ''
          default: ''
        VLANID:
          name: 'VLAN ID'
          type: integer
          minimum: 0
          maximum: 4094
          required: false
          description: '此处以双平面为例，单平面组网时，只需规划一条数据（例如只规划ServName\_N6\_100）。  此处规划的IP地址是与网关互通的外联口IP。  根据ISU VM的数量规划地址池掩码长度。  此处以25位掩码为例进行介绍，具体以网设规划为准。'
          data_source: '参见“5G Core LLD文档 > 业务IP对接设计 > VLAN ID（VM）”。'
          pattern: ''
          default: 0
        BEGINADDR4:
          name: '起始地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '参见“5G Core LLD文档 > 业务IP对接设计 > 起始IP”。'
          pattern: ''
          default: ''
        ENDADDR4:
          name: '结束地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '参见“5G Core LLD文档 > 业务IP对接设计 > 结束IP”。'
          pattern: ''
          default: ''
        MASKLEN:
          name: '地址池掩码长度'
          type: integer
          minimum: 1
          maximum: 128
          required: false
          description: ''
          data_source: '参见“5G Core LLD文档 > 业务IP对接设计 > 子网掩码”。'
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
    add_autoscalingservice_list_2:
      type: items
      properties:
        SERVICENAME:
          name: '服务名称'
          type: string
          maxLength: 31
          required: true
          description: '“IPv4地址分配方式（IPALLOCTYPE4）”取值为“USER\_CONFIG”。  不需要规划“IPv6地址分配方式（IPALLOCTYPE6）”。MP-EBGP组网时，使用IPv4 eBGP，传递IPv6私网路由。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        VPNNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: '固定取值'
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
          data_source: '本端规划'
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
          data_source: '本端规划'
          pattern: ''
          default: USER_CONFIG
        AUTOCFGIFTYPE:
          name: '自动化配置接口类型'
          type: string
          enum:
          - ETHTRUNK
          - VNIC
          required: false
          description: '非SR-IOV bonding组网，自动化配置接口类型为VNIC；SR-IOV bonding组网，设置为ETHTRUNK。'
          data_source: '本端规划'
          pattern: ''
          default: VNIC
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
        VLANID:
          name: 'VLAN ID'
          type: integer
          minimum: 0
          maximum: 4094
          required: false
          description: '此处以双平面为例，单平面组网时，只需规划一条数据（例如只规划ServName\_N6\_100）。  此处规划的IP地址是与网关互通的外联口IP。  根据ISU VM的数量规划地址池掩码长度。  此处以25位掩码为例进行介绍，具体以网设规划为准。'
          data_source: '参见“5G Core LLD文档 > 业务IP对接设计 > VLAN ID（VM）”。'
          pattern: ''
          default: 0
        BEGINADDR4:
          name: '起始地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '参见“5G Core LLD文档 > 业务IP对接设计 > 起始IP”。'
          pattern: ''
          default: ''
        ENDADDR4:
          name: '结束地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '参见“5G Core LLD文档 > 业务IP对接设计 > 结束IP”。'
          pattern: ''
          default: ''
        MASKLEN:
          name: '地址池掩码长度'
          type: integer
          minimum: 1
          maximum: 128
          required: false
          description: ''
          data_source: '参见“5G Core LLD文档 > 业务IP对接设计 > 子网掩码”。'
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
    add_autoscalingbfd_list:
      type: items
      properties:
        TEMPLATENAME:
          name: '模板名称'
          type: string
          maxLength: 59
          required: true
          description: '不需要规划“DESTADDR6”的BFD会话。MP-EBGP组网时，使用IPv4 eBGP，传递IPv6私网路由。  目的地址是PE的IP地址。'
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
          data_source: '本端规划'
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
          data_source: '本端规划'
          pattern: ''
          default: ''
        DESTADDR4:
          name: '目的地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '参见“5G Core LLD文档 > 路由设计 > BFD设计 > 对端IP地址”。'
          pattern: ''
          default: ''
        MINECHORXINT:
          name: '单臂Echo会话的收包间隔（ms）'
          type: integer
          minimum: 30
          maximum: 1000
          required: false
          description: ''
          data_source: '参见“5G Core LLD文档 > 路由设计 > BFD设计 > min-rx-interval(毫秒)”。'
          pattern: ''
          default: 200
        DETECTMULTI:
          name: '检测倍数'
          type: integer
          minimum: 3
          maximum: 50
          required: false
          description: ''
          data_source: '参见“5G Core LLD文档 > 路由设计 > BFD设计 > detect-multiplier”。'
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
          description: '“IPv4路由下一跳分配方式（NEXTHOPALLOCTYPE4）”取值为“CONFIG”。  “BFDENABLE”设置为“TRUE”，即采用单臂Echo。  请根据实际组网，规划IPv4路由前缀。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: '固定取值'
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
          description: ''
          data_source: '参见“5G Core LLD文档 > 路由设计 > BGP设计 > Local interface address（L3GW）”。'
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
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: CONFIG
        NEXTHOP4:
          name: '路由下一跳IPv4'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '从对端获取  参见“5G Core LLD文档 > 路由设计 > 静态路由设计 > 下一跳地址”。'
          pattern: ''
          default: ''
        PREFERENCE:
          name: '路由优先级'
          type: integer
          minimum: 1
          maximum: 255
          required: false
          description: ''
          data_source: '本端规划'
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
          data_source: '本端规划'
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
    add_autoscalingmpls_list:
      type: items
      properties:
        SERVICENAME:
          name: '服务名称'
          type: string
          maxLength: 31
          required: true
          description: '增加MPLS自动化配置模板，将外联口配置为MPLS接口。'
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
          description: 'MPLS OptionB必须配置“VRFRD”值。  不同VPN实例的路由标识必须不同。  此处以“VRFLABELMODE”设置为“perInstance”为例，即每VPN实例分配一个标签。设置为“perInstance”比设置为“perRoute”节省标签资源，可避免标签资源耗尽导致路由无法正常发布。  PE设备上的实例的标签分配模式须和UDG上的一致。'
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
        VRFLABEL:
          name: '实例的标签值'
          type: integer
          minimum: 16
          maximum: 32767
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
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
          description: 'MPLS OptionB必须配置“VRFRD”值。  不同VPN实例的路由标识必须不同。  此处以“VRFLABELMODE”设置为“perInstance”为例，即每VPN实例分配一个标签。设置为“perInstance”比设置为“perRoute”节省标签资源，可避免标签资源耗尽导致路由无法正常发布。  PE设备上的实例的标签分配模式须和UDG上的一致。'
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
        VRFLABEL:
          name: '实例的标签值'
          type: integer
          minimum: 16
          maximum: 32767
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
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
          description: 'Loopback接口IP用于和BGP peer建立BGP邻居。  不能与已存在的Loopback接口名称重复。  请根据实际组网，规划IPv4地址。使用IPv4 eBGP，传递IPv6私网路由。Loopback接口不需要规划IPv6地址。  Loopback接口不用绑定VPN，即用公网BGP传递私网路由。'
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
          description: 'Loopback接口IP用于和BGP peer建立BGP邻居。  不能与已存在的Loopback接口名称重复。  请根据实际组网，规划IPv4地址。使用IPv4 eBGP，传递IPv6私网路由。Loopback接口不需要规划IPv6地址。  Loopback接口不用绑定VPN，即用公网BGP传递私网路由。'
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
          description: 'BGP VPN实例需要与ADD L3VPNINST命令配置的VPN实例名一致。'
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
          description: '是MP-EBGP的开关。  请根据实际组网，规划ipv4vpn、ipv6vpn或ipv4vpn&ipv6vpn的BGP VPN实例地址族。'
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
          description: 'ADD VPNINSTAF命令中的“VRFLABELMODE”设置为“perInstance”时，“APPLYLABELMODE”需要设置为“perNexthop”，可避免标签资源耗尽导致路由无法正常发布。  PE设备上的标签分配方式须和UDG上的一致。'
          data_source: '本端规划'
          pattern: ''
          default: perRoute
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
    add_bgpvrfaf_list_1:
      type: items
      properties:
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: false
          description: '是MP-EBGP的开关。  请根据实际组网，规划ipv4vpn、ipv6vpn或ipv4vpn&ipv6vpn的BGP VPN实例地址族。'
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
          description: 'ADD VPNINSTAF命令中的“VRFLABELMODE”设置为“perInstance”时，“APPLYLABELMODE”需要设置为“perNexthop”，可避免标签资源耗尽导致路由无法正常发布。  PE设备上的标签分配方式须和UDG上的一致。'
          data_source: '本端规划'
          pattern: ''
          default: perRoute
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
    add_bgpvrfaf_list_2:
      type: items
      properties:
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: false
          description: 'BGP VPN实例需要与ADD BGPVRF命令配置的VPN实例名一致。'
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
    add_bgpvrfaf_list_7:
      type: items
      properties:
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: false
          description: 'BGP VPN实例需要与ADD BGPVRF命令配置的VPN实例名一致。'
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
          description: '“EBGP最大跳数”不小于到Peer之间的实际跳数，无法确认时，可设置为10。  如最大跳数设置过小，会导致BGP邻居建立失败。  请根据实际组网，规划IPv4对等体地址。  不需要规划IPv6对等体地址。MP-EBGP组网时，使用IPv4 eBGP，传递IPv6私网路由。'
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
          description: '与ADD BGPPEER命令中配置的BGP对等体地址相同。'
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
          default: 'null'
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
          default: FALSE
        ADVERTISECOMMUNITY:
          name: '团体属性发布'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
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
          default: FALSE
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
          default: FALSE
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
          default: FALSE
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
          default: 'null'
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
          default: FALSE
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
          default: FALSE
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
          default: FALSE
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
          default: FALSE
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
          default: 'null'
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
          default: 0
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
          default: FALSE
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
          default: FALSE
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
          default: FALSE
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
          default: FALSE
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
          default: FALSE
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
          default: 75
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
          default: noparameter
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
          default: FALSE
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
          description: '与ADD BGPPEER命令中配置的BGP对等体地址相同。'
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
          default: 'null'
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
          default: FALSE
        ADVERTISECOMMUNITY:
          name: '团体属性发布'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
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
          default: FALSE
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
          default: FALSE
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
          default: FALSE
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
          default: 'null'
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
          default: FALSE
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
          default: FALSE
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
          default: FALSE
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
          default: FALSE
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
          default: 'null'
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
          default: 0
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
          default: FALSE
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
          default: FALSE
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
          default: FALSE
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
          default: FALSE
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
          default: FALSE
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
          default: 75
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
          default: noparameter
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
          default: FALSE
    add_importroute_list:
      type: items
      properties:
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: false
          description: '使用ADD BGPVRF命令定义的VPN实例名称。  请根据实际组网，规划引入ipv4uni、ipv6uni或ipv4uni&ipv6uni的wlr路由。'
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
    add_importroute_list_5:
      type: items
      properties:
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: false
          description: '使用ADD BGPVRF命令定义的VPN实例名称。  请根据实际组网，规划引入ipv4uni、ipv6uni或ipv4uni&ipv6uni的wlr路由。'
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
  examples:
    set_bfd_list:
    - BFDENABLE: TRUE
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
    set_mplssite_list:
    - MPLSLSRID: '10.10.10.78'
      MPLSENABLE: ENABLE
      LDPENABLE: DISABLE
      NULLLABLETYPE: ''
    set_autoconfig_list:
    - SWITCHFLAG: FALSE
    add_autoscalingethtrunk_list:
    - ETHTRUNKTMPID: 1
      VNICLIST: '4 5'
    add_autoscalingservice_list:
    - SERVICENAME: 'ServName_N6_100'
      VPNNAME: '_public_'
      AFTYPE: IPv4
      IPALLOCTYPE4: USER_CONFIG
      AUTOCFGIFTYPE: VNIC
      VNICID: 4
      VLANID: 100
      BEGINADDR4: '192.168.89.2'
      ENDADDR4: '192.168.89.126'
      MASKLEN: 25
      IPALLOCTYPE6: USER_CONFIG
      ETHTRUNKTMPID: ''
    add_autoscalingservice_list_2:
    - SERVICENAME: 'ServName_N6_100'
      VPNNAME: '_public_'
      AFTYPE: IPv4
      IPALLOCTYPE4: USER_CONFIG
      AUTOCFGIFTYPE: ETHTRUNK
      ETHTRUNKTMPID: 1
      VLANID: 100
      BEGINADDR4: '192.168.89.2'
      ENDADDR4: '192.168.89.126'
      MASKLEN: 25
      IPALLOCTYPE6: USER_CONFIG
      VNICID: ''
    add_autoscalingbfd_list:
    - TEMPLATENAME: 'BFD_1'
      BFDTYPE: Static
      SERVICENAME: 'ServName_N6_100'
      IPVERSION: IPv4
      DESTADDR4: '192.168.89.1'
      MINECHORXINT: 500
      DETECTMULTI: 4
      ONEARMECHO: TRUE
      MINRXINTERVAL: 200
      MINTXINTERVAL: 200
      DESTADDR6: ''
    add_autoscalingsrroute_list:
    - SERVICENAME: 'ServName_N6_100'
      VRFNAME: '_public_'
      IPVERSION: IPv4
      PREFIX4: '10.10.20.78'
      MASKLENGTH: 32
      NEXTHOPALLOCTYPE4: CONFIG
      NEXTHOP4: '192.168.89.1'
      PREFERENCE: 60
      BFDENABLE: TRUE
      BFDTEMPLATENAME: 'BFD_1'
      NEXTHOPALLOCTYPE6: CONFIG
      PREFIX6: ''
    add_autoscalingmpls_list:
    - SERVICENAME: 'ServName_N6_100'
    set_autoconfig_list_1:
    - SWITCHFLAG: TRUE
    add_l3vpninst_list:
    - VRFNAME: 'VRF_PDN1'
    add_vpninstaf_list:
    - VRFNAME: 'VRF_PDN1'
      AFTYPE: ipv4uni
      VRFRD: '100:100'
      VRFLABELMODE: perInstance
      VRFLABEL: ''
    add_vpninstaf_list_5:
    - VRFNAME: 'VRF_PDN1'
      AFTYPE: ipv6uni
      VRFRD: '100:100'
      VRFLABELMODE: perInstance
      VRFLABEL: ''
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
      ACTIVEROUTEADVERTISE: FALSE
      ADDPATHSELNUM: ''
      ALWAYSCOMPAREMED: FALSE
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
      MAXIMUMLOADBALANCE: 1
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
    add_bgpvrfaf_list_1:
    - VRFNAME: '_public_'
      AFTYPE: ipv6vpn
      APPLYLABELMODE: perNexthop
      ACTIVEROUTEADVERTISE: FALSE
      ADDPATHSELNUM: ''
      ALWAYSCOMPAREMED: FALSE
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
      MAXIMUMLOADBALANCE: 1
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
    add_bgpvrfaf_list_2:
    - VRFNAME: 'VRF_PDN1'
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
    add_bgpvrfaf_list_7:
    - VRFNAME: 'VRF_PDN1'
      AFTYPE: ipv6uni
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
    - VRFNAME: '_public_'
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
      ADDPATHMODE: 'null'
      ADVADDPATHNUM: ''
      ADVBESTEXTERNAL: FALSE
      ADVERTISECOMMUNITY: FALSE
      ADVERTISEEXTCOMMUNITY: FALSE
      ALLOWASLOOPENABLE: FALSE
      ALLOWASLOOPLIMIT: ''
      DEFAULTRTADVENABLE: FALSE
      DEFAULTRTADVPOLICY: ''
      DEFAULTRTMATCHMODE: 'null'
      DISCARDEXTCOMMUNITY: FALSE
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
      INCLUDEPEERAS: FALSE
      ISSOURELAYNEIGHINTER: FALSE
      KEEPALLROUTES: FALSE
      NEXTHOPCONFIGURE: 'null'
      PEERGROUPNAME: ''
      PREFERREDVALUE: ''
      PUBLICASONLY: FALSE
      PUBLICASONLYFORCE: FALSE
      PUBLICASONLYLIMITED: FALSE
      PUBLICASONLYREPLACE: FALSE
      REFLECTCLIENT: FALSE
      ROUTELIMIT: ''
      ROUTELIMITIDLETIMEOUT: ''
      ROUTELIMITPERCENT: 75
      ROUTELIMITTYPE: noparameter
      RTUPDTINTERVAL: ''
      SUBSTITUTEASENABLE: FALSE
    add_bgppeeraf_list_2:
    - VRFNAME: '_public_'
      AFTYPE: ipv6vpn
      REMOTEADDRESS: '10.10.20.78'
      ADDRESSTYPE: ipv4
      ADDPATHMODE: 'null'
      ADVADDPATHNUM: ''
      ADVBESTEXTERNAL: FALSE
      ADVERTISECOMMUNITY: FALSE
      ADVERTISEEXTCOMMUNITY: FALSE
      ALLOWASLOOPENABLE: FALSE
      ALLOWASLOOPLIMIT: ''
      DEFAULTRTADVENABLE: FALSE
      DEFAULTRTADVPOLICY: ''
      DEFAULTRTMATCHMODE: 'null'
      DISCARDEXTCOMMUNITY: FALSE
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
      INCLUDEPEERAS: FALSE
      ISSOURELAYNEIGHINTER: FALSE
      KEEPALLROUTES: FALSE
      NEXTHOPCONFIGURE: 'null'
      PEERGROUPNAME: ''
      PREFERREDVALUE: ''
      PUBLICASONLY: FALSE
      PUBLICASONLYFORCE: FALSE
      PUBLICASONLYLIMITED: FALSE
      PUBLICASONLYREPLACE: FALSE
      REFLECTCLIENT: FALSE
      ROUTELIMIT: ''
      ROUTELIMITIDLETIMEOUT: ''
      ROUTELIMITPERCENT: 75
      ROUTELIMITTYPE: noparameter
      RTUPDTINTERVAL: ''
      SUBSTITUTEASENABLE: FALSE
    add_importroute_list:
    - VRFNAME: 'VRF_PDN1'
      AFTYPE: ipv4uni
      IMPORTPROTOCOL: wlr
      MEDENABLE: FALSE
      IMPORTPROCESSID: ''
      MED: ''
    add_importroute_list_5:
    - VRFNAME: 'VRF_PDN1'
      AFTYPE: ipv6uni
      IMPORTPROTOCOL: wlr
      MEDENABLE: FALSE
      IMPORTPROCESSID: ''
      MED: ''
```

## 3 命令模板定义
<!-- @mml:block=commands -->

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
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：MPLSENABLE=ENABLE 时可选 --- -#}
    {%- if item.MPLSENABLE == 'ENABLE' -%}
        {%- if item.NULLLABLETYPE is not none -%}
            NULLLABLETYPE={{item.NULLLABLETYPE}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 关闭自动配置开关。

#### 4.1 查询自动配置开关。

#### 如果“自动配置开关”值为“TRUE”，需要执行4.b和4.c关闭自动配置开关。

#### 如果“自动配置开关”值为“FALSE”，说明已关闭自动配置开关，请跳转到步骤 5。

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

### 如果要实现SR-IOV接口bonding功能，那么一个Eth-trunk接口下的两个成员接口必须MAC相同，且ID号连续。即：“VNICLIST”中配置的ID号为MAC相同且连续的两个以太网接口的ID。可使用**LST INTERFACE**命令查询以太网接口的MAC地址与以太网接口名称。

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
        {#- --- 条件必选：IPALLOCTYPE4=USER_CONFIG 时必选 --- -#}
        {%- if item.IPALLOCTYPE4 == 'USER_CONFIG' -%}
            MASKLEN={{item.MASKLEN}},
        {#- --- 条件必选：IPALLOCTYPE6=USER_CONFIG 时必选 --- -#}
        {%- elif item.IPALLOCTYPE6 == 'USER_CONFIG' -%}
            MASKLEN={{item.MASKLEN}},
        {%- endif -%}
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

#### “VRFNAME”使用默认值“\_public\_”。外联口不需要配置IPv6地址。

### 7 增加BFD会话自动部署模板。

### “DESTADDR4”配置的是PE的IP地址，采用的是单臂BFD。不需要配置IPv6 BFD会话。

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

### “VRFNAME”使用默认值“\_public\_”。不需要配置IPv6路由。

### 9 增加MPLS自动化配置模板（使能接口的MPLS功能）。

```jinja2
{%- for item in add_autoscalingmpls_list -%}
    ADD AUTOSCALINGMPLS:
    {#- --- 必选参数 --- -#}
    SERVICENAME="{{item.SERVICENAME}}",
    ;
{%- endfor -%}
```

### 10 打开自动部署开关。

```jinja2
{%- for item in set_autoconfig_list_1 -%}
    SET AUTOCONFIG:
    {#- --- 必选参数 --- -#}
    SWITCHFLAG={{item.SWITCHFLAG}},
    ;
{%- endfor -%}
```

### 从自动部署开关打开到自动部署功能生效有时延，因此执行其他操作前（例如手动部署路由互通、关闭自动部署开关），务必先执行**DSP OPSASSISTSTATE**命令查询自动部署维护助手“autoscaling\_autoconfig.py”的状态为“准备好状态（Ready）”，否则结果不可预期。

### 11 配置VPN实例及VPN实例地址族。

```jinja2
{%- for item in add_l3vpninst_list -%}
    ADD L3VPNINST:
    {#- --- 必选参数 --- -#}
    VRFNAME="{{item.VRFNAME}}",
    ;
{%- endfor -%}
```

#### 11.1 //IPv4组网或IPv4v6组网，请执行如下脚本：

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
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：VRFLABELMODE=perInstanceStatic 时可选 --- -#}
        {%- if item.VRFLABELMODE == 'perInstanceStatic' -%}
            {%- if item.VRFLABEL is not none -%}
                VRFLABEL={{item.VRFLABEL}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 11.2 //IPv6组网或IPv4v6组网，请执行如下脚本：

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
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：VRFLABELMODE=perInstanceStatic 时可选 --- -#}
        {%- if item.VRFLABELMODE == 'perInstanceStatic' -%}
            {%- if item.VRFLABEL is not none -%}
                VRFLABEL={{item.VRFLABEL}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 12 配置VPN Target。

#### 12.1 //IPv4组网或IPv4v6组网，请执行如下脚本：

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

#### 12.2 //IPv6组网或IPv4v6组网，请执行如下脚本：

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

### 13 配置Loopback接口（BGP本端IP）。

#### 13.1 配置Loopback接口。

```jinja2
{%- for item in add_interface_list -%}
    ADD INTERFACE:
    {#- --- 必选参数 --- -#}
    IFNAME="{{item.IFNAME}}",
    ;
{%- endfor -%}
```

#### 13.2 增加接口IPv4地址。

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

### 14 配置BGP。

#### 14.1 修改公网BGP VPN实例。

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

#### 14.2 增加BGP VPN实例。

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

#### 14.3 增加BGP VPN实例地址族（使能MP-EBGP功能）。“VRFNAME”使用默认值“\_public\_”。

##### 14.3.1 //IPv4组网或IPv4v6组网，请执行如下脚本：

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
            {%- if item.MAXIMUMLOADBALANCE is not none -%}
                MAXIMUMLOADBALANCE={{item.MAXIMUMLOADBALANCE}},
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
{%- endif -%}
```

##### 14.3.2 //IPv6组网或IPv4v6组网，请执行如下脚本：

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
            {%- if item.MAXIMUMLOADBALANCE is not none -%}
                MAXIMUMLOADBALANCE={{item.MAXIMUMLOADBALANCE}},
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
{%- endif -%}
```

##### “AFTYPE”设置为“ipv4vpn”/“ipv6vpn”。

#### 14.4 增加BGP VPN地址族。VNF对接2个负荷分担的BGP邻居时，“MAXIMUMLOADBALANCE”设置为“2”。

##### 14.4.1 //IPv4组网或IPv4v6组网，请执行如下脚本：

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
{%- endif -%}
```

##### 14.4.2 //IPv6组网或IPv4v6组网，请执行如下脚本：

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
{%- endif -%}
```

#### 14.5 增加BGP对等体。

##### 14.5.1 //“VRFNAME”使用默认值“\_public\_”。使用IPv4 BGP传递IPv6路由，不需要配置IPv6的BGP对等体。

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

##### 14.5.2 //（可选）执行**ADD BGPPEER**时，若“VRFNAME”使用默认值“\_public\_”，则会自动生成ipv4uni类型的对等体地址族。如局点不需要创建ipv4uni类型的对等体地址族，可执行如下脚本进行删除。

```jinja2
{%- if is_optional_remove_ipv4uni_peeraf -%}
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
        {#- --- 条件必选：AFTYPE=ipv6uni 时必选 --- -#}
        {%- if item.AFTYPE == 'ipv6uni' -%}
            ADDRESSTYPE={{item.ADDRESSTYPE}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 14.6 配置BGP对等体地址族。

##### 14.6.1 //IPv4组网或IPv4v6组网，请执行如下脚本：

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
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：AFTYPE=ipv4uni/ipv4vpn/ipv6vpn 时可选 --- -#}
        {%- if item.AFTYPE in ['ipv4uni', 'ipv4vpn', 'ipv6vpn'] -%}
            {%- if item.ADDPATHMODE is not none -%}
                ADDPATHMODE={{item.ADDPATHMODE}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：AFTYPE=ipv6uni 时可选 --- -#}
        {%- if item.AFTYPE == 'ipv6uni' -%}
            {%- if item.ADDRESSTYPE is not none -%}
                ADDRESSTYPE={{item.ADDRESSTYPE}},
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
            {%- if item.ADVERTISECOMMUNITY is not none -%}
                ADVERTISECOMMUNITY={{item.ADVERTISECOMMUNITY}},
            {%- endif -%}
        {#- --- 条件可选：AFTYPE=ipv4uni/ipv4vpn/ipv6vpn 时可选 --- -#}
        {%- elif item.AFTYPE in ['ipv4uni', 'ipv4vpn', 'ipv6vpn'] -%}
            {%- if item.ADVERTISECOMMUNITY is not none -%}
                ADVERTISECOMMUNITY={{item.ADVERTISECOMMUNITY}},
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

##### 14.6.2 //IPv6组网或IPv4v6组网，请执行如下脚本：

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
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：AFTYPE=ipv4uni/ipv4vpn/ipv6vpn 时可选 --- -#}
        {%- if item.AFTYPE in ['ipv4uni', 'ipv4vpn', 'ipv6vpn'] -%}
            {%- if item.ADDPATHMODE is not none -%}
                ADDPATHMODE={{item.ADDPATHMODE}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：AFTYPE=ipv6uni 时可选 --- -#}
        {%- if item.AFTYPE == 'ipv6uni' -%}
            {%- if item.ADDRESSTYPE is not none -%}
                ADDRESSTYPE={{item.ADDRESSTYPE}},
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
            {%- if item.ADVERTISECOMMUNITY is not none -%}
                ADVERTISECOMMUNITY={{item.ADVERTISECOMMUNITY}},
            {%- endif -%}
        {#- --- 条件可选：AFTYPE=ipv4uni/ipv4vpn/ipv6vpn 时可选 --- -#}
        {%- elif item.AFTYPE in ['ipv4uni', 'ipv4vpn', 'ipv6vpn'] -%}
            {%- if item.ADVERTISECOMMUNITY is not none -%}
                ADVERTISECOMMUNITY={{item.ADVERTISECOMMUNITY}},
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

#### 14.7 增加BGP引入wlr路由。

##### 14.7.1 //IPv4组网或IPv4v6组网，请执行如下脚本：

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
{%- endif -%}
```

##### 14.7.2 //IPv6组网或IPv4v6组网，请执行如下脚本：

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
{%- endif -%}
```

##### 由于BGP协议自身不能发现路由，所以需要引入其他协议的路由（如OSPF、静态路由或WLR等）注入到BGP路由表中，从而将这些路由在AS之内和AS之间传播。


---
id: GWFD-020423
name: 激活路由交叉功能
ne_type: UDG
type: feature
description: UE激活后，能正常访问网络A中的服务器。另一网络B和网络A之间网络隔离，UE还需访问网络B中的指定服务器（服务器IP需固定，此处IP地址以10.8.8.8为例）。  该场景下，网络A和网络B是两个不同的VPN网络，需通过路由交叉功能，实现UE激活后，既能访问网络A中的服务器，又能访问网络B中的定制服务器。  组网示意如图1所示。  **图1** 路由交叉应用场景示意
risk_level: ''
doc_source: ["特性部署","特性指南","UDG特性指南","组网功能","GWFD-020423 支持路由交叉功能","激活路由交叉功能"]
refs: []
metadata:
  DepOnLiveCfg: true
allowed-tools:
- getParameterValue('LST AUTOCONFIG')
---
<!-- @mml:block=annotations -->
```text
## 操作场景
UE激活后，能正常访问网络A中的服务器。另一网络B和网络A之间网络隔离，UE还需访问网络B中的指定服务器（服务器IP需固定，此处IP地址以10.8.8.8为例）。该场景下，网络A和网络B是两个不同的VPN网络，需通过路由交叉功能，实现UE激活后，既能访问网络A中的服务器，又能访问网络B中的定制服务器。组网示意如图1所示。**图1** 路由交叉应用场景示意

## 必备事项
前提条件

* 请仔细阅读GWFD-020423 支持路由交叉功能特性概述。
* 已完成UE访问网络A中的服务器的相关配置。
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
          description: '复用**ADD L3VPNINST**命令中定义的值。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        AFTYPE:
          name: '地址族名称'
          type: string
          enum:
          - ipv4uni
          - ipv6uni
          required: true
          description: '-'
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
          description: '此处以SR-IOV bonding组网下，复用N6其他VRF的vNIC接口为例。  可通过命令**LST AUTOSCALINGETHTRUNK**查询获取。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        VLANID:
          name: 'VLAN ID'
          type: integer
          minimum: 0
          maximum: 4094
          required: false
          description: '此处以单平面组网为例。  此处规划的IP地址是与网关互通的外联口IP。  根据ISU VM的数量规划地址池掩码长度。  此处以25位掩码为例进行介绍，具体以网设规划为准。'
          data_source: '全网规划'
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
    add_autoscalingsrbfd_list:
      type: items
      properties:
        SERVICENAME:
          name: '服务名称'
          type: string
          maxLength: 31
          required: true
          description: 'BFD双向检测时需要规划。'
          data_source: '已规划数据中获取'
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
          data_source: '已规划数据中获取'
          pattern: ''
          default: IPv4
        MINRXINTERVAL:
          name: '最小接收间隔（ms）'
          type: integer
          minimum: 30
          maximum: 1000
          required: false
          description: ''
          data_source: '参见“5G Core LLD文档 > 路由设计 > BFD设计 > min-rx-interval(毫秒)”。'
          pattern: ''
          default: ''
        MINTXINTERVAL:
          name: '最小发送间隔（ms）'
          type: integer
          minimum: 30
          maximum: 1000
          required: false
          description: ''
          data_source: '参见“5G Core LLD文档 > 路由设计 > BFD设计 > min-tx-interval(毫秒)”。'
          pattern: ''
          default: ''
        MULTIPLIER:
          name: '检测倍数'
          type: integer
          minimum: 3
          maximum: 50
          required: false
          description: ''
          data_source: '参见“5G Core LLD文档 > 路由设计 > BFD设计 > detect-multiplier”。'
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
          description: 'BFD单臂echo检测时需要规划。  参数“目的地址”是网关的接口IP，此处用于检测目的IP能否正常接收报文。'
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
          data_source: '参见“5G Core LLD文档 > 路由设计 > BFD设计 > BFD类型”。  “BFD类型”为“BFD Echo”/“单臂BFD”时，该参数设置为“TRUE”。'
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
          description: '采用**ADD AUTOSCALINGSERVICE**命令定的服务名称。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: false
          description: 'UPF上，与网络A互通的接口绑定的VPN实例名称。  可通过**LST L3VPNINST**查询获取。'
          data_source: '整网规划'
          pattern: ''
          default: '_public_'
        IPVERSION:
          name: '地址族'
          type: string
          enum:
          - IPv4
          - IPv6
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PREFIX4:
          name: '路由前缀IPv4'
          type: string
          maxLength: 15
          required: false
          description: '对端服务器的IP地址及掩码。  须知会到服务器，该地址变更时必须与UPF协商，否则可能出现访问该服务器的业务失败。'
          data_source: '从对端获取'
          pattern: ''
          default: ''
        MASKLENGTH:
          name: '路由掩码长度'
          type: integer
          minimum: 0
          maximum: 128
          required: true
          description: ''
          data_source: '从对端获取'
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
          data_source: '本端规划'
          pattern: ''
          default: CONFIG
        NEXTHOP4:
          name: '路由下一跳IPv4'
          type: string
          maxLength: 15
          required: false
          description: '网关接口IP。  UPF将与网络B互通的报文，发送给该IP所属的直连交换机/路由器。'
          data_source: '从对端获取'
          pattern: ''
          default: ''
        BFDENABLE:
          name: 'BFD使能标识'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: '双向BFD探测或单向BFD探测时均需设置为样例值。'
          data_source: '本端规划'
          pattern: ''
          default: FALSE
        BFDTEMPLATENAME:
          name: 'BFD模板名称'
          type: string
          maxLength: 59
          required: false
          description: '单臂BFD探测时需要规划。  表1中**ADD AUTOSCALINGBFD**命令定义的BFD模板名称。'
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
    mod_vpninstaf_list:
      type: items
      properties:
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: true
          description: 'UPF上，与网络A互通的接口绑定的VPN实例名称。  可通过**LST L3VPNINST**查询获取。'
          data_source: '整网规划'
          pattern: ''
          default: ''
        AFTYPE:
          name: '地址族名称'
          type: string
          enum:
          - ipv4uni
          - ipv6uni
          required: true
          description: '-'
          data_source: '本端规划'
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
          default: ''
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
          description: 'UPF上，与网络A互通的接口绑定的VPN实例名称。  可通过**LST L3VPNINST**查询获取。'
          data_source: '整网规划'
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
          data_source: '本端规划'
          pattern: ''
          default: ''
        VRFRTTYPE:
          name: 'VPN RT类型'
          type: string
          enum:
          - export_extcommunity
          - import_extcommunity
          required: true
          description: '对于VPN实例VRF\_networkA的路由，UPF增加发布扩展属性及RT值。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        VRFRTVALUE:
          name: 'VPN RT值'
          type: string
          maxLength: 21
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
          description: 'UDG上如已使能BGP，此处不需要重复规划。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        ASNUM:
          name: 'BGP自治域号'
          type: string
          maxLength: 11
          required: false
          description: ''
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
    add_bgpvrf_list:
      type: items
      properties:
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: true
          description: 'UPF上，与网络A互通的接口绑定的VPN实例名称。  可通过**LST L3VPNINST**查询获取。'
          data_source: '整网规划'
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
          data_source: '本端规划'
          pattern: ''
          default: ipv4uni
        VRFRIDAUTOSEL:
          name: 'VPN路由器ID自动选择'
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
          description: 'UPF上，与网络A互通的接口绑定的VPN实例名称。  可通过**LST L3VPNINST**查询获取。'
          data_source: '整网规划'
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
          description: '采用样例值。'
          data_source: '本端规划'
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
    mod_vpninstaf_list_1:
      type: items
      properties:
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: true
          description: 'UPF上，与网络B互通的接口绑定的VPN实例名称。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        AFTYPE:
          name: '地址族名称'
          type: string
          enum:
          - ipv4uni
          - ipv6uni
          required: true
          description: '-'
          data_source: '本端规划'
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
          default: ''
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
    add_vpntarget_list_1:
      type: items
      properties:
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: true
          description: 'UPF上，与网络B互通的接口绑定的VPN实例名称。'
          data_source: '整网规划'
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
          data_source: '本端规划'
          pattern: ''
          default: ''
        VRFRTTYPE:
          name: 'VPN RT类型'
          type: string
          enum:
          - export_extcommunity
          - import_extcommunity
          required: true
          description: '对于VPN实例VRF\_networkB，UPF增加引入扩展属性及RT值。  当RT类型为“import\_extcommunity”时，UPF判断其他VPN实例（如VRF\_networkA）路由中的团体属性为发布，且RT值与此处配置的RT值相同时，则将VRF\_networkA中的该条路由加入到本VPN实例的路由表中。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        VRFRTVALUE:
          name: 'VPN RT值'
          type: string
          maxLength: 21
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
  examples:
    add_l3vpninst_list:
    - VRFNAME: 'VRF_networkB'
    add_vpninstaf_list:
    - VRFNAME: 'VRF_networkB'
      AFTYPE: ipv4uni
    set_autoconfig_list:
    - SWITCHFLAG: FALSE
    add_autoscalingservice_list:
    - SERVICENAME: 'ServName_networkB'
      VPNNAME: 'VPN_networkB'
      AFTYPE: IPv4
      IPALLOCTYPE4: USER_CONFIG
      AUTOCFGIFTYPE: ETHTRUNK
      ETHTRUNKTMPID: 6
      VLANID: 20
      BEGINADDR4: '192.168.20.2'
      ENDADDR4: '192.168.20.126'
      MASKLEN: 25
      IPALLOCTYPE6: USER_CONFIG
      VNICID: ''
    add_autoscalingsrbfd_list:
    - SERVICENAME: 'ServName_networkB'
      IPVERSION: IPv4
      MINRXINTERVAL: 500
      MINTXINTERVAL: 500
      MULTIPLIER: 4
    add_autoscalingbfd_list:
    - TEMPLATENAME: 'BFD_10'
      BFDTYPE: Static
      SERVICENAME: 'ServName_networkB'
      IPVERSION: IPv4
      DESTADDR4: '192.168.20.1'
      MINECHORXINT: 500
      DETECTMULTI: 4
      ONEARMECHO: TRUE
      MINRXINTERVAL: 200
      MINTXINTERVAL: 200
      DESTADDR6: ''
    add_autoscalingsrroute_list:
    - SERVICENAME: 'ServName_networkB'
      VRFNAME: 'VRF_networkA'
      IPVERSION: IPv4
      PREFIX4: '10.8.8.8'
      MASKLENGTH: 32
      NEXTHOPALLOCTYPE4: CONFIG
      NEXTHOP4: '192.168.20.1'
      BFDENABLE: TRUE
      BFDTEMPLATENAME: 'BFD_10'
      NEXTHOPALLOCTYPE6: CONFIG
      PREFIX6: ''
    set_autoconfig_list_1:
    - SWITCHFLAG: TRUE
    mod_vpninstaf_list:
    - VRFNAME: 'VRF_networkA'
      AFTYPE: ipv4uni
      VRFRD: '1:1'
      VRFLABELMODE: perInstance
      VRFLABEL: ''
    add_vpntarget_list:
    - VRFNAME: 'VRF_networkA'
      AFTYPE: ipv4uni
      VRFRTTYPE: export_extcommunity
      VRFRTVALUE: '1:1'
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
    add_bgpvrf_list:
    - VRFNAME: 'VRF_networkA'
      DEFAULTAFTYPE: ipv4uni
      VRFRIDAUTOSEL: FALSE
    add_importroute_list:
    - VRFNAME: 'VRF_networkA'
      AFTYPE: ipv4uni
      IMPORTPROTOCOL: wlr
      MEDENABLE: FALSE
      IMPORTPROCESSID: ''
      MED: ''
    mod_vpninstaf_list_1:
    - VRFNAME: 'VRF_networkB'
      AFTYPE: ipv4uni
      VRFRD: '2:2'
      VRFLABELMODE: perInstance
      VRFLABEL: ''
    add_vpntarget_list_1:
    - VRFNAME: 'VRF_networkB'
      AFTYPE: ipv4uni
      VRFRTTYPE: import_extcommunity
      VRFRTVALUE: '1:1'
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
    ;
{%- endfor -%}
```

### 2 关闭自动配置开关。

#### 2.1 查询自动配置开关。

#### 如果自动配置开关值为“TRUE”，需要执行如下步骤关闭自动配置开关。

#### 2.2 （可选）查询自动部署维护助手“autoscaling\_autoconfig.py”的状态，确保状态为“准备好状态（Ready）”或者查询无该脚本，以保证当前设备不在自动部署过程中。因为若系统当前有正在进行的自动部署，而自动部署生效有时延，此时若关闭自动配置开关，会影响系统配置效果。

#### 2.3 （可选）关闭自动配置开关。自动化配置命令只有在自动配置开关为关闭的状态下才可执行，因此需要提前关闭。

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

### 3 配置外联口自动部署模板。

#### 3.1 //如下脚本以SR-IOV bonding组网为例。SR-IOV bonding组网时，“AUTOCFGIFTYPE”取值为“ETHTRUNK”；非SR-IOV bonding组网时，“AUTOCFGIFTYPE”取值为“VNIC”。

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
```

### 4 配置BFD会话。

#### 4.1 BFD双向检测时：

```jinja2
{%- if is_scenario_bfd_bidirectional -%}
    {%- for item in add_autoscalingsrbfd_list -%}
        ADD AUTOSCALINGSRBFD:
        {#- --- 必选参数 --- -#}
        SERVICENAME="{{item.SERVICENAME}}",
        {#- --- 可选参数 --- -#}
        {%- if item.IPVERSION is not none -%}
            IPVERSION={{item.IPVERSION}},
        {%- endif -%}
        {%- if item.MINRXINTERVAL is not none -%}
            MINRXINTERVAL={{item.MINRXINTERVAL}},
        {%- endif -%}
        {%- if item.MINTXINTERVAL is not none -%}
            MINTXINTERVAL={{item.MINTXINTERVAL}},
        {%- endif -%}
        {%- if item.MULTIPLIER is not none -%}
            MULTIPLIER={{item.MULTIPLIER}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 4.2 BFD 单臂echo检测时：

```jinja2
{%- if is_scenario_bfd_one_arm_echo -%}
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
{%- endif -%}
```

### 5 配置路由交叉相关数据（上行路由）。

#### 5.1 //此处以采用单向BFD为例。采用BFD双向检测时，不需要配置BFDTEMPLATENAME参数。

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

### 6 打开自动配置开关。

```jinja2
{%- for item in set_autoconfig_list_1 -%}
    SET AUTOCONFIG:
    {#- --- 必选参数 --- -#}
    SWITCHFLAG={{item.SWITCHFLAG}},
    ;
{%- endfor -%}
```

### 从自动部署开关打开到自动部署功能生效有时延，因此执行其他操作前（例如手动部署路由互通、关闭自动部署开关），务必先执行****DSP OPSASSISTSTATE****命令查询自动部署维护助手“autoscaling\_autoconfig.py”的状态为“准备好状态（Ready）”，否则结果不可预期。

### 在网关侧上配置到VNF的回程路由，目的地址为VNF上各逻辑接口的IP地址，下一跳为VNF上配置的各逻辑接口对应的外联口的IP地址。

### 需要说明的是，配置VNF与DN/PDN通信的回程路由时，目的地址为UE的网段地址。下一跳为VNF上外联口的IP地址，由于自动部署时外联口的IP地址是系统自动分配的，因此建议首先通过命令**LST IFIPV4ADDRESS**查看外联口的IP地址。

### 7 配置VRF\_networkA（源VRF）的相关数据。

#### 7.1 修改L3VPN实例地址族。

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
```

#### 7.2 增加VPN Target。“VRFRTTYPE”须设置为“export\_extcommunity”。

```jinja2
{%- for item in add_vpntarget_list -%}
    ADD VPNTARGET:
    {#- --- 必选参数 --- -#}
    VRFNAME="{{item.VRFNAME}}",
    AFTYPE={{item.AFTYPE}},
    VRFRTTYPE={{item.VRFRTTYPE}},
    VRFRTVALUE="{{item.VRFRTVALUE}}",
    ;
{%- endfor -%}
```

#### 7.3 使能全局BGP。如已使能BGP，则此处不需要重复配置。

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

#### 7.4 增加BGP VPN实例。如已配置，则此处不需要重复配置。

```jinja2
{%- for item in add_bgpvrf_list -%}
    ADD BGPVRF:
    {#- --- 必选参数 --- -#}
    VRFNAME="{{item.VRFNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.DEFAULTAFTYPE is not none -%}
        DEFAULTAFTYPE={{item.DEFAULTAFTYPE}},
    {%- endif -%}
    {%- if item.VRFRIDAUTOSEL is not none -%}
        VRFRIDAUTOSEL={{item.VRFRIDAUTOSEL}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 7.5 增加BGP引入路由。如已配置，则此处不需要重复配置。

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

### 8 配置VRF\_networkB（目的VRF）的相关数据。

#### 8.1 修改L3VPN实例地址族。

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
```

#### 8.2 增加VPN Target。“VRFRTTYPE”须设置为“import\_extcommunity”。

```jinja2
{%- for item in add_vpntarget_list_1 -%}
    ADD VPNTARGET:
    {#- --- 必选参数 --- -#}
    VRFNAME="{{item.VRFNAME}}",
    AFTYPE={{item.AFTYPE}},
    VRFRTTYPE={{item.VRFRTTYPE}},
    VRFRTVALUE="{{item.VRFRTVALUE}}",
    ;
{%- endfor -%}
```


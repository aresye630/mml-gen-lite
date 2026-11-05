---
id: ''
name: 配置BGP over OSPF/静态路由+BFD（IPv4）
ne_type: UDG
type: feature
description: BGP（Border Gateway Protocol）边界网关协议是一种用于AS(Autonomous System)之间的动态路由协议，与OSPF、静态路由等内部网关协议（IGP）不同，其自身不能发现和计算路由，主要用于在自治系统AS间控制路由的传播和选择最佳路由。  当拓扑结构复杂且无法规划在同一自治区域内时，可以采用BGP over OSPF/静态路由+BFD实现VNF与对端设备的网络层互通。  * BGP协议自身没有自动部署功能，本文主要是在OSPF、静态路由等内部网关协议的自动部署基础上，通过BGP协议将其引入并传播。 * 采用DC-GW作网关时，采用BGP over静态路由+BFD；采用PE作网关时，采用BGP over静态路由+BFD（推荐）或BGP over OSPF+BFD。 * VNF所在硬件设备与DC-GW直连且采用双活网关时，支持BGP over 静态路由+BFD单臂echo，不支持OSPF动态路由协议。 * VNF所在硬件设备与DC-GW直连且采用M-LAG时，支持BGP over 静态路由+BFD单臂echo，不支持OSPF动态路由协议。  如图1所示为VNF与周边网元的BGP over OSPF/静态路由+BFD互通组网示意图。VNF与网关运行BGP over OSPF/静态路由+BFD路由协议而接入运营商网络（IP骨干网），网关可以使用DC-GW、EOR（End of Row）交换机或运营商的PE（Provider Edge）交换机。无论哪种方式，VNF的配置相同，没有差异。PE的路由配置请参考运营商的网络规划配置，DC-GW/EOR的配置请参考对应型号设备的产品文档。  **图1** BGP over OSPF/静态路由+BFD组网
risk_level: ''
doc_source: ["网络部署","初始配置","UDG初始配置与调测","组网路由配置","配置VNF侧IP路由数据（无NP卡_非SDN）","自动部署（推荐）","配置BGP over OSPF/静态路由+BFD（IPv4）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
BGP（Border Gateway Protocol）边界网关协议是一种用于AS(Autonomous System)之间的动态路由协议，与OSPF、静态路由等内部网关协议（IGP）不同，其自身不能发现和计算路由，主要用于在自治系统AS间控制路由的传播和选择最佳路由。当拓扑结构复杂且无法规划在同一自治区域内时，可以采用BGP over OSPF/静态路由+BFD实现VNF与对端设备的网络层互通。* BGP协议自身没有自动部署功能，本文主要是在OSPF、静态路由等内部网关协议的自动部署基础上，通过BGP协议将其引入并传播。* 采用DC-GW作网关时，采用BGP over静态路由+BFD；采用PE作网关时，采用BGP over静态路由+BFD（推荐）或BGP over OSPF+BFD。* VNF所在硬件设备与DC-GW直连且采用双活网关时，支持BGP over 静态路由+BFD单臂echo，不支持OSPF动态路由协议。* VNF所在硬件设备与DC-GW直连且采用M-LAG时，支持BGP over 静态路由+BFD单臂echo，不支持OSPF动态路由协议。如图1所示为VNF与周边网元的BGP over OSPF/静态路由+BFD互通组网示意图。VNF与网关运行BGP over OSPF/静态路由+BFD路由协议而接入运营商网络（IP骨干网），网关可以使用DC-GW、EOR（End of Row）交换机或运营商的PE（Provider Edge）交换机。无论哪种方式，VNF的配置相同，没有差异。PE的路由配置请参考运营商的网络规划配置，DC-GW/EOR的配置请参考对应型号设备的产品文档。**图1** BGP over OSPF/静态路由+BFD组网

## 必备事项
前提条件

* 请阅读并熟悉特性IPFD-014002 支持BGP特性概述。
* 已完成配置动态路由OSPF+BFD组网（IPv4）或配置静态路由+BFD组网（IPv4）。

* 具备管理员权限的操作人员已经登录华为操作维护系统（登录U2020/MAE客户端或登录OM Portal）。

* VNF与网络实体之间的网络环境已经构建完成。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    add_interface_list:
      type: items
      properties:
        IFNAME:
          name: '接口名'
          type: string
          maxLength: 63
          required: true
          description: '-'
          data_source: '参见“5G Core LLD文档 > 路由设计 > BGP设计 > Local interface name（VNF）”。'
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
          description: '此处的VPN实例已经配置，与OSPF、静态路由等IGP协议的外联口绑定的VPN实例相同。'
          data_source: '参见“5G Core LLD文档 > 路由设计 > BGP设计 > VRF名称（VNF）”。'
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
          name: '接口IPv4地址'
          type: string
          maxLength: 15
          required: true
          description: '如果规划Loopback接口使用IPv4v6双栈地址，则分别执行**ADD IFIPV4ADDRESS**和**ADD IFIPV6ADDRESS**  对同一Loopback接口配置IPv4和IPv6地址。'
          data_source: '参见“5G Core LLD文档 > 路由设计 > BGP设计 > Local interface address（VNF）”。'
          pattern: ''
          default: ''
        SUBNETMASK:
          name: '接口IPv4地址掩码'
          type: string
          maxLength: 15
          required: true
          description: ''
          data_source: '固定取值'
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
          description: 'BGP VPN实例需要与Loopback接口绑定的VPN实例名一致。'
          data_source: '参见“5G Core LLD文档 > 路由设计 > BGP设计 > VRF名称（VNF）”。'
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
          data_source: '参见“5G Core LLD文档 > 路由设计 > BGP设计 > Router ID（VNF）”。'
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
          data_source: '参见“5G Core LLD文档 > 路由设计 > BGP设计 > LoadBalance是否使能（VNF）”。  “LoadBalance是否使能”为“Y”时，该参数取值与对接的负荷分担的BGP PEER数一致。'
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
          description: '“PEERADDR”是网关上用于和VNF建立BGP邻居关系的IP地址。'
          data_source: '-'
          pattern: ''
          default: ipv4
        PEERADDR:
          name: 'IPv4对等体地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '参见“5G Core LLD文档 > 路由设计 > BGP设计 > Local interface address（L3GW）”。'
          pattern: ''
          default: ''
        REMOTEAS:
          name: '对等体AS号'
          type: string
          maxLength: 11
          required: false
          description: ''
          data_source: '参见“5G Core LLD文档 > 路由设计 > BGP设计 > AS号（L3GW）”。'
          pattern: ''
          default: ''
        LOCALIFADDR:
          name: '本地接口地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: '参见“5G Core LLD文档 > 路由设计 > BGP设计 > Local interface address（VNF）”。'
          pattern: ''
          default: ''
        LOCALIFNAME:
          name: '本地接口名称'
          type: string
          maxLength: 63
          required: false
          description: ''
          data_source: '参见“5G Core LLD文档 > 路由设计 > BGP设计 > Local interface name（VNF）”。'
          pattern: ''
          default: ''
        EBGPMAXHOP:
          name: 'EBGP最大跳数'
          type: integer
          minimum: 1
          maximum: 255
          required: false
          description: '不小于到Peer之间的实际跳数，无法确认时，可设置为10。  如最大跳数设置过小，会导致BGP邻居建立失败。'
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
          description: 'IPv4组网场景下，该参数选择ipv4uni。  该参数全局取值要一致。'
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
          data_source: '参见“5G Core LLD文档 > 路由设计 > BGP设计 > Import Route类型（VNF）”。'
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
    mod_bgppeeraf_list_1:
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
    add_autoscalingbgplf_list_1:
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
    add_autoscalingipreach_list_1:
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
    add_interface_list:
    - IFNAME: 'Loopback1'
    add_ipbindvpn_list:
    - IFNAME: 'Loopback1'
      VRFNAME: 'VPN_Access'
    add_ifipv4address_list:
    - IFNAME: 'Loopback1'
      IFIPADDR: '10.90.7.160'
      SUBNETMASK: '255.255.255.255'
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
    - VRFNAME: 'VPN_Access'
      DEFAULTAFTYPE: noaf
      ROUTERID: '10.90.7.160'
    add_bgpvrfaf_list:
    - VRFNAME: 'VPN_Access'
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
    - VRFNAME: 'VPN_Access'
      ADDRESSTYPE: ipv4
      PEERADDR: '10.9.7.135'
      REMOTEAS: '60002'
      LOCALIFADDR: '10.90.7.160'
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
    - VRFNAME: 'VPN_Access'
      AFTYPE: ipv4uni
      IMPORTPROTOCOL: wlr
      MEDENABLE: FALSE
      MED: 0
      IMPORTPROCESSID: ''
    set_dataplanegiinfmode_list:
    - MODE: RU
      ROUTEENHANCEDSW: ENABLE
    mod_bgppeeraf_list:
    - VRFNAME: 'VPN_Access'
      AFTYPE: ipv4uni
      REMOTEADDRESS: '10.9.7.135'
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
    - POLICYNAME: 'bgppolicy1'
      IPVERSION: IPv4
      SERVICENAME: 'ServName_Access_100'
      PEERIP: '10.9.7.135'
      PEERCOMMUNITY: 1
      UDADVCOMENABLE: TRUE
      UDADVCOM: '200'
      PEERIPV6: ''
    add_autoscalingipreach_list:
    - SERVICENAME: 'ServName_Access_100'
      IPVERSION: IPv4
      DESTADDR4: '10.9.7.135'
      BFDTEMPLATENAME: 'BFD_1'
      DESTADDR6: ''
    set_dataplaneinfmode_list:
    - MODE: Instance
      ROUTEENHANCEDSW: ENABLE
    mod_autoscalingservice_list:
    - SERVICENAME: 'ServName_Access_100'
      ISBACKUP: TRUE
    mod_bgppeeraf_list_1:
    - VRFNAME: 'VPN_Access'
      AFTYPE: ipv4uni
      REMOTEADDRESS: '10.9.7.135'
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
    add_autoscalingbgplf_list_1:
    - POLICYNAME: 'bgppolicy1'
      IPVERSION: IPv4
      SERVICENAME: 'ServName_Access_100'
      PEERIP: '10.9.7.135'
      PEERCOMMUNITY: 1
      UDADVCOMENABLE: TRUE
      UDADVCOM: '200'
      PEERIPV6: ''
    add_autoscalingipreach_list_1:
    - SERVICENAME: 'ServName_Access_100'
      IPVERSION: IPv4
      DESTADDR4: '10.9.7.135'
      BFDTEMPLATENAME: 'BFD_1'
      DESTADDR6: ''
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 配置OSPF+BFD、静态路由+BFD。

### 由于BGP协议自身不能发现路由，所以需要引入其他协议的路由（如OSPF或者静态路由等）注入到BGP路由表中，从而将这些路由在AS之内和AS之间传播。

#### 1.1 配置动态路由OSPF+BFD组网（IPv4）

#### 1.2 配置静态路由+BFD组网（IPv4）

### BFD会话绑定的是路由，不是BGPPEER。如存在**ADD BGPPEERBFD**配置，请删除。

### 静态路由用于实现VNF 的Loopback接口地址与BGP PEER IP（DC-GW）之间的互通。配置静态路由时，需满足如下配置点：

### 外联口的IP地址，是通过将“IPALLOCTYPE4”设置为“USER-CONFIG”的方式在VNF上配置。

### VNF所在硬件设备与DC-GW直连且采用双活网关时，支持BGP over 静态路由+BFD单臂echo，不支持OSPF动态路由协议。

### VNF所在硬件设备与DC-GW直连且采用M-LAG时，支持BGP over 静态路由+BFD单臂echo，不支持OSPF动态路由协议。

### 本步骤配置的是静态路由时，需要配置如下两类路由：

### IP路由1：目的IP是BGP对等体地址，下一跳是网关的接口IP地址，且该路由需要绑定BFD会话。

### IP路由2：目的IP是0.0.0.0，掩码长度是0，其他参数取值与“IP路由1”中的参数值相同。对端不发布默认路由时需要配置。

### 2 配置Loopback接口地址。

#### 2.1 配置Loopback接口。

```jinja2
{%- for item in add_interface_list -%}
    ADD INTERFACE:
    {#- --- 必选参数 --- -#}
    IFNAME="{{item.IFNAME}}",
    ;
{%- endfor -%}
```

#### 2.2 配置接口绑定VPN。

```jinja2
{%- for item in add_ipbindvpn_list -%}
    ADD IPBINDVPN:
    {#- --- 必选参数 --- -#}
    IFNAME="{{item.IFNAME}}",
    VRFNAME="{{item.VRFNAME}}",
    ;
{%- endfor -%}
```

#### 2.3 配置接口IP地址。

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

### 3 全局激活BGP。

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

### 4 配置BGP。

#### 4.1 增加BGP VPN实例。

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

#### 4.2 增加BGP VPN实例地址族。UDG对接2个负荷分担的BGP PEER时，“MAXIMUMLOADBALANCE”设置为“2”。

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

#### 4.3 增加BGP对等体。

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

#### 4.4 增加BGP引入路由。

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

#### 对于N6口，两个UPF上的UE地址段存在重叠且需要对外发布网段路由时，需要将“MEDENABLE”设置为“TRUE”，并设置备UPF的“MED”值大于主UPF的“MED”值。

### 5 U面下沉新建场景，采用高密度框式服务器+标卡+UPF分配IP地址+BGP over静态路由时，配置下行入不转板功能。其他场景不需要配置。

### 仅N6/SGi接口需要配置，其他接口不需要配置。

### 步骤 5.c和步骤 5.d须在自动化配置开关关闭状态下执行，否则执行失败。相关操作请参见配置静态路由+BFD组网（IPv4）中的步骤 3。

### 步骤 5.c和步骤 5.d配置完成后，须开启自动化配置开关（“SWITCHFLAG”设置为“TRUE”），否则配置不生效。相关操作请参见配置静态路由+BFD组网（IPv4）中的步骤 9。

### 开启下行入不转板的命令是**SET DATAPLANEGIINFMODE**，不是**SET DATAPLANEINFMODE**。

### 若误使用**SET DATAPLANEINFMODE**，则会上报ALM-81210 ISU或APU不可用告警。

#### 5.1 开启下行入不转板开关。此处以开启路由增强功能为例。

```jinja2
{%- if is_scenario_u_plane_sink -%}
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

#### 5.2 开启路由增强功能时，修改BGP对等体地址族。

#### 开启路由增强功能时，必须将“ADVERTISECOMMUNITY”设置为“TRUE”。其他参数值此处仅为举例，请通过**LST BGPPEER**获取。

```jinja2
{%- if is_scenario_u_plane_sink -%}
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

#### 5.3 增加入不转板策略自动化配置模板。

```jinja2
{%- if is_scenario_u_plane_sink -%}
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

#### 5.4 增加IP可达性检测自动化配置模板。

```jinja2
{%- if is_scenario_u_plane_sink -%}
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

### 6 中心云新建场景，第三方底层平台场景下业务单板转发性能低+采用ISU POD+标卡+UPF分配IP地址+BGP over静态路由时，配置入不转板功能。其他场景不需要配置。

### 仅如下逻辑接口对应的外联口需要配置，其他接口不需要配置。

### s1-uif（S1-U）、n3if（N3）、saif（S1-U和N3）。

### s5-sif（S5/S8-S）、n9cif（N9c）、scif（S5/S8-S和N9c）。

### paif（N9a/S5-P/S8-P/S2b/Gn-U/Gp-U）。

### 步骤 6.b~步骤 6.e须在自动化配置开关关闭状态下执行，否则执行失败。相关操作请参见配置静态路由+BFD组网（IPv4）中的步骤 3。

### 步骤 6.b~步骤 6.e配置完成后，须开启自动化配置开关（“SWITCHFLAG”设置为“TRUE”），否则配置不生效。相关操作请参见配置静态路由+BFD组网（IPv4）中的步骤 9。

### 开启入不转板的命令是**SET DATAPLANEINFMODE**，不是**SET DATAPLANEGIINFMODE**。

### 如误使用**SET DATAPLANEGIINFMODE**，则下行业务入不转板，上行业务入转板。

#### 6.1 开启入不转板开关。此处以开启路由增强功能为例。

```jinja2
{%- if is_scenario_central_cloud -%}
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

#### 6.2 将接口模板设置为在保护组上生效。

##### 6.2.1 //“ISBACKUP”设置为“TRUE”时，表示在保护组上生效；“ISBACKUP”设置为“FALSE”时，表示在非保护组上生效。

```jinja2
{%- if is_scenario_central_cloud -%}
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

#### 6.3 开启路由增强功能时，修改BGP对等体地址族。

#### 开启路由增强功能时，必须将“ADVERTISECOMMUNITY”设置为“TRUE”。其他参数值此处仅为举例，请通过**LST BGPPEER**获取。

```jinja2
{%- if is_scenario_central_cloud -%}
    {%- for item in mod_bgppeeraf_list_1 -%}
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

#### 6.4 增加入不转板策略自动化配置模板。

```jinja2
{%- if is_scenario_central_cloud -%}
    {%- for item in add_autoscalingbgplf_list_1 -%}
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

#### 6.5 增加IP可达性检测自动化配置模板。

```jinja2
{%- if is_scenario_central_cloud -%}
    {%- for item in add_autoscalingipreach_list_1 -%}
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


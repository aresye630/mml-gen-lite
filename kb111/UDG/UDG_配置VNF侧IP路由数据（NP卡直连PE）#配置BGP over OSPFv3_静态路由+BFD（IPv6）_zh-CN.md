---
id: ''
name: 配置BGP over OSPFv3/静态路由+BFD（IPv6）
ne_type: UDG
type: feature
description: BGP（Border Gateway Protocol）边界网关协议是一种用于AS(Autonomous System)之间的动态路由协议，与OSPFv3、静态路由等内部网关协议（IGP）不同，其自身不能发现和计算路由，主要用于在自治系统AS间控制路由的传播和选择最佳路由。  当拓扑结构复杂且无法规划在同一自治区域内时，可以采用BGP over OSPFv3/静态路由+BFD实现VNF与对端设备的网络层互通。  本文主要是在OSPF、静态路由等内部网关协议的部署基础上，通过BGP协议将其引入并传播。  如图1和图2所示为VNF与周边网元的BGP over OSPFv3/静态路由+BFD互通组网示意图。VNF与网关侧运行BGP over OSPFv3/静态路由+BFD路由协议而接入运营商网络（IP骨干网），网关使用运营商的PE（Provider Edge）交换机，也可以是DC-GW。如下描述以PE做网关为例。PE的路由配置请参考运营商的网络规划配置，DC-GW的配置请参考对应型号设备的产品文档。  **图1** BGP over OSPF/静态路由+BFD组网（Eth-trunk子接口组网）  **图2** BGP over OSPF/静态路由+BFD组网（Ethernet子接口组网）
risk_level: ''
doc_source: ["网络部署","初始配置","UDG初始配置与调测","组网路由配置","配置VNF侧IP路由数据（NP卡直连PE）","配置BGP over OSPFv3/静态路由+BFD（IPv6）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
BGP（Border Gateway Protocol）边界网关协议是一种用于AS(Autonomous System)之间的动态路由协议，与OSPFv3、静态路由等内部网关协议（IGP）不同，其自身不能发现和计算路由，主要用于在自治系统AS间控制路由的传播和选择最佳路由。当拓扑结构复杂且无法规划在同一自治区域内时，可以采用BGP over OSPFv3/静态路由+BFD实现VNF与对端设备的网络层互通。本文主要是在OSPF、静态路由等内部网关协议的部署基础上，通过BGP协议将其引入并传播。如图1和图2所示为VNF与周边网元的BGP over OSPFv3/静态路由+BFD互通组网示意图。VNF与网关侧运行BGP over OSPFv3/静态路由+BFD路由协议而接入运营商网络（IP骨干网），网关使用运营商的PE（Provider Edge）交换机，也可以是DC-GW。如下描述以PE做网关为例。PE的路由配置请参考运营商的网络规划配置，DC-GW的配置请参考对应型号设备的产品文档。**图1** BGP over OSPF/静态路由+BFD组网（Eth-trunk子接口组网）**图2** BGP over OSPF/静态路由+BFD组网（Ethernet子接口组网）

## 必备事项
前提条件

* 请阅读并熟悉特性IPFD-014002 支持BGP特性概述。
* 已完成配置静态路由+BFD组网（IPv6）或配置动态路由OSPFv3+BFD组网（IPv6）。

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
          data_source: '参见“5G Core LLD文档 > 路由设计 > BGP设计 > 本地接口名称（VNF侧）”。'
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
          description: '此处的VPN实例已经配置，与OSPFv3、静态路由等IGP协议的外联口绑定的VPN实例相同。'
          data_source: '参见“5G Core LLD文档 > 路由设计 > BGP设计 > VRF名称”。'
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
          description: '如果规划Loopback接口使用IPv4v6双栈地址，则分别执行**ADD IFIPV4ADDRESS**和**ADD IFIPV6ADDRESS**  对同一Loopback接口配置IPv4和IPv6地址。'
          data_source: '参见“5G Core LLD文档 > 路由设计 > BGP设计 > 本地IP（VNF侧）”。'
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
          data_source: '参见“5G Core LLD文档 > 路由设计 > BGP设计 > AS号（VNF侧）”。'
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
          data_source: '参见“5G Core LLD文档 > 路由设计 > BGP设计 > VRF名称”。'
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
          data_source: '参见“5G Core LLD文档 > 路由设计 > BGP设计 > Router-ID（VNF）”。'
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
          data_source: '参见“5G Core LLD文档 > 路由设计 > BGP设计 > 本地IP（网关侧）”。'
          pattern: ''
          default: ''
        REMOTEAS:
          name: '对等体AS号'
          type: string
          maxLength: 11
          required: false
          description: ''
          data_source: '参见“5G Core LLD文档 > 路由设计 > BGP设计 > AS号（网关侧）”。'
          pattern: ''
          default: ''
        LOCALIFADDR:
          name: '本地接口地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: '参见“5G Core LLD文档 > 路由设计 > BGP设计 > 本地IP（VNF侧）”。'
          pattern: ''
          default: ''
        LOCALIFNAME:
          name: '本地接口名称'
          type: string
          maxLength: 63
          required: false
          description: ''
          data_source: '参见“5G Core LLD文档 > 路由设计 > BGP设计 > 本地接口名称（VNF侧）”。'
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
        PEERADDR:
          name: 'IPv4对等体地址'
          type: string
          maxLength: 15
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
          data_source: '参见“5G Core LLD文档 > 路由设计 > BGP设计 > Import Route类型”。'
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
    add_interface_list:
    - IFNAME: 'Loopback1'
    add_ipbindvpn_list:
    - IFNAME: 'Loopback1'
      VRFNAME: 'VPN_Access'
    set_ifipv6enable_list:
    - IFNAME: 'Loopback1'
      ENABLEFLAG: TRUE
      AUTOLINKLOCAL: ''
      MTU: ''
    add_ifipv6address_list:
    - IFNAME: 'Loopback1'
      IPV6ADDRESS: 'FC00:2013::1'
      PREFIXLEN: 128
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
    - VRFNAME: 'VPN_Access'
      ADDRESSTYPE: ipv6
      PEERADDRV6: 'FC00:2013::2'
      REMOTEAS: '60002'
      LOCALIFADDR: 'FC00:2013::1'
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
      PEERADDR: ''
      PSWDTYPE: 'null'
      ROUTEREFRESH: TRUE
      TRACKINGDELAYTIME: ''
      TRACKINGENABLE: FALSE
      VALIDTTLHOPS: ''
    add_importroute_list:
    - VRFNAME: 'VPN_Access'
      AFTYPE: ipv6uni
      IMPORTPROTOCOL: wlr
      MEDENABLE: FALSE
      IMPORTPROCESSID: ''
      MED: ''
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 配置OSPFv3+BFD、静态路由+BFD。

### 由于BGP协议自身不能发现路由，所以需要引入其他协议的路由（如OSPFv3或者静态路由等）注入到BGP路由表中，从而将这些路由在AS之内和AS之间传播。

#### 1.1 BFD会话绑定的是路由，不是BGPPEER。如存在**ADD BGPPEERBFD**配置，请删除。

#### 1.2 静态路由用于实现VNF 的Loopback接口地址与BGP PEER IP（DC-GW）之间的互通。配置静态路由时，外联口的IP地址是通过**ADD IFIPV6ADDRESS**命令在VNF上配置。

#### 1.3 本步骤配置的是静态路由时，需要配置如下两类路由：

##### 1.3.1 IP路由1：目的IP是BGP对等体地址，下一跳是网关的接口IP地址，且该路由需要绑定BFD会话。

##### 1.3.2 IP路由2：目的IP是0:0:0:0:0:0:0:0，掩码长度是0，其他参数取值与“IP路由1”中的参数值相同。对端不发布默认路由时需要配置。

#### 1.4 配置静态路由+BFD组网（IPv6）

#### 1.5 配置动态路由OSPFv3+BFD组网（IPv6）

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

#### 2.3 配置IPv6使能。

```jinja2
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
```

#### 2.4 配置接口IP地址。

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

##### 4.1.1 此处配置的“ROUTERID”是BGP VPN实例级别的ROUTERID。

##### IPv4v6双栈时，IPv4 BGP VPN实例地址族和IPv6 BGP VPN实例地址族共用此处配置的“ROUTERID”值。

##### 4.1.2 已配置IPv4v6双栈的BGP VPN实例地址族，若需删除IPv4的BGP VPN实例地址族配置，则：

###### 4.1.2.1 1、删除IPv4的配置前需查询并记录“ROUTERID”值。

###### 4.1.2.2 2、删除IPv4的配置后需查询“ROUTERID”值是否存在，若不存在则需通过**MOD BGPVRF**命令将“ROUTERID”参数设置为删除IPv4的配置前记录的“ROUTERID”值。否则IPv6 BGP重新协商时会因无“ROUTERID”值可用而导致协商失败。

#### 4.2 增加BGP VPN实例地址族。UDG对接2个负荷分担的路由设备时，“MAXIMUMLOADBALANCE”设置为“2”。

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
    {#- --- 条件必选：ADDRESSTYPE=ipv6 时必选 --- -#}
    {%- if item.ADDRESSTYPE == 'ipv6' -%}
        PEERADDRV6="{{item.PEERADDRV6}}",
    {%- endif -%}
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

#### 由于BGP协议自身不能发现路由，所以需要引入其他协议的路由（如OSPFv3、静态路由或WLR等）注入到BGP路由表中，从而将这些路由在AS之内和AS之间传播。


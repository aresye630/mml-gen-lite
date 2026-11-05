---
id: ''
name: 配置互访流量的重定向功能
ne_type: UDG
type: feature
description: 重定向功能可以防止上行报文可能存在的报文攻击问题。通过重定向功能的设置保证了在同一UDG内部同一VPN的UE用户之间报文转发的安全。  * 适用于PGW-U、UPF。 * 本文中的重定向设备以Firewall为例。 * PGW-U/UPF内置NAT功能时，不支持UE互访。  UDG报文重定向示意图如图1和图2所示。  图2所示方案非华为数通标准方案，如需使用，请与数通工程师达成一致。  **图1** UDG报文重定向示意图（DC-GW上基于独立VPN实现重定向）  如图1，采用DC-GW上基于独立VPN实现重定向的方案时，组网要求如下：  * DCGW上接收UPF上行报文的接口（接口2）和向UPF发送下行报文的接口（接口5）分开，且两个接口绑定的VPN实例不同。 * DC-GW上接口2发布缺省路由给PGW-U/UPF，不接收PGW-U/UPF发布的UE路由。    接口3绑定的VPN实例与接口2相同，接口3接收PE侧路由，但不能把UE路由发布给PE侧。 * DC-GW上接口5需要接收PGW-U/UPF发布的UE路由，不能向PGW-U/UPF发布缺省路由。    接口4绑定的VPN实例与接口5相同，接口4发布UE路由给PE，但不接收PE侧路由。 * UDG上指定VPN的用户的所有上行报文均发送到重定向设备，由重定向设备安全过滤后基于目的IP转发报文。 * UDG上发送上行报文的接口（子接口1）和接收下行报文的接口（子接口6）分开，但两个子接口绑定的VPN实例相同。    子接口1和子接口6的VLAN不复用，IP地址段不复用。UDG子接口1不对外发布UE路由（不需要引入wlr路由）。  **图2** UDG报文重定向示意图（DC-GW上基于ACL+重定向IP实现重定向）  如图2，采用DC-GW上基于ACL+重定向IP实现重定向方案时，组网要求如下：  * DC-GW上需完成ACL及重定向IP等策略路由的相关配置。 * UDG发送上行报文（重定向报文和普通N6/SGi报文）和接收用户下行报文的子接口复用（单子接口），VLAN复用，VPN复用，IP地址段复用。
risk_level: ''
doc_source: ["网络部署","安全配置","UDG安全配置","安全配置建议","可选配置","业务安全配置","配置互访流量的重定向功能"]
refs: []
metadata:
  DepOnLiveCfg: true
allowed-tools:
- getParameterValue('LST AUTOCONFIG')
---
<!-- @mml:block=annotations -->
```text
## 操作场景
重定向功能可以防止上行报文可能存在的报文攻击问题。通过重定向功能的设置保证了在同一UDG内部同一VPN的UE用户之间报文转发的安全。* 适用于PGW-U、UPF。* 本文中的重定向设备以Firewall为例。* PGW-U/UPF内置NAT功能时，不支持UE互访。UDG报文重定向示意图如图1和图2所示。图2所示方案非华为数通标准方案，如需使用，请与数通工程师达成一致。**图1** UDG报文重定向示意图（DC-GW上基于独立VPN实现重定向）如图1，采用DC-GW上基于独立VPN实现重定向的方案时，组网要求如下：* DCGW上接收UPF上行报文的接口（接口2）和向UPF发送下行报文的接口（接口5）分开，且两个接口绑定的VPN实例不同。* DC-GW上接口2发布缺省路由给PGW-U/UPF，不接收PGW-U/UPF发布的UE路由。  接口3绑定的VPN实例与接口2相同，接口3接收PE侧路由，但不能把UE路由发布给PE侧。* DC-GW上接口5需要接收PGW-U/UPF发布的UE路由，不能向PGW-U/UPF发布缺省路由。  接口4绑定的VPN实例与接口5相同，接口4发布UE路由给PE，但不接收PE侧路由。* UDG上指定VPN的用户的所有上行报文均发送到重定向设备，由重定向设备安全过滤后基于目的IP转发报文。* UDG上发送上行报文的接口（子接口1）和接收下行报文的接口（子接口6）分开，但两个子接口绑定的VPN实例相同。  子接口1和子接口6的VLAN不复用，IP地址段不复用。UDG子接口1不对外发布UE路由（不需要引入wlr路由）。**图2** UDG报文重定向示意图（DC-GW上基于ACL+重定向IP实现重定向）如图2，采用DC-GW上基于ACL+重定向IP实现重定向方案时，组网要求如下：* DC-GW上需完成ACL及重定向IP等策略路由的相关配置。* UDG发送上行报文（重定向报文和普通N6/SGi报文）和接收用户下行报文的子接口复用（单子接口），VLAN复用，VPN复用，IP地址段复用。

## 必备事项
前提条件

如果运营商规划采用VPN组网方式，则操作员在执行本操作前应已创建了相应的VPN实例。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    set_giredirectfunc_list:
      type: items
      properties:
        V4GIREDIRSWITCH:
          name: 'IPV4全局Gi重定向开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: true
          description: '**SET GIREDIRECTFUNC**'
          data_source: '本端规划'
          pattern: ''
          default: ''
        V6GIREDIRSWITCH:
          name: 'IPV6全局Gi重定向开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: true
          description: ''
          data_source: '本端规划'
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
          description: '与APN绑定的VPN实例相同。VRFRD取值此处以复用loopback接口IP为例。  **ADD L3VPNINST**  **ADD VPNINSTAF**'
          data_source: '全网规划'
          pattern: ''
          default: ''
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
    add_vpninstaf_list:
      type: items
      properties:
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: true
          description: '与APN绑定的VPN实例相同。VRFRD取值此处以复用loopback接口IP为例。  **ADD L3VPNINST**  **ADD VPNINSTAF**'
          data_source: '全网规划'
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
          data_source: '-'
          pattern: ''
          default: ''
        VRFRD:
          name: '路由标识'
          type: string
          maxLength: 21
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_giredirectpara_list:
      type: items
      properties:
        VPNINSTANCE:
          name: '需绑定的VPN实例名'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: '此处是基于VPN实现UE互访，即：VPN和一个APN关联时，则是同一APN内的UE互访；VPN和多个APN关联时，则是同一APN内的UE互访+不同APN间的UE互访。  **ADD GIREDIRECTPARA**   * “IPv4重定向IP地址（IPV4ADDRESS）”是重定向设备的IPv4地址。 * “IPv6重定向IP地址（IPV6ADDRESS）”是重定向设备的IPv6地址。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPTYPE:
          name: '重定向的目的地址类型'
          type: string
          enum:
          - IPv4
          - IPv6
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        V4REDIRIPTYPE:
          name: 'IPv4重定向动作'
          type: string
          enum:
          - BLACKHOLE
          - IPADDRESS
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV4ADDRESS:
          name: 'IPv4重定向IP地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        V6REDIRIPTYPE:
          name: 'IPv6重定向动作'
          type: string
          enum:
          - BLACKHOLE
          - IPADDRESS
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV6ADDRESS:
          name: 'IPv6重定向IP地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_giredirectpara_list_3:
      type: items
      properties:
        VPNINSTANCE:
          name: '需绑定的VPN实例名'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: '此处是基于VPN实现UE互访，即：VPN和一个APN关联时，则是同一APN内的UE互访；VPN和多个APN关联时，则是同一APN内的UE互访+不同APN间的UE互访。  **ADD GIREDIRECTPARA**   * “IPv4重定向IP地址（IPV4ADDRESS）”是重定向设备的IPv4地址。 * “IPv6重定向IP地址（IPV6ADDRESS）”是重定向设备的IPv6地址。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPTYPE:
          name: '重定向的目的地址类型'
          type: string
          enum:
          - IPv4
          - IPv6
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        V4REDIRIPTYPE:
          name: 'IPv4重定向动作'
          type: string
          enum:
          - BLACKHOLE
          - IPADDRESS
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV4ADDRESS:
          name: 'IPv4重定向IP地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        V6REDIRIPTYPE:
          name: 'IPv6重定向动作'
          type: string
          enum:
          - BLACKHOLE
          - IPADDRESS
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_giredirectpara_list_5:
      type: items
      properties:
        VPNINSTANCE:
          name: '需绑定的VPN实例名'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: '此处是基于VPN实现UE互访，即：VPN和一个APN关联时，则是同一APN内的UE互访；VPN和多个APN关联时，则是同一APN内的UE互访+不同APN间的UE互访。  **ADD GIREDIRECTPARA**   * “IPv4重定向IP地址（IPV4ADDRESS）”是重定向设备的IPv4地址。 * “IPv6重定向IP地址（IPV6ADDRESS）”是重定向设备的IPv6地址。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPTYPE:
          name: '重定向的目的地址类型'
          type: string
          enum:
          - IPv4
          - IPv6
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        V6REDIRIPTYPE:
          name: 'IPv6重定向动作'
          type: string
          enum:
          - BLACKHOLE
          - IPADDRESS
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV6ADDRESS:
          name: 'IPv6重定向IP地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        V4REDIRIPTYPE:
          name: 'IPv4重定向动作'
          type: string
          enum:
          - BLACKHOLE
          - IPADDRESS
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
    add_interface_list:
      type: items
      properties:
        IFNAME:
          name: '接口名'
          type: string
          maxLength: 63
          required: true
          description: '**ADD INTERFACE**'
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
          description: '**ADD INTERFACE**'
          data_source: '本端规划'
          pattern: ''
          default: ''
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: true
          description: '**ADD IPBINDVPN**'
          data_source: '已配置数据中获取'
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
          description: '**ADD INTERFACE**'
          data_source: '本端规划'
          pattern: ''
          default: ''
        IFIPADDR:
          name: 'IPv4地址'
          type: string
          maxLength: 15
          required: true
          description: '**ADD IFIPV4ADDRESS**'
          data_source: '全网规划'
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
          description: '**ADD INTERFACE**'
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPV6ADDRESS:
          name: 'IPv6地址'
          type: string
          maxLength: 39
          required: true
          description: '**ADD IFIPV6ADDRESS**'
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
          data_source: '固定取值'
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
          description: '**ADD BGPVRF**'
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
        ROUTERID:
          name: '路由器标识'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '已配置数据中获取'
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
          description: '**ADD BGPVRFAF**'
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
          data_source: '本端规划'
          pattern: ''
          default: ''
        MAXIMUMLOADBALANCE:
          name: '最大等价路由数'
          type: integer
          minimum: 1
          maximum: 128
          required: false
          description: ''
          data_source: '与对端协商'
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
          description: '**ADD BGPPEER**   * “PEERADDR”是BGP Peer的IPv4地址。 * “PEERADDRV6”是BGP Peer的IPv6地址。   DC-GW上基于独立VPN实现重定向时，DC-GW上使用不同的VPN，分别用于接收UDG发送的上行报文及向UDG发送UE的下行报文。  即UDG上一个本端BGP地址，需要分别和DC-GW上两个VPN的loopback接口IP分别建立BGP邻居。UDG对接2个DC-GW，所以需要规划4个BGP Peer IP。'
          data_source: '已配置数据中获取'
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
          data_source: '全网规划'
          pattern: ''
          default: ''
        REMOTEAS:
          name: '对等体AS号'
          type: string
          maxLength: 11
          required: false
          description: 'BGP Peer的AS号。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        LOCALIFADDR:
          name: '本地接口地址'
          type: string
          maxLength: 39
          required: false
          description: 'BGP本端IP。上下行接口复用。'
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
    add_bgpvrfaf_list_1:
      type: items
      properties:
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: false
          description: '**ADD BGPVRFAF**'
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
          data_source: '本端规划'
          pattern: ''
          default: ''
        MAXIMUMLOADBALANCE:
          name: '最大等价路由数'
          type: integer
          minimum: 1
          maximum: 128
          required: false
          description: ''
          data_source: '与对端协商'
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
    add_bgppeer_list_2:
      type: items
      properties:
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: false
          description: '**ADD BGPPEER**   * “PEERADDR”是BGP Peer的IPv4地址。 * “PEERADDRV6”是BGP Peer的IPv6地址。   DC-GW上基于独立VPN实现重定向时，DC-GW上使用不同的VPN，分别用于接收UDG发送的上行报文及向UDG发送UE的下行报文。  即UDG上一个本端BGP地址，需要分别和DC-GW上两个VPN的loopback接口IP分别建立BGP邻居。UDG对接2个DC-GW，所以需要规划4个BGP Peer IP。'
          data_source: '已配置数据中获取'
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
        PEERADDRV6:
          name: 'IPv6对等体地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        REMOTEAS:
          name: '对等体AS号'
          type: string
          maxLength: 11
          required: false
          description: 'BGP Peer的AS号。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        LOCALIFADDR:
          name: '本地接口地址'
          type: string
          maxLength: 39
          required: false
          description: 'BGP本端IP。上下行接口复用。'
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
          description: '**ADD IMPORTROUTE**'
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
          data_source: '固定取值'
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
    add_routepolicy_list:
      type: items
      properties:
        POLICYNAME:
          name: '路由策略名字'
          type: string
          maxLength: 200
          required: true
          description: '**ADD ROUTEPOLICY**'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_routepolicynode_list:
      type: items
      properties:
        POLICYNAME:
          name: '路由策略名字'
          type: string
          maxLength: 200
          required: true
          description: '**ADD ROUTEPOLICY**'
          data_source: '本端规划'
          pattern: ''
          default: ''
        NODESEQUENCE:
          name: '路由策略节点号'
          type: integer
          minimum: 0
          maximum: 65535
          required: true
          description: '**ADD ROUTEPOLICYNODE**'
          data_source: '本端规划'
          pattern: ''
          default: ''
        MATCHMODE:
          name: '匹配模式'
          type: string
          enum:
          - deny
          - permit
          required: true
          description: '配置的路由策略节点，用于拒绝接收任何路由。'
          data_source: '固定取值'
          pattern: ''
          default: ''
    add_prefixfilternode_list:
      type: items
      properties:
        NAME:
          name: 'IP前缀列表名字'
          type: string
          maxLength: 169
          required: true
          description: '**ADD PREFIXFILTERNODE**'
          data_source: '本端规划'
          pattern: ''
          default: ''
        NODESEQUENCE:
          name: 'IP前缀列表节点号'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: true
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        MATCHMODE:
          name: 'IP前缀列表匹配模式'
          type: string
          enum:
          - deny
          - permit
          required: true
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
        ADDRESS:
          name: 'IP地址'
          type: string
          maxLength: 15
          required: true
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
        MASKLENGTH:
          name: '掩码长度'
          type: integer
          minimum: 0
          maximum: 32
          required: true
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
        GREATEREQUAL:
          name: '大于或等于'
          type: integer
          minimum: 0
          maximum: 32
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
        LESSEQUAL:
          name: '小于或等于'
          type: integer
          minimum: 0
          maximum: 32
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
        MATCHNETWORK:
          name: '是否匹配网络'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
    add_matchdestprefixfilter_list:
      type: items
      properties:
        POLICYNAME:
          name: '路由策略名字'
          type: string
          maxLength: 200
          required: true
          description: '**ADD MATCHDESTPREFIXFILTER**'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        NODESEQUENCE:
          name: '路由策略节点号'
          type: integer
          minimum: 0
          maximum: 65535
          required: true
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        PREFIXNAME:
          name: 'IP前缀列表名字'
          type: string
          maxLength: 169
          required: true
          description: ''
          data_source: '已配置数据中获取'
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
          description: '**ADD BGPPEERAF**   * 不接收BGP Peer 192.168.78.1和192.168.78.2发布的任何路由。 * 不接收BGP Peer FC00::78:1和FC00::78:2发布的任何路由。'
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
          data_source: '本端规划'
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
        IMPORTRTPOLICYNAME:
          name: '引入路由策略'
          type: string
          maxLength: 200
          required: false
          description: ''
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
    add_ipv6prefixfilternode_list:
      type: items
      properties:
        NAME:
          name: 'IPv6前缀列表名字'
          type: string
          maxLength: 169
          required: true
          description: '**ADD IPV6PREFIXFILTERNODE**'
          data_source: '本端规划'
          pattern: ''
          default: ''
        NODESEQUENCE:
          name: 'IPv6前缀列表节点号'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: true
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        MATCHMODE:
          name: 'IPv6前缀列表匹配模式'
          type: string
          enum:
          - deny
          - permit
          required: true
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
        ADDRESS:
          name: 'IPv6地址'
          type: string
          maxLength: 39
          required: true
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
        MASKLENGTH:
          name: '掩码长度'
          type: integer
          minimum: 0
          maximum: 128
          required: true
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
        MATCHNETWORK:
          name: '是否匹配网络地址'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        GREATEREQUAL:
          name: '掩码长度匹配范围下限'
          type: integer
          minimum: 0
          maximum: 128
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
        LESSEQUAL:
          name: '掩码长度匹配范围上限'
          type: integer
          minimum: 0
          maximum: 128
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
    add_matchdestprefix6filter_list:
      type: items
      properties:
        POLICYNAME:
          name: '路由策略名字'
          type: string
          maxLength: 200
          required: true
          description: '**ADD MATCHDESTPREFIX6FILTER**'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        NODESEQUENCE:
          name: '路由策略节点号'
          type: integer
          minimum: 0
          maximum: 65535
          required: true
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        IPV6PREFIXNAME:
          name: 'IPv6前缀列表名字'
          type: string
          maxLength: 169
          required: true
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    mod_bgppeeraf_list_2:
      type: items
      properties:
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: true
          description: '**ADD BGPPEERAF**   * 不接收BGP Peer 192.168.78.1和192.168.78.2发布的任何路由。 * 不接收BGP Peer FC00::78:1和FC00::78:2发布的任何路由。'
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
          data_source: '本端规划'
          pattern: ''
          default: ''
        REMOTEADDRESSV6:
          name: 'IPv6对等体地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        IMPORTRTPOLICYNAME:
          name: '引入路由策略'
          type: string
          maxLength: 200
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
        REMOTEADDRESS:
          name: 'IPv4对等体地址'
          type: string
          maxLength: 15
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
        EXPORTACLNAMEORNUM:
          name: '发布路由ACL规则标识'
          type: string
          maxLength: 32
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
        IMPORTACLNAMEORNUM:
          name: '接收路由ACL规则标识'
          type: string
          maxLength: 32
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
    add_autoscalingethtrunk_list:
      type: items
      properties:
        ETHTRUNKTMPID:
          name: '以太Trunk模板ID'
          type: integer
          minimum: 1
          maximum: 99
          required: true
          description: '**ADD AUTOSCALINGETHTRUNK**'
          data_source: '本端规划'
          pattern: ''
          default: ''
        VNICLIST:
          name: '虚拟网卡ID列表'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: '本端规划'
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
          description: '**ADD AUTOSCALINGSERVICE**  此处以下行接口（UDG用于接收重定向设备、PDN/DN Server发送的UE报文）所属VLAN是2008，上行接口（UDG用于发送上行报文到重定向设备、PDN/DN Server）所属VLAN是2009为例。  DC-GW上基于独立VPN实现重定向时，需要规划VLAN是2009的上行接口；DC-GW上基于ACL+重定向IP实现重定向时，仅规划VLAN是2008的接口即可。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        VPNNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: '已配置数据中获取'
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
          data_source: '-'
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
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        VLANID:
          name: 'VLAN ID'
          type: integer
          minimum: 0
          maximum: 4094
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: 0
        BEGINADDR4:
          name: '起始地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        ENDADDR4:
          name: '结束地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        MASKLEN:
          name: '地址池掩码长度'
          type: integer
          minimum: 1
          maximum: 128
          required: false
          description: ''
          data_source: '全网规划'
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
          description: '**ADD AUTOSCALINGBFD**  此处以单臂BFD为例。双向BFD时，请使用**ADD AUTOSCALINGSRBFD**命令。'
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
          name: 'IP版本'
          type: string
          enum:
          - IPv4
          - IPv6
          required: false
          description: ''
          data_source: '-'
          pattern: ''
          default: ''
        DESTADDR4:
          name: '目的地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        MINECHORXINT:
          name: '单臂Echo会话的收包间隔（ms）'
          type: integer
          minimum: 30
          maximum: 1000
          required: false
          description: ''
          data_source: '固定取值'
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
        ONEARMECHO:
          name: '单臂Echo'
          type: string
          enum:
          - TRUE
          required: false
          description: ''
          data_source: ''
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
          description: '**ADD AUTOSCALINGSRROUTE**'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: false
          description: '-'
          data_source: '已配置数据中获取'
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
          data_source: '-'
          pattern: ''
          default: ''
        PREFIX4:
          name: '路由前缀IPv4'
          type: string
          maxLength: 15
          required: false
          description: 'BGP Peer的IP地址。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        MASKLENGTH:
          name: '路由掩码长度'
          type: integer
          minimum: 0
          maximum: 128
          required: true
          description: ''
          data_source: '-'
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
          description: 'DC-GW的接口IP。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        BFDENABLE:
          name: 'BFD使能标识'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: FALSE
        DESCRIPTION:
          name: '路由描述'
          type: string
          maxLength: 35
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        BFDTEMPLATENAME:
          name: 'BFD模板名称'
          type: string
          maxLength: 59
          required: false
          description: '使用**ADD AUTOSCALINGBFD**命令定义的BFD模板名称。'
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
    add_autoscalingservice_list_1:
      type: items
      properties:
        SERVICENAME:
          name: '服务名称'
          type: string
          maxLength: 31
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        VPNNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: '已配置数据中获取'
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
          data_source: '-'
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
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        VLANID:
          name: 'VLAN ID'
          type: integer
          minimum: 0
          maximum: 4094
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: 0
        BEGINADDR6:
          name: '起始地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        ENDADDR6:
          name: '结束地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        MASKLEN:
          name: '地址池掩码长度'
          type: integer
          minimum: 1
          maximum: 128
          required: false
          description: ''
          data_source: '全网规划'
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
    add_autoscalingbfd_list_1:
      type: items
      properties:
        TEMPLATENAME:
          name: '模板名称'
          type: string
          maxLength: 59
          required: true
          description: '**ADD AUTOSCALINGBFD**  此处以单臂BFD为例。双向BFD时，请使用**ADD AUTOSCALINGSRBFD**命令。'
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
          name: 'IP版本'
          type: string
          enum:
          - IPv4
          - IPv6
          required: false
          description: ''
          data_source: '-'
          pattern: ''
          default: ''
        DESTADDR6:
          name: '目的地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        MINECHORXINT:
          name: '单臂Echo会话的收包间隔（ms）'
          type: integer
          minimum: 30
          maximum: 1000
          required: false
          description: ''
          data_source: '固定取值'
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
        ONEARMECHO:
          name: '单臂Echo'
          type: string
          enum:
          - TRUE
          required: false
          description: ''
          data_source: ''
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
        DESTADDR4:
          name: '目的地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_autoscalingsrroute_list_2:
      type: items
      properties:
        SERVICENAME:
          name: '服务名称'
          type: string
          maxLength: 31
          required: true
          description: '**ADD AUTOSCALINGSRROUTE**'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: false
          description: '-'
          data_source: '已配置数据中获取'
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
          data_source: '-'
          pattern: ''
          default: ''
        PREFIX6:
          name: '路由前缀IPv6'
          type: string
          maxLength: 39
          required: false
          description: 'BGP Peer的IP地址。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        MASKLENGTH:
          name: '路由掩码长度'
          type: integer
          minimum: 0
          maximum: 128
          required: true
          description: ''
          data_source: '-'
          pattern: ''
          default: ''
        NEXTHOPALLOCTYPE6:
          name: 'IPv6路由下一跳分配方式'
          type: string
          enum:
          - CONFIG
          - DHCP
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: CONFIG
        NEXTHOP6:
          name: '路由下一跳IPv6'
          type: string
          maxLength: 39
          required: false
          description: 'DC-GW的接口IP。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        BFDENABLE:
          name: 'BFD使能标识'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: FALSE
        DESCRIPTION:
          name: '路由描述'
          type: string
          maxLength: 35
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        BFDTEMPLATENAME:
          name: 'BFD模板名称'
          type: string
          maxLength: 59
          required: false
          description: '使用**ADD AUTOSCALINGBFD**命令定义的BFD模板名称。'
          data_source: '已配置数据中获取'
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
          data_source: ''
          pattern: ''
          default: CONFIG
        PREFIX4:
          name: '路由前缀IPv4'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_bgppeer_list_4:
      type: items
      properties:
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: false
          description: '**ADD BGPPEER**   * “PEERADDR”是BGP Peer的IPv4地址。 * “PEERADDRV6”是BGP Peer的IPv6地址。   DC-GW上基于独立VPN实现重定向时，DC-GW上使用不同的VPN，分别用于接收UDG发送的上行报文及向UDG发送UE的下行报文。  即UDG上一个本端BGP地址，需要分别和DC-GW上两个VPN的loopback接口IP分别建立BGP邻居。UDG对接2个DC-GW，所以需要规划4个BGP Peer IP。'
          data_source: '已配置数据中获取'
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
          data_source: '全网规划'
          pattern: ''
          default: ''
        REMOTEAS:
          name: '对等体AS号'
          type: string
          maxLength: 11
          required: false
          description: 'BGP Peer的AS号。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        LOCALIFADDR:
          name: '本地接口地址'
          type: string
          maxLength: 39
          required: false
          description: 'BGP本端IP。上下行接口复用。'
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
    mod_bgppeeraf_list_4:
      type: items
      properties:
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: true
          description: '**ADD BGPPEERAF**   * 不向BGP Peer 192.168.79.1和192.168.79.2发布任何路由。 * 不向BGP Peer FC00::79:1和FC00::79:2发布任何路由。'
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
          data_source: '本端规划'
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
        EXPORTRTPOLICYNAME:
          name: '发布路由策略'
          type: string
          maxLength: 200
          required: false
          description: ''
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
    add_autoscalingservice_list_2:
      type: items
      properties:
        SERVICENAME:
          name: '服务名称'
          type: string
          maxLength: 31
          required: true
          description: '**ADD AUTOSCALINGSERVICE**  此处以下行接口（UDG用于接收重定向设备、PDN/DN Server发送的UE报文）所属VLAN是2008，上行接口（UDG用于发送上行报文到重定向设备、PDN/DN Server）所属VLAN是2009为例。  DC-GW上基于独立VPN实现重定向时，需要规划VLAN是2009的上行接口；DC-GW上基于ACL+重定向IP实现重定向时，仅规划VLAN是2008的接口即可。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        VPNNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: '已配置数据中获取'
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
          data_source: '-'
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
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        VLANID:
          name: 'VLAN ID'
          type: integer
          minimum: 0
          maximum: 4094
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: 0
        BEGINADDR4:
          name: '起始地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        ENDADDR4:
          name: '结束地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        MASKLEN:
          name: '地址池掩码长度'
          type: integer
          minimum: 1
          maximum: 128
          required: false
          description: ''
          data_source: '全网规划'
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
    add_autoscalingbfd_list_2:
      type: items
      properties:
        TEMPLATENAME:
          name: '模板名称'
          type: string
          maxLength: 59
          required: true
          description: '**ADD AUTOSCALINGBFD**  此处以单臂BFD为例。双向BFD时，请使用**ADD AUTOSCALINGSRBFD**命令。'
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
          name: 'IP版本'
          type: string
          enum:
          - IPv4
          - IPv6
          required: false
          description: ''
          data_source: '-'
          pattern: ''
          default: ''
        DESTADDR4:
          name: '目的地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        MINECHORXINT:
          name: '单臂Echo会话的收包间隔（ms）'
          type: integer
          minimum: 30
          maximum: 1000
          required: false
          description: ''
          data_source: '固定取值'
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
        ONEARMECHO:
          name: '单臂Echo'
          type: string
          enum:
          - TRUE
          required: false
          description: ''
          data_source: ''
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
    add_autoscalingsrroute_list_4:
      type: items
      properties:
        SERVICENAME:
          name: '服务名称'
          type: string
          maxLength: 31
          required: true
          description: '**ADD AUTOSCALINGSRROUTE**'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: false
          description: '-'
          data_source: '已配置数据中获取'
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
          data_source: '-'
          pattern: ''
          default: ''
        PREFIX4:
          name: '路由前缀IPv4'
          type: string
          maxLength: 15
          required: false
          description: 'BGP Peer的IP地址。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        MASKLENGTH:
          name: '路由掩码长度'
          type: integer
          minimum: 0
          maximum: 128
          required: true
          description: ''
          data_source: '-'
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
          description: 'DC-GW的接口IP。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        BFDENABLE:
          name: 'BFD使能标识'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: FALSE
        DESCRIPTION:
          name: '路由描述'
          type: string
          maxLength: 35
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        BFDTEMPLATENAME:
          name: 'BFD模板名称'
          type: string
          maxLength: 59
          required: false
          description: '使用**ADD AUTOSCALINGBFD**命令定义的BFD模板名称。'
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
    add_bgppeer_list_6:
      type: items
      properties:
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: false
          description: '**ADD BGPPEER**   * “PEERADDR”是BGP Peer的IPv4地址。 * “PEERADDRV6”是BGP Peer的IPv6地址。   DC-GW上基于独立VPN实现重定向时，DC-GW上使用不同的VPN，分别用于接收UDG发送的上行报文及向UDG发送UE的下行报文。  即UDG上一个本端BGP地址，需要分别和DC-GW上两个VPN的loopback接口IP分别建立BGP邻居。UDG对接2个DC-GW，所以需要规划4个BGP Peer IP。'
          data_source: '已配置数据中获取'
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
        PEERADDRV6:
          name: 'IPv6对等体地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        REMOTEAS:
          name: '对等体AS号'
          type: string
          maxLength: 11
          required: false
          description: 'BGP Peer的AS号。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        LOCALIFADDR:
          name: '本地接口地址'
          type: string
          maxLength: 39
          required: false
          description: 'BGP本端IP。上下行接口复用。'
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
    mod_bgppeeraf_list_6:
      type: items
      properties:
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: true
          description: '**ADD BGPPEERAF**   * 不向BGP Peer 192.168.79.1和192.168.79.2发布任何路由。 * 不向BGP Peer FC00::79:1和FC00::79:2发布任何路由。'
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
          data_source: '本端规划'
          pattern: ''
          default: ''
        REMOTEADDRESSV6:
          name: 'IPv6对等体地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        EXPORTRTPOLICYNAME:
          name: '发布路由策略'
          type: string
          maxLength: 200
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
        IMPORTACL6NAMEORNUM:
          name: '接收路由ACL6规则标识'
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
        REMOTEADDRESS:
          name: 'IPv4对等体地址'
          type: string
          maxLength: 15
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
        EXPORTACLNAMEORNUM:
          name: '发布路由ACL规则标识'
          type: string
          maxLength: 32
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
        IMPORTACLNAMEORNUM:
          name: '接收路由ACL规则标识'
          type: string
          maxLength: 32
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
    add_autoscalingservice_list_3:
      type: items
      properties:
        SERVICENAME:
          name: '服务名称'
          type: string
          maxLength: 31
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        VPNNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: '已配置数据中获取'
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
          data_source: '-'
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
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        VLANID:
          name: 'VLAN ID'
          type: integer
          minimum: 0
          maximum: 4094
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: 0
        BEGINADDR6:
          name: '起始地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        ENDADDR6:
          name: '结束地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        MASKLEN:
          name: '地址池掩码长度'
          type: integer
          minimum: 1
          maximum: 128
          required: false
          description: ''
          data_source: '全网规划'
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
    add_autoscalingbfd_list_3:
      type: items
      properties:
        TEMPLATENAME:
          name: '模板名称'
          type: string
          maxLength: 59
          required: true
          description: '**ADD AUTOSCALINGBFD**  此处以单臂BFD为例。双向BFD时，请使用**ADD AUTOSCALINGSRBFD**命令。'
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
          name: 'IP版本'
          type: string
          enum:
          - IPv4
          - IPv6
          required: false
          description: ''
          data_source: '-'
          pattern: ''
          default: ''
        DESTADDR6:
          name: '目的地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        MINECHORXINT:
          name: '单臂Echo会话的收包间隔（ms）'
          type: integer
          minimum: 30
          maximum: 1000
          required: false
          description: ''
          data_source: '固定取值'
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
        ONEARMECHO:
          name: '单臂Echo'
          type: string
          enum:
          - TRUE
          required: false
          description: ''
          data_source: ''
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
        DESTADDR4:
          name: '目的地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_autoscalingsrroute_list_6:
      type: items
      properties:
        SERVICENAME:
          name: '服务名称'
          type: string
          maxLength: 31
          required: true
          description: '**ADD AUTOSCALINGSRROUTE**'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: false
          description: '-'
          data_source: '已配置数据中获取'
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
          data_source: '-'
          pattern: ''
          default: ''
        PREFIX6:
          name: '路由前缀IPv6'
          type: string
          maxLength: 39
          required: false
          description: 'BGP Peer的IP地址。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        MASKLENGTH:
          name: '路由掩码长度'
          type: integer
          minimum: 0
          maximum: 128
          required: true
          description: ''
          data_source: '-'
          pattern: ''
          default: ''
        NEXTHOPALLOCTYPE6:
          name: 'IPv6路由下一跳分配方式'
          type: string
          enum:
          - CONFIG
          - DHCP
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: CONFIG
        NEXTHOP6:
          name: '路由下一跳IPv6'
          type: string
          maxLength: 39
          required: false
          description: 'DC-GW的接口IP。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        BFDENABLE:
          name: 'BFD使能标识'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: FALSE
        DESCRIPTION:
          name: '路由描述'
          type: string
          maxLength: 35
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        BFDTEMPLATENAME:
          name: 'BFD模板名称'
          type: string
          maxLength: 59
          required: false
          description: '使用**ADD AUTOSCALINGBFD**命令定义的BFD模板名称。'
          data_source: '已配置数据中获取'
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
          data_source: ''
          pattern: ''
          default: CONFIG
        PREFIX4:
          name: '路由前缀IPv4'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_bfd_list_1:
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
        BFDRXCFGFLAG:
          name: '是否配置BFD最小接收报文间隔'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        BFDMINRXINTV:
          name: '接收BFD包的最小时间间隔（ms）'
          type: integer
          minimum: 30
          maximum: 1000
          required: false
          description: ''
          data_source: ''
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
          data_source: ''
          pattern: ''
          default: FALSE
        BFDMINTXINTV:
          name: '发送BFD包的最小时间间隔（ms）'
          type: integer
          minimum: 30
          maximum: 1000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SCHEMABFDDETMUL:
          name: 'BFD检测乘数'
          type: integer
          minimum: 3
          maximum: 50
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 3
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
        LSAARRINTV:
          name: '接收时间间隔（ms）'
          type: integer
          minimum: 0
          maximum: 10000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
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
          description: '需要和对接的DC-GW接口的OSPF区域ID相同。'
          data_source: '全网规划'
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
          description: '两个接口若要建立邻居关系，则Area Type必须相同。'
          data_source: '全网规划'
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
          - TRUE
          - FALSE
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
          name: '配置N-bit位'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        NSSASUPPRESSFORWARDINGADDRESS:
          name: '转换后生成的Type5 LSA的FA配置为0.0.0.0'
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
          name: '转换路由器'
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
          name: '失效时间（s）'
          type: integer
          minimum: 1
          maximum: 120
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 40
        NSSAZEROADDRESSFORWARDING:
          name: '将生成的Type7 LSA的FA置为0.0.0.0'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
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
        MAXCOSTINTVL:
          name: '保持最大开销值时间间隔（s）'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_ospfimportroute_list:
      type: items
      properties:
        PROCID:
          name: 'OSPF进程ID'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: true
          description: '仅和接收下行报文相关的OSPF进程发布wlr路由。   * IPv4 MML：**ADD OSPFIMPORTROUTE** * IPv6 MML：**ADD OSPFV3IMPORTROUTE**'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        TOPOID:
          name: '拓扑标识'
          type: integer
          minimum: 0
          maximum: 0
          required: false
          description: ''
          data_source: '固定取值'
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
          data_source: '固定取值'
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
          type: integer
          minimum: 1
          maximum: 2
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
        ROUTERID:
          name: '路由器标识'
          type: string
          maxLength: 15
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
        BFDRXCFGFLAG:
          name: '是否配置BFD最小接收报文间隔'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        BFDMINRXINTV:
          name: '接收BFD包的最小时间间隔（ms）'
          type: integer
          minimum: 30
          maximum: 1000
          required: false
          description: ''
          data_source: ''
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
          data_source: ''
          pattern: ''
          default: FALSE
        BFDMINTXINTV:
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
          name: 'BFD检测乘数间隔'
          type: integer
          minimum: 3
          maximum: 50
          required: false
          description: ''
          data_source: ''
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
          name: '区域号'
          type: string
          maxLength: 15
          required: true
          description: '需要和对接的DC-GW接口的OSPF区域ID相同。'
          data_source: '全网规划'
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
          description: '两个接口若要建立邻居关系，则Area Type必须相同。'
          data_source: '全网规划'
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
          name: 'OSPF进程ID'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: true
          description: '仅和接收下行报文相关的OSPF进程发布wlr路由。   * IPv4 MML：**ADD OSPFIMPORTROUTE** * IPv6 MML：**ADD OSPFV3IMPORTROUTE**'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        TOPOID:
          name: '拓扑标识'
          type: integer
          minimum: 0
          maximum: 0
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: 0
        PROTOCOL:
          name: '协议分类'
          type: string
          enum:
          - bgp
          - direct
          - ospfv3
          - static
          - wlr
          required: true
          description: ''
          data_source: '固定取值'
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
    add_routepolicy_list_1:
      type: items
      properties:
        POLICYNAME:
          name: '路由策略名字'
          type: string
          maxLength: 200
          required: true
          description: '**ADD ROUTEPOLICY**'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_routepolicynode_list_1:
      type: items
      properties:
        POLICYNAME:
          name: '路由策略名字'
          type: string
          maxLength: 200
          required: true
          description: '**ADD ROUTEPOLICY**'
          data_source: '本端规划'
          pattern: ''
          default: ''
        NODESEQUENCE:
          name: '路由策略节点号'
          type: integer
          minimum: 0
          maximum: 65535
          required: true
          description: '**ADD ROUTEPOLICYNODE**'
          data_source: '本端规划'
          pattern: ''
          default: ''
        MATCHMODE:
          name: '匹配模式'
          type: string
          enum:
          - deny
          - permit
          required: true
          description: '配置的路由策略节点，用于拒绝接收任何路由。'
          data_source: '固定取值'
          pattern: ''
          default: ''
    add_prefixfilternode_list_1:
      type: items
      properties:
        NAME:
          name: 'IP前缀列表名字'
          type: string
          maxLength: 169
          required: true
          description: '**ADD PREFIXFILTERNODE**'
          data_source: '本端规划'
          pattern: ''
          default: ''
        NODESEQUENCE:
          name: 'IP前缀列表节点号'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: true
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        MATCHMODE:
          name: 'IP前缀列表匹配模式'
          type: string
          enum:
          - deny
          - permit
          required: true
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
        ADDRESS:
          name: 'IP地址'
          type: string
          maxLength: 15
          required: true
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
        MASKLENGTH:
          name: '掩码长度'
          type: integer
          minimum: 0
          maximum: 32
          required: true
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
        GREATEREQUAL:
          name: '大于或等于'
          type: integer
          minimum: 0
          maximum: 32
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
        LESSEQUAL:
          name: '小于或等于'
          type: integer
          minimum: 0
          maximum: 32
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
        MATCHNETWORK:
          name: '是否匹配网络'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
    add_matchdestprefixfilter_list_1:
      type: items
      properties:
        POLICYNAME:
          name: '路由策略名字'
          type: string
          maxLength: 200
          required: true
          description: '**ADD MATCHDESTPREFIXFILTER**'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        NODESEQUENCE:
          name: '路由策略节点号'
          type: integer
          minimum: 0
          maximum: 65535
          required: true
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        PREFIXNAME:
          name: 'IP前缀列表名字'
          type: string
          maxLength: 169
          required: true
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_ospffilterpolicy_list:
      type: items
      properties:
        PROCID:
          name: '进程号'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: true
          description: '* IPv4 MML：**ADD OSPFFILTERPOLICY** * IPv6 MML：**ADD OSPFV3FILTERPOLICY**   import表示对接收到的路由进行过滤。  export表示对通过OSPF引入的路由信息向外发布时进行过滤。  “FILTERTYPE”设置为“export”时，可指定对外不发布路由的协议类型，此处以对外不发布wlr路由为例（PROTOCOL设置为wlr）。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        FILTERTYPE:
          name: '过滤方向'
          type: string
          enum:
          - export
          - import
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        TYPE:
          name: '过滤规则类型'
          type: string
          enum:
          - acl_name
          - acl_num
          - ip_prefix
          - route_policy
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPPREFIX:
          name: 'IP前缀列表名称'
          type: string
          maxLength: 169
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        PROTOCOL:
          name: '协议分类'
          type: string
          enum:
          - BGP
          - Direct
          - OSPF
          - Static
          - Total
          - wlr
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: Total
        ACLNAMEORNUM:
          name: 'ACL名称或ACL号'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ROUTEPLYNAME:
          name: '路由策略名称'
          type: string
          maxLength: 200
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SECONDARYFLAG:
          name: '是否优选次优路由'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
    add_interface_list_1:
      type: items
      properties:
        IFNAME:
          name: '接口名'
          type: string
          maxLength: 63
          required: true
          description: '**ADD INTERFACE**  **ADD OSPFINTERFACE**'
          data_source: '本端规划'
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
          description: '**ADD INTERFACE**  **ADD OSPFINTERFACE**'
          data_source: '本端规划'
          pattern: ''
          default: ''
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: true
          description: '**ADD IPBINDVPN**'
          data_source: '已配置数据中获取'
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
          description: '**ADD INTERFACE**  **ADD OSPFINTERFACE**'
          data_source: '本端规划'
          pattern: ''
          default: ''
        IFIPADDR:
          name: 'IPv4地址'
          type: string
          maxLength: 15
          required: true
          description: '**ADD IFIPV4ADDRESS**'
          data_source: '全网规划'
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
          name: '区域号'
          type: string
          maxLength: 15
          required: true
          description: '需要和对接的DC-GW接口的OSPF区域ID相同。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        IFNAME:
          name: '接口名'
          type: string
          maxLength: 63
          required: true
          description: '**ADD INTERFACE**  **ADD OSPFINTERFACE**'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_ipv6prefixfilternode_list_1:
      type: items
      properties:
        NAME:
          name: 'IPv6前缀列表名字'
          type: string
          maxLength: 169
          required: true
          description: '**ADD IPV6PREFIXFILTERNODE**'
          data_source: '本端规划'
          pattern: ''
          default: ''
        NODESEQUENCE:
          name: 'IPv6前缀列表节点号'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: true
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        MATCHMODE:
          name: 'IPv6前缀列表匹配模式'
          type: string
          enum:
          - deny
          - permit
          required: true
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
        ADDRESS:
          name: 'IPv6地址'
          type: string
          maxLength: 39
          required: true
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
        MASKLENGTH:
          name: '掩码长度'
          type: integer
          minimum: 0
          maximum: 128
          required: true
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
        MATCHNETWORK:
          name: '是否匹配网络地址'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        GREATEREQUAL:
          name: '掩码长度匹配范围下限'
          type: integer
          minimum: 0
          maximum: 128
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
        LESSEQUAL:
          name: '掩码长度匹配范围上限'
          type: integer
          minimum: 0
          maximum: 128
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
    add_matchdestprefix6filter_list_1:
      type: items
      properties:
        POLICYNAME:
          name: '路由策略名字'
          type: string
          maxLength: 200
          required: true
          description: '**ADD MATCHDESTPREFIX6FILTER**'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        NODESEQUENCE:
          name: '路由策略节点号'
          type: integer
          minimum: 0
          maximum: 65535
          required: true
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        IPV6PREFIXNAME:
          name: 'IPv6前缀列表名字'
          type: string
          maxLength: 169
          required: true
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_ospfv3filterpolicy_list:
      type: items
      properties:
        PROCID:
          name: '进程号'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: true
          description: '* IPv4 MML：**ADD OSPFFILTERPOLICY** * IPv6 MML：**ADD OSPFV3FILTERPOLICY**   import表示对接收到的路由进行过滤。  export表示对通过OSPF引入的路由信息向外发布时进行过滤。  “FILTERTYPE”设置为“export”时，可指定对外不发布路由的协议类型，此处以对外不发布wlr路由为例（PROTOCOL设置为wlr）。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        FILTERTYPE:
          name: '过滤方向'
          type: string
          enum:
          - export
          - import
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        TYPE:
          name: '过滤规则类型'
          type: string
          enum:
          - acl_name
          - acl_num
          - ip_prefix
          - route_policy
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPPREFIX:
          name: 'IP前缀列表名称'
          type: string
          maxLength: 169
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        PROTOCOL:
          name: '协议号'
          type: string
          enum:
          - bgp
          - direct
          - ospfv3
          - static
          - wlr
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ACLNAMEORNUM:
          name: 'ACL名称或ACL号'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ROUTEPLYNAME:
          name: '路由策略名称'
          type: string
          maxLength: 200
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_autoscalingethtrunk_list_1:
      type: items
      properties:
        ETHTRUNKTMPID:
          name: '以太Trunk模板ID'
          type: integer
          minimum: 1
          maximum: 99
          required: true
          description: '**ADD AUTOSCALINGETHTRUNK**'
          data_source: '本端规划'
          pattern: ''
          default: ''
        VNICLIST:
          name: '虚拟网卡ID列表'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_autoscalingservice_list_4:
      type: items
      properties:
        SERVICENAME:
          name: '服务名称'
          type: string
          maxLength: 31
          required: true
          description: '**ADD AUTOSCALINGSERVICE**  此处以下行接口（UDG用于接收重定向设备、PDN/DN Server发送的UE报文）所属VLAN是2008，上行接口（UDG用于发送上行报文到重定向设备、PDN/DN Server）所属VLAN是2009为例。  DC-GW上基于独立VPN实现重定向时，需要规划VLAN是2009的上行接口；DC-GW上基于ACL+重定向IP实现重定向时，仅规划VLAN是2008的接口即可。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        VPNNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: '已配置数据中获取'
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
          data_source: '-'
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
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        VLANID:
          name: 'VLAN ID'
          type: integer
          minimum: 0
          maximum: 4094
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: 0
        BEGINADDR4:
          name: '起始地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        ENDADDR4:
          name: '结束地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        MASKLEN:
          name: '地址池掩码长度'
          type: integer
          minimum: 1
          maximum: 128
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        OSPFENABLE:
          name: '使能OSPF'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: '**ADD AUTOSCALINGSERVICE**'
          data_source: '固定取值'
          pattern: ''
          default: FALSE
        OSPFPROCID:
          name: 'OSPF进程ID'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: false
          description: '**ADD AUTOSCALINGSERVICE**   * IPv4 MML： **ADD OSPF**  **ADD OSPFAREA** * IPv6 MML： **ADD OSPFV3**  **ADD OSPFV3AREA**   存在多个进程时，进程号不能重复。  此处以OSPF进程8为接收下行报文的进程，OSPF进程9为发送上行报文的'
          data_source: '本端规划'
          pattern: ''
          default: ''
        OSPFAREAID:
          name: 'OSPF区域ID'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TPINENABLE:
          name: '使能入方向的流量策略'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: '-'
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
          description: '-'
          data_source: '-'
          pattern: ''
          default: FALSE
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
        BEGINADDR6:
          name: '起始地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        ENDADDR6:
          name: '结束地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
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
        BFDRXCFGFLAG:
          name: '是否配置BFD最小接收报文间隔'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        BFDMINRXINTV:
          name: '接收BFD包的最小时间间隔（ms）'
          type: integer
          minimum: 30
          maximum: 1000
          required: false
          description: ''
          data_source: ''
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
          data_source: ''
          pattern: ''
          default: FALSE
        BFDMINTXINTV:
          name: '发送BFD包的最小时间间隔（ms）'
          type: integer
          minimum: 30
          maximum: 1000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SCHEMABFDDETMUL:
          name: 'BFD检测乘数'
          type: integer
          minimum: 3
          maximum: 50
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 3
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
        LSAARRINTV:
          name: '接收时间间隔（ms）'
          type: integer
          minimum: 0
          maximum: 10000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
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
          description: '需要和对接的DC-GW接口的OSPF区域ID相同。'
          data_source: '全网规划'
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
          description: '两个接口若要建立邻居关系，则Area Type必须相同。'
          data_source: '全网规划'
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
          - TRUE
          - FALSE
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
          name: '配置N-bit位'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        NSSASUPPRESSFORWARDINGADDRESS:
          name: '转换后生成的Type5 LSA的FA配置为0.0.0.0'
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
          name: '转换路由器'
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
          name: '失效时间（s）'
          type: integer
          minimum: 1
          maximum: 120
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 40
        NSSAZEROADDRESSFORWARDING:
          name: '将生成的Type7 LSA的FA置为0.0.0.0'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
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
        MAXCOSTINTVL:
          name: '保持最大开销值时间间隔（s）'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_ospffilterpolicy_list_1:
      type: items
      properties:
        PROCID:
          name: '进程号'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: true
          description: '* IPv4 MML：**ADD OSPFFILTERPOLICY** * IPv6 MML：**ADD OSPFV3FILTERPOLICY**   import表示对接收到的路由进行过滤。  export表示对通过OSPF引入的路由信息向外发布时进行过滤。  “FILTERTYPE”设置为“export”时，可指定对外不发布路由的协议类型，此处以对外不发布wlr路由为例（PROTOCOL设置为wlr）。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        FILTERTYPE:
          name: '过滤方向'
          type: string
          enum:
          - export
          - import
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        TYPE:
          name: '过滤规则类型'
          type: string
          enum:
          - acl_name
          - acl_num
          - ip_prefix
          - route_policy
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPPREFIX:
          name: 'IP前缀列表名称'
          type: string
          maxLength: 169
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        PROTOCOL:
          name: '协议分类'
          type: string
          enum:
          - BGP
          - Direct
          - OSPF
          - Static
          - Total
          - wlr
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: Total
        PROTOCOLPROCESSID:
          name: '协议进程号'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 1
        ACLNAMEORNUM:
          name: 'ACL名称或ACL号'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ROUTEPLYNAME:
          name: '路由策略名称'
          type: string
          maxLength: 200
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SECONDARYFLAG:
          name: '是否优选次优路由'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
    add_autoscalingservice_list_6:
      type: items
      properties:
        SERVICENAME:
          name: '服务名称'
          type: string
          maxLength: 31
          required: true
          description: '**ADD AUTOSCALINGSERVICE**  此处以下行接口（UDG用于接收重定向设备、PDN/DN Server发送的UE报文）所属VLAN是2008，上行接口（UDG用于发送上行报文到重定向设备、PDN/DN Server）所属VLAN是2009为例。  DC-GW上基于独立VPN实现重定向时，需要规划VLAN是2009的上行接口；DC-GW上基于ACL+重定向IP实现重定向时，仅规划VLAN是2008的接口即可。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        VPNNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: '已配置数据中获取'
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
          data_source: '-'
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
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        VLANID:
          name: 'VLAN ID'
          type: integer
          minimum: 0
          maximum: 4094
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: 0
        BEGINADDR4:
          name: '起始地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        ENDADDR4:
          name: '结束地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        MASKLEN:
          name: '地址池掩码长度'
          type: integer
          minimum: 1
          maximum: 128
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        OSPFENABLE:
          name: '使能OSPF'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: '**ADD AUTOSCALINGSERVICE**'
          data_source: '固定取值'
          pattern: ''
          default: FALSE
        OSPFPROCID:
          name: 'OSPF进程ID'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: false
          description: '**ADD AUTOSCALINGSERVICE**   * IPv4 MML： **ADD OSPF**  **ADD OSPFAREA** * IPv6 MML： **ADD OSPFV3**  **ADD OSPFV3AREA**   存在多个进程时，进程号不能重复。  此处以OSPF进程8为接收下行报文的进程，OSPF进程9为发送上行报文的'
          data_source: '本端规划'
          pattern: ''
          default: ''
        OSPFAREAID:
          name: 'OSPF区域ID'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TPINENABLE:
          name: '使能入方向的流量策略'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: '-'
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
          description: '-'
          data_source: '-'
          pattern: ''
          default: FALSE
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
        ROUTERID:
          name: '路由器标识'
          type: string
          maxLength: 15
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
        BFDRXCFGFLAG:
          name: '是否配置BFD最小接收报文间隔'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        BFDMINRXINTV:
          name: '接收BFD包的最小时间间隔（ms）'
          type: integer
          minimum: 30
          maximum: 1000
          required: false
          description: ''
          data_source: ''
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
          data_source: ''
          pattern: ''
          default: FALSE
        BFDMINTXINTV:
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
          name: 'BFD检测乘数间隔'
          type: integer
          minimum: 3
          maximum: 50
          required: false
          description: ''
          data_source: ''
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
          name: '区域号'
          type: string
          maxLength: 15
          required: true
          description: '需要和对接的DC-GW接口的OSPF区域ID相同。'
          data_source: '全网规划'
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
          description: '两个接口若要建立邻居关系，则Area Type必须相同。'
          data_source: '全网规划'
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
    add_ospfv3filterpolicy_list_1:
      type: items
      properties:
        PROCID:
          name: '进程号'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: true
          description: '* IPv4 MML：**ADD OSPFFILTERPOLICY** * IPv6 MML：**ADD OSPFV3FILTERPOLICY**   import表示对接收到的路由进行过滤。  export表示对通过OSPF引入的路由信息向外发布时进行过滤。  “FILTERTYPE”设置为“export”时，可指定对外不发布路由的协议类型，此处以对外不发布wlr路由为例（PROTOCOL设置为wlr）。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        FILTERTYPE:
          name: '过滤方向'
          type: string
          enum:
          - export
          - import
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        TYPE:
          name: '过滤规则类型'
          type: string
          enum:
          - acl_name
          - acl_num
          - ip_prefix
          - route_policy
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPPREFIX:
          name: 'IP前缀列表名称'
          type: string
          maxLength: 169
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        PROTOCOL:
          name: '协议分类'
          type: string
          enum:
          - bgp
          - direct
          - ospfv3
          - static
          - wlr
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        PROTOCOLPROCESSID:
          name: '协议进程号'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 1
        ACLNAMEORNUM:
          name: 'ACL名称或ACL号'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ROUTEPLYNAME:
          name: '路由策略名称'
          type: string
          maxLength: 200
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_autoscalingservice_list_7:
      type: items
      properties:
        SERVICENAME:
          name: '服务名称'
          type: string
          maxLength: 31
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        VPNNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: '已配置数据中获取'
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
          data_source: '-'
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
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        VLANID:
          name: 'VLAN ID'
          type: integer
          minimum: 0
          maximum: 4094
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: 0
        BEGINADDR6:
          name: '起始地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        ENDADDR6:
          name: '结束地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        MASKLEN:
          name: '地址池掩码长度'
          type: integer
          minimum: 1
          maximum: 128
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        OSPFENABLE:
          name: '使能OSPF'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: '**ADD AUTOSCALINGSERVICE**'
          data_source: '固定取值'
          pattern: ''
          default: FALSE
        OSPFPROCID:
          name: 'OSPF进程ID'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: false
          description: '**ADD AUTOSCALINGSERVICE**   * IPv4 MML： **ADD OSPF**  **ADD OSPFAREA** * IPv6 MML： **ADD OSPFV3**  **ADD OSPFV3AREA**   存在多个进程时，进程号不能重复。  此处以OSPF进程8为接收下行报文的进程，OSPF进程9为发送上行报文的'
          data_source: '本端规划'
          pattern: ''
          default: ''
        OSPFAREAID:
          name: 'OSPF区域ID'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TPINENABLE:
          name: '使能入方向的流量策略'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: '-'
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
          description: '-'
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
    set_giredirectfunc_list:
    - V4GIREDIRSWITCH: ENABLE
      V6GIREDIRSWITCH: ENABLE
    add_l3vpninst_list:
    - VRFNAME: 'ispvpn1'
    add_vpninst_list:
    - VPNINSTANCE: 'ispvpn1'
    add_vpninstaf_list:
    - VRFNAME: 'ispvpn1'
      AFTYPE: ipv4uni
      VRFRD: '192.168.225.138:100'
    add_giredirectpara_list:
    - VPNINSTANCE: 'ispvpn1'
      IPTYPE: IPv4
      V4REDIRIPTYPE: IPADDRESS
      IPV4ADDRESS: '10.1.1.1'
      V6REDIRIPTYPE: IPADDRESS
      IPV6ADDRESS: 'FC00::10:1:1:1'
    add_giredirectpara_list_3:
    - VPNINSTANCE: '\_public\_'
      IPTYPE: IPv4
      V4REDIRIPTYPE: IPADDRESS
      IPV4ADDRESS: '10.1.1.1'
      V6REDIRIPTYPE: ''
    add_giredirectpara_list_5:
    - VPNINSTANCE: 'VPN Instance to Bind'
      IPTYPE: IPv6
      V6REDIRIPTYPE: IPADDRESS
      IPV6ADDRESS: 'FC00::10:1:1:1'
      V4REDIRIPTYPE: ''
    set_autoconfig_list:
    - SWITCHFLAG: FALSE
    add_interface_list:
    - IFNAME: 'LoopBack8'
    add_ipbindvpn_list:
    - IFNAME: 'LoopBack8'
      VRFNAME: 'ispvpn1'
    add_ifipv4address_list:
    - IFNAME: 'LoopBack8'
      IFIPADDR: '192.168.225.138'
      SUBNETMASK: '255.255.255.255'
      ADDRTYPE: main
    set_ifipv6enable_list:
    - IFNAME: 'Loopback8'
      ENABLEFLAG: TRUE
      AUTOLINKLOCAL: ''
      MTU: ''
    add_ifipv6address_list:
    - IFNAME: 'Loopback8'
      IPV6ADDRESS: 'FC00::225:138'
      PREFIXLEN: 128
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
    add_bgpvrf_list:
    - VRFNAME: 'ispvpn1'
      DEFAULTAFTYPE: noaf
      ROUTERID: '192.168.225.138'
    add_bgpvrfaf_list:
    - VRFNAME: 'ispvpn1'
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
    - VRFNAME: 'ispvpn1'
      ADDRESSTYPE: ipv4
      PEERADDR: '192.168.78.1'
      REMOTEAS: '60002'
      LOCALIFADDR: '192.168.225.138'
      LOCALIFNAME: 'Loopback8'
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
    add_bgpvrfaf_list_1:
    - VRFNAME: 'ispvpn1'
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
    add_bgppeer_list_2:
    - VRFNAME: 'ispvpn1'
      ADDRESSTYPE: ipv6
      PEERADDRV6: 'FC00::78:1'
      REMOTEAS: '60002'
      LOCALIFADDR: 'FC00::225:138'
      LOCALIFNAME: 'Loopback8'
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
    - VRFNAME: 'ispvpn1'
      AFTYPE: ipv4uni
      IMPORTPROTOCOL: wlr
      MEDENABLE: FALSE
      IMPORTPROCESSID: ''
      MED: ''
    add_routepolicy_list:
    - POLICYNAME: 'routepolicy_deny'
    add_routepolicynode_list:
    - POLICYNAME: 'routepolicy_deny'
      NODESEQUENCE: 50
      MATCHMODE: deny
    add_prefixfilternode_list:
    - NAME: 'ip-prefix_test'
      NODESEQUENCE: 50
      MATCHMODE: deny
      ADDRESS: '0.0.0.0'
      MASKLENGTH: 0
      GREATEREQUAL: 0
      LESSEQUAL: 32
      MATCHNETWORK: FALSE
    add_matchdestprefixfilter_list:
    - POLICYNAME: 'routepolicy_deny'
      NODESEQUENCE: 50
      PREFIXNAME: 'ip-prefix_test'
    mod_bgppeeraf_list:
    - VRFNAME: 'ispvpn1'
      AFTYPE: ipv4uni
      REMOTEADDRESS: '192.168.78.1'
      IMPORTRTPOLICYNAME: 'routepolicy_deny'
      ADDRESSTYPE: ''
      ADDPATHMODE: ''
      ADVADDPATHNUM: ''
      ADVBESTEXTERNAL: ''
      ADVERTISECOMMUNITY: ''
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
    add_ipv6prefixfilternode_list:
    - NAME: 'ip-prefix_test_v6'
      NODESEQUENCE: 50
      MATCHMODE: deny
      ADDRESS: '0:0:0:0:0:0:0:0'
      MASKLENGTH: 0
      MATCHNETWORK: FALSE
      GREATEREQUAL: 0
      LESSEQUAL: 128
    add_matchdestprefix6filter_list:
    - POLICYNAME: 'routepolicy_deny'
      NODESEQUENCE: 50
      IPV6PREFIXNAME: 'ip-prefix_test_v6'
    mod_bgppeeraf_list_2:
    - VRFNAME: 'ispvpn1'
      AFTYPE: ipv6uni
      ADDRESSTYPE: ipv6
      REMOTEADDRESSV6: 'FC00::78:1'
      IMPORTRTPOLICYNAME: 'routepolicy_deny'
      ADVERTISECOMMUNITY: ''
      ADVERTISEEXTCOMMUNITY: ''
      ALLOWASLOOPENABLE: ''
      ALLOWASLOOPLIMIT: ''
      DEFAULTRTADVENABLE: ''
      DEFAULTRTADVPOLICY: ''
      DEFAULTRTMATCHMODE: ''
      DISCARDEXTCOMMUNITY: ''
      EXPORTACL6NAMEORNUM: ''
      EXPORTASPATHFILTER: ''
      EXPORTPREF6FILTNAME: ''
      EXPORTRTPOLICYNAME: ''
      IMPORTACL6NAMEORNUM: ''
      IMPORTASPATHFILTER: ''
      IMPORTPREF6FILTNAME: ''
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
      REMOTEADDRESS: ''
      ROUTELIMIT: ''
      ROUTELIMITIDLETIMEOUT: ''
      ROUTELIMITPERCENT: ''
      ROUTELIMITTYPE: ''
      RTUPDTINTERVAL: ''
      SUBSTITUTEASENABLE: ''
      ADDPATHMODE: ''
      ADVADDPATHNUM: ''
      ADVBESTEXTERNAL: ''
      EXPORTACLNAMEORNUM: ''
      EXPORTPREFFILTNAME: ''
      IMPORTACLNAMEORNUM: ''
      IMPORTPREFFILTNAME: ''
    add_autoscalingethtrunk_list:
    - ETHTRUNKTMPID: 6
      VNICLIST: '6 7'
    add_autoscalingservice_list:
    - SERVICENAME: 'ServName_ispvpn1_2008'
      VPNNAME: 'ispvpn1'
      AFTYPE: IPv4
      IPALLOCTYPE4: USER_CONFIG
      AUTOCFGIFTYPE: ETHTRUNK
      ETHTRUNKTMPID: 6
      VLANID: 2008
      BEGINADDR4: '192.168.88.2'
      ENDADDR4: '192.168.88.30'
      MASKLEN: 27
      IPALLOCTYPE6: USER_CONFIG
      VNICID: ''
    add_autoscalingbfd_list:
    - TEMPLATENAME: 'BFD_2008'
      BFDTYPE: Static
      SERVICENAME: 'ServName_ispvpn1_2008'
      IPVERSION: IPv4
      DESTADDR4: '192.168.88.1'
      MINECHORXINT: 500
      DETECTMULTI: 4
      ONEARMECHO: TRUE
      MINRXINTERVAL: 200
      MINTXINTERVAL: 200
      DESTADDR6: ''
    add_autoscalingsrroute_list:
    - SERVICENAME: 'ServName_ispvpn1_2008'
      VRFNAME: 'ispvpn1'
      IPVERSION: IPv4
      PREFIX4: '192.168.78.1'
      MASKLENGTH: 32
      NEXTHOPALLOCTYPE4: CONFIG
      NEXTHOP4: '192.168.88.1'
      BFDENABLE: TRUE
      DESCRIPTION: 'ispvpn1'
      BFDTEMPLATENAME: 'BFD_2008'
      NEXTHOPALLOCTYPE6: CONFIG
      PREFIX6: ''
    add_autoscalingservice_list_1:
    - SERVICENAME: 'ServName_ispvpn1_2008_v6'
      VPNNAME: 'ispvpn1'
      AFTYPE: IPv6
      IPALLOCTYPE6: USER_CONFIG
      AUTOCFGIFTYPE: ETHTRUNK
      ETHTRUNKTMPID: 6
      VLANID: 2008
      BEGINADDR6: 'FC00::88C2'
      ENDADDR6: 'FC00::88DE'
      MASKLEN: 123
      IPALLOCTYPE4: USER_CONFIG
      VNICID: ''
      ADDRMODE: HOST_MODE
    add_autoscalingbfd_list_1:
    - TEMPLATENAME: 'BFD_2008_v6'
      BFDTYPE: Static
      SERVICENAME: 'ServName_ispvpn1_2008_v6'
      IPVERSION: IPv6
      DESTADDR6: 'FC00::88C1'
      MINECHORXINT: 500
      DETECTMULTI: 4
      ONEARMECHO: TRUE
      MINRXINTERVAL: 200
      MINTXINTERVAL: 200
      DESTADDR4: ''
    add_autoscalingsrroute_list_2:
    - SERVICENAME: 'ServName_ispvpn1_2008_v6'
      VRFNAME: 'ispvpn1'
      IPVERSION: IPv6
      PREFIX6: 'FC00::78:1'
      MASKLENGTH: 128
      NEXTHOPALLOCTYPE6: CONFIG
      NEXTHOP6: 'FC00::88C1'
      BFDENABLE: TRUE
      DESCRIPTION: 'ispvpn1'
      BFDTEMPLATENAME: 'BFD_2008_v6'
      NEXTHOPALLOCTYPE4: CONFIG
      PREFIX4: ''
    add_bgppeer_list_4:
    - VRFNAME: 'ispvpn1'
      ADDRESSTYPE: ipv4
      PEERADDR: '192.168.79.1'
      REMOTEAS: '60002'
      LOCALIFADDR: '192.168.225.138'
      LOCALIFNAME: 'Loopback8'
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
    mod_bgppeeraf_list_4:
    - VRFNAME: 'ispvpn1'
      AFTYPE: ipv4uni
      REMOTEADDRESS: '192.168.79.1'
      EXPORTRTPOLICYNAME: 'routepolicy_deny'
      ADDRESSTYPE: ''
      ADDPATHMODE: ''
      ADVADDPATHNUM: ''
      ADVBESTEXTERNAL: ''
      ADVERTISECOMMUNITY: ''
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
    add_autoscalingservice_list_2:
    - SERVICENAME: 'ServName_ispvpn1_2009'
      VPNNAME: 'ispvpn1'
      AFTYPE: IPv4
      IPALLOCTYPE4: USER_CONFIG
      AUTOCFGIFTYPE: ETHTRUNK
      ETHTRUNKTMPID: 6
      VLANID: 2009
      BEGINADDR4: '192.168.89.2'
      ENDADDR4: '192.168.89.30'
      MASKLEN: 27
      IPALLOCTYPE6: USER_CONFIG
      VNICID: ''
    add_autoscalingbfd_list_2:
    - TEMPLATENAME: 'BFD_2009'
      BFDTYPE: Static
      SERVICENAME: 'ServName_ispvpn1_2009'
      IPVERSION: IPv4
      DESTADDR4: '192.168.89.1'
      MINECHORXINT: 500
      DETECTMULTI: 4
      ONEARMECHO: TRUE
      MINRXINTERVAL: 200
      MINTXINTERVAL: 200
      DESTADDR6: ''
    add_autoscalingsrroute_list_4:
    - SERVICENAME: 'ServName_ispvpn1_2009'
      VRFNAME: 'ispvpn1'
      IPVERSION: IPv4
      PREFIX4: '192.168.79.1'
      MASKLENGTH: 32
      NEXTHOPALLOCTYPE4: CONFIG
      NEXTHOP4: '192.168.89.1'
      BFDENABLE: TRUE
      DESCRIPTION: 'ispvpn1'
      BFDTEMPLATENAME: 'BFD_2009'
      NEXTHOPALLOCTYPE6: CONFIG
      PREFIX6: ''
    add_bgppeer_list_6:
    - VRFNAME: 'ispvpn1'
      ADDRESSTYPE: ipv6
      PEERADDRV6: 'FC00::79:1'
      REMOTEAS: '60002'
      LOCALIFADDR: 'FC00::225:138'
      LOCALIFNAME: 'Loopback8'
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
    mod_bgppeeraf_list_6:
    - VRFNAME: 'ispvpn1'
      AFTYPE: ipv6uni
      ADDRESSTYPE: ipv6
      REMOTEADDRESSV6: 'FC00::79:1'
      EXPORTRTPOLICYNAME: 'routepolicy_deny'
      ADVERTISECOMMUNITY: ''
      ADVERTISEEXTCOMMUNITY: ''
      ALLOWASLOOPENABLE: ''
      ALLOWASLOOPLIMIT: ''
      DEFAULTRTADVENABLE: ''
      DEFAULTRTADVPOLICY: ''
      DEFAULTRTMATCHMODE: ''
      DISCARDEXTCOMMUNITY: ''
      EXPORTACL6NAMEORNUM: ''
      EXPORTASPATHFILTER: ''
      EXPORTPREF6FILTNAME: ''
      IMPORTACL6NAMEORNUM: ''
      IMPORTASPATHFILTER: ''
      IMPORTPREF6FILTNAME: ''
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
      REMOTEADDRESS: ''
      ROUTELIMIT: ''
      ROUTELIMITIDLETIMEOUT: ''
      ROUTELIMITPERCENT: ''
      ROUTELIMITTYPE: ''
      RTUPDTINTERVAL: ''
      SUBSTITUTEASENABLE: ''
      ADDPATHMODE: ''
      ADVADDPATHNUM: ''
      ADVBESTEXTERNAL: ''
      EXPORTACLNAMEORNUM: ''
      EXPORTPREFFILTNAME: ''
      IMPORTACLNAMEORNUM: ''
      IMPORTPREFFILTNAME: ''
    add_autoscalingservice_list_3:
    - SERVICENAME: 'ServName_ispvpn1_2009_v6'
      VPNNAME: 'ispvpn1'
      AFTYPE: IPv6
      IPALLOCTYPE6: USER_CONFIG
      AUTOCFGIFTYPE: ETHTRUNK
      ETHTRUNKTMPID: 6
      VLANID: 2009
      BEGINADDR6: 'FC00::89C2'
      ENDADDR6: 'FC00::89DE'
      MASKLEN: 123
      IPALLOCTYPE4: USER_CONFIG
      VNICID: ''
      ADDRMODE: HOST_MODE
    add_autoscalingbfd_list_3:
    - TEMPLATENAME: 'BFD_2009_v6'
      BFDTYPE: Static
      SERVICENAME: 'ServName_ispvpn1_2009_v6'
      IPVERSION: IPv6
      DESTADDR6: 'FC00::89C1'
      MINECHORXINT: 500
      DETECTMULTI: 4
      ONEARMECHO: TRUE
      MINRXINTERVAL: 200
      MINTXINTERVAL: 200
      DESTADDR4: ''
    add_autoscalingsrroute_list_6:
    - SERVICENAME: 'ServName_ispvpn1_2009_v6'
      VRFNAME: 'ispvpn1'
      IPVERSION: IPv6
      PREFIX6: 'FC00::79:1'
      MASKLENGTH: 128
      NEXTHOPALLOCTYPE6: CONFIG
      NEXTHOP6: 'FC00::89C1'
      BFDENABLE: TRUE
      DESCRIPTION: 'ispvpn1'
      BFDTEMPLATENAME: 'BFD_2009_v6'
      NEXTHOPALLOCTYPE4: CONFIG
      PREFIX4: ''
    set_bfd_list_1:
    - BFDENABLE: TRUE
    add_ospf_list:
    - PROCID: 8
      VRFNAME: 'ispvpn1'
      SCHEMAROUID: '192.168.225.138'
      BFDALLINTFFLG: TRUE
      BFDRXCFGFLAG: TRUE
      BFDMINRXINTV: 500
      BFDTXCFGFLAG: TRUE
      BFDMINTXINTV: 500
      SCHEMABFDDETMUL: 4
      LSAARRINTVFLAG: FALSE
      LSAARRMAXINTV: 1000
      LSAARRSTARINTV: 500
      LSAARRHLDINTV: 500
      VPNINSCAPSIMFLG: TRUE
      VIRTUALSYSFLAG: TRUE
      LSAARRINTV: ''
    add_ospfarea_list:
    - PROCID: 8
      AREAID: '0.0.0.5'
      AREATYPE: NSSA
      MAXCOSTFLAG: FALSE
      DEFAULTCOST: 1
      NSSADEFAULTROUTEADVERTISE: FALSE
      NSSANOIMPORTROUTE: FALSE
      NSSANOSUMMARY: FALSE
      NSSASETNBIT: FALSE
      NSSASUPPRESSFORWARDINGADDRESS: FALSE
      NSSATRANSLATORALWAYS: FALSE
      NSSATRANSLATORINTERVAL: 40
      NSSAZEROADDRESSFORWARDING: FALSE
      STUBNOSUMMARY: FALSE
      MAXCOSTINTVL: ''
    add_ospfimportroute_list:
    - PROCID: 8
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
    add_ospfv3_list:
    - PROCID: 8
      ROUTERID: '192.168.225.138'
      VRFNAME: 'ispvpn1'
      BFDALLINTFFLG: TRUE
      BFDRXCFGFLAG: TRUE
      BFDMINRXINTV: 500
      BFDTXCFGFLAG: TRUE
      BFDMINTXINTV: 500
      DETECTMULINTV: 4
      VPNINSCAPSIMFLG: TRUE
      VIRTUALSYSFLAG: TRUE
    add_ospfv3area_list:
    - PROCID: 8
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
    - PROCID: 8
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
    add_routepolicy_list_1:
    - POLICYNAME: 'routepolicy_deny'
    add_routepolicynode_list_1:
    - POLICYNAME: 'routepolicy_deny'
      NODESEQUENCE: 50
      MATCHMODE: deny
    add_prefixfilternode_list_1:
    - NAME: 'ip-prefix_test'
      NODESEQUENCE: 50
      MATCHMODE: deny
      ADDRESS: '0.0.0.0'
      MASKLENGTH: 0
      GREATEREQUAL: 0
      LESSEQUAL: 32
      MATCHNETWORK: FALSE
    add_matchdestprefixfilter_list_1:
    - POLICYNAME: 'routepolicy_deny'
      NODESEQUENCE: 50
      PREFIXNAME: 'ip-prefix_test'
    add_ospffilterpolicy_list:
    - PROCID: 8
      FILTERTYPE: import
      TYPE: ip_prefix
      IPPREFIX: 'ip-prefix_test'
      PROTOCOL: Total
      ACLNAMEORNUM: ''
      ROUTEPLYNAME: ''
      SECONDARYFLAG: FALSE
    add_interface_list_1:
    - IFNAME: 'LoopBack8'
    add_ipbindvpn_list_1:
    - IFNAME: 'LoopBack8'
      VRFNAME: 'ispvpn1'
    add_ifipv4address_list_1:
    - IFNAME: 'LoopBack8'
      IFIPADDR: '192.168.225.138'
      SUBNETMASK: '255.255.255.255'
      ADDRTYPE: main
    add_ospfinterface_list:
    - PROCID: 8
      AREAID: '0.0.0.5'
      IFNAME: 'LoopBack8'
    add_ipv6prefixfilternode_list_1:
    - NAME: 'ip-prefix_test_v6'
      NODESEQUENCE: 50
      MATCHMODE: deny
      ADDRESS: '0:0:0:0:0:0:0:0'
      MASKLENGTH: 0
      MATCHNETWORK: FALSE
      GREATEREQUAL: 0
      LESSEQUAL: 128
    add_matchdestprefix6filter_list_1:
    - POLICYNAME: 'routepolicy_deny'
      NODESEQUENCE: 50
      IPV6PREFIXNAME: 'ip-prefix_test_v6'
    add_ospfv3filterpolicy_list:
    - PROCID: 8
      FILTERTYPE: import
      TYPE: ip_prefix
      IPPREFIX: 'ip-prefix_test_v6'
      PROTOCOL: ''
      ACLNAMEORNUM: ''
      ROUTEPLYNAME: ''
    add_autoscalingethtrunk_list_1:
    - ETHTRUNKTMPID: 6
      VNICLIST: '6 7'
    add_autoscalingservice_list_4:
    - SERVICENAME: 'ServName_ispvpn1_2008'
      VPNNAME: 'ispvpn1'
      AFTYPE: IPv4
      IPALLOCTYPE4: USER_CONFIG
      AUTOCFGIFTYPE: ETHTRUNK
      ETHTRUNKTMPID: 6
      VLANID: 2008
      BEGINADDR4: '192.168.88.2'
      ENDADDR4: '192.168.88.30'
      MASKLEN: 27
      OSPFENABLE: TRUE
      OSPFPROCID: 8
      OSPFAREAID: '0.0.0.5'
      TPINENABLE: FALSE
      TPOUTENABLE: FALSE
      IPALLOCTYPE6: USER_CONFIG
      BEGINADDR6: 'FC00::88C2'
      ENDADDR6: 'FC00::88DE'
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
    add_ospf_list_1:
    - PROCID: 9
      VRFNAME: 'ispvpn1'
      SCHEMAROUID: '192.168.225.138'
      BFDALLINTFFLG: TRUE
      BFDRXCFGFLAG: TRUE
      BFDMINRXINTV: 500
      BFDTXCFGFLAG: TRUE
      BFDMINTXINTV: 500
      SCHEMABFDDETMUL: 4
      LSAARRINTVFLAG: FALSE
      LSAARRMAXINTV: 1000
      LSAARRSTARINTV: 500
      LSAARRHLDINTV: 500
      VPNINSCAPSIMFLG: TRUE
      VIRTUALSYSFLAG: TRUE
      LSAARRINTV: ''
    add_ospfarea_list_1:
    - PROCID: 9
      AREAID: '0.0.0.5'
      AREATYPE: NSSA
      MAXCOSTFLAG: FALSE
      DEFAULTCOST: 1
      NSSADEFAULTROUTEADVERTISE: FALSE
      NSSANOIMPORTROUTE: FALSE
      NSSANOSUMMARY: FALSE
      NSSASETNBIT: FALSE
      NSSASUPPRESSFORWARDINGADDRESS: FALSE
      NSSATRANSLATORALWAYS: FALSE
      NSSATRANSLATORINTERVAL: 40
      NSSAZEROADDRESSFORWARDING: FALSE
      STUBNOSUMMARY: FALSE
      MAXCOSTINTVL: ''
    add_ospffilterpolicy_list_1:
    - PROCID: 9
      FILTERTYPE: export
      TYPE: ip_prefix
      IPPREFIX: 'ip-prefix_test'
      PROTOCOL: wlr
      PROTOCOLPROCESSID: 1
      ACLNAMEORNUM: ''
      ROUTEPLYNAME: ''
      SECONDARYFLAG: FALSE
    add_autoscalingservice_list_6:
    - SERVICENAME: 'ServName_ispvpn1_2009'
      VPNNAME: 'ispvpn1'
      AFTYPE: IPv4
      IPALLOCTYPE4: USER_CONFIG
      AUTOCFGIFTYPE: ETHTRUNK
      ETHTRUNKTMPID: 6
      VLANID: 2009
      BEGINADDR4: '192.168.89.2'
      ENDADDR4: '192.168.89.30'
      MASKLEN: 27
      OSPFENABLE: TRUE
      OSPFPROCID: 9
      OSPFAREAID: '0.0.0.5'
      TPINENABLE: FALSE
      TPOUTENABLE: FALSE
      IPALLOCTYPE6: USER_CONFIG
      VNICID: ''
      OSPFCOST: ''
      OSPFDEADTIMER: ''
      OSPFGRPENABLE: FALSE
      OSPFHELLOTIMER: ''
      OSPFINSTID: ''
      TPINLINKFLAG: FALSE
      TPINNAME: ''
      TPOUTLINKFLAG: FALSE
      TPOUTNAME: ''
    add_ospfv3_list_1:
    - PROCID: 9
      ROUTERID: '192.168.225.138'
      VRFNAME: 'ispvpn1'
      BFDALLINTFFLG: TRUE
      BFDRXCFGFLAG: TRUE
      BFDMINRXINTV: 500
      BFDTXCFGFLAG: TRUE
      BFDMINTXINTV: 500
      DETECTMULINTV: 4
      VPNINSCAPSIMFLG: TRUE
      VIRTUALSYSFLAG: TRUE
    add_ospfv3area_list_1:
    - PROCID: 9
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
    add_ospfv3filterpolicy_list_1:
    - PROCID: 9
      FILTERTYPE: export
      TYPE: ip_prefix
      IPPREFIX: 'ip-prefix_test_v6'
      PROTOCOL: wlr
      PROTOCOLPROCESSID: 1
      ACLNAMEORNUM: ''
      ROUTEPLYNAME: ''
    add_autoscalingservice_list_7:
    - SERVICENAME: 'ServName_ispvpn1_2009_v6'
      VPNNAME: 'ispvpn1'
      AFTYPE: IPv6
      IPALLOCTYPE6: USER_CONFIG
      AUTOCFGIFTYPE: ETHTRUNK
      ETHTRUNKTMPID: 6
      VLANID: 2009
      BEGINADDR6: 'FC00::89C2'
      ENDADDR6: 'FC00::89DE'
      MASKLEN: 123
      OSPFENABLE: TRUE
      OSPFPROCID: 9
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

### 1 以下命令在“MML命令行 - UDG”窗口上执行。设置全局的SGi重定向开关。

```jinja2
{%- for item in set_giredirectfunc_list -%}
    SET GIREDIRECTFUNC:
    {#- --- 必选参数 --- -#}
    V4GIREDIRSWITCH={{item.V4GIREDIRSWITCH}},
    V6GIREDIRSWITCH={{item.V6GIREDIRSWITCH}},
    ;
{%- endfor -%}
```

### 当全局的SGi接口重定向开关为不使能时，整个UDG的所有VPN的SGi接口重定向功能都会被关闭。使能全局的SGi接口重定向后，还要根据各个VPN的重定向配置来决定是否进行SGi接口的重定向。

### 2 配置VPN实例。

```jinja2
{%- for item in add_l3vpninst_list -%}
    ADD L3VPNINST:
    {#- --- 必选参数 --- -#}
    VRFNAME="{{item.VRFNAME}}",
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_vpninst_list -%}
    ADD VPNINST:
    {#- --- 必选参数 --- -#}
    VPNINSTANCE="{{item.VPNINSTANCE}}",
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

### 3 设置基于某个VPN的SGi重定向开关及重定向报文的目的地址。

```jinja2
{%- for item in add_giredirectpara_list -%}
    ADD GIREDIRECTPARA:
    {#- --- 必选参数 --- -#}
    VPNINSTANCE="{{item.VPNINSTANCE}}",
    IPTYPE={{item.IPTYPE}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPTYPE=IPv4 时必选 --- -#}
    {%- if item.IPTYPE == 'IPv4' -%}
        V4REDIRIPTYPE={{item.V4REDIRIPTYPE}},
    {%- endif -%}
    {#- --- 条件必选：V4REDIRIPTYPE=IPADDRESS 时必选 --- -#}
    {%- if item.V4REDIRIPTYPE == 'IPADDRESS' -%}
        IPV4ADDRESS="{{item.IPV4ADDRESS}}",
    {%- endif -%}
    {#- --- 条件必选：IPTYPE=IPv6 时必选 --- -#}
    {%- if item.IPTYPE == 'IPv6' -%}
        V6REDIRIPTYPE={{item.V6REDIRIPTYPE}},
    {%- endif -%}
    {#- --- 条件必选：V6REDIRIPTYPE=IPADDRESS 时必选 --- -#}
    {%- if item.V6REDIRIPTYPE == 'IPADDRESS' -%}
        IPV6ADDRESS="{{item.IPV6ADDRESS}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 设置默认VPN（\_public\_）用户的SGi重定向开关及重定向报文的目的地址。

```jinja2
{%- for item in add_giredirectpara_list_3 -%}
    ADD GIREDIRECTPARA:
    {#- --- 必选参数 --- -#}
    VPNINSTANCE="{{item.VPNINSTANCE}}",
    IPTYPE={{item.IPTYPE}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPTYPE=IPv4 时必选 --- -#}
    {%- if item.IPTYPE == 'IPv4' -%}
        V4REDIRIPTYPE={{item.V4REDIRIPTYPE}},
    {%- endif -%}
    {#- --- 条件必选：V4REDIRIPTYPE=IPADDRESS 时必选 --- -#}
    {%- if item.V4REDIRIPTYPE == 'IPADDRESS' -%}
        IPV4ADDRESS="{{item.IPV4ADDRESS}}",
    {%- endif -%}
    {#- --- 条件必选：IPTYPE=IPv6 时必选 --- -#}
    {%- if item.IPTYPE == 'IPv6' -%}
        V6REDIRIPTYPE={{item.V6REDIRIPTYPE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 设置IPv6 Gi redirect。

```jinja2
{%- for item in add_giredirectpara_list_5 -%}
    ADD GIREDIRECTPARA:
    {#- --- 必选参数 --- -#}
    VPNINSTANCE="{{item.VPNINSTANCE}}",
    IPTYPE={{item.IPTYPE}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPTYPE=IPv6 时必选 --- -#}
    {%- if item.IPTYPE == 'IPv6' -%}
        V6REDIRIPTYPE={{item.V6REDIRIPTYPE}},
    {%- endif -%}
    {#- --- 条件必选：V6REDIRIPTYPE=IPADDRESS 时必选 --- -#}
    {%- if item.V6REDIRIPTYPE == 'IPADDRESS' -%}
        IPV6ADDRESS="{{item.IPV6ADDRESS}}",
    {%- endif -%}
    {#- --- 条件必选：IPTYPE=IPv4 时必选 --- -#}
    {%- if item.IPTYPE == 'IPv4' -%}
        V4REDIRIPTYPE={{item.V4REDIRIPTYPE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 5 关闭自动配置开关。

#### 5.1 查询自动配置开关。

#### 如果“自动配置开关”值为“是”，需要执行5.b和5.c关闭自动配置开关。

#### 如果“自动配置开关”值为“否”，说明已关闭自动配置开关，请跳转到6或7。

#### 5.2 查询自动部署维护助手“autoscaling\_autoconfig.py”的状态，确保状态为“准备好状态（Ready）”或者查询无该脚本，以保证当前设备不在自动部署过程中。因为若系统当前有正在进行的自动部署，而自动部署生效有时延，此时若关闭自动配置开关，会影响系统配置效果。

#### 5.3 关闭自动配置开关。自动化配置命令只有在自动配置开关为关闭的状态下才可执行，因此需要提前关闭。

```jinja2
{%- set LST_AUTOCONFIG=getParameterValue('LST AUTOCONFIG') -%}
{%- if LST_AUTOCONFIG=='是' -%}
    {%- for item in set_autoconfig_list -%}
        SET AUTOCONFIG:
        {#- --- 必选参数 --- -#}
        SWITCHFLAG={{item.SWITCHFLAG}},
        ;
    {%- endfor -%}
{%- endif -%}
```

### 6 配置外联口IP及路由。

### 详细操作步骤请参见《UDG 初始配置与调测》。

### 采用BGP over静态路由时，配置外联口IP及路由。此处以APN绑定的VPN实例是ispvpn1为例。

### 上下行的配置区别是：PGW-U/UPF上下行使用的子接口不同，VLAN不同，外联口IP地址不同，BGP Peer IP不同，VPN相同，BGP本端IP相同，且上行不需要引入wlr路由。如图3所示。

### 如下PGW-U/UPF脚本以对接2个DC-GW（M-LAG组网）为例，为方便绘图，图形中仅呈现一个DC-GW图标。

#### 6.1 配置下行报文使用的外联口IP及路由。UDG用于接收重定向设备、PDN/DN Server发送的UE报文。IPv4组网时，不接收BGP Peer 192.168.78.1和192.168.78.2发布的任何路由。IPv6组网时，不接收BGP Peer FC00::78:1和FC00::78:2发布的任何路由。

```jinja2
{%- if is_scenario_bgp_over_static_route -%}
    {%- for item in add_interface_list -%}
        ADD INTERFACE:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_bgp_over_static_route -%}
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
{%- if is_scenario_bgp_over_static_route -%}
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
{%- if is_scenario_bgp_over_static_route -%}
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

```jinja2
{%- if is_scenario_bgp_over_static_route -%}
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

```jinja2
{%- if is_scenario_bgp_over_static_route -%}
    {%- for item in set_bfd_list -%}
        SET BFD:
        {#- --- 必选参数 --- -#}
        BFDENABLE={{item.BFDENABLE}},
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_bgp_over_static_route -%}
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
{%- endif -%}
```

```jinja2
{%- if is_scenario_bgp_over_static_route -%}
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

```jinja2
{%- if is_scenario_bgp_over_static_route -%}
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
{%- endif -%}
```

```jinja2
{%- if is_scenario_bgp_over_static_route -%}
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
{%- endif -%}
```

```jinja2
{%- if is_scenario_bgp_over_static_route -%}
    {%- for item in add_bgpvrfaf_list_1 -%}
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

```jinja2
{%- if is_scenario_bgp_over_static_route -%}
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
{%- endif -%}
```

```jinja2
{%- if is_scenario_bgp_over_static_route -%}
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

```jinja2
{%- if is_scenario_bgp_over_static_route -%}
    {%- for item in add_routepolicy_list -%}
        ADD ROUTEPOLICY:
        {#- --- 必选参数 --- -#}
        POLICYNAME="{{item.POLICYNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_bgp_over_static_route -%}
    {%- for item in add_routepolicynode_list -%}
        ADD ROUTEPOLICYNODE:
        {#- --- 必选参数 --- -#}
        POLICYNAME="{{item.POLICYNAME}}",
        NODESEQUENCE={{item.NODESEQUENCE}},
        MATCHMODE={{item.MATCHMODE}},
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_bgp_over_static_route -%}
    {%- for item in add_prefixfilternode_list -%}
        ADD PREFIXFILTERNODE:
        {#- --- 必选参数 --- -#}
        NAME="{{item.NAME}}",
        NODESEQUENCE={{item.NODESEQUENCE}},
        MATCHMODE={{item.MATCHMODE}},
        ADDRESS="{{item.ADDRESS}}",
        MASKLENGTH={{item.MASKLENGTH}},
        {#- --- 可选参数 --- -#}
        {%- if item.GREATEREQUAL is not none -%}
            GREATEREQUAL={{item.GREATEREQUAL}},
        {%- endif -%}
        {%- if item.LESSEQUAL is not none -%}
            LESSEQUAL={{item.LESSEQUAL}},
        {%- endif -%}
        {%- if item.MATCHNETWORK is not none -%}
            MATCHNETWORK={{item.MATCHNETWORK}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_bgp_over_static_route -%}
    {%- for item in add_matchdestprefixfilter_list -%}
        ADD MATCHDESTPREFIXFILTER:
        {#- --- 必选参数 --- -#}
        POLICYNAME="{{item.POLICYNAME}}",
        NODESEQUENCE={{item.NODESEQUENCE}},
        PREFIXNAME="{{item.PREFIXNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_bgp_over_static_route -%}
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
            {%- if item.IMPORTRTPOLICYNAME is not none -%}
                IMPORTRTPOLICYNAME="{{item.IMPORTRTPOLICYNAME}}",
            {%- endif -%}
        {#- --- 条件可选：AFTYPE=ipv4uni/ipv4vpn/ipv6vpn 时可选 --- -#}
        {%- elif item.AFTYPE in ['ipv4uni', 'ipv4vpn', 'ipv6vpn'] -%}
            {%- if item.IMPORTRTPOLICYNAME is not none -%}
                IMPORTRTPOLICYNAME="{{item.IMPORTRTPOLICYNAME}}",
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

```jinja2
{%- if is_scenario_bgp_over_static_route -%}
    {%- for item in add_ipv6prefixfilternode_list -%}
        ADD IPV6PREFIXFILTERNODE:
        {#- --- 必选参数 --- -#}
        NAME="{{item.NAME}}",
        NODESEQUENCE={{item.NODESEQUENCE}},
        MATCHMODE={{item.MATCHMODE}},
        ADDRESS="{{item.ADDRESS}}",
        MASKLENGTH={{item.MASKLENGTH}},
        {#- --- 可选参数 --- -#}
        {%- if item.MATCHNETWORK is not none -%}
            MATCHNETWORK={{item.MATCHNETWORK}},
        {%- endif -%}
        {%- if item.GREATEREQUAL is not none -%}
            GREATEREQUAL={{item.GREATEREQUAL}},
        {%- endif -%}
        {%- if item.LESSEQUAL is not none -%}
            LESSEQUAL={{item.LESSEQUAL}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_bgp_over_static_route -%}
    {%- for item in add_matchdestprefix6filter_list -%}
        ADD MATCHDESTPREFIX6FILTER:
        {#- --- 必选参数 --- -#}
        POLICYNAME="{{item.POLICYNAME}}",
        NODESEQUENCE={{item.NODESEQUENCE}},
        IPV6PREFIXNAME="{{item.IPV6PREFIXNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_bgp_over_static_route -%}
    {%- for item in mod_bgppeeraf_list_2 -%}
        MOD BGPPEERAF:
        {#- --- 必选参数 --- -#}
        VRFNAME="{{item.VRFNAME}}",
        AFTYPE={{item.AFTYPE}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：AFTYPE=ipv6uni 时必选 --- -#}
        {%- if item.AFTYPE == 'ipv6uni' -%}
            ADDRESSTYPE={{item.ADDRESSTYPE}},
        {%- endif -%}
        {#- --- 条件必选：ADDRESSTYPE=ipv6 时必选 --- -#}
        {%- if item.ADDRESSTYPE == 'ipv6' -%}
            REMOTEADDRESSV6="{{item.REMOTEADDRESSV6}}",
        {%- endif -%}
        {#- --- 条件必选：ADDRESSTYPE=ipv4 时必选 --- -#}
        {%- if item.ADDRESSTYPE == 'ipv4' -%}
            REMOTEADDRESS="{{item.REMOTEADDRESS}}",
        {#- --- 条件必选：AFTYPE=ipv4uni/ipv4vpn/ipv6vpn 时必选 --- -#}
        {%- elif item.AFTYPE in ['ipv4uni', 'ipv4vpn', 'ipv6vpn'] -%}
            REMOTEADDRESS="{{item.REMOTEADDRESS}}",
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
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

```jinja2
{%- if is_scenario_bgp_over_static_route -%}
    {%- for item in add_autoscalingethtrunk_list -%}
        ADD AUTOSCALINGETHTRUNK:
        {#- --- 必选参数 --- -#}
        ETHTRUNKTMPID={{item.ETHTRUNKTMPID}},
        VNICLIST="{{item.VNICLIST}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_bgp_over_static_route -%}
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
{%- endif -%}
```

```jinja2
{%- if is_scenario_bgp_over_static_route -%}
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

```jinja2
{%- if is_scenario_bgp_over_static_route -%}
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
        {%- if item.DESCRIPTION is not none -%}
            DESCRIPTION="{{item.DESCRIPTION}}",
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
{%- endif -%}
```

```jinja2
{%- if is_scenario_bgp_over_static_route -%}
    {%- for item in add_autoscalingservice_list_1 -%}
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
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_bgp_over_static_route -%}
    {%- for item in add_autoscalingbfd_list_1 -%}
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
        {#- --- 条件必选：IPVERSION=IPv6 时必选 --- -#}
        {%- if item.IPVERSION == 'IPv6' -%}
            DESTADDR6="{{item.DESTADDR6}}",
        {%- endif -%}
        {#- --- 条件必选：IPVERSION=IPv4 时必选 --- -#}
        {%- if item.IPVERSION == 'IPv4' -%}
            DESTADDR4="{{item.DESTADDR4}}",
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

```jinja2
{%- if is_scenario_bgp_over_static_route -%}
    {%- for item in add_autoscalingsrroute_list_2 -%}
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
        {%- if item.DESCRIPTION is not none -%}
            DESCRIPTION="{{item.DESCRIPTION}}",
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：IPVERSION=IPv6 时必选 --- -#}
        {%- if item.IPVERSION == 'IPv6' -%}
            PREFIX6="{{item.PREFIX6}}",
        {%- endif -%}
        {#- --- 条件必选：NEXTHOPALLOCTYPE6=CONFIG 时必选 --- -#}
        {%- if item.NEXTHOPALLOCTYPE6 == 'CONFIG' -%}
            NEXTHOP6="{{item.NEXTHOP6}}",
        {%- endif -%}
        {#- --- 条件必选：IPVERSION=IPv4 时必选 --- -#}
        {%- if item.IPVERSION == 'IPv4' -%}
            PREFIX4="{{item.PREFIX4}}",
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：IPVERSION=IPv6 时可选 --- -#}
        {%- if item.IPVERSION == 'IPv6' -%}
            {%- if item.NEXTHOPALLOCTYPE6 is not none -%}
                NEXTHOPALLOCTYPE6={{item.NEXTHOPALLOCTYPE6}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：BFDENABLE=TRUE 时可选 --- -#}
        {%- if item.BFDENABLE == 'TRUE' -%}
            {%- if item.BFDTEMPLATENAME is not none -%}
                BFDTEMPLATENAME="{{item.BFDTEMPLATENAME}}",
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：IPVERSION=IPv4 时可选 --- -#}
        {%- if item.IPVERSION == 'IPv4' -%}
            {%- if item.NEXTHOPALLOCTYPE4 is not none -%}
                NEXTHOPALLOCTYPE4={{item.NEXTHOPALLOCTYPE4}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 6.2 配置上行报文使用的外联口IP及路由。UDG用于发送上行报文到重定向设备、PDN/DN Server。IPv4组网时，不向BGP Peer 192.168.79.1和192.168.79.2发布任何路由。IPv6组网时，不向BGP Peer FC00::79:1和FC00::79:2发布任何路由。

```jinja2
{%- if is_scenario_bgp_over_static_route -%}
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
{%- endif -%}
```

```jinja2
{%- if is_scenario_bgp_over_static_route -%}
    {%- for item in mod_bgppeeraf_list_4 -%}
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
            {%- if item.EXPORTRTPOLICYNAME is not none -%}
                EXPORTRTPOLICYNAME="{{item.EXPORTRTPOLICYNAME}}",
            {%- endif -%}
        {#- --- 条件可选：AFTYPE=ipv4uni/ipv4vpn/ipv6vpn 时可选 --- -#}
        {%- elif item.AFTYPE in ['ipv4uni', 'ipv4vpn', 'ipv6vpn'] -%}
            {%- if item.EXPORTRTPOLICYNAME is not none -%}
                EXPORTRTPOLICYNAME="{{item.EXPORTRTPOLICYNAME}}",
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

```jinja2
{%- if is_scenario_bgp_over_static_route -%}
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

```jinja2
{%- if is_scenario_bgp_over_static_route -%}
    {%- for item in add_autoscalingbfd_list_2 -%}
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

```jinja2
{%- if is_scenario_bgp_over_static_route -%}
    {%- for item in add_autoscalingsrroute_list_4 -%}
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
        {%- if item.DESCRIPTION is not none -%}
            DESCRIPTION="{{item.DESCRIPTION}}",
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
{%- endif -%}
```

```jinja2
{%- if is_scenario_bgp_over_static_route -%}
    {%- for item in add_bgppeer_list_6 -%}
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
{%- endif -%}
```

```jinja2
{%- if is_scenario_bgp_over_static_route -%}
    {%- for item in mod_bgppeeraf_list_6 -%}
        MOD BGPPEERAF:
        {#- --- 必选参数 --- -#}
        VRFNAME="{{item.VRFNAME}}",
        AFTYPE={{item.AFTYPE}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：AFTYPE=ipv6uni 时必选 --- -#}
        {%- if item.AFTYPE == 'ipv6uni' -%}
            ADDRESSTYPE={{item.ADDRESSTYPE}},
        {%- endif -%}
        {#- --- 条件必选：ADDRESSTYPE=ipv6 时必选 --- -#}
        {%- if item.ADDRESSTYPE == 'ipv6' -%}
            REMOTEADDRESSV6="{{item.REMOTEADDRESSV6}}",
        {%- endif -%}
        {#- --- 条件必选：ADDRESSTYPE=ipv4 时必选 --- -#}
        {%- if item.ADDRESSTYPE == 'ipv4' -%}
            REMOTEADDRESS="{{item.REMOTEADDRESS}}",
        {#- --- 条件必选：AFTYPE=ipv4uni/ipv4vpn/ipv6vpn 时必选 --- -#}
        {%- elif item.AFTYPE in ['ipv4uni', 'ipv4vpn', 'ipv6vpn'] -%}
            REMOTEADDRESS="{{item.REMOTEADDRESS}}",
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
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

```jinja2
{%- if is_scenario_bgp_over_static_route -%}
    {%- for item in add_autoscalingservice_list_3 -%}
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
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_bgp_over_static_route -%}
    {%- for item in add_autoscalingbfd_list_3 -%}
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
        {#- --- 条件必选：IPVERSION=IPv6 时必选 --- -#}
        {%- if item.IPVERSION == 'IPv6' -%}
            DESTADDR6="{{item.DESTADDR6}}",
        {%- endif -%}
        {#- --- 条件必选：IPVERSION=IPv4 时必选 --- -#}
        {%- if item.IPVERSION == 'IPv4' -%}
            DESTADDR4="{{item.DESTADDR4}}",
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

```jinja2
{%- if is_scenario_bgp_over_static_route -%}
    {%- for item in add_autoscalingsrroute_list_6 -%}
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
        {%- if item.DESCRIPTION is not none -%}
            DESCRIPTION="{{item.DESCRIPTION}}",
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：IPVERSION=IPv6 时必选 --- -#}
        {%- if item.IPVERSION == 'IPv6' -%}
            PREFIX6="{{item.PREFIX6}}",
        {%- endif -%}
        {#- --- 条件必选：NEXTHOPALLOCTYPE6=CONFIG 时必选 --- -#}
        {%- if item.NEXTHOPALLOCTYPE6 == 'CONFIG' -%}
            NEXTHOP6="{{item.NEXTHOP6}}",
        {%- endif -%}
        {#- --- 条件必选：IPVERSION=IPv4 时必选 --- -#}
        {%- if item.IPVERSION == 'IPv4' -%}
            PREFIX4="{{item.PREFIX4}}",
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：IPVERSION=IPv6 时可选 --- -#}
        {%- if item.IPVERSION == 'IPv6' -%}
            {%- if item.NEXTHOPALLOCTYPE6 is not none -%}
                NEXTHOPALLOCTYPE6={{item.NEXTHOPALLOCTYPE6}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：BFDENABLE=TRUE 时可选 --- -#}
        {%- if item.BFDENABLE == 'TRUE' -%}
            {%- if item.BFDTEMPLATENAME is not none -%}
                BFDTEMPLATENAME="{{item.BFDTEMPLATENAME}}",
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：IPVERSION=IPv4 时可选 --- -#}
        {%- if item.IPVERSION == 'IPv4' -%}
            {%- if item.NEXTHOPALLOCTYPE4 is not none -%}
                NEXTHOPALLOCTYPE4={{item.NEXTHOPALLOCTYPE4}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 7 采用OSPF动态路由时，配置外联口IP及路由。此处以APN绑定的VPN实例是ispvpn1为例，如其他APN还绑定其他VPN（如\_public\_），请参考本步骤进行配置。

### 上下行的配置区别是：上下行使用的子接口不同，VLAN不同，外联口IP地址不同，OSPF进程ID不同，VPN相同，OSPF Area ID相同，OSPF的loopback 接口IP相同，且上行不需要引入wlr路由。如图4所示。

#### 7.1 配置下行报文使用的外联口IP及路由。UDG用于接收重定向设备、PDN/DN Server发送的UE报文。该OSPF进程不接收任何路由。

```jinja2
{%- if is_scenario_ospf_dynamic_route -%}
    {%- for item in set_bfd_list_1 -%}
        SET BFD:
        {#- --- 必选参数 --- -#}
        BFDENABLE={{item.BFDENABLE}},
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_ospf_dynamic_route -%}
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
        {%- if item.BFDRXCFGFLAG is not none -%}
            BFDRXCFGFLAG={{item.BFDRXCFGFLAG}},
        {%- endif -%}
        {%- if item.BFDTXCFGFLAG is not none -%}
            BFDTXCFGFLAG={{item.BFDTXCFGFLAG}},
        {%- endif -%}
        {%- if item.SCHEMABFDDETMUL is not none -%}
            SCHEMABFDDETMUL={{item.SCHEMABFDDETMUL}},
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
        {#- --- 条件必选：BFDRXCFGFLAG=TRUE 时必选 --- -#}
        {%- if item.BFDRXCFGFLAG == 'TRUE' -%}
            BFDMINRXINTV={{item.BFDMINRXINTV}},
        {%- endif -%}
        {#- --- 条件必选：BFDTXCFGFLAG=TRUE 时必选 --- -#}
        {%- if item.BFDTXCFGFLAG == 'TRUE' -%}
            BFDMINTXINTV={{item.BFDMINTXINTV}},
        {%- endif -%}
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
        {#- --- 条件必选：LSAARRINTVFLAG=TRUE 时必选 --- -#}
        {%- if item.LSAARRINTVFLAG == 'TRUE' -%}
            LSAARRINTV={{item.LSAARRINTV}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_ospf_dynamic_route -%}
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
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：MAXCOSTFLAG=TRUE 时必选 --- -#}
        {%- if item.MAXCOSTFLAG == 'TRUE' -%}
            MAXCOSTINTVL={{item.MAXCOSTINTVL}},
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
            {%- if item.NSSASUPPRESSFORWARDINGADDRESS is not none -%}
                NSSASUPPRESSFORWARDINGADDRESS={{item.NSSASUPPRESSFORWARDINGADDRESS}},
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
        {#- --- 条件可选：AREATYPE=NSSA 时可选 --- -#}
        {%- if item.AREATYPE == 'NSSA' -%}
            {%- if item.NSSAZEROADDRESSFORWARDING is not none -%}
                NSSAZEROADDRESSFORWARDING={{item.NSSAZEROADDRESSFORWARDING}},
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
{%- endif -%}
```

```jinja2
{%- if is_scenario_ospf_dynamic_route -%}
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
        {#- --- 条件可选：PROTOCOL=BGP 时可选 --- -#}
        {%- if item.PROTOCOL == 'BGP' -%}
            {%- if item.PERMITIBGPCFG is not none -%}
                PERMITIBGPCFG={{item.PERMITIBGPCFG}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROTOCOL=OSPF 时可选 --- -#}
        {%- if item.PROTOCOL == 'OSPF' -%}
            {%- if item.PROTOCOLPROCID is not none -%}
                PROTOCOLPROCID={{item.PROTOCOLPROCID}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_ospf_dynamic_route -%}
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
{%- endif -%}
```

```jinja2
{%- if is_scenario_ospf_dynamic_route -%}
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
{%- endif -%}
```

```jinja2
{%- if is_scenario_ospf_dynamic_route -%}
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
{%- endif -%}
```

```jinja2
{%- if is_scenario_ospf_dynamic_route -%}
    {%- for item in add_routepolicy_list_1 -%}
        ADD ROUTEPOLICY:
        {#- --- 必选参数 --- -#}
        POLICYNAME="{{item.POLICYNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_ospf_dynamic_route -%}
    {%- for item in add_routepolicynode_list_1 -%}
        ADD ROUTEPOLICYNODE:
        {#- --- 必选参数 --- -#}
        POLICYNAME="{{item.POLICYNAME}}",
        NODESEQUENCE={{item.NODESEQUENCE}},
        MATCHMODE={{item.MATCHMODE}},
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_ospf_dynamic_route -%}
    {%- for item in add_prefixfilternode_list_1 -%}
        ADD PREFIXFILTERNODE:
        {#- --- 必选参数 --- -#}
        NAME="{{item.NAME}}",
        NODESEQUENCE={{item.NODESEQUENCE}},
        MATCHMODE={{item.MATCHMODE}},
        ADDRESS="{{item.ADDRESS}}",
        MASKLENGTH={{item.MASKLENGTH}},
        {#- --- 可选参数 --- -#}
        {%- if item.GREATEREQUAL is not none -%}
            GREATEREQUAL={{item.GREATEREQUAL}},
        {%- endif -%}
        {%- if item.LESSEQUAL is not none -%}
            LESSEQUAL={{item.LESSEQUAL}},
        {%- endif -%}
        {%- if item.MATCHNETWORK is not none -%}
            MATCHNETWORK={{item.MATCHNETWORK}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_ospf_dynamic_route -%}
    {%- for item in add_matchdestprefixfilter_list_1 -%}
        ADD MATCHDESTPREFIXFILTER:
        {#- --- 必选参数 --- -#}
        POLICYNAME="{{item.POLICYNAME}}",
        NODESEQUENCE={{item.NODESEQUENCE}},
        PREFIXNAME="{{item.PREFIXNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_ospf_dynamic_route -%}
    {%- for item in add_ospffilterpolicy_list -%}
        ADD OSPFFILTERPOLICY:
        {#- --- 必选参数 --- -#}
        PROCID={{item.PROCID}},
        FILTERTYPE={{item.FILTERTYPE}},
        TYPE={{item.TYPE}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：TYPE=ip_prefix 时必选 --- -#}
        {%- if item.TYPE == 'ip_prefix' -%}
            IPPREFIX="{{item.IPPREFIX}}",
        {%- endif -%}
        {#- --- 条件必选：TYPE=acl_name/acl_num 时必选 --- -#}
        {%- if item.TYPE in ['acl_name', 'acl_num'] -%}
            ACLNAMEORNUM="{{item.ACLNAMEORNUM}}",
        {%- endif -%}
        {#- --- 条件必选：TYPE=route_policy 时必选 --- -#}
        {%- if item.TYPE == 'route_policy' -%}
            ROUTEPLYNAME="{{item.ROUTEPLYNAME}}",
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：FILTERTYPE=export 时可选 --- -#}
        {%- if item.FILTERTYPE == 'export' -%}
            {%- if item.PROTOCOL is not none -%}
                PROTOCOL={{item.PROTOCOL}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：TYPE=route_policy 时可选 --- -#}
        {%- if item.TYPE == 'route_policy' -%}
            {%- if item.SECONDARYFLAG is not none -%}
                SECONDARYFLAG={{item.SECONDARYFLAG}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_ospf_dynamic_route -%}
    {%- for item in add_interface_list_1 -%}
        ADD INTERFACE:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_ospf_dynamic_route -%}
    {%- for item in add_ipbindvpn_list_1 -%}
        ADD IPBINDVPN:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        VRFNAME="{{item.VRFNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_ospf_dynamic_route -%}
    {%- for item in add_ifipv4address_list_1 -%}
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
{%- if is_scenario_ospf_dynamic_route -%}
    {%- for item in add_ospfinterface_list -%}
        ADD OSPFINTERFACE:
        {#- --- 必选参数 --- -#}
        PROCID={{item.PROCID}},
        AREAID="{{item.AREAID}}",
        IFNAME="{{item.IFNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_ospf_dynamic_route -%}
    {%- for item in add_ipv6prefixfilternode_list_1 -%}
        ADD IPV6PREFIXFILTERNODE:
        {#- --- 必选参数 --- -#}
        NAME="{{item.NAME}}",
        NODESEQUENCE={{item.NODESEQUENCE}},
        MATCHMODE={{item.MATCHMODE}},
        ADDRESS="{{item.ADDRESS}}",
        MASKLENGTH={{item.MASKLENGTH}},
        {#- --- 可选参数 --- -#}
        {%- if item.MATCHNETWORK is not none -%}
            MATCHNETWORK={{item.MATCHNETWORK}},
        {%- endif -%}
        {%- if item.GREATEREQUAL is not none -%}
            GREATEREQUAL={{item.GREATEREQUAL}},
        {%- endif -%}
        {%- if item.LESSEQUAL is not none -%}
            LESSEQUAL={{item.LESSEQUAL}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_ospf_dynamic_route -%}
    {%- for item in add_matchdestprefix6filter_list_1 -%}
        ADD MATCHDESTPREFIX6FILTER:
        {#- --- 必选参数 --- -#}
        POLICYNAME="{{item.POLICYNAME}}",
        NODESEQUENCE={{item.NODESEQUENCE}},
        IPV6PREFIXNAME="{{item.IPV6PREFIXNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_ospf_dynamic_route -%}
    {%- for item in add_ospfv3filterpolicy_list -%}
        ADD OSPFV3FILTERPOLICY:
        {#- --- 必选参数 --- -#}
        PROCID={{item.PROCID}},
        FILTERTYPE={{item.FILTERTYPE}},
        TYPE={{item.TYPE}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：TYPE=ip_prefix 时必选 --- -#}
        {%- if item.TYPE == 'ip_prefix' -%}
            IPPREFIX="{{item.IPPREFIX}}",
        {%- endif -%}
        {#- --- 条件必选：TYPE=acl_name/acl_num 时必选 --- -#}
        {%- if item.TYPE in ['acl_name', 'acl_num'] -%}
            ACLNAMEORNUM="{{item.ACLNAMEORNUM}}",
        {%- endif -%}
        {#- --- 条件必选：TYPE=route_policy 时必选 --- -#}
        {%- if item.TYPE == 'route_policy' -%}
            ROUTEPLYNAME="{{item.ROUTEPLYNAME}}",
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：FILTERTYPE=export 时可选 --- -#}
        {%- if item.FILTERTYPE == 'export' -%}
            {%- if item.PROTOCOL is not none -%}
                PROTOCOL={{item.PROTOCOL}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_ospf_dynamic_route -%}
    {%- for item in add_autoscalingethtrunk_list_1 -%}
        ADD AUTOSCALINGETHTRUNK:
        {#- --- 必选参数 --- -#}
        ETHTRUNKTMPID={{item.ETHTRUNKTMPID}},
        VNICLIST="{{item.VNICLIST}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_ospf_dynamic_route -%}
    {%- for item in add_autoscalingservice_list_4 -%}
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
        {#- --- 条件必选：OSPFENABLE=TRUE 时必选 --- -#}
        {%- if item.OSPFENABLE == 'TRUE' -%}
            OSPFPROCID={{item.OSPFPROCID}},
        {%- endif -%}
        {#- --- 条件必选：OSPFENABLE=TRUE 时必选 --- -#}
        {%- if item.OSPFENABLE == 'TRUE' -%}
            OSPFAREAID="{{item.OSPFAREAID}}",
        {%- endif -%}
        {#- --- 条件必选：IPALLOCTYPE6=USER_CONFIG 时必选 --- -#}
        {%- if item.IPALLOCTYPE6 == 'USER_CONFIG' -%}
            BEGINADDR6="{{item.BEGINADDR6}}",
        {%- endif -%}
        {#- --- 条件必选：IPALLOCTYPE6=USER_CONFIG 时必选 --- -#}
        {%- if item.IPALLOCTYPE6 == 'USER_CONFIG' -%}
            ENDADDR6="{{item.ENDADDR6}}",
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
        {#- --- 条件可选：IPALLOCTYPE6=DHCP 时可选 --- -#}
        {%- if item.IPALLOCTYPE6 == 'DHCP' -%}
            {%- if item.ADDRMODE is not none -%}
                ADDRMODE={{item.ADDRMODE}},
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

#### 7.2 配置上行报文使用的外联口IP及路由。UDG用于发送上行报文到重定向设备、PDN/DN Server。该OSPF进程不发布wlr路由。

```jinja2
{%- if is_scenario_ospf_dynamic_route -%}
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
        {%- if item.BFDRXCFGFLAG is not none -%}
            BFDRXCFGFLAG={{item.BFDRXCFGFLAG}},
        {%- endif -%}
        {%- if item.BFDTXCFGFLAG is not none -%}
            BFDTXCFGFLAG={{item.BFDTXCFGFLAG}},
        {%- endif -%}
        {%- if item.SCHEMABFDDETMUL is not none -%}
            SCHEMABFDDETMUL={{item.SCHEMABFDDETMUL}},
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
        {#- --- 条件必选：BFDRXCFGFLAG=TRUE 时必选 --- -#}
        {%- if item.BFDRXCFGFLAG == 'TRUE' -%}
            BFDMINRXINTV={{item.BFDMINRXINTV}},
        {%- endif -%}
        {#- --- 条件必选：BFDTXCFGFLAG=TRUE 时必选 --- -#}
        {%- if item.BFDTXCFGFLAG == 'TRUE' -%}
            BFDMINTXINTV={{item.BFDMINTXINTV}},
        {%- endif -%}
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
        {#- --- 条件必选：LSAARRINTVFLAG=TRUE 时必选 --- -#}
        {%- if item.LSAARRINTVFLAG == 'TRUE' -%}
            LSAARRINTV={{item.LSAARRINTV}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_ospf_dynamic_route -%}
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
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：MAXCOSTFLAG=TRUE 时必选 --- -#}
        {%- if item.MAXCOSTFLAG == 'TRUE' -%}
            MAXCOSTINTVL={{item.MAXCOSTINTVL}},
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
            {%- if item.NSSASUPPRESSFORWARDINGADDRESS is not none -%}
                NSSASUPPRESSFORWARDINGADDRESS={{item.NSSASUPPRESSFORWARDINGADDRESS}},
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
        {#- --- 条件可选：AREATYPE=NSSA 时可选 --- -#}
        {%- if item.AREATYPE == 'NSSA' -%}
            {%- if item.NSSAZEROADDRESSFORWARDING is not none -%}
                NSSAZEROADDRESSFORWARDING={{item.NSSAZEROADDRESSFORWARDING}},
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
{%- endif -%}
```

```jinja2
{%- if is_scenario_ospf_dynamic_route -%}
    {%- for item in add_ospffilterpolicy_list_1 -%}
        ADD OSPFFILTERPOLICY:
        {#- --- 必选参数 --- -#}
        PROCID={{item.PROCID}},
        FILTERTYPE={{item.FILTERTYPE}},
        TYPE={{item.TYPE}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：TYPE=ip_prefix 时必选 --- -#}
        {%- if item.TYPE == 'ip_prefix' -%}
            IPPREFIX="{{item.IPPREFIX}}",
        {%- endif -%}
        {#- --- 条件必选：TYPE=acl_name/acl_num 时必选 --- -#}
        {%- if item.TYPE in ['acl_name', 'acl_num'] -%}
            ACLNAMEORNUM="{{item.ACLNAMEORNUM}}",
        {%- endif -%}
        {#- --- 条件必选：TYPE=route_policy 时必选 --- -#}
        {%- if item.TYPE == 'route_policy' -%}
            ROUTEPLYNAME="{{item.ROUTEPLYNAME}}",
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：FILTERTYPE=export 时可选 --- -#}
        {%- if item.FILTERTYPE == 'export' -%}
            {%- if item.PROTOCOL is not none -%}
                PROTOCOL={{item.PROTOCOL}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROTOCOL=OSPF 时可选 --- -#}
        {%- if item.PROTOCOL == 'OSPF' -%}
            {%- if item.PROTOCOLPROCESSID is not none -%}
                PROTOCOLPROCESSID={{item.PROTOCOLPROCESSID}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：TYPE=route_policy 时可选 --- -#}
        {%- if item.TYPE == 'route_policy' -%}
            {%- if item.SECONDARYFLAG is not none -%}
                SECONDARYFLAG={{item.SECONDARYFLAG}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_ospf_dynamic_route -%}
    {%- for item in add_autoscalingservice_list_6 -%}
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

```jinja2
{%- if is_scenario_ospf_dynamic_route -%}
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
{%- endif -%}
```

```jinja2
{%- if is_scenario_ospf_dynamic_route -%}
    {%- for item in add_ospfv3area_list_1 -%}
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
{%- endif -%}
```

```jinja2
{%- if is_scenario_ospf_dynamic_route -%}
    {%- for item in add_ospfv3filterpolicy_list_1 -%}
        ADD OSPFV3FILTERPOLICY:
        {#- --- 必选参数 --- -#}
        PROCID={{item.PROCID}},
        FILTERTYPE={{item.FILTERTYPE}},
        TYPE={{item.TYPE}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：TYPE=ip_prefix 时必选 --- -#}
        {%- if item.TYPE == 'ip_prefix' -%}
            IPPREFIX="{{item.IPPREFIX}}",
        {%- endif -%}
        {#- --- 条件必选：TYPE=acl_name/acl_num 时必选 --- -#}
        {%- if item.TYPE in ['acl_name', 'acl_num'] -%}
            ACLNAMEORNUM="{{item.ACLNAMEORNUM}}",
        {%- endif -%}
        {#- --- 条件必选：PROTOCOL=ospfv3 时必选 --- -#}
        {%- if item.PROTOCOL == 'ospfv3' -%}
            PROTOCOLPROCESSID={{item.PROTOCOLPROCESSID}},
        {%- endif -%}
        {#- --- 条件必选：TYPE=route_policy 时必选 --- -#}
        {%- if item.TYPE == 'route_policy' -%}
            ROUTEPLYNAME="{{item.ROUTEPLYNAME}}",
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：FILTERTYPE=export 时可选 --- -#}
        {%- if item.FILTERTYPE == 'export' -%}
            {%- if item.PROTOCOL is not none -%}
                PROTOCOL={{item.PROTOCOL}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_ospf_dynamic_route -%}
    {%- for item in add_autoscalingservice_list_7 -%}
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

### 8 打开自动部署开关。

```jinja2
{%- for item in set_autoconfig_list_1 -%}
    SET AUTOCONFIG:
    {#- --- 必选参数 --- -#}
    SWITCHFLAG={{item.SWITCHFLAG}},
    ;
{%- endfor -%}
```

### 从自动部署开关打开到自动部署功能生效有时延，因此执行其他操作前（例如手动部署路由互通、关闭自动部署开关），务必先执行**DSP OPSASSISTSTATE**命令查询自动部署维护助手“autoscaling\_autoconfig.py”的状态为“准备好状态（Ready）”，否则结果不可预期。


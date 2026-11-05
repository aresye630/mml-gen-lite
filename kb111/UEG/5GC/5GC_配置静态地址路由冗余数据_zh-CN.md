---
id: ''
name: 配置静态地址路由冗余数据
ne_type: UEG
type: feature
description: 当终端地址采用静态签约方式时，网络中需部署冗余的主备两台UEG，并建立GRE Tunnel，确保网络正常运行，保证静态地址签约用户正常进行业务。配置举例如图1所示。  **图1** 静态地址路由冗余GRE数据规划图
tags: []
risk_level: ''
doc_source:
  - ["专线（仅连接，地市共享式）","业务发放","5GC toB DNN业务发放（专线，共享式）","通过OMC发放","DNN发放操作","发放共享式UPF+VPN专线","共享式UPF+VPN专线+主锚点UPF（同级）+主备+静态签约地址（GRE冗余备份）","配置数据","配置UPF数据","配置静态地址路由冗余数据"]
  - ["云网（连接+计算，入驻式或共享式）","业务发放","5GC toB DNN业务发放（云网，带计算）","通过OMC发放","DNN发放操作","发放共享式UPF+VPN专线","共享式UPF+VPN专线+主锚点UPF（同级）+主备+静态签约地址（GRE冗余备份）","配置数据","配置UPF数据","配置静态地址路由冗余数据"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
当终端地址采用静态签约方式时，网络中需部署冗余的主备两台UEG，并建立GRE Tunnel，确保网络正常运行，保证静态地址签约用户正常进行业务。配置举例如图1所示。**图1** 静态地址路由冗余GRE数据规划图

## 必备事项
前提条件

前提条件

主备UEG之间LoopBack接口的路由互通配置已完成。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    mod_pool_list:
      type: items
      properties:
        POOLNAME:
          name: '地址池名称'
          type: string
          minLength: 1
          maxLength: 79
          required: true
          description: '修改静态地址池，地址池的冗余备份开关打开。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        POOLTYPE:
          name: '地址池类型'
          type: string
          enum:
          - EXTERNAL
          - LOCAL
          - MULTICAST
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
        REDUNDFUNC:
          name: '冗余备份功能开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
    mod_uppool_list:
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
          default: ''
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
          default: ''
    add_redundrdtip_list:
      type: items
      properties:
        IPVERSION:
          name: 'IP版本'
          type: string
          enum:
          - IPv4
          - IPv6
          required: true
          description: '* 配置虚拟重定向IP，本端规划的虚拟IP，将业务流重定向到Gre Tunnel。 * 重定向IP是全局规划的，只在内部做重定向转发，不对外发布，只要保证和其他路由不冲突即可，所以主备UPF的重定向IP可以规划为相同IP，也可以规划为不同IP。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV4ADDRESS:
          name: 'IPV4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV6ADDRESS:
          name: 'IPV6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: '全网规划'
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
          description: 'LoopBack接口。'
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
          data_source: '固定取值'
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
          description: '与LoopBack接口关联的VPN实例。  LoopBack接口和Tunnel接口绑定的VPN实例不同，完成物理和业务上的划分。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: true
          description: ''
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
          description: '配置接口的IP地址。'
          data_source: '从已配置数据中获取'
          pattern: ''
          default: ''
        IFIPADDR:
          name: 'IPv4地址'
          type: string
          maxLength: 15
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        SUBNETMASK:
          name: 'IPv4地址掩码'
          type: string
          maxLength: 15
          required: true
          description: ''
          data_source: '全网规划'
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
          description: '针对IPv4生效，MTU配置原则：封装GRE隧道出外联口不会再次分片。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        IFMTU:
          name: '接口最大传输单元（byte）'
          type: integer
          minimum: 46
          maximum: 9600
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_gretunnel_list:
      type: items
      properties:
        TNLNAME:
          name: '隧道名称'
          type: string
          maxLength: 63
          required: true
          description: '配置备份GRE Tunnel。  Tunnel接口编号只具有本地意义，隧道两端可以使用不同的接口编号。'
          data_source: '从已配置数据中获取'
          pattern: ''
          default: ''
        SRCTYPE:
          name: 'IPv4源类型'
          type: string
          enum:
          - if_name
          - ip_address
          - no_type
          required: false
          description: '指定源类型为接口。'
          data_source: '本端规划'
          pattern: ''
          default: no_type
        DSTIPADDR:
          name: '目的IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: '对端设备Loopback接口的IP地址。'
          data_source: '从已配置数据中获取'
          pattern: ''
          default: ''
        TNLTYPE:
          name: '隧道类型'
          type: string
          enum:
          - gre
          - gre6
          required: true
          description: '配置隧道类型。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        SRCIFNAME:
          name: '源接口名称'
          type: string
          maxLength: 63
          required: false
          description: '本端设备的LoopBack接口名称，已通过**ADD INTERFACE**命令配置。'
          data_source: '从已配置数据中获取'
          pattern: ''
          default: ''
        DSTVPNNAME:
          name: '目的VPN名称'
          type: string
          maxLength: 31
          required: false
          description: '隧道的目的地址所属的VPN实例的名称。  已通过**ADD L3VPNINST**和**ADD VPNINSTAF**命令配置，可以使用**LST L3VPNINST**命令进行查询。'
          data_source: '从已配置数据中获取'
          pattern: ''
          default: ''
        GREKEYEN:
          name: '使能识别关键字功能'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: '* 两个UPF之间的GRE隧道需要复用外层LoopBack地址，必须配置GREKey以区分不同的Tunnel。 * 不同Tunnel要规划为不同的值。'
          data_source: '固定取值'
          pattern: ''
          default: FALSE
        GREKEY:
          name: '识别关键字'
          type: string
          maxLength: 268
          required: false
          description: ''
          data_source: '与对端保持一致'
          pattern: ''
          default: ''
        REDUNDANCYEN:
          name: '使能备份隧道功能'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: '使能GRE隧道备份静态地址用户的流量功能。'
          data_source: '固定取值'
          pattern: ''
          default: FALSE
        KEEPALVEN:
          name: '使能Keepalive功能'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: '使能Keepalive功能后，GRE隧道源端周期性的发送Keepalive报文，如果GRE隧道对端不可达，本端的Tunnel接口状态会被置为Down。'
          data_source: '固定取值'
          pattern: ''
          default: FALSE
        SRCTYPE6:
          name: 'IPv6源类型'
          type: string
          enum:
          - if_name
          - ip_address
          - no_type
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: no_type
    add_ipbindvpn_list_1:
      type: items
      properties:
        IFNAME:
          name: '接口名'
          type: string
          maxLength: 63
          required: true
          description: '与接口关联的VPN实例。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: true
          description: '* 已通过**ADD L3VPNINST**命令配置，可以使用**LST L3VPNINST**命令进行查询。 * 由于两个UPF之间的GRE冗余隧道中是N6口流量，所以此参数要与N6口专线的VPN实例相同。'
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
          description: '配置接口的IP地址。'
          data_source: '从已配置数据中获取'
          pattern: ''
          default: ''
        IFIPADDR:
          name: 'IPv4地址'
          type: string
          maxLength: 15
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        SUBNETMASK:
          name: 'IPv4地址掩码'
          type: string
          maxLength: 15
          required: true
          description: ''
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
          description: '修改接口的IPv6使能情况。'
          data_source: '从已配置数据中获取'
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
          data_source: '本端规划'
          pattern: ''
          default: ''
        MTU:
          name: 'IPv6接口最大传输单元（byte）'
          type: integer
          minimum: 1280
          maximum: 9600
          required: false
          description: '针对IPv6生效，MTU配置原则：封装GRE隧道出外联口不会再次分片。'
          data_source: '本端规划'
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
          description: '用于手工配置接口的IPv6地址。'
          data_source: '从已配置数据中获取'
          pattern: ''
          default: ''
        IPV6ADDRESS:
          name: 'IPv6地址'
          type: string
          maxLength: 39
          required: true
          description: ''
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
    add_srroute_list:
      type: items
      properties:
        AFTYPE:
          name: '地址族'
          type: string
          enum:
          - ipv4unicast
          required: true
          description: 'IPv4静态路由。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        PREFIX:
          name: '路由前缀'
          type: string
          maxLength: 15
          required: true
          description: '静态路由的目的地址需要与冗余备份隧道虚拟重定向IP保持一致。'
          data_source: '从已配置数据中获取'
          pattern: ''
          default: ''
        MASKLENGTH:
          name: '路由掩码长度'
          type: integer
          minimum: 0
          maximum: 32
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: false
          description: '-'
          data_source: '从已配置数据中获取'
          pattern: ''
          default: '_public_'
        IFNAME:
          name: '路由出接口名字'
          type: string
          maxLength: 63
          required: false
          description: '本端GRE Tunnel的逻辑接口，已通过**ADD INTERFACE**命令配置。'
          data_source: '从已配置数据中获取'
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
          description: 'IPv6静态路由。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        PREFIX:
          name: '路由前缀'
          type: string
          maxLength: 39
          required: true
          description: '静态路由的目的地址需要与冗余备份隧道虚拟重定向IP保持一致。'
          data_source: '从已配置数据中获取'
          pattern: ''
          default: ''
        MASKLENGTH:
          name: '路由掩码长度'
          type: integer
          minimum: 0
          maximum: 128
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: false
          description: '-'
          data_source: '从已配置数据中获取'
          pattern: ''
          default: '_public_'
        IFNAME:
          name: '路由出接口名字'
          type: string
          maxLength: 63
          required: false
          description: '本端GRE Tunnel的逻辑接口，已通过**ADD INTERFACE**命令配置。'
          data_source: '从已配置数据中获取'
          pattern: ''
          default: ''
    add_srroute_list_1:
      type: items
      properties:
        AFTYPE:
          name: '地址族'
          type: string
          enum:
          - ipv4unicast
          required: true
          description: '在主UEG配置下行缺省低优先级静态地址用户网段路由入冗余GRE隧道，该路由的目的地址网段应与用户地址池网段一致，优先级应低于业务侧下发的静态地址用户WLR路由优先级。路由优先级参数（PREFERENCE）不配置时默认为60，优先级值越大优先级越低。  说明：  PGW-U/UPF与PDN/DN之间配置GRE隧道，并且由PDN/DN侧服务器端配置高低优先级路由。此场景下需要在主UEG配置下行缺省低优先级静态地址用户网段路由入冗余GRE隧道。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        PREFIX:
          name: '路由前缀'
          type: string
          maxLength: 15
          required: true
          description: ''
          data_source: '从已配置数据中获取'
          pattern: ''
          default: ''
        MASKLENGTH:
          name: '路由掩码长度'
          type: integer
          minimum: 0
          maximum: 32
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: '从已配置数据中获取'
          pattern: ''
          default: '_public_'
        IFNAME:
          name: '路由出接口名字'
          type: string
          maxLength: 63
          required: false
          description: ''
          data_source: '从已配置数据中获取'
          pattern: ''
          default: ''
        BFDENABLE:
          name: '动态BFD使能标识'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: FALSE
        DHCPENABLE:
          name: 'DHCP使能标识'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: FALSE
        PREFERENCE:
          name: '路由优先级'
          type: integer
          minimum: 1
          maximum: 255
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: 60
    add_srroute6_list_1:
      type: items
      properties:
        AFTYPE:
          name: '地址族'
          type: string
          enum:
          - ipv6unicast
          required: true
          description: 'IPv6静态路由。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        PREFIX:
          name: '路由前缀'
          type: string
          maxLength: 39
          required: true
          description: '静态路由的目的地址需要与冗余备份隧道虚拟重定向IP保持一致。'
          data_source: '从已配置数据中获取'
          pattern: ''
          default: ''
        MASKLENGTH:
          name: '路由掩码长度'
          type: integer
          minimum: 0
          maximum: 128
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: false
          description: '-'
          data_source: '从已配置数据中获取'
          pattern: ''
          default: '_public_'
        IFNAME:
          name: '路由出接口名字'
          type: string
          maxLength: 63
          required: false
          description: '本端GRE Tunnel的逻辑接口，已通过**ADD INTERFACE**命令配置。'
          data_source: '从已配置数据中获取'
          pattern: ''
          default: ''
        BFDENABLE:
          name: '动态BFD使能标识'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        DHCPENABLE:
          name: 'DHCP使能标识'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
    set_redunduser_list:
      type: items
      properties:
        SWITCH:
          name: '开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: true
          description: '配置静态地址用户路由冗余功能全局开关。'
          data_source: '固定取值'
          pattern: ''
          default: ''
    mod_pool_list_2:
      type: items
      properties:
        POOLNAME:
          name: '地址池名称'
          type: string
          minLength: 1
          maxLength: 79
          required: true
          description: '修改静态地址池，地址池的冗余备份开关打开。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        POOLTYPE:
          name: '地址池类型'
          type: string
          enum:
          - EXTERNAL
          - LOCAL
          - MULTICAST
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
        REDUNDFUNC:
          name: '冗余备份功能开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
    mod_uppool_list_2:
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
          default: ''
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
          default: ''
    add_redundrdtip_list_2:
      type: items
      properties:
        IPVERSION:
          name: 'IP版本'
          type: string
          enum:
          - IPv4
          - IPv6
          required: true
          description: '* 配置虚拟重定向IP，本端规划的虚拟IP，将业务流重定向到Gre Tunnel。 * 重定向IP是全局规划的，只在内部做重定向转发，不对外发布，只要保证和其他路由不冲突即可，所以主备UPF的重定向IP可以规划为相同IP，也可以规划为不同IP。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV4ADDRESS:
          name: 'IPV4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV6ADDRESS:
          name: 'IPV6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: '全网规划'
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
          description: 'LoopBack接口。'
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
          data_source: '固定取值'
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
          description: '与LoopBack接口关联的VPN实例。  LoopBack接口和Tunnel接口绑定的VPN实例不同，完成物理和业务上的划分。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: true
          description: ''
          data_source: '已配置数据中获取'
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
          description: '配置接口的IP地址。'
          data_source: '从已配置数据中获取'
          pattern: ''
          default: ''
        IFIPADDR:
          name: 'IPv4地址'
          type: string
          maxLength: 15
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        SUBNETMASK:
          name: 'IPv4地址掩码'
          type: string
          maxLength: 15
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_interface_list_3:
      type: items
      properties:
        IFNAME:
          name: '接口名'
          type: string
          maxLength: 63
          required: true
          description: '针对IPv4生效，MTU配置原则：封装GRE隧道出外联口不会再次分片。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        IFMTU:
          name: '接口最大传输单元（byte）'
          type: integer
          minimum: 46
          maximum: 9600
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_gretunnel_list_1:
      type: items
      properties:
        TNLNAME:
          name: '隧道名称'
          type: string
          maxLength: 63
          required: true
          description: '配置备份GRE Tunnel。  Tunnel接口编号只具有本地意义，隧道两端可以使用不同的接口编号。'
          data_source: '从已配置数据中获取'
          pattern: ''
          default: ''
        SRCTYPE:
          name: 'IPv4源类型'
          type: string
          enum:
          - if_name
          - ip_address
          - no_type
          required: false
          description: '指定源类型为接口。'
          data_source: '本端规划'
          pattern: ''
          default: no_type
        DSTIPADDR:
          name: '目的IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: '对端设备Loopback接口的IP地址。'
          data_source: '从已配置数据中获取'
          pattern: ''
          default: ''
        TNLTYPE:
          name: '隧道类型'
          type: string
          enum:
          - gre
          - gre6
          required: true
          description: '配置隧道类型。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        SRCIFNAME:
          name: '源接口名称'
          type: string
          maxLength: 63
          required: false
          description: '本端设备的LoopBack接口名称，已通过**ADD INTERFACE**命令配置。'
          data_source: '从已配置数据中获取'
          pattern: ''
          default: ''
        DSTVPNNAME:
          name: '目的VPN名称'
          type: string
          maxLength: 31
          required: false
          description: '隧道的目的地址所属的VPN实例的名称。  已通过**ADD L3VPNINST**和**ADD VPNINSTAF**命令配置，可以使用**LST L3VPNINST**命令进行查询。'
          data_source: '从已配置数据中获取'
          pattern: ''
          default: ''
        GREKEYEN:
          name: '使能识别关键字功能'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: '* 两个UPF之间的GRE隧道需要复用外层LoopBack地址，必须配置GREKey以区分不同的Tunnel。 * 不同Tunnel要规划为不同的值。'
          data_source: '固定取值'
          pattern: ''
          default: FALSE
        GREKEY:
          name: '识别关键字'
          type: string
          maxLength: 268
          required: false
          description: ''
          data_source: '与对端保持一致'
          pattern: ''
          default: ''
        REDUNDANCYEN:
          name: '使能备份隧道功能'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: '使能GRE隧道备份静态地址用户的流量功能。'
          data_source: '固定取值'
          pattern: ''
          default: FALSE
        KEEPALVEN:
          name: '使能Keepalive功能'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: '使能Keepalive功能后，GRE隧道源端周期性的发送Keepalive报文，如果GRE隧道对端不可达，本端的Tunnel接口状态会被置为Down。'
          data_source: '固定取值'
          pattern: ''
          default: FALSE
        SRCTYPE6:
          name: 'IPv6源类型'
          type: string
          enum:
          - if_name
          - ip_address
          - no_type
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: no_type
    add_ipbindvpn_list_3:
      type: items
      properties:
        IFNAME:
          name: '接口名'
          type: string
          maxLength: 63
          required: true
          description: '与接口关联的VPN实例。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: true
          description: '* 已通过**ADD L3VPNINST**命令配置，可以使用**LST L3VPNINST**命令进行查询。 * 由于两个UPF之间的GRE冗余隧道中是N6口流量，所以此参数要与N6口专线的VPN实例相同。'
          data_source: '已配置数据中获取'
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
          description: '配置接口的IP地址。'
          data_source: '从已配置数据中获取'
          pattern: ''
          default: ''
        IFIPADDR:
          name: 'IPv4地址'
          type: string
          maxLength: 15
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        SUBNETMASK:
          name: 'IPv4地址掩码'
          type: string
          maxLength: 15
          required: true
          description: ''
          data_source: '全网规划'
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
          description: '修改接口的IPv6使能情况。'
          data_source: '从已配置数据中获取'
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
          data_source: '本端规划'
          pattern: ''
          default: ''
        MTU:
          name: 'IPv6接口最大传输单元（byte）'
          type: integer
          minimum: 1280
          maximum: 9600
          required: false
          description: '针对IPv6生效，MTU配置原则：封装GRE隧道出外联口不会再次分片。'
          data_source: '本端规划'
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
          description: '用于手工配置接口的IPv6地址。'
          data_source: '从已配置数据中获取'
          pattern: ''
          default: ''
        IPV6ADDRESS:
          name: 'IPv6地址'
          type: string
          maxLength: 39
          required: true
          description: ''
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
    add_srroute_list_2:
      type: items
      properties:
        AFTYPE:
          name: '地址族'
          type: string
          enum:
          - ipv4unicast
          required: true
          description: 'IPv4静态路由。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        PREFIX:
          name: '路由前缀'
          type: string
          maxLength: 15
          required: true
          description: '静态路由的目的地址需要与冗余备份隧道虚拟重定向IP保持一致。'
          data_source: '从已配置数据中获取'
          pattern: ''
          default: ''
        MASKLENGTH:
          name: '路由掩码长度'
          type: integer
          minimum: 0
          maximum: 32
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: false
          description: '-'
          data_source: '从已配置数据中获取'
          pattern: ''
          default: '_public_'
        IFNAME:
          name: '路由出接口名字'
          type: string
          maxLength: 63
          required: false
          description: '本端GRE Tunnel的逻辑接口，已通过**ADD INTERFACE**命令配置。'
          data_source: '从已配置数据中获取'
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
          description: 'IPv6静态路由。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        PREFIX:
          name: '路由前缀'
          type: string
          maxLength: 39
          required: true
          description: '静态路由的目的地址需要与冗余备份隧道虚拟重定向IP保持一致。'
          data_source: '从已配置数据中获取'
          pattern: ''
          default: ''
        MASKLENGTH:
          name: '路由掩码长度'
          type: integer
          minimum: 0
          maximum: 128
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: false
          description: '-'
          data_source: '从已配置数据中获取'
          pattern: ''
          default: '_public_'
        IFNAME:
          name: '路由出接口名字'
          type: string
          maxLength: 63
          required: false
          description: '本端GRE Tunnel的逻辑接口，已通过**ADD INTERFACE**命令配置。'
          data_source: '从已配置数据中获取'
          pattern: ''
          default: ''
    set_redunduser_list_1:
      type: items
      properties:
        SWITCH:
          name: '开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: true
          description: '配置静态地址用户路由冗余功能全局开关。'
          data_source: '固定取值'
          pattern: ''
          default: ''
    set_apnredundupsw_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '配置APN路由冗余上行报文隧道转发功能开关，该命令仅在备用UPF配置。'
          data_source: '从已配置数据中获取'
          pattern: ''
          default: ''
        IPV4SWITCH:
          name: 'APN支持IPV4上行转发功能'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV6SWITCH:
          name: 'APN支持IPV6上行转发功能'
          type: string
          enum:
          - DISABLE
          - ENABLE
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
        ROUTERID:
          name: '路由器标识'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
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
    add_ipbindvpn_list_4:
      type: items
      properties:
        IFNAME:
          name: '接口名'
          type: string
          maxLength: 63
          required: true
          description: '与LoopBack接口关联的VPN实例。  LoopBack接口和Tunnel接口绑定的VPN实例不同，完成物理和业务上的划分。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: true
          description: ''
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
          name: 'VLAN ID'
          type: integer
          minimum: 1
          maximum: 4094
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
    set_ifipv6enable_list_2:
      type: items
      properties:
        IFNAME:
          name: '接口名'
          type: string
          maxLength: 63
          required: true
          description: '修改接口的IPv6使能情况。'
          data_source: '从已配置数据中获取'
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
          data_source: '本端规划'
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
    add_srroute_list_3:
      type: items
      properties:
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: false
          description: '-'
          data_source: '从已配置数据中获取'
          pattern: ''
          default: '_public_'
        AFTYPE:
          name: '地址族'
          type: string
          enum:
          - ipv4unicast
          required: true
          description: 'IPv4静态路由。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        PREFIX:
          name: '路由前缀'
          type: string
          maxLength: 15
          required: true
          description: '静态路由的目的地址需要与冗余备份隧道虚拟重定向IP保持一致。'
          data_source: '从已配置数据中获取'
          pattern: ''
          default: ''
        MASKLENGTH:
          name: '路由掩码长度'
          type: integer
          minimum: 0
          maximum: 32
          required: true
          description: '-'
          data_source: '本端规划'
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
          maxLength: 15
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
          description: '本端GRE Tunnel的逻辑接口，已通过**ADD INTERFACE**命令配置。'
          data_source: '从已配置数据中获取'
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
    add_srroute6_list_3:
      type: items
      properties:
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: false
          description: '-'
          data_source: '从已配置数据中获取'
          pattern: ''
          default: '_public_'
        AFTYPE:
          name: '地址族'
          type: string
          enum:
          - ipv6unicast
          required: true
          description: 'IPv6静态路由。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        PREFIX:
          name: '路由前缀'
          type: string
          maxLength: 39
          required: true
          description: '静态路由的目的地址需要与冗余备份隧道虚拟重定向IP保持一致。'
          data_source: '从已配置数据中获取'
          pattern: ''
          default: ''
        MASKLENGTH:
          name: '路由掩码长度'
          type: integer
          minimum: 0
          maximum: 128
          required: true
          description: '-'
          data_source: '本端规划'
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
          data_source: ''
          pattern: ''
          default: ''
        IFNAME:
          name: '路由出接口名字'
          type: string
          maxLength: 63
          required: false
          description: '本端GRE Tunnel的逻辑接口，已通过**ADD INTERFACE**命令配置。'
          data_source: '从已配置数据中获取'
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
        ROUTERID:
          name: '路由器标识'
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
    add_bgppeeraf_list:
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
    add_ipbindvpn_list_5:
      type: items
      properties:
        IFNAME:
          name: '接口名'
          type: string
          maxLength: 63
          required: true
          description: '与LoopBack接口关联的VPN实例。  LoopBack接口和Tunnel接口绑定的VPN实例不同，完成物理和业务上的划分。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: true
          description: ''
          data_source: '已配置数据中获取'
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
    set_ifipv6enable_list_3:
      type: items
      properties:
        IFNAME:
          name: '接口名'
          type: string
          maxLength: 63
          required: true
          description: '修改接口的IPv6使能情况。'
          data_source: '从已配置数据中获取'
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
          data_source: '本端规划'
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
    add_bfdsession_list_2:
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
    add_srroute_list_5:
      type: items
      properties:
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: false
          description: '-'
          data_source: '从已配置数据中获取'
          pattern: ''
          default: '_public_'
        AFTYPE:
          name: '地址族'
          type: string
          enum:
          - ipv4unicast
          required: true
          description: 'IPv4静态路由。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        PREFIX:
          name: '路由前缀'
          type: string
          maxLength: 15
          required: true
          description: '静态路由的目的地址需要与冗余备份隧道虚拟重定向IP保持一致。'
          data_source: '从已配置数据中获取'
          pattern: ''
          default: ''
        MASKLENGTH:
          name: '路由掩码长度'
          type: integer
          minimum: 0
          maximum: 32
          required: true
          description: '-'
          data_source: '本端规划'
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
          maxLength: 15
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
          description: '本端GRE Tunnel的逻辑接口，已通过**ADD INTERFACE**命令配置。'
          data_source: '从已配置数据中获取'
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
    add_srroute6_list_5:
      type: items
      properties:
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: false
          description: '-'
          data_source: '从已配置数据中获取'
          pattern: ''
          default: '_public_'
        AFTYPE:
          name: '地址族'
          type: string
          enum:
          - ipv6unicast
          required: true
          description: 'IPv6静态路由。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        PREFIX:
          name: '路由前缀'
          type: string
          maxLength: 39
          required: true
          description: '静态路由的目的地址需要与冗余备份隧道虚拟重定向IP保持一致。'
          data_source: '从已配置数据中获取'
          pattern: ''
          default: ''
        MASKLENGTH:
          name: '路由掩码长度'
          type: integer
          minimum: 0
          maximum: 128
          required: true
          description: '-'
          data_source: '本端规划'
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
          data_source: ''
          pattern: ''
          default: ''
        IFNAME:
          name: '路由出接口名字'
          type: string
          maxLength: 63
          required: false
          description: '本端GRE Tunnel的逻辑接口，已通过**ADD INTERFACE**命令配置。'
          data_source: '从已配置数据中获取'
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
        IFDF:
          name: '接口不分片标记'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
    add_ipbindvpn_list_6:
      type: items
      properties:
        IFNAME:
          name: '接口名'
          type: string
          maxLength: 63
          required: true
          description: '与LoopBack接口关联的VPN实例。  LoopBack接口和Tunnel接口绑定的VPN实例不同，完成物理和业务上的划分。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: true
          description: ''
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
        SUBIFTYPE:
          name: '子接口流封装类型'
          type: string
          enum:
          - VlanType
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: VlanType
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
    add_ifipv4address_list_6:
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
          description: '修改接口的IPv6使能情况。'
          data_source: '从已配置数据中获取'
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
          data_source: '本端规划'
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
        ADDRTYPE:
          name: 'IPv6地址类型'
          type: string
          enum:
          - anycast
          - global
          - linkLocal
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: global
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
        NETWORKTYPE:
          name: '接口网络类型'
          type: string
          enum:
          - broadcast
          - nbma
          - p2mp
          - p2p
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        P2MPMASKIGN:
          name: '在P2MP网络上忽略网络掩码'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        SMARTDISCOVER:
          name: '使能Smart-Discover'
          type: string
          enum:
          - TRUE
          - FALSE
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
        FRRBINDINGFLAG:
          name: 'BFD会话与接口链路状态绑定标志'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        FRRBLOCKFLAG:
          name: '阻止指定OSPF接口的FRR能力'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        BFDBLOCK:
          name: '阻塞接口动态创建BFD特性'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        SUPPEREACH:
          name: '可达性抑制'
          type: string
          enum:
          - Disable
          - Enable
          - Not-Configured
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: Not-Configured
        MTUENABLE:
          name: '使能MTU'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        MPLSLDPAUTOCFG:
          name: '禁止自动使能MPLS LDP功能标志位'
          type: string
          enum:
          - Disable
          - None
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: None
        LDPSYNCENABLE:
          name: '使能LDP和OSPF同步功能'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        LDPSYNCBLOCK:
          name: '阻止接口上运行LDP和OSPF同步功能'
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
        MTUENABLE:
          name: '使能MTU'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: TRUE
        NETWORKTYPE:
          name: '接口网络类型'
          type: string
          enum:
          - BROADCAST
          - LOOPBACK
          - NBMA
          - P2MP-NONBROADCAST
          - POINT-TO-MULTIPOINT
          - POINT-TO-POINT
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
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
        FRRBINDINGFLAG:
          name: 'BFD会话与接口链路状态绑定标志'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        FRRBLOCKFLAG:
          name: '阻止指定OSPFv3接口的FRR能力'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        BFDBLOCK:
          name: '阻塞接口动态创建BFD特性'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
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
    add_ospfnetwork_list:
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
        IPADDRESS:
          name: 'IP地址'
          type: string
          maxLength: 15
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        WILDCARDMASK:
          name: '反掩码'
          type: string
          maxLength: 15
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
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
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VPNNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: ''
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
          data_source: ''
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
          data_source: ''
          pattern: ''
          default: ''
        VLANID:
          name: 'VLAN ID'
          type: integer
          minimum: 0
          maximum: 4094
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 0
        BEGINADDR4:
          name: '起始地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ENDADDR4:
          name: '结束地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MASKLEN:
          name: '地址池掩码长度'
          type: integer
          minimum: 1
          maximum: 128
          required: false
          description: ''
          data_source: ''
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
        BEGINADDR6:
          name: '起始地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ENDADDR6:
          name: '结束地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        OSPFENABLE:
          name: '使能OSPF'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        TPINENABLE:
          name: '使能入方向的流量策略'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: ''
          data_source: ''
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
          data_source: ''
          pattern: ''
          default: FALSE
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
    add_autoscalingbfd_list:
      type: items
      properties:
        TEMPLATENAME:
          name: '模板名称'
          type: string
          maxLength: 59
          required: true
          description: ''
          data_source: ''
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
          data_source: ''
          pattern: ''
          default: ''
        SERVICENAME:
          name: '服务名称'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: ''
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
          data_source: ''
          pattern: ''
          default: ''
        DESTADDR4:
          name: '目的地址'
          type: string
          maxLength: 15
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
        IPVERSION:
          name: '地址族'
          type: string
          enum:
          - IPv4
          - IPv6
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PREFIX4:
          name: '路由前缀IPv4'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MASKLENGTH:
          name: '路由掩码长度'
          type: integer
          minimum: 0
          maximum: 128
          required: true
          description: ''
          data_source: ''
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
        NEXTHOP4:
          name: '路由下一跳IPv4'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
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
          data_source: ''
          pattern: ''
          default: FALSE
        BFDTEMPLATENAME:
          name: 'BFD模板名称'
          type: string
          maxLength: 59
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PREFIX6:
          name: '路由前缀IPv6'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
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
        NEXTHOP6:
          name: '路由下一跳IPv6'
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
    add_interface_list_8:
      type: items
      properties:
        IFNAME:
          name: '接口名'
          type: string
          maxLength: 63
          required: true
          description: 'LoopBack接口。'
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
          data_source: '固定取值'
          pattern: ''
          default: ''
        IFMTU:
          name: '接口最大传输单元（byte）'
          type: integer
          minimum: 46
          maximum: 9600
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        IFDF:
          name: '接口不分片标记'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        IFSTATIENABLE:
          name: '接口统计使能标记'
          type: string
          enum:
          - FALSE
          - NONE
          - TRUE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IFTRAPENABLE:
          name: '接口Trap使能标记'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_ipbindvpn_list_8:
      type: items
      properties:
        IFNAME:
          name: '接口名'
          type: string
          maxLength: 63
          required: true
          description: '与LoopBack接口关联的VPN实例。  LoopBack接口和Tunnel接口绑定的VPN实例不同，完成物理和业务上的划分。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: true
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_ifipv4address_list_8:
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
    add_interface_list_9:
      type: items
      properties:
        IFNAME:
          name: '接口名'
          type: string
          maxLength: 63
          required: true
          description: 'LoopBack接口。'
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
          data_source: '固定取值'
          pattern: ''
          default: ''
        IFMTU:
          name: '接口最大传输单元（byte）'
          type: integer
          minimum: 46
          maximum: 9600
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        IFDF:
          name: '接口不分片标记'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        IFSTATIENABLE:
          name: '接口统计使能标记'
          type: string
          enum:
          - FALSE
          - NONE
          - TRUE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IFTRAPENABLE:
          name: '接口Trap使能标记'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_ipbindvpn_list_9:
      type: items
      properties:
        IFNAME:
          name: '接口名'
          type: string
          maxLength: 63
          required: true
          description: '与LoopBack接口关联的VPN实例。  LoopBack接口和Tunnel接口绑定的VPN实例不同，完成物理和业务上的划分。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: true
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    set_ifipv6enable_list_6:
      type: items
      properties:
        IFNAME:
          name: '接口名'
          type: string
          maxLength: 63
          required: true
          description: '修改接口的IPv6使能情况。'
          data_source: '从已配置数据中获取'
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
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_ifipv6address_list_6:
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
    add_bgpvrf_list_2:
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
    add_bgpvrfaf_list_4:
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
    add_bgppeer_list_8:
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
        PEERADDRV6:
          name: 'IPv6对等体地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
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
          description: ''
          data_source: ''
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
        REMOTEADDRESSV6:
          name: 'IPv6对等体地址'
          type: string
          maxLength: 39
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
        IFDF:
          name: '接口不分片标记'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
    add_ipbindvpn_list_10:
      type: items
      properties:
        IFNAME:
          name: '接口名'
          type: string
          maxLength: 63
          required: true
          description: '与LoopBack接口关联的VPN实例。  LoopBack接口和Tunnel接口绑定的VPN实例不同，完成物理和业务上的划分。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: true
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_ethsubif_list_4:
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
        SUBIFTYPE:
          name: '子接口流封装类型'
          type: string
          enum:
          - VlanType
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: VlanType
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
    add_ifipv4address_list_9:
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
    set_ifipv6enable_list_7:
      type: items
      properties:
        IFNAME:
          name: '接口名'
          type: string
          maxLength: 63
          required: true
          description: '修改接口的IPv6使能情况。'
          data_source: '从已配置数据中获取'
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
          data_source: '本端规划'
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
        ADDRTYPE:
          name: 'IPv6地址类型'
          type: string
          enum:
          - anycast
          - global
          - linkLocal
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: global
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
    add_srroute_list_7:
      type: items
      properties:
        AFTYPE:
          name: '地址族'
          type: string
          enum:
          - ipv4unicast
          required: true
          description: 'IPv4静态路由。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        PREFIX:
          name: '路由前缀'
          type: string
          maxLength: 15
          required: true
          description: '静态路由的目的地址需要与冗余备份隧道虚拟重定向IP保持一致。'
          data_source: '从已配置数据中获取'
          pattern: ''
          default: ''
        MASKLENGTH:
          name: '路由掩码长度'
          type: integer
          minimum: 0
          maximum: 32
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: false
          description: '-'
          data_source: '从已配置数据中获取'
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
          description: '本端GRE Tunnel的逻辑接口，已通过**ADD INTERFACE**命令配置。'
          data_source: '从已配置数据中获取'
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
          description: 'IPv6静态路由。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        PREFIX:
          name: '路由前缀'
          type: string
          maxLength: 39
          required: true
          description: '静态路由的目的地址需要与冗余备份隧道虚拟重定向IP保持一致。'
          data_source: '从已配置数据中获取'
          pattern: ''
          default: ''
        MASKLENGTH:
          name: '路由掩码长度'
          type: integer
          minimum: 0
          maximum: 128
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: false
          description: '-'
          data_source: '从已配置数据中获取'
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
          description: '本端GRE Tunnel的逻辑接口，已通过**ADD INTERFACE**命令配置。'
          data_source: '从已配置数据中获取'
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
  examples:
    mod_pool_list:
    - POOLNAME: 'pool_ipv4_APN1'
      POOLTYPE: EXTERNAL
      REDUNDFUNC: ENABLE
    mod_uppool_list:
    - POOLNAME: 'pool_ipv4_APN1'
      POOLTYPE: EXTERNAL
      REDUNDFUNC: ENABLE
    add_redundrdtip_list:
    - IPVERSION: IPv4
      IPV4ADDRESS: '192.168.0.1'
      IPV6ADDRESS: 'fc00:3::1'
    add_interface_list:
    - IFNAME: 'LoopBack1'
      IFADMINSTATUS: up
    add_ipbindvpn_list:
    - IFNAME: 'LoopBack1'
      VRFNAME: 'VRF_N6_Local_2B'
    add_ifipv4address_list:
    - IFNAME: 'LoopBack1'
      IFIPADDR: '10.11.1.1'
      SUBNETMASK: '255.255.255.255'
    add_interface_list_1:
    - IFNAME: 'Tunnel1'
      IFMTU: 1500
    add_gretunnel_list:
    - TNLNAME: 'Tunnel1'
      SRCTYPE: if_name
      DSTIPADDR: '10.10.0.1'
      TNLTYPE: gre
      SRCIFNAME: 'LoopBack1'
      DSTVPNNAME: 'VRF_N6_Local_2B'
      GREKEYEN: TRUE
      GREKEY: '200'
      REDUNDANCYEN: TRUE
      KEEPALVEN: TRUE
      SRCTYPE6: no_type
    add_ipbindvpn_list_1:
    - IFNAME: 'Tunnel1'
      VRFNAME: 'VRF_N6_Local_2B_001'
    add_ifipv4address_list_1:
    - IFNAME: 'Tunnel1'
      IFIPADDR: '10.11.1.3'
      SUBNETMASK: '255.255.255.0'
    set_ifipv6enable_list:
    - IFNAME: 'Tunnel1'
      ENABLEFLAG: TRUE
      MTU: 1500
    add_ifipv6address_list:
    - IFNAME: 'Tunnel1'
      IPV6ADDRESS: 'fc00:2::1'
      PREFIXLEN: 64
    add_srroute_list:
    - AFTYPE: ipv4unicast
      PREFIX: '192.168.0.1'
      MASKLENGTH: 32
      VRFNAME: 'VRF_N6_Local_2B_001'
      IFNAME: 'Tunnel1'
    add_srroute6_list:
    - AFTYPE: ipv6unicast
      PREFIX: 'fc00:3::1'
      MASKLENGTH: 64
      VRFNAME: 'VRF_N6_Local_2B_001'
      IFNAME: 'Tunnel1'
    add_srroute_list_1:
    - AFTYPE: ipv4unicast
      PREFIX: '10.1.1.0'
      MASKLENGTH: 24
      VRFNAME: 'vpn1'
      IFNAME: 'Tunnel1'
      BFDENABLE: FALSE
      DHCPENABLE: FALSE
      PREFERENCE: 60
    add_srroute6_list_1:
    - AFTYPE: ipv6unicast
      PREFIX: 'fc00:1::1'
      MASKLENGTH: 64
      VRFNAME: 'vpn1'
      IFNAME: 'Tunnel1'
      BFDENABLE: FALSE
      DHCPENABLE: FALSE
    set_redunduser_list:
    - SWITCH: ENABLE
    mod_pool_list_2:
    - POOLNAME: 'pool_ipv4_APN1'
      POOLTYPE: EXTERNAL
      REDUNDFUNC: ENABLE
    mod_uppool_list_2:
    - POOLNAME: 'pool_ipv4_APN1'
      POOLTYPE: EXTERNAL
      REDUNDFUNC: ENABLE
    add_redundrdtip_list_2:
    - IPVERSION: IPv4
      IPV4ADDRESS: '192.168.0.1'
      IPV6ADDRESS: 'fc00:3::1'
    add_interface_list_2:
    - IFNAME: 'LoopBack1'
      IFADMINSTATUS: up
    add_ipbindvpn_list_2:
    - IFNAME: 'LoopBack1'
      VRFNAME: 'VRF_N6_Local_2B'
    add_ifipv4address_list_2:
    - IFNAME: 'LoopBack1'
      IFIPADDR: '10.10.0.1'
      SUBNETMASK: '255.255.255.255'
    add_interface_list_3:
    - IFNAME: 'Tunnel1'
      IFMTU: 1500
    add_gretunnel_list_1:
    - TNLNAME: 'Tunnel1'
      SRCTYPE: if_name
      DSTIPADDR: '10.11.1.1'
      TNLTYPE: gre
      SRCIFNAME: 'LoopBack1'
      DSTVPNNAME: 'VRF_N6_Local_2B'
      GREKEYEN: TRUE
      GREKEY: '200'
      REDUNDANCYEN: TRUE
      KEEPALVEN: TRUE
      SRCTYPE6: no_type
    add_ipbindvpn_list_3:
    - IFNAME: 'Tunnel1'
      VRFNAME: 'VRF_N6_Local_2B_001'
    add_ifipv4address_list_3:
    - IFNAME: 'Tunnel1'
      IFIPADDR: '10.11.1.4'
      SUBNETMASK: '255.255.255.0'
    set_ifipv6enable_list_1:
    - IFNAME: 'Tunnel1'
      ENABLEFLAG: TRUE
      MTU: 1500
    add_ifipv6address_list_1:
    - IFNAME: 'Tunnel1'
      IPV6ADDRESS: 'fc00:2::2'
      PREFIXLEN: 64
    add_srroute_list_2:
    - AFTYPE: ipv4unicast
      PREFIX: '192.168.0.1'
      MASKLENGTH: 32
      VRFNAME: 'VRF_N6_Local_2B_001'
      IFNAME: 'Tunnel1'
    add_srroute6_list_2:
    - AFTYPE: ipv6unicast
      PREFIX: 'fc00:3::1'
      MASKLENGTH: 128
      VRFNAME: 'VRF_N6_Local_2B_001'
      IFNAME: 'Tunnel1'
    set_redunduser_list_1:
    - SWITCH: ENABLE
    set_apnredundupsw_list:
    - APN: 'APN1'
      IPV4SWITCH: ENABLE
      IPV6SWITCH: ENABLE
    add_bgpvrf_list:
    - VRFNAME: 'VRF_N6_Local_2B'
      DEFAULTAFTYPE: noaf
    add_bgpvrfaf_list:
    - VRFNAME: 'VRF_N6_Local_2B'
      AFTYPE: ipv4uni
      MAXIMUMLOADBALANCE: 2
      ROUTERID: '192.168.225.138'
    add_bgppeer_list:
    - VRFNAME: 'VRF_N6_Local_2B'
      ADDRESSTYPE: ipv4
      PEERADDR: '192.168.79.8'
      REMOTEAS: '60002'
      LOCALIFADDR: '192.168.225.138'
      LOCALIFNAME: 'Loopback8'
      EBGPMAXHOP: 10
      PEERADDRV6: 'FC00::79:8'
    add_interface_list_4:
    - IFNAME: 'Eth-trunk2.3'
    add_ipbindvpn_list_4:
    - IFNAME: 'Eth-trunk2.3'
      VRFNAME: 'VRF_N6_Local_2B'
    add_ethsubif_list:
    - IFNAME: 'Eth-trunk2.3'
      VLANTYPEVID: 105
    add_ifipv4address_list_4:
    - IFNAME: 'Eth-trunk2.3'
      IFIPADDR: '192.168.85.10'
      SUBNETMASK: '255.255.255.248'
      ADDRTYPE: main
    set_ifipv6enable_list_2:
    - IFNAME: 'Eth-trunk2.3'
      ENABLEFLAG: TRUE
    add_ifipv6address_list_2:
    - IFNAME: 'Eth-trunk2.3'
      IPV6ADDRESS: 'FC00::40CA'
      PREFIXLEN: 123
    add_bfdsession_list:
    - SESSNAME: 'N6if_2_3'
      ADDRTYPE: IPv4
      CREATETYPE4: SESS_STATIC
      ONEARMECHO: TRUE
      DESTADDR4: '192.168.85.1'
      LINKTYPE: IP
      DETECTMULTI: 4
      MINECHORXINT: 500
      VRFNAME: 'VRF_N6_Local_2B'
      LOCALDISCR: 137
      IFNAME: 'Eth-trunk2.3'
      CREATETYPE6: SESS_STATIC
      ONEARMECHO6: TRUE
      DESTADDR6: 'FC00::40C1'
    add_srroute_list_3:
    - VRFNAME: 'VRF_N6_Local_2B'
      AFTYPE: ipv4unicast
      PREFIX: '192.168.79.8'
      MASKLENGTH: 32
      DESTVRFNAME: 'VRF_N6_Local_2B'
      NEXTHOP: '192.168.85.1'
      IFNAME: 'Eth-trunk2.3'
      SESSIONNAME: 'N6if_2_3'
    add_srroute6_list_3:
    - VRFNAME: 'VRF_N6_Local_2B'
      AFTYPE: ipv6unicast
      PREFIX: 'FC00::79:8'
      MASKLENGTH: 128
      DESTVRFNAME: 'VRF_N6_Local_2B'
      NEXTHOP: 'FC00::40C1'
      IFNAME: 'Eth-trunk2.3'
      SESSIONNAME: 'N6if_IPv6_2'
    add_bgpvrf_list_1:
    - VRFNAME: 'VRF_N6_Local_2B'
      DEFAULTAFTYPE: noaf
    add_bgpvrfaf_list_2:
    - VRFNAME: 'VRF_N6_Local_2B'
      AFTYPE: ipv4uni
      MAXIMUMLOADBALANCE: 2
      ROUTERID: '192.168.225.138'
    add_bgppeer_list_4:
    - VRFNAME: 'VRF_N6_Local_2B'
      ADDRESSTYPE: ipv4
      PEERADDR: '192.168.79.8'
      REMOTEAS: '60002'
      LOCALIFADDR: '192.168.225.138'
      LOCALIFNAME: 'Loopback8'
      EBGPMAXHOP: 10
      PEERADDRV6: 'FC00::79:8'
    add_bgppeeraf_list:
    - VRFNAME: 'VRF_N6_Local_2B'
      AFTYPE: ipv4uni
      REMOTEADDRESS: '192.168.79.8'
      ALLOWASLOOPENABLE: TRUE
      ALLOWASLOOPLIMIT: 1
      ADDRESSTYPE: ipv4
    add_interface_list_5:
    - IFNAME: 'Eth-trunk2.3'
    add_ipbindvpn_list_5:
    - IFNAME: 'Eth-trunk2.3'
      VRFNAME: 'VRF_N6_Local_2B'
    add_ethsubif_list_1:
    - IFNAME: 'Eth-trunk2.3'
      VLANTYPEVID: 105
    add_ifipv4address_list_5:
    - IFNAME: 'Eth-trunk2.3'
      IFIPADDR: '192.168.85.10'
      SUBNETMASK: '255.255.255.248'
      ADDRTYPE: main
    set_ifipv6enable_list_3:
    - IFNAME: 'Eth-trunk2.3'
      ENABLEFLAG: TRUE
    add_ifipv6address_list_3:
    - IFNAME: 'Eth-trunk2.3'
      IPV6ADDRESS: 'FC00::40CA'
      PREFIXLEN: 123
    add_bfdsession_list_2:
    - SESSNAME: 'N6if_2_3'
      ADDRTYPE: IPv4
      CREATETYPE4: SESS_STATIC
      ONEARMECHO: TRUE
      DESTADDR4: '192.168.85.1'
      LINKTYPE: IP
      DETECTMULTI: 4
      MINECHORXINT: 500
      VRFNAME: 'VRF_N6_Local_2B'
      LOCALDISCR: 137
      IFNAME: 'Eth-trunk2.3'
      CREATETYPE6: SESS_STATIC
      ONEARMECHO6: TRUE
      DESTADDR6: 'FC00::40C1'
    add_srroute_list_5:
    - VRFNAME: 'VRF_N6_Local_2B'
      AFTYPE: ipv4unicast
      PREFIX: '192.168.79.8'
      MASKLENGTH: 32
      DESTVRFNAME: 'VRF_N6_Local_2B'
      NEXTHOP: '192.168.85.1'
      IFNAME: 'Eth-trunk2.3'
      SESSIONNAME: 'N6if_2_3'
    add_srroute6_list_5:
    - VRFNAME: 'VRF_N6_Local_2B'
      AFTYPE: ipv6unicast
      PREFIX: 'FC00::79:8'
      MASKLENGTH: 128
      DESTVRFNAME: 'VRF_N6_Local_2B'
      NEXTHOP: 'FC00::40C1'
      IFNAME: 'Eth-trunk2.3'
      SESSIONNAME: 'N6if_IPv6_2'
    add_interface_list_6:
    - IFNAME: '100GE65/0/9.2005'
      IFDF: FALSE
    add_ipbindvpn_list_6:
    - IFNAME: '100GE65/0/9.2005'
      VRFNAME: 'VRF_N6_Local_2B'
    add_ethsubif_list_2:
    - IFNAME: '100GE65/0/9.2005'
      SUBIFTYPE: VlanType
      VLANTYPEVID: 2005
    add_ifipv4address_list_6:
    - IFNAME: '100GE65/0/9.2005'
      IFIPADDR: '192.168.246.130'
      SUBNETMASK: '255.255.255.224'
      ADDRTYPE: main
    set_ifipv6enable_list_4:
    - IFNAME: '100GE65/0/9.2005'
      ENABLEFLAG: TRUE
    add_ifipv6address_list_4:
    - IFNAME: '100GE65/0/9.2005'
      IPV6ADDRESS: 'fc00:8028:5000:43::9542'
      PREFIXLEN: 123
      ADDRTYPE: global
    add_ospf_list:
    - PROCID: 4
      VRFNAME: 'VRF_N6_Local_2B'
      SCHEMAROUID: '172.20.7.2'
      BFDALLINTFFLG: TRUE
      LSAARRINTVFLAG: FALSE
      LSAARRMAXINTV: 1000
      LSAARRSTARINTV: 500
      LSAARRHLDINTV: 500
      VPNINSCAPSIMFLG: TRUE
      VIRTUALSYSFLAG: TRUE
    add_ospfv3_list:
    - PROCID: 4
      VRFNAME: 'VRF_N6_Local_2B'
      ROUTERID: '172.20.7.2'
      BFDALLINTFFLG: TRUE
      VPNINSCAPSIMFLG: TRUE
      VIRTUALSYSFLAG: TRUE
    add_ospfarea_list:
    - PROCID: 4
      AREAID: '0.0.0.5'
      AREATYPE: Normal
      MAXCOSTFLAG: FALSE
    add_ospfv3area_list:
    - PROCID: 4
      AREAID: '0.0.0.5'
      AREATYPE: Normal
    add_ospfinterface_list:
    - PROCID: 4
      AREAID: '0.0.0.5'
      IFNAME: '100GE65/0/9.2005'
      DRPRI: 0
      NETWORKTYPE: p2p
      P2MPMASKIGN: FALSE
      SMARTDISCOVER: FALSE
      BFDENABLE: FALSE
      FRRBINDINGFLAG: FALSE
      FRRBLOCKFLAG: FALSE
      BFDBLOCK: FALSE
      SUPPEREACH: Not-Configured
      MTUENABLE: FALSE
      MPLSLDPAUTOCFG: None
      LDPSYNCENABLE: FALSE
      LDPSYNCBLOCK: FALSE
      VIRTUALSYSFLAG: FALSE
      MAXCOSTFLAG: FALSE
    add_ospfv3interface_list:
    - PROCID: 4
      AREAID: '0.0.0.5'
      IFNAME: '100GE65/0/9.2005'
      MTUENABLE: TRUE
      NETWORKTYPE: POINT-TO-POINT
      BFDENABLE: FALSE
      FRRBINDINGFLAG: FALSE
      FRRBLOCKFLAG: FALSE
      BFDBLOCK: FALSE
      DRPRI: 0
      VIRTUALSYSFLAG: FALSE
    add_ospfnetwork_list:
    - PROCID: 4
      AREAID: '0.0.0.5'
      IPADDRESS: '192.168.246.128'
      WILDCARDMASK: '0.0.0.31'
    add_ospfimportroute_list:
    - PROCID: 4
      TOPOID: 0
      PROTOCOL: wlr
      IMPTCOSTCFG: FALSE
      IMPTTAGCFG: FALSE
      IMPTTYPECFG: FALSE
    add_ospfv3importroute_list:
    - PROCID: 4
      TOPOID: 0
      PROTOCOL: wlr
      IMPTCOSTCFG: FALSE
      IMPTTAGCFG: FALSE
      IMPTTYPECFG: FALSE
    set_autoconfig_list:
    - SWITCHFLAG: FALSE
    add_autoscalingservice_list:
    - SERVICENAME: 'VRF_N6_Local_2B_915'
      VPNNAME: 'VRF_N6_Local_2B'
      AFTYPE: IPv4
      IPALLOCTYPE4: USER_CONFIG
      AUTOCFGIFTYPE: ETHTRUNK
      ETHTRUNKTMPID: 6
      VLANID: 915
      BEGINADDR4: '192.168.246.130'
      ENDADDR4: '192.168.246.158'
      MASKLEN: 27
      IPALLOCTYPE6: USER_CONFIG
      BEGINADDR6: 'fc00:8028:5000:43:0:0:0:9542'
      ENDADDR6: 'fc00:8028:5000:43:0:0:0:955E'
      OSPFENABLE: FALSE
      TPINENABLE: FALSE
      TPOUTENABLE: FALSE
      OSPFGRPENABLE: FALSE
    add_autoscalingbfd_list:
    - TEMPLATENAME: 'N6_BFD_3'
      BFDTYPE: Static
      SERVICENAME: 'VRF_N6_Local_2B_915'
      IPVERSION: IPv4
      DESTADDR4: '192.168.11.11'
      MINECHORXINT: 500
      DETECTMULTI: 4
      DESTADDR6: 'fc00:187:C28C:0:0:0:0:1'
    add_autoscalingsrroute_list:
    - SERVICENAME: 'VRF_N6_Local_2B_915'
      VRFNAME: 'VRF_N6_Local_2B'
      IPVERSION: IPv4
      PREFIX4: '192.168.11.1'
      MASKLENGTH: 32
      NEXTHOPALLOCTYPE4: CONFIG
      NEXTHOP4: '192.168.11.11'
      BFDENABLE: TRUE
      BFDTEMPLATENAME: 'N6_BFD_3'
      PREFIX6: 'fc00:187:C289::1'
      NEXTHOPALLOCTYPE6: CONFIG
      NEXTHOP6: 'fc00:187:C28C::1'
    set_autoconfig_list_1:
    - SWITCHFLAG: TRUE
    add_interface_list_8:
    - IFNAME: 'LoopBack16'
      IFADMINSTATUS: up
      IFMTU: 1500
      IFDF: FALSE
      IFSTATIENABLE: TRUE
      IFTRAPENABLE: TRUE
    add_ipbindvpn_list_8:
    - IFNAME: 'LoopBack16'
      VRFNAME: 'VRF_N6_Local_2B'
    add_ifipv4address_list_8:
    - IFNAME: 'LoopBack16'
      IFIPADDR: '172.20.9.7'
      SUBNETMASK: '255.255.255.255'
      ADDRTYPE: main
    add_interface_list_9:
    - IFNAME: 'LoopBack15'
      IFADMINSTATUS: up
      IFMTU: 1500
      IFDF: FALSE
      IFSTATIENABLE: TRUE
      IFTRAPENABLE: TRUE
    add_ipbindvpn_list_9:
    - IFNAME: 'LoopBack15'
      VRFNAME: 'VRF_N6_Local_2B'
    set_ifipv6enable_list_6:
    - IFNAME: 'Loopback15'
      ENABLEFLAG: TRUE
    add_ifipv6address_list_6:
    - IFNAME: 'Loopback15'
      IPV6ADDRESS: 'fc00:187:C281::1'
      PREFIXLEN: 128
    set_bgp_list:
    - BGPENABLE: TRUE
      ASNUM: '64986'
    add_bgpvrf_list_2:
    - VRFNAME: 'VRF_N6_Local_2B'
      DEFAULTAFTYPE: noaf
      ROUTERID: '172.20.7.2'
    add_bgpvrfaf_list_4:
    - VRFNAME: 'VRF_N6_Local_2B'
      AFTYPE: ipv4uni
      MAXLOADEBGPNUM: 2
    add_importroute_list:
    - VRFNAME: 'VRF_N6_Local_2B'
      AFTYPE: ipv4uni
      IMPORTPROTOCOL: wlr
    add_bgppeer_list_8:
    - VRFNAME: 'VRF_N6_Local_2B'
      ADDRESSTYPE: ipv4
      PEERADDR: '192.168.11.1'
      REMOTEAS: '64813'
      LOCALIFADDR: '172.20.9.7'
      LOCALIFNAME: 'LoopBack16'
      EBGPMAXHOP: 2
      CONNECTMODE: 'null'
      PSWDTYPE: 'null'
      PEERADDRV6: 'fc00:187:C289::1'
    mod_bgppeeraf_list:
    - VRFNAME: 'VRF_N6_Local_2B'
      AFTYPE: ipv4uni
      REMOTEADDRESS: '192.168.11.1'
      ADDRESSTYPE: ipv6
      REMOTEADDRESSV6: 'fc00:187:C289:0:0:0:0:1'
    add_interface_list_10:
    - IFNAME: 'Ethernet64/0/6.3'
      IFDF: FALSE
    add_ipbindvpn_list_10:
    - IFNAME: 'Ethernet64/0/6.3'
      VRFNAME: 'VRF_N6_Local_2B'
    add_ethsubif_list_4:
    - IFNAME: 'Ethernet64/0/6.3'
      SUBIFTYPE: VlanType
      VLANTYPEVID: 104
    add_ifipv4address_list_9:
    - IFNAME: 'Ethernet64/0/6.3'
      IFIPADDR: '192.168.85.2'
      SUBNETMASK: '255.255.255.248'
      ADDRTYPE: main
    set_ifipv6enable_list_7:
    - IFNAME: 'Ethernet64/0/6.3'
      ENABLEFLAG: TRUE
    add_ifipv6address_list_7:
    - IFNAME: 'Ethernet64/0/6.3'
      IPV6ADDRESS: 'FC00::40C2'
      PREFIXLEN: 123
      ADDRTYPE: global
    add_bfdsession_list_4:
    - SESSNAME: 'N6if_2_3'
      ADDRTYPE: IPv4
      CREATETYPE4: SESS_STATIC
      ONEARMECHO: FALSE
      DESTADDR4: '192.168.85.1'
      LINKTYPE: IP
      DETECTMULTI: 4
      VRFNAME: 'VRF_N6_Local_2B'
      MINECHORXINT: 500
      LOCALDISCR: 322
      IFNAME: 'Ethernet64/0/6.3'
      CREATETYPE6: SESS_STATIC
      ONEARMECHO6: FALSE
      DESTADDR6: 'FC00::40C1'
    add_srroute_list_7:
    - AFTYPE: ipv4unicast
      PREFIX: '0.0.0.0'
      MASKLENGTH: 0
      VRFNAME: 'VRF_N6_Local_2B'
      DESTVRFNAME: 'VRF_N6_Local_2B'
      IFNAME: 'Ethernet64/0/6.3'
      NEXTHOP: '192.168.85.1'
      SESSIONNAME: 'N6if_2_3'
    add_srroute6_list_7:
    - AFTYPE: ipv6unicast
      PREFIX: '0:0:0:0:0:0:0:0'
      MASKLENGTH: 0
      VRFNAME: 'VRF_N6_Local_2B'
      DESTVRFNAME: 'VRF_N6_Local_2B'
      IFNAME: 'Ethernet64/0/6.3'
      NEXTHOP: 'FC00::40C1'
      SESSIONNAME: 'N6if_IPv6_3'
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 配置主用UPF的静态地址用户路由冗余功能，静态地址段分为IPv4和IPv6两类。

#### 1.1 修改静态地址池，打开地址池的冗余备份开关。

##### 1.1.1 //风筝S

```jinja2
{%- if is_scenario_kite_s -%}
    {%- for item in mod_pool_list -%}
        MOD POOL:
        {#- --- 必选参数 --- -#}
        POOLNAME="{{item.POOLNAME}}",
        {#- --- 可选参数 --- -#}
        {%- if item.POOLTYPE is not none -%}
            POOLTYPE={{item.POOLTYPE}},
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
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

##### 1.1.2 //风筝M或风筝L

```jinja2
{%- if is_scenario_kite_m_or_l -%}
    {%- for item in mod_uppool_list -%}
        MOD UPPOOL:
        {#- --- 必选参数 --- -#}
        POOLNAME="{{item.POOLNAME}}",
        {#- --- 可选参数 --- -#}
        {%- if item.POOLTYPE is not none -%}
            POOLTYPE={{item.POOLTYPE}},
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
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

#### 1.2 配置冗余备份重定向IP。

```jinja2
{%- for item in add_redundrdtip_list -%}
    ADD REDUNDRDTIP:
    {#- --- 必选参数 --- -#}
    IPVERSION={{item.IPVERSION}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPVERSION=IPv4 时必选 --- -#}
    {%- if item.IPVERSION == 'IPv4' -%}
        IPV4ADDRESS="{{item.IPV4ADDRESS}}",
    {%- endif -%}
    {#- --- 条件必选：IPVERSION=IPv6 时必选 --- -#}
    {%- if item.IPVERSION == 'IPv6' -%}
        IPV6ADDRESS="{{item.IPV6ADDRESS}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 1.3 配置LoopBack接口。

```jinja2
{%- for item in add_interface_list -%}
    ADD INTERFACE:
    {#- --- 必选参数 --- -#}
    IFNAME="{{item.IFNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.IFADMINSTATUS is not none -%}
        IFADMINSTATUS={{item.IFADMINSTATUS}},
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_ipbindvpn_list -%}
    ADD IPBINDVPN:
    {#- --- 必选参数 --- -#}
    IFNAME="{{item.IFNAME}}",
    VRFNAME="{{item.VRFNAME}}",
    ;
{%- endfor -%}
```

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

#### 1.4 配置GRE Tunnel。

```jinja2
{%- for item in add_interface_list_1 -%}
    ADD INTERFACE:
    {#- --- 必选参数 --- -#}
    IFNAME="{{item.IFNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.IFMTU is not none -%}
        IFMTU={{item.IFMTU}},
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_gretunnel_list -%}
    ADD GRETUNNEL:
    {#- --- 必选参数 --- -#}
    TNLNAME="{{item.TNLNAME}}",
    TNLTYPE={{item.TNLTYPE}},
    {#- --- 可选参数 --- -#}
    {%- if item.DSTVPNNAME is not none -%}
        DSTVPNNAME="{{item.DSTVPNNAME}}",
    {%- endif -%}
    {%- if item.GREKEYEN is not none -%}
        GREKEYEN={{item.GREKEYEN}},
    {%- endif -%}
    {%- if item.KEEPALVEN is not none -%}
        KEEPALVEN={{item.KEEPALVEN}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：TNLTYPE=gre 时必选 --- -#}
    {%- if item.TNLTYPE == 'gre' -%}
        SRCTYPE={{item.SRCTYPE}},
    {%- endif -%}
    {#- --- 条件必选：SRCTYPE=if_name 时必选 --- -#}
    {%- if item.SRCTYPE == 'if_name' -%}
        SRCIFNAME="{{item.SRCIFNAME}}",
    {#- --- 条件必选：SRCTYPE6=if_name 时必选 --- -#}
    {%- elif item.SRCTYPE6 == 'if_name' -%}
        SRCIFNAME="{{item.SRCIFNAME}}",
    {%- endif -%}
    {#- --- 条件必选：GREKEYEN=TRUE 时必选 --- -#}
    {%- if item.GREKEYEN == 'TRUE' -%}
        GREKEY="{{item.GREKEY}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：TNLTYPE=gre 时可选 --- -#}
    {%- if item.TNLTYPE == 'gre' -%}
        {%- if item.DSTIPADDR is not none -%}
            DSTIPADDR="{{item.DSTIPADDR}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：TNLTYPE=gre/gre6 时可选 --- -#}
    {%- if item.TNLTYPE in ['gre', 'gre6'] -%}
        {%- if item.REDUNDANCYEN is not none -%}
            REDUNDANCYEN={{item.REDUNDANCYEN}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_ipbindvpn_list_1 -%}
    ADD IPBINDVPN:
    {#- --- 必选参数 --- -#}
    IFNAME="{{item.IFNAME}}",
    VRFNAME="{{item.VRFNAME}}",
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_ifipv4address_list_1 -%}
    ADD IFIPV4ADDRESS:
    {#- --- 必选参数 --- -#}
    IFNAME="{{item.IFNAME}}",
    IFIPADDR="{{item.IFIPADDR}}",
    SUBNETMASK="{{item.SUBNETMASK}}",
    ;
{%- endfor -%}
```

```jinja2
{%- for item in set_ifipv6enable_list -%}
    SET IFIPV6ENABLE:
    {#- --- 必选参数 --- -#}
    IFNAME="{{item.IFNAME}}",
    ENABLEFLAG={{item.ENABLEFLAG}},
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：ENABLEFLAG=TRUE 时可选 --- -#}
    {%- if item.ENABLEFLAG == 'TRUE' -%}
        {%- if item.MTU is not none -%}
            MTU={{item.MTU}},
        {%- endif -%}
    {%- endif -%}
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

#### 1.5 配置IPv4静态路由。

```jinja2
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
    {%- if item.IFNAME is not none -%}
        IFNAME="{{item.IFNAME}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 1.6 配置IPv6静态路由。

```jinja2
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
    {%- if item.IFNAME is not none -%}
        IFNAME="{{item.IFNAME}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 1.7 （可选）PGW-U/UPF与PDN/DN之间配置GRE隧道，并且由PDN/DN侧服务器端配置高低优先级路由。此场景下应在主UEG配置下行缺省低优先级静态地址用户网段路由入冗余GRE隧道。

```jinja2
{%- if is_optional_user_downlink_route -%}
    {%- for item in add_srroute_list_1 -%}
        ADD SRROUTE:
        {#- --- 必选参数 --- -#}
        AFTYPE={{item.AFTYPE}},
        PREFIX="{{item.PREFIX}}",
        MASKLENGTH={{item.MASKLENGTH}},
        {#- --- 可选参数 --- -#}
        {%- if item.VRFNAME is not none -%}
            VRFNAME="{{item.VRFNAME}}",
        {%- endif -%}
        {%- if item.IFNAME is not none -%}
            IFNAME="{{item.IFNAME}}",
        {%- endif -%}
        {%- if item.BFDENABLE is not none -%}
            BFDENABLE={{item.BFDENABLE}},
        {%- endif -%}
        {%- if item.DHCPENABLE is not none -%}
            DHCPENABLE={{item.DHCPENABLE}},
        {%- endif -%}
        {%- if item.PREFERENCE is not none -%}
            PREFERENCE={{item.PREFERENCE}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_optional_user_downlink_route -%}
    {%- for item in add_srroute6_list_1 -%}
        ADD SRROUTE6:
        {#- --- 必选参数 --- -#}
        AFTYPE={{item.AFTYPE}},
        PREFIX="{{item.PREFIX}}",
        MASKLENGTH={{item.MASKLENGTH}},
        {#- --- 可选参数 --- -#}
        {%- if item.VRFNAME is not none -%}
            VRFNAME="{{item.VRFNAME}}",
        {%- endif -%}
        {%- if item.IFNAME is not none -%}
            IFNAME="{{item.IFNAME}}",
        {%- endif -%}
        {%- if item.BFDENABLE is not none -%}
            BFDENABLE={{item.BFDENABLE}},
        {%- endif -%}
        {%- if item.DHCPENABLE is not none -%}
            DHCPENABLE={{item.DHCPENABLE}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 1.8 使能静态地址用户路由冗余功能。

```jinja2
{%- for item in set_redunduser_list -%}
    SET REDUNDUSER:
    {#- --- 必选参数 --- -#}
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

### 2 配置备用UPF的静态地址用户路由冗余功能。

#### 2.1 配置地址池信息。

##### 2.1.1 //风筝S

```jinja2
{%- if is_scenario_kite_s -%}
    {%- for item in mod_pool_list_2 -%}
        MOD POOL:
        {#- --- 必选参数 --- -#}
        POOLNAME="{{item.POOLNAME}}",
        {#- --- 可选参数 --- -#}
        {%- if item.POOLTYPE is not none -%}
            POOLTYPE={{item.POOLTYPE}},
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
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

##### 2.1.2 //风筝M或风筝L

```jinja2
{%- if is_scenario_kite_m_or_l -%}
    {%- for item in mod_uppool_list_2 -%}
        MOD UPPOOL:
        {#- --- 必选参数 --- -#}
        POOLNAME="{{item.POOLNAME}}",
        {#- --- 可选参数 --- -#}
        {%- if item.POOLTYPE is not none -%}
            POOLTYPE={{item.POOLTYPE}},
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
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

#### 2.2 配置冗余备份重定向IP。

```jinja2
{%- for item in add_redundrdtip_list_2 -%}
    ADD REDUNDRDTIP:
    {#- --- 必选参数 --- -#}
    IPVERSION={{item.IPVERSION}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPVERSION=IPv4 时必选 --- -#}
    {%- if item.IPVERSION == 'IPv4' -%}
        IPV4ADDRESS="{{item.IPV4ADDRESS}}",
    {%- endif -%}
    {#- --- 条件必选：IPVERSION=IPv6 时必选 --- -#}
    {%- if item.IPVERSION == 'IPv6' -%}
        IPV6ADDRESS="{{item.IPV6ADDRESS}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 2.3 配置LoopBack接口。

```jinja2
{%- for item in add_interface_list_2 -%}
    ADD INTERFACE:
    {#- --- 必选参数 --- -#}
    IFNAME="{{item.IFNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.IFADMINSTATUS is not none -%}
        IFADMINSTATUS={{item.IFADMINSTATUS}},
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_ipbindvpn_list_2 -%}
    ADD IPBINDVPN:
    {#- --- 必选参数 --- -#}
    IFNAME="{{item.IFNAME}}",
    VRFNAME="{{item.VRFNAME}}",
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_ifipv4address_list_2 -%}
    ADD IFIPV4ADDRESS:
    {#- --- 必选参数 --- -#}
    IFNAME="{{item.IFNAME}}",
    IFIPADDR="{{item.IFIPADDR}}",
    SUBNETMASK="{{item.SUBNETMASK}}",
    ;
{%- endfor -%}
```

#### 2.4 配置GRE Tunnel。

```jinja2
{%- for item in add_interface_list_3 -%}
    ADD INTERFACE:
    {#- --- 必选参数 --- -#}
    IFNAME="{{item.IFNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.IFMTU is not none -%}
        IFMTU={{item.IFMTU}},
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_gretunnel_list_1 -%}
    ADD GRETUNNEL:
    {#- --- 必选参数 --- -#}
    TNLNAME="{{item.TNLNAME}}",
    TNLTYPE={{item.TNLTYPE}},
    {#- --- 可选参数 --- -#}
    {%- if item.DSTVPNNAME is not none -%}
        DSTVPNNAME="{{item.DSTVPNNAME}}",
    {%- endif -%}
    {%- if item.GREKEYEN is not none -%}
        GREKEYEN={{item.GREKEYEN}},
    {%- endif -%}
    {%- if item.KEEPALVEN is not none -%}
        KEEPALVEN={{item.KEEPALVEN}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：TNLTYPE=gre 时必选 --- -#}
    {%- if item.TNLTYPE == 'gre' -%}
        SRCTYPE={{item.SRCTYPE}},
    {%- endif -%}
    {#- --- 条件必选：SRCTYPE=if_name 时必选 --- -#}
    {%- if item.SRCTYPE == 'if_name' -%}
        SRCIFNAME="{{item.SRCIFNAME}}",
    {#- --- 条件必选：SRCTYPE6=if_name 时必选 --- -#}
    {%- elif item.SRCTYPE6 == 'if_name' -%}
        SRCIFNAME="{{item.SRCIFNAME}}",
    {%- endif -%}
    {#- --- 条件必选：GREKEYEN=TRUE 时必选 --- -#}
    {%- if item.GREKEYEN == 'TRUE' -%}
        GREKEY="{{item.GREKEY}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：TNLTYPE=gre 时可选 --- -#}
    {%- if item.TNLTYPE == 'gre' -%}
        {%- if item.DSTIPADDR is not none -%}
            DSTIPADDR="{{item.DSTIPADDR}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：TNLTYPE=gre/gre6 时可选 --- -#}
    {%- if item.TNLTYPE in ['gre', 'gre6'] -%}
        {%- if item.REDUNDANCYEN is not none -%}
            REDUNDANCYEN={{item.REDUNDANCYEN}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_ipbindvpn_list_3 -%}
    ADD IPBINDVPN:
    {#- --- 必选参数 --- -#}
    IFNAME="{{item.IFNAME}}",
    VRFNAME="{{item.VRFNAME}}",
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_ifipv4address_list_3 -%}
    ADD IFIPV4ADDRESS:
    {#- --- 必选参数 --- -#}
    IFNAME="{{item.IFNAME}}",
    IFIPADDR="{{item.IFIPADDR}}",
    SUBNETMASK="{{item.SUBNETMASK}}",
    ;
{%- endfor -%}
```

```jinja2
{%- for item in set_ifipv6enable_list_1 -%}
    SET IFIPV6ENABLE:
    {#- --- 必选参数 --- -#}
    IFNAME="{{item.IFNAME}}",
    ENABLEFLAG={{item.ENABLEFLAG}},
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：ENABLEFLAG=TRUE 时可选 --- -#}
    {%- if item.ENABLEFLAG == 'TRUE' -%}
        {%- if item.MTU is not none -%}
            MTU={{item.MTU}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_ifipv6address_list_1 -%}
    ADD IFIPV6ADDRESS:
    {#- --- 必选参数 --- -#}
    IFNAME="{{item.IFNAME}}",
    IPV6ADDRESS="{{item.IPV6ADDRESS}}",
    PREFIXLEN={{item.PREFIXLEN}},
    ;
{%- endfor -%}
```

#### 2.5 配置IPv4静态路由。

```jinja2
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
    {%- if item.IFNAME is not none -%}
        IFNAME="{{item.IFNAME}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 2.6 配置IPv6静态路由。

```jinja2
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
    {%- if item.IFNAME is not none -%}
        IFNAME="{{item.IFNAME}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 2.7 使能静态地址用户路由冗余功能。

```jinja2
{%- for item in set_redunduser_list_1 -%}
    SET REDUNDUSER:
    {#- --- 必选参数 --- -#}
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

#### 2.8 使能IPv4/IPv6上行报文隧道转发功能。

```jinja2
{%- for item in set_apnredundupsw_list -%}
    SET APNREDUNDUPSW:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    {#- --- 可选参数 --- -#}
    {%- if item.IPV4SWITCH is not none -%}
        IPV4SWITCH={{item.IPV4SWITCH}},
    {%- endif -%}
    {%- if item.IPV6SWITCH is not none -%}
        IPV6SWITCH={{item.IPV6SWITCH}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 配置两个UPF之间的GRE隧道对应的子接口相关数据，此处仅以一个UPF的脚本举例，脚本中的参数是举例，仅供参考，实际配置时以实际局点规划为准，配置步骤及参数说明与对应的专线配置相同。

#### 3.1 虚机容器：NP卡+DCGW场景。

```jinja2
{%- if is_scenario_vm_np_card_dcgw -%}
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
{%- endif -%}
```

```jinja2
{%- if is_scenario_vm_np_card_dcgw -%}
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
            {%- if item.ROUTERID is not none -%}
                ROUTERID="{{item.ROUTERID}}",
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_vm_np_card_dcgw -%}
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

```jinja2
{%- if is_scenario_vm_np_card_dcgw -%}
    {%- for item in add_interface_list_4 -%}
        ADD INTERFACE:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_vm_np_card_dcgw -%}
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
{%- if is_scenario_vm_np_card_dcgw -%}
    {%- for item in add_ethsubif_list -%}
        ADD ETHSUBIF:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        VLANTYPEVID={{item.VLANTYPEVID}},
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_vm_np_card_dcgw -%}
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
{%- if is_scenario_vm_np_card_dcgw -%}
    {%- for item in set_ifipv6enable_list_2 -%}
        SET IFIPV6ENABLE:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        ENABLEFLAG={{item.ENABLEFLAG}},
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_vm_np_card_dcgw -%}
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

```jinja2
{%- if is_scenario_vm_np_card_dcgw -%}
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

```jinja2
{%- if is_scenario_vm_np_card_dcgw -%}
    {%- for item in add_srroute_list_3 -%}
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

```jinja2
{%- if is_scenario_vm_np_card_dcgw -%}
    {%- for item in add_srroute6_list_3 -%}
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

#### 3.2 裸机容器：直连DCGW（交换机）场景

```jinja2
{%- if is_scenario_bare_metal_dcgw -%}
    {%- for item in add_bgpvrf_list_1 -%}
        ADD BGPVRF:
        {#- --- 必选参数 --- -#}
        VRFNAME="{{item.VRFNAME}}",
        {#- --- 可选参数 --- -#}
        {%- if item.DEFAULTAFTYPE is not none -%}
            DEFAULTAFTYPE={{item.DEFAULTAFTYPE}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_bare_metal_dcgw -%}
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
            {%- if item.ROUTERID is not none -%}
                ROUTERID="{{item.ROUTERID}}",
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_bare_metal_dcgw -%}
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

```jinja2
{%- if is_scenario_bare_metal_dcgw -%}
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
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_bare_metal_dcgw -%}
    {%- for item in add_interface_list_5 -%}
        ADD INTERFACE:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_bare_metal_dcgw -%}
    {%- for item in add_ipbindvpn_list_5 -%}
        ADD IPBINDVPN:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        VRFNAME="{{item.VRFNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_bare_metal_dcgw -%}
    {%- for item in add_ethsubif_list_1 -%}
        ADD ETHSUBIF:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        VLANTYPEVID={{item.VLANTYPEVID}},
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_bare_metal_dcgw -%}
    {%- for item in add_ifipv4address_list_5 -%}
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
{%- if is_scenario_bare_metal_dcgw -%}
    {%- for item in set_ifipv6enable_list_3 -%}
        SET IFIPV6ENABLE:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        ENABLEFLAG={{item.ENABLEFLAG}},
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_bare_metal_dcgw -%}
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

```jinja2
{%- if is_scenario_bare_metal_dcgw -%}
    {%- for item in add_bfdsession_list_2 -%}
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

```jinja2
{%- if is_scenario_bare_metal_dcgw -%}
    {%- for item in add_srroute_list_5 -%}
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

```jinja2
{%- if is_scenario_bare_metal_dcgw -%}
    {%- for item in add_srroute6_list_5 -%}
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

#### 3.3 虚机容器：NP卡+直连CE/PE场景

```jinja2
{%- if is_scenario_vm_np_card_ce_pe -%}
    {%- for item in add_interface_list_6 -%}
        ADD INTERFACE:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        {#- --- 可选参数 --- -#}
        {%- if item.IFDF is not none -%}
            IFDF={{item.IFDF}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_vm_np_card_ce_pe -%}
    {%- for item in add_ipbindvpn_list_6 -%}
        ADD IPBINDVPN:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        VRFNAME="{{item.VRFNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_vm_np_card_ce_pe -%}
    {%- for item in add_ethsubif_list_2 -%}
        ADD ETHSUBIF:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        VLANTYPEVID={{item.VLANTYPEVID}},
        {#- --- 可选参数 --- -#}
        {%- if item.SUBIFTYPE is not none -%}
            SUBIFTYPE={{item.SUBIFTYPE}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_vm_np_card_ce_pe -%}
    {%- for item in add_ifipv4address_list_6 -%}
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
{%- if is_scenario_vm_np_card_ce_pe -%}
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
{%- if is_scenario_vm_np_card_ce_pe -%}
    {%- for item in add_ifipv6address_list_4 -%}
        ADD IFIPV6ADDRESS:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        IPV6ADDRESS="{{item.IPV6ADDRESS}}",
        PREFIXLEN={{item.PREFIXLEN}},
        {#- --- 可选参数 --- -#}
        {%- if item.ADDRTYPE is not none -%}
            ADDRTYPE={{item.ADDRTYPE}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_vm_np_card_ce_pe -%}
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

```jinja2
{%- if is_scenario_vm_np_card_ce_pe -%}
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

```jinja2
{%- if is_scenario_vm_np_card_ce_pe -%}
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

```jinja2
{%- if is_scenario_vm_np_card_ce_pe -%}
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

```jinja2
{%- if is_scenario_vm_np_card_ce_pe -%}
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
        {%- if item.NETWORKTYPE is not none -%}
            NETWORKTYPE={{item.NETWORKTYPE}},
        {%- endif -%}
        {%- if item.P2MPMASKIGN is not none -%}
            P2MPMASKIGN={{item.P2MPMASKIGN}},
        {%- endif -%}
        {%- if item.SMARTDISCOVER is not none -%}
            SMARTDISCOVER={{item.SMARTDISCOVER}},
        {%- endif -%}
        {%- if item.BFDENABLE is not none -%}
            BFDENABLE={{item.BFDENABLE}},
        {%- endif -%}
        {%- if item.FRRBINDINGFLAG is not none -%}
            FRRBINDINGFLAG={{item.FRRBINDINGFLAG}},
        {%- endif -%}
        {%- if item.FRRBLOCKFLAG is not none -%}
            FRRBLOCKFLAG={{item.FRRBLOCKFLAG}},
        {%- endif -%}
        {%- if item.BFDBLOCK is not none -%}
            BFDBLOCK={{item.BFDBLOCK}},
        {%- endif -%}
        {%- if item.SUPPEREACH is not none -%}
            SUPPEREACH={{item.SUPPEREACH}},
        {%- endif -%}
        {%- if item.MTUENABLE is not none -%}
            MTUENABLE={{item.MTUENABLE}},
        {%- endif -%}
        {%- if item.MPLSLDPAUTOCFG is not none -%}
            MPLSLDPAUTOCFG={{item.MPLSLDPAUTOCFG}},
        {%- endif -%}
        {%- if item.LDPSYNCENABLE is not none -%}
            LDPSYNCENABLE={{item.LDPSYNCENABLE}},
        {%- endif -%}
        {%- if item.LDPSYNCBLOCK is not none -%}
            LDPSYNCBLOCK={{item.LDPSYNCBLOCK}},
        {%- endif -%}
        {%- if item.VIRTUALSYSFLAG is not none -%}
            VIRTUALSYSFLAG={{item.VIRTUALSYSFLAG}},
        {%- endif -%}
        {%- if item.MAXCOSTFLAG is not none -%}
            MAXCOSTFLAG={{item.MAXCOSTFLAG}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_vm_np_card_ce_pe -%}
    {%- for item in add_ospfv3interface_list -%}
        ADD OSPFV3INTERFACE:
        {#- --- 必选参数 --- -#}
        PROCID={{item.PROCID}},
        AREAID="{{item.AREAID}}",
        IFNAME="{{item.IFNAME}}",
        {#- --- 可选参数 --- -#}
        {%- if item.MTUENABLE is not none -%}
            MTUENABLE={{item.MTUENABLE}},
        {%- endif -%}
        {%- if item.NETWORKTYPE is not none -%}
            NETWORKTYPE={{item.NETWORKTYPE}},
        {%- endif -%}
        {%- if item.BFDENABLE is not none -%}
            BFDENABLE={{item.BFDENABLE}},
        {%- endif -%}
        {%- if item.FRRBINDINGFLAG is not none -%}
            FRRBINDINGFLAG={{item.FRRBINDINGFLAG}},
        {%- endif -%}
        {%- if item.FRRBLOCKFLAG is not none -%}
            FRRBLOCKFLAG={{item.FRRBLOCKFLAG}},
        {%- endif -%}
        {%- if item.BFDBLOCK is not none -%}
            BFDBLOCK={{item.BFDBLOCK}},
        {%- endif -%}
        {%- if item.DRPRI is not none -%}
            DRPRI={{item.DRPRI}},
        {%- endif -%}
        {%- if item.VIRTUALSYSFLAG is not none -%}
            VIRTUALSYSFLAG={{item.VIRTUALSYSFLAG}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_vm_np_card_ce_pe -%}
    {%- for item in add_ospfnetwork_list -%}
        ADD OSPFNETWORK:
        {#- --- 必选参数 --- -#}
        PROCID={{item.PROCID}},
        AREAID="{{item.AREAID}}",
        IPADDRESS="{{item.IPADDRESS}}",
        WILDCARDMASK="{{item.WILDCARDMASK}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_vm_np_card_ce_pe -%}
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
{%- if is_scenario_vm_np_card_ce_pe -%}
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

#### 3.4 虚机容器：标卡+DCGW场景

```jinja2
{%- if is_scenario_vm_standard_card_dcgw -%}
    {%- for item in set_autoconfig_list -%}
        SET AUTOCONFIG:
        {#- --- 必选参数 --- -#}
        SWITCHFLAG={{item.SWITCHFLAG}},
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_vm_standard_card_dcgw -%}
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
        {#- --- 条件必选：IPALLOCTYPE6=USER_CONFIG 时必选 --- -#}
        {%- if item.IPALLOCTYPE6 == 'USER_CONFIG' -%}
            BEGINADDR6="{{item.BEGINADDR6}}",
        {%- endif -%}
        {#- --- 条件必选：IPALLOCTYPE6=USER_CONFIG 时必选 --- -#}
        {%- if item.IPALLOCTYPE6 == 'USER_CONFIG' -%}
            ENDADDR6="{{item.ENDADDR6}}",
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
        {#- --- 条件可选：OSPFENABLE=FALSE 时可选 --- -#}
        {%- if item.OSPFENABLE == 'FALSE' -%}
            {%- if item.OSPFGRPENABLE is not none -%}
                OSPFGRPENABLE={{item.OSPFGRPENABLE}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_vm_standard_card_dcgw -%}
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
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_vm_standard_card_dcgw -%}
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
        {#- --- 条件必选：NEXTHOPALLOCTYPE6=CONFIG 时必选 --- -#}
        {%- if item.NEXTHOPALLOCTYPE6 == 'CONFIG' -%}
            NEXTHOP6="{{item.NEXTHOP6}}",
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
{%- if is_scenario_vm_standard_card_dcgw -%}
    {%- for item in set_autoconfig_list_1 -%}
        SET AUTOCONFIG:
        {#- --- 必选参数 --- -#}
        SWITCHFLAG={{item.SWITCHFLAG}},
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_vm_standard_card_dcgw -%}
    {%- for item in add_interface_list_8 -%}
        ADD INTERFACE:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        {#- --- 可选参数 --- -#}
        {%- if item.IFADMINSTATUS is not none -%}
            IFADMINSTATUS={{item.IFADMINSTATUS}},
        {%- endif -%}
        {%- if item.IFMTU is not none -%}
            IFMTU={{item.IFMTU}},
        {%- endif -%}
        {%- if item.IFDF is not none -%}
            IFDF={{item.IFDF}},
        {%- endif -%}
        {%- if item.IFSTATIENABLE is not none -%}
            IFSTATIENABLE={{item.IFSTATIENABLE}},
        {%- endif -%}
        {%- if item.IFTRAPENABLE is not none -%}
            IFTRAPENABLE={{item.IFTRAPENABLE}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_vm_standard_card_dcgw -%}
    {%- for item in add_ipbindvpn_list_8 -%}
        ADD IPBINDVPN:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        VRFNAME="{{item.VRFNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_vm_standard_card_dcgw -%}
    {%- for item in add_ifipv4address_list_8 -%}
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
{%- if is_scenario_vm_standard_card_dcgw -%}
    {%- for item in add_interface_list_9 -%}
        ADD INTERFACE:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        {#- --- 可选参数 --- -#}
        {%- if item.IFADMINSTATUS is not none -%}
            IFADMINSTATUS={{item.IFADMINSTATUS}},
        {%- endif -%}
        {%- if item.IFMTU is not none -%}
            IFMTU={{item.IFMTU}},
        {%- endif -%}
        {%- if item.IFDF is not none -%}
            IFDF={{item.IFDF}},
        {%- endif -%}
        {%- if item.IFSTATIENABLE is not none -%}
            IFSTATIENABLE={{item.IFSTATIENABLE}},
        {%- endif -%}
        {%- if item.IFTRAPENABLE is not none -%}
            IFTRAPENABLE={{item.IFTRAPENABLE}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_vm_standard_card_dcgw -%}
    {%- for item in add_ipbindvpn_list_9 -%}
        ADD IPBINDVPN:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        VRFNAME="{{item.VRFNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_vm_standard_card_dcgw -%}
    {%- for item in set_ifipv6enable_list_6 -%}
        SET IFIPV6ENABLE:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        ENABLEFLAG={{item.ENABLEFLAG}},
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_vm_standard_card_dcgw -%}
    {%- for item in add_ifipv6address_list_6 -%}
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
{%- if is_scenario_vm_standard_card_dcgw -%}
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
{%- endif -%}
```

```jinja2
{%- if is_scenario_vm_standard_card_dcgw -%}
    {%- for item in add_bgpvrf_list_2 -%}
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
{%- if is_scenario_vm_standard_card_dcgw -%}
    {%- for item in add_bgpvrfaf_list_4 -%}
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
            {%- if item.MAXLOADEBGPNUM is not none -%}
                MAXLOADEBGPNUM={{item.MAXLOADEBGPNUM}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_vm_standard_card_dcgw -%}
    {%- for item in add_importroute_list -%}
        ADD IMPORTROUTE:
        {#- --- 必选参数 --- -#}
        AFTYPE={{item.AFTYPE}},
        IMPORTPROTOCOL={{item.IMPORTPROTOCOL}},
        {#- --- 可选参数 --- -#}
        {%- if item.VRFNAME is not none -%}
            VRFNAME="{{item.VRFNAME}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_vm_standard_card_dcgw -%}
    {%- for item in add_bgppeer_list_8 -%}
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
            {%- if item.PSWDTYPE is not none -%}
                PSWDTYPE={{item.PSWDTYPE}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_vm_standard_card_dcgw -%}
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
        {#- --- 条件必选：ADDRESSTYPE=ipv6 时必选 --- -#}
        {%- if item.ADDRESSTYPE == 'ipv6' -%}
            REMOTEADDRESSV6="{{item.REMOTEADDRESSV6}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 3.5 裸机容器：直连CE/PE场景

```jinja2
{%- if is_scenario_bare_metal_ce_pe -%}
    {%- for item in add_interface_list_10 -%}
        ADD INTERFACE:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        {#- --- 可选参数 --- -#}
        {%- if item.IFDF is not none -%}
            IFDF={{item.IFDF}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_bare_metal_ce_pe -%}
    {%- for item in add_ipbindvpn_list_10 -%}
        ADD IPBINDVPN:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        VRFNAME="{{item.VRFNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_bare_metal_ce_pe -%}
    {%- for item in add_ethsubif_list_4 -%}
        ADD ETHSUBIF:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        VLANTYPEVID={{item.VLANTYPEVID}},
        {#- --- 可选参数 --- -#}
        {%- if item.SUBIFTYPE is not none -%}
            SUBIFTYPE={{item.SUBIFTYPE}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_bare_metal_ce_pe -%}
    {%- for item in add_ifipv4address_list_9 -%}
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
{%- if is_scenario_bare_metal_ce_pe -%}
    {%- for item in set_ifipv6enable_list_7 -%}
        SET IFIPV6ENABLE:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        ENABLEFLAG={{item.ENABLEFLAG}},
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_bare_metal_ce_pe -%}
    {%- for item in add_ifipv6address_list_7 -%}
        ADD IFIPV6ADDRESS:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        IPV6ADDRESS="{{item.IPV6ADDRESS}}",
        PREFIXLEN={{item.PREFIXLEN}},
        {#- --- 可选参数 --- -#}
        {%- if item.ADDRTYPE is not none -%}
            ADDRTYPE={{item.ADDRTYPE}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_bare_metal_ce_pe -%}
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

```jinja2
{%- if is_scenario_bare_metal_ce_pe -%}
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
{%- if is_scenario_bare_metal_ce_pe -%}
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


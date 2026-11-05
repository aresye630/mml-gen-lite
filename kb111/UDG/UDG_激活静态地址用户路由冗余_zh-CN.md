---
id: GWFD-010107
name: 激活静态地址用户路由冗余
ne_type: UDG
type: feature
description: 网络同时部署主用备用两台UDG。当主用UDG故障或者主用UDG通信链路故障的时候通过备份tunnel，将静态地址用户的下行数据备份到备用UDG上。  适用于PGW-U、UPF。
risk_level: ''
doc_source: ["特性部署","特性指南","UDG特性指南","基本接入功能","GWFD-010107 静态地址用户路由冗余","激活静态地址用户路由冗余"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
网络同时部署主用备用两台UDG。当主用UDG故障或者主用UDG通信链路故障的时候通过备份tunnel，将静态地址用户的下行数据备份到备用UDG上。适用于PGW-U、UPF。

## 必备事项
前提条件

* 请仔细阅读GWFD-010107 静态地址用户路由冗余。
* 已通过初始配置完成主备LoopBack接口的路由互通配置。
* 静态地址用户路由冗余特性开启和关闭前都要确保APN下无使用静态路由冗余功能的用户。
* 本特性与UNC配合使用生效，请参考UNC中的**WSFD-107021 静态地址用户路由冗余**。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    add_pool_list:
      type: items
      properties:
        POOLNAME:
          name: '地址池名称'
          type: string
          minLength: 1
          maxLength: 79
          required: true
          description: '配置静态地址池。'
          data_source: '本端规划'
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
          data_source: '固定取值'
          pattern: ''
          default: LOCAL
        IPVERSION:
          name: 'IP地址类型'
          type: string
          enum:
          - IPV4
          - IPV6
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: IPV4
        HASVPN:
          name: '绑定VPN'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: DISABLE
        VPNINSTANCE:
          name: 'VPN实例名'
          type: string
          minLength: 1
          maxLength: 31
          required: false
          description: '已通过**ADD L3VPNINST**命令配置，可以使用**LST L3VPNINST**命令进行查询。  说明：  如下三者绑定的VPN实例必须一致。   * 地址池绑定的VPN实例。 * 用户激活使用的APN绑定的VPN实例。 * Tunnel接口绑定的VPN实例。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        REDUNDFUNC:
          name: '冗余备份功能开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '此特性需要地址池的功能开关和全局开关（**SET REDUNDUSER**）同时打开才生效。'
          data_source: '固定取值'
          pattern: ''
          default: DISABLE
        MASTERFLAG:
          name: '主用标记'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '当使能上行转发功能，且需要具备UE互访能力时，配置此参数，确保UE互访成功。'
          data_source: '固定取值'
          pattern: ''
          default: DISABLE
        ALARMSWITCH:
          name: '告警特性是否使能'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
        CHECKIPVALID:
          name: '检查地址合法性'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
        IMSSW:
          name: 'IMS开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ENABLE
        IPLEASE:
          name: '地址租约使能标志'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
        RELEASETIME:
          name: '地址租期（秒）'
          type: integer
          minimum: 0
          maximum: 86400
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 10
        SINGLEIPFLAG:
          name: '小地址池标志'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
    add_section_list:
      type: items
      properties:
        POOLNAME:
          name: '地址池名称'
          type: string
          minLength: 0
          maxLength: 79
          required: true
          description: '* 配置静态地址段，主备UDG要规划相同的地址段。 * 规划的地址段要包含SMF上配置的静态地址段。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        SECTIONNUM:
          name: '地址段号'
          type: integer
          minimum: 0
          maximum: 63
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPVERSION:
          name: 'IP地址类型'
          type: string
          enum:
          - IPV4
          - IPV6
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        V4STARTIP:
          name: '地址段的起始IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        V4ENDIP:
          name: '地址段的终止IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        V6PREFIXSTART:
          name: 'IPv6前缀起始地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        V6PREFIXEND:
          name: 'IPv6前缀结束地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        V6PREFIXLENGTH:
          name: 'IPv6前缀长度'
          type: integer
          minimum: 49
          maximum: 64
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_section_list_1:
      type: items
      properties:
        POOLNAME:
          name: '地址池名称'
          type: string
          minLength: 0
          maxLength: 79
          required: true
          description: '* 配置静态地址段，主备UDG要规划相同的地址段。 * 规划的地址段要包含SMF上配置的静态地址段。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        SECTIONNUM:
          name: '地址段号'
          type: integer
          minimum: 0
          maximum: 63
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPVERSION:
          name: 'IP地址类型'
          type: string
          enum:
          - IPV4
          - IPV6
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        V6PREFIXSTART:
          name: 'IPv6前缀起始地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        V6PREFIXEND:
          name: 'IPv6前缀结束地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        V6PREFIXLENGTH:
          name: 'IPv6前缀长度'
          type: integer
          minimum: 49
          maximum: 64
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        V4STARTIP:
          name: '地址段的起始IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        V4ENDIP:
          name: '地址段的终止IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_poolgroup_list:
      type: items
      properties:
        POOLGRPNAME:
          name: '地址池组名称'
          type: string
          minLength: 0
          maxLength: 79
          required: true
          description: '配置地址池组。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPV4ALLOCPRIALG:
          name: 'IPV4基于地址池优先级分配地址算法'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
    add_poolbindgroup_list:
      type: items
      properties:
        POOLGROUPNAME:
          name: '地址池组名称'
          type: string
          minLength: 0
          maxLength: 79
          required: true
          description: '配置指定地址池与地址池组的绑定关系。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        POOLNAME:
          name: '地址池名称'
          type: string
          minLength: 0
          maxLength: 79
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_apn_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '指定APN名称。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        HASVPN:
          name: '绑定VPN'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: DISABLE
        VPNINSTANCE:
          name: 'VPN实例名'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: '已通过**ADD L3VPNINST**命令配置，可以使用**LST L3VPNINST**命令进行查询。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_poolgrpmap_list:
      type: items
      properties:
        MAPPINGNAME:
          name: '映射规则名称'
          type: string
          minLength: 0
          maxLength: 79
          required: true
          description: 'APN绑定静态地址池组。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        APN:
          name: 'APN名称'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        POOLGROUPNAME:
          name: '地址池组名称'
          type: string
          minLength: 0
          maxLength: 79
          required: true
          description: ''
          data_source: '已配置数据中获取'
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
          description: '* 配置虚拟重定向IP，本端规划的虚拟IP，将业务流重定向到Gre Tunnel。 * 重定向IP是全局规划的，只在内部做重定向转发，不对外发布，只要保证和其他路由不冲突即可，所以主备UDG的重定向IP可以规划为相同IP，也可以规划为不同IP。'
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
          data_source: '全网规划'
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
    add_ipbindvpn_list:
      type: items
      properties:
        IFNAME:
          name: '接口名'
          type: string
          maxLength: 63
          required: true
          description: '与Loopback接口关联的VPN实例。  Loopback接口和Tunnel接口绑定的VPN实例不同，完成物理和业务上的划分。'
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
    add_interface_list_1:
      type: items
      properties:
        IFNAME:
          name: '接口名'
          type: string
          maxLength: 63
          required: true
          description: '针对IPv4生效，MTU配置原则：封装GRE隧道出外联口不会再次分片。'
          data_source: '全网规划'
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
          description: '本端设备的Loopback接口名称，已通过**ADD INTERFACE**命令配置。'
          data_source: '从已配置数据中获取'
          pattern: ''
          default: ''
        DSTVPNNAME:
          name: '目的VPN名称'
          type: string
          maxLength: 31
          required: false
          description: '隧道的目的地址所属的VPN实例的名称。  已通过**ADD L3VPNINST**命令配置，可以使用**LST L3VPNINST**命令进行查询。'
          data_source: '从已配置数据中获取'
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
          data_source: '本端规划'
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
        KEEPALVPERIOD:
          name: 'Keepalive报文发送周期'
          type: integer
          minimum: 1
          maximum: 32767
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 5
        KEEPALVRETRYCNT:
          name: '不可达计数器参数'
          type: integer
          minimum: 1
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 3
        SRCIPADDR:
          name: '源IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DSTIPV6ADDR:
          name: '目的IPv6地址'
          type: string
          maxLength: 39
          required: false
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
          description: '与接口关联的VPN实例。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: true
          description: '已通过**ADD L3VPNINST**命令配置，可以使用**LST L3VPNINST**命令进行查询。'
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
          description: '在主UDG配置下行缺省低优先级静态地址用户网段路由入冗余GRE隧道，该路由的目的地址网段应与用户地址池网段一致，优先级应低于业务侧下发的静态地址用户WLR路由优先级。路由优先级参数（PREFERENCE）不配置时默认为60，优先级值越大优先级越低。  说明：  PGW-U/UPF与PDN/DN之间配置GRE隧道，并且由PDN/DN侧服务器端配置高低优先级路由。此场景下需要在主UDG配置下行缺省低优先级静态地址用户网段路由入冗余GRE隧道。'
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
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
        PREFIX:
          name: '路由前缀'
          type: string
          maxLength: 39
          required: true
          description: ''
          data_source: '从已配置数据中获取'
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
    add_ospfinterface_list:
      type: items
      properties:
        PROCID:
          name: 'OSPF进程号'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: true
          description: '主备LoopBack接口的路由需要打通，当使用OSPF路由时，可以使用**ADD OSPFINTERFACE**或**ADD OSPFNETWORK**命令打通路由，静态路由或BGP请按照对应配置增加，具体路由方式对应的配置命令可以参见“初始配置”中的“组网路由配置”。'
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
          name: '接口名'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    mod_ospfimportroute_list:
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
          required: true
          description: ''
          data_source: ''
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
          description: '对于N6口路由，要检查路由发布优先级，主UPF优先级要高于备UPF优先级。   * BGP方式，通过**MOD** **IMPORTROUTE**命令配置。 * OSPF方式，通过**MOD OSPFIMPORTROUTE**命令配置。 * 非动态方式，则需要PDN/DN侧服务器端配置高低静态路由到主、备UPF，且通过路由探测联动路由生效。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        COST:
          name: '路径Cost值'
          type: integer
          minimum: 0
          maximum: 16777214
          required: false
          description: ''
          data_source: '全网规划'
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
          default: ''
        PROTOCOLPROCID:
          name: '协议进程号'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    mod_importroute_list:
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
    add_pool_list_2:
      type: items
      properties:
        POOLNAME:
          name: '地址池名称'
          type: string
          minLength: 1
          maxLength: 79
          required: true
          description: '配置静态地址池。'
          data_source: '本端规划'
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
          data_source: '固定取值'
          pattern: ''
          default: LOCAL
        IPVERSION:
          name: 'IP地址类型'
          type: string
          enum:
          - IPV4
          - IPV6
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: IPV4
        HASVPN:
          name: '绑定VPN'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: DISABLE
        VPNINSTANCE:
          name: 'VPN实例名'
          type: string
          minLength: 1
          maxLength: 31
          required: false
          description: '已通过**ADD L3VPNINST**命令配置，可以使用**LST L3VPNINST**命令进行查询。  说明：  如下三者绑定的VPN实例必须一致。   * 地址池绑定的VPN实例。 * 用户激活使用的APN绑定的VPN实例。 * Tunnel接口绑定的VPN实例。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        REDUNDFUNC:
          name: '冗余备份功能开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '此特性需要地址池的功能开关和全局开关（**SET REDUNDUSER**）同时打开才生效。'
          data_source: '固定取值'
          pattern: ''
          default: DISABLE
        MASTERFLAG:
          name: '主用标记'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '当使能上行转发功能，且需要具备UE互访能力时，配置此参数，确保UE互访成功。'
          data_source: '固定取值'
          pattern: ''
          default: DISABLE
        ALARMSWITCH:
          name: '告警特性是否使能'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
        CHECKIPVALID:
          name: '检查地址合法性'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
        IMSSW:
          name: 'IMS开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ENABLE
        IPLEASE:
          name: '地址租约使能标志'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
        RELEASETIME:
          name: '地址租期（秒）'
          type: integer
          minimum: 0
          maximum: 86400
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 10
        SINGLEIPFLAG:
          name: '小地址池标志'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
    add_section_list_2:
      type: items
      properties:
        POOLNAME:
          name: '地址池名称'
          type: string
          minLength: 0
          maxLength: 79
          required: true
          description: '* 配置静态地址段，主备UDG要规划相同的地址段。 * 规划的地址段要包含SMF上配置的静态地址段。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        SECTIONNUM:
          name: '地址段号'
          type: integer
          minimum: 0
          maximum: 63
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPVERSION:
          name: 'IP地址类型'
          type: string
          enum:
          - IPV4
          - IPV6
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        V4STARTIP:
          name: '地址段的起始IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        V4ENDIP:
          name: '地址段的终止IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        V6PREFIXSTART:
          name: 'IPv6前缀起始地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        V6PREFIXEND:
          name: 'IPv6前缀结束地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        V6PREFIXLENGTH:
          name: 'IPv6前缀长度'
          type: integer
          minimum: 49
          maximum: 64
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_poolgroup_list_1:
      type: items
      properties:
        POOLGRPNAME:
          name: '地址池组名称'
          type: string
          minLength: 0
          maxLength: 79
          required: true
          description: '配置地址池组。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPV4ALLOCPRIALG:
          name: 'IPV4基于地址池优先级分配地址算法'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
    add_poolbindgroup_list_2:
      type: items
      properties:
        POOLGROUPNAME:
          name: '地址池组名称'
          type: string
          minLength: 0
          maxLength: 79
          required: true
          description: '配置指定地址池与地址池组的绑定关系。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        POOLNAME:
          name: '地址池名称'
          type: string
          minLength: 0
          maxLength: 79
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_apn_list_1:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '指定APN名称。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        HASVPN:
          name: '绑定VPN'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: DISABLE
        VPNINSTANCE:
          name: 'VPN实例名'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: '已通过**ADD L3VPNINST**命令配置，可以使用**LST L3VPNINST**命令进行查询。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_poolgrpmap_list_1:
      type: items
      properties:
        MAPPINGNAME:
          name: '映射规则名称'
          type: string
          minLength: 0
          maxLength: 79
          required: true
          description: 'APN绑定静态地址池组。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        APN:
          name: 'APN名称'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        POOLGROUPNAME:
          name: '地址池组名称'
          type: string
          minLength: 0
          maxLength: 79
          required: true
          description: ''
          data_source: '已配置数据中获取'
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
          description: '* 配置虚拟重定向IP，本端规划的虚拟IP，将业务流重定向到Gre Tunnel。 * 重定向IP是全局规划的，只在内部做重定向转发，不对外发布，只要保证和其他路由不冲突即可，所以主备UDG的重定向IP可以规划为相同IP，也可以规划为不同IP。'
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
          data_source: '全网规划'
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
    add_ipbindvpn_list_2:
      type: items
      properties:
        IFNAME:
          name: '接口名'
          type: string
          maxLength: 63
          required: true
          description: '与Loopback接口关联的VPN实例。  Loopback接口和Tunnel接口绑定的VPN实例不同，完成物理和业务上的划分。'
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
          data_source: '全网规划'
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
          description: '本端设备的Loopback接口名称，已通过**ADD INTERFACE**命令配置。'
          data_source: '从已配置数据中获取'
          pattern: ''
          default: ''
        DSTVPNNAME:
          name: '目的VPN名称'
          type: string
          maxLength: 31
          required: false
          description: '隧道的目的地址所属的VPN实例的名称。  已通过**ADD L3VPNINST**命令配置，可以使用**LST L3VPNINST**命令进行查询。'
          data_source: '从已配置数据中获取'
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
          data_source: '本端规划'
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
        KEEPALVPERIOD:
          name: 'Keepalive报文发送周期'
          type: integer
          minimum: 1
          maximum: 32767
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 5
        KEEPALVRETRYCNT:
          name: '不可达计数器参数'
          type: integer
          minimum: 1
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 3
        SRCIPADDR:
          name: '源IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DSTIPV6ADDR:
          name: '目的IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
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
          description: '与接口关联的VPN实例。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: true
          description: '已通过**ADD L3VPNINST**命令配置，可以使用**LST L3VPNINST**命令进行查询。'
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
    add_ospfinterface_list_1:
      type: items
      properties:
        PROCID:
          name: 'OSPF进程号'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: true
          description: '主备LoopBack接口的路由需要打通，当使用OSPF路由时，可以使用**ADD OSPFINTERFACE**或**ADD OSPFNETWORK**命令打通路由，静态路由或BGP请按照对应配置增加，具体路由方式对应的配置命令可以参见“初始配置”中的“组网路由配置”。'
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
          name: '接口名'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    mod_ospfimportroute_list_1:
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
          required: true
          description: ''
          data_source: ''
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
          description: '对于N6口路由，要检查路由发布优先级，主UPF优先级要高于备UPF优先级。   * BGP方式，通过**MOD** **IMPORTROUTE**命令配置。 * OSPF方式，通过**MOD OSPFIMPORTROUTE**命令配置。 * 非动态方式，则需要PDN/DN侧服务器端配置高低静态路由到主、备UPF，且通过路由探测联动路由生效。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        COST:
          name: '路径Cost值'
          type: integer
          minimum: 0
          maximum: 16777214
          required: false
          description: ''
          data_source: '全网规划'
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
          default: ''
        PROTOCOLPROCID:
          name: '协议进程号'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: false
          description: ''
          data_source: ''
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
          description: '配置APN路由冗余上行报文隧道转发功能开关，该命令仅在备用UDG配置。'
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
    set_apnredundupsw_list_1:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: ''
          data_source: ''
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
          data_source: ''
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
          data_source: ''
          pattern: ''
          default: ''
  examples:
    add_pool_list:
    - POOLNAME: 'pool1'
      POOLTYPE: EXTERNAL
      IPVERSION: IPV4
      HASVPN: ENABLE
      VPNINSTANCE: 'vpn1'
      REDUNDFUNC: ENABLE
      MASTERFLAG: ENABLE
      ALARMSWITCH: DISABLE
      CHECKIPVALID: DISABLE
      IMSSW: ENABLE
      IPLEASE: DISABLE
      RELEASETIME: 10
      SINGLEIPFLAG: DISABLE
    add_section_list:
    - POOLNAME: 'pool1'
      SECTIONNUM: 1
      IPVERSION: IPV4
      V4STARTIP: '10.1.1.0'
      V4ENDIP: '10.1.1.225'
      V6PREFIXSTART: 'fc00:1::1'
      V6PREFIXEND: 'fc00:1::1111'
      V6PREFIXLENGTH: 64
    add_section_list_1:
    - POOLNAME: 'pool2'
      SECTIONNUM: 2
      IPVERSION: IPV6
      V6PREFIXSTART: 'fc00:1::1'
      V6PREFIXEND: 'fc00:1::1111'
      V6PREFIXLENGTH: 64
      V4STARTIP: '10.1.1.0'
      V4ENDIP: '10.1.1.225'
    add_poolgroup_list:
    - POOLGRPNAME: 'poolgroup1'
      IPV4ALLOCPRIALG: ENABLE
    add_poolbindgroup_list:
    - POOLGROUPNAME: 'poolgroup1'
      POOLNAME: 'pool1'
    add_apn_list:
    - APN: 'test'
      HASVPN: ENABLE
      VPNINSTANCE: 'vpn1'
    add_poolgrpmap_list:
    - MAPPINGNAME: 'mapping1'
      APN: 'test'
      POOLGROUPNAME: 'poolgroup1'
    add_redundrdtip_list:
    - IPVERSION: IPv4
      IPV4ADDRESS: '192.168.0.1'
      IPV6ADDRESS: 'fc00:3::1'
    add_interface_list:
    - IFNAME: 'LoopBack1'
      IFADMINSTATUS: up
      IFMTU: 1500
    add_ipbindvpn_list:
    - IFNAME: 'LoopBack1'
      VRFNAME: 'vpn2'
    add_interface_list_1:
    - IFNAME: 'Tunnel1'
      IFMTU: 1500
      IFADMINSTATUS: up
    add_gretunnel_list:
    - TNLNAME: 'Tunnel1'
      SRCTYPE: if_name
      DSTIPADDR: '10.10.0.1'
      TNLTYPE: gre
      SRCIFNAME: 'LoopBack1'
      DSTVPNNAME: 'vpn2'
      REDUNDANCYEN: TRUE
      KEEPALVEN: TRUE
      SRCTYPE6: no_type
      KEEPALVPERIOD: 5
      KEEPALVRETRYCNT: 3
      SRCIPADDR: ''
      DSTIPV6ADDR: ''
    add_ipbindvpn_list_1:
    - IFNAME: 'Tunnel1'
      VRFNAME: 'vpn1'
    add_ifipv4address_list:
    - IFNAME: 'LoopBack1'
      IFIPADDR: '10.11.1.1'
      SUBNETMASK: '255.255.255.255'
    set_ifipv6enable_list:
    - IFNAME: 'Tunnel1'
      ENABLEFLAG: TRUE
      MTU: 1500
      AUTOLINKLOCAL: ''
    add_ifipv6address_list:
    - IFNAME: 'Tunnel1'
      IPV6ADDRESS: 'fc00:2::1'
      PREFIXLEN: 64
    add_srroute_list:
    - AFTYPE: ipv4unicast
      PREFIX: '192.168.0.1'
      MASKLENGTH: 32
      VRFNAME: 'vpn1'
      IFNAME: 'Tunnel1'
    add_srroute6_list:
    - AFTYPE: ipv6unicast
      PREFIX: 'fc00:3::1'
      MASKLENGTH: 128
      VRFNAME: 'vpn1'
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
      PREFERENCE: 60
    add_ospfinterface_list:
    - PROCID: 6
      AREAID: '0.0.0.5'
      IFNAME: 'LoopBack1'
    mod_ospfimportroute_list:
    - PROCID: 600
      TOPOID: 0
      PROTOCOL: wlr
      IMPTCOSTCFG: TRUE
      COST: 100
      PERMITIBGPCFG: ''
      PROTOCOLPROCID: ''
    mod_importroute_list:
    - VRFNAME: ''
      AFTYPE: ''
      IMPORTPROTOCOL: ''
      IMPORTPROCESSID: ''
    set_redunduser_list:
    - SWITCH: ENABLE
    add_pool_list_2:
    - POOLNAME: 'pool3'
      POOLTYPE: EXTERNAL
      IPVERSION: IPV4
      HASVPN: ENABLE
      VPNINSTANCE: 'vpn1'
      REDUNDFUNC: ENABLE
      MASTERFLAG: DISABLE
      ALARMSWITCH: DISABLE
      CHECKIPVALID: DISABLE
      IMSSW: ENABLE
      IPLEASE: DISABLE
      RELEASETIME: 10
      SINGLEIPFLAG: DISABLE
    add_section_list_2:
    - POOLNAME: 'pool3'
      SECTIONNUM: 3
      IPVERSION: IPV4
      V4STARTIP: '10.1.1.0'
      V4ENDIP: '10.1.1.225'
      V6PREFIXSTART: 'fc00:1::1'
      V6PREFIXEND: 'fc00:1::1111'
      V6PREFIXLENGTH: 64
    add_poolgroup_list_1:
    - POOLGRPNAME: 'poolgroup2'
      IPV4ALLOCPRIALG: ENABLE
    add_poolbindgroup_list_2:
    - POOLGROUPNAME: 'poolgroup2'
      POOLNAME: 'pool3'
    add_apn_list_1:
    - APN: 'test'
      HASVPN: ENABLE
      VPNINSTANCE: 'vpn1'
    add_poolgrpmap_list_1:
    - MAPPINGNAME: 'mapping2'
      APN: 'test'
      POOLGROUPNAME: 'poolgroup2'
    add_redundrdtip_list_2:
    - IPVERSION: IPv4
      IPV4ADDRESS: '192.168.0.1'
      IPV6ADDRESS: 'fc00:3::1'
    add_interface_list_2:
    - IFNAME: 'LoopBack2'
      IFADMINSTATUS: up
      IFMTU: 1500
    add_ipbindvpn_list_2:
    - IFNAME: 'LoopBack2'
      VRFNAME: 'vpn2'
    add_ifipv4address_list_2:
    - IFNAME: 'LoopBack2'
      IFIPADDR: '10.10.0.1'
      SUBNETMASK: '255.255.255.255'
    add_interface_list_3:
    - IFNAME: 'Tunnel2'
      IFMTU: 1500
      IFADMINSTATUS: up
    add_gretunnel_list_1:
    - TNLNAME: 'Tunnel2'
      SRCTYPE: if_name
      DSTIPADDR: '10.11.1.1'
      TNLTYPE: gre
      SRCIFNAME: 'LoopBack2'
      DSTVPNNAME: 'vpn2'
      REDUNDANCYEN: TRUE
      KEEPALVEN: TRUE
      SRCTYPE6: no_type
      KEEPALVPERIOD: 5
      KEEPALVRETRYCNT: 3
      SRCIPADDR: ''
      DSTIPV6ADDR: ''
    add_ipbindvpn_list_3:
    - IFNAME: 'Tunnel2'
      VRFNAME: 'vpn1'
    add_ifipv4address_list_3:
    - IFNAME: 'Tunnel2'
      IFIPADDR: '10.11.1.4'
      SUBNETMASK: '255.255.255.0'
    set_ifipv6enable_list_1:
    - IFNAME: 'Tunnel2'
      ENABLEFLAG: TRUE
      MTU: 1500
      AUTOLINKLOCAL: ''
    add_ifipv6address_list_1:
    - IFNAME: 'Tunnel2'
      IPV6ADDRESS: 'fc00:2::2'
      PREFIXLEN: 64
    add_srroute_list_2:
    - AFTYPE: ipv4unicast
      PREFIX: '192.168.0.1'
      MASKLENGTH: 32
      VRFNAME: 'vpn1'
      IFNAME: 'Tunnel2'
    add_srroute6_list_2:
    - AFTYPE: ipv6unicast
      PREFIX: 'fc00:3::1'
      MASKLENGTH: 128
      VRFNAME: 'vpn1'
      IFNAME: 'Tunnel2'
    add_ospfinterface_list_1:
    - PROCID: 6
      AREAID: '0.0.0.5'
      IFNAME: 'LoopBack2'
    mod_ospfimportroute_list_1:
    - PROCID: 601
      TOPOID: 0
      PROTOCOL: wlr
      IMPTCOSTCFG: TRUE
      COST: 200
      PERMITIBGPCFG: ''
      PROTOCOLPROCID: ''
    set_redunduser_list_1:
    - SWITCH: ENABLE
    set_apnredundupsw_list:
    - APN: 'test'
      IPV4SWITCH: ENABLE
      IPV6SWITCH: ENABLE
    set_apnredundupsw_list_1:
    - APN: 'apn1'
      IPV4SWITCH: DISABLE
      IPV6SWITCH: DISABLE
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 配置主用UDG静态地址用户路由冗余功能。

#### 1.1 如果用户为静态IP地址用户或RADIUS分配地址用户，执行以下配置。

##### 1.1.1 配置EXTERNAL类型地址池。

```jinja2
{%- for item in add_pool_list -%}
    ADD POOL:
    {#- --- 必选参数 --- -#}
    POOLNAME="{{item.POOLNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.POOLTYPE is not none -%}
        POOLTYPE={{item.POOLTYPE}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：HASVPN=ENABLE 时必选 --- -#}
    {%- if item.HASVPN == 'ENABLE' -%}
        VPNINSTANCE="{{item.VPNINSTANCE}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：POOLTYPE=LOCAL/EXTERNAL 时可选 --- -#}
    {%- if item.POOLTYPE in ['LOCAL', 'EXTERNAL'] -%}
        {%- if item.IPVERSION is not none -%}
            IPVERSION={{item.IPVERSION}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：POOLTYPE=LOCAL/EXTERNAL 时可选 --- -#}
    {%- if item.POOLTYPE in ['LOCAL', 'EXTERNAL'] -%}
        {%- if item.HASVPN is not none -%}
            HASVPN={{item.HASVPN}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：POOLTYPE=EXTERNAL 时可选 --- -#}
    {%- if item.POOLTYPE == 'EXTERNAL' -%}
        {%- if item.REDUNDFUNC is not none -%}
            REDUNDFUNC={{item.REDUNDFUNC}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：POOLTYPE=LOCAL 时可选 --- -#}
    {%- if item.POOLTYPE == 'LOCAL' -%}
        {%- if item.ALARMSWITCH is not none -%}
            ALARMSWITCH={{item.ALARMSWITCH}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：POOLTYPE=EXTERNAL 时可选 --- -#}
    {%- if item.POOLTYPE == 'EXTERNAL' -%}
        {%- if item.CHECKIPVALID is not none -%}
            CHECKIPVALID={{item.CHECKIPVALID}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：POOLTYPE=LOCAL/EXTERNAL 时可选 --- -#}
    {%- if item.POOLTYPE in ['LOCAL', 'EXTERNAL'] -%}
        {%- if item.IMSSW is not none -%}
            IMSSW={{item.IMSSW}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：POOLTYPE=LOCAL 时可选 --- -#}
    {%- if item.POOLTYPE == 'LOCAL' -%}
        {%- if item.IPLEASE is not none -%}
            IPLEASE={{item.IPLEASE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：REDUNDFUNC=ENABLE 时可选 --- -#}
    {%- if item.REDUNDFUNC == 'ENABLE' -%}
        {%- if item.MASTERFLAG is not none -%}
            MASTERFLAG={{item.MASTERFLAG}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：POOLTYPE=LOCAL 时可选 --- -#}
    {%- if item.POOLTYPE == 'LOCAL' -%}
        {%- if item.RELEASETIME is not none -%}
            RELEASETIME={{item.RELEASETIME}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：POOLTYPE=LOCAL 时可选 --- -#}
    {%- if item.POOLTYPE == 'LOCAL' -%}
        {%- if item.SINGLEIPFLAG is not none -%}
            SINGLEIPFLAG={{item.SINGLEIPFLAG}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

##### 主备UPF是针对地址池发布的路由优先级而定的，地址池发布的路由优先级高，所在的UPF就是主UPF。

##### 当使能上行转发功能，且需要具备UE互访能力时，需在主UPF上将MASTERFLAG配置为ENABLE。

##### 1.1.2 配置静态地址池的地址段。

###### 1.1.2.1 配置IPV4地址段。

```jinja2
{%- for item in add_section_list -%}
    ADD SECTION:
    {#- --- 必选参数 --- -#}
    POOLNAME="{{item.POOLNAME}}",
    SECTIONNUM={{item.SECTIONNUM}},
    IPVERSION={{item.IPVERSION}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPVERSION=IPV4 时必选 --- -#}
    {%- if item.IPVERSION == 'IPV4' -%}
        V4STARTIP="{{item.V4STARTIP}}",
    {%- endif -%}
    {#- --- 条件必选：IPVERSION=IPV4 时必选 --- -#}
    {%- if item.IPVERSION == 'IPV4' -%}
        V4ENDIP="{{item.V4ENDIP}}",
    {%- endif -%}
    {#- --- 条件必选：IPVERSION=IPV6 时必选 --- -#}
    {%- if item.IPVERSION == 'IPV6' -%}
        V6PREFIXEND="{{item.V6PREFIXEND}}",
    {%- endif -%}
    {#- --- 条件必选：IPVERSION=IPV6 时必选 --- -#}
    {%- if item.IPVERSION == 'IPV6' -%}
        V6PREFIXLENGTH={{item.V6PREFIXLENGTH}},
    {%- endif -%}
    {#- --- 条件必选：IPVERSION=IPV6 时必选 --- -#}
    {%- if item.IPVERSION == 'IPV6' -%}
        V6PREFIXSTART="{{item.V6PREFIXSTART}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

###### 1.1.2.2 配置IPV6地址段。

```jinja2
{%- for item in add_section_list_1 -%}
    ADD SECTION:
    {#- --- 必选参数 --- -#}
    POOLNAME="{{item.POOLNAME}}",
    SECTIONNUM={{item.SECTIONNUM}},
    IPVERSION={{item.IPVERSION}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPVERSION=IPV6 时必选 --- -#}
    {%- if item.IPVERSION == 'IPV6' -%}
        V6PREFIXSTART="{{item.V6PREFIXSTART}}",
    {%- endif -%}
    {#- --- 条件必选：IPVERSION=IPV6 时必选 --- -#}
    {%- if item.IPVERSION == 'IPV6' -%}
        V6PREFIXEND="{{item.V6PREFIXEND}}",
    {%- endif -%}
    {#- --- 条件必选：IPVERSION=IPV6 时必选 --- -#}
    {%- if item.IPVERSION == 'IPV6' -%}
        V6PREFIXLENGTH={{item.V6PREFIXLENGTH}},
    {%- endif -%}
    {#- --- 条件必选：IPVERSION=IPV4 时必选 --- -#}
    {%- if item.IPVERSION == 'IPV4' -%}
        V4ENDIP="{{item.V4ENDIP}}",
    {%- endif -%}
    {#- --- 条件必选：IPVERSION=IPV4 时必选 --- -#}
    {%- if item.IPVERSION == 'IPV4' -%}
        V4STARTIP="{{item.V4STARTIP}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

##### 静态地址池下需要配置地址段，一个静态地址池最多可以配置64个地址段。

##### 配置地址池后，必须配置地址段。如果不配置地址段，将导致用户激活失败。

##### 静态地址池在配置时，建议尽量使用完整的网段地址。

##### 1.1.3 配置地址池组。

```jinja2
{%- for item in add_poolgroup_list -%}
    ADD POOLGROUP:
    {#- --- 必选参数 --- -#}
    POOLGRPNAME="{{item.POOLGRPNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.IPV4ALLOCPRIALG is not none -%}
        IPV4ALLOCPRIALG={{item.IPV4ALLOCPRIALG}},
    {%- endif -%}
    ;
{%- endfor -%}
```

##### 1.1.4 将地址池绑定地址池组。

```jinja2
{%- for item in add_poolbindgroup_list -%}
    ADD POOLBINDGROUP:
    {#- --- 必选参数 --- -#}
    POOLGROUPNAME="{{item.POOLGROUPNAME}}",
    POOLNAME="{{item.POOLNAME}}",
    ;
{%- endfor -%}
```

##### 1.1.5 配置APN名称。

```jinja2
{%- for item in add_apn_list -%}
    ADD APN:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    {#- --- 可选参数 --- -#}
    {%- if item.HASVPN is not none -%}
        HASVPN={{item.HASVPN}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：HASVPN=ENABLE 时必选 --- -#}
    {%- if item.HASVPN == 'ENABLE' -%}
        VPNINSTANCE="{{item.VPNINSTANCE}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

##### 1.1.6 配置地址池组与APN的映射关系。

```jinja2
{%- for item in add_poolgrpmap_list -%}
    ADD POOLGRPMAP:
    {#- --- 必选参数 --- -#}
    MAPPINGNAME="{{item.MAPPINGNAME}}",
    POOLGROUPNAME="{{item.POOLGROUPNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.APN is not none -%}
        APN="{{item.APN}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 1.2 配置冗余备份重定向IP，将业务流重定向到GRE Tunnel。

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
    {%- if item.IFMTU is not none -%}
        IFMTU={{item.IFMTU}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 1.4 将LoopBack接口绑定VPN实例。Loopback接口和Tunnel接口绑定的VPN实例不同，完成物理和业务上的划分。

```jinja2
{%- for item in add_ipbindvpn_list -%}
    ADD IPBINDVPN:
    {#- --- 必选参数 --- -#}
    IFNAME="{{item.IFNAME}}",
    VRFNAME="{{item.VRFNAME}}",
    ;
{%- endfor -%}
```

#### 1.5 配置GRE Tunnel接口。

```jinja2
{%- for item in add_interface_list_1 -%}
    ADD INTERFACE:
    {#- --- 必选参数 --- -#}
    IFNAME="{{item.IFNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.IFMTU is not none -%}
        IFMTU={{item.IFMTU}},
    {%- endif -%}
    {%- if item.IFADMINSTATUS is not none -%}
        IFADMINSTATUS={{item.IFADMINSTATUS}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 针对IPv4生效，MTU配置原则：封装GRE隧道出外联口不会再次分片。

#### 1.6 配置备份GRE Tunnel。

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
    {#- --- 条件必选：SRCTYPE=ip_address 时必选 --- -#}
    {%- if item.SRCTYPE == 'ip_address' -%}
        SRCIPADDR="{{item.SRCIPADDR}}",
    {%- endif -%}
    {#- --- 条件必选：TNLTYPE=gre6 时必选 --- -#}
    {%- if item.TNLTYPE == 'gre6' -%}
        SRCTYPE6={{item.SRCTYPE6}},
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
    {#- --- 条件可选：TNLTYPE=gre6 时可选 --- -#}
    {%- if item.TNLTYPE == 'gre6' -%}
        {%- if item.DSTIPV6ADDR is not none -%}
            DSTIPV6ADDR="{{item.DSTIPV6ADDR}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：KEEPALVEN=TRUE 时可选 --- -#}
    {%- if item.KEEPALVEN == 'TRUE' -%}
        {%- if item.KEEPALVPERIOD is not none -%}
            KEEPALVPERIOD={{item.KEEPALVPERIOD}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：KEEPALVEN=TRUE 时可选 --- -#}
    {%- if item.KEEPALVEN == 'TRUE' -%}
        {%- if item.KEEPALVRETRYCNT is not none -%}
            KEEPALVRETRYCNT={{item.KEEPALVRETRYCNT}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 1.7 将Tunnel接口绑定VPN实例。

```jinja2
{%- for item in add_ipbindvpn_list_1 -%}
    ADD IPBINDVPN:
    {#- --- 必选参数 --- -#}
    IFNAME="{{item.IFNAME}}",
    VRFNAME="{{item.VRFNAME}}",
    ;
{%- endfor -%}
```

#### 1.8 配置逻辑接口的IP地址。

##### 1.8.1 配置IPV4地址。

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

##### 1.8.2 配置IPV6地址。

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
    {#- --- 条件可选：ENABLEFLAG=TRUE 时可选 --- -#}
    {%- if item.ENABLEFLAG == 'TRUE' -%}
        {%- if item.AUTOLINKLOCAL is not none -%}
            AUTOLINKLOCAL={{item.AUTOLINKLOCAL}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

##### 针对IPv6生效，MTU配置原则：封装GRE隧道出外联口不会再次分片。

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

#### 1.9 配置IPv4静态路由。

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

#### 1.10 配置IPv6静态路由。

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

#### 1.11 （可选）配置下行缺省低优先级静态地址用户网段路由入冗余GRE隧道。

```jinja2
{%- if is_optional_downlink_default_route -%}
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
{%- if is_optional_downlink_default_route -%}
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
        {%- if item.PREFERENCE is not none -%}
            PREFERENCE={{item.PREFERENCE}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 1.12 主备LoopBack接口的路由需要打通，当使用OSPF路由时，可以使用**ADD OSPFINTERFACE**或**ADD OSPFNETWORK**命令打通路由，静态路由或BGP请按照对应配置增加，具体路由方式对应的配置命令可以参见“初始配置”中的“组网路由配置”。

```jinja2
{%- for item in add_ospfinterface_list -%}
    ADD OSPFINTERFACE:
    {#- --- 必选参数 --- -#}
    PROCID={{item.PROCID}},
    AREAID="{{item.AREAID}}",
    IFNAME="{{item.IFNAME}}",
    ;
{%- endfor -%}
```

#### 1.13 对于N6口路由，要检查路由发布优先级，主UPF优先级要高于备UPF优先级。

```jinja2
{%- for item in mod_ospfimportroute_list -%}
    MOD OSPFIMPORTROUTE:
    {#- --- 必选参数 --- -#}
    PROCID={{item.PROCID}},
    TOPOID={{item.TOPOID}},
    PROTOCOL={{item.PROTOCOL}},
    {#- --- 可选参数 --- -#}
    {%- if item.IMPTCOSTCFG is not none -%}
        IMPTCOSTCFG={{item.IMPTCOSTCFG}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IMPTCOSTCFG=TRUE 时必选 --- -#}
    {%- if item.IMPTCOSTCFG == 'TRUE' -%}
        COST={{item.COST}},
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
```

```jinja2
{%- for item in mod_importroute_list -%}
    MOD IMPORTROUTE:
    {#- --- 必选参数 --- -#}
    AFTYPE={{item.AFTYPE}},
    IMPORTPROTOCOL={{item.IMPORTPROTOCOL}},
    VRFNAME="{{item.VRFNAME}}",
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IMPORTPROTOCOL=ospf/ospfv3 时必选 --- -#}
    {%- if item.IMPORTPROTOCOL in ['ospf', 'ospfv3'] -%}
        IMPORTPROCESSID={{item.IMPORTPROCESSID}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 1.14 配置使能静态地址用户路由冗余功能。

```jinja2
{%- for item in set_redunduser_list -%}
    SET REDUNDUSER:
    {#- --- 必选参数 --- -#}
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

### 2 配置备用UDG静态地址用户路由冗余功能。

#### 2.1 重复主用UDG配置步骤 1。

#### 主备UDG的VPN实例配置可以一致也可以不一致，因为主备UDG的地址池完全相同，因此可以绑定相同的VPN实例；同时，主备UDG是两个设备，两者配置互不影响，也可配置为不同的VPN。

#### 下行缺省低优先级静态地址用户网段路由入冗余GRE隧道仅在主用UDG配置。

```jinja2
{%- for item in add_pool_list_2 -%}
    ADD POOL:
    {#- --- 必选参数 --- -#}
    POOLNAME="{{item.POOLNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.POOLTYPE is not none -%}
        POOLTYPE={{item.POOLTYPE}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：HASVPN=ENABLE 时必选 --- -#}
    {%- if item.HASVPN == 'ENABLE' -%}
        VPNINSTANCE="{{item.VPNINSTANCE}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：POOLTYPE=LOCAL/EXTERNAL 时可选 --- -#}
    {%- if item.POOLTYPE in ['LOCAL', 'EXTERNAL'] -%}
        {%- if item.IPVERSION is not none -%}
            IPVERSION={{item.IPVERSION}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：POOLTYPE=LOCAL/EXTERNAL 时可选 --- -#}
    {%- if item.POOLTYPE in ['LOCAL', 'EXTERNAL'] -%}
        {%- if item.HASVPN is not none -%}
            HASVPN={{item.HASVPN}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：POOLTYPE=EXTERNAL 时可选 --- -#}
    {%- if item.POOLTYPE == 'EXTERNAL' -%}
        {%- if item.REDUNDFUNC is not none -%}
            REDUNDFUNC={{item.REDUNDFUNC}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：POOLTYPE=LOCAL 时可选 --- -#}
    {%- if item.POOLTYPE == 'LOCAL' -%}
        {%- if item.ALARMSWITCH is not none -%}
            ALARMSWITCH={{item.ALARMSWITCH}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：POOLTYPE=EXTERNAL 时可选 --- -#}
    {%- if item.POOLTYPE == 'EXTERNAL' -%}
        {%- if item.CHECKIPVALID is not none -%}
            CHECKIPVALID={{item.CHECKIPVALID}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：POOLTYPE=LOCAL/EXTERNAL 时可选 --- -#}
    {%- if item.POOLTYPE in ['LOCAL', 'EXTERNAL'] -%}
        {%- if item.IMSSW is not none -%}
            IMSSW={{item.IMSSW}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：POOLTYPE=LOCAL 时可选 --- -#}
    {%- if item.POOLTYPE == 'LOCAL' -%}
        {%- if item.IPLEASE is not none -%}
            IPLEASE={{item.IPLEASE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：REDUNDFUNC=ENABLE 时可选 --- -#}
    {%- if item.REDUNDFUNC == 'ENABLE' -%}
        {%- if item.MASTERFLAG is not none -%}
            MASTERFLAG={{item.MASTERFLAG}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：POOLTYPE=LOCAL 时可选 --- -#}
    {%- if item.POOLTYPE == 'LOCAL' -%}
        {%- if item.RELEASETIME is not none -%}
            RELEASETIME={{item.RELEASETIME}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：POOLTYPE=LOCAL 时可选 --- -#}
    {%- if item.POOLTYPE == 'LOCAL' -%}
        {%- if item.SINGLEIPFLAG is not none -%}
            SINGLEIPFLAG={{item.SINGLEIPFLAG}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_section_list_2 -%}
    ADD SECTION:
    {#- --- 必选参数 --- -#}
    POOLNAME="{{item.POOLNAME}}",
    SECTIONNUM={{item.SECTIONNUM}},
    IPVERSION={{item.IPVERSION}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPVERSION=IPV4 时必选 --- -#}
    {%- if item.IPVERSION == 'IPV4' -%}
        V4STARTIP="{{item.V4STARTIP}}",
    {%- endif -%}
    {#- --- 条件必选：IPVERSION=IPV4 时必选 --- -#}
    {%- if item.IPVERSION == 'IPV4' -%}
        V4ENDIP="{{item.V4ENDIP}}",
    {%- endif -%}
    {#- --- 条件必选：IPVERSION=IPV6 时必选 --- -#}
    {%- if item.IPVERSION == 'IPV6' -%}
        V6PREFIXSTART="{{item.V6PREFIXSTART}}",
    {%- endif -%}
    {#- --- 条件必选：IPVERSION=IPV6 时必选 --- -#}
    {%- if item.IPVERSION == 'IPV6' -%}
        V6PREFIXEND="{{item.V6PREFIXEND}}",
    {%- endif -%}
    {#- --- 条件必选：IPVERSION=IPV6 时必选 --- -#}
    {%- if item.IPVERSION == 'IPV6' -%}
        V6PREFIXLENGTH={{item.V6PREFIXLENGTH}},
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_poolgroup_list_1 -%}
    ADD POOLGROUP:
    {#- --- 必选参数 --- -#}
    POOLGRPNAME="{{item.POOLGRPNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.IPV4ALLOCPRIALG is not none -%}
        IPV4ALLOCPRIALG={{item.IPV4ALLOCPRIALG}},
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_poolbindgroup_list_2 -%}
    ADD POOLBINDGROUP:
    {#- --- 必选参数 --- -#}
    POOLGROUPNAME="{{item.POOLGROUPNAME}}",
    POOLNAME="{{item.POOLNAME}}",
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_apn_list_1 -%}
    ADD APN:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    {#- --- 可选参数 --- -#}
    {%- if item.HASVPN is not none -%}
        HASVPN={{item.HASVPN}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：HASVPN=ENABLE 时必选 --- -#}
    {%- if item.HASVPN == 'ENABLE' -%}
        VPNINSTANCE="{{item.VPNINSTANCE}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_poolgrpmap_list_1 -%}
    ADD POOLGRPMAP:
    {#- --- 必选参数 --- -#}
    MAPPINGNAME="{{item.MAPPINGNAME}}",
    POOLGROUPNAME="{{item.POOLGROUPNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.APN is not none -%}
        APN="{{item.APN}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

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

```jinja2
{%- for item in add_interface_list_2 -%}
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

```jinja2
{%- for item in add_interface_list_3 -%}
    ADD INTERFACE:
    {#- --- 必选参数 --- -#}
    IFNAME="{{item.IFNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.IFMTU is not none -%}
        IFMTU={{item.IFMTU}},
    {%- endif -%}
    {%- if item.IFADMINSTATUS is not none -%}
        IFADMINSTATUS={{item.IFADMINSTATUS}},
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
    {#- --- 条件必选：SRCTYPE=ip_address 时必选 --- -#}
    {%- if item.SRCTYPE == 'ip_address' -%}
        SRCIPADDR="{{item.SRCIPADDR}}",
    {%- endif -%}
    {#- --- 条件必选：TNLTYPE=gre6 时必选 --- -#}
    {%- if item.TNLTYPE == 'gre6' -%}
        SRCTYPE6={{item.SRCTYPE6}},
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
    {#- --- 条件可选：TNLTYPE=gre6 时可选 --- -#}
    {%- if item.TNLTYPE == 'gre6' -%}
        {%- if item.DSTIPV6ADDR is not none -%}
            DSTIPV6ADDR="{{item.DSTIPV6ADDR}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：KEEPALVEN=TRUE 时可选 --- -#}
    {%- if item.KEEPALVEN == 'TRUE' -%}
        {%- if item.KEEPALVPERIOD is not none -%}
            KEEPALVPERIOD={{item.KEEPALVPERIOD}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：KEEPALVEN=TRUE 时可选 --- -#}
    {%- if item.KEEPALVEN == 'TRUE' -%}
        {%- if item.KEEPALVRETRYCNT is not none -%}
            KEEPALVRETRYCNT={{item.KEEPALVRETRYCNT}},
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
    {#- --- 条件可选：ENABLEFLAG=TRUE 时可选 --- -#}
    {%- if item.ENABLEFLAG == 'TRUE' -%}
        {%- if item.AUTOLINKLOCAL is not none -%}
            AUTOLINKLOCAL={{item.AUTOLINKLOCAL}},
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

```jinja2
{%- for item in add_ospfinterface_list_1 -%}
    ADD OSPFINTERFACE:
    {#- --- 必选参数 --- -#}
    PROCID={{item.PROCID}},
    AREAID="{{item.AREAID}}",
    IFNAME="{{item.IFNAME}}",
    ;
{%- endfor -%}
```

```jinja2
{%- for item in mod_ospfimportroute_list_1 -%}
    MOD OSPFIMPORTROUTE:
    {#- --- 必选参数 --- -#}
    PROCID={{item.PROCID}},
    TOPOID={{item.TOPOID}},
    PROTOCOL={{item.PROTOCOL}},
    {#- --- 可选参数 --- -#}
    {%- if item.IMPTCOSTCFG is not none -%}
        IMPTCOSTCFG={{item.IMPTCOSTCFG}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IMPTCOSTCFG=TRUE 时必选 --- -#}
    {%- if item.IMPTCOSTCFG == 'TRUE' -%}
        COST={{item.COST}},
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
```

```jinja2
{%- for item in set_redunduser_list_1 -%}
    SET REDUNDUSER:
    {#- --- 必选参数 --- -#}
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

#### 2.2 配置使能IPv4/IPv6上行报文隧道转发功能。

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

#### 使能IPv4/IPv6上行报文隧道转发功能仅在备UPF上配置。

### 3 在静态地址路由冗余叠加UE互访场景下，需要做如下操作：

#### 3.1 使用**SET APNREDUNDUPSW**命令关闭备UPF上的“路由冗余上行报文隧道转发”开关。

```jinja2
{%- if is_scenario_ue_interaccess -%}
    {%- for item in set_apnredundupsw_list_1 -%}
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
{%- endif -%}
```

#### 3.2 如果两个UPF的N6侧对接不同对防火墙，则需在防火墙上需关闭上/下行报文的单通状态监测。


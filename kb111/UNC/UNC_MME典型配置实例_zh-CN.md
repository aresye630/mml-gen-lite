---
id: ''
name: MME典型配置实例
ne_type: UNC
type: feature
description: 本任务实例实现以下场景配置：UNC通过IP骨干网与eNodeB、HSS、S-GW、P-GW、DNS互通。UNC到eNodeB、HSS和S-GW都采用了双平面+VRF+OSPF动态路由+BFD的组网方式，其中UNC到eNodeB采用SCTP非多归属，UNC到HSS采用SCTP双归属。  **图1** 典型组网图
risk_level: ''
doc_source: ["网络部署","初始配置","UNC初始配置与调测","典型配置实例","MME典型配置实例"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本任务实例实现以下场景配置：UNC通过IP骨干网与eNodeB、HSS、S-GW、P-GW、DNS互通。UNC到eNodeB、HSS和S-GW都采用了双平面+VRF+OSPF动态路由+BFD的组网方式，其中UNC到eNodeB采用SCTP非多归属，UNC到HSS采用SCTP双归属。**图1** 典型组网图

## 必备事项
前提条件

* 请了解UNC各类接口的类型及命名规范，可参见业务组网与逻辑接口介绍。
* 基础数据配置、IP路由组网和业务接口配置子任务在前述章节已有详细描述，可参见基础数据配置、配置VNF侧IP路由数据（非SDN）和配置MME。本文针对典型的任务场景举例说明整网脚本配置。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    add_hplmn_list:
      type: items
      properties:
        MCC:
          name: '移动国家码'
          type: string
          maxLength: 3
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MNC:
          name: '移动网号'
          type: string
          maxLength: 3
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CC:
          name: '国家码'
          type: string
          maxLength: 6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        S5S8TYPE:
          name: '协议类型'
          type: string
          enum:
          - GTP
          - PMIP
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: GTP
    add_mmeid_list:
      type: items
      properties:
        MCC:
          name: '移动国家码'
          type: string
          maxLength: 3
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MNC:
          name: '移动网号'
          type: string
          maxLength: 3
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MMEGI:
          name: 'MME组识别码'
          type: string
          maxLength: 4
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MMEC:
          name: 'MME编码（起始值）'
          type: string
          maxLength: 2
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_sys_list:
      type: items
      properties:
        CAP:
          name: '设备能力'
          type: integer
          minimum: 0
          maximum: 255
          required: false
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
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VRFDESCRIPTION:
          name: 'VPN实例描述'
          type: string
          maxLength: 242
          required: false
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
        IFMTU:
          name: '接口最大传输单元（byte）'
          type: integer
          minimum: 46
          maximum: 9600
          required: false
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
          default: ''
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
        IFSTATITVL:
          name: '接口统计时间间隔（s）'
          type: integer
          minimum: 5
          maximum: 600
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
        IFMTU:
          name: '接口最大传输单元（byte）'
          type: integer
          minimum: 46
          maximum: 9600
          required: false
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
        IFSTATITVL:
          name: '接口统计时间间隔（s）'
          type: integer
          minimum: 5
          maximum: 600
          required: false
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
        SILENTALLFLAG:
          name: '抑制接口收发OSPF报文'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
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
        RFC1583COMPFLG:
          name: '兼容RFC1583'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: TRUE
        ROUTAGFLAG:
          name: '配置VPN引入路由的tag值'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        BANDWIDTHREF:
          name: '计算链路开销参考值（Mbps）'
          type: integer
          minimum: 1
          maximum: 2147483648
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 100
        RXMTLIMITENABLE:
          name: '使能最大重传数'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        OPAQCAPFLG:
          name: 'Opaque LSA能力'
          type: string
          enum:
          - FALSE
          - TRUE
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
        LSAORIGINSTFLAG:
          name: '是否指定LSA更新的时间间隔为0'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        LSAORIGINTV:
          name: '更新时间间隔（s）'
          type: integer
          minimum: 0
          maximum: 10
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 5
        LSAORIGMAXINTV:
          name: '更新最长间隔时间（ms）'
          type: integer
          minimum: 1
          maximum: 10000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 5000
        LSAORIGSTARINTV:
          name: '更新初始间隔时间（ms）'
          type: integer
          minimum: 0
          maximum: 1000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 500
        LSAORIGHLDINTV:
          name: '更新基数间隔时间（ms）'
          type: integer
          minimum: 1
          maximum: 5000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 1000
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
        STUBROUFLG:
          name: 'Stub路由器'
          type: string
          enum:
          - NoConfig
          - StubOnBoot
          - StubOnHand
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NoConfig
        SAFESYNCFLG:
          name: '安全同步'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        RTTAGDISFLAG:
          name: '禁止使用tag检测环路'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        ECAROUTEFLAG:
          name: '使能ECA路由类型'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        DOMAINNULLFLAG:
          name: '配置Domain ID为空'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        SUPPREACH:
          name: '使能可达性抑制'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        SPFCONSERVFLAG:
          name: 'SPF正常模式标志'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        SHAMHELLOFLAG:
          name: '使能Sham-hello'
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
          name: '是否自动使能MPLS LDP功能'
          type: string
          enum:
          - Enable
          - None
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: None
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
        ROUTAG:
          name: 'VPN引入路由的tag值'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RETRANSLIMIT:
          name: '最大重传限制'
          type: integer
          minimum: 2
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 30
        STUBROUINCSTUB:
          name: '是否为Stub链路发布最大开销值'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        STUBROUSTUPINTV:
          name: 'On-Startup时间间隔（s）'
          type: integer
          minimum: 5
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 500
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
        TOSEXP:
          name: '动态BFD会话报文优先级'
          type: integer
          minimum: 0
          maximum: 7
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
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
        TIMERCONSERFLAG:
          name: '是否使能邻居失效定时器保守模式'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        CONFIGCOST:
          name: '接口开销值'
          type: integer
          minimum: 0
          maximum: 65535
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
    add_serviceip_list:
      type: items
      properties:
        IPVERSION:
          name: 'IP版本'
          type: string
          enum:
          - IPv4
          - IPv6
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: IPv4
        SERVICEIPV4:
          name: '业务IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VPNINSTNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DESC:
          name: '描述'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6MTU:
          name: 'IPv6 MTU大小'
          type: integer
          minimum: 1280
          maximum: 65534
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 1500
        SERVICEIPV6:
          name: '业务IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_sctppara_list:
      type: items
      properties:
        SCTPPARAINDEX:
          name: 'SCTP协议参数索引'
          type: integer
          minimum: 0
          maximum: 65534
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RTOMIN:
          name: 'RTO最小值（ms）'
          type: integer
          minimum: 10
          maximum: 1000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 500
        RTOMAX:
          name: 'RTO最大值（ms）'
          type: integer
          minimum: 20
          maximum: 60000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 1500
        RTOINIT:
          name: 'RTO初始值（ms）'
          type: integer
          minimum: 10
          maximum: 60000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 500
        RTOALPHA:
          name: 'RTO ALPHA值（%）'
          type: integer
          minimum: 1
          maximum: 100
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 12
        RTOBETA:
          name: 'RTO BETA值（%）'
          type: integer
          minimum: 1
          maximum: 100
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 25
        HBINTERVAL:
          name: '心跳间隔（ms）'
          type: integer
          minimum: 10
          maximum: 60000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 3000
        MAXASSOCRETR:
          name: '偶联最大重发次数'
          type: integer
          minimum: 1
          maximum: 254
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 5
        MAXPATHRETR:
          name: '路径最大重发次数'
          type: integer
          minimum: 1
          maximum: 254
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 4
        MAXINSTREAMS:
          name: '最大入流个数'
          type: integer
          minimum: 2
          maximum: 17
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 17
        MAXOUTSTREAMS:
          name: '最大出流个数'
          type: integer
          minimum: 2
          maximum: 17
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 17
        CNGLEVELNO:
          name: '拥塞结束门限'
          type: integer
          minimum: 1
          maximum: 100
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 40
        CNGLEVELLOW:
          name: '拥塞最低门限'
          type: integer
          minimum: 1
          maximum: 100
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 60
        CNGLEVELHIGH:
          name: '拥塞最高门限'
          type: integer
          minimum: 1
          maximum: 100
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 80
        CHKSUMTX:
          name: '发送消息时是否计算校验和'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: YES
        CHKSUMRX:
          name: '接收消息时是否计算校验和'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: YES
        CHKSUMTYPE:
          name: '校验和算法类型'
          type: string
          enum:
          - ADLER32
          - CRC32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: CRC32
        BINDTMR:
          name: '绑定定时器时长（ms）'
          type: integer
          minimum: 10
          maximum: 200
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 10
        DELAYTMRLEN:
          name: '延迟定时器时长（ms）'
          type: integer
          minimum: 10
          maximum: 500
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 200
        IPV4MTU:
          name: 'IPv4 MTU大小'
          type: integer
          minimum: 96
          maximum: 65534
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 1500
        IPV6MTU:
          name: 'IPv6 MTU大小'
          type: integer
          minimum: 1280
          maximum: 65534
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 1500
        SCTPPARANAME:
          name: 'SCTP协议参数名'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'noname'
        PKGERRFAULT:
          name: '错包率故障门限'
          type: integer
          minimum: 1
          maximum: 100
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 5
        PKGERRRECOVER:
          name: '错包率恢复门限'
          type: integer
          minimum: 1
          maximum: 100
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 3
        MINRECVPKGNUM:
          name: '单偶联最小收包数'
          type: integer
          minimum: 10
          maximum: 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 100
    add_dmle_list:
      type: items
      properties:
        LOINDEX:
          name: '本地实体索引'
          type: integer
          minimum: 0
          maximum: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 0
        LOHSTNAME:
          name: '本地实体主机名'
          type: string
          maxLength: 127
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LORLMNAME:
          name: '本地实体域名'
          type: string
          maxLength: 127
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PDTNAME:
          name: '产品名'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'vUSN'
        LOINFONAME:
          name: '本地实体名'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_dmpe_list:
      type: items
      properties:
        PEERIDX:
          name: '对端实体索引'
          type: integer
          minimum: 0
          maximum: 639
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PEERHTNAM:
          name: '对端主机名'
          type: string
          maxLength: 127
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PEERNAM:
          name: '对端实体名'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        APPCAP:
          name: '节点支持的应用'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CONGSW:
          name: '对端拥塞避免开关'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: OFF
    add_dmlks_list:
      type: items
      properties:
        LINKSIDX:
          name: 'Diameter链路集索引'
          type: integer
          minimum: 0
          maximum: 639
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LOCALIDX:
          name: '本地实体索引'
          type: integer
          minimum: 0
          maximum: 31
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PEERIDX:
          name: '对端实体索引'
          type: integer
          minimum: 0
          maximum: 639
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LSSELMODE:
          name: '选路模式'
          type: string
          enum:
          - SELMODE_ACTIVE
          - SELMODE_LOAD_BALAN
          - SELMODE_MASTER_SLAVE
          - SELMODE_ROUND_ROBIN
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: SELMODE_LOAD_BALAN
        LINKSNAM:
          name: '链路集名称'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'noname'
    add_dmlnk_list:
      type: items
      properties:
        VPNNAME:
          name: 'vpn名称'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LINKIDX:
          name: '链路索引'
          type: integer
          minimum: 0
          maximum: 1279
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPTYPE:
          name: 'IP地址类型'
          type: string
          enum:
          - TPTADDR_TYPE_IPV4
          - TPTADDR_TYPE_IPV6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: TPTADDR_TYPE_IPV4
        PROTOTYPE:
          name: '协议类型'
          type: string
          enum:
          - CONN_PROTOCOL_SCTP
          - CONN_PROTOCOL_TCP
          - CONN_PROTOCOL_UDP
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: CONN_PROTOCOL_SCTP
        LOCALIPV4_1:
          name: '本地IPv4地址1'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LOCALIPV4_2:
          name: '本地IPv4地址2'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LOCALPORT:
          name: '本地端口号'
          type: integer
          minimum: 1024
          maximum: 65534
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 3868
        PEERIPV4_1:
          name: '对端IPv4地址1'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PEERIPV4_2:
          name: '对端IPv4地址2'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PEERPORT:
          name: '对端端口号'
          type: integer
          minimum: 1
          maximum: 65534
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 3868
        CLIORSER:
          name: 'C/S模式'
          type: string
          enum:
          - DIAM_CONN_CLIENT
          - DIAM_CONN_SERVER
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DIAM_CONN_CLIENT
        LINKSIDX:
          name: 'Diameter链路集索引'
          type: integer
          minimum: 0
          maximum: 639
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SCTPINDX:
          name: 'SCTP协议参数索引'
          type: integer
          minimum: 0
          maximum: 65534
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LINKNAM:
          name: '链路名称'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'noname'
        CROSSIPFLAG:
          name: '交叉路径是否可用'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NO
        LOCALIPV6_1:
          name: '本地IPv6地址1'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LOCALIPV6_2:
          name: '本地IPv6地址2'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PEERIPV6_1:
          name: '对端IPv6地址1'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PEERIPV6_2:
          name: '对端IPv6地址2'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_dmhostrt_list:
      type: items
      properties:
        ROUTEIDX:
          name: '路由索引'
          type: integer
          minimum: 0
          maximum: 1023
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        APPNAM:
          name: '应用名称'
          type: string
          enum:
          - S13
          - S6A/S6D
          - SLG
          - T6A/T6AI/T6B/T6BI
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: S6A/S6D
        RSELMODE:
          name: '选路模式'
          type: string
          enum:
          - SELMODE_MASTER_SLAVE
          - SELMODE_PRIORITY_WEIGHT
          - SELMODE_ROUND_ROBIN
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: SELMODE_MASTER_SLAVE
        PEERSEL:
          name: '目的实体选择方式'
          type: string
          enum:
          - PEER_HOST_NAME
          - PEER_INDEX
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: PEER_INDEX
        PEERIDX:
          name: '对端实体索引'
          type: integer
          minimum: 0
          maximum: 639
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ROUTENAM:
          name: '路由名称'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PRIORITY:
          name: '优先级'
          type: integer
          minimum: 0
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PEERHTNAM:
          name: '对端主机名'
          type: string
          maxLength: 127
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        WEIGHT:
          name: '权重'
          type: integer
          minimum: 1
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 1
    add_dmrtgrp_list:
      type: items
      properties:
        GRPIDX:
          name: '路由组索引'
          type: integer
          minimum: 0
          maximum: 1023
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RTMODE:
          name: '路由模式'
          type: string
          enum:
          - HOST_ROUTE
          - REALM_ROUTE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: HOST_ROUTE
        RTPRIMODE:
          name: '路由优选模式'
          type: string
          enum:
          - HOST_ROUTE_PREFER
          - REALM_ROUTE_PREFER
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: HOST_ROUTE_PREFER
        ROUTEIDX:
          name: '路由索引'
          type: integer
          minimum: 0
          maximum: 2047
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ROUTEGRPNAM:
          name: '路由组名称'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'noname'
        PEERIDX:
          name: '对端实体索引'
          type: integer
          minimum: 0
          maximum: 639
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_imsihss_list:
      type: items
      properties:
        IMSIPRE:
          name: 'IMSI前缀'
          type: string
          maxLength: 15
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        HSSRLM:
          name: 'HSS域名'
          type: string
          maxLength: 127
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GRPIDX:
          name: 'Diameter路由组索引'
          type: integer
          minimum: 0
          maximum: 1023
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MNNAME:
          name: '移动网络名称'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'noname'
    add_l3vpninst_list_1:
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
    add_vpninstaf_list_1:
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
    mod_interface_list_4:
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
        IFMTU:
          name: '接口最大传输单元（byte）'
          type: integer
          minimum: 46
          maximum: 9600
          required: false
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
          default: ''
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
        IFSTATITVL:
          name: '接口统计时间间隔（s）'
          type: integer
          minimum: 5
          maximum: 600
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
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
        IFMTU:
          name: '接口最大传输单元（byte）'
          type: integer
          minimum: 46
          maximum: 9600
          required: false
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
        IFSTATITVL:
          name: '接口统计时间间隔（s）'
          type: integer
          minimum: 5
          maximum: 600
          required: false
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
        SILENTALLFLAG:
          name: '抑制接口收发OSPF报文'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
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
        RFC1583COMPFLG:
          name: '兼容RFC1583'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: TRUE
        ROUTAGFLAG:
          name: '配置VPN引入路由的tag值'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        BANDWIDTHREF:
          name: '计算链路开销参考值（Mbps）'
          type: integer
          minimum: 1
          maximum: 2147483648
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 100
        RXMTLIMITENABLE:
          name: '使能最大重传数'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        OPAQCAPFLG:
          name: 'Opaque LSA能力'
          type: string
          enum:
          - FALSE
          - TRUE
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
        LSAORIGINSTFLAG:
          name: '是否指定LSA更新的时间间隔为0'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        LSAORIGINTV:
          name: '更新时间间隔（s）'
          type: integer
          minimum: 0
          maximum: 10
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 5
        LSAORIGMAXINTV:
          name: '更新最长间隔时间（ms）'
          type: integer
          minimum: 1
          maximum: 10000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 5000
        LSAORIGSTARINTV:
          name: '更新初始间隔时间（ms）'
          type: integer
          minimum: 0
          maximum: 1000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 500
        LSAORIGHLDINTV:
          name: '更新基数间隔时间（ms）'
          type: integer
          minimum: 1
          maximum: 5000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 1000
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
        STUBROUFLG:
          name: 'Stub路由器'
          type: string
          enum:
          - NoConfig
          - StubOnBoot
          - StubOnHand
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NoConfig
        SAFESYNCFLG:
          name: '安全同步'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        RTTAGDISFLAG:
          name: '禁止使用tag检测环路'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        ECAROUTEFLAG:
          name: '使能ECA路由类型'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        DOMAINNULLFLAG:
          name: '配置Domain ID为空'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        SUPPREACH:
          name: '使能可达性抑制'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        SPFCONSERVFLAG:
          name: 'SPF正常模式标志'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        SHAMHELLOFLAG:
          name: '使能Sham-hello'
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
          name: '是否自动使能MPLS LDP功能'
          type: string
          enum:
          - Enable
          - None
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: None
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
        ROUTAG:
          name: 'VPN引入路由的tag值'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RETRANSLIMIT:
          name: '最大重传限制'
          type: integer
          minimum: 2
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 30
        STUBROUINCSTUB:
          name: '是否为Stub链路发布最大开销值'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        STUBROUSTUPINTV:
          name: 'On-Startup时间间隔（s）'
          type: integer
          minimum: 5
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 500
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
    add_ospfnetwork_list_3:
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
    add_ospfimportroute_list_1:
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
    add_ospfinterface_list_4:
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
        TIMERCONSERFLAG:
          name: '是否使能邻居失效定时器保守模式'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        CONFIGCOST:
          name: '接口开销值'
          type: integer
          minimum: 0
          maximum: 65535
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
    add_serviceip_list_2:
      type: items
      properties:
        IPVERSION:
          name: 'IP版本'
          type: string
          enum:
          - IPv4
          - IPv6
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: IPv4
        SERVICEIPV4:
          name: '业务IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VPNINSTNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DESC:
          name: '描述'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6MTU:
          name: 'IPv6 MTU大小'
          type: integer
          minimum: 1280
          maximum: 65534
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 1500
        SERVICEIPV6:
          name: '业务IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_sctppara_list_1:
      type: items
      properties:
        SCTPPARAINDEX:
          name: 'SCTP协议参数索引'
          type: integer
          minimum: 0
          maximum: 65534
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RTOMIN:
          name: 'RTO最小值（ms）'
          type: integer
          minimum: 10
          maximum: 1000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 500
        RTOMAX:
          name: 'RTO最大值（ms）'
          type: integer
          minimum: 20
          maximum: 60000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 1500
        RTOINIT:
          name: 'RTO初始值（ms）'
          type: integer
          minimum: 10
          maximum: 60000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 500
        RTOALPHA:
          name: 'RTO ALPHA值（%）'
          type: integer
          minimum: 1
          maximum: 100
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 12
        RTOBETA:
          name: 'RTO BETA值（%）'
          type: integer
          minimum: 1
          maximum: 100
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 25
        HBINTERVAL:
          name: '心跳间隔（ms）'
          type: integer
          minimum: 10
          maximum: 60000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 3000
        MAXASSOCRETR:
          name: '偶联最大重发次数'
          type: integer
          minimum: 1
          maximum: 254
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 5
        MAXPATHRETR:
          name: '路径最大重发次数'
          type: integer
          minimum: 1
          maximum: 254
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 4
        MAXINSTREAMS:
          name: '最大入流个数'
          type: integer
          minimum: 2
          maximum: 17
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 17
        MAXOUTSTREAMS:
          name: '最大出流个数'
          type: integer
          minimum: 2
          maximum: 17
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 17
        CNGLEVELNO:
          name: '拥塞结束门限'
          type: integer
          minimum: 1
          maximum: 100
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 40
        CNGLEVELLOW:
          name: '拥塞最低门限'
          type: integer
          minimum: 1
          maximum: 100
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 60
        CNGLEVELHIGH:
          name: '拥塞最高门限'
          type: integer
          minimum: 1
          maximum: 100
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 80
        CHKSUMTX:
          name: '发送消息时是否计算校验和'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: YES
        CHKSUMRX:
          name: '接收消息时是否计算校验和'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: YES
        CHKSUMTYPE:
          name: '校验和算法类型'
          type: string
          enum:
          - ADLER32
          - CRC32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: CRC32
        BINDTMR:
          name: '绑定定时器时长（ms）'
          type: integer
          minimum: 10
          maximum: 200
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 10
        DELAYTMRLEN:
          name: '延迟定时器时长（ms）'
          type: integer
          minimum: 10
          maximum: 500
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 200
        IPV4MTU:
          name: 'IPv4 MTU大小'
          type: integer
          minimum: 96
          maximum: 65534
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 1500
        IPV6MTU:
          name: 'IPv6 MTU大小'
          type: integer
          minimum: 1280
          maximum: 65534
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 1500
        SCTPPARANAME:
          name: 'SCTP协议参数名'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'noname'
        PKGERRFAULT:
          name: '错包率故障门限'
          type: integer
          minimum: 1
          maximum: 100
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 5
        PKGERRRECOVER:
          name: '错包率恢复门限'
          type: integer
          minimum: 1
          maximum: 100
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 3
        MINRECVPKGNUM:
          name: '单偶联最小收包数'
          type: integer
          minimum: 10
          maximum: 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 100
    add_s1aple_list:
      type: items
      properties:
        LLEINDEX:
          name: '链路本地实体号'
          type: integer
          minimum: 0
          maximum: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPTYPE:
          name: 'IP地址类型'
          type: string
          enum:
          - TPTADDR_TYPE_IPV4
          - TPTADDR_TYPE_IPV6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: TPTADDR_TYPE_IPV4
        LOCALIPV4_1:
          name: '本地IPv4地址1'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LOCALIPV4_2:
          name: '本地IPv4地址2'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LOCALPORT:
          name: '本地端口号'
          type: integer
          minimum: 1024
          maximum: 65534
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 36412
        CROSSIPFLAG:
          name: '交叉路径是否可用'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NO
        SCTPINDEX:
          name: 'SCTP协议参数索引'
          type: integer
          minimum: 0
          maximum: 65534
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LLNAME:
          name: '链路本地实体名'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VPNNAME:
          name: 'VPN名称'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LOCALIPV6_1:
          name: '本地IPv6地址1'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LOCALIPV6_2:
          name: '本地IPv6地址2'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_l3vpninst_list_2:
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
    add_vpninstaf_list_2:
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
    mod_interface_list_8:
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
        IFMTU:
          name: '接口最大传输单元（byte）'
          type: integer
          minimum: 46
          maximum: 9600
          required: false
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
          default: ''
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
        IFSTATITVL:
          name: '接口统计时间间隔（s）'
          type: integer
          minimum: 5
          maximum: 600
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
        IFMTU:
          name: '接口最大传输单元（byte）'
          type: integer
          minimum: 46
          maximum: 9600
          required: false
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
        IFSTATITVL:
          name: '接口统计时间间隔（s）'
          type: integer
          minimum: 5
          maximum: 600
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_ipbindvpn_list_10:
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
    add_ethsubif_list_8:
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
    add_ifipv4address_list_10:
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
        SILENTALLFLAG:
          name: '抑制接口收发OSPF报文'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
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
        RFC1583COMPFLG:
          name: '兼容RFC1583'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: TRUE
        ROUTAGFLAG:
          name: '配置VPN引入路由的tag值'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        BANDWIDTHREF:
          name: '计算链路开销参考值（Mbps）'
          type: integer
          minimum: 1
          maximum: 2147483648
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 100
        RXMTLIMITENABLE:
          name: '使能最大重传数'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        OPAQCAPFLG:
          name: 'Opaque LSA能力'
          type: string
          enum:
          - FALSE
          - TRUE
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
        LSAORIGINSTFLAG:
          name: '是否指定LSA更新的时间间隔为0'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        LSAORIGINTV:
          name: '更新时间间隔（s）'
          type: integer
          minimum: 0
          maximum: 10
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 5
        LSAORIGMAXINTV:
          name: '更新最长间隔时间（ms）'
          type: integer
          minimum: 1
          maximum: 10000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 5000
        LSAORIGSTARINTV:
          name: '更新初始间隔时间（ms）'
          type: integer
          minimum: 0
          maximum: 1000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 500
        LSAORIGHLDINTV:
          name: '更新基数间隔时间（ms）'
          type: integer
          minimum: 1
          maximum: 5000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 1000
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
        STUBROUFLG:
          name: 'Stub路由器'
          type: string
          enum:
          - NoConfig
          - StubOnBoot
          - StubOnHand
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NoConfig
        SAFESYNCFLG:
          name: '安全同步'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        RTTAGDISFLAG:
          name: '禁止使用tag检测环路'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        ECAROUTEFLAG:
          name: '使能ECA路由类型'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        DOMAINNULLFLAG:
          name: '配置Domain ID为空'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        SUPPREACH:
          name: '使能可达性抑制'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        SPFCONSERVFLAG:
          name: 'SPF正常模式标志'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        SHAMHELLOFLAG:
          name: '使能Sham-hello'
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
          name: '是否自动使能MPLS LDP功能'
          type: string
          enum:
          - Enable
          - None
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: None
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
        ROUTAG:
          name: 'VPN引入路由的tag值'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RETRANSLIMIT:
          name: '最大重传限制'
          type: integer
          minimum: 2
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 30
        STUBROUINCSTUB:
          name: '是否为Stub链路发布最大开销值'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        STUBROUSTUPINTV:
          name: 'On-Startup时间间隔（s）'
          type: integer
          minimum: 5
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 500
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
    add_ospfnetwork_list_6:
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
    add_ospfinterface_list_8:
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
        TIMERCONSERFLAG:
          name: '是否使能邻居失效定时器保守模式'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        CONFIGCOST:
          name: '接口开销值'
          type: integer
          minimum: 0
          maximum: 65535
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
    add_serviceip_list_4:
      type: items
      properties:
        IPVERSION:
          name: 'IP版本'
          type: string
          enum:
          - IPv4
          - IPv6
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: IPv4
        SERVICEIPV4:
          name: '业务IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VPNINSTNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DESC:
          name: '描述'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6MTU:
          name: 'IPv6 MTU大小'
          type: integer
          minimum: 1280
          maximum: 65534
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 1500
        SERVICEIPV6:
          name: '业务IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_serviceip_list_5:
      type: items
      properties:
        IPVERSION:
          name: 'IP版本'
          type: string
          enum:
          - IPv4
          - IPv6
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: IPv4
        SERVICEIPV4:
          name: '业务IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VPNINSTNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DESC:
          name: '描述'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6MTU:
          name: 'IPv6 MTU大小'
          type: integer
          minimum: 1280
          maximum: 65534
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 1500
        SERVICEIPV6:
          name: '业务IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_serviceip_list_6:
      type: items
      properties:
        IPVERSION:
          name: 'IP版本'
          type: string
          enum:
          - IPv4
          - IPv6
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: IPv4
        SERVICEIPV4:
          name: '业务IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VPNINSTNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DESC:
          name: '描述'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6MTU:
          name: 'IPv6 MTU大小'
          type: integer
          minimum: 1280
          maximum: 65534
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 1500
        SERVICEIPV6:
          name: '业务IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_gtpcle_list:
      type: items
      properties:
        GROUPID:
          name: '组号'
          type: integer
          minimum: 0
          maximum: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 0
        IPTYPE:
          name: 'IP地址类型'
          type: string
          enum:
          - TPTADDR_TYPE_IPV4
          - TPTADDR_TYPE_IPV6
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LEIPV4:
          name: 'IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VPNNAME:
          name: 'VPN名称'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DESC:
          name: '描述信息'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LEIPV6:
          name: 'IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_gtpule_list:
      type: items
      properties:
        GROUPID:
          name: '组号'
          type: integer
          minimum: 0
          maximum: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 0
        IPTYPE:
          name: 'IP地址类型'
          type: string
          enum:
          - TPTADDR_TYPE_IPV4
          - TPTADDR_TYPE_IPV6
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LEIPV4:
          name: 'IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VPNNAME:
          name: 'VPN名称'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DESC:
          name: '描述信息'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LEIPV6:
          name: 'IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_ugtp_list:
      type: items
      properties:
        ICI:
          name: '空闲计数器扫描间隔（秒）'
          type: integer
          minimum: 60
          maximum: 1800
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SSI:
          name: 'SM信令路径空闲计数器'
          type: integer
          minimum: 10
          maximum: 200
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MSI:
          name: 'MM信令路径空闲计数器'
          type: integer
          minimum: 10
          maximum: 200
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GMSI:
          name: 'GTPMAP路径空闲计数器'
          type: integer
          minimum: 10
          maximum: 200
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PATHVERCHKINT:
          name: '路径版本探测扫描周期（分钟）'
          type: integer
          minimum: 1
          maximum: 2400
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_gtppub_list:
      type: items
      properties:
        PRVEXT:
          name: '发送私有信息'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ECHOSIG:
          name: '发送ECHO Request的路径'
          type: string
          enum:
          - ALL
          - NONE
          - SPECIFIED
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        EI:
          name: '发送Echo请求间隔（s）'
          type: integer
          minimum: 60
          maximum: 3600
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        V2EI:
          name: '发送GTPv2 Echo请求间隔（s）'
          type: integer
          minimum: 60
          maximum: 3600
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        OTSIE:
          name: '乱序信元'
          type: string
          enum:
          - ALLOW
          - DENY
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        POTHD:
          name: '路径数过载门限（%）'
          type: integer
          minimum: 0
          maximum: 100
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PNTHD:
          name: '路径数过载恢复（%）'
          type: integer
          minimum: 0
          maximum: 100
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PCTHD:
          name: '路径数拥塞门限（%）'
          type: integer
          minimum: 0
          maximum: 100
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PRTHD:
          name: '路径数拥塞恢复（%）'
          type: integer
          minimum: 0
          maximum: 100
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PEID:
          name: '企业号'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PE:
          name: '私有信息'
          type: string
          maxLength: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GTPEXT:
          name: '检查GTP扩展头类型个数上限'
          type: integer
          minimum: 1
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GTPSUPEXTLIST:
          name: '检查GTP扩展头列表个数上限'
          type: integer
          minimum: 1
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GTPEXLEN:
          name: '检查GTP扩展头类型长度上限'
          type: integer
          minimum: 1
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GTPVER:
          name: '本端可处理的请求消息的最高GTP版本'
          type: string
          enum:
          - GTPv0
          - GTPv1
          - GTPv2
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        POOLSRCPORTSW:
          name: '缺省SGSN透传源端口号开关'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PEERRECOVERYSW:
          name: '对端Recovery处理开关'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PATHDOWNDEASW:
          name: 'GTPC路径断去激活开关'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PATHVERDETECTSW:
          name: 'V0版本GTPC路径尝试使用V1版本探测开关'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DNSGTPCPATHFILTERSW:
          name: '过滤故障状态的GTPC路径开关'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LOCRECOVERYSW:
          name: '本端recovery更新开关'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        UDPCHKSW:
          name: 'GTPC报文校验功能开关'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_dnss_list:
      type: items
      properties:
        GRPID:
          name: '服务器组ID'
          type: integer
          minimum: 0
          maximum: 37
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 0
        IP:
          name: 'IP地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PRI:
          name: '域名服务器优先级'
          type: string
          enum:
          - PRI1
          - PRI2
          - PRI3
          - PRI4
          - PRI5
          - PRI6
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DNSSNAME:
          name: 'DNS服务器名称'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PRO:
          name: 'DNS服务器承载协议'
          type: string
          enum:
          - TCP
          - UDP
          - UDP_TCP
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: UDP_TCP
        IPT:
          name: 'IP地址类型'
          type: string
          enum:
          - IPV4
          - IPV6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: IPV4
    add_dnsle_list:
      type: items
      properties:
        IPT:
          name: 'IP地址类型'
          type: string
          enum:
          - IPV4
          - IPV6
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV4:
          name: 'IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LOCPORT:
          name: '本地端口号'
          type: integer
          minimum: 15000
          maximum: 65535
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VPNNAME:
          name: 'VPN名称'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LENAME:
          name: 'DNS本端实体名称'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6:
          name: 'IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_ipv4dnsh_list:
      type: items
      properties:
        HSINDEX:
          name: '主机名索引'
          type: integer
          minimum: 1
          maximum: 1024
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        HOSTNAME:
          name: '主机名'
          type: string
          maxLength: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ADDRSECTION:
          name: '地址区间号'
          type: string
          enum:
          - SECTION1
          - SECTION2
          - SECTION3
          - SECTION4
          - SECTION5
          - SECTION6
          - SECTION7
          - SECTION8
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV4ADDR1:
          name: 'IPv4地址1'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PRIORITY1:
          name: '优先级1'
          type: integer
          minimum: 0
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 127
        WEIGHT1:
          name: '权重1'
          type: integer
          minimum: 1
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 127
        IPV4ADDR2:
          name: 'IPv4地址2'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PRIORITY2:
          name: '优先级2'
          type: integer
          minimum: 0
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 127
        WEIGHT2:
          name: '权重2'
          type: integer
          minimum: 1
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 127
        IPV4ADDR3:
          name: 'IPv4地址3'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PRIORITY3:
          name: '优先级3'
          type: integer
          minimum: 0
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 127
        WEIGHT3:
          name: '权重3'
          type: integer
          minimum: 1
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 127
        IPV4ADDR4:
          name: 'IPv4地址4'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PRIORITY4:
          name: '优先级4'
          type: integer
          minimum: 0
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 127
        WEIGHT4:
          name: '权重4'
          type: integer
          minimum: 1
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 127
        IPV4ADDR5:
          name: 'IPv4地址5'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PRIORITY5:
          name: '优先级5'
          type: integer
          minimum: 0
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 127
        WEIGHT5:
          name: '权重5'
          type: integer
          minimum: 1
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 127
        IPV4ADDR6:
          name: 'IPv4地址6'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PRIORITY6:
          name: '优先级6'
          type: integer
          minimum: 0
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 127
        WEIGHT6:
          name: '权重6'
          type: integer
          minimum: 1
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 127
        IPV4ADDR7:
          name: 'IPv4地址7'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PRIORITY7:
          name: '优先级7'
          type: integer
          minimum: 0
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 127
        WEIGHT7:
          name: '权重7'
          type: integer
          minimum: 1
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 127
        IPV4ADDR8:
          name: 'IPv4地址8'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PRIORITY8:
          name: '优先级8'
          type: integer
          minimum: 0
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 127
        WEIGHT8:
          name: '权重8'
          type: integer
          minimum: 1
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 127
    add_dnsn_list:
      type: items
      properties:
        FQDN:
          name: 'FQDN'
          type: string
          maxLength: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        HSINDEX:
          name: '主机名索引'
          type: integer
          minimum: 1
          maximum: 2048
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ENTITY:
          name: '网元类型'
          type: string
          enum:
          - AMF
          - GGSN
          - IWS
          - MME
          - MSC
          - PGW
          - SGSN
          - SGW
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        INTYPE:
          name: '接口类型'
          type: string
          enum:
          - Gn
          - Gp
          - N26
          - S10
          - S102
          - S11
          - S16
          - S3
          - S4
          - S5
          - S8
          - Sdup
          - Sv
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        S5PROTOCOL:
          name: 'S5接口协议类型'
          type: string
          enum:
          - GTP
          - GTP_PMIP
          - PMIP
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: GTP
        S8PROTOCOL:
          name: 'S8接口协议类型'
          type: string
          enum:
          - GTP
          - GTP_PMIP
          - PMIP
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: GTP
        PRIORITY:
          name: '优先级'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 0
        WEIGHT:
          name: '权重'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 100
    add_ipv4dnsh_list_2:
      type: items
      properties:
        HSINDEX:
          name: '主机名索引'
          type: integer
          minimum: 1
          maximum: 1024
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        HOSTNAME:
          name: '主机名'
          type: string
          maxLength: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ADDRSECTION:
          name: '地址区间号'
          type: string
          enum:
          - SECTION1
          - SECTION2
          - SECTION3
          - SECTION4
          - SECTION5
          - SECTION6
          - SECTION7
          - SECTION8
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV4ADDR1:
          name: 'IPv4地址1'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PRIORITY1:
          name: '优先级1'
          type: integer
          minimum: 0
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 127
        WEIGHT1:
          name: '权重1'
          type: integer
          minimum: 1
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 127
        IPV4ADDR2:
          name: 'IPv4地址2'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PRIORITY2:
          name: '优先级2'
          type: integer
          minimum: 0
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 127
        WEIGHT2:
          name: '权重2'
          type: integer
          minimum: 1
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 127
        IPV4ADDR3:
          name: 'IPv4地址3'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PRIORITY3:
          name: '优先级3'
          type: integer
          minimum: 0
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 127
        WEIGHT3:
          name: '权重3'
          type: integer
          minimum: 1
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 127
        IPV4ADDR4:
          name: 'IPv4地址4'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PRIORITY4:
          name: '优先级4'
          type: integer
          minimum: 0
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 127
        WEIGHT4:
          name: '权重4'
          type: integer
          minimum: 1
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 127
        IPV4ADDR5:
          name: 'IPv4地址5'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PRIORITY5:
          name: '优先级5'
          type: integer
          minimum: 0
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 127
        WEIGHT5:
          name: '权重5'
          type: integer
          minimum: 1
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 127
        IPV4ADDR6:
          name: 'IPv4地址6'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PRIORITY6:
          name: '优先级6'
          type: integer
          minimum: 0
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 127
        WEIGHT6:
          name: '权重6'
          type: integer
          minimum: 1
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 127
        IPV4ADDR7:
          name: 'IPv4地址7'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PRIORITY7:
          name: '优先级7'
          type: integer
          minimum: 0
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 127
        WEIGHT7:
          name: '权重7'
          type: integer
          minimum: 1
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 127
        IPV4ADDR8:
          name: 'IPv4地址8'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PRIORITY8:
          name: '优先级8'
          type: integer
          minimum: 0
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 127
        WEIGHT8:
          name: '权重8'
          type: integer
          minimum: 1
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 127
    add_dnsn_list_2:
      type: items
      properties:
        FQDN:
          name: 'FQDN'
          type: string
          maxLength: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        HSINDEX:
          name: '主机名索引'
          type: integer
          minimum: 1
          maximum: 2048
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ENTITY:
          name: '网元类型'
          type: string
          enum:
          - AMF
          - GGSN
          - IWS
          - MME
          - MSC
          - PGW
          - SGSN
          - SGW
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        INTYPE:
          name: '接口类型'
          type: string
          enum:
          - Gn
          - Gp
          - N26
          - S10
          - S102
          - S11
          - S16
          - S3
          - S4
          - S5
          - S8
          - Sdup
          - Sv
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        S5PROTOCOL:
          name: 'S5接口协议类型'
          type: string
          enum:
          - GTP
          - GTP_PMIP
          - PMIP
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: GTP
        S8PROTOCOL:
          name: 'S8接口协议类型'
          type: string
          enum:
          - GTP
          - GTP_PMIP
          - PMIP
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: GTP
        PRIORITY:
          name: '优先级'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 0
        WEIGHT:
          name: '权重'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 100
        DESC:
          name: '描述'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_emm_list:
      type: items
      properties:
        T3422:
          name: 'T3422（s）'
          type: integer
          minimum: 3
          maximum: 12
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        N3422:
          name: 'N3422（times）'
          type: integer
          minimum: 0
          maximum: 5
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        T3450:
          name: 'T3450（s）'
          type: integer
          minimum: 3
          maximum: 12
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        N3450:
          name: 'N3450（times）'
          type: integer
          minimum: 0
          maximum: 5
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        T3460:
          name: 'T3460（s）'
          type: integer
          minimum: 3
          maximum: 12
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        N3460:
          name: 'N3460（times）'
          type: integer
          minimum: 0
          maximum: 5
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        T3470:
          name: 'T3470（s）'
          type: integer
          minimum: 3
          maximum: 12
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        N3470:
          name: 'N3470（times）'
          type: integer
          minimum: 0
          maximum: 5
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        T3412:
          name: 'T3412（min）'
          type: integer
          minimum: 1
          maximum: 186
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        T3402:
          name: 'T3402（min）'
          type: integer
          minimum: 1
          maximum: 186
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        T3413:
          name: 'T3413（s）'
          type: integer
          minimum: 3
          maximum: 12
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        N3413:
          name: 'N3413（times）'
          type: integer
          minimum: 0
          maximum: 5
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PAGINGDELTA:
          name: '重寻呼间隔递增值（s）'
          type: integer
          minimum: 0
          maximum: 20
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        HPT3413:
          name: '高优先级业务的T3413（s）'
          type: integer
          minimum: 1
          maximum: 12
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        HPN3413:
          name: '高优先级业务的N3413（times）'
          type: integer
          minimum: 0
          maximum: 10
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        HPPAGINGDELTA:
          name: '高优先级业务的重寻呼间隔递增值（s）'
          type: integer
          minimum: 0
          maximum: 20
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RCHTMR:
          name: '移动可达定时器（min）'
          type: integer
          minimum: 2
          maximum: 198
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IMDTCHTMR:
          name: '不可达用户隐式分离定时器（min）'
          type: integer
          minimum: 0
          maximum: 198
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GUTITMR:
          name: 'GUTI重分配定时器（h）'
          type: integer
          minimum: 0
          maximum: 24
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GUTIREALLOC:
          name: 'Attach或TAU中重分配GUTI'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        HOPRETMR:
          name: 'Handover准备定时器（s）'
          type: integer
          minimum: 5
          maximum: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        HOCMPSRCTMR:
          name: '源侧Handover完成定时器（s）'
          type: integer
          minimum: 5
          maximum: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        HOCMPTGTTMR:
          name: '目标侧Handover完成定时器（s）'
          type: integer
          minimum: 5
          maximum: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        T3:
          name: 'T3定时器（s）'
          type: integer
          minimum: 3
          maximum: 60
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GUTITMRFORDEBUG:
          name: '测试用GUTI重分配定时器（m）'
          type: integer
          minimum: 0
          maximum: 254
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        HOT3:
          name: '切换流程资源释放定时器（s）'
          type: integer
          minimum: 1
          maximum: 60
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GUTIREALLOCTMR:
          name: 'GUTI重分配最大间隔（h）'
          type: integer
          minimum: 0
          maximum: 24
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_esm_list:
      type: items
      properties:
        T3485:
          name: 'T3485（s）'
          type: integer
          minimum: 1
          maximum: 86400
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        N3485:
          name: 'N3485（times）'
          type: integer
          minimum: 0
          maximum: 5
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        T3486:
          name: 'T3486（s）'
          type: integer
          minimum: 1
          maximum: 86400
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        N3486:
          name: 'N3486（times）'
          type: integer
          minimum: 0
          maximum: 5
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        T3489:
          name: 'T3489（s）'
          type: integer
          minimum: 1
          maximum: 86400
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        N3489:
          name: 'N3489（times）'
          type: integer
          minimum: 0
          maximum: 5
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        T3495:
          name: 'T3495（s）'
          type: integer
          minimum: 1
          maximum: 86400
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        N3495:
          name: 'N3495（times）'
          type: integer
          minimum: 0
          maximum: 5
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TSAEBRSETUP:
          name: 'SAE承载建立定时器（s）'
          type: integer
          minimum: 0
          maximum: 30
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TSAEBRMOD:
          name: 'SAE承载修改定时器（s）'
          type: integer
          minimum: 0
          maximum: 30
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TSAEBRREL:
          name: 'SAE承载释放定时器（s）'
          type: integer
          minimum: 0
          maximum: 30
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TSAEBRHOLD:
          name: 'SAE承载保留时长（s）'
          type: integer
          minimum: 1
          maximum: 120
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_smfunc_list:
      type: items
      properties:
        DUALFLAG:
          name: 'IPv4v6双栈'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        INDFWD:
          name: '强制启动间接转发方式'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TOPSELCFG:
          name: '拓扑选择开关'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        APNRES:
          name: 'APN限制功能开关'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PDPRMD:
          name: 'APN限制的去激活方式'
          type: string
          enum:
          - MAX
          - MIN
          - RANDOM
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SGWTOPO:
          name: '3G到4G切换SGW拓扑选择增强开关'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TZININTERRAU:
          name: '切换后时区携带策略'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        APNOIPLY:
          name: '启用HSS签约的APN级APN-OI-Replacement'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LTEGWSELPLCY:
          name: 'LTE场景相同APN选择网关策略'
          type: string
          enum:
          - INTERFACE_IP
          - SERVICE_IP
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GUGWSELPLCY:
          name: 'GU场景相同APN选择网关策略'
          type: string
          enum:
          - APNDNS
          - INTERFACE_IP
          - SERVICE_IP
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PRAULI:
          name: 'PRA状态上报携带ULI开关'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MMULI:
          name: '移动性管理流程ULI上报开关'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NETLOC:
          name: 'NetLoc功能开关'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RETLOC:
          name: '获取实时位置开关'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ULITYPE:
          name: '用户位置类型'
          type: string
          enum:
          - ECGI
          - TAI_ECGI
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IMSPOLICY:
          name: 'IMS连接激活策略'
          type: string
          enum:
          - ALLOW
          - REJECT
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        APNNISOURCE:
          name: '下发给UE的APN-NI来源'
          type: string
          enum:
          - APNNI_AFTER_SUBDATA_MATCH
          - UE_REQUEST_APNNI
          - UE_REQUEST_APNNI_AFTER_CORRECT
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        EPCO:
          name: 'MME支持ePCO信元处理'
          type: string
          enum:
          - NOT_SUPPORT
          - SUPPORT
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PDPTYPE:
          name: 'PDP/PDN Type策略'
          type: string
          enum:
          - IPv4
          - IPv4v6
          - IPv6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IMSREJCAUSE:
          name: 'IMS连接拒绝原因值'
          type: integer
          minimum: 0
          maximum: 112
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    add_hplmn_list:
    - MCC: '123'
      MNC: '001'
      CC: '86'
      S5S8TYPE: GTP
    add_mmeid_list:
    - MCC: '123'
      MNC: '001'
      MMEGI: 'FF33'
      MMEC: '01'
    set_sys_list:
    - CAP: 255
    add_l3vpninst_list:
    - VRFNAME: 'vpn_SIG'
      VRFDESCRIPTION: 'vpn_SIG'
    add_vpninstaf_list:
    - VRFNAME: 'vpn_SIG'
      AFTYPE: ipv4uni
    mod_interface_list:
    - IFNAME: 'Ethernet64/0/8'
      IFADMINSTATUS: up
      IFMTU: 1500
      IFDF: FALSE
      IFSTATIENABLE: TRUE
      IFTRAPENABLE: TRUE
      IFSTATITVL: 5
    add_interface_list:
    - IFNAME: 'Ethernet64/0/8.2130'
      IFADMINSTATUS: up
      IFMTU: 1500
      IFDF: FALSE
      IFSTATIENABLE: FALSE
      IFTRAPENABLE: TRUE
      IFSTATITVL: 5
    add_ipbindvpn_list:
    - IFNAME: 'Ethernet64/0/8.2130'
      VRFNAME: 'vpn_SIG'
    add_ethsubif_list:
    - IFNAME: 'Ethernet64/0/8.2130'
      SUBIFTYPE: VlanType
      VLANTYPEVID: 2130
    add_ifipv4address_list:
    - IFNAME: 'Ethernet64/0/8.2130'
      IFIPADDR: '10.220.82.98'
      SUBNETMASK: '255.255.255.240'
      ADDRTYPE: main
    add_ospf_list:
    - PROCID: 668
      VRFNAME: 'vpn_SIG'
      SCHEMAROUID: '10.220.95.25'
      SILENTALLFLAG: FALSE
      BFDALLINTFFLG: TRUE
      BFDRXCFGFLAG: TRUE
      BFDMINRXINTV: 500
      BFDTXCFGFLAG: TRUE
      BFDMINTXINTV: 500
      SCHEMABFDDETMUL: 8
      RFC1583COMPFLG: TRUE
      ROUTAGFLAG: FALSE
      BANDWIDTHREF: 100
      RXMTLIMITENABLE: FALSE
      OPAQCAPFLG: FALSE
      LSAARRINTVFLAG: FALSE
      LSAARRMAXINTV: 1000
      LSAARRSTARINTV: 500
      LSAARRHLDINTV: 500
      LSAORIGINSTFLAG: FALSE
      LSAORIGINTV: 5
      LSAORIGMAXINTV: 5000
      LSAORIGSTARINTV: 500
      LSAORIGHLDINTV: 1000
      VPNINSCAPSIMFLG: TRUE
      STUBROUFLG: NoConfig
      SAFESYNCFLG: FALSE
      RTTAGDISFLAG: FALSE
      ECAROUTEFLAG: FALSE
      DOMAINNULLFLAG: FALSE
      SUPPREACH: FALSE
      SPFCONSERVFLAG: FALSE
      SHAMHELLOFLAG: FALSE
      MPLSLDPAUTOCFG: None
      VIRTUALSYSFLAG: TRUE
      LSAARRINTV: ''
      ROUTAG: ''
      RETRANSLIMIT: 30
      STUBROUINCSTUB: FALSE
      STUBROUSTUPINTV: 500
    add_ospfarea_list:
    - PROCID: 668
      AREAID: '10.0.0.33'
      AREATYPE: NSSA
      NSSADEFAULTROUTEADVERTISE: FALSE
      NSSANOIMPORTROUTE: FALSE
      NSSANOSUMMARY: FALSE
      NSSASETNBIT: FALSE
      NSSASUPPRESSFORWARDINGADDRESS: FALSE
      NSSATRANSLATORALWAYS: FALSE
      NSSATRANSLATORINTERVAL: 40
      NSSAZEROADDRESSFORWARDING: FALSE
      DEFAULTCOST: 1
      STUBNOSUMMARY: FALSE
    add_ospfnetwork_list:
    - PROCID: 668
      AREAID: '10.0.0.33'
      IPADDRESS: '10.220.82.96'
      WILDCARDMASK: '0.0.0.15'
    add_ospfimportroute_list:
    - PROCID: 668
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
    set_bfd_list:
    - BFDENABLE: TRUE
      DELAYUPTIMER: 0
      TOSEXP: 7
    add_ospfinterface_list:
    - PROCID: 668
      AREAID: '10.0.0.33'
      IFNAME: 'Ethernet64/0/8.2130'
      DRPRI: 0
      NETWORKTYPE: broadcast
      TIMERCONSERFLAG: FALSE
      CONFIGCOST: 1500
      BFDENABLE: TRUE
      MINRXRECVINTV: 500
      MINTXTRANINTV: 500
      DETECTMULINTV: 4
      VIRTUALSYSFLAG: TRUE
      CFGROUTERIDFLAG: FALSE
    add_serviceip_list:
    - IPVERSION: IPv4
      SERVICEIPV4: '10.220.96.136'
      VPNINSTNAME: 'vpn_SIG'
      DESC: 'S6a'
      IPV6MTU: 1500
      SERVICEIPV6: ''
    add_sctppara_list:
    - SCTPPARAINDEX: 20
      RTOMIN: 220
      RTOMAX: 800
      RTOINIT: 220
      RTOALPHA: 12
      RTOBETA: 25
      HBINTERVAL: 3000
      MAXASSOCRETR: 5
      MAXPATHRETR: 4
      MAXINSTREAMS: 17
      MAXOUTSTREAMS: 17
      CNGLEVELNO: 40
      CNGLEVELLOW: 60
      CNGLEVELHIGH: 80
      CHKSUMTX: YES
      CHKSUMRX: YES
      CHKSUMTYPE: CRC32
      BINDTMR: 10
      DELAYTMRLEN: 200
      IPV4MTU: 1500
      IPV6MTU: 1500
      SCTPPARANAME: 'For_S6a_HSS'
      PKGERRFAULT: 5
      PKGERRRECOVER: 3
      MINRECVPKGNUM: 100
    add_dmle_list:
    - LOINDEX: 0
      LOHSTNAME: 'TEUSNH02.epc.mnc035.mcc123.3gppnetwork.org'
      LORLMNAME: 'epc.mnc035.mcc123.3gppnetwork.org'
      PDTNAME: 'UNC'
      LOINFONAME: 'TEUSNH02'
    add_dmpe_list:
    - PEERIDX: 1
      PEERHTNAM: 'TEHSSH01.epc.mnc035.mcc123.3gppnetwork.org'
      PEERNAM: 'TEHSSH01'
      APPCAP: S13-0&S6a/S6d-1&SLg-0
      CONGSW: OFF
    add_dmlks_list:
    - LINKSIDX: 1
      LOCALIDX: 0
      PEERIDX: 1
      LSSELMODE: SELMODE_LOAD_BALAN
      LINKSNAM: 'TEHSSH01_LKS'
    add_dmlnk_list:
    - VPNNAME: 'vpn_SIG'
      LINKIDX: 1
      IPTYPE: TPTADDR_TYPE_IPV4
      PROTOTYPE: CONN_PROTOCOL_SCTP
      LOCALIPV4_1: '10.220.96.136'
      LOCALIPV4_2: '10.220.96.137'
      LOCALPORT: 8520
      PEERIPV4_1: '10.133.221.4'
      PEERIPV4_2: '10.133.221.12'
      PEERPORT: 3868
      CLIORSER: DIAM_CONN_CLIENT
      LINKSIDX: 1
      SCTPINDX: 20
      LINKNAM: 'TEHSSH01_C_01'
      CROSSIPFLAG: NO
      LOCALIPV6_1: ''
      LOCALIPV6_2: ''
      PEERIPV6_1: ''
      PEERIPV6_2: ''
    add_dmhostrt_list:
    - ROUTEIDX: 1
      APPNAM: S6A/S6D
      RSELMODE: SELMODE_MASTER_SLAVE
      PEERSEL: PEER_INDEX
      PEERIDX: 1
      ROUTENAM: 'TEHSSH01_HR'
      PRIORITY: 0
      PEERHTNAM: ''
      WEIGHT: 1
    add_dmrtgrp_list:
    - GRPIDX: 1
      RTMODE: HOST_ROUTE
      RTPRIMODE: HOST_ROUTE_PREFER
      ROUTEIDX: 1
      ROUTEGRPNAM: 'TEHSSH01_RGP'
      PEERIDX: ''
    add_imsihss_list:
    - IMSIPRE: '12302000'
      HSSRLM: 'epc.mnc035.mcc123.3gppnetwork.org'
      GRPIDX: 1
      MNNAME: 'MVNO'
    add_l3vpninst_list_1:
    - VRFNAME: 'vpn_s1mme'
    add_vpninstaf_list_1:
    - VRFNAME: 'vpn_s1mme'
      AFTYPE: ipv4uni
    mod_interface_list_4:
    - IFNAME: 'Ethernet64/0/4'
      IFADMINSTATUS: up
      IFMTU: 1500
      IFDF: FALSE
      IFSTATIENABLE: TRUE
      IFTRAPENABLE: TRUE
      IFSTATITVL: 5
    add_interface_list_5:
    - IFNAME: 'Ethernet64/0/4.2124'
      IFADMINSTATUS: up
      IFMTU: 1500
      IFDF: FALSE
      IFSTATIENABLE: FALSE
      IFTRAPENABLE: TRUE
      IFSTATITVL: 5
    add_ipbindvpn_list_5:
    - IFNAME: 'Ethernet64/0/4.2124'
      VRFNAME: 'vpn_s1mme'
    add_ethsubif_list_4:
    - IFNAME: 'Ethernet64/0/4.2124'
      SUBIFTYPE: VlanType
      VLANTYPEVID: 2124
    add_ifipv4address_list_5:
    - IFNAME: 'Ethernet64/0/4.2124'
      IFIPADDR: '10.220.83.98'
      SUBNETMASK: '255.255.255.240'
      ADDRTYPE: main
    add_ospf_list_1:
    - PROCID: 224
      VRFNAME: 'vpn_s1mme'
      SCHEMAROUID: '10.220.95.19'
      SILENTALLFLAG: FALSE
      BFDALLINTFFLG: TRUE
      BFDRXCFGFLAG: TRUE
      BFDMINRXINTV: 500
      BFDTXCFGFLAG: TRUE
      BFDMINTXINTV: 500
      SCHEMABFDDETMUL: 8
      RFC1583COMPFLG: TRUE
      ROUTAGFLAG: FALSE
      BANDWIDTHREF: 100
      RXMTLIMITENABLE: FALSE
      OPAQCAPFLG: FALSE
      LSAARRINTVFLAG: FALSE
      LSAARRMAXINTV: 1000
      LSAARRSTARINTV: 500
      LSAARRHLDINTV: 500
      LSAORIGINSTFLAG: FALSE
      LSAORIGINTV: 5
      LSAORIGMAXINTV: 5000
      LSAORIGSTARINTV: 500
      LSAORIGHLDINTV: 1000
      VPNINSCAPSIMFLG: TRUE
      STUBROUFLG: NoConfig
      SAFESYNCFLG: FALSE
      RTTAGDISFLAG: FALSE
      ECAROUTEFLAG: FALSE
      DOMAINNULLFLAG: FALSE
      SUPPREACH: FALSE
      SPFCONSERVFLAG: FALSE
      SHAMHELLOFLAG: FALSE
      MPLSLDPAUTOCFG: None
      VIRTUALSYSFLAG: TRUE
      LSAARRINTV: ''
      ROUTAG: ''
      RETRANSLIMIT: 30
      STUBROUINCSTUB: FALSE
      STUBROUSTUPINTV: 500
    add_ospfarea_list_1:
    - PROCID: 224
      AREAID: '10.0.0.33'
      AREATYPE: NSSA
      NSSADEFAULTROUTEADVERTISE: FALSE
      NSSANOIMPORTROUTE: FALSE
      NSSANOSUMMARY: FALSE
      NSSASETNBIT: FALSE
      NSSASUPPRESSFORWARDINGADDRESS: FALSE
      NSSATRANSLATORALWAYS: FALSE
      NSSATRANSLATORINTERVAL: 40
      NSSAZEROADDRESSFORWARDING: FALSE
      DEFAULTCOST: 1
      STUBNOSUMMARY: FALSE
    add_ospfnetwork_list_3:
    - PROCID: 224
      AREAID: '10.0.0.33'
      IPADDRESS: '10.220.83.96'
      WILDCARDMASK: '0.0.0.15'
    add_ospfimportroute_list_1:
    - PROCID: 224
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
    add_ospfinterface_list_4:
    - PROCID: 224
      AREAID: '10.0.0.33'
      IFNAME: 'Ethernet64/0/4.2124'
      DRPRI: 0
      NETWORKTYPE: broadcast
      TIMERCONSERFLAG: FALSE
      CONFIGCOST: 1500
      BFDENABLE: TRUE
      MINRXRECVINTV: 500
      MINTXTRANINTV: 500
      DETECTMULINTV: 4
      VIRTUALSYSFLAG: TRUE
      CFGROUTERIDFLAG: FALSE
    add_serviceip_list_2:
    - IPVERSION: IPv4
      SERVICEIPV4: '10.220.96.134'
      VPNINSTNAME: 'vpn_s1mme'
      DESC: 'S1-MME'
      IPV6MTU: 1500
      SERVICEIPV6: ''
    add_sctppara_list_1:
    - SCTPPARAINDEX: 10
      RTOMIN: 220
      RTOMAX: 800
      RTOINIT: 220
      RTOALPHA: 12
      RTOBETA: 25
      HBINTERVAL: 3000
      MAXASSOCRETR: 5
      MAXPATHRETR: 4
      MAXINSTREAMS: 17
      MAXOUTSTREAMS: 17
      CNGLEVELNO: 40
      CNGLEVELLOW: 60
      CNGLEVELHIGH: 80
      CHKSUMTX: YES
      CHKSUMRX: YES
      CHKSUMTYPE: CRC32
      BINDTMR: 10
      DELAYTMRLEN: 200
      IPV4MTU: 1500
      IPV6MTU: 1500
      SCTPPARANAME: 'For S1 MME'
      PKGERRFAULT: 5
      PKGERRRECOVER: 3
      MINRECVPKGNUM: 100
    add_s1aple_list:
    - LLEINDEX: 1
      IPTYPE: TPTADDR_TYPE_IPV4
      LOCALIPV4_1: '10.220.96.134'
      LOCALIPV4_2: '10.220.96.135'
      LOCALPORT: 36412
      CROSSIPFLAG: NO
      SCTPINDEX: 10
      LLNAME: 'S1APLE_TEUSNH02'
      VPNNAME: 'vpn_s1mme'
      LOCALIPV6_1: ''
      LOCALIPV6_2: ''
    add_l3vpninst_list_2:
    - VRFNAME: 'vpn_gn_1'
    add_vpninstaf_list_2:
    - VRFNAME: 'vpn_gn_1'
      AFTYPE: ipv4uni
    mod_interface_list_8:
    - IFNAME: 'Ethernet64/0/6'
      IFADMINSTATUS: up
      IFMTU: 1500
      IFDF: FALSE
      IFSTATIENABLE: TRUE
      IFTRAPENABLE: TRUE
      IFSTATITVL: 5
    add_interface_list_10:
    - IFNAME: 'Ethernet64/0/6.2126'
      IFADMINSTATUS: up
      IFMTU: 1500
      IFDF: FALSE
      IFSTATIENABLE: FALSE
      IFTRAPENABLE: TRUE
      IFSTATITVL: 5
    add_ipbindvpn_list_10:
    - IFNAME: 'Ethernet64/0/6.2126'
      VRFNAME: 'vpn_gn_1'
    add_ethsubif_list_8:
    - IFNAME: 'Ethernet64/0/6.2126'
      SUBIFTYPE: VlanType
      VLANTYPEVID: 2126
    add_ifipv4address_list_10:
    - IFNAME: 'Ethernet64/0/6.2126'
      IFIPADDR: '10.220.81.162'
      SUBNETMASK: '255.255.255.240'
      ADDRTYPE: main
    add_ospf_list_2:
    - PROCID: 185
      VRFNAME: 'vpn_gn_1'
      SCHEMAROUID: '10.220.95.21'
      SILENTALLFLAG: FALSE
      BFDALLINTFFLG: TRUE
      BFDRXCFGFLAG: TRUE
      BFDMINRXINTV: 500
      BFDTXCFGFLAG: TRUE
      BFDMINTXINTV: 500
      SCHEMABFDDETMUL: 8
      RFC1583COMPFLG: TRUE
      ROUTAGFLAG: FALSE
      BANDWIDTHREF: 100
      RXMTLIMITENABLE: FALSE
      OPAQCAPFLG: FALSE
      LSAARRINTVFLAG: FALSE
      LSAARRMAXINTV: 1000
      LSAARRSTARINTV: 500
      LSAARRHLDINTV: 500
      LSAORIGINSTFLAG: FALSE
      LSAORIGINTV: 5
      LSAORIGMAXINTV: 5000
      LSAORIGSTARINTV: 500
      LSAORIGHLDINTV: 1000
      VPNINSCAPSIMFLG: TRUE
      STUBROUFLG: NoConfig
      SAFESYNCFLG: FALSE
      RTTAGDISFLAG: FALSE
      ECAROUTEFLAG: FALSE
      DOMAINNULLFLAG: FALSE
      SUPPREACH: FALSE
      SPFCONSERVFLAG: FALSE
      SHAMHELLOFLAG: FALSE
      MPLSLDPAUTOCFG: None
      VIRTUALSYSFLAG: TRUE
      LSAARRINTV: ''
      ROUTAG: ''
      RETRANSLIMIT: 30
      STUBROUINCSTUB: FALSE
      STUBROUSTUPINTV: 500
    add_ospfarea_list_2:
    - PROCID: 185
      AREAID: '10.0.0.33'
      AREATYPE: NSSA
      NSSADEFAULTROUTEADVERTISE: FALSE
      NSSANOIMPORTROUTE: FALSE
      NSSANOSUMMARY: FALSE
      NSSASETNBIT: FALSE
      NSSASUPPRESSFORWARDINGADDRESS: FALSE
      NSSATRANSLATORALWAYS: FALSE
      NSSATRANSLATORINTERVAL: 40
      NSSAZEROADDRESSFORWARDING: FALSE
      DEFAULTCOST: 1
      STUBNOSUMMARY: FALSE
    add_ospfnetwork_list_6:
    - PROCID: 185
      AREAID: '10.0.0.33'
      IPADDRESS: '10.220.81.160'
      WILDCARDMASK: '0.0.0.15'
    add_ospfimportroute_list_2:
    - PROCID: 185
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
    add_ospfinterface_list_8:
    - PROCID: 185
      AREAID: '10.0.0.33'
      IFNAME: 'Ethernet64/0/6.2126'
      DRPRI: 0
      NETWORKTYPE: broadcast
      TIMERCONSERFLAG: FALSE
      CONFIGCOST: 1500
      BFDENABLE: TRUE
      MINRXRECVINTV: 500
      MINTXTRANINTV: 500
      DETECTMULINTV: 4
      VIRTUALSYSFLAG: TRUE
      CFGROUTERIDFLAG: FALSE
    add_serviceip_list_4:
    - IPVERSION: IPv4
      SERVICEIPV4: '10.42.48.113'
      VPNINSTNAME: 'vpn_gn_1'
      DESC: 'for_S10'
      IPV6MTU: 1500
      SERVICEIPV6: ''
    add_serviceip_list_5:
    - IPVERSION: IPv4
      SERVICEIPV4: '10.42.48.114'
      VPNINSTNAME: 'vpn_gn_1'
      DESC: 'for_S11'
      IPV6MTU: 1500
      SERVICEIPV6: ''
    add_serviceip_list_6:
    - IPVERSION: IPv4
      SERVICEIPV4: '10.42.48.115'
      VPNINSTNAME: 'vpn_gn_1'
      DESC: 'for_Gn'
      IPV6MTU: 1500
      SERVICEIPV6: ''
    add_gtpcle_list:
    - GROUPID: 0
      IPTYPE: TPTADDR_TYPE_IPV4
      LEIPV4: '10.42.48.113'
      VPNNAME: 'vpn_gn_1'
      DESC: 'GTPC'
      LEIPV6: ''
    add_gtpule_list:
    - GROUPID: 0
      IPTYPE: TPTADDR_TYPE_IPV4
      LEIPV4: '10.42.48.114'
      VPNNAME: 'vpn_gn_1'
      DESC: 'GTPU'
      LEIPV6: ''
    set_ugtp_list:
    - ICI: 180
      SSI: 180
      MSI: 60
      GMSI: 60
      PATHVERCHKINT: 60
    set_gtppub_list:
    - PRVEXT: OFF
      ECHOSIG: ALL
      EI: 60
      V2EI: 60
      OTSIE: DENY
      POTHD: 85
      PNTHD: 80
      PCTHD: 95
      PRTHD: 90
      PEID: 2011
      PE: 'UNC'
      GTPEXT: 10
      GTPSUPEXTLIST: 100
      GTPEXLEN: 100
      GTPVER: GTPv2
      POOLSRCPORTSW: ON
      PEERRECOVERYSW: OFF
      PATHDOWNDEASW: OFF
      PATHVERDETECTSW: ON
      DNSGTPCPATHFILTERSW: ON
      LOCRECOVERYSW: ON
      UDPCHKSW: OFF
    add_dnss_list:
    - GRPID: 0
      IP: '10.178.167.22'
      PRI: PRI1
      DNSSNAME: 'MSDNSE01'
      PRO: UDP
      IPT: IPV4
    add_dnsle_list:
    - IPT: IPV4
      IPV4: '10.42.48.113'
      LOCPORT: 15000
      VPNNAME: 'vpn_gn_1'
      LENAME: 'TEUSNH02'
      IPV6: ''
    add_ipv4dnsh_list:
    - HSINDEX: 100
      HOSTNAME: 'TOPON.S11.TESGWH3.TE1.EPC.MNC035.MCC123.3GPPNETWORK.ORG'
      ADDRSECTION: SECTION1
      IPV4ADDR1: '10.132.20.176'
      PRIORITY1: 127
      WEIGHT1: 127
      IPV4ADDR2: '0.0.0.0'
      PRIORITY2: 127
      WEIGHT2: 127
      IPV4ADDR3: '0.0.0.0'
      PRIORITY3: 127
      WEIGHT3: 127
      IPV4ADDR4: '0.0.0.0'
      PRIORITY4: 127
      WEIGHT4: 127
      IPV4ADDR5: '0.0.0.0'
      PRIORITY5: 127
      WEIGHT5: 127
      IPV4ADDR6: '0.0.0.0'
      PRIORITY6: 127
      WEIGHT6: 127
      IPV4ADDR7: '0.0.0.0'
      PRIORITY7: 127
      WEIGHT7: 127
      IPV4ADDR8: '0.0.0.0'
      PRIORITY8: 127
      WEIGHT8: 127
    add_dnsn_list:
    - FQDN: 'TAC-LB26.TAC-HB58.TAC.EPC.MNC002.MCC123.3GPPNETWORK.ORG'
      HSINDEX: 301
      ENTITY: SGW
      INTYPE: S11
      S5PROTOCOL: GTP
      S8PROTOCOL: GTP
      PRIORITY: 0
      WEIGHT: 100
    add_ipv4dnsh_list_2:
    - HSINDEX: 777
      HOSTNAME: 'TOPON.S5.TEPGWH3.TE1.EPC.MNC002.MCC123.3GPPNETWORK.ORG'
      ADDRSECTION: SECTION1
      IPV4ADDR1: '10.42.49.81'
      PRIORITY1: 127
      WEIGHT1: 127
      IPV4ADDR2: '0.0.0.0'
      PRIORITY2: 127
      WEIGHT2: 127
      IPV4ADDR3: '0.0.0.0'
      PRIORITY3: 127
      WEIGHT3: 127
      IPV4ADDR4: '0.0.0.0'
      PRIORITY4: 127
      WEIGHT4: 127
      IPV4ADDR5: '0.0.0.0'
      PRIORITY5: 127
      WEIGHT5: 127
      IPV4ADDR6: '0.0.0.0'
      PRIORITY6: 127
      WEIGHT6: 127
      IPV4ADDR7: '0.0.0.0'
      PRIORITY7: 127
      WEIGHT7: 127
      IPV4ADDR8: '0.0.0.0'
      PRIORITY8: 127
      WEIGHT8: 127
    add_dnsn_list_2:
    - FQDN: 'APTEL.APN.EPC.MNC002.MCC123.3GPPNETWORK.ORG'
      HSINDEX: 777
      ENTITY: PGW
      INTYPE: S5
      S5PROTOCOL: GTP
      S8PROTOCOL: GTP
      PRIORITY: 0
      WEIGHT: 100
      DESC: 'aptel'
    set_emm_list:
    - T3422: 6
      N3422: 4
      T3450: 6
      N3450: 4
      T3460: 6
      N3460: 4
      T3470: 6
      N3470: 4
      T3412: 54
      T3402: 12
      T3413: 6
      N3413: 2
      PAGINGDELTA: 0
      HPT3413: 2
      HPN3413: 4
      HPPAGINGDELTA: 0
      RCHTMR: 58
      IMDTCHTMR: 0
      GUTITMR: 0
      GUTIREALLOC: YES
      HOPRETMR: 10
      HOCMPSRCTMR: 10
      HOCMPTGTTMR: 10
      T3: 10
      GUTITMRFORDEBUG: 0
      HOT3: 2
      GUTIREALLOCTMR: 0
    set_esm_list:
    - T3485: 8
      N3485: 4
      T3486: 8
      N3486: 4
      T3489: 4
      N3489: 2
      T3495: 8
      N3495: 4
      TSAEBRSETUP: 12
      TSAEBRMOD: 12
      TSAEBRREL: 12
      TSAEBRHOLD: 60
    set_smfunc_list:
    - DUALFLAG: YES
      INDFWD: YES
      TOPSELCFG: YES
      APNRES: NO
      PDPRMD: MAX
      SGWTOPO: NO
      TZININTERRAU: YES
      APNOIPLY: NO
      LTEGWSELPLCY: INTERFACE_IP
      GUGWSELPLCY: INTERFACE_IP
      PRAULI: OFF
      MMULI: ON
      NETLOC: ON
      RETLOC: OFF
      ULITYPE: TAI_ECGI
      IMSPOLICY: ALLOW
      APNNISOURCE: UE_REQUEST_APNNI_AFTER_CORRECT
      EPCO: NOT_SUPPORT
      PDPTYPE: ''
      IMSREJCAUSE: ''
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 进入“MML命令行-UNC”窗口。

### 2 配置本局信息，包括归属PLMN和MMEID。

```jinja2
{%- for item in add_hplmn_list -%}
    ADD HPLMN:
    {#- --- 必选参数 --- -#}
    MCC="{{item.MCC}}",
    MNC="{{item.MNC}}",
    {#- --- 可选参数 --- -#}
    {%- if item.CC is not none -%}
        CC="{{item.CC}}",
    {%- endif -%}
    {%- if item.S5S8TYPE is not none -%}
        S5S8TYPE={{item.S5S8TYPE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_mmeid_list -%}
    ADD MMEID:
    {#- --- 必选参数 --- -#}
    MCC="{{item.MCC}}",
    MNC="{{item.MNC}}",
    MMEGI="{{item.MMEGI}}",
    MMEC="{{item.MMEC}}",
    ;
{%- endfor -%}
```

```jinja2
{%- for item in set_sys_list -%}
    SET SYS:
    {#- --- 可选参数 --- -#}
    {%- if item.CAP is not none -%}
        CAP={{item.CAP}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 配置S6a数据。

#### 3.1 配置动态路由OSPF。

##### 3.1.1 配置VPN实例。

```jinja2
{%- for item in add_l3vpninst_list -%}
    ADD L3VPNINST:
    {#- --- 必选参数 --- -#}
    VRFNAME="{{item.VRFNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.VRFDESCRIPTION is not none -%}
        VRFDESCRIPTION="{{item.VRFDESCRIPTION}}",
    {%- endif -%}
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

##### 3.1.2 配置主接口的管理状态为up。

```jinja2
{%- for item in mod_interface_list -%}
    MOD INTERFACE:
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
    {%- if item.IFSTATITVL is not none -%}
        IFSTATITVL={{item.IFSTATITVL}},
    {%- endif -%}
    ;
{%- endfor -%}
```

##### 3.1.3 配置以太网接口。

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
    {%- if item.IFDF is not none -%}
        IFDF={{item.IFDF}},
    {%- endif -%}
    {%- if item.IFSTATIENABLE is not none -%}
        IFSTATIENABLE={{item.IFSTATIENABLE}},
    {%- endif -%}
    {%- if item.IFTRAPENABLE is not none -%}
        IFTRAPENABLE={{item.IFTRAPENABLE}},
    {%- endif -%}
    {%- if item.IFSTATITVL is not none -%}
        IFSTATITVL={{item.IFSTATITVL}},
    {%- endif -%}
    ;
{%- endfor -%}
```

##### 3.1.4 增加接口绑定VPN。

```jinja2
{%- for item in add_ipbindvpn_list -%}
    ADD IPBINDVPN:
    {#- --- 必选参数 --- -#}
    IFNAME="{{item.IFNAME}}",
    VRFNAME="{{item.VRFNAME}}",
    ;
{%- endfor -%}
```

##### 3.1.5 在以太网子接口上关联VLAN ID。

```jinja2
{%- for item in add_ethsubif_list -%}
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
```

##### 3.1.6 配置外联口的物理IP。

```jinja2
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
```

##### 3.1.7 创建OSPF进程。

```jinja2
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
    {%- if item.SILENTALLFLAG is not none -%}
        SILENTALLFLAG={{item.SILENTALLFLAG}},
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
    {%- if item.RFC1583COMPFLG is not none -%}
        RFC1583COMPFLG={{item.RFC1583COMPFLG}},
    {%- endif -%}
    {%- if item.ROUTAGFLAG is not none -%}
        ROUTAGFLAG={{item.ROUTAGFLAG}},
    {%- endif -%}
    {%- if item.BANDWIDTHREF is not none -%}
        BANDWIDTHREF={{item.BANDWIDTHREF}},
    {%- endif -%}
    {%- if item.RXMTLIMITENABLE is not none -%}
        RXMTLIMITENABLE={{item.RXMTLIMITENABLE}},
    {%- endif -%}
    {%- if item.OPAQCAPFLG is not none -%}
        OPAQCAPFLG={{item.OPAQCAPFLG}},
    {%- endif -%}
    {%- if item.LSAARRINTVFLAG is not none -%}
        LSAARRINTVFLAG={{item.LSAARRINTVFLAG}},
    {%- endif -%}
    {%- if item.LSAORIGINSTFLAG is not none -%}
        LSAORIGINSTFLAG={{item.LSAORIGINSTFLAG}},
    {%- endif -%}
    {%- if item.VPNINSCAPSIMFLG is not none -%}
        VPNINSCAPSIMFLG={{item.VPNINSCAPSIMFLG}},
    {%- endif -%}
    {%- if item.STUBROUFLG is not none -%}
        STUBROUFLG={{item.STUBROUFLG}},
    {%- endif -%}
    {%- if item.SAFESYNCFLG is not none -%}
        SAFESYNCFLG={{item.SAFESYNCFLG}},
    {%- endif -%}
    {%- if item.RTTAGDISFLAG is not none -%}
        RTTAGDISFLAG={{item.RTTAGDISFLAG}},
    {%- endif -%}
    {%- if item.ECAROUTEFLAG is not none -%}
        ECAROUTEFLAG={{item.ECAROUTEFLAG}},
    {%- endif -%}
    {%- if item.DOMAINNULLFLAG is not none -%}
        DOMAINNULLFLAG={{item.DOMAINNULLFLAG}},
    {%- endif -%}
    {%- if item.SUPPREACH is not none -%}
        SUPPREACH={{item.SUPPREACH}},
    {%- endif -%}
    {%- if item.SPFCONSERVFLAG is not none -%}
        SPFCONSERVFLAG={{item.SPFCONSERVFLAG}},
    {%- endif -%}
    {%- if item.SHAMHELLOFLAG is not none -%}
        SHAMHELLOFLAG={{item.SHAMHELLOFLAG}},
    {%- endif -%}
    {%- if item.MPLSLDPAUTOCFG is not none -%}
        MPLSLDPAUTOCFG={{item.MPLSLDPAUTOCFG}},
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
    {#- --- 条件必选：ROUTAGFLAG=TRUE 时必选 --- -#}
    {%- if item.ROUTAGFLAG == 'TRUE' -%}
        ROUTAG={{item.ROUTAG}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：LSAORIGINSTFLAG=FALSE 时可选 --- -#}
    {%- if item.LSAORIGINSTFLAG == 'FALSE' -%}
        {%- if item.LSAORIGINTV is not none -%}
            LSAORIGINTV={{item.LSAORIGINTV}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：LSAORIGINSTFLAG=FALSE 时可选 --- -#}
    {%- if item.LSAORIGINSTFLAG == 'FALSE' -%}
        {%- if item.LSAORIGMAXINTV is not none -%}
            LSAORIGMAXINTV={{item.LSAORIGMAXINTV}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：LSAORIGINSTFLAG=FALSE 时可选 --- -#}
    {%- if item.LSAORIGINSTFLAG == 'FALSE' -%}
        {%- if item.LSAORIGSTARINTV is not none -%}
            LSAORIGSTARINTV={{item.LSAORIGSTARINTV}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：LSAORIGINSTFLAG=FALSE 时可选 --- -#}
    {%- if item.LSAORIGINSTFLAG == 'FALSE' -%}
        {%- if item.LSAORIGHLDINTV is not none -%}
            LSAORIGHLDINTV={{item.LSAORIGHLDINTV}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：RXMTLIMITENABLE=TRUE 时可选 --- -#}
    {%- if item.RXMTLIMITENABLE == 'TRUE' -%}
        {%- if item.RETRANSLIMIT is not none -%}
            RETRANSLIMIT={{item.RETRANSLIMIT}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：STUBROUFLG=StubOnBoot/StubOnHand 时可选 --- -#}
    {%- if item.STUBROUFLG in ['StubOnBoot', 'StubOnHand'] -%}
        {%- if item.STUBROUINCSTUB is not none -%}
            STUBROUINCSTUB={{item.STUBROUINCSTUB}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：STUBROUFLG=StubOnBoot 时可选 --- -#}
    {%- if item.STUBROUFLG == 'StubOnBoot' -%}
        {%- if item.STUBROUSTUPINTV is not none -%}
            STUBROUSTUPINTV={{item.STUBROUSTUPINTV}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

##### 3.1.8 增加OSPF区域。

```jinja2
{%- for item in add_ospfarea_list -%}
    ADD OSPFAREA:
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
    {#- --- 条件可选：AREATYPE=Stub/NSSA 时可选 --- -#}
    {%- if item.AREATYPE in ['Stub', 'NSSA'] -%}
        {%- if item.DEFAULTCOST is not none -%}
            DEFAULTCOST={{item.DEFAULTCOST}},
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

##### 3.1.9 增加运行OSPF协议的接口。

```jinja2
{%- for item in add_ospfnetwork_list -%}
    ADD OSPFNETWORK:
    {#- --- 必选参数 --- -#}
    PROCID={{item.PROCID}},
    AREAID="{{item.AREAID}}",
    IPADDRESS="{{item.IPADDRESS}}",
    WILDCARDMASK="{{item.WILDCARDMASK}}",
    ;
{%- endfor -%}
```

##### 3.1.10 设置OSPF引入路由类型。

```jinja2
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
```

#### 3.2 配置BFD。

##### 3.2.1 全局激活BFD。

```jinja2
{%- for item in set_bfd_list -%}
    SET BFD:
    {#- --- 必选参数 --- -#}
    BFDENABLE={{item.BFDENABLE}},
    {#- --- 可选参数 --- -#}
    {%- if item.DELAYUPTIMER is not none -%}
        DELAYUPTIMER={{item.DELAYUPTIMER}},
    {%- endif -%}
    {%- if item.TOSEXP is not none -%}
        TOSEXP={{item.TOSEXP}},
    {%- endif -%}
    ;
{%- endfor -%}
```

##### 3.2.2 以接口粒度配置动态BFD。

```jinja2
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
    {%- if item.TIMERCONSERFLAG is not none -%}
        TIMERCONSERFLAG={{item.TIMERCONSERFLAG}},
    {%- endif -%}
    {%- if item.CONFIGCOST is not none -%}
        CONFIGCOST={{item.CONFIGCOST}},
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
    {%- if item.VIRTUALSYSFLAG is not none -%}
        VIRTUALSYSFLAG={{item.VIRTUALSYSFLAG}},
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
```

#### 3.3 配置S6a接口业务IP。

```jinja2
{%- for item in add_serviceip_list -%}
    ADD SERVICEIP:
    {#- --- 必选参数 --- -#}
    IPVERSION={{item.IPVERSION}},
    {#- --- 可选参数 --- -#}
    {%- if item.VPNINSTNAME is not none -%}
        VPNINSTNAME="{{item.VPNINSTNAME}}",
    {%- endif -%}
    {%- if item.DESC is not none -%}
        DESC="{{item.DESC}}",
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPVERSION=IPv4 时必选 --- -#}
    {%- if item.IPVERSION == 'IPv4' -%}
        SERVICEIPV4="{{item.SERVICEIPV4}}",
    {%- endif -%}
    {#- --- 条件必选：IPVERSION=IPv6 时必选 --- -#}
    {%- if item.IPVERSION == 'IPv6' -%}
        SERVICEIPV6="{{item.SERVICEIPV6}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：IPVERSION=IPv6 时可选 --- -#}
    {%- if item.IPVERSION == 'IPv6' -%}
        {%- if item.IPV6MTU is not none -%}
            IPV6MTU={{item.IPV6MTU}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 3.4 配置S6a接口基于IP的宽带信令SCTP偶联配置的SCTP协议参数。

```jinja2
{%- for item in add_sctppara_list -%}
    ADD SCTPPARA:
    {#- --- 必选参数 --- -#}
    SCTPPARAINDEX={{item.SCTPPARAINDEX}},
    {#- --- 可选参数 --- -#}
    {%- if item.RTOMIN is not none -%}
        RTOMIN={{item.RTOMIN}},
    {%- endif -%}
    {%- if item.RTOMAX is not none -%}
        RTOMAX={{item.RTOMAX}},
    {%- endif -%}
    {%- if item.RTOINIT is not none -%}
        RTOINIT={{item.RTOINIT}},
    {%- endif -%}
    {%- if item.RTOALPHA is not none -%}
        RTOALPHA={{item.RTOALPHA}},
    {%- endif -%}
    {%- if item.RTOBETA is not none -%}
        RTOBETA={{item.RTOBETA}},
    {%- endif -%}
    {%- if item.HBINTERVAL is not none -%}
        HBINTERVAL={{item.HBINTERVAL}},
    {%- endif -%}
    {%- if item.MAXASSOCRETR is not none -%}
        MAXASSOCRETR={{item.MAXASSOCRETR}},
    {%- endif -%}
    {%- if item.MAXPATHRETR is not none -%}
        MAXPATHRETR={{item.MAXPATHRETR}},
    {%- endif -%}
    {%- if item.MAXINSTREAMS is not none -%}
        MAXINSTREAMS={{item.MAXINSTREAMS}},
    {%- endif -%}
    {%- if item.MAXOUTSTREAMS is not none -%}
        MAXOUTSTREAMS={{item.MAXOUTSTREAMS}},
    {%- endif -%}
    {%- if item.CNGLEVELNO is not none -%}
        CNGLEVELNO={{item.CNGLEVELNO}},
    {%- endif -%}
    {%- if item.CNGLEVELLOW is not none -%}
        CNGLEVELLOW={{item.CNGLEVELLOW}},
    {%- endif -%}
    {%- if item.CNGLEVELHIGH is not none -%}
        CNGLEVELHIGH={{item.CNGLEVELHIGH}},
    {%- endif -%}
    {%- if item.CHKSUMTX is not none -%}
        CHKSUMTX={{item.CHKSUMTX}},
    {%- endif -%}
    {%- if item.CHKSUMRX is not none -%}
        CHKSUMRX={{item.CHKSUMRX}},
    {%- endif -%}
    {%- if item.CHKSUMTYPE is not none -%}
        CHKSUMTYPE={{item.CHKSUMTYPE}},
    {%- endif -%}
    {%- if item.BINDTMR is not none -%}
        BINDTMR={{item.BINDTMR}},
    {%- endif -%}
    {%- if item.DELAYTMRLEN is not none -%}
        DELAYTMRLEN={{item.DELAYTMRLEN}},
    {%- endif -%}
    {%- if item.IPV4MTU is not none -%}
        IPV4MTU={{item.IPV4MTU}},
    {%- endif -%}
    {%- if item.IPV6MTU is not none -%}
        IPV6MTU={{item.IPV6MTU}},
    {%- endif -%}
    {%- if item.SCTPPARANAME is not none -%}
        SCTPPARANAME="{{item.SCTPPARANAME}}",
    {%- endif -%}
    {%- if item.PKGERRFAULT is not none -%}
        PKGERRFAULT={{item.PKGERRFAULT}},
    {%- endif -%}
    {%- if item.PKGERRRECOVER is not none -%}
        PKGERRRECOVER={{item.PKGERRRECOVER}},
    {%- endif -%}
    {%- if item.MINRECVPKGNUM is not none -%}
        MINRECVPKGNUM={{item.MINRECVPKGNUM}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 3.5 配置Diameter链路数据。

##### 3.5.1 配置Diameter本端信息。

```jinja2
{%- for item in add_dmle_list -%}
    ADD DMLE:
    {#- --- 必选参数 --- -#}
    LOHSTNAME="{{item.LOHSTNAME}}",
    LORLMNAME="{{item.LORLMNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.LOINDEX is not none -%}
        LOINDEX={{item.LOINDEX}},
    {%- endif -%}
    {%- if item.PDTNAME is not none -%}
        PDTNAME="{{item.PDTNAME}}",
    {%- endif -%}
    {%- if item.LOINFONAME is not none -%}
        LOINFONAME="{{item.LOINFONAME}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

##### 3.5.2 配置Diameter对端信息。

```jinja2
{%- for item in add_dmpe_list -%}
    ADD DMPE:
    {#- --- 必选参数 --- -#}
    PEERIDX={{item.PEERIDX}},
    PEERHTNAM="{{item.PEERHTNAM}}",
    {#- --- 可选参数 --- -#}
    {%- if item.PEERNAM is not none -%}
        PEERNAM="{{item.PEERNAM}}",
    {%- endif -%}
    {%- if item.APPCAP is not none -%}
        APPCAP={{item.APPCAP}},
    {%- endif -%}
    {%- if item.CONGSW is not none -%}
        CONGSW={{item.CONGSW}},
    {%- endif -%}
    ;
{%- endfor -%}
```

##### 3.5.3 配置Diameter链路集信息。

```jinja2
{%- for item in add_dmlks_list -%}
    ADD DMLKS:
    {#- --- 必选参数 --- -#}
    LINKSIDX={{item.LINKSIDX}},
    LOCALIDX={{item.LOCALIDX}},
    PEERIDX={{item.PEERIDX}},
    {#- --- 可选参数 --- -#}
    {%- if item.LSSELMODE is not none -%}
        LSSELMODE={{item.LSSELMODE}},
    {%- endif -%}
    {%- if item.LINKSNAM is not none -%}
        LINKSNAM="{{item.LINKSNAM}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

##### 3.5.4 配置Diameter链路信息。

```jinja2
{%- for item in add_dmlnk_list -%}
    ADD DMLNK:
    {#- --- 必选参数 --- -#}
    LINKIDX={{item.LINKIDX}},
    LINKSIDX={{item.LINKSIDX}},
    SCTPINDX={{item.SCTPINDX}},
    {#- --- 可选参数 --- -#}
    {%- if item.VPNNAME is not none -%}
        VPNNAME="{{item.VPNNAME}}",
    {%- endif -%}
    {%- if item.IPTYPE is not none -%}
        IPTYPE={{item.IPTYPE}},
    {%- endif -%}
    {%- if item.PROTOTYPE is not none -%}
        PROTOTYPE={{item.PROTOTYPE}},
    {%- endif -%}
    {%- if item.LOCALPORT is not none -%}
        LOCALPORT={{item.LOCALPORT}},
    {%- endif -%}
    {%- if item.PEERPORT is not none -%}
        PEERPORT={{item.PEERPORT}},
    {%- endif -%}
    {%- if item.CLIORSER is not none -%}
        CLIORSER={{item.CLIORSER}},
    {%- endif -%}
    {%- if item.LINKNAM is not none -%}
        LINKNAM="{{item.LINKNAM}}",
    {%- endif -%}
    {%- if item.CROSSIPFLAG is not none -%}
        CROSSIPFLAG={{item.CROSSIPFLAG}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPTYPE=TPTADDR_TYPE_IPV4 时必选 --- -#}
    {%- if item.IPTYPE == 'TPTADDR_TYPE_IPV4' -%}
        LOCALIPV4_1="{{item.LOCALIPV4_1}}",
    {%- endif -%}
    {#- --- 条件必选：IPTYPE=TPTADDR_TYPE_IPV4 时必选 --- -#}
    {%- if item.IPTYPE == 'TPTADDR_TYPE_IPV4' -%}
        PEERIPV4_1="{{item.PEERIPV4_1}}",
    {%- endif -%}
    {#- --- 条件必选：IPTYPE=TPTADDR_TYPE_IPV6 时必选 --- -#}
    {%- if item.IPTYPE == 'TPTADDR_TYPE_IPV6' -%}
        LOCALIPV6_1="{{item.LOCALIPV6_1}}",
    {%- endif -%}
    {#- --- 条件必选：IPTYPE=TPTADDR_TYPE_IPV6 时必选 --- -#}
    {%- if item.IPTYPE == 'TPTADDR_TYPE_IPV6' -%}
        PEERIPV6_1="{{item.PEERIPV6_1}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：IPTYPE=TPTADDR_TYPE_IPV4 时可选 --- -#}
    {%- if item.IPTYPE == 'TPTADDR_TYPE_IPV4' -%}
        {%- if item.LOCALIPV4_2 is not none -%}
            LOCALIPV4_2="{{item.LOCALIPV4_2}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：IPTYPE=TPTADDR_TYPE_IPV4 时可选 --- -#}
    {%- if item.IPTYPE == 'TPTADDR_TYPE_IPV4' -%}
        {%- if item.PEERIPV4_2 is not none -%}
            PEERIPV4_2="{{item.PEERIPV4_2}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：IPTYPE=TPTADDR_TYPE_IPV6 时可选 --- -#}
    {%- if item.IPTYPE == 'TPTADDR_TYPE_IPV6' -%}
        {%- if item.LOCALIPV6_2 is not none -%}
            LOCALIPV6_2="{{item.LOCALIPV6_2}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：IPTYPE=TPTADDR_TYPE_IPV6 时可选 --- -#}
    {%- if item.IPTYPE == 'TPTADDR_TYPE_IPV6' -%}
        {%- if item.PEERIPV6_2 is not none -%}
            PEERIPV6_2="{{item.PEERIPV6_2}}",
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

##### 3.5.5 配置到HSS的主机路由。

```jinja2
{%- for item in add_dmhostrt_list -%}
    ADD DMHOSTRT:
    {#- --- 必选参数 --- -#}
    ROUTEIDX={{item.ROUTEIDX}},
    {#- --- 可选参数 --- -#}
    {%- if item.APPNAM is not none -%}
        APPNAM={{item.APPNAM}},
    {%- endif -%}
    {%- if item.RSELMODE is not none -%}
        RSELMODE={{item.RSELMODE}},
    {%- endif -%}
    {%- if item.PEERSEL is not none -%}
        PEERSEL={{item.PEERSEL}},
    {%- endif -%}
    {%- if item.ROUTENAM is not none -%}
        ROUTENAM="{{item.ROUTENAM}}",
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：PEERSEL=PEER_INDEX 时必选 --- -#}
    {%- if item.PEERSEL == 'PEER_INDEX' -%}
        PEERIDX={{item.PEERIDX}},
    {%- endif -%}
    {#- --- 条件必选：PEERSEL=PEER_HOST_NAME 时必选 --- -#}
    {%- if item.PEERSEL == 'PEER_HOST_NAME' -%}
        PEERHTNAM="{{item.PEERHTNAM}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：RSELMODE=SELMODE_MASTER_SLAVE/SELMODE_PRIORITY_WEIGHT 时可选 --- -#}
    {%- if item.RSELMODE in ['SELMODE_MASTER_SLAVE', 'SELMODE_PRIORITY_WEIGHT'] -%}
        {%- if item.PRIORITY is not none -%}
            PRIORITY={{item.PRIORITY}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：RSELMODE=SELMODE_PRIORITY_WEIGHT 时可选 --- -#}
    {%- if item.RSELMODE == 'SELMODE_PRIORITY_WEIGHT' -%}
        {%- if item.WEIGHT is not none -%}
            WEIGHT={{item.WEIGHT}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

##### 3.5.6 将主机路由加入Diameter路由组中。

```jinja2
{%- for item in add_dmrtgrp_list -%}
    ADD DMRTGRP:
    {#- --- 必选参数 --- -#}
    GRPIDX={{item.GRPIDX}},
    {#- --- 可选参数 --- -#}
    {%- if item.RTMODE is not none -%}
        RTMODE={{item.RTMODE}},
    {%- endif -%}
    {%- if item.RTPRIMODE is not none -%}
        RTPRIMODE={{item.RTPRIMODE}},
    {%- endif -%}
    {%- if item.ROUTEGRPNAM is not none -%}
        ROUTEGRPNAM="{{item.ROUTEGRPNAM}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：RTMODE=REALM_ROUTE 时可选 --- -#}
    {%- if item.RTMODE == 'REALM_ROUTE' -%}
        {%- if item.PEERIDX is not none -%}
            PEERIDX={{item.PEERIDX}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件必选/可选参数 --- -#}
    {#- --- 路由索引: 条件必选(路由模式=HOST_ROUTE) / 条件可选(路由模式=REALM_ROUTE) --- -#}
    {%- if (item.RTMODE == 'HOST_ROUTE') -%}
        ROUTEIDX={{item.ROUTEIDX}},
    {%- elif (item.RTMODE == 'REALM_ROUTE') -%}
        {%- if item.ROUTEIDX is not none -%}
            ROUTEIDX={{item.ROUTEIDX}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

##### 3.5.7 配置IMSI与HSS的映射关系，用户可以根据改映射关系查找IMSI归属哪个HSS信息。

```jinja2
{%- for item in add_imsihss_list -%}
    ADD IMSIHSS:
    {#- --- 必选参数 --- -#}
    IMSIPRE="{{item.IMSIPRE}}",
    HSSRLM="{{item.HSSRLM}}",
    {#- --- 可选参数 --- -#}
    {%- if item.GRPIDX is not none -%}
        GRPIDX={{item.GRPIDX}},
    {%- endif -%}
    {%- if item.MNNAME is not none -%}
        MNNAME="{{item.MNNAME}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 配置S1-MME接口数据。

#### 4.1 配置动态路由OSPF。

##### 4.1.1 配置VPN实例。

```jinja2
{%- for item in add_l3vpninst_list_1 -%}
    ADD L3VPNINST:
    {#- --- 必选参数 --- -#}
    VRFNAME="{{item.VRFNAME}}",
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_vpninstaf_list_1 -%}
    ADD VPNINSTAF:
    {#- --- 必选参数 --- -#}
    VRFNAME="{{item.VRFNAME}}",
    AFTYPE={{item.AFTYPE}},
    ;
{%- endfor -%}
```

##### 4.1.2 配置主接口的管理状态为up。

```jinja2
{%- for item in mod_interface_list_4 -%}
    MOD INTERFACE:
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
    {%- if item.IFSTATITVL is not none -%}
        IFSTATITVL={{item.IFSTATITVL}},
    {%- endif -%}
    ;
{%- endfor -%}
```

##### 4.1.3 配置以太网接口。

```jinja2
{%- for item in add_interface_list_5 -%}
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
    {%- if item.IFSTATITVL is not none -%}
        IFSTATITVL={{item.IFSTATITVL}},
    {%- endif -%}
    ;
{%- endfor -%}
```

##### 4.1.4 增加接口绑定VPN。

```jinja2
{%- for item in add_ipbindvpn_list_5 -%}
    ADD IPBINDVPN:
    {#- --- 必选参数 --- -#}
    IFNAME="{{item.IFNAME}}",
    VRFNAME="{{item.VRFNAME}}",
    ;
{%- endfor -%}
```

##### 4.1.5 在以太网子接口上关联VLAN ID。

```jinja2
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
```

##### 4.1.6 配置外联口的物理IP。

```jinja2
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
```

##### 4.1.7 创建OSPF进程。

```jinja2
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
    {%- if item.SILENTALLFLAG is not none -%}
        SILENTALLFLAG={{item.SILENTALLFLAG}},
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
    {%- if item.RFC1583COMPFLG is not none -%}
        RFC1583COMPFLG={{item.RFC1583COMPFLG}},
    {%- endif -%}
    {%- if item.ROUTAGFLAG is not none -%}
        ROUTAGFLAG={{item.ROUTAGFLAG}},
    {%- endif -%}
    {%- if item.BANDWIDTHREF is not none -%}
        BANDWIDTHREF={{item.BANDWIDTHREF}},
    {%- endif -%}
    {%- if item.RXMTLIMITENABLE is not none -%}
        RXMTLIMITENABLE={{item.RXMTLIMITENABLE}},
    {%- endif -%}
    {%- if item.OPAQCAPFLG is not none -%}
        OPAQCAPFLG={{item.OPAQCAPFLG}},
    {%- endif -%}
    {%- if item.LSAARRINTVFLAG is not none -%}
        LSAARRINTVFLAG={{item.LSAARRINTVFLAG}},
    {%- endif -%}
    {%- if item.LSAORIGINSTFLAG is not none -%}
        LSAORIGINSTFLAG={{item.LSAORIGINSTFLAG}},
    {%- endif -%}
    {%- if item.VPNINSCAPSIMFLG is not none -%}
        VPNINSCAPSIMFLG={{item.VPNINSCAPSIMFLG}},
    {%- endif -%}
    {%- if item.STUBROUFLG is not none -%}
        STUBROUFLG={{item.STUBROUFLG}},
    {%- endif -%}
    {%- if item.SAFESYNCFLG is not none -%}
        SAFESYNCFLG={{item.SAFESYNCFLG}},
    {%- endif -%}
    {%- if item.RTTAGDISFLAG is not none -%}
        RTTAGDISFLAG={{item.RTTAGDISFLAG}},
    {%- endif -%}
    {%- if item.ECAROUTEFLAG is not none -%}
        ECAROUTEFLAG={{item.ECAROUTEFLAG}},
    {%- endif -%}
    {%- if item.DOMAINNULLFLAG is not none -%}
        DOMAINNULLFLAG={{item.DOMAINNULLFLAG}},
    {%- endif -%}
    {%- if item.SUPPREACH is not none -%}
        SUPPREACH={{item.SUPPREACH}},
    {%- endif -%}
    {%- if item.SPFCONSERVFLAG is not none -%}
        SPFCONSERVFLAG={{item.SPFCONSERVFLAG}},
    {%- endif -%}
    {%- if item.SHAMHELLOFLAG is not none -%}
        SHAMHELLOFLAG={{item.SHAMHELLOFLAG}},
    {%- endif -%}
    {%- if item.MPLSLDPAUTOCFG is not none -%}
        MPLSLDPAUTOCFG={{item.MPLSLDPAUTOCFG}},
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
    {#- --- 条件必选：ROUTAGFLAG=TRUE 时必选 --- -#}
    {%- if item.ROUTAGFLAG == 'TRUE' -%}
        ROUTAG={{item.ROUTAG}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：LSAORIGINSTFLAG=FALSE 时可选 --- -#}
    {%- if item.LSAORIGINSTFLAG == 'FALSE' -%}
        {%- if item.LSAORIGINTV is not none -%}
            LSAORIGINTV={{item.LSAORIGINTV}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：LSAORIGINSTFLAG=FALSE 时可选 --- -#}
    {%- if item.LSAORIGINSTFLAG == 'FALSE' -%}
        {%- if item.LSAORIGMAXINTV is not none -%}
            LSAORIGMAXINTV={{item.LSAORIGMAXINTV}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：LSAORIGINSTFLAG=FALSE 时可选 --- -#}
    {%- if item.LSAORIGINSTFLAG == 'FALSE' -%}
        {%- if item.LSAORIGSTARINTV is not none -%}
            LSAORIGSTARINTV={{item.LSAORIGSTARINTV}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：LSAORIGINSTFLAG=FALSE 时可选 --- -#}
    {%- if item.LSAORIGINSTFLAG == 'FALSE' -%}
        {%- if item.LSAORIGHLDINTV is not none -%}
            LSAORIGHLDINTV={{item.LSAORIGHLDINTV}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：RXMTLIMITENABLE=TRUE 时可选 --- -#}
    {%- if item.RXMTLIMITENABLE == 'TRUE' -%}
        {%- if item.RETRANSLIMIT is not none -%}
            RETRANSLIMIT={{item.RETRANSLIMIT}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：STUBROUFLG=StubOnBoot/StubOnHand 时可选 --- -#}
    {%- if item.STUBROUFLG in ['StubOnBoot', 'StubOnHand'] -%}
        {%- if item.STUBROUINCSTUB is not none -%}
            STUBROUINCSTUB={{item.STUBROUINCSTUB}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：STUBROUFLG=StubOnBoot 时可选 --- -#}
    {%- if item.STUBROUFLG == 'StubOnBoot' -%}
        {%- if item.STUBROUSTUPINTV is not none -%}
            STUBROUSTUPINTV={{item.STUBROUSTUPINTV}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

##### 4.1.8 增加OSPF区域。

```jinja2
{%- for item in add_ospfarea_list_1 -%}
    ADD OSPFAREA:
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
    {#- --- 条件可选：AREATYPE=Stub/NSSA 时可选 --- -#}
    {%- if item.AREATYPE in ['Stub', 'NSSA'] -%}
        {%- if item.DEFAULTCOST is not none -%}
            DEFAULTCOST={{item.DEFAULTCOST}},
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

##### 4.1.9 增加运行OSPF协议的接口。

```jinja2
{%- for item in add_ospfnetwork_list_3 -%}
    ADD OSPFNETWORK:
    {#- --- 必选参数 --- -#}
    PROCID={{item.PROCID}},
    AREAID="{{item.AREAID}}",
    IPADDRESS="{{item.IPADDRESS}}",
    WILDCARDMASK="{{item.WILDCARDMASK}}",
    ;
{%- endfor -%}
```

##### 4.1.10 设置OSPF引入路由类型。

```jinja2
{%- for item in add_ospfimportroute_list_1 -%}
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
```

#### 4.2 配置BFD。

##### 4.2.1 全局激活BFD。上文已配置，此处无需重复配置。

##### 4.2.2 以接口粒度配置动态BFD。

```jinja2
{%- for item in add_ospfinterface_list_4 -%}
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
    {%- if item.TIMERCONSERFLAG is not none -%}
        TIMERCONSERFLAG={{item.TIMERCONSERFLAG}},
    {%- endif -%}
    {%- if item.CONFIGCOST is not none -%}
        CONFIGCOST={{item.CONFIGCOST}},
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
    {%- if item.VIRTUALSYSFLAG is not none -%}
        VIRTUALSYSFLAG={{item.VIRTUALSYSFLAG}},
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
```

#### 4.3 配置S1-MME接口业务IP。

```jinja2
{%- for item in add_serviceip_list_2 -%}
    ADD SERVICEIP:
    {#- --- 必选参数 --- -#}
    IPVERSION={{item.IPVERSION}},
    {#- --- 可选参数 --- -#}
    {%- if item.VPNINSTNAME is not none -%}
        VPNINSTNAME="{{item.VPNINSTNAME}}",
    {%- endif -%}
    {%- if item.DESC is not none -%}
        DESC="{{item.DESC}}",
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPVERSION=IPv4 时必选 --- -#}
    {%- if item.IPVERSION == 'IPv4' -%}
        SERVICEIPV4="{{item.SERVICEIPV4}}",
    {%- endif -%}
    {#- --- 条件必选：IPVERSION=IPv6 时必选 --- -#}
    {%- if item.IPVERSION == 'IPv6' -%}
        SERVICEIPV6="{{item.SERVICEIPV6}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：IPVERSION=IPv6 时可选 --- -#}
    {%- if item.IPVERSION == 'IPv6' -%}
        {%- if item.IPV6MTU is not none -%}
            IPV6MTU={{item.IPV6MTU}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 4.4 配置S1-MME接口SCTP协议参数模板。

```jinja2
{%- for item in add_sctppara_list_1 -%}
    ADD SCTPPARA:
    {#- --- 必选参数 --- -#}
    SCTPPARAINDEX={{item.SCTPPARAINDEX}},
    {#- --- 可选参数 --- -#}
    {%- if item.RTOMIN is not none -%}
        RTOMIN={{item.RTOMIN}},
    {%- endif -%}
    {%- if item.RTOMAX is not none -%}
        RTOMAX={{item.RTOMAX}},
    {%- endif -%}
    {%- if item.RTOINIT is not none -%}
        RTOINIT={{item.RTOINIT}},
    {%- endif -%}
    {%- if item.RTOALPHA is not none -%}
        RTOALPHA={{item.RTOALPHA}},
    {%- endif -%}
    {%- if item.RTOBETA is not none -%}
        RTOBETA={{item.RTOBETA}},
    {%- endif -%}
    {%- if item.HBINTERVAL is not none -%}
        HBINTERVAL={{item.HBINTERVAL}},
    {%- endif -%}
    {%- if item.MAXASSOCRETR is not none -%}
        MAXASSOCRETR={{item.MAXASSOCRETR}},
    {%- endif -%}
    {%- if item.MAXPATHRETR is not none -%}
        MAXPATHRETR={{item.MAXPATHRETR}},
    {%- endif -%}
    {%- if item.MAXINSTREAMS is not none -%}
        MAXINSTREAMS={{item.MAXINSTREAMS}},
    {%- endif -%}
    {%- if item.MAXOUTSTREAMS is not none -%}
        MAXOUTSTREAMS={{item.MAXOUTSTREAMS}},
    {%- endif -%}
    {%- if item.CNGLEVELNO is not none -%}
        CNGLEVELNO={{item.CNGLEVELNO}},
    {%- endif -%}
    {%- if item.CNGLEVELLOW is not none -%}
        CNGLEVELLOW={{item.CNGLEVELLOW}},
    {%- endif -%}
    {%- if item.CNGLEVELHIGH is not none -%}
        CNGLEVELHIGH={{item.CNGLEVELHIGH}},
    {%- endif -%}
    {%- if item.CHKSUMTX is not none -%}
        CHKSUMTX={{item.CHKSUMTX}},
    {%- endif -%}
    {%- if item.CHKSUMRX is not none -%}
        CHKSUMRX={{item.CHKSUMRX}},
    {%- endif -%}
    {%- if item.CHKSUMTYPE is not none -%}
        CHKSUMTYPE={{item.CHKSUMTYPE}},
    {%- endif -%}
    {%- if item.BINDTMR is not none -%}
        BINDTMR={{item.BINDTMR}},
    {%- endif -%}
    {%- if item.DELAYTMRLEN is not none -%}
        DELAYTMRLEN={{item.DELAYTMRLEN}},
    {%- endif -%}
    {%- if item.IPV4MTU is not none -%}
        IPV4MTU={{item.IPV4MTU}},
    {%- endif -%}
    {%- if item.IPV6MTU is not none -%}
        IPV6MTU={{item.IPV6MTU}},
    {%- endif -%}
    {%- if item.SCTPPARANAME is not none -%}
        SCTPPARANAME="{{item.SCTPPARANAME}}",
    {%- endif -%}
    {%- if item.PKGERRFAULT is not none -%}
        PKGERRFAULT={{item.PKGERRFAULT}},
    {%- endif -%}
    {%- if item.PKGERRRECOVER is not none -%}
        PKGERRRECOVER={{item.PKGERRRECOVER}},
    {%- endif -%}
    {%- if item.MINRECVPKGNUM is not none -%}
        MINRECVPKGNUM={{item.MINRECVPKGNUM}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 4.5 配置SIAP链路本地实体。其中LOCALIPV4\_1、LOCALIPV4\_2为S1-MME接口的业务IP。

```jinja2
{%- for item in add_s1aple_list -%}
    ADD S1APLE:
    {#- --- 必选参数 --- -#}
    LLEINDEX={{item.LLEINDEX}},
    SCTPINDEX={{item.SCTPINDEX}},
    {#- --- 可选参数 --- -#}
    {%- if item.IPTYPE is not none -%}
        IPTYPE={{item.IPTYPE}},
    {%- endif -%}
    {%- if item.LOCALPORT is not none -%}
        LOCALPORT={{item.LOCALPORT}},
    {%- endif -%}
    {%- if item.CROSSIPFLAG is not none -%}
        CROSSIPFLAG={{item.CROSSIPFLAG}},
    {%- endif -%}
    {%- if item.LLNAME is not none -%}
        LLNAME="{{item.LLNAME}}",
    {%- endif -%}
    {%- if item.VPNNAME is not none -%}
        VPNNAME="{{item.VPNNAME}}",
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPTYPE=TPTADDR_TYPE_IPV4 时必选 --- -#}
    {%- if item.IPTYPE == 'TPTADDR_TYPE_IPV4' -%}
        LOCALIPV4_1="{{item.LOCALIPV4_1}}",
    {%- endif -%}
    {#- --- 条件必选：IPTYPE=TPTADDR_TYPE_IPV6 时必选 --- -#}
    {%- if item.IPTYPE == 'TPTADDR_TYPE_IPV6' -%}
        LOCALIPV6_1="{{item.LOCALIPV6_1}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：IPTYPE=TPTADDR_TYPE_IPV4 时可选 --- -#}
    {%- if item.IPTYPE == 'TPTADDR_TYPE_IPV4' -%}
        {%- if item.LOCALIPV4_2 is not none -%}
            LOCALIPV4_2="{{item.LOCALIPV4_2}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：IPTYPE=TPTADDR_TYPE_IPV6 时可选 --- -#}
    {%- if item.IPTYPE == 'TPTADDR_TYPE_IPV6' -%}
        {%- if item.LOCALIPV6_2 is not none -%}
            LOCALIPV6_2="{{item.LOCALIPV6_2}}",
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 5 配置S11/S10/GnGp接口数据。

#### 5.1 配置动态路由OSPF。

##### 5.1.1 配置VPN实例。

```jinja2
{%- for item in add_l3vpninst_list_2 -%}
    ADD L3VPNINST:
    {#- --- 必选参数 --- -#}
    VRFNAME="{{item.VRFNAME}}",
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_vpninstaf_list_2 -%}
    ADD VPNINSTAF:
    {#- --- 必选参数 --- -#}
    VRFNAME="{{item.VRFNAME}}",
    AFTYPE={{item.AFTYPE}},
    ;
{%- endfor -%}
```

##### 5.1.2 配置主接口的管理状态为up。

```jinja2
{%- for item in mod_interface_list_8 -%}
    MOD INTERFACE:
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
    {%- if item.IFSTATITVL is not none -%}
        IFSTATITVL={{item.IFSTATITVL}},
    {%- endif -%}
    ;
{%- endfor -%}
```

##### 5.1.3 配置以太网接口。

```jinja2
{%- for item in add_interface_list_10 -%}
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
    {%- if item.IFSTATITVL is not none -%}
        IFSTATITVL={{item.IFSTATITVL}},
    {%- endif -%}
    ;
{%- endfor -%}
```

##### 5.1.4 增加接口绑定VPN。

```jinja2
{%- for item in add_ipbindvpn_list_10 -%}
    ADD IPBINDVPN:
    {#- --- 必选参数 --- -#}
    IFNAME="{{item.IFNAME}}",
    VRFNAME="{{item.VRFNAME}}",
    ;
{%- endfor -%}
```

##### 5.1.5 在以太网子接口上关联VLAN ID。

```jinja2
{%- for item in add_ethsubif_list_8 -%}
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
```

##### 5.1.6 配置外联口的物理IP。

```jinja2
{%- for item in add_ifipv4address_list_10 -%}
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
```

##### 5.1.7 创建OSPF进程。

```jinja2
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
    {%- if item.SILENTALLFLAG is not none -%}
        SILENTALLFLAG={{item.SILENTALLFLAG}},
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
    {%- if item.RFC1583COMPFLG is not none -%}
        RFC1583COMPFLG={{item.RFC1583COMPFLG}},
    {%- endif -%}
    {%- if item.ROUTAGFLAG is not none -%}
        ROUTAGFLAG={{item.ROUTAGFLAG}},
    {%- endif -%}
    {%- if item.BANDWIDTHREF is not none -%}
        BANDWIDTHREF={{item.BANDWIDTHREF}},
    {%- endif -%}
    {%- if item.RXMTLIMITENABLE is not none -%}
        RXMTLIMITENABLE={{item.RXMTLIMITENABLE}},
    {%- endif -%}
    {%- if item.OPAQCAPFLG is not none -%}
        OPAQCAPFLG={{item.OPAQCAPFLG}},
    {%- endif -%}
    {%- if item.LSAARRINTVFLAG is not none -%}
        LSAARRINTVFLAG={{item.LSAARRINTVFLAG}},
    {%- endif -%}
    {%- if item.LSAORIGINSTFLAG is not none -%}
        LSAORIGINSTFLAG={{item.LSAORIGINSTFLAG}},
    {%- endif -%}
    {%- if item.VPNINSCAPSIMFLG is not none -%}
        VPNINSCAPSIMFLG={{item.VPNINSCAPSIMFLG}},
    {%- endif -%}
    {%- if item.STUBROUFLG is not none -%}
        STUBROUFLG={{item.STUBROUFLG}},
    {%- endif -%}
    {%- if item.SAFESYNCFLG is not none -%}
        SAFESYNCFLG={{item.SAFESYNCFLG}},
    {%- endif -%}
    {%- if item.RTTAGDISFLAG is not none -%}
        RTTAGDISFLAG={{item.RTTAGDISFLAG}},
    {%- endif -%}
    {%- if item.ECAROUTEFLAG is not none -%}
        ECAROUTEFLAG={{item.ECAROUTEFLAG}},
    {%- endif -%}
    {%- if item.DOMAINNULLFLAG is not none -%}
        DOMAINNULLFLAG={{item.DOMAINNULLFLAG}},
    {%- endif -%}
    {%- if item.SUPPREACH is not none -%}
        SUPPREACH={{item.SUPPREACH}},
    {%- endif -%}
    {%- if item.SPFCONSERVFLAG is not none -%}
        SPFCONSERVFLAG={{item.SPFCONSERVFLAG}},
    {%- endif -%}
    {%- if item.SHAMHELLOFLAG is not none -%}
        SHAMHELLOFLAG={{item.SHAMHELLOFLAG}},
    {%- endif -%}
    {%- if item.MPLSLDPAUTOCFG is not none -%}
        MPLSLDPAUTOCFG={{item.MPLSLDPAUTOCFG}},
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
    {#- --- 条件必选：ROUTAGFLAG=TRUE 时必选 --- -#}
    {%- if item.ROUTAGFLAG == 'TRUE' -%}
        ROUTAG={{item.ROUTAG}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：LSAORIGINSTFLAG=FALSE 时可选 --- -#}
    {%- if item.LSAORIGINSTFLAG == 'FALSE' -%}
        {%- if item.LSAORIGINTV is not none -%}
            LSAORIGINTV={{item.LSAORIGINTV}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：LSAORIGINSTFLAG=FALSE 时可选 --- -#}
    {%- if item.LSAORIGINSTFLAG == 'FALSE' -%}
        {%- if item.LSAORIGMAXINTV is not none -%}
            LSAORIGMAXINTV={{item.LSAORIGMAXINTV}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：LSAORIGINSTFLAG=FALSE 时可选 --- -#}
    {%- if item.LSAORIGINSTFLAG == 'FALSE' -%}
        {%- if item.LSAORIGSTARINTV is not none -%}
            LSAORIGSTARINTV={{item.LSAORIGSTARINTV}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：LSAORIGINSTFLAG=FALSE 时可选 --- -#}
    {%- if item.LSAORIGINSTFLAG == 'FALSE' -%}
        {%- if item.LSAORIGHLDINTV is not none -%}
            LSAORIGHLDINTV={{item.LSAORIGHLDINTV}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：RXMTLIMITENABLE=TRUE 时可选 --- -#}
    {%- if item.RXMTLIMITENABLE == 'TRUE' -%}
        {%- if item.RETRANSLIMIT is not none -%}
            RETRANSLIMIT={{item.RETRANSLIMIT}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：STUBROUFLG=StubOnBoot/StubOnHand 时可选 --- -#}
    {%- if item.STUBROUFLG in ['StubOnBoot', 'StubOnHand'] -%}
        {%- if item.STUBROUINCSTUB is not none -%}
            STUBROUINCSTUB={{item.STUBROUINCSTUB}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：STUBROUFLG=StubOnBoot 时可选 --- -#}
    {%- if item.STUBROUFLG == 'StubOnBoot' -%}
        {%- if item.STUBROUSTUPINTV is not none -%}
            STUBROUSTUPINTV={{item.STUBROUSTUPINTV}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

##### 5.1.8 增加OSPF区域。

```jinja2
{%- for item in add_ospfarea_list_2 -%}
    ADD OSPFAREA:
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
    {#- --- 条件可选：AREATYPE=Stub/NSSA 时可选 --- -#}
    {%- if item.AREATYPE in ['Stub', 'NSSA'] -%}
        {%- if item.DEFAULTCOST is not none -%}
            DEFAULTCOST={{item.DEFAULTCOST}},
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

##### 5.1.9 增加运行OSPF协议的接口。

```jinja2
{%- for item in add_ospfnetwork_list_6 -%}
    ADD OSPFNETWORK:
    {#- --- 必选参数 --- -#}
    PROCID={{item.PROCID}},
    AREAID="{{item.AREAID}}",
    IPADDRESS="{{item.IPADDRESS}}",
    WILDCARDMASK="{{item.WILDCARDMASK}}",
    ;
{%- endfor -%}
```

##### 5.1.10 设置OSPF引入路由类型。

```jinja2
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
```

#### 5.2 配置BFD。

##### 5.2.1 全局激活BFD。上文已配置，此处无需重复配置。

##### 5.2.2 以接口粒度配置动态BFD。

```jinja2
{%- for item in add_ospfinterface_list_8 -%}
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
    {%- if item.TIMERCONSERFLAG is not none -%}
        TIMERCONSERFLAG={{item.TIMERCONSERFLAG}},
    {%- endif -%}
    {%- if item.CONFIGCOST is not none -%}
        CONFIGCOST={{item.CONFIGCOST}},
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
    {%- if item.VIRTUALSYSFLAG is not none -%}
        VIRTUALSYSFLAG={{item.VIRTUALSYSFLAG}},
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
```

#### 5.3 增加业务IP。

##### 5.3.1 配置S10接口业务IP。

```jinja2
{%- for item in add_serviceip_list_4 -%}
    ADD SERVICEIP:
    {#- --- 必选参数 --- -#}
    IPVERSION={{item.IPVERSION}},
    {#- --- 可选参数 --- -#}
    {%- if item.VPNINSTNAME is not none -%}
        VPNINSTNAME="{{item.VPNINSTNAME}}",
    {%- endif -%}
    {%- if item.DESC is not none -%}
        DESC="{{item.DESC}}",
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPVERSION=IPv4 时必选 --- -#}
    {%- if item.IPVERSION == 'IPv4' -%}
        SERVICEIPV4="{{item.SERVICEIPV4}}",
    {%- endif -%}
    {#- --- 条件必选：IPVERSION=IPv6 时必选 --- -#}
    {%- if item.IPVERSION == 'IPv6' -%}
        SERVICEIPV6="{{item.SERVICEIPV6}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：IPVERSION=IPv6 时可选 --- -#}
    {%- if item.IPVERSION == 'IPv6' -%}
        {%- if item.IPV6MTU is not none -%}
            IPV6MTU={{item.IPV6MTU}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

##### 5.3.2 配置S11接口业务IP。

```jinja2
{%- for item in add_serviceip_list_5 -%}
    ADD SERVICEIP:
    {#- --- 必选参数 --- -#}
    IPVERSION={{item.IPVERSION}},
    {#- --- 可选参数 --- -#}
    {%- if item.VPNINSTNAME is not none -%}
        VPNINSTNAME="{{item.VPNINSTNAME}}",
    {%- endif -%}
    {%- if item.DESC is not none -%}
        DESC="{{item.DESC}}",
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPVERSION=IPv4 时必选 --- -#}
    {%- if item.IPVERSION == 'IPv4' -%}
        SERVICEIPV4="{{item.SERVICEIPV4}}",
    {%- endif -%}
    {#- --- 条件必选：IPVERSION=IPv6 时必选 --- -#}
    {%- if item.IPVERSION == 'IPv6' -%}
        SERVICEIPV6="{{item.SERVICEIPV6}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：IPVERSION=IPv6 时可选 --- -#}
    {%- if item.IPVERSION == 'IPv6' -%}
        {%- if item.IPV6MTU is not none -%}
            IPV6MTU={{item.IPV6MTU}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

##### 5.3.3 配置Gn接口业务IP。

```jinja2
{%- for item in add_serviceip_list_6 -%}
    ADD SERVICEIP:
    {#- --- 必选参数 --- -#}
    IPVERSION={{item.IPVERSION}},
    {#- --- 可选参数 --- -#}
    {%- if item.VPNINSTNAME is not none -%}
        VPNINSTNAME="{{item.VPNINSTNAME}}",
    {%- endif -%}
    {%- if item.DESC is not none -%}
        DESC="{{item.DESC}}",
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPVERSION=IPv4 时必选 --- -#}
    {%- if item.IPVERSION == 'IPv4' -%}
        SERVICEIPV4="{{item.SERVICEIPV4}}",
    {%- endif -%}
    {#- --- 条件必选：IPVERSION=IPv6 时必选 --- -#}
    {%- if item.IPVERSION == 'IPv6' -%}
        SERVICEIPV6="{{item.SERVICEIPV6}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：IPVERSION=IPv6 时可选 --- -#}
    {%- if item.IPVERSION == 'IPv6' -%}
        {%- if item.IPV6MTU is not none -%}
            IPV6MTU={{item.IPV6MTU}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 5.4 配置GTP数据。

##### 5.4.1 增加GTP-C本地实体。

```jinja2
{%- for item in add_gtpcle_list -%}
    ADD GTPCLE:
    {#- --- 必选参数 --- -#}
    IPTYPE={{item.IPTYPE}},
    {#- --- 可选参数 --- -#}
    {%- if item.GROUPID is not none -%}
        GROUPID={{item.GROUPID}},
    {%- endif -%}
    {%- if item.VPNNAME is not none -%}
        VPNNAME="{{item.VPNNAME}}",
    {%- endif -%}
    {%- if item.DESC is not none -%}
        DESC="{{item.DESC}}",
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPTYPE=TPTADDR_TYPE_IPV4 时必选 --- -#}
    {%- if item.IPTYPE == 'TPTADDR_TYPE_IPV4' -%}
        LEIPV4="{{item.LEIPV4}}",
    {%- endif -%}
    {#- --- 条件必选：IPTYPE=TPTADDR_TYPE_IPV6 时必选 --- -#}
    {%- if item.IPTYPE == 'TPTADDR_TYPE_IPV6' -%}
        LEIPV6="{{item.LEIPV6}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

##### 5.4.2 为S11、Gn接口配置GTP-U本地实体。

```jinja2
{%- for item in add_gtpule_list -%}
    ADD GTPULE:
    {#- --- 必选参数 --- -#}
    IPTYPE={{item.IPTYPE}},
    {#- --- 可选参数 --- -#}
    {%- if item.GROUPID is not none -%}
        GROUPID={{item.GROUPID}},
    {%- endif -%}
    {%- if item.VPNNAME is not none -%}
        VPNNAME="{{item.VPNNAME}}",
    {%- endif -%}
    {%- if item.DESC is not none -%}
        DESC="{{item.DESC}}",
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPTYPE=TPTADDR_TYPE_IPV4 时必选 --- -#}
    {%- if item.IPTYPE == 'TPTADDR_TYPE_IPV4' -%}
        LEIPV4="{{item.LEIPV4}}",
    {%- endif -%}
    {#- --- 条件必选：IPTYPE=TPTADDR_TYPE_IPV6 时必选 --- -#}
    {%- if item.IPTYPE == 'TPTADDR_TYPE_IPV6' -%}
        LEIPV6="{{item.LEIPV6}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

##### 5.4.3 配置GTP路径管理参数。

```jinja2
{%- for item in set_ugtp_list -%}
    SET UGTP:
    {#- --- 可选参数 --- -#}
    {%- if item.ICI is not none -%}
        ICI={{item.ICI}},
    {%- endif -%}
    {%- if item.SSI is not none -%}
        SSI={{item.SSI}},
    {%- endif -%}
    {%- if item.MSI is not none -%}
        MSI={{item.MSI}},
    {%- endif -%}
    {%- if item.GMSI is not none -%}
        GMSI={{item.GMSI}},
    {%- endif -%}
    {%- if item.PATHVERCHKINT is not none -%}
        PATHVERCHKINT={{item.PATHVERCHKINT}},
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in set_gtppub_list -%}
    SET GTPPUB:
    {#- --- 可选参数 --- -#}
    {%- if item.PRVEXT is not none -%}
        PRVEXT={{item.PRVEXT}},
    {%- endif -%}
    {%- if item.ECHOSIG is not none -%}
        ECHOSIG={{item.ECHOSIG}},
    {%- endif -%}
    {%- if item.EI is not none -%}
        EI={{item.EI}},
    {%- endif -%}
    {%- if item.V2EI is not none -%}
        V2EI={{item.V2EI}},
    {%- endif -%}
    {%- if item.OTSIE is not none -%}
        OTSIE={{item.OTSIE}},
    {%- endif -%}
    {%- if item.POTHD is not none -%}
        POTHD={{item.POTHD}},
    {%- endif -%}
    {%- if item.PNTHD is not none -%}
        PNTHD={{item.PNTHD}},
    {%- endif -%}
    {%- if item.PCTHD is not none -%}
        PCTHD={{item.PCTHD}},
    {%- endif -%}
    {%- if item.PRTHD is not none -%}
        PRTHD={{item.PRTHD}},
    {%- endif -%}
    {%- if item.PEID is not none -%}
        PEID={{item.PEID}},
    {%- endif -%}
    {%- if item.PE is not none -%}
        PE="{{item.PE}}",
    {%- endif -%}
    {%- if item.GTPEXT is not none -%}
        GTPEXT={{item.GTPEXT}},
    {%- endif -%}
    {%- if item.GTPSUPEXTLIST is not none -%}
        GTPSUPEXTLIST={{item.GTPSUPEXTLIST}},
    {%- endif -%}
    {%- if item.GTPEXLEN is not none -%}
        GTPEXLEN={{item.GTPEXLEN}},
    {%- endif -%}
    {%- if item.GTPVER is not none -%}
        GTPVER={{item.GTPVER}},
    {%- endif -%}
    {%- if item.POOLSRCPORTSW is not none -%}
        POOLSRCPORTSW={{item.POOLSRCPORTSW}},
    {%- endif -%}
    {%- if item.PEERRECOVERYSW is not none -%}
        PEERRECOVERYSW={{item.PEERRECOVERYSW}},
    {%- endif -%}
    {%- if item.PATHDOWNDEASW is not none -%}
        PATHDOWNDEASW={{item.PATHDOWNDEASW}},
    {%- endif -%}
    {%- if item.PATHVERDETECTSW is not none -%}
        PATHVERDETECTSW={{item.PATHVERDETECTSW}},
    {%- endif -%}
    {%- if item.DNSGTPCPATHFILTERSW is not none -%}
        DNSGTPCPATHFILTERSW={{item.DNSGTPCPATHFILTERSW}},
    {%- endif -%}
    {%- if item.LOCRECOVERYSW is not none -%}
        LOCRECOVERYSW={{item.LOCRECOVERYSW}},
    {%- endif -%}
    {%- if item.UDPCHKSW is not none -%}
        UDPCHKSW={{item.UDPCHKSW}},
    {%- endif -%}
    ;
{%- endfor -%}
```

##### 5.4.4 配置DNS服务器。

```jinja2
{%- for item in add_dnss_list -%}
    ADD DNSS:
    {#- --- 必选参数 --- -#}
    PRI={{item.PRI}},
    {#- --- 可选参数 --- -#}
    {%- if item.GRPID is not none -%}
        GRPID={{item.GRPID}},
    {%- endif -%}
    {%- if item.DNSSNAME is not none -%}
        DNSSNAME="{{item.DNSSNAME}}",
    {%- endif -%}
    {%- if item.PRO is not none -%}
        PRO={{item.PRO}},
    {%- endif -%}
    {%- if item.IPT is not none -%}
        IPT={{item.IPT}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPT=IPV4 时必选 --- -#}
    {%- if item.IPT == 'IPV4' -%}
        IP="{{item.IP}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

##### 5.4.5 增加DNS本端实体。

```jinja2
{%- for item in add_dnsle_list -%}
    ADD DNSLE:
    {#- --- 必选参数 --- -#}
    IPT={{item.IPT}},
    LOCPORT={{item.LOCPORT}},
    {#- --- 可选参数 --- -#}
    {%- if item.VPNNAME is not none -%}
        VPNNAME="{{item.VPNNAME}}",
    {%- endif -%}
    {%- if item.LENAME is not none -%}
        LENAME="{{item.LENAME}}",
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPT=IPV4 时必选 --- -#}
    {%- if item.IPT == 'IPV4' -%}
        IPV4="{{item.IPV4}}",
    {%- endif -%}
    {#- --- 条件必选：IPT=IPV6 时必选 --- -#}
    {%- if item.IPT == 'IPV6' -%}
        IPV6="{{item.IPV6}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 5.5 配置解析数据。

##### 5.5.1 配置S-GW数据解析。

```jinja2
{%- for item in add_ipv4dnsh_list -%}
    ADD IPV4DNSH:
    {#- --- 必选参数 --- -#}
    HSINDEX={{item.HSINDEX}},
    HOSTNAME="{{item.HOSTNAME}}",
    ADDRSECTION={{item.ADDRSECTION}},
    {#- --- 可选参数 --- -#}
    {%- if item.IPV4ADDR1 is not none -%}
        IPV4ADDR1="{{item.IPV4ADDR1}}",
    {%- endif -%}
    {%- if item.PRIORITY1 is not none -%}
        PRIORITY1={{item.PRIORITY1}},
    {%- endif -%}
    {%- if item.WEIGHT1 is not none -%}
        WEIGHT1={{item.WEIGHT1}},
    {%- endif -%}
    {%- if item.IPV4ADDR2 is not none -%}
        IPV4ADDR2="{{item.IPV4ADDR2}}",
    {%- endif -%}
    {%- if item.PRIORITY2 is not none -%}
        PRIORITY2={{item.PRIORITY2}},
    {%- endif -%}
    {%- if item.WEIGHT2 is not none -%}
        WEIGHT2={{item.WEIGHT2}},
    {%- endif -%}
    {%- if item.IPV4ADDR3 is not none -%}
        IPV4ADDR3="{{item.IPV4ADDR3}}",
    {%- endif -%}
    {%- if item.PRIORITY3 is not none -%}
        PRIORITY3={{item.PRIORITY3}},
    {%- endif -%}
    {%- if item.WEIGHT3 is not none -%}
        WEIGHT3={{item.WEIGHT3}},
    {%- endif -%}
    {%- if item.IPV4ADDR4 is not none -%}
        IPV4ADDR4="{{item.IPV4ADDR4}}",
    {%- endif -%}
    {%- if item.PRIORITY4 is not none -%}
        PRIORITY4={{item.PRIORITY4}},
    {%- endif -%}
    {%- if item.WEIGHT4 is not none -%}
        WEIGHT4={{item.WEIGHT4}},
    {%- endif -%}
    {%- if item.IPV4ADDR5 is not none -%}
        IPV4ADDR5="{{item.IPV4ADDR5}}",
    {%- endif -%}
    {%- if item.PRIORITY5 is not none -%}
        PRIORITY5={{item.PRIORITY5}},
    {%- endif -%}
    {%- if item.WEIGHT5 is not none -%}
        WEIGHT5={{item.WEIGHT5}},
    {%- endif -%}
    {%- if item.IPV4ADDR6 is not none -%}
        IPV4ADDR6="{{item.IPV4ADDR6}}",
    {%- endif -%}
    {%- if item.PRIORITY6 is not none -%}
        PRIORITY6={{item.PRIORITY6}},
    {%- endif -%}
    {%- if item.WEIGHT6 is not none -%}
        WEIGHT6={{item.WEIGHT6}},
    {%- endif -%}
    {%- if item.IPV4ADDR7 is not none -%}
        IPV4ADDR7="{{item.IPV4ADDR7}}",
    {%- endif -%}
    {%- if item.PRIORITY7 is not none -%}
        PRIORITY7={{item.PRIORITY7}},
    {%- endif -%}
    {%- if item.WEIGHT7 is not none -%}
        WEIGHT7={{item.WEIGHT7}},
    {%- endif -%}
    {%- if item.IPV4ADDR8 is not none -%}
        IPV4ADDR8="{{item.IPV4ADDR8}}",
    {%- endif -%}
    {%- if item.PRIORITY8 is not none -%}
        PRIORITY8={{item.PRIORITY8}},
    {%- endif -%}
    {%- if item.WEIGHT8 is not none -%}
        WEIGHT8={{item.WEIGHT8}},
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_dnsn_list -%}
    ADD DNSN:
    {#- --- 必选参数 --- -#}
    FQDN="{{item.FQDN}}",
    HSINDEX={{item.HSINDEX}},
    ENTITY={{item.ENTITY}},
    INTYPE={{item.INTYPE}},
    {#- --- 可选参数 --- -#}
    {%- if item.PRIORITY is not none -%}
        PRIORITY={{item.PRIORITY}},
    {%- endif -%}
    {%- if item.WEIGHT is not none -%}
        WEIGHT={{item.WEIGHT}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：ENTITY=SGW/PGW 时可选 --- -#}
    {%- if item.ENTITY in ['SGW', 'PGW'] -%}
        {%- if item.S5PROTOCOL is not none -%}
            S5PROTOCOL={{item.S5PROTOCOL}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：ENTITY=SGW/PGW 时可选 --- -#}
    {%- if item.ENTITY in ['SGW', 'PGW'] -%}
        {%- if item.S8PROTOCOL is not none -%}
            S8PROTOCOL={{item.S8PROTOCOL}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

##### 5.5.2 配置P-GW的数据解析。

```jinja2
{%- for item in add_ipv4dnsh_list_2 -%}
    ADD IPV4DNSH:
    {#- --- 必选参数 --- -#}
    HSINDEX={{item.HSINDEX}},
    HOSTNAME="{{item.HOSTNAME}}",
    ADDRSECTION={{item.ADDRSECTION}},
    {#- --- 可选参数 --- -#}
    {%- if item.IPV4ADDR1 is not none -%}
        IPV4ADDR1="{{item.IPV4ADDR1}}",
    {%- endif -%}
    {%- if item.PRIORITY1 is not none -%}
        PRIORITY1={{item.PRIORITY1}},
    {%- endif -%}
    {%- if item.WEIGHT1 is not none -%}
        WEIGHT1={{item.WEIGHT1}},
    {%- endif -%}
    {%- if item.IPV4ADDR2 is not none -%}
        IPV4ADDR2="{{item.IPV4ADDR2}}",
    {%- endif -%}
    {%- if item.PRIORITY2 is not none -%}
        PRIORITY2={{item.PRIORITY2}},
    {%- endif -%}
    {%- if item.WEIGHT2 is not none -%}
        WEIGHT2={{item.WEIGHT2}},
    {%- endif -%}
    {%- if item.IPV4ADDR3 is not none -%}
        IPV4ADDR3="{{item.IPV4ADDR3}}",
    {%- endif -%}
    {%- if item.PRIORITY3 is not none -%}
        PRIORITY3={{item.PRIORITY3}},
    {%- endif -%}
    {%- if item.WEIGHT3 is not none -%}
        WEIGHT3={{item.WEIGHT3}},
    {%- endif -%}
    {%- if item.IPV4ADDR4 is not none -%}
        IPV4ADDR4="{{item.IPV4ADDR4}}",
    {%- endif -%}
    {%- if item.PRIORITY4 is not none -%}
        PRIORITY4={{item.PRIORITY4}},
    {%- endif -%}
    {%- if item.WEIGHT4 is not none -%}
        WEIGHT4={{item.WEIGHT4}},
    {%- endif -%}
    {%- if item.IPV4ADDR5 is not none -%}
        IPV4ADDR5="{{item.IPV4ADDR5}}",
    {%- endif -%}
    {%- if item.PRIORITY5 is not none -%}
        PRIORITY5={{item.PRIORITY5}},
    {%- endif -%}
    {%- if item.WEIGHT5 is not none -%}
        WEIGHT5={{item.WEIGHT5}},
    {%- endif -%}
    {%- if item.IPV4ADDR6 is not none -%}
        IPV4ADDR6="{{item.IPV4ADDR6}}",
    {%- endif -%}
    {%- if item.PRIORITY6 is not none -%}
        PRIORITY6={{item.PRIORITY6}},
    {%- endif -%}
    {%- if item.WEIGHT6 is not none -%}
        WEIGHT6={{item.WEIGHT6}},
    {%- endif -%}
    {%- if item.IPV4ADDR7 is not none -%}
        IPV4ADDR7="{{item.IPV4ADDR7}}",
    {%- endif -%}
    {%- if item.PRIORITY7 is not none -%}
        PRIORITY7={{item.PRIORITY7}},
    {%- endif -%}
    {%- if item.WEIGHT7 is not none -%}
        WEIGHT7={{item.WEIGHT7}},
    {%- endif -%}
    {%- if item.IPV4ADDR8 is not none -%}
        IPV4ADDR8="{{item.IPV4ADDR8}}",
    {%- endif -%}
    {%- if item.PRIORITY8 is not none -%}
        PRIORITY8={{item.PRIORITY8}},
    {%- endif -%}
    {%- if item.WEIGHT8 is not none -%}
        WEIGHT8={{item.WEIGHT8}},
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_dnsn_list_2 -%}
    ADD DNSN:
    {#- --- 必选参数 --- -#}
    FQDN="{{item.FQDN}}",
    HSINDEX={{item.HSINDEX}},
    ENTITY={{item.ENTITY}},
    INTYPE={{item.INTYPE}},
    {#- --- 可选参数 --- -#}
    {%- if item.PRIORITY is not none -%}
        PRIORITY={{item.PRIORITY}},
    {%- endif -%}
    {%- if item.WEIGHT is not none -%}
        WEIGHT={{item.WEIGHT}},
    {%- endif -%}
    {%- if item.DESC is not none -%}
        DESC="{{item.DESC}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：ENTITY=SGW/PGW 时可选 --- -#}
    {%- if item.ENTITY in ['SGW', 'PGW'] -%}
        {%- if item.S5PROTOCOL is not none -%}
            S5PROTOCOL={{item.S5PROTOCOL}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：ENTITY=SGW/PGW 时可选 --- -#}
    {%- if item.ENTITY in ['SGW', 'PGW'] -%}
        {%- if item.S8PROTOCOL is not none -%}
            S8PROTOCOL={{item.S8PROTOCOL}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 6 配置业务特性数据。

#### 6.1 配置移动性管理参数。

```jinja2
{%- for item in set_emm_list -%}
    SET EMM:
    {#- --- 可选参数 --- -#}
    {%- if item.T3422 is not none -%}
        T3422={{item.T3422}},
    {%- endif -%}
    {%- if item.N3422 is not none -%}
        N3422={{item.N3422}},
    {%- endif -%}
    {%- if item.T3450 is not none -%}
        T3450={{item.T3450}},
    {%- endif -%}
    {%- if item.N3450 is not none -%}
        N3450={{item.N3450}},
    {%- endif -%}
    {%- if item.T3460 is not none -%}
        T3460={{item.T3460}},
    {%- endif -%}
    {%- if item.N3460 is not none -%}
        N3460={{item.N3460}},
    {%- endif -%}
    {%- if item.T3470 is not none -%}
        T3470={{item.T3470}},
    {%- endif -%}
    {%- if item.N3470 is not none -%}
        N3470={{item.N3470}},
    {%- endif -%}
    {%- if item.T3412 is not none -%}
        T3412={{item.T3412}},
    {%- endif -%}
    {%- if item.T3402 is not none -%}
        T3402={{item.T3402}},
    {%- endif -%}
    {%- if item.T3413 is not none -%}
        T3413={{item.T3413}},
    {%- endif -%}
    {%- if item.N3413 is not none -%}
        N3413={{item.N3413}},
    {%- endif -%}
    {%- if item.PAGINGDELTA is not none -%}
        PAGINGDELTA={{item.PAGINGDELTA}},
    {%- endif -%}
    {%- if item.HPT3413 is not none -%}
        HPT3413={{item.HPT3413}},
    {%- endif -%}
    {%- if item.HPN3413 is not none -%}
        HPN3413={{item.HPN3413}},
    {%- endif -%}
    {%- if item.HPPAGINGDELTA is not none -%}
        HPPAGINGDELTA={{item.HPPAGINGDELTA}},
    {%- endif -%}
    {%- if item.RCHTMR is not none -%}
        RCHTMR={{item.RCHTMR}},
    {%- endif -%}
    {%- if item.IMDTCHTMR is not none -%}
        IMDTCHTMR={{item.IMDTCHTMR}},
    {%- endif -%}
    {%- if item.GUTITMR is not none -%}
        GUTITMR={{item.GUTITMR}},
    {%- endif -%}
    {%- if item.GUTIREALLOC is not none -%}
        GUTIREALLOC={{item.GUTIREALLOC}},
    {%- endif -%}
    {%- if item.HOPRETMR is not none -%}
        HOPRETMR={{item.HOPRETMR}},
    {%- endif -%}
    {%- if item.HOCMPSRCTMR is not none -%}
        HOCMPSRCTMR={{item.HOCMPSRCTMR}},
    {%- endif -%}
    {%- if item.HOCMPTGTTMR is not none -%}
        HOCMPTGTTMR={{item.HOCMPTGTTMR}},
    {%- endif -%}
    {%- if item.T3 is not none -%}
        T3={{item.T3}},
    {%- endif -%}
    {%- if item.GUTITMRFORDEBUG is not none -%}
        GUTITMRFORDEBUG={{item.GUTITMRFORDEBUG}},
    {%- endif -%}
    {%- if item.HOT3 is not none -%}
        HOT3={{item.HOT3}},
    {%- endif -%}
    {%- if item.GUTIREALLOCTMR is not none -%}
        GUTIREALLOCTMR={{item.GUTIREALLOCTMR}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 6.2 配置会话管理参数。

##### 6.2.1 设置S1模式SM协议参数。

```jinja2
{%- for item in set_esm_list -%}
    SET ESM:
    {#- --- 可选参数 --- -#}
    {%- if item.T3485 is not none -%}
        T3485={{item.T3485}},
    {%- endif -%}
    {%- if item.N3485 is not none -%}
        N3485={{item.N3485}},
    {%- endif -%}
    {%- if item.T3486 is not none -%}
        T3486={{item.T3486}},
    {%- endif -%}
    {%- if item.N3486 is not none -%}
        N3486={{item.N3486}},
    {%- endif -%}
    {%- if item.T3489 is not none -%}
        T3489={{item.T3489}},
    {%- endif -%}
    {%- if item.N3489 is not none -%}
        N3489={{item.N3489}},
    {%- endif -%}
    {%- if item.T3495 is not none -%}
        T3495={{item.T3495}},
    {%- endif -%}
    {%- if item.N3495 is not none -%}
        N3495={{item.N3495}},
    {%- endif -%}
    {%- if item.TSAEBRSETUP is not none -%}
        TSAEBRSETUP={{item.TSAEBRSETUP}},
    {%- endif -%}
    {%- if item.TSAEBRMOD is not none -%}
        TSAEBRMOD={{item.TSAEBRMOD}},
    {%- endif -%}
    {%- if item.TSAEBRREL is not none -%}
        TSAEBRREL={{item.TSAEBRREL}},
    {%- endif -%}
    {%- if item.TSAEBRHOLD is not none -%}
        TSAEBRHOLD={{item.TSAEBRHOLD}},
    {%- endif -%}
    ;
{%- endfor -%}
```

##### 6.2.2 设置会话管理扩展功能。

```jinja2
{%- for item in set_smfunc_list -%}
    SET SMFUNC:
    {#- --- 可选参数 --- -#}
    {%- if item.DUALFLAG is not none -%}
        DUALFLAG={{item.DUALFLAG}},
    {%- endif -%}
    {%- if item.INDFWD is not none -%}
        INDFWD={{item.INDFWD}},
    {%- endif -%}
    {%- if item.TOPSELCFG is not none -%}
        TOPSELCFG={{item.TOPSELCFG}},
    {%- endif -%}
    {%- if item.APNRES is not none -%}
        APNRES={{item.APNRES}},
    {%- endif -%}
    {%- if item.PDPRMD is not none -%}
        PDPRMD={{item.PDPRMD}},
    {%- endif -%}
    {%- if item.SGWTOPO is not none -%}
        SGWTOPO={{item.SGWTOPO}},
    {%- endif -%}
    {%- if item.TZININTERRAU is not none -%}
        TZININTERRAU={{item.TZININTERRAU}},
    {%- endif -%}
    {%- if item.APNOIPLY is not none -%}
        APNOIPLY={{item.APNOIPLY}},
    {%- endif -%}
    {%- if item.LTEGWSELPLCY is not none -%}
        LTEGWSELPLCY={{item.LTEGWSELPLCY}},
    {%- endif -%}
    {%- if item.GUGWSELPLCY is not none -%}
        GUGWSELPLCY={{item.GUGWSELPLCY}},
    {%- endif -%}
    {%- if item.PRAULI is not none -%}
        PRAULI={{item.PRAULI}},
    {%- endif -%}
    {%- if item.MMULI is not none -%}
        MMULI={{item.MMULI}},
    {%- endif -%}
    {%- if item.NETLOC is not none -%}
        NETLOC={{item.NETLOC}},
    {%- endif -%}
    {%- if item.IMSPOLICY is not none -%}
        IMSPOLICY={{item.IMSPOLICY}},
    {%- endif -%}
    {%- if item.APNNISOURCE is not none -%}
        APNNISOURCE={{item.APNNISOURCE}},
    {%- endif -%}
    {%- if item.EPCO is not none -%}
        EPCO={{item.EPCO}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：NETLOC=ON 时可选 --- -#}
    {%- if item.NETLOC == 'ON' -%}
        {%- if item.RETLOC is not none -%}
            RETLOC={{item.RETLOC}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：NETLOC=ON 时可选 --- -#}
    {%- if item.NETLOC == 'ON' -%}
        {%- if item.ULITYPE is not none -%}
            ULITYPE={{item.ULITYPE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：IMSPOLICY=REJECT 时可选 --- -#}
    {%- if item.IMSPOLICY == 'REJECT' -%}
        {%- if item.IMSREJCAUSE is not none -%}
            IMSREJCAUSE={{item.IMSREJCAUSE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：DUALFLAG=NO 时可选 --- -#}
    {%- if item.DUALFLAG == 'NO' -%}
        {%- if item.PDPTYPE is not none -%}
            PDPTYPE={{item.PDPTYPE}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```


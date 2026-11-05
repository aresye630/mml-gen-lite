---
id: ''
name: SGSN典型配置实例
ne_type: UNC
type: feature
description: 本任务实例实现以下场景配置：UNC与RNC、SG、HLR、GGSN、DNS、CG通过IP骨干网相连。UNC到HLR通过两个SG负荷分担转接，采用M3UA通信，在链路上由层三设备汇聚后再与SG相连。UNC到RNC、GGSN和到CG均采用VRF+OSPF动态路由+BFD组网方式，UNC通过业务网与DNS互通。  **图1** 典型组网图
risk_level: ''
doc_source: ["网络部署","初始配置","UNC初始配置与调测","典型配置实例","SGSN典型配置实例"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本任务实例实现以下场景配置：UNC与RNC、SG、HLR、GGSN、DNS、CG通过IP骨干网相连。UNC到HLR通过两个SG负荷分担转接，采用M3UA通信，在链路上由层三设备汇聚后再与SG相连。UNC到RNC、GGSN和到CG均采用VRF+OSPF动态路由+BFD组网方式，UNC通过业务网与DNS互通。**图1** 典型组网图

## 必备事项
前提条件

* 请了解UNC各类接口的类型及命名规范，可参见业务组网与逻辑接口介绍。
* 基础数据配置、IP路由组网和业务接口配置子任务在前述章节已有详细描述，可参见基础数据配置、配置VNF侧IP路由数据（非SDN）和配置SGSN。本文针对典型的任务场景举例说明整网脚本配置。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    set_sys_list:
      type: items
      properties:
        DESC:
          name: '系统描述'
          type: string
          maxLength: 64
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ID:
          name: '系统标识'
          type: integer
          minimum: 0
          maximum: 254
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NM:
          name: '系统名称'
          type: string
          maxLength: 64
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LOC:
          name: '系统位置'
          type: string
          maxLength: 64
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SRV:
          name: '服务描述'
          type: string
          maxLength: 64
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MCC:
          name: '移动国家码'
          type: string
          maxLength: 3
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MNC:
          name: '移动网号'
          type: string
          maxLength: 3
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PROVER:
          name: '协议版本'
          type: string
          enum:
          - R4
          - R99
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CNID:
          name: '核心网标识'
          type: integer
          minimum:
          - 0
          - 65535
          maximum:
          - 4095
          - 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
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
        TMSIALLOC:
          name: 'TMSI资源分配方式'
          type: string
          enum:
          - ENHAN
          - UNENHAN
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
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
        MNOID:
          name: 'MNO标识'
          type: integer
          minimum:
          - 0
          - 128
          maximum:
          - 0
          - 254
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 0
        SM:
          name: '是否允许SM业务'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: YES
        MAXSMNUM:
          name: '最大承载数'
          type: integer
          minimum: 1
          maximum: 11
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 11
        SMS:
          name: '是否允许SMS业务'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: YES
        LCS:
          name: '是否允许LCS业务'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: YES
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
        PLMNN:
          name: '运营商名称'
          type: string
          maxLength: 50
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'noname'
        SMSCR:
          name: '是否允许纠正短消息中心'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NO
    set_sigattr_list:
      type: items
      properties:
        IF:
          name: '国际网标志'
          type: string
          enum:
          - INVALID
          - LABEL14
          - LABEL24
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IRF:
          name: '国际备用网标志'
          type: string
          enum:
          - INVALID
          - LABEL14
          - LABEL24
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NF:
          name: '国内网标志'
          type: string
          enum:
          - INVALID
          - LABEL14
          - LABEL24
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NRF:
          name: '国内备用网标志'
          type: string
          enum:
          - INVALID
          - LABEL14
          - LABEL24
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        M3UASTPF:
          name: 'M3UA STP功能'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        BSSAPPF:
          name: '是否支持BSSAP+'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        BSSAPPNO:
          name: 'BSSAP+子系统号'
          type: integer
          minimum: 0
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        BSSAPPNI:
          name: 'BSSAP+所在信令网'
          type: string
          enum:
          - DISUSED
          - INT
          - INTB
          - NAT
          - NATB
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MAPNI:
          name: 'MAP所在信令网'
          type: string
          enum:
          - DISUSED
          - INT
          - INTB
          - NAT
          - NATB
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SS7T:
          name: '信令网协议类型'
          type: string
          enum:
          - ANSI_SS7
          - ITUT_SS7
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
    add_m3le_list:
      type: items
      properties:
        LEX:
          name: '本地实体索引'
          type: integer
          minimum: 0
          maximum: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NI:
          name: '网络指示语'
          type: string
          enum:
          - INT
          - INTB
          - NAT
          - NATB
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        OPC:
          name: '本地实体编码'
          type: string
          maxLength: 8
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LET:
          name: '本地实体类型'
          type: string
          enum:
          - ASP
          - IPSP
          - SGP
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LEN:
          name: '本地实体名'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'noname'
    add_m3de_list:
      type: items
      properties:
        DEX:
          name: '目的实体索引'
          type: integer
          minimum: 0
          maximum: 1279
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LEX:
          name: '本地实体索引'
          type: integer
          minimum: 0
          maximum: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DPC:
          name: '目的实体编码'
          type: string
          maxLength: 8
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SLSSM:
          name: '链路集选择掩码'
          type: string
          enum:
          - B0000
          - B0001
          - B0010
          - B0011
          - B0100
          - B0101
          - B0110
          - B0111
          - B1000
          - B1001
          - B1010
          - B1011
          - B1100
          - B1101
          - B1110
          - B1111
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: B0000
        STPF:
          name: '信令转接点功能'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
        DET:
          name: '目的实体类型'
          type: string
          enum:
          - ASP
          - IPSP
          - SGP
          - SP
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ADJF:
          name: '相邻标记'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: TRUE
        NMD:
          name: '网络模式'
          type: string
          enum:
          - EXCLUSIVE
          - INCLUSIVE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: EXCLUSIVE
        PVER:
          name: 'M3UA协议版本'
          type: string
          enum:
          - DRAFT10
          - RFC3332
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: RFC3332
        DEN:
          name: '目的实体名'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'noname'
    add_m3lks_list:
      type: items
      properties:
        LSX:
          name: '链路集索引'
          type: integer
          minimum: 0
          maximum: 1279
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DEX:
          name: '目的实体索引'
          type: integer
          minimum: 0
          maximum: 1279
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SLSM:
          name: '链路选择掩码'
          type: string
          enum:
          - B0000
          - B0001
          - B0010
          - B0011
          - B0100
          - B0101
          - B0110
          - B0111
          - B1000
          - B1001
          - B1010
          - B1011
          - B1100
          - B1101
          - B1110
          - B1111
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: B0000
        WM:
          name: '工作模式'
          type: string
          enum:
          - ASP
          - IPSP
          - SGP
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TM:
          name: '业务模式'
          type: string
          enum:
          - LOADSHARE
          - OVERRIDE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: LOADSHARE
        LSN:
          name: '链路集名'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'noname'
    add_m3rt_list:
      type: items
      properties:
        RTX:
          name: '路由索引'
          type: integer
          minimum: 0
          maximum: 1279
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DEX:
          name: '目的实体索引'
          type: integer
          minimum: 0
          maximum: 1279
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LSX:
          name: '链路集索引'
          type: integer
          minimum: 0
          maximum: 1279
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PRI:
          name: '优先级'
          type: integer
          minimum: 0
          maximum: 254
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 0
        RTN:
          name: '信令路由名'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'noname'
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
    add_m3lnk_list:
      type: items
      properties:
        LNK:
          name: '链路号'
          type: integer
          minimum: 0
          maximum: 1279
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
        IPT:
          name: 'IP类型'
          type: string
          enum:
          - IPV4
          - IPV6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: IPV4
        LOCIPV41:
          name: '本地IPv4地址1'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LOCIPV42:
          name: '本地IPv4地址2'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: '255.255.255.255'
        LOCPORT:
          name: '本地端口号'
          type: integer
          minimum: 1024
          maximum: 65534
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 2905
        PEERIPV41:
          name: '对端IP地址1'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PEERIPV42:
          name: '对端IP地址2'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: '255.255.255.255'
        PEERPORT:
          name: '对端端口号'
          type: integer
          minimum: 1024
          maximum: 65534
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 2905
        CS:
          name: 'C/S模式'
          type: string
          enum:
          - C
          - S
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LSX:
          name: '链路集索引'
          type: integer
          minimum: 0
          maximum: 1279
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ASF:
          name: '主备标识'
          type: string
          enum:
          - ACT
          - STD
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ACT
        PRI:
          name: '优先级'
          type: integer
          minimum: 0
          maximum: 254
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 0
        CONSTHD:
          name: '拥塞开始门限'
          type: integer
          minimum: 60
          maximum: 100
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 80
        CONETHD:
          name: '拥塞结束门限'
          type: integer
          minimum: 0
          maximum: 60
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 40
        CROSSIP:
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
        SCTPINDX:
          name: 'SCTP 参数索引'
          type: integer
          minimum: 0
          maximum: 65534
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        EXCHGMODE:
          name: '交换模式'
          type: string
          enum:
          - DOUBLE
          - SINGLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: SINGLE
        LKN:
          name: '链路名'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'noname'
        LOCIPV61:
          name: '本地IPv6地址1'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LOCIPV62:
          name: '本地IPv6地址2'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PEERIPV61:
          name: '对端IP地址1'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PEERIPV62:
          name: '对端IP地址2'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_sccpopc_list:
      type: items
      properties:
        OPX:
          name: '本局信令点索引'
          type: integer
          minimum: 1
          maximum: 64
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NI:
          name: '网络指示语'
          type: string
          enum:
          - INT
          - INTB
          - NAT
          - NATB
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        OPC:
          name: '本局信令点编码'
          type: string
          maxLength: 8
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SPN:
          name: '信令点用途'
          type: string
          enum:
          - COREONLY
          - IUANDCORE
          - IUONLY
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: COREONLY
        OPN:
          name: '本局信令点名'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'noname'
        SGSNN:
          name: '本局SGSN号'
          type: string
          maxLength: 16
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_sccpdpc_list:
      type: items
      properties:
        DPX:
          name: '目的信令点索引'
          type: integer
          minimum: 0
          maximum: 1279
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        OPX:
          name: '本局信令点索引'
          type: integer
          minimum: 1
          maximum: 64
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DPC:
          name: '目的信令点编码'
          type: string
          maxLength: 8
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SS7T:
          name: '协议类型'
          type: string
          enum:
          - ANSI_SS7
          - ITUT_SS7
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ITUT_SS7
        LDP:
          name: '负荷分担类型'
          type: string
          enum:
          - BACKUP
          - LOADSHARE
          - MULTIDPCLOADSHARE
          - NOUSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NOUSE
        DPN:
          name: '目的信令点名'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'noname'
        BDPX:
          name: '备用目的信令点索引'
          type: integer
          minimum: 0
          maximum: 1279
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SDPX:
          name: '负荷分担目的信令点索引'
          type: integer
          minimum: 0
          maximum: 1279
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_sccpssn_list:
      type: items
      properties:
        SSNX:
          name: '子系统索引'
          type: integer
          minimum: 0
          maximum: 2047
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SSN:
          name: '子系统号'
          type: string
          enum:
          - BSSAP
          - BSSAP+
          - CAP
          - EIR
          - GGSN
          - GMLC
          - HLR
          - INAP
          - MAP
          - MSC
          - NODEFINE
          - OMAP
          - RANAP
          - SCMG
          - SGSN
          - STANDBY0
          - STANDBY1
          - VLR
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NI:
          name: '网络指示语'
          type: string
          enum:
          - INT
          - INTB
          - NAT
          - NATB
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DPC:
          name: '目的信令点编码'
          type: string
          maxLength: 8
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        OPC:
          name: '本局信令点编码'
          type: string
          maxLength: 8
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SSNNAME:
          name: '子系统名'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'noname'
        LOADSHARETYPE:
          name: '负荷分担类型'
          type: string
          enum:
          - BACKUP
          - NOUSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        BACKUPINDEX:
          name: '备用子系统索引'
          type: integer
          minimum: 0
          maximum: 2047
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_sccptmr_list:
      type: items
      properties:
        TCONNEST:
          name: '连接建立定时器（s）'
          type: integer
          minimum: 60
          maximum: 120
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TIAS:
          name: '不活动性发送定时器（s）'
          type: integer
          minimum: 60
          maximum: 600
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TIAR:
          name: '不活动性接收定时器（s）'
          type: integer
          minimum: 180
          maximum: 1260
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TREL:
          name: '连接释放定时器（s）'
          type: integer
          minimum: 10
          maximum: 20
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TREPEATREL:
          name: '连接重复释放定时器（s）'
          type: integer
          minimum: 10
          maximum: 20
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TINTERVAL:
          name: '连接释放外围定时器（s）'
          type: integer
          minimum: 0
          maximum: 60
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TGUARD:
          name: '保护定时器（s）'
          type: integer
          minimum: 1380
          maximum: 1500
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TRESET:
          name: '复位定时器（s）'
          type: integer
          minimum: 10
          maximum: 20
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TREASSEMBLY:
          name: '重装定时器（s）'
          type: integer
          minimum: 10
          maximum: 20
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TSTATINFO:
          name: '子系统测试定时器（s）'
          type: integer
          minimum: 5
          maximum: 1200
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TCOORDCHG:
          name: '协调定时器（s）'
          type: integer
          minimum: 60
          maximum: 120
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TIGNORESST:
          name: '忽略子系统测试定时器（s）'
          type: integer
          minimum: 5
          maximum: 3600
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TFREEZEN:
          name: '资源冻结定时器（s）'
          type: integer
          minimum: 4
          maximum: 120
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TEA:
          name: 'EA定时器（s）'
          type: integer
          minimum: 1
          maximum: 60
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TLRN:
          name: 'LRN冻结定时器（s）'
          type: integer
          minimum: 4
          maximum: 60
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TRESOURCE:
          name: '资源核查定时器（s）'
          type: integer
          minimum: 60
          maximum: 86400
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_rnc_list:
      type: items
      properties:
        RNCX:
          name: 'RNC索引'
          type: integer
          minimum: 0
          maximum: 511
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RNCN:
          name: 'RNC名'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RNCMCC:
          name: '移动国家代码'
          type: string
          maxLength: 3
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RNCMNC:
          name: '移动网号'
          type: string
          maxLength: 3
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RNCID:
          name: 'RNC标识'
          type: integer
          minimum: 0
          maximum: 65535
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NI:
          name: '网络指示语'
          type: string
          enum:
          - INT
          - INTB
          - NAT
          - NATB
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SPC:
          name: '信令点编码'
          type: string
          maxLength: 8
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TRLCTMR:
          name: '资源分配定时器（ms）'
          type: integer
          minimum: 0
          maximum: 65534
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 50000
        TRLCCMP:
          name: '迁移完成定时器（ms）'
          type: integer
          minimum: 0
          maximum: 65534
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 55000
        TRABASSGT:
          name: 'RAB指配过程定时器（ms）'
          type: integer
          minimum: 0
          maximum: 65534
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 15000
        TIGOC:
          name: '忽略OVERLOAD定时器（s）'
          type: integer
          minimum: 0
          maximum: 65534
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 60
        TINTC:
          name: '控制流量速率定时器（s）'
          type: integer
          minimum: 0
          maximum: 65534
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 90
        TRAFR:
          name: '复位定时器（s）'
          type: integer
          minimum: 0
          maximum: 65534
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 60
        TRATR:
          name: '复位保护定时器（s）'
          type: integer
          minimum: 0
          maximum: 65534
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 60
        CNID:
          name: 'CN标识'
          type: integer
          minimum:
          - 0
          - 65535
          maximum:
          - 4095
          - 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IMS:
          name: 'RNC是否支持IMS'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NO
        IU_FLEX:
          name: 'RNC是否支持IU-FLEX'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NO
        RANSHR:
          name: 'RNC是否支持RAN共享'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NO
        UESBI:
          name: '保留参数'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NO
        RNCVER:
          name: 'RNC的协议版本'
          type: string
          enum:
          - R4
          - R5
          - R6
          - R7
          - R8
          - R9+
          - R99
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: R6
        SENDRESET:
          name: '发送RESET消息最大次数'
          type: integer
          minimum: 1
          maximum: 50
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 3
        IPV6ATTR:
          name: 'RNC是否支持IPv6'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NO
        SNDOVERLOAD:
          name: '是否向RNC发送OVERLOAD消息'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NO
        OTS:
          name: 'RNC是否支持OneTunnel'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NO
        R7QOS:
          name: 'RNC是否支持R7 QoS'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NO
        RABQOS:
          name: '协商 RAB QoS'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NO
        ALTBRTYPE:
          name: '可选比特率类型'
          type: string
          enum:
          - UNSPECIFIED
          - VALUERANGE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: UNSPECIFIED
        CHGSYMTOASYMBI:
          name: '更改RAB双向对称为非对称'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: YES
        SGSNBUF:
          name: '是否SGSN缓存3G下行数据包'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NO
        OFUTRAN:
          name: 'RNC是否支持Out Of UTRAN'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NO
        SPID:
          name: 'RNC是否支持SPID'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NO
    add_iupaging_list:
      type: items
      properties:
        LAI:
          name: '位置区标识'
          type: string
          maxLength: 10
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RAC:
          name: '路由区编码'
          type: string
          maxLength: 4
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RNCINDEX:
          name: 'RNC索引'
          type: integer
          minimum: 0
          maximum: 511
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_iuload_list:
      type: items
      properties:
        IUSHSPT:
          name: '是否支持Iu负荷分担'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NTMR:
          name: '周期性通知定时器长度（min）'
          type: integer
          minimum: 1
          maximum: 100
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        OVERLOADTMR:
          name: '发送OVERLOAD消息定时器长度（s）'
          type: integer
          minimum: 5
          maximum: 250
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_iuauthciph_list:
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
        SECPLC:
          name: '安全策略'
          type: string
          enum:
          - AUTHANDPROTECTED
          - AUTHONLY
          - NEVER
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: AUTHANDPROTECTED
        AUTHEVENT:
          name: '鉴权事件'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AUTHPERIOD:
          name: '鉴权周期'
          type: integer
          minimum: 0
          maximum: 24
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 24
        AUTHEVENTTHRESHOLD:
          name: '鉴权事件上限'
          type: integer
          minimum: 0
          maximum: 1023
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 1
        ATTSAUTH:
          name: '是否支持附着流程的二次鉴权功能'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NO
        RAUSAUTH:
          name: '是否支持路由更新流程的二次鉴权功能'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NO
        AUTHSETV2:
          name: '是否支持V2取鉴权集功能'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NO
        AUTHSETSNUMBER:
          name: '鉴权集数量'
          type: integer
          minimum: 1
          maximum: 5
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 5
        PREGETAUTHSETS:
          name: '是否预取鉴权集'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: YES
        GETAUTHADVTH:
          name: '预先取鉴权集门限值'
          type: integer
          minimum: 0
          maximum: 4
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 0
        REAUTH:
          name: '重复鉴权'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NO
        CAFTIMES:
          name: '用户鉴权失败次数临界值'
          type: integer
          minimum: 3
          maximum: 20
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 3
        CIPHALG:
          name: '加密算法'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        INTALG:
          name: '完整性算法'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IDRQ:
          name: '强制身份识别'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: YES
    set_iudetach_list:
      type: items
      properties:
        DETACHSW:
          name: '非活动用户分离'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NACTTMR:
          name: '非活动用户分离定时器（分）'
          type: integer
          minimum: 0
          maximum: 1440
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DETACHONFOR:
          name: '是否在Follow-on时启用分离非活动用户功能'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DETACHONCONN:
          name: '保留参数1'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NACTTMRONCONN:
          name: '保留参数2'
          type: integer
          minimum: 0
          maximum: 360
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        REATM:
          name: '保留参数3'
          type: integer
          minimum: 0
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ONLINETIMER:
          name: '永久在线识别定时器长（秒）'
          type: integer
          minimum: 1
          maximum: 65536
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ONLINEFOREVER:
          name: '永久在线识别'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IMPDTCHNORSP:
          name: '是否在分离响应超时后分离用户'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IMPDTCH:
          name: '分离用户方式'
          type: string
          enum:
          - EXPLICITLY
          - IMPLICITLY
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IMPIUONNONACT:
          name: '保留参数4'
          type: string
          enum:
          - EXPLICITLY
          - IMPLICITLY
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IMPONIUREL:
          name: '保留参数5'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_iupaging_list_1:
      type: items
      properties:
        LAI:
          name: '位置区标识'
          type: string
          maxLength: 10
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RAC:
          name: '路由区编码'
          type: string
          maxLength: 4
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RNCINDEX:
          name: 'RNC索引'
          type: integer
          minimum: 0
          maximum: 511
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_iusm_list:
      type: items
      properties:
        T3385:
          name: 'T3385（s）'
          type: integer
          minimum: 1
          maximum: 86400
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        N3385:
          name: 'N3385（times）'
          type: integer
          minimum: 0
          maximum: 5
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        T3386:
          name: 'T3386（s）'
          type: integer
          minimum: 1
          maximum: 86400
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        N3386:
          name: 'N3386（times）'
          type: integer
          minimum: 0
          maximum: 5
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        T3395:
          name: 'T3395（s）'
          type: integer
          minimum: 1
          maximum: 86400
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        N3395:
          name: 'N3395（times）'
          type: integer
          minimum: 0
          maximum: 5
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
        VRFDESCRIPTION:
          name: 'VPN实例描述'
          type: string
          maxLength: 242
          required: false
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
    add_m3le_list_1:
      type: items
      properties:
        LEX:
          name: '本地实体索引'
          type: integer
          minimum: 0
          maximum: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NI:
          name: '网络指示语'
          type: string
          enum:
          - INT
          - INTB
          - NAT
          - NATB
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        OPC:
          name: '本地实体编码'
          type: string
          maxLength: 8
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LET:
          name: '本地实体类型'
          type: string
          enum:
          - ASP
          - IPSP
          - SGP
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RC:
          name: '路由上下文'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NA:
          name: '网络外貌'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LEN:
          name: '本地实体名'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'noname'
    add_m3de_list_1:
      type: items
      properties:
        DEX:
          name: '目的实体索引'
          type: integer
          minimum: 0
          maximum: 1279
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LEX:
          name: '本地实体索引'
          type: integer
          minimum: 0
          maximum: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DPC:
          name: '目的实体编码'
          type: string
          maxLength: 8
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SLSSM:
          name: '链路集选择掩码'
          type: string
          enum:
          - B0000
          - B0001
          - B0010
          - B0011
          - B0100
          - B0101
          - B0110
          - B0111
          - B1000
          - B1001
          - B1010
          - B1011
          - B1100
          - B1101
          - B1110
          - B1111
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: B0000
        DET:
          name: '目的实体类型'
          type: string
          enum:
          - ASP
          - IPSP
          - SGP
          - SP
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ADJF:
          name: '相邻标记'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: TRUE
        RC:
          name: '路由上下文'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PVER:
          name: 'M3UA协议版本'
          type: string
          enum:
          - DRAFT10
          - RFC3332
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: RFC3332
        DEN:
          name: '目的实体名'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'noname'
    add_m3lks_list_1:
      type: items
      properties:
        LSX:
          name: '链路集索引'
          type: integer
          minimum: 0
          maximum: 1279
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DEX:
          name: '目的实体索引'
          type: integer
          minimum: 0
          maximum: 1279
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SLSM:
          name: '链路选择掩码'
          type: string
          enum:
          - B0000
          - B0001
          - B0010
          - B0011
          - B0100
          - B0101
          - B0110
          - B0111
          - B1000
          - B1001
          - B1010
          - B1011
          - B1100
          - B1101
          - B1110
          - B1111
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: B0000
        WM:
          name: '工作模式'
          type: string
          enum:
          - ASP
          - IPSP
          - SGP
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TM:
          name: '业务模式'
          type: string
          enum:
          - LOADSHARE
          - OVERRIDE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: LOADSHARE
        LSN:
          name: '链路集名'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'noname'
    add_m3rt_list_1:
      type: items
      properties:
        RTX:
          name: '路由索引'
          type: integer
          minimum: 0
          maximum: 1279
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DEX:
          name: '目的实体索引'
          type: integer
          minimum: 0
          maximum: 1279
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LSX:
          name: '链路集索引'
          type: integer
          minimum: 0
          maximum: 1279
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RTN:
          name: '信令路由名'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'noname'
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
        SCTPPARANAME:
          name: 'SCTP协议参数名'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'noname'
    add_m3lnk_list_4:
      type: items
      properties:
        LNK:
          name: '链路号'
          type: integer
          minimum: 0
          maximum: 1279
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
        IPT:
          name: 'IP类型'
          type: string
          enum:
          - IPV4
          - IPV6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: IPV4
        LOCIPV41:
          name: '本地IPv4地址1'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LOCIPV42:
          name: '本地IPv4地址2'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: '255.255.255.255'
        LOCPORT:
          name: '本地端口号'
          type: integer
          minimum: 1024
          maximum: 65534
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 2905
        PEERIPV41:
          name: '对端IP地址1'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PEERIPV42:
          name: '对端IP地址2'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: '255.255.255.255'
        PEERPORT:
          name: '对端端口号'
          type: integer
          minimum: 1024
          maximum: 65534
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 2905
        CS:
          name: 'C/S模式'
          type: string
          enum:
          - C
          - S
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LSX:
          name: '链路集索引'
          type: integer
          minimum: 0
          maximum: 1279
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SCTPINDX:
          name: 'SCTP 参数索引'
          type: integer
          minimum: 0
          maximum: 65534
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LKN:
          name: '链路名'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'noname'
        LOCIPV61:
          name: '本地IPv6地址1'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LOCIPV62:
          name: '本地IPv6地址2'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PEERIPV61:
          name: '对端IP地址1'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PEERIPV62:
          name: '对端IP地址2'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_m3le_list_2:
      type: items
      properties:
        LEX:
          name: '本地实体索引'
          type: integer
          minimum: 0
          maximum: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NI:
          name: '网络指示语'
          type: string
          enum:
          - INT
          - INTB
          - NAT
          - NATB
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        OPC:
          name: '本地实体编码'
          type: string
          maxLength: 8
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LET:
          name: '本地实体类型'
          type: string
          enum:
          - ASP
          - IPSP
          - SGP
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LEN:
          name: '本地实体名'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'noname'
    add_m3de_list_2:
      type: items
      properties:
        DEX:
          name: '目的实体索引'
          type: integer
          minimum: 0
          maximum: 1279
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LEX:
          name: '本地实体索引'
          type: integer
          minimum: 0
          maximum: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DPC:
          name: '目的实体编码'
          type: string
          maxLength: 8
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SLSSM:
          name: '链路集选择掩码'
          type: string
          enum:
          - B0000
          - B0001
          - B0010
          - B0011
          - B0100
          - B0101
          - B0110
          - B0111
          - B1000
          - B1001
          - B1010
          - B1011
          - B1100
          - B1101
          - B1110
          - B1111
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: B0000
        STPF:
          name: '信令转接点功能'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
        DET:
          name: '目的实体类型'
          type: string
          enum:
          - ASP
          - IPSP
          - SGP
          - SP
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ADJF:
          name: '相邻标记'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: TRUE
        NMD:
          name: '网络模式'
          type: string
          enum:
          - EXCLUSIVE
          - INCLUSIVE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: EXCLUSIVE
        RC:
          name: '路由上下文'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PVER:
          name: 'M3UA协议版本'
          type: string
          enum:
          - DRAFT10
          - RFC3332
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: RFC3332
        DEN:
          name: '目的实体名'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'noname'
    add_m3lks_list_2:
      type: items
      properties:
        LSX:
          name: '链路集索引'
          type: integer
          minimum: 0
          maximum: 1279
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DEX:
          name: '目的实体索引'
          type: integer
          minimum: 0
          maximum: 1279
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SLSM:
          name: '链路选择掩码'
          type: string
          enum:
          - B0000
          - B0001
          - B0010
          - B0011
          - B0100
          - B0101
          - B0110
          - B0111
          - B1000
          - B1001
          - B1010
          - B1011
          - B1100
          - B1101
          - B1110
          - B1111
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: B0000
        WM:
          name: '工作模式'
          type: string
          enum:
          - ASP
          - IPSP
          - SGP
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TM:
          name: '业务模式'
          type: string
          enum:
          - LOADSHARE
          - OVERRIDE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: LOADSHARE
        LSN:
          name: '链路集名'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'noname'
    add_m3rt_list_2:
      type: items
      properties:
        RTX:
          name: '路由索引'
          type: integer
          minimum: 0
          maximum: 1279
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DEX:
          name: '目的实体索引'
          type: integer
          minimum: 0
          maximum: 1279
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LSX:
          name: '链路集索引'
          type: integer
          minimum: 0
          maximum: 1279
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PRI:
          name: '优先级'
          type: integer
          minimum: 0
          maximum: 254
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 0
        RTN:
          name: '信令路由名'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'noname'
    add_m3lnk_list_5:
      type: items
      properties:
        LNK:
          name: '链路号'
          type: integer
          minimum: 0
          maximum: 1279
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
        IPT:
          name: 'IP类型'
          type: string
          enum:
          - IPV4
          - IPV6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: IPV4
        LOCIPV41:
          name: '本地IPv4地址1'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LOCIPV42:
          name: '本地IPv4地址2'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: '255.255.255.255'
        LOCPORT:
          name: '本地端口号'
          type: integer
          minimum: 1024
          maximum: 65534
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 2905
        PEERIPV41:
          name: '对端IP地址1'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PEERIPV42:
          name: '对端IP地址2'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: '255.255.255.255'
        PEERPORT:
          name: '对端端口号'
          type: integer
          minimum: 1024
          maximum: 65534
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 2905
        CS:
          name: 'C/S模式'
          type: string
          enum:
          - C
          - S
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LSX:
          name: '链路集索引'
          type: integer
          minimum: 0
          maximum: 1279
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ASF:
          name: '主备标识'
          type: string
          enum:
          - ACT
          - STD
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ACT
        PRI:
          name: '优先级'
          type: integer
          minimum: 0
          maximum: 254
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 0
        CONSTHD:
          name: '拥塞开始门限'
          type: integer
          minimum: 60
          maximum: 100
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 80
        CONETHD:
          name: '拥塞结束门限'
          type: integer
          minimum: 0
          maximum: 60
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 40
        CROSSIP:
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
        SCTPINDX:
          name: 'SCTP 参数索引'
          type: integer
          minimum: 0
          maximum: 65534
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        EXCHGMODE:
          name: '交换模式'
          type: string
          enum:
          - DOUBLE
          - SINGLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: SINGLE
        LKN:
          name: '链路名'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'noname'
        LOCIPV61:
          name: '本地IPv6地址1'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LOCIPV62:
          name: '本地IPv6地址2'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PEERIPV61:
          name: '对端IP地址1'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PEERIPV62:
          name: '对端IP地址2'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_sccpopc_list_1:
      type: items
      properties:
        OPX:
          name: '本局信令点索引'
          type: integer
          minimum: 1
          maximum: 64
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NI:
          name: '网络指示语'
          type: string
          enum:
          - INT
          - INTB
          - NAT
          - NATB
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        OPC:
          name: '本局信令点编码'
          type: string
          maxLength: 8
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SPN:
          name: '信令点用途'
          type: string
          enum:
          - COREONLY
          - IUANDCORE
          - IUONLY
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: COREONLY
        SGSNN:
          name: '本局SGSN号'
          type: string
          maxLength: 16
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        OPN:
          name: '本局信令点名'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'noname'
    add_sccpdpc_list_1:
      type: items
      properties:
        DPX:
          name: '目的信令点索引'
          type: integer
          minimum: 0
          maximum: 1279
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        OPX:
          name: '本局信令点索引'
          type: integer
          minimum: 1
          maximum: 64
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DPC:
          name: '目的信令点编码'
          type: string
          maxLength: 8
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SS7T:
          name: '协议类型'
          type: string
          enum:
          - ANSI_SS7
          - ITUT_SS7
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ITUT_SS7
        LDP:
          name: '负荷分担类型'
          type: string
          enum:
          - BACKUP
          - LOADSHARE
          - MULTIDPCLOADSHARE
          - NOUSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NOUSE
        SDPX:
          name: '负荷分担目的信令点索引'
          type: integer
          minimum: 0
          maximum: 1279
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DPN:
          name: '目的信令点名'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'noname'
        BDPX:
          name: '备用目的信令点索引'
          type: integer
          minimum: 0
          maximum: 1279
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_sccpssn_list_2:
      type: items
      properties:
        SSNX:
          name: '子系统索引'
          type: integer
          minimum: 0
          maximum: 2047
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SSN:
          name: '子系统号'
          type: string
          enum:
          - BSSAP
          - BSSAP+
          - CAP
          - EIR
          - GGSN
          - GMLC
          - HLR
          - INAP
          - MAP
          - MSC
          - NODEFINE
          - OMAP
          - RANAP
          - SCMG
          - SGSN
          - STANDBY0
          - STANDBY1
          - VLR
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NI:
          name: '网络指示语'
          type: string
          enum:
          - INT
          - INTB
          - NAT
          - NATB
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DPC:
          name: '目的信令点编码'
          type: string
          maxLength: 8
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        OPC:
          name: '本局信令点编码'
          type: string
          maxLength: 8
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SSNNAME:
          name: '子系统名'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'noname'
        LOADSHARETYPE:
          name: '负荷分担类型'
          type: string
          enum:
          - BACKUP
          - NOUSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        BACKUPINDEX:
          name: '备用子系统索引'
          type: integer
          minimum: 0
          maximum: 2047
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_imsigt_list:
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
        GT:
          name: '国家代码_网络接入号'
          type: string
          maxLength: 15
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MNNAME:
          name: '移动网络名称'
          type: string
          maxLength: 50
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'noname'
    add_connectplmn_list:
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
        NOID:
          name: '运营商标识'
          type: integer
          minimum:
          - 0
          - 128
          maximum:
          - 64
          - 254
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SM:
          name: '是否允许SM业务'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: YES
        MAXSMNUM:
          name: '最大承载数'
          type: integer
          minimum: 1
          maximum: 11
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 11
        SMS:
          name: '是否允许SMS业务'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: YES
        SMSCR:
          name: '是否允许纠正短消息中心'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NO
        LCS:
          name: '是否允许LCS业务'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: YES
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
        COUNTRYORAREANAME:
          name: '运营商名称'
          type: string
          maxLength: 50
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'noname'
        EXCLUSIVEPLMN:
          name: '专属互连PLMN'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NO
        SMSCT:
          name: '纠正后的短消息中心'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_sccpgt_list:
      type: items
      properties:
        GTX:
          name: 'GT码索引'
          type: integer
          minimum: 0
          maximum: 4095
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NI:
          name: '网络指示语'
          type: string
          enum:
          - INT
          - INTB
          - NAT
          - NATB
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RT:
          name: '翻译结果类型'
          type: string
          enum:
          - DPC
          - DPCGT
          - DPCNEWGT
          - DPCSSN
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GTEXP:
          name: 'GT码表示语'
          type: string
          enum:
          - FOUR
          - SIX
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FOUR
        NP:
          name: '编号计划'
          type: string
          enum:
          - DATA
          - ISDNMS
          - ISDNP
          - PMS
          - SMS
          - TELEX
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ISDNP
        ADDREXP:
          name: '地址性质表示语'
          type: string
          enum:
          - FREE
          - INTDN
          - NSU
          - NVU
          - SUBDN
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: INTDN
        ADDR:
          name: '地址信息'
          type: string
          maxLength: 20
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DPC:
          name: '目的信令点编码'
          type: string
          maxLength: 8
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NAME:
          name: 'SCCP GT名称'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'noname'
        TT:
          name: '翻译类型'
          type: string
          enum:
          - ANSI10
          - ANSI9
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ANSI9
        NGTX:
          name: '新GT码索引'
          type: integer
          minimum: 0
          maximum: 4095
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SSN:
          name: '子系统号'
          type: string
          enum:
          - BSSAP
          - BSSAP+
          - CAP
          - EIR
          - GGSN
          - GMLC
          - HLR
          - INAP
          - MAP
          - MSC
          - NODEFINE
          - OMAP
          - RANAP
          - SCMG
          - SGSN
          - STANDBY0
          - STANDBY1
          - VLR
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_l3vpninst_list_3:
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
    add_vpninstaf_list_3:
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
    mod_interface_list_12:
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
    add_interface_list_15:
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
    add_ipbindvpn_list_15:
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
    add_ethsubif_list_12:
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
    add_ifipv4address_list_15:
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
    add_ospf_list_3:
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
    add_ospfarea_list_3:
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
    add_ospfnetwork_list_9:
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
    add_ospfimportroute_list_3:
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
    add_ospfinterface_list_12:
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
    add_gtpule_list_2:
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
    add_ggsncharact_list:
      type: items
      properties:
        RANGE:
          name: '对端设备范围'
          type: string
          enum:
          - ALL_GGSN
          - Gn_GGSN
          - Gp_GGSN
          - SPECIAL_GGSN
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
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
        GGSNIPV4:
          name: 'GGSN的信令面IP地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MASKV4:
          name: '掩码'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        QOSVER:
          name: 'GGSN支持的QoS版本'
          type: string
          enum:
          - R5QOS
          - R7QOS
          - R99QOS
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: R99QOS
        GGSNIPV6:
          name: 'GGSN的信令面IP地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MASKV6:
          name: '子网前缀长度'
          type: integer
          minimum: 1
          maximum: 128
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_l3vpninst_list_4:
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
    add_vpninstaf_list_4:
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
    mod_interface_list_16:
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
    add_interface_list_20:
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
    add_ipbindvpn_list_20:
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
    add_ethsubif_list_16:
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
    add_ifipv4address_list_20:
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
    add_ospf_list_4:
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
    add_ospfarea_list_4:
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
    add_ospfnetwork_list_12:
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
    add_ospfimportroute_list_4:
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
    add_ospfinterface_list_16:
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
    add_serviceip_list_9:
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
    add_chgcdpip_list:
      type: items
      properties:
        IPT:
          name: 'IP地址类型'
          type: string
          enum:
          - IPv4
          - IPv6
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV4ADDR:
          name: 'IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PORTBGN:
          name: '起始端口号'
          type: integer
          minimum: 1024
          maximum: 65534
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 1024
        PORTEND:
          name: '结束端口号'
          type: integer
          minimum: 1024
          maximum: 65534
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
        IPV6ADDR:
          name: 'IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_chgcg_list:
      type: items
      properties:
        IP:
          name: 'CG的IPV4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GRD:
          name: '优先级'
          type: integer
          minimum: 0
          maximum: 11
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 0
        PRO:
          name: 'GTP承载协议'
          type: string
          enum:
          - TCP
          - UDP
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CGR:
          name: 'CG协议版本'
          type: string
          enum:
          - R4
          - R5
          - R6
          - R7
          - R9
          - R98
          - R99
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SPN:
          name: 'CG接收端口号'
          type: integer
          minimum: 1024
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 3386
        DEFAULTCG:
          name: '缺省CG'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: YES
        CGN:
          name: 'CG名'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'noname'
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
    set_chgga_list:
      type: items
      properties:
        GCR:
          name: 'GPRS CDR协议版本'
          type: string
          enum:
          - R4
          - R5
          - R6
          - R7
          - R9
          - R98
          - R99
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        UCR:
          name: 'UMTS CDR协议版本'
          type: string
          enum:
          - R4
          - R5
          - R6
          - R7
          - R9
          - R99
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CHGVER98:
          name: 'R98 CDR版本'
          type: string
          enum:
          - CMCCV130
          - GSM1215V760
          - USI1215V760
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CHGVER99:
          name: 'R99 CDR版本'
          type: string
          enum:
          - AIS32015V360
          - GPP32015V360
          - GPP32015V3A0
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CHGVER4:
          name: 'R4 CDR版本'
          type: string
          enum:
          - GPP32215V440
          - VOX32215V440
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CHGVER5:
          name: 'R5 CDR版本'
          type: string
          enum:
          - GPP32215V560
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CHGVER6:
          name: 'R6 CDR版本'
          type: string
          enum:
          - GPP32251V660
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CHGVER7:
          name: 'R7 CDR版本'
          type: string
          enum:
          - GPP32251V740
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CHGVER9:
          name: 'R9 CDR版本'
          type: string
          enum:
          - GPP32251V940
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ITVRES:
          name: 'CDR重发间隔（s）'
          type: integer
          minimum: 1
          maximum: 10
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RSNUM:
          name: 'CDR重发次数'
          type: integer
          minimum: 1
          maximum: 10
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        HDDETH:
          name: '硬盘操作失败告警次数门限'
          type: integer
          minimum: 1
          maximum: 10
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        HDDFSL:
          name: '硬盘空间不足门限（%）'
          type: integer
          minimum: 50
          maximum: 90
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        REDICTFRMMAXOCCRATE:
          name: '重定向帧最大占用率（%）'
          type: integer
          minimum: 20
          maximum: 80
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        QOSVER:
          name: '话单QoS最高版本'
          type: string
          enum:
          - R5
          - R7
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GASENDUDPCHECK:
          name: '发送消息UDP校验'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GAREVUDPCHECK:
          name: '接收消息UDP校验'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CDROVERWRITE:
          name: '覆盖硬盘上话单文件'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_chgbeha_list:
      type: items
      properties:
        CB:
          name: '计费行为'
          type: string
          enum:
          - B1
          - B10
          - B11
          - B12
          - B2
          - B3
          - B4
          - B5
          - B6
          - B7
          - B8
          - B9
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        BA:
          name: '行为属性'
          type: string
          enum:
          - CGIP
          - NOQOS
          - NOROAMING
          - PLT
          - PST
          - SMSC
          - SMSCMOMT
          - SMSCMT
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ACC:
          name: '支持的计费属性'
          type: string
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
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
        PURGELEN:
          name: '关闭空闲PDP定时器时长（min）'
          type: integer
          minimum: 30
          maximum: 1440
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SMSCADDR:
          name: 'SMSC地址'
          type: string
          maxLength: 16
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_chgchar_list:
      type: items
      properties:
        CC:
          name: '计费属性'
          type: string
          enum:
          - FLATRATE
          - HOTBILLING
          - NORMAL
          - PREPAID
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MP:
          name: '生成M-CDR'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MPCP:
          name: '周期生成M-CDR'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MPL:
          name: 'M-CDR生成周期（min）'
          type: integer
          minimum: 1
          maximum: 1440
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MLCP:
          name: '位置更新生成M-CDR'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MLCL:
          name: 'M-CDR位置更新最大次数'
          type: integer
          minimum: 1
          maximum: 10
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RPCMCDR:
          name: '精简M-CDR'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SP:
          name: '生成S-CDR'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SPP:
          name: '周期生成S-CDR'
          type: string
          enum:
          - FORBID
          - PERMIT
          - VOLUMN
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SPL:
          name: 'S-CDR生成周期（min）'
          type: integer
          minimum: 1
          maximum: 1440
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SVP:
          name: '流量生成S-CDR'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SVL:
          name: '生成S-CDR流量阈值（KB）'
          type: integer
          minimum: 1
          maximum: 1000000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SCCP:
          name: '计费条件变更生成S-CDR'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SCCL:
          name: '最大计费条件变更次数'
          type: integer
          minimum: 1
          maximum: 10
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SLCP:
          name: '位置更新生成S-CDR'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PCC:
          name: 'PLMN变化生成特定原因值S-CDR'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RPCSCDR:
          name: '精简S-CDR'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SMOP:
          name: '生成S-SMO-CDR'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SMTP:
          name: '生成S-SMT-CDR'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LCSMOP:
          name: '生成LCS-MO-CDR'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LCSMTP:
          name: '生成LCS-MT-CDR'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LCSNIP:
          name: '生成LCS-NI-CDR'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SR:
          name: '计费限呼标志'
          type: string
          enum:
          - INTERRUPT
          - RESTRICT
          - UNRESTRICT
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CGIP:
          name: 'CG的IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TARIACCFLG:
          name: '费率变更允许的用户类型'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_chgwkdy_list:
      type: items
      properties:
        WKDAY:
          name: '星期序号'
          type: string
          enum:
          - FRI
          - MON
          - SAT
          - SUN
          - THURS
          - TUES
          - WED
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CC:
          name: '计费属性'
          type: string
          enum:
          - FLATRATE
          - HOTBILLING
          - NORMAL
          - PREPAID
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TT:
          name: '费率类型'
          type: string
          enum:
          - WEEKEND
          - WORK
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_chgtari_list:
      type: items
      properties:
        TT:
          name: '费率类型'
          type: string
          enum:
          - FESTIVAL
          - WEEKEND
          - WORK
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ST:
          name: '起始时间'
          type: string
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: 'HH&MM&SS'
        ET:
          name: '结束时间'
          type: string
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: 'HH&MM&SS'
        CC:
          name: '计费属性'
          type: string
          enum:
          - FLATRATE
          - HOTBILLING
          - NORMAL
          - PREPAID
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_sigattr_list_1:
      type: items
      properties:
        IF:
          name: '国际网标志'
          type: string
          enum:
          - INVALID
          - LABEL14
          - LABEL24
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IRF:
          name: '国际备用网标志'
          type: string
          enum:
          - INVALID
          - LABEL14
          - LABEL24
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NF:
          name: '国内网标志'
          type: string
          enum:
          - INVALID
          - LABEL14
          - LABEL24
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NRF:
          name: '国内备用网标志'
          type: string
          enum:
          - INVALID
          - LABEL14
          - LABEL24
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        M3UASTPF:
          name: 'M3UA STP功能'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        BSSAPPF:
          name: '是否支持BSSAP+'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        BSSAPPNO:
          name: 'BSSAP+子系统号'
          type: integer
          minimum: 0
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        BSSAPPNI:
          name: 'BSSAP+所在信令网'
          type: string
          enum:
          - DISUSED
          - INT
          - INTB
          - NAT
          - NATB
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MAPNI:
          name: 'MAP所在信令网'
          type: string
          enum:
          - DISUSED
          - INT
          - INTB
          - NAT
          - NATB
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SS7T:
          name: '信令网协议类型'
          type: string
          enum:
          - ANSI_SS7
          - ITUT_SS7
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_serviceip_list_10:
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
    set_dns_list:
      type: items
      properties:
        TMS:
          name: '总共发送次数'
          type: integer
          minimum: 1
          maximum: 5
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TRT:
          name: '响应超时时长（ms）'
          type: integer
          minimum: 1
          maximum: 10000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DDS:
          name: 'DNS探测开关'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DDI:
          name: 'DNS探测间隔（s）'
          type: integer
          minimum: 1
          maximum: 120
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SFT:
          name: '故障判定阈值'
          type: integer
          minimum: 1
          maximum: 10
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DDN:
          name: '缺省探测域名'
          type: string
          maxLength: 59
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DISCACHEPURGESW:
          name: '关闭CACHE老化功能开关'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPSORTMODE:
          name: 'IP排序模式'
          type: string
          enum:
          - LOCAL_GGSN_FOR_SVR
          - PRI_WGT
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CNAMESW:
          name: '启用CNAME记录的TTL值'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RCRSPTM:
          name: '一级Cache等待二级Cache响应时长（s）'
          type: integer
          minimum: 1
          maximum: 10
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RCQRYTM:
          name: '二级Cache解析超时时长（s）'
          type: integer
          minimum: 1
          maximum: 10
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        FAILTM:
          name: '持续失败最大时长（s）'
          type: integer
          minimum:
          - 0
          - 60
          maximum:
          - 0
          - 6000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PAUSETM:
          name: '暂停查询最大时长（s）'
          type: integer
          minimum: 10
          maximum: 6000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RCUPDTM:
          name: '二级Cache提前刷新时间（s）'
          type: integer
          minimum:
          - 0
          - 400
          maximum:
          - 0
          - 6000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RCUSEDTM:
          name: '二级Cache最近被使用判断标准（s）'
          type: integer
          minimum: 60
          maximum: 6000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LOCALTTL:
          name: '本地配置TTL（h）'
          type: integer
          minimum:
          - 0
          - 3
          maximum:
          - 0
          - 24
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        REROUTECAUSE:
          name: '服务器重选触发原因值'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_iuauthciph_list_1:
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
        SECPLC:
          name: '安全策略'
          type: string
          enum:
          - AUTHANDPROTECTED
          - AUTHONLY
          - NEVER
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: AUTHANDPROTECTED
        AUTHEVENT:
          name: '鉴权事件'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AUTHEVENTTHRESHOLD:
          name: '鉴权事件上限'
          type: integer
          minimum: 0
          maximum: 1023
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 1
        ATTSAUTH:
          name: '是否支持附着流程的二次鉴权功能'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NO
        RAUSAUTH:
          name: '是否支持路由更新流程的二次鉴权功能'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NO
        AUTHSETV2:
          name: '是否支持V2取鉴权集功能'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NO
        REAUTH:
          name: '重复鉴权'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NO
        CIPHALG:
          name: '加密算法'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        INTALG:
          name: '完整性算法'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AUTHPERIOD:
          name: '鉴权周期'
          type: integer
          minimum: 0
          maximum: 24
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 24
        AUTHSETSNUMBER:
          name: '鉴权集数量'
          type: integer
          minimum: 1
          maximum: 5
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 5
        CAFTIMES:
          name: '用户鉴权失败次数临界值'
          type: integer
          minimum: 3
          maximum: 20
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 3
        GETAUTHADVTH:
          name: '预先取鉴权集门限值'
          type: integer
          minimum: 0
          maximum: 4
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 0
        PREGETAUTHSETS:
          name: '是否预取鉴权集'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: YES
    add_algpriority_list:
      type: items
      properties:
        ALGTYPE:
          name: '算法类型'
          type: string
          enum:
          - CIPH
          - INTE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ALGCIPH:
          name: '加密算法'
          type: string
          enum:
          - NOCIPH
          - UEA1
          - UEA2
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ALGPRI:
          name: '算法优先级'
          type: integer
          minimum: 0
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ALGINTE:
          name: '完整性算法'
          type: string
          enum:
          - UIA1
          - UIA2
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_arppara_list:
      type: items
      properties:
        GROUPID:
          name: 'ARP策略组'
          type: string
          enum:
          - G0
          - G1
          - G2
          - G3
          - G4
          - G5
          - G6
          - G7
          - G8
          - G9
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        USRPRI:
          name: '用户级别'
          type: string
          enum:
          - HIGHLEVELUSER
          - LOWLEVELUSER
          - NORMALUSER
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SRVLVL:
          name: '业务级别'
          type: string
          enum:
          - BACKGROUND
          - CONVERSATION
          - INTERACTIVETRAFFICPRI1
          - INTERACTIVETRAFFICPRI2
          - INTERACTIVETRAFFICPRI3
          - STREAMINGGBRLESS24KBPS
          - STREAMINGGBRMORE25KBPS
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PRTLVL:
          name: '承载优先级'
          type: integer
          minimum: 1
          maximum: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PRELVL:
          name: '抢占性'
          type: string
          enum:
          - MAYPRE-EMPTION
          - NOTPRE-EMPTION
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PREVUL:
          name: '被抢占性'
          type: string
          enum:
          - NOTPRE-EMPTABLE
          - PRE-EMPTABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        QUEUE:
          name: '排队属性'
          type: string
          enum:
          - NOTQUEUING
          - QUEUING
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DESCRIPTION:
          name: '描述'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    set_sys_list:
    - DESC: 'TEUSNH02'
      ID: 0
      NM: 'TEUSNH02'
      LOC: 'TE'
      SRV: 'vUSN'
      MCC: '432'
      MNC: '35'
      PROVER: R4
      CNID: 51
      CAP: 255
      TMSIALLOC: ENHAN
    add_hplmn_list:
    - MCC: '432'
      MNC: '02'
      CC: '98'
      MNOID: 128
      SM: YES
      MAXSMNUM: 11
      SMS: NO
      LCS: YES
      S5S8TYPE: GTP
      PLMNN: 'PLMNA'
      SMSCR: NO
    set_sigattr_list:
    - IF: INVALID
      IRF: INVALID
      NF: LABEL14
      NRF: LABEL14
      M3UASTPF: DISABLE
      BSSAPPF: ENABLE
      BSSAPPNO: 252
      BSSAPPNI: NATB
      MAPNI: NATB
      SS7T: ITUT_SS7
    add_l3vpninst_list:
    - VRFNAME: 'vpn_iuup'
    add_vpninstaf_list:
    - VRFNAME: 'vpn_iuup'
      AFTYPE: ipv4uni
    mod_interface_list:
    - IFNAME: 'Ethernet64/0/4'
      IFADMINSTATUS: up
      IFMTU: 1500
      IFDF: FALSE
      IFSTATIENABLE: TRUE
      IFTRAPENABLE: TRUE
      IFSTATITVL: 5
    add_interface_list:
    - IFNAME: 'Ethernet64/0/4.2122'
      IFADMINSTATUS: up
      IFMTU: 1500
      IFDF: FALSE
      IFSTATIENABLE: FALSE
      IFTRAPENABLE: TRUE
      IFSTATITVL: 5
    add_ipbindvpn_list:
    - IFNAME: 'Ethernet64/0/4.2122'
      VRFNAME: 'vpn_iuup'
    add_ethsubif_list:
    - IFNAME: 'Ethernet64/0/4.2122'
      SUBIFTYPE: VlanType
      VLANTYPEVID: 2122
    add_ifipv4address_list:
    - IFNAME: 'Ethernet64/0/4.2122'
      IFIPADDR: '10.220.81.98'
      SUBNETMASK: '255.255.255.240'
      ADDRTYPE: main
    add_ospf_list:
    - PROCID: 187
      VRFNAME: 'vpn_iuup'
      SCHEMAROUID: '10.220.95.17'
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
    - PROCID: 187
      AREAID: '0.0.0.33'
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
    - PROCID: 187
      AREAID: '0.0.0.33'
      IPADDRESS: '10.220.81.96'
      WILDCARDMASK: '0.0.0.15'
    add_ospfimportroute_list:
    - PROCID: 187
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
    - PROCID: 187
      AREAID: '0.0.0.33'
      IFNAME: 'Ethernet64/0/4.2122'
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
      SERVICEIPV4: '10.220.96.130'
      VPNINSTNAME: 'vpn_iucp'
      DESC: 'Iu-c'
      IPV6MTU: 1500
      SERVICEIPV6: ''
    add_m3le_list:
    - LEX: 1
      NI: NATB
      OPC: '0x1BCA'
      LET: IPSP
      LEN: 'TEUSNH02_IuC'
    add_m3de_list:
    - DEX: 3
      LEX: 1
      DPC: '0xB40'
      SLSSM: B0000
      STPF: DISABLE
      DET: IPSP
      ADJF: TRUE
      NMD: EXCLUSIVE
      PVER: RFC3332
      DEN: 'KRRNCH4'
    add_m3lks_list:
    - LSX: 3
      DEX: 3
      SLSM: B0011
      WM: IPSP
      TM: LOADSHARE
      LSN: 'KRRNCH4'
    add_m3rt_list:
    - RTX: 3
      DEX: 3
      LSX: 3
      PRI: 0
      RTN: 'KRRNCH4'
    add_sctppara_list:
    - SCTPPARAINDEX: 0
      RTOMIN: 120
      RTOMAX: 800
      RTOINIT: 120
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
      SCTPPARANAME: 'Iu&Gr'
      PKGERRFAULT: 5
      PKGERRRECOVER: 3
      MINRECVPKGNUM: 100
    add_m3lnk_list:
    - LNK: 30
      VPNNAME: 'vpn_iucp'
      IPT: IPV4
      LOCIPV41: '10.220.96.130'
      LOCIPV42: '10.220.96.131'
      LOCPORT: 8000
      PEERIPV41: '10.184.57.48'
      PEERIPV42: '10.184.57.51'
      PEERPORT: 3008
      CS: S
      LSX: 3
      ASF: ACT
      PRI: 0
      CONSTHD: 80
      CONETHD: 40
      CROSSIP: NO
      SCTPINDX: 0
      EXCHGMODE: SINGLE
      LKN: 'KRRNCH4_S_04'
      LOCIPV61: ''
      LOCIPV62: ''
      PEERIPV61: ''
      PEERIPV62: ''
    add_sccpopc_list:
    - OPX: 2
      NI: NATB
      OPC: '0x1BCA'
      SPN: IUONLY
      OPN: 'TEUSNH02_IuC'
      SGSNN: ''
    add_sccpdpc_list:
    - DPX: 50
      OPX: 2
      DPC: '0xB40'
      SS7T: ITUT_SS7
      LDP: NOUSE
      DPN: 'KRRNCH4'
      BDPX: ''
      SDPX: ''
    add_sccpssn_list:
    - SSNX: 12
      SSN: RANAP
      NI: NATB
      DPC: '0xB40'
      OPC: '0x1BCA'
      SSNNAME: 'KR_RNCH4_RANAP'
      LOADSHARETYPE: NOUSE
      BACKUPINDEX: ''
    set_sccptmr_list:
    - TCONNEST: 90
      TIAS: 450
      TIAR: 1000
      TREL: 15
      TREPEATREL: 15
      TINTERVAL: 60
      TGUARD: 1440
      TRESET: 15
      TREASSEMBLY: 15
      TSTATINFO: 60
      TCOORDCHG: 90
      TIGNORESST: 60
      TFREEZEN: 30
      TEA: 10
      TLRN: 15
      TRESOURCE: 3600
    add_rnc_list:
    - RNCX: 100
      RNCN: 'KRRNCH4'
      RNCMCC: '432'
      RNCMNC: '35'
      RNCID: 3003
      NI: NATB
      SPC: '0xB40'
      TRLCTMR: 50000
      TRLCCMP: 55000
      TRABASSGT: 15000
      TIGOC: 60
      TINTC: 90
      TRAFR: 60
      TRATR: 60
      CNID: 51
      IMS: NO
      IU_FLEX: NO
      RANSHR: NO
      UESBI: NO
      RNCVER: R7
      SENDRESET: 3
      IPV6ATTR: NO
      SNDOVERLOAD: NO
      OTS: YES
      R7QOS: YES
      RABQOS: NO
      ALTBRTYPE: VALUERANGE
      CHGSYMTOASYMBI: NO
      SGSNBUF: NO
      OFUTRAN: NO
      SPID: NO
    add_iupaging_list:
    - LAI: '4323556CE'
      RAC: '0x01'
      RNCINDEX: 100
    set_iuload_list:
    - IUSHSPT: YES
      NTMR: 5
      OVERLOADTMR: 40
    add_iuauthciph_list:
    - IMSIPRE: 'ALL_USER'
      SECPLC: AUTHANDPROTECTED
      AUTHEVENT: DETACH-0&IMSI_ATTACH-1&INTER_RAU-1&INTER_RAU_AFTER_RELOCATOIN-1&INTRA_RAU-0&INTRA_RAU_AFTER_RELOCATOIN-0&LCS-1&MS_SERVICE_REQ-0&PAGING_RSP-0&PROD_RAU-0&PTMSI_ATTACH-1&PTMSI_SIG_NOMATCH-0&PTMSI_SIG_NOSIG-0&SMS_MO-1&SMS_MT-1&SYSTEM_CHANGE_INTRA_RAU-1
      AUTHPERIOD: 0
      AUTHEVENTTHRESHOLD: 1
      ATTSAUTH: NO
      RAUSAUTH: NO
      AUTHSETV2: NO
      AUTHSETSNUMBER: 4
      PREGETAUTHSETS: YES
      GETAUTHADVTH: 1
      REAUTH: NO
      CAFTIMES: 3
      CIPHALG: NO_ENCRYPTION-1&UEA1-1&UEA2-1
      INTALG: UIA1-1&UIA2-1
      IDRQ: YES
    set_iudetach_list:
    - DETACHSW: YES
      NACTTMR: 120
      DETACHONFOR: NO
      DETACHONCONN: NO
      NACTTMRONCONN: 0
      REATM: 0
      ONLINETIMER: 60
      ONLINEFOREVER: NO
      IMPDTCHNORSP: YES
      IMPDTCH: IMPLICITLY
      IMPIUONNONACT: IMPLICITLY
      IMPONIUREL: NO
    add_iupaging_list_1:
    - LAI: '4323556CE'
      RAC: '0x01'
      RNCINDEX: 100
    set_iusm_list:
    - T3385: 8
      N3385: 4
      T3386: 8
      N3386: 4
      T3395: 8
      N3395: 4
    add_gtpule_list:
    - GROUPID: 32
      IPTYPE: TPTADDR_TYPE_IPV4
      LEIPV4: '10.220.96.132'
      VPNNAME: 'vpn_iuup'
      DESC: 'Iu-u'
      LEIPV6: ''
    add_l3vpninst_list_2:
    - VRFNAME: 'vpn_SIG'
      VRFDESCRIPTION: 'vpn_SIG'
    add_vpninstaf_list_2:
    - VRFNAME: 'vpn_SIG'
      AFTYPE: ipv4uni
    mod_interface_list_8:
    - IFNAME: 'Ethernet64/0/8'
      IFADMINSTATUS: up
      IFMTU: 1500
      IFDF: FALSE
      IFSTATIENABLE: TRUE
      IFTRAPENABLE: TRUE
      IFSTATITVL: 5
    add_interface_list_10:
    - IFNAME: 'Ethernet64/0/8.2130'
      IFADMINSTATUS: up
      IFMTU: 1500
      IFDF: FALSE
      IFSTATIENABLE: FALSE
      IFTRAPENABLE: TRUE
      IFSTATITVL: 5
    add_ipbindvpn_list_10:
    - IFNAME: 'Ethernet64/0/8.2130'
      VRFNAME: 'vpn_SIG'
    add_ethsubif_list_8:
    - IFNAME: 'Ethernet64/0/8.2130'
      SUBIFTYPE: VlanType
      VLANTYPEVID: 2130
    add_ifipv4address_list_10:
    - IFNAME: 'Ethernet64/0/8.2130'
      IFIPADDR: '10.220.82.98'
      SUBNETMASK: '255.255.255.240'
      ADDRTYPE: main
    add_ospf_list_2:
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
    add_ospfarea_list_2:
    - PROCID: 668
      AREAID: '0.0.0.33'
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
    - PROCID: 668
      AREAID: '0.0.0.33'
      IPADDRESS: '10.220.82.96'
      WILDCARDMASK: '0.0.0.15'
    add_ospfimportroute_list_2:
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
    add_ospfinterface_list_8:
    - PROCID: 668
      AREAID: '0.0.0.33'
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
    add_serviceip_list_4:
    - IPVERSION: IPv4
      SERVICEIPV4: '10.220.96.136'
      VPNINSTNAME: 'vpn_SIG'
      DESC: 'Gr'
      IPV6MTU: 1500
      SERVICEIPV6: ''
    add_m3le_list_1:
    - LEX: 0
      NI: NAT
      OPC: '0x30a'
      LET: IPSP
      RC: 123456
      NA: 789456
      LEN: 'to SS7'
    add_m3de_list_1:
    - DEX: 3
      LEX: 0
      DPC: '0x20b'
      SLSSM: B0000
      DET: IPSP
      ADJF: TRUE
      RC: 123456
      PVER: RFC3332
      DEN: 'to HLR'
    add_m3lks_list_1:
    - LSX: 1
      DEX: 3
      SLSM: B0010
      WM: IPSP
      TM: LOADSHARE
      LSN: 'to HLR'
    add_m3rt_list_1:
    - RTX: 1
      DEX: 3
      LSX: 1
      RTN: 'to HLR'
    add_sctppara_list_1:
    - SCTPPARAINDEX: 1
      SCTPPARANAME: 'sctppara1'
    add_m3lnk_list_4:
    - LNK: 1
      VPNNAME: 'VPN_SIG'
      IPT: IPV4
      LOCIPV41: '10.11.150.1'
      LOCIPV42: '10.11.182.1'
      LOCPORT: 2906
      PEERIPV41: '10.11.128.25'
      PEERIPV42: '10.11.160.25'
      PEERPORT: 2905
      CS: C
      LSX: 1
      SCTPINDX: 1
      LKN: 'TO HLR LINK2'
      LOCIPV61: ''
      LOCIPV62: ''
      PEERIPV61: ''
      PEERIPV62: ''
    add_m3le_list_2:
    - LEX: 0
      NI: NATB
      OPC: '0x1BC9'
      LET: ASP
      LEN: 'TEUSNH02_Gr'
    add_m3de_list_2:
    - DEX: 1
      LEX: 0
      DPC: '0x1B70'
      SLSSM: B0000
      STPF: DISABLE
      DET: SGP
      ADJF: TRUE
      NMD: EXCLUSIVE
      RC: 0
      PVER: RFC3332
      DEN: 'TE_STP'
    add_m3lks_list_2:
    - LSX: 0
      DEX: 1
      SLSM: B0111
      WM: ASP
      TM: LOADSHARE
      LSN: 'TESTPH01'
    add_m3rt_list_2:
    - RTX: 0
      DEX: 1
      LSX: 0
      PRI: 0
      RTN: 'TESTPH01'
    add_m3lnk_list_5:
    - LNK: 0
      VPNNAME: 'vpn_SIG'
      IPT: IPV4
      LOCIPV41: '10.220.96.136'
      LOCIPV42: '10.220.96.137'
      LOCPORT: 2941
      PEERIPV41: '10.132.228.15'
      PEERIPV42: '10.132.228.47'
      PEERPORT: 2842
      CS: C
      LSX: 0
      ASF: ACT
      PRI: 0
      CONSTHD: 80
      CONETHD: 40
      CROSSIP: NO
      SCTPINDX: 0
      EXCHGMODE: SINGLE
      LKN: 'TESTPH01_C_1'
      LOCIPV61: ''
      LOCIPV62: ''
      PEERIPV61: ''
      PEERIPV62: ''
    add_sccpopc_list_1:
    - OPX: 1
      NI: NATB
      OPC: '0x1BC9'
      SPN: COREONLY
      SGSNN: '989350071130'
      OPN: 'TEUSNH02'
    add_sccpdpc_list_1:
    - DPX: 1
      OPX: 1
      DPC: '0x1B70'
      SS7T: ITUT_SS7
      LDP: LOADSHARE
      SDPX: 2
      DPN: 'TESTPH01'
      BDPX: ''
    add_sccpssn_list_2:
    - SSNX: 0
      SSN: SGSN
      NI: NATB
      DPC: '0x1BC9'
      OPC: '0x1BC9'
      SSNNAME: 'TEUSNH02_Local_SSN'
      LOADSHARETYPE: NOUSE
      BACKUPINDEX: ''
    add_imsigt_list:
    - IMSIPRE: '43202000'
      GT: '98935'
      MNNAME: 'MVNO'
    add_connectplmn_list:
    - MCC: '460'
      MNC: '00'
      CC: '86'
      NOID: 0
      SM: YES
      MAXSMNUM: 11
      SMS: YES
      SMSCR: NO
      LCS: YES
      S5S8TYPE: GTP
      COUNTRYORAREANAME: 'China mobile'
      EXCLUSIVEPLMN: NO
      SMSCT: ''
    add_sccpgt_list:
    - GTX: 1
      NI: NATB
      RT: DPCGT
      GTEXP: FOUR
      NP: ISDNP
      ADDREXP: INTDN
      ADDR: '98'
      DPC: '0x1B70'
      NAME: 'MTNIrancell'
      TT: ANSI9
      NGTX: ''
      SSN: ''
    add_l3vpninst_list_3:
    - VRFNAME: 'vpn_gn_1'
    add_vpninstaf_list_3:
    - VRFNAME: 'vpn_gn_1'
      AFTYPE: ipv4uni
    mod_interface_list_12:
    - IFNAME: 'Ethernet64/0/6'
      IFADMINSTATUS: up
      IFMTU: 1500
      IFDF: FALSE
      IFSTATIENABLE: TRUE
      IFTRAPENABLE: TRUE
      IFSTATITVL: 5
    add_interface_list_15:
    - IFNAME: 'Ethernet64/0/4.2124'
      IFADMINSTATUS: up
      IFMTU: 1500
      IFDF: FALSE
      IFSTATIENABLE: FALSE
      IFTRAPENABLE: TRUE
      IFSTATITVL: 5
    add_ipbindvpn_list_15:
    - IFNAME: 'Ethernet64/0/6.2126'
      VRFNAME: 'vpn_gn_1'
    add_ethsubif_list_12:
    - IFNAME: 'Ethernet64/0/6.2126'
      SUBIFTYPE: VlanType
      VLANTYPEVID: 2126
    add_ifipv4address_list_15:
    - IFNAME: 'Ethernet64/0/4.2124'
      IFIPADDR: '10.220.83.98'
      SUBNETMASK: '255.255.255.240'
      ADDRTYPE: main
    add_ospf_list_3:
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
    add_ospfarea_list_3:
    - PROCID: 224
      AREAID: '0.0.0.33'
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
    add_ospfnetwork_list_9:
    - PROCID: 224
      AREAID: '0.0.0.33'
      IPADDRESS: '10.220.83.96'
      WILDCARDMASK: '0.0.0.15'
    add_ospfimportroute_list_3:
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
    add_ospfinterface_list_12:
    - PROCID: 224
      AREAID: '0.0.0.33'
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
    add_serviceip_list_6:
    - IPVERSION: IPv4
      SERVICEIPV4: '10.42.48.113'
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
    add_gtpule_list_2:
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
      PE: 'vUSN'
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
    add_ipv4dnsh_list:
    - HSINDEX: 666
      HOSTNAME: 'APTEL.MNC002.MCC432.GPRS'
      ADDRSECTION: SECTION1
      IPV4ADDR1: '10.42.48.12'
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
    add_ggsncharact_list:
    - RANGE: SPECIAL_GGSN
      IPT: IPV4
      GGSNIPV4: '10.10.0.100'
      MASKV4: '255.255.255.255'
      QOSVER: R5QOS
      GGSNIPV6: ''
      MASKV6: ''
    add_l3vpninst_list_4:
    - VRFNAME: 'vpn_ga_1'
    add_vpninstaf_list_4:
    - VRFNAME: 'vpn_ga_1'
      AFTYPE: ipv4uni
    mod_interface_list_16:
    - IFNAME: 'Ethernet64/0/8'
      IFADMINSTATUS: up
      IFMTU: 1500
      IFDF: FALSE
      IFSTATIENABLE: TRUE
      IFTRAPENABLE: TRUE
      IFSTATITVL: 5
    add_interface_list_20:
    - IFNAME: 'Ethernet64/0/8.2132'
      IFADMINSTATUS: up
      IFMTU: 1500
      IFDF: FALSE
      IFSTATIENABLE: FALSE
      IFTRAPENABLE: TRUE
      IFSTATITVL: 5
    add_ipbindvpn_list_20:
    - IFNAME: 'Ethernet64/0/9.2133'
      VRFNAME: 'vpn_ga_1'
    add_ethsubif_list_16:
    - IFNAME: 'Ethernet64/0/8.2132'
      SUBIFTYPE: VlanType
      VLANTYPEVID: 2132
    add_ifipv4address_list_20:
    - IFNAME: 'Ethernet64/0/8.2132'
      IFIPADDR: '10.220.82.162'
      SUBNETMASK: '255.255.255.240'
      ADDRTYPE: main
    add_ospf_list_4:
    - PROCID: 181
      VRFNAME: 'vpn_ga_1'
      SCHEMAROUID: '10.220.95.27'
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
    add_ospfarea_list_4:
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
    add_ospfnetwork_list_12:
    - PROCID: 181
      AREAID: '0.0.0.33'
      IPADDRESS: '10.220.82.160'
      WILDCARDMASK: '0.0.0.15'
    add_ospfimportroute_list_4:
    - PROCID: 181
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
    set_bfd_list_1:
    - BFDENABLE: TRUE
      DELAYUPTIMER: 0
      TOSEXP: 7
    add_ospfinterface_list_16:
    - PROCID: 181
      AREAID: '0.0.0.33'
      IFNAME: 'Ethernet64/0/8.2132'
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
    add_serviceip_list_9:
    - IPVERSION: IPv4
      SERVICEIPV4: '10.220.96.146'
      VPNINSTNAME: 'vpn_ga_1'
      DESC: 'Ga'
      IPV6MTU: 1500
      SERVICEIPV6: ''
    add_chgcdpip_list:
    - IPT: IPv4
      IPV4ADDR: '10.220.96.146'
      PORTBGN: 1024
      PORTEND: 1151
      VPNNAME: 'vpn_ga_1'
      IPV6ADDR: ''
    add_chgcg_list:
    - IP: '10.220.96.21'
      GRD: 1
      PRO: UDP
      CGR: R9
      SPN: 3386
      DEFAULTCG: YES
      CGN: 'TECGH01'
      IPT: IPV4
    set_chgga_list:
    - GCR: R9
      UCR: R9
      CHGVER98: CMCCV130
      CHGVER99: GPP32015V360
      CHGVER4: GPP32215V440
      CHGVER5: GPP32215V560
      CHGVER6: GPP32251V660
      CHGVER7: GPP32251V740
      CHGVER9: GPP32251V940
      ITVRES: 3
      RSNUM: 3
      HDDETH: 5
      HDDFSL: 70
      REDICTFRMMAXOCCRATE: 80
      QOSVER: R5
      GASENDUDPCHECK: DISABLE
      GAREVUDPCHECK: DISABLE
      CDROVERWRITE: NO
    add_chgbeha_list:
    - CB: B1
      BA: NOROAMING
      ACC: HOTBILLING-1&FLATRATE-1&PREPAID-1&NORMAL-1
      IPT: IPV4
      PURGELEN: ''
      SMSCADDR: ''
    set_chgchar_list:
    - CC: HOTBILLING
      MP: NO
      MPCP: NO
      MPL: 60
      MLCP: NO
      MLCL: 5
      RPCMCDR: NO
      SP: YES
      SPP: FORBID
      SPL: 60
      SVP: NO
      SVL: 1000
      SCCP: YES
      SCCL: 3
      SLCP: NO
      PCC: NO
      RPCSCDR: NO
      SMOP: NO
      SMTP: NO
      LCSMOP: NO
      LCSMTP: NO
      LCSNIP: NO
      SR: UNRESTRICT
      CGIP: '0.0.0.0'
      TARIACCFLG: HOME_USER-1&ROAM_USER-1&VISIT_USER-1
    set_chgwkdy_list:
    - WKDAY: SUN
      CC: HOTBILLING
      TT: WEEKEND
    add_chgtari_list:
    - TT: WORK
      ST: '00&00&00'
      ET: '00&00&00'
      CC: HOTBILLING
    set_sigattr_list_1:
    - IF: LABEL24
      IRF: LABEL14
      NF: LABEL14
      NRF: LABEL14
      M3UASTPF: ENABLE
      BSSAPPF: ENABLE
      BSSAPPNO: 252
      BSSAPPNI: DISUSED
      MAPNI: NAT
      SS7T: ITUT_SS7
    add_serviceip_list_10:
    - IPVERSION: IPv4
      SERVICEIPV4: '10.42.48.113'
      VPNINSTNAME: 'vpn_gn_1'
      IPV6MTU: 1500
      SERVICEIPV6: ''
    add_dnsle_list:
    - IPT: IPV4
      IPV4: '10.42.48.113'
      LOCPORT: 15000
      VPNNAME: 'vpn_gn_1'
      LENAME: 'TEUSNH02'
      IPV6: ''
    add_dnss_list:
    - GRPID: 0
      IP: '10.178.167.22'
      PRI: PRI1
      DNSSNAME: 'MSDNSE01'
      PRO: UDP
      IPT: IPV4
    set_dns_list:
    - TMS: 3
      TRT: 1000
      DDS: ON
      DDI: 3
      SFT: 3
      DDN: 'huawei.com'
      DISCACHEPURGESW: OFF
      IPSORTMODE: PRI_WGT
      CNAMESW: OFF
      RCRSPTM: 3
      RCQRYTM: 3
      FAILTM: 60
      PAUSETM: 60
      RCUPDTM: 500
      RCUSEDTM: 600
      LOCALTTL: 0
      REROUTECAUSE: FORMTERR-0&NMERROR-0&NOTIMPLT-0&REFUSED-0&SEVFAIL-0
    add_iuauthciph_list_1:
    - IMSIPRE: '012544'
      SECPLC: AUTHANDPROTECTED
      AUTHEVENT: INTER_RAU-1&PTMSI_ATTACH-1&IMSI_ATTACH-1&PTMSI_SIG_NOMATCH-1&PTMSI_SIG_NOSIG-1
      AUTHEVENTTHRESHOLD: 257
      ATTSAUTH: NO
      RAUSAUTH: NO
      AUTHSETV2: NO
      REAUTH: YES
      CIPHALG: UEA1-1&UEA2-1
      INTALG: UIA1-1&UIA2-1
      AUTHPERIOD: 24
      AUTHSETSNUMBER: 5
      CAFTIMES: 3
      GETAUTHADVTH: ''
      PREGETAUTHSETS: YES
    add_algpriority_list:
    - ALGTYPE: CIPH
      ALGCIPH: UEA1
      ALGPRI: 1
      ALGINTE: ''
    add_arppara_list:
    - GROUPID: G0
      USRPRI: HIGHLEVELUSER
      SRVLVL: CONVERSATION
      PRTLVL: 4
      PRELVL: MAYPRE-EMPTION
      PREVUL: NOTPRE-EMPTABLE
      QUEUE: QUEUING
      DESCRIPTION: ''
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 进入“MML命令行-UNC”窗口。

### 2 配置本局信息，包括归属PLMN和系统信息以及本局7号信令数据。

```jinja2
{%- for item in set_sys_list -%}
    SET SYS:
    {#- --- 可选参数 --- -#}
    {%- if item.DESC is not none -%}
        DESC="{{item.DESC}}",
    {%- endif -%}
    {%- if item.ID is not none -%}
        ID={{item.ID}},
    {%- endif -%}
    {%- if item.NM is not none -%}
        NM="{{item.NM}}",
    {%- endif -%}
    {%- if item.LOC is not none -%}
        LOC="{{item.LOC}}",
    {%- endif -%}
    {%- if item.SRV is not none -%}
        SRV="{{item.SRV}}",
    {%- endif -%}
    {%- if item.MCC is not none -%}
        MCC="{{item.MCC}}",
    {%- endif -%}
    {%- if item.MNC is not none -%}
        MNC="{{item.MNC}}",
    {%- endif -%}
    {%- if item.PROVER is not none -%}
        PROVER={{item.PROVER}},
    {%- endif -%}
    {%- if item.CNID is not none -%}
        CNID={{item.CNID}},
    {%- endif -%}
    {%- if item.CAP is not none -%}
        CAP={{item.CAP}},
    {%- endif -%}
    {%- if item.TMSIALLOC is not none -%}
        TMSIALLOC={{item.TMSIALLOC}},
    {%- endif -%}
    ;
{%- endfor -%}
```

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
    {%- if item.MNOID is not none -%}
        MNOID={{item.MNOID}},
    {%- endif -%}
    {%- if item.SM is not none -%}
        SM={{item.SM}},
    {%- endif -%}
    {%- if item.SMS is not none -%}
        SMS={{item.SMS}},
    {%- endif -%}
    {%- if item.LCS is not none -%}
        LCS={{item.LCS}},
    {%- endif -%}
    {%- if item.S5S8TYPE is not none -%}
        S5S8TYPE={{item.S5S8TYPE}},
    {%- endif -%}
    {%- if item.PLMNN is not none -%}
        PLMNN="{{item.PLMNN}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：SM=YES 时可选 --- -#}
    {%- if item.SM == 'YES' -%}
        {%- if item.MAXSMNUM is not none -%}
            MAXSMNUM={{item.MAXSMNUM}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SMS=YES 时可选 --- -#}
    {%- if item.SMS == 'YES' -%}
        {%- if item.SMSCR is not none -%}
            SMSCR={{item.SMSCR}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in set_sigattr_list -%}
    SET SIGATTR:
    {#- --- 可选参数 --- -#}
    {%- if item.IF is not none -%}
        IF={{item.IF}},
    {%- endif -%}
    {%- if item.IRF is not none -%}
        IRF={{item.IRF}},
    {%- endif -%}
    {%- if item.NF is not none -%}
        NF={{item.NF}},
    {%- endif -%}
    {%- if item.NRF is not none -%}
        NRF={{item.NRF}},
    {%- endif -%}
    {%- if item.M3UASTPF is not none -%}
        M3UASTPF={{item.M3UASTPF}},
    {%- endif -%}
    {%- if item.BSSAPPF is not none -%}
        BSSAPPF={{item.BSSAPPF}},
    {%- endif -%}
    {%- if item.BSSAPPNO is not none -%}
        BSSAPPNO={{item.BSSAPPNO}},
    {%- endif -%}
    {%- if item.BSSAPPNI is not none -%}
        BSSAPPNI={{item.BSSAPPNI}},
    {%- endif -%}
    {%- if item.MAPNI is not none -%}
        MAPNI={{item.MAPNI}},
    {%- endif -%}
    {%- if item.SS7T is not none -%}
        SS7T={{item.SS7T}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 配置Iu接口数据。

#### 3.1 配置动态路由OSPF。

##### 3.1.1 配置VPN实例。

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

#### 3.3 配置Iu接口业务IP。

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

#### 3.4 配置M3UA信令数据。

```jinja2
{%- for item in add_m3le_list -%}
    ADD M3LE:
    {#- --- 必选参数 --- -#}
    LEX={{item.LEX}},
    NI={{item.NI}},
    OPC="{{item.OPC}}",
    LET={{item.LET}},
    {#- --- 可选参数 --- -#}
    {%- if item.LEN is not none -%}
        LEN="{{item.LEN}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_m3de_list -%}
    ADD M3DE:
    {#- --- 必选参数 --- -#}
    DEX={{item.DEX}},
    LEX={{item.LEX}},
    DPC="{{item.DPC}}",
    DET={{item.DET}},
    {#- --- 可选参数 --- -#}
    {%- if item.SLSSM is not none -%}
        SLSSM={{item.SLSSM}},
    {%- endif -%}
    {%- if item.STPF is not none -%}
        STPF={{item.STPF}},
    {%- endif -%}
    {%- if item.ADJF is not none -%}
        ADJF={{item.ADJF}},
    {%- endif -%}
    {%- if item.NMD is not none -%}
        NMD={{item.NMD}},
    {%- endif -%}
    {%- if item.PVER is not none -%}
        PVER={{item.PVER}},
    {%- endif -%}
    {%- if item.DEN is not none -%}
        DEN="{{item.DEN}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_m3lks_list -%}
    ADD M3LKS:
    {#- --- 必选参数 --- -#}
    LSX={{item.LSX}},
    DEX={{item.DEX}},
    WM={{item.WM}},
    {#- --- 可选参数 --- -#}
    {%- if item.SLSM is not none -%}
        SLSM={{item.SLSM}},
    {%- endif -%}
    {%- if item.TM is not none -%}
        TM={{item.TM}},
    {%- endif -%}
    {%- if item.LSN is not none -%}
        LSN="{{item.LSN}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_m3rt_list -%}
    ADD M3RT:
    {#- --- 必选参数 --- -#}
    RTX={{item.RTX}},
    DEX={{item.DEX}},
    LSX={{item.LSX}},
    {#- --- 可选参数 --- -#}
    {%- if item.PRI is not none -%}
        PRI={{item.PRI}},
    {%- endif -%}
    {%- if item.RTN is not none -%}
        RTN="{{item.RTN}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

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

```jinja2
{%- for item in add_m3lnk_list -%}
    ADD M3LNK:
    {#- --- 必选参数 --- -#}
    LNK={{item.LNK}},
    CS={{item.CS}},
    LSX={{item.LSX}},
    SCTPINDX={{item.SCTPINDX}},
    {#- --- 可选参数 --- -#}
    {%- if item.VPNNAME is not none -%}
        VPNNAME="{{item.VPNNAME}}",
    {%- endif -%}
    {%- if item.IPT is not none -%}
        IPT={{item.IPT}},
    {%- endif -%}
    {%- if item.LOCPORT is not none -%}
        LOCPORT={{item.LOCPORT}},
    {%- endif -%}
    {%- if item.PEERPORT is not none -%}
        PEERPORT={{item.PEERPORT}},
    {%- endif -%}
    {%- if item.ASF is not none -%}
        ASF={{item.ASF}},
    {%- endif -%}
    {%- if item.PRI is not none -%}
        PRI={{item.PRI}},
    {%- endif -%}
    {%- if item.CONSTHD is not none -%}
        CONSTHD={{item.CONSTHD}},
    {%- endif -%}
    {%- if item.CONETHD is not none -%}
        CONETHD={{item.CONETHD}},
    {%- endif -%}
    {%- if item.CROSSIP is not none -%}
        CROSSIP={{item.CROSSIP}},
    {%- endif -%}
    {%- if item.EXCHGMODE is not none -%}
        EXCHGMODE={{item.EXCHGMODE}},
    {%- endif -%}
    {%- if item.LKN is not none -%}
        LKN="{{item.LKN}}",
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPT=IPV4 时必选 --- -#}
    {%- if item.IPT == 'IPV4' -%}
        LOCIPV41="{{item.LOCIPV41}}",
    {%- endif -%}
    {#- --- 条件必选：IPT=IPV4 时必选 --- -#}
    {%- if item.IPT == 'IPV4' -%}
        PEERIPV41="{{item.PEERIPV41}}",
    {%- endif -%}
    {#- --- 条件必选：IPT=IPV6 时必选 --- -#}
    {%- if item.IPT == 'IPV6' -%}
        LOCIPV61="{{item.LOCIPV61}}",
    {%- endif -%}
    {#- --- 条件必选：IPT=IPV6 时必选 --- -#}
    {%- if item.IPT == 'IPV6' -%}
        PEERIPV61="{{item.PEERIPV61}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：IPT=IPV4 时可选 --- -#}
    {%- if item.IPT == 'IPV4' -%}
        {%- if item.LOCIPV42 is not none -%}
            LOCIPV42="{{item.LOCIPV42}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：IPT=IPV4 时可选 --- -#}
    {%- if item.IPT == 'IPV4' -%}
        {%- if item.PEERIPV42 is not none -%}
            PEERIPV42="{{item.PEERIPV42}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：IPT=IPV6 时可选 --- -#}
    {%- if item.IPT == 'IPV6' -%}
        {%- if item.LOCIPV62 is not none -%}
            LOCIPV62="{{item.LOCIPV62}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：IPT=IPV6 时可选 --- -#}
    {%- if item.IPT == 'IPV6' -%}
        {%- if item.PEERIPV62 is not none -%}
            PEERIPV62="{{item.PEERIPV62}}",
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 3.5 配置SCCP信令数据。

```jinja2
{%- for item in add_sccpopc_list -%}
    ADD SCCPOPC:
    {#- --- 必选参数 --- -#}
    OPX={{item.OPX}},
    NI={{item.NI}},
    OPC="{{item.OPC}}",
    {#- --- 可选参数 --- -#}
    {%- if item.SPN is not none -%}
        SPN={{item.SPN}},
    {%- endif -%}
    {%- if item.OPN is not none -%}
        OPN="{{item.OPN}}",
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：SPN=COREONLY/IUANDCORE 时必选 --- -#}
    {%- if item.SPN in ['COREONLY', 'IUANDCORE'] -%}
        SGSNN="{{item.SGSNN}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_sccpdpc_list -%}
    ADD SCCPDPC:
    {#- --- 必选参数 --- -#}
    DPX={{item.DPX}},
    OPX={{item.OPX}},
    DPC="{{item.DPC}}",
    {#- --- 可选参数 --- -#}
    {%- if item.SS7T is not none -%}
        SS7T={{item.SS7T}},
    {%- endif -%}
    {%- if item.LDP is not none -%}
        LDP={{item.LDP}},
    {%- endif -%}
    {%- if item.DPN is not none -%}
        DPN="{{item.DPN}}",
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：LDP=BACKUP 时必选 --- -#}
    {%- if item.LDP == 'BACKUP' -%}
        BDPX={{item.BDPX}},
    {%- endif -%}
    {#- --- 条件必选：LDP=LOADSHARE 时必选 --- -#}
    {%- if item.LDP == 'LOADSHARE' -%}
        SDPX={{item.SDPX}},
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_sccpssn_list -%}
    ADD SCCPSSN:
    {#- --- 必选参数 --- -#}
    SSNX={{item.SSNX}},
    SSN={{item.SSN}},
    NI={{item.NI}},
    DPC="{{item.DPC}}",
    OPC="{{item.OPC}}",
    {#- --- 可选参数 --- -#}
    {%- if item.SSNNAME is not none -%}
        SSNNAME="{{item.SSNNAME}}",
    {%- endif -%}
    {%- if item.LOADSHARETYPE is not none -%}
        LOADSHARETYPE={{item.LOADSHARETYPE}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：LOADSHARETYPE=BACKUP 时必选 --- -#}
    {%- if item.LOADSHARETYPE == 'BACKUP' -%}
        BACKUPINDEX={{item.BACKUPINDEX}},
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in set_sccptmr_list -%}
    SET SCCPTMR:
    {#- --- 可选参数 --- -#}
    {%- if item.TCONNEST is not none -%}
        TCONNEST={{item.TCONNEST}},
    {%- endif -%}
    {%- if item.TIAS is not none -%}
        TIAS={{item.TIAS}},
    {%- endif -%}
    {%- if item.TIAR is not none -%}
        TIAR={{item.TIAR}},
    {%- endif -%}
    {%- if item.TREL is not none -%}
        TREL={{item.TREL}},
    {%- endif -%}
    {%- if item.TREPEATREL is not none -%}
        TREPEATREL={{item.TREPEATREL}},
    {%- endif -%}
    {%- if item.TINTERVAL is not none -%}
        TINTERVAL={{item.TINTERVAL}},
    {%- endif -%}
    {%- if item.TGUARD is not none -%}
        TGUARD={{item.TGUARD}},
    {%- endif -%}
    {%- if item.TRESET is not none -%}
        TRESET={{item.TRESET}},
    {%- endif -%}
    {%- if item.TREASSEMBLY is not none -%}
        TREASSEMBLY={{item.TREASSEMBLY}},
    {%- endif -%}
    {%- if item.TSTATINFO is not none -%}
        TSTATINFO={{item.TSTATINFO}},
    {%- endif -%}
    {%- if item.TCOORDCHG is not none -%}
        TCOORDCHG={{item.TCOORDCHG}},
    {%- endif -%}
    {%- if item.TIGNORESST is not none -%}
        TIGNORESST={{item.TIGNORESST}},
    {%- endif -%}
    {%- if item.TFREEZEN is not none -%}
        TFREEZEN={{item.TFREEZEN}},
    {%- endif -%}
    {%- if item.TEA is not none -%}
        TEA={{item.TEA}},
    {%- endif -%}
    {%- if item.TLRN is not none -%}
        TLRN={{item.TLRN}},
    {%- endif -%}
    {%- if item.TRESOURCE is not none -%}
        TRESOURCE={{item.TRESOURCE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 3.6 配置RNC相关信息。

```jinja2
{%- for item in add_rnc_list -%}
    ADD RNC:
    {#- --- 必选参数 --- -#}
    RNCX={{item.RNCX}},
    RNCMCC="{{item.RNCMCC}}",
    RNCMNC="{{item.RNCMNC}}",
    RNCID={{item.RNCID}},
    NI={{item.NI}},
    SPC="{{item.SPC}}",
    {#- --- 可选参数 --- -#}
    {%- if item.RNCN is not none -%}
        RNCN="{{item.RNCN}}",
    {%- endif -%}
    {%- if item.TRLCTMR is not none -%}
        TRLCTMR={{item.TRLCTMR}},
    {%- endif -%}
    {%- if item.TRLCCMP is not none -%}
        TRLCCMP={{item.TRLCCMP}},
    {%- endif -%}
    {%- if item.TRABASSGT is not none -%}
        TRABASSGT={{item.TRABASSGT}},
    {%- endif -%}
    {%- if item.TIGOC is not none -%}
        TIGOC={{item.TIGOC}},
    {%- endif -%}
    {%- if item.TINTC is not none -%}
        TINTC={{item.TINTC}},
    {%- endif -%}
    {%- if item.TRAFR is not none -%}
        TRAFR={{item.TRAFR}},
    {%- endif -%}
    {%- if item.TRATR is not none -%}
        TRATR={{item.TRATR}},
    {%- endif -%}
    {%- if item.CNID is not none -%}
        CNID={{item.CNID}},
    {%- endif -%}
    {%- if item.IMS is not none -%}
        IMS={{item.IMS}},
    {%- endif -%}
    {%- if item.IU_FLEX is not none -%}
        IU_FLEX={{item.IU_FLEX}},
    {%- endif -%}
    {%- if item.RANSHR is not none -%}
        RANSHR={{item.RANSHR}},
    {%- endif -%}
    {%- if item.UESBI is not none -%}
        UESBI={{item.UESBI}},
    {%- endif -%}
    {%- if item.RNCVER is not none -%}
        RNCVER={{item.RNCVER}},
    {%- endif -%}
    {%- if item.SENDRESET is not none -%}
        SENDRESET={{item.SENDRESET}},
    {%- endif -%}
    {%- if item.IPV6ATTR is not none -%}
        IPV6ATTR={{item.IPV6ATTR}},
    {%- endif -%}
    {%- if item.SNDOVERLOAD is not none -%}
        SNDOVERLOAD={{item.SNDOVERLOAD}},
    {%- endif -%}
    {%- if item.OTS is not none -%}
        OTS={{item.OTS}},
    {%- endif -%}
    {%- if item.R7QOS is not none -%}
        R7QOS={{item.R7QOS}},
    {%- endif -%}
    {%- if item.RABQOS is not none -%}
        RABQOS={{item.RABQOS}},
    {%- endif -%}
    {%- if item.ALTBRTYPE is not none -%}
        ALTBRTYPE={{item.ALTBRTYPE}},
    {%- endif -%}
    {%- if item.CHGSYMTOASYMBI is not none -%}
        CHGSYMTOASYMBI={{item.CHGSYMTOASYMBI}},
    {%- endif -%}
    {%- if item.SGSNBUF is not none -%}
        SGSNBUF={{item.SGSNBUF}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：RNCVER=R9+ 时可选 --- -#}
    {%- if item.RNCVER == 'R9+' -%}
        {%- if item.OFUTRAN is not none -%}
            OFUTRAN={{item.OFUTRAN}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：RNCVER=R8/R9+ 时可选 --- -#}
    {%- if item.RNCVER in ['R8', 'R9+'] -%}
        {%- if item.SPID is not none -%}
            SPID={{item.SPID}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_iupaging_list -%}
    ADD IUPAGING:
    {#- --- 必选参数 --- -#}
    LAI="{{item.LAI}}",
    RAC="{{item.RAC}}",
    RNCINDEX={{item.RNCINDEX}},
    ;
{%- endfor -%}
```

```jinja2
{%- for item in set_iuload_list -%}
    SET IULOAD:
    {#- --- 可选参数 --- -#}
    {%- if item.IUSHSPT is not none -%}
        IUSHSPT={{item.IUSHSPT}},
    {%- endif -%}
    {%- if item.NTMR is not none -%}
        NTMR={{item.NTMR}},
    {%- endif -%}
    {%- if item.OVERLOADTMR is not none -%}
        OVERLOADTMR={{item.OVERLOADTMR}},
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_iuauthciph_list -%}
    ADD IUAUTHCIPH:
    {#- --- 必选参数 --- -#}
    IMSIPRE="{{item.IMSIPRE}}",
    {#- --- 可选参数 --- -#}
    {%- if item.SECPLC is not none -%}
        SECPLC={{item.SECPLC}},
    {%- endif -%}
    {%- if item.IDRQ is not none -%}
        IDRQ={{item.IDRQ}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：SECPLC=AUTHONLY/AUTHANDPROTECTED 时可选 --- -#}
    {%- if item.SECPLC in ['AUTHONLY', 'AUTHANDPROTECTED'] -%}
        {%- if item.AUTHEVENT is not none -%}
            AUTHEVENT={{item.AUTHEVENT}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SECPLC=AUTHONLY/AUTHANDPROTECTED 时可选 --- -#}
    {%- if item.SECPLC in ['AUTHONLY', 'AUTHANDPROTECTED'] -%}
        {%- if item.AUTHPERIOD is not none -%}
            AUTHPERIOD={{item.AUTHPERIOD}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SECPLC=AUTHONLY/AUTHANDPROTECTED 时可选 --- -#}
    {%- if item.SECPLC in ['AUTHONLY', 'AUTHANDPROTECTED'] -%}
        {%- if item.AUTHEVENTTHRESHOLD is not none -%}
            AUTHEVENTTHRESHOLD={{item.AUTHEVENTTHRESHOLD}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SECPLC=AUTHONLY/AUTHANDPROTECTED 时可选 --- -#}
    {%- if item.SECPLC in ['AUTHONLY', 'AUTHANDPROTECTED'] -%}
        {%- if item.ATTSAUTH is not none -%}
            ATTSAUTH={{item.ATTSAUTH}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SECPLC=AUTHONLY/AUTHANDPROTECTED 时可选 --- -#}
    {%- if item.SECPLC in ['AUTHONLY', 'AUTHANDPROTECTED'] -%}
        {%- if item.RAUSAUTH is not none -%}
            RAUSAUTH={{item.RAUSAUTH}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SECPLC=AUTHONLY/AUTHANDPROTECTED 时可选 --- -#}
    {%- if item.SECPLC in ['AUTHONLY', 'AUTHANDPROTECTED'] -%}
        {%- if item.AUTHSETV2 is not none -%}
            AUTHSETV2={{item.AUTHSETV2}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SECPLC=AUTHONLY/AUTHANDPROTECTED 时可选 --- -#}
    {%- if item.SECPLC in ['AUTHONLY', 'AUTHANDPROTECTED'] -%}
        {%- if item.AUTHSETSNUMBER is not none -%}
            AUTHSETSNUMBER={{item.AUTHSETSNUMBER}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SECPLC=AUTHONLY/AUTHANDPROTECTED 时可选 --- -#}
    {%- if item.SECPLC in ['AUTHONLY', 'AUTHANDPROTECTED'] -%}
        {%- if item.PREGETAUTHSETS is not none -%}
            PREGETAUTHSETS={{item.PREGETAUTHSETS}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SECPLC=AUTHONLY/AUTHANDPROTECTED 时可选 --- -#}
    {%- if item.SECPLC in ['AUTHONLY', 'AUTHANDPROTECTED'] -%}
        {%- if item.GETAUTHADVTH is not none -%}
            GETAUTHADVTH={{item.GETAUTHADVTH}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SECPLC=AUTHONLY/AUTHANDPROTECTED 时可选 --- -#}
    {%- if item.SECPLC in ['AUTHONLY', 'AUTHANDPROTECTED'] -%}
        {%- if item.REAUTH is not none -%}
            REAUTH={{item.REAUTH}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SECPLC=AUTHONLY/AUTHANDPROTECTED 时可选 --- -#}
    {%- if item.SECPLC in ['AUTHONLY', 'AUTHANDPROTECTED'] -%}
        {%- if item.CAFTIMES is not none -%}
            CAFTIMES={{item.CAFTIMES}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SECPLC=AUTHANDPROTECTED 时可选 --- -#}
    {%- if item.SECPLC == 'AUTHANDPROTECTED' -%}
        {%- if item.CIPHALG is not none -%}
            CIPHALG={{item.CIPHALG}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SECPLC=AUTHANDPROTECTED 时可选 --- -#}
    {%- if item.SECPLC == 'AUTHANDPROTECTED' -%}
        {%- if item.INTALG is not none -%}
            INTALG={{item.INTALG}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in set_iudetach_list -%}
    SET IUDETACH:
    {#- --- 可选参数 --- -#}
    {%- if item.DETACHSW is not none -%}
        DETACHSW={{item.DETACHSW}},
    {%- endif -%}
    {%- if item.NACTTMR is not none -%}
        NACTTMR={{item.NACTTMR}},
    {%- endif -%}
    {%- if item.DETACHONFOR is not none -%}
        DETACHONFOR={{item.DETACHONFOR}},
    {%- endif -%}
    {%- if item.DETACHONCONN is not none -%}
        DETACHONCONN={{item.DETACHONCONN}},
    {%- endif -%}
    {%- if item.NACTTMRONCONN is not none -%}
        NACTTMRONCONN={{item.NACTTMRONCONN}},
    {%- endif -%}
    {%- if item.REATM is not none -%}
        REATM={{item.REATM}},
    {%- endif -%}
    {%- if item.ONLINETIMER is not none -%}
        ONLINETIMER={{item.ONLINETIMER}},
    {%- endif -%}
    {%- if item.ONLINEFOREVER is not none -%}
        ONLINEFOREVER={{item.ONLINEFOREVER}},
    {%- endif -%}
    {%- if item.IMPDTCHNORSP is not none -%}
        IMPDTCHNORSP={{item.IMPDTCHNORSP}},
    {%- endif -%}
    {%- if item.IMPDTCH is not none -%}
        IMPDTCH={{item.IMPDTCH}},
    {%- endif -%}
    {%- if item.IMPIUONNONACT is not none -%}
        IMPIUONNONACT={{item.IMPIUONNONACT}},
    {%- endif -%}
    {%- if item.IMPONIUREL is not none -%}
        IMPONIUREL={{item.IMPONIUREL}},
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_iupaging_list_1 -%}
    ADD IUPAGING:
    {#- --- 必选参数 --- -#}
    LAI="{{item.LAI}}",
    RAC="{{item.RAC}}",
    RNCINDEX={{item.RNCINDEX}},
    ;
{%- endfor -%}
```

```jinja2
{%- for item in set_iusm_list -%}
    SET IUSM:
    {#- --- 可选参数 --- -#}
    {%- if item.T3385 is not none -%}
        T3385={{item.T3385}},
    {%- endif -%}
    {%- if item.N3385 is not none -%}
        N3385={{item.N3385}},
    {%- endif -%}
    {%- if item.T3386 is not none -%}
        T3386={{item.T3386}},
    {%- endif -%}
    {%- if item.N3386 is not none -%}
        N3386={{item.N3386}},
    {%- endif -%}
    {%- if item.T3395 is not none -%}
        T3395={{item.T3395}},
    {%- endif -%}
    {%- if item.N3395 is not none -%}
        N3395={{item.N3395}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 3.7 配置用户面数据。

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

### 4 配置到Gr接口数据。

#### 4.1 配置动态路由OSPF。

##### 4.1.1 配置VPN实例。

```jinja2
{%- for item in add_l3vpninst_list_2 -%}
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
{%- for item in add_vpninstaf_list_2 -%}
    ADD VPNINSTAF:
    {#- --- 必选参数 --- -#}
    VRFNAME="{{item.VRFNAME}}",
    AFTYPE={{item.AFTYPE}},
    ;
{%- endfor -%}
```

##### 4.1.2 配置主接口的管理状态为up。

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

##### 4.1.3 配置以太网接口。

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

##### 4.1.4 增加接口绑定VPN。

```jinja2
{%- for item in add_ipbindvpn_list_10 -%}
    ADD IPBINDVPN:
    {#- --- 必选参数 --- -#}
    IFNAME="{{item.IFNAME}}",
    VRFNAME="{{item.VRFNAME}}",
    ;
{%- endfor -%}
```

##### 4.1.5 在以太网子接口上关联VLAN ID。

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

##### 4.1.6 配置外联口的物理IP。

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

##### 4.1.7 创建OSPF进程。

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

##### 4.1.8 增加OSPF区域。

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

##### 4.1.9 增加运行OSPF协议的接口。

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

##### 4.1.10 设置OSPF引入路由类型。

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

#### 4.2 配置BFD。

##### 4.2.1 全局激活BFD。上文已配置此处无需重复配置。

##### 4.2.2 以接口粒度配置动态BFD。

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

#### 4.3 配置业务IP。

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

#### 4.4 配置M3UA信令数据。SCTP协议参数在Iu接口已配置，此处不再重复配置。

```jinja2
{%- for item in add_m3le_list_1 -%}
    ADD M3LE:
    {#- --- 必选参数 --- -#}
    LEX={{item.LEX}},
    NI={{item.NI}},
    OPC="{{item.OPC}}",
    LET={{item.LET}},
    {#- --- 可选参数 --- -#}
    {%- if item.RC is not none -%}
        RC={{item.RC}},
    {%- endif -%}
    {%- if item.NA is not none -%}
        NA={{item.NA}},
    {%- endif -%}
    {%- if item.LEN is not none -%}
        LEN="{{item.LEN}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_m3de_list_1 -%}
    ADD M3DE:
    {#- --- 必选参数 --- -#}
    DEX={{item.DEX}},
    LEX={{item.LEX}},
    DPC="{{item.DPC}}",
    DET={{item.DET}},
    {#- --- 可选参数 --- -#}
    {%- if item.SLSSM is not none -%}
        SLSSM={{item.SLSSM}},
    {%- endif -%}
    {%- if item.ADJF is not none -%}
        ADJF={{item.ADJF}},
    {%- endif -%}
    {%- if item.RC is not none -%}
        RC={{item.RC}},
    {%- endif -%}
    {%- if item.PVER is not none -%}
        PVER={{item.PVER}},
    {%- endif -%}
    {%- if item.DEN is not none -%}
        DEN="{{item.DEN}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_m3lks_list_1 -%}
    ADD M3LKS:
    {#- --- 必选参数 --- -#}
    LSX={{item.LSX}},
    DEX={{item.DEX}},
    WM={{item.WM}},
    {#- --- 可选参数 --- -#}
    {%- if item.SLSM is not none -%}
        SLSM={{item.SLSM}},
    {%- endif -%}
    {%- if item.TM is not none -%}
        TM={{item.TM}},
    {%- endif -%}
    {%- if item.LSN is not none -%}
        LSN="{{item.LSN}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_m3rt_list_1 -%}
    ADD M3RT:
    {#- --- 必选参数 --- -#}
    RTX={{item.RTX}},
    DEX={{item.DEX}},
    LSX={{item.LSX}},
    {#- --- 可选参数 --- -#}
    {%- if item.RTN is not none -%}
        RTN="{{item.RTN}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_sctppara_list_1 -%}
    ADD SCTPPARA:
    {#- --- 必选参数 --- -#}
    SCTPPARAINDEX={{item.SCTPPARAINDEX}},
    {#- --- 可选参数 --- -#}
    {%- if item.SCTPPARANAME is not none -%}
        SCTPPARANAME="{{item.SCTPPARANAME}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_m3lnk_list_4 -%}
    ADD M3LNK:
    {#- --- 必选参数 --- -#}
    LNK={{item.LNK}},
    CS={{item.CS}},
    LSX={{item.LSX}},
    SCTPINDX={{item.SCTPINDX}},
    {#- --- 可选参数 --- -#}
    {%- if item.VPNNAME is not none -%}
        VPNNAME="{{item.VPNNAME}}",
    {%- endif -%}
    {%- if item.IPT is not none -%}
        IPT={{item.IPT}},
    {%- endif -%}
    {%- if item.LOCPORT is not none -%}
        LOCPORT={{item.LOCPORT}},
    {%- endif -%}
    {%- if item.PEERPORT is not none -%}
        PEERPORT={{item.PEERPORT}},
    {%- endif -%}
    {%- if item.LKN is not none -%}
        LKN="{{item.LKN}}",
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPT=IPV4 时必选 --- -#}
    {%- if item.IPT == 'IPV4' -%}
        LOCIPV41="{{item.LOCIPV41}}",
    {%- endif -%}
    {#- --- 条件必选：IPT=IPV4 时必选 --- -#}
    {%- if item.IPT == 'IPV4' -%}
        PEERIPV41="{{item.PEERIPV41}}",
    {%- endif -%}
    {#- --- 条件必选：IPT=IPV6 时必选 --- -#}
    {%- if item.IPT == 'IPV6' -%}
        LOCIPV61="{{item.LOCIPV61}}",
    {%- endif -%}
    {#- --- 条件必选：IPT=IPV6 时必选 --- -#}
    {%- if item.IPT == 'IPV6' -%}
        PEERIPV61="{{item.PEERIPV61}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：IPT=IPV4 时可选 --- -#}
    {%- if item.IPT == 'IPV4' -%}
        {%- if item.LOCIPV42 is not none -%}
            LOCIPV42="{{item.LOCIPV42}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：IPT=IPV4 时可选 --- -#}
    {%- if item.IPT == 'IPV4' -%}
        {%- if item.PEERIPV42 is not none -%}
            PEERIPV42="{{item.PEERIPV42}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：IPT=IPV6 时可选 --- -#}
    {%- if item.IPT == 'IPV6' -%}
        {%- if item.LOCIPV62 is not none -%}
            LOCIPV62="{{item.LOCIPV62}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：IPT=IPV6 时可选 --- -#}
    {%- if item.IPT == 'IPV6' -%}
        {%- if item.PEERIPV62 is not none -%}
            PEERIPV62="{{item.PEERIPV62}}",
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_m3le_list_2 -%}
    ADD M3LE:
    {#- --- 必选参数 --- -#}
    LEX={{item.LEX}},
    NI={{item.NI}},
    OPC="{{item.OPC}}",
    LET={{item.LET}},
    {#- --- 可选参数 --- -#}
    {%- if item.LEN is not none -%}
        LEN="{{item.LEN}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_m3de_list_2 -%}
    ADD M3DE:
    {#- --- 必选参数 --- -#}
    DEX={{item.DEX}},
    LEX={{item.LEX}},
    DPC="{{item.DPC}}",
    DET={{item.DET}},
    {#- --- 可选参数 --- -#}
    {%- if item.SLSSM is not none -%}
        SLSSM={{item.SLSSM}},
    {%- endif -%}
    {%- if item.STPF is not none -%}
        STPF={{item.STPF}},
    {%- endif -%}
    {%- if item.ADJF is not none -%}
        ADJF={{item.ADJF}},
    {%- endif -%}
    {%- if item.NMD is not none -%}
        NMD={{item.NMD}},
    {%- endif -%}
    {%- if item.RC is not none -%}
        RC={{item.RC}},
    {%- endif -%}
    {%- if item.PVER is not none -%}
        PVER={{item.PVER}},
    {%- endif -%}
    {%- if item.DEN is not none -%}
        DEN="{{item.DEN}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_m3lks_list_2 -%}
    ADD M3LKS:
    {#- --- 必选参数 --- -#}
    LSX={{item.LSX}},
    DEX={{item.DEX}},
    WM={{item.WM}},
    {#- --- 可选参数 --- -#}
    {%- if item.SLSM is not none -%}
        SLSM={{item.SLSM}},
    {%- endif -%}
    {%- if item.TM is not none -%}
        TM={{item.TM}},
    {%- endif -%}
    {%- if item.LSN is not none -%}
        LSN="{{item.LSN}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_m3rt_list_2 -%}
    ADD M3RT:
    {#- --- 必选参数 --- -#}
    RTX={{item.RTX}},
    DEX={{item.DEX}},
    LSX={{item.LSX}},
    {#- --- 可选参数 --- -#}
    {%- if item.PRI is not none -%}
        PRI={{item.PRI}},
    {%- endif -%}
    {%- if item.RTN is not none -%}
        RTN="{{item.RTN}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_m3lnk_list_5 -%}
    ADD M3LNK:
    {#- --- 必选参数 --- -#}
    LNK={{item.LNK}},
    CS={{item.CS}},
    LSX={{item.LSX}},
    SCTPINDX={{item.SCTPINDX}},
    {#- --- 可选参数 --- -#}
    {%- if item.VPNNAME is not none -%}
        VPNNAME="{{item.VPNNAME}}",
    {%- endif -%}
    {%- if item.IPT is not none -%}
        IPT={{item.IPT}},
    {%- endif -%}
    {%- if item.LOCPORT is not none -%}
        LOCPORT={{item.LOCPORT}},
    {%- endif -%}
    {%- if item.PEERPORT is not none -%}
        PEERPORT={{item.PEERPORT}},
    {%- endif -%}
    {%- if item.ASF is not none -%}
        ASF={{item.ASF}},
    {%- endif -%}
    {%- if item.PRI is not none -%}
        PRI={{item.PRI}},
    {%- endif -%}
    {%- if item.CONSTHD is not none -%}
        CONSTHD={{item.CONSTHD}},
    {%- endif -%}
    {%- if item.CONETHD is not none -%}
        CONETHD={{item.CONETHD}},
    {%- endif -%}
    {%- if item.CROSSIP is not none -%}
        CROSSIP={{item.CROSSIP}},
    {%- endif -%}
    {%- if item.EXCHGMODE is not none -%}
        EXCHGMODE={{item.EXCHGMODE}},
    {%- endif -%}
    {%- if item.LKN is not none -%}
        LKN="{{item.LKN}}",
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPT=IPV4 时必选 --- -#}
    {%- if item.IPT == 'IPV4' -%}
        LOCIPV41="{{item.LOCIPV41}}",
    {%- endif -%}
    {#- --- 条件必选：IPT=IPV4 时必选 --- -#}
    {%- if item.IPT == 'IPV4' -%}
        PEERIPV41="{{item.PEERIPV41}}",
    {%- endif -%}
    {#- --- 条件必选：IPT=IPV6 时必选 --- -#}
    {%- if item.IPT == 'IPV6' -%}
        LOCIPV61="{{item.LOCIPV61}}",
    {%- endif -%}
    {#- --- 条件必选：IPT=IPV6 时必选 --- -#}
    {%- if item.IPT == 'IPV6' -%}
        PEERIPV61="{{item.PEERIPV61}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：IPT=IPV4 时可选 --- -#}
    {%- if item.IPT == 'IPV4' -%}
        {%- if item.LOCIPV42 is not none -%}
            LOCIPV42="{{item.LOCIPV42}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：IPT=IPV4 时可选 --- -#}
    {%- if item.IPT == 'IPV4' -%}
        {%- if item.PEERIPV42 is not none -%}
            PEERIPV42="{{item.PEERIPV42}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：IPT=IPV6 时可选 --- -#}
    {%- if item.IPT == 'IPV6' -%}
        {%- if item.LOCIPV62 is not none -%}
            LOCIPV62="{{item.LOCIPV62}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：IPT=IPV6 时可选 --- -#}
    {%- if item.IPT == 'IPV6' -%}
        {%- if item.PEERIPV62 is not none -%}
            PEERIPV62="{{item.PEERIPV62}}",
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 4.5 配置SCCP信令数据。

```jinja2
{%- for item in add_sccpopc_list_1 -%}
    ADD SCCPOPC:
    {#- --- 必选参数 --- -#}
    OPX={{item.OPX}},
    NI={{item.NI}},
    OPC="{{item.OPC}}",
    {#- --- 可选参数 --- -#}
    {%- if item.SPN is not none -%}
        SPN={{item.SPN}},
    {%- endif -%}
    {%- if item.OPN is not none -%}
        OPN="{{item.OPN}}",
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：SPN=COREONLY/IUANDCORE 时必选 --- -#}
    {%- if item.SPN in ['COREONLY', 'IUANDCORE'] -%}
        SGSNN="{{item.SGSNN}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_sccpdpc_list_1 -%}
    ADD SCCPDPC:
    {#- --- 必选参数 --- -#}
    DPX={{item.DPX}},
    OPX={{item.OPX}},
    DPC="{{item.DPC}}",
    {#- --- 可选参数 --- -#}
    {%- if item.SS7T is not none -%}
        SS7T={{item.SS7T}},
    {%- endif -%}
    {%- if item.LDP is not none -%}
        LDP={{item.LDP}},
    {%- endif -%}
    {%- if item.DPN is not none -%}
        DPN="{{item.DPN}}",
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：LDP=LOADSHARE 时必选 --- -#}
    {%- if item.LDP == 'LOADSHARE' -%}
        SDPX={{item.SDPX}},
    {%- endif -%}
    {#- --- 条件必选：LDP=BACKUP 时必选 --- -#}
    {%- if item.LDP == 'BACKUP' -%}
        BDPX={{item.BDPX}},
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_sccpssn_list_2 -%}
    ADD SCCPSSN:
    {#- --- 必选参数 --- -#}
    SSNX={{item.SSNX}},
    SSN={{item.SSN}},
    NI={{item.NI}},
    DPC="{{item.DPC}}",
    OPC="{{item.OPC}}",
    {#- --- 可选参数 --- -#}
    {%- if item.SSNNAME is not none -%}
        SSNNAME="{{item.SSNNAME}}",
    {%- endif -%}
    {%- if item.LOADSHARETYPE is not none -%}
        LOADSHARETYPE={{item.LOADSHARETYPE}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：LOADSHARETYPE=BACKUP 时必选 --- -#}
    {%- if item.LOADSHARETYPE == 'BACKUP' -%}
        BACKUPINDEX={{item.BACKUPINDEX}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 4.6 配置GT翻译数据。

```jinja2
{%- for item in add_imsigt_list -%}
    ADD IMSIGT:
    {#- --- 必选参数 --- -#}
    IMSIPRE="{{item.IMSIPRE}}",
    GT="{{item.GT}}",
    {#- --- 可选参数 --- -#}
    {%- if item.MNNAME is not none -%}
        MNNAME="{{item.MNNAME}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_connectplmn_list -%}
    ADD CONNECTPLMN:
    {#- --- 必选参数 --- -#}
    MCC="{{item.MCC}}",
    MNC="{{item.MNC}}",
    {#- --- 可选参数 --- -#}
    {%- if item.CC is not none -%}
        CC="{{item.CC}}",
    {%- endif -%}
    {%- if item.NOID is not none -%}
        NOID={{item.NOID}},
    {%- endif -%}
    {%- if item.SM is not none -%}
        SM={{item.SM}},
    {%- endif -%}
    {%- if item.SMS is not none -%}
        SMS={{item.SMS}},
    {%- endif -%}
    {%- if item.LCS is not none -%}
        LCS={{item.LCS}},
    {%- endif -%}
    {%- if item.S5S8TYPE is not none -%}
        S5S8TYPE={{item.S5S8TYPE}},
    {%- endif -%}
    {%- if item.COUNTRYORAREANAME is not none -%}
        COUNTRYORAREANAME="{{item.COUNTRYORAREANAME}}",
    {%- endif -%}
    {%- if item.EXCLUSIVEPLMN is not none -%}
        EXCLUSIVEPLMN={{item.EXCLUSIVEPLMN}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：SMSCR=YES 时必选 --- -#}
    {%- if item.SMSCR == 'YES' -%}
        SMSCT="{{item.SMSCT}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：SM=YES 时可选 --- -#}
    {%- if item.SM == 'YES' -%}
        {%- if item.MAXSMNUM is not none -%}
            MAXSMNUM={{item.MAXSMNUM}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SMS=YES 时可选 --- -#}
    {%- if item.SMS == 'YES' -%}
        {%- if item.SMSCR is not none -%}
            SMSCR={{item.SMSCR}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_sccpgt_list -%}
    ADD SCCPGT:
    {#- --- 必选参数 --- -#}
    GTX={{item.GTX}},
    NI={{item.NI}},
    RT={{item.RT}},
    ADDR="{{item.ADDR}}",
    DPC="{{item.DPC}}",
    {#- --- 可选参数 --- -#}
    {%- if item.GTEXP is not none -%}
        GTEXP={{item.GTEXP}},
    {%- endif -%}
    {%- if item.NAME is not none -%}
        NAME="{{item.NAME}}",
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：RT=DPCNEWGT 时必选 --- -#}
    {%- if item.RT == 'DPCNEWGT' -%}
        NGTX={{item.NGTX}},
    {%- endif -%}
    {#- --- 条件必选：RT=DPCSSN 时必选 --- -#}
    {%- if item.RT == 'DPCSSN' -%}
        SSN={{item.SSN}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：GTEXP=FOUR 时可选 --- -#}
    {%- if item.GTEXP == 'FOUR' -%}
        {%- if item.NP is not none -%}
            NP={{item.NP}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：GTEXP=FOUR 时可选 --- -#}
    {%- if item.GTEXP == 'FOUR' -%}
        {%- if item.ADDREXP is not none -%}
            ADDREXP={{item.ADDREXP}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：GTEXP=SIX 时可选 --- -#}
    {%- if item.GTEXP == 'SIX' -%}
        {%- if item.TT is not none -%}
            TT={{item.TT}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 5 配置GnGp接口数据。

#### 5.1 配置动态路由OSPF。

##### 5.1.1 配置VPN实例。

```jinja2
{%- for item in add_l3vpninst_list_3 -%}
    ADD L3VPNINST:
    {#- --- 必选参数 --- -#}
    VRFNAME="{{item.VRFNAME}}",
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_vpninstaf_list_3 -%}
    ADD VPNINSTAF:
    {#- --- 必选参数 --- -#}
    VRFNAME="{{item.VRFNAME}}",
    AFTYPE={{item.AFTYPE}},
    ;
{%- endfor -%}
```

##### 5.1.2 配置主接口的管理状态为up。

```jinja2
{%- for item in mod_interface_list_12 -%}
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
{%- for item in add_interface_list_15 -%}
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
{%- for item in add_ipbindvpn_list_15 -%}
    ADD IPBINDVPN:
    {#- --- 必选参数 --- -#}
    IFNAME="{{item.IFNAME}}",
    VRFNAME="{{item.VRFNAME}}",
    ;
{%- endfor -%}
```

##### 5.1.5 在以太网子接口上关联VLAN ID。

```jinja2
{%- for item in add_ethsubif_list_12 -%}
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
{%- for item in add_ifipv4address_list_15 -%}
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
{%- for item in add_ospf_list_3 -%}
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
{%- for item in add_ospfarea_list_3 -%}
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
{%- for item in add_ospfnetwork_list_9 -%}
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
{%- for item in add_ospfimportroute_list_3 -%}
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
{%- for item in add_ospfinterface_list_12 -%}
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

##### 5.4.1 增加GTP-C IP。

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

##### 5.4.2 配置GTP-U IP。

```jinja2
{%- for item in add_gtpule_list_2 -%}
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

#### 5.5 配置GGSN解析数据。

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
{%- for item in add_ggsncharact_list -%}
    ADD GGSNCHARACT:
    {#- --- 必选参数 --- -#}
    RANGE={{item.RANGE}},
    {#- --- 可选参数 --- -#}
    {%- if item.QOSVER is not none -%}
        QOSVER={{item.QOSVER}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：RANGE=SPECIAL_GGSN 时必选 --- -#}
    {%- if item.RANGE == 'SPECIAL_GGSN' -%}
        IPT={{item.IPT}},
    {%- endif -%}
    {#- --- 条件必选：IPT=IPV4 时必选 --- -#}
    {%- if item.IPT == 'IPV4' -%}
        GGSNIPV4="{{item.GGSNIPV4}}",
    {%- endif -%}
    {#- --- 条件必选：IPT=IPV4 时必选 --- -#}
    {%- if item.IPT == 'IPV4' -%}
        MASKV4="{{item.MASKV4}}",
    {%- endif -%}
    {#- --- 条件必选：IPT=IPV6 时必选 --- -#}
    {%- if item.IPT == 'IPV6' -%}
        GGSNIPV6="{{item.GGSNIPV6}}",
    {%- endif -%}
    {#- --- 条件必选：IPT=IPV6 时必选 --- -#}
    {%- if item.IPT == 'IPV6' -%}
        MASKV6={{item.MASKV6}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 6 配置Ga接口数据。

#### 6.1 配置动态路由OSPF。

##### 6.1.1 配置VPN实例。

```jinja2
{%- for item in add_l3vpninst_list_4 -%}
    ADD L3VPNINST:
    {#- --- 必选参数 --- -#}
    VRFNAME="{{item.VRFNAME}}",
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_vpninstaf_list_4 -%}
    ADD VPNINSTAF:
    {#- --- 必选参数 --- -#}
    VRFNAME="{{item.VRFNAME}}",
    AFTYPE={{item.AFTYPE}},
    ;
{%- endfor -%}
```

##### 6.1.2 配置主接口的管理状态为up。

```jinja2
{%- for item in mod_interface_list_16 -%}
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

##### 6.1.3 配置以太网接口。

```jinja2
{%- for item in add_interface_list_20 -%}
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

##### 6.1.4 增加接口绑定VPN。

```jinja2
{%- for item in add_ipbindvpn_list_20 -%}
    ADD IPBINDVPN:
    {#- --- 必选参数 --- -#}
    IFNAME="{{item.IFNAME}}",
    VRFNAME="{{item.VRFNAME}}",
    ;
{%- endfor -%}
```

##### 6.1.5 在以太网子接口上关联VLAN ID。

```jinja2
{%- for item in add_ethsubif_list_16 -%}
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

##### 6.1.6 配置外联口的物理IP。

```jinja2
{%- for item in add_ifipv4address_list_20 -%}
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

##### 6.1.7 创建OSPF进程。

```jinja2
{%- for item in add_ospf_list_4 -%}
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

##### 6.1.8 增加OSPF区域。

```jinja2
{%- for item in add_ospfarea_list_4 -%}
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

##### 6.1.9 增加运行OSPF协议的接口。

```jinja2
{%- for item in add_ospfnetwork_list_12 -%}
    ADD OSPFNETWORK:
    {#- --- 必选参数 --- -#}
    PROCID={{item.PROCID}},
    AREAID="{{item.AREAID}}",
    IPADDRESS="{{item.IPADDRESS}}",
    WILDCARDMASK="{{item.WILDCARDMASK}}",
    ;
{%- endfor -%}
```

##### 6.1.10 设置OSPF引入路由类型。

```jinja2
{%- for item in add_ospfimportroute_list_4 -%}
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

#### 6.2 配置BFD。

##### 6.2.1 全局激活BFD。

```jinja2
{%- for item in set_bfd_list_1 -%}
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

##### 6.2.2 以接口粒度配置动态BFD。

```jinja2
{%- for item in add_ospfinterface_list_16 -%}
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

#### 6.3 配置业务IP。

```jinja2
{%- for item in add_serviceip_list_9 -%}
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

#### 6.4 配置CG数据。

```jinja2
{%- for item in add_chgcdpip_list -%}
    ADD CHGCDPIP:
    {#- --- 必选参数 --- -#}
    IPT={{item.IPT}},
    {#- --- 可选参数 --- -#}
    {%- if item.PORTBGN is not none -%}
        PORTBGN={{item.PORTBGN}},
    {%- endif -%}
    {%- if item.PORTEND is not none -%}
        PORTEND={{item.PORTEND}},
    {%- endif -%}
    {%- if item.VPNNAME is not none -%}
        VPNNAME="{{item.VPNNAME}}",
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPT=IPv4 时必选 --- -#}
    {%- if item.IPT == 'IPv4' -%}
        IPV4ADDR="{{item.IPV4ADDR}}",
    {%- endif -%}
    {#- --- 条件必选：IPT=IPv6 时必选 --- -#}
    {%- if item.IPT == 'IPv6' -%}
        IPV6ADDR="{{item.IPV6ADDR}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_chgcg_list -%}
    ADD CHGCG:
    {#- --- 必选参数 --- -#}
    PRO={{item.PRO}},
    CGR={{item.CGR}},
    {#- --- 可选参数 --- -#}
    {%- if item.SPN is not none -%}
        SPN={{item.SPN}},
    {%- endif -%}
    {%- if item.DEFAULTCG is not none -%}
        DEFAULTCG={{item.DEFAULTCG}},
    {%- endif -%}
    {%- if item.CGN is not none -%}
        CGN="{{item.CGN}}",
    {%- endif -%}
    {%- if item.IPT is not none -%}
        IPT={{item.IPT}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPT=IPV4 时必选 --- -#}
    {%- if item.IPT == 'IPV4' -%}
        IP="{{item.IP}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：DEFAULTCG=YES 时可选 --- -#}
    {%- if item.DEFAULTCG == 'YES' -%}
        {%- if item.GRD is not none -%}
            GRD={{item.GRD}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in set_chgga_list -%}
    SET CHGGA:
    {#- --- 可选参数 --- -#}
    {%- if item.GCR is not none -%}
        GCR={{item.GCR}},
    {%- endif -%}
    {%- if item.UCR is not none -%}
        UCR={{item.UCR}},
    {%- endif -%}
    {%- if item.CHGVER98 is not none -%}
        CHGVER98={{item.CHGVER98}},
    {%- endif -%}
    {%- if item.CHGVER99 is not none -%}
        CHGVER99={{item.CHGVER99}},
    {%- endif -%}
    {%- if item.CHGVER4 is not none -%}
        CHGVER4={{item.CHGVER4}},
    {%- endif -%}
    {%- if item.CHGVER5 is not none -%}
        CHGVER5={{item.CHGVER5}},
    {%- endif -%}
    {%- if item.CHGVER6 is not none -%}
        CHGVER6={{item.CHGVER6}},
    {%- endif -%}
    {%- if item.CHGVER7 is not none -%}
        CHGVER7={{item.CHGVER7}},
    {%- endif -%}
    {%- if item.CHGVER9 is not none -%}
        CHGVER9={{item.CHGVER9}},
    {%- endif -%}
    {%- if item.ITVRES is not none -%}
        ITVRES={{item.ITVRES}},
    {%- endif -%}
    {%- if item.RSNUM is not none -%}
        RSNUM={{item.RSNUM}},
    {%- endif -%}
    {%- if item.HDDETH is not none -%}
        HDDETH={{item.HDDETH}},
    {%- endif -%}
    {%- if item.HDDFSL is not none -%}
        HDDFSL={{item.HDDFSL}},
    {%- endif -%}
    {%- if item.REDICTFRMMAXOCCRATE is not none -%}
        REDICTFRMMAXOCCRATE={{item.REDICTFRMMAXOCCRATE}},
    {%- endif -%}
    {%- if item.QOSVER is not none -%}
        QOSVER={{item.QOSVER}},
    {%- endif -%}
    {%- if item.GASENDUDPCHECK is not none -%}
        GASENDUDPCHECK={{item.GASENDUDPCHECK}},
    {%- endif -%}
    {%- if item.GAREVUDPCHECK is not none -%}
        GAREVUDPCHECK={{item.GAREVUDPCHECK}},
    {%- endif -%}
    {%- if item.CDROVERWRITE is not none -%}
        CDROVERWRITE={{item.CDROVERWRITE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_chgbeha_list -%}
    ADD CHGBEHA:
    {#- --- 必选参数 --- -#}
    CB={{item.CB}},
    BA={{item.BA}},
    ACC={{item.ACC}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：BA=PLT/PST 时必选 --- -#}
    {%- if item.BA in ['PLT', 'PST'] -%}
        PURGELEN={{item.PURGELEN}},
    {%- endif -%}
    {#- --- 条件必选：BA=SMSC/SMSCMT/SMSCMOMT 时必选 --- -#}
    {%- if item.BA in ['SMSC', 'SMSCMT', 'SMSCMOMT'] -%}
        SMSCADDR="{{item.SMSCADDR}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：BA=CGIP 时可选 --- -#}
    {%- if item.BA == 'CGIP' -%}
        {%- if item.IPT is not none -%}
            IPT={{item.IPT}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in set_chgchar_list -%}
    SET CHGCHAR:
    {#- --- 必选参数 --- -#}
    CC={{item.CC}},
    {#- --- 可选参数 --- -#}
    {%- if item.MP is not none -%}
        MP={{item.MP}},
    {%- endif -%}
    {%- if item.MPCP is not none -%}
        MPCP={{item.MPCP}},
    {%- endif -%}
    {%- if item.MPL is not none -%}
        MPL={{item.MPL}},
    {%- endif -%}
    {%- if item.MLCP is not none -%}
        MLCP={{item.MLCP}},
    {%- endif -%}
    {%- if item.MLCL is not none -%}
        MLCL={{item.MLCL}},
    {%- endif -%}
    {%- if item.RPCMCDR is not none -%}
        RPCMCDR={{item.RPCMCDR}},
    {%- endif -%}
    {%- if item.SP is not none -%}
        SP={{item.SP}},
    {%- endif -%}
    {%- if item.SPP is not none -%}
        SPP={{item.SPP}},
    {%- endif -%}
    {%- if item.SPL is not none -%}
        SPL={{item.SPL}},
    {%- endif -%}
    {%- if item.SVP is not none -%}
        SVP={{item.SVP}},
    {%- endif -%}
    {%- if item.SVL is not none -%}
        SVL={{item.SVL}},
    {%- endif -%}
    {%- if item.SCCP is not none -%}
        SCCP={{item.SCCP}},
    {%- endif -%}
    {%- if item.SCCL is not none -%}
        SCCL={{item.SCCL}},
    {%- endif -%}
    {%- if item.SLCP is not none -%}
        SLCP={{item.SLCP}},
    {%- endif -%}
    {%- if item.PCC is not none -%}
        PCC={{item.PCC}},
    {%- endif -%}
    {%- if item.RPCSCDR is not none -%}
        RPCSCDR={{item.RPCSCDR}},
    {%- endif -%}
    {%- if item.SMOP is not none -%}
        SMOP={{item.SMOP}},
    {%- endif -%}
    {%- if item.SMTP is not none -%}
        SMTP={{item.SMTP}},
    {%- endif -%}
    {%- if item.LCSMOP is not none -%}
        LCSMOP={{item.LCSMOP}},
    {%- endif -%}
    {%- if item.LCSMTP is not none -%}
        LCSMTP={{item.LCSMTP}},
    {%- endif -%}
    {%- if item.LCSNIP is not none -%}
        LCSNIP={{item.LCSNIP}},
    {%- endif -%}
    {%- if item.SR is not none -%}
        SR={{item.SR}},
    {%- endif -%}
    {%- if item.CGIP is not none -%}
        CGIP="{{item.CGIP}}",
    {%- endif -%}
    {%- if item.TARIACCFLG is not none -%}
        TARIACCFLG={{item.TARIACCFLG}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 6.5 配置费率数据。

```jinja2
{%- for item in set_chgwkdy_list -%}
    SET CHGWKDY:
    {#- --- 必选参数 --- -#}
    WKDAY={{item.WKDAY}},
    CC={{item.CC}},
    TT={{item.TT}},
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_chgtari_list -%}
    ADD CHGTARI:
    {#- --- 必选参数 --- -#}
    TT={{item.TT}},
    ST={{item.ST}},
    ET={{item.ET}},
    CC={{item.CC}},
    ;
{%- endfor -%}
```

### 7 配置到DNS的数据。

#### 7.1 确保SGSN上的Gn接口路由配置已经完成。

#### SGSN侧通过Gn接口路由与DNS互通，因此只需确保SGSN上的Gn接口路由配置完成，那么SGSN到DNS的路由配置也就完成了。

#### 7.2 配置本局信令网属性。

```jinja2
{%- for item in set_sigattr_list_1 -%}
    SET SIGATTR:
    {#- --- 可选参数 --- -#}
    {%- if item.IF is not none -%}
        IF={{item.IF}},
    {%- endif -%}
    {%- if item.IRF is not none -%}
        IRF={{item.IRF}},
    {%- endif -%}
    {%- if item.NF is not none -%}
        NF={{item.NF}},
    {%- endif -%}
    {%- if item.NRF is not none -%}
        NRF={{item.NRF}},
    {%- endif -%}
    {%- if item.M3UASTPF is not none -%}
        M3UASTPF={{item.M3UASTPF}},
    {%- endif -%}
    {%- if item.BSSAPPF is not none -%}
        BSSAPPF={{item.BSSAPPF}},
    {%- endif -%}
    {%- if item.BSSAPPNO is not none -%}
        BSSAPPNO={{item.BSSAPPNO}},
    {%- endif -%}
    {%- if item.BSSAPPNI is not none -%}
        BSSAPPNI={{item.BSSAPPNI}},
    {%- endif -%}
    {%- if item.MAPNI is not none -%}
        MAPNI={{item.MAPNI}},
    {%- endif -%}
    {%- if item.SS7T is not none -%}
        SS7T={{item.SS7T}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 7.3 配置业务IP。

```jinja2
{%- for item in add_serviceip_list_10 -%}
    ADD SERVICEIP:
    {#- --- 必选参数 --- -#}
    IPVERSION={{item.IPVERSION}},
    {#- --- 可选参数 --- -#}
    {%- if item.VPNINSTNAME is not none -%}
        VPNINSTNAME="{{item.VPNINSTNAME}}",
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

#### 7.4 设置DNS参数。

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

```jinja2
{%- for item in set_dns_list -%}
    SET DNS:
    {#- --- 可选参数 --- -#}
    {%- if item.TMS is not none -%}
        TMS={{item.TMS}},
    {%- endif -%}
    {%- if item.TRT is not none -%}
        TRT={{item.TRT}},
    {%- endif -%}
    {%- if item.DDS is not none -%}
        DDS={{item.DDS}},
    {%- endif -%}
    {%- if item.DDI is not none -%}
        DDI={{item.DDI}},
    {%- endif -%}
    {%- if item.SFT is not none -%}
        SFT={{item.SFT}},
    {%- endif -%}
    {%- if item.DDN is not none -%}
        DDN="{{item.DDN}}",
    {%- endif -%}
    {%- if item.DISCACHEPURGESW is not none -%}
        DISCACHEPURGESW={{item.DISCACHEPURGESW}},
    {%- endif -%}
    {%- if item.IPSORTMODE is not none -%}
        IPSORTMODE={{item.IPSORTMODE}},
    {%- endif -%}
    {%- if item.CNAMESW is not none -%}
        CNAMESW={{item.CNAMESW}},
    {%- endif -%}
    {%- if item.RCRSPTM is not none -%}
        RCRSPTM={{item.RCRSPTM}},
    {%- endif -%}
    {%- if item.RCQRYTM is not none -%}
        RCQRYTM={{item.RCQRYTM}},
    {%- endif -%}
    {%- if item.FAILTM is not none -%}
        FAILTM={{item.FAILTM}},
    {%- endif -%}
    {%- if item.PAUSETM is not none -%}
        PAUSETM={{item.PAUSETM}},
    {%- endif -%}
    {%- if item.RCUPDTM is not none -%}
        RCUPDTM={{item.RCUPDTM}},
    {%- endif -%}
    {%- if item.RCUSEDTM is not none -%}
        RCUSEDTM={{item.RCUSEDTM}},
    {%- endif -%}
    {%- if item.LOCALTTL is not none -%}
        LOCALTTL={{item.LOCALTTL}},
    {%- endif -%}
    {%- if item.REROUTECAUSE is not none -%}
        REROUTECAUSE={{item.REROUTECAUSE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 8 配置业务特性数据。

#### 8.1 配置移动性管理参数。

```jinja2
{%- for item in add_iuauthciph_list_1 -%}
    ADD IUAUTHCIPH:
    {#- --- 必选参数 --- -#}
    IMSIPRE="{{item.IMSIPRE}}",
    {#- --- 可选参数 --- -#}
    {%- if item.SECPLC is not none -%}
        SECPLC={{item.SECPLC}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：SECPLC=AUTHONLY/AUTHANDPROTECTED 时可选 --- -#}
    {%- if item.SECPLC in ['AUTHONLY', 'AUTHANDPROTECTED'] -%}
        {%- if item.AUTHEVENT is not none -%}
            AUTHEVENT={{item.AUTHEVENT}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SECPLC=AUTHONLY/AUTHANDPROTECTED 时可选 --- -#}
    {%- if item.SECPLC in ['AUTHONLY', 'AUTHANDPROTECTED'] -%}
        {%- if item.AUTHEVENTTHRESHOLD is not none -%}
            AUTHEVENTTHRESHOLD={{item.AUTHEVENTTHRESHOLD}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SECPLC=AUTHONLY/AUTHANDPROTECTED 时可选 --- -#}
    {%- if item.SECPLC in ['AUTHONLY', 'AUTHANDPROTECTED'] -%}
        {%- if item.ATTSAUTH is not none -%}
            ATTSAUTH={{item.ATTSAUTH}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SECPLC=AUTHONLY/AUTHANDPROTECTED 时可选 --- -#}
    {%- if item.SECPLC in ['AUTHONLY', 'AUTHANDPROTECTED'] -%}
        {%- if item.RAUSAUTH is not none -%}
            RAUSAUTH={{item.RAUSAUTH}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SECPLC=AUTHONLY/AUTHANDPROTECTED 时可选 --- -#}
    {%- if item.SECPLC in ['AUTHONLY', 'AUTHANDPROTECTED'] -%}
        {%- if item.AUTHSETV2 is not none -%}
            AUTHSETV2={{item.AUTHSETV2}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SECPLC=AUTHONLY/AUTHANDPROTECTED 时可选 --- -#}
    {%- if item.SECPLC in ['AUTHONLY', 'AUTHANDPROTECTED'] -%}
        {%- if item.REAUTH is not none -%}
            REAUTH={{item.REAUTH}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SECPLC=AUTHANDPROTECTED 时可选 --- -#}
    {%- if item.SECPLC == 'AUTHANDPROTECTED' -%}
        {%- if item.CIPHALG is not none -%}
            CIPHALG={{item.CIPHALG}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SECPLC=AUTHANDPROTECTED 时可选 --- -#}
    {%- if item.SECPLC == 'AUTHANDPROTECTED' -%}
        {%- if item.INTALG is not none -%}
            INTALG={{item.INTALG}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SECPLC=AUTHONLY/AUTHANDPROTECTED 时可选 --- -#}
    {%- if item.SECPLC in ['AUTHONLY', 'AUTHANDPROTECTED'] -%}
        {%- if item.AUTHPERIOD is not none -%}
            AUTHPERIOD={{item.AUTHPERIOD}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SECPLC=AUTHONLY/AUTHANDPROTECTED 时可选 --- -#}
    {%- if item.SECPLC in ['AUTHONLY', 'AUTHANDPROTECTED'] -%}
        {%- if item.AUTHSETSNUMBER is not none -%}
            AUTHSETSNUMBER={{item.AUTHSETSNUMBER}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SECPLC=AUTHONLY/AUTHANDPROTECTED 时可选 --- -#}
    {%- if item.SECPLC in ['AUTHONLY', 'AUTHANDPROTECTED'] -%}
        {%- if item.CAFTIMES is not none -%}
            CAFTIMES={{item.CAFTIMES}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SECPLC=AUTHONLY/AUTHANDPROTECTED 时可选 --- -#}
    {%- if item.SECPLC in ['AUTHONLY', 'AUTHANDPROTECTED'] -%}
        {%- if item.GETAUTHADVTH is not none -%}
            GETAUTHADVTH={{item.GETAUTHADVTH}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SECPLC=AUTHONLY/AUTHANDPROTECTED 时可选 --- -#}
    {%- if item.SECPLC in ['AUTHONLY', 'AUTHANDPROTECTED'] -%}
        {%- if item.PREGETAUTHSETS is not none -%}
            PREGETAUTHSETS={{item.PREGETAUTHSETS}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_algpriority_list -%}
    ADD ALGPRIORITY:
    {#- --- 必选参数 --- -#}
    ALGTYPE={{item.ALGTYPE}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：ALGTYPE=CIPH 时必选 --- -#}
    {%- if item.ALGTYPE == 'CIPH' -%}
        ALGCIPH={{item.ALGCIPH}},
    {%- endif -%}
    {#- --- 条件必选：ALGTYPE=CIPH/INTE 时必选 --- -#}
    {%- if item.ALGTYPE in ['CIPH', 'INTE'] -%}
        ALGPRI={{item.ALGPRI}},
    {%- endif -%}
    {#- --- 条件必选：ALGTYPE=INTE 时必选 --- -#}
    {%- if item.ALGTYPE == 'INTE' -%}
        ALGINTE={{item.ALGINTE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 8.2 配置会话管理参数。

```jinja2
{%- for item in add_arppara_list -%}
    ADD ARPPARA:
    {#- --- 必选参数 --- -#}
    GROUPID={{item.GROUPID}},
    USRPRI={{item.USRPRI}},
    SRVLVL={{item.SRVLVL}},
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：GROUPID=G0/G1/G2/G3/G4/G5/G6/G7/G8/G9 时可选 --- -#}
    {%- if item.GROUPID in ['G0', 'G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'G9'] -%}
        {%- if item.DESCRIPTION is not none -%}
            DESCRIPTION="{{item.DESCRIPTION}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件必选/可选参数 --- -#}
    {#- --- 承载优先级: 条件必选(ARP策略组=G1|G2|G3|G4|G5|G6|G7|G8|G9) / 条件可选(ARP策略组=G0) --- -#}
    {%- if (item.GROUPID in ['G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'G9']) -%}
        PRTLVL={{item.PRTLVL}},
    {%- elif (item.GROUPID == 'G0') -%}
        {%- if item.PRTLVL is not none -%}
            PRTLVL={{item.PRTLVL}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 抢占性: 条件必选(ARP策略组=G1|G2|G3|G4|G5|G6|G7|G8|G9) / 条件可选(ARP策略组=G0) --- -#}
    {%- if (item.GROUPID in ['G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'G9']) -%}
        PRELVL={{item.PRELVL}},
    {%- elif (item.GROUPID == 'G0') -%}
        {%- if item.PRELVL is not none -%}
            PRELVL={{item.PRELVL}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 被抢占性: 条件必选(ARP策略组=G1|G2|G3|G4|G5|G6|G7|G8|G9) / 条件可选(ARP策略组=G0) --- -#}
    {%- if (item.GROUPID in ['G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'G9']) -%}
        PREVUL={{item.PREVUL}},
    {%- elif (item.GROUPID == 'G0') -%}
        {%- if item.PREVUL is not none -%}
            PREVUL={{item.PREVUL}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 排队属性: 条件必选(ARP策略组=G1|G2|G3|G4|G5|G6|G7|G8|G9) / 条件可选(ARP策略组=G0) --- -#}
    {%- if (item.GROUPID in ['G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'G9']) -%}
        QUEUE={{item.QUEUE}},
    {%- elif (item.GROUPID == 'G0') -%}
        {%- if item.QUEUE is not none -%}
            QUEUE={{item.QUEUE}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```


---
id: ''
name: NRF典型配置实例
ne_type: UNC
type: feature
description: 本任务实例实现以下场景配置：  UNC（作为NRF）与周边NF（本例中包含AMF、SMF、NSSF）通过OSPF动态路由绑定动态BFD实现网络互通。  * 网络形态：5G网络 * 网元形态：NRF * 路由协议：OSPF动态路由 * 组网IP格式：IPv4组网 * 接入用户：IPv4单栈用户
risk_level: ''
doc_source: ["网络部署","初始配置","UNC初始配置与调测","典型配置实例","NRF典型配置实例"]
refs: []
metadata:
  DepOnLiveCfg: true
allowed-tools:
- getParameterValue('LST AUTOCONFIG')
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本任务实例实现以下场景配置：UNC（作为NRF）与周边NF（本例中包含AMF、SMF、NSSF）通过OSPF动态路由绑定动态BFD实现网络互通。* 网络形态：5G网络* 网元形态：NRF* 路由协议：OSPF动态路由* 组网IP格式：IPv4组网* 接入用户：IPv4单栈用户

## 必备事项
前提条件

* 请了解UNC各类接口的类型及命名规范，可参见业务组网与逻辑接口介绍。
* 基础数据配置、IP路由组网和业务接口配置子任务在前述章节已有详细描述，可参见基础数据配置、配置VNF侧IP路由数据（非SDN）、配置NRF，本文针对典型的任务场景举例说明整网脚本配置。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
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
        OSPFPROCID:
          name: 'OSPF进程ID'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: false
          description: ''
          data_source: ''
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
    add_ngmno_list:
      type: items
      properties:
        NOID:
          name: '运营商标识'
          type: integer
          minimum: 0
          maximum: 0
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        FULLNAME:
          name: '运营商全称'
          type: string
          minLength: 0
          maxLength: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SHORTNAME:
          name: '运营商简称'
          type: string
          minLength: 0
          maxLength: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_nghplmn_list:
      type: items
      properties:
        NOID:
          name: '运营商标识'
          type: integer
          minimum: 0
          maximum: 0
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MCC:
          name: '移动国家码'
          type: string
          minLength: 3
          maxLength: 3
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MNC:
          name: '移动网号'
          type: string
          minLength: 2
          maxLength: 3
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_licenseswitch_list:
      type: items
      properties:
        LICITEM:
          name: 'License项'
          type: string
          minLength: 0
          maxLength: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SWITCH:
          name: '开关'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_nfuuid_list:
      type: items
      properties:
        NFTYPE:
          name: 'NF类型'
          type: string
          enum:
          - NfInvalid
          - NfNRF
          - NfUDM
          - NfAMF
          - NfSMF
          - NfAUSF
          - NfNEF
          - NfPCF
          - NfSMSF
          - NfNSSF
          - NfUDR
          - NfLMF
          - NfGMLC
          - Nf5G_EIR
          - NfSEPP
          - NfUPF
          - NfN3IWF
          - NfAF
          - NfUDSF
          - NfBSF
          - NfCHF
          - NfNWDAF
          - NfTypeMAX
          - NfMBSMF
          - NfCBCF
          - NfSCF
          - NfSPF
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NFINSTANCENAME:
          name: 'NF实例名称'
          type: string
          minLength: 0
          maxLength: 64
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_logicip_list:
      type: items
      properties:
        IPVERSION:
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
        LOGICIPV4:
          name: 'IPv4地址'
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
          minLength: 1
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DESC:
          name: '描述'
          type: string
          minLength: 0
          maxLength: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV4MTU:
          name: 'IPv4 MTU'
          type: integer
          minimum: 328
          maximum: 9600
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 1500
        IPV6MTU:
          name: 'IPv6 MTU值'
          type: integer
          minimum: 1280
          maximum: 9600
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 1500
        LOGICIPV6:
          name: 'IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_httplegrp_list:
      type: items
      properties:
        INDEX:
          name: '索引'
          type: integer
          minimum: 1
          maximum: 64
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DESC:
          name: '描述'
          type: string
          minLength: 0
          maxLength: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_httple_list:
      type: items
      properties:
        INDEX:
          name: 'HTTPLE本端实体索引'
          type: integer
          minimum: 1
          maximum: 128
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        HTTPLEGRPIDX:
          name: 'HTTP本端实体组标识'
          type: integer
          minimum: 1
          maximum: 64
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LETYPE:
          name: '本端实体类型'
          type: string
          enum:
          - SERVER
          - CLIENT
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPTYPE:
          name: 'IP类型'
          type: string
          enum:
          - IPv4
          - IPv6
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
        PORT:
          name: '端口号'
          type: integer
          minimum: 1
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VPNNAME:
          name: 'VPN名称'
          type: string
          minLength: 0
          maxLength: 31
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
        TLSFLG:
          name: '是否启用TLS'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: YES
        TLSIDX:
          name: 'TLS索引'
          type: integer
          minimum: 1
          maximum: 128
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_sbiaple_list:
      type: items
      properties:
        INDEX:
          name: '索引'
          type: integer
          minimum: 1
          maximum: 128
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        HTTPLEGRPIDX:
          name: 'HTTP本端实体组标识'
          type: integer
          minimum: 1
          maximum: 64
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NFTYPE:
          name: '本端NF类型'
          type: string
          enum:
          - INVALID
          - NFTypeNRF
          - NFTypeUDM
          - NFTypeAMF
          - NFTypeSMF
          - NFTypeAUSF
          - NFTypeNEF
          - NFTypePCF
          - NFTypeSMSF
          - NFTypeNSSF
          - NFTypeUDR
          - NFTypeLMF
          - NFTypeGMLC
          - NFType5GEIR
          - NFTypeSEPP
          - NFTypeUPF
          - NFTypeN3IWF
          - NFTypeAF
          - NFTypeUDSF
          - NFTypeBSF
          - NFTypeCHF
          - NFTypeCUSTOM_OCS
          - NFTypeSCP
          - NFTypeMBSMF
          - NFTypeNWDAF
          - NFTypeUDN
          - NFTypeSFC
          - NFTypeUCBC
          - NFTypeCBE
          - NFTypeNEFEx
          - NFTypeSCF
          - NFTypeKMC
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DESCRIPTION:
          name: '描述'
          type: string
          minLength: 0
          maxLength: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CHFPEERNFTYPE:
          name: 'CHF的目的NF类型'
          type: string
          enum:
          - Nnrf
          - Nocs
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PEERNFTYPE:
          name: '目的NF类型'
          type: string
          enum:
          - Nchf
          - Nupf
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_licenseswitch_list_2:
      type: items
      properties:
        LICITEM:
          name: 'License项'
          type: string
          minLength: 0
          maxLength: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SWITCH:
          name: '开关'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_tokenexp_list:
      type: items
      properties:
        SCFGTYPE:
          name: '生效范围'
          type: string
          enum:
          - BYNFTYPE
          - BYFQDN
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NFTYPE:
          name: 'NF类型'
          type: string
          enum:
          - NRF
          - UDM
          - AMF
          - SMF
          - AUSF
          - NEF
          - PCF
          - SMSF
          - NSSF
          - UDR
          - LMF
          - GMLC
          - EIR_5G
          - SEPP
          - UPF
          - N3IWF
          - AF
          - UDSF
          - BSF
          - CHF
          - NWDAF
          - CUSTOM_OCS
          - SCP
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        EXPTIME:
          name: '有效期时长(分钟)'
          type: integer
          minimum: 1
          maximum: 65535
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        FQDN:
          name: 'FQDN'
          type: string
          minLength: 0
          maxLength: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_nrftimer_list:
      type: items
      properties:
        NFTYPE:
          name: 'NF类型'
          type: string
          enum:
          - DEFAULT
          - NRF
          - UDM
          - AMF
          - SMF
          - AUSF
          - NEF
          - PCF
          - SMSF
          - NSSF
          - UDR
          - LMF
          - GMLC
          - EIR_5G
          - SEPP
          - UPF
          - N3IWF
          - AF
          - UDSF
          - BSF
          - CHF
          - NWDAF
          - CUSTOM_OCS
          - SCP
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        HBTIMES:
          name: '心跳超时次数'
          type: integer
          minimum: 2
          maximum: 10
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        HEARTBEATTIMER:
          name: '心跳周期时长(秒)'
          type: integer
          minimum: 1
          maximum: 86400
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DISCVALIDTIMER:
          name: '服务发现缓存有效时长(秒)'
          type: integer
          minimum: 0
          maximum: 172800
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SUBVALIDTIMER:
          name: '订阅有效时长(秒)'
          type: integer
          minimum: 1
          maximum: 604800
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    set_autoconfig_list:
    - SWITCHFLAG: FALSE
    set_bfd_list:
    - BFDENABLE: TRUE
    add_l3vpninst_list:
    - VRFNAME: 'VRF_SBI'
    add_vpninstaf_list:
    - VRFNAME: 'VRF_SBI'
      AFTYPE: ipv4uni
    add_ospf_list:
    - PROCID: 6
      VRFNAME: 'VRF_SBI'
      SCHEMAROUID: '192.168.35.210'
      BFDALLINTFFLG: TRUE
      LSAARRINTVFLAG: FALSE
      LSAARRMAXINTV: 1000
      LSAARRSTARINTV: 500
      LSAARRHLDINTV: 500
      VPNINSCAPSIMFLG: TRUE
      VIRTUALSYSFLAG: TRUE
      LSAARRINTV: ''
    add_ospfarea_list:
    - PROCID: 6
      AREAID: '10.0.0.5'
    add_ospfimportroute_list:
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
    add_autoscalingservice_list:
    - SERVICENAME: 'VRF_SBI_100'
      VPNNAME: 'VRF_SBI'
      AFTYPE: IPv4
      IPALLOCTYPE4: USER_CONFIG
      VNICID: 4
      VLANID: 100
      BEGINADDR4: '192.168.79.2'
      ENDADDR4: '192.168.89.14'
      MASKLEN: 28
      OSPFENABLE: TRUE
      OSPFPROCID: 6
      OSPFAREAID: '10.0.0.5'
      TPINENABLE: FALSE
      TPOUTENABLE: FALSE
      IPALLOCTYPE6: USER_CONFIG
      AUTOCFGIFTYPE: VNIC
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
    add_ngmno_list:
    - NOID: 0
      FULLNAME: 'Operator A'
      SHORTNAME: 'OA'
    add_nghplmn_list:
    - NOID: 0
      MCC: '123'
      MNC: '03'
    set_licenseswitch_list:
    - LICITEM: 'LKV2NFBNR01'
      SWITCH: ENABLE
    add_nfuuid_list:
    - NFTYPE: NfNRF
      NFINSTANCENAME: 'NRF_INSTANCE_0'
    add_logicip_list:
    - IPVERSION: IPv4
      LOGICIPV4: '172.16.0.7'
      VPNINSTNAME: 'VRF_SBI'
      DESC: 'FOR SBI Server'
      IPV4MTU: 1500
      IPV6MTU: 1500
      LOGICIPV6: ''
    add_httplegrp_list:
    - INDEX: 3
      DESC: 'NRF'
    add_httple_list:
    - INDEX: 5
      HTTPLEGRPIDX: 3
      LETYPE: SERVER
      IPTYPE: IPv4
      IPV4: '172.16.0.7'
      PORT: 8080
      VPNNAME: 'VRF_SBI"", TLSFLG=NO, DESC="NRF Server'
      IPV6: ''
      TLSFLG: YES
      TLSIDX: ''
    add_sbiaple_list:
    - INDEX: 3
      HTTPLEGRPIDX: 3
      NFTYPE: NFTypeNRF
      DESCRIPTION: 'NRF'
      CHFPEERNFTYPE: ''
      PEERNFTYPE: ''
    set_licenseswitch_list_2:
    - LICITEM: 'LKV2NFANR01'
      SWITCH: ENABLE
    add_tokenexp_list:
    - SCFGTYPE: BYNFTYPE
      NFTYPE: AMF
      EXPTIME: 180
      FQDN: ''
    set_nrftimer_list:
    - NFTYPE: AMF
      HBTIMES: 3
      HEARTBEATTIMER: 10
      DISCVALIDTIMER: 86400
      SUBVALIDTIMER: 86400
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 进入“MML命令行-UNC”窗口。

### 2 关闭IP路由自动配置开关。

#### 2.1 查询自动配置开关状态。

#### 如果自动配置开关值为“TRUE”，需要执行如下步骤关闭自动配置开关。

#### 2.2 查询自动部署维护助手“autoscaling\_autoconfig.py”的状态，确保状态为“准备好状态（Ready）”或者查询无该脚本，以保证当前设备不在自动部署过程中。因为若系统当前有正在进行的自动部署，而自动部署生效有时延，此时若关闭自动配置开关，会影响系统配置效果。

#### 2.3 关闭自动配置开关。

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

### 3 全局激活BFD。

```jinja2
{%- for item in set_bfd_list -%}
    SET BFD:
    {#- --- 必选参数 --- -#}
    BFDENABLE={{item.BFDENABLE}},
    ;
{%- endfor -%}
```

### 4 配置UNC与对端AMF、SMF、NSSF的IP路由数据。

#### 4.1 配置外联口的VPN实例。

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

#### 4.2 配置OSPF路由。

##### 4.2.1 创建OSPF进程。

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
    {#- --- 条件必选：LSAARRINTVFLAG=TRUE 时必选 --- -#}
    {%- if item.LSAARRINTVFLAG == 'TRUE' -%}
        LSAARRINTV={{item.LSAARRINTV}},
    {%- endif -%}
    ;
{%- endfor -%}
```

##### 4.2.2 增加OSPF区域。

```jinja2
{%- for item in add_ospfarea_list -%}
    ADD OSPFAREA:
    {#- --- 必选参数 --- -#}
    PROCID={{item.PROCID}},
    AREAID="{{item.AREAID}}",
    ;
{%- endfor -%}
```

##### 如果参数“AREATYPE（区域类型）”配置为“NSSA”时，需要配置Loopback地址，这样设备会自动选取该Loopback地址作为FA。当有其他设备存在多条开销值相同的路径到NSSA设备时，可以形成负载分担。

##### 4.2.3 设置OSPF引入路由类型。

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

#### 4.3 配置外联口自动部署模板。

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
    {%- if item.AUTOCFGIFTYPE is not none -%}
        AUTOCFGIFTYPE={{item.AUTOCFGIFTYPE}},
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
```

### 5 打开IP路由自动配置开关。

```jinja2
{%- for item in set_autoconfig_list_1 -%}
    SET AUTOCONFIG:
    {#- --- 必选参数 --- -#}
    SWITCHFLAG={{item.SWITCHFLAG}},
    ;
{%- endfor -%}
```

### 从自动部署开关打开到自动部署功能生效有时延，因此执行其他操作前（例如手动部署路由互通、关闭自动部署开关），务必先执行****DSP OPSASSISTSTATE****命令查询自动部署维护助手“autoscaling\_autoconfig.py”的状态为“准备好状态（Ready）”，否则结果不可预期。

### 6 配置NRF基础数据。

#### 6.1 配置运营商信息、运营商签约用户的Home PLMN。当前UNC中默认配置一条“NOID”为0的默认记录，不需单独配置。

```jinja2
{%- for item in add_ngmno_list -%}
    ADD NGMNO:
    {#- --- 必选参数 --- -#}
    NOID={{item.NOID}},
    {#- --- 可选参数 --- -#}
    {%- if item.FULLNAME is not none -%}
        FULLNAME="{{item.FULLNAME}}",
    {%- endif -%}
    {%- if item.SHORTNAME is not none -%}
        SHORTNAME="{{item.SHORTNAME}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_nghplmn_list -%}
    ADD NGHPLMN:
    {#- --- 必选参数 --- -#}
    NOID={{item.NOID}},
    MCC="{{item.MCC}}",
    MNC="{{item.MNC}}",
    ;
{%- endfor -%}
```

#### 6.2 打开NRF基本功能、NF发现的License。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

#### 6.3 配置NRF实例信息。

```jinja2
{%- for item in add_nfuuid_list -%}
    ADD NFUUID:
    {#- --- 必选参数 --- -#}
    NFTYPE={{item.NFTYPE}},
    NFINSTANCENAME="{{item.NFINSTANCENAME}}",
    ;
{%- endfor -%}
```

### 7 配置NRF服务化接口数据。

#### 7.1 增加NRF服务化接口的IP地址。

```jinja2
{%- for item in add_logicip_list -%}
    ADD LOGICIP:
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
        LOGICIPV4="{{item.LOGICIPV4}}",
    {%- endif -%}
    {#- --- 条件必选：IPVERSION=IPv6 时必选 --- -#}
    {%- if item.IPVERSION == 'IPv6' -%}
        LOGICIPV6="{{item.LOGICIPV6}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：IPVERSION=IPv4 时可选 --- -#}
    {%- if item.IPVERSION == 'IPv4' -%}
        {%- if item.IPV4MTU is not none -%}
            IPV4MTU={{item.IPV4MTU}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：IPVERSION=IPv6 时可选 --- -#}
    {%- if item.IPVERSION == 'IPv6' -%}
        {%- if item.IPV6MTU is not none -%}
            IPV6MTU={{item.IPV6MTU}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 7.2 配置Nnrf接口的HTTP信息。

```jinja2
{%- for item in add_httplegrp_list -%}
    ADD HTTPLEGRP:
    {#- --- 必选参数 --- -#}
    INDEX={{item.INDEX}},
    {#- --- 可选参数 --- -#}
    {%- if item.DESC is not none -%}
        DESC="{{item.DESC}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_httple_list -%}
    ADD HTTPLE:
    {#- --- 必选参数 --- -#}
    INDEX={{item.INDEX}},
    HTTPLEGRPIDX={{item.HTTPLEGRPIDX}},
    LETYPE={{item.LETYPE}},
    IPTYPE={{item.IPTYPE}},
    {#- --- 可选参数 --- -#}
    {%- if item.VPNNAME is not none -%}
        VPNNAME="{{item.VPNNAME}}",
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPTYPE=IPv4 时必选 --- -#}
    {%- if item.IPTYPE == 'IPv4' -%}
        IPV4="{{item.IPV4}}",
    {%- endif -%}
    {#- --- 条件必选：IPTYPE=IPv6 时必选 --- -#}
    {%- if item.IPTYPE == 'IPv6' -%}
        IPV6="{{item.IPV6}}",
    {%- endif -%}
    {#- --- 条件必选：LETYPE=SERVER 时必选 --- -#}
    {%- if item.LETYPE == 'SERVER' -%}
        TLSFLG={{item.TLSFLG}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：LETYPE=SERVER 时可选 --- -#}
    {%- if item.LETYPE == 'SERVER' -%}
        {%- if item.PORT is not none -%}
            PORT={{item.PORT}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件必选/可选参数 --- -#}
    {#- --- TLS索引: 条件必选(是否启用TLS=YES) / 条件可选(本端实体类型=CLIENT) --- -#}
    {%- if (item.TLSFLG == 'YES') -%}
        TLSIDX={{item.TLSIDX}},
    {%- elif (item.LETYPE == 'CLIENT') -%}
        {%- if item.TLSIDX is not none -%}
            TLSIDX={{item.TLSIDX}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_sbiaple_list -%}
    ADD SBIAPLE:
    {#- --- 必选参数 --- -#}
    INDEX={{item.INDEX}},
    HTTPLEGRPIDX={{item.HTTPLEGRPIDX}},
    NFTYPE={{item.NFTYPE}},
    {#- --- 可选参数 --- -#}
    {%- if item.DESCRIPTION is not none -%}
        DESCRIPTION="{{item.DESCRIPTION}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：NFTYPE=NFTypeCHF 时可选 --- -#}
    {%- if item.NFTYPE == 'NFTypeCHF' -%}
        {%- if item.CHFPEERNFTYPE is not none -%}
            CHFPEERNFTYPE={{item.CHFPEERNFTYPE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：NFTYPE=NFTypeSMF/NFTypeSMSF/NFTypeNWDAF/NFTypeUDN 时可选 --- -#}
    {%- if item.NFTYPE in ['NFTypeSMF', 'NFTypeSMSF', 'NFTypeNWDAF', 'NFTypeUDN'] -%}
        {%- if item.PEERNFTYPE is not none -%}
            PEERNFTYPE={{item.PEERNFTYPE}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 8 打开NF Token管理及NF认证的License。为指定的NF添加Token有效期。

```jinja2
{%- for item in set_licenseswitch_list_2 -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_tokenexp_list -%}
    ADD TOKENEXP:
    {#- --- 必选参数 --- -#}
    SCFGTYPE={{item.SCFGTYPE}},
    EXPTIME={{item.EXPTIME}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：SCFGTYPE=BYNFTYPE 时必选 --- -#}
    {%- if item.SCFGTYPE == 'BYNFTYPE' -%}
        NFTYPE={{item.NFTYPE}},
    {%- endif -%}
    {#- --- 条件必选：SCFGTYPE=BYFQDN 时必选 --- -#}
    {%- if item.SCFGTYPE == 'BYFQDN' -%}
        FQDN="{{item.FQDN}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 9 修改NRF定时器。

```jinja2
{%- for item in set_nrftimer_list -%}
    SET NRFTIMER:
    {#- --- 必选参数 --- -#}
    NFTYPE={{item.NFTYPE}},
    {#- --- 可选参数 --- -#}
    {%- if item.HBTIMES is not none -%}
        HBTIMES={{item.HBTIMES}},
    {%- endif -%}
    {%- if item.HEARTBEATTIMER is not none -%}
        HEARTBEATTIMER={{item.HEARTBEATTIMER}},
    {%- endif -%}
    {%- if item.DISCVALIDTIMER is not none -%}
        DISCVALIDTIMER={{item.DISCVALIDTIMER}},
    {%- endif -%}
    {%- if item.SUBVALIDTIMER is not none -%}
        SUBVALIDTIMER={{item.SUBVALIDTIMER}},
    {%- endif -%}
    ;
{%- endfor -%}
```


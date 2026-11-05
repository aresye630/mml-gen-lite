---
id: ''
name: 基于位置区分配IP地址
ne_type: UNC
type: feature
description: 运营商规划SMF为UE分配IP地址，可基于APN/DNN、位置、UPF或其任意组合分配地址，基于位置区分配IP地址的配置方法可参考本章节。  适用于GGSN、PGW-C、SMF、PGW-U、UPF。
risk_level: ''
doc_source: ["网络部署","业务专题","5G Core 用户IP地址管理解决方案","SMF分配IP地址","激活SMF分配IP地址功能","基于位置区分配IP地址"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
运营商规划SMF为UE分配IP地址，可基于APN/DNN、位置、UPF或其任意组合分配地址，基于位置区分配IP地址的配置方法可参考本章节。适用于GGSN、PGW-C、SMF、PGW-U、UPF。

## 必备事项
前提条件

请仔细阅读SMF分配IP地址流程。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    add_apn_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '配置APN实例。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        HASVPN:
          name: '绑定VPN'
          type: string
          enum:
          - ENABLE
          - DISABLE
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
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_vpninst_list:
      type: items
      properties:
        VPNINSTANCE:
          name: 'VPN实例名'
          type: string
          minLength: 1
          maxLength: 31
          required: true
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_addrpoolgrp_list:
      type: items
      properties:
        POOLGRPNAME:
          name: '地址池组名称'
          type: string
          minLength: 1
          maxLength: 79
          required: true
          description: '配置地址池组。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        POOLGRPTYPE:
          name: '地址池类型'
          type: string
          enum:
          - Local
          - UDM
          - Radius
          - DHCP
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: Local
    add_addrlacgroup_list:
      type: items
      properties:
        LACGROUPNAME:
          name: 'LAC组名'
          type: string
          minLength: 1
          maxLength: 32
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_addrlacid_list:
      type: items
      properties:
        LACGROUPNAME:
          name: 'LAC组名'
          type: string
          minLength: 1
          maxLength: 32
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LACSECNUM:
          name: 'LAC段编号'
          type: integer
          minimum: 0
          maximum: 23999
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LACSTARTID:
          name: 'LAC起始ID'
          type: string
          minLength: 1
          maxLength: 10
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LACENDID:
          name: 'LAC终止ID'
          type: string
          minLength: 1
          maxLength: 10
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_addrtacgroup_list:
      type: items
      properties:
        TACGROUPNAME:
          name: 'TAC组名称'
          type: string
          minLength: 1
          maxLength: 32
          required: true
          description: '配置TAC组。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        TACTYPE:
          name: 'TAC类型'
          type: string
          enum:
          - S1TAC
          - N2TAC
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_addrs1tacid_list:
      type: items
      properties:
        TACGROUPNAME:
          name: 'S1TAC组名'
          type: string
          minLength: 1
          maxLength: 32
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TACSECNUM:
          name: 'S1TAC段编号'
          type: integer
          minimum: 0
          maximum: 15999
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TACSTARTID:
          name: 'S1TAC起始ID'
          type: string
          minLength: 1
          maxLength: 10
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TACENDID:
          name: 'S1TAC终止ID'
          type: string
          minLength: 1
          maxLength: 10
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_addrn2tacid_list:
      type: items
      properties:
        TACGROUPNAME:
          name: 'N2TAC组名'
          type: string
          minLength: 1
          maxLength: 32
          required: true
          description: '配置N2TAC组内N2TAC号段。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        TACSECNUM:
          name: 'N2TAC段编号'
          type: integer
          minimum: 0
          maximum: 15999
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        TACSTARTID:
          name: 'N2TAC起始ID'
          type: string
          minLength: 1
          maxLength: 10
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        TACENDID:
          name: 'N2TAC终止ID'
          type: string
          minLength: 1
          maxLength: 10
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_addrupgroup_list:
      type: items
      properties:
        UPFGRPNAME:
          name: 'UPF组名称'
          type: string
          minLength: 1
          maxLength: 32
          required: true
          description: '配置UPF组。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        UPFGRPTYPE:
          name: 'UPF组类型'
          type: string
          enum:
          - Local
          - UDM
          - Radius
          - DHCP
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: Local
    add_upfbindgrp_list:
      type: items
      properties:
        UPFGRPNAME:
          name: 'UPF组名称'
          type: string
          minLength: 1
          maxLength: 32
          required: true
          description: '配置UPF和UPF组的绑定关系。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        UPFID:
          name: 'UPF实例标识'
          type: string
          minLength: 0
          maxLength: 255
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_poolgrpmap_list:
      type: items
      properties:
        MAPPINGNAME:
          name: '映射名称'
          type: string
          minLength: 1
          maxLength: 79
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        POOLGRPNAME:
          name: '地址池组名称'
          type: string
          minLength: 1
          maxLength: 79
          required: true
          description: '已通过**ADD ADDRPOOLGRP**配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        LOCATIONGRPTYPE:
          name: '位置区组类型'
          type: string
          enum:
          - LAC
          - TAC
          - None
          required: false
          description: '已通过**ADD ADDRTACGROUP**配置'
          data_source: '已配置数据中获取'
          pattern: ''
          default: None
        LOCATIONGRPNAME:
          name: '位置区组名称'
          type: string
          minLength: 1
          maxLength: 32
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        UPFGRPNAME:
          name: 'UPF组名称'
          type: string
          minLength: 1
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_addrpool_list:
      type: items
      properties:
        POOLNAME:
          name: '地址池名'
          type: string
          minLength: 1
          maxLength: 79
          required: true
          description: '为用户配置对应的地址池。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        POOLTYPE:
          name: '地址池类型'
          type: string
          enum:
          - Local
          - UDM
          - Radius
          - DHCP
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: Local
        HASVPN:
          name: '绑定VPN'
          type: string
          enum:
          - Disable
          - Enable
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: Disable
        VPNINSTANCE:
          name: 'VPN实例名'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPVERSION:
          name: 'IP地址类型'
          type: string
          enum:
          - IPv4
          - IPv6
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: IPv4
        CHECKIPVALID:
          name: '检查地址合法性'
          type: string
          enum:
          - Disable
          - Enable
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: Disable
        IMSSW:
          name: 'IMS开关'
          type: string
          enum:
          - Disable
          - Enable
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: Enable
        IPLEASE:
          name: '地址租约使能标志'
          type: string
          enum:
          - Disable
          - Enable
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: Disable
        OVERLAP:
          name: '是否允许地址重叠'
          type: string
          enum:
          - Disable
          - Enable
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: Disable
        RELEASETIME:
          name: '地址租期(秒)'
          type: integer
          minimum: 0
          maximum: 86400
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 10
        SINGLEIPFLAG:
          name: '子池类型'
          type: string
          enum:
          - Enable
          - Disable
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: Disable
    add_poolbindgrp_list:
      type: items
      properties:
        POOLGRPNAME:
          name: '地址池组名称'
          type: string
          minLength: 1
          maxLength: 79
          required: true
          description: '已通过**ADD ADDRPOOLGRP**配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        POOLNAME:
          name: '地址池名称'
          type: string
          minLength: 1
          maxLength: 79
          required: true
          description: '已通过**ADD ADDRPOOL**配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_section_list:
      type: items
      properties:
        POOLNAME:
          name: 'Pool名称'
          type: string
          minLength: 1
          maxLength: 79
          required: true
          description: '配置地址池里的地址段。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SECTIONNUM:
          name: 'Section序号'
          type: integer
          minimum: 0
          maximum: 63
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPVERSION:
          name: 'IP类型'
          type: string
          enum:
          - IPv4
          - IPv6
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        V4STARTIP:
          name: 'IPV4开始地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        V4ENDIP:
          name: 'IPV4结束地址'
          type: string
          maxLength: 15
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
          data_source: ''
          pattern: ''
          default: ''
        V6PREFIXLENGTH:
          name: 'IPv6前缀长度'
          type: integer
          minimum: 49
          maximum: 64
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        V6PREFIXSTART:
          name: 'IPv6前缀起始地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    mod_upnode_list:
      type: items
      properties:
        NFINSTANCENAME:
          name: 'UPF实例名称'
          type: string
          minLength: 0
          maxLength: 255
          required: true
          description: '配置UPF节点的地址分配属性。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        ADDRALLOCMODE:
          name: '地址分配属性'
          type: string
          enum:
          - INHERIT
          - SMF_ALLOC
          - UPF_FIRST
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_apnaddressattr_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '已通过**ADD APN**配置。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPV4ALLOCTYPE:
          name: 'IPV4分配方式'
          type: string
          enum:
          - LOCAL
          - RADIUS
          - DHCP
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPV4ALLOCPRIALG:
          name: '基于优先级的IPV4分配算法'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ALLOCPRECEDENCE:
          name: 'UE地址分配属性'
          type: string
          enum:
          - INHERIT
          - SMF_ALLOC
          - UPF_FIRST
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_ipallocrule_list:
      type: items
      properties:
        IPV4FIRSTRULESW:
          name: 'IPv4第一级规则开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '配置地址分配规则。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPV4FIRSTRULE:
          name: 'IPv4第一级规则'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_ipallocbylocglbsw_list:
      type: items
      properties:
        SWITCH:
          name: '基于位置区分配IPv4地址的全局开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_ipallocbylocsw_list:
      type: items
      properties:
        LOCATIONGRPTYPE:
          name: '位置区组类型'
          type: string
          enum:
          - LAC
          - TAC
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LOCATIONGRPNAME:
          name: '位置区组名称'
          type: string
          minLength: 1
          maxLength: 32
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SWITCH:
          name: 'IPv4开关'
          type: string
          enum:
          - DISABLE
          - INHERIT
          - ENABLE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_conflictip_list:
      type: items
      properties:
        POOLNAME:
          name: '地址池名称'
          type: string
          minLength: 1
          maxLength: 79
          required: true
          description: '配置冲突IP。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPVERSION:
          name: 'IP地址类型'
          type: string
          enum:
          - IPv4
          - IPv6
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: IPv4
        IPADDRESS:
          name: '冲突IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPV6PREFIX:
          name: '冲突IPv6地址前缀'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6PREFIXLEN:
          name: 'IPv6前缀长度'
          type: integer
          minimum: 49
          maximum: 64
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    mod_addrpool_list:
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
          - Local
          - UDM
          - Radius
          - DHCP
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RELEASETIME:
          name: '地址租期(秒)'
          type: integer
          minimum: 0
          maximum: 86400
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CHECKIPVALID:
          name: '白名单检查开关'
          type: string
          enum:
          - Disable
          - Enable
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IMSSW:
          name: 'IMS开关'
          type: string
          enum:
          - Disable
          - Enable
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPLEASE:
          name: '地址租约使能标志'
          type: string
          enum:
          - Disable
          - Enable
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        OVERLAP:
          name: '是否允许地址重叠'
          type: string
          enum:
          - Disable
          - Enable
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SINGLEIPFLAG:
          name: '子池类型'
          type: string
          enum:
          - Enable
          - Disable
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_vpninst_list_1:
      type: items
      properties:
        VPNINSTANCE:
          name: 'VPN实例'
          type: string
          minLength: 1
          maxLength: 31
          required: true
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_pool_list:
      type: items
      properties:
        POOLNAME:
          name: '地址池名称'
          type: string
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        POOLTYPE:
          name: '地址池类型'
          type: string
          required: false
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: ''
        HASVPN:
          name: '绑定VPN'
          type: string
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        VPNINSTANCE:
          name: 'VPN实例名'
          type: string
          required: false
          description: '可以使用**LST VPNINST**命令进行查询。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_section_list_1:
      type: items
      properties:
        POOLNAME:
          name: '地址池名称'
          type: string
          minLength: 1
          maxLength: 79
          required: true
          description: '可以使用**LST POOL**命令进行查询。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SECTIONNUM:
          name: '地址段号'
          type: integer
          minimum: 0
          maximum: 63
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPVERSION:
          name: 'IP地址类型'
          type: string
          enum:
          - IPv4
          - IPv6
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        V4STARTIP:
          name: '地址段的起始IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        V4ENDIP:
          name: '地址段的终止IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        V6PREFIXEND:
          name: 'IPv6前缀结束地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        V6PREFIXLENGTH:
          name: 'IPv6前缀长度'
          type: integer
          minimum: 49
          maximum: 64
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        V6PREFIXSTART:
          name: 'IPv6前缀起始地址'
          type: string
          maxLength: 39
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
          description: '-'
          data_source: '本端规划'
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
          description: '-'
          data_source: '本端规划'
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
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        VRFNAME:
          name: 'VPN名称'
          type: string
          maxLength: 31
          required: false
          description: '可以使用**LST VPNINST**命令进行查询。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: '_public_'
        SCHEMAROUID:
          name: '路由器标识'
          type: string
          maxLength: 15
          required: false
          description: '须知：  Router ID必须全网唯一。'
          data_source: '全网规划'
          pattern: ''
          default: ''
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
    add_ospfarea_list:
      type: items
      properties:
        PROCID:
          name: '进程号'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        AREAID:
          name: '区域号'
          type: string
          maxLength: 15
          required: true
          description: '-'
          data_source: '与对端协商'
          pattern: ''
          default: ''
    add_ospfnetwork_list:
      type: items
      properties:
        PROCID:
          name: '进程号'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        AREAID:
          name: '区域号'
          type: string
          maxLength: 15
          required: true
          description: '-'
          data_source: '与对端协商'
          pattern: ''
          default: ''
        IPADDRESS:
          name: 'IP地址'
          type: string
          maxLength: 15
          required: true
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        WILDCARDMASK:
          name: '反掩码'
          type: string
          maxLength: 15
          required: true
          description: '-'
          data_source: '全网规划'
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
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        TOPOID:
          name: '拓扑标识'
          type: integer
          minimum: 0
          maximum: 0
          required: false
          description: '-'
          data_source: '全网规划'
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
          description: '-'
          data_source: '本端规划'
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
  examples:
    add_apn_list:
    - APN: 'apn-test'
      HASVPN: ENABLE
      VPNINSTANCE: 'vpn1'
    add_vpninst_list:
    - VPNINSTANCE: 'vpn1'
    add_addrpoolgrp_list:
    - POOLGRPNAME: 'poolgroup1'
      POOLGRPTYPE: Local
    add_addrlacgroup_list:
    - LACGROUPNAME: ''
    add_addrlacid_list:
    - LACGROUPNAME: ''
      LACSECNUM: ''
      LACSTARTID: ''
      LACENDID: ''
    add_addrtacgroup_list:
    - TACGROUPNAME: 'TAC1'
      TACTYPE: N2TAC
    add_addrs1tacid_list:
    - TACGROUPNAME: ''
      TACSECNUM: ''
      TACSTARTID: ''
      TACENDID: ''
    add_addrn2tacid_list:
    - TACGROUPNAME: 'TAC1'
      TACSECNUM: 2
      TACSTARTID: '0x000001'
      TACENDID: '0x00001F'
    add_addrupgroup_list:
    - UPFGRPNAME: 'upfgrp1'
      UPFGRPTYPE: Local
    add_upfbindgrp_list:
    - UPFGRPNAME: 'upfgrp1'
      UPFID: 'upf_instance_1'
    add_poolgrpmap_list:
    - MAPPINGNAME: 'one'
      POOLGRPNAME: 'poolgroup1'
      LOCATIONGRPTYPE: TAC
      LOCATIONGRPNAME: 'TAC1'
      UPFGRPNAME: 'upfgrp1'
    add_addrpool_list:
    - POOLNAME: 'pool01'
      POOLTYPE: Local
      HASVPN: Enable
      VPNINSTANCE: 'vpn1'
      IPVERSION: IPV4
      CHECKIPVALID: Enable
      IMSSW: Enable
      IPLEASE: Disable
      OVERLAP: Disable
      RELEASETIME: 10
      SINGLEIPFLAG: Disable
    add_poolbindgrp_list:
    - POOLGRPNAME: 'poolgroup1'
      POOLNAME: 'pool01'
    add_section_list:
    - POOLNAME: 'pool01'
      SECTIONNUM: 1
      IPVERSION: IPv4
      V4STARTIP: '10.10.1.1'
      V4ENDIP: '10.10.1.10'
      V6PREFIXEND: ''
      V6PREFIXLENGTH: ''
      V6PREFIXSTART: ''
    mod_upnode_list:
    - NFINSTANCENAME: 'upf_instance_1'
      ADDRALLOCMODE: INHERIT
    set_apnaddressattr_list:
    - APN: 'apn-test'
      IPV4ALLOCTYPE: LOCAL
      IPV4ALLOCPRIALG: ENABLE
      ALLOCPRECEDENCE: SMF_ALLOC
    set_ipallocrule_list:
    - IPV4FIRSTRULESW: ENABLE
      IPV4FIRSTRULE: APN-0&LOCATION-1&UPNODE-0
    set_ipallocbylocglbsw_list:
    - SWITCH: ENABLE
    set_ipallocbylocsw_list:
    - LOCATIONGRPTYPE: TAC
      LOCATIONGRPNAME: 'TAC1'
      SWITCH: ENABLE
    add_conflictip_list:
    - POOLNAME: 'pool01'
      IPVERSION: IPv4
      IPADDRESS: '10.1.1.1'
      IPV6PREFIX: ''
      IPV6PREFIXLEN: ''
    mod_addrpool_list:
    - POOLNAME: 'pool01'
      POOLTYPE: LOCAL
      RELEASETIME: 20
      CHECKIPVALID: ''
      IMSSW: ''
      IPLEASE: ''
      OVERLAP: ''
      SINGLEIPFLAG: ''
    add_vpninst_list_1:
    - VPNINSTANCE: 'vpn1'
    add_pool_list:
    - POOLNAME: pool01
      POOLTYPE: EXTERNAL
      HASVPN: ENABLE
      VPNINSTANCE: vpn1
    add_section_list_1:
    - POOLNAME: 'pool01'
      SECTIONNUM: 1
      IPVERSION: IPV4
      V4STARTIP: '10.10.1.1'
      V4ENDIP: '10.10.1.10'
      V6PREFIXEND: ''
      V6PREFIXLENGTH: ''
      V6PREFIXSTART: ''
    add_l3vpninst_list:
    - VRFNAME: 'vpn1'
    add_vpninstaf_list:
    - VRFNAME: 'vpn1'
      AFTYPE: ipv4uni
    add_ospf_list:
    - PROCID: 100
      VRFNAME: 'vpn1'
      SCHEMAROUID: '10.10.10.1'
      LSAARRMAXINTV: 1000
      LSAARRSTARINTV: 500
      LSAARRHLDINTV: 500
      LSAARRINTVFLAG: FALSE
    add_ospfarea_list:
    - PROCID: 100
      AREAID: '0.0.0.0'
    add_ospfnetwork_list:
    - PROCID: 100
      AREAID: '0.0.0.0'
      IPADDRESS: '10.13.21.0'
      WILDCARDMASK: '0.0.0.255'
    add_ospfimportroute_list:
    - PROCID: 100
      TOPOID: 0
      PROTOCOL: wlr
      PERMITIBGPCFG: FALSE
      PROTOCOLPROCID: 1
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 在SMF上执行如下命令：

#### 1.1 指定APN实例名称。

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

#### 1.2 配置VPN实例。

```jinja2
{%- for item in add_vpninst_list -%}
    ADD VPNINST:
    {#- --- 必选参数 --- -#}
    VPNINSTANCE="{{item.VPNINSTANCE}}",
    ;
{%- endfor -%}
```

#### 1.3 配置地址池组名称。

```jinja2
{%- for item in add_addrpoolgrp_list -%}
    ADD ADDRPOOLGRP:
    {#- --- 必选参数 --- -#}
    POOLGRPNAME="{{item.POOLGRPNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.POOLGRPTYPE is not none -%}
        POOLGRPTYPE={{item.POOLGRPTYPE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 1.4 配置LAC组。

```jinja2
{%- for item in add_addrlacgroup_list -%}
    ADD ADDRLACGROUP:
    {#- --- 必选参数 --- -#}
    LACGROUPNAME="{{item.LACGROUPNAME}}",
    ;
{%- endfor -%}
```

#### 1.5 配置LAC组内LAC号段。

```jinja2
{%- for item in add_addrlacid_list -%}
    ADD ADDRLACID:
    {#- --- 必选参数 --- -#}
    LACENDID="{{item.LACENDID}}",
    LACGROUPNAME="{{item.LACGROUPNAME}}",
    LACSECNUM={{item.LACSECNUM}},
    LACSTARTID="{{item.LACSTARTID}}",
    ;
{%- endfor -%}
```

#### 1.6 配置TAC组。

```jinja2
{%- for item in add_addrtacgroup_list -%}
    ADD ADDRTACGROUP:
    {#- --- 必选参数 --- -#}
    TACGROUPNAME="{{item.TACGROUPNAME}}",
    TACTYPE={{item.TACTYPE}},
    ;
{%- endfor -%}
```

#### 1.7 配置S1TAC组内S1TAC号段。

```jinja2
{%- for item in add_addrs1tacid_list -%}
    ADD ADDRS1TACID:
    {#- --- 必选参数 --- -#}
    TACENDID="{{item.TACENDID}}",
    TACGROUPNAME="{{item.TACGROUPNAME}}",
    TACSECNUM={{item.TACSECNUM}},
    TACSTARTID="{{item.TACSTARTID}}",
    ;
{%- endfor -%}
```

#### 1.8 配置N2TAC组内N2TAC号段。

```jinja2
{%- for item in add_addrn2tacid_list -%}
    ADD ADDRN2TACID:
    {#- --- 必选参数 --- -#}
    TACGROUPNAME="{{item.TACGROUPNAME}}",
    TACSECNUM={{item.TACSECNUM}},
    TACSTARTID="{{item.TACSTARTID}}",
    TACENDID="{{item.TACENDID}}",
    ;
{%- endfor -%}
```

#### 1.9 配置UPF组。

```jinja2
{%- for item in add_addrupgroup_list -%}
    ADD ADDRUPGROUP:
    {#- --- 必选参数 --- -#}
    UPFGRPNAME="{{item.UPFGRPNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.UPFGRPTYPE is not none -%}
        UPFGRPTYPE={{item.UPFGRPTYPE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 1.10 配置UPF和UPF组的绑定关系。

```jinja2
{%- for item in add_upfbindgrp_list -%}
    ADD UPFBINDGRP:
    {#- --- 必选参数 --- -#}
    UPFGRPNAME="{{item.UPFGRPNAME}}",
    UPFID="{{item.UPFID}}",
    ;
{%- endfor -%}
```

#### 1.11 为该位置区组绑定本地地址池组。

```jinja2
{%- for item in add_poolgrpmap_list -%}
    ADD POOLGRPMAP:
    {#- --- 必选参数 --- -#}
    MAPPINGNAME="{{item.MAPPINGNAME}}",
    POOLGRPNAME="{{item.POOLGRPNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.LOCATIONGRPTYPE is not none -%}
        LOCATIONGRPTYPE={{item.LOCATIONGRPTYPE}},
    {%- endif -%}
    {%- if item.UPFGRPNAME is not none -%}
        UPFGRPNAME="{{item.UPFGRPNAME}}",
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：LOCATIONGRPTYPE=LAC/TAC 时必选 --- -#}
    {%- if item.LOCATIONGRPTYPE in ['LAC', 'TAC'] -%}
        LOCATIONGRPNAME="{{item.LOCATIONGRPNAME}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 1.12 创建本地地址池。

```jinja2
{%- for item in add_addrpool_list -%}
    ADD ADDRPOOL:
    {#- --- 必选参数 --- -#}
    POOLNAME="{{item.POOLNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.POOLTYPE is not none -%}
        POOLTYPE={{item.POOLTYPE}},
    {%- endif -%}
    {%- if item.HASVPN is not none -%}
        HASVPN={{item.HASVPN}},
    {%- endif -%}
    {%- if item.IPVERSION is not none -%}
        IPVERSION={{item.IPVERSION}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：HASVPN=Enable 时必选 --- -#}
    {%- if item.HASVPN == 'Enable' -%}
        VPNINSTANCE="{{item.VPNINSTANCE}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：POOLTYPE=UDM/Radius 时可选 --- -#}
    {%- if item.POOLTYPE in ['UDM', 'Radius'] -%}
        {%- if item.CHECKIPVALID is not none -%}
            CHECKIPVALID={{item.CHECKIPVALID}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：POOLTYPE=Local 时可选 --- -#}
    {%- if item.POOLTYPE == 'Local' -%}
        {%- if item.IMSSW is not none -%}
            IMSSW={{item.IMSSW}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：POOLTYPE=Local 时可选 --- -#}
    {%- if item.POOLTYPE == 'Local' -%}
        {%- if item.IPLEASE is not none -%}
            IPLEASE={{item.IPLEASE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：POOLTYPE=Local 时可选 --- -#}
    {%- if item.POOLTYPE == 'Local' -%}
        {%- if item.OVERLAP is not none -%}
            OVERLAP={{item.OVERLAP}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：POOLTYPE=Local 时可选 --- -#}
    {%- if item.POOLTYPE == 'Local' -%}
        {%- if item.RELEASETIME is not none -%}
            RELEASETIME={{item.RELEASETIME}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：POOLTYPE=Local 时可选 --- -#}
    {%- if item.POOLTYPE == 'Local' -%}
        {%- if item.SINGLEIPFLAG is not none -%}
            SINGLEIPFLAG={{item.SINGLEIPFLAG}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 1.13 配置地址池与地址池组绑定。

```jinja2
{%- for item in add_poolbindgrp_list -%}
    ADD POOLBINDGRP:
    {#- --- 必选参数 --- -#}
    POOLGRPNAME="{{item.POOLGRPNAME}}",
    POOLNAME="{{item.POOLNAME}}",
    ;
{%- endfor -%}
```

#### 1.14 配置地址池里的IPv4地址段。

```jinja2
{%- for item in add_section_list -%}
    ADD SECTION:
    {#- --- 必选参数 --- -#}
    POOLNAME="{{item.POOLNAME}}",
    SECTIONNUM={{item.SECTIONNUM}},
    IPVERSION={{item.IPVERSION}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPVERSION=IPv4 时必选 --- -#}
    {%- if item.IPVERSION == 'IPv4' -%}
        V4STARTIP="{{item.V4STARTIP}}",
    {%- endif -%}
    {#- --- 条件必选：IPVERSION=IPv4 时必选 --- -#}
    {%- if item.IPVERSION == 'IPv4' -%}
        V4ENDIP="{{item.V4ENDIP}}",
    {%- endif -%}
    {#- --- 条件必选：IPVERSION=IPv6 时必选 --- -#}
    {%- if item.IPVERSION == 'IPv6' -%}
        V6PREFIXEND="{{item.V6PREFIXEND}}",
    {%- endif -%}
    {#- --- 条件必选：IPVERSION=IPv6 时必选 --- -#}
    {%- if item.IPVERSION == 'IPv6' -%}
        V6PREFIXLENGTH={{item.V6PREFIXLENGTH}},
    {%- endif -%}
    {#- --- 条件必选：IPVERSION=IPv6 时必选 --- -#}
    {%- if item.IPVERSION == 'IPv6' -%}
        V6PREFIXSTART="{{item.V6PREFIXSTART}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 本地地址池：本地负责分配地址的地址池。本地地址池下需要配置地址段，一个本地地址池最多可以配置64个地址段。

#### 配置地址池后，必须配置地址段。如果不配置地址段，将导致用户激活失败。

#### 本地地址池在配置时，建议尽量使用完整的网段地址，方便生成用户下行路由。

#### 1.15 配置UPF节点的地址分配属性。

```jinja2
{%- for item in mod_upnode_list -%}
    MOD UPNODE:
    {#- --- 必选参数 --- -#}
    NFINSTANCENAME="{{item.NFINSTANCENAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.ADDRALLOCMODE is not none -%}
        ADDRALLOCMODE={{item.ADDRALLOCMODE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 1.16 配置基于APN的地址分配属性。

```jinja2
{%- for item in set_apnaddressattr_list -%}
    SET APNADDRESSATTR:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    {#- --- 可选参数 --- -#}
    {%- if item.IPV4ALLOCTYPE is not none -%}
        IPV4ALLOCTYPE={{item.IPV4ALLOCTYPE}},
    {%- endif -%}
    {%- if item.IPV4ALLOCPRIALG is not none -%}
        IPV4ALLOCPRIALG={{item.IPV4ALLOCPRIALG}},
    {%- endif -%}
    {%- if item.ALLOCPRECEDENCE is not none -%}
        ALLOCPRECEDENCE={{item.ALLOCPRECEDENCE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 1.17 配置地址分配规则。

```jinja2
{%- for item in set_ipallocrule_list -%}
    SET IPALLOCRULE:
    {#- --- 可选参数 --- -#}
    {%- if item.IPV4FIRSTRULESW is not none -%}
        IPV4FIRSTRULESW={{item.IPV4FIRSTRULESW}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPV4FIRSTRULESW=ENABLE 时必选 --- -#}
    {%- if item.IPV4FIRSTRULESW == 'ENABLE' -%}
        IPV4FIRSTRULE={{item.IPV4FIRSTRULE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 1.18 配置基于位置区地址分配的全局开关。

```jinja2
{%- for item in set_ipallocbylocglbsw_list -%}
    SET IPALLOCBYLOCGLBSW:
    {#- --- 必选参数 --- -#}
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

#### 1.19 （可选）如果某一指定位置区的地址分配开关不同于全局位置区地址分配开关的使能状态，则需执行配置基于指定位置区分配地址的开关。

```jinja2
{%- if is_optional_location_ip_allocation_switch -%}
    {%- for item in set_ipallocbylocsw_list -%}
        SET IPALLOCBYLOCSW:
        {#- --- 必选参数 --- -#}
        LOCATIONGRPTYPE={{item.LOCATIONGRPTYPE}},
        LOCATIONGRPNAME="{{item.LOCATIONGRPNAME}}",
        SWITCH={{item.SWITCH}},
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 1.20 在本地地址池中将冲突的地址标识为冲突状态，禁止地址被分配给用户。

```jinja2
{%- for item in add_conflictip_list -%}
    ADD CONFLICTIP:
    {#- --- 必选参数 --- -#}
    POOLNAME="{{item.POOLNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.IPVERSION is not none -%}
        IPVERSION={{item.IPVERSION}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPVERSION=IPv4 时必选 --- -#}
    {%- if item.IPVERSION == 'IPv4' -%}
        IPADDRESS="{{item.IPADDRESS}}",
    {%- endif -%}
    {#- --- 条件必选：IPVERSION=IPv6 时必选 --- -#}
    {%- if item.IPVERSION == 'IPv6' -%}
        IPV6PREFIX="{{item.IPV6PREFIX}}",
    {%- endif -%}
    {#- --- 条件必选：IPVERSION=IPv6 时必选 --- -#}
    {%- if item.IPVERSION == 'IPv6' -%}
        IPV6PREFIXLEN={{item.IPV6PREFIXLEN}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 1.21 配置本地地址池中IP地址的等待释放时间。

```jinja2
{%- for item in mod_addrpool_list -%}
    MOD ADDRPOOL:
    {#- --- 必选参数 --- -#}
    POOLNAME="{{item.POOLNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.POOLTYPE is not none -%}
        POOLTYPE={{item.POOLTYPE}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：POOLTYPE=Local 时可选 --- -#}
    {%- if item.POOLTYPE == 'Local' -%}
        {%- if item.RELEASETIME is not none -%}
            RELEASETIME={{item.RELEASETIME}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：POOLTYPE=UDM/Radius 时可选 --- -#}
    {%- if item.POOLTYPE in ['UDM', 'Radius'] -%}
        {%- if item.CHECKIPVALID is not none -%}
            CHECKIPVALID={{item.CHECKIPVALID}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：POOLTYPE=Local 时可选 --- -#}
    {%- if item.POOLTYPE == 'Local' -%}
        {%- if item.IMSSW is not none -%}
            IMSSW={{item.IMSSW}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：POOLTYPE=Local 时可选 --- -#}
    {%- if item.POOLTYPE == 'Local' -%}
        {%- if item.IPLEASE is not none -%}
            IPLEASE={{item.IPLEASE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：POOLTYPE=Local 时可选 --- -#}
    {%- if item.POOLTYPE == 'Local' -%}
        {%- if item.OVERLAP is not none -%}
            OVERLAP={{item.OVERLAP}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：POOLTYPE=Local 时可选 --- -#}
    {%- if item.POOLTYPE == 'Local' -%}
        {%- if item.SINGLEIPFLAG is not none -%}
            SINGLEIPFLAG={{item.SINGLEIPFLAG}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 2 在UPF上执行如下命令：

#### 2.1 配置VPN实例。

```jinja2
{%- for item in add_vpninst_list_1 -%}
    ADD VPNINST:
    {#- --- 必选参数 --- -#}
    VPNINSTANCE="{{item.VPNINSTANCE}}",
    ;
{%- endfor -%}
```

#### 2.2 （可选）如需节省UPF路由，配置EXTERNAL类型地址池。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_pool_list的变量区（command: ADD POOL） -#}
<!-- MISSING_MACRO: command=ADD POOL list_name=add_pool_list step_id=2.2 -->
```

#### 2.3 （可选）如需节省UPF路由，配置地址池里的IPv4地址段。

```jinja2
{%- if is_optional_pool_ipv4_section -%}
    {%- for item in add_section_list_1 -%}
        ADD SECTION:
        {#- --- 必选参数 --- -#}
        POOLNAME="{{item.POOLNAME}}",
        SECTIONNUM={{item.SECTIONNUM}},
        IPVERSION={{item.IPVERSION}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：IPVERSION=IPv4 时必选 --- -#}
        {%- if item.IPVERSION == 'IPv4' -%}
            V4STARTIP="{{item.V4STARTIP}}",
        {%- endif -%}
        {#- --- 条件必选：IPVERSION=IPv4 时必选 --- -#}
        {%- if item.IPVERSION == 'IPv4' -%}
            V4ENDIP="{{item.V4ENDIP}}",
        {%- endif -%}
        {#- --- 条件必选：IPVERSION=IPv6 时必选 --- -#}
        {%- if item.IPVERSION == 'IPv6' -%}
            V6PREFIXEND="{{item.V6PREFIXEND}}",
        {%- endif -%}
        {#- --- 条件必选：IPVERSION=IPv6 时必选 --- -#}
        {%- if item.IPVERSION == 'IPv6' -%}
            V6PREFIXLENGTH={{item.V6PREFIXLENGTH}},
        {%- endif -%}
        {#- --- 条件必选：IPVERSION=IPv6 时必选 --- -#}
        {%- if item.IPVERSION == 'IPv6' -%}
            V6PREFIXSTART="{{item.V6PREFIXSTART}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 2.4 配置VPN实例。

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

#### 2.5 启动OSPF进程。

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
    {%- if item.LSAARRINTVFLAG is not none -%}
        LSAARRINTVFLAG={{item.LSAARRINTVFLAG}},
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
```

#### 2.6 添加OSPF区域。

```jinja2
{%- for item in add_ospfarea_list -%}
    ADD OSPFAREA:
    {#- --- 必选参数 --- -#}
    PROCID={{item.PROCID}},
    AREAID="{{item.AREAID}}",
    ;
{%- endfor -%}
```

#### 2.7 配置运行OSPF协议的接口。

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

#### 2.8 引入WLR路由。

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

#### 采用路由策略方式发布路由时，不能只选择发布WLR\_SP或者WLR\_UD路由，必须选择WLR方式发布所有路由。


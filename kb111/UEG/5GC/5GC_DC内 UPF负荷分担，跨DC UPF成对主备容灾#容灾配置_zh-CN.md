---
id: ''
name: 容灾配置
ne_type: UEG
type: feature
description: 用于配置DC内负荷分担，跨DC UPF成对主备容灾场景下SMF与UPF的配置。
tags: []
risk_level: ''
doc_source: ["专网（仅连接，园区入驻式）","业务原理","5GC toB 容灾机制（专网，入驻式）","容灾方案","DC内 UPF负荷分担，跨DC UPF成对主备容灾","容灾配置"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
用于配置DC内负荷分担，跨DC UPF成对主备容灾场景下SMF与UPF的配置。

## 必备事项
前提条件

* SMF与UPF已完成基础配置。
* 主备UPF间已完成静态地址路由冗余配置。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    add_apn_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '增加APN信息。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_nsdnn_list:
      type: items
      properties:
        NSIDX:
          name: '网络切片索引'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: true
          description: '* 增加DNN切片绑定关系。 * 参数“NSIDX”由命令**LST NFNS**查询结果中的“网络切片索引”获取。当存在切片发放场景时，此参数引用切片发放对应的参数。 * 参数“DNN”已在**ADD APN**中定义。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        DNN:
          name: '数据网络名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    set_apnpccfunc_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          maxLength: 63
          required: true
          description: '关闭本地用户、漫游用户、拜访地用户动态PCC功能，参数“APN”已在**ADD APN**中定义。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        HOMEPCCSWITCH:
          name: '本地用户动态PCC功能'
          type: string
          enum:
          - DISABLE
          - ENABLE
          - INHERIT
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        ROAMPCCSWITCH:
          name: '漫游用户动态PCC功能'
          type: string
          enum:
          - DISABLE
          - ENABLE
          - INHERIT
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        VISITPCCSWITCH:
          name: '拜访用户动态PCC功能'
          type: string
          enum:
          - DISABLE
          - ENABLE
          - INHERIT
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_apnusrprofg_list:
      type: items
      properties:
        APN:
          name: 'APN'
          type: string
          maxLength: 63
          required: true
          description: '配置将UserProfile Group绑定到APN。参数“APN”已在**ADD APN**中定义，参数“USERPROFGNAME”已在PCC业务配置的**ADD USRPROFGROUP**命令中定义。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        USERPROFGNAME:
          name: '用户模板组名称'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_apnaddressattr_list:
      type: items
      properties:
        ALLOCWITHOUTPCO:
          name: 'ALLOCWITHOUTPCO'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ANTISPOOFINGDI:
          name: 'ANTISPOOFINGDI'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ANTISPOOFINGUI:
          name: 'ANTISPOOFINGUI'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        FRAMEDROUTE:
          name: '手机后路由'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        IGNORECONFLICT:
          name: 'IGNORECONFLICT'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV4ALLOCTYPE:
          name: 'IPV4ALLOCTYPE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV4RADIUSPRIOR:
          name: 'IPV4RADIUSPRIOR'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6ALLOCTYPE:
          name: 'IPV6ALLOCTYPE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6RADIUSPRIOR:
          name: 'IPV6RADIUSPRIOR'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6RAINTV:
          name: 'IPV6RAINTV'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6RAOFLAG:
          name: 'IPV6RAOFLAG'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RADIUSIPROUTE:
          name: 'RADIUSIPROUTE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DHCPIPROUTE:
          name: 'DHCPIPROUTE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        STATICIP:
          name: 'STATICIP'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        STATICIPROUTE:
          name: 'STATICIPROUTE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SUPPORTIPV4:
          name: '支持IPV4'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        SUPPORTIPV6:
          name: '支持IPV6'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        SUPPORTPRIOR:
          name: 'SUPPORTPRIOR'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        APN:
          name: 'APN名称'
          type: string
          required: false
          description: '配置APN地址分配属性。参数“APN”已在**ADD APN**中定义。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        IPTYPEFORDUALIP:
          name: '为双栈用户返回的地址类型'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        SINGLEADDRCAUSE:
          name: '分配单栈地址时返回的原因值'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV4ALLOCPRIALG:
          name: 'IPV4ALLOCPRIALG'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6ALLOCPRIALG:
          name: 'IPV6ALLOCPRIALG'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RDSSVRCTRL:
          name: 'RDSSVRCTRL'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6RAMTUSW:
          name: 'RA携带MTU选项开关'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPV6MTU:
          name: 'IPV6MTU'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6RALIFETIME:
          name: 'IPv6 RA消息路由生命周期'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV6RATIMES:
          name: 'IPV6RATIMES'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_pnfprofile_list:
      type: items
      properties:
        NFINSTANCEID:
          name: 'NF实例标识'
          type: string
          minLength: 1
          maxLength: 36
          required: true
          description: 'SMF本端添加UPF。'
          data_source: '本端规划'
          pattern: ''
          default: ''
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
          - NfCUSTOM_OCS
          - NfSCP
          - NfPCSCF
          - NfMBSMF
          - NfUDN
          - NfNWDAF
          - NfSCF
          - NfKMC
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        NFSTATUS:
          name: 'NF状态'
          type: string
          enum:
          - Invalid
          - Registered
          - Suspend
          - DeRegistered
          - UnDiscoverable
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: Registered
        FQDN:
          name: '域名'
          type: string
          minLength: 0
          maxLength: 255
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPADDRESSTYPE:
          name: 'IP地址类型'
          type: string
          enum:
          - IPTypeV4
          - IPTypeV6
          - IPTypeV4V6
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV4ADDRESS1:
          name: 'IP地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        PORT:
          name: '端口号'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_pnfns_list:
      type: items
      properties:
        INDEX:
          name: '索引'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: true
          description: '配置用户面支持的服务切片信息。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        NFINSTANCEID:
          name: 'NF实例标识'
          type: string
          minLength: 0
          maxLength: 50
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        SST:
          name: '切片/服务类型'
          type: integer
          minimum: 0
          maximum: 255
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_pnfdnn_list:
      type: items
      properties:
        INDEX:
          name: '索引'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: true
          description: '配置UPF的DNN属性，用于在用户会话激活时基于用户的DNN选择UPF。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        NFINSTANCEID:
          name: 'NF实例标识'
          type: string
          minLength: 0
          maxLength: 38
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        DNN:
          name: '数据网络名称'
          type: string
          minLength: 0
          maxLength: 66
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        PNFNSINDEX:
          name: '对端NF的切片索引'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: 0
        PRISWITCH:
          name: '优先级功能开关'
          type: string
          enum:
          - INHERIT
          - SPECIFIC
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: INHERIT
        CAPSWITCH:
          name: '容量功能开关'
          type: string
          enum:
          - INHERIT
          - SPECIFIC
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: INHERIT
    add_upnode_list:
      type: items
      properties:
        NFINSTANCENAME:
          name: 'UPF实例名称'
          type: string
          minLength: 0
          maxLength: 255
          required: true
          description: '配置UPF的属性。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        LOCATION:
          name: 'UPF位置特征'
          type: string
          enum:
          - Local
          - Central
          - CentralOnly
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: Central
        UPFUNCTION:
          name: 'UPF支持功能'
          type: string
          enum:
          - None
          - UlClAndBp
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: None
        LOCK:
          name: 'UPF锁'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: FALSE
        APSAMIGFUNC:
          name: '辅锚点UPF故障迁移功能开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
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
          default: INHERIT
        SHAREDUPFSW:
          name: 'UPF共享开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
        VPNNAME:
          name: 'VPN名称'
          type: string
          minLength: 1
          maxLength: 31
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: '_public_'
        SUPATSSS:
          name: '是否支持作为ATSSS UPF'
          type: string
          enum:
          - Enable
          - Disable
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: Disable
        IPV6NDPLCY:
          name: 'IPv6 ND信息携带方式'
          type: string
          enum:
          - PRIVATE
          - STANDARD
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: PRIVATE
        IOSWITCH:
          name: '惯性运行开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
        CAMPUSSW:
          name: '园区UPF开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
        ULCLFWDTNLSW:
          name: 'ULCL UPF间创建转发隧道开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
        PDUESTWITHOUTN9:
          name: '是否支持UPF无N9逻辑接口地址时作为主锚点激活'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
        NGLANSW:
          name: '是否支持5G LAN'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
    add_uparea_list:
      type: items
      properties:
        AREANAME:
          name: '位置区名称'
          type: string
          minLength: 1
          maxLength: 255
          required: true
          description: '与**ADD PNFSMFSERAREA**中“SMFSERVINGAREA”的取值一致。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        AREATYPE:
          name: 'ARE类型'
          type: string
          enum:
          - S1TAI
          - N2TAI
          - LAI
          required: true
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_upareabindn2tai_list:
      type: items
      properties:
        AREANAME:
          name: 'UP位置区名称'
          type: string
          minLength: 0
          maxLength: 255
          required: true
          description: '已通过命令**ADD UPAREA**配置。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        N2BEGINTAI:
          name: 'N2TAI范围开始值'
          type: string
          minLength: 11
          maxLength: 12
          required: true
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        N2ENDTAI:
          name: 'N2TAI范围结束值'
          type: string
          minLength: 11
          maxLength: 12
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_pnfsmfserarea_list:
      type: items
      properties:
        NFINSTANCEID:
          name: 'NF实例标识'
          type: string
          minLength: 0
          maxLength: 50
          required: true
          description: 'SMF本端配置UPF所覆盖的区域，用于在用户会话激活时基于用户位置区选择UPF。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        SMFSERVINGAREA:
          name: 'SMF服务区域'
          type: string
          minLength: 1
          maxLength: 255
          required: true
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
          required: false
          description: '为采用静态地址分配方式的用户配置对应的地址池。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPVERSION:
          name: 'IP地址类型'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        POOLTYPE:
          name: '地址池类型'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        CHECKIPVALID:
          name: '白名单检查开关'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        HASVPN:
          name: '绑定VPN'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        VPNINSTANCE:
          name: 'VPN实例名'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_section_list:
      type: items
      properties:
        POOLNAME:
          name: '地址池名称'
          type: string
          minLength: 0
          maxLength: 79
          required: true
          description: '配置本地地址池里的地址段。'
          data_source: '本端规划'
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
          data_source: '全网规划'
          pattern: ''
          default: ''
        V4STARTIP:
          name: 'IPv4开始地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        V4ENDIP:
          name: 'IPv4结束地址'
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
    add_poolbindapn_list:
      type: items
      properties:
        POOLNAME:
          name: '地址池名称'
          type: string
          minLength: 1
          maxLength: 79
          required: true
          description: '-'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        APN:
          name: 'APN名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: ''
          data_source: '已配置数据中获取'
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
          name: '地址池组类型'
          type: string
          enum:
          - Local
          - UDM
          - Radius
          - DHCP
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: Local
        IPV4ALLOCPRIALG:
          name: 'IPv4基于地址池优先级分配地址算法'
          type: string
          enum:
          - Disable
          - Enable
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: Disable
        IPV6ALLOCPRIALG:
          name: 'IPv6基于地址池优先级分配地址算法'
          type: string
          enum:
          - Disable
          - Enable
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
    add_addrupgroup_list:
      type: items
      properties:
        UPFGRPNAME:
          name: 'UPF组名称'
          type: string
          minLength: 1
          maxLength: 32
          required: true
          description: '配置静态地址用户使用的UPF组。'
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
          description: '已通过**ADD ADDRUPGROUP**配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        UPFID:
          name: 'UPF实例标识'
          type: string
          minLength: 0
          maxLength: 255
          required: true
          description: '已通过**ADD UPNODE**配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        PRIORITY:
          name: '优先级'
          type: integer
          minimum: 0
          maximum: 255
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: 255
    add_poolgrpmap_list:
      type: items
      properties:
        MAPPINGNAME:
          name: '映射名称'
          type: string
          required: false
          description: '已通过**ADD ADDRPOOLGRP**配置。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        POOLGRPNAME:
          name: '地址池组名称'
          type: string
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        UPFGRPNAME:
          name: 'UPF组名称'
          type: string
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        LOCATIONGRPTYPE:
          name: 'LOCATIONGRPTYPE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_apn_list_2:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '-'
          data_source: '全网规划'
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
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        HASVPNIPV6:
          name: '绑定IPv6 VPN'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: DISABLE
        VPNINSTANCEIPV6:
          name: 'IPv6 VPN实例名'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        PSEUDOACTSWITCH:
          name: '支持假激活用户开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          - INHERIT
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: INHERIT
        RESTORPGWSWITCH:
          name: '故障重启业务恢复功能PGW开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          - INHERIT
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: INHERIT
        APPLAYERVOLUME:
          name: '仅统计应用层流量'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
        HEADENGRAYLIST:
          name: '头增强灰名单'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
    set_apnsglpass_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '配置APN单通检测。参数“APN”已在**ADD APN**中定义。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        SWITCH:
          name: '开关标识'
          type: string
          enum:
          - PF_ACT_DISABLE
          - PF_ACT_ENABLE
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_apnaddressattr_list_1:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          required: false
          description: '配置APN地址分配属性。参数“APN”已在**ADD APN**中定义。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        SUPPORTIPV4:
          name: '支持IPV4'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        SUPPORTIPV6:
          name: '支持IPV6'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        FRAMEDROUTE:
          name: '手机后路由'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        ANTISPOOFINGDL:
          name: '下行防欺诈'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        ANTISPOOFINGUL:
          name: '上行防欺诈'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPTYPEFORDUALIP:
          name: '为双栈用户返回的地址类型'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        SINGLEADDRCAUSE:
          name: '分配单栈地址时返回的原因值'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        CPCTRL:
          name: '基于CP分配IP地址'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPV6RAMTUSW:
          name: 'RA携带MTU选项开关'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPV6RALIFETIME:
          name: 'IPv6 RA消息路由生命周期'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        HOSTROUTEIP:
          name: '主机地址'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_pool_list:
      type: items
      properties:
        POOLNAME:
          name: '地址池名称'
          type: string
          minLength: 1
          maxLength: 79
          required: true
          description: '配置地址池。'
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
          data_source: '全网规划'
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
          data_source: '全网规划'
          pattern: ''
          default: IPV4
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
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
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
          default: DISABLE
    add_section_list_4:
      type: items
      properties:
        POOLNAME:
          name: '地址池名称'
          type: string
          minLength: 0
          maxLength: 79
          required: true
          description: '配置本地地址池里的地址段。'
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
        IPV6ALLOCPRIALG:
          name: 'IPV6基于地址池优先级分配地址算法'
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
          description: '配置绑定地址池到地址池组。   * 参数“POOLGROUPNAME”已在**ADD SECTION**中定义。 * 参数“POOLNAME”已在**ADD POOLGROUP**中定义。'
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
    add_poolgrpmap_list_2:
      type: items
      properties:
        MAPPINGNAME:
          name: '映射规则名称'
          type: string
          required: false
          description: '配置APN与地址池组映射关系。   * 参数“APN”已在**ADD APN**中定义。 * 参数“POOLGROUPNAME”已在**ADD POOLBINDGROUP**中定义。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        APN:
          name: 'APN名称'
          type: string
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        POOLGROUPNAME:
          name: '地址池组名称'
          type: string
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    set_apnipallocrule_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '配置地址分配规则。参数“APN”已在**ADD APN**中定义。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        ALLOCATTR:
          name: 'IPv4分配属性'
          type: string
          enum:
          - INHERIT
          - LOCAL
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        FIRSTRULESW:
          name: 'IPv4第一级规则开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        FIRSTRULE:
          name: 'IPv4第一级规则'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        SECONDRULESW:
          name: 'IPv4第二级规则开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        THIRDRULESW:
          name: 'IPv4第三级规则开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPV6ALLOCATTR:
          name: 'IPv6分配属性'
          type: string
          enum:
          - INHERIT
          - LOCAL
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPV6FIRSTRULESW:
          name: 'IPv6第一级规则开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPV6FIRSTRULE:
          name: 'IPv6第一级规则'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPV6SECRULESW:
          name: 'IPv6第二级规则开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPV6THIRDRULESW:
          name: 'IPv6第三级规则'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
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
    add_apn_list_3:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '-'
          data_source: '全网规划'
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
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        HASVPNIPV6:
          name: '绑定IPv6 VPN'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: DISABLE
        VPNINSTANCEIPV6:
          name: 'IPv6 VPN实例名'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        PSEUDOACTSWITCH:
          name: '支持假激活用户开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          - INHERIT
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: INHERIT
        RESTORPGWSWITCH:
          name: '故障重启业务恢复功能PGW开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          - INHERIT
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: INHERIT
        APPLAYERVOLUME:
          name: '仅统计应用层流量'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
        HEADENGRAYLIST:
          name: '头增强灰名单'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
    set_apnsglpass_list_1:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '配置APN单通检测。参数“APN”已在**ADD APN**中定义。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        SWITCH:
          name: '开关标识'
          type: string
          enum:
          - PF_ACT_DISABLE
          - PF_ACT_ENABLE
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_apnaddressattr_list_2:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          required: false
          description: '配置APN地址分配属性。参数“APN”已在**ADD APN**中定义。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        SUPPORTIPV4:
          name: '支持IPV4'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        SUPPORTIPV6:
          name: '支持IPV6'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        FRAMEDROUTE:
          name: '手机后路由'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        ANTISPOOFINGDL:
          name: '下行防欺诈'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        ANTISPOOFINGUL:
          name: '上行防欺诈'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPTYPEFORDUALIP:
          name: '为双栈用户返回的地址类型'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        SINGLEADDRCAUSE:
          name: '分配单栈地址时返回的原因值'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        CPCTRL:
          name: '基于CP分配IP地址'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPV6RAMTUSW:
          name: 'RA携带MTU选项开关'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPV6RALIFETIME:
          name: 'IPv6 RA消息路由生命周期'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        HOSTROUTEIP:
          name: '主机地址'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
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
          description: '配置地址池。'
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
          data_source: '全网规划'
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
          data_source: '全网规划'
          pattern: ''
          default: IPV4
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
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
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
          default: DISABLE
    add_section_list_6:
      type: items
      properties:
        POOLNAME:
          name: '地址池名称'
          type: string
          minLength: 0
          maxLength: 79
          required: true
          description: '配置本地地址池里的地址段。'
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
        IPV6ALLOCPRIALG:
          name: 'IPV6基于地址池优先级分配地址算法'
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
          description: '配置绑定地址池到地址池组。   * 参数“POOLGROUPNAME”已在**ADD SECTION**中定义。 * 参数“POOLNAME”已在**ADD POOLGROUP**中定义。'
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
    add_poolgrpmap_list_3:
      type: items
      properties:
        MAPPINGNAME:
          name: '映射规则名称'
          type: string
          required: false
          description: '配置APN与地址池组映射关系。   * 参数“APN”已在**ADD APN**中定义。 * 参数“POOLGROUPNAME”已在**ADD POOLBINDGROUP**中定义。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        APN:
          name: 'APN名称'
          type: string
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        POOLGROUPNAME:
          name: '地址池组名称'
          type: string
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    set_apnipallocrule_list_1:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '配置地址分配规则。参数“APN”已在**ADD APN**中定义。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        ALLOCATTR:
          name: 'IPv4分配属性'
          type: string
          enum:
          - INHERIT
          - LOCAL
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        FIRSTRULESW:
          name: 'IPv4第一级规则开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        FIRSTRULE:
          name: 'IPv4第一级规则'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        SECONDRULESW:
          name: 'IPv4第二级规则开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        THIRDRULESW:
          name: 'IPv4第三级规则开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPV6ALLOCATTR:
          name: 'IPv6分配属性'
          type: string
          enum:
          - INHERIT
          - LOCAL
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPV6FIRSTRULESW:
          name: 'IPv6第一级规则开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPV6FIRSTRULE:
          name: 'IPv6第一级规则'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPV6SECRULESW:
          name: 'IPv6第二级规则开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPV6THIRDRULESW:
          name: 'IPv6第三级规则'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '本端规划'
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
    add_apn_list_4:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '-'
          data_source: '全网规划'
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
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        HASVPNIPV6:
          name: '绑定IPv6 VPN'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: DISABLE
        VPNINSTANCEIPV6:
          name: 'IPv6 VPN实例名'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        PSEUDOACTSWITCH:
          name: '支持假激活用户开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          - INHERIT
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: INHERIT
        RESTORPGWSWITCH:
          name: '故障重启业务恢复功能PGW开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          - INHERIT
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: INHERIT
        APPLAYERVOLUME:
          name: '仅统计应用层流量'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
        HEADENGRAYLIST:
          name: '头增强灰名单'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
    set_apnsglpass_list_2:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '配置APN单通检测。参数“APN”已在**ADD APN**中定义。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        SWITCH:
          name: '开关标识'
          type: string
          enum:
          - PF_ACT_DISABLE
          - PF_ACT_ENABLE
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_apnaddressattr_list_3:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          required: false
          description: '配置APN地址分配属性。参数“APN”已在**ADD APN**中定义。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        SUPPORTIPV4:
          name: '支持IPV4'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        SUPPORTIPV6:
          name: '支持IPV6'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        FRAMEDROUTE:
          name: '手机后路由'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        ANTISPOOFINGDL:
          name: '下行防欺诈'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        ANTISPOOFINGUL:
          name: '上行防欺诈'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPTYPEFORDUALIP:
          name: '为双栈用户返回的地址类型'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        SINGLEADDRCAUSE:
          name: '分配单栈地址时返回的原因值'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        CPCTRL:
          name: '基于CP分配IP地址'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPV6RAMTUSW:
          name: 'RA携带MTU选项开关'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPV6RALIFETIME:
          name: 'IPv6 RA消息路由生命周期'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        HOSTROUTEIP:
          name: '主机地址'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_pool_list_4:
      type: items
      properties:
        POOLNAME:
          name: '地址池名称'
          type: string
          minLength: 1
          maxLength: 79
          required: true
          description: '配置地址池。'
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
          data_source: '全网规划'
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
          data_source: '全网规划'
          pattern: ''
          default: IPV4
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
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
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
          default: DISABLE
    add_section_list_8:
      type: items
      properties:
        POOLNAME:
          name: '地址池名称'
          type: string
          minLength: 0
          maxLength: 79
          required: true
          description: '配置本地地址池里的地址段。'
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
    add_poolgroup_list_2:
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
        IPV6ALLOCPRIALG:
          name: 'IPV6基于地址池优先级分配地址算法'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
    add_poolbindgroup_list_4:
      type: items
      properties:
        POOLGROUPNAME:
          name: '地址池组名称'
          type: string
          minLength: 0
          maxLength: 79
          required: true
          description: '配置绑定地址池到地址池组。   * 参数“POOLGROUPNAME”已在**ADD SECTION**中定义。 * 参数“POOLNAME”已在**ADD POOLGROUP**中定义。'
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
    add_poolgrpmap_list_4:
      type: items
      properties:
        MAPPINGNAME:
          name: '映射规则名称'
          type: string
          required: false
          description: '配置APN与地址池组映射关系。   * 参数“APN”已在**ADD APN**中定义。 * 参数“POOLGROUPNAME”已在**ADD POOLBINDGROUP**中定义。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        APN:
          name: 'APN名称'
          type: string
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        POOLGROUPNAME:
          name: '地址池组名称'
          type: string
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    set_apnipallocrule_list_2:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '配置地址分配规则。参数“APN”已在**ADD APN**中定义。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        ALLOCATTR:
          name: 'IPv4分配属性'
          type: string
          enum:
          - INHERIT
          - LOCAL
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        FIRSTRULESW:
          name: 'IPv4第一级规则开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        FIRSTRULE:
          name: 'IPv4第一级规则'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        SECONDRULESW:
          name: 'IPv4第二级规则开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        THIRDRULESW:
          name: 'IPv4第三级规则开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPV6ALLOCATTR:
          name: 'IPv6分配属性'
          type: string
          enum:
          - INHERIT
          - LOCAL
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPV6FIRSTRULESW:
          name: 'IPv6第一级规则开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPV6FIRSTRULE:
          name: 'IPv6第一级规则'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPV6SECRULESW:
          name: 'IPv6第二级规则开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPV6THIRDRULESW:
          name: 'IPv6第三级规则'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    mod_pool_list_4:
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
    add_apn_list_5:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '-'
          data_source: '全网规划'
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
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        HASVPNIPV6:
          name: '绑定IPv6 VPN'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: DISABLE
        VPNINSTANCEIPV6:
          name: 'IPv6 VPN实例名'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        PSEUDOACTSWITCH:
          name: '支持假激活用户开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          - INHERIT
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: INHERIT
        RESTORPGWSWITCH:
          name: '故障重启业务恢复功能PGW开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          - INHERIT
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: INHERIT
        APPLAYERVOLUME:
          name: '仅统计应用层流量'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
        HEADENGRAYLIST:
          name: '头增强灰名单'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
    set_apnsglpass_list_3:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '配置APN单通检测。参数“APN”已在**ADD APN**中定义。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        SWITCH:
          name: '开关标识'
          type: string
          enum:
          - PF_ACT_DISABLE
          - PF_ACT_ENABLE
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_apnaddressattr_list_4:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          required: false
          description: '配置APN地址分配属性。参数“APN”已在**ADD APN**中定义。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        SUPPORTIPV4:
          name: '支持IPV4'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        SUPPORTIPV6:
          name: '支持IPV6'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        FRAMEDROUTE:
          name: '手机后路由'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        ANTISPOOFINGDL:
          name: '下行防欺诈'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        ANTISPOOFINGUL:
          name: '上行防欺诈'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPTYPEFORDUALIP:
          name: '为双栈用户返回的地址类型'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        SINGLEADDRCAUSE:
          name: '分配单栈地址时返回的原因值'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        CPCTRL:
          name: '基于CP分配IP地址'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPV6RAMTUSW:
          name: 'RA携带MTU选项开关'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPV6RALIFETIME:
          name: 'IPv6 RA消息路由生命周期'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        HOSTROUTEIP:
          name: '主机地址'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_pool_list_6:
      type: items
      properties:
        POOLNAME:
          name: '地址池名称'
          type: string
          minLength: 1
          maxLength: 79
          required: true
          description: '配置地址池。'
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
          data_source: '全网规划'
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
          data_source: '全网规划'
          pattern: ''
          default: IPV4
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
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
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
          default: DISABLE
    add_section_list_10:
      type: items
      properties:
        POOLNAME:
          name: '地址池名称'
          type: string
          minLength: 0
          maxLength: 79
          required: true
          description: '配置本地地址池里的地址段。'
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
    add_poolgroup_list_3:
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
        IPV6ALLOCPRIALG:
          name: 'IPV6基于地址池优先级分配地址算法'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
    add_poolbindgroup_list_6:
      type: items
      properties:
        POOLGROUPNAME:
          name: '地址池组名称'
          type: string
          minLength: 0
          maxLength: 79
          required: true
          description: '配置绑定地址池到地址池组。   * 参数“POOLGROUPNAME”已在**ADD SECTION**中定义。 * 参数“POOLNAME”已在**ADD POOLGROUP**中定义。'
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
    add_poolgrpmap_list_5:
      type: items
      properties:
        MAPPINGNAME:
          name: '映射规则名称'
          type: string
          required: false
          description: '配置APN与地址池组映射关系。   * 参数“APN”已在**ADD APN**中定义。 * 参数“POOLGROUPNAME”已在**ADD POOLBINDGROUP**中定义。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        APN:
          name: 'APN名称'
          type: string
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        POOLGROUPNAME:
          name: '地址池组名称'
          type: string
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    set_apnipallocrule_list_3:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '配置地址分配规则。参数“APN”已在**ADD APN**中定义。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        ALLOCATTR:
          name: 'IPv4分配属性'
          type: string
          enum:
          - INHERIT
          - LOCAL
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        FIRSTRULESW:
          name: 'IPv4第一级规则开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        FIRSTRULE:
          name: 'IPv4第一级规则'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        SECONDRULESW:
          name: 'IPv4第二级规则开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        THIRDRULESW:
          name: 'IPv4第三级规则开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPV6ALLOCATTR:
          name: 'IPv6分配属性'
          type: string
          enum:
          - INHERIT
          - LOCAL
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPV6FIRSTRULESW:
          name: 'IPv6第一级规则开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPV6FIRSTRULE:
          name: 'IPv6第一级规则'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPV6SECRULESW:
          name: 'IPv6第二级规则开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPV6THIRDRULESW:
          name: 'IPv6第三级规则'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    mod_pool_list_6:
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
  examples:
    add_apn_list:
    - APN: 'APN1'
    add_nsdnn_list:
    - NSIDX: 0
      DNN: 'APN1'
    set_apnpccfunc_list:
    - APN: 'APN1'
      HOMEPCCSWITCH: DISABLE
      ROAMPCCSWITCH: DISABLE
      VISITPCCSWITCH: DISABLE
    add_apnusrprofg_list:
    - APN: 'APN1'
      USERPROFGNAME: 'up_group_cmcc_cmnet'
    set_apnaddressattr_list:
    - ALLOCWITHOUTPCO: ENABLE
      ANTISPOOFINGDI: ENABLE
      ANTISPOOFINGUI: ENABLE
      FRAMEDROUTE: DISABLE
      IGNORECONFLICT: ENABLE
      IPV4ALLOCTYPE: RADIUS
      IPV4RADIUSPRIOR: ENABLE
      IPV6ALLOCTYPE: RADIUS
      IPV6RADIUSPRIOR: ENABLE
      IPV6RAINTV: '14400'
      IPV6RAOFLAG: ENABLE
      RADIUSIPROUTE: ENABLE
      DHCPIPROUTE: ENABLE
      STATICIP: ENABLE
      STATICIPROUTE: ENABLE
      SUPPORTIPV4: ENABLE
      SUPPORTIPV6: ENABLE
      SUPPORTPRIOR: IPV4
      APN: APN1
      IPTYPEFORDUALIP: IPV4V6
      SINGLEADDRCAUSE: NETWORK_PREFER
      IPV4ALLOCPRIALG: DISABLE
      IPV6ALLOCPRIALG: DISABLE
      RDSSVRCTRL: ENABLE
      IPV6RAMTUSW: DISABLE
      IPV6MTU: '1800'
      IPV6RALIFETIME: '65535'
      IPV6RATIMES: '0'
    add_pnfprofile_list:
    - NFINSTANCEID: 'UPF_Instance_1'
      NFTYPE: NfUPF
      NFSTATUS: Registered
      FQDN: 'upf01.node'
      IPADDRESSTYPE: IPTypeV4
      IPV4ADDRESS1: '192.168.10.2'
      PORT: 8805
    add_pnfns_list:
    - INDEX: 1
      NFINSTANCEID: 'UPF_Instance_1'
      SST: 1
    add_pnfdnn_list:
    - INDEX: 1
      NFINSTANCEID: 'UPF_Instance_1'
      DNN: 'APN1'
      PNFNSINDEX: 1
      PRISWITCH: INHERIT
      CAPSWITCH: INHERIT
    add_upnode_list:
    - NFINSTANCENAME: 'UPF_Instance_1'
      LOCATION: Central
      UPFUNCTION: None
      LOCK: FALSE
      APSAMIGFUNC: DISABLE
      ADDRALLOCMODE: INHERIT
      SHAREDUPFSW: DISABLE
      VPNNAME: 'VRF_CP'
      SUPATSSS: Disable
      IPV6NDPLCY: PRIVATE
      IOSWITCH: DISABLE
      CAMPUSSW: DISABLE
      ULCLFWDTNLSW: DISABLE
      PDUESTWITHOUTN9: DISABLE
      NGLANSW: DISABLE
    add_uparea_list:
    - AREANAME: 'UPAREA1'
      AREATYPE: N2TAI
    add_upareabindn2tai_list:
    - AREANAME: 'UPAREA1'
      N2BEGINTAI: '46011000BB8'
      N2ENDTAI: '46011000BB8'
    add_pnfsmfserarea_list:
    - NFINSTANCEID: 'UPF_Instance_1'
      SMFSERVINGAREA: 'UPAREA1'
    add_addrpool_list:
    - POOLNAME: pool_ipv4_1
      IPVERSION: IPv4
      POOLTYPE: Radius
      CHECKIPVALID: Enable
      HASVPN: Disable
      VPNINSTANCE: VRF_VPN1
    add_section_list:
    - POOLNAME: 'pool_ipv4_1'
      SECTIONNUM: 1
      IPVERSION: IPv4
      V4STARTIP: '168.150.14.51'
      V4ENDIP: '168.150.14.60'
      V6PREFIXSTART: '2201:9:1:1:168:150:14:151'
      V6PREFIXEND: '2201:9:1:10:168:150:14:151'
      V6PREFIXLENGTH: 64
    add_poolbindapn_list:
    - POOLNAME: 'pool_ipv4_1'
      APN: 'APN1'
    add_addrpoolgrp_list:
    - POOLGRPNAME: 'pool_grp_1'
      POOLGRPTYPE: Radius
      IPV4ALLOCPRIALG: Disable
      IPV6ALLOCPRIALG: Disable
    add_poolbindgrp_list:
    - POOLGRPNAME: 'pool_grp_1'
      POOLNAME: 'pool_ipv4_1'
    add_addrupgroup_list:
    - UPFGRPNAME: 'upf_grp1'
      UPFGRPTYPE: Radius
    add_upfbindgrp_list:
    - UPFGRPNAME: 'upf_grp1'
      UPFID: 'UPF_Instance_1'
      PRIORITY: 10
    add_poolgrpmap_list:
    - MAPPINGNAME: mapping01
      POOLGRPNAME: pool_grp_1
      UPFGRPNAME: upf_grp1
      LOCATIONGRPTYPE: None
    add_apn_list_2:
    - APN: 'APN1'
      HASVPN: ENABLE
      VPNINSTANCE: 'DCI_VPN'
      HASVPNIPV6: ENABLE
      VPNINSTANCEIPV6: 'DCI_VPN'
      PSEUDOACTSWITCH: INHERIT
      RESTORPGWSWITCH: INHERIT
      APPLAYERVOLUME: DISABLE
      HEADENGRAYLIST: DISABLE
    set_apnsglpass_list:
    - APN: 'APN1'
      SWITCH: PF_ACT_ENABLE
    set_apnaddressattr_list_1:
    - APN: APN1
      SUPPORTIPV4: ENABLE
      SUPPORTIPV6: ENABLE
      FRAMEDROUTE: DISABLE
      ANTISPOOFINGDL: ENABLE
      ANTISPOOFINGUL: ENABLE
      IPTYPEFORDUALIP: IPV4V6
      SINGLEADDRCAUSE: '1'
      CPCTRL: DISABLE
      IPV6RAMTUSW: DISABLE
      IPV6RALIFETIME: '65535'
      HOSTROUTEIP: ENABLE
    add_pool_list:
    - POOLNAME: 'pool_ipv4_1'
      POOLTYPE: EXTERNAL
      IPVERSION: IPV4
      CHECKIPVALID: DISABLE
      HASVPN: ENABLE
      VPNINSTANCE: 'DCI_VPN'
      IMSSW: ENABLE
      REDUNDFUNC: DISABLE
    add_section_list_4:
    - POOLNAME: 'pool_ipv4_1'
      SECTIONNUM: 1
      IPVERSION: IPV4
      V4STARTIP: '168.150.14.51'
      V4ENDIP: '168.150.14.60'
      V6PREFIXSTART: '2201:9:1:1:168:150:14:151'
      V6PREFIXEND: '2201:9:1:10:168:150:14:151'
      V6PREFIXLENGTH: 64
    add_poolgroup_list:
    - POOLGRPNAME: 'pgrp_APN1'
      IPV4ALLOCPRIALG: ENABLE
      IPV6ALLOCPRIALG: ENABLE
    add_poolbindgroup_list:
    - POOLGROUPNAME: 'pgrp_APN1'
      POOLNAME: 'pool_ipv4_1'
    add_poolgrpmap_list_2:
    - MAPPINGNAME: mapping_APN1
      APN: APN1
      POOLGROUPNAME: pgrp_APN1
    set_apnipallocrule_list:
    - APN: 'APN1'
      ALLOCATTR: LOCAL
      FIRSTRULESW: ENABLE
      FIRSTRULE: APN-1&LOCATION-0&SMF-0
      SECONDRULESW: DISABLE
      THIRDRULESW: DISABLE
      IPV6ALLOCATTR: LOCAL
      IPV6FIRSTRULESW: ENABLE
      IPV6FIRSTRULE: APN-1&LOCATION-0&SMF-0
      IPV6SECRULESW: DISABLE
      IPV6THIRDRULESW: DISABLE
    mod_pool_list:
    - POOLNAME: 'pool_ipv4_1'
      POOLTYPE: EXTERNAL
      REDUNDFUNC: ENABLE
    add_apn_list_3:
    - APN: 'APN1'
      HASVPN: ENABLE
      VPNINSTANCE: 'DCI_VPN'
      HASVPNIPV6: ENABLE
      VPNINSTANCEIPV6: 'DCI_VPN'
      PSEUDOACTSWITCH: INHERIT
      RESTORPGWSWITCH: INHERIT
      APPLAYERVOLUME: DISABLE
      HEADENGRAYLIST: DISABLE
    set_apnsglpass_list_1:
    - APN: 'APN1'
      SWITCH: PF_ACT_ENABLE
    set_apnaddressattr_list_2:
    - APN: APN1
      SUPPORTIPV4: ENABLE
      SUPPORTIPV6: ENABLE
      FRAMEDROUTE: DISABLE
      ANTISPOOFINGDL: ENABLE
      ANTISPOOFINGUL: ENABLE
      IPTYPEFORDUALIP: IPV4V6
      SINGLEADDRCAUSE: '1'
      CPCTRL: DISABLE
      IPV6RAMTUSW: DISABLE
      IPV6RALIFETIME: '65535'
      HOSTROUTEIP: ENABLE
    add_pool_list_2:
    - POOLNAME: 'pool_ipv4_1'
      POOLTYPE: EXTERNAL
      IPVERSION: IPV4
      CHECKIPVALID: DISABLE
      HASVPN: ENABLE
      VPNINSTANCE: 'DCI_VPN'
      IMSSW: ENABLE
      REDUNDFUNC: DISABLE
    add_section_list_6:
    - POOLNAME: 'pool_ipv4_1'
      SECTIONNUM: 1
      IPVERSION: IPV4
      V4STARTIP: '171.151.16.25'
      V4ENDIP: '171.151.16.30'
      V6PREFIXSTART: '2218:9:1:1::'
      V6PREFIXEND: '2218:9:1:10::'
      V6PREFIXLENGTH: 64
    add_poolgroup_list_1:
    - POOLGRPNAME: 'pgrp_APN1'
      IPV4ALLOCPRIALG: ENABLE
      IPV6ALLOCPRIALG: ENABLE
    add_poolbindgroup_list_2:
    - POOLGROUPNAME: 'pgrp_APN1'
      POOLNAME: 'pool_ipv4_1'
    add_poolgrpmap_list_3:
    - MAPPINGNAME: mapping_APN1
      APN: APN1
      POOLGROUPNAME: pgrp_APN1
    set_apnipallocrule_list_1:
    - APN: 'APN1'
      ALLOCATTR: LOCAL
      FIRSTRULESW: ENABLE
      FIRSTRULE: APN-1&LOCATION-0&SMF-0
      SECONDRULESW: DISABLE
      THIRDRULESW: DISABLE
      IPV6ALLOCATTR: LOCAL
      IPV6FIRSTRULESW: ENABLE
      IPV6FIRSTRULE: APN-1&LOCATION-0&SMF-0
      IPV6SECRULESW: DISABLE
      IPV6THIRDRULESW: DISABLE
    mod_pool_list_2:
    - POOLNAME: 'pool_ipv4_1'
      POOLTYPE: EXTERNAL
      REDUNDFUNC: ENABLE
    add_apn_list_4:
    - APN: 'APN1'
      HASVPN: ENABLE
      VPNINSTANCE: 'DCI_VPN'
      HASVPNIPV6: ENABLE
      VPNINSTANCEIPV6: 'DCI_VPN'
      PSEUDOACTSWITCH: INHERIT
      RESTORPGWSWITCH: INHERIT
      APPLAYERVOLUME: DISABLE
      HEADENGRAYLIST: DISABLE
    set_apnsglpass_list_2:
    - APN: 'APN1'
      SWITCH: PF_ACT_ENABLE
    set_apnaddressattr_list_3:
    - APN: APN1
      SUPPORTIPV4: ENABLE
      SUPPORTIPV6: ENABLE
      FRAMEDROUTE: DISABLE
      ANTISPOOFINGDL: ENABLE
      ANTISPOOFINGUL: ENABLE
      IPTYPEFORDUALIP: IPV4V6
      SINGLEADDRCAUSE: '1'
      CPCTRL: DISABLE
      IPV6RAMTUSW: DISABLE
      IPV6RALIFETIME: '65535'
      HOSTROUTEIP: ENABLE
    add_pool_list_4:
    - POOLNAME: 'pool_ipv4_1'
      POOLTYPE: EXTERNAL
      IPVERSION: IPV4
      CHECKIPVALID: DISABLE
      HASVPN: ENABLE
      VPNINSTANCE: 'DCI_VPN'
      IMSSW: ENABLE
      REDUNDFUNC: DISABLE
    add_section_list_8:
    - POOLNAME: 'pool_ipv4_1'
      SECTIONNUM: 1
      IPVERSION: IPV4
      V4STARTIP: '168.150.14.51'
      V4ENDIP: '168.150.14.60'
      V6PREFIXSTART: '2201:9:1:1:168:150:14:151'
      V6PREFIXEND: '2201:9:1:10:168:150:14:151'
      V6PREFIXLENGTH: 64
    add_poolgroup_list_2:
    - POOLGRPNAME: 'pgrp_APN1'
      IPV4ALLOCPRIALG: ENABLE
      IPV6ALLOCPRIALG: ENABLE
    add_poolbindgroup_list_4:
    - POOLGROUPNAME: 'pgrp_APN1'
      POOLNAME: 'pool_ipv4_1'
    add_poolgrpmap_list_4:
    - MAPPINGNAME: mapping_APN1
      APN: APN1
      POOLGROUPNAME: pgrp_APN1
    set_apnipallocrule_list_2:
    - APN: 'APN1'
      ALLOCATTR: LOCAL
      FIRSTRULESW: ENABLE
      FIRSTRULE: APN-1&LOCATION-0&SMF-0
      SECONDRULESW: DISABLE
      THIRDRULESW: DISABLE
      IPV6ALLOCATTR: LOCAL
      IPV6FIRSTRULESW: ENABLE
      IPV6FIRSTRULE: APN-1&LOCATION-0&SMF-0
      IPV6SECRULESW: DISABLE
      IPV6THIRDRULESW: DISABLE
    mod_pool_list_4:
    - POOLNAME: 'pool_ipv4_1'
      POOLTYPE: EXTERNAL
      REDUNDFUNC: ENABLE
    add_apn_list_5:
    - APN: 'APN1'
      HASVPN: ENABLE
      VPNINSTANCE: 'DCI_VPN'
      HASVPNIPV6: ENABLE
      VPNINSTANCEIPV6: 'DCI_VPN'
      PSEUDOACTSWITCH: INHERIT
      RESTORPGWSWITCH: INHERIT
      APPLAYERVOLUME: DISABLE
      HEADENGRAYLIST: DISABLE
    set_apnsglpass_list_3:
    - APN: 'APN1'
      SWITCH: PF_ACT_ENABLE
    set_apnaddressattr_list_4:
    - APN: APN1
      SUPPORTIPV4: ENABLE
      SUPPORTIPV6: ENABLE
      FRAMEDROUTE: DISABLE
      ANTISPOOFINGDL: ENABLE
      ANTISPOOFINGUL: ENABLE
      IPTYPEFORDUALIP: IPV4V6
      SINGLEADDRCAUSE: '1'
      CPCTRL: DISABLE
      IPV6RAMTUSW: DISABLE
      IPV6RALIFETIME: '65535'
      HOSTROUTEIP: ENABLE
    add_pool_list_6:
    - POOLNAME: 'pool_ipv4_1'
      POOLTYPE: EXTERNAL
      IPVERSION: IPV4
      CHECKIPVALID: DISABLE
      HASVPN: ENABLE
      VPNINSTANCE: 'DCI_VPN'
      IMSSW: ENABLE
      REDUNDFUNC: DISABLE
    add_section_list_10:
    - POOLNAME: 'pool_ipv4_1'
      SECTIONNUM: 1
      IPVERSION: IPV4
      V4STARTIP: '171.151.16.25'
      V4ENDIP: '171.151.16.30'
      V6PREFIXSTART: '2218:9:1:1::'
      V6PREFIXEND: '2218:9:1:10::'
      V6PREFIXLENGTH: 64
    add_poolgroup_list_3:
    - POOLGRPNAME: 'pgrp_APN1'
      IPV4ALLOCPRIALG: ENABLE
      IPV6ALLOCPRIALG: ENABLE
    add_poolbindgroup_list_6:
    - POOLGROUPNAME: 'pgrp_APN1'
      POOLNAME: 'pool_ipv4_1'
    add_poolgrpmap_list_5:
    - MAPPINGNAME: mapping_APN1
      APN: APN1
      POOLGROUPNAME: pgrp_APN1
    set_apnipallocrule_list_3:
    - APN: 'APN1'
      ALLOCATTR: LOCAL
      FIRSTRULESW: ENABLE
      FIRSTRULE: APN-1&LOCATION-0&SMF-0
      SECONDRULESW: DISABLE
      THIRDRULESW: DISABLE
      IPV6ALLOCATTR: LOCAL
      IPV6FIRSTRULESW: ENABLE
      IPV6FIRSTRULE: APN-1&LOCATION-0&SMF-0
      IPV6SECRULESW: DISABLE
      IPV6THIRDRULESW: DISABLE
    mod_pool_list_6:
    - POOLNAME: 'pool_ipv4_1'
      POOLTYPE: EXTERNAL
      REDUNDFUNC: ENABLE
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 //SMF配置

```jinja2
{%- for item in add_apn_list -%}
    ADD APN:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_nsdnn_list -%}
    ADD NSDNN:
    {#- --- 必选参数 --- -#}
    NSIDX={{item.NSIDX}},
    DNN="{{item.DNN}}",
    ;
{%- endfor -%}
```

```jinja2
{%- for item in set_apnpccfunc_list -%}
    SET APNPCCFUNC:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    {#- --- 可选参数 --- -#}
    {%- if item.HOMEPCCSWITCH is not none -%}
        HOMEPCCSWITCH={{item.HOMEPCCSWITCH}},
    {%- endif -%}
    {%- if item.ROAMPCCSWITCH is not none -%}
        ROAMPCCSWITCH={{item.ROAMPCCSWITCH}},
    {%- endif -%}
    {%- if item.VISITPCCSWITCH is not none -%}
        VISITPCCSWITCH={{item.VISITPCCSWITCH}},
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_apnusrprofg_list -%}
    ADD APNUSRPROFG:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    USERPROFGNAME="{{item.USERPROFGNAME}}",
    ;
{%- endfor -%}
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_apnaddressattr_list的变量区（command: SET APNADDRESSATTR） -#}
<!-- MISSING_MACRO: command=SET APNADDRESSATTR list_name=set_apnaddressattr_list step_id=1 -->
```

```jinja2
{%- for item in add_pnfprofile_list -%}
    ADD PNFPROFILE:
    {#- --- 必选参数 --- -#}
    NFINSTANCEID="{{item.NFINSTANCEID}}",
    NFTYPE={{item.NFTYPE}},
    {#- --- 可选参数 --- -#}
    {%- if item.NFSTATUS is not none -%}
        NFSTATUS={{item.NFSTATUS}},
    {%- endif -%}
    {%- if item.IPADDRESSTYPE is not none -%}
        IPADDRESSTYPE={{item.IPADDRESSTYPE}},
    {%- endif -%}
    {%- if item.PORT is not none -%}
        PORT={{item.PORT}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPADDRESSTYPE=IPTypeV4/IPTypeV4V6 时必选 --- -#}
    {%- if item.IPADDRESSTYPE in ['IPTypeV4', 'IPTypeV4V6'] -%}
        IPV4ADDRESS1="{{item.IPV4ADDRESS1}}",
    {%- endif -%}
    {#- --- 条件必选/可选参数 --- -#}
    {#- --- 域名: 条件必选(NF类型=NfUPF) / 条件可选(NF类型=NfNRF|NfUDM|NfAMF|NfSMF|NfAUSF|NfNEF|NfPCF|NfSMSF|NfNSSF|NfUDR|NfLMF|NfGMLC|Nf5G_EIR|NfN3IWF|NfAF|NfUDSF|NfBSF|NfCHF|NfInvalid|NfSEPP|NfSCP) --- -#}
    {%- if (item.NFTYPE == 'NfUPF') -%}
        FQDN="{{item.FQDN}}",
    {%- elif (item.NFTYPE in ['NfNRF', 'NfUDM', 'NfAMF', 'NfSMF', 'NfAUSF', 'NfNEF', 'NfPCF', 'NfSMSF', 'NfNSSF', 'NfUDR', 'NfLMF', 'NfGMLC', 'Nf5G_EIR', 'NfN3IWF', 'NfAF', 'NfUDSF', 'NfBSF', 'NfCHF', 'NfInvalid', 'NfSEPP', 'NfSCP']) -%}
        {%- if item.FQDN is not none -%}
            FQDN="{{item.FQDN}}",
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_pnfns_list -%}
    ADD PNFNS:
    {#- --- 必选参数 --- -#}
    INDEX={{item.INDEX}},
    NFINSTANCEID="{{item.NFINSTANCEID}}",
    SST={{item.SST}},
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_pnfdnn_list -%}
    ADD PNFDNN:
    {#- --- 必选参数 --- -#}
    INDEX={{item.INDEX}},
    NFINSTANCEID="{{item.NFINSTANCEID}}",
    DNN="{{item.DNN}}",
    {#- --- 可选参数 --- -#}
    {%- if item.PNFNSINDEX is not none -%}
        PNFNSINDEX={{item.PNFNSINDEX}},
    {%- endif -%}
    {%- if item.PRISWITCH is not none -%}
        PRISWITCH={{item.PRISWITCH}},
    {%- endif -%}
    {%- if item.CAPSWITCH is not none -%}
        CAPSWITCH={{item.CAPSWITCH}},
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_upnode_list -%}
    ADD UPNODE:
    {#- --- 必选参数 --- -#}
    NFINSTANCENAME="{{item.NFINSTANCENAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.LOCATION is not none -%}
        LOCATION={{item.LOCATION}},
    {%- endif -%}
    {%- if item.UPFUNCTION is not none -%}
        UPFUNCTION={{item.UPFUNCTION}},
    {%- endif -%}
    {%- if item.LOCK is not none -%}
        LOCK={{item.LOCK}},
    {%- endif -%}
    {%- if item.APSAMIGFUNC is not none -%}
        APSAMIGFUNC={{item.APSAMIGFUNC}},
    {%- endif -%}
    {%- if item.ADDRALLOCMODE is not none -%}
        ADDRALLOCMODE={{item.ADDRALLOCMODE}},
    {%- endif -%}
    {%- if item.SHAREDUPFSW is not none -%}
        SHAREDUPFSW={{item.SHAREDUPFSW}},
    {%- endif -%}
    {%- if item.VPNNAME is not none -%}
        VPNNAME="{{item.VPNNAME}}",
    {%- endif -%}
    {%- if item.SUPATSSS is not none -%}
        SUPATSSS={{item.SUPATSSS}},
    {%- endif -%}
    {%- if item.IPV6NDPLCY is not none -%}
        IPV6NDPLCY={{item.IPV6NDPLCY}},
    {%- endif -%}
    {%- if item.IOSWITCH is not none -%}
        IOSWITCH={{item.IOSWITCH}},
    {%- endif -%}
    {%- if item.CAMPUSSW is not none -%}
        CAMPUSSW={{item.CAMPUSSW}},
    {%- endif -%}
    {%- if item.ULCLFWDTNLSW is not none -%}
        ULCLFWDTNLSW={{item.ULCLFWDTNLSW}},
    {%- endif -%}
    {%- if item.PDUESTWITHOUTN9 is not none -%}
        PDUESTWITHOUTN9={{item.PDUESTWITHOUTN9}},
    {%- endif -%}
    {%- if item.NGLANSW is not none -%}
        NGLANSW={{item.NGLANSW}},
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_uparea_list -%}
    ADD UPAREA:
    {#- --- 必选参数 --- -#}
    AREANAME="{{item.AREANAME}}",
    AREATYPE={{item.AREATYPE}},
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_upareabindn2tai_list -%}
    ADD UPAREABINDN2TAI:
    {#- --- 必选参数 --- -#}
    AREANAME="{{item.AREANAME}}",
    N2BEGINTAI="{{item.N2BEGINTAI}}",
    N2ENDTAI="{{item.N2ENDTAI}}",
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_pnfsmfserarea_list -%}
    ADD PNFSMFSERAREA:
    {#- --- 必选参数 --- -#}
    NFINSTANCEID="{{item.NFINSTANCEID}}",
    SMFSERVINGAREA="{{item.SMFSERVINGAREA}}",
    ;
{%- endfor -%}
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_addrpool_list的变量区（command: ADD ADDRPOOL） -#}
<!-- MISSING_MACRO: command=ADD ADDRPOOL list_name=add_addrpool_list step_id=1 -->
```

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
{%- for item in add_poolbindapn_list -%}
    ADD POOLBINDAPN:
    {#- --- 必选参数 --- -#}
    POOLNAME="{{item.POOLNAME}}",
    APN="{{item.APN}}",
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_addrpoolgrp_list -%}
    ADD ADDRPOOLGRP:
    {#- --- 必选参数 --- -#}
    POOLGRPNAME="{{item.POOLGRPNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.POOLGRPTYPE is not none -%}
        POOLGRPTYPE={{item.POOLGRPTYPE}},
    {%- endif -%}
    {%- if item.IPV4ALLOCPRIALG is not none -%}
        IPV4ALLOCPRIALG={{item.IPV4ALLOCPRIALG}},
    {%- endif -%}
    {%- if item.IPV6ALLOCPRIALG is not none -%}
        IPV6ALLOCPRIALG={{item.IPV6ALLOCPRIALG}},
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_poolbindgrp_list -%}
    ADD POOLBINDGRP:
    {#- --- 必选参数 --- -#}
    POOLGRPNAME="{{item.POOLGRPNAME}}",
    POOLNAME="{{item.POOLNAME}}",
    ;
{%- endfor -%}
```

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

```jinja2
{%- for item in add_upfbindgrp_list -%}
    ADD UPFBINDGRP:
    {#- --- 必选参数 --- -#}
    UPFGRPNAME="{{item.UPFGRPNAME}}",
    UPFID="{{item.UPFID}}",
    {#- --- 可选参数 --- -#}
    {%- if item.PRIORITY is not none -%}
        PRIORITY={{item.PRIORITY}},
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_poolgrpmap_list的变量区（command: ADD POOLGRPMAP） -#}
<!-- MISSING_MACRO: command=ADD POOLGRPMAP list_name=add_poolgrpmap_list step_id=1 -->
```

### 2 //UPF1配置

```jinja2
{%- for item in add_apn_list_2 -%}
    ADD APN:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    {#- --- 可选参数 --- -#}
    {%- if item.HASVPN is not none -%}
        HASVPN={{item.HASVPN}},
    {%- endif -%}
    {%- if item.HASVPNIPV6 is not none -%}
        HASVPNIPV6={{item.HASVPNIPV6}},
    {%- endif -%}
    {%- if item.PSEUDOACTSWITCH is not none -%}
        PSEUDOACTSWITCH={{item.PSEUDOACTSWITCH}},
    {%- endif -%}
    {%- if item.RESTORPGWSWITCH is not none -%}
        RESTORPGWSWITCH={{item.RESTORPGWSWITCH}},
    {%- endif -%}
    {%- if item.APPLAYERVOLUME is not none -%}
        APPLAYERVOLUME={{item.APPLAYERVOLUME}},
    {%- endif -%}
    {%- if item.HEADENGRAYLIST is not none -%}
        HEADENGRAYLIST={{item.HEADENGRAYLIST}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：HASVPN=ENABLE 时必选 --- -#}
    {%- if item.HASVPN == 'ENABLE' -%}
        VPNINSTANCE="{{item.VPNINSTANCE}}",
    {%- endif -%}
    {#- --- 条件必选：HASVPNIPV6=ENABLE 时必选 --- -#}
    {%- if item.HASVPNIPV6 == 'ENABLE' -%}
        VPNINSTANCEIPV6="{{item.VPNINSTANCEIPV6}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in set_apnsglpass_list -%}
    SET APNSGLPASS:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_apnaddressattr_list_1的变量区（command: SET APNADDRESSATTR） -#}
<!-- MISSING_MACRO: command=SET APNADDRESSATTR list_name=set_apnaddressattr_list_1 step_id=2 -->
```

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
    {#- --- 条件可选：POOLTYPE=EXTERNAL 时可选 --- -#}
    {%- if item.POOLTYPE == 'EXTERNAL' -%}
        {%- if item.CHECKIPVALID is not none -%}
            CHECKIPVALID={{item.CHECKIPVALID}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：POOLTYPE=LOCAL/EXTERNAL 时可选 --- -#}
    {%- if item.POOLTYPE in ['LOCAL', 'EXTERNAL'] -%}
        {%- if item.HASVPN is not none -%}
            HASVPN={{item.HASVPN}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：POOLTYPE=LOCAL/EXTERNAL 时可选 --- -#}
    {%- if item.POOLTYPE in ['LOCAL', 'EXTERNAL'] -%}
        {%- if item.IMSSW is not none -%}
            IMSSW={{item.IMSSW}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：POOLTYPE=EXTERNAL 时可选 --- -#}
    {%- if item.POOLTYPE == 'EXTERNAL' -%}
        {%- if item.REDUNDFUNC is not none -%}
            REDUNDFUNC={{item.REDUNDFUNC}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_section_list_4 -%}
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
{%- for item in add_poolgroup_list -%}
    ADD POOLGROUP:
    {#- --- 必选参数 --- -#}
    POOLGRPNAME="{{item.POOLGRPNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.IPV4ALLOCPRIALG is not none -%}
        IPV4ALLOCPRIALG={{item.IPV4ALLOCPRIALG}},
    {%- endif -%}
    {%- if item.IPV6ALLOCPRIALG is not none -%}
        IPV6ALLOCPRIALG={{item.IPV6ALLOCPRIALG}},
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_poolbindgroup_list -%}
    ADD POOLBINDGROUP:
    {#- --- 必选参数 --- -#}
    POOLGROUPNAME="{{item.POOLGROUPNAME}}",
    POOLNAME="{{item.POOLNAME}}",
    ;
{%- endfor -%}
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_poolgrpmap_list_2的变量区（command: ADD POOLGRPMAP） -#}
<!-- MISSING_MACRO: command=ADD POOLGRPMAP list_name=add_poolgrpmap_list_2 step_id=2 -->
```

```jinja2
{%- for item in set_apnipallocrule_list -%}
    SET APNIPALLOCRULE:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    {#- --- 可选参数 --- -#}
    {%- if item.ALLOCATTR is not none -%}
        ALLOCATTR={{item.ALLOCATTR}},
    {%- endif -%}
    {%- if item.IPV6ALLOCATTR is not none -%}
        IPV6ALLOCATTR={{item.IPV6ALLOCATTR}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：FIRSTRULESW=ENABLE 时必选 --- -#}
    {%- if item.FIRSTRULESW == 'ENABLE' -%}
        FIRSTRULE={{item.FIRSTRULE}},
    {%- endif -%}
    {#- --- 条件必选：IPV6FIRSTRULESW=ENABLE 时必选 --- -#}
    {%- if item.IPV6FIRSTRULESW == 'ENABLE' -%}
        IPV6FIRSTRULE={{item.IPV6FIRSTRULE}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：ALLOCATTR=LOCAL 时可选 --- -#}
    {%- if item.ALLOCATTR == 'LOCAL' -%}
        {%- if item.FIRSTRULESW is not none -%}
            FIRSTRULESW={{item.FIRSTRULESW}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：ALLOCATTR=LOCAL 时可选 --- -#}
    {%- if item.ALLOCATTR == 'LOCAL' -%}
        {%- if item.SECONDRULESW is not none -%}
            SECONDRULESW={{item.SECONDRULESW}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：ALLOCATTR=LOCAL 时可选 --- -#}
    {%- if item.ALLOCATTR == 'LOCAL' -%}
        {%- if item.THIRDRULESW is not none -%}
            THIRDRULESW={{item.THIRDRULESW}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：IPV6ALLOCATTR=LOCAL 时可选 --- -#}
    {%- if item.IPV6ALLOCATTR == 'LOCAL' -%}
        {%- if item.IPV6FIRSTRULESW is not none -%}
            IPV6FIRSTRULESW={{item.IPV6FIRSTRULESW}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：IPV6ALLOCATTR=LOCAL 时可选 --- -#}
    {%- if item.IPV6ALLOCATTR == 'LOCAL' -%}
        {%- if item.IPV6SECRULESW is not none -%}
            IPV6SECRULESW={{item.IPV6SECRULESW}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：IPV6ALLOCATTR=LOCAL 时可选 --- -#}
    {%- if item.IPV6ALLOCATTR == 'LOCAL' -%}
        {%- if item.IPV6THIRDRULESW is not none -%}
            IPV6THIRDRULESW={{item.IPV6THIRDRULESW}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
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
```

### 3 //UPF2配置

```jinja2
{%- for item in add_apn_list_3 -%}
    ADD APN:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    {#- --- 可选参数 --- -#}
    {%- if item.HASVPN is not none -%}
        HASVPN={{item.HASVPN}},
    {%- endif -%}
    {%- if item.HASVPNIPV6 is not none -%}
        HASVPNIPV6={{item.HASVPNIPV6}},
    {%- endif -%}
    {%- if item.PSEUDOACTSWITCH is not none -%}
        PSEUDOACTSWITCH={{item.PSEUDOACTSWITCH}},
    {%- endif -%}
    {%- if item.RESTORPGWSWITCH is not none -%}
        RESTORPGWSWITCH={{item.RESTORPGWSWITCH}},
    {%- endif -%}
    {%- if item.APPLAYERVOLUME is not none -%}
        APPLAYERVOLUME={{item.APPLAYERVOLUME}},
    {%- endif -%}
    {%- if item.HEADENGRAYLIST is not none -%}
        HEADENGRAYLIST={{item.HEADENGRAYLIST}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：HASVPN=ENABLE 时必选 --- -#}
    {%- if item.HASVPN == 'ENABLE' -%}
        VPNINSTANCE="{{item.VPNINSTANCE}}",
    {%- endif -%}
    {#- --- 条件必选：HASVPNIPV6=ENABLE 时必选 --- -#}
    {%- if item.HASVPNIPV6 == 'ENABLE' -%}
        VPNINSTANCEIPV6="{{item.VPNINSTANCEIPV6}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in set_apnsglpass_list_1 -%}
    SET APNSGLPASS:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_apnaddressattr_list_2的变量区（command: SET APNADDRESSATTR） -#}
<!-- MISSING_MACRO: command=SET APNADDRESSATTR list_name=set_apnaddressattr_list_2 step_id=3 -->
```

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
    {#- --- 条件可选：POOLTYPE=EXTERNAL 时可选 --- -#}
    {%- if item.POOLTYPE == 'EXTERNAL' -%}
        {%- if item.CHECKIPVALID is not none -%}
            CHECKIPVALID={{item.CHECKIPVALID}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：POOLTYPE=LOCAL/EXTERNAL 时可选 --- -#}
    {%- if item.POOLTYPE in ['LOCAL', 'EXTERNAL'] -%}
        {%- if item.HASVPN is not none -%}
            HASVPN={{item.HASVPN}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：POOLTYPE=LOCAL/EXTERNAL 时可选 --- -#}
    {%- if item.POOLTYPE in ['LOCAL', 'EXTERNAL'] -%}
        {%- if item.IMSSW is not none -%}
            IMSSW={{item.IMSSW}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：POOLTYPE=EXTERNAL 时可选 --- -#}
    {%- if item.POOLTYPE == 'EXTERNAL' -%}
        {%- if item.REDUNDFUNC is not none -%}
            REDUNDFUNC={{item.REDUNDFUNC}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_section_list_6 -%}
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
    {%- if item.IPV6ALLOCPRIALG is not none -%}
        IPV6ALLOCPRIALG={{item.IPV6ALLOCPRIALG}},
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
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_poolgrpmap_list_3的变量区（command: ADD POOLGRPMAP） -#}
<!-- MISSING_MACRO: command=ADD POOLGRPMAP list_name=add_poolgrpmap_list_3 step_id=3 -->
```

```jinja2
{%- for item in set_apnipallocrule_list_1 -%}
    SET APNIPALLOCRULE:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    {#- --- 可选参数 --- -#}
    {%- if item.ALLOCATTR is not none -%}
        ALLOCATTR={{item.ALLOCATTR}},
    {%- endif -%}
    {%- if item.IPV6ALLOCATTR is not none -%}
        IPV6ALLOCATTR={{item.IPV6ALLOCATTR}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：FIRSTRULESW=ENABLE 时必选 --- -#}
    {%- if item.FIRSTRULESW == 'ENABLE' -%}
        FIRSTRULE={{item.FIRSTRULE}},
    {%- endif -%}
    {#- --- 条件必选：IPV6FIRSTRULESW=ENABLE 时必选 --- -#}
    {%- if item.IPV6FIRSTRULESW == 'ENABLE' -%}
        IPV6FIRSTRULE={{item.IPV6FIRSTRULE}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：ALLOCATTR=LOCAL 时可选 --- -#}
    {%- if item.ALLOCATTR == 'LOCAL' -%}
        {%- if item.FIRSTRULESW is not none -%}
            FIRSTRULESW={{item.FIRSTRULESW}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：ALLOCATTR=LOCAL 时可选 --- -#}
    {%- if item.ALLOCATTR == 'LOCAL' -%}
        {%- if item.SECONDRULESW is not none -%}
            SECONDRULESW={{item.SECONDRULESW}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：ALLOCATTR=LOCAL 时可选 --- -#}
    {%- if item.ALLOCATTR == 'LOCAL' -%}
        {%- if item.THIRDRULESW is not none -%}
            THIRDRULESW={{item.THIRDRULESW}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：IPV6ALLOCATTR=LOCAL 时可选 --- -#}
    {%- if item.IPV6ALLOCATTR == 'LOCAL' -%}
        {%- if item.IPV6FIRSTRULESW is not none -%}
            IPV6FIRSTRULESW={{item.IPV6FIRSTRULESW}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：IPV6ALLOCATTR=LOCAL 时可选 --- -#}
    {%- if item.IPV6ALLOCATTR == 'LOCAL' -%}
        {%- if item.IPV6SECRULESW is not none -%}
            IPV6SECRULESW={{item.IPV6SECRULESW}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：IPV6ALLOCATTR=LOCAL 时可选 --- -#}
    {%- if item.IPV6ALLOCATTR == 'LOCAL' -%}
        {%- if item.IPV6THIRDRULESW is not none -%}
            IPV6THIRDRULESW={{item.IPV6THIRDRULESW}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
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
```

### 4 //UPF3配置

```jinja2
{%- for item in add_apn_list_4 -%}
    ADD APN:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    {#- --- 可选参数 --- -#}
    {%- if item.HASVPN is not none -%}
        HASVPN={{item.HASVPN}},
    {%- endif -%}
    {%- if item.HASVPNIPV6 is not none -%}
        HASVPNIPV6={{item.HASVPNIPV6}},
    {%- endif -%}
    {%- if item.PSEUDOACTSWITCH is not none -%}
        PSEUDOACTSWITCH={{item.PSEUDOACTSWITCH}},
    {%- endif -%}
    {%- if item.RESTORPGWSWITCH is not none -%}
        RESTORPGWSWITCH={{item.RESTORPGWSWITCH}},
    {%- endif -%}
    {%- if item.APPLAYERVOLUME is not none -%}
        APPLAYERVOLUME={{item.APPLAYERVOLUME}},
    {%- endif -%}
    {%- if item.HEADENGRAYLIST is not none -%}
        HEADENGRAYLIST={{item.HEADENGRAYLIST}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：HASVPN=ENABLE 时必选 --- -#}
    {%- if item.HASVPN == 'ENABLE' -%}
        VPNINSTANCE="{{item.VPNINSTANCE}}",
    {%- endif -%}
    {#- --- 条件必选：HASVPNIPV6=ENABLE 时必选 --- -#}
    {%- if item.HASVPNIPV6 == 'ENABLE' -%}
        VPNINSTANCEIPV6="{{item.VPNINSTANCEIPV6}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in set_apnsglpass_list_2 -%}
    SET APNSGLPASS:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_apnaddressattr_list_3的变量区（command: SET APNADDRESSATTR） -#}
<!-- MISSING_MACRO: command=SET APNADDRESSATTR list_name=set_apnaddressattr_list_3 step_id=4 -->
```

```jinja2
{%- for item in add_pool_list_4 -%}
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
    {#- --- 条件可选：POOLTYPE=EXTERNAL 时可选 --- -#}
    {%- if item.POOLTYPE == 'EXTERNAL' -%}
        {%- if item.CHECKIPVALID is not none -%}
            CHECKIPVALID={{item.CHECKIPVALID}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：POOLTYPE=LOCAL/EXTERNAL 时可选 --- -#}
    {%- if item.POOLTYPE in ['LOCAL', 'EXTERNAL'] -%}
        {%- if item.HASVPN is not none -%}
            HASVPN={{item.HASVPN}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：POOLTYPE=LOCAL/EXTERNAL 时可选 --- -#}
    {%- if item.POOLTYPE in ['LOCAL', 'EXTERNAL'] -%}
        {%- if item.IMSSW is not none -%}
            IMSSW={{item.IMSSW}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：POOLTYPE=EXTERNAL 时可选 --- -#}
    {%- if item.POOLTYPE == 'EXTERNAL' -%}
        {%- if item.REDUNDFUNC is not none -%}
            REDUNDFUNC={{item.REDUNDFUNC}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_section_list_8 -%}
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
{%- for item in add_poolgroup_list_2 -%}
    ADD POOLGROUP:
    {#- --- 必选参数 --- -#}
    POOLGRPNAME="{{item.POOLGRPNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.IPV4ALLOCPRIALG is not none -%}
        IPV4ALLOCPRIALG={{item.IPV4ALLOCPRIALG}},
    {%- endif -%}
    {%- if item.IPV6ALLOCPRIALG is not none -%}
        IPV6ALLOCPRIALG={{item.IPV6ALLOCPRIALG}},
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_poolbindgroup_list_4 -%}
    ADD POOLBINDGROUP:
    {#- --- 必选参数 --- -#}
    POOLGROUPNAME="{{item.POOLGROUPNAME}}",
    POOLNAME="{{item.POOLNAME}}",
    ;
{%- endfor -%}
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_poolgrpmap_list_4的变量区（command: ADD POOLGRPMAP） -#}
<!-- MISSING_MACRO: command=ADD POOLGRPMAP list_name=add_poolgrpmap_list_4 step_id=4 -->
```

```jinja2
{%- for item in set_apnipallocrule_list_2 -%}
    SET APNIPALLOCRULE:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    {#- --- 可选参数 --- -#}
    {%- if item.ALLOCATTR is not none -%}
        ALLOCATTR={{item.ALLOCATTR}},
    {%- endif -%}
    {%- if item.IPV6ALLOCATTR is not none -%}
        IPV6ALLOCATTR={{item.IPV6ALLOCATTR}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：FIRSTRULESW=ENABLE 时必选 --- -#}
    {%- if item.FIRSTRULESW == 'ENABLE' -%}
        FIRSTRULE={{item.FIRSTRULE}},
    {%- endif -%}
    {#- --- 条件必选：IPV6FIRSTRULESW=ENABLE 时必选 --- -#}
    {%- if item.IPV6FIRSTRULESW == 'ENABLE' -%}
        IPV6FIRSTRULE={{item.IPV6FIRSTRULE}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：ALLOCATTR=LOCAL 时可选 --- -#}
    {%- if item.ALLOCATTR == 'LOCAL' -%}
        {%- if item.FIRSTRULESW is not none -%}
            FIRSTRULESW={{item.FIRSTRULESW}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：ALLOCATTR=LOCAL 时可选 --- -#}
    {%- if item.ALLOCATTR == 'LOCAL' -%}
        {%- if item.SECONDRULESW is not none -%}
            SECONDRULESW={{item.SECONDRULESW}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：ALLOCATTR=LOCAL 时可选 --- -#}
    {%- if item.ALLOCATTR == 'LOCAL' -%}
        {%- if item.THIRDRULESW is not none -%}
            THIRDRULESW={{item.THIRDRULESW}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：IPV6ALLOCATTR=LOCAL 时可选 --- -#}
    {%- if item.IPV6ALLOCATTR == 'LOCAL' -%}
        {%- if item.IPV6FIRSTRULESW is not none -%}
            IPV6FIRSTRULESW={{item.IPV6FIRSTRULESW}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：IPV6ALLOCATTR=LOCAL 时可选 --- -#}
    {%- if item.IPV6ALLOCATTR == 'LOCAL' -%}
        {%- if item.IPV6SECRULESW is not none -%}
            IPV6SECRULESW={{item.IPV6SECRULESW}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：IPV6ALLOCATTR=LOCAL 时可选 --- -#}
    {%- if item.IPV6ALLOCATTR == 'LOCAL' -%}
        {%- if item.IPV6THIRDRULESW is not none -%}
            IPV6THIRDRULESW={{item.IPV6THIRDRULESW}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in mod_pool_list_4 -%}
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
```

### 5 //UPF4配置

```jinja2
{%- for item in add_apn_list_5 -%}
    ADD APN:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    {#- --- 可选参数 --- -#}
    {%- if item.HASVPN is not none -%}
        HASVPN={{item.HASVPN}},
    {%- endif -%}
    {%- if item.HASVPNIPV6 is not none -%}
        HASVPNIPV6={{item.HASVPNIPV6}},
    {%- endif -%}
    {%- if item.PSEUDOACTSWITCH is not none -%}
        PSEUDOACTSWITCH={{item.PSEUDOACTSWITCH}},
    {%- endif -%}
    {%- if item.RESTORPGWSWITCH is not none -%}
        RESTORPGWSWITCH={{item.RESTORPGWSWITCH}},
    {%- endif -%}
    {%- if item.APPLAYERVOLUME is not none -%}
        APPLAYERVOLUME={{item.APPLAYERVOLUME}},
    {%- endif -%}
    {%- if item.HEADENGRAYLIST is not none -%}
        HEADENGRAYLIST={{item.HEADENGRAYLIST}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：HASVPN=ENABLE 时必选 --- -#}
    {%- if item.HASVPN == 'ENABLE' -%}
        VPNINSTANCE="{{item.VPNINSTANCE}}",
    {%- endif -%}
    {#- --- 条件必选：HASVPNIPV6=ENABLE 时必选 --- -#}
    {%- if item.HASVPNIPV6 == 'ENABLE' -%}
        VPNINSTANCEIPV6="{{item.VPNINSTANCEIPV6}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in set_apnsglpass_list_3 -%}
    SET APNSGLPASS:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_apnaddressattr_list_4的变量区（command: SET APNADDRESSATTR） -#}
<!-- MISSING_MACRO: command=SET APNADDRESSATTR list_name=set_apnaddressattr_list_4 step_id=5 -->
```

```jinja2
{%- for item in add_pool_list_6 -%}
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
    {#- --- 条件可选：POOLTYPE=EXTERNAL 时可选 --- -#}
    {%- if item.POOLTYPE == 'EXTERNAL' -%}
        {%- if item.CHECKIPVALID is not none -%}
            CHECKIPVALID={{item.CHECKIPVALID}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：POOLTYPE=LOCAL/EXTERNAL 时可选 --- -#}
    {%- if item.POOLTYPE in ['LOCAL', 'EXTERNAL'] -%}
        {%- if item.HASVPN is not none -%}
            HASVPN={{item.HASVPN}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：POOLTYPE=LOCAL/EXTERNAL 时可选 --- -#}
    {%- if item.POOLTYPE in ['LOCAL', 'EXTERNAL'] -%}
        {%- if item.IMSSW is not none -%}
            IMSSW={{item.IMSSW}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：POOLTYPE=EXTERNAL 时可选 --- -#}
    {%- if item.POOLTYPE == 'EXTERNAL' -%}
        {%- if item.REDUNDFUNC is not none -%}
            REDUNDFUNC={{item.REDUNDFUNC}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_section_list_10 -%}
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
{%- for item in add_poolgroup_list_3 -%}
    ADD POOLGROUP:
    {#- --- 必选参数 --- -#}
    POOLGRPNAME="{{item.POOLGRPNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.IPV4ALLOCPRIALG is not none -%}
        IPV4ALLOCPRIALG={{item.IPV4ALLOCPRIALG}},
    {%- endif -%}
    {%- if item.IPV6ALLOCPRIALG is not none -%}
        IPV6ALLOCPRIALG={{item.IPV6ALLOCPRIALG}},
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_poolbindgroup_list_6 -%}
    ADD POOLBINDGROUP:
    {#- --- 必选参数 --- -#}
    POOLGROUPNAME="{{item.POOLGROUPNAME}}",
    POOLNAME="{{item.POOLNAME}}",
    ;
{%- endfor -%}
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_poolgrpmap_list_5的变量区（command: ADD POOLGRPMAP） -#}
<!-- MISSING_MACRO: command=ADD POOLGRPMAP list_name=add_poolgrpmap_list_5 step_id=5 -->
```

```jinja2
{%- for item in set_apnipallocrule_list_3 -%}
    SET APNIPALLOCRULE:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    {#- --- 可选参数 --- -#}
    {%- if item.ALLOCATTR is not none -%}
        ALLOCATTR={{item.ALLOCATTR}},
    {%- endif -%}
    {%- if item.IPV6ALLOCATTR is not none -%}
        IPV6ALLOCATTR={{item.IPV6ALLOCATTR}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：FIRSTRULESW=ENABLE 时必选 --- -#}
    {%- if item.FIRSTRULESW == 'ENABLE' -%}
        FIRSTRULE={{item.FIRSTRULE}},
    {%- endif -%}
    {#- --- 条件必选：IPV6FIRSTRULESW=ENABLE 时必选 --- -#}
    {%- if item.IPV6FIRSTRULESW == 'ENABLE' -%}
        IPV6FIRSTRULE={{item.IPV6FIRSTRULE}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：ALLOCATTR=LOCAL 时可选 --- -#}
    {%- if item.ALLOCATTR == 'LOCAL' -%}
        {%- if item.FIRSTRULESW is not none -%}
            FIRSTRULESW={{item.FIRSTRULESW}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：ALLOCATTR=LOCAL 时可选 --- -#}
    {%- if item.ALLOCATTR == 'LOCAL' -%}
        {%- if item.SECONDRULESW is not none -%}
            SECONDRULESW={{item.SECONDRULESW}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：ALLOCATTR=LOCAL 时可选 --- -#}
    {%- if item.ALLOCATTR == 'LOCAL' -%}
        {%- if item.THIRDRULESW is not none -%}
            THIRDRULESW={{item.THIRDRULESW}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：IPV6ALLOCATTR=LOCAL 时可选 --- -#}
    {%- if item.IPV6ALLOCATTR == 'LOCAL' -%}
        {%- if item.IPV6FIRSTRULESW is not none -%}
            IPV6FIRSTRULESW={{item.IPV6FIRSTRULESW}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：IPV6ALLOCATTR=LOCAL 时可选 --- -#}
    {%- if item.IPV6ALLOCATTR == 'LOCAL' -%}
        {%- if item.IPV6SECRULESW is not none -%}
            IPV6SECRULESW={{item.IPV6SECRULESW}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：IPV6ALLOCATTR=LOCAL 时可选 --- -#}
    {%- if item.IPV6ALLOCATTR == 'LOCAL' -%}
        {%- if item.IPV6THIRDRULESW is not none -%}
            IPV6THIRDRULESW={{item.IPV6THIRDRULESW}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in mod_pool_list_6 -%}
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
```


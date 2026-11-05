---
id: ''
name: 激活网元间HTR流控
ne_type: UNC
type: feature
description: 本操作指导介绍在运行网络中激活网元间HTR流控功能的操作过程。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","流控功能","WSFD-206009 网元间HTR流控","激活网元间HTR流控"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本操作指导介绍在运行网络中激活网元间HTR流控功能的操作过程。

## 必备事项
前提条件

请仔细阅读WSFD-206009 网元间HTR流控特性概述。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    set_licenseswitch_list:
      type: items
      properties:
        LICITEM:
          name: 'License项'
          type: string
          minLength: 0
          maxLength: 255
          required: true
          description: '开启HTR流控License项的配置开关。'
          data_source: '本端规划'
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
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_httphtrcfg_list:
      type: items
      properties:
        SWITCH:
          name: 'HTR流控开关'
          type: string
          enum:
          - ON
          - OFF
          required: false
          description: '（可选）设置HTR流控全局配置，开启HTR流控并配置流控相关参数。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        STARTTHD:
          name: '启控失败率阈值(%)'
          type: integer
          minimum: 0
          maximum: 100
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        STOPTHD:
          name: '解控失败率阈值(%)'
          type: integer
          minimum: 0
          maximum: 100
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        TARGETTHD:
          name: '目标失败率阈值(%)'
          type: integer
          minimum: 0
          maximum: 100
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        PERIOD:
          name: '统计周期(s)'
          type: integer
          minimum: 1
          maximum: 60
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        STARTTIMES:
          name: '启控周期数'
          type: integer
          minimum: 1
          maximum: 20
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        STOPTIMES:
          name: '解控周期数'
          type: integer
          minimum: 1
          maximum: 20
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        TIMEOUT:
          name: 'HTR超时时长(ms)'
          type: integer
          minimum: 10
          maximum: 5000
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        DECRATIO:
          name: '放通阈值减少比例(%)'
          type: integer
          minimum: 0
          maximum: 100
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        INCRATIO1:
          name: '放通阈值增加比例1(%)'
          type: integer
          minimum: 0
          maximum: 100
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        INCRATIO2:
          name: '放通阈值增加比例2(%)'
          type: integer
          minimum: 0
          maximum: 100
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_httphtrms_list:
      type: items
      properties:
        LOCALNFTYPE:
          name: '本端网元类型'
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
          - NFTypeNWDAF
          - NFTypePCSCF
          - NFTypeCBCF
          - NFTypeDRA
          - NFTypeMB_SMF
          - NFTypeUDN
          - NFTypeSFC
          - NFTypeUCBC
          - NFTypeCBE
          - NFTypeNEFEx
          - NFTypeSCF
          - NFTypeKMC
          required: true
          description: '（可选）配置HTR流控安全边界，流控期间的消息速率不会超出配置的安全边界。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        PEERNFTYPE:
          name: '对端网元类型'
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
          - NFTypeNWDAF
          - NFTypePCSCF
          - NFTypeCBCF
          - NFTypeDRA
          - NFTypeMB_SMF
          - NFTypeUDN
          - NFTypeSFC
          - NFTypeUCBC
          - NFTypeCBE
          - NFTypeNEFEx
          - NFTypeSCF
          - NFTypeKMC
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        MINTHD:
          name: '最小流控速率(个/秒)'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        MAXTHD:
          name: '最大流控速率(个/秒)'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_httpfcipgrp_list:
      type: items
      properties:
        INDEX:
          name: 'IP地址索引'
          type: integer
          minimum: 0
          maximum: 4095
          required: true
          description: '（可选）增加HTTP流控的IP地址组信息，当HTR流控的局向类型为基于IP组时，需要先配置该信息。  说明：  * 本端网元作为客户端的业务，选择对端网元的IP地址作为流控组的IP地址，如果是间接路由场景，选择下一跳（例如SCP）的IP地址作为流控组的IP地址；本端网元作为服务端的业务，选择本端网元配置的HTTPLE的服务端IP作为流控组的IP地址。 * 不论UDM和AUSF是否共IP或者是否使用多IP实例，同一台UDM(AUSF)的IP都配置到同一个IP组中。 * 此处IP地址仅用于举例，请根据网络实际情况配置IP组信息。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        GROUP:
          name: '流控组'
          type: integer
          minimum: 0
          maximum: 4095
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPTYPE:
          name: 'IP地址类型'
          type: string
          enum:
          - IPv4
          - IPv6
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV4ADDR:
          name: 'IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV4MASK:
          name: 'IPv4掩码'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV6ADDR:
          name: 'IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV6MASK:
          name: 'IPv6前缀'
          type: integer
          minimum: 1
          maximum: 128
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_httpofc_list:
      type: items
      properties:
        OFCIDX:
          name: '局向索引'
          type: integer
          minimum: 0
          maximum: 4095
          required: true
          description: '增加HTR流控生效的HTTP局向，局向类型为基于IP组。  说明：  此处仅以SMF到UDM的局向举例，请根据网络实际情况配置所有局向。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        OFCTYPE:
          name: '局向类型'
          type: string
          enum:
          - NFTYPE
          - IPGROUP
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPGROUP:
          name: 'IP组'
          type: integer
          minimum: 0
          maximum: 4095
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPGRPITEM:
          name: '基于IP组控制项'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        LOCALNFTYPE:
          name: '本端网元类型'
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
          - NFTypeNWDAF
          - NFTypePCSCF
          - NFTypeCBCF
          - NFTypeDRA
          - NFTypeMB_SMF
          - NFTypeUDN
          - NFTypeSFC
          - NFTypeUCBC
          - NFTypeCBE
          - NFTypeNEFEx
          - NFTypeSCF
          - NFTypeKMC
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        OFCNAME:
          name: '局向名称'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        PEERNFTYPE:
          name: '对端网元类型'
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
          - NFTypeNWDAF
          - NFTypePCSCF
          - NFTypeCBCF
          - NFTypeDRA
          - NFTypeMB_SMF
          - NFTypeUDN
          - NFTypeSFC
          - NFTypeUCBC
          - NFTypeCBE
          - NFTypeNEFEx
          - NFTypeSCF
          - NFTypeKMC
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        NFITEM:
          name: '基于NFTYPE控制项'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    set_ngmmproctrl_list:
      type: items
      properties:
        PROT:
          name: '流程类型'
          type: string
          enum:
          - AUSF_DISCOVERY
          - AIR
          - AUTHENTICATION
          - SMC
          - CHECK_IMEI
          - UDM_DISCOVERY
          - UDM_REGISTRATION
          - UDM_GET_SUBSCRIBER_DATA
          - UDM_SUBSCIBE
          - PCF_DISCOVERY
          - PCF_POLICY
          - OTHER_PROC
          - CAG
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        UDMSUBHTTPHTRFC:
          name: '获取UDM签约数据HTR流控拒绝原因值'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ACCRST:
          name: '接入限制拒绝原因值'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AIRAUTHREJECTED:
          name: 'AIR拒绝原因值(AUTHENTICATION_REJECTED)'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AIRCTXNOTFOUND:
          name: 'AIR拒绝原因值(CONTEXT_NOT_FOUND)'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AIRDISCERR:
          name: 'AIRSCP拒绝原因值(NF_DISCOVERY_ERROR)'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AIRDISCFAIL:
          name: 'AIR SCP拒绝原因值(NF_DISCOVERY_FAILURE)'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AIRINVALIDKEYID:
          name: 'AIR拒绝原因值(INVALID_HN_PUBLIC_KEY_IDENTIFIER)'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AIRINVALIDSCHME:
          name: 'AIR拒绝原因值(INVALID_SCHEME_OUTPUT)'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AIRSCPSEPP:
          name: 'AIR拒绝原因值(SCP/SEPP故障)'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AIRSERFAIL:
          name: 'AIR SCP拒绝原因值(NF_SERVICE_FAILOVER)'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AIRSERNETNOAUTH:
          name: 'AIR拒绝原因值(SERVING_NETWORK_NOT_AUTHORIZED)'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AIRSERVUNABLE:
          name: 'AIR拒绝原因值(Service Unavailable)'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AIRSUBNOTFOUND:
          name: 'AIR拒绝原因值(SUBSCRIPTION_NOT_FOUND)'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AIRTIMEOUT:
          name: 'AIR拒绝原因值(超时)'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AIRTOOMANY:
          name: 'AIR拒绝原因值(Too Many Requests)'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AIRUNSPTSCHEME:
          name: 'AIR拒绝原因值(UNSUPPORTED_PROTECTION_SCHEME)'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AIRUSERNOTFOUND:
          name: 'AIR拒绝原因值(USER_NOT_FOUND)'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AREARST:
          name: '区域限制拒绝原因值'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AUSFDISCFC:
          name: 'AUSF发现拒绝原因值(流控)'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AUSFDISCNOFOUND:
          name: 'AUSF发现拒绝原因值(Not Found)'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AUSFDISCOTHER:
          name: 'AUSF发现拒绝原因值(其他原因)'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AUTHHTTPHTRFC:
          name: 'AUTH HTR流控拒绝原因值'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AUTHHTTPOVLD:
          name: 'AUTH HTTP过载拒绝原因值'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AUTHMACFAIL:
          name: 'Authentication拒绝原因值(UE返回MAC Failure)'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AUTHRESCHKFAIL:
          name: 'Authentication拒绝原因值(RES检查失败)'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AUTHSYNCHFAIL:
          name: 'Authentication拒绝原因值(UE返回Synch Failure)'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CAGREJ:
          name: 'CAG拒绝原因值'
          type: integer
          minimum:
          - 0
          - 77
          maximum:
          - 75
          - 111
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CHKIMEICHKFAIL:
          name: 'Check IMEI拒绝原因值(IMEI检查失败)'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NSNOTAVL:
          name: '无可用网络切片拒绝原因值'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ODBREJCAUSE:
          name: 'ODB拒绝原因值'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        OTHPROCSCPSEPP:
          name: 'SCP/SEPP故障'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PCFDISCNOFOUND:
          name: 'PCF发现拒绝原因值(Not Found)'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PCFDISCOTHER:
          name: 'PCF发现拒绝原因值(其他原因)'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PCFPLCYNOFOUND:
          name: 'PCF策略拒绝原因值(RESOURCE_URI_STRUCTURE_NOT_FOUND)'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PCFPLCYOTHER:
          name: 'PCF策略拒绝原因值(其他原因)'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PCFPLCYSCPSEPP:
          name: 'PCF策略拒绝原因值(SCP/SEPP故障)'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ROAMRST:
          name: '漫游受限拒绝原因值'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SARST:
          name: '服务区域限制拒绝原因值'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SMCREJ:
          name: 'SMC拒绝原因值'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SMCTIMEOUT:
          name: 'SMC超时原因值'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SRVPLMNCHGREG:
          name: 'Serving Plmn变更注册拒绝原因值'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TANSNOTAVL:
          name: 'TA级网络切片不可用原因值'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        UDMDATADISCERR:
          name: 'UDM获取签约数据SCP拒绝原因值(NF_DISCOVERY_ERROR)'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        UDMDATADISCFAIL:
          name: 'UDM获取签约数据SCP拒绝原因值(NF_DISCOVERY_FAILURE)'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        UDMDATASCPSEPP:
          name: 'UDM获取签约数据拒绝原因值(SCP/SEPP故障)'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        UDMDATASERFAIL:
          name: 'UDM获取签约数据SCP拒绝原因值(NF_SERVICE_FAILOVER)'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        UDMDISCALWAYS:
          name: '强制发现UDM'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        UDMDISCNOFOUND:
          name: 'UDM发现拒绝原因值(Not Found)'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        UDMDISCOTHER:
          name: 'UDM发现拒绝原因值(其他原因)'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        UDMGETNOSUB:
          name: 'UDM获取签约数据拒绝原因值(SUBSCRIPTION_NOT_FOUND)'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        UDMGETSERVUNABL:
          name: 'UDM获取签约数据拒绝原因值(Service Unavailable)'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        UDMGETSUBNODATA:
          name: 'UDM获取签约数据拒绝原因值(DATA_NOT_FOUND)'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        UDMGETSUBNOUSR:
          name: 'UDM获取签约数据拒绝原因值(USER_NOT_FOUND)'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        UDMGETTIMEOUT:
          name: 'UDM获取签约数据拒绝原因值(超时)'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        UDMGETTOOMANY:
          name: 'UDM获取签约数据拒绝原因值(Too Many Requests)'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        UDMREGACCNOTAL:
          name: 'UDM注册拒绝原因值(ACCESS_NOT_ALLOWED)'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        UDMREGALWAYS:
          name: '强制向UDM注册'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        UDMREGCTXNOTFD:
          name: 'UDM注册拒绝原因值(CONTEXT_NOT_FOUND)'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        UDMREGDISCERR:
          name: 'UDM注册SCP拒绝原因值(NF_DISCOVERY_ERROR)'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        UDMREGDISCFAIL:
          name: 'UDM注册SCP拒绝原因值(NF_DISCOVERY_FAILURE)'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        UDMREGNOPSSUB:
          name: 'UDM注册拒绝原因值(NO_PS_SUBSCRIPTION)'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        UDMREGRATNOTAL:
          name: 'UDM注册拒绝原因值(RAT_NOT_ALLOWED)'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        UDMREGREAUTHREQ:
          name: 'UDM注册拒绝原因值(REAUTHENTICATION_REQUIRED)'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        UDMREGROAMNOTAL:
          name: 'UDM注册拒绝原因值(ROAMING_NOT_ALLOWED)'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        UDMREGSCPSEPP:
          name: 'UDM注册拒绝原因值(SCP/SEPP故障)'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        UDMREGSERFAIL:
          name: 'UDM注册SCP拒绝原因值(NF_SERVICE_FAILOVER)'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        UDMREGSERVUNABL:
          name: 'UDM注册拒绝原因值(Service Unavailable)'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        UDMREGTIMEOUT:
          name: 'UDM注册拒绝原因值(超时)'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        UDMREGTOOMANY:
          name: 'UDM注册拒绝原因值(Too Many Requests)'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        UDMREGUNKNOWSUB:
          name: 'UDM注册拒绝原因值(UNKNOWN_5GS_SUBSCRIPTION)'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        UDMREGUSRNOTFD:
          name: 'UDM注册拒绝原因值(USER_NOT_FOUND)'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        UDMSUBHTTPOVLD:
          name: '获取UDM签约数据HTTP过载拒绝原因值'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        UDMSUBNOUSR:
          name: 'UDM订阅拒绝原因值(USER_NOT_FOUND)'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        UDMSUBSCPSEPP:
          name: 'UDM订阅拒绝原因值(SCP/SEPP故障)'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        UDMSUBSERVUNABL:
          name: 'UDM订阅拒绝原因值(Service Unavailable)'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        UDMSUBTIMEOUT:
          name: 'UDM订阅拒绝原因值(超时)'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        UDMSUBTOOMANY:
          name: 'UDM订阅拒绝原因值(Too Many Requests)'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        UDMSUBUNSPT:
          name: 'UDM订阅拒绝原因值(UNSUPPORTED_RESOURCE_URI)'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        UEMSGCHECKFAIL:
          name: '终端消息非法拒绝原因值'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_smcausegrp_list:
      type: items
      properties:
        CAUSEGRPID:
          name: '原因值组标识'
          type: integer
          minimum: 1
          maximum: 127
          required: true
          description: '增加HTR流控场景失败原因值映射组配置。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        CAUSEGRPNM:
          name: '原因值组名称'
          type: string
          minLength: 0
          maxLength: 32
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: 'noname'
    add_smcausemap_list:
      type: items
      properties:
        CAUSEGRPID:
          name: '原因值组标识'
          type: integer
          minimum: 1
          maximum: 127
          required: true
          description: '向原因值映射组中增加原因值映射配置。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        CAUSERANGE:
          name: '原因值范围'
          type: string
          enum:
          - DEFAULT
          - SPECIAL
          - SPECIAL_APP_ERR
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        BGCAUSE:
          name: '起始原始原因值'
          type: integer
          minimum: 1
          maximum: 65535
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        EDCAUSE:
          name: '终止原始原因值'
          type: integer
          minimum: 1
          maximum: 65535
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        TCAUSE:
          name: '目标原因值'
          type: integer
          minimum: 1
          maximum: 65535
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        APPERROR:
          name: '应用层错误'
          type: integer
          minimum: 1
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_smfcausectrl_list:
      type: items
      properties:
        PROCEDURETYPE:
          name: '流程类型'
          type: string
          required: false
          description: '为PDU Session创建流程配置因HTR流控导致失败时的NAS原因值组。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        NFTYPE:
          name: '异常来源'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        CAUSEGROUPID:
          name: 'NF拒绝导致流程拒绝原因值组号'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_smcausegrp_list_2:
      type: items
      properties:
        CAUSEGRPID:
          name: '原因值组标识'
          type: integer
          minimum: 1
          maximum: 127
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        CAUSEGRPNM:
          name: '原因值组名称'
          type: string
          minLength: 0
          maxLength: 32
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: 'noname'
    add_smcausemap_list_2:
      type: items
      properties:
        CAUSEGRPID:
          name: '原因值组标识'
          type: integer
          minimum: 1
          maximum: 127
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        CAUSERANGE:
          name: '原因值范围'
          type: string
          enum:
          - DEFAULT
          - SPECIAL
          - SPECIAL_APP_ERR
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        BGCAUSE:
          name: '起始原始原因值'
          type: integer
          minimum: 1
          maximum: 65535
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        EDCAUSE:
          name: '终止原始原因值'
          type: integer
          minimum: 1
          maximum: 65535
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        TCAUSE:
          name: '目标原因值'
          type: integer
          minimum: 1
          maximum: 65535
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        APPERROR:
          name: '应用层错误'
          type: integer
          minimum: 1
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_smfcausectrl_list_2:
      type: items
      properties:
        PROCEDURETYPE:
          name: '流程类型'
          type: string
          required: false
          description: '为PDU Session创建流程配置因HTR流控导致失败时的NAS原因值组。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        NFTYPE:
          name: '异常来源'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        CAUSEGROUPID:
          name: 'NF拒绝导致流程拒绝原因值组号'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_smcausegrp_list_3:
      type: items
      properties:
        CAUSEGRPID:
          name: '原因值组标识'
          type: integer
          minimum: 1
          maximum: 127
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        CAUSEGRPNM:
          name: '原因值组名称'
          type: string
          minLength: 0
          maxLength: 32
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: 'noname'
    add_smcausemap_list_3:
      type: items
      properties:
        CAUSEGRPID:
          name: '原因值组标识'
          type: integer
          minimum: 1
          maximum: 127
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        CAUSERANGE:
          name: '原因值范围'
          type: string
          enum:
          - DEFAULT
          - SPECIAL
          - SPECIAL_APP_ERR
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        BGCAUSE:
          name: '起始原始原因值'
          type: integer
          minimum: 1
          maximum: 65535
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        EDCAUSE:
          name: '终止原始原因值'
          type: integer
          minimum: 1
          maximum: 65535
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        TCAUSE:
          name: '目标原因值'
          type: integer
          minimum: 1
          maximum: 65535
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        APPERROR:
          name: '应用层错误'
          type: integer
          minimum: 1
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_spgwcausectrl_list:
      type: items
      properties:
        PROCEDURETYPE:
          name: '流程类型'
          type: string
          enum:
          - CRT_SES_PROC
          - MOD_BR_PROC
          required: true
          description: '为初始会话创建流程配置因HTR流控导致失败时的原因值。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        CAUSESOURCE:
          name: '异常来源'
          type: string
          enum:
          - UPF
          - POLICY_PCF
          - CHG_3GPP
          - POLICY_PCRF
          - RADIUS_AUTH
          - INNER
          - RADIUS_CHG
          - DIAMETER_AAA
          - CHF_3GPP
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        CAUSEREJGROUPID:
          name: '周边网元拒绝导致流程拒绝原因值组号'
          type: integer
          minimum: 0
          maximum: 127
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: 0
        CAUSEAPNLOCK:
          name: 'APN锁定或整机锁定导致流程拒绝的GTPv2原因值'
          type: string
          enum:
          - SRVNOTSUPPORTED
          - APNCONGESTION
          - NORESOURCESAVAILABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: SRVNOTSUPPORTED
        CAUSEBRLIMIT:
          name: '承载受限原因值'
          type: string
          enum:
          - NORESOURCESAVAILABLE
          - APNCONGESTION
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NORESOURCESAVAILABLE
        CAUSEEXPIRATION:
          name: '周边网元响应超时导致流程拒绝的原因值'
          type: integer
          minimum: 0
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 0
        CAUSEFC:
          name: '发送消息流控导致流程拒绝的GTPv2原因值'
          type: string
          enum:
          - USERAUTHFAILED
          - NORESOURCESAVAILABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: USERAUTHFAILED
        CAUSEIPOCCUPIED:
          name: 'IP地址耗尽导致流程拒绝的GTPv2原因值'
          type: string
          enum:
          - APNCONGESTION
          - ALLIPOCCUPIED
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ALLIPOCCUPIED
        CAUSESELFFC:
          name: 'CPU过载原因值'
          type: string
          enum:
          - NORESOURCESAVAILABLE
          - SRVNOTSUPPORTED
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NORESOURCESAVAILABLE
    add_smfcausectrl_list_3:
      type: items
      properties:
        PROCEDURETYPE:
          name: 'PROCEDURETYPE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CAUSESOURCE:
          name: 'CAUSESOURCE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CAUSEREJGROUPID:
          name: 'CAUSEREJGROUPID'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_smcausegrp_list_4:
      type: items
      properties:
        CAUSEGRPID:
          name: '原因值组标识'
          type: integer
          minimum: 1
          maximum: 127
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        CAUSEGRPNM:
          name: '原因值组名称'
          type: string
          minLength: 0
          maxLength: 32
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: 'noname'
    add_smcausemap_list_4:
      type: items
      properties:
        CAUSEGRPID:
          name: '原因值组标识'
          type: integer
          minimum: 1
          maximum: 127
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        CAUSERANGE:
          name: '原因值范围'
          type: string
          enum:
          - DEFAULT
          - SPECIAL
          - SPECIAL_APP_ERR
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        BGCAUSE:
          name: '起始原始原因值'
          type: integer
          minimum: 1
          maximum: 65535
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        EDCAUSE:
          name: '终止原始原因值'
          type: integer
          minimum: 1
          maximum: 65535
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        TCAUSE:
          name: '目标原因值'
          type: integer
          minimum: 1
          maximum: 65535
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        APPERROR:
          name: '应用层错误'
          type: integer
          minimum: 1
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_ggsncausectrl_list:
      type: items
      properties:
        PROCEDURETYPE:
          name: '流程类型'
          type: string
          enum:
          - CRT_PDP_PROC
          - UPD_PDP_PROC
          required: true
          description: '为创建PDP流程配置因HTR流控导致失败时的原因值。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        CAUSESOURCE:
          name: '异常来源'
          type: string
          enum:
          - UPF
          - POLICY_PCRF
          - CHG_3GPP
          - RADIUS_AUTH
          - INNER
          - RADIUS_CHG
          - POLICY_PCF
          - CHF_3GPP
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        CAUSEREJGROUPID:
          name: 'NE拒绝导致流程拒绝原因值组号'
          type: integer
          minimum: 0
          maximum: 127
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: 0
        CAUSEAPNLOCK:
          name: 'APN锁定或整机锁定导致流程拒绝的GTPv1原因值'
          type: string
          enum:
          - SRVNOTSUPPORTED
          - APNCONGESTION
          - NORESOURCESAVAILABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: SRVNOTSUPPORTED
        CAUSEBRLIMIT:
          name: '承载受限原因值'
          type: string
          enum:
          - NORESOURCESAVAILABLE
          - APNCONGESTION
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NORESOURCESAVAILABLE
        CAUSEEXPIRATION:
          name: '响应超时导致流程拒绝的GTPv1原因值'
          type: integer
          minimum: 0
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 0
        CAUSEFC:
          name: '发送消息流控导致流程拒绝的GTPv1原因值'
          type: string
          enum:
          - USERAUTHFAILED
          - NORESOURCESAVAILABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: USERAUTHFAILED
        CAUSEIPOCCUPIED:
          name: 'IP地址耗尽导致流程拒绝的GTPv1原因值'
          type: string
          enum:
          - APNCONGESTION
          - ALLIPOCCUPIED
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ALLIPOCCUPIED
        CAUSESELFFC:
          name: 'CPU过载原因值'
          type: string
          enum:
          - NORESOURCESAVAILABLE
          - SRVNOTSUPPORTED
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NORESOURCESAVAILABLE
    add_smfcausectrl_list_4:
      type: items
      properties:
        PROCEDURETYPE:
          name: 'PROCEDURETYPE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CAUSESOURCE:
          name: 'CAUSESOURCE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CAUSEREJGROUPID:
          name: 'CAUSEREJGROUPID'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV2SHFCUNC01'
      SWITCH: ENABLE
    set_httphtrcfg_list:
    - SWITCH: ON
      STARTTHD: 12
      STOPTHD: 1
      TARGETTHD: 6
      PERIOD: 3
      STARTTIMES: 4
      STOPTIMES: 8
      TIMEOUT: 2000
      DECRATIO: 10
      INCRATIO1: 5
      INCRATIO2: 18
    add_httphtrms_list:
    - LOCALNFTYPE: NFTypeAMF
      PEERNFTYPE: NFTypeUDM
      MINTHD: 210
      MAXTHD: 1500
    add_httpfcipgrp_list:
    - INDEX: 0
      GROUP: 0
      IPTYPE: IPv4
      IPV4ADDR: '192.168.1.1'
      IPV4MASK: '255.255.255.0'
      IPV6ADDR: '2001:0db8::1'
      IPV6MASK: 128
    add_httpofc_list:
    - OFCIDX: 1
      OFCTYPE: IPGROUP
      IPGROUP: 0
      IPGRPITEM: HTRIPGRP-1
      LOCALNFTYPE: NFTypeAMF
      OFCNAME: 'AMF2UDMIPHTR'
      PEERNFTYPE: NFTypeUDM
      NFITEM: HTRINTF-1&FIXSPDFCINTF-0
    set_ngmmproctrl_list:
    - PROT: UDM_GET_SUBSCRIBER_DATA
      UDMSUBHTTPHTRFC: 0
      ACCRST: ''
      AIRAUTHREJECTED: ''
      AIRCTXNOTFOUND: ''
      AIRDISCERR: ''
      AIRDISCFAIL: ''
      AIRINVALIDKEYID: ''
      AIRINVALIDSCHME: ''
      AIRSCPSEPP: ''
      AIRSERFAIL: ''
      AIRSERNETNOAUTH: ''
      AIRSERVUNABLE: ''
      AIRSUBNOTFOUND: ''
      AIRTIMEOUT: ''
      AIRTOOMANY: ''
      AIRUNSPTSCHEME: ''
      AIRUSERNOTFOUND: ''
      AREARST: ''
      AUSFDISCFC: ''
      AUSFDISCNOFOUND: ''
      AUSFDISCOTHER: ''
      AUTHHTTPHTRFC: ''
      AUTHHTTPOVLD: ''
      AUTHMACFAIL: ''
      AUTHRESCHKFAIL: ''
      AUTHSYNCHFAIL: ''
      CAGREJ: ''
      CHKIMEICHKFAIL: ''
      NSNOTAVL: ''
      ODBREJCAUSE: ''
      OTHPROCSCPSEPP: ''
      PCFDISCNOFOUND: ''
      PCFDISCOTHER: ''
      PCFPLCYNOFOUND: ''
      PCFPLCYOTHER: ''
      PCFPLCYSCPSEPP: ''
      ROAMRST: ''
      SARST: ''
      SMCREJ: ''
      SMCTIMEOUT: ''
      SRVPLMNCHGREG: ''
      TANSNOTAVL: ''
      UDMDATADISCERR: ''
      UDMDATADISCFAIL: ''
      UDMDATASCPSEPP: ''
      UDMDATASERFAIL: ''
      UDMDISCALWAYS: ''
      UDMDISCNOFOUND: ''
      UDMDISCOTHER: ''
      UDMGETNOSUB: ''
      UDMGETSERVUNABL: ''
      UDMGETSUBNODATA: ''
      UDMGETSUBNOUSR: ''
      UDMGETTIMEOUT: ''
      UDMGETTOOMANY: ''
      UDMREGACCNOTAL: ''
      UDMREGALWAYS: ''
      UDMREGCTXNOTFD: ''
      UDMREGDISCERR: ''
      UDMREGDISCFAIL: ''
      UDMREGNOPSSUB: ''
      UDMREGRATNOTAL: ''
      UDMREGREAUTHREQ: ''
      UDMREGROAMNOTAL: ''
      UDMREGSCPSEPP: ''
      UDMREGSERFAIL: ''
      UDMREGSERVUNABL: ''
      UDMREGTIMEOUT: ''
      UDMREGTOOMANY: ''
      UDMREGUNKNOWSUB: ''
      UDMREGUSRNOTFD: ''
      UDMSUBHTTPOVLD: ''
      UDMSUBNOUSR: ''
      UDMSUBSCPSEPP: ''
      UDMSUBSERVUNABL: ''
      UDMSUBTIMEOUT: ''
      UDMSUBTOOMANY: ''
      UDMSUBUNSPT: ''
      UEMSGCHECKFAIL: ''
    add_smcausegrp_list:
    - CAUSEGRPID: 1
      CAUSEGRPNM: 'HTR_UDM'
    add_smcausemap_list:
    - CAUSEGRPID: 1
      CAUSERANGE: SPECIAL
      BGCAUSE: 608
      EDCAUSE: 608
      TCAUSE: 31
      APPERROR: ''
    add_smfcausectrl_list:
    - PROCEDURETYPE: PDU_SESSION_EST_PROC
      NFTYPE: UDM
      CAUSEGROUPID: '1'
    add_smcausegrp_list_2:
    - CAUSEGRPID: 2
      CAUSEGRPNM: 'HTR_PCFNAS'
    add_smcausemap_list_2:
    - CAUSEGRPID: 2
      CAUSERANGE: SPECIAL
      BGCAUSE: 608
      EDCAUSE: 608
      TCAUSE: 38
      APPERROR: ''
    add_smfcausectrl_list_2:
    - PROCEDURETYPE: PDU_SESSION_EST_PROC
      NFTYPE: POLICY_PCF
      CAUSEGROUPID: '2'
    add_smcausegrp_list_3:
    - CAUSEGRPID: 3
      CAUSEGRPNM: 'HTR_PCFGTPV2'
    add_smcausemap_list_3:
    - CAUSEGRPID: 3
      CAUSERANGE: SPECIAL
      BGCAUSE: 608
      EDCAUSE: 608
      TCAUSE: 92
      APPERROR: ''
    add_spgwcausectrl_list:
    - PROCEDURETYPE: CRT_SES_PROC
      CAUSESOURCE: POLICY_PCF
      CAUSEREJGROUPID: 3
      CAUSEAPNLOCK: SRVNOTSUPPORTED
      CAUSEBRLIMIT: NORESOURCESAVAILABLE
      CAUSEEXPIRATION: ''
      CAUSEFC: USERAUTHFAILED
      CAUSEIPOCCUPIED: ALLIPOCCUPIED
      CAUSESELFFC: NORESOURCESAVAILABLE
    add_smfcausectrl_list_3:
    - PROCEDURETYPE: CRT_SES_PROC
      CAUSESOURCE: POLICY_PCF
      CAUSEREJGROUPID: '3'
    add_smcausegrp_list_4:
    - CAUSEGRPID: 4
      CAUSEGRPNM: 'HTR_PCFGTPV1'
    add_smcausemap_list_4:
    - CAUSEGRPID: 4
      CAUSERANGE: SPECIAL
      BGCAUSE: 608
      EDCAUSE: 608
      TCAUSE: 209
      APPERROR: ''
    add_ggsncausectrl_list:
    - PROCEDURETYPE: CRT_PDP_PROC
      CAUSESOURCE: POLICY_PCF
      CAUSEREJGROUPID: 4
      CAUSEAPNLOCK: SRVNOTSUPPORTED
      CAUSEBRLIMIT: NORESOURCESAVAILABLE
      CAUSEEXPIRATION: ''
      CAUSEFC: USERAUTHFAILED
      CAUSEIPOCCUPIED: ALLIPOCCUPIED
      CAUSESELFFC: NORESOURCESAVAILABLE
    add_smfcausectrl_list_4:
    - PROCEDURETYPE: CRT_PDP_PROC
      CAUSESOURCE: POLICY_PCF
      CAUSEREJGROUPID: '4'
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 开启HTR流控License项的配置开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

### 2 **可选：**设置HTR流控全局配置。

```jinja2
{%- if is_optional_htr_global_config -%}
    {%- for item in set_httphtrcfg_list -%}
        SET HTTPHTRCFG:
        {#- --- 可选参数 --- -#}
        {%- if item.SWITCH is not none -%}
            SWITCH={{item.SWITCH}},
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：SWITCH=ON 时可选 --- -#}
        {%- if item.SWITCH == 'ON' -%}
            {%- if item.STARTTHD is not none -%}
                STARTTHD={{item.STARTTHD}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：SWITCH=ON 时可选 --- -#}
        {%- if item.SWITCH == 'ON' -%}
            {%- if item.STOPTHD is not none -%}
                STOPTHD={{item.STOPTHD}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：SWITCH=ON 时可选 --- -#}
        {%- if item.SWITCH == 'ON' -%}
            {%- if item.TARGETTHD is not none -%}
                TARGETTHD={{item.TARGETTHD}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：SWITCH=ON 时可选 --- -#}
        {%- if item.SWITCH == 'ON' -%}
            {%- if item.PERIOD is not none -%}
                PERIOD={{item.PERIOD}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：SWITCH=ON 时可选 --- -#}
        {%- if item.SWITCH == 'ON' -%}
            {%- if item.STARTTIMES is not none -%}
                STARTTIMES={{item.STARTTIMES}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：SWITCH=ON 时可选 --- -#}
        {%- if item.SWITCH == 'ON' -%}
            {%- if item.STOPTIMES is not none -%}
                STOPTIMES={{item.STOPTIMES}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：SWITCH=ON 时可选 --- -#}
        {%- if item.SWITCH == 'ON' -%}
            {%- if item.TIMEOUT is not none -%}
                TIMEOUT={{item.TIMEOUT}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：SWITCH=ON 时可选 --- -#}
        {%- if item.SWITCH == 'ON' -%}
            {%- if item.DECRATIO is not none -%}
                DECRATIO={{item.DECRATIO}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：SWITCH=ON 时可选 --- -#}
        {%- if item.SWITCH == 'ON' -%}
            {%- if item.INCRATIO1 is not none -%}
                INCRATIO1={{item.INCRATIO1}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：SWITCH=ON 时可选 --- -#}
        {%- if item.SWITCH == 'ON' -%}
            {%- if item.INCRATIO2 is not none -%}
                INCRATIO2={{item.INCRATIO2}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 3 **可选：**配置HTR流控安全边界。

```jinja2
{%- if is_optional_htr_security_boundary -%}
    {%- for item in add_httphtrms_list -%}
        ADD HTTPHTRMS:
        {#- --- 必选参数 --- -#}
        LOCALNFTYPE={{item.LOCALNFTYPE}},
        PEERNFTYPE={{item.PEERNFTYPE}},
        MINTHD={{item.MINTHD}},
        MAXTHD={{item.MAXTHD}},
        ;
    {%- endfor -%}
{%- endif -%}
```

### 4 **可选：**增加HTTP流控的IP地址组信息。

```jinja2
{%- if is_optional_http_fc_ip_group -%}
    {%- for item in add_httpfcipgrp_list -%}
        ADD HTTPFCIPGRP:
        {#- --- 必选参数 --- -#}
        INDEX={{item.INDEX}},
        GROUP={{item.GROUP}},
        IPTYPE={{item.IPTYPE}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：IPTYPE=IPv4 时必选 --- -#}
        {%- if item.IPTYPE == 'IPv4' -%}
            IPV4ADDR="{{item.IPV4ADDR}}",
        {%- endif -%}
        {#- --- 条件必选：IPTYPE=IPv4 时必选 --- -#}
        {%- if item.IPTYPE == 'IPv4' -%}
            IPV4MASK="{{item.IPV4MASK}}",
        {%- endif -%}
        {#- --- 条件必选：IPTYPE=IPv6 时必选 --- -#}
        {%- if item.IPTYPE == 'IPv6' -%}
            IPV6ADDR="{{item.IPV6ADDR}}",
        {%- endif -%}
        {#- --- 条件必选：IPTYPE=IPv6 时必选 --- -#}
        {%- if item.IPTYPE == 'IPv6' -%}
            IPV6MASK={{item.IPV6MASK}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 5 增加HTR流控生效的HTTP局向。

```jinja2
{%- for item in add_httpofc_list -%}
    ADD HTTPOFC:
    {#- --- 必选参数 --- -#}
    OFCIDX={{item.OFCIDX}},
    OFCTYPE={{item.OFCTYPE}},
    {#- --- 可选参数 --- -#}
    {%- if item.LOCALNFTYPE is not none -%}
        LOCALNFTYPE={{item.LOCALNFTYPE}},
    {%- endif -%}
    {%- if item.OFCNAME is not none -%}
        OFCNAME="{{item.OFCNAME}}",
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：OFCTYPE=IPGROUP 时必选 --- -#}
    {%- if item.OFCTYPE == 'IPGROUP' -%}
        IPGROUP={{item.IPGROUP}},
    {%- endif -%}
    {#- --- 条件必选：OFCTYPE=IPGROUP 时必选 --- -#}
    {%- if item.OFCTYPE == 'IPGROUP' -%}
        IPGRPITEM={{item.IPGRPITEM}},
    {%- endif -%}
    {#- --- 条件必选：OFCTYPE=NFTYPE 时必选 --- -#}
    {%- if item.OFCTYPE == 'NFTYPE' -%}
        PEERNFTYPE={{item.PEERNFTYPE}},
    {%- endif -%}
    {#- --- 条件必选：OFCTYPE=NFTYPE 时必选 --- -#}
    {%- if item.OFCTYPE == 'NFTYPE' -%}
        NFITEM={{item.NFITEM}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 6 **可选：**此步骤仅适用于AMF。配置由于HTR流控导致获取签约数据流程失败或者鉴权流程失败时，AMF发送给UE的拒绝原因值。

```jinja2
{%- if is_optional_amf_reject_cause -%}
    {%- for item in set_ngmmproctrl_list -%}
        SET NGMMPROCTRL:
        {#- --- 必选参数 --- -#}
        PROT={{item.PROT}},
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：PROT=UDM_GET_SUBSCRIBER_DATA 时可选 --- -#}
        {%- if item.PROT == 'UDM_GET_SUBSCRIBER_DATA' -%}
            {%- if item.UDMSUBHTTPHTRFC is not none -%}
                UDMSUBHTTPHTRFC={{item.UDMSUBHTTPHTRFC}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=OTHER_PROC 时可选 --- -#}
        {%- if item.PROT == 'OTHER_PROC' -%}
            {%- if item.ACCRST is not none -%}
                ACCRST={{item.ACCRST}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=AIR 时可选 --- -#}
        {%- if item.PROT == 'AIR' -%}
            {%- if item.AIRAUTHREJECTED is not none -%}
                AIRAUTHREJECTED={{item.AIRAUTHREJECTED}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=AIR 时可选 --- -#}
        {%- if item.PROT == 'AIR' -%}
            {%- if item.AIRCTXNOTFOUND is not none -%}
                AIRCTXNOTFOUND={{item.AIRCTXNOTFOUND}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=AIR 时可选 --- -#}
        {%- if item.PROT == 'AIR' -%}
            {%- if item.AIRDISCERR is not none -%}
                AIRDISCERR={{item.AIRDISCERR}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=AIR 时可选 --- -#}
        {%- if item.PROT == 'AIR' -%}
            {%- if item.AIRDISCFAIL is not none -%}
                AIRDISCFAIL={{item.AIRDISCFAIL}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=AIR 时可选 --- -#}
        {%- if item.PROT == 'AIR' -%}
            {%- if item.AIRINVALIDKEYID is not none -%}
                AIRINVALIDKEYID={{item.AIRINVALIDKEYID}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=AIR 时可选 --- -#}
        {%- if item.PROT == 'AIR' -%}
            {%- if item.AIRINVALIDSCHME is not none -%}
                AIRINVALIDSCHME={{item.AIRINVALIDSCHME}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=AIR 时可选 --- -#}
        {%- if item.PROT == 'AIR' -%}
            {%- if item.AIRSCPSEPP is not none -%}
                AIRSCPSEPP={{item.AIRSCPSEPP}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=AIR 时可选 --- -#}
        {%- if item.PROT == 'AIR' -%}
            {%- if item.AIRSERFAIL is not none -%}
                AIRSERFAIL={{item.AIRSERFAIL}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=AIR 时可选 --- -#}
        {%- if item.PROT == 'AIR' -%}
            {%- if item.AIRSERNETNOAUTH is not none -%}
                AIRSERNETNOAUTH={{item.AIRSERNETNOAUTH}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=AIR 时可选 --- -#}
        {%- if item.PROT == 'AIR' -%}
            {%- if item.AIRSERVUNABLE is not none -%}
                AIRSERVUNABLE={{item.AIRSERVUNABLE}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=AIR 时可选 --- -#}
        {%- if item.PROT == 'AIR' -%}
            {%- if item.AIRSUBNOTFOUND is not none -%}
                AIRSUBNOTFOUND={{item.AIRSUBNOTFOUND}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=AIR 时可选 --- -#}
        {%- if item.PROT == 'AIR' -%}
            {%- if item.AIRTIMEOUT is not none -%}
                AIRTIMEOUT={{item.AIRTIMEOUT}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=AIR 时可选 --- -#}
        {%- if item.PROT == 'AIR' -%}
            {%- if item.AIRTOOMANY is not none -%}
                AIRTOOMANY={{item.AIRTOOMANY}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=AIR 时可选 --- -#}
        {%- if item.PROT == 'AIR' -%}
            {%- if item.AIRUNSPTSCHEME is not none -%}
                AIRUNSPTSCHEME={{item.AIRUNSPTSCHEME}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=AIR 时可选 --- -#}
        {%- if item.PROT == 'AIR' -%}
            {%- if item.AIRUSERNOTFOUND is not none -%}
                AIRUSERNOTFOUND={{item.AIRUSERNOTFOUND}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=OTHER_PROC 时可选 --- -#}
        {%- if item.PROT == 'OTHER_PROC' -%}
            {%- if item.AREARST is not none -%}
                AREARST={{item.AREARST}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=AUSF_DISCOVERY 时可选 --- -#}
        {%- if item.PROT == 'AUSF_DISCOVERY' -%}
            {%- if item.AUSFDISCFC is not none -%}
                AUSFDISCFC={{item.AUSFDISCFC}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=AUSF_DISCOVERY 时可选 --- -#}
        {%- if item.PROT == 'AUSF_DISCOVERY' -%}
            {%- if item.AUSFDISCNOFOUND is not none -%}
                AUSFDISCNOFOUND={{item.AUSFDISCNOFOUND}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=AUSF_DISCOVERY 时可选 --- -#}
        {%- if item.PROT == 'AUSF_DISCOVERY' -%}
            {%- if item.AUSFDISCOTHER is not none -%}
                AUSFDISCOTHER={{item.AUSFDISCOTHER}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=AUTHENTICATION 时可选 --- -#}
        {%- if item.PROT == 'AUTHENTICATION' -%}
            {%- if item.AUTHHTTPHTRFC is not none -%}
                AUTHHTTPHTRFC={{item.AUTHHTTPHTRFC}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=AUTHENTICATION 时可选 --- -#}
        {%- if item.PROT == 'AUTHENTICATION' -%}
            {%- if item.AUTHHTTPOVLD is not none -%}
                AUTHHTTPOVLD={{item.AUTHHTTPOVLD}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=AUTHENTICATION 时可选 --- -#}
        {%- if item.PROT == 'AUTHENTICATION' -%}
            {%- if item.AUTHMACFAIL is not none -%}
                AUTHMACFAIL={{item.AUTHMACFAIL}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=AUTHENTICATION 时可选 --- -#}
        {%- if item.PROT == 'AUTHENTICATION' -%}
            {%- if item.AUTHRESCHKFAIL is not none -%}
                AUTHRESCHKFAIL={{item.AUTHRESCHKFAIL}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=AUTHENTICATION 时可选 --- -#}
        {%- if item.PROT == 'AUTHENTICATION' -%}
            {%- if item.AUTHSYNCHFAIL is not none -%}
                AUTHSYNCHFAIL={{item.AUTHSYNCHFAIL}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=CAG 时可选 --- -#}
        {%- if item.PROT == 'CAG' -%}
            {%- if item.CAGREJ is not none -%}
                CAGREJ={{item.CAGREJ}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=CHECK_IMEI 时可选 --- -#}
        {%- if item.PROT == 'CHECK_IMEI' -%}
            {%- if item.CHKIMEICHKFAIL is not none -%}
                CHKIMEICHKFAIL={{item.CHKIMEICHKFAIL}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=OTHER_PROC 时可选 --- -#}
        {%- if item.PROT == 'OTHER_PROC' -%}
            {%- if item.NSNOTAVL is not none -%}
                NSNOTAVL={{item.NSNOTAVL}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=OTHER_PROC 时可选 --- -#}
        {%- if item.PROT == 'OTHER_PROC' -%}
            {%- if item.ODBREJCAUSE is not none -%}
                ODBREJCAUSE={{item.ODBREJCAUSE}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=OTHER_PROC 时可选 --- -#}
        {%- if item.PROT == 'OTHER_PROC' -%}
            {%- if item.OTHPROCSCPSEPP is not none -%}
                OTHPROCSCPSEPP={{item.OTHPROCSCPSEPP}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=PCF_DISCOVERY 时可选 --- -#}
        {%- if item.PROT == 'PCF_DISCOVERY' -%}
            {%- if item.PCFDISCNOFOUND is not none -%}
                PCFDISCNOFOUND={{item.PCFDISCNOFOUND}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=PCF_DISCOVERY 时可选 --- -#}
        {%- if item.PROT == 'PCF_DISCOVERY' -%}
            {%- if item.PCFDISCOTHER is not none -%}
                PCFDISCOTHER={{item.PCFDISCOTHER}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=PCF_POLICY 时可选 --- -#}
        {%- if item.PROT == 'PCF_POLICY' -%}
            {%- if item.PCFPLCYNOFOUND is not none -%}
                PCFPLCYNOFOUND={{item.PCFPLCYNOFOUND}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=PCF_POLICY 时可选 --- -#}
        {%- if item.PROT == 'PCF_POLICY' -%}
            {%- if item.PCFPLCYOTHER is not none -%}
                PCFPLCYOTHER={{item.PCFPLCYOTHER}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=PCF_POLICY 时可选 --- -#}
        {%- if item.PROT == 'PCF_POLICY' -%}
            {%- if item.PCFPLCYSCPSEPP is not none -%}
                PCFPLCYSCPSEPP={{item.PCFPLCYSCPSEPP}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=OTHER_PROC 时可选 --- -#}
        {%- if item.PROT == 'OTHER_PROC' -%}
            {%- if item.ROAMRST is not none -%}
                ROAMRST={{item.ROAMRST}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=OTHER_PROC 时可选 --- -#}
        {%- if item.PROT == 'OTHER_PROC' -%}
            {%- if item.SARST is not none -%}
                SARST={{item.SARST}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=SMC 时可选 --- -#}
        {%- if item.PROT == 'SMC' -%}
            {%- if item.SMCREJ is not none -%}
                SMCREJ={{item.SMCREJ}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=SMC 时可选 --- -#}
        {%- if item.PROT == 'SMC' -%}
            {%- if item.SMCTIMEOUT is not none -%}
                SMCTIMEOUT={{item.SMCTIMEOUT}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=OTHER_PROC 时可选 --- -#}
        {%- if item.PROT == 'OTHER_PROC' -%}
            {%- if item.SRVPLMNCHGREG is not none -%}
                SRVPLMNCHGREG={{item.SRVPLMNCHGREG}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=OTHER_PROC 时可选 --- -#}
        {%- if item.PROT == 'OTHER_PROC' -%}
            {%- if item.TANSNOTAVL is not none -%}
                TANSNOTAVL={{item.TANSNOTAVL}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=UDM_GET_SUBSCRIBER_DATA 时可选 --- -#}
        {%- if item.PROT == 'UDM_GET_SUBSCRIBER_DATA' -%}
            {%- if item.UDMDATADISCERR is not none -%}
                UDMDATADISCERR={{item.UDMDATADISCERR}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=UDM_GET_SUBSCRIBER_DATA 时可选 --- -#}
        {%- if item.PROT == 'UDM_GET_SUBSCRIBER_DATA' -%}
            {%- if item.UDMDATADISCFAIL is not none -%}
                UDMDATADISCFAIL={{item.UDMDATADISCFAIL}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=UDM_GET_SUBSCRIBER_DATA 时可选 --- -#}
        {%- if item.PROT == 'UDM_GET_SUBSCRIBER_DATA' -%}
            {%- if item.UDMDATASCPSEPP is not none -%}
                UDMDATASCPSEPP={{item.UDMDATASCPSEPP}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=UDM_GET_SUBSCRIBER_DATA 时可选 --- -#}
        {%- if item.PROT == 'UDM_GET_SUBSCRIBER_DATA' -%}
            {%- if item.UDMDATASERFAIL is not none -%}
                UDMDATASERFAIL={{item.UDMDATASERFAIL}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=UDM_DISCOVERY 时可选 --- -#}
        {%- if item.PROT == 'UDM_DISCOVERY' -%}
            {%- if item.UDMDISCALWAYS is not none -%}
                UDMDISCALWAYS={{item.UDMDISCALWAYS}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=UDM_DISCOVERY 时可选 --- -#}
        {%- if item.PROT == 'UDM_DISCOVERY' -%}
            {%- if item.UDMDISCNOFOUND is not none -%}
                UDMDISCNOFOUND={{item.UDMDISCNOFOUND}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=UDM_DISCOVERY 时可选 --- -#}
        {%- if item.PROT == 'UDM_DISCOVERY' -%}
            {%- if item.UDMDISCOTHER is not none -%}
                UDMDISCOTHER={{item.UDMDISCOTHER}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=UDM_GET_SUBSCRIBER_DATA 时可选 --- -#}
        {%- if item.PROT == 'UDM_GET_SUBSCRIBER_DATA' -%}
            {%- if item.UDMGETNOSUB is not none -%}
                UDMGETNOSUB={{item.UDMGETNOSUB}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=UDM_GET_SUBSCRIBER_DATA 时可选 --- -#}
        {%- if item.PROT == 'UDM_GET_SUBSCRIBER_DATA' -%}
            {%- if item.UDMGETSERVUNABL is not none -%}
                UDMGETSERVUNABL={{item.UDMGETSERVUNABL}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=UDM_GET_SUBSCRIBER_DATA 时可选 --- -#}
        {%- if item.PROT == 'UDM_GET_SUBSCRIBER_DATA' -%}
            {%- if item.UDMGETSUBNODATA is not none -%}
                UDMGETSUBNODATA={{item.UDMGETSUBNODATA}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=UDM_GET_SUBSCRIBER_DATA 时可选 --- -#}
        {%- if item.PROT == 'UDM_GET_SUBSCRIBER_DATA' -%}
            {%- if item.UDMGETSUBNOUSR is not none -%}
                UDMGETSUBNOUSR={{item.UDMGETSUBNOUSR}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=UDM_GET_SUBSCRIBER_DATA 时可选 --- -#}
        {%- if item.PROT == 'UDM_GET_SUBSCRIBER_DATA' -%}
            {%- if item.UDMGETTIMEOUT is not none -%}
                UDMGETTIMEOUT={{item.UDMGETTIMEOUT}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=UDM_GET_SUBSCRIBER_DATA 时可选 --- -#}
        {%- if item.PROT == 'UDM_GET_SUBSCRIBER_DATA' -%}
            {%- if item.UDMGETTOOMANY is not none -%}
                UDMGETTOOMANY={{item.UDMGETTOOMANY}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=UDM_REGISTRATION 时可选 --- -#}
        {%- if item.PROT == 'UDM_REGISTRATION' -%}
            {%- if item.UDMREGACCNOTAL is not none -%}
                UDMREGACCNOTAL={{item.UDMREGACCNOTAL}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=UDM_REGISTRATION 时可选 --- -#}
        {%- if item.PROT == 'UDM_REGISTRATION' -%}
            {%- if item.UDMREGALWAYS is not none -%}
                UDMREGALWAYS={{item.UDMREGALWAYS}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=UDM_REGISTRATION 时可选 --- -#}
        {%- if item.PROT == 'UDM_REGISTRATION' -%}
            {%- if item.UDMREGCTXNOTFD is not none -%}
                UDMREGCTXNOTFD={{item.UDMREGCTXNOTFD}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=UDM_REGISTRATION 时可选 --- -#}
        {%- if item.PROT == 'UDM_REGISTRATION' -%}
            {%- if item.UDMREGDISCERR is not none -%}
                UDMREGDISCERR={{item.UDMREGDISCERR}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=UDM_REGISTRATION 时可选 --- -#}
        {%- if item.PROT == 'UDM_REGISTRATION' -%}
            {%- if item.UDMREGDISCFAIL is not none -%}
                UDMREGDISCFAIL={{item.UDMREGDISCFAIL}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=UDM_REGISTRATION 时可选 --- -#}
        {%- if item.PROT == 'UDM_REGISTRATION' -%}
            {%- if item.UDMREGNOPSSUB is not none -%}
                UDMREGNOPSSUB={{item.UDMREGNOPSSUB}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=UDM_REGISTRATION 时可选 --- -#}
        {%- if item.PROT == 'UDM_REGISTRATION' -%}
            {%- if item.UDMREGRATNOTAL is not none -%}
                UDMREGRATNOTAL={{item.UDMREGRATNOTAL}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=UDM_REGISTRATION 时可选 --- -#}
        {%- if item.PROT == 'UDM_REGISTRATION' -%}
            {%- if item.UDMREGREAUTHREQ is not none -%}
                UDMREGREAUTHREQ={{item.UDMREGREAUTHREQ}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=UDM_REGISTRATION 时可选 --- -#}
        {%- if item.PROT == 'UDM_REGISTRATION' -%}
            {%- if item.UDMREGROAMNOTAL is not none -%}
                UDMREGROAMNOTAL={{item.UDMREGROAMNOTAL}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=UDM_REGISTRATION 时可选 --- -#}
        {%- if item.PROT == 'UDM_REGISTRATION' -%}
            {%- if item.UDMREGSCPSEPP is not none -%}
                UDMREGSCPSEPP={{item.UDMREGSCPSEPP}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=UDM_REGISTRATION 时可选 --- -#}
        {%- if item.PROT == 'UDM_REGISTRATION' -%}
            {%- if item.UDMREGSERFAIL is not none -%}
                UDMREGSERFAIL={{item.UDMREGSERFAIL}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=UDM_REGISTRATION 时可选 --- -#}
        {%- if item.PROT == 'UDM_REGISTRATION' -%}
            {%- if item.UDMREGSERVUNABL is not none -%}
                UDMREGSERVUNABL={{item.UDMREGSERVUNABL}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=UDM_REGISTRATION 时可选 --- -#}
        {%- if item.PROT == 'UDM_REGISTRATION' -%}
            {%- if item.UDMREGTIMEOUT is not none -%}
                UDMREGTIMEOUT={{item.UDMREGTIMEOUT}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=UDM_REGISTRATION 时可选 --- -#}
        {%- if item.PROT == 'UDM_REGISTRATION' -%}
            {%- if item.UDMREGTOOMANY is not none -%}
                UDMREGTOOMANY={{item.UDMREGTOOMANY}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=UDM_REGISTRATION 时可选 --- -#}
        {%- if item.PROT == 'UDM_REGISTRATION' -%}
            {%- if item.UDMREGUNKNOWSUB is not none -%}
                UDMREGUNKNOWSUB={{item.UDMREGUNKNOWSUB}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=UDM_REGISTRATION 时可选 --- -#}
        {%- if item.PROT == 'UDM_REGISTRATION' -%}
            {%- if item.UDMREGUSRNOTFD is not none -%}
                UDMREGUSRNOTFD={{item.UDMREGUSRNOTFD}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=UDM_GET_SUBSCRIBER_DATA 时可选 --- -#}
        {%- if item.PROT == 'UDM_GET_SUBSCRIBER_DATA' -%}
            {%- if item.UDMSUBHTTPOVLD is not none -%}
                UDMSUBHTTPOVLD={{item.UDMSUBHTTPOVLD}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=UDM_SUBSCIBE 时可选 --- -#}
        {%- if item.PROT == 'UDM_SUBSCIBE' -%}
            {%- if item.UDMSUBNOUSR is not none -%}
                UDMSUBNOUSR={{item.UDMSUBNOUSR}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=UDM_SUBSCIBE 时可选 --- -#}
        {%- if item.PROT == 'UDM_SUBSCIBE' -%}
            {%- if item.UDMSUBSCPSEPP is not none -%}
                UDMSUBSCPSEPP={{item.UDMSUBSCPSEPP}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=UDM_SUBSCIBE 时可选 --- -#}
        {%- if item.PROT == 'UDM_SUBSCIBE' -%}
            {%- if item.UDMSUBSERVUNABL is not none -%}
                UDMSUBSERVUNABL={{item.UDMSUBSERVUNABL}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=UDM_SUBSCIBE 时可选 --- -#}
        {%- if item.PROT == 'UDM_SUBSCIBE' -%}
            {%- if item.UDMSUBTIMEOUT is not none -%}
                UDMSUBTIMEOUT={{item.UDMSUBTIMEOUT}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=UDM_SUBSCIBE 时可选 --- -#}
        {%- if item.PROT == 'UDM_SUBSCIBE' -%}
            {%- if item.UDMSUBTOOMANY is not none -%}
                UDMSUBTOOMANY={{item.UDMSUBTOOMANY}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=UDM_SUBSCIBE 时可选 --- -#}
        {%- if item.PROT == 'UDM_SUBSCIBE' -%}
            {%- if item.UDMSUBUNSPT is not none -%}
                UDMSUBUNSPT={{item.UDMSUBUNSPT}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=OTHER_PROC 时可选 --- -#}
        {%- if item.PROT == 'OTHER_PROC' -%}
            {%- if item.UEMSGCHECKFAIL is not none -%}
                UEMSGCHECKFAIL={{item.UEMSGCHECKFAIL}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 7 **可选：**此步骤仅适用于SMF。为PDU Session创建流程配置因HTR流控导致失败时的NAS原因值。

```jinja2
{%- if is_optional_pdu_session_nas_cause -%}
    {%- for item in add_smcausegrp_list -%}
        ADD SMCAUSEGRP:
        {#- --- 必选参数 --- -#}
        CAUSEGRPID={{item.CAUSEGRPID}},
        {#- --- 可选参数 --- -#}
        {%- if item.CAUSEGRPNM is not none -%}
            CAUSEGRPNM="{{item.CAUSEGRPNM}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_optional_pdu_session_nas_cause -%}
    {%- for item in add_smcausemap_list -%}
        ADD SMCAUSEMAP:
        {#- --- 必选参数 --- -#}
        CAUSEGRPID={{item.CAUSEGRPID}},
        CAUSERANGE={{item.CAUSERANGE}},
        TCAUSE={{item.TCAUSE}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：CAUSERANGE=SPECIAL/SPECIAL_APP_ERR 时必选 --- -#}
        {%- if item.CAUSERANGE in ['SPECIAL', 'SPECIAL_APP_ERR'] -%}
            BGCAUSE={{item.BGCAUSE}},
        {%- endif -%}
        {#- --- 条件必选：CAUSERANGE=SPECIAL_APP_ERR 时必选 --- -#}
        {%- if item.CAUSERANGE == 'SPECIAL_APP_ERR' -%}
            APPERROR={{item.APPERROR}},
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：CAUSERANGE=SPECIAL/SPECIAL_APP_ERR 时可选 --- -#}
        {%- if item.CAUSERANGE in ['SPECIAL', 'SPECIAL_APP_ERR'] -%}
            {%- if item.EDCAUSE is not none -%}
                EDCAUSE={{item.EDCAUSE}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_smfcausectrl_list的变量区（command: ADD SMFCAUSECTRL） -#}
<!-- MISSING_MACRO: command=ADD SMFCAUSECTRL list_name=add_smfcausectrl_list step_id=7 -->
```

```jinja2
{%- if is_optional_pdu_session_nas_cause -%}
    {%- for item in add_smcausegrp_list_2 -%}
        ADD SMCAUSEGRP:
        {#- --- 必选参数 --- -#}
        CAUSEGRPID={{item.CAUSEGRPID}},
        {#- --- 可选参数 --- -#}
        {%- if item.CAUSEGRPNM is not none -%}
            CAUSEGRPNM="{{item.CAUSEGRPNM}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_optional_pdu_session_nas_cause -%}
    {%- for item in add_smcausemap_list_2 -%}
        ADD SMCAUSEMAP:
        {#- --- 必选参数 --- -#}
        CAUSEGRPID={{item.CAUSEGRPID}},
        CAUSERANGE={{item.CAUSERANGE}},
        TCAUSE={{item.TCAUSE}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：CAUSERANGE=SPECIAL/SPECIAL_APP_ERR 时必选 --- -#}
        {%- if item.CAUSERANGE in ['SPECIAL', 'SPECIAL_APP_ERR'] -%}
            BGCAUSE={{item.BGCAUSE}},
        {%- endif -%}
        {#- --- 条件必选：CAUSERANGE=SPECIAL_APP_ERR 时必选 --- -#}
        {%- if item.CAUSERANGE == 'SPECIAL_APP_ERR' -%}
            APPERROR={{item.APPERROR}},
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：CAUSERANGE=SPECIAL/SPECIAL_APP_ERR 时可选 --- -#}
        {%- if item.CAUSERANGE in ['SPECIAL', 'SPECIAL_APP_ERR'] -%}
            {%- if item.EDCAUSE is not none -%}
                EDCAUSE={{item.EDCAUSE}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_smfcausectrl_list_2的变量区（command: ADD SMFCAUSECTRL） -#}
<!-- MISSING_MACRO: command=ADD SMFCAUSECTRL list_name=add_smfcausectrl_list_2 step_id=7 -->
```

### 8 **可选：**此步骤仅适用于SMF。为初始会话创建流程配置因HTR流控导致失败时的NAS原因值。

```jinja2
{%- if is_optional_initial_session_nas_cause -%}
    {%- for item in add_smcausegrp_list_3 -%}
        ADD SMCAUSEGRP:
        {#- --- 必选参数 --- -#}
        CAUSEGRPID={{item.CAUSEGRPID}},
        {#- --- 可选参数 --- -#}
        {%- if item.CAUSEGRPNM is not none -%}
            CAUSEGRPNM="{{item.CAUSEGRPNM}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_optional_initial_session_nas_cause -%}
    {%- for item in add_smcausemap_list_3 -%}
        ADD SMCAUSEMAP:
        {#- --- 必选参数 --- -#}
        CAUSEGRPID={{item.CAUSEGRPID}},
        CAUSERANGE={{item.CAUSERANGE}},
        TCAUSE={{item.TCAUSE}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：CAUSERANGE=SPECIAL/SPECIAL_APP_ERR 时必选 --- -#}
        {%- if item.CAUSERANGE in ['SPECIAL', 'SPECIAL_APP_ERR'] -%}
            BGCAUSE={{item.BGCAUSE}},
        {%- endif -%}
        {#- --- 条件必选：CAUSERANGE=SPECIAL_APP_ERR 时必选 --- -#}
        {%- if item.CAUSERANGE == 'SPECIAL_APP_ERR' -%}
            APPERROR={{item.APPERROR}},
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：CAUSERANGE=SPECIAL/SPECIAL_APP_ERR 时可选 --- -#}
        {%- if item.CAUSERANGE in ['SPECIAL', 'SPECIAL_APP_ERR'] -%}
            {%- if item.EDCAUSE is not none -%}
                EDCAUSE={{item.EDCAUSE}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_optional_initial_session_nas_cause -%}
    {%- for item in add_spgwcausectrl_list -%}
        ADD SPGWCAUSECTRL:
        {#- --- 必选参数 --- -#}
        CAUSESOURCE={{item.CAUSESOURCE}},
        PROCEDURETYPE={{item.PROCEDURETYPE}},
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：CAUSESOURCE=INNER 时可选 --- -#}
        {%- if item.CAUSESOURCE == 'INNER' -%}
            {%- if item.CAUSEAPNLOCK is not none -%}
                CAUSEAPNLOCK={{item.CAUSEAPNLOCK}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：CAUSESOURCE=INNER 时可选 --- -#}
        {%- if item.CAUSESOURCE == 'INNER' -%}
            {%- if item.CAUSEBRLIMIT is not none -%}
                CAUSEBRLIMIT={{item.CAUSEBRLIMIT}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：CAUSESOURCE=UPF/CHG_3GPP/RADIUS_AUTH/POLICY_PCF/POLICY_PCRF/RADIUS_CHG/DIAMETER_AAA/CHF_3GPP 时可选 --- -#}
        {%- if item.CAUSESOURCE in ['UPF', 'CHG_3GPP', 'RADIUS_AUTH', 'POLICY_PCF', 'POLICY_PCRF', 'RADIUS_CHG', 'DIAMETER_AAA', 'CHF_3GPP'] -%}
            {%- if item.CAUSEEXPIRATION is not none -%}
                CAUSEEXPIRATION={{item.CAUSEEXPIRATION}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：CAUSESOURCE=POLICY_PCF/POLICY_PCRF 时可选 --- -#}
        {%- if item.CAUSESOURCE in ['POLICY_PCF', 'POLICY_PCRF'] -%}
            {%- if item.CAUSEFC is not none -%}
                CAUSEFC={{item.CAUSEFC}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：CAUSESOURCE=INNER 时可选 --- -#}
        {%- if item.CAUSESOURCE == 'INNER' -%}
            {%- if item.CAUSEIPOCCUPIED is not none -%}
                CAUSEIPOCCUPIED={{item.CAUSEIPOCCUPIED}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：CAUSESOURCE=UPF/CHG_3GPP/RADIUS_AUTH/POLICY_PCF/POLICY_PCRF/RADIUS_CHG/DIAMETER_AAA/CHF_3GPP 时可选 --- -#}
        {%- if item.CAUSESOURCE in ['UPF', 'CHG_3GPP', 'RADIUS_AUTH', 'POLICY_PCF', 'POLICY_PCRF', 'RADIUS_CHG', 'DIAMETER_AAA', 'CHF_3GPP'] -%}
            {%- if item.CAUSEREJGROUPID is not none -%}
                CAUSEREJGROUPID={{item.CAUSEREJGROUPID}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：CAUSESOURCE=INNER 时可选 --- -#}
        {%- if item.CAUSESOURCE == 'INNER' -%}
            {%- if item.CAUSESELFFC is not none -%}
                CAUSESELFFC={{item.CAUSESELFFC}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_smfcausectrl_list_3的变量区（command: ADD SMFCAUSECTRL） -#}
<!-- MISSING_MACRO: command=ADD SMFCAUSECTRL list_name=add_smfcausectrl_list_3 step_id=8 -->
```

### 9 **可选：**此步骤仅适用于SMF。为创建PDP流程配置因HTR流控导致失败时的NAS原因值。

```jinja2
{%- if is_optional_pdp_nas_cause -%}
    {%- for item in add_smcausegrp_list_4 -%}
        ADD SMCAUSEGRP:
        {#- --- 必选参数 --- -#}
        CAUSEGRPID={{item.CAUSEGRPID}},
        {#- --- 可选参数 --- -#}
        {%- if item.CAUSEGRPNM is not none -%}
            CAUSEGRPNM="{{item.CAUSEGRPNM}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_optional_pdp_nas_cause -%}
    {%- for item in add_smcausemap_list_4 -%}
        ADD SMCAUSEMAP:
        {#- --- 必选参数 --- -#}
        CAUSEGRPID={{item.CAUSEGRPID}},
        CAUSERANGE={{item.CAUSERANGE}},
        TCAUSE={{item.TCAUSE}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：CAUSERANGE=SPECIAL/SPECIAL_APP_ERR 时必选 --- -#}
        {%- if item.CAUSERANGE in ['SPECIAL', 'SPECIAL_APP_ERR'] -%}
            BGCAUSE={{item.BGCAUSE}},
        {%- endif -%}
        {#- --- 条件必选：CAUSERANGE=SPECIAL_APP_ERR 时必选 --- -#}
        {%- if item.CAUSERANGE == 'SPECIAL_APP_ERR' -%}
            APPERROR={{item.APPERROR}},
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：CAUSERANGE=SPECIAL/SPECIAL_APP_ERR 时可选 --- -#}
        {%- if item.CAUSERANGE in ['SPECIAL', 'SPECIAL_APP_ERR'] -%}
            {%- if item.EDCAUSE is not none -%}
                EDCAUSE={{item.EDCAUSE}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_optional_pdp_nas_cause -%}
    {%- for item in add_ggsncausectrl_list -%}
        ADD GGSNCAUSECTRL:
        {#- --- 必选参数 --- -#}
        CAUSESOURCE={{item.CAUSESOURCE}},
        PROCEDURETYPE={{item.PROCEDURETYPE}},
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：CAUSESOURCE=INNER 时可选 --- -#}
        {%- if item.CAUSESOURCE == 'INNER' -%}
            {%- if item.CAUSEAPNLOCK is not none -%}
                CAUSEAPNLOCK={{item.CAUSEAPNLOCK}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：CAUSESOURCE=INNER 时可选 --- -#}
        {%- if item.CAUSESOURCE == 'INNER' -%}
            {%- if item.CAUSEBRLIMIT is not none -%}
                CAUSEBRLIMIT={{item.CAUSEBRLIMIT}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：CAUSESOURCE=UPF/CHG_3GPP/RADIUS_AUTH/POLICY_PCRF/RADIUS_CHG/POLICY_PCF/CHF_3GPP 时可选 --- -#}
        {%- if item.CAUSESOURCE in ['UPF', 'CHG_3GPP', 'RADIUS_AUTH', 'POLICY_PCRF', 'RADIUS_CHG', 'POLICY_PCF', 'CHF_3GPP'] -%}
            {%- if item.CAUSEEXPIRATION is not none -%}
                CAUSEEXPIRATION={{item.CAUSEEXPIRATION}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：CAUSESOURCE=POLICY_PCRF/POLICY_PCF 时可选 --- -#}
        {%- if item.CAUSESOURCE in ['POLICY_PCRF', 'POLICY_PCF'] -%}
            {%- if item.CAUSEFC is not none -%}
                CAUSEFC={{item.CAUSEFC}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：CAUSESOURCE=INNER 时可选 --- -#}
        {%- if item.CAUSESOURCE == 'INNER' -%}
            {%- if item.CAUSEIPOCCUPIED is not none -%}
                CAUSEIPOCCUPIED={{item.CAUSEIPOCCUPIED}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：CAUSESOURCE=UPF/CHG_3GPP/RADIUS_AUTH/POLICY_PCRF/RADIUS_CHG/POLICY_PCF/CHF_3GPP 时可选 --- -#}
        {%- if item.CAUSESOURCE in ['UPF', 'CHG_3GPP', 'RADIUS_AUTH', 'POLICY_PCRF', 'RADIUS_CHG', 'POLICY_PCF', 'CHF_3GPP'] -%}
            {%- if item.CAUSEREJGROUPID is not none -%}
                CAUSEREJGROUPID={{item.CAUSEREJGROUPID}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：CAUSESOURCE=INNER 时可选 --- -#}
        {%- if item.CAUSESOURCE == 'INNER' -%}
            {%- if item.CAUSESELFFC is not none -%}
                CAUSESELFFC={{item.CAUSESELFFC}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_smfcausectrl_list_4的变量区（command: ADD SMFCAUSECTRL） -#}
<!-- MISSING_MACRO: command=ADD SMFCAUSECTRL list_name=add_smfcausectrl_list_4 step_id=9 -->
```


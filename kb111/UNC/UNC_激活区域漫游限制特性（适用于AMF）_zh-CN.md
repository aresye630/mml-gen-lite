---
id: ''
name: 激活区域漫游限制特性（适用于AMF）
ne_type: UNC
type: feature
description: 本操作指导介绍在运行网络中激活区域漫游限制特性的操作过程。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","漫游管理功能","WSFD-105003 区域漫游限制","WSFD-105003 区域漫游限制（适用于AMF）","激活区域漫游限制特性（适用于AMF）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本操作指导介绍在运行网络中激活区域漫游限制特性的操作过程。

## 必备事项
前提条件

请仔细阅读WSFD-105003 区域漫游限制特性概述（适用于AMF）。
在进行区域漫游限制流程之前，必须先通过接入控制检查，如用户接入控制功能（适用于AMF）。
已完成加载License，对应的License项为“82206572 LKV2RRR02 区域漫游限制”。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    add_areacode_list:
      type: items
      properties:
        AREACODE:
          name: '区域编码'
          type: string
          minLength: 1
          maxLength: 128
          required: true
          description: '设置区域编码，唯一标识AMF服务的某个区域。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        DESC:
          name: '描述信息'
          type: string
          minLength: 0
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_areamem_list:
      type: items
      properties:
        AREACODE:
          name: '区域编码'
          type: string
          minLength: 1
          maxLength: 128
          required: true
          description: '一个区域由若干个跟踪区组成，该命令用于为指定的区域增加跟踪区成员。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        MCC:
          name: 'MCC'
          type: string
          minLength: 3
          maxLength: 3
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MNC:
          name: 'MNC'
          type: string
          minLength: 2
          maxLength: 3
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        BGNTAC:
          name: '跟踪区编码起始值'
          type: string
          minLength: 6
          maxLength: 6
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ENDTAC:
          name: '跟踪区编码结束值'
          type: string
          minLength: 6
          maxLength: 6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DESC:
          name: '描述信息'
          type: string
          minLength: 0
          maxLength: 32
          required: false
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
    set_ngmmfunc_list:
      type: items
      properties:
        AREARSTENSW:
          name: '区域漫游限制功能增强开关'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: '该参数用于表示AMF区域漫游限制功能增强开关。当开关打开时周期性注册更新、服务请求、切换流程中做区域接入限制检查。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    set_amfsoftparaofbit_list:
      type: items
      properties:
        DT:
          name: '数据类型'
          type: string
          enum:
          - Dw
          - Byte
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DWORDNUM:
          name: 'Dword索引'
          type: integer
          minimum: 1
          maximum: 1500
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VALUE:
          name: '软参记录值'
          type: string
          enum:
          - VALUE_0
          - VALUE_1
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        POSITION:
          name: '比特位'
          type: integer
          minimum: 1
          maximum: 32
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_areacode_list_1:
      type: items
      properties:
        AREACODE:
          name: '区域编码'
          type: string
          minLength: 1
          maxLength: 128
          required: true
          description: '设置区域编码，唯一标识AMF服务的某个区域。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        DESC:
          name: '描述信息'
          type: string
          minLength: 0
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_areamem_list_1:
      type: items
      properties:
        AREACODE:
          name: '区域编码'
          type: string
          minLength: 1
          maxLength: 128
          required: true
          description: '一个区域由若干个跟踪区组成，该命令用于为指定的区域增加跟踪区成员。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        MCC:
          name: 'MCC'
          type: string
          minLength: 3
          maxLength: 3
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MNC:
          name: 'MNC'
          type: string
          minLength: 2
          maxLength: 3
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        BGNTAC:
          name: '跟踪区编码起始值'
          type: string
          minLength: 6
          maxLength: 6
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ENDTAC:
          name: '跟踪区编码结束值'
          type: string
          minLength: 6
          maxLength: 6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DESC:
          name: '描述信息'
          type: string
          minLength: 0
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_ngusrgrp_list:
      type: items
      properties:
        USRGRPID:
          name: '用户群组标识'
          type: integer
          minimum: 0
          maximum: 4294967294
          required: true
          description: '设置5G用户群信息，同一个用户群中的用户具有相同的策略。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        DESC:
          name: '描述信息'
          type: string
          minLength: 0
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_ngusrgrpmem_list:
      type: items
      properties:
        USRGRPID:
          name: '用户群组标识'
          type: integer
          minimum: 0
          maximum: 4294967294
          required: true
          description: '该命令用于为5G用户群增加用户群成员。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        IMSIPRE:
          name: 'IMSI前缀'
          type: string
          minLength: 5
          maxLength: 15
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DESC:
          name: '描述信息'
          type: string
          minLength: 0
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_ngmmfunc_list_1:
      type: items
      properties:
        AREARSTENSW:
          name: '区域漫游限制功能增强开关'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: '该参数用于表示AMF区域漫游限制功能增强开关。当开关打开时周期性注册更新、服务请求、切换流程中做区域接入限制检查。'
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
          description: '由用户签约的“禁止区域（ForbiddenArea）”控制用户的接入，拒绝的原因值根据**SET NGMMPROCTRL**的整系统配置进行设置。'
          data_source: '全网规划'
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
    add_ngaccarealst_list:
      type: items
      properties:
        AREARANGE:
          name: '区域范围'
          type: string
          enum:
          - ALL_AREA
          - AREA_CODE
          required: true
          description: 'AMF本地配置限制区域信息、用户信息、控制模式以及拒绝原因值。  由AMF本地配置的接入限制区域控制用户的接入，拒绝原因值根据**ADD NGACCAREALST**的配置进行设置。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        AREACODE:
          name: '区域编码'
          type: string
          minLength: 1
          maxLength: 128
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CTRLMODE:
          name: '控制模式'
          type: string
          enum:
          - WHITELIST
          - BLACKLIST
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SUBRANGE:
          name: '用户范围'
          type: string
          enum:
          - ALL_USER
          - HOME_USER
          - FOREIGN_USER
          - USER_GROUP
          - SPECIAL_USER_RANGE
          - MSISDN_PREFIX
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SUBGRPID:
          name: '用户群组标识'
          type: integer
          minimum: 0
          maximum: 4294967294
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DESC:
          name: '描述信息'
          type: string
          minLength: 0
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        REJCAUSE:
          name: '拒绝原因值'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 15
        IMSIMODE:
          name: '添加IMSI的方式'
          type: string
          enum:
          - IMSI
          - IMSIRANGE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MSISDNPRE:
          name: 'MSISDN前缀'
          type: string
          minLength: 5
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    add_areacode_list:
    - AREACODE: 'MyTown'
      DESC: 'for mytown'
    add_areamem_list:
    - AREACODE: 'MyTown'
      MCC: '123'
      MNC: '456'
      BGNTAC: '010101'
      ENDTAC: '010102'
      DESC: 'areamember of mytown'
    set_licenseswitch_list:
    - LICITEM: 'LKV2RRR02'
      SWITCH: ENABLE
    set_ngmmfunc_list:
    - AREARSTENSW: ON
    set_amfsoftparaofbit_list:
    - DT: Dw
      DWORDNUM: 11
      VALUE: VALUE_1
      POSITION: 2
    add_areacode_list_1:
    - AREACODE: 'MyTown'
      DESC: 'for mytown'
    add_areamem_list_1:
    - AREACODE: 'MyTown'
      MCC: '123'
      MNC: '456'
      BGNTAC: '010101'
      ENDTAC: '010102'
      DESC: 'areamember of mytown'
    add_ngusrgrp_list:
    - USRGRPID: 888
      DESC: 'for usergroup'
    add_ngusrgrpmem_list:
    - USRGRPID: 888
      IMSIPRE: '123456'
      DESC: 'sometown'
    set_ngmmfunc_list_1:
    - AREARSTENSW: ON
    set_ngmmproctrl_list:
    - PROT: OTHER_PROC
      AREARST: 0
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
      UDMSUBHTTPHTRFC: ''
      UDMSUBHTTPOVLD: ''
      UDMSUBNOUSR: ''
      UDMSUBSCPSEPP: ''
      UDMSUBSERVUNABL: ''
      UDMSUBTIMEOUT: ''
      UDMSUBTOOMANY: ''
      UDMSUBUNSPT: ''
      UEMSGCHECKFAIL: ''
    add_ngaccarealst_list:
    - AREARANGE: AREA_CODE
      AREACODE: 'MyTown'
      CTRLMODE: WHITELIST
      SUBRANGE: USER_GROUP
      SUBGRPID: 888
      DESC: 'for employees'
      REJCAUSE: 15
      IMSIMODE: ''
      MSISDNPRE: ''
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 **根据用户接入和移动签约数据中的“禁止区域（Forbidden Area）”信息控制用户的接入。**

#### 1.1 进入“MML命令行-UNC”窗口。

#### 1.2 配置某个区域信息，以及AreaCode与TAI之间的映射关系。

##### 1.2.1 配置区域编码

```jinja2
{%- for item in add_areacode_list -%}
    ADD AREACODE:
    {#- --- 必选参数 --- -#}
    AREACODE="{{item.AREACODE}}",
    {#- --- 可选参数 --- -#}
    {%- if item.DESC is not none -%}
        DESC="{{item.DESC}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

##### 1.2.2 为指定的区域增加跟踪区成员

```jinja2
{%- for item in add_areamem_list -%}
    ADD AREAMEM:
    {#- --- 必选参数 --- -#}
    AREACODE="{{item.AREACODE}}",
    MCC="{{item.MCC}}",
    MNC="{{item.MNC}}",
    BGNTAC="{{item.BGNTAC}}",
    {#- --- 可选参数 --- -#}
    {%- if item.ENDTAC is not none -%}
        ENDTAC="{{item.ENDTAC}}",
    {%- endif -%}
    {%- if item.DESC is not none -%}
        DESC="{{item.DESC}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 2 **AMF针对指定的区域在本地配置用户接入的策略，然后基于策略控制用户的接入。**

#### 2.1 进入“MML命令行-UNC”窗口。

#### 2.2 开启本特性的功能控制开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

#### 2.3 开启区域漫游限制功能增强开关，将“AREARSTENSW”设置为“ON”。

```jinja2
{%- for item in set_ngmmfunc_list -%}
    SET NGMMFUNC:
    {#- --- 可选参数 --- -#}
    {%- if item.AREARSTENSW is not none -%}
        AREARSTENSW={{item.AREARSTENSW}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 2.4 需要限制用户在禁止区域内进行Xn切换以及周期性注册流程时，设置DWORD11中BIT2的取值为“1”。如果用户在禁止区域内发起Xn切换或者周期性注册，AMF会拒绝该流程。

```jinja2
{%- for item in set_amfsoftparaofbit_list -%}
    SET AMFSOFTPARAOFBIT:
    {#- --- 必选参数 --- -#}
    DT={{item.DT}},
    VALUE={{item.VALUE}},
    POSITION={{item.POSITION}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：DT=Dw 时必选 --- -#}
    {%- if item.DT == 'Dw' -%}
        DWORDNUM={{item.DWORDNUM}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 2.5 配置某个区域信息，以及AreaCode与TAI之间的映射关系。

##### 2.5.1 配置区域编码

```jinja2
{%- for item in add_areacode_list_1 -%}
    ADD AREACODE:
    {#- --- 必选参数 --- -#}
    AREACODE="{{item.AREACODE}}",
    {#- --- 可选参数 --- -#}
    {%- if item.DESC is not none -%}
        DESC="{{item.DESC}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

##### 2.5.2 为指定的区域增加跟踪区成员

```jinja2
{%- for item in add_areamem_list_1 -%}
    ADD AREAMEM:
    {#- --- 必选参数 --- -#}
    AREACODE="{{item.AREACODE}}",
    MCC="{{item.MCC}}",
    MNC="{{item.MNC}}",
    BGNTAC="{{item.BGNTAC}}",
    {#- --- 可选参数 --- -#}
    {%- if item.ENDTAC is not none -%}
        ENDTAC="{{item.ENDTAC}}",
    {%- endif -%}
    {%- if item.DESC is not none -%}
        DESC="{{item.DESC}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 2.6 配置某个用户群组信息。

##### 2.6.1 配置5G用户群标识

```jinja2
{%- for item in add_ngusrgrp_list -%}
    ADD NGUSRGRP:
    {#- --- 必选参数 --- -#}
    USRGRPID={{item.USRGRPID}},
    {#- --- 可选参数 --- -#}
    {%- if item.DESC is not none -%}
        DESC="{{item.DESC}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

##### 2.6.2 配置用户群成员

```jinja2
{%- for item in add_ngusrgrpmem_list -%}
    ADD NGUSRGRPMEM:
    {#- --- 必选参数 --- -#}
    USRGRPID={{item.USRGRPID}},
    IMSIPRE="{{item.IMSIPRE}}",
    {#- --- 可选参数 --- -#}
    {%- if item.DESC is not none -%}
        DESC="{{item.DESC}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 2.7 （可选）配置区域漫游限制增强功能，当开关打开时周期性注册更新、服务请求、切换流程中AMF根据本地配置做区域接入限制检查。

```jinja2
{%- if is_optional_area_roaming_restriction_enhancement -%}
    {%- for item in set_ngmmfunc_list_1 -%}
        SET NGMMFUNC:
        {#- --- 可选参数 --- -#}
        {%- if item.AREARSTENSW is not none -%}
            AREARSTENSW={{item.AREARSTENSW}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 2.8 配置拒绝的原因值（由用户签约的“禁止区域（ForbiddenArea）”控制用户的接入）。

```jinja2
{%- for item in set_ngmmproctrl_list -%}
    SET NGMMPROCTRL:
    {#- --- 必选参数 --- -#}
    PROT={{item.PROT}},
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：PROT=OTHER_PROC 时可选 --- -#}
    {%- if item.PROT == 'OTHER_PROC' -%}
        {%- if item.AREARST is not none -%}
            AREARST={{item.AREARST}},
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
        {%- if item.UDMSUBHTTPHTRFC is not none -%}
            UDMSUBHTTPHTRFC={{item.UDMSUBHTTPHTRFC}},
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
```

#### 2.9 AMF本地配置限制区域信息、用户信息、控制模式以及拒绝原因值（由AMF本地配置的接入限制区域控制用户的接入）。

```jinja2
{%- for item in add_ngaccarealst_list -%}
    ADD NGACCAREALST:
    {#- --- 必选参数 --- -#}
    AREARANGE={{item.AREARANGE}},
    CTRLMODE={{item.CTRLMODE}},
    SUBRANGE={{item.SUBRANGE}},
    {#- --- 可选参数 --- -#}
    {%- if item.DESC is not none -%}
        DESC="{{item.DESC}}",
    {%- endif -%}
    {%- if item.REJCAUSE is not none -%}
        REJCAUSE={{item.REJCAUSE}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：AREARANGE=AREA_CODE 时必选 --- -#}
    {%- if item.AREARANGE == 'AREA_CODE' -%}
        AREACODE="{{item.AREACODE}}",
    {%- endif -%}
    {#- --- 条件必选：SUBRANGE=USER_GROUP 时必选 --- -#}
    {%- if item.SUBRANGE == 'USER_GROUP' -%}
        SUBGRPID={{item.SUBGRPID}},
    {%- endif -%}
    {#- --- 条件必选：SUBRANGE=SPECIAL_USER_RANGE 时必选 --- -#}
    {%- if item.SUBRANGE == 'SPECIAL_USER_RANGE' -%}
        IMSIMODE={{item.IMSIMODE}},
    {%- endif -%}
    {#- --- 条件必选：SUBRANGE=MSISDN_PREFIX 时必选 --- -#}
    {%- if item.SUBRANGE == 'MSISDN_PREFIX' -%}
        MSISDNPRE="{{item.MSISDNPRE}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

##### 2.9.1 限制区域之间不允许存在交叉和重叠，“所有区域”例外。

##### 2.9.2 当同时存在“指定区域”和“所有区域”时，以“指定区域”的策略为准，除非UE当前不在“指定区域”。

##### 2.9.3 对于同一个用户，可能匹配“指定区域”内的多个用户号段，该场景下，AMF按照最长匹配的方式优选。


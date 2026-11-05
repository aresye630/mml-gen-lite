---
id: ''
name: 激活服务区域限制特性
ne_type: UNC
type: feature
description: 本操作指导介绍在运行网络中激活服务区域限制特性的操作过程。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","漫游管理功能","WSFD-105006 服务区域限制","激活服务区域限制特性"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本操作指导介绍在运行网络中激活服务区域限制特性的操作过程。

## 必备事项
前提条件

* 请仔细阅读WSFD-105006 服务区域限制特性概述。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    set_ngmmfunc_list:
      type: items
      properties:
        SARSW:
          name: '服务区域限制开关'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: '服务区域限制的功能开关。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        SARNSSW:
          name: '服务区域限制非标开关'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: '“SARNSSW”参数用于配置是否启用服务区域限制的非标方案。所谓服务区域限制的非标方案是指在SMF未支持服务区域限制功能的背景下，由AMF根据UE是否在业务非允许区域内来判定是否限制UE业务可用性。  本特性SMF暂不支持服务区域限制功能，因此建议此处开关设置为“YES”，AMF针对处在业务非允许区域内的UE的所有PDU会话都会限制使用。'
          data_source: ''
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
          description: '配置由于服务区域限制而拒绝UE的业务流程（如服务请求、PDU会话建立）时，下发给UE的原因值。'
          data_source: '全网规划'
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
    add_areacode_list:
      type: items
      properties:
        AREACODE:
          name: '区域编码'
          type: string
          minLength: 1
          maxLength: 128
          required: true
          description: '设置区域编码，唯一标识AMF服务的某个区域。  说明：  对于本网用户，UDM和AMF间可以规划区域码（Area Code），业务允许区域和业务非允许区域也可以通过Area Code进行指定。只不过Area Code的生效范围仅仅是UDM与AMF之间，当AMF需要携带服务区域限制信息跟其它设备，如PCF、NG-RAN或者UE交互时，AMF需要将Area Code翻译成具体的TA列表'
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
    add_srvareares_list:
      type: items
      properties:
        SUBRANGE:
          name: '用户范围'
          type: string
          enum:
          - ALL_USER
          - HOME_USER
          - FOREIGN_USER
          - IMSI_PREFIX
          - IMSI
          required: true
          description: '指定应用接入限制的用户范围。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        AREACODE:
          name: '区域编码'
          type: string
          minLength: 0
          maxLength: 128
          required: false
          description: '指定应用接入限制的某个区域。  该区域编码必须先通过**ADD AREACODE**进行添加；而区域内的跟踪区列表则通过**ADD AREAMEM**进行添加。'
          data_source: ''
          pattern: ''
          default: ''
        SARPRIORITY:
          name: '服务区域限制优先级'
          type: string
          enum:
          - SUB_FIRST
          - CFG_FIRST
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RESTYPE:
          name: '区域群属性'
          type: string
          enum:
          - ALLOWED_AREAS
          - NOT_ALLOWED_AREAS
          required: false
          description: '指定区域群属性。'
          data_source: ''
          pattern: ''
          default: ALLOWED_AREAS
        MAXNUMOFTAS:
          name: '最大跟踪区个数'
          type: integer
          minimum: 0
          maximum: 20000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IMSI:
          name: 'IMSI'
          type: string
          minLength: 14
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IMSIPRE:
          name: 'IMSI前缀'
          type: string
          minLength: 1
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    set_ngmmfunc_list:
    - SARSW: YES
      SARNSSW: YES
    set_ngmmproctrl_list:
    - PROT: OTHER_PROC
      SARST: 0
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
    add_areacode_list:
    - AREACODE: 'MyTown'
      DESC: 'for mytown'
    add_areamem_list:
    - AREACODE: 'MyTown'
      BGNTAC: '010101'
      ENDTAC: '010102'
      MCC: '123'
      MNC: '456'
      DESC: 'areamember of mytown'
    add_srvareares_list:
    - SUBRANGE: ALL_USER
      AREACODE: 'SomeCity'
      SARPRIORITY: CFG_FIRST
      RESTYPE: NOT_ALLOWED_AREAS
      MAXNUMOFTAS: ''
      IMSI: ''
      IMSIPRE: ''
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 进入“MML命令行-UNC”窗口。

### 2 配置服务区域限制的功能开关和非标开关。

```jinja2
{%- for item in set_ngmmfunc_list -%}
    SET NGMMFUNC:
    {#- --- 可选参数 --- -#}
    {%- if item.SARSW is not none -%}
        SARSW={{item.SARSW}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：SARSW=YES 时可选 --- -#}
    {%- if item.SARSW == 'YES' -%}
        {%- if item.SARNSSW is not none -%}
            SARNSSW={{item.SARNSSW}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 配置由于服务区域限制而拒绝UE的业务流程（如服务请求、PDU会话建立）时，下发给UE的原因值。

```jinja2
{%- for item in set_ngmmproctrl_list -%}
    SET NGMMPROCTRL:
    {#- --- 必选参数 --- -#}
    PROT={{item.PROT}},
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：PROT=OTHER_PROC 时可选 --- -#}
    {%- if item.PROT == 'OTHER_PROC' -%}
        {%- if item.SARST is not none -%}
            SARST={{item.SARST}},
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

### 4 （可选）配置某个区域信息，以及AreaCode与TAI之间的映射关系。

#### 4.1 配置区域编码

```jinja2
{%- if is_optional_area_code_tai_mapping -%}
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
{%- endif -%}
```

#### 4.2 为指定的区域增加跟踪区成员

```jinja2
{%- if is_optional_area_code_tai_mapping -%}
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
{%- endif -%}
```

### 5 （可选）配置本地服务区域限制。

```jinja2
{%- if is_optional_local_service_area_restriction -%}
    {%- for item in add_srvareares_list -%}
        ADD SRVAREARES:
        {#- --- 必选参数 --- -#}
        SUBRANGE={{item.SUBRANGE}},
        {#- --- 可选参数 --- -#}
        {%- if item.SARPRIORITY is not none -%}
            SARPRIORITY={{item.SARPRIORITY}},
        {%- endif -%}
        {%- if item.AREACODE is not none -%}
            AREACODE="{{item.AREACODE}}",
        {%- endif -%}
        {%- if item.RESTYPE is not none -%}
            RESTYPE={{item.RESTYPE}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：SUBRANGE=IMSI 时必选 --- -#}
        {%- if item.SUBRANGE == 'IMSI' -%}
            IMSI="{{item.IMSI}}",
        {%- endif -%}
        {#- --- 条件必选：SUBRANGE=IMSI_PREFIX 时必选 --- -#}
        {%- if item.SUBRANGE == 'IMSI_PREFIX' -%}
            IMSIPRE="{{item.IMSIPRE}}",
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：RESTYPE=ALLOWED_AREAS/NOT_ALLOWED_AREAS 时可选 --- -#}
        {%- if item.RESTYPE in ['ALLOWED_AREAS', 'NOT_ALLOWED_AREAS'] -%}
            {%- if item.MAXNUMOFTAS is not none -%}
                MAXNUMOFTAS={{item.MAXNUMOFTAS}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```


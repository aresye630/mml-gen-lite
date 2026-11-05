---
id: ''
name: 激活ODB
ne_type: UNC
type: feature
description: 本操作指导介绍在运行网络中激活支持ODB功能的操作过程。  适用于AMF。
risk_level: ''
doc_source: ["网络部署","业务专题","UNC接入控制专题","会话管理控制","配置会话接入控制功能","激活ODB"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本操作指导介绍在运行网络中激活支持ODB功能的操作过程。适用于AMF。

## 必备事项
前提条件

* 请仔细阅读会话管理控制。
* 需要对端网元UDM支持ODB特性。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    set_ngmmfunc_list:
      type: items
      properties:
        REGODBPLCY:
          name: '注册流程ODB限制策略'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
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
    set_smpductrl_list:
      type: items
      properties:
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
  examples:
    set_ngmmfunc_list:
    - REGODBPLCY: YES
    set_ngmmproctrl_list:
    - PROT: UDM_REGISTRATION
      ODBREJCAUSE: 0
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
    set_smpductrl_list:
    - ODBREJCAUSE: 0
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 进入“MML命令行-UNC”窗口。

### 2 开启ODB注册流程参数检查开关。

#### 2.1 //开启ODB参数检查开关。

```jinja2
{%- for item in set_ngmmfunc_list -%}
    SET NGMMFUNC:
    {#- --- 可选参数 --- -#}
    {%- if item.REGODBPLCY is not none -%}
        REGODBPLCY={{item.REGODBPLCY}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 配置注册流程ODB拒绝原因值。

#### 3.1 //配置注册流程ODB拒绝原因值。

```jinja2
{%- for item in set_ngmmproctrl_list -%}
    SET NGMMPROCTRL:
    {#- --- 必选参数 --- -#}
    PROT={{item.PROT}},
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：PROT=OTHER_PROC 时可选 --- -#}
    {%- if item.PROT == 'OTHER_PROC' -%}
        {%- if item.ODBREJCAUSE is not none -%}
            ODBREJCAUSE={{item.ODBREJCAUSE}},
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

### 4 配置PDU会话建立流程ODB拒绝原因值。

#### 4.1 //配置PDU会话创建流程ODB拒绝原因值。

```jinja2
{%- for item in set_smpductrl_list -%}
    SET SMPDUCTRL:
    {#- --- 可选参数 --- -#}
    {%- if item.ODBREJCAUSE is not none -%}
        ODBREJCAUSE={{item.ODBREJCAUSE}},
    {%- endif -%}
    ;
{%- endfor -%}
```


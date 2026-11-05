---
id: ''
name: 激活VoNR紧急呼叫
ne_type: UNC
type: feature
description: 本操作指导介绍在运行网络中激活VoNR紧急呼叫特性的操作过程。  适用于AMF、SMF。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","语音功能","WSFD-102706 VoNR紧急呼叫","激活VoNR紧急呼叫"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本操作指导介绍在运行网络中激活VoNR紧急呼叫特性的操作过程。适用于AMF、SMF。

## 必备事项
前提条件

* 请仔细阅读7.1-WSFD-102706 VoNR紧急呼叫特性概述。
* 已开启相关License项。
* 已配置紧急呼叫APN。
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
        EMG:
          name: '是否允许紧急呼叫业务'
          type: string
          required: false
          description: '配置AMF支持的紧急呼叫能力。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_ngemgcnum_list:
      type: items
      properties:
        MCC:
          name: '移动国家码'
          type: string
          minLength: 3
          maxLength: 3
          required: true
          description: '添加紧急呼叫号码。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        ESC:
          name: '紧急服务分类'
          type: string
          enum:
          - POLICE
          - AMBULANCE
          - FIREBRIGADE
          - MARINEGUARD
          - MOUNTAIN
          - ALL
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        NUM:
          name: '紧急呼叫号码'
          type: string
          minLength: 1
          maxLength: 80
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    set_ngemgsrvfunc_list:
      type: items
      properties:
        HOMEEMG:
          name: '本网用户是否允许紧急呼叫业务'
          type: string
          required: false
          description: '配置本网用户5G紧急呼叫业务。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        HOMEEMGCNUMSW:
          name: '本网用户紧急号码列表下发开关'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_ngemgcfg_list:
      type: items
      properties:
        NOID:
          name: '运营商标识'
          type: integer
          minimum: 0
          maximum: 0
          required: true
          description: '增加运营商指定MNO或MVNO对应的紧急呼叫配置数据。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        EMGMODE:
          name: '紧急会话创建模式'
          type: string
          enum:
          - VALIDUE
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        DNN:
          name: '数据网络名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        SST:
          name: '切片业务类型'
          type: integer
          minimum: 0
          maximum: 255
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        SD:
          name: '切片细分标识'
          type: string
          minLength: 6
          maxLength: 6
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    set_licenseswitch_list_1:
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
    add_apn_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '添加一个新的APN实例。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        EMERGENCYSWITCH:
          name: '支持紧急呼叫'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: DISABLE
        S6BEMERGCYSERVICE:
          name: 'S6b Emergency Service 标识'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
    set_apnpccfunc_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          maxLength: 63
          required: true
          description: '使能紧急APN的PCC功能。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        HOMEPCCSWITCH:
          name: '本地用户PCC功能'
          type: string
          enum:
          - DISABLE
          - ENABLE
          - INHERIT
          required: false
          description: ''
          data_source: '与对端协商'
          pattern: ''
          default: ''
        ROAMPCCSWITCH:
          name: '漫游用户PCC功能'
          type: string
          enum:
          - DISABLE
          - ENABLE
          - INHERIT
          required: false
          description: ''
          data_source: '与对端协商'
          pattern: ''
          default: ''
        VISITPCCSWITCH:
          name: '拜访用户PCC功能'
          type: string
          enum:
          - DISABLE
          - ENABLE
          - INHERIT
          required: false
          description: ''
          data_source: '与对端协商'
          pattern: ''
          default: ''
        PCFSELECTMODE:
          name: '选择PCF方式'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    set_apnimsattr_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '设置APN的IMS属性。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        IMSSWITCH:
          name: 'IMS开关'
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
        SIGNALRADIOPRE:
          name: '信令空口增强开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_pcscfgroup_list:
      type: items
      properties:
        GROUPNAME:
          name: 'P-CSCF组名'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '增加P-CSCF组配置。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPVERSION:
          name: 'IP地址版本'
          type: string
          enum:
          - IPV4
          - IPV6
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: IPV4
        ALLOCTYPE:
          name: 'P-CSCF获取方式'
          type: string
          enum:
          - LOCAL
          - DHCP
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: LOCAL
    add_pcscfgrpbndapn_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '增加APN和P-CSCF组关联关系。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        DEFAULTFLAG:
          name: '缺省标记'
          type: string
          enum:
          - DEFAULT
          - IMSI_MSISDN_SEG
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        MPCSCFGRPIPV6:
          name: '主IPv6 P-CSCF组'
          type: string
          minLength: 1
          maxLength: 63
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IMSIMSISDNSEG:
          name: 'IMSI/MSISDN号段名称'
          type: string
          minLength: 1
          maxLength: 31
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        PRIORITY:
          name: '优先级'
          type: integer
          minimum: 1
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_smfemgcfg_list:
      type: items
      properties:
        NOID:
          name: '运营商标识'
          type: integer
          minimum: 0
          maximum: 0
          required: true
          description: '增加运营商紧急呼叫会话相关功能配置。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        ARPPL:
          name: '紧急会话ARP优先级级别'
          type: integer
          minimum: 0
          maximum: 15
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        ARPPCI:
          name: '紧急会话ARP的Pre-emption Capability'
          type: string
          enum:
          - NOT_PREEMPT
          - MAY_PREEMPT
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        ARPPVI:
          name: '紧急会话ARP的Pre-emption Vulnerability'
          type: string
          enum:
          - NOT_PREEMPTABLE
          - PREEMPTABLE
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        ULSESSIONAMBR:
          name: '紧急会话上行Session AMBR(千比特/秒)'
          type: integer
          minimum: 0
          maximum: 20000000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 500
        DLSESSIONAMBR:
          name: '紧急会话下行session AMBR(千比特/秒)'
          type: integer
          minimum: 0
          maximum: 20000000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 500
        EMGMODE:
          name: '紧急会话创建模式'
          type: string
          enum:
          - VALIDUE
          - IMSIUE
          - ALLUE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: VALIDUE
        FIVEQI:
          name: '紧急会话标准5QI'
          type: integer
          minimum:
          - 5
          - 69
          - 79
          maximum:
          - 9
          - 70
          - 80
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 5
        FIVEQIPL:
          name: '紧急会话5QI的优先级别'
          type: integer
          minimum: 0
          maximum: 127
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 0
        UDMREG:
          name: '紧急会话注册UDM功能开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
    set_apnidletime_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        INHERIT:
          name: '继承默认开关'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        SCTXCHKSW:
          name: 'SGW-C空闲上下文核查开关'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        PCTXCHKSW:
          name: 'PGW-C和SGW-C/PGW-C空闲上下文检查开关'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        GCTXCHKSW:
          name: 'GGSN空闲上下文检查开关'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        HCTXCHKSW:
          name: 'H-SMF空闲上下文核查开关'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        ICTXCHKSW:
          name: 'I-SMF/V-SMF空闲上下文核查开关'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        GULTIMERLEVEL:
          name: 'GUL承载级别参数'
          type: string
          enum:
          - SESSION
          - BEARER
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        DFTBEARPOLICY:
          name: '缺省承载和默认GBR的定时器'
          type: string
          enum:
          - ONEDAY
          - OFF
          - USEBEARERTIMER
          - USESPECIFICVAL
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        BEARERTIMER:
          name: '承载定时器(min)'
          type: integer
          minimum: 5
          maximum: 12000
          required: false
          description: '配置紧急呼叫结束后释放缺省承载。  对于“BEARERTIMER”时长参数，如果运营商没有特殊要求，建议保持默认值60分钟。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SESSIONTIMER:
          name: '会话定时器时长(min)'
          type: integer
          minimum: 5
          maximum: 12000
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        DFTBRPLCYGGSN:
          name: 'GGSN一次激活上下文定时器'
          type: string
          enum:
          - ONEDAY
          - OFF
          - USEBEARERTIMER
          - USESPECIFICVAL
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        HCTXINACHKSW:
          name: 'H-SMF不活动上下文核查开关'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        HSMFTIMERLEVEL:
          name: 'H-SMF空闲上下文核查级别'
          type: string
          enum:
          - SESSION
          - QOSFLOW
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ICTXINACHKSW:
          name: 'I-SMF/V-SMF不活动上下文核查开关'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IDLEUPDATEMSG:
          name: '空闲超时发送更新消息'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PROS8CTXCHKSW:
          name: 'Proxy-SMF S8空闲上下文核查开关'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PROXYSMFCHKSW:
          name: 'Proxy-SMF 空闲上下文核查开关'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SMFSESIDLETIMER:
          name: 'SMF会话空闲定时器时长(min)'
          type: integer
          minimum: 5
          maximum: 12000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SMFSESINATIMER:
          name: 'SMF会话不活动定时器时长(min)'
          type: integer
          minimum: 5
          maximum: 12000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV2VONRECMM01'
      SWITCH: ENABLE
    set_ngmmfunc_list:
    - EMG: EMCNR-1
    add_ngemgcnum_list:
    - MCC: '123'
      ESC: FIREBRIGADE
      NUM: '119'
    set_ngemgsrvfunc_list:
    - HOMEEMG: EMFNR-0&EMCNR-1
      HOMEEMGCNUMSW: YES
    add_ngemgcfg_list:
    - NOID: 0
      EMGMODE: VALIDUE
      DNN: 'sos'
      SST: 0
      SD: 'FFFFFF'
    set_licenseswitch_list_1:
    - LICITEM: 'LKV2VONRECSM01'
      SWITCH: ENABLE
    add_apn_list:
    - APN: 'sos'
      EMERGENCYSWITCH: ENABLE
      S6BEMERGCYSERVICE: DISABLE
    set_apnpccfunc_list:
    - APN: 'sos'
      HOMEPCCSWITCH: ENABLE
      ROAMPCCSWITCH: ENABLE
      VISITPCCSWITCH: ENABLE
      PCFSELECTMODE: DNN-1&GPSI-0&IMSI-0&NFLOC-0&PLMN-0&SERVINGSCOPE-1&SNSSAIS-0
    set_apnimsattr_list:
    - APN: 'sos'
      IMSSWITCH: ENABLE
      SIGNALRADIOPRE: ''
    add_pcscfgroup_list:
    - GROUPNAME: 'pcscf_group1'
      IPVERSION: IPV6
      ALLOCTYPE: LOCAL
    add_pcscfgrpbndapn_list:
    - APN: 'sos'
      DEFAULTFLAG: DEFAULT
      MPCSCFGRPIPV6: 'pcscf_group1'
      IMSIMSISDNSEG: 'pcscf_group1'
      PRIORITY: ''
    add_smfemgcfg_list:
    - NOID: 0
      ARPPL: 1
      ARPPCI: NOT_PREEMPT
      ARPPVI: NOT_PREEMPTABLE
      ULSESSIONAMBR: 20000
      DLSESSIONAMBR: 40000
      EMGMODE: VALIDUE
      FIVEQI: 5
      FIVEQIPL: 0
      UDMREG: DISABLE
    set_apnidletime_list:
    - APN: 'sos'
      INHERIT: NO
      SCTXCHKSW: ENABLE
      PCTXCHKSW: ENABLE
      GCTXCHKSW: ENABLE
      HCTXCHKSW: ENABLE
      ICTXCHKSW: ENABLE
      GULTIMERLEVEL: BEARER
      DFTBEARPOLICY: ONEDAY
      BEARERTIMER: 60
      SESSIONTIMER: 120
      DFTBRPLCYGGSN: ''
      HCTXINACHKSW: ''
      HSMFTIMERLEVEL: ''
      ICTXINACHKSW: ''
      IDLEUPDATEMSG: ''
      PROS8CTXCHKSW: ''
      PROXYSMFCHKSW: ''
      SMFSESIDLETIMER: ''
      SMFSESINATIMER: ''
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 在AMF上配置VoNR紧急呼叫业务

### 打开本特性的License配置开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

### 2 配置是否允许紧急呼叫业务。

```jinja2
{%- for item in set_ngmmfunc_list -%}
    SET NGMMFUNC:
    {#- --- 可选参数 --- -#}
    {%- if item.EMG is not none -%}
        EMG={{item.EMG}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 添加紧急呼叫号码。

```jinja2
{%- for item in add_ngemgcnum_list -%}
    ADD NGEMGCNUM:
    {#- --- 必选参数 --- -#}
    MCC="{{item.MCC}}",
    ESC={{item.ESC}},
    NUM="{{item.NUM}}",
    ;
{%- endfor -%}
```

### 4 配置本网用户5G紧急呼叫业务。

```jinja2
{%- for item in set_ngemgsrvfunc_list -%}
    SET NGEMGSRVFUNC:
    {#- --- 可选参数 --- -#}
    {%- if item.HOMEEMG is not none -%}
        HOMEEMG={{item.HOMEEMG}},
    {%- endif -%}
    {%- if item.HOMEEMGCNUMSW is not none -%}
        HOMEEMGCNUMSW={{item.HOMEEMGCNUMSW}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 5 **可选：**配置互联PLMN的用户使用VoNR紧急呼叫业务。

### 如果系统中已有互联PLMN的配置，通过**LST NGCONNECTPLMN**确认“EMG”参数配置是否符合预期，如果不符合预期，通过**MOD NGCONNECTPLMN**调整。

### 该紧急呼叫业务受**SET NGMMFUNC**参数“EMG”和**ADD NGCONNECTPLMN**参数“EMG”控制，且同时开启才能生效。

### 6 配置运营商指定MNO或MVNO对应的紧急呼叫数据。

```jinja2
{%- for item in add_ngemgcfg_list -%}
    ADD NGEMGCFG:
    {#- --- 必选参数 --- -#}
    NOID={{item.NOID}},
    EMGMODE={{item.EMGMODE}},
    DNN="{{item.DNN}}",
    {#- --- 可选参数 --- -#}
    {%- if item.SST is not none -%}
        SST={{item.SST}},
    {%- endif -%}
    {%- if item.SD is not none -%}
        SD="{{item.SD}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 7 在SMF上配置VoNR紧急呼叫业务

### 打开本特性的License配置开关。

```jinja2
{%- for item in set_licenseswitch_list_1 -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

### 8 配置APN参数，并将APN下的某指定号段绑定到P-CSCF组，使能紧急呼叫功能。

### 创建APN实例。

```jinja2
{%- for item in add_apn_list -%}
    ADD APN:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    {#- --- 可选参数 --- -#}
    {%- if item.EMERGENCYSWITCH is not none -%}
        EMERGENCYSWITCH={{item.EMERGENCYSWITCH}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：EMERGENCYSWITCH=ENABLE 时可选 --- -#}
    {%- if item.EMERGENCYSWITCH == 'ENABLE' -%}
        {%- if item.S6BEMERGCYSERVICE is not none -%}
            S6BEMERGCYSERVICE={{item.S6BEMERGCYSERVICE}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 若此APN上已有用户，则已接入的用户仍然按照普通APN处理，新接入的用户按照紧急呼叫用户处理。

### 使能APN的PCC功能。

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
    {%- if item.PCFSELECTMODE is not none -%}
        PCFSELECTMODE={{item.PCFSELECTMODE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 配置APN的IMS属性。

```jinja2
{%- for item in set_apnimsattr_list -%}
    SET APNIMSATTR:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    {#- --- 可选参数 --- -#}
    {%- if item.IMSSWITCH is not none -%}
        IMSSWITCH={{item.IMSSWITCH}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：IMSSWITCH=ENABLE 时可选 --- -#}
    {%- if item.IMSSWITCH == 'ENABLE' -%}
        {%- if item.SIGNALRADIOPRE is not none -%}
            SIGNALRADIOPRE={{item.SIGNALRADIOPRE}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 配置P-CSCF组名。

```jinja2
{%- for item in add_pcscfgroup_list -%}
    ADD PCSCFGROUP:
    {#- --- 必选参数 --- -#}
    GROUPNAME="{{item.GROUPNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.IPVERSION is not none -%}
        IPVERSION={{item.IPVERSION}},
    {%- endif -%}
    {%- if item.ALLOCTYPE is not none -%}
        ALLOCTYPE={{item.ALLOCTYPE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 将APN下的某指定号段绑定到P-CSCF组。

```jinja2
{%- for item in add_pcscfgrpbndapn_list -%}
    ADD PCSCFGRPBNDAPN:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    DEFAULTFLAG={{item.DEFAULTFLAG}},
    {#- --- 可选参数 --- -#}
    {%- if item.MPCSCFGRPIPV6 is not none -%}
        MPCSCFGRPIPV6="{{item.MPCSCFGRPIPV6}}",
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：DEFAULTFLAG=IMSI_MSISDN_SEG 时必选 --- -#}
    {%- if item.DEFAULTFLAG == 'IMSI_MSISDN_SEG' -%}
        IMSIMSISDNSEG="{{item.IMSIMSISDNSEG}}",
    {%- endif -%}
    {#- --- 条件必选：DEFAULTFLAG=IMSI_MSISDN_SEG 时必选 --- -#}
    {%- if item.DEFAULTFLAG == 'IMSI_MSISDN_SEG' -%}
        PRIORITY={{item.PRIORITY}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 9 配置运营商紧急呼叫会话相关功能。

```jinja2
{%- for item in add_smfemgcfg_list -%}
    ADD SMFEMGCFG:
    {#- --- 必选参数 --- -#}
    NOID={{item.NOID}},
    ARPPL={{item.ARPPL}},
    ARPPCI={{item.ARPPCI}},
    ARPPVI={{item.ARPPVI}},
    {#- --- 可选参数 --- -#}
    {%- if item.ULSESSIONAMBR is not none -%}
        ULSESSIONAMBR={{item.ULSESSIONAMBR}},
    {%- endif -%}
    {%- if item.DLSESSIONAMBR is not none -%}
        DLSESSIONAMBR={{item.DLSESSIONAMBR}},
    {%- endif -%}
    {%- if item.EMGMODE is not none -%}
        EMGMODE={{item.EMGMODE}},
    {%- endif -%}
    {%- if item.FIVEQI is not none -%}
        FIVEQI={{item.FIVEQI}},
    {%- endif -%}
    {%- if item.FIVEQIPL is not none -%}
        FIVEQIPL={{item.FIVEQIPL}},
    {%- endif -%}
    {%- if item.UDMREG is not none -%}
        UDMREG={{item.UDMREG}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 10 配置紧急呼叫结束后释放缺省承载。

```jinja2
{%- for item in set_apnidletime_list -%}
    SET APNIDLETIME:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    {#- --- 可选参数 --- -#}
    {%- if item.INHERIT is not none -%}
        INHERIT={{item.INHERIT}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：INHERIT=NO 时可选 --- -#}
    {%- if item.INHERIT == 'NO' -%}
        {%- if item.SCTXCHKSW is not none -%}
            SCTXCHKSW={{item.SCTXCHKSW}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：INHERIT=NO 时可选 --- -#}
    {%- if item.INHERIT == 'NO' -%}
        {%- if item.PCTXCHKSW is not none -%}
            PCTXCHKSW={{item.PCTXCHKSW}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：INHERIT=NO 时可选 --- -#}
    {%- if item.INHERIT == 'NO' -%}
        {%- if item.GCTXCHKSW is not none -%}
            GCTXCHKSW={{item.GCTXCHKSW}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：INHERIT=NO 时可选 --- -#}
    {%- if item.INHERIT == 'NO' -%}
        {%- if item.HCTXCHKSW is not none -%}
            HCTXCHKSW={{item.HCTXCHKSW}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：INHERIT=NO 时可选 --- -#}
    {%- if item.INHERIT == 'NO' -%}
        {%- if item.ICTXCHKSW is not none -%}
            ICTXCHKSW={{item.ICTXCHKSW}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：INHERIT=NO 时可选 --- -#}
    {%- if item.INHERIT == 'NO' -%}
        {%- if item.GULTIMERLEVEL is not none -%}
            GULTIMERLEVEL={{item.GULTIMERLEVEL}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：INHERIT=NO 时可选 --- -#}
    {%- if item.INHERIT == 'NO' -%}
        {%- if item.DFTBEARPOLICY is not none -%}
            DFTBEARPOLICY={{item.DFTBEARPOLICY}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：INHERIT=NO 时可选 --- -#}
    {%- if item.INHERIT == 'NO' -%}
        {%- if item.BEARERTIMER is not none -%}
            BEARERTIMER={{item.BEARERTIMER}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：INHERIT=NO 时可选 --- -#}
    {%- if item.INHERIT == 'NO' -%}
        {%- if item.SESSIONTIMER is not none -%}
            SESSIONTIMER={{item.SESSIONTIMER}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：INHERIT=NO 时可选 --- -#}
    {%- if item.INHERIT == 'NO' -%}
        {%- if item.DFTBRPLCYGGSN is not none -%}
            DFTBRPLCYGGSN={{item.DFTBRPLCYGGSN}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：INHERIT=NO 时可选 --- -#}
    {%- if item.INHERIT == 'NO' -%}
        {%- if item.HCTXINACHKSW is not none -%}
            HCTXINACHKSW={{item.HCTXINACHKSW}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：INHERIT=NO 时可选 --- -#}
    {%- if item.INHERIT == 'NO' -%}
        {%- if item.HSMFTIMERLEVEL is not none -%}
            HSMFTIMERLEVEL={{item.HSMFTIMERLEVEL}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：INHERIT=NO 时可选 --- -#}
    {%- if item.INHERIT == 'NO' -%}
        {%- if item.ICTXINACHKSW is not none -%}
            ICTXINACHKSW={{item.ICTXINACHKSW}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：INHERIT=NO 时可选 --- -#}
    {%- if item.INHERIT == 'NO' -%}
        {%- if item.IDLEUPDATEMSG is not none -%}
            IDLEUPDATEMSG={{item.IDLEUPDATEMSG}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：INHERIT=NO 时可选 --- -#}
    {%- if item.INHERIT == 'NO' -%}
        {%- if item.PROS8CTXCHKSW is not none -%}
            PROS8CTXCHKSW={{item.PROS8CTXCHKSW}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：INHERIT=NO 时可选 --- -#}
    {%- if item.INHERIT == 'NO' -%}
        {%- if item.PROXYSMFCHKSW is not none -%}
            PROXYSMFCHKSW={{item.PROXYSMFCHKSW}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：INHERIT=NO 时可选 --- -#}
    {%- if item.INHERIT == 'NO' -%}
        {%- if item.SMFSESIDLETIMER is not none -%}
            SMFSESIDLETIMER={{item.SMFSESIDLETIMER}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：INHERIT=NO 时可选 --- -#}
    {%- if item.INHERIT == 'NO' -%}
        {%- if item.SMFSESINATIMER is not none -%}
            SMFSESINATIMER={{item.SMFSESINATIMER}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```


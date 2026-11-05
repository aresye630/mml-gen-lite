---
id: ''
name: 激活DNS tunnel计费防欺诈
ne_type: UDG
type: feature
description: 当运营商设置了DNS免费策略时，为了避免黑客将用户原始数据报文隐匿在DNS报文中进行计费欺诈，需要部署DNS tunnel计费防欺诈功能阻止该类行为的发生。  适用于PGW-U、UPF。
risk_level: ''
doc_source: ["特性部署","业务专题","UDG防欺诈功能专题","DNS计费防欺诈","激活DNS计费防欺诈","激活DNS tunnel计费防欺诈"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
当运营商设置了DNS免费策略时，为了避免黑客将用户原始数据报文隐匿在DNS报文中进行计费欺诈，需要部署DNS tunnel计费防欺诈功能阻止该类行为的发生。适用于PGW-U、UPF。

## 必备事项
前提条件

* 请仔细阅读DNS计费防欺诈原理。
* 完成加载license（如果有需求，请联系华为技术支持工程师处理）。
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
          description: '-'
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
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_apnaffunc_list:
      type: items
      properties:
        APN:
          name: 'APN'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '已通过**ADD APN**命令配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        ISENABLE:
          name: '防欺诈开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: true
          description: '只有使能了**SET APNAFFUNC**，使能DNS计费防欺诈开关**SET ANTIFRAUD**才有效。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_antifraud_list:
      type: items
      properties:
        ISNULLRECEN:
          name: '空记录DNS防欺诈开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '使能头域Type字段是否为“NULL”或“text”的检查，关闭启发式识别。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        ISTEXTEN:
          name: '文本记录DNS防欺诈开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        ISHEURISTICEN:
          name: '启发式DNS防欺诈开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_afdnschecktype_list:
      type: items
      properties:
        TYPEVALUE:
          name: 'DNS防欺诈检查类型值'
          type: integer
          minimum: 1
          maximum: 255
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_urr_list:
      type: items
      properties:
        URRNAME:
          name: '使用量上报规则名称'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: 'urr\_dns用于DNS欺诈报文的使用量上报规则处理。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        URRID:
          name: 'URR标识'
          type: integer
          minimum: 0
          maximum: 2147483646
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        USAGERPTMODE:
          name: '使用量上报模式'
          type: string
          enum:
          - MONITORINGKEY
          - OFFLINE
          - ONLINE
          - QOS
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        DFTQUOTAPARA:
          name: '默认流量配额的单位'
          type: string
          enum:
          - Byte
          - KByte
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: Byte
        DFTQUOTATIME:
          name: '默认时长配额（秒）'
          type: integer
          minimum:
          - 0
          - 4294967295
          maximum:
          - 3600
          - 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DFTQUOTAVOLUME:
          name: '默认流量配额'
          type: integer
          minimum:
          - 0
          - 1000
          maximum:
          - 0
          - 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        OFFMETERINGTYPE:
          name: '离线计费统计类型'
          type: string
          enum:
          - EVENT
          - EVENT_TIME
          - EVENT_VOLUME
          - EVENT_VOLUME_TIME
          - FREE
          - TIME
          - VOLUME
          - VOLUME_TIME
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: VOLUME
        ONLMETERINGTYPE:
          name: '在线计费统计类型'
          type: string
          enum:
          - EVENT
          - EVENT_TIME
          - EVENT_VOLUME
          - EVENT_VOLUME_TIME
          - FREE
          - TIME
          - VOLUME
          - VOLUME_TIME
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: VOLUME
        RG:
          name: '计费组'
          type: integer
          minimum: 0
          maximum: 4294967294
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SID:
          name: '业务标识'
          type: integer
          minimum: 0
          maximum: 4294967294
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_urrgroup_list:
      type: items
      properties:
        URRGROUPNAME:
          name: '使用量上报规则组名称'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: '上下行业务触发使用的URRName，已通过**ADD URR**命令配置完成。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        UPURRNAME1:
          name: '上行发起URR名称1'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        UPURRNAME2:
          name: '上行发起URR名称2'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        DOWNURRNAME1:
          name: '下行发起URR名称1'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        DOWNURRNAME2:
          name: '下行发起URR名称2'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_pccactionprop_list:
      type: items
      properties:
        PCCACTPROPNAME:
          name: 'PCC动作属性名称'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: 'ap\_dns用于DNS欺诈报文的动作处理。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        UPINITUPGATE:
          name: '上行发起上行门控'
          type: string
          enum:
          - DISCARD
          - PASS
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: PASS
    add_pccpolicygrp_list:
      type: items
      properties:
        PCCPOLICYGRPNM:
          name: 'PCC策略组名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: 'pg\_dns用于DNS欺诈报文的PCC策略组，包括计费处理和动作处理。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        URRGROUPNAME:
          name: 'URR组名称'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: 'PCC策略组绑定的URR组名称，已通过**ADD URRGROUP**命令配置完成。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        PCCACTPROPNAME:
          name: 'PCC动作属性名称'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: 'PCC策略组绑定的动作属性，已通过**ADD PCCACTIONPROP**命令配置完成。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_afpolicy_list:
      type: items
      properties:
        AFPOLICYTYPE:
          name: '防欺诈策略类型'
          type: string
          enum:
          - DNS
          - HTTP
          - HTTPS
          required: true
          description: '指定防欺诈策略类型是DNS。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PCCPOLICYGRPNM:
          name: 'PCC策略组名称'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: 'DNS欺诈报文使用的PCC策略，已通过**ADD PCCPOLICYGRP**命令配置完成。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV3G5DCAS01'
      SWITCH: ENABLE
    set_apnaffunc_list:
    - APN: 'apn-test'
      ISENABLE: ENABLE
    set_antifraud_list:
    - ISNULLRECEN: ENABLE
      ISTEXTEN: ENABLE
      ISHEURISTICEN: DISABLE
    add_afdnschecktype_list:
    - TYPEVALUE: 11
    add_urr_list:
    - URRNAME: 'urr_fraud_online'
      URRID: 1000
      USAGERPTMODE: ONLINE
      DFTQUOTAPARA: Byte
      DFTQUOTATIME: ''
      DFTQUOTAVOLUME: ''
      OFFMETERINGTYPE: VOLUME
      ONLMETERINGTYPE: VOLUME
      RG: ''
      SID: ''
    add_urrgroup_list:
    - URRGROUPNAME: 'urrg_fraud'
      UPURRNAME1: 'urr_fraud_online'
      UPURRNAME2: 'urr_fraud_offline'
      DOWNURRNAME1: 'urr_fraud_online'
      DOWNURRNAME2: 'urr_fraud_offline'
    add_pccactionprop_list:
    - PCCACTPROPNAME: 'ap_fraud'
      UPINITUPGATE: PASS
    add_pccpolicygrp_list:
    - PCCPOLICYGRPNM: 'pg_fraud'
      URRGROUPNAME: 'urrg_fraud'
      PCCACTPROPNAME: 'ap_fraud'
    add_afpolicy_list:
    - AFPOLICYTYPE: DNS
      PCCPOLICYGRPNM: 'pg_fraud'
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 //打开本特性的License配置开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

### 2 //配置指定APN下使能计费防欺诈。

```jinja2
{%- for item in set_apnaffunc_list -%}
    SET APNAFFUNC:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    ISENABLE={{item.ISENABLE}},
    ;
{%- endfor -%}
```

### 3 //配置使能DNS计费防欺诈功能。

```jinja2
{%- for item in set_antifraud_list -%}
    SET ANTIFRAUD:
    {#- --- 可选参数 --- -#}
    {%- if item.ISNULLRECEN is not none -%}
        ISNULLRECEN={{item.ISNULLRECEN}},
    {%- endif -%}
    {%- if item.ISTEXTEN is not none -%}
        ISTEXTEN={{item.ISTEXTEN}},
    {%- endif -%}
    {%- if item.ISHEURISTICEN is not none -%}
        ISHEURISTICEN={{item.ISHEURISTICEN}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 //配置需要进行防欺诈检查的DNS报文类型。

```jinja2
{%- for item in add_afdnschecktype_list -%}
    ADD AFDNSCHECKTYPE:
    {#- --- 必选参数 --- -#}
    TYPEVALUE={{item.TYPEVALUE}},
    ;
{%- endfor -%}
```

### 5 //配置URR组和策略。

```jinja2
{%- for item in add_urr_list -%}
    ADD URR:
    {#- --- 必选参数 --- -#}
    URRNAME="{{item.URRNAME}}",
    URRID={{item.URRID}},
    USAGERPTMODE={{item.USAGERPTMODE}},
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：USAGERPTMODE=ONLINE 时可选 --- -#}
    {%- if item.USAGERPTMODE == 'ONLINE' -%}
        {%- if item.DFTQUOTAPARA is not none -%}
            DFTQUOTAPARA={{item.DFTQUOTAPARA}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：USAGERPTMODE=ONLINE 时可选 --- -#}
    {%- if item.USAGERPTMODE == 'ONLINE' -%}
        {%- if item.DFTQUOTATIME is not none -%}
            DFTQUOTATIME={{item.DFTQUOTATIME}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：USAGERPTMODE=ONLINE 时可选 --- -#}
    {%- if item.USAGERPTMODE == 'ONLINE' -%}
        {%- if item.DFTQUOTAVOLUME is not none -%}
            DFTQUOTAVOLUME={{item.DFTQUOTAVOLUME}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：USAGERPTMODE=OFFLINE 时可选 --- -#}
    {%- if item.USAGERPTMODE == 'OFFLINE' -%}
        {%- if item.OFFMETERINGTYPE is not none -%}
            OFFMETERINGTYPE={{item.OFFMETERINGTYPE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：USAGERPTMODE=ONLINE 时可选 --- -#}
    {%- if item.USAGERPTMODE == 'ONLINE' -%}
        {%- if item.ONLMETERINGTYPE is not none -%}
            ONLMETERINGTYPE={{item.ONLMETERINGTYPE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：USAGERPTMODE=ONLINE/OFFLINE 时可选 --- -#}
    {%- if item.USAGERPTMODE in ['ONLINE', 'OFFLINE'] -%}
        {%- if item.RG is not none -%}
            RG={{item.RG}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：USAGERPTMODE=ONLINE/OFFLINE 时可选 --- -#}
    {%- if item.USAGERPTMODE in ['ONLINE', 'OFFLINE'] -%}
        {%- if item.SID is not none -%}
            SID={{item.SID}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_urrgroup_list -%}
    ADD URRGROUP:
    {#- --- 必选参数 --- -#}
    URRGROUPNAME="{{item.URRGROUPNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.UPURRNAME1 is not none -%}
        UPURRNAME1="{{item.UPURRNAME1}}",
    {%- endif -%}
    {%- if item.UPURRNAME2 is not none -%}
        UPURRNAME2="{{item.UPURRNAME2}}",
    {%- endif -%}
    {%- if item.DOWNURRNAME1 is not none -%}
        DOWNURRNAME1="{{item.DOWNURRNAME1}}",
    {%- endif -%}
    {%- if item.DOWNURRNAME2 is not none -%}
        DOWNURRNAME2="{{item.DOWNURRNAME2}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_pccactionprop_list -%}
    ADD PCCACTIONPROP:
    {#- --- 必选参数 --- -#}
    PCCACTPROPNAME="{{item.PCCACTPROPNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.UPINITUPGATE is not none -%}
        UPINITUPGATE={{item.UPINITUPGATE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_pccpolicygrp_list -%}
    ADD PCCPOLICYGRP:
    {#- --- 必选参数 --- -#}
    PCCPOLICYGRPNM="{{item.PCCPOLICYGRPNM}}",
    {#- --- 可选参数 --- -#}
    {%- if item.PCCACTPROPNAME is not none -%}
        PCCACTPROPNAME="{{item.PCCACTPROPNAME}}",
    {%- endif -%}
    {%- if item.URRGROUPNAME is not none -%}
        URRGROUPNAME="{{item.URRGROUPNAME}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 6 //配置DNS欺诈报文的策略。

```jinja2
{%- for item in add_afpolicy_list -%}
    ADD AFPOLICY:
    {#- --- 必选参数 --- -#}
    AFPOLICYTYPE={{item.AFPOLICYTYPE}},
    {#- --- 可选参数 --- -#}
    {%- if item.PCCPOLICYGRPNM is not none -%}
        PCCPOLICYGRPNM="{{item.PCCPOLICYGRPNM}}",
    {%- endif -%}
    ;
{%- endfor -%}
```


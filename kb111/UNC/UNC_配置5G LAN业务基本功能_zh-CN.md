---
id: ''
name: 配置5G LAN业务基本功能
ne_type: UNC
type: feature
description: 本操作用于指导在SMF侧开通5G LAN相关业务，完成相关配置。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","5G LAN解决方案","WSFD-225003 5G LAN业务基本功能","配置5G LAN业务基本功能"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本操作用于指导在SMF侧开通5G LAN相关业务，完成相关配置。

## 必备事项
前提条件

* 操作人员已了解本功能的原理。
* 已完成加载License，可以通过**DSP LICENSE**命令查询确认，如果本特性的License在查询列表中可见，即可认为本特性License已加载成功。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    set_smffunc_list:
      type: items
      properties:
        NGLANSWITCH:
          name: '支持是否建立5G LAN会话'
          type: string
          enum:
          - NotSupport
          - Support
          required: false
          description: '配置开启5G LAN功能开关。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        VNGROUPDATASW:
          name: '5G LAN会话是否向UDM查询VnGroupData'
          type: string
          enum:
          - NotSupport
          - Support
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_upselectflag_list:
      type: items
      properties:
        NGLANUPFSELSW:
          name: '5G LAN UPF选择开关'
          type: string
          enum:
          - LOCALABILITY
          - GCOMABILITY
          - LOCALANDGCOM
          required: false
          description: '配置对5G LAN UPF的选择机制。'
          data_source: '本端规划'
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
          description: '配置对端UPF支持5G LAN。'
          data_source: '全网规划  与**ADD PNFPROFILE**命令中的“NF实例标识”参数取值保持一致'
          pattern: ''
          default: ''
        NGLANSW:
          name: '是否支持5G LAN'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_pfcppvtext_list:
      type: items
      properties:
        FEATURE:
          name: '特性名称'
          type: string
          enum:
          - QER_TYPE
          - BWM
          - UPA
          - SESSION_ROLE_TYPE
          - DNAI
          - QCI
          - ARP
          - URR_CHARGING_TYPE
          - RG
          - SID
          - HW_EVENT_MEASUREMENT
          - S_NSSAI
          - SELF_SEID
          - SGW_STATE_INFO
          - NGLAN
          - L2TP_TNL
          - L2TP_PCO
          - MultiDNN_Type
          - MultiDNN_DNN
          - MultiDNN_Snssai
          - MultiDNN_IP_Address
          - MultiDNN_Rat_Type
          - MultiDNN_DNS_Filter
          - MultiDNN_Filter_Indication
          - URR_PERF_TYPE
          - AUTH_CLASS
          - CHARGING_TYPE
          - Qos_Analysis
          - EXTEND_ROAMING_TYPE
          - EXTEND_PROXY_TYPE
          - Session_Delete_Cause
          - Qos_Experience
          - Feature_Rule
          - Qos_Quality_Indicate
          - IPE_Indicate
          - Default_Qos_Flag
          required: true
          description: '配置5G LAN关键信元。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SWITCH:
          name: '私有信元携带开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
  examples:
    set_smffunc_list:
    - NGLANSWITCH: Support
      VNGROUPDATASW: Support
    set_upselectflag_list:
    - NGLANUPFSELSW: LOCALABILITY
    mod_upnode_list:
    - NFINSTANCENAME: 'UPF_Instance0'
      NGLANSW: ENABLE
    set_pfcppvtext_list:
    - FEATURE: NGLAN
      SWITCH: ENABLE
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 //配置开启5G LAN功能开关。

```jinja2
{%- for item in set_smffunc_list -%}
    SET SMFFUNC:
    {#- --- 可选参数 --- -#}
    {%- if item.NGLANSWITCH is not none -%}
        NGLANSWITCH={{item.NGLANSWITCH}},
    {%- endif -%}
    {%- if item.VNGROUPDATASW is not none -%}
        VNGROUPDATASW={{item.VNGROUPDATASW}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 2 //配置对5G LAN UPF的选择机制。

```jinja2
{%- for item in set_upselectflag_list -%}
    SET UPSELECTFLAG:
    {#- --- 可选参数 --- -#}
    {%- if item.NGLANUPFSELSW is not none -%}
        NGLANUPFSELSW={{item.NGLANUPFSELSW}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 //配置对端UPF支持5G LAN。

```jinja2
{%- for item in mod_upnode_list -%}
    MOD UPNODE:
    {#- --- 必选参数 --- -#}
    NFINSTANCENAME="{{item.NFINSTANCENAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.NGLANSW is not none -%}
        NGLANSW={{item.NGLANSW}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 //配置5G LAN关键信元。

```jinja2
{%- for item in set_pfcppvtext_list -%}
    SET PFCPPVTEXT:
    {#- --- 必选参数 --- -#}
    FEATURE={{item.FEATURE}},
    {#- --- 可选参数 --- -#}
    {%- if item.SWITCH is not none -%}
        SWITCH={{item.SWITCH}},
    {%- endif -%}
    ;
{%- endfor -%}
```


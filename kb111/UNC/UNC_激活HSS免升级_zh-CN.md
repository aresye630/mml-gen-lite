---
id: ''
name: 激活HSS免升级
ne_type: UNC
type: feature
description: 本操作指导介绍在运行网络中激活HSS免升级的操作过程。  在HSS未升级不支持NB-IoT终端接入、无法进行Non-IP数据传输的情况下，通过配置使MME发送给HSS可以识别的消息和信元，建立Non-IP的PDN上下文，保证NB-IoT终端成功接入网络，采用Non-IP Data Over NAS进行数据传输。  适用于MME。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","NB-IOT业务功能","WSFD-215301 HSS免升级","激活HSS免升级"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本操作指导介绍在运行网络中激活HSS免升级的操作过程。在HSS未升级不支持NB-IoT终端接入、无法进行Non-IP数据传输的情况下，通过配置使MME发送给HSS可以识别的消息和信元，建立Non-IP的PDN上下文，保证NB-IoT终端成功接入网络，采用Non-IP Data Over NAS进行数据传输。适用于MME。

## 必备事项
前提条件

* 请仔细阅读WSFD-215301 HSS免升级特性概述。
* 已完成加载License。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    set_dmcmpt_list:
      type: items
      properties:
        NBIOTRAT:
          name: '是否支持NB-IoT RAT'
          type: string
          enum:
          - NOT_SUPPORT
          - SUPPORT
          required: false
          description: 'S6a接口兼容性策略'
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_nonipsubctrl_list:
      type: items
      properties:
        SUBRANGE:
          name: '用户范围'
          type: string
          enum:
          - ALL_USER
          - IMSI_PREFIX
          required: true
          description: '增加Non-IP APNNI配置'
          data_source: '全网规划'
          pattern: ''
          default: ''
        IMSIPRE:
          name: 'IMSI前缀'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SUPAPNNI:
          name: '支持Non-IP的APNNI'
          type: string
          enum:
          - ALL_APNNI
          - SPECIAL_APNNI
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        APNNIGROUPID:
          name: 'APNNI组号'
          type: integer
          minimum: 0
          maximum: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DFTAPNNI:
          name: '缺省APNNI'
          type: string
          maxLength: 62
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
  examples:
    set_dmcmpt_list:
    - NBIOTRAT: NOT_SUPPORT
    add_nonipsubctrl_list:
    - SUBRANGE: IMSI_PREFIX
      IMSIPRE: '12303'
      SUPAPNNI: ALL_APNNI
      APNNIGROUPID: ''
      DFTAPNNI: ''
    set_licenseswitch_list:
    - LICITEM: 'LKV2HUNN01'
      SWITCH: ENABLE
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 进入“MML命令行-UNC”窗口。

### 2 配置S6a接口兼容性策略。

```jinja2
{%- for item in set_dmcmpt_list -%}
    SET DMCMPT:
    {#- --- 可选参数 --- -#}
    {%- if item.NBIOTRAT is not none -%}
        NBIOTRAT={{item.NBIOTRAT}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 **可选：**当HSS中未给用户签约Non-IP签约数据且需要使用Non-IP业务时，需要增加Non-IP APNNI配置。

```jinja2
{%- if is_optional_add_nonip_apnni_config -%}
    {%- for item in add_nonipsubctrl_list -%}
        ADD NONIPSUBCTRL:
        {#- --- 必选参数 --- -#}
        SUBRANGE={{item.SUBRANGE}},
        SUPAPNNI={{item.SUPAPNNI}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：SUBRANGE=IMSI_PREFIX 时必选 --- -#}
        {%- if item.SUBRANGE == 'IMSI_PREFIX' -%}
            IMSIPRE="{{item.IMSIPRE}}",
        {%- endif -%}
        {#- --- 条件必选：SUPAPNNI=SPECIAL_APNNI 时必选 --- -#}
        {%- if item.SUPAPNNI == 'SPECIAL_APNNI' -%}
            APNNIGROUPID={{item.APNNIGROUPID}},
        {%- endif -%}
        {#- --- 条件必选：SUPAPNNI=SPECIAL_APNNI 时必选 --- -#}
        {%- if item.SUPAPNNI == 'SPECIAL_APNNI' -%}
            DFTAPNNI="{{item.DFTAPNNI}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 当“SUPAPNNI”选为“SPECIAL\_APNNI”时，需要先通过**ADD APNNIGROUP**和**ADD APNNI**来绑定APNNI组。

### 4 打开本功能的License配置开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```


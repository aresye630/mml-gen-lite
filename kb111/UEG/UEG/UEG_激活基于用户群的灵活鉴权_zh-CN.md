---
id: GWFD-021510
name: 激活基于用户群的灵活鉴权
ne_type: UEG
type: feature
description: 本操作指导介绍在运行网络中激活基于用户群的灵活鉴权特性的操作过程。  通过基于用户群的灵活鉴权功能，UEG可以针对不同的用户群的属性使用差异化的安全策略。  适用于SGSN、MME。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝L","MEC 特性指南（风筝L）","MME特性指南","GWFD-021500 数据安全管理","GWFD-021510 基于用户群的灵活鉴权","激活基于用户群的灵活鉴权"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
本操作指导介绍在运行网络中激活基于用户群的灵活鉴权特性的操作过程。通过基于用户群的灵活鉴权功能，UEG可以针对不同的用户群的属性使用差异化的安全策略。适用于SGSN、MME。

## 必备事项
前提条件

* 请仔细阅读GWFD-021510 基于用户群的灵活鉴权特性概述。

* 安全功能被启用：
  + 在Gb模式下，将**ADD GBAUTHCIPH**命令中的"SECPLC"参数设置为"AUTHANDPROTECTED"或"AUTHONLY"。
  + 在Iu模式下，将**ADD IUAUTHCIPH**命令中的"SECPLC"参数设置为"AUTHANDPROTECTED"或"AUTHONLY"。
  + 在S1模式下，将**ADD S1USRSECPARA**命令中的"SECPLC"参数设置为"AUTHANDPROTECTED"；"OPTIONAL"参数设置为"YES"。

* 完成加载License。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
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
    add_gbauthciph_list:
      type: items
      properties:
        IMSIPRE:
          name: 'IMSI前缀'
          type: string
          maxLength: 15
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SECPLC:
          name: '安全策略'
          type: string
          enum:
          - AUTHANDPROTECTED
          - AUTHONLY
          - NEVER
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: AUTHANDPROTECTED
        AUTHEVENT:
          name: '鉴权事件'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AUTHEVENTTHRESHOLD:
          name: '鉴权事件上限'
          type: integer
          minimum: 0
          maximum: 1023
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 1
        AUTHPERIOD:
          name: '鉴权周期'
          type: integer
          minimum: 0
          maximum: 24
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: 24
    add_iuauthciph_list:
      type: items
      properties:
        IMSIPRE:
          name: 'IMSI前缀'
          type: string
          maxLength: 15
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SECPLC:
          name: '安全策略'
          type: string
          enum:
          - AUTHANDPROTECTED
          - AUTHONLY
          - NEVER
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: AUTHANDPROTECTED
        AUTHEVENT:
          name: '鉴权事件'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AUTHEVENTTHRESHOLD:
          name: '鉴权事件上限'
          type: integer
          minimum: 0
          maximum: 1023
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 1
        AUTHPERIOD:
          name: '鉴权周期'
          type: integer
          minimum: 0
          maximum: 24
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: 24
    add_s1usrsecpara_list:
      type: items
      properties:
        IMSIPRE:
          name: 'IMSI前缀'
          type: string
          maxLength: 15
          required: true
          description: '安全配置的相关参数'
          data_source: '全网规划'
          pattern: ''
          default: ''
        SECPLC:
          name: '安全策略'
          type: string
          enum:
          - AUTHANDPROTECTED
          - AUTHONLY
          - NEVER
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: AUTHANDPROTECTED
        OPTIONAL:
          name: '高级选项'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AUTHEVENT:
          name: '鉴权事件'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        AUTHEVENTTHRESHOLD:
          name: '鉴权事件上限'
          type: integer
          minimum: 0
          maximum: 1023
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: 1023
        AUTHPERIOD:
          name: '鉴权周期'
          type: integer
          minimum: 0
          maximum: 24
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: 24
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV2FLEXAUTH02'
      SWITCH: ENABLE
    add_gbauthciph_list:
    - IMSIPRE: '308010001'
      SECPLC: AUTHANDPROTECTED
      AUTHEVENT: PTMSI_ATTACH-1&IMSI_ATTACH-1
      AUTHEVENTTHRESHOLD: 3
      AUTHPERIOD: 24
    add_iuauthciph_list:
    - IMSIPRE: '308010000000001'
      SECPLC: AUTHANDPROTECTED
      AUTHEVENT: INTRA_RAU-1&IMSI_ATTACH-1
      AUTHEVENTTHRESHOLD: 2
      AUTHPERIOD: 24
    add_s1usrsecpara_list:
    - IMSIPRE: '30801'
      SECPLC: AUTHANDPROTECTED
      OPTIONAL: YES
      AUTHEVENT: ATTACH-1
      AUTHEVENTTHRESHOLD: 3
      AUTHPERIOD: 24
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 进入“MML命令行-UEG”窗口。

### 2 打开本特性的License配置开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

### 3 配置基于用户群的灵活鉴权策略。

#### 3.1 Gb模式下增加指定用户群的灵活鉴权策略。

```jinja2
{%- if is_scenario_gb_mode -%}
    {%- for item in add_gbauthciph_list -%}
        ADD GBAUTHCIPH:
        {#- --- 必选参数 --- -#}
        IMSIPRE="{{item.IMSIPRE}}",
        {#- --- 可选参数 --- -#}
        {%- if item.SECPLC is not none -%}
            SECPLC={{item.SECPLC}},
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：SECPLC=AUTHONLY/AUTHANDPROTECTED 时可选 --- -#}
        {%- if item.SECPLC in ['AUTHONLY', 'AUTHANDPROTECTED'] -%}
            {%- if item.AUTHEVENT is not none -%}
                AUTHEVENT={{item.AUTHEVENT}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：SECPLC=AUTHONLY/AUTHANDPROTECTED 时可选 --- -#}
        {%- if item.SECPLC in ['AUTHONLY', 'AUTHANDPROTECTED'] -%}
            {%- if item.AUTHEVENTTHRESHOLD is not none -%}
                AUTHEVENTTHRESHOLD={{item.AUTHEVENTTHRESHOLD}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：SECPLC=AUTHONLY/AUTHANDPROTECTED 时可选 --- -#}
        {%- if item.SECPLC in ['AUTHONLY', 'AUTHANDPROTECTED'] -%}
            {%- if item.AUTHPERIOD is not none -%}
                AUTHPERIOD={{item.AUTHPERIOD}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 3.2 Iu模式下增加指定用户群的灵活鉴权策略。

```jinja2
{%- if is_scenario_iu_mode -%}
    {%- for item in add_iuauthciph_list -%}
        ADD IUAUTHCIPH:
        {#- --- 必选参数 --- -#}
        IMSIPRE="{{item.IMSIPRE}}",
        {#- --- 可选参数 --- -#}
        {%- if item.SECPLC is not none -%}
            SECPLC={{item.SECPLC}},
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：SECPLC=AUTHONLY/AUTHANDPROTECTED 时可选 --- -#}
        {%- if item.SECPLC in ['AUTHONLY', 'AUTHANDPROTECTED'] -%}
            {%- if item.AUTHEVENT is not none -%}
                AUTHEVENT={{item.AUTHEVENT}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：SECPLC=AUTHONLY/AUTHANDPROTECTED 时可选 --- -#}
        {%- if item.SECPLC in ['AUTHONLY', 'AUTHANDPROTECTED'] -%}
            {%- if item.AUTHEVENTTHRESHOLD is not none -%}
                AUTHEVENTTHRESHOLD={{item.AUTHEVENTTHRESHOLD}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：SECPLC=AUTHONLY/AUTHANDPROTECTED 时可选 --- -#}
        {%- if item.SECPLC in ['AUTHONLY', 'AUTHANDPROTECTED'] -%}
            {%- if item.AUTHPERIOD is not none -%}
                AUTHPERIOD={{item.AUTHPERIOD}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 3.3 S1模式下增加指定用户群的灵活鉴权策略。

```jinja2
{%- if is_scenario_s1_mode -%}
    {%- for item in add_s1usrsecpara_list -%}
        ADD S1USRSECPARA:
        {#- --- 必选参数 --- -#}
        IMSIPRE="{{item.IMSIPRE}}",
        {#- --- 可选参数 --- -#}
        {%- if item.SECPLC is not none -%}
            SECPLC={{item.SECPLC}},
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：SECPLC=AUTHONLY/AUTHANDPROTECTED 时可选 --- -#}
        {%- if item.SECPLC in ['AUTHONLY', 'AUTHANDPROTECTED'] -%}
            {%- if item.OPTIONAL is not none -%}
                OPTIONAL={{item.OPTIONAL}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：OPTIONAL=YES 时可选 --- -#}
        {%- if item.OPTIONAL == 'YES' -%}
            {%- if item.AUTHEVENT is not none -%}
                AUTHEVENT={{item.AUTHEVENT}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：OPTIONAL=YES 时可选 --- -#}
        {%- if item.OPTIONAL == 'YES' -%}
            {%- if item.AUTHEVENTTHRESHOLD is not none -%}
                AUTHEVENTTHRESHOLD={{item.AUTHEVENTTHRESHOLD}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：OPTIONAL=YES 时可选 --- -#}
        {%- if item.OPTIONAL == 'YES' -%}
            {%- if item.AUTHPERIOD is not none -%}
                AUTHPERIOD={{item.AUTHPERIOD}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### ****ADD S1USRSECPARA****


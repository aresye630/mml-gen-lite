---
id: GWFD-026301
name: 激活eMTC终端省电PSM模式
ne_type: UEG
type: feature
description: 本操作指导介绍在运行网络中激活eMTC终端省电PSM模式的操作过程。  随着物联网的发展，eMTC（enhanced Machine-Type Communications）广泛应用于智能抄表等领域。这些领域的eMTC终端被置于某些固定位置，采用各种电池供电，这种情况对电池寿命要求较高。本特性可以在这类eMTC终端无上行数传时，指示终端进入PSM（Power Saving Mode）。终端进入PSM后MME将拒绝周边网元对终端的寻呼请求，达到省电的目的，从而提高电池的使用寿命。  适用于MME。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝L","MEC 特性指南（风筝L）","MME特性指南","GWFD-026300 eMTC基本功能","GWFD-026301 eMTC终端省电PSM模式","激活eMTC终端省电PSM模式"]
refs: []
metadata:
  DepOnLiveCfg: true
allowed-tools:
- getParameterValue('LST M2MPLCY')
---
<!-- @mml:block= annotations -->
```text
## 操作场景
本操作指导介绍在运行网络中激活eMTC终端省电PSM模式的操作过程。随着物联网的发展，eMTC（enhanced Machine-Type Communications）广泛应用于智能抄表等领域。这些领域的eMTC终端被置于某些固定位置，采用各种电池供电，这种情况对电池寿命要求较高。本特性可以在这类eMTC终端无上行数传时，指示终端进入PSM（Power Saving Mode）。终端进入PSM后MME将拒绝周边网元对终端的寻呼请求，达到省电的目的，从而提高电池的使用寿命。适用于MME。

## 必备事项
前提条件

* 请仔细阅读GWFD-026301 eMTC终端省电PSM模式特性概述。
* 已完成加载License。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    add_m2mplcy_list:
      type: items
      properties:
        SUBRANGE:
          name: '用户范围'
          type: string
          enum:
          - ALL_USER
          - FOREIGN_USER
          - HOME_USER
          - IMSI_PREFIX
          required: true
          description: '增加eMTC终端省电策略'
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
        APNNI:
          name: 'APNNI'
          type: string
          maxLength: 62
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PSMSW:
          name: 'PSM开关'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: OFF
        ACTIVETIMERSRC:
          name: 'Active Timer来源'
          type: string
          enum:
          - USE_CONFIG
          - USE_MAXRSPTM
          - USE_MAXRSPTM_OR_UEREQ
          - USE_UE_REQUEST
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: USE_CONFIG
        ACTIVETIMER:
          name: 'Active Timer定时器时长（秒）'
          type: integer
          minimum: 0
          maximum: 11160
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 180
        DELAYSEND:
          name: '延迟发送'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NO
    mod_m2mplcy_list:
      type: items
      properties:
        SUBRANGE:
          name: '用户范围'
          type: string
          enum:
          - ALL_USER
          - FOREIGN_USER
          - HOME_USER
          - IMSI_PREFIX
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        APNNI:
          name: 'APNNI'
          type: string
          maxLength: 62
          required: true
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
    add_m2mplcy_list:
    - SUBRANGE: IMSI_PREFIX
      IMSIPRE: '123033601'
      APNNI: 'HUAWEI1.com'
      PSMSW: ON
      ACTIVETIMERSRC: USE_CONFIG
      ACTIVETIMER: 180
      DELAYSEND: NO
    mod_m2mplcy_list:
    - SUBRANGE: ''
      APNNI: ''
    set_licenseswitch_list:
    - LICITEM: 'LKV2M2MS02'
      SWITCH: ENABLE
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 进入“MML命令行-UEG”窗口。

### 2 配置eMTC终端省电策略。

#### 2.1 查询某指定用户范围的省电策略配置。

#### 对于处于PSM态的终端，当有下行短消息时，MME会通知上游网元终端不可达。当终端进入连接态后，HSS给短消息中心发送Alert Service Request消息触发短消息重发流程，此时由于短消息中心向EPC核心网下发的短消息存在延时，可能出现短消息下发至终端时，终端又再一次进入PSM态，导致短消息一直发送失败。因此若存在下行短消息的场景，参数“ACTIVETIMER”时长的设置需要和短消息中心协商。

#### 2.2 **可选：**如果步骤a未查询到该指定用户范围的相关配置，则执行此步骤，为该用户范围新配置省电策略。

```jinja2
{%- set LST_M2MPLCY=getParameterValue('LST M2MPLCY') -%}
{%- if is_optional_add_power_saving_policy and LST_M2MPLCY=='' -%}
    {%- for item in add_m2mplcy_list -%}
        ADD M2MPLCY:
        {#- --- 必选参数 --- -#}
        SUBRANGE={{item.SUBRANGE}},
        APNNI="{{item.APNNI}}",
        {#- --- 可选参数 --- -#}
        {%- if item.PSMSW is not none -%}
            PSMSW={{item.PSMSW}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：SUBRANGE=IMSI_PREFIX 时必选 --- -#}
        {%- if item.SUBRANGE == 'IMSI_PREFIX' -%}
            IMSIPRE="{{item.IMSIPRE}}",
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：PSMSW=ON 时可选 --- -#}
        {%- if item.PSMSW == 'ON' -%}
            {%- if item.ACTIVETIMERSRC is not none -%}
                ACTIVETIMERSRC={{item.ACTIVETIMERSRC}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：ACTIVETIMERSRC=USE_CONFIG/USE_MAXRSPTM 时可选 --- -#}
        {%- if item.ACTIVETIMERSRC in ['USE_CONFIG', 'USE_MAXRSPTM'] -%}
            {%- if item.ACTIVETIMER is not none -%}
                ACTIVETIMER={{item.ACTIVETIMER}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PSMSW=ON 时可选 --- -#}
        {%- if item.PSMSW == 'ON' -%}
            {%- if item.DELAYSEND is not none -%}
                DELAYSEND={{item.DELAYSEND}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### Active Timer定时器时长必须小于Periodic TAU Timer (T3412/T3412 extended)转化为秒之后的时长。

#### 2.3 **可选：**如果步骤a查询到系统已存在该指定用户范围的相关配置，则执行此步骤，修改其原有省电策略。

```jinja2
{%- if is_optional_modify_power_saving_policy and LST_M2MPLCY -%}
    {%- for item in mod_m2mplcy_list -%}
        MOD M2MPLCY:
        {#- --- 必选参数 --- -#}
        APNNI="{{item.APNNI}}",
        SUBRANGE={{item.SUBRANGE}},
        ;
    {%- endfor -%}
{%- endif -%}
```

### 3 打开本功能的License配置开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```


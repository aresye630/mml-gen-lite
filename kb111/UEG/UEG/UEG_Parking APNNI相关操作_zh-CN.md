---
id: GWFD-020909
name: Parking APNNI相关操作
ne_type: UEG
type: feature
description: 本操作指导介绍在运行网络中为满足不同场景的需求，针对Parking APN所进行的操作过程。  * 场景1：设备PDN连接资源不足    当设备PDN连接资源不足时，系统需要暂时释放Parking APN所使用的PDN连接资源。 * 场景2：尽快恢复使用Parking APN激活功能的用户的各项业务。    当终端反复发送Attach Request、PDN Connectivity Request消息时，系统启用了Parking APN激活抑制措施。由于Parking APN不能进行数据业务，当用户需要使用Parking APN激活功能的各项业务时，需要帮助用户尽快恢复业务。 * 场景3：修改Parking APN    当系统Parking APN激活抑制措施已经开启并配置相应的Parking APN后，运营商可根据需要修改此Parking APN。  适用于MME。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝L","MEC 特性指南（风筝L）","MME特性指南","GWFD-020900 接入管理","GWFD-020909 LTE UE信令控制","Parking APNNI相关操作"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
本操作指导介绍在运行网络中为满足不同场景的需求，针对Parking APN所进行的操作过程。* 场景1：设备PDN连接资源不足  当设备PDN连接资源不足时，系统需要暂时释放Parking APN所使用的PDN连接资源。* 场景2：尽快恢复使用Parking APN激活功能的用户的各项业务。  当终端反复发送Attach Request、PDN Connectivity Request消息时，系统启用了Parking APN激活抑制措施。由于Parking APN不能进行数据业务，当用户需要使用Parking APN激活功能的各项业务时，需要帮助用户尽快恢复业务。* 场景3：修改Parking APN  当系统Parking APN激活抑制措施已经开启并配置相应的Parking APN后，运营商可根据需要修改此Parking APN。适用于MME。

## 必备事项
前提条件

* 已经加载支持Parking APN激活功能的License，对应的License项为“LTE UE信令控制”。
* Parking APN激活抑制措施已经开启，可调用****LST S1SMARTRULE****和****LST S1SMARTPLCY****命令查询“ATTACHCTRLRULE（附着抑制措施）”、“PDNCONNCTRLRULE（PDN连接抑制措施）”参数的配置。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    mod_s1smartrule_list:
      type: items
      properties:
        UETYPE:
          name: '终端类型'
          type: string
          enum:
          - ANDROID
          - BLACKBERRY
          - CUSTOM_TYPE_1
          - CUSTOM_TYPE_10
          - CUSTOM_TYPE_11
          - CUSTOM_TYPE_12
          - CUSTOM_TYPE_2
          - CUSTOM_TYPE_3
          - CUSTOM_TYPE_4
          - CUSTOM_TYPE_5
          - CUSTOM_TYPE_6
          - CUSTOM_TYPE_7
          - CUSTOM_TYPE_8
          - CUSTOM_TYPE_9
          - IOS
          - UNKNOWN_TYPE
          - WINDOWS
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ATTACHCTRLRULE:
          name: '附着抑制措施'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PDNCONNCTRLRULE:
          name: 'PDN连接抑制措施'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    mod_s1smartplcy_list:
      type: items
      properties:
        SUBRANGE:
          name: '用户范围'
          type: string
          enum:
          - IMSI_PREFIX
          - MSISDN_PREFIX
          required: true
          description: ''
          data_source: ''
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
        ATTACHCTRLRULE:
          name: '附着抑制措施'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PDNCONNCTRLRULE:
          name: 'PDN连接抑制措施'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    mod_s1smartrule_list_1:
      type: items
      properties:
        UETYPE:
          name: '终端类型'
          type: string
          enum:
          - ANDROID
          - BLACKBERRY
          - CUSTOM_TYPE_1
          - CUSTOM_TYPE_10
          - CUSTOM_TYPE_11
          - CUSTOM_TYPE_12
          - CUSTOM_TYPE_2
          - CUSTOM_TYPE_3
          - CUSTOM_TYPE_4
          - CUSTOM_TYPE_5
          - CUSTOM_TYPE_6
          - CUSTOM_TYPE_7
          - CUSTOM_TYPE_8
          - CUSTOM_TYPE_9
          - IOS
          - UNKNOWN_TYPE
          - WINDOWS
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ATTACHCTRLRULE:
          name: '附着抑制措施'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PDNCONNCTRLRULE:
          name: 'PDN连接抑制措施'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    mod_s1smartplcy_list_1:
      type: items
      properties:
        SUBRANGE:
          name: '用户范围'
          type: string
          enum:
          - IMSI_PREFIX
          - MSISDN_PREFIX
          required: true
          description: ''
          data_source: ''
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
        ATTACHCTRLRULE:
          name: '附着抑制措施'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PDNCONNCTRLRULE:
          name: 'PDN连接抑制措施'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    mod_s1smartrule_list_2:
      type: items
      properties:
        UETYPE:
          name: '终端类型'
          type: string
          enum:
          - ANDROID
          - BLACKBERRY
          - CUSTOM_TYPE_1
          - CUSTOM_TYPE_10
          - CUSTOM_TYPE_11
          - CUSTOM_TYPE_12
          - CUSTOM_TYPE_2
          - CUSTOM_TYPE_3
          - CUSTOM_TYPE_4
          - CUSTOM_TYPE_5
          - CUSTOM_TYPE_6
          - CUSTOM_TYPE_7
          - CUSTOM_TYPE_8
          - CUSTOM_TYPE_9
          - IOS
          - UNKNOWN_TYPE
          - WINDOWS
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ATTACHCTRLRULE:
          name: '附着抑制措施'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PDNCONNCTRLRULE:
          name: 'PDN连接抑制措施'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    mod_s1smartplcy_list_2:
      type: items
      properties:
        SUBRANGE:
          name: '用户范围'
          type: string
          enum:
          - IMSI_PREFIX
          - MSISDN_PREFIX
          required: true
          description: ''
          data_source: ''
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
        ATTACHCTRLRULE:
          name: '附着抑制措施'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PDNCONNCTRLRULE:
          name: 'PDN连接抑制措施'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    mod_s1smartrule_list_3:
      type: items
      properties:
        UETYPE:
          name: '终端类型'
          type: string
          enum:
          - ANDROID
          - BLACKBERRY
          - CUSTOM_TYPE_1
          - CUSTOM_TYPE_10
          - CUSTOM_TYPE_11
          - CUSTOM_TYPE_12
          - CUSTOM_TYPE_2
          - CUSTOM_TYPE_3
          - CUSTOM_TYPE_4
          - CUSTOM_TYPE_5
          - CUSTOM_TYPE_6
          - CUSTOM_TYPE_7
          - CUSTOM_TYPE_8
          - CUSTOM_TYPE_9
          - IOS
          - UNKNOWN_TYPE
          - WINDOWS
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ATTACHCTRLRULE:
          name: '附着抑制措施'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PDNCONNCTRLRULE:
          name: 'PDN连接抑制措施'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    mod_s1smartplcy_list_3:
      type: items
      properties:
        SUBRANGE:
          name: '用户范围'
          type: string
          enum:
          - IMSI_PREFIX
          - MSISDN_PREFIX
          required: true
          description: ''
          data_source: ''
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
        ATTACHCTRLRULE:
          name: '附着抑制措施'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PDNCONNCTRLRULE:
          name: 'PDN连接抑制措施'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    mod_s1smartrule_list_4:
      type: items
      properties:
        UETYPE:
          name: '终端类型'
          type: string
          enum:
          - ANDROID
          - BLACKBERRY
          - CUSTOM_TYPE_1
          - CUSTOM_TYPE_10
          - CUSTOM_TYPE_11
          - CUSTOM_TYPE_12
          - CUSTOM_TYPE_2
          - CUSTOM_TYPE_3
          - CUSTOM_TYPE_4
          - CUSTOM_TYPE_5
          - CUSTOM_TYPE_6
          - CUSTOM_TYPE_7
          - CUSTOM_TYPE_8
          - CUSTOM_TYPE_9
          - IOS
          - UNKNOWN_TYPE
          - WINDOWS
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ATTACHCTRLRULE:
          name: '附着抑制措施'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PDNCONNCTRLRULE:
          name: 'PDN连接抑制措施'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    mod_s1smartplcy_list_4:
      type: items
      properties:
        SUBRANGE:
          name: '用户范围'
          type: string
          enum:
          - IMSI_PREFIX
          - MSISDN_PREFIX
          required: true
          description: ''
          data_source: ''
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
        ATTACHCTRLRULE:
          name: '附着抑制措施'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PDNCONNCTRLRULE:
          name: 'PDN连接抑制措施'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_s1smartpara_list:
      type: items
      properties:
        PARKINGAPN:
          name: 'Parking APN'
          type: string
          maxLength: 62
          required: false
          description: 'Parking APN'
          data_source: '全网规划'
          pattern: ''
          default: ''
    mod_s1smartplcy_list_5:
      type: items
      properties:
        SUBRANGE:
          name: '用户范围'
          type: string
          enum:
          - IMSI_PREFIX
          - MSISDN_PREFIX
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    mod_s1smartrule_list_5:
      type: items
      properties:
        UETYPE:
          name: '终端类型'
          type: string
          enum:
          - ANDROID
          - BLACKBERRY
          - CUSTOM_TYPE_1
          - CUSTOM_TYPE_10
          - CUSTOM_TYPE_11
          - CUSTOM_TYPE_12
          - CUSTOM_TYPE_2
          - CUSTOM_TYPE_3
          - CUSTOM_TYPE_4
          - CUSTOM_TYPE_5
          - CUSTOM_TYPE_6
          - CUSTOM_TYPE_7
          - CUSTOM_TYPE_8
          - CUSTOM_TYPE_9
          - IOS
          - UNKNOWN_TYPE
          - WINDOWS
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ATTACHCTRLRULE:
          name: '附着抑制措施'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PDNCONNCTRLRULE:
          name: 'PDN连接抑制措施'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    mod_s1smartplcy_list_6:
      type: items
      properties:
        SUBRANGE:
          name: '用户范围'
          type: string
          enum:
          - IMSI_PREFIX
          - MSISDN_PREFIX
          required: true
          description: ''
          data_source: ''
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
        ATTACHCTRLRULE:
          name: '附着抑制措施'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PDNCONNCTRLRULE:
          name: 'PDN连接抑制措施'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    mod_s1smartrule_list:
    - UETYPE: ANDROID
      ATTACHCTRLRULE: PARKAPNACT-0
      PDNCONNCTRLRULE: PARKAPNACT-0
    mod_s1smartplcy_list:
    - SUBRANGE: IMSI_PREFIX
      IMSIPRE: '1230301'
      ATTACHCTRLRULE: =PARKAPNACT-0
      PDNCONNCTRLRULE: PARKAPNACT-0
    mod_s1smartrule_list_1:
    - UETYPE: ANDROID
      ATTACHCTRLRULE: PARKAPNACT-1
      PDNCONNCTRLRULE: PARKAPNACT-1
    mod_s1smartplcy_list_1:
    - SUBRANGE: IMSI_PREFIX
      IMSIPRE: '1230301'
      ATTACHCTRLRULE: =PARKAPNACT-1
      PDNCONNCTRLRULE: PARKAPNACT-1
    mod_s1smartrule_list_2:
    - UETYPE: ANDROID
      ATTACHCTRLRULE: PARKAPNACT-0
      PDNCONNCTRLRULE: PARKAPNACT-0
    mod_s1smartplcy_list_2:
    - SUBRANGE: IMSI_PREFIX
      IMSIPRE: '1230301'
      ATTACHCTRLRULE: =PARKAPNACT-0
      PDNCONNCTRLRULE: PARKAPNACT-0
    mod_s1smartrule_list_3:
    - UETYPE: ANDROID
      ATTACHCTRLRULE: PARKAPNACT-1
      PDNCONNCTRLRULE: PARKAPNACT-1
    mod_s1smartplcy_list_3:
    - SUBRANGE: IMSI_PREFIX
      IMSIPRE: '1230301'
      ATTACHCTRLRULE: =PARKAPNACT-1
      PDNCONNCTRLRULE: PARKAPNACT-1
    mod_s1smartrule_list_4:
    - UETYPE: ANDROID
      ATTACHCTRLRULE: PARKAPNACT-0
      PDNCONNCTRLRULE: PARKAPNACT-0
    mod_s1smartplcy_list_4:
    - SUBRANGE: IMSI_PREFIX
      IMSIPRE: '1230301'
      ATTACHCTRLRULE: =PARKAPNACT-0
      PDNCONNCTRLRULE: PARKAPNACT-0
    set_s1smartpara_list:
    - PARKINGAPN: 'huawei2.com'
    mod_s1smartplcy_list_5:
    - SUBRANGE: ''
    mod_s1smartrule_list_5:
    - UETYPE: ANDROID
      ATTACHCTRLRULE: PARKAPNACT-1
      PDNCONNCTRLRULE: PARKAPNACT-1
    mod_s1smartplcy_list_6:
    - SUBRANGE: IMSI_PREFIX
      IMSIPRE: '1230301'
      ATTACHCTRLRULE: =PARKAPNACT-1
      PDNCONNCTRLRULE: PARKAPNACT-1
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 进入“MML命令行-UEG”窗口。

### 2 * **场景1：设备PDN连接资源不足。**

#### 2.1 关闭所有终端类型的Parking APN激活抑制措施。

```jinja2
{%- if is_scenario_pdn_resource_insufficient -%}
    {%- for item in mod_s1smartrule_list -%}
        MOD S1SMARTRULE:
        {#- --- 必选参数 --- -#}
        UETYPE={{item.UETYPE}},
        {#- --- 可选参数 --- -#}
        {%- if item.ATTACHCTRLRULE is not none -%}
            ATTACHCTRLRULE={{item.ATTACHCTRLRULE}},
        {%- endif -%}
        {%- if item.PDNCONNCTRLRULE is not none -%}
            PDNCONNCTRLRULE={{item.PDNCONNCTRLRULE}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 只有“ATTACHCTRLRULE（附着抑制措施）”和“PDNCONNCTRLRULE（PDN连接抑制措施）”可以配置“Parking APN激活”抑制措施。

#### 2.2 关闭基于指定用户范围的Parking APN激活抑制措施。

```jinja2
{%- if is_scenario_pdn_resource_insufficient -%}
    {%- for item in mod_s1smartplcy_list -%}
        MOD S1SMARTPLCY:
        {#- --- 必选参数 --- -#}
        SUBRANGE={{item.SUBRANGE}},
        {#- --- 可选参数 --- -#}
        {%- if item.ATTACHCTRLRULE is not none -%}
            ATTACHCTRLRULE={{item.ATTACHCTRLRULE}},
        {%- endif -%}
        {%- if item.PDNCONNCTRLRULE is not none -%}
            PDNCONNCTRLRULE={{item.PDNCONNCTRLRULE}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：SUBRANGE=IMSI_PREFIX 时必选 --- -#}
        {%- if item.SUBRANGE == 'IMSI_PREFIX' -%}
            IMSIPRE="{{item.IMSIPRE}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 2.3 在UDG上去激活使用Parking APN的PDN连接，使Parking APN的PDN连接数目为零。

#### 2.4 **可选：**PDN连接资源问题（例如完成设备PDN连接扩容）解决后，可以开启Parking APN激活抑制措施。

#### 如果需要对发送异常Attach Request、PDN Connectivity Request消息的终端继续采用Parking APN激活抑制措施，则执行此步骤。

```jinja2
{%- if is_optional_enable_parking_apn_suppression and is_scenario_pdn_resource_insufficient -%}
    {%- for item in mod_s1smartrule_list_1 -%}
        MOD S1SMARTRULE:
        {#- --- 必选参数 --- -#}
        UETYPE={{item.UETYPE}},
        {#- --- 可选参数 --- -#}
        {%- if item.ATTACHCTRLRULE is not none -%}
            ATTACHCTRLRULE={{item.ATTACHCTRLRULE}},
        {%- endif -%}
        {%- if item.PDNCONNCTRLRULE is not none -%}
            PDNCONNCTRLRULE={{item.PDNCONNCTRLRULE}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_optional_enable_parking_apn_suppression and is_scenario_pdn_resource_insufficient -%}
    {%- for item in mod_s1smartplcy_list_1 -%}
        MOD S1SMARTPLCY:
        {#- --- 必选参数 --- -#}
        SUBRANGE={{item.SUBRANGE}},
        {#- --- 可选参数 --- -#}
        {%- if item.ATTACHCTRLRULE is not none -%}
            ATTACHCTRLRULE={{item.ATTACHCTRLRULE}},
        {%- endif -%}
        {%- if item.PDNCONNCTRLRULE is not none -%}
            PDNCONNCTRLRULE={{item.PDNCONNCTRLRULE}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：SUBRANGE=IMSI_PREFIX 时必选 --- -#}
        {%- if item.SUBRANGE == 'IMSI_PREFIX' -%}
            IMSIPRE="{{item.IMSIPRE}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 3 * **场景2：尽快恢复使用Parking APN激活功能的用户的各项业务。**

#### 3.1 关闭所有终端类型的Parking APN激活抑制措施，具体步骤请参考场景1中的步骤 1。

```jinja2
{%- if is_scenario_restore_business -%}
    {%- for item in mod_s1smartrule_list_2 -%}
        MOD S1SMARTRULE:
        {#- --- 必选参数 --- -#}
        UETYPE={{item.UETYPE}},
        {#- --- 可选参数 --- -#}
        {%- if item.ATTACHCTRLRULE is not none -%}
            ATTACHCTRLRULE={{item.ATTACHCTRLRULE}},
        {%- endif -%}
        {%- if item.PDNCONNCTRLRULE is not none -%}
            PDNCONNCTRLRULE={{item.PDNCONNCTRLRULE}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 3.2 关闭基于指定用户范围的Parking APN激活抑制措施。

```jinja2
{%- if is_scenario_restore_business -%}
    {%- for item in mod_s1smartplcy_list_2 -%}
        MOD S1SMARTPLCY:
        {#- --- 必选参数 --- -#}
        SUBRANGE={{item.SUBRANGE}},
        {#- --- 可选参数 --- -#}
        {%- if item.ATTACHCTRLRULE is not none -%}
            ATTACHCTRLRULE={{item.ATTACHCTRLRULE}},
        {%- endif -%}
        {%- if item.PDNCONNCTRLRULE is not none -%}
            PDNCONNCTRLRULE={{item.PDNCONNCTRLRULE}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：SUBRANGE=IMSI_PREFIX 时必选 --- -#}
        {%- if item.SUBRANGE == 'IMSI_PREFIX' -%}
            IMSIPRE="{{item.IMSIPRE}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 3.3 在UDG上去激活使用Parking APN的PDN连接，使Parking APN的PDN连接数目为零。

#### 3.4 **可选：**大量用户业务恢复正常（例如1小时后）后，开启各终端类型Attach Request、PDN Connectivity Request消息的Parking APN激活抑制措施，具体步骤请参考场景中1的步骤 4。

```jinja2
{%- if is_optional_enable_parking_apn_suppression and is_scenario_restore_business -%}
    {%- for item in mod_s1smartrule_list_3 -%}
        MOD S1SMARTRULE:
        {#- --- 必选参数 --- -#}
        UETYPE={{item.UETYPE}},
        {#- --- 可选参数 --- -#}
        {%- if item.ATTACHCTRLRULE is not none -%}
            ATTACHCTRLRULE={{item.ATTACHCTRLRULE}},
        {%- endif -%}
        {%- if item.PDNCONNCTRLRULE is not none -%}
            PDNCONNCTRLRULE={{item.PDNCONNCTRLRULE}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_optional_enable_parking_apn_suppression and is_scenario_restore_business -%}
    {%- for item in mod_s1smartplcy_list_3 -%}
        MOD S1SMARTPLCY:
        {#- --- 必选参数 --- -#}
        SUBRANGE={{item.SUBRANGE}},
        {#- --- 可选参数 --- -#}
        {%- if item.ATTACHCTRLRULE is not none -%}
            ATTACHCTRLRULE={{item.ATTACHCTRLRULE}},
        {%- endif -%}
        {%- if item.PDNCONNCTRLRULE is not none -%}
            PDNCONNCTRLRULE={{item.PDNCONNCTRLRULE}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：SUBRANGE=IMSI_PREFIX 时必选 --- -#}
        {%- if item.SUBRANGE == 'IMSI_PREFIX' -%}
            IMSIPRE="{{item.IMSIPRE}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 4 * **场景3：修改Parking APN。**

#### 4.1 关闭所有终端类型的Parking APN激活抑制措施，具体步骤请参考场景1中的步骤 1。

```jinja2
{%- if is_scenario_modify_parking_apn -%}
    {%- for item in mod_s1smartrule_list_4 -%}
        MOD S1SMARTRULE:
        {#- --- 必选参数 --- -#}
        UETYPE={{item.UETYPE}},
        {#- --- 可选参数 --- -#}
        {%- if item.ATTACHCTRLRULE is not none -%}
            ATTACHCTRLRULE={{item.ATTACHCTRLRULE}},
        {%- endif -%}
        {%- if item.PDNCONNCTRLRULE is not none -%}
            PDNCONNCTRLRULE={{item.PDNCONNCTRLRULE}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 4.2 关闭基于指定用户范围的Parking APN激活抑制措施。

```jinja2
{%- if is_scenario_modify_parking_apn -%}
    {%- for item in mod_s1smartplcy_list_4 -%}
        MOD S1SMARTPLCY:
        {#- --- 必选参数 --- -#}
        SUBRANGE={{item.SUBRANGE}},
        {#- --- 可选参数 --- -#}
        {%- if item.ATTACHCTRLRULE is not none -%}
            ATTACHCTRLRULE={{item.ATTACHCTRLRULE}},
        {%- endif -%}
        {%- if item.PDNCONNCTRLRULE is not none -%}
            PDNCONNCTRLRULE={{item.PDNCONNCTRLRULE}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：SUBRANGE=IMSI_PREFIX 时必选 --- -#}
        {%- if item.SUBRANGE == 'IMSI_PREFIX' -%}
            IMSIPRE="{{item.IMSIPRE}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 4.3 在UDG上去激活使用Parking APN的PDN连接，使Parking APN的PDN连接数目为零。

#### 4.4 修改UEG的Parking APN。

```jinja2
{%- if is_scenario_modify_parking_apn -%}
    {%- for item in set_s1smartpara_list -%}
        SET S1SMARTPARA:
        {#- --- 可选参数 --- -#}
        {%- if item.PARKINGAPN is not none -%}
            PARKINGAPN="{{item.PARKINGAPN}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_modify_parking_apn -%}
    {%- for item in mod_s1smartplcy_list_5 -%}
        MOD S1SMARTPLCY:
        {#- --- 必选参数 --- -#}
        SUBRANGE={{item.SUBRANGE}},
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 4.5 修改UDG的Parking APN。

#### 4.6 **可选：**开启Parking APN激活抑制措施，具体步骤请参考场景1中的步骤 4。

```jinja2
{%- if is_optional_enable_parking_apn_suppression and is_scenario_modify_parking_apn -%}
    {%- for item in mod_s1smartrule_list_5 -%}
        MOD S1SMARTRULE:
        {#- --- 必选参数 --- -#}
        UETYPE={{item.UETYPE}},
        {#- --- 可选参数 --- -#}
        {%- if item.ATTACHCTRLRULE is not none -%}
            ATTACHCTRLRULE={{item.ATTACHCTRLRULE}},
        {%- endif -%}
        {%- if item.PDNCONNCTRLRULE is not none -%}
            PDNCONNCTRLRULE={{item.PDNCONNCTRLRULE}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_optional_enable_parking_apn_suppression and is_scenario_modify_parking_apn -%}
    {%- for item in mod_s1smartplcy_list_6 -%}
        MOD S1SMARTPLCY:
        {#- --- 必选参数 --- -#}
        SUBRANGE={{item.SUBRANGE}},
        {#- --- 可选参数 --- -#}
        {%- if item.ATTACHCTRLRULE is not none -%}
            ATTACHCTRLRULE={{item.ATTACHCTRLRULE}},
        {%- endif -%}
        {%- if item.PDNCONNCTRLRULE is not none -%}
            PDNCONNCTRLRULE={{item.PDNCONNCTRLRULE}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：SUBRANGE=IMSI_PREFIX 时必选 --- -#}
        {%- if item.SUBRANGE == 'IMSI_PREFIX' -%}
            IMSIPRE="{{item.IMSIPRE}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```


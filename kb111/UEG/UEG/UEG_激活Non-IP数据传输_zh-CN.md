---
id: GWFD-026107
name: 激活Non-IP数据传输
ne_type: UEG
type: feature
description: 本操作指导介绍在运行网络中激活Non-IP数据传输的操作过程。  本特性支持NB-IoT（Narrow Band Internet of Things）制式UE通过NB-IoT RAN接入MME后，建立Non-IP的PDN上下文，并采用Non-IP进行数据传输，从而减小传送数据包大小，提高传输效率和空口容量。  适用于MME。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝L","MEC 特性指南（风筝L）","MME特性指南","GWFD-026100 NB-IoT基本功能","GWFD-026107 Non-IP数据传输（MME）","激活Non-IP数据传输"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
本操作指导介绍在运行网络中激活Non-IP数据传输的操作过程。本特性支持NB-IoT（Narrow Band Internet of Things）制式UE通过NB-IoT RAN接入MME后，建立Non-IP的PDN上下文，并采用Non-IP进行数据传输，从而减小传送数据包大小，提高传输效率和空口容量。适用于MME。

## 必备事项
前提条件

* 请仔细阅读GWFD-026107 Non-IP数据传输特性概述（MME）。
* 已按照配置到S-GW的数据完成S11-U接口的配置。
* 完成加载License。
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
          description: '增加M2M的策略参数，即为不同范围的用户、不同的APN业务配置M2M业务相关参数，以满足运营商灵活部署网络的需求。'
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
        CPOPSW:
          name: 'CP优化功能'
          type: string
          enum:
          - NOT_SUPPORT
          - SUPPORT
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NOT_SUPPORT
    set_dmcmpt_list:
      type: items
      properties:
        SF2:
          name: '特性列表2'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NBIOTRAT:
          name: '是否支持NBIoT RAT'
          type: string
          enum:
          - NOT_SUPPORT
          - SUPPORT
          required: false
          description: '设置Diameter兼容性。'
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
          description: '配置支持激活Non-IP类型PDN的APNNI。'
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
    add_mmecharact_list:
      type: items
      properties:
        RANGE:
          name: '对端设备范围'
          type: string
          enum:
          - ALL_MME
          - COMB_AMF
          - SPECIAL_MME
          required: true
          description: '增加MME属性配置信息。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        CIOTIND:
          name: 'CIoT优化支持指示'
          type: string
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
    add_m2mplcy_list:
    - SUBRANGE: IMSI_PREFIX
      IMSIPRE: '12303'
      APNNI: 'huawei.com'
      CPOPSW: SUPPORT
    set_dmcmpt_list:
    - SF2: FLSTID2_BIT21-1
      NBIOTRAT: SUPPORT
    add_nonipsubctrl_list:
    - SUBRANGE: IMSI_PREFIX
      IMSIPRE: '12303'
      SUPAPNNI: ALL_APNNI
    add_mmecharact_list:
    - RANGE: ALL_MME
      CIOTIND: SGNIPDN-1
    set_licenseswitch_list:
    - LICITEM: 'LKV2NOIP01'
      SWITCH: ENABLE
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 进入“MML命令行-UEG”窗口。

### 2 增加M2M策略参数。

```jinja2
{%- for item in add_m2mplcy_list -%}
    ADD M2MPLCY:
    {#- --- 必选参数 --- -#}
    SUBRANGE={{item.SUBRANGE}},
    APNNI="{{item.APNNI}}",
    {#- --- 可选参数 --- -#}
    {%- if item.CPOPSW is not none -%}
        CPOPSW={{item.CPOPSW}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：SUBRANGE=IMSI_PREFIX 时必选 --- -#}
    {%- if item.SUBRANGE == 'IMSI_PREFIX' -%}
        IMSIPRE="{{item.IMSIPRE}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 （可选）设置Diameter兼容性。

```jinja2
{%- if is_optional_diameter_compatibility -%}
    {%- for item in set_dmcmpt_list -%}
        SET DMCMPT:
        {#- --- 可选参数 --- -#}
        {%- if item.SF2 is not none -%}
            SF2={{item.SF2}},
        {%- endif -%}
        {%- if item.NBIOTRAT is not none -%}
            NBIOTRAT={{item.NBIOTRAT}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 4 （可选）当HSS中未给用户签约Non-IP签约数据且需要使用Non-IP业务时，需要增加Non-IP APNNI配置。

```jinja2
{%- if is_optional_non_ip_apnni_config -%}
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
        ;
    {%- endfor -%}
{%- endif -%}
```

### 当开启WSFD-215301 HSS免升级时，**ADD NONIPSUBCTRL**生效。

### 当“SUPAPNNI”选为“SPECIAL\_APNNI”时，需要先通过**ADD APNNIGROUP**和**ADD APNNI**来绑定APNNI组。

### 签约数据匹配时，如果UE未携带请求的APN NI，系统将使用签约的Non-IP Default APN作为该PDN的APN NI。

### 5 （可选）当用户发生Inter MME移动，且目标MME支持Non-IP数据传输时，需要增加MME属性配置信息。

```jinja2
{%- if is_optional_mme_attribute_config -%}
    {%- for item in add_mmecharact_list -%}
        ADD MMECHARACT:
        {#- --- 必选参数 --- -#}
        RANGE={{item.RANGE}},
        {#- --- 可选参数 --- -#}
        {%- if item.CIOTIND is not none -%}
            CIOTIND={{item.CIOTIND}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 6 打开本功能的License配置开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```


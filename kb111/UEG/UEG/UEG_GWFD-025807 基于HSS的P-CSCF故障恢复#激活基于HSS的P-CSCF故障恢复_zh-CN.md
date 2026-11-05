---
id: GWFD-025807
name: 激活基于HSS的P-CSCF故障恢复
ne_type: UEG
type: feature
description: 本操作指导介绍在运行网络中激活基于HSS的P-CSCF故障恢复的操作过程。  适用于MME。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝L","MEC 特性指南（风筝L）","MME特性指南","GWFD-025800 UDM语音基本功能","GWFD-025807 基于HSS的P-CSCF故障恢复","激活基于HSS的P-CSCF故障恢复"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
本操作指导介绍在运行网络中激活基于HSS的P-CSCF故障恢复的操作过程。适用于MME。

## 必备事项
前提条件

* 请仔细阅读GWFD-025807 基于HSS的P-CSCF故障恢复特性概述。
* 已完成加载License。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
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
    set_cpglobalims_list:
      type: items
      properties:
        UDMPCSCF:
          name: '基于UDM的P-CSCF Restoration功能开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        UDMPCSCFMODE:
          name: '基于UDM的P-CSCF Restoration功能模式'
          type: string
          enum:
          - PDUREACTIVATE
          - PCSCFADDRUPDATE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_dmcmptbyimsi_list:
      type: items
      properties:
        SUBRANGE:
          name: '用户范围'
          type: string
          enum:
          - FOREIGN_USER
          - HOME_USER
          - IMSI_PREFIX
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NOID:
          name: '运营商标识'
          type: integer
          minimum:
          - 0
          - 128
          maximum:
          - 64
          - 254
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SF2:
          name: '特性列表2'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_dmcmptbyimsi_list_1:
      type: items
      properties:
        SUBRANGE:
          name: '用户范围'
          type: string
          enum:
          - FOREIGN_USER
          - HOME_USER
          - IMSI_PREFIX
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
        SF2:
          name: '特性列表2'
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
    clr_hssinfo_list:
      type: items
      properties:
        HSSHTNAME:
          name: 'HSS主机名'
          type: string
          maxLength: 127
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    set_dmcmpt_list:
    - SF2: FLSTID2_BIT16-1
    set_cpglobalims_list:
    - UDMPCSCF: ENABLE
      UDMPCSCFMODE: PDUREACTIVATE
    add_dmcmptbyimsi_list:
    - SUBRANGE: HOME_USER
      NOID: 0
      SF2: FLSTID2_BIT16-1
    add_dmcmptbyimsi_list_1:
    - SUBRANGE: IMSI_PREFIX
      IMSIPRE: '46123'
      SF2: FLSTID2_BIT16-1
    set_licenseswitch_list:
    - LICITEM: 'LKV2FRPH02'
      SWITCH: ENABLE
    clr_hssinfo_list:
    - HSSHTNAME: 'hss.epc.mnc456.mcc123.3gppnetwork.org'
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 进入“MML命令行-UEG”窗口。

### 2 配置支持基于HSS的P-CSCF故障恢复特性。

```jinja2
{%- if is_scenario_all_hss_support -%}
    {%- for item in set_dmcmpt_list -%}
        SET DMCMPT:
        {#- --- 可选参数 --- -#}
        {%- if item.SF2 is not none -%}
            SF2={{item.SF2}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- for item in set_cpglobalims_list -%}
    SET CPGLOBALIMS:
    {#- --- 可选参数 --- -#}
    {%- if item.UDMPCSCF is not none -%}
        UDMPCSCF={{item.UDMPCSCF}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：UDMPCSCF=ENABLE 时可选 --- -#}
    {%- if item.UDMPCSCF == 'ENABLE' -%}
        {%- if item.UDMPCSCFMODE is not none -%}
            UDMPCSCFMODE={{item.UDMPCSCFMODE}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- if is_scenario_local_hss_support -%}
    {%- for item in add_dmcmptbyimsi_list -%}
        ADD DMCMPTBYIMSI:
        {#- --- 必选参数 --- -#}
        SUBRANGE={{item.SUBRANGE}},
        {#- --- 可选参数 --- -#}
        {%- if item.SF2 is not none -%}
            SF2={{item.SF2}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：SUBRANGE=FOREIGN_USER/HOME_USER 时必选 --- -#}
        {%- if item.SUBRANGE in ['FOREIGN_USER', 'HOME_USER'] -%}
            NOID={{item.NOID}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_imsi_prefix_hss_support -%}
    {%- for item in add_dmcmptbyimsi_list_1 -%}
        ADD DMCMPTBYIMSI:
        {#- --- 必选参数 --- -#}
        SUBRANGE={{item.SUBRANGE}},
        {#- --- 可选参数 --- -#}
        {%- if item.SF2 is not none -%}
            SF2={{item.SF2}},
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

### 命令**SET DMCMPT**和**ADD DMCMPTBYIMSI**中除“用户范围”、“运营商标识”以及“IMSI前缀”外的其余参数功能均相同，且若系统中同时存在这两条命令的配置，系统会优先匹配命令**ADD DMCMPTBYIMSI**的配置。因此在配置**ADD DMCMPTBYIMSI**前需先执行**LST DMCMPT**查询系统中**SET DMCMPT**的配置记录，确保命令**ADD DMCMPTBYIMSI**的配置记录中所携带的参数默认值不影响系统已有配置。

### 3 打开本特性的License配置开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

### 4 **可选：**清除HSS信息。

```jinja2
{%- if is_optional_clear_hss_info -%}
    {%- for item in clr_hssinfo_list -%}
        CLR HSSINFO:
        {#- --- 必选参数 --- -#}
        HSSHTNAME="{{item.HSSHTNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

### 根据3GPP 23.380定义，只要有一个用户通过Update Location Request消息通知HSS MME支持P-CSCF Restoration特性，HSS即认为整个MME支持此特性。如果HSS实现符合协议定义，则无需执行本步骤。


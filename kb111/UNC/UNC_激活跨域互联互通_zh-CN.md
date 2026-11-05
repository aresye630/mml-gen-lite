---
id: ''
name: 激活跨域互联互通
ne_type: UNC
type: feature
description: 本操作指导介绍在运行网络中，UE进行跨区域移动，所在区域超出了原来SMF的服务范围的场景下，保证UE会话业务连续性的操作过程。  适用于AMF、SMF。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","漫游管理功能","WSFD-205012 跨域互联互通","激活跨域互联互通"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本操作指导介绍在运行网络中，UE进行跨区域移动，所在区域超出了原来SMF的服务范围的场景下，保证UE会话业务连续性的操作过程。适用于AMF、SMF。

## 必备事项
前提条件

* 运营商已完成不同SMF所服务的TAI范围的规划（每个SMF可能支持部分TAI，所有SMF共同支持网络所有TAI）。
* 请仔细阅读WSFD-205012 跨域互联互通特性概述。
* 完成加载License。
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
    add_smfselplcy_list:
      type: items
      properties:
        SUBRANGE:
          name: '用户范围'
          type: string
          enum:
          - ALL_USER
          - HOME_USER
          - FOREIGN_USER
          - IMSI_PREFIX
          required: true
          description: 'I-SMF选择策略。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        ISMFSW:
          name: '是否支持I-SMF选择'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: NO
        ISMFSUPPORTIND:
          name: '是否携带IsmfSupportInd'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PREFERREDTAISW:
          name: 'Preferred TAI功能开关'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TAISW:
          name: '是否使用TAI'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NO
        IMSIPRE:
          name: 'IMSI前缀'
          type: string
          minLength: 5
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LOCDISCOPTSW:
          name: '本地服务发现SMF调优开关'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SSSW:
          name: '是否携带Serving Scope'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: ''
          data_source: ''
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
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV2ASLSR01'
      SWITCH: ENABLE
    add_smfselplcy_list:
    - SUBRANGE: HOME_USER
      ISMFSW: YES
      ISMFSUPPORTIND: ''
      PREFERREDTAISW: ''
      TAISW: NO
      IMSIPRE: ''
      LOCDISCOPTSW: ''
      SSSW: ''
    set_licenseswitch_list_1:
    - LICITEM: 'LKV2ASLSR02'
      SWITCH: ENABLE
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 进入“MML命令行-UNC”窗口。-AMF

### 2 打开本特性AMF的License配置开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

### 3 配置I-SMF选择策略。

```jinja2
{%- for item in add_smfselplcy_list -%}
    ADD SMFSELPLCY:
    {#- --- 必选参数 --- -#}
    SUBRANGE={{item.SUBRANGE}},
    {#- --- 可选参数 --- -#}
    {%- if item.ISMFSW is not none -%}
        ISMFSW={{item.ISMFSW}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：SUBRANGE=IMSI_PREFIX 时必选 --- -#}
    {%- if item.SUBRANGE == 'IMSI_PREFIX' -%}
        IMSIPRE="{{item.IMSIPRE}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：ISMFSW=YES 时可选 --- -#}
    {%- if item.ISMFSW == 'YES' -%}
        {%- if item.ISMFSUPPORTIND is not none -%}
            ISMFSUPPORTIND={{item.ISMFSUPPORTIND}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SUBRANGE=IMSI_PREFIX 时可选 --- -#}
    {%- if item.SUBRANGE == 'IMSI_PREFIX' -%}
        {%- if item.LOCDISCOPTSW is not none -%}
            LOCDISCOPTSW={{item.LOCDISCOPTSW}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：ISMFSW=YES 时可选 --- -#}
    {%- if item.ISMFSW == 'YES' -%}
        {%- if item.PREFERREDTAISW is not none -%}
            PREFERREDTAISW={{item.PREFERREDTAISW}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SUBRANGE=ALL_USER/HOME_USER/FOREIGN_USER/IMSI_PREFIX 时可选 --- -#}
    {%- if item.SUBRANGE in ['ALL_USER', 'HOME_USER', 'FOREIGN_USER', 'IMSI_PREFIX'] -%}
        {%- if item.SSSW is not none -%}
            SSSW={{item.SSSW}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：ISMFSW=NO 时可选 --- -#}
    {%- if item.ISMFSW == 'NO' -%}
        {%- if item.TAISW is not none -%}
            TAISW={{item.TAISW}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 进入“MML命令行-UNC”窗口。-SMF

### 5 打开本特性SMF的License配置开关。

```jinja2
{%- for item in set_licenseswitch_list_1 -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```


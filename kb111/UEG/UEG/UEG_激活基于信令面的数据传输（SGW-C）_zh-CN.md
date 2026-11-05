---
id: GWFD-026105
name: 激活基于信令面的数据传输（SGW-C）
ne_type: UEG
type: feature
description: 本操作指导介绍在运行网络中激活基于信令面的数据传输特性的操作过程。  适用于SGW-C
tags: []
risk_level: ''
doc_source: ["业务配置","风筝L","MEC 特性指南（风筝L）","GW-C&SMF特性指南","GWFD-026100 NB-IoT基本功能","GWFD-026105 基于信令面的数据传输（SGW-C）","激活基于信令面的数据传输（SGW-C）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
本操作指导介绍在运行网络中激活基于信令面的数据传输特性的操作过程。适用于SGW-C

## 必备事项
前提条件

* 请仔细阅读GWFD-026105 基于信令面的数据传输特性概述（SGW-C）。
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
    add_cdrfieldtemp_list:
      type: items
      properties:
        TEMPLATENAME:
          name: 'TEMPLATENAME'
          type: string
          maxLength: 63
          required: true
          description: '指定话单字段模板的名称。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        CPEPSOINDICATOR:
          name: 'CPEPSOINDICATOR'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '置话单中是否携带cp-eps-optimisation-indicator字段。'
          data_source: ''
          pattern: ''
          default: DISABLE
        UNIPDUCPONLY:
          name: 'UNIPDUCPONLY'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '配置话单中是否携带uni-pdu-cp-only-flag字段。'
          data_source: ''
          pattern: ''
          default: DISABLE
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV3WPSDTO11'
      SWITCH: ENABLE
    add_cdrfieldtemp_list:
    - TEMPLATENAME: 'cdrfieldtemp'
      CPEPSOINDICATOR: ENABLE
      UNIPDUCPONLY: ENABLE
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

### 3 **可选：**配置话单中是否携带CP CIoT EPS Optimisation Indicator、UNI PDU CP Only Flag字段。

```jinja2
{%- if is_optional_cdr_field_indicator -%}
    {%- for item in add_cdrfieldtemp_list -%}
        ADD CDRFIELDTEMP:
        {#- --- 必选参数 --- -#}
        TEMPLATENAME="{{item.TEMPLATENAME}}",
        {#- --- 可选参数 --- -#}
        {%- if item.CPEPSOINDICATOR is not none -%}
            CPEPSOINDICATOR={{item.CPEPSOINDICATOR}},
        {%- endif -%}
        {%- if item.UNIPDUCPONLY is not none -%}
            UNIPDUCPONLY={{item.UNIPDUCPONLY}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```


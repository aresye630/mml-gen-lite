---
id: GWFD-026108
name: 激活支持Category NB2 接入（S/PGW-C）
ne_type: UEG
type: feature
description: 本操作指导介绍在运行网络中激活支持Category NB2 接入特性的操作过程。  SGW-C、PGW-C
tags: []
risk_level: ''
doc_source: ["业务配置","风筝L","MEC 特性指南（风筝L）","GW-C&SMF特性指南","GWFD-026100 NB-IoT基本功能","GWFD-026108 支持Category NB2 接入（S/PGW-C）","激活支持Category NB2 接入（S/PGW-C）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
本操作指导介绍在运行网络中激活支持Category NB2 接入特性的操作过程。SGW-C、PGW-C

## 必备事项
前提条件

* 请仔细阅读GWFD-026108 支持Category NB2 接入特性概述（S/PGW-C）。
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
    set_smfsoftpara_list:
      type: items
      properties:
        DT:
          name: '数据类型'
          type: string
          enum:
          - Dw
          - Bit
          - Byte
          - String
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        BITNUM:
          name: 'Bit索引'
          type: integer
          minimum: 1
          maximum: 4000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        BITVALUE:
          name: 'Bit值'
          type: integer
          minimum: 0
          maximum: 1
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV3WSNBAC21'
      SWITCH: ENABLE
    set_smfsoftpara_list:
    - DT: Bit
      BITNUM: 717
      BITVALUE: 1
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

### 3 打开本特性的软参配置开关。

```jinja2
{%- for item in set_smfsoftpara_list -%}
    SET SMFSOFTPARA:
    {#- --- 必选参数 --- -#}
    DT={{item.DT}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：DT=Bit 时必选 --- -#}
    {%- if item.DT == 'Bit' -%}
        BITNUM={{item.BITNUM}},
    {%- endif -%}
    {#- --- 条件必选：DT=Bit 时必选 --- -#}
    {%- if item.DT == 'Bit' -%}
        BITVALUE={{item.BITVALUE}},
    {%- endif -%}
    ;
{%- endfor -%}
```


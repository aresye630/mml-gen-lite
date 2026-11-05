---
id: GWFD-023102
name: 激活支持多HPLMN功能（适用于SGW-C/PGW-C/SMF）
ne_type: UEG
type: feature
description: 当网络允许属于不同运营商用户共同接入时，为了判断用户的归属的属性，需要配置支持多HPLMN功能。  适用于SGW-C、PGW-C、SMF
tags: []
risk_level: ''
doc_source: ["业务配置","风筝L","MEC 特性指南（风筝L）","GW-C&SMF特性指南","GWFD-023100 组网能力增强","GWFD-023102 支持多HPLMN功能","激活支持多HPLMN功能（适用于SGW-C/PGW-C/SMF）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
当网络允许属于不同运营商用户共同接入时，为了判断用户的归属的属性，需要配置支持多HPLMN功能。适用于SGW-C、PGW-C、SMF

## 必备事项
前提条件

* 请仔细阅读GWFD-023102 支持多HPLMN功能特性概述。
* 已完成加载License。
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
    add_nghplmn_list:
      type: items
      properties:
        NOID:
          name: '运营商标识'
          type: integer
          minimum: 0
          maximum: 0
          required: true
          description: '新增HPLMN'
          data_source: '全网规划'
          pattern: ''
          default: ''
        MCC:
          name: '移动国家码'
          type: string
          minLength: 3
          maxLength: 3
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MNC:
          name: '移动网络号'
          type: string
          minLength: 2
          maxLength: 3
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DESC:
          name: '描述信息'
          type: string
          minLength: 0
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV2MHSM01'
      SWITCH: ENABLE
    add_nghplmn_list:
    - NOID: 0
      MCC: '123'
      MNC: '011'
      DESC: '00'
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 进入“MML命令行-UEG”窗口。

### 2 打开本特性的License控制开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

### 3 **可选：**新增HPLMN信息。

```jinja2
{%- if is_optional_add_hplmn -%}
    {%- for item in add_nghplmn_list -%}
        ADD NGHPLMN:
        {#- --- 必选参数 --- -#}
        NOID={{item.NOID}},
        MCC="{{item.MCC}}",
        MNC="{{item.MNC}}",
        {#- --- 可选参数 --- -#}
        {%- if item.DESC is not none -%}
            DESC="{{item.DESC}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```


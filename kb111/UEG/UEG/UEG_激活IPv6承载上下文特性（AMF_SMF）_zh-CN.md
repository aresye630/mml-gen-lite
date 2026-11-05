---
id: GWFD-022901
name: 激活IPv6承载上下文特性（AMF/SMF）
ne_type: UEG
type: feature
description: 本操作指导介绍激活IPv6承载上下文的操作过程。  适用于AMF、SMF
tags: []
risk_level: ''
doc_source:
  - ["业务配置","风筝L","MEC 特性指南（风筝L）","AMF特性指南","GWFD-022900 IPV6基本功能","GWFD-022901 IPv6承载上下文","激活IPv6承载上下文特性（AMF/SMF）"]
  - ["业务配置","风筝L","MEC 特性指南（风筝L）","GW-C&SMF特性指南","GWFD-022900 IPV6基本功能","GWFD-022901 IPv6承载上下文","GWFD-022901 IPv6承载上下文（AMF/SMF）","激活IPv6承载上下文特性（AMF/SMF）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
本操作指导介绍激活IPv6承载上下文的操作过程。适用于AMF、SMF

## 必备事项
前提条件

前提条件

* 请仔细阅读GWFD-022901 IPv6承载上下文特性概述（AMF/SMF）。
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
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV2IPV6AM01'
      SWITCH: ENABLE
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 进入“MML命令行-UEG”窗口。

### 2 打开IPv6承载上下文特性的License配置开关。

#### 2.1 //打开本特性的License配置开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```


---
id: GWFD-020913
name: 激活支持Null-MSISDN（适用于MME）
ne_type: UEG
type: feature
description: 本操作指导介绍在运行网络中激活支持Null-MSISDN特性的操作过程。  支持Null-MSISDN特性是指UEG支持不携带MSISDN（Mobile Station International ISDN Number）的用户进行基本的移动性管理和会话管理业务，如附着、TAU/RAU、激活等。  适用于MME。
tags: []
risk_level: ''
doc_source:
  - ["业务配置","风筝L","MEC 特性指南（风筝L）","MME特性指南","GWFD-020900 接入管理","GWFD-020913 支持Null-MSISDN","GWFD-020913 支持Null-MSISDN","激活支持Null-MSISDN（适用于MME）"]
  - ["业务配置","风筝L","MEC 特性指南（风筝L）","GW-C&SMF特性指南","GWFD-020900 接入管理","GWFD-020913 支持Null-MSISDN","GWFD-020913 支持Null-MSISDN","激活支持Null-MSISDN（适用于MME）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
本操作指导介绍在运行网络中激活支持Null-MSISDN特性的操作过程。支持Null-MSISDN特性是指UEG支持不携带MSISDN（Mobile Station International ISDN Number）的用户进行基本的移动性管理和会话管理业务，如附着、TAU/RAU、激活等。适用于MME。

## 必备事项
前提条件

* 请仔细阅读GWFD-020913 支持Null-MSISDN特性概述。
* 已完成加载License，对应的License项为“82207024 LKV2NOISDN02 支持Null-MSISDN”。
* 移动网络中的相关网元（如P-GW、HSS等）打开Null MSISDN业务功能。
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
    - LICITEM: 'LKV2NOISDN02'
      SWITCH: ENABLE
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 打开本特性的License配置开关。

### 进入“MML命令行-UEG”窗口。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```


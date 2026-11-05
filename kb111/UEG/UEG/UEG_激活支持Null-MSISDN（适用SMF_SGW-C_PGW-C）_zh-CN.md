---
id: GWFD-020913
name: 激活支持Null-MSISDN（适用SMF/SGW-C/PGW-C）
ne_type: UEG
type: feature
description: 本操作指导介绍在运行网络中激活支持Null-MSISDN特性的操作过程。  支持Null-MSISDN特性是指UEG支持不携带MSISDN（Mobile Station International ISDN Number）的用户进行基本的移动性管理和会话管理业务，如附着、TAU/RAU、激活等。  适用于SGW-C、PGW-C、SMF。
tags: []
risk_level: ''
doc_source:
  - ["业务配置","风筝L","MEC 特性指南（风筝L）","MME特性指南","GWFD-020900 接入管理","GWFD-020913 支持Null-MSISDN","GWFD-020913 支持Null-MSISDN","激活支持Null-MSISDN（适用SMF/SGW-C/PGW-C）"]
  - ["业务配置","风筝L","MEC 特性指南（风筝L）","GW-C&SMF特性指南","GWFD-020900 接入管理","GWFD-020913 支持Null-MSISDN","GWFD-020913 支持Null-MSISDN","激活支持Null-MSISDN（适用SMF/SGW-C/PGW-C）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
本操作指导介绍在运行网络中激活支持Null-MSISDN特性的操作过程。支持Null-MSISDN特性是指UEG支持不携带MSISDN（Mobile Station International ISDN Number）的用户进行基本的移动性管理和会话管理业务，如附着、TAU/RAU、激活等。适用于SGW-C、PGW-C、SMF。

## 必备事项
前提条件

* 请仔细阅读GWFD-020913 支持Null-MSISDN特性概述。
* 已完成加载License，对应的License项为“81202798 LKV3W9NUMD02 支持Null-MSISDN”。
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
    set_cpapnaccessctrl_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '使能Null-MSISDN功能'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        NULLMSISDN:
          name: '不携带MSISDN用户激活策略'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV3W9NUMD02'
      SWITCH: ENABLE
    set_cpapnaccessctrl_list:
    - APN: 'apn-test'
      NULLMSISDN: ENABLE
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 以下命令在“MML命令行-UEG”窗口上执行。打开本特性的License配置开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

### 2 使能Null-MSISDN功能。

### 该命令对新接入用户生效，不影响已接入用户。

```jinja2
{%- for item in set_cpapnaccessctrl_list -%}
    SET CPAPNACCESSCTRL:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    {#- --- 可选参数 --- -#}
    {%- if item.NULLMSISDN is not none -%}
        NULLMSISDN={{item.NULLMSISDN}},
    {%- endif -%}
    ;
{%- endfor -%}
```


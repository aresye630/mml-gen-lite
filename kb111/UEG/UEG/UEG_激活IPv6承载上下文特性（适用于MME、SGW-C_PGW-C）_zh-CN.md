---
id: GWFD-022901
name: 激活IPv6承载上下文特性（适用于MME、SGW-C/PGW-C）
ne_type: UEG
type: feature
description: 本操作指导介绍在运行网络中激活IPv6承载上下文的操作过程。  适用于MME、SGW-C、PGW-C。
tags: []
risk_level: ''
doc_source:
  - ["业务配置","风筝L","MEC 特性指南（风筝L）","MME特性指南","GWFD-022900 IPV6基本功能","GWFD-022901 IPv6承载上下文","激活IPv6承载上下文特性（适用于MME、SGW-C/PGW-C）"]
  - ["业务配置","风筝L","MEC 特性指南（风筝L）","GW-C&SMF特性指南","GWFD-022900 IPV6基本功能","GWFD-022901 IPv6承载上下文","GWFD-022901 IPv6承载上下文（MME、SGW-C/PGW-C）","激活IPv6承载上下文特性（适用于MME、SGW-C/PGW-C）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
本操作指导介绍在运行网络中激活IPv6承载上下文的操作过程。适用于MME、SGW-C、PGW-C。

## 必备事项
前提条件

* 请仔细阅读GWFD-022901 IPv6承载上下文特性概述（MME、S/PGW-C）。
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
    - LICITEM: 'LKV2IPV601'
      SWITCH: ENABLE
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 进入“MML命令行-UEG”窗口。

### 2 打开IPv6承载上下文特性的License配置开关。

### 设置License项的开关（SET LICENSESWITCH）**SET LICENSESWITCH**

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```


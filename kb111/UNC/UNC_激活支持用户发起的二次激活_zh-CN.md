---
id: ''
name: 激活支持用户发起的二次激活
ne_type: UNC
type: feature
description: 本操作指导介绍在运行网络中激活支持终端侧发起二次PDP上下文激活特性的操作过程。  适用于GGSN。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","会话管理功能","终端侧发起二次激活","WSFD-205104 支持用户发起的二次激活","激活支持用户发起的二次激活"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本操作指导介绍在运行网络中激活支持终端侧发起二次PDP上下文激活特性的操作过程。适用于GGSN。

## 必备事项
前提条件

* 请仔细阅读WSFD-205104 支持用户发起的二次激活特性概述
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
    add_apn_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        USRINTSECACTSW:
          name: '用户发起的二次激活开关'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV3W9SACT11'
      SWITCH: ENABLE
    add_apn_list:
    - APN: 'huawei.com'
      USRINTSECACTSW: ENABLE
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 进入“MML命令行-UNC”窗口。

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

### 3 打开UE发起二次激活开关。

```jinja2
{%- for item in add_apn_list -%}
    ADD APN:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    {#- --- 可选参数 --- -#}
    {%- if item.USRINTSECACTSW is not none -%}
        USRINTSECACTSW={{item.USRINTSECACTSW}},
    {%- endif -%}
    ;
{%- endfor -%}
```


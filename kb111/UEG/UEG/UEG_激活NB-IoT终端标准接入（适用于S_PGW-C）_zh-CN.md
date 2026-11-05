---
id: GWFD-026101
name: 激活NB-IoT终端标准接入（适用于S/PGW-C）
ne_type: UEG
type: feature
description: 本操作指导介绍在运行网络中激活NB-IoT终端标准接入的操作过程。  适用于SGW-C、PGW-C。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝L","MEC 特性指南（风筝L）","GW-C&SMF特性指南","GWFD-026100 NB-IoT基本功能","GWFD-026101 NB-IoT终端标准接入（适用于S/PGW-C）","激活NB-IoT终端标准接入（适用于S/PGW-C）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
本操作指导介绍在运行网络中激活NB-IoT终端标准接入的操作过程。适用于SGW-C、PGW-C。

## 必备事项
前提条件

请仔细阅读GWFD-026101 NB-IoT终端标准接入特性概述（适用于S/PGW-C）。
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
          description: '用于配置License控制项开关。'
          data_source: '本端规划'
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
          data_source: '本端规划'
          pattern: ''
          default: ''
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV3WPNBPS11'
      SWITCH: ENABLE
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


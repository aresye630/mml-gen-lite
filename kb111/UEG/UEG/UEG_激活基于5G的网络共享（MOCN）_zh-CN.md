---
id: GWFD-024401
name: 激活基于5G的网络共享（MOCN）
ne_type: UEG
type: feature
description: 本操作指导介绍在运行网络中激活基于5G的网络共享（MOCN）特性的操作过程。  适用于AMF。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝L","MEC 特性指南（风筝L）","AMF特性指南","GWFD-024400 MVNO基本功能","GWFD-024401 基于5G的网络共享（MOCN）","激活基于5G的网络共享（MOCN）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
本操作指导介绍在运行网络中激活基于5G的网络共享（MOCN）特性的操作过程。适用于AMF。

## 必备事项
前提条件

* 请仔细阅读基于5G的网络共享（MOCN）特性概述。
* 到AMF的基本数据已经配置完成，配置方法请参见《初始配置与调测》。
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
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV2MOCN04'
      SWITCH: ENABLE
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 进入“MML命令行-UEG”窗口。

### 2 打开基于5G的网络共享（MOCN）功能开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```


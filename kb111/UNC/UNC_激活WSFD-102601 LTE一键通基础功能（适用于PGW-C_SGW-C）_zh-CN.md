---
id: ''
name: 激活WSFD-102601 LTE一键通基础功能（适用于PGW-C/SGW-C）
ne_type: UNC
type: feature
description: 本操作指导介绍在运行网络中激活LTE一键通基础功能特性的操作过程。  适用于SGW-C、PGW-C。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","语音功能","WSFD-102600 Push to Talk（适用于PGW-C/SGW-C）","WSFD-102601 LTE一键通基础功能（适用于PGW-C/SGW-C）","激活WSFD-102601 LTE一键通基础功能（适用于PGW-C/SGW-C）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本操作指导介绍在运行网络中激活LTE一键通基础功能特性的操作过程。适用于SGW-C、PGW-C。

## 必备事项
前提条件

* 请仔细阅读WSFD-102601 LTE一键通基础功能（适用于PGW-C/SGW-C）。

* 已完成加载License。
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
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV3WNPLTE11'
      SWITCH: ENABLE
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 进入“MML命令行-UNC”窗口。

### 2 打开LTE一键通基础功能的License配置开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```


---
id: ''
name: 激活支持HTTP头压缩字典
ne_type: UNC
type: feature
description: 本操作指导介绍激活支持HTTP头压缩字典功能的操作过程。  适用于AMF、SMF。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","运维功能","WSFD-202002 支持HTTP头压缩字典","激活支持HTTP头压缩字典"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本操作指导介绍激活支持HTTP头压缩字典功能的操作过程。适用于AMF、SMF。

## 必备事项
前提条件

* 请仔细阅读WSFD-202002 支持HTTP头压缩字典特性概述。
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
    set_httpinforpt_list:
      type: items
      properties:
        HTTPLNKINFOLST:
          name: 'HTTP连接信息上报列表'
          type: string
          required: false
          description: '配置HTTP动态头域压缩字典上报功能，以及上报周期，用于控制HTTP连接信息上报。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        DYNHDRPTMR:
          name: 'HTTP动态头域压缩字典上报定时器'
          type: integer
          minimum: 5
          maximum: 3600
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV2HTTPCMPHD01'
      SWITCH: ENABLE
    set_httpinforpt_list:
    - HTTPLNKINFOLST: HTTPDYNCOMPHDIDXRPT-1
      DYNHDRPTMR: 60
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

### 3 配置HTTP动态头域压缩字典上报功能，以及上报周期。

```jinja2
{%- for item in set_httpinforpt_list -%}
    SET HTTPINFORPT:
    {#- --- 可选参数 --- -#}
    {%- if item.HTTPLNKINFOLST is not none -%}
        HTTPLNKINFOLST={{item.HTTPLNKINFOLST}},
    {%- endif -%}
    {%- if item.DYNHDRPTMR is not none -%}
        DYNHDRPTMR={{item.DYNHDRPTMR}},
    {%- endif -%}
    ;
{%- endfor -%}
```


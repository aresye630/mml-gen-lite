---
id: GWFD-025601
name: 激活LTE一键通基础功能（适用于MME）
ne_type: UEG
type: feature
description: 本操作指导介绍在运行网络中激活LTE一键通基础功能的操作过程。  适用于MME。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝L","MEC 特性指南（风筝L）","MME特性指南","GWFD-025600 Push to Talk","GWFD-025601 LTE一键通基础功能（适用于MME）","激活LTE一键通基础功能（适用于MME）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
本操作指导介绍在运行网络中激活LTE一键通基础功能的操作过程。适用于MME。

## 必备事项
前提条件

已完成加载License。
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
    add_qciconv_list:
      type: items
      properties:
        QCIEXT:
          name: '扩展QCI基准值'
          type: integer
          minimum: 10
          maximum: 254
          required: true
          description: 'PTT业务QCI转换为标准QCI'
          data_source: '全网规划'
          pattern: ''
          default: ''
        QCISTEP:
          name: '扩展QCI范围'
          type: integer
          minimum: 0
          maximum: 244
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        QCISTD:
          name: '标准QCI值'
          type: integer
          minimum: 1
          maximum: 9
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV2PPTF01'
      SWITCH: ENABLE
    add_qciconv_list:
    - QCIEXT: 65
      QCISTEP: 1
      QCISTD: 1
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 进入“MML命令行-UEG”窗口。

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

### 3 配置PTT业务QCI和标准QCI的映射规则。

```jinja2
{%- for item in add_qciconv_list -%}
    ADD QCICONV:
    {#- --- 必选参数 --- -#}
    QCIEXT={{item.QCIEXT}},
    QCISTD={{item.QCISTD}},
    {#- --- 可选参数 --- -#}
    {%- if item.QCISTEP is not none -%}
        QCISTEP={{item.QCISTEP}},
    {%- endif -%}
    ;
{%- endfor -%}
```


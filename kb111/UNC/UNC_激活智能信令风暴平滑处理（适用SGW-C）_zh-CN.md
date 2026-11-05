---
id: ''
name: 激活智能信令风暴平滑处理（适用SGW-C）
ne_type: UNC
type: feature
description: 当运营商需要部署SGW-C上智能信令风暴平滑处理，需要激活该功能。  适用于SGW-C。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","流控功能","WSFD-010804 智能信令风暴平滑处理","激活智能信令风暴平滑处理（适用SGW-C）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
当运营商需要部署SGW-C上智能信令风暴平滑处理，需要激活该功能。适用于SGW-C。

## 必备事项
前提条件

* 请仔细阅读WSFD-010804 智能信令风暴平滑处理特性概述。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    set_ddntimeoutctrl_list:
      type: items
      properties:
        DELAYSUBDELSW:
          name: '用户延时删除开关'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: true
          description: '使能“DDN消息无响应时进行用户延时删除处理”功能，并设置延时时长。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        MINDELAYTIMER:
          name: '延时定时器时长下限分钟值'
          type: integer
          minimum: 1
          maximum: 120
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        MAXDELAYTIMER:
          name: '延时定时器时长上限分钟值'
          type: integer
          minimum: 1
          maximum: 120
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
  examples:
    set_ddntimeoutctrl_list:
    - DELAYSUBDELSW: ENABLE
      MINDELAYTIMER: 40
      MAXDELAYTIMER: 70
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 进入“MML命令行-UNC”窗口。

### 2 使能“DDN消息无响应时进行用户延时删除处理”功能，并设置延时时长。

```jinja2
{%- for item in set_ddntimeoutctrl_list -%}
    SET DDNTIMEOUTCTRL:
    {#- --- 必选参数 --- -#}
    DELAYSUBDELSW={{item.DELAYSUBDELSW}},
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：DELAYSUBDELSW=ENABLE 时可选 --- -#}
    {%- if item.DELAYSUBDELSW == 'ENABLE' -%}
        {%- if item.MINDELAYTIMER is not none -%}
            MINDELAYTIMER={{item.MINDELAYTIMER}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：DELAYSUBDELSW=ENABLE 时可选 --- -#}
    {%- if item.DELAYSUBDELSW == 'ENABLE' -%}
        {%- if item.MAXDELAYTIMER is not none -%}
            MAXDELAYTIMER={{item.MAXDELAYTIMER}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```


---
id: ''
name: 配置APN锁定状态上报SMF
ne_type: UEG
type: feature
description: 需要在UPF上锁定APN，SMF联动选择其他UPF时，请参考本章节进行操作。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝S","MEC 特性指南（风筝S）","UEG特性指南","可靠性功能","支持APN锁定状态上报SMF","配置APN锁定状态上报SMF"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
需要在UPF上锁定APN，SMF联动选择其他UPF时，请参考本章节进行操作。

## 必备事项
前提条件

* 请仔细阅读支持APN锁定状态上报SMF功能概述。
* 请参考“UPF选择专题”描述，在SMF上完成相关配置。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    lck_apn_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '已通过**ADD APN**命令配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        LOCKED:
          name: '锁定'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: true
          description: '配置锁定或解锁定。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        N4RPTSTATE:
          name: 'N4链路上报状态'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '配置锁定状态是否上报SMF。'
          data_source: '本端规划'
          pattern: ''
          default: DISABLE
    lck_apn_list_1:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '已通过**ADD APN**命令配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        LOCKED:
          name: '锁定'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: true
          description: '配置锁定或解锁定。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        N4RPTSTATE:
          name: 'N4链路上报状态'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '配置锁定状态是否上报SMF。'
          data_source: '本端规划'
          pattern: ''
          default: DISABLE
  examples:
    lck_apn_list:
    - APN: 'test'
      LOCKED: ENABLE
      N4RPTSTATE: ENABLE
    lck_apn_list_1:
    - APN: 'test'
      LOCKED: DISABLE
      N4RPTSTATE: DISABLE
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 //锁定APN。

```jinja2
{%- if is_scenario_lock_apn -%}
    {%- for item in lck_apn_list -%}
        LCK APN:
        {#- --- 必选参数 --- -#}
        APN="{{item.APN}}",
        LOCKED={{item.LOCKED}},
        {#- --- 可选参数 --- -#}
        {%- if item.N4RPTSTATE is not none -%}
            N4RPTSTATE={{item.N4RPTSTATE}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 2 //解锁定APN。

```jinja2
{%- if is_scenario_unlock_apn -%}
    {%- for item in lck_apn_list_1 -%}
        LCK APN:
        {#- --- 必选参数 --- -#}
        APN="{{item.APN}}",
        LOCKED={{item.LOCKED}},
        {#- --- 可选参数 --- -#}
        {%- if item.N4RPTSTATE is not none -%}
            N4RPTSTATE={{item.N4RPTSTATE}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```


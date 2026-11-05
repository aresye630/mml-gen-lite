---
id: GWFD-021404
name: 激活SMF支持DDN流控功能
ne_type: UEG
type: feature
description: SMF的周边AMF存在过载风险时，SMF能够根据本地配置控制向各AMF发送DDN消息的速率，从而保护周边AMF。  适用于SMF。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝L","MEC 特性指南（风筝L）","GW-C&SMF特性指南","GWFD-021400 可靠性功能","GWFD-021404 周边网元过载保护","SMF支持DDN流控","激活SMF支持DDN流控功能"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
SMF的周边AMF存在过载风险时，SMF能够根据本地配置控制向各AMF发送DDN消息的速率，从而保护周边AMF。适用于SMF。

## 必备事项
前提条件

请仔细阅读GWFD-021404 周边网元过载保护特性概述（SMF支持DDN流控）。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    set_ddnflowctrl_list:
      type: items
      properties:
        WALVALUE:
          name: 'wal值'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: '设置SMF每秒发送给AMF的最大DDN消息数'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_ddnpriorityarp_list:
      type: items
      properties:
        ARP:
          name: 'ARP数值'
          type: integer
          minimum: 1
          maximum: 15
          required: true
          description: '添加DDN消息的ARP优先级规则。'
          data_source: ''
          pattern: ''
          default: ''
        PRIORITY:
          name: '优先级'
          type: string
          enum:
          - DDN_LOW
          - DDN_HIGH
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_ddnpriorityapn_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '设置DDN消息的APN优先级规则。'
          data_source: ''
          pattern: ''
          default: ''
        PRIORITY:
          name: '优先级'
          type: string
          enum:
          - DDN_LOW
          - DDN_HIGH
          - DDN_LOWEST
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    set_ddnflowctrl_list:
    - WALVALUE: 1000
    add_ddnpriorityarp_list:
    - ARP: 1
      PRIORITY: DDN_HIGH
    add_ddnpriorityapn_list:
    - APN: 'ims'
      PRIORITY: DDN_HIGH
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 进入“MML命令行-UEG”窗口。

### 2 设置SMF每秒发送给AMF的最大DDN消息数。

```jinja2
{%- for item in set_ddnflowctrl_list -%}
    SET DDNFLOWCTRL:
    {#- --- 可选参数 --- -#}
    {%- if item.WALVALUE is not none -%}
        WALVALUE={{item.WALVALUE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 配置高优先级DDN消息的ARP。

```jinja2
{%- for item in add_ddnpriorityarp_list -%}
    ADD DDNPRIORITYARP:
    {#- --- 必选参数 --- -#}
    ARP={{item.ARP}},
    PRIORITY={{item.PRIORITY}},
    ;
{%- endfor -%}
```

### 4 配置高优先级DDN消息的APN。

```jinja2
{%- for item in add_ddnpriorityapn_list -%}
    ADD DDNPRIORITYAPN:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    PRIORITY={{item.PRIORITY}},
    ;
{%- endfor -%}
```


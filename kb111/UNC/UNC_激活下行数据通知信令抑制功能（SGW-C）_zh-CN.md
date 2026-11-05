---
id: ''
name: 激活下行数据通知信令抑制功能（SGW-C）
ne_type: UNC
type: feature
description: 短时间内SGW-C向MME发送大量DDN消息会触发MME交互大量的寻呼信令，在SGW-C上激活下行数据通知信令抑制功能，从而达到保护MME的目的。  适用于SGW-C。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","流控功能","WSFD-010803 下行数据通知信令抑制","WSFD-010803 下行数据通知信令抑制（适用于SGW-C）","激活下行数据通知信令抑制功能（SGW-C）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
短时间内SGW-C向MME发送大量DDN消息会触发MME交互大量的寻呼信令，在SGW-C上激活下行数据通知信令抑制功能，从而达到保护MME的目的。适用于SGW-C。

## 必备事项
前提条件

请仔细阅读WSFD-010803 下行数据通知信令抑制（适用于SGW-C）特性概述。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    set_ddnthrottling_list:
      type: items
      properties:
        DDNTHROTSWITCH:
          name: 'DDN Throttling功能开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: true
          description: '设置DDN Throttling开关。'
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
    set_ddnthrottling_list:
    - DDNTHROTSWITCH: ENABLE
    add_ddnpriorityarp_list:
    - ARP: 1
      PRIORITY: DDN_HIGH
    add_ddnpriorityapn_list:
    - APN: 'ims'
      PRIORITY: DDN_HIGH
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 进入“MML命令行-UNC”窗口。

### 2 打开DDN Throttling开关。

```jinja2
{%- for item in set_ddnthrottling_list -%}
    SET DDNTHROTTLING:
    {#- --- 必选参数 --- -#}
    DDNTHROTSWITCH={{item.DDNTHROTSWITCH}},
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


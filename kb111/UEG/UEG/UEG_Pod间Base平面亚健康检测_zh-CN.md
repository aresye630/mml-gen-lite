---
id: ''
name: Pod间Base平面亚健康检测
ne_type: UEG
type: feature
description: Pod间Base平面亚健康检测是基于Pod间的点到点探测结果，进行的网络亚健康诊断。  操作员可以开启网络亚健康检查开关，并设置检查参数和相关告警上报参数，使系统根据设置参数检查网络亚健康状态并上报相关告警。
tags: []
risk_level: ''
doc_source:
  - ["业务配置","风筝M","MEC 特性指南（风筝M）","UEG特性指南","Service Fabric特性","Service Fabric可靠性","SFFD-010008 通信亚健康自愈","Pod间Base平面亚健康检测"]
  - ["业务配置","风筝L","MEC 特性指南（风筝L）","UEG公共特性指南","ServiceFabric特性（虚机容器）","Service Fabric可靠性","SFFD-010008 通信亚健康自愈","Pod间Base平面亚健康检测"]
  - ["业务配置","风筝L","MEC 特性指南（风筝L）","UEG公共特性指南","ServiceFabric特性（裸机容器）","Service Fabric可靠性","SFFD-010008 通信亚健康自愈","Pod间Base平面亚健康检测"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
Pod间Base平面亚健康检测是基于Pod间的点到点探测结果，进行的网络亚健康诊断。操作员可以开启网络亚健康检查开关，并设置检查参数和相关告警上报参数，使系统根据设置参数检查网络亚健康状态并上报相关告警。

## 必备事项
前提条件

请仔细阅读SFFD-010008 通信亚健康自愈。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    set_combasehealth_list:
      type: items
      properties:
        DETECTINTERVAL:
          name: '检测周期(秒)'
          type: integer
          minimum: 1
          maximum: 10
          required: false
          description: '设置Base平面的亚健康检测参数。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        STATISINTERVAL:
          name: '统计周期(秒)'
          type: integer
          minimum: 10
          maximum: 180
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        THRESHOLD:
          name: '亚健康告警阈值(千分比)'
          type: integer
          minimum: 1
          maximum: 1000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ENABLEFLAG:
          name: '使能开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    set_combasehealth_list:
    - DETECTINTERVAL: 1
      STATISINTERVAL: 30
      THRESHOLD: 50
      ENABLEFLAG: ENABLE
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 已经登录OM Portal，或者已登录MAE并进入Access子系统。

### 2 使用**SET COMBASEHEALTH**命令设置Base平面的pod之间链路亚健康检测参数。

```jinja2
{%- for item in set_combasehealth_list -%}
    SET COMBASEHEALTH:
    {#- --- 可选参数 --- -#}
    {%- if item.DETECTINTERVAL is not none -%}
        DETECTINTERVAL={{item.DETECTINTERVAL}},
    {%- endif -%}
    {%- if item.STATISINTERVAL is not none -%}
        STATISINTERVAL={{item.STATISINTERVAL}},
    {%- endif -%}
    {%- if item.THRESHOLD is not none -%}
        THRESHOLD={{item.THRESHOLD}},
    {%- endif -%}
    {%- if item.ENABLEFLAG is not none -%}
        ENABLEFLAG={{item.ENABLEFLAG}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### Base平面亚健康可能会导致上报如下相关告警：

### * **ALM-100319 Base平面Pod级亚健康告警**

### * **ALM-221257862 资源单元Base平面亚健康**

### * **ALM-221257870 Base平面亚健康**


---
id: ''
name: 配置会话级累计流量策略控制
ne_type: UDG
type: feature
description: 为了保证用户公平使用流量，配置基于会话级的累计流量的策略控制。
risk_level: ''
doc_source: ["特性部署","业务专题","5G Core FUP解决方案","会话级累计流量策略控制","配置会话级累计流量策略控制"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
为了保证用户公平使用流量，配置基于会话级的累计流量的策略控制。

## 必备事项
前提条件

* 完成PCC相关基本功能配置。
* 完成加载License（如果有需求，请联系华为技术支持工程师处理）。
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
          description: '**必选**，会话级累计流量策略控制的License项。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        SWITCH:
          name: '开关'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: true
          description: '**必选**，开启会话级累计流量策略控制功能。'
          data_source: '固定取值'
          pattern: ''
          default: ''
    set_licenseswitch_list_1:
      type: items
      properties:
        LICITEM:
          name: 'License项'
          type: string
          minLength: 0
          maxLength: 255
          required: true
          description: '**必选**，会话级累计流量策略控制的License项。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        SWITCH:
          name: '开关'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: true
          description: '**必选**，开启会话级累计流量策略控制功能。'
          data_source: '固定取值'
          pattern: ''
          default: ''
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV3W9PCBT12'
      SWITCH: ENABLE
    set_licenseswitch_list_1:
    - LICITEM: 'LKV3G5PCBT01'
      SWITCH: ENABLE
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 UNC侧配置

#### 1.1 //打开本特性的License配置开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

### 2 UDG侧配置

#### 2.1 //打开本特性的License配置开关。

```jinja2
{%- for item in set_licenseswitch_list_1 -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```


---
id: GWFD-110332
name: 激活基于小区负荷上报的无线资源优化
ne_type: UDG
type: feature
description: 运营商规划基于小区负荷状态对某些用户或某些业务进行策略控制以解除小区拥塞状况，需要激活基于小区负荷上报的无线资源优化功能。  适用于PGW-U。
risk_level: ''
doc_source: ["特性部署","特性指南","UDG特性指南","智能策略控制功能","GWFD-110332 基于小区负荷上报的无线资源优化","激活基于小区负荷上报的无线资源优化"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
运营商规划基于小区负荷状态对某些用户或某些业务进行策略控制以解除小区拥塞状况，需要激活基于小区负荷上报的无线资源优化功能。适用于PGW-U。

## 必备事项
前提条件

* 请仔细阅读GWFD-110332 基于小区负荷上报的无线资源优化。
* 完成**加载license**（如果有需求，请联系华为技术支持工程师处理）。
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
    set_apnreportattr_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '开启小区负荷上报功能。  UDG开启本功能后，要求RAN侧和PCRF同时也支持该功能。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        CONGESTIONRPT:
          name: '拥塞控制'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV3G5WOCR01'
      SWITCH: ENABLE
    set_apnreportattr_list:
    - APN: 'apn-test'
      CONGESTIONRPT: ENABLE
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 打开本特性的License配置开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

### 2 开启指定APN的小区负荷上报功能。

```jinja2
{%- for item in set_apnreportattr_list -%}
    SET APNREPORTATTR:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    {#- --- 可选参数 --- -#}
    {%- if item.CONGESTIONRPT is not none -%}
        CONGESTIONRPT={{item.CONGESTIONRPT}},
    {%- endif -%}
    ;
{%- endfor -%}
```


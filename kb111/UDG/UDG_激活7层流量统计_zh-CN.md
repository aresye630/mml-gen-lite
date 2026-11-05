---
id: GWFD-020308
name: 激活7层流量统计
ne_type: UDG
type: feature
description: 运营商部署7层流量统计功能实现在用户访问业务后，只统计7层应用层流量，不统计L3/L4承载层流量。  适用于PGW-U、UPF。
risk_level: ''
doc_source: ["特性部署","特性指南","UDG特性指南","计费功能","GWFD-020308 7层流量统计","激活7层流量统计"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
运营商部署7层流量统计功能实现在用户访问业务后，只统计7层应用层流量，不统计L3/L4承载层流量。适用于PGW-U、UPF。

## 必备事项
前提条件

* 请仔细阅读GWFD-020308 7层流量统计。
* 已完成部署UPF。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    add_apn_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '配置仅统计7层应用层流量功能。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        APPLAYERVOLUME:
          name: '仅统计应用层流量'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: DISABLE
  examples:
    add_apn_list:
    - APN: 'apn-test'
      APPLAYERVOLUME: ENABLE
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 配置仅统计7层应用层流量功能。

```jinja2
{%- for item in add_apn_list -%}
    ADD APN:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    {#- --- 可选参数 --- -#}
    {%- if item.APPLAYERVOLUME is not none -%}
        APPLAYERVOLUME={{item.APPLAYERVOLUME}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 当“APPLAYERVOLUME”参数配置为ENABLE，则只统计L7应用层流量。

### 当“APPLAYERVOLUME”参数配置为DISABLE，则统计L7应用层流量和L3/L4承载层流量。

### 当“APPLAYERVOLUME”参数配置为ENABLE，则只统计L7应用层流量。该配置会影响用户的计费流量统计，修改前请联系华为技术支持。


---
id: ''
name: 激活鉴权功能（适用于5G）
ne_type: UNC
type: feature
description: 对于建议强制鉴权的流程（包括初始注册、移动性INTER注册、空闲态EPS到5GS注册流程），系统默认开启鉴权功能。新建部署或运维阶段，可以执行本操作对所需流程开启强制鉴权功能，或者修改强制鉴权的流程。  适用于AMF。
risk_level: ''
doc_source: ["网络部署","安全配置","UNC安全配置","安全配置建议","必选配置","业务安全配置","激活鉴权功能（适用于5G）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
对于建议强制鉴权的流程（包括初始注册、移动性INTER注册、空闲态EPS到5GS注册流程），系统默认开启鉴权功能。新建部署或运维阶段，可以执行本操作对所需流程开启强制鉴权功能，或者修改强制鉴权的流程。适用于AMF。

## 必备事项
前提条件

请仔细阅读WSFD-010301 鉴权功能特性概述（适用于5G）。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    add_ngusrsecpara_list:
      type: items
      properties:
        SUBRANGE:
          name: '用户范围'
          type: string
          enum:
          - ALL_USER
          - IMSI_PREFIX
          required: true
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        AUTHEVENT:
          name: '鉴权事件'
          type: string
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        AUTHPERIOD:
          name: '鉴权周期(h)'
          type: integer
          minimum: 0
          maximum: 24
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: 24
        IMSIPRE:
          name: 'IMSI前缀'
          type: string
          minLength: 5
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    add_ngusrsecpara_list:
    - SUBRANGE: ALL_USER
      AUTHEVENT: SERVICE_REQUEST
      AUTHPERIOD: 24
      IMSIPRE: ''
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 进入“MML命令行-UNC”窗口。

### 2 设置需要强制鉴权的流程。

```jinja2
{%- for item in add_ngusrsecpara_list -%}
    ADD NGUSRSECPARA:
    {#- --- 必选参数 --- -#}
    SUBRANGE={{item.SUBRANGE}},
    {#- --- 可选参数 --- -#}
    {%- if item.AUTHEVENT is not none -%}
        AUTHEVENT={{item.AUTHEVENT}},
    {%- endif -%}
    {%- if item.AUTHPERIOD is not none -%}
        AUTHPERIOD={{item.AUTHPERIOD}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：SUBRANGE=IMSI_PREFIX 时必选 --- -#}
    {%- if item.SUBRANGE == 'IMSI_PREFIX' -%}
        IMSIPRE="{{item.IMSIPRE}}",
    {%- endif -%}
    ;
{%- endfor -%}
```


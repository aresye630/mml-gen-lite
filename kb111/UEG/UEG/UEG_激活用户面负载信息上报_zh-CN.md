---
id: GWFD-021604
name: 激活用户面负载信息上报
ne_type: UEG
type: feature
description: 当SGW-C/PGW-C/SMF需要基于网元负载信息选择SGW-U/PGW-U/UPF时，可激活本特性。  适用于SGW-U、PGW-U、UPF。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝L","MEC 特性指南（风筝L）","GW-U&UPF特性指南","GWFD-021600 分布式网络","GWFD-021604 用户面负载信息上报","激活用户面负载信息上报"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
当SGW-C/PGW-C/SMF需要基于网元负载信息选择SGW-U/PGW-U/UPF时，可激活本特性。适用于SGW-U、PGW-U、UPF。

## 必备事项
前提条件

请仔细阅读GWFD-021604 用户面负载信息上报。
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
    set_pfcploadrpt_list:
      type: items
      properties:
        LOADRPTSW:
          name: '负荷上报开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '用户面负载信息上报功能开关。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        RPTTHD:
          name: '上报阈值'
          type: integer
          minimum: 1
          maximum: 100
          required: false
          description: '设置负载信息上报和停止上报的阈值。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        STOPTHD:
          name: '停止上报阈值'
          type: integer
          minimum: 1
          maximum: 100
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        RANGETHD:
          name: '变化范围阈值'
          type: integer
          minimum: 1
          maximum: 100
          required: false
          description: '设置上报变化范围阈值。'
          data_source: '本端规划'
          pattern: ''
          default: ''
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV3G5UPLR01'
      SWITCH: ENABLE
    set_pfcploadrpt_list:
    - LOADRPTSW: ENABLE
      RPTTHD: 50
      STOPTHD: 45
      RANGETHD: 5
```

## 3 命令模板定义
<!-- @mml:block= commands -->

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

### 2 开启用户面负载信息上报的功能开关，并设置上报阈值。

```jinja2
{%- for item in set_pfcploadrpt_list -%}
    SET PFCPLOADRPT:
    {#- --- 可选参数 --- -#}
    {%- if item.LOADRPTSW is not none -%}
        LOADRPTSW={{item.LOADRPTSW}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：LOADRPTSW=ENABLE 时可选 --- -#}
    {%- if item.LOADRPTSW == 'ENABLE' -%}
        {%- if item.RPTTHD is not none -%}
            RPTTHD={{item.RPTTHD}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：LOADRPTSW=ENABLE 时可选 --- -#}
    {%- if item.LOADRPTSW == 'ENABLE' -%}
        {%- if item.STOPTHD is not none -%}
            STOPTHD={{item.STOPTHD}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：LOADRPTSW=ENABLE 时可选 --- -#}
    {%- if item.LOADRPTSW == 'ENABLE' -%}
        {%- if item.RANGETHD is not none -%}
            RANGETHD={{item.RANGETHD}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```


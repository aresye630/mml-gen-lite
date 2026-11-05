---
id: GWFD-021401
name: 配置系统过载特性
ne_type: UEG
type: feature
description: 在系统负荷较重的情况下，建议开启流控策略。通过控制系统接入业务量来保证系统过载情况下业务的正常进行，避免造成整系统瘫痪。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝L","MEC 特性指南（风筝L）","GW-U&UPF特性指南","GWFD-021400 可靠性功能","GWFD-021401 系统过载控制","配置系统过载特性"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
在系统负荷较重的情况下，建议开启流控策略。通过控制系统接入业务量来保证系统过载情况下业务的正常进行，避免造成整系统瘫痪。

## 必备事项
前提条件

请仔细阅读GWFD-021401 系统过载控制。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    add_upapn_list:
      type: items
      properties:
        UPAPN:
          name: 'UPAPN'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_apnaccesswal_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: 'APN下用户的接入速率'
          data_source: '本端规划'
          pattern: ''
          default: ''
        WALNUMBER:
          name: '用户的接入速率'
          type: integer
          minimum:
          - 0
          - 30
          maximum:
          - 0
          - 1000000
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_deactiverate_list:
      type: items
      properties:
        RATE:
          name: '去活速率'
          type: integer
          minimum: 10
          maximum: 2000
          required: true
          description: '去激活流控速率'
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_upsoftpara_list:
      type: items
      properties:
        DT:
          name: '软参记录数据类型'
          type: string
          enum:
          - BIT
          - BYTE
          - DWORD
          - STRING
          required: true
          description: '每秒发送的最大Error Indication消息数'
          data_source: '本端规划'
          pattern: ''
          default: ''
        DWORDNUM:
          name: 'DWord索引'
          type: integer
          minimum: 1
          maximum: 180
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        DWORDVALUE:
          name: 'Dword值'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
  examples:
    add_upapn_list:
    - UPAPN: apn1
    set_apnaccesswal_list:
    - APN: 'apn1'
      WALNUMBER: 30
    set_deactiverate_list:
    - RATE: 25
    set_upsoftpara_list:
    - DT: DWORD
      DWORDNUM: 47
      DWORDVALUE: 35
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 配置APN实例。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_upapn_list的变量区（command: ADD UPAPN） -#}
<!-- MISSING_MACRO: command=ADD UPAPN list_name=add_upapn_list step_id=1 -->
```

### 2 配置APN下用户的接入速率。

```jinja2
{%- for item in set_apnaccesswal_list -%}
    SET APNACCESSWAL:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    WALNUMBER={{item.WALNUMBER}},
    ;
{%- endfor -%}
```

### 3 配置用户去激活流控速率。

```jinja2
{%- for item in set_deactiverate_list -%}
    SET DEACTIVERATE:
    {#- --- 必选参数 --- -#}
    RATE={{item.RATE}},
    ;
{%- endfor -%}
```

### 4 配置每个VMPod每秒发送的最大Error Indication消息数。

```jinja2
{%- for item in set_upsoftpara_list -%}
    SET UPSOFTPARA:
    {#- --- 必选参数 --- -#}
    DT={{item.DT}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：DT=DWORD 时必选 --- -#}
    {%- if item.DT == 'DWORD' -%}
        DWORDNUM={{item.DWORDNUM}},
    {%- endif -%}
    {#- --- 条件必选：DT=DWORD 时必选 --- -#}
    {%- if item.DT == 'DWORD' -%}
        DWORDVALUE={{item.DWORDVALUE}},
    {%- endif -%}
    ;
{%- endfor -%}
```


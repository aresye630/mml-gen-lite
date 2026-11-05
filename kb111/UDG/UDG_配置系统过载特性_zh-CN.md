---
id: GWFD-010251
name: 配置系统过载特性
ne_type: UDG
type: feature
description: 在系统负荷较重的情况下，建议开启流控策略。通过控制系统接入业务量来保证系统过载情况下业务的正常进行，避免造成整系统瘫痪。
risk_level: ''
doc_source: ["特性部署","特性指南","UDG特性指南","可靠性功能","GWFD-010251 系统过载控制","配置系统过载特性"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
在系统负荷较重的情况下，建议开启流控策略。通过控制系统接入业务量来保证系统过载情况下业务的正常进行，避免造成整系统瘫痪。

## 必备事项
前提条件

请仔细阅读GWFD-010251 系统过载控制特性概述。
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
    set_softpara_list:
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
        BITNUM:
          name: 'Bit索引'
          type: integer
          minimum: 1
          maximum: 3840
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        BITVALUE:
          name: 'Bit值'
          type: integer
          minimum: 0
          maximum: 1
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        BYTENUM:
          name: 'Byte索引'
          type: integer
          minimum: 1
          maximum: 1200
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        BYTEVALUE:
          name: 'Byte值'
          type: integer
          minimum: 0
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        STRINGNUM:
          name: 'String索引'
          type: integer
          minimum: 1
          maximum: 30
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        STRINGVALUE:
          name: 'String值'
          type: string
          minLength: 0
          maxLength: 64
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    add_apn_list:
    - APN: 'apn1'
    set_apnaccesswal_list:
    - APN: 'apn1'
      WALNUMBER: 30
    set_deactiverate_list:
    - RATE: 25
    set_softpara_list:
    - DT: DWORD
      DWORDNUM: 47
      DWORDVALUE: 35
      BITNUM: ''
      BITVALUE: ''
      BYTENUM: ''
      BYTEVALUE: ''
      STRINGNUM: ''
      STRINGVALUE: ''
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 配置APN实例。

```jinja2
{%- for item in add_apn_list -%}
    ADD APN:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    ;
{%- endfor -%}
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
{%- for item in set_softpara_list -%}
    SET SOFTPARA:
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
    {#- --- 条件必选：DT=BIT 时必选 --- -#}
    {%- if item.DT == 'BIT' -%}
        BITNUM={{item.BITNUM}},
    {%- endif -%}
    {#- --- 条件必选：DT=BIT 时必选 --- -#}
    {%- if item.DT == 'BIT' -%}
        BITVALUE={{item.BITVALUE}},
    {%- endif -%}
    {#- --- 条件必选：DT=BYTE 时必选 --- -#}
    {%- if item.DT == 'BYTE' -%}
        BYTENUM={{item.BYTENUM}},
    {%- endif -%}
    {#- --- 条件必选：DT=BYTE 时必选 --- -#}
    {%- if item.DT == 'BYTE' -%}
        BYTEVALUE={{item.BYTEVALUE}},
    {%- endif -%}
    {#- --- 条件必选：DT=STRING 时必选 --- -#}
    {%- if item.DT == 'STRING' -%}
        STRINGNUM={{item.STRINGNUM}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：DT=STRING 时可选 --- -#}
    {%- if item.DT == 'STRING' -%}
        {%- if item.STRINGVALUE is not none -%}
            STRINGVALUE="{{item.STRINGVALUE}}",
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```


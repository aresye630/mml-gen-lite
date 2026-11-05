---
id: ''
name: 激活基于PCRF/PCF的VoLTE业务快速恢复
ne_type: UNC
type: feature
description: 在UNC上激活基于PCRF/PCF的VoLTE业务快速恢复功能，降低P-CSCF服务器故障时，对用户业务的影响。  适用于PGW-C。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","语音功能","WSFD-102203 基于PCRF/PCF的VoLTE业务快速恢复","激活基于PCRF/PCF的VoLTE业务快速恢复"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
在UNC上激活基于PCRF/PCF的VoLTE业务快速恢复功能，降低P-CSCF服务器故障时，对用户业务的影响。适用于PGW-C。

## 必备事项
前提条件

* 请仔细阅读WSFD-102203 基于PCRF/PCF的VoLTE业务快速恢复特性概述。
* 完成激活P-CSCF故障时IMS业务恢复。
* 已完成加载License。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    set_apnreportattr_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '将真实使用的APN与终端上报的APN配置映射关系。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PCRF:
          name: '上报给PCRF的APN名'
          type: string
          enum:
          - REQUESTED
          - SERVICE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_smfsoftparaofbit_list:
      type: items
      properties:
        DT:
          name: 'DT'
          type: string
          enum:
          - Dw
          - Byte
          required: true
          description: '设置SMF软件参数比特位，配置PGW-C基于PCRF/PCF的P-CSCF故障恢复会重新激活会话。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        DWORDNUM:
          name: 'DWORDNUM'
          type: integer
          minimum: 1
          maximum: 1500
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VALUE:
          name: 'VALUE'
          type: string
          enum:
          - VALUE_0
          - VALUE_1
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        POSITION:
          name: 'POSITION'
          type: integer
          minimum: 1
          maximum: 32
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
        BYTEPOSITION:
          name: 'Byte软参比特位'
          type: integer
          minimum: 1
          maximum: 8
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    set_apnreportattr_list:
    - APN: 'ims.real'
      PCRF: REQUESTED
    set_smfsoftparaofbit_list:
    - DT: Dw
      DWORDNUM: 1017
      VALUE: VALUE_1
      POSITION: 30
      BYTENUM: ''
      BYTEPOSITION: ''
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 进入“MML命令行-UNC”窗口。

### 2 将真实使用的APN与终端上报的APN配置映射关系。

```jinja2
{%- for item in set_apnreportattr_list -%}
    SET APNREPORTATTR:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    {#- --- 可选参数 --- -#}
    {%- if item.PCRF is not none -%}
        PCRF={{item.PCRF}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 配置PGW-C基于PCRF/PCF的P-CSCF故障恢复会重新激活会话。

```jinja2
{%- for item in set_smfsoftparaofbit_list -%}
    SET SMFSOFTPARAOFBIT:
    {#- --- 必选参数 --- -#}
    DT={{item.DT}},
    VALUE={{item.VALUE}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：DT=Dw 时必选 --- -#}
    {%- if item.DT == 'Dw' -%}
        DWORDNUM={{item.DWORDNUM}},
    {%- endif -%}
    {#- --- 条件必选：DT=Dw 时必选 --- -#}
    {%- if item.DT == 'Dw' -%}
        POSITION={{item.POSITION}},
    {%- endif -%}
    {#- --- 条件必选：DT=Byte 时必选 --- -#}
    {%- if item.DT == 'Byte' -%}
        BYTENUM={{item.BYTENUM}},
    {%- endif -%}
    {#- --- 条件必选：DT=Byte 时必选 --- -#}
    {%- if item.DT == 'Byte' -%}
        BYTEPOSITION={{item.BYTEPOSITION}},
    {%- endif -%}
    ;
{%- endfor -%}
```


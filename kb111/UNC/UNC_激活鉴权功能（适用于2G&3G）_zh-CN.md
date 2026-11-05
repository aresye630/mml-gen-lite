---
id: ''
name: 激活鉴权功能（适用于2G&3G）
ne_type: UNC
type: feature
description: 本操作指导介绍在运行网络中激活鉴权功能的操作过程。  鉴权功能是指SGSN通过对用户的身份识别和鉴权，以及对用户业务请求有效性的判断，使合法的用户能使用网络提供的业务。  适用于SGSN。
risk_level: ''
doc_source: ["网络部署","安全配置","UNC安全配置","安全配置建议","必选配置","业务安全配置","激活鉴权功能（适用于2G&3G）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本操作指导介绍在运行网络中激活鉴权功能的操作过程。鉴权功能是指SGSN通过对用户的身份识别和鉴权，以及对用户业务请求有效性的判断，使合法的用户能使用网络提供的业务。适用于SGSN。

## 必备事项
前提条件

* 请仔细阅读WSFD-010301 鉴权功能特性概述（适用于2G&3G）。
* 完成加载License。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    mod_gbauthciph_list:
      type: items
      properties:
        SUBRANGE:
          name: '用户范围'
          type: string
          enum:
          - ALL_USER
          - SPECIAL_USER
          required: true
          description: '设置GSM网络鉴权参数。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        SECPLC:
          name: '安全策略'
          type: string
          enum:
          - AUTHANDPROTECTED
          - AUTHONLY
          - NEVER
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AUTHEVENT:
          name: '鉴权事件'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AUTHEVENTTHRESHOLD:
          name: '鉴权事件上限'
          type: integer
          minimum: 0
          maximum: 1023
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ATTSAUTH:
          name: '是否支持附着流程的二次鉴权功能'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AUTHPERIOD:
          name: '鉴权周期'
          type: integer
          minimum: 0
          maximum: 24
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AUTHSETSNUMBER:
          name: '鉴权集数量'
          type: integer
          minimum: 1
          maximum: 5
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AUTHSETV2:
          name: '是否支持V2取鉴权集功能'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CAFTIMES:
          name: '用户鉴权失败次数临界值'
          type: integer
          minimum: 3
          maximum: 20
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CIPHALG:
          name: '加密算法'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GETAUTHADVTH:
          name: '预先取鉴权集门限值'
          type: integer
          minimum: 0
          maximum: 4
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NCIPH:
          name: '版本协商失败允许不加密'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PREGETAUTHSETS:
          name: '是否预取鉴权集'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RAUSAUTH:
          name: '是否支持路由更新流程的二次鉴权功能'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RNUM:
          name: '鉴权集重用次数'
          type: integer
          minimum: 0
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        XIDRESET:
          name: 'Rau Accept无响应后是否启用XID Reset流程'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IMSIPRE:
          name: 'IMSI前缀'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    mod_iuauthciph_list:
      type: items
      properties:
        SUBRANGE:
          name: '用户范围'
          type: string
          enum:
          - ALL_USER
          - SPECIAL_USER
          required: true
          description: '设置UMTS网络鉴权参数。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        SECPLC:
          name: '安全策略'
          type: string
          enum:
          - AUTHANDPROTECTED
          - AUTHONLY
          - NEVER
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AUTHEVENT:
          name: '鉴权事件'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AUTHEVENTTHRESHOLD:
          name: '鉴权事件上限'
          type: integer
          minimum: 0
          maximum: 1023
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ATTSAUTH:
          name: '是否支持附着流程的二次鉴权功能'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AUTHPERIOD:
          name: '鉴权周期'
          type: integer
          minimum: 0
          maximum: 24
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AUTHSETSNUMBER:
          name: '鉴权集数量'
          type: integer
          minimum: 1
          maximum: 5
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AUTHSETV2:
          name: '是否支持V2取鉴权集功能'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CAFTIMES:
          name: '用户鉴权失败次数临界值'
          type: integer
          minimum: 3
          maximum: 20
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CIPHALG:
          name: '加密算法'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GETAUTHADVTH:
          name: '预先取鉴权集门限值'
          type: integer
          minimum: 0
          maximum: 4
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        INTALG:
          name: '完整性算法'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PREGETAUTHSETS:
          name: '是否预取鉴权集'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RAUSAUTH:
          name: '是否支持路由更新流程的二次鉴权功能'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        REAUTH:
          name: '重复鉴权'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IMSIPRE:
          name: 'IMSI前缀'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_softparaofbit_list:
      type: items
      properties:
        DT:
          name: '参数类型'
          type: string
          enum:
          - BYTE
          - BYTE_EX
          - BYTE_EX_B
          - DWORD
          - DWORD_EX
          - DWORD_EX_B
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PARANUM:
          name: '参数索引'
          type: integer
          minimum: 1
          maximum: 512
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VALUE:
          name: '参数值'
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
          name: '比特位'
          type: integer
          minimum: 1
          maximum: 32
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    mod_gbauthciph_list:
    - SUBRANGE: ALL_USER
      SECPLC: AUTHANDPROTECTED
      AUTHEVENT: INTER_RAU-1
      AUTHEVENTTHRESHOLD: 1
      ATTSAUTH: NO
      AUTHPERIOD: ''
      AUTHSETSNUMBER: ''
      AUTHSETV2: ''
      CAFTIMES: ''
      CIPHALG: ''
      GETAUTHADVTH: ''
      NCIPH: ''
      PREGETAUTHSETS: ''
      RAUSAUTH: ''
      RNUM: ''
      XIDRESET: ''
      IMSIPRE: ''
    mod_iuauthciph_list:
    - SUBRANGE: ALL_USER
      SECPLC: AUTHANDPROTECTED
      AUTHEVENT: INTER_RAU-1
      AUTHEVENTTHRESHOLD: 1
      ATTSAUTH: NO
      AUTHPERIOD: ''
      AUTHSETSNUMBER: ''
      AUTHSETV2: ''
      CAFTIMES: ''
      CIPHALG: ''
      GETAUTHADVTH: ''
      INTALG: ''
      PREGETAUTHSETS: ''
      RAUSAUTH: ''
      REAUTH: ''
      IMSIPRE: ''
    set_softparaofbit_list:
    - DT: ''
      PARANUM: ''
      VALUE: ''
      POSITION: ''
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 进入“MML命令行-UNC”窗口。

### 2 设置GSM网络鉴权参数。

```jinja2
{%- for item in mod_gbauthciph_list -%}
    MOD GBAUTHCIPH:
    {#- --- 必选参数 --- -#}
    SUBRANGE={{item.SUBRANGE}},
    {#- --- 可选参数 --- -#}
    {%- if item.SECPLC is not none -%}
        SECPLC={{item.SECPLC}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：SUBRANGE=SPECIAL_USER 时必选 --- -#}
    {%- if item.SUBRANGE == 'SPECIAL_USER' -%}
        IMSIPRE="{{item.IMSIPRE}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：SECPLC=AUTHONLY/AUTHANDPROTECTED 时可选 --- -#}
    {%- if item.SECPLC in ['AUTHONLY', 'AUTHANDPROTECTED'] -%}
        {%- if item.AUTHEVENT is not none -%}
            AUTHEVENT={{item.AUTHEVENT}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SECPLC=AUTHONLY/AUTHANDPROTECTED 时可选 --- -#}
    {%- if item.SECPLC in ['AUTHONLY', 'AUTHANDPROTECTED'] -%}
        {%- if item.ATTSAUTH is not none -%}
            ATTSAUTH={{item.ATTSAUTH}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SECPLC=AUTHONLY/AUTHANDPROTECTED 时可选 --- -#}
    {%- if item.SECPLC in ['AUTHONLY', 'AUTHANDPROTECTED'] -%}
        {%- if item.AUTHEVENTTHRESHOLD is not none -%}
            AUTHEVENTTHRESHOLD={{item.AUTHEVENTTHRESHOLD}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SECPLC=AUTHONLY/AUTHANDPROTECTED 时可选 --- -#}
    {%- if item.SECPLC in ['AUTHONLY', 'AUTHANDPROTECTED'] -%}
        {%- if item.AUTHPERIOD is not none -%}
            AUTHPERIOD={{item.AUTHPERIOD}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SECPLC=AUTHONLY/AUTHANDPROTECTED 时可选 --- -#}
    {%- if item.SECPLC in ['AUTHONLY', 'AUTHANDPROTECTED'] -%}
        {%- if item.AUTHSETSNUMBER is not none -%}
            AUTHSETSNUMBER={{item.AUTHSETSNUMBER}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SECPLC=AUTHONLY/AUTHANDPROTECTED 时可选 --- -#}
    {%- if item.SECPLC in ['AUTHONLY', 'AUTHANDPROTECTED'] -%}
        {%- if item.AUTHSETV2 is not none -%}
            AUTHSETV2={{item.AUTHSETV2}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SECPLC=AUTHONLY/AUTHANDPROTECTED 时可选 --- -#}
    {%- if item.SECPLC in ['AUTHONLY', 'AUTHANDPROTECTED'] -%}
        {%- if item.CAFTIMES is not none -%}
            CAFTIMES={{item.CAFTIMES}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SECPLC=AUTHANDPROTECTED 时可选 --- -#}
    {%- if item.SECPLC == 'AUTHANDPROTECTED' -%}
        {%- if item.CIPHALG is not none -%}
            CIPHALG={{item.CIPHALG}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SECPLC=AUTHONLY/AUTHANDPROTECTED 时可选 --- -#}
    {%- if item.SECPLC in ['AUTHONLY', 'AUTHANDPROTECTED'] -%}
        {%- if item.GETAUTHADVTH is not none -%}
            GETAUTHADVTH={{item.GETAUTHADVTH}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SECPLC=AUTHANDPROTECTED 时可选 --- -#}
    {%- if item.SECPLC == 'AUTHANDPROTECTED' -%}
        {%- if item.NCIPH is not none -%}
            NCIPH={{item.NCIPH}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SECPLC=AUTHONLY/AUTHANDPROTECTED 时可选 --- -#}
    {%- if item.SECPLC in ['AUTHONLY', 'AUTHANDPROTECTED'] -%}
        {%- if item.PREGETAUTHSETS is not none -%}
            PREGETAUTHSETS={{item.PREGETAUTHSETS}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SECPLC=AUTHONLY/AUTHANDPROTECTED 时可选 --- -#}
    {%- if item.SECPLC in ['AUTHONLY', 'AUTHANDPROTECTED'] -%}
        {%- if item.RAUSAUTH is not none -%}
            RAUSAUTH={{item.RAUSAUTH}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SECPLC=AUTHONLY/AUTHANDPROTECTED 时可选 --- -#}
    {%- if item.SECPLC in ['AUTHONLY', 'AUTHANDPROTECTED'] -%}
        {%- if item.RNUM is not none -%}
            RNUM={{item.RNUM}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SECPLC=AUTHANDPROTECTED 时可选 --- -#}
    {%- if item.SECPLC == 'AUTHANDPROTECTED' -%}
        {%- if item.XIDRESET is not none -%}
            XIDRESET={{item.XIDRESET}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### “SECPLC”（安全策略）选择“AUTHANDPROTECTED”。

### 3 设置UMTS网络鉴权参数。

```jinja2
{%- for item in mod_iuauthciph_list -%}
    MOD IUAUTHCIPH:
    {#- --- 必选参数 --- -#}
    SUBRANGE={{item.SUBRANGE}},
    {#- --- 可选参数 --- -#}
    {%- if item.SECPLC is not none -%}
        SECPLC={{item.SECPLC}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：SUBRANGE=SPECIAL_USER 时必选 --- -#}
    {%- if item.SUBRANGE == 'SPECIAL_USER' -%}
        IMSIPRE="{{item.IMSIPRE}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：SECPLC=AUTHONLY/AUTHANDPROTECTED 时可选 --- -#}
    {%- if item.SECPLC in ['AUTHONLY', 'AUTHANDPROTECTED'] -%}
        {%- if item.AUTHEVENT is not none -%}
            AUTHEVENT={{item.AUTHEVENT}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SECPLC=AUTHONLY/AUTHANDPROTECTED 时可选 --- -#}
    {%- if item.SECPLC in ['AUTHONLY', 'AUTHANDPROTECTED'] -%}
        {%- if item.ATTSAUTH is not none -%}
            ATTSAUTH={{item.ATTSAUTH}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SECPLC=AUTHONLY/AUTHANDPROTECTED 时可选 --- -#}
    {%- if item.SECPLC in ['AUTHONLY', 'AUTHANDPROTECTED'] -%}
        {%- if item.AUTHEVENTTHRESHOLD is not none -%}
            AUTHEVENTTHRESHOLD={{item.AUTHEVENTTHRESHOLD}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SECPLC=AUTHONLY/AUTHANDPROTECTED 时可选 --- -#}
    {%- if item.SECPLC in ['AUTHONLY', 'AUTHANDPROTECTED'] -%}
        {%- if item.AUTHPERIOD is not none -%}
            AUTHPERIOD={{item.AUTHPERIOD}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SECPLC=AUTHONLY/AUTHANDPROTECTED 时可选 --- -#}
    {%- if item.SECPLC in ['AUTHONLY', 'AUTHANDPROTECTED'] -%}
        {%- if item.AUTHSETSNUMBER is not none -%}
            AUTHSETSNUMBER={{item.AUTHSETSNUMBER}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SECPLC=AUTHONLY/AUTHANDPROTECTED 时可选 --- -#}
    {%- if item.SECPLC in ['AUTHONLY', 'AUTHANDPROTECTED'] -%}
        {%- if item.AUTHSETV2 is not none -%}
            AUTHSETV2={{item.AUTHSETV2}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SECPLC=AUTHONLY/AUTHANDPROTECTED 时可选 --- -#}
    {%- if item.SECPLC in ['AUTHONLY', 'AUTHANDPROTECTED'] -%}
        {%- if item.CAFTIMES is not none -%}
            CAFTIMES={{item.CAFTIMES}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SECPLC=AUTHANDPROTECTED 时可选 --- -#}
    {%- if item.SECPLC == 'AUTHANDPROTECTED' -%}
        {%- if item.CIPHALG is not none -%}
            CIPHALG={{item.CIPHALG}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SECPLC=AUTHONLY/AUTHANDPROTECTED 时可选 --- -#}
    {%- if item.SECPLC in ['AUTHONLY', 'AUTHANDPROTECTED'] -%}
        {%- if item.GETAUTHADVTH is not none -%}
            GETAUTHADVTH={{item.GETAUTHADVTH}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SECPLC=AUTHANDPROTECTED 时可选 --- -#}
    {%- if item.SECPLC == 'AUTHANDPROTECTED' -%}
        {%- if item.INTALG is not none -%}
            INTALG={{item.INTALG}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SECPLC=AUTHONLY/AUTHANDPROTECTED 时可选 --- -#}
    {%- if item.SECPLC in ['AUTHONLY', 'AUTHANDPROTECTED'] -%}
        {%- if item.PREGETAUTHSETS is not none -%}
            PREGETAUTHSETS={{item.PREGETAUTHSETS}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SECPLC=AUTHONLY/AUTHANDPROTECTED 时可选 --- -#}
    {%- if item.SECPLC in ['AUTHONLY', 'AUTHANDPROTECTED'] -%}
        {%- if item.RAUSAUTH is not none -%}
            RAUSAUTH={{item.RAUSAUTH}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SECPLC=AUTHONLY/AUTHANDPROTECTED 时可选 --- -#}
    {%- if item.SECPLC in ['AUTHONLY', 'AUTHANDPROTECTED'] -%}
        {%- if item.REAUTH is not none -%}
            REAUTH={{item.REAUTH}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### “SECPLC”（安全策略）选择“AUTHANDPROTECTED”。

### 4 **可选：**进一步设置在Intra RAU 2G切3G流程中，是否发起鉴权加密流程。

```jinja2
{%- if is_optional_intra_rau_auth_cipher -%}
    {%- for item in set_softparaofbit_list -%}
        SET SOFTPARAOFBIT:
        {#- --- 必选参数 --- -#}
        DT={{item.DT}},
        PARANUM={{item.PARANUM}},
        POSITION={{item.POSITION}},
        VALUE={{item.VALUE}},
        ;
    {%- endfor -%}
{%- endif -%}
```

### DWORD6 BIT6的软参值设置为0，发起鉴权和加密流程。参数值设置为1仅发起加密流程。

### 在网络侧下发鉴权加密请求，MS因为USIM卡故障回复Auth Failure导致Intra RAU失败时，建议设置本软参值为1。


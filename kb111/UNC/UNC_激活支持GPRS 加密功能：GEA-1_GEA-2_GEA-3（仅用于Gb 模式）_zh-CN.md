---
id: ''
name: 激活支持GPRS 加密功能：GEA-1/GEA-2/GEA-3（仅用于Gb 模式）
ne_type: UNC
type: feature
description: 本操作指导介绍在运行网络中激活支持GPRS加密功能：GEA特性的操作过程。  GEA（GPRS Encryption Algorithm）是对LLC（Logic Link Control）层传递的用户数据进行加密的一种算法，加密范围从SGSN到MS，用来保证数据传输的安全性。加密处理的数据部分主要包括LLC帧所携带的信息域和校验域。GEA分为三种类型：GEA-1、GEA-2和GEA-3。  请至少激活GEA-1/GEA-2/GEA-3中的至少一种加密算法。  适用于SGSN。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","安全管理功能","WSFD-103000 支持GPRS 加密功能：GEA（仅用于Gb 模式）","激活支持GPRS 加密功能：GEA-1/GEA-2/GEA-3（仅用于Gb 模式）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本操作指导介绍在运行网络中激活支持GPRS加密功能：GEA特性的操作过程。GEA（GPRS Encryption Algorithm）是对LLC（Logic Link Control）层传递的用户数据进行加密的一种算法，加密范围从SGSN到MS，用来保证数据传输的安全性。加密处理的数据部分主要包括LLC帧所携带的信息域和校验域。GEA分为三种类型：GEA-1、GEA-2和GEA-3。请至少激活GEA-1/GEA-2/GEA-3中的至少一种加密算法。适用于SGSN。

## 必备事项
前提条件

* 请仔细阅读支持GPRS加密功能：GEA（仅用于Gb 模式）特性概述。
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
          description: '激活GEA功能。'
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
        CIPHALG:
          name: '加密算法'
          type: string
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
    mod_gbauthciph_list_1:
      type: items
      properties:
        SUBRANGE:
          name: '用户范围'
          type: string
          enum:
          - ALL_USER
          - SPECIAL_USER
          required: true
          description: '激活GEA功能。'
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
        CIPHALG:
          name: '加密算法'
          type: string
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
    mod_gbauthciph_list_2:
      type: items
      properties:
        SUBRANGE:
          name: '用户范围'
          type: string
          enum:
          - ALL_USER
          - SPECIAL_USER
          required: true
          description: '激活GEA功能。'
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
        CIPHALG:
          name: '加密算法'
          type: string
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
    set_licenseswitch_list:
      type: items
      properties:
        LICITEM:
          name: 'License项'
          type: string
          minLength: 0
          maxLength: 255
          required: true
          description: '打开本特性的License配置开关。'
          data_source: '本端规划'
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
  examples:
    mod_gbauthciph_list:
    - SUBRANGE: ALL_USER
      SECPLC: AUTHANDPROTECTED
      CIPHALG: GEA_1-1
      ATTSAUTH: ''
      AUTHEVENT: ''
      AUTHEVENTTHRESHOLD: ''
      AUTHPERIOD: ''
      AUTHSETSNUMBER: ''
      AUTHSETV2: ''
      CAFTIMES: ''
      GETAUTHADVTH: ''
      NCIPH: ''
      PREGETAUTHSETS: ''
      RAUSAUTH: ''
      RNUM: ''
      XIDRESET: ''
      IMSIPRE: ''
    mod_gbauthciph_list_1:
    - SUBRANGE: ALL_USER
      SECPLC: AUTHANDPROTECTED
      CIPHALG: GEA_1-1
      ATTSAUTH: ''
      AUTHEVENT: ''
      AUTHEVENTTHRESHOLD: ''
      AUTHPERIOD: ''
      AUTHSETSNUMBER: ''
      AUTHSETV2: ''
      CAFTIMES: ''
      GETAUTHADVTH: ''
      NCIPH: ''
      PREGETAUTHSETS: ''
      RAUSAUTH: ''
      RNUM: ''
      XIDRESET: ''
      IMSIPRE: ''
    mod_gbauthciph_list_2:
    - SUBRANGE: ALL_USER
      SECPLC: AUTHANDPROTECTED
      CIPHALG: GEA_1-1
      ATTSAUTH: ''
      AUTHEVENT: ''
      AUTHEVENTTHRESHOLD: ''
      AUTHPERIOD: ''
      AUTHSETSNUMBER: ''
      AUTHSETV2: ''
      CAFTIMES: ''
      GETAUTHADVTH: ''
      NCIPH: ''
      PREGETAUTHSETS: ''
      RAUSAUTH: ''
      RNUM: ''
      XIDRESET: ''
      IMSIPRE: ''
    set_licenseswitch_list:
    - LICITEM: 'LKV2GEA102'
      SWITCH: ENABLE
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 进入“MML命令行-UNC”窗口。

### 2 激活GEA功能。

#### 2.1 GEA-1：**MOD GBAUTHCIPH**

```jinja2
{%- if is_scenario_gea_1 -%}
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
        {#- --- 条件可选：SECPLC=AUTHANDPROTECTED 时可选 --- -#}
        {%- if item.SECPLC == 'AUTHANDPROTECTED' -%}
            {%- if item.CIPHALG is not none -%}
                CIPHALG={{item.CIPHALG}},
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
            {%- if item.AUTHEVENT is not none -%}
                AUTHEVENT={{item.AUTHEVENT}},
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
{%- endif -%}
```

#### 2.2 GEA-2：**MOD GBAUTHCIPH**

```jinja2
{%- if is_scenario_gea_2 -%}
    {%- for item in mod_gbauthciph_list_1 -%}
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
        {#- --- 条件可选：SECPLC=AUTHANDPROTECTED 时可选 --- -#}
        {%- if item.SECPLC == 'AUTHANDPROTECTED' -%}
            {%- if item.CIPHALG is not none -%}
                CIPHALG={{item.CIPHALG}},
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
            {%- if item.AUTHEVENT is not none -%}
                AUTHEVENT={{item.AUTHEVENT}},
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
{%- endif -%}
```

#### 2.3 GEA-3：**MOD GBAUTHCIPH**

```jinja2
{%- if is_scenario_gea_3 -%}
    {%- for item in mod_gbauthciph_list_2 -%}
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
        {#- --- 条件可选：SECPLC=AUTHANDPROTECTED 时可选 --- -#}
        {%- if item.SECPLC == 'AUTHANDPROTECTED' -%}
            {%- if item.CIPHALG is not none -%}
                CIPHALG={{item.CIPHALG}},
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
            {%- if item.AUTHEVENT is not none -%}
                AUTHEVENT={{item.AUTHEVENT}},
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
{%- endif -%}
```

#### 2.4 参数“SUBRANGE”（用户范围）选择“ALL\_USER”。

#### 2.5 参数“SECPLC”（安全策略）选择“AUTHANDPROTECTED”。

### 3 打开GEA特性的License配置开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```


---
id: ''
name: 激活切换策略控制
ne_type: UNC
type: feature
description: 本操作指导介绍在运行网络中激活切换策略控制特性的操作过程。  切换策略控制就是根据用户属性确定用户在GSM和UMTS网络中的切换策略，来引导GSM、UMTS和LTE的网络业务承载和网络负荷。  适用于SGSN。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","互操作功能","WSFD-104507 切换策略控制","激活切换策略控制"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本操作指导介绍在运行网络中激活切换策略控制特性的操作过程。切换策略控制就是根据用户属性确定用户在GSM和UMTS网络中的切换策略，来引导GSM、UMTS和LTE的网络业务承载和网络负荷。适用于SGSN。

## 必备事项
前提条件

* 请仔细阅读WSFD-104507 切换策略控制特性概述。
* 完成加载License。
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
    set_compatibility_list:
      type: items
      properties:
        SRVHANDOVER2G:
          name: 'Gb模式Service Handover'
          type: string
          enum:
          - FIRST_PDP_ONLY
          - MULT_PDP
          - NOT_SUPPORT
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SRVHANDOVER3G:
          name: 'Iu模式Service Handover'
          type: string
          enum:
          - FIRST_PDP_ONLY
          - MULT_PDP
          - NOT_SUPPORT
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        GTL:
          name: 'GPRS到LTE网络优选'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        WTL:
          name: 'WCDMA到LTE网络优选'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_softpara_list:
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
          - STR
          - STR_EX
          - STR_EX_B
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
          maxLength: 31
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    mod_rnc_list:
      type: items
      properties:
        RNCX:
          name: 'RNC索引'
          type: integer
          minimum: 0
          maximum: 511
          required: true
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        RNCVER:
          name: 'RNC的协议版本'
          type: string
          enum:
          - R4
          - R5
          - R6
          - R7
          - R8
          - R9+
          - R99
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        OFUTRAN:
          name: 'RNC是否支持Out Of UTRAN'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SPID:
          name: 'RNC是否支持SPID'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_srvhandover_list:
      type: items
      properties:
        SRVLVL:
          name: '业务级别'
          type: string
          enum:
          - BACKGROUND
          - CONVERSATION
          - INTERACTIVETRAFFICPRI1
          - INTERACTIVETRAFFICPRI2
          - INTERACTIVETRAFFICPRI3
          - STREAMINGGBRLESS24KBPS
          - STREAMINGGBRMORE25KBPS
          required: true
          description: '* 业务级别为“Background”，用户级别为“高端用户”，WCDMA业务切换策略为“GPRS(建议切换到GPRS)”，GPRS业务切换策略为建议切换到WCDMA。 * 业务级别为“Background”，用户级别为“低端用户”，WCDMA业务切换策略为建议切换到GPRS，GPRS业务切换策略为“GPRS(不建议切换到WCDMA)”。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        USRPRI:
          name: '用户级别'
          type: string
          enum:
          - HIGHLEVELUSER
          - LOWLEVELUSER
          - NONE
          - NORMALUSER
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        WSHS:
          name: 'WCDMA业务切换策略'
          type: string
          enum:
          - GPRS
          - ONLYWCDMA
          - WCDMA
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        GSHS:
          name: 'GPRS业务切换策略'
          type: string
          enum:
          - GPRS
          - ONLYGPRS
          - WCDMA
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV2SRVHD02'
      SWITCH: ENABLE
    set_compatibility_list:
    - SRVHANDOVER2G: MULT_PDP
      SRVHANDOVER3G: MULT_PDP
      GTL: YES
      WTL: YES
    set_softpara_list:
    - DT: BYTE_EX
      PARANUM: 60
      VALUE: '5'
    mod_rnc_list:
    - RNCX: 1
      RNCVER: R8
      OFUTRAN: ''
      SPID: ''
    add_srvhandover_list:
    - SRVLVL: BACKGROUND
      USRPRI: HIGHLEVELUSER
      WSHS: GPRS
      GSHS: WCDMA
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 进入“MML命令行-UNC”窗口。

### 2 打开本特性的License配置开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

### 3 启用业务切换策略功能。

```jinja2
{%- for item in set_compatibility_list -%}
    SET COMPATIBILITY:
    {#- --- 可选参数 --- -#}
    {%- if item.SRVHANDOVER2G is not none -%}
        SRVHANDOVER2G={{item.SRVHANDOVER2G}},
    {%- endif -%}
    {%- if item.SRVHANDOVER3G is not none -%}
        SRVHANDOVER3G={{item.SRVHANDOVER3G}},
    {%- endif -%}
    {%- if item.GTL is not none -%}
        GTL={{item.GTL}},
    {%- endif -%}
    {%- if item.WTL is not none -%}
        WTL={{item.WTL}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 此命令用于启用2G、3G业务切换策略功能。“SRVHANDOVER2G”取值为“FIRST\_PDP\_ONLY”表示2G只支持第一个PDP业务切换，“SRVHANDOVER3G”取值为“MULT\_PDP”表示3G支持多PDP切换，“GTL”取值为“YES”表示支持GSM网络到LTE网络的切换策略下发，“WTL”取值为“YES”表示UMTS网络到LTE网络的切换策略下发。

### 4 打开E-UTRAN Service Handover信元和Service UTRAN CCO信元中的Service E-UTRAN CCO Value的下发控制开关。

```jinja2
{%- for item in set_softpara_list -%}
    SET SOFTPARA:
    {#- --- 必选参数 --- -#}
    DT={{item.DT}},
    PARANUM={{item.PARANUM}},
    VALUE="{{item.VALUE}}",
    ;
{%- endfor -%}
```

### “PARANUM”为60的BIT1-BIT4是E-UTRAN Service Handover信元和Service UTRAN CCO信元中的Service E-UTRAN CCO Value的下发控制开关。BYTE\_EX60 BIT1-BIT4配置为0表示UNC始终不下发；配置为其他非0值表示UNC可以下发。

### 5 设置RNC的协议版本为R8及以上版本。

```jinja2
{%- for item in mod_rnc_list -%}
    MOD RNC:
    {#- --- 必选参数 --- -#}
    RNCX={{item.RNCX}},
    {#- --- 可选参数 --- -#}
    {%- if item.RNCVER is not none -%}
        RNCVER={{item.RNCVER}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：RNCVER=R9+ 时可选 --- -#}
    {%- if item.RNCVER == 'R9+' -%}
        {%- if item.OFUTRAN is not none -%}
            OFUTRAN={{item.OFUTRAN}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：RNCVER=R8/R9+ 时可选 --- -#}
    {%- if item.RNCVER in ['R8', 'R9+'] -%}
        {%- if item.SPID is not none -%}
            SPID={{item.SPID}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 为了避免RNC的协议版本较低时下发E-UTRAN Service Handover信元可能导致的RELOCATION流程失败，还需要设置RNC的协议版本“RNCVER”为R8及以上版本，UNC才会下发E-UTRAN Service Handover信元。

### 6 配置业务切换策略。

```jinja2
{%- for item in add_srvhandover_list -%}
    ADD SRVHANDOVER:
    {#- --- 必选参数 --- -#}
    SRVLVL={{item.SRVLVL}},
    USRPRI={{item.USRPRI}},
    WSHS={{item.WSHS}},
    GSHS={{item.GSHS}},
    ;
{%- endfor -%}
```


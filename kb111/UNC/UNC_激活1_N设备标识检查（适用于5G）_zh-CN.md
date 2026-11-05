---
id: ''
name: 激活1/N设备标识检查（适用于5G）
ne_type: UNC
type: feature
description: 本章节指导如何在运行的5G网络中激活1/N设备标识检查特性。  适用于AMF。
risk_level: ''
doc_source: ["网络部署","安全配置","UNC安全配置","安全配置建议","可选配置","业务安全配置","激活1/N设备标识检查（适用于5G）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本章节指导如何在运行的5G网络中激活1/N设备标识检查特性。适用于AMF。

## 必备事项
前提条件

* 请仔细阅读WSFD-103006 1/N设备标识检查特性概述（适用于5G）。

* 该特性的依赖特性WSFD-103004 设备标识检查特性已经正常开通，详细请参见激活设备标识检查特性（适用于5G）。
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
    mod_ngpeiplcy_list:
      type: items
      properties:
        SUBRANGE:
          name: '用户范围'
          type: string
          enum:
          - ALL_USER
          - IMSI_PREFIX
          - IMSI
          required: true
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        GETPEIPLCY:
          name: 'PEI获取策略'
          type: string
          enum:
          - NOGET
          - GETIMEI
          - GETIMEISV
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        CHKPEIPLCY:
          name: 'PEI检查策略'
          type: string
          enum:
          - NOCHK
          - CHKIMEI
          - CHKIMEISV
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        CHKPEITHRESHOLD:
          name: 'PEI检查上限'
          type: integer
          minimum: 0
          maximum: 1023
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        BALLOW:
          name: '是否允许黑名单用户接入'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CHKFAIL:
          name: '是否允许EIR返回失败时接入'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CTFLAG:
          name: 'PEI检查超时是否允许接入'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DISCFAIL:
          name: '是否允许EIR发现失败时接入'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        EMERGENCYSW:
          name: '是否允许紧急注册用户接入'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GRALLOW:
          name: '是否允许灰名单用户接入'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PROTTYPE:
          name: '流程类型'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        REDIRECTSW:
          name: '是否支持EIR重定向'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RETRYSW:
          name: '是否重选EIR'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PEIACCESS:
          name: 'PEI获取失败是否允许接入'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IMSI:
          name: 'IMSI'
          type: string
          minLength: 14
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
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
    set_licenseswitch_list:
    - LICITEM: 'LKV21NIMEI01'
      SWITCH: ENABLE
    mod_ngpeiplcy_list:
    - SUBRANGE: ALL_USER
      GETPEIPLCY: GETIMEISV
      CHKPEIPLCY: CHKIMEISV
      CHKPEITHRESHOLD: 2
      BALLOW: ''
      CHKFAIL: ''
      CTFLAG: ''
      DISCFAIL: ''
      EMERGENCYSW: ''
      GRALLOW: ''
      PROTTYPE: ''
      REDIRECTSW: ''
      RETRYSW: ''
      PEIACCESS: ''
      IMSI: ''
      IMSIPRE: ''
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 打开本特性的License配置开关。

### 进入“MML命令行-UNC”窗口。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

### 2 配置PEI检查上限。

```jinja2
{%- for item in mod_ngpeiplcy_list -%}
    MOD NGPEIPLCY:
    {#- --- 必选参数 --- -#}
    SUBRANGE={{item.SUBRANGE}},
    {#- --- 可选参数 --- -#}
    {%- if item.GETPEIPLCY is not none -%}
        GETPEIPLCY={{item.GETPEIPLCY}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：SUBRANGE=IMSI 时必选 --- -#}
    {%- if item.SUBRANGE == 'IMSI' -%}
        IMSI="{{item.IMSI}}",
    {%- endif -%}
    {#- --- 条件必选：SUBRANGE=IMSI_PREFIX 时必选 --- -#}
    {%- if item.SUBRANGE == 'IMSI_PREFIX' -%}
        IMSIPRE="{{item.IMSIPRE}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：GETPEIPLCY=GETIMEISV/GETIMEI 时可选 --- -#}
    {%- if item.GETPEIPLCY in ['GETIMEISV', 'GETIMEI'] -%}
        {%- if item.CHKPEIPLCY is not none -%}
            CHKPEIPLCY={{item.CHKPEIPLCY}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：CHKPEIPLCY=CHKIMEISV/CHKIMEI 时可选 --- -#}
    {%- if item.CHKPEIPLCY in ['CHKIMEISV', 'CHKIMEI'] -%}
        {%- if item.CHKPEITHRESHOLD is not none -%}
            CHKPEITHRESHOLD={{item.CHKPEITHRESHOLD}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：CHKPEIPLCY=CHKIMEISV/CHKIMEI 时可选 --- -#}
    {%- if item.CHKPEIPLCY in ['CHKIMEISV', 'CHKIMEI'] -%}
        {%- if item.BALLOW is not none -%}
            BALLOW={{item.BALLOW}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：CHKPEIPLCY=CHKIMEISV/CHKIMEI 时可选 --- -#}
    {%- if item.CHKPEIPLCY in ['CHKIMEISV', 'CHKIMEI'] -%}
        {%- if item.CHKFAIL is not none -%}
            CHKFAIL={{item.CHKFAIL}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：CHKPEIPLCY=CHKIMEISV/CHKIMEI 时可选 --- -#}
    {%- if item.CHKPEIPLCY in ['CHKIMEISV', 'CHKIMEI'] -%}
        {%- if item.CTFLAG is not none -%}
            CTFLAG={{item.CTFLAG}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：CHKPEIPLCY=CHKIMEISV/CHKIMEI 时可选 --- -#}
    {%- if item.CHKPEIPLCY in ['CHKIMEISV', 'CHKIMEI'] -%}
        {%- if item.DISCFAIL is not none -%}
            DISCFAIL={{item.DISCFAIL}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：CHKPEIPLCY=CHKIMEISV/CHKIMEI 时可选 --- -#}
    {%- if item.CHKPEIPLCY in ['CHKIMEISV', 'CHKIMEI'] -%}
        {%- if item.EMERGENCYSW is not none -%}
            EMERGENCYSW={{item.EMERGENCYSW}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：CHKPEIPLCY=CHKIMEISV/CHKIMEI 时可选 --- -#}
    {%- if item.CHKPEIPLCY in ['CHKIMEISV', 'CHKIMEI'] -%}
        {%- if item.GRALLOW is not none -%}
            GRALLOW={{item.GRALLOW}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：GETPEIPLCY=GETIMEISV/GETIMEI 时可选 --- -#}
    {%- if item.GETPEIPLCY in ['GETIMEISV', 'GETIMEI'] -%}
        {%- if item.PEIACCESS is not none -%}
            PEIACCESS={{item.PEIACCESS}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：CHKPEIPLCY=CHKIMEISV/CHKIMEI 时可选 --- -#}
    {%- if item.CHKPEIPLCY in ['CHKIMEISV', 'CHKIMEI'] -%}
        {%- if item.PROTTYPE is not none -%}
            PROTTYPE={{item.PROTTYPE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：CHKPEIPLCY=CHKIMEISV/CHKIMEI 时可选 --- -#}
    {%- if item.CHKPEIPLCY in ['CHKIMEISV', 'CHKIMEI'] -%}
        {%- if item.REDIRECTSW is not none -%}
            REDIRECTSW={{item.REDIRECTSW}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：CHKPEIPLCY=CHKIMEISV/CHKIMEI 时可选 --- -#}
    {%- if item.CHKPEIPLCY in ['CHKIMEISV', 'CHKIMEI'] -%}
        {%- if item.RETRYSW is not none -%}
            RETRYSW={{item.RETRYSW}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```


---
id: ''
name: 激活设备标识检查特性（适用于4G）
ne_type: UNC
type: feature
description: 本操作指导介绍在运行的4G网络中激活设备标识检查功能的操作过程。  适用于MME。
risk_level: ''
doc_source: ["网络部署","安全配置","UNC安全配置","安全配置建议","可选配置","业务安全配置","激活设备标识检查特性（适用于4G）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本操作指导介绍在运行的4G网络中激活设备标识检查功能的操作过程。适用于MME。

## 必备事项
前提条件

* 请仔细阅读WSFD-103004 设备标识检查特性概述（适用于4G）。
* EIR已激活设备标识检查功能。
* 完成EIR对接配置。MME通过S13接口对接4G网络EIR时，请参考配置到EIR的数据。MME与AMF融合部署且通过N17接口对接5G-EIR时，请参考配置SBI接口。
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
    mod_s1imeicfg_list:
      type: items
      properties:
        SUBRANGE:
          name: '用户范围'
          type: string
          enum:
          - ALL_USER
          - IMSI_PREFIX
          - IMSI_RANGE
          required: true
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        GETIMEIPLC:
          name: 'IMEI获取策略'
          type: string
          enum:
          - IMEI
          - IMEISV
          - NO
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        CHKIMEIPLC:
          name: 'IMEI检查策略'
          type: string
          enum:
          - IMEI
          - IMEISV
          - NO
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        ITTYPE:
          name: 'EIR接口类型'
          type: string
          enum:
          - Gf
          - N17
          - S13
          required: false
          description: '* MME通过S13接口对接4G网络EIR时，配置为S13。 * MME与AMF融合部署且通过N17接口对接5G-EIR时，配置为N17。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        IMEIACCESS:
          name: 'IMEI获取失败是否允许接入'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        CTFLAG:
          name: 'IMEI检查超时是否允许接入'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        GRALLOW:
          name: '是否允许灰名单用户接入'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        BLALLOW:
          name: '是否允许黑名单用户接入'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        USERERR:
          name: '是否允许EIR返回用户原因失败时接入'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        PROVIDERR:
          name: '是否允许EIR返回设备原因失败时接入'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        EIROUTTIMER:
          name: 'EIR响应超时时长'
          type: integer
          minimum: 1
          maximum: 15
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        CHKIMEITHRESHOLD:
          name: 'IMEI检查上限'
          type: integer
          minimum: 0
          maximum: 1023
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ABORTERR:
          name: '是否允许底层原因失败时接入'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        S13FAIL:
          name: '是否允许EIR返回失败时接入'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        BEGIMSI:
          name: '起始IMSI'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ENDIMSI:
          name: '终止IMSI'
          type: string
          maxLength: 15
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
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV2EIR02'
      SWITCH: ENABLE
    mod_s1imeicfg_list:
    - SUBRANGE: ALL_USER
      GETIMEIPLC: IMEISV
      CHKIMEIPLC: IMEISV
      ITTYPE: S13
      IMEIACCESS: YES
      CTFLAG: YES
      GRALLOW: YES
      BLALLOW: NO
      USERERR: YES
      PROVIDERR: YES
      EIROUTTIMER: 5
      CHKIMEITHRESHOLD: ''
      ABORTERR: ''
      S13FAIL: ''
      BEGIMSI: ''
      ENDIMSI: ''
      IMSIPRE: ''
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

### 3 设置4G网络设备标识获取和检查策略。

```jinja2
{%- for item in mod_s1imeicfg_list -%}
    MOD S1IMEICFG:
    {#- --- 必选参数 --- -#}
    SUBRANGE={{item.SUBRANGE}},
    {#- --- 可选参数 --- -#}
    {%- if item.GETIMEIPLC is not none -%}
        GETIMEIPLC={{item.GETIMEIPLC}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：SUBRANGE=IMSI_RANGE 时必选 --- -#}
    {%- if item.SUBRANGE == 'IMSI_RANGE' -%}
        BEGIMSI="{{item.BEGIMSI}}",
    {%- endif -%}
    {#- --- 条件必选：SUBRANGE=IMSI_RANGE 时必选 --- -#}
    {%- if item.SUBRANGE == 'IMSI_RANGE' -%}
        ENDIMSI="{{item.ENDIMSI}}",
    {%- endif -%}
    {#- --- 条件必选：SUBRANGE=IMSI_PREFIX 时必选 --- -#}
    {%- if item.SUBRANGE == 'IMSI_PREFIX' -%}
        IMSIPRE="{{item.IMSIPRE}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：GETIMEIPLC=IMEI/IMEISV 时可选 --- -#}
    {%- if item.GETIMEIPLC in ['IMEI', 'IMEISV'] -%}
        {%- if item.CHKIMEIPLC is not none -%}
            CHKIMEIPLC={{item.CHKIMEIPLC}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：CHKIMEIPLC=IMEI/IMEISV 时可选 --- -#}
    {%- if item.CHKIMEIPLC in ['IMEI', 'IMEISV'] -%}
        {%- if item.ITTYPE is not none -%}
            ITTYPE={{item.ITTYPE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：GETIMEIPLC=IMEI/IMEISV 时可选 --- -#}
    {%- if item.GETIMEIPLC in ['IMEI', 'IMEISV'] -%}
        {%- if item.IMEIACCESS is not none -%}
            IMEIACCESS={{item.IMEIACCESS}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：CHKIMEIPLC=IMEI/IMEISV 时可选 --- -#}
    {%- if item.CHKIMEIPLC in ['IMEI', 'IMEISV'] -%}
        {%- if item.CTFLAG is not none -%}
            CTFLAG={{item.CTFLAG}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：CHKIMEIPLC=IMEI/IMEISV 时可选 --- -#}
    {%- if item.CHKIMEIPLC in ['IMEI', 'IMEISV'] -%}
        {%- if item.GRALLOW is not none -%}
            GRALLOW={{item.GRALLOW}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：CHKIMEIPLC=IMEI/IMEISV 时可选 --- -#}
    {%- if item.CHKIMEIPLC in ['IMEI', 'IMEISV'] -%}
        {%- if item.BLALLOW is not none -%}
            BLALLOW={{item.BLALLOW}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：ITTYPE=Gf 时可选 --- -#}
    {%- if item.ITTYPE == 'Gf' -%}
        {%- if item.USERERR is not none -%}
            USERERR={{item.USERERR}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：ITTYPE=Gf 时可选 --- -#}
    {%- if item.ITTYPE == 'Gf' -%}
        {%- if item.PROVIDERR is not none -%}
            PROVIDERR={{item.PROVIDERR}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：CHKIMEIPLC=IMEI/IMEISV 时可选 --- -#}
    {%- if item.CHKIMEIPLC in ['IMEI', 'IMEISV'] -%}
        {%- if item.EIROUTTIMER is not none -%}
            EIROUTTIMER={{item.EIROUTTIMER}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：ITTYPE=Gf 时可选 --- -#}
    {%- if item.ITTYPE == 'Gf' -%}
        {%- if item.ABORTERR is not none -%}
            ABORTERR={{item.ABORTERR}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：CHKIMEIPLC=IMEI/IMEISV 时可选 --- -#}
    {%- if item.CHKIMEIPLC in ['IMEI', 'IMEISV'] -%}
        {%- if item.CHKIMEITHRESHOLD is not none -%}
            CHKIMEITHRESHOLD={{item.CHKIMEITHRESHOLD}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：ITTYPE=S13/N17 时可选 --- -#}
    {%- if item.ITTYPE in ['S13', 'N17'] -%}
        {%- if item.S13FAIL is not none -%}
            S13FAIL={{item.S13FAIL}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```


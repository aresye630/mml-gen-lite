---
id: ''
name: 激活设备标识检查特性（适用于2G&3G）
ne_type: UNC
type: feature
description: 本操作指导介绍在运行的2G&3G网络中激活设备标识检查功能的操作过程。  适用于SGSN。
risk_level: ''
doc_source: ["网络部署","安全配置","UNC安全配置","安全配置建议","可选配置","业务安全配置","激活设备标识检查特性（适用于2G&3G）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本操作指导介绍在运行的2G&3G网络中激活设备标识检查功能的操作过程。适用于SGSN。

## 必备事项
前提条件

* 请仔细阅读WSFD-103004 设备标识检查特性概述（适用于2G&3G）。
* 需要对端网元EIR激活IMEI检查功能。
* 完成加载License。
* EIR已经配置成功，具体配置内容请参考配置到EIR的数据。
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
    mod_gbimeicfg_list:
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
          description: 'IMEI检查相关配置'
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
          description: ''
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
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        ITTYPE:
          name: 'EIR接口类型'
          type: string
          enum:
          - Gf
          - S13
          required: false
          description: ''
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
          description: ''
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
          description: ''
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
          description: ''
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
          description: ''
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
          description: ''
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
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        EIROUTTIMER:
          name: 'EIR响应超时时长'
          type: integer
          minimum: 1
          maximum: 15
          required: false
          description: ''
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
    mod_iuimeicfg_list:
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
          description: 'IMEI检查相关配置'
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
          description: ''
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
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        ITTYPE:
          name: 'EIR接口类型'
          type: string
          enum:
          - Gf
          - S13
          required: false
          description: ''
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
          description: ''
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
          description: ''
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
          description: ''
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
          description: ''
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
          description: ''
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
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        EIROUTTIMER:
          name: 'EIR响应超时时长'
          type: integer
          minimum: 1
          maximum: 15
          required: false
          description: ''
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
    add_gbimeicfg_list:
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
    add_iuimeicfg_list:
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
        GETIMEIPLC:
          name: 'IMEI获取策略'
          type: string
          enum:
          - IMEI
          - IMEISV
          - NO
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NO
        CHKIMEIPLC:
          name: 'IMEI检查策略'
          type: string
          enum:
          - IMEI
          - IMEISV
          - NO
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NO
        BLALLOW:
          name: '是否允许黑名单用户接入'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: YES
        CHKIMEITHRESHOLD:
          name: 'IMEI检查上限'
          type: integer
          minimum: 0
          maximum: 1023
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 0
        CTFLAG:
          name: 'IMEI检查超时是否允许接入'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: YES
        EIROUTTIMER:
          name: 'EIR响应超时时长'
          type: integer
          minimum: 1
          maximum: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 5
        GRALLOW:
          name: '是否允许灰名单用户接入'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: YES
        ITTYPE:
          name: 'EIR接口类型'
          type: string
          enum:
          - Gf
          - S13
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: Gf
        IMEIACCESS:
          name: 'IMEI获取失败是否允许接入'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: YES
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
    add_gbimeicfg_list_1:
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
    mod_gbimeicfg_list:
    - SUBRANGE: ALL_USER
      GETIMEIPLC: IMEISV
      CHKIMEIPLC: IMEI
      ITTYPE: Gf
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
    mod_iuimeicfg_list:
    - SUBRANGE: ALL_USER
      GETIMEIPLC: IMEISV
      CHKIMEIPLC: IMEI
      ITTYPE: Gf
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
    add_gbimeicfg_list:
    - SUBRANGE: ''
      BEGIMSI: ''
      ENDIMSI: ''
      IMSIPRE: ''
    add_iuimeicfg_list:
    - SUBRANGE: IMSI_PREFIX
      IMSIPRE: '12303'
      GETIMEIPLC: IMEISV
      CHKIMEIPLC: NO
      BLALLOW: YES
      CHKIMEITHRESHOLD: ''
      CTFLAG: YES
      EIROUTTIMER: 5
      GRALLOW: YES
      ITTYPE: Gf
      IMEIACCESS: YES
      BEGIMSI: ''
      ENDIMSI: ''
    add_gbimeicfg_list_1:
    - SUBRANGE: ''
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

### 3 设置GERAN、UTRAN、E-UTRAN网络获取和检查IMEI的策略。

```jinja2
{%- for item in mod_gbimeicfg_list -%}
    MOD GBIMEICFG:
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
    {#- --- 条件可选：ITTYPE=Gf 时可选 --- -#}
    {%- if item.ITTYPE == 'Gf' -%}
        {%- if item.ABORTERR is not none -%}
            ABORTERR={{item.ABORTERR}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：CHKIMEIPLC=IMEI/IMEISV 时可选 --- -#}
    {%- if item.CHKIMEIPLC in ['IMEI', 'IMEISV'] -%}
        {%- if item.BLALLOW is not none -%}
            BLALLOW={{item.BLALLOW}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：GETIMEIPLC=IMEI/IMEISV 时可选 --- -#}
    {%- if item.GETIMEIPLC in ['IMEI', 'IMEISV'] -%}
        {%- if item.CHKIMEIPLC is not none -%}
            CHKIMEIPLC={{item.CHKIMEIPLC}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：CHKIMEIPLC=IMEI/IMEISV 时可选 --- -#}
    {%- if item.CHKIMEIPLC in ['IMEI', 'IMEISV'] -%}
        {%- if item.CHKIMEITHRESHOLD is not none -%}
            CHKIMEITHRESHOLD={{item.CHKIMEITHRESHOLD}},
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
        {%- if item.EIROUTTIMER is not none -%}
            EIROUTTIMER={{item.EIROUTTIMER}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：CHKIMEIPLC=IMEI/IMEISV 时可选 --- -#}
    {%- if item.CHKIMEIPLC in ['IMEI', 'IMEISV'] -%}
        {%- if item.GRALLOW is not none -%}
            GRALLOW={{item.GRALLOW}},
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
        {%- if item.ITTYPE is not none -%}
            ITTYPE={{item.ITTYPE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：ITTYPE=Gf 时可选 --- -#}
    {%- if item.ITTYPE == 'Gf' -%}
        {%- if item.PROVIDERR is not none -%}
            PROVIDERR={{item.PROVIDERR}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：ITTYPE=S13 时可选 --- -#}
    {%- if item.ITTYPE == 'S13' -%}
        {%- if item.S13FAIL is not none -%}
            S13FAIL={{item.S13FAIL}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：ITTYPE=Gf 时可选 --- -#}
    {%- if item.ITTYPE == 'Gf' -%}
        {%- if item.USERERR is not none -%}
            USERERR={{item.USERERR}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in mod_iuimeicfg_list -%}
    MOD IUIMEICFG:
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
    {#- --- 条件可选：ITTYPE=S13 时可选 --- -#}
    {%- if item.ITTYPE == 'S13' -%}
        {%- if item.S13FAIL is not none -%}
            S13FAIL={{item.S13FAIL}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 **可选：**增加指定IMSI号段用户获取和检查IMEI的策略。指定IMSI号段的用户采用对应的IMEI策略，未配置的用户采用默认的IMEI策略。

### IMSI号段有两种形式：一种为IMSI前缀形式，另一种为起始IMSI和终止IMSI形式。这两种形式同时只允许配置一种。

#### 4.1 配置IMSI前缀形式的号段用户在GERAN网络获取和检查IMEI的策略。

```jinja2
{%- if is_optional_add_imsi_segment_user_policy and is_scenario_imsi_prefix -%}
    {%- for item in add_gbimeicfg_list -%}
        ADD GBIMEICFG:
        {#- --- 必选参数 --- -#}
        SUBRANGE={{item.SUBRANGE}},
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
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_optional_add_imsi_segment_user_policy and is_scenario_imsi_prefix -%}
    {%- for item in add_iuimeicfg_list -%}
        ADD IUIMEICFG:
        {#- --- 必选参数 --- -#}
        SUBRANGE={{item.SUBRANGE}},
        {#- --- 可选参数 --- -#}
        {%- if item.GETIMEIPLC is not none -%}
            GETIMEIPLC={{item.GETIMEIPLC}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：SUBRANGE=IMSI_PREFIX 时必选 --- -#}
        {%- if item.SUBRANGE == 'IMSI_PREFIX' -%}
            IMSIPRE="{{item.IMSIPRE}}",
        {%- endif -%}
        {#- --- 条件必选：SUBRANGE=IMSI_RANGE 时必选 --- -#}
        {%- if item.SUBRANGE == 'IMSI_RANGE' -%}
            BEGIMSI="{{item.BEGIMSI}}",
        {%- endif -%}
        {#- --- 条件必选：SUBRANGE=IMSI_RANGE 时必选 --- -#}
        {%- if item.SUBRANGE == 'IMSI_RANGE' -%}
            ENDIMSI="{{item.ENDIMSI}}",
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
            {%- if item.BLALLOW is not none -%}
                BLALLOW={{item.BLALLOW}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：CHKIMEIPLC=IMEI/IMEISV 时可选 --- -#}
        {%- if item.CHKIMEIPLC in ['IMEI', 'IMEISV'] -%}
            {%- if item.CHKIMEITHRESHOLD is not none -%}
                CHKIMEITHRESHOLD={{item.CHKIMEITHRESHOLD}},
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
            {%- if item.EIROUTTIMER is not none -%}
                EIROUTTIMER={{item.EIROUTTIMER}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：CHKIMEIPLC=IMEI/IMEISV 时可选 --- -#}
        {%- if item.CHKIMEIPLC in ['IMEI', 'IMEISV'] -%}
            {%- if item.GRALLOW is not none -%}
                GRALLOW={{item.GRALLOW}},
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
            {%- if item.ITTYPE is not none -%}
                ITTYPE={{item.ITTYPE}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 4.2 配置起始IMSI和终止IMSI形式的号段用户在GERAN网络获取和检查IMEI的策略。

```jinja2
{%- if is_optional_add_imsi_segment_user_policy and is_scenario_imsi_start_end -%}
    {%- for item in add_gbimeicfg_list_1 -%}
        ADD GBIMEICFG:
        {#- --- 必选参数 --- -#}
        SUBRANGE={{item.SUBRANGE}},
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
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 激活IMEI检查特性，参数“GETIMEIPLC”（是否获取用户的IMEI）选择“IMEI”（获取IMEI）或“IMEISV”（获取IMEISV）；参数“CHKIMEIPLC”（是否检查用户的IMEI）选择“IMEI”（检查IMEI）或“IMEISV”（检查IMEISV）。


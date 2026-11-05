---
id: ''
name: 激活1/N设备标识检查（适用于2G&3G&4G）
ne_type: UNC
type: feature
description: 本操作指导介绍在运行的2G&3G&4G网络中激活1/N设备标识检查功能的操作过程。  适用于SGSN、MME。
risk_level: ''
doc_source: ["网络部署","安全配置","UNC安全配置","安全配置建议","可选配置","业务安全配置","激活1/N设备标识检查（适用于2G&3G&4G）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本操作指导介绍在运行的2G&3G&4G网络中激活1/N设备标识检查功能的操作过程。适用于SGSN、MME。

## 必备事项
前提条件

* 请仔细阅读WSFD-103006 1/N设备标识检查特性概述（适用于2G&3G&4G）。

* 该特性的依赖特性WSFD-103004 设备标识检查特性已经正常开通，详细操作请参见激活设备标识检查特性（适用于2G&3G）和激活设备标识检查特性（适用于4G）。
* EIR已经配置成功，具体配置内容请参考配置到EIR的数据。
* 需要对端网元EIR激活IMEI检查功能。
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
    mod_gbimeicfg_list:
      type: items
      properties:
        CHKIMEITHRESHOLD:
          name: 'IMEI检查上限'
          type: integer
          minimum: 0
          maximum: 1023
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
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
          data_source: ''
          pattern: ''
          default: ''
        CHKIMEITHRESHOLD:
          name: 'IMEI检查上限'
          type: integer
          minimum: 0
          maximum: 1023
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
          description: ''
          data_source: ''
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
          data_source: ''
          pattern: ''
          default: ''
        EIROUTTIMER:
          name: 'EIR响应超时时长'
          type: integer
          minimum: 1
          maximum: 15
          required: false
          description: ''
          data_source: ''
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
          data_source: ''
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
          data_source: ''
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
    mod_s1imeicfg_list:
      type: items
      properties:
        CHKIMEITHRESHOLD:
          name: 'IMEI检查上限'
          type: integer
          minimum: 0
          maximum: 1023
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
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
    - LICITEM: 'LKV21NIMEI01'
      SWITCH: ENABLE
    mod_gbimeicfg_list:
    - CHKIMEITHRESHOLD: 2
      SUBRANGE: ''
      CHKIMEIPLC: ''
      BEGIMSI: ''
      ENDIMSI: ''
      IMSIPRE: ''
    mod_iuimeicfg_list:
    - SUBRANGE: ALL_USER
      GETIMEIPLC: IMEI
      CHKIMEIPLC: IMEI
      CHKIMEITHRESHOLD: 2
      BLALLOW: ''
      CTFLAG: ''
      EIROUTTIMER: ''
      GRALLOW: ''
      ITTYPE: ''
      IMEIACCESS: ''
      BEGIMSI: ''
      ENDIMSI: ''
      IMSIPRE: ''
    mod_s1imeicfg_list:
    - CHKIMEITHRESHOLD: 2
      SUBRANGE: ''
      CHKIMEIPLC: ''
      BEGIMSI: ''
      ENDIMSI: ''
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

### 2 配置IMEI检查上限，即指定当IMEI未改变时，UNC每多少次Attach流程发起一次IMEI检查。

### Gb模式下：**MOD GBIMEICFG**

```jinja2
{%- if is_scenario_gb -%}
    {%- for item in mod_gbimeicfg_list -%}
        MOD GBIMEICFG:
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
        {#- --- 条件可选参数 --- -#}
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
        ;
    {%- endfor -%}
{%- endif -%}
```

### Iu模式下：**MOD IUIMEICFG**

```jinja2
{%- if is_scenario_iu -%}
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
            {%- if item.CHKIMEITHRESHOLD is not none -%}
                CHKIMEITHRESHOLD={{item.CHKIMEITHRESHOLD}},
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

### S1模式下：**MOD S1IMEICFG**

```jinja2
{%- if is_scenario_s1 -%}
    {%- for item in mod_s1imeicfg_list -%}
        MOD S1IMEICFG:
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
        {#- --- 条件可选参数 --- -#}
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
        ;
    {%- endfor -%}
{%- endif -%}
```

### 参数“IMEI检查上限”设置为“0”，表示仅UE第一次接入UNC或者IMEI改变时，需要进行IMEI检查，对于IMEI未改变的Attach流程，UNC不发起IMEI检查流程。


---
id: GWFD-026104
name: 激活NB-IoT eDRX模式（MME）
ne_type: UEG
type: feature
description: 本操作指导介绍在运行网络中激活NB-IoT eDRX模式的操作过程。  本特性通过在网元间传递eDRX（Extended Discontinuous Reception）信元并计算出合理的寻呼时机来缩短对移动性、实时性较低的M2M终端的监控寻呼信道时长，从而减少网络信令负荷，节省终端耗电量，延长电池使用寿命。  适用于MME。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝L","MEC 特性指南（风筝L）","MME特性指南","GWFD-026100 NB-IoT基本功能","GWFD-026104 NB-IoT eDRX模式（MME）","激活NB-IoT eDRX模式（MME）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
本操作指导介绍在运行网络中激活NB-IoT eDRX模式的操作过程。本特性通过在网元间传递eDRX（Extended Discontinuous Reception）信元并计算出合理的寻呼时机来缩短对移动性、实时性较低的M2M终端的监控寻呼信道时长，从而减少网络信令负荷，节省终端耗电量，延长电池使用寿命。适用于MME。

## 必备事项
前提条件

* 请仔细阅读GWFD-026104 NB-IoT eDRX模式特性概述（MME）。
* 已完成加载License。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    set_hsfntime_list:
      type: items
      properties:
        TIMETYPE:
          name: '时间类型'
          type: string
          enum:
          - GPS
          - UTC
          required: false
          description: '设置H-SFN参考时间'
          data_source: '全网规划  说明：  如下参数值都需要与eNodeB侧协商一致：  * “时间类型” * “使用GPS起始时间” * 以及当不使用GPS起始时间时，“H-SFN参考日期”和“H-SFN参考时间（TIME）”'
          pattern: ''
          default: ''
        GPSBEGIN:
          name: '使用GPS起始时间'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GPSLEAPSEC:
          name: '当前时间与参考时间闰秒差'
          type: integer
          minimum: 0
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DATE:
          name: 'H-SFN参考日期'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'YYYY&MM&DD'
        TIME:
          name: 'H-SFN参考时间'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'HH&MM&SS'
    set_m2mctrl_list:
      type: items
      properties:
        NBEDRXPAGDIFF:
          name: 'NB-S1模式寻呼窗口差值'
          type: string
          enum:
          - MAX_DIFF_10_SECONDS
          - MAX_DIFF_11_SECONDS
          - MAX_DIFF_1_SECOND
          - MAX_DIFF_2_SECONDS
          - MAX_DIFF_3_SECONDS
          - MAX_DIFF_4_SECONDS
          - MAX_DIFF_5_SECONDS
          - MAX_DIFF_6_SECONDS
          - MAX_DIFF_7_SECONDS
          - MAX_DIFF_8_SECONDS
          - MAX_DIFF_9_SECONDS
          - SAME
          required: false
          description: '设置Diameter兼容性参数，保证网元间支持信元的兼容性。'
          data_source: '全网规划  说明：  “NB-S1模式寻呼窗口差值”的取值依据eNodeB提供寻呼窗口起始时间的最大时间差值进行配置，MME配置值为大于等于该差值的可配置的最小值。'
          pattern: ''
          default: ''
        USERPLANOPT:
          name: '用户面建立优化'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_m2mplcy_list:
      type: items
      properties:
        SUBRANGE:
          name: '用户范围'
          type: string
          enum:
          - ALL_USER
          - FOREIGN_USER
          - HOME_USER
          - IMSI_PREFIX
          required: true
          description: '增加M2M的策略参数，即为不同范围的用户、不同的APN业务配置M2M业务相关参数，以满足运营商灵活部署网络的需求。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        APNNI:
          name: 'APNNI'
          type: string
          maxLength: 62
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        EDRXSW:
          name: 'eDRX开关'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: OFF
        NBECL:
          name: '窄带S1模式寻呼周期'
          type: string
          enum:
          - SECONDS_10485_76
          - SECONDS_1310_72
          - SECONDS_163_84
          - SECONDS_20_48
          - SECONDS_2621_44
          - SECONDS_327_68
          - SECONDS_40_96
          - SECONDS_5242_88
          - SECONDS_655_36
          - SECONDS_81_92
          - USE_UE_REQUEST
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: USE_UE_REQUEST
        NBPTW:
          name: '窄带S1模式寻呼时间窗口时长'
          type: string
          enum:
          - SECONDS_10_24
          - SECONDS_12_8
          - SECONDS_15_36
          - SECONDS_17_92
          - SECONDS_20_48
          - SECONDS_23_04
          - SECONDS_25_6
          - SECONDS_28_16
          - SECONDS_2_56
          - SECONDS_30_72
          - SECONDS_33_28
          - SECONDS_35_84
          - SECONDS_38_4
          - SECONDS_40_96
          - SECONDS_5_12
          - SECONDS_7_68
          - USE_UE_REQUEST
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: USE_UE_REQUEST
        NBEDRXSUBPRI:
          name: '窄带EDRX寻呼周期签约优先'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NO
        NBPTWSUBPRI:
          name: '窄带寻呼时间窗口时长签约优先'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NO
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
  examples:
    set_hsfntime_list:
    - TIMETYPE: GPS
      GPSBEGIN: YES
      GPSLEAPSEC: 18
      DATE: '2010/01/01'
      TIME: '00：00：00'
    set_m2mctrl_list:
    - NBEDRXPAGDIFF: SAME
      USERPLANOPT: YES
    add_m2mplcy_list:
    - SUBRANGE: ALL_USER
      APNNI: 'huawei.com'
      EDRXSW: ON
      NBECL: USE_UE_REQUEST
      NBPTW: USE_UE_REQUEST
      NBEDRXSUBPRI: NO
      NBPTWSUBPRI: NO
    set_licenseswitch_list:
    - LICITEM: 'LKV2EDRX01'
      SWITCH: ENABLE
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 进入“MML命令行-UEG”窗口。

### 2 设置H-SFN参考时间。

### eDRX周期的取值以H-SFN（超帧）为单位。为了计算UE的寻呼时间，MME需要使用和eNodeB相同的H-SFN号。MME通过如下配置，能够配置H-SFN=0对应的参考时间，使MME和eNodeB设置为同一个时间，对齐H-SFN。

```jinja2
{%- for item in set_hsfntime_list -%}
    SET HSFNTIME:
    {#- --- 可选参数 --- -#}
    {%- if item.TIMETYPE is not none -%}
        TIMETYPE={{item.TIMETYPE}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：TIMETYPE=GPS 时可选 --- -#}
    {%- if item.TIMETYPE == 'GPS' -%}
        {%- if item.GPSBEGIN is not none -%}
            GPSBEGIN={{item.GPSBEGIN}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：GPSBEGIN=NO/YES 时可选 --- -#}
    {%- if item.GPSBEGIN in ['NO', 'YES'] -%}
        {%- if item.GPSLEAPSEC is not none -%}
            GPSLEAPSEC={{item.GPSLEAPSEC}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：GPSBEGIN=NO 时可选 --- -#}
    {%- if item.GPSBEGIN == 'NO' -%}
        {%- if item.TIME is not none -%}
            TIME={{item.TIME}},
        {%- endif -%}
    {#- --- 条件可选：TIMETYPE=UTC 时可选 --- -#}
    {%- elif item.TIMETYPE == 'UTC' -%}
        {%- if item.TIME is not none -%}
            TIME={{item.TIME}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：GPSBEGIN=NO 时可选 --- -#}
    {%- if item.GPSBEGIN == 'NO' -%}
        {%- if item.DATE is not none -%}
            DATE={{item.DATE}},
        {%- endif -%}
    {#- --- 条件可选：TIMETYPE=UTC 时可选 --- -#}
    {%- elif item.TIMETYPE == 'UTC' -%}
        {%- if item.DATE is not none -%}
            DATE={{item.DATE}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 计算寻呼时间的算法请参见协议3GPP TS 36.304。

### 3 **可选：**设置M2M控制参数。

### 如果确认eNodeB对H-SFN进行了偏移处理，即eNodeB计算的寻呼时间窗口起始时间与MME计算的寻呼窗口起始时间存在偏差值时，可通过执行如下命令的“NB-S1模式寻呼窗口差值”参数进行配置。

```jinja2
{%- if is_optional_m2m_control_params -%}
    {%- for item in set_m2mctrl_list -%}
        SET M2MCTRL:
        {#- --- 可选参数 --- -#}
        {%- if item.NBEDRXPAGDIFF is not none -%}
            NBEDRXPAGDIFF={{item.NBEDRXPAGDIFF}},
        {%- endif -%}
        {%- if item.USERPLANOPT is not none -%}
            USERPLANOPT={{item.USERPLANOPT}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 由于eNodeB和MME上的时间可能存在时间差，或eNodeB为了减少SFN的跳变，在计算H-SFN时以SFN为准对H-SFN进行偏移，导致eNodeB与MME计算得到的寻呼窗口起始时间有差值，如果MME严格按照计算得出的寻呼窗口进行寻呼，可能错过部分eNodeB计算的寻呼窗口而导致寻呼成功率较低。

### 4 增加M2M终端省电策略。

```jinja2
{%- for item in add_m2mplcy_list -%}
    ADD M2MPLCY:
    {#- --- 必选参数 --- -#}
    SUBRANGE={{item.SUBRANGE}},
    APNNI="{{item.APNNI}}",
    {#- --- 可选参数 --- -#}
    {%- if item.EDRXSW is not none -%}
        EDRXSW={{item.EDRXSW}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：EDRXSW=ON 时可选 --- -#}
    {%- if item.EDRXSW == 'ON' -%}
        {%- if item.NBECL is not none -%}
            NBECL={{item.NBECL}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：EDRXSW=ON 时可选 --- -#}
    {%- if item.EDRXSW == 'ON' -%}
        {%- if item.NBPTW is not none -%}
            NBPTW={{item.NBPTW}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：EDRXSW=ON 时可选 --- -#}
    {%- if item.EDRXSW == 'ON' -%}
        {%- if item.NBPTWSUBPRI is not none -%}
            NBPTWSUBPRI={{item.NBPTWSUBPRI}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：EDRXSW=ON 时可选 --- -#}
    {%- if item.EDRXSW == 'ON' -%}
        {%- if item.NBEDRXSUBPRI is not none -%}
            NBEDRXSUBPRI={{item.NBEDRXSUBPRI}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### “窄带S1模式寻呼时间窗口时长”设置时，建议NBPTW的值至少为NB-IoT Default Paging DRX值的2倍，这样eNodeB在NBPTW窗口内可以有多次机会寻呼用户。NB-IoT Default Paging DRX值是eNodeB在S1 Setup Request消息中携带给MME的。

### 5 打开本功能的License配置开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```


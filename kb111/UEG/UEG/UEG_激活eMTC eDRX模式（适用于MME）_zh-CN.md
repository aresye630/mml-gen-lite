---
id: GWFD-026302
name: 激活eMTC eDRX模式（适用于MME）
ne_type: UEG
type: feature
description: 本操作指导介绍在运行网络中激活eMTC eDRX模式的操作过程。  本特性通过在网元间传递eDRX（Extended Discontinuous Reception）信元并计算出合理的寻呼时机来缩短对移动性、实时性较低的eMTC终端的监控寻呼信道时长，从而减少网络信令负荷，节省终端耗电量，延长电池使用寿命。  适用于MME。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝L","MEC 特性指南（风筝L）","MME特性指南","GWFD-026300 eMTC基本功能","GWFD-026302 eMTC eDRX模式","GWFD-026302 eMTC eDRX模式（适用于MME）","激活eMTC eDRX模式（适用于MME）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
本操作指导介绍在运行网络中激活eMTC eDRX模式的操作过程。本特性通过在网元间传递eDRX（Extended Discontinuous Reception）信元并计算出合理的寻呼时机来缩短对移动性、实时性较低的eMTC终端的监控寻呼信道时长，从而减少网络信令负荷，节省终端耗电量，延长电池使用寿命。适用于MME。

## 必备事项
前提条件

请仔细阅读GWFD-026302 eMTC eDRX模式特性概述（适用于MME）。
已完成加载License。
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
        WBEDRXPAGDIFF:
          name: 'WB-S1模式寻呼窗口差值'
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
          description: '设置eMTC控制参数'
          data_source: '全网规划  说明：  “WB-S1模式寻呼窗口差值”的取值依据eNodeB提供寻呼窗口起始时间的最大时间差值进行配置，MME配置值为大于等于该差值的可配置的最小值。'
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
          description: '增加eMTC终端省电策略'
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
        WBECL:
          name: '宽带S1模式寻呼周期'
          type: string
          enum:
          - SECONDS_102_4
          - SECONDS_10_24
          - SECONDS_122_88
          - SECONDS_1310_72
          - SECONDS_143_36
          - SECONDS_163_84
          - SECONDS_20_48
          - SECONDS_2621_44
          - SECONDS_327_68
          - SECONDS_40_96
          - SECONDS_5_12
          - SECONDS_61_44
          - SECONDS_655_36
          - SECONDS_81_92
          - USE_UE_REQUEST
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: USE_UE_REQUEST
        WBPTW:
          name: '宽带S1模式寻呼时间窗口时长'
          type: string
          enum:
          - SECONDS_10_24
          - SECONDS_11_52
          - SECONDS_12_8
          - SECONDS_14_08
          - SECONDS_15_36
          - SECONDS_16_64
          - SECONDS_17_92
          - SECONDS_19_2
          - SECONDS_1_28
          - SECONDS_20_48
          - SECONDS_2_56
          - SECONDS_3_84
          - SECONDS_5_12
          - SECONDS_6_4
          - SECONDS_7_68
          - SECONDS_8_96
          - USE_UE_REQUEST
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: USE_UE_REQUEST
        WBPTWSUBPRI:
          name: '宽带寻呼时间窗口时长签约优先'
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
    add_gtpcv2cmpt_list:
      type: items
      properties:
        IDX:
          name: '索引'
          type: integer
          minimum: 0
          maximum: 511
          required: true
          description: '协议兼容性相关参数'
          data_source: '本端规划'
          pattern: ''
          default: ''
        MSGCLS:
          name: '消息分类'
          type: string
          enum:
          - MM
          - PM
          - SV
          - TM
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        TMMSGTYPE:
          name: '消息类型'
          type: string
          enum:
          - CRT_SES_REQ
          - MOD_BR_REQ
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CRTSESREQ:
          name: 'Create Session Request的信元类型'
          type: string
          enum:
          - INDICATION
          - UPSELIND
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CRTSESREQIND:
          name: 'Indication Bit位'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RATTYPELTEM:
          name: '是否支持LTE-M类型的RAT TYPE'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: NO
        MODBRREQ:
          name: 'Modify Bearer Request的信元类型'
          type: string
          enum:
          - BCMOD
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        FTEIDVALUE:
          name: 'F-TEID取值'
          type: string
          enum:
          - RESERVED
          - VALID
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MMMSGTYPE:
          name: '消息类型'
          type: string
          enum:
          - CTX_RSP
          - FWD_RLC_REQ
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        FWDRLCREQ:
          name: 'Forward Relocation Request的信元类型'
          type: string
          enum:
          - C-MSISDN
          - INDICATION
          - SERNET
          - SRVCCFLG
          - SRVCCMMCTXT
          - STN-SR
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        FWDRLCREQIND:
          name: 'Indication Bit位'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CTXRSP:
          name: 'Context Response的信元类型'
          type: string
          enum:
          - INDICATION
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CTXRSPIND:
          name: 'Indication Bit位'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_pgwcharact_list:
      type: items
      properties:
        RANGE:
          name: '对端设备范围'
          type: string
          enum:
          - ALL
          - FOREIGN
          - HOME
          - SPECIFIC
          required: true
          description: 'PGW-C对接相关参数'
          data_source: '本端规划'
          pattern: ''
          default: ''
        RATTYPELTEM:
          name: '是否向P-GW转发LTE-M类型的RAT TYPE'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: NO
    set_dmcmpt_list:
      type: items
      properties:
        RATTYPELTEM:
          name: '是否支持LTE-M类型的RAT TYPE'
          type: string
          required: false
          description: '设置Diameter兼容性'
          data_source: '本端规划'
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
    - WBEDRXPAGDIFF: SAME
      USERPLANOPT: YES
    add_m2mplcy_list:
    - SUBRANGE: ALL_USER
      APNNI: 'huawei.com'
      EDRXSW: ON
      WBECL: USE_UE_REQUEST
      WBPTW: USE_UE_REQUEST
      WBPTWSUBPRI: NO
      NBPTWSUBPRI: NO
    set_licenseswitch_list:
    - LICITEM: 'LKV2EDRX02'
      SWITCH: ENABLE
    add_gtpcv2cmpt_list:
    - IDX: 0
      MSGCLS: TM
      TMMSGTYPE: CRT_SES_REQ
      CRTSESREQ: INDICATION
      CRTSESREQIND: CPOPCI-0
      RATTYPELTEM: YES
      MODBRREQ: BCMOD
      FTEIDVALUE: VALID
      MMMSGTYPE: FWD_RLC_REQ
      FWDRLCREQ: INDICATION
      FWDRLCREQIND: SQCI-0
      CTXRSP: INDICATION
      CTXRSPIND: SQCI-0&SRNI-0&CPOPCI-0&BDWI-0
    add_pgwcharact_list:
    - RANGE: ALL
      RATTYPELTEM: YES
    set_dmcmpt_list:
    - RATTYPELTEM: ULR-1&NOR-0
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

### 3 设置eMTC控制参数。

### 如果确认eNodeB对H-SFN进行了偏移处理，即eNodeB计算的寻呼时间窗口起始时间与MME计算的寻呼窗口起始时间存在偏差值时，可通过执行如下命令的“WB-S1模式寻呼窗口差值”参数进行配置。

```jinja2
{%- for item in set_m2mctrl_list -%}
    SET M2MCTRL:
    {#- --- 可选参数 --- -#}
    {%- if item.WBEDRXPAGDIFF is not none -%}
        WBEDRXPAGDIFF={{item.WBEDRXPAGDIFF}},
    {%- endif -%}
    {%- if item.USERPLANOPT is not none -%}
        USERPLANOPT={{item.USERPLANOPT}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 由于eNodeB和MME上的时间可能存在时间差，或eNodeB为了减少SFN的跳变，在计算H-SFN时以SFN为准对H-SFN进行偏移，导致eNodeB与MME计算得到的寻呼窗口起始时间有差值，如果MME严格按照计算得出的寻呼窗口进行寻呼，可能错过部分eNodeB计算的寻呼窗口而导致寻呼成功率较低。

### 4 增加eMTC终端省电策略。

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
        {%- if item.WBECL is not none -%}
            WBECL={{item.WBECL}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：EDRXSW=ON 时可选 --- -#}
    {%- if item.EDRXSW == 'ON' -%}
        {%- if item.WBPTW is not none -%}
            WBPTW={{item.WBPTW}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：EDRXSW=ON 时可选 --- -#}
    {%- if item.EDRXSW == 'ON' -%}
        {%- if item.WBPTWSUBPRI is not none -%}
            WBPTWSUBPRI={{item.WBPTWSUBPRI}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：EDRXSW=ON 时可选 --- -#}
    {%- if item.EDRXSW == 'ON' -%}
        {%- if item.NBPTWSUBPRI is not none -%}
            NBPTWSUBPRI={{item.NBPTWSUBPRI}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### “宽带S1模式寻呼时间窗口时长”设置时，建议WBPTW的值至少为DefaultPagingDRX值的2倍，这样eNodeB在WBPTW窗口内可以有多次机会寻呼用户。Default Paging DRX值是eNodeB在S1 Setup Request消息中携带给MME的。

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

### 6 **可选：**如果eMTC终端需要添加RAT Type为LTE-M类型时，需要执行此步骤。

#### 6.1 将RAT Type为LTE-M的消息传递给SGW-C。

```jinja2
{%- if is_optional_add_lte_m_rat_type -%}
    {%- for item in add_gtpcv2cmpt_list -%}
        ADD GTPCV2CMPT:
        {#- --- 必选参数 --- -#}
        IDX={{item.IDX}},
        MSGCLS={{item.MSGCLS}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：MSGCLS=TM 时必选 --- -#}
        {%- if item.MSGCLS == 'TM' -%}
            TMMSGTYPE={{item.TMMSGTYPE}},
        {%- endif -%}
        {#- --- 条件必选：TMMSGTYPE=CRT_SES_REQ 时必选 --- -#}
        {%- if item.TMMSGTYPE == 'CRT_SES_REQ' -%}
            CRTSESREQ={{item.CRTSESREQ}},
        {%- endif -%}
        {#- --- 条件必选：CRTSESREQ=INDICATION 时必选 --- -#}
        {%- if item.CRTSESREQ == 'INDICATION' -%}
            CRTSESREQIND={{item.CRTSESREQIND}},
        {%- endif -%}
        {#- --- 条件必选：TMMSGTYPE=MOD_BR_REQ 时必选 --- -#}
        {%- if item.TMMSGTYPE == 'MOD_BR_REQ' -%}
            MODBRREQ={{item.MODBRREQ}},
        {%- endif -%}
        {#- --- 条件必选：MODBRREQ=BCMOD 时必选 --- -#}
        {%- if item.MODBRREQ == 'BCMOD' -%}
            FTEIDVALUE={{item.FTEIDVALUE}},
        {%- endif -%}
        {#- --- 条件必选：MSGCLS=MM 时必选 --- -#}
        {%- if item.MSGCLS == 'MM' -%}
            MMMSGTYPE={{item.MMMSGTYPE}},
        {%- endif -%}
        {#- --- 条件必选：MMMSGTYPE=FWD_RLC_REQ 时必选 --- -#}
        {%- if item.MMMSGTYPE == 'FWD_RLC_REQ' -%}
            FWDRLCREQ={{item.FWDRLCREQ}},
        {%- endif -%}
        {#- --- 条件必选：FWDRLCREQ=INDICATION 时必选 --- -#}
        {%- if item.FWDRLCREQ == 'INDICATION' -%}
            FWDRLCREQIND={{item.FWDRLCREQIND}},
        {%- endif -%}
        {#- --- 条件必选：MMMSGTYPE=CTX_RSP 时必选 --- -#}
        {%- if item.MMMSGTYPE == 'CTX_RSP' -%}
            CTXRSP={{item.CTXRSP}},
        {%- endif -%}
        {#- --- 条件必选：CTXRSP=INDICATION 时必选 --- -#}
        {%- if item.CTXRSP == 'INDICATION' -%}
            CTXRSPIND={{item.CTXRSPIND}},
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：MMMSGTYPE=FWD_RLC_REQ/CTX_RSP 时可选 --- -#}
        {%- if item.MMMSGTYPE in ['FWD_RLC_REQ', 'CTX_RSP'] -%}
            {%- if item.RATTYPELTEM is not none -%}
                RATTYPELTEM={{item.RATTYPELTEM}},
            {%- endif -%}
        {#- --- 条件可选：TMMSGTYPE=CRT_SES_REQ/MOD_BR_REQ 时可选 --- -#}
        {%- elif item.TMMSGTYPE in ['CRT_SES_REQ', 'MOD_BR_REQ'] -%}
            {%- if item.RATTYPELTEM is not none -%}
                RATTYPELTEM={{item.RATTYPELTEM}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 6.2 指示SGW-C向PGW-C传递RAT Type为LTE-M类型。

```jinja2
{%- if is_optional_add_lte_m_rat_type -%}
    {%- for item in add_pgwcharact_list -%}
        ADD PGWCHARACT:
        {#- --- 必选参数 --- -#}
        RANGE={{item.RANGE}},
        {#- --- 可选参数 --- -#}
        {%- if item.RATTYPELTEM is not none -%}
            RATTYPELTEM={{item.RATTYPELTEM}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 6.3 UEG向HSS发送Update Location Request消息或者Notify Request消息时，消息中的RAT TYPE信元设置为LTE-M。

```jinja2
{%- if is_optional_add_lte_m_rat_type -%}
    {%- for item in set_dmcmpt_list -%}
        SET DMCMPT:
        {#- --- 可选参数 --- -#}
        {%- if item.RATTYPELTEM is not none -%}
            RATTYPELTEM={{item.RATTYPELTEM}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```


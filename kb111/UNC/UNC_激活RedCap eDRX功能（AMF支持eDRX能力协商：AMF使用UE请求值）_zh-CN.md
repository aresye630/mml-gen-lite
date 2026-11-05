---
id: ''
name: 激活RedCap eDRX功能（AMF支持eDRX能力协商：AMF使用UE请求值）
ne_type: UNC
type: feature
description: 本操作指导介绍在运行网络中激活5G eDRX模式的过程。  适用于AMF。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","NB-IOT业务功能","WSFD-990005 支持RedCap eDRX功能","激活RedCap eDRX功能（AMF支持eDRX能力协商：AMF使用UE请求值）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本操作指导介绍在运行网络中激活5G eDRX模式的过程。适用于AMF。

## 必备事项
前提条件

前提条件

* 请仔细阅读WSFD-990005 支持5G eDRX功能特性概述。
* 已完成加载License。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
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
          description: 'AMF上使用的时间类型需要与gNodeB保持一致。若大部分gNodeB使用GPS时间类型，则此参数需要配置为GPS。'
          data_source: '对端协商'
          pattern: ''
          default: ''
        GPSBEGIN:
          name: '使用GPS起始时间'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: '当时间类型选为GPS时，此参数固定配置为”YES”。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        GPSLEAPSEC:
          name: '当前时间与参考时间闰秒差'
          type: integer
          minimum: 0
          maximum: 255
          required: false
          description: '18仅为参考值。此参数设置值=最新公布的闰秒数-设置的参考时间之前最近一次公布的闰秒数。闰秒数请到IERS官方网站查询：http://hpiers.obspm.fr/eoppc/bul/bulc/UTC-TAI.history。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        DATE:
          name: 'H-SFN参考日期'
          type: string
          required: false
          description: '设置的日期为已经过去的某一日期，不能配置未来的日期。建议保持系统初始值。'
          data_source: '固定取值'
          pattern: ''
          default: 'YYYY&MM&DD'
        TIME:
          name: 'H-SFN参考时间'
          type: string
          required: false
          description: '建议保持系统初始值。'
          data_source: '固定取值'
          pattern: ''
          default: 'HH&MM&SS'
    add_ngm2mplcy_list:
      type: items
      properties:
        SUBRANGE:
          name: '用户范围'
          type: string
          required: false
          description: '这三个参数需根据实际业务范围和用户范围进行规划。此处以本网用户根据DNN配置策略为例。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        FEATURECOND:
          name: '特征条件组合'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        DNNNI:
          name: '数据网络名称'
          type: string
          required: false
          description: ''
          data_source: '根据业务场景的DNNNI配置'
          pattern: ''
          default: ''
        EDRXSW:
          name: 'eDRX开关'
          type: string
          required: false
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: ''
        NRECL:
          name: 'NR模式寻呼周期'
          type: string
          required: false
          description: '取默认值即可。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        NRPTW:
          name: 'NR模式寻呼时间窗口时长'
          type: string
          required: false
          description: '取默认值即可。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        NBPTWSUBPRI:
          name: 'NBPTWSUBPRI'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NREDRXSUBPRI:
          name: 'NR模式EDRX寻呼周期签约优先'
          type: string
          required: false
          description: '当UDM没有签约eDRX参数时，AMF优先使用参数“NRECL“和“NRPTW“的值。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    set_ngm2mctrl_list:
      type: items
      properties:
        UEEDRXCOSW:
          name: 'EDRX参数校正开关'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: ''
        SHORTECLSW:
          name: 'EDRX短周期使能开关'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        REACHEVENTNSSW:
          name: '可达性事件上报非标开关'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: 'eDRX用户建议设置此参数为”YES”，非标方案，只有连接态才认为可达，这样可以提高eDRX用户下行数据传输成功率。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        INTRAUSRPLANOPT:
          name: 'AMF内移动性流程用户面建立优化'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: ''
        NREDRXPAGDIFF:
          name: 'NR模式寻呼窗口差值'
          type: string
          enum:
          - SAME
          - MAX_DIFF_1_SECOND
          - MAX_DIFF_2_SECOND
          - MAX_DIFF_3_SECOND
          - MAX_DIFF_4_SECOND
          - MAX_DIFF_5_SECOND
          - MAX_DIFF_6_SECOND
          - MAX_DIFF_7_SECOND
          - MAX_DIFF_8_SECOND
          - MAX_DIFF_9_SECOND
          - MAX_DIFF_10_SECOND
          - MAX_DIFF_11_SECOND
          required: false
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: ''
  examples:
    set_hsfntime_list:
    - TIMETYPE: GPS
      GPSBEGIN: YES
      GPSLEAPSEC: 18
      DATE: '2010/01/01'
      TIME: '00：00：00'
    add_ngm2mplcy_list:
    - SUBRANGE: HOME_USER
      FEATURECOND: DNN
      DNNNI: huawei.com
      EDRXSW: ON
      NRECL: USE_UE_REQUEST
      NRPTW: USE_UE_REQUEST
      NBPTWSUBPRI: NO
      NREDRXSUBPRI: NO
    set_ngm2mctrl_list:
    - UEEDRXCOSW: YES
      SHORTECLSW: NO
      REACHEVENTNSSW: YES
      INTRAUSRPLANOPT: YES
      NREDRXPAGDIFF: MAX_DIFF_3_SECOND
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 进入“MML命令行-UNC”窗口。

### 2 设置H-SFN参考时间（时间类型GPS或者UTC请与gNodeB对齐）：

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
        {%- if item.DATE is not none -%}
            DATE={{item.DATE}},
        {%- endif -%}
    {#- --- 条件可选：TIMETYPE=UTC 时可选 --- -#}
    {%- elif item.TIMETYPE == 'UTC' -%}
        {%- if item.DATE is not none -%}
            DATE={{item.DATE}},
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
    ;
{%- endfor -%}
```

### 3 配置5G M2M策略参数：

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_ngm2mplcy_list的变量区（command: ADD NGM2MPLCY） -#}
<!-- MISSING_MACRO: command=ADD NGM2MPLCY list_name=add_ngm2mplcy_list step_id=3 -->
```

### 4 配置5G M2M控制参数：

```jinja2
{%- for item in set_ngm2mctrl_list -%}
    SET NGM2MCTRL:
    {#- --- 可选参数 --- -#}
    {%- if item.UEEDRXCOSW is not none -%}
        UEEDRXCOSW={{item.UEEDRXCOSW}},
    {%- endif -%}
    {%- if item.SHORTECLSW is not none -%}
        SHORTECLSW={{item.SHORTECLSW}},
    {%- endif -%}
    {%- if item.REACHEVENTNSSW is not none -%}
        REACHEVENTNSSW={{item.REACHEVENTNSSW}},
    {%- endif -%}
    {%- if item.INTRAUSRPLANOPT is not none -%}
        INTRAUSRPLANOPT={{item.INTRAUSRPLANOPT}},
    {%- endif -%}
    {%- if item.NREDRXPAGDIFF is not none -%}
        NREDRXPAGDIFF={{item.NREDRXPAGDIFF}},
    {%- endif -%}
    ;
{%- endfor -%}
```


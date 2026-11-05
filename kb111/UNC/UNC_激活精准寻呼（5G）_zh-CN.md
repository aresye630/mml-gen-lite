---
id: ''
name: 激活精准寻呼（5G）
ne_type: UNC
type: feature
description: 本操作指导介绍在运行网络中激活5G精准寻呼的操作过程。  UNC基于用户类型、业务类型选择相应的寻呼策略，综合用户的移动性进行寻呼规则过滤，选择合适的范围对用户进行寻呼，从而有效地减少整个网络中gNodeB的寻呼负荷，节省网络资源。  适用于AMF。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","流控功能","WSFD-206001 精准寻呼","WSFD-206001 精准寻呼（5G）","激活精准寻呼（5G）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本操作指导介绍在运行网络中激活5G精准寻呼的操作过程。UNC基于用户类型、业务类型选择相应的寻呼策略，综合用户的移动性进行寻呼规则过滤，选择合适的范围对用户进行寻呼，从而有效地减少整个网络中gNodeB的寻呼负荷，节省网络资源。适用于AMF。

## 必备事项
前提条件

* 请仔细阅读WSFD-206001 5G精准寻呼特性概述。
* 建议由华为专业服务对本网进行评估后选定最优的精准寻呼参数。
* 已完成加载License。
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
    add_ngpagingrule_list:
      type: items
      properties:
        RULEIDX:
          name: '规则索引'
          type: integer
          minimum: 1
          maximum: 1000
          required: true
          description: '配置寻呼规则，包括用户类型、业务类型和寻呼范围组合。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        GRPTYPE:
          name: '用户群类型'
          type: string
          enum:
          - ALL_USER
          - IMSI_PREFIX
          - MSISDN_PREFIX
          - IMEI_TAC
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SVRTYPE:
          name: '业务类型'
          type: string
          enum:
          - SMF_N1N2
          - UDM_SDM
          - OTHER
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PRIORITY:
          name: '匹配优先级'
          type: integer
          minimum: 0
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 200
        ACTGRP:
          name: '寻呼动作组合'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DNNIND:
          name: 'DNN指示'
          type: string
          enum:
          - ALL_DNN
          - SPEC_DNN
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        FQI:
          name: '5G QoS标识'
          type: integer
          minimum: 1
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DNN:
          name: '数据网络名称'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IMEITAC:
          name: 'IMEI TAC'
          type: string
          minLength: 8
          maxLength: 8
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
        MSISDNPRE:
          name: 'MSISDN前缀'
          type: string
          minLength: 1
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ARPPL:
          name: 'ARP优先级别'
          type: integer
          minimum: 1
          maximum: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PPI:
          name: '寻呼策略指示'
          type: integer
          minimum: 0
          maximum: 7
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_ngpagingctrl_list:
      type: items
      properties:
        LASTGNBSW:
          name: '最近gNodeB开关'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: '配置寻呼策略参数，如寻呼范围开关、低移动性检查开关、粘性时长、寻呼定时器、重发次数、邻接关系学习开关、老化时间等参数。  说明：  当前“全网寻呼开关”功能不生效，最大寻呼范围为基于TA List的3GPP标准寻呼。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        LASTGNBT3513:
          name: '最近gNodeB超时时长'
          type: integer
          minimum: 2
          maximum: 6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LASTGNBN3513:
          name: '最近gNodeB重发次数'
          type: integer
          minimum: 0
          maximum: 5
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LOWMOBICHKSW:
          name: '低移动性检查开关'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GNBSTICKTIME:
          name: 'gNodeB粘性时长'
          type: integer
          minimum: 0
          maximum: 60
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        HOLRNSW:
          name: 'HO学习开关'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SONLRNSW:
          name: 'SON学习开关'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PSLRNSW:
          name: 'Path Switch学习开关'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GNBEXPIRETIME:
          name: '邻接gNodeB老化时间'
          type: integer
          minimum: 0
          maximum: 720
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TASTICKTIME:
          name: 'TA粘性时长(min)'
          type: integer
          minimum: 0
          maximum: 120
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_ngtapagingplcy_list:
      type: items
      properties:
        TALISTID:
          name: '跟踪区列表标识'
          type: integer
          minimum: 0
          maximum: 65534
          required: true
          description: '配置指定的5G TA List是否关闭精准寻呼功能。  TA List需要先通过**ADD NGTALST**配置。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        CLSPRECISEPAG:
          name: '是否关闭精准寻呼'
          type: string
          enum:
          - YES
          - NO
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_ngpagingtmrplcy_list:
      type: items
      properties:
        PLCYIDX:
          name: '策略索引'
          type: integer
          minimum: 0
          maximum: 1999
          required: true
          description: '基于业务参数配置寻呼定时器、重发次数和重呼间隔时间。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        DNN:
          name: '数据网络名称'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        T3513:
          name: 'T3513(s)'
          type: integer
          minimum: 3
          maximum: 12
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        N3513:
          name: 'N3513(times)'
          type: integer
          minimum: 0
          maximum: 5
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_ngpagingpriplcy_list:
      type: items
      properties:
        PLCYIDX:
          name: '策略索引'
          type: integer
          minimum: 0
          maximum: 127
          required: true
          description: '配置DNN、ARP映射寻呼优先级的规则。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        DNN:
          name: '数据网络名称'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PAGINGPRIORITY:
          name: '寻呼优先级等级'
          type: integer
          minimum: 1
          maximum: 8
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 8
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV2PRPG02'
      SWITCH: ENABLE
    add_ngpagingrule_list:
    - RULEIDX: 1
      GRPTYPE: ALL_USER
      SVRTYPE: OTHER
      PRIORITY: 100
      ACTGRP: LAST_GNB-0&NEIGH_GNB-0&LAST_TA-0
      DNNIND: ALL_DNN
      FQI: 5
      DNN: ''
      IMEITAC: ''
      IMSIPRE: ''
      MSISDNPRE: ''
      ARPPL: ''
      PPI: ''
    set_ngpagingctrl_list:
    - LASTGNBSW: ON
      LASTGNBT3513: 4
      LASTGNBN3513: 1
      LOWMOBICHKSW: ON
      GNBSTICKTIME: 2
      HOLRNSW: ON
      SONLRNSW: ON
      PSLRNSW: ON
      GNBEXPIRETIME: 360
      TASTICKTIME: ''
    add_ngtapagingplcy_list:
    - TALISTID: 1
      CLSPRECISEPAG: YES
    add_ngpagingtmrplcy_list:
    - PLCYIDX: 1
      DNN: 'huawei.com'
      T3513: 5
      N3513: 1
    add_ngpagingpriplcy_list:
    - PLCYIDX: 1
      DNN: 'huawei.com'
      PAGINGPRIORITY: 2
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

### 3 配置寻呼规则，包括用户类型、业务类型和寻呼范围组合。

```jinja2
{%- for item in add_ngpagingrule_list -%}
    ADD NGPAGINGRULE:
    {#- --- 必选参数 --- -#}
    RULEIDX={{item.RULEIDX}},
    GRPTYPE={{item.GRPTYPE}},
    SVRTYPE={{item.SVRTYPE}},
    {#- --- 可选参数 --- -#}
    {%- if item.PRIORITY is not none -%}
        PRIORITY={{item.PRIORITY}},
    {%- endif -%}
    {%- if item.ACTGRP is not none -%}
        ACTGRP={{item.ACTGRP}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：SVRTYPE=SMF_N1N2 时必选 --- -#}
    {%- if item.SVRTYPE == 'SMF_N1N2' -%}
        DNNIND={{item.DNNIND}},
    {%- endif -%}
    {#- --- 条件必选：DNNIND=SPEC_DNN 时必选 --- -#}
    {%- if item.DNNIND == 'SPEC_DNN' -%}
        DNN="{{item.DNN}}",
    {%- endif -%}
    {#- --- 条件必选：GRPTYPE=IMEI_TAC 时必选 --- -#}
    {%- if item.GRPTYPE == 'IMEI_TAC' -%}
        IMEITAC="{{item.IMEITAC}}",
    {%- endif -%}
    {#- --- 条件必选：GRPTYPE=IMSI_PREFIX 时必选 --- -#}
    {%- if item.GRPTYPE == 'IMSI_PREFIX' -%}
        IMSIPRE="{{item.IMSIPRE}}",
    {%- endif -%}
    {#- --- 条件必选：GRPTYPE=MSISDN_PREFIX 时必选 --- -#}
    {%- if item.GRPTYPE == 'MSISDN_PREFIX' -%}
        MSISDNPRE="{{item.MSISDNPRE}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：SVRTYPE=SMF_N1N2 时可选 --- -#}
    {%- if item.SVRTYPE == 'SMF_N1N2' -%}
        {%- if item.FQI is not none -%}
            FQI={{item.FQI}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SVRTYPE=SMF_N1N2 时可选 --- -#}
    {%- if item.SVRTYPE == 'SMF_N1N2' -%}
        {%- if item.ARPPL is not none -%}
            ARPPL={{item.ARPPL}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SVRTYPE=SMF_N1N2 时可选 --- -#}
    {%- if item.SVRTYPE == 'SMF_N1N2' -%}
        {%- if item.PPI is not none -%}
            PPI={{item.PPI}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 在部署本特性时，建议针对时延比较敏感的语音业务使用TA List的寻呼范围，从而在不影响语音被叫时延的情况下节省网络资源。

### 针对数据业务和其他非语音类业务，“寻呼动作组合”推荐采用“最近访问gNodeB -> TA List”组合，即“ACTGRP（寻呼动作组合）”取值设置为“LAST\_GNB”。这样能够有效减少寻呼范围的同时，明显减少对gNodeB侧的资源消耗。

### 4 配置寻呼策略，包括寻呼范围开关、低移动性检查开关、粘性时长，进行寻呼规则过滤。配置寻呼定时器、重发次数、邻接关系学习开关、老化时间等。

```jinja2
{%- for item in set_ngpagingctrl_list -%}
    SET NGPAGINGCTRL:
    {#- --- 可选参数 --- -#}
    {%- if item.LASTGNBSW is not none -%}
        LASTGNBSW={{item.LASTGNBSW}},
    {%- endif -%}
    {%- if item.LOWMOBICHKSW is not none -%}
        LOWMOBICHKSW={{item.LOWMOBICHKSW}},
    {%- endif -%}
    {%- if item.HOLRNSW is not none -%}
        HOLRNSW={{item.HOLRNSW}},
    {%- endif -%}
    {%- if item.SONLRNSW is not none -%}
        SONLRNSW={{item.SONLRNSW}},
    {%- endif -%}
    {%- if item.PSLRNSW is not none -%}
        PSLRNSW={{item.PSLRNSW}},
    {%- endif -%}
    {%- if item.GNBEXPIRETIME is not none -%}
        GNBEXPIRETIME={{item.GNBEXPIRETIME}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：LASTGNBSW=ON 时可选 --- -#}
    {%- if item.LASTGNBSW == 'ON' -%}
        {%- if item.LASTGNBT3513 is not none -%}
            LASTGNBT3513={{item.LASTGNBT3513}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：LASTGNBSW=ON 时可选 --- -#}
    {%- if item.LASTGNBSW == 'ON' -%}
        {%- if item.LASTGNBN3513 is not none -%}
            LASTGNBN3513={{item.LASTGNBN3513}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：LOWMOBICHKSW=ON 时可选 --- -#}
    {%- if item.LOWMOBICHKSW == 'ON' -%}
        {%- if item.GNBSTICKTIME is not none -%}
            GNBSTICKTIME={{item.GNBSTICKTIME}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：LOWMOBICHKSW=ON 时可选 --- -#}
    {%- if item.LOWMOBICHKSW == 'ON' -%}
        {%- if item.TASTICKTIME is not none -%}
            TASTICKTIME={{item.TASTICKTIME}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 全局TA List的寻呼定时器、重发次数和重呼间隔时间由**SET NGMMPARA**配置。

### 5 配置指定的5G TA List是否关闭精准寻呼功能。

```jinja2
{%- for item in add_ngtapagingplcy_list -%}
    ADD NGTAPAGINGPLCY:
    {#- --- 必选参数 --- -#}
    TALISTID={{item.TALISTID}},
    CLSPRECISEPAG={{item.CLSPRECISEPAG}},
    ;
{%- endfor -%}
```

### TA List需要先通过**ADD NGTALST**配置。

### 若针对指定的TA List关闭精准寻呼功能，则3设置的精准寻呼规则不生效。

### 6 基于业务参数配置寻呼定时器、重发次数和重呼间隔时间。

```jinja2
{%- for item in add_ngpagingtmrplcy_list -%}
    ADD NGPAGINGTMRPLCY:
    {#- --- 必选参数 --- -#}
    PLCYIDX={{item.PLCYIDX}},
    {#- --- 可选参数 --- -#}
    {%- if item.DNN is not none -%}
        DNN="{{item.DNN}}",
    {%- endif -%}
    {%- if item.T3513 is not none -%}
        T3513={{item.T3513}},
    {%- endif -%}
    {%- if item.N3513 is not none -%}
        N3513={{item.N3513}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 匹配成功，**SET NGMMPARA**命令设置的寻呼定时器、重发次数和重呼间隔时间将失效。

### 匹配失败，则使用全局的定时器时长、重发次数，即**SET NGMMPARA**命令设置的寻呼定时器、重发次数和重呼间隔时间。

### 7 配置DNN、ARP映射寻呼优先级的规则。

```jinja2
{%- for item in add_ngpagingpriplcy_list -%}
    ADD NGPAGINGPRIPLCY:
    {#- --- 必选参数 --- -#}
    PLCYIDX={{item.PLCYIDX}},
    {#- --- 可选参数 --- -#}
    {%- if item.DNN is not none -%}
        DNN="{{item.DNN}}",
    {%- endif -%}
    {%- if item.PAGINGPRIORITY is not none -%}
        PAGINGPRIORITY={{item.PAGINGPRIORITY}},
    {%- endif -%}
    ;
{%- endfor -%}
```


---
id: GWFD-021411
name: 激活精准寻呼（LTE）
ne_type: UEG
type: feature
description: 本操作指导介绍在运行网络中激活LTE精准寻呼的操作过程。  UEG基于用户类型、业务类型选择相应的寻呼策略，综合用户的移动性进行寻呼规则过滤，选择合适的范围对用户进行寻呼，从而有效地减少整个网络中eNodeB的寻呼负荷，节省网络资源。  * 适用于MME。 * 本特性与**GWFD-025402 基于VoLTE的优先语音服务**特性中的**MPS优先级**业务存在冲突，启用前请先检查是否已配置MPS业务（**SET MPSARP**），如果已配置，建议先关闭MPS业务，再开启本特性，否则精准寻呼业务会失效。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝L","MEC 特性指南（风筝L）","MME特性指南","GWFD-021400 可靠性功能","GWFD-021411 精准寻呼","GWFD-021411 精准寻呼（4G）","激活精准寻呼（LTE）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
本操作指导介绍在运行网络中激活LTE精准寻呼的操作过程。UEG基于用户类型、业务类型选择相应的寻呼策略，综合用户的移动性进行寻呼规则过滤，选择合适的范围对用户进行寻呼，从而有效地减少整个网络中eNodeB的寻呼负荷，节省网络资源。* 适用于MME。* 本特性与**GWFD-025402 基于VoLTE的优先语音服务**特性中的**MPS优先级**业务存在冲突，启用前请先检查是否已配置MPS业务（**SET MPSARP**），如果已配置，建议先关闭MPS业务，再开启本特性，否则精准寻呼业务会失效。

## 必备事项
前提条件

前提条件

* 请仔细阅读GWFD-021411 精准寻呼（4G）。
* 部署基于APN，QCI或ARP的精准寻呼策略时，S-GW需要支持在发送给MME的Downlink Data Notification消息中携带EPS Bearer ID信元。
* 建议由华为专业服务对本网进行评估后选定最优的精准寻呼参数。
* 已完成加载License。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
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
    set_s1pagingctrl_list:
      type: items
      properties:
        LASTENBSW:
          name: '最近eNodeB开关'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: '设置S1寻呼策略。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        NEIB_ENBSW:
          name: '邻接eNodeB开关'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LASTTA:
          name: '最近TA开关'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SUBT3413:
          name: 'SUB\_T3413'
          type: integer
          minimum: 2
          maximum: 6
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
        ENB_STICK_TIME:
          name: 'eNodeB粘性时长'
          type: integer
          minimum: 0
          maximum: 60
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TA_STICK_TIME:
          name: 'TA粘性时长'
          type: integer
          minimum: 0
          maximum: 120
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ECT_LRN_SW:
          name: 'ECT学习开关'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        X2HO_LRN_SW:
          name: 'X2HO学习开关'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        S1HO_LRN_SW:
          name: 'S1HO学习开关'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NEB_EXPIRE_TIME:
          name: '邻接eNodeB老化时间'
          type: integer
          minimum: 0
          maximum: 720
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ALLNET:
          name: '全网寻呼开关'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SGS_REPAG_THRE:
          name: 'SGs寻呼重发上限'
          type: integer
          minimum: 10
          maximum: 120
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_s1pagingrule_list:
      type: items
      properties:
        GRPTYPE:
          name: '用户群类型'
          type: string
          enum:
          - ALL_USER
          - IMEI_TAC
          - IMSI_PREFIX
          - MSISDN_PREFIX
          required: true
          description: '配置S1寻呼规则。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        SVRTYPE:
          name: '业务类型'
          type: string
          enum:
          - OTHER
          - S102_PAGING
          - S11_DOWNLINK
          - S6A_IDR_PAGING
          - SGS_PAGING
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SGSSI:
          name: 'SGs接口业务指示'
          type: string
          enum:
          - CS_CALL
          - SMS
          required: false
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
        DESC:
          name: '规则描述'
          type: string
          maxLength: 32
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
        MSISDNPRE:
          name: 'MSISDN前缀'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IMEITAC:
          name: 'IMEI TAC'
          type: string
          maxLength: 8
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        APNIND:
          name: 'APN指示'
          type: string
          enum:
          - ALL_APN
          - SPEC_APN
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MCC:
          name: '移动国家码'
          type: string
          maxLength: 3
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MNC:
          name: '移动网号'
          type: string
          maxLength: 3
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        APN:
          name: 'APN NI'
          type: string
          maxLength: 62
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        QCI:
          name: 'QCI值'
          type: integer
          minimum: 1
          maximum: 254
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ARPPL:
          name: 'ARP优先级'
          type: integer
          minimum: 1
          maximum: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MSGTYPE:
          name: '消息类型'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_s1pagingctrl_list_1:
      type: items
      properties:
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
        ENB_STICK_TIME:
          name: 'eNodeB粘性时长'
          type: integer
          minimum: 0
          maximum: 60
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LASTENBSW:
          name: '最近eNodeB开关'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: '设置S1寻呼策略。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        NEIB_ENBSW:
          name: '邻接eNodeB开关'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LASTTA:
          name: '最近TA开关'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SUBT3413:
          name: 'SUB\_T3413'
          type: integer
          minimum: 2
          maximum: 6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TA_STICK_TIME:
          name: 'TA粘性时长'
          type: integer
          minimum: 0
          maximum: 120
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ECT_LRN_SW:
          name: 'ECT学习开关'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        X2HO_LRN_SW:
          name: 'X2HO学习开关'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        S1HO_LRN_SW:
          name: 'S1HO学习开关'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NEB_EXPIRE_TIME:
          name: '邻接eNodeB老化时间'
          type: integer
          minimum: 0
          maximum: 720
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ALLNET:
          name: '全网寻呼开关'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SGS_REPAG_THRE:
          name: 'SGs寻呼重发上限'
          type: integer
          minimum: 10
          maximum: 120
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_talstpagingplcy_list:
      type: items
      properties:
        TALISTID:
          name: 'TA List标号'
          type: integer
          minimum: 0
          maximum: 65534
          required: true
          description: '配置指定TA List寻呼规则。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        CLSPRECISEPAG:
          name: '是否关闭精准寻呼'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: YES
        CONFIGTIMER:
          name: '是否配置定时器'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: NO
        T3413:
          name: 'T3413(s)'
          type: integer
          minimum: 3
          maximum: 12
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        N3413:
          name: 'N3413(times)'
          type: integer
          minimum: 0
          maximum: 5
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        PAGINGDELTA:
          name: '重寻呼间隔递增值(s)'
          type: integer
          minimum: 0
          maximum: 20
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: 0
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV2PRPG02'
      SWITCH: ENABLE
    set_s1pagingctrl_list:
    - LASTENBSW: ON
      NEIB_ENBSW: OFF
      LASTTA: OFF
      SUBT3413: 3
      LOWMOBICHKSW: ON
      ENB_STICK_TIME: 2
      TA_STICK_TIME: 60
      ECT_LRN_SW: ON
      X2HO_LRN_SW: ON
      S1HO_LRN_SW: ON
      NEB_EXPIRE_TIME: 360
      ALLNET: OFF
      SGS_REPAG_THRE: 15
    add_s1pagingrule_list:
    - GRPTYPE: ALL_USER
      SVRTYPE: SGS_PAGING
      SGSSI: CS_CALL
      PRIORITY: 100
      ACTGRP: LAST_ENODEB-0&NEIGH_ENODEB-0&LAST_TAI-0
      DESC: 'Voice of CSFB'
      IMSIPRE: '460002'
      MSISDNPRE: '861392'
      IMEITAC: '12345678'
      APNIND: SPEC_APN
      MCC: '460'
      MNC: '03'
      APN: 'huawei.com'
      QCI: 123
      ARPPL: 3
      MSGTYPE: “DDN(DDN)”+“CBR/UBR(CBR/UBR)”
    set_s1pagingctrl_list_1:
    - LOWMOBICHKSW: ON
      ENB_STICK_TIME: 2
      LASTENBSW: ON
      NEIB_ENBSW: ON
      LASTTA: ON
      SUBT3413: 3
      TA_STICK_TIME: 60
      ECT_LRN_SW: ON
      X2HO_LRN_SW: ON
      S1HO_LRN_SW: ON
      NEB_EXPIRE_TIME: 360
      ALLNET: OFF
      SGS_REPAG_THRE: 15
    add_talstpagingplcy_list:
    - TALISTID: 1
      CLSPRECISEPAG: YES
      CONFIGTIMER: NO
      T3413: 3
      N3413: 2
      PAGINGDELTA: 2
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 进入“MML命令行-UEG”窗口。

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

### 3 打开eNodeB学习邻接关系和寻呼范围开关。

```jinja2
{%- for item in set_s1pagingctrl_list -%}
    SET S1PAGINGCTRL:
    {#- --- 可选参数 --- -#}
    {%- if item.LASTENBSW is not none -%}
        LASTENBSW={{item.LASTENBSW}},
    {%- endif -%}
    {%- if item.NEIB_ENBSW is not none -%}
        NEIB_ENBSW={{item.NEIB_ENBSW}},
    {%- endif -%}
    {%- if item.LASTTA is not none -%}
        LASTTA={{item.LASTTA}},
    {%- endif -%}
    {%- if item.SUBT3413 is not none -%}
        SUBT3413={{item.SUBT3413}},
    {%- endif -%}
    {%- if item.S1HO_LRN_SW is not none -%}
        S1HO_LRN_SW={{item.S1HO_LRN_SW}},
    {%- endif -%}
    {%- if item.ALLNET is not none -%}
        ALLNET={{item.ALLNET}},
    {%- endif -%}
    {%- if item.SGS_REPAG_THRE is not none -%}
        SGS_REPAG_THRE={{item.SGS_REPAG_THRE}},
    {%- endif -%}
    {%- if item.ECT_LRN_SW is not none -%}
        ECT_LRN_SW={{item.ECT_LRN_SW}},
    {%- endif -%}
    {%- if item.LOWMOBICHKSW is not none -%}
        LOWMOBICHKSW={{item.LOWMOBICHKSW}},
    {%- endif -%}
    {%- if item.NEB_EXPIRE_TIME is not none -%}
        NEB_EXPIRE_TIME={{item.NEB_EXPIRE_TIME}},
    {%- endif -%}
    {%- if item.X2HO_LRN_SW is not none -%}
        X2HO_LRN_SW={{item.X2HO_LRN_SW}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：LOWMOBICHKSW=ON 时可选 --- -#}
    {%- if item.LOWMOBICHKSW == 'ON' -%}
        {%- if item.ENB_STICK_TIME is not none -%}
            ENB_STICK_TIME={{item.ENB_STICK_TIME}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：LOWMOBICHKSW=ON 时可选 --- -#}
    {%- if item.LOWMOBICHKSW == 'ON' -%}
        {%- if item.TA_STICK_TIME is not none -%}
            TA_STICK_TIME={{item.TA_STICK_TIME}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 配置寻呼策略及寻呼规则。

### 部署了WSFD-102301 基于CSFB的语音业务、GWFD-025401 VoLTE基础语音业务或GWFD-025601 LTE一键通基础功能特性概述（适用于MME）的情况下，启用LTE精准寻呼特性会增加被叫寻呼时延，在部署本特性时，建议针对CSFB、VoLTE语音或PTT业务使用TA List的寻呼范围，从而在不影响语音被叫时延的情况下节省网络资源。

### 针对数据业务和其他非语音类业务，“寻呼动作组合”推荐采用“最近访问eNodeB -> TA List”组合，即“ACTGRP（寻呼动作组合）”取值设置为“LAST\_ENODEB-1”。这样能够有效减少寻呼范围的同时，明显减少对eNodeB侧的CPU消耗。

```jinja2
{%- for item in add_s1pagingrule_list -%}
    ADD S1PAGINGRULE:
    {#- --- 必选参数 --- -#}
    GRPTYPE={{item.GRPTYPE}},
    SVRTYPE={{item.SVRTYPE}},
    {#- --- 可选参数 --- -#}
    {%- if item.PRIORITY is not none -%}
        PRIORITY={{item.PRIORITY}},
    {%- endif -%}
    {%- if item.ACTGRP is not none -%}
        ACTGRP={{item.ACTGRP}},
    {%- endif -%}
    {%- if item.DESC is not none -%}
        DESC="{{item.DESC}}",
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：SVRTYPE=SGS_PAGING 时必选 --- -#}
    {%- if item.SVRTYPE == 'SGS_PAGING' -%}
        SGSSI={{item.SGSSI}},
    {%- endif -%}
    {#- --- 条件必选：SVRTYPE=S11_DOWNLINK 时必选 --- -#}
    {%- if item.SVRTYPE == 'S11_DOWNLINK' -%}
        APNIND={{item.APNIND}},
    {%- endif -%}
    {#- --- 条件必选：APNIND=SPEC_APN 时必选 --- -#}
    {%- if item.APNIND == 'SPEC_APN' -%}
        MNC="{{item.MNC}}",
    {%- endif -%}
    {#- --- 条件必选：APNIND=SPEC_APN 时必选 --- -#}
    {%- if item.APNIND == 'SPEC_APN' -%}
        MCC="{{item.MCC}}",
    {%- endif -%}
    {#- --- 条件必选：GRPTYPE=IMSI_PREFIX 时必选 --- -#}
    {%- if item.GRPTYPE == 'IMSI_PREFIX' -%}
        IMSIPRE="{{item.IMSIPRE}}",
    {%- endif -%}
    {#- --- 条件必选：GRPTYPE=IMEI_TAC 时必选 --- -#}
    {%- if item.GRPTYPE == 'IMEI_TAC' -%}
        IMEITAC="{{item.IMEITAC}}",
    {%- endif -%}
    {#- --- 条件必选：APNIND=SPEC_APN 时必选 --- -#}
    {%- if item.APNIND == 'SPEC_APN' -%}
        APN="{{item.APN}}",
    {%- endif -%}
    {#- --- 条件必选：GRPTYPE=MSISDN_PREFIX 时必选 --- -#}
    {%- if item.GRPTYPE == 'MSISDN_PREFIX' -%}
        MSISDNPRE="{{item.MSISDNPRE}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：SVRTYPE=S11_DOWNLINK 时可选 --- -#}
    {%- if item.SVRTYPE == 'S11_DOWNLINK' -%}
        {%- if item.QCI is not none -%}
            QCI={{item.QCI}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SVRTYPE=S11_DOWNLINK 时可选 --- -#}
    {%- if item.SVRTYPE == 'S11_DOWNLINK' -%}
        {%- if item.MSGTYPE is not none -%}
            MSGTYPE={{item.MSGTYPE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SVRTYPE=S11_DOWNLINK 时可选 --- -#}
    {%- if item.SVRTYPE == 'S11_DOWNLINK' -%}
        {%- if item.ARPPL is not none -%}
            ARPPL={{item.ARPPL}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 5 检查用户移动性，进行寻呼规则过滤。

```jinja2
{%- for item in set_s1pagingctrl_list_1 -%}
    SET S1PAGINGCTRL:
    {#- --- 可选参数 --- -#}
    {%- if item.LOWMOBICHKSW is not none -%}
        LOWMOBICHKSW={{item.LOWMOBICHKSW}},
    {%- endif -%}
    {%- if item.S1HO_LRN_SW is not none -%}
        S1HO_LRN_SW={{item.S1HO_LRN_SW}},
    {%- endif -%}
    {%- if item.SUBT3413 is not none -%}
        SUBT3413={{item.SUBT3413}},
    {%- endif -%}
    {%- if item.ALLNET is not none -%}
        ALLNET={{item.ALLNET}},
    {%- endif -%}
    {%- if item.LASTTA is not none -%}
        LASTTA={{item.LASTTA}},
    {%- endif -%}
    {%- if item.SGS_REPAG_THRE is not none -%}
        SGS_REPAG_THRE={{item.SGS_REPAG_THRE}},
    {%- endif -%}
    {%- if item.NEIB_ENBSW is not none -%}
        NEIB_ENBSW={{item.NEIB_ENBSW}},
    {%- endif -%}
    {%- if item.LASTENBSW is not none -%}
        LASTENBSW={{item.LASTENBSW}},
    {%- endif -%}
    {%- if item.ECT_LRN_SW is not none -%}
        ECT_LRN_SW={{item.ECT_LRN_SW}},
    {%- endif -%}
    {%- if item.NEB_EXPIRE_TIME is not none -%}
        NEB_EXPIRE_TIME={{item.NEB_EXPIRE_TIME}},
    {%- endif -%}
    {%- if item.X2HO_LRN_SW is not none -%}
        X2HO_LRN_SW={{item.X2HO_LRN_SW}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：LOWMOBICHKSW=ON 时可选 --- -#}
    {%- if item.LOWMOBICHKSW == 'ON' -%}
        {%- if item.ENB_STICK_TIME is not none -%}
            ENB_STICK_TIME={{item.ENB_STICK_TIME}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：LOWMOBICHKSW=ON 时可选 --- -#}
    {%- if item.LOWMOBICHKSW == 'ON' -%}
        {%- if item.TA_STICK_TIME is not none -%}
            TA_STICK_TIME={{item.TA_STICK_TIME}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### “ENB\_STICK\_TIME（eNodeB粘性时长）”推荐设置为2min。

### 6 配置指定TA List寻呼规则。

```jinja2
{%- for item in add_talstpagingplcy_list -%}
    ADD TALSTPAGINGPLCY:
    {#- --- 必选参数 --- -#}
    TALISTID={{item.TALISTID}},
    {#- --- 可选参数 --- -#}
    {%- if item.CLSPRECISEPAG is not none -%}
        CLSPRECISEPAG={{item.CLSPRECISEPAG}},
    {%- endif -%}
    {%- if item.CONFIGTIMER is not none -%}
        CONFIGTIMER={{item.CONFIGTIMER}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：CONFIGTIMER=YES 时必选 --- -#}
    {%- if item.CONFIGTIMER == 'YES' -%}
        N3413={{item.N3413}},
    {%- endif -%}
    {#- --- 条件必选：CONFIGTIMER=YES 时必选 --- -#}
    {%- if item.CONFIGTIMER == 'YES' -%}
        T3413={{item.T3413}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：CONFIGTIMER=YES 时可选 --- -#}
    {%- if item.CONFIGTIMER == 'YES' -%}
        {%- if item.PAGINGDELTA is not none -%}
            PAGINGDELTA={{item.PAGINGDELTA}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 若针对指定的TA List关闭精准寻呼功能，设置**ADD TALSTPAGINGPLCY**命令中“CLSPRECISEPAG”参数为“YES”，4设置的精准寻呼规则不生效。

### 若需要关闭特定TA List的精准寻呼功能，且针对TA List范围的寻呼配置差异化的寻呼定时器时长，配置**ADD TALSTPAGINGPLCY**命令中“CLSPRECISEPAG”参数为“YES”，“T3413”、“N3413”和“PAGINGDELTA”为需要的值。

### “TALISTID”需要在**ADD TALST**中已经配置。


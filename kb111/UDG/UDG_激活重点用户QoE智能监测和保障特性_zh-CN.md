---
id: GWFD-111525
name: 激活重点用户QoE智能监测和保障特性
ne_type: UDG
type: feature
description: 当运营商需要对签约了重点业务保障套餐的用户业务流量进行QoE智能监测和保障时，需要配置本页面。
risk_level: ''
doc_source: ["特性部署","特性指南","UDG特性指南","重点业务体验保障功能","GWFD-111525 重点用户QoE智能监测和保障","激活重点用户QoE智能监测和保障特性"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
当运营商需要对签约了重点业务保障套餐的用户业务流量进行QoE智能监测和保障时，需要配置本页面。

## 必备事项
前提条件

前提条件

* 请仔细阅读GWFD-111525 重点用户QoE智能监测和保障特性概述。
* 使用重点用户QoE智能监测和保障特性时，需要确保已完成CoreMind与IISA可选服务的安装，请参考安装CoreMind服务、安装IISA服务。
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
          description: '开启重点用户QoE智能监测和保障的License控制项。'
          data_source: '固定取值'
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
          data_source: '固定取值'
          pattern: ''
          default: ''
    set_qoebasicfunc_list:
      type: items
      properties:
        QOESWITCH:
          name: 'QoE分析开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: true
          description: '设置基于智能业务感知进行QoE推理。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        INQOESWITCH:
          name: 'QoE智能分析开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ENABLE
        MODE:
          name: '运行模式'
          type: string
          enum:
          - SSU
          - IISA
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: SSU
    set_iisabasicfunc_list:
      type: items
      properties:
        SWITCH:
          name: '分析开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: true
          description: '设置智能业务感知智能推理开关。'
          data_source: '固定取值'
          pattern: ''
          default: ''
    set_vvipbasicfunc_list:
      type: items
      properties:
        SWITCH:
          name: '重点业务保障基本功能'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: true
          description: '配置开启重点业务保障功能。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        QOERPTPERIOD:
          name: '质差上报周期（秒）'
          type: integer
          minimum: 1
          maximum: 300
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        NONQOERPTPERIOD:
          name: '非质差上报周期（秒）'
          type: integer
          minimum: 1
          maximum: 300
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        REPORTSCOPE:
          name: '质差报表上报范围'
          type: string
          enum:
          - ALL_QOE_REPORT
          - ONLY_QOE_REPORT
          required: false
          description: '发生质差时上报质差单据时，该参数值修改为ONLY\_QOE\_REPORT。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SAMPLEPERIOD:
          name: '采集单据周期（秒）'
          type: integer
          minimum: 1
          maximum: 300
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        RPTUSERTYPE:
          name: '上报用户类型'
          type: string
          enum:
          - RPT_FOR5GUSER
          - RPT_FOR45GUSER
          required: false
          description: '支持上报4G和5G用户单据时，该参数值修改为RPT\_FOR45GUSER。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        CATEGORYRPT:
          name: '应用大类上报'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '需要开启基于应用大类检测时，设置开启基于应用大类的上报开关。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_policycondition_list:
      type: items
      properties:
        POLICYCNDNAME:
          name: '策略参数名'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '配置质差策略，该质差策略需要绑定到具体的协议，UPF根据该协议绑定的策略进行该协议的质差检测。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        UPLINKAVGRATE:
          name: '上行平均速率基线（千比特/秒）'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        UPFLOWTHRD:
          name: '上行大流阈值（千比特/秒）'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        MULTIKPIJUDGE:
          name: '多指标质差判断逻辑'
          type: string
          enum:
          - ALL_COND_NOT_MATCHED
          - SOME_COND_NOT_MATCHED
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_ssuprotcolgroup_list:
      type: items
      properties:
        DEFPRTGRPNAME:
          name: '自定义协议组名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '配置基于协议的质差检测策略，为每个协议组绑定质差检测策略。  策略参数名已通过**ADD POLICYCONDITION**命令配置。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PROTOCOLNAME:
          name: '协议名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        POLICYCNDNAME:
          name: '策略参数名'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        QOEDETECTCOND:
          name: '业务流量特征'
          type: string
          enum:
          - ALL_CHECK
          - DOWN_BIGFLOW_CHECK
          - UP_BIGFLOW_CHECK
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_apppolicyctrl_list:
      type: items
      properties:
        APPIDNAME:
          name: '应用ID'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '配置基于应用的质差上报策略，绑定对应的检测协议组。  自定义协议组名称已通过**ADD SSUPROTCOLGROUP**命令配置。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        SUBAPPIDNAME:
          name: '子应用ID'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        DEFPRTGRPNAME:
          name: '自定义协议组名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        MOS:
          name: '平均意见分'
          type: integer
          minimum: 0
          maximum: 100
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        ASSURANCELEVEL:
          name: '质差保障级别'
          type: string
          enum:
          - FLOW
          - SUB_APP
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_catepolicyctrl_list:
      type: items
      properties:
        APPIDNAME:
          name: '应用ID'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '需要开启基于应用大类检测时，设置基于应用大类的质差策略。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        CATEGORYID:
          name: '应用大类ID'
          type: integer
          minimum: 101
          maximum: 200
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        QOEDETPRD:
          name: '基于应用的质差上报周期'
          type: integer
          minimum: 0
          maximum: 300
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        NONQOEDETPRD:
          name: '基于应用的非质差上报周期'
          type: integer
          minimum: 0
          maximum: 300
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        MOS:
          name: '平均意见分'
          type: integer
          minimum: 0
          maximum: 100
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        QOERPTPOLICY:
          name: '应用质差上报策略'
          type: string
          enum:
          - QOE_REPORT_ONCE
          - QOE_REPORT_PERIOD
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        ENDDELAY:
          name: '应用结束延时时间'
          type: integer
          minimum: 1
          maximum: 300
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        ULICHANGERPT:
          name: '位置变更上报'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_rptglbpara_list:
      type: items
      properties:
        FLOWSAMPLERATE:
          name: '流的识别抽样率'
          type: integer
          minimum: 1
          maximum: 1000
          required: false
          description: '开启抽样率为100%。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_rptglbcfg_list:
      type: items
      properties:
        TCPINSIGHTSW:
          name: 'TCP业务分析上报开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '开启TCP UDP分析。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        UDPINSIGHTSW:
          name: 'UDP业务分析上报开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_softpara_list:
      type: items
      properties:
        DT:
          name: '软参记录数据类型'
          type: string
          enum:
          - BIT
          - BYTE
          - DWORD
          - STRING
          required: true
          description: '设置NWDAF专有承载保障场景使用已配置的预定义规则进行计费PCC功能控制。  须知：  UDG 20.13.2.10及其后续版本支持，其他版本不支持。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        BITNUM:
          name: 'Bit软参索引'
          type: integer
          minimum: 1
          maximum: 3840
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        BITVALUE:
          name: 'Bit软参取值'
          type: integer
          minimum: 0
          maximum: 1
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        BYTENUM:
          name: 'Byte索引'
          type: integer
          minimum: 1
          maximum: 1200
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        BYTEVALUE:
          name: 'Byte值'
          type: integer
          minimum: 0
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DWORDNUM:
          name: 'DWord索引'
          type: integer
          minimum: 1
          maximum: 180
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DWORDVALUE:
          name: 'Dword值'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        STRINGNUM:
          name: 'String索引'
          type: integer
          minimum: 1
          maximum: 30
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        STRINGVALUE:
          name: 'String值'
          type: string
          minLength: 0
          maxLength: 64
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV3G5ANAQ01'
      SWITCH: ENABLE
    set_qoebasicfunc_list:
    - QOESWITCH: ENABLE
      INQOESWITCH: ENABLE
      MODE: IISA
    set_iisabasicfunc_list:
    - SWITCH: ENABLE
    set_vvipbasicfunc_list:
    - SWITCH: ENABLE
      QOERPTPERIOD: 5
      NONQOERPTPERIOD: 300
      REPORTSCOPE: ALL_QOE_REPORT
      SAMPLEPERIOD: 5
      RPTUSERTYPE: RPT_FOR45GUSER
      CATEGORYRPT: ENABLE
    add_policycondition_list:
    - POLICYCNDNAME: 'policytestname'
      UPLINKAVGRATE: 300
      UPFLOWTHRD: 15
      MULTIKPIJUDGE: SOME_COND_NOT_MATCHED
    add_ssuprotcolgroup_list:
    - DEFPRTGRPNAME: 'live_video'
      PROTOCOLNAME: 'taobao_live'
      POLICYCNDNAME: 'policytestname'
      QOEDETECTCOND: UP_BIGFLOW_CHECK
    add_apppolicyctrl_list:
    - APPIDNAME: 'appgroup1'
      SUBAPPIDNAME: 'app1'
      DEFPRTGRPNAME: 'live_video'
      MOS: 4
      ASSURANCELEVEL: SUB_APP
    add_catepolicyctrl_list:
    - APPIDNAME: 'appgroup1'
      CATEGORYID: 105
      QOEDETPRD: 5
      NONQOEDETPRD: 300
      MOS: 20
      QOERPTPOLICY: QOE_REPORT_ONCE
      ENDDELAY: 100
      ULICHANGERPT: ''
    set_rptglbpara_list:
    - FLOWSAMPLERATE: 1000
    set_rptglbcfg_list:
    - TCPINSIGHTSW: ENABLE
      UDPINSIGHTSW: ENABLE
    set_softpara_list:
    - DT: BIT
      BITNUM: 2576
      BITVALUE: 1
      BYTENUM: ''
      BYTEVALUE: ''
      DWORDNUM: ''
      DWORDVALUE: ''
      STRINGNUM: ''
      STRINGVALUE: ''
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 打开本特性的License配置开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

### 2 打开QoE模型子类开关。

```jinja2
{%- for item in set_qoebasicfunc_list -%}
    SET QOEBASICFUNC:
    {#- --- 必选参数 --- -#}
    QOESWITCH={{item.QOESWITCH}},
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：QOESWITCH=ENABLE 时可选 --- -#}
    {%- if item.QOESWITCH == 'ENABLE' -%}
        {%- if item.INQOESWITCH is not none -%}
            INQOESWITCH={{item.INQOESWITCH}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：QOESWITCH=ENABLE 时可选 --- -#}
    {%- if item.QOESWITCH == 'ENABLE' -%}
        {%- if item.MODE is not none -%}
            MODE={{item.MODE}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 打开业务识别模型子类开关。

```jinja2
{%- for item in set_iisabasicfunc_list -%}
    SET IISABASICFUNC:
    {#- --- 必选参数 --- -#}
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

### 4 配置保障策略。

```jinja2
{%- for item in set_vvipbasicfunc_list -%}
    SET VVIPBASICFUNC:
    {#- --- 必选参数 --- -#}
    SWITCH={{item.SWITCH}},
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：SWITCH=ENABLE 时可选 --- -#}
    {%- if item.SWITCH == 'ENABLE' -%}
        {%- if item.QOERPTPERIOD is not none -%}
            QOERPTPERIOD={{item.QOERPTPERIOD}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SWITCH=ENABLE 时可选 --- -#}
    {%- if item.SWITCH == 'ENABLE' -%}
        {%- if item.NONQOERPTPERIOD is not none -%}
            NONQOERPTPERIOD={{item.NONQOERPTPERIOD}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SWITCH=ENABLE 时可选 --- -#}
    {%- if item.SWITCH == 'ENABLE' -%}
        {%- if item.REPORTSCOPE is not none -%}
            REPORTSCOPE={{item.REPORTSCOPE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SWITCH=ENABLE 时可选 --- -#}
    {%- if item.SWITCH == 'ENABLE' -%}
        {%- if item.SAMPLEPERIOD is not none -%}
            SAMPLEPERIOD={{item.SAMPLEPERIOD}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SWITCH=ENABLE 时可选 --- -#}
    {%- if item.SWITCH == 'ENABLE' -%}
        {%- if item.RPTUSERTYPE is not none -%}
            RPTUSERTYPE={{item.RPTUSERTYPE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SWITCH=ENABLE 时可选 --- -#}
    {%- if item.SWITCH == 'ENABLE' -%}
        {%- if item.CATEGORYRPT is not none -%}
            CATEGORYRPT={{item.CATEGORYRPT}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_policycondition_list -%}
    ADD POLICYCONDITION:
    {#- --- 必选参数 --- -#}
    POLICYCNDNAME="{{item.POLICYCNDNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.UPLINKAVGRATE is not none -%}
        UPLINKAVGRATE={{item.UPLINKAVGRATE}},
    {%- endif -%}
    {%- if item.UPFLOWTHRD is not none -%}
        UPFLOWTHRD={{item.UPFLOWTHRD}},
    {%- endif -%}
    {%- if item.MULTIKPIJUDGE is not none -%}
        MULTIKPIJUDGE={{item.MULTIKPIJUDGE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_ssuprotcolgroup_list -%}
    ADD SSUPROTCOLGROUP:
    {#- --- 必选参数 --- -#}
    DEFPRTGRPNAME="{{item.DEFPRTGRPNAME}}",
    PROTOCOLNAME="{{item.PROTOCOLNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.POLICYCNDNAME is not none -%}
        POLICYCNDNAME="{{item.POLICYCNDNAME}}",
    {%- endif -%}
    {%- if item.QOEDETECTCOND is not none -%}
        QOEDETECTCOND={{item.QOEDETECTCOND}},
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_apppolicyctrl_list -%}
    ADD APPPOLICYCTRL:
    {#- --- 必选参数 --- -#}
    APPIDNAME="{{item.APPIDNAME}}",
    SUBAPPIDNAME="{{item.SUBAPPIDNAME}}",
    DEFPRTGRPNAME="{{item.DEFPRTGRPNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.MOS is not none -%}
        MOS={{item.MOS}},
    {%- endif -%}
    {%- if item.ASSURANCELEVEL is not none -%}
        ASSURANCELEVEL={{item.ASSURANCELEVEL}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 5 若需要开启大类检测时，开启应用大类模型子类相关策略及配置。

```jinja2
{%- if is_optional_category_detection -%}
    {%- for item in add_catepolicyctrl_list -%}
        ADD CATEPOLICYCTRL:
        {#- --- 必选参数 --- -#}
        APPIDNAME="{{item.APPIDNAME}}",
        CATEGORYID={{item.CATEGORYID}},
        {#- --- 可选参数 --- -#}
        {%- if item.QOEDETPRD is not none -%}
            QOEDETPRD={{item.QOEDETPRD}},
        {%- endif -%}
        {%- if item.MOS is not none -%}
            MOS={{item.MOS}},
        {%- endif -%}
        {%- if item.QOERPTPOLICY is not none -%}
            QOERPTPOLICY={{item.QOERPTPOLICY}},
        {%- endif -%}
        {%- if item.ENDDELAY is not none -%}
            ENDDELAY={{item.ENDDELAY}},
        {%- endif -%}
        {%- if item.NONQOEDETPRD is not none -%}
            NONQOEDETPRD={{item.NONQOEDETPRD}},
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：QOERPTPOLICY=QOE_REPORT_ONCE 时可选 --- -#}
        {%- if item.QOERPTPOLICY == 'QOE_REPORT_ONCE' -%}
            {%- if item.ULICHANGERPT is not none -%}
                ULICHANGERPT={{item.ULICHANGERPT}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 6 开启抽样率为100%。

```jinja2
{%- for item in set_rptglbpara_list -%}
    SET RPTGLBPARA:
    {#- --- 可选参数 --- -#}
    {%- if item.FLOWSAMPLERATE is not none -%}
        FLOWSAMPLERATE={{item.FLOWSAMPLERATE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 7 开启TCP UDP分析。

```jinja2
{%- for item in set_rptglbcfg_list -%}
    SET RPTGLBCFG:
    {#- --- 可选参数 --- -#}
    {%- if item.TCPINSIGHTSW is not none -%}
        TCPINSIGHTSW={{item.TCPINSIGHTSW}},
    {%- endif -%}
    {%- if item.UDPINSIGHTSW is not none -%}
        UDPINSIGHTSW={{item.UDPINSIGHTSW}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 8 开启NWDAF专有承载使用配置预定义规则进行计费PCC控制功能。

```jinja2
{%- for item in set_softpara_list -%}
    SET SOFTPARA:
    {#- --- 必选参数 --- -#}
    DT={{item.DT}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：DT=BIT 时必选 --- -#}
    {%- if item.DT == 'BIT' -%}
        BITNUM={{item.BITNUM}},
    {%- endif -%}
    {#- --- 条件必选：DT=BIT 时必选 --- -#}
    {%- if item.DT == 'BIT' -%}
        BITVALUE={{item.BITVALUE}},
    {%- endif -%}
    {#- --- 条件必选：DT=BYTE 时必选 --- -#}
    {%- if item.DT == 'BYTE' -%}
        BYTENUM={{item.BYTENUM}},
    {%- endif -%}
    {#- --- 条件必选：DT=BYTE 时必选 --- -#}
    {%- if item.DT == 'BYTE' -%}
        BYTEVALUE={{item.BYTEVALUE}},
    {%- endif -%}
    {#- --- 条件必选：DT=DWORD 时必选 --- -#}
    {%- if item.DT == 'DWORD' -%}
        DWORDNUM={{item.DWORDNUM}},
    {%- endif -%}
    {#- --- 条件必选：DT=DWORD 时必选 --- -#}
    {%- if item.DT == 'DWORD' -%}
        DWORDVALUE={{item.DWORDVALUE}},
    {%- endif -%}
    {#- --- 条件必选：DT=STRING 时必选 --- -#}
    {%- if item.DT == 'STRING' -%}
        STRINGNUM={{item.STRINGNUM}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：DT=STRING 时可选 --- -#}
    {%- if item.DT == 'STRING' -%}
        {%- if item.STRINGVALUE is not none -%}
            STRINGVALUE="{{item.STRINGVALUE}}",
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```


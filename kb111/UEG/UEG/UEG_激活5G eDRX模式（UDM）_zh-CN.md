---
id: GWFD-026202
name: 激活5G eDRX模式（UDM）
ne_type: UEG
type: feature
description: 该任务旨在指导操作人员在5G网络中配置5G eDRX模式功能。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝L","MEC 特性指南（风筝L）","UEG公共特性指南","RedCap基本功能","GWFD-026202 5G eDRX模式","激活5G eDRX模式","激活5G eDRX模式（UDM）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
该任务旨在指导操作人员在5G网络中配置5G eDRX模式功能。

## 必备事项
前提条件

前提条件

* 请仔细阅读实现原理。
* 操作人员具有PGW Web LMT的操作权限。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    add_serareatpl_list:
      type: items
      properties:
        HLRSN:
          name: 'HLR序列号'
          type: string
          required: false
          description: '用于标识一个HLR序列号。该参数必须先由**ADD HLRSN**命令定义，然后才能在此处引用。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        TPLID:
          name: '模板ID'
          type: string
          required: false
          description: '用于标识待增加模板在系统中的序号。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SERAREAINFO:
          name: '业务区域限制信息'
          type: string
          required: false
          description: '用于标识业务区域限制信息。'
          data_source: '与对端协商'
          pattern: ''
          default: ''
    add_forbidareatpl_list:
      type: items
      properties:
        HLRSN:
          name: 'HLR序列号'
          type: integer
          minimum: 1
          maximum: 255
          required: true
          description: '用于标识一个HLR序列号。该参数必须先由**ADD HLRSN**命令定义，然后才能在此处引用。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        TPLID:
          name: '模板ID'
          type: integer
          minimum: 1
          maximum: 2147483646
          required: true
          description: '用于标识待增加模板在系统中的序号。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        FORBIDDENAREAS:
          name: '禁止区域'
          type: string
          maxLength: 4000
          required: true
          description: '用于标识禁止业务区域信息。'
          data_source: '与对端协商'
          pattern: ''
          default: ''
    add_dnnqostpl_list:
      type: items
      properties:
        HLRSN:
          name: 'HLR序列号'
          type: integer
          minimum: 1
          maximum: 255
          required: true
          description: '用于标识一个HLR序列号。该参数必须先由**ADD HLRSN**命令定义，然后才能在此处引用。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        TPLID:
          name: '模板ID'
          type: integer
          minimum: 1
          maximum: 2147483646
          required: true
          description: '用于标识待增加模板在系统中的序号。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PDUTYPE:
          name: '默认PDU类型'
          type: string
          enum:
          - IPV4V6
          - IPV4
          - IPV6
          - UNSTR
          - ETHER
          required: true
          description: '用于标识默认PDU会话类型。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        ALLOWEDPDUTYPE:
          name: '其它允许的PDU类型'
          type: string
          enum:
          - IPV4V6
          - IPV4
          - IPV6
          - UNSTR
          - ETHER
          required: false
          description: '用于标识其它允许的PDU会话类型。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        SSCMODE:
          name: '默认SSC模式'
          type: string
          enum:
          - SSC_MODE_1
          - SSC_MODE_2
          - SSC_MODE_3
          required: true
          description: '用于标识默认会话和业务连续性模式。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        ALLOWEDSCCMODE:
          name: '其它允许的SSC模式'
          type: string
          enum:
          - SSC_MODE_1
          - SSC_MODE_2
          - SSC_MODE_3
          required: false
          description: '用于标识其它允许的会话和业务连续性模式。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        IWKEPSIND:
          name: '是否签约EPS互操作'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: '用于标识是否签约EPS互操作。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        LADN:
          name: '是否为LADN'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: '用于标识是否支持本地数据网络。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        LBO:
          name: '是否允许Local Break Out'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: '用于标识漫游场景下是否允许使用漫游地网关。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        NGCQOSTPLID:
          name: '5GC QoS模板ID'
          type: integer
          minimum: 1
          maximum: 2147483646
          required: true
          description: '用于标识5GC QoS模板ID。该参数必须先由**ADD NGCQOSTPL**命令定义，然后才能在此处引用。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        AMBRUP:
          name: 'DNN级别上行速率'
          type: integer
          minimum: 1
          maximum: 9223372036854775807
          required: true
          description: '用于标识DNN级别上行速率的参数。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        UPUNIT:
          name: 'DNN级别上行速率单位'
          type: string
          enum:
          - bps
          - Kbps
          - Mbps
          - Gbps
          - Tbps
          required: true
          description: '用于标识DNN级别上行速率单位的参数。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        AMBRDW:
          name: 'DNN级别下行速率'
          type: integer
          minimum: 1
          maximum: 9223372036854775807
          required: true
          description: '用于标识DNN级别下行速率的参数。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        DWUNIT:
          name: 'DNN级别下行速率单位'
          type: string
          enum:
          - bps
          - Kbps
          - Mbps
          - Gbps
          - Tbps
          required: true
          description: '用于标识DNN级别下行速率单位的参数。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        CHARGE:
          name: '计费特性'
          type: string
          maxLength: 4
          required: false
          description: '用于标识计费特性。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        UPINTEGR:
          name: '用户面完整性保护策略'
          type: string
          enum:
          - NOT_NEEDED
          - REQUIRED
          - PREFERRED
          required: false
          description: '用于标识用户面完整性保护策略。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        UPCONFID:
          name: '用户面机密性保护策略'
          type: string
          enum:
          - NOT_NEEDED
          - REQUIRED
          - PREFERRED
          required: false
          description: '用于标识用户面机密性保护策略。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    mod_amdata_list:
      type: items
      properties:
        IMSI:
          name: 'IMSI'
          type: string
          required: false
          description: '用于标识用户的IMSI号码。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PROV:
          name: '是否提供AM签约数据'
          type: string
          required: false
          description: '用于标识签约、修改或删除AMF数据。'
          data_source: '固定配置'
          pattern: ''
          default: ''
        AMBRUP:
          name: 'UE级别上行速率'
          type: string
          required: false
          description: '用于标识UE级别上行速率。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        UPUNIT:
          name: 'UE级别上行速率单位'
          type: string
          required: false
          description: '用于标识UE级别上行速率单位。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        AMBRDW:
          name: 'UE级别下行速率'
          type: string
          required: false
          description: '用于标识UE级别下行速率。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        DWUNIT:
          name: 'UE级别下行速率单位'
          type: string
          required: false
          description: '用于标识UE级别下行速率单位。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        RATRESTRICT:
          name: '无线接入类型限制'
          type: string
          required: false
          description: '用于标识无线接入类型限制。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        RFSPINDEX:
          name: '无线频率选择优先级'
          type: string
          required: false
          description: '用于标识无线频率选择优先级。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        SUBSREGTIMER:
          name: '周期注册定时器'
          type: string
          required: false
          description: '用于标识周期注册时间。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        MPS:
          name: '是否支持多媒体优先级服务'
          type: string
          required: false
          description: '用于标识是否提供多媒体优先级服务功能。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        ACTIVETIME:
          name: '激活时间定时器'
          type: string
          required: false
          description: '用于标识UE在PSM模式开启时，从进入IDLE态开始到进入PSM态的定时器时长。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        DLBUFFERIND:
          name: '是否提供签约高延迟通信时的下行缓存大小'
          type: string
          required: false
          description: '用于标识是否提供高延迟通信时的下行缓存大小。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        DLBUFFER:
          name: '高延迟通信时的下行缓存大小'
          type: string
          required: false
          description: '用于标识高延迟通信时的下行缓存大小。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        AUTHTYPE:
          name: '鉴权方式'
          type: string
          required: false
          description: '用于标识鉴权方式。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        NREDRXVALUE:
          name: 'NR类型eDRX取值'
          type: string
          required: false
          description: '用于标识NR接入类型的edrxValue取值。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        NRREDCAPEDRXVALUE:
          name: 'NRREDCAP类型eDRX取值'
          type: string
          required: false
          description: '用于标识NRREDCAP接入类型的edrxValue取值。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        NRN1EXPTWVALUENRN1EXPTWVALUE:
          name: 'NRN1模式扩展PTW取值'
          type: string
          required: false
          description: '用于标识NRN1模式的扩展PTW取值。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_snssai_list:
      type: items
      properties:
        IMSI:
          name: 'IMSI'
          type: string
          required: false
          description: '用于标识用户的IMSI号码。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SNSSAI:
          name: '切片标识'
          type: string
          required: false
          description: '用于标识5G系统中的网络切片。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        DEFAULT:
          name: '是否默认S-NSSAI'
          type: string
          required: false
          description: '用于标识签约的S-NSSAI数据是否为默认S-NSSAI数据。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_smdata_list:
      type: items
      properties:
        IMSI:
          name: 'IMSI'
          type: string
          required: false
          description: '用于标识用户的IMSI号码。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SNSSAI:
          name: '切片标识'
          type: string
          required: false
          description: '用于标识网络切片ID。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        DNN:
          name: '数据网名称'
          type: string
          required: false
          description: '用于标识数据网名称。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        DNNQOSTPLID:
          name: '5GS DNNQoS模板ID'
          type: string
          required: false
          description: '用于标识用户待签约的5GS DNNQoS模板ID。该参数必须由**ADD DNNQOSTPL**命令定义后才能在此处引用。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        DEFAULT:
          name: '是否默认DNN'
          type: string
          required: false
          description: '用于标识是否默认DNN。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPV4ADDR:
          name: '终端IPv4地址'
          type: string
          required: false
          description: '用于标识终端IPv4地址。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV6ADDR:
          name: '终端IPv6地址'
          type: string
          required: false
          description: '用于标识终端IPv6地址或者IPv6前缀。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        SUGGESTEDPACKETNUMDL:
          name: '建议的下行数据缓存包大小'
          type: string
          required: false
          description: '用于标识建议的下行数据缓存包大小。'
          data_source: '本端规划'
          pattern: ''
          default: ''
  examples:
    add_serareatpl_list:
    - HLRSN: '1'
      TPLID: '199'
      SERAREAINFO: '{\"restrictionType\":\"ALLOWED_AREAS\"\,\"areas\":[{\"tacs\":[\"4445\"]}]\,\"maxNumOfTAs\":6}'
    add_forbidareatpl_list:
    - HLRSN: 1
      TPLID: 199
      FORBIDDENAREAS: '[{\"areaCode\":\"4305\"}\,{\"tacs\":[\"63F84B\"]}]'
    add_dnnqostpl_list:
    - HLRSN: 1
      TPLID: 199
      PDUTYPE: IPV4
      ALLOWEDPDUTYPE: IPV4V6&IPV6&UNSTR&ETHER
      SSCMODE: SSC_MODE_1
      ALLOWEDSCCMODE: SSC_MODE_2&SSC_MODE_3
      IWKEPSIND: TRUE
      LADN: TRUE
      LBO: TRUE
      NGCQOSTPLID: 199
      AMBRUP: 1
      UPUNIT: bps
      AMBRDW: 2
      DWUNIT: bps
      CHARGE: '2134'
      UPINTEGR: PREFERRED
      UPCONFID: REQUIRED
    mod_amdata_list:
    - IMSI: '460000009123456'
      PROV: TRUE
      AMBRUP: '11111111'
      UPUNIT: bps
      AMBRDW: '111111111'
      DWUNIT: bps
      RATRESTRICT: WLAN&VIRTUAL
      RFSPINDEX: '255'
      SUBSREGTIMER: '11111'
      MPS: TRUE
      ACTIVETIME: '11111'
      DLBUFFERIND: REQUESTED
      DLBUFFER: '1'
      AUTHTYPE: 5G-AKA
      NREDRXVALUE: '4'
      NRREDCAPEDRXVALUE: '4'
      NRN1EXPTWVALUENRN1EXPTWVALUE: '3'
    add_snssai_list:
    - IMSI: '460000009123456'
      SNSSAI: 1-111111
      DEFAULT: TRUE
    add_smdata_list:
    - IMSI: '460000009123456'
      SNSSAI: 1-111111
      DNN: test
      DNNQOSTPLID: '199'
      DEFAULT: TRUE
      IPV4ADDR: 192.168.31.43
      IPV6ADDR: 2001:db8::10
      SUGGESTEDPACKETNUMDL: '10'
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 登录“UDM业务管理”窗口。

### 2 执行**ADD SERAREATPL**命令增加5G业务区域信息模板。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_serareatpl_list的变量区（command: ADD SERAREATPL） -#}
<!-- MISSING_MACRO: command=ADD SERAREATPL list_name=add_serareatpl_list step_id=2 -->
```

### 3 执行**ADD FORBIDAREATPL**命令增加5G禁止区域模板。

```jinja2
{%- for item in add_forbidareatpl_list -%}
    ADD FORBIDAREATPL:
    {#- --- 必选参数 --- -#}
    HLRSN={{item.HLRSN}},
    TPLID={{item.TPLID}},
    FORBIDDENAREAS="{{item.FORBIDDENAREAS}}",
    ;
{%- endfor -%}
```

### 4 执行**ADD DNNQOSTPL**命令增加5GS DNN QoS模板。

```jinja2
{%- for item in add_dnnqostpl_list -%}
    ADD DNNQOSTPL:
    {#- --- 必选参数 --- -#}
    HLRSN={{item.HLRSN}},
    TPLID={{item.TPLID}},
    PDUTYPE={{item.PDUTYPE}},
    SSCMODE={{item.SSCMODE}},
    NGCQOSTPLID={{item.NGCQOSTPLID}},
    AMBRUP={{item.AMBRUP}},
    UPUNIT={{item.UPUNIT}},
    AMBRDW={{item.AMBRDW}},
    DWUNIT={{item.DWUNIT}},
    {#- --- 可选参数 --- -#}
    {%- if item.ALLOWEDPDUTYPE is not none -%}
        ALLOWEDPDUTYPE={{item.ALLOWEDPDUTYPE}},
    {%- endif -%}
    {%- if item.ALLOWEDSCCMODE is not none -%}
        ALLOWEDSCCMODE={{item.ALLOWEDSCCMODE}},
    {%- endif -%}
    {%- if item.IWKEPSIND is not none -%}
        IWKEPSIND={{item.IWKEPSIND}},
    {%- endif -%}
    {%- if item.LADN is not none -%}
        LADN={{item.LADN}},
    {%- endif -%}
    {%- if item.LBO is not none -%}
        LBO={{item.LBO}},
    {%- endif -%}
    {%- if item.CHARGE is not none -%}
        CHARGE="{{item.CHARGE}}",
    {%- endif -%}
    {%- if item.UPINTEGR is not none -%}
        UPINTEGR={{item.UPINTEGR}},
    {%- endif -%}
    {%- if item.UPCONFID is not none -%}
        UPCONFID={{item.UPCONFID}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 5 执行**MOD AMDATA**命令签约AMF数据。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该mod_amdata_list的变量区（command: MOD AMDATA） -#}
<!-- MISSING_MACRO: command=MOD AMDATA list_name=mod_amdata_list step_id=5 -->
```

### 6 执行**ADD SNSSAI**命令签约切片管理数据。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_snssai_list的变量区（command: ADD SNSSAI） -#}
<!-- MISSING_MACRO: command=ADD SNSSAI list_name=add_snssai_list step_id=6 -->
```

### 7 执行**ADD SMDATA**命令签约SMF数据。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_smdata_list的变量区（command: ADD SMDATA） -#}
<!-- MISSING_MACRO: command=ADD SMDATA list_name=add_smdata_list step_id=7 -->
```


---
id: ''
name: 配置CCR消息中携带的参数
ne_type: UNC
type: feature
description: 本指导描述UNC上支持配置CCR消息中是否携带某些参数的相关配置操作。
risk_level: ''
doc_source: ["网络部署","业务专题","5G Core 计费解决方案","计费解决方案概述","计费方案部署与调测","方案五：部署NCG且融合接口计费组网方案","SMF配置","在线计费配置","在线计费模板及交互配置","配置在线计费模板","配置CCR消息中携带的参数"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本指导描述UNC上支持配置CCR消息中是否携带某些参数的相关配置操作。

## 必备事项
前提条件

* 请仔细阅读Ga/Gy接口离线/在线计费。
* 完成加载license。
* 已完成计费属性、APN、User Profile创建。
* 已根据配置在线计费模板完成在线计费模板创建和绑定，根据配置在线计费的费率标识完成在线计费费率标识配置。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    add_diamdictpath_list:
      type: items
      properties:
        APPLICATION:
          name: '应用'
          type: string
          enum:
          - GX
          - GY
          - S6B
          required: true
          description: '（可选）为Gy应用配置字典加载路径。'
          data_source: '与对端协商'
          pattern: ''
          default: ''
        DICTNO:
          name: '字典序号'
          type: integer
          minimum: 1
          maximum: 2
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DICTPATH:
          name: '字典加载路径'
          type: string
          enum:
          - CUSTOM1
          - CUSTOM2
          - EPC970_STANDARD
          - EPC_STANDARD
          - GU_STANDARD
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    mod_diamdictpath_list:
      type: items
      properties:
        APPLICATION:
          name: '应用'
          type: string
          enum:
          - GX
          - GY
          - S6B
          required: true
          description: '（可选）为Gy应用配置字典加载路径。'
          data_source: '与对端协商'
          pattern: ''
          default: ''
        DICTNO:
          name: '字典序号'
          type: integer
          minimum: 1
          maximum: 2
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DICTPATH:
          name: '字典加载路径'
          type: string
          enum:
          - CUSTOM1
          - CUSTOM2
          - EPC970_STANDARD
          - EPC_STANDARD
          - GU_STANDARD
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    lod_diamdict_list:
      type: items
      properties:
        DICTFILESELECT:
          name: '字典文件选择'
          type: string
          enum:
          - ALL
          required: true
          description: '加载Diameter字典文件。  说明：  加载Diameter字典可能会导致UNC各Diameter应用对外接口消息发生改变，请在确认UNC对应目录下保存了Diameter字典文件并且对端网元支持字典中定义的消息及信元后再执行此动作。'
          data_source: '与对端协商'
          pattern: ''
          default: ''
    add_dcctemplate_list:
      type: items
      properties:
        DCCTMPLTNAME:
          name: 'DCC模板名称'
          type: string
          maxLength: 63
          required: true
          description: '新增或者修改DCC在线计费模板，用于配置在线计费CCR消息中携带的信元。  说明：  如果需要配置在线计费全局参数，则需要使用**MOD DCCTEMPLATE**命令，“DCCTMPLTNAME”参数值为“global”。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PRIVATEATTR:
          name: '私有属性使能开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          - INHERIT
          required: false
          description: '配置CCR消息是否携带运营商的私有扩展属性。'
          data_source: '与对端协商'
          pattern: ''
          default: INHERIT
        CCRTARIFFSW:
          name: 'CCR携带费率切换点信元开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          - INHERIT
          required: false
          description: '配置CCR消息是否携带CCA下发的费率切换时间点。'
          data_source: ''
          pattern: ''
          default: INHERIT
        QUOTATOTAL:
          name: '是否携带累加流量信息'
          type: string
          enum:
          - DISABLE
          - ENABLE
          - INHERIT
          required: false
          description: '配置Gy接口按照累加/增量方式上报计费信息。'
          data_source: ''
          pattern: ''
          default: INHERIT
        RARNORGACTION:
          name: 'RAR消息RG上报方式'
          type: string
          enum:
          - INHERIT
          - REPORT_ALL_RG
          - REPORT_NO_RG
          required: false
          description: '配置由RAR触发的CCR消息中是否携带全部Rating Group的使用信息。  说明：  * REPORT\_ALL\_RG：携带全部RG的使用信息。 * REPORT\_NO\_RG：不携带RG的使用信息。 * INHERIT：表示继承DCC模板的默认值名称为global中的RARNORGACTION配置。'
          data_source: ''
          pattern: ''
          default: INHERIT
        MSCCCARRYTYPE:
          name: 'MSCC携带方式'
          type: string
          enum:
          - INHERIT
          - MULTIPLE
          - SINGLE
          required: false
          description: '配置CCR-U和CCR-T中MSCC的携带方式。  说明：  * MULTIPLE：表示CCR-U和CCR-T消息中可以携带多个MSCC。 * SINGLE：表示每个CCR-U消息中只携带一个MSCC，CCR-T消息中不携带MSCC。当用户去活时，会连续发送多个CCR-U消息和一个CCR-T消息给OCS。 * INHERIT：表示继承DCC模板的默认值名称为global中的MSCCCARRYTYPE配置。'
          data_source: ''
          pattern: ''
          default: INHERIT
        CCRSPESMFLAG:
          name: 'CCR消息携带3GPP specific AVPs的M标志'
          type: string
          enum:
          - CLEAR
          - DICT_SPECIFIED
          - INHERIT
          - SET
          required: false
          description: '配置3GPP specific AVP的m-flag是否置为1。  说明：  此参数仅在global模板中生效。参数取值如下：   * DICT\_SPECIFIED：数据字典指定M-Flag。 * SET：M-Flag设置为1。 * CLEAR：M-Flag设置为0。 * INHERIT：表示继承DCC模板的默认值名称为global中的CCRSPESMFLAG配置。'
          data_source: ''
          pattern: ''
          default: INHERIT
        QHTEXPIREDRSU:
          name: 'QHT超时触发的CCR消息MSCC中是否携带RSU'
          type: string
          enum:
          - INHERIT
          - WITHOUT_RSU
          - WITH_RSU
          required: false
          description: '配置QHT超时触发的CCR消息MSCC中是否携带RSU信元。  说明：  此参数仅在global模板中生效。参数取值如下：   * WITH\_RSU：携带RSU。 * WITHOUT\_RSU：不携带RSU。 * INHERIT：表示继承DCC模板的默认值名称为global中的QHTEXPIREDRSU配置。'
          data_source: ''
          pattern: ''
          default: INHERIT
        PDPTYPE4NONIP:
          name: 'None IP用户的PDP类型'
          type: string
          enum:
          - INHERIT
          - NONIP
          - REALPDPTYPE
          required: false
          description: '配置CCR消息中3GPP-PDP-Type AVP的取值方式。  说明：  * REALPDPTYPE：对None IP物联网用户，Gy接口CCR消息中3GPP-PDP-Type AVP取值为PGW上真正的PDP类型：IPv4(0)，PPP(1)，IPv6(2)，IPv4v6(3)。 * NONIP：对None IP物联网用户，Gy接口CCR消息中3GPP-PDP-Type AVP取值为Non-IP（4）。 * INHERIT：表示继承DCC模板的默认值名称为global中的PdpType4NonIP配置。'
          data_source: ''
          pattern: ''
          default: INHERIT
    modd_dcctemplate_list:
      type: items
      properties:
        DCCTMPLTNAME:
          name: 'DCCTMPLTNAME'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CCRTARIFFSW:
          name: 'CCRTARIFFSW'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PRIVATEATTR:
          name: 'PRIVATEATTR'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        QUOTATOTAL:
          name: 'QUOTATOTAL'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RARNORGACTION:
          name: 'RARNORGACTION'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MSCCCARRYTYPE:
          name: 'MSCCCARRYTYPE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PDPTYPE4NONIP:
          name: 'PDPTYPE4NONIP'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    mod_dcctemplate_list:
      type: items
      properties:
        DCCTMPLTNAME:
          name: 'DCC模板名称'
          type: string
          maxLength: 63
          required: true
          description: '新增或者修改DCC在线计费模板，用于配置在线计费CCR消息中携带的信元。  说明：  如果需要配置在线计费全局参数，则需要使用**MOD DCCTEMPLATE**命令，“DCCTMPLTNAME”参数值为“global”。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PRIVATEATTR:
          name: '私有属性使能开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          - INHERIT
          required: false
          description: '配置CCR消息是否携带运营商的私有扩展属性。'
          data_source: '与对端协商'
          pattern: ''
          default: ''
        CCRTARIFFSW:
          name: 'CCR携带费率切换点信元开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          - INHERIT
          required: false
          description: '配置CCR消息是否携带CCA下发的费率切换时间点。'
          data_source: ''
          pattern: ''
          default: ''
        QUOTATOTAL:
          name: '是否携带累加流量信息'
          type: string
          enum:
          - DISABLE
          - ENABLE
          - INHERIT
          required: false
          description: '配置Gy接口按照累加/增量方式上报计费信息。'
          data_source: ''
          pattern: ''
          default: ''
        RARNORGACTION:
          name: 'RAR消息RG上报方式'
          type: string
          enum:
          - INHERIT
          - REPORT_ALL_RG
          - REPORT_NO_RG
          required: false
          description: '配置由RAR触发的CCR消息中是否携带全部Rating Group的使用信息。  说明：  * REPORT\_ALL\_RG：携带全部RG的使用信息。 * REPORT\_NO\_RG：不携带RG的使用信息。 * INHERIT：表示继承DCC模板的默认值名称为global中的RARNORGACTION配置。'
          data_source: ''
          pattern: ''
          default: ''
        MSCCCARRYTYPE:
          name: 'MSCC携带方式'
          type: string
          enum:
          - INHERIT
          - MULTIPLE
          - SINGLE
          required: false
          description: '配置CCR-U和CCR-T中MSCC的携带方式。  说明：  * MULTIPLE：表示CCR-U和CCR-T消息中可以携带多个MSCC。 * SINGLE：表示每个CCR-U消息中只携带一个MSCC，CCR-T消息中不携带MSCC。当用户去活时，会连续发送多个CCR-U消息和一个CCR-T消息给OCS。 * INHERIT：表示继承DCC模板的默认值名称为global中的MSCCCARRYTYPE配置。'
          data_source: ''
          pattern: ''
          default: ''
        CCRSPESMFLAG:
          name: 'CCR消息携带3GPP specific AVPs的M标志'
          type: string
          enum:
          - CLEAR
          - DICT_SPECIFIED
          - INHERIT
          - SET
          required: false
          description: '配置3GPP specific AVP的m-flag是否置为1。  说明：  此参数仅在global模板中生效。参数取值如下：   * DICT\_SPECIFIED：数据字典指定M-Flag。 * SET：M-Flag设置为1。 * CLEAR：M-Flag设置为0。 * INHERIT：表示继承DCC模板的默认值名称为global中的CCRSPESMFLAG配置。'
          data_source: ''
          pattern: ''
          default: ''
        QHTEXPIREDRSU:
          name: 'QHT超时触发的CCR消息MSCC中是否携带RSU'
          type: string
          enum:
          - INHERIT
          - WITHOUT_RSU
          - WITH_RSU
          required: false
          description: '配置QHT超时触发的CCR消息MSCC中是否携带RSU信元。  说明：  此参数仅在global模板中生效。参数取值如下：   * WITH\_RSU：携带RSU。 * WITHOUT\_RSU：不携带RSU。 * INHERIT：表示继承DCC模板的默认值名称为global中的QHTEXPIREDRSU配置。'
          data_source: ''
          pattern: ''
          default: ''
        PDPTYPE4NONIP:
          name: 'None IP用户的PDP类型'
          type: string
          enum:
          - INHERIT
          - NONIP
          - REALPDPTYPE
          required: false
          description: '配置CCR消息中3GPP-PDP-Type AVP的取值方式。  说明：  * REALPDPTYPE：对None IP物联网用户，Gy接口CCR消息中3GPP-PDP-Type AVP取值为PGW上真正的PDP类型：IPv4(0)，PPP(1)，IPv6(2)，IPv4v6(3)。 * NONIP：对None IP物联网用户，Gy接口CCR消息中3GPP-PDP-Type AVP取值为Non-IP（4）。 * INHERIT：表示继承DCC模板的默认值名称为global中的PdpType4NonIP配置。'
          data_source: ''
          pattern: ''
          default: ''
  examples:
    add_diamdictpath_list:
    - APPLICATION: GY
      DICTNO: 1
      DICTPATH: CUSTOM1
    mod_diamdictpath_list:
    - APPLICATION: GY
      DICTNO: 1
      DICTPATH: CUSTOM1
    lod_diamdict_list:
    - DICTFILESELECT: ALL
    add_dcctemplate_list:
    - DCCTMPLTNAME: 'dcc-test'
      PRIVATEATTR: ENABLE
      CCRTARIFFSW: ENABLE
      QUOTATOTAL: ENABLE
      RARNORGACTION: REPORT\_ALL\_RG
      MSCCCARRYTYPE: MULTIPLE
      CCRSPESMFLAG: DICT\_SPECIFIED
      QHTEXPIREDRSU: WITHOUT\_RSU
      PDPTYPE4NONIP: REALPDPTYPE
    modd_dcctemplate_list:
    - DCCTMPLTNAME: dcc-test
      CCRTARIFFSW: ENABLE
      PRIVATEATTR: ENABLE
      QUOTATOTAL: ENABLE
      RARNORGACTION: REPORT_ALL_RG
      MSCCCARRYTYPE: MULTIPLE
      PDPTYPE4NONIP: REALPDPTYPE
    mod_dcctemplate_list:
    - DCCTMPLTNAME: 'dcc-test'
      PRIVATEATTR: ENABLE
      CCRTARIFFSW: ENABLE
      QUOTATOTAL: ENABLE
      RARNORGACTION: REPORT\_ALL\_RG
      MSCCCARRYTYPE: MULTIPLE
      CCRSPESMFLAG: DICT\_SPECIFIED
      QHTEXPIREDRSU: WITHOUT\_RSU
      PDPTYPE4NONIP: REALPDPTYPE
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 为Gy应用配置字典加载路径，并执行加载动作。

#### 1.1 为Gy应用配置字典加载路径。

```jinja2
{%- for item in add_diamdictpath_list -%}
    ADD DIAMDICTPATH:
    {#- --- 必选参数 --- -#}
    APPLICATION={{item.APPLICATION}},
    DICTNO={{item.DICTNO}},
    DICTPATH={{item.DICTPATH}},
    ;
{%- endfor -%}
```

```jinja2
{%- for item in mod_diamdictpath_list -%}
    MOD DIAMDICTPATH:
    {#- --- 必选参数 --- -#}
    APPLICATION={{item.APPLICATION}},
    DICTNO={{item.DICTNO}},
    DICTPATH={{item.DICTPATH}},
    ;
{%- endfor -%}
```

#### 1.2 执行字典加载动作。

#### 加载Diameter字典可能会导致UNC各Diameter应用对外接口消息发生改变，请在确认UNC对应目录下保存了Diameter字典文件并且对端网元支持字典中定义的消息及信元后再执行此动作。

```jinja2
{%- for item in lod_diamdict_list -%}
    LOD DIAMDICT:
    {#- --- 必选参数 --- -#}
    DICTFILESELECT={{item.DICTFILESELECT}},
    ;
{%- endfor -%}
```

### 2 配置DCC模板中CCR消息中携带的参数。

#### 2.1 配置CCR消息中是否携带前一个CCA消息中下发的费率切换时间点，配置参数“CCRTARIFFSW”。

#### 在线计费中，费率切换时间点只能由OCS下发，UNC上无法配置。此配置是用来控制当UNC检测到发生了费率切换，在后续的CCR消息中上报费率切换信息时，是否连同对应的费率切换点一并上报。

#### 另外，只有当CCA消息中下发的event-trigger中包含了费率切换，发生费率切换时才会触发CCR上报。

#### 2.2 配置CCR消息中是否携带运营商私有扩展属性开关，配置参数“PRIVATEATTR”。

#### 只有在本命令开关使能后，下面配置的运营商私有属性才能生效。

#### 2.3 配置Gy接口按照累加模式上报计费信息，配置参数“QUOTATOTAL”。

#### 默认情况下是按照增量方式上报，上述开关打开后按照累加模式上报。

#### 2.4 配置由RAR触发的CCR消息中是否携带全部Rating Group的使用信息，参数为“RARNORGACTION”。

#### 2.5 配置CCR消息中携带一个或多个Multiple-Service-Credit-Control(MSCC) AVP，配置参数“MSCCCARRYTYPE”。

#### 2.6 配置CCR消息中3GPP-PDP-Type AVP的取值方式，参数为“PDPTYPE4NONIP”。

```jinja2
{%- for item in add_dcctemplate_list -%}
    ADD DCCTEMPLATE:
    {#- --- 必选参数 --- -#}
    DCCTMPLTNAME="{{item.DCCTMPLTNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.CCRSPESMFLAG is not none -%}
        CCRSPESMFLAG={{item.CCRSPESMFLAG}},
    {%- endif -%}
    {%- if item.CCRTARIFFSW is not none -%}
        CCRTARIFFSW={{item.CCRTARIFFSW}},
    {%- endif -%}
    {%- if item.MSCCCARRYTYPE is not none -%}
        MSCCCARRYTYPE={{item.MSCCCARRYTYPE}},
    {%- endif -%}
    {%- if item.PDPTYPE4NONIP is not none -%}
        PDPTYPE4NONIP={{item.PDPTYPE4NONIP}},
    {%- endif -%}
    {%- if item.PRIVATEATTR is not none -%}
        PRIVATEATTR={{item.PRIVATEATTR}},
    {%- endif -%}
    {%- if item.QHTEXPIREDRSU is not none -%}
        QHTEXPIREDRSU={{item.QHTEXPIREDRSU}},
    {%- endif -%}
    {%- if item.QUOTATOTAL is not none -%}
        QUOTATOTAL={{item.QUOTATOTAL}},
    {%- endif -%}
    {%- if item.RARNORGACTION is not none -%}
        RARNORGACTION={{item.RARNORGACTION}},
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该modd_dcctemplate_list的变量区（command: MODD DCCTEMPLATE） -#}
<!-- MISSING_MACRO: command=MODD DCCTEMPLATE list_name=modd_dcctemplate_list step_id=2.6 -->
```

### 3 配置全局DCC模板中CCR消息中携带的参数。

#### 3.1 配置CCR消息中是否携带Requested-Service-Unit (RSU) AVP，配置参数“QHTEXPIREDRSU”。

#### 3.2 配置CCR消息中携带的部分AVP的M标志位是否置为1，配置参数“CCRSPESMFLAG”。

#### 涉及的AVP包括：

#### 3GPP-Charging-Characteristics、3GPP-Charging-Id、3GPP-GGSN-MCC-MNC、3GPP-GPRS-Negotiated-QoS-Profile、3GPP-IMSI-MCC-MNC、3GPP-MS-TimeZone、3GPP-NSAPI、3GPP-PDP-Type、3GPP-RAT-Type、3GPP-Selection-Mode、3GPP-Session-Stop-Indicator、3GPP-SGSN-MCC-MNC、3GPP-User-Location-Info

```jinja2
{%- for item in mod_dcctemplate_list -%}
    MOD DCCTEMPLATE:
    {#- --- 必选参数 --- -#}
    DCCTMPLTNAME="{{item.DCCTMPLTNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.CCRSPESMFLAG is not none -%}
        CCRSPESMFLAG={{item.CCRSPESMFLAG}},
    {%- endif -%}
    {%- if item.CCRTARIFFSW is not none -%}
        CCRTARIFFSW={{item.CCRTARIFFSW}},
    {%- endif -%}
    {%- if item.MSCCCARRYTYPE is not none -%}
        MSCCCARRYTYPE={{item.MSCCCARRYTYPE}},
    {%- endif -%}
    {%- if item.PDPTYPE4NONIP is not none -%}
        PDPTYPE4NONIP={{item.PDPTYPE4NONIP}},
    {%- endif -%}
    {%- if item.PRIVATEATTR is not none -%}
        PRIVATEATTR={{item.PRIVATEATTR}},
    {%- endif -%}
    {%- if item.QHTEXPIREDRSU is not none -%}
        QHTEXPIREDRSU={{item.QHTEXPIREDRSU}},
    {%- endif -%}
    {%- if item.QUOTATOTAL is not none -%}
        QUOTATOTAL={{item.QUOTATOTAL}},
    {%- endif -%}
    {%- if item.RARNORGACTION is not none -%}
        RARNORGACTION={{item.RARNORGACTION}},
    {%- endif -%}
    ;
{%- endfor -%}
```


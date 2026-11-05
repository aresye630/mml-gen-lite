---
id: ''
name: 配置CCR消息中携带的参数
ne_type: UNC
type: feature
description: GGSN/PGW-C上支持配置CCR消息中是否携带某些参数。  适用于GGSN、PGW-C。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","计费管理功能","WSFD-109001 Gy/Diameter在线计费","激活Gy/Diameter在线计费","配置在线计费模板","配置CCR消息中携带的参数"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
GGSN/PGW-C上支持配置CCR消息中是否携带某些参数。适用于GGSN、PGW-C。

## 必备事项
前提条件

* 请仔细阅读Ga/Gy接口离线/在线计费。
* 完成配置到OCS的数据(静态路由+BFD组网)。
* 完成**加载license**（如果有需求，请联系华为技术支持工程师处理）。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    add_dcctemplate_list:
      type: items
      properties:
        DCCTMPLTNAME:
          name: 'DCC模板名称'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: ''
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
          description: 'CCR消息是否携带CCA下发的费率切换时间点。'
          data_source: '本端规划'
          pattern: ''
          default: INHERIT
        PRIVATEATTR:
          name: '私有属性使能开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          - INHERIT
          required: false
          description: 'CCR消息是否携带运营商的私有扩展属性。'
          data_source: '本端规划'
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
          description: 'Gy接口按照累加/增量方式上报计费信息。'
          data_source: '本端规划'
          pattern: ''
          default: INHERIT
    set_apnchargectrl_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          maxLength: 63
          required: true
          description: 'APN实例绑定DCC Template模板。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        DCCTEMPLATE:
          name: 'DCC模板名称'
          type: string
          maxLength: 63
          required: false
          description: ''
          data_source: '已配置数据中获取'
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
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_urr_list:
      type: items
      properties:
        URRNAME:
          name: '使用量上报规则名称'
          type: string
          maxLength: 31
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        URRID:
          name: 'URR标识'
          type: integer
          minimum: 0
          maximum: 2147483646
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        USAGERPTMODE:
          name: '使用量上报模式'
          type: string
          enum:
          - MONITORINGKEY
          - OFFLINE
          - ONLINE
          - QOS
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MONITORINGKEY:
          name: '监控属性值'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        N40AGESW:
          name: 'N40接口场景下是否允许老化'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ENABLE
        OFCSRVTMPLNAME:
          name: '离线业务模板名'
          type: string
          maxLength: 63
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        OFFCOMPOUNDTYPE:
          name: '离线计费标识组成类型'
          type: string
          enum:
          - ONLYRG
          - ONLYSID
          - RGSID
          - UPDOWNSID
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        OFFMETERINGTYPE:
          name: '离线计费统计类型'
          type: string
          enum:
          - EVENT
          - EVENT_TIME
          - EVENT_VOLUME
          - EVENT_VOLUME_TIME
          - FREE
          - TIME
          - VOLUME
          - VOLUME_TIME
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ONLCOMPOUNDTYPE:
          name: '在线计费标识组成类型'
          type: string
          enum:
          - ONLYRG
          - RGSID
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ONLMETERINGTYPE:
          name: '在线计费统计类型'
          type: string
          enum:
          - EVENT
          - EVENT_TIME
          - EVENT_VOLUME
          - EVENT_VOLUME_TIME
          - FREE
          - TIME
          - VOLUME
          - VOLUME_TIME
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        REDIRENDTOKEN:
          name: 'Gy重定向结束Token'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    add_dcctemplate_list:
    - DCCTMPLTNAME: 'dcc-test'
      CCRTARIFFSW: ENABLE
      PRIVATEATTR: ENABLE
      QUOTATOTAL: ENABLE
    set_apnchargectrl_list:
    - APN: 'apn-test'
      DCCTEMPLATE: 'dcc-test'
    mod_dcctemplate_list:
    - DCCTMPLTNAME: ''
    add_urr_list:
    - URRNAME: ''
      URRID: ''
      USAGERPTMODE: ''
      MONITORINGKEY: ''
      N40AGESW: ENABLE
      OFCSRVTMPLNAME: ''
      OFFCOMPOUNDTYPE: ''
      OFFMETERINGTYPE: ''
      ONLCOMPOUNDTYPE: ''
      ONLMETERINGTYPE: ''
      REDIRENDTOKEN: ''
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 配置DCC模板中CCR消息中携带的参数。

#### 1.1 配置CCR消息中是否携带前一个CCA消息中下发的费率切换时间点，配置参数“CCRTARIFFSW”。

#### 在线计费中，费率切换时间点只能由OCS下发，GGSN/PGW-C上无法配置。此配置是用来控制当GGSN/PGW-C检测到发生了费率切换，在后续的CCR消息中上报费率切换信息时，是否连同对应的费率切换点一并上报。

#### 另外，只有当CCA消息中下发的event-trigger中包含了费率切换，发生费率切换时才会触发CCR上报。

#### 1.2 配置CCR消息中是否携带运营商私有扩展属性开关，配置参数“PRIVATEATTR”。

#### 只有在本命令开关使能后，下面配置的运营商私有属性才能生效。

#### 1.3 配置Gy接口按照累加模式上报计费信息，配置参数“QUOTATOTAL”。

#### 默认情况下是按照增量方式上报，上述开关打开后按照累加模式上报。

#### 1.4 配置CCR消息中携带一个或多个Multiple-Service-Credit-Control(MSCC) AVP，配置参数“MSCCCARRYTYPE”。

```jinja2
{%- for item in add_dcctemplate_list -%}
    ADD DCCTEMPLATE:
    {#- --- 必选参数 --- -#}
    DCCTMPLTNAME="{{item.DCCTMPLTNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.CCRTARIFFSW is not none -%}
        CCRTARIFFSW={{item.CCRTARIFFSW}},
    {%- endif -%}
    {%- if item.PRIVATEATTR is not none -%}
        PRIVATEATTR={{item.PRIVATEATTR}},
    {%- endif -%}
    {%- if item.QUOTATOTAL is not none -%}
        QUOTATOTAL={{item.QUOTATOTAL}},
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in set_apnchargectrl_list -%}
    SET APNCHARGECTRL:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    {#- --- 可选参数 --- -#}
    {%- if item.DCCTEMPLATE is not none -%}
        DCCTEMPLATE="{{item.DCCTEMPLATE}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 2 配置全局DCC模板中CCR消息中携带的参数。

#### 2.1 配置CCR消息中是否携带Requested-Service-Unit (RSU) AVP，配置参数“QHTEXPIREDRSU”。

#### 2.2 配置CCR消息中携带的部分AVP的M标志位是否置位，配置参数“CCRSPESMFLAG”。

#### 涉及的AVP包括：

#### 3GPP-Charging-Characteristics、3GPP-Charging-Id、3GPP-GGSN-MCC-MNC、3GPP-GPRS-Negotiated-QoS-Profile、3GPP-IMSI-MCC-MNC、3GPP-MS-TimeZone、3GPP-NSAPI、3GPP-PDP-Type、3GPP-RAT-Type、3GPP-Selection-Mode、3GPP-Session-Stop-Indicator、3GPP-SGSN-MCC-MNC、3GPP-User-Location-Info

```jinja2
{%- for item in mod_dcctemplate_list -%}
    MOD DCCTEMPLATE:
    {#- --- 必选参数 --- -#}
    DCCTMPLTNAME="{{item.DCCTMPLTNAME}}",
    ;
{%- endfor -%}
```

### 3 配置CCR消息中默认请求的配额数。

### 各费率组RG的配额一般由OCS下发，当OCS不支持配置配额下发的具体数值时，也可以在GGSN/PGW-C本地配置要申请的配额数。当OCS和GGSN/PGW-C都配置有费率下发/申请的配额数时，OCS上的配置优先级高。

#### 3.1 配置时长/流量计费时CCR消息中默认请求的时长/流量配额数。

```jinja2
{%- for item in add_urr_list -%}
    ADD URR:
    {#- --- 必选参数 --- -#}
    URRID={{item.URRID}},
    URRNAME="{{item.URRNAME}}",
    USAGERPTMODE={{item.USAGERPTMODE}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：USAGERPTMODE=MONITORINGKEY 时必选 --- -#}
    {%- if item.USAGERPTMODE == 'MONITORINGKEY' -%}
        MONITORINGKEY="{{item.MONITORINGKEY}}",
    {%- endif -%}
    {#- --- 条件必选：USAGERPTMODE=OFFLINE 时必选 --- -#}
    {%- if item.USAGERPTMODE == 'OFFLINE' -%}
        OFFCOMPOUNDTYPE={{item.OFFCOMPOUNDTYPE}},
    {%- endif -%}
    {#- --- 条件必选：USAGERPTMODE=ONLINE 时必选 --- -#}
    {%- if item.USAGERPTMODE == 'ONLINE' -%}
        ONLCOMPOUNDTYPE={{item.ONLCOMPOUNDTYPE}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：USAGERPTMODE=OFFLINE/ONLINE 时可选 --- -#}
    {%- if item.USAGERPTMODE in ['OFFLINE', 'ONLINE'] -%}
        {%- if item.N40AGESW is not none -%}
            N40AGESW={{item.N40AGESW}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：USAGERPTMODE=OFFLINE 时可选 --- -#}
    {%- if item.USAGERPTMODE == 'OFFLINE' -%}
        {%- if item.OFCSRVTMPLNAME is not none -%}
            OFCSRVTMPLNAME="{{item.OFCSRVTMPLNAME}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：USAGERPTMODE=OFFLINE 时可选 --- -#}
    {%- if item.USAGERPTMODE == 'OFFLINE' -%}
        {%- if item.OFFMETERINGTYPE is not none -%}
            OFFMETERINGTYPE={{item.OFFMETERINGTYPE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：USAGERPTMODE=ONLINE 时可选 --- -#}
    {%- if item.USAGERPTMODE == 'ONLINE' -%}
        {%- if item.ONLMETERINGTYPE is not none -%}
            ONLMETERINGTYPE={{item.ONLMETERINGTYPE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：USAGERPTMODE=ONLINE 时可选 --- -#}
    {%- if item.USAGERPTMODE == 'ONLINE' -%}
        {%- if item.REDIRENDTOKEN is not none -%}
            REDIRENDTOKEN="{{item.REDIRENDTOKEN}}",
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 参数“ONLMETERINGTYPE”的值“VOLUME”（按流量计费），或“TIME”（按时间计费）配置相应的配额数即可。

#### 3.2 将配置的URR绑定到使用量上报规则组，或者被全局引用，或者被UserProfile/APN引用，此处不再赘述配置步骤。


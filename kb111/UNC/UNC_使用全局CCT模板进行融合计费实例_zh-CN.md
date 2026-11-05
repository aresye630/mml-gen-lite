---
id: ''
name: 使用全局CCT模板进行融合计费实例
ne_type: UNC
type: feature
description: 当对全局所有业务采用同样的计费参数时，可以使用全局CCT模板进行计费。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","计费管理功能","WSFD-011206 支持融合计费","激活支持融合计费","使用全局CCT模板进行融合计费实例"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
当对全局所有业务采用同样的计费参数时，可以使用全局CCT模板进行计费。

## 必备事项
前提条件

* 请仔细阅读融合计费原理。
* 完成加载License。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    add_urr_list:
      type: items
      properties:
        URRNAME:
          name: '使用量上报规则名称'
          type: string
          maxLength: 31
          required: true
          description: '配置使用量上报规则，从而配置使用的费率标识。'
          data_source: '本端规划'
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
        ONLINERG:
          name: '在线计费组'
          type: integer
          minimum: 0
          maximum: 4294967294
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ONLINESID:
          name: '在线业务标识'
          type: integer
          minimum: 0
          maximum: 4294967294
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
        EVENTRSUVALUE:
          name: '事件配额值（次）'
          type: integer
          minimum: 0
          maximum: 5000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 0
        TIMERSUVALUE:
          name: '时间配额值（秒）'
          type: integer
          minimum: 0
          maximum: 3600000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VOLUMERSUVALUE:
          name: '流量配额值（字节）'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: false
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
        REDIRENDTOKEN:
          name: 'Gy重定向结束Token'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_glburrgroup_list:
      type: items
      properties:
        UPONLURRNAME:
          name: '上行发起在线URR名称'
          type: string
          maxLength: 31
          required: false
          description: '将URR绑定到全局URR组上。如果上下行使用不同的URR，则两者必须同时为在线计费或离线计费。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        DNONLURRNAME:
          name: '下行发起在线URR名称'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    mod_cct_list:
      type: items
      properties:
        CCTMPLTNAME:
          name: '融合计费模板名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '配置全局通用参数CCT模板。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        QHT:
          name: '配额空闲时间门限值(秒)'
          type: integer
          minimum:
          - 0
          - 5
          maximum:
          - 0
          - 3600
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_chfinit_list:
      type: items
      properties:
        CCTMPLTNAME:
          name: '融合计费模板名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '配置建立PDU会话时是否发送ChargingDataRqueset与CHF交互。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        CHFINIT:
          name: 'CHF交互使能开关'
          type: string
          enum:
          - SENDREQ
          - NOTSENDREQ
          - INITRGTRIGR
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CCRINITRGNUM:
          name: '初始RG个数'
          type: integer
          minimum: 0
          maximum: 10
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_pdutrigger_list:
      type: items
      properties:
        CCTMPLTNAME:
          name: 'CCT模板名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '配置Session级/RG级Trigger。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        QOSCHG:
          name: 'QoS更新'
          type: string
          enum:
          - NONREPORT
          - IMMEDIATE
          - DEFERRED
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DEFERRED
        SRVNDCHG:
          name: '服务节点更新'
          type: string
          enum:
          - NONREPORT
          - IMMEDIATE
          - DEFERRED
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DEFERRED
        RATCHG:
          name: 'RAT更新'
          type: string
          enum:
          - NONREPORT
          - IMMEDIATE
          - DEFERRED
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: IMMEDIATE
    add_rgtrigger_list:
      type: items
      properties:
        CCTMPLTNAME:
          name: 'CCT模板名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        ULCHG:
          name: '用户位置更新'
          type: string
          enum:
          - NONREPORT
          - IMMEDIATE
          - DEFERRED
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DEFERRED
        PRACHG:
          name: '区域用户位置上报更新'
          type: string
          enum:
          - NONREPORT
          - IMMEDIATE
          - DEFERRED
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DEFERRED
        PSDATAOFFCHG:
          name: 'PS数据关闭状态更新'
          type: string
          enum:
          - NONREPORT
          - IMMEDIATE
          - DEFERRED
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DEFERRED
    set_failhandling_list:
      type: items
      properties:
        CCTMPLTNAME:
          name: '融合计费模板名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '配置当SMF与CHF交互时，SMF超时未收到CHF返回的ChargingDataResponse消息时的动作。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        FHACTION:
          name: 'FH处理动作'
          type: string
          enum:
          - TERMINATE
          - CONTINUE
          - RETRY_AND_TERM
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        FAILOVERSUP:
          name: '支持failover使能开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AUTOFAILBACK:
          name: 'failback使能开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TXTIMER:
          name: 'Tx定时器时长(秒)'
          type: integer
          minimum: 0
          maximum: 20
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        HOLDINGTIME:
          name: '用户保持时长(分钟)'
          type: integer
          minimum: 0
          maximum: 2880
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_pduscact_list:
      type: items
      properties:
        CCTMPLTNAME:
          name: 'CCT名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '配置当SMF收到CHF的PDU级异常返回码时的动作。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        CODETYPE:
          name: '返回码类型'
          type: string
          enum:
          - DEFAULT
          - VALUE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        STATUSCODE:
          name: '状态码'
          type: integer
          minimum:
          - 300
          - 65535
          maximum:
          - 999
          - 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SCACT:
          name: '处理动作'
          type: string
          enum:
          - FAILOVER
          - CONTINUE
          - TERM_WITH_REL
          - TERM_NO_REL
          - BLOCK
          - REDIRECT
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        BLKTIMER:
          name: '阻塞处理时间间隔'
          type: integer
          minimum: 0
          maximum: 1440
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GTPV01CAUSE:
          name: '原因值GtpV0-1'
          type: integer
          minimum: 0
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GTPV2CAUSE:
          name: '原因值GtpV2'
          type: integer
          minimum: 0
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RDVIRTIP:
          name: '重定向IPV4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RDVIRTIPV6:
          name: '重定向IPV6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        REACTREQ:
          name: '重新激活请求'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_rgrcact_list:
      type: items
      properties:
        CCTMPLTNAME:
          name: '在线计费模板名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '配置当SMF收到CHF的响应的RG级异常返回码时的动作。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        RCCODE:
          name: 'RG级异常返回码'
          type: string
          enum:
          - DEFAULT
          - SERVICEDENIED
          - QUOTAMNOTAPPL
          - QUOTALIMITRCH
          - SERVICEREJECT
          - USERUNKNOWN
          - RATINGFAILED
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RCACT:
          name: 'RG级异常返回码动作'
          type: string
          enum:
          - BLCK_TRG_RPT
          - BLCK_IMMED_RPT
          - BLCK_NO_RPT
          - CONTINUE
          - TERMINATE
          - REDIRECT
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        BLKTIMER:
          name: 'RG级阻塞处理时间间隔'
          type: integer
          minimum: 0
          maximum: 1440
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        HOLDINGTIME:
          name: '用户保持时长(分钟)'
          type: integer
          minimum: 0
          maximum: 2880
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RDVIRTIP:
          name: 'RG级重定向处理重定向IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RDVIRTIPV6:
          name: 'RG级重定向处理重定向IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        REACTREQ:
          name: 'RG级重新激活请求'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    add_urr_list:
    - URRNAME: 'urr1'
      URRID: 1
      USAGERPTMODE: ONLINE
      ONLCOMPOUNDTYPE: RGSID
      ONLINERG: 10
      ONLINESID: 20
      ONLMETERINGTYPE: VOLUME
      EVENTRSUVALUE: ''
      TIMERSUVALUE: ''
      VOLUMERSUVALUE: ''
      MONITORINGKEY: ''
      N40AGESW: ENABLE
      OFCSRVTMPLNAME: ''
      OFFCOMPOUNDTYPE: ''
      OFFMETERINGTYPE: ''
      REDIRENDTOKEN: ''
    set_glburrgroup_list:
    - UPONLURRNAME: 'urr1'
      DNONLURRNAME: 'urr1'
    mod_cct_list:
    - CCTMPLTNAME: 'global'
      QHT: 5
    set_chfinit_list:
    - CCTMPLTNAME: 'global'
      CHFINIT: SENDREQ
      CCRINITRGNUM: 10
    add_pdutrigger_list:
    - CCTMPLTNAME: 'global'
      QOSCHG: IMMEDIATE
      SRVNDCHG: DEFERRED
      RATCHG: IMMEDIATE
    add_rgtrigger_list:
    - CCTMPLTNAME: 'global'
      ULCHG: NONREPORT
      PRACHG: IMMEDIATE
      PSDATAOFFCHG: IMMEDIATE
    set_failhandling_list:
    - CCTMPLTNAME: 'global'
      FHACTION: RETRY_AND_TERM
      FAILOVERSUP: ENABLE
      AUTOFAILBACK: ENABLE
      TXTIMER: 5
      HOLDINGTIME: 10
    add_pduscact_list:
    - CCTMPLTNAME: 'global'
      CODETYPE: VALUE
      STATUSCODE: 404
      SCACT: CONTINUE
      BLKTIMER: ''
      GTPV01CAUSE: ''
      GTPV2CAUSE: ''
      RDVIRTIP: ''
      RDVIRTIPV6: ''
      REACTREQ: ''
    add_rgrcact_list:
    - CCTMPLTNAME: 'global'
      RCCODE: QUOTAMNOTAPPL
      RCACT: BLCK_IMMED_RPT
      BLKTIMER: 30
      HOLDINGTIME: ''
      RDVIRTIP: ''
      RDVIRTIPV6: ''
      REACTREQ: ''
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 //配置在线计费、且费率标识为（RG，SID）=（10,20）的URR，并将该URR设置为全局上下行URR。

```jinja2
{%- for item in add_urr_list -%}
    ADD URR:
    {#- --- 必选参数 --- -#}
    URRNAME="{{item.URRNAME}}",
    URRID={{item.URRID}},
    USAGERPTMODE={{item.USAGERPTMODE}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：USAGERPTMODE=ONLINE 时必选 --- -#}
    {%- if item.USAGERPTMODE == 'ONLINE' -%}
        ONLCOMPOUNDTYPE={{item.ONLCOMPOUNDTYPE}},
    {%- endif -%}
    {#- --- 条件必选：ONLCOMPOUNDTYPE=RGSID/ONLYRG 时必选 --- -#}
    {%- if item.ONLCOMPOUNDTYPE in ['RGSID', 'ONLYRG'] -%}
        ONLINERG={{item.ONLINERG}},
    {%- endif -%}
    {#- --- 条件必选：ONLCOMPOUNDTYPE=RGSID 时必选 --- -#}
    {%- if item.ONLCOMPOUNDTYPE == 'RGSID' -%}
        ONLINESID={{item.ONLINESID}},
    {%- endif -%}
    {#- --- 条件必选：USAGERPTMODE=MONITORINGKEY 时必选 --- -#}
    {%- if item.USAGERPTMODE == 'MONITORINGKEY' -%}
        MONITORINGKEY="{{item.MONITORINGKEY}}",
    {%- endif -%}
    {#- --- 条件必选：USAGERPTMODE=OFFLINE 时必选 --- -#}
    {%- if item.USAGERPTMODE == 'OFFLINE' -%}
        OFFCOMPOUNDTYPE={{item.OFFCOMPOUNDTYPE}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：USAGERPTMODE=ONLINE 时可选 --- -#}
    {%- if item.USAGERPTMODE == 'ONLINE' -%}
        {%- if item.ONLMETERINGTYPE is not none -%}
            ONLMETERINGTYPE={{item.ONLMETERINGTYPE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：ONLMETERINGTYPE=EVENT/EVENT_TIME/EVENT_VOLUME/EVENT_VOLUME_TIME 时可选 --- -#}
    {%- if item.ONLMETERINGTYPE in ['EVENT', 'EVENT_TIME', 'EVENT_VOLUME', 'EVENT_VOLUME_TIME'] -%}
        {%- if item.EVENTRSUVALUE is not none -%}
            EVENTRSUVALUE={{item.EVENTRSUVALUE}},
        {%- endif -%}
    {%- endif -%}
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
        {%- if item.REDIRENDTOKEN is not none -%}
            REDIRENDTOKEN="{{item.REDIRENDTOKEN}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：ONLMETERINGTYPE=TIME/VOLUME_TIME/EVENT_TIME/EVENT_VOLUME_TIME 时可选 --- -#}
    {%- if item.ONLMETERINGTYPE in ['TIME', 'VOLUME_TIME', 'EVENT_TIME', 'EVENT_VOLUME_TIME'] -%}
        {%- if item.TIMERSUVALUE is not none -%}
            TIMERSUVALUE={{item.TIMERSUVALUE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：ONLMETERINGTYPE=VOLUME/VOLUME_TIME/EVENT_VOLUME/EVENT_VOLUME_TIME 时可选 --- -#}
    {%- if item.ONLMETERINGTYPE in ['VOLUME', 'VOLUME_TIME', 'EVENT_VOLUME', 'EVENT_VOLUME_TIME'] -%}
        {%- if item.VOLUMERSUVALUE is not none -%}
            VOLUMERSUVALUE={{item.VOLUMERSUVALUE}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in set_glburrgroup_list -%}
    SET GLBURRGROUP:
    {#- --- 可选参数 --- -#}
    {%- if item.UPONLURRNAME is not none -%}
        UPONLURRNAME="{{item.UPONLURRNAME}}",
    {%- endif -%}
    {%- if item.DNONLURRNAME is not none -%}
        DNONLURRNAME="{{item.DNONLURRNAME}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 2 //修改全局通用参数CCT模板的QHT参数值为5。

```jinja2
{%- for item in mod_cct_list -%}
    MOD CCT:
    {#- --- 必选参数 --- -#}
    CCTMPLTNAME="{{item.CCTMPLTNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.QHT is not none -%}
        QHT={{item.QHT}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 //配置建立PDU会话时发送ChargingDataRqueset与CHF交互。

```jinja2
{%- for item in set_chfinit_list -%}
    SET CHFINIT:
    {#- --- 必选参数 --- -#}
    CCTMPLTNAME="{{item.CCTMPLTNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.CHFINIT is not none -%}
        CHFINIT={{item.CHFINIT}},
    {%- endif -%}
    {%- if item.CCRINITRGNUM is not none -%}
        CCRINITRGNUM={{item.CCRINITRGNUM}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 //配置Session级/PDU级Trigger。

```jinja2
{%- for item in add_pdutrigger_list -%}
    ADD PDUTRIGGER:
    {#- --- 必选参数 --- -#}
    CCTMPLTNAME="{{item.CCTMPLTNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.QOSCHG is not none -%}
        QOSCHG={{item.QOSCHG}},
    {%- endif -%}
    {%- if item.SRVNDCHG is not none -%}
        SRVNDCHG={{item.SRVNDCHG}},
    {%- endif -%}
    {%- if item.RATCHG is not none -%}
        RATCHG={{item.RATCHG}},
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_rgtrigger_list -%}
    ADD RGTRIGGER:
    {#- --- 必选参数 --- -#}
    CCTMPLTNAME="{{item.CCTMPLTNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.ULCHG is not none -%}
        ULCHG={{item.ULCHG}},
    {%- endif -%}
    {%- if item.PRACHG is not none -%}
        PRACHG={{item.PRACHG}},
    {%- endif -%}
    {%- if item.PSDATAOFFCHG is not none -%}
        PSDATAOFFCHG={{item.PSDATAOFFCHG}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 5 //配置SMF超时未收到ChargingDataResponse消息时的动作。

```jinja2
{%- for item in set_failhandling_list -%}
    SET FAILHANDLING:
    {#- --- 必选参数 --- -#}
    CCTMPLTNAME="{{item.CCTMPLTNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.FHACTION is not none -%}
        FHACTION={{item.FHACTION}},
    {%- endif -%}
    {%- if item.FAILOVERSUP is not none -%}
        FAILOVERSUP={{item.FAILOVERSUP}},
    {%- endif -%}
    {%- if item.AUTOFAILBACK is not none -%}
        AUTOFAILBACK={{item.AUTOFAILBACK}},
    {%- endif -%}
    {%- if item.TXTIMER is not none -%}
        TXTIMER={{item.TXTIMER}},
    {%- endif -%}
    {%- if item.HOLDINGTIME is not none -%}
        HOLDINGTIME={{item.HOLDINGTIME}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 6 //配置SMF收到PDU级异常返回码时的动作。

```jinja2
{%- for item in add_pduscact_list -%}
    ADD PDUSCACT:
    {#- --- 必选参数 --- -#}
    CCTMPLTNAME="{{item.CCTMPLTNAME}}",
    CODETYPE={{item.CODETYPE}},
    SCACT={{item.SCACT}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：CODETYPE=VALUE 时必选 --- -#}
    {%- if item.CODETYPE == 'VALUE' -%}
        STATUSCODE={{item.STATUSCODE}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：SCACT=BLOCK/REDIRECT 时可选 --- -#}
    {%- if item.SCACT in ['BLOCK', 'REDIRECT'] -%}
        {%- if item.BLKTIMER is not none -%}
            BLKTIMER={{item.BLKTIMER}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SCACT=TERM_WITH_REL/TERM_NO_REL 时可选 --- -#}
    {%- if item.SCACT in ['TERM_WITH_REL', 'TERM_NO_REL'] -%}
        {%- if item.GTPV01CAUSE is not none -%}
            GTPV01CAUSE={{item.GTPV01CAUSE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SCACT=TERM_WITH_REL/TERM_NO_REL 时可选 --- -#}
    {%- if item.SCACT in ['TERM_WITH_REL', 'TERM_NO_REL'] -%}
        {%- if item.GTPV2CAUSE is not none -%}
            GTPV2CAUSE={{item.GTPV2CAUSE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SCACT=REDIRECT 时可选 --- -#}
    {%- if item.SCACT == 'REDIRECT' -%}
        {%- if item.RDVIRTIP is not none -%}
            RDVIRTIP="{{item.RDVIRTIP}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SCACT=REDIRECT 时可选 --- -#}
    {%- if item.SCACT == 'REDIRECT' -%}
        {%- if item.RDVIRTIPV6 is not none -%}
            RDVIRTIPV6="{{item.RDVIRTIPV6}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SCACT=TERM_WITH_REL/TERM_NO_REL 时可选 --- -#}
    {%- if item.SCACT in ['TERM_WITH_REL', 'TERM_NO_REL'] -%}
        {%- if item.REACTREQ is not none -%}
            REACTREQ={{item.REACTREQ}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 7 //配置SMF收到RG级异常返回码时的动作。

```jinja2
{%- for item in add_rgrcact_list -%}
    ADD RGRCACT:
    {#- --- 必选参数 --- -#}
    CCTMPLTNAME="{{item.CCTMPLTNAME}}",
    RCCODE={{item.RCCODE}},
    RCACT={{item.RCACT}},
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：RCACT=BLCK_IMMED_RPT/BLCK_NO_RPT/REDIRECT 时可选 --- -#}
    {%- if item.RCACT in ['BLCK_IMMED_RPT', 'BLCK_NO_RPT', 'REDIRECT'] -%}
        {%- if item.BLKTIMER is not none -%}
            BLKTIMER={{item.BLKTIMER}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：RCACT=CONTINUE 时可选 --- -#}
    {%- if item.RCACT == 'CONTINUE' -%}
        {%- if item.HOLDINGTIME is not none -%}
            HOLDINGTIME={{item.HOLDINGTIME}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：RCACT=REDIRECT 时可选 --- -#}
    {%- if item.RCACT == 'REDIRECT' -%}
        {%- if item.RDVIRTIP is not none -%}
            RDVIRTIP="{{item.RDVIRTIP}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：RCACT=REDIRECT 时可选 --- -#}
    {%- if item.RCACT == 'REDIRECT' -%}
        {%- if item.RDVIRTIPV6 is not none -%}
            RDVIRTIPV6="{{item.RDVIRTIPV6}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：RCACT=TERMINATE 时可选 --- -#}
    {%- if item.RCACT == 'TERMINATE' -%}
        {%- if item.REACTREQ is not none -%}
            REACTREQ={{item.REACTREQ}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```


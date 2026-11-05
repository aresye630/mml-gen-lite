---
id: ''
name: 配置异常返回码和异常信元动作
ne_type: UNC
type: feature
description: 融合计费会话过程中，对于各种异常场景，可以在CHF本地设置一些处理动作对融合计费流程进行干预，以确保业务的正常进行。这里的异常场景，主要是指CHF响应SMF请求消息的状况，及响应消息中携带的返回码值。处理动作有三种大小不同的粒度：整个用户的所有计费过程、PDU会话、RG。  适用于SMF。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","计费管理功能","WSFD-011206 支持融合计费","激活支持融合计费","配置异常返回码和异常信元动作"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
融合计费会话过程中，对于各种异常场景，可以在CHF本地设置一些处理动作对融合计费流程进行干预，以确保业务的正常进行。这里的异常场景，主要是指CHF响应SMF请求消息的状况，及响应消息中携带的返回码值。处理动作有三种大小不同的粒度：整个用户的所有计费过程、PDU会话、RG。适用于SMF。

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
    set_failhandling_list:
      type: items
      properties:
        CCTMPLTNAME:
          name: '融合计费模板名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '配置当SMF与CHF交互时，SMF超时未收到CHF返回的ChargingDataResponse消息时，向备CHF重发消息。'
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
          description: '配置当SMF收到CHF的PDU级异常返回码时的动作。基于用户计费过程中的PDU会话进行处理。'
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
          description: '配置当SMF收到CHF的响应的RG级异常返回码时的动作。基于计费过程中PDU会话下的RG进行处理。'
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
    set_cnvrgdchgpara_list:
      type: items
      properties:
        IGNORERSPAVP:
          name: '忽略CHF响应消息的信元列表'
          type: string
          required: false
          description: '配置SMF处理CHF响应消息时，忽略CHF下发的指定信元。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        BADRSPACT:
          name: 'CHF响应消息信元错误的处理动作'
          type: string
          enum:
          - TERMINATE
          - CONTINUE
          required: false
          description: '如果CHF返回的响应消息携带了异常信元，导致SMF无法计费时：   * “BADRSPACT”参数配置为“TERMINATE”时，PDU会话去活。 * “BADRSPACT”参数配置为“CONTINUE”时，用户业务会继续进行，并且不再进行配额管理。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    set_n40badrspact_list:
      type: items
      properties:
        BADRSPTYPE:
          name: 'BADRSP错误原因'
          type: string
          enum:
          - ErrTypeNoUpfId
          - ErrTypeErrMetering
          - ErrTypeNotRspReportRg
          - ErrTypeGsuNotMatchRsu
          - ErrTypeNoMatchHttpCode
          - ErrTypeErrSeqNum
          - ErrTypePushedRgStateDiffWithSess
          - ErrTypeInvalidRgLevRC
          - ErrTypeFuiRedirectWithoutServer
          - ErrTypeRedirectAddrInvalid
          - ErrTypeRedirectWithoutAddr
          - ErrTypeInvalidFuaType
          - ErrTypeEventRgButRspMeteringNoEvent
          - ErrTypeGsuWithOnlyUpOrDnVolume
          - ErrTypeGsuWithZeroTimeQuota
          - ErrTypeGsuForMeteringZero
          - ErrTypeWrongLocation
          required: true
          description: '配置N40接口收到错误响应时的处理动作。如果动作配置为“INHERIT”，则继承**SET CNVRGDCHGPARA**命令的“BADRSPACT”参数配置。  此处取值仅为举例，请根据实际需要配置。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        BADRSPACT:
          name: 'BADRSP处理动作'
          type: string
          enum:
          - INHERIT
          - TERMINATE
          - CONTINUE
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    set_n40badccaact_list:
      type: items
      properties:
        BADRSPTYPE:
          name: 'BADRSPTYPE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        BADRSPACT:
          name: 'BADRSPACT'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    set_failhandling_list:
    - CCTMPLTNAME: 'cct-test'
      FHACTION: CONTINUE
      FAILOVERSUP: ENABLE
      AUTOFAILBACK: ENABLE
      TXTIMER: 5
      HOLDINGTIME: 10
    add_pduscact_list:
    - CCTMPLTNAME: 'cct-test'
      CODETYPE: VALUE
      STATUSCODE: 502
      SCACT: FAILOVER
      BLKTIMER: ''
      GTPV01CAUSE: ''
      GTPV2CAUSE: ''
      RDVIRTIP: ''
      RDVIRTIPV6: ''
      REACTREQ: ''
    add_rgrcact_list:
    - CCTMPLTNAME: 'cct-test'
      RCCODE: QUOTAMNOTAPPL
      RCACT: BLCK_IMMED_RPT
      BLKTIMER: 30
      HOLDINGTIME: ''
      RDVIRTIP: ''
      RDVIRTIPV6: ''
      REACTREQ: ''
    set_cnvrgdchgpara_list:
    - IGNORERSPAVP: FUI
      BADRSPACT: TERMINATE
    set_n40badrspact_list:
    - BADRSPTYPE: ErrTypeFuiRedirectWithoutServer
      BADRSPACT: TERMINATE
    set_n40badccaact_list:
    - BADRSPTYPE: ErrTypeFuiRedirectWithoutServer
      BADRSPACT: TERMINATE
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 进入“MML命令行-UNC”窗口。

### 2 **可选：**配置当SMF与CHF交互时，SMF超时未收到CHF返回的ChargingDataResponse消息时的动作。

```jinja2
{%- if is_optional_smf_cdr_timeout_action -%}
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
{%- endif -%}
```

### 3 **可选：**配置当SMF收到CHF的PDU级异常返回码时的动作。

```jinja2
{%- if is_optional_pdu_abnormal_return_code -%}
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
{%- endif -%}
```

### 4 **可选：**配置当SMF收到CHF的响应的RG级异常返回码时的动作。

```jinja2
{%- if is_optional_rg_abnormal_return_code -%}
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
{%- endif -%}
```

### 5 **可选：**配置忽略CHF响应消息的信元列表。

```jinja2
{%- if is_optional_ignore_response_cell_list -%}
    {%- for item in set_cnvrgdchgpara_list -%}
        SET CNVRGDCHGPARA:
        {#- --- 可选参数 --- -#}
        {%- if item.IGNORERSPAVP is not none -%}
            IGNORERSPAVP={{item.IGNORERSPAVP}},
        {%- endif -%}
        {%- if item.BADRSPACT is not none -%}
            BADRSPACT={{item.BADRSPACT}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### ****SET CNVRGDCHGPARA****命令的“IGNORERSPAVP”参数的取值范围是位域类型，支持如下参数单独配置或同时配置：

### 当“IGNORERSPAVP”参数配置为“INVOCATIONNUM”时，表示忽略CHF响应消息中的Invocation Sequence Number，不检查是否跟请求消息一致。

### 当“IGNORERSPAVP”参数配置为“FUI”时，表示当CHF返回RG级异常返回码和FUI时，忽略CHF响应消息中的FinalUnitIndication，按照对应****ADD RGRCACT****配置的“RCACT”动作执行。当**ADD RGRCACT**未配置时，执行默认动作。

### 当“IGNORERSPAVP”参数配置为“SESSIONFAILOVER”时，表示忽略CHF响应消息中的SessionFailover，使用对应CCT模板通过****SET FAILHANDLING****配置的“FAILOVERSUP”动作，“FAILOVERSUP”表示主CHF故障时，向备CHF发送计费消息进行处理。

### 当“IGNORERSPAVP”参数配置为“FAILUREHANDLING”时，表示忽略CHF响应消息中的FailureHandling，使用对应CCT模板通过**SET FAILHANDLING**配置的“FHACTION”动作。

### 6 **可选：**配置N40接口收到错误响应时的处理动作。

```jinja2
{%- if is_optional_n40_bad_response_action -%}
    {%- for item in set_n40badrspact_list -%}
        SET N40BADRSPACT:
        {#- --- 必选参数 --- -#}
        BADRSPTYPE={{item.BADRSPTYPE}},
        {#- --- 可选参数 --- -#}
        {%- if item.BADRSPACT is not none -%}
            BADRSPACT={{item.BADRSPACT}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_n40badccaact_list的变量区（command: SET N40BADCCAACT） -#}
<!-- MISSING_MACRO: command=SET N40BADCCAACT list_name=set_n40badccaact_list step_id=6 -->
```

### 如果动作配置为“INHERIT”，则继承**SET CNVRGDCHGPARA**命令的“BADRSPACT”参数配置。


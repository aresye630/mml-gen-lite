---
id: ''
name: 配置异常返回码动作
ne_type: UNC
type: feature
description: 本指导描述在UNC上配置NCG/CHF(OCS)响应的异常结果码动作的相关操作过程。  融合计费会话过程中，对于各种异常场景，可以在NCG/CHF(OCS)本地设置一些处理动作对融合计费流程进行干预，以确保业务的正常进行。这里的异常场景，主要是指**NCG/CHF(OCS)响应SMF请求消息的状况**，及**响应消息中携带的返回码值**。处理动作有三种大小不同的粒度：**整个用户的所有计费过程**、**PDU会话**、**RG**。
risk_level: ''
doc_source: ["网络部署","业务专题","5G Core 计费解决方案","计费解决方案概述","计费方案部署与调测","方案一：未部署NCG的计费解决方案","SMF配置","融合计费模板及交互配置","配置异常返回码动作"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本指导描述在UNC上配置NCG/CHF(OCS)响应的异常结果码动作的相关操作过程。融合计费会话过程中，对于各种异常场景，可以在NCG/CHF(OCS)本地设置一些处理动作对融合计费流程进行干预，以确保业务的正常进行。这里的异常场景，主要是指**NCG/CHF(OCS)响应SMF请求消息的状况**，及**响应消息中携带的返回码值**。处理动作有三种大小不同的粒度：**整个用户的所有计费过程**、**PDU会话**、**RG**。

## 必备事项
前提条件

* 请仔细阅读融合计费原理。
* 完成加载License。
* 已完成融合计费模板创建。
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
          description: '配置融合计费模板故障处理相关动作。  如果为全局融合计费模板配置故障处理相关动作，则“CCTMPLTNAME”为“global”。'
          data_source: '从已有配置中获取'
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
          data_source: '与对端协商'
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
        RANGETIME:
          name: '用户保持调整时长(分钟)'
          type: integer
          minimum: 0
          maximum: 60
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CNVCHGRECOVER:
          name: '融合计费自动恢复功能开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RECOVERINTERVAL:
          name: '融合计费自动恢复间隔 (分钟)'
          type: integer
          minimum: 0
          maximum: 60
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        UPDCONTTERM:
          name: 'Update消息触发业务放通结束计费会话开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SCPFAILOVERSW:
          name: 'SCP故障重选开关'
          type: string
          enum:
          - SCP_NOT_FAILOVER
          - SCP_FAILOVER
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
          description: '配置当SMF收到NCG/CHF(OCS)的PDU级异常返回码时的动作。基于用户计费过程中的PDU会话进行处理。  如果为全局融合计费模板配置PDU级异常返回码动作，则“CCTMPLTNAME”为“global”。'
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
          description: '配置当SMF收到NCG/CHF(OCS)的响应的RG级异常返回码时的动作。基于计费过程中PDU会话下的RG进行处理。  如果为全局融合计费模板配置RG级异常返回码动作，则“CCTMPLTNAME”为“global”。'
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
          name: 'RG级阻塞处理时间间隔(分钟)'
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
          description: '配置融合计费全局参数。  本示例以配置CHF(OCS)响应消息的信元列表为FUI以及CHF(OCS)响应消息信元错误的处理动作为TERMINATE为例。请根据实际业务需求参考**SET CNVRGDCHGPARA**命令帮助文档进行配置。'
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
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
  examples:
    set_failhandling_list:
    - CCTMPLTNAME: 'cct-test'
      FHACTION: CONTINUE
      FAILOVERSUP: ENABLE
      AUTOFAILBACK: ENABLE
      TXTIMER: 3
      HOLDINGTIME: 30
      RANGETIME: 30
      CNVCHGRECOVER: DISABLE
      RECOVERINTERVAL: 20
      UPDCONTTERM: DISABLE
      SCPFAILOVERSW: SCP_NOT_FAILOVER
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
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 进入“MML命令行-UNC”窗口。

### 2 **可选：**配置当SMF与NCG/CHF(OCS)交互时，SMF超时未收到NCG/CHF(OCS)返回的ChargingDataResponse消息时的动作。

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
        {%- if item.CNVCHGRECOVER is not none -%}
            CNVCHGRECOVER={{item.CNVCHGRECOVER}},
        {%- endif -%}
        {%- if item.RANGETIME is not none -%}
            RANGETIME={{item.RANGETIME}},
        {%- endif -%}
        {%- if item.RECOVERINTERVAL is not none -%}
            RECOVERINTERVAL={{item.RECOVERINTERVAL}},
        {%- endif -%}
        {%- if item.SCPFAILOVERSW is not none -%}
            SCPFAILOVERSW={{item.SCPFAILOVERSW}},
        {%- endif -%}
        {%- if item.UPDCONTTERM is not none -%}
            UPDCONTTERM={{item.UPDCONTTERM}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 3 **可选：**配置当SMF收到NCG/CHF(OCS)的PDU级异常返回码时的动作。

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

### 4 **可选：**配置当SMF收到NCG/CHF(OCS)的响应的RG级异常返回码时的动作。

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

### 5 **可选：**配置忽略NCG/CHF(OCS)响应消息的信元列表。

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

### 当“IGNORERSPAVP”参数配置为“INVOCATIONNUM”时，表示忽略NCG/CHF(OCS)响应消息中的Invocation Sequence Number，不检查是否跟请求消息一致。

### 当“IGNORERSPAVP”参数配置为“FUI”时，表示当NCG/CHF(OCS)返回RG级异常返回码和FUI时，忽略NCG/CHF(OCS)响应消息中的FinalUnitIndication，按照对应****ADD RGRCACT****配置的“RCACT”动作执行。当**ADD RGRCACT**未配置时，执行默认动作。

### 当“IGNORERSPAVP”参数配置为“SESSIONFAILOVER”时，表示忽略NCG/CHF(OCS)响应消息中的SessionFailover，使用对应CCT模板通过****SET FAILHANDLING****配置的“FAILOVERSUP”动作，“FAILOVERSUP”表示主NCG/CHF(OCS)故障时，向备NCG/CHF(OCS)发送计费消息进行处理。

### 当“IGNORERSPAVP”参数配置为“FAILUREHANDLING”时，表示忽略NCG/CHF(OCS)响应消息中的FailureHandling，使用对应CCT模板通过**SET FAILHANDLING**配置的“FHACTION”动作。


---
id: ''
name: 配置异常返回码动作
ne_type: UDG
type: feature
description: 本指导描述在UNC上配置NCG/CHF(OCS)响应的异常结果码动作的相关操作过程。  融合计费会话过程中，对于各种异常场景，可以在NCG/CHF(OCS)本地设置一些处理动作对融合计费流程进行干预，以确保业务的正常进行。这里的异常场景，主要是指**NCG/CHF(OCS)响应SMF请求消息的状况**，及**响应消息中携带的返回码值**。处理动作有三种大小不同的粒度：**整个用户的所有计费过程**、**PDU会话**、**RG**。
risk_level: ''
doc_source: ["特性部署","业务专题","5G Core 计费解决方案","计费解决方案概述","计费方案部署与调测","方案三：部署NCG且基于服务化接口的纯离线计费组网方案（N40接口）","SMF配置","融合计费模板及交互配置（N40接口）","配置异常返回码动作"]
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
          required: false
          description: '配置融合计费模板故障处理相关动作。  如果为全局融合计费模板配置故障处理相关动作，则“CCTMPLTNAME”为“global”。'
          data_source: '从已有配置中获取'
          pattern: ''
          default: ''
        FHACTION:
          name: 'FH处理动作'
          type: string
          required: false
          description: ''
          data_source: '与对端协商'
          pattern: ''
          default: ''
        FAILOVERSUP:
          name: '支持failover使能开关'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AUTOFAILBACK:
          name: 'failback使能开关'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TXTIMER:
          name: 'Tx定时器时长(秒)'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        HOLDINGTIME:
          name: '用户保持时长(分钟)'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RANGETIME:
          name: '用户保持调整时长(分钟)'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CNVCHGRECOVER:
          name: '融合计费自动恢复功能开关'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RECOVERINTERVAL:
          name: '融合计费自动恢复间隔 (分钟)'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        UPDCONTTERM:
          name: 'Update消息触发业务放通结束计费会话开关'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SCPFAILOVERSW:
          name: 'SCP故障重选开关'
          type: string
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
          required: false
          description: '配置当SMF收到NCG/CHF(OCS)的PDU级异常返回码时的动作。基于用户计费过程中的PDU会话进行处理。  如果为全局融合计费模板配置PDU级异常返回码动作，则“CCTMPLTNAME”为“global”。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        CODETYPE:
          name: '返回码类型'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        STATUSCODE:
          name: '状态码'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SCACT:
          name: '处理动作'
          type: string
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
          required: false
          description: '配置当SMF收到NCG/CHF(OCS)的响应的RG级异常返回码时的动作。基于计费过程中PDU会话下的RG进行处理。  如果为全局融合计费模板配置RG级异常返回码动作，则“CCTMPLTNAME”为“global”。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        RCCODE:
          name: 'RG级异常返回码'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RCACT:
          name: 'RG级异常返回码动作'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        BLKTIMER:
          name: 'RG级阻塞处理时间间隔(分钟)'
          type: string
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
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
  examples:
    set_failhandling_list:
    - CCTMPLTNAME: cct-test
      FHACTION: CONTINUE
      FAILOVERSUP: ENABLE
      AUTOFAILBACK: ENABLE
      TXTIMER: '3'
      HOLDINGTIME: '30'
      RANGETIME: '30'
      CNVCHGRECOVER: DISABLE
      RECOVERINTERVAL: '20'
      UPDCONTTERM: DISABLE
      SCPFAILOVERSW: SCP_NOT_FAILOVER
    add_pduscact_list:
    - CCTMPLTNAME: cct-test
      CODETYPE: VALUE
      STATUSCODE: '502'
      SCACT: FAILOVER
    add_rgrcact_list:
    - CCTMPLTNAME: cct-test
      RCCODE: QUOTAMNOTAPPL
      RCACT: BLCK_IMMED_RPT
      BLKTIMER: '30'
    set_cnvrgdchgpara_list:
    - IGNORERSPAVP: FUI
      BADRSPACT: TERMINATE
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 进入“MML命令行-UNC”窗口。

### 2 **可选：**配置当SMF与NCG/CHF(OCS)交互时，SMF超时未收到NCG/CHF(OCS)返回的ChargingDataResponse消息时的动作。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_failhandling_list的变量区（command: SET FAILHANDLING） -#}
<!-- MISSING_MACRO: command=SET FAILHANDLING list_name=set_failhandling_list step_id=2 -->
```

### 3 **可选：**配置当SMF收到NCG/CHF(OCS)的PDU级异常返回码时的动作。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_pduscact_list的变量区（command: ADD PDUSCACT） -#}
<!-- MISSING_MACRO: command=ADD PDUSCACT list_name=add_pduscact_list step_id=3 -->
```

### 4 **可选：**配置当SMF收到NCG/CHF(OCS)的响应的RG级异常返回码时的动作。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_rgrcact_list的变量区（command: ADD RGRCACT） -#}
<!-- MISSING_MACRO: command=ADD RGRCACT list_name=add_rgrcact_list step_id=4 -->
```

### 5 **可选：**配置忽略NCG/CHF(OCS)响应消息的信元列表。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_cnvrgdchgpara_list的变量区（command: SET CNVRGDCHGPARA） -#}
<!-- MISSING_MACRO: command=SET CNVRGDCHGPARA list_name=set_cnvrgdchgpara_list step_id=5 -->
```

### ****SET CNVRGDCHGPARA****命令的“IGNORERSPAVP”参数的取值范围是位域类型，支持如下参数单独配置或同时配置：

### 当“IGNORERSPAVP”参数配置为“INVOCATIONNUM”时，表示忽略NCG/CHF(OCS)响应消息中的Invocation Sequence Number，不检查是否跟请求消息一致。

### 当“IGNORERSPAVP”参数配置为“FUI”时，表示当NCG/CHF(OCS)返回RG级异常返回码和FUI时，忽略NCG/CHF(OCS)响应消息中的FinalUnitIndication，按照对应****ADD RGRCACT****配置的“RCACT”动作执行。当**ADD RGRCACT**未配置时，执行默认动作。

### 当“IGNORERSPAVP”参数配置为“SESSIONFAILOVER”时，表示忽略NCG/CHF(OCS)响应消息中的SessionFailover，使用对应CCT模板通过****SET FAILHANDLING****配置的“FAILOVERSUP”动作，“FAILOVERSUP”表示主NCG/CHF(OCS)故障时，向备NCG/CHF(OCS)发送计费消息进行处理。

### 当“IGNORERSPAVP”参数配置为“FAILUREHANDLING”时，表示忽略NCG/CHF(OCS)响应消息中的FailureHandling，使用对应CCT模板通过**SET FAILHANDLING**配置的“FHACTION”动作。


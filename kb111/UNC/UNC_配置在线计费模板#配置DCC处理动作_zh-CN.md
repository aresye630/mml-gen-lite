---
id: ''
name: 配置DCC处理动作
ne_type: UNC
type: feature
description: 本指导描述UNC对于OCS故障或者OCS的响应消息携带的特定结果码配置相就的处理动作的配置过程。  在线计费会话过程中，对于各种正常和异常场景，可以在UNC本地设置一些处理动作对DCC流程进行干预。这里的正常和异常场景，主要是指OCS响应UNC请求消息的状况，及响应消息的返回码值。
risk_level: ''
doc_source: ["网络部署","业务专题","5G Core 计费解决方案","计费解决方案概述","计费方案部署与调测","方案五：部署NCG且融合接口计费组网方案","SMF配置","在线计费配置","在线计费模板及交互配置","配置在线计费模板","配置DCC处理动作"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools:
- getParameterValue('MOD DCCTEMPLATE')
- getParameterValue('SET OCSDOWNACTION')
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本指导描述UNC对于OCS故障或者OCS的响应消息携带的特定结果码配置相就的处理动作的配置过程。在线计费会话过程中，对于各种正常和异常场景，可以在UNC本地设置一些处理动作对DCC流程进行干预。这里的正常和异常场景，主要是指OCS响应UNC请求消息的状况，及响应消息的返回码值。

## 必备事项
前提条件

* 请仔细阅读Ga/Gy接口离线/在线计费。

* 已完成计费属性、APN、User Profile创建。
* 已根据配置在线计费模板完成在线计费模板创建和绑定，根据配置在线计费的费率标识完成在线计费费率标识配置。
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
          description: '使用的DCC模板名称。  说明：  如果需要配置在线计费全局参数，则需要使用**MOD DCCTEMPLATE**命令，“DCCTMPLTNAME”参数值为“global”。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        CCFH:
          name: 'CCFH处理动作'
          type: string
          enum:
          - BLOCK
          - CONTINUE
          - INHERIT
          - RETRY_AND_TERM
          - TERMINATE
          required: false
          description: '配置Tx定时器超时，以及OCS返回的错误码动作为failover时的处理方式。'
          data_source: '全网规划'
          pattern: ''
          default: INHERIT
        CCFHOFFLINE:
          name: 'CCFH离线标志位使能开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          - INHERIT
          required: false
          description: '配置发生CCFH之后是否在离线话单中添加CCFH标志位。该参数开启，CCFH之后会使非离线计费用户离线计费能力强制设置为使能。'
          data_source: ''
          pattern: ''
          default: INHERIT
        FAILOVERSUP:
          name: '支持failover使能开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          - INHERIT
          required: false
          description: '配置是否支持failover功能使能。'
          data_source: ''
          pattern: ''
          default: INHERIT
    mod_dcctemplate_list:
      type: items
      properties:
        DCCTMPLTNAME:
          name: 'DCC模板名称'
          type: string
          maxLength: 63
          required: true
          description: '使用的DCC模板名称。  说明：  如果需要配置在线计费全局参数，则需要使用**MOD DCCTEMPLATE**命令，“DCCTMPLTNAME”参数值为“global”。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        CCFH:
          name: 'CCFH处理动作'
          type: string
          enum:
          - BLOCK
          - CONTINUE
          - INHERIT
          - RETRY_AND_TERM
          - TERMINATE
          required: false
          description: '配置Tx定时器超时，以及OCS返回的错误码动作为failover时的处理方式。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        CCFHOFFLINE:
          name: 'CCFH离线标志位使能开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          - INHERIT
          required: false
          description: '配置发生CCFH之后是否在离线话单中添加CCFH标志位。该参数开启，CCFH之后会使非离线计费用户离线计费能力强制设置为使能。'
          data_source: ''
          pattern: ''
          default: ''
        FAILOVERSUP:
          name: '支持failover使能开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          - INHERIT
          required: false
          description: '配置是否支持failover功能使能。'
          data_source: ''
          pattern: ''
          default: ''
    add_dcctemplate_list_1:
      type: items
      properties:
        DCCTMPLTNAME:
          name: 'DCC模板名称'
          type: string
          maxLength: 63
          required: true
          description: '使用的DCC模板名称。  说明：  如果需要配置在线计费全局参数，则需要使用**MOD DCCTEMPLATE**命令，“DCCTMPLTNAME”参数值为“global”。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        CCFH:
          name: 'CCFH处理动作'
          type: string
          enum:
          - BLOCK
          - CONTINUE
          - INHERIT
          - RETRY_AND_TERM
          - TERMINATE
          required: false
          description: '配置Tx定时器超时，以及OCS返回的错误码动作为failover时的处理方式。'
          data_source: '全网规划'
          pattern: ''
          default: INHERIT
        CCFHOFFLINE:
          name: 'CCFH离线标志位使能开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          - INHERIT
          required: false
          description: '配置发生CCFH之后是否在离线话单中添加CCFH标志位。该参数开启，CCFH之后会使非离线计费用户离线计费能力强制设置为使能。'
          data_source: ''
          pattern: ''
          default: INHERIT
        FAILOVERSUP:
          name: '支持failover使能开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          - INHERIT
          required: false
          description: '配置是否支持failover功能使能。'
          data_source: ''
          pattern: ''
          default: INHERIT
    mod_dcctemplate_list_1:
      type: items
      properties:
        DCCTMPLTNAME:
          name: 'DCC模板名称'
          type: string
          maxLength: 63
          required: true
          description: '使用的DCC模板名称。  说明：  如果需要配置在线计费全局参数，则需要使用**MOD DCCTEMPLATE**命令，“DCCTMPLTNAME”参数值为“global”。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        CCFH:
          name: 'CCFH处理动作'
          type: string
          enum:
          - BLOCK
          - CONTINUE
          - INHERIT
          - RETRY_AND_TERM
          - TERMINATE
          required: false
          description: '配置Tx定时器超时，以及OCS返回的错误码动作为failover时的处理方式。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        CCFHOFFLINE:
          name: 'CCFH离线标志位使能开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          - INHERIT
          required: false
          description: '配置发生CCFH之后是否在离线话单中添加CCFH标志位。该参数开启，CCFH之后会使非离线计费用户离线计费能力强制设置为使能。'
          data_source: ''
          pattern: ''
          default: ''
        FAILOVERSUP:
          name: '支持failover使能开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          - INHERIT
          required: false
          description: '配置是否支持failover功能使能。'
          data_source: ''
          pattern: ''
          default: ''
    add_dcctemplate_list_2:
      type: items
      properties:
        DCCTMPLTNAME:
          name: 'DCC模板名称'
          type: string
          maxLength: 63
          required: true
          description: '使用的DCC模板名称。  说明：  如果需要配置在线计费全局参数，则需要使用**MOD DCCTEMPLATE**命令，“DCCTMPLTNAME”参数值为“global”。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        CCFH:
          name: 'CCFH处理动作'
          type: string
          enum:
          - BLOCK
          - CONTINUE
          - INHERIT
          - RETRY_AND_TERM
          - TERMINATE
          required: false
          description: '配置Tx定时器超时，以及OCS返回的错误码动作为failover时的处理方式。'
          data_source: '全网规划'
          pattern: ''
          default: INHERIT
        CCFHOFFLINE:
          name: 'CCFH离线标志位使能开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          - INHERIT
          required: false
          description: '配置发生CCFH之后是否在离线话单中添加CCFH标志位。该参数开启，CCFH之后会使非离线计费用户离线计费能力强制设置为使能。'
          data_source: ''
          pattern: ''
          default: INHERIT
        FAILOVERSUP:
          name: '支持failover使能开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          - INHERIT
          required: false
          description: '配置是否支持failover功能使能。'
          data_source: ''
          pattern: ''
          default: INHERIT
    mod_dcctemplate_list_2:
      type: items
      properties:
        DCCTMPLTNAME:
          name: 'DCC模板名称'
          type: string
          maxLength: 63
          required: true
          description: '使用的DCC模板名称。  说明：  如果需要配置在线计费全局参数，则需要使用**MOD DCCTEMPLATE**命令，“DCCTMPLTNAME”参数值为“global”。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        CCFH:
          name: 'CCFH处理动作'
          type: string
          enum:
          - BLOCK
          - CONTINUE
          - INHERIT
          - RETRY_AND_TERM
          - TERMINATE
          required: false
          description: '配置Tx定时器超时，以及OCS返回的错误码动作为failover时的处理方式。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        CCFHOFFLINE:
          name: 'CCFH离线标志位使能开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          - INHERIT
          required: false
          description: '配置发生CCFH之后是否在离线话单中添加CCFH标志位。该参数开启，CCFH之后会使非离线计费用户离线计费能力强制设置为使能。'
          data_source: ''
          pattern: ''
          default: ''
        FAILOVERSUP:
          name: '支持failover使能开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          - INHERIT
          required: false
          description: '配置是否支持failover功能使能。'
          data_source: ''
          pattern: ''
          default: ''
    add_dcctemplate_list_3:
      type: items
      properties:
        DCCTMPLTNAME:
          name: 'DCC模板名称'
          type: string
          maxLength: 63
          required: true
          description: '使用的DCC模板名称。  说明：  如果需要配置在线计费全局参数，则需要使用**MOD DCCTEMPLATE**命令，“DCCTMPLTNAME”参数值为“global”。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        CCFH:
          name: 'CCFH处理动作'
          type: string
          enum:
          - BLOCK
          - CONTINUE
          - INHERIT
          - RETRY_AND_TERM
          - TERMINATE
          required: false
          description: '配置Tx定时器超时，以及OCS返回的错误码动作为failover时的处理方式。'
          data_source: '全网规划'
          pattern: ''
          default: INHERIT
        CCFHOFFLINE:
          name: 'CCFH离线标志位使能开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          - INHERIT
          required: false
          description: '配置发生CCFH之后是否在离线话单中添加CCFH标志位。该参数开启，CCFH之后会使非离线计费用户离线计费能力强制设置为使能。'
          data_source: ''
          pattern: ''
          default: INHERIT
        FAILOVERSUP:
          name: '支持failover使能开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          - INHERIT
          required: false
          description: '配置是否支持failover功能使能。'
          data_source: ''
          pattern: ''
          default: INHERIT
    mod_dcctemplate_list_3:
      type: items
      properties:
        DCCTMPLTNAME:
          name: 'DCC模板名称'
          type: string
          maxLength: 63
          required: true
          description: '使用的DCC模板名称。  说明：  如果需要配置在线计费全局参数，则需要使用**MOD DCCTEMPLATE**命令，“DCCTMPLTNAME”参数值为“global”。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        CCFH:
          name: 'CCFH处理动作'
          type: string
          enum:
          - BLOCK
          - CONTINUE
          - INHERIT
          - RETRY_AND_TERM
          - TERMINATE
          required: false
          description: '配置Tx定时器超时，以及OCS返回的错误码动作为failover时的处理方式。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        CCFHOFFLINE:
          name: 'CCFH离线标志位使能开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          - INHERIT
          required: false
          description: '配置发生CCFH之后是否在离线话单中添加CCFH标志位。该参数开启，CCFH之后会使非离线计费用户离线计费能力强制设置为使能。'
          data_source: ''
          pattern: ''
          default: ''
        FAILOVERSUP:
          name: '支持failover使能开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          - INHERIT
          required: false
          description: '配置是否支持failover功能使能。'
          data_source: ''
          pattern: ''
          default: ''
    set_txtimer_list:
      type: items
      properties:
        DCCTMPLTNAME:
          name: 'DCC模板名称'
          type: string
          maxLength: 63
          required: true
          description: '配置Tx定时器时长。 说明：  * 如果需要配置在线计费全局参数，则“DCCTMPLTNAME”参数值为“global”。 * Tx定时器超时时长配置较大，可能激活响应的总时长过长，用户激活失败。建议：   + “TXTIMER”小于GGSN-C/PGW-C产品**ADD GTPCT3N3**命令配置的T3\*N3时长及SGSN/MME/SGW-C的T3\*N3时长。   + “TXTIMER”小于产品**SET SMCOMMTIMER**命令配置的“TCHARGING”的时长。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        TXTIMERFLAG:
          name: 'Tx定时器配置模式'
          type: string
          enum:
          - APP_RETRANSMIT
          - INHERIT
          - TXTIMER_VALUE
          required: true
          description: ''
          data_source: '整网规划'
          pattern: ''
          default: ''
        TXTIMER:
          name: 'Tx定时器时长（秒）'
          type: integer
          minimum:
          - 1
          - 4294967295
          maximum:
          - 20
          - 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RETRYTIMEOUT:
          name: '应用重传时间间隔（秒）'
          type: integer
          minimum: 1
          maximum: 3
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RETRYTIMES:
          name: '应用重传次数'
          type: integer
          minimum: 0
          maximum: 3
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_ofccdrpara_list:
      type: items
      properties:
        PSFCIFORMAT:
          name: 'OCS故障导致用户离线后产生的话单pSFreeFormatData格式'
          type: string
          enum:
          - ASCII
          - HEX
          required: false
          description: '配置OCS故障导致用户离线后产生的话单pSFurnishChargingInformation中pSFreeFormatData字段的格式。'
          data_source: '与对端协商'
          pattern: ''
          default: ''
        CCFHCDRSW:
          name: 'CCFH强制产生话单开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '配置CCFH（Credit Control Failure Handling）是否强制产生话单。'
          data_source: ''
          pattern: ''
          default: ''
        CCFHCDRCC:
          name: 'CCFH强制产生话单填充的Charging Characteristics值'
          type: string
          maxLength: 6
          required: false
          description: '配置CCFH强制产生话单填充的Charging Characteristics的值。'
          data_source: ''
          pattern: ''
          default: ''
        R6EGCDRCCFHSW:
          name: 'R6 eGCRD支持CCFH强制生成话单'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '配置CCFH发生时是否支持强制产生R6 eGCDR话单。'
          data_source: ''
          pattern: ''
          default: ''
    set_holdingtime_list:
      type: items
      properties:
        DCCTMPLTNAME:
          name: 'DCC模板名称'
          type: string
          maxLength: 63
          required: true
          description: '配置在线计费用户转离线计费后，可以继续使用业务的时长，超出该时长后，用户会被去激活。  说明：  * 如果需要配置在线计费全局参数，则“DCCTMPLTNAME”参数值为“global”。 * “RANGETIME”是在“HOLDINGTIME”基础上增加的一个随机调整范围。每个转离线的用户都会被增加一个“RANGETIME”范围内的随机值作为补充时长。 * 建议配置该时长，使批量转离线的用户可以离散的被去激活，从而也可以离散的再次激活，以避免集中去激活后再集中激活，对周边网元造成信令冲击。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        HOLDINGTIME:
          name: '用户保持时长（分）'
          type: integer
          minimum:
          - 0
          - 4294967295
          maximum:
          - 2880
          - 4294967295
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        RANGETIME:
          name: '用户保持调整时长（分）'
          type: integer
          minimum:
          - 0
          - 4294967295
          maximum:
          - 60
          - 4294967295
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_holdingtime_list_1:
      type: items
      properties:
        DCCTMPLTNAME:
          name: 'DCC模板名称'
          type: string
          maxLength: 63
          required: true
          description: '配置在线计费用户转离线计费后，可以继续使用业务的时长，超出该时长后，用户会被去激活。  说明：  * 如果需要配置在线计费全局参数，则“DCCTMPLTNAME”参数值为“global”。 * “RANGETIME”是在“HOLDINGTIME”基础上增加的一个随机调整范围。每个转离线的用户都会被增加一个“RANGETIME”范围内的随机值作为补充时长。 * 建议配置该时长，使批量转离线的用户可以离散的被去激活，从而也可以离散的再次激活，以避免集中去激活后再集中激活，对周边网元造成信令冲击。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        HOLDINGTIME:
          name: '用户保持时长（分）'
          type: integer
          minimum:
          - 0
          - 4294967295
          maximum:
          - 2880
          - 4294967295
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        RANGETIME:
          name: '用户保持调整时长（分）'
          type: integer
          minimum:
          - 0
          - 4294967295
          maximum:
          - 60
          - 4294967295
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_ocsdownaction_list:
      type: items
      properties:
        DCCTMPLTNAME:
          name: 'DCC模板名称'
          type: string
          maxLength: 63
          required: true
          description: '使用的DCC模板名称。  说明：  如果需要配置在线计费全局参数，则“DCCTMPLTNAME”参数值为“global”。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        OCSDNACTION:
          name: 'OCS断用户处理动作'
          type: string
          enum:
          - BLOCK
          - FORBIDDEN
          - INHERIT
          - PERMIT
          required: true
          description: '配置用户激活流程中，由于OCS状态异常或者Gy链路异常导致无可用OCS时UNC的处理动作。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        HOLDINGTMFLAG:
          name: 'OCS断用户允许在线时间控制开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          - INHERIT
          required: false
          description: '配置当“OCSDNACTION”值为“PERMIT”时，是否使用HoldingTime控制允许用户访问的时间。HoldingTime由命令**SET HOLDINGTIME**配置。'
          data_source: ''
          pattern: ''
          default: ''
    add_cmdrcact_list:
      type: items
      properties:
        DCCTMPLTNAME:
          name: '在线计费模板名称'
          type: string
          maxLength: 63
          required: true
          description: 'CCA消息中命令层返回异常消息码的处理动作。  说明：  如果需要配置在线计费全局参数，则“DCCTMPLTNAME”参数值为“global”。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        CMDRC:
          name: '命令层异常返回码'
          type: string
          maxLength: 4
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        CMDRCACT:
          name: '命令层异常返回码处理动作'
          type: string
          enum:
          - BLOCK
          - CONTINUE
          - FAILOVER
          - INHERIT
          - REDIRECT
          - TERM_NO_CCRT
          - TERM_WITH_CCRT
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        CCAHOLDTIME:
          name: 'CCA Holding Timer开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
        CMDLEVREACTREQ:
          name: '命令层重新激活请求'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
        CMDRCGTPV01:
          name: '命令层去活原因值GtpV0-1'
          type: integer
          minimum:
          - 0
          - 192
          maximum:
          - 0
          - 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 0
        CMDRCGTPV2:
          name: '命令层去活原因值GtpV2'
          type: integer
          minimum:
          - 0
          - 64
          maximum:
          - 0
          - 239
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 0
        CMDRDVIRTIP:
          name: '命令层重定向处理重定向IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CMDRDVIRTIPV6:
          name: '命令层重定向处理重定向IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_cmdlevdftbeh_list:
      type: items
      properties:
        DCCTMPLTNAME:
          name: 'DCC模板名称'
          type: string
          maxLength: 63
          required: true
          description: 'CCA消息中命令层返回异常消息码的默认处理动作。  说明：  如果需要配置在线计费全局参数，则“DCCTMPLTNAME”参数值为“global”。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        CMDLEVDFTBEH:
          name: '命令层缺省异常返回码处理动作配置'
          type: string
          enum:
          - BLOCK
          - CONTINUE
          - FAILOVER
          - INHERIT
          - REDIRECT
          - TERM_NO_CCRT
          - TERM_WITH_CCRT
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        CCAHOLDTIME:
          name: 'CCA Holding Timer开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CMDDFTGTPV01:
          name: '命令层去活原因值GtpV0-1'
          type: integer
          minimum:
          - 0
          - 192
          maximum:
          - 0
          - 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CMDDFTGTPV2:
          name: '命令层去活原因值GtpV2'
          type: integer
          minimum:
          - 0
          - 64
          maximum:
          - 0
          - 239
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CMDDFTRDIPV4:
          name: '命令层缺省处理重定向IP'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CMDDFTRDIPV6:
          name: '命令层缺省处理重定向IPV6'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CMDLEVREACTREQ:
          name: '命令层重新激活请求'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_msccrcact_list:
      type: items
      properties:
        DCCTMPLTNAME:
          name: '在线计费模板名称'
          type: string
          maxLength: 63
          required: true
          description: 'CCA消息中MSCC层返回异常消息码的处理动作。  说明：  如果需要配置在线计费全局参数，则“DCCTMPLTNAME”参数值为“global”。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        MSCCRC:
          name: 'MSCC层异常返回码'
          type: string
          maxLength: 4
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        MSCCRCACT:
          name: 'MSCC层异常返回码动作'
          type: string
          enum:
          - BLCK_IMMED_RPT
          - BLCK_NO_RPT
          - BLCK_TRG_RPT
          - BLOCK
          - CONTINUE
          - INHERIT
          - REDIRECT
          - TERMINATE
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        MSCCBLKTIMER:
          name: 'MSCC层阻塞处理时间间隔'
          type: integer
          minimum: 1
          maximum: 1440
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MSCCRDVIRTIP:
          name: 'MSCC层重定向处理重定向IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MSCCRDVIRTIPV6:
          name: 'MSCC层重定向处理重定向IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MSCCREACTREQ:
          name: 'MSCC层重新激活请求'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
    set_mscclevdftbeh_list:
      type: items
      properties:
        DCCTMPLTNAME:
          name: 'DCC模板名称'
          type: string
          maxLength: 63
          required: true
          description: 'CCA消息中MSCC层返回异常消息码的默认处理动作。  说明：  如果需要配置在线计费全局参数，则“DCCTMPLTNAME”参数值为“global”。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        MSCCLEVDFTBEH:
          name: 'MSCC层缺省处理动作'
          type: string
          enum:
          - BLCK_IMMED_RPT
          - BLCK_NO_RPT
          - BLCK_TRG_RPT
          - BLOCK
          - CONTINUE
          - INHERIT
          - REDIRECT
          - TERMINATE
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        MSCCDFTBLKTM:
          name: 'MSCC层缺省阻塞处理时间间隔（分）'
          type: integer
          minimum: 1
          maximum: 1440
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MSCCDFTRDIPV4:
          name: 'MSCC层缺省处理重定向IP'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MSCCDFTRDIPV6:
          name: 'MSCC层缺省处理重定向IPV6'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MSCCREACTREQ:
          name: 'MSCC层重新激活请求'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_dcctemplate_list_4:
      type: items
      properties:
        DCCTMPLTNAME:
          name: 'DCC模板名称'
          type: string
          maxLength: 63
          required: true
          description: '使用的DCC模板名称。  说明：  如果需要配置在线计费全局参数，则需要使用**MOD DCCTEMPLATE**命令，“DCCTMPLTNAME”参数值为“global”。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        CCFH:
          name: 'CCFH处理动作'
          type: string
          enum:
          - BLOCK
          - CONTINUE
          - INHERIT
          - RETRY_AND_TERM
          - TERMINATE
          required: false
          description: '配置Tx定时器超时，以及OCS返回的错误码动作为failover时的处理方式。'
          data_source: '全网规划'
          pattern: ''
          default: INHERIT
        CCFHOFFLINE:
          name: 'CCFH离线标志位使能开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          - INHERIT
          required: false
          description: '配置发生CCFH之后是否在离线话单中添加CCFH标志位。该参数开启，CCFH之后会使非离线计费用户离线计费能力强制设置为使能。'
          data_source: ''
          pattern: ''
          default: INHERIT
        FAILOVERSUP:
          name: '支持failover使能开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          - INHERIT
          required: false
          description: '配置是否支持failover功能使能。'
          data_source: ''
          pattern: ''
          default: INHERIT
    mod_dcctemplate_list_4:
      type: items
      properties:
        DCCTMPLTNAME:
          name: 'DCC模板名称'
          type: string
          maxLength: 63
          required: true
          description: '使用的DCC模板名称。  说明：  如果需要配置在线计费全局参数，则需要使用**MOD DCCTEMPLATE**命令，“DCCTMPLTNAME”参数值为“global”。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        CCFH:
          name: 'CCFH处理动作'
          type: string
          enum:
          - BLOCK
          - CONTINUE
          - INHERIT
          - RETRY_AND_TERM
          - TERMINATE
          required: false
          description: '配置Tx定时器超时，以及OCS返回的错误码动作为failover时的处理方式。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        CCFHOFFLINE:
          name: 'CCFH离线标志位使能开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          - INHERIT
          required: false
          description: '配置发生CCFH之后是否在离线话单中添加CCFH标志位。该参数开启，CCFH之后会使非离线计费用户离线计费能力强制设置为使能。'
          data_source: ''
          pattern: ''
          default: ''
        FAILOVERSUP:
          name: '支持failover使能开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          - INHERIT
          required: false
          description: '配置是否支持failover功能使能。'
          data_source: ''
          pattern: ''
          default: ''
    set_tctimer_list:
      type: items
      properties:
        TCTIMERLEN:
          name: 'TC定时器时长（单位500ms）'
          type: integer
          minimum: 1
          maximum: 3600
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TCMODE:
          name: '定时器模式'
          type: string
          enum:
          - FIXED
          - MULTIPLY
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_twtimer_list:
      type: items
      properties:
        TWTIMERLEN:
          name: 'TW定时器时长（秒）'
          type: integer
          minimum: 1
          maximum: 180
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TWNORESPTIMES:
          name: 'DWR消息响应超时次数上限'
          type: integer
          minimum: 1
          maximum: 3
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TWRSTTCP:
          name: '超时次数达到上限复位连接'
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
    add_dcctemplate_list:
    - DCCTMPLTNAME: 'dcc-test'
      CCFH: CONTINUE
      CCFHOFFLINE: ENABLE
      FAILOVERSUP: ENABLE
    mod_dcctemplate_list:
    - DCCTMPLTNAME: 'dcc-test'
      CCFH: CONTINUE
      CCFHOFFLINE: ENABLE
      FAILOVERSUP: ENABLE
    add_dcctemplate_list_1:
    - DCCTMPLTNAME: 'dcc-test'
      CCFH: CONTINUE
      CCFHOFFLINE: ENABLE
      FAILOVERSUP: ENABLE
    mod_dcctemplate_list_1:
    - DCCTMPLTNAME: 'dcc-test'
      CCFH: CONTINUE
      CCFHOFFLINE: ENABLE
      FAILOVERSUP: ENABLE
    add_dcctemplate_list_2:
    - DCCTMPLTNAME: 'dcc-test'
      CCFH: CONTINUE
      CCFHOFFLINE: ENABLE
      FAILOVERSUP: ENABLE
    mod_dcctemplate_list_2:
    - DCCTMPLTNAME: 'dcc-test'
      CCFH: CONTINUE
      CCFHOFFLINE: ENABLE
      FAILOVERSUP: ENABLE
    add_dcctemplate_list_3:
    - DCCTMPLTNAME: 'dcc-test'
      CCFH: CONTINUE
      CCFHOFFLINE: ENABLE
      FAILOVERSUP: ENABLE
    mod_dcctemplate_list_3:
    - DCCTMPLTNAME: 'dcc-test'
      CCFH: CONTINUE
      CCFHOFFLINE: ENABLE
      FAILOVERSUP: ENABLE
    set_txtimer_list:
    - DCCTMPLTNAME: 'dcc-test'
      TXTIMERFLAG: TXTIMER_VALUE
      TXTIMER: 3
      RETRYTIMEOUT: ''
      RETRYTIMES: ''
    set_ofccdrpara_list:
    - PSFCIFORMAT: HEX
      CCFHCDRSW: DISABLE
      CCFHCDRCC: '0xFFFF'
      R6EGCDRCCFHSW: DISABLE
    set_holdingtime_list:
    - DCCTMPLTNAME: 'dcc-test'
      HOLDINGTIME: 30
      RANGETIME: 10
    set_holdingtime_list_1:
    - DCCTMPLTNAME: 'dcc-test'
      HOLDINGTIME: 30
      RANGETIME: 10
    set_ocsdownaction_list:
    - DCCTMPLTNAME: 'dcc-test'
      OCSDNACTION: PERMIT
      HOLDINGTMFLAG: ENABLE
    add_cmdrcact_list:
    - DCCTMPLTNAME: 'dcc-test'
      CMDRC: '4012'
      CMDRCACT: TERM_WITH_CCRT
      CCAHOLDTIME: DISABLE
      CMDLEVREACTREQ: DISABLE
      CMDRCGTPV01: ''
      CMDRCGTPV2: ''
      CMDRDVIRTIP: ''
      CMDRDVIRTIPV6: ''
    set_cmdlevdftbeh_list:
    - DCCTMPLTNAME: 'dcc-test'
      CMDLEVDFTBEH: TERM_WITH_CCRT
      CCAHOLDTIME: ''
      CMDDFTGTPV01: ''
      CMDDFTGTPV2: ''
      CMDDFTRDIPV4: ''
      CMDDFTRDIPV6: ''
      CMDLEVREACTREQ: ''
    add_msccrcact_list:
    - DCCTMPLTNAME: 'dcc-test'
      MSCCRC: '4012'
      MSCCRCACT: BLOCK
      MSCCBLKTIMER: ''
      MSCCRDVIRTIP: ''
      MSCCRDVIRTIPV6: ''
      MSCCREACTREQ: DISABLE
    set_mscclevdftbeh_list:
    - DCCTMPLTNAME: 'dcc-test'
      MSCCLEVDFTBEH: BLOCK
      MSCCDFTBLKTM: ''
      MSCCDFTRDIPV4: ''
      MSCCDFTRDIPV6: ''
      MSCCREACTREQ: ''
    add_dcctemplate_list_4:
    - DCCTMPLTNAME: 'dcc-test'
      CCFH: CONTINUE
      CCFHOFFLINE: ENABLE
      FAILOVERSUP: ENABLE
    mod_dcctemplate_list_4:
    - DCCTMPLTNAME: 'dcc-test'
      CCFH: CONTINUE
      CCFHOFFLINE: ENABLE
      FAILOVERSUP: ENABLE
    set_tctimer_list:
    - TCTIMERLEN: 1
      TCMODE: MULTIPLY
    set_twtimer_list:
    - TWTIMERLEN: 30
      TWNORESPTIMES: 3
      TWRSTTCP: DISABLE
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 配置用户激活后OCS故障的处理动作。

#### 1.1 配置Tx定时器超时以后的处理方式。

```jinja2
{%- for item in add_dcctemplate_list -%}
    ADD DCCTEMPLATE:
    {#- --- 必选参数 --- -#}
    DCCTMPLTNAME="{{item.DCCTMPLTNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.CCFH is not none -%}
        CCFH={{item.CCFH}},
    {%- endif -%}
    {%- if item.CCFHOFFLINE is not none -%}
        CCFHOFFLINE={{item.CCFHOFFLINE}},
    {%- endif -%}
    {%- if item.FAILOVERSUP is not none -%}
        FAILOVERSUP={{item.FAILOVERSUP}},
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in mod_dcctemplate_list -%}
    MOD DCCTEMPLATE:
    {#- --- 必选参数 --- -#}
    DCCTMPLTNAME="{{item.DCCTMPLTNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.CCFH is not none -%}
        CCFH={{item.CCFH}},
    {%- endif -%}
    {%- if item.CCFHOFFLINE is not none -%}
        CCFHOFFLINE={{item.CCFHOFFLINE}},
    {%- endif -%}
    {%- if item.FAILOVERSUP is not none -%}
        FAILOVERSUP={{item.FAILOVERSUP}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 参数“CCFH”用于non-IEC计费 模式下在线计费Tx定时器超时后的动作处理。

#### Tx定时器超时后有三种动作处理方式：

##### 1.1.1 “TERMINATE”：表示去激活用户。

##### 1.1.2 “RETRY\_AND\_TERM”：表示UNC会向备OCS重发一次请求消息，如果能收到响应，则与备OCS交互；如果Tx定时器超时仍然未得到响应，则去激活用户。选择该种方式时，需要一方面部署主备OCS，一方面主OCS组支持failover，即在CCA消息中CC-Session-Failover AVP支持failover，另一方面还需要在UNC本地配置支持failover功能，即配置了步骤 2，该动作才能生效。

##### 1.1.3 “CONTINUE”：表示UNC会向备OCS重发一次请求消息，如果能收到响应，则与备OCS交互；如果Tx定时器超时仍然未得到响应，则转离线计费，继续进行业务。选择该种方式时，同上需要一方面部署主备OCS组，一方面主OCS组支持failover，即在CCA消息中CC-Session-Failover AVP支持failover，另一方面还需要在UNC本地配置支持failover功能，即配置步骤 2，步骤 7，该动作才能生效。

#### 1.2 配置在线计费是否支持failover，配置“FAILOVERSUP”参数为“ENABLE”。当Tx定时器超时后的处理方式为“RETRY\_AND\_TERM”或者“CONTINUE”时，需要配置该步骤。

```jinja2
{%- set MOD_DCCTEMPLATE=getParameterValue('MOD DCCTEMPLATE') -%}
{%- if MOD_DCCTEMPLATE -%}
    {%- for item in add_dcctemplate_list_1 -%}
        ADD DCCTEMPLATE:
        {#- --- 必选参数 --- -#}
        DCCTMPLTNAME="{{item.DCCTMPLTNAME}}",
        {#- --- 可选参数 --- -#}
        {%- if item.CCFH is not none -%}
            CCFH={{item.CCFH}},
        {%- endif -%}
        {%- if item.CCFHOFFLINE is not none -%}
            CCFHOFFLINE={{item.CCFHOFFLINE}},
        {%- endif -%}
        {%- if item.FAILOVERSUP is not none -%}
            FAILOVERSUP={{item.FAILOVERSUP}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if MOD_DCCTEMPLATE -%}
    {%- for item in mod_dcctemplate_list_1 -%}
        MOD DCCTEMPLATE:
        {#- --- 必选参数 --- -#}
        DCCTMPLTNAME="{{item.DCCTMPLTNAME}}",
        {#- --- 可选参数 --- -#}
        {%- if item.CCFH is not none -%}
            CCFH={{item.CCFH}},
        {%- endif -%}
        {%- if item.CCFHOFFLINE is not none -%}
            CCFHOFFLINE={{item.CCFHOFFLINE}},
        {%- endif -%}
        {%- if item.FAILOVERSUP is not none -%}
            FAILOVERSUP={{item.FAILOVERSUP}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 1.3 **可选：**配置在线计费是否支持自动failback。

```jinja2
{%- if is_optional_auto_failback -%}
    {%- for item in add_dcctemplate_list_2 -%}
        ADD DCCTEMPLATE:
        {#- --- 必选参数 --- -#}
        DCCTMPLTNAME="{{item.DCCTMPLTNAME}}",
        {#- --- 可选参数 --- -#}
        {%- if item.CCFH is not none -%}
            CCFH={{item.CCFH}},
        {%- endif -%}
        {%- if item.CCFHOFFLINE is not none -%}
            CCFHOFFLINE={{item.CCFHOFFLINE}},
        {%- endif -%}
        {%- if item.FAILOVERSUP is not none -%}
            FAILOVERSUP={{item.FAILOVERSUP}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_optional_auto_failback -%}
    {%- for item in mod_dcctemplate_list_2 -%}
        MOD DCCTEMPLATE:
        {#- --- 必选参数 --- -#}
        DCCTMPLTNAME="{{item.DCCTMPLTNAME}}",
        {#- --- 可选参数 --- -#}
        {%- if item.CCFH is not none -%}
            CCFH={{item.CCFH}},
        {%- endif -%}
        {%- if item.CCFHOFFLINE is not none -%}
            CCFHOFFLINE={{item.CCFHOFFLINE}},
        {%- endif -%}
        {%- if item.FAILOVERSUP is not none -%}
            FAILOVERSUP={{item.FAILOVERSUP}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### “FAILOVERSUP”和“AUTOFAILBACK”是协议定义的两种OCS故障容错方式，“FAILOVERSUP”是指在主OCS故障的情况下，UNC会发送DCC消息给备OCS服务器组进行处理。“AUTOFAILBACK”是指当主OCS链路故障恢复后，DCC业务切换回到主OCS服务器上。

#### 1.4 配置在线计费和离线计费同时使能的用户进行在线计费时，发生CCFH之后是否在离线话单中添加ccfh标志位。

```jinja2
{%- for item in add_dcctemplate_list_3 -%}
    ADD DCCTEMPLATE:
    {#- --- 必选参数 --- -#}
    DCCTMPLTNAME="{{item.DCCTMPLTNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.CCFH is not none -%}
        CCFH={{item.CCFH}},
    {%- endif -%}
    {%- if item.CCFHOFFLINE is not none -%}
        CCFHOFFLINE={{item.CCFHOFFLINE}},
    {%- endif -%}
    {%- if item.FAILOVERSUP is not none -%}
        FAILOVERSUP={{item.FAILOVERSUP}},
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in mod_dcctemplate_list_3 -%}
    MOD DCCTEMPLATE:
    {#- --- 必选参数 --- -#}
    DCCTMPLTNAME="{{item.DCCTMPLTNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.CCFH is not none -%}
        CCFH={{item.CCFH}},
    {%- endif -%}
    {%- if item.CCFHOFFLINE is not none -%}
        CCFHOFFLINE={{item.CCFHOFFLINE}},
    {%- endif -%}
    {%- if item.FAILOVERSUP is not none -%}
        FAILOVERSUP={{item.FAILOVERSUP}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 本命令只针对在线计费用户生效，且根据用户归属属性配置的离线计费开关**SET CHARGECTRL**必须使能。

#### 1.5 配置Tx定时器的时长。

```jinja2
{%- for item in set_txtimer_list -%}
    SET TXTIMER:
    {#- --- 必选参数 --- -#}
    DCCTMPLTNAME="{{item.DCCTMPLTNAME}}",
    TXTIMERFLAG={{item.TXTIMERFLAG}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：TXTIMERFLAG=TXTIMER_VALUE 时必选 --- -#}
    {%- if item.TXTIMERFLAG == 'TXTIMER_VALUE' -%}
        TXTIMER={{item.TXTIMER}},
    {%- endif -%}
    {#- --- 条件必选：TXTIMERFLAG=APP_RETRANSMIT 时必选 --- -#}
    {%- if item.TXTIMERFLAG == 'APP_RETRANSMIT' -%}
        RETRYTIMEOUT={{item.RETRYTIMEOUT}},
    {%- endif -%}
    {#- --- 条件必选：TXTIMERFLAG=APP_RETRANSMIT 时必选 --- -#}
    {%- if item.TXTIMERFLAG == 'APP_RETRANSMIT' -%}
        RETRYTIMES={{item.RETRYTIMES}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 1.6 配置在线计费CCFH处理时是否强制产生话单，强制产生话单时话单中charging characteristics字段的取值；配置R6版本的eG-CDR是否支持CCFH处理。

```jinja2
{%- for item in set_ofccdrpara_list -%}
    SET OFCCDRPARA:
    {#- --- 可选参数 --- -#}
    {%- if item.PSFCIFORMAT is not none -%}
        PSFCIFORMAT={{item.PSFCIFORMAT}},
    {%- endif -%}
    {%- if item.CCFHCDRSW is not none -%}
        CCFHCDRSW={{item.CCFHCDRSW}},
    {%- endif -%}
    {%- if item.R6EGCDRCCFHSW is not none -%}
        R6EGCDRCCFHSW={{item.R6EGCDRCCFHSW}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：CCFHCDRSW=ENABLE 时可选 --- -#}
    {%- if item.CCFHCDRSW == 'ENABLE' -%}
        {%- if item.CCFHCDRCC is not none -%}
            CCFHCDRCC="{{item.CCFHCDRCC}}",
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 1.7 配置业务持续时长。

```jinja2
{%- for item in set_holdingtime_list -%}
    SET HOLDINGTIME:
    {#- --- 必选参数 --- -#}
    DCCTMPLTNAME="{{item.DCCTMPLTNAME}}",
    HOLDINGTIME={{item.HOLDINGTIME}},
    {#- --- 可选参数 --- -#}
    {%- if item.RANGETIME is not none -%}
        RANGETIME={{item.RANGETIME}},
    {%- endif -%}
    ;
{%- endfor -%}
```

##### 1.7.1 使用命令**SET DEACTIVERATE**可以去激活在线计费转为离线计费且Holding Time定时器值为0的用户。

##### 1.7.2 当Tx定时器超时后的处理方式为“CONTINUE”时，允许用户保持业务的时长，超出该时长则去激活用户。当配置为0分钟表示允许用户永久保持在线进行业务。

### 2 配置用户激活时OCS故障的处理动作。

#### 2.1 **可选：**配置转离线后业务持续时长。

```jinja2
{%- set SET_OCSDOWNACTION=getParameterValue('SET OCSDOWNACTION') -%}
{%- if is_optional_offline_holdtime and SET_OCSDOWNACTION -%}
    {%- for item in set_holdingtime_list_1 -%}
        SET HOLDINGTIME:
        {#- --- 必选参数 --- -#}
        DCCTMPLTNAME="{{item.DCCTMPLTNAME}}",
        HOLDINGTIME={{item.HOLDINGTIME}},
        {#- --- 可选参数 --- -#}
        {%- if item.RANGETIME is not none -%}
            RANGETIME={{item.RANGETIME}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 当**SET OCSDOWNACTION**命令**OCSDNACTION**参数值为“PERMIT”并且“HOLDINGTMFLAG”参数值为“ENABLE”时，需要首先配置**HOLDINGTIME**。

#### 2.2 配置OCS故障时是否允许用户激活。

```jinja2
{%- for item in set_ocsdownaction_list -%}
    SET OCSDOWNACTION:
    {#- --- 必选参数 --- -#}
    DCCTMPLTNAME="{{item.DCCTMPLTNAME}}",
    OCSDNACTION={{item.OCSDNACTION}},
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：OCSDNACTION=PERMIT 时可选 --- -#}
    {%- if item.OCSDNACTION == 'PERMIT' -%}
        {%- if item.HOLDINGTMFLAG is not none -%}
            HOLDINGTMFLAG={{item.HOLDINGTMFLAG}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 配置command层消息码为异常返回码时的处理动作。

#### 3.1 配置command层消息码为异常返回码时的处理动作。

```jinja2
{%- for item in add_cmdrcact_list -%}
    ADD CMDRCACT:
    {#- --- 必选参数 --- -#}
    DCCTMPLTNAME="{{item.DCCTMPLTNAME}}",
    CMDRC="{{item.CMDRC}}",
    CMDRCACT={{item.CMDRCACT}},
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：CMDRCACT=CONTINUE 时可选 --- -#}
    {%- if item.CMDRCACT == 'CONTINUE' -%}
        {%- if item.CCAHOLDTIME is not none -%}
            CCAHOLDTIME={{item.CCAHOLDTIME}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：CMDRCACT=TERM_NO_CCRT/TERM_WITH_CCRT 时可选 --- -#}
    {%- if item.CMDRCACT in ['TERM_NO_CCRT', 'TERM_WITH_CCRT'] -%}
        {%- if item.CMDLEVREACTREQ is not none -%}
            CMDLEVREACTREQ={{item.CMDLEVREACTREQ}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：CMDRCACT=TERM_NO_CCRT/TERM_WITH_CCRT 时可选 --- -#}
    {%- if item.CMDRCACT in ['TERM_NO_CCRT', 'TERM_WITH_CCRT'] -%}
        {%- if item.CMDRCGTPV01 is not none -%}
            CMDRCGTPV01={{item.CMDRCGTPV01}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：CMDRCACT=TERM_NO_CCRT/TERM_WITH_CCRT 时可选 --- -#}
    {%- if item.CMDRCACT in ['TERM_NO_CCRT', 'TERM_WITH_CCRT'] -%}
        {%- if item.CMDRCGTPV2 is not none -%}
            CMDRCGTPV2={{item.CMDRCGTPV2}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：CMDRCACT=REDIRECT 时可选 --- -#}
    {%- if item.CMDRCACT == 'REDIRECT' -%}
        {%- if item.CMDRDVIRTIP is not none -%}
            CMDRDVIRTIP="{{item.CMDRDVIRTIP}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：CMDRCACT=REDIRECT 时可选 --- -#}
    {%- if item.CMDRCACT == 'REDIRECT' -%}
        {%- if item.CMDRDVIRTIPV6 is not none -%}
            CMDRDVIRTIPV6="{{item.CMDRDVIRTIPV6}}",
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

##### 3.1.1 返回码DIAMETER\_SUCCESS (2001)，DIAMETER\_LIMITED\_SUCCESS (2002)的动作不可配置，属于正常返回码，业务动作取决于MSCC层的返回码动作控制。

##### 3.1.2 当在线计费用户本地配置用户转离线时，UNC支持开启Holding Time定时器，Holding Time定时器超时之后再进行用户去活。

##### 3.1.3 如果某返回码没有单独配置对应的动作，则采用步骤 2的**SET CMDLEVDFTBEH**配置的动作进行处理。

##### 3.1.4 部分协议规定了标准处理的特殊返回码缺省值为固定处理，如果这部分返回码对应的动作没有配置，缺省值为特殊的处理流程，不会采用**SET CMDLEVDFTBEH**配置的动作；如果配置了返回码对应的动作，则按照配置的动作处理。这部分返回码及缺省动作处理请参见命令帮助的说明。

#### 3.2 配置command层消息码为异常返回码时的默认处理动作。

```jinja2
{%- for item in set_cmdlevdftbeh_list -%}
    SET CMDLEVDFTBEH:
    {#- --- 必选参数 --- -#}
    DCCTMPLTNAME="{{item.DCCTMPLTNAME}}",
    CMDLEVDFTBEH={{item.CMDLEVDFTBEH}},
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：CMDLEVDFTBEH=CONTINUE 时可选 --- -#}
    {%- if item.CMDLEVDFTBEH == 'CONTINUE' -%}
        {%- if item.CCAHOLDTIME is not none -%}
            CCAHOLDTIME={{item.CCAHOLDTIME}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：CMDLEVDFTBEH=TERM_NO_CCRT/TERM_WITH_CCRT 时可选 --- -#}
    {%- if item.CMDLEVDFTBEH in ['TERM_NO_CCRT', 'TERM_WITH_CCRT'] -%}
        {%- if item.CMDDFTGTPV01 is not none -%}
            CMDDFTGTPV01={{item.CMDDFTGTPV01}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：CMDLEVDFTBEH=TERM_NO_CCRT/TERM_WITH_CCRT 时可选 --- -#}
    {%- if item.CMDLEVDFTBEH in ['TERM_NO_CCRT', 'TERM_WITH_CCRT'] -%}
        {%- if item.CMDDFTGTPV2 is not none -%}
            CMDDFTGTPV2={{item.CMDDFTGTPV2}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：CMDLEVDFTBEH=REDIRECT 时可选 --- -#}
    {%- if item.CMDLEVDFTBEH == 'REDIRECT' -%}
        {%- if item.CMDDFTRDIPV4 is not none -%}
            CMDDFTRDIPV4="{{item.CMDDFTRDIPV4}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：CMDLEVDFTBEH=REDIRECT 时可选 --- -#}
    {%- if item.CMDLEVDFTBEH == 'REDIRECT' -%}
        {%- if item.CMDDFTRDIPV6 is not none -%}
            CMDDFTRDIPV6="{{item.CMDDFTRDIPV6}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：CMDLEVDFTBEH=TERM_NO_CCRT/TERM_WITH_CCRT 时可选 --- -#}
    {%- if item.CMDLEVDFTBEH in ['TERM_NO_CCRT', 'TERM_WITH_CCRT'] -%}
        {%- if item.CMDLEVREACTREQ is not none -%}
            CMDLEVREACTREQ={{item.CMDLEVREACTREQ}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 配置MSCC层消息码为异常返回码时的处理动作。

#### 4.1 配置MSCC层消息码为异常返回码时的处理动作。

```jinja2
{%- for item in add_msccrcact_list -%}
    ADD MSCCRCACT:
    {#- --- 必选参数 --- -#}
    DCCTMPLTNAME="{{item.DCCTMPLTNAME}}",
    MSCCRC="{{item.MSCCRC}}",
    MSCCRCACT={{item.MSCCRCACT}},
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：MSCCRCACT=BLCK_IMMED_RPT/BLCK_NO_RPT 时可选 --- -#}
    {%- if item.MSCCRCACT in ['BLCK_IMMED_RPT', 'BLCK_NO_RPT'] -%}
        {%- if item.MSCCBLKTIMER is not none -%}
            MSCCBLKTIMER={{item.MSCCBLKTIMER}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：MSCCRCACT=REDIRECT 时可选 --- -#}
    {%- if item.MSCCRCACT == 'REDIRECT' -%}
        {%- if item.MSCCRDVIRTIP is not none -%}
            MSCCRDVIRTIP="{{item.MSCCRDVIRTIP}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：MSCCRCACT=REDIRECT 时可选 --- -#}
    {%- if item.MSCCRCACT == 'REDIRECT' -%}
        {%- if item.MSCCRDVIRTIPV6 is not none -%}
            MSCCRDVIRTIPV6="{{item.MSCCRDVIRTIPV6}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：MSCCRCACT=TERMINATE 时可选 --- -#}
    {%- if item.MSCCRCACT == 'TERMINATE' -%}
        {%- if item.MSCCREACTREQ is not none -%}
            MSCCREACTREQ={{item.MSCCREACTREQ}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

##### 4.1.1 返回码DIAMETER\_SUCCESS (2001)，DIAMETER\_LIMITED\_SUCCESS (2002)的动作不可配置，属于正常返回码，正常转发报文并计费。

##### 4.1.2 如果某返回码没有单独配置对应的动作，则采用步骤 2的**SET MSCCLEVDFTBEH**配置的动作进行处理。

##### 4.1.3 部分协议规定了标准处理的特殊返回码缺省值为固定处理，如果这部分返回码对应的动作没有配置，缺省值为特殊的处理流程，不会采用**SET MSCCLEVDFTBEH**配置的动作；如果配置了返回码对应的动作，则按照配置的动作处理。这部分返回码及缺省动作处理请参见命令帮助的说明。

#### 4.2 配置MSCC层消息码为异常返回码时的默认处理动作。

```jinja2
{%- for item in set_mscclevdftbeh_list -%}
    SET MSCCLEVDFTBEH:
    {#- --- 必选参数 --- -#}
    DCCTMPLTNAME="{{item.DCCTMPLTNAME}}",
    MSCCLEVDFTBEH={{item.MSCCLEVDFTBEH}},
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：MSCCLEVDFTBEH=BLCK_IMMED_RPT/BLCK_NO_RPT 时可选 --- -#}
    {%- if item.MSCCLEVDFTBEH in ['BLCK_IMMED_RPT', 'BLCK_NO_RPT'] -%}
        {%- if item.MSCCDFTBLKTM is not none -%}
            MSCCDFTBLKTM={{item.MSCCDFTBLKTM}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：MSCCLEVDFTBEH=REDIRECT 时可选 --- -#}
    {%- if item.MSCCLEVDFTBEH == 'REDIRECT' -%}
        {%- if item.MSCCDFTRDIPV4 is not none -%}
            MSCCDFTRDIPV4="{{item.MSCCDFTRDIPV4}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：MSCCLEVDFTBEH=REDIRECT 时可选 --- -#}
    {%- if item.MSCCLEVDFTBEH == 'REDIRECT' -%}
        {%- if item.MSCCDFTRDIPV6 is not none -%}
            MSCCDFTRDIPV6="{{item.MSCCDFTRDIPV6}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：MSCCLEVDFTBEH=TERMINATE 时可选 --- -#}
    {%- if item.MSCCLEVDFTBEH == 'TERMINATE' -%}
        {%- if item.MSCCREACTREQ is not none -%}
            MSCCREACTREQ={{item.MSCCREACTREQ}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### UNC支持针对OCS返回的特殊返回码设置动作，包括重定向动作。当UNC收到这些特殊返回码时，会根据配置的动作进行重定向处理。重定向处理动作可以由OCS下发，也可以在UNC本地配置。其优先级关系是：

##### 4.2.1 OCS下发的动作优先级最高。

##### 4.2.2 其次是在UNC本地为Command层特殊返回码配置的动作**ADD CMDRCACT**。

##### 4.2.3 再者是在UNC本地为MSCC层特殊返回码配置的动作**ADD MSCCRCACT**。

##### 4.2.4 然后是UNC本地默认的Command层特殊返回码处理动作**SET CMDLEVDFTBEH**。

##### 4.2.5 优先级最低的是UNC本地默认的MSCC层特殊返回码处理动作**SET MSCCLEVDFTBEH**。

### 5 配置UNC收到OCS的CCA消息中携带FUI Terminate时的处理动作，配置“FUATERMINATE”参数。

```jinja2
{%- for item in add_dcctemplate_list_4 -%}
    ADD DCCTEMPLATE:
    {#- --- 必选参数 --- -#}
    DCCTMPLTNAME="{{item.DCCTMPLTNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.CCFH is not none -%}
        CCFH={{item.CCFH}},
    {%- endif -%}
    {%- if item.CCFHOFFLINE is not none -%}
        CCFHOFFLINE={{item.CCFHOFFLINE}},
    {%- endif -%}
    {%- if item.FAILOVERSUP is not none -%}
        FAILOVERSUP={{item.FAILOVERSUP}},
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in mod_dcctemplate_list_4 -%}
    MOD DCCTEMPLATE:
    {#- --- 必选参数 --- -#}
    DCCTMPLTNAME="{{item.DCCTMPLTNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.CCFH is not none -%}
        CCFH={{item.CCFH}},
    {%- endif -%}
    {%- if item.CCFHOFFLINE is not none -%}
        CCFHOFFLINE={{item.CCFHOFFLINE}},
    {%- endif -%}
    {%- if item.FAILOVERSUP is not none -%}
        FAILOVERSUP={{item.FAILOVERSUP}},
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in set_tctimer_list -%}
    SET TCTIMER:
    {#- --- 必选参数 --- -#}
    TCTIMERLEN={{item.TCTIMERLEN}},
    {#- --- 可选参数 --- -#}
    {%- if item.TCMODE is not none -%}
        TCMODE={{item.TCMODE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in set_twtimer_list -%}
    SET TWTIMER:
    {#- --- 必选参数 --- -#}
    TWTIMERLEN={{item.TWTIMERLEN}},
    {#- --- 可选参数 --- -#}
    {%- if item.TWNORESPTIMES is not none -%}
        TWNORESPTIMES={{item.TWNORESPTIMES}},
    {%- endif -%}
    {%- if item.TWRSTTCP is not none -%}
        TWRSTTCP={{item.TWRSTTCP}},
    {%- endif -%}
    ;
{%- endfor -%}
```


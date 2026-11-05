---
id: ''
name: 配置DCC处理动作
ne_type: UDG
type: feature
description: 本指导描述UNC对于OCS故障或者OCS的响应消息携带的特定结果码配置相就的处理动作的配置过程。  在线计费会话过程中，对于各种正常和异常场景，可以在UNC本地设置一些处理动作对DCC流程进行干预。这里的正常和异常场景，主要是指OCS响应UNC请求消息的状况，及响应消息的返回码值。
risk_level: ''
doc_source: ["特性部署","业务专题","5G Core 计费解决方案","计费解决方案概述","计费方案部署与调测","方案二：部署NCG且基于传统Ga/Gy接口计费组网方案","SMF配置","在线计费配置","在线计费模板及交互配置","配置在线计费模板","配置DCC处理动作"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
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
      properties: {}
    mod_dcctemplate_list:
      type: items
      properties:
        DCCTMPLTNAME:
          name: 'DCC模板名称'
          type: string
          required: false
          description: '使用的DCC模板名称。  说明：  如果需要配置在线计费全局参数，则需要使用**MOD DCCTEMPLATE**命令，“DCCTMPLTNAME”参数值为“global”。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        CCFH:
          name: 'CCFH处理动作'
          type: string
          required: false
          description: '配置Tx定时器超时，以及OCS返回的错误码动作为failover时的处理方式。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        CCFHOFFLINE:
          name: 'CCFH离线标志位使能开关'
          type: string
          required: false
          description: '配置发生CCFH之后是否在离线话单中添加CCFH标志位。该参数开启，CCFH之后会使非离线计费用户离线计费能力强制设置为使能。'
          data_source: ''
          pattern: ''
          default: ''
        FAILOVERSUP:
          name: '支持failover使能开关'
          type: string
          required: false
          description: '配置是否支持failover功能使能。'
          data_source: ''
          pattern: ''
          default: ''
    add_dcctemplate_list_1:
      type: items
      properties: {}
    mod_dcctemplate_list_1:
      type: items
      properties:
        DCCTMPLTNAME:
          name: 'DCC模板名称'
          type: string
          required: false
          description: '使用的DCC模板名称。  说明：  如果需要配置在线计费全局参数，则需要使用**MOD DCCTEMPLATE**命令，“DCCTMPLTNAME”参数值为“global”。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        CCFH:
          name: 'CCFH处理动作'
          type: string
          required: false
          description: '配置Tx定时器超时，以及OCS返回的错误码动作为failover时的处理方式。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        CCFHOFFLINE:
          name: 'CCFH离线标志位使能开关'
          type: string
          required: false
          description: '配置发生CCFH之后是否在离线话单中添加CCFH标志位。该参数开启，CCFH之后会使非离线计费用户离线计费能力强制设置为使能。'
          data_source: ''
          pattern: ''
          default: ''
        FAILOVERSUP:
          name: '支持failover使能开关'
          type: string
          required: false
          description: '配置是否支持failover功能使能。'
          data_source: ''
          pattern: ''
          default: ''
    add_dcctemplate_list_2:
      type: items
      properties: {}
    mod_dcctemplate_list_2:
      type: items
      properties:
        DCCTMPLTNAME:
          name: 'DCC模板名称'
          type: string
          required: false
          description: '使用的DCC模板名称。  说明：  如果需要配置在线计费全局参数，则需要使用**MOD DCCTEMPLATE**命令，“DCCTMPLTNAME”参数值为“global”。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        CCFH:
          name: 'CCFH处理动作'
          type: string
          required: false
          description: '配置Tx定时器超时，以及OCS返回的错误码动作为failover时的处理方式。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        CCFHOFFLINE:
          name: 'CCFH离线标志位使能开关'
          type: string
          required: false
          description: '配置发生CCFH之后是否在离线话单中添加CCFH标志位。该参数开启，CCFH之后会使非离线计费用户离线计费能力强制设置为使能。'
          data_source: ''
          pattern: ''
          default: ''
        FAILOVERSUP:
          name: '支持failover使能开关'
          type: string
          required: false
          description: '配置是否支持failover功能使能。'
          data_source: ''
          pattern: ''
          default: ''
    add_dcctemplate_list_3:
      type: items
      properties: {}
    mod_dcctemplate_list_3:
      type: items
      properties:
        DCCTMPLTNAME:
          name: 'DCC模板名称'
          type: string
          required: false
          description: '使用的DCC模板名称。  说明：  如果需要配置在线计费全局参数，则需要使用**MOD DCCTEMPLATE**命令，“DCCTMPLTNAME”参数值为“global”。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        CCFH:
          name: 'CCFH处理动作'
          type: string
          required: false
          description: '配置Tx定时器超时，以及OCS返回的错误码动作为failover时的处理方式。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        CCFHOFFLINE:
          name: 'CCFH离线标志位使能开关'
          type: string
          required: false
          description: '配置发生CCFH之后是否在离线话单中添加CCFH标志位。该参数开启，CCFH之后会使非离线计费用户离线计费能力强制设置为使能。'
          data_source: ''
          pattern: ''
          default: ''
        FAILOVERSUP:
          name: '支持failover使能开关'
          type: string
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
          required: false
          description: '配置Tx定时器时长。 说明：  * 如果需要配置在线计费全局参数，则“DCCTMPLTNAME”参数值为“global”。 * Tx定时器超时时长配置较大，可能激活响应的总时长过长，用户激活失败。建议：   + “TXTIMER”小于GGSN-C/PGW-C产品**ADD GTPCT3N3**命令配置的T3\*N3时长及SGSN/MME/SGW-C的T3\*N3时长。   + “TXTIMER”小于产品**SET SMCOMMTIMER**命令配置的“TCHARGING”的时长。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        TXTIMERFLAG:
          name: 'Tx定时器配置模式'
          type: string
          required: false
          description: ''
          data_source: '整网规划'
          pattern: ''
          default: ''
        TXTIMER:
          name: 'Tx定时器时长（秒）'
          type: string
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
          required: false
          description: '配置OCS故障导致用户离线后产生的话单pSFurnishChargingInformation中pSFreeFormatData字段的格式。'
          data_source: '与对端协商'
          pattern: ''
          default: ''
        CCFHCDRSW:
          name: 'CCFH强制产生话单开关'
          type: string
          required: false
          description: '配置CCFH（Credit Control Failure Handling）是否强制产生话单。'
          data_source: ''
          pattern: ''
          default: ''
        CCFHCDRCC:
          name: 'CCFH强制产生话单填充的Charging Characteristics值'
          type: string
          required: false
          description: '配置CCFH强制产生话单填充的Charging Characteristics的值。'
          data_source: ''
          pattern: ''
          default: ''
        R6EGCDRCCFHSW:
          name: 'R6 eGCRD支持CCFH强制生成话单'
          type: string
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
          required: false
          description: '配置在线计费用户转离线计费后，可以继续使用业务的时长，超出该时长后，用户会被去激活。  说明：  * 如果需要配置在线计费全局参数，则“DCCTMPLTNAME”参数值为“global”。 * “RANGETIME”是在“HOLDINGTIME”基础上增加的一个随机调整范围。每个转离线的用户都会被增加一个“RANGETIME”范围内的随机值作为补充时长。 * 建议配置该时长，使批量转离线的用户可以离散的被去激活，从而也可以离散的再次激活，以避免集中去激活后再集中激活，对周边网元造成信令冲击。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        HOLDINGTIME:
          name: '用户保持时长（分）'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        RANGETIME:
          name: '用户保持调整时长（分）'
          type: string
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
          required: false
          description: '配置在线计费用户转离线计费后，可以继续使用业务的时长，超出该时长后，用户会被去激活。  说明：  * 如果需要配置在线计费全局参数，则“DCCTMPLTNAME”参数值为“global”。 * “RANGETIME”是在“HOLDINGTIME”基础上增加的一个随机调整范围。每个转离线的用户都会被增加一个“RANGETIME”范围内的随机值作为补充时长。 * 建议配置该时长，使批量转离线的用户可以离散的被去激活，从而也可以离散的再次激活，以避免集中去激活后再集中激活，对周边网元造成信令冲击。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        HOLDINGTIME:
          name: '用户保持时长（分）'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        RANGETIME:
          name: '用户保持调整时长（分）'
          type: string
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
          required: false
          description: '使用的DCC模板名称。  说明：  如果需要配置在线计费全局参数，则“DCCTMPLTNAME”参数值为“global”。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        OCSDNACTION:
          name: 'OCS断用户处理动作'
          type: string
          required: false
          description: '配置用户激活流程中，由于OCS状态异常或者Gy链路异常导致无可用OCS时UNC的处理动作。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        HOLDINGTMFLAG:
          name: 'OCS断用户允许在线时间控制开关'
          type: string
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
          required: false
          description: 'CCA消息中命令层返回异常消息码的处理动作。  说明：  如果需要配置在线计费全局参数，则“DCCTMPLTNAME”参数值为“global”。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        CMDRC:
          name: '命令层异常返回码'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        CMDRCACT:
          name: '命令层异常返回码处理动作'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_cmdlevdftbeh_list:
      type: items
      properties:
        DCCTMPLTNAME:
          name: 'DCC模板名称'
          type: string
          required: false
          description: 'CCA消息中命令层返回异常消息码的默认处理动作。  说明：  如果需要配置在线计费全局参数，则“DCCTMPLTNAME”参数值为“global”。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        CMDLEVDFTBEH:
          name: '命令层缺省异常返回码处理动作配置'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_msccrcact_list:
      type: items
      properties:
        DCCTMPLTNAME:
          name: '在线计费模板名称'
          type: string
          required: false
          description: 'CCA消息中MSCC层返回异常消息码的处理动作。  说明：  如果需要配置在线计费全局参数，则“DCCTMPLTNAME”参数值为“global”。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        MSCCRC:
          name: 'MSCC层异常返回码'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        MSCCRCACT:
          name: 'MSCC层异常返回码动作'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_mscclevdftbeh_list:
      type: items
      properties:
        DCCTMPLTNAME:
          name: 'DCC模板名称'
          type: string
          required: false
          description: 'CCA消息中MSCC层返回异常消息码的默认处理动作。  说明：  如果需要配置在线计费全局参数，则“DCCTMPLTNAME”参数值为“global”。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        MSCCLEVDFTBEH:
          name: 'MSCC层缺省处理动作'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_dcctemplate_list_4:
      type: items
      properties: {}
    mod_dcctemplate_list_4:
      type: items
      properties:
        DCCTMPLTNAME:
          name: 'DCC模板名称'
          type: string
          required: false
          description: '使用的DCC模板名称。  说明：  如果需要配置在线计费全局参数，则需要使用**MOD DCCTEMPLATE**命令，“DCCTMPLTNAME”参数值为“global”。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        CCFH:
          name: 'CCFH处理动作'
          type: string
          required: false
          description: '配置Tx定时器超时，以及OCS返回的错误码动作为failover时的处理方式。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        CCFHOFFLINE:
          name: 'CCFH离线标志位使能开关'
          type: string
          required: false
          description: '配置发生CCFH之后是否在离线话单中添加CCFH标志位。该参数开启，CCFH之后会使非离线计费用户离线计费能力强制设置为使能。'
          data_source: ''
          pattern: ''
          default: ''
        FAILOVERSUP:
          name: '支持failover使能开关'
          type: string
          required: false
          description: '配置是否支持failover功能使能。'
          data_source: ''
          pattern: ''
          default: ''
    set_tctimer_list:
      type: items
      properties:
        TCTIMERLEN:
          name: 'TCTIMERLEN'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TCMODE:
          name: 'TCMODE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_twtimer_list:
      type: items
      properties:
        TWTIMERLEN:
          name: 'TWTIMERLEN'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TWNORESPTIMES:
          name: 'TWNORESPTIMES'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TWRSTTCP:
          name: 'TWRSTTCP'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    add_dcctemplate_list:
    - {}
    mod_dcctemplate_list:
    - DCCTMPLTNAME: dcc-test
      CCFH: CONTINUE
      CCFHOFFLINE: ENABLE
      FAILOVERSUP: ENABLE
    add_dcctemplate_list_1:
    - {}
    mod_dcctemplate_list_1:
    - DCCTMPLTNAME: dcc-test
      CCFH: CONTINUE
      CCFHOFFLINE: ENABLE
      FAILOVERSUP: ENABLE
    add_dcctemplate_list_2:
    - {}
    mod_dcctemplate_list_2:
    - DCCTMPLTNAME: dcc-test
      CCFH: CONTINUE
      CCFHOFFLINE: ENABLE
      FAILOVERSUP: ENABLE
    add_dcctemplate_list_3:
    - {}
    mod_dcctemplate_list_3:
    - DCCTMPLTNAME: dcc-test
      CCFH: CONTINUE
      CCFHOFFLINE: ENABLE
      FAILOVERSUP: ENABLE
    set_txtimer_list:
    - DCCTMPLTNAME: dcc-test
      TXTIMERFLAG: TXTIMER_VALUE
      TXTIMER: '3'
    set_ofccdrpara_list:
    - PSFCIFORMAT: HEX
      CCFHCDRSW: DISABLE
      CCFHCDRCC: '0xFFFF'
      R6EGCDRCCFHSW: DISABLE
    set_holdingtime_list:
    - DCCTMPLTNAME: dcc-test
      HOLDINGTIME: '30'
      RANGETIME: '10'
    set_holdingtime_list_1:
    - DCCTMPLTNAME: dcc-test
      HOLDINGTIME: '30'
      RANGETIME: '10'
    set_ocsdownaction_list:
    - DCCTMPLTNAME: dcc-test
      OCSDNACTION: PERMIT
      HOLDINGTMFLAG: ENABLE
    add_cmdrcact_list:
    - DCCTMPLTNAME: dcc-test
      CMDRC: '4012'
      CMDRCACT: TERM_WITH_CCRT
    set_cmdlevdftbeh_list:
    - DCCTMPLTNAME: dcc-test
      CMDLEVDFTBEH: TERM_WITH_CCRT
    add_msccrcact_list:
    - DCCTMPLTNAME: dcc-test
      MSCCRC: '4012'
      MSCCRCACT: BLOCK
    set_mscclevdftbeh_list:
    - DCCTMPLTNAME: dcc-test
      MSCCLEVDFTBEH: BLOCK
    add_dcctemplate_list_4:
    - {}
    mod_dcctemplate_list_4:
    - DCCTMPLTNAME: dcc-test
      CCFH: CONTINUE
      CCFHOFFLINE: ENABLE
      FAILOVERSUP: ENABLE
    set_tctimer_list:
    - TCTIMERLEN: '1'
      TCMODE: MULTIPLY
    set_twtimer_list:
    - TWTIMERLEN: '30'
      TWNORESPTIMES: '3'
      TWRSTTCP: DISABLE
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 配置用户激活后OCS故障的处理动作。

#### 1.1 配置Tx定时器超时以后的处理方式。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_dcctemplate_list的变量区（command: ADD DCCTEMPLATE） -#}
<!-- MISSING_MACRO: command=ADD DCCTEMPLATE list_name=add_dcctemplate_list step_id=1.1 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该mod_dcctemplate_list的变量区（command: MOD DCCTEMPLATE） -#}
<!-- MISSING_MACRO: command=MOD DCCTEMPLATE list_name=mod_dcctemplate_list step_id=1.1 -->
```

#### 参数“CCFH”用于non-IEC计费 模式下在线计费Tx定时器超时后的动作处理。

#### Tx定时器超时后有三种动作处理方式：

##### 1.1.1 “TERMINATE”：表示去激活用户。

##### 1.1.2 “RETRY\_AND\_TERM”：表示UNC会向备OCS重发一次请求消息，如果能收到响应，则与备OCS交互；如果Tx定时器超时仍然未得到响应，则去激活用户。选择该种方式时，需要一方面部署主备OCS，一方面主OCS组支持failover，即在CCA消息中CC-Session-Failover AVP支持failover，另一方面还需要在UNC本地配置支持failover功能，即配置了步骤 2，该动作才能生效。

##### 1.1.3 “CONTINUE”：表示UNC会向备OCS重发一次请求消息，如果能收到响应，则与备OCS交互；如果Tx定时器超时仍然未得到响应，则转离线计费，继续进行业务。选择该种方式时，同上需要一方面部署主备OCS组，一方面主OCS组支持failover，即在CCA消息中CC-Session-Failover AVP支持failover，另一方面还需要在UNC本地配置支持failover功能，即配置步骤 2，步骤 7，该动作才能生效。

#### 1.2 配置在线计费是否支持failover，配置“FAILOVERSUP”参数为“ENABLE”。当Tx定时器超时后的处理方式为“RETRY\_AND\_TERM”或者“CONTINUE”时，需要配置该步骤。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_dcctemplate_list_1的变量区（command: ADD DCCTEMPLATE） -#}
<!-- MISSING_MACRO: command=ADD DCCTEMPLATE list_name=add_dcctemplate_list_1 step_id=1.2 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该mod_dcctemplate_list_1的变量区（command: MOD DCCTEMPLATE） -#}
<!-- MISSING_MACRO: command=MOD DCCTEMPLATE list_name=mod_dcctemplate_list_1 step_id=1.2 -->
```

#### 1.3 **可选：**配置在线计费是否支持自动failback。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_dcctemplate_list_2的变量区（command: ADD DCCTEMPLATE） -#}
<!-- MISSING_MACRO: command=ADD DCCTEMPLATE list_name=add_dcctemplate_list_2 step_id=1.3 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该mod_dcctemplate_list_2的变量区（command: MOD DCCTEMPLATE） -#}
<!-- MISSING_MACRO: command=MOD DCCTEMPLATE list_name=mod_dcctemplate_list_2 step_id=1.3 -->
```

#### “FAILOVERSUP”和“AUTOFAILBACK”是协议定义的两种OCS故障容错方式，“FAILOVERSUP”是指在主OCS故障的情况下，UNC会发送DCC消息给备OCS服务器组进行处理。“AUTOFAILBACK”是指当主OCS链路故障恢复后，DCC业务切换回到主OCS服务器上。

#### 1.4 配置在线计费和离线计费同时使能的用户进行在线计费时，发生CCFH之后是否在离线话单中添加ccfh标志位。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_dcctemplate_list_3的变量区（command: ADD DCCTEMPLATE） -#}
<!-- MISSING_MACRO: command=ADD DCCTEMPLATE list_name=add_dcctemplate_list_3 step_id=1.4 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该mod_dcctemplate_list_3的变量区（command: MOD DCCTEMPLATE） -#}
<!-- MISSING_MACRO: command=MOD DCCTEMPLATE list_name=mod_dcctemplate_list_3 step_id=1.4 -->
```

#### 本命令只针对在线计费用户生效，且根据用户归属属性配置的离线计费开关**SET CHARGECTRL**必须使能。

#### 1.5 配置Tx定时器的时长。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_txtimer_list的变量区（command: SET TXTIMER） -#}
<!-- MISSING_MACRO: command=SET TXTIMER list_name=set_txtimer_list step_id=1.5 -->
```

#### 1.6 配置在线计费CCFH处理时是否强制产生话单，强制产生话单时话单中charging characteristics字段的取值；配置R6版本的eG-CDR是否支持CCFH处理。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_ofccdrpara_list的变量区（command: SET OFCCDRPARA） -#}
<!-- MISSING_MACRO: command=SET OFCCDRPARA list_name=set_ofccdrpara_list step_id=1.6 -->
```

#### 1.7 配置业务持续时长。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_holdingtime_list的变量区（command: SET HOLDINGTIME） -#}
<!-- MISSING_MACRO: command=SET HOLDINGTIME list_name=set_holdingtime_list step_id=1.7 -->
```

##### 1.7.1 使用命令**SET DEACTIVERATE**可以去激活在线计费转为离线计费且Holding Time定时器值为0的用户。

##### 1.7.2 当Tx定时器超时后的处理方式为“CONTINUE”时，允许用户保持业务的时长，超出该时长则去激活用户。当配置为0分钟表示允许用户永久保持在线进行业务。

### 2 配置用户激活时OCS故障的处理动作。

#### 2.1 **可选：**配置转离线后业务持续时长。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_holdingtime_list_1的变量区（command: SET HOLDINGTIME） -#}
<!-- MISSING_MACRO: command=SET HOLDINGTIME list_name=set_holdingtime_list_1 step_id=2.1 -->
```

#### 当**SET OCSDOWNACTION**命令**OCSDNACTION**参数值为“PERMIT”并且“HOLDINGTMFLAG”参数值为“ENABLE”时，需要首先配置**HOLDINGTIME**。

#### 2.2 配置OCS故障时是否允许用户激活。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_ocsdownaction_list的变量区（command: SET OCSDOWNACTION） -#}
<!-- MISSING_MACRO: command=SET OCSDOWNACTION list_name=set_ocsdownaction_list step_id=2.2 -->
```

### 3 配置command层消息码为异常返回码时的处理动作。

#### 3.1 配置command层消息码为异常返回码时的处理动作。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_cmdrcact_list的变量区（command: ADD CMDRCACT） -#}
<!-- MISSING_MACRO: command=ADD CMDRCACT list_name=add_cmdrcact_list step_id=3.1 -->
```

##### 3.1.1 返回码DIAMETER\_SUCCESS (2001)，DIAMETER\_LIMITED\_SUCCESS (2002)的动作不可配置，属于正常返回码，业务动作取决于MSCC层的返回码动作控制。

##### 3.1.2 当在线计费用户本地配置用户转离线时，UNC支持开启Holding Time定时器，Holding Time定时器超时之后再进行用户去活。

##### 3.1.3 如果某返回码没有单独配置对应的动作，则采用步骤 2的**SET CMDLEVDFTBEH**配置的动作进行处理。

##### 3.1.4 部分协议规定了标准处理的特殊返回码缺省值为固定处理，如果这部分返回码对应的动作没有配置，缺省值为特殊的处理流程，不会采用**SET CMDLEVDFTBEH**配置的动作；如果配置了返回码对应的动作，则按照配置的动作处理。这部分返回码及缺省动作处理请参见命令帮助的说明。

#### 3.2 配置command层消息码为异常返回码时的默认处理动作。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_cmdlevdftbeh_list的变量区（command: SET CMDLEVDFTBEH） -#}
<!-- MISSING_MACRO: command=SET CMDLEVDFTBEH list_name=set_cmdlevdftbeh_list step_id=3.2 -->
```

### 4 配置MSCC层消息码为异常返回码时的处理动作。

#### 4.1 配置MSCC层消息码为异常返回码时的处理动作。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_msccrcact_list的变量区（command: ADD MSCCRCACT） -#}
<!-- MISSING_MACRO: command=ADD MSCCRCACT list_name=add_msccrcact_list step_id=4.1 -->
```

##### 4.1.1 返回码DIAMETER\_SUCCESS (2001)，DIAMETER\_LIMITED\_SUCCESS (2002)的动作不可配置，属于正常返回码，正常转发报文并计费。

##### 4.1.2 如果某返回码没有单独配置对应的动作，则采用步骤 2的**SET MSCCLEVDFTBEH**配置的动作进行处理。

##### 4.1.3 部分协议规定了标准处理的特殊返回码缺省值为固定处理，如果这部分返回码对应的动作没有配置，缺省值为特殊的处理流程，不会采用**SET MSCCLEVDFTBEH**配置的动作；如果配置了返回码对应的动作，则按照配置的动作处理。这部分返回码及缺省动作处理请参见命令帮助的说明。

#### 4.2 配置MSCC层消息码为异常返回码时的默认处理动作。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_mscclevdftbeh_list的变量区（command: SET MSCCLEVDFTBEH） -#}
<!-- MISSING_MACRO: command=SET MSCCLEVDFTBEH list_name=set_mscclevdftbeh_list step_id=4.2 -->
```

#### UNC支持针对OCS返回的特殊返回码设置动作，包括重定向动作。当UNC收到这些特殊返回码时，会根据配置的动作进行重定向处理。重定向处理动作可以由OCS下发，也可以在UNC本地配置。其优先级关系是：

##### 4.2.1 OCS下发的动作优先级最高。

##### 4.2.2 其次是在UNC本地为Command层特殊返回码配置的动作**ADD CMDRCACT**。

##### 4.2.3 再者是在UNC本地为MSCC层特殊返回码配置的动作**ADD MSCCRCACT**。

##### 4.2.4 然后是UNC本地默认的Command层特殊返回码处理动作**SET CMDLEVDFTBEH**。

##### 4.2.5 优先级最低的是UNC本地默认的MSCC层特殊返回码处理动作**SET MSCCLEVDFTBEH**。

### 5 配置UNC收到OCS的CCA消息中携带FUI Terminate时的处理动作，配置“FUATERMINATE”参数。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_dcctemplate_list_4的变量区（command: ADD DCCTEMPLATE） -#}
<!-- MISSING_MACRO: command=ADD DCCTEMPLATE list_name=add_dcctemplate_list_4 step_id=5 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该mod_dcctemplate_list_4的变量区（command: MOD DCCTEMPLATE） -#}
<!-- MISSING_MACRO: command=MOD DCCTEMPLATE list_name=mod_dcctemplate_list_4 step_id=5 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_tctimer_list的变量区（command: SET TCTIMER） -#}
<!-- MISSING_MACRO: command=SET TCTIMER list_name=set_tctimer_list step_id=6 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_twtimer_list的变量区（command: SET TWTIMER） -#}
<!-- MISSING_MACRO: command=SET TWTIMER list_name=set_twtimer_list step_id=7 -->
```


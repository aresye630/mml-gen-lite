---
id: ''
name: 配置CCR触发场景
ne_type: UDG
type: feature
description: 本指导描述UNC上触发CCR消息的相关配置操作。  UNC和OCS都可以指定CCR触发场景，OCS可以通过CCA消息携带的信元Trigger AVP指定触发CCR上报的场景，UNC本地也可以配置CCR触发场景，OCS下发优先级更高。  UNC在多种场景下支持向OCS发起CCR更新流程，配置的时候可以根据需要选择配置。在线计费过程中，当其中一个条件满足时，便会触发CCR上报。建议配置的配额门限的大小适度，要满足CCR与CCA之间下次新配额申请时使用。
risk_level: ''
doc_source: ["特性部署","业务专题","5G Core 计费解决方案","计费解决方案概述","计费方案部署与调测","方案五：部署NCG且融合接口计费组网方案（N40接口+传统Ga/Gy接口）","SMF配置","在线计费配置","在线计费模板及交互配置","配置在线计费模板","配置CCR触发场景"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本指导描述UNC上触发CCR消息的相关配置操作。UNC和OCS都可以指定CCR触发场景，OCS可以通过CCA消息携带的信元Trigger AVP指定触发CCR上报的场景，UNC本地也可以配置CCR触发场景，OCS下发优先级更高。UNC在多种场景下支持向OCS发起CCR更新流程，配置的时候可以根据需要选择配置。在线计费过程中，当其中一个条件满足时，便会触发CCR上报。建议配置的配额门限的大小适度，要满足CCR与CCA之间下次新配额申请时使用。

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
    mod_dcctemplate_list:
      type: items
      properties:
        DCCTMPLTNAME:
          name: 'DCC模板名称'
          type: string
          required: false
          description: '新增或者修改DCC在线计费模板，用于配置在线计费相关属性。  说明：  如果需要配置在线计费全局参数，则需要使用**MOD DCCTEMPLATE**命令，“DCCTMPLTNAME”参数值为“global”。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        QCT:
          name: '配额空耗时间门限值（秒）'
          type: string
          required: false
          description: '配额空耗时间标识如何统计业务时长。QCT=0表示连续统计业务时长。'
          data_source: '与对端协商'
          pattern: ''
          default: ''
        QHT:
          name: '配额空闲时间门限值（秒）'
          type: string
          required: false
          description: '配额空闲时间监控业务暂停的时长。QHT=0表示QHT不生效。  说明：  如果OCS支持接收QHT超时触发的CCR消息，建议QHT不小于60秒，避免频繁触发CCR消息。'
          data_source: ''
          pattern: ''
          default: ''
        VQT:
          name: '流量阈值触发百分比（%）'
          type: string
          required: false
          description: '标识业务剩余流量配额百分比小于等于VQT时，触发上报CCR消息请求新配额。'
          data_source: ''
          pattern: ''
          default: ''
        TQT:
          name: '时间阈值触发百分比（%）'
          type: string
          required: false
          description: '标识业务剩余时长配额百分比小于等于TQT时，触发上报CCR消息请求新配额。'
          data_source: ''
          pattern: ''
          default: ''
        UQT:
          name: '事件阈值触发百分比（%）'
          type: string
          required: false
          description: '标识业务剩余事件配额百分比小于等于UQT时，触发上报CCR消息请求新配额。'
          data_source: ''
          pattern: ''
          default: ''
        CCRINITRGNUM:
          name: '指定CCR-I消息中携带RG的个数'
          type: string
          required: false
          description: '用户激活时发送的CCR-I消息中携带RG的个数。  说明：  该参数要与**SET CTXSTARTRATING**命令配合使用。如果在**SET CTXSTARTRATING**命令中指定了N个RG，则该参数至少要配置为N，才能使得上述N个RG都能被CCR-I消息带上申请配额。'
          data_source: ''
          pattern: ''
          default: ''
        VALIDTIME:
          name: '在线配额有效时长（分）'
          type: string
          required: false
          description: '标识配额有效时长，超时后触发上报CCR消息。'
          data_source: ''
          pattern: ''
          default: ''
        SERVICETRIGGER:
          name: '业务触发请求使能开关'
          type: string
          required: false
          description: '使用新业务是否发送CCR。'
          data_source: ''
          pattern: ''
          default: ''
        RATTRIGGER:
          name: 'Rat变化触发使能开关'
          type: string
          required: false
          description: 'RAT改变是否发送CCR。'
          data_source: ''
          pattern: ''
          default: ''
        SGSNTRIGGER:
          name: 'SGSN变化触发使能开关'
          type: string
          required: false
          description: 'SGSN/SGW地址改变是否发送CCR。'
          data_source: ''
          pattern: ''
          default: ''
        QOSTRIGGER:
          name: 'QoS变化触发使能开关'
          type: string
          required: false
          description: 'QoS改变是否发送CCR。'
          data_source: ''
          pattern: ''
          default: ''
        ULITRIGGER:
          name: 'ULI变化触发使能开关'
          type: string
          required: false
          description: 'ULI改变是否发送CCR。'
          data_source: ''
          pattern: ''
          default: ''
        MCCTRIGGER:
          name: 'MCC变化触发重授权开关'
          type: string
          required: false
          description: 'MCC改变是否发送CCR。'
          data_source: ''
          pattern: ''
          default: ''
        MNCTRIGGER:
          name: 'MNC变化触发重授权开关'
          type: string
          required: false
          description: 'MNC改变是否发送CCR.'
          data_source: ''
          pattern: ''
          default: ''
        LACTRIGGER:
          name: 'LAC变化触发重授权开关'
          type: string
          required: false
          description: 'LAC改变是否发送CCR。'
          data_source: ''
          pattern: ''
          default: ''
        UETZTRIGGER:
          name: 'UE TimeZone改变触发重授权开关'
          type: string
          required: false
          description: '终端时区改变是否发送CCR。'
          data_source: ''
          pattern: ''
          default: ''
        TACTRIGGER:
          name: 'TA改变触发重授权开关'
          type: string
          required: false
          description: 'TA改变是否触发重授权CCR请求。'
          data_source: ''
          pattern: ''
          default: ''
        ECGITRIGGER:
          name: 'ECGI改变触发重授权开关'
          type: string
          required: false
          description: 'ECGI改变是否触发重授权CCR请求'
          data_source: ''
          pattern: ''
          default: ''
        NOQUOTATRIGGER:
          name: '无配额更新开关'
          type: string
          required: false
          description: '业务无配额情况下，是否在PDP更新时发起重授权请求。'
          data_source: ''
          pattern: ''
          default: ''
        RACTRIGGER:
          name: 'RAC改变触发重授权开关'
          type: string
          required: false
          description: '用户RAC改变是否发送CCR。'
          data_source: ''
          pattern: ''
          default: ''
        CELLIDTRIGGER:
          name: 'CellID改变触发重授权开关'
          type: string
          required: false
          description: '用户CellID改变是否发送CCR。'
          data_source: ''
          pattern: ''
          default: ''
        ENBTRIGGER:
          name: 'eNodeB变化触发重授权开关'
          type: string
          required: false
          description: 'eNodeB变化是否触发重授权CCR请求。'
          data_source: ''
          pattern: ''
          default: ''
        SPRATETRIGGER:
          name: '服务PLMN控制速率改变触发重授权开关'
          type: string
          required: false
          description: '服务PLMN控制速率改变是否触发重授权CCR请求。'
          data_source: ''
          pattern: ''
          default: ''
        APNRATETRIGGER:
          name: 'APN控制速率改变触发重授权开关'
          type: string
          required: false
          description: 'APN控制速率改变是否触发重授权CCR请求。'
          data_source: ''
          pattern: ''
          default: ''
    add_dcctemplate_list:
      type: items
      properties:
        DCCTMPLTNAME:
          name: 'DCC模板名称'
          type: string
          required: false
          description: '新增或者修改DCC在线计费模板，用于配置在线计费相关属性。  说明：  如果需要配置在线计费全局参数，则需要使用**MOD DCCTEMPLATE**命令，“DCCTMPLTNAME”参数值为“global”。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        QCT:
          name: '配额空耗时间门限值（秒）'
          type: string
          required: false
          description: '配额空耗时间标识如何统计业务时长。QCT=0表示连续统计业务时长。'
          data_source: '与对端协商'
          pattern: ''
          default: ''
        QHT:
          name: '配额空闲时间门限值（秒）'
          type: string
          required: false
          description: '配额空闲时间监控业务暂停的时长。QHT=0表示QHT不生效。  说明：  如果OCS支持接收QHT超时触发的CCR消息，建议QHT不小于60秒，避免频繁触发CCR消息。'
          data_source: ''
          pattern: ''
          default: ''
        VQT:
          name: '流量阈值触发百分比（%）'
          type: string
          required: false
          description: '标识业务剩余流量配额百分比小于等于VQT时，触发上报CCR消息请求新配额。'
          data_source: ''
          pattern: ''
          default: ''
        TQT:
          name: '时间阈值触发百分比（%）'
          type: string
          required: false
          description: '标识业务剩余时长配额百分比小于等于TQT时，触发上报CCR消息请求新配额。'
          data_source: ''
          pattern: ''
          default: ''
        UQT:
          name: '事件阈值触发百分比（%）'
          type: string
          required: false
          description: '标识业务剩余事件配额百分比小于等于UQT时，触发上报CCR消息请求新配额。'
          data_source: ''
          pattern: ''
          default: ''
        CCRINITRGNUM:
          name: '指定CCR-I消息中携带RG的个数'
          type: string
          required: false
          description: '用户激活时发送的CCR-I消息中携带RG的个数。  说明：  该参数要与**SET CTXSTARTRATING**命令配合使用。如果在**SET CTXSTARTRATING**命令中指定了N个RG，则该参数至少要配置为N，才能使得上述N个RG都能被CCR-I消息带上申请配额。'
          data_source: ''
          pattern: ''
          default: ''
        VALIDTIME:
          name: '在线配额有效时长（分）'
          type: string
          required: false
          description: '标识配额有效时长，超时后触发上报CCR消息。'
          data_source: ''
          pattern: ''
          default: ''
        SERVICETRIGGER:
          name: '业务触发请求使能开关'
          type: string
          required: false
          description: '使用新业务是否发送CCR。'
          data_source: ''
          pattern: ''
          default: ''
        RATTRIGGER:
          name: 'Rat变化触发使能开关'
          type: string
          required: false
          description: 'RAT改变是否发送CCR。'
          data_source: ''
          pattern: ''
          default: ''
        SGSNTRIGGER:
          name: 'SGSN变化触发使能开关'
          type: string
          required: false
          description: 'SGSN/SGW地址改变是否发送CCR。'
          data_source: ''
          pattern: ''
          default: ''
        QOSTRIGGER:
          name: 'QoS变化触发使能开关'
          type: string
          required: false
          description: 'QoS改变是否发送CCR。'
          data_source: ''
          pattern: ''
          default: ''
        ULITRIGGER:
          name: 'ULI变化触发使能开关'
          type: string
          required: false
          description: 'ULI改变是否发送CCR。'
          data_source: ''
          pattern: ''
          default: ''
        MCCTRIGGER:
          name: 'MCC变化触发重授权开关'
          type: string
          required: false
          description: 'MCC改变是否发送CCR。'
          data_source: ''
          pattern: ''
          default: ''
        MNCTRIGGER:
          name: 'MNC变化触发重授权开关'
          type: string
          required: false
          description: 'MNC改变是否发送CCR.'
          data_source: ''
          pattern: ''
          default: ''
        LACTRIGGER:
          name: 'LAC变化触发重授权开关'
          type: string
          required: false
          description: 'LAC改变是否发送CCR。'
          data_source: ''
          pattern: ''
          default: ''
        UETZTRIGGER:
          name: 'UE TimeZone改变触发重授权开关'
          type: string
          required: false
          description: '终端时区改变是否发送CCR。'
          data_source: ''
          pattern: ''
          default: ''
        TACTRIGGER:
          name: 'TA改变触发重授权开关'
          type: string
          required: false
          description: 'TA改变是否触发重授权CCR请求。'
          data_source: ''
          pattern: ''
          default: ''
        ECGITRIGGER:
          name: 'ECGI改变触发重授权开关'
          type: string
          required: false
          description: 'ECGI改变是否触发重授权CCR请求'
          data_source: ''
          pattern: ''
          default: ''
        NOQUOTATRIGGER:
          name: '无配额更新开关'
          type: string
          required: false
          description: '业务无配额情况下，是否在PDP更新时发起重授权请求。'
          data_source: ''
          pattern: ''
          default: ''
        RACTRIGGER:
          name: 'RAC改变触发重授权开关'
          type: string
          required: false
          description: '用户RAC改变是否发送CCR。'
          data_source: ''
          pattern: ''
          default: ''
        CELLIDTRIGGER:
          name: 'CellID改变触发重授权开关'
          type: string
          required: false
          description: '用户CellID改变是否发送CCR。'
          data_source: ''
          pattern: ''
          default: ''
        ENBTRIGGER:
          name: 'eNodeB变化触发重授权开关'
          type: string
          required: false
          description: 'eNodeB变化是否触发重授权CCR请求。'
          data_source: ''
          pattern: ''
          default: ''
        SPRATETRIGGER:
          name: '服务PLMN控制速率改变触发重授权开关'
          type: string
          required: false
          description: '服务PLMN控制速率改变是否触发重授权CCR请求。'
          data_source: ''
          pattern: ''
          default: ''
        APNRATETRIGGER:
          name: 'APN控制速率改变触发重授权开关'
          type: string
          required: false
          description: 'APN控制速率改变是否触发重授权CCR请求。'
          data_source: ''
          pattern: ''
          default: ''
    mod_dcctemplate_list_1:
      type: items
      properties:
        DCCTMPLTNAME:
          name: 'DCC模板名称'
          type: string
          required: false
          description: '新增或者修改DCC在线计费模板，用于配置在线计费相关属性。  说明：  如果需要配置在线计费全局参数，则需要使用**MOD DCCTEMPLATE**命令，“DCCTMPLTNAME”参数值为“global”。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        QCT:
          name: '配额空耗时间门限值（秒）'
          type: string
          required: false
          description: '配额空耗时间标识如何统计业务时长。QCT=0表示连续统计业务时长。'
          data_source: '与对端协商'
          pattern: ''
          default: ''
        QHT:
          name: '配额空闲时间门限值（秒）'
          type: string
          required: false
          description: '配额空闲时间监控业务暂停的时长。QHT=0表示QHT不生效。  说明：  如果OCS支持接收QHT超时触发的CCR消息，建议QHT不小于60秒，避免频繁触发CCR消息。'
          data_source: ''
          pattern: ''
          default: ''
        VQT:
          name: '流量阈值触发百分比（%）'
          type: string
          required: false
          description: '标识业务剩余流量配额百分比小于等于VQT时，触发上报CCR消息请求新配额。'
          data_source: ''
          pattern: ''
          default: ''
        TQT:
          name: '时间阈值触发百分比（%）'
          type: string
          required: false
          description: '标识业务剩余时长配额百分比小于等于TQT时，触发上报CCR消息请求新配额。'
          data_source: ''
          pattern: ''
          default: ''
        UQT:
          name: '事件阈值触发百分比（%）'
          type: string
          required: false
          description: '标识业务剩余事件配额百分比小于等于UQT时，触发上报CCR消息请求新配额。'
          data_source: ''
          pattern: ''
          default: ''
        CCRINITRGNUM:
          name: '指定CCR-I消息中携带RG的个数'
          type: string
          required: false
          description: '用户激活时发送的CCR-I消息中携带RG的个数。  说明：  该参数要与**SET CTXSTARTRATING**命令配合使用。如果在**SET CTXSTARTRATING**命令中指定了N个RG，则该参数至少要配置为N，才能使得上述N个RG都能被CCR-I消息带上申请配额。'
          data_source: ''
          pattern: ''
          default: ''
        VALIDTIME:
          name: '在线配额有效时长（分）'
          type: string
          required: false
          description: '标识配额有效时长，超时后触发上报CCR消息。'
          data_source: ''
          pattern: ''
          default: ''
        SERVICETRIGGER:
          name: '业务触发请求使能开关'
          type: string
          required: false
          description: '使用新业务是否发送CCR。'
          data_source: ''
          pattern: ''
          default: ''
        RATTRIGGER:
          name: 'Rat变化触发使能开关'
          type: string
          required: false
          description: 'RAT改变是否发送CCR。'
          data_source: ''
          pattern: ''
          default: ''
        SGSNTRIGGER:
          name: 'SGSN变化触发使能开关'
          type: string
          required: false
          description: 'SGSN/SGW地址改变是否发送CCR。'
          data_source: ''
          pattern: ''
          default: ''
        QOSTRIGGER:
          name: 'QoS变化触发使能开关'
          type: string
          required: false
          description: 'QoS改变是否发送CCR。'
          data_source: ''
          pattern: ''
          default: ''
        ULITRIGGER:
          name: 'ULI变化触发使能开关'
          type: string
          required: false
          description: 'ULI改变是否发送CCR。'
          data_source: ''
          pattern: ''
          default: ''
        MCCTRIGGER:
          name: 'MCC变化触发重授权开关'
          type: string
          required: false
          description: 'MCC改变是否发送CCR。'
          data_source: ''
          pattern: ''
          default: ''
        MNCTRIGGER:
          name: 'MNC变化触发重授权开关'
          type: string
          required: false
          description: 'MNC改变是否发送CCR.'
          data_source: ''
          pattern: ''
          default: ''
        LACTRIGGER:
          name: 'LAC变化触发重授权开关'
          type: string
          required: false
          description: 'LAC改变是否发送CCR。'
          data_source: ''
          pattern: ''
          default: ''
        UETZTRIGGER:
          name: 'UE TimeZone改变触发重授权开关'
          type: string
          required: false
          description: '终端时区改变是否发送CCR。'
          data_source: ''
          pattern: ''
          default: ''
        TACTRIGGER:
          name: 'TA改变触发重授权开关'
          type: string
          required: false
          description: 'TA改变是否触发重授权CCR请求。'
          data_source: ''
          pattern: ''
          default: ''
        ECGITRIGGER:
          name: 'ECGI改变触发重授权开关'
          type: string
          required: false
          description: 'ECGI改变是否触发重授权CCR请求'
          data_source: ''
          pattern: ''
          default: ''
        NOQUOTATRIGGER:
          name: '无配额更新开关'
          type: string
          required: false
          description: '业务无配额情况下，是否在PDP更新时发起重授权请求。'
          data_source: ''
          pattern: ''
          default: ''
        RACTRIGGER:
          name: 'RAC改变触发重授权开关'
          type: string
          required: false
          description: '用户RAC改变是否发送CCR。'
          data_source: ''
          pattern: ''
          default: ''
        CELLIDTRIGGER:
          name: 'CellID改变触发重授权开关'
          type: string
          required: false
          description: '用户CellID改变是否发送CCR。'
          data_source: ''
          pattern: ''
          default: ''
        ENBTRIGGER:
          name: 'eNodeB变化触发重授权开关'
          type: string
          required: false
          description: 'eNodeB变化是否触发重授权CCR请求。'
          data_source: ''
          pattern: ''
          default: ''
        SPRATETRIGGER:
          name: '服务PLMN控制速率改变触发重授权开关'
          type: string
          required: false
          description: '服务PLMN控制速率改变是否触发重授权CCR请求。'
          data_source: ''
          pattern: ''
          default: ''
        APNRATETRIGGER:
          name: 'APN控制速率改变触发重授权开关'
          type: string
          required: false
          description: 'APN控制速率改变是否触发重授权CCR请求。'
          data_source: ''
          pattern: ''
          default: ''
    set_ocsinit_list:
      type: items
      properties:
        DCCTMPLTNAME:
          name: 'DCC模板名称'
          type: string
          required: false
          description: '配置用户激活时是否与OCS交互以及交互时是否等待OCS响应。  说明：  如果需要配置在线计费全局参数，则“DCCTMPLTNAME”参数值为“global”。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        OCSINIT:
          name: 'OCS交互使能开关'
          type: string
          required: false
          description: ''
          data_source: '与对端协商'
          pattern: ''
          default: ''
        WAITOCSRESP:
          name: 'OCS交互等待OCS响应开关'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_ctxstartrating_list:
      type: items
      properties:
        USERPROFILENAME:
          name: '用户模板名称'
          type: string
          required: false
          description: '配置用户激活时与OCS交互的CCR消息中携带的Rating Group信息。  说明：  此命令只对内容计费用户生效，PDP级别计费用户不适用该命令。PDP级别计费用户CCR-I中携带User Profile下或者全局下配置的默认计费属性，其中User Profile下的优先。如果User Profile下没有配置CCR-I的计费属性，则使用配置在全局下的CCR-I的计费属性。如果全局下没有配置CCR-I的计费属性，则CCR-I不携带计费属性。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        CTXRURRGRPNAME1:
          name: '初始请求URR组名称1'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CTXRURRGRPNAME2:
          name: '初始请求URR组名称2'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CTXRURRGRPNAME3:
          name: '初始请求URR组名称3'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CTXRURRGRPNAME4:
          name: '初始请求URR组名称4'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CTXRURRGRPNAME5:
          name: '初始请求URR组名称5'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    mod_dcctemplate_list:
    - DCCTMPLTNAME: dcc-test
      QCT: '0'
      QHT: '0'
      VQT: '20'
      TQT: '20'
      UQT: '20'
      CCRINITRGNUM: '5'
      VALIDTIME: '30'
      SERVICETRIGGER: ENABLE
      RATTRIGGER: ENABLE
      SGSNTRIGGER: ENABLE
      QOSTRIGGER: ENABLE
      ULITRIGGER: ENABLE
      MCCTRIGGER: ENABLE
      MNCTRIGGER: ENABLE
      LACTRIGGER: ENABLE
      UETZTRIGGER: ENABLE
      TACTRIGGER: DISABLE
      ECGITRIGGER: DISABLE
      NOQUOTATRIGGER: ENABLE
      RACTRIGGER: DISABLE
      CELLIDTRIGGER: DISABLE
      ENBTRIGGER: DISABLE
      SPRATETRIGGER: DISABLE
      APNRATETRIGGER: DISABLE
    add_dcctemplate_list:
    - DCCTMPLTNAME: dcc-test
      QCT: '0'
      QHT: '0'
      VQT: '20'
      TQT: '20'
      UQT: '20'
      CCRINITRGNUM: '5'
      VALIDTIME: '30'
      SERVICETRIGGER: ENABLE
      RATTRIGGER: ENABLE
      SGSNTRIGGER: ENABLE
      QOSTRIGGER: ENABLE
      ULITRIGGER: ENABLE
      MCCTRIGGER: ENABLE
      MNCTRIGGER: ENABLE
      LACTRIGGER: ENABLE
      UETZTRIGGER: ENABLE
      TACTRIGGER: DISABLE
      ECGITRIGGER: DISABLE
      NOQUOTATRIGGER: ENABLE
      RACTRIGGER: DISABLE
      CELLIDTRIGGER: DISABLE
      ENBTRIGGER: DISABLE
      SPRATETRIGGER: DISABLE
      APNRATETRIGGER: DISABLE
    mod_dcctemplate_list_1:
    - DCCTMPLTNAME: dcc-test
      QCT: '0'
      QHT: '0'
      VQT: '20'
      TQT: '20'
      UQT: '20'
      CCRINITRGNUM: '5'
      VALIDTIME: '30'
      SERVICETRIGGER: ENABLE
      RATTRIGGER: ENABLE
      SGSNTRIGGER: ENABLE
      QOSTRIGGER: ENABLE
      ULITRIGGER: ENABLE
      MCCTRIGGER: ENABLE
      MNCTRIGGER: ENABLE
      LACTRIGGER: ENABLE
      UETZTRIGGER: ENABLE
      TACTRIGGER: DISABLE
      ECGITRIGGER: DISABLE
      NOQUOTATRIGGER: ENABLE
      RACTRIGGER: DISABLE
      CELLIDTRIGGER: DISABLE
      ENBTRIGGER: DISABLE
      SPRATETRIGGER: DISABLE
      APNRATETRIGGER: DISABLE
    set_ocsinit_list:
    - DCCTMPLTNAME: dcc-test
      OCSINIT: ENABLE
      WAITOCSRESP: ENABLE
    set_ctxstartrating_list:
    - USERPROFILENAME: up-test
      CTXRURRGRPNAME1: urrgroup1
      CTXRURRGRPNAME2: urrgroup2
      CTXRURRGRPNAME3: urrgroup3
      CTXRURRGRPNAME4: urrgroup4
      CTXRURRGRPNAME5: urrgroup5
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 配置UNC Gy接口与OCS之间的DCC会话建立方式。

### 配置全局通用参数DCC模板，DCC模板名称。“DCCTMPLTNAME”=“global”

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该mod_dcctemplate_list的变量区（command: MOD DCCTEMPLATE） -#}
<!-- MISSING_MACRO: command=MOD DCCTEMPLATE list_name=mod_dcctemplate_list step_id=1 -->
```

### 2 配置/修改DCC模板。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_dcctemplate_list的变量区（command: ADD DCCTEMPLATE） -#}
<!-- MISSING_MACRO: command=ADD DCCTEMPLATE list_name=add_dcctemplate_list step_id=2 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该mod_dcctemplate_list_1的变量区（command: MOD DCCTEMPLATE） -#}
<!-- MISSING_MACRO: command=MOD DCCTEMPLATE list_name=mod_dcctemplate_list_1 step_id=2 -->
```

#### 2.1 配置CCR-I消息中允许携带的RG的最大个数。配置参数“CCRINITRGNUM”

#### 2.2 配置剩余流量配额小于VQT后向OCS发起CCR。配置参数“VQT”

#### 2.3 配置剩余时长配额小于TQT后向OCS发起CCR。配置参数“TQT”

#### “VQT”和“TQT”配置值不建议小于20，建议保持默认配置。

#### 2.4 配置剩余事件配额小于UQT后向OCS发起CCR。配置参数“UQT”

#### 2.5 配置配额能使用的有效时长超时后向OCS发起CCR。配置参数“VALIDTIME”

#### 2.6 配置当用户数据包停止传送时长超过QHT后向OCS发起CCR。配置参数“QHT”

##### 2.6.1 如果不想使用该功能，即无论用户停止数据传送多长时间也不触发CCR，则可以在OCS上指定CCA中携带的Quota-Holding-Time AVP值为0，或CCA中不携带Quota-Holding-Time AVP，且UNC本地配置QHT为0。

##### 2.6.2 在没有明确需求的情况下建议不使用QHT，配置为0。

##### 2.6.3 当QHT不为0时QHT必须大于QCT（Quota Consumption Time）。

#### 2.7 尚未申请过配额的新业务触发向OCS发起CCR。配置参数“SERVICETRIGGER”

#### 以下为配置PDP上下文/EPS承载更新场景（RAT改变、SGSN/S-GW地址改变、QoS改变、用户位置信息ULI改变（包括用户MCC、MNC改变）、终端时区改变触发的PDP上下文/EPS承载更新等）触发CCR。

#### 2.8 配置RAT改变发送CCR。配置参数“RATTRIGGER”

#### 2.9 配置SGSN/S-GW地址改变发送CCR。配置参数“SGSNTRIGGER”

#### 2.10 配置QoS改变发送CCR。配置参数“QOSTRIGGER”

#### 2.11 配置ULI改变发送CCR。配置参数“ULITRIGGER”

#### 2.12 配置终端时区改变发送CCR。配置参数“UETZTRIGGER”

#### 2.13 配置终端的MCC改变发送CCR。配置参数“MCCTRIGGER”

#### 2.14 配置终端的MNC改变发送CCR。配置参数“MNCTRIGGER”

#### 2.15 配置终端的LAC改变发送CCR。配置参数“LACTRIGGER”

#### 2.16 配置终端的eNodeB改变发送CCR。配置参数“ENBTRIGGER”

#### 2.17 配置终端的RAC改变发送CCR。配置参数“RACTRIGGER”

#### 2.18 配置终端的CellID改变发送CCR。配置参数“CELLIDTRIGGER”

#### 2.19 配置无配额情况下，在PDP/bearer更新时发送CCR。配置参数“NOQUOTATRIGGER”

#### 2.20 配置终端的服务PLMN控制速率改变发送CCR。配置参数“SPRATETRIGGER”

#### 2.21 配置终端的APN控制速率改变发送CCR。配置参数“APNRATETRIGGER”

### 3 配置PDP上下文/EPS承载激活时发送CCR-I与OCS交互。

#### 3.1 配置在线计费用户激活时需要与OCS交互。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_ocsinit_list的变量区（command: SET OCSINIT） -#}
<!-- MISSING_MACRO: command=SET OCSINIT list_name=set_ocsinit_list step_id=3.1 -->
```

#### 3.2 配置在线计费用户激活时CCR-I消息中携带指定的费率标识。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_ctxstartrating_list的变量区（command: SET CTXSTARTRATING） -#}
<!-- MISSING_MACRO: command=SET CTXSTARTRATING list_name=set_ctxstartrating_list step_id=3.2 -->
```

#### 此命令只对内容计费用户生效，PDP级别计费用户不适用该命令。PDP级别计费用户CCR-I中携带User Profile下或者全局下配置的默认计费属性，其中User Profile下的优先。如果User Profile下没有配置CCR-I的计费属性，则使用配置在全局下的CCR-I的计费属性。如果全局下没有配置CCR-I的计费属性，则CCR-I不携带计费属性。

#### **ADD DCCTEMPLATE**命令配置CCR-I消息中允许携带的RG的最大个数时要与**SET CTXSTARTRATING**命令配合使用。如果在**SET CTXSTARTRATING**命令中指定了N个RG，则**ADD DCCTEMPLATE**命令配置CCR-I消息中允许携带的RG的最大个数至少要配置为N，才能使得上述N个RG都能被CCR-I消息带上申请配额。


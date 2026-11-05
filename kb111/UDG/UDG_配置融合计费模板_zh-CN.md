---
id: ''
name: 配置融合计费模板
ne_type: UDG
type: feature
description: 本指导描述在UNC上配置融合计费模板的相关操作过程。  融合计费模板CCT（Converged Charging Template）中包含本地配置的融合计费参数，如计费的时间/流量门限等。UNC上默认配置一个名为global的模板，即全局通用参数模板CCT-global，用于配置整机通用的融合计费参数。除了CCT-global外，还可以配置其他普通CCT模板，用于配置以下更细粒度的融合计费参数。  * User Profile粒度：根据User Profile配置CCT，将CCT绑定到特定User Profile下。 * DNN粒度：根据DNN配置CCT，将CCT绑定到特定DNN下。 * 计费属性粒度：根据用户的计费属性Charging Characteristics配置CCT，将CCT绑定到特定CC下。  上述几种粒度范围的优先级从高到低依次是： User Profile下的配置 > DNN下的配置 > 计费属性Charging Characteristics下的配置 > 整机通用参数。如果高级别的参数没有配置，则依次向下继承低一级别的参数取值。  一旦确定了整个系统的融合计费参数配置粒度，则原则上所有融合计费参数的配置都必须统一使用该粒度。
risk_level: ''
doc_source: ["特性部署","业务专题","5G Core 计费解决方案","计费解决方案概述","计费方案部署与调测","方案一：未部署NCG的计费解决方案（N40接口）","SMF配置","融合计费模板及交互配置（N40接口）","配置融合计费模板"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本指导描述在UNC上配置融合计费模板的相关操作过程。融合计费模板CCT（Converged Charging Template）中包含本地配置的融合计费参数，如计费的时间/流量门限等。UNC上默认配置一个名为global的模板，即全局通用参数模板CCT-global，用于配置整机通用的融合计费参数。除了CCT-global外，还可以配置其他普通CCT模板，用于配置以下更细粒度的融合计费参数。* User Profile粒度：根据User Profile配置CCT，将CCT绑定到特定User Profile下。* DNN粒度：根据DNN配置CCT，将CCT绑定到特定DNN下。* 计费属性粒度：根据用户的计费属性Charging Characteristics配置CCT，将CCT绑定到特定CC下。上述几种粒度范围的优先级从高到低依次是： User Profile下的配置 > DNN下的配置 > 计费属性Charging Characteristics下的配置 > 整机通用参数。如果高级别的参数没有配置，则依次向下继承低一级别的参数取值。一旦确定了整个系统的融合计费参数配置粒度，则原则上所有融合计费参数的配置都必须统一使用该粒度。

## 必备事项
前提条件

前提条件

* 请仔细阅读融合计费原理。
* 完成加载License。
* 已完成APN、User Profile创建。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    mod_cct_list:
      type: items
      properties:
        CCTMPLTNAME:
          name: '融合计费模板名称'
          type: string
          required: false
          description: '修改全局通用参数CCT模板。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        QHT:
          name: '配额空闲时间门限值(秒)'
          type: string
          required: false
          description: ''
          data_source: '与对端协商'
          pattern: ''
          default: ''
        VQT:
          name: '流量阈值触发百分比(%)'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TQT:
          name: '时间阈值触发百分比(%)'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        UQT:
          name: '事件阈值触发百分比(%)'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VT:
          name: '在线配额有效时长(分)'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MAXNUMOFCCC:
          name: '计费条件改变阈值'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PDUVOLUMELIMIT:
          name: 'PDU流量阈值(MB)'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PDUTIMELIMIT:
          name: 'PDU时长阈值(分钟)'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RGVOLUMELIMIT:
          name: '业务级流量阈值(MB)'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RGTIMELIMIT:
          name: '业务级时长阈值(分钟)'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        QFVOLUMELIMIT:
          name: 'QF流量阈值(MB)'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        QFTIMELIMIT:
          name: 'QF时长阈值(分钟)'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        FUATERMINATE:
          name: '最终配额动作指示终结方式'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TIMEFORMAT:
          name: '时间格式'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MAXSVCCONTAINER:
          name: '最大携带的业务容器数量'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SECRUTHRESHOLD:
          name: 'RAN-SecondaryRAT-Usage-Report上报CHF的阈值'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MAXUSEDSRVNUM:
          name: '最大可使用的业务个数'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        QHTRPTTRIGGER:
          name: 'QHT超时触发的容器中Trigger的值'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ROAMFUATERMACT:
          name: '漫游用户最终配额动作指示终结方式'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ROAMVOLUMELIMIT:
          name: '漫游用户的PDU流量阈值(MB)'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        BLKFREESRV:
          name: '会话层异常返回码动作为Block时阻塞免费业务'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NOQUOTATRIGGER:
          name: '无配额更新开关'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_cct_list:
      type: items
      properties:
        CCTMPLTNAME:
          name: '融合计费模板名称'
          type: string
          required: false
          description: '新增CCT模板。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        QHT:
          name: '配额空闲时间门限值(秒)'
          type: string
          required: false
          description: '设置配额空闲时间门限值，数据包停止传送后，QHT立即开始计时，当数据包停止传送时间达到此门限值，向NCG/CHF(OCS)上报使用的配额。'
          data_source: '与对端协商'
          pattern: ''
          default: ''
        VQT:
          name: '流量阈值触发百分比(%)'
          type: string
          required: false
          description: '设置流量阈值，当剩余配额小于等于该值时触发Charging Data Request消息。'
          data_source: ''
          pattern: ''
          default: ''
        TQT:
          name: '时间阈值触发百分比(%)'
          type: string
          required: false
          description: '设置时间阈值，当剩余配额小于等于该值时触发Charging Data Request消息。'
          data_source: ''
          pattern: ''
          default: ''
        UQT:
          name: '事件阈值触发百分比(%)'
          type: string
          required: false
          description: '设置事件阈值，当剩余配额小于等于该值时触发Charging Data Request消息。'
          data_source: ''
          pattern: ''
          default: ''
        VT:
          name: '在线配额有效时长(分)'
          type: string
          required: false
          description: 'RG级配额的有效时长，即SMF/PGW-C/GGSN-C收到NCG/CHF(OCS)下发的配额后按有效时长启定时器，超时后SMF/PGW-C/GGSN-C立即向NCG/CHF(OCS)上报配额用量并申请新配额。'
          data_source: ''
          pattern: ''
          default: ''
        MAXNUMOFCCC:
          name: '计费条件改变阈值'
          type: string
          required: false
          description: '指定计费条件改变几次后会触发Charging Data Request Update消息。'
          data_source: ''
          pattern: ''
          default: ''
        PDUVOLUMELIMIT:
          name: 'PDU流量阈值(MB)'
          type: string
          required: false
          description: '指定PDU级触发Charging Data Request Update消息的流量阈值。'
          data_source: ''
          pattern: ''
          default: ''
        PDUTIMELIMIT:
          name: 'PDU时长阈值(分钟)'
          type: string
          required: false
          description: '指定PDU级别触发Charging Data Request Update消息的时长阈值。'
          data_source: ''
          pattern: ''
          default: ''
        RGVOLUMELIMIT:
          name: '业务级流量阈值(MB)'
          type: string
          required: false
          description: '指定RG级别触发Charging Data Request Update消息的流量阈值。'
          data_source: ''
          pattern: ''
          default: ''
        RGTIMELIMIT:
          name: '业务级时长阈值(分钟)'
          type: string
          required: false
          description: '指定RG级别触发Charging Data Request Update消息的时长阈值。'
          data_source: ''
          pattern: ''
          default: ''
        QFVOLUMELIMIT:
          name: 'QF流量阈值(MB)'
          type: string
          required: false
          description: '指定QF级别触发Charging Data Request Update消息的流量阈值。'
          data_source: ''
          pattern: ''
          default: ''
        QFTIMELIMIT:
          name: 'QF时长阈值(分钟)'
          type: string
          required: false
          description: '指定QF级别触发Charging Data Request Update消息的时长阈值。'
          data_source: ''
          pattern: ''
          default: ''
        FUATERMINATE:
          name: '最终配额动作指示终结方式'
          type: string
          required: false
          description: '配置融合计费模板中最终配额动作指示终结方式。'
          data_source: ''
          pattern: ''
          default: ''
        TIMEFORMAT:
          name: '时间格式'
          type: string
          required: false
          description: '指定发给NCG/CHF(OCS)的消息中的时间格式为localtime。'
          data_source: ''
          pattern: ''
          default: ''
        MAXSVCCONTAINER:
          name: '最大携带的业务容器数量'
          type: string
          required: false
          description: '控制N40消息中最大可以携带的容器数，避免在延时上报场景，用量长期不上报NCG/CHF(OCS)时容器个数过多和消息超大，并造成数据无法备份问题。  当消息中业务容器数量大于等于该值，SMF/PGW-C/GGSN-C会强制发送一个N40接口更新消息给NCG/CHF(OCS)，并携带TriggerType为“MANAGEMENT\_INTERVENTION”。取值0表示对消息中的业务容器数量不做限制。'
          data_source: ''
          pattern: ''
          default: ''
        SECRUTHRESHOLD:
          name: 'RAN-SecondaryRAT-Usage-Report上报CHF的阈值'
          type: string
          required: false
          description: '当SMF检查当前的RAN-SecondaryRAT-Usage-Report数量已达到过阈值配置，发起用量下查并上报NCG/CHF(OCS)，上报TriggerType为MANAGEMENT\_INTERVENTION。  该参数在**ADD N40MSGTEMP**命令的“SECRUSAGE”参数配置为ENABLE时才生效。'
          data_source: ''
          pattern: ''
          default: ''
        MAXUSEDSRVNUM:
          name: '最大可使用的业务个数'
          type: string
          required: false
          description: '配置用户最多可以同时访问的业务（RG/RG+SID）个数，当用户访问的业务超过该配置时，用户会被去活。'
          data_source: ''
          pattern: ''
          default: ''
        QHTRPTTRIGGER:
          name: 'QHT超时触发的容器中Trigger的值'
          type: string
          required: false
          description: '配置业务QHT超时触发的NCHF消息容器中Trigger的值。'
          data_source: ''
          pattern: ''
          default: ''
        ROAMFUATERMACT:
          name: '漫游用户最终配额动作指示终结方式'
          type: string
          required: false
          description: '配置漫游用户最终配额动作指示终结方式。'
          data_source: ''
          pattern: ''
          default: ''
        ROAMVOLUMELIMIT:
          name: '漫游用户的PDU流量阈值(MB)'
          type: string
          required: false
          description: '指定漫游用户的PDU级触发Charging Data Request Update消息的流量阈值。'
          data_source: ''
          pattern: ''
          default: ''
        BLKFREESRV:
          name: '会话层异常返回码动作为Block时阻塞免费业务'
          type: string
          required: false
          description: '配置会话层异常返回码动作为Block时是否阻塞免费业务。'
          data_source: ''
          pattern: ''
          default: ''
        NOQUOTATRIGGER:
          name: '无配额更新开关'
          type: string
          required: false
          description: '配置业务无配额（阻塞或重定向）场景，是否允许SMF/PGW-C/GGSN-C在接入侧更新或PDU会话级阈值到触发上报时向NCG/CHF(OCS)发起配额更新请求。'
          data_source: ''
          pattern: ''
          default: ''
    add_selectcctbycc_list:
      type: items
      properties:
        CCTYPE:
          name: 'Charge Characteristic类型'
          type: string
          required: false
          description: '基于CC粒度，将CCT绑定到特定CC下。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        CCVALUE:
          name: 'Charge Characteristic值'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        CCTMPLTNAME:
          name: '融合计费模板名称'
          type: string
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        MASK:
          name: 'Charge Characteristic特定值掩码'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        PRIORITY:
          name: 'Charge Characteristic优先级'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        SERVINGCCT:
          name: 'I-SMF/SGW使用的融合计费模板名称'
          type: string
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_cct_list_1:
      type: items
      properties:
        CCTMPLTNAME:
          name: '融合计费模板名称'
          type: string
          required: false
          description: '新增CCT模板。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        QHT:
          name: '配额空闲时间门限值(秒)'
          type: string
          required: false
          description: '设置配额空闲时间门限值，数据包停止传送后，QHT立即开始计时，当数据包停止传送时间达到此门限值，向NCG/CHF(OCS)上报使用的配额。'
          data_source: '与对端协商'
          pattern: ''
          default: ''
        VQT:
          name: '流量阈值触发百分比(%)'
          type: string
          required: false
          description: '设置流量阈值，当剩余配额小于等于该值时触发Charging Data Request消息。'
          data_source: ''
          pattern: ''
          default: ''
        TQT:
          name: '时间阈值触发百分比(%)'
          type: string
          required: false
          description: '设置时间阈值，当剩余配额小于等于该值时触发Charging Data Request消息。'
          data_source: ''
          pattern: ''
          default: ''
        UQT:
          name: '事件阈值触发百分比(%)'
          type: string
          required: false
          description: '设置事件阈值，当剩余配额小于等于该值时触发Charging Data Request消息。'
          data_source: ''
          pattern: ''
          default: ''
        VT:
          name: '在线配额有效时长(分)'
          type: string
          required: false
          description: 'RG级配额的有效时长，即SMF/PGW-C/GGSN-C收到NCG/CHF(OCS)下发的配额后按有效时长启定时器，超时后SMF/PGW-C/GGSN-C立即向NCG/CHF(OCS)上报配额用量并申请新配额。'
          data_source: ''
          pattern: ''
          default: ''
        MAXNUMOFCCC:
          name: '计费条件改变阈值'
          type: string
          required: false
          description: '指定计费条件改变几次后会触发Charging Data Request Update消息。'
          data_source: ''
          pattern: ''
          default: ''
        PDUVOLUMELIMIT:
          name: 'PDU流量阈值(MB)'
          type: string
          required: false
          description: '指定PDU级触发Charging Data Request Update消息的流量阈值。'
          data_source: ''
          pattern: ''
          default: ''
        PDUTIMELIMIT:
          name: 'PDU时长阈值(分钟)'
          type: string
          required: false
          description: '指定PDU级别触发Charging Data Request Update消息的时长阈值。'
          data_source: ''
          pattern: ''
          default: ''
        RGVOLUMELIMIT:
          name: '业务级流量阈值(MB)'
          type: string
          required: false
          description: '指定RG级别触发Charging Data Request Update消息的流量阈值。'
          data_source: ''
          pattern: ''
          default: ''
        RGTIMELIMIT:
          name: '业务级时长阈值(分钟)'
          type: string
          required: false
          description: '指定RG级别触发Charging Data Request Update消息的时长阈值。'
          data_source: ''
          pattern: ''
          default: ''
        QFVOLUMELIMIT:
          name: 'QF流量阈值(MB)'
          type: string
          required: false
          description: '指定QF级别触发Charging Data Request Update消息的流量阈值。'
          data_source: ''
          pattern: ''
          default: ''
        QFTIMELIMIT:
          name: 'QF时长阈值(分钟)'
          type: string
          required: false
          description: '指定QF级别触发Charging Data Request Update消息的时长阈值。'
          data_source: ''
          pattern: ''
          default: ''
        FUATERMINATE:
          name: '最终配额动作指示终结方式'
          type: string
          required: false
          description: '配置融合计费模板中最终配额动作指示终结方式。'
          data_source: ''
          pattern: ''
          default: ''
        TIMEFORMAT:
          name: '时间格式'
          type: string
          required: false
          description: '指定发给NCG/CHF(OCS)的消息中的时间格式为localtime。'
          data_source: ''
          pattern: ''
          default: ''
        MAXSVCCONTAINER:
          name: '最大携带的业务容器数量'
          type: string
          required: false
          description: '控制N40消息中最大可以携带的容器数，避免在延时上报场景，用量长期不上报NCG/CHF(OCS)时容器个数过多和消息超大，并造成数据无法备份问题。  当消息中业务容器数量大于等于该值，SMF/PGW-C/GGSN-C会强制发送一个N40接口更新消息给NCG/CHF(OCS)，并携带TriggerType为“MANAGEMENT\_INTERVENTION”。取值0表示对消息中的业务容器数量不做限制。'
          data_source: ''
          pattern: ''
          default: ''
        SECRUTHRESHOLD:
          name: 'RAN-SecondaryRAT-Usage-Report上报CHF的阈值'
          type: string
          required: false
          description: '当SMF检查当前的RAN-SecondaryRAT-Usage-Report数量已达到过阈值配置，发起用量下查并上报NCG/CHF(OCS)，上报TriggerType为MANAGEMENT\_INTERVENTION。  该参数在**ADD N40MSGTEMP**命令的“SECRUSAGE”参数配置为ENABLE时才生效。'
          data_source: ''
          pattern: ''
          default: ''
        MAXUSEDSRVNUM:
          name: '最大可使用的业务个数'
          type: string
          required: false
          description: '配置用户最多可以同时访问的业务（RG/RG+SID）个数，当用户访问的业务超过该配置时，用户会被去活。'
          data_source: ''
          pattern: ''
          default: ''
        QHTRPTTRIGGER:
          name: 'QHT超时触发的容器中Trigger的值'
          type: string
          required: false
          description: '配置业务QHT超时触发的NCHF消息容器中Trigger的值。'
          data_source: ''
          pattern: ''
          default: ''
        ROAMFUATERMACT:
          name: '漫游用户最终配额动作指示终结方式'
          type: string
          required: false
          description: '配置漫游用户最终配额动作指示终结方式。'
          data_source: ''
          pattern: ''
          default: ''
        ROAMVOLUMELIMIT:
          name: '漫游用户的PDU流量阈值(MB)'
          type: string
          required: false
          description: '指定漫游用户的PDU级触发Charging Data Request Update消息的流量阈值。'
          data_source: ''
          pattern: ''
          default: ''
        BLKFREESRV:
          name: '会话层异常返回码动作为Block时阻塞免费业务'
          type: string
          required: false
          description: '配置会话层异常返回码动作为Block时是否阻塞免费业务。'
          data_source: ''
          pattern: ''
          default: ''
        NOQUOTATRIGGER:
          name: '无配额更新开关'
          type: string
          required: false
          description: '配置业务无配额（阻塞或重定向）场景，是否允许SMF/PGW-C/GGSN-C在接入侧更新或PDU会话级阈值到触发上报时向NCG/CHF(OCS)发起配额更新请求。'
          data_source: ''
          pattern: ''
          default: ''
    set_apnchargectrl_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          required: false
          description: '为DNN/APN绑定融合计费模板。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        CCTEMPLATE:
          name: '融合计费模板'
          type: string
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_cct_list_2:
      type: items
      properties:
        CCTMPLTNAME:
          name: '融合计费模板名称'
          type: string
          required: false
          description: '新增CCT模板。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        QHT:
          name: '配额空闲时间门限值(秒)'
          type: string
          required: false
          description: '设置配额空闲时间门限值，数据包停止传送后，QHT立即开始计时，当数据包停止传送时间达到此门限值，向NCG/CHF(OCS)上报使用的配额。'
          data_source: '与对端协商'
          pattern: ''
          default: ''
        VQT:
          name: '流量阈值触发百分比(%)'
          type: string
          required: false
          description: '设置流量阈值，当剩余配额小于等于该值时触发Charging Data Request消息。'
          data_source: ''
          pattern: ''
          default: ''
        TQT:
          name: '时间阈值触发百分比(%)'
          type: string
          required: false
          description: '设置时间阈值，当剩余配额小于等于该值时触发Charging Data Request消息。'
          data_source: ''
          pattern: ''
          default: ''
        UQT:
          name: '事件阈值触发百分比(%)'
          type: string
          required: false
          description: '设置事件阈值，当剩余配额小于等于该值时触发Charging Data Request消息。'
          data_source: ''
          pattern: ''
          default: ''
        VT:
          name: '在线配额有效时长(分)'
          type: string
          required: false
          description: 'RG级配额的有效时长，即SMF/PGW-C/GGSN-C收到NCG/CHF(OCS)下发的配额后按有效时长启定时器，超时后SMF/PGW-C/GGSN-C立即向NCG/CHF(OCS)上报配额用量并申请新配额。'
          data_source: ''
          pattern: ''
          default: ''
        MAXNUMOFCCC:
          name: '计费条件改变阈值'
          type: string
          required: false
          description: '指定计费条件改变几次后会触发Charging Data Request Update消息。'
          data_source: ''
          pattern: ''
          default: ''
        PDUVOLUMELIMIT:
          name: 'PDU流量阈值(MB)'
          type: string
          required: false
          description: '指定PDU级触发Charging Data Request Update消息的流量阈值。'
          data_source: ''
          pattern: ''
          default: ''
        PDUTIMELIMIT:
          name: 'PDU时长阈值(分钟)'
          type: string
          required: false
          description: '指定PDU级别触发Charging Data Request Update消息的时长阈值。'
          data_source: ''
          pattern: ''
          default: ''
        RGVOLUMELIMIT:
          name: '业务级流量阈值(MB)'
          type: string
          required: false
          description: '指定RG级别触发Charging Data Request Update消息的流量阈值。'
          data_source: ''
          pattern: ''
          default: ''
        RGTIMELIMIT:
          name: '业务级时长阈值(分钟)'
          type: string
          required: false
          description: '指定RG级别触发Charging Data Request Update消息的时长阈值。'
          data_source: ''
          pattern: ''
          default: ''
        QFVOLUMELIMIT:
          name: 'QF流量阈值(MB)'
          type: string
          required: false
          description: '指定QF级别触发Charging Data Request Update消息的流量阈值。'
          data_source: ''
          pattern: ''
          default: ''
        QFTIMELIMIT:
          name: 'QF时长阈值(分钟)'
          type: string
          required: false
          description: '指定QF级别触发Charging Data Request Update消息的时长阈值。'
          data_source: ''
          pattern: ''
          default: ''
        FUATERMINATE:
          name: '最终配额动作指示终结方式'
          type: string
          required: false
          description: '配置融合计费模板中最终配额动作指示终结方式。'
          data_source: ''
          pattern: ''
          default: ''
        TIMEFORMAT:
          name: '时间格式'
          type: string
          required: false
          description: '指定发给NCG/CHF(OCS)的消息中的时间格式为localtime。'
          data_source: ''
          pattern: ''
          default: ''
        MAXSVCCONTAINER:
          name: '最大携带的业务容器数量'
          type: string
          required: false
          description: '控制N40消息中最大可以携带的容器数，避免在延时上报场景，用量长期不上报NCG/CHF(OCS)时容器个数过多和消息超大，并造成数据无法备份问题。  当消息中业务容器数量大于等于该值，SMF/PGW-C/GGSN-C会强制发送一个N40接口更新消息给NCG/CHF(OCS)，并携带TriggerType为“MANAGEMENT\_INTERVENTION”。取值0表示对消息中的业务容器数量不做限制。'
          data_source: ''
          pattern: ''
          default: ''
        SECRUTHRESHOLD:
          name: 'RAN-SecondaryRAT-Usage-Report上报CHF的阈值'
          type: string
          required: false
          description: '当SMF检查当前的RAN-SecondaryRAT-Usage-Report数量已达到过阈值配置，发起用量下查并上报NCG/CHF(OCS)，上报TriggerType为MANAGEMENT\_INTERVENTION。  该参数在**ADD N40MSGTEMP**命令的“SECRUSAGE”参数配置为ENABLE时才生效。'
          data_source: ''
          pattern: ''
          default: ''
        MAXUSEDSRVNUM:
          name: '最大可使用的业务个数'
          type: string
          required: false
          description: '配置用户最多可以同时访问的业务（RG/RG+SID）个数，当用户访问的业务超过该配置时，用户会被去活。'
          data_source: ''
          pattern: ''
          default: ''
        QHTRPTTRIGGER:
          name: 'QHT超时触发的容器中Trigger的值'
          type: string
          required: false
          description: '配置业务QHT超时触发的NCHF消息容器中Trigger的值。'
          data_source: ''
          pattern: ''
          default: ''
        ROAMFUATERMACT:
          name: '漫游用户最终配额动作指示终结方式'
          type: string
          required: false
          description: '配置漫游用户最终配额动作指示终结方式。'
          data_source: ''
          pattern: ''
          default: ''
        ROAMVOLUMELIMIT:
          name: '漫游用户的PDU流量阈值(MB)'
          type: string
          required: false
          description: '指定漫游用户的PDU级触发Charging Data Request Update消息的流量阈值。'
          data_source: ''
          pattern: ''
          default: ''
        BLKFREESRV:
          name: '会话层异常返回码动作为Block时阻塞免费业务'
          type: string
          required: false
          description: '配置会话层异常返回码动作为Block时是否阻塞免费业务。'
          data_source: ''
          pattern: ''
          default: ''
        NOQUOTATRIGGER:
          name: '无配额更新开关'
          type: string
          required: false
          description: '配置业务无配额（阻塞或重定向）场景，是否允许SMF/PGW-C/GGSN-C在接入侧更新或PDU会话级阈值到触发上报时向NCG/CHF(OCS)发起配额更新请求。'
          data_source: ''
          pattern: ''
          default: ''
    set_usrprofcharge_list:
      type: items
      properties:
        USRPROFNAME:
          name: '用户模板名称'
          type: string
          required: false
          description: '为User Profile绑定融合计费模板。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        CCTEMPLATE:
          name: '融合计费模板名称'
          type: string
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
  examples:
    mod_cct_list:
    - CCTMPLTNAME: global
      QHT: '0'
      VQT: '20'
      TQT: '20'
      UQT: '20'
      VT: '30'
      MAXNUMOFCCC: '3'
      PDUVOLUMELIMIT: '500'
      PDUTIMELIMIT: '30'
      RGVOLUMELIMIT: '500'
      RGTIMELIMIT: '30'
      QFVOLUMELIMIT: '500'
      QFTIMELIMIT: '30'
      FUATERMINATE: TERM_SERVICE
      TIMEFORMAT: LocalTime
      MAXSVCCONTAINER: '100'
      SECRUTHRESHOLD: '100'
      MAXUSEDSRVNUM: '60'
      QHTRPTTRIGGER: QHT
      ROAMFUATERMACT: TERM_SERVICE
      ROAMVOLUMELIMIT: '0'
      BLKFREESRV: PASS
      NOQUOTATRIGGER: ENABLE
    add_cct_list:
    - CCTMPLTNAME: cct_test
      QHT: '0'
      VQT: '20'
      TQT: '20'
      UQT: '20'
      VT: '30'
      MAXNUMOFCCC: '3'
      PDUVOLUMELIMIT: '500'
      PDUTIMELIMIT: '30'
      RGVOLUMELIMIT: '500'
      RGTIMELIMIT: '30'
      QFVOLUMELIMIT: '500'
      QFTIMELIMIT: '30'
      FUATERMINATE: TERM_SERVICE
      TIMEFORMAT: LocalTime
      MAXSVCCONTAINER: '100'
      SECRUTHRESHOLD: '100'
      MAXUSEDSRVNUM: '60'
      QHTRPTTRIGGER: QHT
      ROAMFUATERMACT: TERM_SERVICE
      ROAMVOLUMELIMIT: '20'
      BLKFREESRV: PASS
      NOQUOTATRIGGER: ENABLE
    add_selectcctbycc_list:
    - CCTYPE: VALUE
      CCVALUE: '0x0800'
      CCTMPLTNAME: cct_test
      MASK: '0xFFFF'
      PRIORITY: '1'
      SERVINGCCT: cct_test
    add_cct_list_1:
    - CCTMPLTNAME: cct_test
      QHT: '0'
      VQT: '20'
      TQT: '20'
      UQT: '20'
      VT: '30'
      MAXNUMOFCCC: '3'
      PDUVOLUMELIMIT: '500'
      PDUTIMELIMIT: '30'
      RGVOLUMELIMIT: '500'
      RGTIMELIMIT: '30'
      QFVOLUMELIMIT: '500'
      QFTIMELIMIT: '30'
      FUATERMINATE: TERM_SERVICE
      TIMEFORMAT: LocalTime
      MAXSVCCONTAINER: '100'
      SECRUTHRESHOLD: '100'
      MAXUSEDSRVNUM: '60'
      QHTRPTTRIGGER: QHT
      ROAMFUATERMACT: TERM_SERVICE
      ROAMVOLUMELIMIT: '20'
      BLKFREESRV: PASS
      NOQUOTATRIGGER: ENABLE
    set_apnchargectrl_list:
    - APN: apn-test
      CCTEMPLATE: cct_test
    add_cct_list_2:
    - CCTMPLTNAME: cct_test
      QHT: '0'
      VQT: '20'
      TQT: '20'
      UQT: '20'
      VT: '30'
      MAXNUMOFCCC: '3'
      PDUVOLUMELIMIT: '500'
      PDUTIMELIMIT: '30'
      RGVOLUMELIMIT: '500'
      RGTIMELIMIT: '30'
      QFVOLUMELIMIT: '500'
      QFTIMELIMIT: '30'
      FUATERMINATE: TERM_SERVICE
      TIMEFORMAT: LocalTime
      MAXSVCCONTAINER: '100'
      SECRUTHRESHOLD: '100'
      MAXUSEDSRVNUM: '60'
      QHTRPTTRIGGER: QHT
      ROAMFUATERMACT: TERM_SERVICE
      ROAMVOLUMELIMIT: '20'
      BLKFREESRV: PASS
      NOQUOTATRIGGER: ENABLE
    set_usrprofcharge_list:
    - USRPROFNAME: up_test
      CCTEMPLATE: cct_test
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 配置全局通用CCT模板。

#### 1.1 修改系统默认配置的全局通用参数CCT模板，该模板名称为“global”。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该mod_cct_list的变量区（command: MOD CCT） -#}
<!-- MISSING_MACRO: command=MOD CCT list_name=mod_cct_list step_id=1.1 -->
```

### 2 配置CC粒度的CCT。

#### 2.1 配置CCT模板。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_cct_list的变量区（command: ADD CCT） -#}
<!-- MISSING_MACRO: command=ADD CCT list_name=add_cct_list step_id=2.1 -->
```

#### 2.2 配置计费属性。

#### 请参见配置计费属性。

#### 2.3 配置CCT模板绑定CC。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_selectcctbycc_list的变量区（command: ADD SELECTCCTBYCC） -#}
<!-- MISSING_MACRO: command=ADD SELECTCCTBYCC list_name=add_selectcctbycc_list step_id=2.3 -->
```

### 3 配置DNN粒度的CCT。

#### 3.1 配置CCT模板。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_cct_list_1的变量区（command: ADD CCT） -#}
<!-- MISSING_MACRO: command=ADD CCT list_name=add_cct_list_1 step_id=3.1 -->
```

#### 3.2 配置CCT模板绑定DNN。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_apnchargectrl_list的变量区（command: SET APNCHARGECTRL） -#}
<!-- MISSING_MACRO: command=SET APNCHARGECTRL list_name=set_apnchargectrl_list step_id=3.2 -->
```

### 4 配置User Profile粒度的CCT。

#### 4.1 配置CCT模板。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_cct_list_2的变量区（command: ADD CCT） -#}
<!-- MISSING_MACRO: command=ADD CCT list_name=add_cct_list_2 step_id=4.1 -->
```

#### 4.2 配置User Profile，将CCT绑定到User Profile上。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_usrprofcharge_list的变量区（command: SET USRPROFCHARGE） -#}
<!-- MISSING_MACRO: command=SET USRPROFCHARGE list_name=set_usrprofcharge_list step_id=4.2 -->
```


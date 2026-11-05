---
id: ''
name: 配置融合计费模板
ne_type: UNC
type: feature
description: 融合计费模板CCT（Converged Charging Template）中包含本地配置的融合计费参数，如计费的时间/流量门限等。UNC上默认配置一个名为global的模板，即全局通用参数模板CCT-global，用于配置整机通用的融合计费参数。除了CCT-global外，还可以配置其他普通CCT模板，用于配置以下更细粒度的融合计费参数。  * UserProfile粒度：根据UserProfile配置CCT，将CCT绑定到特性UserProfile下。 * DNN粒度：根据DNN配置CCT，将CCT绑定到特定DNN下。 * CC粒度：根据用户的计费属性Charging Characteristics配置CCT，将CCT绑定到特定CC下。  上述几种粒度范围的优先级从高到低依次是： UserProfile下的配置 > DNN下的配置 > 计费属性Charging Characteristics下的配置 > 整机通用参数。如果高级别的参数没有配置，则依次向下继承低一级别的参数取值。  一旦确定了整个系统的融合计费参数配置粒度，则原则上所有融合计费参数的配置都必须统一使用该粒度。  适用于SMF。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","计费管理功能","WSFD-011206 支持融合计费","激活支持融合计费","配置融合计费模板"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
融合计费模板CCT（Converged Charging Template）中包含本地配置的融合计费参数，如计费的时间/流量门限等。UNC上默认配置一个名为global的模板，即全局通用参数模板CCT-global，用于配置整机通用的融合计费参数。除了CCT-global外，还可以配置其他普通CCT模板，用于配置以下更细粒度的融合计费参数。* UserProfile粒度：根据UserProfile配置CCT，将CCT绑定到特性UserProfile下。* DNN粒度：根据DNN配置CCT，将CCT绑定到特定DNN下。* CC粒度：根据用户的计费属性Charging Characteristics配置CCT，将CCT绑定到特定CC下。上述几种粒度范围的优先级从高到低依次是： UserProfile下的配置 > DNN下的配置 > 计费属性Charging Characteristics下的配置 > 整机通用参数。如果高级别的参数没有配置，则依次向下继承低一级别的参数取值。一旦确定了整个系统的融合计费参数配置粒度，则原则上所有融合计费参数的配置都必须统一使用该粒度。适用于SMF。

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
    mod_cct_list:
      type: items
      properties:
        CCTMPLTNAME:
          name: '融合计费模板名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '修改全局通用参数CCT模板。'
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
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_cct_list:
      type: items
      properties:
        CCTMPLTNAME:
          name: '融合计费模板名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '新增CCT模板。'
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
          description: '设置配额空闲时间门限值，数据包停止传送后，QHT立即开始计时，当数据包停止传送时间达到此门限值，向CHF上报使用的配额。'
          data_source: '本端规划'
          pattern: ''
          default: 0
        VQT:
          name: '流量阈值触发百分比(%)'
          type: integer
          minimum: 0
          maximum: 50
          required: false
          description: '设置流量阈值。'
          data_source: ''
          pattern: ''
          default: 20
        TQT:
          name: '时间阈值触发百分比(%)'
          type: integer
          minimum: 0
          maximum: 50
          required: false
          description: '设置时间阈值。'
          data_source: ''
          pattern: ''
          default: 20
        UQT:
          name: '事件阈值触发百分比(%)'
          type: integer
          minimum: 0
          maximum: 50
          required: false
          description: '设置事件阈值。'
          data_source: ''
          pattern: ''
          default: 20
        VT:
          name: '在线配额有效时长(分)'
          type: integer
          minimum:
          - 0
          - 5
          maximum:
          - 0
          - 1440
          required: false
          description: 'RG级配额的有效时长，即SMF收到CHF下发的配额后按有效时长启定时器，超时后SMF立即向CHF上报配额用量并申请新配额。'
          data_source: ''
          pattern: ''
          default: 30
        MAXNUMOFCCC:
          name: '计费条件改变阈值'
          type: integer
          minimum: 1
          maximum: 10
          required: false
          description: '指定计费条件改变几次后会触发Charging Data Request Update消息。'
          data_source: ''
          pattern: ''
          default: 3
        PDUVOLUMELIMIT:
          name: 'PDU流量阈值(MB)'
          type: integer
          minimum: 0
          maximum: 2147483647
          required: false
          description: '指定PDU级触发Charging Data Request Update消息的流量阈值。'
          data_source: ''
          pattern: ''
          default: 500
        PDUTIMELIMIT:
          name: 'PDU时长阈值(分钟)'
          type: integer
          minimum: 0
          maximum: 1440
          required: false
          description: '指定PDU级别触发Charging Data Request Update消息的时长阈值。'
          data_source: ''
          pattern: ''
          default: 30
        RGVOLUMELIMIT:
          name: '业务级流量阈值(MB)'
          type: integer
          minimum: 0
          maximum: 2147483647
          required: false
          description: '指定RG级别触发Charging Data Request Update消息的流量阈值。'
          data_source: ''
          pattern: ''
          default: 500
        RGTIMELIMIT:
          name: '业务级时长阈值(分钟)'
          type: integer
          minimum: 0
          maximum: 1440
          required: false
          description: '指定RG级别触发Charging Data Request Update消息的时长阈值。'
          data_source: ''
          pattern: ''
          default: 30
        FUATERMINATE:
          name: '最终配额动作指示终结方式'
          type: string
          enum:
          - TERM_SERVICE
          - TERM_SESSION
          required: false
          description: '配置融合计费模板中最终配额动作指示终结方式为阻塞业务。'
          data_source: ''
          pattern: ''
          default: TERM_SERVICE
        TIMEFORMAT:
          name: '时间格式'
          type: string
          enum:
          - LocalTime
          - UTC
          required: false
          description: '指定发给CHF的消息中的时间格式为localtime。'
          data_source: ''
          pattern: ''
          default: LocalTime
        MAXSVCCONTAINER:
          name: '最大携带的业务容器数量'
          type: integer
          minimum: 0
          maximum: 100
          required: false
          description: '控制N40消息中最大可以携带的容器数，避免在延时上报场景，用量长期不上报CHF时容器个数过多和消息超大，并造成数据无法备份问题。  当消息中业务容器数量大于等于该值，会强制发送一个N40接口更新消息给CHF，并携带TriggerType为“MANAGEMENT\_INTERVENTION”。取值0表示对消息中的业务容器数量不做限制。'
          data_source: ''
          pattern: ''
          default: 100
        SECRUTHRESHOLD:
          name: 'RAN-SecondaryRAT-Usage-Report上报CHF的阈值'
          type: integer
          minimum: 0
          maximum: 100
          required: false
          description: '当SMF检查当前的RAN-SecondaryRAT-Usage-Report数量已达到过阈值配置，发起用量下查并上报CHF，上报TriggerType为MANAGEMENT\_INTERVENTION。  该参数在****ADD N40MSGTEMP****命令的“SECRATUSAGE”参数配置为ENABLE时才生效。'
          data_source: ''
          pattern: ''
          default: 100
        ROAMFUATERMACT:
          name: '漫游用户最终配额动作指示终结方式'
          type: string
          enum:
          - TERM_SERVICE
          - TERM_SESSION
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: TERM_SERVICE
    add_selectcctbycc_list:
      type: items
      properties:
        CCTYPE:
          name: 'Charge Characteristic类型'
          type: string
          enum:
          - DEFAULT
          - VALUE
          required: true
          description: '基于CC粒度，将CCT绑定到特定CC下。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        CCVALUE:
          name: 'Charge Characteristic值'
          type: string
          minLength: 1
          maxLength: 6
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        CCTMPLTNAME:
          name: '融合计费模板名称'
          type: string
          minLength: 1
          maxLength: 63
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        MASK:
          name: 'Charge Characteristic特定值掩码'
          type: string
          minLength: 1
          maxLength: 6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PRIORITY:
          name: 'Charge Characteristic优先级'
          type: integer
          minimum: 1
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_cct_list_1:
      type: items
      properties:
        CCTMPLTNAME:
          name: '融合计费模板名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '新增CCT模板。'
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
          description: '设置配额空闲时间门限值，数据包停止传送后，QHT立即开始计时，当数据包停止传送时间达到此门限值，向CHF上报使用的配额。'
          data_source: '本端规划'
          pattern: ''
          default: 0
        VQT:
          name: '流量阈值触发百分比(%)'
          type: integer
          minimum: 0
          maximum: 50
          required: false
          description: '设置流量阈值。'
          data_source: ''
          pattern: ''
          default: 20
        TQT:
          name: '时间阈值触发百分比(%)'
          type: integer
          minimum: 0
          maximum: 50
          required: false
          description: '设置时间阈值。'
          data_source: ''
          pattern: ''
          default: 20
        UQT:
          name: '事件阈值触发百分比(%)'
          type: integer
          minimum: 0
          maximum: 50
          required: false
          description: '设置事件阈值。'
          data_source: ''
          pattern: ''
          default: 20
        VT:
          name: '在线配额有效时长(分)'
          type: integer
          minimum:
          - 0
          - 5
          maximum:
          - 0
          - 1440
          required: false
          description: 'RG级配额的有效时长，即SMF收到CHF下发的配额后按有效时长启定时器，超时后SMF立即向CHF上报配额用量并申请新配额。'
          data_source: ''
          pattern: ''
          default: 30
        MAXNUMOFCCC:
          name: '计费条件改变阈值'
          type: integer
          minimum: 1
          maximum: 10
          required: false
          description: '指定计费条件改变几次后会触发Charging Data Request Update消息。'
          data_source: ''
          pattern: ''
          default: 3
        PDUVOLUMELIMIT:
          name: 'PDU流量阈值(MB)'
          type: integer
          minimum: 0
          maximum: 2147483647
          required: false
          description: '指定PDU级触发Charging Data Request Update消息的流量阈值。'
          data_source: ''
          pattern: ''
          default: 500
        PDUTIMELIMIT:
          name: 'PDU时长阈值(分钟)'
          type: integer
          minimum: 0
          maximum: 1440
          required: false
          description: '指定PDU级别触发Charging Data Request Update消息的时长阈值。'
          data_source: ''
          pattern: ''
          default: 30
        RGVOLUMELIMIT:
          name: '业务级流量阈值(MB)'
          type: integer
          minimum: 0
          maximum: 2147483647
          required: false
          description: '指定RG级别触发Charging Data Request Update消息的流量阈值。'
          data_source: ''
          pattern: ''
          default: 500
        RGTIMELIMIT:
          name: '业务级时长阈值(分钟)'
          type: integer
          minimum: 0
          maximum: 1440
          required: false
          description: '指定RG级别触发Charging Data Request Update消息的时长阈值。'
          data_source: ''
          pattern: ''
          default: 30
        FUATERMINATE:
          name: '最终配额动作指示终结方式'
          type: string
          enum:
          - TERM_SERVICE
          - TERM_SESSION
          required: false
          description: '配置融合计费模板中最终配额动作指示终结方式为阻塞业务。'
          data_source: ''
          pattern: ''
          default: TERM_SERVICE
        TIMEFORMAT:
          name: '时间格式'
          type: string
          enum:
          - LocalTime
          - UTC
          required: false
          description: '指定发给CHF的消息中的时间格式为localtime。'
          data_source: ''
          pattern: ''
          default: LocalTime
        MAXSVCCONTAINER:
          name: '最大携带的业务容器数量'
          type: integer
          minimum: 0
          maximum: 100
          required: false
          description: '控制N40消息中最大可以携带的容器数，避免在延时上报场景，用量长期不上报CHF时容器个数过多和消息超大，并造成数据无法备份问题。  当消息中业务容器数量大于等于该值，会强制发送一个N40接口更新消息给CHF，并携带TriggerType为“MANAGEMENT\_INTERVENTION”。取值0表示对消息中的业务容器数量不做限制。'
          data_source: ''
          pattern: ''
          default: 100
        SECRUTHRESHOLD:
          name: 'RAN-SecondaryRAT-Usage-Report上报CHF的阈值'
          type: integer
          minimum: 0
          maximum: 100
          required: false
          description: '当SMF检查当前的RAN-SecondaryRAT-Usage-Report数量已达到过阈值配置，发起用量下查并上报CHF，上报TriggerType为MANAGEMENT\_INTERVENTION。  该参数在****ADD N40MSGTEMP****命令的“SECRATUSAGE”参数配置为ENABLE时才生效。'
          data_source: ''
          pattern: ''
          default: 100
        ROAMFUATERMACT:
          name: '漫游用户最终配额动作指示终结方式'
          type: string
          enum:
          - TERM_SERVICE
          - TERM_SESSION
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: TERM_SERVICE
    add_apn_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '基于DNN粒度，将CCT绑定到特定DNN下。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        HASVPN:
          name: '绑定VPN'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
        HASVPNIPV6:
          name: '绑定IPv6 VPN'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
        RESTORPGWSWITCH:
          name: '故障重启业务恢复功能PGW开关'
          type: string
          enum:
          - ENABLE
          - INHERIT
          - DISABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: INHERIT
        VPNINSTANCE:
          name: 'VPN实例名'
          type: string
          minLength: 1
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VPNINSTANCEIPV6:
          name: 'IPv6 VPN实例名'
          type: string
          minLength: 1
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PDTNSWITCH:
          name: 'PDTN功能开关'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
    set_apnchargectrl_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        CCTEMPLATE:
          name: '融合计费模板'
          type: string
          maxLength: 63
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
          minLength: 1
          maxLength: 63
          required: true
          description: '新增CCT模板。'
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
          description: '设置配额空闲时间门限值，数据包停止传送后，QHT立即开始计时，当数据包停止传送时间达到此门限值，向CHF上报使用的配额。'
          data_source: '本端规划'
          pattern: ''
          default: 0
        VQT:
          name: '流量阈值触发百分比(%)'
          type: integer
          minimum: 0
          maximum: 50
          required: false
          description: '设置流量阈值。'
          data_source: ''
          pattern: ''
          default: 20
        TQT:
          name: '时间阈值触发百分比(%)'
          type: integer
          minimum: 0
          maximum: 50
          required: false
          description: '设置时间阈值。'
          data_source: ''
          pattern: ''
          default: 20
        UQT:
          name: '事件阈值触发百分比(%)'
          type: integer
          minimum: 0
          maximum: 50
          required: false
          description: '设置事件阈值。'
          data_source: ''
          pattern: ''
          default: 20
        VT:
          name: '在线配额有效时长(分)'
          type: integer
          minimum:
          - 0
          - 5
          maximum:
          - 0
          - 1440
          required: false
          description: 'RG级配额的有效时长，即SMF收到CHF下发的配额后按有效时长启定时器，超时后SMF立即向CHF上报配额用量并申请新配额。'
          data_source: ''
          pattern: ''
          default: 30
        MAXNUMOFCCC:
          name: '计费条件改变阈值'
          type: integer
          minimum: 1
          maximum: 10
          required: false
          description: '指定计费条件改变几次后会触发Charging Data Request Update消息。'
          data_source: ''
          pattern: ''
          default: 3
        PDUVOLUMELIMIT:
          name: 'PDU流量阈值(MB)'
          type: integer
          minimum: 0
          maximum: 2147483647
          required: false
          description: '指定PDU级触发Charging Data Request Update消息的流量阈值。'
          data_source: ''
          pattern: ''
          default: 500
        PDUTIMELIMIT:
          name: 'PDU时长阈值(分钟)'
          type: integer
          minimum: 0
          maximum: 1440
          required: false
          description: '指定PDU级别触发Charging Data Request Update消息的时长阈值。'
          data_source: ''
          pattern: ''
          default: 30
        RGVOLUMELIMIT:
          name: '业务级流量阈值(MB)'
          type: integer
          minimum: 0
          maximum: 2147483647
          required: false
          description: '指定RG级别触发Charging Data Request Update消息的流量阈值。'
          data_source: ''
          pattern: ''
          default: 500
        RGTIMELIMIT:
          name: '业务级时长阈值(分钟)'
          type: integer
          minimum: 0
          maximum: 1440
          required: false
          description: '指定RG级别触发Charging Data Request Update消息的时长阈值。'
          data_source: ''
          pattern: ''
          default: 30
        FUATERMINATE:
          name: '最终配额动作指示终结方式'
          type: string
          enum:
          - TERM_SERVICE
          - TERM_SESSION
          required: false
          description: '配置融合计费模板中最终配额动作指示终结方式为阻塞业务。'
          data_source: ''
          pattern: ''
          default: TERM_SERVICE
        TIMEFORMAT:
          name: '时间格式'
          type: string
          enum:
          - LocalTime
          - UTC
          required: false
          description: '指定发给CHF的消息中的时间格式为localtime。'
          data_source: ''
          pattern: ''
          default: LocalTime
        MAXSVCCONTAINER:
          name: '最大携带的业务容器数量'
          type: integer
          minimum: 0
          maximum: 100
          required: false
          description: '控制N40消息中最大可以携带的容器数，避免在延时上报场景，用量长期不上报CHF时容器个数过多和消息超大，并造成数据无法备份问题。  当消息中业务容器数量大于等于该值，会强制发送一个N40接口更新消息给CHF，并携带TriggerType为“MANAGEMENT\_INTERVENTION”。取值0表示对消息中的业务容器数量不做限制。'
          data_source: ''
          pattern: ''
          default: 100
        SECRUTHRESHOLD:
          name: 'RAN-SecondaryRAT-Usage-Report上报CHF的阈值'
          type: integer
          minimum: 0
          maximum: 100
          required: false
          description: '当SMF检查当前的RAN-SecondaryRAT-Usage-Report数量已达到过阈值配置，发起用量下查并上报CHF，上报TriggerType为MANAGEMENT\_INTERVENTION。  该参数在****ADD N40MSGTEMP****命令的“SECRATUSAGE”参数配置为ENABLE时才生效。'
          data_source: ''
          pattern: ''
          default: 100
        ROAMFUATERMACT:
          name: '漫游用户最终配额动作指示终结方式'
          type: string
          enum:
          - TERM_SERVICE
          - TERM_SESSION
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: TERM_SERVICE
    add_userprofile_list:
      type: items
      properties:
        USERPROFILENAME:
          name: '用户模板名称'
          type: string
          maxLength: 63
          required: true
          description: '基于UserProfile粒度，将CCT绑定到特定UserProfile下。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        UPTYPE:
          name: '用户模板类型'
          type: string
          enum:
          - PCC
          - ULCL
          - UPSELECT
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: PCC
        PROFILERANGE:
          name: '模板生效范围'
          type: string
          enum:
          - ALL
          - CENTRAL
          - LOCAL
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ALL
    set_usrprofcharge_list:
      type: items
      properties:
        USRPROFNAME:
          name: '用户模板名称'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        CCTEMPLATE:
          name: '融合计费模板名称'
          type: string
          maxLength: 63
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_usrprofgroup_list:
      type: items
      properties:
        USERPROFGNAME:
          name: '用户模板组名称'
          type: string
          maxLength: 63
          required: true
          description: '将UserProfile绑定到DNN实例。  基于UserProfile粒度需要规划。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_upbindupg_list:
      type: items
      properties:
        USERPROFGNAME:
          name: '用户模板组名称'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        UPBINDTYPE:
          name: '用户模板绑定类型'
          type: string
          enum:
          - DEFAULT
          - SPECIFIC
          - ULCL
          required: true
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
        USERPROFILENAME:
          name: '用户模板名称'
          type: string
          maxLength: 63
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        CCCONFIGMODE:
          name: '计费属性配置模式'
          type: string
          enum:
          - FLATBILLING
          - HOTBILLING
          - NORMAL
          - PREPAID
          - SPECIFIC
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IMEISVSEGNAME:
          name: 'IMEISV号段名称'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IMSIMSSEGNAME:
          name: 'IMSI/MSISDN号段名称'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LOCALPCCSELECT:
          name: '本地PCC策略选择模式'
          type: string
          enum:
          - INHERIT
          - LOCAL_PCC_ACTIVE
          - LOCAL_PCC_DEACTIVE
          - LOCAL_PCC_NO_CRBN_ACT
          - LOCAL_PCC_NO_RULE_ACT
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: INHERIT
        LOCGROUPNAME:
          name: '位置组名称'
          type: string
          maxLength: 63
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PRIORITY:
          name: '优先级'
          type: integer
          minimum: 1
          maximum: 65534
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RAT:
          name: 'RAT'
          type: string
          enum:
          - EMTC
          - EUTRAN
          - GAN
          - GERAN
          - HSPA
          - NBIOT
          - NONE
          - NR
          - REDCAP
          - UTRAN
          - WLAN
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ROAMING:
          name: '漫游属性'
          type: string
          enum:
          - HOME
          - NONE
          - ROAMING
          - VISITING
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SEGGROUPNAME:
          name: 'IMSI/MSISDN/IMEISV 号段组名称'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_apn_list_1:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '基于DNN粒度，将CCT绑定到特定DNN下。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        HASVPN:
          name: '绑定VPN'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
        HASVPNIPV6:
          name: '绑定IPv6 VPN'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
        RESTORPGWSWITCH:
          name: '故障重启业务恢复功能PGW开关'
          type: string
          enum:
          - ENABLE
          - INHERIT
          - DISABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: INHERIT
        VPNINSTANCE:
          name: 'VPN实例名'
          type: string
          minLength: 1
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VPNINSTANCEIPV6:
          name: 'IPv6 VPN实例名'
          type: string
          minLength: 1
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PDTNSWITCH:
          name: 'PDTN功能开关'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
    add_apnusrprofg_list:
      type: items
      properties:
        APN:
          name: 'APN'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        USERPROFGNAME:
          name: '用户模板组名称'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
  examples:
    mod_cct_list:
    - CCTMPLTNAME: 'global'
      QHT: 5
    add_cct_list:
    - CCTMPLTNAME: 'cct_test'
      QHT: 0
      VQT: 20
      TQT: 20
      UQT: 0
      VT: 30
      MAXNUMOFCCC: 3
      PDUVOLUMELIMIT: 500
      PDUTIMELIMIT: 30
      RGVOLUMELIMIT: 500
      RGTIMELIMIT: 30
      FUATERMINATE: TERM_SERVICE
      TIMEFORMAT: LocalTime
      MAXSVCCONTAINER: 100
      SECRUTHRESHOLD: 100
      ROAMFUATERMACT: TERM_SERVICE
    add_selectcctbycc_list:
    - CCTYPE: VALUE
      CCVALUE: '0x0800'
      CCTMPLTNAME: 'cct_test'
      MASK: ''
      PRIORITY: ''
    add_cct_list_1:
    - CCTMPLTNAME: 'cct_test'
      QHT: 0
      VQT: 20
      TQT: 20
      UQT: 0
      VT: 30
      MAXNUMOFCCC: 3
      PDUVOLUMELIMIT: 500
      PDUTIMELIMIT: 30
      RGVOLUMELIMIT: 500
      RGTIMELIMIT: 30
      FUATERMINATE: TERM_SERVICE
      TIMEFORMAT: LocalTime
      MAXSVCCONTAINER: 100
      SECRUTHRESHOLD: 100
      ROAMFUATERMACT: TERM_SERVICE
    add_apn_list:
    - APN: 'apn-test'
      HASVPN: DISABLE
      HASVPNIPV6: DISABLE
      RESTORPGWSWITCH: INHERIT
      VPNINSTANCE: ''
      VPNINSTANCEIPV6: ''
      PDTNSWITCH: DISABLE
    set_apnchargectrl_list:
    - APN: 'apn-test'
      CCTEMPLATE: 'cct_test'
    add_cct_list_2:
    - CCTMPLTNAME: 'cct_test'
      QHT: 0
      VQT: 20
      TQT: 20
      UQT: 0
      VT: 30
      MAXNUMOFCCC: 3
      PDUVOLUMELIMIT: 500
      PDUTIMELIMIT: 30
      RGVOLUMELIMIT: 500
      RGTIMELIMIT: 30
      FUATERMINATE: TERM_SERVICE
      TIMEFORMAT: LocalTime
      MAXSVCCONTAINER: 100
      SECRUTHRESHOLD: 100
      ROAMFUATERMACT: TERM_SERVICE
    add_userprofile_list:
    - USERPROFILENAME: 'up_test'
      UPTYPE: PCC
      PROFILERANGE: ALL
    set_usrprofcharge_list:
    - USRPROFNAME: 'up_test'
      CCTEMPLATE: 'cct_test'
    add_usrprofgroup_list:
    - USERPROFGNAME: 'upg_test'
    add_upbindupg_list:
    - USERPROFGNAME: 'upg_test'
      UPBINDTYPE: DEFAULT
      USERPROFILENAME: 'userprofile001'
      CCCONFIGMODE: ''
      IMEISVSEGNAME: ''
      IMSIMSSEGNAME: ''
      LOCALPCCSELECT: INHERIT
      LOCGROUPNAME: ''
      PRIORITY: ''
      RAT: ''
      ROAMING: ''
      SEGGROUPNAME: ''
    add_apn_list_1:
    - APN: 'apn-test'
      HASVPN: DISABLE
      HASVPNIPV6: DISABLE
      RESTORPGWSWITCH: INHERIT
      VPNINSTANCE: ''
      VPNINSTANCEIPV6: ''
      PDTNSWITCH: DISABLE
    add_apnusrprofg_list:
    - APN: 'apn-test'
      USERPROFGNAME: 'upg_test'
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 配置全局通用CCT模板。

#### 1.1 修改系统默认配置的全局通用参数CCT模板，该模板名称为“global”。

```jinja2
{%- if is_scenario_global_cct -%}
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
{%- endif -%}
```

### 2 配置CC粒度的CCT。

#### 2.1 配置CCT模板。

```jinja2
{%- if is_scenario_cc_granularity -%}
    {%- for item in add_cct_list -%}
        ADD CCT:
        {#- --- 必选参数 --- -#}
        CCTMPLTNAME="{{item.CCTMPLTNAME}}",
        {#- --- 可选参数 --- -#}
        {%- if item.QHT is not none -%}
            QHT={{item.QHT}},
        {%- endif -%}
        {%- if item.VQT is not none -%}
            VQT={{item.VQT}},
        {%- endif -%}
        {%- if item.TQT is not none -%}
            TQT={{item.TQT}},
        {%- endif -%}
        {%- if item.UQT is not none -%}
            UQT={{item.UQT}},
        {%- endif -%}
        {%- if item.VT is not none -%}
            VT={{item.VT}},
        {%- endif -%}
        {%- if item.MAXNUMOFCCC is not none -%}
            MAXNUMOFCCC={{item.MAXNUMOFCCC}},
        {%- endif -%}
        {%- if item.PDUVOLUMELIMIT is not none -%}
            PDUVOLUMELIMIT={{item.PDUVOLUMELIMIT}},
        {%- endif -%}
        {%- if item.PDUTIMELIMIT is not none -%}
            PDUTIMELIMIT={{item.PDUTIMELIMIT}},
        {%- endif -%}
        {%- if item.RGVOLUMELIMIT is not none -%}
            RGVOLUMELIMIT={{item.RGVOLUMELIMIT}},
        {%- endif -%}
        {%- if item.RGTIMELIMIT is not none -%}
            RGTIMELIMIT={{item.RGTIMELIMIT}},
        {%- endif -%}
        {%- if item.FUATERMINATE is not none -%}
            FUATERMINATE={{item.FUATERMINATE}},
        {%- endif -%}
        {%- if item.TIMEFORMAT is not none -%}
            TIMEFORMAT={{item.TIMEFORMAT}},
        {%- endif -%}
        {%- if item.MAXSVCCONTAINER is not none -%}
            MAXSVCCONTAINER={{item.MAXSVCCONTAINER}},
        {%- endif -%}
        {%- if item.SECRUTHRESHOLD is not none -%}
            SECRUTHRESHOLD={{item.SECRUTHRESHOLD}},
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：FUATERMINATE=TERM_SERVICE 时可选 --- -#}
        {%- if item.FUATERMINATE == 'TERM_SERVICE' -%}
            {%- if item.ROAMFUATERMACT is not none -%}
                ROAMFUATERMACT={{item.ROAMFUATERMACT}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 2.2 配置计费属性。

#### 请参见配置计费属性CC。

#### 2.3 配置CCT模板绑定CC。

```jinja2
{%- if is_scenario_cc_granularity -%}
    {%- for item in add_selectcctbycc_list -%}
        ADD SELECTCCTBYCC:
        {#- --- 必选参数 --- -#}
        CCTYPE={{item.CCTYPE}},
        {#- --- 可选参数 --- -#}
        {%- if item.CCTMPLTNAME is not none -%}
            CCTMPLTNAME="{{item.CCTMPLTNAME}}",
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：CCTYPE=VALUE 时必选 --- -#}
        {%- if item.CCTYPE == 'VALUE' -%}
            CCVALUE="{{item.CCVALUE}}",
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：CCTYPE=VALUE 时可选 --- -#}
        {%- if item.CCTYPE == 'VALUE' -%}
            {%- if item.MASK is not none -%}
                MASK="{{item.MASK}}",
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：CCTYPE=VALUE 时可选 --- -#}
        {%- if item.CCTYPE == 'VALUE' -%}
            {%- if item.PRIORITY is not none -%}
                PRIORITY={{item.PRIORITY}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 3 配置DNN粒度的CCT。

#### 3.1 配置CCT模板。

```jinja2
{%- if is_scenario_dnn_granularity -%}
    {%- for item in add_cct_list_1 -%}
        ADD CCT:
        {#- --- 必选参数 --- -#}
        CCTMPLTNAME="{{item.CCTMPLTNAME}}",
        {#- --- 可选参数 --- -#}
        {%- if item.QHT is not none -%}
            QHT={{item.QHT}},
        {%- endif -%}
        {%- if item.VQT is not none -%}
            VQT={{item.VQT}},
        {%- endif -%}
        {%- if item.TQT is not none -%}
            TQT={{item.TQT}},
        {%- endif -%}
        {%- if item.UQT is not none -%}
            UQT={{item.UQT}},
        {%- endif -%}
        {%- if item.VT is not none -%}
            VT={{item.VT}},
        {%- endif -%}
        {%- if item.MAXNUMOFCCC is not none -%}
            MAXNUMOFCCC={{item.MAXNUMOFCCC}},
        {%- endif -%}
        {%- if item.PDUVOLUMELIMIT is not none -%}
            PDUVOLUMELIMIT={{item.PDUVOLUMELIMIT}},
        {%- endif -%}
        {%- if item.PDUTIMELIMIT is not none -%}
            PDUTIMELIMIT={{item.PDUTIMELIMIT}},
        {%- endif -%}
        {%- if item.RGVOLUMELIMIT is not none -%}
            RGVOLUMELIMIT={{item.RGVOLUMELIMIT}},
        {%- endif -%}
        {%- if item.RGTIMELIMIT is not none -%}
            RGTIMELIMIT={{item.RGTIMELIMIT}},
        {%- endif -%}
        {%- if item.FUATERMINATE is not none -%}
            FUATERMINATE={{item.FUATERMINATE}},
        {%- endif -%}
        {%- if item.TIMEFORMAT is not none -%}
            TIMEFORMAT={{item.TIMEFORMAT}},
        {%- endif -%}
        {%- if item.MAXSVCCONTAINER is not none -%}
            MAXSVCCONTAINER={{item.MAXSVCCONTAINER}},
        {%- endif -%}
        {%- if item.SECRUTHRESHOLD is not none -%}
            SECRUTHRESHOLD={{item.SECRUTHRESHOLD}},
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：FUATERMINATE=TERM_SERVICE 时可选 --- -#}
        {%- if item.FUATERMINATE == 'TERM_SERVICE' -%}
            {%- if item.ROAMFUATERMACT is not none -%}
                ROAMFUATERMACT={{item.ROAMFUATERMACT}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 3.2 配置DNN。

```jinja2
{%- if is_scenario_dnn_granularity -%}
    {%- for item in add_apn_list -%}
        ADD APN:
        {#- --- 必选参数 --- -#}
        APN="{{item.APN}}",
        {#- --- 可选参数 --- -#}
        {%- if item.HASVPN is not none -%}
            HASVPN={{item.HASVPN}},
        {%- endif -%}
        {%- if item.HASVPNIPV6 is not none -%}
            HASVPNIPV6={{item.HASVPNIPV6}},
        {%- endif -%}
        {%- if item.RESTORPGWSWITCH is not none -%}
            RESTORPGWSWITCH={{item.RESTORPGWSWITCH}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：HASVPN=ENABLE 时必选 --- -#}
        {%- if item.HASVPN == 'ENABLE' -%}
            VPNINSTANCE="{{item.VPNINSTANCE}}",
        {%- endif -%}
        {#- --- 条件必选：HASVPNIPV6=ENABLE 时必选 --- -#}
        {%- if item.HASVPNIPV6 == 'ENABLE' -%}
            VPNINSTANCEIPV6="{{item.VPNINSTANCEIPV6}}",
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：RESTORPGWSWITCH=ENABLE 时可选 --- -#}
        {%- if item.RESTORPGWSWITCH == 'ENABLE' -%}
            {%- if item.PDTNSWITCH is not none -%}
                PDTNSWITCH={{item.PDTNSWITCH}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 3.3 配置CCT模板绑定DNN。

```jinja2
{%- if is_scenario_dnn_granularity -%}
    {%- for item in set_apnchargectrl_list -%}
        SET APNCHARGECTRL:
        {#- --- 必选参数 --- -#}
        APN="{{item.APN}}",
        {#- --- 可选参数 --- -#}
        {%- if item.CCTEMPLATE is not none -%}
            CCTEMPLATE="{{item.CCTEMPLATE}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 4 配置UserProfile粒度的CCT。

#### 4.1 配置CCT模板。

```jinja2
{%- if is_scenario_userprofile_granularity -%}
    {%- for item in add_cct_list_2 -%}
        ADD CCT:
        {#- --- 必选参数 --- -#}
        CCTMPLTNAME="{{item.CCTMPLTNAME}}",
        {#- --- 可选参数 --- -#}
        {%- if item.QHT is not none -%}
            QHT={{item.QHT}},
        {%- endif -%}
        {%- if item.VQT is not none -%}
            VQT={{item.VQT}},
        {%- endif -%}
        {%- if item.TQT is not none -%}
            TQT={{item.TQT}},
        {%- endif -%}
        {%- if item.UQT is not none -%}
            UQT={{item.UQT}},
        {%- endif -%}
        {%- if item.VT is not none -%}
            VT={{item.VT}},
        {%- endif -%}
        {%- if item.MAXNUMOFCCC is not none -%}
            MAXNUMOFCCC={{item.MAXNUMOFCCC}},
        {%- endif -%}
        {%- if item.PDUVOLUMELIMIT is not none -%}
            PDUVOLUMELIMIT={{item.PDUVOLUMELIMIT}},
        {%- endif -%}
        {%- if item.PDUTIMELIMIT is not none -%}
            PDUTIMELIMIT={{item.PDUTIMELIMIT}},
        {%- endif -%}
        {%- if item.RGVOLUMELIMIT is not none -%}
            RGVOLUMELIMIT={{item.RGVOLUMELIMIT}},
        {%- endif -%}
        {%- if item.RGTIMELIMIT is not none -%}
            RGTIMELIMIT={{item.RGTIMELIMIT}},
        {%- endif -%}
        {%- if item.FUATERMINATE is not none -%}
            FUATERMINATE={{item.FUATERMINATE}},
        {%- endif -%}
        {%- if item.TIMEFORMAT is not none -%}
            TIMEFORMAT={{item.TIMEFORMAT}},
        {%- endif -%}
        {%- if item.MAXSVCCONTAINER is not none -%}
            MAXSVCCONTAINER={{item.MAXSVCCONTAINER}},
        {%- endif -%}
        {%- if item.SECRUTHRESHOLD is not none -%}
            SECRUTHRESHOLD={{item.SECRUTHRESHOLD}},
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：FUATERMINATE=TERM_SERVICE 时可选 --- -#}
        {%- if item.FUATERMINATE == 'TERM_SERVICE' -%}
            {%- if item.ROAMFUATERMACT is not none -%}
                ROAMFUATERMACT={{item.ROAMFUATERMACT}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 4.2 配置UserProfile，将CCT绑定到UserProfile上。

##### 4.2.1 配置UserProfile。

```jinja2
{%- if is_scenario_userprofile_granularity -%}
    {%- for item in add_userprofile_list -%}
        ADD USERPROFILE:
        {#- --- 必选参数 --- -#}
        USERPROFILENAME="{{item.USERPROFILENAME}}",
        UPTYPE={{item.UPTYPE}},
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：UPTYPE=PCC 时可选 --- -#}
        {%- if item.UPTYPE == 'PCC' -%}
            {%- if item.PROFILERANGE is not none -%}
                PROFILERANGE={{item.PROFILERANGE}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 4.2.2 将CCT绑定到UserProfile上。

```jinja2
{%- if is_scenario_userprofile_granularity -%}
    {%- for item in set_usrprofcharge_list -%}
        SET USRPROFCHARGE:
        {#- --- 必选参数 --- -#}
        USRPROFNAME="{{item.USRPROFNAME}}",
        {#- --- 可选参数 --- -#}
        {%- if item.CCTEMPLATE is not none -%}
            CCTEMPLATE="{{item.CCTEMPLATE}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 4.3 配置UserProfile组及DNN实例。

##### 4.3.1 配置UserProfile组，将UserProfile绑定到UserProfile组。

```jinja2
{%- if is_scenario_userprofile_granularity -%}
    {%- for item in add_usrprofgroup_list -%}
        ADD USRPROFGROUP:
        {#- --- 必选参数 --- -#}
        USERPROFGNAME="{{item.USERPROFGNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_userprofile_granularity -%}
    {%- for item in add_upbindupg_list -%}
        ADD UPBINDUPG:
        {#- --- 必选参数 --- -#}
        USERPROFGNAME="{{item.USERPROFGNAME}}",
        UPBINDTYPE={{item.UPBINDTYPE}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：UPBINDTYPE=SPECIFIC/DEFAULT/ULCL 时必选 --- -#}
        {%- if item.UPBINDTYPE in ['SPECIFIC', 'DEFAULT', 'ULCL'] -%}
            USERPROFILENAME="{{item.USERPROFILENAME}}",
        {%- endif -%}
        {#- --- 条件必选：UPBINDTYPE=SPECIFIC 时必选 --- -#}
        {%- if item.UPBINDTYPE == 'SPECIFIC' -%}
            PRIORITY={{item.PRIORITY}},
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：UPBINDTYPE=SPECIFIC 时可选 --- -#}
        {%- if item.UPBINDTYPE == 'SPECIFIC' -%}
            {%- if item.CCCONFIGMODE is not none -%}
                CCCONFIGMODE={{item.CCCONFIGMODE}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：UPBINDTYPE=SPECIFIC 时可选 --- -#}
        {%- if item.UPBINDTYPE == 'SPECIFIC' -%}
            {%- if item.IMEISVSEGNAME is not none -%}
                IMEISVSEGNAME="{{item.IMEISVSEGNAME}}",
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：UPBINDTYPE=SPECIFIC 时可选 --- -#}
        {%- if item.UPBINDTYPE == 'SPECIFIC' -%}
            {%- if item.IMSIMSSEGNAME is not none -%}
                IMSIMSSEGNAME="{{item.IMSIMSSEGNAME}}",
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：UPBINDTYPE=SPECIFIC/DEFAULT 时可选 --- -#}
        {%- if item.UPBINDTYPE in ['SPECIFIC', 'DEFAULT'] -%}
            {%- if item.LOCALPCCSELECT is not none -%}
                LOCALPCCSELECT={{item.LOCALPCCSELECT}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：UPBINDTYPE=SPECIFIC 时可选 --- -#}
        {%- if item.UPBINDTYPE == 'SPECIFIC' -%}
            {%- if item.LOCGROUPNAME is not none -%}
                LOCGROUPNAME="{{item.LOCGROUPNAME}}",
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：UPBINDTYPE=SPECIFIC 时可选 --- -#}
        {%- if item.UPBINDTYPE == 'SPECIFIC' -%}
            {%- if item.RAT is not none -%}
                RAT={{item.RAT}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：UPBINDTYPE=SPECIFIC 时可选 --- -#}
        {%- if item.UPBINDTYPE == 'SPECIFIC' -%}
            {%- if item.ROAMING is not none -%}
                ROAMING={{item.ROAMING}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：UPBINDTYPE=SPECIFIC 时可选 --- -#}
        {%- if item.UPBINDTYPE == 'SPECIFIC' -%}
            {%- if item.SEGGROUPNAME is not none -%}
                SEGGROUPNAME="{{item.SEGGROUPNAME}}",
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 4.3.2 配置DNN实例，将UserProifle组绑定到DNN实例。

```jinja2
{%- if is_scenario_userprofile_granularity -%}
    {%- for item in add_apn_list_1 -%}
        ADD APN:
        {#- --- 必选参数 --- -#}
        APN="{{item.APN}}",
        {#- --- 可选参数 --- -#}
        {%- if item.HASVPN is not none -%}
            HASVPN={{item.HASVPN}},
        {%- endif -%}
        {%- if item.HASVPNIPV6 is not none -%}
            HASVPNIPV6={{item.HASVPNIPV6}},
        {%- endif -%}
        {%- if item.RESTORPGWSWITCH is not none -%}
            RESTORPGWSWITCH={{item.RESTORPGWSWITCH}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：HASVPN=ENABLE 时必选 --- -#}
        {%- if item.HASVPN == 'ENABLE' -%}
            VPNINSTANCE="{{item.VPNINSTANCE}}",
        {%- endif -%}
        {#- --- 条件必选：HASVPNIPV6=ENABLE 时必选 --- -#}
        {%- if item.HASVPNIPV6 == 'ENABLE' -%}
            VPNINSTANCEIPV6="{{item.VPNINSTANCEIPV6}}",
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：RESTORPGWSWITCH=ENABLE 时可选 --- -#}
        {%- if item.RESTORPGWSWITCH == 'ENABLE' -%}
            {%- if item.PDTNSWITCH is not none -%}
                PDTNSWITCH={{item.PDTNSWITCH}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_userprofile_granularity -%}
    {%- for item in add_apnusrprofg_list -%}
        ADD APNUSRPROFG:
        {#- --- 必选参数 --- -#}
        APN="{{item.APN}}",
        USERPROFGNAME="{{item.USERPROFGNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 每个DNN实例只能绑定一个UserProfile组。如UserProfile组和DNN实例已配置且已绑定，本步骤只需执行**ADD UPBINDUPG**命令，将UserProfile绑定到UserProfile组即可。


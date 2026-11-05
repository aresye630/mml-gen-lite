---
id: ''
name: 配置普通在线计费实例
ne_type: UNC
type: feature
description: 普通在线计费不区分业务内容进行统一计费，在线计费的计费粒度有四种：UserProfile、APN、计费属性Charging Characteristics和全局，优先级依次降低。如果高一级别的计费参数没有配置，则继承低一级别的计费参数。  适用于GGSN、PGW-C。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","计费管理功能","WSFD-109001 Gy/Diameter在线计费","激活Gy/Diameter在线计费","配置普通在线计费实例"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
普通在线计费不区分业务内容进行统一计费，在线计费的计费粒度有四种：UserProfile、APN、计费属性Charging Characteristics和全局，优先级依次降低。如果高一级别的计费参数没有配置，则继承低一级别的计费参数。适用于GGSN、PGW-C。

## 必备事项
前提条件

* 请仔细阅读Ga/Gy接口离线/在线计费。
* 完成配置到OCS的数据(静态路由+BFD组网)。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    add_chargechar_list:
      type: items
      properties:
        CCNAME:
          name: '计费属性名称'
          type: string
          maxLength: 31
          required: true
          description: '计费属性。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        HOME:
          name: '本地用户计费属性'
          type: string
          maxLength: 6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: '0x0800'
        ROAM:
          name: '漫游用户计费属性'
          type: string
          maxLength: 6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: '0x0800'
        VISIT:
          name: '拜访用户计费属性'
          type: string
          maxLength: 6
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: '0x0800'
        HOMESGSN:
          name: '本地用户使用Serving Node计费属性'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ENABLE
        ROAMSGSN:
          name: '漫游用户使用Serving Node计费属性'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ENABLE
        VISITSGSN:
          name: '拜访用户使用Serving Node计费属性'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ENABLE
    set_chargectrl_list:
      type: items
      properties:
        HOMEONLINE:
          name: '归属地在线用户计费控制'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '用来控制是否基于用户漫游、拜访、本地属性来提供在线计费。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        VISITONLINE:
          name: '拜访地在线计费用户计费控制'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        ROAMONLINE:
          name: '漫游在线计费用户计费控制'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '全网规划'
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
          data_source: '本端规划'
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
          data_source: '本端规划'
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
          data_source: '本端规划'
          pattern: ''
          default: ''
        ONLINERG:
          name: '在线计费组'
          type: integer
          minimum: 0
          maximum: 4294967294
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        ONLINESID:
          name: '在线业务标识'
          type: integer
          minimum: 0
          maximum: 4294967294
          required: false
          description: ''
          data_source: '本端规划'
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
    add_urrgroup_list:
      type: items
      properties:
        URRGROUPNAME:
          name: '使用量上报规则组名称'
          type: string
          maxLength: 31
          required: true
          description: '配置URR组，将上下行URR绑定到URR组上。  如果上下行使用不同的URR，则两者必须同时为在线计费或离线计费。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        UPURRNAME1:
          name: '上行发起URR名称1'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        DOWNURRNAME1:
          name: '下行发起URR名称1'
          type: string
          maxLength: 31
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
        PRIOCSGRPNAME:
          name: '主OCS组名称'
          type: string
          maxLength: 63
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_dcctemplate_list:
      type: items
      properties:
        DCCTMPLTNAME:
          name: 'DCC模板名称'
          type: string
          maxLength: 63
          required: true
          description: '新增DCC在线计费模板，用于配置在线计费相关属性。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        QCT:
          name: '配额空耗时间门限值（秒）'
          type: integer
          minimum:
          - 0
          - 5
          - 4294967295
          maximum:
          - 0
          - 200
          - 4294967295
          required: false
          description: '配额空耗时间标识如何统计业务时长。QCT=0表示连续统计业务时长。'
          data_source: '本端规划'
          pattern: ''
          default: 4294967295
        QHT:
          name: '配额空闲时间门限值（秒）'
          type: integer
          minimum:
          - 0
          - 5
          - 4294967295
          maximum:
          - 0
          - 3600
          - 4294967295
          required: false
          description: '配额空闲时间监控业务暂停的时长。QHT=0表示QHT不生效。'
          data_source: '本端规划'
          pattern: ''
          default: 4294967295
        VQT:
          name: '流量阈值触发百分比（%）'
          type: integer
          minimum:
          - 0
          - 4294967295
          maximum:
          - 50
          - 4294967295
          required: false
          description: '标识业务剩余流量配额达到VQT时，触发GGSN/PGW-C上报CCR消息请求新配额，收到新配额后可以继续之前的业务。'
          data_source: '本端规划'
          pattern: ''
          default: 4294967295
        TQT:
          name: '时间阈值触发百分比（%）'
          type: integer
          minimum:
          - 0
          - 4294967295
          maximum:
          - 50
          - 4294967295
          required: false
          description: '标识业务剩余时长配额达到TQT时，触发GGSN/PGW-C上报CCR消息请求新配额，收到新配额后可以继续之前的业务。'
          data_source: '本端规划'
          pattern: ''
          default: 4294967295
        CCRINITRGNUM:
          name: '指定CCR-I消息中携带RG的个数'
          type: integer
          minimum:
          - 0
          - 4294967295
          maximum:
          - 10
          - 4294967295
          required: false
          description: '用户激活时发送的CCR-I消息中携带RG的个数。'
          data_source: '本端规划'
          pattern: ''
          default: 4294967295
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
          description: 'Tx定时器超时后处理动作。'
          data_source: '本端规划'
          pattern: ''
          default: INHERIT
        SGSNTRIGGER:
          name: 'SGSN变化触发使能开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          - INHERIT
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: INHERIT
        SERVICETRIGGER:
          name: '业务触发请求使能开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          - INHERIT
          required: false
          description: '应用新业务是否发送CCR。'
          data_source: '本端规划'
          pattern: ''
          default: INHERIT
        VALIDTIME:
          name: '在线配额有效时长（分）'
          type: integer
          minimum:
          - 0
          - 5
          - 4294967295
          maximum:
          - 0
          - 1440
          - 4294967295
          required: false
          description: '标识配额有效时长，超时后触发GGSN/PGW-C上报CCR消息。'
          data_source: '本端规划'
          pattern: ''
          default: 4294967295
        PRIOCSGRPNAME:
          name: '主OCS组名称'
          type: string
          maxLength: 63
          required: false
          description: '配置主从OCS组。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_diamlocinfo_list:
      type: items
      properties:
        HOSTNAME:
          name: '本端主机名'
          type: string
          maxLength: 127
          required: true
          description: 'GGSN/PGW-C信息。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        REALMNAME:
          name: '本端域名'
          type: string
          maxLength: 127
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        PRODUCTNAME:
          name: '产品名称'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_ocs_list:
      type: items
      properties:
        OCSHOSTNAME:
          name: 'Ocs主机名称'
          type: string
          maxLength: 127
          required: true
          description: '配置OCS。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        REALMNAME:
          name: 'Ocs域名'
          type: string
          maxLength: 127
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_diampeeraddr_list:
      type: items
      properties:
        HOSTNAME:
          name: '主机名称'
          type: string
          maxLength: 127
          required: true
          description: 'OCS信息。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        ADDRTYPE:
          name: '地址类型'
          type: string
          enum:
          - IPv4
          - IPv6
          - SCTP
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPV4ADDRESS:
          name: 'IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        PORT:
          name: '端口号'
          type: integer
          minimum: 1
          maximum: 65534
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: 3868
        IPV6ADDRESS:
          name: 'IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SCTPENDPOINT:
          name: 'SCTP端点名称'
          type: string
          maxLength: 63
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_ocsgroup_list:
      type: items
      properties:
        OCSGRPNAME:
          name: 'Ocs组名称'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_ocsbinding_list:
      type: items
      properties:
        OCSGRPNAME:
          name: 'Ocs组名称'
          type: string
          maxLength: 63
          required: true
          description: '增加OCS绑定关系。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        OCSHOSTNAME:
          name: 'Ocs主机名称'
          type: string
          maxLength: 127
          required: true
          description: ''
          data_source: '已配置数据中获取'
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
          description: '新增DCC在线计费模板，用于配置在线计费相关属性。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        QCT:
          name: '配额空耗时间门限值（秒）'
          type: integer
          minimum:
          - 0
          - 5
          - 4294967295
          maximum:
          - 0
          - 200
          - 4294967295
          required: false
          description: '配额空耗时间标识如何统计业务时长。QCT=0表示连续统计业务时长。'
          data_source: '本端规划'
          pattern: ''
          default: 4294967295
        QHT:
          name: '配额空闲时间门限值（秒）'
          type: integer
          minimum:
          - 0
          - 5
          - 4294967295
          maximum:
          - 0
          - 3600
          - 4294967295
          required: false
          description: '配额空闲时间监控业务暂停的时长。QHT=0表示QHT不生效。'
          data_source: '本端规划'
          pattern: ''
          default: 4294967295
        VQT:
          name: '流量阈值触发百分比（%）'
          type: integer
          minimum:
          - 0
          - 4294967295
          maximum:
          - 50
          - 4294967295
          required: false
          description: '标识业务剩余流量配额达到VQT时，触发GGSN/PGW-C上报CCR消息请求新配额，收到新配额后可以继续之前的业务。'
          data_source: '本端规划'
          pattern: ''
          default: 4294967295
        TQT:
          name: '时间阈值触发百分比（%）'
          type: integer
          minimum:
          - 0
          - 4294967295
          maximum:
          - 50
          - 4294967295
          required: false
          description: '标识业务剩余时长配额达到TQT时，触发GGSN/PGW-C上报CCR消息请求新配额，收到新配额后可以继续之前的业务。'
          data_source: '本端规划'
          pattern: ''
          default: 4294967295
        CCRINITRGNUM:
          name: '指定CCR-I消息中携带RG的个数'
          type: integer
          minimum:
          - 0
          - 4294967295
          maximum:
          - 10
          - 4294967295
          required: false
          description: '用户激活时发送的CCR-I消息中携带RG的个数。'
          data_source: '本端规划'
          pattern: ''
          default: 4294967295
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
          description: 'Tx定时器超时后处理动作。'
          data_source: '本端规划'
          pattern: ''
          default: INHERIT
        SGSNTRIGGER:
          name: 'SGSN变化触发使能开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          - INHERIT
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: INHERIT
        SERVICETRIGGER:
          name: '业务触发请求使能开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          - INHERIT
          required: false
          description: '应用新业务是否发送CCR。'
          data_source: '本端规划'
          pattern: ''
          default: INHERIT
        VALIDTIME:
          name: '在线配额有效时长（分）'
          type: integer
          minimum:
          - 0
          - 5
          - 4294967295
          maximum:
          - 0
          - 1440
          - 4294967295
          required: false
          description: '标识配额有效时长，超时后触发GGSN/PGW-C上报CCR消息。'
          data_source: '本端规划'
          pattern: ''
          default: 4294967295
        PRIOCSGRPNAME:
          name: '主OCS组名称'
          type: string
          maxLength: 63
          required: false
          description: '配置主从OCS组。'
          data_source: '本端规划'
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
          description: '新增DCC在线计费模板，用于配置在线计费相关属性。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        QCT:
          name: '配额空耗时间门限值（秒）'
          type: integer
          minimum:
          - 0
          - 5
          - 4294967295
          maximum:
          - 0
          - 200
          - 4294967295
          required: false
          description: '配额空耗时间标识如何统计业务时长。QCT=0表示连续统计业务时长。'
          data_source: '本端规划'
          pattern: ''
          default: 4294967295
        QHT:
          name: '配额空闲时间门限值（秒）'
          type: integer
          minimum:
          - 0
          - 5
          - 4294967295
          maximum:
          - 0
          - 3600
          - 4294967295
          required: false
          description: '配额空闲时间监控业务暂停的时长。QHT=0表示QHT不生效。'
          data_source: '本端规划'
          pattern: ''
          default: 4294967295
        VQT:
          name: '流量阈值触发百分比（%）'
          type: integer
          minimum:
          - 0
          - 4294967295
          maximum:
          - 50
          - 4294967295
          required: false
          description: '标识业务剩余流量配额达到VQT时，触发GGSN/PGW-C上报CCR消息请求新配额，收到新配额后可以继续之前的业务。'
          data_source: '本端规划'
          pattern: ''
          default: 4294967295
        TQT:
          name: '时间阈值触发百分比（%）'
          type: integer
          minimum:
          - 0
          - 4294967295
          maximum:
          - 50
          - 4294967295
          required: false
          description: '标识业务剩余时长配额达到TQT时，触发GGSN/PGW-C上报CCR消息请求新配额，收到新配额后可以继续之前的业务。'
          data_source: '本端规划'
          pattern: ''
          default: 4294967295
        CCRINITRGNUM:
          name: '指定CCR-I消息中携带RG的个数'
          type: integer
          minimum:
          - 0
          - 4294967295
          maximum:
          - 10
          - 4294967295
          required: false
          description: '用户激活时发送的CCR-I消息中携带RG的个数。'
          data_source: '本端规划'
          pattern: ''
          default: 4294967295
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
          description: 'Tx定时器超时后处理动作。'
          data_source: '本端规划'
          pattern: ''
          default: INHERIT
        SGSNTRIGGER:
          name: 'SGSN变化触发使能开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          - INHERIT
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: INHERIT
        SERVICETRIGGER:
          name: '业务触发请求使能开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          - INHERIT
          required: false
          description: '应用新业务是否发送CCR。'
          data_source: '本端规划'
          pattern: ''
          default: INHERIT
        VALIDTIME:
          name: '在线配额有效时长（分）'
          type: integer
          minimum:
          - 0
          - 5
          - 4294967295
          maximum:
          - 0
          - 1440
          - 4294967295
          required: false
          description: '标识配额有效时长，超时后触发GGSN/PGW-C上报CCR消息。'
          data_source: '本端规划'
          pattern: ''
          default: 4294967295
        PRIOCSGRPNAME:
          name: '主OCS组名称'
          type: string
          maxLength: 63
          required: false
          description: '配置主从OCS组。'
          data_source: '本端规划'
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
          description: '新增DCC在线计费模板，用于配置在线计费相关属性。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        QCT:
          name: '配额空耗时间门限值（秒）'
          type: integer
          minimum:
          - 0
          - 5
          - 4294967295
          maximum:
          - 0
          - 200
          - 4294967295
          required: false
          description: '配额空耗时间标识如何统计业务时长。QCT=0表示连续统计业务时长。'
          data_source: '本端规划'
          pattern: ''
          default: 4294967295
        QHT:
          name: '配额空闲时间门限值（秒）'
          type: integer
          minimum:
          - 0
          - 5
          - 4294967295
          maximum:
          - 0
          - 3600
          - 4294967295
          required: false
          description: '配额空闲时间监控业务暂停的时长。QHT=0表示QHT不生效。'
          data_source: '本端规划'
          pattern: ''
          default: 4294967295
        VQT:
          name: '流量阈值触发百分比（%）'
          type: integer
          minimum:
          - 0
          - 4294967295
          maximum:
          - 50
          - 4294967295
          required: false
          description: '标识业务剩余流量配额达到VQT时，触发GGSN/PGW-C上报CCR消息请求新配额，收到新配额后可以继续之前的业务。'
          data_source: '本端规划'
          pattern: ''
          default: 4294967295
        TQT:
          name: '时间阈值触发百分比（%）'
          type: integer
          minimum:
          - 0
          - 4294967295
          maximum:
          - 50
          - 4294967295
          required: false
          description: '标识业务剩余时长配额达到TQT时，触发GGSN/PGW-C上报CCR消息请求新配额，收到新配额后可以继续之前的业务。'
          data_source: '本端规划'
          pattern: ''
          default: 4294967295
        CCRINITRGNUM:
          name: '指定CCR-I消息中携带RG的个数'
          type: integer
          minimum:
          - 0
          - 4294967295
          maximum:
          - 10
          - 4294967295
          required: false
          description: '用户激活时发送的CCR-I消息中携带RG的个数。'
          data_source: '本端规划'
          pattern: ''
          default: 4294967295
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
          description: 'Tx定时器超时后处理动作。'
          data_source: '本端规划'
          pattern: ''
          default: INHERIT
        SGSNTRIGGER:
          name: 'SGSN变化触发使能开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          - INHERIT
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: INHERIT
        SERVICETRIGGER:
          name: '业务触发请求使能开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          - INHERIT
          required: false
          description: '应用新业务是否发送CCR。'
          data_source: '本端规划'
          pattern: ''
          default: INHERIT
        VALIDTIME:
          name: '在线配额有效时长（分）'
          type: integer
          minimum:
          - 0
          - 5
          - 4294967295
          maximum:
          - 0
          - 1440
          - 4294967295
          required: false
          description: '标识配额有效时长，超时后触发GGSN/PGW-C上报CCR消息。'
          data_source: '本端规划'
          pattern: ''
          default: 4294967295
        PRIOCSGRPNAME:
          name: '主OCS组名称'
          type: string
          maxLength: 63
          required: false
          description: '配置主从OCS组。'
          data_source: '本端规划'
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
          description: 'DCC在线计费模板Tx定时器。'
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
          data_source: '本端规划'
          pattern: ''
          default: ''
        TXTIMER:
          name: 'Tx定时器时长'
          type: integer
          minimum:
          - 1
          - 4294967295
          maximum:
          - 20
          - 4294967295
          required: false
          description: ''
          data_source: '本端规划'
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
    add_dcctemplate_list_4:
      type: items
      properties:
        DCCTMPLTNAME:
          name: 'DCC模板名称'
          type: string
          maxLength: 63
          required: true
          description: '新增DCC在线计费模板，用于配置在线计费相关属性。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        QCT:
          name: '配额空耗时间门限值（秒）'
          type: integer
          minimum:
          - 0
          - 5
          - 4294967295
          maximum:
          - 0
          - 200
          - 4294967295
          required: false
          description: '配额空耗时间标识如何统计业务时长。QCT=0表示连续统计业务时长。'
          data_source: '本端规划'
          pattern: ''
          default: 4294967295
        QHT:
          name: '配额空闲时间门限值（秒）'
          type: integer
          minimum:
          - 0
          - 5
          - 4294967295
          maximum:
          - 0
          - 3600
          - 4294967295
          required: false
          description: '配额空闲时间监控业务暂停的时长。QHT=0表示QHT不生效。'
          data_source: '本端规划'
          pattern: ''
          default: 4294967295
        VQT:
          name: '流量阈值触发百分比（%）'
          type: integer
          minimum:
          - 0
          - 4294967295
          maximum:
          - 50
          - 4294967295
          required: false
          description: '标识业务剩余流量配额达到VQT时，触发GGSN/PGW-C上报CCR消息请求新配额，收到新配额后可以继续之前的业务。'
          data_source: '本端规划'
          pattern: ''
          default: 4294967295
        TQT:
          name: '时间阈值触发百分比（%）'
          type: integer
          minimum:
          - 0
          - 4294967295
          maximum:
          - 50
          - 4294967295
          required: false
          description: '标识业务剩余时长配额达到TQT时，触发GGSN/PGW-C上报CCR消息请求新配额，收到新配额后可以继续之前的业务。'
          data_source: '本端规划'
          pattern: ''
          default: 4294967295
        CCRINITRGNUM:
          name: '指定CCR-I消息中携带RG的个数'
          type: integer
          minimum:
          - 0
          - 4294967295
          maximum:
          - 10
          - 4294967295
          required: false
          description: '用户激活时发送的CCR-I消息中携带RG的个数。'
          data_source: '本端规划'
          pattern: ''
          default: 4294967295
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
          description: 'Tx定时器超时后处理动作。'
          data_source: '本端规划'
          pattern: ''
          default: INHERIT
        SGSNTRIGGER:
          name: 'SGSN变化触发使能开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          - INHERIT
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: INHERIT
        SERVICETRIGGER:
          name: '业务触发请求使能开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          - INHERIT
          required: false
          description: '应用新业务是否发送CCR。'
          data_source: '本端规划'
          pattern: ''
          default: INHERIT
        VALIDTIME:
          name: '在线配额有效时长（分）'
          type: integer
          minimum:
          - 0
          - 5
          - 4294967295
          maximum:
          - 0
          - 1440
          - 4294967295
          required: false
          description: '标识配额有效时长，超时后触发GGSN/PGW-C上报CCR消息。'
          data_source: '本端规划'
          pattern: ''
          default: 4294967295
        PRIOCSGRPNAME:
          name: '主OCS组名称'
          type: string
          maxLength: 63
          required: false
          description: '配置主从OCS组。'
          data_source: '本端规划'
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
          description: 'CCA消息中MSCC层返回异常消息码的处理动作。'
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
    set_apnchargectrl_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          maxLength: 63
          required: true
          description: '配置APN实例得在线计费方式。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        ONLINESW:
          name: '在线计费开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          - INHERIT
          required: false
          description: ''
          data_source: '本端规划'
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
        CCNAME:
          name: '计费属性名称'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
  examples:
    add_chargechar_list:
    - CCNAME: 'testchgcha'
      HOME: '0x0800'
      ROAM: '0x0800'
      VISIT: '0x0800'
      HOMESGSN: ENABLE
      ROAMSGSN: ENABLE
      VISITSGSN: ENABLE
    set_chargectrl_list:
    - HOMEONLINE: ENABLE
      VISITONLINE: ENABLE
      ROAMONLINE: ENABLE
    add_urr_list:
    - URRNAME: 'onlineURR'
      URRID: 1100
      USAGERPTMODE: ONLINE
      ONLCOMPOUNDTYPE: RGSID
      ONLINERG: 10
      ONLINESID: 20
      MONITORINGKEY: ''
      N40AGESW: ENABLE
      OFCSRVTMPLNAME: ''
      OFFCOMPOUNDTYPE: ''
      OFFMETERINGTYPE: ''
      ONLMETERINGTYPE: ''
      REDIRENDTOKEN: ''
    add_urrgroup_list:
    - URRGROUPNAME: 'urrgroup1'
      UPURRNAME1: 'onlineURR'
      DOWNURRNAME1: 'onlineURR'
    mod_dcctemplate_list:
    - DCCTMPLTNAME: 'dcc-test'
      PRIOCSGRPNAME: 'ocs-grp'
    add_dcctemplate_list:
    - DCCTMPLTNAME: 'dcc-test'
      QCT: 0
      QHT: 0
      VQT: 20
      TQT: 20
      CCRINITRGNUM: 5
      CCFH: TERMINATE
      SGSNTRIGGER: ENABLE
      SERVICETRIGGER: ENABLE
      VALIDTIME: 30
      PRIOCSGRPNAME: 'ocs_host'
    add_diamlocinfo_list:
    - HOSTNAME: 'pgw1'
      REALMNAME: 'huawei.com'
      PRODUCTNAME: 'unc@huawei.com'
    add_ocs_list:
    - OCSHOSTNAME: 'ocs_host'
      REALMNAME: 'ocs_realm'
    add_diampeeraddr_list:
    - HOSTNAME: 'ocs_host'
      ADDRTYPE: IPv4
      IPV4ADDRESS: '192.168.40.10'
      PORT: 3868
      IPV6ADDRESS: ''
      SCTPENDPOINT: ''
    add_ocsgroup_list:
    - OCSGRPNAME: 'ocs-grp'
    add_ocsbinding_list:
    - OCSGRPNAME: 'ocs-grp'
      OCSHOSTNAME: 'ocs_host'
    add_dcctemplate_list_1:
    - DCCTMPLTNAME: 'dcc-test'
      QCT: 0
      QHT: 0
      VQT: 20
      TQT: 20
      CCRINITRGNUM: 5
      CCFH: TERMINATE
      SGSNTRIGGER: ENABLE
      SERVICETRIGGER: ENABLE
      VALIDTIME: 30
      PRIOCSGRPNAME: 'ocs_host'
    add_dcctemplate_list_2:
    - DCCTMPLTNAME: 'dcc-test'
      QCT: 0
      QHT: 0
      VQT: 20
      TQT: 20
      CCRINITRGNUM: 5
      CCFH: TERMINATE
      SGSNTRIGGER: ENABLE
      SERVICETRIGGER: ENABLE
      VALIDTIME: 30
      PRIOCSGRPNAME: 'ocs_host'
    add_dcctemplate_list_3:
    - DCCTMPLTNAME: 'dcc-test'
      QCT: 0
      QHT: 0
      VQT: 20
      TQT: 20
      CCRINITRGNUM: 5
      CCFH: TERMINATE
      SGSNTRIGGER: ENABLE
      SERVICETRIGGER: ENABLE
      VALIDTIME: 30
      PRIOCSGRPNAME: 'ocs_host'
    set_txtimer_list:
    - DCCTMPLTNAME: 'dcc-test'
      TXTIMERFLAG: TXTIMER_VALUE
      TXTIMER: 10
      RETRYTIMEOUT: ''
      RETRYTIMES: ''
    add_dcctemplate_list_4:
    - DCCTMPLTNAME: 'dcc-test'
      QCT: 0
      QHT: 0
      VQT: 20
      TQT: 20
      CCRINITRGNUM: 5
      CCFH: TERMINATE
      SGSNTRIGGER: ENABLE
      SERVICETRIGGER: ENABLE
      VALIDTIME: 30
      PRIOCSGRPNAME: 'ocs_host'
    add_msccrcact_list:
    - DCCTMPLTNAME: 'dcc-test'
      MSCCRC: '4012'
      MSCCRCACT: TERMINATE
      MSCCBLKTIMER: ''
      MSCCRDVIRTIP: ''
      MSCCRDVIRTIPV6: ''
      MSCCREACTREQ: DISABLE
    set_apnchargectrl_list:
    - APN: 'apn-test'
      ONLINESW: ENABLE
      DCCTEMPLATE: 'dcc-test'
      CCNAME: 'testchgcha'
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 配置计费属性。

```jinja2
{%- for item in add_chargechar_list -%}
    ADD CHARGECHAR:
    {#- --- 必选参数 --- -#}
    CCNAME="{{item.CCNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.HOME is not none -%}
        HOME="{{item.HOME}}",
    {%- endif -%}
    {%- if item.ROAM is not none -%}
        ROAM="{{item.ROAM}}",
    {%- endif -%}
    {%- if item.VISIT is not none -%}
        VISIT="{{item.VISIT}}",
    {%- endif -%}
    {%- if item.HOMESGSN is not none -%}
        HOMESGSN={{item.HOMESGSN}},
    {%- endif -%}
    {%- if item.ROAMSGSN is not none -%}
        ROAMSGSN={{item.ROAMSGSN}},
    {%- endif -%}
    {%- if item.VISITSGSN is not none -%}
        VISITSGSN={{item.VISITSGSN}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 如果该计费属性实例没有绑定APN实例或者UserProfile实例，则配置的计费属性不生效。

### 2 配置用户的计费方式是在线计费。

```jinja2
{%- for item in set_chargectrl_list -%}
    SET CHARGECTRL:
    {#- --- 可选参数 --- -#}
    {%- if item.HOMEONLINE is not none -%}
        HOMEONLINE={{item.HOMEONLINE}},
    {%- endif -%}
    {%- if item.VISITONLINE is not none -%}
        VISITONLINE={{item.VISITONLINE}},
    {%- endif -%}
    {%- if item.ROAMONLINE is not none -%}
        ROAMONLINE={{item.ROAMONLINE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 配置在线计费的费率标识。

#### 3.1 配置URR，从而配置相应的计费费率标识，包括必须配置的RG和可选配置的SID。

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

#### 3.2 配置URR组，将上下行URR绑定到URR组上。上下行可以使用不同的URR。

```jinja2
{%- for item in add_urrgroup_list -%}
    ADD URRGROUP:
    {#- --- 必选参数 --- -#}
    URRGROUPNAME="{{item.URRGROUPNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.UPURRNAME1 is not none -%}
        UPURRNAME1="{{item.UPURRNAME1}}",
    {%- endif -%}
    {%- if item.DOWNURRNAME1 is not none -%}
        DOWNURRNAME1="{{item.DOWNURRNAME1}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 配置DCC模板。

#### 4.1 全局DCC模板。

```jinja2
{%- for item in mod_dcctemplate_list -%}
    MOD DCCTEMPLATE:
    {#- --- 必选参数 --- -#}
    DCCTMPLTNAME="{{item.DCCTMPLTNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.PRIOCSGRPNAME is not none -%}
        PRIOCSGRPNAME="{{item.PRIOCSGRPNAME}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 4.2 DCC模板。

```jinja2
{%- for item in add_dcctemplate_list -%}
    ADD DCCTEMPLATE:
    {#- --- 必选参数 --- -#}
    DCCTMPLTNAME="{{item.DCCTMPLTNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.QCT is not none -%}
        QCT={{item.QCT}},
    {%- endif -%}
    {%- if item.QHT is not none -%}
        QHT={{item.QHT}},
    {%- endif -%}
    {%- if item.VQT is not none -%}
        VQT={{item.VQT}},
    {%- endif -%}
    {%- if item.TQT is not none -%}
        TQT={{item.TQT}},
    {%- endif -%}
    {%- if item.CCRINITRGNUM is not none -%}
        CCRINITRGNUM={{item.CCRINITRGNUM}},
    {%- endif -%}
    {%- if item.CCFH is not none -%}
        CCFH={{item.CCFH}},
    {%- endif -%}
    {%- if item.SGSNTRIGGER is not none -%}
        SGSNTRIGGER={{item.SGSNTRIGGER}},
    {%- endif -%}
    {%- if item.SERVICETRIGGER is not none -%}
        SERVICETRIGGER={{item.SERVICETRIGGER}},
    {%- endif -%}
    {%- if item.PRIOCSGRPNAME is not none -%}
        PRIOCSGRPNAME="{{item.PRIOCSGRPNAME}}",
    {%- endif -%}
    {%- if item.VALIDTIME is not none -%}
        VALIDTIME={{item.VALIDTIME}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 配置全局DCC模板使用命令全局**MOD DCCTEMPLATE**，其他粒度（UserProfile、APN、计费属性Charging Characteristics）的DCC模板使用命令**ADD DCCTEMPLATE**，在模板下配置在线计费参数（如步骤 6~步骤 9），最后绑定不同的粒度范围。

#### 由此可见，主要是粒度范围不一致，其他的计费参数命令类似。

### 5 配置在线计费设备标识。

#### 5.1 配置在线计费中通信的GGSN/PGW-C设备标识，重复执行本步可添加多个Gy应用的本地信息。

```jinja2
{%- for item in add_diamlocinfo_list -%}
    ADD DIAMLOCINFO:
    {#- --- 必选参数 --- -#}
    HOSTNAME="{{item.HOSTNAME}}",
    REALMNAME="{{item.REALMNAME}}",
    PRODUCTNAME="{{item.PRODUCTNAME}}",
    ;
{%- endfor -%}
```

#### 5.2 配置OCS信息。重复执行本步可增加多个OCS信息。

```jinja2
{%- for item in add_ocs_list -%}
    ADD OCS:
    {#- --- 必选参数 --- -#}
    OCSHOSTNAME="{{item.OCSHOSTNAME}}",
    REALMNAME="{{item.REALMNAME}}",
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_diampeeraddr_list -%}
    ADD DIAMPEERADDR:
    {#- --- 必选参数 --- -#}
    HOSTNAME="{{item.HOSTNAME}}",
    ADDRTYPE={{item.ADDRTYPE}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：ADDRTYPE=IPv4 时必选 --- -#}
    {%- if item.ADDRTYPE == 'IPv4' -%}
        IPV4ADDRESS="{{item.IPV4ADDRESS}}",
    {%- endif -%}
    {#- --- 条件必选：ADDRTYPE=IPv6 时必选 --- -#}
    {%- if item.ADDRTYPE == 'IPv6' -%}
        IPV6ADDRESS="{{item.IPV6ADDRESS}}",
    {%- endif -%}
    {#- --- 条件必选：ADDRTYPE=SCTP 时必选 --- -#}
    {%- if item.ADDRTYPE == 'SCTP' -%}
        SCTPENDPOINT="{{item.SCTPENDPOINT}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：ADDRTYPE=IPv4/IPv6 时可选 --- -#}
    {%- if item.ADDRTYPE in ['IPv4', 'IPv6'] -%}
        {%- if item.PORT is not none -%}
            PORT={{item.PORT}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 5.3 配置OCS组。

```jinja2
{%- for item in add_ocsgroup_list -%}
    ADD OCSGROUP:
    {#- --- 必选参数 --- -#}
    OCSGRPNAME="{{item.OCSGRPNAME}}",
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_ocsbinding_list -%}
    ADD OCSBINDING:
    {#- --- 必选参数 --- -#}
    OCSGRPNAME="{{item.OCSGRPNAME}}",
    OCSHOSTNAME="{{item.OCSHOSTNAME}}",
    ;
{%- endfor -%}
```

#### 5.4 配置主从OCS组。

```jinja2
{%- for item in add_dcctemplate_list_1 -%}
    ADD DCCTEMPLATE:
    {#- --- 必选参数 --- -#}
    DCCTMPLTNAME="{{item.DCCTMPLTNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.QCT is not none -%}
        QCT={{item.QCT}},
    {%- endif -%}
    {%- if item.QHT is not none -%}
        QHT={{item.QHT}},
    {%- endif -%}
    {%- if item.VQT is not none -%}
        VQT={{item.VQT}},
    {%- endif -%}
    {%- if item.TQT is not none -%}
        TQT={{item.TQT}},
    {%- endif -%}
    {%- if item.CCRINITRGNUM is not none -%}
        CCRINITRGNUM={{item.CCRINITRGNUM}},
    {%- endif -%}
    {%- if item.CCFH is not none -%}
        CCFH={{item.CCFH}},
    {%- endif -%}
    {%- if item.SGSNTRIGGER is not none -%}
        SGSNTRIGGER={{item.SGSNTRIGGER}},
    {%- endif -%}
    {%- if item.SERVICETRIGGER is not none -%}
        SERVICETRIGGER={{item.SERVICETRIGGER}},
    {%- endif -%}
    {%- if item.PRIOCSGRPNAME is not none -%}
        PRIOCSGRPNAME="{{item.PRIOCSGRPNAME}}",
    {%- endif -%}
    {%- if item.VALIDTIME is not none -%}
        VALIDTIME={{item.VALIDTIME}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 6 配置配额门限（配额空耗时间QCT、配额空闲时间QHT、流量门限阈值VQT、时长门限阈值TQT）。

```jinja2
{%- for item in add_dcctemplate_list_2 -%}
    ADD DCCTEMPLATE:
    {#- --- 必选参数 --- -#}
    DCCTMPLTNAME="{{item.DCCTMPLTNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.QCT is not none -%}
        QCT={{item.QCT}},
    {%- endif -%}
    {%- if item.QHT is not none -%}
        QHT={{item.QHT}},
    {%- endif -%}
    {%- if item.VQT is not none -%}
        VQT={{item.VQT}},
    {%- endif -%}
    {%- if item.TQT is not none -%}
        TQT={{item.TQT}},
    {%- endif -%}
    {%- if item.CCRINITRGNUM is not none -%}
        CCRINITRGNUM={{item.CCRINITRGNUM}},
    {%- endif -%}
    {%- if item.CCFH is not none -%}
        CCFH={{item.CCFH}},
    {%- endif -%}
    {%- if item.SGSNTRIGGER is not none -%}
        SGSNTRIGGER={{item.SGSNTRIGGER}},
    {%- endif -%}
    {%- if item.SERVICETRIGGER is not none -%}
        SERVICETRIGGER={{item.SERVICETRIGGER}},
    {%- endif -%}
    {%- if item.PRIOCSGRPNAME is not none -%}
        PRIOCSGRPNAME="{{item.PRIOCSGRPNAME}}",
    {%- endif -%}
    {%- if item.VALIDTIME is not none -%}
        VALIDTIME={{item.VALIDTIME}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 7 配置CCR触发机制（SGSN/SGW地址改变发送CCR、业务触发请求CCR、CCR-I消息中允许携带的RG的最大个数）。

```jinja2
{%- for item in add_dcctemplate_list_3 -%}
    ADD DCCTEMPLATE:
    {#- --- 必选参数 --- -#}
    DCCTMPLTNAME="{{item.DCCTMPLTNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.QCT is not none -%}
        QCT={{item.QCT}},
    {%- endif -%}
    {%- if item.QHT is not none -%}
        QHT={{item.QHT}},
    {%- endif -%}
    {%- if item.VQT is not none -%}
        VQT={{item.VQT}},
    {%- endif -%}
    {%- if item.TQT is not none -%}
        TQT={{item.TQT}},
    {%- endif -%}
    {%- if item.CCRINITRGNUM is not none -%}
        CCRINITRGNUM={{item.CCRINITRGNUM}},
    {%- endif -%}
    {%- if item.CCFH is not none -%}
        CCFH={{item.CCFH}},
    {%- endif -%}
    {%- if item.SGSNTRIGGER is not none -%}
        SGSNTRIGGER={{item.SGSNTRIGGER}},
    {%- endif -%}
    {%- if item.SERVICETRIGGER is not none -%}
        SERVICETRIGGER={{item.SERVICETRIGGER}},
    {%- endif -%}
    {%- if item.PRIOCSGRPNAME is not none -%}
        PRIOCSGRPNAME="{{item.PRIOCSGRPNAME}}",
    {%- endif -%}
    {%- if item.VALIDTIME is not none -%}
        VALIDTIME={{item.VALIDTIME}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 8 配置定时器。

#### 8.1 配置Tx定时器的时长。

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

#### 8.2 配置Tx定时器超时以后的处理方式。

```jinja2
{%- for item in add_dcctemplate_list_4 -%}
    ADD DCCTEMPLATE:
    {#- --- 必选参数 --- -#}
    DCCTMPLTNAME="{{item.DCCTMPLTNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.QCT is not none -%}
        QCT={{item.QCT}},
    {%- endif -%}
    {%- if item.QHT is not none -%}
        QHT={{item.QHT}},
    {%- endif -%}
    {%- if item.VQT is not none -%}
        VQT={{item.VQT}},
    {%- endif -%}
    {%- if item.TQT is not none -%}
        TQT={{item.TQT}},
    {%- endif -%}
    {%- if item.CCRINITRGNUM is not none -%}
        CCRINITRGNUM={{item.CCRINITRGNUM}},
    {%- endif -%}
    {%- if item.CCFH is not none -%}
        CCFH={{item.CCFH}},
    {%- endif -%}
    {%- if item.SGSNTRIGGER is not none -%}
        SGSNTRIGGER={{item.SGSNTRIGGER}},
    {%- endif -%}
    {%- if item.SERVICETRIGGER is not none -%}
        SERVICETRIGGER={{item.SERVICETRIGGER}},
    {%- endif -%}
    {%- if item.PRIOCSGRPNAME is not none -%}
        PRIOCSGRPNAME="{{item.PRIOCSGRPNAME}}",
    {%- endif -%}
    {%- if item.VALIDTIME is not none -%}
        VALIDTIME={{item.VALIDTIME}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 9 配置MSCC层消息码为异常返回码时的业务处理动作。

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

### 10 为APN实例绑定计费属性、计费方式、DCC模板。

### 本实例以APN粒度为例说明普通在线计费的配置步骤，对于UserProfile和计费属性Charging Characteristics粒度的配置步骤，与APN粒度的配置步骤类似，只是绑定范围不同。

### 对于全局粒度的普通在线计费配置步骤，没有绑定动作，不同的是采用的是全局DCC模板**MOD DCCTEMPLATE**。

### 为APN实例"apn-test"绑定计费属性、计费方式、计费模板。

```jinja2
{%- for item in set_apnchargectrl_list -%}
    SET APNCHARGECTRL:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    {#- --- 可选参数 --- -#}
    {%- if item.ONLINESW is not none -%}
        ONLINESW={{item.ONLINESW}},
    {%- endif -%}
    {%- if item.DCCTEMPLATE is not none -%}
        DCCTEMPLATE="{{item.DCCTEMPLATE}}",
    {%- endif -%}
    {%- if item.CCNAME is not none -%}
        CCNAME="{{item.CCNAME}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 针对同一个用户，**ADD CHARGECHAR**和**ADD CHARGEMETHOD**配置的结果要保持一致，要么是“ONLINE”，要么是“OFFLINE”，或者两者同时使能，如果不一致将导致用户计费方式错误。


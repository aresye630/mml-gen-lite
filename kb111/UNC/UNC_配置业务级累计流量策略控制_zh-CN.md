---
id: ''
name: 配置业务级累计流量策略控制
ne_type: UNC
type: feature
description: 通过部署基于业务累计流量的策略控制功能，实现对特定业务的控制，如用户业务访问量超出限额时降低其访问速率或提高费率，达到网络公平使用的原则，使访问相同业务的用户得到同样的网络体验。
risk_level: ''
doc_source: ["网络部署","业务专题","5G Core FUP解决方案","业务级累计流量策略控制","配置业务级累计流量策略控制"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
通过部署基于业务累计流量的策略控制功能，实现对特定业务的控制，如用户业务访问量超出限额时降低其访问速率或提高费率，达到网络公平使用的原则，使访问相同业务的用户得到同样的网络体验。

## 必备事项
前提条件

完成PCC相关基本功能配置。
完成加载License。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    set_licenseswitch_list:
      type: items
      properties:
        LICITEM:
          name: 'License项'
          type: string
          minLength: 0
          maxLength: 255
          required: true
          description: '业务级累计流量策略控制的License项。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        SWITCH:
          name: '开关'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: true
          description: '开启业务级累计流量策略控制功能。'
          data_source: '固定取值'
          pattern: ''
          default: ''
    set_pccfunc_list:
      type: items
      properties:
        MKPARSEFORMAT:
          name: 'Monitoring-Key的解析方式'
          type: string
          enum:
          - ASCII
          - SELFADAPT
          - UNSIGNED32
          required: false
          description: '该参数需要与PCRF/PCF保持一致。'
          data_source: '与对端协商'
          pattern: ''
          default: ''
        N7FEATURELIST:
          name: 'N7接口特性列表'
          type: string
          required: false
          description: '该参数需要与PCRF/PCF保持一致。'
          data_source: '与对端协商'
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
          description: '存在多条记录时，该参数不能重复。  urr\_01为累计流量上报的URR名称，urrA为配额耗尽前的URR名称，urrB为配额耗尽后的URR名称。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        URRID:
          name: 'URR标识'
          type: integer
          minimum: 0
          maximum: 2147483646
          required: true
          description: '该参数需要与PGW-U/UPF上的URR标识保持一致。  1000为累计流量上报的URR ID，2000为配额耗尽前的URR ID，3000为配额耗尽后的URR ID。'
          data_source: '与对端协商'
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
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        MONITORINGKEY:
          name: '监控属性值'
          type: string
          maxLength: 31
          required: false
          description: '该参数需要与PCRF/PCF的监控属性值保持一致。'
          data_source: '与对端协商'
          pattern: ''
          default: ''
        ONLCOMPOUNDTYPE:
          name: '在线计费标识组成类型'
          type: string
          enum:
          - ONLYRG
          - RGSID
          required: false
          description: '-'
          data_source: '与对端协商'
          pattern: ''
          default: ''
        ONLINERG:
          name: '在线计费组'
          type: integer
          minimum: 0
          maximum: 4294967294
          required: false
          description: '10为配额耗尽前的费率组，20为配额耗尽后的费率组。'
          data_source: '与对端协商'
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
          description: '-'
          data_source: '全网规划'
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
    add_urr_list_1:
      type: items
      properties:
        URRNAME:
          name: '使用量上报规则名称'
          type: string
          maxLength: 31
          required: true
          description: '存在多条记录时，该参数不能重复。  urr\_01为累计流量上报的URR名称，urrA为配额耗尽前的URR名称，urrB为配额耗尽后的URR名称。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        URRID:
          name: 'URR标识'
          type: integer
          minimum: 0
          maximum: 2147483646
          required: true
          description: '该参数需要与PGW-U/UPF上的URR标识保持一致。  1000为累计流量上报的URR ID，2000为配额耗尽前的URR ID，3000为配额耗尽后的URR ID。'
          data_source: '与对端协商'
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
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        ONLCOMPOUNDTYPE:
          name: '在线计费标识组成类型'
          type: string
          enum:
          - ONLYRG
          - RGSID
          required: false
          description: '-'
          data_source: '与对端协商'
          pattern: ''
          default: ''
        ONLINERG:
          name: '在线计费组'
          type: integer
          minimum: 0
          maximum: 4294967294
          required: false
          description: '10为配额耗尽前的费率组，20为配额耗尽后的费率组。'
          data_source: '与对端协商'
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
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        MONITORINGKEY:
          name: '监控属性值'
          type: string
          maxLength: 31
          required: false
          description: '该参数需要与PCRF/PCF的监控属性值保持一致。'
          data_source: '与对端协商'
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
    add_urrgroup_list:
      type: items
      properties:
        URRGROUPNAME:
          name: '使用量上报规则组名称'
          type: string
          maxLength: 31
          required: true
          description: '存在多条记录时，该参数不能重复。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        UPURRNAME1:
          name: '上行发起URR名称1'
          type: string
          maxLength: 31
          required: false
          description: '使用**ADD URR**定义的URRNAME。'
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
        UPURRNAME2:
          name: '上行发起URR名称2'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        DOWNURRNAME2:
          name: '下行发起URR名称2'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_pccpolicygrp_list:
      type: items
      properties:
        PCCPOLICYGRPNM:
          name: 'PCC策略组名称'
          type: string
          maxLength: 63
          required: true
          description: '存在多条记录时，该参数不能重复。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        URRGROUPNAME:
          name: '使用量上报规则组名称'
          type: string
          maxLength: 31
          required: false
          description: '使用**ADD URRGROUP**定义的URRGROUPNAME。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        FUPSESSIONEXC:
          name: 'Session级FUP累计标识'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: 'ENABLE表示该PCC策略组对应的业务不计入Session级流量。默认DISABLE，计入Session级流量。'
          data_source: '本端规划'
          pattern: ''
          default: DISABLE
    add_rule_list:
      type: items
      properties:
        RULENAME:
          name: '规则名称'
          type: string
          required: false
          description: '与PGW-U/UPF上配置的规则名称保持一致。存在多条数据时，该参数+策略类型不能完全相同。  rule\_test1为配额耗尽前的规则，rule\_test2为配额耗尽后的规则。'
          data_source: '与对端协商'
          pattern: ''
          default: ''
        POLICYTYPE:
          name: '策略类型'
          type: string
          required: false
          description: '使用样例值。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PRIORITY:
          name: '全局优先级'
          type: string
          required: false
          description: '仅对PCC用户生效。优先级值越小，优先级越高。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        POLICYNAME:
          name: '策略名称'
          type: string
          required: false
          description: '使用**ADD PCCPOLICYGRP**命令定义的PCC策略组名称。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_userprofile_list:
      type: items
      properties:
        USERPROFILENAME:
          name: '用户模板名称'
          type: string
          maxLength: 63
          required: true
          description: '与PGW-U/UPF上配置的用户模板名称保持一致。'
          data_source: '与对端协商'
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
          description: '-'
          data_source: '固定取值'
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
    add_rulebinding_list:
      type: items
      properties:
        USERPROFILENAME:
          name: '用户模板名称'
          type: string
          maxLength: 63
          required: true
          description: '使用**ADD USERPROFILE**命令定义的用户模板名称。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        RULENAME:
          name: '规则名称'
          type: string
          maxLength: 63
          required: true
          description: '适用**ADD RULE**命令定义的规则名称。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    set_licenseswitch_list_1:
      type: items
      properties:
        LICITEM:
          name: 'License项'
          type: string
          minLength: 0
          maxLength: 255
          required: true
          description: '业务级累计流量策略控制的License项。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        SWITCH:
          name: '开关'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: true
          description: '开启业务级累计流量策略控制功能。'
          data_source: '固定取值'
          pattern: ''
          default: ''
    add_filter_list:
      type: items
      properties:
        FILTERNAME:
          name: '过滤器名字'
          type: string
          required: false
          description: 'UDG通过将用户上下行报文匹配filter，实现报文的过滤。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        L34PROTTYPE:
          name: '三四层IPv4协议输入类型'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        L34PROTOCOL:
          name: '三四层协议类型'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        SVRIPMODE:
          name: '服务器IP地址配置模式'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        SVRIP:
          name: '服务器IP地址'
          type: string
          required: false
          description: ''
          data_source: '与对端协商'
          pattern: ''
          default: ''
        SVRIPMASKTYPE:
          name: '服务器IP地址掩码类型'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        SVRIPMASKLEN:
          name: '服务器IP地址掩码长度'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_flowfilter_list:
      type: items
      properties:
        FLOWFILTERNAME:
          name: '流过滤器名称'
          type: string
          maxLength: 63
          required: true
          description: '流过滤器。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_fltbindflowf_list:
      type: items
      properties:
        FLOWFILTERNAME:
          name: 'FLOWFILTERNAME'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        FILTERNAME:
          name: '过滤器名字'
          type: string
          required: false
          description: '绑定的三四层过滤条件已通过**ADD FILTER**命令配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    set_refreshsrv_list:
      type: items
      properties:
        REFRESHTYPE:
          name: '刷新类型'
          type: string
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_urr_list_3:
      type: items
      properties:
        URRNAME:
          name: '使用量上报规则名称'
          type: string
          maxLength: 31
          required: true
          description: 'urr\_mk为累计流量上报的URR名称，urr\_basic为配额耗尽前的URR名称，urr\_exhaust为配额耗尽后的URR名称。  在线流量计费使用量上报规则信息，要求和UNC两端的URR标识的取值要一致。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        URRID:
          name: 'URR标识'
          type: integer
          minimum: 0
          maximum: 2147483646
          required: true
          description: '该参数需要与PGW-C/SMF上的URR标识保持一致。1000为累计流量上报的URR ID，2000为配额耗尽前的URR ID，3000为配额耗尽后的URR ID。'
          data_source: '与对端协商'
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
          description: '-'
          data_source: '全网规划'
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
          description: '-'
          data_source: '全网规划'
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
        REDIRENDTOKEN:
          name: 'Gy重定向结束Token'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_urr_list_4:
      type: items
      properties:
        URRNAME:
          name: '使用量上报规则名称'
          type: string
          maxLength: 31
          required: true
          description: 'urr\_mk为累计流量上报的URR名称，urr\_basic为配额耗尽前的URR名称，urr\_exhaust为配额耗尽后的URR名称。  在线流量计费使用量上报规则信息，要求和UNC两端的URR标识的取值要一致。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        URRID:
          name: 'URR标识'
          type: integer
          minimum: 0
          maximum: 2147483646
          required: true
          description: '该参数需要与PGW-C/SMF上的URR标识保持一致。1000为累计流量上报的URR ID，2000为配额耗尽前的URR ID，3000为配额耗尽后的URR ID。'
          data_source: '与对端协商'
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
          description: '-'
          data_source: '全网规划'
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
          description: '-'
          data_source: '全网规划'
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
        REDIRENDTOKEN:
          name: 'Gy重定向结束Token'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_urrgroup_list_2:
      type: items
      properties:
        URRGROUPNAME:
          name: '使用量上报规则组名称'
          type: string
          maxLength: 31
          required: true
          description: 'urrg\_basic为配额耗尽前的规则组名称，urrg\_exhaust为配额耗尽后的规则组名称。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        UPURRNAME1:
          name: '上行发起URR名称1'
          type: string
          maxLength: 31
          required: false
          description: '已在该配置任务中通过命令**ADD URR**配置。'
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
        UPURRNAME2:
          name: '上行发起URR名称2'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        DOWNURRNAME2:
          name: '下行发起URR名称2'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_pccpolicygrp_list_2:
      type: items
      properties:
        PCCPOLICYGRPNM:
          name: 'PCC策略组名称'
          type: string
          maxLength: 63
          required: true
          description: 'cg\_basic为配额耗尽前的PCC策略组，cg\_exhaust为配额耗尽后的PCC策略组。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        URRGROUPNAME:
          name: 'URR组名称'
          type: string
          maxLength: 31
          required: false
          description: 'PCC策略组绑定的URR组，已通过**ADD URRGROUP**命令配置完成。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_rule_list_2:
      type: items
      properties:
        RULENAME:
          name: '规则名称'
          type: string
          required: false
          description: '与PGW-C/SMF上配置的规则名称保持一致。存在多条数据时，该参数+策略类型不能完全相同。  rule\_test1为配额耗尽前的规则，rule\_test2为配额耗尽后的规则。'
          data_source: '与对端协商'
          pattern: ''
          default: ''
        POLICYTYPE:
          name: '策略类型'
          type: string
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        FILTERINGMODE:
          name: '流过滤器或流过滤器组选择'
          type: string
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        FLOWFILTERNAME:
          name: '流过滤器名称'
          type: string
          required: false
          description: '绑定的FlowFilter已通过**ADD FLOWFILTER**命令配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        POLICYNAME:
          name: '策略名称'
          type: string
          required: false
          description: '绑定的PCC策略组已通过**ADD PCCPOLICYGRP**命令配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        PRIORITY:
          name: '全局优先级'
          type: string
          required: false
          description: '仅对PCC用户生效。优先级值越小，优先级越高。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_userprofile_list_1:
      type: items
      properties:
        USERPROFILENAME:
          name: '用户模板名称'
          type: string
          maxLength: 63
          required: true
          description: '与PGW-C/SMF上配置的用户模板名称保持一致。'
          data_source: '与对端协商'
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
    add_rulebinding_list_2:
      type: items
      properties:
        USERPROFILENAME:
          name: '用户模板名称'
          type: string
          maxLength: 63
          required: true
          description: '使用**ADD USERPROFILE**命令定义的用户模板名称。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        RULENAME:
          name: '规则名称'
          type: string
          maxLength: 63
          required: true
          description: 'UserProfile绑定的业务规则，已通过**ADD RULE**命令配置完成。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV2FUPSAT01'
      SWITCH: ENABLE
    set_pccfunc_list:
    - MKPARSEFORMAT: UNSIGNED32
      N7FEATURELIST: UMC
    add_urr_list:
    - URRNAME: 'urr_01'
      URRID: 1000
      USAGERPTMODE: MONITORINGKEY
      MONITORINGKEY: '2001'
      ONLCOMPOUNDTYPE: ONLYRG
      ONLINERG: 10
      ONLMETERINGTYPE: VOLUME
      ONLINESID: ''
      EVENTRSUVALUE: ''
      TIMERSUVALUE: ''
      VOLUMERSUVALUE: ''
      N40AGESW: ENABLE
      OFCSRVTMPLNAME: ''
      OFFCOMPOUNDTYPE: ''
      OFFMETERINGTYPE: ''
      REDIRENDTOKEN: ''
    add_urr_list_1:
    - URRNAME: 'urrA'
      URRID: 2000
      USAGERPTMODE: ONLINE
      ONLCOMPOUNDTYPE: ONLYRG
      ONLINERG: 10
      ONLMETERINGTYPE: VOLUME
      MONITORINGKEY: '2001'
      ONLINESID: ''
      EVENTRSUVALUE: ''
      TIMERSUVALUE: ''
      VOLUMERSUVALUE: ''
      N40AGESW: ENABLE
      OFCSRVTMPLNAME: ''
      OFFCOMPOUNDTYPE: ''
      OFFMETERINGTYPE: ''
      REDIRENDTOKEN: ''
    - URRNAME: 'urrB'
      URRID: 3000
      USAGERPTMODE: ONLINE
      ONLCOMPOUNDTYPE: ONLYRG
      ONLINERG: 20
      ONLMETERINGTYPE: VOLUME
      MONITORINGKEY: '2001'
      ONLINESID: ''
      EVENTRSUVALUE: ''
      TIMERSUVALUE: ''
      VOLUMERSUVALUE: ''
      N40AGESW: ''
      OFCSRVTMPLNAME: ''
      OFFCOMPOUNDTYPE: ''
      OFFMETERINGTYPE: ''
      REDIRENDTOKEN: ''
    add_urrgroup_list:
    - URRGROUPNAME: 'urrgA'
      UPURRNAME1: 'urr_01'
      DOWNURRNAME1: 'urr_01'
      UPURRNAME2: 'urrA'
      DOWNURRNAME2: 'urrA'
    - URRGROUPNAME: 'urrgB'
      UPURRNAME1: 'urr_01'
      DOWNURRNAME1: 'urr_01'
      UPURRNAME2: 'urrB'
      DOWNURRNAME2: 'urrB'
    add_pccpolicygrp_list:
    - PCCPOLICYGRPNM: 'pccgA'
      URRGROUPNAME: 'urrgA'
      FUPSESSIONEXC: ENABLE
    - PCCPOLICYGRPNM: 'pccgB'
      URRGROUPNAME: 'urrgB'
      FUPSESSIONEXC: ENABLE
    add_rule_list:
    - RULENAME: rule_test1
      POLICYTYPE: PCC
      PRIORITY: '30'
      POLICYNAME: pccgA
    add_userprofile_list:
    - USERPROFILENAME: 'up_test'
      UPTYPE: PCC
      PROFILERANGE: ALL
    add_rulebinding_list:
    - USERPROFILENAME: 'up_test'
      RULENAME: 'rule_test1'
    set_licenseswitch_list_1:
    - LICITEM: 'LKV3G5FPBS01'
      SWITCH: ENABLE
    add_filter_list:
    - FILTERNAME: filter_red
      L34PROTTYPE: STRING
      L34PROTOCOL: ANY
      SVRIPMODE: IP
      SVRIP: 10.7.19.38
      SVRIPMASKTYPE: LENGTHTYPE
      SVRIPMASKLEN: '32'
    add_flowfilter_list:
    - FLOWFILTERNAME: 'fg_red'
    add_fltbindflowf_list:
    - FLOWFILTERNAME: fg_red
      FILTERNAME: filter_red
    set_refreshsrv_list:
    - REFRESHTYPE: USERPROFILE
    add_urr_list_3:
    - URRNAME: 'urr_mk'
      URRID: 1000
      USAGERPTMODE: MONITORINGKEY
      ONLMETERINGTYPE: VOLUME
      EVENTRSUVALUE: ''
      TIMERSUVALUE: ''
      VOLUMERSUVALUE: ''
      MONITORINGKEY: ''
      N40AGESW: ENABLE
      OFCSRVTMPLNAME: ''
      OFFCOMPOUNDTYPE: ''
      OFFMETERINGTYPE: ''
      ONLCOMPOUNDTYPE: ''
      REDIRENDTOKEN: ''
    add_urr_list_4:
    - URRNAME: 'urr_basic'
      URRID: 2000
      USAGERPTMODE: ONLINE
      ONLMETERINGTYPE: VOLUME
      EVENTRSUVALUE: ''
      TIMERSUVALUE: ''
      VOLUMERSUVALUE: ''
      MONITORINGKEY: ''
      N40AGESW: ENABLE
      OFCSRVTMPLNAME: ''
      OFFCOMPOUNDTYPE: ''
      OFFMETERINGTYPE: ''
      ONLCOMPOUNDTYPE: ''
      REDIRENDTOKEN: ''
    - URRNAME: 'urr_exhaust'
      URRID: 3000
      USAGERPTMODE: ONLINE
      ONLMETERINGTYPE: VOLUME
      EVENTRSUVALUE: ''
      TIMERSUVALUE: ''
      VOLUMERSUVALUE: ''
      MONITORINGKEY: ''
      N40AGESW: ''
      OFCSRVTMPLNAME: ''
      OFFCOMPOUNDTYPE: ''
      OFFMETERINGTYPE: ''
      ONLCOMPOUNDTYPE: ''
      REDIRENDTOKEN: ''
    add_urrgroup_list_2:
    - URRGROUPNAME: 'urrg_basic'
      UPURRNAME1: 'urr_mk'
      DOWNURRNAME1: 'urr_mk'
      UPURRNAME2: 'urr_basic'
      DOWNURRNAME2: 'urr_basic'
    - URRGROUPNAME: 'urrg_exhaust'
      UPURRNAME1: 'urr_mk'
      DOWNURRNAME1: 'urr_mk'
      UPURRNAME2: 'urr_exhaust'
      DOWNURRNAME2: 'urr_exhaust'
    add_pccpolicygrp_list_2:
    - PCCPOLICYGRPNM: 'cg_basic'
      URRGROUPNAME: 'urrg_basic'
    - PCCPOLICYGRPNM: 'cg_exhaust'
      URRGROUPNAME: 'urrg_exhaust'
    add_rule_list_2:
    - RULENAME: rule_test1
      POLICYTYPE: PCC
      FILTERINGMODE: FLOWFILTER
      FLOWFILTERNAME: fg_red
      POLICYNAME: cg_basic
      PRIORITY: '100'
    add_userprofile_list_1:
    - USERPROFILENAME: 'up_test'
      UPTYPE: PCC
      PROFILERANGE: ALL
    add_rulebinding_list_2:
    - USERPROFILENAME: 'up_test'
      RULENAME: 'rule_test1'
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 脚本中的蓝色字体表示UNC和UDG上规划的数据需要一致。

### UNC侧配置

#### 1.1 //打开本特性的License配置开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

#### 1.2 //配置PCC功能。

```jinja2
{%- for item in set_pccfunc_list -%}
    SET PCCFUNC:
    {#- --- 可选参数 --- -#}
    {%- if item.MKPARSEFORMAT is not none -%}
        MKPARSEFORMAT={{item.MKPARSEFORMAT}},
    {%- endif -%}
    {%- if item.N7FEATURELIST is not none -%}
        N7FEATURELIST={{item.N7FEATURELIST}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 1.4 //配置URR标识与监控属性值的绑定关系。

```jinja2
{%- for item in add_urr_list -%}
    ADD URR:
    {#- --- 必选参数 --- -#}
    URRNAME="{{item.URRNAME}}",
    URRID={{item.URRID}},
    USAGERPTMODE={{item.USAGERPTMODE}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：USAGERPTMODE=MONITORINGKEY 时必选 --- -#}
    {%- if item.USAGERPTMODE == 'MONITORINGKEY' -%}
        MONITORINGKEY="{{item.MONITORINGKEY}}",
    {%- endif -%}
    {#- --- 条件必选：USAGERPTMODE=OFFLINE 时必选 --- -#}
    {%- if item.USAGERPTMODE == 'OFFLINE' -%}
        OFFCOMPOUNDTYPE={{item.OFFCOMPOUNDTYPE}},
    {%- endif -%}
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
    {#- --- 条件可选参数 --- -#}
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

#### 1.5 //配置配额耗尽前的计费策略。

```jinja2
{%- for item in add_urr_list_1 -%}
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
    {#- --- 条件必选：USAGERPTMODE=MONITORINGKEY 时必选 --- -#}
    {%- if item.USAGERPTMODE == 'MONITORINGKEY' -%}
        MONITORINGKEY="{{item.MONITORINGKEY}}",
    {%- endif -%}
    {#- --- 条件必选：USAGERPTMODE=OFFLINE 时必选 --- -#}
    {%- if item.USAGERPTMODE == 'OFFLINE' -%}
        OFFCOMPOUNDTYPE={{item.OFFCOMPOUNDTYPE}},
    {%- endif -%}
    {#- --- 条件必选：ONLCOMPOUNDTYPE=RGSID 时必选 --- -#}
    {%- if item.ONLCOMPOUNDTYPE == 'RGSID' -%}
        ONLINESID={{item.ONLINESID}},
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
{%- for item in add_urrgroup_list -%}
    ADD URRGROUP:
    {#- --- 必选参数 --- -#}
    URRGROUPNAME="{{item.URRGROUPNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.UPURRNAME1 is not none -%}
        UPURRNAME1="{{item.UPURRNAME1}}",
    {%- endif -%}
    {%- if item.UPURRNAME2 is not none -%}
        UPURRNAME2="{{item.UPURRNAME2}}",
    {%- endif -%}
    {%- if item.DOWNURRNAME1 is not none -%}
        DOWNURRNAME1="{{item.DOWNURRNAME1}}",
    {%- endif -%}
    {%- if item.DOWNURRNAME2 is not none -%}
        DOWNURRNAME2="{{item.DOWNURRNAME2}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_pccpolicygrp_list -%}
    ADD PCCPOLICYGRP:
    {#- --- 必选参数 --- -#}
    PCCPOLICYGRPNM="{{item.PCCPOLICYGRPNM}}",
    {#- --- 可选参数 --- -#}
    {%- if item.URRGROUPNAME is not none -%}
        URRGROUPNAME="{{item.URRGROUPNAME}}",
    {%- endif -%}
    {%- if item.FUPSESSIONEXC is not none -%}
        FUPSESSIONEXC={{item.FUPSESSIONEXC}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 1.7 //配置业务使用的规则。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_rule_list的变量区（command: ADD RULE） -#}
<!-- MISSING_MACRO: command=ADD RULE list_name=add_rule_list step_id=1.7 -->
```

#### 1.8 //配置规则与用户模板的绑定关系。

```jinja2
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
```

```jinja2
{%- for item in add_rulebinding_list -%}
    ADD RULEBINDING:
    {#- --- 必选参数 --- -#}
    USERPROFILENAME="{{item.USERPROFILENAME}}",
    RULENAME="{{item.RULENAME}}",
    ;
{%- endfor -%}
```

### 2 UDG侧配置

#### 2.1 //打开本特性的License配置开关。

```jinja2
{%- for item in set_licenseswitch_list_1 -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

#### 2.2 //配置三四层过滤条件。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_filter_list的变量区（command: ADD FILTER） -#}
<!-- MISSING_MACRO: command=ADD FILTER list_name=add_filter_list step_id=2.2 -->
```

```jinja2
{%- for item in add_flowfilter_list -%}
    ADD FLOWFILTER:
    {#- --- 必选参数 --- -#}
    FLOWFILTERNAME="{{item.FLOWFILTERNAME}}",
    ;
{%- endfor -%}
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_fltbindflowf_list的变量区（command: ADD FLTBINDFLOWF） -#}
<!-- MISSING_MACRO: command=ADD FLTBINDFLOWF list_name=add_fltbindflowf_list step_id=2.2 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_refreshsrv_list的变量区（command: SET REFRESHSRV） -#}
<!-- MISSING_MACRO: command=SET REFRESHSRV list_name=set_refreshsrv_list step_id=2.2 -->
```

#### 2.4 //配置累计流量上报的URR ID。

```jinja2
{%- for item in add_urr_list_3 -%}
    ADD URR:
    {#- --- 必选参数 --- -#}
    URRNAME="{{item.URRNAME}}",
    URRID={{item.URRID}},
    USAGERPTMODE={{item.USAGERPTMODE}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：USAGERPTMODE=MONITORINGKEY 时必选 --- -#}
    {%- if item.USAGERPTMODE == 'MONITORINGKEY' -%}
        MONITORINGKEY="{{item.MONITORINGKEY}}",
    {%- endif -%}
    {#- --- 条件必选：USAGERPTMODE=OFFLINE 时必选 --- -#}
    {%- if item.USAGERPTMODE == 'OFFLINE' -%}
        OFFCOMPOUNDTYPE={{item.OFFCOMPOUNDTYPE}},
    {%- endif -%}
    {#- --- 条件必选：USAGERPTMODE=ONLINE 时必选 --- -#}
    {%- if item.USAGERPTMODE == 'ONLINE' -%}
        ONLCOMPOUNDTYPE={{item.ONLCOMPOUNDTYPE}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
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

#### 2.5 //配置配额耗尽前的计费策略。

```jinja2
{%- for item in add_urr_list_4 -%}
    ADD URR:
    {#- --- 必选参数 --- -#}
    URRNAME="{{item.URRNAME}}",
    URRID={{item.URRID}},
    USAGERPTMODE={{item.USAGERPTMODE}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：USAGERPTMODE=MONITORINGKEY 时必选 --- -#}
    {%- if item.USAGERPTMODE == 'MONITORINGKEY' -%}
        MONITORINGKEY="{{item.MONITORINGKEY}}",
    {%- endif -%}
    {#- --- 条件必选：USAGERPTMODE=OFFLINE 时必选 --- -#}
    {%- if item.USAGERPTMODE == 'OFFLINE' -%}
        OFFCOMPOUNDTYPE={{item.OFFCOMPOUNDTYPE}},
    {%- endif -%}
    {#- --- 条件必选：USAGERPTMODE=ONLINE 时必选 --- -#}
    {%- if item.USAGERPTMODE == 'ONLINE' -%}
        ONLCOMPOUNDTYPE={{item.ONLCOMPOUNDTYPE}},
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
{%- for item in add_urrgroup_list_2 -%}
    ADD URRGROUP:
    {#- --- 必选参数 --- -#}
    URRGROUPNAME="{{item.URRGROUPNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.UPURRNAME1 is not none -%}
        UPURRNAME1="{{item.UPURRNAME1}}",
    {%- endif -%}
    {%- if item.UPURRNAME2 is not none -%}
        UPURRNAME2="{{item.UPURRNAME2}}",
    {%- endif -%}
    {%- if item.DOWNURRNAME1 is not none -%}
        DOWNURRNAME1="{{item.DOWNURRNAME1}}",
    {%- endif -%}
    {%- if item.DOWNURRNAME2 is not none -%}
        DOWNURRNAME2="{{item.DOWNURRNAME2}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_pccpolicygrp_list_2 -%}
    ADD PCCPOLICYGRP:
    {#- --- 必选参数 --- -#}
    PCCPOLICYGRPNM="{{item.PCCPOLICYGRPNM}}",
    {#- --- 可选参数 --- -#}
    {%- if item.URRGROUPNAME is not none -%}
        URRGROUPNAME="{{item.URRGROUPNAME}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 2.7 //配置规则。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_rule_list_2的变量区（command: ADD RULE） -#}
<!-- MISSING_MACRO: command=ADD RULE list_name=add_rule_list_2 step_id=2.7 -->
```

#### 2.8 //配置业务策略组合。

```jinja2
{%- for item in add_userprofile_list_1 -%}
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
```

```jinja2
{%- for item in add_rulebinding_list_2 -%}
    ADD RULEBINDING:
    {#- --- 必选参数 --- -#}
    USERPROFILENAME="{{item.USERPROFILENAME}}",
    RULENAME="{{item.RULENAME}}",
    ;
{%- endfor -%}
```


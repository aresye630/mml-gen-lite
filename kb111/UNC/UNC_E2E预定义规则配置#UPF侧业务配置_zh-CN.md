---
id: ''
name: UPF侧业务配置
ne_type: UNC
type: feature
description: 根据整体方案设计，SMF侧需配置1个预定义规则与1个预定义规则组：  * 规则名“Rule\_Normal”：关键参数为5QI=5，ARP=2，MFBR=100 Mbit/s及流描述。 * 规则组名“up\_Exhaust”：关键参数为5QI=5，ARP=2，MFBR=1 Kbit/s、流描述及重定向。
risk_level: ''
doc_source: ["网络部署","业务专题","5G PCC之SM策略解决方案","典型业务场景E2E方案设计","业务重定向方案（预定义+动态）","E2E业务配置","E2E预定义规则配置","UPF侧业务配置"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
根据整体方案设计，SMF侧需配置1个预定义规则与1个预定义规则组：* 规则名“Rule\_Normal”：关键参数为5QI=5，ARP=2，MFBR=100 Mbit/s及流描述。* 规则组名“up\_Exhaust”：关键参数为5QI=5，ARP=2，MFBR=1 Kbit/s、流描述及重定向。

## 必备事项
前提条件

* 请仔细阅读UDG特性之《GWFD-020351 PCC基本功能》。
* 完成加载License（如果有需求，请联系华为技术支持工程师）。
* 已通过学习SM策略E2E实现原理、业务配置方法及E2E业务调测了解了SM策略的配置原理及方法。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    add_filter_list:
      type: items
      properties:
        FILTERNAME:
          name: '过滤器名称'
          type: string
          required: false
          description: '不同过滤器之间，该参数不能重复。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        L34PROTTYPE:
          name: '三四层IPv4协议输入类型'
          type: string
          required: false
          description: 'Any to any的三四层filter。'
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
    add_filter_list_1:
      type: items
      properties:
        FILTERNAME:
          name: '过滤器名称'
          type: string
          required: false
          description: '不同过滤器之间，该参数不能重复。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        L34PROTTYPE:
          name: '三四层IPv4协议输入类型'
          type: string
          required: false
          description: 'Any to any的三四层filter。'
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
    add_flowfilter_list:
      type: items
      properties:
        FLOWFILTERNAME:
          name: '流过滤器名称'
          type: string
          required: false
          description: '不同流过滤器之间，该参数不能重复。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_fltbindflowf_list:
      type: items
      properties:
        FLOWFILTERNAME:
          name: '流过滤器名称'
          type: string
          required: false
          description: '使用**ADD FLOWFILTER**命令定义的流过滤器名称。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        FILTERNAME:
          name: '过滤器名称'
          type: string
          required: false
          description: '使用**ADD FILTER**命令定义的过滤器名称。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_flowfilter_list_1:
      type: items
      properties:
        FLOWFILTERNAME:
          name: '流过滤器名称'
          type: string
          required: false
          description: '不同流过滤器之间，该参数不能重复。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_fltbindflowf_list_1:
      type: items
      properties:
        FLOWFILTERNAME:
          name: '流过滤器名称'
          type: string
          required: false
          description: '使用**ADD FLOWFILTER**命令定义的流过滤器名称。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        FILTERNAME:
          name: '过滤器名称'
          type: string
          required: false
          description: '使用**ADD FILTER**命令定义的过滤器名称。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_l7filter_list:
      type: items
      properties:
        L7FILTERNAME:
          name: '七层过滤器名称'
          type: string
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SUBL7FLTNAME:
          name: '子七层过滤器名称'
          type: string
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_flowfilter_list_2:
      type: items
      properties:
        FLOWFILTERNAME:
          name: '流过滤器名称'
          type: string
          required: false
          description: '不同流过滤器之间，该参数不能重复。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        TETHERDETFLAG:
          name: 'TETHERDETFLAG'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_protbindflowf_list:
      type: items
      properties:
        FLOWFILTERNAME:
          name: '流过滤器名称'
          type: string
          required: false
          description: '使用**ADD FLOWFILTER**命令定义的流过滤器名称。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        PROTOCOLNAME:
          name: '协议名称'
          type: string
          required: false
          description: '该参数须根据运营商实际规划具体分析确定。'
          data_source: '与对端协商'
          pattern: ''
          default: ''
        L7FILTERNAME:
          name: '七层过滤器名字'
          type: string
          required: false
          description: '使用**ADD L7FILTER**命令定义的七层过滤器名称。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_filter_list_2:
      type: items
      properties:
        FILTERNAME:
          name: '过滤器名称'
          type: string
          required: false
          description: '不同过滤器之间，该参数不能重复。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        L34PROTTYPE:
          name: '三四层IPv4协议输入类型'
          type: string
          required: false
          description: 'Any to any的三四层filter。'
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
    add_flowfilter_list_3:
      type: items
      properties:
        FLOWFILTERNAME:
          name: '流过滤器名称'
          type: string
          required: false
          description: '不同流过滤器之间，该参数不能重复。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        TETHERDETFLAG:
          name: 'TETHERDETFLAG'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_protbindflowf_list_1:
      type: items
      properties:
        FLOWFILTERNAME:
          name: '流过滤器名称'
          type: string
          required: false
          description: '使用**ADD FLOWFILTER**命令定义的流过滤器名称。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        PROTOCOLNAME:
          name: '协议名称'
          type: string
          required: false
          description: '该参数须根据运营商实际规划具体分析确定。'
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
          description: '存在多条记录时，该参数不能重复。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        URRID:
          name: 'URR标识'
          type: integer
          minimum: 0
          maximum: 2147483646
          required: true
          description: '该参数需要与UPF上的URR标识保持一致。'
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
          data_source: '固定取值'
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
    add_qosprop_list:
      type: items
      properties:
        QOSPROPNAME:
          name: 'QoS属性名称'
          type: string
          maxLength: 31
          required: true
          description: '存在多条记录时，不能重复。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        MBRUPLKVALUE:
          name: '最大上行比特率'
          type: integer
          minimum: 0
          maximum: 20000000
          required: false
          description: '此处数据仅为举例，请根据业务模型进行规划。  创建专有QoSFlow/专有承载时，以SMF上此处配置的为准。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        MBRDNLKVALUE:
          name: '最大下行比特率'
          type: integer
          minimum: 0
          maximum: 20000000
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        QOSTYPE:
          name: 'QoS属性类型'
          type: string
          enum:
          - QOS_BEARER_PARA
          - QOS_FLOW_PARA
          - QOS_L2_PARA
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ARPVALUE:
          name: '分配保留优先级'
          type: integer
          minimum: 1
          maximum: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        FQI:
          name: '5G QoS标识'
          type: integer
          minimum: 1
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        QOSURRNAME:
          name: 'QoS使用量上报规则名称'
          type: string
          maxLength: 31
          required: false
          description: '使用**ADD URR**定义的URRNAME。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        EMPCAP:
          name: 'QoS抢占能力'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '该业务可以抢占已经分配给其他低优先级业务流的资源时，设置为ENABLE。此处以不抢占为例。'
          data_source: '本端规划'
          pattern: ''
          default: DISABLE
        EMPVUL:
          name: 'QoS被抢占设置'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '其他高优先级业务不能抢占本业务流的资源时，设置为DISABLE。此处以被抢占为例。'
          data_source: '本端规划'
          pattern: ''
          default: ENABLE
        QCIVALUE:
          name: 'QoS等级标识'
          type: integer
          minimum: 1
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RQI:
          name: '反射QoS指示'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_qosprop_list_1:
      type: items
      properties:
        QOSPROPNAME:
          name: 'QoS属性名称'
          type: string
          maxLength: 31
          required: true
          description: '存在多条记录时，不能重复。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        MBRUPLKVALUE:
          name: '最大上行比特率'
          type: integer
          minimum: 0
          maximum: 20000000
          required: false
          description: '此处数据仅为举例，请根据业务模型进行规划。  创建专有QoSFlow/专有承载时，以SMF上此处配置的为准。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        MBRDNLKVALUE:
          name: '最大下行比特率'
          type: integer
          minimum: 0
          maximum: 20000000
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        QOSTYPE:
          name: 'QoS属性类型'
          type: string
          enum:
          - QOS_BEARER_PARA
          - QOS_FLOW_PARA
          - QOS_L2_PARA
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ARPVALUE:
          name: '分配保留优先级'
          type: integer
          minimum: 1
          maximum: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        FQI:
          name: '5G QoS标识'
          type: integer
          minimum: 1
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        QOSURRNAME:
          name: 'QoS使用量上报规则名称'
          type: string
          maxLength: 31
          required: false
          description: '使用**ADD URR**定义的URRNAME。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        EMPCAP:
          name: 'QoS抢占能力'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '该业务可以抢占已经分配给其他低优先级业务流的资源时，设置为ENABLE。此处以不抢占为例。'
          data_source: '本端规划'
          pattern: ''
          default: DISABLE
        EMPVUL:
          name: 'QoS被抢占设置'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '其他高优先级业务不能抢占本业务流的资源时，设置为DISABLE。此处以被抢占为例。'
          data_source: '本端规划'
          pattern: ''
          default: ENABLE
        QCIVALUE:
          name: 'QoS等级标识'
          type: integer
          minimum: 1
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RQI:
          name: '反射QoS指示'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_redirect_list:
      type: items
      properties:
        REDIRECTNAME:
          name: '重定向名称'
          type: string
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        URL:
          name: 'URL'
          type: string
          required: false
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: ''
    add_redirect_list_1:
      type: items
      properties:
        REDIRECTNAME:
          name: '重定向名称'
          type: string
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        URL:
          name: 'URL'
          type: string
          required: false
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: ''
    add_pccactionprop_list:
      type: items
      properties:
        PCCACTPROPNAME:
          name: 'PCC动作属性名称'
          type: string
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        UPINITREDIRNM:
          name: '上行发起重定向名称'
          type: string
          required: false
          description: '使用**ADD REDIRECT**命令定义的重定向名称。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        UPINITUPGATE:
          name: 'UPINITUPGATE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        UPINITDNGATE:
          name: 'UPINITDNGATE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DNINITUPGATE:
          name: 'DNINITUPGATE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DNINITDNGATE:
          name: 'DNINITDNGATE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_pccpolicygrp_list:
      type: items
      properties:
        PCCPOLICYGRPNM:
          name: 'PCC策略组名称'
          type: string
          required: false
          description: '存在多条记录时，该参数不能重复。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        TOKENFUNCFLAG:
          name: 'TOKENFUNCFLAG'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        URRGROUPNAME:
          name: '使用量上报规则组名称'
          type: string
          required: false
          description: '使用**ADD URRGROUP**定义的“URRGROUPNAME”。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        SIGURRGRPNAME:
          name: 'SIGURRGRPNAME'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        QOSPROPNAME:
          name: 'QoS属性名称'
          type: string
          required: false
          description: '使用**ADD QOSPROP**定义的**QOSPROPNAME**。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_pccpolicygrp_list_1:
      type: items
      properties:
        PCCPOLICYGRPNM:
          name: 'PCC策略组名称'
          type: string
          required: false
          description: '存在多条记录时，该参数不能重复。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        TOKENFUNCFLAG:
          name: 'TOKENFUNCFLAG'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        URRGROUPNAME:
          name: '使用量上报规则组名称'
          type: string
          required: false
          description: '使用**ADD URRGROUP**定义的“URRGROUPNAME”。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        SIGURRGRPNAME:
          name: 'SIGURRGRPNAME'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        QOSPROPNAME:
          name: 'QoS属性名称'
          type: string
          required: false
          description: '使用**ADD QOSPROP**定义的**QOSPROPNAME**。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_pccpolicygrp_list_2:
      type: items
      properties:
        PCCPOLICYGRPNM:
          name: 'PCC策略组名称'
          type: string
          required: false
          description: '存在多条记录时，该参数不能重复。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PCCACTPROPNAME:
          name: 'PCC动作属性名称'
          type: string
          required: false
          description: '使用**ADD PCCACTIONPROP**命令中定义的PCC动作属性名称。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_rule_list:
      type: items
      properties:
        RULENAME:
          name: '规则名称'
          type: string
          required: false
          description: '存在多条数据时，该参数+策略类型不能完全相同。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        POLICYTYPE:
          name: '策略类型'
          type: string
          required: false
          description: '需根据业务策略选择相应的策略类型。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        FILTERINGMODE:
          name: 'FILTERINGMODE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        FLOWFILTERNAME:
          name: '流过滤器名称'
          type: string
          required: false
          description: '使用**ADD FLOWFILTER**命令定义的流过滤器名称。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        PRIORITY:
          name: '全局优先级'
          type: string
          required: false
          description: '值越小，优先级越高。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        POLICYNAME:
          name: '策略名称'
          type: string
          required: false
          description: '使用**ADD PCCPOLICYGRP**定义的“PCCPOLICYGRPNM”。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_userprofile_list:
      type: items
      properties:
        USERPROFILENAME:
          name: '用户模板名称'
          type: string
          required: false
          description: '与UPF上配置的用户模板名称保持一致。'
          data_source: '与对端协商'
          pattern: ''
          default: ''
        ALIASMARKFLAG:
          name: 'ALIASMARKFLAG'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DDOSCHECK:
          name: 'DDOSCHECK'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CAPMODETHRES:
          name: 'CAPMODETHRES'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LOCRPTSWITCH:
          name: 'LOCRPTSWITCH'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TETHERINGMAXNUM:
          name: 'TETHERINGMAXNUM'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        UPTYPE:
          name: '用户模板类型'
          type: string
          required: false
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: ''
    add_rulebinding_list:
      type: items
      properties:
        USERPROFILENAME:
          name: '模板名称'
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
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_refreshsrv_list:
      type: items
      properties:
        REFRESHTYPE:
          name: 'REFRESHTYPE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    add_filter_list:
    - FILTERNAME: f_fup_service_100M
      L34PROTTYPE: STRING
      L34PROTOCOL: ANY
    add_filter_list_1:
    - FILTERNAME: f_fup_service_1K
      L34PROTTYPE: STRING
      L34PROTOCOL: ANY
    add_flowfilter_list:
    - FLOWFILTERNAME: flowfliter_service_100M
    add_fltbindflowf_list:
    - FLOWFILTERNAME: flowfliter_service_100M
      FILTERNAME: f_fup_service_100M
    add_flowfilter_list_1:
    - FLOWFILTERNAME: flowfliter_service_1K
    add_fltbindflowf_list_1:
    - FLOWFILTERNAME: flowfliter_service_1K
      FILTERNAME: f_fup_service_1K
    add_l7filter_list:
    - L7FILTERNAME: f_Redirection
      SUBL7FLTNAME: f_SubRedirection
    add_flowfilter_list_2:
    - FLOWFILTERNAME: flowfliter_Redirection
      TETHERDETFLAG: FILTER
    add_protbindflowf_list:
    - FLOWFILTERNAME: flowfliter_Redirection
      PROTOCOLNAME: http
      L7FILTERNAME: f_Redirection
    add_filter_list_2:
    - FILTERNAME: f_Redirection
      L34PROTTYPE: STRING
      L34PROTOCOL: ANY
    add_flowfilter_list_3:
    - FLOWFILTERNAME: flowfliter_Redirection
      TETHERDETFLAG: FILTER
    add_protbindflowf_list_1:
    - FLOWFILTERNAME: flowfliter_Redirection
      PROTOCOLNAME: http
    add_urr_list:
    - URRNAME: 'urr_QoS2'
      URRID: 2
      USAGERPTMODE: QOS
      MONITORINGKEY: ''
      N40AGESW: ENABLE
      OFCSRVTMPLNAME: ''
      OFFCOMPOUNDTYPE: ''
      OFFMETERINGTYPE: ''
      ONLCOMPOUNDTYPE: ''
      ONLMETERINGTYPE: ''
      REDIRENDTOKEN: ''
    add_urrgroup_list:
    - URRGROUPNAME: 'urrg_qos_service'
      UPURRNAME1: 'urr_MK'
      DOWNURRNAME1: 'urr_MK'
    add_qosprop_list:
    - QOSPROPNAME: 'qosprop_5qi5_arp2_100M'
      MBRUPLKVALUE: 100000
      MBRDNLKVALUE: 100000
      QOSTYPE: QOS_FLOW_PARA
      ARPVALUE: 2
      FQI: 5
      QOSURRNAME: 'urr_QoS2'
      EMPCAP: DISABLE
      EMPVUL: ENABLE
      QCIVALUE: ''
      RQI: ''
    add_qosprop_list_1:
    - QOSPROPNAME: 'qosprop_5qi5_arp2_1K'
      MBRUPLKVALUE: 1
      MBRDNLKVALUE: 1
      QOSTYPE: QOS_FLOW_PARA
      ARPVALUE: 2
      FQI: 5
      QOSURRNAME: 'urr_QoS3'
      EMPCAP: DISABLE
      EMPVUL: ENABLE
      QCIVALUE: ''
      RQI: ''
    add_redirect_list:
    - REDIRECTNAME: Redirect_Name
      URL: www.example.com
    add_redirect_list_1:
    - REDIRECTNAME: Redirect_Name
      URL: http://172.30.26.103:8080
    add_pccactionprop_list:
    - PCCACTPROPNAME: PCCAction_Name
      UPINITREDIRNM: Redirect_Name
      UPINITUPGATE: PASS
      UPINITDNGATE: PASS
      DNINITUPGATE: DISCARD
      DNINITDNGATE: DISCARD
    add_pccpolicygrp_list:
    - PCCPOLICYGRPNM: pccfuppolicy_100M
      TOKENFUNCFLAG: DISABLE
      URRGROUPNAME: urrg_qos_service
      SIGURRGRPNAME: urrg_qos_service
      QOSPROPNAME: qosprop_5qi5_arp2_100M
    add_pccpolicygrp_list_1:
    - PCCPOLICYGRPNM: pccfuppolicy_1K
      TOKENFUNCFLAG: DISABLE
      URRGROUPNAME: urrg_qos_service
      SIGURRGRPNAME: urrg_qos_service
      QOSPROPNAME: qosprop_5qi5_arp2_1K
    add_pccpolicygrp_list_2:
    - PCCPOLICYGRPNM: pccfuppolicy_Redir
      PCCACTPROPNAME: PCCAction_Name
    add_rule_list:
    - RULENAME: Rule_Normal
      POLICYTYPE: PCC
      FILTERINGMODE: FLOWFILTER
      FLOWFILTERNAME: flowfliter_service_100M
      PRIORITY: '10'
      POLICYNAME: pccfuppolicy_100M
    add_userprofile_list:
    - USERPROFILENAME: up_Exhaust
      ALIASMARKFLAG: DISABLE
      DDOSCHECK: DISABLE
      CAPMODETHRES: '0'
      LOCRPTSWITCH: INHERIT
      TETHERINGMAXNUM: '255'
      UPTYPE: PCC
    add_rulebinding_list:
    - USERPROFILENAME: 'up_Exhaust'
      RULENAME: 'Rule_Exhaust'
    set_refreshsrv_list:
    - REFRESHTYPE: ALL
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 登录UDG CSP OM Portal，进入“MML命令行-UDG”窗口。

### 2 配置L3/4层流过滤器。

#### 2.1 用户配额耗尽前，即PCF下发预定义规则“Rule\_Normal”场景。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_filter_list的变量区（command: ADD FILTER） -#}
<!-- MISSING_MACRO: command=ADD FILTER list_name=add_filter_list step_id=2.1 -->
```

#### 2.2 用户配额耗尽后，即PCF下发预定义规则“up\_Exhaust”场景。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_filter_list_1的变量区（command: ADD FILTER） -#}
<!-- MISSING_MACRO: command=ADD FILTER list_name=add_filter_list_1 step_id=2.2 -->
```

### 3 添加L3/4层流过滤器并绑定过滤器。

#### 3.1 用户配额耗尽前，即PCF下发预定义规则“Rule\_Normal”场景。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_flowfilter_list的变量区（command: ADD FLOWFILTER） -#}
<!-- MISSING_MACRO: command=ADD FLOWFILTER list_name=add_flowfilter_list step_id=3.1 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_fltbindflowf_list的变量区（command: ADD FLTBINDFLOWF） -#}
<!-- MISSING_MACRO: command=ADD FLTBINDFLOWF list_name=add_fltbindflowf_list step_id=3.1 -->
```

#### 3.2 用户配额耗尽后，即PCF下发预定义规则“up\_Exhaust”场景。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_flowfilter_list_1的变量区（command: ADD FLOWFILTER） -#}
<!-- MISSING_MACRO: command=ADD FLOWFILTER list_name=add_flowfilter_list_1 step_id=3.2 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_fltbindflowf_list_1的变量区（command: ADD FLTBINDFLOWF） -#}
<!-- MISSING_MACRO: command=ADD FLTBINDFLOWF list_name=add_fltbindflowf_list_1 step_id=3.2 -->
```

### 4 添加重定向场景流过滤器（两种配置选一种即可）

#### 4.1 采用7层流过滤配置

#### 添加过滤器

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_l7filter_list的变量区（command: ADD L7FILTER） -#}
<!-- MISSING_MACRO: command=ADD L7FILTER list_name=add_l7filter_list step_id=4.1 -->
```

#### 添加流过滤器及绑定关系

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_flowfilter_list_2的变量区（command: ADD FLOWFILTER） -#}
<!-- MISSING_MACRO: command=ADD FLOWFILTER list_name=add_flowfilter_list_2 step_id=4.1 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_protbindflowf_list的变量区（command: ADD PROTBINDFLOWF） -#}
<!-- MISSING_MACRO: command=ADD PROTBINDFLOWF list_name=add_protbindflowf_list step_id=4.1 -->
```

#### 4.2 采用L3/4层流过滤配置

#### 添加过滤器

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_filter_list_2的变量区（command: ADD FILTER） -#}
<!-- MISSING_MACRO: command=ADD FILTER list_name=add_filter_list_2 step_id=4.2 -->
```

#### 添加流过滤器及绑定关系

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_flowfilter_list_3的变量区（command: ADD FLOWFILTER） -#}
<!-- MISSING_MACRO: command=ADD FLOWFILTER list_name=add_flowfilter_list_3 step_id=4.2 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_protbindflowf_list_1的变量区（command: ADD PROTBINDFLOWF） -#}
<!-- MISSING_MACRO: command=ADD PROTBINDFLOWF list_name=add_protbindflowf_list_1 step_id=4.2 -->
```

### 5 配置使用量上报属性。

#### 5.1 此处的配置须与SMF侧配置保持严格一致。

#### //配置QoS URR、MK URR及URR Group绑定关系

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

### 6 配置QoS参数。

### 该步骤为预定义规则（组）场景下的可选配置。只有在需要对用户进行带宽控制或建立专有QoS Flow时，才需配置。须配置配额耗尽前、耗尽后两种场景的带宽控制策略。

#### 6.1 用户配额耗尽前，此处5QI/ARP取值参考SMF（UNC）侧业务设计规划分别取5和2。

```jinja2
{%- if is_optional_qos_params and is_scenario_quota_normal -%}
    {%- for item in add_qosprop_list -%}
        ADD QOSPROP:
        {#- --- 必选参数 --- -#}
        QOSPROPNAME="{{item.QOSPROPNAME}}",
        QOSTYPE={{item.QOSTYPE}},
        {#- --- 可选参数 --- -#}
        {%- if item.MBRUPLKVALUE is not none -%}
            MBRUPLKVALUE={{item.MBRUPLKVALUE}},
        {%- endif -%}
        {%- if item.MBRDNLKVALUE is not none -%}
            MBRDNLKVALUE={{item.MBRDNLKVALUE}},
        {%- endif -%}
        {%- if item.EMPCAP is not none -%}
            EMPCAP={{item.EMPCAP}},
        {%- endif -%}
        {%- if item.EMPVUL is not none -%}
            EMPVUL={{item.EMPVUL}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：QOSTYPE=QOS_FLOW_PARA/QOS_L2_PARA 时必选 --- -#}
        {%- if item.QOSTYPE in ['QOS_FLOW_PARA', 'QOS_L2_PARA'] -%}
            FQI={{item.FQI}},
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：QOSTYPE=QOS_BEARER_PARA/QOS_FLOW_PARA 时可选 --- -#}
        {%- if item.QOSTYPE in ['QOS_BEARER_PARA', 'QOS_FLOW_PARA'] -%}
            {%- if item.QOSURRNAME is not none -%}
                QOSURRNAME="{{item.QOSURRNAME}}",
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOSTYPE=QOS_BEARER_PARA 时可选 --- -#}
        {%- if item.QOSTYPE == 'QOS_BEARER_PARA' -%}
            {%- if item.QCIVALUE is not none -%}
                QCIVALUE={{item.QCIVALUE}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOSTYPE=QOS_FLOW_PARA 时可选 --- -#}
        {%- if item.QOSTYPE == 'QOS_FLOW_PARA' -%}
            {%- if item.RQI is not none -%}
                RQI={{item.RQI}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件必选/可选参数 --- -#}
        {#- --- 分配保留优先级: 条件必选(QoS属性类型=QOS_FLOW_PARA|QOS_L2_PARA) / 条件可选(QoS属性类型=QOS_BEARER_PARA) --- -#}
        {%- if (item.QOSTYPE in ['QOS_FLOW_PARA', 'QOS_L2_PARA']) -%}
            ARPVALUE={{item.ARPVALUE}},
        {%- elif (item.QOSTYPE == 'QOS_BEARER_PARA') -%}
            {%- if item.ARPVALUE is not none -%}
                ARPVALUE={{item.ARPVALUE}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 6.2 用户配额耗尽后，此处5QI/ARP取值参考SMF（UNC）侧业务设计规划分别取5和2。

```jinja2
{%- if is_optional_qos_params and is_scenario_quota_exhaust -%}
    {%- for item in add_qosprop_list_1 -%}
        ADD QOSPROP:
        {#- --- 必选参数 --- -#}
        QOSPROPNAME="{{item.QOSPROPNAME}}",
        QOSTYPE={{item.QOSTYPE}},
        {#- --- 可选参数 --- -#}
        {%- if item.MBRUPLKVALUE is not none -%}
            MBRUPLKVALUE={{item.MBRUPLKVALUE}},
        {%- endif -%}
        {%- if item.MBRDNLKVALUE is not none -%}
            MBRDNLKVALUE={{item.MBRDNLKVALUE}},
        {%- endif -%}
        {%- if item.EMPCAP is not none -%}
            EMPCAP={{item.EMPCAP}},
        {%- endif -%}
        {%- if item.EMPVUL is not none -%}
            EMPVUL={{item.EMPVUL}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：QOSTYPE=QOS_FLOW_PARA/QOS_L2_PARA 时必选 --- -#}
        {%- if item.QOSTYPE in ['QOS_FLOW_PARA', 'QOS_L2_PARA'] -%}
            FQI={{item.FQI}},
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：QOSTYPE=QOS_BEARER_PARA/QOS_FLOW_PARA 时可选 --- -#}
        {%- if item.QOSTYPE in ['QOS_BEARER_PARA', 'QOS_FLOW_PARA'] -%}
            {%- if item.QOSURRNAME is not none -%}
                QOSURRNAME="{{item.QOSURRNAME}}",
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOSTYPE=QOS_BEARER_PARA 时可选 --- -#}
        {%- if item.QOSTYPE == 'QOS_BEARER_PARA' -%}
            {%- if item.QCIVALUE is not none -%}
                QCIVALUE={{item.QCIVALUE}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOSTYPE=QOS_FLOW_PARA 时可选 --- -#}
        {%- if item.QOSTYPE == 'QOS_FLOW_PARA' -%}
            {%- if item.RQI is not none -%}
                RQI={{item.RQI}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件必选/可选参数 --- -#}
        {#- --- 分配保留优先级: 条件必选(QoS属性类型=QOS_FLOW_PARA|QOS_L2_PARA) / 条件可选(QoS属性类型=QOS_BEARER_PARA) --- -#}
        {%- if (item.QOSTYPE in ['QOS_FLOW_PARA', 'QOS_L2_PARA']) -%}
            ARPVALUE={{item.ARPVALUE}},
        {%- elif (item.QOSTYPE == 'QOS_BEARER_PARA') -%}
            {%- if item.ARPVALUE is not none -%}
                ARPVALUE={{item.ARPVALUE}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 7 配置重定向及绑定关系。

### 添加重定向URL等信息（根据实际情况选择如下两种配置中的一种即可）。

#### 7.1 //7层流对应的重定向配置

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_redirect_list的变量区（command: ADD REDIRECT） -#}
<!-- MISSING_MACRO: command=ADD REDIRECT list_name=add_redirect_list step_id=7.1 -->
```

#### 7.2 //L3/4层流对应的重定向配置

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_redirect_list_1的变量区（command: ADD REDIRECT） -#}
<!-- MISSING_MACRO: command=ADD REDIRECT list_name=add_redirect_list_1 step_id=7.2 -->
```

### 添加PCC动作用于绑定重定向内容。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_pccactionprop_list的变量区（command: ADD PCCACTIONPROP） -#}
<!-- MISSING_MACRO: command=ADD PCCACTIONPROP list_name=add_pccactionprop_list step_id=7 -->
```

### 8 配置PCC策略组。

### 该步骤为预定义规则（组）场景下的必选配置。配置PCC策略组的目的是用于关联QoS URR策略。此处“URRGROUPNAME”参数使用ADD URRGROUP定义的“URRGROUPNAME”。

#### 8.1 用户配额耗尽前，即PCF下发预定义规则“Rule\_Normal”场景。

##### 8.1.1 //PCC策略关联QoS URR Group及MK URR Group

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_pccpolicygrp_list的变量区（command: ADD PCCPOLICYGRP） -#}
<!-- MISSING_MACRO: command=ADD PCCPOLICYGRP list_name=add_pccpolicygrp_list step_id=8.1.1 -->
```

#### 8.2 用户配额耗尽后，即PCF下发预定义规则“up\_Exhaust”场景。

##### 8.2.1 //PCC策略关联QoS URR Group及MK URR Group

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_pccpolicygrp_list_1的变量区（command: ADD PCCPOLICYGRP） -#}
<!-- MISSING_MACRO: command=ADD PCCPOLICYGRP list_name=add_pccpolicygrp_list_1 step_id=8.2.1 -->
```

##### 8.2.2 //PCC策略绑定重定向

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_pccpolicygrp_list_2的变量区（command: ADD PCCPOLICYGRP） -#}
<!-- MISSING_MACRO: command=ADD PCCPOLICYGRP list_name=add_pccpolicygrp_list_2 step_id=8.2.2 -->
```

### 9 配置预定义规则。

### 该步骤为预定义规则（组）场景下的必选配置。主要用于关联PCC策略组。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_rule_list的变量区（command: ADD RULE） -#}
<!-- MISSING_MACRO: command=ADD RULE list_name=add_rule_list step_id=9 -->
```

### 10 （配额耗尽场景）配置预定义规则组。

### 添加UserProfile

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_userprofile_list的变量区（command: ADD USERPROFILE） -#}
<!-- MISSING_MACRO: command=ADD USERPROFILE list_name=add_userprofile_list step_id=10 -->
```

### 添加规则与UserProfile绑定关系

```jinja2
{%- if is_scenario_quota_exhaust -%}
    {%- for item in add_rulebinding_list -%}
        ADD RULEBINDING:
        {#- --- 必选参数 --- -#}
        USERPROFILENAME="{{item.USERPROFILENAME}}",
        RULENAME="{{item.RULENAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

### 11 将新配置的Filter置为生效。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_refreshsrv_list的变量区（command: SET REFRESHSRV） -#}
<!-- MISSING_MACRO: command=SET REFRESHSRV list_name=set_refreshsrv_list step_id=11 -->
```


---
id: ''
name: 激活业务触发的QoS保证
ne_type: UNC
type: feature
description: 当运营商规划需要为指定业务提供专有承载/专有QoS Flow时，需要参考本页面进行配置。  适用于GGSN、PGW-C、SMF。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","智能PCC解决方案","WSFD-109107 业务触发的QoS保证","激活业务触发的QoS保证"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
当运营商规划需要为指定业务提供专有承载/专有QoS Flow时，需要参考本页面进行配置。适用于GGSN、PGW-C、SMF。

## 必备事项
前提条件

* 请仔细阅读WSFD-109107 业务触发的QoS保证。
* 完成加载license（如果有需求，请联系华为技术支持工程师处理）。
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
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SWITCH:
          name: '开关'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: true
          description: ''
          data_source: ''
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
          description: '存在多条记录时，不能重复。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        URRID:
          name: 'URR标识'
          type: integer
          minimum: 0
          maximum: 2147483646
          required: true
          description: 'URRID在所有URR内唯一，建议分配大于1000的值。'
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
    add_qosprop_list:
      type: items
      properties:
        QOSPROPNAME:
          name: 'QoS属性名称'
          type: string
          maxLength: 31
          required: true
          description: '存在多条记录时，不能重复。  以5G用户使用的QoSProp名称为qosprop\_501；2/3/4G用户使用的名称为qosprop\_401为例。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        GBRUPLKVALUE:
          name: '保证的上行比特率'
          type: integer
          minimum: 0
          maximum: 20000000
          required: false
          description: '此处数据仅为举例，请根据业务模型进行规划。  创建专有QoSFlow/专有承载时，以SMF上此处配置的为准。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        GBRDNLKVALUE:
          name: '保证的下行比特率'
          type: integer
          minimum: 0
          maximum: 20000000
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        MBRUPLKVALUE:
          name: '最大上行比特率'
          type: integer
          minimum: 0
          maximum: 20000000
          required: false
          description: ''
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
          description: '5G用户使用QOS\_FLOW\_PARA，2/3/4G用户使用QOS\_BEARER\_PARA。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        ARPVALUE:
          name: '分配保留优先级'
          type: integer
          minimum: 1
          maximum: 15
          required: false
          description: '值越小优先级越高。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        FQI:
          name: '5G QoS标识'
          type: integer
          minimum: 1
          maximum: 255
          required: false
          description: '“QOSTYPE”为“QOS\_FLOW\_PARA”时需要规划。'
          data_source: '本端规划'
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
          description: '“QOSTYPE”为“QOS\_BEARER\_PARA”时需要规划。'
          data_source: '全网规划'
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
        QOSPROPNAME:
          name: 'Qos属性名称'
          type: string
          maxLength: 31
          required: false
          description: '使用**ADD QOSPROP**定义的QOSPROPNAME。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_rule_list:
      type: items
      properties:
        RULENAME:
          name: '规则名称'
          type: string
          maxLength: 63
          required: true
          description: '存在多条数据时，该参数+策略类型不能完全相同。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        POLICYTYPE:
          name: '策略类型'
          type: string
          enum:
          - ADC
          - BWM
          - FIREWALL
          - FUP
          - HEADEN
          - IPREDIR
          - LBO
          - NON_SPECIFIC_TYPE
          - PCC
          - QOS
          - REMARK_FPI
          - SMARTREDIRECT
          - SRV_TRIGGER
          - TRAFFICCLASS
          - ULCL
          - WEBPROXY
          required: true
          description: '“POLICYTYPE”设置为“PCC”时，“POLICYNAME”使用**ADD PCCPOLICYGRP**定义的PCCPOLICYGRPNM。  “POLICYTYPE”设置为“QOS”时，“POLICYNAME”使用**ADD QOSPROP**定义的QOSPROPNAME。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        POLICYNAME:
          name: '策略名称'
          type: string
          maxLength: 63
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        FLOWFILTERNAME:
          name: '流过滤器名称'
          type: string
          maxLength: 63
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PROTODESCDL:
          name: '下行协议描述参数'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PROTODESCUL:
          name: '上行协议描述参数'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RULERANGE:
          name: '规则生效范围'
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
    add_rule_list_1:
      type: items
      properties:
        RULENAME:
          name: '规则名称'
          type: string
          maxLength: 63
          required: true
          description: '存在多条数据时，该参数+策略类型不能完全相同。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        POLICYTYPE:
          name: '策略类型'
          type: string
          enum:
          - ADC
          - BWM
          - FIREWALL
          - FUP
          - HEADEN
          - IPREDIR
          - LBO
          - NON_SPECIFIC_TYPE
          - PCC
          - QOS
          - REMARK_FPI
          - SMARTREDIRECT
          - SRV_TRIGGER
          - TRAFFICCLASS
          - ULCL
          - WEBPROXY
          required: true
          description: '“POLICYTYPE”设置为“PCC”时，“POLICYNAME”使用**ADD PCCPOLICYGRP**定义的PCCPOLICYGRPNM。  “POLICYTYPE”设置为“QOS”时，“POLICYNAME”使用**ADD QOSPROP**定义的QOSPROPNAME。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        POLICYNAME:
          name: '策略名称'
          type: string
          maxLength: 63
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        FLOWFILTERNAME:
          name: '流过滤器名称'
          type: string
          maxLength: 63
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PROTODESCDL:
          name: '下行协议描述参数'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PROTODESCUL:
          name: '上行协议描述参数'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RULERANGE:
          name: '规则生效范围'
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
    add_userprofile_list:
      type: items
      properties:
        USERPROFILENAME:
          name: '用户模板名称'
          type: string
          maxLength: 63
          required: true
          description: '配置SMF上的UserProfile。'
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
          description: '将本地rule/预定义规则rule绑定到UserProfile上。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        RULENAME:
          name: '规则名称'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        POLICYTYPE:
          name: '策略类型'
          type: string
          enum:
          - ADC
          - BWM
          - FIREWALL
          - FUP
          - HEADEN
          - IPREDIR
          - LBO
          - NON_SPECIFIC_TYPE
          - PCC
          - QOS
          - REMARK_FPI
          - SMARTREDIRECT
          - SRV_TRIGGER
          - TRAFFICCLASS
          - ULCL
          - WEBPROXY
          required: false
          description: '如果不指定策略类型，则把规则名称相同的所有策略类型的规则绑定到用户模板上。'
          data_source: '本端规划'
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
          description: '配置UserProfile Group。'
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
          description: '将UserProfile绑定到UserProfile Group。'
          data_source: '全网规划'
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
          data_source: ''
          pattern: ''
          default: ''
        USERPROFILENAME:
          name: '用户模板名称'
          type: string
          maxLength: 63
          required: false
          description: ''
          data_source: '本端规划'
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
    add_apnusrprofg_list:
      type: items
      properties:
        APN:
          name: 'APN'
          type: string
          maxLength: 63
          required: true
          description: '将UserProfile Group绑定到DNN。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        USERPROFGNAME:
          name: '用户模板组名称'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_apnidletime_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '-'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        INHERIT:
          name: '继承默认开关'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        HSMFTIMERLEVEL:
          name: 'H-SMF空闲上下文核查级别'
          type: string
          enum:
          - SESSION
          - QOSFLOW
          required: false
          description: '设置QoS Flow级别的SMF（N11）上下文空闲定时器时长时，必须使用样例值。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        DEDQFIDLETIMER:
          name: '专有QoS Flow空闲定时器时长(min)'
          type: integer
          minimum: 5
          maximum: 12000
          required: false
          description: '根据业务模型进行设置。设置过大，会长时间占用上下文资源；设置过小，会强制拆话，删除QoS Flow后还需要重新创建QoS Flow。  此处以600分钟为例，请以局点规划数据为准。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        DFTQFIDLETIMER:
          name: '缺省QoS Flow空闲定时器时长(min)'
          type: integer
          minimum:
          - 0
          - 5
          maximum:
          - 0
          - 12000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        BEARERTIMER:
          name: '承载定时器(min)'
          type: integer
          minimum: 5
          maximum: 12000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DFTBEARPOLICY:
          name: '缺省承载和默认GBR的定时器'
          type: string
          enum:
          - ONEDAY
          - OFF
          - USEBEARERTIMER
          - USESPECIFICVAL
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DFTBRPLCYGGSN:
          name: 'GGSN一次激活上下文定时器'
          type: string
          enum:
          - ONEDAY
          - OFF
          - USEBEARERTIMER
          - USESPECIFICVAL
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GCTXCHKSW:
          name: 'GGSN空闲上下文检查开关'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GULTIMERLEVEL:
          name: 'GUL承载级别参数'
          type: string
          enum:
          - SESSION
          - BEARER
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        HCTXCHKSW:
          name: 'H-SMF空闲上下文核查开关'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        HCTXINACHKSW:
          name: 'H-SMF不活动上下文核查开关'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ICTXCHKSW:
          name: 'I-SMF/V-SMF空闲上下文核查开关'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ICTXINACHKSW:
          name: 'I-SMF/V-SMF不活动上下文核查开关'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IDLEUPDATEMSG:
          name: '空闲超时发送更新消息'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PCTXCHKSW:
          name: 'PGW-C和SGW-C/PGW-C空闲上下文检查开关'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PROS8CTXCHKSW:
          name: 'Proxy-SMF S8空闲上下文核查开关'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PROXYSMFCHKSW:
          name: 'Proxy-SMF 空闲上下文核查开关'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SCTXCHKSW:
          name: 'SGW-C空闲上下文核查开关'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SESSIONTIMER:
          name: '会话定时器时长(min)'
          type: integer
          minimum: 5
          maximum: 12000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SMFSESIDLETIMER:
          name: 'SMF会话空闲定时器时长(min)'
          type: integer
          minimum: 5
          maximum: 12000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SMFSESINATIMER:
          name: 'SMF会话不活动定时器时长(min)'
          type: integer
          minimum: 5
          maximum: 12000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_apndeactqfplcy_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '在收到UE Context Release（CauseRadioNetwork：radio-connection-with-ue-lost），立即释放专有QoS Flow可能影响进行中的业务（如语音）时，需要设置延迟释放时间。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        NGAPCAUSEGROUP:
          name: 'NgApCause组'
          type: string
          enum:
          - RADIO_NETWORK
          - TRANSPORT
          - NAS
          - PROTOCOL
          - MISC
          - INVALID
          required: true
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
        NGAPCAUSEVALUE:
          name: 'NgApCause值'
          type: integer
          minimum: 0
          maximum: 255
          required: true
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
        QFPLCY:
          name: '专有GBR类型QoS Flow处理策略'
          type: string
          enum:
          - RELEASE
          - DELAY_RELEASE
          - NOT_RELEASE
          required: true
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
        DELAYTIMER:
          name: '延迟释放专有GBR类型QoS Flow时长(秒)'
          type: integer
          minimum: 10
          maximum: 100
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: 60
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV3W9STQE11'
      SWITCH: ENABLE
    add_urr_list:
    - URRNAME: 'URR_qos_01'
      URRID: 1005
      USAGERPTMODE: QOS
      MONITORINGKEY: ''
      N40AGESW: ENABLE
      OFCSRVTMPLNAME: ''
      OFFCOMPOUNDTYPE: ''
      OFFMETERINGTYPE: ''
      ONLCOMPOUNDTYPE: ''
      ONLMETERINGTYPE: ''
      REDIRENDTOKEN: ''
    add_qosprop_list:
    - QOSPROPNAME: 'qosprop_501'
      GBRUPLKVALUE: 600
      GBRDNLKVALUE: 6000
      MBRUPLKVALUE: 1000
      MBRDNLKVALUE: 10000
      QOSTYPE: QOS_FLOW_PARA
      ARPVALUE: 5
      FQI: 2
      QOSURRNAME: 'URR_qos_01'
      EMPCAP: DISABLE
      EMPVUL: ENABLE
      QCIVALUE: 66
      RQI: ''
    add_pccpolicygrp_list:
    - PCCPOLICYGRPNM: 'pccpolicy_group'
      QOSPROPNAME: 'qosprop_501'
    add_rule_list:
    - RULENAME: 'rule_test'
      POLICYTYPE: PCC
      POLICYNAME: 'pccpolicy_group'
      FLOWFILTERNAME: ''
      PROTODESCDL: ''
      PROTODESCUL: ''
      RULERANGE: ALL
    add_rule_list_1:
    - RULENAME: 'rule_test'
      POLICYTYPE: QOS
      POLICYNAME: 'qosprop_501'
      FLOWFILTERNAME: ''
      PROTODESCDL: ''
      PROTODESCUL: ''
      RULERANGE: ALL
    add_userprofile_list:
    - USERPROFILENAME: 'up_test'
      UPTYPE: PCC
      PROFILERANGE: ALL
    add_rulebinding_list:
    - USERPROFILENAME: 'up_test'
      RULENAME: 'rule_test'
      POLICYTYPE: QOS
    add_usrprofgroup_list:
    - USERPROFGNAME: 'upg_test'
    add_upbindupg_list:
    - USERPROFGNAME: 'upg_test'
      UPBINDTYPE: DEFAULT
      USERPROFILENAME: 'up_test'
      CCCONFIGMODE: ''
      IMEISVSEGNAME: ''
      IMSIMSSEGNAME: ''
      LOCALPCCSELECT: INHERIT
      LOCGROUPNAME: ''
      PRIORITY: ''
      RAT: ''
      ROAMING: ''
      SEGGROUPNAME: ''
    add_apnusrprofg_list:
    - APN: 'huawei.com'
      USERPROFGNAME: 'upg_test'
    set_apnidletime_list:
    - APN: 'huawei.com'
      INHERIT: NO
      HSMFTIMERLEVEL: QOSFLOW
      DEDQFIDLETIMER: 600
      DFTQFIDLETIMER: ''
      BEARERTIMER: ''
      DFTBEARPOLICY: ''
      DFTBRPLCYGGSN: ''
      GCTXCHKSW: ''
      GULTIMERLEVEL: ''
      HCTXCHKSW: ''
      HCTXINACHKSW: ''
      ICTXCHKSW: ''
      ICTXINACHKSW: ''
      IDLEUPDATEMSG: ''
      PCTXCHKSW: ''
      PROS8CTXCHKSW: ''
      PROXYSMFCHKSW: ''
      SCTXCHKSW: ''
      SESSIONTIMER: ''
      SMFSESIDLETIMER: ''
      SMFSESINATIMER: ''
    add_apndeactqfplcy_list:
    - APN: 'huawei.com'
      NGAPCAUSEGROUP: RADIO_NETWORK
      NGAPCAUSEVALUE: 21
      QFPLCY: DELAY_RELEASE
      DELAYTIMER: 60
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 打开本特性的License配置开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

### 2 配置QoS URR。

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

### 3 配置QoS属性。

```jinja2
{%- for item in add_qosprop_list -%}
    ADD QOSPROP:
    {#- --- 必选参数 --- -#}
    QOSPROPNAME="{{item.QOSPROPNAME}}",
    QOSTYPE={{item.QOSTYPE}},
    {#- --- 可选参数 --- -#}
    {%- if item.GBRUPLKVALUE is not none -%}
        GBRUPLKVALUE={{item.GBRUPLKVALUE}},
    {%- endif -%}
    {%- if item.GBRDNLKVALUE is not none -%}
        GBRDNLKVALUE={{item.GBRDNLKVALUE}},
    {%- endif -%}
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
```

### 4 规则通过PCC策略组绑定QoS属性时，配置PCC策略组。规则直接绑定QoS属性时，请跳过本步骤。

```jinja2
{%- if is_scenario_pcc_policy_binding -%}
    {%- for item in add_pccpolicygrp_list -%}
        ADD PCCPOLICYGRP:
        {#- --- 必选参数 --- -#}
        PCCPOLICYGRPNM="{{item.PCCPOLICYGRPNM}}",
        {#- --- 可选参数 --- -#}
        {%- if item.QOSPROPNAME is not none -%}
            QOSPROPNAME="{{item.QOSPROPNAME}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 5 配置SMF上的本地rule。

```jinja2
{%- if is_scenario_pcc_policy_binding -%}
    {%- for item in add_rule_list -%}
        ADD RULE:
        {#- --- 必选参数 --- -#}
        RULENAME="{{item.RULENAME}}",
        POLICYTYPE={{item.POLICYTYPE}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：POLICYTYPE=PCC/ULCL/QOS 时必选 --- -#}
        {%- if item.POLICYTYPE in ['PCC', 'ULCL', 'QOS'] -%}
            POLICYNAME="{{item.POLICYNAME}}",
        {%- endif -%}
        {#- --- 条件必选：POLICYTYPE=ULCL 时必选 --- -#}
        {%- if item.POLICYTYPE == 'ULCL' -%}
            FLOWFILTERNAME="{{item.FLOWFILTERNAME}}",
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：POLICYTYPE=PCC/QOS 时可选 --- -#}
        {%- if item.POLICYTYPE in ['PCC', 'QOS'] -%}
            {%- if item.PROTODESCDL is not none -%}
                PROTODESCDL="{{item.PROTODESCDL}}",
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：POLICYTYPE=PCC/QOS 时可选 --- -#}
        {%- if item.POLICYTYPE in ['PCC', 'QOS'] -%}
            {%- if item.PROTODESCUL is not none -%}
                PROTODESCUL="{{item.PROTODESCUL}}",
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：POLICYTYPE=PCC/QOS 时可选 --- -#}
        {%- if item.POLICYTYPE in ['PCC', 'QOS'] -%}
            {%- if item.RULERANGE is not none -%}
                RULERANGE={{item.RULERANGE}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_qos_binding -%}
    {%- for item in add_rule_list_1 -%}
        ADD RULE:
        {#- --- 必选参数 --- -#}
        RULENAME="{{item.RULENAME}}",
        POLICYTYPE={{item.POLICYTYPE}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：POLICYTYPE=PCC/ULCL/QOS 时必选 --- -#}
        {%- if item.POLICYTYPE in ['PCC', 'ULCL', 'QOS'] -%}
            POLICYNAME="{{item.POLICYNAME}}",
        {%- endif -%}
        {#- --- 条件必选：POLICYTYPE=ULCL 时必选 --- -#}
        {%- if item.POLICYTYPE == 'ULCL' -%}
            FLOWFILTERNAME="{{item.FLOWFILTERNAME}}",
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：POLICYTYPE=PCC/QOS 时可选 --- -#}
        {%- if item.POLICYTYPE in ['PCC', 'QOS'] -%}
            {%- if item.PROTODESCDL is not none -%}
                PROTODESCDL="{{item.PROTODESCDL}}",
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：POLICYTYPE=PCC/QOS 时可选 --- -#}
        {%- if item.POLICYTYPE in ['PCC', 'QOS'] -%}
            {%- if item.PROTODESCUL is not none -%}
                PROTODESCUL="{{item.PROTODESCUL}}",
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：POLICYTYPE=PCC/QOS 时可选 --- -#}
        {%- if item.POLICYTYPE in ['PCC', 'QOS'] -%}
            {%- if item.RULERANGE is not none -%}
                RULERANGE={{item.RULERANGE}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 规则通过PCC策略组绑定QoS属性时，“POLICYTYPE”设置为“PCC”，“POLICYNAME”使用**ADD PCCPOLICYGRP**命令配置的“PCCPOLICYGRPNM”参数值。

### 规则直接绑定QoS属性时，“POLICYTYPE”设置为“QOS”“POLICYNAME”使用**ADD QOSPROP**命令配置的“QOSPROPNAME”参数值。

### PCC类型的“RULENAME”值与QOS类型的“RULENAME”值不能相同。

### 6 配置SMF上的UserProfile，将本地rule绑定到UserProfile上。用于动态PCC时PCF下发预定义规则组，或本地PCC时的静态规则组。

#### 6.1 配置UserProfile。

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

#### 6.2 将rule绑定到UserProfile。

```jinja2
{%- for item in add_rulebinding_list -%}
    ADD RULEBINDING:
    {#- --- 必选参数 --- -#}
    USERPROFILENAME="{{item.USERPROFILENAME}}",
    RULENAME="{{item.RULENAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.POLICYTYPE is not none -%}
        POLICYTYPE={{item.POLICYTYPE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 7 **可选：**（无可用PCRF/PCF时使用）配置UserProfile组，将UserProfile绑定到UserProfile组，再将UserProfile组绑定到DNN实例上。用于本地PCC的静态规则。如UserProfile已配置，请跳过本步骤。

#### 7.1 配置UserProfile Group。

```jinja2
{%- if is_optional_userprofile_group -%}
    {%- for item in add_usrprofgroup_list -%}
        ADD USRPROFGROUP:
        {#- --- 必选参数 --- -#}
        USERPROFGNAME="{{item.USERPROFGNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 7.2 将UserProfile绑定到UserProfile Group。

```jinja2
{%- if is_optional_userprofile_group -%}
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

#### 7.3 将UserProfile Group绑定到DNN。

```jinja2
{%- if is_optional_userprofile_group -%}
    {%- for item in add_apnusrprofg_list -%}
        ADD APNUSRPROFG:
        {#- --- 必选参数 --- -#}
        APN="{{item.APN}}",
        USERPROFGNAME="{{item.USERPROFGNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

### 8 **可选：**系统初始值不符合要求时，修改指定APN级别的专有QoS Flow级别的空闲定时器时长。

```jinja2
{%- if is_optional_apn_idle_timer -%}
    {%- for item in set_apnidletime_list -%}
        SET APNIDLETIME:
        {#- --- 必选参数 --- -#}
        APN="{{item.APN}}",
        {#- --- 可选参数 --- -#}
        {%- if item.INHERIT is not none -%}
            INHERIT={{item.INHERIT}},
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：INHERIT=NO 时可选 --- -#}
        {%- if item.INHERIT == 'NO' -%}
            {%- if item.HSMFTIMERLEVEL is not none -%}
                HSMFTIMERLEVEL={{item.HSMFTIMERLEVEL}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：HSMFTIMERLEVEL=QOSFLOW 时可选 --- -#}
        {%- if item.HSMFTIMERLEVEL == 'QOSFLOW' -%}
            {%- if item.DEDQFIDLETIMER is not none -%}
                DEDQFIDLETIMER={{item.DEDQFIDLETIMER}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：INHERIT=NO 时可选 --- -#}
        {%- if item.INHERIT == 'NO' -%}
            {%- if item.BEARERTIMER is not none -%}
                BEARERTIMER={{item.BEARERTIMER}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：INHERIT=NO 时可选 --- -#}
        {%- if item.INHERIT == 'NO' -%}
            {%- if item.DFTBEARPOLICY is not none -%}
                DFTBEARPOLICY={{item.DFTBEARPOLICY}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：INHERIT=NO 时可选 --- -#}
        {%- if item.INHERIT == 'NO' -%}
            {%- if item.DFTBRPLCYGGSN is not none -%}
                DFTBRPLCYGGSN={{item.DFTBRPLCYGGSN}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：HSMFTIMERLEVEL=QOSFLOW 时可选 --- -#}
        {%- if item.HSMFTIMERLEVEL == 'QOSFLOW' -%}
            {%- if item.DFTQFIDLETIMER is not none -%}
                DFTQFIDLETIMER={{item.DFTQFIDLETIMER}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：INHERIT=NO 时可选 --- -#}
        {%- if item.INHERIT == 'NO' -%}
            {%- if item.GCTXCHKSW is not none -%}
                GCTXCHKSW={{item.GCTXCHKSW}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：INHERIT=NO 时可选 --- -#}
        {%- if item.INHERIT == 'NO' -%}
            {%- if item.GULTIMERLEVEL is not none -%}
                GULTIMERLEVEL={{item.GULTIMERLEVEL}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：INHERIT=NO 时可选 --- -#}
        {%- if item.INHERIT == 'NO' -%}
            {%- if item.HCTXCHKSW is not none -%}
                HCTXCHKSW={{item.HCTXCHKSW}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：INHERIT=NO 时可选 --- -#}
        {%- if item.INHERIT == 'NO' -%}
            {%- if item.HCTXINACHKSW is not none -%}
                HCTXINACHKSW={{item.HCTXINACHKSW}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：INHERIT=NO 时可选 --- -#}
        {%- if item.INHERIT == 'NO' -%}
            {%- if item.ICTXCHKSW is not none -%}
                ICTXCHKSW={{item.ICTXCHKSW}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：INHERIT=NO 时可选 --- -#}
        {%- if item.INHERIT == 'NO' -%}
            {%- if item.ICTXINACHKSW is not none -%}
                ICTXINACHKSW={{item.ICTXINACHKSW}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：INHERIT=NO 时可选 --- -#}
        {%- if item.INHERIT == 'NO' -%}
            {%- if item.IDLEUPDATEMSG is not none -%}
                IDLEUPDATEMSG={{item.IDLEUPDATEMSG}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：INHERIT=NO 时可选 --- -#}
        {%- if item.INHERIT == 'NO' -%}
            {%- if item.PCTXCHKSW is not none -%}
                PCTXCHKSW={{item.PCTXCHKSW}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：INHERIT=NO 时可选 --- -#}
        {%- if item.INHERIT == 'NO' -%}
            {%- if item.PROS8CTXCHKSW is not none -%}
                PROS8CTXCHKSW={{item.PROS8CTXCHKSW}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：INHERIT=NO 时可选 --- -#}
        {%- if item.INHERIT == 'NO' -%}
            {%- if item.PROXYSMFCHKSW is not none -%}
                PROXYSMFCHKSW={{item.PROXYSMFCHKSW}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：INHERIT=NO 时可选 --- -#}
        {%- if item.INHERIT == 'NO' -%}
            {%- if item.SCTXCHKSW is not none -%}
                SCTXCHKSW={{item.SCTXCHKSW}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：INHERIT=NO 时可选 --- -#}
        {%- if item.INHERIT == 'NO' -%}
            {%- if item.SESSIONTIMER is not none -%}
                SESSIONTIMER={{item.SESSIONTIMER}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：INHERIT=NO 时可选 --- -#}
        {%- if item.INHERIT == 'NO' -%}
            {%- if item.SMFSESIDLETIMER is not none -%}
                SMFSESIDLETIMER={{item.SMFSESIDLETIMER}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：INHERIT=NO 时可选 --- -#}
        {%- if item.INHERIT == 'NO' -%}
            {%- if item.SMFSESINATIMER is not none -%}
                SMFSESINATIMER={{item.SMFSESINATIMER}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### APN粒度优先级>全局粒度。全局粒度的可使用**SET DFTIDLETIME**设置。

### 修改参数“专有QoS Flow空闲定时器时长（DEDQFIDLETIMER）”后，对新激活的用户生效，且仅对专有QoS Flow生效。

### 9 **可选：**UE无线连接丢失（NGAPCAUSEVALUE=21）时，配置基于APN去活用户面专有QoS Flow策略。

```jinja2
{%- if is_optional_apn_deactivate_qosflow_policy -%}
    {%- for item in add_apndeactqfplcy_list -%}
        ADD APNDEACTQFPLCY:
        {#- --- 必选参数 --- -#}
        APN="{{item.APN}}",
        NGAPCAUSEGROUP={{item.NGAPCAUSEGROUP}},
        NGAPCAUSEVALUE={{item.NGAPCAUSEVALUE}},
        QFPLCY={{item.QFPLCY}},
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：QFPLCY=DELAY_RELEASE 时可选 --- -#}
        {%- if item.QFPLCY == 'DELAY_RELEASE' -%}
            {%- if item.DELAYTIMER is not none -%}
                DELAYTIMER={{item.DELAYTIMER}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### APN粒度优先级>全局粒度。全局粒度的可使用**ADD DEACTQFPLCY**设置。


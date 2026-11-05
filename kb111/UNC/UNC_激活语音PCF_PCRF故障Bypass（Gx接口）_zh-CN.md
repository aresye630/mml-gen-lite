---
id: ''
name: 激活语音PCF/PCRF故障Bypass（Gx接口）
ne_type: UNC
type: feature
description: 本操作指导在运行网络中激活语音PCF/PCRF故障Bypass特性的过程。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","语音功能","WSFD-201207 语音PCF/PCRF故障Bypass","激活语音PCF/PCRF故障Bypass（Gx接口）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本操作指导在运行网络中激活语音PCF/PCRF故障Bypass特性的过程。

## 必备事项
前提条件

前提条件

* 请仔细阅读WSFD-201207 语音PCF/PCRF故障Bypass特性概述和实现原理（Gx接口）。
* 依赖的特性已完成配置，相关特性参见与其他特性的交互。
* PGW-C和PCRF直连场景，对于支持Failover的PCRF已参考Gx Failover功能配置PCRF支持Failover功能。
* 已完成License加载，对应License项见License支持。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    add_urr_list:
      type: items
      properties:
        URRNAME:
          name: '使用量上报规则名称'
          type: string
          maxLength: 31
          required: true
          description: '增加使用量上报规则信息。存在多条记录时，使用量上报规则名称不能重复。  “URRID”在所有URR内唯一。  此处取值为举例，请根据业务规划进行配置。'
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
          data_source: '本端规划'
          pattern: ''
          default: ''
        RG:
          name: '离线计费组'
          type: integer
          minimum: 0
          maximum: 4294967294
          required: false
          description: ''
          data_source: '本端规划'
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
          data_source: '本端规划'
          pattern: ''
          default: ''
        DOWNSID:
          name: '离线下行业务标识'
          type: integer
          minimum: 0
          maximum: 4294967294
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SID:
          name: '离线业务标识'
          type: integer
          minimum: 0
          maximum: 4294967294
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        UPSID:
          name: '离线上行业务标识'
          type: integer
          minimum: 0
          maximum: 4294967294
          required: false
          description: ''
          data_source: ''
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
          description: '增加使用量上报规则组。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        UPURRNAME1:
          name: '上行发起URR名称1'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        DOWNURRNAME1:
          name: '下行发起URR名称1'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        UPURRNAME2:
          name: '上行发起URR名称2'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        DOWNURRNAME2:
          name: '下行发起URR名称2'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: '本端规划'
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
          description: '配置PCC策略组。存在多条记录时，PCC策略组名称不能重复。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        URRGROUPNAME:
          name: '使用量上报规则组名称'
          type: string
          maxLength: 31
          required: false
          description: '使用**ADD URRGROUP**定义的使用量上报规则组。'
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
          description: '配置业务策略规则。存在多条数据时，规则名称+策略类型不能完全相同。'
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
          description: '* “POLICYTYPE”设置为“PCC”时，“POLICYNAME”使用**ADD PCCPOLICYGRP**定义的PCCPOLICYGRPNM。 * “POLICYTYPE”设置为“QOS”时，“POLICYNAME”使用**ADD QOSPROP**定义的QOSPROPNAME。 * 配置“PRIORITY”时需要注意：PCRF下发的用于创建语音专有承载的规则的优先级高于本地配置的用于创建语音专有承载的规则；本地配置的用于创建语音/专有承载的规则优先级高于PCRF下发的any to any的动态规则和本地配置的any to any的预定义规则。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PRIORITY:
          name: '全局优先级'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: false
          description: ''
          data_source: '与对端协商'
          pattern: ''
          default: 4294967295
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
          description: '（可选）配置用户模板。'
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
    add_rulebinding_list:
      type: items
      properties:
        USERPROFILENAME:
          name: '用户模板名称'
          type: string
          maxLength: 63
          required: true
          description: '增加用户模板与规则的绑定关系，将本地rule/预定义规则rule绑定到UserProfile上。'
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
          description: '（可选）配置用户模板组。'
          data_source: '全网规划'
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
          description: '（可选）将用户模板绑定到用户模板组中。'
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
          data_source: '全网规划'
          pattern: ''
          default: ''
        PRIORITY:
          name: '优先级'
          type: integer
          minimum: 1
          maximum: 65534
          required: false
          description: ''
          data_source: '本端规划'
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
          description: '（可选）为APN绑定用户模板组。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        USERPROFGNAME:
          name: '用户模板组名称'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_urr_list_2:
      type: items
      properties:
        URRNAME:
          name: '使用量上报规则名称'
          type: string
          maxLength: 31
          required: true
          description: '增加使用量上报规则信息。存在多条记录时，使用量上报规则名称不能重复。  “URRID”在所有URR内唯一。  此处取值为举例，请根据业务规划进行配置。'
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
          data_source: '本端规划'
          pattern: ''
          default: ''
        RG:
          name: '离线计费组'
          type: integer
          minimum: 0
          maximum: 4294967294
          required: false
          description: ''
          data_source: '本端规划'
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
          data_source: '本端规划'
          pattern: ''
          default: ''
        DOWNSID:
          name: '离线下行业务标识'
          type: integer
          minimum: 0
          maximum: 4294967294
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SID:
          name: '离线业务标识'
          type: integer
          minimum: 0
          maximum: 4294967294
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        UPSID:
          name: '离线上行业务标识'
          type: integer
          minimum: 0
          maximum: 4294967294
          required: false
          description: ''
          data_source: ''
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
        REDIRENDTOKEN:
          name: 'Gy重定向结束Token'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_urrgroup_list_1:
      type: items
      properties:
        URRGROUPNAME:
          name: '使用量上报规则组名称'
          type: string
          maxLength: 31
          required: true
          description: '增加使用量上报规则组。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        UPURRNAME1:
          name: '上行发起URR名称1'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        DOWNURRNAME1:
          name: '下行发起URR名称1'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        UPURRNAME2:
          name: '上行发起URR名称2'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        DOWNURRNAME2:
          name: '下行发起URR名称2'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: '本端规划'
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
          description: '配置静态PCC策略的QoS参数。存在多条记录时，QoS属性名称不能重复。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        EMPCAP:
          name: 'QoS抢占能力'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '该业务可以抢占已经分配给其他低优先级业务流的资源时，设置为ENABLE。此处以抢占为例。'
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
          description: '其他高优先级业务不能抢占本业务流的资源时，设置为DISABLE。此处以不被抢占为例。'
          data_source: '本端规划'
          pattern: ''
          default: ENABLE
        GBRUPLKVALUE:
          name: '保证的上行比特率'
          type: integer
          minimum: 0
          maximum: 20000000
          required: false
          description: 'PCRF正常时，MBR\GBR是由UE携带给SBC网元，然后由SBC网元根据UE请求的带宽以及和UE协商的音频编解码方式的带宽要求等下发，并且GBR和MBR的UL/DL带宽按照相同值下发。  PCRF Bypass期间，创建专有承载时，使用PGW-C上配置的MBR\GBR。参考IMS音频编解码带宽要求，建议按照64Kbit/s，不影响语音业务体验。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        GBRDNLKVALUE:
          name: '保证的下行比特率'
          type: integer
          minimum: 0
          maximum: 20000000
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
        MBRUPLKVALUE:
          name: '最大上行比特率'
          type: integer
          minimum: 0
          maximum: 20000000
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
        MBRDNLKVALUE:
          name: '最大下行比特率'
          type: integer
          minimum: 0
          maximum: 20000000
          required: false
          description: ''
          data_source: '固定取值'
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
        QCIVALUE:
          name: 'QoS等级标识'
          type: integer
          minimum: 1
          maximum: 255
          required: false
          description: '“QOSTYPE”为“QOS\_BEARER\_PARA”时需要规划。'
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
    add_pccpolicygrp_list_1:
      type: items
      properties:
        PCCPOLICYGRPNM:
          name: 'PCC策略组名称'
          type: string
          maxLength: 63
          required: true
          description: '配置PCC策略组。存在多条记录时，PCC策略组名称不能重复。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        URRGROUPNAME:
          name: '使用量上报规则组名称'
          type: string
          maxLength: 31
          required: false
          description: '使用**ADD URRGROUP**定义的使用量上报规则组。'
          data_source: '已配置数据中获取'
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
    add_rule_list_1:
      type: items
      properties:
        RULENAME:
          name: '规则名称'
          type: string
          maxLength: 63
          required: true
          description: '配置业务策略规则。存在多条数据时，规则名称+策略类型不能完全相同。'
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
          description: '* “POLICYTYPE”设置为“PCC”时，“POLICYNAME”使用**ADD PCCPOLICYGRP**定义的PCCPOLICYGRPNM。 * “POLICYTYPE”设置为“QOS”时，“POLICYNAME”使用**ADD QOSPROP**定义的QOSPROPNAME。 * 配置“PRIORITY”时需要注意：PCF下发的用于创建语音专有QoS Flow/专有承载的规则的优先级高于本地配置的用于创建语音专有QoS Flow/专有承载的规则；本地配置的用于创建语音专有QoS Flow/专有承载的规则优先级高于PCF下发的any to any的动态规则和本地配置的any to any的预定义规则。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PRIORITY:
          name: '全局优先级'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: false
          description: ''
          data_source: '与对端协商'
          pattern: ''
          default: 4294967295
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
    add_userprofile_list_1:
      type: items
      properties:
        USERPROFILENAME:
          name: '用户模板名称'
          type: string
          maxLength: 63
          required: true
          description: '（可选）配置用户模板。'
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
    add_rulebinding_list_1:
      type: items
      properties:
        USERPROFILENAME:
          name: '用户模板名称'
          type: string
          maxLength: 63
          required: true
          description: '增加用户模板与规则的绑定关系，将本地rule/预定义规则rule绑定到UserProfile上。'
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
    add_usrprofgroup_list_1:
      type: items
      properties:
        USERPROFGNAME:
          name: '用户模板组名称'
          type: string
          maxLength: 63
          required: true
          description: '（可选）配置用户模板组。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_upbindupg_list_1:
      type: items
      properties:
        USERPROFGNAME:
          name: '用户模板组名称'
          type: string
          maxLength: 63
          required: true
          description: '（可选）将用户模板绑定到用户模板组中。'
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
          data_source: '全网规划'
          pattern: ''
          default: ''
        PRIORITY:
          name: '优先级'
          type: integer
          minimum: 1
          maximum: 65534
          required: false
          description: ''
          data_source: '本端规划'
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
    add_apnusrprofg_list_1:
      type: items
      properties:
        APN:
          name: 'APN'
          type: string
          maxLength: 63
          required: true
          description: '（可选）为APN绑定用户模板组。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        USERPROFGNAME:
          name: '用户模板组名称'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    set_pccfailaction_list:
      type: items
      properties:
        SELPEERFAILACT:
          name: '选择PCRF/PCF失败动作'
          type: string
          enum:
          - DEFAULT
          - FORBIDDEN
          - ROLLBACK
          required: false
          description: '配置PCRF故障处理动作。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        INITIALFAILACT:
          name: 'Initial流程故障处理动作'
          type: string
          enum:
          - FORBIDDEN
          - ROLLBACK
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        UPDATEFAILACT:
          name: 'Update流程故障处理动作'
          type: string
          enum:
          - CONTINUE
          - ROLLBACK
          - TERMINATE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        UPDFAILLOCPCC:
          name: 'Update流程故障回滚为Local PCC用户类型'
          type: string
          enum:
          - INHERIT_PCC
          - LOCAL_PCC
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        INITFAILLOCPCC:
          name: 'Initial流程故障回滚为Local PCC用户类型'
          type: string
          enum:
          - LOCAL_PCC
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        INITFAILRDSPCC:
          name: 'Initial流程故障回滚为RADIUS PCC用户类型'
          type: string
          enum:
          - LOCAL_PCC
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SELPEERLOCPCC:
          name: '选择PCRF/PCF失败回滚为Local PCC用户类型'
          type: string
          enum:
          - LOCAL_PCC
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SELPEERRDSPCC:
          name: '选择PCRF/PCF失败回滚为RADIUS PCC用户类型'
          type: string
          enum:
          - LOCAL_PCC
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_pcctimer_list:
      type: items
      properties:
        HOLDINGTIME:
          name: '用户回滚后在线保持时长（分钟）'
          type: integer
          minimum: 0
          maximum: 1440
          required: false
          description: '配置全局Holding Time和Fast Holding Time。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        ADJUSTRANGE:
          name: '随机延迟范围（分钟）'
          type: integer
          minimum: 0
          maximum: 60
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        FASTHOLDINGTIME:
          name: '用户快速回滚后在线保持时长（分钟）'
          type: integer
          minimum: 0
          maximum: 1440
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        FASTADJUSTRANGE:
          name: '快速随机延迟范围（分钟）'
          type: integer
          minimum: 0
          maximum: 60
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_pcctemplate_list:
      type: items
      properties:
        PCCTEMPNAME:
          name: 'PCC模板名称'
          type: string
          maxLength: 63
          required: true
          description: '配置PCC模板中PCRF故障处理动作、Failover开关和Holding Time。  说明：  建议IMS语音业务单独使用一个PCC模板。新建模板使用**ADD PCCTEMPLATE**命令；修改已有模板使用**MOD PCCTEMPLATE**命令。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SELPEERFAILACT:
          name: '选择PCRF/PCF失败动作'
          type: string
          enum:
          - DEFAULT
          - FORBIDDEN
          - INHERIT
          - ROLLBACK
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: INHERIT
        INITIALFAILACT:
          name: 'Initial流程故障处理动作'
          type: string
          enum:
          - FORBIDDEN
          - INHERIT
          - ROLLBACK
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: INHERIT
        UPDATEFAILACT:
          name: 'Update流程故障处理动作'
          type: string
          enum:
          - CONTINUE
          - INHERIT
          - ROLLBACK
          - TERMINATE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: INHERIT
        UPDFAILLOCPCC:
          name: 'Update流程故障回滚为Local PCC用户类型'
          type: string
          enum:
          - INHERIT_PCC
          - LOCAL_PCC
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: LOCAL_PCC
        HOLDINGTIME:
          name: '用户回滚后在线保持时长（分钟）'
          type: integer
          minimum:
          - 0
          - 65535
          maximum:
          - 1440
          - 65535
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: 65535
        ADJUSTRANGE:
          name: '随机延迟范围（分钟）'
          type: integer
          minimum: 0
          maximum: 60
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        INITFAILLOCPCC:
          name: 'Initial流程故障回滚为Local PCC用户类型'
          type: string
          enum:
          - LOCAL_PCC
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: LOCAL_PCC
        INITFAILRDSPCC:
          name: 'Initial流程故障回滚为RADIUS PCC用户类型'
          type: string
          enum:
          - LOCAL_PCC
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: LOCAL_PCC
        SELPEERLOCPCC:
          name: '选择PCF/PCRF失败回滚为Local PCC用户类型'
          type: string
          enum:
          - LOCAL_PCC
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: LOCAL_PCC
        SELPEERRDSPCC:
          name: '选择PCF/PCRF失败回滚为RADIUS PCC用户类型'
          type: string
          enum:
          - LOCAL_PCC
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: LOCAL_PCC
    mod_pcctemplate_list:
      type: items
      properties:
        PCCTEMPNAME:
          name: 'PCC模板名称'
          type: string
          maxLength: 63
          required: true
          description: '配置PCC模板中PCRF故障处理动作、Failover开关和Holding Time。  说明：  建议IMS语音业务单独使用一个PCC模板。新建模板使用**ADD PCCTEMPLATE**命令；修改已有模板使用**MOD PCCTEMPLATE**命令。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SELPEERFAILACT:
          name: '选择PCRF/PCF失败动作'
          type: string
          enum:
          - DEFAULT
          - FORBIDDEN
          - INHERIT
          - ROLLBACK
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        INITIALFAILACT:
          name: 'Initial流程故障处理动作'
          type: string
          enum:
          - FORBIDDEN
          - INHERIT
          - ROLLBACK
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        UPDATEFAILACT:
          name: 'Update流程故障处理动作'
          type: string
          enum:
          - CONTINUE
          - INHERIT
          - ROLLBACK
          - TERMINATE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        UPDFAILLOCPCC:
          name: 'Update流程故障回滚为Local PCC用户类型'
          type: string
          enum:
          - INHERIT_PCC
          - LOCAL_PCC
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        HOLDINGTIME:
          name: '用户回滚后在线保持时长（分钟）'
          type: integer
          minimum:
          - 0
          - 65535
          maximum:
          - 1440
          - 65535
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        ADJUSTRANGE:
          name: '随机延迟范围（分钟）'
          type: integer
          minimum: 0
          maximum: 60
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        INITFAILLOCPCC:
          name: 'Initial流程故障回滚为Local PCC用户类型'
          type: string
          enum:
          - LOCAL_PCC
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        INITFAILRDSPCC:
          name: 'Initial流程故障回滚为RADIUS PCC用户类型'
          type: string
          enum:
          - LOCAL_PCC
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SELPEERLOCPCC:
          name: '选择PCF/PCRF失败回滚为Local PCC用户类型'
          type: string
          enum:
          - LOCAL_PCC
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SELPEERRDSPCC:
          name: '选择PCF/PCRF失败回滚为RADIUS PCC用户类型'
          type: string
          enum:
          - LOCAL_PCC
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_resultcodectrl_list:
      type: items
      properties:
        PCCTEMPLATE:
          name: 'PCC模板名称'
          type: string
          maxLength: 63
          required: true
          description: '配置对端回复指定结果码后PGW-C的处理操作。  “INTFTYPE”需要根据现网语音业务使用的策略接口进行配置。  “GXRESULTCODEVAL”需要与对端PCRF/DRA确认，此处取值仅为举例。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        INTFTYPE:
          name: '接口类型'
          type: string
          enum:
          - INTFTYPE_GX
          - INTFTYPE_N7
          required: true
          description: ''
          data_source: '与对端协商'
          pattern: ''
          default: ''
        VENDORID:
          name: '设备提供商标识'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        GXRESULTCODEVAL:
          name: 'Gx返回码'
          type: string
          maxLength: 4
          required: false
          description: ''
          data_source: '与对端协商'
          pattern: ''
          default: ''
        DIRECTINITACT:
          name: '直连对端Initial流程处理动作'
          type: string
          enum:
          - DEFAULT
          - FAILOVER
          - FAILOVERALL
          - INVALID
          - LOCALPCC
          - TERMINATE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: INVALID
        DIRECTUPDACT:
          name: '直连对端Update流程处理动作'
          type: string
          enum:
          - CONTINUE
          - FAILOVER
          - FAILOVERALL
          - INHERIT_PCC
          - INVALID
          - LOCALPCC
          - TERMINATE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: INVALID
        DIRECTINITHTSW:
          name: '直连对端Initial流程回滚后使能Holding-Time'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
        DIRECTREACTREQ:
          name: '直连对端重激活请求'
          type: string
          enum:
          - DEFAULT
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DEFAULT
        DIRECTUPDHTSW:
          name: '直连对端Update流程回滚后使能Holding-Time'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
        N7RESULTCODEVAL:
          name: 'N7返回码'
          type: string
          maxLength: 3
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    mod_resultcodectrl_list:
      type: items
      properties:
        PCCTEMPLATE:
          name: 'PCC模板名称'
          type: string
          maxLength: 63
          required: true
          description: '配置对端回复指定结果码后PGW-C的处理操作。  “INTFTYPE”需要根据现网语音业务使用的策略接口进行配置。  “GXRESULTCODEVAL”需要与对端PCRF/DRA确认，此处取值仅为举例。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        INTFTYPE:
          name: '接口类型'
          type: string
          enum:
          - INTFTYPE_GX
          - INTFTYPE_N7
          required: true
          description: ''
          data_source: '与对端协商'
          pattern: ''
          default: ''
        VENDORID:
          name: '设备提供商标识'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        GXRESULTCODEVAL:
          name: 'Gx返回码'
          type: string
          maxLength: 4
          required: false
          description: ''
          data_source: '与对端协商'
          pattern: ''
          default: ''
        DIRECTINITACT:
          name: '直连对端Initial流程处理动作'
          type: string
          enum:
          - DEFAULT
          - FAILOVER
          - FAILOVERALL
          - INVALID
          - LOCALPCC
          - TERMINATE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        DIRECTUPDACT:
          name: '直连对端Update流程处理动作'
          type: string
          enum:
          - CONTINUE
          - FAILOVER
          - FAILOVERALL
          - INHERIT_PCC
          - INVALID
          - LOCALPCC
          - TERMINATE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        DIRECTINITHTSW:
          name: '直连对端Initial流程回滚后使能Holding-Time'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DIRECTREACTREQ:
          name: '直连对端重激活请求'
          type: string
          enum:
          - DEFAULT
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DIRECTUPDHTSW:
          name: '直连对端Update流程回滚后使能Holding-Time'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        N7RESULTCODEVAL:
          name: 'N7返回码'
          type: string
          maxLength: 3
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_resultcodedra_list:
      type: items
      properties:
        PCCTEMPLATE:
          name: 'PCC模板名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '配置PGW-C与PCRF非直连场景，DRA返回异常返回码的处理动作。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        VENDORID:
          name: '设备提供商标识'
          type: integer
          minimum: 0
          maximum: 65535
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        RESULTCODEVAL:
          name: '返回码'
          type: string
          minLength: 1
          maxLength: 4
          required: true
          description: ''
          data_source: '与对端协商'
          pattern: ''
          default: ''
        INITACTION:
          name: 'Initial流程处理动作'
          type: string
          enum:
          - DEFAULT
          - FAILOVER
          - TERMINATE
          - LOCALPCC
          - INHERIT
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        UPDATEACTION:
          name: 'Update流程处理动作'
          type: string
          enum:
          - FAILOVER
          - TERMINATE
          - LOCALPCC
          - INHERIT_PCC
          - CONTINUE
          - INHERIT
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        INITHOLDTMSW:
          name: 'Initial流程回滚后使能Holding-Time'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: DISABLE
        UPDHOLDTMSW:
          name: 'Update流程回滚后使能Holding-Time'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: DISABLE
        REACTREQ:
          name: '重新激活请求'
          type: string
          enum:
          - DISABLE
          - ENABLE
          - DEFAULT
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DEFAULT
    add_pccbypasscode_list:
      type: items
      properties:
        PCCTEMPLATE:
          name: 'PCC模板名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '配置在非直连组网场景，会话退出PCRF Bypass状态时PGW-C发送探测消息后，收到对端网元返回特定状态码会话继续保持Bypass状态。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        INTFTYPE:
          name: '接口类型'
          type: string
          enum:
          - INTFTYPE_N7
          - INTFTYPE_GX
          required: true
          description: ''
          data_source: '与对端协商'
          pattern: ''
          default: ''
        GXRESULTCODEVAL:
          name: 'Gx返回码'
          type: string
          minLength: 1
          maxLength: 4
          required: false
          description: ''
          data_source: '与对端协商'
          pattern: ''
          default: ''
        ERRINFO:
          name: '错误信息'
          type: string
          minLength: 0
          maxLength: 128
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        N7RESULTCODEVAL:
          name: 'N7返回码'
          type: string
          minLength: 1
          maxLength: 3
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_imsbypassfunc_list:
      type: items
      properties:
        ACTNODEDBEARER:
          name: '无语音专载时的故障非预期Bypass场景的异常处理动作'
          type: string
          enum:
          - INHERIT
          - TERMINATE
          required: false
          description: '配置更新流程Gx接口不支持Failover场景、PGW-C和PCRF直连场景Failover后收到备PCRF返回异常码场景和PGW-C和PCRF非直连场景Failover后收到DRA返回非RESULTCODEDRA配置的异常码场景，分别在有、无语音专有承载时的处理动作，以及在PGW-C和PCRF非直连场景没有语音专有承载时，会话退出PCRF Bypass状态是否发送探测消息。  说明：  此处取值仅为举例，请根据局点实际业务需要进行配置。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        ACTWITDEDBEARER:
          name: '存在语音专载时的更新流程故障非预期Bypass场景的异常处理动作'
          type: string
          enum:
          - INHERIT
          - FASTROLLBACK
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        FAILLOCPCC:
          name: '存在语音专载时更新流程故障回滚为Local PCC用户类型'
          type: string
          enum:
          - LOCAL_PCC
          - INHERIT_PCC
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        TSTUPDATEREQSW:
          name: '非直连场景下退出Bypass发送探测消息开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        REACTREQ:
          name: '重新激活请求'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    mod_diamrtrealm_list:
      type: items
      properties:
        REALMNAME:
          name: 'Diameter域名名称'
          type: string
          maxLength: 127
          required: true
          description: '配置DRA支持Failover功能。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        APPLICATION:
          name: 'Diameter应用'
          type: string
          enum:
          - GX
          - GY
          - S6B
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        FAILOVERSW:
          name: 'Failover开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_apnpccfunc_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          maxLength: 63
          required: true
          description: '（可选）针对指定的DNN绑定PCC模板。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        PCCTEMPLATE:
          name: 'PCC模板名称'
          type: string
          maxLength: 63
          required: false
          description: ''
          data_source: '本端规划'
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
          description: '设置承载空闲定时器时长，在呼叫结束，业务空闲超过该时长后可以删除承载。  说明：  根据业务模型进行设置。设置过大，会长时间占用上下文资源；设置过小，会强制删除承载，删除承载后还需要重新创建承载。  此处以5分钟为例，请以局点规划数据为准。'
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
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        PCTXCHKSW:
          name: 'PGW-C和SGW-C/PGW-C空闲上下文检查开关(PCTXCHKSW)'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: false
          description: ''
          data_source: '本端规划'
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
          data_source: '本端规划'
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
          data_source: '本端规划'
          pattern: ''
          default: ''
        BEARERTIMER:
          name: '承载定时器(min)'
          type: integer
          minimum: 5
          maximum: 12000
          required: false
          description: ''
          data_source: '本端规划'
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
        HSMFTIMERLEVEL:
          name: 'H-SMF空闲上下文核查级别'
          type: string
          enum:
          - SESSION
          - QOSFLOW
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
    mod_apn_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '配置语音业务APN的会话在N7接口发送重激活请求的Delete Bearer Request消息或者PduSession Release Command消息中携带cause信元值为“reactivation requested”。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        REACWITHDEL:
          name: '去活消息携带reactivation-request开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          - SPECIFIC_SCENE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        SCENELIST:
          name: '场景列表'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_smfsoftparaofbit_list:
      type: items
      properties:
        DT:
          name: '数据类型'
          type: string
          enum:
          - Dw
          - Byte
          required: true
          description: '配置在HoldingTime超时时，用户会话中有语音专有承载时不去活会话，重启HoldingTime定时器；没有语音专有承载时去活会话。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        DWORDNUM:
          name: 'Dword索引'
          type: integer
          minimum: 1
          maximum: 1500
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        VALUE:
          name: '软参记录值'
          type: string
          enum:
          - VALUE_0
          - VALUE_1
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        POSITION:
          name: '比特位'
          type: integer
          minimum: 1
          maximum: 32
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        BYTENUM:
          name: 'Byte索引'
          type: integer
          minimum: 1
          maximum: 1200
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        BYTEPOSITION:
          name: 'Byte软参比特位'
          type: integer
          minimum: 1
          maximum: 8
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_smfsoftparaofbit_list_2:
      type: items
      properties:
        DT:
          name: '数据类型'
          type: string
          enum:
          - Dw
          - Byte
          required: true
          description: '配置PGW-C在激活流程查询PCRF失败发生回滚时，HoldingTime功能（当HoldingTime超时时，去活用户）生效。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        DWORDNUM:
          name: 'Dword索引'
          type: integer
          minimum: 1
          maximum: 1500
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        VALUE:
          name: '软参记录值'
          type: string
          enum:
          - VALUE_0
          - VALUE_1
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        POSITION:
          name: '比特位'
          type: integer
          minimum: 1
          maximum: 32
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        BYTENUM:
          name: 'Byte索引'
          type: integer
          minimum: 1
          maximum: 1200
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        BYTEPOSITION:
          name: 'Byte软参比特位'
          type: integer
          minimum: 1
          maximum: 8
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_smfsoftparaofbit_list_4:
      type: items
      properties:
        DT:
          name: '数据类型'
          type: string
          enum:
          - Dw
          - Byte
          required: true
          description: '配置语音PCRF进入Bypass后，HoldingTime定时器启动三次后不强制去活会话。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        DWORDNUM:
          name: 'Dword索引'
          type: integer
          minimum: 1
          maximum: 1500
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        VALUE:
          name: '软参记录值'
          type: string
          enum:
          - VALUE_0
          - VALUE_1
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        POSITION:
          name: '比特位'
          type: integer
          minimum: 1
          maximum: 32
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        BYTENUM:
          name: 'Byte索引'
          type: integer
          minimum: 1
          maximum: 1200
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        BYTEPOSITION:
          name: 'Byte软参比特位'
          type: integer
          minimum: 1
          maximum: 8
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_smfsoftparaofbit_list_6:
      type: items
      properties:
        DT:
          name: '数据类型'
          type: string
          enum:
          - Dw
          - Byte
          required: true
          description: '配置PGW-C对接语音PCRF时将业务触发专载的双向流进行拆分处理。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        DWORDNUM:
          name: 'Dword索引'
          type: integer
          minimum: 1
          maximum: 1500
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        VALUE:
          name: '软参记录值'
          type: string
          enum:
          - VALUE_0
          - VALUE_1
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        POSITION:
          name: '比特位'
          type: integer
          minimum: 1
          maximum: 32
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        BYTENUM:
          name: 'Byte索引'
          type: integer
          minimum: 1
          maximum: 1200
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        BYTEPOSITION:
          name: 'Byte软参比特位'
          type: integer
          minimum: 1
          maximum: 8
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    add_urr_list:
    - URRNAME: 'urr_signaling_offline'
      URRID: 2005
      USAGERPTMODE: OFFLINE
      OFFCOMPOUNDTYPE: ONLYRG
      RG: 20
      OFFMETERINGTYPE: VOLUME
      ONLCOMPOUNDTYPE: ONLYRG
      ONLINERG: 25
      ONLMETERINGTYPE: VOLUME
      DOWNSID: ''
      SID: ''
      UPSID: ''
      ONLINESID: ''
      EVENTRSUVALUE: ''
      TIMERSUVALUE: ''
      VOLUMERSUVALUE: ''
      MONITORINGKEY: ''
      N40AGESW: ENABLE
      OFCSRVTMPLNAME: ''
      REDIRENDTOKEN: ''
    add_urrgroup_list:
    - URRGROUPNAME: 'urrg_signaling_01'
      UPURRNAME1: 'urr_signaling_offline'
      DOWNURRNAME1: 'urr_signaling_offline'
      UPURRNAME2: 'urr_signaling_online'
      DOWNURRNAME2: 'urr_signaling_online'
    add_pccpolicygrp_list:
    - PCCPOLICYGRPNM: 'pccpolicygrp_signaling'
      URRGROUPNAME: 'urrg_signaling_01'
    add_rule_list:
    - RULENAME: 'rule_ims_signaling'
      POLICYTYPE: PCC
      PRIORITY: 65535
      POLICYNAME: 'pccpolicygrp_signaling'
      FLOWFILTERNAME: ''
      PROTODESCDL: ''
      PROTODESCUL: ''
      RULERANGE: ALL
    add_userprofile_list:
    - USERPROFILENAME: 'up_ims'
      UPTYPE: PCC
      PROFILERANGE: ALL
    add_rulebinding_list:
    - USERPROFILENAME: 'up_ims'
      RULENAME: 'rule_ims_signaling'
      POLICYTYPE: PCC
    add_usrprofgroup_list:
    - USERPROFGNAME: 'upg_ims'
    add_upbindupg_list:
    - USERPROFGNAME: 'upg_ims'
      UPBINDTYPE: SPECIFIC
      PRIORITY: 15
      USERPROFILENAME: 'up_ims'
      CCCONFIGMODE: ''
      IMEISVSEGNAME: ''
      IMSIMSSEGNAME: ''
      LOCALPCCSELECT: INHERIT
      LOCGROUPNAME: ''
      RAT: ''
      ROAMING: ''
      SEGGROUPNAME: ''
    add_apnusrprofg_list:
    - APN: 'ims'
      USERPROFGNAME: 'upg_ims'
    add_urr_list_2:
    - URRNAME: 'urr_qos_01'
      URRID: 1006
      USAGERPTMODE: QOS
      OFFCOMPOUNDTYPE: ONLYRG
      RG: 10
      OFFMETERINGTYPE: VOLUME
      ONLCOMPOUNDTYPE: ONLYRG
      ONLINERG: 15
      ONLMETERINGTYPE: VOLUME
      DOWNSID: ''
      SID: ''
      UPSID: ''
      ONLINESID: ''
      EVENTRSUVALUE: ''
      TIMERSUVALUE: ''
      VOLUMERSUVALUE: ''
      MONITORINGKEY: ''
      N40AGESW: ENABLE
      OFCSRVTMPLNAME: ''
      REDIRENDTOKEN: ''
    add_urrgroup_list_1:
    - URRGROUPNAME: 'urrg_voice_01'
      UPURRNAME1: 'urr_voice_offline'
      DOWNURRNAME1: 'urr_voice_offline'
      UPURRNAME2: 'urr_voice_online'
      DOWNURRNAME2: 'urr_voice_online'
    add_qosprop_list:
    - QOSPROPNAME: 'qosprop_voice'
      EMPCAP: ENABLE
      EMPVUL: DISABLE
      GBRUPLKVALUE: 64
      GBRDNLKVALUE: 64
      MBRUPLKVALUE: 64
      MBRDNLKVALUE: 64
      QOSTYPE: QOS_BEARER_PARA
      QCIVALUE: 1
      QOSURRNAME: 'urr_qos_01'
      ARPVALUE: ''
      FQI: ''
      RQI: ''
    add_pccpolicygrp_list_1:
    - PCCPOLICYGRPNM: 'pccpolicygrp_voice'
      URRGROUPNAME: 'urrg_voice_01'
      QOSPROPNAME: 'qosprop_voice'
    add_rule_list_1:
    - RULENAME: 'rule_ims_voice'
      POLICYTYPE: PCC
      PRIORITY: 65535
      POLICYNAME: 'pccpolicygrp_voice'
      FLOWFILTERNAME: ''
      PROTODESCDL: ''
      PROTODESCUL: ''
      RULERANGE: ALL
    add_userprofile_list_1:
    - USERPROFILENAME: 'up_ims'
      UPTYPE: PCC
      PROFILERANGE: ALL
    add_rulebinding_list_1:
    - USERPROFILENAME: 'up_ims'
      RULENAME: 'rule_ims_voice'
      POLICYTYPE: PCC
    add_usrprofgroup_list_1:
    - USERPROFGNAME: 'upg_ims'
    add_upbindupg_list_1:
    - USERPROFGNAME: 'upg_ims'
      UPBINDTYPE: SPECIFIC
      PRIORITY: 15
      USERPROFILENAME: 'up_ims'
      CCCONFIGMODE: ''
      IMEISVSEGNAME: ''
      IMSIMSSEGNAME: ''
      LOCALPCCSELECT: INHERIT
      LOCGROUPNAME: ''
      RAT: ''
      ROAMING: ''
      SEGGROUPNAME: ''
    add_apnusrprofg_list_1:
    - APN: 'ims'
      USERPROFGNAME: 'upg_ims'
    set_pccfailaction_list:
    - SELPEERFAILACT: ROLLBACK
      INITIALFAILACT: ROLLBACK
      UPDATEFAILACT: ROLLBACK
      UPDFAILLOCPCC: INHERIT_PCC
      INITFAILLOCPCC: ''
      INITFAILRDSPCC: ''
      SELPEERLOCPCC: ''
      SELPEERRDSPCC: ''
    set_pcctimer_list:
    - HOLDINGTIME: 30
      ADJUSTRANGE: 10
      FASTHOLDINGTIME: 10
      FASTADJUSTRANGE: 5
    add_pcctemplate_list:
    - PCCTEMPNAME: 'pcctemplate'
      SELPEERFAILACT: ROLLBACK
      INITIALFAILACT: ROLLBACK
      UPDATEFAILACT: ROLLBACK
      UPDFAILLOCPCC: INHERIT_PCC
      HOLDINGTIME: 30
      ADJUSTRANGE: 10
      INITFAILLOCPCC: LOCAL_PCC
      INITFAILRDSPCC: LOCAL_PCC
      SELPEERLOCPCC: LOCAL_PCC
      SELPEERRDSPCC: LOCAL_PCC
    mod_pcctemplate_list:
    - PCCTEMPNAME: 'pcctemplate'
      SELPEERFAILACT: ROLLBACK
      INITIALFAILACT: ROLLBACK
      UPDATEFAILACT: ROLLBACK
      UPDFAILLOCPCC: INHERIT_PCC
      HOLDINGTIME: 30
      ADJUSTRANGE: 10
      INITFAILLOCPCC: ''
      INITFAILRDSPCC: ''
      SELPEERLOCPCC: ''
      SELPEERRDSPCC: ''
    add_resultcodectrl_list:
    - PCCTEMPLATE: 'pcctemplate'
      INTFTYPE: INTFTYPE_GX
      VENDORID: 0
      GXRESULTCODEVAL: '3004'
      DIRECTINITACT: FAILOVER
      DIRECTUPDACT: FAILOVER
      DIRECTINITHTSW: DISABLE
      DIRECTREACTREQ: DEFAULT
      DIRECTUPDHTSW: DISABLE
      N7RESULTCODEVAL: ''
    mod_resultcodectrl_list:
    - PCCTEMPLATE: 'pcctemplate'
      INTFTYPE: INTFTYPE_GX
      VENDORID: 0
      GXRESULTCODEVAL: '3004'
      DIRECTINITACT: FAILOVER
      DIRECTUPDACT: FAILOVER
      DIRECTINITHTSW: ''
      DIRECTREACTREQ: ''
      DIRECTUPDHTSW: ''
      N7RESULTCODEVAL: ''
    add_resultcodedra_list:
    - PCCTEMPLATE: 'pcctemplate'
      VENDORID: 0
      RESULTCODEVAL: '3004'
      INITACTION: FAILOVER
      UPDATEACTION: FAILOVER
      INITHOLDTMSW: ENABLE
      UPDHOLDTMSW: ENABLE
      REACTREQ: DEFAULT
    add_pccbypasscode_list:
    - PCCTEMPLATE: 'pcctemplate'
      INTFTYPE: INTFTYPE_GX
      GXRESULTCODEVAL: '3xxx'
      ERRINFO: ''
      N7RESULTCODEVAL: ''
    set_imsbypassfunc_list:
    - ACTNODEDBEARER: TERMINATE
      ACTWITDEDBEARER: FASTROLLBACK
      FAILLOCPCC: INHERIT_PCC
      TSTUPDATEREQSW: ENABLE
      REACTREQ: ENABLE
    mod_diamrtrealm_list:
    - REALMNAME: 'pcrf.huawei.com'
      APPLICATION: GX
      FAILOVERSW: ENABLE
    set_apnpccfunc_list:
    - APN: 'ims'
      PCCTEMPLATE: 'pcctemplate'
    set_apnidletime_list:
    - APN: 'ims'
      INHERIT: NO
      PCTXCHKSW: ENABLE
      GULTIMERLEVEL: BEARER
      DFTBEARPOLICY: OFF
      BEARERTIMER: 5
      DFTBRPLCYGGSN: ''
      GCTXCHKSW: ''
      HCTXCHKSW: ''
      HCTXINACHKSW: ''
      HSMFTIMERLEVEL: ''
      ICTXCHKSW: ''
      ICTXINACHKSW: ''
      IDLEUPDATEMSG: ''
      PROS8CTXCHKSW: ''
      PROXYSMFCHKSW: ''
      SCTXCHKSW: ''
      SESSIONTIMER: ''
      SMFSESIDLETIMER: ''
      SMFSESINATIMER: ''
    mod_apn_list:
    - APN: 'ims'
      REACWITHDEL: SPECIFIC_SCENE
      SCENELIST: N7_REACTIVE_REQUEST
    set_smfsoftparaofbit_list:
    - DT: Dw
      DWORDNUM: 519
      VALUE: VALUE_1
      POSITION: 5
      BYTENUM: ''
      BYTEPOSITION: ''
    set_smfsoftparaofbit_list_2:
    - DT: Dw
      DWORDNUM: 519
      VALUE: VALUE_1
      POSITION: 9
      BYTENUM: ''
      BYTEPOSITION: ''
    set_smfsoftparaofbit_list_4:
    - DT: Dw
      DWORDNUM: 544
      VALUE: VALUE_1
      POSITION: 17
      BYTENUM: ''
      BYTEPOSITION: ''
    set_smfsoftparaofbit_list_6:
    - DT: Dw
      DWORDNUM: 545
      VALUE: VALUE_1
      POSITION: 18
      BYTENUM: ''
      BYTEPOSITION: ''
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 全部展开

### 1 **可选：**

### 配置语音缺省承载静态PCC策略。

### 仅当局点未配置语音缺省承载静态PCC策略时，执行本步骤。否则，跳过本步骤。

#### 1.1 增加使用量上报规则信息。

```jinja2
{%- if is_optional_voice_default_bearer_static_pcc_policy -%}
    {%- for item in add_urr_list -%}
        ADD URR:
        {#- --- 必选参数 --- -#}
        URRNAME="{{item.URRNAME}}",
        URRID={{item.URRID}},
        USAGERPTMODE={{item.USAGERPTMODE}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：USAGERPTMODE=OFFLINE 时必选 --- -#}
        {%- if item.USAGERPTMODE == 'OFFLINE' -%}
            OFFCOMPOUNDTYPE={{item.OFFCOMPOUNDTYPE}},
        {%- endif -%}
        {#- --- 条件必选：OFFCOMPOUNDTYPE=ONLYRG/RGSID 时必选 --- -#}
        {%- if item.OFFCOMPOUNDTYPE in ['ONLYRG', 'RGSID'] -%}
            RG={{item.RG}},
        {%- endif -%}
        {#- --- 条件必选：USAGERPTMODE=ONLINE 时必选 --- -#}
        {%- if item.USAGERPTMODE == 'ONLINE' -%}
            ONLCOMPOUNDTYPE={{item.ONLCOMPOUNDTYPE}},
        {%- endif -%}
        {#- --- 条件必选：ONLCOMPOUNDTYPE=RGSID/ONLYRG 时必选 --- -#}
        {%- if item.ONLCOMPOUNDTYPE in ['RGSID', 'ONLYRG'] -%}
            ONLINERG={{item.ONLINERG}},
        {%- endif -%}
        {#- --- 条件必选：OFFCOMPOUNDTYPE=UPDOWNSID 时必选 --- -#}
        {%- if item.OFFCOMPOUNDTYPE == 'UPDOWNSID' -%}
            DOWNSID={{item.DOWNSID}},
        {%- endif -%}
        {#- --- 条件必选：USAGERPTMODE=MONITORINGKEY 时必选 --- -#}
        {%- if item.USAGERPTMODE == 'MONITORINGKEY' -%}
            MONITORINGKEY="{{item.MONITORINGKEY}}",
        {%- endif -%}
        {#- --- 条件必选：ONLCOMPOUNDTYPE=RGSID 时必选 --- -#}
        {%- if item.ONLCOMPOUNDTYPE == 'RGSID' -%}
            ONLINESID={{item.ONLINESID}},
        {%- endif -%}
        {#- --- 条件必选：OFFCOMPOUNDTYPE=ONLYSID/RGSID 时必选 --- -#}
        {%- if item.OFFCOMPOUNDTYPE in ['ONLYSID', 'RGSID'] -%}
            SID={{item.SID}},
        {%- endif -%}
        {#- --- 条件必选：OFFCOMPOUNDTYPE=UPDOWNSID 时必选 --- -#}
        {%- if item.OFFCOMPOUNDTYPE == 'UPDOWNSID' -%}
            UPSID={{item.UPSID}},
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
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
{%- endif -%}
```

#### 1.2 增加使用量上报规则组。

```jinja2
{%- if is_optional_voice_default_bearer_static_pcc_policy -%}
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
        {%- if item.UPURRNAME2 is not none -%}
            UPURRNAME2="{{item.UPURRNAME2}}",
        {%- endif -%}
        {%- if item.DOWNURRNAME2 is not none -%}
            DOWNURRNAME2="{{item.DOWNURRNAME2}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 1.3 配置PCC策略组。

```jinja2
{%- if is_optional_voice_default_bearer_static_pcc_policy -%}
    {%- for item in add_pccpolicygrp_list -%}
        ADD PCCPOLICYGRP:
        {#- --- 必选参数 --- -#}
        PCCPOLICYGRPNM="{{item.PCCPOLICYGRPNM}}",
        {#- --- 可选参数 --- -#}
        {%- if item.URRGROUPNAME is not none -%}
            URRGROUPNAME="{{item.URRGROUPNAME}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 1.4 配置业务策略规则。

```jinja2
{%- if is_optional_voice_default_bearer_static_pcc_policy -%}
    {%- for item in add_rule_list -%}
        ADD RULE:
        {#- --- 必选参数 --- -#}
        RULENAME="{{item.RULENAME}}",
        POLICYTYPE={{item.POLICYTYPE}},
        {#- --- 可选参数 --- -#}
        {%- if item.PRIORITY is not none -%}
            PRIORITY={{item.PRIORITY}},
        {%- endif -%}
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

#### 1.5 **可选：**配置用户模板。

#### 如果已配置了APN ims使用的用户模板，则跳过本步骤。

```jinja2
{%- if is_optional_voice_default_bearer_static_pcc_policy and is_optional_user_profile -%}
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

#### 1.6 增加用户模板与规则的绑定关系。

```jinja2
{%- if is_optional_voice_default_bearer_static_pcc_policy -%}
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
{%- endif -%}
```

#### 1.7 **可选：**配置用户模板组。

#### 如果已配置了APN ims使用的用户模板组，则跳过本步骤。

```jinja2
{%- if is_optional_voice_default_bearer_static_pcc_policy and is_optional_user_profile_group -%}
    {%- for item in add_usrprofgroup_list -%}
        ADD USRPROFGROUP:
        {#- --- 必选参数 --- -#}
        USERPROFGNAME="{{item.USERPROFGNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 1.8 **可选：**将用户模板绑定到用户模板组中。

#### 如果已配置了APN ims使用的用户模板与模板组的绑定关系，则跳过本步骤。

```jinja2
{%- if is_optional_voice_default_bearer_static_pcc_policy and is_optional_bind_user_profile_to_group -%}
    {%- for item in add_upbindupg_list -%}
        ADD UPBINDUPG:
        {#- --- 必选参数 --- -#}
        USERPROFGNAME="{{item.USERPROFGNAME}}",
        UPBINDTYPE={{item.UPBINDTYPE}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：UPBINDTYPE=SPECIFIC 时必选 --- -#}
        {%- if item.UPBINDTYPE == 'SPECIFIC' -%}
            PRIORITY={{item.PRIORITY}},
        {%- endif -%}
        {#- --- 条件必选：UPBINDTYPE=SPECIFIC/DEFAULT/ULCL 时必选 --- -#}
        {%- if item.UPBINDTYPE in ['SPECIFIC', 'DEFAULT', 'ULCL'] -%}
            USERPROFILENAME="{{item.USERPROFILENAME}}",
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

#### 1.9 **可选：**为APN绑定用户模板组。

#### 如果APN ims已绑定了用户模板组，则跳过本步骤。

```jinja2
{%- if is_optional_voice_default_bearer_static_pcc_policy and is_optional_bind_user_profile_group_to_apn -%}
    {%- for item in add_apnusrprofg_list -%}
        ADD APNUSRPROFG:
        {#- --- 必选参数 --- -#}
        APN="{{item.APN}}",
        USERPROFGNAME="{{item.USERPROFGNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

### 2 配置语音缺省承载静态PCC策略。

#### 2.1 增加使用量上报规则信息。

```jinja2
{%- for item in add_urr_list_2 -%}
    ADD URR:
    {#- --- 必选参数 --- -#}
    URRNAME="{{item.URRNAME}}",
    URRID={{item.URRID}},
    USAGERPTMODE={{item.USAGERPTMODE}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：USAGERPTMODE=OFFLINE 时必选 --- -#}
    {%- if item.USAGERPTMODE == 'OFFLINE' -%}
        OFFCOMPOUNDTYPE={{item.OFFCOMPOUNDTYPE}},
    {%- endif -%}
    {#- --- 条件必选：OFFCOMPOUNDTYPE=ONLYRG/RGSID 时必选 --- -#}
    {%- if item.OFFCOMPOUNDTYPE in ['ONLYRG', 'RGSID'] -%}
        RG={{item.RG}},
    {%- endif -%}
    {#- --- 条件必选：USAGERPTMODE=ONLINE 时必选 --- -#}
    {%- if item.USAGERPTMODE == 'ONLINE' -%}
        ONLCOMPOUNDTYPE={{item.ONLCOMPOUNDTYPE}},
    {%- endif -%}
    {#- --- 条件必选：ONLCOMPOUNDTYPE=RGSID/ONLYRG 时必选 --- -#}
    {%- if item.ONLCOMPOUNDTYPE in ['RGSID', 'ONLYRG'] -%}
        ONLINERG={{item.ONLINERG}},
    {%- endif -%}
    {#- --- 条件必选：OFFCOMPOUNDTYPE=UPDOWNSID 时必选 --- -#}
    {%- if item.OFFCOMPOUNDTYPE == 'UPDOWNSID' -%}
        DOWNSID={{item.DOWNSID}},
    {%- endif -%}
    {#- --- 条件必选：USAGERPTMODE=MONITORINGKEY 时必选 --- -#}
    {%- if item.USAGERPTMODE == 'MONITORINGKEY' -%}
        MONITORINGKEY="{{item.MONITORINGKEY}}",
    {%- endif -%}
    {#- --- 条件必选：ONLCOMPOUNDTYPE=RGSID 时必选 --- -#}
    {%- if item.ONLCOMPOUNDTYPE == 'RGSID' -%}
        ONLINESID={{item.ONLINESID}},
    {%- endif -%}
    {#- --- 条件必选：OFFCOMPOUNDTYPE=ONLYSID/RGSID 时必选 --- -#}
    {%- if item.OFFCOMPOUNDTYPE in ['ONLYSID', 'RGSID'] -%}
        SID={{item.SID}},
    {%- endif -%}
    {#- --- 条件必选：OFFCOMPOUNDTYPE=UPDOWNSID 时必选 --- -#}
    {%- if item.OFFCOMPOUNDTYPE == 'UPDOWNSID' -%}
        UPSID={{item.UPSID}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
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

#### 2.2 增加使用量上报规则组。

```jinja2
{%- for item in add_urrgroup_list_1 -%}
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
    {%- if item.UPURRNAME2 is not none -%}
        UPURRNAME2="{{item.UPURRNAME2}}",
    {%- endif -%}
    {%- if item.DOWNURRNAME2 is not none -%}
        DOWNURRNAME2="{{item.DOWNURRNAME2}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 2.3 配置静态PCC策略的QoS参数。

```jinja2
{%- for item in add_qosprop_list -%}
    ADD QOSPROP:
    {#- --- 必选参数 --- -#}
    QOSPROPNAME="{{item.QOSPROPNAME}}",
    QOSTYPE={{item.QOSTYPE}},
    {#- --- 可选参数 --- -#}
    {%- if item.EMPCAP is not none -%}
        EMPCAP={{item.EMPCAP}},
    {%- endif -%}
    {%- if item.EMPVUL is not none -%}
        EMPVUL={{item.EMPVUL}},
    {%- endif -%}
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
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：QOSTYPE=QOS_FLOW_PARA/QOS_L2_PARA 时必选 --- -#}
    {%- if item.QOSTYPE in ['QOS_FLOW_PARA', 'QOS_L2_PARA'] -%}
        FQI={{item.FQI}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：QOSTYPE=QOS_BEARER_PARA 时可选 --- -#}
    {%- if item.QOSTYPE == 'QOS_BEARER_PARA' -%}
        {%- if item.QCIVALUE is not none -%}
            QCIVALUE={{item.QCIVALUE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：QOSTYPE=QOS_BEARER_PARA/QOS_FLOW_PARA 时可选 --- -#}
    {%- if item.QOSTYPE in ['QOS_BEARER_PARA', 'QOS_FLOW_PARA'] -%}
        {%- if item.QOSURRNAME is not none -%}
            QOSURRNAME="{{item.QOSURRNAME}}",
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

#### 2.4 配置PCC策略组。

```jinja2
{%- for item in add_pccpolicygrp_list_1 -%}
    ADD PCCPOLICYGRP:
    {#- --- 必选参数 --- -#}
    PCCPOLICYGRPNM="{{item.PCCPOLICYGRPNM}}",
    {#- --- 可选参数 --- -#}
    {%- if item.URRGROUPNAME is not none -%}
        URRGROUPNAME="{{item.URRGROUPNAME}}",
    {%- endif -%}
    {%- if item.QOSPROPNAME is not none -%}
        QOSPROPNAME="{{item.QOSPROPNAME}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 2.5 配置业务策略规则。

```jinja2
{%- for item in add_rule_list_1 -%}
    ADD RULE:
    {#- --- 必选参数 --- -#}
    RULENAME="{{item.RULENAME}}",
    POLICYTYPE={{item.POLICYTYPE}},
    {#- --- 可选参数 --- -#}
    {%- if item.PRIORITY is not none -%}
        PRIORITY={{item.PRIORITY}},
    {%- endif -%}
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
```

#### 2.6 **可选：**配置用户模板。

#### 如果已配置了APN ims使用的用户模板，则跳过本步骤。

```jinja2
{%- if is_optional_user_profile -%}
    {%- for item in add_userprofile_list_1 -%}
        ADD USERPROFILE:
        {#- --- 必选参数 --- -#}
        UPTYPE={{item.UPTYPE}},
        USERPROFILENAME="{{item.USERPROFILENAME}}",
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

#### 2.7 增加用户模板与规则的绑定关系。

```jinja2
{%- for item in add_rulebinding_list_1 -%}
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

#### 2.8 **可选：**配置用户模板组。

#### 如果已配置了APN ims使用的用户模板组，则跳过本步骤。

```jinja2
{%- if is_optional_user_profile_group -%}
    {%- for item in add_usrprofgroup_list_1 -%}
        ADD USRPROFGROUP:
        {#- --- 必选参数 --- -#}
        USERPROFGNAME="{{item.USERPROFGNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 2.9 **可选：**将用户模板绑定到用户模板组中。

#### 如果已配置了APN ims使用的用户模板与模板组的绑定关系，则跳过本步骤。

```jinja2
{%- if is_optional_bind_user_profile_to_group -%}
    {%- for item in add_upbindupg_list_1 -%}
        ADD UPBINDUPG:
        {#- --- 必选参数 --- -#}
        UPBINDTYPE={{item.UPBINDTYPE}},
        USERPROFGNAME="{{item.USERPROFGNAME}}",
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：UPBINDTYPE=SPECIFIC 时必选 --- -#}
        {%- if item.UPBINDTYPE == 'SPECIFIC' -%}
            PRIORITY={{item.PRIORITY}},
        {%- endif -%}
        {#- --- 条件必选：UPBINDTYPE=SPECIFIC/DEFAULT/ULCL 时必选 --- -#}
        {%- if item.UPBINDTYPE in ['SPECIFIC', 'DEFAULT', 'ULCL'] -%}
            USERPROFILENAME="{{item.USERPROFILENAME}}",
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

#### 2.10 **可选：**为APN绑定用户模板组。

#### 如果APN ims已绑定了用户模板组，则跳过本步骤。

```jinja2
{%- if is_optional_bind_user_profile_group_to_apn -%}
    {%- for item in add_apnusrprofg_list_1 -%}
        ADD APNUSRPROFG:
        {#- --- 必选参数 --- -#}
        APN="{{item.APN}}",
        USERPROFGNAME="{{item.USERPROFGNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

### 3 配置PCRF Bypass条件。

#### 3.1 配置全局PCRF故障处理动作。

```jinja2
{%- for item in set_pccfailaction_list -%}
    SET PCCFAILACTION:
    {#- --- 可选参数 --- -#}
    {%- if item.SELPEERFAILACT is not none -%}
        SELPEERFAILACT={{item.SELPEERFAILACT}},
    {%- endif -%}
    {%- if item.INITIALFAILACT is not none -%}
        INITIALFAILACT={{item.INITIALFAILACT}},
    {%- endif -%}
    {%- if item.UPDATEFAILACT is not none -%}
        UPDATEFAILACT={{item.UPDATEFAILACT}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：UPDATEFAILACT=ROLLBACK 时可选 --- -#}
    {%- if item.UPDATEFAILACT == 'ROLLBACK' -%}
        {%- if item.UPDFAILLOCPCC is not none -%}
            UPDFAILLOCPCC={{item.UPDFAILLOCPCC}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：INITIALFAILACT=ROLLBACK 时可选 --- -#}
    {%- if item.INITIALFAILACT == 'ROLLBACK' -%}
        {%- if item.INITFAILLOCPCC is not none -%}
            INITFAILLOCPCC={{item.INITFAILLOCPCC}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：INITIALFAILACT=ROLLBACK 时可选 --- -#}
    {%- if item.INITIALFAILACT == 'ROLLBACK' -%}
        {%- if item.INITFAILRDSPCC is not none -%}
            INITFAILRDSPCC={{item.INITFAILRDSPCC}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SELPEERFAILACT=ROLLBACK 时可选 --- -#}
    {%- if item.SELPEERFAILACT == 'ROLLBACK' -%}
        {%- if item.SELPEERLOCPCC is not none -%}
            SELPEERLOCPCC={{item.SELPEERLOCPCC}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SELPEERFAILACT=ROLLBACK 时可选 --- -#}
    {%- if item.SELPEERFAILACT == 'ROLLBACK' -%}
        {%- if item.SELPEERRDSPCC is not none -%}
            SELPEERRDSPCC={{item.SELPEERRDSPCC}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 3.2 配置全局Holding Time。

```jinja2
{%- for item in set_pcctimer_list -%}
    SET PCCTIMER:
    {#- --- 可选参数 --- -#}
    {%- if item.HOLDINGTIME is not none -%}
        HOLDINGTIME={{item.HOLDINGTIME}},
    {%- endif -%}
    {%- if item.ADJUSTRANGE is not none -%}
        ADJUSTRANGE={{item.ADJUSTRANGE}},
    {%- endif -%}
    {%- if item.FASTHOLDINGTIME is not none -%}
        FASTHOLDINGTIME={{item.FASTHOLDINGTIME}},
    {%- endif -%}
    {%- if item.FASTADJUSTRANGE is not none -%}
        FASTADJUSTRANGE={{item.FASTADJUSTRANGE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 3.3 基于PCC模板配置故障处理动作、failover开关和Holding Time。

#### 建议IMS语音业务单独使用一个PCC模板。新建模板使用**ADD PCCTEMPLATE**命令；修改已有模板使用**MOD PCCTEMPLATE**命令。

```jinja2
{%- for item in add_pcctemplate_list -%}
    ADD PCCTEMPLATE:
    {#- --- 必选参数 --- -#}
    PCCTEMPNAME="{{item.PCCTEMPNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.ADJUSTRANGE is not none -%}
        ADJUSTRANGE={{item.ADJUSTRANGE}},
    {%- endif -%}
    {%- if item.HOLDINGTIME is not none -%}
        HOLDINGTIME={{item.HOLDINGTIME}},
    {%- endif -%}
    {%- if item.INITIALFAILACT is not none -%}
        INITIALFAILACT={{item.INITIALFAILACT}},
    {%- endif -%}
    {%- if item.SELPEERFAILACT is not none -%}
        SELPEERFAILACT={{item.SELPEERFAILACT}},
    {%- endif -%}
    {%- if item.UPDATEFAILACT is not none -%}
        UPDATEFAILACT={{item.UPDATEFAILACT}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：INITIALFAILACT=ROLLBACK 时可选 --- -#}
    {%- if item.INITIALFAILACT == 'ROLLBACK' -%}
        {%- if item.INITFAILLOCPCC is not none -%}
            INITFAILLOCPCC={{item.INITFAILLOCPCC}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：INITIALFAILACT=ROLLBACK 时可选 --- -#}
    {%- if item.INITIALFAILACT == 'ROLLBACK' -%}
        {%- if item.INITFAILRDSPCC is not none -%}
            INITFAILRDSPCC={{item.INITFAILRDSPCC}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SELPEERFAILACT=ROLLBACK 时可选 --- -#}
    {%- if item.SELPEERFAILACT == 'ROLLBACK' -%}
        {%- if item.SELPEERLOCPCC is not none -%}
            SELPEERLOCPCC={{item.SELPEERLOCPCC}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SELPEERFAILACT=ROLLBACK 时可选 --- -#}
    {%- if item.SELPEERFAILACT == 'ROLLBACK' -%}
        {%- if item.SELPEERRDSPCC is not none -%}
            SELPEERRDSPCC={{item.SELPEERRDSPCC}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：UPDATEFAILACT=ROLLBACK 时可选 --- -#}
    {%- if item.UPDATEFAILACT == 'ROLLBACK' -%}
        {%- if item.UPDFAILLOCPCC is not none -%}
            UPDFAILLOCPCC={{item.UPDFAILLOCPCC}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in mod_pcctemplate_list -%}
    MOD PCCTEMPLATE:
    {#- --- 必选参数 --- -#}
    PCCTEMPNAME="{{item.PCCTEMPNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.SELPEERFAILACT is not none -%}
        SELPEERFAILACT={{item.SELPEERFAILACT}},
    {%- endif -%}
    {%- if item.INITIALFAILACT is not none -%}
        INITIALFAILACT={{item.INITIALFAILACT}},
    {%- endif -%}
    {%- if item.UPDATEFAILACT is not none -%}
        UPDATEFAILACT={{item.UPDATEFAILACT}},
    {%- endif -%}
    {%- if item.HOLDINGTIME is not none -%}
        HOLDINGTIME={{item.HOLDINGTIME}},
    {%- endif -%}
    {%- if item.ADJUSTRANGE is not none -%}
        ADJUSTRANGE={{item.ADJUSTRANGE}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：UPDATEFAILACT=ROLLBACK 时可选 --- -#}
    {%- if item.UPDATEFAILACT == 'ROLLBACK' -%}
        {%- if item.UPDFAILLOCPCC is not none -%}
            UPDFAILLOCPCC={{item.UPDFAILLOCPCC}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：INITIALFAILACT=ROLLBACK 时可选 --- -#}
    {%- if item.INITIALFAILACT == 'ROLLBACK' -%}
        {%- if item.INITFAILLOCPCC is not none -%}
            INITFAILLOCPCC={{item.INITFAILLOCPCC}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：INITIALFAILACT=ROLLBACK 时可选 --- -#}
    {%- if item.INITIALFAILACT == 'ROLLBACK' -%}
        {%- if item.INITFAILRDSPCC is not none -%}
            INITFAILRDSPCC={{item.INITFAILRDSPCC}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SELPEERFAILACT=ROLLBACK 时可选 --- -#}
    {%- if item.SELPEERFAILACT == 'ROLLBACK' -%}
        {%- if item.SELPEERLOCPCC is not none -%}
            SELPEERLOCPCC={{item.SELPEERLOCPCC}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SELPEERFAILACT=ROLLBACK 时可选 --- -#}
    {%- if item.SELPEERFAILACT == 'ROLLBACK' -%}
        {%- if item.SELPEERRDSPCC is not none -%}
            SELPEERRDSPCC={{item.SELPEERRDSPCC}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 3.4 配置对端PCRF/DRA回复指定结果码后PGW-C的处理操作。

#### 具体结果码需要与对端PCRF/DRA确认。

```jinja2
{%- for item in add_resultcodectrl_list -%}
    ADD RESULTCODECTRL:
    {#- --- 必选参数 --- -#}
    PCCTEMPLATE="{{item.PCCTEMPLATE}}",
    INTFTYPE={{item.INTFTYPE}},
    {#- --- 可选参数 --- -#}
    {%- if item.DIRECTINITACT is not none -%}
        DIRECTINITACT={{item.DIRECTINITACT}},
    {%- endif -%}
    {%- if item.DIRECTUPDACT is not none -%}
        DIRECTUPDACT={{item.DIRECTUPDACT}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：INTFTYPE=INTFTYPE_GX 时必选 --- -#}
    {%- if item.INTFTYPE == 'INTFTYPE_GX' -%}
        VENDORID={{item.VENDORID}},
    {%- endif -%}
    {#- --- 条件必选：INTFTYPE=INTFTYPE_GX 时必选 --- -#}
    {%- if item.INTFTYPE == 'INTFTYPE_GX' -%}
        GXRESULTCODEVAL="{{item.GXRESULTCODEVAL}}",
    {%- endif -%}
    {#- --- 条件必选：INTFTYPE=INTFTYPE_N7 时必选 --- -#}
    {%- if item.INTFTYPE == 'INTFTYPE_N7' -%}
        N7RESULTCODEVAL="{{item.N7RESULTCODEVAL}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：DIRECTINITACT=LOCALPCC 时可选 --- -#}
    {%- if item.DIRECTINITACT == 'LOCALPCC' -%}
        {%- if item.DIRECTINITHTSW is not none -%}
            DIRECTINITHTSW={{item.DIRECTINITHTSW}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：DIRECTUPDACT=TERMINATE 时可选 --- -#}
    {%- if item.DIRECTUPDACT == 'TERMINATE' -%}
        {%- if item.DIRECTREACTREQ is not none -%}
            DIRECTREACTREQ={{item.DIRECTREACTREQ}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：DIRECTUPDACT=INHERIT_PCC/LOCALPCC 时可选 --- -#}
    {%- if item.DIRECTUPDACT in ['INHERIT_PCC', 'LOCALPCC'] -%}
        {%- if item.DIRECTUPDHTSW is not none -%}
            DIRECTUPDHTSW={{item.DIRECTUPDHTSW}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in mod_resultcodectrl_list -%}
    MOD RESULTCODECTRL:
    {#- --- 必选参数 --- -#}
    INTFTYPE={{item.INTFTYPE}},
    PCCTEMPLATE="{{item.PCCTEMPLATE}}",
    {#- --- 可选参数 --- -#}
    {%- if item.DIRECTINITACT is not none -%}
        DIRECTINITACT={{item.DIRECTINITACT}},
    {%- endif -%}
    {%- if item.DIRECTUPDACT is not none -%}
        DIRECTUPDACT={{item.DIRECTUPDACT}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：INTFTYPE=INTFTYPE_GX 时必选 --- -#}
    {%- if item.INTFTYPE == 'INTFTYPE_GX' -%}
        GXRESULTCODEVAL="{{item.GXRESULTCODEVAL}}",
    {%- endif -%}
    {#- --- 条件必选：INTFTYPE=INTFTYPE_N7 时必选 --- -#}
    {%- if item.INTFTYPE == 'INTFTYPE_N7' -%}
        N7RESULTCODEVAL="{{item.N7RESULTCODEVAL}}",
    {%- endif -%}
    {#- --- 条件必选：INTFTYPE=INTFTYPE_GX 时必选 --- -#}
    {%- if item.INTFTYPE == 'INTFTYPE_GX' -%}
        VENDORID={{item.VENDORID}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：DIRECTINITACT=LOCALPCC 时可选 --- -#}
    {%- if item.DIRECTINITACT == 'LOCALPCC' -%}
        {%- if item.DIRECTINITHTSW is not none -%}
            DIRECTINITHTSW={{item.DIRECTINITHTSW}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：DIRECTUPDACT=TERMINATE 时可选 --- -#}
    {%- if item.DIRECTUPDACT == 'TERMINATE' -%}
        {%- if item.DIRECTREACTREQ is not none -%}
            DIRECTREACTREQ={{item.DIRECTREACTREQ}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：DIRECTUPDACT=INHERIT_PCC/LOCALPCC 时可选 --- -#}
    {%- if item.DIRECTUPDACT in ['INHERIT_PCC', 'LOCALPCC'] -%}
        {%- if item.DIRECTUPDHTSW is not none -%}
            DIRECTUPDHTSW={{item.DIRECTUPDHTSW}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_resultcodedra_list -%}
    ADD RESULTCODEDRA:
    {#- --- 必选参数 --- -#}
    VENDORID={{item.VENDORID}},
    PCCTEMPLATE="{{item.PCCTEMPLATE}}",
    RESULTCODEVAL="{{item.RESULTCODEVAL}}",
    {#- --- 可选参数 --- -#}
    {%- if item.INITACTION is not none -%}
        INITACTION={{item.INITACTION}},
    {%- endif -%}
    {%- if item.UPDATEACTION is not none -%}
        UPDATEACTION={{item.UPDATEACTION}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：INITACTION=LOCALPCC 时可选 --- -#}
    {%- if item.INITACTION == 'LOCALPCC' -%}
        {%- if item.INITHOLDTMSW is not none -%}
            INITHOLDTMSW={{item.INITHOLDTMSW}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：UPDATEACTION=INHERIT_PCC/LOCALPCC 时可选 --- -#}
    {%- if item.UPDATEACTION in ['INHERIT_PCC', 'LOCALPCC'] -%}
        {%- if item.UPDHOLDTMSW is not none -%}
            UPDHOLDTMSW={{item.UPDHOLDTMSW}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：UPDATEACTION=TERMINATE 时可选 --- -#}
    {%- if item.UPDATEACTION == 'TERMINATE' -%}
        {%- if item.REACTREQ is not none -%}
            REACTREQ={{item.REACTREQ}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 3.5 增加PCC故障场景维持BYPASS状态码配置。

```jinja2
{%- for item in add_pccbypasscode_list -%}
    ADD PCCBYPASSCODE:
    {#- --- 必选参数 --- -#}
    PCCTEMPLATE="{{item.PCCTEMPLATE}}",
    INTFTYPE={{item.INTFTYPE}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：INTFTYPE=INTFTYPE_GX 时必选 --- -#}
    {%- if item.INTFTYPE == 'INTFTYPE_GX' -%}
        GXRESULTCODEVAL="{{item.GXRESULTCODEVAL}}",
    {%- endif -%}
    {#- --- 条件必选：INTFTYPE=INTFTYPE_N7 时必选 --- -#}
    {%- if item.INTFTYPE == 'INTFTYPE_N7' -%}
        N7RESULTCODEVAL="{{item.N7RESULTCODEVAL}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：INTFTYPE=INTFTYPE_N7 时可选 --- -#}
    {%- if item.INTFTYPE == 'INTFTYPE_N7' -%}
        {%- if item.ERRINFO is not none -%}
            ERRINFO="{{item.ERRINFO}}",
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 3.6 配置更新流程Gx接口不支持Failover场景、PGW-C和PCRF直连场景Failover后收到备PCRF返回异常码场景和PGW-C和PCRF非直连场景Failover后收到DRA返回非5012/3002异常码场景，分别在有、无语音专有承载时的处理动作，以及在PGW-C和PCRF非直连场景没有语音专有承载时，会话退出PCRF Bypass状态是否发送探测消息。

```jinja2
{%- for item in set_imsbypassfunc_list -%}
    SET IMSBYPASSFUNC:
    {#- --- 可选参数 --- -#}
    {%- if item.ACTNODEDBEARER is not none -%}
        ACTNODEDBEARER={{item.ACTNODEDBEARER}},
    {%- endif -%}
    {%- if item.ACTWITDEDBEARER is not none -%}
        ACTWITDEDBEARER={{item.ACTWITDEDBEARER}},
    {%- endif -%}
    {%- if item.TSTUPDATEREQSW is not none -%}
        TSTUPDATEREQSW={{item.TSTUPDATEREQSW}},
    {%- endif -%}
    {%- if item.REACTREQ is not none -%}
        REACTREQ={{item.REACTREQ}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：ACTWITDEDBEARER=FASTROLLBACK 时可选 --- -#}
    {%- if item.ACTWITDEDBEARER == 'FASTROLLBACK' -%}
        {%- if item.FAILLOCPCC is not none -%}
            FAILLOCPCC={{item.FAILLOCPCC}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 3.7 Gx接口PGW-C和PCRF非直连场景，对于支持Failover的DRA配置支持Failover功能。

#### 如果DRA不支持Failover则跳过本步骤。

```jinja2
{%- for item in mod_diamrtrealm_list -%}
    MOD DIAMRTREALM:
    {#- --- 必选参数 --- -#}
    REALMNAME="{{item.REALMNAME}}",
    APPLICATION={{item.APPLICATION}},
    {#- --- 可选参数 --- -#}
    {%- if item.FAILOVERSW is not none -%}
        FAILOVERSW={{item.FAILOVERSW}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 3.8 **可选：**为DNN绑定PCC模板，如果已经绑定过，则不需要执行该步骤。

```jinja2
{%- if is_optional_bind_pcc_template_to_dnn -%}
    {%- for item in set_apnpccfunc_list -%}
        SET APNPCCFUNC:
        {#- --- 必选参数 --- -#}
        APN="{{item.APN}}",
        {#- --- 可选参数 --- -#}
        {%- if item.PCCTEMPLATE is not none -%}
            PCCTEMPLATE="{{item.PCCTEMPLATE}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 3.9 设置承载空闲定时器时长，在呼叫结束，业务空闲超过该时长后可以删除承载。

```jinja2
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
        {%- if item.PCTXCHKSW is not none -%}
            PCTXCHKSW={{item.PCTXCHKSW}},
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
        {%- if item.DFTBEARPOLICY is not none -%}
            DFTBEARPOLICY={{item.DFTBEARPOLICY}},
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
        {%- if item.DFTBRPLCYGGSN is not none -%}
            DFTBRPLCYGGSN={{item.DFTBRPLCYGGSN}},
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
        {%- if item.HSMFTIMERLEVEL is not none -%}
            HSMFTIMERLEVEL={{item.HSMFTIMERLEVEL}},
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
```

#### 3.10 配置语音业务APN的会话在N7接口发送重激活请求的Delete Bearer Request消息或者PduSession Release Command消息中携带cause信元值为“reactivation requested”。

```jinja2
{%- for item in mod_apn_list -%}
    MOD APN:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    {#- --- 可选参数 --- -#}
    {%- if item.REACWITHDEL is not none -%}
        REACWITHDEL={{item.REACWITHDEL}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：REACWITHDEL=SPECIFIC_SCENE 时可选 --- -#}
    {%- if item.REACWITHDEL == 'SPECIFIC_SCENE' -%}
        {%- if item.SCENELIST is not none -%}
            SCENELIST={{item.SCENELIST}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 配置相关软参。

#### 4.1 通过软参DWORD519 Bit5配置在HoldingTime超时时，用户会话中有语音专有承载时不去活会话，重启HoldingTime定时器；没有语音专有承载时去活会话。

```jinja2
{%- for item in set_smfsoftparaofbit_list -%}
    SET SMFSOFTPARAOFBIT:
    {#- --- 必选参数 --- -#}
    DT={{item.DT}},
    VALUE={{item.VALUE}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：DT=Dw 时必选 --- -#}
    {%- if item.DT == 'Dw' -%}
        DWORDNUM={{item.DWORDNUM}},
    {%- endif -%}
    {#- --- 条件必选：DT=Dw 时必选 --- -#}
    {%- if item.DT == 'Dw' -%}
        POSITION={{item.POSITION}},
    {%- endif -%}
    {#- --- 条件必选：DT=Byte 时必选 --- -#}
    {%- if item.DT == 'Byte' -%}
        BYTENUM={{item.BYTENUM}},
    {%- endif -%}
    {#- --- 条件必选：DT=Byte 时必选 --- -#}
    {%- if item.DT == 'Byte' -%}
        BYTEPOSITION={{item.BYTEPOSITION}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 4.2 通过软参DWORD519 Bit9配置在PGW-C激活流程查询PCRF失败发生回滚时，HoldingTime功能（当HoldingTime超时时，去活会话）生效。

```jinja2
{%- for item in set_smfsoftparaofbit_list_2 -%}
    SET SMFSOFTPARAOFBIT:
    {#- --- 必选参数 --- -#}
    DT={{item.DT}},
    VALUE={{item.VALUE}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：DT=Dw 时必选 --- -#}
    {%- if item.DT == 'Dw' -%}
        DWORDNUM={{item.DWORDNUM}},
    {%- endif -%}
    {#- --- 条件必选：DT=Dw 时必选 --- -#}
    {%- if item.DT == 'Dw' -%}
        POSITION={{item.POSITION}},
    {%- endif -%}
    {#- --- 条件必选：DT=Byte 时必选 --- -#}
    {%- if item.DT == 'Byte' -%}
        BYTENUM={{item.BYTENUM}},
    {%- endif -%}
    {#- --- 条件必选：DT=Byte 时必选 --- -#}
    {%- if item.DT == 'Byte' -%}
        BYTEPOSITION={{item.BYTEPOSITION}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 4.3 **可选：**通过软参DWORD544 BIT17配置语音PCRF进入Bypass后，HoldingTime定时器启动三次后是否强制去活会话。

```jinja2
{%- if is_optional_force_deactivate_session -%}
    {%- for item in set_smfsoftparaofbit_list_4 -%}
        SET SMFSOFTPARAOFBIT:
        {#- --- 必选参数 --- -#}
        DT={{item.DT}},
        VALUE={{item.VALUE}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：DT=Dw 时必选 --- -#}
        {%- if item.DT == 'Dw' -%}
            DWORDNUM={{item.DWORDNUM}},
        {%- endif -%}
        {#- --- 条件必选：DT=Dw 时必选 --- -#}
        {%- if item.DT == 'Dw' -%}
            POSITION={{item.POSITION}},
        {%- endif -%}
        {#- --- 条件必选：DT=Byte 时必选 --- -#}
        {%- if item.DT == 'Byte' -%}
            BYTENUM={{item.BYTENUM}},
        {%- endif -%}
        {#- --- 条件必选：DT=Byte 时必选 --- -#}
        {%- if item.DT == 'Byte' -%}
            BYTEPOSITION={{item.BYTEPOSITION}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 4.4 通过软参DWORD545 BIT18配置PGW-C对接语音PCRF时将业务触发专载的双向流进行拆分处理。

```jinja2
{%- for item in set_smfsoftparaofbit_list_6 -%}
    SET SMFSOFTPARAOFBIT:
    {#- --- 必选参数 --- -#}
    DT={{item.DT}},
    VALUE={{item.VALUE}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：DT=Dw 时必选 --- -#}
    {%- if item.DT == 'Dw' -%}
        DWORDNUM={{item.DWORDNUM}},
    {%- endif -%}
    {#- --- 条件必选：DT=Dw 时必选 --- -#}
    {%- if item.DT == 'Dw' -%}
        POSITION={{item.POSITION}},
    {%- endif -%}
    {#- --- 条件必选：DT=Byte 时必选 --- -#}
    {%- if item.DT == 'Byte' -%}
        BYTENUM={{item.BYTENUM}},
    {%- endif -%}
    {#- --- 条件必选：DT=Byte 时必选 --- -#}
    {%- if item.DT == 'Byte' -%}
        BYTEPOSITION={{item.BYTEPOSITION}},
    {%- endif -%}
    ;
{%- endfor -%}
```


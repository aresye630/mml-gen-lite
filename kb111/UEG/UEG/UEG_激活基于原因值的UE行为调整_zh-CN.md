---
id: GWFD-024301
name: 激活基于原因值的UE行为调整
ne_type: UEG
type: feature
description: 本操作指导介绍在运行网络中激活基于原因值的UE行为调整特性的操作过程。  UEG通过向UE发送不同的原因值以调整UE的行为。  适用于SGSN、MME。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝L","MEC 特性指南（风筝L）","MME特性指南","GWFD-024300 系统管理","GWFD-024301 基于原因值的UE行为调整（适用于MME）","激活基于原因值的UE行为调整"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
本操作指导介绍在运行网络中激活基于原因值的UE行为调整特性的操作过程。UEG通过向UE发送不同的原因值以调整UE的行为。适用于SGSN、MME。

## 必备事项
前提条件

* HLR/HSS上已有相关用户签约信息。
* 请仔细阅读GWFD-024301 基于原因值的UE行为调整（适用于MME）特性概述。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    set_gmmproctrl_list:
      type: items
      properties:
        PROT:
          name: '流程类型'
          type: string
          enum:
          - AIR
          - ATTACH
          - AUTHENTICATION
          - CANCEL_LOCATION
          - CHECK_IMEI
          - INTER_RAU
          - INTRA_RAU
          - NET_SHARE
          - PAGING
          - UPDATE_LOCATION
          required: true
          description: 'MM流程控制参数'
          data_source: '全网规划'
          pattern: ''
          default: ''
        ULRIMSIGTERR:
          name: 'ULR拒绝原因值（IMSIGT错误）'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        ULRSCCPGTERR:
          name: 'ULR拒绝原因值（SCCPGT错误）'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        ULRLINKERR:
          name: 'ULR拒绝原因值（链路异常）'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        ULRHLRHSSTMOUT:
          name: 'ULR拒绝原因值（HLR/HSS超时）'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        ULRHLRHSSREJ:
          name: 'ULR拒绝原因值（HLR/HSS拒绝）'
          type: integer
          minimum: 0
          maximum: 127
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        AIRIMSIGTERR:
          name: 'AIR拒绝原因值（IMSIGT错误）'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        AIRLINKERR:
          name: 'AIR拒绝原因值（链路异常）'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        AIRHLRHSSTMOUT:
          name: 'AIR拒绝原因值（HLR/HSS超时）'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        AIRHLRHSSREJ:
          name: 'AIR拒绝原因值（HLR/HSS拒绝）'
          type: integer
          minimum: 0
          maximum: 127
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        ATTACHROAMRST:
          name: 'Attach拒绝原因值（漫游受限）'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        INTRARAUIDTYTMOUT:
          name: 'Intra RAU拒绝原因值（Identity超时）'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        INTERRAUSGSNTMOUT:
          name: 'Inter RAU拒绝原因值'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        INTERRAUROAMRST:
          name: 'Inter RAU拒绝原因值（漫游受限）'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        INTERRAUIDTYTMOUT:
          name: 'Inter RAU拒绝原因值（Identity超时）'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        INTERRAUDNSFAIL:
          name: 'Inter RAU拒绝原因值（DNS解析失败）'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        AUTHRESCHKFAIL:
          name: 'Authentication拒绝原因值（鉴权检查失败）'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        CHKIMEICHKFAIL:
          name: 'Check IMEI拒绝原因值（IMEI检查失败）'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        DETACHCAUSE_CLR:
          name: '分离请求原因值'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    set_pmmproctrl_list:
      type: items
      properties:
        PROT:
          name: '流程类型'
          type: string
          enum:
          - AIR
          - ATTACH
          - AUTHENTICATION
          - CANCEL_LOCATION
          - CHECK_IMEI
          - INTER_RAU
          - INTRA_RAU
          - IU_RELEASE
          - NET_SHARE
          - PAGING
          - UPDATE_LOCATION
          required: true
          description: 'MM流程控制参数'
          data_source: '全网规划'
          pattern: ''
          default: ''
        ULRHLRHSSTMOUT:
          name: 'ULR拒绝原因值（HLR/HSS超时）'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        ULRIMSIGTERR:
          name: 'ULR拒绝原因值（IMSIGT错误）'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        ULRSCCPGTERR:
          name: 'ULR拒绝原因值（SCCPGT错误）'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        ULRLINKERR:
          name: 'ULR拒绝原因值（链路异常）'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        ULRHLRHSSREJ:
          name: 'ULR拒绝原因值（HLR/HSS拒绝）'
          type: integer
          minimum: 0
          maximum: 127
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        AIRIMSIGTERR:
          name: 'AIR拒绝原因值（IMSIGT错误）'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        AIRLINKERR:
          name: 'AIR拒绝原因值（链路异常）'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        AIRHLRHSSTMOUT:
          name: 'AIR拒绝原因值（HLR/HSS超时）'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        AIRHLRHSSREJ:
          name: 'AIR拒绝原因值（HLR/HSS拒绝）'
          type: integer
          minimum: 0
          maximum: 127
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        ATTACHROAMRST:
          name: 'Attach拒绝原因值（漫游受限）'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        INTRARAUIDTYTMOUT:
          name: 'Intra RAU拒绝原因值（Identity超时）'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        INTERRAUSGSNTMOUT:
          name: 'Inter RAU拒绝原因值'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        INTERRAUROAMRST:
          name: 'Inter RAU拒绝原因值（漫游受限）'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        INTERRAUIDTYTMOUT:
          name: 'Inter RAU拒绝原因值（Identity超时）'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        INTERRAUDNSFAIL:
          name: 'Inter RAU拒绝原因值（DNS解析失败）'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        AUTHRESCHKFAIL:
          name: 'Authentication拒绝原因值（鉴权检查失败）'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        CHKIMEICHKFAIL:
          name: 'Check IMEI拒绝原因值（IMEI检查失败）'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        DETACHCAUSE_CLR:
          name: '分离请求原因值'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    set_emmproctrl_list:
      type: items
      properties:
        PROT:
          name: '流程类型'
          type: string
          enum:
          - AIR
          - ATTACH
          - AUTHENTICATION
          - CHECK_IMEI
          - CONTEXT_RESPONSE
          - INTER_TAU
          - LOCATION_UPDATE
          - PAGING
          - UPDATE_LOCATION
          required: true
          description: 'MM流程控制参数'
          data_source: '全网规划'
          pattern: ''
          default: ''
        ULRHSSREJ:
          name: 'ULR拒绝原因值（HSS拒绝）'
          type: integer
          minimum: 0
          maximum: 127
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        ATTACHROAMRST:
          name: 'Attach拒绝原因值（漫游受限）'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        AUTHRESCHKFAIL:
          name: 'Authentication拒绝原因值（鉴权检查失败）'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        CHKIMEICHKFAIL:
          name: 'Check IMEI拒绝原因值（IMEI检查失败）'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        ULRHSSTMOUT:
          name: 'ULR拒绝原因值（HSS超时）'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        ULRDMERR:
          name: 'ULR拒绝原因值（Diameter链路异常）'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        AIRHSSTMOUT:
          name: 'AIR拒绝原因值（HSS超时）'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        AIRHSSREJ:
          name: 'AIR拒绝原因值（HSS拒绝）'
          type: integer
          minimum: 0
          maximum: 127
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        AIRDMERR:
          name: 'AIR拒绝原因值（Diameter链路异常）'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        INTERTAUROAMRST:
          name: 'Inter TAU拒绝原因值（漫游受限）'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        INTERTAUDNSFAIL:
          name: 'Inter TAU拒绝原因值（DNS解析失败）'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_emmproctrlimsi_list:
      type: items
      properties:
        SUBRANGE:
          name: '用户范围'
          type: string
          enum:
          - FOREIGN_USER
          - HOME_USER
          - IMSI_PREFIX
          - SPECIFIC_IMSI
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IMSIPRE:
          name: 'IMSI前缀'
          type: string
          maxLength: 14
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ULRHSSREJ:
          name: 'ULR拒绝原因值（HSS拒绝）'
          type: integer
          minimum: 0
          maximum: 127
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 0
    set_gbsmproctrl_list:
      type: items
      properties:
        PROT:
          name: '流程类型'
          type: string
          enum:
          - ACT_PROC
          - HSS_INIT_SUB_QOS_MOD_PROC
          - MOD_PROC
          - PFC_PROC
          required: true
          description: 'SM流程控制参数'
          data_source: '全网规划'
          pattern: ''
          default: ''
        ACTGGSNTMOUT:
          name: '激活拒绝原因'
          type: integer
          minimum: 0
          maximum: 112
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        ACTGGSNREJ:
          name: '激活拒绝原因'
          type: integer
          minimum: 0
          maximum: 127
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        MODGGSNREJ:
          name: '修改拒绝原因值'
          type: integer
          minimum: 0
          maximum: 127
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    set_iusmproctrl_list:
      type: items
      properties:
        PROT:
          name: '流程类型'
          type: string
          enum:
          - ACT_PROC
          - HSS_INIT_SUB_QOS_MOD_PROC
          - MOD_PROC
          required: true
          description: 'SM流程控制参数'
          data_source: '全网规划'
          pattern: ''
          default: ''
        ACTGGSNTMOUT:
          name: '激活拒绝原因'
          type: integer
          minimum: 0
          maximum: 112
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        ACTGGSNREJ:
          name: '激活拒绝原因'
          type: integer
          minimum: 0
          maximum: 127
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        MODGGSNREJ:
          name: '修改拒绝原因值'
          type: integer
          minimum: 0
          maximum: 127
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    set_s1smproctrl_list:
      type: items
      properties:
        PROT:
          name: '流程类型'
          type: string
          enum:
          - ATTACH_BEARER_ACT_PROC
          - BEARER_DEACT_PROC
          - BEARER_MODIFICATION_PROC
          - BEARER_RESOURCE_ALLOCTION_PROC
          - BEARER_RESOURCE_MOD_PROC
          - DEDICATED_BEARER_ACT_PROC
          - HSS_INIT_SUB_QOS_MOD_PROC
          - PDN_CONNECTIVITY_PROC
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        PDNCONSGWREJ:
          name: 'PDN连接拒绝原因值组号(SGW拒绝)'
          type: integer
          minimum: 0
          maximum: 127
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        PDNCONSGWTMOUT:
          name: 'PDN连接拒绝原因值(SGW超时)'
          type: integer
          minimum: 0
          maximum: 112
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_causegrp_list:
      type: items
      properties:
        CAUSEGRPID:
          name: '原因值组标识'
          type: integer
          minimum: 1
          maximum: 127
          required: true
          description: '原因值映射组配置'
          data_source: '全网规划'
          pattern: ''
          default: ''
        CAUSEGRPNM:
          name: '原因值组名称'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'noname'
    add_causemap_list:
      type: items
      properties:
        CAUSEGRPID:
          name: '原因值组标识'
          type: integer
          minimum: 1
          maximum: 127
          required: true
          description: '原因值映射配置'
          data_source: '全网规划'
          pattern: ''
          default: ''
        CAUSERANGE:
          name: '原因值范围'
          type: string
          enum:
          - DEFAULT
          - SPECIAL
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DEFAULT
        BGCAUSE:
          name: '起始原始原因值'
          type: integer
          minimum: 1
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        EDCAUSE:
          name: '终止原始原因值'
          type: integer
          minimum: 1
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TCAUSE:
          name: '目标原因值'
          type: integer
          minimum: 1
          maximum: 65535
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_gmmproctrl_list_1:
      type: items
      properties:
        PROT:
          name: '流程类型'
          type: string
          enum:
          - AIR
          - ATTACH
          - AUTHENTICATION
          - CANCEL_LOCATION
          - CHECK_IMEI
          - INTER_RAU
          - INTRA_RAU
          - NET_SHARE
          - PAGING
          - UPDATE_LOCATION
          required: true
          description: 'MM流程控制参数'
          data_source: '全网规划'
          pattern: ''
          default: ''
        ULRIMSIGTERR:
          name: 'ULR拒绝原因值（IMSIGT错误）'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        ULRSCCPGTERR:
          name: 'ULR拒绝原因值（SCCPGT错误）'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        ULRLINKERR:
          name: 'ULR拒绝原因值（链路异常）'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        ULRHLRHSSTMOUT:
          name: 'ULR拒绝原因值（HLR/HSS超时）'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        ULRHLRHSSREJ:
          name: 'ULR拒绝原因值（HLR/HSS拒绝）'
          type: integer
          minimum: 0
          maximum: 127
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        AIRIMSIGTERR:
          name: 'AIR拒绝原因值（IMSIGT错误）'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        AIRLINKERR:
          name: 'AIR拒绝原因值（链路异常）'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        AIRHLRHSSTMOUT:
          name: 'AIR拒绝原因值（HLR/HSS超时）'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        AIRHLRHSSREJ:
          name: 'AIR拒绝原因值（HLR/HSS拒绝）'
          type: integer
          minimum: 0
          maximum: 127
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        ATTACHROAMRST:
          name: 'Attach拒绝原因值（漫游受限）'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        INTRARAUIDTYTMOUT:
          name: 'Intra RAU拒绝原因值（Identity超时）'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        INTERRAUSGSNTMOUT:
          name: 'Inter RAU拒绝原因值'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        INTERRAUROAMRST:
          name: 'Inter RAU拒绝原因值（漫游受限）'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        INTERRAUIDTYTMOUT:
          name: 'Inter RAU拒绝原因值（Identity超时）'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        INTERRAUDNSFAIL:
          name: 'Inter RAU拒绝原因值（DNS解析失败）'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        AUTHRESCHKFAIL:
          name: 'Authentication拒绝原因值（鉴权检查失败）'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        CHKIMEICHKFAIL:
          name: 'Check IMEI拒绝原因值（IMEI检查失败）'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        DETACHCAUSE_CLR:
          name: '分离请求原因值'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    set_pmmproctrl_list_1:
      type: items
      properties:
        PROT:
          name: '流程类型'
          type: string
          enum:
          - AIR
          - ATTACH
          - AUTHENTICATION
          - CANCEL_LOCATION
          - CHECK_IMEI
          - INTER_RAU
          - INTRA_RAU
          - IU_RELEASE
          - NET_SHARE
          - PAGING
          - UPDATE_LOCATION
          required: true
          description: 'MM流程控制参数'
          data_source: '全网规划'
          pattern: ''
          default: ''
        ULRHLRHSSTMOUT:
          name: 'ULR拒绝原因值（HLR/HSS超时）'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        ULRIMSIGTERR:
          name: 'ULR拒绝原因值（IMSIGT错误）'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        ULRSCCPGTERR:
          name: 'ULR拒绝原因值（SCCPGT错误）'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        ULRLINKERR:
          name: 'ULR拒绝原因值（链路异常）'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        ULRHLRHSSREJ:
          name: 'ULR拒绝原因值（HLR/HSS拒绝）'
          type: integer
          minimum: 0
          maximum: 127
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        AIRIMSIGTERR:
          name: 'AIR拒绝原因值（IMSIGT错误）'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        AIRLINKERR:
          name: 'AIR拒绝原因值（链路异常）'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        AIRHLRHSSTMOUT:
          name: 'AIR拒绝原因值（HLR/HSS超时）'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        AIRHLRHSSREJ:
          name: 'AIR拒绝原因值（HLR/HSS拒绝）'
          type: integer
          minimum: 0
          maximum: 127
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        ATTACHROAMRST:
          name: 'Attach拒绝原因值（漫游受限）'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        INTRARAUIDTYTMOUT:
          name: 'Intra RAU拒绝原因值（Identity超时）'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        INTERRAUSGSNTMOUT:
          name: 'Inter RAU拒绝原因值'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        INTERRAUROAMRST:
          name: 'Inter RAU拒绝原因值（漫游受限）'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        INTERRAUIDTYTMOUT:
          name: 'Inter RAU拒绝原因值（Identity超时）'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        INTERRAUDNSFAIL:
          name: 'Inter RAU拒绝原因值（DNS解析失败）'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        AUTHRESCHKFAIL:
          name: 'Authentication拒绝原因值（鉴权检查失败）'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        CHKIMEICHKFAIL:
          name: 'Check IMEI拒绝原因值（IMEI检查失败）'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        DETACHCAUSE_CLR:
          name: '分离请求原因值'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    set_emmproctrl_list_1:
      type: items
      properties:
        PROT:
          name: '流程类型'
          type: string
          enum:
          - AIR
          - ATTACH
          - AUTHENTICATION
          - CHECK_IMEI
          - CONTEXT_RESPONSE
          - INTER_TAU
          - LOCATION_UPDATE
          - PAGING
          - UPDATE_LOCATION
          required: true
          description: 'MM流程控制参数'
          data_source: '全网规划'
          pattern: ''
          default: ''
        ULRHSSREJ:
          name: 'ULR拒绝原因值（HSS拒绝）'
          type: integer
          minimum: 0
          maximum: 127
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        ATTACHROAMRST:
          name: 'Attach拒绝原因值（漫游受限）'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        AUTHRESCHKFAIL:
          name: 'Authentication拒绝原因值（鉴权检查失败）'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        CHKIMEICHKFAIL:
          name: 'Check IMEI拒绝原因值（IMEI检查失败）'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        ULRHSSTMOUT:
          name: 'ULR拒绝原因值（HSS超时）'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        ULRDMERR:
          name: 'ULR拒绝原因值（Diameter链路异常）'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        AIRHSSTMOUT:
          name: 'AIR拒绝原因值（HSS超时）'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        AIRHSSREJ:
          name: 'AIR拒绝原因值（HSS拒绝）'
          type: integer
          minimum: 0
          maximum: 127
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        AIRDMERR:
          name: 'AIR拒绝原因值（Diameter链路异常）'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        INTERTAUROAMRST:
          name: 'Inter TAU拒绝原因值（漫游受限）'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        INTERTAUDNSFAIL:
          name: 'Inter TAU拒绝原因值（DNS解析失败）'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_emmproctrlimsi_list_1:
      type: items
      properties:
        SUBRANGE:
          name: '用户范围'
          type: string
          enum:
          - FOREIGN_USER
          - HOME_USER
          - IMSI_PREFIX
          - SPECIFIC_IMSI
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IMSIPRE:
          name: 'IMSI前缀'
          type: string
          maxLength: 14
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ULRHSSREJ:
          name: 'ULR拒绝原因值（HSS拒绝）'
          type: integer
          minimum: 0
          maximum: 127
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 0
    set_gbsmproctrl_list_1:
      type: items
      properties:
        PROT:
          name: '流程类型'
          type: string
          enum:
          - ACT_PROC
          - HSS_INIT_SUB_QOS_MOD_PROC
          - MOD_PROC
          - PFC_PROC
          required: true
          description: 'SM流程控制参数'
          data_source: '全网规划'
          pattern: ''
          default: ''
        ACTGGSNTMOUT:
          name: '激活拒绝原因'
          type: integer
          minimum: 0
          maximum: 112
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        ACTGGSNREJ:
          name: '激活拒绝原因'
          type: integer
          minimum: 0
          maximum: 127
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        MODGGSNREJ:
          name: '修改拒绝原因值'
          type: integer
          minimum: 0
          maximum: 127
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    set_iusmproctrl_list_1:
      type: items
      properties:
        PROT:
          name: '流程类型'
          type: string
          enum:
          - ACT_PROC
          - HSS_INIT_SUB_QOS_MOD_PROC
          - MOD_PROC
          required: true
          description: 'SM流程控制参数'
          data_source: '全网规划'
          pattern: ''
          default: ''
        ACTGGSNTMOUT:
          name: '激活拒绝原因'
          type: integer
          minimum: 0
          maximum: 112
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        ACTGGSNREJ:
          name: '激活拒绝原因'
          type: integer
          minimum: 0
          maximum: 127
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        MODGGSNREJ:
          name: '修改拒绝原因值'
          type: integer
          minimum: 0
          maximum: 127
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    set_s1smproctrl_list_1:
      type: items
      properties:
        PROT:
          name: '流程类型'
          type: string
          enum:
          - ATTACH_BEARER_ACT_PROC
          - BEARER_DEACT_PROC
          - BEARER_MODIFICATION_PROC
          - BEARER_RESOURCE_ALLOCTION_PROC
          - BEARER_RESOURCE_MOD_PROC
          - DEDICATED_BEARER_ACT_PROC
          - HSS_INIT_SUB_QOS_MOD_PROC
          - PDN_CONNECTIVITY_PROC
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        PDNCONSGWREJ:
          name: 'PDN连接拒绝原因值组号(SGW拒绝)'
          type: integer
          minimum: 0
          maximum: 127
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        PDNCONSGWTMOUT:
          name: 'PDN连接拒绝原因值(SGW超时)'
          type: integer
          minimum: 0
          maximum: 112
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
  examples:
    set_gmmproctrl_list:
    - PROT: UPDATE_LOCATION
      ULRIMSIGTERR: 11
      ULRSCCPGTERR: 22
      ULRLINKERR: 17
      ULRHLRHSSTMOUT: 33
      ULRHLRHSSREJ: 0
      AIRIMSIGTERR: 14
      AIRLINKERR: 17
      AIRHLRHSSTMOUT: 17
      AIRHLRHSSREJ: 17
      ATTACHROAMRST: 13
      INTRARAUIDTYTMOUT: 9
      INTERRAUSGSNTMOUT: 17
      INTERRAUROAMRST: 0
      INTERRAUIDTYTMOUT: 0
      INTERRAUDNSFAIL: 9
      AUTHRESCHKFAIL: 9
      CHKIMEICHKFAIL: 9
      DETACHCAUSE_CLR: 7
    set_pmmproctrl_list:
    - PROT: UPDATE_LOCATION
      ULRHLRHSSTMOUT: 33
      ULRIMSIGTERR: 11
      ULRSCCPGTERR: 22
      ULRLINKERR: 17
      ULRHLRHSSREJ: 0
      AIRIMSIGTERR: 14
      AIRLINKERR: 17
      AIRHLRHSSTMOUT: 17
      AIRHLRHSSREJ: 17
      ATTACHROAMRST: 13
      INTRARAUIDTYTMOUT: 9
      INTERRAUSGSNTMOUT: 17
      INTERRAUROAMRST: 0
      INTERRAUIDTYTMOUT: 0
      INTERRAUDNSFAIL: 9
      AUTHRESCHKFAIL: 9
      CHKIMEICHKFAIL: 9
      DETACHCAUSE_CLR: 7
    set_emmproctrl_list:
    - PROT: UPDATE_LOCATION
      ULRHSSREJ: 3
      ATTACHROAMRST: 13
      AUTHRESCHKFAIL: 9
      CHKIMEICHKFAIL: 9
      ULRHSSTMOUT: 17
      ULRDMERR: 17
      AIRHSSTMOUT: 17
      AIRHSSREJ: 17
      AIRDMERR: 17
      INTERTAUROAMRST: 17
      INTERTAUDNSFAIL: 17
    add_emmproctrlimsi_list:
    - SUBRANGE: IMSI_PREFIX
      IMSIPRE: '12307'
      ULRHSSREJ: 3
    set_gbsmproctrl_list:
    - PROT: ACT_PROC
      ACTGGSNTMOUT: 0
      ACTGGSNREJ: 0
      MODGGSNREJ: 215
    set_iusmproctrl_list:
    - PROT: ACT_PROC
      ACTGGSNTMOUT: 0
      ACTGGSNREJ: 0
      MODGGSNREJ: 215
    set_s1smproctrl_list:
    - PROT: PDN_CONNECTIVITY_PROC
      PDNCONSGWREJ: 1
      PDNCONSGWTMOUT: 0
    add_causegrp_list:
    - CAUSEGRPID: 3
      CAUSEGRPNM: '4G-S6a-To-NAS'
    add_causemap_list:
    - CAUSEGRPID: 3
      CAUSERANGE: SPECIAL
      BGCAUSE: 5000
      EDCAUSE: 5100
      TCAUSE: 12
    set_gmmproctrl_list_1:
    - PROT: UPDATE_LOCATION
      ULRIMSIGTERR: 11
      ULRSCCPGTERR: 22
      ULRLINKERR: 17
      ULRHLRHSSTMOUT: 33
      ULRHLRHSSREJ: 0
      AIRIMSIGTERR: 14
      AIRLINKERR: 17
      AIRHLRHSSTMOUT: 17
      AIRHLRHSSREJ: 17
      ATTACHROAMRST: 13
      INTRARAUIDTYTMOUT: 9
      INTERRAUSGSNTMOUT: 17
      INTERRAUROAMRST: 0
      INTERRAUIDTYTMOUT: 0
      INTERRAUDNSFAIL: 9
      AUTHRESCHKFAIL: 9
      CHKIMEICHKFAIL: 9
      DETACHCAUSE_CLR: 7
    set_pmmproctrl_list_1:
    - PROT: UPDATE_LOCATION
      ULRHLRHSSTMOUT: 33
      ULRIMSIGTERR: 11
      ULRSCCPGTERR: 22
      ULRLINKERR: 17
      ULRHLRHSSREJ: 0
      AIRIMSIGTERR: 14
      AIRLINKERR: 17
      AIRHLRHSSTMOUT: 17
      AIRHLRHSSREJ: 17
      ATTACHROAMRST: 13
      INTRARAUIDTYTMOUT: 9
      INTERRAUSGSNTMOUT: 17
      INTERRAUROAMRST: 0
      INTERRAUIDTYTMOUT: 0
      INTERRAUDNSFAIL: 9
      AUTHRESCHKFAIL: 9
      CHKIMEICHKFAIL: 9
      DETACHCAUSE_CLR: 7
    set_emmproctrl_list_1:
    - PROT: UPDATE_LOCATION
      ULRHSSREJ: 3
      ATTACHROAMRST: 13
      AUTHRESCHKFAIL: 9
      CHKIMEICHKFAIL: 9
      ULRHSSTMOUT: 17
      ULRDMERR: 17
      AIRHSSTMOUT: 17
      AIRHSSREJ: 17
      AIRDMERR: 17
      INTERTAUROAMRST: 17
      INTERTAUDNSFAIL: 17
    add_emmproctrlimsi_list_1:
    - SUBRANGE: IMSI_PREFIX
      IMSIPRE: '12307'
      ULRHSSREJ: 3
    set_gbsmproctrl_list_1:
    - PROT: ACT_PROC
      ACTGGSNTMOUT: 0
      ACTGGSNREJ: 0
      MODGGSNREJ: 215
    set_iusmproctrl_list_1:
    - PROT: ACT_PROC
      ACTGGSNTMOUT: 0
      ACTGGSNREJ: 0
      MODGGSNREJ: 215
    set_s1smproctrl_list_1:
    - PROT: PDN_CONNECTIVITY_PROC
      PDNCONSGWREJ: 1
      PDNCONSGWTMOUT: 0
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 处理一：UEG直接向UE下发用户事先配置的原因值。

### 以下三种情况适用：

#### 1.1 由于UEG系统内部异常（配置/链路）导致的流程失败。

#### 1.2 由于周边网元响应消息超时。

#### 1.3 周边网元返回响应消息，但响应消息错误。

#### 1.4 设置Gb模式移动性管理流程中指定原因值的下发。

#### 进入“MML命令行-UEG”窗口。

```jinja2
{%- if is_scenario_direct_delivery -%}
    {%- for item in set_gmmproctrl_list -%}
        SET GMMPROCTRL:
        {#- --- 必选参数 --- -#}
        PROT={{item.PROT}},
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：PROT=UPDATE_LOCATION 时可选 --- -#}
        {%- if item.PROT == 'UPDATE_LOCATION' -%}
            {%- if item.ULRIMSIGTERR is not none -%}
                ULRIMSIGTERR={{item.ULRIMSIGTERR}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=UPDATE_LOCATION 时可选 --- -#}
        {%- if item.PROT == 'UPDATE_LOCATION' -%}
            {%- if item.ULRSCCPGTERR is not none -%}
                ULRSCCPGTERR={{item.ULRSCCPGTERR}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=AIR 时可选 --- -#}
        {%- if item.PROT == 'AIR' -%}
            {%- if item.AIRHLRHSSREJ is not none -%}
                AIRHLRHSSREJ={{item.AIRHLRHSSREJ}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=AIR 时可选 --- -#}
        {%- if item.PROT == 'AIR' -%}
            {%- if item.AIRHLRHSSTMOUT is not none -%}
                AIRHLRHSSTMOUT={{item.AIRHLRHSSTMOUT}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=AUTHENTICATION 时可选 --- -#}
        {%- if item.PROT == 'AUTHENTICATION' -%}
            {%- if item.AUTHRESCHKFAIL is not none -%}
                AUTHRESCHKFAIL={{item.AUTHRESCHKFAIL}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=CANCEL_LOCATION 时可选 --- -#}
        {%- if item.PROT == 'CANCEL_LOCATION' -%}
            {%- if item.DETACHCAUSE_CLR is not none -%}
                DETACHCAUSE_CLR={{item.DETACHCAUSE_CLR}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=UPDATE_LOCATION 时可选 --- -#}
        {%- if item.PROT == 'UPDATE_LOCATION' -%}
            {%- if item.ULRHLRHSSTMOUT is not none -%}
                ULRHLRHSSTMOUT={{item.ULRHLRHSSTMOUT}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=INTER_RAU 时可选 --- -#}
        {%- if item.PROT == 'INTER_RAU' -%}
            {%- if item.INTERRAUDNSFAIL is not none -%}
                INTERRAUDNSFAIL={{item.INTERRAUDNSFAIL}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=INTER_RAU 时可选 --- -#}
        {%- if item.PROT == 'INTER_RAU' -%}
            {%- if item.INTERRAUROAMRST is not none -%}
                INTERRAUROAMRST={{item.INTERRAUROAMRST}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=INTER_RAU 时可选 --- -#}
        {%- if item.PROT == 'INTER_RAU' -%}
            {%- if item.INTERRAUIDTYTMOUT is not none -%}
                INTERRAUIDTYTMOUT={{item.INTERRAUIDTYTMOUT}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=AIR 时可选 --- -#}
        {%- if item.PROT == 'AIR' -%}
            {%- if item.AIRIMSIGTERR is not none -%}
                AIRIMSIGTERR={{item.AIRIMSIGTERR}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=ATTACH 时可选 --- -#}
        {%- if item.PROT == 'ATTACH' -%}
            {%- if item.ATTACHROAMRST is not none -%}
                ATTACHROAMRST={{item.ATTACHROAMRST}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=INTRA_RAU 时可选 --- -#}
        {%- if item.PROT == 'INTRA_RAU' -%}
            {%- if item.INTRARAUIDTYTMOUT is not none -%}
                INTRARAUIDTYTMOUT={{item.INTRARAUIDTYTMOUT}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=UPDATE_LOCATION 时可选 --- -#}
        {%- if item.PROT == 'UPDATE_LOCATION' -%}
            {%- if item.ULRLINKERR is not none -%}
                ULRLINKERR={{item.ULRLINKERR}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=UPDATE_LOCATION 时可选 --- -#}
        {%- if item.PROT == 'UPDATE_LOCATION' -%}
            {%- if item.ULRHLRHSSREJ is not none -%}
                ULRHLRHSSREJ={{item.ULRHLRHSSREJ}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=AIR 时可选 --- -#}
        {%- if item.PROT == 'AIR' -%}
            {%- if item.AIRLINKERR is not none -%}
                AIRLINKERR={{item.AIRLINKERR}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=INTER_RAU 时可选 --- -#}
        {%- if item.PROT == 'INTER_RAU' -%}
            {%- if item.INTERRAUSGSNTMOUT is not none -%}
                INTERRAUSGSNTMOUT={{item.INTERRAUSGSNTMOUT}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=CHECK_IMEI 时可选 --- -#}
        {%- if item.PROT == 'CHECK_IMEI' -%}
            {%- if item.CHKIMEICHKFAIL is not none -%}
                CHKIMEICHKFAIL={{item.CHKIMEICHKFAIL}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 此命令这里列出了所有参数，但是这些参数不会同时显示，具体“流程类型”选择不同，对应的参数也不同。

#### 1.5 设置Iu模式移动性管理流程中指定原因值的下发。

```jinja2
{%- if is_scenario_direct_delivery -%}
    {%- for item in set_pmmproctrl_list -%}
        SET PMMPROCTRL:
        {#- --- 必选参数 --- -#}
        PROT={{item.PROT}},
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：PROT=UPDATE_LOCATION 时可选 --- -#}
        {%- if item.PROT == 'UPDATE_LOCATION' -%}
            {%- if item.ULRHLRHSSTMOUT is not none -%}
                ULRHLRHSSTMOUT={{item.ULRHLRHSSTMOUT}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=AIR 时可选 --- -#}
        {%- if item.PROT == 'AIR' -%}
            {%- if item.AIRHLRHSSREJ is not none -%}
                AIRHLRHSSREJ={{item.AIRHLRHSSREJ}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=AIR 时可选 --- -#}
        {%- if item.PROT == 'AIR' -%}
            {%- if item.AIRHLRHSSTMOUT is not none -%}
                AIRHLRHSSTMOUT={{item.AIRHLRHSSTMOUT}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=AUTHENTICATION 时可选 --- -#}
        {%- if item.PROT == 'AUTHENTICATION' -%}
            {%- if item.AUTHRESCHKFAIL is not none -%}
                AUTHRESCHKFAIL={{item.AUTHRESCHKFAIL}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=CANCEL_LOCATION 时可选 --- -#}
        {%- if item.PROT == 'CANCEL_LOCATION' -%}
            {%- if item.DETACHCAUSE_CLR is not none -%}
                DETACHCAUSE_CLR={{item.DETACHCAUSE_CLR}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=INTER_RAU 时可选 --- -#}
        {%- if item.PROT == 'INTER_RAU' -%}
            {%- if item.INTERRAUDNSFAIL is not none -%}
                INTERRAUDNSFAIL={{item.INTERRAUDNSFAIL}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=INTER_RAU 时可选 --- -#}
        {%- if item.PROT == 'INTER_RAU' -%}
            {%- if item.INTERRAUROAMRST is not none -%}
                INTERRAUROAMRST={{item.INTERRAUROAMRST}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=INTER_RAU 时可选 --- -#}
        {%- if item.PROT == 'INTER_RAU' -%}
            {%- if item.INTERRAUIDTYTMOUT is not none -%}
                INTERRAUIDTYTMOUT={{item.INTERRAUIDTYTMOUT}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=AIR 时可选 --- -#}
        {%- if item.PROT == 'AIR' -%}
            {%- if item.AIRIMSIGTERR is not none -%}
                AIRIMSIGTERR={{item.AIRIMSIGTERR}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=ATTACH 时可选 --- -#}
        {%- if item.PROT == 'ATTACH' -%}
            {%- if item.ATTACHROAMRST is not none -%}
                ATTACHROAMRST={{item.ATTACHROAMRST}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=INTRA_RAU 时可选 --- -#}
        {%- if item.PROT == 'INTRA_RAU' -%}
            {%- if item.INTRARAUIDTYTMOUT is not none -%}
                INTRARAUIDTYTMOUT={{item.INTRARAUIDTYTMOUT}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=UPDATE_LOCATION 时可选 --- -#}
        {%- if item.PROT == 'UPDATE_LOCATION' -%}
            {%- if item.ULRSCCPGTERR is not none -%}
                ULRSCCPGTERR={{item.ULRSCCPGTERR}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=UPDATE_LOCATION 时可选 --- -#}
        {%- if item.PROT == 'UPDATE_LOCATION' -%}
            {%- if item.ULRIMSIGTERR is not none -%}
                ULRIMSIGTERR={{item.ULRIMSIGTERR}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=UPDATE_LOCATION 时可选 --- -#}
        {%- if item.PROT == 'UPDATE_LOCATION' -%}
            {%- if item.ULRLINKERR is not none -%}
                ULRLINKERR={{item.ULRLINKERR}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=UPDATE_LOCATION 时可选 --- -#}
        {%- if item.PROT == 'UPDATE_LOCATION' -%}
            {%- if item.ULRHLRHSSREJ is not none -%}
                ULRHLRHSSREJ={{item.ULRHLRHSSREJ}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=AIR 时可选 --- -#}
        {%- if item.PROT == 'AIR' -%}
            {%- if item.AIRLINKERR is not none -%}
                AIRLINKERR={{item.AIRLINKERR}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=INTER_RAU 时可选 --- -#}
        {%- if item.PROT == 'INTER_RAU' -%}
            {%- if item.INTERRAUSGSNTMOUT is not none -%}
                INTERRAUSGSNTMOUT={{item.INTERRAUSGSNTMOUT}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=CHECK_IMEI 时可选 --- -#}
        {%- if item.PROT == 'CHECK_IMEI' -%}
            {%- if item.CHKIMEICHKFAIL is not none -%}
                CHKIMEICHKFAIL={{item.CHKIMEICHKFAIL}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 此命令这里列出了所有参数，但是这些参数不会同时显示，具体“流程类型”选择不同，对应的参数也不同。

#### 1.6 设置S1模式移动性管理流程中指定原因值的下发。

```jinja2
{%- if is_scenario_direct_delivery -%}
    {%- for item in set_emmproctrl_list -%}
        SET EMMPROCTRL:
        {#- --- 必选参数 --- -#}
        PROT={{item.PROT}},
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：PROT=UPDATE_LOCATION 时可选 --- -#}
        {%- if item.PROT == 'UPDATE_LOCATION' -%}
            {%- if item.ULRHSSREJ is not none -%}
                ULRHSSREJ={{item.ULRHSSREJ}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=AUTHENTICATION 时可选 --- -#}
        {%- if item.PROT == 'AUTHENTICATION' -%}
            {%- if item.AUTHRESCHKFAIL is not none -%}
                AUTHRESCHKFAIL={{item.AUTHRESCHKFAIL}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=AIR 时可选 --- -#}
        {%- if item.PROT == 'AIR' -%}
            {%- if item.AIRDMERR is not none -%}
                AIRDMERR={{item.AIRDMERR}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=ATTACH 时可选 --- -#}
        {%- if item.PROT == 'ATTACH' -%}
            {%- if item.ATTACHROAMRST is not none -%}
                ATTACHROAMRST={{item.ATTACHROAMRST}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=INTER_TAU 时可选 --- -#}
        {%- if item.PROT == 'INTER_TAU' -%}
            {%- if item.INTERTAUDNSFAIL is not none -%}
                INTERTAUDNSFAIL={{item.INTERTAUDNSFAIL}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=UPDATE_LOCATION 时可选 --- -#}
        {%- if item.PROT == 'UPDATE_LOCATION' -%}
            {%- if item.ULRDMERR is not none -%}
                ULRDMERR={{item.ULRDMERR}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=AIR 时可选 --- -#}
        {%- if item.PROT == 'AIR' -%}
            {%- if item.AIRHSSREJ is not none -%}
                AIRHSSREJ={{item.AIRHSSREJ}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=INTER_TAU 时可选 --- -#}
        {%- if item.PROT == 'INTER_TAU' -%}
            {%- if item.INTERTAUROAMRST is not none -%}
                INTERTAUROAMRST={{item.INTERTAUROAMRST}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=AIR 时可选 --- -#}
        {%- if item.PROT == 'AIR' -%}
            {%- if item.AIRHSSTMOUT is not none -%}
                AIRHSSTMOUT={{item.AIRHSSTMOUT}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=UPDATE_LOCATION 时可选 --- -#}
        {%- if item.PROT == 'UPDATE_LOCATION' -%}
            {%- if item.ULRHSSTMOUT is not none -%}
                ULRHSSTMOUT={{item.ULRHSSTMOUT}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=CHECK_IMEI 时可选 --- -#}
        {%- if item.PROT == 'CHECK_IMEI' -%}
            {%- if item.CHKIMEICHKFAIL is not none -%}
                CHKIMEICHKFAIL={{item.CHKIMEICHKFAIL}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_direct_delivery -%}
    {%- for item in add_emmproctrlimsi_list -%}
        ADD EMMPROCTRLIMSI:
        {#- --- 必选参数 --- -#}
        SUBRANGE={{item.SUBRANGE}},
        {#- --- 可选参数 --- -#}
        {%- if item.ULRHSSREJ is not none -%}
            ULRHSSREJ={{item.ULRHSSREJ}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：SUBRANGE=IMSI_PREFIX 时必选 --- -#}
        {%- if item.SUBRANGE == 'IMSI_PREFIX' -%}
            IMSIPRE="{{item.IMSIPRE}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 基于指定用户范围的原因值映射控制，与**SET EMMPROCTRL**命令配合使用，系统会首先匹配本命令的配置记录，若发现系统中不存在或不匹配本命令的配置记录才会匹配**SET EMMPROCTRL**命令的配置记录。

#### 此命令这里列出了所有参数，但是这些参数不会同时显示，具体“流程类型”选择不同，对应的参数也不同。

#### 1.7 设置Gb模式会话管理流程中指定原因值的下发。

```jinja2
{%- if is_scenario_direct_delivery -%}
    {%- for item in set_gbsmproctrl_list -%}
        SET GBSMPROCTRL:
        {#- --- 必选参数 --- -#}
        PROT={{item.PROT}},
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：PROT=MOD_PROC 时可选 --- -#}
        {%- if item.PROT == 'MOD_PROC' -%}
            {%- if item.MODGGSNREJ is not none -%}
                MODGGSNREJ={{item.MODGGSNREJ}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=ACT_PROC 时可选 --- -#}
        {%- if item.PROT == 'ACT_PROC' -%}
            {%- if item.ACTGGSNREJ is not none -%}
                ACTGGSNREJ={{item.ACTGGSNREJ}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=ACT_PROC 时可选 --- -#}
        {%- if item.PROT == 'ACT_PROC' -%}
            {%- if item.ACTGGSNTMOUT is not none -%}
                ACTGGSNTMOUT={{item.ACTGGSNTMOUT}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 具体“流程类型”选择不同，对应的参数也不同。此处以激活流程为例。

#### 1.8 设置Iu模式会话管理流程中指定原因值的下发。

```jinja2
{%- if is_scenario_direct_delivery -%}
    {%- for item in set_iusmproctrl_list -%}
        SET IUSMPROCTRL:
        {#- --- 必选参数 --- -#}
        PROT={{item.PROT}},
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：PROT=MOD_PROC 时可选 --- -#}
        {%- if item.PROT == 'MOD_PROC' -%}
            {%- if item.MODGGSNREJ is not none -%}
                MODGGSNREJ={{item.MODGGSNREJ}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=ACT_PROC 时可选 --- -#}
        {%- if item.PROT == 'ACT_PROC' -%}
            {%- if item.ACTGGSNREJ is not none -%}
                ACTGGSNREJ={{item.ACTGGSNREJ}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=ACT_PROC 时可选 --- -#}
        {%- if item.PROT == 'ACT_PROC' -%}
            {%- if item.ACTGGSNTMOUT is not none -%}
                ACTGGSNTMOUT={{item.ACTGGSNTMOUT}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 具体“流程类型”选择不同，对应的参数也不同。此处以激活流程为例。

#### 1.9 设置S1模式会话管理流程中指定原因值的下发。

```jinja2
{%- if is_scenario_direct_delivery -%}
    {%- for item in set_s1smproctrl_list -%}
        SET S1SMPROCTRL:
        {#- --- 必选参数 --- -#}
        PROT={{item.PROT}},
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：PROT=PDN_CONNECTIVITY_PROC 时可选 --- -#}
        {%- if item.PROT == 'PDN_CONNECTIVITY_PROC' -%}
            {%- if item.PDNCONSGWREJ is not none -%}
                PDNCONSGWREJ={{item.PDNCONSGWREJ}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=PDN_CONNECTIVITY_PROC 时可选 --- -#}
        {%- if item.PROT == 'PDN_CONNECTIVITY_PROC' -%}
            {%- if item.PDNCONSGWTMOUT is not none -%}
                PDNCONSGWTMOUT={{item.PDNCONSGWTMOUT}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 具体“流程类型”选择不同，对应的参数也不同。此处以PDN连接建立流程为例。

### 2 处理二：UEG首先根据用户事先配置的规则完成原始原因值到目标原因值的映射后，将映射后的目标原因值下发给UE。

### 当周边网元返回拒绝消息时，采用此操作。

#### 2.1 增加原因值映射组配置记录。

```jinja2
{%- if is_scenario_mapped_delivery -%}
    {%- for item in add_causegrp_list -%}
        ADD CAUSEGRP:
        {#- --- 必选参数 --- -#}
        CAUSEGRPID={{item.CAUSEGRPID}},
        {#- --- 可选参数 --- -#}
        {%- if item.CAUSEGRPNM is not none -%}
            CAUSEGRPNM="{{item.CAUSEGRPNM}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 2.2 增加原因值映射配置。

```jinja2
{%- if is_scenario_mapped_delivery -%}
    {%- for item in add_causemap_list -%}
        ADD CAUSEMAP:
        {#- --- 必选参数 --- -#}
        CAUSEGRPID={{item.CAUSEGRPID}},
        TCAUSE={{item.TCAUSE}},
        {#- --- 可选参数 --- -#}
        {%- if item.CAUSERANGE is not none -%}
            CAUSERANGE={{item.CAUSERANGE}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：CAUSERANGE=SPECIAL 时必选 --- -#}
        {%- if item.CAUSERANGE == 'SPECIAL' -%}
            BGCAUSE={{item.BGCAUSE}},
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：CAUSERANGE=SPECIAL 时可选 --- -#}
        {%- if item.CAUSERANGE == 'SPECIAL' -%}
            {%- if item.EDCAUSE is not none -%}
                EDCAUSE={{item.EDCAUSE}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 2.3 配置用户指定原因值。

##### 2.3.1 设置Gb模式移动性管理流程中指定原因值的下发。

```jinja2
{%- if is_scenario_mapped_delivery -%}
    {%- for item in set_gmmproctrl_list_1 -%}
        SET GMMPROCTRL:
        {#- --- 必选参数 --- -#}
        PROT={{item.PROT}},
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：PROT=UPDATE_LOCATION 时可选 --- -#}
        {%- if item.PROT == 'UPDATE_LOCATION' -%}
            {%- if item.ULRIMSIGTERR is not none -%}
                ULRIMSIGTERR={{item.ULRIMSIGTERR}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=UPDATE_LOCATION 时可选 --- -#}
        {%- if item.PROT == 'UPDATE_LOCATION' -%}
            {%- if item.ULRSCCPGTERR is not none -%}
                ULRSCCPGTERR={{item.ULRSCCPGTERR}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=AIR 时可选 --- -#}
        {%- if item.PROT == 'AIR' -%}
            {%- if item.AIRHLRHSSREJ is not none -%}
                AIRHLRHSSREJ={{item.AIRHLRHSSREJ}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=AIR 时可选 --- -#}
        {%- if item.PROT == 'AIR' -%}
            {%- if item.AIRHLRHSSTMOUT is not none -%}
                AIRHLRHSSTMOUT={{item.AIRHLRHSSTMOUT}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=AUTHENTICATION 时可选 --- -#}
        {%- if item.PROT == 'AUTHENTICATION' -%}
            {%- if item.AUTHRESCHKFAIL is not none -%}
                AUTHRESCHKFAIL={{item.AUTHRESCHKFAIL}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=CANCEL_LOCATION 时可选 --- -#}
        {%- if item.PROT == 'CANCEL_LOCATION' -%}
            {%- if item.DETACHCAUSE_CLR is not none -%}
                DETACHCAUSE_CLR={{item.DETACHCAUSE_CLR}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=UPDATE_LOCATION 时可选 --- -#}
        {%- if item.PROT == 'UPDATE_LOCATION' -%}
            {%- if item.ULRHLRHSSTMOUT is not none -%}
                ULRHLRHSSTMOUT={{item.ULRHLRHSSTMOUT}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=INTER_RAU 时可选 --- -#}
        {%- if item.PROT == 'INTER_RAU' -%}
            {%- if item.INTERRAUDNSFAIL is not none -%}
                INTERRAUDNSFAIL={{item.INTERRAUDNSFAIL}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=INTER_RAU 时可选 --- -#}
        {%- if item.PROT == 'INTER_RAU' -%}
            {%- if item.INTERRAUROAMRST is not none -%}
                INTERRAUROAMRST={{item.INTERRAUROAMRST}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=INTER_RAU 时可选 --- -#}
        {%- if item.PROT == 'INTER_RAU' -%}
            {%- if item.INTERRAUIDTYTMOUT is not none -%}
                INTERRAUIDTYTMOUT={{item.INTERRAUIDTYTMOUT}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=AIR 时可选 --- -#}
        {%- if item.PROT == 'AIR' -%}
            {%- if item.AIRIMSIGTERR is not none -%}
                AIRIMSIGTERR={{item.AIRIMSIGTERR}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=ATTACH 时可选 --- -#}
        {%- if item.PROT == 'ATTACH' -%}
            {%- if item.ATTACHROAMRST is not none -%}
                ATTACHROAMRST={{item.ATTACHROAMRST}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=INTRA_RAU 时可选 --- -#}
        {%- if item.PROT == 'INTRA_RAU' -%}
            {%- if item.INTRARAUIDTYTMOUT is not none -%}
                INTRARAUIDTYTMOUT={{item.INTRARAUIDTYTMOUT}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=UPDATE_LOCATION 时可选 --- -#}
        {%- if item.PROT == 'UPDATE_LOCATION' -%}
            {%- if item.ULRLINKERR is not none -%}
                ULRLINKERR={{item.ULRLINKERR}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=UPDATE_LOCATION 时可选 --- -#}
        {%- if item.PROT == 'UPDATE_LOCATION' -%}
            {%- if item.ULRHLRHSSREJ is not none -%}
                ULRHLRHSSREJ={{item.ULRHLRHSSREJ}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=AIR 时可选 --- -#}
        {%- if item.PROT == 'AIR' -%}
            {%- if item.AIRLINKERR is not none -%}
                AIRLINKERR={{item.AIRLINKERR}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=INTER_RAU 时可选 --- -#}
        {%- if item.PROT == 'INTER_RAU' -%}
            {%- if item.INTERRAUSGSNTMOUT is not none -%}
                INTERRAUSGSNTMOUT={{item.INTERRAUSGSNTMOUT}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=CHECK_IMEI 时可选 --- -#}
        {%- if item.PROT == 'CHECK_IMEI' -%}
            {%- if item.CHKIMEICHKFAIL is not none -%}
                CHKIMEICHKFAIL={{item.CHKIMEICHKFAIL}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 2.3.2 设置Iu模式移动性管理流程中指定原因值的下发。

```jinja2
{%- if is_scenario_mapped_delivery -%}
    {%- for item in set_pmmproctrl_list_1 -%}
        SET PMMPROCTRL:
        {#- --- 必选参数 --- -#}
        PROT={{item.PROT}},
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：PROT=UPDATE_LOCATION 时可选 --- -#}
        {%- if item.PROT == 'UPDATE_LOCATION' -%}
            {%- if item.ULRHLRHSSTMOUT is not none -%}
                ULRHLRHSSTMOUT={{item.ULRHLRHSSTMOUT}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=AIR 时可选 --- -#}
        {%- if item.PROT == 'AIR' -%}
            {%- if item.AIRHLRHSSREJ is not none -%}
                AIRHLRHSSREJ={{item.AIRHLRHSSREJ}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=AIR 时可选 --- -#}
        {%- if item.PROT == 'AIR' -%}
            {%- if item.AIRHLRHSSTMOUT is not none -%}
                AIRHLRHSSTMOUT={{item.AIRHLRHSSTMOUT}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=AUTHENTICATION 时可选 --- -#}
        {%- if item.PROT == 'AUTHENTICATION' -%}
            {%- if item.AUTHRESCHKFAIL is not none -%}
                AUTHRESCHKFAIL={{item.AUTHRESCHKFAIL}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=CANCEL_LOCATION 时可选 --- -#}
        {%- if item.PROT == 'CANCEL_LOCATION' -%}
            {%- if item.DETACHCAUSE_CLR is not none -%}
                DETACHCAUSE_CLR={{item.DETACHCAUSE_CLR}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=INTER_RAU 时可选 --- -#}
        {%- if item.PROT == 'INTER_RAU' -%}
            {%- if item.INTERRAUDNSFAIL is not none -%}
                INTERRAUDNSFAIL={{item.INTERRAUDNSFAIL}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=INTER_RAU 时可选 --- -#}
        {%- if item.PROT == 'INTER_RAU' -%}
            {%- if item.INTERRAUROAMRST is not none -%}
                INTERRAUROAMRST={{item.INTERRAUROAMRST}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=INTER_RAU 时可选 --- -#}
        {%- if item.PROT == 'INTER_RAU' -%}
            {%- if item.INTERRAUIDTYTMOUT is not none -%}
                INTERRAUIDTYTMOUT={{item.INTERRAUIDTYTMOUT}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=AIR 时可选 --- -#}
        {%- if item.PROT == 'AIR' -%}
            {%- if item.AIRIMSIGTERR is not none -%}
                AIRIMSIGTERR={{item.AIRIMSIGTERR}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=ATTACH 时可选 --- -#}
        {%- if item.PROT == 'ATTACH' -%}
            {%- if item.ATTACHROAMRST is not none -%}
                ATTACHROAMRST={{item.ATTACHROAMRST}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=INTRA_RAU 时可选 --- -#}
        {%- if item.PROT == 'INTRA_RAU' -%}
            {%- if item.INTRARAUIDTYTMOUT is not none -%}
                INTRARAUIDTYTMOUT={{item.INTRARAUIDTYTMOUT}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=UPDATE_LOCATION 时可选 --- -#}
        {%- if item.PROT == 'UPDATE_LOCATION' -%}
            {%- if item.ULRSCCPGTERR is not none -%}
                ULRSCCPGTERR={{item.ULRSCCPGTERR}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=UPDATE_LOCATION 时可选 --- -#}
        {%- if item.PROT == 'UPDATE_LOCATION' -%}
            {%- if item.ULRIMSIGTERR is not none -%}
                ULRIMSIGTERR={{item.ULRIMSIGTERR}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=UPDATE_LOCATION 时可选 --- -#}
        {%- if item.PROT == 'UPDATE_LOCATION' -%}
            {%- if item.ULRLINKERR is not none -%}
                ULRLINKERR={{item.ULRLINKERR}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=UPDATE_LOCATION 时可选 --- -#}
        {%- if item.PROT == 'UPDATE_LOCATION' -%}
            {%- if item.ULRHLRHSSREJ is not none -%}
                ULRHLRHSSREJ={{item.ULRHLRHSSREJ}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=AIR 时可选 --- -#}
        {%- if item.PROT == 'AIR' -%}
            {%- if item.AIRLINKERR is not none -%}
                AIRLINKERR={{item.AIRLINKERR}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=INTER_RAU 时可选 --- -#}
        {%- if item.PROT == 'INTER_RAU' -%}
            {%- if item.INTERRAUSGSNTMOUT is not none -%}
                INTERRAUSGSNTMOUT={{item.INTERRAUSGSNTMOUT}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=CHECK_IMEI 时可选 --- -#}
        {%- if item.PROT == 'CHECK_IMEI' -%}
            {%- if item.CHKIMEICHKFAIL is not none -%}
                CHKIMEICHKFAIL={{item.CHKIMEICHKFAIL}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 2.3.3 设置S1模式移动性管理流程中指定原因值的下发。

```jinja2
{%- if is_scenario_mapped_delivery -%}
    {%- for item in set_emmproctrl_list_1 -%}
        SET EMMPROCTRL:
        {#- --- 必选参数 --- -#}
        PROT={{item.PROT}},
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：PROT=UPDATE_LOCATION 时可选 --- -#}
        {%- if item.PROT == 'UPDATE_LOCATION' -%}
            {%- if item.ULRHSSREJ is not none -%}
                ULRHSSREJ={{item.ULRHSSREJ}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=AUTHENTICATION 时可选 --- -#}
        {%- if item.PROT == 'AUTHENTICATION' -%}
            {%- if item.AUTHRESCHKFAIL is not none -%}
                AUTHRESCHKFAIL={{item.AUTHRESCHKFAIL}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=AIR 时可选 --- -#}
        {%- if item.PROT == 'AIR' -%}
            {%- if item.AIRDMERR is not none -%}
                AIRDMERR={{item.AIRDMERR}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=ATTACH 时可选 --- -#}
        {%- if item.PROT == 'ATTACH' -%}
            {%- if item.ATTACHROAMRST is not none -%}
                ATTACHROAMRST={{item.ATTACHROAMRST}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=INTER_TAU 时可选 --- -#}
        {%- if item.PROT == 'INTER_TAU' -%}
            {%- if item.INTERTAUDNSFAIL is not none -%}
                INTERTAUDNSFAIL={{item.INTERTAUDNSFAIL}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=UPDATE_LOCATION 时可选 --- -#}
        {%- if item.PROT == 'UPDATE_LOCATION' -%}
            {%- if item.ULRDMERR is not none -%}
                ULRDMERR={{item.ULRDMERR}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=AIR 时可选 --- -#}
        {%- if item.PROT == 'AIR' -%}
            {%- if item.AIRHSSREJ is not none -%}
                AIRHSSREJ={{item.AIRHSSREJ}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=INTER_TAU 时可选 --- -#}
        {%- if item.PROT == 'INTER_TAU' -%}
            {%- if item.INTERTAUROAMRST is not none -%}
                INTERTAUROAMRST={{item.INTERTAUROAMRST}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=AIR 时可选 --- -#}
        {%- if item.PROT == 'AIR' -%}
            {%- if item.AIRHSSTMOUT is not none -%}
                AIRHSSTMOUT={{item.AIRHSSTMOUT}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=UPDATE_LOCATION 时可选 --- -#}
        {%- if item.PROT == 'UPDATE_LOCATION' -%}
            {%- if item.ULRHSSTMOUT is not none -%}
                ULRHSSTMOUT={{item.ULRHSSTMOUT}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=CHECK_IMEI 时可选 --- -#}
        {%- if item.PROT == 'CHECK_IMEI' -%}
            {%- if item.CHKIMEICHKFAIL is not none -%}
                CHKIMEICHKFAIL={{item.CHKIMEICHKFAIL}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_mapped_delivery -%}
    {%- for item in add_emmproctrlimsi_list_1 -%}
        ADD EMMPROCTRLIMSI:
        {#- --- 必选参数 --- -#}
        SUBRANGE={{item.SUBRANGE}},
        {#- --- 可选参数 --- -#}
        {%- if item.ULRHSSREJ is not none -%}
            ULRHSSREJ={{item.ULRHSSREJ}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：SUBRANGE=IMSI_PREFIX 时必选 --- -#}
        {%- if item.SUBRANGE == 'IMSI_PREFIX' -%}
            IMSIPRE="{{item.IMSIPRE}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 基于指定用户范围的原因值映射控制，与**SET EMMPROCTRL**命令配合使用，系统会首先匹配本命令的配置记录，若发现系统中不存在或不匹配本命令的配置记录才会匹配**SET EMMPROCTRL**命令的配置记录。

##### 2.3.4 设置Gb模式会话管理流程中指定原因值的下发。

```jinja2
{%- if is_scenario_mapped_delivery -%}
    {%- for item in set_gbsmproctrl_list_1 -%}
        SET GBSMPROCTRL:
        {#- --- 必选参数 --- -#}
        PROT={{item.PROT}},
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：PROT=MOD_PROC 时可选 --- -#}
        {%- if item.PROT == 'MOD_PROC' -%}
            {%- if item.MODGGSNREJ is not none -%}
                MODGGSNREJ={{item.MODGGSNREJ}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=ACT_PROC 时可选 --- -#}
        {%- if item.PROT == 'ACT_PROC' -%}
            {%- if item.ACTGGSNREJ is not none -%}
                ACTGGSNREJ={{item.ACTGGSNREJ}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=ACT_PROC 时可选 --- -#}
        {%- if item.PROT == 'ACT_PROC' -%}
            {%- if item.ACTGGSNTMOUT is not none -%}
                ACTGGSNTMOUT={{item.ACTGGSNTMOUT}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 具体“流程类型”选择不同，对应的参数也不同。此处以激活流程为例。

##### 2.3.5 设置Iu模式会话管理流程中指定原因值的下发。

```jinja2
{%- if is_scenario_mapped_delivery -%}
    {%- for item in set_iusmproctrl_list_1 -%}
        SET IUSMPROCTRL:
        {#- --- 必选参数 --- -#}
        PROT={{item.PROT}},
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：PROT=MOD_PROC 时可选 --- -#}
        {%- if item.PROT == 'MOD_PROC' -%}
            {%- if item.MODGGSNREJ is not none -%}
                MODGGSNREJ={{item.MODGGSNREJ}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=ACT_PROC 时可选 --- -#}
        {%- if item.PROT == 'ACT_PROC' -%}
            {%- if item.ACTGGSNREJ is not none -%}
                ACTGGSNREJ={{item.ACTGGSNREJ}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=ACT_PROC 时可选 --- -#}
        {%- if item.PROT == 'ACT_PROC' -%}
            {%- if item.ACTGGSNTMOUT is not none -%}
                ACTGGSNTMOUT={{item.ACTGGSNTMOUT}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 具体“流程类型”选择不同，对应的参数也不同。此处以激活流程为例。

##### 2.3.6 设置S1模式会话管理流程中指定原因值的下发。

```jinja2
{%- if is_scenario_mapped_delivery -%}
    {%- for item in set_s1smproctrl_list_1 -%}
        SET S1SMPROCTRL:
        {#- --- 必选参数 --- -#}
        PROT={{item.PROT}},
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：PROT=PDN_CONNECTIVITY_PROC 时可选 --- -#}
        {%- if item.PROT == 'PDN_CONNECTIVITY_PROC' -%}
            {%- if item.PDNCONSGWREJ is not none -%}
                PDNCONSGWREJ={{item.PDNCONSGWREJ}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=PDN_CONNECTIVITY_PROC 时可选 --- -#}
        {%- if item.PROT == 'PDN_CONNECTIVITY_PROC' -%}
            {%- if item.PDNCONSGWTMOUT is not none -%}
                PDNCONSGWTMOUT={{item.PDNCONSGWTMOUT}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 具体“流程类型”选择不同，对应的参数也不同。此处以PDN连接建立流程为例。


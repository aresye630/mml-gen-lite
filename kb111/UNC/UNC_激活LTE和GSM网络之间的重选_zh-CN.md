---
id: ''
name: 激活LTE和GSM网络之间的重选
ne_type: UNC
type: feature
description: 本操作指导介绍在运行网络中激活LTE和GSM网络之间的重选特性的操作过程。  * LTE到GSM的网络重选    UE移动出LTE和GSM的重叠覆盖区进入单GSM的覆盖区后，执行小区重选，发起RAU（路由区更新）过程，驻留到GSM小区。 * GSM到LTE的网络重选    UE从单GSM网络覆盖区移动到LTE和GSM的重叠覆盖区后，LTE具有高优先级，执行小区重选，发起TAU（跟踪区更新）过程，驻留到LTE小区。  适用于SGSN、GGSN、MME、SGW-C、PGW-C。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","互操作功能","WSFD-104502 LTE和GSM 网络之间的重选","激活LTE和GSM网络之间的重选"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本操作指导介绍在运行网络中激活LTE和GSM网络之间的重选特性的操作过程。* LTE到GSM的网络重选  UE移动出LTE和GSM的重叠覆盖区进入单GSM的覆盖区后，执行小区重选，发起RAU（路由区更新）过程，驻留到GSM小区。* GSM到LTE的网络重选  UE从单GSM网络覆盖区移动到LTE和GSM的重叠覆盖区后，LTE具有高优先级，执行小区重选，发起TAU（跟踪区更新）过程，驻留到LTE小区。适用于SGSN、GGSN、MME、SGW-C、PGW-C。

## 必备事项
前提条件

* 请仔细阅读WSFD-104502 LTE和GSM 网络之间的重选特性概述。
* 完成加载License。
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
    set_peselplcy_list:
      type: items
      properties:
        PEIDMODE:
          name: '对等网元识别模式'
          type: string
          enum:
          - DOMAIN_ROLLBACK_MODE
          - MASK_MODE
          - SECTION_MODE
          required: false
          description: '对端网元识别参数'
          data_source: '全网规划'
          pattern: ''
          default: ''
        MMEGI:
          name: 'MME Group ID'
          type: string
          maxLength: 6
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        MMEGIRANGE:
          name: 'MME Group ID范围'
          type: string
          maxLength: 6
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        RNCID:
          name: '使用RNC ID域名'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        BITMASK:
          name: '比特掩码'
          type: string
          maxLength: 6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_ipv4dnsh_list:
      type: items
      properties:
        HSINDEX:
          name: '主机名索引'
          type: integer
          minimum: 1
          maximum: 1024
          required: true
          description: 'A解析数据'
          data_source: '全网规划'
          pattern: ''
          default: ''
        HOSTNAME:
          name: '主机名'
          type: string
          maxLength: 255
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        ADDRSECTION:
          name: '地址区间号'
          type: string
          enum:
          - SECTION1
          - SECTION2
          - SECTION3
          - SECTION4
          - SECTION5
          - SECTION6
          - SECTION7
          - SECTION8
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV4ADDR1:
          name: 'IPv4地址1'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        PRIORITY1:
          name: '优先级1'
          type: integer
          minimum: 0
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 127
        WEIGHT1:
          name: '权重1'
          type: integer
          minimum: 1
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 127
        IPV4ADDR2:
          name: 'IPv4地址2'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PRIORITY2:
          name: '优先级2'
          type: integer
          minimum: 0
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 127
        WEIGHT2:
          name: '权重2'
          type: integer
          minimum: 1
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 127
    add_dnsn_list:
      type: items
      properties:
        FQDN:
          name: '域名'
          type: string
          maxLength: 255
          required: true
          description: 'NAPTR解析数据'
          data_source: '全网规划'
          pattern: ''
          default: ''
        HSINDEX:
          name: '主机名索引'
          type: integer
          minimum: 1
          maximum: 2048
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        ENTITY:
          name: '网元类型'
          type: string
          enum:
          - AMF
          - GGSN
          - IWS
          - MME
          - MSC
          - PGW
          - SGSN
          - SGW
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        INTYPE:
          name: '接口类型'
          type: string
          enum:
          - Gn
          - Gp
          - N26
          - S10
          - S102
          - S11
          - S16
          - S3
          - S4
          - S5
          - S8
          - Sdup
          - Sv
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        PRIORITY:
          name: '优先级'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: 0
        WEIGHT:
          name: '权重'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: 100
        S5PROTOCOL:
          name: 'S5接口协议类型'
          type: string
          enum:
          - GTP
          - GTP_PMIP
          - PMIP
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: GTP
        S8PROTOCOL:
          name: 'S8接口协议类型'
          type: string
          enum:
          - GTP
          - GTP_PMIP
          - PMIP
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: GTP
    set_compatibility_list:
      type: items
      properties:
        HARP:
          name: 'H值'
          type: integer
          minimum: 1
          maximum: 13
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MARP:
          name: 'M值'
          type: integer
          minimum: 2
          maximum: 14
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_r8qosmap_list:
      type: items
      properties:
        QCI:
          name: 'QoS 级别标识'
          type: integer
          minimum: 1
          maximum: 254
          required: true
          description: 'EPS QoS参数到Pre-R8 QoS参数映射规则'
          data_source: '全网规划'
          pattern: ''
          default: ''
        RBER:
          name: '保留BER'
          type: string
          enum:
          - E_RESIDUAL_BIT_ERR_RATIO_1
          - E_RESIDUAL_BIT_ERR_RATIO_2
          - E_RESIDUAL_BIT_ERR_RATIO_3
          - E_RESIDUAL_BIT_ERR_RATIO_4
          - E_RESIDUAL_BIT_ERR_RATIO_5
          - E_RESIDUAL_BIT_ERR_RATIO_6
          - E_RESIDUAL_BIT_ERR_RATIO_7
          - E_RESIDUAL_BIT_ERR_RATIO_8
          - E_RESIDUAL_BIT_ERR_RATIO_9
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TC:
          name: '流量等级'
          type: string
          enum:
          - BC
          - CC
          - IC
          - SC
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MAXSDU:
          name: '最大SDU长度'
          type: integer
          minimum: 1
          maximum: 153
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DO:
          name: '发送次序'
          type: string
          enum:
          - NORDER
          - ORDER
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DESDU:
          name: '发送错误SDU'
          type: string
          enum:
          - ERR_SDU_DELIVERED
          - ERR_SDU_NOT_DELIVERED
          - NOT_DETECT
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SDUER:
          name: 'SDU误码率'
          type: string
          enum:
          - SDUER1
          - SDUER2
          - SDUER3
          - SDUER4
          - SDUER5
          - SDUER6
          - SDUER7
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        THPRI:
          name: '发送控制优先级'
          type: string
          enum:
          - THPRI1
          - THPRI2
          - THPRI3
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TD:
          name: '传递时延'
          type: integer
          minimum: 1
          maximum: 62
          required: false
          description: ''
          data_source: ''
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
          description: 'Inter RAT的TAU流程中是否要发生Oos修改流程'
          data_source: '全网规划'
          pattern: ''
          default: ''
        ECMIDLE:
          name: 'ECM-IDLE状态立即发起修改流程'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ATTACHBEARERSGWREJ:
          name: '附着中缺省承载建立拒绝原因值组号（SGW拒绝）'
          type: integer
          minimum: 0
          maximum: 127
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ATTACHBEARERSGWTMOUT:
          name: '附着中缺省承载建立拒绝原因值（SGW超时）'
          type: integer
          minimum: 0
          maximum: 112
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        BRALSGWREJ:
          name: '承载资源分配拒绝原因值组号（SGW拒绝）'
          type: integer
          minimum: 0
          maximum: 127
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        BRALSGWTMOUT:
          name: '承载资源分配拒绝原因值（SGW超时）'
          type: integer
          minimum: 0
          maximum: 112
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        BRMSGWREJ:
          name: '承载资源修改拒绝原因值组号（SGW拒绝）'
          type: integer
          minimum: 0
          maximum: 127
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        BRMSGWTMOUT:
          name: '承载资源修改拒绝原因值（SGW超时）'
          type: integer
          minimum: 0
          maximum: 112
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CBRCONFLICTMODE:
          name: 'CBR冲突处理模式'
          type: string
          enum:
          - BUFFER
          - DISCARD
          - REJECT
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PDNCONSGWREJ:
          name: 'PDN连接拒绝原因值组号（SGW拒绝）'
          type: integer
          minimum: 0
          maximum: 127
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PDNCONSGWTMOUT:
          name: 'PDN连接拒绝原因值（SGW超时）'
          type: integer
          minimum: 0
          maximum: 112
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PDNREACT:
          name: '重新激活类型的承载删除功能'
          type: string
          enum:
          - REACT
          - REATTACH
          - REGULAR
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SUBQOSCMP:
          name: '签约QoS变更判断策略'
          type: string
          enum:
          - QOS_IN_USE
          - QOS_SUB
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        UBRCONFLICTMODE:
          name: 'UBR冲突处理模式'
          type: string
          enum:
          - BUFFER
          - DISCARD
          - REJECT
          required: false
          description: ''
          data_source: ''
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
          description: 'Inter RAT TAU流程结束后是否立即释放S1信令连接'
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
          data_source: ''
          pattern: ''
          default: ''
        AIRHSSREJ:
          name: 'AIR拒绝原因值（HSS拒绝）'
          type: integer
          minimum: 0
          maximum: 127
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AIRHSSTMOUT:
          name: 'AIR拒绝原因值（HSS超时）'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AIRNOEPSGPRS:
          name: 'AIR拒绝原因值（未知EPS签约用户，有GPRS签约数据）'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AIRNOEPSNOGPRS:
          name: 'AIR拒绝原因值（未知EPS签约用户，没有GPRS签约数据）'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AIRS6AFLOWCTRL:
          name: 'AIR拒绝原因值（S6a接口流控）'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AMFCTXREJ:
          name: 'CTX_RSP拒绝原因值映射（AMF拒绝）'
          type: integer
          minimum: 0
          maximum: 127
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AMFCTXTMOUT:
          name: 'CTX_RSP拒绝原因值（AMF超时）'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ATTACHFORCE:
          name: 'Attach强制HSS注册'
          type: string
          enum:
          - NO
          - ULR
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ATTACHHTRFC:
          name: 'Attach拒绝原因值（统一HTR流控）'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ATTACHROAMRST:
          name: 'Attach拒绝原因值（漫游受限）'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AUTHMACFAIL:
          name: 'Authentication拒绝原因值（UE返回MAC Failure）'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AUTHRESCHKFAIL:
          name: 'Authentication拒绝原因值（鉴权检查失败）'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AUTHSYNCHFAIL:
          name: 'Authentication拒绝原因值（UE返回Synch failure）'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AUTHUETMOUT:
          name: 'Authentication拒绝原因值（UE 超时）'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CHKIMEICHKFAIL:
          name: 'Check IMEI拒绝原因值（IMEI检查失败）'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        INTERTAUCONNRULE:
          name: 'Inter RAT TAU流程结束后S1连接释放策略'
          type: string
          enum:
          - IMMEDIATE_RELEASE
          - SUSPENDED_RELEASE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        INTERTAUDNSFAIL:
          name: 'Inter TAU拒绝原因值（DNS解析失败）'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        INTERTAUHTRFC:
          name: 'Inter TAU拒绝原因值（统一HTR流控）'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        INTERTAUROAMRST:
          name: 'Inter TAU拒绝原因值（漫游受限）'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MMECTXREJ:
          name: 'CTX_RSP拒绝原因值映射（MME拒绝）'
          type: integer
          minimum: 0
          maximum: 127
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MMECTXTMOUT:
          name: 'CTX_RSP拒绝原因值（MME超时）'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SGSREJ:
          name: 'LUR拒绝原因值映射（MSC拒绝）'
          type: integer
          minimum: 0
          maximum: 127
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        STOPPAGING:
          name: '寻呼失败后停止寻呼'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ULRDMERR:
          name: 'ULR拒绝原因值（Diameter链路异常）'
          type: integer
          minimum: 0
          maximum: 111
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
          default: ''
        ULRHSSTMOUT:
          name: 'ULR拒绝原因值（HSS超时）'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ULRNOEPSGPRS:
          name: 'ULR拒绝原因值（未知EPS签约用户，有GPRS签约数据）'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ULRNOEPSNOGPRS:
          name: 'ULR拒绝原因值（未知EPS签约用户，没有GPRS签约数据）'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ULRODBREJ:
          name: 'ULR拒绝原因值（ODB限制）'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ULRS6AFLOWCTRL:
          name: 'ULR拒绝原因值（S6a接口流控）'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV2AUGL02'
      SWITCH: ENABLE
    set_peselplcy_list:
    - PEIDMODE: SECTION_MODE
      MMEGI: '0x1000'
      MMEGIRANGE: '0x1088'
      RNCID: NO
      BITMASK: '0x8000'
    add_ipv4dnsh_list:
    - HSINDEX: 1
      HOSTNAME: 'RAC0000.LAC2302.MNC0000.MCC0123GPRS'
      ADDRSECTION: SECTION1
      IPV4ADDR1: '172.25.6.53'
      PRIORITY1: 1
      WEIGHT1: 50
      IPV4ADDR2: '172.25.6.54'
      PRIORITY2: 1
      WEIGHT2: 50
    add_dnsn_list:
    - FQDN: 'MMEC12.MMEGI8001.MME.EPC.MNC000.MCC123.3GPPNETWORK.ORG'
      HSINDEX: 2
      ENTITY: MME
      INTYPE: Gn
      PRIORITY: 1
      WEIGHT: 150
      S5PROTOCOL: GTP
      S8PROTOCOL: GTP
    set_compatibility_list:
    - HARP: 6
      MARP: 11
    set_r8qosmap_list:
    - QCI: 9
      RBER: E_RESIDUAL_BIT_ERR_RATIO_7
      TC: CC
      MAXSDU: 150
      DO: ORDER
      DESDU: NOT_DETECT
      SDUER: SDUER4
      THPRI: THPRI1
      TD: 10
    set_s1smproctrl_list:
    - PROT: HSS_INIT_SUB_QOS_MOD_PROC
      ECMIDLE: YES
      ATTACHBEARERSGWREJ: ''
      ATTACHBEARERSGWTMOUT: ''
      BRALSGWREJ: ''
      BRALSGWTMOUT: ''
      BRMSGWREJ: ''
      BRMSGWTMOUT: ''
      CBRCONFLICTMODE: ''
      PDNCONSGWREJ: ''
      PDNCONSGWTMOUT: ''
      PDNREACT: ''
      SUBQOSCMP: ''
      UBRCONFLICTMODE: ''
    set_emmproctrl_list:
    - PROT: INTER_TAU
      AIRDMERR: ''
      AIRHSSREJ: ''
      AIRHSSTMOUT: ''
      AIRNOEPSGPRS: ''
      AIRNOEPSNOGPRS: ''
      AIRS6AFLOWCTRL: ''
      AMFCTXREJ: ''
      AMFCTXTMOUT: ''
      ATTACHFORCE: ''
      ATTACHHTRFC: ''
      ATTACHROAMRST: ''
      AUTHMACFAIL: ''
      AUTHRESCHKFAIL: ''
      AUTHSYNCHFAIL: ''
      AUTHUETMOUT: ''
      CHKIMEICHKFAIL: ''
      INTERTAUCONNRULE: ''
      INTERTAUDNSFAIL: ''
      INTERTAUHTRFC: ''
      INTERTAUROAMRST: ''
      MMECTXREJ: ''
      MMECTXTMOUT: ''
      SGSREJ: ''
      STOPPAGING: ''
      ULRDMERR: ''
      ULRHSSREJ: ''
      ULRHSSTMOUT: ''
      ULRNOEPSGPRS: ''
      ULRNOEPSNOGPRS: ''
      ULRODBREJ: ''
      ULRS6AFLOWCTRL: ''
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 进入“MML命令行-UNC”窗口。

### 2 打开本特性的License配置开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

### 3 设置GUTI和PTMSI/RAI的识别模式，需要分别配置掩码模式、区段模式和域名回退模式下的RNC ID。

#### 3.1 **SET PESELPLCY**

```jinja2
{%- for item in set_peselplcy_list -%}
    SET PESELPLCY:
    {#- --- 可选参数 --- -#}
    {%- if item.PEIDMODE is not none -%}
        PEIDMODE={{item.PEIDMODE}},
    {%- endif -%}
    {%- if item.RNCID is not none -%}
        RNCID={{item.RNCID}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：PEIDMODE=SECTION_MODE 时必选 --- -#}
    {%- if item.PEIDMODE == 'SECTION_MODE' -%}
        MMEGI="{{item.MMEGI}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：PEIDMODE=SECTION_MODE 时可选 --- -#}
    {%- if item.PEIDMODE == 'SECTION_MODE' -%}
        {%- if item.MMEGIRANGE is not none -%}
            MMEGIRANGE="{{item.MMEGIRANGE}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：PEIDMODE=MASK_MODE 时可选 --- -#}
    {%- if item.PEIDMODE == 'MASK_MODE' -%}
        {%- if item.BITMASK is not none -%}
            BITMASK="{{item.BITMASK}}",
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 配置到DNS的数据，进行对端网元寻址。

#### 4.1 使用DNS服务器。具体配置请参见配置DNS服务器的数据。

#### 4.2 不使用DNS服务器，使用本地的DNS Hostfile。具体配置请参见配置Hostfile的数据。

```jinja2
{%- for item in add_ipv4dnsh_list -%}
    ADD IPV4DNSH:
    {#- --- 必选参数 --- -#}
    HSINDEX={{item.HSINDEX}},
    HOSTNAME="{{item.HOSTNAME}}",
    ADDRSECTION={{item.ADDRSECTION}},
    {#- --- 可选参数 --- -#}
    {%- if item.IPV4ADDR1 is not none -%}
        IPV4ADDR1="{{item.IPV4ADDR1}}",
    {%- endif -%}
    {%- if item.PRIORITY1 is not none -%}
        PRIORITY1={{item.PRIORITY1}},
    {%- endif -%}
    {%- if item.WEIGHT1 is not none -%}
        WEIGHT1={{item.WEIGHT1}},
    {%- endif -%}
    {%- if item.IPV4ADDR2 is not none -%}
        IPV4ADDR2="{{item.IPV4ADDR2}}",
    {%- endif -%}
    {%- if item.PRIORITY2 is not none -%}
        PRIORITY2={{item.PRIORITY2}},
    {%- endif -%}
    {%- if item.WEIGHT2 is not none -%}
        WEIGHT2={{item.WEIGHT2}},
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_dnsn_list -%}
    ADD DNSN:
    {#- --- 必选参数 --- -#}
    FQDN="{{item.FQDN}}",
    HSINDEX={{item.HSINDEX}},
    ENTITY={{item.ENTITY}},
    INTYPE={{item.INTYPE}},
    {#- --- 可选参数 --- -#}
    {%- if item.PRIORITY is not none -%}
        PRIORITY={{item.PRIORITY}},
    {%- endif -%}
    {%- if item.WEIGHT is not none -%}
        WEIGHT={{item.WEIGHT}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：ENTITY=SGW/PGW 时可选 --- -#}
    {%- if item.ENTITY in ['SGW', 'PGW'] -%}
        {%- if item.S5PROTOCOL is not none -%}
            S5PROTOCOL={{item.S5PROTOCOL}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：ENTITY=SGW/PGW 时可选 --- -#}
    {%- if item.ENTITY in ['SGW', 'PGW'] -%}
        {%- if item.S8PROTOCOL is not none -%}
            S8PROTOCOL={{item.S8PROTOCOL}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 5 **可选：**配置QoS参数转换规则。

#### 5.1 配置EPS QoS和GPRS QoS的ARP参数转换规则。

```jinja2
{%- if is_optional_qos_conversion_rule -%}
    {%- for item in set_compatibility_list -%}
        SET COMPATIBILITY:
        {#- --- 可选参数 --- -#}
        {%- if item.HARP is not none -%}
            HARP={{item.HARP}},
        {%- endif -%}
        {%- if item.MARP is not none -%}
            MARP={{item.MARP}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 5.2 配置EPS QoS和GPRS QoS的QCI参数转换规则。

```jinja2
{%- if is_optional_qos_conversion_rule -%}
    {%- for item in set_r8qosmap_list -%}
        SET R8QOSMAP:
        {#- --- 必选参数 --- -#}
        QCI={{item.QCI}},
        {#- --- 可选参数 --- -#}
        {%- if item.RBER is not none -%}
            RBER={{item.RBER}},
        {%- endif -%}
        {%- if item.DESDU is not none -%}
            DESDU={{item.DESDU}},
        {%- endif -%}
        {%- if item.DO is not none -%}
            DO={{item.DO}},
        {%- endif -%}
        {%- if item.MAXSDU is not none -%}
            MAXSDU={{item.MAXSDU}},
        {%- endif -%}
        {%- if item.SDUER is not none -%}
            SDUER={{item.SDUER}},
        {%- endif -%}
        {%- if item.TC is not none -%}
            TC={{item.TC}},
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：TC=CC/SC 时可选 --- -#}
        {%- if item.TC in ['CC', 'SC'] -%}
            {%- if item.TD is not none -%}
                TD={{item.TD}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：TC=IC 时可选 --- -#}
        {%- if item.TC == 'IC' -%}
            {%- if item.THPRI is not none -%}
                THPRI={{item.THPRI}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 6 **可选：**设置Inter RAT的TAU流程中是否要发生Oos修改流程。

```jinja2
{%- if is_optional_oos_modification_process -%}
    {%- for item in set_s1smproctrl_list -%}
        SET S1SMPROCTRL:
        {#- --- 必选参数 --- -#}
        PROT={{item.PROT}},
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：PROT=ATTACH_BEARER_ACT_PROC 时可选 --- -#}
        {%- if item.PROT == 'ATTACH_BEARER_ACT_PROC' -%}
            {%- if item.ATTACHBEARERSGWREJ is not none -%}
                ATTACHBEARERSGWREJ={{item.ATTACHBEARERSGWREJ}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=ATTACH_BEARER_ACT_PROC 时可选 --- -#}
        {%- if item.PROT == 'ATTACH_BEARER_ACT_PROC' -%}
            {%- if item.ATTACHBEARERSGWTMOUT is not none -%}
                ATTACHBEARERSGWTMOUT={{item.ATTACHBEARERSGWTMOUT}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=BEARER_RESOURCE_ALLOCTION_PROC 时可选 --- -#}
        {%- if item.PROT == 'BEARER_RESOURCE_ALLOCTION_PROC' -%}
            {%- if item.BRALSGWREJ is not none -%}
                BRALSGWREJ={{item.BRALSGWREJ}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=BEARER_RESOURCE_ALLOCTION_PROC 时可选 --- -#}
        {%- if item.PROT == 'BEARER_RESOURCE_ALLOCTION_PROC' -%}
            {%- if item.BRALSGWTMOUT is not none -%}
                BRALSGWTMOUT={{item.BRALSGWTMOUT}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=BEARER_RESOURCE_MOD_PROC 时可选 --- -#}
        {%- if item.PROT == 'BEARER_RESOURCE_MOD_PROC' -%}
            {%- if item.BRMSGWREJ is not none -%}
                BRMSGWREJ={{item.BRMSGWREJ}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=BEARER_RESOURCE_MOD_PROC 时可选 --- -#}
        {%- if item.PROT == 'BEARER_RESOURCE_MOD_PROC' -%}
            {%- if item.BRMSGWTMOUT is not none -%}
                BRMSGWTMOUT={{item.BRMSGWTMOUT}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=DEDICATED_BEARER_ACT_PROC 时可选 --- -#}
        {%- if item.PROT == 'DEDICATED_BEARER_ACT_PROC' -%}
            {%- if item.CBRCONFLICTMODE is not none -%}
                CBRCONFLICTMODE={{item.CBRCONFLICTMODE}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=HSS_INIT_SUB_QOS_MOD_PROC 时可选 --- -#}
        {%- if item.PROT == 'HSS_INIT_SUB_QOS_MOD_PROC' -%}
            {%- if item.ECMIDLE is not none -%}
                ECMIDLE={{item.ECMIDLE}},
            {%- endif -%}
        {%- endif -%}
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
        {#- --- 条件可选：PROT=BEARER_DEACT_PROC 时可选 --- -#}
        {%- if item.PROT == 'BEARER_DEACT_PROC' -%}
            {%- if item.PDNREACT is not none -%}
                PDNREACT={{item.PDNREACT}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=HSS_INIT_SUB_QOS_MOD_PROC 时可选 --- -#}
        {%- if item.PROT == 'HSS_INIT_SUB_QOS_MOD_PROC' -%}
            {%- if item.SUBQOSCMP is not none -%}
                SUBQOSCMP={{item.SUBQOSCMP}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=BEARER_MODIFICATION_PROC 时可选 --- -#}
        {%- if item.PROT == 'BEARER_MODIFICATION_PROC' -%}
            {%- if item.UBRCONFLICTMODE is not none -%}
                UBRCONFLICTMODE={{item.UBRCONFLICTMODE}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 7 **可选：**设置Inter RAT TAU流程结束后是否立即释放S1信令连接。

```jinja2
{%- if is_optional_release_s1_signaling_connection -%}
    {%- for item in set_emmproctrl_list -%}
        SET EMMPROCTRL:
        {#- --- 必选参数 --- -#}
        PROT={{item.PROT}},
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：PROT=AIR 时可选 --- -#}
        {%- if item.PROT == 'AIR' -%}
            {%- if item.AIRDMERR is not none -%}
                AIRDMERR={{item.AIRDMERR}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=AIR 时可选 --- -#}
        {%- if item.PROT == 'AIR' -%}
            {%- if item.AIRHSSREJ is not none -%}
                AIRHSSREJ={{item.AIRHSSREJ}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=AIR 时可选 --- -#}
        {%- if item.PROT == 'AIR' -%}
            {%- if item.AIRHSSTMOUT is not none -%}
                AIRHSSTMOUT={{item.AIRHSSTMOUT}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=AIR 时可选 --- -#}
        {%- if item.PROT == 'AIR' -%}
            {%- if item.AIRNOEPSGPRS is not none -%}
                AIRNOEPSGPRS={{item.AIRNOEPSGPRS}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=AIR 时可选 --- -#}
        {%- if item.PROT == 'AIR' -%}
            {%- if item.AIRNOEPSNOGPRS is not none -%}
                AIRNOEPSNOGPRS={{item.AIRNOEPSNOGPRS}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=AIR 时可选 --- -#}
        {%- if item.PROT == 'AIR' -%}
            {%- if item.AIRS6AFLOWCTRL is not none -%}
                AIRS6AFLOWCTRL={{item.AIRS6AFLOWCTRL}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=CONTEXT_RESPONSE 时可选 --- -#}
        {%- if item.PROT == 'CONTEXT_RESPONSE' -%}
            {%- if item.AMFCTXREJ is not none -%}
                AMFCTXREJ={{item.AMFCTXREJ}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=CONTEXT_RESPONSE 时可选 --- -#}
        {%- if item.PROT == 'CONTEXT_RESPONSE' -%}
            {%- if item.AMFCTXTMOUT is not none -%}
                AMFCTXTMOUT={{item.AMFCTXTMOUT}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=ATTACH 时可选 --- -#}
        {%- if item.PROT == 'ATTACH' -%}
            {%- if item.ATTACHFORCE is not none -%}
                ATTACHFORCE={{item.ATTACHFORCE}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=ATTACH 时可选 --- -#}
        {%- if item.PROT == 'ATTACH' -%}
            {%- if item.ATTACHHTRFC is not none -%}
                ATTACHHTRFC={{item.ATTACHHTRFC}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=ATTACH 时可选 --- -#}
        {%- if item.PROT == 'ATTACH' -%}
            {%- if item.ATTACHROAMRST is not none -%}
                ATTACHROAMRST={{item.ATTACHROAMRST}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=AUTHENTICATION 时可选 --- -#}
        {%- if item.PROT == 'AUTHENTICATION' -%}
            {%- if item.AUTHMACFAIL is not none -%}
                AUTHMACFAIL={{item.AUTHMACFAIL}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=AUTHENTICATION 时可选 --- -#}
        {%- if item.PROT == 'AUTHENTICATION' -%}
            {%- if item.AUTHRESCHKFAIL is not none -%}
                AUTHRESCHKFAIL={{item.AUTHRESCHKFAIL}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=AUTHENTICATION 时可选 --- -#}
        {%- if item.PROT == 'AUTHENTICATION' -%}
            {%- if item.AUTHSYNCHFAIL is not none -%}
                AUTHSYNCHFAIL={{item.AUTHSYNCHFAIL}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=AUTHENTICATION 时可选 --- -#}
        {%- if item.PROT == 'AUTHENTICATION' -%}
            {%- if item.AUTHUETMOUT is not none -%}
                AUTHUETMOUT={{item.AUTHUETMOUT}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=CHECK_IMEI 时可选 --- -#}
        {%- if item.PROT == 'CHECK_IMEI' -%}
            {%- if item.CHKIMEICHKFAIL is not none -%}
                CHKIMEICHKFAIL={{item.CHKIMEICHKFAIL}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=INTER_TAU 时可选 --- -#}
        {%- if item.PROT == 'INTER_TAU' -%}
            {%- if item.INTERTAUCONNRULE is not none -%}
                INTERTAUCONNRULE={{item.INTERTAUCONNRULE}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=INTER_TAU 时可选 --- -#}
        {%- if item.PROT == 'INTER_TAU' -%}
            {%- if item.INTERTAUDNSFAIL is not none -%}
                INTERTAUDNSFAIL={{item.INTERTAUDNSFAIL}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=INTER_TAU 时可选 --- -#}
        {%- if item.PROT == 'INTER_TAU' -%}
            {%- if item.INTERTAUHTRFC is not none -%}
                INTERTAUHTRFC={{item.INTERTAUHTRFC}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=INTER_TAU 时可选 --- -#}
        {%- if item.PROT == 'INTER_TAU' -%}
            {%- if item.INTERTAUROAMRST is not none -%}
                INTERTAUROAMRST={{item.INTERTAUROAMRST}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=CONTEXT_RESPONSE 时可选 --- -#}
        {%- if item.PROT == 'CONTEXT_RESPONSE' -%}
            {%- if item.MMECTXREJ is not none -%}
                MMECTXREJ={{item.MMECTXREJ}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=CONTEXT_RESPONSE 时可选 --- -#}
        {%- if item.PROT == 'CONTEXT_RESPONSE' -%}
            {%- if item.MMECTXTMOUT is not none -%}
                MMECTXTMOUT={{item.MMECTXTMOUT}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=LOCATION_UPDATE 时可选 --- -#}
        {%- if item.PROT == 'LOCATION_UPDATE' -%}
            {%- if item.SGSREJ is not none -%}
                SGSREJ={{item.SGSREJ}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=PAGING 时可选 --- -#}
        {%- if item.PROT == 'PAGING' -%}
            {%- if item.STOPPAGING is not none -%}
                STOPPAGING={{item.STOPPAGING}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=UPDATE_LOCATION 时可选 --- -#}
        {%- if item.PROT == 'UPDATE_LOCATION' -%}
            {%- if item.ULRDMERR is not none -%}
                ULRDMERR={{item.ULRDMERR}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=UPDATE_LOCATION 时可选 --- -#}
        {%- if item.PROT == 'UPDATE_LOCATION' -%}
            {%- if item.ULRHSSREJ is not none -%}
                ULRHSSREJ={{item.ULRHSSREJ}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=UPDATE_LOCATION 时可选 --- -#}
        {%- if item.PROT == 'UPDATE_LOCATION' -%}
            {%- if item.ULRHSSTMOUT is not none -%}
                ULRHSSTMOUT={{item.ULRHSSTMOUT}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=UPDATE_LOCATION 时可选 --- -#}
        {%- if item.PROT == 'UPDATE_LOCATION' -%}
            {%- if item.ULRNOEPSGPRS is not none -%}
                ULRNOEPSGPRS={{item.ULRNOEPSGPRS}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=UPDATE_LOCATION 时可选 --- -#}
        {%- if item.PROT == 'UPDATE_LOCATION' -%}
            {%- if item.ULRNOEPSNOGPRS is not none -%}
                ULRNOEPSNOGPRS={{item.ULRNOEPSNOGPRS}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=UPDATE_LOCATION 时可选 --- -#}
        {%- if item.PROT == 'UPDATE_LOCATION' -%}
            {%- if item.ULRODBREJ is not none -%}
                ULRODBREJ={{item.ULRODBREJ}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=UPDATE_LOCATION 时可选 --- -#}
        {%- if item.PROT == 'UPDATE_LOCATION' -%}
            {%- if item.ULRS6AFLOWCTRL is not none -%}
                ULRS6AFLOWCTRL={{item.ULRS6AFLOWCTRL}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```


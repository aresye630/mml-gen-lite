---
id: ''
name: 配置Radius功能（AAA灵活调整5G LAN组ID）
ne_type: UEG
type: feature
description: 企业产线部署5G LAN业务后，存在根据业务实际需要，灵活调整CPE（5G模组）/5G LAN终端（5G模组）签约的5G LAN组的需求。  产线需要灵活调整时，若仅依赖在UDM上修改5G LAN组签约数据，则存在申请周期较长等问题。故需支持灵活调整时，可基于AAA服务器调整用户所属的5G LAN组。  基于AAA服务器实现5G LAN组ID的灵活调整，依赖如下功能：  * SMF支持基于二次鉴权流程，从AAA服务器（Radius服务器）获取签约的5G LAN组ID。 * SMF支持基于APN配置以从AAA服务器（Radius服务器）获取签约的5G LAN组ID为准，不使用从UDM获取签约的5G LAN组ID。  该任务旨在指导操作人员完成SMF与AAA（Radius Server）的对接配置和功能配置。从组网上看，SMF与AAA对接支持如下两种方式：  * 直连方式：SMF与AAA直接互通，不经由UPF中转二次鉴权消息。组网示意如图1所示。    **图1** 直连方式组网示意 * 非直连方式：SMF与AAA不能直接互通，需经由UPF中转二次鉴权消息。组网示意如图2所示。    **图2** 非直连方式组网示意
tags: []
risk_level: ''
doc_source: ["原子能力&行业场景","原子能力","5GC toB 原子能力-5G LAN","特性指南","UNC特性指南","配置Radius功能（AAA灵活调整5G LAN组ID）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
企业产线部署5G LAN业务后，存在根据业务实际需要，灵活调整CPE（5G模组）/5G LAN终端（5G模组）签约的5G LAN组的需求。产线需要灵活调整时，若仅依赖在UDM上修改5G LAN组签约数据，则存在申请周期较长等问题。故需支持灵活调整时，可基于AAA服务器调整用户所属的5G LAN组。基于AAA服务器实现5G LAN组ID的灵活调整，依赖如下功能：* SMF支持基于二次鉴权流程，从AAA服务器（Radius服务器）获取签约的5G LAN组ID。* SMF支持基于APN配置以从AAA服务器（Radius服务器）获取签约的5G LAN组ID为准，不使用从UDM获取签约的5G LAN组ID。该任务旨在指导操作人员完成SMF与AAA（Radius Server）的对接配置和功能配置。从组网上看，SMF与AAA对接支持如下两种方式：* 直连方式：SMF与AAA直接互通，不经由UPF中转二次鉴权消息。组网示意如图1所示。  **图1** 直连方式组网示意* 非直连方式：SMF与AAA不能直接互通，需经由UPF中转二次鉴权消息。组网示意如图2所示。  **图2** 非直连方式组网示意

## 必备事项
前提条件

* 已完成配置SMF数据。
* 已申请并加载License控制项“LKV2SECAA01 终端二次鉴权”和“LKV2UNCCOA1 支持CoA功能”。
* 二次鉴权消息经由UPF中转时，必须先配置UPF上的相关数据，详细请参见配置终端二次鉴权（风筝S，通过AAA灵活调整5G LAN组ID）。
* 对需由AAA调整5G LAN组ID的用户，UDM上仍需初始签约5G LAN组ID。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
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
    add_l3vpninst_list:
      type: items
      properties:
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: true
          description: '非直连方式时，VPN实例名称建议与UPF上N6接口绑定的VPN实例名称相同。'
          data_source: '全局规划'
          pattern: ''
          default: ''
    add_vpninstaf_list:
      type: items
      properties:
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: true
          description: '已通过**ADD L3VPNINST**命令进行配置，可以使用**LST L3VPNINST**进行查询。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        AFTYPE:
          name: '地址族类型'
          type: string
          enum:
          - ipv4uni
          - ipv6uni
          required: true
          description: '-'
          data_source: '全局规划'
          pattern: ''
          default: ''
        VRFLABELMODE:
          name: '实例的标签分配模式'
          type: string
          enum:
          - perInstance
          - perInstanceStatic
          - perRoute
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: perRoute
    add_vpninst_list:
      type: items
      properties:
        VPNINSTANCE:
          name: 'VPN实例名'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: '-'
          data_source: '全局规划'
          pattern: ''
          default: ''
    add_logicip_list:
      type: items
      properties:
        IPVERSION:
          name: 'IP地址类型'
          type: string
          enum:
          - IPv4
          - IPv6
          required: true
          description: '与Gi逻辑接口IP相同。'
          data_source: '全局规划'
          pattern: ''
          default: ''
        LOGICIPV4:
          name: 'IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全局规划'
          pattern: ''
          default: ''
        VPNINSTNAME:
          name: 'VPN实例名称'
          type: string
          minLength: 1
          maxLength: 31
          required: false
          description: '已通过**ADD L3VPNINST**命令进行配置，可以使用**LST L3VPNINST**进行查询。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_logicinf_list:
      type: items
      properties:
        NAME:
          name: '逻辑接口名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '配置与AAA服务器对接使用的逻辑接口。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPVERSION:
          name: '逻辑接口的IP版本'
          type: string
          enum:
          - IPV4
          - IPV6
          - IPVER_ALL
          required: true
          description: ''
          data_source: '全局规划'
          pattern: ''
          default: ''
        IPV4ADDRESS1:
          name: '逻辑接口的IPv4地址1'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全局规划'
          pattern: ''
          default: ''
        IPV4MASK1:
          name: '逻辑接口的IPv4掩码1'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全局规划'
          pattern: ''
          default: ''
        VPNINSTANCE:
          name: 'VPN实例名称'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: 'AAA服务器所属的VPN实例名。已通过**ADD VPNINST**配置，可以使用**LST VPNINST**命令进行查询。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_rdssvrgrp_list:
      type: items
      properties:
        RDSSVRGRPNAME:
          name: 'Radius Server Group名称'
          type: string
          maxLength: 31
          required: true
          description: '配置Radius服务器组。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        MODE:
          name: '模式'
          type: string
          enum:
          - MASTER_SLAVE
          - ROUND_ROBIN
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: MASTER_SLAVE
        ACCTTOAUTH:
          name: '利用鉴权服务器计费'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '指定RADIUS服务器组不支持计费。'
          data_source: '本端规划'
          pattern: ''
          default: DISABLE
        SIGOPTACCTMSG:
          name: '支持可选计费消息'
          type: string
          enum:
          - DISABLE
          required: false
          description: '指定RADIUS服务器组不支持可选计费消息。'
          data_source: '本端规划'
          pattern: ''
          default: DISABLE
        ACCTTIMEOUT:
          name: 'Radius Accounting Request超时时间 (秒)'
          type: integer
          minimum: 1
          maximum: 10
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 3
        ACCTRETRANSMIT:
          name: 'Radius Accounting Request重发次数'
          type: integer
          minimum: 0
          maximum: 5
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 3
    add_rdssvr_list:
      type: items
      properties:
        RDSSVRGRPNAME:
          name: 'Radius Server Group名称'
          type: string
          maxLength: 31
          required: true
          description: '已通过**ADD RDSSVRGRP**命令进行配置，可以使用**LST RDSSVRGRP**进行查询。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        SERVERTYPE:
          name: '服务器类型'
          type: string
          enum:
          - ACCOUNTING
          - AUTHENTICATION
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPVERSION:
          name: '服务器IP版本'
          type: string
          enum:
          - IPV4
          - IPV6
          required: true
          description: '与鉴权AAA服务器的IP地址、端口号保持一致。'
          data_source: '全局规划'
          pattern: ''
          default: IPV4
        SERVERIPV4:
          name: 'IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全局规划'
          pattern: ''
          default: ''
        PORT:
          name: '端口'
          type: integer
          minimum: 1
          maximum: 65535
          required: false
          description: ''
          data_source: '与对端协商'
          pattern: ''
          default: ''
        VPNINSTANCE:
          name: 'VPN实例'
          type: string
          maxLength: 31
          required: false
          description: '已通过**ADD L3VPNINST**命令进行配置，可以使用**LST L3VPNINST**进行查询。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        CIPHERKEY:
          name: '服务器密钥（加密的）'
          type: string
          maxLength: 109
          required: true
          description: '与鉴权AAA服务器的密钥保持一致。'
          data_source: '与对端协商'
          pattern: ''
          default: ''
        CONGESTION:
          name: '小区拥塞上报开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
        PRIFLAG:
          name: '主备用类型'
          type: string
          enum:
          - CARBON_COPY
          - PRIMARY
          - SECONDARY
          required: false
          description: '-'
          data_source: '全局规划'
          pattern: ''
          default: PRIMARY
        WALVALUE:
          name: 'wal值'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CIPHERKEYCNFM:
          name: '确认服务器密钥（加密的）'
          type: string
          maxLength: 109
          required: true
          description: '-'
          data_source: '与对端协商'
          pattern: ''
          default: ''
        UDPCHECKSUMSW:
          name: 'UDP报文校验和开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '对端要求校验UDP checksum时，设置为“ENABLE”；否则设置为“DISABLE”。  此处以校验UDP checksum为例。  基于AAA灵活调整5G LAN组ID时，使用样例值。'
          data_source: '与对端协商'
          pattern: ''
          default: DISABLE
    add_radiusclientip_list:
      type: items
      properties:
        RDSSVRGRPNAME:
          name: 'Radius Server Group名称'
          type: string
          maxLength: 31
          required: true
          description: '配置Gi接口鉴权。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        AUTHORACCT:
          name: '鉴权或计费'
          type: string
          enum:
          - ACCOUNTING
          - ACCT_AND_AUTH
          - AUTHENTICATION
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ACCT_AND_AUTH
        INTFNAME:
          name: '接口名称'
          type: string
          maxLength: 13
          required: true
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_apnrdsclientip_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          maxLength: 63
          required: true
          description: '配置APN级Gi接口鉴权。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        AUTHORACCT:
          name: '鉴权或计费'
          type: string
          enum:
          - ACCOUNTING
          - ACCT_AND_AUTH
          - AUTHENTICATION
          required: true
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
        INTFNAME:
          name: '接口名称'
          type: string
          maxLength: 13
          required: true
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    set_apnauthattr_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '配置APN鉴权属性。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        ACCESSMODE:
          name: '接入模式'
          type: string
          enum:
          - TRANS_AUTH
          - TRANS_NON_AUTH
          - NON_TRANS
          - LOC_AUTH
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
        AUTHMODE:
          name: '鉴权模式'
          type: string
          enum:
          - PCO
          - APN
          - MSISDN
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
        PASSWORD:
          name: '鉴权密码'
          type: string
          minLength: 1
          maxLength: 128
          required: false
          description: ''
          data_source: '全局规划'
          pattern: ''
          default: ''
        COMMONUSERNAME:
          name: '公用用户名'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: ''
          data_source: '全局规划'
          pattern: ''
          default: ''
        COMMONUSERPASS:
          name: '公用密码'
          type: string
          minLength: 1
          maxLength: 128
          required: false
          description: ''
          data_source: '全局规划'
          pattern: ''
          default: ''
        COASWITCH:
          name: 'COA开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CFMCOMMUSERPASS:
          name: '确认公共密码'
          type: string
          minLength: 1
          maxLength: 128
          required: false
          description: ''
          data_source: '全局规划'
          pattern: ''
          default: ''
        CFMPASSWORD:
          name: '确认鉴权密码'
          type: string
          minLength: 1
          maxLength: 128
          required: false
          description: ''
          data_source: '全局规划'
          pattern: ''
          default: ''
    add_apnrdssvrgrp_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          maxLength: 63
          required: true
          description: 'APN绑定Radius服务器组。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        RDSSVRGRPNAME:
          name: 'Radius Server Group名称'
          type: string
          maxLength: 31
          required: true
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    set_rdsauthreqattr_list:
      type: items
      properties:
        RDSSVRGRPNAME:
          name: 'RADIUS服务器组名称'
          type: string
          minLength: 1
          maxLength: 31
          required: true
          description: '设置鉴权请求携带的属性，实际能力需与对端AAA服务器协商。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        ACCTSESSIONID:
          name: 'Acct-Session-Id'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '全局规划'
          pattern: ''
          default: ''
        NASID:
          name: 'NAS-ID'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '全局规划'
          pattern: ''
          default: ''
        NASIDTYPE:
          name: 'NAS ID Type'
          type: string
          enum:
          - APN
          - SPECIFIC_VALUE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IMSI:
          name: 'IMSI'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CHARGINGID:
          name: 'Charging-ID'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PREPAIDIND:
          name: 'Prepaid-ind'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GGSNIP:
          name: 'GGSN-IP'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SGSNIP:
          name: 'SGSN (S-GW)-IP'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        REQUESTAPN:
          name: 'Requested-APN'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GGSNVENDOR:
          name: 'GGSN-Vendor'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GGSNVERION:
          name: 'GGSN-Version'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RQAUTHTICATOR:
          name: 'Request Authenticator'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ACCTMULSESSID:
          name: 'Acct-Multi-Session-Id'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        EVENTTIME:
          name: 'Event-Timestamp'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NASPORTIDSW:
          name: 'NAS-Port-Id属性开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NASPORTID:
          name: 'NAS-Port-Id属性值'
          type: string
          minLength: 1
          maxLength: 16
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        WLANADDR:
          name: 'UE-Local-IP-Address和UE-UDP-Port'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_rdsauthreqvsa_list:
      type: items
      properties:
        RDSSVRGRPNAME:
          name: 'RADIUS服务器组名称'
          type: string
          minLength: 1
          maxLength: 31
          required: true
          description: '配置鉴权请求携带的私有扩展属性，实际能力需与对端AAA服务器协商。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        THREEGPP:
          name: '3GPP私有扩展属性开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '全局规划'
          pattern: ''
          default: ''
        IMSI:
          name: '3GPP-IMSI'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '全局规划'
          pattern: ''
          default: ''
        CHARGINGID:
          name: '3GPP-Charging-ID'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PDPTYPE:
          name: '3GPP-PDP-Type'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CGADDRESS:
          name: '3GPP-CG-Address'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NEGOTIAEDQOS:
          name: '3GPP-GPRS-Negotiated-QoS-Profile'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SGSNSGWADDRESS:
          name: '3GPP-SGSN(SGW)-Address'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GGSNADDRESS:
          name: '3GPP-GGSN-Address'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IMSIMCCMNC:
          name: '3GPP-IMSI-MCC-MNC'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GGSNMCCMNC:
          name: '3GPP-GGSN-MCC-MNC'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NSAPI:
          name: '3GPP-NSAPI'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SELECTIONMODE:
          name: '3GPP-Selection-Mode'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CHARGINGCHAR:
          name: '3GPP-Charging-Characteristics'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SGSNSGWMCCMNC:
          name: '3GPP-SGSN(SGW)-MCC-MNC'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IMEISV:
          name: '3GPP-IMEISV'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RATTYPE:
          name: '3GPP-RAT-Type'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ULI:
          name: '3GPP-User-Location-Info'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MSTIMEZONE:
          name: '3GPP-MS-TimeZone'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NEGOTIAEDDSCP:
          name: '3GPP-Negotiated-DSCP'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SGSNIPV6ADDRESS:
          name: '3GPP-SGSN-IPv6-Address'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GGSNIPV6ADDRESS:
          name: '3GPP-GGSN-IPv6-Address'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CGIPV6ADDRESS:
          name: '3GPP-CG-IPv6-Address'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_apnradiusattr_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '配置Radius的域名相关配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        DOMAINNAMEACT:
          name: '增加或剥离域名'
          type: string
          enum:
          - ADD_DISABLE_STRIP_DISABLE
          - ADD_ENABLE_STRIP_DISABLE
          - ADD_DISABLE_STRIP_ENABLE
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
        DOMAINNAMEPOS:
          name: '域名位置'
          type: string
          enum:
          - 'NULL'
          - PREFIX
          - SUFFIX
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
    add_apnsmcomfunc_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '从Radius服务器获取签约的5G LAN组ID时，设置为样例值。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        GETPOLICYFIRST:
          name: '在EPS是否先获取策略'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
        VNGRPIDSRC:
          name: 'VnGroupID来源'
          type: string
          enum:
          - UDM
          - Radius
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: UDM
    add_nglangrpsub_list:
      type: items
      properties:
        GROUPID:
          name: '5G LAN组ID'
          type: string
          minLength: 18
          maxLength: 37
          required: true
          description: '此处配置的是允许AAA服务器（Radius服务器）调整的5G LAN终端的5G LAN组ID白名单。  SMF从AAA服务器（Radius服务器）获取的5G LAN组ID，必须在该白名单中，否则调整失败。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        DNN:
          name: 'DNN'
          type: string
          minLength: 1
          maxLength: 31
          required: true
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_cpgtpuaddr_list:
      type: items
      properties:
        IPVERSION:
          name: 'IP地址类型'
          type: string
          enum:
          - IPV4
          - IPV6
          required: true
          description: '此处以IPv4为例。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPV4ADDR:
          name: 'IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: '用于指定与UPF对接的本端GTP-U IPv4地址。  复用SMF N4接口信令IP及VPN。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        VPN:
          name: 'VPN名称'
          type: string
          minLength: 1
          maxLength: 31
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: '_public_'
    add_uplist4rds_list:
      type: items
      properties:
        UPLISTNAME:
          name: 'UP列表名称'
          type: string
          maxLength: 63
          required: true
          description: 'UP列表名称，用于指定UP列表名称。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        UPINSTANCEID:
          name: 'UP实例标识'
          type: string
          maxLength: 36
          required: true
          description: 'UP实例标识。可执行**LST PNFPROFILE**命令查询，“NF类型”为“NfUPF”。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_rdsupfctrl_list:
      type: items
      properties:
        UPLISTNAME:
          name: 'UP列表名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '同一UP列表中，存在多个中转UPF时需要规划。  采用**ADD UPLIST4RDS**命令中的对应参数。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        UPINSTANCEID:
          name: 'UPF实例标识'
          type: string
          minLength: 1
          maxLength: 36
          required: true
          description: ''
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        PREFERENCE:
          name: '优先级'
          type: integer
          minimum: 0
          maximum: 255
          required: true
          description: '值越大优先级越高。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        LOCKED:
          name: '锁定'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: true
          description: '* SMF需要选择该UPF创建UPF中转RADIUS会话时，设置为“DISABLE”。 * SMF不选择该UPF创建中转RADIUS会话时，例如故障场景，设置为“ENABLE”。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_upfrdssvr_list:
      type: items
      properties:
        SERVERTYPE:
          name: '服务器类型'
          type: string
          enum:
          - AUTHENTICATION
          - ACCOUNTING
          required: true
          description: '使用样例值。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPVERSION:
          name: '服务器IP版本'
          type: string
          enum:
          - IPV4
          - IPV6
          required: true
          description: 'DN-AAA的IP地址。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SERVERIPV4:
          name: 'IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        UPLISTNAME:
          name: 'UP列表名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '可执行**LST UPLIST4RDS**命令查询。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_upfrdsclientip_list:
      type: items
      properties:
        CLIENTYPE:
          name: '客户端类型'
          type: string
          enum:
          - AUTHENTICATION
          - ACCOUNTING
          - ACCT_AND_AUTH
          required: true
          description: '使用样例值。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPVERSION:
          name: '客户端IP版本'
          type: string
          enum:
          - IPV4
          - IPV6
          required: true
          description: 'SMF Gi接口的IP地址。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        CLIENTIPV4:
          name: 'CLIENTIPV4'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        UPLISTNAME:
          name: 'UP列表名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '可执行**LST UPLIST4RDS**命令查询。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        VPNINSTANCE:
          name: 'VPNINSTANCE'
          type: string
          minLength: 1
          maxLength: 31
          required: false
          description: '指定VPN实例。本参数由UPF和DN-AAA共同规划，是UPF与DN-AAA对接的VPN。'
          data_source: '本端规划'
          pattern: ''
          default: ''
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV2UNCCOA1'
      SWITCH: ENABLE
    add_l3vpninst_list:
    - VRFNAME: 'VRF_AAA'
    add_vpninstaf_list:
    - VRFNAME: 'VRF_AAA'
      AFTYPE: ipv4uni
      VRFLABELMODE: perRoute
    add_vpninst_list:
    - VPNINSTANCE: 'VRF_AAA'
    add_logicip_list:
    - IPVERSION: IPv4
      LOGICIPV4: '10.8.20.1'
      VPNINSTNAME: 'VRF_AAA'
    add_logicinf_list:
    - NAME: 'giif1/0/0'
      IPVERSION: IPV4
      IPV4ADDRESS1: '10.8.20.1'
      IPV4MASK1: '255.255.255.255'
      VPNINSTANCE: 'VRF_AAA'
    add_rdssvrgrp_list:
    - RDSSVRGRPNAME: 'radius_001'
      MODE: MASTER_SLAVE
      ACCTTOAUTH: DISABLE
      SIGOPTACCTMSG: DISABLE
      ACCTTIMEOUT: 10
      ACCTRETRANSMIT: 5
    add_rdssvr_list:
    - RDSSVRGRPNAME: 'radius_001'
      SERVERTYPE: AUTHENTICATION
      IPVERSION: IPV4
      SERVERIPV4: '10.168.10.1'
      PORT: 1812
      VPNINSTANCE: 'VRF_AAA'
      CIPHERKEY: '*****'
      CONGESTION: DISABLE
      PRIFLAG: PRIMARY
      WALVALUE: 0
      CIPHERKEYCNFM: '*****'
      UDPCHECKSUMSW: ENABLE
    add_radiusclientip_list:
    - RDSSVRGRPNAME: 'radius_001'
      AUTHORACCT: AUTHENTICATION
      INTFNAME: 'giif1/0/0'
    add_apnrdsclientip_list:
    - APN: 'dnn5glan01'
      AUTHORACCT: AUTHENTICATION
      INTFNAME: 'giif1/0/0'
    set_apnauthattr_list:
    - APN: 'dnn5glan01'
      ACCESSMODE: NON_TRANS
      AUTHMODE: MSISDN
      PASSWORD: '*****'
      COMMONUSERNAME: 'admin'
      COMMONUSERPASS: '*****'
      COASWITCH: ENABLE
      CFMCOMMUSERPASS: '*****'
      CFMPASSWORD: '*****'
    add_apnrdssvrgrp_list:
    - APN: 'dnn5glan01'
      RDSSVRGRPNAME: 'radius_001'
    set_rdsauthreqattr_list:
    - RDSSVRGRPNAME: 'radius_001'
      ACCTSESSIONID: ENABLE
      NASID: ENABLE
      NASIDTYPE: APN
      IMSI: DISABLE
      CHARGINGID: DISABLE
      PREPAIDIND: DISABLE
      GGSNIP: ENABLE
      SGSNIP: ENABLE
      REQUESTAPN: DISABLE
      GGSNVENDOR: ENABLE
      GGSNVERION: ENABLE
      RQAUTHTICATOR: DISABLE
      ACCTMULSESSID: ENABLE
      EVENTTIME: ENABLE
      NASPORTIDSW: ENABLE
      NASPORTID: 'UNC'
      WLANADDR: DISABLE
    set_rdsauthreqvsa_list:
    - RDSSVRGRPNAME: 'radius_001'
      THREEGPP: ENABLE
      IMSI: ENABLE
      CHARGINGID: ENABLE
      PDPTYPE: ENABLE
      CGADDRESS: ENABLE
      NEGOTIAEDQOS: ENABLE
      SGSNSGWADDRESS: ENABLE
      GGSNADDRESS: ENABLE
      IMSIMCCMNC: ENABLE
      GGSNMCCMNC: ENABLE
      NSAPI: ENABLE
      SELECTIONMODE: ENABLE
      CHARGINGCHAR: ENABLE
      SGSNSGWMCCMNC: ENABLE
      IMEISV: ENABLE
      RATTYPE: ENABLE
      ULI: ENABLE
      MSTIMEZONE: ENABLE
      NEGOTIAEDDSCP: ENABLE
      SGSNIPV6ADDRESS: ENABLE
      GGSNIPV6ADDRESS: ENABLE
      CGIPV6ADDRESS: ENABLE
    set_apnradiusattr_list:
    - APN: 'dnn5glan01'
      DOMAINNAMEACT: ADD_ENABLE_STRIP_DISABLE
      DOMAINNAMEPOS: SUFFIX
    add_apnsmcomfunc_list:
    - APN: 'dnn5glan01'
      GETPOLICYFIRST: DISABLE
      VNGRPIDSRC: Radius
    add_nglangrpsub_list:
    - GROUPID: '000003e9-460-08-01'
      DNN: 'dnn5glan01'
    add_cpgtpuaddr_list:
    - IPVERSION: IPV4
      IPV4ADDR: '192.168.0.20'
      VPN: 'VRF_CN'
    add_uplist4rds_list:
    - UPLISTNAME: 'uplist1'
      UPINSTANCEID: 'upf_instance_1'
    add_rdsupfctrl_list:
    - UPLISTNAME: 'uplist1'
      UPINSTANCEID: 'upf_instance_1'
      PREFERENCE: 100
      LOCKED: DISABLE
    add_upfrdssvr_list:
    - SERVERTYPE: AUTHENTICATION
      IPVERSION: IPV4
      SERVERIPV4: '10.168.10.1'
      UPLISTNAME: 'uplist1'
    add_upfrdsclientip_list:
    - CLIENTYPE: AUTHENTICATION
      IPVERSION: IPV4
      CLIENTIPV4: '10.8.20.1'
      UPLISTNAME: 'uplist1'
      VPNINSTANCE: 'VRF_LocalDN'
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 **//****公共数据：任务示例一和任务示例二均需要的配置。**

#### 1.1 //打开License开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

#### 1.2 //创建L3VPN实例。

```jinja2
{%- for item in add_l3vpninst_list -%}
    ADD L3VPNINST:
    {#- --- 必选参数 --- -#}
    VRFNAME="{{item.VRFNAME}}",
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_vpninstaf_list -%}
    ADD VPNINSTAF:
    {#- --- 必选参数 --- -#}
    VRFNAME="{{item.VRFNAME}}",
    AFTYPE={{item.AFTYPE}},
    {#- --- 可选参数 --- -#}
    {%- if item.VRFLABELMODE is not none -%}
        VRFLABELMODE={{item.VRFLABELMODE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 1.3 //创建VPN实例。

```jinja2
{%- for item in add_vpninst_list -%}
    ADD VPNINST:
    {#- --- 必选参数 --- -#}
    VPNINSTANCE="{{item.VPNINSTANCE}}",
    ;
{%- endfor -%}
```

#### 1.4 //配置Gi接口。

```jinja2
{%- for item in add_logicip_list -%}
    ADD LOGICIP:
    {#- --- 必选参数 --- -#}
    IPVERSION={{item.IPVERSION}},
    {#- --- 可选参数 --- -#}
    {%- if item.VPNINSTNAME is not none -%}
        VPNINSTNAME="{{item.VPNINSTNAME}}",
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPVERSION=IPv4 时必选 --- -#}
    {%- if item.IPVERSION == 'IPv4' -%}
        LOGICIPV4="{{item.LOGICIPV4}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_logicinf_list -%}
    ADD LOGICINF:
    {#- --- 必选参数 --- -#}
    NAME="{{item.NAME}}",
    IPVERSION={{item.IPVERSION}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPVERSION=IPV4/IPVER_ALL 时必选 --- -#}
    {%- if item.IPVERSION in ['IPV4', 'IPVER_ALL'] -%}
        IPV4ADDRESS1="{{item.IPV4ADDRESS1}}",
    {%- endif -%}
    {#- --- 条件必选：IPVERSION=IPV4/IPVER_ALL 时必选 --- -#}
    {%- if item.IPVERSION in ['IPV4', 'IPVER_ALL'] -%}
        IPV4MASK1="{{item.IPV4MASK1}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：IPVERSION=IPV4/IPVER_ALL/IPV6 时可选 --- -#}
    {%- if item.IPVERSION in ['IPV4', 'IPVER_ALL', 'IPV6'] -%}
        {%- if item.VPNINSTANCE is not none -%}
            VPNINSTANCE="{{item.VPNINSTANCE}}",
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 1.5 //配置Radius服务器组和Radius服务器。

```jinja2
{%- for item in add_rdssvrgrp_list -%}
    ADD RDSSVRGRP:
    {#- --- 必选参数 --- -#}
    RDSSVRGRPNAME="{{item.RDSSVRGRPNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.MODE is not none -%}
        MODE={{item.MODE}},
    {%- endif -%}
    {%- if item.ACCTTOAUTH is not none -%}
        ACCTTOAUTH={{item.ACCTTOAUTH}},
    {%- endif -%}
    {%- if item.SIGOPTACCTMSG is not none -%}
        SIGOPTACCTMSG={{item.SIGOPTACCTMSG}},
    {%- endif -%}
    {%- if item.ACCTTIMEOUT is not none -%}
        ACCTTIMEOUT={{item.ACCTTIMEOUT}},
    {%- endif -%}
    {%- if item.ACCTRETRANSMIT is not none -%}
        ACCTRETRANSMIT={{item.ACCTRETRANSMIT}},
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_rdssvr_list -%}
    ADD RDSSVR:
    {#- --- 必选参数 --- -#}
    RDSSVRGRPNAME="{{item.RDSSVRGRPNAME}}",
    SERVERTYPE={{item.SERVERTYPE}},
    IPVERSION={{item.IPVERSION}},
    CIPHERKEY="{{item.CIPHERKEY}}",
    CIPHERKEYCNFM="{{item.CIPHERKEYCNFM}}",
    {#- --- 可选参数 --- -#}
    {%- if item.PORT is not none -%}
        PORT={{item.PORT}},
    {%- endif -%}
    {%- if item.VPNINSTANCE is not none -%}
        VPNINSTANCE="{{item.VPNINSTANCE}}",
    {%- endif -%}
    {%- if item.CONGESTION is not none -%}
        CONGESTION={{item.CONGESTION}},
    {%- endif -%}
    {%- if item.PRIFLAG is not none -%}
        PRIFLAG={{item.PRIFLAG}},
    {%- endif -%}
    {%- if item.WALVALUE is not none -%}
        WALVALUE={{item.WALVALUE}},
    {%- endif -%}
    {%- if item.UDPCHECKSUMSW is not none -%}
        UDPCHECKSUMSW={{item.UDPCHECKSUMSW}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPVERSION=IPV4 时必选 --- -#}
    {%- if item.IPVERSION == 'IPV4' -%}
        SERVERIPV4="{{item.SERVERIPV4}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 1.6 //配置Gi接口鉴权。

```jinja2
{%- for item in add_radiusclientip_list -%}
    ADD RADIUSCLIENTIP:
    {#- --- 必选参数 --- -#}
    RDSSVRGRPNAME="{{item.RDSSVRGRPNAME}}",
    INTFNAME="{{item.INTFNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.AUTHORACCT is not none -%}
        AUTHORACCT={{item.AUTHORACCT}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 1.7 //配置APN级Gi接口鉴权。

```jinja2
{%- for item in add_apnrdsclientip_list -%}
    ADD APNRDSCLIENTIP:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    AUTHORACCT={{item.AUTHORACCT}},
    INTFNAME="{{item.INTFNAME}}",
    ;
{%- endfor -%}
```

#### 1.8 //配置access request消息鉴权属性。

```jinja2
{%- for item in set_apnauthattr_list -%}
    SET APNAUTHATTR:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    {#- --- 可选参数 --- -#}
    {%- if item.ACCESSMODE is not none -%}
        ACCESSMODE={{item.ACCESSMODE}},
    {%- endif -%}
    {%- if item.COMMONUSERNAME is not none -%}
        COMMONUSERNAME="{{item.COMMONUSERNAME}}",
    {%- endif -%}
    {%- if item.COMMONUSERPASS is not none -%}
        COMMONUSERPASS="{{item.COMMONUSERPASS}}",
    {%- endif -%}
    {%- if item.COASWITCH is not none -%}
        COASWITCH={{item.COASWITCH}},
    {%- endif -%}
    {%- if item.CFMCOMMUSERPASS is not none -%}
        CFMCOMMUSERPASS="{{item.CFMCOMMUSERPASS}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：ACCESSMODE=NON_TRANS 时可选 --- -#}
    {%- if item.ACCESSMODE == 'NON_TRANS' -%}
        {%- if item.AUTHMODE is not none -%}
            AUTHMODE={{item.AUTHMODE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：AUTHMODE=APN/MSISDN 时可选 --- -#}
    {%- if item.AUTHMODE in ['APN', 'MSISDN'] -%}
        {%- if item.PASSWORD is not none -%}
            PASSWORD="{{item.PASSWORD}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：AUTHMODE=APN/MSISDN 时可选 --- -#}
    {%- if item.AUTHMODE in ['APN', 'MSISDN'] -%}
        {%- if item.CFMPASSWORD is not none -%}
            CFMPASSWORD="{{item.CFMPASSWORD}}",
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 1.9 //配置APN绑定Radius服务器组。

```jinja2
{%- for item in add_apnrdssvrgrp_list -%}
    ADD APNRDSSVRGRP:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    RDSSVRGRPNAME="{{item.RDSSVRGRPNAME}}",
    ;
{%- endfor -%}
```

#### 1.10 //配置鉴权请求携带的属性。脚本仅为示例，实际能力需与对端AAA服务器协商。

```jinja2
{%- for item in set_rdsauthreqattr_list -%}
    SET RDSAUTHREQATTR:
    {#- --- 必选参数 --- -#}
    RDSSVRGRPNAME="{{item.RDSSVRGRPNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.ACCTSESSIONID is not none -%}
        ACCTSESSIONID={{item.ACCTSESSIONID}},
    {%- endif -%}
    {%- if item.NASID is not none -%}
        NASID={{item.NASID}},
    {%- endif -%}
    {%- if item.IMSI is not none -%}
        IMSI={{item.IMSI}},
    {%- endif -%}
    {%- if item.CHARGINGID is not none -%}
        CHARGINGID={{item.CHARGINGID}},
    {%- endif -%}
    {%- if item.PREPAIDIND is not none -%}
        PREPAIDIND={{item.PREPAIDIND}},
    {%- endif -%}
    {%- if item.GGSNIP is not none -%}
        GGSNIP={{item.GGSNIP}},
    {%- endif -%}
    {%- if item.SGSNIP is not none -%}
        SGSNIP={{item.SGSNIP}},
    {%- endif -%}
    {%- if item.REQUESTAPN is not none -%}
        REQUESTAPN={{item.REQUESTAPN}},
    {%- endif -%}
    {%- if item.GGSNVENDOR is not none -%}
        GGSNVENDOR={{item.GGSNVENDOR}},
    {%- endif -%}
    {%- if item.GGSNVERION is not none -%}
        GGSNVERION={{item.GGSNVERION}},
    {%- endif -%}
    {%- if item.RQAUTHTICATOR is not none -%}
        RQAUTHTICATOR={{item.RQAUTHTICATOR}},
    {%- endif -%}
    {%- if item.ACCTMULSESSID is not none -%}
        ACCTMULSESSID={{item.ACCTMULSESSID}},
    {%- endif -%}
    {%- if item.EVENTTIME is not none -%}
        EVENTTIME={{item.EVENTTIME}},
    {%- endif -%}
    {%- if item.NASPORTIDSW is not none -%}
        NASPORTIDSW={{item.NASPORTIDSW}},
    {%- endif -%}
    {%- if item.WLANADDR is not none -%}
        WLANADDR={{item.WLANADDR}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：NASID=ENABLE 时必选 --- -#}
    {%- if item.NASID == 'ENABLE' -%}
        NASIDTYPE={{item.NASIDTYPE}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：NASPORTIDSW=ENABLE 时可选 --- -#}
    {%- if item.NASPORTIDSW == 'ENABLE' -%}
        {%- if item.NASPORTID is not none -%}
            NASPORTID="{{item.NASPORTID}}",
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 1.11 //配置鉴权请求携带的私有扩展属性。脚本仅为示例，实际能力需与对端AAA服务器协商。

```jinja2
{%- for item in set_rdsauthreqvsa_list -%}
    SET RDSAUTHREQVSA:
    {#- --- 必选参数 --- -#}
    RDSSVRGRPNAME="{{item.RDSSVRGRPNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.THREEGPP is not none -%}
        THREEGPP={{item.THREEGPP}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：THREEGPP=ENABLE 时可选 --- -#}
    {%- if item.THREEGPP == 'ENABLE' -%}
        {%- if item.IMSI is not none -%}
            IMSI={{item.IMSI}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：THREEGPP=ENABLE 时可选 --- -#}
    {%- if item.THREEGPP == 'ENABLE' -%}
        {%- if item.CHARGINGID is not none -%}
            CHARGINGID={{item.CHARGINGID}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：THREEGPP=ENABLE 时可选 --- -#}
    {%- if item.THREEGPP == 'ENABLE' -%}
        {%- if item.PDPTYPE is not none -%}
            PDPTYPE={{item.PDPTYPE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：THREEGPP=ENABLE 时可选 --- -#}
    {%- if item.THREEGPP == 'ENABLE' -%}
        {%- if item.CGADDRESS is not none -%}
            CGADDRESS={{item.CGADDRESS}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：THREEGPP=ENABLE 时可选 --- -#}
    {%- if item.THREEGPP == 'ENABLE' -%}
        {%- if item.NEGOTIAEDQOS is not none -%}
            NEGOTIAEDQOS={{item.NEGOTIAEDQOS}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：THREEGPP=ENABLE 时可选 --- -#}
    {%- if item.THREEGPP == 'ENABLE' -%}
        {%- if item.SGSNSGWADDRESS is not none -%}
            SGSNSGWADDRESS={{item.SGSNSGWADDRESS}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：THREEGPP=ENABLE 时可选 --- -#}
    {%- if item.THREEGPP == 'ENABLE' -%}
        {%- if item.GGSNADDRESS is not none -%}
            GGSNADDRESS={{item.GGSNADDRESS}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：THREEGPP=ENABLE 时可选 --- -#}
    {%- if item.THREEGPP == 'ENABLE' -%}
        {%- if item.IMSIMCCMNC is not none -%}
            IMSIMCCMNC={{item.IMSIMCCMNC}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：THREEGPP=ENABLE 时可选 --- -#}
    {%- if item.THREEGPP == 'ENABLE' -%}
        {%- if item.GGSNMCCMNC is not none -%}
            GGSNMCCMNC={{item.GGSNMCCMNC}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：THREEGPP=ENABLE 时可选 --- -#}
    {%- if item.THREEGPP == 'ENABLE' -%}
        {%- if item.NSAPI is not none -%}
            NSAPI={{item.NSAPI}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：THREEGPP=ENABLE 时可选 --- -#}
    {%- if item.THREEGPP == 'ENABLE' -%}
        {%- if item.SELECTIONMODE is not none -%}
            SELECTIONMODE={{item.SELECTIONMODE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：THREEGPP=ENABLE 时可选 --- -#}
    {%- if item.THREEGPP == 'ENABLE' -%}
        {%- if item.CHARGINGCHAR is not none -%}
            CHARGINGCHAR={{item.CHARGINGCHAR}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：THREEGPP=ENABLE 时可选 --- -#}
    {%- if item.THREEGPP == 'ENABLE' -%}
        {%- if item.SGSNSGWMCCMNC is not none -%}
            SGSNSGWMCCMNC={{item.SGSNSGWMCCMNC}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：THREEGPP=ENABLE 时可选 --- -#}
    {%- if item.THREEGPP == 'ENABLE' -%}
        {%- if item.IMEISV is not none -%}
            IMEISV={{item.IMEISV}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：THREEGPP=ENABLE 时可选 --- -#}
    {%- if item.THREEGPP == 'ENABLE' -%}
        {%- if item.RATTYPE is not none -%}
            RATTYPE={{item.RATTYPE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：THREEGPP=ENABLE 时可选 --- -#}
    {%- if item.THREEGPP == 'ENABLE' -%}
        {%- if item.ULI is not none -%}
            ULI={{item.ULI}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：THREEGPP=ENABLE 时可选 --- -#}
    {%- if item.THREEGPP == 'ENABLE' -%}
        {%- if item.MSTIMEZONE is not none -%}
            MSTIMEZONE={{item.MSTIMEZONE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：THREEGPP=ENABLE 时可选 --- -#}
    {%- if item.THREEGPP == 'ENABLE' -%}
        {%- if item.NEGOTIAEDDSCP is not none -%}
            NEGOTIAEDDSCP={{item.NEGOTIAEDDSCP}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：THREEGPP=ENABLE 时可选 --- -#}
    {%- if item.THREEGPP == 'ENABLE' -%}
        {%- if item.SGSNIPV6ADDRESS is not none -%}
            SGSNIPV6ADDRESS={{item.SGSNIPV6ADDRESS}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：THREEGPP=ENABLE 时可选 --- -#}
    {%- if item.THREEGPP == 'ENABLE' -%}
        {%- if item.GGSNIPV6ADDRESS is not none -%}
            GGSNIPV6ADDRESS={{item.GGSNIPV6ADDRESS}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：THREEGPP=ENABLE 时可选 --- -#}
    {%- if item.THREEGPP == 'ENABLE' -%}
        {%- if item.CGIPV6ADDRESS is not none -%}
            CGIPV6ADDRESS={{item.CGIPV6ADDRESS}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 1.12 //配置Radius域名相关参数。

```jinja2
{%- for item in set_apnradiusattr_list -%}
    SET APNRADIUSATTR:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    {#- --- 可选参数 --- -#}
    {%- if item.DOMAINNAMEACT is not none -%}
        DOMAINNAMEACT={{item.DOMAINNAMEACT}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：DOMAINNAMEACT=ADD_ENABLE_STRIP_DISABLE 时必选 --- -#}
    {%- if item.DOMAINNAMEACT == 'ADD_ENABLE_STRIP_DISABLE' -%}
        DOMAINNAMEPOS={{item.DOMAINNAMEPOS}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 1.13 //配置SMF从Radius服务器（AAA）获取5G LAN组ID信息。

```jinja2
{%- for item in add_apnsmcomfunc_list -%}
    ADD APNSMCOMFUNC:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    {#- --- 可选参数 --- -#}
    {%- if item.GETPOLICYFIRST is not none -%}
        GETPOLICYFIRST={{item.GETPOLICYFIRST}},
    {%- endif -%}
    {%- if item.VNGRPIDSRC is not none -%}
        VNGRPIDSRC={{item.VNGRPIDSRC}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 1.14 //配置允许Radius服务器（AAA）调整的5G LAN组ID白名单。Radius服务器（AAA）调整后的5G LAN组ID不在该白名单中时，调整失败。

```jinja2
{%- for item in add_nglangrpsub_list -%}
    ADD NGLANGRPSUB:
    {#- --- 必选参数 --- -#}
    GROUPID="{{item.GROUPID}}",
    DNN="{{item.DNN}}",
    ;
{%- endfor -%}
```

### 2 **//专有数据：仅任务示例二（SMF与AAA不能直接互通，需经由UPF中转二次鉴权消息的场景）需要的配置。**

#### 2.1 //增加与UPF对接的本端GTP-U地址。复用SMF N4信令接口的IP和VPN。

```jinja2
{%- if is_scenario_via_upf_relay -%}
    {%- for item in add_cpgtpuaddr_list -%}
        ADD CPGTPUADDR:
        {#- --- 必选参数 --- -#}
        IPVERSION={{item.IPVERSION}},
        {#- --- 可选参数 --- -#}
        {%- if item.VPN is not none -%}
            VPN="{{item.VPN}}",
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：IPVERSION=IPV4 时必选 --- -#}
        {%- if item.IPVERSION == 'IPV4' -%}
            IPV4ADDR="{{item.IPV4ADDR}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 2.2 //配置中转使用的UPF列表。规划多个中转UPF时，需要配置多条数据。

```jinja2
{%- if is_scenario_via_upf_relay -%}
    {%- for item in add_uplist4rds_list -%}
        ADD UPLIST4RDS:
        {#- --- 必选参数 --- -#}
        UPLISTNAME="{{item.UPLISTNAME}}",
        UPINSTANCEID="{{item.UPINSTANCEID}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 2.3 //同一UP列表中存在多个中转UPF时，配置UPF实例的优先级。“PREFERENCE”值越大优先级越高，“LOCKED”使用样例值。

```jinja2
{%- if is_scenario_via_upf_relay -%}
    {%- for item in add_rdsupfctrl_list -%}
        ADD RDSUPFCTRL:
        {#- --- 必选参数 --- -#}
        UPLISTNAME="{{item.UPLISTNAME}}",
        UPINSTANCEID="{{item.UPINSTANCEID}}",
        PREFERENCE={{item.PREFERENCE}},
        LOCKED={{item.LOCKED}},
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 2.4 //配置UPF与Radius服务器（AAA）绑定。需先在UPF上执行ADD NETWORKINSTVPNMAP命令否则SMF尝试建立N4-U会话失败，需延迟一段时间后才会自动重试，UPF上的配置请参见配置终端二次鉴权（风筝S，通过AAA灵活调整5G LAN组ID）。

```jinja2
{%- if is_scenario_via_upf_relay -%}
    {%- for item in add_upfrdssvr_list -%}
        ADD UPFRDSSVR:
        {#- --- 必选参数 --- -#}
        SERVERTYPE={{item.SERVERTYPE}},
        IPVERSION={{item.IPVERSION}},
        UPLISTNAME="{{item.UPLISTNAME}}",
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：IPVERSION=IPV4 时必选 --- -#}
        {%- if item.IPVERSION == 'IPV4' -%}
            SERVERIPV4="{{item.SERVERIPV4}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 2.5 //配置UPF与Radius客户端（SMF Gi接口）绑定。

```jinja2
{%- if is_scenario_via_upf_relay -%}
    {%- for item in add_upfrdsclientip_list -%}
        ADD UPFRDSCLIENTIP:
        {#- --- 必选参数 --- -#}
        CLIENTYPE={{item.CLIENTYPE}},
        IPVERSION={{item.IPVERSION}},
        UPLISTNAME="{{item.UPLISTNAME}}",
        {#- --- 可选参数 --- -#}
        {%- if item.VPNINSTANCE is not none -%}
            VPNINSTANCE="{{item.VPNINSTANCE}}",
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：IPVERSION=IPV4 时必选 --- -#}
        {%- if item.IPVERSION == 'IPV4' -%}
            CLIENTIPV4="{{item.CLIENTIPV4}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```


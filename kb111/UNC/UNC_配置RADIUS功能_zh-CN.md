---
id: ''
name: 配置RADIUS功能
ne_type: UNC
type: feature
description: 该任务旨在指导操作人员完成SMF与AAA(RADIUS Server)的对接配置和功能配置。
risk_level: ''
doc_source: ["网络部署","业务专题","5G Core 一跳入家解决方案","一跳入家解决方案（基于3GPP接入方案）","业务初始部署与调测","部署一跳入家","配置专网SMF","配置RADIUS功能"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
该任务旨在指导操作人员完成SMF与AAA(RADIUS Server)的对接配置和功能配置。

## 必备事项
前提条件

* 已完成SMF基础配置。
* 已完成一跳入家要求的移动VPN相关配置。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    add_l3vpninst_list:
      type: items
      properties:
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: true
          description: '-'
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
          description: '-'
          data_source: '全局规划'
          pattern: ''
          default: perRoute
        VRFLABEL:
          name: '实例的标签值'
          type: integer
          minimum: 16
          maximum: 32767
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_vpninst_list:
      type: items
      properties:
        VPNINSTANCE:
          name: 'VPN实例名'
          type: string
          minLength: 1
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
          description: '逻辑接口使用的逻辑IP。'
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
        IPV4MTU:
          name: 'IPv4 MTU'
          type: integer
          minimum: 328
          maximum: 9600
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 1500
        IPV6MTU:
          name: 'IPv6 MTU值'
          type: integer
          minimum: 1280
          maximum: 9600
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 1500
        LOGICIPV6:
          name: 'IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_logicinf_list:
      type: items
      properties:
        NAME:
          name: '逻辑接口名称'
          type: string
          maxLength: 63
          required: true
          description: '配置使用的逻辑接口。'
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
          maxLength: 31
          required: false
          description: 'AAA服务器所属的VPN实例名。已通过**ADD VPNINST**配置，可以使用**LST VPNINST**命令进行查询。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        IPV4ADDRESS2:
          name: '逻辑接口的IPv4地址2'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV4MASK2:
          name: '逻辑接口的IPv4掩码2'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6ADDRESS1:
          name: '逻辑接口的IPv6地址1'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6ADDRESS2:
          name: '逻辑接口的IPv6地址2'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6PREFIXLEN1:
          name: 'IPv6前缀长度1'
          type: integer
          minimum: 128
          maximum: 128
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6PREFIXLEN2:
          name: 'IPv6前缀长度2'
          type: integer
          minimum: 128
          maximum: 128
          required: false
          description: ''
          data_source: ''
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
          description: '配置RADIUS服务器组。'
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
          - ENABLE
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
        ACCTONACTIVE:
          name: 'Accounting Request ON应答之前是否激活用户'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
        OFFRETRANSMIT:
          name: 'Accounting Request Off重发次数'
          type: integer
          minimum: 0
          maximum: 5
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 3
        OFFTIMEOUT:
          name: 'Accounting Request Off超时时间(秒)'
          type: integer
          minimum: 3
          maximum: 120
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 3
        ONOFFWAITTIME:
          name: 'Accounting Request On/Off消息间的时间间隔（秒）'
          type: integer
          minimum: 0
          maximum: 999
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 9
        ONRETRANSMIT:
          name: 'Accounting Request On重发次数'
          type: integer
          minimum:
          - 0
          - 255
          maximum:
          - 5
          - 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 3
        ONTIMEOUT:
          name: 'Accounting Request On超时时间 (秒)'
          type: integer
          minimum: 3
          maximum: 120
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
          description: '与AAA鉴权服务器的IP地址保持一致。'
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
          description: '鉴权AAA服务器IP地址、端口号、密钥。'
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
          description: ''
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
        SERVERIPV6:
          name: 'IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ACCTATTTEMP:
          name: 'Radius计费消息属性模板'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        COPYSVRPRIORITY:
          name: '抄送服务器优先级'
          type: integer
          minimum: 0
          maximum: 64
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 0
        PRIORITY:
          name: '服务器优先级'
          type: integer
          minimum: 1
          maximum: 16
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        WEIGHT:
          name: '权重'
          type: integer
          minimum: 1
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 255
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
          description: '可选配置。  配置APN级Gi接口鉴权。如果APN无特别规划，通过**ADD RADIUSCLIENTIP**配置即可。'
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
          description: '配置对接RADIUS场景时的鉴权能力。'
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
        APNEAP:
          name: 'APN EAP鉴权'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GULAUTHSW:
          name: '控制2/3/4G场景下是否进行鉴权'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SECONDAUTH:
          name: '二次鉴权'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        UDMSUBAUTHSW:
          name: '控制是否使用UDM签约数据参与决策进行AAA鉴权'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PCOPRIORITY:
          name: 'PCO优先级'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PWDUSEPCO:
          name: '使用PCO中的密码'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        USRNMTYPE:
          name: 'User Name信元填充方式'
          type: string
          enum:
          - MSISDN
          - IMSI
          required: false
          description: ''
          data_source: ''
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
          description: 'APN绑定RADIUS服务器组。'
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
        NASIDVALUE:
          name: 'NAS ID Value'
          type: string
          minLength: 1
          maxLength: 63
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
  examples:
    add_l3vpninst_list:
    - VRFNAME: 'vpn_aaa'
    add_vpninstaf_list:
    - VRFNAME: 'vpn_aaa'
      AFTYPE: ipv4uni
      VRFLABELMODE: perRoute
      VRFLABEL: ''
    add_vpninst_list:
    - VPNINSTANCE: 'vpn_aaa'
    add_logicip_list:
    - IPVERSION: IPv4
      LOGICIPV4: '10.8.20.1'
      VPNINSTNAME: 'vpn_aaa'
      IPV4MTU: 1500
      IPV6MTU: 1500
      LOGICIPV6: ''
    add_logicinf_list:
    - NAME: 'giif1/0/0'
      IPVERSION: IPV4
      IPV4ADDRESS1: '10.8.20.1'
      IPV4MASK1: '255.255.255.255'
      VPNINSTANCE: 'vpn_aaa'
      IPV4ADDRESS2: ''
      IPV4MASK2: ''
      IPV6ADDRESS1: ''
      IPV6ADDRESS2: ''
      IPV6PREFIXLEN1: ''
      IPV6PREFIXLEN2: ''
    add_rdssvrgrp_list:
    - RDSSVRGRPNAME: 'radius_001'
      MODE: MASTER_SLAVE
      ACCTTOAUTH: DISABLE
      SIGOPTACCTMSG: DISABLE
      ACCTTIMEOUT: 10
      ACCTRETRANSMIT: 5
      ACCTONACTIVE: DISABLE
      OFFRETRANSMIT: 3
      OFFTIMEOUT: 3
      ONOFFWAITTIME: 9
      ONRETRANSMIT: 3
      ONTIMEOUT: 3
    add_rdssvr_list:
    - RDSSVRGRPNAME: 'radius_001'
      SERVERTYPE: AUTHENTICATION
      IPVERSION: IPV4
      SERVERIPV4: '10.168.10.1'
      PORT: 1812
      VPNINSTANCE: 'vpn_aaa'
      CIPHERKEY: '*****'
      CONGESTION: DISABLE
      PRIFLAG: PRIMARY
      WALVALUE: 0
      CIPHERKEYCNFM: '*****'
      SERVERIPV6: ''
      ACCTATTTEMP: ''
      COPYSVRPRIORITY: ''
      PRIORITY: ''
      WEIGHT: 255
    add_radiusclientip_list:
    - RDSSVRGRPNAME: 'radius_001'
      AUTHORACCT: AUTHENTICATION
      INTFNAME: 'giif1/0/0'
    add_apnrdsclientip_list:
    - APN: 'home.dnn'
      AUTHORACCT: AUTHENTICATION
      INTFNAME: 'giif1/0/0'
    set_apnauthattr_list:
    - APN: 'home.dnn'
      ACCESSMODE: NON_TRANS
      AUTHMODE: MSISDN
      PASSWORD: 'Pwd001'
      CFMPASSWORD: 'Pwd001'
      COMMONUSERNAME: 'admin'
      COMMONUSERPASS: 'Huawei12#$'
      CFMCOMMUSERPASS: 'Huawei12#$'
      APNEAP: ''
      GULAUTHSW: ''
      SECONDAUTH: ''
      UDMSUBAUTHSW: ''
      PCOPRIORITY: ''
      PWDUSEPCO: ''
      USRNMTYPE: ''
    add_apnrdssvrgrp_list:
    - APN: 'home.dnn'
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
      NASIDVALUE: ''
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
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 //创建L3VPN实例。

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
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：VRFLABELMODE=perInstanceStatic 时可选 --- -#}
    {%- if item.VRFLABELMODE == 'perInstanceStatic' -%}
        {%- if item.VRFLABEL is not none -%}
            VRFLABEL={{item.VRFLABEL}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 2 //创建VPN实例。

```jinja2
{%- for item in add_vpninst_list -%}
    ADD VPNINST:
    {#- --- 必选参数 --- -#}
    VPNINSTANCE="{{item.VPNINSTANCE}}",
    ;
{%- endfor -%}
```

### 3 //配置Gi接口。

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
    {#- --- 条件必选：IPVERSION=IPv6 时必选 --- -#}
    {%- if item.IPVERSION == 'IPv6' -%}
        LOGICIPV6="{{item.LOGICIPV6}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：IPVERSION=IPv4 时可选 --- -#}
    {%- if item.IPVERSION == 'IPv4' -%}
        {%- if item.IPV4MTU is not none -%}
            IPV4MTU={{item.IPV4MTU}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：IPVERSION=IPv6 时可选 --- -#}
    {%- if item.IPVERSION == 'IPv6' -%}
        {%- if item.IPV6MTU is not none -%}
            IPV6MTU={{item.IPV6MTU}},
        {%- endif -%}
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
    {#- --- 条件必选：IPVERSION=IPV6/IPVER_ALL 时必选 --- -#}
    {%- if item.IPVERSION in ['IPV6', 'IPVER_ALL'] -%}
        IPV6ADDRESS1="{{item.IPV6ADDRESS1}}",
    {%- endif -%}
    {#- --- 条件必选：IPVERSION=IPV6/IPVER_ALL 时必选 --- -#}
    {%- if item.IPVERSION in ['IPV6', 'IPVER_ALL'] -%}
        IPV6PREFIXLEN1={{item.IPV6PREFIXLEN1}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：IPVERSION=IPV4/IPV6/IPVER_ALL 时可选 --- -#}
    {%- if item.IPVERSION in ['IPV4', 'IPV6', 'IPVER_ALL'] -%}
        {%- if item.VPNINSTANCE is not none -%}
            VPNINSTANCE="{{item.VPNINSTANCE}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：IPVERSION=IPV4/IPVER_ALL 时可选 --- -#}
    {%- if item.IPVERSION in ['IPV4', 'IPVER_ALL'] -%}
        {%- if item.IPV4ADDRESS2 is not none -%}
            IPV4ADDRESS2="{{item.IPV4ADDRESS2}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：IPVERSION=IPV4/IPVER_ALL 时可选 --- -#}
    {%- if item.IPVERSION in ['IPV4', 'IPVER_ALL'] -%}
        {%- if item.IPV4MASK2 is not none -%}
            IPV4MASK2="{{item.IPV4MASK2}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：IPVERSION=IPV6/IPVER_ALL 时可选 --- -#}
    {%- if item.IPVERSION in ['IPV6', 'IPVER_ALL'] -%}
        {%- if item.IPV6ADDRESS2 is not none -%}
            IPV6ADDRESS2="{{item.IPV6ADDRESS2}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：IPVERSION=IPV6/IPVER_ALL 时可选 --- -#}
    {%- if item.IPVERSION in ['IPV6', 'IPVER_ALL'] -%}
        {%- if item.IPV6PREFIXLEN2 is not none -%}
            IPV6PREFIXLEN2={{item.IPV6PREFIXLEN2}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 //配置RADIUS服务器组和RADIUS服务器。

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
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：SIGOPTACCTMSG=ENABLE 时可选 --- -#}
    {%- if item.SIGOPTACCTMSG == 'ENABLE' -%}
        {%- if item.ACCTONACTIVE is not none -%}
            ACCTONACTIVE={{item.ACCTONACTIVE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SIGOPTACCTMSG=ENABLE 时可选 --- -#}
    {%- if item.SIGOPTACCTMSG == 'ENABLE' -%}
        {%- if item.OFFRETRANSMIT is not none -%}
            OFFRETRANSMIT={{item.OFFRETRANSMIT}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SIGOPTACCTMSG=ENABLE 时可选 --- -#}
    {%- if item.SIGOPTACCTMSG == 'ENABLE' -%}
        {%- if item.OFFTIMEOUT is not none -%}
            OFFTIMEOUT={{item.OFFTIMEOUT}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SIGOPTACCTMSG=ENABLE 时可选 --- -#}
    {%- if item.SIGOPTACCTMSG == 'ENABLE' -%}
        {%- if item.ONOFFWAITTIME is not none -%}
            ONOFFWAITTIME={{item.ONOFFWAITTIME}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SIGOPTACCTMSG=ENABLE 时可选 --- -#}
    {%- if item.SIGOPTACCTMSG == 'ENABLE' -%}
        {%- if item.ONRETRANSMIT is not none -%}
            ONRETRANSMIT={{item.ONRETRANSMIT}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SIGOPTACCTMSG=ENABLE 时可选 --- -#}
    {%- if item.SIGOPTACCTMSG == 'ENABLE' -%}
        {%- if item.ONTIMEOUT is not none -%}
            ONTIMEOUT={{item.ONTIMEOUT}},
        {%- endif -%}
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
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPVERSION=IPV4 时必选 --- -#}
    {%- if item.IPVERSION == 'IPV4' -%}
        SERVERIPV4="{{item.SERVERIPV4}}",
    {%- endif -%}
    {#- --- 条件必选：IPVERSION=IPV6 时必选 --- -#}
    {%- if item.IPVERSION == 'IPV6' -%}
        SERVERIPV6="{{item.SERVERIPV6}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：PRIFLAG=CARBON_COPY 时可选 --- -#}
    {%- if item.PRIFLAG == 'CARBON_COPY' -%}
        {%- if item.ACCTATTTEMP is not none -%}
            ACCTATTTEMP="{{item.ACCTATTTEMP}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：PRIFLAG=CARBON_COPY 时可选 --- -#}
    {%- if item.PRIFLAG == 'CARBON_COPY' -%}
        {%- if item.COPYSVRPRIORITY is not none -%}
            COPYSVRPRIORITY={{item.COPYSVRPRIORITY}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：PRIFLAG=PRIMARY 时可选 --- -#}
    {%- if item.PRIFLAG == 'PRIMARY' -%}
        {%- if item.PRIORITY is not none -%}
            PRIORITY={{item.PRIORITY}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SERVERTYPE=AUTHENTICATION 时可选 --- -#}
    {%- if item.SERVERTYPE == 'AUTHENTICATION' -%}
        {%- if item.WEIGHT is not none -%}
            WEIGHT={{item.WEIGHT}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 5 //配置Gi接口鉴权。

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

### 6 //配置APN级Gi接口鉴权。如果APN无特别规划，通过**ADD RADIUSCLIENTIP**配置即可。

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

### 7 //配置对接RADIUS场景时的鉴权能力。

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
    {#- --- 条件可选：ACCESSMODE=NON_TRANS 时可选 --- -#}
    {%- if item.ACCESSMODE == 'NON_TRANS' -%}
        {%- if item.APNEAP is not none -%}
            APNEAP={{item.APNEAP}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：ACCESSMODE=TRANS_AUTH/NON_TRANS/LOC_AUTH 时可选 --- -#}
    {%- if item.ACCESSMODE in ['TRANS_AUTH', 'NON_TRANS', 'LOC_AUTH'] -%}
        {%- if item.GULAUTHSW is not none -%}
            GULAUTHSW={{item.GULAUTHSW}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：AUTHMODE=APN/MSISDN 时可选 --- -#}
    {%- if item.AUTHMODE in ['APN', 'MSISDN'] -%}
        {%- if item.PCOPRIORITY is not none -%}
            PCOPRIORITY={{item.PCOPRIORITY}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：AUTHMODE=APN/MSISDN 时可选 --- -#}
    {%- if item.AUTHMODE in ['APN', 'MSISDN'] -%}
        {%- if item.PWDUSEPCO is not none -%}
            PWDUSEPCO={{item.PWDUSEPCO}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：ACCESSMODE=TRANS_AUTH/NON_TRANS 时可选 --- -#}
    {%- if item.ACCESSMODE in ['TRANS_AUTH', 'NON_TRANS'] -%}
        {%- if item.SECONDAUTH is not none -%}
            SECONDAUTH={{item.SECONDAUTH}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：ACCESSMODE=TRANS_AUTH/NON_TRANS/LOC_AUTH 时可选 --- -#}
    {%- if item.ACCESSMODE in ['TRANS_AUTH', 'NON_TRANS', 'LOC_AUTH'] -%}
        {%- if item.UDMSUBAUTHSW is not none -%}
            UDMSUBAUTHSW={{item.UDMSUBAUTHSW}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：AUTHMODE=MSISDN 时可选 --- -#}
    {%- if item.AUTHMODE == 'MSISDN' -%}
        {%- if item.USRNMTYPE is not none -%}
            USRNMTYPE={{item.USRNMTYPE}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 8 //配置APN绑定RADIUS服务器组。

```jinja2
{%- for item in add_apnrdssvrgrp_list -%}
    ADD APNRDSSVRGRP:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    RDSSVRGRPNAME="{{item.RDSSVRGRPNAME}}",
    ;
{%- endfor -%}
```

### 9 //配置鉴权请求携带的属性。脚本仅为示例，实际能力需与对端AAA服务器协商。

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
    {#- --- 条件必选：NASIDTYPE=SPECIFIC_VALUE 时必选 --- -#}
    {%- if item.NASIDTYPE == 'SPECIFIC_VALUE' -%}
        NASIDVALUE="{{item.NASIDVALUE}}",
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

### 10 //配置鉴权请求携带的私有扩展属性。脚本仅为示例，实际能力需与对端AAA服务器协商。

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


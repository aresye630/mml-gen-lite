---
id: ''
name: 配置RADIUS功能
ne_type: UDG
type: feature
description: 该任务旨在指导操作人员完成SMF与AAA(RADIUS Server)的对接配置和功能配置。
risk_level: ''
doc_source: ["特性部署","业务专题","5G Core 一跳入家解决方案","一跳入家解决方案（基于3GPP接入方案）","业务初始部署与调测","部署一跳入家","配置专网SMF","配置RADIUS功能"]
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
          minLength: 0
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
          minLength: 0
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
        IPV4MTU:
          name: 'IPv4逻辑接口MTU（字节）'
          type: integer
          minimum: 328
          maximum: 9600
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 1500
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
        IPV6MTU:
          name: 'IPv6逻辑接口MTU（字节）'
          type: integer
          minimum: 1280
          maximum: 9600
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 1800
        IPV6PREFIXLEN1:
          name: 'IPv6前缀长度1'
          type: integer
          minimum: 1
          maximum: 128
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6PREFIXLEN2:
          name: 'IPv6前缀长度2'
          type: integer
          minimum: 1
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
          required: false
          description: '配置RADIUS服务器组。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        MODE:
          name: '模式'
          type: string
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        ACCTTOAUTH:
          name: '利用鉴权服务器计费'
          type: string
          required: false
          description: '指定RADIUS服务器组不支持计费。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SIGOPTACCTMSG:
          name: '支持可选计费消息'
          type: string
          required: false
          description: '指定RADIUS服务器组不支持可选计费消息。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        ACCTTIMEOUT:
          name: 'ACCTTIMEOUT'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ACCTRETRANSMIT:
          name: 'ACCTRETRANSMIT'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_rdssvr_list:
      type: items
      properties:
        RDSSVRGRPNAME:
          name: 'Radius Server Group名称'
          type: string
          required: false
          description: '与AAA鉴权服务器的IP地址保持一致。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        SERVERTYPE:
          name: '服务器类型'
          type: string
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPVERSION:
          name: '服务器IP版本'
          type: string
          required: false
          description: '鉴权AAA服务器IP地址、端口号、密钥。'
          data_source: '全局规划'
          pattern: ''
          default: ''
        SERVERIPV4:
          name: 'IPv4地址'
          type: string
          required: false
          description: ''
          data_source: '全局规划'
          pattern: ''
          default: ''
        PORT:
          name: '端口'
          type: string
          required: false
          description: ''
          data_source: '与对端协商'
          pattern: ''
          default: ''
        CIPHERKEY:
          name: '服务器密钥（加密的）'
          type: string
          required: false
          description: ''
          data_source: '与对端协商'
          pattern: ''
          default: ''
        VPNINSTANCE:
          name: 'VPN实例'
          type: string
          required: false
          description: '已通过**ADD L3VPNINST**命令进行配置，可以使用**LST L3VPNINST**进行查询。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        PRIFLAG:
          name: '主备用类型'
          type: string
          required: false
          description: '-'
          data_source: '全局规划'
          pattern: ''
          default: ''
        CIPHERKEYCNFM:
          name: '确认服务器密钥（加密的）'
          type: string
          required: false
          description: '-'
          data_source: '与对端协商'
          pattern: ''
          default: ''
        CONGESTION:
          name: 'CONGESTION'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        WALVALUE:
          name: 'WALVALUE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_radiusclientip_list:
      type: items
      properties:
        RDSSVRGRPNAME:
          name: 'Radius Server Group名称'
          type: string
          required: false
          description: '配置Gi接口鉴权。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        AUTHORACCT:
          name: '鉴权或计费'
          type: string
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
        INTFNAME:
          name: '接口名称'
          type: string
          required: false
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
          required: false
          description: '可选配置。  配置APN级Gi接口鉴权。如果APN无特别规划，通过**ADD RADIUSCLIENTIP**配置即可。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        AUTHORACCT:
          name: '鉴权或计费'
          type: string
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
        INTFNAME:
          name: '接口名称'
          type: string
          required: false
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
          required: false
          description: '配置对接RADIUS场景时的鉴权能力。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        ACCESSMODE:
          name: '接入模式'
          type: string
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
        AUTHMODE:
          name: '鉴权模式'
          type: string
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
        PASSWORD:
          name: '鉴权密码'
          type: string
          required: false
          description: ''
          data_source: '全局规划'
          pattern: ''
          default: ''
        CFMPASSWORD:
          name: '确认鉴权密码'
          type: string
          required: false
          description: ''
          data_source: '全局规划'
          pattern: ''
          default: ''
        COMMONUSERNAME:
          name: '公用用户名'
          type: string
          required: false
          description: ''
          data_source: '全局规划'
          pattern: ''
          default: ''
        COMMONUSERPASS:
          name: '公用密码'
          type: string
          required: false
          description: ''
          data_source: '全局规划'
          pattern: ''
          default: ''
        CFMCOMMUSERPASS:
          name: '确认公共密码'
          type: string
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
          required: false
          description: 'APN绑定RADIUS服务器组。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        RDSSVRGRPNAME:
          name: 'Radius Server Group名称'
          type: string
          required: false
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
          required: false
          description: '设置鉴权请求携带的属性，实际能力需与对端AAA服务器协商。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        ACCTSESSIONID:
          name: 'Acct-Session-Id'
          type: string
          required: false
          description: ''
          data_source: '全局规划'
          pattern: ''
          default: ''
        NASID:
          name: 'NAS-ID'
          type: string
          required: false
          description: ''
          data_source: '全局规划'
          pattern: ''
          default: ''
        NASIDTYPE:
          name: 'NASIDTYPE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IMSI:
          name: 'IMSI'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CHARGINGID:
          name: 'CHARGINGID'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PREPAIDIND:
          name: 'PREPAIDIND'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GGSNIP:
          name: 'GGSNIP'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SGSNIP:
          name: 'SGSNIP'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        REQUESTAPN:
          name: 'REQUESTAPN'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GGSNVENDOR:
          name: 'GGSNVENDOR'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GGSNVERION:
          name: 'GGSNVERION'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RQAUTHTICATOR:
          name: 'RQAUTHTICATOR'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ACCTMULSESSID:
          name: 'ACCTMULSESSID'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        EVENTTIME:
          name: 'EVENTTIME'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NASPORTIDSW:
          name: 'NASPORTIDSW'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NASPORTID:
          name: 'NASPORTID'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        WLANADDR:
          name: 'WLANADDR'
          type: string
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
          required: false
          description: '配置鉴权请求携带的私有扩展属性，实际能力需与对端AAA服务器协商。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        THREEGPP:
          name: '3GPP私有扩展属性开关'
          type: string
          required: false
          description: ''
          data_source: '全局规划'
          pattern: ''
          default: ''
        IMSI:
          name: '3GPP-IMSI'
          type: string
          required: false
          description: ''
          data_source: '全局规划'
          pattern: ''
          default: ''
        CHARGINGID:
          name: 'CHARGINGID'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PDPTYPE:
          name: 'PDPTYPE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CGADDRESS:
          name: 'CGADDRESS'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NEGOTIAEDQOS:
          name: 'NEGOTIAEDQOS'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SGSNSGWADDRESS:
          name: 'SGSNSGWADDRESS'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GGSNADDRESS:
          name: 'GGSNADDRESS'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IMSIMCCMNC:
          name: 'IMSIMCCMNC'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GGSNMCCMNC:
          name: 'GGSNMCCMNC'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NSAPI:
          name: 'NSAPI'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SELECTIONMODE:
          name: 'SELECTIONMODE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CHARGINGCHAR:
          name: 'CHARGINGCHAR'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SGSNSGWMCCMNC:
          name: 'SGSNSGWMCCMNC'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IMEISV:
          name: 'IMEISV'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RATTYPE:
          name: 'RATTYPE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ULI:
          name: 'ULI'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MSTIMEZONE:
          name: 'MSTIMEZONE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NEGOTIAEDDSCP:
          name: 'NEGOTIAEDDSCP'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SGSNIPV6ADDRESS:
          name: 'SGSNIPV6ADDRESS'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GGSNIPV6ADDRESS:
          name: 'GGSNIPV6ADDRESS'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CGIPV6ADDRESS:
          name: 'CGIPV6ADDRESS'
          type: string
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
      IPV4MTU: 1500
      IPV6ADDRESS1: ''
      IPV6ADDRESS2: ''
      IPV6MTU: 1800
      IPV6PREFIXLEN1: ''
      IPV6PREFIXLEN2: ''
    add_rdssvrgrp_list:
    - RDSSVRGRPNAME: radius_001
      MODE: MASTER_SLAVE
      ACCTTOAUTH: DISABLE
      SIGOPTACCTMSG: DISABLE
      ACCTTIMEOUT: '10'
      ACCTRETRANSMIT: '5'
    add_rdssvr_list:
    - RDSSVRGRPNAME: radius_001
      SERVERTYPE: AUTHENTICATION
      IPVERSION: IPV4
      SERVERIPV4: 10.168.10.1
      PORT: '1812'
      CIPHERKEY: '*****'
      VPNINSTANCE: vpn_aaa
      PRIFLAG: PRIMARY
      CIPHERKEYCNFM: '*****'
      CONGESTION: DISABLE
      WALVALUE: '0'
    add_radiusclientip_list:
    - RDSSVRGRPNAME: radius_001
      AUTHORACCT: AUTHENTICATION
      INTFNAME: giif1/0/0
    add_apnrdsclientip_list:
    - APN: home.dnn
      AUTHORACCT: AUTHENTICATION
      INTFNAME: giif1/0/0
    set_apnauthattr_list:
    - APN: home.dnn
      ACCESSMODE: NON_TRANS
      AUTHMODE: MSISDN
      PASSWORD: Pwd001
      CFMPASSWORD: Pwd001
      COMMONUSERNAME: admin
      COMMONUSERPASS: Huawei12#$
      CFMCOMMUSERPASS: Huawei12#$
    add_apnrdssvrgrp_list:
    - APN: home.dnn
      RDSSVRGRPNAME: radius_001
    set_rdsauthreqattr_list:
    - RDSSVRGRPNAME: radius_001
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
      NASPORTID: UNC
      WLANADDR: DISABLE
    set_rdsauthreqvsa_list:
    - RDSSVRGRPNAME: radius_001
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
    {#- --- 条件必选：IPVERSION=IPVER_ALL/IPV6 时必选 --- -#}
    {%- if item.IPVERSION in ['IPVER_ALL', 'IPV6'] -%}
        IPV6ADDRESS1="{{item.IPV6ADDRESS1}}",
    {%- endif -%}
    {#- --- 条件必选：IPVERSION=IPVER_ALL/IPV6 时必选 --- -#}
    {%- if item.IPVERSION in ['IPVER_ALL', 'IPV6'] -%}
        IPV6PREFIXLEN1={{item.IPV6PREFIXLEN1}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：IPVERSION=IPV4/IPVER_ALL/IPV6 时可选 --- -#}
    {%- if item.IPVERSION in ['IPV4', 'IPVER_ALL', 'IPV6'] -%}
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
    {#- --- 条件可选：IPVERSION=IPV4/IPVER_ALL 时可选 --- -#}
    {%- if item.IPVERSION in ['IPV4', 'IPVER_ALL'] -%}
        {%- if item.IPV4MTU is not none -%}
            IPV4MTU={{item.IPV4MTU}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：IPVERSION=IPVER_ALL/IPV6 时可选 --- -#}
    {%- if item.IPVERSION in ['IPVER_ALL', 'IPV6'] -%}
        {%- if item.IPV6ADDRESS2 is not none -%}
            IPV6ADDRESS2="{{item.IPV6ADDRESS2}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：IPVERSION=IPVER_ALL/IPV6 时可选 --- -#}
    {%- if item.IPVERSION in ['IPVER_ALL', 'IPV6'] -%}
        {%- if item.IPV6MTU is not none -%}
            IPV6MTU={{item.IPV6MTU}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：IPVERSION=IPVER_ALL/IPV6 时可选 --- -#}
    {%- if item.IPVERSION in ['IPVER_ALL', 'IPV6'] -%}
        {%- if item.IPV6PREFIXLEN2 is not none -%}
            IPV6PREFIXLEN2={{item.IPV6PREFIXLEN2}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 //配置RADIUS服务器组和RADIUS服务器。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_rdssvrgrp_list的变量区（command: ADD RDSSVRGRP） -#}
<!-- MISSING_MACRO: command=ADD RDSSVRGRP list_name=add_rdssvrgrp_list step_id=4 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_rdssvr_list的变量区（command: ADD RDSSVR） -#}
<!-- MISSING_MACRO: command=ADD RDSSVR list_name=add_rdssvr_list step_id=4 -->
```

### 5 //配置Gi接口鉴权。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_radiusclientip_list的变量区（command: ADD RADIUSCLIENTIP） -#}
<!-- MISSING_MACRO: command=ADD RADIUSCLIENTIP list_name=add_radiusclientip_list step_id=5 -->
```

### 6 //配置APN级Gi接口鉴权。如果APN无特别规划，通过**ADD RADIUSCLIENTIP**配置即可。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_apnrdsclientip_list的变量区（command: ADD APNRDSCLIENTIP） -#}
<!-- MISSING_MACRO: command=ADD APNRDSCLIENTIP list_name=add_apnrdsclientip_list step_id=6 -->
```

### 7 //配置对接RADIUS场景时的鉴权能力。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_apnauthattr_list的变量区（command: SET APNAUTHATTR） -#}
<!-- MISSING_MACRO: command=SET APNAUTHATTR list_name=set_apnauthattr_list step_id=7 -->
```

### 8 //配置APN绑定RADIUS服务器组。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_apnrdssvrgrp_list的变量区（command: ADD APNRDSSVRGRP） -#}
<!-- MISSING_MACRO: command=ADD APNRDSSVRGRP list_name=add_apnrdssvrgrp_list step_id=8 -->
```

### 9 //配置鉴权请求携带的属性。脚本仅为示例，实际能力需与对端AAA服务器协商。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_rdsauthreqattr_list的变量区（command: SET RDSAUTHREQATTR） -#}
<!-- MISSING_MACRO: command=SET RDSAUTHREQATTR list_name=set_rdsauthreqattr_list step_id=9 -->
```

### 10 //配置鉴权请求携带的私有扩展属性。脚本仅为示例，实际能力需与对端AAA服务器协商。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_rdsauthreqvsa_list的变量区（command: SET RDSAUTHREQVSA） -#}
<!-- MISSING_MACRO: command=SET RDSAUTHREQVSA list_name=set_rdsauthreqvsa_list step_id=10 -->
```


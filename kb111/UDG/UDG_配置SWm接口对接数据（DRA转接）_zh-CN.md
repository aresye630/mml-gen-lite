---
id: ''
name: 配置SWm接口对接数据（DRA转接）
ne_type: UDG
type: feature
description: UPF与Non-SIM AAA UDM-UIM间存在直连、非直连路径。图1表示经DRA的非直连路径。  **图1** DRA组网  当UPF与Non-SIM AAA之间直连路径故障或者未配置直连路径时，可以配置到DRA，DRA在UPF与Non-SIM AAA间转交消息，提供非3GPP鉴权认证功能。UPF与Non-SIM AAA交互时，优先选择直连路径发送消息。  * SWm接口当前版本仅支持IPv4栈类型。 * 专网UPF配置SWm接口时，不支持开启入不转板功能特性。
risk_level: ''
doc_source: ["特性部署","业务专题","5G Core 一跳入家解决方案","一跳入家解决方案（基于非3GPP接入方案）","业务初始部署与调测","部署一跳入家","配置一跳入家专网UPF","配置SWm接口对接数据（DRA转接）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
UPF与Non-SIM AAA UDM-UIM间存在直连、非直连路径。图1表示经DRA的非直连路径。**图1** DRA组网当UPF与Non-SIM AAA之间直连路径故障或者未配置直连路径时，可以配置到DRA，DRA在UPF与Non-SIM AAA间转交消息，提供非3GPP鉴权认证功能。UPF与Non-SIM AAA交互时，优先选择直连路径发送消息。* SWm接口当前版本仅支持IPv4栈类型。* 专网UPF配置SWm接口时，不支持开启入不转板功能特性。

## 必备事项
前提条件

前提条件

* UPF软件安装已完成。
* UPF初始配置已完成。
* 已完成一跳入家依赖功能的License加载。
* 已完成一跳入家要求的移动VPN相关配置。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
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
          data_source: '全网规划'
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
          description: '-'
          data_source: '全网规划'
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
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AFTYPE:
          name: '地址族类型'
          type: string
          enum:
          - ipv4uni
          - ipv6uni
          required: true
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
          description: '-'
          data_source: '全网规划'
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
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV4ADDRESS1:
          name: '逻辑接口的IPv4地址1'
          type: string
          maxLength: 15
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV4MASK1:
          name: '逻辑接口的IPv4掩码1'
          type: string
          maxLength: 15
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        VPNINSTANCE:
          name: 'VPN实例名称'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: '-'
          data_source: '全网规划'
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
    set_upconcenpoint_list:
      type: items
      properties:
        SWMCONCENMODE:
          name: 'Swm集中点模式'
          type: string
          enum:
          - LOCALIP_PEER
          - LOCALPORT
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_updra_list:
      type: items
      properties:
        HOSTNAME:
          name: '主机名'
          type: string
          minLength: 0
          maxLength: 127
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        VPNINSTANCE:
          name: 'VPN实例'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: '-'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_updiampeeraddr_list:
      type: items
      properties:
        HOSTNAME:
          name: '主机名称'
          type: string
          minLength: 0
          maxLength: 127
          required: true
          description: '-'
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
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPV4ADDRESS:
          name: 'IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: '-'
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
          data_source: ''
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
          minLength: 0
          maxLength: 63
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_updiamlocinfo_list:
      type: items
      properties:
        HOSTNAME:
          name: '本端主机名'
          type: string
          minLength: 0
          maxLength: 127
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        REALMNAME:
          name: '本端域名'
          type: string
          minLength: 0
          maxLength: 127
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PRODUCTNAME:
          name: '产品名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        ORIGINSTATEID:
          name: 'Origin-State-Id AVP使能开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
        SUPPORTVENDORID:
          name: 'Supported-Vendor-Id AVP使能开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
    add_updiamconngrp_list:
      type: items
      properties:
        CONNGROUPNAME:
          name: 'Diameter链路组名'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: '该命令用于指定本端主机名与指定对端服务器之间建立一组Diameter链路。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        LOCALHOSTNAME:
          name: '本端主机名'
          type: string
          minLength: 0
          maxLength: 127
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        APPLICATION:
          name: 'Diameter应用'
          type: string
          enum:
          - SWM
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        PEERHOSTNAME:
          name: '对端主机名'
          type: string
          minLength: 0
          maxLength: 127
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        SELECTMODE:
          name: '链路选择模式'
          type: string
          enum:
          - MASTER_SLAVE
          - ROUND_ROBIN
          - SESSION_ID
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: SESSION_ID
    add_updiamconn_list:
      type: items
      properties:
        DIAMCONNGRP:
          name: 'Diameter链路组名'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: '增加Diameter链路。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        LOCINTERFACE:
          name: '本端接口名'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        PEERADDRTYPE:
          name: '对端地址类型'
          type: string
          enum:
          - IPv4
          - IPv6
          - SCTP
          required: false
          description: '*-*'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PEERPORT:
          name: '对端端口'
          type: integer
          minimum: 1
          maximum: 65534
          required: false
          description: '*-*'
          data_source: '对端协商'
          pattern: ''
          default: ''
        PEERIPV4ADDR:
          name: '对端IPV4地址'
          type: string
          maxLength: 15
          required: false
          description: 'IPv4地址类型。不支持0.0.0.0和255.255.255.255。'
          data_source: '对端协商'
          pattern: ''
          default: ''
        LOCALPORT:
          name: '本端端口'
          type: integer
          minimum:
          - 0
          - 19865
          maximum:
          - 0
          - 19928
          required: false
          description: '取值范围19865~19928。'
          data_source: '对端协商'
          pattern: ''
          default: 0
        PEERIPV6ADDR:
          name: '对端IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PEERSCTPENDPT:
          name: '对端SCTP端点名称'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        REVERSEIP:
          name: 'SCTP建链交换本端IP地址'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
    add_updiamrtrealm_list:
      type: items
      properties:
        REALMNAME:
          name: 'Diameter域名名称'
          type: string
          minLength: 0
          maxLength: 127
          required: true
          description: '-'
          data_source: '与对端协商'
          pattern: ''
          default: ''
        APPLICATION:
          name: 'Diameter应用'
          type: string
          enum:
          - SWM
          required: true
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        SELECTMODE:
          name: '路由选择模式'
          type: string
          enum:
          - MASTER_SLAVE
          - ROUND_ROBIN
          - SESSION_ID
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: SESSION_ID
        FAILOVERSW:
          name: 'Failover开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
        AUTOFAILBACKSW:
          name: '自动倒回开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
    add_updiamrtnexthop_list:
      type: items
      properties:
        REALMNAME:
          name: 'Diameter域名名称'
          type: string
          minLength: 0
          maxLength: 127
          required: true
          description: '说明：  下一跳的主机名“HOSTNAME”只允许设置成已配置的DRA主机名。'
          data_source: '与对端协商'
          pattern: ''
          default: ''
        APPLICATION:
          name: 'Diameter应用'
          type: string
          enum:
          - SWM
          required: true
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        NEXTHOP:
          name: '下一跳'
          type: string
          minLength: 0
          maxLength: 127
          required: true
          description: '-'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        SEQUENCE:
          name: '序号'
          type: integer
          minimum: 1
          maximum: 65535
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_updiameterpara_list:
      type: items
      properties:
        REALMBASEROUTE:
          name: '基于域名的路由功能开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_upglbdiamrealm_list:
      type: items
      properties:
        APPLICATION:
          name: 'Diameter应用'
          type: string
          enum:
          - SWM
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        CONSTBYIMSISW:
          name: '根据IMSI构造归属地Realm开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        REALM:
          name: 'Diameter域名'
          type: string
          minLength: 0
          maxLength: 127
          required: false
          description: '-'
          data_source: '与对端协商'
          pattern: ''
          default: ''
    add_apn_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_uprealmbindapn_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '已通过命令**ADD APN**进行配置，可以使用命令**LST APN**查询。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        APPLICATION:
          name: 'Diameter应用'
          type: string
          enum:
          - SWM
          required: true
          description: '-'
          data_source: '与对端协商'
          pattern: ''
          default: ''
        CONSTBYIMSISW:
          name: '根据IMSI构造归属地Realm开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: true
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        REALMNAME:
          name: 'Realm名'
          type: string
          minLength: 0
          maxLength: 127
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_vpninst_list_1:
      type: items
      properties:
        VPNINSTANCE:
          name: 'VPN实例名'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_l3vpninst_list_1:
      type: items
      properties:
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: true
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_vpninstaf_list_1:
      type: items
      properties:
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AFTYPE:
          name: '地址族类型'
          type: string
          enum:
          - ipv4uni
          - ipv6uni
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_logicinf_list_1:
      type: items
      properties:
        NAME:
          name: '逻辑接口名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '-'
          data_source: '全网规划'
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
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV4ADDRESS1:
          name: '逻辑接口的IPv4地址1'
          type: string
          maxLength: 15
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV4MASK1:
          name: '逻辑接口的IPv4掩码1'
          type: string
          maxLength: 15
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV4ADDRESS2:
          name: '逻辑接口的IPv4地址2'
          type: string
          maxLength: 15
          required: false
          description: 'SCTP over DRA场景下配置该参数，TCP over DRA场景下，无需配置。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV4MASK2:
          name: '逻辑接口的IPv4掩码2'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        VPNINSTANCE:
          name: 'VPN实例名称'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: '-'
          data_source: '全网规划'
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
    set_upconcenpoint_list_1:
      type: items
      properties:
        SWMCONCENMODE:
          name: 'Swm集中点模式'
          type: string
          enum:
          - LOCALIP_PEER
          - LOCALPORT
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_upsctptemplate_list:
      type: items
      properties:
        SCTPTEMPLNAME:
          name: 'SCTP模板名称'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        HEARTBEATINTVAL:
          name: 'SCTP发送心跳消息的间隔周期（毫秒）'
          type: integer
          minimum: 10
          maximum: 60000
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: 30000
        MAXASSOCRETRY:
          name: 'SCTP耦联上消息重传的最大次数'
          type: integer
          minimum: 2
          maximum: 254
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: 5
        MAXPATHRETRY:
          name: 'SCTP到特定IP消息重传的最大次数'
          type: integer
          minimum: 1
          maximum: 253
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: 4
        CHECKSUMTYPE:
          name: 'SCTP协议校验和算法'
          type: string
          enum:
          - ADLER32
          - CRC32
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: CRC32
    add_upsctpendpoint_list:
      type: items
      properties:
        ENDPOINTNAME:
          name: '端点名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '定义两个端点为“endpoint0”和“endpoint1”，每个端点有两个IP地址，端点“endpoint0”的IP地址为192.168.10.1和192.168.10.2，端点“endpoint1”的IP地址为192.168.20.1和192.168.20.2。端口号均为3868。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPVERSION:
          name: 'IP版本'
          type: string
          enum:
          - IPV4
          - IPV6
          required: true
          description: ''
          data_source: '与对端协商'
          pattern: ''
          default: ''
        IPV4ADDRESS1:
          name: 'IPv4地址1'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV4ADDRESS2:
          name: 'IPv4地址2'
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
          data_source: '与对端协商'
          pattern: ''
          default: 3868
        SCTPTEMPLNAME:
          name: 'SCTP模板名称'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: '已通过**ADD SCTPTEMPLATE**命令配置，可以使用**LST SCTPTEMPLATE**命令查询。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        IPV6ADDRESS1:
          name: 'IPv6地址1'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6ADDRESS2:
          name: 'IPv6地址2'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_upglbsctppara_list:
      type: items
      properties:
        PATHSELECTMODE:
          name: 'SCTP路径选择模式'
          type: string
          enum:
          - ALL
          - PARALLEL
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        RTOMINVALUE:
          name: 'RTO重发超时的最小值（毫秒）'
          type: integer
          minimum: 200
          maximum: 1000
          required: false
          description: '-'
          data_source: '与对端协商'
          pattern: ''
          default: ''
        RTOMAXVALUE:
          name: 'RTO重发超时的最大值（毫秒）'
          type: integer
          minimum: 500
          maximum: 6000
          required: false
          description: '-'
          data_source: '与对端协商'
          pattern: ''
          default: ''
        RTOINITVALUE:
          name: 'RTO重发超时的初始值（毫秒）'
          type: integer
          minimum: 200
          maximum: 1000
          required: false
          description: '-'
          data_source: '与对端协商'
          pattern: ''
          default: ''
    add_updra_list_2:
      type: items
      properties:
        HOSTNAME:
          name: '主机名'
          type: string
          minLength: 0
          maxLength: 127
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        VPNINSTANCE:
          name: 'VPN实例'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: '-'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_updiampeeraddr_list_2:
      type: items
      properties:
        HOSTNAME:
          name: '主机名称'
          type: string
          minLength: 0
          maxLength: 127
          required: true
          description: '-'
          data_source: '与对端协商'
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
          description: '-'
          data_source: '与对端协商'
          pattern: ''
          default: ''
        SCTPENDPOINT:
          name: 'SCTP端点名称'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: '-'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        IPV4ADDRESS:
          name: 'IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6ADDRESS:
          name: 'IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PORT:
          name: '端口号'
          type: integer
          minimum: 1
          maximum: 65534
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 3868
    add_updiamlocinfo_list_1:
      type: items
      properties:
        HOSTNAME:
          name: '本端主机名'
          type: string
          minLength: 0
          maxLength: 127
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        REALMNAME:
          name: '本端域名'
          type: string
          minLength: 0
          maxLength: 127
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PRODUCTNAME:
          name: '产品名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        ORIGINSTATEID:
          name: 'Origin-State-Id AVP使能开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
        SUPPORTVENDORID:
          name: 'Supported-Vendor-Id AVP使能开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
    add_updiamconngrp_list_2:
      type: items
      properties:
        CONNGROUPNAME:
          name: 'Diameter链路组名'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: '该命令用于指定本端主机名与指定对端服务器之间建立一组Diameter链路。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        LOCALHOSTNAME:
          name: '本端主机名'
          type: string
          minLength: 0
          maxLength: 127
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        APPLICATION:
          name: 'Diameter应用'
          type: string
          enum:
          - SWM
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        PEERHOSTNAME:
          name: '对端主机名'
          type: string
          minLength: 0
          maxLength: 127
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        SELECTMODE:
          name: '链路选择模式'
          type: string
          enum:
          - MASTER_SLAVE
          - ROUND_ROBIN
          - SESSION_ID
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: SESSION_ID
    add_updiamconn_list_2:
      type: items
      properties:
        DIAMCONNGRP:
          name: 'Diameter链路组名'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: '增加Diameter链路。  已经通过**ADD LOGICINF**命令配置，可以使用**LST LOGICINF**查询。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        LOCINTERFACE:
          name: '本端接口名'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        PEERADDRTYPE:
          name: '对端地址类型'
          type: string
          enum:
          - IPv4
          - IPv6
          - SCTP
          required: false
          description: '-'
          data_source: '与对端协商'
          pattern: ''
          default: ''
        PEERSCTPENDPT:
          name: '对端SCTP端点名称'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: 'SCTP端点已通过**ADD SCTPENDPOINT**命令配置，可以使用**LST SCTPENDPOINT**查询。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        REVERSEIP:
          name: 'SCTP建链交换本端IP地址'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '-'
          data_source: '与对端协商'
          pattern: ''
          default: DISABLE
        LOCALPORT:
          name: '本端端口'
          type: integer
          minimum:
          - 0
          - 19865
          maximum:
          - 0
          - 19928
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: 0
        PEERIPV4ADDR:
          name: '对端IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PEERIPV6ADDR:
          name: '对端IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PEERPORT:
          name: '对端端口号'
          type: integer
          minimum: 1
          maximum: 65534
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_updiamrtrealm_list_1:
      type: items
      properties:
        REALMNAME:
          name: 'iameter域名名称'
          type: string
          minLength: 0
          maxLength: 127
          required: true
          description: '-'
          data_source: '与对端协商'
          pattern: ''
          default: ''
        APPLICATION:
          name: 'Diameter应用'
          type: string
          enum:
          - SWM
          required: true
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        SELECTMODE:
          name: '路由选择模式'
          type: string
          enum:
          - MASTER_SLAVE
          - ROUND_ROBIN
          - SESSION_ID
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: SESSION_ID
        FAILOVERSW:
          name: 'Failover开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
        AUTOFAILBACKSW:
          name: '自动倒回开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
    add_updiamrtnexthop_list_2:
      type: items
      properties:
        REALMNAME:
          name: 'Diameter域名名称'
          type: string
          minLength: 0
          maxLength: 127
          required: true
          description: '说明：  下一跳的主机名“HOSTNAME”只允许设置成已配置的DRA主机名。'
          data_source: '与对端协商'
          pattern: ''
          default: ''
        APPLICATION:
          name: 'Diameter应用'
          type: string
          enum:
          - SWM
          required: true
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        NEXTHOP:
          name: '下一跳'
          type: string
          minLength: 0
          maxLength: 127
          required: true
          description: '-'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        SEQUENCE:
          name: '序号'
          type: integer
          minimum: 1
          maximum: 65535
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_updiameterpara_list_1:
      type: items
      properties:
        REALMBASEROUTE:
          name: '基于域名的路由功能开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_upglbdiamrealm_list_1:
      type: items
      properties:
        APPLICATION:
          name: 'Diameter应用'
          type: string
          enum:
          - SWM
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        CONSTBYIMSISW:
          name: '根据IMSI构造归属地Realm开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        REALM:
          name: 'Diameter域名'
          type: string
          minLength: 0
          maxLength: 127
          required: false
          description: '-'
          data_source: '与对端协商'
          pattern: ''
          default: ''
    add_apn_list_1:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_uprealmbindapn_list_1:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '已通过命令**ADD APN**进行配置，可以使用命令**LST APN**查询。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        APPLICATION:
          name: 'Diameter应用'
          type: string
          enum:
          - SWM
          required: true
          description: '-'
          data_source: '与对端协商'
          pattern: ''
          default: ''
        CONSTBYIMSISW:
          name: '根据IMSI构造归属地Realm开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: true
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        REALMNAME:
          name: 'Realm名'
          type: string
          minLength: 0
          maxLength: 127
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
  examples:
    add_vpninst_list:
    - VPNINSTANCE: 'VPN_Signaling'
    add_l3vpninst_list:
    - VRFNAME: 'VPN_Signaling'
    add_vpninstaf_list:
    - VRFNAME: 'VPN_Signaling'
      AFTYPE: ipv4uni
    add_logicinf_list:
    - NAME: 'swmif1/0/0'
      IPVERSION: IPV4
      IPV4ADDRESS1: '192.168.3.1'
      IPV4MASK1: '255.255.255.255'
      VPNINSTANCE: 'VPN_Signaling'
      IPV4ADDRESS2: ''
      IPV4MASK2: ''
      IPV4MTU: 1500
      IPV6ADDRESS1: ''
      IPV6ADDRESS2: ''
      IPV6MTU: 1800
      IPV6PREFIXLEN1: ''
      IPV6PREFIXLEN2: ''
    set_upconcenpoint_list:
    - SWMCONCENMODE: LOCALPORT
    add_updra_list:
    - HOSTNAME: 'dra01.huawei.com'
      VPNINSTANCE: 'VPN_Signaling'
    add_updiampeeraddr_list:
    - HOSTNAME: 'dra01.huawei.com'
      ADDRTYPE: IPv4
      IPV4ADDRESS: '172.17.251.66'
      PORT: 3868
      IPV6ADDRESS: ''
      SCTPENDPOINT: ''
    add_updiamlocinfo_list:
    - HOSTNAME: 'udg_1'
      REALMNAME: 'peer.huawei.com'
      PRODUCTNAME: 'udg@huawei.com'
      ORIGINSTATEID: DISABLE
      SUPPORTVENDORID: DISABLE
    add_updiamconngrp_list:
    - CONNGROUPNAME: 'udgaaagrp1'
      LOCALHOSTNAME: 'udg_1'
      APPLICATION: SWM
      PEERHOSTNAME: 'dra01.huawei.com'
      SELECTMODE: SESSION_ID
    add_updiamconn_list:
    - DIAMCONNGRP: 'udgaaagrp1'
      LOCINTERFACE: 'swmif1/0/0'
      PEERADDRTYPE: IPv4
      PEERPORT: 3868
      PEERIPV4ADDR: '172.16.251.66'
      LOCALPORT: 19865
      PEERIPV6ADDR: ''
      PEERSCTPENDPT: ''
      REVERSEIP: DISABLE
    add_updiamrtrealm_list:
    - REALMNAME: 'huawei.com'
      APPLICATION: SWM
      SELECTMODE: SESSION_ID
      FAILOVERSW: DISABLE
      AUTOFAILBACKSW: DISABLE
    add_updiamrtnexthop_list:
    - REALMNAME: 'huawei.com'
      APPLICATION: SWM
      NEXTHOP: 'dra01.huawei.com'
      SEQUENCE: 1
    set_updiameterpara_list:
    - REALMBASEROUTE: ENABLE
    add_upglbdiamrealm_list:
    - APPLICATION: SWM
      CONSTBYIMSISW: DISABLE
      REALM: 'huawei.com'
    add_apn_list:
    - APN: '032apn1.com'
    add_uprealmbindapn_list:
    - APN: '032apn1.com'
      APPLICATION: SWM
      CONSTBYIMSISW: DISABLE
      REALMNAME: 'huawei.com'
    add_vpninst_list_1:
    - VPNINSTANCE: 'VPN_Signaling'
    add_l3vpninst_list_1:
    - VRFNAME: 'VPN_Signaling'
    add_vpninstaf_list_1:
    - VRFNAME: 'VPN_Signaling'
      AFTYPE: ipv4uni
    add_logicinf_list_1:
    - NAME: 'swmif1/0/0'
      IPVERSION: IPV4
      IPV4ADDRESS1: '192.168.3.1'
      IPV4MASK1: '255.255.255.255'
      IPV4ADDRESS2: '192.168.3.2'
      IPV4MASK2: '255.255.255.255'
      VPNINSTANCE: 'VPN_Signaling'
      IPV4MTU: 1500
      IPV6ADDRESS1: ''
      IPV6ADDRESS2: ''
      IPV6MTU: 1800
      IPV6PREFIXLEN1: ''
      IPV6PREFIXLEN2: ''
    set_upconcenpoint_list_1:
    - SWMCONCENMODE: LOCALPORT
    add_upsctptemplate_list:
    - SCTPTEMPLNAME: 'dra_template'
      HEARTBEATINTVAL: 30000
      MAXASSOCRETRY: 5
      MAXPATHRETRY: 4
      CHECKSUMTYPE: CRC32
    add_upsctpendpoint_list:
    - ENDPOINTNAME: 'endpoint0'
      IPVERSION: IPV4
      IPV4ADDRESS1: '192.168.10.1'
      IPV4ADDRESS2: '192.168.10.2'
      PORT: 3868
      SCTPTEMPLNAME: 'dra_template'
      IPV6ADDRESS1: ''
      IPV6ADDRESS2: ''
    set_upglbsctppara_list:
    - PATHSELECTMODE: ALL
      RTOMINVALUE: 500
      RTOMAXVALUE: 1500
      RTOINITVALUE: 500
    add_updra_list_2:
    - HOSTNAME: 'dra01.huawei.com'
      VPNINSTANCE: 'VPN_Signaling'
    add_updiampeeraddr_list_2:
    - HOSTNAME: 'dra01.huawei.com'
      ADDRTYPE: SCTP
      SCTPENDPOINT: 'endpoint0'
      IPV4ADDRESS: ''
      IPV6ADDRESS: ''
      PORT: 3868
    add_updiamlocinfo_list_1:
    - HOSTNAME: 'udg_1'
      REALMNAME: 'peer.huawei.com'
      PRODUCTNAME: 'udg@huawei.com'
      ORIGINSTATEID: DISABLE
      SUPPORTVENDORID: DISABLE
    add_updiamconngrp_list_2:
    - CONNGROUPNAME: 'udgaaagrp1'
      LOCALHOSTNAME: 'udg_1'
      APPLICATION: SWM
      PEERHOSTNAME: 'dra01.huawei.com'
      SELECTMODE: SESSION_ID
    add_updiamconn_list_2:
    - DIAMCONNGRP: 'udgaaagrp1'
      LOCINTERFACE: 'swmif1/0/0'
      PEERADDRTYPE: SCTP
      PEERSCTPENDPT: 'endpoint0'
      REVERSEIP: DISABLE
      LOCALPORT: 19865
      PEERIPV4ADDR: ''
      PEERIPV6ADDR: ''
      PEERPORT: ''
    add_updiamrtrealm_list_1:
    - REALMNAME: 'huawei.com'
      APPLICATION: SWM
      SELECTMODE: SESSION_ID
      FAILOVERSW: DISABLE
      AUTOFAILBACKSW: DISABLE
    add_updiamrtnexthop_list_2:
    - REALMNAME: 'huawei.com'
      APPLICATION: SWM
      NEXTHOP: 'dra01.huawei.com'
      SEQUENCE: 1
    set_updiameterpara_list_1:
    - REALMBASEROUTE: ENABLE
    add_upglbdiamrealm_list_1:
    - APPLICATION: SWM
      CONSTBYIMSISW: DISABLE
      REALM: 'huawei.com'
    add_apn_list_1:
    - APN: '032apn1.com'
    add_uprealmbindapn_list_1:
    - APN: '032apn1.com'
      APPLICATION: SWM
      CONSTBYIMSISW: DISABLE
      REALMNAME: 'huawei.com'
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 **任务1，TCP over DRA配置脚本：**

#### 1.1 创建VPN实例。可选配置，如果已配置VPN跳过此步骤。

```jinja2
{%- if is_scenario_tcp_over_dra -%}
    {%- for item in add_vpninst_list -%}
        ADD VPNINST:
        {#- --- 必选参数 --- -#}
        VPNINSTANCE="{{item.VPNINSTANCE}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_tcp_over_dra -%}
    {%- for item in add_l3vpninst_list -%}
        ADD L3VPNINST:
        {#- --- 必选参数 --- -#}
        VRFNAME="{{item.VRFNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_tcp_over_dra -%}
    {%- for item in add_vpninstaf_list -%}
        ADD VPNINSTAF:
        {#- --- 必选参数 --- -#}
        VRFNAME="{{item.VRFNAME}}",
        AFTYPE={{item.AFTYPE}},
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 1.2 配置SWm逻辑接口，VPN实例名称为VPN\_Signaling。

```jinja2
{%- if is_scenario_tcp_over_dra -%}
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
{%- endif -%}
```

#### 1.3 配置SWm接口的集中点模式为本端端口模式。

```jinja2
{%- if is_scenario_tcp_over_dra -%}
    {%- for item in set_upconcenpoint_list -%}
        SET UPCONCENPOINT:
        {#- --- 可选参数 --- -#}
        {%- if item.SWMCONCENMODE is not none -%}
            SWMCONCENMODE={{item.SWMCONCENMODE}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 1.4 配置DRA数据。配置DRA主机名以及地址信息。

```jinja2
{%- if is_scenario_tcp_over_dra -%}
    {%- for item in add_updra_list -%}
        ADD UPDRA:
        {#- --- 必选参数 --- -#}
        HOSTNAME="{{item.HOSTNAME}}",
        {#- --- 可选参数 --- -#}
        {%- if item.VPNINSTANCE is not none -%}
            VPNINSTANCE="{{item.VPNINSTANCE}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_tcp_over_dra -%}
    {%- for item in add_updiampeeraddr_list -%}
        ADD UPDIAMPEERADDR:
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
{%- endif -%}
```

#### 1.5 配置对接数据。

##### 1.5.1 配置本端端点的主机信息。

```jinja2
{%- if is_scenario_tcp_over_dra -%}
    {%- for item in add_updiamlocinfo_list -%}
        ADD UPDIAMLOCINFO:
        {#- --- 必选参数 --- -#}
        HOSTNAME="{{item.HOSTNAME}}",
        REALMNAME="{{item.REALMNAME}}",
        PRODUCTNAME="{{item.PRODUCTNAME}}",
        {#- --- 可选参数 --- -#}
        {%- if item.ORIGINSTATEID is not none -%}
            ORIGINSTATEID={{item.ORIGINSTATEID}},
        {%- endif -%}
        {%- if item.SUPPORTVENDORID is not none -%}
            SUPPORTVENDORID={{item.SUPPORTVENDORID}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 1.5.2 配置网元对接。

```jinja2
{%- if is_scenario_tcp_over_dra -%}
    {%- for item in add_updiamconngrp_list -%}
        ADD UPDIAMCONNGRP:
        {#- --- 必选参数 --- -#}
        CONNGROUPNAME="{{item.CONNGROUPNAME}}",
        LOCALHOSTNAME="{{item.LOCALHOSTNAME}}",
        APPLICATION={{item.APPLICATION}},
        PEERHOSTNAME="{{item.PEERHOSTNAME}}",
        {#- --- 可选参数 --- -#}
        {%- if item.SELECTMODE is not none -%}
            SELECTMODE={{item.SELECTMODE}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_tcp_over_dra -%}
    {%- for item in add_updiamconn_list -%}
        ADD UPDIAMCONN:
        {#- --- 必选参数 --- -#}
        DIAMCONNGRP="{{item.DIAMCONNGRP}}",
        LOCINTERFACE="{{item.LOCINTERFACE}}",
        {#- --- 可选参数 --- -#}
        {%- if item.PEERADDRTYPE is not none -%}
            PEERADDRTYPE={{item.PEERADDRTYPE}},
        {%- endif -%}
        {%- if item.LOCALPORT is not none -%}
            LOCALPORT={{item.LOCALPORT}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：PEERADDRTYPE=IPv4 时必选 --- -#}
        {%- if item.PEERADDRTYPE == 'IPv4' -%}
            PEERIPV4ADDR="{{item.PEERIPV4ADDR}}",
        {%- endif -%}
        {#- --- 条件必选：PEERADDRTYPE=IPv6 时必选 --- -#}
        {%- if item.PEERADDRTYPE == 'IPv6' -%}
            PEERIPV6ADDR="{{item.PEERIPV6ADDR}}",
        {%- endif -%}
        {#- --- 条件必选：PEERADDRTYPE=SCTP 时必选 --- -#}
        {%- if item.PEERADDRTYPE == 'SCTP' -%}
            PEERSCTPENDPT="{{item.PEERSCTPENDPT}}",
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：PEERADDRTYPE=IPv4/IPv6 时可选 --- -#}
        {%- if item.PEERADDRTYPE in ['IPv4', 'IPv6'] -%}
            {%- if item.PEERPORT is not none -%}
                PEERPORT={{item.PEERPORT}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PEERADDRTYPE=SCTP 时可选 --- -#}
        {%- if item.PEERADDRTYPE == 'SCTP' -%}
            {%- if item.REVERSEIP is not none -%}
                REVERSEIP={{item.REVERSEIP}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_tcp_over_dra -%}
    {%- for item in add_updiamrtrealm_list -%}
        ADD UPDIAMRTREALM:
        {#- --- 必选参数 --- -#}
        REALMNAME="{{item.REALMNAME}}",
        APPLICATION={{item.APPLICATION}},
        {#- --- 可选参数 --- -#}
        {%- if item.SELECTMODE is not none -%}
            SELECTMODE={{item.SELECTMODE}},
        {%- endif -%}
        {%- if item.FAILOVERSW is not none -%}
            FAILOVERSW={{item.FAILOVERSW}},
        {%- endif -%}
        {%- if item.AUTOFAILBACKSW is not none -%}
            AUTOFAILBACKSW={{item.AUTOFAILBACKSW}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_tcp_over_dra -%}
    {%- for item in add_updiamrtnexthop_list -%}
        ADD UPDIAMRTNEXTHOP:
        {#- --- 必选参数 --- -#}
        REALMNAME="{{item.REALMNAME}}",
        APPLICATION={{item.APPLICATION}},
        NEXTHOP="{{item.NEXTHOP}}",
        SEQUENCE={{item.SEQUENCE}},
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 1.6 配置会话激活路由选取方式。

##### 1.6.1 开启路由功能开关。

```jinja2
{%- if is_scenario_tcp_over_dra -%}
    {%- for item in set_updiameterpara_list -%}
        SET UPDIAMETERPARA:
        {#- --- 可选参数 --- -#}
        {%- if item.REALMBASEROUTE is not none -%}
            REALMBASEROUTE={{item.REALMBASEROUTE}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 1.6.2 选取路由。选取路由时，基于APN选路配置比基于全局配置的优先级高。

###### 1.6.2.1 基于全局配置选取路由。

```jinja2
{%- if is_scenario_tcp_over_dra -%}
    {%- for item in add_upglbdiamrealm_list -%}
        ADD UPGLBDIAMREALM:
        {#- --- 必选参数 --- -#}
        APPLICATION={{item.APPLICATION}},
        CONSTBYIMSISW={{item.CONSTBYIMSISW}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：CONSTBYIMSISW=DISABLE 时必选 --- -#}
        {%- if item.CONSTBYIMSISW == 'DISABLE' -%}
            REALM="{{item.REALM}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

###### 1.6.2.2 基于APN配置选取路由。

###### 增加APN。同一个APN只能配置TCP/SCTP中的一种场景，不允许两种场景同时配置到同一APN下。

```jinja2
{%- if is_scenario_tcp_over_dra -%}
    {%- for item in add_apn_list -%}
        ADD APN:
        {#- --- 必选参数 --- -#}
        APN="{{item.APN}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

###### 基于APN绑定关系选取路由。

```jinja2
{%- if is_scenario_tcp_over_dra -%}
    {%- for item in add_uprealmbindapn_list -%}
        ADD UPREALMBINDAPN:
        {#- --- 必选参数 --- -#}
        APN="{{item.APN}}",
        APPLICATION={{item.APPLICATION}},
        CONSTBYIMSISW={{item.CONSTBYIMSISW}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：CONSTBYIMSISW=DISABLE 时必选 --- -#}
        {%- if item.CONSTBYIMSISW == 'DISABLE' -%}
            REALMNAME="{{item.REALMNAME}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 2 **任务2，SCTP over DRA配置脚本：**

#### 2.1 创建VPN实例。可选配置，如果已配置VPN跳过此步骤。

```jinja2
{%- if is_scenario_sctp_over_dra -%}
    {%- for item in add_vpninst_list_1 -%}
        ADD VPNINST:
        {#- --- 必选参数 --- -#}
        VPNINSTANCE="{{item.VPNINSTANCE}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_sctp_over_dra -%}
    {%- for item in add_l3vpninst_list_1 -%}
        ADD L3VPNINST:
        {#- --- 必选参数 --- -#}
        VRFNAME="{{item.VRFNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_sctp_over_dra -%}
    {%- for item in add_vpninstaf_list_1 -%}
        ADD VPNINSTAF:
        {#- --- 必选参数 --- -#}
        VRFNAME="{{item.VRFNAME}}",
        AFTYPE={{item.AFTYPE}},
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 2.2 配置SWm逻辑接口，VPN实例名称为VPN\_Signaling。

```jinja2
{%- if is_scenario_sctp_over_dra -%}
    {%- for item in add_logicinf_list_1 -%}
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
        {#- --- 条件可选：IPVERSION=IPV4/IPVER_ALL/IPV6 时可选 --- -#}
        {%- if item.IPVERSION in ['IPV4', 'IPVER_ALL', 'IPV6'] -%}
            {%- if item.VPNINSTANCE is not none -%}
                VPNINSTANCE="{{item.VPNINSTANCE}}",
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
{%- endif -%}
```

#### 2.3 配置SWm接口的集中点模式为本端端口模式。

```jinja2
{%- if is_scenario_sctp_over_dra -%}
    {%- for item in set_upconcenpoint_list_1 -%}
        SET UPCONCENPOINT:
        {#- --- 可选参数 --- -#}
        {%- if item.SWMCONCENMODE is not none -%}
            SWMCONCENMODE={{item.SWMCONCENMODE}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 2.4 配置DRA数据。

##### 2.4.1 配置SCTP模板参数。

```jinja2
{%- if is_scenario_sctp_over_dra -%}
    {%- for item in add_upsctptemplate_list -%}
        ADD UPSCTPTEMPLATE:
        {#- --- 必选参数 --- -#}
        SCTPTEMPLNAME="{{item.SCTPTEMPLNAME}}",
        {#- --- 可选参数 --- -#}
        {%- if item.HEARTBEATINTVAL is not none -%}
            HEARTBEATINTVAL={{item.HEARTBEATINTVAL}},
        {%- endif -%}
        {%- if item.MAXASSOCRETRY is not none -%}
            MAXASSOCRETRY={{item.MAXASSOCRETRY}},
        {%- endif -%}
        {%- if item.MAXPATHRETRY is not none -%}
            MAXPATHRETRY={{item.MAXPATHRETRY}},
        {%- endif -%}
        {%- if item.CHECKSUMTYPE is not none -%}
            CHECKSUMTYPE={{item.CHECKSUMTYPE}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 2.4.2 配置SCTP端点信息，并将模板分别与SCTP端点绑定。

```jinja2
{%- if is_scenario_sctp_over_dra -%}
    {%- for item in add_upsctpendpoint_list -%}
        ADD UPSCTPENDPOINT:
        {#- --- 必选参数 --- -#}
        ENDPOINTNAME="{{item.ENDPOINTNAME}}",
        IPVERSION={{item.IPVERSION}},
        {#- --- 可选参数 --- -#}
        {%- if item.PORT is not none -%}
            PORT={{item.PORT}},
        {%- endif -%}
        {%- if item.SCTPTEMPLNAME is not none -%}
            SCTPTEMPLNAME="{{item.SCTPTEMPLNAME}}",
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：IPVERSION=IPV4 时必选 --- -#}
        {%- if item.IPVERSION == 'IPV4' -%}
            IPV4ADDRESS1="{{item.IPV4ADDRESS1}}",
        {%- endif -%}
        {#- --- 条件必选：IPVERSION=IPV6 时必选 --- -#}
        {%- if item.IPVERSION == 'IPV6' -%}
            IPV6ADDRESS1="{{item.IPV6ADDRESS1}}",
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：IPVERSION=IPV4 时可选 --- -#}
        {%- if item.IPVERSION == 'IPV4' -%}
            {%- if item.IPV4ADDRESS2 is not none -%}
                IPV4ADDRESS2="{{item.IPV4ADDRESS2}}",
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：IPVERSION=IPV6 时可选 --- -#}
        {%- if item.IPVERSION == 'IPV6' -%}
            {%- if item.IPV6ADDRESS2 is not none -%}
                IPV6ADDRESS2="{{item.IPV6ADDRESS2}}",
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 2.4.3 配置SCTP重传超时（RTO，Retransmission Time-Out）参数和SCTP偶联内使用路径的模式。

```jinja2
{%- if is_scenario_sctp_over_dra -%}
    {%- for item in set_upglbsctppara_list -%}
        SET UPGLBSCTPPARA:
        {#- --- 可选参数 --- -#}
        {%- if item.PATHSELECTMODE is not none -%}
            PATHSELECTMODE={{item.PATHSELECTMODE}},
        {%- endif -%}
        {%- if item.RTOMINVALUE is not none -%}
            RTOMINVALUE={{item.RTOMINVALUE}},
        {%- endif -%}
        {%- if item.RTOMAXVALUE is not none -%}
            RTOMAXVALUE={{item.RTOMAXVALUE}},
        {%- endif -%}
        {%- if item.RTOINITVALUE is not none -%}
            RTOINITVALUE={{item.RTOINITVALUE}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 2.4.4 配置DRA主机名以及地址信息。

```jinja2
{%- if is_scenario_sctp_over_dra -%}
    {%- for item in add_updra_list_2 -%}
        ADD UPDRA:
        {#- --- 必选参数 --- -#}
        HOSTNAME="{{item.HOSTNAME}}",
        {#- --- 可选参数 --- -#}
        {%- if item.VPNINSTANCE is not none -%}
            VPNINSTANCE="{{item.VPNINSTANCE}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_sctp_over_dra -%}
    {%- for item in add_updiampeeraddr_list_2 -%}
        ADD UPDIAMPEERADDR:
        {#- --- 必选参数 --- -#}
        HOSTNAME="{{item.HOSTNAME}}",
        ADDRTYPE={{item.ADDRTYPE}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：ADDRTYPE=SCTP 时必选 --- -#}
        {%- if item.ADDRTYPE == 'SCTP' -%}
            SCTPENDPOINT="{{item.SCTPENDPOINT}}",
        {%- endif -%}
        {#- --- 条件必选：ADDRTYPE=IPv4 时必选 --- -#}
        {%- if item.ADDRTYPE == 'IPv4' -%}
            IPV4ADDRESS="{{item.IPV4ADDRESS}}",
        {%- endif -%}
        {#- --- 条件必选：ADDRTYPE=IPv6 时必选 --- -#}
        {%- if item.ADDRTYPE == 'IPv6' -%}
            IPV6ADDRESS="{{item.IPV6ADDRESS}}",
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
{%- endif -%}
```

#### 2.5 配置对接数据。

##### 2.5.1 配置本端端点的主机信息。

```jinja2
{%- if is_scenario_sctp_over_dra -%}
    {%- for item in add_updiamlocinfo_list_1 -%}
        ADD UPDIAMLOCINFO:
        {#- --- 必选参数 --- -#}
        HOSTNAME="{{item.HOSTNAME}}",
        REALMNAME="{{item.REALMNAME}}",
        PRODUCTNAME="{{item.PRODUCTNAME}}",
        {#- --- 可选参数 --- -#}
        {%- if item.ORIGINSTATEID is not none -%}
            ORIGINSTATEID={{item.ORIGINSTATEID}},
        {%- endif -%}
        {%- if item.SUPPORTVENDORID is not none -%}
            SUPPORTVENDORID={{item.SUPPORTVENDORID}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 2.5.2 配置网元对接。

```jinja2
{%- if is_scenario_sctp_over_dra -%}
    {%- for item in add_updiamconngrp_list_2 -%}
        ADD UPDIAMCONNGRP:
        {#- --- 必选参数 --- -#}
        CONNGROUPNAME="{{item.CONNGROUPNAME}}",
        LOCALHOSTNAME="{{item.LOCALHOSTNAME}}",
        APPLICATION={{item.APPLICATION}},
        PEERHOSTNAME="{{item.PEERHOSTNAME}}",
        {#- --- 可选参数 --- -#}
        {%- if item.SELECTMODE is not none -%}
            SELECTMODE={{item.SELECTMODE}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_sctp_over_dra -%}
    {%- for item in add_updiamconn_list_2 -%}
        ADD UPDIAMCONN:
        {#- --- 必选参数 --- -#}
        DIAMCONNGRP="{{item.DIAMCONNGRP}}",
        LOCINTERFACE="{{item.LOCINTERFACE}}",
        {#- --- 可选参数 --- -#}
        {%- if item.PEERADDRTYPE is not none -%}
            PEERADDRTYPE={{item.PEERADDRTYPE}},
        {%- endif -%}
        {%- if item.LOCALPORT is not none -%}
            LOCALPORT={{item.LOCALPORT}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：PEERADDRTYPE=SCTP 时必选 --- -#}
        {%- if item.PEERADDRTYPE == 'SCTP' -%}
            PEERSCTPENDPT="{{item.PEERSCTPENDPT}}",
        {%- endif -%}
        {#- --- 条件必选：PEERADDRTYPE=IPv4 时必选 --- -#}
        {%- if item.PEERADDRTYPE == 'IPv4' -%}
            PEERIPV4ADDR="{{item.PEERIPV4ADDR}}",
        {%- endif -%}
        {#- --- 条件必选：PEERADDRTYPE=IPv6 时必选 --- -#}
        {%- if item.PEERADDRTYPE == 'IPv6' -%}
            PEERIPV6ADDR="{{item.PEERIPV6ADDR}}",
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：PEERADDRTYPE=SCTP 时可选 --- -#}
        {%- if item.PEERADDRTYPE == 'SCTP' -%}
            {%- if item.REVERSEIP is not none -%}
                REVERSEIP={{item.REVERSEIP}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PEERADDRTYPE=IPv4/IPv6 时可选 --- -#}
        {%- if item.PEERADDRTYPE in ['IPv4', 'IPv6'] -%}
            {%- if item.PEERPORT is not none -%}
                PEERPORT={{item.PEERPORT}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_sctp_over_dra -%}
    {%- for item in add_updiamrtrealm_list_1 -%}
        ADD UPDIAMRTREALM:
        {#- --- 必选参数 --- -#}
        REALMNAME="{{item.REALMNAME}}",
        APPLICATION={{item.APPLICATION}},
        {#- --- 可选参数 --- -#}
        {%- if item.SELECTMODE is not none -%}
            SELECTMODE={{item.SELECTMODE}},
        {%- endif -%}
        {%- if item.FAILOVERSW is not none -%}
            FAILOVERSW={{item.FAILOVERSW}},
        {%- endif -%}
        {%- if item.AUTOFAILBACKSW is not none -%}
            AUTOFAILBACKSW={{item.AUTOFAILBACKSW}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_sctp_over_dra -%}
    {%- for item in add_updiamrtnexthop_list_2 -%}
        ADD UPDIAMRTNEXTHOP:
        {#- --- 必选参数 --- -#}
        REALMNAME="{{item.REALMNAME}}",
        APPLICATION={{item.APPLICATION}},
        NEXTHOP="{{item.NEXTHOP}}",
        SEQUENCE={{item.SEQUENCE}},
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 2.6 配置会话激活路由选取方式。

##### 2.6.1 开启路由功能开关。

```jinja2
{%- if is_scenario_sctp_over_dra -%}
    {%- for item in set_updiameterpara_list_1 -%}
        SET UPDIAMETERPARA:
        {#- --- 可选参数 --- -#}
        {%- if item.REALMBASEROUTE is not none -%}
            REALMBASEROUTE={{item.REALMBASEROUTE}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 2.6.2 选取路由。选取路由时，基于APN选路配置比基于全局配置的优先级高。

###### 2.6.2.1 基于全局配置选取路由。

```jinja2
{%- if is_scenario_sctp_over_dra -%}
    {%- for item in add_upglbdiamrealm_list_1 -%}
        ADD UPGLBDIAMREALM:
        {#- --- 必选参数 --- -#}
        APPLICATION={{item.APPLICATION}},
        CONSTBYIMSISW={{item.CONSTBYIMSISW}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：CONSTBYIMSISW=DISABLE 时必选 --- -#}
        {%- if item.CONSTBYIMSISW == 'DISABLE' -%}
            REALM="{{item.REALM}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

###### 2.6.2.2 基于APN配置选取路由。

###### 增加APN。同一个APN只能配置TCP/SCTP中的一种场景，不允许两种场景同时配置到同一APN下。

```jinja2
{%- if is_scenario_sctp_over_dra -%}
    {%- for item in add_apn_list_1 -%}
        ADD APN:
        {#- --- 必选参数 --- -#}
        APN="{{item.APN}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

###### 基于APN绑定关系选取路由。

```jinja2
{%- if is_scenario_sctp_over_dra -%}
    {%- for item in add_uprealmbindapn_list_1 -%}
        ADD UPREALMBINDAPN:
        {#- --- 必选参数 --- -#}
        APN="{{item.APN}}",
        APPLICATION={{item.APPLICATION}},
        CONSTBYIMSISW={{item.CONSTBYIMSISW}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：CONSTBYIMSISW=DISABLE 时必选 --- -#}
        {%- if item.CONSTBYIMSISW == 'DISABLE' -%}
            REALMNAME="{{item.REALMNAME}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```


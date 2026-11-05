---
id: ''
name: 配置SWm接口对接数据（DRA转接）
ne_type: UNC
type: feature
description: UPF与Non-SIM AAA UDM-UIM间存在直连、非直连路径。图1表示经DRA的非直连路径。  **图1** DRA组网  当UPF与Non-SIM AAA之间直连路径故障或者未配置直连路径时，可以配置到DRA，DRA在UPF与Non-SIM AAA间转交消息，提供非3GPP鉴权认证功能。UPF与Non-SIM AAA交互时，优先选择直连路径发送消息。  * SWm接口当前版本仅支持IPv4栈类型。 * 专网UPF配置SWm接口时，不支持开启入不转板功能特性。
risk_level: ''
doc_source: ["网络部署","业务专题","5G Core 一跳入家解决方案","一跳入家解决方案（基于非3GPP接入方案）","业务初始部署与调测","部署一跳入家","配置一跳入家专网UPF","配置SWm接口对接数据（DRA转接）"]
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
          minLength: 1
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
    set_upconcenpoint_list:
      type: items
      properties:
        SWMCONCENMODE:
          name: 'Swm集中点模式'
          type: string
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
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        VPNINSTANCE:
          name: 'VPN实例'
          type: string
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
          required: false
          description: '-'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        ADDRTYPE:
          name: '地址类型'
          type: string
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPV4ADDRESS:
          name: 'IPv4地址'
          type: string
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        PORT:
          name: 'PORT'
          type: string
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
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        REALMNAME:
          name: '本端域名'
          type: string
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PRODUCTNAME:
          name: '产品名称'
          type: string
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        ORIGINSTATEID:
          name: 'ORIGINSTATEID'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SUPPORTVENDORID:
          name: 'SUPPORTVENDORID'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_updiamconngrp_list:
      type: items
      properties:
        CONNGROUPNAME:
          name: 'Diameter链路组名'
          type: string
          required: false
          description: '该命令用于指定本端主机名与指定对端服务器之间建立一组Diameter链路。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        LOCALHOSTNAME:
          name: '本端主机名'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        APPLICATION:
          name: 'Diameter应用'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        PEERHOSTNAME:
          name: '对端主机名'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        SELECTMODE:
          name: '链路选择模式'
          type: string
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_updiamconn_list:
      type: items
      properties:
        DIAMCONNGRP:
          name: 'Diameter链路组名'
          type: string
          required: false
          description: '增加Diameter链路。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        LOCINTERFACE:
          name: '本端接口名'
          type: string
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        PEERADDRTYPE:
          name: '对端地址类型'
          type: string
          required: false
          description: '*-*'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PEERIPV4ADDR:
          name: '对端IPV4地址'
          type: string
          required: false
          description: 'IPv4地址类型。不支持0.0.0.0和255.255.255.255。'
          data_source: '对端协商'
          pattern: ''
          default: ''
        PEERPORT:
          name: '对端端口'
          type: string
          required: false
          description: '*-*'
          data_source: '对端协商'
          pattern: ''
          default: ''
        LOCALPORT:
          name: '本端端口'
          type: string
          required: false
          description: '取值范围19865~19928。'
          data_source: '对端协商'
          pattern: ''
          default: ''
    add_updiamrtrealm_list:
      type: items
      properties:
        REALMNAME:
          name: 'Diameter域名名称'
          type: string
          required: false
          description: '-'
          data_source: '与对端协商'
          pattern: ''
          default: ''
        APPLICATION:
          name: 'Diameter应用'
          type: string
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        SELECTMODE:
          name: '路由选择模式'
          type: string
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        FAILOVERSW:
          name: 'FAILOVERSW'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AUTOFAILBACKSW:
          name: 'AUTOFAILBACKSW'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_updiamrtnexthop_list:
      type: items
      properties:
        REALMNAME:
          name: 'Diameter域名名称'
          type: string
          required: false
          description: '说明：  下一跳的主机名“HOSTNAME”只允许设置成已配置的DRA主机名。'
          data_source: '与对端协商'
          pattern: ''
          default: ''
        APPLICATION:
          name: 'Diameter应用'
          type: string
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        NEXTHOP:
          name: '下一跳'
          type: string
          required: false
          description: '-'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        SEQUENCE:
          name: '序号'
          type: string
          required: false
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
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        CONSTBYIMSISW:
          name: 'CONSTBYIMSISW'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        REALM:
          name: 'Diameter域名'
          type: string
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
          minLength: 1
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
          required: false
          description: '已通过命令**ADD APN**进行配置，可以使用命令**LST APN**查询。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        APPLICATION:
          name: 'Diameter应用'
          type: string
          required: false
          description: '-'
          data_source: '与对端协商'
          pattern: ''
          default: ''
        CONSTBYIMSISW:
          name: '根据IMSI构造归属地Realm开关'
          type: string
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        REALMNAME:
          name: 'Realm名'
          type: string
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
          minLength: 1
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
          maxLength: 31
          required: false
          description: '-'
          data_source: '全网规划'
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
    set_upconcenpoint_list_1:
      type: items
      properties:
        SWMCONCENMODE:
          name: 'Swm集中点模式'
          type: string
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
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        HEARTBEATINTVAL:
          name: 'SCTP发送心跳消息的间隔周期（毫秒）'
          type: string
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        MAXASSOCRETRY:
          name: 'SCTP耦联上消息重传的最大次数'
          type: string
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        MAXPATHRETRY:
          name: 'SCTP到特定IP消息重传的最大次数'
          type: string
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        CHECKSUMTYPE:
          name: 'SCTP协议校验和算法'
          type: string
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_upsctpendpoint_list:
      type: items
      properties:
        ENDPOINTNAME:
          name: '端点名称'
          type: string
          required: false
          description: '定义两个端点为“endpoint0”和“endpoint1”，每个端点有两个IP地址，端点“endpoint0”的IP地址为192.168.10.1和192.168.10.2，端点“endpoint1”的IP地址为192.168.20.1和192.168.20.2。端口号均为3868。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPVERSION:
          name: 'IP版本'
          type: string
          required: false
          description: ''
          data_source: '与对端协商'
          pattern: ''
          default: ''
        IPV4ADDRESS1:
          name: 'IPv4地址1'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV4ADDRESS2:
          name: 'IPv4地址2'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        PORT:
          name: '端口号'
          type: string
          required: false
          description: ''
          data_source: '与对端协商'
          pattern: ''
          default: ''
        SCTPTEMPLNAME:
          name: 'SCTP模板名称'
          type: string
          required: false
          description: '已通过**ADD SCTPTEMPLATE**命令配置，可以使用**LST SCTPTEMPLATE**命令查询。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    set_upglbsctppara_list:
      type: items
      properties:
        PATHSELECTMODE:
          name: 'SCTP路径选择模式'
          type: string
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        RTOMINVALUE:
          name: 'RTO重发超时的最小值（毫秒）'
          type: string
          required: false
          description: '-'
          data_source: '与对端协商'
          pattern: ''
          default: ''
        RTOMAXVALUE:
          name: 'RTO重发超时的最大值（毫秒）'
          type: string
          required: false
          description: '-'
          data_source: '与对端协商'
          pattern: ''
          default: ''
        RTOINITVALUE:
          name: 'RTO重发超时的初始值（毫秒）'
          type: string
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
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        VPNINSTANCE:
          name: 'VPN实例'
          type: string
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
          required: false
          description: '-'
          data_source: '与对端协商'
          pattern: ''
          default: ''
        ADDRTYPE:
          name: '地址类型'
          type: string
          required: false
          description: '-'
          data_source: '与对端协商'
          pattern: ''
          default: ''
        SCTPENDPOINT:
          name: 'SCTP端点名称'
          type: string
          required: false
          description: '-'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_updiamlocinfo_list_1:
      type: items
      properties:
        HOSTNAME:
          name: '本端主机名'
          type: string
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        REALMNAME:
          name: '本端域名'
          type: string
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PRODUCTNAME:
          name: '产品名称'
          type: string
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        ORIGINSTATEID:
          name: 'ORIGINSTATEID'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SUPPORTVENDORID:
          name: 'SUPPORTVENDORID'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_updiamconngrp_list_2:
      type: items
      properties:
        CONNGROUPNAME:
          name: 'Diameter链路组名'
          type: string
          required: false
          description: '该命令用于指定本端主机名与指定对端服务器之间建立一组Diameter链路。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        LOCALHOSTNAME:
          name: '本端主机名'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        APPLICATION:
          name: 'Diameter应用'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        PEERHOSTNAME:
          name: '对端主机名'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        SELECTMODE:
          name: '链路选择模式'
          type: string
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_updiamconn_list_2:
      type: items
      properties:
        DIAMCONNGRP:
          name: 'Diameter链路组名'
          type: string
          required: false
          description: '增加Diameter链路。  已经通过**ADD LOGICINF**命令配置，可以使用**LST LOGICINF**查询。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        LOCINTERFACE:
          name: '本端接口名'
          type: string
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        LOCALPORT:
          name: '本端端口'
          type: string
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PEERSCTPENDPT:
          name: '对端SCTP端点名称'
          type: string
          required: false
          description: 'SCTP端点已通过**ADD SCTPENDPOINT**命令配置，可以使用**LST SCTPENDPOINT**查询。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        PEERADDRTYPE:
          name: '对端地址类型'
          type: string
          required: false
          description: '-'
          data_source: '与对端协商'
          pattern: ''
          default: ''
        REVERSEIP:
          name: 'SCTP建链交换本端IP地址'
          type: string
          required: false
          description: '-'
          data_source: '与对端协商'
          pattern: ''
          default: ''
    add_updiamrtrealm_list_1:
      type: items
      properties:
        REALMNAME:
          name: 'iameter域名名称'
          type: string
          required: false
          description: '-'
          data_source: '与对端协商'
          pattern: ''
          default: ''
        APPLICATION:
          name: 'Diameter应用'
          type: string
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        SELECTMODE:
          name: '路由选择模式'
          type: string
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        FAILOVERSW:
          name: 'FAILOVERSW'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AUTOFAILBACKSW:
          name: 'AUTOFAILBACKSW'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_updiamrtnexthop_list_2:
      type: items
      properties:
        REALMNAME:
          name: 'Diameter域名名称'
          type: string
          required: false
          description: '说明：  下一跳的主机名“HOSTNAME”只允许设置成已配置的DRA主机名。'
          data_source: '与对端协商'
          pattern: ''
          default: ''
        APPLICATION:
          name: 'Diameter应用'
          type: string
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        NEXTHOP:
          name: '下一跳'
          type: string
          required: false
          description: '-'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        SEQUENCE:
          name: '序号'
          type: string
          required: false
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
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        CONSTBYIMSISW:
          name: 'CONSTBYIMSISW'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        REALM:
          name: 'Diameter域名'
          type: string
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
          minLength: 1
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
          required: false
          description: '已通过命令**ADD APN**进行配置，可以使用命令**LST APN**查询。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        APPLICATION:
          name: 'Diameter应用'
          type: string
          required: false
          description: '-'
          data_source: '与对端协商'
          pattern: ''
          default: ''
        CONSTBYIMSISW:
          name: '根据IMSI构造归属地Realm开关'
          type: string
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        REALMNAME:
          name: 'Realm名'
          type: string
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
      IPV6ADDRESS1: ''
      IPV6ADDRESS2: ''
      IPV6PREFIXLEN1: ''
      IPV6PREFIXLEN2: ''
    set_upconcenpoint_list:
    - SWMCONCENMODE: LOCALPORT
    add_updra_list:
    - HOSTNAME: dra01.huawei.com
      VPNINSTANCE: VPN_Signaling
    add_updiampeeraddr_list:
    - HOSTNAME: dra01.huawei.com
      ADDRTYPE: IPv4
      IPV4ADDRESS: 172.17.251.66
      PORT: '3868'
    add_updiamlocinfo_list:
    - HOSTNAME: udg_1
      REALMNAME: peer.huawei.com
      PRODUCTNAME: udg@huawei.com
      ORIGINSTATEID: DISABLE
      SUPPORTVENDORID: DISABLE
    add_updiamconngrp_list:
    - CONNGROUPNAME: udgaaagrp1
      LOCALHOSTNAME: udg_1
      APPLICATION: SWM
      PEERHOSTNAME: dra01.huawei.com
      SELECTMODE: SESSION_ID
    add_updiamconn_list:
    - DIAMCONNGRP: udgaaagrp1
      LOCINTERFACE: swmif1/0/0
      PEERADDRTYPE: IPv4
      PEERIPV4ADDR: 172.16.251.66
      PEERPORT: '3868'
      LOCALPORT: '19865'
    add_updiamrtrealm_list:
    - REALMNAME: huawei.com
      APPLICATION: SWM
      SELECTMODE: SESSION_ID
      FAILOVERSW: DISABLE
      AUTOFAILBACKSW: DISABLE
    add_updiamrtnexthop_list:
    - REALMNAME: huawei.com
      APPLICATION: SWM
      NEXTHOP: dra01.huawei.com
      SEQUENCE: '1'
    set_updiameterpara_list:
    - REALMBASEROUTE: ENABLE
    add_upglbdiamrealm_list:
    - APPLICATION: SWM
      CONSTBYIMSISW: DISABLE
      REALM: huawei.com
    add_apn_list:
    - APN: '032apn1.com'
    add_uprealmbindapn_list:
    - APN: 032apn1.com
      APPLICATION: SWM
      CONSTBYIMSISW: DISABLE
      REALMNAME: huawei.com
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
      IPV6ADDRESS1: ''
      IPV6ADDRESS2: ''
      IPV6PREFIXLEN1: ''
      IPV6PREFIXLEN2: ''
    set_upconcenpoint_list_1:
    - SWMCONCENMODE: LOCALPORT
    add_upsctptemplate_list:
    - SCTPTEMPLNAME: dra_template
      HEARTBEATINTVAL: '30000'
      MAXASSOCRETRY: '5'
      MAXPATHRETRY: '4'
      CHECKSUMTYPE: CRC32
    add_upsctpendpoint_list:
    - ENDPOINTNAME: endpoint0
      IPVERSION: IPV4
      IPV4ADDRESS1: 192.168.10.1
      IPV4ADDRESS2: 192.168.10.2
      PORT: '3868'
      SCTPTEMPLNAME: dra_template
    set_upglbsctppara_list:
    - PATHSELECTMODE: ALL
      RTOMINVALUE: '500'
      RTOMAXVALUE: '1500'
      RTOINITVALUE: '500'
    add_updra_list_2:
    - HOSTNAME: dra01.huawei.com
      VPNINSTANCE: VPN_Signaling
    add_updiampeeraddr_list_2:
    - HOSTNAME: dra01.huawei.com
      ADDRTYPE: SCTP
      SCTPENDPOINT: endpoint0
    add_updiamlocinfo_list_1:
    - HOSTNAME: udg_1
      REALMNAME: peer.huawei.com
      PRODUCTNAME: udg@huawei.com
      ORIGINSTATEID: DISABLE
      SUPPORTVENDORID: DISABLE
    add_updiamconngrp_list_2:
    - CONNGROUPNAME: udgaaagrp1
      LOCALHOSTNAME: udg_1
      APPLICATION: SWM
      PEERHOSTNAME: dra01.huawei.com
      SELECTMODE: SESSION_ID
    add_updiamconn_list_2:
    - DIAMCONNGRP: udgaaagrp1
      LOCINTERFACE: swmif1/0/0
      LOCALPORT: '19865'
      PEERSCTPENDPT: endpoint0
      PEERADDRTYPE: SCTP
      REVERSEIP: DISABLE
    add_updiamrtrealm_list_1:
    - REALMNAME: huawei.com
      APPLICATION: SWM
      SELECTMODE: SESSION_ID
      FAILOVERSW: DISABLE
      AUTOFAILBACKSW: DISABLE
    add_updiamrtnexthop_list_2:
    - REALMNAME: huawei.com
      APPLICATION: SWM
      NEXTHOP: dra01.huawei.com
      SEQUENCE: '1'
    set_updiameterpara_list_1:
    - REALMBASEROUTE: ENABLE
    add_upglbdiamrealm_list_1:
    - APPLICATION: SWM
      CONSTBYIMSISW: DISABLE
      REALM: huawei.com
    add_apn_list_1:
    - APN: '032apn1.com'
    add_uprealmbindapn_list_1:
    - APN: 032apn1.com
      APPLICATION: SWM
      CONSTBYIMSISW: DISABLE
      REALMNAME: huawei.com
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 **任务1，TCP over DRA配置脚本：**

#### 1.1 创建VPN实例。可选配置，如果已配置VPN跳过此步骤。

```jinja2
{%- if is_optional_create_vpn and is_scenario_tcp -%}
    {%- for item in add_vpninst_list -%}
        ADD VPNINST:
        {#- --- 必选参数 --- -#}
        VPNINSTANCE="{{item.VPNINSTANCE}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_optional_create_vpn and is_scenario_tcp -%}
    {%- for item in add_l3vpninst_list -%}
        ADD L3VPNINST:
        {#- --- 必选参数 --- -#}
        VRFNAME="{{item.VRFNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_optional_create_vpn and is_scenario_tcp -%}
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
{%- if is_scenario_tcp -%}
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
{%- endif -%}
```

#### 1.3 配置SWm接口的集中点模式为本端端口模式。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_upconcenpoint_list的变量区（command: SET UPCONCENPOINT） -#}
<!-- MISSING_MACRO: command=SET UPCONCENPOINT list_name=set_upconcenpoint_list step_id=1.3 -->
```

#### 1.4 配置DRA数据。配置DRA主机名以及地址信息。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_updra_list的变量区（command: ADD UPDRA） -#}
<!-- MISSING_MACRO: command=ADD UPDRA list_name=add_updra_list step_id=1.4 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_updiampeeraddr_list的变量区（command: ADD UPDIAMPEERADDR） -#}
<!-- MISSING_MACRO: command=ADD UPDIAMPEERADDR list_name=add_updiampeeraddr_list step_id=1.4 -->
```

#### 1.5 配置对接数据。

##### 1.5.1 配置本端端点的主机信息。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_updiamlocinfo_list的变量区（command: ADD UPDIAMLOCINFO） -#}
<!-- MISSING_MACRO: command=ADD UPDIAMLOCINFO list_name=add_updiamlocinfo_list step_id=1.5.1 -->
```

##### 1.5.2 配置网元对接。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_updiamconngrp_list的变量区（command: ADD UPDIAMCONNGRP） -#}
<!-- MISSING_MACRO: command=ADD UPDIAMCONNGRP list_name=add_updiamconngrp_list step_id=1.5.2 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_updiamconn_list的变量区（command: ADD UPDIAMCONN） -#}
<!-- MISSING_MACRO: command=ADD UPDIAMCONN list_name=add_updiamconn_list step_id=1.5.2 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_updiamrtrealm_list的变量区（command: ADD UPDIAMRTREALM） -#}
<!-- MISSING_MACRO: command=ADD UPDIAMRTREALM list_name=add_updiamrtrealm_list step_id=1.5.2 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_updiamrtnexthop_list的变量区（command: ADD UPDIAMRTNEXTHOP） -#}
<!-- MISSING_MACRO: command=ADD UPDIAMRTNEXTHOP list_name=add_updiamrtnexthop_list step_id=1.5.2 -->
```

#### 1.6 配置会话激活路由选取方式。

##### 1.6.1 开启路由功能开关。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_updiameterpara_list的变量区（command: SET UPDIAMETERPARA） -#}
<!-- MISSING_MACRO: command=SET UPDIAMETERPARA list_name=set_updiameterpara_list step_id=1.6.1 -->
```

##### 1.6.2 选取路由。选取路由时，基于APN选路配置比基于全局配置的优先级高。

###### 1.6.2.1 基于全局配置选取路由。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_upglbdiamrealm_list的变量区（command: ADD UPGLBDIAMREALM） -#}
<!-- MISSING_MACRO: command=ADD UPGLBDIAMREALM list_name=add_upglbdiamrealm_list step_id=1.6.2.1 -->
```

###### 1.6.2.2 基于APN配置选取路由。

###### 增加APN。同一个APN只能配置TCP/SCTP中的一种场景，不允许两种场景同时配置到同一APN下。

```jinja2
{%- if is_scenario_tcp -%}
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
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_uprealmbindapn_list的变量区（command: ADD UPREALMBINDAPN） -#}
<!-- MISSING_MACRO: command=ADD UPREALMBINDAPN list_name=add_uprealmbindapn_list step_id=1.6.2.2 -->
```

### 2 **任务2，SCTP over DRA配置脚本：**

#### 2.1 创建VPN实例。可选配置，如果已配置VPN跳过此步骤。

```jinja2
{%- if is_optional_create_vpn and is_scenario_sctp -%}
    {%- for item in add_vpninst_list_1 -%}
        ADD VPNINST:
        {#- --- 必选参数 --- -#}
        VPNINSTANCE="{{item.VPNINSTANCE}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_optional_create_vpn and is_scenario_sctp -%}
    {%- for item in add_l3vpninst_list_1 -%}
        ADD L3VPNINST:
        {#- --- 必选参数 --- -#}
        VRFNAME="{{item.VRFNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_optional_create_vpn and is_scenario_sctp -%}
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
{%- if is_scenario_sctp -%}
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
        {#- --- 条件必选：IPVERSION=IPV6/IPVER_ALL 时必选 --- -#}
        {%- if item.IPVERSION in ['IPV6', 'IPVER_ALL'] -%}
            IPV6ADDRESS1="{{item.IPV6ADDRESS1}}",
        {%- endif -%}
        {#- --- 条件必选：IPVERSION=IPV6/IPVER_ALL 时必选 --- -#}
        {%- if item.IPVERSION in ['IPV6', 'IPVER_ALL'] -%}
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
        {#- --- 条件可选：IPVERSION=IPV4/IPV6/IPVER_ALL 时可选 --- -#}
        {%- if item.IPVERSION in ['IPV4', 'IPV6', 'IPVER_ALL'] -%}
            {%- if item.VPNINSTANCE is not none -%}
                VPNINSTANCE="{{item.VPNINSTANCE}}",
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
{%- endif -%}
```

#### 2.3 配置SWm接口的集中点模式为本端端口模式。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_upconcenpoint_list_1的变量区（command: SET UPCONCENPOINT） -#}
<!-- MISSING_MACRO: command=SET UPCONCENPOINT list_name=set_upconcenpoint_list_1 step_id=2.3 -->
```

#### 2.4 配置DRA数据。

##### 2.4.1 配置SCTP模板参数。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_upsctptemplate_list的变量区（command: ADD UPSCTPTEMPLATE） -#}
<!-- MISSING_MACRO: command=ADD UPSCTPTEMPLATE list_name=add_upsctptemplate_list step_id=2.4.1 -->
```

##### 2.4.2 配置SCTP端点信息，并将模板分别与SCTP端点绑定。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_upsctpendpoint_list的变量区（command: ADD UPSCTPENDPOINT） -#}
<!-- MISSING_MACRO: command=ADD UPSCTPENDPOINT list_name=add_upsctpendpoint_list step_id=2.4.2 -->
```

##### 2.4.3 配置SCTP重传超时（RTO，Retransmission Time-Out）参数和SCTP偶联内使用路径的模式。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_upglbsctppara_list的变量区（command: SET UPGLBSCTPPARA） -#}
<!-- MISSING_MACRO: command=SET UPGLBSCTPPARA list_name=set_upglbsctppara_list step_id=2.4.3 -->
```

##### 2.4.4 配置DRA主机名以及地址信息。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_updra_list_2的变量区（command: ADD UPDRA） -#}
<!-- MISSING_MACRO: command=ADD UPDRA list_name=add_updra_list_2 step_id=2.4.4 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_updiampeeraddr_list_2的变量区（command: ADD UPDIAMPEERADDR） -#}
<!-- MISSING_MACRO: command=ADD UPDIAMPEERADDR list_name=add_updiampeeraddr_list_2 step_id=2.4.4 -->
```

#### 2.5 配置对接数据。

##### 2.5.1 配置本端端点的主机信息。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_updiamlocinfo_list_1的变量区（command: ADD UPDIAMLOCINFO） -#}
<!-- MISSING_MACRO: command=ADD UPDIAMLOCINFO list_name=add_updiamlocinfo_list_1 step_id=2.5.1 -->
```

##### 2.5.2 配置网元对接。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_updiamconngrp_list_2的变量区（command: ADD UPDIAMCONNGRP） -#}
<!-- MISSING_MACRO: command=ADD UPDIAMCONNGRP list_name=add_updiamconngrp_list_2 step_id=2.5.2 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_updiamconn_list_2的变量区（command: ADD UPDIAMCONN） -#}
<!-- MISSING_MACRO: command=ADD UPDIAMCONN list_name=add_updiamconn_list_2 step_id=2.5.2 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_updiamrtrealm_list_1的变量区（command: ADD UPDIAMRTREALM） -#}
<!-- MISSING_MACRO: command=ADD UPDIAMRTREALM list_name=add_updiamrtrealm_list_1 step_id=2.5.2 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_updiamrtnexthop_list_2的变量区（command: ADD UPDIAMRTNEXTHOP） -#}
<!-- MISSING_MACRO: command=ADD UPDIAMRTNEXTHOP list_name=add_updiamrtnexthop_list_2 step_id=2.5.2 -->
```

#### 2.6 配置会话激活路由选取方式。

##### 2.6.1 开启路由功能开关。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_updiameterpara_list_1的变量区（command: SET UPDIAMETERPARA） -#}
<!-- MISSING_MACRO: command=SET UPDIAMETERPARA list_name=set_updiameterpara_list_1 step_id=2.6.1 -->
```

##### 2.6.2 选取路由。选取路由时，基于APN选路配置比基于全局配置的优先级高。

###### 2.6.2.1 基于全局配置选取路由。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_upglbdiamrealm_list_1的变量区（command: ADD UPGLBDIAMREALM） -#}
<!-- MISSING_MACRO: command=ADD UPGLBDIAMREALM list_name=add_upglbdiamrealm_list_1 step_id=2.6.2.1 -->
```

###### 2.6.2.2 基于APN配置选取路由。

###### 增加APN。同一个APN只能配置TCP/SCTP中的一种场景，不允许两种场景同时配置到同一APN下。

```jinja2
{%- if is_scenario_sctp -%}
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
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_uprealmbindapn_list_1的变量区（command: ADD UPREALMBINDAPN） -#}
<!-- MISSING_MACRO: command=ADD UPREALMBINDAPN list_name=add_uprealmbindapn_list_1 step_id=2.6.2.2 -->
```


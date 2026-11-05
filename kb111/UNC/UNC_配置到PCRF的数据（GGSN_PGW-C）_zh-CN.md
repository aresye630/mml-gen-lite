---
id: ''
name: 配置到PCRF的数据（GGSN/PGW-C）
ne_type: UNC
type: feature
description: 当部署PCC基本功能，实现通过PCRF为用户指定控制策略，则需要配置UNC到PCRF的互通数据。  适用于GGSN、PGW-C。
risk_level: ''
doc_source: ["网络部署","初始配置","UNC初始配置与调测","组网对接配置","配置SMF&PGW-C&SGW-C&GGSN","公共配置","配置到计费系统和策略控制网元的对接（Ga/Gy/N40/Gx/N7）","配置到PCRF的数据（GGSN/PGW-C）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
当部署PCC基本功能，实现通过PCRF为用户指定控制策略，则需要配置UNC到PCRF的互通数据。适用于GGSN、PGW-C。

## 必备事项
前提条件

* 操作员了解UNC与对端网元互通时可以采用的各种组网方式，以及每种组网方式的实现及特点等信息。
* 如果运营商规划采用VPN组网方式，则操作员在执行本操作前应已创建了相应的VPN实例。
* 需要配置逻辑接口的PBU正常运行，且PBU上无用户存在。当PBU还未启动或正在启动过程中，将无法在该PBU上配置逻辑接口。
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
          description: '创建VPN实例。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    set_concenpoint_list:
      type: items
      properties:
        GXCONCENMODE:
          name: 'Gx集中点模式'
          type: string
          enum:
          - LOCALIP_PEER
          - LOCALPORT
          required: false
          description: '配置Diameter应用集中点模式。'
          data_source: '本端规划'
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
          description: '配置Gx接口逻辑IP地址。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        LOGICIPV4:
          name: 'IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        VPNINSTNAME:
          name: 'VPN实例名称'
          type: string
          minLength: 1
          maxLength: 31
          required: false
          description: ''
          data_source: '全网规划'
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
          description: '配置组级Gx逻辑接口。'
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
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPV4ADDRESS1:
          name: '逻辑接口的IPv4地址1'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV4MASK1:
          name: '逻辑接口的IPv4掩码1'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
        VPNINSTANCE:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: false
          description: '已通过命令**ADD VPNINST**配置，可以使用**LST VPNINST**命令进行查询。'
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
    add_logicip_list_1:
      type: items
      properties:
        IPVERSION:
          name: 'IP地址类型'
          type: string
          enum:
          - IPv4
          - IPv6
          required: true
          description: '配置Gx接口逻辑IP地址。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        LOGICIPV4:
          name: 'IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        VPNINSTNAME:
          name: 'VPN实例名称'
          type: string
          minLength: 1
          maxLength: 31
          required: false
          description: ''
          data_source: '全网规划'
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
    add_logicinf_list_1:
      type: items
      properties:
        NAME:
          name: '逻辑接口名称'
          type: string
          maxLength: 63
          required: true
          description: '配置组级Gx逻辑接口。'
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
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPV4ADDRESS1:
          name: '逻辑接口的IPv4地址1'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV4MASK1:
          name: '逻辑接口的IPv4掩码1'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
        VPNINSTANCE:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: false
          description: '已通过命令**ADD VPNINST**配置，可以使用**LST VPNINST**命令进行查询。'
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
    add_diamlocinfo_list:
      type: items
      properties:
        HOSTNAME:
          name: '本端主机名'
          type: string
          maxLength: 127
          required: true
          description: '配置GGSN/PGW-C的本端信息。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        REALMNAME:
          name: '本端域名'
          type: string
          maxLength: 127
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        PRODUCTNAME:
          name: '产品名称'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_pcrf_list:
      type: items
      properties:
        HOSTNAME:
          name: 'PCRF主机名'
          type: string
          maxLength: 127
          required: true
          description: '配置PCRF信息。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        REALMNAME:
          name: 'PCRF域名'
          type: string
          maxLength: 127
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        VPNINSTANCE:
          name: 'VPN实例'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        SUPFEANEGOSW:
          name: 'Supported-Features动态协商开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '与对端协商'
          pattern: ''
          default: DISABLE
        FEATURELIST:
          name: 'Feature列表'
          type: string
          required: false
          description: ''
          data_source: '与对端协商'
          pattern: ''
          default: ''
        CARRYSUPFEASW:
          name: 'Supported-Feature AVP携带开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ENABLE
    add_diampeeraddr_list:
      type: items
      properties:
        HOSTNAME:
          name: '主机名称'
          type: string
          maxLength: 127
          required: true
          description: '增加Diameter链路对端的地址信息，配置Diameter链路对端的地址类型、IP、端口号或端点信息。'
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
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPV4ADDRESS:
          name: 'IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
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
        SCTPENDPOINT:
          name: 'SCTP端点名称'
          type: string
          maxLength: 63
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_diamconngrp_list:
      type: items
      properties:
        CONNGROUPNAME:
          name: 'Diameter链路组名'
          type: string
          maxLength: 31
          required: true
          description: '该命令用于指定GGSN/PGW-C与指定PCRF之间建立一组Diameter链路。本端主机名和对端主机名唯一确定了一组Diameter链路。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        LOCALHOSTNAME:
          name: '本端主机名'
          type: string
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
          - GX
          - GY
          - S6b
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        PEERHOSTNAME:
          name: '对端主机名'
          type: string
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
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: SESSION_ID
    add_diamconnection_list:
      type: items
      properties:
        DIAMCONNGRP:
          name: 'Diameter链路组名'
          type: string
          maxLength: 31
          required: true
          description: '增加Diameter链路。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        LOCINTERFACE:
          name: '本端接口名'
          type: string
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
          description: ''
          data_source: '与对端协商'
          pattern: ''
          default: ''
        PEERIPV4ADDR:
          name: '对端IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '与对端协商'
          pattern: ''
          default: ''
        LOCALPORT:
          name: '本端端口'
          type: integer
          minimum:
          - 0
          - 13200
          - 16400
          - 19765
          maximum:
          - 0
          - 13263
          - 16463
          - 19784
          required: false
          description: '**SET CONCENPOINT**命令中的“GXCONCENMODE”为“LOCALPORT”时，此处必须配置“本端端口”为非0的有效值；否则不配置“本端端口”或配置为“0”。'
          data_source: '本端规划'
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
        PEERSCTPENDPT:
          name: '对端SCTP端点名称'
          type: string
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
    add_imsimsisdnseg_list:
      type: items
      properties:
        SEGMENTNAME:
          name: 'IMSI/MSISDN号段名称'
          type: string
          maxLength: 31
          required: true
          description: '配置IMSI/MSISDN号码段。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SEGMENTTYPE:
          name: 'IMSI/MSISDN号段类型'
          type: string
          enum:
          - IMSI
          - IMSIWILDCARD
          - MSISDN
          - MSISDNWILDCARD
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        SEGSTART:
          name: '号段起始字符串'
          type: string
          maxLength: 17
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        SEGEND:
          name: '号段结束字符串'
          type: string
          maxLength: 17
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        WILDCARDSEG:
          name: '通配号段字符串'
          type: string
          maxLength: 47
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_pcrfgroup_list:
      type: items
      properties:
        PCRFGRPNAME:
          name: 'PCRF组名称'
          type: string
          maxLength: 128
          required: true
          description: '增加PCRF组。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        LOADBALANCEMODE:
          name: '负荷分担模式'
          type: string
          enum:
          - LOAD_BALANCE
          - MASTER_SLAVE
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: MASTER_SLAVE
    add_pcrfbindgrp_list:
      type: items
      properties:
        PCRFGRPNAME:
          name: 'PCRF组名称'
          type: string
          maxLength: 128
          required: true
          description: '将PCRF绑定到PCRF组中。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        PCRFHOSTNAME:
          name: 'PCRF主机名称'
          type: string
          maxLength: 127
          required: true
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    set_masterpcrf_list:
      type: items
      properties:
        PCRFGRPNAME:
          name: 'PCRF组名称'
          type: string
          maxLength: 128
          required: true
          description: '设置PCRF组中的主PCRF。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        MASTERPCRF:
          name: '主用PCRF主机名'
          type: string
          maxLength: 127
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_glbpcrfgroup_list:
      type: items
      properties:
        IMSIMSISDNSEG:
          name: 'IMSI/MSISDN号段名称'
          type: string
          maxLength: 31
          required: true
          description: '基于号段绑定PCRF组。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        PRIORITY:
          name: '优先级'
          type: integer
          minimum: 1
          maximum: 65535
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        PCRFGRPNAME:
          name: 'PCRF组名称'
          type: string
          maxLength: 128
          required: true
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    set_dftglbpcrfgrp_list:
      type: items
      properties:
        PCRFGRPNAME:
          name: 'PCRF组名称'
          type: string
          maxLength: 128
          required: false
          description: '配置全局缺省PCRF组。'
          data_source: '已配置数据中获取'
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
          description: '配置APN。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_pcrfgrpbndapn_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          maxLength: 63
          required: true
          description: '为APN绑定PCRF组。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        DEFAULTFLAG:
          name: '缺省标记'
          type: string
          enum:
          - DEFAULT
          - IMSI_MSISDN_SEG
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        PCRFGRPNAME:
          name: 'PCRF组名称'
          type: string
          maxLength: 128
          required: true
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        IMSIMSISDNSEG:
          name: 'IMSI/MSISDN号段名称'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PRIORITY:
          name: '优先级'
          type: integer
          minimum: 1
          maximum: 65535
          required: false
          description: ''
          data_source: ''
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
          description: '创建VPN实例。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    set_concenpoint_list_1:
      type: items
      properties:
        GXCONCENMODE:
          name: 'Gx集中点模式'
          type: string
          enum:
          - LOCALIP_PEER
          - LOCALPORT
          required: false
          description: '配置Diameter应用集中点模式。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_logicip_list_2:
      type: items
      properties:
        IPVERSION:
          name: 'IP地址类型'
          type: string
          enum:
          - IPv4
          - IPv6
          required: true
          description: '配置Gx接口逻辑IP地址。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        LOGICIPV4:
          name: 'IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        VPNINSTNAME:
          name: 'VPN实例名称'
          type: string
          minLength: 1
          maxLength: 31
          required: false
          description: ''
          data_source: '全网规划'
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
    add_logicinf_list_2:
      type: items
      properties:
        NAME:
          name: '逻辑接口名称'
          type: string
          maxLength: 63
          required: true
          description: '配置组级Gx逻辑接口。'
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
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPV4ADDRESS1:
          name: '逻辑接口的IPv4地址1'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV4MASK1:
          name: '逻辑接口的IPv4掩码1'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
        VPNINSTANCE:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: false
          description: '已通过命令**ADD VPNINST**配置，可以使用**LST VPNINST**命令进行查询。'
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
    add_logicip_list_3:
      type: items
      properties:
        IPVERSION:
          name: 'IP地址类型'
          type: string
          enum:
          - IPv4
          - IPv6
          required: true
          description: '配置Gx接口逻辑IP地址。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        LOGICIPV4:
          name: 'IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        VPNINSTNAME:
          name: 'VPN实例名称'
          type: string
          minLength: 1
          maxLength: 31
          required: false
          description: ''
          data_source: '全网规划'
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
    add_logicinf_list_3:
      type: items
      properties:
        NAME:
          name: '逻辑接口名称'
          type: string
          maxLength: 63
          required: true
          description: '配置组级Gx逻辑接口。'
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
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPV4ADDRESS1:
          name: '逻辑接口的IPv4地址1'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV4MASK1:
          name: '逻辑接口的IPv4掩码1'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
        VPNINSTANCE:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: false
          description: '已通过命令**ADD VPNINST**配置，可以使用**LST VPNINST**命令进行查询。'
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
    add_diamlocinfo_list_1:
      type: items
      properties:
        HOSTNAME:
          name: '本端主机名'
          type: string
          maxLength: 127
          required: true
          description: '配置GGSN/PGW-C的本端信息。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        REALMNAME:
          name: '本端域名'
          type: string
          maxLength: 127
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        PRODUCTNAME:
          name: '产品名称'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_pcrf_list_2:
      type: items
      properties:
        HOSTNAME:
          name: 'PCRF主机名'
          type: string
          maxLength: 127
          required: true
          description: '配置PCRF信息。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        REALMNAME:
          name: 'PCRF域名'
          type: string
          maxLength: 127
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        VPNINSTANCE:
          name: 'VPN实例'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        SUPFEANEGOSW:
          name: 'Supported-Features动态协商开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '与对端协商'
          pattern: ''
          default: DISABLE
        FEATURELIST:
          name: 'Feature列表'
          type: string
          required: false
          description: ''
          data_source: '与对端协商'
          pattern: ''
          default: ''
        CARRYSUPFEASW:
          name: 'Supported-Feature AVP携带开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ENABLE
    add_imsimsisdnseg_list_2:
      type: items
      properties:
        SEGMENTNAME:
          name: 'IMSI/MSISDN号段名称'
          type: string
          maxLength: 31
          required: true
          description: '配置IMSI/MSISDN号码段。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SEGMENTTYPE:
          name: 'IMSI/MSISDN号段类型'
          type: string
          enum:
          - IMSI
          - IMSIWILDCARD
          - MSISDN
          - MSISDNWILDCARD
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        SEGSTART:
          name: '号段起始字符串'
          type: string
          maxLength: 17
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        SEGEND:
          name: '号段结束字符串'
          type: string
          maxLength: 17
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        WILDCARDSEG:
          name: '通配号段字符串'
          type: string
          maxLength: 47
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_pcrfgroup_list_1:
      type: items
      properties:
        PCRFGRPNAME:
          name: 'PCRF组名称'
          type: string
          maxLength: 128
          required: true
          description: '增加PCRF组。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        LOADBALANCEMODE:
          name: '负荷分担模式'
          type: string
          enum:
          - LOAD_BALANCE
          - MASTER_SLAVE
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: MASTER_SLAVE
    add_pcrfbindgrp_list_2:
      type: items
      properties:
        PCRFGRPNAME:
          name: 'PCRF组名称'
          type: string
          maxLength: 128
          required: true
          description: '将PCRF绑定到PCRF组中。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        PCRFHOSTNAME:
          name: 'PCRF主机名称'
          type: string
          maxLength: 127
          required: true
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    set_masterpcrf_list_1:
      type: items
      properties:
        PCRFGRPNAME:
          name: 'PCRF组名称'
          type: string
          maxLength: 128
          required: true
          description: '设置PCRF组中的主PCRF。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        MASTERPCRF:
          name: '主用PCRF主机名'
          type: string
          maxLength: 127
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_glbpcrfgroup_list_1:
      type: items
      properties:
        IMSIMSISDNSEG:
          name: 'IMSI/MSISDN号段名称'
          type: string
          maxLength: 31
          required: true
          description: '基于号段绑定PCRF组。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        PRIORITY:
          name: '优先级'
          type: integer
          minimum: 1
          maximum: 65535
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        PCRFGRPNAME:
          name: 'PCRF组名称'
          type: string
          maxLength: 128
          required: true
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    set_dftglbpcrfgrp_list_1:
      type: items
      properties:
        PCRFGRPNAME:
          name: 'PCRF组名称'
          type: string
          maxLength: 128
          required: false
          description: '配置全局缺省PCRF组。'
          data_source: '已配置数据中获取'
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
          description: '配置APN。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_pcrfgrpbndapn_list_1:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          maxLength: 63
          required: true
          description: '为APN绑定PCRF组。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        DEFAULTFLAG:
          name: '缺省标记'
          type: string
          enum:
          - DEFAULT
          - IMSI_MSISDN_SEG
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        PCRFGRPNAME:
          name: 'PCRF组名称'
          type: string
          maxLength: 128
          required: true
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        IMSIMSISDNSEG:
          name: 'IMSI/MSISDN号段名称'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PRIORITY:
          name: '优先级'
          type: integer
          minimum: 1
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_diampeeraddr_list_3:
      type: items
      properties:
        HOSTNAME:
          name: '主机名称'
          type: string
          maxLength: 127
          required: true
          description: '增加Diameter链路对端的地址信息，配置Diameter链路对端的地址类型、IP、端口号或端点信息。'
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
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPV4ADDRESS:
          name: 'IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
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
        SCTPENDPOINT:
          name: 'SCTP端点名称'
          type: string
          maxLength: 63
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_diamconngrp_list_2:
      type: items
      properties:
        CONNGROUPNAME:
          name: 'Diameter链路组名'
          type: string
          maxLength: 31
          required: true
          description: '该命令用于指定GGSN/PGW-C与指定PCRF之间建立一组Diameter链路。本端主机名和对端主机名唯一确定了一组Diameter链路。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        LOCALHOSTNAME:
          name: '本端主机名'
          type: string
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
          - GX
          - GY
          - S6b
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        PEERHOSTNAME:
          name: '对端主机名'
          type: string
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
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: SESSION_ID
    add_diamconnection_list_3:
      type: items
      properties:
        DIAMCONNGRP:
          name: 'Diameter链路组名'
          type: string
          maxLength: 31
          required: true
          description: '增加Diameter链路。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        LOCINTERFACE:
          name: '本端接口名'
          type: string
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
          description: ''
          data_source: '与对端协商'
          pattern: ''
          default: ''
        PEERIPV4ADDR:
          name: '对端IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '与对端协商'
          pattern: ''
          default: ''
        LOCALPORT:
          name: '本端端口'
          type: integer
          minimum:
          - 0
          - 13200
          - 16400
          - 19765
          maximum:
          - 0
          - 13263
          - 16463
          - 19784
          required: false
          description: '**SET CONCENPOINT**命令中的“GXCONCENMODE”为“LOCALPORT”时，此处必须配置“本端端口”为非0的有效值；否则不配置“本端端口”或配置为“0”。'
          data_source: '本端规划'
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
        PEERSCTPENDPT:
          name: '对端SCTP端点名称'
          type: string
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
    add_localhostgrp_list:
      type: items
      properties:
        LOCGRPNAME:
          name: 'Diameter本端信息组名称'
          type: string
          maxLength: 63
          required: true
          description: '配置Diameter本端主机组。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_localhostbind_list:
      type: items
      properties:
        LOCGRPNAME:
          name: 'Diameter本端信息组名'
          type: string
          maxLength: 63
          required: true
          description: '将Diameter本端主机添加到Diameter本端主机组中。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        LOCHOSTNAME:
          name: 'Diameter本端主机名'
          type: string
          maxLength: 127
          required: true
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_gxupfgroup_list:
      type: items
      properties:
        UPFGRPNAME:
          name: 'Gx UPF组名称'
          type: string
          maxLength: 32
          required: true
          description: '配置Gx UPF组。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_upfbindgxupfgrp_list:
      type: items
      properties:
        UPFGRPNAME:
          name: 'Gx UPF组名称'
          type: string
          maxLength: 32
          required: true
          description: '将对接的UPF主机名添加到UPF组中。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        UPFINSTANCEID:
          name: 'UPF实例标识'
          type: string
          maxLength: 36
          required: true
          description: ''
          data_source: '与对端协商'
          pattern: ''
          default: ''
    add_upfglocgbndgrp_list:
      type: items
      properties:
        UPFGLOCGBNDGNAME:
          name: 'UPF组与Diameter本端主机组的绑定关系组名称'
          type: string
          maxLength: 63
          required: true
          description: '配置UPF组与Diameter本端主机组的绑定关系组。规划多个时，该参数不能重复。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_upfgbindlocg_list:
      type: items
      properties:
        UPFGLOCGBNDGNAME:
          name: 'UPF组与Diameter本端主机组的绑定关系组名称'
          type: string
          maxLength: 63
          required: true
          description: '同一PGW-C对接多个PGW-U，不同PGW-U下的用户IP存在相同或重叠时，则同时满足上述2个条件的PGW-U对应的PGW-U组必须绑定不同的Diameter本端主机组。例如，upf1和upf2满足上述条件，则upf1和upf2对应的Diameter本端主机名必须不同。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        UPFGRPNAME:
          name: 'Gx UPF组名称'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        DIAMLOCGRPNAME:
          name: 'Diameter本端信息组名称'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        PRIORITY:
          name: '优先级'
          type: integer
          minimum: 1
          maximum: 127
          required: true
          description: '值越小，优先级越高。'
          data_source: '本端规划'
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
          description: '基于APN配置PCC本端主机名选择模式。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        LOCSLCTMODE:
          name: '本端主机名选择模式'
          type: string
          enum:
          - INHERIT
          - LOADSHARING
          - SPECIFIC
          - UPFGRP
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: INHERIT
        UPFGLOCGBNDGNAME:
          name: 'UPF组与Diameter本端主机组的绑定关系组名称'
          type: string
          maxLength: 63
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        LOCALHOSTNAME:
          name: '本端主机名'
          type: string
          maxLength: 127
          required: false
          description: ''
          data_source: ''
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
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        PCCTEMPLATE:
          name: 'PCC模板名称'
          type: string
          maxLength: 63
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
  examples:
    add_vpninst_list:
    - VPNINSTANCE: 'vpn_gxif'
    set_concenpoint_list:
    - GXCONCENMODE: LOCALPORT
    add_logicip_list:
    - IPVERSION: IPv4
      LOGICIPV4: '10.8.10.1'
      VPNINSTNAME: 'vpn_gxif'
      IPV4MTU: 1500
      IPV6MTU: 1500
      LOGICIPV6: ''
    add_logicinf_list:
    - NAME: 'gxif1/0/0'
      IPVERSION: IPV4
      IPV4ADDRESS1: '10.8.10.1'
      IPV4MASK1: '255.255.255.255'
      VPNINSTANCE: 'vpn_gxif'
      IPV4ADDRESS2: ''
      IPV4MASK2: ''
      IPV6ADDRESS1: ''
      IPV6ADDRESS2: ''
      IPV6PREFIXLEN1: ''
      IPV6PREFIXLEN2: ''
    add_logicip_list_1:
    - IPVERSION: IPv4
      LOGICIPV4: '10.8.10.2'
      VPNINSTNAME: 'vpn_gxif'
      IPV4MTU: 1500
      IPV6MTU: 1500
      LOGICIPV6: ''
    add_logicinf_list_1:
    - NAME: 'gxif1/0/1'
      IPVERSION: IPV4
      IPV4ADDRESS1: '10.8.10.2'
      IPV4MASK1: '255.255.255.255'
      VPNINSTANCE: 'vpn_gxif'
      IPV4ADDRESS2: ''
      IPV4MASK2: ''
      IPV6ADDRESS1: ''
      IPV6ADDRESS2: ''
      IPV6PREFIXLEN1: ''
      IPV6PREFIXLEN2: ''
    add_diamlocinfo_list:
    - HOSTNAME: 'pgwc_1'
      REALMNAME: 'huawei.com'
      PRODUCTNAME: 'unc@huawei.com'
    add_pcrf_list:
    - HOSTNAME: 'pcrf_1'
      REALMNAME: 'example.com'
      VPNINSTANCE: 'vpn_gxif'
      SUPFEANEGOSW: ENABLE
      FEATURELIST: RELEASE8-1&RELEASE9-1&RELEASE10-1
      CARRYSUPFEASW: ENABLE
    add_diampeeraddr_list:
    - HOSTNAME: 'pcrf_1'
      ADDRTYPE: IPv4
      IPV4ADDRESS: '10.11.21.59'
      IPV6ADDRESS: ''
      PORT: 3868
      SCTPENDPOINT: ''
    add_diamconngrp_list:
    - CONNGROUPNAME: 'dconn_pcrf1'
      LOCALHOSTNAME: 'pgwc_1'
      APPLICATION: GX
      PEERHOSTNAME: 'pcrf_1'
      SELECTMODE: SESSION_ID
    add_diamconnection_list:
    - DIAMCONNGRP: 'dconn_pcrf1'
      LOCINTERFACE: 'gxif1/0/0'
      PEERADDRTYPE: IPv4
      PEERIPV4ADDR: '10.11.21.59'
      LOCALPORT: 16450
      PEERIPV6ADDR: ''
      PEERPORT: ''
      PEERSCTPENDPT: ''
      REVERSEIP: DISABLE
    add_imsimsisdnseg_list:
    - SEGMENTNAME: 'msisdnseg1'
      SEGMENTTYPE: MSISDN
      SEGSTART: '18900000000'
      SEGEND: '18949999999'
      WILDCARDSEG: ''
    add_pcrfgroup_list:
    - PCRFGRPNAME: 'pcrf_group_1'
      LOADBALANCEMODE: MASTER_SLAVE
    add_pcrfbindgrp_list:
    - PCRFGRPNAME: 'pcrf_group_1'
      PCRFHOSTNAME: 'pcrf_1'
    set_masterpcrf_list:
    - PCRFGRPNAME: 'pcrf_group_1'
      MASTERPCRF: 'pcrf_1'
    add_glbpcrfgroup_list:
    - IMSIMSISDNSEG: 'msisdnseg1'
      PRIORITY: 1
      PCRFGRPNAME: 'pcrf_group_1'
    set_dftglbpcrfgrp_list:
    - PCRFGRPNAME: 'pcrf_group_1'
    add_apn_list:
    - APN: 'apn-test1'
    add_pcrfgrpbndapn_list:
    - APN: 'apn-test1'
      DEFAULTFLAG: DEFAULT
      PCRFGRPNAME: 'pcrf_group_1'
      IMSIMSISDNSEG: ''
      PRIORITY: ''
    add_vpninst_list_1:
    - VPNINSTANCE: 'vpn_gxif'
    set_concenpoint_list_1:
    - GXCONCENMODE: LOCALPORT
    add_logicip_list_2:
    - IPVERSION: IPv4
      LOGICIPV4: '10.8.10.1'
      VPNINSTNAME: 'vpn_gxif'
      IPV4MTU: 1500
      IPV6MTU: 1500
      LOGICIPV6: ''
    add_logicinf_list_2:
    - NAME: 'gxif1/0/0'
      IPVERSION: IPV4
      IPV4ADDRESS1: '10.8.10.1'
      IPV4MASK1: '255.255.255.255'
      VPNINSTANCE: 'vpn_gxif'
      IPV4ADDRESS2: ''
      IPV4MASK2: ''
      IPV6ADDRESS1: ''
      IPV6ADDRESS2: ''
      IPV6PREFIXLEN1: ''
      IPV6PREFIXLEN2: ''
    add_logicip_list_3:
    - IPVERSION: IPv4
      LOGICIPV4: '10.8.10.2'
      VPNINSTNAME: 'vpn_gxif'
      IPV4MTU: 1500
      IPV6MTU: 1500
      LOGICIPV6: ''
    add_logicinf_list_3:
    - NAME: 'gxif1/0/1'
      IPVERSION: IPV4
      IPV4ADDRESS1: '10.8.10.2'
      IPV4MASK1: '255.255.255.255'
      VPNINSTANCE: 'vpn_gxif'
      IPV4ADDRESS2: ''
      IPV4MASK2: ''
      IPV6ADDRESS1: ''
      IPV6ADDRESS2: ''
      IPV6PREFIXLEN1: ''
      IPV6PREFIXLEN2: ''
    add_diamlocinfo_list_1:
    - HOSTNAME: 'pgwc_1'
      REALMNAME: 'huawei.com'
      PRODUCTNAME: 'unc@huawei.com'
    add_pcrf_list_2:
    - HOSTNAME: 'pcrf_1'
      REALMNAME: 'example.com'
      VPNINSTANCE: 'vpn_gxif'
      SUPFEANEGOSW: ENABLE
      FEATURELIST: RELEASE8-1&RELEASE9-1&RELEASE10-1
      CARRYSUPFEASW: ENABLE
    add_imsimsisdnseg_list_2:
    - SEGMENTNAME: 'msisdnseg1'
      SEGMENTTYPE: MSISDN
      SEGSTART: '18900000000'
      SEGEND: '18949999999'
      WILDCARDSEG: ''
    add_pcrfgroup_list_1:
    - PCRFGRPNAME: 'pcrf_group_1'
      LOADBALANCEMODE: MASTER_SLAVE
    add_pcrfbindgrp_list_2:
    - PCRFGRPNAME: 'pcrf_group_1'
      PCRFHOSTNAME: 'pcrf_1'
    set_masterpcrf_list_1:
    - PCRFGRPNAME: 'pcrf_group_1'
      MASTERPCRF: 'pcrf_1'
    add_glbpcrfgroup_list_1:
    - IMSIMSISDNSEG: 'msisdnseg1'
      PRIORITY: 1
      PCRFGRPNAME: 'pcrf_group_1'
    set_dftglbpcrfgrp_list_1:
    - PCRFGRPNAME: 'pcrf_group_1'
    add_apn_list_1:
    - APN: 'apn-test1'
    add_pcrfgrpbndapn_list_1:
    - APN: 'apn-test1'
      DEFAULTFLAG: DEFAULT
      PCRFGRPNAME: 'pcrf_group_1'
      IMSIMSISDNSEG: ''
      PRIORITY: ''
    add_diampeeraddr_list_3:
    - HOSTNAME: 'pcrf_1'
      ADDRTYPE: IPv4
      IPV4ADDRESS: '10.11.21.59'
      IPV6ADDRESS: ''
      PORT: 3868
      SCTPENDPOINT: ''
    add_diamconngrp_list_2:
    - CONNGROUPNAME: 'dconn_pcrf1'
      LOCALHOSTNAME: 'pgwc_1'
      APPLICATION: GX
      PEERHOSTNAME: 'pcrf_1'
      SELECTMODE: SESSION_ID
    add_diamconnection_list_3:
    - DIAMCONNGRP: 'dconn_pcrf1'
      LOCINTERFACE: 'gxif1/0/0'
      PEERADDRTYPE: IPv4
      PEERIPV4ADDR: '10.11.21.59'
      LOCALPORT: 16450
      PEERIPV6ADDR: ''
      PEERPORT: ''
      PEERSCTPENDPT: ''
      REVERSEIP: DISABLE
    add_localhostgrp_list:
    - LOCGRPNAME: 'pgwc_host_group_01'
    add_localhostbind_list:
    - LOCGRPNAME: 'pgwc_host_group_01'
      LOCHOSTNAME: 'pgwc_1'
    add_gxupfgroup_list:
    - UPFGRPNAME: 'upfgrp_01'
    add_upfbindgxupfgrp_list:
    - UPFGRPNAME: 'upfgrp_01'
      UPFINSTANCEID: 'UPF_Instance_1'
    add_upfglocgbndgrp_list:
    - UPFGLOCGBNDGNAME: 'test'
    add_upfgbindlocg_list:
    - UPFGLOCGBNDGNAME: 'test'
      UPFGRPNAME: 'upfgrp_01'
      DIAMLOCGRPNAME: 'pgwc_host_group_01'
      PRIORITY: 10
    add_pcctemplate_list:
    - PCCTEMPNAME: 'pcctemplate_01'
      LOCSLCTMODE: UPFGRP
      UPFGLOCGBNDGNAME: 'test'
      LOCALHOSTNAME: ''
    set_apnpccfunc_list:
    - APN: 'apn-test1'
      PCCTEMPLATE: 'pcctemplate_01'
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 **场景一：同一PGW-C下的不同PGW-U下的用户IP不同。**

### GGSN/PGW-C使用逻辑接口与PCRF连通。

### GGSN/PGW-C使用VPN缺省路由与PCRF建立起正常的IP连接。

#### 1.1 参考组网路由配置配置外联口IP及路由。

#### 1.2 创建一个VPN实例。

```jinja2
{%- if is_scenario_user_ip_different -%}
    {%- for item in add_vpninst_list -%}
        ADD VPNINST:
        {#- --- 必选参数 --- -#}
        VPNINSTANCE="{{item.VPNINSTANCE}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 1.3 配置Gx接口Diameter应用集中点模式。

```jinja2
{%- if is_scenario_user_ip_different -%}
    {%- for item in set_concenpoint_list -%}
        SET CONCENPOINT:
        {#- --- 可选参数 --- -#}
        {%- if item.GXCONCENMODE is not none -%}
            GXCONCENMODE={{item.GXCONCENMODE}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 1.4 配置Gx逻辑接口。

```jinja2
{%- if is_scenario_user_ip_different -%}
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
{%- endif -%}
```

```jinja2
{%- if is_scenario_user_ip_different -%}
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

```jinja2
{%- if is_scenario_user_ip_different -%}
    {%- for item in add_logicip_list_1 -%}
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
{%- endif -%}
```

```jinja2
{%- if is_scenario_user_ip_different -%}
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

#### 1.5 配置PCRF信息。

#### 配置GGSN/PGW-C的设备标识。

```jinja2
{%- if is_scenario_user_ip_different -%}
    {%- for item in add_diamlocinfo_list -%}
        ADD DIAMLOCINFO:
        {#- --- 必选参数 --- -#}
        HOSTNAME="{{item.HOSTNAME}}",
        REALMNAME="{{item.REALMNAME}}",
        PRODUCTNAME="{{item.PRODUCTNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 配置PCRF设备标识。其中GGSN/PGW-C与pcrf1之间建立一条Diameter链路，与pcrf2之间建立两条Diameter链路，不同的用户会话将负荷分担到不同链路上。

```jinja2
{%- if is_scenario_user_ip_different -%}
    {%- for item in add_pcrf_list -%}
        ADD PCRF:
        {#- --- 必选参数 --- -#}
        HOSTNAME="{{item.HOSTNAME}}",
        REALMNAME="{{item.REALMNAME}}",
        {#- --- 可选参数 --- -#}
        {%- if item.VPNINSTANCE is not none -%}
            VPNINSTANCE="{{item.VPNINSTANCE}}",
        {%- endif -%}
        {%- if item.SUPFEANEGOSW is not none -%}
            SUPFEANEGOSW={{item.SUPFEANEGOSW}},
        {%- endif -%}
        {%- if item.FEATURELIST is not none -%}
            FEATURELIST={{item.FEATURELIST}},
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：SUPFEANEGOSW=DISABLE 时可选 --- -#}
        {%- if item.SUPFEANEGOSW == 'DISABLE' -%}
            {%- if item.CARRYSUPFEASW is not none -%}
                CARRYSUPFEASW={{item.CARRYSUPFEASW}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 1.6 配置Diameter对端地址。为Diameter主机增加一个Diameter对端地址，建链后用以进行消息交互。

```jinja2
{%- if is_scenario_user_ip_different -%}
    {%- for item in add_diampeeraddr_list -%}
        ADD DIAMPEERADDR:
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

#### 1.7 配置Diameter链路组。

```jinja2
{%- if is_scenario_user_ip_different -%}
    {%- for item in add_diamconngrp_list -%}
        ADD DIAMCONNGRP:
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

#### 1.8 配置UNC到对端网元的一条Diameter链路。

```jinja2
{%- if is_scenario_user_ip_different -%}
    {%- for item in add_diamconnection_list -%}
        ADD DIAMCONNECTION:
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

#### 1.9 **可选：**配置IMSI/MSISDN号码段。

```jinja2
{%- if is_optional_imsi_msisdn_segment and is_scenario_user_ip_different -%}
    {%- for item in add_imsimsisdnseg_list -%}
        ADD IMSIMSISDNSEG:
        {#- --- 必选参数 --- -#}
        SEGMENTNAME="{{item.SEGMENTNAME}}",
        SEGMENTTYPE={{item.SEGMENTTYPE}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：SEGMENTTYPE=IMSI/MSISDN 时必选 --- -#}
        {%- if item.SEGMENTTYPE in ['IMSI', 'MSISDN'] -%}
            SEGSTART="{{item.SEGSTART}}",
        {%- endif -%}
        {#- --- 条件必选：SEGMENTTYPE=IMSI/MSISDN 时必选 --- -#}
        {%- if item.SEGMENTTYPE in ['IMSI', 'MSISDN'] -%}
            SEGEND="{{item.SEGEND}}",
        {%- endif -%}
        {#- --- 条件必选：SEGMENTTYPE=IMSIWILDCARD/MSISDNWILDCARD 时必选 --- -#}
        {%- if item.SEGMENTTYPE in ['IMSIWILDCARD', 'MSISDNWILDCARD'] -%}
            WILDCARDSEG="{{item.WILDCARDSEG}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 1.10 增加PCRF组。

```jinja2
{%- if is_scenario_user_ip_different -%}
    {%- for item in add_pcrfgroup_list -%}
        ADD PCRFGROUP:
        {#- --- 必选参数 --- -#}
        PCRFGRPNAME="{{item.PCRFGRPNAME}}",
        {#- --- 可选参数 --- -#}
        {%- if item.LOADBALANCEMODE is not none -%}
            LOADBALANCEMODE={{item.LOADBALANCEMODE}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 1.11 把PCRF绑定到PCRF组中。

```jinja2
{%- if is_scenario_user_ip_different -%}
    {%- for item in add_pcrfbindgrp_list -%}
        ADD PCRFBINDGRP:
        {#- --- 必选参数 --- -#}
        PCRFGRPNAME="{{item.PCRFGRPNAME}}",
        PCRFHOSTNAME="{{item.PCRFHOSTNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 1.12 设置PCRF组中的主PCRF。

```jinja2
{%- if is_scenario_user_ip_different -%}
    {%- for item in set_masterpcrf_list -%}
        SET MASTERPCRF:
        {#- --- 必选参数 --- -#}
        PCRFGRPNAME="{{item.PCRFGRPNAME}}",
        MASTERPCRF="{{item.MASTERPCRF}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 1.13 **可选：**基于号段绑定PCRF组。

```jinja2
{%- if is_optional_bind_pcrf_group_by_segment and is_scenario_user_ip_different -%}
    {%- for item in add_glbpcrfgroup_list -%}
        ADD GLBPCRFGROUP:
        {#- --- 必选参数 --- -#}
        IMSIMSISDNSEG="{{item.IMSIMSISDNSEG}}",
        PCRFGRPNAME="{{item.PCRFGRPNAME}}",
        PRIORITY={{item.PRIORITY}},
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 1.14 配置全局缺省PCRF组。

```jinja2
{%- if is_scenario_user_ip_different -%}
    {%- for item in set_dftglbpcrfgrp_list -%}
        SET DFTGLBPCRFGRP:
        {#- --- 可选参数 --- -#}
        {%- if item.PCRFGRPNAME is not none -%}
            PCRFGRPNAME="{{item.PCRFGRPNAME}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 1.15 **可选：**配置APN。如果已配置APN，则跳过本步骤。

```jinja2
{%- if is_optional_apn and is_scenario_user_ip_different -%}
    {%- for item in add_apn_list -%}
        ADD APN:
        {#- --- 必选参数 --- -#}
        APN="{{item.APN}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 1.16 为APN绑定PCRF组。

```jinja2
{%- if is_scenario_user_ip_different -%}
    {%- for item in add_pcrfgrpbndapn_list -%}
        ADD PCRFGRPBNDAPN:
        {#- --- 必选参数 --- -#}
        APN="{{item.APN}}",
        DEFAULTFLAG={{item.DEFAULTFLAG}},
        PCRFGRPNAME="{{item.PCRFGRPNAME}}",
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：DEFAULTFLAG=IMSI_MSISDN_SEG 时必选 --- -#}
        {%- if item.DEFAULTFLAG == 'IMSI_MSISDN_SEG' -%}
            IMSIMSISDNSEG="{{item.IMSIMSISDNSEG}}",
        {%- endif -%}
        {#- --- 条件必选：DEFAULTFLAG=IMSI_MSISDN_SEG 时必选 --- -#}
        {%- if item.DEFAULTFLAG == 'IMSI_MSISDN_SEG' -%}
            PRIORITY={{item.PRIORITY}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 2 **场景二：同一PGW-C下的两个PGW-U的用户IP存在相同的情况。**

### GGSN/PGW-C使用逻辑接口与PCRF连通。

### GGSN/PGW-C使用VPN缺省路由与PCRF建立起正常的IP连接。

### 该APN下的两个PGW-U的用户IP存在相同的情况，其他APN不存在。

### PCRF要求UE IP + GxLocalHost能唯一确定一个用户。

#### 2.1 参考组网路由配置配置外联口IP及路由。

#### 2.2 创建一个VPN实例。

```jinja2
{%- if is_scenario_user_ip_same -%}
    {%- for item in add_vpninst_list_1 -%}
        ADD VPNINST:
        {#- --- 必选参数 --- -#}
        VPNINSTANCE="{{item.VPNINSTANCE}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 2.3 配置Gx接口Diameter应用集中点模式。

```jinja2
{%- if is_scenario_user_ip_same -%}
    {%- for item in set_concenpoint_list_1 -%}
        SET CONCENPOINT:
        {#- --- 可选参数 --- -#}
        {%- if item.GXCONCENMODE is not none -%}
            GXCONCENMODE={{item.GXCONCENMODE}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 2.4 配置Gx逻辑接口。

```jinja2
{%- if is_scenario_user_ip_same -%}
    {%- for item in add_logicip_list_2 -%}
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
{%- endif -%}
```

```jinja2
{%- if is_scenario_user_ip_same -%}
    {%- for item in add_logicinf_list_2 -%}
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

```jinja2
{%- if is_scenario_user_ip_same -%}
    {%- for item in add_logicip_list_3 -%}
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
{%- endif -%}
```

```jinja2
{%- if is_scenario_user_ip_same -%}
    {%- for item in add_logicinf_list_3 -%}
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

#### 2.5 配置PCRF信息。

#### 配置GGSN/PGW-C的设备标识。

```jinja2
{%- if is_scenario_user_ip_same -%}
    {%- for item in add_diamlocinfo_list_1 -%}
        ADD DIAMLOCINFO:
        {#- --- 必选参数 --- -#}
        HOSTNAME="{{item.HOSTNAME}}",
        REALMNAME="{{item.REALMNAME}}",
        PRODUCTNAME="{{item.PRODUCTNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 配置PCRF设备标识。其中GGSN/PGW-C与pcrf1之间建立一条Diameter链路，与pcrf2之间建立两条Diameter链路，不同的用户会话将负荷分担到不同链路上。

```jinja2
{%- if is_scenario_user_ip_same -%}
    {%- for item in add_pcrf_list_2 -%}
        ADD PCRF:
        {#- --- 必选参数 --- -#}
        HOSTNAME="{{item.HOSTNAME}}",
        REALMNAME="{{item.REALMNAME}}",
        {#- --- 可选参数 --- -#}
        {%- if item.VPNINSTANCE is not none -%}
            VPNINSTANCE="{{item.VPNINSTANCE}}",
        {%- endif -%}
        {%- if item.SUPFEANEGOSW is not none -%}
            SUPFEANEGOSW={{item.SUPFEANEGOSW}},
        {%- endif -%}
        {%- if item.FEATURELIST is not none -%}
            FEATURELIST={{item.FEATURELIST}},
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：SUPFEANEGOSW=DISABLE 时可选 --- -#}
        {%- if item.SUPFEANEGOSW == 'DISABLE' -%}
            {%- if item.CARRYSUPFEASW is not none -%}
                CARRYSUPFEASW={{item.CARRYSUPFEASW}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 2.6 **可选：**配置IMSI/MSISDN号码段。

```jinja2
{%- if is_optional_imsi_msisdn_segment and is_scenario_user_ip_same -%}
    {%- for item in add_imsimsisdnseg_list_2 -%}
        ADD IMSIMSISDNSEG:
        {#- --- 必选参数 --- -#}
        SEGMENTNAME="{{item.SEGMENTNAME}}",
        SEGMENTTYPE={{item.SEGMENTTYPE}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：SEGMENTTYPE=IMSI/MSISDN 时必选 --- -#}
        {%- if item.SEGMENTTYPE in ['IMSI', 'MSISDN'] -%}
            SEGSTART="{{item.SEGSTART}}",
        {%- endif -%}
        {#- --- 条件必选：SEGMENTTYPE=IMSI/MSISDN 时必选 --- -#}
        {%- if item.SEGMENTTYPE in ['IMSI', 'MSISDN'] -%}
            SEGEND="{{item.SEGEND}}",
        {%- endif -%}
        {#- --- 条件必选：SEGMENTTYPE=IMSIWILDCARD/MSISDNWILDCARD 时必选 --- -#}
        {%- if item.SEGMENTTYPE in ['IMSIWILDCARD', 'MSISDNWILDCARD'] -%}
            WILDCARDSEG="{{item.WILDCARDSEG}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 2.7 增加PCRF组。

```jinja2
{%- if is_scenario_user_ip_same -%}
    {%- for item in add_pcrfgroup_list_1 -%}
        ADD PCRFGROUP:
        {#- --- 必选参数 --- -#}
        PCRFGRPNAME="{{item.PCRFGRPNAME}}",
        {#- --- 可选参数 --- -#}
        {%- if item.LOADBALANCEMODE is not none -%}
            LOADBALANCEMODE={{item.LOADBALANCEMODE}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 2.8 把PCRF绑定到PCRF组中。

```jinja2
{%- if is_scenario_user_ip_same -%}
    {%- for item in add_pcrfbindgrp_list_2 -%}
        ADD PCRFBINDGRP:
        {#- --- 必选参数 --- -#}
        PCRFGRPNAME="{{item.PCRFGRPNAME}}",
        PCRFHOSTNAME="{{item.PCRFHOSTNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 2.9 设置PCRF组中的主PCRF。

```jinja2
{%- if is_scenario_user_ip_same -%}
    {%- for item in set_masterpcrf_list_1 -%}
        SET MASTERPCRF:
        {#- --- 必选参数 --- -#}
        PCRFGRPNAME="{{item.PCRFGRPNAME}}",
        MASTERPCRF="{{item.MASTERPCRF}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 2.10 **可选：**基于号段绑定PCRF组。

```jinja2
{%- if is_optional_bind_pcrf_group_by_segment and is_scenario_user_ip_same -%}
    {%- for item in add_glbpcrfgroup_list_1 -%}
        ADD GLBPCRFGROUP:
        {#- --- 必选参数 --- -#}
        IMSIMSISDNSEG="{{item.IMSIMSISDNSEG}}",
        PCRFGRPNAME="{{item.PCRFGRPNAME}}",
        PRIORITY={{item.PRIORITY}},
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 2.11 配置全局缺省PCRF组。

```jinja2
{%- if is_scenario_user_ip_same -%}
    {%- for item in set_dftglbpcrfgrp_list_1 -%}
        SET DFTGLBPCRFGRP:
        {#- --- 可选参数 --- -#}
        {%- if item.PCRFGRPNAME is not none -%}
            PCRFGRPNAME="{{item.PCRFGRPNAME}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 2.12 **可选：**配置APN。如果已配置APN，则跳过本步骤。

```jinja2
{%- if is_optional_apn and is_scenario_user_ip_same -%}
    {%- for item in add_apn_list_1 -%}
        ADD APN:
        {#- --- 必选参数 --- -#}
        APN="{{item.APN}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 2.13 为APN绑定PCRF组。

```jinja2
{%- if is_scenario_user_ip_same -%}
    {%- for item in add_pcrfgrpbndapn_list_1 -%}
        ADD PCRFGRPBNDAPN:
        {#- --- 必选参数 --- -#}
        APN="{{item.APN}}",
        DEFAULTFLAG={{item.DEFAULTFLAG}},
        PCRFGRPNAME="{{item.PCRFGRPNAME}}",
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：DEFAULTFLAG=IMSI_MSISDN_SEG 时必选 --- -#}
        {%- if item.DEFAULTFLAG == 'IMSI_MSISDN_SEG' -%}
            IMSIMSISDNSEG="{{item.IMSIMSISDNSEG}}",
        {%- endif -%}
        {#- --- 条件必选：DEFAULTFLAG=IMSI_MSISDN_SEG 时必选 --- -#}
        {%- if item.DEFAULTFLAG == 'IMSI_MSISDN_SEG' -%}
            PRIORITY={{item.PRIORITY}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 2.14 配置Diameter对端地址。为Diameter主机增加一个Diameter对端地址，建链后用以进行消息交互。

```jinja2
{%- if is_scenario_user_ip_same -%}
    {%- for item in add_diampeeraddr_list_3 -%}
        ADD DIAMPEERADDR:
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

#### 2.15 配置Diameter链路组。

```jinja2
{%- if is_scenario_user_ip_same -%}
    {%- for item in add_diamconngrp_list_2 -%}
        ADD DIAMCONNGRP:
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

#### 2.16 配置UNC到对端网元的一条Diameter链路。

```jinja2
{%- if is_scenario_user_ip_same -%}
    {%- for item in add_diamconnection_list_3 -%}
        ADD DIAMCONNECTION:
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

#### 2.17 添加Diameter本端主机组。

```jinja2
{%- if is_scenario_user_ip_same -%}
    {%- for item in add_localhostgrp_list -%}
        ADD LOCALHOSTGRP:
        {#- --- 必选参数 --- -#}
        LOCGRPNAME="{{item.LOCGRPNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 2.18 增加Diameter本端主机名与Diameter本端主机组的关联关系。

```jinja2
{%- if is_scenario_user_ip_same -%}
    {%- for item in add_localhostbind_list -%}
        ADD LOCALHOSTBIND:
        {#- --- 必选参数 --- -#}
        LOCGRPNAME="{{item.LOCGRPNAME}}",
        LOCHOSTNAME="{{item.LOCHOSTNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 2.19 配置Gx UPF组名称。

```jinja2
{%- if is_scenario_user_ip_same -%}
    {%- for item in add_gxupfgroup_list -%}
        ADD GXUPFGROUP:
        {#- --- 必选参数 --- -#}
        UPFGRPNAME="{{item.UPFGRPNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 2.20 增加UPF和Gx UPF组的绑定关系。

```jinja2
{%- if is_scenario_user_ip_same -%}
    {%- for item in add_upfbindgxupfgrp_list -%}
        ADD UPFBINDGXUPFGRP:
        {#- --- 必选参数 --- -#}
        UPFGRPNAME="{{item.UPFGRPNAME}}",
        UPFINSTANCEID="{{item.UPFINSTANCEID}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 2.21 添加UPF组与Diameter本端主机组的绑定关系组。

```jinja2
{%- if is_scenario_user_ip_same -%}
    {%- for item in add_upfglocgbndgrp_list -%}
        ADD UPFGLOCGBNDGRP:
        {#- --- 必选参数 --- -#}
        UPFGLOCGBNDGNAME="{{item.UPFGLOCGBNDGNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 2.22 增加Diameter本端主机名与Diameter本端主机组的绑定关系。

```jinja2
{%- if is_scenario_user_ip_same -%}
    {%- for item in add_upfgbindlocg_list -%}
        ADD UPFGBINDLOCG:
        {#- --- 必选参数 --- -#}
        UPFGLOCGBNDGNAME="{{item.UPFGLOCGBNDGNAME}}",
        UPFGRPNAME="{{item.UPFGRPNAME}}",
        DIAMLOCGRPNAME="{{item.DIAMLOCGRPNAME}}",
        PRIORITY={{item.PRIORITY}},
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 2.23 增加PCC模板配置，以便于绑定到APN下，使得不同的APN可以有不同的PCC配置属性。

```jinja2
{%- if is_scenario_user_ip_same -%}
    {%- for item in add_pcctemplate_list -%}
        ADD PCCTEMPLATE:
        {#- --- 必选参数 --- -#}
        PCCTEMPNAME="{{item.PCCTEMPNAME}}",
        {#- --- 可选参数 --- -#}
        {%- if item.LOCSLCTMODE is not none -%}
            LOCSLCTMODE={{item.LOCSLCTMODE}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：LOCSLCTMODE=UPFGRP 时必选 --- -#}
        {%- if item.LOCSLCTMODE == 'UPFGRP' -%}
            UPFGLOCGBNDGNAME="{{item.UPFGLOCGBNDGNAME}}",
        {%- endif -%}
        {#- --- 条件必选：LOCSLCTMODE=SPECIFIC 时必选 --- -#}
        {%- if item.LOCSLCTMODE == 'SPECIFIC' -%}
            LOCALHOSTNAME="{{item.LOCALHOSTNAME}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 2.24 使能或关闭指定APN/DNN用户的动态PCC功能。

```jinja2
{%- if is_scenario_user_ip_same -%}
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


---
id: GWFD-024303
name: 配置到AAA Server的数据（带外组网GRE VPN）
ne_type: UEG
type: feature
description: UEG和AAA Server（计费/鉴权AAA服务器）的互通采用带外组网方式，为RADIUS信令报文和数据报文配置不同的出接口。UEG到计费/鉴权AAA服务器采用缺省路由，当有多个计费/鉴权AAA服务器时，可减少路由配置的工作量，并便于管理。为了提高互通的安全性，在UEG和企业网所在网段的防火墙之间建立GRE VPN隧道。隧道绑定的VPN和计费/鉴权AAA服务器绑定的VPN不同。  适用于PGW-C、SMF
tags: []
risk_level: ''
doc_source: ["业务配置","风筝L","MEC 特性指南（风筝L）","GW-C&SMF特性指南","GWFD-024300 系统管理","GWFD-024303 Radius功能","激活RADIUS功能","配置到AAA Server的数据（带外组网GRE VPN）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
UEG和AAA Server（计费/鉴权AAA服务器）的互通采用带外组网方式，为RADIUS信令报文和数据报文配置不同的出接口。UEG到计费/鉴权AAA服务器采用缺省路由，当有多个计费/鉴权AAA服务器时，可减少路由配置的工作量，并便于管理。为了提高互通的安全性，在UEG和企业网所在网段的防火墙之间建立GRE VPN隧道。隧道绑定的VPN和计费/鉴权AAA服务器绑定的VPN不同。适用于PGW-C、SMF

## 必备事项
前提条件

* 请仔细阅读IPFD-020601 VRF功能和IPFD-020501 支持OSPF特性概述。
* UEG与网络实体之间的网络环境已经构建完成。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
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
          data_source: '本端规划'
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
          data_source: '本端规划'
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
          data_source: '本端规划'
          pattern: ''
          default: perRoute
    add_l3vpninst_list_1:
      type: items
      properties:
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: true
          description: '-'
          data_source: '本端规划'
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
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_l3vpninst_list_2:
      type: items
      properties:
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_vpninstaf_list_2:
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
          data_source: '本端规划'
          pattern: ''
          default: ''
        VRFRD:
          name: '路由标识'
          type: string
          maxLength: 21
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_interface_list:
      type: items
      properties:
        IFNAME:
          name: '接口名'
          type: string
          maxLength: 63
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_ipbindvpn_list:
      type: items
      properties:
        IFNAME:
          name: '接口名'
          type: string
          maxLength: 63
          required: true
          description: '分别对应GRE隧道的Loopback接口、Tunnel接口名称。已通过**ADD INTERFACE**命令进行配置，可以使用**LST INTERFACE**进行查询。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: true
          description: '分别对应GRE隧道的Loopback接口、Tunnel接口所使用的VPN实例。  当UEG的产品形态为风筝L时，已通过**ADD CPVPNINST**配置，可以使用**LST CPVPNINST**命令进行查询。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_ifipv4address_list:
      type: items
      properties:
        IFNAME:
          name: '接口名'
          type: string
          maxLength: 63
          required: true
          description: '已通过**ADD INTERFACE**命令进行配置，可以使用**LST INTERFACE**进行查询。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        IFIPADDR:
          name: 'IPv4地址'
          type: string
          maxLength: 15
          required: true
          description: '分别对应GRE隧道的Loopback接口、Tunnel接口所使用的IPv4地址和地址掩码。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SUBNETMASK:
          name: 'IPv4地址掩码'
          type: string
          maxLength: 15
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_gretunnel_list:
      type: items
      properties:
        TNLNAME:
          name: '隧道名称'
          type: string
          maxLength: 63
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        TNLTYPE:
          name: '隧道类型'
          type: string
          enum:
          - gre
          - gre6
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        SRCTYPE:
          name: 'IPv4源类型'
          type: string
          enum:
          - if_name
          - ip_address
          - no_type
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: no_type
        SRCIFNAME:
          name: '源接口名称'
          type: string
          maxLength: 63
          required: false
          description: '已通过**ADD INTERFACE**命令进行配置，可以使用**LST INTERFACE**进行查询。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        DSTIPADDR:
          name: '目的IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: '该参数值与Firewall B的IP地址取值一致。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        SRCTYPE6:
          name: 'IPv6源类型'
          type: string
          enum:
          - if_name
          - ip_address
          - no_type
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: no_type
    add_ipbindvpn_list_1:
      type: items
      properties:
        IFNAME:
          name: '接口名'
          type: string
          maxLength: 63
          required: true
          description: '分别对应GRE隧道的Loopback接口、Tunnel接口名称。已通过**ADD INTERFACE**命令进行配置，可以使用**LST INTERFACE**进行查询。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: true
          description: '分别对应GRE隧道的Loopback接口、Tunnel接口所使用的VPN实例。  当UEG的产品形态为风筝L时，已通过**ADD CPVPNINST**配置，可以使用**LST CPVPNINST**命令进行查询。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_ifipv4address_list_1:
      type: items
      properties:
        IFNAME:
          name: '接口名'
          type: string
          maxLength: 63
          required: true
          description: '已通过**ADD INTERFACE**命令进行配置，可以使用**LST INTERFACE**进行查询。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        IFIPADDR:
          name: 'IPv4地址'
          type: string
          maxLength: 15
          required: true
          description: '分别对应GRE隧道的Loopback接口、Tunnel接口所使用的IPv4地址和地址掩码。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SUBNETMASK:
          name: 'IPv4地址掩码'
          type: string
          maxLength: 15
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_srroute_list:
      type: items
      properties:
        AFTYPE:
          name: '地址族'
          type: string
          enum:
          - ipv4unicast
          required: true
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: ''
        PREFIX:
          name: '路由前缀'
          type: string
          maxLength: 15
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        MASKLENGTH:
          name: '路由掩码长度'
          type: integer
          minimum: 0
          maximum: 32
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: false
          description: '已通过**ADD L3VPNINST**命令进行配置，可以使用**LST L3VPNINST**进行查询。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: '_public_'
        IFNAME:
          name: '路由出接口名字'
          type: string
          maxLength: 63
          required: false
          description: '已通过**ADD GRETUNNEL**命令进行配置，可以使用**LST GRETUNNEL**进行查询。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_cpvpninst_list:
      type: items
      properties:
        VPNINSTANCE:
          name: 'VPN实例名'
          type: string
          minLength: 1
          maxLength: 31
          required: true
          description: '-'
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
          description: '逻辑接口使用的逻辑IP。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        LOGICIPV4:
          name: 'IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        VPNINSTNAME:
          name: 'VPN实例名称'
          type: string
          minLength: 1
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_cplogicinf_list:
      type: items
      properties:
        NAME:
          name: '逻辑接口名称'
          type: string
          maxLength: 63
          required: true
          description: '配置使用的逻辑接口，其中“giif1/0/0”和“10.8.20.1”用于鉴权AAA服务器，“giif1/0/1”和“10.8.20.2”用于计费AAA服务器。'
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
          description: '鉴权AAA服务器所属的VPN实例名。当UEG的产品形态为风筝L时，已通过**ADD CPVPNINST**配置，可以使用**LST CPVPNINST**命令进行查询。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_uplist4rds_list:
      type: items
      properties:
        UPLISTNAME:
          name: 'UP列表名称'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        UPINSTANCEID:
          name: 'UP实例标识'
          type: string
          maxLength: 36
          required: true
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
          description: '-'
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
        SIGOPTACCTMSG:
          name: '支持可选计费消息'
          type: string
          enum:
          - DISABLE
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: DISABLE
    add_rdssvr_list:
      type: items
      properties:
        RDSSVRGRPNAME:
          name: 'Radius Server Group名称'
          type: string
          maxLength: 31
          required: true
          description: '鉴权AAA服务器所在的AAA服务器组，已通过**ADD RDSSVRGRP**进行配置。'
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
          data_source: '全网规划'
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
          data_source: '全网规划'
          pattern: ''
          default: IPV4
        SERVERIPV4:
          name: 'IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
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
          name: 'VPN实例名'
          type: string
          maxLength: 31
          required: false
          description: '计费AAA服务器所属的VPN实例名。当UEG的产品形态为风筝L时，已通过**ADD CPVPNINST**配置，可以使用**LST CPVPNINST**命令进行查询。'
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
        CIPHERKEYCNFM:
          name: '确认服务器密钥（加密的）'
          type: string
          maxLength: 109
          required: true
          description: '-'
          data_source: '与对端协商'
          pattern: ''
          default: ''
        PRIFLAG:
          name: '主备用类型'
          type: string
          enum:
          - CARBON_COPY
          - PRIMARY
          - SECONDARY
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: PRIMARY
    add_rdssvr_list_1:
      type: items
      properties:
        RDSSVRGRPNAME:
          name: 'Radius Server Group名称'
          type: string
          maxLength: 31
          required: true
          description: '鉴权AAA服务器所在的AAA服务器组，已通过**ADD RDSSVRGRP**进行配置。'
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
          data_source: '全网规划'
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
          data_source: '全网规划'
          pattern: ''
          default: IPV4
        SERVERIPV4:
          name: 'IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
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
        CIPHERKEY:
          name: '服务器密钥（加密的）'
          type: string
          maxLength: 109
          required: true
          description: ''
          data_source: '与对端协商'
          pattern: ''
          default: ''
        PRIFLAG:
          name: '主备用类型'
          type: string
          enum:
          - CARBON_COPY
          - PRIMARY
          - SECONDARY
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: PRIMARY
        VPNINSTANCE:
          name: 'VPN实例名'
          type: string
          maxLength: 31
          required: false
          description: '计费AAA服务器所属的VPN实例名。当UEG的产品形态为风筝L时，已通过**ADD CPVPNINST**配置，可以使用**LST CPVPNINST**命令进行查询。'
          data_source: '已配置数据中获取'
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
    add_rdssvr_list_2:
      type: items
      properties:
        RDSSVRGRPNAME:
          name: 'Radius Server Group名称'
          type: string
          maxLength: 31
          required: true
          description: '计费AAA服务器所在的AAA服务器组，已通过**ADD RDSSVRGRP**进行配置。'
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
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPVERSION:
          name: '服务器IP版本'
          type: string
          enum:
          - IPV4
          - IPV6
          required: true
          description: '计费AAA服务器IP地址、端口号、密钥。'
          data_source: '全网规划'
          pattern: ''
          default: IPV4
        SERVERIPV4:
          name: 'IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
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
          name: 'VPN实例名'
          type: string
          maxLength: 31
          required: false
          description: '计费AAA服务器所属的VPN实例名。当UEG的产品形态为风筝L时，已通过**ADD CPVPNINST**配置，可以使用**LST CPVPNINST**命令进行查询。'
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
        CIPHERKEYCNFM:
          name: '确认服务器密钥（加密的）'
          type: string
          maxLength: 109
          required: true
          description: '-'
          data_source: '与对端协商'
          pattern: ''
          default: ''
        PRIFLAG:
          name: '主备用类型'
          type: string
          enum:
          - CARBON_COPY
          - PRIMARY
          - SECONDARY
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: PRIMARY
    add_rdssvr_list_3:
      type: items
      properties:
        RDSSVRGRPNAME:
          name: 'Radius Server Group名称'
          type: string
          maxLength: 31
          required: true
          description: '计费AAA服务器所在的AAA服务器组，已通过**ADD RDSSVRGRP**进行配置。'
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
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPVERSION:
          name: '服务器IP版本'
          type: string
          enum:
          - IPV4
          - IPV6
          required: true
          description: '计费AAA服务器IP地址、端口号、密钥。'
          data_source: '全网规划'
          pattern: ''
          default: IPV4
        SERVERIPV4:
          name: 'IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
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
        CIPHERKEY:
          name: '服务器密钥（加密的）'
          type: string
          maxLength: 109
          required: true
          description: ''
          data_source: '与对端协商'
          pattern: ''
          default: ''
        PRIFLAG:
          name: '主备用类型'
          type: string
          enum:
          - CARBON_COPY
          - PRIMARY
          - SECONDARY
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: PRIMARY
        VPNINSTANCE:
          name: 'VPN实例名'
          type: string
          maxLength: 31
          required: false
          description: '计费AAA服务器所属的VPN实例名。当UEG的产品形态为风筝L时，已通过**ADD CPVPNINST**配置，可以使用**LST CPVPNINST**命令进行查询。'
          data_source: '已配置数据中获取'
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
    add_cpapn_list:
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
        HASVPN:
          name: '绑定VPN'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: DISABLE
        VPNINSTANCE:
          name: 'VPN实例名'
          type: string
          minLength: 1
          maxLength: 31
          required: false
          description: '当UEG的产品形态为风筝L时，已通过**ADD CPVPNINST**配置，可以使用**LST CPVPNINST**命令进行查询。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        HASVPNIPV6:
          name: '绑定IPv6 VPN'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: DISABLE
        RESTORPGWSWITCH:
          name: '故障重启业务恢复功能PGW开关'
          type: string
          enum:
          - ENABLE
          - INHERIT
          - DISABLE
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: INHERIT
        REACWITHDEL:
          name: '去活消息携带reactivation-request开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          - SPECIFIC_SCENE
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: DISABLE
    add_apnrdsclientip_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          maxLength: 63
          required: true
          description: '当UEG的产品形态为风筝L时，已通过**ADD CPAPN**配置，可以使用**LST CPAPN**命令进行查询。'
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
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        INTFNAME:
          name: '接口名称'
          type: string
          maxLength: 13
          required: true
          description: '当UEG的产品形态为风筝L时，已通过**ADD CPLOGICINF**配置，可以使用**LST CPLOGICINF**命令进行查询。'
          data_source: '已配置数据中获取'
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
          description: '当UEG的产品形态为风筝L时，已通过**ADD CPLOGICINF**配置，可以使用**LST CPLOGICINF**命令进行查询。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        RDSSVRGRPNAME:
          name: 'Radius Server Group名称'
          type: string
          maxLength: 31
          required: true
          description: '鉴权AAA服务器所在的AAA服务器组，已通过**ADD RDSSVRGRP**进行配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
  examples:
    add_l3vpninst_list:
    - VRFNAME: 'vpn_enterprise'
    add_vpninstaf_list:
    - VRFNAME: 'vpn_enterprise'
      AFTYPE: ipv4uni
      VRFLABELMODE: perRoute
    add_l3vpninst_list_1:
    - VRFNAME: 'vpn_tunnel'
    add_vpninstaf_list_1:
    - VRFNAME: 'vpn_tunnel'
      AFTYPE: ipv4uni
    add_l3vpninst_list_2:
    - VRFNAME: 'vpn_aaa'
    add_vpninstaf_list_2:
    - VRFNAME: 'vpn_aaa'
      AFTYPE: ipv4uni
      VRFRD: '200:1'
    add_interface_list:
    - IFNAME: 'LoopBack0'
    add_ipbindvpn_list:
    - IFNAME: 'Loopback0'
      VRFNAME: 'vpn_tunnel'
    add_ifipv4address_list:
    - IFNAME: 'LoopBack0'
      IFIPADDR: '192.168.100.105'
      SUBNETMASK: '255.255.255.255'
    add_gretunnel_list:
    - TNLNAME: 'Tunnel1'
      TNLTYPE: gre
      SRCTYPE: if_name
      SRCIFNAME: 'Loopback0'
      DSTIPADDR: '192.168.95.100'
      SRCTYPE6: no_type
    add_ipbindvpn_list_1:
    - IFNAME: 'Tunnel1'
      VRFNAME: 'vpn_enterprise'
    add_ifipv4address_list_1:
    - IFNAME: 'Tunnel1'
      IFIPADDR: '10.10.1.201'
      SUBNETMASK: '255.255.255.252'
    add_srroute_list:
    - AFTYPE: ipv4unicast
      PREFIX: '10.10.1.202'
      MASKLENGTH: 30
      VRFNAME: 'vpn_enterprise'
      IFNAME: 'Tunnel1'
    add_cpvpninst_list:
    - VPNINSTANCE: 'vpn_enterprise'
    add_logicip_list:
    - IPVERSION: IPv4
      LOGICIPV4: '10.8.20.1'
      VPNINSTNAME: 'vpn_pdn'
    add_cplogicinf_list:
    - NAME: 'giif1/0/0'
      IPVERSION: IPV4
      IPV4ADDRESS1: '10.8.20.1'
      IPV4MASK1: '255.255.255.255'
      VPNINSTANCE: 'vpn_aaa'
    add_uplist4rds_list:
    - UPLISTNAME: ''
      UPINSTANCEID: ''
    add_rdssvrgrp_list:
    - RDSSVRGRPNAME: 'isprg'
      MODE: MASTER_SLAVE
      SIGOPTACCTMSG: DISABLE
    add_rdssvr_list:
    - RDSSVRGRPNAME: 'isprg'
      SERVERTYPE: AUTHENTICATION
      IPVERSION: IPV4
      SERVERIPV4: '10.168.10.1'
      PORT: 1812
      VPNINSTANCE: 'vpn_aaa'
      CIPHERKEY: '*****'
      CIPHERKEYCNFM: '*****'
      PRIFLAG: PRIMARY
    add_rdssvr_list_1:
    - RDSSVRGRPNAME: 'isprg'
      SERVERTYPE: AUTHENTICATION
      IPVERSION: IPV4
      SERVERIPV4: '10.168.10.1'
      PORT: 1812
      CIPHERKEY: 'ispchina'
      PRIFLAG: PRIMARY
      VPNINSTANCE: 'vpn_aaa'
      CIPHERKEYCNFM: 'ispchina'
    add_rdssvr_list_2:
    - RDSSVRGRPNAME: 'isprg'
      SERVERTYPE: ACCOUNTING
      IPVERSION: IPV4
      SERVERIPV4: '10.168.10.1'
      PORT: 1813
      VPNINSTANCE: 'vpn_aaa'
      CIPHERKEY: '*****'
      CIPHERKEYCNFM: '*****'
      PRIFLAG: PRIMARY
    add_rdssvr_list_3:
    - RDSSVRGRPNAME: 'isprg'
      SERVERTYPE: ACCOUNTING
      IPVERSION: IPV4
      SERVERIPV4: '10.168.10.1'
      PORT: 1813
      CIPHERKEY: 'ispchina'
      PRIFLAG: PRIMARY
      VPNINSTANCE: 'vpn_aaa'
      CIPHERKEYCNFM: 'ispchina'
    add_cpapn_list:
    - APN: 'apn1'
      HASVPN: ENABLE
      VPNINSTANCE: 'vpn_enterprise'
      HASVPNIPV6: DISABLE
      RESTORPGWSWITCH: INHERIT
      REACWITHDEL: DISABLE
    add_apnrdsclientip_list:
    - APN: 'apn1'
      AUTHORACCT: AUTHENTICATION
      INTFNAME: 'giif1/0/0'
    add_apnrdssvrgrp_list:
    - APN: 'apn1'
      RDSSVRGRPNAME: 'isprg'
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 参考配置静态路由+BFD组网（IPv4）配置对应的组网。

### 2 进入“MML命令行-UEG”窗口。

### 3 创建L3VPN实例。

### ****ADD VPNINSTAF****

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

```jinja2
{%- for item in add_l3vpninst_list_1 -%}
    ADD L3VPNINST:
    {#- --- 必选参数 --- -#}
    VRFNAME="{{item.VRFNAME}}",
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_vpninstaf_list_1 -%}
    ADD VPNINSTAF:
    {#- --- 必选参数 --- -#}
    VRFNAME="{{item.VRFNAME}}",
    AFTYPE={{item.AFTYPE}},
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_l3vpninst_list_2 -%}
    ADD L3VPNINST:
    {#- --- 必选参数 --- -#}
    VRFNAME="{{item.VRFNAME}}",
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_vpninstaf_list_2 -%}
    ADD VPNINSTAF:
    {#- --- 必选参数 --- -#}
    VRFNAME="{{item.VRFNAME}}",
    AFTYPE={{item.AFTYPE}},
    {#- --- 可选参数 --- -#}
    {%- if item.VRFRD is not none -%}
        VRFRD="{{item.VRFRD}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 创建GRE隧道。

#### 4.1 创建Loopback接口。

#### ****ADD INTERFACE****

```jinja2
{%- for item in add_interface_list -%}
    ADD INTERFACE:
    {#- --- 必选参数 --- -#}
    IFNAME="{{item.IFNAME}}",
    ;
{%- endfor -%}
```

#### 4.2 配置Loopback接口的IP地址和掩码，并将Loopback接口绑定VPN实例。

#### ****ADD IPBINDVPN****

#### ****ADD IFIPV4ADDRESS****

```jinja2
{%- for item in add_ipbindvpn_list -%}
    ADD IPBINDVPN:
    {#- --- 必选参数 --- -#}
    IFNAME="{{item.IFNAME}}",
    VRFNAME="{{item.VRFNAME}}",
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_ifipv4address_list -%}
    ADD IFIPV4ADDRESS:
    {#- --- 必选参数 --- -#}
    IFNAME="{{item.IFNAME}}",
    IFIPADDR="{{item.IFIPADDR}}",
    SUBNETMASK="{{item.SUBNETMASK}}",
    ;
{%- endfor -%}
```

#### 4.3 设置Tunnel接口报文的封装模式为GRE，设置Tunnel接口的源端地址以及目的端地址，其中指定隧道接口的Loopback接口作为源地址。

#### ****ADD GRETUNNEL****

```jinja2
{%- for item in add_gretunnel_list -%}
    ADD GRETUNNEL:
    {#- --- 必选参数 --- -#}
    TNLNAME="{{item.TNLNAME}}",
    TNLTYPE={{item.TNLTYPE}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：TNLTYPE=gre 时必选 --- -#}
    {%- if item.TNLTYPE == 'gre' -%}
        SRCTYPE={{item.SRCTYPE}},
    {%- endif -%}
    {#- --- 条件必选：SRCTYPE=if_name 时必选 --- -#}
    {%- if item.SRCTYPE == 'if_name' -%}
        SRCIFNAME="{{item.SRCIFNAME}}",
    {#- --- 条件必选：SRCTYPE6=if_name 时必选 --- -#}
    {%- elif item.SRCTYPE6 == 'if_name' -%}
        SRCIFNAME="{{item.SRCIFNAME}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：TNLTYPE=gre 时可选 --- -#}
    {%- if item.TNLTYPE == 'gre' -%}
        {%- if item.DSTIPADDR is not none -%}
            DSTIPADDR="{{item.DSTIPADDR}}",
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 4.4 配置Tunnel接口的IP地址和掩码，并将Tunnel接口绑定VPN实例。

#### ****ADD IPBINDVPN****

#### ****ADD IFIPV4ADDRESS****

```jinja2
{%- for item in add_ipbindvpn_list_1 -%}
    ADD IPBINDVPN:
    {#- --- 必选参数 --- -#}
    IFNAME="{{item.IFNAME}}",
    VRFNAME="{{item.VRFNAME}}",
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_ifipv4address_list_1 -%}
    ADD IFIPV4ADDRESS:
    {#- --- 必选参数 --- -#}
    IFNAME="{{item.IFNAME}}",
    IFIPADDR="{{item.IFIPADDR}}",
    SUBNETMASK="{{item.SUBNETMASK}}",
    ;
{%- endfor -%}
```

#### 4.5 配置静态路由。

#### ****ADD SRROUTE****

```jinja2
{%- for item in add_srroute_list -%}
    ADD SRROUTE:
    {#- --- 必选参数 --- -#}
    AFTYPE={{item.AFTYPE}},
    PREFIX="{{item.PREFIX}}",
    MASKLENGTH={{item.MASKLENGTH}},
    {#- --- 可选参数 --- -#}
    {%- if item.VRFNAME is not none -%}
        VRFNAME="{{item.VRFNAME}}",
    {%- endif -%}
    {%- if item.IFNAME is not none -%}
        IFNAME="{{item.IFNAME}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 如果需要一同配置IPv6的GRE隧道，则步骤b、d均需要先使用****SET IFIPV6ENABLE****命令开启IPv6使能，再使用****ADD IFIPV6ADDRESS****命令配置IPv6地址，步骤e需要使用****ADD SRROUTE6****命令配置IPv6静态路由。

### 5 创建VPN实例。

### 当UEG的产品形态为风筝L时，**ADD CPVPNINST**

```jinja2
{%- if is_scenario_kite_l -%}
    {%- for item in add_cpvpninst_list -%}
        ADD CPVPNINST:
        {#- --- 必选参数 --- -#}
        VPNINSTANCE="{{item.VPNINSTANCE}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

### 6 配置Gi逻辑接口。

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

### 当UEG的产品形态为风筝L时，**ADD CPLOGICINF**

```jinja2
{%- if is_scenario_kite_l -%}
    {%- for item in add_cplogicinf_list -%}
        ADD CPLOGICINF:
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
        {#- --- 条件可选：IPVERSION=IPV4/IPV6/IPVER_ALL 时可选 --- -#}
        {%- if item.IPVERSION in ['IPV4', 'IPV6', 'IPVER_ALL'] -%}
            {%- if item.VPNINSTANCE is not none -%}
                VPNINSTANCE="{{item.VPNINSTANCE}}",
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 7 **可选：**配置鉴权或计费AAA服务器使用的PGW-U/UPF列表。

```jinja2
{%- if is_optional_pgwu_upf_list -%}
    {%- for item in add_uplist4rds_list -%}
        ADD UPLIST4RDS:
        {#- --- 必选参数 --- -#}
        UPLISTNAME="{{item.UPLISTNAME}}",
        UPINSTANCEID="{{item.UPINSTANCEID}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

### 8 配置鉴权/计费AAA服务器。

#### 8.1 配置AAA服务器组以及服务器的工作模式。

```jinja2
{%- for item in add_rdssvrgrp_list -%}
    ADD RDSSVRGRP:
    {#- --- 必选参数 --- -#}
    RDSSVRGRPNAME="{{item.RDSSVRGRPNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.MODE is not none -%}
        MODE={{item.MODE}},
    {%- endif -%}
    {%- if item.SIGOPTACCTMSG is not none -%}
        SIGOPTACCTMSG={{item.SIGOPTACCTMSG}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 8.2 设置主用鉴权AAA服务器的IP地址、目的端口号、所属VPN、密钥。

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
    {%- if item.PRIFLAG is not none -%}
        PRIFLAG={{item.PRIFLAG}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPVERSION=IPV4 时必选 --- -#}
    {%- if item.IPVERSION == 'IPV4' -%}
        SERVERIPV4="{{item.SERVERIPV4}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 8.3 **可选：**设置备用鉴权AAA服务器的IP地址、目的端口号、所属VPN、密钥。

```jinja2
{%- if is_optional_standby_auth_aaa_server -%}
    {%- for item in add_rdssvr_list_1 -%}
        ADD RDSSVR:
        {#- --- 必选参数 --- -#}
        RDSSVRGRPNAME="{{item.RDSSVRGRPNAME}}",
        CIPHERKEYCNFM="{{item.CIPHERKEYCNFM}}",
        CIPHERKEY="{{item.CIPHERKEY}}",
        IPVERSION={{item.IPVERSION}},
        SERVERTYPE={{item.SERVERTYPE}},
        {#- --- 可选参数 --- -#}
        {%- if item.VPNINSTANCE is not none -%}
            VPNINSTANCE="{{item.VPNINSTANCE}}",
        {%- endif -%}
        {%- if item.PRIFLAG is not none -%}
            PRIFLAG={{item.PRIFLAG}},
        {%- endif -%}
        {%- if item.PORT is not none -%}
            PORT={{item.PORT}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：IPVERSION=IPV4 时必选 --- -#}
        {%- if item.IPVERSION == 'IPV4' -%}
            SERVERIPV4="{{item.SERVERIPV4}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 8.4 配置主用计费AAA服务器的IP地址、目的端口号、所属VPN、密钥。

```jinja2
{%- for item in add_rdssvr_list_2 -%}
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
    {%- if item.PRIFLAG is not none -%}
        PRIFLAG={{item.PRIFLAG}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPVERSION=IPV4 时必选 --- -#}
    {%- if item.IPVERSION == 'IPV4' -%}
        SERVERIPV4="{{item.SERVERIPV4}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 8.5 **可选：**配置备用计费AAA服务器的IP地址、目的端口号、所属VPN、密钥。

```jinja2
{%- if is_optional_standby_acct_aaa_server -%}
    {%- for item in add_rdssvr_list_3 -%}
        ADD RDSSVR:
        {#- --- 必选参数 --- -#}
        RDSSVRGRPNAME="{{item.RDSSVRGRPNAME}}",
        CIPHERKEYCNFM="{{item.CIPHERKEYCNFM}}",
        CIPHERKEY="{{item.CIPHERKEY}}",
        IPVERSION={{item.IPVERSION}},
        SERVERTYPE={{item.SERVERTYPE}},
        {#- --- 可选参数 --- -#}
        {%- if item.VPNINSTANCE is not none -%}
            VPNINSTANCE="{{item.VPNINSTANCE}}",
        {%- endif -%}
        {%- if item.PRIFLAG is not none -%}
            PRIFLAG={{item.PRIFLAG}},
        {%- endif -%}
        {%- if item.PORT is not none -%}
            PORT={{item.PORT}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：IPVERSION=IPV4 时必选 --- -#}
        {%- if item.IPVERSION == 'IPV4' -%}
            SERVERIPV4="{{item.SERVERIPV4}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 步骤b-e中，执行该命令多次，可以配置多个计费/鉴权AAA服务器。

#### 8.6 配置APN。

#### 当UEG的产品形态为风筝L时，**ADD CPAPN**

```jinja2
{%- if is_scenario_kite_l -%}
    {%- for item in add_cpapn_list -%}
        ADD CPAPN:
        {#- --- 必选参数 --- -#}
        APN="{{item.APN}}",
        {#- --- 可选参数 --- -#}
        {%- if item.HASVPN is not none -%}
            HASVPN={{item.HASVPN}},
        {%- endif -%}
        {%- if item.REACWITHDEL is not none -%}
            REACWITHDEL={{item.REACWITHDEL}},
        {%- endif -%}
        {%- if item.HASVPNIPV6 is not none -%}
            HASVPNIPV6={{item.HASVPNIPV6}},
        {%- endif -%}
        {%- if item.RESTORPGWSWITCH is not none -%}
            RESTORPGWSWITCH={{item.RESTORPGWSWITCH}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：HASVPN=ENABLE 时必选 --- -#}
        {%- if item.HASVPN == 'ENABLE' -%}
            VPNINSTANCE="{{item.VPNINSTANCE}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 8.7 配置APN下的Client-IP。

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

#### 8.8 APN实例下绑定RADIUS服务器组。

```jinja2
{%- for item in add_apnrdssvrgrp_list -%}
    ADD APNRDSSVRGRP:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    RDSSVRGRPNAME="{{item.RDSSVRGRPNAME}}",
    ;
{%- endfor -%}
```


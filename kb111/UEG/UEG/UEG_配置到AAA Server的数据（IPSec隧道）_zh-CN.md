---
id: GWFD-024303
name: 配置到AAA Server的数据（IPSec隧道）
ne_type: UEG
type: feature
description: 当AAA Server（计费/鉴权AAA服务器）位于Internet中，UEG与计费/鉴权AAA服务器之间采用带外组网方式，建立IPSec隧道。  适用于PGW-C、SMF
tags: []
risk_level: ''
doc_source: ["业务配置","风筝L","MEC 特性指南（风筝L）","GW-C&SMF特性指南","GWFD-024300 系统管理","GWFD-024303 Radius功能","激活RADIUS功能","配置到AAA Server的数据（IPSec隧道）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
当AAA Server（计费/鉴权AAA服务器）位于Internet中，UEG与计费/鉴权AAA服务器之间采用带外组网方式，建立IPSec隧道。适用于PGW-C、SMF

## 必备事项
前提条件

UEG与网络实体之间的网络环境已经构建完成。
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
          description: '已通过**ADD L3VPNINST**命令进行配置，可以使用****LST L3VPNINST****进行查询'
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
          description: '已通过**ADD L3VPNINST**命令进行配置，可以使用****LST L3VPNINST****进行查询'
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
        IFADMINSTATUS:
          name: '管理状态'
          type: string
          enum:
          - down
          - up
          required: false
          description: ''
          data_source: '本端规划'
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
          description: '已通过****ADD INTERFACE****命令进行配置，可以使用**LST INTERFACE**进行查询。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        IFIPADDR:
          name: 'IPv4地址'
          type: string
          maxLength: 15
          required: true
          description: '对应IPsec隧道的Tunnel接口所使用的IPv4地址和地址掩码。'
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
    add_ipbindvpn_list:
      type: items
      properties:
        IFNAME:
          name: '接口名'
          type: string
          maxLength: 63
          required: true
          description: '对应IPsec隧道的Tunnel接口名称。已通过****ADD INTERFACE****命令进行配置，可以使用****LST INTERFACE****进行查询。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: true
          description: '对应IPsec隧道所使用的VPN实例。已通过**ADD L3VPNINST**命令进行配置，可以使用****LST L3VPNINST****进行查询'
          data_source: '已配置数据中获取'
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
        DESTVRFNAME:
          name: '下一跳VPN名字'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IFNAME:
          name: '路由出接口名字'
          type: string
          maxLength: 63
          required: false
          description: '已通过****ADD INTERFACE****命令进行配置，可以使用**LST INTERFACE**进行查询。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_aclgroup_list:
      type: items
      properties:
        ACLNAME:
          name: 'ACL规则组标识'
          type: string
          maxLength: 32
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_aclruleadv4_list:
      type: items
      properties:
        ACLNAME:
          name: 'ACL规则组标识'
          type: string
          maxLength: 32
          required: true
          description: '已通过**ADD ACLGROUP**命令进行配置，可以使用**LST ACLGROUP**进行查询。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        ACLRULENAME:
          name: '规则名称'
          type: string
          maxLength: 32
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        ACLACTION:
          name: '规则行为'
          type: string
          enum:
          - Deny
          - Permit
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        ACLPROTOCOL:
          name: '协议类型值'
          type: integer
          minimum: 0
          maximum: 255
          required: true
          description: ''
          data_source: '与对端协商'
          pattern: ''
          default: ''
        ACLSOURCEIP:
          name: '源IP地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: '0.0.0.0'
        ACLSRCWILD:
          name: '源IP地址反掩码'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: '255.255.255.255'
        ACLDESTIP:
          name: '目的IP地址'
          type: string
          maxLength: 15
          required: false
          description: 'IPSec隧道的目的IP地址，为IPSec隧道终结端的设备IP地址。'
          data_source: '全网规划'
          pattern: ''
          default: '0.0.0.0'
    add_ipsecproposal_list:
      type: items
      properties:
        PROPOSALNAME:
          name: 'Proposal名称'
          type: string
          maxLength: 15
          required: true
          description: '要求与对端的加密算法配置一致。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPSECPROTOCOL:
          name: 'IPsec安全协议'
          type: string
          enum:
          - ah
          - esp
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: esp
        ESPAUTHALGO:
          name: 'ESP认证算法'
          type: string
          enum:
          - md5
          - 'null'
          - sha1
          - sha2_256
          - sha2_384
          - sha2_512
          - unconfigure
          required: false
          description: ''
          data_source: '与对端协商'
          pattern: ''
          default: sha2_256
        ESPENCRYPTALGO:
          name: 'ESP加密算法'
          type: string
          enum:
          - 3des
          - aes_128
          - aes_192
          - aes_256
          - des
          - 'null'
          - unconfigure
          required: false
          description: ''
          data_source: '与对端协商'
          pattern: ''
          default: aes_256
        ENCAPMODE:
          name: '封装模式'
          type: string
          enum:
          - transport
          required: false
          description: ''
          data_source: '与对端协商'
          pattern: ''
          default: transport
    add_ipsecintfcfg_list:
      type: items
      properties:
        INTERFACENAME:
          name: '接口名称'
          type: string
          maxLength: 63
          required: true
          description: '已通过****ADD INTERFACE****命令进行配置，可以使用****LST INTERFACE****进行查询。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        TNLTYPE:
          name: 'Tunnel口协议类型'
          type: string
          enum:
          - IPSEC
          - IPSEC6
          required: true
          description: '-'
          data_source: '固定取值'
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
    add_cplogicinf_list:
      type: items
      properties:
        NAME:
          name: '逻辑接口名称'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: ''
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
          data_source: ''
          pattern: ''
          default: ''
        IPV4ADDRESS1:
          name: '逻辑接口的IPv4地址1'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV4MASK1:
          name: '逻辑接口的IPv4掩码1'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VPNINSTANCE:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: ''
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
          description: '当UEG的产品形态为风筝L时，已通过**ADD CPVPNINST**配置，可以使用**LST CPVPNINST**命令进行查询。'
          data_source: '全网规划'
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
          description: '当UEG的产品形态为风筝L时，已通过**ADD CPLOGICINF**配置，可以使用****LST CPLOGICINF****命令进行查询。'
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
          description: '当UEG的产品形态为风筝L时，已通过**ADD CPAPN**配置，可以使用****LST CPAPN****命令进行查询。'
          data_source: '全网规划'
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
    - VRFNAME: 'vpn_pdn'
    add_vpninstaf_list:
    - VRFNAME: 'vpn_pdn'
      AFTYPE: ipv4uni
      VRFLABELMODE: perRoute
    add_l3vpninst_list_1:
    - VRFNAME: 'vpn_aaa'
    add_vpninstaf_list_1:
    - VRFNAME: 'vpn_aaa'
      AFTYPE: ipv4uni
      VRFLABELMODE: perRoute
    add_interface_list:
    - IFNAME: 'Tunnel1'
      IFADMINSTATUS: up
    add_ifipv4address_list:
    - IFNAME: 'Tunnel1'
      IFIPADDR: '10.1.1.1'
      SUBNETMASK: '255.255.255.240'
    add_ipbindvpn_list:
    - IFNAME: 'Tunnel1'
      VRFNAME: 'vpn_aaa'
    add_srroute_list:
    - AFTYPE: ipv4unicast
      PREFIX: '10.1.128.23'
      MASKLENGTH: 32
      VRFNAME: 'vpn_aaa'
      DESTVRFNAME: 'vpn_aaa'
      IFNAME: 'Tunnel1'
    add_aclgroup_list:
    - ACLNAME: '3101'
    add_aclruleadv4_list:
    - ACLNAME: '3101'
      ACLRULENAME: 'rule_10'
      ACLACTION: Permit
      ACLPROTOCOL: 17
      ACLSOURCEIP: '10.1.1.1'
      ACLSRCWILD: '0.0.0.0'
      ACLDESTIP: '10.1.1.2'
    add_ipsecproposal_list:
    - PROPOSALNAME: 'proposal_propo1'
      IPSECPROTOCOL: esp
      ESPAUTHALGO: sha2_256
      ESPENCRYPTALGO: aes_256
      ENCAPMODE: transport
    add_ipsecintfcfg_list:
    - INTERFACENAME: 'Tunnel1'
      TNLTYPE: IPSEC
    add_cpvpninst_list:
    - VPNINSTANCE: 'vpn_pdn'
    add_logicip_list:
    - IPVERSION: IPv4
      LOGICIPV4: '10.8.20.1'
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
      SERVERIPV4: '10.1.128.23'
      PORT: 1812
      VPNINSTANCE: 'vpn_aaa'
      CIPHERKEY: '*****'
      CIPHERKEYCNFM: '*****'
      PRIFLAG: PRIMARY
    add_rdssvr_list_1:
    - RDSSVRGRPNAME: 'isprg'
      SERVERTYPE: AUTHENTICATION
      IPVERSION: IPV4
      SERVERIPV4: '10.1.128.23'
      PORT: 1812
      CIPHERKEY: 'ispchina'
      PRIFLAG: PRIMARY
      VPNINSTANCE: 'vpn_aaa'
      CIPHERKEYCNFM: 'ispchina'
    add_rdssvr_list_2:
    - RDSSVRGRPNAME: 'isprg'
      SERVERTYPE: ACCOUNTING
      IPVERSION: IPV4
      SERVERIPV4: '10.1.128.23'
      PORT: 1813
      VPNINSTANCE: 'vpn_aaa'
      CIPHERKEY: '*****'
      CIPHERKEYCNFM: '*****'
      PRIFLAG: PRIMARY
    add_rdssvr_list_3:
    - RDSSVRGRPNAME: 'isprg'
      SERVERTYPE: ACCOUNTING
      IPVERSION: IPV4
      SERVERIPV4: '10.1.128.23'
      PORT: 1813
      CIPHERKEY: 'ispchina'
      PRIFLAG: PRIMARY
      VPNINSTANCE: 'vpn_aaa'
      CIPHERKEYCNFM: 'ispchina'
    add_cpapn_list:
    - APN: 'apn1'
      HASVPN: ENABLE
      VPNINSTANCE: 'vpn_pdn'
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
    {#- --- 可选参数 --- -#}
    {%- if item.VRFLABELMODE is not none -%}
        VRFLABELMODE={{item.VRFLABELMODE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 配置IPsec的Tunnel接口。

### ****ADD INTERFACE****

### ****ADD IFIPV4ADDRESS****

### ****ADD IPBINDVPN****

```jinja2
{%- for item in add_interface_list -%}
    ADD INTERFACE:
    {#- --- 必选参数 --- -#}
    IFNAME="{{item.IFNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.IFADMINSTATUS is not none -%}
        IFADMINSTATUS={{item.IFADMINSTATUS}},
    {%- endif -%}
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

```jinja2
{%- for item in add_ipbindvpn_list -%}
    ADD IPBINDVPN:
    {#- --- 必选参数 --- -#}
    IFNAME="{{item.IFNAME}}",
    VRFNAME="{{item.VRFNAME}}",
    ;
{%- endfor -%}
```

### 5 配置静态路由。

### ****ADD SRROUTE****

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
    {%- if item.DESTVRFNAME is not none -%}
        DESTVRFNAME="{{item.DESTVRFNAME}}",
    {%- endif -%}
    {%- if item.IFNAME is not none -%}
        IFNAME="{{item.IFNAME}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 6 配置安全策略为IKE协商方式时的IPSec数据。

#### 6.1 配置数据流的访问控制规则。

```jinja2
{%- for item in add_aclgroup_list -%}
    ADD ACLGROUP:
    {#- --- 必选参数 --- -#}
    ACLNAME="{{item.ACLNAME}}",
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_aclruleadv4_list -%}
    ADD ACLRULEADV4:
    {#- --- 必选参数 --- -#}
    ACLNAME="{{item.ACLNAME}}",
    ACLRULENAME="{{item.ACLRULENAME}}",
    ACLACTION={{item.ACLACTION}},
    ACLPROTOCOL={{item.ACLPROTOCOL}},
    {#- --- 可选参数 --- -#}
    {%- if item.ACLSOURCEIP is not none -%}
        ACLSOURCEIP="{{item.ACLSOURCEIP}}",
    {%- endif -%}
    {%- if item.ACLSRCWILD is not none -%}
        ACLSRCWILD="{{item.ACLSRCWILD}}",
    {%- endif -%}
    {%- if item.ACLDESTIP is not none -%}
        ACLDESTIP="{{item.ACLDESTIP}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 6.2 配置IPsec安全提议。

```jinja2
{%- for item in add_ipsecproposal_list -%}
    ADD IPSECPROPOSAL:
    {#- --- 必选参数 --- -#}
    PROPOSALNAME="{{item.PROPOSALNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.IPSECPROTOCOL is not none -%}
        IPSECPROTOCOL={{item.IPSECPROTOCOL}},
    {%- endif -%}
    {%- if item.ENCAPMODE is not none -%}
        ENCAPMODE={{item.ENCAPMODE}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：IPSECPROTOCOL=esp 时可选 --- -#}
    {%- if item.IPSECPROTOCOL == 'esp' -%}
        {%- if item.ESPAUTHALGO is not none -%}
            ESPAUTHALGO={{item.ESPAUTHALGO}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：IPSECPROTOCOL=esp 时可选 --- -#}
    {%- if item.IPSECPROTOCOL == 'esp' -%}
        {%- if item.ESPENCRYPTALGO is not none -%}
            ESPENCRYPTALGO={{item.ESPENCRYPTALGO}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 6.3 在Tunnel接口上应用安全策略。

```jinja2
{%- for item in add_ipsecintfcfg_list -%}
    ADD IPSECINTFCFG:
    {#- --- 必选参数 --- -#}
    INTERFACENAME="{{item.INTERFACENAME}}",
    TNLTYPE={{item.TNLTYPE}},
    ;
{%- endfor -%}
```

### 7 创建VPN实例。

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

### 8 配置Gi逻辑接口。

```jinja2
{%- for item in add_logicip_list -%}
    ADD LOGICIP:
    {#- --- 必选参数 --- -#}
    IPVERSION={{item.IPVERSION}},
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

### 9 **可选：**配置鉴权或计费AAA服务器使用的PGW-U/UPF列表。

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

### 10 配置鉴权/计费AAA服务器。

#### 10.1 配置AAA服务器组以及服务器的工作模式。

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

#### 10.2 设置主用鉴权AAA服务器的IP地址、目的端口号、所属VPN、密钥。

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

#### 10.3 **可选：**设置备用鉴权AAA服务器的IP地址、目的端口号、所属VPN、密钥。

```jinja2
{%- if is_optional_backup_auth_aaa_server -%}
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

#### 10.4 配置主用计费AAA服务器的IP地址、目的端口号、所属VPN、密钥。

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

#### 10.5 **可选：**配置备用计费AAA服务器的IP地址、目的端口号、所属VPN、密钥。

```jinja2
{%- if is_optional_backup_accounting_aaa_server -%}
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

#### 10.6 配置APN。

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

#### 10.7 配置APN下的Client-IP。

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

#### 10.8 APN实例下绑定RADIUS服务器组。

```jinja2
{%- for item in add_apnrdssvrgrp_list -%}
    ADD APNRDSSVRGRP:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    RDSSVRGRPNAME="{{item.RDSSVRGRPNAME}}",
    ;
{%- endfor -%}
```


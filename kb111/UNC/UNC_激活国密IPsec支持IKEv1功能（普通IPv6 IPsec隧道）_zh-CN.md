---
id: ''
name: 激活国密IPsec支持IKEv1功能（普通IPv6 IPsec隧道）
ne_type: UNC
type: feature
description: 如图1所示，网络A和网络B之间采用网关对网关组网模式进行资源传输。网络A和网络B分别通过Device A和Device B连接到Internet，要求通过配置IPsec隧道实现PCA与PCB之间可以安全地互访。  **图1** IPv6 IPsec组网图  网络环境描述如下：  * 网络A属于2001:db8:1::/64子网，通过接口interface 2与Device A连接。 * 网络B属于2001:db8:4::/64子网，通过接口interface 2与Device B连接。 * Device A和Device B路由可达。假设Device A往Device B方向下一跳地址为2001:db8:1:1:1::2/64，Device B往Device A方向下一跳地址为2001:db8:1:0:2::2/64。    **表1** 设备接口IP地址（普通IPv6 IPsec隧道）    | 设备名称 | 接口 | IP地址 |   | --- | --- | --- |   | Device A VNRS微服务 | Ethernet66/0/5 | 2001:db8:1::1/64 |   | Device A VNRS微服务 | Ethernet66/0/6 | 2001:db8:1:1:1::1/64 |   | Device A VNRS微服务 | Tunnel27 | 2001:db8:1::1:0:1（需要双配） |   | Device B VNRS微服务 | Ethernet66/0/5 | 2001:db8:4::1/64 |   | Device B VNRS微服务 | Ethernet66/0/6 | 2001:db8:1:0:2::1/64 |   | Device B VNRS微服务 | Tunnel27 | 2001:db8:4::1:0:1（需要双配） |   | Device A IPsec微服务 | Tunnel27 | 2001:db8:1::1:0:1（IKE协商IP地址） |   | Device B IPsec微服务 | Tunnel27 | 2001:db8:4::1:0:1（IKE协商IP地址） |   | PCA | - | 2001:db8:1::2/64 |   | PCB | - | 2001:db8:4::2/64 |   | - | Device A侧网关接口 | 2001:db8:1:1:1::2/64 |   | - | Device B侧网关接口 | 2001:db8:1:0:2::2/64 |
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","IP基本功能","IPFD-016000 IPSec功能","特性配置","激活国密IPsec支持IKEv1功能（普通IPv6 IPsec隧道）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
如图1所示，网络A和网络B之间采用网关对网关组网模式进行资源传输。网络A和网络B分别通过Device A和Device B连接到Internet，要求通过配置IPsec隧道实现PCA与PCB之间可以安全地互访。**图1** IPv6 IPsec组网图网络环境描述如下：* 网络A属于2001:db8:1::/64子网，通过接口interface 2与Device A连接。* 网络B属于2001:db8:4::/64子网，通过接口interface 2与Device B连接。* Device A和Device B路由可达。假设Device A往Device B方向下一跳地址为2001:db8:1:1:1::2/64，Device B往Device A方向下一跳地址为2001:db8:1:0:2::2/64。  **表1** 设备接口IP地址（普通IPv6 IPsec隧道）  | 设备名称 | 接口 | IP地址 |  | --- | --- | --- |  | Device A VNRS微服务 | Ethernet66/0/5 | 2001:db8:1::1/64 |  | Device A VNRS微服务 | Ethernet66/0/6 | 2001:db8:1:1:1::1/64 |  | Device A VNRS微服务 | Tunnel27 | 2001:db8:1::1:0:1（需要双配） |  | Device B VNRS微服务 | Ethernet66/0/5 | 2001:db8:4::1/64 |  | Device B VNRS微服务 | Ethernet66/0/6 | 2001:db8:1:0:2::1/64 |  | Device B VNRS微服务 | Tunnel27 | 2001:db8:4::1:0:1（需要双配） |  | Device A IPsec微服务 | Tunnel27 | 2001:db8:1::1:0:1（IKE协商IP地址） |  | Device B IPsec微服务 | Tunnel27 | 2001:db8:4::1:0:1（IKE协商IP地址） |  | PCA | - | 2001:db8:1::2/64 |  | PCB | - | 2001:db8:4::2/64 |  | - | Device A侧网关接口 | 2001:db8:1:1:1::2/64 |  | - | Device B侧网关接口 | 2001:db8:1:0:2::2/64 |

## 必备事项
前提条件

* 操作人员已经登录网管。
* 配置接口的IP地址。
* 配置路由，使隧道两端路由可达。
* IPSec功能由IPSec服务承载，请完成IPSec安装，参见**软件安装**章节中的“安装可选服务 > 安装IPSec服务”。
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
          description: ''
          data_source: ''
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
    mod_interface_list:
      type: items
      properties:
        IFNAME:
          name: '接口名'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: ''
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
          data_source: ''
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
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_ifipv6enable_list:
      type: items
      properties:
        IFNAME:
          name: '接口名'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ENABLEFLAG:
          name: 'IPv6使能标志'
          type: string
          enum:
          - FALSE
          - TRUE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AUTOLINKLOCAL:
          name: '自动生成链路层地址标志'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MTU:
          name: 'IPv6接口最大传输单元（byte）'
          type: integer
          minimum: 1280
          maximum: 9600
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_ifipv6address_list:
      type: items
      properties:
        IFNAME:
          name: '接口名'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6ADDRESS:
          name: 'IPv6地址'
          type: string
          maxLength: 39
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PREFIXLEN:
          name: 'IPv6地址前缀'
          type: integer
          minimum: 1
          maximum: 128
          required: true
          description: ''
          data_source: ''
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
          description: ''
          data_source: ''
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
          data_source: ''
          pattern: ''
          default: ''
    set_ifipv6enable_list_4:
      type: items
      properties:
        IFNAME:
          name: '接口名'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ENABLEFLAG:
          name: 'IPv6使能标志'
          type: string
          enum:
          - FALSE
          - TRUE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AUTOLINKLOCAL:
          name: '自动生成链路层地址标志'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MTU:
          name: 'IPv6接口最大传输单元（byte）'
          type: integer
          minimum: 1280
          maximum: 9600
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_ipsecintfcfg_list:
      type: items
      properties:
        INTERFACENAME:
          name: '接口名称'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TNLTYPE:
          name: 'Tunnel口协议类型'
          type: string
          enum:
          - IPSEC
          - IPSEC6
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_ipbindvpn_list_4:
      type: items
      properties:
        IFNAME:
          name: '接口名'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_ifipv6address_list_4:
      type: items
      properties:
        IFNAME:
          name: '接口名'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6ADDRESS:
          name: 'IPv6地址'
          type: string
          maxLength: 39
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PREFIXLEN:
          name: 'IPv6地址前缀'
          type: integer
          minimum: 1
          maximum: 128
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_srroute6_list:
      type: items
      properties:
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: '_public_'
        AFTYPE:
          name: '地址族'
          type: string
          enum:
          - ipv6unicast
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PREFIX:
          name: '路由前缀'
          type: string
          maxLength: 39
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MASKLENGTH:
          name: '路由前缀长度'
          type: integer
          minimum: 0
          maximum: 128
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DESTVRFNAME:
          name: '下一跳VPN名字'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NEXTHOP:
          name: '路由下一跳'
          type: string
          maxLength: 39
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
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_l3vpninstipsec_list:
      type: items
      properties:
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          minLength: 1
          maxLength: 31
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_vpninstafipsec_list:
      type: items
      properties:
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          minLength: 1
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
          - Ipv4uni
          - Ipv6uni
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_interfaceipsec_list:
      type: items
      properties:
        IFNAME:
          name: '接口名'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IFADMINSTATUS:
          name: '管理状态'
          type: string
          enum:
          - Down
          - Up
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_ifipv6enableipsec_list:
      type: items
      properties:
        IFNAME:
          name: '接口名'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ENABLEFLAG:
          name: 'IPv6使能标志'
          type: string
          enum:
          - FALSE
          - TRUE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IFMTU6:
          name: 'IPv6接口最大传输单元(字节)'
          type: integer
          minimum: 1280
          maximum: 9600
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_ipbindvpnipsec_list:
      type: items
      properties:
        IFNAME:
          name: '接口名'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          minLength: 1
          maxLength: 31
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_ifipv6addressipsec_list:
      type: items
      properties:
        IFNAME:
          name: '接口名'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IFIP6ADDR:
          name: 'IPv6地址'
          type: string
          maxLength: 39
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ADDRPREFIXLEN:
          name: 'IPv6地址前缀'
          type: integer
          minimum: 1
          maximum: 128
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_aclgroup6ipsec_list:
      type: items
      properties:
        ACLNAME:
          name: 'ACL规则组标识'
          type: string
          minLength: 1
          maxLength: 32
          required: true
          description: '通过ACL规则定义需要保护的数据流。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_aclruleadv6ipsec_list:
      type: items
      properties:
        ACLNAME:
          name: '高级ACL规则组标识'
          type: string
          minLength: 1
          maxLength: 32
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        ACLRULENAME:
          name: '规则名称'
          type: string
          minLength: 1
          maxLength: 32
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        ACLACTION:
          name: '规则行为'
          type: string
          enum:
          - Permit
          - Deny
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          minLength: 1
          maxLength: 31
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        ACLSOURCEIP:
          name: '源IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        ACLSRCWILD:
          name: '源IPv6地址正掩码'
          type: integer
          minimum: 0
          maximum: 128
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        ACLDESTIP:
          name: '目的IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        ACLDESTWILD:
          name: '目的IPv6地址正掩码'
          type: integer
          minimum: 0
          maximum: 128
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        ACLPROTOCOLTYPE:
          name: '协议选项类型'
          type: string
          enum:
          - Number
          - WellKnow
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: Number
        ACLPROTOCOL:
          name: '协议类型值'
          type: integer
          minimum: 0
          maximum: 255
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        ACLPROTOCOLNAME:
          name: '协议名称'
          type: string
          enum:
          - GRE
          - HOPOPT
          - ICMPv6
          - IPv6
          - IPv6_AH
          - IPv6_ESP
          - OSPF
          - TCP
          - UDP
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_aclgroup6ipsec_list_1:
      type: items
      properties:
        ACLNAME:
          name: 'ACL规则组标识'
          type: string
          minLength: 1
          maxLength: 32
          required: true
          description: '通过ACL规则定义需要保护的数据流。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_aclruleadv6ipsec_list_2:
      type: items
      properties:
        ACLNAME:
          name: '高级ACL规则组标识'
          type: string
          minLength: 1
          maxLength: 32
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        ACLRULENAME:
          name: '规则名称'
          type: string
          minLength: 1
          maxLength: 32
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        ACLACTION:
          name: '规则行为'
          type: string
          enum:
          - Permit
          - Deny
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          minLength: 1
          maxLength: 31
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        ACLSOURCEIP:
          name: '源IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        ACLSRCWILD:
          name: '源IPv6地址正掩码'
          type: integer
          minimum: 0
          maximum: 128
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        ACLDESTIP:
          name: '目的IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        ACLDESTWILD:
          name: '目的IPv6地址正掩码'
          type: integer
          minimum: 0
          maximum: 128
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        ACLPROTOCOLTYPE:
          name: '协议选项类型'
          type: string
          enum:
          - Number
          - WellKnow
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: Number
        ACLPROTOCOL:
          name: '协议类型值'
          type: integer
          minimum: 0
          maximum: 255
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        ACLPROTOCOLNAME:
          name: '协议名称'
          type: string
          enum:
          - GRE
          - HOPOPT
          - ICMPv6
          - IPv6
          - IPv6_AH
          - IPv6_ESP
          - OSPF
          - TCP
          - UDP
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_fwsoftpara_list:
      type: items
      properties:
        PARAMETERSTYPE:
          name: '参数类型'
          type: string
          enum:
          - DWORD
          - DWORD_EX
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DWORDINDEX:
          name: 'DWORD索引'
          type: integer
          minimum: 1
          maximum: 2048
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DWORDVALUE:
          name: 'DWORD取值'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        EXTENDDWORDINDEX:
          name: '扩展DWORD索引'
          type: integer
          minimum: 1
          maximum: 2048
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        EXTENDDWORDVALUE:
          name: '扩展DWORD取值'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_ipsecproposalipsec_list:
      type: items
      properties:
        PROPOSALNAME:
          name: 'Proposal名称'
          type: string
          minLength: 1
          maxLength: 15
          required: true
          description: '配置IPsec安全提议。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPSECPROTOCOL:
          name: 'IPsec安全协议'
          type: string
          enum:
          - Ah
          - Esp
          - Ah_esp
          required: false
          description: ''
          data_source: '对端协商'
          pattern: ''
          default: Esp
        ESPAUTHALGO:
          name: 'ESP认证算法'
          type: string
          enum:
          - Md5
          - Sha1
          - Sha2_256
          - Sha2_384
          - Sha2_512
          - 'Null'
          - Unconfigure
          - Sm3
          required: false
          description: ''
          data_source: '对端协商'
          pattern: ''
          default: 'Null'
        ESPENCRYPTALGO:
          name: 'ESP加密算法'
          type: string
          enum:
          - Des
          - A3des
          - Aes_128
          - Aes_192
          - Aes_256
          - Unconfigure
          - Sm4
          - Aes_gcm_128
          - Aes_gcm_256
          - Aes_gmac_128
          - 'Null'
          required: false
          description: ''
          data_source: '对端协商'
          pattern: ''
          default: Aes_gcm_128
        ENCAPMODE:
          name: '封装模式'
          type: string
          enum:
          - Transport
          - Tunnel
          required: false
          description: ''
          data_source: '对端协商'
          pattern: ''
          default: Tunnel
        AHAUTHALGO:
          name: 'AH认证算法'
          type: string
          enum:
          - Md5
          - Sha1
          - Sha2_256
          - Sha2_384
          - Sha2_512
          - Unconfigure
          - Sm3
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: Sha2_256
    add_ikeproposal_list:
      type: items
      properties:
        PROPOSALNUMBER:
          name: '安全提议号'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: true
          description: '配置IKE安全提议。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        AUTHMETHOD:
          name: '认证方法'
          type: string
          enum:
          - Pre_share
          - Rsa_signature
          - Cert_signature
          - Digital_envelope
          required: false
          description: ''
          data_source: '对端协商'
          pattern: ''
          default: Pre_share
        ENCRALGORITHM:
          name: '加密算法'
          type: string
          enum:
          - Des_cbc
          - Aes_cbc_128
          - Aes_cbc_192
          - Aes_cbc_256
          - Alg_3Des_cbc
          - Aes_gcm_128
          - Aes_gcm_256
          - Sm4
          required: false
          description: ''
          data_source: '对端协商'
          pattern: ''
          default: Aes_gcm_128
        INTEGALGORITHM:
          name: '完整性算法'
          type: string
          enum:
          - Hmac_md5_96
          - Hmac_sha1_96
          - Hmac_sha2_256
          - Hmac_sha2_384
          - Aes_xcbc_96
          - Sm3
          - Hmac_sha2_512
          required: false
          description: ''
          data_source: '对端协商'
          pattern: ''
          default: Hmac_sha2_256
        ASYMENCRALG:
          name: '非对称加密算法'
          type: string
          enum:
          - 'NULL'
          - Sm2
          required: false
          description: ''
          data_source: '对端协商'
          pattern: ''
          default: Sm2
        SIGHASHALGNEGSW:
          name: '签名哈希算法协商开关'
          type: string
          enum:
          - Disable
          - Enable
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: Enable
    add_ikepeer6_list:
      type: items
      properties:
        PEERNAME:
          name: '对等体名称'
          type: string
          minLength: 1
          maxLength: 15
          required: true
          description: '配置IKE对等体。'
          data_source: '对端规划'
          pattern: ''
          default: ''
        PROPOSAL:
          name: '安全提议'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        LOWREMOTEADDR:
          name: '远程地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        INVRFNAME:
          name: 'SA绑定VPN名称'
          type: string
          minLength: 1
          maxLength: 47
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        OUTVRFNAME:
          name: '远程地址VPN名称'
          type: string
          minLength: 1
          maxLength: 47
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        VERSION2:
          name: '版本2'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: '对端协商'
          pattern: ''
          default: TRUE
        CERTLOCALFILE:
          name: '签名证书文件名'
          type: string
          minLength: 1
          maxLength: 127
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        ENCCERTLOCFILE:
          name: '加密证书文件名'
          type: string
          minLength: 1
          maxLength: 127
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_ipsecpolicy6_list:
      type: items
      properties:
        POLICYNAME:
          name: '策略名称'
          type: string
          minLength: 1
          maxLength: 15
          required: true
          description: '配置IPsec安全策略。  如果**ADD ACLGROUP6IPSEC**中的“规则组标识（ACLNAME）”配置为规则组编号，则IPsec策略中使用“ACL编号-IPV6（ACL6NUMBER）”；如果**ADD ACLGROUP6IPSEC**中的“规则组标识（ACLNAME）”配置为规则组名称，则IPsec策略中使用“ACL名称-ipv6（ACL6NAME）”。此处以ACL规则组编号为例。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SEQUENCENUMBER:
          name: '序列号'
          type: integer
          minimum: 1
          maximum: 10000
          required: true
          description: ''
          data_source: '对端协商'
          pattern: ''
          default: ''
        POLICYMODE:
          name: '策略模式'
          type: string
          enum:
          - Isakmp
          required: true
          description: ''
          data_source: '对端协商'
          pattern: ''
          default: ''
        TEMPLATEMODE:
          name: '模板模式'
          type: string
          enum:
          - None
          - PolicyTemplate
          required: true
          description: ''
          data_source: '对端协商'
          pattern: ''
          default: ''
        ACLTYPE:
          name: 'ACL类型'
          type: string
          enum:
          - AclIPv4
          - AclIPv6
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        ACL6NUMBER:
          name: 'ACL编号-IPV6'
          type: integer
          minimum:
          - 0
          - 3000
          maximum:
          - 0
          - 3999
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        ACL6NAME:
          name: 'ACL名称-IPv6'
          type: string
          minLength: 0
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ACLNAME:
          name: 'ACL名称'
          type: string
          minLength: 1
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ACLNUMBER:
          name: 'ACL编号'
          type: integer
          minimum:
          - 3000
          - 0
          maximum:
          - 3999
          - 0
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_propattachipsecproposal_list:
      type: items
      properties:
        POLICYNAME:
          name: '策略名称'
          type: string
          minLength: 1
          maxLength: 15
          required: true
          description: '在安全策略中引用安全提议。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SEQUENCENUMBER:
          name: '序列号'
          type: integer
          minimum: 1
          maximum: 10000
          required: true
          description: ''
          data_source: '对端协商'
          pattern: ''
          default: ''
        POLICYMODE:
          name: '策略模式'
          type: string
          enum:
          - Isakmp
          required: true
          description: ''
          data_source: '对端协商'
          pattern: ''
          default: ''
        TEMPLATEMODE:
          name: '模板模式'
          type: string
          enum:
          - None
          - PolicyTemplate
          required: true
          description: ''
          data_source: '对端协商'
          pattern: ''
          default: ''
        IPSECPROPNAME:
          name: 'IPsec安全提议名称'
          type: string
          minLength: 1
          maxLength: 15
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_attachikepeer_list:
      type: items
      properties:
        POLICYNAME:
          name: '策略名称'
          type: string
          minLength: 1
          maxLength: 15
          required: true
          description: '绑定安全策略和IKE对等体。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SEQUENCENUMBER:
          name: '序列号'
          type: integer
          minimum: 1
          maximum: 10000
          required: true
          description: ''
          data_source: '对端协商'
          pattern: ''
          default: ''
        POLICYMODE:
          name: '策略模式'
          type: string
          enum:
          - Isakmp
          required: true
          description: ''
          data_source: '对端协商'
          pattern: ''
          default: ''
        TEMPLATEMODE:
          name: '模板模式'
          type: string
          enum:
          - None
          - PolicyTemplate
          required: true
          description: ''
          data_source: '对端协商'
          pattern: ''
          default: ''
        IKEPEERNAME:
          name: 'IKE对等体名称'
          type: string
          minLength: 1
          maxLength: 15
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        PEERPRIORITY:
          name: '优先级'
          type: integer
          minimum: 1
          maximum: 3
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_ipsecintfcfgipsec_list:
      type: items
      properties:
        INTERFACENAME:
          name: '接口名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '应用IPsec安全策略。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        TNLTYPE:
          name: 'Tunnel口协议类型'
          type: string
          enum:
          - IPSEC
          - IPSEC6
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        POLICYNAME:
          name: '策略名称'
          type: string
          minLength: 1
          maxLength: 15
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
  examples:
    add_l3vpninst_list:
    - VRFNAME: 'vrf1'
    add_vpninstaf_list:
    - VRFNAME: 'vrf1'
      AFTYPE: ipv6uni
    mod_interface_list:
    - IFNAME: 'Ethernet66/0/5'
      IFADMINSTATUS: up
    add_ipbindvpn_list:
    - IFNAME: 'Ethernet66/0/5'
      VRFNAME: 'vrf1'
    set_ifipv6enable_list:
    - IFNAME: 'Ethernet66/0/5'
      ENABLEFLAG: TRUE
      AUTOLINKLOCAL: ''
      MTU: ''
    add_ifipv6address_list:
    - IFNAME: 'Ethernet66/0/5'
      IPV6ADDRESS: '2001:db8:1::1'
      PREFIXLEN: 96
    add_interface_list:
    - IFNAME: 'Tunnel27'
      IFADMINSTATUS: up
    set_ifipv6enable_list_4:
    - IFNAME: 'Tunnel27'
      ENABLEFLAG: TRUE
      AUTOLINKLOCAL: ''
      MTU: ''
    add_ipsecintfcfg_list:
    - INTERFACENAME: 'Tunnel27'
      TNLTYPE: IPSEC6
    add_ipbindvpn_list_4:
    - IFNAME: 'Tunnel27'
      VRFNAME: 'vrf1'
    add_ifipv6address_list_4:
    - IFNAME: 'Tunnel27'
      IPV6ADDRESS: '2001:db8:1::1:0:1'
      PREFIXLEN: 96
    add_srroute6_list:
    - VRFNAME: 'vrf1'
      AFTYPE: ipv6unicast
      PREFIX: '2001:db8:4::2'
      MASKLENGTH: 128
      DESTVRFNAME: 'vrf1'
      NEXTHOP: '2001:db8:4::1:0:1'
      IFNAME: 'Tunnel27'
    add_l3vpninstipsec_list:
    - VRFNAME: 'vrf1'
    add_vpninstafipsec_list:
    - VRFNAME: 'vrf1'
      AFTYPE: Ipv6uni
    add_interfaceipsec_list:
    - IFNAME: 'Tunnel27'
      IFADMINSTATUS: Up
    set_ifipv6enableipsec_list:
    - IFNAME: 'Tunnel27'
      ENABLEFLAG: TRUE
      IFMTU6: ''
    add_ipbindvpnipsec_list:
    - IFNAME: 'Tunnel27'
      VRFNAME: 'vrf1'
    add_ifipv6addressipsec_list:
    - IFNAME: 'Tunnel27'
      IFIP6ADDR: '2001:db8:1::1:0:1'
      ADDRPREFIXLEN: 96
    add_aclgroup6ipsec_list:
    - ACLNAME: '3027'
    add_aclruleadv6ipsec_list:
    - ACLNAME: '3027'
      ACLRULENAME: 'rule27_1'
      ACLACTION: Permit
      VRFNAME: 'vrf1'
      ACLSOURCEIP: '2001:db8:1::2'
      ACLSRCWILD: 128
      ACLDESTIP: '2001:db8:4::2'
      ACLDESTWILD: 128
      ACLPROTOCOLTYPE: Number
      ACLPROTOCOL: 0
      ACLPROTOCOLNAME: ''
    add_aclgroup6ipsec_list_1:
    - ACLNAME: '3027'
    add_aclruleadv6ipsec_list_2:
    - ACLNAME: '3027'
      ACLRULENAME: 'rule27_1'
      ACLACTION: Permit
      VRFNAME: 'vrf1'
      ACLSOURCEIP: '2001:db8:4::2'
      ACLSRCWILD: 128
      ACLDESTIP: '2001:db8:1::2'
      ACLDESTWILD: 128
      ACLPROTOCOLTYPE: Number
      ACLPROTOCOL: 0
      ACLPROTOCOLNAME: ''
    set_fwsoftpara_list:
    - PARAMETERSTYPE: DWORD
      DWORDINDEX: 1401
      DWORDVALUE: 1
      EXTENDDWORDINDEX: ''
      EXTENDDWORDVALUE: ''
    add_ipsecproposalipsec_list:
    - PROPOSALNAME: 'tran1'
      IPSECPROTOCOL: Esp
      ESPAUTHALGO: Sha2_256
      ESPENCRYPTALGO: Aes_256
      ENCAPMODE: Tunnel
      AHAUTHALGO: Sha2_256
    add_ikeproposal_list:
    - PROPOSALNUMBER: 10
      AUTHMETHOD: Digital_envelope
      ENCRALGORITHM: Sm4
      INTEGALGORITHM: Sm3
      ASYMENCRALG: Sm2
      SIGHASHALGNEGSW: Enable
    add_ikepeer6_list:
    - PEERNAME: 'b'
      PROPOSAL: 10
      LOWREMOTEADDR: '2001:db8:4::1:0:1'
      INVRFNAME: 'vrf1'
      OUTVRFNAME: 'vrf1'
      VERSION2: FALSE
      CERTLOCALFILE: 'sm2_c_sig.cer'
      ENCCERTLOCFILE: 'sm2_c_enc.cer'
    add_ipsecpolicy6_list:
    - POLICYNAME: 'map1'
      SEQUENCENUMBER: 10
      POLICYMODE: Isakmp
      TEMPLATEMODE: None
      ACLTYPE: AclIPv6
      ACL6NUMBER: 3027
      ACL6NAME: ''
      ACLNAME: ''
      ACLNUMBER: ''
    add_propattachipsecproposal_list:
    - POLICYNAME: 'map1'
      SEQUENCENUMBER: 10
      POLICYMODE: Isakmp
      TEMPLATEMODE: None
      IPSECPROPNAME: 'tran1'
    add_attachikepeer_list:
    - POLICYNAME: 'map1'
      SEQUENCENUMBER: 10
      POLICYMODE: Isakmp
      TEMPLATEMODE: None
      IKEPEERNAME: 'b'
      PEERPRIORITY: 1
    add_ipsecintfcfgipsec_list:
    - INTERFACENAME: 'Tunnel27'
      TNLTYPE: IPSEC6
      POLICYNAME: 'map1'
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 创建VNRS微服务的VPN和IPsec隧道接口，并配置到达目的网络的静态路由。

#### 1.1 创建VPN实例。

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
    ;
{%- endfor -%}
```

#### 1.2 将与VPN网络连接的接口与VPN实例绑定，并配置接口IP地址。

```jinja2
{%- for item in mod_interface_list -%}
    MOD INTERFACE:
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
{%- for item in add_ipbindvpn_list -%}
    ADD IPBINDVPN:
    {#- --- 必选参数 --- -#}
    IFNAME="{{item.IFNAME}}",
    VRFNAME="{{item.VRFNAME}}",
    ;
{%- endfor -%}
```

```jinja2
{%- for item in set_ifipv6enable_list -%}
    SET IFIPV6ENABLE:
    {#- --- 必选参数 --- -#}
    IFNAME="{{item.IFNAME}}",
    ENABLEFLAG={{item.ENABLEFLAG}},
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：ENABLEFLAG=TRUE 时可选 --- -#}
    {%- if item.ENABLEFLAG == 'TRUE' -%}
        {%- if item.AUTOLINKLOCAL is not none -%}
            AUTOLINKLOCAL={{item.AUTOLINKLOCAL}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：ENABLEFLAG=TRUE 时可选 --- -#}
    {%- if item.ENABLEFLAG == 'TRUE' -%}
        {%- if item.MTU is not none -%}
            MTU={{item.MTU}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_ifipv6address_list -%}
    ADD IFIPV6ADDRESS:
    {#- --- 必选参数 --- -#}
    IFNAME="{{item.IFNAME}}",
    IPV6ADDRESS="{{item.IPV6ADDRESS}}",
    PREFIXLEN={{item.PREFIXLEN}},
    ;
{%- endfor -%}
```

#### 1.3 创建IPsec隧道接口，并将IPsec隧道接口与VPN实例绑定。

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
{%- for item in set_ifipv6enable_list_4 -%}
    SET IFIPV6ENABLE:
    {#- --- 必选参数 --- -#}
    IFNAME="{{item.IFNAME}}",
    ENABLEFLAG={{item.ENABLEFLAG}},
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：ENABLEFLAG=TRUE 时可选 --- -#}
    {%- if item.ENABLEFLAG == 'TRUE' -%}
        {%- if item.AUTOLINKLOCAL is not none -%}
            AUTOLINKLOCAL={{item.AUTOLINKLOCAL}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：ENABLEFLAG=TRUE 时可选 --- -#}
    {%- if item.ENABLEFLAG == 'TRUE' -%}
        {%- if item.MTU is not none -%}
            MTU={{item.MTU}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_ipsecintfcfg_list -%}
    ADD IPSECINTFCFG:
    {#- --- 必选参数 --- -#}
    INTERFACENAME="{{item.INTERFACENAME}}",
    TNLTYPE={{item.TNLTYPE}},
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_ipbindvpn_list_4 -%}
    ADD IPBINDVPN:
    {#- --- 必选参数 --- -#}
    IFNAME="{{item.IFNAME}}",
    VRFNAME="{{item.VRFNAME}}",
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_ifipv6address_list_4 -%}
    ADD IFIPV6ADDRESS:
    {#- --- 必选参数 --- -#}
    IFNAME="{{item.IFNAME}}",
    IPV6ADDRESS="{{item.IPV6ADDRESS}}",
    PREFIXLEN={{item.PREFIXLEN}},
    ;
{%- endfor -%}
```

#### 1.4 配置到达目的网络的静态路由，并与VPN实例绑定。

```jinja2
{%- for item in add_srroute6_list -%}
    ADD SRROUTE6:
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
    {%- if item.NEXTHOP is not none -%}
        NEXTHOP="{{item.NEXTHOP}}",
    {%- endif -%}
    {%- if item.IFNAME is not none -%}
        IFNAME="{{item.IFNAME}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 2 创建IPsec微服务的VPN和IPsec隧道接口。

#### 2.1 创建VPN实例。

```jinja2
{%- for item in add_l3vpninstipsec_list -%}
    ADD L3VPNINSTIPSEC:
    {#- --- 必选参数 --- -#}
    VRFNAME="{{item.VRFNAME}}",
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_vpninstafipsec_list -%}
    ADD VPNINSTAFIPSEC:
    {#- --- 必选参数 --- -#}
    VRFNAME="{{item.VRFNAME}}",
    AFTYPE={{item.AFTYPE}},
    ;
{%- endfor -%}
```

#### 2.2 创建IPsec隧道接口，并将IPsec隧道接口与VPN实例绑定。

```jinja2
{%- for item in add_interfaceipsec_list -%}
    ADD INTERFACEIPSEC:
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
{%- for item in set_ifipv6enableipsec_list -%}
    SET IFIPV6ENABLEIPSEC:
    {#- --- 必选参数 --- -#}
    IFNAME="{{item.IFNAME}}",
    ENABLEFLAG={{item.ENABLEFLAG}},
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：ENABLEFLAG=TRUE 时可选 --- -#}
    {%- if item.ENABLEFLAG == 'TRUE' -%}
        {%- if item.IFMTU6 is not none -%}
            IFMTU6={{item.IFMTU6}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_ipbindvpnipsec_list -%}
    ADD IPBINDVPNIPSEC:
    {#- --- 必选参数 --- -#}
    IFNAME="{{item.IFNAME}}",
    VRFNAME="{{item.VRFNAME}}",
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_ifipv6addressipsec_list -%}
    ADD IFIPV6ADDRESSIPSEC:
    {#- --- 必选参数 --- -#}
    IFNAME="{{item.IFNAME}}",
    IFIP6ADDR="{{item.IFIP6ADDR}}",
    ADDRPREFIXLEN={{item.ADDRPREFIXLEN}},
    ;
{%- endfor -%}
```

### 3 定义需要保护的数据流。由用户根据ACL规则来定义，根据不同的数据流特征，定义不同的ACL规则。

```jinja2
{%- for item in add_aclgroup6ipsec_list -%}
    ADD ACLGROUP6IPSEC:
    {#- --- 必选参数 --- -#}
    ACLNAME="{{item.ACLNAME}}",
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_aclruleadv6ipsec_list -%}
    ADD ACLRULEADV6IPSEC:
    {#- --- 必选参数 --- -#}
    ACLNAME="{{item.ACLNAME}}",
    ACLRULENAME="{{item.ACLRULENAME}}",
    ACLACTION={{item.ACLACTION}},
    ACLPROTOCOL={{item.ACLPROTOCOL}},
    {#- --- 可选参数 --- -#}
    {%- if item.VRFNAME is not none -%}
        VRFNAME="{{item.VRFNAME}}",
    {%- endif -%}
    {%- if item.ACLSOURCEIP is not none -%}
        ACLSOURCEIP="{{item.ACLSOURCEIP}}",
    {%- endif -%}
    {%- if item.ACLSRCWILD is not none -%}
        ACLSRCWILD={{item.ACLSRCWILD}},
    {%- endif -%}
    {%- if item.ACLDESTIP is not none -%}
        ACLDESTIP="{{item.ACLDESTIP}}",
    {%- endif -%}
    {%- if item.ACLDESTWILD is not none -%}
        ACLDESTWILD={{item.ACLDESTWILD}},
    {%- endif -%}
    {%- if item.ACLPROTOCOLTYPE is not none -%}
        ACLPROTOCOLTYPE={{item.ACLPROTOCOLTYPE}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：ACLPROTOCOLTYPE=WellKnow 时必选 --- -#}
    {%- if item.ACLPROTOCOLTYPE == 'WellKnow' -%}
        ACLPROTOCOLNAME={{item.ACLPROTOCOLNAME}},
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_aclgroup6ipsec_list_1 -%}
    ADD ACLGROUP6IPSEC:
    {#- --- 必选参数 --- -#}
    ACLNAME="{{item.ACLNAME}}",
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_aclruleadv6ipsec_list_2 -%}
    ADD ACLRULEADV6IPSEC:
    {#- --- 必选参数 --- -#}
    ACLNAME="{{item.ACLNAME}}",
    ACLRULENAME="{{item.ACLRULENAME}}",
    ACLACTION={{item.ACLACTION}},
    ACLPROTOCOL={{item.ACLPROTOCOL}},
    {#- --- 可选参数 --- -#}
    {%- if item.VRFNAME is not none -%}
        VRFNAME="{{item.VRFNAME}}",
    {%- endif -%}
    {%- if item.ACLSOURCEIP is not none -%}
        ACLSOURCEIP="{{item.ACLSOURCEIP}}",
    {%- endif -%}
    {%- if item.ACLSRCWILD is not none -%}
        ACLSRCWILD={{item.ACLSRCWILD}},
    {%- endif -%}
    {%- if item.ACLDESTIP is not none -%}
        ACLDESTIP="{{item.ACLDESTIP}}",
    {%- endif -%}
    {%- if item.ACLDESTWILD is not none -%}
        ACLDESTWILD={{item.ACLDESTWILD}},
    {%- endif -%}
    {%- if item.ACLPROTOCOLTYPE is not none -%}
        ACLPROTOCOLTYPE={{item.ACLPROTOCOLTYPE}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：ACLPROTOCOLTYPE=WellKnow 时必选 --- -#}
    {%- if item.ACLPROTOCOLTYPE == 'WellKnow' -%}
        ACLPROTOCOLNAME={{item.ACLPROTOCOLNAME}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### ACL只支持源IP和目的IP的配置，如果配置了端口，不会对端口配置生效。

### 4 执行**SET FWSOFTPARA**命令，设置**DWORD 1401**，打开国密算法开关。

```jinja2
{%- for item in set_fwsoftpara_list -%}
    SET FWSOFTPARA:
    {#- --- 必选参数 --- -#}
    PARAMETERSTYPE={{item.PARAMETERSTYPE}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：PARAMETERSTYPE=DWORD 时必选 --- -#}
    {%- if item.PARAMETERSTYPE == 'DWORD' -%}
        DWORDINDEX={{item.DWORDINDEX}},
    {%- endif -%}
    {#- --- 条件必选：PARAMETERSTYPE=DWORD 时必选 --- -#}
    {%- if item.PARAMETERSTYPE == 'DWORD' -%}
        DWORDVALUE={{item.DWORDVALUE}},
    {%- endif -%}
    {#- --- 条件必选：PARAMETERSTYPE=DWORD_EX 时必选 --- -#}
    {%- if item.PARAMETERSTYPE == 'DWORD_EX' -%}
        EXTENDDWORDINDEX={{item.EXTENDDWORDINDEX}},
    {%- endif -%}
    {#- --- 条件必选：PARAMETERSTYPE=DWORD_EX 时必选 --- -#}
    {%- if item.PARAMETERSTYPE == 'DWORD_EX' -%}
        EXTENDDWORDVALUE={{item.EXTENDDWORDVALUE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 5 配置IPsec安全提议。

```jinja2
{%- for item in add_ipsecproposalipsec_list -%}
    ADD IPSECPROPOSALIPSEC:
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
    {#- --- 条件可选：IPSECPROTOCOL=Esp/Ah_esp 时可选 --- -#}
    {%- if item.IPSECPROTOCOL in ['Esp', 'Ah_esp'] -%}
        {%- if item.ESPAUTHALGO is not none -%}
            ESPAUTHALGO={{item.ESPAUTHALGO}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：IPSECPROTOCOL=Esp/Ah_esp 时可选 --- -#}
    {%- if item.IPSECPROTOCOL in ['Esp', 'Ah_esp'] -%}
        {%- if item.ESPENCRYPTALGO is not none -%}
            ESPENCRYPTALGO={{item.ESPENCRYPTALGO}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：IPSECPROTOCOL=Ah/Ah_esp 时可选 --- -#}
    {%- if item.IPSECPROTOCOL in ['Ah', 'Ah_esp'] -%}
        {%- if item.AHAUTHALGO is not none -%}
            AHAUTHALGO={{item.AHAUTHALGO}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 6 配置IKE安全提议。

```jinja2
{%- for item in add_ikeproposal_list -%}
    ADD IKEPROPOSAL:
    {#- --- 必选参数 --- -#}
    PROPOSALNUMBER={{item.PROPOSALNUMBER}},
    {#- --- 可选参数 --- -#}
    {%- if item.AUTHMETHOD is not none -%}
        AUTHMETHOD={{item.AUTHMETHOD}},
    {%- endif -%}
    {%- if item.ENCRALGORITHM is not none -%}
        ENCRALGORITHM={{item.ENCRALGORITHM}},
    {%- endif -%}
    {%- if item.INTEGALGORITHM is not none -%}
        INTEGALGORITHM={{item.INTEGALGORITHM}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：AUTHMETHOD=Digital_envelope 时必选 --- -#}
    {%- if item.AUTHMETHOD == 'Digital_envelope' -%}
        ASYMENCRALG={{item.ASYMENCRALG}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：AUTHMETHOD=Cert_signature 时可选 --- -#}
    {%- if item.AUTHMETHOD == 'Cert_signature' -%}
        {%- if item.SIGHASHALGNEGSW is not none -%}
            SIGHASHALGNEGSW={{item.SIGHASHALGNEGSW}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 7 配置IKE对等体。

```jinja2
{%- for item in add_ikepeer6_list -%}
    ADD IKEPEER6:
    {#- --- 必选参数 --- -#}
    PEERNAME="{{item.PEERNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.PROPOSAL is not none -%}
        PROPOSAL={{item.PROPOSAL}},
    {%- endif -%}
    {%- if item.LOWREMOTEADDR is not none -%}
        LOWREMOTEADDR="{{item.LOWREMOTEADDR}}",
    {%- endif -%}
    {%- if item.INVRFNAME is not none -%}
        INVRFNAME="{{item.INVRFNAME}}",
    {%- endif -%}
    {%- if item.OUTVRFNAME is not none -%}
        OUTVRFNAME="{{item.OUTVRFNAME}}",
    {%- endif -%}
    {%- if item.VERSION2 is not none -%}
        VERSION2={{item.VERSION2}},
    {%- endif -%}
    {%- if item.CERTLOCALFILE is not none -%}
        CERTLOCALFILE="{{item.CERTLOCALFILE}}",
    {%- endif -%}
    {%- if item.ENCCERTLOCFILE is not none -%}
        ENCCERTLOCFILE="{{item.ENCCERTLOCFILE}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 8 配置IPsec安全策略。

#### 8.1 增加IPsec安全策略

```jinja2
{%- for item in add_ipsecpolicy6_list -%}
    ADD IPSECPOLICY6:
    {#- --- 必选参数 --- -#}
    POLICYNAME="{{item.POLICYNAME}}",
    SEQUENCENUMBER={{item.SEQUENCENUMBER}},
    POLICYMODE={{item.POLICYMODE}},
    TEMPLATEMODE={{item.TEMPLATEMODE}},
    ACLTYPE={{item.ACLTYPE}},
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：ACLTYPE=AclIPv6 时可选 --- -#}
    {%- if item.ACLTYPE == 'AclIPv6' -%}
        {%- if item.ACL6NUMBER is not none -%}
            ACL6NUMBER={{item.ACL6NUMBER}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：ACLTYPE=AclIPv6 时可选 --- -#}
    {%- if item.ACLTYPE == 'AclIPv6' -%}
        {%- if item.ACL6NAME is not none -%}
            ACL6NAME="{{item.ACL6NAME}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：ACLTYPE=AclIPv4 时可选 --- -#}
    {%- if item.ACLTYPE == 'AclIPv4' -%}
        {%- if item.ACLNAME is not none -%}
            ACLNAME="{{item.ACLNAME}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：ACLTYPE=AclIPv4 时可选 --- -#}
    {%- if item.ACLTYPE == 'AclIPv4' -%}
        {%- if item.ACLNUMBER is not none -%}
            ACLNUMBER={{item.ACLNUMBER}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 8.2 在安全策略中引用安全提议

```jinja2
{%- for item in add_propattachipsecproposal_list -%}
    ADD PROPATTACHIPSECPROPOSAL:
    {#- --- 必选参数 --- -#}
    POLICYNAME="{{item.POLICYNAME}}",
    SEQUENCENUMBER={{item.SEQUENCENUMBER}},
    POLICYMODE={{item.POLICYMODE}},
    TEMPLATEMODE={{item.TEMPLATEMODE}},
    IPSECPROPNAME="{{item.IPSECPROPNAME}}",
    ;
{%- endfor -%}
```

#### 8.3 绑定IKE对等体

```jinja2
{%- for item in add_attachikepeer_list -%}
    ADD ATTACHIKEPEER:
    {#- --- 必选参数 --- -#}
    POLICYNAME="{{item.POLICYNAME}}",
    SEQUENCENUMBER={{item.SEQUENCENUMBER}},
    POLICYMODE={{item.POLICYMODE}},
    TEMPLATEMODE={{item.TEMPLATEMODE}},
    IKEPEERNAME="{{item.IKEPEERNAME}}",
    PEERPRIORITY={{item.PEERPRIORITY}},
    ;
{%- endfor -%}
```

### 9 应用IPsec安全策略。

```jinja2
{%- for item in add_ipsecintfcfgipsec_list -%}
    ADD IPSECINTFCFGIPSEC:
    {#- --- 必选参数 --- -#}
    INTERFACENAME="{{item.INTERFACENAME}}",
    TNLTYPE={{item.TNLTYPE}},
    {#- --- 可选参数 --- -#}
    {%- if item.POLICYNAME is not none -%}
        POLICYNAME="{{item.POLICYNAME}}",
    {%- endif -%}
    ;
{%- endfor -%}
```


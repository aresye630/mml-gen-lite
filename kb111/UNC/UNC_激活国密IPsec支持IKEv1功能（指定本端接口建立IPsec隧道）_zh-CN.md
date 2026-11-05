---
id: ''
name: 激活国密IPsec支持IKEv1功能（指定本端接口建立IPsec隧道）
ne_type: UNC
type: feature
description: 指定本端Loopback口建立IPsec隧道作为本端IKE的协商地址，支持多个IPsec隧道指定同一个Loopback口，作为本端IKE的协商地址。  被指定的接口需要被IPsec隧道单独使用，如果被其他协议使用，则该协议不生效。  如图1所示，网络A和网络B之间采用网关对网关组网模式进行资源传输。网络A和网络B分别通过Device A和Device B连接到Internet。要求通过指定本端接口配置IPsec隧道，实现PCA与PCB之间可以安全地互访。  **图1** 指定本端接口建立IPsec隧道组网图  本例中interface1和interface2分别代表Ethernet66/0/3和Ethernet66/0/5。  网络环境描述如下，以IPv4网络为例：  * 网络A属于10.1.1.0/24子网Device A，通过接口interface2与Device A连接。 * 网络B属于10.1.2.0/24子网，通过接口interface2与Device B连接。 * Device A和Device B路由可达。假设Device A往Device B方向下一跳地址为192.168.1.2/24，Device B往Device A方向下一跳地址为192.168.2.2/24。  **表1** 设备接口IP地址（指定本端接口建立IPsec隧道）  | 设备名称 | 接口 | IP地址 | | --- | --- | --- | | Device A VNRS微服务 | Ethernet66/0/3 | 192.168.1.1/24（IPsec报文的本端物理出接口） | | Device A VNRS微服务 | Ethernet66/0/5 | 10.1.1.1/24 | | Device A VNRS微服务 | LoopBack1 | 10.3.3.3/32（需要双配） | | Device A VNRS微服务 | Tunnel2 | 10.2.2.1/32（需要双配） | | Device B VNRS微服务 | Ethernet66/0/3 | 192.168.2.1/24（IPsec报文的本端物理出接口） | | Device B VNRS微服务 | Ethernet66/0/5 | 10.1.2.1/24 | | Device B VNRS微服务 | LoopBack1 | 10.3.4.3/32（需要双配） | | Device B VNRS微服务 | Tunnel2 | 10.2.3.1/32（需要双配） | | Device A IPsec微服务 | LoopBack1 | 10.3.3.3/32（被指定的本端接口地址，同时是本端的协商IP地址） | | Device A IPsec微服务 | Tunnel2 | 10.2.2.1/32 | | Device B IPsec微服务 | LoopBack1 | 10.3.4.3/32（被指定的本端接口地址，同时是本端的协商IP地址） | | Device B IPsec微服务 | Tunnel2 | 10.2.3.1/32 | | PCA | - | 10.1.1.2/24 | | PCB | - | 10.1.2.2/24 | | - | Device A侧网关接口 | 192.168.1.2/24 | | - | Device B侧网关接口 | 192.168.2.2/24 |
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","IP基本功能","IPFD-016000 IPSec功能","特性配置","激活国密IPsec支持IKEv1功能（指定本端接口建立IPsec隧道）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
指定本端Loopback口建立IPsec隧道作为本端IKE的协商地址，支持多个IPsec隧道指定同一个Loopback口，作为本端IKE的协商地址。被指定的接口需要被IPsec隧道单独使用，如果被其他协议使用，则该协议不生效。如图1所示，网络A和网络B之间采用网关对网关组网模式进行资源传输。网络A和网络B分别通过Device A和Device B连接到Internet。要求通过指定本端接口配置IPsec隧道，实现PCA与PCB之间可以安全地互访。**图1** 指定本端接口建立IPsec隧道组网图本例中interface1和interface2分别代表Ethernet66/0/3和Ethernet66/0/5。网络环境描述如下，以IPv4网络为例：* 网络A属于10.1.1.0/24子网Device A，通过接口interface2与Device A连接。* 网络B属于10.1.2.0/24子网，通过接口interface2与Device B连接。* Device A和Device B路由可达。假设Device A往Device B方向下一跳地址为192.168.1.2/24，Device B往Device A方向下一跳地址为192.168.2.2/24。**表1** 设备接口IP地址（指定本端接口建立IPsec隧道）| 设备名称 | 接口 | IP地址 || --- | --- | --- || Device A VNRS微服务 | Ethernet66/0/3 | 192.168.1.1/24（IPsec报文的本端物理出接口） || Device A VNRS微服务 | Ethernet66/0/5 | 10.1.1.1/24 || Device A VNRS微服务 | LoopBack1 | 10.3.3.3/32（需要双配） || Device A VNRS微服务 | Tunnel2 | 10.2.2.1/32（需要双配） || Device B VNRS微服务 | Ethernet66/0/3 | 192.168.2.1/24（IPsec报文的本端物理出接口） || Device B VNRS微服务 | Ethernet66/0/5 | 10.1.2.1/24 || Device B VNRS微服务 | LoopBack1 | 10.3.4.3/32（需要双配） || Device B VNRS微服务 | Tunnel2 | 10.2.3.1/32（需要双配） || Device A IPsec微服务 | LoopBack1 | 10.3.3.3/32（被指定的本端接口地址，同时是本端的协商IP地址） || Device A IPsec微服务 | Tunnel2 | 10.2.2.1/32 || Device B IPsec微服务 | LoopBack1 | 10.3.4.3/32（被指定的本端接口地址，同时是本端的协商IP地址） || Device B IPsec微服务 | Tunnel2 | 10.2.3.1/32 || PCA | - | 10.1.1.2/24 || PCB | - | 10.1.2.2/24 || - | Device A侧网关接口 | 192.168.1.2/24 || - | Device B侧网关接口 | 192.168.2.2/24 |

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
        IFMTU:
          name: '接口最大传输单元（byte）'
          type: integer
          minimum: 46
          maximum: 9600
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IFDF:
          name: '接口不分片标记'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IFSTATIENABLE:
          name: '接口统计使能标记'
          type: string
          enum:
          - FALSE
          - NONE
          - TRUE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IFSTATITVL:
          name: '接口统计时间间隔（s）'
          type: integer
          minimum: 5
          maximum: 600
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
    add_ifipv4address_list:
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
        IFIPADDR:
          name: 'IPv4地址'
          type: string
          maxLength: 15
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SUBNETMASK:
          name: 'IPv4地址掩码'
          type: string
          maxLength: 15
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ADDRTYPE:
          name: 'IPv4地址类型'
          type: string
          enum:
          - main
          - sub
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: main
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
    add_interface_list_2:
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
        IFMTU:
          name: '接口最大传输单元（byte）'
          type: integer
          minimum: 46
          maximum: 9600
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IFDF:
          name: '接口不分片标记'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        IFSTATITVL:
          name: '接口统计时间间隔（s）'
          type: integer
          minimum: 5
          maximum: 600
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_ipbindvpn_list_6:
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
    add_ifipv4address_list_4:
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
        IFIPADDR:
          name: 'IPv4地址'
          type: string
          maxLength: 15
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SUBNETMASK:
          name: 'IPv4地址掩码'
          type: string
          maxLength: 15
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ADDRTYPE:
          name: 'IPv4地址类型'
          type: string
          enum:
          - main
          - sub
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: main
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
    add_srroute_list:
      type: items
      properties:
        AFTYPE:
          name: '地址族'
          type: string
          enum:
          - ipv4unicast
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PREFIX:
          name: '路由前缀'
          type: string
          maxLength: 15
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MASKLENGTH:
          name: '路由掩码长度'
          type: integer
          minimum: 0
          maximum: 32
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: '_public_'
        IFNAME:
          name: '路由出接口名字'
          type: string
          maxLength: 63
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NEXTHOP:
          name: '路由下一跳'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PREFERENCE:
          name: '路由优先级'
          type: integer
          minimum: 1
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 60
        BFDENABLE:
          name: '动态BFD使能标识'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
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
    add_ifipv4addressipsec_list:
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
        IFIPADDR:
          name: 'IPv4地址'
          type: string
          maxLength: 15
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SUBNETMASK:
          name: 'IPv4地址掩码'
          type: string
          maxLength: 15
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ADDRTYPE:
          name: 'IPv4地址类型'
          type: string
          enum:
          - Main
          - Sub
          - Brwd
          - Brw
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: Main
    add_interfaceipsec_list_2:
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
        IFMTU:
          name: '接口最大传输单元 (byte)'
          type: integer
          minimum: 46
          maximum: 9600
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IFDF:
          name: '接口不分片标记'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        IFSTATITVL:
          name: '接口统计时间间隔 (s)'
          type: integer
          minimum: 5
          maximum: 600
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_ipbindvpnipsec_list_2:
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
    add_ifipv4addressipsec_list_2:
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
        IFIPADDR:
          name: 'IPv4地址'
          type: string
          maxLength: 15
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SUBNETMASK:
          name: 'IPv4地址掩码'
          type: string
          maxLength: 15
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ADDRTYPE:
          name: 'IPv4地址类型'
          type: string
          enum:
          - Main
          - Sub
          - Brwd
          - Brw
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: Main
    add_aclgroupipsec_list:
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
        ACLSTEP:
          name: '规则组步长'
          type: integer
          minimum: 1
          maximum: 20
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: 5
        ACLTYPE:
          name: '规则组类型'
          type: string
          enum:
          - Basic
          - Advance
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        ACLMATCHORDER:
          name: '规则的匹配顺序'
          type: string
          enum:
          - Config
          - Auto
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: Config
    add_aclruleadv4ipsec_list:
      type: items
      properties:
        ACLNAME:
          name: 'ACL规则组标识'
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
        ACLRULEID:
          name: '规则ID'
          type: integer
          minimum: 0
          maximum: 4294967294
          required: false
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
          data_source: '全网规划'
          pattern: ''
          default: '255.255.255.255'
        ACLDESTIP:
          name: '目的IP地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: '0.0.0.0'
        ACLDESTWILD:
          name: '目的IP地址反掩码'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: '255.255.255.255'
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
          data_source: '对端协商'
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
        SADURATION:
          name: 'SA持续长度 (s)'
          type: integer
          minimum: 60
          maximum: 604800
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 86400
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
        REAUTHINTERVAL:
          name: '重认证间隔（s）'
          type: integer
          minimum: 60
          maximum: 604800
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
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
    add_ikepeer_list:
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
        EXCHANGEMODE:
          name: '交换模式'
          type: string
          enum:
          - Main
          - Aggressive
          required: false
          description: ''
          data_source: '对端协商'
          pattern: ''
          default: Main
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
        LOCALIDTYPE:
          name: '本地ID类型'
          type: string
          enum:
          - Ip
          - Fqdn
          - User_fqdn
          - Dn
          - Ip_disable
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: Ip
        LOWREMOTEADDR:
          name: '远程地址'
          type: string
          maxLength: 15
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
        VERSION1:
          name: '版本1'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: '对端协商'
          pattern: ''
          default: TRUE
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
    add_ipsecpolicy_list:
      type: items
      properties:
        POLICYNAME:
          name: '策略名称'
          type: string
          minLength: 1
          maxLength: 15
          required: true
          description: '配置IPsec安全策略。  如果**ADD ACLGROUPIPSEC**中的“ACL规则组标识（ACLNAME）”配置为规则组编号，则IPsec策略中使用“ACL编号（ACLNUMBER）”；如果**ADD ACLGROUPIPSEC**中的“ACL规则组标识（ACLNAME）”配置为规则组名称，则IPsec策略中使用“ACL名称（ACLNAME）”。此处以ACL规则组编号为例。'
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
          data_source: '本端规划'
          pattern: ''
          default: ''
        TRAFFSADISFLG:
          name: '去使能SA按流量计长'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: FALSE
        SALIFETIMEKB:
          name: 'SA按流量计长'
          type: integer
          minimum: 8000
          maximum: 200000000
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        SALIFETIMESEC:
          name: 'SA按时计长'
          type: integer
          minimum:
          - 0
          - 480
          maximum:
          - 0
          - 604800
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        PFS:
          name: 'PFS'
          type: string
          enum:
          - None
          - Dh_group1
          - Dh_group2
          - Dh_group5
          - Dh_group14
          - Dh_group19
          - Dh_group20
          - Dh_group31
          required: false
          description: ''
          data_source: '对端协商'
          pattern: ''
          default: ''
        DSCPINSELECT:
          name: '选择DSCP入方向值'
          type: string
          enum:
          - Af11
          - Af12
          - Af13
          - Af21
          - Af22
          - Af23
          - Af31
          - Af32
          - Af33
          - Af41
          - Af42
          - Af43
          - Cs1
          - Cs2
          - Cs3
          - Cs4
          - Cs5
          - Cs6
          - Cs7
          - Default
          - Ef
          - None
          - EnterDSCPCode
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        DSCPOUTSELECT:
          name: '选择DSCP出方向值'
          type: string
          enum:
          - Af11
          - Af12
          - Af13
          - Af21
          - Af22
          - Af23
          - Af31
          - Af32
          - Af33
          - Af41
          - Af42
          - Af43
          - Cs1
          - Cs2
          - Cs3
          - Cs4
          - Cs5
          - Cs6
          - Cs7
          - Default
          - Ef
          - None
          - EnterDSCPCode
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        ANTIREPLAYENUM:
          name: '抗重放'
          type: string
          enum:
          - NotConfigured
          - Enable
          - Disable
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: NotConfigured
        DFBITCLEAR:
          name: '清除分片标记'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: FALSE
        FRAGBEFOREENCR:
          name: '加密前分片报文'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: FALSE
        LOGENABLE:
          name: '日志使能'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: FALSE
        WINDOWSIZE:
          name: '抗重放窗口大小'
          type: string
          enum:
          - None
          - Size_32
          - Size_64
          - Size_128
          - Size_256
          - Size_512
          - Size_1024
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DSCPINBOUNDVAL:
          name: '输入DSCP入方向值'
          type: integer
          minimum: 0
          maximum: 63
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DSCPOUTBOUNDVAL:
          name: '输入DSCP出方向值'
          type: integer
          minimum: 0
          maximum: 63
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
        ACLTYPE:
          name: 'ACL类型'
          type: string
          enum:
          - AclIPv4
          - AclIPv6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: AclIPv4
        ESN:
          name: '扩展序列号'
          type: string
          enum:
          - Disable
          - Enable
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: Disable
        INSPEEDLIMIT:
          name: '入方向限速 (kbyte/s)'
          type: integer
          minimum:
          - 8
          - 0
          maximum:
          - 4194303
          - 0
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        OUTSPEEDLIMIT:
          name: '出方向限速 (kbyte/s)'
          type: integer
          minimum:
          - 8
          - 0
          maximum:
          - 4194303
          - 0
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TEMPLATENAME:
          name: '模板名称'
          type: string
          minLength: 0
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TFCENABLE:
          name: '数据流可信使能'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        WORKMODE:
          name: '工作模式'
          type: string
          enum:
          - Round_robin
          - Master_standby
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: Round_robin
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
        SRCIFNAME:
          name: '源接口名称'
          type: string
          minLength: 1
          maxLength: 63
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
      AFTYPE: ipv4uni
    mod_interface_list:
    - IFNAME: 'Ethernet66/0/3'
      IFADMINSTATUS: up
      IFMTU: 1500
      IFDF: FALSE
      IFSTATIENABLE: TRUE
      IFSTATITVL: 20
    add_ipbindvpn_list:
    - IFNAME: 'Ethernet66/0/3'
      VRFNAME: 'vrf1'
    add_ifipv4address_list:
    - IFNAME: 'Ethernet66/0/3'
      IFIPADDR: '192.168.1.1'
      SUBNETMASK: '255.255.255.0'
      ADDRTYPE: main
    add_interface_list:
    - IFNAME: 'LoopBack1'
    add_ipbindvpn_list_4:
    - IFNAME: 'LoopBack1'
      VRFNAME: 'vrf1'
    add_interface_list_2:
    - IFNAME: 'Tunnel2'
      IFADMINSTATUS: up
      IFMTU: 1500
      IFDF: FALSE
      IFSTATITVL: 20
    add_ipbindvpn_list_6:
    - IFNAME: 'Tunnel2'
      VRFNAME: 'vrf1'
    add_ifipv4address_list_4:
    - IFNAME: 'LoopBack1'
      IFIPADDR: '10.3.3.3'
      SUBNETMASK: '255.255.255.255'
      ADDRTYPE: main
    add_ipsecintfcfg_list:
    - INTERFACENAME: 'Tunnel2'
      TNLTYPE: IPSEC
    add_srroute_list:
    - AFTYPE: ipv4unicast
      PREFIX: '10.1.2.0'
      MASKLENGTH: 24
      VRFNAME: 'vrf1'
      IFNAME: 'Tunnel2'
      NEXTHOP: '10.3.4.3'
      PREFERENCE: 60
      BFDENABLE: FALSE
    add_l3vpninstipsec_list:
    - VRFNAME: 'vrf1'
    add_vpninstafipsec_list:
    - VRFNAME: 'vrf1'
      AFTYPE: Ipv4uni
    add_interfaceipsec_list:
    - IFNAME: 'LoopBack1'
    add_ipbindvpnipsec_list:
    - IFNAME: 'LoopBack1'
      VRFNAME: 'vrf1'
    add_ifipv4addressipsec_list:
    - IFNAME: 'LoopBack1'
      IFIPADDR: '10.3.3.3'
      SUBNETMASK: '255.255.255.255'
      ADDRTYPE: Main
    add_interfaceipsec_list_2:
    - IFNAME: 'Tunnel2'
      IFADMINSTATUS: Up
      IFMTU: 1500
      IFDF: FALSE
      IFSTATITVL: 20
    add_ipbindvpnipsec_list_2:
    - IFNAME: 'Tunnel2'
      VRFNAME: 'vrf1'
    add_ifipv4addressipsec_list_2:
    - IFNAME: 'Tunnel2'
      IFIPADDR: '10.2.2.1'
      SUBNETMASK: '255.255.255.255'
      ADDRTYPE: Main
    add_aclgroupipsec_list:
    - ACLNAME: '3001'
      ACLSTEP: 5
      ACLTYPE: Advance
      ACLMATCHORDER: Config
    add_aclruleadv4ipsec_list:
    - ACLNAME: '3001'
      ACLRULENAME: 'rule_5'
      ACLRULEID: 5
      ACLACTION: Permit
      ACLPROTOCOL: 0
      ACLSOURCEIP: '10.1.1.2'
      ACLSRCWILD: '0.0.0.0'
      ACLDESTIP: '10.1.2.2'
      ACLDESTWILD: '0.0.0.0'
      VRFNAME: 'vrf1'
    set_fwsoftpara_list:
    - PARAMETERSTYPE: DWORD
      DWORDINDEX: 1401
      DWORDVALUE: 1
      EXTENDDWORDINDEX: ''
      EXTENDDWORDVALUE: ''
    add_ipsecproposalipsec_list:
    - PROPOSALNAME: 'Proposal1'
      IPSECPROTOCOL: Esp
      ESPAUTHALGO: Sha2_512
      ESPENCRYPTALGO: Aes_256
      ENCAPMODE: Tunnel
      AHAUTHALGO: Sha2_512
    add_ikeproposal_list:
    - PROPOSALNUMBER: 1
      AUTHMETHOD: Digital_envelope
      ENCRALGORITHM: Sm4
      INTEGALGORITHM: Sm3
      SADURATION: 86400
      ASYMENCRALG: Sm2
      REAUTHINTERVAL: 86400
      SIGHASHALGNEGSW: Enable
    add_ikepeer_list:
    - PEERNAME: '1'
      EXCHANGEMODE: Main
      PROPOSAL: 1
      LOCALIDTYPE: Ip
      LOWREMOTEADDR: '10.3.4.3'
      INVRFNAME: 'vrf1'
      OUTVRFNAME: 'vrf1'
      VERSION1: TRUE
      VERSION2: FALSE
      CERTLOCALFILE: 'sm2_c_sig.cer'
      ENCCERTLOCFILE: 'sm2_c_enc.cer'
    add_ipsecpolicy_list:
    - POLICYNAME: 'policy1'
      SEQUENCENUMBER: 1
      POLICYMODE: Isakmp
      TEMPLATEMODE: None
      ACLNUMBER: 3001
      TRAFFSADISFLG: FALSE
      SALIFETIMEKB: 1843200
      SALIFETIMESEC: 3600
      PFS: None
      DSCPINSELECT: None
      DSCPOUTSELECT: None
      ANTIREPLAYENUM: NotConfigured
      DFBITCLEAR: FALSE
      FRAGBEFOREENCR: FALSE
      LOGENABLE: FALSE
      WINDOWSIZE: ''
      DSCPINBOUNDVAL: ''
      DSCPOUTBOUNDVAL: ''
      ACLNAME: ''
      ACLTYPE: AclIPv4
      ESN: Disable
      INSPEEDLIMIT: ''
      OUTSPEEDLIMIT: ''
      TEMPLATENAME: ''
      TFCENABLE: FALSE
      WORKMODE: Round_robin
    add_propattachipsecproposal_list:
    - POLICYNAME: 'policy1'
      SEQUENCENUMBER: 1
      POLICYMODE: Isakmp
      TEMPLATEMODE: None
      IPSECPROPNAME: 'Proposal1'
    add_attachikepeer_list:
    - POLICYNAME: 'policy1'
      SEQUENCENUMBER: 1
      POLICYMODE: Isakmp
      TEMPLATEMODE: None
      IKEPEERNAME: '1'
      PEERPRIORITY: 1
    add_ipsecintfcfgipsec_list:
    - INTERFACENAME: 'Tunnel2'
      TNLTYPE: IPSEC
      POLICYNAME: 'policy1'
      SRCIFNAME: 'LoopBack1'
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 创建VNRS微服务的VPN和IPsec隧道接口、Loopback接口，并配置静态路由用于IPsec引流。

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
    {%- if item.IFMTU is not none -%}
        IFMTU={{item.IFMTU}},
    {%- endif -%}
    {%- if item.IFDF is not none -%}
        IFDF={{item.IFDF}},
    {%- endif -%}
    {%- if item.IFSTATIENABLE is not none -%}
        IFSTATIENABLE={{item.IFSTATIENABLE}},
    {%- endif -%}
    {%- if item.IFSTATITVL is not none -%}
        IFSTATITVL={{item.IFSTATITVL}},
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
{%- for item in add_ifipv4address_list -%}
    ADD IFIPV4ADDRESS:
    {#- --- 必选参数 --- -#}
    IFNAME="{{item.IFNAME}}",
    IFIPADDR="{{item.IFIPADDR}}",
    SUBNETMASK="{{item.SUBNETMASK}}",
    {#- --- 可选参数 --- -#}
    {%- if item.ADDRTYPE is not none -%}
        ADDRTYPE={{item.ADDRTYPE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 1.3 创建IPsec隧道接口和Loopback接口，并将其与VPN实例绑定。

```jinja2
{%- for item in add_interface_list -%}
    ADD INTERFACE:
    {#- --- 必选参数 --- -#}
    IFNAME="{{item.IFNAME}}",
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
{%- for item in add_interface_list_2 -%}
    ADD INTERFACE:
    {#- --- 必选参数 --- -#}
    IFNAME="{{item.IFNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.IFADMINSTATUS is not none -%}
        IFADMINSTATUS={{item.IFADMINSTATUS}},
    {%- endif -%}
    {%- if item.IFMTU is not none -%}
        IFMTU={{item.IFMTU}},
    {%- endif -%}
    {%- if item.IFDF is not none -%}
        IFDF={{item.IFDF}},
    {%- endif -%}
    {%- if item.IFSTATITVL is not none -%}
        IFSTATITVL={{item.IFSTATITVL}},
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_ipbindvpn_list_6 -%}
    ADD IPBINDVPN:
    {#- --- 必选参数 --- -#}
    IFNAME="{{item.IFNAME}}",
    VRFNAME="{{item.VRFNAME}}",
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_ifipv4address_list_4 -%}
    ADD IFIPV4ADDRESS:
    {#- --- 必选参数 --- -#}
    IFNAME="{{item.IFNAME}}",
    IFIPADDR="{{item.IFIPADDR}}",
    SUBNETMASK="{{item.SUBNETMASK}}",
    {#- --- 可选参数 --- -#}
    {%- if item.ADDRTYPE is not none -%}
        ADDRTYPE={{item.ADDRTYPE}},
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

#### 1.4 配置静态有用于IPsec引流。

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
    {%- if item.NEXTHOP is not none -%}
        NEXTHOP="{{item.NEXTHOP}}",
    {%- endif -%}
    {%- if item.PREFERENCE is not none -%}
        PREFERENCE={{item.PREFERENCE}},
    {%- endif -%}
    {%- if item.BFDENABLE is not none -%}
        BFDENABLE={{item.BFDENABLE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 2 创建IPsec微服务的VPN和IPsec隧道接口、Loopback接口。

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

#### 2.2 创建IPsec隧道接口和Loopback接口，并将其与VPN实例绑定。

```jinja2
{%- for item in add_interfaceipsec_list -%}
    ADD INTERFACEIPSEC:
    {#- --- 必选参数 --- -#}
    IFNAME="{{item.IFNAME}}",
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
{%- for item in add_ifipv4addressipsec_list -%}
    ADD IFIPV4ADDRESSIPSEC:
    {#- --- 必选参数 --- -#}
    IFNAME="{{item.IFNAME}}",
    IFIPADDR="{{item.IFIPADDR}}",
    SUBNETMASK="{{item.SUBNETMASK}}",
    {#- --- 可选参数 --- -#}
    {%- if item.ADDRTYPE is not none -%}
        ADDRTYPE={{item.ADDRTYPE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_interfaceipsec_list_2 -%}
    ADD INTERFACEIPSEC:
    {#- --- 必选参数 --- -#}
    IFNAME="{{item.IFNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.IFADMINSTATUS is not none -%}
        IFADMINSTATUS={{item.IFADMINSTATUS}},
    {%- endif -%}
    {%- if item.IFMTU is not none -%}
        IFMTU={{item.IFMTU}},
    {%- endif -%}
    {%- if item.IFDF is not none -%}
        IFDF={{item.IFDF}},
    {%- endif -%}
    {%- if item.IFSTATITVL is not none -%}
        IFSTATITVL={{item.IFSTATITVL}},
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_ipbindvpnipsec_list_2 -%}
    ADD IPBINDVPNIPSEC:
    {#- --- 必选参数 --- -#}
    IFNAME="{{item.IFNAME}}",
    VRFNAME="{{item.VRFNAME}}",
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_ifipv4addressipsec_list_2 -%}
    ADD IFIPV4ADDRESSIPSEC:
    {#- --- 必选参数 --- -#}
    IFNAME="{{item.IFNAME}}",
    IFIPADDR="{{item.IFIPADDR}}",
    SUBNETMASK="{{item.SUBNETMASK}}",
    {#- --- 可选参数 --- -#}
    {%- if item.ADDRTYPE is not none -%}
        ADDRTYPE={{item.ADDRTYPE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 定义需要保护的数据流。由用户根据ACL规则来定义，根据不同的数据流特征，定义不同的ACL规则。

```jinja2
{%- for item in add_aclgroupipsec_list -%}
    ADD ACLGROUPIPSEC:
    {#- --- 必选参数 --- -#}
    ACLNAME="{{item.ACLNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.ACLSTEP is not none -%}
        ACLSTEP={{item.ACLSTEP}},
    {%- endif -%}
    {%- if item.ACLTYPE is not none -%}
        ACLTYPE={{item.ACLTYPE}},
    {%- endif -%}
    {%- if item.ACLMATCHORDER is not none -%}
        ACLMATCHORDER={{item.ACLMATCHORDER}},
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_aclruleadv4ipsec_list -%}
    ADD ACLRULEADV4IPSEC:
    {#- --- 必选参数 --- -#}
    ACLNAME="{{item.ACLNAME}}",
    ACLRULENAME="{{item.ACLRULENAME}}",
    ACLACTION={{item.ACLACTION}},
    ACLPROTOCOL={{item.ACLPROTOCOL}},
    {#- --- 可选参数 --- -#}
    {%- if item.ACLRULEID is not none -%}
        ACLRULEID={{item.ACLRULEID}},
    {%- endif -%}
    {%- if item.VRFNAME is not none -%}
        VRFNAME="{{item.VRFNAME}}",
    {%- endif -%}
    {%- if item.ACLSOURCEIP is not none -%}
        ACLSOURCEIP="{{item.ACLSOURCEIP}}",
    {%- endif -%}
    {%- if item.ACLSRCWILD is not none -%}
        ACLSRCWILD="{{item.ACLSRCWILD}}",
    {%- endif -%}
    {%- if item.ACLDESTIP is not none -%}
        ACLDESTIP="{{item.ACLDESTIP}}",
    {%- endif -%}
    {%- if item.ACLDESTWILD is not none -%}
        ACLDESTWILD="{{item.ACLDESTWILD}}",
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
    {%- if item.SADURATION is not none -%}
        SADURATION={{item.SADURATION}},
    {%- endif -%}
    {%- if item.REAUTHINTERVAL is not none -%}
        REAUTHINTERVAL={{item.REAUTHINTERVAL}},
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
{%- for item in add_ikepeer_list -%}
    ADD IKEPEER:
    {#- --- 必选参数 --- -#}
    PEERNAME="{{item.PEERNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.EXCHANGEMODE is not none -%}
        EXCHANGEMODE={{item.EXCHANGEMODE}},
    {%- endif -%}
    {%- if item.PROPOSAL is not none -%}
        PROPOSAL={{item.PROPOSAL}},
    {%- endif -%}
    {%- if item.LOCALIDTYPE is not none -%}
        LOCALIDTYPE={{item.LOCALIDTYPE}},
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
    {%- if item.VERSION1 is not none -%}
        VERSION1={{item.VERSION1}},
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
{%- for item in add_ipsecpolicy_list -%}
    ADD IPSECPOLICY:
    {#- --- 必选参数 --- -#}
    POLICYNAME="{{item.POLICYNAME}}",
    SEQUENCENUMBER={{item.SEQUENCENUMBER}},
    POLICYMODE={{item.POLICYMODE}},
    TEMPLATEMODE={{item.TEMPLATEMODE}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：DSCPINSELECT=EnterDSCPCode 时必选 --- -#}
    {%- if item.DSCPINSELECT == 'EnterDSCPCode' -%}
        DSCPINBOUNDVAL={{item.DSCPINBOUNDVAL}},
    {%- endif -%}
    {#- --- 条件必选：DSCPOUTSELECT=EnterDSCPCode 时必选 --- -#}
    {%- if item.DSCPOUTSELECT == 'EnterDSCPCode' -%}
        DSCPOUTBOUNDVAL={{item.DSCPOUTBOUNDVAL}},
    {%- endif -%}
    {#- --- 条件必选：TEMPLATEMODE=PolicyTemplate 时必选 --- -#}
    {%- if item.TEMPLATEMODE == 'PolicyTemplate' -%}
        TEMPLATENAME="{{item.TEMPLATENAME}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：TEMPLATEMODE=None 时可选 --- -#}
    {%- if item.TEMPLATEMODE == 'None' -%}
        {%- if item.ACLNUMBER is not none -%}
            ACLNUMBER={{item.ACLNUMBER}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：TEMPLATEMODE=None 时可选 --- -#}
    {%- if item.TEMPLATEMODE == 'None' -%}
        {%- if item.TRAFFSADISFLG is not none -%}
            TRAFFSADISFLG={{item.TRAFFSADISFLG}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：TRAFFSADISFLG=FALSE 时可选 --- -#}
    {%- if item.TRAFFSADISFLG == 'FALSE' -%}
        {%- if item.SALIFETIMEKB is not none -%}
            SALIFETIMEKB={{item.SALIFETIMEKB}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：TEMPLATEMODE=None 时可选 --- -#}
    {%- if item.TEMPLATEMODE == 'None' -%}
        {%- if item.SALIFETIMESEC is not none -%}
            SALIFETIMESEC={{item.SALIFETIMESEC}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：TEMPLATEMODE=None 时可选 --- -#}
    {%- if item.TEMPLATEMODE == 'None' -%}
        {%- if item.PFS is not none -%}
            PFS={{item.PFS}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：TEMPLATEMODE=None 时可选 --- -#}
    {%- if item.TEMPLATEMODE == 'None' -%}
        {%- if item.DSCPINSELECT is not none -%}
            DSCPINSELECT={{item.DSCPINSELECT}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：TEMPLATEMODE=None 时可选 --- -#}
    {%- if item.TEMPLATEMODE == 'None' -%}
        {%- if item.DSCPOUTSELECT is not none -%}
            DSCPOUTSELECT={{item.DSCPOUTSELECT}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：TEMPLATEMODE=None 时可选 --- -#}
    {%- if item.TEMPLATEMODE == 'None' -%}
        {%- if item.ANTIREPLAYENUM is not none -%}
            ANTIREPLAYENUM={{item.ANTIREPLAYENUM}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：TEMPLATEMODE=None 时可选 --- -#}
    {%- if item.TEMPLATEMODE == 'None' -%}
        {%- if item.DFBITCLEAR is not none -%}
            DFBITCLEAR={{item.DFBITCLEAR}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：TEMPLATEMODE=None 时可选 --- -#}
    {%- if item.TEMPLATEMODE == 'None' -%}
        {%- if item.FRAGBEFOREENCR is not none -%}
            FRAGBEFOREENCR={{item.FRAGBEFOREENCR}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：TEMPLATEMODE=None 时可选 --- -#}
    {%- if item.TEMPLATEMODE == 'None' -%}
        {%- if item.LOGENABLE is not none -%}
            LOGENABLE={{item.LOGENABLE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：TEMPLATEMODE=None 时可选 --- -#}
    {%- if item.TEMPLATEMODE == 'None' -%}
        {%- if item.ACLNAME is not none -%}
            ACLNAME="{{item.ACLNAME}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：TEMPLATEMODE=None 时可选 --- -#}
    {%- if item.TEMPLATEMODE == 'None' -%}
        {%- if item.ACLTYPE is not none -%}
            ACLTYPE={{item.ACLTYPE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：TEMPLATEMODE=None 时可选 --- -#}
    {%- if item.TEMPLATEMODE == 'None' -%}
        {%- if item.ESN is not none -%}
            ESN={{item.ESN}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：TEMPLATEMODE=None 时可选 --- -#}
    {%- if item.TEMPLATEMODE == 'None' -%}
        {%- if item.INSPEEDLIMIT is not none -%}
            INSPEEDLIMIT={{item.INSPEEDLIMIT}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：TEMPLATEMODE=None 时可选 --- -#}
    {%- if item.TEMPLATEMODE == 'None' -%}
        {%- if item.OUTSPEEDLIMIT is not none -%}
            OUTSPEEDLIMIT={{item.OUTSPEEDLIMIT}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：TEMPLATEMODE=None 时可选 --- -#}
    {%- if item.TEMPLATEMODE == 'None' -%}
        {%- if item.TFCENABLE is not none -%}
            TFCENABLE={{item.TFCENABLE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：ANTIREPLAYENUM=Enable 时可选 --- -#}
    {%- if item.ANTIREPLAYENUM == 'Enable' -%}
        {%- if item.WINDOWSIZE is not none -%}
            WINDOWSIZE={{item.WINDOWSIZE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：TEMPLATEMODE=None 时可选 --- -#}
    {%- if item.TEMPLATEMODE == 'None' -%}
        {%- if item.WORKMODE is not none -%}
            WORKMODE={{item.WORKMODE}},
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
    {%- if item.SRCIFNAME is not none -%}
        SRCIFNAME="{{item.SRCIFNAME}}",
    {%- endif -%}
    ;
{%- endfor -%}
```


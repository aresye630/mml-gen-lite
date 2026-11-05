---
id: GWFD-030502
name: 激活IPsec功能（GRE over IPsec）
ne_type: UEG
type: feature
description: IPsec只支持IP报文数据的传输，GRE over IPsec解决了IPsec不支持组播报文和广播报文数据传输的问题。组播报文和广播报文经过GRE封装后变成GRE报文，通过路由，再将GRE报文引入IPsec隧道进行加解密。  如图1所示，该网络需实现以下需求：  * 将IPsec不支持的组播、广播报文数据在PCA和PCB之间传输。 * PCA和PCB之间传输的数据需要加密。  **图1** GRE over IPsec组网图  网络环境描述如下，以IPv4网络为例：  * 网络A属于10.1.1.0/24子网，通过接口interface2与Device A连接。 * 网络B属于10.1.2.0/24子网，通过接口interface2与Device B连接。 * Device A和Device B路由可达。假设Device A往Device B方向下一跳地址为192.168.1.2/24，Device B往Device A方向下一跳地址为192.168.2.2/24。  **表1** 设备接口IP地址（GRE over IPsec）  | 设备名称 | 接口 | IP地址 | | --- | --- | --- | | Device A VNRS微服务 | Ethernet66/0/5 | 192.168.1.1/24（IPsec报文的本端物理出接口） | | Device A VNRS微服务 | Ethernet66/0/6 | 10.1.1.1/24 | | Device A VNRS微服务 | Tunnel1 | 192.168.3.1/24（GRE隧道，该IP地址用于使GRE隧道的IPv4协议UP） | | Device A VNRS微服务 | Tunnel2 | 10.102.101.25/32（需要双配） | | Device A VNRS微服务 | LoopBack1 | 10.102.105.238/32（GRE的本端源接口） | | Device B VNRS微服务 | Ethernet66/0/5 | 192.168.2.1/24（IPsec报文的本端物理出接口） | | Device B VNRS微服务 | Ethernet66/0/6 | 10.1.2.1/24 | | Device B VNRS微服务 | Tunnel1 | 192.168.4.1/24（GRE隧道，该IP地址用于使GRE隧道的IPv4协议UP） | | Device B VNRS微服务 | Tunnel2 | 10.102.101.21/32（需要双配） | | Device B VNRS微服务 | LoopBack1 | 10.102.105.224/32（GRE的本端源接口） | | Device A IPsec微服务 | Tunnel2 | 10.102.101.25/32（IKE协商IP地址，同时是GRE的本端出接口） | | Device B IPsec微服务 | Tunnel2 | 10.102.101.21/32（IKE协商IP地址，同时是GRE的本端出接口） | | PCA | - | 10.1.1.2/24 | | PCB | - | 10.1.2.2/24 | | - | Device A侧网关接口 | 192.168.1.2/24 | | - | Device B侧网关接口 | 192.168.2.2/24 |
tags: []
risk_level: ''
doc_source:
  - ["网络部署","园区入驻式（仅连接）","5GC toB 部署边缘站点（站点为“风筝S”，入驻式）","虚机容器模式","配置安全数据（风筝S）","安全配置建议","可选配置","网络安全配置","配置IPSec功能","激活IPsec功能（GRE over IPsec）"]
  - ["网络部署","地市共享式（仅连接）","5GC toB 部署边缘站点（站点为“风筝S”，共享式）","配置安全数据（风筝S）","安全配置建议","可选配置","网络安全配置","配置IPSec功能","激活IPsec功能（GRE over IPsec）"]
  - ["网络部署","园区入驻+地市共享（连接+计算）","5GC toB 部署边缘站点（站点为“风筝S”，带计算）","配置安全数据（风筝S）","配置UEG安全数据","UPF安全数据","安全配置建议","可选配置","网络安全配置","配置IPSec功能","激活IPsec功能（GRE over IPsec）"]
  - ["网络部署","园区入驻+地市共享（连接+计算）","5GC toB 部署边缘站点（站点为“风筝S”，带计算）","配置安全数据（风筝S）","配置UEG安全数据","MPF安全数据","安全配置建议","可选配置","网络安全配置","配置IPSec功能","激活IPsec功能（GRE over IPsec）"]
  - ["业务配置","风筝S","MEC 特性指南（风筝S）","UEG特性指南","安全管理功能","GWFD-030502 IPSec","特性配置","激活IPsec功能（GRE over IPsec）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
IPsec只支持IP报文数据的传输，GRE over IPsec解决了IPsec不支持组播报文和广播报文数据传输的问题。组播报文和广播报文经过GRE封装后变成GRE报文，通过路由，再将GRE报文引入IPsec隧道进行加解密。如图1所示，该网络需实现以下需求：* 将IPsec不支持的组播、广播报文数据在PCA和PCB之间传输。* PCA和PCB之间传输的数据需要加密。**图1** GRE over IPsec组网图网络环境描述如下，以IPv4网络为例：* 网络A属于10.1.1.0/24子网，通过接口interface2与Device A连接。* 网络B属于10.1.2.0/24子网，通过接口interface2与Device B连接。* Device A和Device B路由可达。假设Device A往Device B方向下一跳地址为192.168.1.2/24，Device B往Device A方向下一跳地址为192.168.2.2/24。**表1** 设备接口IP地址（GRE over IPsec）| 设备名称 | 接口 | IP地址 || --- | --- | --- || Device A VNRS微服务 | Ethernet66/0/5 | 192.168.1.1/24（IPsec报文的本端物理出接口） || Device A VNRS微服务 | Ethernet66/0/6 | 10.1.1.1/24 || Device A VNRS微服务 | Tunnel1 | 192.168.3.1/24（GRE隧道，该IP地址用于使GRE隧道的IPv4协议UP） || Device A VNRS微服务 | Tunnel2 | 10.102.101.25/32（需要双配） || Device A VNRS微服务 | LoopBack1 | 10.102.105.238/32（GRE的本端源接口） || Device B VNRS微服务 | Ethernet66/0/5 | 192.168.2.1/24（IPsec报文的本端物理出接口） || Device B VNRS微服务 | Ethernet66/0/6 | 10.1.2.1/24 || Device B VNRS微服务 | Tunnel1 | 192.168.4.1/24（GRE隧道，该IP地址用于使GRE隧道的IPv4协议UP） || Device B VNRS微服务 | Tunnel2 | 10.102.101.21/32（需要双配） || Device B VNRS微服务 | LoopBack1 | 10.102.105.224/32（GRE的本端源接口） || Device A IPsec微服务 | Tunnel2 | 10.102.101.25/32（IKE协商IP地址，同时是GRE的本端出接口） || Device B IPsec微服务 | Tunnel2 | 10.102.101.21/32（IKE协商IP地址，同时是GRE的本端出接口） || PCA | - | 10.1.1.2/24 || PCB | - | 10.1.2.2/24 || - | Device A侧网关接口 | 192.168.1.2/24 || - | Device B侧网关接口 | 192.168.2.2/24 |

## 必备事项
前提条件

* 操作人员已经登录网管。
* 配置接口的IP地址。
* 配置路由，使隧道两端路由可达。
* IPSec功能由IPSec服务承载，请完成IPSec安装，参见**软件安装**章节中的“安装可选服务 > 安装IPSec服务”。
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
    mod_interface_list_4:
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
    add_interface_list_2:
      type: items
      properties:
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
        IFNAME:
          name: '接口名'
          type: string
          maxLength: 63
          required: true
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
    add_ifipv4address_list_6:
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
    add_interface_list_4:
      type: items
      properties:
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
        IFNAME:
          name: '接口名'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_ipbindvpn_list_8:
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
    add_gretunnel_list:
      type: items
      properties:
        TNLNAME:
          name: '隧道名称'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: ''
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
          data_source: ''
          pattern: ''
          default: no_type
        DSTIPADDR:
          name: '目的IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        KEEPALVEN:
          name: '使能Keepalive功能'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        TNLTYPE:
          name: '隧道类型'
          type: string
          enum:
          - gre
          - gre6
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SRCIFNAME:
          name: '源接口名称'
          type: string
          maxLength: 63
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GREKEYEN:
          name: '使能识别关键字功能'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        CHECKSUMEN:
          name: '使能端到端校验功能'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        STATENABLE:
          name: '使能报文统计功能'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
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
    add_ifipv4address_list_8:
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
        IFSTATIENABLE:
          name: '接口统计使能标记'
          type: string
          enum:
          - FALSE
          - TRUE
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
    add_aclgroupipsec_list:
      type: items
      properties:
        ACLNAME:
          name: 'ACL规则组标识'
          type: string
          minLength: 1
          maxLength: 32
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_aclruleadv4ipsec_list:
      type: items
      properties:
        ACLNAME:
          name: 'ACL规则组标识'
          type: string
          minLength: 1
          maxLength: 32
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        ACLRULENAME:
          name: '规则名称'
          type: string
          minLength: 1
          maxLength: 32
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        ACLRULEID:
          name: '规则ID'
          type: integer
          minimum: 0
          maximum: 4294967294
          required: false
          description: '-'
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
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        ACLPROTOCOL:
          name: '协议类型值'
          type: integer
          minimum: 0
          maximum: 255
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        ACLSOURCEIP:
          name: '源IP地址'
          type: string
          maxLength: 15
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: '0.0.0.0'
        ACLSRCWILD:
          name: '源IP地址反掩码'
          type: string
          maxLength: 15
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: '255.255.255.255'
        ACLDESTIP:
          name: '目的IP地址'
          type: string
          maxLength: 15
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: '0.0.0.0'
        ACLDESTWILD:
          name: '目的IP地址反掩码'
          type: string
          maxLength: 15
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: '255.255.255.255'
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          minLength: 1
          maxLength: 31
          required: false
          description: '-'
          data_source: '本端规划'
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
          description: '-'
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
          description: '-'
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
          description: '-'
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
          description: '-'
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
          description: '-'
          data_source: '对端协商'
          pattern: ''
          default: Tunnel
    add_ikeproposal_list:
      type: items
      properties:
        PROPOSALNUMBER:
          name: '安全提议号'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: true
          description: '-'
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
          description: '-'
          data_source: '对端协商'
          pattern: ''
          default: Pre_share
        AUTHALGORITHM:
          name: '认证算法'
          type: string
          enum:
          - Md5
          - Sha1
          - Sha2_256
          - Sha2_384
          - Sha2_512
          required: false
          description: '-'
          data_source: '对端协商'
          pattern: ''
          default: Sha2_256
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
          description: '-'
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
          description: '-'
          data_source: '对端协商'
          pattern: ''
          default: Hmac_sha2_256
        DHGROUP:
          name: 'DH组'
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
          description: '-'
          data_source: '对端协商'
          pattern: ''
          default: Dh_group19
        SADURATION:
          name: 'SA持续长度（s）'
          type: integer
          minimum: 60
          maximum: 604800
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: 86400
    add_ikepeer_list:
      type: items
      properties:
        PEERNAME:
          name: '对等体名称'
          type: string
          minLength: 1
          maxLength: 15
          required: true
          description: '-'
          data_source: '对端规划'
          pattern: ''
          default: ''
        PRESHAREDKEY:
          name: '预共享密钥'
          type: string
          minLength: 1
          maxLength: 127
          required: false
          description: '-'
          data_source: '对端协商'
          pattern: ''
          default: ''
        EXCHANGEMODE:
          name: '交换模式'
          type: string
          enum:
          - Main
          - Aggressive
          required: false
          description: '-'
          data_source: '对端协商'
          pattern: ''
          default: Main
        PROPOSAL:
          name: '安全提议'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: false
          description: '-'
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
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: Ip
        LOWREMOTEADDR:
          name: '远程地址'
          type: string
          maxLength: 15
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        INVRFNAME:
          name: 'SA绑定VPN名称'
          type: string
          minLength: 1
          maxLength: 47
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        OUTVRFNAME:
          name: '远程地址VPN名称'
          type: string
          minLength: 1
          maxLength: 47
          required: false
          description: '-'
          data_source: '全网规划'
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
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SEQUENCENUMBER:
          name: '序列号'
          type: integer
          minimum: 1
          maximum: 10000
          required: true
          description: '-'
          data_source: '对端协商'
          pattern: ''
          default: ''
        POLICYMODE:
          name: '策略模式'
          type: string
          enum:
          - Isakmp
          required: true
          description: '-'
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
          description: '-'
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
          description: '如果**ADD ACLGROUPIPSEC**中的“ACL规则组标识（ACLNAME）”配置为规则组编号，则IPsec策略中使用“ACL编号（ACLNUMBER）”；如果**ADD ACLGROUPIPSEC**中的“ACL规则组标识（ACLNAME）”配置为规则组名称，则IPsec策略中使用“ACL名称（ACLNAME）”。此处以ACL规则组编号为例。'
          data_source: '本端规划'
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
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SEQUENCENUMBER:
          name: '序列号'
          type: integer
          minimum: 1
          maximum: 10000
          required: true
          description: '-'
          data_source: '对端协商'
          pattern: ''
          default: ''
        POLICYMODE:
          name: '策略模式'
          type: string
          enum:
          - Isakmp
          required: true
          description: '-'
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
          description: '-'
          data_source: '对端协商'
          pattern: ''
          default: ''
        IPSECPROPNAME:
          name: 'IPsec安全提议名称'
          type: string
          minLength: 1
          maxLength: 15
          required: true
          description: '-'
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
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SEQUENCENUMBER:
          name: '序列号'
          type: integer
          minimum: 1
          maximum: 10000
          required: true
          description: '-'
          data_source: '对端协商'
          pattern: ''
          default: ''
        POLICYMODE:
          name: '策略模式'
          type: string
          enum:
          - Isakmp
          required: true
          description: '-'
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
          description: '-'
          data_source: '对端协商'
          pattern: ''
          default: ''
        IKEPEERNAME:
          name: 'IKE对等体名称'
          type: string
          minLength: 1
          maxLength: 15
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PEERPRIORITY:
          name: '优先级'
          type: integer
          minimum: 1
          maximum: 3
          required: true
          description: '-'
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
          description: '-'
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
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        POLICYNAME:
          name: '策略名称'
          type: string
          minLength: 1
          maxLength: 15
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_ikeglobalconfig_list:
      type: items
      properties:
        DPDINTERVAL:
          name: 'DPD检查间隔（s）'
          type: integer
          minimum: 10
          maximum: 3600
          required: false
          description: '如需开启DPD功能，可配置该参数。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        DPDTYPE:
          name: 'DPD类型'
          type: string
          enum:
          - None
          - Periodic
          - Ondemand
          required: false
          description: '如需开启DPD功能，可配置该参数。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        DPDRETRYINTRVL:
          name: 'DPD重试间隔（s）'
          type: integer
          minimum: 2
          maximum: 60
          required: false
          description: '如需开启DPD功能，可配置该参数。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        NATKLI:
          name: 'NAT保活时间间隔 (s)'
          type: integer
          minimum: 5
          maximum: 300
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 20
    add_srroute_list:
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
  examples:
    add_l3vpninst_list:
    - VRFNAME: 'vrf1'
    add_vpninstaf_list:
    - VRFNAME: 'vrf1'
      AFTYPE: ipv4uni
    mod_interface_list:
    - IFNAME: 'Ethernet66/0/5'
      IFADMINSTATUS: up
      IFMTU: 1500
    add_interface_list:
    - IFNAME: 'LoopBack1'
    mod_interface_list_4:
    - IFNAME: 'LoopBack1'
      IFADMINSTATUS: up
      IFMTU: 1500
      IFDF: FALSE
      IFSTATIENABLE: TRUE
    add_ipbindvpn_list:
    - IFNAME: 'Ethernet66/0/5'
      VRFNAME: 'vrf1'
    add_ifipv4address_list:
    - IFNAME: 'Ethernet66/0/5'
      IFIPADDR: '192.168.1.1'
      SUBNETMASK: '255.255.255.0'
      ADDRTYPE: main
    add_interface_list_2:
    - IFADMINSTATUS: up
      IFMTU: 1500
      IFDF: FALSE
      IFSTATIENABLE: TRUE
      IFNAME: 'Tunnel2'
    add_ipbindvpn_list_6:
    - IFNAME: 'Tunnel2'
      VRFNAME: 'vrf1'
    add_ipsecintfcfg_list:
    - INTERFACENAME: 'Tunnel2'
      TNLTYPE: IPSEC
    add_ifipv4address_list_6:
    - IFNAME: 'Tunnel2'
      IFIPADDR: '10.102.101.25'
      SUBNETMASK: '255.255.255.255'
      ADDRTYPE: main
    add_interface_list_4:
    - IFADMINSTATUS: up
      IFMTU: 1500
      IFDF: FALSE
      IFNAME: 'Tunnel1'
    add_ipbindvpn_list_8:
    - IFNAME: 'Tunnel1'
      VRFNAME: 'vrf1'
    add_gretunnel_list:
    - TNLNAME: 'Tunnel1'
      SRCTYPE: if_name
      DSTIPADDR: '10.102.105.224'
      KEEPALVEN: FALSE
      TNLTYPE: gre
      SRCIFNAME: 'LoopBack1'
      GREKEYEN: FALSE
      CHECKSUMEN: FALSE
      STATENABLE: FALSE
      SRCTYPE6: no_type
    add_ifipv4address_list_8:
    - IFNAME: 'Tunnel1'
      IFIPADDR: '192.168.3.1'
      SUBNETMASK: '255.255.255.0'
      ADDRTYPE: main
    add_l3vpninstipsec_list:
    - VRFNAME: 'vrf1'
    add_vpninstafipsec_list:
    - VRFNAME: 'vrf1'
      AFTYPE: Ipv4uni
    add_interfaceipsec_list:
    - IFNAME: 'Tunnel2'
      IFADMINSTATUS: Up
      IFMTU: 1500
      IFDF: FALSE
      IFSTATIENABLE: TRUE
    add_ipbindvpnipsec_list:
    - IFNAME: 'Tunnel2'
      VRFNAME: 'vrf1'
    add_ifipv4addressipsec_list:
    - IFNAME: 'Tunnel2'
      IFIPADDR: '10.102.101.25'
      SUBNETMASK: '255.255.255.255'
      ADDRTYPE: Main
    add_aclgroupipsec_list:
    - ACLNAME: '3001'
    add_aclruleadv4ipsec_list:
    - ACLNAME: '3001'
      ACLRULENAME: 'rule_1'
      ACLRULEID: 1
      ACLACTION: Permit
      ACLPROTOCOL: 0
      ACLSOURCEIP: '10.102.105.238'
      ACLSRCWILD: '0.0.0.0'
      ACLDESTIP: '10.102.105.224'
      ACLDESTWILD: '0.0.0.0'
      VRFNAME: 'vrf1'
    add_ipsecproposalipsec_list:
    - PROPOSALNAME: '1'
      IPSECPROTOCOL: Esp
      ESPAUTHALGO: Sha2_256
      ESPENCRYPTALGO: Aes_256
      ENCAPMODE: Tunnel
    add_ikeproposal_list:
    - PROPOSALNUMBER: 1
      AUTHMETHOD: Pre_share
      AUTHALGORITHM: Sha2_256
      ENCRALGORITHM: Aes_cbc_256
      INTEGALGORITHM: Hmac_sha2_256
      DHGROUP: Dh_group19
      SADURATION: 3600
    add_ikepeer_list:
    - PEERNAME: 'b'
      PRESHAREDKEY: 'abcde'
      EXCHANGEMODE: Main
      PROPOSAL: 1
      LOCALIDTYPE: Ip
      LOWREMOTEADDR: '10.102.101.21'
      INVRFNAME: 'vrf1'
      OUTVRFNAME: 'vrf1'
    add_ipsecpolicy_list:
    - POLICYNAME: 'policy1'
      SEQUENCENUMBER: 1
      POLICYMODE: Isakmp
      TEMPLATEMODE: None
      ACLNUMBER: 3001
    add_propattachipsecproposal_list:
    - POLICYNAME: 'policy1'
      SEQUENCENUMBER: 1
      POLICYMODE: Isakmp
      TEMPLATEMODE: None
      IPSECPROPNAME: '1'
    add_attachikepeer_list:
    - POLICYNAME: 'policy1'
      SEQUENCENUMBER: 1
      POLICYMODE: Isakmp
      TEMPLATEMODE: None
      IKEPEERNAME: 'b'
      PEERPRIORITY: 1
    add_ipsecintfcfgipsec_list:
    - INTERFACENAME: 'Tunnel2'
      TNLTYPE: IPSEC
      POLICYNAME: 'policy1'
    set_ikeglobalconfig_list:
    - DPDINTERVAL: 10
      DPDTYPE: Periodic
      DPDRETRYINTRVL: 3
      NATKLI: 30
    add_srroute_list:
    - VRFNAME: 'vrf1'
      AFTYPE: ipv4unicast
      PREFIX: '10.102.101.21'
      MASKLENGTH: 32
      IFNAME: 'Invalid0'
      NEXTHOP: '192.168.2.2'
      PREFERENCE: 60
      BFDENABLE: FALSE
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 创建VNRS微服务的VPN、IPsec隧道接口和GRE隧道接口。

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

#### 1.2 创建GRE本端源接口。

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
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_interface_list -%}
    ADD INTERFACE:
    {#- --- 必选参数 --- -#}
    IFNAME="{{item.IFNAME}}",
    ;
{%- endfor -%}
```

```jinja2
{%- for item in mod_interface_list_4 -%}
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
    ;
{%- endfor -%}
```

#### 1.3 将与VPN网络连接的接口与VPN实例绑定，并配置接口IP地址。

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

#### 1.4 创建IPsec隧道接口，并将IPsec隧道接口与VPN实例绑定。

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
    {%- if item.IFSTATIENABLE is not none -%}
        IFSTATIENABLE={{item.IFSTATIENABLE}},
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
{%- for item in add_ipsecintfcfg_list -%}
    ADD IPSECINTFCFG:
    {#- --- 必选参数 --- -#}
    INTERFACENAME="{{item.INTERFACENAME}}",
    TNLTYPE={{item.TNLTYPE}},
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_ifipv4address_list_6 -%}
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

#### 1.5 创建GRE隧道接口，并将GRE隧道接口与VPN实例绑定。

```jinja2
{%- for item in add_interface_list_4 -%}
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
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_ipbindvpn_list_8 -%}
    ADD IPBINDVPN:
    {#- --- 必选参数 --- -#}
    IFNAME="{{item.IFNAME}}",
    VRFNAME="{{item.VRFNAME}}",
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_gretunnel_list -%}
    ADD GRETUNNEL:
    {#- --- 必选参数 --- -#}
    TNLNAME="{{item.TNLNAME}}",
    TNLTYPE={{item.TNLTYPE}},
    {#- --- 可选参数 --- -#}
    {%- if item.KEEPALVEN is not none -%}
        KEEPALVEN={{item.KEEPALVEN}},
    {%- endif -%}
    {%- if item.GREKEYEN is not none -%}
        GREKEYEN={{item.GREKEYEN}},
    {%- endif -%}
    {%- if item.CHECKSUMEN is not none -%}
        CHECKSUMEN={{item.CHECKSUMEN}},
    {%- endif -%}
    {%- if item.STATENABLE is not none -%}
        STATENABLE={{item.STATENABLE}},
    {%- endif -%}
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

```jinja2
{%- for item in add_ifipv4address_list_8 -%}
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
    {%- if item.IFMTU is not none -%}
        IFMTU={{item.IFMTU}},
    {%- endif -%}
    {%- if item.IFDF is not none -%}
        IFDF={{item.IFDF}},
    {%- endif -%}
    {%- if item.IFSTATIENABLE is not none -%}
        IFSTATIENABLE={{item.IFSTATIENABLE}},
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

### 3 定义需要保护的数据流。由用户根据ACL规则来定义，根据不同的数据流特征，定义不同的ACL规则。

```jinja2
{%- for item in add_aclgroupipsec_list -%}
    ADD ACLGROUPIPSEC:
    {#- --- 必选参数 --- -#}
    ACLNAME="{{item.ACLNAME}}",
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

### 4 配置IPsec安全提议。

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
    ;
{%- endfor -%}
```

### 5 配置IKE安全提议。

```jinja2
{%- for item in add_ikeproposal_list -%}
    ADD IKEPROPOSAL:
    {#- --- 必选参数 --- -#}
    PROPOSALNUMBER={{item.PROPOSALNUMBER}},
    {#- --- 可选参数 --- -#}
    {%- if item.AUTHMETHOD is not none -%}
        AUTHMETHOD={{item.AUTHMETHOD}},
    {%- endif -%}
    {%- if item.AUTHALGORITHM is not none -%}
        AUTHALGORITHM={{item.AUTHALGORITHM}},
    {%- endif -%}
    {%- if item.ENCRALGORITHM is not none -%}
        ENCRALGORITHM={{item.ENCRALGORITHM}},
    {%- endif -%}
    {%- if item.INTEGALGORITHM is not none -%}
        INTEGALGORITHM={{item.INTEGALGORITHM}},
    {%- endif -%}
    {%- if item.DHGROUP is not none -%}
        DHGROUP={{item.DHGROUP}},
    {%- endif -%}
    {%- if item.SADURATION is not none -%}
        SADURATION={{item.SADURATION}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 缺省情况下的认证方法为预共享密钥认证（PSK），需要通过**ADD IKEPEER**配置“预共享密钥（PRESHAREDKEY）”，否则建立SA不成功。

### DHGROUP参数不能配置为**None**或者不配置，建议配置为**Dh\_group19**。

### 6 配置IKE对等体。

```jinja2
{%- for item in add_ikepeer_list -%}
    ADD IKEPEER:
    {#- --- 必选参数 --- -#}
    PEERNAME="{{item.PEERNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.PRESHAREDKEY is not none -%}
        PRESHAREDKEY="{{item.PRESHAREDKEY}}",
    {%- endif -%}
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
    ;
{%- endfor -%}
```

### 当配置的认证方式为预共享密钥验证时，必须配置预共享密钥，预共享密钥的配置需要与对端设备相同。此处安全提议为IKE安全提议，IKE对等体被IPsec安全策略引用时，必须配置对端地址。对端地址不能配置为地址段。

### 设备同时开启IKEv1和IKEv2，缺省情况下采用IKEv2进行协商。若对端不支持IKEv2，请禁用IKEv2，采用IKEv1进行协商。

### 7 配置IPsec安全策略。

#### 7.1 增加IPsec安全策略

```jinja2
{%- for item in add_ipsecpolicy_list -%}
    ADD IPSECPOLICY:
    {#- --- 必选参数 --- -#}
    POLICYNAME="{{item.POLICYNAME}}",
    SEQUENCENUMBER={{item.SEQUENCENUMBER}},
    POLICYMODE={{item.POLICYMODE}},
    TEMPLATEMODE={{item.TEMPLATEMODE}},
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：TEMPLATEMODE=None 时可选 --- -#}
    {%- if item.TEMPLATEMODE == 'None' -%}
        {%- if item.ACLNUMBER is not none -%}
            ACLNUMBER={{item.ACLNUMBER}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 7.2 在安全策略中引用安全提议

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

#### 7.3 绑定IKE对等体

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

### 8 应用IPsec安全策略。

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

### 9 当需要配置DPD功能。

```jinja2
{%- if is_optional_dpd_function -%}
    {%- for item in set_ikeglobalconfig_list -%}
        SET IKEGLOBALCONFIG:
        {#- --- 可选参数 --- -#}
        {%- if item.DPDTYPE is not none -%}
            DPDTYPE={{item.DPDTYPE}},
        {%- endif -%}
        {%- if item.NATKLI is not none -%}
            NATKLI={{item.NATKLI}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：DPDTYPE=Periodic/Ondemand 时必选 --- -#}
        {%- if item.DPDTYPE in ['Periodic', 'Ondemand'] -%}
            DPDINTERVAL={{item.DPDINTERVAL}},
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：DPDTYPE=Periodic/Ondemand 时可选 --- -#}
        {%- if item.DPDTYPE in ['Periodic', 'Ondemand'] -%}
            {%- if item.DPDRETRYINTRVL is not none -%}
                DPDRETRYINTRVL={{item.DPDRETRYINTRVL}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 10 配置静态路由用于IPsec引流。

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


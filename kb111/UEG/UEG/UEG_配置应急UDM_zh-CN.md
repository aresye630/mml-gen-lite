---
id: ''
name: 配置应急UDM
ne_type: UEG
type: feature
description: 高可用边缘网关部署在企业园区，新开局场景，需要配置应急UDM实体功能，以保证应急场景下新注册用户或发生信令交互的已注册用户能够正常开展业务。
tags: []
risk_level: ''
doc_source: ["网络部署","园区入驻+地市共享（连接+计算）","5GC toB 部署边缘站点（站点为“风筝M”，带计算）","UEG初始配置（风筝M）","配置实例（虚机容器）","配置应急UDM"]
refs: []
metadata:
  DepOnLiveCfg: true
allowed-tools:
- getParameterValue('LST AUTOCONFIG')
---
<!-- @mml:block= annotations -->
```text
## 操作场景
高可用边缘网关部署在企业园区，新开局场景，需要配置应急UDM实体功能，以保证应急场景下新注册用户或发生信令交互的已注册用户能够正常开展业务。

## 必备事项
前提条件

前提条件

* 已完成软件安装。
* 具备管理员权限的操作人员已经登录华为操作维护系统（登录MAE客户端或登录OM Portal）。
* 已加载License文件。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    set_autoconfig_list:
      type: items
      properties:
        SWITCHFLAG:
          name: '自动配置开关'
          type: string
          enum:
          - TRUE
          - FALSE
          required: true
          description: ''
          data_source: ''
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
        VRFRD:
          name: '路由标识'
          type: string
          maxLength: 21
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_autoscalingethtrunk_list:
      type: items
      properties:
        ETHTRUNKTMPID:
          name: '以太Trunk模板ID'
          type: integer
          minimum: 1
          maximum: 99
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VNICLIST:
          name: '虚拟网卡ID列表'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_autoscalingservice_list:
      type: items
      properties:
        SERVICENAME:
          name: '服务名称'
          type: string
          maxLength: 31
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VPNNAME:
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
          - IPv4
          - IPv6
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPALLOCTYPE4:
          name: 'IPv4地址分配方式'
          type: string
          enum:
          - DHCP
          - USER_CONFIG
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: USER_CONFIG
        AUTOCFGIFTYPE:
          name: '自动化配置接口类型'
          type: string
          enum:
          - ETHTRUNK
          - VNIC
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: VNIC
        ETHTRUNKTMPID:
          name: '以太Trunk模板ID'
          type: integer
          minimum: 1
          maximum: 99
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VLANID:
          name: 'VLAN ID'
          type: integer
          minimum: 0
          maximum: 4094
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 0
        BEGINADDR4:
          name: '起始地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ENDADDR4:
          name: '结束地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MASKLEN:
          name: '地址池掩码长度'
          type: integer
          minimum: 1
          maximum: 128
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPALLOCTYPE6:
          name: 'IPv6地址分配方式'
          type: string
          enum:
          - DHCP
          - USER_CONFIG
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: USER_CONFIG
        BEGINADDR6:
          name: '起始地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ENDADDR6:
          name: '结束地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_autoscalingbfd_list:
      type: items
      properties:
        TEMPLATENAME:
          name: '模板名称'
          type: string
          maxLength: 59
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        BFDTYPE:
          name: 'BFD类型'
          type: string
          enum:
          - Dynamic
          - Static
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SERVICENAME:
          name: '服务名称'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPVERSION:
          name: 'IP版本'
          type: string
          enum:
          - IPv4
          - IPv6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DESTADDR4:
          name: '目的地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MINECHORXINT:
          name: '单臂Echo会话的收包间隔（ms）'
          type: integer
          minimum: 30
          maximum: 1000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 200
        DETECTMULTI:
          name: '检测倍数'
          type: integer
          minimum: 3
          maximum: 50
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 3
        ONEARMECHO:
          name: '单臂Echo'
          type: string
          enum:
          - TRUE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: TRUE
        DESTADDR6:
          name: '目的地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_autoscalingsrroute_list:
      type: items
      properties:
        SERVICENAME:
          name: '服务名称'
          type: string
          maxLength: 31
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
        IPVERSION:
          name: '地址族'
          type: string
          enum:
          - IPv4
          - IPv6
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PREFIX4:
          name: '路由前缀IPv4'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MASKLENGTH:
          name: '路由掩码长度'
          type: integer
          minimum: 0
          maximum: 128
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NEXTHOPALLOCTYPE4:
          name: 'IPv4路由下一跳分配方式'
          type: string
          enum:
          - CONFIG
          - DHCP
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: CONFIG
        NEXTHOP4:
          name: '路由下一跳IPv4'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        BFDENABLE:
          name: 'BFD使能标识'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        DESCRIPTION:
          name: '路由描述'
          type: string
          maxLength: 35
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        BFDTEMPLATENAME:
          name: 'BFD模板名称'
          type: string
          maxLength: 59
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_autoscalingsrroute_list_1:
      type: items
      properties:
        SERVICENAME:
          name: '服务名称'
          type: string
          maxLength: 31
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
        IPVERSION:
          name: '地址族'
          type: string
          enum:
          - IPv4
          - IPv6
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PREFIX6:
          name: '路由前缀IPv6'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MASKLENGTH:
          name: '路由掩码长度'
          type: integer
          minimum: 0
          maximum: 128
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NEXTHOPALLOCTYPE6:
          name: 'IPv6路由下一跳分配方式'
          type: string
          enum:
          - CONFIG
          - DHCP
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: CONFIG
        NEXTHOP6:
          name: '路由下一跳IPv6'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        BFDENABLE:
          name: 'BFD使能标识'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        DESCRIPTION:
          name: '路由描述'
          type: string
          maxLength: 35
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        BFDTEMPLATENAME:
          name: 'BFD模板名称'
          type: string
          maxLength: 59
          required: false
          description: ''
          data_source: ''
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
          description: ''
          data_source: ''
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
        VRFRD:
          name: '路由标识'
          type: string
          maxLength: 21
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
    add_bgpvrf_list:
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
        DEFAULTAFTYPE:
          name: '默认地址族'
          type: string
          enum:
          - ipv4uni
          - ipv6uni
          - noaf
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ipv4uni
        ROUTERID:
          name: '路由器ID'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_bgpvrfaf_list:
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
          name: '地址族类型'
          type: string
          enum:
          - ipv4uni
          - ipv4vpn
          - ipv6uni
          - ipv6vpn
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MAXIMUMLOADBALANCE:
          name: '最大等价路由数'
          type: integer
          minimum: 1
          maximum: 128
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 1
    add_bgppeer_list:
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
        ADDRESSTYPE:
          name: '地址类型'
          type: string
          enum:
          - ipv4
          - ipv6
          - noaf
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ipv4
        PEERADDR:
          name: 'IPv4对等体地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        REMOTEAS:
          name: '对等体AS号'
          type: string
          maxLength: 11
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LOCALIFADDR:
          name: '本地接口地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LOCALIFNAME:
          name: '本地接口名称'
          type: string
          maxLength: 63
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        EBGPMAXHOP:
          name: 'EBGP最大跳数'
          type: integer
          minimum: 1
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PEERADDRV6:
          name: 'IPv6对等体地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_importroute_list:
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
        IMPORTPROTOCOL:
          name: '路由协议'
          type: string
          enum:
          - direct
          - ospf
          - ospfv3
          - static
          - wlr
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MEDENABLE:
          name: '使能MED'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
    add_autoscalingethtrunk_list_1:
      type: items
      properties:
        ETHTRUNKTMPID:
          name: '以太Trunk模板ID'
          type: integer
          minimum: 1
          maximum: 99
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VNICLIST:
          name: '虚拟网卡ID列表'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_autoscalingservice_list_2:
      type: items
      properties:
        SERVICENAME:
          name: '服务名称'
          type: string
          maxLength: 31
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VPNNAME:
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
          - IPv4
          - IPv6
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPALLOCTYPE4:
          name: 'IPv4地址分配方式'
          type: string
          enum:
          - DHCP
          - USER_CONFIG
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: USER_CONFIG
        AUTOCFGIFTYPE:
          name: '自动化配置接口类型'
          type: string
          enum:
          - ETHTRUNK
          - VNIC
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: VNIC
        ETHTRUNKTMPID:
          name: '以太Trunk模板ID'
          type: integer
          minimum: 1
          maximum: 99
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VLANID:
          name: 'VLAN ID'
          type: integer
          minimum: 0
          maximum: 4094
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 0
        BEGINADDR4:
          name: '起始地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ENDADDR4:
          name: '结束地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MASKLEN:
          name: '地址池掩码长度'
          type: integer
          minimum: 1
          maximum: 128
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPALLOCTYPE6:
          name: 'IPv6地址分配方式'
          type: string
          enum:
          - DHCP
          - USER_CONFIG
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: USER_CONFIG
        BEGINADDR6:
          name: '起始地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ENDADDR6:
          name: '结束地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_autoscalingbfd_list_2:
      type: items
      properties:
        TEMPLATENAME:
          name: '模板名称'
          type: string
          maxLength: 59
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        BFDTYPE:
          name: 'BFD类型'
          type: string
          enum:
          - Dynamic
          - Static
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SERVICENAME:
          name: '服务名称'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPVERSION:
          name: 'IP版本'
          type: string
          enum:
          - IPv4
          - IPv6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DESTADDR4:
          name: '目的地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MINECHORXINT:
          name: '单臂Echo会话的收包间隔（ms）'
          type: integer
          minimum: 30
          maximum: 1000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 200
        DETECTMULTI:
          name: '检测倍数'
          type: integer
          minimum: 3
          maximum: 50
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 3
        ONEARMECHO:
          name: '单臂Echo'
          type: string
          enum:
          - TRUE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: TRUE
        DESTADDR6:
          name: '目的地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_autoscalingsrroute_list_2:
      type: items
      properties:
        SERVICENAME:
          name: '服务名称'
          type: string
          maxLength: 31
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
        IPVERSION:
          name: '地址族'
          type: string
          enum:
          - IPv4
          - IPv6
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PREFIX4:
          name: '路由前缀IPv4'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MASKLENGTH:
          name: '路由掩码长度'
          type: integer
          minimum: 0
          maximum: 128
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NEXTHOPALLOCTYPE4:
          name: 'IPv4路由下一跳分配方式'
          type: string
          enum:
          - CONFIG
          - DHCP
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: CONFIG
        NEXTHOP4:
          name: '路由下一跳IPv4'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        BFDENABLE:
          name: 'BFD使能标识'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        DESCRIPTION:
          name: '路由描述'
          type: string
          maxLength: 35
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        BFDTEMPLATENAME:
          name: 'BFD模板名称'
          type: string
          maxLength: 59
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_autoscalingsrroute_list_4:
      type: items
      properties:
        SERVICENAME:
          name: '服务名称'
          type: string
          maxLength: 31
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
        IPVERSION:
          name: '地址族'
          type: string
          enum:
          - IPv4
          - IPv6
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PREFIX4:
          name: '路由前缀IPv4'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MASKLENGTH:
          name: '路由掩码长度'
          type: integer
          minimum: 0
          maximum: 128
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NEXTHOPALLOCTYPE4:
          name: 'IPv4路由下一跳分配方式'
          type: string
          enum:
          - CONFIG
          - DHCP
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: CONFIG
        NEXTHOP4:
          name: '路由下一跳IPv4'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        BFDENABLE:
          name: 'BFD使能标识'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        DESCRIPTION:
          name: '路由描述'
          type: string
          maxLength: 35
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        BFDTEMPLATENAME:
          name: 'BFD模板名称'
          type: string
          maxLength: 59
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_autoscalingsrroute_list_5:
      type: items
      properties:
        SERVICENAME:
          name: '服务名称'
          type: string
          maxLength: 31
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
        IPVERSION:
          name: '地址族'
          type: string
          enum:
          - IPv4
          - IPv6
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PREFIX6:
          name: '路由前缀IPv6'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MASKLENGTH:
          name: '路由掩码长度'
          type: integer
          minimum: 0
          maximum: 128
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NEXTHOPALLOCTYPE6:
          name: 'IPv6路由下一跳分配方式'
          type: string
          enum:
          - CONFIG
          - DHCP
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: CONFIG
        NEXTHOP6:
          name: '路由下一跳IPv6'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        BFDENABLE:
          name: 'BFD使能标识'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        DESCRIPTION:
          name: '路由描述'
          type: string
          maxLength: 35
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        BFDTEMPLATENAME:
          name: 'BFD模板名称'
          type: string
          maxLength: 59
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_autoscalingsrroute_list_7:
      type: items
      properties:
        SERVICENAME:
          name: '服务名称'
          type: string
          maxLength: 31
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
        IPVERSION:
          name: '地址族'
          type: string
          enum:
          - IPv4
          - IPv6
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PREFIX6:
          name: '路由前缀IPv6'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MASKLENGTH:
          name: '路由掩码长度'
          type: integer
          minimum: 0
          maximum: 128
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NEXTHOPALLOCTYPE6:
          name: 'IPv6路由下一跳分配方式'
          type: string
          enum:
          - CONFIG
          - DHCP
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: CONFIG
        NEXTHOP6:
          name: '路由下一跳IPv6'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        BFDENABLE:
          name: 'BFD使能标识'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        DESCRIPTION:
          name: '路由描述'
          type: string
          maxLength: 35
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        BFDTEMPLATENAME:
          name: 'BFD模板名称'
          type: string
          maxLength: 59
          required: false
          description: ''
          data_source: ''
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
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_vpninstaf_list_4:
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
        VRFRD:
          name: '路由标识'
          type: string
          maxLength: 21
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_interface_list_1:
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
    add_ipbindvpn_list_1:
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
    add_ifipv4address_list_1:
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
    set_ifipv6enable_list_1:
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
    add_ifipv6address_list_1:
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
    add_bgpvrf_list_1:
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
        DEFAULTAFTYPE:
          name: '默认地址族'
          type: string
          enum:
          - ipv4uni
          - ipv6uni
          - noaf
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ipv4uni
        ROUTERID:
          name: '路由器ID'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_bgpvrfaf_list_2:
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
          name: '地址族类型'
          type: string
          enum:
          - ipv4uni
          - ipv4vpn
          - ipv6uni
          - ipv6vpn
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MAXIMUMLOADBALANCE:
          name: '最大等价路由数'
          type: integer
          minimum: 1
          maximum: 128
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 1
    add_bgppeer_list_4:
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
        ADDRESSTYPE:
          name: '地址类型'
          type: string
          enum:
          - ipv4
          - ipv6
          - noaf
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ipv4
        PEERADDR:
          name: 'IPv4对等体地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        REMOTEAS:
          name: '对等体AS号'
          type: string
          maxLength: 11
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LOCALIFADDR:
          name: '本地接口地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LOCALIFNAME:
          name: '本地接口名称'
          type: string
          maxLength: 63
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        EBGPMAXHOP:
          name: 'EBGP最大跳数'
          type: integer
          minimum: 1
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PEERADDRV6:
          name: 'IPv6对等体地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_importroute_list_2:
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
        IMPORTPROTOCOL:
          name: '路由协议'
          type: string
          enum:
          - direct
          - ospf
          - ospfv3
          - static
          - wlr
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MEDENABLE:
          name: '使能MED'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
    add_autoscalingethtrunk_list_2:
      type: items
      properties:
        ETHTRUNKTMPID:
          name: '以太Trunk模板ID'
          type: integer
          minimum: 1
          maximum: 99
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VNICLIST:
          name: '虚拟网卡ID列表'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_autoscalingservice_list_4:
      type: items
      properties:
        SERVICENAME:
          name: '服务名称'
          type: string
          maxLength: 31
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VPNNAME:
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
          - IPv4
          - IPv6
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPALLOCTYPE4:
          name: 'IPv4地址分配方式'
          type: string
          enum:
          - DHCP
          - USER_CONFIG
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: USER_CONFIG
        AUTOCFGIFTYPE:
          name: '自动化配置接口类型'
          type: string
          enum:
          - ETHTRUNK
          - VNIC
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: VNIC
        ETHTRUNKTMPID:
          name: '以太Trunk模板ID'
          type: integer
          minimum: 1
          maximum: 99
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VLANID:
          name: 'VLAN ID'
          type: integer
          minimum: 0
          maximum: 4094
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 0
        BEGINADDR4:
          name: '起始地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ENDADDR4:
          name: '结束地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MASKLEN:
          name: '地址池掩码长度'
          type: integer
          minimum: 1
          maximum: 128
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPALLOCTYPE6:
          name: 'IPv6地址分配方式'
          type: string
          enum:
          - DHCP
          - USER_CONFIG
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: USER_CONFIG
        BEGINADDR6:
          name: '起始地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ENDADDR6:
          name: '结束地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_autoscalingbfd_list_4:
      type: items
      properties:
        TEMPLATENAME:
          name: '模板名称'
          type: string
          maxLength: 59
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        BFDTYPE:
          name: 'BFD类型'
          type: string
          enum:
          - Dynamic
          - Static
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SERVICENAME:
          name: '服务名称'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPVERSION:
          name: 'IP版本'
          type: string
          enum:
          - IPv4
          - IPv6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DESTADDR4:
          name: '目的地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MINECHORXINT:
          name: '单臂Echo会话的收包间隔（ms）'
          type: integer
          minimum: 30
          maximum: 1000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 200
        DETECTMULTI:
          name: '检测倍数'
          type: integer
          minimum: 3
          maximum: 50
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 3
        ONEARMECHO:
          name: '单臂Echo'
          type: string
          enum:
          - TRUE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: TRUE
        DESTADDR6:
          name: '目的地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_autoscalingsrroute_list_8:
      type: items
      properties:
        SERVICENAME:
          name: '服务名称'
          type: string
          maxLength: 31
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
        IPVERSION:
          name: '地址族'
          type: string
          enum:
          - IPv4
          - IPv6
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PREFIX4:
          name: '路由前缀IPv4'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MASKLENGTH:
          name: '路由掩码长度'
          type: integer
          minimum: 0
          maximum: 128
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NEXTHOPALLOCTYPE4:
          name: 'IPv4路由下一跳分配方式'
          type: string
          enum:
          - CONFIG
          - DHCP
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: CONFIG
        NEXTHOP4:
          name: '路由下一跳IPv4'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        BFDENABLE:
          name: 'BFD使能标识'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        DESCRIPTION:
          name: '路由描述'
          type: string
          maxLength: 35
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        BFDTEMPLATENAME:
          name: 'BFD模板名称'
          type: string
          maxLength: 59
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_autoscalingsrroute_list_10:
      type: items
      properties:
        SERVICENAME:
          name: '服务名称'
          type: string
          maxLength: 31
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
        IPVERSION:
          name: '地址族'
          type: string
          enum:
          - IPv4
          - IPv6
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PREFIX4:
          name: '路由前缀IPv4'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MASKLENGTH:
          name: '路由掩码长度'
          type: integer
          minimum: 0
          maximum: 128
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NEXTHOPALLOCTYPE4:
          name: 'IPv4路由下一跳分配方式'
          type: string
          enum:
          - CONFIG
          - DHCP
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: CONFIG
        NEXTHOP4:
          name: '路由下一跳IPv4'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        BFDENABLE:
          name: 'BFD使能标识'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        DESCRIPTION:
          name: '路由描述'
          type: string
          maxLength: 35
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        BFDTEMPLATENAME:
          name: 'BFD模板名称'
          type: string
          maxLength: 59
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_autoscalingsrroute_list_11:
      type: items
      properties:
        SERVICENAME:
          name: '服务名称'
          type: string
          maxLength: 31
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
        IPVERSION:
          name: '地址族'
          type: string
          enum:
          - IPv4
          - IPv6
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PREFIX6:
          name: '路由前缀IPv6'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MASKLENGTH:
          name: '路由掩码长度'
          type: integer
          minimum: 0
          maximum: 128
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NEXTHOPALLOCTYPE6:
          name: 'IPv6路由下一跳分配方式'
          type: string
          enum:
          - CONFIG
          - DHCP
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: CONFIG
        NEXTHOP6:
          name: '路由下一跳IPv6'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        BFDENABLE:
          name: 'BFD使能标识'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        DESCRIPTION:
          name: '路由描述'
          type: string
          maxLength: 35
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        BFDTEMPLATENAME:
          name: 'BFD模板名称'
          type: string
          maxLength: 59
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_autoscalingsrroute_list_13:
      type: items
      properties:
        SERVICENAME:
          name: '服务名称'
          type: string
          maxLength: 31
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
        IPVERSION:
          name: '地址族'
          type: string
          enum:
          - IPv4
          - IPv6
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PREFIX6:
          name: '路由前缀IPv6'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MASKLENGTH:
          name: '路由掩码长度'
          type: integer
          minimum: 0
          maximum: 128
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NEXTHOPALLOCTYPE6:
          name: 'IPv6路由下一跳分配方式'
          type: string
          enum:
          - CONFIG
          - DHCP
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: CONFIG
        NEXTHOP6:
          name: '路由下一跳IPv6'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        BFDENABLE:
          name: 'BFD使能标识'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        DESCRIPTION:
          name: '路由描述'
          type: string
          maxLength: 35
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        BFDTEMPLATENAME:
          name: 'BFD模板名称'
          type: string
          maxLength: 59
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_autoconfig_list_1:
      type: items
      properties:
        SWITCHFLAG:
          name: '自动配置开关'
          type: string
          enum:
          - TRUE
          - FALSE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    set_autoconfig_list:
    - SWITCHFLAG: FALSE
    add_l3vpninst_list:
    - VRFNAME: 'VRF_DATA'
    add_vpninstaf_list:
    - VRFNAME: 'VRF_DATA'
      AFTYPE: ipv4uni
      VRFRD: '192.168.225.215:100'
    add_autoscalingethtrunk_list:
    - ETHTRUNKTMPID: 6
      VNICLIST: '6 7'
    add_autoscalingservice_list:
    - SERVICENAME: 'ServName_DATA_2215_v4'
      VPNNAME: 'VRF_DATA'
      AFTYPE: IPv4
      IPALLOCTYPE4: USER_CONFIG
      AUTOCFGIFTYPE: ETHTRUNK
      ETHTRUNKTMPID: 6
      VLANID: 2215
      BEGINADDR4: '192.168.215.2'
      ENDADDR4: '192.168.215.30'
      MASKLEN: 27
      IPALLOCTYPE6: USER_CONFIG
      BEGINADDR6: 'FC00::215:2'
      ENDADDR6: 'FC00::215:1E'
    add_autoscalingbfd_list:
    - TEMPLATENAME: 'BFD_2215_v4'
      BFDTYPE: Static
      SERVICENAME: 'ServName_DATA_2215_v4'
      IPVERSION: IPv4
      DESTADDR4: '192.168.215.1'
      MINECHORXINT: 500
      DETECTMULTI: 4
      ONEARMECHO: TRUE
      DESTADDR6: 'FC00::215:1'
    add_autoscalingsrroute_list:
    - SERVICENAME: 'ServName_DATA_2215_v4'
      VRFNAME: 'VRF_DATA'
      IPVERSION: IPv4
      PREFIX4: 'x.x.x.x'
      MASKLENGTH: 32
      NEXTHOPALLOCTYPE4: CONFIG
      NEXTHOP4: '192.168.215.1'
      BFDENABLE: TRUE
      DESCRIPTION: 'VRF_DATA'
      BFDTEMPLATENAME: 'BFD_2215_v4'
    add_autoscalingsrroute_list_1:
    - SERVICENAME: 'ServName_DATA_2215_v6'
      VRFNAME: 'VRF_DATA'
      IPVERSION: IPv6
      PREFIX6: 'FC00::x:x:x:x'
      MASKLENGTH: 128
      NEXTHOPALLOCTYPE6: CONFIG
      NEXTHOP6: 'FC00::215:1'
      BFDENABLE: TRUE
      DESCRIPTION: 'VRF_DATA'
      BFDTEMPLATENAME: 'BFD_2215_v6'
    add_l3vpninst_list_1:
    - VRFNAME: 'VRF_OM'
    add_vpninstaf_list_2:
    - VRFNAME: 'VRF_OM'
      AFTYPE: ipv4uni
      VRFRD: '192.168.225.216:100'
    add_interface_list:
    - IFNAME: 'LoopBack216'
    add_ipbindvpn_list:
    - IFNAME: 'LoopBack216'
      VRFNAME: 'VRF_OM'
    add_ifipv4address_list:
    - IFNAME: 'LoopBack216'
      IFIPADDR: '192.168.225.216'
      SUBNETMASK: '255.255.255.255'
      ADDRTYPE: main
    set_ifipv6enable_list:
    - IFNAME: 'Loopback216'
      ENABLEFLAG: TRUE
    add_ifipv6address_list:
    - IFNAME: 'Loopback216'
      IPV6ADDRESS: 'FC00::225:216'
      PREFIXLEN: 128
    add_bgpvrf_list:
    - VRFNAME: 'VRF_OM'
      DEFAULTAFTYPE: noaf
      ROUTERID: '192.168.225.216'
    add_bgpvrfaf_list:
    - VRFNAME: 'VRF_OM'
      AFTYPE: ipv4uni
      MAXIMUMLOADBALANCE: 2
    add_bgppeer_list:
    - VRFNAME: 'VRF_OM'
      ADDRESSTYPE: ipv4
      PEERADDR: '192.168.79.216'
      REMOTEAS: '60002'
      LOCALIFADDR: '192.168.225.216'
      LOCALIFNAME: 'Loopback216'
      EBGPMAXHOP: 10
      PEERADDRV6: 'FC00::79:216'
    add_importroute_list:
    - VRFNAME: 'VRF_OM'
      AFTYPE: ipv4uni
      IMPORTPROTOCOL: wlr
      MEDENABLE: FALSE
    add_autoscalingethtrunk_list_1:
    - ETHTRUNKTMPID: 4
      VNICLIST: '4 5'
    add_autoscalingservice_list_2:
    - SERVICENAME: 'ServName_OM_2216_v4'
      VPNNAME: 'VRF_OM'
      AFTYPE: IPv4
      IPALLOCTYPE4: USER_CONFIG
      AUTOCFGIFTYPE: ETHTRUNK
      ETHTRUNKTMPID: 4
      VLANID: 2216
      BEGINADDR4: '192.168.216.2'
      ENDADDR4: '192.168.216.30'
      MASKLEN: 27
      IPALLOCTYPE6: USER_CONFIG
      BEGINADDR6: 'FC00::216:2'
      ENDADDR6: 'FC00::216:1E'
    add_autoscalingbfd_list_2:
    - TEMPLATENAME: 'BFD_2216_v4'
      BFDTYPE: Static
      SERVICENAME: 'ServName_OM_2216_v4'
      IPVERSION: IPv4
      DESTADDR4: '192.168.216.1'
      MINECHORXINT: 500
      DETECTMULTI: 4
      ONEARMECHO: TRUE
      DESTADDR6: 'FC00::216:1'
    add_autoscalingsrroute_list_2:
    - SERVICENAME: 'ServName_OM_2216_v4'
      VRFNAME: 'VRF_OM'
      IPVERSION: IPv4
      PREFIX4: '192.168.79.216'
      MASKLENGTH: 32
      NEXTHOPALLOCTYPE4: CONFIG
      NEXTHOP4: '192.168.216.1'
      BFDENABLE: TRUE
      DESCRIPTION: 'VRF_OM'
      BFDTEMPLATENAME: 'BFD_2216_v4'
    add_autoscalingsrroute_list_4:
    - SERVICENAME: 'ServName_OM_2216_v4'
      VRFNAME: 'VRF_OM'
      IPVERSION: IPv4
      PREFIX4: '0.0.0.0'
      MASKLENGTH: 0
      NEXTHOPALLOCTYPE4: CONFIG
      NEXTHOP4: '192.168.216.1'
      BFDENABLE: TRUE
      DESCRIPTION: 'VRF_OM'
      BFDTEMPLATENAME: 'BFD_2216_v4'
    add_autoscalingsrroute_list_5:
    - SERVICENAME: 'ServName_OM_2216_v6'
      VRFNAME: 'VRF_OM'
      IPVERSION: IPv6
      PREFIX6: 'FC00::79:216'
      MASKLENGTH: 128
      NEXTHOPALLOCTYPE6: CONFIG
      NEXTHOP6: 'FC00::216:1'
      BFDENABLE: TRUE
      DESCRIPTION: 'VRF_OM'
      BFDTEMPLATENAME: 'BFD_2216_v6'
    add_autoscalingsrroute_list_7:
    - SERVICENAME: 'ServName_OM_2216_v6'
      VRFNAME: 'VRF_OM'
      IPVERSION: IPv6
      PREFIX6: '0:0:0:0:0:0:0:0'
      MASKLENGTH: 0
      NEXTHOPALLOCTYPE6: CONFIG
      NEXTHOP6: 'FC00::216:1'
      BFDENABLE: TRUE
      DESCRIPTION: 'VRF_OM'
      BFDTEMPLATENAME: 'BFD_2216_v6'
    add_l3vpninst_list_2:
    - VRFNAME: 'VRF_DSM'
    add_vpninstaf_list_4:
    - VRFNAME: 'VRF_DSM'
      AFTYPE: ipv4uni
      VRFRD: '192.168.225.219:100'
    add_interface_list_1:
    - IFNAME: 'LoopBack219'
    add_ipbindvpn_list_1:
    - IFNAME: 'LoopBack219'
      VRFNAME: 'VRF_DSM'
    add_ifipv4address_list_1:
    - IFNAME: 'LoopBack219'
      IFIPADDR: '192.168.225.219'
      SUBNETMASK: '255.255.255.255'
      ADDRTYPE: main
    set_ifipv6enable_list_1:
    - IFNAME: 'Loopback219'
      ENABLEFLAG: TRUE
    add_ifipv6address_list_1:
    - IFNAME: 'Loopback219'
      IPV6ADDRESS: 'FC00::225:219'
      PREFIXLEN: 128
    add_bgpvrf_list_1:
    - VRFNAME: 'VRF_DSM'
      DEFAULTAFTYPE: noaf
      ROUTERID: '192.168.225.219'
    add_bgpvrfaf_list_2:
    - VRFNAME: 'VRF_DSM'
      AFTYPE: ipv4uni
      MAXIMUMLOADBALANCE: 2
    add_bgppeer_list_4:
    - VRFNAME: 'VRF_DSM'
      ADDRESSTYPE: ipv4
      PEERADDR: '192.168.79.219'
      REMOTEAS: '60002'
      LOCALIFADDR: '192.168.225.219'
      LOCALIFNAME: 'Loopback219'
      EBGPMAXHOP: 10
      PEERADDRV6: 'FC00::79:219'
    add_importroute_list_2:
    - VRFNAME: 'VRF_DSM'
      AFTYPE: ipv4uni
      IMPORTPROTOCOL: wlr
      MEDENABLE: FALSE
    add_autoscalingethtrunk_list_2:
    - ETHTRUNKTMPID: 6
      VNICLIST: '6 7'
    add_autoscalingservice_list_4:
    - SERVICENAME: 'ServName_DSM_2219_v4'
      VPNNAME: 'VRF_DSM'
      AFTYPE: IPv4
      IPALLOCTYPE4: USER_CONFIG
      AUTOCFGIFTYPE: ETHTRUNK
      ETHTRUNKTMPID: 6
      VLANID: 2219
      BEGINADDR4: '192.168.219.2'
      ENDADDR4: '192.168.219.30'
      MASKLEN: 27
      IPALLOCTYPE6: USER_CONFIG
      BEGINADDR6: 'FC00::219:2'
      ENDADDR6: 'FC00::219:1E'
    add_autoscalingbfd_list_4:
    - TEMPLATENAME: 'BFD_2219_v4'
      BFDTYPE: Static
      SERVICENAME: 'ServName_DSM_2219_v4'
      IPVERSION: IPv4
      DESTADDR4: '192.168.219.1'
      MINECHORXINT: 500
      DETECTMULTI: 4
      ONEARMECHO: TRUE
      DESTADDR6: 'FC00::219:1'
    add_autoscalingsrroute_list_8:
    - SERVICENAME: 'ServName_DSM_2219_v4'
      VRFNAME: 'VRF_DSM'
      IPVERSION: IPv4
      PREFIX4: '192.168.79.219'
      MASKLENGTH: 32
      NEXTHOPALLOCTYPE4: CONFIG
      NEXTHOP4: '192.168.219.1'
      BFDENABLE: TRUE
      DESCRIPTION: 'VRF_DSM'
      BFDTEMPLATENAME: 'BFD_2219_v4'
    add_autoscalingsrroute_list_10:
    - SERVICENAME: 'ServName_DSM_2219_v4'
      VRFNAME: 'VRF_DSM'
      IPVERSION: IPv4
      PREFIX4: '0.0.0.0'
      MASKLENGTH: 0
      NEXTHOPALLOCTYPE4: CONFIG
      NEXTHOP4: '192.168.219.1'
      BFDENABLE: TRUE
      DESCRIPTION: 'VRF_DSM'
      BFDTEMPLATENAME: 'BFD_2219_v4'
    add_autoscalingsrroute_list_11:
    - SERVICENAME: 'ServName_DSM_2219_v6'
      VRFNAME: 'VRF_DSM'
      IPVERSION: IPv6
      PREFIX6: 'FC00::79:219'
      MASKLENGTH: 128
      NEXTHOPALLOCTYPE6: CONFIG
      NEXTHOP6: 'FC00::219:1'
      BFDENABLE: TRUE
      DESCRIPTION: 'VRF_DSM'
      BFDTEMPLATENAME: 'BFD_2219_v6'
    add_autoscalingsrroute_list_13:
    - SERVICENAME: 'ServName_DSM_2219_v6'
      VRFNAME: 'VRF_DSM'
      IPVERSION: IPv6
      PREFIX6: '0:0:0:0:0:0:0:0'
      MASKLENGTH: 0
      NEXTHOPALLOCTYPE6: CONFIG
      NEXTHOP6: 'FC00::219:1'
      BFDENABLE: TRUE
      DESCRIPTION: 'VRF_DSM'
      BFDTEMPLATENAME: 'BFD_2219_v6'
    set_autoconfig_list_1:
    - SWITCHFLAG: TRUE
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 登录“UEG MML命令”界面。

### 外联口IP和路由数据，均在“UEG MML命令”界面执行。

### 2 关闭自动配置开关。

#### 2.1 查询自动配置开关。

#### 如果“自动配置开关”值为“TRUE”，需要执行2.b和2.c关闭自动配置开关。

#### 如果“自动配置开关”值为“FALSE”，说明已关闭自动配置开关，请跳转到4。

#### 2.2 查询自动部署维护助手“autoscaling\_autoconfig.py”的状态，确保状态为“准备好状态（Ready）”或者查询无该脚本，以保证当前设备不在自动部署过程中。因为若系统当前有正在进行的自动部署，而自动部署生效有时延，此时若关闭自动配置开关，会影响系统配置效果。

#### 2.3 关闭自动配置开关。自动化配置命令只有在自动配置开关为关闭的状态下才可执行，因此需要提前关闭。

```jinja2
{%- set LST_AUTOCONFIG=getParameterValue('LST AUTOCONFIG') -%}
{%- if LST_AUTOCONFIG=='TRUE' -%}
    {%- for item in set_autoconfig_list -%}
        SET AUTOCONFIG:
        {#- --- 必选参数 --- -#}
        SWITCHFLAG={{item.SWITCHFLAG}},
        ;
    {%- endfor -%}
{%- endif -%}
```

### 3 配置外联口IP和路由数据（USCDB与另一UEG内的USCDB互通）。

#### 3.1 配置VPN实例。

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
    {%- if item.VRFRD is not none -%}
        VRFRD="{{item.VRFRD}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 3.2 添加以太网隧道多虚拟网卡自动化配置模板。如已配置，请跳过本步骤。

```jinja2
{%- for item in add_autoscalingethtrunk_list -%}
    ADD AUTOSCALINGETHTRUNK:
    {#- --- 必选参数 --- -#}
    ETHTRUNKTMPID={{item.ETHTRUNKTMPID}},
    VNICLIST="{{item.VNICLIST}}",
    ;
{%- endfor -%}
```

#### 3.3 配置外联口自动部署模板。

```jinja2
{%- for item in add_autoscalingservice_list -%}
    ADD AUTOSCALINGSERVICE:
    {#- --- 必选参数 --- -#}
    SERVICENAME="{{item.SERVICENAME}}",
    AFTYPE={{item.AFTYPE}},
    {#- --- 可选参数 --- -#}
    {%- if item.VPNNAME is not none -%}
        VPNNAME="{{item.VPNNAME}}",
    {%- endif -%}
    {%- if item.AUTOCFGIFTYPE is not none -%}
        AUTOCFGIFTYPE={{item.AUTOCFGIFTYPE}},
    {%- endif -%}
    {%- if item.VLANID is not none -%}
        VLANID={{item.VLANID}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：AUTOCFGIFTYPE=ETHTRUNK 时必选 --- -#}
    {%- if item.AUTOCFGIFTYPE == 'ETHTRUNK' -%}
        ETHTRUNKTMPID={{item.ETHTRUNKTMPID}},
    {%- endif -%}
    {#- --- 条件必选：IPALLOCTYPE4=USER_CONFIG 时必选 --- -#}
    {%- if item.IPALLOCTYPE4 == 'USER_CONFIG' -%}
        BEGINADDR4="{{item.BEGINADDR4}}",
    {%- endif -%}
    {#- --- 条件必选：IPALLOCTYPE4=USER_CONFIG 时必选 --- -#}
    {%- if item.IPALLOCTYPE4 == 'USER_CONFIG' -%}
        ENDADDR4="{{item.ENDADDR4}}",
    {%- endif -%}
    {#- --- 条件必选：IPALLOCTYPE4=USER_CONFIG 时必选 --- -#}
    {%- if item.IPALLOCTYPE4 == 'USER_CONFIG' -%}
        MASKLEN={{item.MASKLEN}},
    {#- --- 条件必选：IPALLOCTYPE6=USER_CONFIG 时必选 --- -#}
    {%- elif item.IPALLOCTYPE6 == 'USER_CONFIG' -%}
        MASKLEN={{item.MASKLEN}},
    {%- endif -%}
    {#- --- 条件必选：IPALLOCTYPE6=USER_CONFIG 时必选 --- -#}
    {%- if item.IPALLOCTYPE6 == 'USER_CONFIG' -%}
        BEGINADDR6="{{item.BEGINADDR6}}",
    {%- endif -%}
    {#- --- 条件必选：IPALLOCTYPE6=USER_CONFIG 时必选 --- -#}
    {%- if item.IPALLOCTYPE6 == 'USER_CONFIG' -%}
        ENDADDR6="{{item.ENDADDR6}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：AFTYPE=IPv4 时可选 --- -#}
    {%- if item.AFTYPE == 'IPv4' -%}
        {%- if item.IPALLOCTYPE4 is not none -%}
            IPALLOCTYPE4={{item.IPALLOCTYPE4}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：AFTYPE=IPv6 时可选 --- -#}
    {%- if item.AFTYPE == 'IPv6' -%}
        {%- if item.IPALLOCTYPE6 is not none -%}
            IPALLOCTYPE6={{item.IPALLOCTYPE6}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 3.4 增加BFD会话自动部署模板。

```jinja2
{%- for item in add_autoscalingbfd_list -%}
    ADD AUTOSCALINGBFD:
    {#- --- 必选参数 --- -#}
    TEMPLATENAME="{{item.TEMPLATENAME}}",
    BFDTYPE={{item.BFDTYPE}},
    {#- --- 可选参数 --- -#}
    {%- if item.DETECTMULTI is not none -%}
        DETECTMULTI={{item.DETECTMULTI}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：BFDTYPE=Static 时必选 --- -#}
    {%- if item.BFDTYPE == 'Static' -%}
        SERVICENAME="{{item.SERVICENAME}}",
    {%- endif -%}
    {#- --- 条件必选：BFDTYPE=Static 时必选 --- -#}
    {%- if item.BFDTYPE == 'Static' -%}
        IPVERSION={{item.IPVERSION}},
    {%- endif -%}
    {#- --- 条件必选：IPVERSION=IPv4 时必选 --- -#}
    {%- if item.IPVERSION == 'IPv4' -%}
        DESTADDR4="{{item.DESTADDR4}}",
    {%- endif -%}
    {#- --- 条件必选：IPVERSION=IPv6 时必选 --- -#}
    {%- if item.IPVERSION == 'IPv6' -%}
        DESTADDR6="{{item.DESTADDR6}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：BFDTYPE=Static 时可选 --- -#}
    {%- if item.BFDTYPE == 'Static' -%}
        {%- if item.MINECHORXINT is not none -%}
            MINECHORXINT={{item.MINECHORXINT}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：BFDTYPE=Static 时可选 --- -#}
    {%- if item.BFDTYPE == 'Static' -%}
        {%- if item.ONEARMECHO is not none -%}
            ONEARMECHO={{item.ONEARMECHO}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 3.5 增加静态路由自动部署模板。

##### 3.5.1 //“PREFIX4”和“MASKLENGTH”是目的IP和掩码（USCDB上和另一USCDB互通的业务IP地址和掩码）。

```jinja2
{%- for item in add_autoscalingsrroute_list -%}
    ADD AUTOSCALINGSRROUTE:
    {#- --- 必选参数 --- -#}
    SERVICENAME="{{item.SERVICENAME}}",
    IPVERSION={{item.IPVERSION}},
    MASKLENGTH={{item.MASKLENGTH}},
    {#- --- 可选参数 --- -#}
    {%- if item.VRFNAME is not none -%}
        VRFNAME="{{item.VRFNAME}}",
    {%- endif -%}
    {%- if item.BFDENABLE is not none -%}
        BFDENABLE={{item.BFDENABLE}},
    {%- endif -%}
    {%- if item.DESCRIPTION is not none -%}
        DESCRIPTION="{{item.DESCRIPTION}}",
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPVERSION=IPv4 时必选 --- -#}
    {%- if item.IPVERSION == 'IPv4' -%}
        PREFIX4="{{item.PREFIX4}}",
    {%- endif -%}
    {#- --- 条件必选：NEXTHOPALLOCTYPE4=CONFIG 时必选 --- -#}
    {%- if item.NEXTHOPALLOCTYPE4 == 'CONFIG' -%}
        NEXTHOP4="{{item.NEXTHOP4}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：IPVERSION=IPv4 时可选 --- -#}
    {%- if item.IPVERSION == 'IPv4' -%}
        {%- if item.NEXTHOPALLOCTYPE4 is not none -%}
            NEXTHOPALLOCTYPE4={{item.NEXTHOPALLOCTYPE4}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：BFDENABLE=TRUE 时可选 --- -#}
    {%- if item.BFDENABLE == 'TRUE' -%}
        {%- if item.BFDTEMPLATENAME is not none -%}
            BFDTEMPLATENAME="{{item.BFDTEMPLATENAME}}",
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

##### 3.5.2 //“PREFIX6”和“MASKLENGTH”是目的IP和掩码（USCDB上和另一USCDB互通的业务IP地址和掩码）。

```jinja2
{%- for item in add_autoscalingsrroute_list_1 -%}
    ADD AUTOSCALINGSRROUTE:
    {#- --- 必选参数 --- -#}
    SERVICENAME="{{item.SERVICENAME}}",
    IPVERSION={{item.IPVERSION}},
    MASKLENGTH={{item.MASKLENGTH}},
    {#- --- 可选参数 --- -#}
    {%- if item.VRFNAME is not none -%}
        VRFNAME="{{item.VRFNAME}}",
    {%- endif -%}
    {%- if item.BFDENABLE is not none -%}
        BFDENABLE={{item.BFDENABLE}},
    {%- endif -%}
    {%- if item.DESCRIPTION is not none -%}
        DESCRIPTION="{{item.DESCRIPTION}}",
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPVERSION=IPv6 时必选 --- -#}
    {%- if item.IPVERSION == 'IPv6' -%}
        PREFIX6="{{item.PREFIX6}}",
    {%- endif -%}
    {#- --- 条件必选：NEXTHOPALLOCTYPE6=CONFIG 时必选 --- -#}
    {%- if item.NEXTHOPALLOCTYPE6 == 'CONFIG' -%}
        NEXTHOP6="{{item.NEXTHOP6}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：IPVERSION=IPv6 时可选 --- -#}
    {%- if item.IPVERSION == 'IPv6' -%}
        {%- if item.NEXTHOPALLOCTYPE6 is not none -%}
            NEXTHOPALLOCTYPE6={{item.NEXTHOPALLOCTYPE6}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：BFDENABLE=TRUE 时可选 --- -#}
    {%- if item.BFDENABLE == 'TRUE' -%}
        {%- if item.BFDTEMPLATENAME is not none -%}
            BFDTEMPLATENAME="{{item.BFDTEMPLATENAME}}",
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 配置外联口IP和路由数据（登录PGW Web LMT使用）。

#### 4.1 配置VPN实例。

```jinja2
{%- for item in add_l3vpninst_list_1 -%}
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

#### 4.2 配置Loopback接口IP。用于建立BGP邻居。

```jinja2
{%- for item in add_interface_list -%}
    ADD INTERFACE:
    {#- --- 必选参数 --- -#}
    IFNAME="{{item.IFNAME}}",
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

```jinja2
{%- for item in set_ifipv6enable_list -%}
    SET IFIPV6ENABLE:
    {#- --- 必选参数 --- -#}
    IFNAME="{{item.IFNAME}}",
    ENABLEFLAG={{item.ENABLEFLAG}},
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

#### 4.3 配置BGP VPN实例。

```jinja2
{%- for item in add_bgpvrf_list -%}
    ADD BGPVRF:
    {#- --- 必选参数 --- -#}
    VRFNAME="{{item.VRFNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.DEFAULTAFTYPE is not none -%}
        DEFAULTAFTYPE={{item.DEFAULTAFTYPE}},
    {%- endif -%}
    {%- if item.ROUTERID is not none -%}
        ROUTERID="{{item.ROUTERID}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 4.4 增加BGP VPN实例地址族。UEG对接2个负荷分担的BGP PEER时，“MAXIMUMLOADBALANCE”设置为“2”。

```jinja2
{%- for item in add_bgpvrfaf_list -%}
    ADD BGPVRFAF:
    {#- --- 必选参数 --- -#}
    AFTYPE={{item.AFTYPE}},
    {#- --- 可选参数 --- -#}
    {%- if item.VRFNAME is not none -%}
        VRFNAME="{{item.VRFNAME}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：AFTYPE=ipv4uni/ipv6uni 时可选 --- -#}
    {%- if item.AFTYPE in ['ipv4uni', 'ipv6uni'] -%}
        {%- if item.MAXIMUMLOADBALANCE is not none -%}
            MAXIMUMLOADBALANCE={{item.MAXIMUMLOADBALANCE}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 4.5 配置BGP对等体。此处以对接2个IPv4v6双栈的BGP对等体为例。

```jinja2
{%- for item in add_bgppeer_list -%}
    ADD BGPPEER:
    {#- --- 可选参数 --- -#}
    {%- if item.VRFNAME is not none -%}
        VRFNAME="{{item.VRFNAME}}",
    {%- endif -%}
    {%- if item.ADDRESSTYPE is not none -%}
        ADDRESSTYPE={{item.ADDRESSTYPE}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：ADDRESSTYPE=noaf/ipv4 时必选 --- -#}
    {%- if item.ADDRESSTYPE in ['noaf', 'ipv4'] -%}
        PEERADDR="{{item.PEERADDR}}",
    {%- endif -%}
    {#- --- 条件必选：ADDRESSTYPE=ipv6 时必选 --- -#}
    {%- if item.ADDRESSTYPE == 'ipv6' -%}
        PEERADDRV6="{{item.PEERADDRV6}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：ADDRESSTYPE=noaf/ipv4/ipv6 时可选 --- -#}
    {%- if item.ADDRESSTYPE in ['noaf', 'ipv4', 'ipv6'] -%}
        {%- if item.REMOTEAS is not none -%}
            REMOTEAS="{{item.REMOTEAS}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：ADDRESSTYPE=noaf/ipv4/ipv6 时可选 --- -#}
    {%- if item.ADDRESSTYPE in ['noaf', 'ipv4', 'ipv6'] -%}
        {%- if item.LOCALIFADDR is not none -%}
            LOCALIFADDR="{{item.LOCALIFADDR}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：ADDRESSTYPE=noaf/ipv4/ipv6 时可选 --- -#}
    {%- if item.ADDRESSTYPE in ['noaf', 'ipv4', 'ipv6'] -%}
        {%- if item.LOCALIFNAME is not none -%}
            LOCALIFNAME="{{item.LOCALIFNAME}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：ADDRESSTYPE=noaf/ipv4/ipv6 时可选 --- -#}
    {%- if item.ADDRESSTYPE in ['noaf', 'ipv4', 'ipv6'] -%}
        {%- if item.EBGPMAXHOP is not none -%}
            EBGPMAXHOP={{item.EBGPMAXHOP}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 4.6 配置BGP引入wlr路由。

```jinja2
{%- for item in add_importroute_list -%}
    ADD IMPORTROUTE:
    {#- --- 必选参数 --- -#}
    AFTYPE={{item.AFTYPE}},
    IMPORTPROTOCOL={{item.IMPORTPROTOCOL}},
    {#- --- 可选参数 --- -#}
    {%- if item.VRFNAME is not none -%}
        VRFNAME="{{item.VRFNAME}}",
    {%- endif -%}
    {%- if item.MEDENABLE is not none -%}
        MEDENABLE={{item.MEDENABLE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 4.7 添加以太网隧道多虚拟网卡自动化配置模板。如已配置，请跳过本步骤。

```jinja2
{%- for item in add_autoscalingethtrunk_list_1 -%}
    ADD AUTOSCALINGETHTRUNK:
    {#- --- 必选参数 --- -#}
    ETHTRUNKTMPID={{item.ETHTRUNKTMPID}},
    VNICLIST="{{item.VNICLIST}}",
    ;
{%- endfor -%}
```

#### 4.8 配置外联口自动部署模板。

```jinja2
{%- for item in add_autoscalingservice_list_2 -%}
    ADD AUTOSCALINGSERVICE:
    {#- --- 必选参数 --- -#}
    SERVICENAME="{{item.SERVICENAME}}",
    AFTYPE={{item.AFTYPE}},
    {#- --- 可选参数 --- -#}
    {%- if item.VPNNAME is not none -%}
        VPNNAME="{{item.VPNNAME}}",
    {%- endif -%}
    {%- if item.AUTOCFGIFTYPE is not none -%}
        AUTOCFGIFTYPE={{item.AUTOCFGIFTYPE}},
    {%- endif -%}
    {%- if item.VLANID is not none -%}
        VLANID={{item.VLANID}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：AUTOCFGIFTYPE=ETHTRUNK 时必选 --- -#}
    {%- if item.AUTOCFGIFTYPE == 'ETHTRUNK' -%}
        ETHTRUNKTMPID={{item.ETHTRUNKTMPID}},
    {%- endif -%}
    {#- --- 条件必选：IPALLOCTYPE4=USER_CONFIG 时必选 --- -#}
    {%- if item.IPALLOCTYPE4 == 'USER_CONFIG' -%}
        BEGINADDR4="{{item.BEGINADDR4}}",
    {%- endif -%}
    {#- --- 条件必选：IPALLOCTYPE4=USER_CONFIG 时必选 --- -#}
    {%- if item.IPALLOCTYPE4 == 'USER_CONFIG' -%}
        ENDADDR4="{{item.ENDADDR4}}",
    {%- endif -%}
    {#- --- 条件必选：IPALLOCTYPE4=USER_CONFIG 时必选 --- -#}
    {%- if item.IPALLOCTYPE4 == 'USER_CONFIG' -%}
        MASKLEN={{item.MASKLEN}},
    {#- --- 条件必选：IPALLOCTYPE6=USER_CONFIG 时必选 --- -#}
    {%- elif item.IPALLOCTYPE6 == 'USER_CONFIG' -%}
        MASKLEN={{item.MASKLEN}},
    {%- endif -%}
    {#- --- 条件必选：IPALLOCTYPE6=USER_CONFIG 时必选 --- -#}
    {%- if item.IPALLOCTYPE6 == 'USER_CONFIG' -%}
        BEGINADDR6="{{item.BEGINADDR6}}",
    {%- endif -%}
    {#- --- 条件必选：IPALLOCTYPE6=USER_CONFIG 时必选 --- -#}
    {%- if item.IPALLOCTYPE6 == 'USER_CONFIG' -%}
        ENDADDR6="{{item.ENDADDR6}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：AFTYPE=IPv4 时可选 --- -#}
    {%- if item.AFTYPE == 'IPv4' -%}
        {%- if item.IPALLOCTYPE4 is not none -%}
            IPALLOCTYPE4={{item.IPALLOCTYPE4}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：AFTYPE=IPv6 时可选 --- -#}
    {%- if item.AFTYPE == 'IPv6' -%}
        {%- if item.IPALLOCTYPE6 is not none -%}
            IPALLOCTYPE6={{item.IPALLOCTYPE6}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 4.9 增加BFD会话自动部署模板。

```jinja2
{%- for item in add_autoscalingbfd_list_2 -%}
    ADD AUTOSCALINGBFD:
    {#- --- 必选参数 --- -#}
    TEMPLATENAME="{{item.TEMPLATENAME}}",
    BFDTYPE={{item.BFDTYPE}},
    {#- --- 可选参数 --- -#}
    {%- if item.DETECTMULTI is not none -%}
        DETECTMULTI={{item.DETECTMULTI}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：BFDTYPE=Static 时必选 --- -#}
    {%- if item.BFDTYPE == 'Static' -%}
        SERVICENAME="{{item.SERVICENAME}}",
    {%- endif -%}
    {#- --- 条件必选：BFDTYPE=Static 时必选 --- -#}
    {%- if item.BFDTYPE == 'Static' -%}
        IPVERSION={{item.IPVERSION}},
    {%- endif -%}
    {#- --- 条件必选：IPVERSION=IPv4 时必选 --- -#}
    {%- if item.IPVERSION == 'IPv4' -%}
        DESTADDR4="{{item.DESTADDR4}}",
    {%- endif -%}
    {#- --- 条件必选：IPVERSION=IPv6 时必选 --- -#}
    {%- if item.IPVERSION == 'IPv6' -%}
        DESTADDR6="{{item.DESTADDR6}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：BFDTYPE=Static 时可选 --- -#}
    {%- if item.BFDTYPE == 'Static' -%}
        {%- if item.MINECHORXINT is not none -%}
            MINECHORXINT={{item.MINECHORXINT}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：BFDTYPE=Static 时可选 --- -#}
    {%- if item.BFDTYPE == 'Static' -%}
        {%- if item.ONEARMECHO is not none -%}
            ONEARMECHO={{item.ONEARMECHO}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 4.10 增加静态路由自动部署模板。

##### 4.10.1 //“PREFIX4”和“MASKLENGTH”是目的IP和掩码（BGP对等体的IP地址和掩码）。

```jinja2
{%- for item in add_autoscalingsrroute_list_2 -%}
    ADD AUTOSCALINGSRROUTE:
    {#- --- 必选参数 --- -#}
    SERVICENAME="{{item.SERVICENAME}}",
    IPVERSION={{item.IPVERSION}},
    MASKLENGTH={{item.MASKLENGTH}},
    {#- --- 可选参数 --- -#}
    {%- if item.VRFNAME is not none -%}
        VRFNAME="{{item.VRFNAME}}",
    {%- endif -%}
    {%- if item.BFDENABLE is not none -%}
        BFDENABLE={{item.BFDENABLE}},
    {%- endif -%}
    {%- if item.DESCRIPTION is not none -%}
        DESCRIPTION="{{item.DESCRIPTION}}",
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPVERSION=IPv4 时必选 --- -#}
    {%- if item.IPVERSION == 'IPv4' -%}
        PREFIX4="{{item.PREFIX4}}",
    {%- endif -%}
    {#- --- 条件必选：NEXTHOPALLOCTYPE4=CONFIG 时必选 --- -#}
    {%- if item.NEXTHOPALLOCTYPE4 == 'CONFIG' -%}
        NEXTHOP4="{{item.NEXTHOP4}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：IPVERSION=IPv4 时可选 --- -#}
    {%- if item.IPVERSION == 'IPv4' -%}
        {%- if item.NEXTHOPALLOCTYPE4 is not none -%}
            NEXTHOPALLOCTYPE4={{item.NEXTHOPALLOCTYPE4}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：BFDENABLE=TRUE 时可选 --- -#}
    {%- if item.BFDENABLE == 'TRUE' -%}
        {%- if item.BFDTEMPLATENAME is not none -%}
            BFDTEMPLATENAME="{{item.BFDTEMPLATENAME}}",
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

##### 4.10.2 //对端网元不发布BGP默认路由时，需要配置该步骤。“PREFIX4”设置为“0.0.0.0”，“MASKLENGTH”设置为“0”。其他参数与到BGP对等体的路由相同。

```jinja2
{%- if is_scenario_peer_no_default_route -%}
    {%- for item in add_autoscalingsrroute_list_4 -%}
        ADD AUTOSCALINGSRROUTE:
        {#- --- 必选参数 --- -#}
        SERVICENAME="{{item.SERVICENAME}}",
        IPVERSION={{item.IPVERSION}},
        MASKLENGTH={{item.MASKLENGTH}},
        {#- --- 可选参数 --- -#}
        {%- if item.VRFNAME is not none -%}
            VRFNAME="{{item.VRFNAME}}",
        {%- endif -%}
        {%- if item.BFDENABLE is not none -%}
            BFDENABLE={{item.BFDENABLE}},
        {%- endif -%}
        {%- if item.DESCRIPTION is not none -%}
            DESCRIPTION="{{item.DESCRIPTION}}",
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：IPVERSION=IPv4 时必选 --- -#}
        {%- if item.IPVERSION == 'IPv4' -%}
            PREFIX4="{{item.PREFIX4}}",
        {%- endif -%}
        {#- --- 条件必选：NEXTHOPALLOCTYPE4=CONFIG 时必选 --- -#}
        {%- if item.NEXTHOPALLOCTYPE4 == 'CONFIG' -%}
            NEXTHOP4="{{item.NEXTHOP4}}",
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：IPVERSION=IPv4 时可选 --- -#}
        {%- if item.IPVERSION == 'IPv4' -%}
            {%- if item.NEXTHOPALLOCTYPE4 is not none -%}
                NEXTHOPALLOCTYPE4={{item.NEXTHOPALLOCTYPE4}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：BFDENABLE=TRUE 时可选 --- -#}
        {%- if item.BFDENABLE == 'TRUE' -%}
            {%- if item.BFDTEMPLATENAME is not none -%}
                BFDTEMPLATENAME="{{item.BFDTEMPLATENAME}}",
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 4.10.3 //“PREFIX6”和“MASKLENGTH”是目的IP和掩码（BGP对等体的IP地址和掩码）。

```jinja2
{%- for item in add_autoscalingsrroute_list_5 -%}
    ADD AUTOSCALINGSRROUTE:
    {#- --- 必选参数 --- -#}
    SERVICENAME="{{item.SERVICENAME}}",
    IPVERSION={{item.IPVERSION}},
    MASKLENGTH={{item.MASKLENGTH}},
    {#- --- 可选参数 --- -#}
    {%- if item.VRFNAME is not none -%}
        VRFNAME="{{item.VRFNAME}}",
    {%- endif -%}
    {%- if item.BFDENABLE is not none -%}
        BFDENABLE={{item.BFDENABLE}},
    {%- endif -%}
    {%- if item.DESCRIPTION is not none -%}
        DESCRIPTION="{{item.DESCRIPTION}}",
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPVERSION=IPv6 时必选 --- -#}
    {%- if item.IPVERSION == 'IPv6' -%}
        PREFIX6="{{item.PREFIX6}}",
    {%- endif -%}
    {#- --- 条件必选：NEXTHOPALLOCTYPE6=CONFIG 时必选 --- -#}
    {%- if item.NEXTHOPALLOCTYPE6 == 'CONFIG' -%}
        NEXTHOP6="{{item.NEXTHOP6}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：IPVERSION=IPv6 时可选 --- -#}
    {%- if item.IPVERSION == 'IPv6' -%}
        {%- if item.NEXTHOPALLOCTYPE6 is not none -%}
            NEXTHOPALLOCTYPE6={{item.NEXTHOPALLOCTYPE6}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：BFDENABLE=TRUE 时可选 --- -#}
    {%- if item.BFDENABLE == 'TRUE' -%}
        {%- if item.BFDTEMPLATENAME is not none -%}
            BFDTEMPLATENAME="{{item.BFDTEMPLATENAME}}",
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

##### 4.10.4 //对端网元不发布BGP默认路由时，需要配置该步骤。“PREFIX6”设置为“0:0:0:0:0:0:0:0”，“MASKLENGTH”设置为“0”。其他参数与到BGP对等体的路由相同。

```jinja2
{%- if is_scenario_peer_no_default_route -%}
    {%- for item in add_autoscalingsrroute_list_7 -%}
        ADD AUTOSCALINGSRROUTE:
        {#- --- 必选参数 --- -#}
        SERVICENAME="{{item.SERVICENAME}}",
        IPVERSION={{item.IPVERSION}},
        MASKLENGTH={{item.MASKLENGTH}},
        {#- --- 可选参数 --- -#}
        {%- if item.VRFNAME is not none -%}
            VRFNAME="{{item.VRFNAME}}",
        {%- endif -%}
        {%- if item.BFDENABLE is not none -%}
            BFDENABLE={{item.BFDENABLE}},
        {%- endif -%}
        {%- if item.DESCRIPTION is not none -%}
            DESCRIPTION="{{item.DESCRIPTION}}",
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：IPVERSION=IPv6 时必选 --- -#}
        {%- if item.IPVERSION == 'IPv6' -%}
            PREFIX6="{{item.PREFIX6}}",
        {%- endif -%}
        {#- --- 条件必选：NEXTHOPALLOCTYPE6=CONFIG 时必选 --- -#}
        {%- if item.NEXTHOPALLOCTYPE6 == 'CONFIG' -%}
            NEXTHOP6="{{item.NEXTHOP6}}",
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：IPVERSION=IPv6 时可选 --- -#}
        {%- if item.IPVERSION == 'IPv6' -%}
            {%- if item.NEXTHOPALLOCTYPE6 is not none -%}
                NEXTHOPALLOCTYPE6={{item.NEXTHOPALLOCTYPE6}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：BFDENABLE=TRUE 时可选 --- -#}
        {%- if item.BFDENABLE == 'TRUE' -%}
            {%- if item.BFDTEMPLATENAME is not none -%}
                BFDTEMPLATENAME="{{item.BFDTEMPLATENAME}}",
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 5 配置外联口IP和路由数据（用于传输用户数据文件）。

#### 5.1 配置VPN实例。

```jinja2
{%- for item in add_l3vpninst_list_2 -%}
    ADD L3VPNINST:
    {#- --- 必选参数 --- -#}
    VRFNAME="{{item.VRFNAME}}",
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_vpninstaf_list_4 -%}
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

#### 5.2 配置Loopback接口IP。用于建立BGP邻居。

```jinja2
{%- for item in add_interface_list_1 -%}
    ADD INTERFACE:
    {#- --- 必选参数 --- -#}
    IFNAME="{{item.IFNAME}}",
    ;
{%- endfor -%}
```

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
    {#- --- 可选参数 --- -#}
    {%- if item.ADDRTYPE is not none -%}
        ADDRTYPE={{item.ADDRTYPE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in set_ifipv6enable_list_1 -%}
    SET IFIPV6ENABLE:
    {#- --- 必选参数 --- -#}
    IFNAME="{{item.IFNAME}}",
    ENABLEFLAG={{item.ENABLEFLAG}},
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_ifipv6address_list_1 -%}
    ADD IFIPV6ADDRESS:
    {#- --- 必选参数 --- -#}
    IFNAME="{{item.IFNAME}}",
    IPV6ADDRESS="{{item.IPV6ADDRESS}}",
    PREFIXLEN={{item.PREFIXLEN}},
    ;
{%- endfor -%}
```

#### 5.3 配置BGP VPN实例。

```jinja2
{%- for item in add_bgpvrf_list_1 -%}
    ADD BGPVRF:
    {#- --- 必选参数 --- -#}
    VRFNAME="{{item.VRFNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.DEFAULTAFTYPE is not none -%}
        DEFAULTAFTYPE={{item.DEFAULTAFTYPE}},
    {%- endif -%}
    {%- if item.ROUTERID is not none -%}
        ROUTERID="{{item.ROUTERID}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 5.4 增加BGP VPN实例地址族。UEG对接2个负荷分担的BGP PEER时，“MAXIMUMLOADBALANCE”设置为“2”。

```jinja2
{%- for item in add_bgpvrfaf_list_2 -%}
    ADD BGPVRFAF:
    {#- --- 必选参数 --- -#}
    AFTYPE={{item.AFTYPE}},
    {#- --- 可选参数 --- -#}
    {%- if item.VRFNAME is not none -%}
        VRFNAME="{{item.VRFNAME}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：AFTYPE=ipv4uni/ipv6uni 时可选 --- -#}
    {%- if item.AFTYPE in ['ipv4uni', 'ipv6uni'] -%}
        {%- if item.MAXIMUMLOADBALANCE is not none -%}
            MAXIMUMLOADBALANCE={{item.MAXIMUMLOADBALANCE}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 5.5 配置BGP对等体。此处以对接2个IPv4v6双栈的BGP对等体为例。

```jinja2
{%- for item in add_bgppeer_list_4 -%}
    ADD BGPPEER:
    {#- --- 可选参数 --- -#}
    {%- if item.VRFNAME is not none -%}
        VRFNAME="{{item.VRFNAME}}",
    {%- endif -%}
    {%- if item.ADDRESSTYPE is not none -%}
        ADDRESSTYPE={{item.ADDRESSTYPE}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：ADDRESSTYPE=noaf/ipv4 时必选 --- -#}
    {%- if item.ADDRESSTYPE in ['noaf', 'ipv4'] -%}
        PEERADDR="{{item.PEERADDR}}",
    {%- endif -%}
    {#- --- 条件必选：ADDRESSTYPE=ipv6 时必选 --- -#}
    {%- if item.ADDRESSTYPE == 'ipv6' -%}
        PEERADDRV6="{{item.PEERADDRV6}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：ADDRESSTYPE=noaf/ipv4/ipv6 时可选 --- -#}
    {%- if item.ADDRESSTYPE in ['noaf', 'ipv4', 'ipv6'] -%}
        {%- if item.REMOTEAS is not none -%}
            REMOTEAS="{{item.REMOTEAS}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：ADDRESSTYPE=noaf/ipv4/ipv6 时可选 --- -#}
    {%- if item.ADDRESSTYPE in ['noaf', 'ipv4', 'ipv6'] -%}
        {%- if item.LOCALIFADDR is not none -%}
            LOCALIFADDR="{{item.LOCALIFADDR}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：ADDRESSTYPE=noaf/ipv4/ipv6 时可选 --- -#}
    {%- if item.ADDRESSTYPE in ['noaf', 'ipv4', 'ipv6'] -%}
        {%- if item.LOCALIFNAME is not none -%}
            LOCALIFNAME="{{item.LOCALIFNAME}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：ADDRESSTYPE=noaf/ipv4/ipv6 时可选 --- -#}
    {%- if item.ADDRESSTYPE in ['noaf', 'ipv4', 'ipv6'] -%}
        {%- if item.EBGPMAXHOP is not none -%}
            EBGPMAXHOP={{item.EBGPMAXHOP}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 5.6 配置BGP引入wlr路由。

```jinja2
{%- for item in add_importroute_list_2 -%}
    ADD IMPORTROUTE:
    {#- --- 必选参数 --- -#}
    AFTYPE={{item.AFTYPE}},
    IMPORTPROTOCOL={{item.IMPORTPROTOCOL}},
    {#- --- 可选参数 --- -#}
    {%- if item.VRFNAME is not none -%}
        VRFNAME="{{item.VRFNAME}}",
    {%- endif -%}
    {%- if item.MEDENABLE is not none -%}
        MEDENABLE={{item.MEDENABLE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 5.7 添加以太网隧道多虚拟网卡自动化配置模板。如已配置，请跳过本步骤。

```jinja2
{%- for item in add_autoscalingethtrunk_list_2 -%}
    ADD AUTOSCALINGETHTRUNK:
    {#- --- 必选参数 --- -#}
    ETHTRUNKTMPID={{item.ETHTRUNKTMPID}},
    VNICLIST="{{item.VNICLIST}}",
    ;
{%- endfor -%}
```

#### 5.8 配置外联口自动部署模板。

```jinja2
{%- for item in add_autoscalingservice_list_4 -%}
    ADD AUTOSCALINGSERVICE:
    {#- --- 必选参数 --- -#}
    SERVICENAME="{{item.SERVICENAME}}",
    AFTYPE={{item.AFTYPE}},
    {#- --- 可选参数 --- -#}
    {%- if item.VPNNAME is not none -%}
        VPNNAME="{{item.VPNNAME}}",
    {%- endif -%}
    {%- if item.AUTOCFGIFTYPE is not none -%}
        AUTOCFGIFTYPE={{item.AUTOCFGIFTYPE}},
    {%- endif -%}
    {%- if item.VLANID is not none -%}
        VLANID={{item.VLANID}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：AUTOCFGIFTYPE=ETHTRUNK 时必选 --- -#}
    {%- if item.AUTOCFGIFTYPE == 'ETHTRUNK' -%}
        ETHTRUNKTMPID={{item.ETHTRUNKTMPID}},
    {%- endif -%}
    {#- --- 条件必选：IPALLOCTYPE4=USER_CONFIG 时必选 --- -#}
    {%- if item.IPALLOCTYPE4 == 'USER_CONFIG' -%}
        BEGINADDR4="{{item.BEGINADDR4}}",
    {%- endif -%}
    {#- --- 条件必选：IPALLOCTYPE4=USER_CONFIG 时必选 --- -#}
    {%- if item.IPALLOCTYPE4 == 'USER_CONFIG' -%}
        ENDADDR4="{{item.ENDADDR4}}",
    {%- endif -%}
    {#- --- 条件必选：IPALLOCTYPE4=USER_CONFIG 时必选 --- -#}
    {%- if item.IPALLOCTYPE4 == 'USER_CONFIG' -%}
        MASKLEN={{item.MASKLEN}},
    {#- --- 条件必选：IPALLOCTYPE6=USER_CONFIG 时必选 --- -#}
    {%- elif item.IPALLOCTYPE6 == 'USER_CONFIG' -%}
        MASKLEN={{item.MASKLEN}},
    {%- endif -%}
    {#- --- 条件必选：IPALLOCTYPE6=USER_CONFIG 时必选 --- -#}
    {%- if item.IPALLOCTYPE6 == 'USER_CONFIG' -%}
        BEGINADDR6="{{item.BEGINADDR6}}",
    {%- endif -%}
    {#- --- 条件必选：IPALLOCTYPE6=USER_CONFIG 时必选 --- -#}
    {%- if item.IPALLOCTYPE6 == 'USER_CONFIG' -%}
        ENDADDR6="{{item.ENDADDR6}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：AFTYPE=IPv4 时可选 --- -#}
    {%- if item.AFTYPE == 'IPv4' -%}
        {%- if item.IPALLOCTYPE4 is not none -%}
            IPALLOCTYPE4={{item.IPALLOCTYPE4}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：AFTYPE=IPv6 时可选 --- -#}
    {%- if item.AFTYPE == 'IPv6' -%}
        {%- if item.IPALLOCTYPE6 is not none -%}
            IPALLOCTYPE6={{item.IPALLOCTYPE6}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 5.9 增加BFD会话自动部署模板。

```jinja2
{%- for item in add_autoscalingbfd_list_4 -%}
    ADD AUTOSCALINGBFD:
    {#- --- 必选参数 --- -#}
    TEMPLATENAME="{{item.TEMPLATENAME}}",
    BFDTYPE={{item.BFDTYPE}},
    {#- --- 可选参数 --- -#}
    {%- if item.DETECTMULTI is not none -%}
        DETECTMULTI={{item.DETECTMULTI}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：BFDTYPE=Static 时必选 --- -#}
    {%- if item.BFDTYPE == 'Static' -%}
        SERVICENAME="{{item.SERVICENAME}}",
    {%- endif -%}
    {#- --- 条件必选：BFDTYPE=Static 时必选 --- -#}
    {%- if item.BFDTYPE == 'Static' -%}
        IPVERSION={{item.IPVERSION}},
    {%- endif -%}
    {#- --- 条件必选：IPVERSION=IPv4 时必选 --- -#}
    {%- if item.IPVERSION == 'IPv4' -%}
        DESTADDR4="{{item.DESTADDR4}}",
    {%- endif -%}
    {#- --- 条件必选：IPVERSION=IPv6 时必选 --- -#}
    {%- if item.IPVERSION == 'IPv6' -%}
        DESTADDR6="{{item.DESTADDR6}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：BFDTYPE=Static 时可选 --- -#}
    {%- if item.BFDTYPE == 'Static' -%}
        {%- if item.MINECHORXINT is not none -%}
            MINECHORXINT={{item.MINECHORXINT}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：BFDTYPE=Static 时可选 --- -#}
    {%- if item.BFDTYPE == 'Static' -%}
        {%- if item.ONEARMECHO is not none -%}
            ONEARMECHO={{item.ONEARMECHO}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 5.10 增加静态路由自动部署模板。

##### 5.10.1 //“PREFIX4”和“MASKLENGTH”是目的IP和掩码（BGP对等体的IP地址和掩码）。

```jinja2
{%- for item in add_autoscalingsrroute_list_8 -%}
    ADD AUTOSCALINGSRROUTE:
    {#- --- 必选参数 --- -#}
    SERVICENAME="{{item.SERVICENAME}}",
    IPVERSION={{item.IPVERSION}},
    MASKLENGTH={{item.MASKLENGTH}},
    {#- --- 可选参数 --- -#}
    {%- if item.VRFNAME is not none -%}
        VRFNAME="{{item.VRFNAME}}",
    {%- endif -%}
    {%- if item.BFDENABLE is not none -%}
        BFDENABLE={{item.BFDENABLE}},
    {%- endif -%}
    {%- if item.DESCRIPTION is not none -%}
        DESCRIPTION="{{item.DESCRIPTION}}",
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPVERSION=IPv4 时必选 --- -#}
    {%- if item.IPVERSION == 'IPv4' -%}
        PREFIX4="{{item.PREFIX4}}",
    {%- endif -%}
    {#- --- 条件必选：NEXTHOPALLOCTYPE4=CONFIG 时必选 --- -#}
    {%- if item.NEXTHOPALLOCTYPE4 == 'CONFIG' -%}
        NEXTHOP4="{{item.NEXTHOP4}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：IPVERSION=IPv4 时可选 --- -#}
    {%- if item.IPVERSION == 'IPv4' -%}
        {%- if item.NEXTHOPALLOCTYPE4 is not none -%}
            NEXTHOPALLOCTYPE4={{item.NEXTHOPALLOCTYPE4}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：BFDENABLE=TRUE 时可选 --- -#}
    {%- if item.BFDENABLE == 'TRUE' -%}
        {%- if item.BFDTEMPLATENAME is not none -%}
            BFDTEMPLATENAME="{{item.BFDTEMPLATENAME}}",
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

##### 5.10.2 //对端网元不发布BGP默认路由时，需要配置该步骤。“PREFIX4”设置为“0.0.0.0”，“MASKLENGTH”设置为“0”。其他参数与到BGP对等体的路由相同。

```jinja2
{%- if is_scenario_peer_no_default_route -%}
    {%- for item in add_autoscalingsrroute_list_10 -%}
        ADD AUTOSCALINGSRROUTE:
        {#- --- 必选参数 --- -#}
        SERVICENAME="{{item.SERVICENAME}}",
        IPVERSION={{item.IPVERSION}},
        MASKLENGTH={{item.MASKLENGTH}},
        {#- --- 可选参数 --- -#}
        {%- if item.VRFNAME is not none -%}
            VRFNAME="{{item.VRFNAME}}",
        {%- endif -%}
        {%- if item.BFDENABLE is not none -%}
            BFDENABLE={{item.BFDENABLE}},
        {%- endif -%}
        {%- if item.DESCRIPTION is not none -%}
            DESCRIPTION="{{item.DESCRIPTION}}",
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：IPVERSION=IPv4 时必选 --- -#}
        {%- if item.IPVERSION == 'IPv4' -%}
            PREFIX4="{{item.PREFIX4}}",
        {%- endif -%}
        {#- --- 条件必选：NEXTHOPALLOCTYPE4=CONFIG 时必选 --- -#}
        {%- if item.NEXTHOPALLOCTYPE4 == 'CONFIG' -%}
            NEXTHOP4="{{item.NEXTHOP4}}",
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：IPVERSION=IPv4 时可选 --- -#}
        {%- if item.IPVERSION == 'IPv4' -%}
            {%- if item.NEXTHOPALLOCTYPE4 is not none -%}
                NEXTHOPALLOCTYPE4={{item.NEXTHOPALLOCTYPE4}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：BFDENABLE=TRUE 时可选 --- -#}
        {%- if item.BFDENABLE == 'TRUE' -%}
            {%- if item.BFDTEMPLATENAME is not none -%}
                BFDTEMPLATENAME="{{item.BFDTEMPLATENAME}}",
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 5.10.3 //“PREFIX6”和“MASKLENGTH”是目的IP和掩码（BGP对等体的IP地址和掩码）。

```jinja2
{%- for item in add_autoscalingsrroute_list_11 -%}
    ADD AUTOSCALINGSRROUTE:
    {#- --- 必选参数 --- -#}
    SERVICENAME="{{item.SERVICENAME}}",
    IPVERSION={{item.IPVERSION}},
    MASKLENGTH={{item.MASKLENGTH}},
    {#- --- 可选参数 --- -#}
    {%- if item.VRFNAME is not none -%}
        VRFNAME="{{item.VRFNAME}}",
    {%- endif -%}
    {%- if item.BFDENABLE is not none -%}
        BFDENABLE={{item.BFDENABLE}},
    {%- endif -%}
    {%- if item.DESCRIPTION is not none -%}
        DESCRIPTION="{{item.DESCRIPTION}}",
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPVERSION=IPv6 时必选 --- -#}
    {%- if item.IPVERSION == 'IPv6' -%}
        PREFIX6="{{item.PREFIX6}}",
    {%- endif -%}
    {#- --- 条件必选：NEXTHOPALLOCTYPE6=CONFIG 时必选 --- -#}
    {%- if item.NEXTHOPALLOCTYPE6 == 'CONFIG' -%}
        NEXTHOP6="{{item.NEXTHOP6}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：IPVERSION=IPv6 时可选 --- -#}
    {%- if item.IPVERSION == 'IPv6' -%}
        {%- if item.NEXTHOPALLOCTYPE6 is not none -%}
            NEXTHOPALLOCTYPE6={{item.NEXTHOPALLOCTYPE6}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：BFDENABLE=TRUE 时可选 --- -#}
    {%- if item.BFDENABLE == 'TRUE' -%}
        {%- if item.BFDTEMPLATENAME is not none -%}
            BFDTEMPLATENAME="{{item.BFDTEMPLATENAME}}",
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

##### 5.10.4 //对端网元不发布BGP默认路由时，需要配置该步骤。“PREFIX6”设置为“0:0:0:0:0:0:0:0”，“MASKLENGTH”设置为“0”。其他参数与到BGP对等体的路由相同。

```jinja2
{%- if is_scenario_peer_no_default_route -%}
    {%- for item in add_autoscalingsrroute_list_13 -%}
        ADD AUTOSCALINGSRROUTE:
        {#- --- 必选参数 --- -#}
        SERVICENAME="{{item.SERVICENAME}}",
        IPVERSION={{item.IPVERSION}},
        MASKLENGTH={{item.MASKLENGTH}},
        {#- --- 可选参数 --- -#}
        {%- if item.VRFNAME is not none -%}
            VRFNAME="{{item.VRFNAME}}",
        {%- endif -%}
        {%- if item.BFDENABLE is not none -%}
            BFDENABLE={{item.BFDENABLE}},
        {%- endif -%}
        {%- if item.DESCRIPTION is not none -%}
            DESCRIPTION="{{item.DESCRIPTION}}",
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：IPVERSION=IPv6 时必选 --- -#}
        {%- if item.IPVERSION == 'IPv6' -%}
            PREFIX6="{{item.PREFIX6}}",
        {%- endif -%}
        {#- --- 条件必选：NEXTHOPALLOCTYPE6=CONFIG 时必选 --- -#}
        {%- if item.NEXTHOPALLOCTYPE6 == 'CONFIG' -%}
            NEXTHOP6="{{item.NEXTHOP6}}",
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：IPVERSION=IPv6 时可选 --- -#}
        {%- if item.IPVERSION == 'IPv6' -%}
            {%- if item.NEXTHOPALLOCTYPE6 is not none -%}
                NEXTHOPALLOCTYPE6={{item.NEXTHOPALLOCTYPE6}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：BFDENABLE=TRUE 时可选 --- -#}
        {%- if item.BFDENABLE == 'TRUE' -%}
            {%- if item.BFDTEMPLATENAME is not none -%}
                BFDTEMPLATENAME="{{item.BFDTEMPLATENAME}}",
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 6 打开自动部署开关。

```jinja2
{%- for item in set_autoconfig_list_1 -%}
    SET AUTOCONFIG:
    {#- --- 必选参数 --- -#}
    SWITCHFLAG={{item.SWITCHFLAG}},
    ;
{%- endfor -%}
```

### 从自动部署开关打开到自动部署功能生效有时延，因此执行其他操作前（例如手动部署路由互通、关闭自动部署开关），务必先执行**DSP OPSASSISTSTATE**命令查询自动部署维护助手“autoscaling\_autoconfig.py”的状态为“准备好状态（Ready）”，否则结果不可预期。

### 7 配置应急UDM的业务数据。

### **表4** 应急UDM的业务数据

### | 配置项目 | 配置参考 | 容灾说明 |

### | --- | --- | --- |

### | 配置USCDB业务IP及激活插件包 | 配置USCDB基础数据 | USCDB仅与本DC内的UDM互通，UDM仅与本DC内的USCDB互通。  园区双DC场景，选择本DC的应急AMF、应急SMF，容灾与非容灾场景仅样例值有区别，其他没有区别。 |

### | 配置UDM业务IP | 配置UDM基础数据 |  |

### | 配置UDM和USCDB对接数据 | 配置UDM和USCDB对接配置 |  |

### | 配置与应急AMF互通数据 | 配置HTTP信令数据 |  |

### | 配置用户数据文件同步 | 配置用户数据文件同步 |  |

### | 配置全局数据 | 配置全局数据 |  |

### | 配置鉴权数据 | 配置鉴权数据 |  |

### | 配置模板数据 | 配置模板数据 |  |


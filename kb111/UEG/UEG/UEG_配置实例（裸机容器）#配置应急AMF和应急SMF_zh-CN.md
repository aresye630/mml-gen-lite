---
id: ''
name: 配置应急AMF和应急SMF
ne_type: UEG
type: feature
description: 高可用边缘网关部署在企业园区，新开局场景，需要配置应急AMF和应急SMF实体功能，以保证应急场景下新注册用户或发生信令交互的已注册用户能够正常开展业务。  **图1** 应急AMF和应急SMF与其他网络实体的逻辑接口
tags: []
risk_level: ''
doc_source: ["网络部署","园区入驻式（仅连接）","5GC toB 部署边缘站点（站点为“风筝M”，入驻式）","UEG初始配置（风筝M）","配置实例（裸机容器）","配置应急AMF和应急SMF"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
高可用边缘网关部署在企业园区，新开局场景，需要配置应急AMF和应急SMF实体功能，以保证应急场景下新注册用户或发生信令交互的已注册用户能够正常开展业务。**图1** 应急AMF和应急SMF与其他网络实体的逻辑接口

## 必备事项
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
    add_ethsubif_list:
      type: items
      properties:
        IFNAME:
          name: '子接口名字'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VLANTYPEVID:
          name: 'VLAN ID'
          type: integer
          minimum: 1
          maximum: 4094
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
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
    add_ifipv4address_list_2:
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
    add_ifipv6address_list_2:
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
    add_bfdsession_list:
      type: items
      properties:
        SESSNAME:
          name: '会话名称'
          type: string
          maxLength: 64
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ADDRTYPE:
          name: 'IP协议版本号'
          type: string
          enum:
          - IPv4
          - IPv6
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CREATETYPE4:
          name: 'IPv4会话创建方式'
          type: string
          enum:
          - SESS_AUTO
          - SESS_STATIC
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ONEARMECHO:
          name: 'IPv4单臂Echo'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DESTADDR4:
          name: 'IPv4目的地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LINKTYPE:
          name: '会话链路类型'
          type: string
          enum:
          - IP
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
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
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
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
        LOCALDISCR:
          name: '本地标识符'
          type: integer
          minimum: 1
          maximum: 16384
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IFNAME:
          name: '出接口名称'
          type: string
          maxLength: 63
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CREATETYPE6:
          name: 'IPv6会话创建方式'
          type: string
          enum:
          - SESS_AUTO
          - SESS_STATIC
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ONEARMECHO6:
          name: 'IPv6单臂Echo'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        DESTADDR6:
          name: 'IPv6目的地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_bfdsession_list_4:
      type: items
      properties:
        SESSNAME:
          name: '会话名称'
          type: string
          maxLength: 64
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ADDRTYPE:
          name: 'IP协议版本号'
          type: string
          enum:
          - IPv4
          - IPv6
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CREATETYPE4:
          name: 'IPv4会话创建方式'
          type: string
          enum:
          - SESS_AUTO
          - SESS_STATIC
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ONEARMECHO:
          name: 'IPv4单臂Echo'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DESTADDR4:
          name: 'IPv4目的地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LINKTYPE:
          name: '会话链路类型'
          type: string
          enum:
          - IP
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MINTXINT:
          name: '最小发送间隔（ms）'
          type: integer
          minimum: 30
          maximum: 1000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 200
        MINRXINT:
          name: '最小接收间隔（ms）'
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
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LOCALDISCR:
          name: '本地标识符'
          type: integer
          minimum: 1
          maximum: 16384
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        REMOTEDISCR:
          name: '远端标识符'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IFNAME:
          name: '出接口名称'
          type: string
          maxLength: 63
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CREATETYPE6:
          name: 'IPv6会话创建方式'
          type: string
          enum:
          - SESS_AUTO
          - SESS_STATIC
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ONEARMECHO6:
          name: 'IPv6单臂Echo'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        DESTADDR6:
          name: 'IPv6目的地址'
          type: string
          maxLength: 39
          required: false
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
        SESSIONNAME:
          name: '静态BFD会话名'
          type: string
          maxLength: 64
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_srroute6_list:
      type: items
      properties:
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
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: ''
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
        SESSIONNAME:
          name: '静态BFD会话名'
          type: string
          maxLength: 64
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_srroute_list_2:
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
        SESSIONNAME:
          name: '静态BFD会话名'
          type: string
          maxLength: 64
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_srroute_list_4:
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
        SESSIONNAME:
          name: '静态BFD会话名'
          type: string
          maxLength: 64
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_srroute6_list_2:
      type: items
      properties:
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
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: ''
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
        SESSIONNAME:
          name: '静态BFD会话名'
          type: string
          maxLength: 64
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_srroute6_list_4:
      type: items
      properties:
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
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: ''
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
        SESSIONNAME:
          name: '静态BFD会话名'
          type: string
          maxLength: 64
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
    add_interface_list_3:
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
    add_ipbindvpn_list_3:
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
    add_ethsubif_list_2:
      type: items
      properties:
        IFNAME:
          name: '子接口名字'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VLANTYPEVID:
          name: 'VLAN ID'
          type: integer
          minimum: 1
          maximum: 4094
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_ifipv6enable_list_3:
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
    add_ifipv4address_list_3:
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
    add_ifipv6address_list_3:
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
    add_bfdsession_list_8:
      type: items
      properties:
        SESSNAME:
          name: '会话名称'
          type: string
          maxLength: 64
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ADDRTYPE:
          name: 'IP协议版本号'
          type: string
          enum:
          - IPv4
          - IPv6
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CREATETYPE4:
          name: 'IPv4会话创建方式'
          type: string
          enum:
          - SESS_AUTO
          - SESS_STATIC
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ONEARMECHO:
          name: 'IPv4单臂Echo'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DESTADDR4:
          name: 'IPv4目的地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LINKTYPE:
          name: '会话链路类型'
          type: string
          enum:
          - IP
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
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
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
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
        LOCALDISCR:
          name: '本地标识符'
          type: integer
          minimum: 1
          maximum: 16384
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IFNAME:
          name: '出接口名称'
          type: string
          maxLength: 63
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CREATETYPE6:
          name: 'IPv6会话创建方式'
          type: string
          enum:
          - SESS_AUTO
          - SESS_STATIC
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ONEARMECHO6:
          name: 'IPv6单臂Echo'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        DESTADDR6:
          name: 'IPv6目的地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_srroute_list_6:
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
        SESSIONNAME:
          name: '静态BFD会话名'
          type: string
          maxLength: 64
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_srroute6_list_6:
      type: items
      properties:
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
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: ''
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
        SESSIONNAME:
          name: '静态BFD会话名'
          type: string
          maxLength: 64
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
    add_interface_list_4:
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
    add_interface_list_5:
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
    add_ipbindvpn_list_5:
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
    add_ethsubif_list_3:
      type: items
      properties:
        IFNAME:
          name: '子接口名字'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VLANTYPEVID:
          name: 'VLAN ID'
          type: integer
          minimum: 1
          maximum: 4094
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_ifipv6enable_list_5:
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
    add_ifipv4address_list_5:
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
    add_ifipv6address_list_5:
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
    add_bfdsession_list_10:
      type: items
      properties:
        SESSNAME:
          name: '会话名称'
          type: string
          maxLength: 64
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ADDRTYPE:
          name: 'IP协议版本号'
          type: string
          enum:
          - IPv4
          - IPv6
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CREATETYPE4:
          name: 'IPv4会话创建方式'
          type: string
          enum:
          - SESS_AUTO
          - SESS_STATIC
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ONEARMECHO:
          name: 'IPv4单臂Echo'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DESTADDR4:
          name: 'IPv4目的地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LINKTYPE:
          name: '会话链路类型'
          type: string
          enum:
          - IP
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MINTXINT:
          name: '最小发送间隔（ms）'
          type: integer
          minimum: 30
          maximum: 1000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 200
        MINRXINT:
          name: '最小接收间隔（ms）'
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
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LOCALDISCR:
          name: '本地标识符'
          type: integer
          minimum: 1
          maximum: 16384
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        REMOTEDISCR:
          name: '远端标识符'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IFNAME:
          name: '出接口名称'
          type: string
          maxLength: 63
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CREATETYPE6:
          name: 'IPv6会话创建方式'
          type: string
          enum:
          - SESS_AUTO
          - SESS_STATIC
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ONEARMECHO6:
          name: 'IPv6单臂Echo'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        DESTADDR6:
          name: 'IPv6目的地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_bfdsession_list_14:
      type: items
      properties:
        SESSNAME:
          name: '会话名称'
          type: string
          maxLength: 64
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ADDRTYPE:
          name: 'IP协议版本号'
          type: string
          enum:
          - IPv4
          - IPv6
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CREATETYPE4:
          name: 'IPv4会话创建方式'
          type: string
          enum:
          - SESS_AUTO
          - SESS_STATIC
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ONEARMECHO:
          name: 'IPv4单臂Echo'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DESTADDR4:
          name: 'IPv4目的地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LINKTYPE:
          name: '会话链路类型'
          type: string
          enum:
          - IP
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
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
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
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
        LOCALDISCR:
          name: '本地标识符'
          type: integer
          minimum: 1
          maximum: 16384
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IFNAME:
          name: '出接口名称'
          type: string
          maxLength: 63
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CREATETYPE6:
          name: 'IPv6会话创建方式'
          type: string
          enum:
          - SESS_AUTO
          - SESS_STATIC
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ONEARMECHO6:
          name: 'IPv6单臂Echo'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        DESTADDR6:
          name: 'IPv6目的地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_srroute_list_7:
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
        SESSIONNAME:
          name: '静态BFD会话名'
          type: string
          maxLength: 64
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_srroute6_list_7:
      type: items
      properties:
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
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: ''
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
        SESSIONNAME:
          name: '静态BFD会话名'
          type: string
          maxLength: 64
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_srroute_list_9:
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
        SESSIONNAME:
          name: '静态BFD会话名'
          type: string
          maxLength: 64
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_srroute_list_11:
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
        SESSIONNAME:
          name: '静态BFD会话名'
          type: string
          maxLength: 64
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_srroute6_list_9:
      type: items
      properties:
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
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: ''
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
        SESSIONNAME:
          name: '静态BFD会话名'
          type: string
          maxLength: 64
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_srroute6_list_11:
      type: items
      properties:
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
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: ''
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
        SESSIONNAME:
          name: '静态BFD会话名'
          type: string
          maxLength: 64
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    add_l3vpninst_list:
    - VRFNAME: 'VRF_SBI'
    add_vpninstaf_list:
    - VRFNAME: 'VRF_SBI'
      AFTYPE: ipv4uni
      VRFRD: '192.168.225.205:100'
    add_interface_list:
    - IFNAME: 'LoopBack205'
    add_ipbindvpn_list:
    - IFNAME: 'LoopBack205'
      VRFNAME: 'VRF_SBI'
    add_ifipv4address_list:
    - IFNAME: 'LoopBack205'
      IFIPADDR: '192.168.225.205'
      SUBNETMASK: '255.255.255.255'
      ADDRTYPE: main
    set_ifipv6enable_list:
    - IFNAME: 'Loopback205'
      ENABLEFLAG: TRUE
    add_ifipv6address_list:
    - IFNAME: 'Loopback205'
      IPV6ADDRESS: 'FC00::225:205'
      PREFIXLEN: 128
    add_bgpvrf_list:
    - VRFNAME: 'VRF_SBI'
      DEFAULTAFTYPE: noaf
      ROUTERID: '192.168.225.205'
    add_bgpvrfaf_list:
    - VRFNAME: 'VRF_SBI'
      AFTYPE: ipv4uni
      MAXIMUMLOADBALANCE: 2
    add_bgppeer_list:
    - VRFNAME: 'VRF_SBI'
      ADDRESSTYPE: ipv4
      PEERADDR: '192.168.79.205'
      REMOTEAS: '60002'
      LOCALIFADDR: '192.168.225.205'
      LOCALIFNAME: 'Loopback205'
      EBGPMAXHOP: 10
      PEERADDRV6: 'FC00::79:205'
    add_importroute_list:
    - VRFNAME: 'VRF_SBI'
      AFTYPE: ipv4uni
      IMPORTPROTOCOL: wlr
      MEDENABLE: FALSE
    add_interface_list_1:
    - IFNAME: 'Eth-trunk1.3'
    add_ipbindvpn_list_1:
    - IFNAME: 'Eth-trunk1.3'
      VRFNAME: 'VRF_SBI'
    add_ethsubif_list:
    - IFNAME: 'Eth-trunk1.3'
      VLANTYPEVID: 2205
    set_ifipv6enable_list_1:
    - IFNAME: 'Eth-trunk1.3'
      ENABLEFLAG: TRUE
    add_ifipv4address_list_1:
    - IFNAME: 'Eth-trunk1.3'
      IFIPADDR: '192.168.205.2'
      SUBNETMASK: '255.255.255.248'
    add_ifipv6address_list_1:
    - IFNAME: 'Eth-trunk1.3'
      IPV6ADDRESS: 'FC00::205:2'
      PREFIXLEN: 125
    add_ifipv4address_list_2:
    - IFNAME: 'Eth-trunk2.3'
      IFIPADDR: '192.168.105.2'
      SUBNETMASK: '255.255.255.248'
    add_ifipv6address_list_2:
    - IFNAME: 'Eth-trunk2.3'
      IPV6ADDRESS: 'FC00::105:2'
      PREFIXLEN: 125
    add_bfdsession_list:
    - SESSNAME: 'BfdName2051_v4'
      ADDRTYPE: IPv4
      CREATETYPE4: SESS_STATIC
      ONEARMECHO: TRUE
      DESTADDR4: '192.168.205.1'
      LINKTYPE: IP
      DETECTMULTI: 4
      VRFNAME: 'VRF_SBI'
      MINECHORXINT: 500
      LOCALDISCR: 10541
      IFNAME: 'Eth-trunk1.3'
      CREATETYPE6: SESS_STATIC
      ONEARMECHO6: TRUE
      DESTADDR6: 'FC00::205:1'
    add_bfdsession_list_4:
    - SESSNAME: 'BfdName2051_v4'
      ADDRTYPE: IPv4
      CREATETYPE4: SESS_STATIC
      ONEARMECHO: FALSE
      DESTADDR4: '192.168.205.1'
      LINKTYPE: IP
      MINTXINT: 500
      MINRXINT: 500
      DETECTMULTI: 4
      VRFNAME: 'VRF_SBI'
      LOCALDISCR: 10541
      REMOTEDISCR: 8542
      IFNAME: 'Eth-trunk1.3'
      CREATETYPE6: SESS_STATIC
      ONEARMECHO6: FALSE
      DESTADDR6: 'FC00::205:1'
    add_srroute_list:
    - AFTYPE: ipv4unicast
      PREFIX: 'x.x.x.x'
      MASKLENGTH: 32
      VRFNAME: 'VRF_SBI'
      DESTVRFNAME: 'VRF_SBI'
      IFNAME: 'Eth-trunk1.3'
      NEXTHOP: '192.168.205.1'
      SESSIONNAME: 'BfdName2051_v4'
    - AFTYPE: ipv4unicast
      PREFIX: 'x.x.x.x'
      MASKLENGTH: 32
      VRFNAME: 'VRF_SBI'
      DESTVRFNAME: 'VRF_SBI'
      IFNAME: 'Eth-trunk2.3'
      NEXTHOP: '192.168.105.1'
      SESSIONNAME: 'BfdName2052_v4'
    add_srroute6_list:
    - AFTYPE: ipv6unicast
      PREFIX: 'FC00:x::x'
      MASKLENGTH: 128
      VRFNAME: 'VRF_SBI'
      DESTVRFNAME: 'VRF_SBI'
      IFNAME: 'Eth-trunk1.3'
      NEXTHOP: 'FC00::205:1'
      SESSIONNAME: 'BfdName2051_v6'
    - AFTYPE: ipv6unicast
      PREFIX: 'FC00:x::x'
      MASKLENGTH: 128
      VRFNAME: 'VRF_SBI'
      DESTVRFNAME: 'VRF_SBI'
      IFNAME: 'Eth-trunk2.3'
      NEXTHOP: 'FC00::105:1'
      SESSIONNAME: 'BfdName2052_v6'
    add_srroute_list_2:
    - AFTYPE: ipv4unicast
      PREFIX: '192.168.79.205'
      MASKLENGTH: 32
      VRFNAME: 'VRF_SBI'
      DESTVRFNAME: 'VRF_SBI'
      IFNAME: 'Eth-trunk1.3'
      NEXTHOP: '192.168.205.1'
      SESSIONNAME: 'BfdName2051_v4'
    add_srroute_list_4:
    - AFTYPE: ipv4unicast
      PREFIX: '0.0.0.0'
      MASKLENGTH: 0
      VRFNAME: 'VRF_SBI'
      DESTVRFNAME: 'VRF_SBI'
      IFNAME: 'Eth-trunk1.3'
      NEXTHOP: '192.168.205.1'
      SESSIONNAME: 'BfdName2051_v4'
    add_srroute6_list_2:
    - AFTYPE: ipv6unicast
      PREFIX: 'FC00::79:205'
      MASKLENGTH: 128
      VRFNAME: 'VRF_SBI'
      DESTVRFNAME: 'VRF_SBI'
      IFNAME: 'Eth-trunk1.3'
      NEXTHOP: 'FC00::205:1'
      SESSIONNAME: 'BfdName2051_v6'
    add_srroute6_list_4:
    - AFTYPE: ipv6unicast
      PREFIX: '0:0:0:0:0:0:0:0'
      MASKLENGTH: 0
      VRFNAME: 'VRF_SBI'
      DESTVRFNAME: 'VRF_SBI'
      IFNAME: 'Eth-trunk1.3'
      NEXTHOP: 'FC00::205:1'
      SESSIONNAME: 'BfdName2051_v6'
    add_l3vpninst_list_1:
    - VRFNAME: 'VRF_SBI'
    add_vpninstaf_list_2:
    - VRFNAME: 'VRF_SBI'
      AFTYPE: ipv4uni
      VRFRD: '192.168.225.205:100'
    add_interface_list_3:
    - IFNAME: 'Eth-trunk1.3'
    add_ipbindvpn_list_3:
    - IFNAME: 'Eth-trunk1.3'
      VRFNAME: 'VRF_SBI'
    add_ethsubif_list_2:
    - IFNAME: 'Eth-trunk1.3'
      VLANTYPEVID: 2205
    set_ifipv6enable_list_3:
    - IFNAME: 'Eth-trunk1.3'
      ENABLEFLAG: TRUE
    add_ifipv4address_list_3:
    - IFNAME: 'Eth-trunk1.3'
      IFIPADDR: '192.168.205.2'
      SUBNETMASK: '255.255.255.248'
    add_ifipv6address_list_3:
    - IFNAME: 'Eth-trunk1.3'
      IPV6ADDRESS: 'FC00::205:2'
      PREFIXLEN: 125
    add_bfdsession_list_8:
    - SESSNAME: 'BfdName2051_v4'
      ADDRTYPE: IPv4
      CREATETYPE4: SESS_STATIC
      ONEARMECHO: TRUE
      DESTADDR4: '192.168.205.1'
      LINKTYPE: IP
      DETECTMULTI: 4
      VRFNAME: 'VRF_SBI'
      MINECHORXINT: 500
      LOCALDISCR: 10541
      IFNAME: 'Eth-trunk1.3'
      CREATETYPE6: SESS_STATIC
      ONEARMECHO6: TRUE
      DESTADDR6: 'FC00::205:1'
    add_srroute_list_6:
    - AFTYPE: ipv4unicast
      PREFIX: 'x.x.x.x'
      MASKLENGTH: 32
      VRFNAME: 'VRF_SBI'
      DESTVRFNAME: 'VRF_SBI'
      IFNAME: 'Eth-trunk1.3'
      NEXTHOP: '192.168.205.1'
      SESSIONNAME: 'BfdName2051_v4'
    add_srroute6_list_6:
    - AFTYPE: ipv6unicast
      PREFIX: 'FC00:x::x'
      MASKLENGTH: 128
      VRFNAME: 'VRF_SBI'
      DESTVRFNAME: 'VRF_SBI'
      IFNAME: 'Eth-trunk1.3'
      NEXTHOP: 'FC00::205:1'
      SESSIONNAME: 'BfdName2051_v6'
    add_l3vpninst_list_2:
    - VRFNAME: 'VRF_AAA'
    add_vpninstaf_list_4:
    - VRFNAME: 'VRF_AAA'
      AFTYPE: ipv4uni
      VRFRD: '192.168.225.206:100'
    add_interface_list_4:
    - IFNAME: 'LoopBack206'
    add_ipbindvpn_list_4:
    - IFNAME: 'LoopBack206'
      VRFNAME: 'VRF_AAA'
    add_ifipv4address_list_4:
    - IFNAME: 'LoopBack206'
      IFIPADDR: '192.168.225.206'
      SUBNETMASK: '255.255.255.255'
      ADDRTYPE: main
    set_ifipv6enable_list_4:
    - IFNAME: 'Loopback206'
      ENABLEFLAG: TRUE
    add_ifipv6address_list_4:
    - IFNAME: 'Loopback206'
      IPV6ADDRESS: 'FC00::225:206'
      PREFIXLEN: 128
    add_bgpvrf_list_1:
    - VRFNAME: 'VRF_AAA'
      DEFAULTAFTYPE: noaf
      ROUTERID: '192.168.225.206'
    add_bgpvrfaf_list_2:
    - VRFNAME: 'VRF_AAA'
      AFTYPE: ipv4uni
      MAXIMUMLOADBALANCE: 2
    add_bgppeer_list_4:
    - VRFNAME: 'VRF_AAA'
      ADDRESSTYPE: ipv4
      PEERADDR: '192.168.79.206'
      REMOTEAS: '60002'
      LOCALIFADDR: '192.168.225.206'
      LOCALIFNAME: 'Loopback206'
      EBGPMAXHOP: 10
      PEERADDRV6: 'FC00::79:206'
    add_importroute_list_2:
    - VRFNAME: 'VRF_AAA'
      AFTYPE: ipv4uni
      IMPORTPROTOCOL: wlr
      MEDENABLE: FALSE
    add_interface_list_5:
    - IFNAME: 'Ethernet64/0/6.3'
    add_ipbindvpn_list_5:
    - IFNAME: 'Ethernet64/0/6.3'
      VRFNAME: 'VRF_AAA'
    add_ethsubif_list_3:
    - IFNAME: 'Ethernet64/0/6.3'
      VLANTYPEVID: 2206
    set_ifipv6enable_list_5:
    - IFNAME: 'Ethernet64/0/6.3'
      ENABLEFLAG: TRUE
    add_ifipv4address_list_5:
    - IFNAME: 'Ethernet64/0/6.3'
      IFIPADDR: '192.168.206.2'
      SUBNETMASK: '255.255.255.248'
    add_ifipv6address_list_5:
    - IFNAME: 'Ethernet64/0/6.3'
      IPV6ADDRESS: 'FC00::206:2'
      PREFIXLEN: 125
    add_bfdsession_list_10:
    - SESSNAME: 'BfdName2061_v4'
      ADDRTYPE: IPv4
      CREATETYPE4: SESS_STATIC
      ONEARMECHO: FALSE
      DESTADDR4: '192.168.206.1'
      LINKTYPE: IP
      MINTXINT: 500
      MINRXINT: 500
      DETECTMULTI: 4
      VRFNAME: 'VRF_AAA'
      LOCALDISCR: 2641
      REMOTEDISCR: 2642
      IFNAME: 'Ethernet64/0/6.3'
      CREATETYPE6: SESS_STATIC
      ONEARMECHO6: FALSE
      DESTADDR6: 'FC00::206:1'
    add_bfdsession_list_14:
    - SESSNAME: 'BfdName2061_v4'
      ADDRTYPE: IPv4
      CREATETYPE4: SESS_STATIC
      ONEARMECHO: TRUE
      DESTADDR4: '192.168.206.1'
      LINKTYPE: IP
      DETECTMULTI: 4
      VRFNAME: 'VRF_AAA'
      MINECHORXINT: 500
      LOCALDISCR: 2641
      IFNAME: 'Ethernet64/0/6.3'
      CREATETYPE6: SESS_STATIC
      ONEARMECHO6: TRUE
      DESTADDR6: 'FC00::206:1'
    add_srroute_list_7:
    - AFTYPE: ipv4unicast
      PREFIX: 'x.x.x.x'
      MASKLENGTH: 32
      VRFNAME: 'VRF_AAA'
      DESTVRFNAME: 'VRF_AAA'
      IFNAME: 'Ethernet64/0/6.3'
      NEXTHOP: '192.168.206.1'
      SESSIONNAME: 'BfdName2061_v4'
    add_srroute6_list_7:
    - AFTYPE: ipv6unicast
      PREFIX: 'FC00:x::x'
      MASKLENGTH: 128
      VRFNAME: 'VRF_AAA'
      DESTVRFNAME: 'VRF_AAA'
      IFNAME: 'Ethernet64/0/6.3'
      NEXTHOP: 'FC00::206:1'
      SESSIONNAME: 'BfdName2061_v6'
    add_srroute_list_9:
    - AFTYPE: ipv4unicast
      PREFIX: '192.168.79.206'
      MASKLENGTH: 32
      VRFNAME: 'VRF_AAA'
      DESTVRFNAME: 'VRF_AAA'
      IFNAME: 'Ethernet64/0/6.3'
      NEXTHOP: '192.168.206.1'
      SESSIONNAME: 'BfdName2061_v4'
    add_srroute_list_11:
    - AFTYPE: ipv4unicast
      PREFIX: '0.0.0.0'
      MASKLENGTH: 0
      VRFNAME: 'VRF_AAA'
      DESTVRFNAME: 'VRF_AAA'
      IFNAME: 'Ethernet64/0/6.3'
      NEXTHOP: '192.168.206.1'
      SESSIONNAME: 'BfdName2061_v4'
    add_srroute6_list_9:
    - AFTYPE: ipv6unicast
      PREFIX: 'FC00::79:206'
      MASKLENGTH: 128
      VRFNAME: 'VRF_AAA'
      DESTVRFNAME: 'VRF_AAA'
      IFNAME: 'Ethernet64/0/6.3'
      NEXTHOP: 'FC00::206:1'
      SESSIONNAME: 'BfdName2061_v6'
    add_srroute6_list_11:
    - AFTYPE: ipv6unicast
      PREFIX: '0:0:0:0:0:0:0:0'
      MASKLENGTH: 0
      VRFNAME: 'VRF_AAA'
      DESTVRFNAME: 'VRF_AAA'
      IFNAME: 'Ethernet64/0/6.3'
      NEXTHOP: 'FC00::206:1'
      SESSIONNAME: 'BfdName2061_v6'
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 登录“MML命令行-UEG”界面。

### 2 直连DCGW时，配置UEG间互通的IP路由数据。例如：传输应急UDM通过N8接口向另一UEG中的应急AMF主动发送的cancel location报文。

#### 2.1 配置VPN实例。

```jinja2
{%- if is_scenario_direct_to_dcgw -%}
    {%- for item in add_l3vpninst_list -%}
        ADD L3VPNINST:
        {#- --- 必选参数 --- -#}
        VRFNAME="{{item.VRFNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_direct_to_dcgw -%}
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
{%- endif -%}
```

#### 步骤2.b~步骤2.f是BGP相关数据，仅采用BGP over静态路由+BFD时需要配置。采用静态路由+BFD时不需要配置。

#### 2.2 配置Loopback接口IP。用于建立BGP邻居。

```jinja2
{%- if is_scenario_direct_to_dcgw and is_scenario_bgp_over_static_bfd -%}
    {%- for item in add_interface_list -%}
        ADD INTERFACE:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_direct_to_dcgw and is_scenario_bgp_over_static_bfd -%}
    {%- for item in add_ipbindvpn_list -%}
        ADD IPBINDVPN:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        VRFNAME="{{item.VRFNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_direct_to_dcgw and is_scenario_bgp_over_static_bfd -%}
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
{%- endif -%}
```

```jinja2
{%- if is_scenario_direct_to_dcgw and is_scenario_bgp_over_static_bfd -%}
    {%- for item in set_ifipv6enable_list -%}
        SET IFIPV6ENABLE:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        ENABLEFLAG={{item.ENABLEFLAG}},
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_direct_to_dcgw and is_scenario_bgp_over_static_bfd -%}
    {%- for item in add_ifipv6address_list -%}
        ADD IFIPV6ADDRESS:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        IPV6ADDRESS="{{item.IPV6ADDRESS}}",
        PREFIXLEN={{item.PREFIXLEN}},
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 2.3 配置BGP VPN实例。

```jinja2
{%- if is_scenario_direct_to_dcgw and is_scenario_bgp_over_static_bfd -%}
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
{%- endif -%}
```

#### 2.4 增加BGP VPN实例地址族。

##### 2.4.1 //UEG对接2个负荷分担的BGP PEER，“MAXIMUMLOADBALANCE”设置为“2”。

```jinja2
{%- if is_scenario_direct_to_dcgw and is_scenario_bgp_over_static_bfd -%}
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
{%- endif -%}
```

#### 2.5 配置BGP对等体。此处以对接2个IPv4v6双栈的BGP对等体为例。

```jinja2
{%- if is_scenario_direct_to_dcgw and is_scenario_bgp_over_static_bfd -%}
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
{%- endif -%}
```

#### 2.6 配置BGP引入wlr路由。

```jinja2
{%- if is_scenario_direct_to_dcgw and is_scenario_bgp_over_static_bfd -%}
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
{%- endif -%}
```

#### 2.7 配置外联口IP地址。

##### 2.7.1 添加Eth-trunk子接口。此处以与N3/N4复用物理端口为例。

```jinja2
{%- if is_scenario_direct_to_dcgw -%}
    {%- for item in add_interface_list_1 -%}
        ADD INTERFACE:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 2.7.2 增加接口绑定VPN。

```jinja2
{%- if is_scenario_direct_to_dcgw -%}
    {%- for item in add_ipbindvpn_list_1 -%}
        ADD IPBINDVPN:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        VRFNAME="{{item.VRFNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 2.7.3 在以太网子接口上关联VLAN ID。

```jinja2
{%- if is_scenario_direct_to_dcgw -%}
    {%- for item in add_ethsubif_list -%}
        ADD ETHSUBIF:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        VLANTYPEVID={{item.VLANTYPEVID}},
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 2.7.4 配置IPv6使能。

```jinja2
{%- if is_scenario_direct_to_dcgw -%}
    {%- for item in set_ifipv6enable_list_1 -%}
        SET IFIPV6ENABLE:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        ENABLEFLAG={{item.ENABLEFLAG}},
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 2.7.5 配置外联口IP地址。

```jinja2
{%- if is_scenario_direct_to_dcgw -%}
    {%- for item in add_ifipv4address_list_1 -%}
        ADD IFIPV4ADDRESS:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        IFIPADDR="{{item.IFIPADDR}}",
        SUBNETMASK="{{item.SUBNETMASK}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_direct_to_dcgw -%}
    {%- for item in add_ifipv6address_list_1 -%}
        ADD IFIPV6ADDRESS:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        IPV6ADDRESS="{{item.IPV6ADDRESS}}",
        PREFIXLEN={{item.PREFIXLEN}},
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_direct_to_dcgw -%}
    {%- for item in add_ifipv4address_list_2 -%}
        ADD IFIPV4ADDRESS:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        IFIPADDR="{{item.IFIPADDR}}",
        SUBNETMASK="{{item.SUBNETMASK}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_direct_to_dcgw -%}
    {%- for item in add_ifipv6address_list_2 -%}
        ADD IFIPV6ADDRESS:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        IPV6ADDRESS="{{item.IPV6ADDRESS}}",
        PREFIXLEN={{item.PREFIXLEN}},
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 2.8 新建BFD会话。

##### 2.8.1 //配置BFD单臂echo探测。直连DCGW场景，请配置该步骤。PE支持BFD时，可采用单臂echo或双向BFD探测。

```jinja2
{%- if is_scenario_direct_to_dcgw and is_scenario_bfd_onearm_echo -%}
    {%- for item in add_bfdsession_list -%}
        ADD BFDSESSION:
        {#- --- 必选参数 --- -#}
        SESSNAME="{{item.SESSNAME}}",
        ADDRTYPE={{item.ADDRTYPE}},
        LINKTYPE={{item.LINKTYPE}},
        {#- --- 可选参数 --- -#}
        {%- if item.DETECTMULTI is not none -%}
            DETECTMULTI={{item.DETECTMULTI}},
        {%- endif -%}
        {%- if item.VRFNAME is not none -%}
            VRFNAME="{{item.VRFNAME}}",
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：ADDRTYPE=IPv4 时必选 --- -#}
        {%- if item.ADDRTYPE == 'IPv4' -%}
            CREATETYPE4={{item.CREATETYPE4}},
        {%- endif -%}
        {#- --- 条件必选：CREATETYPE4=SESS_STATIC 时必选 --- -#}
        {%- if item.CREATETYPE4 == 'SESS_STATIC' -%}
            ONEARMECHO={{item.ONEARMECHO}},
        {%- endif -%}
        {#- --- 条件必选：ADDRTYPE=IPv4 时必选 --- -#}
        {%- if item.ADDRTYPE == 'IPv4' -%}
            DESTADDR4="{{item.DESTADDR4}}",
        {%- endif -%}
        {#- --- 条件必选：CREATETYPE4=SESS_STATIC 时必选 --- -#}
        {%- if item.CREATETYPE4 == 'SESS_STATIC' -%}
            LOCALDISCR={{item.LOCALDISCR}},
        {#- --- 条件必选：CREATETYPE6=SESS_STATIC 时必选 --- -#}
        {%- elif item.CREATETYPE6 == 'SESS_STATIC' -%}
            LOCALDISCR={{item.LOCALDISCR}},
        {%- endif -%}
        {#- --- 条件必选：ADDRTYPE=IPv6 时必选 --- -#}
        {%- if item.ADDRTYPE == 'IPv6' -%}
            CREATETYPE6={{item.CREATETYPE6}},
        {%- endif -%}
        {#- --- 条件必选：ADDRTYPE=IPv6 时必选 --- -#}
        {%- if item.ADDRTYPE == 'IPv6' -%}
            DESTADDR6="{{item.DESTADDR6}}",
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：ONEARMECHO=TRUE 时可选 --- -#}
        {%- if item.ONEARMECHO == 'TRUE' -%}
            {%- if item.MINECHORXINT is not none -%}
                MINECHORXINT={{item.MINECHORXINT}},
            {%- endif -%}
        {#- --- 条件可选：ONEARMECHO6=TRUE 时可选 --- -#}
        {%- elif item.ONEARMECHO6 == 'TRUE' -%}
            {%- if item.MINECHORXINT is not none -%}
                MINECHORXINT={{item.MINECHORXINT}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：CREATETYPE6=SESS_STATIC 时可选 --- -#}
        {%- if item.CREATETYPE6 == 'SESS_STATIC' -%}
            {%- if item.ONEARMECHO6 is not none -%}
                ONEARMECHO6={{item.ONEARMECHO6}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件必选/可选参数 --- -#}
        {#- --- 出接口名称: 条件必选(IPv4单臂Echo=TRUE; IPv6单臂Echo=TRUE) / 条件可选(IPv4会话创建方式=SESS_AUTO; IPv6会话创建方式=SESS_AUTO; IPv4单臂Echo=FALSE; IPv6单臂Echo=FALSE) --- -#}
        {%- if (item.ONEARMECHO == 'TRUE') or (item.ONEARMECHO6 == 'TRUE') -%}
            IFNAME="{{item.IFNAME}}",
        {%- elif (item.CREATETYPE4 == 'SESS_AUTO') or (item.CREATETYPE6 == 'SESS_AUTO') or (item.ONEARMECHO == 'FALSE') or (item.ONEARMECHO6 == 'FALSE') -%}
            {%- if item.IFNAME is not none -%}
                IFNAME="{{item.IFNAME}}",
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 2.8.2 //配置双向BFD探测。PE支持BFD探测且使用双向BFD探测时，请配置该步骤。其他场景请跳过该步骤。

```jinja2
{%- if is_scenario_direct_to_dcgw and is_scenario_bfd_bidirectional -%}
    {%- for item in add_bfdsession_list_4 -%}
        ADD BFDSESSION:
        {#- --- 必选参数 --- -#}
        SESSNAME="{{item.SESSNAME}}",
        ADDRTYPE={{item.ADDRTYPE}},
        LINKTYPE={{item.LINKTYPE}},
        {#- --- 可选参数 --- -#}
        {%- if item.DETECTMULTI is not none -%}
            DETECTMULTI={{item.DETECTMULTI}},
        {%- endif -%}
        {%- if item.VRFNAME is not none -%}
            VRFNAME="{{item.VRFNAME}}",
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：ADDRTYPE=IPv4 时必选 --- -#}
        {%- if item.ADDRTYPE == 'IPv4' -%}
            CREATETYPE4={{item.CREATETYPE4}},
        {%- endif -%}
        {#- --- 条件必选：CREATETYPE4=SESS_STATIC 时必选 --- -#}
        {%- if item.CREATETYPE4 == 'SESS_STATIC' -%}
            ONEARMECHO={{item.ONEARMECHO}},
        {%- endif -%}
        {#- --- 条件必选：ADDRTYPE=IPv4 时必选 --- -#}
        {%- if item.ADDRTYPE == 'IPv4' -%}
            DESTADDR4="{{item.DESTADDR4}}",
        {%- endif -%}
        {#- --- 条件必选：CREATETYPE4=SESS_STATIC 时必选 --- -#}
        {%- if item.CREATETYPE4 == 'SESS_STATIC' -%}
            LOCALDISCR={{item.LOCALDISCR}},
        {#- --- 条件必选：CREATETYPE6=SESS_STATIC 时必选 --- -#}
        {%- elif item.CREATETYPE6 == 'SESS_STATIC' -%}
            LOCALDISCR={{item.LOCALDISCR}},
        {%- endif -%}
        {#- --- 条件必选：ONEARMECHO=FALSE 时必选 --- -#}
        {%- if item.ONEARMECHO == 'FALSE' -%}
            REMOTEDISCR={{item.REMOTEDISCR}},
        {#- --- 条件必选：ONEARMECHO6=FALSE 时必选 --- -#}
        {%- elif item.ONEARMECHO6 == 'FALSE' -%}
            REMOTEDISCR={{item.REMOTEDISCR}},
        {%- endif -%}
        {#- --- 条件必选：ADDRTYPE=IPv6 时必选 --- -#}
        {%- if item.ADDRTYPE == 'IPv6' -%}
            CREATETYPE6={{item.CREATETYPE6}},
        {%- endif -%}
        {#- --- 条件必选：ADDRTYPE=IPv6 时必选 --- -#}
        {%- if item.ADDRTYPE == 'IPv6' -%}
            DESTADDR6="{{item.DESTADDR6}}",
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：CREATETYPE4=SESS_AUTO 时可选 --- -#}
        {%- if item.CREATETYPE4 == 'SESS_AUTO' -%}
            {%- if item.MINTXINT is not none -%}
                MINTXINT={{item.MINTXINT}},
            {%- endif -%}
        {#- --- 条件可选：CREATETYPE6=SESS_AUTO 时可选 --- -#}
        {%- elif item.CREATETYPE6 == 'SESS_AUTO' -%}
            {%- if item.MINTXINT is not none -%}
                MINTXINT={{item.MINTXINT}},
            {%- endif -%}
        {#- --- 条件可选：ONEARMECHO=FALSE 时可选 --- -#}
        {%- elif item.ONEARMECHO == 'FALSE' -%}
            {%- if item.MINTXINT is not none -%}
                MINTXINT={{item.MINTXINT}},
            {%- endif -%}
        {#- --- 条件可选：ONEARMECHO6=FALSE 时可选 --- -#}
        {%- elif item.ONEARMECHO6 == 'FALSE' -%}
            {%- if item.MINTXINT is not none -%}
                MINTXINT={{item.MINTXINT}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：CREATETYPE4=SESS_AUTO 时可选 --- -#}
        {%- if item.CREATETYPE4 == 'SESS_AUTO' -%}
            {%- if item.MINRXINT is not none -%}
                MINRXINT={{item.MINRXINT}},
            {%- endif -%}
        {#- --- 条件可选：CREATETYPE6=SESS_AUTO 时可选 --- -#}
        {%- elif item.CREATETYPE6 == 'SESS_AUTO' -%}
            {%- if item.MINRXINT is not none -%}
                MINRXINT={{item.MINRXINT}},
            {%- endif -%}
        {#- --- 条件可选：ONEARMECHO=FALSE 时可选 --- -#}
        {%- elif item.ONEARMECHO == 'FALSE' -%}
            {%- if item.MINRXINT is not none -%}
                MINRXINT={{item.MINRXINT}},
            {%- endif -%}
        {#- --- 条件可选：ONEARMECHO6=FALSE 时可选 --- -#}
        {%- elif item.ONEARMECHO6 == 'FALSE' -%}
            {%- if item.MINRXINT is not none -%}
                MINRXINT={{item.MINRXINT}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：CREATETYPE6=SESS_STATIC 时可选 --- -#}
        {%- if item.CREATETYPE6 == 'SESS_STATIC' -%}
            {%- if item.ONEARMECHO6 is not none -%}
                ONEARMECHO6={{item.ONEARMECHO6}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件必选/可选参数 --- -#}
        {#- --- 出接口名称: 条件必选(IPv4单臂Echo=TRUE; IPv6单臂Echo=TRUE) / 条件可选(IPv4会话创建方式=SESS_AUTO; IPv6会话创建方式=SESS_AUTO; IPv4单臂Echo=FALSE; IPv6单臂Echo=FALSE) --- -#}
        {%- if (item.ONEARMECHO == 'TRUE') or (item.ONEARMECHO6 == 'TRUE') -%}
            IFNAME="{{item.IFNAME}}",
        {%- elif (item.CREATETYPE4 == 'SESS_AUTO') or (item.CREATETYPE6 == 'SESS_AUTO') or (item.ONEARMECHO == 'FALSE') or (item.ONEARMECHO6 == 'FALSE') -%}
            {%- if item.IFNAME is not none -%}
                IFNAME="{{item.IFNAME}}",
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 2.9 采用静态路由+BFD时，配置静态路由并绑定BFD会话。采用BGP over静态路由+BFD时，请跳过该步骤。

##### 2.9.1 //“PREFIX”/“MASKLENGTH”是另一UEG的S6a/N8/N14逻辑接口IP地址及所在网段掩码长度，请根据网设文档替换。

```jinja2
{%- if is_scenario_direct_to_dcgw and is_scenario_static_route_bfd -%}
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
        {%- if item.NEXTHOP is not none -%}
            NEXTHOP="{{item.NEXTHOP}}",
        {%- endif -%}
        {%- if item.SESSIONNAME is not none -%}
            SESSIONNAME="{{item.SESSIONNAME}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_direct_to_dcgw and is_scenario_static_route_bfd -%}
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
        {%- if item.IFNAME is not none -%}
            IFNAME="{{item.IFNAME}}",
        {%- endif -%}
        {%- if item.NEXTHOP is not none -%}
            NEXTHOP="{{item.NEXTHOP}}",
        {%- endif -%}
        {%- if item.SESSIONNAME is not none -%}
            SESSIONNAME="{{item.SESSIONNAME}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 2.10 采用BGP over静态路由+BFD时，配置静态路由并绑定BFD会话。采用静态路由+BFD时，请跳过该步骤。

##### 2.10.1 //“PREFIX”和“MASKLENGTH”是目的IP和掩码（BGP对等体的IP地址和掩码）。

```jinja2
{%- if is_scenario_direct_to_dcgw and is_scenario_bgp_over_static_bfd -%}
    {%- for item in add_srroute_list_2 -%}
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
        {%- if item.NEXTHOP is not none -%}
            NEXTHOP="{{item.NEXTHOP}}",
        {%- endif -%}
        {%- if item.SESSIONNAME is not none -%}
            SESSIONNAME="{{item.SESSIONNAME}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 2.10.2 //对端网元不发布BGP默认路由时，需要配置该步骤。“PREFIX”设置为“0.0.0.0”，“MASKLENGTH”设置为“0”。其他参数与到BGP对等体的路由相同。

```jinja2
{%- if is_scenario_direct_to_dcgw and is_scenario_bgp_over_static_bfd and is_scenario_peer_no_default_route -%}
    {%- for item in add_srroute_list_4 -%}
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
        {%- if item.NEXTHOP is not none -%}
            NEXTHOP="{{item.NEXTHOP}}",
        {%- endif -%}
        {%- if item.SESSIONNAME is not none -%}
            SESSIONNAME="{{item.SESSIONNAME}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 2.10.3 //“PREFIX”和“MASKLENGTH”是目的IP和掩码（BGP对等体的IP地址和掩码）。

```jinja2
{%- if is_scenario_direct_to_dcgw and is_scenario_bgp_over_static_bfd -%}
    {%- for item in add_srroute6_list_2 -%}
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
        {%- if item.IFNAME is not none -%}
            IFNAME="{{item.IFNAME}}",
        {%- endif -%}
        {%- if item.NEXTHOP is not none -%}
            NEXTHOP="{{item.NEXTHOP}}",
        {%- endif -%}
        {%- if item.SESSIONNAME is not none -%}
            SESSIONNAME="{{item.SESSIONNAME}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 2.10.4 //对端网元不发布BGP默认路由时，需要配置该步骤。“PREFIX”设置为“0:0:0:0:0:0:0:0”，“MASKLENGTH”设置为“0”。其他参数与到BGP对等体的路由相同。

```jinja2
{%- if is_scenario_direct_to_dcgw and is_scenario_bgp_over_static_bfd and is_scenario_peer_no_default_route -%}
    {%- for item in add_srroute6_list_4 -%}
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
        {%- if item.IFNAME is not none -%}
            IFNAME="{{item.IFNAME}}",
        {%- endif -%}
        {%- if item.NEXTHOP is not none -%}
            NEXTHOP="{{item.NEXTHOP}}",
        {%- endif -%}
        {%- if item.SESSIONNAME is not none -%}
            SESSIONNAME="{{item.SESSIONNAME}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 3 直连PE时，配置直连口。

### 配置的直连口用于传输UEG间NF互通的报文。例如：传输应急UDM通过N8接口向另一UEG中的应急AMF主动发送的cancel location报文等。

#### 3.1 配置VPN实例。

```jinja2
{%- if is_scenario_direct_to_pe -%}
    {%- for item in add_l3vpninst_list_1 -%}
        ADD L3VPNINST:
        {#- --- 必选参数 --- -#}
        VRFNAME="{{item.VRFNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_direct_to_pe -%}
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
{%- endif -%}
```

#### 3.2 配置外联口IP地址。

##### 3.2.1 配置子接口。

```jinja2
{%- if is_scenario_direct_to_pe -%}
    {%- for item in add_interface_list_3 -%}
        ADD INTERFACE:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 3.2.2 增加接口绑定VPN。

```jinja2
{%- if is_scenario_direct_to_pe -%}
    {%- for item in add_ipbindvpn_list_3 -%}
        ADD IPBINDVPN:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        VRFNAME="{{item.VRFNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 3.2.3 在以太网子接口上关联VLAN ID。

```jinja2
{%- if is_scenario_direct_to_pe -%}
    {%- for item in add_ethsubif_list_2 -%}
        ADD ETHSUBIF:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        VLANTYPEVID={{item.VLANTYPEVID}},
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 3.2.4 配置IPv6使能。

```jinja2
{%- if is_scenario_direct_to_pe -%}
    {%- for item in set_ifipv6enable_list_3 -%}
        SET IFIPV6ENABLE:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        ENABLEFLAG={{item.ENABLEFLAG}},
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 3.2.5 配置外联口IP地址。

```jinja2
{%- if is_scenario_direct_to_pe -%}
    {%- for item in add_ifipv4address_list_3 -%}
        ADD IFIPV4ADDRESS:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        IFIPADDR="{{item.IFIPADDR}}",
        SUBNETMASK="{{item.SUBNETMASK}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_direct_to_pe -%}
    {%- for item in add_ifipv6address_list_3 -%}
        ADD IFIPV6ADDRESS:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        IPV6ADDRESS="{{item.IPV6ADDRESS}}",
        PREFIXLEN={{item.PREFIXLEN}},
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 3.3 新建BFD会话。

```jinja2
{%- if is_scenario_direct_to_pe -%}
    {%- for item in add_bfdsession_list_8 -%}
        ADD BFDSESSION:
        {#- --- 必选参数 --- -#}
        SESSNAME="{{item.SESSNAME}}",
        ADDRTYPE={{item.ADDRTYPE}},
        LINKTYPE={{item.LINKTYPE}},
        {#- --- 可选参数 --- -#}
        {%- if item.DETECTMULTI is not none -%}
            DETECTMULTI={{item.DETECTMULTI}},
        {%- endif -%}
        {%- if item.VRFNAME is not none -%}
            VRFNAME="{{item.VRFNAME}}",
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：ADDRTYPE=IPv4 时必选 --- -#}
        {%- if item.ADDRTYPE == 'IPv4' -%}
            CREATETYPE4={{item.CREATETYPE4}},
        {%- endif -%}
        {#- --- 条件必选：CREATETYPE4=SESS_STATIC 时必选 --- -#}
        {%- if item.CREATETYPE4 == 'SESS_STATIC' -%}
            ONEARMECHO={{item.ONEARMECHO}},
        {%- endif -%}
        {#- --- 条件必选：ADDRTYPE=IPv4 时必选 --- -#}
        {%- if item.ADDRTYPE == 'IPv4' -%}
            DESTADDR4="{{item.DESTADDR4}}",
        {%- endif -%}
        {#- --- 条件必选：CREATETYPE4=SESS_STATIC 时必选 --- -#}
        {%- if item.CREATETYPE4 == 'SESS_STATIC' -%}
            LOCALDISCR={{item.LOCALDISCR}},
        {#- --- 条件必选：CREATETYPE6=SESS_STATIC 时必选 --- -#}
        {%- elif item.CREATETYPE6 == 'SESS_STATIC' -%}
            LOCALDISCR={{item.LOCALDISCR}},
        {%- endif -%}
        {#- --- 条件必选：ADDRTYPE=IPv6 时必选 --- -#}
        {%- if item.ADDRTYPE == 'IPv6' -%}
            CREATETYPE6={{item.CREATETYPE6}},
        {%- endif -%}
        {#- --- 条件必选：ADDRTYPE=IPv6 时必选 --- -#}
        {%- if item.ADDRTYPE == 'IPv6' -%}
            DESTADDR6="{{item.DESTADDR6}}",
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：ONEARMECHO=TRUE 时可选 --- -#}
        {%- if item.ONEARMECHO == 'TRUE' -%}
            {%- if item.MINECHORXINT is not none -%}
                MINECHORXINT={{item.MINECHORXINT}},
            {%- endif -%}
        {#- --- 条件可选：ONEARMECHO6=TRUE 时可选 --- -#}
        {%- elif item.ONEARMECHO6 == 'TRUE' -%}
            {%- if item.MINECHORXINT is not none -%}
                MINECHORXINT={{item.MINECHORXINT}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：CREATETYPE6=SESS_STATIC 时可选 --- -#}
        {%- if item.CREATETYPE6 == 'SESS_STATIC' -%}
            {%- if item.ONEARMECHO6 is not none -%}
                ONEARMECHO6={{item.ONEARMECHO6}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件必选/可选参数 --- -#}
        {#- --- 出接口名称: 条件必选(IPv4单臂Echo=TRUE; IPv6单臂Echo=TRUE) / 条件可选(IPv4会话创建方式=SESS_AUTO; IPv6会话创建方式=SESS_AUTO; IPv4单臂Echo=FALSE; IPv6单臂Echo=FALSE) --- -#}
        {%- if (item.ONEARMECHO == 'TRUE') or (item.ONEARMECHO6 == 'TRUE') -%}
            IFNAME="{{item.IFNAME}}",
        {%- elif (item.CREATETYPE4 == 'SESS_AUTO') or (item.CREATETYPE6 == 'SESS_AUTO') or (item.ONEARMECHO == 'FALSE') or (item.ONEARMECHO6 == 'FALSE') -%}
            {%- if item.IFNAME is not none -%}
                IFNAME="{{item.IFNAME}}",
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 3.4 配置静态路由并绑定BFD会话。

##### 3.4.1 //“PREFIX”/“MASKLENGTH”是另一UEG的S6a/N8/N14逻辑接口IP及所在网段掩码长度，请根据网设文档替换。

```jinja2
{%- if is_scenario_direct_to_pe -%}
    {%- for item in add_srroute_list_6 -%}
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
        {%- if item.NEXTHOP is not none -%}
            NEXTHOP="{{item.NEXTHOP}}",
        {%- endif -%}
        {%- if item.SESSIONNAME is not none -%}
            SESSIONNAME="{{item.SESSIONNAME}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_direct_to_pe -%}
    {%- for item in add_srroute6_list_6 -%}
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
        {%- if item.IFNAME is not none -%}
            IFNAME="{{item.IFNAME}}",
        {%- endif -%}
        {%- if item.NEXTHOP is not none -%}
            NEXTHOP="{{item.NEXTHOP}}",
        {%- endif -%}
        {%- if item.SESSIONNAME is not none -%}
            SESSIONNAME="{{item.SESSIONNAME}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 4 园区内部署AAA服务器进行二次鉴权时，配置SMF与园区AAA服务器互通的外联口IP和路由数据。

#### 4.1 配置VPN实例。

```jinja2
{%- if is_scenario_aaa_secondary_auth -%}
    {%- for item in add_l3vpninst_list_2 -%}
        ADD L3VPNINST:
        {#- --- 必选参数 --- -#}
        VRFNAME="{{item.VRFNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_aaa_secondary_auth -%}
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
{%- endif -%}
```

#### 4.2 配置Loopback接口IP。用于建立BGP邻居。

```jinja2
{%- if is_scenario_aaa_secondary_auth -%}
    {%- for item in add_interface_list_4 -%}
        ADD INTERFACE:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_aaa_secondary_auth -%}
    {%- for item in add_ipbindvpn_list_4 -%}
        ADD IPBINDVPN:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        VRFNAME="{{item.VRFNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_aaa_secondary_auth -%}
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
{%- endif -%}
```

```jinja2
{%- if is_scenario_aaa_secondary_auth -%}
    {%- for item in set_ifipv6enable_list_4 -%}
        SET IFIPV6ENABLE:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        ENABLEFLAG={{item.ENABLEFLAG}},
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_aaa_secondary_auth -%}
    {%- for item in add_ifipv6address_list_4 -%}
        ADD IFIPV6ADDRESS:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        IPV6ADDRESS="{{item.IPV6ADDRESS}}",
        PREFIXLEN={{item.PREFIXLEN}},
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 4.3 配置BGP VPN实例。

```jinja2
{%- if is_scenario_aaa_secondary_auth -%}
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
{%- endif -%}
```

#### 4.4 增加BGP VPN实例地址族。UEG对接2个负荷分担的BGP PEER时，“MAXIMUMLOADBALANCE”设置为“2”。

```jinja2
{%- if is_scenario_aaa_secondary_auth -%}
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
{%- endif -%}
```

#### 4.5 配置BGP对等体。此处以对接2个IPv4v6双栈的BGP对等体为例。

```jinja2
{%- if is_scenario_aaa_secondary_auth -%}
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
{%- endif -%}
```

#### 4.6 配置BGP引入wlr路由。

```jinja2
{%- if is_scenario_aaa_secondary_auth -%}
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
{%- endif -%}
```

#### 4.7 配置外联口IP地址。

##### 4.7.1 添加以太网子接口。

```jinja2
{%- if is_scenario_aaa_secondary_auth -%}
    {%- for item in add_interface_list_5 -%}
        ADD INTERFACE:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 4.7.2 增加接口绑定VPN。

```jinja2
{%- if is_scenario_aaa_secondary_auth -%}
    {%- for item in add_ipbindvpn_list_5 -%}
        ADD IPBINDVPN:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        VRFNAME="{{item.VRFNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 4.7.3 在以太网子接口上关联VLAN ID。

```jinja2
{%- if is_scenario_aaa_secondary_auth -%}
    {%- for item in add_ethsubif_list_3 -%}
        ADD ETHSUBIF:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        VLANTYPEVID={{item.VLANTYPEVID}},
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 4.7.4 配置IPv6使能。

```jinja2
{%- if is_scenario_aaa_secondary_auth -%}
    {%- for item in set_ifipv6enable_list_5 -%}
        SET IFIPV6ENABLE:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        ENABLEFLAG={{item.ENABLEFLAG}},
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 4.7.5 配置外联口IP地址。

```jinja2
{%- if is_scenario_aaa_secondary_auth -%}
    {%- for item in add_ifipv4address_list_5 -%}
        ADD IFIPV4ADDRESS:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        IFIPADDR="{{item.IFIPADDR}}",
        SUBNETMASK="{{item.SUBNETMASK}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_aaa_secondary_auth -%}
    {%- for item in add_ifipv6address_list_5 -%}
        ADD IFIPV6ADDRESS:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        IPV6ADDRESS="{{item.IPV6ADDRESS}}",
        PREFIXLEN={{item.PREFIXLEN}},
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 4.8 新建BFD会话。

##### 4.8.1 //配置双向BFD探测。

```jinja2
{%- if is_scenario_aaa_secondary_auth and is_scenario_bfd_bidirectional -%}
    {%- for item in add_bfdsession_list_10 -%}
        ADD BFDSESSION:
        {#- --- 必选参数 --- -#}
        SESSNAME="{{item.SESSNAME}}",
        ADDRTYPE={{item.ADDRTYPE}},
        LINKTYPE={{item.LINKTYPE}},
        {#- --- 可选参数 --- -#}
        {%- if item.DETECTMULTI is not none -%}
            DETECTMULTI={{item.DETECTMULTI}},
        {%- endif -%}
        {%- if item.VRFNAME is not none -%}
            VRFNAME="{{item.VRFNAME}}",
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：ADDRTYPE=IPv4 时必选 --- -#}
        {%- if item.ADDRTYPE == 'IPv4' -%}
            CREATETYPE4={{item.CREATETYPE4}},
        {%- endif -%}
        {#- --- 条件必选：CREATETYPE4=SESS_STATIC 时必选 --- -#}
        {%- if item.CREATETYPE4 == 'SESS_STATIC' -%}
            ONEARMECHO={{item.ONEARMECHO}},
        {%- endif -%}
        {#- --- 条件必选：ADDRTYPE=IPv4 时必选 --- -#}
        {%- if item.ADDRTYPE == 'IPv4' -%}
            DESTADDR4="{{item.DESTADDR4}}",
        {%- endif -%}
        {#- --- 条件必选：CREATETYPE4=SESS_STATIC 时必选 --- -#}
        {%- if item.CREATETYPE4 == 'SESS_STATIC' -%}
            LOCALDISCR={{item.LOCALDISCR}},
        {#- --- 条件必选：CREATETYPE6=SESS_STATIC 时必选 --- -#}
        {%- elif item.CREATETYPE6 == 'SESS_STATIC' -%}
            LOCALDISCR={{item.LOCALDISCR}},
        {%- endif -%}
        {#- --- 条件必选：ONEARMECHO=FALSE 时必选 --- -#}
        {%- if item.ONEARMECHO == 'FALSE' -%}
            REMOTEDISCR={{item.REMOTEDISCR}},
        {#- --- 条件必选：ONEARMECHO6=FALSE 时必选 --- -#}
        {%- elif item.ONEARMECHO6 == 'FALSE' -%}
            REMOTEDISCR={{item.REMOTEDISCR}},
        {%- endif -%}
        {#- --- 条件必选：ADDRTYPE=IPv6 时必选 --- -#}
        {%- if item.ADDRTYPE == 'IPv6' -%}
            CREATETYPE6={{item.CREATETYPE6}},
        {%- endif -%}
        {#- --- 条件必选：ADDRTYPE=IPv6 时必选 --- -#}
        {%- if item.ADDRTYPE == 'IPv6' -%}
            DESTADDR6="{{item.DESTADDR6}}",
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：CREATETYPE4=SESS_AUTO 时可选 --- -#}
        {%- if item.CREATETYPE4 == 'SESS_AUTO' -%}
            {%- if item.MINTXINT is not none -%}
                MINTXINT={{item.MINTXINT}},
            {%- endif -%}
        {#- --- 条件可选：CREATETYPE6=SESS_AUTO 时可选 --- -#}
        {%- elif item.CREATETYPE6 == 'SESS_AUTO' -%}
            {%- if item.MINTXINT is not none -%}
                MINTXINT={{item.MINTXINT}},
            {%- endif -%}
        {#- --- 条件可选：ONEARMECHO=FALSE 时可选 --- -#}
        {%- elif item.ONEARMECHO == 'FALSE' -%}
            {%- if item.MINTXINT is not none -%}
                MINTXINT={{item.MINTXINT}},
            {%- endif -%}
        {#- --- 条件可选：ONEARMECHO6=FALSE 时可选 --- -#}
        {%- elif item.ONEARMECHO6 == 'FALSE' -%}
            {%- if item.MINTXINT is not none -%}
                MINTXINT={{item.MINTXINT}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：CREATETYPE4=SESS_AUTO 时可选 --- -#}
        {%- if item.CREATETYPE4 == 'SESS_AUTO' -%}
            {%- if item.MINRXINT is not none -%}
                MINRXINT={{item.MINRXINT}},
            {%- endif -%}
        {#- --- 条件可选：CREATETYPE6=SESS_AUTO 时可选 --- -#}
        {%- elif item.CREATETYPE6 == 'SESS_AUTO' -%}
            {%- if item.MINRXINT is not none -%}
                MINRXINT={{item.MINRXINT}},
            {%- endif -%}
        {#- --- 条件可选：ONEARMECHO=FALSE 时可选 --- -#}
        {%- elif item.ONEARMECHO == 'FALSE' -%}
            {%- if item.MINRXINT is not none -%}
                MINRXINT={{item.MINRXINT}},
            {%- endif -%}
        {#- --- 条件可选：ONEARMECHO6=FALSE 时可选 --- -#}
        {%- elif item.ONEARMECHO6 == 'FALSE' -%}
            {%- if item.MINRXINT is not none -%}
                MINRXINT={{item.MINRXINT}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：CREATETYPE6=SESS_STATIC 时可选 --- -#}
        {%- if item.CREATETYPE6 == 'SESS_STATIC' -%}
            {%- if item.ONEARMECHO6 is not none -%}
                ONEARMECHO6={{item.ONEARMECHO6}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件必选/可选参数 --- -#}
        {#- --- 出接口名称: 条件必选(IPv4单臂Echo=TRUE; IPv6单臂Echo=TRUE) / 条件可选(IPv4会话创建方式=SESS_AUTO; IPv6会话创建方式=SESS_AUTO; IPv4单臂Echo=FALSE; IPv6单臂Echo=FALSE) --- -#}
        {%- if (item.ONEARMECHO == 'TRUE') or (item.ONEARMECHO6 == 'TRUE') -%}
            IFNAME="{{item.IFNAME}}",
        {%- elif (item.CREATETYPE4 == 'SESS_AUTO') or (item.CREATETYPE6 == 'SESS_AUTO') or (item.ONEARMECHO == 'FALSE') or (item.ONEARMECHO6 == 'FALSE') -%}
            {%- if item.IFNAME is not none -%}
                IFNAME="{{item.IFNAME}}",
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 4.8.2 //配置BFD单臂echo探测。

```jinja2
{%- if is_scenario_aaa_secondary_auth and is_scenario_bfd_onearm_echo -%}
    {%- for item in add_bfdsession_list_14 -%}
        ADD BFDSESSION:
        {#- --- 必选参数 --- -#}
        SESSNAME="{{item.SESSNAME}}",
        ADDRTYPE={{item.ADDRTYPE}},
        LINKTYPE={{item.LINKTYPE}},
        {#- --- 可选参数 --- -#}
        {%- if item.DETECTMULTI is not none -%}
            DETECTMULTI={{item.DETECTMULTI}},
        {%- endif -%}
        {%- if item.VRFNAME is not none -%}
            VRFNAME="{{item.VRFNAME}}",
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：ADDRTYPE=IPv4 时必选 --- -#}
        {%- if item.ADDRTYPE == 'IPv4' -%}
            CREATETYPE4={{item.CREATETYPE4}},
        {%- endif -%}
        {#- --- 条件必选：CREATETYPE4=SESS_STATIC 时必选 --- -#}
        {%- if item.CREATETYPE4 == 'SESS_STATIC' -%}
            ONEARMECHO={{item.ONEARMECHO}},
        {%- endif -%}
        {#- --- 条件必选：ADDRTYPE=IPv4 时必选 --- -#}
        {%- if item.ADDRTYPE == 'IPv4' -%}
            DESTADDR4="{{item.DESTADDR4}}",
        {%- endif -%}
        {#- --- 条件必选：CREATETYPE4=SESS_STATIC 时必选 --- -#}
        {%- if item.CREATETYPE4 == 'SESS_STATIC' -%}
            LOCALDISCR={{item.LOCALDISCR}},
        {#- --- 条件必选：CREATETYPE6=SESS_STATIC 时必选 --- -#}
        {%- elif item.CREATETYPE6 == 'SESS_STATIC' -%}
            LOCALDISCR={{item.LOCALDISCR}},
        {%- endif -%}
        {#- --- 条件必选：ADDRTYPE=IPv6 时必选 --- -#}
        {%- if item.ADDRTYPE == 'IPv6' -%}
            CREATETYPE6={{item.CREATETYPE6}},
        {%- endif -%}
        {#- --- 条件必选：ADDRTYPE=IPv6 时必选 --- -#}
        {%- if item.ADDRTYPE == 'IPv6' -%}
            DESTADDR6="{{item.DESTADDR6}}",
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：ONEARMECHO=TRUE 时可选 --- -#}
        {%- if item.ONEARMECHO == 'TRUE' -%}
            {%- if item.MINECHORXINT is not none -%}
                MINECHORXINT={{item.MINECHORXINT}},
            {%- endif -%}
        {#- --- 条件可选：ONEARMECHO6=TRUE 时可选 --- -#}
        {%- elif item.ONEARMECHO6 == 'TRUE' -%}
            {%- if item.MINECHORXINT is not none -%}
                MINECHORXINT={{item.MINECHORXINT}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：CREATETYPE6=SESS_STATIC 时可选 --- -#}
        {%- if item.CREATETYPE6 == 'SESS_STATIC' -%}
            {%- if item.ONEARMECHO6 is not none -%}
                ONEARMECHO6={{item.ONEARMECHO6}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件必选/可选参数 --- -#}
        {#- --- 出接口名称: 条件必选(IPv4单臂Echo=TRUE; IPv6单臂Echo=TRUE) / 条件可选(IPv4会话创建方式=SESS_AUTO; IPv6会话创建方式=SESS_AUTO; IPv4单臂Echo=FALSE; IPv6单臂Echo=FALSE) --- -#}
        {%- if (item.ONEARMECHO == 'TRUE') or (item.ONEARMECHO6 == 'TRUE') -%}
            IFNAME="{{item.IFNAME}}",
        {%- elif (item.CREATETYPE4 == 'SESS_AUTO') or (item.CREATETYPE6 == 'SESS_AUTO') or (item.ONEARMECHO == 'FALSE') or (item.ONEARMECHO6 == 'FALSE') -%}
            {%- if item.IFNAME is not none -%}
                IFNAME="{{item.IFNAME}}",
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 4.9 采用静态路由+BFD时，配置静态路由并绑定BFD会话。采用BGP over静态路由+BFD时，请跳过该步骤。

#### 直连PE时，根据PE能力选择使用“BGP over静态路由+BFD”或“静态路由+BFD”。

#### 直连DCGW时，推荐采用“BGP over静态路由+BFD”。

##### 4.9.1 //“PREFIX”/“MASKLENGTH”是园区服务器的IP地址及所在网段掩码长度，请根据网设文档替换。

```jinja2
{%- if is_scenario_aaa_secondary_auth and is_scenario_static_route_bfd -%}
    {%- for item in add_srroute_list_7 -%}
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
        {%- if item.NEXTHOP is not none -%}
            NEXTHOP="{{item.NEXTHOP}}",
        {%- endif -%}
        {%- if item.SESSIONNAME is not none -%}
            SESSIONNAME="{{item.SESSIONNAME}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_aaa_secondary_auth and is_scenario_static_route_bfd -%}
    {%- for item in add_srroute6_list_7 -%}
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
        {%- if item.IFNAME is not none -%}
            IFNAME="{{item.IFNAME}}",
        {%- endif -%}
        {%- if item.NEXTHOP is not none -%}
            NEXTHOP="{{item.NEXTHOP}}",
        {%- endif -%}
        {%- if item.SESSIONNAME is not none -%}
            SESSIONNAME="{{item.SESSIONNAME}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 4.10 采用BGP over静态路由+BFD时，配置静态路由并绑定BFD会话。采用静态路由+BFD时，请跳过该步骤。

##### 4.10.1 //“PREFIX”和“MASKLENGTH”是目的IP和掩码（BGP对等体的IP地址和掩码）。

```jinja2
{%- if is_scenario_aaa_secondary_auth and is_scenario_bgp_over_static_bfd -%}
    {%- for item in add_srroute_list_9 -%}
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
        {%- if item.NEXTHOP is not none -%}
            NEXTHOP="{{item.NEXTHOP}}",
        {%- endif -%}
        {%- if item.SESSIONNAME is not none -%}
            SESSIONNAME="{{item.SESSIONNAME}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 4.10.2 //对端网元不发布BGP默认路由时，需要配置该步骤。“PREFIX”设置为“0.0.0.0”，“MASKLENGTH”设置为“0”。其他参数与到BGP对等体的路由相同。

```jinja2
{%- if is_scenario_aaa_secondary_auth and is_scenario_bgp_over_static_bfd and is_scenario_peer_no_default_route -%}
    {%- for item in add_srroute_list_11 -%}
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
        {%- if item.NEXTHOP is not none -%}
            NEXTHOP="{{item.NEXTHOP}}",
        {%- endif -%}
        {%- if item.SESSIONNAME is not none -%}
            SESSIONNAME="{{item.SESSIONNAME}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 4.10.3 //“PREFIX”和“MASKLENGTH”是目的IP和掩码（BGP对等体的IP地址和掩码）。

```jinja2
{%- if is_scenario_aaa_secondary_auth and is_scenario_bgp_over_static_bfd -%}
    {%- for item in add_srroute6_list_9 -%}
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
        {%- if item.IFNAME is not none -%}
            IFNAME="{{item.IFNAME}}",
        {%- endif -%}
        {%- if item.NEXTHOP is not none -%}
            NEXTHOP="{{item.NEXTHOP}}",
        {%- endif -%}
        {%- if item.SESSIONNAME is not none -%}
            SESSIONNAME="{{item.SESSIONNAME}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 4.10.4 //对端网元不发布BGP默认路由时，需要配置该步骤。“PREFIX”设置为“0:0:0:0:0:0:0:0”，“MASKLENGTH”设置为“0”。其他参数与到BGP对等体的路由相同。

```jinja2
{%- if is_scenario_aaa_secondary_auth and is_scenario_bgp_over_static_bfd and is_scenario_peer_no_default_route -%}
    {%- for item in add_srroute6_list_11 -%}
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
        {%- if item.IFNAME is not none -%}
            IFNAME="{{item.IFNAME}}",
        {%- endif -%}
        {%- if item.NEXTHOP is not none -%}
            NEXTHOP="{{item.NEXTHOP}}",
        {%- endif -%}
        {%- if item.SESSIONNAME is not none -%}
            SESSIONNAME="{{item.SESSIONNAME}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 5 配置应急AMF和应急SMF的业务数据。

### **表3** 应急AMF和应急SMF的业务数据

### | 配置项目 | 配置参考 | 容灾说明 |

### | --- | --- | --- |

### | 配置应急AMF和应急SMF的公共数据 | 公共参数配置（应急AMF/SMF） | 容灾与非容灾场景配置没有区别。 |

### | 配置应急AMF与gNodeB的对接数据 | 配置N2接口数据 | 容灾与非容灾场景，两台高可用边缘网关的N2接口业务IP不能相同，其他配置没有区别。 |

### | 配置应急AMF与应急AUSF、应急UDM、应急SMF的对接数据 | 配置AMF服务化接口数据（N8/N11/N12） | 选择同一高可用边缘网关内的应急AUSF、应急UDM、应急SMF，容灾与非容灾场景配置没有区别。 |

### | 配置应急SMF与UPF的对接数据 | 配置N4接口数据 | 容灾场景，应急SMF选择同一高可用边缘网关内的UPF。 |

### | 配置应急SMF与应急AMF、应急UDM的对接数据 | 配置SMF服务化接口数据（N10/N11/N7） | 选择同一高可用边缘网关内的应急AMF、应急UDM，容灾与非容灾场景配置没有区别。 |

### | 配置应急SMF与园区AAA服务器的对接数据 | 配置Gi接口数据 | 园区部署两台高可用边缘网关场景，两个应急SMF分别与园区AAA服务器互通，两个高可用边缘网关的Gi接口业务IP不能相同。 |


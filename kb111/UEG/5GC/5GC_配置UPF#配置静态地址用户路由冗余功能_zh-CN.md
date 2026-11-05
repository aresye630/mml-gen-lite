---
id: ''
name: 配置静态地址用户路由冗余功能
ne_type: UEG
type: feature
description: '**对于风筝M/风筝L**：  两套UEG间采用负荷分担模式容灾场景，终端采用静态签约的IP时，需要在园区的两个UPF之间部署静态地址用户路由冗余功能，保证两个UPF都正常时，SGi/N6侧发布低优先级路由的UPF上激活的用户业务连续。  对于风筝M/风筝L，配置举例如图1所示。  **图1** 静态地址路由冗余GRE数据规划图'
tags: []
risk_level: ''
doc_source: ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（火电专网，入驻式）","部署配置指导","子园区部署入驻式UEG-M","初始配置与调测","配置实例（裸机容器）","配置UPF","配置静态地址用户路由冗余功能"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
**对于风筝M/风筝L**：两套UEG间采用负荷分担模式容灾场景，终端采用静态签约的IP时，需要在园区的两个UPF之间部署静态地址用户路由冗余功能，保证两个UPF都正常时，SGi/N6侧发布低优先级路由的UPF上激活的用户业务连续。对于风筝M/风筝L，配置举例如图1所示。**图1** 静态地址路由冗余GRE数据规划图

## 必备事项
前提条件

前提条件

* 具备管理员权限的操作人员已经登录华为操作维护系统（登录MAE客户端或登录OM Portal）。
* VNF与网络实体之间的网络环境已经构建完成。
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
    add_networkroute_list:
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
        NETWORKADDRESS:
          name: 'IPv4路由前缀地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MASKLEN:
          name: 'IPv4掩码长度'
          type: integer
          minimum: 0
          maximum: 32
          required: false
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
    add_bfdsession_list_2:
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
    add_redundrdtip_list:
      type: items
      properties:
        IPVERSION:
          name: 'IP版本'
          type: string
          enum:
          - IPv4
          - IPv6
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV4ADDRESS:
          name: 'IPV4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6ADDRESS:
          name: 'IPV6地址'
          type: string
          maxLength: 39
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
        DSTVPNNAME:
          name: '目的VPN名称'
          type: string
          maxLength: 31
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
        GREKEY:
          name: '识别关键字'
          type: string
          maxLength: 268
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        REDUNDANCYEN:
          name: '使能备份隧道功能'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
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
        IFNAME:
          name: '路由出接口名字'
          type: string
          maxLength: 63
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
        IFNAME:
          name: '路由出接口名字'
          type: string
          maxLength: 63
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_redunduser_list:
      type: items
      properties:
        SWITCH:
          name: '开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    mod_uppool_list:
      type: items
      properties:
        POOLNAME:
          name: '地址池名称'
          type: string
          minLength: 1
          maxLength: 79
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        POOLTYPE:
          name: '地址池类型'
          type: string
          enum:
          - EXTERNAL
          - LOCAL
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        REDUNDFUNC:
          name: '冗余备份功能开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_apnredundupsw_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV4SWITCH:
          name: 'APN支持IPV4上行转发功能'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6SWITCH:
          name: 'APN支持IPV6上行转发功能'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_licenseswitch_list:
      type: items
      properties:
        LICITEM:
          name: 'License项'
          type: string
          minLength: 0
          maxLength: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SWITCH:
          name: '开关'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_cpteidualloc_list:
      type: items
      properties:
        SWITCH:
          name: '开关标识'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    add_l3vpninst_list:
    - VRFNAME: 'VRF_Redundancy'
    add_vpninstaf_list:
    - VRFNAME: 'VRF_Redundancy'
      AFTYPE: ipv4uni
      VRFRD: '192.168.225.150:100'
    add_interface_list:
    - IFNAME: 'LoopBack100'
    add_ipbindvpn_list:
    - IFNAME: 'LoopBack100'
      VRFNAME: 'VRF_Redundancy'
    add_ifipv4address_list:
    - IFNAME: 'LoopBack100'
      IFIPADDR: '192.168.225.150'
      SUBNETMASK: '255.255.255.255'
      ADDRTYPE: main
    add_bgpvrf_list:
    - VRFNAME: 'VRF_Redundancy'
      DEFAULTAFTYPE: noaf
      ROUTERID: '192.168.225.150'
    add_bgpvrfaf_list:
    - VRFNAME: 'VRF_Redundancy'
      AFTYPE: ipv4uni
      MAXIMUMLOADBALANCE: 2
    add_bgppeer_list:
    - VRFNAME: 'VRF_Redundancy'
      ADDRESSTYPE: ipv4
      PEERADDR: '192.168.79.20'
      REMOTEAS: '60002'
      LOCALIFADDR: '192.168.225.150'
      LOCALIFNAME: 'Loopback100'
      EBGPMAXHOP: 10
    add_networkroute_list:
    - VRFNAME: 'VRF_Redundancy'
      AFTYPE: ipv4uni
      NETWORKADDRESS: '10.11.1.1'
      MASKLEN: 32
    mod_interface_list:
    - IFNAME: 'Ethernet64/0/6'
      IFADMINSTATUS: up
    add_interface_list_1:
    - IFNAME: 'Ethernet64/0/6.2'
    add_ipbindvpn_list_1:
    - IFNAME: 'Ethernet64/0/6.2'
      VRFNAME: 'VRF_Redundancy'
    add_ethsubif_list:
    - IFNAME: 'Ethernet64/0/6.2'
      VLANTYPEVID: 2100
    add_ifipv4address_list_1:
    - IFNAME: 'Ethernet64/0/6.2'
      IFIPADDR: '192.168.100.2'
      SUBNETMASK: '255.255.255.248'
    add_bfdsession_list:
    - SESSNAME: 'BfdName1001_v4'
      ADDRTYPE: IPv4
      CREATETYPE4: SESS_STATIC
      ONEARMECHO: FALSE
      DESTADDR4: '192.168.100.1'
      LINKTYPE: IP
      MINTXINT: 500
      MINRXINT: 500
      DETECTMULTI: 4
      VRFNAME: 'VRF_Redundancy'
      LOCALDISCR: 10041
      REMOTEDISCR: 10042
      IFNAME: 'Ethernet64/0/6.2'
      ONEARMECHO6: FALSE
      CREATETYPE6: ''
    add_bfdsession_list_2:
    - SESSNAME: 'BfdName1001_v4'
      ADDRTYPE: IPv4
      CREATETYPE4: SESS_STATIC
      ONEARMECHO: TRUE
      DESTADDR4: '192.168.100.1'
      LINKTYPE: IP
      DETECTMULTI: 4
      VRFNAME: 'VRF_Redundancy'
      MINECHORXINT: 500
      LOCALDISCR: 10041
      IFNAME: 'Ethernet64/0/6.2'
      ONEARMECHO6: FALSE
      CREATETYPE6: ''
    add_srroute_list:
    - AFTYPE: ipv4unicast
      PREFIX: '10.10.0.1'
      MASKLENGTH: 32
      VRFNAME: 'VRF_Redundancy'
      DESTVRFNAME: 'VRF_Redundancy'
      IFNAME: 'Ethernet64/0/6.2'
      NEXTHOP: '192.168.100.1'
      SESSIONNAME: 'BfdName1001_v4'
    add_srroute_list_2:
    - AFTYPE: ipv4unicast
      PREFIX: '192.168.79.20'
      MASKLENGTH: 32
      VRFNAME: 'VRF_Redundancy'
      DESTVRFNAME: 'VRF_Redundancy'
      IFNAME: 'Ethernet64/0/6.2'
      NEXTHOP: '192.168.100.1'
      SESSIONNAME: 'BfdName1001_v4'
    add_interface_list_3:
    - IFNAME: 'LoopBack10'
    add_ipbindvpn_list_3:
    - IFNAME: 'LoopBack10'
      VRFNAME: 'VRF_Redundancy'
    add_ifipv4address_list_3:
    - IFNAME: 'LoopBack10'
      IFIPADDR: '10.11.1.1'
      SUBNETMASK: '255.255.255.255'
      ADDRTYPE: main
    add_redundrdtip_list:
    - IPVERSION: IPv4
      IPV4ADDRESS: '192.168.0.1'
      IPV6ADDRESS: 'fc00:3::1'
    add_interface_list_4:
    - IFNAME: 'Tunnel1'
      IFMTU: 1500
    add_gretunnel_list:
    - TNLNAME: 'Tunnel1'
      SRCTYPE: if_name
      DSTIPADDR: '10.10.0.1'
      TNLTYPE: gre
      SRCIFNAME: 'LoopBack10'
      DSTVPNNAME: 'VRF_Redundancy'
      GREKEYEN: TRUE
      GREKEY: '200'
      REDUNDANCYEN: TRUE
      KEEPALVEN: TRUE
      SRCTYPE6: no_type
    add_ipbindvpn_list_4:
    - IFNAME: 'Tunnel1'
      VRFNAME: 'VRF_LocalDN'
    add_ifipv4address_list_4:
    - IFNAME: 'Tunnel1'
      IFIPADDR: '10.11.1.3'
      SUBNETMASK: '255.255.255.0'
    set_ifipv6enable_list:
    - IFNAME: 'Tunnel1'
      ENABLEFLAG: TRUE
      MTU: 1500
    add_ifipv6address_list:
    - IFNAME: 'Tunnel1'
      IPV6ADDRESS: 'fc00:2::1'
      PREFIXLEN: 64
    add_srroute_list_4:
    - AFTYPE: ipv4unicast
      PREFIX: '192.168.0.1'
      MASKLENGTH: 32
      VRFNAME: 'VRF_LocalDN'
      IFNAME: 'Tunnel1'
    add_srroute6_list:
    - AFTYPE: ipv6unicast
      PREFIX: 'fc00:3::1'
      MASKLENGTH: 128
      VRFNAME: 'VRF_LocalDN'
      IFNAME: 'Tunnel1'
    set_redunduser_list:
    - SWITCH: ENABLE
    mod_uppool_list:
    - POOLNAME: 'pool_ipv4_APN1'
      POOLTYPE: EXTERNAL
      REDUNDFUNC: ENABLE
    set_apnredundupsw_list:
    - APN: 'apn-op1'
      IPV4SWITCH: ENABLE
      IPV6SWITCH: ENABLE
    set_licenseswitch_list:
    - LICITEM: 'LKV3G5CUFM01'
      SWITCH: ENABLE
    set_cpteidualloc_list:
    - SWITCH: DISABLE
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 配置主UPF到备UPF的IP路由数据。

### 此处以配置主UPF为例。备UPF的配置与主UPF的配置过程相同，仅数据不同，请替换成实际规划的数据。

#### 1.1 配置VPN实例。

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

#### 步骤1.b~步骤1.f是BGP相关数据，仅采用BGP over静态路由+BFD时需要配置。采用静态路由+BFD时不需要配置。

#### 1.2 配置Loopback接口IP。用于建立BGP邻居。

```jinja2
{%- if is_scenario_bgp_over_static_route_bfd -%}
    {%- for item in add_interface_list -%}
        ADD INTERFACE:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_bgp_over_static_route_bfd -%}
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
{%- if is_scenario_bgp_over_static_route_bfd -%}
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

#### 1.3 配置BGP VPN实例。

```jinja2
{%- if is_scenario_bgp_over_static_route_bfd -%}
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

#### 1.4 增加BGP VPN实例地址族。UEG对接2个负荷分担的BGP PEER时，“MAXIMUMLOADBALANCE”设置为“2”。

```jinja2
{%- if is_scenario_bgp_over_static_route_bfd -%}
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

#### 1.5 配置BGP对等体。此处以对接2个BGP对等体为例。

```jinja2
{%- if is_scenario_bgp_over_static_route_bfd -%}
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

#### 1.6 配置BGP引入到10.11.1.1的IP路由，即对外发布到Tunnel隧道的源接口IP的路由。

```jinja2
{%- if is_scenario_bgp_over_static_route_bfd -%}
    {%- for item in add_networkroute_list -%}
        ADD NETWORKROUTE:
        {#- --- 必选参数 --- -#}
        AFTYPE={{item.AFTYPE}},
        {#- --- 可选参数 --- -#}
        {%- if item.VRFNAME is not none -%}
            VRFNAME="{{item.VRFNAME}}",
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：AFTYPE=ipv4uni 时必选 --- -#}
        {%- if item.AFTYPE == 'ipv4uni' -%}
            NETWORKADDRESS="{{item.NETWORKADDRESS}}",
        {%- endif -%}
        {#- --- 条件必选：AFTYPE=ipv4uni 时必选 --- -#}
        {%- if item.AFTYPE == 'ipv4uni' -%}
            MASKLEN={{item.MASKLEN}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 对于风筝L：N6外联口使用的是以太网子接口。

#### 1.7 配置外联口IP地址。

##### 1.7.1 查询接口名，确认可使用的外联口的接口类型和接口编号。

##### 1.7.2 配置主接口的管理状态为up。将网设规划的接口的管理状态设置为up。

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

##### 1.7.3 添加以太网子接口。

```jinja2
{%- for item in add_interface_list_1 -%}
    ADD INTERFACE:
    {#- --- 必选参数 --- -#}
    IFNAME="{{item.IFNAME}}",
    ;
{%- endfor -%}
```

##### 1.7.4 增加接口绑定VPN。

```jinja2
{%- for item in add_ipbindvpn_list_1 -%}
    ADD IPBINDVPN:
    {#- --- 必选参数 --- -#}
    IFNAME="{{item.IFNAME}}",
    VRFNAME="{{item.VRFNAME}}",
    ;
{%- endfor -%}
```

##### 1.7.5 在以太网子接口上关联VLAN ID。

```jinja2
{%- for item in add_ethsubif_list -%}
    ADD ETHSUBIF:
    {#- --- 必选参数 --- -#}
    IFNAME="{{item.IFNAME}}",
    VLANTYPEVID={{item.VLANTYPEVID}},
    ;
{%- endfor -%}
```

##### 1.7.6 配置外联口IP地址。

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

#### 1.8 新建BFD会话。

##### 1.8.1 //配置双向BFD探测。

```jinja2
{%- if is_scenario_bidirectional_bfd -%}
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
        {#- --- 条件必选：ONEARMECHO=FALSE 时必选 --- -#}
        {%- if item.ONEARMECHO == 'FALSE' -%}
            REMOTEDISCR={{item.REMOTEDISCR}},
        {#- --- 条件必选：ONEARMECHO6=FALSE 时必选 --- -#}
        {%- elif item.ONEARMECHO6 == 'FALSE' -%}
            REMOTEDISCR={{item.REMOTEDISCR}},
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

##### 1.8.2 //配置BFD单臂echo探测。

```jinja2
{%- if is_scenario_bfd_onearm_echo -%}
    {%- for item in add_bfdsession_list_2 -%}
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

#### 1.9 采用静态路由+BFD时，配置静态路由并绑定BFD会话。采用BGP over静态路由+BFD时，请跳过该步骤。

##### 1.9.1 直连PE时，根据PE能力选择使用“BGP over静态路由+BFD”或“静态路由+BFD”。

##### 1.9.2 直连DCGW时，推荐采用“BGP over静态路由+BFD”。

##### 1.9.3 //“PREFIX”/“MASKLENGTH”是Tunnel隧道对端的源接口IP地址，请根据网设文档替换。

```jinja2
{%- if is_scenario_static_route_bfd -%}
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

#### 1.10 采用BGP over静态路由+BFD时，配置静态路由并绑定BFD会话。采用静态路由+BFD时，请跳过该步骤。

##### 1.10.1 //“PREFIX”和“MASKLENGTH”是目的IP和掩码（BGP对等体的IP地址和掩码）。

```jinja2
{%- if is_scenario_bgp_over_static_route_bfd -%}
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

#### 1.11 配置Loopback接口IP。用作Tunnel隧道的源接口。

```jinja2
{%- for item in add_interface_list_3 -%}
    ADD INTERFACE:
    {#- --- 必选参数 --- -#}
    IFNAME="{{item.IFNAME}}",
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_ipbindvpn_list_3 -%}
    ADD IPBINDVPN:
    {#- --- 必选参数 --- -#}
    IFNAME="{{item.IFNAME}}",
    VRFNAME="{{item.VRFNAME}}",
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_ifipv4address_list_3 -%}
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

### 2 配置虚拟重定向IP。

### 此处以配置主UPF为例。备UPF的配置与主UPF的配置过程相同，仅数据不同，请替换成实际规划的数据。

```jinja2
{%- for item in add_redundrdtip_list -%}
    ADD REDUNDRDTIP:
    {#- --- 必选参数 --- -#}
    IPVERSION={{item.IPVERSION}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPVERSION=IPv4 时必选 --- -#}
    {%- if item.IPVERSION == 'IPv4' -%}
        IPV4ADDRESS="{{item.IPV4ADDRESS}}",
    {%- endif -%}
    {#- --- 条件必选：IPVERSION=IPv6 时必选 --- -#}
    {%- if item.IPVERSION == 'IPv6' -%}
        IPV6ADDRESS="{{item.IPV6ADDRESS}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 配置GRE Tunnel。

### 此处以配置主UPF为例。备UPF的配置与主UPF的配置过程相同，仅数据不同，请替换成实际规划的数据。

```jinja2
{%- for item in add_interface_list_4 -%}
    ADD INTERFACE:
    {#- --- 必选参数 --- -#}
    IFNAME="{{item.IFNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.IFMTU is not none -%}
        IFMTU={{item.IFMTU}},
    {%- endif -%}
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
    {%- if item.DSTVPNNAME is not none -%}
        DSTVPNNAME="{{item.DSTVPNNAME}}",
    {%- endif -%}
    {%- if item.GREKEYEN is not none -%}
        GREKEYEN={{item.GREKEYEN}},
    {%- endif -%}
    {%- if item.KEEPALVEN is not none -%}
        KEEPALVEN={{item.KEEPALVEN}},
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
    {#- --- 条件必选：GREKEYEN=TRUE 时必选 --- -#}
    {%- if item.GREKEYEN == 'TRUE' -%}
        GREKEY="{{item.GREKEY}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：TNLTYPE=gre 时可选 --- -#}
    {%- if item.TNLTYPE == 'gre' -%}
        {%- if item.DSTIPADDR is not none -%}
            DSTIPADDR="{{item.DSTIPADDR}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：TNLTYPE=gre/gre6 时可选 --- -#}
    {%- if item.TNLTYPE in ['gre', 'gre6'] -%}
        {%- if item.REDUNDANCYEN is not none -%}
            REDUNDANCYEN={{item.REDUNDANCYEN}},
        {%- endif -%}
    {%- endif -%}
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
{%- for item in add_ifipv4address_list_4 -%}
    ADD IFIPV4ADDRESS:
    {#- --- 必选参数 --- -#}
    IFNAME="{{item.IFNAME}}",
    IFIPADDR="{{item.IFIPADDR}}",
    SUBNETMASK="{{item.SUBNETMASK}}",
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

### 4 配置到虚拟重定向IP的路由。

### 此处以配置主UPF为例。备UPF的配置与主UPF的配置过程相同，仅数据不同，请替换成实际规划的数据。

```jinja2
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
    {%- if item.IFNAME is not none -%}
        IFNAME="{{item.IFNAME}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

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
    {%- if item.IFNAME is not none -%}
        IFNAME="{{item.IFNAME}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 5 使能静态地址用户路由冗余功能。主备UPF上均需要执行本步骤。

```jinja2
{%- for item in set_redunduser_list -%}
    SET REDUNDUSER:
    {#- --- 必选参数 --- -#}
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

### 6 修改静态地址池，打开地址池的冗余备份开关。

### 此处以配置主UPF为例。备UPF的配置与主UPF的配置过程相同，仅数据不同，请替换成实际规划的数据。

```jinja2
{%- for item in mod_uppool_list -%}
    MOD UPPOOL:
    {#- --- 必选参数 --- -#}
    POOLNAME="{{item.POOLNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.POOLTYPE is not none -%}
        POOLTYPE={{item.POOLTYPE}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：POOLTYPE=EXTERNAL 时可选 --- -#}
    {%- if item.POOLTYPE == 'EXTERNAL' -%}
        {%- if item.REDUNDFUNC is not none -%}
            REDUNDFUNC={{item.REDUNDFUNC}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 7 开启APN路由冗余上行报文隧道转发功能。仅在备用UEG配置，主UPF上不配置。

```jinja2
{%- for item in set_apnredundupsw_list -%}
    SET APNREDUNDUPSW:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    {#- --- 可选参数 --- -#}
    {%- if item.IPV4SWITCH is not none -%}
        IPV4SWITCH={{item.IPV4SWITCH}},
    {%- endif -%}
    {%- if item.IPV6SWITCH is not none -%}
        IPV6SWITCH={{item.IPV6SWITCH}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 8 配置CU Full Mesh数据。在主备UPF上均需要执行本步骤。

#### 8.1 //打开本特性的License配置开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

#### 8.2 //配置用户面支持分配F-TEID。

```jinja2
{%- for item in set_cpteidualloc_list -%}
    SET CPTEIDUALLOC:
    {#- --- 必选参数 --- -#}
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```


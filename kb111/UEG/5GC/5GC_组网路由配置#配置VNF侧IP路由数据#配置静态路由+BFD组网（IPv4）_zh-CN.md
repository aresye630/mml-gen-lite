---
id: ''
name: 配置静态路由+BFD组网（IPv4）
ne_type: UEG
type: feature
description: UEG与对端设备可通过静态路由绑定静态BFD探测的方式进行组网连接。  在网络拓扑结构比较简单时，通常使用静态路由方式组网，合理的静态路由可以改进网络性能，并为业务保证带宽。同时，利用BFD检测机制，提高链路可靠性。  如图1所示为UEG与周边网元的静态路由互通组网示意图。UEG与三层路由设备运行静态路由协议而接入IP网络（运营商IP骨干网/企业网络）。  **图1** IPv4静态路由+IPv4 BFD组网  * UEG直连PE时，组bonding的2个端口连接到同一PE设备。 * UEG直连DCGW时，组bonding的2个端口连接到不同DCGW设备。
tags: []
risk_level: ''
doc_source:
  - ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（电力专网，入驻式）","软件安装与初始配置","部署UEG","电力专网采用风筝S部署模式","UEG初始配置","裸机容器模式UPF初始配置","参考：详细配置指导","组网路由配置","配置VNF侧IP路由数据","配置静态路由+BFD组网（IPv4）"]
  - ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（火电专网，入驻式）","部署配置指导","子园区部署入驻式UEG-S","子园区UEG-S初始配置","裸机容器模式UPF初始配置","参考：详细配置指导","组网路由配置","配置VNF侧IP路由数据","配置静态路由+BFD组网（IPv4）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
UEG与对端设备可通过静态路由绑定静态BFD探测的方式进行组网连接。在网络拓扑结构比较简单时，通常使用静态路由方式组网，合理的静态路由可以改进网络性能，并为业务保证带宽。同时，利用BFD检测机制，提高链路可靠性。如图1所示为UEG与周边网元的静态路由互通组网示意图。UEG与三层路由设备运行静态路由协议而接入IP网络（运营商IP骨干网/企业网络）。**图1** IPv4静态路由+IPv4 BFD组网* UEG直连PE时，组bonding的2个端口连接到同一PE设备。* UEG直连DCGW时，组bonding的2个端口连接到不同DCGW设备。

## 必备事项
前提条件

* 请阅读并熟悉特性IPFD-020503 静态路由和IPFD-020403 BFD特性概述。

* 具备管理员权限的操作人员已经登录华为操作维护系统（登录MAE客户端或登录OM Portal）。

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
          description: 'VPN实例全网统一规划，一条通信路径上所有节点绑定的VPN实例要一致，才能正常通信。'
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
          description: 'IPv4组网场景下，该参数选择ipv4uni。'
          data_source: '-'
          pattern: ''
          default: ''
    mod_interface_list:
      type: items
      properties:
        IFNAME:
          name: '接口名称'
          type: string
          maxLength: 63
          required: true
          description: '（UEG-S）请参考外联口介绍(机架服务器-ARM)/外联口介绍(刀片式服务器2U)进行规划。'
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
          data_source: ''
          pattern: ''
          default: ''
    add_interface_list:
      type: items
      properties:
        IFNAME:
          name: '子接口名字'
          type: string
          maxLength: 63
          required: true
          description: '非SR-IOV bonding组网需要规划。   （UEG-S）直连PE时，N6外联口采用非SR-IOV bonding组网，详细请参见外联口介绍(机架服务器-ARM)/外联口介绍(刀片式服务器2U)。'
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
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VRFNAME:
          name: 'VPN名字'
          type: string
          maxLength: 31
          required: true
          description: '-'
          data_source: '已配置数据中获取'
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
          name: 'VLAN类型子接口的VLAN ID'
          type: integer
          minimum: 1
          maximum: 4094
          required: true
          description: '此处以双平面为例，SR-IOV bonding单平面组网时，只需规划一条数据（例如只规划VLAN 100）。'
          data_source: '全网规划'
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
          name: '接口IPv4地址'
          type: string
          maxLength: 15
          required: true
          description: '如果规划外联口使用IPv4v6双栈地址，则分别执行**ADD IFIPV4ADDRESS**和**ADD IFIPV6ADDRESS**  对同一外联口配置IPv4和IPv6地址。  此处规划的IP地址是与网关互通的外联口IP。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        SUBNETMASK:
          name: '接口IPv4地址掩码'
          type: string
          maxLength: 15
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    mod_interface_list_2:
      type: items
      properties:
        IFNAME:
          name: '接口名称'
          type: string
          maxLength: 63
          required: true
          description: '（UEG-S）请参考外联口介绍(机架服务器-ARM)/外联口介绍(刀片式服务器2U)进行规划。'
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
          data_source: ''
          pattern: ''
          default: ''
    add_interface_list_2:
      type: items
      properties:
        IFNAME:
          name: '接口名称'
          type: string
          maxLength: 63
          required: true
          description: 'SR-IOV bonding组网需要规划。   （UEG-S）N3/N4/N9外联口采用SR-IOV bonding组网，详细请参见外联口介绍(机架服务器-ARM)/外联口介绍(刀片式服务器2U)。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    mod_trunkif_list:
      type: items
      properties:
        IFNAME:
          name: '接口名称'
          type: string
          maxLength: 63
          required: true
          description: 'SR-IOV bonding组网下需要规划。  需保证只有MAC地址一样的VNIC加到同一个Eth-trunk接口中。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        WORKMODE:
          name: '工作模式'
          type: string
          enum:
          - Lacp
          - Manual
          - MultiBackup
          required: true
          description: ''
          data_source: '固定值'
          pattern: ''
          default: ''
    add_trunkmember_list:
      type: items
      properties:
        TRUNKIFNAME:
          name: 'Trunk接口名'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        MEMBERIFNAME:
          name: '成员接口名'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_interface_list_3:
      type: items
      properties:
        IFNAME:
          name: '接口名称'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_ipbindvpn_list_2:
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
          name: 'VPN名字'
          type: string
          maxLength: 31
          required: true
          description: '-'
          data_source: '已配置数据中获取'
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
          name: 'VLAN类型子接口的VLAN ID'
          type: integer
          minimum: 1
          maximum: 4094
          required: true
          description: '此处以双平面为例，SR-IOV bonding单平面组网时，只需规划一条数据（例如只规划VLAN 100）。'
          data_source: '全网规划'
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
          name: '接口IPv4地址'
          type: string
          maxLength: 15
          required: true
          description: '如果规划外联口使用IPv4v6双栈地址，则分别执行**ADD IFIPV4ADDRESS**和**ADD IFIPV6ADDRESS**  对同一外联口配置IPv4和IPv6地址。  此处规划的IP地址是与网关互通的外联口IP。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        SUBNETMASK:
          name: '接口IPv4地址掩码'
          type: string
          maxLength: 15
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    set_bfd_list:
      type: items
      properties:
        BFDENABLE:
          name: '激活BFD'
          type: string
          enum:
          - TRUE
          - FALSE
          required: true
          description: '参数“DELAYUPTIMER”（会话延迟UP时间）和“TOSEXP”（动态会话报文优先级）可以不用配置，使用默认值即可。'
          data_source: '全网规划'
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
          description: '-'
          data_source: '本端规划'
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
          data_source: '固定取值'
          pattern: ''
          default: ''
        LOCALDISCR:
          name: '本地标识符'
          type: integer
          minimum: 1
          maximum: 16384
          required: false
          description: 'UEG上BFD会话的本地标识符，需要和对接网关上的标识符对应，即本端的本地标识符与对端网关侧的远端标识符相同。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        REMOTEDISCR:
          name: '远端标识符'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: false
          description: 'UEG上BFD会话的远端标识符，需要和对接网关上的标识符对应，即本端的远端标识符与对端网关侧的本端标识符相同。'
          data_source: '与对端协商'
          pattern: ''
          default: ''
        DESTADDR4:
          name: 'IPv4目的地址'
          type: string
          maxLength: 15
          required: false
          description: '参数“DESTADDR4”是网关的接口IP，此处用于检测目的IP能否正常接收报文。'
          data_source: '与对端协商'
          pattern: ''
          default: ''
        LINKTYPE:
          name: '链路类型'
          type: string
          enum:
          - IP
          required: true
          description: ''
          data_source: '固定取值'
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
          data_source: '固定取值'
          pattern: ''
          default: ''
        IFNAME:
          name: '出接口名称'
          type: string
          maxLength: 63
          required: false
          description: '非SR-IOV bonding组网需要规划Ethernet接口，SR-IOV bonding组网需要规划Eth-trunk接口。  -'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: false
          description: '直连PE设备时，PE不支持BFD探测时，“ONEARMECHO”需要设置为“TRUE”。'
          data_source: '已配置数据中获取'
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
          data_source: '全网规划'
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
          description: '-'
          data_source: '本端规划'
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
          data_source: '固定取值'
          pattern: ''
          default: ''
        LOCALDISCR:
          name: '本地标识符'
          type: integer
          minimum: 1
          maximum: 16384
          required: false
          description: 'UEG上BFD会话的本地标识符，需要和对接网关上的标识符对应，即本端的本地标识符与对端网关侧的远端标识符相同。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        REMOTEDISCR:
          name: '远端标识符'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: false
          description: 'UEG上BFD会话的远端标识符，需要和对接网关上的标识符对应，即本端的远端标识符与对端网关侧的本端标识符相同。'
          data_source: '与对端协商'
          pattern: ''
          default: ''
        DESTADDR4:
          name: 'IPv4目的地址'
          type: string
          maxLength: 15
          required: false
          description: '参数“DESTADDR4”是网关的接口IP，此处用于检测目的IP能否正常接收报文。'
          data_source: '与对端协商'
          pattern: ''
          default: ''
        LINKTYPE:
          name: '链路类型'
          type: string
          enum:
          - IP
          required: true
          description: ''
          data_source: '固定取值'
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
          data_source: '固定取值'
          pattern: ''
          default: ''
        IFNAME:
          name: '出接口名称'
          type: string
          maxLength: 63
          required: false
          description: '非SR-IOV bonding组网需要规划Ethernet接口，SR-IOV bonding组网需要规划Eth-trunk接口。  -'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: false
          description: '直连PE设备时，PE不支持BFD探测时，“ONEARMECHO”需要设置为“TRUE”。'
          data_source: '已配置数据中获取'
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
          data_source: '全网规划'
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
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: false
          description: '双平面组网时，2个路由下一跳IP地址在不同网段。  参数“PREFIX”是目的IP，规划的是用于传输N3接口报文时，此处是基站的IP地址。  参数“NEXTHOP”是网关的接口IP。'
          data_source: '已配置数据中获取'
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
          data_source: '与对端协商'
          pattern: ''
          default: ''
        MASKLENGTH:
          name: '路由掩码长度'
          type: integer
          minimum: 0
          maximum: 32
          required: true
          description: ''
          data_source: '与对端协商'
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
          maxLength: 15
          required: false
          description: ''
          data_source: '已规划数据中获取'
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
        SESSIONNAME:
          name: '静态BFD会话名'
          type: string
          maxLength: 64
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_srroute_list_2:
      type: items
      properties:
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: false
          description: '双平面组网时，2个路由下一跳IP地址在不同网段。  参数“PREFIX”是目的IP，规划的是用于传输N3接口报文时，此处是基站的IP地址。  参数“NEXTHOP”是网关的接口IP。'
          data_source: '已配置数据中获取'
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
          data_source: '与对端协商'
          pattern: ''
          default: ''
        MASKLENGTH:
          name: '路由掩码长度'
          type: integer
          minimum: 0
          maximum: 32
          required: true
          description: ''
          data_source: '与对端协商'
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
          maxLength: 15
          required: false
          description: ''
          data_source: '已规划数据中获取'
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
        SESSIONNAME:
          name: '静态BFD会话名'
          type: string
          maxLength: 64
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
  examples:
    add_l3vpninst_list:
    - VRFNAME: 'VPN_Access'
    add_vpninstaf_list:
    - VRFNAME: 'VPN_Access'
      AFTYPE: ipv4uni
    mod_interface_list:
    - IFNAME: 'Ethernet64/0/4'
      IFADMINSTATUS: up
    add_interface_list:
    - IFNAME: 'Ethernet64/0/4.1'
    add_ipbindvpn_list:
    - IFNAME: 'Ethernet64/0/4.1'
      VRFNAME: 'VPN_Access'
    add_ethsubif_list:
    - IFNAME: 'Ethernet64/0/4.1'
      VLANTYPEVID: 100
    add_ifipv4address_list:
    - IFNAME: 'Ethernet64/0/4.1'
      IFIPADDR: '192.168.89.2'
      SUBNETMASK: '255.255.255.248'
    mod_interface_list_2:
    - IFNAME: 'Ethernet64/0/4'
      IFADMINSTATUS: up
    add_interface_list_2:
    - IFNAME: 'Eth-trunk1'
    mod_trunkif_list:
    - IFNAME: 'Eth-Trunk1'
      WORKMODE: Manual
    add_trunkmember_list:
    - TRUNKIFNAME: 'Eth-trunk1'
      MEMBERIFNAME: 'Ethernet64/0/4'
    add_interface_list_3:
    - IFNAME: 'Eth-trunk1.1'
    add_ipbindvpn_list_2:
    - IFNAME: 'Eth-trunk1.1'
      VRFNAME: 'VPN_Access'
    add_ethsubif_list_2:
    - IFNAME: 'Eth-trunk1.1'
      VLANTYPEVID: 100
    add_ifipv4address_list_2:
    - IFNAME: 'Eth-trunk1.1'
      IFIPADDR: '192.168.89.2'
      SUBNETMASK: '255.255.255.248'
    set_bfd_list:
    - BFDENABLE: TRUE
    add_bfdsession_list:
    - SESSNAME: 'BfdName21'
      ADDRTYPE: IPv4
      LOCALDISCR: 121
      REMOTEDISCR: 221
      DESTADDR4: '192.168.89.1'
      LINKTYPE: IP
      CREATETYPE4: SESS_STATIC
      IFNAME: 'Ethernet64/0/4.1'
      VRFNAME: 'VPN_Access'
      ONEARMECHO: FALSE
      ONEARMECHO6: FALSE
      CREATETYPE6: ''
    add_bfdsession_list_2:
    - SESSNAME: 'BfdName21'
      ADDRTYPE: IPv4
      LOCALDISCR: 121
      REMOTEDISCR: 221
      DESTADDR4: '192.168.89.1'
      LINKTYPE: IP
      CREATETYPE4: SESS_STATIC
      IFNAME: 'Eth-trunk1.1'
      VRFNAME: 'VPN_Access'
      ONEARMECHO: FALSE
      ONEARMECHO6: FALSE
      CREATETYPE6: ''
    add_srroute_list:
    - VRFNAME: 'VPN_Access'
      AFTYPE: ipv4unicast
      PREFIX: '192.168.53.4'
      MASKLENGTH: 32
      DESTVRFNAME: 'VPN_Access'
      NEXTHOP: '192.168.89.1'
      IFNAME: 'Ethernet64/0/4.1'
      SESSIONNAME: 'BfdName21'
    add_srroute_list_2:
    - VRFNAME: 'VPN_Access'
      AFTYPE: ipv4unicast
      PREFIX: '192.168.53.4'
      MASKLENGTH: 32
      DESTVRFNAME: 'VPN_Access'
      NEXTHOP: '192.168.89.1'
      IFNAME: 'Eth-trunk1.1'
      SESSIONNAME: 'BfdName21'
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 配置外联口的VPN实例。

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

### 一条通信路径上所有节点绑定的VPN实例要一致，才能正常通信，例如UEG逻辑接口、UEG外联口、网关上的VPN，否则从逻辑接口发出去的报文会查询路由失败。

### 2 非SR-IOV bonding组网时，配置外联口IP地址。SR-IOV bonding组网时，请跳转到3。

#### 2.1 查询接口名，确认CSLB上可使用的外联口的接口类型和接口编号。

#### 2.2 配置主接口的管理状态为up。

```jinja2
{%- if is_scenario_non_sriov_bonding -%}
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
{%- endif -%}
```

#### 2.3 配置以太网子接口。

```jinja2
{%- if is_scenario_non_sriov_bonding -%}
    {%- for item in add_interface_list -%}
        ADD INTERFACE:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 2.4 增加接口绑定VPN。

```jinja2
{%- if is_scenario_non_sriov_bonding -%}
    {%- for item in add_ipbindvpn_list -%}
        ADD IPBINDVPN:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        VRFNAME="{{item.VRFNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 2.5 在以太网子接口上关联VLAN ID。

```jinja2
{%- if is_scenario_non_sriov_bonding -%}
    {%- for item in add_ethsubif_list -%}
        ADD ETHSUBIF:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        VLANTYPEVID={{item.VLANTYPEVID}},
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 子接口配置了VLAN，则需要在交换机、对接网关上调整VLAN的配置。

#### 2.6 配置外联口IP地址。

```jinja2
{%- if is_scenario_non_sriov_bonding -%}
    {%- for item in add_ifipv4address_list -%}
        ADD IFIPV4ADDRESS:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        IFIPADDR="{{item.IFIPADDR}}",
        SUBNETMASK="{{item.SUBNETMASK}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 如果规划外联口使用IPv4v6双栈地址，则分别执行**ADD IFIPV4ADDRESS**和**ADD IFIPV6ADDRESS**对同一外联口配置IPv4和IPv6地址。

### 3 SR-IOV bonding组网时，配置外联口IP地址。

#### 3.1 查询接口名，确认CSLB上可使用的外联口的接口类型和接口编号。

#### 3.2 配置主接口的管理状态为up。

```jinja2
{%- if is_scenario_sriov_bonding -%}
    {%- for item in mod_interface_list_2 -%}
        MOD INTERFACE:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        {#- --- 可选参数 --- -#}
        {%- if item.IFADMINSTATUS is not none -%}
            IFADMINSTATUS={{item.IFADMINSTATUS}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 3.3 配置以太Trunk接口。

```jinja2
{%- if is_scenario_sriov_bonding -%}
    {%- for item in add_interface_list_2 -%}
        ADD INTERFACE:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 3.4 配置Eth-trunk接口的工作模式并添加成员端口。

```jinja2
{%- if is_scenario_sriov_bonding -%}
    {%- for item in mod_trunkif_list -%}
        MOD TRUNKIF:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        WORKMODE={{item.WORKMODE}},
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_sriov_bonding -%}
    {%- for item in add_trunkmember_list -%}
        ADD TRUNKMEMBER:
        {#- --- 必选参数 --- -#}
        TRUNKIFNAME="{{item.TRUNKIFNAME}}",
        MEMBERIFNAME="{{item.MEMBERIFNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 3.5 配置以太Trunk子接口。

```jinja2
{%- if is_scenario_sriov_bonding -%}
    {%- for item in add_interface_list_3 -%}
        ADD INTERFACE:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 3.6 增加接口绑定VPN。

```jinja2
{%- if is_scenario_sriov_bonding -%}
    {%- for item in add_ipbindvpn_list_2 -%}
        ADD IPBINDVPN:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        VRFNAME="{{item.VRFNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 3.7 在以太Trunk子接口上关联VLAN ID。

```jinja2
{%- if is_scenario_sriov_bonding -%}
    {%- for item in add_ethsubif_list_2 -%}
        ADD ETHSUBIF:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        VLANTYPEVID={{item.VLANTYPEVID}},
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 子接口配置了VLAN，则需要在交换机、对接网关上调整VLAN的配置。

#### 3.8 配置外联口IP地址。

```jinja2
{%- if is_scenario_sriov_bonding -%}
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

#### 如果规划外联口使用IPv4v6双栈地址，则分别执行**ADD IFIPV4ADDRESS**和**ADD IFIPV6ADDRESS**对同一外联口配置IPv4和IPv6地址。

### 4 全局激活BFD。

```jinja2
{%- for item in set_bfd_list -%}
    SET BFD:
    {#- --- 必选参数 --- -#}
    BFDENABLE={{item.BFDENABLE}},
    ;
{%- endfor -%}
```

### 5 新建BFD会话。

### 必须全局使能BFD功能后该命令才可生效。

#### 5.1 非SR-IOV bonding组网场景下：

```jinja2
{%- if is_scenario_non_sriov_bonding -%}
    {%- for item in add_bfdsession_list -%}
        ADD BFDSESSION:
        {#- --- 必选参数 --- -#}
        SESSNAME="{{item.SESSNAME}}",
        ADDRTYPE={{item.ADDRTYPE}},
        LINKTYPE={{item.LINKTYPE}},
        {#- --- 可选参数 --- -#}
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

#### 5.2 SR-IOV bonding组网场景下：

```jinja2
{%- if is_scenario_sriov_bonding -%}
    {%- for item in add_bfdsession_list_2 -%}
        ADD BFDSESSION:
        {#- --- 必选参数 --- -#}
        SESSNAME="{{item.SESSNAME}}",
        ADDRTYPE={{item.ADDRTYPE}},
        LINKTYPE={{item.LINKTYPE}},
        {#- --- 可选参数 --- -#}
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

### 6 配置静态路由并绑定BFD会话。

#### 6.1 非SR-IOV bonding组网场景下：

```jinja2
{%- if is_scenario_non_sriov_bonding -%}
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
        {%- if item.NEXTHOP is not none -%}
            NEXTHOP="{{item.NEXTHOP}}",
        {%- endif -%}
        {%- if item.IFNAME is not none -%}
            IFNAME="{{item.IFNAME}}",
        {%- endif -%}
        {%- if item.SESSIONNAME is not none -%}
            SESSIONNAME="{{item.SESSIONNAME}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 6.2 SR-IOV bonding组网场景下：

```jinja2
{%- if is_scenario_sriov_bonding -%}
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
        {%- if item.NEXTHOP is not none -%}
            NEXTHOP="{{item.NEXTHOP}}",
        {%- endif -%}
        {%- if item.IFNAME is not none -%}
            IFNAME="{{item.IFNAME}}",
        {%- endif -%}
        {%- if item.SESSIONNAME is not none -%}
            SESSIONNAME="{{item.SESSIONNAME}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 如果需要为静态路由绑定静态BFD会话，通过**ADD SRROUTE**的“静态BFD会话名”来指定静态路由所联动的静态BFD的会话名。

### 在网关侧配置到UEG的回程路由，目的地址为VNF上各逻辑接口的IP地址，下一跳为VNF上配置的各逻辑接口对应的外联口的IP地址。

### 需要说明的是，配置UEG与DN/PDN通信的回程路由时，目的地址为UE的网段地址，下一跳为VNF上外联口的IP地址。


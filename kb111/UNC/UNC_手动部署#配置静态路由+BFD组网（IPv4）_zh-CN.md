---
id: ''
name: 配置静态路由+BFD组网（IPv4）
ne_type: UNC
type: feature
description: VNF与对端设备可通过静态路由绑定静态BFD探测的方式进行组网连接。在网络拓扑结构比较简单时，通常使用静态路由方式组网，合理的静态路由可以改进网络性能，并为业务保证带宽。同时，利用BFD双向/单臂echo转发检测机制为链路提供双向/单向、轻负荷且持续时间短的快速检测功能，提高链路可靠性。  * 图1为VNF与周边网元的静态路由互通组网示意图。VNF与网关侧运行静态路由协议而接入运营商网络（IP骨干网），网关推荐使用DC-GW，也可以使用运营商的PE（Provider Edge）交换机，或者EOR（End of Row）交换机。无论哪种方式，VNF的配置相同，没有差异。PE的路由配置请参考运营商的网络规划配置，DC-GW/EOR的配置请参考对应型号设备的产品文档。 * 图2为VNF与周边网元的静态路由互通组网示意图。VNF与网关侧运行静态路由协议而接入运营商网络（IP骨干网），DC-GW作为网关设备。VNF和DC-GW之间采用单臂BFD探测。DC-GW的配置请参考对应型号设备的产品文档。  **图1** 静态路由+BFD组网（DC-GW/EOR做L3GW）  **图2** 静态路由+BFD组网（DC-GW做L3GW+L2GW）
risk_level: ''
doc_source: ["网络部署","初始配置","UNC初始配置与调测","组网路由配置","配置VNF侧IP路由数据（非SDN）","手动部署","配置静态路由+BFD组网（IPv4）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
VNF与对端设备可通过静态路由绑定静态BFD探测的方式进行组网连接。在网络拓扑结构比较简单时，通常使用静态路由方式组网，合理的静态路由可以改进网络性能，并为业务保证带宽。同时，利用BFD双向/单臂echo转发检测机制为链路提供双向/单向、轻负荷且持续时间短的快速检测功能，提高链路可靠性。* 图1为VNF与周边网元的静态路由互通组网示意图。VNF与网关侧运行静态路由协议而接入运营商网络（IP骨干网），网关推荐使用DC-GW，也可以使用运营商的PE（Provider Edge）交换机，或者EOR（End of Row）交换机。无论哪种方式，VNF的配置相同，没有差异。PE的路由配置请参考运营商的网络规划配置，DC-GW/EOR的配置请参考对应型号设备的产品文档。* 图2为VNF与周边网元的静态路由互通组网示意图。VNF与网关侧运行静态路由协议而接入运营商网络（IP骨干网），DC-GW作为网关设备。VNF和DC-GW之间采用单臂BFD探测。DC-GW的配置请参考对应型号设备的产品文档。**图1** 静态路由+BFD组网（DC-GW/EOR做L3GW）**图2** 静态路由+BFD组网（DC-GW做L3GW+L2GW）

## 必备事项
前提条件

* 请阅读并熟悉特性IPFD-014003 静态路由和IPFD-012003 BFD特性概述。

* 具备管理员权限的操作人员已经登录华为操作维护系统（登录U2020/MAE客户端或登录OM Portal）。

* VNF与网络实体之间的网络环境已经构建完成。
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
          description: 'VPN实例全网统一规划，一条通信路径上所有节点绑定的VPN实例要一致，才能正常通信。'
          data_source: '参见“5G Core LLD文档 > 路由设计 > 5G Core路由设计 > VRF设计 > VRF名称(VNF)”。'
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
          description: '-'
          data_source: '参见“5G Core LLD文档 > 业务IP对接设计 > 业务IP设计 > 端口”。'
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
          description: '-'
          data_source: '参见“5G Core LLD文档 > 业务IP对接设计 > 业务IP设计 > 子端口”。'
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
          data_source: '参见“5G Core LLD文档 > 业务IP对接设计 > 业务IP设计 > VRF”。'
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
          description: '-'
          data_source: '参见“5G Core LLD文档 > 业务IP对接设计 > 业务IP设计 > VLAN序号”。'
          pattern: ''
          default: ''
    add_dhcpclient_list:
      type: items
      properties:
        IFNAME:
          name: '接口名称'
          type: string
          maxLength: 63
          required: true
          description: '采用DHCP获取外联口IP地址时需要规划，静态配置外联口IP地址时不需要规划。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        ISDHCPV4CENABLE:
          name: 'DHCPv4客户端使能'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: TRUE
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
          description: '如果规划外联口使用IPv4v6双栈地址，则分别执行**ADD IFIPV4ADDRESS**和**ADD IFIPV6ADDRESS**对同一vNIC配置IPv4和IPv6地址。静态配置外联口IP地址时需要规划，DHCP获取外联口IP地址时不需要规划。'
          data_source: '参见“5G Core LLD文档 > 业务IP对接设计 > 业务IP设计 > IP”。'
          pattern: ''
          default: ''
        SUBNETMASK:
          name: '接口IPv4地址掩码'
          type: string
          maxLength: 15
          required: true
          description: ''
          data_source: '参见“5G Core LLD文档 > 业务IP对接设计 > 业务IP设计 > 子网掩码”。'
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
          data_source: '参见“5G Core LLD文档 > 路由设计 > 其他路由设计信息 > BFD设计 > BFD是否使能”。'
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
          data_source: '参见“5G Core LLD文档 > 路由设计 > BFD会话 > 会话名称”。'
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
          data_source: '参见“5G Core LLD文档 > 路由设计 > BFD会话 > IP协议版本号”。'
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
          data_source: '参见“5G Core LLD文档 > 路由设计 > BFD会话 > 会话创建方式”。'
          pattern: ''
          default: ''
        ONEARMECHO:
          name: 'IPv4单臂Echo'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: 'SDN场景，必须设置为“TRUE”。非SDN场景，请根据实际组网规划。此处以双向BFD为例。'
          data_source: '参见“5G Core LLD文档 > 路由设计 > BFD会话 > 单臂Echo”。'
          pattern: ''
          default: ''
        DESTADDR4:
          name: 'IPv4目的地址'
          type: string
          maxLength: 15
          required: false
          description: '参数“DESTADDR4”是网关的接口IP，此处用于检测目的IP能否正常接收报文。'
          data_source: '参见“5G Core LLD文档 > 路由设计 > BFD会话 > 目的地址”。'
          pattern: ''
          default: ''
        LINKTYPE:
          name: '链路类型'
          type: string
          enum:
          - IP
          required: true
          description: ''
          data_source: '参见“5G Core LLD文档 > 路由设计 > BFD会话 > 链路类型”。'
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
          data_source: '参见“5G Core LLD文档 > 路由设计 > BFD会话 > VPN实例名称”。'
          pattern: ''
          default: ''
        LOCALDISCR:
          name: '本地标识符'
          type: integer
          minimum: 1
          maximum: 16384
          required: false
          description: '双向BFD时，VNF上BFD会话的本地标识符，需要和对接网关上的标识符对应，即本端的本地标识符与对端网关侧的远端标识符相同。单臂BFD时，VNF内不重复即可。'
          data_source: '参见“5G Core LLD文档 > 路由设计 > BFD会话 > 本地标识符”。'
          pattern: ''
          default: ''
        REMOTEDISCR:
          name: '远端标识符'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: false
          description: '双向BFD时，VNF上BFD会话的远端标识符，需要和对接网关上的标识符对应，即本端的远端标识符与对端网关侧的本端标识符相同。单臂BFD时，不需要规划远端标识符。'
          data_source: '参见“5G Core LLD文档 > 路由设计 > BFD会话 > 远端标识符”。'
          pattern: ''
          default: ''
        IFNAME:
          name: '出接口名称'
          type: string
          maxLength: 63
          required: false
          description: ''
          data_source: '参见“5G Core LLD文档 > 路由设计 > BFD会话 > 出接口名称”。'
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
        SRCADDR4:
          name: 'IPv4源地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TOSEXP:
          name: '报文优先级'
          type: integer
          minimum: 0
          maximum: 7
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 7
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
    add_bfdsession_list_4:
      type: items
      properties:
        SESSNAME:
          name: '会话名称'
          type: string
          maxLength: 64
          required: true
          description: '-'
          data_source: '参见“5G Core LLD文档 > 路由设计 > BFD会话 > 会话名称”。'
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
          data_source: '参见“5G Core LLD文档 > 路由设计 > BFD会话 > IP协议版本号”。'
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
          data_source: '参见“5G Core LLD文档 > 路由设计 > BFD会话 > 会话创建方式”。'
          pattern: ''
          default: ''
        ONEARMECHO:
          name: 'IPv4单臂Echo'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: 'SDN场景，必须设置为“TRUE”。非SDN场景，请根据实际组网规划。此处以双向BFD为例。'
          data_source: '参见“5G Core LLD文档 > 路由设计 > BFD会话 > 单臂Echo”。'
          pattern: ''
          default: ''
        DESTADDR4:
          name: 'IPv4目的地址'
          type: string
          maxLength: 15
          required: false
          description: '参数“DESTADDR4”是网关的接口IP，此处用于检测目的IP能否正常接收报文。'
          data_source: '参见“5G Core LLD文档 > 路由设计 > BFD会话 > 目的地址”。'
          pattern: ''
          default: ''
        LINKTYPE:
          name: '链路类型'
          type: string
          enum:
          - IP
          required: true
          description: ''
          data_source: '参见“5G Core LLD文档 > 路由设计 > BFD会话 > 链路类型”。'
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
          data_source: '参见“5G Core LLD文档 > 路由设计 > BFD会话 > VPN实例名称”。'
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
          description: '双向BFD时，VNF上BFD会话的本地标识符，需要和对接网关上的标识符对应，即本端的本地标识符与对端网关侧的远端标识符相同。单臂BFD时，VNF内不重复即可。'
          data_source: '参见“5G Core LLD文档 > 路由设计 > BFD会话 > 本地标识符”。'
          pattern: ''
          default: ''
        IFNAME:
          name: '出接口名称'
          type: string
          maxLength: 63
          required: false
          description: ''
          data_source: '参见“5G Core LLD文档 > 路由设计 > BFD会话 > 出接口名称”。'
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
        SRCADDR4:
          name: 'IPv4源地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TOSEXP:
          name: '报文优先级'
          type: integer
          minimum: 0
          maximum: 7
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 7
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
    add_srroute_list:
      type: items
      properties:
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: false
          description: '参数“PREFIX”是目的IP，规划的是用于传输N4接口报文时，此处是UPF上的N4逻辑接口IP地址。参数“NEXTHOP”是网关的接口IP。'
          data_source: '参见“5G Core LLD文档 > 路由设计 > 静态路由设计 > VRF名称”。'
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
          data_source: '参见“5G Core LLD文档 > 路由设计 > 静态路由设计 > 路由前缀”。'
          pattern: ''
          default: ''
        MASKLENGTH:
          name: '路由掩码长度'
          type: integer
          minimum: 0
          maximum: 32
          required: true
          description: ''
          data_source: '参见“5G Core LLD文档 > 路由设计 > 静态路由设计 > 掩码长度”。'
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
          data_source: '参见“5G Core LLD文档 > 路由设计 > 静态路由设计 > 静态BFD会话”。'
          pattern: ''
          default: ''
        DHCPENABLE:
          name: 'DHCP使能标识'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: 'DHCP获取外联口IP地址时，设置为“TRUE”。静态配置外联口IP地址时，设置为“FALSE”。'
          data_source: '本端规划'
          pattern: ''
          default: FALSE
    add_srroute_list_8:
      type: items
      properties:
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: false
          description: '参数“PREFIX”是目的IP，规划的是用于传输N4接口报文时，此处是UPF上的N4逻辑接口IP地址。参数“NEXTHOP”是网关的接口IP。'
          data_source: '参见“5G Core LLD文档 > 路由设计 > 静态路由设计 > VRF名称”。'
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
          data_source: '参见“5G Core LLD文档 > 路由设计 > 静态路由设计 > 路由前缀”。'
          pattern: ''
          default: ''
        MASKLENGTH:
          name: '路由掩码长度'
          type: integer
          minimum: 0
          maximum: 32
          required: true
          description: ''
          data_source: '参见“5G Core LLD文档 > 路由设计 > 静态路由设计 > 掩码长度”。'
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
          data_source: '参见“5G Core LLD文档 > 路由设计 > 静态路由设计 > 静态BFD会话”。'
          pattern: ''
          default: ''
        DHCPENABLE:
          name: 'DHCP使能标识'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: 'DHCP获取外联口IP地址时，设置为“TRUE”。静态配置外联口IP地址时，设置为“FALSE”。'
          data_source: '本端规划'
          pattern: ''
          default: FALSE
  examples:
    add_l3vpninst_list:
    - VRFNAME: 'VPN_Access'
    add_vpninstaf_list:
    - VRFNAME: 'VPN_Access'
      AFTYPE: ipv4uni
    mod_interface_list:
    - IFNAME: 'Ethernet66/0/4'
      IFADMINSTATUS: up
    add_interface_list:
    - IFNAME: 'Ethernet66/0/4.1'
    add_ipbindvpn_list:
    - IFNAME: 'Ethernet66/0/4.1'
      VRFNAME: 'VPN_Access'
    add_ethsubif_list:
    - IFNAME: 'Ethernet66/0/4.1'
      VLANTYPEVID: 100
    add_dhcpclient_list:
    - IFNAME: 'Ethernet66/0/4.1'
      ISDHCPV4CENABLE: TRUE
    add_ifipv4address_list:
    - IFNAME: 'Ethernet66/0/4.1'
      IFIPADDR: '192.168.89.2'
      SUBNETMASK: '255.255.255.248'
    set_bfd_list:
    - BFDENABLE: TRUE
    add_bfdsession_list:
    - SESSNAME: 'BfdName21'
      ADDRTYPE: IPv4
      CREATETYPE4: SESS_STATIC
      ONEARMECHO: FALSE
      DESTADDR4: '192.168.89.1'
      LINKTYPE: IP
      MINTXINT: 500
      MINRXINT: 500
      DETECTMULTI: 4
      VRFNAME: 'VPN_Access'
      LOCALDISCR: 121
      REMOTEDISCR: 221
      IFNAME: 'Ethernet66/0/4.1'
      CREATETYPE6: ''
      ONEARMECHO6: FALSE
      DESTADDR6: ''
      SRCADDR4: ''
      TOSEXP: 7
      MINECHORXINT: 200
    add_bfdsession_list_4:
    - SESSNAME: 'BfdName21'
      ADDRTYPE: IPv4
      CREATETYPE4: SESS_STATIC
      ONEARMECHO: TRUE
      DESTADDR4: '192.168.89.1'
      LINKTYPE: IP
      DETECTMULTI: 4
      VRFNAME: 'VPN_Access'
      MINECHORXINT: 500
      LOCALDISCR: 121
      IFNAME: 'Ethernet66/0/4.1'
      CREATETYPE6: ''
      ONEARMECHO6: FALSE
      DESTADDR6: ''
      MINRXINT: 200
      MINTXINT: 200
      SRCADDR4: ''
      TOSEXP: 7
      REMOTEDISCR: ''
    add_srroute_list:
    - VRFNAME: 'VPN_Access'
      AFTYPE: ipv4unicast
      PREFIX: '192.168.53.4'
      MASKLENGTH: 32
      DESTVRFNAME: 'VPN_Access'
      NEXTHOP: '192.168.89.1'
      IFNAME: 'Ethernet66/0/4.1'
      SESSIONNAME: 'BfdName21'
      DHCPENABLE: FALSE
    add_srroute_list_8:
    - VRFNAME: 'VPN_Access'
      AFTYPE: ipv4unicast
      PREFIX: '192.168.53.4'
      MASKLENGTH: 32
      DESTVRFNAME: 'VPN_Access'
      NEXTHOP: '192.168.89.1'
      IFNAME: 'Ethernet66/0/4.1'
      SESSIONNAME: 'BfdName21'
      DHCPENABLE: TRUE
```

## 3 命令模板定义
<!-- @mml:block=commands -->

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

### 一条通信路径上所有节点绑定的VPN实例要一致，才能正常通信，例如VNF逻辑接口、VNF外联口、网关上的VPN，否则从逻辑接口发出去的报文会查询路由失败。

### 2 配置外联口IP地址。

#### 2.1 查询接口名，确认CSLB上可使用的外联口的接口类型和接口编号。

#### 2.2 配置主接口的管理状态为up。

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

#### 2.3 配置以太网子接口。

```jinja2
{%- for item in add_interface_list -%}
    ADD INTERFACE:
    {#- --- 必选参数 --- -#}
    IFNAME="{{item.IFNAME}}",
    ;
{%- endfor -%}
```

#### 2.4 增加接口绑定VPN。

```jinja2
{%- for item in add_ipbindvpn_list -%}
    ADD IPBINDVPN:
    {#- --- 必选参数 --- -#}
    IFNAME="{{item.IFNAME}}",
    VRFNAME="{{item.VRFNAME}}",
    ;
{%- endfor -%}
```

#### 2.5 在以太网子接口上关联VLAN ID。

```jinja2
{%- for item in add_ethsubif_list -%}
    ADD ETHSUBIF:
    {#- --- 必选参数 --- -#}
    IFNAME="{{item.IFNAME}}",
    VLANTYPEVID={{item.VLANTYPEVID}},
    ;
{%- endfor -%}
```

#### 子接口配置了VLAN，则需要在交换机、对接网关上调整VLAN的配置。

#### 2.6 配置外联口IP通过DHCP动态获取。静态配置外联口IP地址时，请跳过该步骤。

```jinja2
{%- if is_scenario_dhcp_external_ip -%}
    {%- for item in add_dhcpclient_list -%}
        ADD DHCPCLIENT:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        {#- --- 可选参数 --- -#}
        {%- if item.ISDHCPV4CENABLE is not none -%}
            ISDHCPV4CENABLE={{item.ISDHCPV4CENABLE}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 2.7 配置外联口IP地址。DHCP获取外联口IP地址时，请跳过该步骤。

```jinja2
{%- if is_scenario_static_external_ip -%}
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

#### 如果规划外联口使用IPv4v6双栈地址，则分别执行**ADD IFIPV4ADDRESS**和**ADD IFIPV6ADDRESS**对同一vNIC配置IPv4和IPv6地址。

### 3 全局激活BFD。

```jinja2
{%- for item in set_bfd_list -%}
    SET BFD:
    {#- --- 必选参数 --- -#}
    BFDENABLE={{item.BFDENABLE}},
    ;
{%- endfor -%}
```

### 4 新建BFD会话。

### 必须全局使能BFD功能后该命令才可生效。

#### 4.1 //双向BFD：

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
        {#- --- 条件可选：CREATETYPE4=SESS_STATIC 时可选 --- -#}
        {%- if item.CREATETYPE4 == 'SESS_STATIC' -%}
            {%- if item.TOSEXP is not none -%}
                TOSEXP={{item.TOSEXP}},
            {%- endif -%}
        {#- --- 条件可选：CREATETYPE6=SESS_STATIC 时可选 --- -#}
        {%- elif item.CREATETYPE6 == 'SESS_STATIC' -%}
            {%- if item.TOSEXP is not none -%}
                TOSEXP={{item.TOSEXP}},
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
        {#- --- IPv4源地址: 条件必选(IPv4会话创建方式=SESS_AUTO) / 条件可选(IPv4单臂Echo=TRUE|FALSE) --- -#}
        {%- if (item.CREATETYPE4 == 'SESS_AUTO') -%}
            SRCADDR4="{{item.SRCADDR4}}",
        {%- elif (item.ONEARMECHO in ['TRUE', 'FALSE']) -%}
            {%- if item.SRCADDR4 is not none -%}
                SRCADDR4="{{item.SRCADDR4}}",
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 4.2 //单臂BFD（BFD echo）：

```jinja2
{%- if is_scenario_onearm_bfd -%}
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
        {#- --- 条件必选：ADDRTYPE=IPv6 时必选 --- -#}
        {%- if item.ADDRTYPE == 'IPv6' -%}
            CREATETYPE6={{item.CREATETYPE6}},
        {%- endif -%}
        {#- --- 条件必选：ADDRTYPE=IPv6 时必选 --- -#}
        {%- if item.ADDRTYPE == 'IPv6' -%}
            DESTADDR6="{{item.DESTADDR6}}",
        {%- endif -%}
        {#- --- 条件必选：ONEARMECHO=FALSE 时必选 --- -#}
        {%- if item.ONEARMECHO == 'FALSE' -%}
            REMOTEDISCR={{item.REMOTEDISCR}},
        {#- --- 条件必选：ONEARMECHO6=FALSE 时必选 --- -#}
        {%- elif item.ONEARMECHO6 == 'FALSE' -%}
            REMOTEDISCR={{item.REMOTEDISCR}},
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
        {#- --- 条件可选：CREATETYPE6=SESS_STATIC 时可选 --- -#}
        {%- if item.CREATETYPE6 == 'SESS_STATIC' -%}
            {%- if item.ONEARMECHO6 is not none -%}
                ONEARMECHO6={{item.ONEARMECHO6}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：CREATETYPE4=SESS_STATIC 时可选 --- -#}
        {%- if item.CREATETYPE4 == 'SESS_STATIC' -%}
            {%- if item.TOSEXP is not none -%}
                TOSEXP={{item.TOSEXP}},
            {%- endif -%}
        {#- --- 条件可选：CREATETYPE6=SESS_STATIC 时可选 --- -#}
        {%- elif item.CREATETYPE6 == 'SESS_STATIC' -%}
            {%- if item.TOSEXP is not none -%}
                TOSEXP={{item.TOSEXP}},
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
        {#- --- IPv4源地址: 条件必选(IPv4会话创建方式=SESS_AUTO) / 条件可选(IPv4单臂Echo=TRUE|FALSE) --- -#}
        {%- if (item.CREATETYPE4 == 'SESS_AUTO') -%}
            SRCADDR4="{{item.SRCADDR4}}",
        {%- elif (item.ONEARMECHO in ['TRUE', 'FALSE']) -%}
            {%- if item.SRCADDR4 is not none -%}
                SRCADDR4="{{item.SRCADDR4}}",
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 5 配置静态路由并绑定BFD会话。

#### 5.1 //静态配置外联口IP地址时：

```jinja2
{%- if is_scenario_static_external_ip -%}
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
        {%- if item.DHCPENABLE is not none -%}
            DHCPENABLE={{item.DHCPENABLE}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 5.2 //DHCP获取外联口IP地址时：

```jinja2
{%- if is_scenario_dhcp_external_ip -%}
    {%- for item in add_srroute_list_8 -%}
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
        {%- if item.DHCPENABLE is not none -%}
            DHCPENABLE={{item.DHCPENABLE}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 如果需要为静态路由绑定静态BFD会话，通过**ADD SRROUTE**的“静态BFD会话名”来指定静态路由所联动的静态BFD的会话名。

#### 在网关侧配置到VNF的回程路由，目的地址为VNF上各逻辑接口的IP地址，下一跳为VNF上配置的各逻辑接口对应的外联口的IP地址。

#### 需要说明的是，配置VNF与DN/PDN通信的回程路由时，目的地址为UE的网段地址，下一跳为VNF上外联口的IP地址。


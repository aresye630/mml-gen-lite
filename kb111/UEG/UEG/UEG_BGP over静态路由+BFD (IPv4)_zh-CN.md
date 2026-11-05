---
id: ''
name: BGP over静态路由+BFD (IPv4)
ne_type: UEG
type: feature
description: SDN场景，VNF和DC-GW间通过Loopback IP建立eBGP邻居，用于业务路由的学习和发布。Loopback IP之间通过静态路由互通。  如图1所示为VNF与周边网元的静态路由互通组网示意图。VNF与网关运行BGP over静态路由协议而接入运营商网络/企业网络，DC-GW作网关。VNF和DC-GW之间采用单臂BFD探测。DC-GW的配置请参考对应型号设备的产品文档。  **图1** 静态路由+BFD组网
tags: []
risk_level: ''
doc_source: ["网络部署","园区入驻+地市共享（连接+计算）","5GC toB 部署边缘站点（站点为“风筝S”，带计算）","UEG初始配置（风筝S）","初始配置与调测（MPF）","初始配置与调测（MPF，SDN）","参考：详细配置指导","组网路由配置（独立部署）","配置VNF侧IP路由（SDN）","BGP over静态路由+BFD (IPv4)"]
refs: []
metadata:
  DepOnLiveCfg: true
allowed-tools:
- getParameterValue('LST AUTOCONFIG')
---
<!-- @mml:block= annotations -->
```text
## 操作场景
SDN场景，VNF和DC-GW间通过Loopback IP建立eBGP邻居，用于业务路由的学习和发布。Loopback IP之间通过静态路由互通。如图1所示为VNF与周边网元的静态路由互通组网示意图。VNF与网关运行BGP over静态路由协议而接入运营商网络/企业网络，DC-GW作网关。VNF和DC-GW之间采用单臂BFD探测。DC-GW的配置请参考对应型号设备的产品文档。**图1** 静态路由+BFD组网

## 必备事项
前提条件

* 请阅读并熟悉特性IPFD-014003 静态路由、IPFD-014002 支持BGP特性概述和IPFD-104403 BFD特性概述。
* 具备管理员权限的操作人员已经登录华为操作维护系统。
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
          description: 'VPN实例全网统一规划，一条通信路径上所有节点绑定的VPN实例要一致，才能正常通信。'
          data_source: '参见“5G Core LLD文档 > 业务IP对接设计 > VRF”。  请选中“虚拟机类型”为“ISU”/“ISU\_Cxx”且“子端口”为“vNICx.xxxx”的所有行，查找指定“逻辑接口”对应的“VRF”。逻辑接口包括Mp1、Mp2、Nxua、N6x等接口。此处以Mp1为例。'
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
          name: '地址族名称'
          type: string
          enum:
          - ipv4uni
          - ipv6uni
          required: true
          description: 'IPv4组网场景下，该参数选择ipv4uni。'
          data_source: ''
          pattern: ''
          default: ''
        VRFRD:
          name: '路由标识'
          type: string
          maxLength: 21
          required: false
          description: '不同VPN实例的路由标识必须不同。'
          data_source: '参见“5G Core LLD文档 > 路由设计 > VRF设计”。  请查找指定“3GPP接口”对应的“RD值（VNF）”。“3GPP接口”包括Mp1、Mp2、Nxua、N6x等接口。此处以Mp1为例。'
          pattern: ''
          default: ''
    mod_vpninstaf_list:
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
    set_bfd_list:
      type: items
      properties:
        BFDENABLE:
          name: 'BFD使能标志'
          type: string
          enum:
          - TRUE
          - FALSE
          required: true
          description: '参数“DELAYUPTIMER”（会话延迟UP时间）和“TOSEXP”（动态会话报文优先级）可以不用配置，使用默认值即可。'
          data_source: '参见“5G Core LLD文档 > 路由设计 > BFD设计 > BFD是否使能”。'
          pattern: ''
          default: ''
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
    add_autoscalingservice_list:
      type: items
      properties:
        SERVICENAME:
          name: '服务名称'
          type: string
          maxLength: 31
          required: true
          description: '需要规划3个VLAN平面，每个VLAN平面一条数据。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        VPNNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: '已规划数据中获取'
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
          data_source: '已规划数据中获取'
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
          data_source: '固定取值'
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
          data_source: '固定取值'
          pattern: ''
          default: VNIC
        VNICID:
          name: '虚拟网卡ID'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
        VLANID:
          name: 'VLAN ID'
          type: integer
          minimum: 0
          maximum: 4094
          required: false
          description: ''
          data_source: '参见“5G Core LLD文档 > 业务IP对接设计 > VLAN ID（VM）”。  请选中“虚拟机类型”为“ISU”/“ISU\_Cxx”且“子端口”为“vNICx.xxxx”的所有行，查找指定“逻辑接口”对应的“VLAN ID（VM）”。逻辑接口包括Mp1、Mp2、Nxua、N6x等接口。此处以Mp1为例。'
          pattern: ''
          default: 0
    add_autoscalingbfd_list:
      type: items
      properties:
        TEMPLATENAME:
          name: '模板名称'
          type: string
          maxLength: 59
          required: true
          description: '参数“DESTADDR4”是网关的接口IP，此处用于检测目的IP能否正常接收报文。'
          data_source: '本端规划'
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
          data_source: '固定取值'
          pattern: ''
          default: ''
        SERVICENAME:
          name: '服务名称'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        IPVERSION:
          name: '地址族'
          type: string
          enum:
          - IPv4
          - IPv6
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
        DESTADDR4:
          name: '目的地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '参见“5G Core LLD文档 > 路由设计 > BFD设计 > 对端IP地址”。'
          pattern: ''
          default: ''
        MINECHORXINT:
          name: '单臂Echo会话的收包间隔（ms）'
          type: integer
          minimum: 30
          maximum: 1000
          required: false
          description: ''
          data_source: '参见“5G Core LLD文档 > 路由设计 > BFD设计 > min-rx-interval(毫秒)”。'
          pattern: ''
          default: 200
        DETECTMULTI:
          name: '检测倍数'
          type: integer
          minimum: 3
          maximum: 50
          required: false
          description: ''
          data_source: '参见“5G Core LLD文档 > 路由设计 > BFD设计 > detect-multiplier”。'
          pattern: ''
          default: 3
        ONEARMECHO:
          name: '单臂Echo'
          type: string
          enum:
          - TRUE
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: TRUE
    add_autoscalingsrroute_list:
      type: items
      properties:
        SERVICENAME:
          name: '服务名称'
          type: string
          required: false
          description: '3个路由下一跳IP地址在不同网段。  参数“PREFIX4”是目的IP，规划的是用于传输Mp1接口报文时：  * 静态路由场景，此处是APP的IP地址。 * eBGP over 静态路由场景，此处是BGP Peer的IP地址。  参数“NEXTHOP4”是网关的接口IP。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          required: false
          description: ''
          data_source: '参见“5G Core LLD文档 > 路由设计 > 静态路由设计 > 本端VRF名称”。'
          pattern: ''
          default: ''
        IPVERSION:
          name: 'IPVERSION'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PREFIX4:
          name: '路由前缀IPv4'
          type: string
          required: false
          description: ''
          data_source: '参见“5G Core LLD文档 > 路由设计 > BGP设计 > Local interface address（L3GW）”。'
          pattern: ''
          default: ''
        MASKLENGTH:
          name: '路由掩码长度'
          type: string
          required: false
          description: ''
          data_source: '参见“5G Core LLD文档 > 路由设计 > 静态路由设计 > 子网掩码/掩码长度”。'
          pattern: ''
          default: ''
        NEXTHOPALLOCTYPE4:
          name: 'IPv4路由下一跳分配方式'
          type: string
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
        PREFERENCE:
          name: 'PREFERENCE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        BFDENABLE:
          name: 'BFD使能标识'
          type: string
          required: false
          description: '开启BFD探测时，必须设置为“TRUE”。'
          data_source: '参见“5G Core LLD文档 > 路由设计 > BFD设计 > BFD是否使能”。'
          pattern: ''
          default: ''
        BFDTEMPLATENAME:
          name: 'BFD模板名称'
          type: string
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        BBFDENABLE:
          name: 'BBFDENABLE'
          type: string
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
    set_bgp_list:
      type: items
      properties:
        BGPENABLE:
          name: '使能BGP'
          type: string
          enum:
          - FALSE
          - TRUE
          required: true
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
        ASNUM:
          name: 'BGP自治域号'
          type: string
          maxLength: 11
          required: false
          description: ''
          data_source: '参见“5G Core垂直网设LLD文档 > 路由设计 > BGP设计”'
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
          data_source: '参见“5G Core垂直网设LLD文档 > 路由设计 > BGP设计”'
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
          description: '此处的VPN实例已经配置，与外联口绑定的VPN实例相同。'
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
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IFIPADDR:
          name: 'IPv4地址'
          type: string
          maxLength: 15
          required: true
          description: '如果规划Loopback接口使用IPv4v6双栈地址，则分别执行**ADD IFIPV4ADDRESS**和**ADD IFIPV6ADDRESS**对同一Loopback接口配置IPv4和IPv6地址。'
          data_source: '参见“5G Core垂直网设LLD文档 > 路由设计 > BGP设计”'
          pattern: ''
          default: ''
        SUBNETMASK:
          name: 'IPv4地址掩码'
          type: string
          maxLength: 15
          required: true
          description: ''
          data_source: '固定取值'
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
          description: 'BGP VPN实例需要与Loopback接口绑定的VPN实例名一致。'
          data_source: '已配置数据中获取'
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
          data_source: '固定取值'
          pattern: ''
          default: ipv4uni
        ROUTERID:
          name: '路由器ID'
          type: string
          maxLength: 15
          required: false
          description: '不同BGP VPN实例的ROUTERID不能重复。'
          data_source: '参见“5G Core垂直网设LLD文档 > 路由设计 > BGP设计”'
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
          description: '使用**ADD BGPVRF**命令中的VPN实例名称。'
          data_source: '已配置数据中获取'
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
          data_source: '本端规划'
          pattern: ''
          default: ''
        MAXIMUMLOADBALANCE:
          name: '最大等价路由数'
          type: integer
          minimum: 1
          maximum: 128
          required: false
          description: '负荷分担关系的BGP PEER数。'
          data_source: '本端规划'
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
          data_source: '已配置数据中获取'
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
          description: 'DC-GW上的BGP Loopback IP地址及AS号。'
          data_source: '参见“5G Core垂直网设LLD文档 > 路由设计 > BGP设计”'
          pattern: ''
          default: ''
        REMOTEAS:
          name: '对等体AS号'
          type: string
          maxLength: 11
          required: false
          description: ''
          data_source: '参见“5G Core垂直网设LLD文档 > 路由设计 > BGP设计”'
          pattern: ''
          default: ''
        LOCALIFADDR:
          name: '本地接口地址'
          type: string
          maxLength: 39
          required: false
          description: 'VNF的Loopback IP地址及Loopback接口名称。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        LOCALIFNAME:
          name: '本地接口名称'
          type: string
          maxLength: 63
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        EBGPMAXHOP:
          name: 'EBGP最大跳数'
          type: integer
          minimum: 1
          maximum: 255
          required: false
          description: '“EBGP最大跳数”必须不小于到Peer之间的实际跳数。  如最大跳数设置过小，会导致BGP邻居建立失败。'
          data_source: '本端规划'
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
          data_source: '已配置数据中获取'
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
          data_source: '参见“5G Core垂直网设LLD文档 > 路由设计 > BGP设计”'
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
  examples:
    add_l3vpninst_list:
    - VRFNAME: 'VRF_Mp1'
    add_vpninstaf_list:
    - VRFNAME: 'VRF_Mp1'
      AFTYPE: ipv4uni
      VRFRD: '10.10.10.78'
    mod_vpninstaf_list:
    - VRFNAME: 'VRF_Mp1'
      AFTYPE: ipv4uni
      VRFRD: '10.10.10.78:100'
    set_bfd_list:
    - BFDENABLE: TRUE
    set_autoconfig_list:
    - SWITCHFLAG: FALSE
    add_autoscalingservice_list:
    - SERVICENAME: 'ServName_Mp1_100_v4'
      VPNNAME: 'VRF_Mp1'
      AFTYPE: IPv4
      IPALLOCTYPE4: DHCP
      AUTOCFGIFTYPE: VNIC
      VNICID: 4
      VLANID: 100
    add_autoscalingbfd_list:
    - TEMPLATENAME: 'BFD_Mp1_1_v4'
      BFDTYPE: Static
      SERVICENAME: 'ServName_Mp1_100_v4'
      IPVERSION: IPv4
      DESTADDR4: '192.168.89.1'
      MINECHORXINT: 500
      DETECTMULTI: 4
      ONEARMECHO: TRUE
    add_autoscalingsrroute_list:
    - SERVICENAME: ServName_Mp1_100_v4
      VRFNAME: VRF_Mp1
      IPVERSION: IPv4
      PREFIX4: 10.10.20.78
      MASKLENGTH: '32'
      NEXTHOPALLOCTYPE4: DHCP
      PREFERENCE: '60'
      BFDENABLE: TRUE
      BFDTEMPLATENAME: BFD_Mp1_1_v4
      BBFDENABLE: TRUE
    set_autoconfig_list_1:
    - SWITCHFLAG: TRUE
    set_bgp_list:
    - BGPENABLE: TRUE
      ASNUM: '60001'
    add_interface_list:
    - IFNAME: 'Loopback1'
    add_ipbindvpn_list:
    - IFNAME: 'Loopback1'
      VRFNAME: 'VRF_Mp1'
    add_ifipv4address_list:
    - IFNAME: 'Loopback1'
      IFIPADDR: '10.10.10.78'
      SUBNETMASK: '255.255.255.255'
    add_bgpvrf_list:
    - VRFNAME: 'VRF_Mp1'
      DEFAULTAFTYPE: noaf
      ROUTERID: '10.10.10.78'
    add_bgpvrfaf_list:
    - VRFNAME: 'VRF_Mp1'
      AFTYPE: ipv4uni
      MAXIMUMLOADBALANCE: 2
    add_bgppeer_list:
    - VRFNAME: 'VRF_Mp1'
      ADDRESSTYPE: ipv4
      PEERADDR: '10.10.20.78'
      REMOTEAS: '60002'
      LOCALIFADDR: '10.10.10.78'
      LOCALIFNAME: 'Loopback1'
      EBGPMAXHOP: 10
    add_importroute_list:
    - VRFNAME: 'VRF_Mp1'
      AFTYPE: ipv4uni
      IMPORTPROTOCOL: wlr
      MEDENABLE: FALSE
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
    {#- --- 可选参数 --- -#}
    {%- if item.VRFRD is not none -%}
        VRFRD="{{item.VRFRD}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in mod_vpninstaf_list -%}
    MOD VPNINSTAF:
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

### 一条通信路径上所有节点绑定的VPN实例要一致，才能正常通信，例如VNF逻辑接口、VNF外联口、BGP相关的VPN，否则从逻辑接口发出去的报文会查询路由失败。

### 2 全局激活BFD。

```jinja2
{%- for item in set_bfd_list -%}
    SET BFD:
    {#- --- 必选参数 --- -#}
    BFDENABLE={{item.BFDENABLE}},
    ;
{%- endfor -%}
```

### 3 关闭自动配置开关。

#### 3.1 查询自动配置开关。

#### 如果“自动配置开关”值为“TRUE”，需要执行3.b和3.c关闭自动配置开关。

#### 如果“自动配置开关”值为“FALSE”，说明已关闭自动配置开关，请跳转到4。

#### 3.2 查询自动部署维护助手“autoscaling\_autoconfig.py”的状态，确保状态为“准备好状态（Ready）”或者查询无该脚本，以保证当前设备不在自动部署过程中。因为若系统当前有正在进行的自动部署，而自动部署生效有时延，此时若关闭自动配置开关，会影响系统配置效果。

#### 3.3 关闭自动配置开关。自动化配置命令只有在自动配置开关为关闭的状态下才可执行，因此需要提前关闭。

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

### 4 配置外联口自动化配置模板。

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
    {#- --- 条件必选：AUTOCFGIFTYPE=VNIC 时必选 --- -#}
    {%- if item.AUTOCFGIFTYPE == 'VNIC' -%}
        VNICID={{item.VNICID}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：AFTYPE=IPv4 时可选 --- -#}
    {%- if item.AFTYPE == 'IPv4' -%}
        {%- if item.IPALLOCTYPE4 is not none -%}
            IPALLOCTYPE4={{item.IPALLOCTYPE4}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 5 增加BFD会话自动部署模板。

### “DESTADDR4”配置的是Leaf节点的IP地址，采用的是单臂BFD。

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

### 6 增加静态路由自动部署模板。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_autoscalingsrroute_list的变量区（command: ADD AUTOSCALINGSRROUTE） -#}
<!-- MISSING_MACRO: command=ADD AUTOSCALINGSRROUTE list_name=add_autoscalingsrroute_list step_id=6 -->
```

### 7 打开自动配置开关。

```jinja2
{%- for item in set_autoconfig_list_1 -%}
    SET AUTOCONFIG:
    {#- --- 必选参数 --- -#}
    SWITCHFLAG={{item.SWITCHFLAG}},
    ;
{%- endfor -%}
```

### 从自动部署开关打开到自动部署功能生效有时延，因此执行其他操作前（例如手动部署路由互通、关闭自动部署开关），务必先执行**DSP OPSASSISTSTATE**命令查询自动部署维护助手“autoscaling\_autoconfig.py”的状态为“准备好状态（Ready）”，否则结果不可预期。

### 在网关侧上配置到VNF的回程路由，目的地址为VNF上各逻辑接口的IP地址，下一跳为VNF上配置的各逻辑接口对应的外联口的IP地址。

### 需要说明的是，配置VNF与DN/PDN通信的回程路由时，目的地址为UE的网段地址。下一跳为VNF上外联口的IP地址，由于自动部署时外联口的IP地址是系统自动分配的，因此建议首先通过命令**LST IFIPV4ADDRESS**查看外联口的IP地址。

### 8 全局激活BGP。

```jinja2
{%- for item in set_bgp_list -%}
    SET BGP:
    {#- --- 必选参数 --- -#}
    BGPENABLE={{item.BGPENABLE}},
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：BGPENABLE=TRUE 时可选 --- -#}
    {%- if item.BGPENABLE == 'TRUE' -%}
        {%- if item.ASNUM is not none -%}
            ASNUM="{{item.ASNUM}}",
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### “ASNUM”参数若需要变更，则需先去使能BGP功能。去使能BGP时，BGP VPN实例等配置会被同步删除。必须按照LLD规划的“ASNUM”值进行配置。

### 9 配置Loopback接口地址（BGP本端IP）。

#### 9.1 配置Loopback接口。

```jinja2
{%- for item in add_interface_list -%}
    ADD INTERFACE:
    {#- --- 必选参数 --- -#}
    IFNAME="{{item.IFNAME}}",
    ;
{%- endfor -%}
```

#### 9.2 配置接口绑定VPN。

```jinja2
{%- for item in add_ipbindvpn_list -%}
    ADD IPBINDVPN:
    {#- --- 必选参数 --- -#}
    IFNAME="{{item.IFNAME}}",
    VRFNAME="{{item.VRFNAME}}",
    ;
{%- endfor -%}
```

#### 9.3 配置接口IP地址。

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

### 10 配置BGP。

#### 10.1 增加BGP VPN实例。

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

#### 此处配置的“ROUTERID”是BGP VPN实例级别的ROUTERID。

#### IPv4v6双栈时，IPv4 BGP VPN实例地址族和IPv6 BGP VPN实例地址族共用此处配置的“ROUTERID”值。

#### 已配置IPv4v6双栈的BGP VPN实例地址族，若需删除IPv4的BGP VPN实例地址族配置，则：

#### 1、删除IPv4的配置前需查询并记录“ROUTERID”值。

#### 2、删除IPv4的配置后需查询“ROUTERID”值是否存在，若不存在则需通过**MOD BGPVRF**命令将“ROUTERID”参数设置为删除IPv4的配置前记录的“ROUTERID”值。否则IPv6 BGP重新协商时会因无“ROUTERID”值可用而导致协商失败。

#### 10.2 增加BGP VPN地址族。VNF对接2个负荷分担的BGP邻居时，“MAXIMUMLOADBALANCE”设置为“2”。

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

#### 10.3 增加BGP对等体。

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

#### 10.4 增加BGP引入路由。

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

#### 由于BGP协议自身不能发现路由，所以需要引入其他协议的路由（如OSPF、静态路由或WLR等）注入到BGP路由表中，从而将这些路由在AS之内和AS之间传播。


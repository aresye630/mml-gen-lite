---
id: ''
name: 配置动态路由OSPF（IPv4）
ne_type: UEG
type: feature
description: 网关设备（如FW）不支持BFD时，UEG与对端设备可通过OSPF动态路由进行组网连接，该方式适用于IPv4组网的网络中。  图1是UEG与周边网元通过OSPF动态路由互通的组网示意。UEG与网关设备（如FW）运行动态路由协议而接入企业网络，UEG的配置请参考本页面，FW的配置请参考FW对应型号设备的产品文档。  **图1** OSPF动态路由组网
tags: []
risk_level: ''
doc_source:
  - ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（电力专网，入驻式）","软件安装与初始配置","部署UEG","电力专网采用风筝S部署模式","UEG初始配置","裸机容器模式UPF初始配置","参考：详细配置指导","组网路由配置","配置VNF侧IP路由数据","配置动态路由OSPF（IPv4）"]
  - ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（火电专网，入驻式）","部署配置指导","子园区部署入驻式UEG-S","子园区UEG-S初始配置","裸机容器模式UPF初始配置","参考：详细配置指导","组网路由配置","配置VNF侧IP路由数据","配置动态路由OSPF（IPv4）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools:
- getParameterValue('ADD OSPFAREA')
---
<!-- @mml:block= annotations -->
```text
## 操作场景
网关设备（如FW）不支持BFD时，UEG与对端设备可通过OSPF动态路由进行组网连接，该方式适用于IPv4组网的网络中。图1是UEG与周边网元通过OSPF动态路由互通的组网示意。UEG与网关设备（如FW）运行动态路由协议而接入企业网络，UEG的配置请参考本页面，FW的配置请参考FW对应型号设备的产品文档。**图1** OSPF动态路由组网

## 必备事项
前提条件

* 请阅读并熟悉特性IPFD-020501 支持OSPF特性概述。
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
          description: '请参考外联口介绍(机架服务器-ARM)/外联口介绍(刀片式服务器2U)进行规划。'
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
          description: '免交换场景，使用非SR-IOV bonding组网，此处规划的是Ethernet子接口。'
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
          data_source: '已规划数据中获取'
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
          description: '此处以双平面为例。'
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
          data_source: '已规划数据中获取'
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
    add_ospf_list:
      type: items
      properties:
        PROCID:
          name: 'OSPF进程号'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        VRFNAME:
          name: 'VPN的名称'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: '_public_'
        SCHEMAROUID:
          name: 'Schema路由器标识'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        BFDALLINTFFLG:
          name: '使能BFD'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: '三层路由设备FW不支持BFD时，使用样例值。'
          data_source: '全网规划'
          pattern: ''
          default: FALSE
        LSAARRINTVFLAG:
          name: '取消使用智能定时器配置LSA接收的间隔时间'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        LSAARRMAXINTV:
          name: '接收最长间隔时间（ms）'
          type: integer
          minimum: 1
          maximum: 10000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 1000
        LSAARRSTARINTV:
          name: '接收初始间隔时间（ms）'
          type: integer
          minimum: 0
          maximum: 1000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 500
        LSAARRHLDINTV:
          name: '接收基数间隔时间（ms）'
          type: integer
          minimum: 1
          maximum: 5000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 500
        VPNINSCAPSIMFLG:
          name: '去使能VPN路由环路检测'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        VIRTUALSYSFLAG:
          name: 'OSPF共网段虚拟系统使能标志'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: TRUE
    add_ospfarea_list:
      type: items
      properties:
        PROCID:
          name: '进程号'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AREAID:
          name: '区域号'
          type: string
          maxLength: 15
          required: true
          description: '两个接口若要建立邻居关系，则Area ID必须相同。'
          data_source: '与对端协商'
          pattern: ''
          default: ''
        AREATYPE:
          name: '区域类型'
          type: string
          enum:
          - NSSA
          - Normal
          - Stub
          required: false
          description: '两个接口若要建立邻居关系，则Area Type必须相同。'
          data_source: '与对端协商'
          pattern: ''
          default: Normal
        MAXCOSTFLAG:
          name: '保持最大开销值标志'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
    add_ospfareaauth_list:
      type: items
      properties:
        PROCID:
          name: 'OSPF进程号'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AREAID:
          name: '区域号'
          type: string
          maxLength: 15
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AUTHENMODE:
          name: '认证模式'
          type: string
          enum:
          - hmac-md5
          - hmac-sha256
          - keychain
          - md5
          - simple
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_ospfinterface_list:
      type: items
      properties:
        PROCID:
          name: 'OSPF进程号'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: true
          description: '-'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        AREAID:
          name: '区域标识'
          type: string
          maxLength: 15
          required: true
          description: ''
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        IFNAME:
          name: '接口名称'
          type: string
          maxLength: 63
          required: true
          description: '子接口名称。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        DRPRI:
          name: '指定路由器优先级'
          type: integer
          minimum: 0
          maximum: 255
          required: false
          description: '“DRPRI”设置为“0”表示不参与DR和BDR的选举。为避免UEG被选为DR或BDR，建议将VNF“DRPRI”配置为0，对端配置为非0。'
          data_source: '-'
          pattern: ''
          default: 1
        VIRTUALSYSFLAG:
          name: 'OSPF共网段虚拟系统使能标志'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: '-'
          data_source: '-'
          pattern: ''
          default: FALSE
        CFGROUTERIDFLAG:
          name: 'OSPF虚Router-id配置标志'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        MAXCOSTFLAG:
          name: '保持最大开销值标志'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
    add_ospfnetwork_list:
      type: items
      properties:
        PROCID:
          name: 'OSPF进程号'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: true
          description: '“IPADDRESS”和“WILDCARDMASK”是在指定OSPF区域内的外联口所在的网段。  “WILDCARDMASK”是反掩码，相当于把IP地址的掩码反转（0变1，1变0）。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        AREAID:
          name: '区域号'
          type: string
          maxLength: 15
          required: true
          description: ''
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        IPADDRESS:
          name: '网段IP地址'
          type: string
          maxLength: 15
          required: true
          description: ''
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        WILDCARDMASK:
          name: '反掩码'
          type: string
          maxLength: 15
          required: true
          description: ''
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
    add_ospfinterfaceauth_list:
      type: items
      properties:
        PROCID:
          name: 'OSPF进程号'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AREAID:
          name: '区域号'
          type: string
          maxLength: 15
          required: true
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
        AUTHENMODE:
          name: '认证模式'
          type: string
          enum:
          - hmac-md5
          - hmac-sha256
          - keychain
          - md5
          - 'null'
          - simple
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_ospfinterfaceauth_list_1:
      type: items
      properties:
        PROCID:
          name: 'OSPF进程号'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AREAID:
          name: '区域号'
          type: string
          maxLength: 15
          required: true
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
        AUTHENMODE:
          name: '认证模式'
          type: string
          enum:
          - hmac-md5
          - hmac-sha256
          - keychain
          - md5
          - 'null'
          - simple
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_ospfimportroute_list:
      type: items
      properties:
        PROCID:
          name: 'OSPF进程号'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: true
          description: '-'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        TOPOID:
          name: '拓扑标识'
          type: integer
          minimum: 0
          maximum: 0
          required: false
          description: ''
          data_source: '-'
          pattern: ''
          default: 0
        PROTOCOL:
          name: '协议分类'
          type: string
          enum:
          - BGP
          - Direct
          - OSPF
          - Static
          - wlr
          required: true
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
        IMPTCOSTCFG:
          name: '引入路由开销值配置'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: '2个UPF是主备时，设置为“TRUE”；2个UPF是负荷分担关系时，设置为“FALSE”。'
          data_source: '本端规划'
          pattern: ''
          default: FALSE
        IMPTTAGCFG:
          name: '引入路由标签配置'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        IMPTTYPECFG:
          name: '引入路由类型配置'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        COST:
          name: '路径Cost值'
          type: integer
          minimum: 0
          maximum: 16777214
          required: false
          description: '主备UPF引入路由的COST值。主UPF设置的COST值必须小于备UPF设置的COST值。'
          data_source: '与对端协商'
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
          description: 'Loopback接口数据。  **ADD OSPFAREA**命令中的“区域类型(AREATYPE)”为“NSSA”时需要规划；“区域类型(AREATYPE)”为“Normal”时不需要规划。'
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
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        VRFNAME:
          name: 'VPN的名称'
          type: string
          maxLength: 31
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
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        IFIPADDR:
          name: '接口IPv4地址'
          type: string
          maxLength: 15
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        SUBNETMASK:
          name: '接口IPv4地址掩码'
          type: string
          maxLength: 15
          required: true
          description: ''
          data_source: '固定取值'
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
    add_ospfinterface_list_2:
      type: items
      properties:
        PROCID:
          name: 'OSPF进程号'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: true
          description: ''
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        AREAID:
          name: '区域号'
          type: string
          maxLength: 15
          required: true
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
    add_ospfnetwork_list_2:
      type: items
      properties:
        PROCID:
          name: 'OSPF进程号'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: true
          description: '“IPADDRESS”和“WILDCARDMASK”是在指定OSPF区域内的外联口所在的网段。  “WILDCARDMASK”是反掩码，相当于把IP地址的掩码反转（0变1，1变0）。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        AREAID:
          name: '区域号'
          type: string
          maxLength: 15
          required: true
          description: ''
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        IPADDRESS:
          name: '网段IP地址'
          type: string
          maxLength: 15
          required: true
          description: ''
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        WILDCARDMASK:
          name: '反掩码'
          type: string
          maxLength: 15
          required: true
          description: ''
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
  examples:
    add_l3vpninst_list:
    - VRFNAME: 'VPN_LocalDN'
    add_vpninstaf_list:
    - VRFNAME: 'VPN_LocalDN'
      AFTYPE: ipv4uni
    mod_interface_list:
    - IFNAME: 'Ethernet64/0/6'
      IFADMINSTATUS: up
    add_interface_list:
    - IFNAME: 'Ethernet64/0/6.1'
    add_ipbindvpn_list:
    - IFNAME: 'Ethernet64/0/6.1'
      VRFNAME: 'VPN_LocalDN'
    add_ethsubif_list:
    - IFNAME: 'Ethernet64/0/6.1'
      VLANTYPEVID: 100
    add_ifipv4address_list:
    - IFNAME: 'Ethernet64/0/6.1'
      IFIPADDR: '192.168.89.2'
      SUBNETMASK: '255.255.255.248'
    add_ospf_list:
    - PROCID: 6
      VRFNAME: 'VPN_LocalDN'
      SCHEMAROUID: '192.168.35.210'
      BFDALLINTFFLG: FALSE
      LSAARRINTVFLAG: FALSE
      LSAARRMAXINTV: 1000
      LSAARRSTARINTV: 500
      LSAARRHLDINTV: 500
      VPNINSCAPSIMFLG: TRUE
      VIRTUALSYSFLAG: TRUE
    add_ospfarea_list:
    - PROCID: 6
      AREAID: '0.0.0.5'
      AREATYPE: Normal
      MAXCOSTFLAG: FALSE
    add_ospfareaauth_list:
    - PROCID: 进程号
      AREAID: '区域号'
      AUTHENMODE: 认证模式
    add_ospfinterface_list:
    - PROCID: 6
      AREAID: '0.0.0.5'
      IFNAME: 'Ethernet64/0/6.1'
      DRPRI: 0
      VIRTUALSYSFLAG: TRUE
      CFGROUTERIDFLAG: FALSE
      MAXCOSTFLAG: FALSE
    add_ospfnetwork_list:
    - PROCID: 6
      AREAID: '0.0.0.5'
      IPADDRESS: '192.168.89.0'
      WILDCARDMASK: '0.0.0.7'
    add_ospfinterfaceauth_list:
    - PROCID: 进程号
      AREAID: '区域号'
      IFNAME: '接口名称'
      AUTHENMODE: 'null'
    add_ospfinterfaceauth_list_1:
    - PROCID: 进程号
      AREAID: '区域号'
      IFNAME: '接口名称'
      AUTHENMODE: 认证模式
    add_ospfimportroute_list:
    - PROCID: 6
      TOPOID: 0
      PROTOCOL: wlr
      IMPTCOSTCFG: FALSE
      IMPTTAGCFG: FALSE
      IMPTTYPECFG: FALSE
      COST: 100
    add_interface_list_2:
    - IFNAME: 'LoopBack605'
    add_ipbindvpn_list_2:
    - IFNAME: 'LoopBack605'
      VRFNAME: 'VPN_LocalDN'
    add_ifipv4address_list_2:
    - IFNAME: 'LoopBack605'
      IFIPADDR: '192.168.235.130'
      SUBNETMASK: '255.255.255.255'
      ADDRTYPE: main
    add_ospfinterface_list_2:
    - PROCID: 6
      AREAID: '0.0.0.5'
      IFNAME: 'LoopBack605'
    add_ospfnetwork_list_2:
    - PROCID: 6
      AREAID: '0.0.0.5'
      IPADDRESS: '192.168.235.130'
      WILDCARDMASK: '0.0.0.0'
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

### 2 配置外联口IP地址。

#### 2.1 查询接口名，确认可使用的外联口的接口类型和接口编号。

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

#### 2.6 配置外联口IP地址。

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

#### 如果规划外联口使用IPv4v6双栈地址，则分别执行**ADD IFIPV4ADDRESS**和**ADD IFIPV6ADDRESS**对同一外联口配置IPv4和IPv6地址。

### 3 配置OSPF路由数据。

#### 3.1 创建OSPF进程。

```jinja2
{%- for item in add_ospf_list -%}
    ADD OSPF:
    {#- --- 必选参数 --- -#}
    PROCID={{item.PROCID}},
    {#- --- 可选参数 --- -#}
    {%- if item.VRFNAME is not none -%}
        VRFNAME="{{item.VRFNAME}}",
    {%- endif -%}
    {%- if item.SCHEMAROUID is not none -%}
        SCHEMAROUID="{{item.SCHEMAROUID}}",
    {%- endif -%}
    {%- if item.BFDALLINTFFLG is not none -%}
        BFDALLINTFFLG={{item.BFDALLINTFFLG}},
    {%- endif -%}
    {%- if item.LSAARRINTVFLAG is not none -%}
        LSAARRINTVFLAG={{item.LSAARRINTVFLAG}},
    {%- endif -%}
    {%- if item.VPNINSCAPSIMFLG is not none -%}
        VPNINSCAPSIMFLG={{item.VPNINSCAPSIMFLG}},
    {%- endif -%}
    {%- if item.VIRTUALSYSFLAG is not none -%}
        VIRTUALSYSFLAG={{item.VIRTUALSYSFLAG}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：LSAARRINTVFLAG=FALSE 时必选 --- -#}
    {%- if item.LSAARRINTVFLAG == 'FALSE' -%}
        LSAARRMAXINTV={{item.LSAARRMAXINTV}},
    {%- endif -%}
    {#- --- 条件必选：LSAARRINTVFLAG=FALSE 时必选 --- -#}
    {%- if item.LSAARRINTVFLAG == 'FALSE' -%}
        LSAARRSTARINTV={{item.LSAARRSTARINTV}},
    {%- endif -%}
    {#- --- 条件必选：LSAARRINTVFLAG=FALSE 时必选 --- -#}
    {%- if item.LSAARRINTVFLAG == 'FALSE' -%}
        LSAARRHLDINTV={{item.LSAARRHLDINTV}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### UEG支持VPN多实例时，需要取消环路检查（参数“VPNINSCAPSIMFLG”配置为“TRUE”），否则会导致OSPF路由引入失败。

#### 路由器标识Router ID（“SCHEMAROUID”）的选择策略：优选用户配置的Router ID，如果未配置，则选择OSPF进程所在VRF内或者公网内的最大接口IP地址。

#### FW不支持BFD，参数“BFDALLINTFFLG（使能BFD）”配置为“FALSE”。

#### 当OSPF路由配置共网段时，需要将参数“VIRTUALSYSFLAG（OSPF共网段虚拟系统使能标志）”配置为“TRUE”。

#### 3.2 增加OSPF区域。

```jinja2
{%- for item in add_ospfarea_list -%}
    ADD OSPFAREA:
    {#- --- 必选参数 --- -#}
    PROCID={{item.PROCID}},
    AREAID="{{item.AREAID}}",
    {#- --- 可选参数 --- -#}
    {%- if item.AREATYPE is not none -%}
        AREATYPE={{item.AREATYPE}},
    {%- endif -%}
    {%- if item.MAXCOSTFLAG is not none -%}
        MAXCOSTFLAG={{item.MAXCOSTFLAG}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 3.3 **（可选）**配置OSPF区域认证。

```jinja2
{%- if is_optional_ospf_area_auth -%}
    {%- for item in add_ospfareaauth_list -%}
        ADD OSPFAREAAUTH:
        {#- --- 必选参数 --- -#}
        PROCID={{item.PROCID}},
        AREAID="{{item.AREAID}}",
        AUTHENMODE={{item.AUTHENMODE}},
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 参数“AUTHENMODE”（认证模式），选择“keychain”、“simple”、“md5”、“hmac-sha256”或“hmac-md5”。

#### 使用区域验证时，一个区域中所有设备的接口上所配置的认证模式和口令必须一致。

#### 3.4 配置OSPF协议的接口属性。

```jinja2
{%- for item in add_ospfinterface_list -%}
    ADD OSPFINTERFACE:
    {#- --- 必选参数 --- -#}
    PROCID={{item.PROCID}},
    AREAID="{{item.AREAID}}",
    IFNAME="{{item.IFNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.DRPRI is not none -%}
        DRPRI={{item.DRPRI}},
    {%- endif -%}
    {%- if item.VIRTUALSYSFLAG is not none -%}
        VIRTUALSYSFLAG={{item.VIRTUALSYSFLAG}},
    {%- endif -%}
    {%- if item.MAXCOSTFLAG is not none -%}
        MAXCOSTFLAG={{item.MAXCOSTFLAG}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：VIRTUALSYSFLAG=TRUE 时可选 --- -#}
    {%- if item.VIRTUALSYSFLAG == 'TRUE' -%}
        {%- if item.CFGROUTERIDFLAG is not none -%}
            CFGROUTERIDFLAG={{item.CFGROUTERIDFLAG}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 参数“NETWORKTYPE”（网络类型）选择“broadcast”、“nbma”、“p2p”或“p2mp”。

#### 广播或NBMA网络中，根据此接口优先级选举DR和BDR路由器，“优先级”设置为“0”表示不参与DR和BDR的选举。为避免UEG被选为DR或BDR，建议将VNF“优先级”配置为0，对端配置为非0。

#### 3.5 增加运行OSPF协议的接口。

```jinja2
{%- for item in add_ospfnetwork_list -%}
    ADD OSPFNETWORK:
    {#- --- 必选参数 --- -#}
    PROCID={{item.PROCID}},
    AREAID="{{item.AREAID}}",
    IPADDRESS="{{item.IPADDRESS}}",
    WILDCARDMASK="{{item.WILDCARDMASK}}",
    ;
{%- endfor -%}
```

#### 3.6 **（可选）**配置OSPF接口验证参数。

#### 根据不同的接口验证类型选择不同的配置。

##### 3.6.1 不配置认证模式。

```jinja2
{%- if is_optional_ospf_interface_auth and is_scenario_no_auth -%}
    {%- for item in add_ospfinterfaceauth_list -%}
        ADD OSPFINTERFACEAUTH:
        {#- --- 必选参数 --- -#}
        PROCID={{item.PROCID}},
        AREAID="{{item.AREAID}}",
        IFNAME="{{item.IFNAME}}",
        AUTHENMODE={{item.AUTHENMODE}},
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 3.6.2 配置认证模式。

```jinja2
{%- if is_optional_ospf_interface_auth and is_scenario_auth -%}
    {%- for item in add_ospfinterfaceauth_list_1 -%}
        ADD OSPFINTERFACEAUTH:
        {#- --- 必选参数 --- -#}
        PROCID={{item.PROCID}},
        AREAID="{{item.AREAID}}",
        IFNAME="{{item.IFNAME}}",
        AUTHENMODE={{item.AUTHENMODE}},
        ;
    {%- endfor -%}
{%- endif -%}
```

###### 3.6.2.1 参数“AUTHENMODE”（认证模式）可以选择“keychain”、“hmac-sha256”、“simple”、“md5”或“hmac-md5”。

###### 3.6.2.2 参数“IFNAME”（接口名称）采用3.d中的接口名称。

#### 3.7 设置OSPF引入路由类型。

```jinja2
{%- for item in add_ospfimportroute_list -%}
    ADD OSPFIMPORTROUTE:
    {#- --- 必选参数 --- -#}
    PROCID={{item.PROCID}},
    PROTOCOL={{item.PROTOCOL}},
    {#- --- 可选参数 --- -#}
    {%- if item.TOPOID is not none -%}
        TOPOID={{item.TOPOID}},
    {%- endif -%}
    {%- if item.IMPTCOSTCFG is not none -%}
        IMPTCOSTCFG={{item.IMPTCOSTCFG}},
    {%- endif -%}
    {%- if item.IMPTTAGCFG is not none -%}
        IMPTTAGCFG={{item.IMPTTAGCFG}},
    {%- endif -%}
    {%- if item.IMPTTYPECFG is not none -%}
        IMPTTYPECFG={{item.IMPTTYPECFG}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IMPTCOSTCFG=TRUE 时必选 --- -#}
    {%- if item.IMPTCOSTCFG == 'TRUE' -%}
        COST={{item.COST}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 **（可选）**3中**ADD OSPFAREA**命令的参数“AREATYPE（区域类型）”配置为“NSSA”时，设置Loopback接口。

### 如果参数“AREATYPE（区域类型）”配置为“NSSA”时，需要配置Loopback地址，这样设备会自动选取该Loopback地址作为FA。当有其他设备存在多条开销值相同的路径到NSSA设备时，可以形成负载分担。

#### 4.1 配置Loopback接口。

```jinja2
{%- set ADD_OSPFAREA=getParameterValue('ADD OSPFAREA') -%}
{%- if is_optional_loopback_interface and ADD_OSPFAREA -%}
    {%- for item in add_interface_list_2 -%}
        ADD INTERFACE:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 4.2 增加Loopback接口绑定VPN。

```jinja2
{%- if is_optional_loopback_interface and ADD_OSPFAREA -%}
    {%- for item in add_ipbindvpn_list_2 -%}
        ADD IPBINDVPN:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        VRFNAME="{{item.VRFNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 4.3 配置Loopback的IPv4地址。

```jinja2
{%- if is_optional_loopback_interface and ADD_OSPFAREA -%}
    {%- for item in add_ifipv4address_list_2 -%}
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

#### 4.4 使能Loopback接口到OSPF进程的区域下。

##### 4.4.1 通过**ADD OSPFINTERFACE**配置。

```jinja2
{%- if is_optional_loopback_interface and is_scenario_via_ospfinterface and ADD_OSPFAREA -%}
    {%- for item in add_ospfinterface_list_2 -%}
        ADD OSPFINTERFACE:
        {#- --- 必选参数 --- -#}
        PROCID={{item.PROCID}},
        AREAID="{{item.AREAID}}",
        IFNAME="{{item.IFNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 4.4.2 通过**ADD OSPFNETWORK**配置。

```jinja2
{%- if is_optional_loopback_interface and is_scenario_via_ospfnetwork and ADD_OSPFAREA -%}
    {%- for item in add_ospfnetwork_list_2 -%}
        ADD OSPFNETWORK:
        {#- --- 必选参数 --- -#}
        PROCID={{item.PROCID}},
        AREAID="{{item.AREAID}}",
        IPADDRESS="{{item.IPADDRESS}}",
        WILDCARDMASK="{{item.WILDCARDMASK}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 推荐使用**ADD OSPFINTERFACE**命令进行配置。使用**ADD OSPFNETWORK**命令配置时，请将“WILDCARDMASK(反掩码)”设置为“0.0.0.0”。

#### 参数“PROCID（进程号）”与3中的“PROCID（进程号）”的取值相一致；参数“AREAID（区域号）”与3中的“AREAID（区域号）”的取值相一致。


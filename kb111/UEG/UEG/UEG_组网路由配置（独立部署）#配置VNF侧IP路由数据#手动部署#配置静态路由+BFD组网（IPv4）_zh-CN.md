---
id: ''
name: 配置静态路由+BFD组网（IPv4）
ne_type: UEG
type: feature
description: VNF与对端设备可通过静态路由绑定静态BFD探测的方式进行组网连接。  在网络拓扑结构比较简单时，通常使用静态路由方式组网，合理的静态路由可以改进网络性能，并为业务保证带宽。同时，利用单臂Echo转发检测机制为链路提供单向、轻负荷且持续时间短的快速检测功能，提高链路可靠性。  如图1所示为VNF与周边网元的静态路由互通组网示意图。VNF与网关运行静态路由协议而接入运营商网络/企业网络，DC-GW作网关。VNF和DC-GW之间采用单臂BFD探测。DC-GW的配置请参考对应型号设备的产品文档。  **图1** 静态路由+BFD组网
tags: []
risk_level: ''
doc_source: ["网络部署","园区入驻+地市共享（连接+计算）","5GC toB 部署边缘站点（站点为“风筝S”，带计算）","UEG初始配置（风筝S）","初始配置与调测（MPF）","初始配置与调测（MPF，非SDN）","参考：详细配置指导","组网路由配置（独立部署）","配置VNF侧IP路由数据","手动部署","配置静态路由+BFD组网（IPv4）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
VNF与对端设备可通过静态路由绑定静态BFD探测的方式进行组网连接。在网络拓扑结构比较简单时，通常使用静态路由方式组网，合理的静态路由可以改进网络性能，并为业务保证带宽。同时，利用单臂Echo转发检测机制为链路提供单向、轻负荷且持续时间短的快速检测功能，提高链路可靠性。如图1所示为VNF与周边网元的静态路由互通组网示意图。VNF与网关运行静态路由协议而接入运营商网络/企业网络，DC-GW作网关。VNF和DC-GW之间采用单臂BFD探测。DC-GW的配置请参考对应型号设备的产品文档。**图1** 静态路由+BFD组网

## 必备事项
前提条件

* 请阅读并熟悉特性IPFD-020503 静态路由和IPFD-020403 BFD特性概述。

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
          data_source: '参见“5G Core LLD文档 > 业务IP对接设计 > 业务IP设计 > VLAN号”。'
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
          description: '如果规划外联口使用IPv4v6双栈地址，则分别执行**ADD IFIPV4ADDRESS**和**ADD IFIPV6ADDRESS**  对同一外联口配置IPv4和IPv6地址。  此处规划的IP地址是与网关互通的外联口IP。  此处以27位掩码为例进行介绍，具体以网设规划为准。'
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
          description: ''
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
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: false
          description: '-'
          data_source: '参见“5G Core LLD文档 > 路由设计 > BFD会话 > VPN实例名称”。'
          pattern: ''
          default: ''
        LOCALDISCR:
          name: '本地标识符'
          type: integer
          minimum: 1
          maximum: 16384
          required: false
          description: 'VNF上BFD会话的本地标识符，需要和对接网关上的标识符对应，即本端的本地标识符与对端网关侧的远端标识符相同。'
          data_source: '参见“5G Core LLD文档 > 路由设计 > BFD会话 > 本地标识符”。'
          pattern: ''
          default: ''
        IFNAME:
          name: '出接口名称'
          type: string
          maxLength: 63
          required: false
          description: '-'
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
    add_srroute_list:
      type: items
      properties:
        VRFNAME:
          name: 'VPN实例名称 '
          type: string
          maxLength: 31
          required: false
          description: '3个路由下一跳IP地址在不同网段。  参数“PREFIX4”是目的IP，规划的是用于传输Mp1接口报文时：  * 静态路由场景，此处是APP的IP地址。 * eBGP over 静态路由场景，此处是BGP Peer的IP地址。  参数“NEXTHOP”是网关的接口IP。'
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
          data_source: '已规划数据中获取'
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
  examples:
    add_l3vpninst_list:
    - VRFNAME: 'VRF_Mp1'
    add_vpninstaf_list:
    - VRFNAME: 'VRF_Mp1'
      AFTYPE: ipv4uni
    mod_interface_list:
    - IFNAME: 'Ethernet64/0/4'
      IFADMINSTATUS: up
    add_interface_list:
    - IFNAME: 'Ethernet64/0/4.1'
    add_ipbindvpn_list:
    - IFNAME: 'Ethernet64/0/4.1'
      VRFNAME: 'VRF_Mp1'
    add_ethsubif_list:
    - IFNAME: 'Ethernet64/0/4.1'
      VLANTYPEVID: 100
    add_ifipv4address_list:
    - IFNAME: 'Ethernet64/0/4.1'
      IFIPADDR: '192.168.89.2'
      SUBNETMASK: '255.255.255.224'
    set_bfd_list:
    - BFDENABLE: TRUE
    add_bfdsession_list:
    - SESSNAME: 'BfdName21'
      ADDRTYPE: IPv4
      CREATETYPE4: SESS_STATIC
      ONEARMECHO: TRUE
      DESTADDR4: '192.168.89.1'
      LINKTYPE: IP
      VRFNAME: 'VRF_Mp1'
      LOCALDISCR: 121
      IFNAME: 'Ethernet64/0/4.1'
      CREATETYPE6: ''
      ONEARMECHO6: FALSE
    add_srroute_list:
    - VRFNAME: 'VRF_Mp1'
      AFTYPE: ipv4unicast
      PREFIX: '192.168.53.4'
      MASKLENGTH: 32
      DESTVRFNAME: 'VRF_Mp1'
      NEXTHOP: '192.168.89.1'
      IFNAME: 'Ethernet64/0/4.1'
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

```jinja2
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
```

### 5 配置静态路由并绑定BFD会话。

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
```

### 如果需要为静态路由绑定静态BFD会话，通过**ADD SRROUTE**的“静态BFD会话名”来指定静态路由所联动的静态BFD的会话名。

### 在网关侧配置到VNF的回程路由，目的地址为VNF上各逻辑接口的IP地址，下一跳为VNF上配置的各逻辑接口对应的外联口的IP地址。

### 需要说明的是，配置VNF与DN/PDN通信的回程路由时，目的地址为UE的网段地址，下一跳为VNF上外联口的IP地址。


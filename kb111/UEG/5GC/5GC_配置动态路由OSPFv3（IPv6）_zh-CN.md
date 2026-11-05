---
id: ''
name: 配置动态路由OSPFv3（IPv6）
ne_type: UEG
type: feature
description: 网关设备（如FW）不支持BFD时，UEG与对端设备可通过OSPFv3动态路由进行组网连接，该方式适用于IPv6组网的网络中。  图1是UEG与周边网元通过OSPFv3动态路由互通的组网示意。UEG与网关设备（如FW）运行动态路由协议而接入企业网络，UEG的配置请参考本页面，FW的配置请参考FW对应型号设备的产品文档。  **图1** OSPFv3动态路由组网
tags: []
risk_level: ''
doc_source: ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（一号通专网通用场景，入驻式）","软件安装与开站","UEG软件安装与开站","UEG初始配置","参考：详细配置指导","组网路由配置（裸机容器）","配置VNF侧IP路由数据","配置动态路由OSPFv3（IPv6）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
网关设备（如FW）不支持BFD时，UEG与对端设备可通过OSPFv3动态路由进行组网连接，该方式适用于IPv6组网的网络中。图1是UEG与周边网元通过OSPFv3动态路由互通的组网示意。UEG与网关设备（如FW）运行动态路由协议而接入企业网络，UEG的配置请参考本页面，FW的配置请参考FW对应型号设备的产品文档。**图1** OSPFv3动态路由组网

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
          description: 'IPv6组网场景下，该参数选择ipv6uni。'
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
          description: '* （UEG-S）请参考外联口介绍(机架服务器-ARM)/外联口介绍(刀片式服务器2U)进行规划。 * （UEG-M）请参考外联口介绍(刀片式服务器2U)进行规划。 * （UEG-L）请参考外联口介绍(刀片式服务器2U)进行规划。'
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
          description: '此处以双平面为例。'
          data_source: '全网规划'
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
          description: '-'
          data_source: '固定取值'
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
          description: '如果规划外联口使用IPv4v6双栈地址，则分别执行**ADD IFIPV4ADDRESS**和**ADD IFIPV6ADDRESS**  对同一外联口配置IPv4和IPv6地址。  此处规划的IP地址是与网关互通的外联口IP。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        PREFIXLEN:
          name: 'IPv6地址前缀'
          type: integer
          minimum: 1
          maximum: 128
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_ospfv3_list:
      type: items
      properties:
        PROCID:
          name: 'OSPFv3进程号'
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
        ROUTERID:
          name: '路由器标识'
          type: string
          maxLength: 15
          required: true
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
          name: 'OSPFv3共网段虚拟系统使能标志'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: TRUE
    add_ospfv3area_list:
      type: items
      properties:
        PROCID:
          name: 'OSPFv3进程号'
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
          name: 'OSPFv3区域类型'
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
    add_ospfv3areaauth_list:
      type: items
      properties:
        PROCID:
          name: 'OSPFv3进程号'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AREAID:
          name: 'OSPFv3区域号'
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
          - hmac-sha256
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AUTHTEXTTYPE:
          name: '认证密码类型'
          type: string
          enum:
          - cipher
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: cipher
        AUTHTEXTMD5:
          name: '密文验证密码'
          type: string
          maxLength: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        KEYID:
          name: '密文验证字标识符'
          type: integer
          minimum: 1
          maximum: 65535
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_ospfv3interface_list:
      type: items
      properties:
        PROCID:
          name: 'OSPFv3进程号'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: true
          description: '-'
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
          description: '“DRPRI”设置为“0”表示不参与DR和BDR的选举。为避免UEG被选为DR或BDR，建议将VNF“DRPRI”配置为0，对端配置为非0。-'
          data_source: '-'
          pattern: ''
          default: 1
        VIRTUALSYSFLAG:
          name: 'OSPFv3共网段虚拟系统使能标志'
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
          name: 'OSPFv3虚拟路由器标识使能标识'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
    add_ospfv3interfaceauth_list:
      type: items
      properties:
        PROCID:
          name: 'OSPFv3进程号'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AREAID:
          name: 'OSPFv3区域号'
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
          - hmac-sha256
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AUTHENTYPE:
          name: '认证密码类型'
          type: string
          enum:
          - cipher
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: cipher
        AUTHTEXTMD5:
          name: '密文验证密码'
          type: string
          maxLength: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        KEYID:
          name: '密文验证字标识符'
          type: integer
          minimum: 1
          maximum: 65535
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        INSTANCEID:
          name: '实例号'
          type: integer
          minimum: 0
          maximum: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_ospfv3importroute_list:
      type: items
      properties:
        PROCID:
          name: 'OSPFv3进程号'
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
          name: '协议号'
          type: string
          enum:
          - bgp
          - direct
          - ospfv3
          - static
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
          description: '-'
          data_source: '-'
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
          data_source: '-'
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
  examples:
    add_l3vpninst_list:
    - VRFNAME: 'VPN_LocalDN'
    add_vpninstaf_list:
    - VRFNAME: 'VPN_LocalDN'
      AFTYPE: ipv6uni
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
    set_ifipv6enable_list:
    - IFNAME: 'Ethernet64/0/6.1'
      ENABLEFLAG: TRUE
    add_ifipv6address_list:
    - IFNAME: 'Ethernet64/0/6.1'
      IPV6ADDRESS: 'FC00::10C2'
      PREFIXLEN: 123
    add_ospfv3_list:
    - PROCID: 6
      VRFNAME: 'VPN_Access'
      ROUTERID: '10.8.25.1'
      BFDALLINTFFLG: FALSE
      VPNINSCAPSIMFLG: TRUE
      VIRTUALSYSFLAG: TRUE
    add_ospfv3area_list:
    - PROCID: 6
      AREAID: '0.0.0.5'
      AREATYPE: NSSA
    add_ospfv3areaauth_list:
    - PROCID: OSPFv3进程号
      AREAID: 'OSPFv3区域标识'
      AUTHENMODE: hmac-sha256
      AUTHTEXTTYPE: cipher
      AUTHTEXTMD5: '密文验证密码'
      KEYID: 密文验证字标识符
    add_ospfv3interface_list:
    - PROCID: 6
      AREAID: '0.0.0.5'
      IFNAME: 'Ethernet64/0/6.1'
      DRPRI: 0
      VIRTUALSYSFLAG: TRUE
      CFGROUTERIDFLAG: FALSE
    add_ospfv3interfaceauth_list:
    - PROCID: OSPFv3进程号
      AREAID: '区域号'
      IFNAME: '接口名称'
      AUTHENMODE: hmac-sha256
      AUTHENTYPE: cipher
      AUTHTEXTMD5: '密文验证密码'
      KEYID: 密文验证字标识符
      INSTANCEID: 实例号
    add_ospfv3importroute_list:
    - PROCID: 6
      TOPOID: 0
      PROTOCOL: wlr
      IMPTCOSTCFG: FALSE
      IMPTTAGCFG: FALSE
      IMPTTYPECFG: FALSE
      COST: 100
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

#### 2.6 配置IPv6使能。

```jinja2
{%- for item in set_ifipv6enable_list -%}
    SET IFIPV6ENABLE:
    {#- --- 必选参数 --- -#}
    IFNAME="{{item.IFNAME}}",
    ENABLEFLAG={{item.ENABLEFLAG}},
    ;
{%- endfor -%}
```

#### 2.7 配置外联口IP地址。

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

#### 如果规划外联口使用IPv4v6双栈地址，则分别执行**ADD IFIPV4ADDRESS**和**ADD IFIPV6ADDRESS**对同一外联口配置IPv4和IPv6地址。

### 3 配置OSPFv3路由数据。

#### 3.1 创建OSPFv3进程。

```jinja2
{%- for item in add_ospfv3_list -%}
    ADD OSPFV3:
    {#- --- 必选参数 --- -#}
    PROCID={{item.PROCID}},
    ROUTERID="{{item.ROUTERID}}",
    {#- --- 可选参数 --- -#}
    {%- if item.VRFNAME is not none -%}
        VRFNAME="{{item.VRFNAME}}",
    {%- endif -%}
    {%- if item.BFDALLINTFFLG is not none -%}
        BFDALLINTFFLG={{item.BFDALLINTFFLG}},
    {%- endif -%}
    {%- if item.VPNINSCAPSIMFLG is not none -%}
        VPNINSCAPSIMFLG={{item.VPNINSCAPSIMFLG}},
    {%- endif -%}
    {%- if item.VIRTUALSYSFLAG is not none -%}
        VIRTUALSYSFLAG={{item.VIRTUALSYSFLAG}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### UEG支持VPN多实例时，需要取消环路检查（参数“VPNINSCAPSIMFLG”配置为“TRUE”），否则会导致OSPFv3路由引入失败。

#### 路由器标识Router ID（“ROUTERID”）的选择策略：优选用户配置的Router ID，如果未配置，则选择OSPFv3进程所在VRF内或者公网内的最大接口IP地址。

#### FW不支持BFD，参数“BFDALLINTFFLG（使能BFD）”配置为“FALSE”。

#### 当OSPF路由配置共网段时，需要将参数“VIRTUALSYSFLAG（OSPF共网段虚拟系统使能标志）”配置为“TRUE”。

#### 3.2 增加OSPFv3区域。

```jinja2
{%- for item in add_ospfv3area_list -%}
    ADD OSPFV3AREA:
    {#- --- 必选参数 --- -#}
    PROCID={{item.PROCID}},
    AREAID="{{item.AREAID}}",
    {#- --- 可选参数 --- -#}
    {%- if item.AREATYPE is not none -%}
        AREATYPE={{item.AREATYPE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 参数“AREATYPE（OSPFv3区域类型）”配置为“NSSA”或“Normal”时，都不需要配置Loopback地址。

#### 3.3 **（可选）**配置OSPFv3区域认证。

```jinja2
{%- if is_optional_ospfv3_area_auth -%}
    {%- for item in add_ospfv3areaauth_list -%}
        ADD OSPFV3AREAAUTH:
        {#- --- 必选参数 --- -#}
        PROCID={{item.PROCID}},
        AREAID="{{item.AREAID}}",
        AUTHENMODE={{item.AUTHENMODE}},
        AUTHTEXTMD5="{{item.AUTHTEXTMD5}}",
        KEYID={{item.KEYID}},
        {#- --- 可选参数 --- -#}
        {%- if item.AUTHTEXTTYPE is not none -%}
            AUTHTEXTTYPE={{item.AUTHTEXTTYPE}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 使用区域验证时，一个区域中所有设备的接口上所配置的认证模式和口令必须一致。

#### 3.4 配置OSPFv3协议的接口属性。

```jinja2
{%- for item in add_ospfv3interface_list -%}
    ADD OSPFV3INTERFACE:
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

#### 参数“NETWORKTYPE”（网络类型）选择“BROADCAST”、“NBMA”、“POINT-TO-POINT”、“POINT-TO-MULTIPOINT”或“P2MP-NONBROADCAST”。

#### 广播或NBMA网络中，根据此接口优先级选举DR和BDR路由器，“优先级”设置为“0”表示不参与DR和BDR的选举。为避免VNF被选为DR或BDR，建议将VNF“优先级”配置为0，对端配置为非0。

#### 3.5 **（可选）**配置OSPFv3接口验证参数。

```jinja2
{%- if is_optional_ospfv3_interface_auth -%}
    {%- for item in add_ospfv3interfaceauth_list -%}
        ADD OSPFV3INTERFACEAUTH:
        {#- --- 必选参数 --- -#}
        PROCID={{item.PROCID}},
        AREAID="{{item.AREAID}}",
        IFNAME="{{item.IFNAME}}",
        AUTHENMODE={{item.AUTHENMODE}},
        AUTHTEXTMD5="{{item.AUTHTEXTMD5}}",
        KEYID={{item.KEYID}},
        INSTANCEID={{item.INSTANCEID}},
        {#- --- 可选参数 --- -#}
        {%- if item.AUTHENTYPE is not none -%}
            AUTHENTYPE={{item.AUTHENTYPE}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 参数“IFNAME”（接口名称）采用3.d中的接口名称。

#### 3.6 设置OSPFv3引入路由类型。

```jinja2
{%- for item in add_ospfv3importroute_list -%}
    ADD OSPFV3IMPORTROUTE:
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


---
id: ''
name: 激活QoS简单流分类特性（VNRS_VNFC）
ne_type: UEG
type: feature
description: 本操作指导介绍在运行网络配置基于简单流分类的Qos策略的操作过程。  在Ethernet接口、Ethernet子接口或Eth-Trunk接口上配置基于简单流分类的QoS策略，比如说IP报文、VLAN报文的优先级。可以先在该接口上配置DiffServ域， 然后对该DS域配置各种优先级的映射关系，接口上的报文会按照DiffServ域中的映射关系进行简单流分类映射。  简单流分类通常配置在网络的核心位置。  当需要对来自上游设备的VLAN报文进行QoS调度的时候，可以通过本命令配置DiffServ域中VLAN报文的802.1p优先级到路由器内部服务等级之间的映射，并为报文着色。对于IP报文，则是将DSCP值映射成内部服务等级，并着色。将DiffServ域绑定到报文的入接口后，QoS将根据报文映射的路由器内部服务等级和颜色进行拥塞管理和拥塞避免。  对于下行报文则将路由器内部的服务等级和颜色映射成对应的DSCP值或者802.1p值。  NP卡场景下，不支持接口重定向到指定VPN功能。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝S","MEC 特性指南（风筝S）","UEG特性指南","IP基本特性","IPFD-020400 IP可靠性","IPFD-020401 QoS","特性配置","简单流分类配置（VNRS_VNFC）","激活QoS简单流分类特性（VNRS_VNFC）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
本操作指导介绍在运行网络配置基于简单流分类的Qos策略的操作过程。在Ethernet接口、Ethernet子接口或Eth-Trunk接口上配置基于简单流分类的QoS策略，比如说IP报文、VLAN报文的优先级。可以先在该接口上配置DiffServ域， 然后对该DS域配置各种优先级的映射关系，接口上的报文会按照DiffServ域中的映射关系进行简单流分类映射。简单流分类通常配置在网络的核心位置。当需要对来自上游设备的VLAN报文进行QoS调度的时候，可以通过本命令配置DiffServ域中VLAN报文的802.1p优先级到路由器内部服务等级之间的映射，并为报文着色。对于IP报文，则是将DSCP值映射成内部服务等级，并着色。将DiffServ域绑定到报文的入接口后，QoS将根据报文映射的路由器内部服务等级和颜色进行拥塞管理和拥塞避免。对于下行报文则将路由器内部的服务等级和颜色映射成对应的DSCP值或者802.1p值。NP卡场景下，不支持接口重定向到指定VPN功能。

## 必备事项
前提条件

已经创建对应DiffServ域。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    add_qosdifferserv_list:
      type: items
      properties:
        DSNAME:
          name: 'DS域名'
          type: string
          maxLength: 31
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_qosba_list:
      type: items
      properties:
        DSNAME:
          name: 'DS域名'
          type: string
          maxLength: 31
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        BATYPE:
          name: 'ba类型'
          type: string
          enum:
          - 8021p
          - ip_dscp
          - mpls_exp
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        BAVALUE:
          name: 'ba值'
          type: integer
          minimum: 0
          maximum: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SERVICECLASS:
          name: '服务分类'
          type: string
          enum:
          - af1
          - af2
          - af3
          - af4
          - be
          - cs6
          - cs7
          - ef
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        COLOR:
          name: '颜色分类'
          type: string
          enum:
          - green
          - red
          - yellow
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_qosphb_list:
      type: items
      properties:
        DSNAME:
          name: 'DS域名'
          type: string
          maxLength: 31
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        PHBTYPE:
          name: 'PHB类型'
          type: string
          enum:
          - 8021p
          - ip_dscp
          - mpls_exp
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PHBVALUE:
          name: 'PHB值'
          type: integer
          minimum: 0
          maximum: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SERVICECLASS:
          name: '服务分类'
          type: string
          enum:
          - af1
          - af2
          - af3
          - af4
          - be
          - cs6
          - cs7
          - ef
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        COLOR:
          name: '颜色分类'
          type: string
          enum:
          - green
          - red
          - yellow
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_qosiftrust_list:
      type: items
      properties:
        DSNAME:
          name: 'DS域名'
          type: string
          maxLength: 31
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        IFNAME:
          name: '接口名称'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        FLAG8021P:
          name: '8021p标志'
          type: string
          enum:
          - false
          - true
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: false
    add_qosrdrvpn_list:
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
        VRFNAME:
          name: 'VPN名称'
          type: string
          maxLength: 31
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_qosifphb_list:
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
        PHBTYPE:
          name: '出接口报文的优先级字段映射类型'
          type: string
          enum:
          - dscp
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    add_qosdifferserv_list:
    - DSNAME: 'ds1'
    set_qosba_list:
    - DSNAME: 'ds1'
      BATYPE: ip_dscp
      BAVALUE: 1
      SERVICECLASS: be
      COLOR: green
    set_qosphb_list:
    - DSNAME: 'ds1'
      PHBTYPE: 8021p
      PHBVALUE: 1
      SERVICECLASS: be
      COLOR: green
    add_qosiftrust_list:
    - DSNAME: 'ds1'
      IFNAME: 'Ethernet 64/0/3'
      FLAG8021P: 否
    add_qosrdrvpn_list:
    - IFNAME: 'Ethernet 64/0/3'
      VRFNAME: 'vpn1'
    add_qosifphb_list:
    - IFNAME: 'Ethernet64/0/3'
      PHBTYPE: dscp
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 当不使用默认存在两个DiffServ域（default和5p3d）时，配置DiffServ域。

### 在“MML命令行-UEG”窗口上执行：

```jinja2
{%- for item in add_qosdifferserv_list -%}
    ADD QOSDIFFERSERV:
    {#- --- 必选参数 --- -#}
    DSNAME="{{item.DSNAME}}",
    ;
{%- endfor -%}
```

### 2 当需要修改上行或者下行的映射关系时，通过**SET QOSBA**修改“服务分类”、“颜色分类”，通过**SET QOSPHB**修改“PHB值”，其中5p3d域不允许修改。

### 在“MML命令行-UEG”窗口上执行：

```jinja2
{%- for item in set_qosba_list -%}
    SET QOSBA:
    {#- --- 必选参数 --- -#}
    DSNAME="{{item.DSNAME}}",
    BATYPE={{item.BATYPE}},
    BAVALUE={{item.BAVALUE}},
    SERVICECLASS={{item.SERVICECLASS}},
    {#- --- 可选参数 --- -#}
    {%- if item.COLOR is not none -%}
        COLOR={{item.COLOR}},
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in set_qosphb_list -%}
    SET QOSPHB:
    {#- --- 必选参数 --- -#}
    DSNAME="{{item.DSNAME}}",
    PHBTYPE={{item.PHBTYPE}},
    PHBVALUE={{item.PHBVALUE}},
    SERVICECLASS={{item.SERVICECLASS}},
    COLOR={{item.COLOR}},
    ;
{%- endfor -%}
```

### 3 配置接口绑定相应的DiffServ域。

### 在“MML命令行-UEG”窗口上执行：

```jinja2
{%- for item in add_qosiftrust_list -%}
    ADD QOSIFTRUST:
    {#- --- 必选参数 --- -#}
    DSNAME="{{item.DSNAME}}",
    IFNAME="{{item.IFNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.FLAG8021P is not none -%}
        FLAG8021P={{item.FLAG8021P}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 只有Ethernet子接口和GE子接口支持802.1p映射。

### 4 当需要将流量指定到VPN时，配置接口重定向到指定VPN。

### 在“MML命令行-UEG”窗口上执行：

```jinja2
{%- for item in add_qosrdrvpn_list -%}
    ADD QOSRDRVPN:
    {#- --- 必选参数 --- -#}
    IFNAME="{{item.IFNAME}}",
    VRFNAME="{{item.VRFNAME}}",
    ;
{%- endfor -%}
```

### 必须先创建相应的VPN实例，只支持在以太主接口和GE主接口进行配置。

### 5 当只需要检查BA表时，激活QoS不检查PHB表。

### 在“MML命令行-UEG”窗口上执行：

```jinja2
{%- for item in add_qosifphb_list -%}
    ADD QOSIFPHB:
    {#- --- 必选参数 --- -#}
    IFNAME="{{item.IFNAME}}",
    PHBTYPE={{item.PHBTYPE}},
    ;
{%- endfor -%}
```


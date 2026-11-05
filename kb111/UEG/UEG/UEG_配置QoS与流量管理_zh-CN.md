---
id: GWFD-021201
name: 配置QoS与流量管理
ne_type: UEG
type: feature
description: 通过配置QoS与流量管理功能，可实现以下需求：  * 为了保证在资源紧缺时，运营商能够为高优先级用户优先分配资源。 * 在资源相对富余时，更充分地发挥网络资源的效益，提高客户满意度。    适用于SGW-U、PGW-U、UPF。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝L","MEC 特性指南（风筝L）","GW-U&UPF特性指南","GWFD-021200 QoS与流量管理","GWFD-021201 QoS与流量管理","配置QoS与流量管理"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
通过配置QoS与流量管理功能，可实现以下需求：* 为了保证在资源紧缺时，运营商能够为高优先级用户优先分配资源。* 在资源相对富余时，更充分地发挥网络资源的效益，提高客户满意度。  适用于SGW-U、PGW-U、UPF。

## 必备事项
前提条件

请仔细阅读GWFD-021201 QoS与流量管理。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    set_srvcommonpara_list:
      type: items
      properties:
        TUNNELMARKINGID:
          name: 'TunnelMarking开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: 'VLAN到IP网络的优先级映射'
          data_source: '本端规划'
          pattern: ''
          default: ''
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
          data_source: ''
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
          data_source: '本端规划'
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
    add_qosiftrust_list:
      type: items
      properties:
        DSNAME:
          name: 'DS域名'
          type: string
          maxLength: 31
          required: true
          description: 'VLAN到IP网络的优先级映射'
          data_source: '本端规划'
          pattern: ''
          default: ''
        IFNAME:
          name: '接口名称'
          type: string
          maxLength: 63
          required: true
          description: '物理接口，使用**LST INTERFACE**查询获得。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_srvcommonpara_list_1:
      type: items
      properties:
        TUNNELMARKINGID:
          name: 'TunnelMarking开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: 'VLAN到IP网络的优先级映射'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_qosdifferserv_list_1:
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
    set_qosphb_list:
      type: items
      properties:
        DSNAME:
          name: 'DS域名'
          type: string
          maxLength: 31
          required: true
          description: ''
          data_source: ''
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
          description: 'IP网络到VLAN的优先级映射'
          data_source: '本端规划'
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
    add_qosiftrust_list_1:
      type: items
      properties:
        DSNAME:
          name: 'DS域名'
          type: string
          maxLength: 31
          required: true
          description: 'VLAN到IP网络的优先级映射'
          data_source: '本端规划'
          pattern: ''
          default: ''
        IFNAME:
          name: '接口名称'
          type: string
          maxLength: 63
          required: true
          description: '物理接口，使用**LST INTERFACE**查询获得。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_qoscar_list:
      type: items
      properties:
        USERTYPE:
          name: '用户漫游类型'
          type: string
          enum:
          - HOME
          - ROAMING
          - VISITING
          required: true
          description: '指定4G本地用户开启上下行CAR功能。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        ULRAT:
          name: '上行RAT类型'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        DLRAT:
          name: '下行RAT类型'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_apnqosattr_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '开启基于APN的QoS CAR功能。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        CARSHAPESWUL:
          name: '上行Qos开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          - INHERIT
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        CARSHAPEUL:
          name: '上行CAR/SHAPE开关'
          type: string
          enum:
          - CAR
          - SHAPE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        CARSHAPESWDL:
          name: '下行Qos开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          - INHERIT
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        CARSHAPEDL:
          name: '下行CAR/SHAPE开关'
          type: string
          enum:
          - CAR
          - SHAPE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
  examples:
    set_srvcommonpara_list:
    - TUNNELMARKINGID: ENABLE
    add_qosdifferserv_list:
    - DSNAME: 'default'
    set_qosba_list:
    - DSNAME: 'default'
      BATYPE: 8021p
      BAVALUE: 3
      SERVICECLASS: be
      COLOR: red
    add_qosiftrust_list:
    - DSNAME: 'default'
      IFNAME: 'Ethernet66/0/5'
    set_srvcommonpara_list_1:
    - TUNNELMARKINGID: ENABLE
    add_qosdifferserv_list_1:
    - DSNAME: 'default'
    set_qosphb_list:
    - DSNAME: 'default'
      PHBTYPE: 8021p
      PHBVALUE: 3
      SERVICECLASS: be
      COLOR: green
    add_qosiftrust_list_1:
    - DSNAME: 'default'
      IFNAME: 'Ethernet66/0/5'
    set_qoscar_list:
    - USERTYPE: HOME
      ULRAT: eutran-1
      DLRAT: eutran-1
    set_apnqosattr_list:
    - APN: 'apn1'
      CARSHAPESWUL: ENABLE
      CARSHAPEUL: CAR
      CARSHAPESWDL: ENABLE
      CARSHAPEDL: CAR
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 配置支持入口报文的优先级由CoS到ToS映射（VLAN到IP网络的优先级映射）。

### 如果同时配置CoS到ToS的映射和3GPP QoS到DSCP/ToS的映射，CoS到ToS的映射结果会被3GPP QoS到DSCP/ToS的映射结果覆盖。

#### 1.1 配置TunnelMarking是否使能。

```jinja2
{%- if is_scenario_ingress_cos_tos -%}
    {%- for item in set_srvcommonpara_list -%}
        SET SRVCOMMONPARA:
        {#- --- 可选参数 --- -#}
        {%- if item.TUNNELMARKINGID is not none -%}
            TUNNELMARKINGID={{item.TUNNELMARKINGID}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 1.2 定义一个DS域并进入Diff-Serv域实例。

```jinja2
{%- if is_scenario_ingress_cos_tos -%}
    {%- for item in add_qosdifferserv_list -%}
        ADD QOSDIFFERSERV:
        {#- --- 必选参数 --- -#}
        DSNAME="{{item.DSNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 1.3 配置DS域的上行VLAN报文的802.1p的值与UEG内部的服务等级的对应关系，并可将报文着色。

```jinja2
{%- if is_scenario_ingress_cos_tos -%}
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
{%- endif -%}
```

#### 1.4 在接口上绑定DS域，使其支持简单流分类，以便对报文的优先级进行修改,并在该VLAN子接口上配置trust CoS。

```jinja2
{%- if is_scenario_ingress_cos_tos -%}
    {%- for item in add_qosiftrust_list -%}
        ADD QOSIFTRUST:
        {#- --- 必选参数 --- -#}
        DSNAME="{{item.DSNAME}}",
        IFNAME="{{item.IFNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

### 2 配置支持出口报文的优先级由ToS到CoS映射（IP网络到VLAN的优先级映射）。

#### 2.1 配置TunnelMarking是否使能。

```jinja2
{%- if is_scenario_egress_tos_cos -%}
    {%- for item in set_srvcommonpara_list_1 -%}
        SET SRVCOMMONPARA:
        {#- --- 可选参数 --- -#}
        {%- if item.TUNNELMARKINGID is not none -%}
            TUNNELMARKINGID={{item.TUNNELMARKINGID}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 2.2 定义DS域并创建一个新的DS域。

```jinja2
{%- if is_scenario_egress_tos_cos -%}
    {%- for item in add_qosdifferserv_list_1 -%}
        ADD QOSDIFFERSERV:
        {#- --- 必选参数 --- -#}
        DSNAME="{{item.DSNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 2.3 配置DS域的下行报文在UEG内部的服务等级和报文颜色与外部vlan报文的802.1p值的对应关系。

```jinja2
{%- if is_scenario_egress_tos_cos -%}
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
{%- endif -%}
```

#### 2.4 用来在接口上绑定DS域，使其支持简单流分类，以便对报文的优先级进行修改，并在该VLAN子接口上配置trust CoS。

```jinja2
{%- if is_scenario_egress_tos_cos -%}
    {%- for item in add_qosiftrust_list_1 -%}
        ADD QOSIFTRUST:
        {#- --- 必选参数 --- -#}
        DSNAME="{{item.DSNAME}}",
        IFNAME="{{item.IFNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

### 3 配置QoS CAR功能。

#### 3.1 配置指定类型的用户上下行CAR功能。

```jinja2
{%- if is_scenario_qos_car -%}
    {%- for item in set_qoscar_list -%}
        SET QOSCAR:
        {#- --- 必选参数 --- -#}
        USERTYPE={{item.USERTYPE}},
        {#- --- 可选参数 --- -#}
        {%- if item.ULRAT is not none -%}
            ULRAT={{item.ULRAT}},
        {%- endif -%}
        {%- if item.DLRAT is not none -%}
            DLRAT={{item.DLRAT}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 3.2 配置基于APN的QoS属性数据。

```jinja2
{%- if is_scenario_qos_car -%}
    {%- for item in set_apnqosattr_list -%}
        SET APNQOSATTR:
        {#- --- 必选参数 --- -#}
        APN="{{item.APN}}",
        {#- --- 可选参数 --- -#}
        {%- if item.CARSHAPESWUL is not none -%}
            CARSHAPESWUL={{item.CARSHAPESWUL}},
        {%- endif -%}
        {%- if item.CARSHAPESWDL is not none -%}
            CARSHAPESWDL={{item.CARSHAPESWDL}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：CARSHAPESWUL=ENABLE 时必选 --- -#}
        {%- if item.CARSHAPESWUL == 'ENABLE' -%}
            CARSHAPEUL={{item.CARSHAPEUL}},
        {%- endif -%}
        {#- --- 条件必选：CARSHAPESWDL=ENABLE 时必选 --- -#}
        {%- if item.CARSHAPESWDL == 'ENABLE' -%}
            CARSHAPEDL={{item.CARSHAPEDL}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```


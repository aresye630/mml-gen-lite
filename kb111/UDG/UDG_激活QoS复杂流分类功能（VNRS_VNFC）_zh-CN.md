---
id: ''
name: 激活QoS复杂流分类功能（VNRS_VNFC）
ne_type: UDG
type: feature
description: 本操作指导介绍在运行网络中激活QoS复杂流分类功能特性的操作过程。  QoS复杂流分类涉及到流策略、流分类、流行为三个概念。一个流分类和流行为可以组成一个CB对，在具体的流策略中绑定。流策略可以绑定到指定的Ethernet接口、Ethernet子接口、Eth-Trunk接口或Eth-Trunk子接口的出入方向，经过的报文会匹配流分类中的规则，匹配上后会按照流行为中指定的动作进行处理。  流分类中指定了具体的报文匹配规则。ACL规则的配置请见ACL配置手册。  流行为中指定了报文匹配成功后对应的处理动作。目前动作类型有：允许、拒绝、指定下一跳、级联流策略。  NP卡场景下，不支持流策略统计功能以及以下ACL流行为。  * 级联流策略动作 * 重定向VPN组 * 安全URPF * CAR
risk_level: ''
doc_source: ["特性部署","特性指南","UDG特性指南","IP基本特性","IPFD-012000 IP可靠性","IPFD-012001 QoS","特性配置","复杂流分类配置（VNRS_VNFC）","激活QoS复杂流分类功能（VNRS_VNFC）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本操作指导介绍在运行网络中激活QoS复杂流分类功能特性的操作过程。QoS复杂流分类涉及到流策略、流分类、流行为三个概念。一个流分类和流行为可以组成一个CB对，在具体的流策略中绑定。流策略可以绑定到指定的Ethernet接口、Ethernet子接口、Eth-Trunk接口或Eth-Trunk子接口的出入方向，经过的报文会匹配流分类中的规则，匹配上后会按照流行为中指定的动作进行处理。流分类中指定了具体的报文匹配规则。ACL规则的配置请见ACL配置手册。流行为中指定了报文匹配成功后对应的处理动作。目前动作类型有：允许、拒绝、指定下一跳、级联流策略。NP卡场景下，不支持流策略统计功能以及以下ACL流行为。* 级联流策略动作* 重定向VPN组* 安全URPF* CAR

## 必备事项
前提条件

操作人员已经登录网络管理系统NMS（Network Management System）。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    add_mqcbehavior_list:
      type: items
      properties:
        BEHAVIORNAME:
          name: '行为名称'
          type: string
          maxLength: 31
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_qosactrdrnhp_list:
      type: items
      properties:
        BEHAVIORNAME:
          name: '流行为名称'
          type: string
          maxLength: 31
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPVERSION:
          name: 'IP协议版本'
          type: string
          enum:
          - IPv4
          - IPv6
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: IPv4
        NEXTHOP:
          name: '下一跳地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NEXTHOP6:
          name: 'IPv6下一跳地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_sqosremark_list:
      type: items
      properties:
        BEHAVIORNAME:
          name: '流行为名称'
          type: string
          maxLength: 31
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        V4DSCPVALUE:
          name: 'IPv4的DSCP值'
          type: integer
          minimum: 0
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 255
        V6DSCPVALUE:
          name: 'IPv6的DSCP值'
          type: integer
          minimum: 0
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 255
        DFVALUE:
          name: 'DF值'
          type: integer
          minimum: 0
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 255
    set_qosactfilter_list:
      type: items
      properties:
        BEHAVIORNAME:
          name: '行为名称'
          type: string
          maxLength: 31
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        FILTER:
          name: '行为状态'
          type: string
          enum:
          - deny
          - permit
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_qosactrdrpolicy_list:
      type: items
      properties:
        BEHAVIORNAME:
          name: '行为名称'
          type: string
          maxLength: 31
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        POLICYNAME:
          name: '策略名称'
          type: string
          maxLength: 31
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_sqosrdrvpngroup_list:
      type: items
      properties:
        VPNGROUPNAME:
          name: 'VPN组名称'
          type: string
          maxLength: 31
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        BEHAVIORNAME:
          name: '行为名称'
          type: string
          maxLength: 31
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_sqosurpf_list:
      type: items
      properties:
        BEHAVIORNAME:
          name: '流行为名称'
          type: string
          maxLength: 31
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        URPFTYPE:
          name: 'URPF检查类型'
          type: string
          enum:
          - loose
          - strict
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        URPFDEFAULT:
          name: '匹配默认路由'
          type: string
          enum:
          - allow
          - disallow
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_sqoscar_list:
      type: items
      properties:
        BEHAVIORNAME:
          name: '流行为名称'
          type: string
          maxLength: 31
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        CIR:
          name: '承诺信息速率（kbps）'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_mqcclassifier_list:
      type: items
      properties:
        CLASSIFIERNAME:
          name: '分类名称'
          type: string
          maxLength: 31
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        OPERATOR:
          name: '关系类型'
          type: string
          enum:
          - or
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: or
    add_qosruleacl_list:
      type: items
      properties:
        CLASSIFIERNAME:
          name: '分类名称'
          type: string
          maxLength: 31
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPVERSION:
          name: 'IP协议版本'
          type: string
          enum:
          - IPv4
          - IPv6
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ACLTYPE:
          name: 'ACL类型'
          type: string
          enum:
          - acl-name
          - acl-number
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ACLNAME:
          name: 'ACL名称'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ACLNUM:
          name: 'ACL编号'
          type: integer
          minimum: 2000
          maximum: 4999
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_mqcpolicy_list:
      type: items
      properties:
        POLICYNAME:
          name: '策略名称'
          type: string
          maxLength: 31
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_mqcpolicynode_list:
      type: items
      properties:
        POLICYNAME:
          name: '策略名称'
          type: string
          maxLength: 31
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        CLASSIFIERNAME:
          name: '分类名称'
          type: string
          maxLength: 31
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        BEHAVIORNAME:
          name: '行为名称'
          type: string
          maxLength: 31
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PRECEDENCE:
          name: '优先级'
          type: integer
          minimum: 1
          maximum: 5100
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_qosapplication_list:
      type: items
      properties:
        POLICYNAME:
          name: '策略名称'
          type: string
          maxLength: 31
          required: true
          description: ''
          data_source: ''
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
        DIRECTION:
          name: '报文方向'
          type: string
          enum:
          - inbound
          - outbound
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    mod_mqcpolicy_list:
      type: items
      properties:
        POLICYNAME:
          name: '策略名称'
          type: string
          maxLength: 31
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        STCENABLE:
          name: '统计使能标志'
          type: string
          enum:
          - disable
          - enable
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_aclgroup_list:
      type: items
      properties:
        ACLNAME:
          name: 'ACL规则组标识'
          type: string
          maxLength: 32
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_aclruleadv4_list:
      type: items
      properties:
        ACLNAME:
          name: 'ACL规则组标识'
          type: string
          maxLength: 32
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        ACLRULENAME:
          name: '规则名称'
          type: string
          maxLength: 32
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ACLACTION:
          name: '规则行为'
          type: string
          enum:
          - Deny
          - Permit
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ACLPROTOCOL:
          name: '协议类型值'
          type: integer
          minimum: 0
          maximum: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ACLSOURCEIP:
          name: '源IP地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: '0.0.0.0'
        ACLSRCWILD:
          name: '源IP地址反掩码'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: '255.255.255.255'
        ACLDESTIP:
          name: '目的IP地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: '0.0.0.0'
        ACLDESTWILD:
          name: '目的IP地址反掩码'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: '255.255.255.255'
    add_mqcbehavior_list_1:
      type: items
      properties:
        BEHAVIORNAME:
          name: '行为名称'
          type: string
          maxLength: 31
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_mqcclassifier_list_1:
      type: items
      properties:
        CLASSIFIERNAME:
          name: '分类名称'
          type: string
          maxLength: 31
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_qosruleacl_list_1:
      type: items
      properties:
        CLASSIFIERNAME:
          name: '分类名称'
          type: string
          maxLength: 31
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPVERSION:
          name: 'IP协议版本'
          type: string
          enum:
          - IPv4
          - IPv6
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ACLTYPE:
          name: 'ACL类型'
          type: string
          enum:
          - acl-name
          - acl-number
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ACLNAME:
          name: 'ACL名称'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ACLNUM:
          name: 'ACL编号'
          type: integer
          minimum: 2000
          maximum: 4999
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_qosactrdrnhp_list_1:
      type: items
      properties:
        BEHAVIORNAME:
          name: '流行为名称'
          type: string
          maxLength: 31
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPVERSION:
          name: 'IP协议版本'
          type: string
          enum:
          - IPv4
          - IPv6
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: IPv4
        NEXTHOP:
          name: '下一跳地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NEXTHOP6:
          name: 'IPv6下一跳地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_mqcpolicy_list_1:
      type: items
      properties:
        POLICYNAME:
          name: '策略名称'
          type: string
          maxLength: 31
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_mqcpolicynode_list_1:
      type: items
      properties:
        POLICYNAME:
          name: '策略名称'
          type: string
          maxLength: 31
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        BEHAVIORNAME:
          name: '行为名称'
          type: string
          maxLength: 31
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CLASSIFIERNAME:
          name: '分类名称'
          type: string
          maxLength: 31
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PRECEDENCE:
          name: '优先级'
          type: integer
          minimum: 1
          maximum: 5100
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_qosapplication_list_1:
      type: items
      properties:
        POLICYNAME:
          name: '策略名称'
          type: string
          maxLength: 31
          required: true
          description: ''
          data_source: ''
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
        DIRECTION:
          name: '报文方向'
          type: string
          enum:
          - inbound
          - outbound
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    mod_mqcpolicy_list_1:
      type: items
      properties:
        POLICYNAME:
          name: '策略名称'
          type: string
          maxLength: 31
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        STCENABLE:
          name: '统计使能标志'
          type: string
          enum:
          - disable
          - enable
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    add_mqcbehavior_list:
    - BEHAVIORNAME: 'behavior1'
    add_qosactrdrnhp_list:
    - BEHAVIORNAME: 'behavior1'
      IPVERSION: IPv4
      NEXTHOP: '192.168.2.3（公网IP）'
      NEXTHOP6: ''
    add_sqosremark_list:
    - BEHAVIORNAME: 'behavior1'
      V4DSCPVALUE: 5
      V6DSCPVALUE: 5
      DFVALUE: 1
    set_qosactfilter_list:
    - BEHAVIORNAME: 'behavior1'
      FILTER: deny
    add_qosactrdrpolicy_list:
    - BEHAVIORNAME: 'behavior1'
      POLICYNAME: 'policy2'
    add_sqosrdrvpngroup_list:
    - VPNGROUPNAME: 'test1'
      BEHAVIORNAME: 'behavior1'
    add_sqosurpf_list:
    - BEHAVIORNAME: 'behavior1'
      URPFTYPE: strict
      URPFDEFAULT: disallow
    add_sqoscar_list:
    - BEHAVIORNAME: 'behavior1'
      CIR: 10
    add_mqcclassifier_list:
    - CLASSIFIERNAME: 'class1'
      OPERATOR: or
    add_qosruleacl_list:
    - CLASSIFIERNAME: 'class1'
      IPVERSION: IPv4
      ACLTYPE: acl-name
      ACLNAME: 'acl1'
      ACLNUM: ''
    add_mqcpolicy_list:
    - POLICYNAME: 'policy1、policy2'
    add_mqcpolicynode_list:
    - POLICYNAME: 'policy1'
      CLASSIFIERNAME: 'class1'
      BEHAVIORNAME: 'behavior1'
      PRECEDENCE: 1
    add_qosapplication_list:
    - POLICYNAME: 'policy1'
      IFNAME: 'Ethernet64/0/3'
      DIRECTION: 出方向
    mod_mqcpolicy_list:
    - POLICYNAME: 'policy1'
      STCENABLE: enable
    add_aclgroup_list:
    - ACLNAME: 'acl1'
    add_aclruleadv4_list:
    - ACLNAME: 'acl1'
      ACLRULENAME: 'adv_3'
      ACLACTION: Deny
      ACLPROTOCOL: 0
      ACLSOURCEIP: '192.168.1.3'
      ACLSRCWILD: '0.0.0.0'
      ACLDESTIP: '192.168.2.1'
      ACLDESTWILD: '0.0.0.0'
    add_mqcbehavior_list_1:
    - BEHAVIORNAME: 'behavior1'
    add_mqcclassifier_list_1:
    - CLASSIFIERNAME: 'class1'
    add_qosruleacl_list_1:
    - CLASSIFIERNAME: 'class1'
      IPVERSION: IPv4
      ACLTYPE: acl-name
      ACLNAME: 'acl1'
      ACLNUM: ''
    add_qosactrdrnhp_list_1:
    - BEHAVIORNAME: 'behavior1'
      IPVERSION: IPv4
      NEXTHOP: '192.168.2.3'
      NEXTHOP6: ''
    add_mqcpolicy_list_1:
    - POLICYNAME: 'policy1'
    add_mqcpolicynode_list_1:
    - POLICYNAME: 'policy1'
      BEHAVIORNAME: 'behavior1'
      CLASSIFIERNAME: 'class1'
      PRECEDENCE: 1
    add_qosapplication_list_1:
    - POLICYNAME: 'policy1'
      IFNAME: 'Ethernet64/0/3'
      DIRECTION: outbound
    mod_mqcpolicy_list_1:
    - POLICYNAME: 'policy1'
      STCENABLE: enable
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 配置ACL规则组。

### ACL4规则组参见激活支持ACL的配置，ACL6规则组参见激活支持ACL6的配置。

### 2 增加流行为。

### 在“MML命令行-UDG”窗口上执行：

```jinja2
{%- for item in add_mqcbehavior_list -%}
    ADD MQCBEHAVIOR:
    {#- --- 必选参数 --- -#}
    BEHAVIORNAME="{{item.BEHAVIORNAME}}",
    ;
{%- endfor -%}
```

### 3 当需要指定对应的流动作时，增加对应的流动作：

### 在“MML命令行-UDG”窗口上执行：

#### 3.1 当需要配置重定向下一跳动作：

```jinja2
{%- if is_scenario_redirect_next_hop -%}
    {%- for item in add_qosactrdrnhp_list -%}
        ADD QOSACTRDRNHP:
        {#- --- 必选参数 --- -#}
        BEHAVIORNAME="{{item.BEHAVIORNAME}}",
        IPVERSION={{item.IPVERSION}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：IPVERSION=IPv4 时必选 --- -#}
        {%- if item.IPVERSION == 'IPv4' -%}
            NEXTHOP="{{item.NEXTHOP}}",
        {%- endif -%}
        {#- --- 条件必选：IPVERSION=IPv6 时必选 --- -#}
        {%- if item.IPVERSION == 'IPv6' -%}
            NEXTHOP6="{{item.NEXTHOP6}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 3.2 当需要配置重标记：

```jinja2
{%- if is_scenario_remark -%}
    {%- for item in add_sqosremark_list -%}
        ADD SQOSREMARK:
        {#- --- 必选参数 --- -#}
        BEHAVIORNAME="{{item.BEHAVIORNAME}}",
        {#- --- 可选参数 --- -#}
        {%- if item.V4DSCPVALUE is not none -%}
            V4DSCPVALUE={{item.V4DSCPVALUE}},
        {%- endif -%}
        {%- if item.V6DSCPVALUE is not none -%}
            V6DSCPVALUE={{item.V6DSCPVALUE}},
        {%- endif -%}
        {%- if item.DFVALUE is not none -%}
            DFVALUE={{item.DFVALUE}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 3.3 当需要配置deny动作：

```jinja2
{%- if is_scenario_deny -%}
    {%- for item in set_qosactfilter_list -%}
        SET QOSACTFILTER:
        {#- --- 必选参数 --- -#}
        BEHAVIORNAME="{{item.BEHAVIORNAME}}",
        FILTER={{item.FILTER}},
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 3.4 当需要配置级联流策略动作：

```jinja2
{%- if is_scenario_cascade_policy -%}
    {%- for item in add_qosactrdrpolicy_list -%}
        ADD QOSACTRDRPOLICY:
        {#- --- 必选参数 --- -#}
        BEHAVIORNAME="{{item.BEHAVIORNAME}}",
        POLICYNAME="{{item.POLICYNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 3.5 当需要配置重定向VPN组：

```jinja2
{%- if is_scenario_redirect_vpn_group -%}
    {%- for item in add_sqosrdrvpngroup_list -%}
        ADD SQOSRDRVPNGROUP:
        {#- --- 必选参数 --- -#}
        VPNGROUPNAME="{{item.VPNGROUPNAME}}",
        BEHAVIORNAME="{{item.BEHAVIORNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 需要先使用 **ADD SQOSVPNGROUP**命令添加VPN组，使用**ADD L3VPNINST**命令添加VPN实例，使用 **ADD SQOSVPNGROUPMEM**命令向VPN组添加VPN成员。

#### 3.6 当需要配置安全URPF：

```jinja2
{%- if is_scenario_urpf -%}
    {%- for item in add_sqosurpf_list -%}
        ADD SQOSURPF:
        {#- --- 必选参数 --- -#}
        BEHAVIORNAME="{{item.BEHAVIORNAME}}",
        URPFTYPE={{item.URPFTYPE}},
        URPFDEFAULT={{item.URPFDEFAULT}},
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 3.7 当需要配置CAR：

```jinja2
{%- if is_scenario_car -%}
    {%- for item in add_sqoscar_list -%}
        ADD SQOSCAR:
        {#- --- 必选参数 --- -#}
        BEHAVIORNAME="{{item.BEHAVIORNAME}}",
        CIR={{item.CIR}},
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 流动作permit可以和其他动作共存，其他都是互斥的。

### 4 增加流分类。

### 在“MML命令行-UDG”窗口上执行：

```jinja2
{%- for item in add_mqcclassifier_list -%}
    ADD MQCCLASSIFIER:
    {#- --- 必选参数 --- -#}
    CLASSIFIERNAME="{{item.CLASSIFIERNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.OPERATOR is not none -%}
        OPERATOR={{item.OPERATOR}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 5 当需要流分类绑定ACL规则。

### 在“MML命令行-UDG”窗口上执行：

#### 5.1 绑定基于名称和编号的ACL规则：

```jinja2
{%- for item in add_qosruleacl_list -%}
    ADD QOSRULEACL:
    {#- --- 必选参数 --- -#}
    CLASSIFIERNAME="{{item.CLASSIFIERNAME}}",
    IPVERSION={{item.IPVERSION}},
    ACLTYPE={{item.ACLTYPE}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：ACLTYPE=acl-name 时必选 --- -#}
    {%- if item.ACLTYPE == 'acl-name' -%}
        ACLNAME="{{item.ACLNAME}}",
    {%- endif -%}
    {#- --- 条件必选：ACLTYPE=acl-number 时必选 --- -#}
    {%- if item.ACLTYPE == 'acl-number' -%}
        ACLNUM={{item.ACLNUM}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 6 增加流策略，并绑定流行为和流分类。

### 在“MML命令行-UDG”窗口上执行：

#### 6.1 增加流策略：

```jinja2
{%- for item in add_mqcpolicy_list -%}
    ADD MQCPOLICY:
    {#- --- 必选参数 --- -#}
    POLICYNAME="{{item.POLICYNAME}}",
    ;
{%- endfor -%}
```

#### 6.2 绑定流分类和流行为：

```jinja2
{%- for item in add_mqcpolicynode_list -%}
    ADD MQCPOLICYNODE:
    {#- --- 必选参数 --- -#}
    POLICYNAME="{{item.POLICYNAME}}",
    CLASSIFIERNAME="{{item.CLASSIFIERNAME}}",
    BEHAVIORNAME="{{item.BEHAVIORNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.PRECEDENCE is not none -%}
        PRECEDENCE={{item.PRECEDENCE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 7 将流策略应用到指定的接口视图。

### 在“MML命令行-UDG”窗口上执行：

```jinja2
{%- for item in add_qosapplication_list -%}
    ADD QOSAPPLICATION:
    {#- --- 必选参数 --- -#}
    POLICYNAME="{{item.POLICYNAME}}",
    IFNAME="{{item.IFNAME}}",
    DIRECTION={{item.DIRECTION}},
    ;
{%- endfor -%}
```

### 8 使能流策略统计。

### 在“MML命令行-UDG”窗口上执行：

```jinja2
{%- for item in mod_mqcpolicy_list -%}
    MOD MQCPOLICY:
    {#- --- 必选参数 --- -#}
    POLICYNAME="{{item.POLICYNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.STCENABLE is not none -%}
        STCENABLE={{item.STCENABLE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_aclgroup_list -%}
    ADD ACLGROUP:
    {#- --- 必选参数 --- -#}
    ACLNAME="{{item.ACLNAME}}",
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_aclruleadv4_list -%}
    ADD ACLRULEADV4:
    {#- --- 必选参数 --- -#}
    ACLNAME="{{item.ACLNAME}}",
    ACLRULENAME="{{item.ACLRULENAME}}",
    ACLACTION={{item.ACLACTION}},
    ACLPROTOCOL={{item.ACLPROTOCOL}},
    {#- --- 可选参数 --- -#}
    {%- if item.ACLSOURCEIP is not none -%}
        ACLSOURCEIP="{{item.ACLSOURCEIP}}",
    {%- endif -%}
    {%- if item.ACLSRCWILD is not none -%}
        ACLSRCWILD="{{item.ACLSRCWILD}}",
    {%- endif -%}
    {%- if item.ACLDESTIP is not none -%}
        ACLDESTIP="{{item.ACLDESTIP}}",
    {%- endif -%}
    {%- if item.ACLDESTWILD is not none -%}
        ACLDESTWILD="{{item.ACLDESTWILD}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_mqcbehavior_list_1 -%}
    ADD MQCBEHAVIOR:
    {#- --- 必选参数 --- -#}
    BEHAVIORNAME="{{item.BEHAVIORNAME}}",
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_mqcclassifier_list_1 -%}
    ADD MQCCLASSIFIER:
    {#- --- 必选参数 --- -#}
    CLASSIFIERNAME="{{item.CLASSIFIERNAME}}",
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_qosruleacl_list_1 -%}
    ADD QOSRULEACL:
    {#- --- 必选参数 --- -#}
    CLASSIFIERNAME="{{item.CLASSIFIERNAME}}",
    IPVERSION={{item.IPVERSION}},
    ACLTYPE={{item.ACLTYPE}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：ACLTYPE=acl-name 时必选 --- -#}
    {%- if item.ACLTYPE == 'acl-name' -%}
        ACLNAME="{{item.ACLNAME}}",
    {%- endif -%}
    {#- --- 条件必选：ACLTYPE=acl-number 时必选 --- -#}
    {%- if item.ACLTYPE == 'acl-number' -%}
        ACLNUM={{item.ACLNUM}},
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- if is_scenario_redirect_next_hop -%}
    {%- for item in add_qosactrdrnhp_list_1 -%}
        ADD QOSACTRDRNHP:
        {#- --- 必选参数 --- -#}
        BEHAVIORNAME="{{item.BEHAVIORNAME}}",
        IPVERSION={{item.IPVERSION}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：IPVERSION=IPv4 时必选 --- -#}
        {%- if item.IPVERSION == 'IPv4' -%}
            NEXTHOP="{{item.NEXTHOP}}",
        {%- endif -%}
        {#- --- 条件必选：IPVERSION=IPv6 时必选 --- -#}
        {%- if item.IPVERSION == 'IPv6' -%}
            NEXTHOP6="{{item.NEXTHOP6}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- for item in add_mqcpolicy_list_1 -%}
    ADD MQCPOLICY:
    {#- --- 必选参数 --- -#}
    POLICYNAME="{{item.POLICYNAME}}",
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_mqcpolicynode_list_1 -%}
    ADD MQCPOLICYNODE:
    {#- --- 必选参数 --- -#}
    POLICYNAME="{{item.POLICYNAME}}",
    BEHAVIORNAME="{{item.BEHAVIORNAME}}",
    CLASSIFIERNAME="{{item.CLASSIFIERNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.PRECEDENCE is not none -%}
        PRECEDENCE={{item.PRECEDENCE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_qosapplication_list_1 -%}
    ADD QOSAPPLICATION:
    {#- --- 必选参数 --- -#}
    POLICYNAME="{{item.POLICYNAME}}",
    IFNAME="{{item.IFNAME}}",
    DIRECTION={{item.DIRECTION}},
    ;
{%- endfor -%}
```

```jinja2
{%- for item in mod_mqcpolicy_list_1 -%}
    MOD MQCPOLICY:
    {#- --- 必选参数 --- -#}
    POLICYNAME="{{item.POLICYNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.STCENABLE is not none -%}
        STCENABLE={{item.STCENABLE}},
    {%- endif -%}
    ;
{%- endfor -%}
```


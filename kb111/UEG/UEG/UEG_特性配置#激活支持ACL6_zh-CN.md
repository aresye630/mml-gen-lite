---
id: ''
name: 激活支持ACL6
ne_type: UEG
type: feature
description: 本操作指导介绍在运行网络中激活ACL6功能特性的操作过程。  ACL6是一种IPv6包过滤技术，通过对IPv6报文的源地址、报文目的地址、协议号、源端口号、目的端口号（上述5个字段一般称为五元组，其中源端口号和目的端口号只对TCP和UDP协议有意义）等信息对照ACL6规则数据库进行匹配，符合某一规则集合的数据包视为同一数据流，将按照ACL规则集合中规定的动作采取相同的处理策略，动作包括：允许（Permit）、拒绝（Deny）等，防止设备被非法报文攻击，保证网络安全。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝S","MEC 特性指南（风筝S）","UEG特性指南","IP基本特性","IPFD-020400 IP可靠性","IPFD-020402 ACL","特性配置","激活支持ACL6"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
本操作指导介绍在运行网络中激活ACL6功能特性的操作过程。ACL6是一种IPv6包过滤技术，通过对IPv6报文的源地址、报文目的地址、协议号、源端口号、目的端口号（上述5个字段一般称为五元组，其中源端口号和目的端口号只对TCP和UDP协议有意义）等信息对照ACL6规则数据库进行匹配，符合某一规则集合的数据包视为同一数据流，将按照ACL规则集合中规定的动作采取相同的处理策略，动作包括：允许（Permit）、拒绝（Deny）等，防止设备被非法报文攻击，保证网络安全。

## 必备事项
前提条件

* 操作人员已经登录网络管理系统NMS（Network Management System）。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    add_aclgroup6_list:
      type: items
      properties:
        ACLNAME:
          name: 'IPv6 ACL规则组标识'
          type: string
          maxLength: 32
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        ACLTYPE:
          name: '规则组类型'
          type: string
          enum:
          - Advance
          - Basic
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_aclrulebas6_list:
      type: items
      properties:
        ACLNAME:
          name: 'IPv6 ACL规则组标识'
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
          data_source: '本端规划'
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
          data_source: '本端规划'
          pattern: ''
          default: ''
        ACLSOURCEIP:
          name: '源IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        ACLSRCWILD:
          name: '源IPv6地址正掩码长度'
          type: integer
          minimum: 0
          maximum: 128
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_aclruleadv6_list:
      type: items
      properties:
        ACLNAME:
          name: 'IPv6 ACL规则组标识'
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
          data_source: '本端规划'
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
          data_source: '本端规划'
          pattern: ''
          default: ''
        ACLPROTOCOLTYPE:
          name: '协议选项类型'
          type: string
          enum:
          - Number
          - WellKnow
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: Number
        ACLPROTOCOL:
          name: '协议类型值'
          type: integer
          minimum: 0
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ACLSOURCEIP:
          name: '源IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        ACLSRCWILD:
          name: '源IPv6地址正掩码长度'
          type: integer
          minimum: 0
          maximum: 128
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        ACLDESTIP:
          name: '目的IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ACLDESTWILD:
          name: '目的IPv6地址正掩码长度'
          type: integer
          minimum: 0
          maximum: 128
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_aclruleadv6_list_1:
      type: items
      properties:
        ACLNAME:
          name: 'IPv6 ACL规则组标识'
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
          data_source: '本端规划'
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
          data_source: '本端规划'
          pattern: ''
          default: ''
        ACLPROTOCOLTYPE:
          name: '协议选项类型'
          type: string
          enum:
          - Number
          - WellKnow
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: Number
        ACLPROTOCOL:
          name: '协议类型值'
          type: integer
          minimum: 0
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ACLSOURCEIP:
          name: '源IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        ACLSRCWILD:
          name: '源IPv6地址正掩码长度'
          type: integer
          minimum: 0
          maximum: 128
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        ACLDESTIP:
          name: '目的IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ACLDESTWILD:
          name: '目的IPv6地址正掩码长度'
          type: integer
          minimum: 0
          maximum: 128
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ACLICMPNAME:
          name: 'ICMP名称'
          type: string
          enum:
          - Custom
          - Echo
          - EchoReply
          - ErrHeaderField
          - FragTimeExceeded
          - HopLimitExceeded
          - HostAdminProhib
          - HostUnreachable
          - NeighborAdvertisement
          - NeighborSolicitation
          - NetworkUnreachable
          - PacketTooBig
          - PortUnreachable
          - Redirect
          - RouterAdvertisement
          - RouterSolicitation
          - Unconfiged
          - UnknownIpv6Opt
          - UnknownNextHdr
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ACLICMPTYPE:
          name: '网络控制管理协议类型'
          type: integer
          minimum: 0
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ACLICMPCODE:
          name: '网络控制管理协议消息码'
          type: integer
          minimum: 0
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_aclruleadv6_list_2:
      type: items
      properties:
        ACLNAME:
          name: 'IPv6 ACL规则组标识'
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
          data_source: '本端规划'
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
          data_source: '本端规划'
          pattern: ''
          default: ''
        ACLPROTOCOLTYPE:
          name: '协议选项类型'
          type: string
          enum:
          - Number
          - WellKnow
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: Number
        ACLPROTOCOL:
          name: '协议类型值'
          type: integer
          minimum: 0
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ACLSOURCEIP:
          name: '源IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        ACLSRCWILD:
          name: '源IPv6地址正掩码长度'
          type: integer
          minimum: 0
          maximum: 128
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        ACLDESTIP:
          name: '目的IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ACLDESTWILD:
          name: '目的IPv6地址正掩码长度'
          type: integer
          minimum: 0
          maximum: 128
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ACLSRCPORTOP:
          name: '源端口范围类型'
          type: string
          enum:
          - Eq
          - Gt
          - Lt
          - Neq
          - Range
          - Unconfiged
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ACLSRCPORTBEGIN:
          name: '源端口的开始端口号'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ACLSRCPORTEND:
          name: '源端口的结束端口号'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ACLDESTPORTOP:
          name: '目的端口范围类型'
          type: string
          enum:
          - Eq
          - Gt
          - Lt
          - Neq
          - Range
          - Unconfiged
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ACLDESTPORTBEGIN:
          name: '目的端口的开始端口号'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ACLDESTPORTEND:
          name: '目的端口的结束端口号'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_aclgroup6_list_1:
      type: items
      properties:
        ACLNAME:
          name: 'IPv6 ACL规则组标识'
          type: string
          maxLength: 32
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_aclruleadv6_list_3:
      type: items
      properties:
        ACLNAME:
          name: 'IPv6 ACL规则组标识'
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
          data_source: '本端规划'
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
          data_source: '本端规划'
          pattern: ''
          default: ''
        ACLPROTOCOL:
          name: '协议类型值'
          type: integer
          minimum: 0
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ACLSOURCEIP:
          name: '源IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        ACLSRCWILD:
          name: '源IPv6地址正掩码长度'
          type: integer
          minimum: 0
          maximum: 128
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        ACLPROTOCOLTYPE:
          name: '协议选项类型'
          type: string
          enum:
          - Number
          - WellKnow
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: Number
  examples:
    add_aclgroup6_list:
    - ACLNAME: '3000'
      ACLTYPE: 规则组类型
    add_aclrulebas6_list:
    - ACLNAME: '3000'
      ACLRULENAME: 'rule_5'
      ACLACTION: Permit
      ACLSOURCEIP: '2001:db8::1'
      ACLSRCWILD: 24
    add_aclruleadv6_list:
    - ACLNAME: '3000'
      ACLRULENAME: 'rule_5'
      ACLACTION: Permit
      ACLPROTOCOLTYPE: 协议选项类型
      ACLPROTOCOL: 协议类型值
      ACLSOURCEIP: '2001:db8::1'
      ACLSRCWILD: 24
      ACLDESTIP: '目的IPV6地址'
      ACLDESTWILD: 目的IPV6地址正掩码长度
    add_aclruleadv6_list_1:
    - ACLNAME: '3000'
      ACLRULENAME: 'rule_5'
      ACLACTION: Permit
      ACLPROTOCOLTYPE: 协议选项类型
      ACLPROTOCOL: 协议类型值
      ACLSOURCEIP: '2001:db8::1'
      ACLSRCWILD: 24
      ACLDESTIP: '目的IPV6地址'
      ACLDESTWILD: 目的IPV6地址正掩码长度
      ACLICMPNAME: ICMP名称
      ACLICMPTYPE: 网络控制管理协议类型
      ACLICMPCODE: 网络控制管理协议消息码
    add_aclruleadv6_list_2:
    - ACLNAME: '3000'
      ACLRULENAME: 'rule_5'
      ACLACTION: Permit
      ACLPROTOCOLTYPE: 协议选项类型
      ACLPROTOCOL: 协议类型值
      ACLSOURCEIP: '2001:db8::1'
      ACLSRCWILD: 24
      ACLDESTIP: '目的IPV6地址'
      ACLDESTWILD: 目的IPV6地址正掩码长度
      ACLSRCPORTOP: 源端口范围类型
      ACLSRCPORTBEGIN: 源端口号开始端口号
      ACLSRCPORTEND: 源端口号结束端口号
      ACLDESTPORTOP: 目的端口范围类型
      ACLDESTPORTBEGIN: 目的端口号开始端口号
      ACLDESTPORTEND: 目的端口号结束端口号
    add_aclgroup6_list_1:
    - ACLNAME: '3000'
    add_aclruleadv6_list_3:
    - ACLNAME: '3000'
      ACLRULENAME: 'rule_5'
      ACLACTION: Permit
      ACLPROTOCOL: 0
      ACLSOURCEIP: '2001:db8::1'
      ACLSRCWILD: 24
      ACLPROTOCOLTYPE: Number
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 增加ACL6规则组。

### 在“MML命令行-VNRS\_VNFC”窗口上执行：

```jinja2
{%- for item in add_aclgroup6_list -%}
    ADD ACLGROUP6:
    {#- --- 必选参数 --- -#}
    ACLNAME="{{item.ACLNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.ACLTYPE is not none -%}
        ACLTYPE={{item.ACLTYPE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 参数"ACLTYPE"（规则组类型）在"ACLNAME"（规则组名称）为数字字符串时可以不用输入。

### 2 增加ACL6规则。

### 根据不同的协议选择不同的配置。

#### 2.1 协议类型是IP

#### 在“MML命令行-VNRS\_VNFC”窗口上执行：

```jinja2
{%- if is_scenario_protocol_ip -%}
    {%- for item in add_aclrulebas6_list -%}
        ADD ACLRULEBAS6:
        {#- --- 必选参数 --- -#}
        ACLNAME="{{item.ACLNAME}}",
        ACLRULENAME="{{item.ACLRULENAME}}",
        ACLACTION={{item.ACLACTION}},
        {#- --- 可选参数 --- -#}
        {%- if item.ACLSOURCEIP is not none -%}
            ACLSOURCEIP="{{item.ACLSOURCEIP}}",
        {%- endif -%}
        {%- if item.ACLSRCWILD is not none -%}
            ACLSRCWILD={{item.ACLSRCWILD}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_protocol_ip -%}
    {%- for item in add_aclruleadv6_list -%}
        ADD ACLRULEADV6:
        {#- --- 必选参数 --- -#}
        ACLNAME="{{item.ACLNAME}}",
        ACLRULENAME="{{item.ACLRULENAME}}",
        ACLACTION={{item.ACLACTION}},
        {#- --- 可选参数 --- -#}
        {%- if item.ACLPROTOCOLTYPE is not none -%}
            ACLPROTOCOLTYPE={{item.ACLPROTOCOLTYPE}},
        {%- endif -%}
        {%- if item.ACLSOURCEIP is not none -%}
            ACLSOURCEIP="{{item.ACLSOURCEIP}}",
        {%- endif -%}
        {%- if item.ACLSRCWILD is not none -%}
            ACLSRCWILD={{item.ACLSRCWILD}},
        {%- endif -%}
        {%- if item.ACLDESTIP is not none -%}
            ACLDESTIP="{{item.ACLDESTIP}}",
        {%- endif -%}
        {%- if item.ACLDESTWILD is not none -%}
            ACLDESTWILD={{item.ACLDESTWILD}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：ACLPROTOCOLTYPE=Number 时必选 --- -#}
        {%- if item.ACLPROTOCOLTYPE == 'Number' -%}
            ACLPROTOCOL={{item.ACLPROTOCOL}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 基本ACL6的范围段为2000～2999，高级ACL的范围段为3000～3999，增加规则时ACL规则组必须创建。

#### 基本ACL6只能基于源IP地址和掩码进行匹配。

#### 高级ACL6可以基于五元组进行匹配（协议类型、本端IP地址、对端IP地址、本端端口、对端端口）。

#### 2.2 协议类型是ICMP

#### 在“MML命令行-VNRS\_VNFC”窗口上执行：

```jinja2
{%- if is_scenario_protocol_icmp -%}
    {%- for item in add_aclruleadv6_list_1 -%}
        ADD ACLRULEADV6:
        {#- --- 必选参数 --- -#}
        ACLNAME="{{item.ACLNAME}}",
        ACLRULENAME="{{item.ACLRULENAME}}",
        ACLACTION={{item.ACLACTION}},
        {#- --- 可选参数 --- -#}
        {%- if item.ACLPROTOCOLTYPE is not none -%}
            ACLPROTOCOLTYPE={{item.ACLPROTOCOLTYPE}},
        {%- endif -%}
        {%- if item.ACLSOURCEIP is not none -%}
            ACLSOURCEIP="{{item.ACLSOURCEIP}}",
        {%- endif -%}
        {%- if item.ACLSRCWILD is not none -%}
            ACLSRCWILD={{item.ACLSRCWILD}},
        {%- endif -%}
        {%- if item.ACLDESTIP is not none -%}
            ACLDESTIP="{{item.ACLDESTIP}}",
        {%- endif -%}
        {%- if item.ACLDESTWILD is not none -%}
            ACLDESTWILD={{item.ACLDESTWILD}},
        {%- endif -%}
        {%- if item.ACLICMPNAME is not none -%}
            ACLICMPNAME={{item.ACLICMPNAME}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：ACLPROTOCOLTYPE=Number 时必选 --- -#}
        {%- if item.ACLPROTOCOLTYPE == 'Number' -%}
            ACLPROTOCOL={{item.ACLPROTOCOL}},
        {%- endif -%}
        {#- --- 条件必选：ACLICMPNAME=Custom 时必选 --- -#}
        {%- if item.ACLICMPNAME == 'Custom' -%}
            ACLICMPTYPE={{item.ACLICMPTYPE}},
        {%- endif -%}
        {#- --- 条件必选：ACLICMPNAME=Custom 时必选 --- -#}
        {%- if item.ACLICMPNAME == 'Custom' -%}
            ACLICMPCODE={{item.ACLICMPCODE}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 参数"ACLICMPNAME"可以直接输入知名ICMP报文类型，对于知名类型，"ACLICMPTYPE"和"ACLICMPCODE"不需要输入。

#### 参数"ACLICMPNAME"输入为"Custom"时，用户可以自定义输入"ACLICMPTYPE"和"ACLICMPCODE"。

#### 当ICMP类型和ICMP编码都不输入时，规则将匹配所有的ICMP报文；当仅输入ICMP类型时，规则将匹配该类型所有的ICMP报文；当ICMP类型不输入时输入的ICMP编码无效。

#### 2.3 协议类型是TCP或UDP

#### 在“MML命令行-VNRS\_VNFC”窗口上执行：

```jinja2
{%- if is_scenario_protocol_tcp_udp -%}
    {%- for item in add_aclruleadv6_list_2 -%}
        ADD ACLRULEADV6:
        {#- --- 必选参数 --- -#}
        ACLNAME="{{item.ACLNAME}}",
        ACLRULENAME="{{item.ACLRULENAME}}",
        ACLACTION={{item.ACLACTION}},
        {#- --- 可选参数 --- -#}
        {%- if item.ACLPROTOCOLTYPE is not none -%}
            ACLPROTOCOLTYPE={{item.ACLPROTOCOLTYPE}},
        {%- endif -%}
        {%- if item.ACLSOURCEIP is not none -%}
            ACLSOURCEIP="{{item.ACLSOURCEIP}}",
        {%- endif -%}
        {%- if item.ACLSRCWILD is not none -%}
            ACLSRCWILD={{item.ACLSRCWILD}},
        {%- endif -%}
        {%- if item.ACLDESTIP is not none -%}
            ACLDESTIP="{{item.ACLDESTIP}}",
        {%- endif -%}
        {%- if item.ACLDESTWILD is not none -%}
            ACLDESTWILD={{item.ACLDESTWILD}},
        {%- endif -%}
        {%- if item.ACLSRCPORTOP is not none -%}
            ACLSRCPORTOP={{item.ACLSRCPORTOP}},
        {%- endif -%}
        {%- if item.ACLDESTPORTOP is not none -%}
            ACLDESTPORTOP={{item.ACLDESTPORTOP}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：ACLPROTOCOLTYPE=Number 时必选 --- -#}
        {%- if item.ACLPROTOCOLTYPE == 'Number' -%}
            ACLPROTOCOL={{item.ACLPROTOCOL}},
        {%- endif -%}
        {#- --- 条件必选：ACLSRCPORTOP=Eq/Gt/Neq/Range 时必选 --- -#}
        {%- if item.ACLSRCPORTOP in ['Eq', 'Gt', 'Neq', 'Range'] -%}
            ACLSRCPORTBEGIN={{item.ACLSRCPORTBEGIN}},
        {%- endif -%}
        {#- --- 条件必选：ACLSRCPORTOP=Lt/Range 时必选 --- -#}
        {%- if item.ACLSRCPORTOP in ['Lt', 'Range'] -%}
            ACLSRCPORTEND={{item.ACLSRCPORTEND}},
        {%- endif -%}
        {#- --- 条件必选：ACLDESTPORTOP=Eq/Gt/Neq/Range 时必选 --- -#}
        {%- if item.ACLDESTPORTOP in ['Eq', 'Gt', 'Neq', 'Range'] -%}
            ACLDESTPORTBEGIN={{item.ACLDESTPORTBEGIN}},
        {%- endif -%}
        {#- --- 条件必选：ACLDESTPORTOP=Lt/Range 时必选 --- -#}
        {%- if item.ACLDESTPORTOP in ['Lt', 'Range'] -%}
            ACLDESTPORTEND={{item.ACLDESTPORTEND}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 当端口号的操作符为"Lt"时，需要输入结束端口号。当端口号的操作符为"Gt"、"Eq"、"Neq"时，需要输入起始端口号。当端口号的操作符为"Range"时，起始端口号同结束端口号都需要输入。

```jinja2
{%- for item in add_aclgroup6_list_1 -%}
    ADD ACLGROUP6:
    {#- --- 必选参数 --- -#}
    ACLNAME="{{item.ACLNAME}}",
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_aclruleadv6_list_3 -%}
    ADD ACLRULEADV6:
    {#- --- 必选参数 --- -#}
    ACLNAME="{{item.ACLNAME}}",
    ACLRULENAME="{{item.ACLRULENAME}}",
    ACLACTION={{item.ACLACTION}},
    {#- --- 可选参数 --- -#}
    {%- if item.ACLSOURCEIP is not none -%}
        ACLSOURCEIP="{{item.ACLSOURCEIP}}",
    {%- endif -%}
    {%- if item.ACLSRCWILD is not none -%}
        ACLSRCWILD={{item.ACLSRCWILD}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：ACLPROTOCOLTYPE=Number 时必选 --- -#}
    {%- if item.ACLPROTOCOLTYPE == 'Number' -%}
        ACLPROTOCOL={{item.ACLPROTOCOL}},
    {%- endif -%}
    ;
{%- endfor -%}
```


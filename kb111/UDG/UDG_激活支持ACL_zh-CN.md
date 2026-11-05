---
id: ''
name: 激活支持ACL
ne_type: UDG
type: feature
description: 本操作指导介绍在运行网络中激活ACL功能特性的操作过程。  ACL是一种IP包过滤技术，通过对IP报文的源地址、报文目的地址、协议号、源端口号、目的端口号（上述5个字段一般称为五元组，其中源端口号和目的端口号只对TCP和UDP协议有意义）等信息对照ACL规则数据库进行匹配，符合某一规则集合的数据包视为同一数据流，将按照ACL规则集合中规定的动作采取相同的处理策略，动作包括：允许（Permit）、拒绝（Deny）等。
risk_level: ''
doc_source: ["特性部署","特性指南","UDG特性指南","IP基本特性","IPFD-012000 IP可靠性","IPFD-012002 ACL","特性配置","激活支持ACL"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本操作指导介绍在运行网络中激活ACL功能特性的操作过程。ACL是一种IP包过滤技术，通过对IP报文的源地址、报文目的地址、协议号、源端口号、目的端口号（上述5个字段一般称为五元组，其中源端口号和目的端口号只对TCP和UDP协议有意义）等信息对照ACL规则数据库进行匹配，符合某一规则集合的数据包视为同一数据流，将按照ACL规则集合中规定的动作采取相同的处理策略，动作包括：允许（Permit）、拒绝（Deny）等。

## 必备事项
前提条件

* 操作人员已经登录华为操作维护系统。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
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
        ACLTYPE:
          name: '规则组类型'
          type: string
          enum:
          - Advance
          - Basic
          - Ethernet
          - Interface
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_aclgroup_list_1:
      type: items
      properties:
        ACLNAME:
          name: 'ACL规则组标识'
          type: string
          maxLength: 32
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_aclrulebas4_list:
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
          name: '源IP地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: '0.0.0.0'
        ACLSRCWILD:
          name: '源IP地址反掩码'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: '255.255.255.255'
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
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        ACLSOURCEIP:
          name: '源IP地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: '0.0.0.0'
        ACLSRCWILD:
          name: '源IP地址反掩码'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: '255.255.255.255'
        ACLDESTIP:
          name: '目的IP地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: '0.0.0.0'
        ACLDESTWILD:
          name: '目的IP地址反掩码'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: '255.255.255.255'
    add_aclruleadv4_list_1:
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
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        ACLSOURCEIP:
          name: '源IP地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: '0.0.0.0'
        ACLSRCWILD:
          name: '源IP地址反掩码'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: '255.255.255.255'
        ACLDESTIP:
          name: '目的IP地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: '0.0.0.0'
        ACLDESTWILD:
          name: '目的IP地址反掩码'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: '255.255.255.255'
        ACLICMPNAME:
          name: 'ICMP名称'
          type: string
          enum:
          - AddressMaskReply
          - AddressMaskRequest
          - Custom
          - Echo
          - EchoReply
          - FragmentneedDFset
          - HostRedirect
          - HostTosRedirect
          - HostUnreachable
          - InformationReply
          - InformationRequest
          - NetRedirect
          - NetTosRedirect
          - NetUnreachable
          - ParameterProblem
          - PortUnreachable
          - ProtocolUnreachable
          - ReassemblyTimeout
          - SourceQuench
          - SourceRouteFailed
          - TimestampReply
          - TimestampRequest
          - TtlExceeded
          - Unconfiged
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
    add_aclruleadv4_list_2:
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
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        ACLSOURCEIP:
          name: '源IP地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: '0.0.0.0'
        ACLSRCWILD:
          name: '源IP地址反掩码'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: '255.255.255.255'
        ACLDESTIP:
          name: '目的IP地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: '0.0.0.0'
        ACLDESTWILD:
          name: '目的IP地址反掩码'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: '255.255.255.255'
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
    add_aclruleadv4_list_3:
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
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        ACLSOURCEIP:
          name: '源IP地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: '0.0.0.0'
        ACLSRCWILD:
          name: '源IP地址反掩码'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: '255.255.255.255'
        ACLDESTIP:
          name: '目的IP地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: '0.0.0.0'
        ACLDESTWILD:
          name: '目的IP地址反掩码'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: '255.255.255.255'
    add_aclruleeth_list:
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
        ACLSRCMAC:
          name: '源MAC地址'
          type: string
          maxLength: 18
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_aclruleif_list:
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
        IFNAME:
          name: '接口名'
          type: string
          maxLength: 49
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    add_aclgroup_list:
    - ACLNAME: '3000'
      ACLTYPE: ACL规则类型
    add_aclgroup_list_1:
    - ACLNAME: '3001'
    add_aclrulebas4_list:
    - ACLNAME: '2000'
      ACLRULENAME: 'rule_bas'
      ACLACTION: Deny
      ACLSOURCEIP: '10.1.2.2'
      ACLSRCWILD: '0.0.0.255'
    add_aclruleadv4_list:
    - ACLNAME: '3000'
      ACLRULENAME: 'rule_adv'
      ACLACTION: Permit
      ACLPROTOCOL: 0
      ACLSOURCEIP: '10.1.2.2'
      ACLSRCWILD: '0.0.0.255'
      ACLDESTIP: '192.168.1.1'
      ACLDESTWILD: '0.0.0.255'
    add_aclruleadv4_list_1:
    - ACLNAME: '3000'
      ACLRULENAME: 'rule_adv'
      ACLACTION: Permit
      ACLPROTOCOL: 0
      ACLSOURCEIP: '10.1.2.2'
      ACLSRCWILD: '0.0.0.255'
      ACLDESTIP: '192.168.1.1'
      ACLDESTWILD: '0.0.0.255'
      ACLICMPNAME: ICMP名称
      ACLICMPTYPE: 网络控制管理协议类型
      ACLICMPCODE: 网络控制管理协议消息码
    add_aclruleadv4_list_2:
    - ACLNAME: '3000'
      ACLRULENAME: 'rule_adv'
      ACLACTION: Permit
      ACLPROTOCOL: 0
      ACLSOURCEIP: '10.1.2.2'
      ACLSRCWILD: '0.0.0.255'
      ACLDESTIP: '192.168.1.1'
      ACLDESTWILD: '0.0.0.255'
      ACLSRCPORTOP: 源端口范围类型
      ACLSRCPORTBEGIN: 源端口号开始端口号
      ACLSRCPORTEND: 源端口号结束端口号
      ACLDESTPORTOP: 目的端口范围类型
      ACLDESTPORTBEGIN: 目的端口号开始端口号
      ACLDESTPORTEND: 目的端口号结束端口号
    add_aclruleadv4_list_3:
    - ACLNAME: '3001'
      ACLRULENAME: 'adv_2'
      ACLACTION: Permit
      ACLPROTOCOL: 0
      ACLSOURCEIP: '10.1.1.2'
      ACLSRCWILD: '0.0.0.0'
      ACLDESTIP: '192.168.1.1'
      ACLDESTWILD: '0.0.0.0'
    add_aclruleeth_list:
    - ACLNAME: '4000'
      ACLRULENAME: 'rule_eth'
      ACLACTION: Permit
      ACLSRCMAC: '00E0-FC11-2233'
    add_aclruleif_list:
    - ACLNAME: '1000'
      ACLRULENAME: 'rule_if'
      ACLACTION: Permit
      IFNAME: 'Ethernet64/0/5'
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 增加ACL规则组。

### 在“MML命令行-UDG”窗口上执行：

```jinja2
{%- for item in add_aclgroup_list -%}
    ADD ACLGROUP:
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

#### 1.1 //添加ACL规则组。添加组号为3001的扩展规则组。

```jinja2
{%- for item in add_aclgroup_list_1 -%}
    ADD ACLGROUP:
    {#- --- 必选参数 --- -#}
    ACLNAME="{{item.ACLNAME}}",
    ;
{%- endfor -%}
```

### 2 增加基本ACL规则

### 在“MML命令行-UDG”窗口上执行：

```jinja2
{%- for item in add_aclrulebas4_list -%}
    ADD ACLRULEBAS4:
    {#- --- 必选参数 --- -#}
    ACLNAME="{{item.ACLNAME}}",
    ACLRULENAME="{{item.ACLRULENAME}}",
    ACLACTION={{item.ACLACTION}},
    {#- --- 可选参数 --- -#}
    {%- if item.ACLSOURCEIP is not none -%}
        ACLSOURCEIP="{{item.ACLSOURCEIP}}",
    {%- endif -%}
    {%- if item.ACLSRCWILD is not none -%}
        ACLSRCWILD="{{item.ACLSRCWILD}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 基本ACL的范围段为2000～2999，增加规则时ACL规则组必须创建。

### 基本ACL只能基于源IP地址和掩码进行匹配。

### 3 增加高级ACL规则。

### 根据不同的协议选择不同的配置。

### 高级ACL的范围段为3000～3999，增加规则时ACL规则组必须创建。

### 高级ACL可以基于五元组进行匹配（协议类型、本端IP地址、对端IP地址、本端端口、对端端口）。

#### 3.1 协议类型是IP

#### 在“MML命令行-UDG”窗口上执行：

```jinja2
{%- if is_scenario_protocol_ip -%}
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
{%- endif -%}
```

#### 3.2 协议类型是ICMP

#### 在“MML命令行-UDG”窗口上执行：

```jinja2
{%- if is_scenario_protocol_icmp -%}
    {%- for item in add_aclruleadv4_list_1 -%}
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
        {%- if item.ACLICMPNAME is not none -%}
            ACLICMPNAME={{item.ACLICMPNAME}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
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

#### 3.3 协议类型是TCP或UDP

#### 在“MML命令行-UDG”窗口上执行：

```jinja2
{%- if is_scenario_protocol_tcp_udp -%}
    {%- for item in add_aclruleadv4_list_2 -%}
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
        {%- if item.ACLSRCPORTOP is not none -%}
            ACLSRCPORTOP={{item.ACLSRCPORTOP}},
        {%- endif -%}
        {%- if item.ACLDESTPORTOP is not none -%}
            ACLDESTPORTOP={{item.ACLDESTPORTOP}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
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

#### 当端口号的操作符为"Lt"时，需要输入结束端口号，当端口号的操作符为"Gt"、"Eq"、"Neq"时，需要输入起始端口号，当端口号的操作符为"Range"时，起始端口号同结束端口号都需要输入

#### 3.4 //添加ACL规则。添加规则名称为"adv\_2"和"adv\_3"的规则。

```jinja2
{%- for item in add_aclruleadv4_list_3 -%}
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

### 4 增加以太ACL规则

### 在“MML命令行-UDG”窗口上执行：

```jinja2
{%- for item in add_aclruleeth_list -%}
    ADD ACLRULEETH:
    {#- --- 必选参数 --- -#}
    ACLNAME="{{item.ACLNAME}}",
    ACLRULENAME="{{item.ACLRULENAME}}",
    ACLACTION={{item.ACLACTION}},
    {#- --- 可选参数 --- -#}
    {%- if item.ACLSRCMAC is not none -%}
        ACLSRCMAC="{{item.ACLSRCMAC}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 5 增加接口ACL规则

### 在“MML命令行-UDG”窗口上执行：

```jinja2
{%- for item in add_aclruleif_list -%}
    ADD ACLRULEIF:
    {#- --- 必选参数 --- -#}
    ACLNAME="{{item.ACLNAME}}",
    ACLRULENAME="{{item.ACLRULENAME}}",
    ACLACTION={{item.ACLACTION}},
    {#- --- 可选参数 --- -#}
    {%- if item.IFNAME is not none -%}
        IFNAME="{{item.IFNAME}}",
    {%- endif -%}
    ;
{%- endfor -%}
```


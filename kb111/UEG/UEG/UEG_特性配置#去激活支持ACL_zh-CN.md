---
id: ''
name: 去激活支持ACL
ne_type: UEG
type: feature
description: 本操作指导介绍在运行网络中去激活ACL功能特性的操作过程。  ACL是一种IP包过滤技术，通过对IP报文的源地址、报文目的地址、协议号、源端口号、目的端口号（上述5个字段一般称为五元组，其中源端口号和目的端口号只对TCP和UDP协议有意义）等信息对照ACL规则数据库进行匹配，符合某一规则集合的数据包视为同一数据流，将按照ACL规则集合中规定的动作采取相同的处理策略，动作包括：允许（Permit）、拒绝（Deny）等。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝S","MEC 特性指南（风筝S）","UEG特性指南","IP基本特性","IPFD-020400 IP可靠性","IPFD-020402 ACL","特性配置","去激活支持ACL"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
本操作指导介绍在运行网络中去激活ACL功能特性的操作过程。ACL是一种IP包过滤技术，通过对IP报文的源地址、报文目的地址、协议号、源端口号、目的端口号（上述5个字段一般称为五元组，其中源端口号和目的端口号只对TCP和UDP协议有意义）等信息对照ACL规则数据库进行匹配，符合某一规则集合的数据包视为同一数据流，将按照ACL规则集合中规定的动作采取相同的处理策略，动作包括：允许（Permit）、拒绝（Deny）等。

## 必备事项
前提条件

* 操作人员已经登录网络管理系统NMS（Network Management System）。
* 支持包过滤功能特性已经激活。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    rmv_aclruleif_list:
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
        ACLRULENAME:
          name: '规则名称'
          type: string
          maxLength: 32
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    rmv_aclruleeth_list:
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
        ACLRULENAME:
          name: '规则名称'
          type: string
          maxLength: 32
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    rmv_aclruleadv4_list:
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
        ACLRULENAME:
          name: '规则名称'
          type: string
          maxLength: 32
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    rmv_aclrulebas4_list:
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
        ACLRULENAME:
          name: '规则名称'
          type: string
          maxLength: 32
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    rmv_aclgroup_list:
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
  examples:
    rmv_aclruleif_list:
    - ACLNAME: 'ACL规则组标识'
      ACLRULENAME: '规则名称'
    rmv_aclruleeth_list:
    - ACLNAME: 'ACL规则组标识'
      ACLRULENAME: '规则名称'
    rmv_aclruleadv4_list:
    - ACLNAME: 'ACL规则组标识'
      ACLRULENAME: '规则名称'
    rmv_aclrulebas4_list:
    - ACLNAME: 'ACL规则组标识'
      ACLRULENAME: '规则名称'
    rmv_aclgroup_list:
    - ACLNAME: 'ACL规则组标识'
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 删除接口ACL规则。

### 在“MML命令行-VNRS\_VNFC”窗口上执行：

```jinja2
{%- for item in rmv_aclruleif_list -%}
    RMV ACLRULEIF:
    {#- --- 必选参数 --- -#}
    ACLNAME="{{item.ACLNAME}}",
    ACLRULENAME="{{item.ACLRULENAME}}",
    ;
{%- endfor -%}
```

### 2 删除以太ACL规则。

### 在“MML命令行-VNRS\_VNFC”窗口上执行：

```jinja2
{%- for item in rmv_aclruleeth_list -%}
    RMV ACLRULEETH:
    {#- --- 必选参数 --- -#}
    ACLNAME="{{item.ACLNAME}}",
    ACLRULENAME="{{item.ACLRULENAME}}",
    ;
{%- endfor -%}
```

### 3 删除高级ACL规则。

### 在“MML命令行-VNRS\_VNFC”窗口上执行：

```jinja2
{%- for item in rmv_aclruleadv4_list -%}
    RMV ACLRULEADV4:
    {#- --- 必选参数 --- -#}
    ACLNAME="{{item.ACLNAME}}",
    ACLRULENAME="{{item.ACLRULENAME}}",
    ;
{%- endfor -%}
```

### 4 删除基本ACL规则。

### 在“MML命令行-VNRS\_VNFC”窗口上执行：

```jinja2
{%- for item in rmv_aclrulebas4_list -%}
    RMV ACLRULEBAS4:
    {#- --- 必选参数 --- -#}
    ACLNAME="{{item.ACLNAME}}",
    ACLRULENAME="{{item.ACLRULENAME}}",
    ;
{%- endfor -%}
```

### 5 删除ACL规则组。

### 在“MML命令行-VNRS\_VNFC”窗口上执行：

```jinja2
{%- for item in rmv_aclgroup_list -%}
    RMV ACLGROUP:
    {#- --- 必选参数 --- -#}
    ACLNAME="{{item.ACLNAME}}",
    ;
{%- endfor -%}
```


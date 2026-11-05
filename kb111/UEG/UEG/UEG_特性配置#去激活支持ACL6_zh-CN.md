---
id: ''
name: 去激活支持ACL6
ne_type: UEG
type: feature
description: 本操作指导介绍在运行网络中去激活ACL6功能特性的操作过程。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝S","MEC 特性指南（风筝S）","UEG特性指南","IP基本特性","IPFD-020400 IP可靠性","IPFD-020402 ACL","特性配置","去激活支持ACL6"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
本操作指导介绍在运行网络中去激活ACL6功能特性的操作过程。

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
    rmv_aclruleadv6_list:
      type: items
      properties:
        ACLNAME:
          name: 'IPv6 ACL规则组标识'
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
    rmv_aclruleadv6_list_1:
      type: items
      properties:
        ACLNAME:
          name: 'IPv6 ACL规则组标识'
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
    rmv_aclgroup6_list:
      type: items
      properties:
        ACLNAME:
          name: 'IPv6 ACL规则组标识'
          type: string
          maxLength: 32
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    rmv_aclgroup6_list_1:
      type: items
      properties:
        ACLNAME:
          name: 'IPv6 ACL规则组标识'
          type: string
          maxLength: 32
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    rmv_aclruleadv6_list:
    - ACLNAME: 'IPv6 ACL规则组标识'
      ACLRULENAME: '规则名称'
    rmv_aclruleadv6_list_1:
    - ACLNAME: '3000'
      ACLRULENAME: 'rule_5'
    rmv_aclgroup6_list:
    - ACLNAME: 'IPv6 ACL规则组标识'
    rmv_aclgroup6_list_1:
    - ACLNAME: '3000'
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 删除ACL6规则。

### 在“MML命令行-VNRS\_VNFC”窗口上执行：

```jinja2
{%- for item in rmv_aclruleadv6_list -%}
    RMV ACLRULEADV6:
    {#- --- 必选参数 --- -#}
    ACLNAME="{{item.ACLNAME}}",
    ACLRULENAME="{{item.ACLRULENAME}}",
    ;
{%- endfor -%}
```

#### 1.1 //删除ACL6规则。删除规则名称为"rule\_5"规则。

```jinja2
{%- for item in rmv_aclruleadv6_list_1 -%}
    RMV ACLRULEADV6:
    {#- --- 必选参数 --- -#}
    ACLNAME="{{item.ACLNAME}}",
    ACLRULENAME="{{item.ACLRULENAME}}",
    ;
{%- endfor -%}
```

### 2 删除ACL6规则组。

### 在“MML命令行-VNRS\_VNFC”窗口上执行：

```jinja2
{%- for item in rmv_aclgroup6_list -%}
    RMV ACLGROUP6:
    {#- --- 必选参数 --- -#}
    ACLNAME="{{item.ACLNAME}}",
    ;
{%- endfor -%}
```

#### 2.1 //删除ACL6规则组。删除规则组号为3000的扩展规则组。

```jinja2
{%- for item in rmv_aclgroup6_list_1 -%}
    RMV ACLGROUP6:
    {#- --- 必选参数 --- -#}
    ACLNAME="{{item.ACLNAME}}",
    ;
{%- endfor -%}
```


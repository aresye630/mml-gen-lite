---
id: ''
name: 去激活支持ACL6
ne_type: UEG
type: feature
description: 本操作指导介绍在运行网络中去激活ACL6功能特性的操作过程。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝L","MEC 特性指南（风筝L）","UEG公共特性指南","IP基本特性","IPFD-020400 IP可靠性","IPFD-020402 ACL","特性配置","去激活支持ACL6"]
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
  examples:
    rmv_aclruleadv6_list:
    - ACLNAME: 'IPv6 ACL规则组标识'
      ACLRULENAME: '规则名称'
    rmv_aclgroup6_list:
    - ACLNAME: 'IPv6 ACL规则组标识'
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


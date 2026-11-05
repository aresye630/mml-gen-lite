---
id: ''
name: 去激活支持GRE
ne_type: UEG
type: feature
description: 本操作指导介绍在运行网络中去激活GRE功能的操作过程。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝S","MEC 特性指南（风筝S）","UEG特性指南","IP基本特性","IPFD-020600 VPN功能","IPFD-020602 GRE","特性配置","去激活支持GRE"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
本操作指导介绍在运行网络中去激活GRE功能的操作过程。

## 必备事项
前提条件

* 操作人员已经登录网络管理系统NMS（Network Management System）。
* GRE隧道已建立。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    rmv_gretunnel_list:
      type: items
      properties:
        TNLNAME:
          name: '隧道名称'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TNLTYPE:
          name: '隧道类型'
          type: string
          enum:
          - gre
          - gre6
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    rmv_gretunnel_list:
    - TNLNAME: '隧道名称'
      TNLTYPE: 隧道类型
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 删除GRE隧道。

### 在“MML命令行-UEG”窗口上执行：

```jinja2
{%- for item in rmv_gretunnel_list -%}
    RMV GRETUNNEL:
    {#- --- 必选参数 --- -#}
    TNLNAME="{{item.TNLNAME}}",
    TNLTYPE={{item.TNLTYPE}},
    ;
{%- endfor -%}
```


---
id: ''
name: 去激活QoS简单流分类（VNRS）
ne_type: UNC
type: feature
description: 本操作指导介绍在运行网络中去激活QoS简单流分类功能的操作过程。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","IP基本功能","IPFD-012001 QoS","特性配置","简单流分类配置（VNRS）","去激活QoS简单流分类（VNRS）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本操作指导介绍在运行网络中去激活QoS简单流分类功能的操作过程。

## 必备事项
前提条件

* 操作人员已经登录网络管理系统NMS（Network Management System）。
* 已经激活QoS简单流分类。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    rmv_qosiftrust_list:
      type: items
      properties:
        IFNAME:
          name: '接口名称'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    rmv_qosdifferserv_list:
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
    rmv_qosrdrvpn_list:
      type: items
      properties:
        IFNAME:
          name: '接口名称'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    rmv_qosifphb_list:
      type: items
      properties:
        IFNAME:
          name: '接口名称'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: ''
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
    rmv_qosiftrust_list:
    - IFNAME: '接口名称'
    rmv_qosdifferserv_list:
    - DSNAME: 'DS名称'
    rmv_qosrdrvpn_list:
    - IFNAME: '接口名称'
    rmv_qosifphb_list:
    - IFNAME: '接口名称'
      PHBTYPE: 出接口报文的优先级字段映射类型
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 删除对应的QOSIFTRUST。

### 在“MML命令行-UNC”窗口上执行：

```jinja2
{%- for item in rmv_qosiftrust_list -%}
    RMV QOSIFTRUST:
    {#- --- 必选参数 --- -#}
    IFNAME="{{item.IFNAME}}",
    ;
{%- endfor -%}
```

### 2 当需要删除对应的DiffServ域。

### 在“MML命令行-UNC”窗口上执行：

```jinja2
{%- for item in rmv_qosdifferserv_list -%}
    RMV QOSDIFFERSERV:
    {#- --- 必选参数 --- -#}
    DSNAME="{{item.DSNAME}}",
    ;
{%- endfor -%}
```

### 3 当需要删除对应的重定向至指定VPN的配置。

### 在“MML命令行-UNC”窗口上执行：

```jinja2
{%- for item in rmv_qosrdrvpn_list -%}
    RMV QOSRDRVPN:
    {#- --- 必选参数 --- -#}
    IFNAME="{{item.IFNAME}}",
    ;
{%- endfor -%}
```

### 4 当需要去激活QoS不检查PHB表。

### 在“MML命令行-UNC”窗口上执行：

```jinja2
{%- for item in rmv_qosifphb_list -%}
    RMV QOSIFPHB:
    {#- --- 必选参数 --- -#}
    IFNAME="{{item.IFNAME}}",
    PHBTYPE={{item.PHBTYPE}},
    ;
{%- endfor -%}
```


---
id: ''
name: 激活DSCP到VLAN优先级的映射（VNRS）
ne_type: UNC
type: feature
description: 本操作指导介绍，基于简单流分类，在运行网络配置DSCP和VLAN优先级映射关系。在需要配置DSCP和VLAN优先级映射关系的场景中使用此命令，此命令全局生效，将对出口报文中DSCP值按预期配置映射修改802.1p的值。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","IP基本功能","IPFD-012001 QoS","特性配置","简单流分类配置（VNRS）","激活DSCP到VLAN优先级的映射（VNRS）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本操作指导介绍，基于简单流分类，在运行网络配置DSCP和VLAN优先级映射关系。在需要配置DSCP和VLAN优先级映射关系的场景中使用此命令，此命令全局生效，将对出口报文中DSCP值按预期配置映射修改802.1p的值。

## 必备事项
前提条件

操作人员已经登录华为网络管理系统NMS（Network Management System）。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    add_dscpmap_list:
      type: items
      properties:
        DSCP:
          name: 'DSCP值'
          type: integer
          minimum: 0
          maximum: 63
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        TYPE:
          name: '优先级类型'
          type: string
          enum:
          - 8021p
          - exp
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VALUE:
          name: '优先级数值'
          type: integer
          minimum: 0
          maximum: 7
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    add_dscpmap_list:
    - DSCP: 62
      TYPE: 8201p
      VALUE: 5
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 配置DSCP到VLAN优先级的映射。

### 在“MML命令行-UNC”窗口上执行：

```jinja2
{%- for item in add_dscpmap_list -%}
    ADD DSCPMAP:
    {#- --- 必选参数 --- -#}
    DSCP={{item.DSCP}},
    TYPE={{item.TYPE}},
    VALUE={{item.VALUE}},
    ;
{%- endfor -%}
```


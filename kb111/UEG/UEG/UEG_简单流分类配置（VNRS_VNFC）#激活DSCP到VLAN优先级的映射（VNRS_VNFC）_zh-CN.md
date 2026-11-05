---
id: ''
name: 激活DSCP到VLAN优先级的映射（VNRS_VNFC）
ne_type: UEG
type: feature
description: 本操作指导介绍，基于简单流分类，在运行网络配置DSCP和VLAN优先级映射关系。在需要配置DSCP和VLAN优先级映射关系的场景中使用此命令，此命令全局生效，将对出口报文中DSCP值按预期配置映射修改802.1p的值。  NP卡场景下，不支持优先级类型EXP。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝S","MEC 特性指南（风筝S）","UEG特性指南","IP基本特性","IPFD-020400 IP可靠性","IPFD-020401 QoS","特性配置","简单流分类配置（VNRS_VNFC）","激活DSCP到VLAN优先级的映射（VNRS_VNFC）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
本操作指导介绍，基于简单流分类，在运行网络配置DSCP和VLAN优先级映射关系。在需要配置DSCP和VLAN优先级映射关系的场景中使用此命令，此命令全局生效，将对出口报文中DSCP值按预期配置映射修改802.1p的值。NP卡场景下，不支持优先级类型EXP。

## 必备事项
前提条件

操作人员已经登录华为网络管理系统NMS（Network Management System）。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
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
    add_dscpmap_list_1:
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
  examples:
    add_dscpmap_list:
    - DSCP: 62
      TYPE: 8201p
      VALUE: 5
    add_dscpmap_list_1:
    - DSCP: 62
      VALUE: 5
      TYPE: 8021p
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 配置DSCP到VLAN优先级的映射。

### 在“MML命令行-UEG”窗口上执行：

```jinja2
{%- for item in add_dscpmap_list -%}
    ADD_DSCPMAP:
    {#- --- 必选参数 --- -#}
    DSCP={{item.DSCP}},
    TYPE={{item.TYPE}},
    VALUE={{item.VALUE}},
    ;
{%- endfor -%}
```

### **ADD\_DSCPMAP**: DSCP=DSCP值,TYPE=优先级类型,VALUE=优先级数值;

```jinja2
{%- for item in add_dscpmap_list_1 -%}
    ADD DSCPMAP:
    {#- --- 必选参数 --- -#}
    DSCP={{item.DSCP}},
    VALUE={{item.VALUE}},
    TYPE={{item.TYPE}},
    ;
{%- endfor -%}
```


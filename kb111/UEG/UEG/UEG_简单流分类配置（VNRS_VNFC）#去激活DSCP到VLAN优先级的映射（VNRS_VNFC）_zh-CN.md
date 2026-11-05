---
id: ''
name: 去激活DSCP到VLAN优先级的映射（VNRS_VNFC）
ne_type: UEG
type: feature
description: 本操作指导介绍，在运行网络中，去激活DSCP到VLAN优先级映射功能的操作过程。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝S","MEC 特性指南（风筝S）","UEG特性指南","IP基本特性","IPFD-020400 IP可靠性","IPFD-020401 QoS","特性配置","简单流分类配置（VNRS_VNFC）","去激活DSCP到VLAN优先级的映射（VNRS_VNFC）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
本操作指导介绍，在运行网络中，去激活DSCP到VLAN优先级映射功能的操作过程。

## 必备事项
前提条件

前提条件

* 操作人员已经登录网络管理系统NMS（Network Management System）。
* 已经激活DSCP到VLAN优先级映射功能。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    rmv_dscpmap_list:
      type: items
      properties:
        DSCP:
          name: 'DSCP值'
          type: integer
          minimum: 0
          maximum: 63
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
    rmv_dscpmap_list:
    - DSCP: DSCP值
      TYPE: 优先级类型
      VALUE: 优先级数值
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 删除对应的DSCPMAP。

### 在“MML命令行-UEG”窗口上执行：

```jinja2
{%- for item in rmv_dscpmap_list -%}
    RMV DSCPMAP:
    {#- --- 必选参数 --- -#}
    DSCP={{item.DSCP}},
    TYPE={{item.TYPE}},
    VALUE={{item.VALUE}},
    ;
{%- endfor -%}
```


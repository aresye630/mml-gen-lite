---
id: GWFD-024303
name: 修改AAA计费的可选计费消息属性
ne_type: UEG
type: feature
description: 当计费策略发生改变时，需要在UEG上修改可选计费消息属性。  适用于PGW-C、SMF
tags: []
risk_level: ''
doc_source: ["业务配置","风筝L","MEC 特性指南（风筝L）","GW-C&SMF特性指南","GWFD-024300 系统管理","GWFD-024303 Radius功能","调整AAA计费参数","修改AAA计费的可选计费消息属性"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
当计费策略发生改变时，需要在UEG上修改可选计费消息属性。适用于PGW-C、SMF

## 必备事项
前提条件

完成配置RADIUS功能。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    set_rdsacctreqattr_list:
      type: items
      properties:
        RDSSVRGRPNAME:
          name: 'Radius Server Group名称'
          type: string
          maxLength: 31
          required: true
          description: '计费服务器所在的Radius服务器组，已通过**ADD RDSSVRGRP**进行配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        TRIGGERTYPE:
          name: '支持携带属性Trigger-type'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '**SET RDSACCTREQATTR**'
          data_source: '本端规划'
          pattern: ''
          default: ''
  examples:
    set_rdsacctreqattr_list:
    - RDSSVRGRPNAME: 'ss'
      TRIGGERTYPE: ENABLE
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 进入“MML命令行-UEG”窗口。

### 2 修改AAA计费的可选计费消息属性，支持携带属性Trigger-type。

```jinja2
{%- for item in set_rdsacctreqattr_list -%}
    SET RDSACCTREQATTR:
    {#- --- 必选参数 --- -#}
    RDSSVRGRPNAME="{{item.RDSSVRGRPNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.TRIGGERTYPE is not none -%}
        TRIGGERTYPE={{item.TRIGGERTYPE}},
    {%- endif -%}
    ;
{%- endfor -%}
```


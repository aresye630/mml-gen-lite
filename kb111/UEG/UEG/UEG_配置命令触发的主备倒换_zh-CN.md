---
id: ''
name: 配置命令触发的主备倒换
ne_type: UEG
type: feature
description: 通过命令主动触发主备倒换时，需参考本页面进行配置。  本页面中的命令均为高危命令，请在华为工程师指导下执行。否则可能导致业务受损。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝L","UEG容灾方案介绍（风筝L）","1+1主备容灾原理","1+1主备容灾部署与调测","1+1主备容灾模式","配置命令触发的主备倒换"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
通过命令主动触发主备倒换时，需参考本页面进行配置。本页面中的命令均为高危命令，请在华为工程师指导下执行。否则可能导致业务受损。

## 必备事项
前提条件

两套UEG已完成1+1主备容灾模式配置。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    swap_dr_list:
      type: items
      properties:
        DRGROUPID:
          name: '容灾组标识'
          type: integer
          minimum: 1
          maximum: 8
          required: true
          description: '引用**ADD DRGROUPINFO**定义的容灾组标识。可通过**LST DRGROUPINFO**命令查询。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        FORCE:
          name: '是否强制倒换'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: NO
  examples:
    swap_dr_list:
    - DRGROUPID: 1
      FORCE: NO
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 进入“MML命令行-UEG”窗口。

### 2 执行容灾实例主备倒换。

### 如下以DC1运行状态为主，DC2运行状态为备为例，在UEG1上下发主备倒换命令。

```jinja2
{%- for item in swap_dr_list -%}
    SWAP DR:
    {#- --- 必选参数 --- -#}
    DRGROUPID={{item.DRGROUPID}},
    {#- --- 可选参数 --- -#}
    {%- if item.FORCE is not none -%}
        FORCE={{item.FORCE}},
    {%- endif -%}
    ;
{%- endfor -%}
```


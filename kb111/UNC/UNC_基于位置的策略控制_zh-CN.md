---
id: ''
name: 基于位置的策略控制
ne_type: UNC
type: feature
description: 本章节介绍配置当不需要基于实时位置进行策略控制，只需要SMF感知到用户的位置发生变化时上报Npcf\_SMPolicyControl\_Update Request给PCF。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","智能PCC解决方案","基于实时位置的策略控制","基于位置的策略控制"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本章节介绍配置当不需要基于实时位置进行策略控制，只需要SMF感知到用户的位置发生变化时上报Npcf\_SMPolicyControl\_Update Request给PCF。

## 必备事项
前提条件

请仔细阅读基于实时位置的策略控制。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    set_n7rcvattrctrl_list:
      type: items
      properties:
        SCELLCHNR:
          name: 'SCELL\_CH是否允许上报NCGI'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '当PCF下发基于Cell粒度的位置Trigger时，需在SMF开启该功能。'
          data_source: '对端协商'
          pattern: ''
          default: ''
  examples:
    set_n7rcvattrctrl_list:
    - SCELLCHNR: ENABLE
```

## 3 命令模板定义
<!-- @mml:block=commands -->

#### 1.2 //在SMF上开启NCGI订阅和上报功能。

```jinja2
{%- for item in set_n7rcvattrctrl_list -%}
    SET N7RCVATTRCTRL:
    {#- --- 可选参数 --- -#}
    {%- if item.SCELLCHNR is not none -%}
        SCELLCHNR={{item.SCELLCHNR}},
    {%- endif -%}
    ;
{%- endfor -%}
```


---
id: ''
name: 激活eNB IP冲突检测
ne_type: UNC
type: feature
description: 本操作指导介绍部署eNB IP冲突检测特性的操作过程。  本特性支持eNodeB IP冲突检测，如果存在eNodeB IP冲突，会上报“**ALM-80716 eNodeB IP重复**”告警，运维人员可以快速定位eNodeB侧IP配置重复问题，避免业务受损。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","组网功能","WSFD-104417 eNB IP冲突检测","激活eNB IP冲突检测"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本操作指导介绍部署eNB IP冲突检测特性的操作过程。本特性支持eNodeB IP冲突检测，如果存在eNodeB IP冲突，会上报“**ALM-80716 eNodeB IP重复**”告警，运维人员可以快速定位eNodeB侧IP配置重复问题，避免业务受损。

## 必备事项
前提条件

前提条件

请仔细阅读WSFD-104417 eNB IP冲突检测特性概述。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    set_s1appara_list:
      type: items
      properties:
        ENBIPALMSW:
          name: 'eNodeB IP重复告警上报功能开关'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    set_s1appara_list:
    - ENBIPALMSW: YES
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 打开eNodeB IP重复告警上报功能开关。将“ENBIPALMSW”开关设置为“YES(是)”。

```jinja2
{%- for item in set_s1appara_list -%}
    SET S1APPARA:
    {#- --- 可选参数 --- -#}
    {%- if item.ENBIPALMSW is not none -%}
        ENBIPALMSW={{item.ENBIPALMSW}},
    {%- endif -%}
    ;
{%- endfor -%}
```


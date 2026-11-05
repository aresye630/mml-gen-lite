---
id: GWFD-021403
name: 修改DDoS Check是否使能
ne_type: UEG
type: feature
description: 需要修改DDoS Check是否使能。  适用于SGW-U、PGW-U、UPF。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝L","MEC 特性指南（风筝L）","GW-U&UPF特性指南","GWFD-021400 可靠性功能","GWFD-021403 防DDoS功能","调整DDoS Check数据","修改DDoS Check是否使能"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
需要修改DDoS Check是否使能。适用于SGW-U、PGW-U、UPF。

## 必备事项
前提条件

请仔细阅读GWFD-021403 防DDoS功能。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    mod_userprofile_list:
      type: items
      properties:
        USERPROFILENAME:
          name: '用户模板名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        DDOSCHECK:
          name: '防DDoS攻击标记'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
  examples:
    mod_userprofile_list:
    - USERPROFILENAME: 'up_test'
      DDOSCHECK: ENABLE
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 修改UserProfile的DDoS Check使能。

```jinja2
{%- for item in mod_userprofile_list -%}
    MOD USERPROFILE:
    {#- --- 必选参数 --- -#}
    USERPROFILENAME="{{item.USERPROFILENAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.DDOSCHECK is not none -%}
        DDOSCHECK={{item.DDOSCHECK}},
    {%- endif -%}
    ;
{%- endfor -%}
```


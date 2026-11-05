---
id: GWFD-024303
name: 配置AAA鉴权的3GPP扩展属性
ne_type: UEG
type: feature
description: 根据要求在UEG上配置AAA鉴权消息中携带的3GPP扩展属性。  适用于PGW-C、SMF
tags: []
risk_level: ''
doc_source: ["业务配置","风筝L","MEC 特性指南（风筝L）","GW-C&SMF特性指南","GWFD-024300 系统管理","GWFD-024303 Radius功能","调整AAA鉴权参数","配置AAA鉴权的3GPP扩展属性"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
根据要求在UEG上配置AAA鉴权消息中携带的3GPP扩展属性。适用于PGW-C、SMF

## 必备事项
前提条件

完成配置RADIUS功能。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    set_rdsauthreqvsa_list:
      type: items
      properties:
        RDSSVRGRPNAME:
          name: 'RADIUS服务器组名称'
          type: string
          minLength: 1
          maxLength: 31
          required: true
          description: '鉴权服务器所在的Radius服务器组，已通过**ADD RDSSVRGRP**进行配置。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        THREEGPP:
          name: '3GPP私有扩展属性开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '**SET RDSAUTHREQVSA**'
          data_source: '本端规划'
          pattern: ''
          default: ''
  examples:
    set_rdsauthreqvsa_list:
    - RDSSVRGRPNAME: 'ss'
      THREEGPP: ENABLE
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 进入“MML命令行-UEG”窗口。

### 2 配置AAA鉴权消息中携带的3GPP扩展属性。

#### 2.1 //配置AAA鉴权消息中携带的3GPP扩展属性。

```jinja2
{%- for item in set_rdsauthreqvsa_list -%}
    SET RDSAUTHREQVSA:
    {#- --- 必选参数 --- -#}
    RDSSVRGRPNAME="{{item.RDSSVRGRPNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.THREEGPP is not none -%}
        THREEGPP={{item.THREEGPP}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 缺省情况下不支持鉴权消息中携带3GPP（26/10415）这组属性。


---
id: ''
name: 配置在线计费自动回切功能
ne_type: UNC
type: feature
description: 在线计费用户因OCS故障等原因转离线后，在holding-time超时前，OCS故障恢复，用户可以自动恢复为在线计费用户。  GGSN/PGW-C支持在DCC template模板、DCC global模板下开启本功能，此处以前者为例说明功能激活过程。  适用于GGSN、PGW-C。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","计费管理功能","WSFD-109001 Gy/Diameter在线计费","激活Gy/Diameter在线计费","配置在线计费模板","配置在线计费自动回切功能"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
在线计费用户因OCS故障等原因转离线后，在holding-time超时前，OCS故障恢复，用户可以自动恢复为在线计费用户。GGSN/PGW-C支持在DCC template模板、DCC global模板下开启本功能，此处以前者为例说明功能激活过程。适用于GGSN、PGW-C。

## 必备事项
前提条件

* 请仔细阅读Ga/Gy接口离线/在线计费。
* 在线转离线功能已经通过配置DCC处理动作开启。

  在线计费回切功能要求转离线功能中：

  + **SET OCSDOWNACTION**:“OCSDNACTION”需配置为*permit。*
  + **ADD DCCTEMPLATE**:“CCFH”。
  + **ADD CMDRCACT**:“CMDRCACT”为*continue*。
* 完成**加载license**（如果有需求，请联系华为技术支持工程师处理）。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    add_dcctemplate_list:
      type: items
      properties:
        DCCTMPLTNAME:
          name: 'DCC模板名称'
          type: string
          maxLength: 63
          required: true
          description: '配置在线计费自动回切功能。 说明：  用户转离线时如果配置了**SET HOLDINGTIME**命令的HOLDINGTIME，则GGSN/PGW-C在*HOLDINGTIME*超时前一直按照**ADD DCCTEMPLATE**命令配置的RECOVERINTERVAL值定期尝试恢复在线计费；若未配置HOLDINGTIME，则视作该值无限大。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        ONLCHGRECOVER:
          name: '在线计费自动恢复功能开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          - INHERIT
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: INHERIT
        RECOVERINTERVAL:
          name: '在线计费自动恢复间隔 （分钟）'
          type: integer
          minimum: 1
          maximum: 60
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: 5
  examples:
    add_dcctemplate_list:
    - DCCTMPLTNAME: 'dcc-test'
      ONLCHGRECOVER: ENABLE
      RECOVERINTERVAL: 10
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 配置在线计费自动回切功能。

```jinja2
{%- for item in add_dcctemplate_list -%}
    ADD DCCTEMPLATE:
    {#- --- 必选参数 --- -#}
    DCCTMPLTNAME="{{item.DCCTMPLTNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.ONLCHGRECOVER is not none -%}
        ONLCHGRECOVER={{item.ONLCHGRECOVER}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：ONLCHGRECOVER=ENABLE 时可选 --- -#}
    {%- if item.ONLCHGRECOVER == 'ENABLE' -%}
        {%- if item.RECOVERINTERVAL is not none -%}
            RECOVERINTERVAL={{item.RECOVERINTERVAL}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```


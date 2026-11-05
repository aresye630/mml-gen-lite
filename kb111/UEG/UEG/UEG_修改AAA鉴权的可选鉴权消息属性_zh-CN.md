---
id: GWFD-024303
name: 修改AAA鉴权的可选鉴权消息属性
ne_type: UEG
type: feature
description: 根据要求在UEG 上修改AAA的可选鉴权消息属性。  适用于PGW-C、SMF
tags: []
risk_level: ''
doc_source: ["业务配置","风筝L","MEC 特性指南（风筝L）","GW-C&SMF特性指南","GWFD-024300 系统管理","GWFD-024303 Radius功能","调整AAA鉴权参数","修改AAA鉴权的可选鉴权消息属性"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
根据要求在UEG 上修改AAA的可选鉴权消息属性。适用于PGW-C、SMF

## 必备事项
前提条件

完成配置RADIUS功能。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    set_rdsauthreqattr_list:
      type: items
      properties:
        RDSSVRGRPNAME:
          name: 'RADIUS服务器组名称'
          type: string
          minLength: 1
          maxLength: 31
          required: true
          description: '**SET RDSAUTHREQVSA**'
          data_source: '本端规划'
          pattern: ''
          default: ''
        CHARGINGID:
          name: '3GPP-Charging-ID'
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
    set_rdsauthreqattr_list:
    - RDSSVRGRPNAME: 'ss'
      CHARGINGID: ENABLE
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 进入“MML命令行-UEG”窗口。

### 2 修改AAA鉴权消息中携带的3GPP扩展属性。

#### 2.1 //修改AAA鉴权消息中携带的3GPP扩展属性。

```jinja2
{%- for item in set_rdsauthreqattr_list -%}
    SET RDSAUTHREQATTR:
    {#- --- 必选参数 --- -#}
    RDSSVRGRPNAME="{{item.RDSSVRGRPNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.CHARGINGID is not none -%}
        CHARGINGID={{item.CHARGINGID}},
    {%- endif -%}
    ;
{%- endfor -%}
```


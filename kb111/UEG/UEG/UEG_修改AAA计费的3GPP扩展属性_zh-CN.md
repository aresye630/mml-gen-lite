---
id: GWFD-024303
name: 修改AAA计费的3GPP扩展属性
ne_type: UEG
type: feature
description: 当AAA Server的3GPP扩展属性发生变化时，UEG需要修改AAA计费的3GPP扩展属性以便和AAA Server保持一致。  适用于PGW-C、SMF
tags: []
risk_level: ''
doc_source: ["业务配置","风筝L","MEC 特性指南（风筝L）","GW-C&SMF特性指南","GWFD-024300 系统管理","GWFD-024303 Radius功能","调整AAA计费参数","修改AAA计费的3GPP扩展属性"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
当AAA Server的3GPP扩展属性发生变化时，UEG需要修改AAA计费的3GPP扩展属性以便和AAA Server保持一致。适用于PGW-C、SMF

## 必备事项
前提条件

完成配置RADIUS功能。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    set_rdsacctreqvsa_list:
      type: items
      properties:
        RDSSVRGRPNAME:
          name: 'RADIUS Server Group名称'
          type: string
          maxLength: 31
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        THREEGPP:
          name: '支持3gpp私有扩展属性'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: true
          description: '**SET RDSACCTREQVSA**'
          data_source: '与对端协商'
          pattern: ''
          default: ''
        THREEGPP2:
          name: '支持3gpp2私有扩展属性'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    set_rdsacctreqvsa_list:
    - RDSSVRGRPNAME: 'ss'
      THREEGPP: ENABLE
      THREEGPP2: DISABLE
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 进入“MML命令行-UEG”窗口。

### 2 修改AAA计费的3GPP扩展属性。

#### 2.1 //修改AAA计费的3GPP扩展属性。

```jinja2
{%- for item in set_rdsacctreqvsa_list -%}
    SET RDSACCTREQVSA:
    {#- --- 必选参数 --- -#}
    RDSSVRGRPNAME="{{item.RDSSVRGRPNAME}}",
    THREEGPP={{item.THREEGPP}},
    THREEGPP2={{item.THREEGPP2}},
    ;
{%- endfor -%}
```


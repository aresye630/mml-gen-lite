---
id: GWFD-023801
name: 激活端到端用户跟踪（4G）
ne_type: UEG
type: feature
description: 本操作指导介绍在运行网络中激活端到端用户跟踪的操作过程。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝L","MEC 特性指南（风筝L）","UEG公共特性指南","网络OM增强","GWFD-023801 端到端用户跟踪","激活端到端用户跟踪(MME/SGW-C/PGW-C/AMF/SMF)","激活端到端用户跟踪（4G）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
本操作指导介绍在运行网络中激活端到端用户跟踪的操作过程。

## 必备事项
前提条件

完成加载License。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    set_licenseswitch_list:
      type: items
      properties:
        LICITEM:
          name: 'License项'
          type: string
          minLength: 0
          maxLength: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SWITCH:
          name: '开关'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV2ESTAM01'
      SWITCH: ENABLE
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 打开本功能的License配置开关。

### 在“MML命令行-UEG”窗口上执行：

#### 1.1 //打开端到端用户跟踪的License配置开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```


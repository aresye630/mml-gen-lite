---
id: GWFD-020252
name: 激活SRVCC
ne_type: UDG
type: feature
description: 在UDG上开启特性的License开关激活SRVCC功能。  适用于SGW-U、PGW-U。
risk_level: ''
doc_source: ["特性部署","特性指南","UDG特性指南","语音功能","GWFD-020252 SRVCC","激活SRVCC"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
在UDG上开启特性的License开关激活SRVCC功能。适用于SGW-U、PGW-U。

## 必备事项
前提条件

* 请仔细阅读GWFD-020252 SRVCC。
* 完成配置VoLTE基础语音业务。
* 完成**加载license**（如果有需求，请联系华为技术支持工程师处理）。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
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
    - LICITEM: 'LKV3G5RVCC01'
      SWITCH: ENABLE
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 打开本特性的License配置开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```


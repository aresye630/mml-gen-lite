---
id: ''
name: 激活第三方应用智能运维
ne_type: UDG
type: feature
description: 运营商为运维人员提供第三方app智能运维系统时，需要先对第三方app智能运维功能进行激活。
risk_level: ''
doc_source: ["特性部署","业务专题","UDG SFIP功能专题","功能描述","第三方应用智能运维","激活第三方应用智能运维"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
运营商为运维人员提供第三方app智能运维系统时，需要先对第三方app智能运维功能进行激活。

## 必备事项
前提条件

请仔细阅读第三方应用智能运维。
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
    - LICITEM: 'LKV4SSTAPP02'
      SWITCH: ENABLE
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 在“MML命令行 - UDG”窗口上执行**SET LICENSESWITCH**打开license开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```


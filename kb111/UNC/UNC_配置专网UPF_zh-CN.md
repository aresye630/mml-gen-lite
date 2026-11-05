---
id: ''
name: 配置专网UPF
ne_type: UNC
type: feature
description: 该任务旨在指导操作人员完成一跳入家相关业务配置。  一跳入家业务专网UPF上无需额外配置，只需打开对应License。
risk_level: ''
doc_source: ["网络部署","业务专题","5G Core 一跳入家解决方案","一跳入家解决方案（基于3GPP接入方案）","业务初始部署与调测","部署一跳入家","配置专网UPF"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
该任务旨在指导操作人员完成一跳入家相关业务配置。一跳入家业务专网UPF上无需额外配置，只需打开对应License。

## 必备事项
前提条件

* 已完成**智网接入**的License加载。
* 已经完成专网UPF的基础配置。
* 已完成一跳入家要求的移动VPN相关配置。
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
          description: '打开智网接入的License。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SWITCH:
          name: '开关'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: true
          description: '-'
          data_source: '固定配置'
          pattern: ''
          default: ''
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV3G5SNAC01'
      SWITCH: ENABLE
```

## 3 命令模板定义
<!-- @mml:block=commands -->

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```


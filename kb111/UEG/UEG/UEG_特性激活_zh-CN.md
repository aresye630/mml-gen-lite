---
id: GWFD-030204
name: 特性激活
ne_type: UEG
type: feature
description: 在UEG上部署4G/NSA UL CL分流功能，需要配置本地分流功能并开启特性License配置。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝S","MEC 特性指南（风筝S）","UEG特性指南","本地分流功能","GWFD-030204 4G/NSA UL CL分流","特性激活"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
在UEG上部署4G/NSA UL CL分流功能，需要配置本地分流功能并开启特性License配置。

## 必备事项
前提条件

* 请仔细阅读GWFD-030204 4G/NSA UL CL分流。
* UEG完成与周边网元的对接。
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
    - LICITEM: ''
      SWITCH: ''
```

## 3 命令模板定义
<!-- @mml:block= commands -->

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

### 2 分流策略在SMF上决策，UPF、PGW根据SMF下发的分流规则执行分流功能。分流策略在SMF上配置，具体可参见UNC产品文档中的“WSFD-108002 本地分流策略控制”。在UPF、PGW上仅需要打开本特性的License开关，并在主锚点完成本地分流功能配置。本地分流功能配置请参见GWFD-023601 基于域名的本地分流、GWFD-023602 基于IP地址的本地分流。


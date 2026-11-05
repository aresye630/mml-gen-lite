---
id: ''
name: 激活RedCap终端标准接入（UPF）
ne_type: UEG
type: feature
description: 本操作用于指导网元激活RedCap终端标准接入（UPF）功能的操作过程。  适用于UPF。
tags: []
risk_level: ''
doc_source: ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（电力专网，入驻式）","配置基础业务","5G Redcap功能配置","激活RedCap终端标准接入（UPF）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
本操作用于指导网元激活RedCap终端标准接入（UPF）功能的操作过程。适用于UPF。

## 必备事项
前提条件

* 请仔细阅读WSFD-010110 支持RedCap接入特性概述及实现原理。
* 完成加载License（如果有需求，请联系华为技术支持工程师处理）。
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
          description: '打开本特性的License配置开关。'
          data_source: '固定取值'
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
          data_source: '固定取值'
          pattern: ''
          default: ''
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV3G5RED001'
      SWITCH: ENABLE
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 打开本特性的License配置开关：

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```


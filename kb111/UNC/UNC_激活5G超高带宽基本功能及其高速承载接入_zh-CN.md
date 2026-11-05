---
id: ''
name: 激活5G超高带宽基本功能及其高速承载接入
ne_type: UNC
type: feature
description: 本操作指导介绍在运行网络中激活5G超高带宽基本功能及其高速承载接入的操作过程。  适用于MME、SGW-C、PGW-C、AMF、SMF。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","高速数据连接功能","WSFD-210000 5G超高带宽基本功能","5G超高带宽基本功能及其高速承载接入","激活5G超高带宽基本功能及其高速承载接入"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本操作指导介绍在运行网络中激活5G超高带宽基本功能及其高速承载接入的操作过程。适用于MME、SGW-C、PGW-C、AMF、SMF。

## 必备事项
前提条件

* 请仔细阅读5G超高带宽基本功能及其高速承载接入。
* 完成加载License。
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
    - LICITEM: 'LKV2UNCBASE01'
      SWITCH: ENABLE
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 进入“MML命令行-UNC”窗口。

### 2 重复执行如下命令，依次打开5G超高带宽基本功能（1Gbps）、5G超高带宽高速承载接入（1Gbps）、5G超高带宽基本功能（2Gbps）、5G超高带宽高速承载接入（2Gbps）、5G超高带宽基本功能（5Gbps）、5G超高带宽高速承载接入（5Gbps）、5G超高带宽基本功能（10Gbps）、5G超高带宽高速承载接入（10Gbps）、5G超高带宽基本功能（20Gbps）和5G超高带宽高速承载接入（20Gbps）的License配置开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```


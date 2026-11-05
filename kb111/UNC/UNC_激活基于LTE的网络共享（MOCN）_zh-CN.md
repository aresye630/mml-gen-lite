---
id: ''
name: 激活基于LTE的网络共享（MOCN）
ne_type: UNC
type: feature
description: 本操作指导介绍在运行网络中激活基于LTE的网络共享（MOCN）特性的操作过程。  适用于MME。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","网络共享功能","WSFD-207003 基于LTE的网络共享（MOCN）","激活基于LTE的网络共享（MOCN）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本操作指导介绍在运行网络中激活基于LTE的网络共享（MOCN）特性的操作过程。适用于MME。

## 必备事项
前提条件

* 请仔细阅读WSFD-207003 基于LTE的网络共享（MOCN）特性概述。
* 到eNodeB的基本数据已经配置完成，配置方法见配置到eNodeB的数据。
* 已完成加载License。

SGW-C/PGW-C/SMF选择SGW-U/PGW-U/UPF时涉及基于用户位置区信息选择，请提前确认SGW-C/PGW-C/SMF上支持的位置区信息，避免开启网络共享（MOCN）功能，运营商改造配置后选择的SGW-U/PGW-U/UPF不符合组网规划。
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
    - LICITEM: 'LKV2MOCN03'
      SWITCH: ENABLE
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 进入“MML命令行-UNC”窗口。

### 2 打开基于LTE的网络共享（MOCN）功能开关。

#### 2.1 //开启MOCN功能。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```


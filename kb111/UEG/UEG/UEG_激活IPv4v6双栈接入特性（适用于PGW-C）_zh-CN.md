---
id: GWFD-022903
name: 激活IPv4v6双栈接入特性（适用于PGW-C）
ne_type: UEG
type: feature
description: 本操作指导介绍在运行网络中激活IPv4v6双栈接入特性的操作过程。  适用于PGW-C。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝L","MEC 特性指南（风筝L）","GW-C&SMF特性指南","GWFD-022900 IPV6基本功能","GWFD-022903 IPv4v6双栈接入","IPv4v6双栈接入（2G/3G/4G）","激活IPv4v6双栈接入特性（适用于PGW-C）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
本操作指导介绍在运行网络中激活IPv4v6双栈接入特性的操作过程。适用于PGW-C。

## 必备事项
前提条件

* 请仔细阅读GWFD-022903 IPv4v6双栈接入特性概述（适用于2G/3G/4G）。

* 完成加载License。
* 支持IPv4v6的用户已经接入到网络。
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
    - LICITEM: 'LKV2IPDSSM01'
      SWITCH: ENABLE
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 进入“MML命令行-UEG”窗口。

### 2 打开IPv6承载上下文特性的License配置开关。

#### 2.1 //打开本特性的License配置开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```


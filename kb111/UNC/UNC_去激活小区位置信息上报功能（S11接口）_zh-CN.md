---
id: ''
name: 去激活小区位置信息上报功能（S11接口）
ne_type: UNC
type: feature
description: 本操作指导介绍在运行网络中去激活小区位置信息上报功能的操作过程。  适用于MME
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","智能PCC解决方案","基于实时位置的策略控制","相关特性","WSFD-106403 小区位置信息上报功能（S11接口）","去激活小区位置信息上报功能（S11接口）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本操作指导介绍在运行网络中去激活小区位置信息上报功能的操作过程。适用于MME

## 必备事项
前提条件

* 操作人员已经登录U2020/MAE。
* 小区位置信息上报功能已经激活。
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
    mod_locrptcfg_list:
      type: items
      properties:
        RANGE:
          name: '对端设备范围'
          type: string
          enum:
          - ALL_GGSN/P-GW
          - FOREIGN_GGSN/P-GW
          - HOME_GGSN/P-GW
          - SPECIFIC_GGSN/P-GW
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LOCRPT:
          name: '支持位置上报功能'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPT:
          name: 'IP地址类型'
          type: string
          enum:
          - IPV4
          - IPV6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GWIPV4:
          name: 'GGSN/P-GW的信令面IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MASKV4:
          name: '掩码'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GWIPV6:
          name: 'GGSN/P-GW的信令面IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MASKV6:
          name: '子网前缀长度'
          type: integer
          minimum: 1
          maximum: 128
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    set_licenseswitch_list:
    - LICITEM: '"LKV2LCR01"，SWITCH=DISABLE；'
      SWITCH: DISABLE
    mod_locrptcfg_list:
    - RANGE: 对端设备范围，IPT=IP地址类型，GWIPV4=GGSN/P-GW的信令面地址，MASKV4=掩码
      LOCRPT: 支持位置上报功能；
      IPT: IP地址类型
      GWIPV4: 'GGSN/P-GW的信令面地址'
      MASKV4: '掩码'
      GWIPV6: ''
      MASKV6: ''
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 关闭本特性的License配置开关。

### 在“MML命令行-UNC”窗口上执行：

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

### 2 配置特定的GGSN/P-GW不允许使用该功能。

### 在“MML命令行-UNC”窗口上执行：

```jinja2
{%- for item in mod_locrptcfg_list -%}
    MOD LOCRPTCFG:
    {#- --- 必选参数 --- -#}
    RANGE={{item.RANGE}},
    {#- --- 可选参数 --- -#}
    {%- if item.LOCRPT is not none -%}
        LOCRPT={{item.LOCRPT}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：RANGE=SPECIFIC_GGSN/P-GW 时必选 --- -#}
    {%- if item.RANGE == 'SPECIFIC_GGSN/P-GW' -%}
        IPT={{item.IPT}},
    {%- endif -%}
    {#- --- 条件必选：IPT=IPV4 时必选 --- -#}
    {%- if item.IPT == 'IPV4' -%}
        GWIPV4="{{item.GWIPV4}}",
    {%- endif -%}
    {#- --- 条件必选：IPT=IPV4 时必选 --- -#}
    {%- if item.IPT == 'IPV4' -%}
        MASKV4="{{item.MASKV4}}",
    {%- endif -%}
    {#- --- 条件必选：IPT=IPV6 时必选 --- -#}
    {%- if item.IPT == 'IPV6' -%}
        GWIPV6="{{item.GWIPV6}}",
    {%- endif -%}
    {#- --- 条件必选：IPT=IPV6 时必选 --- -#}
    {%- if item.IPT == 'IPV6' -%}
        MASKV6={{item.MASKV6}},
    {%- endif -%}
    ;
{%- endfor -%}
```


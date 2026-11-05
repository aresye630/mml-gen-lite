---
id: ''
name: 激活小区位置信息上报功能（S11接口）
ne_type: UNC
type: feature
description: 本操作指导介绍在运行网络中激活小区位置信息上报功能的操作过程。  小区位置信息上报功能是指MME基于S-GW/P-GW下发的策略向RAN侧发起位置订阅，当用户的ECGI发生变化时，MME将最新的用户位置信息上报给S-GW/P-GW，并经S-GW/P-GW上报给PCRF。PCRF可综合用户位置、使用流量、网络状态等进行策略决策并发起策略更新。  适用于MME
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","智能PCC解决方案","基于实时位置的策略控制","相关特性","WSFD-106403 小区位置信息上报功能（S11接口）","激活小区位置信息上报功能（S11接口）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本操作指导介绍在运行网络中激活小区位置信息上报功能的操作过程。小区位置信息上报功能是指MME基于S-GW/P-GW下发的策略向RAN侧发起位置订阅，当用户的ECGI发生变化时，MME将最新的用户位置信息上报给S-GW/P-GW，并经S-GW/P-GW上报给PCRF。PCRF可综合用户位置、使用流量、网络状态等进行策略决策并发起策略更新。适用于MME

## 必备事项
前提条件

* 操作人员已经登录U2020/MAE
* 需要对端网元P-GW、PCRF激活小区位置信息上报功能。
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
    add_locrptcfg_list:
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
          default: IPV4
        GWIPV4:
          name: 'GGSN/P-GW的信令面IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
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
          default: NO
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
    set_mmfunc_list:
      type: items
      properties:
        LOCRPTTIMER:
          name: '实时位置上报最小间隔'
          type: integer
          minimum: 0
          maximum: 3600
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    set_licenseswitch_list:
    - LICITEM: '"LKV2LCR01"，SWITCH=ENABLE；'
      SWITCH: ENABLE
    add_locrptcfg_list:
    - RANGE: 对端设备范围，IPT=IP地址类型，GWIPV4=GGSN/P-GW的信令面地址，MASKV4=掩码，LOCRPT=支持位置上报功能；
      IPT: IP地址类型
      GWIPV4: '10.0.0.1'
      MASKV4: '掩码'
      LOCRPT: 支持位置上报功能
      GWIPV6: ''
      MASKV6: ''
    set_mmfunc_list:
    - LOCRPTTIMER: 实时位置上报最小间隔。
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 打开本特性的License配置开关。

### 在“MML命令行-UNC”：

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

### 2 配置特定的GGSN/P-GW允许使用该功能。

### 在“MML命令行-UNC”窗口上执行：

```jinja2
{%- for item in add_locrptcfg_list -%}
    ADD LOCRPTCFG:
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

### 3 **可选：**设置实时位置上报最小间隔。

### 在“MML命令行-UNC”窗口上执行：

```jinja2
{%- if is_optional_set_realtime_location_report_interval -%}
    {%- for item in set_mmfunc_list -%}
        SET MMFUNC:
        {#- --- 可选参数 --- -#}
        {%- if item.LOCRPTTIMER is not none -%}
            LOCRPTTIMER={{item.LOCRPTTIMER}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```


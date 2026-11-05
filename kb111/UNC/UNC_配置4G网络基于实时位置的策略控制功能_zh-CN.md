---
id: ''
name: 配置4G网络基于实时位置的策略控制功能
ne_type: UNC
type: feature
description: 本章节介绍4G用户接入4G网络场景，或者5G用户接入4G网络并通过N7接口连接PCF场景，如何开启基于实时位置的策略控制功能。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","智能PCC解决方案","基于实时位置的策略控制","4G网络基于实时位置的策略控制","配置4G网络基于实时位置的策略控制功能"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本章节介绍4G用户接入4G网络场景，或者5G用户接入4G网络并通过N7接口连接PCF场景，如何开启基于实时位置的策略控制功能。

## 必备事项
前提条件

前提条件

* 完成加载License。

* 部署本特性会增加相关接口的负荷，在部署本特性之前，需要对现有网络的业务模型、资费策略、网络资源占用情况进行评估，以降低对整个网络的负荷冲击。
* 需要对端网元PCRF/PCF激活基于实时位置信息的策略控制功能。
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
          description: '-'
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
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_licenseswitch_list_1:
      type: items
      properties:
        LICITEM:
          name: 'License项'
          type: string
          minLength: 0
          maxLength: 255
          required: true
          description: '-'
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
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_smcommfunc_list:
      type: items
      properties:
        LOCREPORT:
          name: '位置上报'
          type: string
          enum:
          - NotSupport
          - Support
          required: false
          description: '开启全局位置上报功能。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_apn_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '开启指定APN位置上报功能。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        LOCREPORT:
          name: '位置上报'
          type: string
          enum:
          - INHERIT
          - ENABLE
          - DISABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: INHERIT
    set_policymode_list:
      type: items
      properties:
        TMACCTYPE:
          name: '指定终端和接入类型'
          type: string
          enum:
          - UE5G_RAT4G
          - UENON5G_RAT4G
          - RAT2G
          - RATNBIOT
          - NON_3GPP
          - RATLTEM
          - RAT3G
          required: true
          description: '可选，5G用户接入4G网络且通过N7接口连接PCF场景，需要在PGW-C侧配置策略接口为Npcf接口。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        BY5GSIWKI:
          name: '按5GS互操作指示选择策略接口开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        FORCED:
          name: '指定策略接口'
          type: string
          enum:
          - Npcf
          - Gx
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        BY5GCNRI:
          name: '按5GC无限制接入标识选择策略接口开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        BYIWKUEN5GR4G:
          name: '非5G终端4G接入按5GS互操作指示选择策略接口开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV2LCR01'
      SWITCH: ENABLE
    set_licenseswitch_list_1:
    - LICITEM: 'LKV2PYCTRL1'
      SWITCH: ENABLE
    set_smcommfunc_list:
    - LOCREPORT: Support
    add_apn_list:
    - APN: 'huawei.com'
      LOCREPORT: INHERIT
    set_policymode_list:
    - TMACCTYPE: UE5G_RAT4G
      BY5GSIWKI: DISABLE
      FORCED: Npcf
      BY5GCNRI: ''
      BYIWKUEN5GR4G: ''
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 //开启MME小区位置信息上报功能的license。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

### 2 //开启SGW/PGW-C基于实时位置的策略控制功能的license。

```jinja2
{%- for item in set_licenseswitch_list_1 -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

### 3 //开启全局位置上报功能。

```jinja2
{%- for item in set_smcommfunc_list -%}
    SET SMCOMMFUNC:
    {#- --- 可选参数 --- -#}
    {%- if item.LOCREPORT is not none -%}
        LOCREPORT={{item.LOCREPORT}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 //设置APN（huawei.com）的位置上报功能，指定该APN的位置上报功能继承全局配置。

```jinja2
{%- for item in add_apn_list -%}
    ADD APN:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    {#- --- 可选参数 --- -#}
    {%- if item.LOCREPORT is not none -%}
        LOCREPORT={{item.LOCREPORT}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 5 //设置策略接口为Npcf。

```jinja2
{%- for item in set_policymode_list -%}
    SET POLICYMODE:
    {#- --- 必选参数 --- -#}
    TMACCTYPE={{item.TMACCTYPE}},
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：TMACCTYPE=UE5G_RAT4G/RATNBIOT 时可选 --- -#}
    {%- if item.TMACCTYPE in ['UE5G_RAT4G', 'RATNBIOT'] -%}
        {%- if item.BY5GSIWKI is not none -%}
            BY5GSIWKI={{item.BY5GSIWKI}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：TMACCTYPE=UENON5G_RAT4G/UE5G_RAT4G 时可选 --- -#}
    {%- if item.TMACCTYPE in ['UENON5G_RAT4G', 'UE5G_RAT4G'] -%}
        {%- if item.BY5GCNRI is not none -%}
            BY5GCNRI={{item.BY5GCNRI}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：TMACCTYPE=UENON5G_RAT4G 时可选 --- -#}
    {%- if item.TMACCTYPE == 'UENON5G_RAT4G' -%}
        {%- if item.BYIWKUEN5GR4G is not none -%}
            BYIWKUEN5GR4G={{item.BYIWKUEN5GR4G}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件必选/可选参数 --- -#}
    {#- --- 指定策略接口: 条件必选(指定终端和接入类型=RAT2G|NON_3GPP|RATLTEM|RAT3G) / 条件可选(指定终端和接入类型=UENON5G_RAT4G|UE5G_RAT4G|RATNBIOT) --- -#}
    {%- if (item.TMACCTYPE in ['RAT2G', 'NON_3GPP', 'RATLTEM', 'RAT3G']) -%}
        FORCED={{item.FORCED}},
    {%- elif (item.TMACCTYPE in ['UENON5G_RAT4G', 'UE5G_RAT4G', 'RATNBIOT']) -%}
        {%- if item.FORCED is not none -%}
            FORCED={{item.FORCED}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```


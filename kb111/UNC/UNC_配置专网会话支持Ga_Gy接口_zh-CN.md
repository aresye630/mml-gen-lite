---
id: ''
name: 配置专网会话支持Ga/Gy接口
ne_type: UNC
type: feature
description: 本章节用于指导配置在用户4G/5G NSA接入时，专网SMF基于Ga/Gy接口选择计费网元CG/OCS并完成对用户流量的计费。  根据用户接入网络类型的不同（4G/5G NSA/5G SA），用户的公网会话可以是4G会话，也可以是5G会话，但是在创建用户专网会话时，智能分流PGW-C会将默认将4G信息转换为5G信息，再触发专网会话的建立，因此用户专网会话默认都是5G会话。这种情况下，当运营商的计费网络未改造，仅支持Ga/Gy的组网方式，不支持基于5G SA的N40组网时，需要专网SMF能够基于Gy/Ga接口传递4G计费的关键信息给OCS或CG，如携带4G格式的位置信息/QoS信息/用户接入网元类型等。
risk_level: ''
doc_source: ["网络部署","业务专题","5G Core 一跳入家解决方案","一跳入家解决方案（基于3GPP接入方案）","业务初始部署与调测","部署移动VPN","配置专用DNN数据","配置SMF","配置专网会话支持Ga/Gy接口"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本章节用于指导配置在用户4G/5G NSA接入时，专网SMF基于Ga/Gy接口选择计费网元CG/OCS并完成对用户流量的计费。根据用户接入网络类型的不同（4G/5G NSA/5G SA），用户的公网会话可以是4G会话，也可以是5G会话，但是在创建用户专网会话时，智能分流PGW-C会将默认将4G信息转换为5G信息，再触发专网会话的建立，因此用户专网会话默认都是5G会话。这种情况下，当运营商的计费网络未改造，仅支持Ga/Gy的组网方式，不支持基于5G SA的N40组网时，需要专网SMF能够基于Gy/Ga接口传递4G计费的关键信息给OCS或CG，如携带4G格式的位置信息/QoS信息/用户接入网元类型等。

## 必备事项
前提条件

* 已完成专网SMF基于Ga/Gy接口和CG/OCS的对接配置。
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
    add_apnchgmode_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '对应园区专用DNN。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        TMACCTYPE:
          name: '指定终端和接入类型'
          type: string
          enum:
          - UE5G_RAT4G
          - UE5G_RAT5G
          - UENON5G_RAT4G
          - RAT2G
          - RATNBIOT
          - NON_3GPP
          - RATLTEM
          - RAT3G
          required: true
          description: '**该参数指示用户类型和其接入方式的对应关系，专网会话为5G会话，因此该参数取值UE5G\_RAT5G。**'
          data_source: '本端规划'
          pattern: ''
          default: ''
        FORCED:
          name: '指定的计费接口'
          type: string
          enum:
          - GaGyMode
          - NchfMode
          - INVALID
          required: false
          description: '该参数表示在参数“TMACCTYPE”指示的组合方式下，专网SMF选择什么样接口类型的计费网元，如选择Ga/Gy接口类型的计费网元。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        BY5GCNRI:
          name: '按5GC无限制接入标识选择计费接口'
          type: string
          enum:
          - False
          - True
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: False
        BY5GSIWKI:
          name: '按5GS互操作指示选择计费接口'
          type: string
          enum:
          - False
          - True
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: False
        FORSGWONLY:
          name: '作为SGW计费模式'
          type: string
          enum:
          - GaGyMode
          - NchfMode
          - Inherit
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        FORVSMFONLY:
          name: '作为V-SMF计费模式'
          type: string
          enum:
          - GaGyMode
          - NchfMode
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ISMFCHGSW:
          name: 'I-SMF是否支持计费'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_apnga5greuseavp_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '对应园区专用DNN。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        RAT:
          name: '无线接入技术'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '该参数取值为ENABLE时，专网SMF会携带用户真实的RAT信息给计费网元。'
          data_source: '本端规划'
          pattern: ''
          default: ENABLE
        ULI:
          name: '用户位置信息'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '该参数取值为ENABLE时，专网SMF会携带用户真实的位置信息给计费网元。'
          data_source: '本端规划'
          pattern: ''
          default: ENABLE
        SERVINGNODETYPE:
          name: '服务节点类型'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '该参数取值为ENABLE时，专网SMF会携带用户真实的接入网元信息（如MME）给计费网元。'
          data_source: '本端规划'
          pattern: ''
          default: ENABLE
    add_apngy5greuseavp_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '对应园区专用DNN。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        RAT:
          name: '无线接入技术'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '该参数取值为ENABLE时，专网SMF会携带用户真实的RAT信息给计费网元。'
          data_source: '本端规划'
          pattern: ''
          default: ENABLE
        ULI:
          name: '用户位置信息'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '该参数取值为ENABLE时，专网SMF会携带用户真实的位置信息给计费网元。'
          data_source: '本端规划'
          pattern: ''
          default: ENABLE
        SERVINGNODETYPE:
          name: '服务节点类型'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '该参数取值为ENABLE时，专网SMF会携带用户真实的接入网元信息（如MME）给计费网元。'
          data_source: '本端规划'
          pattern: ''
          default: ENABLE
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV3EGAGY5G01'
      SWITCH: ENABLE
    add_apnchgmode_list:
    - APN: 'stjwt.gd'
      TMACCTYPE: UE5G_RAT5G
      FORCED: GaGyMode
      BY5GCNRI: False
      BY5GSIWKI: False
      FORSGWONLY: ''
      FORVSMFONLY: ''
      ISMFCHGSW: ''
    add_apnga5greuseavp_list:
    - APN: 'stjwt.gd'
      RAT: ENABLE
      ULI: ENABLE
      SERVINGNODETYPE: ENABLE
    add_apngy5greuseavp_list:
    - APN: 'stjwt.gd'
      RAT: ENABLE
      ULI: ENABLE
      SERVINGNODETYPE: ENABLE
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 激活5G SA计费的增强型GaGy接口的License。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

### 2 配置基于园区APN的计费接口选择方式。

```jinja2
{%- for item in add_apnchgmode_list -%}
    ADD APNCHGMODE:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    TMACCTYPE={{item.TMACCTYPE}},
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：TMACCTYPE=UENON5G_RAT4G/UE5G_RAT4G 时可选 --- -#}
    {%- if item.TMACCTYPE in ['UENON5G_RAT4G', 'UE5G_RAT4G'] -%}
        {%- if item.BY5GCNRI is not none -%}
            BY5GCNRI={{item.BY5GCNRI}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：TMACCTYPE=UENON5G_RAT4G/UE5G_RAT4G 时可选 --- -#}
    {%- if item.TMACCTYPE in ['UENON5G_RAT4G', 'UE5G_RAT4G'] -%}
        {%- if item.BY5GSIWKI is not none -%}
            BY5GSIWKI={{item.BY5GSIWKI}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：TMACCTYPE=UENON5G_RAT4G/UE5G_RAT4G 时可选 --- -#}
    {%- if item.TMACCTYPE in ['UENON5G_RAT4G', 'UE5G_RAT4G'] -%}
        {%- if item.FORSGWONLY is not none -%}
            FORSGWONLY={{item.FORSGWONLY}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：TMACCTYPE=UE5G_RAT5G 时可选 --- -#}
    {%- if item.TMACCTYPE == 'UE5G_RAT5G' -%}
        {%- if item.FORVSMFONLY is not none -%}
            FORVSMFONLY={{item.FORVSMFONLY}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：TMACCTYPE=UE5G_RAT5G 时可选 --- -#}
    {%- if item.TMACCTYPE == 'UE5G_RAT5G' -%}
        {%- if item.ISMFCHGSW is not none -%}
            ISMFCHGSW={{item.ISMFCHGSW}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件必选/可选参数 --- -#}
    {#- --- 指定的计费接口: 条件必选(指定终端和接入类型=RAT2G|RATNBIOT|NON_3GPP|RATLTEM|RAT3G) / 条件可选(指定终端和接入类型=UE5G_RAT5G|UENON5G_RAT4G|UE5G_RAT4G) --- -#}
    {%- if (item.TMACCTYPE in ['RAT2G', 'RATNBIOT', 'NON_3GPP', 'RATLTEM', 'RAT3G']) -%}
        FORCED={{item.FORCED}},
    {%- elif (item.TMACCTYPE in ['UE5G_RAT5G', 'UENON5G_RAT4G', 'UE5G_RAT4G']) -%}
        {%- if item.FORCED is not none -%}
            FORCED={{item.FORCED}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 配置Ga接口组网方式下专网SMF给CG携带计费信息类型。

```jinja2
{%- for item in add_apnga5greuseavp_list -%}
    ADD APNGA5GREUSEAVP:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    {#- --- 可选参数 --- -#}
    {%- if item.RAT is not none -%}
        RAT={{item.RAT}},
    {%- endif -%}
    {%- if item.ULI is not none -%}
        ULI={{item.ULI}},
    {%- endif -%}
    {%- if item.SERVINGNODETYPE is not none -%}
        SERVINGNODETYPE={{item.SERVINGNODETYPE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 配置Gy接口组网方式下专网SMF给OCS携带计费信息类型。

```jinja2
{%- for item in add_apngy5greuseavp_list -%}
    ADD APNGY5GREUSEAVP:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    {#- --- 可选参数 --- -#}
    {%- if item.RAT is not none -%}
        RAT={{item.RAT}},
    {%- endif -%}
    {%- if item.ULI is not none -%}
        ULI={{item.ULI}},
    {%- endif -%}
    {%- if item.SERVINGNODETYPE is not none -%}
        SERVINGNODETYPE={{item.SERVINGNODETYPE}},
    {%- endif -%}
    ;
{%- endfor -%}
```


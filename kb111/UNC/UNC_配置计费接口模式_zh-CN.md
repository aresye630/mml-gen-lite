---
id: ''
name: 配置计费接口模式
ne_type: UNC
type: feature
description: 本指导描述终端在接入网络时计费接口使用Nchf接口的配置过程。  UNC支持配置在不同类型终端接入不同网络时选择计费接口，计费接口选择有三种方式，优先级从高到低为：基于用户漫游属性选择计费接口 （对应命令为**ADD ROAMCHGMODE**）> 基于APN/DNN选择计费接口 （对应命令为**ADD APNCHGMODE**）> 全局配置计费接口（对应命令为**SET CHGMODE**）。  图1绘制了不同类型终端接入不同网络时计费接口选择。  **图1** 不同类型终端接入不同网络时计费接口选择逻辑图  SGW-C独立部署的场景下，需要SGW-C发起计费会话。在这种场景下，通过设置SGW-C上**ADD ROAMCHGMODE**/**ADD APNCHGMODE**/**SET CHGMODE**命令中**FORSGWONLY**的值可以手动指定计费接口。  UNC支持配置在不同类型终端接入不同网络时选择策略接口，策略接口选择有两种方式，优先级从高到低为：基于APN/DNN选择策略接口 > 全局配置策略接口。  图2绘制了不同类型终端接入不同网络时策略接口选择。  **图2** 不同类型终端接入不同网络时策略接口选择逻辑图  当UNC通过上述方式配置了计费接口和策略接口后，可通过**ADD PCCCHGMODEBYPCFID**命令基于PCF instance ID配置用户最终使用的策略接口类型和计费接口类型。
risk_level: ''
doc_source: ["网络部署","业务专题","5G Core 计费解决方案","计费解决方案概述","计费方案部署与调测","方案一：未部署NCG的计费解决方案","SMF配置","配置计费接口模式"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本指导描述终端在接入网络时计费接口使用Nchf接口的配置过程。UNC支持配置在不同类型终端接入不同网络时选择计费接口，计费接口选择有三种方式，优先级从高到低为：基于用户漫游属性选择计费接口 （对应命令为**ADD ROAMCHGMODE**）> 基于APN/DNN选择计费接口 （对应命令为**ADD APNCHGMODE**）> 全局配置计费接口（对应命令为**SET CHGMODE**）。图1绘制了不同类型终端接入不同网络时计费接口选择。**图1** 不同类型终端接入不同网络时计费接口选择逻辑图SGW-C独立部署的场景下，需要SGW-C发起计费会话。在这种场景下，通过设置SGW-C上**ADD ROAMCHGMODE**/**ADD APNCHGMODE**/**SET CHGMODE**命令中**FORSGWONLY**的值可以手动指定计费接口。UNC支持配置在不同类型终端接入不同网络时选择策略接口，策略接口选择有两种方式，优先级从高到低为：基于APN/DNN选择策略接口 > 全局配置策略接口。图2绘制了不同类型终端接入不同网络时策略接口选择。**图2** 不同类型终端接入不同网络时策略接口选择逻辑图当UNC通过上述方式配置了计费接口和策略接口后，可通过**ADD PCCCHGMODEBYPCFID**命令基于PCF instance ID配置用户最终使用的策略接口类型和计费接口类型。

## 必备事项
前提条件

* 请仔细阅读融合计费原理。
* 完成加载License。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    set_chgmode_list:
      type: items
      properties:
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
          description: '配置5G终端接入4G网络时使用的计费接口模式。  说明：  本示例配置5G终端接入4G网络时，使用Nchf接口模式。请根据实际情况使用该命令进行配置。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        BY5GSIWKI:
          name: '按5GS互操作指示选择计费接口'
          type: string
          enum:
          - False
          - True
          required: false
          description: ''
          data_source: '全网规划'
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
          description: ''
          data_source: '全网规划'
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
          data_source: '全网规划'
          pattern: ''
          default: ''
        ISMFCHGSW:
          name: 'ISMF是否支持计费'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        BYIWKUEN5GR4G:
          name: '非5G终端4G接入时按5GS互操作指示选择计费接口'
          type: string
          enum:
          - False
          - True
          required: false
          description: ''
          data_source: '全网规划'
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
          default: ''
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
    add_apnchgmode_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '（可选）基于APN/DNN配置计费接口模式。当全局配置不能满足诉求，需要基于APN/DNN对某些用户群做特殊计费接口配置时，可以执行此操作。  说明：  本示例配置对于APN为ap-test的5G终端接入4G网络时，使用Nchf接口。请根据实际情况使用该命令进行配置。'
          data_source: '已配置数据中获取'
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
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        BY5GSIWKI:
          name: '按5GS互操作指示选择计费接口'
          type: string
          enum:
          - False
          - True
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: False
        FORCED:
          name: '指定的计费接口'
          type: string
          enum:
          - GaGyMode
          - NchfMode
          - INVALID
          required: false
          description: ''
          data_source: '全网规划'
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
    add_roamchgmode_list:
      type: items
      properties:
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
          description: '（可选）基于终端漫游属性计费接口模式。当全局配置不能满足诉求，需要基于漫游属性对某些用户群做特殊计费接口配置时，可以执行此操作。  说明：  本示例配置对于全局的漫游用户，在使用5G终端接入4G网络时，使用Nchf计费接口；UNC作为V-SMF时，计费接口使用Nchf接口模式。请根据实际情况使用该命令进行配置。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        CTRLTYPE:
          name: '控制类型'
          type: string
          enum:
          - APN_LEVEL
          - GLOBAL_LEVEL
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        ROAMINGTYPE:
          name: '漫游属性'
          type: string
          enum:
          - ROAMING
          - VISITING
          - HOME
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        BY5GSIWKI:
          name: '按5GS互操作指示选择计费接口'
          type: string
          enum:
          - False
          - True
          required: false
          description: ''
          data_source: '全网规划'
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
          description: ''
          data_source: '全网规划'
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
          data_source: '全网规划'
          pattern: ''
          default: ''
        APN:
          name: 'APN名称'
          type: string
          minLength: 1
          maxLength: 63
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        BY5GCNRI:
          name: '按5GC无限制接入标识选择计费'
          type: string
          enum:
          - False
          - True
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
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
    add_pccchgmodebypcfid_list:
      type: items
      properties:
        PCFINSID:
          name: 'PCF实例标识'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '（可选）一般情况下不需要配置该命令，当需要基于PCF实例标识调整用户最终使用的策略接口类型 (N7/Gx) 或计费接口类型 (N40/GaGy) 时，可以通过该命令进行配置。  用户的计费接口类型以**ADD APNCHGMODE**或**SET CHGMODE**为初选结果，在此基础上，可以通过本命令决策是否由N40回落GaGy，或者是否由GaGy升级为N40。  说明：  本示例以pcf1，策略接口类型为N7，计费接口类型继承**ADD APNCHGMODE**或**SET CHGMODE**命令配置举例。请根据实际情况使用该命令进行配置。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        POLICYINTF:
          name: '策略接口类型'
          type: string
          enum:
          - INHERIT
          - N7
          - Gx
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        CHGINTF:
          name: '计费接口类型'
          type: string
          enum:
          - INHERIT
          - N40
          - GaGy
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
  examples:
    set_chgmode_list:
    - TMACCTYPE: UE5G_RAT4G
      BY5GSIWKI: False
      FORCED: NchfMode
      FORVSMFONLY: NchfMode
      ISMFCHGSW: DISABLE
      BYIWKUEN5GR4G: False
      BY5GCNRI: ''
      FORSGWONLY: ''
    add_apnchgmode_list:
    - APN: 'apn-test'
      TMACCTYPE: UE5G_RAT4G
      BY5GSIWKI: False
      FORCED: NchfMode
      BY5GCNRI: False
      FORSGWONLY: ''
      FORVSMFONLY: ''
      ISMFCHGSW: ''
    add_roamchgmode_list:
    - TMACCTYPE: UE5G_RAT4G
      CTRLTYPE: GLOBAL_LEVEL
      ROAMINGTYPE: ROAMING
      BY5GSIWKI: False
      FORCED: NchfMode
      FORVSMFONLY: NchfMode
      APN: ''
      BY5GCNRI: ''
      FORSGWONLY: ''
    add_pccchgmodebypcfid_list:
    - PCFINSID: 'pcf1'
      POLICYINTF: N7
      CHGINTF: INHERIT
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 配置在不同类型终端接入不同网络时所选择的计费接口。

```jinja2
{%- for item in set_chgmode_list -%}
    SET CHGMODE:
    {#- --- 必选参数 --- -#}
    TMACCTYPE={{item.TMACCTYPE}},
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：TMACCTYPE=UE5G_RAT4G 时可选 --- -#}
    {%- if item.TMACCTYPE == 'UE5G_RAT4G' -%}
        {%- if item.BY5GSIWKI is not none -%}
            BY5GSIWKI={{item.BY5GSIWKI}},
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
    {#- --- 条件可选：TMACCTYPE=UENON5G_RAT4G 时可选 --- -#}
    {%- if item.TMACCTYPE == 'UENON5G_RAT4G' -%}
        {%- if item.BYIWKUEN5GR4G is not none -%}
            BYIWKUEN5GR4G={{item.BYIWKUEN5GR4G}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：TMACCTYPE=UENON5G_RAT4G/UE5G_RAT4G 时可选 --- -#}
    {%- if item.TMACCTYPE in ['UENON5G_RAT4G', 'UE5G_RAT4G'] -%}
        {%- if item.BY5GCNRI is not none -%}
            BY5GCNRI={{item.BY5GCNRI}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：TMACCTYPE=UENON5G_RAT4G/UE5G_RAT4G 时可选 --- -#}
    {%- if item.TMACCTYPE in ['UENON5G_RAT4G', 'UE5G_RAT4G'] -%}
        {%- if item.FORSGWONLY is not none -%}
            FORSGWONLY={{item.FORSGWONLY}},
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

### 2 **可选：**配置不同的APN/DNN在不同类型终端接入不同网络时所选择的计费接口。

```jinja2
{%- if is_optional_apn_dnn_chgmode -%}
    {%- for item in add_apnchgmode_list -%}
        ADD APNCHGMODE:
        {#- --- 必选参数 --- -#}
        APN="{{item.APN}}",
        TMACCTYPE={{item.TMACCTYPE}},
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：TMACCTYPE=UENON5G_RAT4G/UE5G_RAT4G 时可选 --- -#}
        {%- if item.TMACCTYPE in ['UENON5G_RAT4G', 'UE5G_RAT4G'] -%}
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
{%- endif -%}
```

### 3 **可选：**配置不同漫游类型在不同类型终端接入不同网络时所选择的计费接口。

```jinja2
{%- if is_optional_roaming_chgmode -%}
    {%- for item in add_roamchgmode_list -%}
        ADD ROAMCHGMODE:
        {#- --- 必选参数 --- -#}
        TMACCTYPE={{item.TMACCTYPE}},
        CTRLTYPE={{item.CTRLTYPE}},
        ROAMINGTYPE={{item.ROAMINGTYPE}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：CTRLTYPE=APN_LEVEL 时必选 --- -#}
        {%- if item.CTRLTYPE == 'APN_LEVEL' -%}
            APN="{{item.APN}}",
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：TMACCTYPE=UE5G_RAT4G/UENON5G_RAT4G 时可选 --- -#}
        {%- if item.TMACCTYPE in ['UE5G_RAT4G', 'UENON5G_RAT4G'] -%}
            {%- if item.BY5GSIWKI is not none -%}
                BY5GSIWKI={{item.BY5GSIWKI}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：TMACCTYPE=UE5G_RAT5G 时可选 --- -#}
        {%- if item.TMACCTYPE == 'UE5G_RAT5G' -%}
            {%- if item.FORVSMFONLY is not none -%}
                FORVSMFONLY={{item.FORVSMFONLY}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：TMACCTYPE=UE5G_RAT4G/UENON5G_RAT4G 时可选 --- -#}
        {%- if item.TMACCTYPE in ['UE5G_RAT4G', 'UENON5G_RAT4G'] -%}
            {%- if item.BY5GCNRI is not none -%}
                BY5GCNRI={{item.BY5GCNRI}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：TMACCTYPE=UE5G_RAT4G/UENON5G_RAT4G 时可选 --- -#}
        {%- if item.TMACCTYPE in ['UE5G_RAT4G', 'UENON5G_RAT4G'] -%}
            {%- if item.FORSGWONLY is not none -%}
                FORSGWONLY={{item.FORSGWONLY}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件必选/可选参数 --- -#}
        {#- --- 指定的计费接口: 条件必选(指定终端和接入类型=RAT2G|RATNBIOT|NON_3GPP|RATLTEM|RAT3G|UE5G_RAT5G) / 条件可选(指定终端和接入类型=UE5G_RAT4G|UENON5G_RAT4G) --- -#}
        {%- if (item.TMACCTYPE in ['RAT2G', 'RATNBIOT', 'NON_3GPP', 'RATLTEM', 'RAT3G', 'UE5G_RAT5G']) -%}
            FORCED={{item.FORCED}},
        {%- elif (item.TMACCTYPE in ['UE5G_RAT4G', 'UENON5G_RAT4G']) -%}
            {%- if item.FORCED is not none -%}
                FORCED={{item.FORCED}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 4 **可选：**配置基于PCF的计费接口和策略接口类型。

```jinja2
{%- if is_optional_pcf_chgmode -%}
    {%- for item in add_pccchgmodebypcfid_list -%}
        ADD PCCCHGMODEBYPCFID:
        {#- --- 必选参数 --- -#}
        CHGINTF={{item.CHGINTF}},
        PCFINSID="{{item.PCFINSID}}",
        POLICYINTF={{item.POLICYINTF}},
        ;
    {%- endfor -%}
{%- endif -%}
```

### 一般情况下不需要配置该命令，当需要基于PCF实例标识调整用户最终使用的策略接口类型 (N7/Gx) 或计费接口类型 (N40/GaGy) 时，可以通过该命令进行配置。


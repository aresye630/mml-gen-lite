---
id: ''
name: 配置5G网络基于实时位置的策略控制功能
ne_type: UNC
type: feature
description: 本章节介绍5G用户接入5G网络场景如何开启基于实时位置信息的策略控制功能。本场景下，仅需在SMF配置相关参数。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","智能PCC解决方案","基于实时位置的策略控制","5G网络基于实时位置的策略控制","配置5G网络基于实时位置的策略控制功能"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本章节介绍5G用户接入5G网络场景如何开启基于实时位置信息的策略控制功能。本场景下，仅需在SMF配置相关参数。

## 必备事项
前提条件

前提条件

* 完成加载License（如果有需求，请联系华为技术支持工程师处理）。

* 部署本特性会增加N7接口的负荷，因此在部署本特性之前请对现有网络的业务模型、资费策略、网络资源占用情况进行评估，以降低对整个网络的负荷冲击。
* 需要对端网元PCF激活基于实时位置信息的策略控制功能。
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
          description: '-'
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
          description: '-'
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
    set_n7rcvattrctrl_list:
      type: items
      properties:
        SCELLCHNR:
          name: 'SCELL\_CH是否允许上报NCGI'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '当PCF下发基于Cell粒度的位置Trigger时，需在SMF开启该功能。'
          data_source: '对端协商'
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
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_smcommfunc_list_1:
      type: items
      properties:
        LOCREPORT:
          name: '位置上报'
          type: string
          enum:
          - NotSupport
          - Support
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_apn_list_1:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '-'
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
    set_locationreport_list:
      type: items
      properties:
        TAITRIGGERFLG:
          name: '配置跟踪区的trigger'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        ULITRIGGERFLG:
          name: '配置用户位置信息的trigger'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '当PCF没有下发位置相关Trigger时，可根据规划在SMF配置位置相关Trigger。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        NCGITRIGGERFLG:
          name: '配置NR全球小区的trigger'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        ULITRIROAMING:
          name: '基于用户漫游属性控制ULI信息上报'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        TAITRIROAMING:
          name: '基于用户漫游属性控制TAI信息上报'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        NCGITRIROAMING:
          name: '基于用户漫游属性控制NCGI信息上报'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        TAITRIRAT:
          name: '基于用户RAT类型控制TAI信息上报'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ULITRIRAT:
          name: '基于用户RAT类型控制ULI信息上报'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV2PYCTRL1'
      SWITCH: ENABLE
    set_smcommfunc_list:
    - LOCREPORT: Support
    add_apn_list:
    - APN: 'huawei.com'
      LOCREPORT: INHERIT
    set_n7rcvattrctrl_list:
    - SCELLCHNR: ENABLE
    set_licenseswitch_list_1:
    - LICITEM: 'LKV2PYCTRL1'
      SWITCH: ENABLE
    set_smcommfunc_list_1:
    - LOCREPORT: Support
    add_apn_list_1:
    - APN: 'huawei.com'
      LOCREPORT: INHERIT
    set_locationreport_list:
    - TAITRIGGERFLG: ENABLE
      ULITRIGGERFLG: ENABLE
      NCGITRIGGERFLG: ENABLE
      ULITRIROAMING: ROAMING（漫游用户）
      TAITRIROAMING: ROAMING（漫游用户）
      NCGITRIROAMING: ROAMING（漫游用户）
      TAITRIRAT: ''
      ULITRIRAT: ''
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 任务一：PCF下发基于Cell粒度的位置Trigger场景，在SMF侧配置基于实时位置的策略控制功能。

#### 1.1 //开启基于实时位置信息的策略控制功能的License。

```jinja2
{%- if is_scenario_pcf_cell_trigger -%}
    {%- for item in set_licenseswitch_list -%}
        SET LICENSESWITCH:
        {#- --- 必选参数 --- -#}
        LICITEM="{{item.LICITEM}}",
        SWITCH={{item.SWITCH}},
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 1.2 //开启全局位置上报功能。

```jinja2
{%- if is_scenario_pcf_cell_trigger -%}
    {%- for item in set_smcommfunc_list -%}
        SET SMCOMMFUNC:
        {#- --- 可选参数 --- -#}
        {%- if item.LOCREPORT is not none -%}
            LOCREPORT={{item.LOCREPORT}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 1.3 //设置APN（huawei.com）的位置上报功能，指定该APN的位置上报功能继承全局配置。

```jinja2
{%- if is_scenario_pcf_cell_trigger -%}
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
{%- endif -%}
```

#### 1.4 //开启NCGI订阅和上报功能。

```jinja2
{%- if is_scenario_pcf_cell_trigger -%}
    {%- for item in set_n7rcvattrctrl_list -%}
        SET N7RCVATTRCTRL:
        {#- --- 可选参数 --- -#}
        {%- if item.SCELLCHNR is not none -%}
            SCELLCHNR={{item.SCELLCHNR}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 2 任务二：SMF本地配置位置Trigger场景，开启基于TAI粒度的实时位置策略控制功能。

#### 2.1 //开启基于实时位置信息的策略控制功能的License。

```jinja2
{%- if is_scenario_smf_local_tai_trigger -%}
    {%- for item in set_licenseswitch_list_1 -%}
        SET LICENSESWITCH:
        {#- --- 必选参数 --- -#}
        LICITEM="{{item.LICITEM}}",
        SWITCH={{item.SWITCH}},
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 2.2 //开启全局位置上报功能。

```jinja2
{%- if is_scenario_smf_local_tai_trigger -%}
    {%- for item in set_smcommfunc_list_1 -%}
        SET SMCOMMFUNC:
        {#- --- 可选参数 --- -#}
        {%- if item.LOCREPORT is not none -%}
            LOCREPORT={{item.LOCREPORT}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 2.3 //设置APN（huawei.com）的位置上报功能，指定该APN的位置上报功能继承全局配置。

```jinja2
{%- if is_scenario_smf_local_tai_trigger -%}
    {%- for item in add_apn_list_1 -%}
        ADD APN:
        {#- --- 必选参数 --- -#}
        APN="{{item.APN}}",
        {#- --- 可选参数 --- -#}
        {%- if item.LOCREPORT is not none -%}
            LOCREPORT={{item.LOCREPORT}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 2.4 //配置本地TAI位置Trigger。

```jinja2
{%- if is_scenario_smf_local_tai_trigger -%}
    {%- for item in set_locationreport_list -%}
        SET LOCATIONREPORT:
        {#- --- 可选参数 --- -#}
        {%- if item.TAITRIGGERFLG is not none -%}
            TAITRIGGERFLG={{item.TAITRIGGERFLG}},
        {%- endif -%}
        {%- if item.NCGITRIGGERFLG is not none -%}
            NCGITRIGGERFLG={{item.NCGITRIGGERFLG}},
        {%- endif -%}
        {%- if item.ULITRIGGERFLG is not none -%}
            ULITRIGGERFLG={{item.ULITRIGGERFLG}},
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：NCGITRIGGERFLG=ENABLE 时可选 --- -#}
        {%- if item.NCGITRIGGERFLG == 'ENABLE' -%}
            {%- if item.NCGITRIROAMING is not none -%}
                NCGITRIROAMING={{item.NCGITRIROAMING}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：TAITRIGGERFLG=ENABLE 时可选 --- -#}
        {%- if item.TAITRIGGERFLG == 'ENABLE' -%}
            {%- if item.TAITRIRAT is not none -%}
                TAITRIRAT={{item.TAITRIRAT}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：TAITRIGGERFLG=ENABLE 时可选 --- -#}
        {%- if item.TAITRIGGERFLG == 'ENABLE' -%}
            {%- if item.TAITRIROAMING is not none -%}
                TAITRIROAMING={{item.TAITRIROAMING}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：ULITRIGGERFLG=ENABLE 时可选 --- -#}
        {%- if item.ULITRIGGERFLG == 'ENABLE' -%}
            {%- if item.ULITRIRAT is not none -%}
                ULITRIRAT={{item.ULITRIRAT}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：ULITRIGGERFLG=ENABLE 时可选 --- -#}
        {%- if item.ULITRIGGERFLG == 'ENABLE' -%}
            {%- if item.ULITRIROAMING is not none -%}
                ULITRIROAMING={{item.ULITRIROAMING}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```


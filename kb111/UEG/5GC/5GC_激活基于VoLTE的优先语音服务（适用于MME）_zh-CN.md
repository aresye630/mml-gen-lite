---
id: ''
name: 激活基于VoLTE的优先语音服务（适用于MME）
ne_type: UEG
type: feature
description: 本操作指导介绍在运行网络中激活基于VoLTE的优先语音服务业务特性的操作过程，包括两种方案，配置MPS业务功能和配置语音寻呼优先业务功能。  **表1** 优先级方案对比  | 方案 | 是否需要用户签约 | 应用业务场景 | 部署建议 | | --- | --- | --- | --- | | 语音寻呼优先业务（推荐） | 否 | 仅针对VoLTE/CSFB被叫业务 | VoLTE组网场景下推荐部署本方案，以提升被叫寻呼成功率，提升用户语音业务体验。 | | MPS业务 | 是 | 针对所有业务 | MPS业务的优先级高于语音寻呼优先业务，该方案可提升特定签约用户享用网络资源的优先级。 |  适用于MME。
tags: []
risk_level: ''
doc_source: ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（火电专网，入驻式）","部署配置指导","中心园区部署入驻式UEG-L","配置业务数据（风筝L）","语音功能配置","MME&AMF&GW-C&SMF配置","VoLTE基本功能","激活基于VoLTE的优先语音服务（适用于MME）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
本操作指导介绍在运行网络中激活基于VoLTE的优先语音服务业务特性的操作过程，包括两种方案，配置MPS业务功能和配置语音寻呼优先业务功能。**表1** 优先级方案对比| 方案 | 是否需要用户签约 | 应用业务场景 | 部署建议 || --- | --- | --- | --- || 语音寻呼优先业务（推荐） | 否 | 仅针对VoLTE/CSFB被叫业务 | VoLTE组网场景下推荐部署本方案，以提升被叫寻呼成功率，提升用户语音业务体验。 || MPS业务 | 是 | 针对所有业务 | MPS业务的优先级高于语音寻呼优先业务，该方案可提升特定签约用户享用网络资源的优先级。 |适用于MME。

## 必备事项
前提条件

* 请仔细阅读GWFD-025402 基于VoLTE的优先语音服务特性概述。
* 已经加载支持该特性的License。
* 本特性需要在MME、eNodeB、SGW-C/PGW-C、PCRF、SPR、P-CSCF等网元上完成基本业务的数据配置。
* 用户需要在HSS签约相应数据。
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
    set_mmfunc_list:
      type: items
      properties:
        VOICEPAGINGPRIORITY:
          name: '是否支持语音优先寻呼'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: '开启语音寻呼优先功能。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    set_mpsarp_list:
      type: items
      properties:
        MPSFUNC:
          name: 'MPS功能开关'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: '配置MPS业务数据。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        PRILVL:
          name: '优先级'
          type: integer
          minimum: 0
          maximum: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV2EMPS01'
      SWITCH: ENABLE
    set_mmfunc_list:
    - VOICEPAGINGPRIORITY: YES
    set_mpsarp_list:
    - MPSFUNC: ON
      PRILVL: 7
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 进入“MML命令行-UEG”窗口。

### 2 打开本特性的License配置开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

### 3 **推荐：**部署语音寻呼优先业务。

```jinja2
{%- if is_scenario_voice_paging_priority -%}
    {%- for item in set_mmfunc_list -%}
        SET MMFUNC:
        {#- --- 可选参数 --- -#}
        {%- if item.VOICEPAGINGPRIORITY is not none -%}
            VOICEPAGINGPRIORITY={{item.VOICEPAGINGPRIORITY}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 4 **可选：**部署MPS业务。

```jinja2
{%- if is_optional_mps_service -%}
    {%- for item in set_mpsarp_list -%}
        SET MPSARP:
        {#- --- 可选参数 --- -#}
        {%- if item.MPSFUNC is not none -%}
            MPSFUNC={{item.MPSFUNC}},
        {%- endif -%}
        {%- if item.PRILVL is not none -%}
            PRILVL={{item.PRILVL}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 步骤3和步骤4部署时二选一，推荐部署语音寻呼优先业务。


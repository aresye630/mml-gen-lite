---
id: GWFD-026105
name: 激活基于信令面的数据传输（MME）
ne_type: UEG
type: feature
description: 本操作指导介绍在运行网络中激活基于信令面的数据传输的操作过程。  IoT终端数据收发频率低、数据包较小且多数情况为单向发送（例如智能抄表）。本特性是3GPP协议针对此类业务定义的控制面优化功能CP-CIoT（Control Plane Cellular Internet of Thing），实现了数据包在终端和MME之间通过NAS消息传递，在MME和SGW-U间通过S11-U口传递，上、下行数传过程中无需频繁建立E-RAB，从而提升数传效率，节省不必要的信令开销。  适用于MME。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝L","MEC 特性指南（风筝L）","MME特性指南","GWFD-026100 NB-IoT基本功能","GWFD-026105 基于信令面的数据传输（MME）","激活基于信令面的数据传输（MME）"]
refs: []
metadata:
  DepOnLiveCfg: true
allowed-tools:
- getParameterValue('LST M2MPLCY')
- getParameterValue('LST TAICIOT')
---
<!-- @mml:block= annotations -->
```text
## 操作场景
本操作指导介绍在运行网络中激活基于信令面的数据传输的操作过程。IoT终端数据收发频率低、数据包较小且多数情况为单向发送（例如智能抄表）。本特性是3GPP协议针对此类业务定义的控制面优化功能CP-CIoT（Control Plane Cellular Internet of Thing），实现了数据包在终端和MME之间通过NAS消息传递，在MME和SGW-U间通过S11-U口传递，上、下行数传过程中无需频繁建立E-RAB，从而提升数传效率，节省不必要的信令开销。适用于MME。

## 必备事项
前提条件

* 请仔细阅读GWFD-026105 基于信令面的数据传输特性概述（MME）。
* 已按照配置到S-GW的数据完成S11-U接口的配置。
* 完成加载License。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    add_m2mplcy_list:
      type: items
      properties:
        SUBRANGE:
          name: '用户范围'
          type: string
          enum:
          - ALL_USER
          - FOREIGN_USER
          - HOME_USER
          - IMSI_PREFIX
          required: true
          description: '增加M2M的策略参数，即为不同范围的用户、不同的APN业务配置M2M业务相关参数，以满足运营商灵活部署网络的需求。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        IMSIPRE:
          name: 'IMSI前缀'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        APNNI:
          name: 'APNNI'
          type: string
          maxLength: 62
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LONGRAUTAUTMR:
          name: '长周期RAU或TAU定时器时长（小时）'
          type: integer
          minimum: 0
          maximum: 10000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 0
        CPOPSW:
          name: 'CP优化功能'
          type: string
          enum:
          - NOT_SUPPORT
          - SUPPORT
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NOT_SUPPORT
    mod_m2mplcy_list:
      type: items
      properties:
        SUBRANGE:
          name: '用户范围'
          type: string
          enum:
          - ALL_USER
          - FOREIGN_USER
          - HOME_USER
          - IMSI_PREFIX
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        APNNI:
          name: 'APNNI'
          type: string
          maxLength: 62
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_taiciot_list:
      type: items
      properties:
        BEGINTAI:
          name: '起始TAI'
          type: string
          maxLength: 10
          required: true
          description: '增加指定TAI下eNodeB支持的CIoT能力。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        ENDTAI:
          name: '终止TAI'
          type: string
          maxLength: 10
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NBDATATRANSSUPPORT:
          name: '窄带数据传输能力指示'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    mod_taiciot_list:
      type: items
      properties:
        BEGINTAI:
          name: '起始TAI'
          type: string
          maxLength: 10
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
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
    add_m2mplcy_list:
    - SUBRANGE: IMSI_PREFIX
      IMSIPRE: '123038101'
      APNNI: 'HUAWEI1.com'
      LONGRAUTAUTMR: 0
      CPOPSW: SUPPORT
    mod_m2mplcy_list:
    - SUBRANGE: ''
      APNNI: ''
    add_taiciot_list:
    - BEGINTAI: '123037301'
      ENDTAI: '123037302'
      NBDATATRANSSUPPORT: SUPPORT_CP-1
    mod_taiciot_list:
    - BEGINTAI: ''
    set_licenseswitch_list:
    - LICITEM: 'LKV2DNAS01'
      SWITCH: ENABLE
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 进入“MML命令行-UEG”窗口。

### 2 配置CP-CIoT功能。

#### 2.1 查询某指定用户范围是否配置了CP-CIoT功能。

#### 2.2 **可选：**如果步骤a未查询到该指定用户范围的相关配置，则执行此步骤，为该用户范围配置CP-CIoT功能。

```jinja2
{%- set LST_M2MPLCY=getParameterValue('LST M2MPLCY') -%}
{%- if is_optional_configure_cp_ciot and LST_M2MPLCY=='' -%}
    {%- for item in add_m2mplcy_list -%}
        ADD M2MPLCY:
        {#- --- 必选参数 --- -#}
        SUBRANGE={{item.SUBRANGE}},
        APNNI="{{item.APNNI}}",
        {#- --- 可选参数 --- -#}
        {%- if item.LONGRAUTAUTMR is not none -%}
            LONGRAUTAUTMR={{item.LONGRAUTAUTMR}},
        {%- endif -%}
        {%- if item.CPOPSW is not none -%}
            CPOPSW={{item.CPOPSW}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：SUBRANGE=IMSI_PREFIX 时必选 --- -#}
        {%- if item.SUBRANGE == 'IMSI_PREFIX' -%}
            IMSIPRE="{{item.IMSIPRE}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 2.3 **可选：**如果步骤a查询到系统已存在该指定用户范围的相关配置，则执行此步骤，为该用户范围添加CP-CIoT功能。

```jinja2
{%- if is_optional_add_cp_ciot and LST_M2MPLCY -%}
    {%- for item in mod_m2mplcy_list -%}
        MOD M2MPLCY:
        {#- --- 必选参数 --- -#}
        APNNI="{{item.APNNI}}",
        SUBRANGE={{item.SUBRANGE}},
        ;
    {%- endfor -%}
{%- endif -%}
```

### 3 **可选：**配置某指定TAI下eNodeB的CP-CIoT能力。

#### 3.1 查询某指定TAI下相关配置。

#### 3.2 **可选：**如果3.a未查询到该指定TAI下的相关配置，则执行此步骤，为该TAI下的eNodeB配置CP-CIoT能力。

```jinja2
{%- set LST_TAICIOT=getParameterValue('LST TAICIOT') -%}
{%- if is_optional_configure_cp_ciot_capability and LST_TAICIOT=='' -%}
    {%- for item in add_taiciot_list -%}
        ADD TAICIOT:
        {#- --- 必选参数 --- -#}
        BEGINTAI="{{item.BEGINTAI}}",
        {#- --- 可选参数 --- -#}
        {%- if item.ENDTAI is not none -%}
            ENDTAI="{{item.ENDTAI}}",
        {%- endif -%}
        {%- if item.NBDATATRANSSUPPORT is not none -%}
            NBDATATRANSSUPPORT={{item.NBDATATRANSSUPPORT}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 3.3 **可选：**如果3.a查询到系统已存在该指定TAI下的相关配置，且不支持CP-CIoT能力，则执行此步骤，为该TAI下的eNodeB添加CP-CIoT能力。

```jinja2
{%- if is_optional_configure_cp_ciot_capability and is_optional_add_cp_ciot_capability and LST_TAICIOT -%}
    {%- for item in mod_taiciot_list -%}
        MOD TAICIOT:
        {#- --- 必选参数 --- -#}
        BEGINTAI="{{item.BEGINTAI}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

### 4 **可选：**配置Control Plane Service Request流程CHR单据的上报。

### 系统支持通过命令**SET CHRCFG**和**SET CHRLOWPERFSVRSUB**配置在Control Plane Service Request流程成功或失败时是否上报CHR单据，配置过程参见激活CHR功能。

### 5 打开本功能的License配置开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```


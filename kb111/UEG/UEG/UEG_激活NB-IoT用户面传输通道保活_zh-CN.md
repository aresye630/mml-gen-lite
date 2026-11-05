---
id: GWFD-026106
name: 激活NB-IoT用户面传输通道保活
ne_type: UEG
type: feature
description: 本操作指导介绍在运行网络中激活NB-IoT用户面传输通道保活的操作过程。  NB-IoT终端数据收发频率低、数据包较小且多数情况为单向发送（例如智能抄表），建立、释放S1–U连接和数据无线承载信令开销大，需要一种高效的小数据传输解决方案。3GPP协议针对此类业务定义了用户面优化功能UP-CIoT（User Plane CIoT EPS Optimization）。UP-CIoT的方式是当终端进入ECM-IDLE态时，UE、eNodeB和MME保存用于恢复连接的S1-AP关联、UE上下文和承载上下文数据。当需要恢复数传时，无需进行频繁的E-RAB重建，提升数传效率，节省信令开销。  适用于MME。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝L","MEC 特性指南（风筝L）","MME特性指南","GWFD-026100 NB-IoT基本功能","GWFD-026106 NB-IoT用户面传输通道保活","激活NB-IoT用户面传输通道保活"]
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
本操作指导介绍在运行网络中激活NB-IoT用户面传输通道保活的操作过程。NB-IoT终端数据收发频率低、数据包较小且多数情况为单向发送（例如智能抄表），建立、释放S1–U连接和数据无线承载信令开销大，需要一种高效的小数据传输解决方案。3GPP协议针对此类业务定义了用户面优化功能UP-CIoT（User Plane CIoT EPS Optimization）。UP-CIoT的方式是当终端进入ECM-IDLE态时，UE、eNodeB和MME保存用于恢复连接的S1-AP关联、UE上下文和承载上下文数据。当需要恢复数传时，无需进行频繁的E-RAB重建，提升数传效率，节省信令开销。适用于MME。

## 必备事项
前提条件

请仔细阅读GWFD-026106 NB-IoT用户面传输通道保活特性概述。

完成加载License。
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
        S1UCAPA:
          name: 'S1-U能力'
          type: string
          enum:
          - NOT_SUPPORT
          - SUPPORT_S1UDATA
          - SUPPORT_S1UDATA_AND_UP
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
      IMSIPRE: '123037301'
      APNNI: 'HUAWEI1.com'
      S1UCAPA: SUPPORT_S1UDATA_AND_UP
    mod_m2mplcy_list:
    - SUBRANGE: ''
      APNNI: ''
    add_taiciot_list:
    - BEGINTAI: '123037301'
      ENDTAI: '123037301'
      NBDATATRANSSUPPORT: SUPPORT_UP-1&SUPPORT_S1U-1
    mod_taiciot_list:
    - BEGINTAI: ''
    set_licenseswitch_list:
    - LICITEM: 'LKV2UPTH01'
      SWITCH: ENABLE
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 进入“MML命令行-UEG”窗口。

### 2 配置UP-CIoT功能。

#### 2.1 查询某指定用户范围的相关配置。

#### 2.2 **可选：**如果2.a未查询到该指定用户范围的相关配置，则执行此步骤，为该用户范围配置UP-CIoT功能。

```jinja2
{%- set LST_M2MPLCY=getParameterValue('LST M2MPLCY') -%}
{%- if is_optional_configure_user_range_up_ciot and LST_M2MPLCY=='' -%}
    {%- for item in add_m2mplcy_list -%}
        ADD M2MPLCY:
        {#- --- 必选参数 --- -#}
        SUBRANGE={{item.SUBRANGE}},
        APNNI="{{item.APNNI}}",
        {#- --- 可选参数 --- -#}
        {%- if item.S1UCAPA is not none -%}
            S1UCAPA={{item.S1UCAPA}},
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

#### 2.3 **可选：**如果2.a查询到系统已存在该指定用户范围的相关配置，且未配置UP-CIoT功能，则执行此步骤，为该用户范围添加UP-CIoT功能。

```jinja2
{%- if is_optional_add_user_range_up_ciot and LST_M2MPLCY -%}
    {%- for item in mod_m2mplcy_list -%}
        MOD M2MPLCY:
        {#- --- 必选参数 --- -#}
        APNNI="{{item.APNNI}}",
        SUBRANGE={{item.SUBRANGE}},
        ;
    {%- endfor -%}
{%- endif -%}
```

### 3 **可选：**配置某指定TAI下eNodeB的UP-CIoT能力。

#### 3.1 查询某指定TAI下相关配置。

#### 3.2 **可选：**如果3.a未查询到该指定TAI下的相关配置，则执行此步骤，为该TAI下的eNodeB配置UP-CIoT能力。

```jinja2
{%- set LST_TAICIOT=getParameterValue('LST TAICIOT') -%}
{%- if is_optional_configure_enodeb_up_ciot and LST_TAICIOT=='' -%}
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

#### 3.3 **可选：**如果3.a查询到系统已存在该指定TAI下的相关配置，且不支持UP-CIoT能力，则执行此步骤，为该TAI下的eNodeB添加UP-CIoT能力。

```jinja2
{%- if is_optional_configure_enodeb_up_ciot and is_optional_add_enodeb_up_ciot and LST_TAICIOT -%}
    {%- for item in mod_taiciot_list -%}
        MOD TAICIOT:
        {#- --- 必选参数 --- -#}
        BEGINTAI="{{item.BEGINTAI}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

### 4 打开本功能的License配置开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```


---
id: ''
name: 激活NB-IoT终端的位置延迟定位服务
ne_type: UNC
type: feature
description: 本操作指导介绍在运行网络中激活NB-IoT终端的位置延迟定位服务特性的操作过程。  适用于MME。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","NB-IOT业务功能","WSFD-215206 NB-IoT终端的位置延迟定位服务","激活NB-IoT终端的位置延迟定位服务"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本操作指导介绍在运行网络中激活NB-IoT终端的位置延迟定位服务特性的操作过程。适用于MME。

## 必备事项
前提条件

前提条件

* 操作人员已经登录U2020\MAE-Access。
* 本特性为可选特性，需要加载支持该特性的License，对应的License项为“NB-IoT终端的位置延迟定位服务”。
* 3GPP协议定义的标准LCS组网场景下，已经完成SLg和SLs接口数据配置，详细请参见配置到GMLC的数据和配置到E-SMLC的数据。
* 请仔细阅读WSFD-215206 NB-IoT终端的位置延迟定位服务特性概述。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    add_esmlc_list:
      type: items
      properties:
        ESMLCID:
          name: 'E-SMLC 标识'
          type: integer
          minimum: 0
          maximum: 255
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        ESMLCNAME:
          name: 'E-SMLC名称'
          type: string
          maxLength: 20
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RATIESW:
          name: '是否携带RAT Type信元'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NO
    add_gmlcau_list:
      type: items
      properties:
        GMLCID:
          name: 'GMLC 标识'
          type: integer
          minimum: 0
          maximum: 639
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        CLTTYPE:
          name: '支持的客户端类型'
          type: string
          enum:
          - EMERGENCY_SERVICES
          - LAWFUL_INTERCEPT_SERVICES
          - PLMN_OPERATOR_SERVICES
          - VALUE_ADDED_SERVICES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SERTYPE:
          name: '支持的LCS业务类型'
          type: integer
          minimum: 0
          maximum: 127
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_lcspara_list:
      type: items
      properties:
        TR1:
          name: '隐私验证定时器(s)'
          type: integer
          minimum: 1
          maximum: 50
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        POSTIMER:
          name: 'EPC 位置获取定时器(s)'
          type: integer
          minimum: 1
          maximum: 120
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        POSIDLE:
          name: 'EPC 位置信息表老化时长(min)'
          type: integer
          minimum: 1
          maximum: 60
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GMLCAU:
          name: 'EPC UE级的GMLC的鉴权方案'
          type: string
          enum:
          - AUALL
          - AUNONE
          - AUONLYSAMEPLMN
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DELAYLOCTIMER:
          name: '延迟定位超时时长（min）'
          type: integer
          minimum: 1
          maximum: 1440
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LCS4GPOLICY:
          name: '4G LCS定位策略'
          type: string
          enum:
          - NO_ESMLC_POSITION
          - PROTOCOL_POSITION
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LRC:
          name: '启用连接态LRC流程'
          type: string
          enum:
          - NO
          - YES
          required: false
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
    add_esmlc_list:
    - ESMLCID: 1
      ESMLCNAME: 'E-SMLC名称'
      RATIESW: YES
    add_gmlcau_list:
    - GMLCID: 1
      CLTTYPE: PLMN_OPERATOR_SERVICES
      SERTYPE: 3
    set_lcspara_list:
    - TR1: 20
      POSTIMER: 60
      POSIDLE: 60
      GMLCAU: AUALL
      DELAYLOCTIMER: 720
      LCS4GPOLICY: PROTOCOL_POSITION(协议模式定位)
      LRC: ''
    set_licenseswitch_list:
    - LICITEM: 'LKV2DPNB01'
      SWITCH: ENABLE
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 增加一条E-SMLC配置，并设置MME向E-SMLC请求定位时携带RAT Type信元。

```jinja2
{%- for item in add_esmlc_list -%}
    ADD ESMLC:
    {#- --- 必选参数 --- -#}
    ESMLCID={{item.ESMLCID}},
    {#- --- 可选参数 --- -#}
    {%- if item.ESMLCNAME is not none -%}
        ESMLCNAME="{{item.ESMLCNAME}}",
    {%- endif -%}
    {%- if item.RATIESW is not none -%}
        RATIESW={{item.RATIESW}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 如果使用已配置的E-SMLC，请使用**MOD ESMLC**命令，修改“RATIESW”为“YES”。

### 2 增加发起定位请求的GMLC的权限。

```jinja2
{%- for item in add_gmlcau_list -%}
    ADD GMLCAU:
    {#- --- 必选参数 --- -#}
    GMLCID={{item.GMLCID}},
    {#- --- 可选参数 --- -#}
    {%- if item.CLTTYPE is not none -%}
        CLTTYPE={{item.CLTTYPE}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：CLTTYPE=EMERGENCY_SERVICES/VALUE_ADDED_SERVICES/PLMN_OPERATOR_SERVICES/LAWFUL_INTERCEPT_SERVICES 时可选 --- -#}
    {%- if item.CLTTYPE in ['EMERGENCY_SERVICES', 'VALUE_ADDED_SERVICES', 'PLMN_OPERATOR_SERVICES', 'LAWFUL_INTERCEPT_SERVICES'] -%}
        {%- if item.SERTYPE is not none -%}
            SERTYPE={{item.SERTYPE}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 **可选：**设置延迟定位业务的运行参数。

```jinja2
{%- if is_optional_delay_positioning_params -%}
    {%- for item in set_lcspara_list -%}
        SET LCSPARA:
        {#- --- 可选参数 --- -#}
        {%- if item.TR1 is not none -%}
            TR1={{item.TR1}},
        {%- endif -%}
        {%- if item.POSTIMER is not none -%}
            POSTIMER={{item.POSTIMER}},
        {%- endif -%}
        {%- if item.POSIDLE is not none -%}
            POSIDLE={{item.POSIDLE}},
        {%- endif -%}
        {%- if item.GMLCAU is not none -%}
            GMLCAU={{item.GMLCAU}},
        {%- endif -%}
        {%- if item.DELAYLOCTIMER is not none -%}
            DELAYLOCTIMER={{item.DELAYLOCTIMER}},
        {%- endif -%}
        {%- if item.LCS4GPOLICY is not none -%}
            LCS4GPOLICY={{item.LCS4GPOLICY}},
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：LCS4GPOLICY=PROTOCOL_POSITION 时可选 --- -#}
        {%- if item.LCS4GPOLICY == 'PROTOCOL_POSITION' -%}
            {%- if item.LRC is not none -%}
                LRC={{item.LRC}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 4 打开本特性的License配置开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```


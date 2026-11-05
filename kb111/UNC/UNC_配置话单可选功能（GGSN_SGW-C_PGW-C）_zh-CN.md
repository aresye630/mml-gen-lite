---
id: ''
name: 配置话单可选功能（GGSN/SGW-C/PGW-C）
ne_type: UNC
type: feature
description: GGSN/SGW-C/PGW-C上的话单可选功能包含：  * 强制产生话单    在系统测试时，如果GGSN/SGW-C/PGW-C上设置的话单产生条件未到，还不具备自动产生话单时，可采用命令强制产生话单。 * 进行话单缓存    GGSN/SGW-C/PGW-C支持缓存话单的功能，在与CG组中的CG链路中断的情况下，能够将系统生成的话单暂时缓存在介质上。待CG状态正常后，再将缓存的话单重新发送到CG，从而增强了系统对异常情况的处理，最大限度的降低可能出现的风险。  适用于SGW-C、PGW-C、GGSN。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","计费管理功能","WSFD-011201 支持离线计费","激活离线计费","配置话单可选功能（GGSN/SGW-C/PGW-C）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
GGSN/SGW-C/PGW-C上的话单可选功能包含：* 强制产生话单  在系统测试时，如果GGSN/SGW-C/PGW-C上设置的话单产生条件未到，还不具备自动产生话单时，可采用命令强制产生话单。* 进行话单缓存  GGSN/SGW-C/PGW-C支持缓存话单的功能，在与CG组中的CG链路中断的情况下，能够将系统生成的话单暂时缓存在介质上。待CG状态正常后，再将缓存的话单重新发送到CG，从而增强了系统对异常情况的处理，最大限度的降低可能出现的风险。适用于SGW-C、PGW-C、GGSN。

## 必备事项
前提条件

* 请仔细阅读Ga/Gy接口离线/在线计费。
* 完成配置到CG的数据（GGSN/SGW-C/PGW-C）。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    foc_generatecdr_list:
      type: items
      properties:
        RANGE:
          name: '范围'
          type: string
          enum:
          - ALL
          - IMSI
          - MSISDN
          - POD
          required: true
          description: '强制产生话单'
          data_source: '本端规划'
          pattern: ''
          default: ''
        MSISDN:
          name: 'MSISDN'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        IMSI:
          name: 'IMSI'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PODNAME:
          name: 'POD名称'
          type: string
          maxLength: 63
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_ofccdrpara_list:
      type: items
      properties:
        CCFHCDRSW:
          name: 'CCFH强制产生话单开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '用户进行在线计费发生CCFH动作处理后，可在话单中增加CCFH标识。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        CCFHCDRCC:
          name: 'CCFH强制产生话单填充的Charging Characteristics值'
          type: string
          maxLength: 6
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_cdrstrgstatus_list:
      type: items
      properties:
        PODNAME:
          name: 'POD名称'
          type: string
          maxLength: 63
          required: true
          description: '对话单缓存目录**CHARGE1**或者**CHARGE2**中的话单文件进行操作之前，必须锁定目录**CHARGE1**或者**CHARGE2**。操作完成后，要解锁目录**CHARGE1**或者**CHARGE2**。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        DIRECTORY:
          name: '话单缓存目录'
          type: string
          enum:
          - CHARGE1
          - CHARGE2
          - CONVERGED1
          - CONVERGED2
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        STATUS:
          name: '目录状态'
          type: string
          enum:
          - LOCK
          - UNLOCK
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_cdrstoragectrl_list:
      type: items
      properties:
        CDREXPIREDAY:
          name: '话单缓存超期天数'
          type: integer
          minimum: 0
          maximum: 6
          required: false
          description: '配置缓存话单文件的超期时间'
          data_source: '本端规划'
          pattern: ''
          default: ''
        CDREXPIREWEEK:
          name: '话单缓存超期周数'
          type: integer
          minimum: 0
          maximum: 52
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_cdrstrgstatus_list_3:
      type: items
      properties:
        PODNAME:
          name: 'POD名称'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DIRECTORY:
          name: '话单缓存目录'
          type: string
          enum:
          - CHARGE1
          - CHARGE2
          - CONVERGED1
          - CONVERGED2
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        STATUS:
          name: '目录状态'
          type: string
          enum:
          - LOCK
          - UNLOCK
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    foc_generatecdr_list:
    - RANGE: MSISDN
      MSISDN: '1351234568'
      IMSI: ''
      PODNAME: ''
    set_ofccdrpara_list:
    - CCFHCDRSW: ENABLE
      CCFHCDRCC: '0x1000'
    set_cdrstrgstatus_list:
    - PODNAME: 'pod1'
      DIRECTORY: CHARGE2
      STATUS: UNLOCK
    set_cdrstoragectrl_list:
    - CDREXPIREDAY: 3
      CDREXPIREWEEK: 3
    set_cdrstrgstatus_list_3:
    - PODNAME: ''
      DIRECTORY: ''
      STATUS: ''
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 配置强制产生话单。

#### 1.1 配置强制产生话单（包括G-CDR、eG-CDR、PGW-CDR、SGW-CDR）。

```jinja2
{%- for item in foc_generatecdr_list -%}
    FOC GENERATECDR:
    {#- --- 必选参数 --- -#}
    RANGE={{item.RANGE}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：RANGE=MSISDN 时必选 --- -#}
    {%- if item.RANGE == 'MSISDN' -%}
        MSISDN="{{item.MSISDN}}",
    {%- endif -%}
    {#- --- 条件必选：RANGE=IMSI 时必选 --- -#}
    {%- if item.RANGE == 'IMSI' -%}
        IMSI="{{item.IMSI}}",
    {%- endif -%}
    {#- --- 条件必选：RANGE=POD 时必选 --- -#}
    {%- if item.RANGE == 'POD' -%}
        PODNAME="{{item.PODNAME}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 该命令可基于用户（IMSI、MSISDN）强制产生话单。

#### 1.2 配置在线计费CCFH处理时是否强制产生话单，以及强制产生话单时话单中charging characteristic字段的取值、R6版本的eG-CDR是否支持CCFH处理。

```jinja2
{%- for item in set_ofccdrpara_list -%}
    SET OFCCDRPARA:
    {#- --- 可选参数 --- -#}
    {%- if item.CCFHCDRSW is not none -%}
        CCFHCDRSW={{item.CCFHCDRSW}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：CCFHCDRSW=ENABLE 时可选 --- -#}
    {%- if item.CCFHCDRSW == 'ENABLE' -%}
        {%- if item.CCFHCDRCC is not none -%}
            CCFHCDRCC="{{item.CCFHCDRCC}}",
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 2 配置话单缓存功能。

#### 2.1 配置锁定话单缓存目录。

```jinja2
{%- for item in set_cdrstrgstatus_list -%}
    SET CDRSTRGSTATUS:
    {#- --- 必选参数 --- -#}
    PODNAME="{{item.PODNAME}}",
    DIRECTORY={{item.DIRECTORY}},
    STATUS={{item.STATUS}},
    ;
{%- endfor -%}
```

#### 2.2 配置缓存话单的超期时间。

```jinja2
{%- for item in set_cdrstoragectrl_list -%}
    SET CDRSTORAGECTRL:
    {#- --- 可选参数 --- -#}
    {%- if item.CDREXPIREDAY is not none -%}
        CDREXPIREDAY={{item.CDREXPIREDAY}},
    {%- endif -%}
    {%- if item.CDREXPIREWEEK is not none -%}
        CDREXPIREWEEK={{item.CDREXPIREWEEK}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 当话单缓存的时间超过配置的超期时间时，系统会产生告警**ALM-81059 超期话单缓存**，提醒操作维护人员尽快处理话单。话单长期超期得不到处理，会导致用户计费信息丢失。

#### 2.3 配置解锁话单缓存目录。

```jinja2
{%- for item in set_cdrstrgstatus_list_3 -%}
    SET CDRSTRGSTATUS:
    {#- --- 必选参数 --- -#}
    DIRECTORY={{item.DIRECTORY}},
    PODNAME="{{item.PODNAME}}",
    STATUS={{item.STATUS}},
    ;
{%- endfor -%}
```


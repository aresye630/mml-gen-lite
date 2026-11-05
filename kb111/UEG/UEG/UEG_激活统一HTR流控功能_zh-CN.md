---
id: GWFD-021404
name: 激活统一HTR流控功能
ne_type: UEG
type: feature
description: 系统（MME）的周边网元存在过载风险时，微服务USN能够基于周边网元返回成功应答数的周期变化自动调节Attach、Inter-MME TAU、、Inter RAT Intra USN TAU、Inter RAT Intra USN RAU流程的处理速率。  适用于SGSN、MME。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝L","MEC 特性指南（风筝L）","MME特性指南","GWFD-021400 可靠性功能","GWFD-021404 周边网元过载保护","统一HTR流控功能","激活统一HTR流控功能"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
系统（MME）的周边网元存在过载风险时，微服务USN能够基于周边网元返回成功应答数的周期变化自动调节Attach、Inter-MME TAU、、Inter RAT Intra USN TAU、Inter RAT Intra USN RAU流程的处理速率。适用于SGSN、MME。

## 必备事项
前提条件

请仔细阅读统一HTR流控功能特性概述。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    set_emmproctrl_list:
      type: items
      properties:
        PROT:
          name: '流程类型'
          type: string
          enum:
          - AIR
          - ATTACH
          - AUTHENTICATION
          - CHECK_IMEI
          - CONTEXT_RESPONSE
          - INTER_TAU
          - LOCATION_UPDATE
          - PAGING
          - UPDATE_LOCATION
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ATTACHROAMRST:
          name: 'Attach拒绝原因值（漫游受限）'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ATTACHHTRFC:
          name: 'Attach拒绝原因值（统一HTR流控）'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: '设置S1模式移动性管理流程控制参数'
          data_source: '全网规划'
          pattern: ''
          default: ''
        INTERTAUHTRFC:
          name: 'Inter TAU拒绝原因值（统一HTR流控）'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_unihtr_list:
      type: items
      properties:
        OFFICESWITCH:
          name: '局向流控开关'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: '设置统一HTR功能'
          data_source: '全网规划'
          pattern: ''
          default: ''
        INITFCTHDPLCY:
          name: '流控速率配置策略'
          type: string
          enum:
          - DEFAULT
          - SPECIFIC
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        INITFCTHD:
          name: '初始启控速率'
          type: integer
          minimum: 200
          maximum: 1000000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MAXFCTHD:
          name: '最大流控速率'
          type: integer
          minimum: 200
          maximum: 1000000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SUCCPERCENT:
          name: '流控恢复阈值'
          type: integer
          minimum: 0
          maximum: 100
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_unihtr_list_1:
      type: items
      properties:
        OFFICESWITCH:
          name: '局向流控开关'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: '设置统一HTR功能'
          data_source: '全网规划'
          pattern: ''
          default: ''
        INITFCTHDPLCY:
          name: '流控速率配置策略'
          type: string
          enum:
          - DEFAULT
          - SPECIFIC
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        INITFCTHD:
          name: '初始启控速率'
          type: integer
          minimum: 200
          maximum: 1000000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MAXFCTHD:
          name: '最大流控速率'
          type: integer
          minimum: 200
          maximum: 1000000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SUCCPERCENT:
          name: '流控恢复阈值'
          type: integer
          minimum: 0
          maximum: 100
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_unihtr_list_2:
      type: items
      properties:
        OFFICESWITCH:
          name: '局向流控开关'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: '设置统一HTR功能'
          data_source: '全网规划'
          pattern: ''
          default: ''
        INITFCTHDPLCY:
          name: '流控速率配置策略'
          type: string
          enum:
          - DEFAULT
          - SPECIFIC
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        INITFCTHD:
          name: '初始启控速率'
          type: integer
          minimum: 200
          maximum: 1000000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MAXFCTHD:
          name: '最大流控速率'
          type: integer
          minimum: 200
          maximum: 1000000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SUCCPERCENT:
          name: '流控恢复阈值'
          type: integer
          minimum: 0
          maximum: 100
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    set_emmproctrl_list:
    - PROT: ATTACH
      ATTACHROAMRST: 10
      ATTACHHTRFC: 10
      INTERTAUHTRFC: 10
    set_unihtr_list:
    - OFFICESWITCH: ON
      INITFCTHDPLCY: SPECIFIC
      INITFCTHD: 400
      MAXFCTHD: 800
      SUCCPERCENT: 85
    set_unihtr_list_1:
    - OFFICESWITCH: ON
      INITFCTHDPLCY: SPECIFIC
      INITFCTHD: 400
      MAXFCTHD: 800
      SUCCPERCENT: 85
    set_unihtr_list_2:
    - OFFICESWITCH: ON
      INITFCTHDPLCY: SPECIFIC
      INITFCTHD: 400
      MAXFCTHD: 800
      SUCCPERCENT: 85
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 进入“MML命令行-UEG”窗口。

### 2 设置因开启统一HTR流控而导致Attach/Inter TAU流程失败时，下发给UE的原因值。

### ****SET EMMPROCTRL****

```jinja2
{%- for item in set_emmproctrl_list -%}
    SET EMMPROCTRL:
    {#- --- 必选参数 --- -#}
    PROT={{item.PROT}},
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：PROT=ATTACH 时可选 --- -#}
    {%- if item.PROT == 'ATTACH' -%}
        {%- if item.ATTACHROAMRST is not none -%}
            ATTACHROAMRST={{item.ATTACHROAMRST}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：PROT=INTER_TAU 时可选 --- -#}
    {%- if item.PROT == 'INTER_TAU' -%}
        {%- if item.INTERTAUHTRFC is not none -%}
            INTERTAUHTRFC={{item.INTERTAUHTRFC}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：PROT=ATTACH 时可选 --- -#}
    {%- if item.PROT == 'ATTACH' -%}
        {%- if item.ATTACHHTRFC is not none -%}
            ATTACHHTRFC={{item.ATTACHHTRFC}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 **可选：**计算初始启控速率。

### 启控速率的取值参照统一HTR流程功能实现原理页面。

### 4 打开局向流控开关，设置初始启控速率。

#### 4.1 如果“流控速率配置策略”为“DEFAULT（系统缺省值）”，则打开局向流控开关，不需要设置初始启控速率。

#### ****SET UNIHTR****

```jinja2
{%- if is_scenario_default_policy -%}
    {%- for item in set_unihtr_list -%}
        SET UNIHTR:
        {#- --- 可选参数 --- -#}
        {%- if item.OFFICESWITCH is not none -%}
            OFFICESWITCH={{item.OFFICESWITCH}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：INITFCTHDPLCY=SPECIFIC 时必选 --- -#}
        {%- if item.INITFCTHDPLCY == 'SPECIFIC' -%}
            INITFCTHD={{item.INITFCTHD}},
        {%- endif -%}
        {#- --- 条件必选：INITFCTHDPLCY=SPECIFIC 时必选 --- -#}
        {%- if item.INITFCTHDPLCY == 'SPECIFIC' -%}
            MAXFCTHD={{item.MAXFCTHD}},
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：OFFICESWITCH=ON 时可选 --- -#}
        {%- if item.OFFICESWITCH == 'ON' -%}
            {%- if item.INITFCTHDPLCY is not none -%}
                INITFCTHDPLCY={{item.INITFCTHDPLCY}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：OFFICESWITCH=ON 时可选 --- -#}
        {%- if item.OFFICESWITCH == 'ON' -%}
            {%- if item.SUCCPERCENT is not none -%}
                SUCCPERCENT={{item.SUCCPERCENT}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 4.2 如果“流控速率配置策略”为“SPECIFIC（自定义值）”，则按照3计算的值设置“初始启控速率”。

#### ****SET UNIHTR****

```jinja2
{%- if is_scenario_specific_policy -%}
    {%- for item in set_unihtr_list_1 -%}
        SET UNIHTR:
        {#- --- 可选参数 --- -#}
        {%- if item.OFFICESWITCH is not none -%}
            OFFICESWITCH={{item.OFFICESWITCH}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：INITFCTHDPLCY=SPECIFIC 时必选 --- -#}
        {%- if item.INITFCTHDPLCY == 'SPECIFIC' -%}
            INITFCTHD={{item.INITFCTHD}},
        {%- endif -%}
        {#- --- 条件必选：INITFCTHDPLCY=SPECIFIC 时必选 --- -#}
        {%- if item.INITFCTHDPLCY == 'SPECIFIC' -%}
            MAXFCTHD={{item.MAXFCTHD}},
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：OFFICESWITCH=ON 时可选 --- -#}
        {%- if item.OFFICESWITCH == 'ON' -%}
            {%- if item.INITFCTHDPLCY is not none -%}
                INITFCTHDPLCY={{item.INITFCTHDPLCY}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：OFFICESWITCH=ON 时可选 --- -#}
        {%- if item.OFFICESWITCH == 'ON' -%}
            {%- if item.SUCCPERCENT is not none -%}
                SUCCPERCENT={{item.SUCCPERCENT}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 当“流控速率配置策略”设置为“SPECIFIC（自定义值）”时，“最大流控速率”的配置原则为：

##### 4.2.1 “最大流控速率”取值要大于等于“初始启控速率”取值。“最大流控速率”一般设置为“初始启控速率”的两倍。

##### 4.2.2 当“最大流控速率”取值等于“初始启控速率”的取值时，统一HTR局向流控效果相当于固定速率流控功能。

### 5 设置初始启控速率后，系统自动调整用户接入速率，过程中用户实时判断是否需要调整初始启控速率。

#### 5.1 判断是否需要调整初始启控速率。

#### 当“初始启控速率”与现网的Attach、Inter TAU/RAU请求消息接入速率需求不一致时，需要调整初始启控速率。如现网需要更短的接入时长，则提高初始启控速率。

#### 是 => 5.c

#### 否 => 5.b

#### 5.2 观察性能指标判断是否有突发需流控的情况。

#### 观察性能指标15分钟后，如果S6a/S6d、S11/S4、SGs、S13/Gf接口负荷过高，DRA/HSS、SGW-C/PGW-C、MSC、DRA/EIR网元长时间拥塞，接入成功率极低为5%以下，可以适当调低接入速率；如果接入成功率保持100%，可以适当调高接入速率。

#### 是 => 5.c

#### 否 => 5.d

#### 5.3 计算并设置初始启控速率。

#### 计算方法参考3。****SET UNIHTR****执行后立即生效。

```jinja2
{%- for item in set_unihtr_list_2 -%}
    SET UNIHTR:
    {#- --- 可选参数 --- -#}
    {%- if item.OFFICESWITCH is not none -%}
        OFFICESWITCH={{item.OFFICESWITCH}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：INITFCTHDPLCY=SPECIFIC 时必选 --- -#}
    {%- if item.INITFCTHDPLCY == 'SPECIFIC' -%}
        INITFCTHD={{item.INITFCTHD}},
    {%- endif -%}
    {#- --- 条件必选：INITFCTHDPLCY=SPECIFIC 时必选 --- -#}
    {%- if item.INITFCTHDPLCY == 'SPECIFIC' -%}
        MAXFCTHD={{item.MAXFCTHD}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：OFFICESWITCH=ON 时可选 --- -#}
    {%- if item.OFFICESWITCH == 'ON' -%}
        {%- if item.INITFCTHDPLCY is not none -%}
            INITFCTHDPLCY={{item.INITFCTHDPLCY}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：OFFICESWITCH=ON 时可选 --- -#}
    {%- if item.OFFICESWITCH == 'ON' -%}
        {%- if item.SUCCPERCENT is not none -%}
            SUCCPERCENT={{item.SUCCPERCENT}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 5.4 系统基于设置的“初始启控速率”，自动调节Attach、Inter-MME TAU、Inter RAT Intra USN TAU、Inter RAT Intra USN RAU流程首条消息的接入速率。


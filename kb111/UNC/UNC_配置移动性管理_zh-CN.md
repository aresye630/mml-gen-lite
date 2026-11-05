---
id: ''
name: 配置移动性管理
ne_type: UNC
type: feature
description: 本操作指导介绍在运行网络中配置移动性管理特性的操作过程。  移动性管理功能EMM（EPS Mobility Management）用来控制UE（User Equipment）在LTE/EPC的接入及跟踪UE当前的位置信息，即UE当前所在的TA(Tracking Area)/TA List、当前所在的MME（Mobilit Management Entity）等信息。
risk_level: ''
doc_source: ["网络部署","初始配置","UNC初始配置与调测","组网对接配置","配置AMF&MME&SGSN","配置MME","配置移动性管理"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本操作指导介绍在运行网络中配置移动性管理特性的操作过程。移动性管理功能EMM（EPS Mobility Management）用来控制UE（User Equipment）在LTE/EPC的接入及跟踪UE当前的位置信息，即UE当前所在的TA(Tracking Area)/TA List、当前所在的MME（Mobilit Management Entity）等信息。

## 必备事项
前提条件

* 具备管理员权限的操作人员已经登录华为操作维护系统（登录U2020客户端或登录OM Portal）。

* UNC软件安装已完成。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    set_emm_list:
      type: items
      properties:
        T3422:
          name: 'T3422（s）'
          type: integer
          minimum: 3
          maximum: 12
          required: false
          description: '此命令中的所有参数均有系统初始值，如果用户使用初始值，就不必执行此命令  当使用NB-IoT业务时，需通过****SET NBEMM****来配置移动性管理。'
          data_source: '参见“水平网设LLD文档 ”。'
          pattern: ''
          default: ''
        N3422:
          name: 'N3422（times）'
          type: integer
          minimum: 0
          maximum: 5
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        T3450:
          name: 'T3450（s）'
          type: integer
          minimum: 3
          maximum: 12
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        N3450:
          name: 'N3450（times）'
          type: integer
          minimum: 0
          maximum: 5
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        T3460:
          name: 'T3460（s）'
          type: integer
          minimum: 3
          maximum: 12
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        N3460:
          name: 'N3460（times）'
          type: integer
          minimum: 0
          maximum: 5
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        T3470:
          name: 'T3470（s）'
          type: integer
          minimum: 3
          maximum: 12
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        N3470:
          name: 'N3470（times）'
          type: integer
          minimum: 0
          maximum: 5
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        T3412:
          name: 'T3412（min）'
          type: integer
          minimum: 1
          maximum: 186
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        T3402:
          name: 'T3402（min）'
          type: integer
          minimum: 1
          maximum: 186
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        T3413:
          name: 'T3413（s）'
          type: integer
          minimum: 3
          maximum: 12
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        N3413:
          name: 'N3413（times）'
          type: integer
          minimum: 0
          maximum: 5
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PAGINGDELTA:
          name: '重寻呼间隔递增值（s）'
          type: integer
          minimum: 0
          maximum: 20
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RCHTMR:
          name: '移动可达定时器（min）'
          type: integer
          minimum: 2
          maximum: 198
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GUTITMR:
          name: 'GUTI重分配定时器（h）'
          type: integer
          minimum: 0
          maximum: 24
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GUTIREALLOC:
          name: 'Attach或TAU中重分配GUTI'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        HOPRETMR:
          name: 'Handover准备定时器（s）'
          type: integer
          minimum: 5
          maximum: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        HOCMPSRCTMR:
          name: '源侧Handover完成定时器（s）'
          type: integer
          minimum: 5
          maximum: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        HOCMPTGTTMR:
          name: '目标侧Handover完成定时器（s）'
          type: integer
          minimum: 5
          maximum: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        T3:
          name: 'T3定时器（s）'
          type: integer
          minimum: 3
          maximum: 60
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_talst_list:
      type: items
      properties:
        TALISTID:
          name: 'TA List标号'
          type: integer
          minimum: 0
          maximum: 65534
          required: true
          description: '增加跟踪区域码列表。'
          data_source: ''
          pattern: ''
          default: ''
        TAI:
          name: 'TAI'
          type: string
          maxLength: 10
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    set_emm_list:
    - T3422: 6
      N3422: 4
      T3450: 6
      N3450: 4
      T3460: 6
      N3460: 4
      T3470: 6
      N3470: 4
      T3412: 54
      T3402: 12
      T3413: 6
      N3413: 2
      PAGINGDELTA: 0
      RCHTMR: 58
      GUTITMR: 0
      GUTIREALLOC: YES
      HOPRETMR: 10
      HOCMPSRCTMR: 10
      HOCMPTGTTMR: 10
      T3: 10
    add_talst_list:
    - TALISTID: 1
      TAI: '4600100010'
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 进入“MML命令行-UNC”窗口。

### 2 **可选：**设置移动性管理EMM（EPS Mobility Management）参数。

```jinja2
{%- if is_optional_set_emm_parameters -%}
    {%- for item in set_emm_list -%}
        SET EMM:
        {#- --- 可选参数 --- -#}
        {%- if item.T3422 is not none -%}
            T3422={{item.T3422}},
        {%- endif -%}
        {%- if item.N3422 is not none -%}
            N3422={{item.N3422}},
        {%- endif -%}
        {%- if item.T3450 is not none -%}
            T3450={{item.T3450}},
        {%- endif -%}
        {%- if item.N3450 is not none -%}
            N3450={{item.N3450}},
        {%- endif -%}
        {%- if item.T3460 is not none -%}
            T3460={{item.T3460}},
        {%- endif -%}
        {%- if item.N3460 is not none -%}
            N3460={{item.N3460}},
        {%- endif -%}
        {%- if item.T3470 is not none -%}
            T3470={{item.T3470}},
        {%- endif -%}
        {%- if item.N3470 is not none -%}
            N3470={{item.N3470}},
        {%- endif -%}
        {%- if item.T3412 is not none -%}
            T3412={{item.T3412}},
        {%- endif -%}
        {%- if item.T3402 is not none -%}
            T3402={{item.T3402}},
        {%- endif -%}
        {%- if item.T3413 is not none -%}
            T3413={{item.T3413}},
        {%- endif -%}
        {%- if item.N3413 is not none -%}
            N3413={{item.N3413}},
        {%- endif -%}
        {%- if item.PAGINGDELTA is not none -%}
            PAGINGDELTA={{item.PAGINGDELTA}},
        {%- endif -%}
        {%- if item.RCHTMR is not none -%}
            RCHTMR={{item.RCHTMR}},
        {%- endif -%}
        {%- if item.GUTITMR is not none -%}
            GUTITMR={{item.GUTITMR}},
        {%- endif -%}
        {%- if item.GUTIREALLOC is not none -%}
            GUTIREALLOC={{item.GUTIREALLOC}},
        {%- endif -%}
        {%- if item.HOPRETMR is not none -%}
            HOPRETMR={{item.HOPRETMR}},
        {%- endif -%}
        {%- if item.HOCMPSRCTMR is not none -%}
            HOCMPSRCTMR={{item.HOCMPSRCTMR}},
        {%- endif -%}
        {%- if item.HOCMPTGTTMR is not none -%}
            HOCMPTGTTMR={{item.HOCMPTGTTMR}},
        {%- endif -%}
        {%- if item.T3 is not none -%}
            T3={{item.T3}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 3 增加跟踪区域码列表。

```jinja2
{%- for item in add_talst_list -%}
    ADD TALST:
    {#- --- 必选参数 --- -#}
    TALISTID={{item.TALISTID}},
    TAI="{{item.TAI}}",
    ;
{%- endfor -%}
```


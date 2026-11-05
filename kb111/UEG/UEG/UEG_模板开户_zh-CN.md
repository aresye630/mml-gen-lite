---
id: ''
name: 模板开户
ne_type: UEG
type: feature
description: 该操作指导工程师在开局阶段，新建UDM网元时，完成5G模板开户数据的配置。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝L","UEG UDM用户管理（风筝L）","用户数据配置（5G SA网络）","5G用户开户配置","模板开户"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
该操作指导工程师在开局阶段，新建UDM网元时，完成5G模板开户数据的配置。

## 必备事项
前提条件

前提条件

* 已经完成UDM的CSP OM Portal侧基础数据的配置。

* 已完成5G用户数据配置。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    add_smdatatpl_list:
      type: items
      properties:
        HLRSN:
          name: 'HLR序列号'
          type: integer
          minimum: 1
          maximum: 255
          required: true
          description: '该参数的取值需要与系统管理MML命令界面上的**ADD VHLRSN**命令配置的“HLRSN”的取值一一对应。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        TPLID:
          name: '模板ID'
          type: integer
          minimum: 1
          maximum: 2147483646
          required: true
          description: '统一规划。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SNSSAI:
          name: '切片标识'
          type: string
          minLength: 1
          maxLength: 10
          required: true
          description: '标识5G系统中的网络切片。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        DEFSNSSAI:
          name: '是否默认S-NSSAI'
          type: string
          enum:
          - TRUE
          - FALSE
          required: true
          description: '统一规划。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        DNN:
          name: '数据网名称'
          type: string
          maxLength: 64
          required: true
          description: '数据网名称，需与UNC侧配置一致。从UNC侧获取进行配置。'
          data_source: '与对端协商'
          pattern: ''
          default: ''
        DNNQOSTPLID:
          name: '5GS DNNQOS模板ID'
          type: integer
          minimum: 1
          maximum: 2147483646
          required: true
          description: '该参数必须先由**ADD DNNQOSTPL**命令定义，然后才能在此处引用。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_ngsusertpl_list:
      type: items
      properties:
        HLRSN:
          name: 'HLR序列号'
          type: integer
          minimum: 1
          maximum: 255
          required: true
          description: '与**ADD SMDATATPL**中的“HLRSN(HLR序列号)”保持一致。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        TPLID:
          name: '模板ID'
          type: integer
          minimum: 1
          maximum: 2147483646
          required: true
          description: '统一规划。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        AMBRUP:
          name: 'UE级别上行速率'
          type: integer
          minimum: 1
          maximum: 9223372036854775807
          required: true
          description: '统一规划。  表示5G网络UE级别上行带宽，需与UNC侧配置一致。从UNC侧获取进行配置。'
          data_source: '与对端协商'
          pattern: ''
          default: ''
        UPUNIT:
          name: 'UE级别上行速率单位'
          type: string
          enum:
          - bps
          - Kbps
          - Mbps
          - Gbps
          - Tbps
          required: true
          description: '-'
          data_source: '与对端协商'
          pattern: ''
          default: bps
        AMBRDW:
          name: 'UE级别下行速率'
          type: integer
          minimum: 1
          maximum: 9223372036854775807
          required: true
          description: '统一规划。  表示5GUE级别下行带宽，需与UNC侧配置一致。从UNC侧获取进行配置。'
          data_source: '与对端协商'
          pattern: ''
          default: ''
        DWUNIT:
          name: 'UE级别下行速率单位'
          type: string
          enum:
          - bps
          - Kbps
          - Mbps
          - Gbps
          - Tbps
          required: true
          description: '-'
          data_source: '与对端协商'
          pattern: ''
          default: bps
        FORBIDTPLID:
          name: '禁止区域模板ID'
          type: integer
          minimum: 1
          maximum: 2147483646
          required: false
          description: '该参数必须先由**ADD FORBIDAREATPL**命令定义，然后才能在此处引用。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        SERAREATPLID:
          name: '业务区域限制模板ID'
          type: integer
          minimum: 1
          maximum: 2147483646
          required: false
          description: '该参数必须先由**ADD SERAREATPL**命令定义，然后才能在此处引用。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        AUTHTYPE:
          name: '鉴权方式'
          type: string
          enum:
          - EAP-AKA'
          - 5G-AKA
          required: false
          description: '选择5G-AKA鉴权方式。需要与UE保持一致。'
          data_source: '本端规划'
          pattern: ''
          default: 5G-AKA
        MICOALLOWED:
          name: '是否支持MICO模式'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: '统一规划。'
          data_source: '本端规划'
          pattern: ''
          default: FALSE
        SMDATATPLID:
          name: '会话信息模板ID'
          type: integer
          minimum: 1
          maximum: 2147483646
          required: false
          description: '该参数必须先由**ADD SMDATATPL**命令定义，然后才能在此处引用。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_tplsub_list:
      type: items
      properties:
        HLRSN:
          name: 'HLR序列号'
          type: string
          required: false
          description: '与**ADD SMDATATPL**中的“HLRSN(HLR序列号)”保持一致。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        IMSI:
          name: 'IMSI'
          type: string
          required: false
          description: '与UE卡数据一致。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        ISDN:
          name: 'MSISDN'
          type: string
          required: false
          description: '与UE卡数据一致。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        TPLTYPE:
          name: '模板类型'
          type: string
          required: false
          description: '统一规划。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        NGSUSERTPLID:
          name: '5G用户模板ID'
          type: string
          required: false
          description: '统一规划。'
          data_source: '本端规划'
          pattern: ''
          default: ''
  examples:
    add_smdatatpl_list:
    - HLRSN: 1
      TPLID: 1
      SNSSAI: '1-D143A5'
      DEFSNSSAI: TRUE
      DNN: 'huawei.com'
      DNNQOSTPLID: 1
    add_ngsusertpl_list:
    - HLRSN: 1
      TPLID: 1
      AMBRUP: 200
      UPUNIT: bps
      AMBRDW: 500
      DWUNIT: bps
      FORBIDTPLID: 1
      SERAREATPLID: 99
      AUTHTYPE: 5G-AKA
      MICOALLOWED: FALSE
      SMDATATPLID: 1
    add_tplsub_list:
    - HLRSN: '1'
      IMSI: '460031200100003'
      ISDN: '86111111113'
      TPLTYPE: EPS_SEPARATE
      NGSUSERTPLID: '1'
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 登录“UDM业务管理”窗口。

### 2 执行**ADD SMDATATPL**命令，增加5G会话信息模板数据记录。

```jinja2
{%- for item in add_smdatatpl_list -%}
    ADD SMDATATPL:
    {#- --- 必选参数 --- -#}
    DEFSNSSAI={{item.DEFSNSSAI}},
    DNN="{{item.DNN}}",
    SNSSAI="{{item.SNSSAI}}",
    HLRSN={{item.HLRSN}},
    DNNQOSTPLID={{item.DNNQOSTPLID}},
    TPLID={{item.TPLID}},
    ;
{%- endfor -%}
```

### 3 执行**ADD NGSUSERTPL**命令，增加5GS用户模板数据记录。

```jinja2
{%- for item in add_ngsusertpl_list -%}
    ADD NGSUSERTPL:
    {#- --- 必选参数 --- -#}
    AMBRDW={{item.AMBRDW}},
    DWUNIT={{item.DWUNIT}},
    HLRSN={{item.HLRSN}},
    AMBRUP={{item.AMBRUP}},
    TPLID={{item.TPLID}},
    UPUNIT={{item.UPUNIT}},
    {#- --- 可选参数 --- -#}
    {%- if item.SMDATATPLID is not none -%}
        SMDATATPLID={{item.SMDATATPLID}},
    {%- endif -%}
    {%- if item.FORBIDTPLID is not none -%}
        FORBIDTPLID={{item.FORBIDTPLID}},
    {%- endif -%}
    {%- if item.MICOALLOWED is not none -%}
        MICOALLOWED={{item.MICOALLOWED}},
    {%- endif -%}
    {%- if item.SERAREATPLID is not none -%}
        SERAREATPLID={{item.SERAREATPLID}},
    {%- endif -%}
    {%- if item.AUTHTYPE is not none -%}
        AUTHTYPE={{item.AUTHTYPE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 执行**ADD TPLSUB**命令，为用户模板开户。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_tplsub_list的变量区（command: ADD TPLSUB） -#}
<!-- MISSING_MACRO: command=ADD TPLSUB list_name=add_tplsub_list step_id=4 -->
```

### 还可以通过**ADD TPLUSCSUB**或者**ADD SCARD**命令为用户进行模板开户。


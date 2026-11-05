---
id: ''
name: 激活用户身份保密性功能（适用于2G&3G）
ne_type: UNC
type: feature
description: 本操作指导介绍在运行网络中激活用户身份保密性功能的操作过程。  用户身份保密功能是UNC的基本功能，通过给用户分配分组域临时用户标识P-TMSI，减少在空口上直接使用IMSI，来为用户身份提供保密性措施，防止用户身份泄密。  适用于SGSN。
risk_level: ''
doc_source: ["网络部署","安全配置","UNC安全配置","安全配置建议","必选配置","业务安全配置","激活用户身份保密性功能（适用于2G&3G）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本操作指导介绍在运行网络中激活用户身份保密性功能的操作过程。用户身份保密功能是UNC的基本功能，通过给用户分配分组域临时用户标识P-TMSI，减少在空口上直接使用IMSI，来为用户身份提供保密性措施，防止用户身份泄密。适用于SGSN。

## 必备事项
前提条件

请仔细阅读WSFD-010302 用户身份保密性功能（适用于SGSN）特性概述。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    set_gmmptmsirealloc_list:
      type: items
      properties: {}
    set_pmmptmsirealloc_list:
      type: items
      properties:
        WITHRAUPROC:
          name: '伴随RAU流程分配'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        REALLOCTMR:
          name: 'P-TMSI重分配流程间隔时长（小时）'
          type: integer
          minimum: 0
          maximum: 24
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        REALLOCCOND:
          name: 'P-TMSI重分配流程发起条件'
          type: string
          enum:
          - AFTER_PTMSI_ALLOC
          - IN_PMM_CONNECTED_STATE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    set_gmmptmsirealloc_list:
    - {}
    set_pmmptmsirealloc_list:
    - WITHRAUPROC: YES
      REALLOCTMR: 1
      REALLOCCOND: IN_PMM_CONNECTED_STATE
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 进入“MML命令行-UNC”窗口。

### 2 设置GSM移动性管理功能参数。

#### 2.1 开启P-TMSI重分配功能。

```jinja2
SET GMMPTMSIREALLOC:
;
```

#### 参数“REALLOCTMR”用于设定P-TMSI重分配流程的间隔时间长。如果配置为0时，PTMSI重分配功能关闭；配置为其他取值时，PTMSI重分配功能开启。

### 3 设置UMTS移动性管理功能参数。

#### 3.1 开启P-TMSI重分配功能。

```jinja2
{%- for item in set_pmmptmsirealloc_list -%}
    SET PMMPTMSIREALLOC:
    {#- --- 可选参数 --- -#}
    {%- if item.WITHRAUPROC is not none -%}
        WITHRAUPROC={{item.WITHRAUPROC}},
    {%- endif -%}
    {%- if item.REALLOCTMR is not none -%}
        REALLOCTMR={{item.REALLOCTMR}},
    {%- endif -%}
    {%- if item.REALLOCCOND is not none -%}
        REALLOCCOND={{item.REALLOCCOND}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 参数“REALLOCTMR”用于设定P-TMSI重分配流程的间隔时间长。如果配置为0时，PTMSI重分配功能关闭；配置为其他取值时，PTMSI重分配功能开启。


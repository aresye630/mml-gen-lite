---
id: ''
name: 激活AMF Pool 用户迁移特性
ne_type: UNC
type: feature
description: 本操作指导介绍在运行网络中激活AMF Pool用户迁移特性的操作过程。  AMF Pool用户迁移特性是指根据AMF Pool内各AMF的负载情况，操作人员通过下发启动迁移命令，将负载过高或需要升级的AMF上的用户迁移到AMF Pool中的其他AMF上，从而实现实时、动态地调整AMF Pool内的负荷分布。  适用于AMF。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","容灾功能","WSFD-104302 AMF Pool用户迁移","激活AMF Pool 用户迁移特性"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本操作指导介绍在运行网络中激活AMF Pool用户迁移特性的操作过程。AMF Pool用户迁移特性是指根据AMF Pool内各AMF的负载情况，操作人员通过下发启动迁移命令，将负载过高或需要升级的AMF上的用户迁移到AMF Pool中的其他AMF上，从而实现实时、动态地调整AMF Pool内的负荷分布。适用于AMF。

## 必备事项
前提条件

* 请仔细阅读WSFD-104302 AMF Pool用户迁移特性概述。
* 完成加载License。
* 完成激活AMF Pool特性。
* 需要对端网元gNodeB支持AMF Pool用户迁移特性。
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
    str_offloadamf_list:
      type: items
      properties:
        TYPE:
          name: '迁移类型'
          type: string
          enum:
          - ALL
          - PART
          - RATE
          - IMSI
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ALL
        IMSI:
          name: 'IMSI'
          type: string
          minLength: 5
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        OFFLOADNUM:
          name: '迁移总数'
          type: integer
          minimum: 0
          maximum: 17000000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        OFFLOADRATE:
          name: '迁移比率(百分比)'
          type: integer
          minimum: 1
          maximum: 100
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PRIMIGCONUSER:
          name: '优先迁移连接态用户开关'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RATE:
          name: '迁移速率(千/分钟)'
          type: integer
          minimum: 1
          maximum: 500
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    str_offloadamf_list_1:
      type: items
      properties: {}
    str_offloadamf_list_2:
      type: items
      properties:
        TYPE:
          name: '迁移类型'
          type: string
          enum:
          - ALL
          - PART
          - RATE
          - IMSI
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ALL
        OFFLOADRATE:
          name: '迁移比率(百分比)'
          type: integer
          minimum: 1
          maximum: 100
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IMSI:
          name: 'IMSI'
          type: string
          minLength: 5
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        OFFLOADNUM:
          name: '迁移总数'
          type: integer
          minimum: 0
          maximum: 17000000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PRIMIGCONUSER:
          name: '优先迁移连接态用户开关'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RATE:
          name: '迁移速率(千/分钟)'
          type: integer
          minimum: 1
          maximum: 500
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    str_offloadamf_list_3:
      type: items
      properties: {}
    str_offloadamf_list_4:
      type: items
      properties:
        TYPE:
          name: '迁移类型'
          type: string
          enum:
          - ALL
          - PART
          - RATE
          - IMSI
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ALL
        IMSI:
          name: 'IMSI'
          type: string
          minLength: 5
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TAMF:
          name: '目标AMF名称'
          type: string
          minLength: 0
          maxLength: 150
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        OFFLOADNUM:
          name: '迁移总数'
          type: integer
          minimum: 0
          maximum: 17000000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        OFFLOADRATE:
          name: '迁移比率(百分比)'
          type: integer
          minimum: 1
          maximum: 100
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PRIMIGCONUSER:
          name: '优先迁移连接态用户开关'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RATE:
          name: '迁移速率(千/分钟)'
          type: integer
          minimum: 1
          maximum: 500
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV2SMAP01'
      SWITCH: ENABLE
    str_offloadamf_list:
    - TYPE: ALL
      IMSI: ''
      OFFLOADNUM: ''
      OFFLOADRATE: ''
      PRIMIGCONUSER: ''
      RATE: ''
    str_offloadamf_list_1:
    - {}
    str_offloadamf_list_2:
    - TYPE: RATE
      OFFLOADRATE: 10
      IMSI: ''
      OFFLOADNUM: ''
      PRIMIGCONUSER: ''
      RATE: ''
    str_offloadamf_list_3:
    - {}
    str_offloadamf_list_4:
    - TYPE: IMSI
      IMSI: '123037301000001'
      TAMF: 'AMF2'
      OFFLOADNUM: ''
      OFFLOADRATE: ''
      PRIMIGCONUSER: ''
      RATE: ''
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 配置特性开关以及迁移配置参数。

#### 1.1 进入“MML命令行-UNC”窗口。

#### 1.2 打开本特性的License配置开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

### 2 配置迁移任务

#### 2.1 启动用户迁移任务。

##### 2.1.1 迁移全部用户

```jinja2
{%- if is_scenario_migrate_all_users -%}
    {%- for item in str_offloadamf_list -%}
        STR OFFLOADAMF:
        {#- --- 可选参数 --- -#}
        {%- if item.TYPE is not none -%}
            TYPE={{item.TYPE}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：TYPE=IMSI 时必选 --- -#}
        {%- if item.TYPE == 'IMSI' -%}
            IMSI="{{item.IMSI}}",
        {%- endif -%}
        {#- --- 条件必选：TYPE=PART 时必选 --- -#}
        {%- if item.TYPE == 'PART' -%}
            OFFLOADNUM={{item.OFFLOADNUM}},
        {%- endif -%}
        {#- --- 条件必选：TYPE=RATE 时必选 --- -#}
        {%- if item.TYPE == 'RATE' -%}
            OFFLOADRATE={{item.OFFLOADRATE}},
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：TYPE=ALL/RATE/PART 时可选 --- -#}
        {%- if item.TYPE in ['ALL', 'RATE', 'PART'] -%}
            {%- if item.PRIMIGCONUSER is not none -%}
                PRIMIGCONUSER={{item.PRIMIGCONUSER}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：TYPE=ALL/RATE/PART 时可选 --- -#}
        {%- if item.TYPE in ['ALL', 'RATE', 'PART'] -%}
            {%- if item.RATE is not none -%}
                RATE={{item.RATE}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 2.1.2 迁移部分用户

```jinja2
{%- if is_scenario_migrate_partial_users -%}
    STR OFFLOADAMF:
    ;
{%- endif -%}
```

##### 2.1.3 迁移百分比用户

```jinja2
{%- if is_scenario_migrate_percentage_users -%}
    {%- for item in str_offloadamf_list_2 -%}
        STR OFFLOADAMF:
        {#- --- 可选参数 --- -#}
        {%- if item.TYPE is not none -%}
            TYPE={{item.TYPE}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：TYPE=RATE 时必选 --- -#}
        {%- if item.TYPE == 'RATE' -%}
            OFFLOADRATE={{item.OFFLOADRATE}},
        {%- endif -%}
        {#- --- 条件必选：TYPE=IMSI 时必选 --- -#}
        {%- if item.TYPE == 'IMSI' -%}
            IMSI="{{item.IMSI}}",
        {%- endif -%}
        {#- --- 条件必选：TYPE=PART 时必选 --- -#}
        {%- if item.TYPE == 'PART' -%}
            OFFLOADNUM={{item.OFFLOADNUM}},
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：TYPE=ALL/RATE/PART 时可选 --- -#}
        {%- if item.TYPE in ['ALL', 'RATE', 'PART'] -%}
            {%- if item.PRIMIGCONUSER is not none -%}
                PRIMIGCONUSER={{item.PRIMIGCONUSER}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：TYPE=ALL/RATE/PART 时可选 --- -#}
        {%- if item.TYPE in ['ALL', 'RATE', 'PART'] -%}
            {%- if item.RATE is not none -%}
                RATE={{item.RATE}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 2.1.4 按IMSI迁移单个用户

```jinja2
{%- if is_scenario_migrate_by_imsi -%}
    STR OFFLOADAMF:
    ;
{%- endif -%}
```

### 3 配置按指定IMSI的单个用户至指定目标AMF的迁移类型

#### 3.1 查询目标AMF名称。

#### 3.2 在原AMF上配置指定IMSI的单个用户至指定目标AMF的迁移参数，迁移单个用户。

```jinja2
{%- if is_scenario_migrate_by_imsi -%}
    {%- for item in str_offloadamf_list_4 -%}
        STR OFFLOADAMF:
        {#- --- 可选参数 --- -#}
        {%- if item.TYPE is not none -%}
            TYPE={{item.TYPE}},
        {%- endif -%}
        {%- if item.TAMF is not none -%}
            TAMF="{{item.TAMF}}",
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：TYPE=IMSI 时必选 --- -#}
        {%- if item.TYPE == 'IMSI' -%}
            IMSI="{{item.IMSI}}",
        {%- endif -%}
        {#- --- 条件必选：TYPE=PART 时必选 --- -#}
        {%- if item.TYPE == 'PART' -%}
            OFFLOADNUM={{item.OFFLOADNUM}},
        {%- endif -%}
        {#- --- 条件必选：TYPE=RATE 时必选 --- -#}
        {%- if item.TYPE == 'RATE' -%}
            OFFLOADRATE={{item.OFFLOADRATE}},
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：TYPE=ALL/RATE/PART 时可选 --- -#}
        {%- if item.TYPE in ['ALL', 'RATE', 'PART'] -%}
            {%- if item.PRIMIGCONUSER is not none -%}
                PRIMIGCONUSER={{item.PRIMIGCONUSER}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：TYPE=ALL/RATE/PART 时可选 --- -#}
        {%- if item.TYPE in ['ALL', 'RATE', 'PART'] -%}
            {%- if item.RATE is not none -%}
                RATE={{item.RATE}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```


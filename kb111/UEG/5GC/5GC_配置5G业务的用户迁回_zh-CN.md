---
id: ''
name: 配置5G业务的用户迁回
ne_type: UEG
type: feature
description: 子园区UEG-L故障恢复后必须要尽快在总部园区UEG-L上将故障期间激活的用户回迁至子园区UEG-L，本章节介绍5G用户的迁回操作。  * 本页面中的命令均为高危命令，请在华为工程师指导下执行。否则可能导致业务受损。 * 如果多个子园区UEG-L同时故障，由于接入总部园区UEG-L的用户容量受限，因此可能导致故障子园区的新用户接入总部园区UEG-L失败。 * 如果多个子园区UEG-L同时故障，建议子园区UEG-L均恢复后，再进行用户迁回操作。 * 在总部园区UEG-L上将在线用户去激活后，用户业务发生中断，业务重新在子园区UEG-L上恢复的时间取决于终端业务行为。
tags: []
risk_level: ''
doc_source: ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（风筝多园区，入驻式）","风筝L+L多园区方案（跨级容灾，仅适用于海外）","子园区UEG-L故障恢复后配置","配置5G业务的用户迁回"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
子园区UEG-L故障恢复后必须要尽快在总部园区UEG-L上将故障期间激活的用户回迁至子园区UEG-L，本章节介绍5G用户的迁回操作。* 本页面中的命令均为高危命令，请在华为工程师指导下执行。否则可能导致业务受损。* 如果多个子园区UEG-L同时故障，由于接入总部园区UEG-L的用户容量受限，因此可能导致故障子园区的新用户接入总部园区UEG-L失败。* 如果多个子园区UEG-L同时故障，建议子园区UEG-L均恢复后，再进行用户迁回操作。* 在总部园区UEG-L上将在线用户去激活后，用户业务发生中断，业务重新在子园区UEG-L上恢复的时间取决于终端业务行为。

## 必备事项
前提条件

两套UEG-L已完成跨级容灾模式配置。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    mod_amfinfo_list:
      type: items
      properties:
        AMFINSTANCENAME:
          name: 'AMF实例名称'
          type: string
          minLength: 0
          maxLength: 50
          required: true
          description: 'AMF实例名称，通过**LST AMFINFO**查询。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        CAPACITY:
          name: '相对容量'
          type: integer
          minimum: 0
          maximum: 255
          required: false
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: ''
    mod_cpnfprofile_list:
      type: items
      properties:
        NFINSTANCENAME:
          name: 'NF实例名称'
          type: string
          minLength: 0
          maxLength: 50
          required: true
          description: 'AMF实例名称，通过**LST CPNFPROFILE**查询。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        CAPACITY:
          name: '容量'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: ''
    str_offloadbyedgeamf_list:
      type: items
      properties:
        OFFLOADTYPE:
          name: '迁移类型'
          type: string
          enum:
          - RATE
          - TAIRANGE
          - IMSI
          required: true
          description: '总部园区用户全部迁移到子园区。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        TACSTART:
          name: 'TAC起始号段'
          type: string
          minLength: 6
          maxLength: 6
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        AMFPOINTER:
          name: '目标AMF指示符'
          type: string
          minLength: 2
          maxLength: 2
          required: true
          description: '目标AMF指示符，通过**LST GUAMI**查询。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        OFFLOADRATE:
          name: '迁移比例'
          type: integer
          minimum: 1
          maximum: 100
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
    str_offloadbyedgeamf_list_1:
      type: items
      properties:
        OFFLOADTYPE:
          name: '迁移类型'
          type: string
          enum:
          - RATE
          - TAIRANGE
          - IMSI
          required: true
          description: '故障子园区签约用户的号段范围。通过**LST UPAREABINDN2TAI**查询。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        OFFLOADRATE:
          name: '迁移比例'
          type: integer
          minimum: 1
          maximum: 100
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
        TACEND:
          name: 'TAC终止号段'
          type: string
          minLength: 6
          maxLength: 6
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        AMFPOINTER:
          name: '目标AMF指示符'
          type: string
          minLength: 2
          maxLength: 2
          required: true
          description: '目标AMF指示符，通过**LST GUAMI**查询。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        TACSTART:
          name: 'TAC起始号段'
          type: string
          minLength: 6
          maxLength: 6
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    mod_amfinfo_list_1:
      type: items
      properties:
        AMFINSTANCENAME:
          name: 'AMF实例名称'
          type: string
          minLength: 0
          maxLength: 50
          required: true
          description: 'AMF实例名称，通过**LST AMFINFO**查询。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        CAPACITY:
          name: '相对容量'
          type: integer
          minimum: 0
          maximum: 255
          required: false
          description: '-'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    mod_cpnfprofile_list_1:
      type: items
      properties:
        NFINSTANCENAME:
          name: 'NF实例名称'
          type: string
          minLength: 0
          maxLength: 50
          required: true
          description: 'AMF实例名称，通过**LST CPNFPROFILE**查询。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        CAPACITY:
          name: '容量'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: '-'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
  examples:
    mod_amfinfo_list:
    - AMFINSTANCENAME: 'AMF实例名称'
      CAPACITY: 1
    mod_cpnfprofile_list:
    - NFINSTANCENAME: 'AMF实例名称'
      CAPACITY: 0
    str_offloadbyedgeamf_list:
    - OFFLOADTYPE: RATE
      TACSTART: '100'
      AMFPOINTER: '子园区UEG的AMF指示符'
      OFFLOADRATE: 100
    str_offloadbyedgeamf_list_1:
    - OFFLOADTYPE: TAIRANGE
      OFFLOADRATE: 12301000003
      TACEND: '12301000004'
      AMFPOINTER: '子园区UEG的AMF指示符'
      TACSTART: '12301000003'
    mod_amfinfo_list_1:
    - AMFINSTANCENAME: 'AMF实例名称'
      CAPACITY: 相对容量
    mod_cpnfprofile_list_1:
    - NFINSTANCENAME: 'AMF实例名称'
      CAPACITY: 容量
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 进入子园区的UEG-L“MML命令行-UEG”窗口。

### 2 执行**LST GUAMI**查询并记录“AMF指示符”。

### 3 进入总部园区的UEG-L“MML命令行-UEG”窗口。

### 4 执行以下命令，查询并记录相关参数。

#### 4.1 //查询并记录参数“相对容量”和“AMF实例名称”

#### 4.2 //查询并记录“NF类型”为“NfAMF”的参数“容量”和“NF实例名称”

### 5 修改AMF的“相对容量”，建议修改为1。

```jinja2
{%- for item in mod_amfinfo_list -%}
    MOD AMFINFO:
    {#- --- 必选参数 --- -#}
    AMFINSTANCENAME="{{item.AMFINSTANCENAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.CAPACITY is not none -%}
        CAPACITY={{item.CAPACITY}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 6 修改AMF的“容量”，建议修改为0。

```jinja2
{%- for item in mod_cpnfprofile_list -%}
    MOD CPNFPROFILE:
    {#- --- 必选参数 --- -#}
    NFINSTANCENAME="{{item.NFINSTANCENAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.CAPACITY is not none -%}
        CAPACITY={{item.CAPACITY}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 7 如果仅一个子园区故障，且该园区已恢复，下发启动迁移命令，向子园区的AMF迁移100%用户。其中“AMFPOINTER”是在子园区的UEG设备执行**LST GUAMI**查询到的“AMF指示符”。

```jinja2
{%- if is_scenario_single_park_fault -%}
    {%- for item in str_offloadbyedgeamf_list -%}
        STR OFFLOADBYEDGEAMF:
        {#- --- 必选参数 --- -#}
        OFFLOADTYPE={{item.OFFLOADTYPE}},
        AMFPOINTER="{{item.AMFPOINTER}}",
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：OFFLOADTYPE=TAIRANGE 时必选 --- -#}
        {%- if item.OFFLOADTYPE == 'TAIRANGE' -%}
            TACSTART="{{item.TACSTART}}",
        {%- endif -%}
        {#- --- 条件必选：OFFLOADTYPE=RATE 时必选 --- -#}
        {%- if item.OFFLOADTYPE == 'RATE' -%}
            OFFLOADRATE={{item.OFFLOADRATE}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 8 如果1个以上子园区故障，且该园区已恢复，则通过设置TAC区域迁移用户。

```jinja2
{%- if is_scenario_multi_park_fault -%}
    {%- for item in str_offloadbyedgeamf_list_1 -%}
        STR OFFLOADBYEDGEAMF:
        {#- --- 必选参数 --- -#}
        OFFLOADTYPE={{item.OFFLOADTYPE}},
        AMFPOINTER="{{item.AMFPOINTER}}",
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：OFFLOADTYPE=RATE 时必选 --- -#}
        {%- if item.OFFLOADTYPE == 'RATE' -%}
            OFFLOADRATE={{item.OFFLOADRATE}},
        {%- endif -%}
        {#- --- 条件必选：OFFLOADTYPE=TAIRANGE 时必选 --- -#}
        {%- if item.OFFLOADTYPE == 'TAIRANGE' -%}
            TACEND="{{item.TACEND}}",
        {%- endif -%}
        {#- --- 条件必选：OFFLOADTYPE=TAIRANGE 时必选 --- -#}
        {%- if item.OFFLOADTYPE == 'TAIRANGE' -%}
            TACSTART="{{item.TACSTART}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 9 执行以下命令查询用户迁移的进度信息，每隔30s执行一次，确保“迁移状态”为“迁移任务已经结束”，并且“待迁移用户数”为0。

### 10 执行以下命令查询AMF的会话上下文数，确保“SA会话上下文总数”为0。

### 11 修改AMF的“相对容量”。其中“相对容量”为4中记录的值。

```jinja2
{%- for item in mod_amfinfo_list_1 -%}
    MOD AMFINFO:
    {#- --- 必选参数 --- -#}
    AMFINSTANCENAME="{{item.AMFINSTANCENAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.CAPACITY is not none -%}
        CAPACITY={{item.CAPACITY}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 12 修改AMF的“容量”。其中“容量”为4中记录的值。

```jinja2
{%- for item in mod_cpnfprofile_list_1 -%}
    MOD CPNFPROFILE:
    {#- --- 必选参数 --- -#}
    NFINSTANCENAME="{{item.NFINSTANCENAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.CAPACITY is not none -%}
        CAPACITY={{item.CAPACITY}},
    {%- endif -%}
    ;
{%- endfor -%}
```


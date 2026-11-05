---
id: ''
name: 配置5G业务故障恢复后的用户迁移
ne_type: UEG
type: feature
description: 在负荷分担容灾模式下，为避免故障恢复后两套UEG上网络负载不均衡的情况，需要参考本页面进行用户迁移操作。  本页面中的命令均为高危命令，请在华为工程师指导下执行。否则可能导致业务受损。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝L","UEG容灾方案介绍（风筝L）","负荷分担容灾原理","容灾部署与调测","负荷分担容灾模式","配置故障恢复后的用户迁移","配置5G业务故障恢复后的用户迁移"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
在负荷分担容灾模式下，为避免故障恢复后两套UEG上网络负载不均衡的情况，需要参考本页面进行用户迁移操作。本页面中的命令均为高危命令，请在华为工程师指导下执行。否则可能导致业务受损。

## 必备事项
前提条件

两套UEG已完成负荷分担容灾模式配置。
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
          description: '进行用户迁移的UEG中的AMF实例名称。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        CAPACITY:
          name: '相对容量'
          type: integer
          minimum: 0
          maximum: 255
          required: false
          description: '在启动迁移任务前，需将此参数设置为0，避免新用户接入。'
          data_source: '本端规划'
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
          description: '进行用户迁移的UEG中的AMF实例名称。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        CAPACITY:
          name: '容量'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: '在启动迁移任务前，需将此参数设置为0。'
          data_source: '本端规划'
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
          - TAIRANGE
          required: false
          description: '根据实际情况进行配置，两套UEG上需达到负载均衡。'
          data_source: '本端规划'
          pattern: ''
          default: ALL
        OFFLOADRATE:
          name: '迁移比率（%）'
          type: integer
          minimum: 1
          maximum: 100
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        TAMF:
          name: '目标AMF名称'
          type: string
          minLength: 0
          maxLength: 150
          required: false
          description: 'UEG1中的AMF名称，可通过****LST AMFINFO****查询。'
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
          description: '进行用户迁移的UEG中的AMF实例名称。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        CAPACITY:
          name: '相对容量'
          type: integer
          minimum: 0
          maximum: 255
          required: false
          description: '当迁移任务结束后，需要恢复AMF原相对容量。'
          data_source: '本端规划'
          pattern: ''
          default: ''
  examples:
    mod_amfinfo_list:
    - AMFINSTANCENAME: 'AMF_Instance_0'
      CAPACITY: 0
    mod_cpnfprofile_list:
    - NFINSTANCENAME: 'AMF_Instance_0'
      CAPACITY: 0
    str_offloadamf_list:
    - TYPE: RATE
      OFFLOADRATE: 50
      TAMF: 'AMF1'
    mod_amfinfo_list_1:
    - AMFINSTANCENAME: 'AMF_Instance_0'
      CAPACITY: 255
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 进入“MML命令行-UEG”窗口。

### 2 修改需要迁移的AMF的相对容量设置为0。

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

### 3 修改需要迁移的AMF实例信息。

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

### 4 对需要迁移的AMF下发启动迁移命令，向目标AMF迁移50%用户。

```jinja2
{%- for item in str_offloadamf_list -%}
    STR OFFLOADAMF:
    {#- --- 可选参数 --- -#}
    {%- if item.TYPE is not none -%}
        TYPE={{item.TYPE}},
    {%- endif -%}
    {%- if item.TAMF is not none -%}
        TAMF="{{item.TAMF}}",
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：TYPE=RATE 时必选 --- -#}
    {%- if item.TYPE == 'RATE' -%}
        OFFLOADRATE={{item.OFFLOADRATE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 5 当迁移任务结束后，恢复迁移的AMF原相对容量。

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


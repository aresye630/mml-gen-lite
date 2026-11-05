---
id: ''
name: 配置4G业务故障恢复后的用户迁移
ne_type: UEG
type: feature
description: 在负荷分担容灾模式下，为避免故障恢复后两套UEG上网络负载不均衡的情况，需要参考本页面进行用户迁移操作。  本页面中的命令均为高危命令，请在华为工程师指导下执行。否则可能导致业务受损。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝L","UEG容灾方案介绍（风筝L）","负荷分担容灾原理","容灾部署与调测","负荷分担容灾模式","配置故障恢复后的用户迁移","配置4G业务故障恢复后的用户迁移"]
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
    set_offloadinf_list:
      type: items
      properties:
        FIRSTTM:
          name: '第一阶段迁移时间'
          type: integer
          minimum: 0
          maximum: 432
          required: false
          description: '第一阶段迁移时间需要配置为0。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    set_cpsys_list:
      type: items
      properties:
        CAP:
          name: '设备能力'
          type: integer
          minimum: 0
          maximum: 255
          required: false
          description: '当UEG支持MME POOL时，在启动迁移任务时，需将此参数设置为0，避免新用户接入。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    str_offloadbyedgemme_list:
      type: items
      properties:
        OFFLOADRATE:
          name: '迁移比率'
          type: integer
          minimum: 1
          maximum: 100
          required: true
          description: '根据实际情况进行配置，两套UEG上需达到负载均衡。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        MMEC:
          name: '目标MME编码'
          type: string
          maxLength: 4
          required: true
          description: 'UEG1中的MME编码，可通过****LST MMEID****查询。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    str_nboffloadbyedgemme_list:
      type: items
      properties:
        OFFLOADRATE:
          name: '迁移比率'
          type: integer
          minimum: 1
          maximum: 100
          required: true
          description: '根据实际情况进行配置，两套UEG上需达到负载均衡。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        MMEC:
          name: '目标MME编码'
          type: string
          maxLength: 4
          required: true
          description: 'UEG1中的MME编码，可通过**LST MMEID**查询。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    set_cpsys_list_1:
      type: items
      properties:
        CAP:
          name: '设备能力'
          type: integer
          minimum: 0
          maximum: 255
          required: false
          description: '当迁移任务结束后，需要恢复MME原设备能力。'
          data_source: '本端规划'
          pattern: ''
          default: ''
  examples:
    set_offloadinf_list:
    - FIRSTTM: 0
    set_cpsys_list:
    - CAP: 0
    str_offloadbyedgemme_list:
    - OFFLOADRATE: 50
      MMEC: '01'
    str_nboffloadbyedgemme_list:
    - OFFLOADRATE: 50
      MMEC: '01'
    set_cpsys_list_1:
    - CAP: 255
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 进入“MML命令行-UEG”窗口。

### 2 设置迁移配置信息。

```jinja2
{%- for item in set_offloadinf_list -%}
    SET OFFLOADINF:
    {#- --- 可选参数 --- -#}
    {%- if item.FIRSTTM is not none -%}
        FIRSTTM={{item.FIRSTTM}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 修改需要迁移的MME的设备能力为0。

```jinja2
{%- for item in set_cpsys_list -%}
    SET CPSYS:
    {#- --- 可选参数 --- -#}
    {%- if item.CAP is not none -%}
        CAP={{item.CAP}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 对需要迁移的MME下发启动迁移命令，向目标MME迁移50%用户。

```jinja2
{%- for item in str_offloadbyedgemme_list -%}
    STR OFFLOADBYEDGEMME:
    {#- --- 必选参数 --- -#}
    OFFLOADRATE={{item.OFFLOADRATE}},
    MMEC="{{item.MMEC}}",
    ;
{%- endfor -%}
```

```jinja2
{%- for item in str_nboffloadbyedgemme_list -%}
    STR NBOFFLOADBYEDGEMME:
    {#- --- 必选参数 --- -#}
    OFFLOADRATE={{item.OFFLOADRATE}},
    MMEC="{{item.MMEC}}",
    ;
{%- endfor -%}
```

### 如果想停止用户迁移，可通过**STP OFFLOAD**命令主动停止当前正在进行的迁移任务。

### 5 当迁移任务结束后，恢复迁移的MME原设备能力。

```jinja2
{%- for item in set_cpsys_list_1 -%}
    SET CPSYS:
    {#- --- 可选参数 --- -#}
    {%- if item.CAP is not none -%}
        CAP={{item.CAP}},
    {%- endif -%}
    ;
{%- endfor -%}
```


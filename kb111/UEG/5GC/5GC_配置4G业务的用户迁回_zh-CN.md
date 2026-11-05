---
id: ''
name: 配置4G业务的用户迁回
ne_type: UEG
type: feature
description: 子园区UEG-L故障恢复后必须要尽快在总部园区UEG-L上将故障期间激活的用户回迁至子园区UEG-L，本章节介绍4G用户的迁回操作。  * 本页面中的命令均为高危命令，请在华为工程师指导下执行。否则可能导致业务受损。 * 如果多个子园区UEG-L同时故障，由于接入总部园区UEG-L的用户容量受限，因此可能导致故障子园区的新用户接入总部园区UEG-L失败。 * 如果多个子园区UEG-L同时故障，建议子园区UEG-L均恢复后，再进行用户迁回操作。 * 在总部园区UEG-L上将在线用户去激活后，用户业务发生中断，业务重新在子园区UEG-L上恢复的时间取决于终端业务行为。
tags: []
risk_level: ''
doc_source: ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（风筝多园区，入驻式）","风筝L+L多园区方案（跨级容灾，仅适用于海外）","子园区UEG-L故障恢复后配置","配置4G业务的用户迁回"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
子园区UEG-L故障恢复后必须要尽快在总部园区UEG-L上将故障期间激活的用户回迁至子园区UEG-L，本章节介绍4G用户的迁回操作。* 本页面中的命令均为高危命令，请在华为工程师指导下执行。否则可能导致业务受损。* 如果多个子园区UEG-L同时故障，由于接入总部园区UEG-L的用户容量受限，因此可能导致故障子园区的新用户接入总部园区UEG-L失败。* 如果多个子园区UEG-L同时故障，建议子园区UEG-L均恢复后，再进行用户迁回操作。* 在总部园区UEG-L上将在线用户去激活后，用户业务发生中断，业务重新在子园区UEG-L上恢复的时间取决于终端业务行为。

## 必备事项
前提条件

前提条件

两套UEG-L已完成跨级容灾模式配置。
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
          description: '当UEG支持MME POOL时，在启动迁移任务时，需将此参数设置为0，避免新用户接入。设备能力值越低，用户接入优先级越低'
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
    - OFFLOADRATE: 100
      MMEC: '子园区MME编码'
    set_cpsys_list_1:
    - CAP: 255
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 进入子园区的UEG-L“MML命令行-UEG”窗口。

### 2 执行**LST MMEID**查询“MME编码（起始值）”值。

### 3 进入总部园区的UEG-L“MML命令行-UEG”窗口。

### 4 设置迁移配置信息。

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

### 5 修改MME的设备能力为0。

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

### 6 下发启动迁移命令，向子园区MME迁移100%用户，其中MMEC为2查询的“MME编码（起始值）”值。

```jinja2
{%- for item in str_offloadbyedgemme_list -%}
    STR OFFLOADBYEDGEMME:
    {#- --- 必选参数 --- -#}
    OFFLOADRATE={{item.OFFLOADRATE}},
    MMEC="{{item.MMEC}}",
    ;
{%- endfor -%}
```

### 如果想停止用户迁移，可通过**STP OFFLOAD**命令主动停止当前正在进行的迁移任务。

### 7 执行以下命令查询用户迁移的进度信息，每隔30s执行一次，确保“迁移状态”为“结束完成”，并且“需要卸载用户数”为0。

### 8 执行以下命令查询网元的承载上下文，确保“GTPv2承载上下文总数”为0。

### 9 恢复迁移的MME原设备能力。

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


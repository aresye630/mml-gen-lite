---
id: ''
name: 配置主用UPF链路故障恢复
ne_type: UEG
type: feature
description: 在UPF主备容灾场景下，主用UPF故障恢复后，可通过本操作将备用UPF上的5G LAN会话去活后重新在主UPF上激活。
tags: []
risk_level: ''
doc_source: ["原子能力&行业场景","原子能力","5GC toB 原子能力-5G LAN","特性指南","UNC特性指南","配置主用UPF链路故障恢复"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
在UPF主备容灾场景下，主用UPF故障恢复后，可通过本操作将备用UPF上的5G LAN会话去活后重新在主UPF上激活。

## 必备事项
前提条件

已完成配置5G LAN业务基本功能。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    set_smfsoftparaofbit_list:
      type: items
      properties:
        DT:
          name: '数据类型'
          type: string
          enum:
          - Dw
          - Byte
          required: true
          description: '设置SMF软件参数比特位，主UPF故障恢复后，删除备UPF上的5G LAN会话。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        DWORDNUM:
          name: 'Dword索引'
          type: integer
          minimum: 1
          maximum: 1500
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VALUE:
          name: '软参记录值'
          type: string
          enum:
          - VALUE_0
          - VALUE_1
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        POSITION:
          name: '比特位'
          type: integer
          minimum: 1
          maximum: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_apnuprecover_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '配置主UPF故障恢复处理模式。'
          data_source: '本端规划  该参数需在**ADD APN**中进行配置。'
          pattern: ''
          default: ''
        MASTERUPFID:
          name: '主UPF实例名称'
          type: string
          minLength: 1
          maxLength: 255
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        HANDLINGMODE:
          name: 'UP链路故障恢复处理模式'
          type: string
          enum:
          - NOHANDLING
          - BACKMIGRATION
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        BACKUPFID:
          name: '备UPF实例名称'
          type: string
          minLength: 1
          maxLength: 255
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    set_upcscanrate_list:
      type: items
      properties:
        SCANTYPE:
          name: '扫描任务类型'
          type: string
          enum:
          - DEACTIVE
          - CHECK
          - DAILYCHECK
          - MIGRATE
          - ADDRDEACTIVE
          - INERTIALOPERATION
          - UPPATHFAULT
          - GTPUPATHFAULT
          - APNFAULT
          - PATHFAULTMIGRATE
          - PATHMIGRATE
          - BACKMIGRATION
          required: true
          description: '配置SMF上故障恢复回迁任务的控制扫描速率和扫描间隔。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        RATE:
          name: '扫描速率'
          type: integer
          minimum: 0
          maximum: 300
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        INTERVAL:
          name: '扫描间隔'
          type: integer
          minimum: 1
          maximum: 60
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    set_smfsoftparaofbit_list:
    - DT: Dw
      DWORDNUM: 1066
      VALUE: VALUE_1
      POSITION: 29
    add_apnuprecover_list:
    - APN: 'apn1'
      MASTERUPFID: 'upf1'
      HANDLINGMODE: BACKMIGRATION
      BACKUPFID: 'upf2'
    set_upcscanrate_list:
    - SCANTYPE: BACKMIGRATION
      RATE: 10
      INTERVAL: 5
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 //配置软参DWORD1066 BIT29值为1，主UPF故障恢复后，删除备UPF上的5G LAN会话。

```jinja2
{%- for item in set_smfsoftparaofbit_list -%}
    SET SMFSOFTPARAOFBIT:
    {#- --- 必选参数 --- -#}
    DT={{item.DT}},
    VALUE={{item.VALUE}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：DT=Dw 时必选 --- -#}
    {%- if item.DT == 'Dw' -%}
        DWORDNUM={{item.DWORDNUM}},
    {%- endif -%}
    {#- --- 条件必选：DT=Dw 时必选 --- -#}
    {%- if item.DT == 'Dw' -%}
        POSITION={{item.POSITION}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 2 //配置主UPF故障恢复处理模式。

```jinja2
{%- for item in add_apnuprecover_list -%}
    ADD APNUPRECOVER:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    MASTERUPFID="{{item.MASTERUPFID}}",
    HANDLINGMODE={{item.HANDLINGMODE}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：HANDLINGMODE=BACKMIGRATION 时必选 --- -#}
    {%- if item.HANDLINGMODE == 'BACKMIGRATION' -%}
        BACKUPFID="{{item.BACKUPFID}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 //配置SMF上故障恢复回迁任务的控制扫描速率和扫描间隔。

```jinja2
{%- for item in set_upcscanrate_list -%}
    SET UPCSCANRATE:
    {#- --- 必选参数 --- -#}
    SCANTYPE={{item.SCANTYPE}},
    RATE={{item.RATE}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：SCANTYPE=BACKMIGRATION 时必选 --- -#}
    {%- if item.SCANTYPE == 'BACKMIGRATION' -%}
        INTERVAL={{item.INTERVAL}},
    {%- endif -%}
    ;
{%- endfor -%}
```


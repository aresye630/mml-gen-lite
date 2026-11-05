---
id: ''
name: 激活N6接口故障隔离特性
ne_type: UNC
type: feature
description: 当网络中存在UPF/PGW-U/GGSN-U与DNN/APN数据网络之间的接口（N6接口、SGi或者Gi接口）故障时，可以激活N6接口故障隔离特性，使SMF/PGW-C/GGSN-C在选择UPF/PGW-U/GGSN-U时屏蔽N6/SGi/Gi接口故障的用户面网元。激活N6接口故障隔离特性，需要在UPF/PGW-U/GGSN-U侧和SMF/PGW-C/GGSN-C侧分别进行配置。SMF/PGW-C/GGSN-C侧配置请参考本章节进行操作。UPF/PGW-U/GGSN-U侧配置请在SMF/PGW-C/GGSN-C侧配置完成后参考UPF/PGW-U/GGSN-U的产品文档进行配置。  适用于GGSN、PGW-C、SMF。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","容灾功能","WSFD-213006 N6接口故障隔离","激活N6接口故障隔离特性"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
当网络中存在UPF/PGW-U/GGSN-U与DNN/APN数据网络之间的接口（N6接口、SGi或者Gi接口）故障时，可以激活N6接口故障隔离特性，使SMF/PGW-C/GGSN-C在选择UPF/PGW-U/GGSN-U时屏蔽N6/SGi/Gi接口故障的用户面网元。激活N6接口故障隔离特性，需要在UPF/PGW-U/GGSN-U侧和SMF/PGW-C/GGSN-C侧分别进行配置。SMF/PGW-C/GGSN-C侧配置请参考本章节进行操作。UPF/PGW-U/GGSN-U侧配置请在SMF/PGW-C/GGSN-C侧配置完成后参考UPF/PGW-U/GGSN-U的产品文档进行配置。适用于GGSN、PGW-C、SMF。

## 必备事项
前提条件

* 请仔细阅读WSFD-213006 N6接口故障隔离特性概述。
* 已激活WSFD-107010 UPF选择特性，详细操作请参考WSFD-107010 UPF选择。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    set_apnfault_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        UPFAULTMODE:
          name: 'UP链路故障处理模式'
          type: string
          enum:
          - NOHANDLING
          - DETECTION
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        RESTOREFAULT:
          name: 'SMF是否支持用户面链路故障恢复'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        AUXMIGFUNC:
          name: '辅锚点UPF迁移功能开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_pfcppara_list:
      type: items
      properties:
        UPFAULTAGETIME:
          name: '用户面链路故障信息老化时间(小时)'
          type: integer
          minimum: 5
          maximum: 72
          required: false
          description: '该参数应大于UPF上配置的路径状态上报周期。'
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
          description: '设置APN故障任务扫描用户的速率。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        RATE:
          name: '扫描速率(个/秒)'
          type: integer
          minimum: 0
          maximum: 300
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        INTERVAL:
          name: '扫描间隔（秒）'
          type: integer
          minimum: 1
          maximum: 60
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    set_apnfault_list:
    - APN: 'huawei.com'
      UPFAULTMODE: DETECTION
      RESTOREFAULT: ENABLE
      AUXMIGFUNC: ''
    set_pfcppara_list:
    - UPFAULTAGETIME: 5
    set_upcscanrate_list:
    - SCANTYPE: APNFAULT
      RATE: 20
      INTERVAL: ''
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 配置检测到N6接口故障后进行联动的APN。

```jinja2
{%- for item in set_apnfault_list -%}
    SET APNFAULT:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    {#- --- 可选参数 --- -#}
    {%- if item.UPFAULTMODE is not none -%}
        UPFAULTMODE={{item.UPFAULTMODE}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：UPFAULTMODE=DETECTION 时可选 --- -#}
    {%- if item.UPFAULTMODE == 'DETECTION' -%}
        {%- if item.RESTOREFAULT is not none -%}
            RESTOREFAULT={{item.RESTOREFAULT}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：RESTOREFAULT=ENABLE 时可选 --- -#}
    {%- if item.RESTOREFAULT == 'ENABLE' -%}
        {%- if item.AUXMIGFUNC is not none -%}
            AUXMIGFUNC={{item.AUXMIGFUNC}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 2 配置用户面链路故障老化时间。

```jinja2
{%- for item in set_pfcppara_list -%}
    SET PFCPPARA:
    {#- --- 可选参数 --- -#}
    {%- if item.UPFAULTAGETIME is not none -%}
        UPFAULTAGETIME={{item.UPFAULTAGETIME}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 设置APN故障任务扫描用户的速率。

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


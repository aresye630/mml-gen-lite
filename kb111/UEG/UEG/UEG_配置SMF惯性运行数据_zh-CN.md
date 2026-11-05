---
id: ''
name: 配置SMF惯性运行数据
ne_type: UEG
type: feature
description: 用户面业务通道保活是指，企业园区场景下，当园区gNodeB、UPF跟园区外部署的AMF、SMF失联时，即N2/N4接口不可用但N3接口可用时，弱移动性（不跨gNodeB切换）连接态用户的数传业务能够继续进行（惯性运行）。  适用于SMF。
tags: []
risk_level: ''
doc_source:
  - ["网络部署","园区入驻+地市共享（连接+计算）","5GC toB 部署边缘站点（站点为“风筝M”，带计算）","配置业务数据（风筝M）","惯性运行及数据同步配置（5G Core）","配置SMF惯性运行数据"]
  - ["业务配置","风筝M","MEC 特性指南（风筝M）","UNC特性指南","WSFD-217001 用户面业务通道保活","配置SMF惯性运行数据"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
用户面业务通道保活是指，企业园区场景下，当园区gNodeB、UPF跟园区外部署的AMF、SMF失联时，即N2/N4接口不可用但N3接口可用时，弱移动性（不跨gNodeB切换）连接态用户的数传业务能够继续进行（惯性运行）。适用于SMF。

## 必备事项
前提条件

* 请仔细阅读WSFD-217001 用户面业务通道保活特性概述。
* 完成加载License。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    mod_upnode_list:
      type: items
      properties:
        NFINSTANCENAME:
          name: 'UPF实例名称'
          type: string
          minLength: 0
          maxLength: 255
          required: true
          description: '该命令用于设置园区惯性运行开关。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        IOSWITCH:
          name: '惯性运行开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CAMPUSSW:
          name: '园区UPF开关'
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
        IOINTERVAL:
          name: '惯性运行定时器(秒)'
          type: integer
          minimum: 0
          maximum: 300
          required: false
          description: '该命令用于设置链路惯性运行定时器，UPF心跳异常后开启该定时器，定时器超时后心跳仍未恢复，该链路惯性运行定时器超时。'
          data_source: '本端规划'
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
          description: '该命令用于设置控制面扫描用户的速率。'
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
          data_source: ''
          pattern: ''
          default: ''
  examples:
    mod_upnode_list:
    - NFINSTANCENAME: 'upf1'
      IOSWITCH: ENABLE
      CAMPUSSW: ENABLE
    set_pfcppara_list:
    - IOINTERVAL: 60
    set_upcscanrate_list:
    - SCANTYPE: INERTIALOPERATION
      RATE: 30
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 进入“MML命令行-UEG”窗口。

### 2 **可选：**增加园区策略，设置园区惯性运行开关。

```jinja2
{%- if is_optional_campus_policy -%}
    {%- for item in mod_upnode_list -%}
        MOD UPNODE:
        {#- --- 必选参数 --- -#}
        NFINSTANCENAME="{{item.NFINSTANCENAME}}",
        {#- --- 可选参数 --- -#}
        {%- if item.IOSWITCH is not none -%}
            IOSWITCH={{item.IOSWITCH}},
        {%- endif -%}
        {%- if item.CAMPUSSW is not none -%}
            CAMPUSSW={{item.CAMPUSSW}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 3 设置SMF和园区UPF间链路惯性运行定时器。

```jinja2
{%- for item in set_pfcppara_list -%}
    SET PFCPPARA:
    {#- --- 可选参数 --- -#}
    {%- if item.IOINTERVAL is not none -%}
        IOINTERVAL={{item.IOINTERVAL}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 设置控制面扫描用户的速率。

```jinja2
{%- for item in set_upcscanrate_list -%}
    SET UPCSCANRATE:
    {#- --- 必选参数 --- -#}
    SCANTYPE={{item.SCANTYPE}},
    RATE={{item.RATE}},
    ;
{%- endfor -%}
```


---
id: GWFD-020162
name: 配置用户面会话过载控制
ne_type: UDG
type: feature
description: 为了避免UDG上EPS承载/PDU会话资源残留从而出现用户面会话过载，需要配置会话核查功能，及时清除残留的EPS承载/PDU会话信息。  适用于SGW-U、PGW-U、UPF。
risk_level: ''
doc_source: ["特性部署","特性指南","UDG特性指南","可靠性功能","GWFD-020162 用户面会话过载控制","配置用户面会话过载控制"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
为了避免UDG上EPS承载/PDU会话资源残留从而出现用户面会话过载，需要配置会话核查功能，及时清除残留的EPS承载/PDU会话信息。适用于SGW-U、PGW-U、UPF。

## 必备事项
前提条件

请仔细阅读GWFD-020162 用户面会话过载控制特性概述。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    set_sesschkfunc_list:
      type: items
      properties:
        ESTABLISHCHK:
          name: '会话创建核查开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '控制新的EPS承载/PDU会话创建时对UDG上已经存在的相同IMSI的EPS承载/PDU会话是否触发核查。默认使能。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SESSNUMTHD:
          name: '会话创建核查阈值'
          type: integer
          minimum: 1
          maximum: 21
          required: false
          description: '配置存在几个相同IMSI的EPS承载/PDU会话数时触发会话核查。默认4个。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PATHDWNCHK:
          name: '路径断核查开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '控制N4链路从断到正常后是否触发与SGW-C/PGW-C/SMF之间的会话信息核查。默认使能。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        DAYCHK:
          name: '每日核查开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '控制系统每天是否触发与SGW-C/PGW-C/SMF之间的会话信息核查。默认使能。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SGRECOVERYCHK:
          name: 'Session SG恢复核查开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '控制系统进程故障恢复后是否触发与SGW-C/PGW-C/SMF之间的会话信息核查。默认使能。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SESSLIMITCHK:
          name: '会话规格限制核查开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '控制会话资源达到阈值90%时是否触发跟SGW-C/PGW-C/SMF的会话信息核查。默认使能。'
          data_source: '本端规划'
          pattern: ''
          default: ''
  examples:
    set_sesschkfunc_list:
    - ESTABLISHCHK: ENABLE
      SESSNUMTHD: 4
      PATHDWNCHK: ENABLE
      DAYCHK: ENABLE
      SGRECOVERYCHK: ENABLE
      SESSLIMITCHK: ENABLE
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 设置会话核查配置。

#### 1.1 //设置会话核查配置，打开会话核查开关。

```jinja2
{%- for item in set_sesschkfunc_list -%}
    SET SESSCHKFUNC:
    {#- --- 可选参数 --- -#}
    {%- if item.ESTABLISHCHK is not none -%}
        ESTABLISHCHK={{item.ESTABLISHCHK}},
    {%- endif -%}
    {%- if item.PATHDWNCHK is not none -%}
        PATHDWNCHK={{item.PATHDWNCHK}},
    {%- endif -%}
    {%- if item.DAYCHK is not none -%}
        DAYCHK={{item.DAYCHK}},
    {%- endif -%}
    {%- if item.SGRECOVERYCHK is not none -%}
        SGRECOVERYCHK={{item.SGRECOVERYCHK}},
    {%- endif -%}
    {%- if item.SESSLIMITCHK is not none -%}
        SESSLIMITCHK={{item.SESSLIMITCHK}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：ESTABLISHCHK=ENABLE 时可选 --- -#}
    {%- if item.ESTABLISHCHK == 'ENABLE' -%}
        {%- if item.SESSNUMTHD is not none -%}
            SESSNUMTHD={{item.SESSNUMTHD}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```


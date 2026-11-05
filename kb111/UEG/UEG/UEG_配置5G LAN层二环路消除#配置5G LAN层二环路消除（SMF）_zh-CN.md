---
id: GWFD-031104
name: 配置5G LAN层二环路消除（SMF）
ne_type: UEG
type: feature
description: 同一5G LAN终端组成员之间或5G LAN终端组的成员和数据网络中的应用之间进行以太通信时，可通过部署5G LAN层二环路消除，避免二层环路的危害。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝S","MEC 特性指南（风筝S）","UEG特性指南","5G LAN基本功能","可选功能","GWFD-031104 5G LAN层二环路消除","配置5G LAN层二环路消除","配置5G LAN层二环路消除（SMF）"]
refs: []
metadata:
  DepOnLiveCfg: true
allowed-tools:
- getParameterValue('LST GRPNGLANFUNC')
---
<!-- @mml:block= annotations -->
```text
## 操作场景
同一5G LAN终端组成员之间或5G LAN终端组的成员和数据网络中的应用之间进行以太通信时，可通过部署5G LAN层二环路消除，避免二层环路的危害。

## 必备事项
前提条件

已在SMF上完成5G LAN基本配置。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    mod_grpnglanfunc_list:
      type: items
      properties:
        GROUPID:
          name: '5G LAN组ID'
          type: string
          minLength: 1
          maxLength: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LDRSW:
          name: '环路检测开关'
          type: string
          enum:
          - NotSupport
          - Support
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_grpnglanfunc_list:
      type: items
      properties:
        GROUPID:
          name: '5G LAN组ID'
          type: string
          minLength: 1
          maxLength: 255
          required: true
          description: '与UPF上**ADD NGVNINSTANCE**命令定义的VNINSTANCE一致。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        LDRSW:
          name: '环路检测开关'
          type: string
          enum:
          - NotSupport
          - Support
          required: false
          description: 'UPF上的同一5G LAN组开启环路检测时，SMF上该参数设置为“Support”；否则设置为“NotSupport”。'
          data_source: '本端规划'
          pattern: ''
          default: ''
  examples:
    mod_grpnglanfunc_list:
    - GROUPID: '000003e9-460-08-02'
      LDRSW: SUPPORT
    add_grpnglanfunc_list:
    - GROUPID: '000003e9-460-08-02'
      LDRSW: SUPPORT
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 执行**LST GRPNGLANFUNC**命令，查看指定5G LAN组的“环路检测开关（LDRSW）”参数值。

#### 1.1 “环路检测开关（LDRSW）”参数值为“Support”，已开启环路检测开关，配置结束。

#### 1.2 “环路检测开关（LDRSW）”参数值为“NotSupport”，请执行2。

#### 1.3 未查询到该5G LAN组的信息，请执行3。

### 2 执行**MOD GRPNGLANFUNC**命令，开启环路检测开关。

```jinja2
{%- set LST_GRPNGLANFUNC=getParameterValue('LST GRPNGLANFUNC') -%}
{%- if LST_GRPNGLANFUNC=='NotSupport' -%}
    {%- for item in mod_grpnglanfunc_list -%}
        MOD GRPNGLANFUNC:
        {#- --- 必选参数 --- -#}
        GROUPID="{{item.GROUPID}}",
        {#- --- 可选参数 --- -#}
        {%- if item.LDRSW is not none -%}
            LDRSW={{item.LDRSW}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 3 执行**ADD GRPNGLANFUNC**命令，开启环路检测开关。

```jinja2
{%- if LST_GRPNGLANFUNC=='' -%}
    {%- for item in add_grpnglanfunc_list -%}
        ADD GRPNGLANFUNC:
        {#- --- 必选参数 --- -#}
        GROUPID="{{item.GROUPID}}",
        {#- --- 可选参数 --- -#}
        {%- if item.LDRSW is not none -%}
            LDRSW={{item.LDRSW}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```


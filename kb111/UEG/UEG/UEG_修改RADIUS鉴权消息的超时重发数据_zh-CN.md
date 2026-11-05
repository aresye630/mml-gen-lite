---
id: GWFD-024303
name: 修改RADIUS鉴权消息的超时重发数据
ne_type: UEG
type: feature
description: 当AAA Server的RADIUS消息的重发次数和超时的时间发生变化时，UEG需要修改相应的配置以便和AAA Server保持一致。  适用于PGW-C、SMF
tags: []
risk_level: ''
doc_source: ["业务配置","风筝L","MEC 特性指南（风筝L）","GW-C&SMF特性指南","GWFD-024300 系统管理","GWFD-024303 Radius功能","调整AAA鉴权参数","修改RADIUS鉴权消息的超时重发数据"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
当AAA Server的RADIUS消息的重发次数和超时的时间发生变化时，UEG需要修改相应的配置以便和AAA Server保持一致。适用于PGW-C、SMF

## 必备事项
前提条件

完成配置RADIUS功能。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    mod_rdssvrgrp_list:
      type: items
      properties:
        RDSSVRGRPNAME:
          name: 'Radius Server Group名称'
          type: string
          maxLength: 31
          required: true
          description: '鉴权服务器所在的Radius服务器组，已通过**ADD RDSSVRGRP**进行配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        AUTHTIMEOUT:
          name: 'Radius Authentication Request超时时间'
          type: integer
          minimum: 1
          maximum: 10
          required: false
          description: '**MOD RDSSVRGRP**'
          data_source: '与对端协商'
          pattern: ''
          default: ''
        AUTHRETRANSMIT:
          name: 'Radius Authentication Request重发次数'
          type: integer
          minimum: 0
          maximum: 5
          required: false
          description: ''
          data_source: '与对端协商'
          pattern: ''
          default: ''
  examples:
    mod_rdssvrgrp_list:
    - RDSSVRGRPNAME: 'ss'
      AUTHTIMEOUT: 3
      AUTHRETRANSMIT: 1
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 进入“MML命令行-UEG”窗口。

### 2 修改RADIUS消息的重发数据。

#### 2.1 //修改RADIUS消息的重发数据。

```jinja2
{%- for item in mod_rdssvrgrp_list -%}
    MOD RDSSVRGRP:
    {#- --- 必选参数 --- -#}
    RDSSVRGRPNAME="{{item.RDSSVRGRPNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.AUTHTIMEOUT is not none -%}
        AUTHTIMEOUT={{item.AUTHTIMEOUT}},
    {%- endif -%}
    {%- if item.AUTHRETRANSMIT is not none -%}
        AUTHRETRANSMIT={{item.AUTHRETRANSMIT}},
    {%- endif -%}
    ;
{%- endfor -%}
```


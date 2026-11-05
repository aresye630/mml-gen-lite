---
id: GWFD-021404
name: 激活服务化接口发送消息固定速率流控功能
ne_type: UEG
type: feature
description: 服务化接口固定速率流控功能是指在服务化接口存在拥塞风险时，UEG基于配置的服务化接口流控速率阈值，控制接口上发送消息的速率，减少服务化接口拥塞，避免对端网元过载。  本章节以本端网元为AMF，对端网元为UDM举例。  适用于AMF、SMF、NSSF
tags: []
risk_level: ''
doc_source:
  - ["业务配置","风筝L","MEC 特性指南（风筝L）","AMF特性指南","GWFD-021400 可靠性功能","GWFD-021404 周边网元过载保护","服务化接口固定速率流控功能","激活服务化接口发送消息固定速率流控功能"]
  - ["业务配置","风筝L","MEC 特性指南（风筝L）","GW-C&SMF特性指南","GWFD-021400 可靠性功能","GWFD-021404 周边网元过载保护","服务化接口固定速率流控功能","激活服务化接口发送消息固定速率流控功能"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
服务化接口固定速率流控功能是指在服务化接口存在拥塞风险时，UEG基于配置的服务化接口流控速率阈值，控制接口上发送消息的速率，减少服务化接口拥塞，避免对端网元过载。本章节以本端网元为AMF，对端网元为UDM举例。适用于AMF、SMF、NSSF

## 必备事项
前提条件

该操作无需具备特殊条件。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    add_httpfcipgrp_list:
      type: items
      properties:
        INDEX:
          name: '索引'
          type: integer
          minimum: 0
          maximum: 4095
          required: true
          description: '设置流控组信息。  说明：  本端网元作为客户端的业务，选择对端网元的IP地址作为流控组的IP地址，如果是间接路由场景，选择下一跳（例如SCP）的IP地址作为流控组的IP地址；本端网元作为服务端的业务，选择本端网元配置的HTTPLE的服务端IP作为流控组的IP地址。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        GROUP:
          name: '流控组'
          type: integer
          minimum: 0
          maximum: 4095
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPTYPE:
          name: 'IP地址类型'
          type: string
          enum:
          - IPv4
          - IPv6
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV4ADDR:
          name: 'IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV4MASK:
          name: 'IPv4掩码'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DESC:
          name: '描述'
          type: string
          minLength: 0
          maxLength: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_httpfixedfc_list:
      type: items
      properties:
        GROUP:
          name: '流控组'
          type: integer
          minimum: 0
          maximum: 4095
          required: true
          description: '增加HTTP流控门限。  说明：  此处门限值为举例，请根据局点实际情况进行设置。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        GROUPTYPE:
          name: '流控组类型'
          type: string
          enum:
          - SERVER
          - CLIENT
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: SERVER
        SENDTHD:
          name: '单链路发送消息流控门限(条/秒)'
          type: integer
          minimum: 1
          maximum: 1000000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DESC:
          name: '描述'
          type: string
          minLength: 0
          maxLength: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_httpfixedfc_list_1:
      type: items
      properties:
        GROUP:
          name: '流控组'
          type: integer
          minimum: 0
          maximum: 4095
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GROUPTYPE:
          name: '流控组类型'
          type: string
          enum:
          - SERVER
          - CLIENT
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: SERVER
        GLBSENDTHD:
          name: '整系统发送消息流控门限(条/秒)'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DESC:
          name: '描述'
          type: string
          minLength: 0
          maxLength: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    add_httpfcipgrp_list:
    - INDEX: 1
      GROUP: 1
      IPTYPE: IPv4
      IPV4ADDR: '192.168.100.1'
      IPV4MASK: '255.255.255.0'
      DESC: 'UDM_instance1'
    - INDEX: 3
      GROUP: 2
      IPTYPE: IPv4
      IPV4ADDR: '192.168.200.1'
      IPV4MASK: '255.255.255.0'
      DESC: 'UDM_instance1'
    add_httpfixedfc_list:
    - GROUP: 1
      GROUPTYPE: CLIENT
      SENDTHD: 1000
      DESC: 'LINK'
    add_httpfixedfc_list_1:
    - GROUP: 2
      GROUPTYPE: CLIENT
      GLBSENDTHD: 2000
      DESC: 'GLOBAL'
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 进入“MML命令行-UEG”窗口。

### 2 增加HTTP固定速率流控的IP地址组信息。

##### 2.1.1 //配置流控组信息。

```jinja2
{%- for item in add_httpfcipgrp_list -%}
    ADD HTTPFCIPGRP:
    {#- --- 必选参数 --- -#}
    INDEX={{item.INDEX}},
    GROUP={{item.GROUP}},
    IPTYPE={{item.IPTYPE}},
    {#- --- 可选参数 --- -#}
    {%- if item.DESC is not none -%}
        DESC="{{item.DESC}}",
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPTYPE=IPv4 时必选 --- -#}
    {%- if item.IPTYPE == 'IPv4' -%}
        IPV4ADDR="{{item.IPV4ADDR}}",
    {%- endif -%}
    {#- --- 条件必选：IPTYPE=IPv4 时必选 --- -#}
    {%- if item.IPTYPE == 'IPv4' -%}
        IPV4MASK="{{item.IPV4MASK}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 AMF上增加HTTP流控门限。

##### 3.1.1 //配置流控速率。

```jinja2
{%- for item in add_httpfixedfc_list -%}
    ADD HTTPFIXEDFC:
    {#- --- 必选参数 --- -#}
    GROUP={{item.GROUP}},
    {#- --- 可选参数 --- -#}
    {%- if item.GROUPTYPE is not none -%}
        GROUPTYPE={{item.GROUPTYPE}},
    {%- endif -%}
    {%- if item.SENDTHD is not none -%}
        SENDTHD={{item.SENDTHD}},
    {%- endif -%}
    {%- if item.DESC is not none -%}
        DESC="{{item.DESC}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

##### 3.1.2 //配置流控速率。

```jinja2
{%- for item in add_httpfixedfc_list_1 -%}
    ADD HTTPFIXEDFC:
    {#- --- 必选参数 --- -#}
    GROUP={{item.GROUP}},
    {#- --- 可选参数 --- -#}
    {%- if item.GROUPTYPE is not none -%}
        GROUPTYPE={{item.GROUPTYPE}},
    {%- endif -%}
    {%- if item.GLBSENDTHD is not none -%}
        GLBSENDTHD={{item.GLBSENDTHD}},
    {%- endif -%}
    {%- if item.DESC is not none -%}
        DESC="{{item.DESC}}",
    {%- endif -%}
    ;
{%- endfor -%}
```


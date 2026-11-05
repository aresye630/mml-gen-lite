---
id: GWFD-020804
name: 配置静态地址黑名单
ne_type: UEG
type: feature
description: 可以在本地配置静态地址黑名单，判断用户携带地址的合法性，若用户地址出现于黑名单中，标明地址非法，不允许接入。  适用于PGW-C、SMF。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝L","MEC 特性指南（风筝L）","GW-C&SMF特性指南","GWFD-020800 基本业务","GWFD-020804 地址分配方式","配置静态地址黑名单"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
可以在本地配置静态地址黑名单，判断用户携带地址的合法性，若用户地址出现于黑名单中，标明地址非法，不允许接入。适用于PGW-C、SMF。

## 必备事项
前提条件

请仔细阅读GWFD-020804 地址分配方式特性概述。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    add_blacklist_list:
      type: items
      properties:
        NAME:
          name: '名称'
          type: string
          minLength: 1
          maxLength: 79
          required: true
          description: '配置静态地址黑名单'
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPVERSION:
          name: 'IP地址类型'
          type: string
          enum:
          - IPv4
          - IPv6
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: IPv4
        V4STARTIP:
          name: 'IPv4起始地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        V4ENDIP:
          name: 'IPv4结束地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        HASVPN:
          name: '绑定VPN'
          type: string
          enum:
          - Disable
          - Enable
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: Disable
        VPNINSTANCE:
          name: 'VPN实例名'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: '-'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
  examples:
    add_blacklist_list:
    - NAME: 'testblacklist'
      IPVERSION: IPv4
      V4STARTIP: '10.1.1.1'
      V4ENDIP: '10.1.1.10'
      HASVPN: Enable
      VPNINSTANCE: 'testvpn'
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 进入“MML命令行-UEG”窗口。

### 2 创建静态地址黑名单。

#### 2.1 //创建静态地址黑名单。

```jinja2
{%- for item in add_blacklist_list -%}
    ADD BLACKLIST:
    {#- --- 必选参数 --- -#}
    NAME="{{item.NAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.IPVERSION is not none -%}
        IPVERSION={{item.IPVERSION}},
    {%- endif -%}
    {%- if item.HASVPN is not none -%}
        HASVPN={{item.HASVPN}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPVERSION=IPv4 时必选 --- -#}
    {%- if item.IPVERSION == 'IPv4' -%}
        V4STARTIP="{{item.V4STARTIP}}",
    {%- endif -%}
    {#- --- 条件必选：IPVERSION=IPv4 时必选 --- -#}
    {%- if item.IPVERSION == 'IPv4' -%}
        V4ENDIP="{{item.V4ENDIP}}",
    {%- endif -%}
    {#- --- 条件必选：HASVPN=Enable 时必选 --- -#}
    {%- if item.HASVPN == 'Enable' -%}
        VPNINSTANCE="{{item.VPNINSTANCE}}",
    {%- endif -%}
    ;
{%- endfor -%}
```


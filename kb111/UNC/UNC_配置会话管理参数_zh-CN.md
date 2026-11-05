---
id: ''
name: 配置会话管理参数
ne_type: UNC
type: feature
description: 配置GGSN本局数据的基本流程包括：开始→配置APN信息→结束。
risk_level: ''
doc_source: ["网络部署","初始配置","UNC初始配置与调测","组网对接配置","配置SMF&PGW-C&SGW-C&GGSN","配置GGSN","配置会话管理参数"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
配置GGSN本局数据的基本流程包括：开始→配置APN信息→结束。

## 必备事项
前提条件

* 具备管理员权限的操作人员已经登录华为操作维护系统（登录U2020/MAE客户端或登录OM Portal）。

* 已经获取网设LLD文档。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    add_apn_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '配置APN。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        VIRTUALAPN:
          name: '虚拟APN'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: DISABLE
        HASVPN:
          name: '绑定VPN'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: DISABLE
        VPNINSTANCE:
          name: 'VPN实例名'
          type: string
          minLength: 1
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_uednsbindapn_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '配置指定APN实例的DNS属性和DNS64属性。APN名称已通过**ADD APN**配置。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        MDNSSERVERV4:
          name: 'IPv4主DNS服务器IP'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        BDNSSERVERV4:
          name: 'IPv4备DNS服务器IP'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
  examples:
    add_apn_list:
    - APN: 'huawei.com'
      VIRTUALAPN: DISABLE
      HASVPN: DISABLE
      VPNINSTANCE: ''
    set_uednsbindapn_list:
    - APN: 'huawei.com'
      MDNSSERVERV4: '10.10.1.1'
      BDNSSERVERV4: '10.10.1.2'
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 配置PGW-C支持的APN。

```jinja2
{%- for item in add_apn_list -%}
    ADD APN:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    {#- --- 可选参数 --- -#}
    {%- if item.VIRTUALAPN is not none -%}
        VIRTUALAPN={{item.VIRTUALAPN}},
    {%- endif -%}
    {%- if item.HASVPN is not none -%}
        HASVPN={{item.HASVPN}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：HASVPN=ENABLE 时必选 --- -#}
    {%- if item.HASVPN == 'ENABLE' -%}
        VPNINSTANCE="{{item.VPNINSTANCE}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 2 在使用DNS服务器场景下，配置指定APN的DNS属性。

```jinja2
{%- for item in set_uednsbindapn_list -%}
    SET UEDNSBINDAPN:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    {#- --- 可选参数 --- -#}
    {%- if item.MDNSSERVERV4 is not none -%}
        MDNSSERVERV4="{{item.MDNSSERVERV4}}",
    {%- endif -%}
    {%- if item.BDNSSERVERV4 is not none -%}
        BDNSSERVERV4="{{item.BDNSSERVERV4}}",
    {%- endif -%}
    ;
{%- endfor -%}
```


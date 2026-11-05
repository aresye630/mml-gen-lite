---
id: ''
name: 激活Radius鉴权接入
ne_type: UNC
type: feature
description: 本操作指导介绍在运行网络中激活Radius鉴权接入特性的操作过程。  适用于GGSN、PGW-C、SMF。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","组网功能","WSFD-011305 Radius鉴权接入","激活Radius鉴权接入"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本操作指导介绍在运行网络中激活Radius鉴权接入特性的操作过程。适用于GGSN、PGW-C、SMF。

## 必备事项
前提条件

* 请仔细阅读WSFD-011305 Radius鉴权接入特性概述。
* 已经完成配置普通DNN。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    set_apnauthattr_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '已通过命令****ADD APN**** 配置。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        ACCESSMODE:
          name: '接入模式'
          type: string
          enum:
          - TRANS_AUTH
          - TRANS_NON_AUTH
          - NON_TRANS
          - LOC_AUTH
          required: false
          description: '可选的接入模式包括：   * TRANS\_AUTH（透明鉴权）：指定为透明并需要鉴权。这种鉴权方式对用户是透明的，不需要用户感知，鉴权使用的用户名和密码一般由UNC配置。 * TRANS\_NON\_AUTH（透明不鉴权）：指定为透明不需要鉴权。这种接入方式不需要去RADIUS服务器鉴权。 * NON\_TRANS（不透明）：指定为不透明接入，需要鉴权。这种鉴权方式可以继续配置鉴权使用的用户名和密码。 * LOC\_AUTH（本地鉴权）：指定为本地鉴权。这种接入方式不需要去RADIUS服务器鉴权，通过UNC完成鉴权功能。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        COMMONUSERNAME:
          name: '公用用户名'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        COMMONUSERPASS:
          name: '公用密码'
          type: string
          minLength: 1
          maxLength: 128
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        CFMCOMMUSERPASS:
          name: '确认公共密码'
          type: string
          minLength: 1
          maxLength: 128
          required: false
          description: '该参数需要与“COMMONUSERPASS”保持一致。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        APNEAP:
          name: 'APN EAP鉴权'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AUTHMODE:
          name: '鉴权模式'
          type: string
          enum:
          - PCO
          - APN
          - MSISDN
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GULAUTHSW:
          name: '控制2/3/4G场景下是否进行鉴权'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SECONDAUTH:
          name: '二次鉴权'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        UDMSUBAUTHSW:
          name: '控制是否使用UDM签约数据参与决策进行AAA鉴权'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    set_apnauthattr_list:
    - APN: 'huawei.com'
      ACCESSMODE: TRANS_AUTH
      COMMONUSERNAME: 'huawei123'
      COMMONUSERPASS: '123'
      CFMCOMMUSERPASS: '123'
      APNEAP: ''
      AUTHMODE: ''
      GULAUTHSW: ''
      SECONDAUTH: ''
      UDMSUBAUTHSW: ''
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 进入“MML命令行-UNC”窗口。

### 2 配置APN鉴权属性。

```jinja2
{%- for item in set_apnauthattr_list -%}
    SET APNAUTHATTR:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    {#- --- 可选参数 --- -#}
    {%- if item.ACCESSMODE is not none -%}
        ACCESSMODE={{item.ACCESSMODE}},
    {%- endif -%}
    {%- if item.COMMONUSERNAME is not none -%}
        COMMONUSERNAME="{{item.COMMONUSERNAME}}",
    {%- endif -%}
    {%- if item.COMMONUSERPASS is not none -%}
        COMMONUSERPASS="{{item.COMMONUSERPASS}}",
    {%- endif -%}
    {%- if item.CFMCOMMUSERPASS is not none -%}
        CFMCOMMUSERPASS="{{item.CFMCOMMUSERPASS}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：ACCESSMODE=NON_TRANS 时可选 --- -#}
    {%- if item.ACCESSMODE == 'NON_TRANS' -%}
        {%- if item.APNEAP is not none -%}
            APNEAP={{item.APNEAP}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：ACCESSMODE=NON_TRANS 时可选 --- -#}
    {%- if item.ACCESSMODE == 'NON_TRANS' -%}
        {%- if item.AUTHMODE is not none -%}
            AUTHMODE={{item.AUTHMODE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：ACCESSMODE=TRANS_AUTH/NON_TRANS/LOC_AUTH 时可选 --- -#}
    {%- if item.ACCESSMODE in ['TRANS_AUTH', 'NON_TRANS', 'LOC_AUTH'] -%}
        {%- if item.GULAUTHSW is not none -%}
            GULAUTHSW={{item.GULAUTHSW}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：ACCESSMODE=TRANS_AUTH/NON_TRANS 时可选 --- -#}
    {%- if item.ACCESSMODE in ['TRANS_AUTH', 'NON_TRANS'] -%}
        {%- if item.SECONDAUTH is not none -%}
            SECONDAUTH={{item.SECONDAUTH}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：ACCESSMODE=TRANS_AUTH/NON_TRANS/LOC_AUTH 时可选 --- -#}
    {%- if item.ACCESSMODE in ['TRANS_AUTH', 'NON_TRANS', 'LOC_AUTH'] -%}
        {%- if item.UDMSUBAUTHSW is not none -%}
            UDMSUBAUTHSW={{item.UDMSUBAUTHSW}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```


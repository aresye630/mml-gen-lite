---
id: GWFD-024302
name: 激活Radius鉴权接入
ne_type: UEG
type: feature
description: 本操作指导介绍在运行网络中激活Radius鉴权接入特性的操作过程。  适用于PGW-C、SMF
tags: []
risk_level: ''
doc_source: ["业务配置","风筝L","MEC 特性指南（风筝L）","GW-C&SMF特性指南","GWFD-024300 系统管理","GWFD-024302 Radius鉴权接入","激活Radius鉴权接入"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
本操作指导介绍在运行网络中激活Radius鉴权接入特性的操作过程。适用于PGW-C、SMF

## 必备事项
前提条件

前提条件

* 当UEG的产品形态为风筝L时，请仔细阅读GWFD-024302 Radius鉴权接入特性概述。
* 已经完成配置普通DNN。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
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
          description: '已通过命令 ****ADD CPAPN****配置。'
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
          description: '可选的接入模式包括：   * TRANS\_AUTH（透明鉴权）：指定为透明并需要鉴权。这种鉴权方式对用户是透明的，不需要用户感知，鉴权使用的用户名和密码一般由UEG配置。 * TRANS\_NON\_AUTH（透明不鉴权）：指定为透明不需要鉴权。这种接入方式不需要去RADIUS服务器鉴权。 * NON\_TRANS（不透明）：指定为不透明接入，需要鉴权。这种鉴权方式可以继续配置鉴权使用的用户名和密码。 * LOC\_AUTH（本地鉴权）：指定为本地鉴权。这种接入方式不需要去RADIUS服务器鉴权，通过UEG完成鉴权功能。'
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
  examples:
    set_apnauthattr_list:
    - APN: 'huawei.com'
      ACCESSMODE: TRANS_AUTH
      COMMONUSERNAME: 'huawei123'
      COMMONUSERPASS: '123'
      CFMCOMMUSERPASS: '123'
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 进入“MML命令行-UEG”窗口。

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
    ;
{%- endfor -%}
```


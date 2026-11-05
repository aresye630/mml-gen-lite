---
id: ''
name: 基于拨测用户设置媒体中继业务开关
ne_type: UDG
type: feature
description: 当SMF无法下发媒体中继用户标识及规则的场景下，需要基于拨测用户在UPF上开启媒体中继功能进行调测，或调测完成后删除拨测用户时，可以参考本章节进行配置。
risk_level: ''
doc_source: ["特性部署","业务专题","5G Core 媒体中继解决方案","媒体中继业务配置","新建媒体中继基础配置","配置UPF","基于拨测用户设置媒体中继业务开关"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
当SMF无法下发媒体中继用户标识及规则的场景下，需要基于拨测用户在UPF上开启媒体中继功能进行调测，或调测完成后删除拨测用户时，可以参考本章节进行配置。

## 必备事项
前提条件

已完成媒体中继业务增加媒体中继全局配置~开启媒体中继业务总开关的相关配置。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    add_relaytestuser_list:
      type: items
      properties:
        TESTUSERNAME:
          name: '拨测用户名称'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        APNNAME:
          name: 'APN名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '此APN为测试用户所在的APN。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        USERTYPE:
          name: '用户类型'
          type: string
          enum:
          - IMSI
          - MSISDN
          required: true
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        IMSI:
          name: 'IMSI'
          type: string
          minLength: 0
          maxLength: 15
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        RELAYFUNC:
          name: '媒体中继功能开关'
          type: string
          enum:
          - Disable
          - Enable
          required: true
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: ''
        USERPROFILENAME:
          name: '用户模板名称'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: '该规则与SMF下发的规则保持一致。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        MSISDN:
          name: 'MSISDN'
          type: string
          minLength: 0
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    rmv_relaytestuser_list:
      type: items
      properties:
        TESTUSERNAME:
          name: '拨测用户名称'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: '已通过**ADD RELAYTESTUSER**配置。'
          data_source: '本端规划'
          pattern: ''
          default: ''
  examples:
    add_relaytestuser_list:
    - TESTUSERNAME: 'relaytestuser01'
      APNNAME: 'huawei.com'
      USERTYPE: IMSI
      IMSI: '460011223344551'
      RELAYFUNC: Enable
      USERPROFILENAME: 'testuserprofilename'
      MSISDN: ''
    rmv_relaytestuser_list:
    - TESTUSERNAME: 'relaytestuser01'
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 增加媒体中继拨测用户。

```jinja2
{%- for item in add_relaytestuser_list -%}
    ADD RELAYTESTUSER:
    {#- --- 必选参数 --- -#}
    TESTUSERNAME="{{item.TESTUSERNAME}}",
    APNNAME="{{item.APNNAME}}",
    USERTYPE={{item.USERTYPE}},
    RELAYFUNC={{item.RELAYFUNC}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：USERTYPE=IMSI 时必选 --- -#}
    {%- if item.USERTYPE == 'IMSI' -%}
        IMSI="{{item.IMSI}}",
    {%- endif -%}
    {#- --- 条件必选：RELAYFUNC=Enable 时必选 --- -#}
    {%- if item.RELAYFUNC == 'Enable' -%}
        USERPROFILENAME="{{item.USERPROFILENAME}}",
    {%- endif -%}
    {#- --- 条件必选：USERTYPE=MSISDN 时必选 --- -#}
    {%- if item.USERTYPE == 'MSISDN' -%}
        MSISDN="{{item.MSISDN}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 2 调测完成后，删除拨测用户。

```jinja2
{%- for item in rmv_relaytestuser_list -%}
    RMV RELAYTESTUSER:
    {#- --- 必选参数 --- -#}
    TESTUSERNAME="{{item.TESTUSERNAME}}",
    ;
{%- endfor -%}
```


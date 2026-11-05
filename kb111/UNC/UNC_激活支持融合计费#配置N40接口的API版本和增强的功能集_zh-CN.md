---
id: ''
name: 配置N40接口的API版本和增强的功能集
ne_type: UNC
type: feature
description: 3GPP TS 32291协议定义的SMF的N40接口API版本不断演进，不同运营商对N40接口有不同的协议版本要求，部分运营商还有在指定基础协议版本基础上跟进后续协议版本的要求。  SMF支持根据现网实际情况配置指定N40接口支持的协议版本，并支持在该协议版本基础上叠加指定的增加功能。  适用于SMF。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","计费管理功能","WSFD-011206 支持融合计费","激活支持融合计费","配置N40接口的API版本和增强的功能集"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
3GPP TS 32291协议定义的SMF的N40接口API版本不断演进，不同运营商对N40接口有不同的协议版本要求，部分运营商还有在指定基础协议版本基础上跟进后续协议版本的要求。SMF支持根据现网实际情况配置指定N40接口支持的协议版本，并支持在该协议版本基础上叠加指定的增加功能。适用于SMF。

## 必备事项
前提条件

* 请仔细阅读融合计费原理。
* 完成加载License。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    set_n40apiver_list:
      type: items
      properties:
        APIVER:
          name: 'API接口版本'
          type: string
          enum:
          - F30
          - F40
          required: true
          description: '配置N40接口支持的API版本，需和CHF使用相同的协议版本。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        FEATURE:
          name: '特性'
          type: string
          required: false
          description: '配置N40接口增强的功能，需和CHF使用相同的接口能力。  该参数类型为位域类型，支持取值叠加进行选择，功能使能时参数后携带-1，不使能时参数后携带-0，如果不修改对应功能，无需携带对应参数，详细可参考任务示例。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_n40msgtemp_list:
      type: items
      properties:
        TEMPLATENAME:
          name: 'N40消息属性模板名'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '指定N40消息字段模板名。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        NBEXTENDATTR:
          name: 'NB扩展属性'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: false
          description: '控制NB-IOT、LTEM接入时是否携带扩展属性信息，包括APN Rate Control、Serving PLMN Rate Control、CP only indication和PtP隧道。'
          data_source: '本端规划'
          pattern: ''
          default: ENABLE
  examples:
    set_n40apiver_list:
    - APIVER: F30
      FEATURE: NODEFUNC-1
    add_n40msgtemp_list:
    - TEMPLATENAME: 'n40attr'
      NBEXTENDATTR: ENABLE
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 进入“MML命令行-UNC”窗口。

### 2 配置N40接口支持的API版本及增强功能集。

```jinja2
{%- for item in set_n40apiver_list -%}
    SET N40APIVER:
    {#- --- 必选参数 --- -#}
    APIVER={{item.APIVER}},
    {#- --- 可选参数 --- -#}
    {%- if item.FEATURE is not none -%}
        FEATURE={{item.FEATURE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 配置N40消息属性模板，控制N40消息中是否携带对应字段。

```jinja2
{%- for item in add_n40msgtemp_list -%}
    ADD N40MSGTEMP:
    {#- --- 必选参数 --- -#}
    TEMPLATENAME="{{item.TEMPLATENAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.NBEXTENDATTR is not none -%}
        NBEXTENDATTR={{item.NBEXTENDATTR}},
    {%- endif -%}
    ;
{%- endfor -%}
```


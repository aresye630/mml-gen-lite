---
id: ''
name: 激活动态分流规则下发
ne_type: UEG
type: feature
description: 在不同场景下或针对不同运营商，支持两种方式下发动态Traffic Rule和动态DNS Rule。通过**SET MPFATTR**命令设置MPF属性配置，即管理面MEPM和MPF之间的Mm5接口可以处理的消息类型，从而设置不同的下发方式，两种场景不会同时存在：  * “MM5MSGTYPE”参数配置为APPD：表示管理面MEPM向MPF下发规则的模式是APPD（APP Descriptor）模式，Mm5接口的一条HTTPS请求消息中的APPD包含一个APP实例的动态Traffic Rule、动态DNS Rule、APP依赖的服务和APP提供的服务等信息。 * “MM5MSGTYPE”参数配置为SPEC\_RULE：表示管理面MEPM向MPF下发规则的模式是指定Rule模式，Mm5接口的一条HTTPS请求消息中仅包含一个APP实例的动态Traffic Rule或者动态DNS Rule。  适用于MPF。
tags: []
risk_level: ''
doc_source: ["网络部署","园区入驻+地市共享（连接+计算）","5GC toB 部署边缘站点（站点为“风筝S”，带计算）","配置业务数据（风筝S）","APP集成管理功能","配置MPF","激活动态分流规则下发（MPF）","激活动态分流规则下发"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
在不同场景下或针对不同运营商，支持两种方式下发动态Traffic Rule和动态DNS Rule。通过**SET MPFATTR**命令设置MPF属性配置，即管理面MEPM和MPF之间的Mm5接口可以处理的消息类型，从而设置不同的下发方式，两种场景不会同时存在：* “MM5MSGTYPE”参数配置为APPD：表示管理面MEPM向MPF下发规则的模式是APPD（APP Descriptor）模式，Mm5接口的一条HTTPS请求消息中的APPD包含一个APP实例的动态Traffic Rule、动态DNS Rule、APP依赖的服务和APP提供的服务等信息。* “MM5MSGTYPE”参数配置为SPEC\_RULE：表示管理面MEPM向MPF下发规则的模式是指定Rule模式，Mm5接口的一条HTTPS请求消息中仅包含一个APP实例的动态Traffic Rule或者动态DNS Rule。适用于MPF。

## 必备事项
前提条件

请仔细阅读动态分流规则下发。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    set_mpfattr_list:
      type: items
      properties:
        MM5MSGTYPE:
          name: 'Mm5接口消息类型'
          type: string
          enum:
          - APPD
          - SPEC_RULE
          required: true
          description: '* APPD：表示Mm5接口处理的消息类型的Rule模式为APPD模式。 * SPEC\_RULE：表示Mm5接口处理的消息类型的Rule模式为指定Rule模式。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        MEPID:
          name: 'MEP ID'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: '* 该参数在“MM5MSGTYPE”配置为“SPEC\_RULE”时不需要配置，因为Mm5接口下发指定Rule时会携带MEP ID信息。 * 该参数在“MM5MSGTYPE”配置为“APPD”时为可选参数，用于配置MEP ID信息，如果不配置则表示使用默认值mpf。'
          data_source: '全网规划'
          pattern: ''
          default: ''
  examples:
    set_mpfattr_list:
    - MM5MSGTYPE: APPD
      MEPID: 'mepid'
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 设置MPF属性配置。

```jinja2
{%- for item in set_mpfattr_list -%}
    SET MPFATTR:
    {#- --- 必选参数 --- -#}
    MM5MSGTYPE={{item.MM5MSGTYPE}},
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：MM5MSGTYPE=APPD 时可选 --- -#}
    {%- if item.MM5MSGTYPE == 'APPD' -%}
        {%- if item.MEPID is not none -%}
            MEPID="{{item.MEPID}}",
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 该命令属于高危命令，“Mm5接口消息类型”的APPD类型和指定SPEC\_RULE类型互斥，配置成功后会导致另一种类型消息不作处理，请谨慎执行。“Mm5接口消息类型”默认配置为APPD。


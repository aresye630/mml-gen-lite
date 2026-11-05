---
id: ''
name: 激活动态分流规则状态
ne_type: UEG
type: feature
description: 动态Traffic Rule和动态DNS Rule在MPF上存在两种状态：ACTIVE（激活状态）、INACTIVE（去激活状态）。在不同场景下或针对不同运营商，支持如下两种方式下发动态Traffic Rule和动态DNS Rule：  1. 第三方管理平台通过MEPM向MPF动态Traffic Rule时，下发的动态Traffic Rule全部是ACTIVE状态。 2. 管理面MEAO/MEPM下发的动态Traffic Rule保存在MPF上时初始状态均被置为INACTIVE。  上述两种下发方式下，MPF均支持通过MPF本地配置的命令修改动态Traffic Rule和动态DNS Rule状态：  * 通过**ACT TRAFFICRULE**命令将动态Traffic Rule的状态从INACTIVE修改为ACTIVE；通过**DEA TRAFFICRULE**命令将动态Traffic Rule的状态从ACTIVE修改为INACTIVE。 * 通过**ACT DNSRULE**命令将动态DNS Rule的状态从INACTIVE修改为ACTIVE；通过**DEA DNSRULE**命令将动态DNS Rule的状态从ACTIVE修改为INACTIVE。  适用于MPF。
tags: []
risk_level: ''
doc_source: ["网络部署","园区入驻+地市共享（连接+计算）","5GC toB 部署边缘站点（站点为“风筝S”，带计算）","配置业务数据（风筝S）","APP集成管理功能","配置MPF","激活动态分流规则下发（MPF）","激活动态分流规则状态"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
动态Traffic Rule和动态DNS Rule在MPF上存在两种状态：ACTIVE（激活状态）、INACTIVE（去激活状态）。在不同场景下或针对不同运营商，支持如下两种方式下发动态Traffic Rule和动态DNS Rule：1. 第三方管理平台通过MEPM向MPF动态Traffic Rule时，下发的动态Traffic Rule全部是ACTIVE状态。2. 管理面MEAO/MEPM下发的动态Traffic Rule保存在MPF上时初始状态均被置为INACTIVE。上述两种下发方式下，MPF均支持通过MPF本地配置的命令修改动态Traffic Rule和动态DNS Rule状态：* 通过**ACT TRAFFICRULE**命令将动态Traffic Rule的状态从INACTIVE修改为ACTIVE；通过**DEA TRAFFICRULE**命令将动态Traffic Rule的状态从ACTIVE修改为INACTIVE。* 通过**ACT DNSRULE**命令将动态DNS Rule的状态从INACTIVE修改为ACTIVE；通过**DEA DNSRULE**命令将动态DNS Rule的状态从ACTIVE修改为INACTIVE。适用于MPF。

## 必备事项
前提条件

请仔细阅读Traffic Rule状态激活和DNS Rule状态激活。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    act_dnsrule_list:
      type: items
      properties:
        RULETYPE:
          name: '规则类型'
          type: string
          enum:
          - DYNAMIC
          - STATIC
          required: true
          description: '激活指定APP名称，APP实例和DNS规则ID的动态DNS Rule。  当“RULETYPE”配置为“STATIC”，表示激活静态DNS Rule。  当“RULETYPE”配置为“DYNAMIC”，表示激活动态DNS Rule。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        APPNAME:
          name: '应用名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        APPINSTANCEID:
          name: 'APP实例号'
          type: string
          minLength: 0
          maxLength: 32
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        DNSRULEID:
          name: 'DNS规则ID'
          type: string
          minLength: 0
          maxLength: 95
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    dea_dnsrule_list:
      type: items
      properties:
        RULETYPE:
          name: '规则类型'
          type: string
          enum:
          - DYNAMIC
          - STATIC
          required: true
          description: '去激活指定APP名称，APP实例和DNS规则ID的动态DNS Rule。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        APPNAME:
          name: '应用名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        APPINSTANCEID:
          name: 'APP实例号'
          type: string
          minLength: 0
          maxLength: 32
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        DNSRULEID:
          name: 'DNS规则ID'
          type: string
          minLength: 0
          maxLength: 95
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    act_trafficrule_list:
      type: items
      properties:
        APPNAME:
          name: '应用名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '激活动态Traffic Rule。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        APPINSTANCEID:
          name: 'APP实例号'
          type: string
          minLength: 0
          maxLength: 32
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        TRAFFICRULEID:
          name: '流规则ID'
          type: string
          minLength: 0
          maxLength: 95
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    dea_trafficrule_list:
      type: items
      properties:
        APPNAME:
          name: '应用名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '去激活动态Traffic Rule。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        APPINSTANCEID:
          name: 'APP实例号'
          type: string
          minLength: 0
          maxLength: 32
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        TRAFFICRULEID:
          name: '流规则ID'
          type: string
          minLength: 0
          maxLength: 95
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    act_rulesyn_list:
      type: items
      properties: {}
  examples:
    act_dnsrule_list:
    - RULETYPE: DYNAMIC
      APPNAME: 'app1'
      APPINSTANCEID: 'appInstanceId1'
      DNSRULEID: 'rule1'
    dea_dnsrule_list:
    - RULETYPE: DYNAMIC
      APPNAME: 'app1'
      APPINSTANCEID: 'appInstanceId1'
      DNSRULEID: 'rule1'
    act_trafficrule_list:
    - APPNAME: 'appName_1'
      APPINSTANCEID: 'appInstanceId_1'
      TRAFFICRULEID: 'trafficRuleId_0'
    dea_trafficrule_list:
    - APPNAME: 'appName_1'
      APPINSTANCEID: 'appInstanceId_1'
      TRAFFICRULEID: 'trafficRuleId_0'
    act_rulesyn_list:
    - {}
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 **可选：**激活DNS Rule。

```jinja2
{%- if is_optional_activate_dns_rule -%}
    {%- for item in act_dnsrule_list -%}
        ACT DNSRULE:
        {#- --- 必选参数 --- -#}
        RULETYPE={{item.RULETYPE}},
        APPNAME="{{item.APPNAME}}",
        {#- --- 可选参数 --- -#}
        {%- if item.DNSRULEID is not none -%}
            DNSRULEID="{{item.DNSRULEID}}",
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：RULETYPE=DYNAMIC 时可选 --- -#}
        {%- if item.RULETYPE == 'DYNAMIC' -%}
            {%- if item.APPINSTANCEID is not none -%}
                APPINSTANCEID="{{item.APPINSTANCEID}}",
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### MPF支持激活动态DNS Rule状态。

### MPF基于appName粒度激活动态DNS Rule时，该指定appName下所有动态DNS Rule的状态将置为ACTIVE。

### MPF基于appName和appInstanceId粒度激活动态DNS Rule时，该指定appName和appInstanceId下所有动态DNS Rule的状态将置为ACTIVE。

### MPF基于appName和DNS Rule ID粒度激活动态DNS Rule时，该指定appName下所有指定DNS Rule ID的动态DNS Rule的状态将置为ACTIVE。

### MPF基于appName、appInstanceId和DNS Rule ID粒度激活动态DNS Rule，该指定appName、appInstanceId下指定DNS Rule ID的动态DNS Rule的状态将置为ACTIVE，该场景仅激活一条DNS Rule。

### MPF支持在MPF上的**SET DNSLITEPARA**命令的“DNSRULESTATSW”参数配置为“ENABLE”时，激活静态DNS Rule状态。

### MPF基于appName粒度激活静态DNS Rule时，该指定appName下所有静态DNS Rule的状态将置为ACTIVE。

### MPF基于appName和DNS Rule ID粒度激活静态DNS Rule时，该指定appName下指定静态DNS Rule的状态将置为ACTIVE。

### 2 **可选：**去激活DNS Rule。

```jinja2
{%- if is_optional_deactivate_dns_rule -%}
    {%- for item in dea_dnsrule_list -%}
        DEA DNSRULE:
        {#- --- 必选参数 --- -#}
        RULETYPE={{item.RULETYPE}},
        APPNAME="{{item.APPNAME}}",
        {#- --- 可选参数 --- -#}
        {%- if item.DNSRULEID is not none -%}
            DNSRULEID="{{item.DNSRULEID}}",
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：RULETYPE=DYNAMIC 时可选 --- -#}
        {%- if item.RULETYPE == 'DYNAMIC' -%}
            {%- if item.APPINSTANCEID is not none -%}
                APPINSTANCEID="{{item.APPINSTANCEID}}",
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 3 **可选：**激活动态Traffic Rule。

```jinja2
{%- if is_optional_activate_traffic_rule -%}
    {%- for item in act_trafficrule_list -%}
        ACT TRAFFICRULE:
        {#- --- 必选参数 --- -#}
        APPNAME="{{item.APPNAME}}",
        {#- --- 可选参数 --- -#}
        {%- if item.APPINSTANCEID is not none -%}
            APPINSTANCEID="{{item.APPINSTANCEID}}",
        {%- endif -%}
        {%- if item.TRAFFICRULEID is not none -%}
            TRAFFICRULEID="{{item.TRAFFICRULEID}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### MPF基于appName粒度激活动态Traffic Rule时，该指定appName下所有动态Traffic Rule的状态将置为ACTIVE。

### MPF基于appName和appInstanceId粒度激活动态Traffic Rule时，该指定appName和appInstanceId下所有动态Traffic Rule的状态将置为ACTIVE。

### MPF基于appName和Traffic Rule ID粒度激活动态Traffic Rule时，该指定appName下所有指定Traffic Rule ID的动态Traffic Rule的状态将置为ACTIVE。

### MPF基于appName、appInstanceId和Traffic Rule ID粒度激活动态Traffic Rule，该指定appName、appInstanceId下指定Traffic Rule ID的动态Traffic Rule的状态将置为ACTIVE，该场景仅激活一条Traffic Rule。

### 4 **可选：**去激活动态Traffic Rule。

```jinja2
{%- if is_optional_deactivate_traffic_rule -%}
    {%- for item in dea_trafficrule_list -%}
        DEA TRAFFICRULE:
        {#- --- 必选参数 --- -#}
        APPNAME="{{item.APPNAME}}",
        {#- --- 可选参数 --- -#}
        {%- if item.APPINSTANCEID is not none -%}
            APPINSTANCEID="{{item.APPINSTANCEID}}",
        {%- endif -%}
        {%- if item.TRAFFICRULEID is not none -%}
            TRAFFICRULEID="{{item.TRAFFICRULEID}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 5 **可选：**用于特殊场景主动推送激活态的分流规则。

```jinja2
{%- if is_optional_push_active_traffic_rules -%}
    ACT RULESYN:
    ;
{%- endif -%}
```


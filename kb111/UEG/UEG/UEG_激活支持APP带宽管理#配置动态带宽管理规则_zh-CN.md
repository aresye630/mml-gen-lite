---
id: ''
name: 配置动态带宽管理规则
ne_type: UEG
type: feature
description: 当APP通过Mp1接口/管理面MEPM通过Mm5接口下发动态带宽管理规则，用于管理访问APP的上下行带宽时，需要配置本页面，将动态带宽管理规则激活生效。  适用于MPF。
tags: []
risk_level: ''
doc_source: ["业务配置","公共业务","MEC APP业务访问控制（公共）","分流后带宽控制（MPF）","激活支持APP带宽管理","配置动态带宽管理规则"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
当APP通过Mp1接口/管理面MEPM通过Mm5接口下发动态带宽管理规则，用于管理访问APP的上下行带宽时，需要配置本页面，将动态带宽管理规则激活生效。适用于MPF。

## 必备事项
前提条件

* 请仔细阅读带宽管理规则的获取和执行和增/删/改/查动态带宽管理规则。
* 已完成配置Mp1接口数据。
* 已完成加载License。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    set_licenseswitch_list:
      type: items
      properties:
        LICITEM:
          name: 'License项'
          type: string
          minLength: 0
          maxLength: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SWITCH:
          name: '开关'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_dnslitepara_list:
      type: items
      properties:
        DNSLMATCHSW:
          name: '轻量DNS规则匹配开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '本参数配置为“ENABLE”后，表示开启DNS Rule开关，支持DNS Rule匹配功能。动态DNS Rule和静态DNS Rule均支持。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        DNSLPOLICYSW:
          name: '轻量DNS策略执行开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '本参数配置为“ENABLE”后，如果DNS Rule匹配成功，则支持UE发起DNS查询并响应。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_apptrafficpara_list:
      type: items
      properties:
        TRAFFICRULESW:
          name: '应用流量规则开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: true
          description: '打开应用流量规则开关。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        RULESOURCE:
          name: '规则来源'
          type: string
          enum:
          - DNS_RULE_EXTENDED
          - DYNAMIC_TRAFFIC_RULE
          required: false
          description: '* 当“规则来源”设置为“DYNAMIC\_TRAFFIC\_RULE”，表示使用动态Traffic Rule进行规则匹配，携带IP地址的数据报文命中动态Traffic Rule进行本地分流。 * 当“规则来源”设置为“DNS\_RULE\_EXTENDED”，表示使用DNS Rule衍生的IP地址匹配，携带IP地址的数据报文命中DNS Rule的IP地址进行本地分流。   说明：  基于动态Traffic Rule的分流功能和DNS Rule衍生的基于目的IP的本地分流功能不能同时生效。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_apppolicypara_list:
      type: items
      properties:
        BWALLOCATION:
          name: '应用带宽策略开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '配置为“ENABLE”后，支持基于动态分流的带宽控制功能。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_qoscarburst_list:
      type: items
      properties:
        RATE:
          name: 'Qos-Car速率（千比特/秒）'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: true
          description: '指定速率，该参数一般由运营商规划给出。'
          data_source: '本端规划'
          pattern: ''
          default: 0
        BURSTTYPE:
          name: '突发尺寸类型'
          type: string
          enum:
          - Auto_Calculate
          - BYTE
          required: true
          description: '指定流量的突发尺寸的计算类型。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        DURATION:
          name: '自动计算时长（毫秒）'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: '配置duration-milliseconds，表示突发尺寸为流量的速率与duration-milliseconds的乘积。'
          data_source: '本端规划'
          pattern: ''
          default: ''
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV3G5BWMF01'
      SWITCH: ENABLE
    set_dnslitepara_list:
    - DNSLMATCHSW: ENABLE
      DNSLPOLICYSW: ENABLE
    set_apptrafficpara_list:
    - TRAFFICRULESW: ENABLE
      RULESOURCE: DYNAMIC_TRAFFIC_RULE
    set_apppolicypara_list:
    - BWALLOCATION: ENABLE
    add_qoscarburst_list:
    - RATE: 128
      BURSTTYPE: Auto_Calculate
      DURATION: 1000
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 打开本特性的License配置开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

### 2 配置使能动态DNS Rule进行业务匹配。

```jinja2
{%- for item in set_dnslitepara_list -%}
    SET DNSLITEPARA:
    {#- --- 可选参数 --- -#}
    {%- if item.DNSLMATCHSW is not none -%}
        DNSLMATCHSW={{item.DNSLMATCHSW}},
    {%- endif -%}
    {%- if item.DNSLPOLICYSW is not none -%}
        DNSLPOLICYSW={{item.DNSLPOLICYSW}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 配置使能动态Traffic Rule进行业务匹配。

```jinja2
{%- for item in set_apptrafficpara_list -%}
    SET APPTRAFFICPARA:
    {#- --- 必选参数 --- -#}
    TRAFFICRULESW={{item.TRAFFICRULESW}},
    {#- --- 可选参数 --- -#}
    {%- if item.RULESOURCE is not none -%}
        RULESOURCE={{item.RULESOURCE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 打开带宽管理策略开关，根据命中的Traffic Rule查找相同appName的带宽管理规则。

```jinja2
{%- for item in set_apppolicypara_list -%}
    SET APPPOLICYPARA:
    {#- --- 可选参数 --- -#}
    {%- if item.BWALLOCATION is not none -%}
        BWALLOCATION={{item.BWALLOCATION}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 5 配置用户做car的参数。

```jinja2
{%- for item in add_qoscarburst_list -%}
    ADD QOSCARBURST:
    {#- --- 必选参数 --- -#}
    RATE={{item.RATE}},
    BURSTTYPE={{item.BURSTTYPE}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：BURSTTYPE=Auto_Calculate 时必选 --- -#}
    {%- if item.BURSTTYPE == 'Auto_Calculate' -%}
        DURATION={{item.DURATION}},
    {%- endif -%}
    ;
{%- endfor -%}
```


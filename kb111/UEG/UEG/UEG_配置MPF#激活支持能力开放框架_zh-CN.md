---
id: ''
name: 激活支持能力开放框架
ne_type: UEG
type: feature
description: 当MPF通过API GW对APP开放网络能力，APP通过调用API接口访问MPF内部服务时，需要配置本页面相关功能。  适用于MPF。
tags: []
risk_level: ''
doc_source: ["网络部署","园区入驻+地市共享（连接+计算）","5GC toB 部署边缘站点（站点为“风筝S”，带计算）","配置业务数据（风筝S）","APP集成管理功能","配置MPF","激活支持能力开放框架"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
当MPF通过API GW对APP开放网络能力，APP通过调用API接口访问MPF内部服务时，需要配置本页面相关功能。适用于MPF。

## 必备事项
前提条件

* 请仔细阅读GWFD-023502 支持能力开放框架特性概述。
* 虚机场景：完成配置Mp1接口数据。
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
    set_ratelimit_list:
      type: items
      properties:
        RATELIMIT_TYPE:
          name: '流控类型'
          type: string
          enum:
          - GLOBAL
          - SINGLE
          required: true
          description: '配置全局API GW访问次数控制。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SECOND:
          name: '每秒请求限制'
          type: integer
          minimum: 0
          maximum: 2147483647
          required: false
          description: '控制APP单位时间内对API GW的访问频率。'
          data_source: '本端规划'
          pattern: ''
          default: ''
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV3G5APIG01'
      SWITCH: ENABLE
    set_ratelimit_list:
    - RATELIMIT_TYPE: GLOBAL
      SECOND: 5000
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

### 2 **可选：**配置限流策略，控制APP单位时间内对API GW的访问频率。

```jinja2
{%- if is_optional_rate_limit_policy -%}
    {%- for item in set_ratelimit_list -%}
        SET RATELIMIT:
        {#- --- 必选参数 --- -#}
        RATELIMIT_TYPE={{item.RATELIMIT_TYPE}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：RATELIMIT_TYPE=SINGLE/GLOBAL 时必选 --- -#}
        {%- if item.RATELIMIT_TYPE in ['SINGLE', 'GLOBAL'] -%}
            SECOND={{item.SECOND}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```


---
id: GWFD-023502
name: 激活支持能力开放框架
ne_type: UEG
type: feature
description: 当UEG通过API GW对消费者开放网络能力，消费者通过调用API接口访问UEG内部服务时，需要配置本页面相关功能。  适用于PGW-U、UPF。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝L","MEC 特性指南（风筝L）","GW-U&UPF特性指南","GWFD-023500 支持APP集成管理（适用于虚机场景）","GWFD-023502 支持能力开放框架","GWFD-023502 支持能力开放框架（适用于PGW-U/UPF）","激活支持能力开放框架"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
当UEG通过API GW对消费者开放网络能力，消费者通过调用API接口访问UEG内部服务时，需要配置本页面相关功能。适用于PGW-U、UPF。

## 必备事项
前提条件

* 请仔细阅读GWFD-023502 支持能力开放框架（适用于PGW-U/UPF）。
* 已完成加载License。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
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
          description: '控制消费者单位时间内对API GW的访问频率。'
          data_source: '本端规划'
          pattern: ''
          default: ''
  examples:
    set_ratelimit_list:
    - RATELIMIT_TYPE: GLOBAL
      SECOND: 5000
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 **可选：**配置限流策略，控制消费者单位时间内对API GW的访问频率。

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


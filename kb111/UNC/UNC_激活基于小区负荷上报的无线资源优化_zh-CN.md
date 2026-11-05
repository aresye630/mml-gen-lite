---
id: ''
name: 激活基于小区负荷上报的无线资源优化
ne_type: UNC
type: feature
description: 某些小区出现拥塞且不扩容，运营商规划基于小区负荷状态对某些用户或某些业务进行策略控制，从而解除/减缓小区拥塞状态时，需要激活基于小区负荷上报的无线资源优化功能。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","智能PCC解决方案","WSFD-211101 基于小区负荷上报的无线资源优化","激活基于小区负荷上报的无线资源优化"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
某些小区出现拥塞且不扩容，运营商规划基于小区负荷状态对某些用户或某些业务进行策略控制，从而解除/减缓小区拥塞状态时，需要激活基于小区负荷上报的无线资源优化功能。

## 必备事项
前提条件

* 请仔细阅读WSFD-211101 基于小区负荷上报的无线资源优化和PCC基本功能（2G/3G/4G，基于Gx接口）。
* 完成激活PCC基本功能。
* 完成加载License（如果有需求，请联系华为技术支持工程师处理）。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
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
    set_apnreportattr_list:
      type: items
      properties:
        APN:
          name: 'APN'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '使能基于APN的小区拥塞上报功能。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        CONGESTIONRPT:
          name: '拥塞控制'
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
    set_licenseswitch_list:
    - LICITEM: 'LKV3W9WOCR11'
      SWITCH: ENABLE
    set_apnreportattr_list:
    - APN: 'apn1'
      CONGESTIONRPT: ENABLE
```

## 3 命令模板定义
<!-- @mml:block=commands -->

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

### 2 使能基于APN的小区拥塞上报功能。

```jinja2
{%- for item in set_apnreportattr_list -%}
    SET APNREPORTATTR:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    {#- --- 可选参数 --- -#}
    {%- if item.CONGESTIONRPT is not none -%}
        CONGESTIONRPT={{item.CONGESTIONRPT}},
    {%- endif -%}
    ;
{%- endfor -%}
```


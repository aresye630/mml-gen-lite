---
id: ''
name: 配置AMF惯性运行数据
ne_type: UEG
type: feature
description: 用户面业务通道保活是指，企业园区场景下，当园区gNodeB、UPF跟园区外部署的AMF、SMF失联时，即N2/N4接口不可用但N3接口可用时，弱移动性（不跨gNodeB切换）连接态用户的数传业务能够继续进行（惯性运行）。  适用于AMF。
tags: []
risk_level: ''
doc_source: ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（火电专网，入驻式）","部署配置指导","子园区部署入驻式UEG-M","配置业务数据（风筝M）","惯性运行配置（中心园区控制面）","配置AMF惯性运行数据"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
用户面业务通道保活是指，企业园区场景下，当园区gNodeB、UPF跟园区外部署的AMF、SMF失联时，即N2/N4接口不可用但N3接口可用时，弱移动性（不跨gNodeB切换）连接态用户的数传业务能够继续进行（惯性运行）。适用于AMF。

## 必备事项
前提条件

* 请仔细阅读WSFD-217001 用户面业务通道保活特性概述。
* 完成加载License。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    add_dnngrp_list:
      type: items
      properties:
        DNNGRPID:
          name: 'DNN群组标识'
          type: string
          minLength: 1
          maxLength: 32
          required: true
          description: '为具有相同属性的DNN配置到同一个群组。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_dnngrpmem_list:
      type: items
      properties:
        DNNGRPID:
          name: 'DNN群组标识'
          type: string
          minLength: 1
          maxLength: 32
          required: true
          description: '为DNN群组添加DNN成员。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        DNN:
          name: 'DNN'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_areacode_list:
      type: items
      properties:
        AREACODE:
          name: '区域编码'
          type: string
          minLength: 1
          maxLength: 128
          required: true
          description: '增加区域编码，基于运营商规划的区域做差异化控制。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_areamem_list:
      type: items
      properties:
        AREACODE:
          name: '区域编码'
          type: string
          minLength: 1
          maxLength: 128
          required: true
          description: '为指定的区域增加跟踪区成员。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        MCC:
          name: 'MCC'
          type: string
          minLength: 3
          maxLength: 3
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MNC:
          name: 'MNC'
          type: string
          minLength: 2
          maxLength: 3
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        BGNTAC:
          name: '跟踪区编码起始值'
          type: string
          minLength: 6
          maxLength: 6
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ENDTAC:
          name: '跟踪区编码结束值'
          type: string
          minLength: 6
          maxLength: 6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_ngparkplcy_list:
      type: items
      properties:
        PARKID:
          name: '园区标识'
          type: string
          minLength: 1
          maxLength: 32
          required: true
          description: '该命令用于增加园区策略，设置园区惯性运行开关。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        AREACODE:
          name: '区域编码'
          type: string
          minLength: 1
          maxLength: 128
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DNNGRPID:
          name: 'DNN群组标识'
          type: string
          minLength: 1
          maxLength: 32
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        INERTIA:
          name: '惯性运行开关'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: OFF
  examples:
    add_dnngrp_list:
    - DNNGRPID: '1'
    add_dnngrpmem_list:
    - DNNGRPID: '1'
      DNN: 'DNNa'
    add_areacode_list:
    - AREACODE: '1'
    add_areamem_list:
    - AREACODE: '1'
      MCC: '460'
      MNC: '03'
      BGNTAC: '120101'
      ENDTAC: '999999'
    add_ngparkplcy_list:
    - PARKID: 'park'
      AREACODE: 'huawei'
      DNNGRPID: 'BIG_GROUP'
      INERTIA: ON
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 进入“MML命令行-UEG”窗口。

### 2 配置DNN群组。

```jinja2
{%- for item in add_dnngrp_list -%}
    ADD DNNGRP:
    {#- --- 必选参数 --- -#}
    DNNGRPID="{{item.DNNGRPID}}",
    ;
{%- endfor -%}
```

### 3 为DNN群组添加DNN成员。

```jinja2
{%- for item in add_dnngrpmem_list -%}
    ADD DNNGRPMEM:
    {#- --- 必选参数 --- -#}
    DNNGRPID="{{item.DNNGRPID}}",
    DNN="{{item.DNN}}",
    ;
{%- endfor -%}
```

### 4 增加区域编码。

```jinja2
{%- for item in add_areacode_list -%}
    ADD AREACODE:
    {#- --- 必选参数 --- -#}
    AREACODE="{{item.AREACODE}}",
    ;
{%- endfor -%}
```

### 5 为指定的区域增加跟踪区成员。

```jinja2
{%- for item in add_areamem_list -%}
    ADD AREAMEM:
    {#- --- 必选参数 --- -#}
    AREACODE="{{item.AREACODE}}",
    MCC="{{item.MCC}}",
    MNC="{{item.MNC}}",
    BGNTAC="{{item.BGNTAC}}",
    {#- --- 可选参数 --- -#}
    {%- if item.ENDTAC is not none -%}
        ENDTAC="{{item.ENDTAC}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 6 **可选：**增加园区策略，设置园区惯性运行开关。

```jinja2
{%- if is_optional_add_park_policy -%}
    {%- for item in add_ngparkplcy_list -%}
        ADD NGPARKPLCY:
        {#- --- 必选参数 --- -#}
        PARKID="{{item.PARKID}}",
        AREACODE="{{item.AREACODE}}",
        DNNGRPID="{{item.DNNGRPID}}",
        {#- --- 可选参数 --- -#}
        {%- if item.INERTIA is not none -%}
            INERTIA={{item.INERTIA}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```


---
id: ''
name: 部署SMF选择ULCL合一策略增强
ne_type: UNC
type: feature
description: 为5G用户配置UL CL部署模式，从而实现UL CL合设锚点的选择可基于UE的位置灵活切换。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","MEC解决方案","WSFD-223005 SMF选择ULCL合一策略增强","部署SMF选择ULCL合一策略增强"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
为5G用户配置UL CL部署模式，从而实现UL CL合设锚点的选择可基于UE的位置灵活切换。

## 必备事项
前提条件

已开启UL CL分流相关功能特性：

* WSFD-107010 UPF选择
* WSFD-108002 基于预定义规则的分流策略控制
* WSFD-108001 动态分流策略控制
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    add_dnaiinfo_list:
      type: items
      properties:
        DNAI:
          name: '数据网络访问标识'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '打开ALWAYS分流开关。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        ALWAYSSHUNTSW:
          name: 'Always分流开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: DISABLE
    add_ulclareadpmode_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '增加指定DNAI服务区域粒度的ULCL部署模式为优先使用辅锚点分流。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        DNAI:
          name: '数据网络访问标识'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        DNAREANAME:
          name: 'DNAI服务区域名称'
          type: string
          minLength: 1
          maxLength: 255
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        ULCLDEPLOYMODE:
          name: 'ULCL部署模式'
          type: string
          enum:
          - AUXSHUNTPREFER
          - AUXSHUNTMUST
          - PSASHUNTMUST
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: AUXSHUNTPREFER
    add_ulcldnaidpmode_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '增加指定DNAI粒度的ULCL部署模式为只使用主锚点分流。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        DNAI:
          name: '数据网络访问标识'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        ULCLDEPLOYMODE:
          name: 'ULCL部署模式'
          type: string
          enum:
          - AUXSHUNTPREFER
          - AUXSHUNTMUST
          - PSASHUNTMUST
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: AUXSHUNTPREFER
    add_ulclapndpmode_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '指定APN名称后，增加指定DNN的ULCL部署模式为只使用主锚点分流。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        ULCLDEPLOYMODE:
          name: 'ULCL部署模式'
          type: string
          enum:
          - AUXSHUNTPREFER
          - AUXSHUNTMUST
          - PSASHUNTMUST
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: AUXSHUNTPREFER
  examples:
    add_dnaiinfo_list:
    - DNAI: 'huawei'
      ALWAYSSHUNTSW: ENABLE
    add_ulclareadpmode_list:
    - APN: 'huawei.com'
      DNAI: 'huawei'
      DNAREANAME: 'dnarea1'
      ULCLDEPLOYMODE: AUXSHUNTPREFER
    add_ulcldnaidpmode_list:
    - APN: 'huawei.com'
      DNAI: 'huawei'
      ULCLDEPLOYMODE: PSASHUNTMUST
    add_ulclapndpmode_list:
    - APN: 'huawei.com'
      ULCLDEPLOYMODE: PSASHUNTMUST
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 进入“MML命令行-UNC”窗口。

### 2 打开ALWAYS分流开关。

```jinja2
{%- for item in add_dnaiinfo_list -%}
    ADD DNAIINFO:
    {#- --- 必选参数 --- -#}
    DNAI="{{item.DNAI}}",
    {#- --- 可选参数 --- -#}
    {%- if item.ALWAYSSHUNTSW is not none -%}
        ALWAYSSHUNTSW={{item.ALWAYSSHUNTSW}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 增加指定DNAI服务区域的UL CL部署模式。

```jinja2
{%- for item in add_ulclareadpmode_list -%}
    ADD ULCLAREADPMODE:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    DNAI="{{item.DNAI}}",
    DNAREANAME="{{item.DNAREANAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.ULCLDEPLOYMODE is not none -%}
        ULCLDEPLOYMODE={{item.ULCLDEPLOYMODE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 增加指定DNAI的UL CL部署模式。

```jinja2
{%- for item in add_ulcldnaidpmode_list -%}
    ADD ULCLDNAIDPMODE:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    DNAI="{{item.DNAI}}",
    {#- --- 可选参数 --- -#}
    {%- if item.ULCLDEPLOYMODE is not none -%}
        ULCLDEPLOYMODE={{item.ULCLDEPLOYMODE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 5 增加指定APN的UL CL部署模式。

```jinja2
{%- for item in add_ulclapndpmode_list -%}
    ADD ULCLAPNDPMODE:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    {#- --- 可选参数 --- -#}
    {%- if item.ULCLDEPLOYMODE is not none -%}
        ULCLDEPLOYMODE={{item.ULCLDEPLOYMODE}},
    {%- endif -%}
    ;
{%- endfor -%}
```


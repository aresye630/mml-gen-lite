---
id: ''
name: 部署跨域业务漫游访问（正向分流）（SMF）
ne_type: UNC
type: feature
description: 本文档用于指导部署跨域业务漫游访问的正向分流方案。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","MEC解决方案","WSFD-228001 跨域业务访问","部署跨域业务漫游访问（正向分流）（SMF）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本文档用于指导部署跨域业务漫游访问的正向分流方案。

## 必备事项
前提条件

* 请仔细阅读WSFD-228001 跨域业务访问特性概述。
* 已完成本特性License（82200EDE LKV2SACDSA01 跨域业务访问）加载，可以通过**DSP LICENSE**命令查询确认，如果本特性的License在查询列表中可见，即可认为本特性License已加载成功。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    add_ulclprop_list:
      type: items
      properties:
        ULCLPROPNAME:
          name: 'ULCL属性名称'
          type: string
          maxLength: 63
          required: true
          description: '配置UL CL属性和DNAI的映射关系'
          data_source: '本端规划'
          pattern: ''
          default: ''
        DNAI:
          name: '数据网络访问标识符'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_dnaiinfo_list:
      type: items
      properties:
        DNAI:
          name: '数据网络访问标识符'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '配置正向分流DNAI信息'
          data_source: '全网规划'
          pattern: ''
          default: ''
        SHUNTDIRECT:
          name: '分流方向'
          type: string
          enum:
          - NORMAL
          - REVERSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NORMAL
        SHUNTLOC:
          name: '分流位置'
          type: string
          enum:
          - HOME
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: HOME
        ALWAYSSHUNTSW:
          name: 'Always分流开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
    add_apn_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '配置专用DNN Always的分流功能'
          data_source: '全网规划'
          pattern: ''
          default: ''
        ALWAYSPSAULCLSW:
          name: '主锚点Always分流开关'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
    add_apnupfinfo_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '配置专用DNN下主锚点+分流UPF位置特征'
          data_source: '全网规划'
          pattern: ''
          default: ''
        UPFINSTANCEID:
          name: 'UPF实例名称'
          type: string
          minLength: 1
          maxLength: 36
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LOCATION:
          name: 'UPF的位置特征'
          type: string
          enum:
          - INHERIT
          - BOTH
          - LOCALONLY
          - CENTERONLY
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: INHERIT
        PSACOMBINEULCL:
          name: '主锚点与分流节点合设功能'
          type: string
          enum:
          - INHERIT
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: INHERIT
    mod_upnode_list:
      type: items
      properties:
        NFINSTANCENAME:
          name: 'UPF实例名称'
          type: string
          minLength: 0
          maxLength: 255
          required: true
          description: '修改主锚点UPF属性为支持主锚点和分流UPF合设形态'
          data_source: '全网规划'
          pattern: ''
          default: ''
        LOCATION:
          name: 'UPF位置特征'
          type: string
          enum:
          - Local
          - Central
          - CentralOnly
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SUPULCLBPONLY:
          name: '是否仅支持作为分流UPF'
          type: string
          enum:
          - Disable
          - Enable
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PSACOMBINEULCL:
          name: '主锚点与分流节点合设功能'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_smffunc_list:
      type: items
      properties:
        IPV6LOCALUP:
          name: 'IPv6本地UP分流策略'
          type: string
          enum:
          - BpPrefer
          - UlClPrefer
          required: false
          description: '配置IPv6会话场景下的分流策略。  如果是IPv6会话，系统默认选择Bp分流模式，如果是UL CL分流需要修改配置。'
          data_source: '本端规划'
          pattern: ''
          default: ''
  examples:
    add_ulclprop_list:
    - ULCLPROPNAME: 'testulclpropname'
      DNAI: 'testdnai'
    add_dnaiinfo_list:
    - DNAI: 'testdnai'
      SHUNTDIRECT: NORMAL
      SHUNTLOC: HOME
      ALWAYSSHUNTSW: ENABLE
    add_apn_list:
    - APN: 'Huawei.com'
      ALWAYSPSAULCLSW: ENABLE
    add_apnupfinfo_list:
    - APN: 'Huawei.com'
      UPFINSTANCEID: 'UPF_INSTANCE0'
      LOCATION: INHERIT
      PSACOMBINEULCL: ENABLE
    mod_upnode_list:
    - NFINSTANCENAME: 'UPF_INSTANCE0'
      LOCATION: Central
      SUPULCLBPONLY: Disable
      PSACOMBINEULCL: ENABLE
    set_smffunc_list:
    - IPV6LOCALUP: UlClPrefer
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 进入“MML命令行-UNC”窗口。

### 2 配置UL CL属性名称和DNAI的绑定关系。

#### 2.1 //配置UL CL属性名称和DNAI的绑定关系。

```jinja2
{%- for item in add_ulclprop_list -%}
    ADD ULCLPROP:
    {#- --- 必选参数 --- -#}
    ULCLPROPNAME="{{item.ULCLPROPNAME}}",
    DNAI="{{item.DNAI}}",
    ;
{%- endfor -%}
```

### 3 配置正向分流DNAI信息。

#### 3.1 //配置正向分流DNAI信息。

```jinja2
{%- for item in add_dnaiinfo_list -%}
    ADD DNAIINFO:
    {#- --- 必选参数 --- -#}
    DNAI="{{item.DNAI}}",
    {#- --- 可选参数 --- -#}
    {%- if item.SHUNTDIRECT is not none -%}
        SHUNTDIRECT={{item.SHUNTDIRECT}},
    {%- endif -%}
    {%- if item.SHUNTLOC is not none -%}
        SHUNTLOC={{item.SHUNTLOC}},
    {%- endif -%}
    {%- if item.ALWAYSSHUNTSW is not none -%}
        ALWAYSSHUNTSW={{item.ALWAYSSHUNTSW}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 配置专用DNN Always的分流功能。

#### 4.1 //配置专用DNN Always的分流功能。

```jinja2
{%- for item in add_apn_list -%}
    ADD APN:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    {#- --- 可选参数 --- -#}
    {%- if item.ALWAYSPSAULCLSW is not none -%}
        ALWAYSPSAULCLSW={{item.ALWAYSPSAULCLSW}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 5 配置专用DNN下UPF位置特征。

#### 5.1 //配置专用DNN下UPF位置特征。

```jinja2
{%- for item in add_apnupfinfo_list -%}
    ADD APNUPFINFO:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    UPFINSTANCEID="{{item.UPFINSTANCEID}}",
    {#- --- 可选参数 --- -#}
    {%- if item.LOCATION is not none -%}
        LOCATION={{item.LOCATION}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：LOCATION=CENTERONLY/BOTH 时可选 --- -#}
    {%- if item.LOCATION in ['CENTERONLY', 'BOTH'] -%}
        {%- if item.PSACOMBINEULCL is not none -%}
            PSACOMBINEULCL={{item.PSACOMBINEULCL}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 6 修改主锚点UPF为支持主锚点和分流UPF合设形态。

#### 6.1 //修改主锚点UPF为支持主锚点和分流UPF合设形态。

```jinja2
{%- for item in mod_upnode_list -%}
    MOD UPNODE:
    {#- --- 必选参数 --- -#}
    NFINSTANCENAME="{{item.NFINSTANCENAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.LOCATION is not none -%}
        LOCATION={{item.LOCATION}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：LOCATION=Central/CentralOnly 时可选 --- -#}
    {%- if item.LOCATION in ['Central', 'CentralOnly'] -%}
        {%- if item.SUPULCLBPONLY is not none -%}
            SUPULCLBPONLY={{item.SUPULCLBPONLY}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：LOCATION=Central/CentralOnly 时可选 --- -#}
    {%- if item.LOCATION in ['Central', 'CentralOnly'] -%}
        {%- if item.PSACOMBINEULCL is not none -%}
            PSACOMBINEULCL={{item.PSACOMBINEULCL}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 7 配置IPv6会话场景下的分流策略。

#### 7.1 //配置IPv6会话场景下的分流策略。

```jinja2
{%- for item in set_smffunc_list -%}
    SET SMFFUNC:
    {#- --- 可选参数 --- -#}
    {%- if item.IPV6LOCALUP is not none -%}
        IPV6LOCALUP={{item.IPV6LOCALUP}},
    {%- endif -%}
    ;
{%- endfor -%}
```


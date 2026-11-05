---
id: ''
name: 部署基于动态规则的分流策略控制(4G)（SMF）
ne_type: UNC
type: feature
description: 本文档用于指导4G网络中基于动态规则的UL CL分流策略控制功能的部署。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","MEC解决方案","WSFD-223102 基于动态规则的分流策略控制(4G)","部署基于动态规则的分流策略控制(4G)（SMF）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本文档用于指导4G网络中基于动态规则的UL CL分流策略控制功能的部署。

## 必备事项
前提条件

前提条件

* 请仔细阅读WSFD-223101 基于预定义规则的分流策略控制(4G)特性概述。
* 已完成本特性License加载，可以通过**DSP LICENSE**命令查询确认，如果本特性的License在查询列表中可见，即可认为本特性License已加载成功。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
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
        UPFUNCTION:
          name: 'UPF功能'
          type: string
          enum:
          - None
          - UlClAndBp
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
    add_dnarea_list:
      type: items
      properties:
        AREANAME:
          name: 'DNAI服务区域名称'
          type: string
          minLength: 1
          maxLength: 255
          required: true
          description: '配置DNAI对应的服务区域'
          data_source: '全网规划'
          pattern: ''
          default: ''
        AREATYPE:
          name: 'DNAI服务区域类型'
          type: string
          enum:
          - N2TAI
          - N2CID
          - S1TAI
          - S1CID
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_dnareabinds1tai_list:
      type: items
      properties:
        AREANAME:
          name: 'DNAI服务区域名称'
          type: string
          minLength: 1
          maxLength: 255
          required: true
          description: '配置DNAI服务区名称绑定的4G TAI范围'
          data_source: '全网规划'
          pattern: ''
          default: ''
        S1BEGINTAI:
          name: 'DNAI服务区名称支持4G TAI范围的起始值'
          type: string
          minLength: 9
          maxLength: 10
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        S1ENDTAI:
          name: 'DNAI服务区名称支持4G TAI范围的结束值'
          type: string
          minLength: 9
          maxLength: 10
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_dnaibinddnarea_list:
      type: items
      properties:
        DNAI:
          name: '数据网络访问标识'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '配置DNAI绑定的服务区域名称'
          data_source: '全网规划'
          pattern: ''
          default: ''
        AREANAME:
          name: 'DNAI服务区域名称'
          type: string
          minLength: 1
          maxLength: 255
          required: true
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
    set_smgtpprot_list:
      type: items
      properties:
        LTEULCLSW:
          name: '4G UL CL功能开关'
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
    mod_upnode_list:
    - NFINSTANCENAME: 'UPF_INSTANCE0'
      UPFUNCTION: UlClAndBp
      SUPULCLBPONLY: Disable
      PSACOMBINEULCL: ENABLE
      LOCATION: ''
    add_dnarea_list:
    - AREANAME: 'DNAREA1'
      AREATYPE: S1TAI
    add_dnareabinds1tai_list:
    - AREANAME: 'DNAREA1'
      S1BEGINTAI: '46001000001'
      S1ENDTAI: '46001123456'
    add_dnaibinddnarea_list:
    - DNAI: 'testdnai'
      AREANAME: 'DNAREA1'
    set_smffunc_list:
    - IPV6LOCALUP: UlClPrefer
    set_smgtpprot_list:
    - LTEULCLSW: ENABLE
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 进入“MML命令行-UNC”窗口。

### 2 修改主锚点UPF属性为支持主锚点和分流UPF合设形态。

```jinja2
{%- for item in mod_upnode_list -%}
    MOD UPNODE:
    {#- --- 必选参数 --- -#}
    NFINSTANCENAME="{{item.NFINSTANCENAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.UPFUNCTION is not none -%}
        UPFUNCTION={{item.UPFUNCTION}},
    {%- endif -%}
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

### 3 **可选：**配置DNAI关联的位置区域。当采用基于SMF本地DNN使能UL CL分流方式时，需要配置此步骤。

#### 3.1 配置DNAI对应的服务区域。

```jinja2
{%- if is_optional_dnai_location_area -%}
    {%- for item in add_dnarea_list -%}
        ADD DNAREA:
        {#- --- 必选参数 --- -#}
        AREANAME="{{item.AREANAME}}",
        AREATYPE={{item.AREATYPE}},
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 3.2 配置DNAI服务区名称绑定的4G TAI范围。

```jinja2
{%- if is_optional_dnai_location_area -%}
    {%- for item in add_dnareabinds1tai_list -%}
        ADD DNAREABINDS1TAI:
        {#- --- 必选参数 --- -#}
        AREANAME="{{item.AREANAME}}",
        S1BEGINTAI="{{item.S1BEGINTAI}}",
        S1ENDTAI="{{item.S1ENDTAI}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 3.3 配置DNAI绑定的服务区域名称。

```jinja2
{%- if is_optional_dnai_location_area -%}
    {%- for item in add_dnaibinddnarea_list -%}
        ADD DNAIBINDDNAREA:
        {#- --- 必选参数 --- -#}
        AREANAME="{{item.AREANAME}}",
        DNAI="{{item.DNAI}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

### 4 配置IPv6会话场景下的分流策略。

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

### 5 配置开启4G UL CL功能开关。

```jinja2
{%- for item in set_smgtpprot_list -%}
    SET SMGTPPROT:
    {#- --- 可选参数 --- -#}
    {%- if item.LTEULCLSW is not none -%}
        LTEULCLSW={{item.LTEULCLSW}},
    {%- endif -%}
    ;
{%- endfor -%}
```


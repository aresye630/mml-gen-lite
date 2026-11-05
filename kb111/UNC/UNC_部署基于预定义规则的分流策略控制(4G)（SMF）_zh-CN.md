---
id: ''
name: 部署基于预定义规则的分流策略控制(4G)（SMF）
ne_type: UNC
type: feature
description: 本文档用于指导4G网络中基于预定义规则的UL CL分流策略。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","MEC解决方案","WSFD-223101 基于预定义规则的分流策略控制(4G)","部署基于预定义规则的分流策略控制(4G)（SMF）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本文档用于指导4G网络中基于预定义规则的UL CL分流策略。

## 必备事项
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
    add_flowfilter_list:
      type: items
      properties:
        FLOWFILTERNAME:
          name: '流过滤器名称'
          type: string
          maxLength: 63
          required: true
          description: '配置App ID'
          data_source: '与对端协商'
          pattern: ''
          default: ''
    add_rule_list:
      type: items
      properties:
        RULENAME:
          name: '规则名称'
          type: string
          maxLength: 63
          required: true
          description: '配置UL CL分流rule以及和App ID的绑定关系'
          data_source: '全网规划'
          pattern: ''
          default: ''
        POLICYTYPE:
          name: '策略类型'
          type: string
          enum:
          - ADC
          - BWM
          - FIREWALL
          - FUP
          - HEADEN
          - IPREDIR
          - LBO
          - NON_SPECIFIC_TYPE
          - PCC
          - QOS
          - REMARK_FPI
          - SMARTREDIRECT
          - SRV_TRIGGER
          - TRAFFICCLASS
          - ULCL
          - WEBPROXY
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        POLICYNAME:
          name: '策略名称'
          type: string
          maxLength: 63
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        FLOWFILTERNAME:
          name: '流过滤器名称'
          type: string
          maxLength: 63
          required: false
          description: ''
          data_source: '与对端协商'
          pattern: ''
          default: ''
        PROTODESCDL:
          name: '下行协议描述参数'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PROTODESCUL:
          name: '上行协议描述参数'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RULERANGE:
          name: '规则生效范围'
          type: string
          enum:
          - ALL
          - CENTRAL
          - LOCAL
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ALL
    add_userprofile_list:
      type: items
      properties:
        USERPROFILENAME:
          name: '用户模板名称'
          type: string
          maxLength: 63
          required: true
          description: '配置UL CL属性的User Profile'
          data_source: '全网规划'
          pattern: ''
          default: ''
        UPTYPE:
          name: '用户模板类型'
          type: string
          enum:
          - PCC
          - ULCL
          - UPSELECT
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: PCC
        PROFILERANGE:
          name: '模板生效范围'
          type: string
          enum:
          - ALL
          - CENTRAL
          - LOCAL
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ALL
    add_rulebinding_list:
      type: items
      properties:
        USERPROFILENAME:
          name: '用户模板名称'
          type: string
          maxLength: 63
          required: true
          description: '将UL CL属性的User Profile和rule进行绑定'
          data_source: '全网规划'
          pattern: ''
          default: ''
        RULENAME:
          name: '规则名称'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        POLICYTYPE:
          name: '策略类型'
          type: string
          enum:
          - ADC
          - BWM
          - FIREWALL
          - FUP
          - HEADEN
          - IPREDIR
          - LBO
          - NON_SPECIFIC_TYPE
          - PCC
          - QOS
          - REMARK_FPI
          - SMARTREDIRECT
          - SRV_TRIGGER
          - TRAFFICCLASS
          - ULCL
          - WEBPROXY
          required: false
          description: ''
          data_source: '本端规划'
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
          description: '配置DNAI服务区名称绑定的4GTAI范围'
          data_source: '全网规划'
          pattern: ''
          default: ''
        S1BEGINTAI:
          name: 'DNAI服务区名称支持4GTAI范围的起始值'
          type: string
          minLength: 9
          maxLength: 10
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        S1ENDTAI:
          name: 'DNAI服务区名称支持4GTAI范围的结束值'
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
    add_ulclprop_list:
    - ULCLPROPNAME: 'testulclpropname'
      DNAI: 'testdnai'
    add_flowfilter_list:
    - FLOWFILTERNAME: 'ulcl'
    add_rule_list:
    - RULENAME: 'testrule'
      POLICYTYPE: ULCL
      POLICYNAME: 'testulclpropname'
      FLOWFILTERNAME: 'ulcl'
      PROTODESCDL: ''
      PROTODESCUL: ''
      RULERANGE: ALL
    add_userprofile_list:
    - USERPROFILENAME: 'testuserprofilename'
      UPTYPE: ULCL
      PROFILERANGE: ALL
    add_rulebinding_list:
    - USERPROFILENAME: 'testuserprofilename'
      RULENAME: 'testrule'
      POLICYTYPE: ULCL
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

### 3 配置基于预定义规则的UL CL策略。

#### 3.1 配置ULCL属性名称和DNAI的绑定关系。

```jinja2
{%- for item in add_ulclprop_list -%}
    ADD ULCLPROP:
    {#- --- 必选参数 --- -#}
    ULCLPROPNAME="{{item.ULCLPROPNAME}}",
    DNAI="{{item.DNAI}}",
    ;
{%- endfor -%}
```

#### 3.2 配置ULCL过滤器名称。

```jinja2
{%- for item in add_flowfilter_list -%}
    ADD FLOWFILTER:
    {#- --- 必选参数 --- -#}
    FLOWFILTERNAME="{{item.FLOWFILTERNAME}}",
    ;
{%- endfor -%}
```

#### 3.3 配置ULCL分流策略rule。

```jinja2
{%- for item in add_rule_list -%}
    ADD RULE:
    {#- --- 必选参数 --- -#}
    RULENAME="{{item.RULENAME}}",
    POLICYTYPE={{item.POLICYTYPE}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：POLICYTYPE=PCC/ULCL/QOS 时必选 --- -#}
    {%- if item.POLICYTYPE in ['PCC', 'ULCL', 'QOS'] -%}
        POLICYNAME="{{item.POLICYNAME}}",
    {%- endif -%}
    {#- --- 条件必选：POLICYTYPE=ULCL 时必选 --- -#}
    {%- if item.POLICYTYPE == 'ULCL' -%}
        FLOWFILTERNAME="{{item.FLOWFILTERNAME}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：POLICYTYPE=PCC/QOS 时可选 --- -#}
    {%- if item.POLICYTYPE in ['PCC', 'QOS'] -%}
        {%- if item.PROTODESCDL is not none -%}
            PROTODESCDL="{{item.PROTODESCDL}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：POLICYTYPE=PCC/QOS 时可选 --- -#}
    {%- if item.POLICYTYPE in ['PCC', 'QOS'] -%}
        {%- if item.PROTODESCUL is not none -%}
            PROTODESCUL="{{item.PROTODESCUL}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：POLICYTYPE=PCC/QOS 时可选 --- -#}
    {%- if item.POLICYTYPE in ['PCC', 'QOS'] -%}
        {%- if item.RULERANGE is not none -%}
            RULERANGE={{item.RULERANGE}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 3.4 配置ULCL属性的用户模板。

```jinja2
{%- for item in add_userprofile_list -%}
    ADD USERPROFILE:
    {#- --- 必选参数 --- -#}
    USERPROFILENAME="{{item.USERPROFILENAME}}",
    UPTYPE={{item.UPTYPE}},
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：UPTYPE=PCC 时可选 --- -#}
    {%- if item.UPTYPE == 'PCC' -%}
        {%- if item.PROFILERANGE is not none -%}
            PROFILERANGE={{item.PROFILERANGE}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 3.5 将上述rule绑定至用户模板。

```jinja2
{%- for item in add_rulebinding_list -%}
    ADD RULEBINDING:
    {#- --- 必选参数 --- -#}
    USERPROFILENAME="{{item.USERPROFILENAME}}",
    RULENAME="{{item.RULENAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.POLICYTYPE is not none -%}
        POLICYTYPE={{item.POLICYTYPE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 **可选：**配置DNAI关联的位置区域。当采用基于SMF本地DNN使能UL CL分流方式时，需要配置此步骤。

#### 4.1 配置DNAI对应的服务区域。

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

#### 4.2 配置DNAI服务区名称绑定的4GTAI范围。

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

#### 4.3 配置DNAI绑定的服务区域名称。

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

### 5 配置IPv6会话场景下的分流策略。

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

### 6 配置开启4G UL CL功能开关。

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


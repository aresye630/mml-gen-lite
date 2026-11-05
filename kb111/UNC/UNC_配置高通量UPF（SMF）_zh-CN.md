---
id: ''
name: 配置高通量UPF（SMF）
ne_type: UNC
type: feature
description: 本操作指导完成高通量UPF选择解决方案中UNC侧的初始业务配置。
risk_level: ''
doc_source: ["网络部署","业务专题","5G Core 高通量UPF选择方案","配置高通量UPF（SMF）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本操作指导完成高通量UPF选择解决方案中UNC侧的初始业务配置。

## 必备事项
前提条件

* 请仔细阅读高通量UPF特性概述。
* 完成相关接口配置，具体请参考《UNC 产品文档》：初始配置 > UNC初始配置与调测中各接口配置。
* 高通量业务的规则名已全网统一规划。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    add_apnsmcomfunc_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '增加APN粒度的通用会话拓展功能控制，SMF先从UPCF获取会话策略再进行UPF选择。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        GETPOLICYFIRST:
          name: '在EPS是否先获取策略'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: DISABLE
    add_userprofile_list:
      type: items
      properties:
        USERPROFILENAME:
          name: '用户模板名称'
          type: string
          maxLength: 63
          required: true
          description: '配置用户模板。该UserProfile仅用于高通量UPF选择。'
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
          data_source: '全网规划'
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
    add_selectruleinfo_list:
      type: items
      properties:
        RULENAME:
          name: '规则名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '增加高通量规则信息，规则下发给主锚点。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        RULEFUNC:
          name: '规则功能'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        DELIVERSW:
          name: '是否下发给UPF'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        RULERANGE:
          name: '下发范围'
          type: string
          enum:
          - CENTRAL
          - ALL
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        PRIORITY:
          name: '优先级'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_upfbindselrule_list:
      type: items
      properties:
        INDEX:
          name: '索引'
          type: integer
          minimum: 0
          maximum: 4999
          required: true
          description: 'UPF0支持高通量。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        NFINSTANCENAME:
          name: 'UPF实例名称'
          type: string
          minLength: 1
          maxLength: 255
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        RULENAME:
          name: '规则名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    set_pfcppvtext_list:
      type: items
      properties:
        FEATURE:
          name: '特性名称'
          type: string
          enum:
          - QER_TYPE
          - BWM
          - UPA
          - SESSION_ROLE_TYPE
          - DNAI
          - QCI
          - ARP
          - URR_CHARGING_TYPE
          - RG
          - SID
          - HW_EVENT_MEASUREMENT
          - S_NSSAI
          - SELF_SEID
          - SGW_STATE_INFO
          - NGLAN
          - L2TP_TNL
          - L2TP_PCO
          - MultiDNN_Type
          - MultiDNN_DNN
          - MultiDNN_Snssai
          - MultiDNN_IP_Address
          - MultiDNN_Rat_Type
          - MultiDNN_DNS_Filter
          - MultiDNN_Filter_Indication
          - URR_PERF_TYPE
          - AUTH_CLASS
          - CHARGING_TYPE
          - Qos_Analysis
          - EXTEND_ROAMING_TYPE
          - EXTEND_PROXY_TYPE
          - Session_Delete_Cause
          - Qos_Experience
          - Feature_Rule
          - Qos_Quality_Indicate
          - IPE_Indicate
          - Default_Qos_Flag
          required: true
          description: '功能开启时，在PFCP Session Establishment Request/PFCP Session Modification Request消息中携带私有信元ActivatedFeatureRule。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SWITCH:
          name: '私有信元携带开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_apnsmcomfunc_list_1:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '增加APN粒度的通用会话拓展功能控制，SMF先从UPCF获取会话策略再进行UPF选择。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        GETPOLICYFIRST:
          name: '在EPS是否先获取策略'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: DISABLE
    add_selectruleinfo_list_1:
      type: items
      properties:
        RULENAME:
          name: '规则名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '+ 增加高通量规则信息，规则下发给主锚点。 + 规则名称请根据现网情况修改。 说明：  不同类型UPF之间优先级关系：  同时支持高通量和智能面的UPF>仅支持智能面的UPF>仅支持高通量的UPF'
          data_source: '全网规划'
          pattern: ''
          default: ''
        RULEFUNC:
          name: '规则功能'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        DELIVERSW:
          name: '是否下发给UPF'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        RULERANGE:
          name: '下发范围'
          type: string
          enum:
          - CENTRAL
          - ALL
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        PRIORITY:
          name: '优先级'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_upfbindselrule_list_2:
      type: items
      properties:
        INDEX:
          name: '索引'
          type: integer
          minimum: 0
          maximum: 4999
          required: true
          description: '增加高通量规则和UPF2的绑定关系。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        NFINSTANCENAME:
          name: 'UPF实例名称'
          type: string
          minLength: 1
          maxLength: 255
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        RULENAME:
          name: '规则名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    set_pfcppvtext_list_1:
      type: items
      properties:
        FEATURE:
          name: '特性名称'
          type: string
          enum:
          - QER_TYPE
          - BWM
          - UPA
          - SESSION_ROLE_TYPE
          - DNAI
          - QCI
          - ARP
          - URR_CHARGING_TYPE
          - RG
          - SID
          - HW_EVENT_MEASUREMENT
          - S_NSSAI
          - SELF_SEID
          - SGW_STATE_INFO
          - NGLAN
          - L2TP_TNL
          - L2TP_PCO
          - MultiDNN_Type
          - MultiDNN_DNN
          - MultiDNN_Snssai
          - MultiDNN_IP_Address
          - MultiDNN_Rat_Type
          - MultiDNN_DNS_Filter
          - MultiDNN_Filter_Indication
          - URR_PERF_TYPE
          - AUTH_CLASS
          - CHARGING_TYPE
          - Qos_Analysis
          - EXTEND_ROAMING_TYPE
          - EXTEND_PROXY_TYPE
          - Session_Delete_Cause
          - Qos_Experience
          - Feature_Rule
          - Qos_Quality_Indicate
          - IPE_Indicate
          - Default_Qos_Flag
          required: true
          description: '功能开启时，在PFCP Session Establishment Request/PFCP Session Modification Request消息中携带私有信元ActivatedFeatureRule。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SWITCH:
          name: '私有信元携带开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
  examples:
    add_apnsmcomfunc_list:
    - APN: 'HUAWEI.COM'
      GETPOLICYFIRST: ENABLE
    add_userprofile_list:
    - USERPROFILENAME: 'testuserprofilename'
      UPTYPE: UPSELECT
      PROFILERANGE: ALL
    add_selectruleinfo_list:
    - RULENAME: 'testuserprofilename'
      RULEFUNC: QOSANA-0&QOSEXP-0&QOSCCC-1，DELIVERSW=ENABLE，RULERANGE=CENTRAL
      DELIVERSW: ENABLE
      RULERANGE: CENTRAL
      PRIORITY: 1
    add_upfbindselrule_list:
    - INDEX: 0
      NFINSTANCENAME: 'upf_instance_0'
      RULENAME: 'testuserprofilename'
    set_pfcppvtext_list:
    - FEATURE: Feature_Rule
      SWITCH: ENABLE
    add_apnsmcomfunc_list_1:
    - APN: 'HUAWEI.COM'
      GETPOLICYFIRST: ENABLE
    add_selectruleinfo_list_1:
    - RULENAME: 'select_high_upf'
      RULEFUNC: QOSANA-0&QOSEXP-0&QOSCCC-1，DELIVERSW=ENABLE，RULERANGE=CENTRAL
      DELIVERSW: ENABLE
      RULERANGE: CENTRAL
      PRIORITY: 2
    add_upfbindselrule_list_2:
    - INDEX: 1
      NFINSTANCENAME: 'upf_instance_2'
      RULENAME: 'select_high_upf'
    set_pfcppvtext_list_1:
    - FEATURE: Feature_Rule
      SWITCH: ENABLE
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 配置选择支持高通量的UPF（N7接口按pccRules信元下发高通量规则（预定义规则））

### 进入“MML命令行-UNC”窗口。

### 2 配置SMF支持基于用户签约选择高通量UPF。

```jinja2
{%- if is_scenario_pccrules -%}
    {%- for item in add_apnsmcomfunc_list -%}
        ADD APNSMCOMFUNC:
        {#- --- 必选参数 --- -#}
        APN="{{item.APN}}",
        {#- --- 可选参数 --- -#}
        {%- if item.GETPOLICYFIRST is not none -%}
            GETPOLICYFIRST={{item.GETPOLICYFIRST}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 3 配置业务策略规则。

```jinja2
{%- if is_scenario_pccrules -%}
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
{%- endif -%}
```

### 4 增加UPF选择规则信息。

```jinja2
{%- if is_scenario_pccrules -%}
    {%- for item in add_selectruleinfo_list -%}
        ADD SELECTRULEINFO:
        {#- --- 必选参数 --- -#}
        RULENAME="{{item.RULENAME}}",
        {#- --- 可选参数 --- -#}
        {%- if item.RULEFUNC is not none -%}
            RULEFUNC={{item.RULEFUNC}},
        {%- endif -%}
        {%- if item.DELIVERSW is not none -%}
            DELIVERSW={{item.DELIVERSW}},
        {%- endif -%}
        {%- if item.PRIORITY is not none -%}
            PRIORITY={{item.PRIORITY}},
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：DELIVERSW=ENABLE 时可选 --- -#}
        {%- if item.DELIVERSW == 'ENABLE' -%}
            {%- if item.RULERANGE is not none -%}
                RULERANGE={{item.RULERANGE}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 5 配置用户面支持高通量业务。UPF2仅支持高通量、UPF0支持高通量。

```jinja2
{%- if is_scenario_pccrules -%}
    {%- for item in add_upfbindselrule_list -%}
        ADD UPFBINDSELRULE:
        {#- --- 必选参数 --- -#}
        INDEX={{item.INDEX}},
        NFINSTANCENAME="{{item.NFINSTANCENAME}}",
        RULENAME="{{item.RULENAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

### 6 配置在PFCP Session Establishment Request和PFCP Session Modification Request消息中携带私有信元ActivatedFeatureRule。

```jinja2
{%- if is_scenario_pccrules -%}
    {%- for item in set_pfcppvtext_list -%}
        SET PFCPPVTEXT:
        {#- --- 必选参数 --- -#}
        FEATURE={{item.FEATURE}},
        {#- --- 可选参数 --- -#}
        {%- if item.SWITCH is not none -%}
            SWITCH={{item.SWITCH}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 7 配置选择支持高通量的UPF（N7接口按upfSelectRules信元形式下发高通量规则）

### 进入“MML命令行-UNC”窗口。

### 8 配置SMF支持基于用户签约选择高通UPF。

```jinja2
{%- if is_scenario_upfselectrules -%}
    {%- for item in add_apnsmcomfunc_list_1 -%}
        ADD APNSMCOMFUNC:
        {#- --- 必选参数 --- -#}
        APN="{{item.APN}}",
        {#- --- 可选参数 --- -#}
        {%- if item.GETPOLICYFIRST is not none -%}
            GETPOLICYFIRST={{item.GETPOLICYFIRST}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 9 增加UPF选择规则信息。

```jinja2
{%- if is_scenario_upfselectrules -%}
    {%- for item in add_selectruleinfo_list_1 -%}
        ADD SELECTRULEINFO:
        {#- --- 必选参数 --- -#}
        RULENAME="{{item.RULENAME}}",
        {#- --- 可选参数 --- -#}
        {%- if item.RULEFUNC is not none -%}
            RULEFUNC={{item.RULEFUNC}},
        {%- endif -%}
        {%- if item.DELIVERSW is not none -%}
            DELIVERSW={{item.DELIVERSW}},
        {%- endif -%}
        {%- if item.PRIORITY is not none -%}
            PRIORITY={{item.PRIORITY}},
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：DELIVERSW=ENABLE 时可选 --- -#}
        {%- if item.DELIVERSW == 'ENABLE' -%}
            {%- if item.RULERANGE is not none -%}
                RULERANGE={{item.RULERANGE}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 10 增加智能规则和UPF的绑定关系。UPF2仅支持高通量、UPF0支持高通量。

```jinja2
{%- if is_scenario_upfselectrules -%}
    {%- for item in add_upfbindselrule_list_2 -%}
        ADD UPFBINDSELRULE:
        {#- --- 必选参数 --- -#}
        INDEX={{item.INDEX}},
        NFINSTANCENAME="{{item.NFINSTANCENAME}}",
        RULENAME="{{item.RULENAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

### 11 配置在PFCP Session Establishment Request和PFCP Session Modification Request消息中携带私有信元ActivatedFeatureRule。

```jinja2
{%- if is_scenario_upfselectrules -%}
    {%- for item in set_pfcppvtext_list_1 -%}
        SET PFCPPVTEXT:
        {#- --- 必选参数 --- -#}
        FEATURE={{item.FEATURE}},
        {#- --- 可选参数 --- -#}
        {%- if item.SWITCH is not none -%}
            SWITCH={{item.SWITCH}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```


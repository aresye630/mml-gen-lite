---
id: ''
name: 媒体中继UPF选择配置
ne_type: UNC
type: feature
description: 本操作指导完成媒体中继UPF选择中SMF侧的业务配置。
risk_level: ''
doc_source: ["网络部署","业务专题","UNC UPF选择专题","媒体中继UPF选择","媒体中继UPF选择配置"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本操作指导完成媒体中继UPF选择中SMF侧的业务配置。

## 必备事项
前提条件

* 请仔细阅读媒体中继UPF选择原理、媒体中继UPF选择场景。
* 完成SMF和UPF的N4接口配置，具体请参考《UNC 产品文档》：初始配置 > UNC初始配置与调测中各接口配置。
* 媒体中继业务的规则名已全网统一规划。
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
          description: '增加APN粒度的通用会话拓展功能控制，SMF先从PCF获取会话策略再进行UPF选择。'
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
    add_rule_list:
      type: items
      properties:
        RULENAME:
          name: '规则名称'
          type: string
          maxLength: 63
          required: true
          description: '配置业务策略规则。'
          data_source: '对端协商'
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
          data_source: '对端协商'
          pattern: ''
          default: ''
        FLOWFILTERNAME:
          name: '流过滤器名称'
          type: string
          maxLength: 63
          required: false
          description: ''
          data_source: ''
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
          description: '配置用户模板。该UserProfile用于媒体中继UPF选择，标识媒体中继业务相关的预定义规则。'
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
        RELAYSW:
          name: '媒体中继开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: DISABLE
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
          description: '配置用户模板与规则的绑定关系。用户模板名称已通过**ADD USERPROFILE**完成配置，规则名称已通过**ADD RULE**完成配置。'
          data_source: '本端规划'
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
    add_selectruleinfo_list:
      type: items
      properties:
        RULENAME:
          name: '规则名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '增加媒体中继规则信息，规则下发给主锚点。'
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
          description: 'upf\_instance\_3支持媒体中继业务。'
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
          description: '功能开启时，在PFCP Session Establishment Request/PFCP Session Modification Request消息中携带私有信元ActivatedFeatureRule/DeactivatedFeatureRule。'
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
          description: '增加APN粒度的通用会话拓展功能控制，SMF先从PCF获取会话策略再进行UPF选择。'
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
          description: '+ 增加媒体中继规则信息，规则下发给主锚点。 + 规则名称请根据现网情况修改。 说明：  对于同时签约媒体中继+双域+智能业务的用户，选择UPF优先级顺序如下：双域+智能+媒体中继 UPF > 双域+智能UPF > 智能UPF > 普通UPF。'
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
    add_upfbindselrule_list_1:
      type: items
      properties:
        INDEX:
          name: '索引'
          type: integer
          minimum: 0
          maximum: 4999
          required: true
          description: '增加媒体中继规则和upf\_instance\_3的绑定关系。'
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
          description: '功能开启时，在PFCP Session Establishment Request/PFCP Session Modification Request消息中携带私有信元ActivatedFeatureRule/DeactivatedFeatureRule。'
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
    add_rule_list_1:
      type: items
      properties:
        RULENAME:
          name: '规则名称'
          type: string
          maxLength: 63
          required: true
          description: '配置业务策略规则。'
          data_source: '对端协商'
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
          data_source: '对端协商'
          pattern: ''
          default: ''
        FLOWFILTERNAME:
          name: '流过滤器名称'
          type: string
          maxLength: 63
          required: false
          description: ''
          data_source: ''
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
    add_userprofile_list_1:
      type: items
      properties:
        USERPROFILENAME:
          name: '用户模板名称'
          type: string
          maxLength: 63
          required: true
          description: '配置用户模板。该UserProfile用于标识媒体中继业务相关的预定义规则。'
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
          data_source: '全网规划'
          pattern: ''
          default: ALL
    add_rulebinding_list_1:
      type: items
      properties:
        USERPROFILENAME:
          name: '用户模板名称'
          type: string
          maxLength: 63
          required: true
          description: '配置用户模板与规则的绑定关系。用户模板名称已通过**ADD USERPROFILE**完成配置，规则名称已通过**ADD RULE**完成配置。'
          data_source: '本端规划'
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
  examples:
    add_apnsmcomfunc_list:
    - APN: 'huawei.com'
      GETPOLICYFIRST: ENABLE
    add_rule_list:
    - RULENAME: 'relayrule'
      POLICYTYPE: NON_SPECIFIC_TYPE
      FLOWFILTERNAME: ''
      POLICYNAME: ''
      PROTODESCDL: ''
      PROTODESCUL: ''
      RULERANGE: ALL
    add_userprofile_list:
    - USERPROFILENAME: 'testuserprofilename'
      UPTYPE: UPSELECT
      RELAYSW: ENABLE
      PROFILERANGE: ALL
    add_rulebinding_list:
    - USERPROFILENAME: 'testuserprofilename'
      RULENAME: 'relayrule'
      POLICYTYPE: NON_SPECIFIC_TYPE
    add_selectruleinfo_list:
    - RULENAME: 'testuserprofilename'
      RULEFUNC: QOSANA-0&QOSEXP-0&QOSCCC-0&RELAY-1
      DELIVERSW: ENABLE
      RULERANGE: CENTRAL
      PRIORITY: 1
    add_upfbindselrule_list:
    - INDEX: 0
      NFINSTANCENAME: 'upf_instance_3'
      RULENAME: 'testuserprofilename'
    set_pfcppvtext_list:
    - FEATURE: Feature_Rule
      SWITCH: ENABLE
    add_apnsmcomfunc_list_1:
    - APN: 'huawei.com'
      GETPOLICYFIRST: ENABLE
    add_selectruleinfo_list_1:
    - RULENAME: 'select_relay_upf'
      RULEFUNC: QOSANA-0&QOSEXP-0&QOSCCC-0&RELAY-1
      DELIVERSW: ENABLE
      RULERANGE: CENTRAL
      PRIORITY: 2
    add_upfbindselrule_list_1:
    - INDEX: 1
      NFINSTANCENAME: 'upf_instance_3'
      RULENAME: 'select_relay_upf'
    set_pfcppvtext_list_1:
    - FEATURE: Feature_Rule
      SWITCH: ENABLE
    add_rule_list_1:
    - RULENAME: 'relayrule'
      POLICYTYPE: NON_SPECIFIC_TYPE
      FLOWFILTERNAME: ''
      POLICYNAME: ''
      PROTODESCDL: ''
      PROTODESCUL: ''
      RULERANGE: ALL
    add_userprofile_list_1:
    - USERPROFILENAME: 'testuserprofilename'
      UPTYPE: PCC
      PROFILERANGE: CENTRAL
    add_rulebinding_list_1:
    - USERPROFILENAME: 'testuserprofilename'
      RULENAME: 'relayrule'
      POLICYTYPE: NON_SPECIFIC_TYPE
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 配置选择媒体中继UPF（PCF通过pccRules信元下发UPF选择规则）

#### 1.1 进入“MML命令行-UNC”窗口。

#### 1.2 配置SMF支持基于用户签约选择媒体中继UPF。

```jinja2
{%- if is_scenario_pcc_rules -%}
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

#### 1.3 配置业务策略规则。

```jinja2
{%- if is_scenario_pcc_rules -%}
    {%- for item in add_rule_list -%}
        ADD RULE:
        {#- --- 必选参数 --- -#}
        RULENAME="{{item.RULENAME}}",
        POLICYTYPE={{item.POLICYTYPE}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：POLICYTYPE=ULCL 时必选 --- -#}
        {%- if item.POLICYTYPE == 'ULCL' -%}
            FLOWFILTERNAME="{{item.FLOWFILTERNAME}}",
        {%- endif -%}
        {#- --- 条件必选：POLICYTYPE=PCC/ULCL/QOS 时必选 --- -#}
        {%- if item.POLICYTYPE in ['PCC', 'ULCL', 'QOS'] -%}
            POLICYNAME="{{item.POLICYNAME}}",
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
{%- endif -%}
```

```jinja2
{%- if is_scenario_pcc_rules -%}
    {%- for item in add_userprofile_list -%}
        ADD USERPROFILE:
        {#- --- 必选参数 --- -#}
        USERPROFILENAME="{{item.USERPROFILENAME}}",
        UPTYPE={{item.UPTYPE}},
        {#- --- 可选参数 --- -#}
        {%- if item.RELAYSW is not none -%}
            RELAYSW={{item.RELAYSW}},
        {%- endif -%}
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

```jinja2
{%- if is_scenario_pcc_rules -%}
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
{%- endif -%}
```

#### 1.4 配置UPF选择规则信息。

```jinja2
{%- if is_scenario_pcc_rules -%}
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

#### 1.5 配置用户面支持媒体中继业务。upf\_instance\_3支持媒体中继业务。

```jinja2
{%- if is_scenario_pcc_rules -%}
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

#### 1.6 配置在PFCP Session Establishment Request和PFCP Session Modification Request消息中携带私有信元ActivatedFeatureRule/DeactivatedFeatureRule。

```jinja2
{%- if is_scenario_pcc_rules -%}
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

### 2 配置选择媒体中继UPF（PCF通过upfSelectRules信元下发UPF选择规则）

#### 2.1 进入“MML命令行-UNC”窗口。

#### 2.2 配置SMF支持基于用户签约选择媒体中继UPF。

```jinja2
{%- if is_scenario_upf_select_rules -%}
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

#### 2.3 配置UPF选择规则信息。

```jinja2
{%- if is_scenario_upf_select_rules -%}
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

#### 2.4 配置规则和UPF的绑定关系。upf\_instance\_3支持媒体中继业务。

```jinja2
{%- if is_scenario_upf_select_rules -%}
    {%- for item in add_upfbindselrule_list_1 -%}
        ADD UPFBINDSELRULE:
        {#- --- 必选参数 --- -#}
        INDEX={{item.INDEX}},
        NFINSTANCENAME="{{item.NFINSTANCENAME}}",
        RULENAME="{{item.RULENAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 2.5 配置在PFCP Session Establishment Request和PFCP Session Modification Request消息中携带私有信元ActivatedFeatureRule/DeactivatedFeatureRule。

```jinja2
{%- if is_scenario_upf_select_rules -%}
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

#### 2.6 配置业务策略规则。标识媒体中继业务相关的预定义规则。

```jinja2
{%- if is_scenario_upf_select_rules -%}
    {%- for item in add_rule_list_1 -%}
        ADD RULE:
        {#- --- 必选参数 --- -#}
        RULENAME="{{item.RULENAME}}",
        POLICYTYPE={{item.POLICYTYPE}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：POLICYTYPE=ULCL 时必选 --- -#}
        {%- if item.POLICYTYPE == 'ULCL' -%}
            FLOWFILTERNAME="{{item.FLOWFILTERNAME}}",
        {%- endif -%}
        {#- --- 条件必选：POLICYTYPE=PCC/ULCL/QOS 时必选 --- -#}
        {%- if item.POLICYTYPE in ['PCC', 'ULCL', 'QOS'] -%}
            POLICYNAME="{{item.POLICYNAME}}",
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
{%- endif -%}
```

```jinja2
{%- if is_scenario_upf_select_rules -%}
    {%- for item in add_userprofile_list_1 -%}
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

```jinja2
{%- if is_scenario_upf_select_rules -%}
    {%- for item in add_rulebinding_list_1 -%}
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
{%- endif -%}
```


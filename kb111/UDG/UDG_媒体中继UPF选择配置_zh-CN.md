---
id: ''
name: 媒体中继UPF选择配置
ne_type: UDG
type: feature
description: 本操作指导完成媒体中继UPF选择中SMF侧的业务配置。
risk_level: ''
doc_source: ["特性部署","业务专题","5G Core 媒体中继解决方案","媒体中继业务配置","新建媒体中继基础配置","配置SMF","媒体中继UPF选择配置"]
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
          required: false
          description: '增加APN粒度的通用会话拓展功能控制，SMF先从PCF获取会话策略再进行UPF选择。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        GETPOLICYFIRST:
          name: '在EPS是否先获取策略'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_rule_list:
      type: items
      properties:
        RULENAME:
          name: '规则名称'
          type: string
          minLength: 0
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
          - HEADEN
          - IPREDIR
          - LBO
          - PCC
          - QOS
          - REMARK_FPI
          - SMARTREDIRECT
          - SRV_TRIGGER
          - TRAFFICCLASS
          - WEBPROXY
          - WORKER
          required: true
          description: ''
          data_source: '对端协商'
          pattern: ''
          default: ''
        FILTERINGMODE:
          name: '流过滤器或流过滤器组选择'
          type: string
          enum:
          - FLOWFILTER
          - FLOWFILTERGRP
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        FLOWFILTERNAME:
          name: '流过滤器名称'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        FLWFLTRGRPNAME:
          name: '流过滤器组名称'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ADCMUTEFLAG:
          name: 'ADC静默通知标识'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ENABLE
        ALGSWITCH:
          name: 'ALG功能开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
        POLICYNAME:
          name: '策略名称'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RDSTRIGGERFLAG:
          name: 'Radius消息触发标识'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
        REDIRIPVERFLAG:
          name: 'IP重定向虚拟IP协议版本'
          type: string
          enum:
          - IPV4
          - IPV6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        REMARKFPISEL:
          name: '重标记、FPI或SAI选择'
          type: string
          enum:
          - FPI
          - REMARK
          - REMARKANDFPI
          - SAI
          - REMARKANDSAI
          - FPIANDSAI
          - RMKFPISAI
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: REMARK
        SRVLBOFLAG:
          name: '本地业务分流标识'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
        WORKERNAME:
          name: '通用Rule子策略名称'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        WORKERPARA:
          name: '通用策略参数'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_userprofile_list:
      type: items
      properties:
        USERPROFILENAME:
          name: '用户模板名称'
          type: string
          required: false
          description: '配置用户模板。该UserProfile用于媒体中继UPF选择，标识媒体中继业务相关的预定义规则。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        UPTYPE:
          name: '用户模板类型'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        RELAYSW:
          name: '媒体中继开关'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_rulebinding_list:
      type: items
      properties:
        USERPROFILENAME:
          name: '用户模板名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '配置用户模板与规则的绑定关系。用户模板名称已通过**ADD USERPROFILE**完成配置，规则名称已通过**ADD RULE**完成配置。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        RULENAME:
          name: '规则名称'
          type: string
          minLength: 0
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
          - HEADEN
          - IPREDIR
          - LBO
          - PCC
          - QOS
          - REMARK_FPI
          - SMARTREDIRECT
          - SRV_TRIGGER
          - TRAFFICCLASS
          - WEBPROXY
          - WORKER
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
          required: false
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
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        RULERANGE:
          name: '下发范围'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        PRIORITY:
          name: '优先级'
          type: string
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
          type: string
          required: false
          description: 'upf\_instance\_3支持媒体中继业务。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        NFINSTANCENAME:
          name: 'UPF实例名称'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        RULENAME:
          name: '规则名称'
          type: string
          required: false
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
          required: false
          description: '功能开启时，在PFCP Session Establishment Request/PFCP Session Modification Request消息中携带私有信元ActivatedFeatureRule/DeactivatedFeatureRule。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SWITCH:
          name: '私有信元携带开关'
          type: string
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
          required: false
          description: '增加APN粒度的通用会话拓展功能控制，SMF先从PCF获取会话策略再进行UPF选择。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        GETPOLICYFIRST:
          name: '在EPS是否先获取策略'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_selectruleinfo_list_1:
      type: items
      properties:
        RULENAME:
          name: '规则名称'
          type: string
          required: false
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
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        RULERANGE:
          name: '下发范围'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        PRIORITY:
          name: '优先级'
          type: string
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
          type: string
          required: false
          description: '增加媒体中继规则和upf\_instance\_3的绑定关系。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        NFINSTANCENAME:
          name: 'UPF实例名称'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        RULENAME:
          name: '规则名称'
          type: string
          required: false
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
          required: false
          description: '功能开启时，在PFCP Session Establishment Request/PFCP Session Modification Request消息中携带私有信元ActivatedFeatureRule/DeactivatedFeatureRule。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SWITCH:
          name: '私有信元携带开关'
          type: string
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
          minLength: 0
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
          - HEADEN
          - IPREDIR
          - LBO
          - PCC
          - QOS
          - REMARK_FPI
          - SMARTREDIRECT
          - SRV_TRIGGER
          - TRAFFICCLASS
          - WEBPROXY
          - WORKER
          required: true
          description: ''
          data_source: '对端协商'
          pattern: ''
          default: ''
        FILTERINGMODE:
          name: '流过滤器或流过滤器组选择'
          type: string
          enum:
          - FLOWFILTER
          - FLOWFILTERGRP
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        FLOWFILTERNAME:
          name: '流过滤器名称'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        FLWFLTRGRPNAME:
          name: '流过滤器组名称'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ADCMUTEFLAG:
          name: 'ADC静默通知标识'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ENABLE
        ALGSWITCH:
          name: 'ALG功能开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
        POLICYNAME:
          name: '策略名称'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RDSTRIGGERFLAG:
          name: 'Radius消息触发标识'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
        REDIRIPVERFLAG:
          name: 'IP重定向虚拟IP协议版本'
          type: string
          enum:
          - IPV4
          - IPV6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        REMARKFPISEL:
          name: '重标记、FPI或SAI选择'
          type: string
          enum:
          - FPI
          - REMARK
          - REMARKANDFPI
          - SAI
          - REMARKANDSAI
          - FPIANDSAI
          - RMKFPISAI
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: REMARK
        SRVLBOFLAG:
          name: '本地业务分流标识'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
        WORKERNAME:
          name: '通用Rule子策略名称'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        WORKERPARA:
          name: '通用策略参数'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_userprofile_list_1:
      type: items
      properties:
        USERPROFILENAME:
          name: '用户模板名称'
          type: string
          required: false
          description: '配置用户模板。该UserProfile用于标识媒体中继业务相关的预定义规则。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        UPTYPE:
          name: '用户模板类型'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        PROFILERANGE:
          name: '模板生效范围'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_rulebinding_list_1:
      type: items
      properties:
        USERPROFILENAME:
          name: '用户模板名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '配置用户模板与规则的绑定关系。用户模板名称已通过**ADD USERPROFILE**完成配置，规则名称已通过**ADD RULE**完成配置。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        RULENAME:
          name: '规则名称'
          type: string
          minLength: 0
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
          - HEADEN
          - IPREDIR
          - LBO
          - PCC
          - QOS
          - REMARK_FPI
          - SMARTREDIRECT
          - SRV_TRIGGER
          - TRAFFICCLASS
          - WEBPROXY
          - WORKER
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
  examples:
    add_apnsmcomfunc_list:
    - APN: huawei.com
      GETPOLICYFIRST: ENABLE
    add_rule_list:
    - RULENAME: 'relayrule'
      POLICYTYPE: NON_SPECIFIC_TYPE
      FILTERINGMODE: ''
      FLOWFILTERNAME: ''
      FLWFLTRGRPNAME: ''
      ADCMUTEFLAG: ENABLE
      ALGSWITCH: DISABLE
      POLICYNAME: ''
      RDSTRIGGERFLAG: DISABLE
      REDIRIPVERFLAG: ''
      REMARKFPISEL: REMARK
      SRVLBOFLAG: DISABLE
      WORKERNAME: ''
      WORKERPARA: ''
    add_userprofile_list:
    - USERPROFILENAME: testuserprofilename
      UPTYPE: UPSELECT
      RELAYSW: ENABLE
    add_rulebinding_list:
    - USERPROFILENAME: 'testuserprofilename'
      RULENAME: 'relayrule'
      POLICYTYPE: NON_SPECIFIC_TYPE
    add_selectruleinfo_list:
    - RULENAME: testuserprofilename
      RULEFUNC: QOSANA-0&QOSEXP-0&QOSCCC-0&RELAY-1
      DELIVERSW: ENABLE
      RULERANGE: CENTRAL
      PRIORITY: '1'
    add_upfbindselrule_list:
    - INDEX: '0'
      NFINSTANCENAME: upf_instance_3
      RULENAME: testuserprofilename
    set_pfcppvtext_list:
    - FEATURE: Feature_Rule
      SWITCH: ENABLE
    add_apnsmcomfunc_list_1:
    - APN: huawei.com
      GETPOLICYFIRST: ENABLE
    add_selectruleinfo_list_1:
    - RULENAME: select_relay_upf
      RULEFUNC: QOSANA-0&QOSEXP-0&QOSCCC-0&RELAY-1
      DELIVERSW: ENABLE
      RULERANGE: CENTRAL
      PRIORITY: '2'
    add_upfbindselrule_list_1:
    - INDEX: '1'
      NFINSTANCENAME: upf_instance_3
      RULENAME: select_relay_upf
    set_pfcppvtext_list_1:
    - FEATURE: Feature_Rule
      SWITCH: ENABLE
    add_rule_list_1:
    - RULENAME: 'relayrule'
      POLICYTYPE: NON_SPECIFIC_TYPE
      FILTERINGMODE: ''
      FLOWFILTERNAME: ''
      FLWFLTRGRPNAME: ''
      ADCMUTEFLAG: ENABLE
      ALGSWITCH: DISABLE
      POLICYNAME: ''
      RDSTRIGGERFLAG: DISABLE
      REDIRIPVERFLAG: ''
      REMARKFPISEL: REMARK
      SRVLBOFLAG: DISABLE
      WORKERNAME: ''
      WORKERPARA: ''
    add_userprofile_list_1:
    - USERPROFILENAME: testuserprofilename
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
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_apnsmcomfunc_list的变量区（command: ADD APNSMCOMFUNC） -#}
<!-- MISSING_MACRO: command=ADD APNSMCOMFUNC list_name=add_apnsmcomfunc_list step_id=1.2 -->
```

#### 1.3 配置业务策略规则。

```jinja2
{%- if is_scenario_pcc_rules -%}
    {%- for item in add_rule_list -%}
        ADD RULE:
        {#- --- 必选参数 --- -#}
        RULENAME="{{item.RULENAME}}",
        POLICYTYPE={{item.POLICYTYPE}},
        FILTERINGMODE={{item.FILTERINGMODE}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：POLICYTYPE=ADC 时必选 --- -#}
        {%- if item.POLICYTYPE == 'ADC' -%}
            ADCMUTEFLAG={{item.ADCMUTEFLAG}},
        {%- endif -%}
        {#- --- 条件必选：FILTERINGMODE=FLOWFILTER 时必选 --- -#}
        {%- if item.FILTERINGMODE == 'FLOWFILTER' -%}
            FLOWFILTERNAME="{{item.FLOWFILTERNAME}}",
        {%- endif -%}
        {#- --- 条件必选：FILTERINGMODE=FLOWFILTERGRP 时必选 --- -#}
        {%- if item.FILTERINGMODE == 'FLOWFILTERGRP' -%}
            FLWFLTRGRPNAME="{{item.FLWFLTRGRPNAME}}",
        {%- endif -%}
        {#- --- 条件必选：POLICYTYPE=PCC/BWM/HEADEN/SMARTREDIRECT/TRAFFICCLASS/FIREWALL/QOS/WEBPROXY 时必选 --- -#}
        {%- if item.POLICYTYPE in ['PCC', 'BWM', 'HEADEN', 'SMARTREDIRECT', 'TRAFFICCLASS', 'FIREWALL', 'QOS', 'WEBPROXY'] -%}
            POLICYNAME="{{item.POLICYNAME}}",
        {%- endif -%}
        {#- --- 条件必选：POLICYTYPE=SRV_TRIGGER 时必选 --- -#}
        {%- if item.POLICYTYPE == 'SRV_TRIGGER' -%}
            RDSTRIGGERFLAG={{item.RDSTRIGGERFLAG}},
        {%- endif -%}
        {#- --- 条件必选：POLICYTYPE=IPREDIR 时必选 --- -#}
        {%- if item.POLICYTYPE == 'IPREDIR' -%}
            REDIRIPVERFLAG={{item.REDIRIPVERFLAG}},
        {%- endif -%}
        {#- --- 条件必选：POLICYTYPE=REMARK_FPI 时必选 --- -#}
        {%- if item.POLICYTYPE == 'REMARK_FPI' -%}
            REMARKFPISEL={{item.REMARKFPISEL}},
        {%- endif -%}
        {#- --- 条件必选：POLICYTYPE=LBO 时必选 --- -#}
        {%- if item.POLICYTYPE == 'LBO' -%}
            SRVLBOFLAG={{item.SRVLBOFLAG}},
        {%- endif -%}
        {#- --- 条件必选：POLICYTYPE=WORKER 时必选 --- -#}
        {%- if item.POLICYTYPE == 'WORKER' -%}
            WORKERNAME="{{item.WORKERNAME}}",
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：POLICYTYPE=WEBPROXY 时可选 --- -#}
        {%- if item.POLICYTYPE == 'WEBPROXY' -%}
            {%- if item.ALGSWITCH is not none -%}
                ALGSWITCH={{item.ALGSWITCH}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：POLICYTYPE=WORKER 时可选 --- -#}
        {%- if item.POLICYTYPE == 'WORKER' -%}
            {%- if item.WORKERPARA is not none -%}
                WORKERPARA="{{item.WORKERPARA}}",
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_userprofile_list的变量区（command: ADD USERPROFILE） -#}
<!-- MISSING_MACRO: command=ADD USERPROFILE list_name=add_userprofile_list step_id=1.3 -->
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
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_selectruleinfo_list的变量区（command: ADD SELECTRULEINFO） -#}
<!-- MISSING_MACRO: command=ADD SELECTRULEINFO list_name=add_selectruleinfo_list step_id=1.4 -->
```

#### 1.5 配置用户面支持媒体中继业务。upf\_instance\_3支持媒体中继业务。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_upfbindselrule_list的变量区（command: ADD UPFBINDSELRULE） -#}
<!-- MISSING_MACRO: command=ADD UPFBINDSELRULE list_name=add_upfbindselrule_list step_id=1.5 -->
```

#### 1.6 配置在PFCP Session Establishment Request和PFCP Session Modification Request消息中携带私有信元ActivatedFeatureRule/DeactivatedFeatureRule。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_pfcppvtext_list的变量区（command: SET PFCPPVTEXT） -#}
<!-- MISSING_MACRO: command=SET PFCPPVTEXT list_name=set_pfcppvtext_list step_id=1.6 -->
```

### 2 配置选择媒体中继UPF（PCF通过upfSelectRules信元下发UPF选择规则）

#### 2.1 进入“MML命令行-UNC”窗口。

#### 2.2 配置SMF支持基于用户签约选择媒体中继UPF。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_apnsmcomfunc_list_1的变量区（command: ADD APNSMCOMFUNC） -#}
<!-- MISSING_MACRO: command=ADD APNSMCOMFUNC list_name=add_apnsmcomfunc_list_1 step_id=2.2 -->
```

#### 2.3 配置UPF选择规则信息。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_selectruleinfo_list_1的变量区（command: ADD SELECTRULEINFO） -#}
<!-- MISSING_MACRO: command=ADD SELECTRULEINFO list_name=add_selectruleinfo_list_1 step_id=2.3 -->
```

#### 2.4 配置规则和UPF的绑定关系。upf\_instance\_3支持媒体中继业务。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_upfbindselrule_list_1的变量区（command: ADD UPFBINDSELRULE） -#}
<!-- MISSING_MACRO: command=ADD UPFBINDSELRULE list_name=add_upfbindselrule_list_1 step_id=2.4 -->
```

#### 2.5 配置在PFCP Session Establishment Request和PFCP Session Modification Request消息中携带私有信元ActivatedFeatureRule/DeactivatedFeatureRule。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_pfcppvtext_list_1的变量区（command: SET PFCPPVTEXT） -#}
<!-- MISSING_MACRO: command=SET PFCPPVTEXT list_name=set_pfcppvtext_list_1 step_id=2.5 -->
```

#### 2.6 配置业务策略规则。标识媒体中继业务相关的预定义规则。

```jinja2
{%- if is_scenario_upf_select_rules -%}
    {%- for item in add_rule_list_1 -%}
        ADD RULE:
        {#- --- 必选参数 --- -#}
        RULENAME="{{item.RULENAME}}",
        POLICYTYPE={{item.POLICYTYPE}},
        FILTERINGMODE={{item.FILTERINGMODE}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：POLICYTYPE=ADC 时必选 --- -#}
        {%- if item.POLICYTYPE == 'ADC' -%}
            ADCMUTEFLAG={{item.ADCMUTEFLAG}},
        {%- endif -%}
        {#- --- 条件必选：FILTERINGMODE=FLOWFILTER 时必选 --- -#}
        {%- if item.FILTERINGMODE == 'FLOWFILTER' -%}
            FLOWFILTERNAME="{{item.FLOWFILTERNAME}}",
        {%- endif -%}
        {#- --- 条件必选：FILTERINGMODE=FLOWFILTERGRP 时必选 --- -#}
        {%- if item.FILTERINGMODE == 'FLOWFILTERGRP' -%}
            FLWFLTRGRPNAME="{{item.FLWFLTRGRPNAME}}",
        {%- endif -%}
        {#- --- 条件必选：POLICYTYPE=PCC/BWM/HEADEN/SMARTREDIRECT/TRAFFICCLASS/FIREWALL/QOS/WEBPROXY 时必选 --- -#}
        {%- if item.POLICYTYPE in ['PCC', 'BWM', 'HEADEN', 'SMARTREDIRECT', 'TRAFFICCLASS', 'FIREWALL', 'QOS', 'WEBPROXY'] -%}
            POLICYNAME="{{item.POLICYNAME}}",
        {%- endif -%}
        {#- --- 条件必选：POLICYTYPE=SRV_TRIGGER 时必选 --- -#}
        {%- if item.POLICYTYPE == 'SRV_TRIGGER' -%}
            RDSTRIGGERFLAG={{item.RDSTRIGGERFLAG}},
        {%- endif -%}
        {#- --- 条件必选：POLICYTYPE=IPREDIR 时必选 --- -#}
        {%- if item.POLICYTYPE == 'IPREDIR' -%}
            REDIRIPVERFLAG={{item.REDIRIPVERFLAG}},
        {%- endif -%}
        {#- --- 条件必选：POLICYTYPE=REMARK_FPI 时必选 --- -#}
        {%- if item.POLICYTYPE == 'REMARK_FPI' -%}
            REMARKFPISEL={{item.REMARKFPISEL}},
        {%- endif -%}
        {#- --- 条件必选：POLICYTYPE=LBO 时必选 --- -#}
        {%- if item.POLICYTYPE == 'LBO' -%}
            SRVLBOFLAG={{item.SRVLBOFLAG}},
        {%- endif -%}
        {#- --- 条件必选：POLICYTYPE=WORKER 时必选 --- -#}
        {%- if item.POLICYTYPE == 'WORKER' -%}
            WORKERNAME="{{item.WORKERNAME}}",
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：POLICYTYPE=WEBPROXY 时可选 --- -#}
        {%- if item.POLICYTYPE == 'WEBPROXY' -%}
            {%- if item.ALGSWITCH is not none -%}
                ALGSWITCH={{item.ALGSWITCH}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：POLICYTYPE=WORKER 时可选 --- -#}
        {%- if item.POLICYTYPE == 'WORKER' -%}
            {%- if item.WORKERPARA is not none -%}
                WORKERPARA="{{item.WORKERPARA}}",
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_userprofile_list_1的变量区（command: ADD USERPROFILE） -#}
<!-- MISSING_MACRO: command=ADD USERPROFILE list_name=add_userprofile_list_1 step_id=2.6 -->
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


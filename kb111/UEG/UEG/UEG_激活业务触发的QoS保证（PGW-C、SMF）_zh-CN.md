---
id: GWFD-022307
name: 激活业务触发的QoS保证（PGW-C、SMF）
ne_type: UEG
type: feature
description: 当运营商规划需要为指定业务提供专有承载/专有QoS Flow时，需要参考本页面进行配置。  适用于PGW-C、SMF
tags: []
risk_level: ''
doc_source: ["业务配置","风筝L","MEC 特性指南（风筝L）","GW-U&UPF特性指南","GWFD-022300 智能QoS管理增强","GWFD-022307 业务触发的QoS保证","激活业务触发的QoS保证","激活业务触发的QoS保证（PGW-C、SMF）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
当运营商规划需要为指定业务提供专有承载/专有QoS Flow时，需要参考本页面进行配置。适用于PGW-C、SMF

## 必备事项
前提条件

* 请仔细阅读GWFD-022307 业务触发的QoS保证。
* 完成加载license（如果有需求，请联系华为技术支持工程师处理）。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
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
    add_cpurr_list:
      type: items
      properties:
        URRNAME:
          name: '使用量上报规则名称'
          type: string
          maxLength: 31
          required: true
          description: '存在多条记录时，不能重复。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        URRID:
          name: 'URR标识'
          type: integer
          minimum: 0
          maximum: 2147483646
          required: true
          description: 'URRID在所有URR内唯一，建议分配大于1000的值。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        USAGERPTMODE:
          name: '使用量上报模式'
          type: string
          enum:
          - MONITORINGKEY
          - OFFLINE
          - ONLINE
          - QOS
          required: true
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: ''
    add_cpqosprop_list:
      type: items
      properties:
        QOSPROPNAME:
          name: 'QoS属性名称'
          type: string
          maxLength: 31
          required: true
          description: '存在多条记录时，不能重复。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        GBRUPLKVALUE:
          name: '保证的上行比特率'
          type: integer
          minimum: 0
          maximum: 20000000
          required: false
          description: '此处数据仅为举例，请根据业务模型进行规划。  创建专有QoSFlow/专有承载时，以SMF上此处配置的为准。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        GBRDNLKVALUE:
          name: '保证的下行比特率'
          type: integer
          minimum: 0
          maximum: 20000000
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        MBRUPLKVALUE:
          name: '最大上行比特率'
          type: integer
          minimum: 0
          maximum: 20000000
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        MBRDNLKVALUE:
          name: '最大下行比特率'
          type: integer
          minimum: 0
          maximum: 20000000
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        QOSTYPE:
          name: 'QoS属性类型'
          type: string
          enum:
          - QOS_BEARER_PARA
          - QOS_FLOW_PARA
          - QOS_L2_PARA
          required: true
          description: '5G用户使用QOS_FLOW_PARA，2/3/4G用户使用QOS_BEARER_PARA。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        ARPVALUE:
          name: '分配保留优先级'
          type: integer
          minimum: 1
          maximum: 15
          required: false
          description: '值越小优先级越高。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        FQI:
          name: '5G QoS标识'
          type: integer
          minimum: 1
          maximum: 255
          required: false
          description: '“QOSTYPE”为“QOS_FLOW_PARA”时需要规划。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        QOSURRNAME:
          name: 'QoS使用量上报规则名称'
          type: string
          maxLength: 31
          required: false
          description: '使用**ADD CPURR**定义的URRNAME。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        EMPCAP:
          name: 'QoS抢占能力'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '该业务可以抢占已经分配给其他低优先级业务流的资源时，设置为ENABLE。此处以不抢占为例。'
          data_source: '本端规划'
          pattern: ''
          default: DISABLE
        EMPVUL:
          name: 'QoS被抢占设置'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '其他高优先级业务不能抢占本业务流的资源时，设置为DISABLE。此处以被抢占为例。'
          data_source: '本端规划'
          pattern: ''
          default: ENABLE
        QCIVALUE:
          name: 'QoS等级标识'
          type: integer
          minimum: 1
          maximum: 255
          required: false
          description: '“QOSTYPE”为“QOS_BEARER_PARA”时需要规划。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_cppccpolicygrp_list:
      type: items
      properties:
        PCCPOLICYGRPNM:
          name: 'PCC策略组名称'
          type: string
          maxLength: 63
          required: true
          description: '存在多条记录时，该参数不能重复。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        QOSPROPNAME:
          name: 'Qos属性名称'
          type: string
          maxLength: 31
          required: false
          description: '使用**ADD CPQOSPROP**定义的QOSPROPNAME。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        URRGROUPNAME:
          name: '使用量上报规则组名称'
          type: string
          maxLength: 31
          required: false
          description: '使用**ADD CPURRGROUP**定义的URRGROUPNAME。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_cprule_list:
      type: items
      properties:
        RULENAME:
          name: '规则名称'
          type: string
          maxLength: 63
          required: true
          description: '存在多条数据时，该参数+策略类型不能完全相同。'
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
          required: true
          description: '“POLICYTYPE”设置为“PCC”时，“POLICYNAME”使用**ADD CPPCCPOLICYGRP**定义的PCCPOLICYGRPNM。  “POLICYTYPE”设置为“QOS”时，“POLICYNAME”使用**ADD CPQOSPROP**  定义的QOSPROPNAME。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        POLICYNAME:
          name: '策略名称'
          type: string
          maxLength: 63
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_cpuserprofile_list:
      type: items
      properties:
        USERPROFILENAME:
          name: '用户模板名称'
          type: string
          maxLength: 63
          required: true
          description: '配置SMF上的UserProfile。'
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
          data_source: '固定取值'
          pattern: ''
          default: PCC
    add_cprulebinding_list:
      type: items
      properties:
        USERPROFILENAME:
          name: '用户模板名称'
          type: string
          maxLength: 63
          required: true
          description: '将本地rule/预定义规则rule绑定到UserProfile上。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        RULENAME:
          name: '规则名称'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: '已配置数据中获取'
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
          description: '如果不指定策略类型，则把规则名称相同的所有策略类型的规则绑定到用户模板上。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_usrprofgroup_list:
      type: items
      properties:
        USERPROFGNAME:
          name: '用户模板组名称'
          type: string
          maxLength: 63
          required: true
          description: '配置UserProfile Group。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_upbindupg_list:
      type: items
      properties:
        USERPROFGNAME:
          name: '用户模板组名称'
          type: string
          maxLength: 63
          required: true
          description: '将UserProfile绑定到UserProfile Group。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        UPBINDTYPE:
          name: '用户模板绑定类型'
          type: string
          enum:
          - DEFAULT
          - SPECIFIC
          - ULCL
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        USERPROFILENAME:
          name: '用户模板名称'
          type: string
          maxLength: 63
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_apnusrprofg_list:
      type: items
      properties:
        APN:
          name: 'APN'
          type: string
          maxLength: 63
          required: true
          description: '将UserProfile Group绑定到DNN。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        USERPROFGNAME:
          name: '用户模板组名称'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV3W9STQE11'
      SWITCH: ENABLE
    add_cpurr_list:
    - URRNAME: 'urr_1'
      URRID: 1001
      USAGERPTMODE: QOS
    add_cpqosprop_list:
    - QOSPROPNAME: 'qos-property1'
      GBRUPLKVALUE: 110
      GBRDNLKVALUE: 110
      MBRUPLKVALUE: 220
      MBRDNLKVALUE: 220
      QOSTYPE: QOS_FLOW_PARA
      ARPVALUE: 5
      FQI: 2
      QOSURRNAME: 'urr_1'
      EMPCAP: DISABLE
      EMPVUL: ENABLE
      QCIVALUE: 66
    add_cppccpolicygrp_list:
    - PCCPOLICYGRPNM: 'ppg1'
      QOSPROPNAME: 'qos-property1'
      URRGROUPNAME: 'urrgroup1'
    add_cprule_list:
    - RULENAME: 'rule_test'
      POLICYTYPE: PCC
      POLICYNAME: 'ppg1'
    add_cpuserprofile_list:
    - USERPROFILENAME: 'up_test'
      UPTYPE: PCC
    add_cprulebinding_list:
    - USERPROFILENAME: 'up_test'
      RULENAME: 'rule_test'
      POLICYTYPE: QOS
    add_usrprofgroup_list:
    - USERPROFGNAME: 'upg_test'
    add_upbindupg_list:
    - USERPROFGNAME: 'upg_test'
      UPBINDTYPE: DEFAULT
      USERPROFILENAME: 'up_test'
    add_apnusrprofg_list:
    - APN: 'huawei.com'
      USERPROFGNAME: 'upg_test'
```

## 3 命令模板定义
<!-- @mml:block= commands -->

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

### 2 配置QoS URR。

```jinja2
{%- for item in add_cpurr_list -%}
    ADD CPURR:
    {#- --- 必选参数 --- -#}
    URRNAME="{{item.URRNAME}}",
    URRID={{item.URRID}},
    USAGERPTMODE={{item.USAGERPTMODE}},
    ;
{%- endfor -%}
```

### 3 配置QoS属性。

```jinja2
{%- for item in add_cpqosprop_list -%}
    ADD CPQOSPROP:
    {#- --- 必选参数 --- -#}
    QOSPROPNAME="{{item.QOSPROPNAME}}",
    QOSTYPE={{item.QOSTYPE}},
    {#- --- 可选参数 --- -#}
    {%- if item.GBRUPLKVALUE is not none -%}
        GBRUPLKVALUE={{item.GBRUPLKVALUE}},
    {%- endif -%}
    {%- if item.GBRDNLKVALUE is not none -%}
        GBRDNLKVALUE={{item.GBRDNLKVALUE}},
    {%- endif -%}
    {%- if item.MBRUPLKVALUE is not none -%}
        MBRUPLKVALUE={{item.MBRUPLKVALUE}},
    {%- endif -%}
    {%- if item.MBRDNLKVALUE is not none -%}
        MBRDNLKVALUE={{item.MBRDNLKVALUE}},
    {%- endif -%}
    {%- if item.EMPCAP is not none -%}
        EMPCAP={{item.EMPCAP}},
    {%- endif -%}
    {%- if item.EMPVUL is not none -%}
        EMPVUL={{item.EMPVUL}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：QOSTYPE=QOS_FLOW_PARA/QOS_L2_PARA 时必选 --- -#}
    {%- if item.QOSTYPE in ['QOS_FLOW_PARA', 'QOS_L2_PARA'] -%}
        FQI={{item.FQI}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：QOSTYPE=QOS_BEARER_PARA/QOS_FLOW_PARA 时可选 --- -#}
    {%- if item.QOSTYPE in ['QOS_BEARER_PARA', 'QOS_FLOW_PARA'] -%}
        {%- if item.QOSURRNAME is not none -%}
            QOSURRNAME="{{item.QOSURRNAME}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：QOSTYPE=QOS_BEARER_PARA 时可选 --- -#}
    {%- if item.QOSTYPE == 'QOS_BEARER_PARA' -%}
        {%- if item.QCIVALUE is not none -%}
            QCIVALUE={{item.QCIVALUE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件必选/可选参数 --- -#}
    {#- --- 分配保留优先级: 条件必选(QoS属性类型=QOS_FLOW_PARA|QOS_L2_PARA) / 条件可选(QoS属性类型=QOS_BEARER_PARA) --- -#}
    {%- if (item.QOSTYPE in ['QOS_FLOW_PARA', 'QOS_L2_PARA']) -%}
        ARPVALUE={{item.ARPVALUE}},
    {%- elif (item.QOSTYPE == 'QOS_BEARER_PARA') -%}
        {%- if item.ARPVALUE is not none -%}
            ARPVALUE={{item.ARPVALUE}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 规则通过PCC策略组绑定QoS属性时，配置PCC策略组。规则直接绑定QoS属性时，请跳过本步骤。

```jinja2
{%- if is_scenario_pcc_policy_group -%}
    {%- for item in add_cppccpolicygrp_list -%}
        ADD CPPCCPOLICYGRP:
        {#- --- 必选参数 --- -#}
        PCCPOLICYGRPNM="{{item.PCCPOLICYGRPNM}}",
        {#- --- 可选参数 --- -#}
        {%- if item.QOSPROPNAME is not none -%}
            QOSPROPNAME="{{item.QOSPROPNAME}}",
        {%- endif -%}
        {%- if item.URRGROUPNAME is not none -%}
            URRGROUPNAME="{{item.URRGROUPNAME}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 5 配置SMF上的本地rule。

```jinja2
{%- for item in add_cprule_list -%}
    ADD CPRULE:
    {#- --- 必选参数 --- -#}
    RULENAME="{{item.RULENAME}}",
    POLICYTYPE={{item.POLICYTYPE}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：POLICYTYPE=PCC/ULCL/QOS 时必选 --- -#}
    {%- if item.POLICYTYPE in ['PCC', 'ULCL', 'QOS'] -%}
        POLICYNAME="{{item.POLICYNAME}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 5.1 规则通过PCC策略组绑定QoS属性时，“POLICYTYPE”设置为“PCC”，“POLICYNAME”使用**ADD CPPCCPOLICYGRP**命令配置的“PCCPOLICYGRPNM”参数值。

#### 5.2 规则直接绑定QoS属性时，“POLICYTYPE”设置为“QOS”“POLICYNAME”使用**ADD CPQOSPROP**命令配置的“QOSPROPNAME”参数值。

#### 5.3 PCC类型的“RULENAME”值与QOS类型的“RULENAME”值不能相同。

### 6 （无可用PCRF/PCF或预定义规则组时使用）配置SMF上的UserProfile，将本地rule绑定到UserProfile上。用于动态PCC时PCF下发预定义规则组，或本地PCC时的静态规则组。

#### 6.1 配置UserProfile。

```jinja2
{%- if is_scenario_no_pcrf_pcf -%}
    {%- for item in add_cpuserprofile_list -%}
        ADD CPUSERPROFILE:
        {#- --- 必选参数 --- -#}
        USERPROFILENAME="{{item.USERPROFILENAME}}",
        UPTYPE={{item.UPTYPE}},
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 6.2 将rule绑定到UserProfile。

```jinja2
{%- if is_scenario_no_pcrf_pcf -%}
    {%- for item in add_cprulebinding_list -%}
        ADD CPRULEBINDING:
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

### 7 **可选：**（无可用PCRF/PCF时使用）配置UserProfile组，将UserProfile绑定到UserProfile组，再将UserProfile组绑定到DNN实例上。用于本地PCC的静态规则。如UserProfile已配置，请跳过本步骤。

#### 7.1 配置UserProfile Group。

```jinja2
{%- if is_optional_userprofile_group and is_scenario_no_pcrf_pcf -%}
    {%- for item in add_usrprofgroup_list -%}
        ADD USRPROFGROUP:
        {#- --- 必选参数 --- -#}
        USERPROFGNAME="{{item.USERPROFGNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 7.2 将UserProfile绑定到UserProfile Group。

```jinja2
{%- if is_optional_userprofile_group and is_scenario_no_pcrf_pcf -%}
    {%- for item in add_upbindupg_list -%}
        ADD UPBINDUPG:
        {#- --- 必选参数 --- -#}
        USERPROFGNAME="{{item.USERPROFGNAME}}",
        UPBINDTYPE={{item.UPBINDTYPE}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：UPBINDTYPE=SPECIFIC/DEFAULT/ULCL 时必选 --- -#}
        {%- if item.UPBINDTYPE in ['SPECIFIC', 'DEFAULT', 'ULCL'] -%}
            USERPROFILENAME="{{item.USERPROFILENAME}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 7.3 将UserProfile Group绑定到DNN。

```jinja2
{%- if is_optional_userprofile_group and is_scenario_no_pcrf_pcf -%}
    {%- for item in add_apnusrprofg_list -%}
        ADD APNUSRPROFG:
        {#- --- 必选参数 --- -#}
        APN="{{item.APN}}",
        USERPROFGNAME="{{item.USERPROFGNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```


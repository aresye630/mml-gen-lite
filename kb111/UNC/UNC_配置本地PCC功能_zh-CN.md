---
id: ''
name: 配置本地PCC功能
ne_type: UNC
type: feature
description: 当网络中无PCRF，而通过特定APN激活的用户需要激活为PCC用户，且为该PCC用户的特定业务创建专有承载以提供QoS保障，此时需要开启本地PCC功能，并在本地配置静态规则，策略匹配时按照rule的全局优先级进行匹配。  UNC上开启本地PCC功能时，需要在UNC上配置rule和UserProfile，本处在UNC上仅开启PCC功能开关，不关注具体规则内容配置，具体规则内容需要根据具体业务策略确定。  适用于GGSN、PGW-C。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","智能PCC解决方案","WSFD-109101 PCC基本功能","PCC基本功能（2G/3G/4G，基于Gx接口）","激活PCC基本功能","配置本地PCC功能"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools:
- getParameterValue('ADD UPBINDUPG')
---
<!-- @mml:block=annotations -->
```text
## 操作场景
当网络中无PCRF，而通过特定APN激活的用户需要激活为PCC用户，且为该PCC用户的特定业务创建专有承载以提供QoS保障，此时需要开启本地PCC功能，并在本地配置静态规则，策略匹配时按照rule的全局优先级进行匹配。UNC上开启本地PCC功能时，需要在UNC上配置rule和UserProfile，本处在UNC上仅开启PCC功能开关，不关注具体规则内容配置，具体规则内容需要根据具体业务策略确定。适用于GGSN、PGW-C。

## 必备事项
前提条件

* 请仔细阅读PCC基本功能（2G/3G/4G，基于Gx接口）。
* 完成**加载license**（如果有需求，请联系华为技术支持工程师处理）
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
    set_pccfunc_list:
      type: items
      properties:
        HOMEPCCSWITCH:
          name: '本地用户PCC功能'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '使能GGSN/PGW-C上的全局用户的本地PCC功能。  网络中未部署PCRF时，设置为DISABLE。否则需要设置为ENABLE。  APN粒度（**SET APNPCCFUNC**）的优先级高于全局粒度（**SET PCCFUNC**）。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        ROAMPCCSWITCH:
          name: '漫游用户PCC功能'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VISITPCCSWITCH:
          name: '拜访用户PCC功能'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_pcctemplate_list:
      type: items
      properties:
        PCCTEMPNAME:
          name: 'PCC模板名称'
          type: string
          maxLength: 63
          required: true
          description: '配置PCC模板，将PCC模板配置为本地PCC。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        INITIALFAILACT:
          name: 'Initial流程故障处理动作'
          type: string
          enum:
          - FORBIDDEN
          - INHERIT
          - ROLLBACK
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: INHERIT
        UPDATEFAILACT:
          name: 'Update流程故障处理动作'
          type: string
          enum:
          - CONTINUE
          - INHERIT
          - ROLLBACK
          - TERMINATE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: INHERIT
        INITFAILLOCPCC:
          name: 'Initial流程故障回滚为Local PCC用户类型'
          type: string
          enum:
          - LOCAL_PCC
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: LOCAL_PCC
        INITFAILRDSPCC:
          name: 'Initial流程故障回滚为RADIUS PCC用户类型'
          type: string
          enum:
          - LOCAL_PCC
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: LOCAL_PCC
        UPDFAILLOCPCC:
          name: 'Update流程故障回滚为Local PCC用户类型'
          type: string
          enum:
          - INHERIT_PCC
          - LOCAL_PCC
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: LOCAL_PCC
    set_apnpccfunc_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          maxLength: 63
          required: true
          description: '针对指定的APN配置本地PCC使能开关，绑定PCC模板。  APN粒度（**SET APNPCCFUNC**）的优先级高于全局粒度（**SET PCCFUNC**）。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        HOMEPCCSWITCH:
          name: '本地用户PCC功能'
          type: string
          enum:
          - DISABLE
          - ENABLE
          - INHERIT
          required: false
          description: ''
          data_source: '对端协商'
          pattern: ''
          default: ''
        ROAMPCCSWITCH:
          name: '漫游用户PCC功能'
          type: string
          enum:
          - DISABLE
          - ENABLE
          - INHERIT
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VISITPCCSWITCH:
          name: '拜访用户PCC功能'
          type: string
          enum:
          - DISABLE
          - ENABLE
          - INHERIT
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PCCTEMPLATE:
          name: 'PCC模板名称'
          type: string
          maxLength: 63
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_qosprop_list:
      type: items
      properties:
        QOSPROPNAME:
          name: 'QoS属性名称'
          type: string
          maxLength: 31
          required: true
          description: '配置QoS类型的PCC策略。'
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
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        ARPVALUE:
          name: '分配保留优先级'
          type: integer
          minimum: 1
          maximum: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        FQI:
          name: '5G QoS标识'
          type: integer
          minimum: 1
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        QCIVALUE:
          name: 'QoS等级标识'
          type: integer
          minimum: 1
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        QOSURRNAME:
          name: 'QoS使用量上报规则名称'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RQI:
          name: '反射QoS指示'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_pccpolicygrp_list:
      type: items
      properties:
        PCCPOLICYGRPNM:
          name: 'PCC策略组名称'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        QOSPROPNAME:
          name: 'Qos属性名称'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: '已配置数据中获取'
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
          description: '增加rule。'
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
          data_source: '已配置数据中获取'
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
          description: 'PGW-C支持将规则下发给主锚点PGW-U+辅锚点PGW-U、主锚点PGW-U或辅锚点PGW-U。  此处以rule同时下发给主锚点PGW-U和辅锚点PGW-U为例。  rule只下发给主锚点PGW-U时，需设置为“CENTRAL”；rule只下发给辅锚点PGW-U时，需设置为“LOCAL”。'
          data_source: '全网规划'
          pattern: ''
          default: ALL
        FLOWFILTERNAME:
          name: '流过滤器名称'
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
    add_rulebinddnai_list:
      type: items
      properties:
        RULENAME:
          name: '规则名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '配置的rule需要下发给指定的辅锚点PGW-U时需要配置。例如，rule的“规则生效范围”设置为“LOCAL”时，该规则只下发给DNAI是huawei.com的辅锚点PGW-U。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        DNAI:
          name: '数据网络访问标识符'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_userprofile_list:
      type: items
      properties:
        USERPROFILENAME:
          name: '用户模板名称'
          type: string
          maxLength: 63
          required: true
          description: '配置GGSN/PGW-C上的UserProfile，将本地rule绑定到UserProfile上。'
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
        PROFILERANGE:
          name: '模板生效范围'
          type: string
          enum:
          - ALL
          - CENTRAL
          - LOCAL
          required: false
          description: 'PGW-C支持将UserProfile下发给主锚点PGW-U+辅锚点PGW-U、主锚点PGW-U或辅锚点PGW-U。  此处以Userprofile同时下发给主锚点PGW-U和辅锚点PGW-U为例。  Userprofile只下发给主锚点PGW-U时，需设置为“CENTRAL”；Userprofile只下发给辅锚点PGW-U时，需设置为“LOCAL”。'
          data_source: '全网规划'
          pattern: ''
          default: ALL
    add_usrprobinddnai_list:
      type: items
      properties:
        USRPRONAME:
          name: '用户模板名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '配置的Userprofile需要下发给指定的辅锚点PGW-U时需要配置。例如，Userprofile的“模板生效范围”设置为“LOCAL”时，该Userprofile只下发给DNAI是test.com的辅锚点PGW-U。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        DNAI:
          name: '数据网络访问标识符'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_rulebinding_list:
      type: items
      properties:
        USERPROFILENAME:
          name: '用户模板名称'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RULENAME:
          name: '规则名称'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: ''
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
        CCCONFIGMODE:
          name: '计费属性配置模式'
          type: string
          enum:
          - FLATBILLING
          - HOTBILLING
          - NORMAL
          - PREPAID
          - SPECIFIC
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IMEISVSEGNAME:
          name: 'IMEISV号段名称'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IMSIMSSEGNAME:
          name: 'IMSI/MSISDN号段名称'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LOCALPCCSELECT:
          name: '本地PCC策略选择模式'
          type: string
          enum:
          - INHERIT
          - LOCAL_PCC_ACTIVE
          - LOCAL_PCC_DEACTIVE
          - LOCAL_PCC_NO_CRBN_ACT
          - LOCAL_PCC_NO_RULE_ACT
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: INHERIT
        LOCGROUPNAME:
          name: '位置组名称'
          type: string
          maxLength: 63
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PRIORITY:
          name: '优先级'
          type: integer
          minimum: 1
          maximum: 65534
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RAT:
          name: 'RAT'
          type: string
          enum:
          - EMTC
          - EUTRAN
          - GAN
          - GERAN
          - HSPA
          - NBIOT
          - NONE
          - NR
          - REDCAP
          - UTRAN
          - WLAN
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ROAMING:
          name: '漫游属性'
          type: string
          enum:
          - HOME
          - NONE
          - ROAMING
          - VISITING
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SEGGROUPNAME:
          name: 'IMSI/MSISDN/IMEISV 号段组名称'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_pccpbindupg_list:
      type: items
      properties:
        USERPROFGNAME:
          name: '用户模板组名称'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PCCPROFILENAME:
          name: '用户PCC模板名称'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: ''
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
          description: '将UserProfile Group绑定到APN。'
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
    - LICITEM: 'LKV3W9SPCC11'
      SWITCH: ENABLE
    set_pccfunc_list:
    - HOMEPCCSWITCH: DISABLE
      ROAMPCCSWITCH: DISABLE
      VISITPCCSWITCH: DISABLE
    add_pcctemplate_list:
    - PCCTEMPNAME: 'pcctemplate'
      INITIALFAILACT: FORBIDDEN
      UPDATEFAILACT: INHERIT
      INITFAILLOCPCC: LOCAL_PCC
      INITFAILRDSPCC: LOCAL_PCC
      UPDFAILLOCPCC: LOCAL_PCC
    set_apnpccfunc_list:
    - APN: 'apn1'
      HOMEPCCSWITCH: DISABLE
      ROAMPCCSWITCH: DISABLE
      VISITPCCSWITCH: DISABLE
      PCCTEMPLATE: 'pcctemplate'
    add_qosprop_list:
    - QOSPROPNAME: 'qos_property1'
      QOSTYPE: QOS_BEARER_PARA
      ARPVALUE: ''
      FQI: ''
      QCIVALUE: ''
      QOSURRNAME: ''
      RQI: ''
    add_pccpolicygrp_list:
    - PCCPOLICYGRPNM: 'pccpolicy_group'
      QOSPROPNAME: 'qos_property1'
    add_rule_list:
    - RULENAME: 'rule_test'
      POLICYTYPE: PCC
      POLICYNAME: 'pccpolicy_group'
      RULERANGE: ALL
      FLOWFILTERNAME: ''
      PROTODESCDL: ''
      PROTODESCUL: ''
    add_rulebinddnai_list:
    - RULENAME: 'rule_test'
      DNAI: 'huawei.com'
    add_userprofile_list:
    - USERPROFILENAME: 'up_test'
      UPTYPE: PCC
      PROFILERANGE: ALL
    add_usrprobinddnai_list:
    - USRPRONAME: 'up_test'
      DNAI: 'test.com'
    add_rulebinding_list:
    - USERPROFILENAME: 'up_test'
      RULENAME: 'rule_test'
    add_usrprofgroup_list:
    - USERPROFGNAME: 'upg_test'
    add_upbindupg_list:
    - USERPROFGNAME: 'upg_test'
      UPBINDTYPE: DEFAULT
      USERPROFILENAME: 'up_test'
      CCCONFIGMODE: ''
      IMEISVSEGNAME: ''
      IMSIMSSEGNAME: ''
      LOCALPCCSELECT: INHERIT
      LOCGROUPNAME: ''
      PRIORITY: ''
      RAT: ''
      ROAMING: ''
      SEGGROUPNAME: ''
    add_pccpbindupg_list:
    - USERPROFGNAME: ''
      PCCPROFILENAME: ''
    add_apnusrprofg_list:
    - APN: 'apn1'
      USERPROFGNAME: 'upg_test'
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 进入“MML命令行-UNC”窗口。

### 2 打开本特性的License配置开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

### 3 关闭全局粒度的动态PCC功能。关闭后，开启的是全局粒度的本地PCC功能。

```jinja2
{%- for item in set_pccfunc_list -%}
    SET PCCFUNC:
    {#- --- 可选参数 --- -#}
    {%- if item.HOMEPCCSWITCH is not none -%}
        HOMEPCCSWITCH={{item.HOMEPCCSWITCH}},
    {%- endif -%}
    {%- if item.ROAMPCCSWITCH is not none -%}
        ROAMPCCSWITCH={{item.ROAMPCCSWITCH}},
    {%- endif -%}
    {%- if item.VISITPCCSWITCH is not none -%}
        VISITPCCSWITCH={{item.VISITPCCSWITCH}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 开启APN下的PCC开关。

#### 4.1 配置PCC模板。

```jinja2
{%- for item in add_pcctemplate_list -%}
    ADD PCCTEMPLATE:
    {#- --- 必选参数 --- -#}
    PCCTEMPNAME="{{item.PCCTEMPNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.INITIALFAILACT is not none -%}
        INITIALFAILACT={{item.INITIALFAILACT}},
    {%- endif -%}
    {%- if item.UPDATEFAILACT is not none -%}
        UPDATEFAILACT={{item.UPDATEFAILACT}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：INITIALFAILACT=ROLLBACK 时可选 --- -#}
    {%- if item.INITIALFAILACT == 'ROLLBACK' -%}
        {%- if item.INITFAILLOCPCC is not none -%}
            INITFAILLOCPCC={{item.INITFAILLOCPCC}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：INITIALFAILACT=ROLLBACK 时可选 --- -#}
    {%- if item.INITIALFAILACT == 'ROLLBACK' -%}
        {%- if item.INITFAILRDSPCC is not none -%}
            INITFAILRDSPCC={{item.INITFAILRDSPCC}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：UPDATEFAILACT=ROLLBACK 时可选 --- -#}
    {%- if item.UPDATEFAILACT == 'ROLLBACK' -%}
        {%- if item.UPDFAILLOCPCC is not none -%}
            UPDFAILLOCPCC={{item.UPDFAILLOCPCC}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 4.2 针对指定的APN配置PCC使能开关和PCC模板。

```jinja2
{%- for item in set_apnpccfunc_list -%}
    SET APNPCCFUNC:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    {#- --- 可选参数 --- -#}
    {%- if item.HOMEPCCSWITCH is not none -%}
        HOMEPCCSWITCH={{item.HOMEPCCSWITCH}},
    {%- endif -%}
    {%- if item.ROAMPCCSWITCH is not none -%}
        ROAMPCCSWITCH={{item.ROAMPCCSWITCH}},
    {%- endif -%}
    {%- if item.VISITPCCSWITCH is not none -%}
        VISITPCCSWITCH={{item.VISITPCCSWITCH}},
    {%- endif -%}
    {%- if item.PCCTEMPLATE is not none -%}
        PCCTEMPLATE="{{item.PCCTEMPLATE}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 5 配置PCC用户使用的业务规则。

#### 5.1 配置QoS属性。

```jinja2
{%- for item in add_qosprop_list -%}
    ADD QOSPROP:
    {#- --- 必选参数 --- -#}
    QOSPROPNAME="{{item.QOSPROPNAME}}",
    QOSTYPE={{item.QOSTYPE}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：QOSTYPE=QOS_FLOW_PARA/QOS_L2_PARA 时必选 --- -#}
    {%- if item.QOSTYPE in ['QOS_FLOW_PARA', 'QOS_L2_PARA'] -%}
        FQI={{item.FQI}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：QOSTYPE=QOS_BEARER_PARA 时可选 --- -#}
    {%- if item.QOSTYPE == 'QOS_BEARER_PARA' -%}
        {%- if item.QCIVALUE is not none -%}
            QCIVALUE={{item.QCIVALUE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：QOSTYPE=QOS_BEARER_PARA/QOS_FLOW_PARA 时可选 --- -#}
    {%- if item.QOSTYPE in ['QOS_BEARER_PARA', 'QOS_FLOW_PARA'] -%}
        {%- if item.QOSURRNAME is not none -%}
            QOSURRNAME="{{item.QOSURRNAME}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：QOSTYPE=QOS_FLOW_PARA 时可选 --- -#}
    {%- if item.QOSTYPE == 'QOS_FLOW_PARA' -%}
        {%- if item.RQI is not none -%}
            RQI={{item.RQI}},
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

#### 5.2 配置PCC策略。

```jinja2
{%- for item in add_pccpolicygrp_list -%}
    ADD PCCPOLICYGRP:
    {#- --- 必选参数 --- -#}
    PCCPOLICYGRPNM="{{item.PCCPOLICYGRPNM}}",
    {#- --- 可选参数 --- -#}
    {%- if item.QOSPROPNAME is not none -%}
        QOSPROPNAME="{{item.QOSPROPNAME}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 5.3 配置本地静态规则

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
        {%- if item.RULERANGE is not none -%}
            RULERANGE={{item.RULERANGE}},
        {%- endif -%}
    {%- endif -%}
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
    ;
{%- endfor -%}
```

#### 5.4 **可选：**配置rule和DNAI关联。可选配置，将rule下发给指定DNAI的辅锚点PGW-U时需要配置。

```jinja2
{%- if is_optional_rule_dnai_association -%}
    {%- for item in add_rulebinddnai_list -%}
        ADD RULEBINDDNAI:
        {#- --- 必选参数 --- -#}
        DNAI="{{item.DNAI}}",
        RULENAME="{{item.RULENAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

### 6 配置业务策略组合。

#### 6.1 配置UserProfile。

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

#### 6.2 **可选：**将UserProfile下发给指定DNAI的辅锚点PGW-U时，配置UserProfile和DNAI关联。

```jinja2
{%- if is_optional_userprofile_dnai_association -%}
    {%- for item in add_usrprobinddnai_list -%}
        ADD USRPROBINDDNAI:
        {#- --- 必选参数 --- -#}
        DNAI="{{item.DNAI}}",
        USRPRONAME="{{item.USRPRONAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 6.3 将已配置的rule绑定到UserProfile。

```jinja2
{%- for item in add_rulebinding_list -%}
    ADD RULEBINDING:
    {#- --- 必选参数 --- -#}
    USERPROFILENAME="{{item.USERPROFILENAME}}",
    RULENAME="{{item.RULENAME}}",
    ;
{%- endfor -%}
```

#### 6.4 配置UserProfile Group。

```jinja2
{%- for item in add_usrprofgroup_list -%}
    ADD USRPROFGROUP:
    {#- --- 必选参数 --- -#}
    USERPROFGNAME="{{item.USERPROFGNAME}}",
    ;
{%- endfor -%}
```

#### 6.5 将UserProfile绑定到UserProfile Group。

```jinja2
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
    {#- --- 条件必选：UPBINDTYPE=SPECIFIC 时必选 --- -#}
    {%- if item.UPBINDTYPE == 'SPECIFIC' -%}
        PRIORITY={{item.PRIORITY}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：UPBINDTYPE=SPECIFIC 时可选 --- -#}
    {%- if item.UPBINDTYPE == 'SPECIFIC' -%}
        {%- if item.CCCONFIGMODE is not none -%}
            CCCONFIGMODE={{item.CCCONFIGMODE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：UPBINDTYPE=SPECIFIC 时可选 --- -#}
    {%- if item.UPBINDTYPE == 'SPECIFIC' -%}
        {%- if item.IMEISVSEGNAME is not none -%}
            IMEISVSEGNAME="{{item.IMEISVSEGNAME}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：UPBINDTYPE=SPECIFIC 时可选 --- -#}
    {%- if item.UPBINDTYPE == 'SPECIFIC' -%}
        {%- if item.IMSIMSSEGNAME is not none -%}
            IMSIMSSEGNAME="{{item.IMSIMSSEGNAME}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：UPBINDTYPE=SPECIFIC/DEFAULT 时可选 --- -#}
    {%- if item.UPBINDTYPE in ['SPECIFIC', 'DEFAULT'] -%}
        {%- if item.LOCALPCCSELECT is not none -%}
            LOCALPCCSELECT={{item.LOCALPCCSELECT}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：UPBINDTYPE=SPECIFIC 时可选 --- -#}
    {%- if item.UPBINDTYPE == 'SPECIFIC' -%}
        {%- if item.LOCGROUPNAME is not none -%}
            LOCGROUPNAME="{{item.LOCGROUPNAME}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：UPBINDTYPE=SPECIFIC 时可选 --- -#}
    {%- if item.UPBINDTYPE == 'SPECIFIC' -%}
        {%- if item.RAT is not none -%}
            RAT={{item.RAT}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：UPBINDTYPE=SPECIFIC 时可选 --- -#}
    {%- if item.UPBINDTYPE == 'SPECIFIC' -%}
        {%- if item.ROAMING is not none -%}
            ROAMING={{item.ROAMING}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：UPBINDTYPE=SPECIFIC 时可选 --- -#}
    {%- if item.UPBINDTYPE == 'SPECIFIC' -%}
        {%- if item.SEGGROUPNAME is not none -%}
            SEGGROUPNAME="{{item.SEGGROUPNAME}}",
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### UserProfile Group中可以绑定多个UserProfile，本地PCC用户激活后，UNC根据**ADD UPBINDUPG**中的匹配条件最终只能为本地PCC用户安装一个UserProfile，如果要为本地PCC用户安装多个UserProfile，用以区分不同的业务套餐，需要执行步骤 6.f。

#### 6.6 **可选：**将UserProfile绑定到UserProfile Group，为本地PCC用户安装多个UserProfile。

```jinja2
{%- set ADD_UPBINDUPG=getParameterValue('ADD UPBINDUPG') -%}
{%- if is_optional_install_multiple_userprofiles and ADD_UPBINDUPG -%}
    {%- for item in add_pccpbindupg_list -%}
        ADD PCCPBINDUPG:
        {#- --- 必选参数 --- -#}
        PCCPROFILENAME="{{item.PCCPROFILENAME}}",
        USERPROFGNAME="{{item.USERPROFGNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 重复执行本步骤可以绑定多个UserProfile，实现为本地PCC用户安装多个UserProfile。

#### 用户激活后优先安装**ADD PCCPBINDUPG**命令绑定的UserProfile，如果**ADD PCCPBINDUPG**命令未绑定任何UserProfile，则使用**ADD UPBINDUPG**中绑定的UserProfile。

#### **ADD PCCPBINDUPG**命令配置后，common policy仍使用**ADD UPBINDUPG**中配置的匹配条件的UserProfile中的策略。

#### 6.7 将UserProfile Group绑定到APN。

```jinja2
{%- for item in add_apnusrprofg_list -%}
    ADD APNUSRPROFG:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    USERPROFGNAME="{{item.USERPROFGNAME}}",
    ;
{%- endfor -%}
```

#### 业务策略组合和APN建立绑定关系后，对该APN已经存在的用户无效，只对后续新激活的用户生效。


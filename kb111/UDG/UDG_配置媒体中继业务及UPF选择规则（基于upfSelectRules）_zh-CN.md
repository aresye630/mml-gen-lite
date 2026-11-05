---
id: ''
name: 配置媒体中继业务及UPF选择规则（基于upfSelectRules）
ne_type: UDG
type: feature
description: 本操作指导完成在部署媒体中继业务时，如何配置通过upfSelectRules下发UPF选择规则及业务规则。
risk_level: ''
doc_source: ["特性部署","业务专题","5G Core 媒体中继解决方案","媒体中继业务配置","新建媒体中继基础配置","配置PCF","配置媒体中继业务及UPF选择规则（基于upfSelectRules）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本操作指导完成在部署媒体中继业务时，如何配置通过upfSelectRules下发UPF选择规则及业务规则。

## 必备事项
前提条件

媒体中继业务的规则名已全网统一规划。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    add_conditiongroup_list:
      type: items
      properties:
        CONDITIONGROUPNAME:
          name: 'CONDITIONGROUPNAME'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RELATION:
          name: 'RELATION'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        USETIMEZONE:
          name: 'USETIMEZONE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_condition_list:
      type: items
      properties:
        CONDITIONGROUPNAME:
          name: 'CONDITIONGROUPNAME'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CONDITIONNAME:
          name: 'CONDITIONNAME'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        OBJECTATTRIBUTE:
          name: 'OBJECTATTRIBUTE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        OPERATOR:
          name: 'OPERATOR'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RIGHTVALUETYPE:
          name: 'RIGHTVALUETYPE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RIGHTVALUE:
          name: 'RIGHTVALUE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_ngaction_list:
      type: items
      properties:
        ACTIONNAME:
          name: 'ACTIONNAME'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TYPE:
          name: 'TYPE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_ngactionattr_list:
      type: items
      properties:
        ACTIONNAME:
          name: 'ACTIONNAME'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ATTRNAME:
          name: 'ATTRNAME'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TYPE:
          name: 'TYPE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VALUE:
          name: 'VALUE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_rule_list:
      type: items
      properties:
        RULENAME:
          name: 'RULENAME'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        OPERATION:
          name: 'OPERATION'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TYPE:
          name: 'TYPE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PRECEDENCE:
          name: 'PRECEDENCE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VOLUMEUSAGEROUNDING:
          name: 'VOLUMEUSAGEROUNDING'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        EDR:
          name: 'EDR'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RELATION:
          name: 'RELATION'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_ruleconditiongroup_list:
      type: items
      properties:
        RULENAME:
          name: 'RULENAME'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CONDITIONGROUPNAME:
          name: 'CONDITIONGROUPNAME'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_rulengaction_list:
      type: items
      properties:
        RULENAME:
          name: 'RULENAME'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ACTIONNAME:
          name: 'ACTIONNAME'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_conditiongroup_list_1:
      type: items
      properties:
        CONDITIONGROUPNAME:
          name: 'CONDITIONGROUPNAME'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RELATION:
          name: 'RELATION'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        USETIMEZONE:
          name: 'USETIMEZONE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_condition_list_1:
      type: items
      properties:
        CONDITIONGROUPNAME:
          name: 'CONDITIONGROUPNAME'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CONDITIONNAME:
          name: 'CONDITIONNAME'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        OBJECTATTRIBUTE:
          name: 'OBJECTATTRIBUTE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        OPERATOR:
          name: 'OPERATOR'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RIGHTVALUETYPE:
          name: 'RIGHTVALUETYPE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RIGHTVALUE:
          name: 'RIGHTVALUE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_ngaction_list_1:
      type: items
      properties:
        ACTIONNAME:
          name: 'ACTIONNAME'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TYPE:
          name: 'TYPE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_ngactionattr_list_2:
      type: items
      properties:
        ACTIONNAME:
          name: 'ACTIONNAME'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ATTRNAME:
          name: 'ATTRNAME'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TYPE:
          name: 'TYPE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VALUE:
          name: 'VALUE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_rule_list_1:
      type: items
      properties:
        RULENAME:
          name: 'RULENAME'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        OPERATION:
          name: 'OPERATION'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TYPE:
          name: 'TYPE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PRECEDENCE:
          name: 'PRECEDENCE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VOLUMEUSAGEROUNDING:
          name: 'VOLUMEUSAGEROUNDING'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        EDR:
          name: 'EDR'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RELATION:
          name: 'RELATION'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_ruleconditiongroup_list_1:
      type: items
      properties:
        RULENAME:
          name: 'RULENAME'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CONDITIONGROUPNAME:
          name: 'CONDITIONGROUPNAME'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_rulengaction_list_1:
      type: items
      properties:
        RULENAME:
          name: 'RULENAME'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ACTIONNAME:
          name: 'ACTIONNAME'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_policy_list:
      type: items
      properties:
        POLICYNAME:
          name: 'POLICYNAME'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TYPE:
          name: 'TYPE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_policyrule_list:
      type: items
      properties:
        POLICYNAME:
          name: 'POLICYNAME'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RULENAME:
          name: 'RULENAME'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_policytrigger_list:
      type: items
      properties:
        POLICYNAME:
          name: 'POLICYNAME'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TRIGGERNAME:
          name: 'TRIGGERNAME'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_service_list:
      type: items
      properties:
        SERVICENAME:
          name: 'SERVICENAME'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SERVICETYPE:
          name: 'SERVICETYPE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ACTIVATEDBY:
          name: 'ACTIVATEDBY'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PRECEDENCE:
          name: 'PRECEDENCE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        QOSMODE:
          name: 'QOSMODE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SUBSCRIPTIONFORCED:
          name: 'SUBSCRIPTIONFORCED'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PROBILLDATE:
          name: 'PROBILLDATE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        QUOTAALLOCATIONMODE:
          name: 'QUOTAALLOCATIONMODE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ISSETSHAREDMODE:
          name: 'ISSETSHAREDMODE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RESUBSCRIPTIONOPERATION:
          name: 'RESUBSCRIPTIONOPERATION'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ISGROUPSERVICE:
          name: 'ISGROUPSERVICE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ISTEMPLATE:
          name: 'ISTEMPLATE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ISRECUSRLOC:
          name: 'ISRECUSRLOC'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        APNMATCHTYPE:
          name: 'APNMATCHTYPE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        HASBASESERVICE:
          name: 'HASBASESERVICE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ADDONLEVEL:
          name: 'ADDONLEVEL'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CALCVALIDFORDYNSUBGROUP:
          name: 'CALCVALIDFORDYNSUBGROUP'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CUSTOMIZEDRESET:
          name: 'CUSTOMIZEDRESET'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MASTER2MASTERSHARESERVICE:
          name: 'MASTER2MASTERSHARESERVICE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_servicepolicy_list:
      type: items
      properties:
        SERVICENAME:
          name: 'SERVICENAME'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        POLICYNAME:
          name: 'POLICYNAME'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_psub_list:
      type: items
      properties:
        USRIDENTIFIER:
          name: 'USRIDENTIFIER'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        USRSTATUS:
          name: 'USRSTATUS'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        USRBILLINGTYPE:
          name: 'USRBILLINGTYPE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        USRGRADE:
          name: 'USRGRADE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        USRBILLCYCLEDATE:
          name: 'USRBILLCYCLEDATE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ESSTATUS:
          name: 'ESSTATUS'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PACKAGETYPE:
          name: 'PACKAGETYPE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_psrv_list:
      type: items
      properties:
        USRIDENTIFIER:
          name: 'USRIDENTIFIER'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SRVNAME:
          name: 'SRVNAME'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SRVUSAGESTATE:
          name: 'SRVUSAGESTATE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SRVROAMINGTYPE:
          name: 'SRVROAMINGTYPE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SRVCONTACTMETHOD:
          name: 'SRVCONTACTMETHOD'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SRVCREATESUBSCRIBER:
          name: 'SRVCREATESUBSCRIBER'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PAYMENTFLAG:
          name: 'PAYMENTFLAG'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SRVEXATTR1:
          name: 'SRVEXATTR1'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    add_conditiongroup_list:
    - CONDITIONGROUPNAME: ConditionCG02_relay_5G
      RELATION: AND
      USETIMEZONE: No
    add_condition_list:
    - CONDITIONGROUPNAME: ConditionCG02_relay_5G
      CONDITIONNAME: ConditionCG02_relay_5G
      OBJECTATTRIBUTE: SmfSession.RatType
      OPERATOR: Equal
      RIGHTVALUETYPE: Value
      RIGHTVALUE: NR
    add_ngaction_list:
    - ACTIONNAME: AG_select_relay_upf
      TYPE: UpfSelectRule
    add_ngactionattr_list:
    - ACTIONNAME: AG_select_relay_upf
      ATTRNAME: upfSelectId
      TYPE: Value
      VALUE: select_relay_upf
    add_rule_list:
    - RULENAME: Rule_select_relay_upf01
      OPERATION: Change Rule
      TYPE: Smf Pcc Rule 5G
      PRECEDENCE: '0'
      VOLUMEUSAGEROUNDING: No
      EDR: OFF
      RELATION: AND
    add_ruleconditiongroup_list:
    - RULENAME: Rule_select_relay_upf01
      CONDITIONGROUPNAME: ConditionCG02_relay_5G
    add_rulengaction_list:
    - RULENAME: Rule_select_relay_upf01
      ACTIONNAME: AG_select_relay_upf
    add_conditiongroup_list_1:
    - CONDITIONGROUPNAME: ConditionCG01_relay_5G
      RELATION: AND
      USETIMEZONE: No
    add_condition_list_1:
    - CONDITIONGROUPNAME: ConditionCG01_relay_5G
      CONDITIONNAME: ConditionCG01_relay_5G
      OBJECTATTRIBUTE: SmfSession.upfActive
      OPERATOR: Equal
      RIGHTVALUETYPE: Value
      RIGHTVALUE: select_relay_upf
    add_ngaction_list_1:
    - ACTIONNAME: AG_relayrule
      TYPE: PredefinedPccRule
    add_ngactionattr_list_2:
    - ACTIONNAME: AG_relayrule
      ATTRNAME: pccRuleId
      TYPE: Value
      VALUE: testuserprofilename
    add_rule_list_1:
    - RULENAME: Rule_select_relay_upf02
      OPERATION: Change Rule
      TYPE: Smf Pcc Rule 5G
      PRECEDENCE: '0'
      VOLUMEUSAGEROUNDING: No
      EDR: OFF
      RELATION: AND
    add_ruleconditiongroup_list_1:
    - RULENAME: Rule_select_relay_upf02
      CONDITIONGROUPNAME: ConditionCG01_relay_5G
    add_rulengaction_list_1:
    - RULENAME: Rule_select_relay_upf02
      ACTIONNAME: AG_relayrule
    add_policy_list:
    - POLICYNAME: relay_policy
      TYPE: N7 Policy
    add_policyrule_list:
    - POLICYNAME: relay_policy
      RULENAME: Rule_select_relay_upf01
    add_policytrigger_list:
    - POLICYNAME: relay_policy
      TRIGGERNAME: IPCAN_EST
    add_service_list:
    - SERVICENAME: service_relay
      SERVICETYPE: VALUE_ADDED_SERVICE
      ACTIVATEDBY: PCEF
      PRECEDENCE: '0'
      QOSMODE: Replace
      SUBSCRIPTIONFORCED: No
      PROBILLDATE: No
      QUOTAALLOCATIONMODE: None
      ISSETSHAREDMODE: No
      RESUBSCRIPTIONOPERATION: 'NULL'
      ISGROUPSERVICE: No
      ISTEMPLATE: No
      ISRECUSRLOC: No
      APNMATCHTYPE: Full Matching
      HASBASESERVICE: No
      ADDONLEVEL: Exhaust
      CALCVALIDFORDYNSUBGROUP: No
      CUSTOMIZEDRESET: No
      MASTER2MASTERSHARESERVICE: No
    add_servicepolicy_list:
    - SERVICENAME: service_relay
      POLICYNAME: relay_policy
    add_psub_list:
    - USRIDENTIFIER: xxxxx
      USRSTATUS: Custom1
      USRBILLINGTYPE: Postpaid
      USRGRADE: 'NULL'
      USRBILLCYCLEDATE: '5'
      ESSTATUS: NotEmergency
      PACKAGETYPE: 'NULL'
    add_psrv_list:
    - USRIDENTIFIER: xxxxx
      SRVNAME: service_relay
      SRVUSAGESTATE: Normal
      SRVROAMINGTYPE: 'NULL'
      SRVCONTACTMETHOD: None
      SRVCREATESUBSCRIBER: No
      PAYMENTFLAG: Yes
      SRVEXATTR1: '255'
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 登录UPCF WebUI界面进行业务配置，在“系统管理 > 批处理 > CLI导入”界面执行以下CLI命令。

### 登录UPCF WebUI界面可参考《UPCF 产品文档》>UPCF WebUI GUI参考 > UPCF WebUI > 登录UPCF WebUI界面。

### 2 执行如下CLI脚本，创建规则“Rule\_select\_relay\_upf01”，用于当SmfSession.RatType取值为“NR”时，执行动作“UpfSelectRule”，下发UPF预定义规则。

#### 2.1 /*创建条件组ConditionCG02_relay_5G：当SmfSession.RatType取值为“NR”时，下发规则“Rule_select_relay_upf01”。*/

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_conditiongroup_list的变量区（command: ADD CONDITIONGROUP） -#}
<!-- MISSING_MACRO: command=ADD CONDITIONGROUP list_name=add_conditiongroup_list step_id=2.1 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_condition_list的变量区（command: ADD CONDITION） -#}
<!-- MISSING_MACRO: command=ADD CONDITION list_name=add_condition_list step_id=2.1 -->
```

#### 2.2 /*创建动作组AG_select_relay_upf：用于下发UPF预定义规则。取值“select_relay_upf”需要和SMF规划保持一致。*/

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_ngaction_list的变量区（command: ADD NGACTION） -#}
<!-- MISSING_MACRO: command=ADD NGACTION list_name=add_ngaction_list step_id=2.2 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_ngactionattr_list的变量区（command: ADD NGACTIONATTR） -#}
<!-- MISSING_MACRO: command=ADD NGACTIONATTR list_name=add_ngactionattr_list step_id=2.2 -->
```

#### 2.3 /*创建规则Rule_select_relay_upf01：绑定条件组ConditionCG02_relay_5G和动作组AG_select_relay_upf，用于控制SmfSession.RatType取值为“NR”时，下发UPF预定义规则。*/

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_rule_list的变量区（command: ADD RULE） -#}
<!-- MISSING_MACRO: command=ADD RULE list_name=add_rule_list step_id=2.3 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_ruleconditiongroup_list的变量区（command: ADD RULECONDITIONGROUP） -#}
<!-- MISSING_MACRO: command=ADD RULECONDITIONGROUP list_name=add_ruleconditiongroup_list step_id=2.3 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_rulengaction_list的变量区（command: ADD RULENGACTION） -#}
<!-- MISSING_MACRO: command=ADD RULENGACTION list_name=add_rulengaction_list step_id=2.3 -->
```

### 3 执行如下CLI脚本，创建规则“Rule\_select\_relay\_upf02”，用于当SmfSession.upfActive取值为“select\_relay\_upf”时，执行动作“PredefinedPccRule”，下发5G预定义规则。

#### 3.1 /*创建条件组ConditionCG01_relay_5G：当SmfSession.upfActive取值为“select_relay_upf”时，下发规则Rule_select_relay_upf02*/

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_conditiongroup_list_1的变量区（command: ADD CONDITIONGROUP） -#}
<!-- MISSING_MACRO: command=ADD CONDITIONGROUP list_name=add_conditiongroup_list_1 step_id=3.1 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_condition_list_1的变量区（command: ADD CONDITION） -#}
<!-- MISSING_MACRO: command=ADD CONDITION list_name=add_condition_list_1 step_id=3.1 -->
```

#### 3.2 /*创建动作组AG_relayrule：用于下发5G预定义规则。取值“testuserprofilename”需要和SMF规划保持一致。*/

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_ngaction_list_1的变量区（command: ADD NGACTION） -#}
<!-- MISSING_MACRO: command=ADD NGACTION list_name=add_ngaction_list_1 step_id=3.2 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_ngactionattr_list_2的变量区（command: ADD NGACTIONATTR） -#}
<!-- MISSING_MACRO: command=ADD NGACTIONATTR list_name=add_ngactionattr_list_2 step_id=3.2 -->
```

#### 3.3 /*创建规则Rule_select_relay_upf02：绑定条件组ConditionCG01_relay_5G和动作组AG_relayrule，用于控制SmfSession.upfActive取值为“select_relay_upf”时，下发5G预定义规则。*/

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_rule_list_1的变量区（command: ADD RULE） -#}
<!-- MISSING_MACRO: command=ADD RULE list_name=add_rule_list_1 step_id=3.3 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_ruleconditiongroup_list_1的变量区（command: ADD RULECONDITIONGROUP） -#}
<!-- MISSING_MACRO: command=ADD RULECONDITIONGROUP list_name=add_ruleconditiongroup_list_1 step_id=3.3 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_rulengaction_list_1的变量区（command: ADD RULENGACTION） -#}
<!-- MISSING_MACRO: command=ADD RULENGACTION list_name=add_rulengaction_list_1 step_id=3.3 -->
```

### 4 添加策略“relay\_policy”，策略类型为N7 Policy，在用户上线时下发，配置触发器“IPCAN\_EST”和“RAT\_TY\_CH”，同时关联规则“Rule\_select\_relay\_upf01”和“Rule\_select\_relay\_upf02”。

#### 4.1 /*创建策略relay_policy：绑定规则Rule_select_relay_upf01和Rule_select_relay_upf02，触发器为IPCAN_EST和RAT_TY_CH*/

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_policy_list的变量区（command: ADD POLICY） -#}
<!-- MISSING_MACRO: command=ADD POLICY list_name=add_policy_list step_id=4.1 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_policyrule_list的变量区（command: ADD POLICYRULE） -#}
<!-- MISSING_MACRO: command=ADD POLICYRULE list_name=add_policyrule_list step_id=4.1 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_policytrigger_list的变量区（command: ADD POLICYTRIGGER） -#}
<!-- MISSING_MACRO: command=ADD POLICYTRIGGER list_name=add_policytrigger_list step_id=4.1 -->
```

### 5 添加业务“service\_relay”，业务类型为VALUE\_ADDED\_SERVICE，用于关联策略“relay\_policy”。

#### 5.1 /*创建业务service_relay：绑定策略relay_policy。*/

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_service_list的变量区（command: ADD SERVICE） -#}
<!-- MISSING_MACRO: command=ADD SERVICE list_name=add_service_list step_id=5.1 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_servicepolicy_list的变量区（command: ADD SERVICEPOLICY） -#}
<!-- MISSING_MACRO: command=ADD SERVICEPOLICY list_name=add_servicepolicy_list step_id=5.1 -->
```

### 6 发放业务。

#### 6.1 执行**ADD PSUB**增加一个用户。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_psub_list的变量区（command: ADD PSUB） -#}
<!-- MISSING_MACRO: command=ADD PSUB list_name=add_psub_list step_id=6.1 -->
```

#### 6.2 执行**ADD PSRV**给用户签约业务。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_psrv_list的变量区（command: ADD PSRV） -#}
<!-- MISSING_MACRO: command=ADD PSRV list_name=add_psrv_list step_id=6.2 -->
```


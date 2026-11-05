---
id: ''
name: 配置PCF基础数据
ne_type: UEG
type: feature
description: 本场景用于在PCF上配置用户的签约数据。
tags: []
risk_level: ''
doc_source:
  - ["专网（仅连接，园区入驻式）","业务发放","5GC toB 业务发放概述（专网，入驻式）","参考","用户数据发放","数据配置","配置PCF基础数据"]
  - ["专线（仅连接，地市共享式）","业务发放","5GC toB 业务发放概述（专线，共享式）","参考","用户数据发放","数据配置","配置PCF基础数据"]
  - ["云网（连接+计算，入驻式或共享式）","业务发放","5GC toB 业务发放概述（云网，带计算）","参考","用户数据发放","数据配置","配置PCF基础数据"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
本场景用于在PCF上配置用户的签约数据。

## 必备事项
前提条件

无。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    add_psub_list:
      type: items
      properties:
        USRIDENTIFIER:
          name: '用户标识'
          type: string
          required: false
          description: '配置终端开户数据。'
          data_source: '全局规划'
          pattern: ''
          default: ''
        USRMSISDN:
          name: '移动用户MSISDN号'
          type: string
          required: false
          description: ''
          data_source: '全局规划'
          pattern: ''
          default: ''
        USRSTATE:
          name: '用户状态'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        USRPAIDTYPE:
          name: '付费类型'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        USRSTATION:
          name: '用户身份'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        USRCONTACTMETHOD:
          name: '联系方式'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        USRBILLCYCLEDATE:
          name: '结帐日'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        USRSUBNETTYPE:
          name: '所属网络类型'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        USRLANGUAGE:
          name: '语言'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        USRSMSRECEIVEFLAG:
          name: '短信接收选项'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        USRVERSTATUS:
          name: '用户版本状态'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_psrv_list:
      type: items
      properties:
        USRIDENTIFIER:
          name: '用户标识'
          type: string
          required: false
          description: '配置终端签约数据。参数“USRIDENTIFIER”在**ADD PSUB**的参数“USRIDENTIFIER”中定义，此处引用。'
          data_source: '已有配置中获取'
          pattern: ''
          default: ''
        SRVNAME:
          name: '业务'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_ngaction_list:
      type: items
      properties:
        ACTIONNAME:
          name: '5G动作名称'
          type: string
          required: false
          description: '配置动作。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        TYPE:
          name: '动作类型'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        DESCRIPTION:
          name: '描述'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_ngactionattr_list:
      type: items
      properties:
        ACTIONNAME:
          name: '5G动作名称'
          type: string
          required: false
          description: '配置动作属性。参数“5G动作名称”由命令**ADD NGACTION**定义，在此处引用。'
          data_source: '已有配置中获取'
          pattern: ''
          default: ''
        ATTRNAME:
          name: '属性名称'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        TYPE:
          name: '参数值类型'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        VALUE:
          name: '参数值'
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
          required: false
          description: '配置规则。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        TYPE:
          name: '类型'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        RELATION:
          name: '运算符'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_rulengaction_list:
      type: items
      properties:
        RULENAME:
          name: '规则名称'
          type: string
          required: false
          description: '配置规则条件组。参数“规则名称”由命令**ADD RULE**定义，在此处引用。'
          data_source: '已有配置中获取'
          pattern: ''
          default: ''
        ACTIONNAME:
          name: '5G动作组名称'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_policy_list:
      type: items
      properties:
        POLICYNAME:
          name: '策略名称'
          type: string
          required: false
          description: '配置策略。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        TYPE:
          name: '策略类型'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_policyrule_list:
      type: items
      properties:
        POLICYNAME:
          name: '策略名称'
          type: string
          required: false
          description: '配置策略规则。   * 参数“策略名称”由命令**ADD POLICY**定义，在此处引用。 * 参数“规则名称”由命令**ADD RULE**定义，在此处引用。'
          data_source: '已有配置中获取'
          pattern: ''
          default: ''
        RULENAME:
          name: '规则名称'
          type: string
          required: false
          description: ''
          data_source: '已有配置中获取'
          pattern: ''
          default: ''
    add_policytrigger_list:
      type: items
      properties:
        POLICYNAME:
          name: '策略名称'
          type: string
          required: false
          description: '配置策略触发器。参数“策略名称”由命令**ADD POLICY**定义，在此处引用。'
          data_source: '已有配置中获取'
          pattern: ''
          default: ''
        TRIGGERNAME:
          name: '触发器名称'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_service_list:
      type: items
      properties:
        SERVICENAME:
          name: '业务名称'
          type: string
          required: false
          description: '配置业务。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SERVICETYPE:
          name: '业务类型'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        ACTIVATEDBY:
          name: '激活方式'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        PRECEDENCE:
          name: '优先级'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        QOSMODE:
          name: 'QoS模式'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        SUBSCRIPTIONFORCED:
          name: '签约后才能使用'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        PROBILLDATE:
          name: '结账日失效'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        QUOTAALLOCATIONMODE:
          name: '配额分配方式'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        ISSETSHAREDMODE:
          name: '是否设置共享方式'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        RESUBSCRIPTIONOPERATION:
          name: '重复订购方式'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        ISGROUPSERVICE:
          name: '是否组业务'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        ISTEMPLATE:
          name: '是否模板'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        ISRECUSRLOC:
          name: '是否支持用户在线时记录位置信息'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        APNMATCHTYPE:
          name: 'APN匹配类型'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        HASBASESERVICE:
          name: '是否有基础业务'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        ADDONLEVEL:
          name: '自动订购触发阈值'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        CALCVALIDFORDYNSUBGROUP:
          name: '是否计算动态实例有效期'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_servicepolicy_list:
      type: items
      properties:
        SERVICENAME:
          name: '业务名称'
          type: string
          required: false
          description: '配置业务关联的策略。   * 参数“业务名称”由命令**ADD SERVICE**定义，在此处引用。 * 参数“策略名称”由命令**ADD POLICY**定义，在此处引用。'
          data_source: '已有配置中获取'
          pattern: ''
          default: ''
        POLICYNAME:
          name: '策略名称'
          type: string
          required: false
          description: ''
          data_source: '已有配置中获取'
          pattern: ''
          default: ''
  examples:
    add_psub_list:
    - USRIDENTIFIER: '460020000000001'
      USRMSISDN: 8614xxxxx631335
      USRSTATE: Normal
      USRPAIDTYPE: 'NULL'
      USRSTATION: Master
      USRCONTACTMETHOD: SMS
      USRBILLCYCLEDATE: 'NULL'
      USRSUBNETTYPE: MBB
      USRLANGUAGE: 'NULL'
      USRSMSRECEIVEFLAG: All
      USRVERSTATUS: Normal
    add_psrv_list:
    - USRIDENTIFIER: '460020000000001'
      SRVNAME: 9cu00_03_ffffff_testqci4
    add_ngaction_list:
    - ACTIONNAME: AG_ConneCapab
      TYPE: ConnectionCapabilities
      DESCRIPTION: ConnectionCapabilities01
    add_ngactionattr_list:
    - ACTIONNAME: AG_ConneCapab
      ATTRNAME: ims
      TYPE: Value
      VALUE: True
    add_rule_list:
    - RULENAME: Rule_UEPolicy
      TYPE: Amf Pcc Rule 5G
      RELATION: AND
    add_rulengaction_list:
    - RULENAME: Rule_UEPolicy
      ACTIONNAME: AG_UePolicyAction
    add_policy_list:
    - POLICYNAME: Policy_UE
      TYPE: N15 Policy
    add_policyrule_list:
    - POLICYNAME: Policy_UE
      RULENAME: Rule_UEPolicy
    add_policytrigger_list:
    - POLICYNAME: Policy_UE
      TRIGGERNAME: N15UserLocationChange
    add_service_list:
    - SERVICENAME: Service_UE
      SERVICETYPE: VALUE_ADDED_SERVICE
      ACTIVATEDBY: PCEF
      PRECEDENCE: '0'
      QOSMODE: Replace
      SUBSCRIPTIONFORCED: Yes
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
    add_servicepolicy_list:
    - SERVICENAME: Service_UE
      POLICYNAME: Policy_UE
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 配置终端开户数据。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_psub_list的变量区（command: ADD PSUB） -#}
<!-- MISSING_MACRO: command=ADD PSUB list_name=add_psub_list step_id=1 -->
```

### 2 配置终端签约数据。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_psrv_list的变量区（command: ADD PSRV） -#}
<!-- MISSING_MACRO: command=ADD PSRV list_name=add_psrv_list step_id=2 -->
```

### 3 配置URSP策略数据。

#### 3.1 /*添加动作*/

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_ngaction_list的变量区（command: ADD NGACTION） -#}
<!-- MISSING_MACRO: command=ADD NGACTION list_name=add_ngaction_list step_id=3.1 -->
```

#### 3.2 /*添加动作属性*/

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_ngactionattr_list的变量区（command: ADD NGACTIONATTR） -#}
<!-- MISSING_MACRO: command=ADD NGACTIONATTR list_name=add_ngactionattr_list step_id=3.2 -->
```

#### 3.3 /*添加规则*/

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_rule_list的变量区（command: ADD RULE） -#}
<!-- MISSING_MACRO: command=ADD RULE list_name=add_rule_list step_id=3.3 -->
```

#### 3.4 /*添加规则动作*/

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_rulengaction_list的变量区（command: ADD RULENGACTION） -#}
<!-- MISSING_MACRO: command=ADD RULENGACTION list_name=add_rulengaction_list step_id=3.4 -->
```

#### 3.5 /*添加策略*/

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_policy_list的变量区（command: ADD POLICY） -#}
<!-- MISSING_MACRO: command=ADD POLICY list_name=add_policy_list step_id=3.5 -->
```

#### 3.6 /*添加策略规则*/

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_policyrule_list的变量区（command: ADD POLICYRULE） -#}
<!-- MISSING_MACRO: command=ADD POLICYRULE list_name=add_policyrule_list step_id=3.6 -->
```

#### 3.7 /*添加策略触发器*/

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_policytrigger_list的变量区（command: ADD POLICYTRIGGER） -#}
<!-- MISSING_MACRO: command=ADD POLICYTRIGGER list_name=add_policytrigger_list step_id=3.7 -->
```

#### 3.8 /*添加业务*/

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_service_list的变量区（command: ADD SERVICE） -#}
<!-- MISSING_MACRO: command=ADD SERVICE list_name=add_service_list step_id=3.8 -->
```

#### 3.9 /*添加业务策略

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_servicepolicy_list的变量区（command: ADD SERVICEPOLICY） -#}
<!-- MISSING_MACRO: command=ADD SERVICEPOLICY list_name=add_servicepolicy_list step_id=3.9 -->
```


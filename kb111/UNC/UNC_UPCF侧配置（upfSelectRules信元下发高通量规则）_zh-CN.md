---
id: ''
name: UPCF侧配置（upfSelectRules信元下发高通量规则）
ne_type: UNC
type: feature
description: 本操作指导您完成高通量UPF选择解决方案中UPCF侧的初始业务配置。
risk_level: ''
doc_source: ["网络部署","业务专题","5G Core 高通量UPF选择方案","UPCF侧配置（upfSelectRules信元下发高通量规则）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本操作指导您完成高通量UPF选择解决方案中UPCF侧的初始业务配置。

## 必备事项
前提条件

* 已完成配置UPCF与SMF的对接数据。
* 已阅读高通量UPF特性概述。
* 高通量业务的规则名已全网统一规划。
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
        RIGHTOBJECTATTRIBUTE:
          name: 'RIGHTOBJECTATTRIBUTE'
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
        USRMSISDN:
          name: 'USRMSISDN'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        USRSTATE:
          name: 'USRSTATE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        USRPAIDTYPE:
          name: 'USRPAIDTYPE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        USRSTATION:
          name: 'USRSTATION'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        USRCONTACTMETHOD:
          name: 'USRCONTACTMETHOD'
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
        USRSUBNETTYPE:
          name: 'USRSUBNETTYPE'
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
  examples:
    add_conditiongroup_list:
    - CONDITIONGROUPNAME: SubscriberStatus_CG01
      RELATION: AND
      USETIMEZONE: No
    add_condition_list:
    - CONDITIONGROUPNAME: SubscriberStatus_CG01
      CONDITIONNAME: SubscriberStatus_C01
      OBJECTATTRIBUTE: Subscriber.SubscriberIdentifier
      OPERATOR: Not Equal
      RIGHTVALUETYPE: Attribute
      RIGHTOBJECTATTRIBUTE: System.Null
    add_ngactionattr_list:
    - ACTIONNAME: UpfSelect_AG01
      ATTRNAME: upfSelectId
      TYPE: Value
      VALUE: select_high_upf
    add_rule_list:
    - RULENAME: N7_High_Rule01
      OPERATION: Change Rule
      TYPE: Smf Pcc Rule 5G
      PRECEDENCE: '0'
      VOLUMEUSAGEROUNDING: No
      EDR: OFF
      RELATION: AND
    add_ruleconditiongroup_list:
    - RULENAME: N7_High_Rule01
      CONDITIONGROUPNAME: SubscriberStatus_CG01
    add_rulengaction_list:
    - RULENAME: N7_High_Rule01
      ACTIONNAME: UpfSelect_AG01
    add_policy_list:
    - POLICYNAME: N7_High_Policy01
      TYPE: N7 Policy
    add_policyrule_list:
    - POLICYNAME: N7_High_Policy01
      RULENAME: N7_High_Rule01
    add_policytrigger_list:
    - POLICYNAME: N7_High_Policy01
      TRIGGERNAME: IPCAN_EST
    add_service_list:
    - SERVICENAME: N7_High_Service01
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
      CUSTOMIZEDRESET: No
      MASTER2MASTERSHARESERVICE: No
    add_servicepolicy_list:
    - SERVICENAME: N7_High_Service01
      POLICYNAME: N7_High_Policy01
    add_psub_list:
    - USRIDENTIFIER: 46010381012****
      USRMSISDN: 1234567****
      USRSTATE: Normal
      USRPAIDTYPE: 'NULL'
      USRSTATION: Master
      USRCONTACTMETHOD: SMS
      USRBILLCYCLEDATE: 'NULL'
      USRSUBNETTYPE: eMBB-SA
    add_psrv_list:
    - USRIDENTIFIER: 46010381012****
      SRVNAME: N7_High_Service01
      SRVUSAGESTATE: Normal
      SRVROAMINGTYPE: 'NULL'
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 登录UPCF WebUI界面。

### 2 配置条件组。

### 导航入口为“策略管理 > 策略 > 条件组”。

### 当业务的使用需要设置控制条件时，需要配置条件组。若某规则不配置条件组，表示在同一业务里其他条件都匹配不上时，才触发此规则。

### 条件组是一个或多个条件的组合。条件组中的各条件之间可以是“与”的关系，也可以是“或”的关系。条件之间的与/或关系由参数“关系”的取值决定。

### 需要配置条件组，条件组的数据规划如表2所示。

### **表2** 条件组

### | 类别 | 参数 |  | 取值样例 |

### | --- | --- | --- | --- |

### | 条件组 | 基本信息 | 名称 | SubscriberStatus\_CG01 |

### |  |  | 关系 | AND |

### |  | 条件 | 名称 | SubscriberStatus\_C01 |

### |  |  | 对象属性 | * 对象：Subscriber * 属性：SubscriberIdentifier |

### |  |  | 操作符 | Not Equal |

### |  |  | 右值类型 | Attribute |

### |  |  | 右值 | System.Null |

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_conditiongroup_list的变量区（command: ADD CONDITIONGROUP） -#}
<!-- MISSING_MACRO: command=ADD CONDITIONGROUP list_name=add_conditiongroup_list step_id=2 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_condition_list的变量区（command: ADD CONDITION） -#}
<!-- MISSING_MACRO: command=ADD CONDITION list_name=add_condition_list step_id=2 -->
```

### 3 配置5G动作组。

### 导航入口为“策略管理 > 策略 > 5G动作组”。

### 预定义动作的名称需要提前与对端SMF规划一致，具体规则的实现细节由对端SMF配置决定。

### 需要配置如下动作和动作组，动作组的数据规划如表3所示。

### **表3** 5G动作组

### | 类别 | 参数 |  | 取值样例 |

### | --- | --- | --- | --- |

### | 5G动作组 | 基本信息 | 名称 | UpfSelect\_AG01 |

### |  |  | 类型 | UpfSelectRule |

### |  | 属性 | upfSelectId | * 类型：Value * 值：select\_high\_upf |

### |  |  | reportInd | * 类型：Value * 值：True |

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_ngactionattr_list的变量区（command: ADD NGACTIONATTR） -#}
<!-- MISSING_MACRO: command=ADD NGACTIONATTR list_name=add_ngactionattr_list step_id=3 -->
```

### 4 配置规则。

### 导航入口为“策略管理 > 策略 > 规则”。

### 规则的数据规划如表4所示。

### **表4** 规则

### | 类别 | 参数 |  | 取值样例 |

### | --- | --- | --- | --- |

### | 规则 | 基本信息 | 名称 | N7\_High\_Rule01 |

### |  |  | 操作类型 | Change Rule |

### |  |  | 类型 | 5G Smf Pcc Rule |

### |  | 条件组 | 关系 | AND  说明：  当规则中只有一个条件组时，“关系”可设置为任意值。 |

### |  |  | 条件组 | SubscriberStatus\_CG01  说明：  已在条件组中定义。 |

### |  | 5G动作组 | 5G动作组 | UpfSelect\_AG01  说明：  已在5G动作组中定义。 |

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_rule_list的变量区（command: ADD RULE） -#}
<!-- MISSING_MACRO: command=ADD RULE list_name=add_rule_list step_id=4 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_ruleconditiongroup_list的变量区（command: ADD RULECONDITIONGROUP） -#}
<!-- MISSING_MACRO: command=ADD RULECONDITIONGROUP list_name=add_ruleconditiongroup_list step_id=4 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_rulengaction_list的变量区（command: ADD RULENGACTION） -#}
<!-- MISSING_MACRO: command=ADD RULENGACTION list_name=add_rulengaction_list step_id=4 -->
```

### 5 配置策略。

### 导航入口为“策略管理 > 策略 > 策略”。

### 策略的数据规划如表5所示。

### **表5** 策略

### | 类别 | 参数 |  | 取值样例 |

### | --- | --- | --- | --- |

### | 策略 | 基本信息 | 名称 | N7\_High\_Policy01 |

### |  |  | 类型 | N7 Policy |

### |  | 触发器 | 名称 | IPCAN\_EST |

### |  | 规则 | 名称 | N7\_High\_Rule01  说明：  已在规则中定义。 |

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_policy_list的变量区（command: ADD POLICY） -#}
<!-- MISSING_MACRO: command=ADD POLICY list_name=add_policy_list step_id=5 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_policyrule_list的变量区（command: ADD POLICYRULE） -#}
<!-- MISSING_MACRO: command=ADD POLICYRULE list_name=add_policyrule_list step_id=5 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_policytrigger_list的变量区（command: ADD POLICYTRIGGER） -#}
<!-- MISSING_MACRO: command=ADD POLICYTRIGGER list_name=add_policytrigger_list step_id=5 -->
```

### 6 配置业务。

### 导航入口为“业务管理 > 业务 > 业务”。

### 业务的数据规划如表6所示。

### **表6** 业务

### | 类别 | 参数 |  | 取值样例 |

### | --- | --- | --- | --- |

### | 业务 | 基本信息 | 名称 | N7\_High\_Service01 |

### |  |  | 类型 | VALUE\_ADDED\_SERVICE |

### |  |  | 激活方式 | PCEF |

### |  |  | 优先级 | 0  说明：  运营商统一规划，用于设置该业务在互斥组中的优先级。当此业务不需配置相关互斥组时，此值取默认值“0”。 |

### |  |  | QoS模式 | 替换 |

### |  |  | 签约后才能使用 | 是 |

### |  | 策略 | 名称 | N7\_High\_Policy01  说明：  已在策略中定义。 |

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_service_list的变量区（command: ADD SERVICE） -#}
<!-- MISSING_MACRO: command=ADD SERVICE list_name=add_service_list step_id=6 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_servicepolicy_list的变量区（command: ADD SERVICEPOLICY） -#}
<!-- MISSING_MACRO: command=ADD SERVICEPOLICY list_name=add_servicepolicy_list step_id=6 -->
```

### 7 登录“UPCF 业务管理”窗口。

### 8 发放业务。

#### 8.1 执行**ADD PSUB**增加一个用户。

#### “USRIDENTIFIER”的参数类型受软参VRM\_SUBSRCIPTIONIDTYPE（系统支持的用户类型）控制，默认为“IMSI”。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_psub_list的变量区（command: ADD PSUB） -#}
<!-- MISSING_MACRO: command=ADD PSUB list_name=add_psub_list step_id=8.1 -->
```

#### 8.2 执行**ADD PSRV**给用户签约业务。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_psrv_list的变量区（command: ADD PSRV） -#}
<!-- MISSING_MACRO: command=ADD PSRV list_name=add_psrv_list step_id=8.2 -->
```


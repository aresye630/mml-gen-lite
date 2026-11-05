---
id: ''
name: 部署基于漫游地动态签约的分流策略控制（PCF）
ne_type: UNC
type: feature
description: 当5G用户在漫游地签约本地专网业务，当用户进入专网区域后能自动激活专网业务提供的网络服务，以对接华为UNC为例，专网业务内容定义如下：  * 用户在漫游地进入特定专网区域（如NR Tai Tac=123）后可享受专网业务。 * 当用户进入专网区域后，PCF会动态下发专网DNN=dnn-ar给SMF。 * SMF基于新的DNN激活dnn-ar绑定的ULCL分流规则，用户使用园区专网提供的网络服务。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","MEC解决方案","WSFD-223003 基于漫游地动态签约的分流策略控制","特性部署","部署基于漫游地动态签约的分流策略控制（PCF）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
当5G用户在漫游地签约本地专网业务，当用户进入专网区域后能自动激活专网业务提供的网络服务，以对接华为UNC为例，专网业务内容定义如下：* 用户在漫游地进入特定专网区域（如NR Tai Tac=123）后可享受专网业务。* 当用户进入专网区域后，PCF会动态下发专网DNN=dnn-ar给SMF。* SMF基于新的DNN激活dnn-ar绑定的ULCL分流规则，用户使用园区专网提供的网络服务。

## 必备事项
前提条件

* 操作员已了解“特性概述”及“实现原理”。
* 操作已完成“配置UPCF与NRF的对接数据”。
* 已完成本特性License加载，可以通过**DSP LICENSE**命令查询确认，如果本特性的License在查询列表中可见，即可认为本特性License已加载成功。

用户进入专网区域后，PCF通过用户上线位置区域判断下发专网DNN策略逻辑如图1所示。

**图1** **PCF下发专网DNN的业务配置逻辑**  

图中“必须配置的动作类型”也仅是针对当前场景而言，其他不同场景须参考对应的配置逻辑。
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
        TYPE:
          name: 'TYPE'
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
    - CONDITIONGROUPNAME: CG_Special
      RELATION: AND
    add_condition_list:
    - CONDITIONGROUPNAME: CG_Special
      CONDITIONNAME: 90895_0101_C01
      OBJECTATTRIBUTE: AmPolicySession.NrTaiTac
      OPERATOR: Equal
      RIGHTVALUETYPE: Value
      RIGHTVALUE: '123'
    add_ngaction_list:
    - ACTIONNAME: AG_SpecialDnn
      TYPE: AmPolicyAction
    add_ngactionattr_list:
    - ACTIONNAME: AG_SpecialDnn
      ATTRNAME: LBOService
      TYPE: Value
      VALUE: dnn-ar
    add_rule_list:
    - RULENAME: Rule_Dnn
      TYPE: Amf Pcc Rule 5G
      RELATION: AND
    add_ruleconditiongroup_list:
    - RULENAME: Rule_Dnn
      CONDITIONGROUPNAME: CG_Special
    add_rulengaction_list:
    - RULENAME: Rule_Dnn
      ACTIONNAME: AG_SpecialDnn
    add_policy_list:
    - POLICYNAME: Policy_Dnn
      TYPE: N15 Policy
    add_policyrule_list:
    - POLICYNAME: Policy_Dnn
      RULENAME: Rule_Dnn
    add_policytrigger_list:
    - POLICYNAME: Policy_Dnn
      TRIGGERNAME: N15UserLocationChange
    add_service_list:
    - SERVICENAME: S_SelectedDnn
      SERVICETYPE: VRM_BD_SERVICE_LOCAL
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
      HASBASESERVICE: No
      ADDONLEVEL: Exhaust
      CALCVALIDFORDYNSUBGROUP: No
    add_servicepolicy_list:
    - SERVICENAME: S_SelectedDnn
      POLICYNAME: Policy_Dnn
    add_psub_list:
    - USRIDENTIFIER: 46010381012****
      USRMSISDN: 1234567****
      USRSTATE: Normal
      USRPAIDTYPE: 'NULL'
      USRSTATION: Master
      USRCONTACTMETHOD: SMS
      USRBILLCYCLEDATE: 'NULL'
      USRSUBNETTYPE: LocalService
    add_psrv_list:
    - USRIDENTIFIER: 46010381012****
      SRVNAME: S_SelectedDnn
      SRVUSAGESTATE: Normal
      SRVROAMINGTYPE: 'NULL'
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 登录UPCF Web UI界面。

### 2 配置条件组。

### 导航入口为“策略管理 > 策略 > 条件组”。

#### 2.1 当业务的使用需要设置控制条件时，需要配置条件组。若某规则不配置条件组，表示在同一业务里其他条件都匹配不上时，才触发此规则。

#### 2.2 条件组是一个或多个条件的组合。条件组中的各条件之间可以是“与”的关系，也可以是“或”的关系。条件之间的与/或关系由参数“关系”的取值决定。

### 需要配置1个条件组，即用户上线所在位置区域为专网区域场景，当用户位于非专网区域时，当前策略无需定义相关处理内容，用户可直接使用普通业务。条件组的数据规划如表2所示。

### **表2** 条件组

### | 类别 | 参数 |  | 取值样例 |

### | --- | --- | --- | --- |

### | 条件组1 | 基本信息 | 名称 | CG\_Special |

### |  |  | 关系 | AND |

### |  | 条件 | 名称 | CG\_Special |

### |  |  | 对象属性 | * 对象：AmPolicySession * 属性：NrTaiTac |

### |  |  | 操作符 | Equal |

### |  |  | 右值类型 | Value |

### |  |  | 右值 | 123  说明：  “123”：表示用户在漫游地进入专网区域后接入5G网络对应的小区TAC标识 |

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

### 5G动作组的数据规划如表3所示。

### **表3** 5G动作组

### | 类别 | 参数 |  | 取值样例 |

### | --- | --- | --- | --- |

### | 5G动作组1 | 基本信息 | 名称 | AG\_SpecialDnn |

### |  |  | 类型 | AmPolicyAction |

### |  | 属性 | LBOService | * 类型：Value * 值：dnn-ar 说明：  + 该参数取值须与对端网元协商。   + 该参数配置当前仅支持由“-”、“.”、“0～9”、“a～f”以及“A～F”组成的长度为1～63字节的字符串，且不能以“.”开头、不能出现连续两个“.”。 |

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_ngaction_list的变量区（command: ADD NGACTION） -#}
<!-- MISSING_MACRO: command=ADD NGACTION list_name=add_ngaction_list step_id=3 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_ngactionattr_list的变量区（command: ADD NGACTIONATTR） -#}
<!-- MISSING_MACRO: command=ADD NGACTIONATTR list_name=add_ngactionattr_list step_id=3 -->
```

### 4 配置规则

### 导航入口为“策略管理 > 策略 > 规则”。

### 此场景，规则的“类型”需要配置为“5G Amf Pcc Rule”。

### 规则的数据规划如表4所示。

### **表4** 规则

### | 类别 | 参数 |  | 取值样例 |

### | --- | --- | --- | --- |

### | 规则1 | 基本信息 | 名称 | Rule\_Dnn |

### |  |  | 操作类型 | Change Rule |

### |  |  | 类型 | 5G Amf Pcc Rule |

### |  | 条件组 | 关系 | AND  说明：  当规则中只有一个条件组时，“关系”可设置为任意值。 |

### |  |  | 条件组 | CG\_Special  说明：  已在表2中定义。 |

### |  | 5G动作组 | 5G动作组 | AG\_SpecialDnn  说明：  已在表3中定义。 |

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

### | 策略1 | 基本信息 | 名称 | Policy\_Dnn |

### |  |  | 策略类型 | N15 Policy |

### |  | 触发器 | 名称 | * N15UserLocationChange * N15PolicyCreateRequest |

### |  | 规则 | 名称 | Rule\_Dnn  说明：  已在表4中定义。 |

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

### | 业务1 | 基本信息 | 名称 | S\_SelectedDnn |

### |  |  | 类型 | VRM\_BD\_SERVICE\_LOCAL |

### |  |  | 是否记入基本配额 | 是 |

### |  |  | 激活方式 | PCEF |

### |  |  | 优先级 | 0  说明：  运营商统一规划，用于设置该业务在互斥组中的优先级。当此业务不需配置相关互斥组时，此值可任意取值。 |

### |  |  | QoS模式 | 替换 |

### |  |  | 签约后才能使用 | 是 |

### |  | 策略 | 名称 | Policy\_Dnn  说明：  已在表5中定义。 |

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


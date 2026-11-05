---
id: ''
name: 配置专用DNN策略数据
ne_type: UDG
type: feature
description: 对于专用DNN（stjwt.gd）接入场景，需要将已配置的增值类业务改造为专网业务，并在PCF配置园区RG预定义规则、DNS重定向预定义规则，预定义规则名称需要与对端SMF网元协商一致。
risk_level: ''
doc_source: ["特性部署","业务专题","5G Core 一跳入家解决方案","一跳入家解决方案（基于3GPP接入方案）","业务初始部署与调测","部署移动VPN","配置专用DNN数据","配置PCF","配置专用DNN数据","配置专用DNN策略数据"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
对于专用DNN（stjwt.gd）接入场景，需要将已配置的增值类业务改造为专网业务，并在PCF配置园区RG预定义规则、DNS重定向预定义规则，预定义规则名称需要与对端SMF网元协商一致。

## 必备事项
前提条件

* 已完成通用DNN数据配置，专网用户已签约业务MulDNN\_Service01。
* 确认园区RG预定义规则、DNS重定向预定义规则标识，与对端SMF协商一致。
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
          name: '对象属性'
          type: string
          required: false
          description: 'UPCF WebUI配置项。'
          data_source: '-'
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
          name: '右值'
          type: string
          required: false
          description: '用于设置归属地园区专用DNN信息。当用户从此DNN接入时，触发PCF下发园区RG预定义规则及DNS重定向预定义规则。  取值范围：长度为1～64的字符串。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    mod_service_list:
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
        ISSETSHAREDMODE:
          name: 'ISSETSHAREDMODE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SHAREDMODE:
          name: 'SHAREDMODE'
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
        DEDICATEDSRVCONGRP:
          name: 'DEDICATEDSRVCONGRP'
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
          name: '名称（预定义规则标识01）'
          type: string
          required: false
          description: 'UPCF WebUI配置项。'
          data_source: '-'
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
          name: '值'
          type: string
          required: false
          description: '用于控制园区的费率，实际费率按照园区客户规划决定。  取值范围：长度为1～128的字符串，且不能输入的特殊字符为<>[]%&"+=,;/''  说明：  * 当园区计费采用缺省费率时，PCF基于园区DNN信息，下发u\_p\_multi\_default。该预定义规则在SMF和UPF均需要配置。 * 当园区计费采用特定费率时，PCF基于园区DNN信息，下发u\_p\_<01>\_multi。其中<01>是变量，基于费率的不同而变化，该预定义规则在SMF和UPF均需要同步配置。'
          data_source: '全网规划'
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
    add_ngactionattr_list_1:
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
          name: '名称（预定义规则标识02）'
          type: string
          required: false
          description: 'UPCF WebUI配置项。'
          data_source: '-'
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
          name: '值'
          type: string
          required: false
          description: '用于控制DNS重定向。  取值范围：长度为1～128的字符串，且不能输入的特殊字符为<>[]%&"+=,;/''  说明：  当园区有DNS重定向动作时，PCF基于园区DNN信息，下发u\_p\_<enterprise>\_dns。其中<enterprise>建议为企业业务缩写，该预定义规则在SMF和UPF均需要同步配置。'
          data_source: '全网规划'
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
  examples:
    add_conditiongroup_list:
    - CONDITIONGROUPNAME: Intranet_CG01
      RELATION: OR
      USETIMEZONE: No
    add_condition_list:
    - CONDITIONGROUPNAME: Intranet_CG01
      CONDITIONNAME: Intranet_C01
      OBJECTATTRIBUTE: SmfSession.Dnn
      OPERATOR: Equal
      RIGHTVALUETYPE: Value
      RIGHTVALUE: stjwt.gd
    mod_service_list:
    - SERVICENAME: MulDNN_Service01
      ISSETSHAREDMODE: Yes
      SHAREDMODE: NotShared
      SERVICETYPE: INTRANET_SERVICE
      DEDICATEDSRVCONGRP: Intranet_CG01
    add_ngaction_list:
    - ACTIONNAME: PrePCC_5GAG01
      TYPE: PredefinedPccRule
    add_ngactionattr_list:
    - ACTIONNAME: PrePCC_5GAG01
      ATTRNAME: pccRuleId
      TYPE: Value
      VALUE: u_p_multi_default
    add_rule_list:
    - RULENAME: PrePCC_Rule01
      TYPE: Smf Pcc Rule 5G
      PRECEDENCE: '0'
      VOLUMEUSAGEROUNDING: No
      EDR: OFF
      RELATION: AND
    add_ruleconditiongroup_list:
    - RULENAME: PrePCC_Rule01
      CONDITIONGROUPNAME: Intranet_CG01
    add_rulengaction_list:
    - RULENAME: PrePCC_Rule01
      ACTIONNAME: PrePCC_5GAG01
    add_ngaction_list_1:
    - ACTIONNAME: PrePCC_5GAG02
      TYPE: PredefinedPccRule
    add_ngactionattr_list_1:
    - ACTIONNAME: PrePCC_5GAG02
      ATTRNAME: pccRuleId
      TYPE: Value
      VALUE: u_p_enterprise_dns
    add_rule_list_1:
    - RULENAME: PrePCC_Rule02
      TYPE: Smf Pcc Rule 5G
      PRECEDENCE: '0'
      VOLUMEUSAGEROUNDING: No
      EDR: OFF
      RELATION: AND
    add_ruleconditiongroup_list_1:
    - RULENAME: PrePCC_Rule02
      CONDITIONGROUPNAME: Intranet_CG01
    add_rulengaction_list_1:
    - RULENAME: PrePCC_Rule02
      ACTIONNAME: PrePCC_5GAG02
    add_policyrule_list:
    - POLICYNAME: MulDNN_Policy01
      RULENAME: PrePCC_Rule01
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 登录UPCF WebUI界面进行业务配置，在“系统管理 > 批处理 > CLI导入”界面执行以下CLI命令。

### 添加专网会话隔离条件组（Intranet\_CG01），用户携带专用DNN（stjwt.gd）上线。此处操作符OPERATOR支持选择Equal、Not Equal、Like、Matchpostfix等。对于满足此条件的会话，PCF仅下发专网业务，不下发大网业务。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_conditiongroup_list的变量区（command: ADD CONDITIONGROUP） -#}
<!-- MISSING_MACRO: command=ADD CONDITIONGROUP list_name=add_conditiongroup_list step_id=1 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_condition_list的变量区（command: ADD CONDITION） -#}
<!-- MISSING_MACRO: command=ADD CONDITION list_name=add_condition_list step_id=1 -->
```

### 2 将配置通用DNN策略数据已配置的业务MulDNN\_Service01改造为专网业务，改造后的业务类型为INTRANET\_SERVICE，同时关联1中配置的专网会话隔离条件组。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该mod_service_list的变量区（command: MOD SERVICE） -#}
<!-- MISSING_MACRO: command=MOD SERVICE list_name=mod_service_list step_id=2 -->
```

### 3 添加5G动作组（PrePCC\_5GAG01）及动作组子参数。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_ngaction_list的变量区（command: ADD NGACTION） -#}
<!-- MISSING_MACRO: command=ADD NGACTION list_name=add_ngaction_list step_id=3 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_ngactionattr_list的变量区（command: ADD NGACTIONATTR） -#}
<!-- MISSING_MACRO: command=ADD NGACTIONATTR list_name=add_ngactionattr_list step_id=3 -->
```

### 4 添加园区RG预定义规则（PrePCC\_Rule01），用于关联1配置的条件组和3配置的动作组。

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

### 5 添加5G动作组（PrePCC\_5GAG02）及动作组子参数。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_ngaction_list_1的变量区（command: ADD NGACTION） -#}
<!-- MISSING_MACRO: command=ADD NGACTION list_name=add_ngaction_list_1 step_id=5 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_ngactionattr_list_1的变量区（command: ADD NGACTIONATTR） -#}
<!-- MISSING_MACRO: command=ADD NGACTIONATTR list_name=add_ngactionattr_list_1 step_id=5 -->
```

### 6 添加DNS重定向预定义规则（PrePCC\_Rule02），用于关联1配置的条件组和5配置的动作组。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_rule_list_1的变量区（command: ADD RULE） -#}
<!-- MISSING_MACRO: command=ADD RULE list_name=add_rule_list_1 step_id=6 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_ruleconditiongroup_list_1的变量区（command: ADD RULECONDITIONGROUP） -#}
<!-- MISSING_MACRO: command=ADD RULECONDITIONGROUP list_name=add_ruleconditiongroup_list_1 step_id=6 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_rulengaction_list_1的变量区（command: ADD RULENGACTION） -#}
<!-- MISSING_MACRO: command=ADD RULENGACTION list_name=add_rulengaction_list_1 step_id=6 -->
```

### 7 将预定义规则关联到已配置的通用DNN策略中。策略MulDNN\_Policy01已在配置通用DNN策略数据完成配置。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_policyrule_list的变量区（command: ADD POLICYRULE） -#}
<!-- MISSING_MACRO: command=ADD POLICYRULE list_name=add_policyrule_list step_id=7 -->
```

### 此为新增的CLI脚本，需叠加至配置通用DNN策略数据已配置的脚本中。


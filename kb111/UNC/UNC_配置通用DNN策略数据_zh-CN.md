---
id: ''
name: 配置通用DNN策略数据
ne_type: UNC
type: feature
description: 用户上线接入通用DNN（common.dnn），PCF支持通过N7接口给SMF下发智能分流的动态规则，使园区业务从专用DNN（stjwt.gd）接入访问。
risk_level: ''
doc_source: ["网络部署","业务专题","5G Core 一跳入家解决方案","一跳入家解决方案（基于3GPP接入方案）","业务初始部署与调测","部署移动VPN","配置专用DNN数据","配置PCF","配置通用DNN数据","配置通用DNN策略数据"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
用户上线接入通用DNN（common.dnn），PCF支持通过N7接口给SMF下发智能分流的动态规则，使园区业务从专用DNN（stjwt.gd）接入访问。

## 必备事项
前提条件

前提条件

* 已按照运营商配置规范完成PCF网元的基本配置，并与周边网元完成对接。
* 用户已签约大网套餐，不需要PCF配置和下发大网套餐。
* 确认新建场景下的多DNN特性参数已规划，例如，专用DNN名称、IP地址池规划、园区IP地址列表、域名列表。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    add_plmn_list:
      type: items
      properties:
        PLMNIDENTITY:
          name: 'PLMN标识'
          type: string
          required: false
          description: 'PLMN的标识。  取值范围：长度为1～32字节的字符串，且不能输入的特殊字符为<>[]%#&"+=,;/'''
          data_source: '本端规划'
          pattern: ''
          default: ''
        PLMNTYPE:
          name: 'PLMNTYPE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MCC:
          name: 'MCC'
          type: string
          required: false
          description: 'PLMN所在的国家对应的移动国家码。  取值范围：长度为3位的数字。当MCC长度不足3位时，请在数字前面补0确保位数为3位。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        MNC:
          name: 'MNC'
          type: string
          required: false
          description: 'PLMN对应的移动网号。  取值范围：长度为2位或3位的数字。当MNC长度不足2位时，请在数字前面补0确保位数至少为2位。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_roamregion_list:
      type: items
      properties:
        ROAMREGIONIDENTITY:
          name: 'ROAMREGIONIDENTITY'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_roamregionplmn_list:
      type: items
      properties:
        ROAMREGIONIDENTITY:
          name: 'ROAMREGIONIDENTITY'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PLMNIDENTITY:
          name: 'PLMNIDENTITY'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
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
          description: '用于设置拜访地通用DNN。当用户从此DNN接入时，触发PCF下发多DNN策略。  取值范围：长度为1～64的字符串。'
          data_source: '全网规划'
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
          description: '用于设置异网漫游下的本网标识。只有当用户从本网接入时，才能触发PCF下发多DNN策略。  取值范围：长度为1～32字节的字符串。  说明：  若局点已开启异网漫游功能，则需要配置此条件，用于关联PLMN，从而确保不会对异网漫游接入的用户下发分流策略。'
          data_source: '本端规划'
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
    add_ngaction_list_2:
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
          name: '名称'
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
          description: '用于设置归属地园区DNN策略的动作标识，随信元MulDNNSessRules下发。  取值范围：长度为1～128字节的字符串，且不能输入的特殊字符为<>[]%#&"+=,;/'''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_ngactionattr_list_6:
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
          name: '名称'
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
          description: '用于设置归属地园区提供服务的IP地址段，通过PCF下发给SMF分流。  取值范围：长度不超过256字节的字符串，每个serviceURL仅支持携带一类流描述信息，每个流描述信息使用“;”作为分隔符，支持“\*”通配符。  IP地址段按实际规划配置，配置范围不宜过大，否则会影响SMF和UPF上的UE IP地址分配。该参数支持携带包括IP（段）、FQDN、URL等多种流描述信息，每类流描述信息含标识符前缀，标识符前缀区分大小写，标识符前缀后取值内容不区分大小写。  当该动作属性的“类型”配置为“Value”时，“值”支持直接配置和通过URL列表方式进行配置。   * Value类型的“值”直接配置时，参数支持包括IP（段）、FQDN、URL等多种流描述信息，每类流描述信息含标识符前缀。   + IPv4：标识符前缀固定为“IPv4-\_-”，IPv4段格式支持“X.X.X.X[/Y]” 和“from X.X.X.X to X.X.X.Y”两种模式，其中[]代表可选，/Y为掩码长度，即可以不指定掩码长度。   + IPv6：标识符前缀固定为“IPv6-\_-”，IPv6段格式支持“X:X:X::X[/Y]” 和“from X:X:X::X to X:X:X::Y”两种模式，其中[]代表可选，/Y为前缀长度，即可以不指定前缀长度。   + FQDN：标识符前缀固定为“FQDN-\_-”，FQDN中单个流描述信息的长度不超过128字节。   + URL：标识符前缀固定为“URL-\_-”。 * Value类型的“值”通过URL列表方式配置时，可单击“配置”，进入“配置serviceURL属性”界面进行配置，配置的相关参数请参考表3。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_ngactionattr_list_8:
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
          name: '名称'
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
        URLTYPE:
          name: 'URLTYPE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        URLVALUE:
          name: 'URLVALUE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_ngactionattr_list_12:
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
        PRECEDENCE:
          name: 'PRECEDENCE'
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
        USRLANGUAGE:
          name: 'USRLANGUAGE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        USRSMSRECEIVEFLAG:
          name: 'USRSMSRECEIVEFLAG'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        USRVERSTATUS:
          name: 'USRVERSTATUS'
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
  examples:
    add_plmn_list:
    - PLMNIDENTITY: PLMN_01
      PLMNTYPE: Local
      MCC: '100'
      MNC: '001'
    add_roamregion_list:
    - ROAMREGIONIDENTITY: Localnetwork
    add_roamregionplmn_list:
    - ROAMREGIONIDENTITY: Localnetwork
      PLMNIDENTITY: PLMN_01
    add_conditiongroup_list:
    - CONDITIONGROUPNAME: MulDNN_CG01
      RELATION: AND
      USETIMEZONE: No
    add_condition_list:
    - CONDITIONGROUPNAME: MulDNN_CG01
      CONDITIONNAME: MulDNN_C01
      OBJECTATTRIBUTE: SmfSession.Dnn
      OPERATOR: Equal
      RIGHTVALUETYPE: Value
      RIGHTVALUE: common.dnn
    add_condition_list_1:
    - CONDITIONGROUPNAME: MulDNN_CG01
      CONDITIONNAME: Roaming_C01
      OBJECTATTRIBUTE: SmfSession.RoamingRegion
      OPERATOR: Equal
      RIGHTVALUETYPE: Value
      RIGHTVALUE: Localnetwork
    add_ngaction_list:
    - ACTIONNAME: MulDNN_NSSAI
      TYPE: ServiceNSSAI
    add_ngaction_list_1:
    - ACTIONNAME: MulDNN_5GAG01
      TYPE: MulDNNSessRule
    add_ngaction_list_2:
    - ACTIONNAME: MulDNN_5GAG02
      TYPE: BasicInfoAction
    add_ngactionattr_list:
    - ACTIONNAME: MulDNN_NSSAI
      ATTRNAME: sd
      TYPE: Value
      VALUE: '000000'
    add_ngactionattr_list_2:
    - ACTIONNAME: MulDNN_5GAG01
      ATTRNAME: MulDNNSessRuleId
      TYPE: Value
      VALUE: MulDNNSessRule01
    add_ngactionattr_list_6:
    - ACTIONNAME: MulDNN_5GAG01
      ATTRNAME: serviceURL
      TYPE: Value
      VALUE: IPv4-_-10.0.0.1\;10.0.0.5\;from 10.10.10.10 to 10.10.10.20
    add_ngactionattr_list_8:
    - ACTIONNAME: MulDNN_5GAG01
      ATTRNAME: serviceURL
      TYPE: Value
      URLTYPE: IPv4
      URLVALUE: 10.0.0.1
    add_ngactionattr_list_12:
    - ACTIONNAME: MulDNN_5GAG02
      ATTRNAME: MulDNNSessRules
      TYPE: Reference ActionGroup
      VALUE: MulDNN_5GAG01
    add_rule_list:
    - RULENAME: MulDNN_Rule01
      TYPE: Smf Basic Rule 5G
      PRECEDENCE: '0'
      EDR: OFF
      RELATION: AND
    add_ruleconditiongroup_list:
    - RULENAME: MulDNN_Rule01
      CONDITIONGROUPNAME: MulDNN_CG01
    add_rulengaction_list:
    - RULENAME: MulDNN_Rule01
      ACTIONNAME: MulDNN_5GAG02
    add_policy_list:
    - POLICYNAME: MulDNN_Policy01
      TYPE: N7 Policy
    add_policyrule_list:
    - POLICYNAME: MulDNN_Policy01
      RULENAME: MulDNN_Rule01
    add_policytrigger_list:
    - POLICYNAME: MulDNN_Policy01
      TRIGGERNAME: IPCAN_EST
    add_service_list:
    - SERVICENAME: MulDNN_Service01
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
    - SERVICENAME: MulDNN_Service01
      POLICYNAME: MulDNN_Policy01
    add_psub_list:
    - USRIDENTIFIER: 46010381012\*\*\*\*
      USRSTATE: Normal
      USRPAIDTYPE: 'NULL'
      USRSTATION: Master
      USRCONTACTMETHOD: SMS
      USRBILLCYCLEDATE: '5'
      USRSUBNETTYPE: MBB
      USRLANGUAGE: 'NULL'
      USRSMSRECEIVEFLAG: All
      USRVERSTATUS: Normal
    add_psrv_list:
    - USRIDENTIFIER: 46010381012\*\*\*\*
      SRVNAME: MulDNN\_Service01
      SRVUSAGESTATE: Normal
      SRVROAMINGTYPE: 'NULL'
      SRVCONTACTMETHOD: None
      SRVCREATESUBSCRIBER: No
      PAYMENTFLAG: Yes
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 登录UPCF WebUI界面进行业务配置，在“系统管理 > 批处理 > CLI导入”界面执行以下CLI命令。

### 登录UPCF WebUI界面可参考《UPCF 产品文档》>UPCF WebUI GUI参考 > UPCF WebUI > 登录UPCF WebUI界面。

### 添加本网标识，此处以PLMN\_01（MCC="100",MNC="001"）、PLMN\_02（MCC="101",MNC="002"）为例进行配置。仅在局点已开启异网漫游功能时需要配置此条件，现网配置参数以局点实际情况为准。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_plmn_list的变量区（command: ADD PLMN） -#}
<!-- MISSING_MACRO: command=ADD PLMN list_name=add_plmn_list step_id=1 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_roamregion_list的变量区（command: ADD ROAMREGION） -#}
<!-- MISSING_MACRO: command=ADD ROAMREGION list_name=add_roamregion_list step_id=1 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_roamregionplmn_list的变量区（command: ADD ROAMREGIONPLMN） -#}
<!-- MISSING_MACRO: command=ADD ROAMREGIONPLMN list_name=add_roamregionplmn_list step_id=1 -->
```

### 2 添加条件组（MulDNN\_CG01），包含条件用户从通用DNN（common.dnn）上线。对于已开启异网漫游功能的局点，还需将用户从本网（Localnetwork）接入添加至此条件组。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_conditiongroup_list的变量区（command: ADD CONDITIONGROUP） -#}
<!-- MISSING_MACRO: command=ADD CONDITIONGROUP list_name=add_conditiongroup_list step_id=2 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_condition_list的变量区（command: ADD CONDITION） -#}
<!-- MISSING_MACRO: command=ADD CONDITION list_name=add_condition_list step_id=2 -->
```

#### 2.1 /*局点开启异网漫游功能时，需要同时添加用户从Localnetwork上线的条件 */

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_condition_list_1的变量区（command: ADD CONDITION） -#}
<!-- MISSING_MACRO: command=ADD CONDITION list_name=add_condition_list_1 step_id=2.1 -->
```

### 3 添加5G动作组，分别用于配置切片信息（MulDNN\_NSSAI），多DNN动作（MulDNN\_5GAG01）和SM策略动作（MulDNN\_5GAG02）的动作类型。

#### 3.1 /*添加5G动作组MulDNN_NSSAI，用于配置切片信息,动作类型为ServiceNSSAI */

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_ngaction_list的变量区（command: ADD NGACTION） -#}
<!-- MISSING_MACRO: command=ADD NGACTION list_name=add_ngaction_list step_id=3.1 -->
```

#### 3.2 /*添加5G动作组MulDNN_5GAG01，用于配置URL、DNN和切片信息，动作类型为MulDNNSessRule，此处以配置IPv4和FQDN为例*/

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_ngaction_list_1的变量区（command: ADD NGACTION） -#}
<!-- MISSING_MACRO: command=ADD NGACTION list_name=add_ngaction_list_1 step_id=3.2 -->
```

#### 3.3 /*添加5G动作组MulDNN_5GAG02，用于配置SM策略动作，动作类型为BasicInfoAction */

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_ngaction_list_2的变量区（command: ADD NGACTION） -#}
<!-- MISSING_MACRO: command=ADD NGACTION list_name=add_ngaction_list_2 step_id=3.3 -->
```

### 4 给5G动作组MulDNN\_NSSAI添加子参数，添加的切片参数以sd=000000，sst=1为例。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_ngactionattr_list的变量区（command: ADD NGACTIONATTR） -#}
<!-- MISSING_MACRO: command=ADD NGACTIONATTR list_name=add_ngactionattr_list step_id=4 -->
```

### 5 给5G动作组MulDNN\_5GAG01添加子参数，配置园区提供服务的多个地址需要用“;”作为分隔符，CLI脚本需要在分隔符前添加转义字符“\”。以配置IPv4和FQDN为例：

### IPv4地址：10.0.0.1、10.0.0.5、从10.10.10.10到10.10.10.20地址段。

### FQDN地址：\*.huawei.com。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_ngactionattr_list_2的变量区（command: ADD NGACTIONATTR） -#}
<!-- MISSING_MACRO: command=ADD NGACTIONATTR list_name=add_ngactionattr_list_2 step_id=5 -->
```

#### 5.1 /*通过VALUE配置serviceURL*/

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_ngactionattr_list_6的变量区（command: ADD NGACTIONATTR） -#}
<!-- MISSING_MACRO: command=ADD NGACTIONATTR list_name=add_ngactionattr_list_6 step_id=5.1 -->
```

#### 上述serviceURL还可以通过URLTYPE和URLVALUE配置，两种方法选一种配置即可，脚本如下：

#### 5.2 /*通过URLTYPE和URLVALUE配置serviceURL*/

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_ngactionattr_list_8的变量区（command: ADD NGACTIONATTR） -#}
<!-- MISSING_MACRO: command=ADD NGACTIONATTR list_name=add_ngactionattr_list_8 step_id=5.2 -->
```

### 6 给5G动作组添加子参数，给MulDNN\_5GAG02添加MulDNNSessRules参数，用于引用5中配置的多DNN动作组。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_ngactionattr_list_12的变量区（command: ADD NGACTIONATTR） -#}
<!-- MISSING_MACRO: command=ADD NGACTIONATTR list_name=add_ngactionattr_list_12 step_id=6 -->
```

### 7 添加规则MulDNN\_Rule01，用于关联2中配置的条件组和6中配置的5G动作组。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_rule_list的变量区（command: ADD RULE） -#}
<!-- MISSING_MACRO: command=ADD RULE list_name=add_rule_list step_id=7 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_ruleconditiongroup_list的变量区（command: ADD RULECONDITIONGROUP） -#}
<!-- MISSING_MACRO: command=ADD RULECONDITIONGROUP list_name=add_ruleconditiongroup_list step_id=7 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_rulengaction_list的变量区（command: ADD RULENGACTION） -#}
<!-- MISSING_MACRO: command=ADD RULENGACTION list_name=add_rulengaction_list step_id=7 -->
```

### 8 添加策略MulDNN\_Policy01，此策略在用户上线时被调用，触发器为IPCAN\_EST、PLMN\_CH（异网漫游场景），用于控制7中配置的规则的下发。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_policy_list的变量区（command: ADD POLICY） -#}
<!-- MISSING_MACRO: command=ADD POLICY list_name=add_policy_list step_id=8 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_policyrule_list的变量区（command: ADD POLICYRULE） -#}
<!-- MISSING_MACRO: command=ADD POLICYRULE list_name=add_policyrule_list step_id=8 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_policytrigger_list的变量区（command: ADD POLICYTRIGGER） -#}
<!-- MISSING_MACRO: command=ADD POLICYTRIGGER list_name=add_policytrigger_list step_id=8 -->
```

### 9 添加业务MulDNN\_Service01，此业务即为需要PCF下发的分流业务，包含8配置的策略。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_service_list的变量区（command: ADD SERVICE） -#}
<!-- MISSING_MACRO: command=ADD SERVICE list_name=add_service_list step_id=9 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_servicepolicy_list的变量区（command: ADD SERVICEPOLICY） -#}
<!-- MISSING_MACRO: command=ADD SERVICEPOLICY list_name=add_servicepolicy_list step_id=9 -->
```

### 10 在BOSS或PGW Web LMT上进行业务发放。

#### 10.1 商用场景下，在BOSS上完成园区用户开户，并签约已配置的多DNN业务MulDNN\_Service01。

#### 10.2 测试场景下，用户需要在PGW Web LMT上完成用户的开户和签约，执行以下命令。

##### 10.2.1 登录“UPCF 业务管理”窗口可参考《UPCF 产品文档》> PGW Web LMT GUI参考 > PGW Web LMT > 登录“UPCF 业务管理”窗口。

##### 10.2.2 若局点已加载定制适配包AdpConfig\_\*\*\*\_VxxxRxxxCxx.tar，则以下开户和签约命令需要替换为局点对应的定制命令。

##### 10.2.3 执行**ADD PSUB**增加一个用户。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_psub_list的变量区（command: ADD PSUB） -#}
<!-- MISSING_MACRO: command=ADD PSUB list_name=add_psub_list step_id=10.2.3 -->
```

##### 10.2.4 执行**ADD PSRV**给用户签约业务。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_psrv_list的变量区（command: ADD PSRV） -#}
<!-- MISSING_MACRO: command=ADD PSRV list_name=add_psrv_list step_id=10.2.4 -->
```


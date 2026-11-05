---
id: ''
name: SMF侧业务配置
ne_type: UNC
type: feature
description: 根据整体方案设计，SMF侧需配置1个预定义规则与1个预定义规则组：  * 规则名“Rule\_Normal”：关键参数为5QI=5，ARP=2，MFBR=100 Mbit/s。 * 规则组名“up\_Exhaust”：关键参数为5QI=5，ARP=2，MFBR=1 Kbit/s。
risk_level: ''
doc_source: ["网络部署","业务专题","5G PCC之SM策略解决方案","典型业务场景E2E方案设计","业务重定向方案（预定义+动态）","E2E业务配置","E2E预定义规则配置","SMF侧业务配置"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
根据整体方案设计，SMF侧需配置1个预定义规则与1个预定义规则组：* 规则名“Rule\_Normal”：关键参数为5QI=5，ARP=2，MFBR=100 Mbit/s。* 规则组名“up\_Exhaust”：关键参数为5QI=5，ARP=2，MFBR=1 Kbit/s。

## 必备事项
前提条件

* 请仔细阅读UNC特性之《WSFD-109101 PCC基本功能》。
* 完成加载License（如果有需求，请联系华为技术支持工程师）。
* 已通过学习SM策略E2E实现原理、业务配置方法及E2E业务调测了解了SM策略的配置原理及方法。
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
          name: '本地用户动态PCC功能'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_apnpccfunc_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        HOMEPCCSWITCH:
          name: '本地用户动态PCC功能'
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
        ROAMPCCSWITCH:
          name: '漫游用户动态PCC功能'
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
          name: '拜访用户动态PCC功能'
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
    add_urr_list:
      type: items
      properties:
        URRNAME:
          name: '使用量上报规则名称'
          type: string
          maxLength: 31
          required: true
          description: '存在多条记录时，该参数不能重复。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        URRID:
          name: 'URR标识'
          type: integer
          minimum: 0
          maximum: 2147483646
          required: true
          description: '该参数需要与UPF上的URR标识保持一致。'
          data_source: '与对端协商'
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
        MONITORINGKEY:
          name: '监控属性值'
          type: string
          maxLength: 31
          required: false
          description: '该参数取值须与PCF侧定义的配额监控键值保持一致。'
          data_source: '与对端协商'
          pattern: ''
          default: ''
        N40AGESW:
          name: 'N40接口场景下是否允许老化'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ENABLE
        OFCSRVTMPLNAME:
          name: '离线业务模板名'
          type: string
          maxLength: 63
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        OFFCOMPOUNDTYPE:
          name: '离线计费标识组成类型'
          type: string
          enum:
          - ONLYRG
          - ONLYSID
          - RGSID
          - UPDOWNSID
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        OFFMETERINGTYPE:
          name: '离线计费统计类型'
          type: string
          enum:
          - EVENT
          - EVENT_TIME
          - EVENT_VOLUME
          - EVENT_VOLUME_TIME
          - FREE
          - TIME
          - VOLUME
          - VOLUME_TIME
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ONLCOMPOUNDTYPE:
          name: '在线计费标识组成类型'
          type: string
          enum:
          - ONLYRG
          - RGSID
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ONLMETERINGTYPE:
          name: '在线计费统计类型'
          type: string
          enum:
          - EVENT
          - EVENT_TIME
          - EVENT_VOLUME
          - EVENT_VOLUME_TIME
          - FREE
          - TIME
          - VOLUME
          - VOLUME_TIME
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        REDIRENDTOKEN:
          name: 'Gy重定向结束Token'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_urrgroup_list:
      type: items
      properties:
        URRGROUPNAME:
          name: '使用量上报规则组名称'
          type: string
          maxLength: 31
          required: true
          description: '存在多条记录时，该参数不能重复。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        UPURRNAME1:
          name: '上行发起URR名称1'
          type: string
          maxLength: 31
          required: false
          description: '使用**ADD URR**定义的URRNAME。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        DOWNURRNAME1:
          name: '下行发起URR名称1'
          type: string
          maxLength: 31
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
          description: '存在多条记录时，不能重复。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        MBRUPLKVALUE:
          name: '最大上行比特率'
          type: integer
          minimum: 0
          maximum: 20000000
          required: false
          description: '此处数据仅为举例，请根据业务模型进行规划。  创建专有QoSFlow/专有承载时，以SMF上此处配置的为准。'
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
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ARPVALUE:
          name: '分配保留优先级'
          type: integer
          minimum: 1
          maximum: 15
          required: false
          description: '“QOSTYPE”为“QOS\_FLOW\_PARA”时需要规划。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        FQI:
          name: '5G QoS标识'
          type: integer
          minimum: 1
          maximum: 255
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        QOSURRNAME:
          name: 'QoS使用量上报规则名称'
          type: string
          maxLength: 31
          required: false
          description: '使用**ADD URR**定义的URRNAME。'
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
    add_qosprop_list_1:
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
        MBRUPLKVALUE:
          name: '最大上行比特率'
          type: integer
          minimum: 0
          maximum: 20000000
          required: false
          description: '此处数据仅为举例，请根据业务模型进行规划。  创建专有QoSFlow/专有承载时，以SMF上此处配置的为准。'
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
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ARPVALUE:
          name: '分配保留优先级'
          type: integer
          minimum: 1
          maximum: 15
          required: false
          description: '“QOSTYPE”为“QOS\_FLOW\_PARA”时需要规划。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        FQI:
          name: '5G QoS标识'
          type: integer
          minimum: 1
          maximum: 255
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        QOSURRNAME:
          name: 'QoS使用量上报规则名称'
          type: string
          maxLength: 31
          required: false
          description: '使用**ADD URR**定义的URRNAME。'
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
          description: '存在多条记录时，该参数不能重复。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        URRGROUPNAME:
          name: '使用量上报规则组名称'
          type: string
          maxLength: 31
          required: false
          description: '使用**ADD URRGROUP**定义的“URRGROUPNAME”。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        QOSPROPNAME:
          name: 'QoS属性名称'
          type: string
          maxLength: 31
          required: false
          description: '使用**ADD QOSPROP**定义的**QOSPROPNAME**。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_pccpolicygrp_list_1:
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
        URRGROUPNAME:
          name: '使用量上报规则组名称'
          type: string
          maxLength: 31
          required: false
          description: '使用**ADD URRGROUP**定义的“URRGROUPNAME”。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        QOSPROPNAME:
          name: 'QoS属性名称'
          type: string
          maxLength: 31
          required: false
          description: '使用**ADD QOSPROP**定义的**QOSPROPNAME**。'
          data_source: '本端规划'
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
          description: '需根据业务策略选择相应的策略类型。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PRIORITY:
          name: '全局优先级'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: false
          description: '值越小，优先级越高。'
          data_source: '本端规划'
          pattern: ''
          default: 4294967295
        POLICYNAME:
          name: '策略名称'
          type: string
          maxLength: 63
          required: false
          description: '使用**ADD PCCPOLICYGRP**定义的“PCCPOLICYGRPNM”。'
          data_source: '已配置数据中获取'
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
          description: '与UPF上配置的用户模板名称保持一致。'
          data_source: '与对端协商'
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
          description: '-'
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
          description: ''
          data_source: ''
          pattern: ''
          default: ALL
    add_rulebinding_list:
      type: items
      properties:
        USERPROFILENAME:
          name: '模板名称'
          type: string
          maxLength: 63
          required: true
          description: '使用**ADD USERPROFILE**命令定义的用户模板名称。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        RULENAME:
          name: '规则名称'
          type: string
          maxLength: 63
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV2FUPSAT01'
      SWITCH: ENABLE
    set_pccfunc_list:
    - HOMEPCCSWITCH: ENABLE
    set_apnpccfunc_list:
    - APN: 'cmnet'
      HOMEPCCSWITCH: ENABLE
      ROAMPCCSWITCH: ENABLE
      VISITPCCSWITCH: ENABLE
    add_urr_list:
    - URRNAME: 'urr_QoS2'
      URRID: 2
      USAGERPTMODE: QOS
      MONITORINGKEY: '101'
      N40AGESW: ENABLE
      OFCSRVTMPLNAME: ''
      OFFCOMPOUNDTYPE: ''
      OFFMETERINGTYPE: ''
      ONLCOMPOUNDTYPE: ''
      ONLMETERINGTYPE: ''
      REDIRENDTOKEN: ''
    add_urrgroup_list:
    - URRGROUPNAME: 'urrg_qos_service'
      UPURRNAME1: 'urr_MK'
      DOWNURRNAME1: 'urr_MK'
    add_qosprop_list:
    - QOSPROPNAME: 'qosprop_5qi5_arp2_100M'
      MBRUPLKVALUE: 100000
      MBRDNLKVALUE: 100000
      QOSTYPE: QOS_FLOW_PARA
      ARPVALUE: 2
      FQI: 5
      QOSURRNAME: 'urr_QoS2'
      EMPCAP: DISABLE
      EMPVUL: ENABLE
      QCIVALUE: ''
      RQI: ''
    add_qosprop_list_1:
    - QOSPROPNAME: 'qosprop_5qi5_arp2_1K'
      MBRUPLKVALUE: 1
      MBRDNLKVALUE: 1
      QOSTYPE: QOS_FLOW_PARA
      ARPVALUE: 2
      FQI: 5
      QOSURRNAME: 'urr_QoS3'
      EMPCAP: DISABLE
      EMPVUL: ENABLE
      QCIVALUE: ''
      RQI: ''
    add_pccpolicygrp_list:
    - PCCPOLICYGRPNM: 'pccfuppolicy_100M'
      URRGROUPNAME: 'urrg_qos_service'
      QOSPROPNAME: 'qosprop_5qi5_arp2_100M'
    add_pccpolicygrp_list_1:
    - PCCPOLICYGRPNM: 'pccfuppolicy_1K'
      URRGROUPNAME: 'urrg_qos_service'
      QOSPROPNAME: 'qosprop_5qi5_arp2_1K'
    add_rule_list:
    - RULENAME: 'Rule_Normal'
      POLICYTYPE: PCC
      PRIORITY: 10
      POLICYNAME: 'pccfuppolicy_100M'
      FLOWFILTERNAME: ''
      PROTODESCDL: ''
      PROTODESCUL: ''
      RULERANGE: ALL
    add_userprofile_list:
    - USERPROFILENAME: 'up_Exhaust'
      UPTYPE: PCC
      PROFILERANGE: ALL
    add_rulebinding_list:
    - USERPROFILENAME: 'up_Exhaust'
      RULENAME: 'Rule_Exhaust'
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 登录UNC CSP OM Portal，进入“MML命令行-UNC”窗口。

### 2 开启License。

### 该步骤为预定义规则（组）场景下的必选配置。执行SET LICENSESWITCH命令设置基于使用量特性对应的License开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

### 3 打开PCC功能开关。

### 步骤为预定义规则（组）场景下的必选配置。预定义规则（组）场景下，策略下发都涉及PCF网元配置，因此需打开此开关。

```jinja2
{%- for item in set_pccfunc_list -%}
    SET PCCFUNC:
    {#- --- 可选参数 --- -#}
    {%- if item.HOMEPCCSWITCH is not none -%}
        HOMEPCCSWITCH={{item.HOMEPCCSWITCH}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 （条件可选）使能APN PCC开关。

### 该步骤主要用于使能或关闭指定APN/DNN用户的动态PCC功能。例如当前网络中有两个数据APN，分别为APN1和APN2，可通过配置此命令对APN1与APN2做业务隔离。

```jinja2
{%- if is_optional_apn_pcc_switch -%}
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
        ;
    {%- endfor -%}
{%- endif -%}
```

### 针对多APN组网复杂的场景，建议配置此命令。

### 5 配置QoS URR与MK URR。

### 该步骤为预定义规则（组）场景下的可选配置，只有在基于使用量上报/QoS控制/计费控制场景才需配置，此处根据需求描述需配置QoS URR与MK URR。

```jinja2
{%- for item in add_urr_list -%}
    ADD URR:
    {#- --- 必选参数 --- -#}
    URRNAME="{{item.URRNAME}}",
    URRID={{item.URRID}},
    USAGERPTMODE={{item.USAGERPTMODE}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：USAGERPTMODE=MONITORINGKEY 时必选 --- -#}
    {%- if item.USAGERPTMODE == 'MONITORINGKEY' -%}
        MONITORINGKEY="{{item.MONITORINGKEY}}",
    {%- endif -%}
    {#- --- 条件必选：USAGERPTMODE=OFFLINE 时必选 --- -#}
    {%- if item.USAGERPTMODE == 'OFFLINE' -%}
        OFFCOMPOUNDTYPE={{item.OFFCOMPOUNDTYPE}},
    {%- endif -%}
    {#- --- 条件必选：USAGERPTMODE=ONLINE 时必选 --- -#}
    {%- if item.USAGERPTMODE == 'ONLINE' -%}
        ONLCOMPOUNDTYPE={{item.ONLCOMPOUNDTYPE}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：USAGERPTMODE=OFFLINE/ONLINE 时可选 --- -#}
    {%- if item.USAGERPTMODE in ['OFFLINE', 'ONLINE'] -%}
        {%- if item.N40AGESW is not none -%}
            N40AGESW={{item.N40AGESW}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：USAGERPTMODE=OFFLINE 时可选 --- -#}
    {%- if item.USAGERPTMODE == 'OFFLINE' -%}
        {%- if item.OFCSRVTMPLNAME is not none -%}
            OFCSRVTMPLNAME="{{item.OFCSRVTMPLNAME}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：USAGERPTMODE=OFFLINE 时可选 --- -#}
    {%- if item.USAGERPTMODE == 'OFFLINE' -%}
        {%- if item.OFFMETERINGTYPE is not none -%}
            OFFMETERINGTYPE={{item.OFFMETERINGTYPE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：USAGERPTMODE=ONLINE 时可选 --- -#}
    {%- if item.USAGERPTMODE == 'ONLINE' -%}
        {%- if item.ONLMETERINGTYPE is not none -%}
            ONLMETERINGTYPE={{item.ONLMETERINGTYPE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：USAGERPTMODE=ONLINE 时可选 --- -#}
    {%- if item.USAGERPTMODE == 'ONLINE' -%}
        {%- if item.REDIRENDTOKEN is not none -%}
            REDIRENDTOKEN="{{item.REDIRENDTOKEN}}",
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 6 配置URR Group用于关联QoS URR及MK URR。

```jinja2
{%- for item in add_urrgroup_list -%}
    ADD URRGROUP:
    {#- --- 必选参数 --- -#}
    URRGROUPNAME="{{item.URRGROUPNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.UPURRNAME1 is not none -%}
        UPURRNAME1="{{item.UPURRNAME1}}",
    {%- endif -%}
    {%- if item.DOWNURRNAME1 is not none -%}
        DOWNURRNAME1="{{item.DOWNURRNAME1}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 7 配置QoS参数。

### 该步骤为预定义规则（组）场景下的可选配置。只有在需要对用户进行带宽控制或建立专有QoS Flow时，才需配置。须配置配额耗尽前、耗尽后两种场景的带宽控制策略。

### 当用户配额未耗尽时，即PCF下发预定义规则“Rule\_Normal”场景，此处5QI/ARP表1取值参考规划分别取5和2。

```jinja2
{%- for item in add_qosprop_list -%}
    ADD QOSPROP:
    {#- --- 必选参数 --- -#}
    QOSPROPNAME="{{item.QOSPROPNAME}}",
    QOSTYPE={{item.QOSTYPE}},
    {#- --- 可选参数 --- -#}
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

### 当用户配额耗尽时，即PCF下发预定义规则组“up\_Exhaust”场景，此处5QI/ARP取值参考表1规划分别取5和2。

```jinja2
{%- for item in add_qosprop_list_1 -%}
    ADD QOSPROP:
    {#- --- 必选参数 --- -#}
    QOSPROPNAME="{{item.QOSPROPNAME}}",
    QOSTYPE={{item.QOSTYPE}},
    {#- --- 可选参数 --- -#}
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

### 8 配置PCC策略组。

### 该步骤为预定义规则（组）场景下的必选配置。配置PCC策略组的目的是用于关联QoS URR及MK URR策略。此处“URRGROUPNAME”参数使用ADD URRGROUP定义的“URRGROUPNAME”。

### 配额未耗尽时关联如下策略：

```jinja2
{%- for item in add_pccpolicygrp_list -%}
    ADD PCCPOLICYGRP:
    {#- --- 必选参数 --- -#}
    PCCPOLICYGRPNM="{{item.PCCPOLICYGRPNM}}",
    {#- --- 可选参数 --- -#}
    {%- if item.URRGROUPNAME is not none -%}
        URRGROUPNAME="{{item.URRGROUPNAME}}",
    {%- endif -%}
    {%- if item.QOSPROPNAME is not none -%}
        QOSPROPNAME="{{item.QOSPROPNAME}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 配额耗尽后关联如下策略：

```jinja2
{%- for item in add_pccpolicygrp_list_1 -%}
    ADD PCCPOLICYGRP:
    {#- --- 必选参数 --- -#}
    PCCPOLICYGRPNM="{{item.PCCPOLICYGRPNM}}",
    {#- --- 可选参数 --- -#}
    {%- if item.URRGROUPNAME is not none -%}
        URRGROUPNAME="{{item.URRGROUPNAME}}",
    {%- endif -%}
    {%- if item.QOSPROPNAME is not none -%}
        QOSPROPNAME="{{item.QOSPROPNAME}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 9 配置预定义规则。

### 该步骤为预定义规则（组）场景下的必选配置。主要用于关联PCC策略组。此处预定义规则名称、数量都须与PCF侧定义的保持一致。

```jinja2
{%- for item in add_rule_list -%}
    ADD RULE:
    {#- --- 必选参数 --- -#}
    RULENAME="{{item.RULENAME}}",
    POLICYTYPE={{item.POLICYTYPE}},
    {#- --- 可选参数 --- -#}
    {%- if item.PRIORITY is not none -%}
        PRIORITY={{item.PRIORITY}},
    {%- endif -%}
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
```

### 10 （配额耗尽场景）配置用户模板。

### 根据SMF（UNC）侧业务设计（可选），配额耗尽场景SMF侧需配置预定义规则组。

```jinja2
{%- if is_scenario_quota_exhausted -%}
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
{%- endif -%}
```

### 11 （配额耗尽场景）配置用户模板与规则绑定关系。

```jinja2
{%- if is_scenario_quota_exhausted -%}
    {%- for item in add_rulebinding_list -%}
        ADD RULEBINDING:
        {#- --- 必选参数 --- -#}
        USERPROFILENAME="{{item.USERPROFILENAME}}",
        RULENAME="{{item.RULENAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```


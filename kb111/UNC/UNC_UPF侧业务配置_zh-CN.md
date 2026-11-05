---
id: ''
name: UPF侧业务配置
ne_type: UNC
type: feature
description: 根据整体方案设计，UPF侧需配置两个预定义规则：  * 规则名“Predefined1”：关键参数为5QI=5，ARP=2，MFBR=100Mbit/s及流描述。 * 规则名“Predefined2”：关键参数为5QI=5，ARP=2，MFBR=1Mbit/s及流描述。
risk_level: ''
doc_source: ["网络部署","业务专题","5G PCC之SM策略解决方案","典型业务场景E2E方案设计","基于位置区域的带宽差异化控制方案（预定义）","E2E业务配置","UPF侧业务配置"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
根据整体方案设计，UPF侧需配置两个预定义规则：* 规则名“Predefined1”：关键参数为5QI=5，ARP=2，MFBR=100Mbit/s及流描述。* 规则名“Predefined2”：关键参数为5QI=5，ARP=2，MFBR=1Mbit/s及流描述。

## 必备事项
前提条件

* 请仔细阅读UDG特性之《GWFD-020351 PCC基本功能》。
* 完成加载License（如果有需求，请联系华为技术支持工程师）。
* 已通过学习SM策略E2E实现原理、业务配置方法及E2E业务调测了解了SM策略的配置原理及方法。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    add_filter_list:
      type: items
      properties:
        FILTERNAME:
          name: '过滤器名称'
          type: string
          required: false
          description: '不同过滤器之间，该参数不能重复。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        L34PROTTYPE:
          name: '三四层IPv4协议输入类型'
          type: string
          required: false
          description: 'Any to any的三四层filter。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        L34PROTOCOL:
          name: '三四层协议类型'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_filter_list_1:
      type: items
      properties:
        FILTERNAME:
          name: '过滤器名称'
          type: string
          required: false
          description: '不同过滤器之间，该参数不能重复。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        L34PROTTYPE:
          name: '三四层IPv4协议输入类型'
          type: string
          required: false
          description: 'Any to any的三四层filter。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        L34PROTOCOL:
          name: '三四层协议类型'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_flowfilter_list:
      type: items
      properties:
        FLOWFILTERNAME:
          name: '流过滤器名称'
          type: string
          maxLength: 63
          required: true
          description: '不同流过滤器之间，该参数不能重复。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_fltbindflowf_list:
      type: items
      properties:
        FLOWFILTERNAME:
          name: '流过滤器名称'
          type: string
          required: false
          description: '使用**ADD FLOWFILTER**命令定义的流过滤器名称。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        FILTERNAME:
          name: '过滤器名称'
          type: string
          required: false
          description: '使用**ADD FILTER**命令定义的过滤器名称。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_flowfilter_list_1:
      type: items
      properties:
        FLOWFILTERNAME:
          name: '流过滤器名称'
          type: string
          maxLength: 63
          required: true
          description: '不同流过滤器之间，该参数不能重复。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_fltbindflowf_list_1:
      type: items
      properties:
        FLOWFILTERNAME:
          name: '流过滤器名称'
          type: string
          required: false
          description: '使用**ADD FLOWFILTER**命令定义的流过滤器名称。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        FILTERNAME:
          name: '过滤器名称'
          type: string
          required: false
          description: '使用**ADD FILTER**命令定义的过滤器名称。'
          data_source: '已配置数据中获取'
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
          description: '该参数需要与SMF上的URR标识保持一致。'
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
          description: ''
          data_source: ''
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
    add_qosprop_list:
      type: items
      properties:
        QOSPROPNAME:
          name: 'QoS属性名称'
          type: string
          required: false
          description: '存在多条记录时，不能重复。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        MBRUPLKVALUE:
          name: '最大上行比特率'
          type: string
          required: false
          description: '此处数据仅为举例，请根据业务模型进行规划。  创建专有QoSFlow/专有承载时，以SMF上此处配置的为准。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        MBRDNLKVALUE:
          name: '最大下行比特率'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        QOSURRNAME:
          name: 'QoS使用量上报规则名称'
          type: string
          required: false
          description: '使用**ADD URR**定义的URRNAME。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        DECOUPLINGSW:
          name: 'DECOUPLINGSW'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        KEYFLOWDETECTSW:
          name: 'KEYFLOWDETECTSW'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        EMPCAP:
          name: 'QoS抢占能力'
          type: string
          required: false
          description: '该业务可以抢占已经分配给其他低优先级业务流的资源时，设置为ENABLE。此处以不抢占为例。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        EMPVUL:
          name: 'QoS被抢占设置'
          type: string
          required: false
          description: '其他高优先级业务不能抢占本业务流的资源时，设置为DISABLE。此处以被抢占为例。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_qosprop_list_1:
      type: items
      properties:
        QOSPROPNAME:
          name: 'QoS属性名称'
          type: string
          required: false
          description: '存在多条记录时，不能重复。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        MBRUPLKVALUE:
          name: '最大上行比特率'
          type: string
          required: false
          description: '此处数据仅为举例，请根据业务模型进行规划。  创建专有QoSFlow/专有承载时，以SMF上此处配置的为准。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        MBRDNLKVALUE:
          name: '最大下行比特率'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        QOSURRNAME:
          name: 'QoS使用量上报规则名称'
          type: string
          required: false
          description: '使用**ADD URR**定义的URRNAME。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        DECOUPLINGSW:
          name: 'DECOUPLINGSW'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        KEYFLOWDETECTSW:
          name: 'KEYFLOWDETECTSW'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        EMPCAP:
          name: 'QoS抢占能力'
          type: string
          required: false
          description: '该业务可以抢占已经分配给其他低优先级业务流的资源时，设置为ENABLE。此处以不抢占为例。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        EMPVUL:
          name: 'QoS被抢占设置'
          type: string
          required: false
          description: '其他高优先级业务不能抢占本业务流的资源时，设置为DISABLE。此处以被抢占为例。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_pccpolicygrp_list:
      type: items
      properties:
        PCCPOLICYGRPNM:
          name: 'PCC策略组名称'
          type: string
          required: false
          description: '存在多条记录时，该参数不能重复。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        FUPSESSIONEXC:
          name: 'FUPSESSIONEXC'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TOKENFUNCFLAG:
          name: 'TOKENFUNCFLAG'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SIGNALASSOCIATE:
          name: 'SIGNALASSOCIATE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ADCMUTEFLAG:
          name: 'ADCMUTEFLAG'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        QOSPROPNAME:
          name: 'QoS属性名称'
          type: string
          required: false
          description: '使用**ADD QOSPROP**定义的**QOSPROPNAME**。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        HTTP2DEGRADESW:
          name: 'HTTP2DEGRADESW'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        EVENTCHARGEFLAG:
          name: 'EVENTCHARGEFLAG'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        EVENTCHGPOINT:
          name: 'EVENTCHGPOINT'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MMSCHARGETYPE:
          name: 'MMSCHARGETYPE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_pccpolicygrp_list_1:
      type: items
      properties:
        PCCPOLICYGRPNM:
          name: 'PCC策略组名称'
          type: string
          required: false
          description: '存在多条记录时，该参数不能重复。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        FUPSESSIONEXC:
          name: 'FUPSESSIONEXC'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TOKENFUNCFLAG:
          name: 'TOKENFUNCFLAG'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SIGNALASSOCIATE:
          name: 'SIGNALASSOCIATE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ADCMUTEFLAG:
          name: 'ADCMUTEFLAG'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        QOSPROPNAME:
          name: 'QoS属性名称'
          type: string
          required: false
          description: '使用**ADD QOSPROP**定义的**QOSPROPNAME**。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        HTTP2DEGRADESW:
          name: 'HTTP2DEGRADESW'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        EVENTCHARGEFLAG:
          name: 'EVENTCHARGEFLAG'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        EVENTCHGPOINT:
          name: 'EVENTCHGPOINT'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MMSCHARGETYPE:
          name: 'MMSCHARGETYPE'
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
          name: '规则名称'
          type: string
          required: false
          description: '存在多条数据时，该参数+策略类型不能完全相同。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        POLICYTYPE:
          name: '策略类型'
          type: string
          required: false
          description: '需根据业务策略选择相应的策略类型。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        FILTERINGMODE:
          name: 'FILTERINGMODE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        FLOWFILTERNAME:
          name: '流过滤器名称'
          type: string
          required: false
          description: '使用**ADD FLOWFILTER**命令定义的流过滤器名称。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        PRIORITY:
          name: '全局优先级'
          type: string
          required: false
          description: '值越小，优先级越高。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        POLICYNAME:
          name: '策略名称'
          type: string
          required: false
          description: '使用**ADD PCCPOLICYGRP**定义的“PCCPOLICYGRPNM”。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    set_refreshsrv_list:
      type: items
      properties:
        REFRESHTYPE:
          name: 'REFRESHTYPE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    add_filter_list:
    - FILTERNAME: f_fup_service_100M
      L34PROTTYPE: STRING
      L34PROTOCOL: ANY
    add_filter_list_1:
    - FILTERNAME: f_fup_service_1M
      L34PROTTYPE: STRING
      L34PROTOCOL: ANY
    add_flowfilter_list:
    - FLOWFILTERNAME: 'flowfliter_service_100M'
    add_fltbindflowf_list:
    - FLOWFILTERNAME: flowfliter_service_100M
      FILTERNAME: f_fup_service_100M
    add_flowfilter_list_1:
    - FLOWFILTERNAME: 'flowfliter_service_1M'
    add_fltbindflowf_list_1:
    - FLOWFILTERNAME: flowfliter_service_1M
      FILTERNAME: f_fup_service_1M
    add_urr_list:
    - URRNAME: 'urr_QoS2'
      URRID: 2
      USAGERPTMODE: QOS
      MONITORINGKEY: ''
      N40AGESW: ENABLE
      OFCSRVTMPLNAME: ''
      OFFCOMPOUNDTYPE: ''
      OFFMETERINGTYPE: ''
      ONLCOMPOUNDTYPE: ''
      ONLMETERINGTYPE: ''
      REDIRENDTOKEN: ''
    add_qosprop_list:
    - QOSPROPNAME: qosprop_5qi5_arp2_100
      MBRUPLKVALUE: '100000'
      MBRDNLKVALUE: '100000'
      QOSURRNAME: urr_QoS2
      DECOUPLINGSW: DISABLE
      KEYFLOWDETECTSW: DISABLE
      EMPCAP: DISABLE
      EMPVUL: ENABLE
    add_qosprop_list_1:
    - QOSPROPNAME: qosprop_5qi5_arp2_1
      MBRUPLKVALUE: '1000'
      MBRDNLKVALUE: '1000'
      QOSURRNAME: urr_QoS3
      DECOUPLINGSW: DISABLE
      KEYFLOWDETECTSW: DISABLE
      EMPCAP: DISABLE
      EMPVUL: ENABLE
    add_pccpolicygrp_list:
    - PCCPOLICYGRPNM: pccfuppolicy_100M
      FUPSESSIONEXC: DISABLE
      TOKENFUNCFLAG: DISABLE
      SIGNALASSOCIATE: ENABLE
      ADCMUTEFLAG: ENABLE
      QOSPROPNAME: qosprop_5qi5_arp2_100
      HTTP2DEGRADESW: INHERIT
      EVENTCHARGEFLAG: DISABLE
      EVENTCHGPOINT: RESPONSE
      MMSCHARGETYPE: SINGLE
    add_pccpolicygrp_list_1:
    - PCCPOLICYGRPNM: pccfuppolicy_1M
      FUPSESSIONEXC: DISABLE
      TOKENFUNCFLAG: DISABLE
      SIGNALASSOCIATE: ENABLE
      ADCMUTEFLAG: ENABLE
      QOSPROPNAME: qosprop_5qi5_arp2_1
      HTTP2DEGRADESW: INHERIT
      EVENTCHARGEFLAG: DISABLE
      EVENTCHGPOINT: RESPONSE
      MMSCHARGETYPE: SINGLE
    add_rule_list:
    - RULENAME: Predefined1
      POLICYTYPE: PCC
      FILTERINGMODE: FLOWFILTER
      FLOWFILTERNAME: flowfliter_service_100M
      PRIORITY: '10'
      POLICYNAME: pccfuppolicy_100M
    set_refreshsrv_list:
    - REFRESHTYPE: ALL
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 登录UDG CSP OM Portal，进入“MML命令行-UDG”窗口。

### 2 配置过滤器。

#### 2.1 //用户从国内接入网络时，即PCF下发预定义规则“Predefined1”场景。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_filter_list的变量区（command: ADD FILTER） -#}
<!-- MISSING_MACRO: command=ADD FILTER list_name=add_filter_list step_id=2.1 -->
```

#### 2.2 //用户从国外（漫游区）的位置区域接入网络时，即PCF下发预定义规则“Predefined2”场景。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_filter_list_1的变量区（command: ADD FILTER） -#}
<!-- MISSING_MACRO: command=ADD FILTER list_name=add_filter_list_1 step_id=2.2 -->
```

### 3 添加流过滤器并绑定过滤器。

#### 3.1 //用户从国内接入网络时，即PCF下发预定义规则“Predefined1”场景。

```jinja2
{%- if is_scenario_domestic_access -%}
    {%- for item in add_flowfilter_list -%}
        ADD FLOWFILTER:
        {#- --- 必选参数 --- -#}
        FLOWFILTERNAME="{{item.FLOWFILTERNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_fltbindflowf_list的变量区（command: ADD FLTBINDFLOWF） -#}
<!-- MISSING_MACRO: command=ADD FLTBINDFLOWF list_name=add_fltbindflowf_list step_id=3.1 -->
```

#### 3.2 //用户从国外（漫游区）的位置区域接入网络时，即PCF下发预定义规则“Predefined2”场景。

```jinja2
{%- if is_scenario_roaming_access -%}
    {%- for item in add_flowfilter_list_1 -%}
        ADD FLOWFILTER:
        {#- --- 必选参数 --- -#}
        FLOWFILTERNAME="{{item.FLOWFILTERNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_fltbindflowf_list_1的变量区（command: ADD FLTBINDFLOWF） -#}
<!-- MISSING_MACRO: command=ADD FLTBINDFLOWF list_name=add_fltbindflowf_list_1 step_id=3.2 -->
```

### 4 配置使用量上报属性。

### 此处的配置须与SMF侧配置保持严格一致。

#### 4.1 //配置QoS URR

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

### 5 配置QoS参数。

### 该步骤为预定义规则（组）场景下的可选配置。只有在需要对用户进行带宽控制或建立专有QoS Flow时，才需配置。须配置配额耗尽前、耗尽后两种场景的带宽控制策略。

#### 5.1 //用户从国内接入网络时，即PCF下发预定义规则predefined1场景，此处5QI/ARP取值参考SMF（UNC）侧业务设计规划分别取5和2。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_qosprop_list的变量区（command: ADD QOSPROP） -#}
<!-- MISSING_MACRO: command=ADD QOSPROP list_name=add_qosprop_list step_id=5.1 -->
```

#### 5.2 //用户从国外（漫游区）的地方接入网络时，即PCF下发预定义规则predefined2场景，此处5QI/ARP取值参考SMF（UNC）侧业务设计规划分别取5和2。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_qosprop_list_1的变量区（command: ADD QOSPROP） -#}
<!-- MISSING_MACRO: command=ADD QOSPROP list_name=add_qosprop_list_1 step_id=5.2 -->
```

### 6 配置PCC策略组。

### 该步骤为预定义规则（组）场景下的必选配置。配置PCC策略组的目的是用于关联QoS URR策略。此处“URRGROUPNAME”参数使用ADD URRGROUP定义的“URRGROUPNAME”。

#### 6.1 //用户从国内接入网络时，即PCF下发预定义规则predefined1场景。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_pccpolicygrp_list的变量区（command: ADD PCCPOLICYGRP） -#}
<!-- MISSING_MACRO: command=ADD PCCPOLICYGRP list_name=add_pccpolicygrp_list step_id=6.1 -->
```

#### 6.2 //用户从国外（漫游区）的地方接入网络时，即PCF下发预定义规则predefined2场景。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_pccpolicygrp_list_1的变量区（command: ADD PCCPOLICYGRP） -#}
<!-- MISSING_MACRO: command=ADD PCCPOLICYGRP list_name=add_pccpolicygrp_list_1 step_id=6.2 -->
```

### 7 配置预定义规则。

### 该步骤为预定义规则（组）场景下的必选配置。主要用于关联PCC策略组。此处预定义规则名称、数量都须与PCF侧定义的保持一致。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_rule_list的变量区（command: ADD RULE） -#}
<!-- MISSING_MACRO: command=ADD RULE list_name=add_rule_list step_id=7 -->
```

### 8 将新配置的Filter置为生效。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_refreshsrv_list的变量区（command: SET REFRESHSRV） -#}
<!-- MISSING_MACRO: command=SET REFRESHSRV list_name=set_refreshsrv_list step_id=8 -->
```


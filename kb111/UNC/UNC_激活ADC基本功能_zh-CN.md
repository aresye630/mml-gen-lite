---
id: ''
name: 激活ADC基本功能
ne_type: UNC
type: feature
description: PCRF/PCF需要感知到应用数据流（L7），并为应用数据流提供QoS保障时，需要在UNC上激活ADC基本功能。  PGW-U/UPF检测应用并通过UNC上报给PCRF/PCF。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","智能PCC解决方案","WSFD-109102 ADC基本功能","激活ADC基本功能"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
PCRF/PCF需要感知到应用数据流（L7），并为应用数据流提供QoS保障时，需要在UNC上激活ADC基本功能。PGW-U/UPF检测应用并通过UNC上报给PCRF/PCF。

## 必备事项
前提条件

* 请仔细阅读WSFD-109102 ADC基本功能。
* 完成加载License（如果有需求，请联系华为技术支持工程师）。
* 完成激活PCC基本功能。
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
    add_flowfilter_list:
      type: items
      properties:
        FLOWFILTERNAME:
          name: '流过滤器名称'
          type: string
          maxLength: 63
          required: true
          description: '不同流过滤器之间，该参数不能重复。  GGSN-C/PGW-C/SMF、PGW-U/UPF、PCRF/PCF三个网元上的该参数必须一致，否则无法正常上报。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_adcpara_list:
      type: items
      properties:
        FLOWFILTERNAME:
          name: '流过滤器名称'
          type: string
          maxLength: 63
          required: true
          description: '使用**ADD FLOWFILTER**命令定义的流过滤器名称。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        FLOWINFORPT:
          name: '流信息上报开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: 'PCRF/PCF需要获取流信息时，设置为ENABLE。默认取值是DISABLE。'
          data_source: '本端规划'
          pattern: ''
          default: DISABLE
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
        FLOWFILTERNAME:
          name: '流过滤器名称'
          type: string
          maxLength: 63
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        POLICYNAME:
          name: '策略名称'
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
          description: '配置GGSN-C/PGW-C/SMF上的UserProfile。'
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
          description: ''
          data_source: ''
          pattern: ''
          default: ALL
    add_rulebinding_list:
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
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV2BADCF01'
      SWITCH: ENABLE
    add_flowfilter_list:
    - FLOWFILTERNAME: 'flowfilter_ADC01'
    add_adcpara_list:
    - FLOWFILTERNAME: 'flowfilter_ADC01'
      FLOWINFORPT: ENABLE
    add_rule_list:
    - RULENAME: 'rule_test'
      POLICYTYPE: ADC
      FLOWFILTERNAME: ''
      POLICYNAME: ''
      PROTODESCDL: ''
      PROTODESCUL: ''
      RULERANGE: ALL
    add_userprofile_list:
    - USERPROFILENAME: 'up_test'
      UPTYPE: PCC
      PROFILERANGE: ALL
    add_rulebinding_list:
    - USERPROFILENAME: 'up_test'
      RULENAME: 'rule_test'
```

## 3 命令模板定义
<!-- @mml:block=commands -->

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

### 2 PCRF/PCF要下发应用Start和Stop的两个Event Trigger，当PCRF/PCF通过动态规则下发appid时，请执行本步骤。

#### 2.1 配置ADC业务使用的appid。

```jinja2
{%- if is_scenario_dynamic_rule -%}
    {%- for item in add_flowfilter_list -%}
        ADD FLOWFILTER:
        {#- --- 必选参数 --- -#}
        FLOWFILTERNAME="{{item.FLOWFILTERNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 2.2 配置ADC参数。

```jinja2
{%- if is_scenario_dynamic_rule -%}
    {%- for item in add_adcpara_list -%}
        ADD ADCPARA:
        {#- --- 必选参数 --- -#}
        FLOWFILTERNAME="{{item.FLOWFILTERNAME}}",
        {#- --- 可选参数 --- -#}
        {%- if item.FLOWINFORPT is not none -%}
            FLOWINFORPT={{item.FLOWINFORPT}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 3 PCRF/PCF要下发应用Start和Stop的两个Event Trigger，当PCRF/PCF不通过动态规则下发appid时，请执行本步骤。

#### 3.1 **可选：**配置SMF上的本地rule。

```jinja2
{%- if is_optional_local_rule and is_scenario_predefined_rule -%}
    {%- for item in add_rule_list -%}
        ADD RULE:
        {#- --- 必选参数 --- -#}
        RULENAME="{{item.RULENAME}}",
        POLICYTYPE={{item.POLICYTYPE}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：POLICYTYPE=ULCL 时必选 --- -#}
        {%- if item.POLICYTYPE == 'ULCL' -%}
            FLOWFILTERNAME="{{item.FLOWFILTERNAME}}",
        {%- endif -%}
        {#- --- 条件必选：POLICYTYPE=PCC/ULCL/QOS 时必选 --- -#}
        {%- if item.POLICYTYPE in ['PCC', 'ULCL', 'QOS'] -%}
            POLICYNAME="{{item.POLICYNAME}}",
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
{%- endif -%}
```

#### 3.2 **可选：**配置SMF上的UserProfile，将本地rule绑定到UserProfile上。

##### 3.2.1 配置UserProfile。

```jinja2
{%- if is_optional_userprofile and is_scenario_predefined_rule -%}
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

##### 3.2.2 将rule绑定到UserProfile。

```jinja2
{%- if is_optional_userprofile and is_scenario_predefined_rule -%}
    {%- for item in add_rulebinding_list -%}
        ADD RULEBINDING:
        {#- --- 必选参数 --- -#}
        USERPROFILENAME="{{item.USERPROFILENAME}}",
        RULENAME="{{item.RULENAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```


---
id: ''
name: SMF侧业务配置
ne_type: UNC
type: feature
description: PCF通过ADC功能感知到特定视频应用数据流，并为该特定应用数据流提供QoS保证等时，需要在SMF上配置ADC基本功能。  UPF检测应用数据流（应用数据流通过L3/4、L7或L3/4+L7识别）时，通过SMF上报给PCF。
risk_level: ''
doc_source: ["网络部署","业务专题","5G PCC之SM策略解决方案","典型业务场景E2E方案设计","基于业务类别的带宽差异化控制方案设计（ADC）","E2E业务配置","SMF侧业务配置"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
PCF通过ADC功能感知到特定视频应用数据流，并为该特定应用数据流提供QoS保证等时，需要在SMF上配置ADC基本功能。UPF检测应用数据流（应用数据流通过L3/4、L7或L3/4+L7识别）时，通过SMF上报给PCF。

## 必备事项
前提条件

* 请仔细阅读SMF（UNC）特性之《WSFD-109102 ADC基本功能》。
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
        ROAMPCCSWITCH:
          name: '漫游用户动态PCC功能'
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
          name: '拜访用户动态PCC功能'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        N7FAILOVERSW:
          name: 'N7 Failover功能开关'
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
    set_licenseswitch_list_1:
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
          description: '不同流过滤器之间，该参数不能重复。  SMF、UPF、PCF三个网元上的该参数必须一致，否则无法正常上报。'
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
          description: 'PCF需要获取流信息时，设置为“ENABLE”。默认取值是“DISABLE”。'
          data_source: '本端规划'
          pattern: ''
          default: DISABLE
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV3W9SPCC11'
      SWITCH: ENABLE
    set_pccfunc_list:
    - HOMEPCCSWITCH: ENABLE
      ROAMPCCSWITCH: ENABLE
      VISITPCCSWITCH: ENABLE
      N7FAILOVERSW: ENABLE
    set_apnpccfunc_list:
    - APN: 'cmnet'
      HOMEPCCSWITCH: ENABLE
      ROAMPCCSWITCH: ENABLE
      VISITPCCSWITCH: ENABLE
    set_licenseswitch_list_1:
    - LICITEM: 'LKV2BADCF01'
      SWITCH: ENABLE
    add_flowfilter_list:
    - FLOWFILTERNAME: 'flow_ADC'
    add_adcpara_list:
    - FLOWFILTERNAME: 'flow_ADC'
      FLOWINFORPT: ENABLE
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 打开PCC基本功能的License配置开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

### 2 使能SMF的全局缺省的PCC开关。

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
    {%- if item.N7FAILOVERSW is not none -%}
        N7FAILOVERSW={{item.N7FAILOVERSW}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 使能APN PCC开关。（条件可选）

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

### 4 打开ADC基本功能的License配置开关。

```jinja2
{%- for item in set_licenseswitch_list_1 -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

### 5 PCF通过动态规则下发appId时，请执行本步骤。

#### 5.1 配置ADC业务使用的appId。

```jinja2
{%- for item in add_flowfilter_list -%}
    ADD FLOWFILTER:
    {#- --- 必选参数 --- -#}
    FLOWFILTERNAME="{{item.FLOWFILTERNAME}}",
    ;
{%- endfor -%}
```

#### 5.2 配置ADC参数。

```jinja2
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
```

#### 存在多个appId时，请多次执行5。


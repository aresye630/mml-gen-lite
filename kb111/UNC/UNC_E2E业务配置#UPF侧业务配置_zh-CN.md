---
id: ''
name: UPF侧业务配置
ne_type: UNC
type: feature
description: PCF通过ADC功能感知到特定应用数据流，并为该特定应用数据流提供QoS保证等时，需要在UPF上配置ADC基本功能。  UPF检测应用数据流（应用数据流通过L3/4、L7或L3/4+L7识别）开始、结束时，通过SMF上报给PCF。
risk_level: ''
doc_source: ["网络部署","业务专题","5G PCC之SM策略解决方案","典型业务场景E2E方案设计","基于业务类别的带宽差异化控制方案设计（ADC）","E2E业务配置","UPF侧业务配置"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
PCF通过ADC功能感知到特定应用数据流，并为该特定应用数据流提供QoS保证等时，需要在UPF上配置ADC基本功能。UPF检测应用数据流（应用数据流通过L3/4、L7或L3/4+L7识别）开始、结束时，通过SMF上报给PCF。

## 必备事项
前提条件

前提条件

* 请仔细阅读UPF特性之《GWFD-020357 增强的ADC基本功能》。
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
    add_filter_list:
      type: items
      properties:
        FILTERNAME:
          name: '过滤器名称'
          type: string
          required: false
          description: '不同过滤器之间，该参数不能重复。三四层过滤条件。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        L34PROTTYPE:
          name: '三四层IPv4协议输入类型'
          type: string
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        L34PROTOCOL:
          name: 'L34PROTOCOL'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SVRIPMODE:
          name: '服务器IP地址配置模式'
          type: string
          required: false
          description: '-'
          data_source: '根据用户实际业务类型进行规划'
          pattern: ''
          default: ''
        SVRIP:
          name: '服务器IP地址'
          type: string
          required: false
          description: '特定视频应用对应的服务器IP地址。在测试场景，终端侧一般可通过FTP软件等起FTP服务的方式生成服务器IP地址。'
          data_source: '根据用户实际业务类型进行规划'
          pattern: ''
          default: ''
        SVRIPMASKTYPE:
          name: 'SVRIPMASKTYPE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SVRIPMASKLEN:
          name: 'SVRIPMASKLEN'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MSSTARTPORT:
          name: 'MSSTARTPORT'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MSENDPORT:
          name: 'MSENDPORT'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SVRSTARTPORT:
          name: 'SVRSTARTPORT'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SVRENDPORT:
          name: 'SVRENDPORT'
          type: string
          required: false
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
          description: '不同流过滤器之间，该参数不能重复。  PCF下发动态规则携带appId时，SMF、UPF、PCF三个网元上的该参数必须一致，否则无法正常上报。  PCF通过预定义规则下发APP\_STA和APP\_STO事件时，FlowFilter与ADC功能无关。'
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
    add_l7filter_list:
      type: items
      properties:
        L7FILTERNAME:
          name: '七层过滤器名称'
          type: string
          required: false
          description: '不同的七层过滤器，其名称不能相同。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SUBL7FLTNAME:
          name: '子七层过滤器名称'
          type: string
          required: false
          description: '同一个七层过滤器包含的多个子七层过滤器名称不能相同。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        URL:
          name: 'URL'
          type: string
          required: false
          description: '根据应用服务器的URL规划。  采用基于URL时，需要规划；仅采用基于HTTP协议时，不需要规划该数据。'
          data_source: '与对端协商'
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
          description: '不同流过滤器之间，该参数不能重复。  PCF下发动态规则携带appId时，SMF、UPF、PCF三个网元上的该参数必须一致，否则无法正常上报。  PCF通过预定义规则下发APP\_STA和APP\_STO事件时，FlowFilter与ADC功能无关。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_protbindflowf_list:
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
        PROTOCOLNAME:
          name: '协议名称'
          type: string
          required: false
          description: '使用样例值。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        L7FILTERNAME:
          name: '七层过滤器名字'
          type: string
          required: false
          description: '使用**ADD L7FILTER**命令定义的七层过滤器名称。  采用基于URL时，需要规划；仅采用基于HTTP协议时不需要规划。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    set_refreshsrv_list_1:
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
    set_licenseswitch_list:
    - LICITEM: 'LKV3G5PCCB01'
      SWITCH: ENABLE
    set_licenseswitch_list_1:
    - LICITEM: 'LKV3G5ADCF01'
      SWITCH: ENABLE
    add_filter_list:
    - FILTERNAME: filter_test1
      L34PROTTYPE: STRING
      L34PROTOCOL: ANY
      SVRIPMODE: IP
      SVRIP: 10.27.3.56
      SVRIPMASKTYPE: LENGTHTYPE
      SVRIPMASKLEN: '32'
      MSSTARTPORT: '0'
      MSENDPORT: '65535'
      SVRSTARTPORT: '0'
      SVRENDPORT: '65535'
    add_flowfilter_list:
    - FLOWFILTERNAME: 'flow_ADC'
    add_fltbindflowf_list:
    - FLOWFILTERNAME: flow_ADC
      FILTERNAME: filter_test1
    set_refreshsrv_list:
    - REFRESHTYPE: ALL
    add_l7filter_list:
    - L7FILTERNAME: l7filter_test_01
      SUBL7FLTNAME: sl7_test_1
      URL: www.huawei.com
    add_flowfilter_list_1:
    - FLOWFILTERNAME: 'flow_ADC'
    add_protbindflowf_list:
    - FLOWFILTERNAME: flow_ADC
      PROTOCOLNAME: http
      L7FILTERNAME: l7filter_test_01
    set_refreshsrv_list_1:
    - REFRESHTYPE: ALL
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

### 2 打开ADC基本功能的License配置开关。

```jinja2
{%- for item in set_licenseswitch_list_1 -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

### 3 如果采用了L3/4层过滤则须配置ADC业务使用的三四层过滤条件。

#### 3.1 配置ADC业务使用的三四层过滤条件。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_filter_list的变量区（command: ADD FILTER） -#}
<!-- MISSING_MACRO: command=ADD FILTER list_name=add_filter_list step_id=3.1 -->
```

#### 3.2 配置流分类器。

```jinja2
{%- if is_scenario_l34_filter -%}
    {%- for item in add_flowfilter_list -%}
        ADD FLOWFILTER:
        {#- --- 必选参数 --- -#}
        FLOWFILTERNAME="{{item.FLOWFILTERNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

#### PCF通过动态规则下发appId时，动态规则中携带的appId映射到本地配置的FlowFilter。

#### 3.3 绑定三四层过滤信息。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_fltbindflowf_list的变量区（command: ADD FLTBINDFLOWF） -#}
<!-- MISSING_MACRO: command=ADD FLTBINDFLOWF list_name=add_fltbindflowf_list step_id=3.3 -->
```

#### 3.4 将新配置的Filter置为生效。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_refreshsrv_list的变量区（command: SET REFRESHSRV） -#}
<!-- MISSING_MACRO: command=SET REFRESHSRV list_name=set_refreshsrv_list step_id=3.4 -->
```

#### 修改完流信息后需执行**SET REFRESHSRV**命令刷新流配置才能立即生效。

### 4 如果采用了L7层过滤配置ADC业务使用的七层过滤条件。

#### 4.1 配置七层过滤器。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_l7filter_list的变量区（command: ADD L7FILTER） -#}
<!-- MISSING_MACRO: command=ADD L7FILTER list_name=add_l7filter_list step_id=4.1 -->
```

#### 4.2 配置流分类器。

```jinja2
{%- if is_scenario_l7_filter -%}
    {%- for item in add_flowfilter_list_1 -%}
        ADD FLOWFILTER:
        {#- --- 必选参数 --- -#}
        FLOWFILTERNAME="{{item.FLOWFILTERNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 4.3 绑定七层过滤信息。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_protbindflowf_list的变量区（command: ADD PROTBINDFLOWF） -#}
<!-- MISSING_MACRO: command=ADD PROTBINDFLOWF list_name=add_protbindflowf_list step_id=4.3 -->
```

#### 4.4 将新配置的L7Filter置为生效。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_refreshsrv_list_1的变量区（command: SET REFRESHSRV） -#}
<!-- MISSING_MACRO: command=SET REFRESHSRV list_name=set_refreshsrv_list_1 step_id=4.4 -->
```


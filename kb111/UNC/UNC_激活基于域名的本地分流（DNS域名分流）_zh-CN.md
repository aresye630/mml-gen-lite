---
id: ''
name: 激活基于域名的本地分流（DNS域名分流）
ne_type: UNC
type: feature
description: 部署基于域名的本地分流功能，需要配置七层分流规则。
risk_level: ''
doc_source: ["网络部署","业务专题","5G Core ULCL分流解决方案","分流业务部署","基于PCF静态签约的分流","功能部署","部署基于PCF静态签约的分流（UPF）","激活基于域名的本地分流（DNS域名分流）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
部署基于域名的本地分流功能，需要配置七层分流规则。

## 必备事项
前提条件

* 请仔细阅读分流原理。
* 已完成与周边网元的对接。
* 完成协议识别库和解析库的加载。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    set_colocatedlbo_list:
      type: items
      properties:
        ULCLSWITCH:
          name: 'ULCL功能开关'
          type: string
          required: false
          description: '配置UL CL与PSA1共部署的本地分流功能开关。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_host_list:
      type: items
      properties:
        HOSTNAME:
          name: 'Host配置名称'
          type: string
          required: false
          description: '配置触发分流的Host信息。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        DOMAINVALUE:
          name: '域名'
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
          required: false
          description: '流过滤器。  说明：  flowfilter\_ulcl01用于DNS报文的匹配，flowfilter\_ulcl02用于TCP报文的匹配。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        TETHERDETFLAG:
          name: 'TETHERDETFLAG'
          type: string
          required: false
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
          description: '配置三四层过滤条件。  说明：  匹配DNS报文的过滤条件，三四层协议只能配置为UDP。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        L34PROTTYPE:
          name: '三四层IPv4协议输入类型'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        L34PROTOCOL:
          name: '三四层IPv4协议输入类型'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        SVRSTARTPORT:
          name: '服务器起始端口号'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        SVRENDPORT:
          name: '服务器结束端口号'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        SVRIPMODE:
          name: '服务器IP地址配置模式'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        HOSTNAME:
          name: 'Host配置名称'
          type: string
          required: false
          description: 'Host配置名称已通过**ADD HOST**命令配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_fltbindflowf_list:
      type: items
      properties:
        FLOWFILTERNAME:
          name: '流过滤器名称'
          type: string
          required: false
          description: '流过滤器名称已通过**ADD FLOWFILTER**命令配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        FILTERNAME:
          name: '过滤器名称'
          type: string
          required: false
          description: '过滤器名称已通过**ADD FILTER**命令配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_l7filter_list:
      type: items
      properties:
        L7FILTERNAME:
          name: '七层过滤器名称'
          type: string
          required: false
          description: '匹配DNS报文的过滤条件需要配置七层过滤条件。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SUBL7FLTNAME:
          name: '子七层过滤器名称'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
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
        URL:
          name: 'URL'
          type: string
          required: false
          description: '该参数取值要和**ADD HOST**命令配置的域名保持一致。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_protbindflowf_list:
      type: items
      properties:
        FLOWFILTERNAME:
          name: '流过滤器名称'
          type: string
          required: false
          description: '流过滤器名称已通过**ADD FLOWFILTER**命令配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        PROTOCOLNAME:
          name: '协议名称'
          type: string
          required: false
          description: '匹配DNS报文的过滤条件需要绑定七层协议。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        L7FILTERNAME:
          name: '七层过滤器名字'
          type: string
          required: false
          description: '七层过滤器名字已通过**ADD L7FILTER**命令配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_flowfiltergrp_list:
      type: items
      properties:
        FLWFLTRGRPNAME:
          name: '流过滤器组名称'
          type: string
          required: false
          description: '对应SMF下发的Application ID。'
          data_source: '与对端协商'
          pattern: ''
          default: ''
        FLOWFILTERNAME:
          name: '流过滤器名称'
          type: string
          required: false
          description: '绑定的FlowFilter已通过**ADD FLOWFILTER**命令配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        FLWFLTRLOGICGRP:
          name: '流过滤器逻辑分组'
          type: string
          required: false
          description: '或组内的任何一个流过滤器命中，则执行分流流程。'
          data_source: '本端规划'
          pattern: ''
          default: ''
  examples:
    set_colocatedlbo_list:
    - ULCLSWITCH: ENABLE
    add_host_list:
    - HOSTNAME: host1
      DOMAINVALUE: www.huawei.com
    add_flowfilter_list:
    - FLOWFILTERNAME: flowfilter_ulcl01
      TETHERDETFLAG: NONE
    add_filter_list:
    - FILTERNAME: filter_test01
      L34PROTTYPE: STRING
      L34PROTOCOL: UDP
      SVRSTARTPORT: '53'
      SVRENDPORT: '53'
      SVRIPMODE: HOSTNAME
      HOSTNAME: host1
    add_fltbindflowf_list:
    - FLOWFILTERNAME: flowfilter_ulcl01
      FILTERNAME: filter_test01
    add_l7filter_list:
    - L7FILTERNAME: l7filter-test
      SUBL7FLTNAME: sl7filter-test
      URLTYPE: URL
      URL: www.huawei.com
    add_protbindflowf_list:
    - FLOWFILTERNAME: flowfilter_ulcl01
      PROTOCOLNAME: dns
      L7FILTERNAME: l7filter-test
    add_flowfiltergrp_list:
    - FLWFLTRGRPNAME: flowfiltergrp_ulcl01
      FLOWFILTERNAME: flowfilter_ulcl01
      FLWFLTRLOGICGRP: OR
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 配置UL CL与PSA1共部署的本地分流功能开关。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_colocatedlbo_list的变量区（command: SET COLOCATEDLBO） -#}
<!-- MISSING_MACRO: command=SET COLOCATEDLBO list_name=set_colocatedlbo_list step_id=1 -->
```

### 2 配置Host信息。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_host_list的变量区（command: ADD HOST） -#}
<!-- MISSING_MACRO: command=ADD HOST list_name=add_host_list step_id=2 -->
```

### 3 配置基于域名的本地分流过滤条件。

#### 3.1 配置流过滤器。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_flowfilter_list的变量区（command: ADD FLOWFILTER） -#}
<!-- MISSING_MACRO: command=ADD FLOWFILTER list_name=add_flowfilter_list step_id=3.1 -->
```

#### 3.2 配置三四层过滤条件。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_filter_list的变量区（command: ADD FILTER） -#}
<!-- MISSING_MACRO: command=ADD FILTER list_name=add_filter_list step_id=3.2 -->
```

#### 3.3 绑定三四层过滤条件。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_fltbindflowf_list的变量区（command: ADD FLTBINDFLOWF） -#}
<!-- MISSING_MACRO: command=ADD FLTBINDFLOWF list_name=add_fltbindflowf_list step_id=3.3 -->
```

#### 3.4 配置七层过滤条件。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_l7filter_list的变量区（command: ADD L7FILTER） -#}
<!-- MISSING_MACRO: command=ADD L7FILTER list_name=add_l7filter_list step_id=3.4 -->
```

#### 3.5 绑定七层过滤条件。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_protbindflowf_list的变量区（command: ADD PROTBINDFLOWF） -#}
<!-- MISSING_MACRO: command=ADD PROTBINDFLOWF list_name=add_protbindflowf_list step_id=3.5 -->
```

### 4 配置本地分流流过滤器组。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_flowfiltergrp_list的变量区（command: ADD FLOWFILTERGRP） -#}
<!-- MISSING_MACRO: command=ADD FLOWFILTERGRP list_name=add_flowfiltergrp_list step_id=4 -->
```

### 流过滤器组对应SMF下发的AppID。一个流过滤器组中需要绑定基于域名的本地分流过滤条件，才能实现针对一个AppID的分流功能。

### 匹配中流过滤器组后，根据ApplD检索到分流PDR，然后按照PDR中的转发规则FAR、QoS规则QER执行策略动作。


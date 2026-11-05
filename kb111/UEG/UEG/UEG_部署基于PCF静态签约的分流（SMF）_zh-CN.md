---
id: ''
name: 部署基于PCF静态签约的分流（SMF）
ne_type: UEG
type: feature
description: 本章节用于指导部署基于PCF静态签约的分流方案，主要包括分流策略以及DNAI等相关配置。
tags: []
risk_level: ''
doc_source: ["业务配置","公共业务","MEC ULCL专题（公共）","分流业务部署","基于PCF静态签约的分流","功能部署","部署基于PCF静态签约的分流（SMF）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
本章节用于指导部署基于PCF静态签约的分流方案，主要包括分流策略以及DNAI等相关配置。

## 必备事项
前提条件

* 操作人员已了解本功能的原理。
* 已完成和分流UPF的对接配置。
* 完成PCC相关基本功能配置。
* 已完成加载License，可以通过**DSP LICENSE**命令查询确认，如果本特性的License在查询列表中可见，即可认为本特性License已加载成功。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    add_rule_list:
      type: items
      properties:
        RULENAME:
          name: '规则名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '配置规则  规则需要和PCF上配置的策略保持一致。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        POLICYTYPE:
          name: '策略类型'
          type: string
          enum:
          - ADC
          - BWM
          - FIREWALL
          - HEADEN
          - IPREDIR
          - LBO
          - PCC
          - QOS
          - REMARK_FPI
          - SMARTREDIRECT
          - SRV_TRIGGER
          - TRAFFICCLASS
          - WEBPROXY
          - WORKER
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        POLICYNAME:
          name: '策略名称'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        FLOWFILTERNAME:
          name: '流过滤器名称'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: ''
          data_source: '与对端协商'
          pattern: ''
          default: ''
        FILTERINGMODE:
          name: '流过滤器或流过滤器组选择'
          type: string
          enum:
          - FLOWFILTER
          - FLOWFILTERGRP
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_userprofile_list:
      type: items
      properties:
        USERPROFILENAME:
          name: '用户模板名称'
          type: string
          required: false
          description: '配置用户属性模板  “用户模板类型”和“策略类型”均配置为ULCL'
          data_source: '全网规划'
          pattern: ''
          default: ''
        UPTYPE:
          name: '用户模板类型'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_rulebinding_list:
      type: items
      properties:
        USERPROFILENAME:
          name: '用户模板名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        RULENAME:
          name: '规则名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: ''
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
          - HEADEN
          - IPREDIR
          - LBO
          - PCC
          - QOS
          - REMARK_FPI
          - SMARTREDIRECT
          - SRV_TRIGGER
          - TRAFFICCLASS
          - WEBPROXY
          - WORKER
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
          minLength: 0
          maxLength: 63
          required: true
          description: '配置UL CL分流策略  “流过滤器名称”需要和UPF侧保持一致。  这里的“数据网络访问标识符”需要和与分流UPF对接配置中ADD PNFDNAI中的DNAI在数据规划上保持一致。'
          data_source: '与对端协商'
          pattern: ''
          default: ''
    add_ulclprop_list:
      type: items
      properties:
        ULCLPROPNAME:
          name: 'ULCL属性名称'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        DNAI:
          name: '数据网络访问标识符'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_dnarea_list:
      type: items
      properties:
        AREANAME:
          name: 'DNAI服务区域名称'
          type: string
          minLength: 1
          maxLength: 255
          required: true
          description: '配置DNAI对应的服务区域  “数据网络访问标识符”需要和**ADD ULCLPROP**中的“数据网络访问标识符”保持一致。  DNAI是用于SMF选择辅锚点UPF用的，需要确保本处配置的区域范围在辅锚点UPF的覆盖范围内。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        AREATYPE:
          name: 'DNAI服务区域类型'
          type: string
          enum:
          - N2TAI
          - N2CID
          - S1TAI
          - S1CID
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_dnareabindn2tai_list:
      type: items
      properties:
        AREANAME:
          name: 'DNAI服务区域名称'
          type: string
          minLength: 1
          maxLength: 255
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        N2BEGINTAI:
          name: 'DNAI服务区名称支持5GTAI范围的起始值'
          type: string
          minLength: 11
          maxLength: 12
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        N2ENDTAI:
          name: 'DNAI服务区名称支持5GTAI范围的结束值'
          type: string
          minLength: 11
          maxLength: 12
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_dnaibinddnarea_list:
      type: items
      properties:
        DNAI:
          name: '数据网络访问标识'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        AREANAME:
          name: 'DNAI服务区域名称'
          type: string
          minLength: 1
          maxLength: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_smffunc_list:
      type: items
      properties:
        IPV6LOCALUP:
          name: 'IPv6本地UP分流策略'
          type: string
          enum:
          - BpPrefer
          - UlClPrefer
          required: false
          description: '配置IPv6会话场景下的分流策略  如果是IPv6会话，系统默认选择Bp分流模式，如果是UL CL分流需要修改配置。'
          data_source: '本端规划'
          pattern: ''
          default: ''
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
    set_apnauthattr_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '配置当用户二次鉴权失败后，仍可以访问公网。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        AAAREJECTCTRL:
          name: '控制AAA鉴权服务器回复Access Reject时是否允许用户继续激活'
          type: string
          enum:
          - DEACTIVE
          - CONTINUE
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
  examples:
    add_rule_list:
    - RULENAME: 'testrule'
      POLICYTYPE: ULCL
      POLICYNAME: 'testulclpropname'
      FLOWFILTERNAME: 'ulcl'
      FILTERINGMODE: ''
    add_userprofile_list:
    - USERPROFILENAME: testuserprofilename
      UPTYPE: ULCL
    add_rulebinding_list:
    - USERPROFILENAME: 'testuserprofilename'
      RULENAME: 'testrule'
      POLICYTYPE: ULCL
    add_flowfilter_list:
    - FLOWFILTERNAME: 'ulcl'
    add_ulclprop_list:
    - ULCLPROPNAME: 'testulclpropname'
      DNAI: 'testdnai'
    add_dnarea_list:
    - AREANAME: 'DNAREA1'
      AREATYPE: N2TAI
    add_dnareabindn2tai_list:
    - AREANAME: 'DNAREA1'
      N2BEGINTAI: '46001000001'
      N2ENDTAI: '46001000006'
    add_dnaibinddnarea_list:
    - DNAI: 'testdnai'
      AREANAME: 'DNAREA1'
    set_smffunc_list:
    - IPV6LOCALUP: UlClPrefer
    set_licenseswitch_list:
    - LICITEM: 'LKV2PCLBO01'
      SWITCH: ENABLE
    set_apnauthattr_list:
    - APN: 'cmnet'
      AAAREJECTCTRL: CONTINUE
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 //配置规则。

```jinja2
{%- for item in add_rule_list -%}
    ADD RULE:
    {#- --- 必选参数 --- -#}
    RULENAME="{{item.RULENAME}}",
    POLICYTYPE={{item.POLICYTYPE}},
    FILTERINGMODE={{item.FILTERINGMODE}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：POLICYTYPE=PCC/BWM/HEADEN/SMARTREDIRECT/TRAFFICCLASS/FIREWALL/QOS/WEBPROXY 时必选 --- -#}
    {%- if item.POLICYTYPE in ['PCC', 'BWM', 'HEADEN', 'SMARTREDIRECT', 'TRAFFICCLASS', 'FIREWALL', 'QOS', 'WEBPROXY'] -%}
        POLICYNAME="{{item.POLICYNAME}}",
    {%- endif -%}
    {#- --- 条件必选：FILTERINGMODE=FLOWFILTER 时必选 --- -#}
    {%- if item.FILTERINGMODE == 'FLOWFILTER' -%}
        FLOWFILTERNAME="{{item.FLOWFILTERNAME}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 2 //配置用户属性模板。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_userprofile_list的变量区（command: ADD USERPROFILE） -#}
<!-- MISSING_MACRO: command=ADD USERPROFILE list_name=add_userprofile_list step_id=2 -->
```

```jinja2
{%- for item in add_rulebinding_list -%}
    ADD RULEBINDING:
    {#- --- 必选参数 --- -#}
    USERPROFILENAME="{{item.USERPROFILENAME}}",
    RULENAME="{{item.RULENAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.POLICYTYPE is not none -%}
        POLICYTYPE={{item.POLICYTYPE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 //配置UL CL分流策略。

```jinja2
{%- for item in add_flowfilter_list -%}
    ADD FLOWFILTER:
    {#- --- 必选参数 --- -#}
    FLOWFILTERNAME="{{item.FLOWFILTERNAME}}",
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_ulclprop_list -%}
    ADD ULCLPROP:
    {#- --- 必选参数 --- -#}
    ULCLPROPNAME="{{item.ULCLPROPNAME}}",
    DNAI="{{item.DNAI}}",
    ;
{%- endfor -%}
```

### 4 //配置DNAI对应的服务区域。

```jinja2
{%- for item in add_dnarea_list -%}
    ADD DNAREA:
    {#- --- 必选参数 --- -#}
    AREANAME="{{item.AREANAME}}",
    AREATYPE={{item.AREATYPE}},
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_dnareabindn2tai_list -%}
    ADD DNAREABINDN2TAI:
    {#- --- 必选参数 --- -#}
    AREANAME="{{item.AREANAME}}",
    N2BEGINTAI="{{item.N2BEGINTAI}}",
    N2ENDTAI="{{item.N2ENDTAI}}",
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_dnaibinddnarea_list -%}
    ADD DNAIBINDDNAREA:
    {#- --- 必选参数 --- -#}
    DNAI="{{item.DNAI}}",
    AREANAME="{{item.AREANAME}}",
    ;
{%- endfor -%}
```

### 5 //配置IPv6会话场景下的分流策略。

```jinja2
{%- for item in set_smffunc_list -%}
    SET SMFFUNC:
    {#- --- 可选参数 --- -#}
    {%- if item.IPV6LOCALUP is not none -%}
        IPV6LOCALUP={{item.IPV6LOCALUP}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 6 //打开本功能的License配置开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

### 7 //配置用户二次鉴权失败后，仍可以访问公网。

```jinja2
{%- for item in set_apnauthattr_list -%}
    SET APNAUTHATTR:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    {#- --- 可选参数 --- -#}
    {%- if item.AAAREJECTCTRL is not none -%}
        AAAREJECTCTRL={{item.AAAREJECTCTRL}},
    {%- endif -%}
    ;
{%- endfor -%}
```


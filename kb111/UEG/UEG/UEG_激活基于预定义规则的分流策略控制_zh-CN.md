---
id: ''
name: 激活基于预定义规则的分流策略控制
ne_type: UEG
type: feature
description: 本操作指导介绍在部署基于预定义规则的分流策略控制特性的操作过程。  3GPP针对于5G用户面的数据分流定义了UL CL(Uplink Classifier)功能，通过上行分流器（即UL CL UPF）实现根据用户业务流特征将访问本地网络的数据分流到本地DN，将访问Internet数据分流到公网，从而实现对用户本地业务数据的分流控制。  当UE会话激活或位置发生变化时，SMF基于用户的DNN、位置区以及DNAI（Data Network Access Identifier）等信息判定是否需要将用户数据分流到本地DN，如需分流则为用户选择UL CL UPF和辅锚点UPF，将UL CL UPF和辅锚点UPF插入当前的会话中并对UL CL UPF下发相应的分流规则来实现对用户本地数据的分流控制。  DNAI（DN Access Identifier）是3GPP定义用于标识DN网络接入点。DNN表示DN的名称，DNAI则表示DN的具体网络接入点，带有一定的物理属性。例如网络中规划了一个DN，其DNN为abc，该DN有A城和B城两个接入点，则A、B城对应的DNAI可以命名为abc.A和abc.B。在UL CL分流场景下，DNAI则用于标识边缘侧的PDU会话锚点，即辅锚点UPF。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝S","MEC 特性指南（风筝S）","UNC特性指南","WSFD-108002 基于预定义规则的分流策略控制","激活基于预定义规则的分流策略控制"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
本操作指导介绍在部署基于预定义规则的分流策略控制特性的操作过程。3GPP针对于5G用户面的数据分流定义了UL CL(Uplink Classifier)功能，通过上行分流器（即UL CL UPF）实现根据用户业务流特征将访问本地网络的数据分流到本地DN，将访问Internet数据分流到公网，从而实现对用户本地业务数据的分流控制。当UE会话激活或位置发生变化时，SMF基于用户的DNN、位置区以及DNAI（Data Network Access Identifier）等信息判定是否需要将用户数据分流到本地DN，如需分流则为用户选择UL CL UPF和辅锚点UPF，将UL CL UPF和辅锚点UPF插入当前的会话中并对UL CL UPF下发相应的分流规则来实现对用户本地数据的分流控制。DNAI（DN Access Identifier）是3GPP定义用于标识DN网络接入点。DNN表示DN的名称，DNAI则表示DN的具体网络接入点，带有一定的物理属性。例如网络中规划了一个DN，其DNN为abc，该DN有A城和B城两个接入点，则A、B城对应的DNAI可以命名为abc.A和abc.B。在UL CL分流场景下，DNAI则用于标识边缘侧的PDU会话锚点，即辅锚点UPF。

## 必备事项
前提条件

* 请仔细阅读WSFD-108002 基于预定义规则的分流策略控制特性概述特性原理概述。
* 已完成WSFD-109101 PCC基本功能和WSFD-107010 UPF选择的部署。
* 以下配置过程是基于SMF和**主锚点UPF**以及**“ULCL UPF+辅锚点UPF”**的对接配置已完成情况下的操作。SMF和主锚点UPF的对接配置参见N4接口配置，SMF和**“ULCL UPF+辅锚点UPF”**的对接配置参见配置SMF和“UL CL UPF+辅锚点UPF”对接。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    add_ulclprop_list:
      type: items
      properties:
        ULCLPROPNAME:
          name: 'ULCL属性名称'
          type: string
          maxLength: 63
          required: true
          description: '配置UL CL属性和DNAI的映射关系'
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
          description: '配置DNAI对应的服务区域'
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
          description: '配置DNAI服务区名称绑定的5G TAI范围'
          data_source: '全网规划'
          pattern: ''
          default: ''
        N2BEGINTAI:
          name: 'DNAI服务区名称支持5G TAI范围的起始值'
          type: string
          minLength: 11
          maxLength: 12
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        N2ENDTAI:
          name: 'DNAI服务区名称支持5G TAI范围的结束值'
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
          description: '配置DNAI支持的服务区域名称'
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
    add_flowfilter_list:
      type: items
      properties:
        FLOWFILTERNAME:
          name: '流过滤器名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '配置App ID'
          data_source: '与对端协商'
          pattern: ''
          default: ''
    add_rule_list:
      type: items
      properties:
        RULENAME:
          name: '规则名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '配置UL CL分流rule以及和App ID的绑定关系。'
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
          description: '配置UL CL属性的User Profile'
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
          description: '将UL CL属性的User Profile和rule进行绑定'
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
    add_apn_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          required: false
          description: '配置使能SMF上的ULCL功能'
          data_source: '全网规划'
          pattern: ''
          default: ''
        ULCLFUNC:
          name: 'ULCL功能开关'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_usrprofgroup_list:
      type: items
      properties:
        USERPROFGNAME:
          name: '用户模板组名称'
          type: string
          maxLength: 63
          required: true
          description: '配置基于DNN UL CL分流的用户模板组，并将DNN绑定至该模板组'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_upbindupg_list:
      type: items
      properties:
        USERPROFGNAME:
          name: '用户模板组名称'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        UPBINDTYPE:
          name: '用户模板绑定类型'
          type: string
          enum:
          - DEFAULT
          - SPECIFIC
          - ULCL
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        USERPROFILENAME:
          name: '用户模板名称'
          type: string
          maxLength: 63
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_apnusrprofg_list:
      type: items
      properties:
        APN:
          name: 'APN'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        USERPROFGNAME:
          name: '用户模板组名称'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: '本端规划'
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
          description: '配置IPv6会话场景下的分流策略。  如果是IPv6会话，系统默认选择Bp分流模式，如果是UL CL分流需要修改配置。'
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
  examples:
    add_ulclprop_list:
    - ULCLPROPNAME: 'testulclpropname'
      DNAI: 'testdnai'
    add_dnarea_list:
    - AREANAME: 'DNAREA1'
      AREATYPE: N2TAI
    add_dnareabindn2tai_list:
    - AREANAME: 'DNAREA1'
      N2BEGINTAI: '46001000001'
      N2ENDTAI: '46001123456'
    add_dnaibinddnarea_list:
    - DNAI: 'testdnai'
      AREANAME: 'DNAREA1'
    add_flowfilter_list:
    - FLOWFILTERNAME: 'ulcl'
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
    add_apn_list:
    - APN: Huawei.com
      ULCLFUNC: ENABLE
    add_usrprofgroup_list:
    - USERPROFGNAME: 'ulcl_test'
    add_upbindupg_list:
    - USERPROFGNAME: 'ulcl_test'
      UPBINDTYPE: ULCL
      USERPROFILENAME: 'testuserprofilename'
    add_apnusrprofg_list:
    - APN: 'Huawei.com'
      USERPROFGNAME: 'ulcl_test'
    set_smffunc_list:
    - IPV6LOCALUP: UlClPrefer
    set_licenseswitch_list:
    - LICITEM: 'LKV2PCLBO01'
      SWITCH: ENABLE
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 进入“MML命令行-UEG”窗口。

### 2 配置指定APN的ULCL策略。

#### 2.1 配置ULCL属性名称和DNAI的绑定关系。

```jinja2
{%- for item in add_ulclprop_list -%}
    ADD ULCLPROP:
    {#- --- 必选参数 --- -#}
    ULCLPROPNAME="{{item.ULCLPROPNAME}}",
    DNAI="{{item.DNAI}}",
    ;
{%- endfor -%}
```

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

#### 2.2 配置ULCL过滤器名称。

```jinja2
{%- for item in add_flowfilter_list -%}
    ADD FLOWFILTER:
    {#- --- 必选参数 --- -#}
    FLOWFILTERNAME="{{item.FLOWFILTERNAME}}",
    ;
{%- endfor -%}
```

#### 2.3 配置ULCL分流策略rule。

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

#### 2.4 配置ULCL属性的用户模板。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_userprofile_list的变量区（command: ADD USERPROFILE） -#}
<!-- MISSING_MACRO: command=ADD USERPROFILE list_name=add_userprofile_list step_id=2.4 -->
```

#### 2.5 将上述rule绑定至用户模板。

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

### 3 配置基于DNN的分流，将DNN绑定至UL CL分流规则中。

#### 3.1 配置使能SMF上的ULCL功能。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_apn_list的变量区（command: ADD APN） -#}
<!-- MISSING_MACRO: command=ADD APN list_name=add_apn_list step_id=3.1 -->
```

#### 3.2 配置用户模板组。

```jinja2
{%- for item in add_usrprofgroup_list -%}
    ADD USRPROFGROUP:
    {#- --- 必选参数 --- -#}
    USERPROFGNAME="{{item.USERPROFGNAME}}",
    ;
{%- endfor -%}
```

#### 3.3 将上述用户模板绑定至用户模板组。

```jinja2
{%- for item in add_upbindupg_list -%}
    ADD UPBINDUPG:
    {#- --- 必选参数 --- -#}
    USERPROFGNAME="{{item.USERPROFGNAME}}",
    UPBINDTYPE={{item.UPBINDTYPE}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：UPBINDTYPE=SPECIFIC/DEFAULT/ULCL 时必选 --- -#}
    {%- if item.UPBINDTYPE in ['SPECIFIC', 'DEFAULT', 'ULCL'] -%}
        USERPROFILENAME="{{item.USERPROFILENAME}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 3.4 将用户模板组绑定至指定APN。

```jinja2
{%- for item in add_apnusrprofg_list -%}
    ADD APNUSRPROFG:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    USERPROFGNAME="{{item.USERPROFGNAME}}",
    ;
{%- endfor -%}
```

### 4 配置IPv6会话场景下的分流策略。

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

### 5 打开本特性的License配置开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```


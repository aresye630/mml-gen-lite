---
id: ''
name: 部署基于漫游地动态签约的分流策略控制（SMF）
ne_type: UNC
type: feature
description: 本章节用于指导在SMF上配置基于专网业务DNN的分流策略的过程。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","MEC解决方案","WSFD-223003 基于漫游地动态签约的分流策略控制","特性部署","部署基于漫游地动态签约的分流策略控制（SMF）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本章节用于指导在SMF上配置基于专网业务DNN的分流策略的过程。

## 必备事项
前提条件

* 请仔细阅读WSFD-223003 基于漫游地动态签约的分流策略控制特性概述。
* 已完成本特性License加载，可以通过**DSP LICENSE**命令查询确认，如果本特性的License在查询列表中可见，即可认为本特性License已加载成功。
* 已完成**WSFD-109101 PCC基本功能**、**WSFD-107010 UPF选择**和**WSFD-108002 本地分流策略控制**的部署。
* 以下配置过程是基于SMF和**主锚点UPF**以及**“ULCL UPF+辅锚点UPF”**的对接配置已完成情况下的操作。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    add_pnfdnai_list:
      type: items
      properties:
        INDEX:
          name: '索引'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NFINSTANCEID:
          name: 'NF实例标识'
          type: string
          minLength: 1
          maxLength: 36
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DNAI:
          name: '数据网络访问标识'
          type: string
          minLength: 0
          maxLength: 50
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PNFDNNINDEX:
          name: '对端NF的DNN索引'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: false
          description: ''
          data_source: ''
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
    add_flowfilter_list:
      type: items
      properties:
        FLOWFILTERNAME:
          name: '流过滤器名称'
          type: string
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
          maxLength: 63
          required: true
          description: '配置UL CL分流rule以及和App ID的绑定关系'
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
          description: ''
          data_source: '本端规划'
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
        FLOWFILTERNAME:
          name: '流过滤器名称'
          type: string
          maxLength: 63
          required: false
          description: ''
          data_source: '与对端协商'
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
          description: '配置UL CL属性的User Profile'
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
          data_source: '本端规划'
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
          description: '将UL CL属性的User Profile和rule进行绑定'
          data_source: '全网规划'
          pattern: ''
          default: ''
        RULENAME:
          name: '规则名称'
          type: string
          maxLength: 63
          required: true
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
          minLength: 1
          maxLength: 63
          required: true
          description: '配置使能专网DNN的ULCL功能'
          data_source: '全网规划'
          pattern: ''
          default: ''
        ULCLFUNC:
          name: 'ULCL功能开关'
          type: string
          enum:
          - ENABLE
          - INHERIT
          - DISABLE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: DISABLE
        TRAFFICDIST:
          name: '支持基于漫游地动态签约的分流策略控制'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: DISABLE
    add_usrprofgroup_list:
      type: items
      properties:
        USERPROFGNAME:
          name: '用户模板组名称'
          type: string
          maxLength: 63
          required: true
          description: '配置基于专网业务DNN UL CL分流的用户模板组，并将DNN绑定至该模板组'
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
        CCCONFIGMODE:
          name: '计费属性配置模式'
          type: string
          enum:
          - FLATBILLING
          - HOTBILLING
          - NORMAL
          - PREPAID
          - SPECIFIC
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IMEISVSEGNAME:
          name: 'IMEISV号段名称'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IMSIMSSEGNAME:
          name: 'IMSI/MSISDN号段名称'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LOCALPCCSELECT:
          name: '本地PCC策略选择模式'
          type: string
          enum:
          - INHERIT
          - LOCAL_PCC_ACTIVE
          - LOCAL_PCC_DEACTIVE
          - LOCAL_PCC_NO_CRBN_ACT
          - LOCAL_PCC_NO_RULE_ACT
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: INHERIT
        LOCGROUPNAME:
          name: '位置组名称'
          type: string
          maxLength: 63
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PRIORITY:
          name: '优先级'
          type: integer
          minimum: 1
          maximum: 65534
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RAT:
          name: 'RAT'
          type: string
          enum:
          - EMTC
          - EUTRAN
          - GAN
          - GERAN
          - HSPA
          - NBIOT
          - NONE
          - NR
          - REDCAP
          - UTRAN
          - WLAN
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ROAMING:
          name: '漫游属性'
          type: string
          enum:
          - HOME
          - NONE
          - ROAMING
          - VISITING
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SEGGROUPNAME:
          name: 'IMSI/MSISDN/IMEISV 号段组名称'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: ''
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
  examples:
    add_pnfdnai_list:
    - INDEX: 1
      NFINSTANCEID: 'UPF_Instance_0'
      DNAI: 'testdnai'
      PNFDNNINDEX: 3
    add_ulclprop_list:
    - ULCLPROPNAME: 'testulclpropname'
      DNAI: 'testdnai'
    add_flowfilter_list:
    - FLOWFILTERNAME: 'ulcl'
    add_rule_list:
    - RULENAME: 'testrule'
      POLICYTYPE: ULCL
      POLICYNAME: 'testulclpropname'
      FLOWFILTERNAME: 'ulcl'
      PROTODESCDL: ''
      PROTODESCUL: ''
      RULERANGE: ALL
    add_userprofile_list:
    - USERPROFILENAME: 'testuserprofilename'
      UPTYPE: ULCL
      PROFILERANGE: ALL
    add_rulebinding_list:
    - USERPROFILENAME: 'testuserprofilename'
      RULENAME: 'testrule'
    add_apn_list:
    - APN: 'dnn-ar'
      ULCLFUNC: ENABLE
      TRAFFICDIST: ENABLE
    add_usrprofgroup_list:
    - USERPROFGNAME: 'ulcl_test'
    add_upbindupg_list:
    - USERPROFGNAME: 'ulcl_test'
      UPBINDTYPE: ULCL
      USERPROFILENAME: 'testuserprofilename'
      CCCONFIGMODE: ''
      IMEISVSEGNAME: ''
      IMSIMSSEGNAME: ''
      LOCALPCCSELECT: INHERIT
      LOCGROUPNAME: ''
      PRIORITY: ''
      RAT: ''
      ROAMING: ''
      SEGGROUPNAME: ''
    add_apnusrprofg_list:
    - APN: 'dnn-ar'
      USERPROFGNAME: 'ulcl_test'
    set_smffunc_list:
    - IPV6LOCALUP: UlClPrefer
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 进入“MML命令行-UNC”窗口。

### 2 配置指定APN的ULCL策略。

#### 2.1 配置ULCL属性名称和DNAI的绑定关系。

```jinja2
{%- for item in add_pnfdnai_list -%}
    ADD PNFDNAI:
    {#- --- 必选参数 --- -#}
    INDEX={{item.INDEX}},
    NFINSTANCEID="{{item.NFINSTANCEID}}",
    {#- --- 可选参数 --- -#}
    {%- if item.DNAI is not none -%}
        DNAI="{{item.DNAI}}",
    {%- endif -%}
    {%- if item.PNFDNNINDEX is not none -%}
        PNFDNNINDEX={{item.PNFDNNINDEX}},
    {%- endif -%}
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

#### 2.4 配置ULCL属性的用户模板。

```jinja2
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
```

#### 2.5 将上述rule绑定至用户模板。

```jinja2
{%- for item in add_rulebinding_list -%}
    ADD RULEBINDING:
    {#- --- 必选参数 --- -#}
    USERPROFILENAME="{{item.USERPROFILENAME}}",
    RULENAME="{{item.RULENAME}}",
    ;
{%- endfor -%}
```

### 3 配置基于DNN的分流，将专网DNN绑定至UL CL分流规则中。

#### 3.1 配置使能SMF上的ULCL功能。

```jinja2
{%- for item in add_apn_list -%}
    ADD APN:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    {#- --- 可选参数 --- -#}
    {%- if item.ULCLFUNC is not none -%}
        ULCLFUNC={{item.ULCLFUNC}},
    {%- endif -%}
    {%- if item.TRAFFICDIST is not none -%}
        TRAFFICDIST={{item.TRAFFICDIST}},
    {%- endif -%}
    ;
{%- endfor -%}
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
    {#- --- 条件必选：UPBINDTYPE=SPECIFIC 时必选 --- -#}
    {%- if item.UPBINDTYPE == 'SPECIFIC' -%}
        PRIORITY={{item.PRIORITY}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：UPBINDTYPE=SPECIFIC 时可选 --- -#}
    {%- if item.UPBINDTYPE == 'SPECIFIC' -%}
        {%- if item.CCCONFIGMODE is not none -%}
            CCCONFIGMODE={{item.CCCONFIGMODE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：UPBINDTYPE=SPECIFIC 时可选 --- -#}
    {%- if item.UPBINDTYPE == 'SPECIFIC' -%}
        {%- if item.IMEISVSEGNAME is not none -%}
            IMEISVSEGNAME="{{item.IMEISVSEGNAME}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：UPBINDTYPE=SPECIFIC 时可选 --- -#}
    {%- if item.UPBINDTYPE == 'SPECIFIC' -%}
        {%- if item.IMSIMSSEGNAME is not none -%}
            IMSIMSSEGNAME="{{item.IMSIMSSEGNAME}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：UPBINDTYPE=SPECIFIC/DEFAULT 时可选 --- -#}
    {%- if item.UPBINDTYPE in ['SPECIFIC', 'DEFAULT'] -%}
        {%- if item.LOCALPCCSELECT is not none -%}
            LOCALPCCSELECT={{item.LOCALPCCSELECT}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：UPBINDTYPE=SPECIFIC 时可选 --- -#}
    {%- if item.UPBINDTYPE == 'SPECIFIC' -%}
        {%- if item.LOCGROUPNAME is not none -%}
            LOCGROUPNAME="{{item.LOCGROUPNAME}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：UPBINDTYPE=SPECIFIC 时可选 --- -#}
    {%- if item.UPBINDTYPE == 'SPECIFIC' -%}
        {%- if item.RAT is not none -%}
            RAT={{item.RAT}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：UPBINDTYPE=SPECIFIC 时可选 --- -#}
    {%- if item.UPBINDTYPE == 'SPECIFIC' -%}
        {%- if item.ROAMING is not none -%}
            ROAMING={{item.ROAMING}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：UPBINDTYPE=SPECIFIC 时可选 --- -#}
    {%- if item.UPBINDTYPE == 'SPECIFIC' -%}
        {%- if item.SEGGROUPNAME is not none -%}
            SEGGROUPNAME="{{item.SEGGROUPNAME}}",
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 3.4 将用户模板组绑定至专网DNN。

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


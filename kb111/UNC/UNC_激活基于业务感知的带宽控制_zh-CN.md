---
id: ''
name: 激活基于业务感知的带宽控制
ne_type: UNC
type: feature
description: 保护带宽资源不被P2P/VoIP流量吞噬，确保应用公平分享带宽资源。  适用于GGSN、PGW-C、SMF。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","智能PCC解决方案","WSFD-211005 基于业务感知的带宽控制","激活基于业务感知的带宽控制"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
保护带宽资源不被P2P/VoIP流量吞噬，确保应用公平分享带宽资源。适用于GGSN、PGW-C、SMF。

## 必备事项
前提条件

* 请仔细阅读WSFD-211005 基于业务感知的带宽控制特性概述。
* 请仔细阅读WSFD-109101 PCC基本功能。
* 完成激活PCC基本功能/激活PCC基本功能。
* 完成加载License。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
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
          description: '使用样例值。'
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
          description: '配置UserProfile。'
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
    add_usrprofgroup_list:
      type: items
      properties:
        USERPROFGNAME:
          name: '用户模板组名称'
          type: string
          maxLength: 63
          required: true
          description: '配置UserProfile Group。'
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
          description: '将UserProfile绑定到UserProfile Group。'
          data_source: '全网规划'
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
          data_source: '本端规划'
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
          description: '将UserProfile Group绑定到DNN。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        USERPROFGNAME:
          name: '用户模板组名称'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    add_rule_list:
    - RULENAME: 'rule_test'
      POLICYTYPE: BWM
      PRIORITY: 10
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
    add_usrprofgroup_list:
    - USERPROFGNAME: 'upg_test'
    add_upbindupg_list:
    - USERPROFGNAME: 'upg_test'
      UPBINDTYPE: DEFAULT
      USERPROFILENAME: 'up_test'
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
    - APN: 'huawei.com'
      USERPROFGNAME: 'upg_test'
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 配置SMF上的本地rule。用于动态PCC时PCF下发预定义规则，或本地PCC时的静态规则。

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
```

### 规则用于带宽控制时，“策略类型（POLICYTYPE）”设置为“BWM”。

### 2 配置SMF上的UserProfile，将本地rule绑定到UserProfile上。用于动态PCC时PCF下发预定义规则组，或本地PCC时的静态规则组。

#### 2.1 配置UserProfile。如已配置，请跳过本步骤。

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

#### 2.2 将rule绑定到UserProfile。

```jinja2
{%- for item in add_rulebinding_list -%}
    ADD RULEBINDING:
    {#- --- 必选参数 --- -#}
    USERPROFILENAME="{{item.USERPROFILENAME}}",
    RULENAME="{{item.RULENAME}}",
    ;
{%- endfor -%}
```

### 3 配置UserProfile组，将UserProfile绑定到UserProfile组，再将UserProfile组绑定到DNN实例上。用于动态PCC或本地PCC。

#### 3.1 配置UserProfile Group。如已配置，请跳过本步骤。

```jinja2
{%- for item in add_usrprofgroup_list -%}
    ADD USRPROFGROUP:
    {#- --- 必选参数 --- -#}
    USERPROFGNAME="{{item.USERPROFGNAME}}",
    ;
{%- endfor -%}
```

#### 3.2 将UserProfile绑定到UserProfile Group。如已配置，请跳过本步骤。

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

#### 3.3 UserProfile Group绑定到DNN。如已配置，请跳过本步骤。

```jinja2
{%- for item in add_apnusrprofg_list -%}
    ADD APNUSRPROFG:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    USERPROFGNAME="{{item.USERPROFGNAME}}",
    ;
{%- endfor -%}
```


---
id: GWFD-024303
name: 配置业务触发RADIUS功能
ne_type: UEG
type: feature
description: 需要使能业务触发RADIUS时，执行此任务。  适用于PGW-C、SMF
tags: []
risk_level: ''
doc_source: ["业务配置","风筝L","MEC 特性指南（风筝L）","GW-C&SMF特性指南","GWFD-024300 系统管理","GWFD-024303 Radius功能","激活RADIUS功能","配置业务触发RADIUS功能"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
需要使能业务触发RADIUS时，执行此任务。适用于PGW-C、SMF

## 必备事项
前提条件

* 请仔细阅读GWFD-024303 Radius功能特性概述。
* UEG与周边网元的互通配置已经完成。
* 完成增加APN配置。
* **该功能需要与UPF/PGW-U共同完成配置**。配置该功能前，需要确保已在UPF/PGW-U上配置完成使用的过滤器和绑定的流过滤器、规则等业务感知信息。
* 已通过**ADD LOGICIP**配置完成逻辑接口使用到的逻辑IP。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    add_cpapn_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    set_apnrdsacctctrl_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          maxLength: 63
          required: true
          description: '在指定APN下使能业务触发RADIUS功能。  当UEG的产品形态为风筝L时，已通过**ADD CPAPN**配置，可以使用****LST CPAPN****命令进行查询。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        SRVTRIGGER:
          name: '业务报文（通过3/4层规则配置）时触发计费请求消息'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_cpsvcflowfilter_list:
      type: items
      properties:
        FLOWFILTERNAME:
          name: '流过滤器名称'
          type: string
          maxLength: 63
          required: true
          description: '需要与UPF/PGW-U上规划的流过滤器保持一致。'
          data_source: '与对端协商'
          pattern: ''
          default: ''
    add_cprule_list:
      type: items
      properties:
        RULENAME:
          name: '规则名称'
          type: string
          maxLength: 63
          required: true
          description: '用于对匹配上该规则的业务进行业务触发RADIUS动作，需要与UPF/PGW-U上规划的规则保持一致。'
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
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        PRIORITY:
          name: '全局优先级'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: 4294967295
    add_cpuserprofile_list:
      type: items
      properties:
        USERPROFILENAME:
          name: '用户模板名称'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: '本端规划'
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
    add_cprulebinding_list:
      type: items
      properties:
        USERPROFILENAME:
          name: '用户模板名称'
          type: string
          maxLength: 63
          required: true
          description: '当UEG的产品形态为风筝L时，已通过**ADD CPUSERPROFILE**配置，可以使用****LST CPUSERPROFIL****命令进行查询。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        RULENAME:
          name: '规则名称'
          type: string
          maxLength: 63
          required: true
          description: 'User Profile绑定的业务规则，当UEG的产品形态为风筝L时，已通过**ADD CPRULE**配置，可以使用****LST CPRULE****命令进行查询。'
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
          description: ''
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
          description: '已经通过**ADD USRPROFGROUP**命令配置完成，可以使用**LST USRPROFGROUP**查询。'
          data_source: '已配置数据中获取'
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
          data_source: '本端规划'
          pattern: ''
          default: ''
        USERPROFILENAME:
          name: '用户模板名称'
          type: string
          maxLength: 63
          required: false
          description: '当UEG的产品形态为风筝L时，已通过**ADD CPUSERPROFILE**配置，可以使用****LST CPUSERPROFIL****命令进行查询。  。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_apnusrprofg_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          maxLength: 63
          required: true
          description: '将User Profile Group绑定到指定APN下。  当UEG的产品形态为风筝L时，已通过**ADD CPAPN**配置，可以使用****LST CPAPN****命令进行查询。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        USERPROFGNAME:
          name: '用户模板组名称'
          type: string
          maxLength: 63
          required: true
          description: '已经通过**ADD USRPROFGROUP**命令配置完成，可以使用**LST USRPROFGROUP**查询。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
  examples:
    add_cpapn_list:
    - APN: 'apn-test'
    set_apnrdsacctctrl_list:
    - APN: 'apn-test'
      SRVTRIGGER: ENABLE
    add_cpsvcflowfilter_list:
    - FLOWFILTERNAME: 'flowfilter_1'
    add_cprule_list:
    - RULENAME: 'rule_test1'
      POLICYTYPE: SRV_TRIGGER
      PRIORITY: 50
    add_cpuserprofile_list:
    - USERPROFILENAME: 'up_test'
      UPTYPE: PCC
    add_cprulebinding_list:
    - USERPROFILENAME: 'up_test'
      RULENAME: 'rule_test1'
    add_usrprofgroup_list:
    - USERPROFGNAME: 'upg_test'
    add_upbindupg_list:
    - USERPROFGNAME: 'upg_test'
      UPBINDTYPE: DEFAULT
      USERPROFILENAME: 'up_test'
    add_apnusrprofg_list:
    - APN: 'apn-test'
      USERPROFGNAME: 'upg_test'
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 进入“MML命令行-UEG”窗口。

### 2 配置业务触发RADIUS功能。

#### 2.1 配置APN。

#### 当UEG的产品形态为风筝L时，**ADD CPAPN**

```jinja2
{%- for item in add_cpapn_list -%}
    ADD CPAPN:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    ;
{%- endfor -%}
```

#### 2.2 使能业务触发RADIUS功能。

#### **SET APNRDSACCTCTRL**

```jinja2
{%- for item in set_apnrdsacctctrl_list -%}
    SET APNRDSACCTCTRL:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    {#- --- 可选参数 --- -#}
    {%- if item.SRVTRIGGER is not none -%}
        SRVTRIGGER={{item.SRVTRIGGER}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 配置业务使用的流过滤器。

### 当UEG的产品形态为风筝L时，****ADD CPSVCFLOWFILTER****

```jinja2
{%- for item in add_cpsvcflowfilter_list -%}
    ADD CPSVCFLOWFILTER:
    {#- --- 必选参数 --- -#}
    FLOWFILTERNAME="{{item.FLOWFILTERNAME}}",
    ;
{%- endfor -%}
```

### 4 配置业务规则。

### 当UEG的产品形态为风筝L时，**ADD CPRULE**

```jinja2
{%- for item in add_cprule_list -%}
    ADD CPRULE:
    {#- --- 必选参数 --- -#}
    RULENAME="{{item.RULENAME}}",
    POLICYTYPE={{item.POLICYTYPE}},
    {#- --- 可选参数 --- -#}
    {%- if item.PRIORITY is not none -%}
        PRIORITY={{item.PRIORITY}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 5 配置业务策略组合。

#### 5.1 配置UserProfile模板。

#### 当UEG的产品形态为风筝L时，**ADD CPUSERPROFILE**

```jinja2
{%- for item in add_cpuserprofile_list -%}
    ADD CPUSERPROFILE:
    {#- --- 必选参数 --- -#}
    USERPROFILENAME="{{item.USERPROFILENAME}}",
    UPTYPE={{item.UPTYPE}},
    ;
{%- endfor -%}
```

#### 5.2 将已配置的Rule绑定到UserProfile。

#### 当UEG的产品形态为风筝L时，ADD CPRULEBINDING

```jinja2
{%- for item in add_cprulebinding_list -%}
    ADD CPRULEBINDING:
    {#- --- 必选参数 --- -#}
    USERPROFILENAME="{{item.USERPROFILENAME}}",
    RULENAME="{{item.RULENAME}}",
    ;
{%- endfor -%}
```

#### 5.3 配置UsrProfGroup。

#### **ADD USRPROFGROUP**

```jinja2
{%- for item in add_usrprofgroup_list -%}
    ADD USRPROFGROUP:
    {#- --- 必选参数 --- -#}
    USERPROFGNAME="{{item.USERPROFGNAME}}",
    ;
{%- endfor -%}
```

#### 5.4 将UserProfile绑定到UsrProfGroup。

#### **ADD UPBINDUPG**

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

#### 5.5 将UsrProfGroup绑定到指定APN。

#### **ADD APNUSRPROFG**

```jinja2
{%- for item in add_apnusrprofg_list -%}
    ADD APNUSRPROFG:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    USERPROFGNAME="{{item.USERPROFGNAME}}",
    ;
{%- endfor -%}
```

#### 业务策略组合和APN建立绑定关系后，对该APN已经存在的用户无效，只对后续激活的用户生效。


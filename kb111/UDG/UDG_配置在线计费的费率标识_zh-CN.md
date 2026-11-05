---
id: ''
name: 配置在线计费的费率标识
ne_type: UDG
type: feature
description: 本操作描述在线计费使用的费率标识的配置过程。  在线计费中，UNC与OCS消息交互时需要用到费率标识。UNC支持用户级在线计费，也支持更细粒度的按用户使用的业务进行在线计费，即内容计费。这两种方式下都以费率组（Rating Group，缩写为RG）和业务ID（Service ID，缩写为SID）作为费率标识，其中RG是必须的，SID是可选的，同时使用RG和SID进行标识，使在线计费能够做更细粒度的信用控制，且OCS可以生成更丰富的话单信息。  如果OCS主动推送费率标识类型与UNC本地配置不一致，则认为是无效的，去激活PDP上下文/EPS承载。所以要求UNC和OCS两端的费率标识配置一致。
risk_level: ''
doc_source: ["特性部署","业务专题","5G Core 计费解决方案","计费解决方案概述","计费方案部署与调测","方案二：部署NCG且基于传统Ga/Gy接口计费组网方案","SMF配置","在线计费配置","配置在线计费的费率标识"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本操作描述在线计费使用的费率标识的配置过程。在线计费中，UNC与OCS消息交互时需要用到费率标识。UNC支持用户级在线计费，也支持更细粒度的按用户使用的业务进行在线计费，即内容计费。这两种方式下都以费率组（Rating Group，缩写为RG）和业务ID（Service ID，缩写为SID）作为费率标识，其中RG是必须的，SID是可选的，同时使用RG和SID进行标识，使在线计费能够做更细粒度的信用控制，且OCS可以生成更丰富的话单信息。如果OCS主动推送费率标识类型与UNC本地配置不一致，则认为是无效的，去激活PDP上下文/EPS承载。所以要求UNC和OCS两端的费率标识配置一致。

## 必备事项
前提条件

* 请仔细阅读Ga/Gy接口离线/在线计费。

* 完成加载license。
* 本操作任务涉及的APN/DNN、User Profile、User Profile group已经创建完成，并完成User Profile group与APN/DNN的绑定。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    add_urr_list:
      type: items
      properties:
        URRNAME:
          name: '使用量上报规则名称'
          type: string
          required: false
          description: '配置使用量上报规则，从而配置使用的费率标识。  说明：  参数“USAGERPTMODE”取值“ONLINE”时，参数“ONLCOMPOUNDTYPE”、“ONLINERG”、“ONLINESID”组合配置要求唯一。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        URRID:
          name: 'URR标识'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        USAGERPTMODE:
          name: '使用量上报模式'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ONLCOMPOUNDTYPE:
          name: '在线计费标识组成类型'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ONLINERG:
          name: '在线计费组'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ONLMETERINGTYPE:
          name: '在线计费统计类型'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_glburrgroup_list:
      type: items
      properties:
        UPONLURRNAME:
          name: '上行发起在线URR名称'
          type: string
          required: false
          description: '将URR绑定到全局URR组上。如果上下行使用不同的URR，则两者必须同时为在线计费或离线计费。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        DNONLURRNAME:
          name: '下行发起在线URR名称'
          type: string
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_urr_list_1:
      type: items
      properties:
        URRNAME:
          name: '使用量上报规则名称'
          type: string
          required: false
          description: '配置使用量上报规则，从而配置使用的费率标识。  说明：  参数“USAGERPTMODE”取值“ONLINE”时，参数“ONLCOMPOUNDTYPE”、“ONLINERG”、“ONLINESID”组合配置要求唯一。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        URRID:
          name: 'URR标识'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        USAGERPTMODE:
          name: '使用量上报模式'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ONLCOMPOUNDTYPE:
          name: '在线计费标识组成类型'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ONLINERG:
          name: '在线计费组'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ONLMETERINGTYPE:
          name: '在线计费统计类型'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_urrgroup_list:
      type: items
      properties:
        URRGROUPNAME:
          name: '使用量上报规则组名称'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: '配置URR组，将上下行URR绑定到URR组上。  如果上下行使用不同的URR，则两者必须同时为在线计费或离线计费。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        UPURRNAME1:
          name: '上行发起URR名称1'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        DOWNURRNAME1:
          name: '下行发起URR名称1'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    set_urrgrpbinding_list:
      type: items
      properties:
        USERPROFILENAME:
          name: '用户模板名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '将URR组绑定到User Profile上。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        DFTURRGRPNAME:
          name: '缺省URR组名称'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: ''
          data_source: '已配置数据中获取'
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
    add_urr_list_2:
      type: items
      properties:
        URRNAME:
          name: '使用量上报规则名称'
          type: string
          required: false
          description: '配置使用量上报规则，从而配置使用的费率标识。  说明：  参数“USAGERPTMODE”取值“ONLINE”时，参数“ONLCOMPOUNDTYPE”、“ONLINERG”、“ONLINESID”组合配置要求唯一。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        URRID:
          name: 'URR标识'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        USAGERPTMODE:
          name: '使用量上报模式'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ONLCOMPOUNDTYPE:
          name: '在线计费标识组成类型'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ONLINERG:
          name: '在线计费组'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ONLMETERINGTYPE:
          name: '在线计费统计类型'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_urrgroup_list_1:
      type: items
      properties:
        URRGROUPNAME:
          name: '使用量上报规则组名称'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: '配置URR组，将上下行URR绑定到URR组上。  如果上下行使用不同的URR，则两者必须同时为在线计费或离线计费。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        UPURRNAME1:
          name: '上行发起URR名称1'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        DOWNURRNAME1:
          name: '下行发起URR名称1'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_pccpolicygrp_list:
      type: items
      properties:
        PCCPOLICYGRPNM:
          name: 'PCC策略组名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '配置内容计费使用的Rule。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        URRGROUPNAME:
          name: 'URR组名称'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: ''
          data_source: '已配置数据中获取'
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
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        PRIORITY:
          name: '优先级'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: 4294967295
        POLICYNAME:
          name: '策略名称'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: ''
          data_source: '已配置数据中获取'
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
        FLOWFILTERNAME:
          name: '流过滤器名称'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        FLWFLTRGRPNAME:
          name: '流过滤器组名称'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ADCMUTEFLAG:
          name: 'ADC静默通知标识'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ENABLE
        ALGSWITCH:
          name: 'ALG功能开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
        RDSTRIGGERFLAG:
          name: 'Radius消息触发标识'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
        REDIRIPVERFLAG:
          name: 'IP重定向虚拟IP协议版本'
          type: string
          enum:
          - IPV4
          - IPV6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        REMARKFPISEL:
          name: '重标记、FPI或SAI选择'
          type: string
          enum:
          - FPI
          - REMARK
          - REMARKANDFPI
          - SAI
          - REMARKANDSAI
          - FPIANDSAI
          - RMKFPISAI
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: REMARK
        SRVLBOFLAG:
          name: '本地业务分流标识'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
        WORKERNAME:
          name: '通用Rule子策略名称'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        WORKERPARA:
          name: '通用策略参数'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: ''
          data_source: ''
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
          description: '将Rule绑定到User Profile上。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        RULENAME:
          name: '规则名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
  examples:
    add_urr_list:
    - URRNAME: urr_online_URL
      URRID: '2300'
      USAGERPTMODE: ONLINE
      ONLCOMPOUNDTYPE: ONLYRG
      ONLINERG: '100'
      ONLMETERINGTYPE: EVENT_VOLUME_TIME
    set_glburrgroup_list:
    - UPONLURRNAME: urr_online_URL
      DNONLURRNAME: urr_online_URL
    add_urr_list_1:
    - URRNAME: urr_online_URL
      URRID: '2300'
      USAGERPTMODE: ONLINE
      ONLCOMPOUNDTYPE: ONLYRG
      ONLINERG: '100'
      ONLMETERINGTYPE: EVENT_VOLUME_TIME
    add_urrgroup_list:
    - URRGROUPNAME: 'UrrGp_URL'
      UPURRNAME1: 'urr_online_URL'
      DOWNURRNAME1: 'urr_online_URL'
    set_urrgrpbinding_list:
    - USERPROFILENAME: 'userprofile001'
      DFTURRGRPNAME: 'UrrGp_any'
    set_licenseswitch_list:
    - LICITEM: 'LKV3W9BCC12'
      SWITCH: ENABLE
    add_urr_list_2:
    - URRNAME: urr_online_URL
      URRID: '2300'
      USAGERPTMODE: ONLINE
      ONLCOMPOUNDTYPE: ONLYRG
      ONLINERG: '100'
      ONLMETERINGTYPE: VOLUME
    add_urrgroup_list_1:
    - URRGROUPNAME: 'UrrGp_URL'
      UPURRNAME1: 'urr_online_URL'
      DOWNURRNAME1: 'urr_online_URL'
    add_pccpolicygrp_list:
    - PCCPOLICYGRPNM: 'PPG_URL'
      URRGROUPNAME: 'UrrGp_URL'
    add_rule_list:
    - RULENAME: 'Rule001_url'
      POLICYTYPE: PCC
      PRIORITY: 100
      POLICYNAME: 'PPG_URL'
      FILTERINGMODE: ''
      FLOWFILTERNAME: ''
      FLWFLTRGRPNAME: ''
      ADCMUTEFLAG: ENABLE
      ALGSWITCH: DISABLE
      RDSTRIGGERFLAG: DISABLE
      REDIRIPVERFLAG: ''
      REMARKFPISEL: REMARK
      SRVLBOFLAG: DISABLE
      WORKERNAME: ''
      WORKERPARA: ''
    add_rulebinding_list:
    - USERPROFILENAME: 'userprofile001'
      RULENAME: 'Rule001_url'
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 配置全局粒度的Session级计费费率标识。

#### 1.1 配置全局URR，从而配置相应的计费费率标识，包括必须配置的RG和可选配置的SID。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_urr_list的变量区（command: ADD URR） -#}
<!-- MISSING_MACRO: command=ADD URR list_name=add_urr_list step_id=1.1 -->
```

##### 1.1.1 各费率组RG的配额一般由OCS下发，当OCS不支持配置配额下发的具体数值时，也可以在UNC本地配置要申请的配额数。本地通过**ADD URR**命令参数“ONLMETERINGTYPE”的值“VOLUME”（按流量计费），或“TIME”（按时间计费）配置相应的配额数即可。

##### 1.1.2 当OCS配置了下发的配额数并且UNC配置了申请的配额数时，OCS上的配置优先级高。

#### 1.2 将全局URR绑定到全局URR组上，上下行可以使用不同的URR。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_glburrgroup_list的变量区（command: SET GLBURRGROUP） -#}
<!-- MISSING_MACRO: command=SET GLBURRGROUP list_name=set_glburrgroup_list step_id=1.2 -->
```

### 2 配置User Profile粒度的Session级计费费率标识。

#### 2.1 配置User Profile下绑定的缺省URR组及相应URR，从而配置相应的计费费率标识。

##### 2.1.1 配置URR，从而配置相应的计费费率标识，包括必须配置的RG和可选配置的SID。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_urr_list_1的变量区（command: ADD URR） -#}
<!-- MISSING_MACRO: command=ADD URR list_name=add_urr_list_1 step_id=2.1.1 -->
```

##### 2.1.2 配置URR组，将上下行URR绑定到URR组上。上下行可以使用不同的URR。

```jinja2
{%- for item in add_urrgroup_list -%}
    ADD URRGROUP:
    {#- --- 必选参数 --- -#}
    URRGROUPNAME="{{item.URRGROUPNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.UPURRNAME1 is not none -%}
        UPURRNAME1="{{item.UPURRNAME1}}",
    {%- endif -%}
    {%- if item.DOWNURRNAME1 is not none -%}
        DOWNURRNAME1="{{item.DOWNURRNAME1}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 2.2 为User Profile绑定缺省URR组。

```jinja2
{%- for item in set_urrgrpbinding_list -%}
    SET URRGRPBINDING:
    {#- --- 必选参数 --- -#}
    USERPROFILENAME="{{item.USERPROFILENAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.DFTURRGRPNAME is not none -%}
        DFTURRGRPNAME="{{item.DFTURRGRPNAME}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 配置内容计费费率标识。

#### 3.1 打开内容计费的License配置开关。

#### 配置内容计费费率标识不依赖于内容计费License，但内容计费费率标识需在打开内容计费License后生效。因此，仅在激活内容计费时，执行本步骤。

```jinja2
{%- if is_scenario_content_charging -%}
    {%- for item in set_licenseswitch_list -%}
        SET LICENSESWITCH:
        {#- --- 必选参数 --- -#}
        LICITEM="{{item.LICITEM}}",
        SWITCH={{item.SWITCH}},
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 3.2 配置内容计费使用的URR组及相应URR，从而配置相应的计费费率标识。

##### 3.2.1 配置URR，从而配置相应的计费费率标识，包括必须配置的RG和可选配置的SID。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_urr_list_2的变量区（command: ADD URR） -#}
<!-- MISSING_MACRO: command=ADD URR list_name=add_urr_list_2 step_id=3.2.1 -->
```

##### 3.2.2 配置URR组，将上下行URR绑定到URR组上。上下行可以使用不同的URR。

```jinja2
{%- for item in add_urrgroup_list_1 -%}
    ADD URRGROUP:
    {#- --- 必选参数 --- -#}
    URRGROUPNAME="{{item.URRGROUPNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.UPURRNAME1 is not none -%}
        UPURRNAME1="{{item.UPURRNAME1}}",
    {%- endif -%}
    {%- if item.DOWNURRNAME1 is not none -%}
        DOWNURRNAME1="{{item.DOWNURRNAME1}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 3.3 配置内容计费使用的Rule，将URR组绑定到对应的Rule上。

##### 3.3.1 配置Rule绑定的PCC策略组，将URR组绑定到PCC策略组。

```jinja2
{%- for item in add_pccpolicygrp_list -%}
    ADD PCCPOLICYGRP:
    {#- --- 必选参数 --- -#}
    PCCPOLICYGRPNM="{{item.PCCPOLICYGRPNM}}",
    {#- --- 可选参数 --- -#}
    {%- if item.URRGROUPNAME is not none -%}
        URRGROUPNAME="{{item.URRGROUPNAME}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

##### 3.3.2 配置Rule，将PCC策略组绑定到Rule上。

```jinja2
{%- for item in add_rule_list -%}
    ADD RULE:
    {#- --- 必选参数 --- -#}
    RULENAME="{{item.RULENAME}}",
    POLICYTYPE={{item.POLICYTYPE}},
    FILTERINGMODE={{item.FILTERINGMODE}},
    {#- --- 可选参数 --- -#}
    {%- if item.PRIORITY is not none -%}
        PRIORITY={{item.PRIORITY}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：POLICYTYPE=PCC/BWM/HEADEN/SMARTREDIRECT/TRAFFICCLASS/FIREWALL/QOS/WEBPROXY 时必选 --- -#}
    {%- if item.POLICYTYPE in ['PCC', 'BWM', 'HEADEN', 'SMARTREDIRECT', 'TRAFFICCLASS', 'FIREWALL', 'QOS', 'WEBPROXY'] -%}
        POLICYNAME="{{item.POLICYNAME}}",
    {%- endif -%}
    {#- --- 条件必选：POLICYTYPE=ADC 时必选 --- -#}
    {%- if item.POLICYTYPE == 'ADC' -%}
        ADCMUTEFLAG={{item.ADCMUTEFLAG}},
    {%- endif -%}
    {#- --- 条件必选：FILTERINGMODE=FLOWFILTER 时必选 --- -#}
    {%- if item.FILTERINGMODE == 'FLOWFILTER' -%}
        FLOWFILTERNAME="{{item.FLOWFILTERNAME}}",
    {%- endif -%}
    {#- --- 条件必选：FILTERINGMODE=FLOWFILTERGRP 时必选 --- -#}
    {%- if item.FILTERINGMODE == 'FLOWFILTERGRP' -%}
        FLWFLTRGRPNAME="{{item.FLWFLTRGRPNAME}}",
    {%- endif -%}
    {#- --- 条件必选：POLICYTYPE=SRV_TRIGGER 时必选 --- -#}
    {%- if item.POLICYTYPE == 'SRV_TRIGGER' -%}
        RDSTRIGGERFLAG={{item.RDSTRIGGERFLAG}},
    {%- endif -%}
    {#- --- 条件必选：POLICYTYPE=IPREDIR 时必选 --- -#}
    {%- if item.POLICYTYPE == 'IPREDIR' -%}
        REDIRIPVERFLAG={{item.REDIRIPVERFLAG}},
    {%- endif -%}
    {#- --- 条件必选：POLICYTYPE=REMARK_FPI 时必选 --- -#}
    {%- if item.POLICYTYPE == 'REMARK_FPI' -%}
        REMARKFPISEL={{item.REMARKFPISEL}},
    {%- endif -%}
    {#- --- 条件必选：POLICYTYPE=LBO 时必选 --- -#}
    {%- if item.POLICYTYPE == 'LBO' -%}
        SRVLBOFLAG={{item.SRVLBOFLAG}},
    {%- endif -%}
    {#- --- 条件必选：POLICYTYPE=WORKER 时必选 --- -#}
    {%- if item.POLICYTYPE == 'WORKER' -%}
        WORKERNAME="{{item.WORKERNAME}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：POLICYTYPE=WEBPROXY 时可选 --- -#}
    {%- if item.POLICYTYPE == 'WEBPROXY' -%}
        {%- if item.ALGSWITCH is not none -%}
            ALGSWITCH={{item.ALGSWITCH}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：POLICYTYPE=WORKER 时可选 --- -#}
    {%- if item.POLICYTYPE == 'WORKER' -%}
        {%- if item.WORKERPARA is not none -%}
            WORKERPARA="{{item.WORKERPARA}}",
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 3.4 为User Profile绑定Rule。

```jinja2
{%- for item in add_rulebinding_list -%}
    ADD RULEBINDING:
    {#- --- 必选参数 --- -#}
    USERPROFILENAME="{{item.USERPROFILENAME}}",
    RULENAME="{{item.RULENAME}}",
    ;
{%- endfor -%}
```


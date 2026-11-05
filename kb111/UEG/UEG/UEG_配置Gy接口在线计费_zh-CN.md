---
id: GWFD-022101
name: 配置Gy接口在线计费
ne_type: UEG
type: feature
description: 适用于PGW-U。  在线计费中，UEG支持按用户使用的业务进行在线计费，UEG与UNC消息交互时需要用到URR ID，上报计费信息。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝S","MEC 特性指南（风筝S）","UEG特性指南","计费功能","GWFD-022101 在线计费","配置Gy接口在线计费"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
适用于PGW-U。在线计费中，UEG支持按用户使用的业务进行在线计费，UEG与UNC消息交互时需要用到URR ID，上报计费信息。

## 必备事项
前提条件

请仔细阅读Ga/Gy接口离线/在线计费。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
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
    add_urr_list:
      type: items
      properties:
        URRNAME:
          name: '使用量上报规则名称'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: '使用量上报规则信息。  URRID、USAGERPTMODE、ONLMETERINGTYPE在PGW-C和PGW-U上的配置需要保持一致。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        URRID:
          name: 'URR标识'
          type: integer
          minimum: 0
          maximum: 2147483646
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        USAGERPTMODE:
          name: '使用量上报模式'
          type: string
          enum:
          - MONITORINGKEY
          - OFFLINE
          - ONLINE
          - QOS
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        ONLMETERINGTYPE:
          name: '在线计费统计类型'
          type: string
          enum:
          - EVENT
          - EVENT_TIME
          - EVENT_VOLUME
          - EVENT_VOLUME_TIME
          - FREE
          - TIME
          - VOLUME
          - VOLUME_TIME
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: VOLUME
    add_urrgroup_list:
      type: items
      properties:
        URRGROUPNAME:
          name: '使用量上报规则组名称'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: '配置URRGROUP。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        UPURRNAME1:
          name: '上行发起URR名称1'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: '已在该配置任务中通过命令**ADD URR**配置。'
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
          description: 'PCC策略组。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        URRGROUPNAME:
          name: 'URR组名称'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: 'PCC策略组绑定的URR组，已通过**ADD URRGROUP**命令配置完成。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_filter_list:
      type: items
      properties:
        FILTERNAME:
          name: '过滤器名字'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '通过将用户上下行报文匹配filter，实现报文的过滤。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        L34PROTTYPE:
          name: '三四层IPv4协议输入类型'
          type: string
          enum:
          - NUMBER
          - STRING
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        L34PROTOCOL:
          name: '三四层协议类型'
          type: string
          enum:
          - ANY
          - GRE
          - ICMP
          - TCP
          - UDP
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ANY
        SVRSTARTPORT:
          name: '服务器起始端口号'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: 0
        SVRENDPORT:
          name: '服务器结束端口号'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: 65535
    add_flowfilter_list:
      type: items
      properties:
        FLOWFILTERNAME:
          name: '流过滤器名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '流过滤器。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_fltbindflowf_list:
      type: items
      properties:
        FLOWFILTERNAME:
          name: '流过滤器名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        FILTERNAME:
          name: '过滤器名字'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '绑定的三四层过滤条件已通过**ADD FILTER**命令配置。'
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
          description: '使用的内容计费规则。PGW-C、PGW-U上RuleName以及RULE下配置的POLICYTYPE、POLICYNAME需要保持一致。'
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
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        FILTERINGMODE:
          name: '流过滤器或流过滤器组选择'
          type: string
          enum:
          - FLOWFILTER
          - FLOWFILTERGRP
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        FLOWFILTERNAME:
          name: '流过滤器名称'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: '绑定的FlowFilter已通过**ADD FLOWFILTER**命令配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        POLICYNAME:
          name: '策略名称'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: '绑定的PCC策略组已通过**ADD PCCPOLICYGRP**命令配置。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PRIORITY:
          name: '优先级'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: false
          description: '数字越小优先级越高。只绑定三四层filter的RULE的优先级应该低于绑定7层filter的RULE的优先级。'
          data_source: '本端规划'
          pattern: ''
          default: 4294967295
    set_refreshsrv_list:
      type: items
      properties:
        REFRESHTYPE:
          name: '刷新类型'
          type: string
          enum:
          - ACL
          - ALL
          - USERPROFILE
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
          minLength: 0
          maxLength: 63
          required: true
          description: 'USERPROFILE的名称统一规划，保证在PCRF、PGW-C、PGW-U间名称一致。不一致时PCF下发的策略无法生效。'
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
          description: '已通过**ADD USERPROFILE**命令配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        RULENAME:
          name: '规则名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '已通过**ADD RULE**命令配置。  PGW-C、PGW-U上USERPROFILE下绑定的RULENAME、POLICYTYPE需要保持一致。不一致策略无法按照预期生效。'
          data_source: ''
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
          data_source: ''
          pattern: ''
          default: ''
    set_updefaultquota_list:
      type: items
      properties:
        USERTYPE:
          name: '用户漫游类型'
          type: string
          enum:
          - HOME
          - ROAMING
          - VISITING
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DFTQTSWITCH:
          name: '默认配额使能开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_upglbchgpara_list:
      type: items
      properties: {}
    set_urrfailaction_list:
      type: items
      properties: {}
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV3G5OLCH01'
      SWITCH: ENABLE
    add_urr_list:
    - URRNAME: 'onlineURR'
      URRID: 1100
      USAGERPTMODE: ONLINE
      ONLMETERINGTYPE: EVENT_VOLUME_TIME
    add_urrgroup_list:
    - URRGROUPNAME: 'urrgroup001'
      UPURRNAME1: 'onlineURR'
      DOWNURRNAME1: 'onlineURR'
    add_pccpolicygrp_list:
    - PCCPOLICYGRPNM: 'cg_red'
      URRGROUPNAME: 'urrgroup001'
    add_filter_list:
    - FILTERNAME: 'filter_red'
      L34PROTTYPE: STRING
      L34PROTOCOL: TCP
      SVRSTARTPORT: 80
      SVRENDPORT: 80
    add_flowfilter_list:
    - FLOWFILTERNAME: 'fg_red'
    add_fltbindflowf_list:
    - FLOWFILTERNAME: 'fg_red'
      FILTERNAME: 'filter_red'
    add_rule_list:
    - RULENAME: 'Rule002'
      POLICYTYPE: PCC
      FILTERINGMODE: FLOWFILTER
      FLOWFILTERNAME: 'fg_red'
      POLICYNAME: 'cg_red'
      PRIORITY: 120
    set_refreshsrv_list:
    - REFRESHTYPE: USERPROFILE
    add_userprofile_list:
    - USERPROFILENAME: 'up_test'
    add_rulebinding_list:
    - USERPROFILENAME: 'up_test'
      RULENAME: 'Rule002'
      POLICYTYPE: PCC
    set_updefaultquota_list:
    - USERTYPE: ''
      DFTQTSWITCH: ''
    set_upglbchgpara_list:
    - {}
    set_urrfailaction_list:
    - {}
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 0 配置业务级在线计费的费率标识。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

### 1 配置内容计费使用的URR。

#### 1.1 配置URR。

```jinja2
{%- for item in add_urr_list -%}
    ADD URR:
    {#- --- 必选参数 --- -#}
    URRNAME="{{item.URRNAME}}",
    URRID={{item.URRID}},
    USAGERPTMODE={{item.USAGERPTMODE}},
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：USAGERPTMODE=ONLINE 时可选 --- -#}
    {%- if item.USAGERPTMODE == 'ONLINE' -%}
        {%- if item.ONLMETERINGTYPE is not none -%}
            ONLMETERINGTYPE={{item.ONLMETERINGTYPE}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 1.2 配置上行和下行发起的业务对应的URR。

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

### 2 配置内容计费使用的PCC策略组。

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

### 3 配置过滤条件。

#### 3.1 配置三四层过滤条件。

```jinja2
{%- for item in add_filter_list -%}
    ADD FILTER:
    {#- --- 必选参数 --- -#}
    FILTERNAME="{{item.FILTERNAME}}",
    L34PROTTYPE={{item.L34PROTTYPE}},
    {#- --- 可选参数 --- -#}
    {%- if item.SVRSTARTPORT is not none -%}
        SVRSTARTPORT={{item.SVRSTARTPORT}},
    {%- endif -%}
    {%- if item.SVRENDPORT is not none -%}
        SVRENDPORT={{item.SVRENDPORT}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：L34PROTTYPE=STRING 时必选 --- -#}
    {%- if item.L34PROTTYPE == 'STRING' -%}
        L34PROTOCOL={{item.L34PROTOCOL}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 3.2 配置流过滤器。

```jinja2
{%- for item in add_flowfilter_list -%}
    ADD FLOWFILTER:
    {#- --- 必选参数 --- -#}
    FLOWFILTERNAME="{{item.FLOWFILTERNAME}}",
    ;
{%- endfor -%}
```

#### 3.3 绑定三四层过滤条件。

```jinja2
{%- for item in add_fltbindflowf_list -%}
    ADD FLTBINDFLOWF:
    {#- --- 必选参数 --- -#}
    FLOWFILTERNAME="{{item.FLOWFILTERNAME}}",
    FILTERNAME="{{item.FILTERNAME}}",
    ;
{%- endfor -%}
```

### 4 配置内容计费使用的规则。

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
    {#- --- 条件必选：FILTERINGMODE=FLOWFILTER 时必选 --- -#}
    {%- if item.FILTERINGMODE == 'FLOWFILTER' -%}
        FLOWFILTERNAME="{{item.FLOWFILTERNAME}}",
    {%- endif -%}
    {#- --- 条件必选：POLICYTYPE=PCC/BWM/HEADEN/SMARTREDIRECT/TRAFFICCLASS/FIREWALL/QOS/WEBPROXY 时必选 --- -#}
    {%- if item.POLICYTYPE in ['PCC', 'BWM', 'HEADEN', 'SMARTREDIRECT', 'TRAFFICCLASS', 'FIREWALL', 'QOS', 'WEBPROXY'] -%}
        POLICYNAME="{{item.POLICYNAME}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in set_refreshsrv_list -%}
    SET REFRESHSRV:
    {#- --- 必选参数 --- -#}
    REFRESHTYPE={{item.REFRESHTYPE}},
    ;
{%- endfor -%}
```

### 5 配置内容计费规则绑定用户模板。

#### 5.1 创建UserProfile实例。

```jinja2
{%- for item in add_userprofile_list -%}
    ADD USERPROFILE:
    {#- --- 必选参数 --- -#}
    USERPROFILENAME="{{item.USERPROFILENAME}}",
    ;
{%- endfor -%}
```

#### 5.2 将已配置的内容计费规则绑定到UserProfile。

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

### 6 **可选**：设置全局默认配额开关。

```jinja2
{%- if is_optional_set_global_default_quota_switch -%}
    {%- for item in set_updefaultquota_list -%}
        SET UPDEFAULTQUOTA:
        {#- --- 必选参数 --- -#}
        USERTYPE={{item.USERTYPE}},
        DFTQTSWITCH={{item.DFTQTSWITCH}},
        ;
    {%- endfor -%}
{%- endif -%}
```

### 新业务触发申请配额期间是否允许使用默认配额由**SET UPDEFAULTQUOTA**命令控制。

#### 6.1 使能情况下使用**ADD URR**配置的默认配额正常处理报文。

#### 6.2 不使能情况下根据**SET UPGLBCHGPARA**命令决定缓存报文或者丢弃报文。

### 7 可选：设置全局Credit Pooling功能开关。

```jinja2
{%- if is_optional_set_global_credit_pooling_switch -%}
    SET UPGLBCHGPARA:
    ;
{%- endif -%}
```

#### 7.1 是否使能Credit Pooling功能由**SET UPGLBCHGPARA**命令的参数**CREDITPOOLSW**控制。

#### 7.2 该功能与DefaultQuota功能不能同时使用。

### 8 **可选**：设置URR上报失败后的动作处理参数。

```jinja2
{%- if is_optional_set_urr_failaction -%}
    SET URRFAILACTION:
    ;
{%- endif -%}
```

#### 8.1 该命令在在线计费需要申请配额的场景下生效。

#### 8.2 当业务部署调整导致PGW-U上的URR ID在GGSN/PGW-C上不存在时(比如，先添加PGW-U上**ADD URR**，后添加GGSN/PGW-C上**ADD URR**)，会导致GGSN/PGW-C无法处理PGW-U的计费用量上报。为减小该场景下对用户业务的影响，可通过该命令设置PGW-U向GGSN/PGW-C进行计费用量上报失败时的处理动作。

#### 8.3 当计费URR上报失败，业务被阻塞时，如果想要放通业务，可以执行**SET URRFAILACTION**命令，配置“RETRYFAILACT”参数为“CONTINUE”，则URR对应的业务将不计费。在PGW-U向GGSN/PGW-C进行用量上报恢复后，将恢复对该URR的计费。


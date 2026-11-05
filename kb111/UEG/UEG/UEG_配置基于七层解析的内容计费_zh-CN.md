---
id: ''
name: 配置基于七层解析的内容计费
ne_type: UEG
type: feature
description: UEG通过对用户七层数据报文进行分析和检测，对于匹配到规则的业务采取相应的计费策略。  此配置实例以离线计费为例，进行七层业务的内容计费配置。  适用于SGW-U、PGW-U、UPF。
tags: []
risk_level: ''
doc_source: ["网络部署","园区入驻式（仅连接）","5GC toB 部署边缘站点（站点为“风筝S”，入驻式）","裸机容器模式","配置业务数据（风筝S）","计费功能","配置基于七层解析的内容计费"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
UEG通过对用户七层数据报文进行分析和检测，对于匹配到规则的业务采取相应的计费策略。此配置实例以离线计费为例，进行七层业务的内容计费配置。适用于SGW-U、PGW-U、UPF。

## 必备事项
前提条件

请仔细阅读GWFD-022102 内容计费基本功能。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    add_urr_list:
      type: items
      properties:
        URRNAME:
          name: '使用量上报规则名称'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: '使用量上报规则信息。'
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
    add_urrgroup_list:
      type: items
      properties:
        URRGROUPNAME:
          name: '使用量上报规则组名称'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: '-'
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
          data_source: '从已配置数据中获取'
          pattern: ''
          default: ''
        DOWNURRNAME1:
          name: '下行发起URR名称1'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: ''
          data_source: '从已配置数据中获取'
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
          data_source: '从已配置数据中获取'
          pattern: ''
          default: ''
    add_l7filter_list:
      type: items
      properties:
        L7FILTERNAME:
          name: '七层过滤器名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '配置7层过滤条件。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SUBL7FLTNAME:
          name: '子七层过滤器名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        URL:
          name: 'URL'
          type: string
          minLength: 0
          maxLength: 119
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        URLTYPE:
          name: 'URL类型'
          type: string
          enum:
          - HOST
          - URL
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: URL
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
    add_protbindflowf_list:
      type: items
      properties:
        FLOWFILTERNAME:
          name: '流过滤器名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '流过滤器名称已通过**ADD FLOWFILTER**命令配置。'
          data_source: '从已配置数据中获取'
          pattern: ''
          default: ''
        PROTOCOLNAME:
          name: '协议名称'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: '绑定的七层协议。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        L7FILTERNAME:
          name: '七层过滤器名字'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: '七层过滤器名字已通过**ADD L7FILTER**命令配置。'
          data_source: '从已配置数据中获取'
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
          description: '使用的内容计费规则。'
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
          data_source: '从已配置数据中获取'
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
    add_userprofile_list:
      type: items
      properties:
        USERPROFILENAME:
          name: '用户模板名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '-'
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
          data_source: ''
          pattern: ''
          default: ''
        RULENAME:
          name: '规则名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: 'UserProfile绑定的业务规则，已通过**ADD RULE**命令配置完成。'
          data_source: '从已配置数据中获取'
          pattern: ''
          default: ''
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
  examples:
    add_urr_list:
    - URRNAME: 'urr_red'
      URRID: '01'
      USAGERPTMODE: ONLINE
    add_urrgroup_list:
    - URRGROUPNAME: 'cp_red'
      UPURRNAME1: 'urr_red'
      DOWNURRNAME1: 'urr_red'
    add_pccpolicygrp_list:
    - PCCPOLICYGRPNM: 'cg_red'
      URRGROUPNAME: 'cp_red'
    add_l7filter_list:
    - L7FILTERNAME: 'l7-test'
      SUBL7FLTNAME: 'sl7-test'
      URL: 'www.huawei.com'
      URLTYPE: URL
    add_flowfilter_list:
    - FLOWFILTERNAME: 'fg_red'
    add_protbindflowf_list:
    - FLOWFILTERNAME: 'fg_red'
      PROTOCOLNAME: 'http'
      L7FILTERNAME: 'l7-test'
    add_rule_list:
    - RULENAME: 'rule_red'
      POLICYTYPE: PCC
      FILTERINGMODE: FLOWFILTER
      FLOWFILTERNAME: 'fg_red'
      POLICYNAME: 'cg_red'
    add_userprofile_list:
    - USERPROFILENAME: 'up_test'
    add_rulebinding_list:
    - USERPROFILENAME: 'up_test'
      RULENAME: 'rule_red'
    set_refreshsrv_list:
    - REFRESHTYPE: USERPROFILE
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 配置基于七层解析的内容计费。

### 配置内容计费使用的URR Group。

#### 1.1 配置URR。

```jinja2
{%- for item in add_urr_list -%}
    ADD URR:
    {#- --- 必选参数 --- -#}
    URRNAME="{{item.URRNAME}}",
    URRID={{item.URRID}},
    USAGERPTMODE={{item.USAGERPTMODE}},
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

#### 3.1 配置七层过滤条件。

```jinja2
{%- for item in add_l7filter_list -%}
    ADD L7FILTER:
    {#- --- 必选参数 --- -#}
    L7FILTERNAME="{{item.L7FILTERNAME}}",
    SUBL7FLTNAME="{{item.SUBL7FLTNAME}}",
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：URLTYPE=URL 时可选 --- -#}
    {%- if item.URLTYPE == 'URL' -%}
        {%- if item.URL is not none -%}
            URL="{{item.URL}}",
        {%- endif -%}
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

#### 3.3 绑定七层过滤条件。

```jinja2
{%- for item in add_protbindflowf_list -%}
    ADD PROTBINDFLOWF:
    {#- --- 必选参数 --- -#}
    FLOWFILTERNAME="{{item.FLOWFILTERNAME}}",
    PROTOCOLNAME="{{item.PROTOCOLNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.L7FILTERNAME is not none -%}
        L7FILTERNAME="{{item.L7FILTERNAME}}",
    {%- endif -%}
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


---
id: GWFD-110283
name: 激活DNS纠错
ne_type: UDG
type: feature
description: 运营商规划要求用户在访问internet时出现页面不存在的情况下，能引导用户访问第三方Platform，则需要在UDG上部署DNS纠错功能。  适用于PGW-U、UPF。
risk_level: ''
doc_source: ["特性部署","特性指南","UDG特性指南","智能策略控制功能","GWFD-110283 DNS纠错","激活DNS纠错"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
运营商规划要求用户在访问internet时出现页面不存在的情况下，能引导用户访问第三方Platform，则需要在UDG上部署DNS纠错功能。适用于PGW-U、UPF。

## 必备事项
前提条件

* 请仔细阅读GWFD-110283 DNS纠错。
* 完成激活PCC基本功能。
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
    lod_signaturedb_list:
      type: items
      properties:
        LOADMODE:
          name: '特征库加载模式'
          type: string
          enum:
          - LATEST
          - REFRESH
          - SPECIFIC
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        VERSION:
          name: '特征库版本号'
          type: string
          minLength: 0
          maxLength: 16
          required: false
          description: ''
          data_source: '本端规划'
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
          description: '53为DNS Server的端口号。'
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
          data_source: '与对端协商'
          pattern: ''
          default: 0
        SVRENDPORT:
          name: '服务器结束端口号'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: '与对端协商'
          pattern: ''
          default: 65535
        L34PROTNUM:
          name: '三四层协议数字类型'
          type: integer
          minimum: 0
          maximum: 255
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
          minLength: 0
          maxLength: 63
          required: true
          description: '-'
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
          description: '已通过**ADD FLOWFILTER**命令配置，可以使用**LST FLOWFILTER**查询。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        FILTERNAME:
          name: '过滤器名字'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '已通过**ADD FILTER**命令配置，可以使用**LST FILTER**查询。'
          data_source: '已配置数据中获取'
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
    add_extendedfilter_list:
      type: items
      properties:
        EXTFLTNAME:
          name: '扩展过滤器名字'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: '-'
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
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_errorcode_list:
      type: items
      properties:
        ERRORCODENAME:
          name: '错误码名称'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        ERRORCODEOP:
          name: '错误码范围操作码'
          type: string
          enum:
          - EQUAL
          - GT
          - LT
          - RANGE
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        ERRORCODESTART:
          name: '错误码范围起始值'
          type: integer
          minimum: 0
          maximum: 1000
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        ERRORCODEEND:
          name: '错误码范围终止值'
          type: integer
          minimum: 0
          maximum: 1000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_dnsoverwriting_list:
      type: items
      properties:
        DNSOVERWRTNAME:
          name: 'DNS重写动作名字'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        EXTFLTTYPE1:
          name: '扩展过滤器类型1'
          type: string
          enum:
          - AND
          - NOT
          - OR
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        EXTFLTNAME1:
          name: '扩展过滤器名称1'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: '已通过**ADD EXTENDEDFILTER**命令配置，可以使用**LST EXTENDEDFILTER**查询。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        SERVERIP1:
          name: '服务器IPv4地址1'
          type: string
          maxLength: 15
          required: false
          description: '服务器IPv4地址是第三方Platform的IP地址。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        BINDERRCODENAME:
          name: '绑定错误码名称'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: '已通过**ADD ERRORCODE**命令配置，可以使用**LST ERRORCODE**查询。'
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
          description: '-'
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
        FILTERINGMODE:
          name: '流过滤器或流过滤器组选择'
          type: string
          enum:
          - FLOWFILTER
          - FLOWFILTERGRP
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        FLOWFILTERNAME:
          name: '流过滤器名称'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: '已通过**ADD FLOWFILTER**命令配置，可以使用**LST FLOWFILTER**查询。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        PRIORITY:
          name: '全局优先级'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: 4294967295
        POLICYNAME:
          name: '策略名称'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: '已通过**ADD DNSOVERWRITING**命令配置，可以使用**LST DNSOVERWRITING**查询。'
          data_source: '已配置数据中获取'
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
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV3G5DNSO01'
      SWITCH: ENABLE
    lod_signaturedb_list:
    - LOADMODE: SPECIFIC
      VERSION: '01.0002.0358.01'
    add_filter_list:
    - FILTERNAME: 'filter1'
      L34PROTTYPE: STRING
      L34PROTOCOL: UDP
      SVRSTARTPORT: 53
      SVRENDPORT: 53
      L34PROTNUM: ''
    add_flowfilter_list:
    - FLOWFILTERNAME: 'flow-filter1'
    add_fltbindflowf_list:
    - FLOWFILTERNAME: 'flow-filter1'
      FILTERNAME: 'filter1'
    set_refreshsrv_list:
    - REFRESHTYPE: USERPROFILE
    add_extendedfilter_list:
    - EXTFLTNAME: 'l7-filter1'
      URL: 'www.example.com/*'
    add_errorcode_list:
    - ERRORCODENAME: 'dnserrorcode'
      ERRORCODEOP: EQUAL
      ERRORCODESTART: 3
      ERRORCODEEND: ''
    add_dnsoverwriting_list:
    - DNSOVERWRTNAME: 'dec_1'
      EXTFLTTYPE1: AND
      EXTFLTNAME1: 'l7-filter1'
      SERVERIP1: '192.168.1.1'
      BINDERRCODENAME: 'dnserrorcode'
    add_rule_list:
    - RULENAME: 'testrule'
      POLICYTYPE: SMARTREDIRECT
      FILTERINGMODE: FLOWFILTER
      FLOWFILTERNAME: 'flow-filter1'
      PRIORITY: 20
      POLICYNAME: 'dec_1'
      FLWFLTRGRPNAME: ''
      ADCMUTEFLAG: ENABLE
      ALGSWITCH: DISABLE
      RDSTRIGGERFLAG: DISABLE
      REDIRIPVERFLAG: ''
      REMARKFPISEL: REMARK
      SRVLBOFLAG: DISABLE
      WORKERNAME: ''
      WORKERPARA: ''
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 打开本特性的License配置开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

### 2 **可选：**解析七层协议时，需要加载协议特征库文件。

```jinja2
{%- if is_optional_load_protocol_signature_file -%}
    {%- for item in lod_signaturedb_list -%}
        LOD SIGNATUREDB:
        {#- --- 必选参数 --- -#}
        LOADMODE={{item.LOADMODE}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：LOADMODE=SPECIFIC 时必选 --- -#}
        {%- if item.LOADMODE == 'SPECIFIC' -%}
            VERSION="{{item.VERSION}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 如果已经加载协议特征库文件，则使用本命令升级到最新版本的协议特征库文件。

### 3 配置DNS纠错业务使用的三四层过滤条件。

#### 3.1 配置DNS纠错业务使用的三四层过滤规则。

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
    {#- --- 条件必选：L34PROTTYPE=NUMBER 时必选 --- -#}
    {%- if item.L34PROTTYPE == 'NUMBER' -%}
        L34PROTNUM={{item.L34PROTNUM}},
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

#### 3.3 绑定三四层过滤信息。

```jinja2
{%- for item in add_fltbindflowf_list -%}
    ADD FLTBINDFLOWF:
    {#- --- 必选参数 --- -#}
    FLOWFILTERNAME="{{item.FLOWFILTERNAME}}",
    FILTERNAME="{{item.FILTERNAME}}",
    ;
{%- endfor -%}
```

#### 3.4 将新配置的Filter置为生效。

```jinja2
{%- for item in set_refreshsrv_list -%}
    SET REFRESHSRV:
    {#- --- 必选参数 --- -#}
    REFRESHTYPE={{item.REFRESHTYPE}},
    ;
{%- endfor -%}
```

### 4 配置DNS纠错使用的扩展过滤器。

```jinja2
{%- for item in add_extendedfilter_list -%}
    ADD EXTENDEDFILTER:
    {#- --- 必选参数 --- -#}
    EXTFLTNAME="{{item.EXTFLTNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.URL is not none -%}
        URL="{{item.URL}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 重复执行本步骤可以增加多个不同过滤条件的扩展过滤器。

### 5 配置DNS错误码。

```jinja2
{%- for item in add_errorcode_list -%}
    ADD ERRORCODE:
    {#- --- 必选参数 --- -#}
    ERRORCODENAME="{{item.ERRORCODENAME}}",
    ERRORCODEOP={{item.ERRORCODEOP}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：ERRORCODEOP=EQUAL/GT/RANGE 时必选 --- -#}
    {%- if item.ERRORCODEOP in ['EQUAL', 'GT', 'RANGE'] -%}
        ERRORCODESTART={{item.ERRORCODESTART}},
    {%- endif -%}
    {#- --- 条件必选：ERRORCODEOP=LT/RANGE 时必选 --- -#}
    {%- if item.ERRORCODEOP in ['LT', 'RANGE'] -%}
        ERRORCODEEND={{item.ERRORCODEEND}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 6 配置DNS纠错动作策略。

```jinja2
{%- for item in add_dnsoverwriting_list -%}
    ADD DNSOVERWRITING:
    {#- --- 必选参数 --- -#}
    DNSOVERWRTNAME="{{item.DNSOVERWRTNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.EXTFLTTYPE1 is not none -%}
        EXTFLTTYPE1={{item.EXTFLTTYPE1}},
    {%- endif -%}
    {%- if item.EXTFLTNAME1 is not none -%}
        EXTFLTNAME1="{{item.EXTFLTNAME1}}",
    {%- endif -%}
    {%- if item.SERVERIP1 is not none -%}
        SERVERIP1="{{item.SERVERIP1}}",
    {%- endif -%}
    {%- if item.BINDERRCODENAME is not none -%}
        BINDERRCODENAME="{{item.BINDERRCODENAME}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 7 配置DNS纠错使用的业务规则。

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
    {#- --- 条件必选：POLICYTYPE=ADC 时必选 --- -#}
    {%- if item.POLICYTYPE == 'ADC' -%}
        ADCMUTEFLAG={{item.ADCMUTEFLAG}},
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

### 如果运营商希望基于流过滤器组设置过滤条件时，配置“流过滤器或流过滤器组选择(FILTERINGMODE)”为“FLOWFILTERGRP”，并且使用**ADD FLOWFILTERGRP**命令配置流过滤器组。


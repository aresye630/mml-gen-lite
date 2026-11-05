---
id: GWFD-110331
name: 激活基于业务流标识的无线资源优化
ne_type: UDG
type: feature
description: 运营商通过综合业务保障级别、业务签约及用户级别等信息规划业务流优先级，需要激活基于业务流标识的无线资源优化功能。  适用于PGW-U、UPF。
risk_level: ''
doc_source: ["特性部署","特性指南","UDG特性指南","智能策略控制功能","GWFD-110331 基于业务流标识的无线资源优化","激活基于业务流标识的无线资源优化"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
运营商通过综合业务保障级别、业务签约及用户级别等信息规划业务流优先级，需要激活基于业务流标识的无线资源优化功能。适用于PGW-U、UPF。

## 必备事项
前提条件

* 请仔细阅读GWFD-110331 基于业务流标识的无线资源优化。
* 完成**加载License**（如果有需求，请联系华为技术支持工程师处理）。
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
    set_fpifunc_list:
      type: items
      properties:
        FPISWITCH:
          name: 'FPI使能开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: true
          description: '用于使能FPI功能，设置FPI的传递方式等内容。开启本功能后，要求无线侧同时也支持该功能。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        FPITRANSMETHOD:
          name: 'FPI传递类型'
          type: string
          enum:
          - GTPU
          - DSCP
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        FPIPOLICYORIGIN:
          name: '策略来源'
          type: string
          enum:
          - INTERNAL
          - EXTERNAL
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_saifunc_list:
      type: items
      properties:
        SWITCH:
          name: '功能开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: true
          description: '用于使能SAI功能。开启本功能后，要求无线侧同时也支持该功能。'
          data_source: '全网规划'
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
          description: 'UDG通过将用户上下行报文匹配Filter，实现三四层报文的分析，从而过滤出会触发内容感知的数据报文。'
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
          description: '用于绑定Filter的FlowFilter。'
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
          name: '过滤器名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: ''
          data_source: ''
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
    add_pccactionprop_list:
      type: items
      properties:
        PCCACTPROPNAME:
          name: 'PCC动作属性名称'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: '配置PCC动作属性。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        UPINITDNGATE:
          name: '上行发起下行门控'
          type: string
          enum:
          - DISCARD
          - PASS
          required: false
          description: 'FPI规则携带在下行数据报文中，因此下行数据需要配置为直接通过。上下行动作使用**ADD PCCACTIONPROP**命令中配置的动作。'
          data_source: '本端规划'
          pattern: ''
          default: PASS
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
          description: '已通过****ADD URRGROUP****命令配置计费属性。'
          data_source: '从已配置数据中获取'
          pattern: ''
          default: ''
        PCCACTPROPNAME:
          name: 'PCC动作属性名称'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: '分类组绑定的动作属性，已通过**ADD PCCACTIONPROP**命令配置完成，可以通过**LST PCCACTIONPROP**命令查询。'
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
          description: '配置业务规则。'
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
          description: '规则绑定的流过滤器。已通过**ADD FLOWFILTER**命令配置完成，可以使用**LST FLOWFILTER**命令进行查询。'
          data_source: '从已配置数据中获取'
          pattern: ''
          default: ''
        PRIORITY:
          name: '全局优先级'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 4294967295
        POLICYNAME:
          name: '策略名称'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: '规则绑定的策略。已通过**ADD PCCPOLICYGRP**命令配置完成，可以使用**LST PCCPOLICYGRP**命令进行查询。'
          data_source: '从已配置数据中获取'
          pattern: ''
          default: ''
        REMARKFPISEL:
          name: '重标记或FPI选择'
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
          description: '配置FPI业务规则。'
          data_source: '本端规划'
          pattern: ''
          default: REMARK
        FPIVALUE:
          name: 'FPI值'
          type: integer
          minimum: 0
          maximum: 255
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        SAIVALUE:
          name: 'SAI值'
          type: integer
          minimum: 1
          maximum: 39
          required: false
          description: ''
          data_source: '本端规划'
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
        REMARKCFGTYPE:
          name: 'Remark配置类型'
          type: string
          enum:
          - CLASS
          - DSCP
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: CLASS
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV3G5WOFR01'
      SWITCH: ENABLE
    set_fpifunc_list:
    - FPISWITCH: ENABLE
      FPITRANSMETHOD: DSCP
      FPIPOLICYORIGIN: INTERNAL
    set_saifunc_list:
    - SWITCH: ENABLE
    add_filter_list:
    - FILTERNAME: 'filter_test'
      L34PROTTYPE: STRING
      L34PROTOCOL: TCP
      L34PROTNUM: ''
    add_flowfilter_list:
    - FLOWFILTERNAME: 'ff_test'
    add_fltbindflowf_list:
    - FLOWFILTERNAME: 'ff_test'
      FILTERNAME: 'filter_test'
    set_refreshsrv_list:
    - REFRESHTYPE: ALL
    add_pccactionprop_list:
    - PCCACTPROPNAME: 'pap_test'
      UPINITDNGATE: PASS
    add_pccpolicygrp_list:
    - PCCPOLICYGRPNM: 'ppg_test'
      URRGROUPNAME: 'urrgp_test'
      PCCACTPROPNAME: 'pap_test'
    add_rule_list:
    - RULENAME: 'rule_test1'
      POLICYTYPE: PCC
      FILTERINGMODE: FLOWFILTER
      FLOWFILTERNAME: 'ff_test'
      PRIORITY: 1
      POLICYNAME: 'ppg_test'
      REMARKFPISEL: FPI
      FPIVALUE: 63
      SAIVALUE: 25
      FLWFLTRGRPNAME: ''
      ADCMUTEFLAG: ENABLE
      ALGSWITCH: DISABLE
      RDSTRIGGERFLAG: DISABLE
      REDIRIPVERFLAG: ''
      SRVLBOFLAG: DISABLE
      WORKERNAME: ''
      WORKERPARA: ''
      REMARKCFGTYPE: CLASS
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

### 2 配置FPI使能开关，选择资源优化方法。

```jinja2
{%- for item in set_fpifunc_list -%}
    SET FPIFUNC:
    {#- --- 必选参数 --- -#}
    FPISWITCH={{item.FPISWITCH}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：FPISWITCH=ENABLE 时必选 --- -#}
    {%- if item.FPISWITCH == 'ENABLE' -%}
        FPITRANSMETHOD={{item.FPITRANSMETHOD}},
    {%- endif -%}
    {#- --- 条件必选：FPITRANSMETHOD=GTPU 时必选 --- -#}
    {%- if item.FPITRANSMETHOD == 'GTPU' -%}
        FPIPOLICYORIGIN={{item.FPIPOLICYORIGIN}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 配置SAI使能开关。

```jinja2
{%- for item in set_saifunc_list -%}
    SET SAIFUNC:
    {#- --- 必选参数 --- -#}
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

### 4 配置三四层过滤规则。

#### 4.1 配置业务使用的三四层过滤规则为TCP项。

```jinja2
{%- for item in add_filter_list -%}
    ADD FILTER:
    {#- --- 必选参数 --- -#}
    FILTERNAME="{{item.FILTERNAME}}",
    L34PROTTYPE={{item.L34PROTTYPE}},
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

#### 4.2 配置流过滤器。

```jinja2
{%- for item in add_flowfilter_list -%}
    ADD FLOWFILTER:
    {#- --- 必选参数 --- -#}
    FLOWFILTERNAME="{{item.FLOWFILTERNAME}}",
    ;
{%- endfor -%}
```

#### 4.3 流过滤器绑定过滤器。

```jinja2
{%- for item in add_fltbindflowf_list -%}
    ADD FLTBINDFLOWF:
    {#- --- 必选参数 --- -#}
    FLOWFILTERNAME="{{item.FLOWFILTERNAME}}",
    FILTERNAME="{{item.FILTERNAME}}",
    ;
{%- endfor -%}
```

#### 4.4 将新配置的Filter置为生效。

```jinja2
{%- for item in set_refreshsrv_list -%}
    SET REFRESHSRV:
    {#- --- 必选参数 --- -#}
    REFRESHTYPE={{item.REFRESHTYPE}},
    ;
{%- endfor -%}
```

### 5 配置PCC动作属性。

```jinja2
{%- for item in add_pccactionprop_list -%}
    ADD PCCACTIONPROP:
    {#- --- 必选参数 --- -#}
    PCCACTPROPNAME="{{item.PCCACTPROPNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.UPINITDNGATE is not none -%}
        UPINITDNGATE={{item.UPINITDNGATE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 6 配置PCC策略组。

```jinja2
{%- for item in add_pccpolicygrp_list -%}
    ADD PCCPOLICYGRP:
    {#- --- 必选参数 --- -#}
    PCCPOLICYGRPNM="{{item.PCCPOLICYGRPNM}}",
    {#- --- 可选参数 --- -#}
    {%- if item.PCCACTPROPNAME is not none -%}
        PCCACTPROPNAME="{{item.PCCACTPROPNAME}}",
    {%- endif -%}
    {%- if item.URRGROUPNAME is not none -%}
        URRGROUPNAME="{{item.URRGROUPNAME}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 7 配置业务规则。

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
    {#- --- 条件必选：POLICYTYPE=REMARK_FPI 时必选 --- -#}
    {%- if item.POLICYTYPE == 'REMARK_FPI' -%}
        REMARKFPISEL={{item.REMARKFPISEL}},
    {%- endif -%}
    {#- --- 条件必选：REMARKFPISEL=FPI/REMARKANDFPI/FPIANDSAI/RMKFPISAI 时必选 --- -#}
    {%- if item.REMARKFPISEL in ['FPI', 'REMARKANDFPI', 'FPIANDSAI', 'RMKFPISAI'] -%}
        FPIVALUE={{item.FPIVALUE}},
    {%- endif -%}
    {#- --- 条件必选：REMARKFPISEL=SAI/REMARKANDSAI/FPIANDSAI/RMKFPISAI 时必选 --- -#}
    {%- if item.REMARKFPISEL in ['SAI', 'REMARKANDSAI', 'FPIANDSAI', 'RMKFPISAI'] -%}
        SAIVALUE={{item.SAIVALUE}},
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
    {#- --- 条件必选：REMARKFPISEL=REMARK/REMARKANDFPI/REMARKANDSAI/RMKFPISAI 时必选 --- -#}
    {%- if item.REMARKFPISEL in ['REMARK', 'REMARKANDFPI', 'REMARKANDSAI', 'RMKFPISAI'] -%}
        REMARKCFGTYPE={{item.REMARKCFGTYPE}},
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


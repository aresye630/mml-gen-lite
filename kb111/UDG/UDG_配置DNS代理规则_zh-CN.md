---
id: ''
name: 配置DNS代理规则
ne_type: UDG
type: feature
description: 媒体中继业务中，UPF需要识别DNS请求中是否携带OTT规划的relay域名来作DNS代理，此时需要在UPF上配置对应的URL识别规则。
risk_level: ''
doc_source: ["特性部署","业务专题","5G Core 媒体中继解决方案","媒体中继业务配置","新建媒体中继基础配置","配置UPF","增加媒体服务商配置（基于OTT应用）","配置DNS代理规则"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
媒体中继业务中，UPF需要识别DNS请求中是否携带OTT规划的relay域名来作DNS代理，此时需要在UPF上配置对应的URL识别规则。

## 必备事项
前提条件

前提条件

已参考增加媒体服务商基础配置~配置内容计费规则完成媒体中继业务相关配置。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    add_filter_list:
      type: items
      properties:
        FILTERNAME:
          name: '过滤器名字'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '-'
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
          description: '-'
          data_source: '固定取值'
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
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: ANY
        MSSTARTPORT:
          name: '手机起始端口号'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: 0
        MSENDPORT:
          name: '手机结束端口号'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: 65535
        SVRSTARTPORT:
          name: '服务器起始端口号'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 0
        SVRENDPORT:
          name: '服务器结束端口号'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: '-'
          data_source: '固定取值'
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
    add_filteripv6_list:
      type: items
      properties:
        FILTERNAME:
          name: '过滤器名字'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        L34PROTTYPEV6:
          name: '三四层IPv6协议输入类型'
          type: string
          enum:
          - NUMBER
          - STRING
          required: true
          description: '-'
          data_source: '固定取值'
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
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: ANY
        SVRSTARTPORT:
          name: '服务器起始端口号'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 0
        SVRENDPORT:
          name: '服务器结束端口号'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: '-'
          data_source: '固定取值'
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
    add_l7filter_list:
      type: items
      properties:
        L7FILTERNAME:
          name: '七层过滤器名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SUBL7FLTNAME:
          name: '子七层过滤器名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '-'
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
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: URL
        URL:
          name: 'URL'
          type: string
          minLength: 0
          maxLength: 119
          required: false
          description: '与OTT厂商规划的直播、点播域名保持一致。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        METHODTYPE:
          name: '方法类型'
          type: string
          required: false
          description: '-'
          data_source: '与对端协商'
          pattern: ''
          default: ''
        ISREFEREREN:
          name: 'Referer关联计费开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: DISABLE
        MMSBLURMATCH:
          name: '彩信模糊匹配'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: DISABLE
        HOST:
          name: 'HOST'
          type: string
          minLength: 0
          maxLength: 119
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
        TETHERDETFLAG:
          name: 'Tethering检测标识'
          type: string
          enum:
          - DETECT_ONLY
          - FILTER
          - NONE
          - NOT_FILTER
          required: false
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: NONE
        FLOWFILTERTYPE:
          name: 'FlowFilter类型'
          type: string
          enum:
          - EXTEROTTDB
          - USERCONFIG
          required: false
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: USERCONFIG
        FILTERGRPNAME:
          name: '过滤器组名称'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: ''
          data_source: ''
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
          description: '已通过  **ADD FLOWFILTER**命令完成配置。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        FILTERNAME:
          name: '过滤器名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '已通过  **ADD FILTER**或**ADD FILTERIPV6**命令完成配置。'
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
          description: '已通过  **ADD FLOWFILTER**命令完成配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        PROTOCOLNAME:
          name: '协议名称'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: ''
        L7FILTERNAME:
          name: '七层过滤器名字'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: '已通过**ADD L7FILTER**命令完成配置。'
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
          description: '-'
          data_source: '固定取值'
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
          description: '已通过  **ADD FLOWFILTER**命令完成配置。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        WORKERNAME:
          name: '通用Rule子策略名称'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: ''
        WORKERPARA:
          name: '通用策略参数'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: '规则下绑定媒体中继模板，已通过**ADD RELAYTEMPLATE**命令完成配置。'
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
    add_rulebinding_list:
      type: items
      properties:
        USERPROFILENAME:
          name: '用户模板名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '与SMF下发的媒体中继业务套餐使用的预定义规则保持一致。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        RULENAME:
          name: '规则名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '已通过**ADD RULE**命令完成配置。'
          data_source: '已配置数据中获取'
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
          description: '-'
          data_source: '固定取值'
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
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: ''
  examples:
    add_filter_list:
    - FILTERNAME: 'relay_f_dns'
      L34PROTTYPE: STRING
      L34PROTOCOL: UDP
      MSSTARTPORT: 0
      MSENDPORT: 65535
      SVRSTARTPORT: 53
      SVRENDPORT: 53
      L34PROTNUM: ''
    add_filteripv6_list:
    - FILTERNAME: 'ipv6_relay_f_dns'
      L34PROTTYPEV6: STRING
      L34PROTOCOL: UDP
      SVRSTARTPORT: 53
      SVRENDPORT: 53
      L34PROTNUM: ''
    add_l7filter_list:
    - L7FILTERNAME: 'sp_relay_d_00_l7_f_001'
      SUBL7FLTNAME: 'sp_relay_d_00_sl7_f_100'
      URLTYPE: URL
      URL: 'relay.spliving.com'
      METHODTYPE: CONNECT-1&DELETE-1&GET-1&HEAD-1&OPTIONS-1&POST-1&PUT-1&TRACE-1
      ISREFEREREN: DISABLE
      MMSBLURMATCH: DISABLE
      HOST: ''
    add_flowfilter_list:
    - FLOWFILTERNAME: 'sp_relay_d_00_f_f_h_001'
      TETHERDETFLAG: NONE
      FLOWFILTERTYPE: USERCONFIG
      FILTERGRPNAME: ''
    add_fltbindflowf_list:
    - FLOWFILTERNAME: 'sp_relay_d_00_f_f_h_001'
      FILTERNAME: 'relay_f_dns'
    add_protbindflowf_list:
    - FLOWFILTERNAME: 'sp_relay_d_00_f_f_h_001'
      PROTOCOLNAME: 'dns'
      L7FILTERNAME: 'sp_relay_d_00_l7_f_001'
    add_rule_list:
    - RULENAME: 'sp_relay_d_00_r_h_001'
      POLICYTYPE: WORKER
      FILTERINGMODE: FLOWFILTER
      FLOWFILTERNAME: 'sp_relay_d_00_f_f_h_001'
      WORKERNAME: 'relay_dns'
      WORKERPARA: 'sp_relay_tpl'
      FLWFLTRGRPNAME: ''
      ADCMUTEFLAG: ENABLE
      ALGSWITCH: DISABLE
      POLICYNAME: ''
      RDSTRIGGERFLAG: DISABLE
      REDIRIPVERFLAG: ''
      REMARKFPISEL: REMARK
      SRVLBOFLAG: DISABLE
    add_rulebinding_list:
    - USERPROFILENAME: 'testuserprofilename'
      RULENAME: 'sp_relay_d_00_r_h_001'
      POLICYTYPE: WORKER
    set_refreshsrv_list:
    - REFRESHTYPE: USERPROFILE
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 //配置DNS代理的流过滤器。

```jinja2
{%- for item in add_filter_list -%}
    ADD FILTER:
    {#- --- 必选参数 --- -#}
    FILTERNAME="{{item.FILTERNAME}}",
    L34PROTTYPE={{item.L34PROTTYPE}},
    {#- --- 可选参数 --- -#}
    {%- if item.MSSTARTPORT is not none -%}
        MSSTARTPORT={{item.MSSTARTPORT}},
    {%- endif -%}
    {%- if item.MSENDPORT is not none -%}
        MSENDPORT={{item.MSENDPORT}},
    {%- endif -%}
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

```jinja2
{%- for item in add_filteripv6_list -%}
    ADD FILTERIPV6:
    {#- --- 必选参数 --- -#}
    FILTERNAME="{{item.FILTERNAME}}",
    L34PROTTYPEV6={{item.L34PROTTYPEV6}},
    {#- --- 可选参数 --- -#}
    {%- if item.SVRSTARTPORT is not none -%}
        SVRSTARTPORT={{item.SVRSTARTPORT}},
    {%- endif -%}
    {%- if item.SVRENDPORT is not none -%}
        SVRENDPORT={{item.SVRENDPORT}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：L34PROTTYPEV6=STRING 时必选 --- -#}
    {%- if item.L34PROTTYPEV6 == 'STRING' -%}
        L34PROTOCOL={{item.L34PROTOCOL}},
    {%- endif -%}
    {#- --- 条件必选：L34PROTTYPEV6=NUMBER 时必选 --- -#}
    {%- if item.L34PROTTYPEV6 == 'NUMBER' -%}
        L34PROTNUM={{item.L34PROTNUM}},
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_l7filter_list -%}
    ADD L7FILTER:
    {#- --- 必选参数 --- -#}
    L7FILTERNAME="{{item.L7FILTERNAME}}",
    SUBL7FLTNAME="{{item.SUBL7FLTNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.URLTYPE is not none -%}
        URLTYPE={{item.URLTYPE}},
    {%- endif -%}
    {%- if item.METHODTYPE is not none -%}
        METHODTYPE={{item.METHODTYPE}},
    {%- endif -%}
    {%- if item.ISREFEREREN is not none -%}
        ISREFEREREN={{item.ISREFEREREN}},
    {%- endif -%}
    {%- if item.MMSBLURMATCH is not none -%}
        MMSBLURMATCH={{item.MMSBLURMATCH}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：URLTYPE=URL 时可选 --- -#}
    {%- if item.URLTYPE == 'URL' -%}
        {%- if item.URL is not none -%}
            URL="{{item.URL}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：URLTYPE=HOST 时可选 --- -#}
    {%- if item.URLTYPE == 'HOST' -%}
        {%- if item.HOST is not none -%}
            HOST="{{item.HOST}}",
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 2 //增加域名DNS代理规则流过滤器。

```jinja2
{%- for item in add_flowfilter_list -%}
    ADD FLOWFILTER:
    {#- --- 必选参数 --- -#}
    FLOWFILTERNAME="{{item.FLOWFILTERNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.TETHERDETFLAG is not none -%}
        TETHERDETFLAG={{item.TETHERDETFLAG}},
    {%- endif -%}
    {%- if item.FLOWFILTERTYPE is not none -%}
        FLOWFILTERTYPE={{item.FLOWFILTERTYPE}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：FLOWFILTERTYPE=USERCONFIG 时可选 --- -#}
    {%- if item.FLOWFILTERTYPE == 'USERCONFIG' -%}
        {%- if item.FILTERGRPNAME is not none -%}
            FILTERGRPNAME="{{item.FILTERGRPNAME}}",
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_fltbindflowf_list -%}
    ADD FLTBINDFLOWF:
    {#- --- 必选参数 --- -#}
    FLOWFILTERNAME="{{item.FLOWFILTERNAME}}",
    FILTERNAME="{{item.FILTERNAME}}",
    ;
{%- endfor -%}
```

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

### 3 //配置DNS代理规则并绑定到媒体中继签约套餐。

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
    {#- --- 条件必选：POLICYTYPE=WORKER 时必选 --- -#}
    {%- if item.POLICYTYPE == 'WORKER' -%}
        WORKERNAME="{{item.WORKERNAME}}",
    {%- endif -%}
    {#- --- 条件必选：POLICYTYPE=ADC 时必选 --- -#}
    {%- if item.POLICYTYPE == 'ADC' -%}
        ADCMUTEFLAG={{item.ADCMUTEFLAG}},
    {%- endif -%}
    {#- --- 条件必选：FILTERINGMODE=FLOWFILTERGRP 时必选 --- -#}
    {%- if item.FILTERINGMODE == 'FLOWFILTERGRP' -%}
        FLWFLTRGRPNAME="{{item.FLWFLTRGRPNAME}}",
    {%- endif -%}
    {#- --- 条件必选：POLICYTYPE=PCC/BWM/HEADEN/SMARTREDIRECT/TRAFFICCLASS/FIREWALL/QOS/WEBPROXY 时必选 --- -#}
    {%- if item.POLICYTYPE in ['PCC', 'BWM', 'HEADEN', 'SMARTREDIRECT', 'TRAFFICCLASS', 'FIREWALL', 'QOS', 'WEBPROXY'] -%}
        POLICYNAME="{{item.POLICYNAME}}",
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
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：POLICYTYPE=WORKER 时可选 --- -#}
    {%- if item.POLICYTYPE == 'WORKER' -%}
        {%- if item.WORKERPARA is not none -%}
            WORKERPARA="{{item.WORKERPARA}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：POLICYTYPE=WEBPROXY 时可选 --- -#}
    {%- if item.POLICYTYPE == 'WEBPROXY' -%}
        {%- if item.ALGSWITCH is not none -%}
            ALGSWITCH={{item.ALGSWITCH}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
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

### 4 //执行配置刷新操作，生效媒体中继DNS代理规则

```jinja2
{%- for item in set_refreshsrv_list -%}
    SET REFRESHSRV:
    {#- --- 必选参数 --- -#}
    REFRESHTYPE={{item.REFRESHTYPE}},
    ;
{%- endfor -%}
```


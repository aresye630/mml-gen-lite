---
id: GWFD-022307
name: 配置七层业务触发的QOS保证（PGW-U、UPF）
ne_type: UEG
type: feature
description: 当运营商规划了为某类需要QoS保证的业务提供专有承载/专有QoS Flow时，需要在UEG上配置基于七层的业务触发的QoS保证数据。  适用于PGW-U、UPF。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝L","MEC 特性指南（风筝L）","GW-U&UPF特性指南","GWFD-022300 智能QoS管理增强","GWFD-022307 业务触发的QoS保证","激活业务触发的QoS保证","配置七层业务触发的QOS保证（PGW-U、UPF）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
当运营商规划了为某类需要QoS保证的业务提供专有承载/专有QoS Flow时，需要在UEG上配置基于七层的业务触发的QoS保证数据。适用于PGW-U、UPF。

## 必备事项
前提条件

* 请仔细阅读GWFD-022307 业务触发的QoS保证。
* 完成加载license（如果有需求，请联系华为技术支持工程师处理）。
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
    add_filter_list:
      type: items
      properties:
        FILTERNAME:
          name: '过滤器名字'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: 'UEG通过将用户上下行报文匹配Filter，实现三四层报文的分析，从而过滤出会触发的数据报文。'
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
    add_l7filter_list:
      type: items
      properties:
        L7FILTERNAME:
          name: '七层过滤器名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '七层过滤条件。'
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
    add_fltbindflowf_list:
      type: items
      properties:
        FLOWFILTERNAME:
          name: '流过滤器名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '已通过**ADD FLOWFILTER**命令配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        FILTERNAME:
          name: '过滤器名字'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '绑定的三四层过滤条件已通过**ADD FILTER**命令配置，可以通过**LST FILTER**命令查询。'
          data_source: '已配置数据中获取'
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
          description: '已通过**ADD FLOWFILTER**命令配置。'
          data_source: '已配置数据中获取'
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
          description: '绑定的七层过滤条件已通过**ADD L7FILTER**命令配置，可以通过**LST L7FILTER**命令查询。'
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
    add_urr_list:
      type: items
      properties:
        URRNAME:
          name: '使用量上报规则名称'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: '增加用于QoS事件上报的规则。'
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
          data_source: '本端规划'
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
          data_source: '固定取值'
          pattern: ''
          default: ''
    add_qosprop_list:
      type: items
      properties:
        QOSPROPNAME:
          name: 'Qos属性名称'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        QOSURRNAME:
          name: 'QoS使用量上报规则名称'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GBRUPLKVALUE:
          name: '保证的上行比特率'
          type: integer
          minimum: 0
          maximum: 20000000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GBRDNLKVALUE:
          name: '保证的下行比特率'
          type: integer
          minimum: 0
          maximum: 20000000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MBRUPLKVALUE:
          name: '最大上行比特率'
          type: integer
          minimum: 0
          maximum: 20000000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MBRDNLKVALUE:
          name: '最大下行比特率'
          type: integer
          minimum: 0
          maximum: 20000000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        QBGRPT:
          name: '质差分析上报开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '* DISABLE：无需关联质差检测，匹配中QoS规则即可上报。 * ENABLE：业务触发专载时，当系统检测到QoS质差后触发上报。   该参数需要与**SET QOSURRRPTCTRL**命令的**QBGRPT**参数保持一致。'
          data_source: '全网规划'
          pattern: ''
          default: DISABLE
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
        QOSPROPNAME:
          name: 'Qos属性名称'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: 'QoS参数，已通过**ADD QOSPROP**命令配置完成。'
          data_source: '已配置数据中获取'
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
    add_wellknownport_list:
      type: items
      properties:
        IDENPROTNAME:
          name: '知名端口名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: 'HTTP协议的默认端口是80。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PROTOCOLNAME:
          name: '协议名称'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        PORTOP:
          name: '端口范围操作码'
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
        STARTPORT:
          name: '起始端口号'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        PRIORITY:
          name: '优先级'
          type: integer
          minimum: 1
          maximum: 65535
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_sadedicbearer_list:
      type: items
      properties:
        PROTOCOLLEVEL:
          name: '协议等级'
          type: string
          enum:
          - PROTOCOL
          - PROTOCOLGROUP
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PROTOCOLNAME:
          name: '协议名称'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        TRIGGERMODE:
          name: '触发专有承载模式'
          type: string
          enum:
          - DOWNLINK_ONLY
          - FLOWNODE_BASED
          - NOT_TRIGGER
          required: true
          description: ''
          data_source: '本端规划'
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
          description: '绑定的FlowFilter已通过**ADD FLOWFILTER**命令配置，可以通过**LST FLOWFILTER**命令查询。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        POLICYNAME:
          name: '策略名称'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: '绑定的PCC策略组已通过**ADD PCCPOLICYGRP**命令配置，可以通过**LST PCCPOLICYGRP**命令查询。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        PRIORITY:
          name: '全局优先级'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: false
          description: '指定rule的优先级。'
          data_source: '本端规划'
          pattern: ''
          default: 4294967295
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
          description: '使用**ADD USERPROFILE**命令定义的用户模板名称。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        RULENAME:
          name: '规则名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: 'UserProfile绑定的业务规则，已通过**ADD RULE**命令配置完成。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    set_upglbpmpara_list:
      type: items
      properties:
        FLOWDANYFMT:
          name: '流描述中Any IP地址格式'
          type: string
          enum:
          - ANYFMT
          - IPMASK
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV3G5STQE01'
      SWITCH: ENABLE
    add_filter_list:
    - FILTERNAME: 'filter_test'
      L34PROTTYPE: STRING
      L34PROTOCOL: ANY
    add_l7filter_list:
    - L7FILTERNAME: 'l7_test'
      SUBL7FLTNAME: 'subl7_test'
      URL: 'www.example.com*/*'
      URLTYPE: URL
    add_flowfilter_list:
    - FLOWFILTERNAME: 'flowfilter_test1'
    add_fltbindflowf_list:
    - FLOWFILTERNAME: 'flowfilter_test1'
      FILTERNAME: 'filter_test'
    add_protbindflowf_list:
    - FLOWFILTERNAME: 'flowfilter_test1'
      PROTOCOLNAME: 'http'
      L7FILTERNAME: 'l7_test'
    set_refreshsrv_list:
    - REFRESHTYPE: USERPROFILE
    add_urr_list:
    - URRNAME: 'urr_1'
      URRID: 1001
      USAGERPTMODE: QOS
    add_qosprop_list:
    - QOSPROPNAME: 'qos-property1'
      QOSURRNAME: 'urr_1'
      GBRUPLKVALUE: 110
      GBRDNLKVALUE: 110
      MBRUPLKVALUE: 220
      MBRDNLKVALUE: 220
      QBGRPT: DISABLE
    add_pccpolicygrp_list:
    - PCCPOLICYGRPNM: 'ppg1'
      QOSPROPNAME: 'qos-property1'
      URRGROUPNAME: 'urrgroup1'
    add_wellknownport_list:
    - IDENPROTNAME: 'http'
      PROTOCOLNAME: 'http'
      PORTOP: EQUAL
      STARTPORT: 80
      PRIORITY: 5
    add_sadedicbearer_list:
    - PROTOCOLLEVEL: PROTOCOL
      PROTOCOLNAME: 'http'
      TRIGGERMODE: DOWNLINK_ONLY
    add_rule_list:
    - RULENAME: 'rule_test'
      POLICYTYPE: PCC
      FILTERINGMODE: FLOWFILTER
      FLOWFILTERNAME: 'flowfilter_test1'
      POLICYNAME: 'ppg1'
      PRIORITY: 10
    add_userprofile_list:
    - USERPROFILENAME: 'up_test'
    add_rulebinding_list:
    - USERPROFILENAME: 'up_test'
      RULENAME: 'rule_test'
    set_upglbpmpara_list:
    - FLOWDANYFMT: AnyFMT
```

## 3 命令模板定义
<!-- @mml:block= commands -->

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

### 2 配置三四层过滤条件。

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
    ;
{%- endfor -%}
```

### 3 配置七层过滤条件。

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

### 4 配置流过滤器，绑定三四层、七层过滤条件。

#### 4.1 配置流过滤器。

```jinja2
{%- for item in add_flowfilter_list -%}
    ADD FLOWFILTER:
    {#- --- 必选参数 --- -#}
    FLOWFILTERNAME="{{item.FLOWFILTERNAME}}",
    ;
{%- endfor -%}
```

#### 4.2 配置三四层过滤条件与流过滤器的绑定关系。

```jinja2
{%- for item in add_fltbindflowf_list -%}
    ADD FLTBINDFLOWF:
    {#- --- 必选参数 --- -#}
    FLOWFILTERNAME="{{item.FLOWFILTERNAME}}",
    FILTERNAME="{{item.FILTERNAME}}",
    ;
{%- endfor -%}
```

#### 4.3 配置七层过滤条件与流过滤器的绑定关系。

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

#### 4.4 将新配置的Filter置为生效。

```jinja2
{%- for item in set_refreshsrv_list -%}
    SET REFRESHSRV:
    {#- --- 必选参数 --- -#}
    REFRESHTYPE={{item.REFRESHTYPE}},
    ;
{%- endfor -%}
```

### 5 配置QoS属性。

#### 5.1 配置QoS类型URR。

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

#### 5.2 配置QoS属性。

```jinja2
{%- for item in add_qosprop_list -%}
    ADD QOSPROP:
    {#- --- 必选参数 --- -#}
    QOSPROPNAME="{{item.QOSPROPNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.QOSURRNAME is not none -%}
        QOSURRNAME="{{item.QOSURRNAME}}",
    {%- endif -%}
    {%- if item.GBRUPLKVALUE is not none -%}
        GBRUPLKVALUE={{item.GBRUPLKVALUE}},
    {%- endif -%}
    {%- if item.GBRDNLKVALUE is not none -%}
        GBRDNLKVALUE={{item.GBRDNLKVALUE}},
    {%- endif -%}
    {%- if item.MBRUPLKVALUE is not none -%}
        MBRUPLKVALUE={{item.MBRUPLKVALUE}},
    {%- endif -%}
    {%- if item.MBRDNLKVALUE is not none -%}
        MBRDNLKVALUE={{item.MBRDNLKVALUE}},
    {%- endif -%}
    {%- if item.QBGRPT is not none -%}
        QBGRPT={{item.QBGRPT}},
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
    {%- if item.URRGROUPNAME is not none -%}
        URRGROUPNAME="{{item.URRGROUPNAME}}",
    {%- endif -%}
    {%- if item.QOSPROPNAME is not none -%}
        QOSPROPNAME="{{item.QOSPROPNAME}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 7 配置协议识别数据。

```jinja2
{%- for item in add_wellknownport_list -%}
    ADD WELLKNOWNPORT:
    {#- --- 必选参数 --- -#}
    IDENPROTNAME="{{item.IDENPROTNAME}}",
    PROTOCOLNAME="{{item.PROTOCOLNAME}}",
    PORTOP={{item.PORTOP}},
    PRIORITY={{item.PRIORITY}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：PORTOP=EQUAL/GT/RANGE 时必选 --- -#}
    {%- if item.PORTOP in ['EQUAL', 'GT', 'RANGE'] -%}
        STARTPORT={{item.STARTPORT}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 8 使能协议或协议组支持基于业务感知能力触发专有承载创建，并配置触发专有承载创建的模式。

```jinja2
{%- for item in add_sadedicbearer_list -%}
    ADD SADEDICBEARER:
    {#- --- 必选参数 --- -#}
    PROTOCOLLEVEL={{item.PROTOCOLLEVEL}},
    TRIGGERMODE={{item.TRIGGERMODE}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：PROTOCOLLEVEL=PROTOCOL 时必选 --- -#}
    {%- if item.PROTOCOLLEVEL == 'PROTOCOL' -%}
        PROTOCOLNAME="{{item.PROTOCOLNAME}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 9 配置业务规则。

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

### 如果运营商希望基于流过滤器组设置过滤条件时，配置“流过滤器或流过滤器组选择(FILTERINGMODE)”为“FLOWFILTERGRP”，并且使用**ADD FLOWFILTERGRP**命令配置流过滤器组。

### 10 配置业务策略组合。

#### 10.1 创建UserProfile。

```jinja2
{%- for item in add_userprofile_list -%}
    ADD USERPROFILE:
    {#- --- 必选参数 --- -#}
    USERPROFILENAME="{{item.USERPROFILENAME}}",
    ;
{%- endfor -%}
```

#### 10.2 将已配置的Rule绑定到UserProfile。

```jinja2
{%- for item in add_rulebinding_list -%}
    ADD RULEBINDING:
    {#- --- 必选参数 --- -#}
    USERPROFILENAME="{{item.USERPROFILENAME}}",
    RULENAME="{{item.RULENAME}}",
    ;
{%- endfor -%}
```

### 11 配置UPF上报Flow-Description信息的格式。

```jinja2
{%- for item in set_upglbpmpara_list -%}
    SET UPGLBPMPARA:
    {#- --- 可选参数 --- -#}
    {%- if item.FLOWDANYFMT is not none -%}
        FLOWDANYFMT={{item.FLOWDANYFMT}},
    {%- endif -%}
    ;
{%- endfor -%}
```


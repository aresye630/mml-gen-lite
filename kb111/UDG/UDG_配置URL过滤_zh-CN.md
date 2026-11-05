---
id: GWFD-110471
name: 配置URL过滤
ne_type: UDG
type: feature
description: 当运营商需要为用户提供URL过滤套餐，以满足特殊用户群的业务需求，则需要部署URL过滤基本功能。  适用于PGW-U、UPF。
risk_level: ''
doc_source: ["特性部署","特性指南","UDG特性指南","业务感知功能","GWFD-110471 URL过滤基本功能","激活URL过滤基本功能","配置URL过滤"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
当运营商需要为用户提供URL过滤套餐，以满足特殊用户群的业务需求，则需要部署URL过滤基本功能。适用于PGW-U、UPF。

## 必备事项
前提条件

* 请仔细阅读GWFD-110471 URL过滤基本功能。
* 完成加载license（如果有需求，请联系华为技术支持工程师处理）。
* 完成配置到ICAP Server的互通数据。
* 完成激活PCC 基本功能。
* 在ICAP Server上已导入URL分类数据信息。
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
    add_apn_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: 'URL过滤用户使用的APN。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_apncffunc_list:
      type: items
      properties:
        APNNAME:
          name: 'APN名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '与通过**ADD APN**配置的**APN**保持一致。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        CFSWITCHVALUE:
          name: '内容过滤功能开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          - INHERIT
          required: true
          description: '基于APN粒度开启URL过滤功能。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_cfprofile_list:
      type: items
      properties:
        CFPROFILENAME:
          name: '内容过滤策略名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_cftemplate_list:
      type: items
      properties:
        CFTEMPLATENAME:
          name: '内容过滤模板名称'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        ICAPSRVGMNAME:
          name: '主用CONTENT\_FILTERING类型的ICAP服务器组名称'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: '与通过**ADD ICAPSVRGRP**配置的“ICAPSVRGRPNAME”保持一致。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        ACTION:
          name: '缺省动作'
          type: string
          enum:
          - BLOCK
          - PASS
          - REDIRECT
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: PASS
        DEFREDNAME:
          name: '缺省重定向名称'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_apncftemplate_list:
      type: items
      properties:
        APNNAME:
          name: 'APN名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '与通过**ADD APN**配置的**APN**保持一致。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        CFTEMPLATENAME:
          name: '内容过滤模板名称'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: '已通过**ADD CFTEMPLATE**配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_cfprofbindcft_list:
      type: items
      properties:
        CFTEMPLATENAME:
          name: '内容过滤模板名称'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: '已通过**ADD CFTEMPLATE**配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        CFPROFILENAME:
          name: '内容过滤策略名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '已通过**ADD CFPROFILE**配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_contcategroup_list:
      type: items
      properties:
        CONTCATEGNAME:
          name: '内容分类组名称'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        CATEGORYTYPE:
          name: '内容分类类型'
          type: string
          enum:
          - NAME
          - PRIORITY
          - RANGE
          - SPECIFIC
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        CATEGORYID:
          name: '内容分类值'
          type: integer
          minimum: 1
          maximum: 65535
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        CATEGORYNAME:
          name: '内容分类名称'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ENDID:
          name: '内容分类结束值'
          type: integer
          minimum: 1
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PRIORITY:
          name: '优先级'
          type: integer
          minimum: 1
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        STARTID:
          name: '内容分类起始值'
          type: integer
          minimum: 1
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_contcategbind_list:
      type: items
      properties:
        CFPROFILENAME:
          name: '内容过滤策略名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '已通过**ADD CFPROFILE**配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        CONTCATEGNAME:
          name: '内容分类组名称'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: '已通过**ADD CONTCATEGROUP**配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        ACTION:
          name: '动作'
          type: string
          enum:
          - BLOCK
          - PASS
          - REDIRECT
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: PASS
        REDIRECTNAME:
          name: '缺省重定向名称'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_cfcachepara_list:
      type: items
      properties:
        CACHEIDLETIME:
          name: '本地缓存过期时间'
          type: integer
          minimum: 0
          maximum: 4294967294
          required: false
          description: '开启本地cache功能。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        CACHESW:
          name: '缓存开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
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
          description: 'URL过滤使用的三四层过滤条件。'
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
          description: '将Filter配置为生效。'
          data_source: '本端规划'
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
          description: '用于将指定Filter绑定到指定的FlowFilter。  使用的“ FLOWFILTERNAME”，已通过**ADD FLOWFILTER**命令配置完成。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
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
        DFTQUOTAPARA:
          name: '默认流量配额的单位'
          type: string
          enum:
          - Byte
          - KByte
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: Byte
        DFTQUOTATIME:
          name: '默认时长配额（秒）'
          type: integer
          minimum:
          - 0
          - 4294967295
          maximum:
          - 3600
          - 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DFTQUOTAVOLUME:
          name: '默认流量配额'
          type: integer
          minimum:
          - 0
          - 1000
          maximum:
          - 0
          - 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        OFFMETERINGTYPE:
          name: '离线计费统计类型'
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
          data_source: ''
          pattern: ''
          default: VOLUME
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
          data_source: ''
          pattern: ''
          default: VOLUME
        RG:
          name: '计费组'
          type: integer
          minimum: 0
          maximum: 4294967294
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SID:
          name: '业务标识'
          type: integer
          minimum: 0
          maximum: 4294967294
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
          description: '已通过命令**ADD URR**配置。'
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
          description: 'URL过滤使用的PCC策略组。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        URRGROUPNAME:
          name: 'URR组名称'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: '已通过命令**ADD URRGROUP**配置。'
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
          description: '业务规则绑定的FlowFilter已通过命令**ADD FLOWFILTER**配置。'
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
          description: '业务规则绑定的PCC策略组已通过命令**ADD PCCPOLICYGRP**配置。'
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
          description: '“USERPROFILENAME”已通过**ADD USERPROFILE**命令配置完成'
          data_source: '本端规划'
          pattern: ''
          default: ''
        RULENAME:
          name: '规则名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: 'User Profile绑定的业务规则，已通过**ADD RULE**命令配置完成。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV3G5UFBF01'
      SWITCH: ENABLE
    add_apn_list:
    - APN: 'apn-test'
    set_apncffunc_list:
    - APNNAME: 'apn-test'
      CFSWITCHVALUE: ENABLE
    add_cfprofile_list:
    - CFPROFILENAME: 'cf1'
    add_cftemplate_list:
    - CFTEMPLATENAME: 'icaptemplate'
      ICAPSRVGMNAME: 'icapsvrgrp1'
      ACTION: BLOCK
      DEFREDNAME: ''
    set_apncftemplate_list:
    - APNNAME: 'apn-test'
      CFTEMPLATENAME: 'icaptemplate'
    add_cfprofbindcft_list:
    - CFTEMPLATENAME: 'icaptemplate'
      CFPROFILENAME: 'cf1'
    add_contcategroup_list:
    - CONTCATEGNAME: 'ccgp1'
      CATEGORYTYPE: SPECIFIC
      CATEGORYID: 1
      CATEGORYNAME: ''
      ENDID: ''
      PRIORITY: ''
      STARTID: ''
    add_contcategbind_list:
    - CFPROFILENAME: 'cf1'
      CONTCATEGNAME: 'ccgp1'
      ACTION: BLOCK
      REDIRECTNAME: ''
    set_cfcachepara_list:
    - CACHEIDLETIME: 7200
      CACHESW: ENABLE
    add_filter_list:
    - FILTERNAME: 'filter_test'
      L34PROTTYPE: STRING
      L34PROTOCOL: ANY
      L34PROTNUM: ''
    set_refreshsrv_list:
    - REFRESHTYPE: USERPROFILE
    add_flowfilter_list:
    - FLOWFILTERNAME: 'flowfilter_test1'
    add_fltbindflowf_list:
    - FLOWFILTERNAME: 'flowfilter_test1'
      FILTERNAME: 'filter_test'
    add_urr_list:
    - URRNAME: 'urr_2'
      URRID: 2
      USAGERPTMODE: OFFLINE
      DFTQUOTAPARA: Byte
      DFTQUOTATIME: ''
      DFTQUOTAVOLUME: ''
      OFFMETERINGTYPE: VOLUME
      ONLMETERINGTYPE: VOLUME
      RG: ''
      SID: ''
    add_urrgroup_list:
    - URRGROUPNAME: 'urrgroup1'
      UPURRNAME1: 'urr_2'
      DOWNURRNAME1: 'urr_2'
    add_pccpolicygrp_list:
    - PCCPOLICYGRPNM: 'ppg_test'
      URRGROUPNAME: 'urrgroup1'
    add_rule_list:
    - RULENAME: 'rule_test'
      POLICYTYPE: PCC
      FILTERINGMODE: FLOWFILTER
      FLOWFILTERNAME: 'flowfilter_test1'
      PRIORITY: 1
      POLICYNAME: 'ppg_test'
      FLWFLTRGRPNAME: ''
      ADCMUTEFLAG: ENABLE
      ALGSWITCH: DISABLE
      RDSTRIGGERFLAG: DISABLE
      REDIRIPVERFLAG: ''
      REMARKFPISEL: REMARK
      SRVLBOFLAG: DISABLE
      WORKERNAME: ''
      WORKERPARA: ''
    add_userprofile_list:
    - USERPROFILENAME: 'up_test'
    add_rulebinding_list:
    - USERPROFILENAME: 'up_test'
      RULENAME: 'rule_test'
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

### 2 配置URL过滤用户使用的APN。

#### 2.1 添加APN。

```jinja2
{%- for item in add_apn_list -%}
    ADD APN:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    ;
{%- endfor -%}
```

#### 2.2 基于APN粒度开启URL过滤功能。

```jinja2
{%- for item in set_apncffunc_list -%}
    SET APNCFFUNC:
    {#- --- 必选参数 --- -#}
    APNNAME="{{item.APNNAME}}",
    CFSWITCHVALUE={{item.CFSWITCHVALUE}},
    ;
{%- endfor -%}
```

### 3 配置URL过滤。

#### 3.1 配置过滤策略。

```jinja2
{%- for item in add_cfprofile_list -%}
    ADD CFPROFILE:
    {#- --- 必选参数 --- -#}
    CFPROFILENAME="{{item.CFPROFILENAME}}",
    ;
{%- endfor -%}
```

#### 3.2 配置过滤策略模板。

```jinja2
{%- for item in add_cftemplate_list -%}
    ADD CFTEMPLATE:
    {#- --- 必选参数 --- -#}
    CFTEMPLATENAME="{{item.CFTEMPLATENAME}}",
    ICAPSRVGMNAME="{{item.ICAPSRVGMNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.ACTION is not none -%}
        ACTION={{item.ACTION}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：ACTION=REDIRECT 时必选 --- -#}
    {%- if item.ACTION == 'REDIRECT' -%}
        DEFREDNAME="{{item.DEFREDNAME}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 3.3 配置APN的URL过滤模板。

```jinja2
{%- for item in set_apncftemplate_list -%}
    SET APNCFTEMPLATE:
    {#- --- 必选参数 --- -#}
    APNNAME="{{item.APNNAME}}",
    CFTEMPLATENAME="{{item.CFTEMPLATENAME}}",
    ;
{%- endfor -%}
```

#### 3.4 配置URL过滤策略和模板绑定。

```jinja2
{%- for item in add_cfprofbindcft_list -%}
    ADD CFPROFBINDCFT:
    {#- --- 必选参数 --- -#}
    CFTEMPLATENAME="{{item.CFTEMPLATENAME}}",
    CFPROFILENAME="{{item.CFPROFILENAME}}",
    ;
{%- endfor -%}
```

#### 3.5 配置分类组。

```jinja2
{%- for item in add_contcategroup_list -%}
    ADD CONTCATEGROUP:
    {#- --- 必选参数 --- -#}
    CONTCATEGNAME="{{item.CONTCATEGNAME}}",
    CATEGORYTYPE={{item.CATEGORYTYPE}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：CATEGORYTYPE=SPECIFIC/NAME 时必选 --- -#}
    {%- if item.CATEGORYTYPE in ['SPECIFIC', 'NAME'] -%}
        CATEGORYID={{item.CATEGORYID}},
    {%- endif -%}
    {#- --- 条件必选：CATEGORYTYPE=NAME 时必选 --- -#}
    {%- if item.CATEGORYTYPE == 'NAME' -%}
        CATEGORYNAME="{{item.CATEGORYNAME}}",
    {%- endif -%}
    {#- --- 条件必选：CATEGORYTYPE=RANGE 时必选 --- -#}
    {%- if item.CATEGORYTYPE == 'RANGE' -%}
        ENDID={{item.ENDID}},
    {%- endif -%}
    {#- --- 条件必选：CATEGORYTYPE=PRIORITY 时必选 --- -#}
    {%- if item.CATEGORYTYPE == 'PRIORITY' -%}
        PRIORITY={{item.PRIORITY}},
    {%- endif -%}
    {#- --- 条件必选：CATEGORYTYPE=RANGE 时必选 --- -#}
    {%- if item.CATEGORYTYPE == 'RANGE' -%}
        STARTID={{item.STARTID}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 3.6 配置过滤策略与分类组绑定。

```jinja2
{%- for item in add_contcategbind_list -%}
    ADD CONTCATEGBIND:
    {#- --- 必选参数 --- -#}
    CFPROFILENAME="{{item.CFPROFILENAME}}",
    CONTCATEGNAME="{{item.CONTCATEGNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.ACTION is not none -%}
        ACTION={{item.ACTION}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：ACTION=REDIRECT 时必选 --- -#}
    {%- if item.ACTION == 'REDIRECT' -%}
        REDIRECTNAME="{{item.REDIRECTNAME}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 开启本地cache功能。

```jinja2
{%- for item in set_cfcachepara_list -%}
    SET CFCACHEPARA:
    {#- --- 可选参数 --- -#}
    {%- if item.CACHEIDLETIME is not none -%}
        CACHEIDLETIME={{item.CACHEIDLETIME}},
    {%- endif -%}
    {%- if item.CACHESW is not none -%}
        CACHESW={{item.CACHESW}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 5 配置URL过滤条件。

#### 5.1 配置Filter。

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

#### 5.2 将Filter配置为生效。

```jinja2
{%- for item in set_refreshsrv_list -%}
    SET REFRESHSRV:
    {#- --- 必选参数 --- -#}
    REFRESHTYPE={{item.REFRESHTYPE}},
    ;
{%- endfor -%}
```

### 6 配置流过滤器，绑定过滤条件。

#### 6.1 配置流过滤器。

```jinja2
{%- for item in add_flowfilter_list -%}
    ADD FLOWFILTER:
    {#- --- 必选参数 --- -#}
    FLOWFILTERNAME="{{item.FLOWFILTERNAME}}",
    ;
{%- endfor -%}
```

#### 6.2 配置过滤条件与流过滤器的绑定关系。

```jinja2
{%- for item in add_fltbindflowf_list -%}
    ADD FLTBINDFLOWF:
    {#- --- 必选参数 --- -#}
    FLOWFILTERNAME="{{item.FLOWFILTERNAME}}",
    FILTERNAME="{{item.FILTERNAME}}",
    ;
{%- endfor -%}
```

### 7 配置计费属性。

#### 7.1 配置URR。

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
        {%- if item.DFTQUOTAPARA is not none -%}
            DFTQUOTAPARA={{item.DFTQUOTAPARA}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：USAGERPTMODE=ONLINE 时可选 --- -#}
    {%- if item.USAGERPTMODE == 'ONLINE' -%}
        {%- if item.DFTQUOTATIME is not none -%}
            DFTQUOTATIME={{item.DFTQUOTATIME}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：USAGERPTMODE=ONLINE 时可选 --- -#}
    {%- if item.USAGERPTMODE == 'ONLINE' -%}
        {%- if item.DFTQUOTAVOLUME is not none -%}
            DFTQUOTAVOLUME={{item.DFTQUOTAVOLUME}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：USAGERPTMODE=OFFLINE 时可选 --- -#}
    {%- if item.USAGERPTMODE == 'OFFLINE' -%}
        {%- if item.OFFMETERINGTYPE is not none -%}
            OFFMETERINGTYPE={{item.OFFMETERINGTYPE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：USAGERPTMODE=ONLINE 时可选 --- -#}
    {%- if item.USAGERPTMODE == 'ONLINE' -%}
        {%- if item.ONLMETERINGTYPE is not none -%}
            ONLMETERINGTYPE={{item.ONLMETERINGTYPE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：USAGERPTMODE=ONLINE/OFFLINE 时可选 --- -#}
    {%- if item.USAGERPTMODE in ['ONLINE', 'OFFLINE'] -%}
        {%- if item.RG is not none -%}
            RG={{item.RG}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：USAGERPTMODE=ONLINE/OFFLINE 时可选 --- -#}
    {%- if item.USAGERPTMODE in ['ONLINE', 'OFFLINE'] -%}
        {%- if item.SID is not none -%}
            SID={{item.SID}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 7.2 配置上行和下行业务对应的URR。

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

### 8 配置PCC策略。

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


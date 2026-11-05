---
id: ''
name: 基于PCC预定义规则的带宽控制
ne_type: UEG
type: feature
description: PCF/PCRF作为用户计费与控制策略管理中心，能够基于用户签约、套餐使用量等多种场景动态安装或者删除预定义规则。基于PCC预定义规则的带宽控制可应用于以下两种场景：  * PCF/PCRF可感知用户套餐的使用量，当用户业务访问量超出限额时通过安装预定义规则通知UEG执行带宽控制策略，以降低用户的访问速率，达到公平使用网络的原则，使访问相同业务的用户得到同样的网络体验。 * PCF/PCRF可感知SMF的PRA（Presence Reporting Area）位置上报，当用户进入指定区域时通过安装预定义规则通知UEG执行带宽控制策略，达到对指定区域的业务做限速的目的。  适用于PGW-U、UPF。
tags: []
risk_level: ''
doc_source: ["网络部署","地市共享式（仅连接）","5GC toB 部署边缘站点（站点为“风筝S”，共享式）","配置业务数据（风筝S）","带宽控制","基于PCC预定义规则的带宽控制"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
PCF/PCRF作为用户计费与控制策略管理中心，能够基于用户签约、套餐使用量等多种场景动态安装或者删除预定义规则。基于PCC预定义规则的带宽控制可应用于以下两种场景：* PCF/PCRF可感知用户套餐的使用量，当用户业务访问量超出限额时通过安装预定义规则通知UEG执行带宽控制策略，以降低用户的访问速率，达到公平使用网络的原则，使访问相同业务的用户得到同样的网络体验。* PCF/PCRF可感知SMF的PRA（Presence Reporting Area）位置上报，当用户进入指定区域时通过安装预定义规则通知UEG执行带宽控制策略，达到对指定区域的业务做限速的目的。适用于PGW-U、UPF。

## 必备事项
前提条件

* 请仔细阅读GWFD-022701 基于业务感知的带宽控制。
* UEG与网络实体之间的网络环境已经构建完成。
* 已完成GWFD-022201 PCC基本功能的配置。
* 已完成协议特征库的加载。
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
    add_categoryprop_list:
      type: items
      properties:
        CATEPROPNAME:
          name: '分类属性名称'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_bwmservice_list:
      type: items
      properties:
        BWMSERVICENAME:
          name: '带宽控制业务名称'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: '“CATEPROPNAME”参数和**ADD RULE**中配置的“POLICYNAME”参数必须规划一致。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        BWMSERVICETYPE:
          name: '业务类型'
          type: string
          enum:
          - NONTOS
          - TOS
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        NONTOSSRVTYPE:
          name: '非TOS业务类型'
          type: string
          enum:
          - CATEGORY_PROP
          - PROTOCOL
          - PROTOCOLGROUP
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        CATEPROPNAME:
          name: '分类属性名称'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_bwmcontroller_list:
      type: items
      properties:
        BWMCNAME:
          name: '带宽管理控制器名称'
          type: string
          maxLength: 31
          required: true
          description: '推荐配置：  CIR = 0.5 \* PIR （最大带宽建议为保证带宽的2倍）'
          data_source: '本端规划'
          pattern: ''
          default: ''
        CTRLTYPE:
          name: '带宽管理控制类型'
          type: string
          enum:
          - CAR
          - SHAPING
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        CIR:
          name: '承诺信息速率（千比特/秒）'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        PIR:
          name: '峰值信息速率（千比特/秒）'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        GREEN:
          name: '绿色'
          type: string
          enum:
          - DISCARD
          - PASS
          - REMARK
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: PASS
        YELLOW:
          name: '黄色'
          type: string
          enum:
          - DISCARD
          - PASS
          - REMARK
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: PASS
        RED:
          name: '红色'
          type: string
          enum:
          - DISCARD
          - PASS
          - REMARK
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: PASS
    add_bwmusergroup_list:
      type: items
      properties:
        USERGROUPTYPE:
          name: '用户组类型'
          type: string
          enum:
          - DEFAULT_GROUP
          - SPECIFIC_GROUP
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        USERGROUPNAME:
          name: '用户组名称'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        USERGROUPPRI:
          name: '用户组优先级'
          type: integer
          minimum: 1
          maximum: 32768
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        USERLEVSRVTYPE:
          name: '用户级业务类型'
          type: string
          enum:
          - NONTOS
          - TOS
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: TOS
    add_bwmrule_list:
      type: items
      properties:
        USERGROUPTYPE:
          name: '用户组类型'
          type: string
          enum:
          - DEFAULT_GROUP
          - SPECIFIC_GROUP
          required: true
          description: 'BwmService已通过**ADD BWMSERVICE**命令配置；  BwmController已通过  **ADD BWMCONTROLLER**命令配置。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        USERGROUPNAME:
          name: '用户组名称'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        BWMRULETYPE:
          name: '带宽管理规则类型'
          type: string
          enum:
          - GROUP_DEFAULT
          - GROUP_SPECIFIC
          - SUBSCRIBER_DEFAULT
          - SUBSCRIBER_SPECIFIC
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        BWMRULENAME:
          name: '带宽管理规则名称'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        BWMSERVICENAME:
          name: '带宽控制业务名称'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        UPBWMCTRLNAME1:
          name: '上行带宽管理控制器名称一'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        DNBWMCTRLNAME1:
          name: '下行带宽管理控制器名称一'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        BWMRULEPRI:
          name: '带宽管理规则优先级'
          type: integer
          minimum: 1
          maximum: 32768
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_apnbindbwmusrg_list:
      type: items
      properties:
        USERGROUPNAME:
          name: '用户组名称'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        APN:
          name: 'APN名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '通过**ADD APN**命令配置，可以使用**LST APN**命令进行查询。'
          data_source: '本端规划'
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
          description: '-'
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
          description: '流过滤器名称“FLOWFILTERNAME”已通过**ADD FLOWFILTER**配置。  七层过滤器名字“L7FILTERNAME”已通过**ADD L7FILTER**配置。'
          data_source: '已配置数据中获取'
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
        L7FILTERNAME:
          name: '七层过滤器名字'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: ''
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
    add_rule_list:
      type: items
      properties:
        RULENAME:
          name: '规则名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '“RULENAME”必须与PCF/PCRF、UNC规划一致。'
          data_source: '全网规划'
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
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        PRIORITY:
          name: '全局优先级'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: 4294967295
        POLICYNAME:
          name: '策略名称'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV3G5TCSA01'
      SWITCH: ENABLE
    add_categoryprop_list:
    - CATEPROPNAME: 'cp_700_600'
    add_bwmservice_list:
    - BWMSERVICENAME: 'my-bwm-service1'
      BWMSERVICETYPE: NONTOS
      NONTOSSRVTYPE: CATEGORY_PROP
      CATEPROPNAME: 'cp_700_600'
    add_bwmcontroller_list:
    - BWMCNAME: 'bc-up-p2p'
      CTRLTYPE: CAR
      CIR: 100
      PIR: 700
      GREEN: PASS
      YELLOW: PASS
      RED: DISCARD
    add_bwmusergroup_list:
    - USERGROUPTYPE: SPECIFIC_GROUP
      USERGROUPNAME: 'ug-bwm'
      USERGROUPPRI: 1
      USERLEVSRVTYPE: NONTOS
    add_bwmrule_list:
    - USERGROUPTYPE: SPECIFIC_GROUP
      USERGROUPNAME: 'ug-bwm'
      BWMRULETYPE: SUBSCRIBER_SPECIFIC
      BWMRULENAME: 'br-p2p'
      BWMSERVICENAME: 'my-bwm-service1'
      UPBWMCTRLNAME1: 'bc-up-p2p'
      DNBWMCTRLNAME1: 'bc-dn-p2p'
      BWMRULEPRI: 1
    add_apnbindbwmusrg_list:
    - USERGROUPNAME: 'ug-bwm'
      APN: 'testapn'
    add_l7filter_list:
    - L7FILTERNAME: 'l7-p2p'
      SUBL7FLTNAME: 'sl7-p2p'
      URL: 'www.example.com*/*'
      URLTYPE: URL
    add_flowfilter_list:
    - FLOWFILTERNAME: 'flowfilter_p2p'
    add_protbindflowf_list:
    - FLOWFILTERNAME: 'flowfilter_p2p'
      PROTOCOLNAME: 'http'
      L7FILTERNAME: 'l7-p2p'
    set_refreshsrv_list:
    - REFRESHTYPE: USERPROFILE
    add_rule_list:
    - RULENAME: 'rule_p2pbwm'
      POLICYTYPE: BWM
      FILTERINGMODE: FLOWFILTER
      FLOWFILTERNAME: 'flowfilter_p2p'
      PRIORITY: 1
      POLICYNAME: 'cp_700_600'
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

### 2 配置BWM业务。

#### 2.1 设置分类属性。

```jinja2
{%- for item in add_categoryprop_list -%}
    ADD CATEGORYPROP:
    {#- --- 必选参数 --- -#}
    CATEPROPNAME="{{item.CATEPROPNAME}}",
    ;
{%- endfor -%}
```

#### 2.2 设置基于分类属性的BWM业务。

```jinja2
{%- for item in add_bwmservice_list -%}
    ADD BWMSERVICE:
    {#- --- 必选参数 --- -#}
    BWMSERVICENAME="{{item.BWMSERVICENAME}}",
    BWMSERVICETYPE={{item.BWMSERVICETYPE}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：BWMSERVICETYPE=NONTOS 时必选 --- -#}
    {%- if item.BWMSERVICETYPE == 'NONTOS' -%}
        NONTOSSRVTYPE={{item.NONTOSSRVTYPE}},
    {%- endif -%}
    {#- --- 条件必选：NONTOSSRVTYPE=CATEGORY_PROP 时必选 --- -#}
    {%- if item.NONTOSSRVTYPE == 'CATEGORY_PROP' -%}
        CATEPROPNAME="{{item.CATEPROPNAME}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 2.3 配置BWM控制器，设置CAR参数。

```jinja2
{%- for item in add_bwmcontroller_list -%}
    ADD BWMCONTROLLER:
    {#- --- 必选参数 --- -#}
    BWMCNAME="{{item.BWMCNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.CTRLTYPE is not none -%}
        CTRLTYPE={{item.CTRLTYPE}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：CTRLTYPE=CAR 时必选 --- -#}
    {%- if item.CTRLTYPE == 'CAR' -%}
        CIR={{item.CIR}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：CTRLTYPE=CAR 时可选 --- -#}
    {%- if item.CTRLTYPE == 'CAR' -%}
        {%- if item.PIR is not none -%}
            PIR={{item.PIR}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：CTRLTYPE=CAR 时可选 --- -#}
    {%- if item.CTRLTYPE == 'CAR' -%}
        {%- if item.GREEN is not none -%}
            GREEN={{item.GREEN}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：CTRLTYPE=CAR 时可选 --- -#}
    {%- if item.CTRLTYPE == 'CAR' -%}
        {%- if item.YELLOW is not none -%}
            YELLOW={{item.YELLOW}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：CTRLTYPE=CAR 时可选 --- -#}
    {%- if item.CTRLTYPE == 'CAR' -%}
        {%- if item.RED is not none -%}
            RED={{item.RED}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 2.4 定义带宽管理用户组，配置优先级和业务类型。

```jinja2
{%- for item in add_bwmusergroup_list -%}
    ADD BWMUSERGROUP:
    {#- --- 必选参数 --- -#}
    USERGROUPTYPE={{item.USERGROUPTYPE}},
    {#- --- 可选参数 --- -#}
    {%- if item.USERLEVSRVTYPE is not none -%}
        USERLEVSRVTYPE={{item.USERLEVSRVTYPE}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：USERGROUPTYPE=SPECIFIC_GROUP 时必选 --- -#}
    {%- if item.USERGROUPTYPE == 'SPECIFIC_GROUP' -%}
        USERGROUPNAME="{{item.USERGROUPNAME}}",
    {%- endif -%}
    {#- --- 条件必选：USERGROUPTYPE=SPECIFIC_GROUP 时必选 --- -#}
    {%- if item.USERGROUPTYPE == 'SPECIFIC_GROUP' -%}
        USERGROUPPRI={{item.USERGROUPPRI}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 2.5 配置用户级带宽控制规则。

```jinja2
{%- for item in add_bwmrule_list -%}
    ADD BWMRULE:
    {#- --- 必选参数 --- -#}
    USERGROUPTYPE={{item.USERGROUPTYPE}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：USERGROUPTYPE=SPECIFIC_GROUP 时必选 --- -#}
    {%- if item.USERGROUPTYPE == 'SPECIFIC_GROUP' -%}
        USERGROUPNAME="{{item.USERGROUPNAME}}",
    {%- endif -%}
    {#- --- 条件必选：USERGROUPTYPE=DEFAULT_GROUP/SPECIFIC_GROUP 时必选 --- -#}
    {%- if item.USERGROUPTYPE in ['DEFAULT_GROUP', 'SPECIFIC_GROUP'] -%}
        BWMRULETYPE={{item.BWMRULETYPE}},
    {%- endif -%}
    {#- --- 条件必选：BWMRULETYPE=GROUP_SPECIFIC/SUBSCRIBER_SPECIFIC 时必选 --- -#}
    {%- if item.BWMRULETYPE in ['GROUP_SPECIFIC', 'SUBSCRIBER_SPECIFIC'] -%}
        BWMRULENAME="{{item.BWMRULENAME}}",
    {%- endif -%}
    {#- --- 条件必选：BWMRULETYPE=GROUP_SPECIFIC/SUBSCRIBER_SPECIFIC 时必选 --- -#}
    {%- if item.BWMRULETYPE in ['GROUP_SPECIFIC', 'SUBSCRIBER_SPECIFIC'] -%}
        BWMSERVICENAME="{{item.BWMSERVICENAME}}",
    {%- endif -%}
    {#- --- 条件必选：BWMRULETYPE=GROUP_SPECIFIC/SUBSCRIBER_SPECIFIC 时必选 --- -#}
    {%- if item.BWMRULETYPE in ['GROUP_SPECIFIC', 'SUBSCRIBER_SPECIFIC'] -%}
        BWMRULEPRI={{item.BWMRULEPRI}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：BWMRULETYPE=GROUP_DEFAULT/SUBSCRIBER_DEFAULT/GROUP_SPECIFIC/SUBSCRIBER_SPECIFIC 时可选 --- -#}
    {%- if item.BWMRULETYPE in ['GROUP_DEFAULT', 'SUBSCRIBER_DEFAULT', 'GROUP_SPECIFIC', 'SUBSCRIBER_SPECIFIC'] -%}
        {%- if item.UPBWMCTRLNAME1 is not none -%}
            UPBWMCTRLNAME1="{{item.UPBWMCTRLNAME1}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：BWMRULETYPE=GROUP_DEFAULT/SUBSCRIBER_DEFAULT/GROUP_SPECIFIC/SUBSCRIBER_SPECIFIC 时可选 --- -#}
    {%- if item.BWMRULETYPE in ['GROUP_DEFAULT', 'SUBSCRIBER_DEFAULT', 'GROUP_SPECIFIC', 'SUBSCRIBER_SPECIFIC'] -%}
        {%- if item.DNBWMCTRLNAME1 is not none -%}
            DNBWMCTRLNAME1="{{item.DNBWMCTRLNAME1}}",
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 2.6 将APN下的用户包含到该用户组。

```jinja2
{%- for item in add_apnbindbwmusrg_list -%}
    ADD APNBINDBWMUSRG:
    {#- --- 必选参数 --- -#}
    USERGROUPNAME="{{item.USERGROUPNAME}}",
    APN="{{item.APN}}",
    ;
{%- endfor -%}
```

### 3 配置业务感知规则。

#### 3.1 配置七层过滤规则。

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

#### 3.2 配置FlowFilter。

```jinja2
{%- for item in add_flowfilter_list -%}
    ADD FLOWFILTER:
    {#- --- 必选参数 --- -#}
    FLOWFILTERNAME="{{item.FLOWFILTERNAME}}",
    ;
{%- endfor -%}
```

#### 3.3 将指定L7Filter绑定到FlowFilter。

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

#### 3.4 将新配置的信息置为生效。

```jinja2
{%- for item in set_refreshsrv_list -%}
    SET REFRESHSRV:
    {#- --- 必选参数 --- -#}
    REFRESHTYPE={{item.REFRESHTYPE}},
    ;
{%- endfor -%}
```

#### 3.5 配置业务使用的rule规则。

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

#### PCF/PCRF和UNC上仅配置预定义规则的名称，UEG上配置该预定义规则的名称及具体的规则内容，如QoS管理、计费控制策略等。且PCF/PCRF、UNC 和UEG上的预定义规则名称必须规划一致。

#### 带宽控制策略通过**ADD RULE**中的“POLICYNAME”和**ADD BWMSERVICE**中的“CATEPROPNAME”关联获得，因此两者的值必须规划一致。


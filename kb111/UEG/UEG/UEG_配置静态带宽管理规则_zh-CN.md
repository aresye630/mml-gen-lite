---
id: ''
name: 配置静态带宽管理规则
ne_type: UEG
type: feature
description: 当APP/管理面MEPM没有下发动态带宽管理规则时，如果需要对用户访问APP的业务流进行上下行带宽控制，支持在MPF本地配置带宽管理规则。  适用于MPF。
tags: []
risk_level: ''
doc_source: ["网络部署","园区入驻+地市共享（连接+计算）","5GC toB 部署边缘站点（站点为“风筝S”，带计算）","配置业务数据（风筝S）","APP集成管理功能","配置MPF","激活支持APP带宽管理","配置静态带宽管理规则"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
当APP/管理面MEPM没有下发动态带宽管理规则时，如果需要对用户访问APP的业务流进行上下行带宽控制，支持在MPF本地配置带宽管理规则。适用于MPF。

## 必备事项
前提条件

请仔细阅读带宽管理规则的获取和执行。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    add_categoryprop_list:
      type: items
      properties:
        CATEPROPNAME:
          name: '分类属性名称'
          type: string
          maxLength: 31
          required: true
          description: '配置带宽控制属性，用户进行带宽控制时，通过CATEPROPNAME匹配到相应的带宽控制策略，以完成带宽控制功能。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_bwmservice_list:
      type: items
      properties:
        BWMSERVICENAME:
          name: '带宽控制业务名称'
          type: string
          maxLength: 31
          required: true
          description: '增加一条带宽管理的业务范围，实现业务区分。'
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
          description: '为带宽管理业务绑定一个分类属性。'
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
          description: '当配置为CATEGORY_PROP时，支持匹配IP地址的过滤条件区分业务。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        CATEPROPNAME:
          name: '分类属性名称'
          type: string
          maxLength: 31
          required: false
          description: '该参数和**ADD RULE**中配置的“POLICYNAME”参数必须规划一致。'
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
          description: '配置一个BWM控制器，设置保证带宽、峰值速率、五元组个数等相关参数。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        CTRLTYPE:
          name: '带宽管理控制类型'
          type: string
          enum:
          - CAR
          required: false
          description: 'BWM控制器的类型为流量监管。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        CIR:
          name: '承诺信息速率（千比特/秒）'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: false
          description: '保证带宽。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PIR:
          name: '峰值信息速率（千比特/秒）'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: false
          description: '上下行峰值速率带宽。'
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
          description: '入口速率小于或等于保证带宽的报文被标记为绿色，对标记的报文采取通过动作。'
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
          description: '入口速率大于保证带宽，但小于或等于峰值速率带宽的报文被标记为黄色，对标记的报文采取通过动作。'
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
          description: '入口速率大于峰值速率带宽的报文被标记为红色，对标记的报文采取丢弃动作。'
          data_source: '本端规划'
          pattern: ''
          default: DISCARD
    set_bandwidthmng_list:
      type: items
      properties:
        RANGE:
          name: '带宽管理生效范围'
          type: string
          enum:
          - CPU
          - SYSTEM
          required: false
          description: '设置带宽控制器中用户组级业务带宽和连接数是整机生效。'
          data_source: '本端规划'
          pattern: ''
          default: ''
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
          description: '对某一类用户访问的业务进行带宽控制。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        USERGROUPNAME:
          name: '用户组名称'
          type: string
          maxLength: 31
          required: false
          description: '配置带宽管理用户组名称。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        USERGROUPPRI:
          name: '用户组优先级'
          type: integer
          minimum: 1
          maximum: 32768
          required: false
          description: '配置带宽管理用户组的优先级。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        USERGLEVSRVTYPE:
          name: '用户组级业务类型'
          type: string
          enum:
          - NONTOS
          - TOS
          required: false
          description: '非TOS类型有分类属性、7层协议和协议组，MPF上通过分类属性实现。'
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
          description: '特定用户组。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        USERGROUPNAME:
          name: '用户组名称'
          type: string
          maxLength: 31
          required: false
          description: '配置具体用户组的名称，已使用**ADD BWMUSERGROUP**命令配置生成。'
          data_source: '已配置数据中获取'
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
          description: '用户组级别特定规则。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        BWMRULENAME:
          name: '带宽管理规则名称'
          type: string
          maxLength: 31
          required: false
          description: '配置带宽管理规则的名称。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        BWMSERVICENAME:
          name: '带宽控制业务名称'
          type: string
          maxLength: 31
          required: false
          description: '配置带宽管理业务名称，已使用**ADD BWMSERVICE**命令配置生成。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        UPBWMCTRLNAME1:
          name: '上行带宽管理控制器名称一'
          type: string
          maxLength: 31
          required: false
          description: '配置上行方向带宽管理控制器的名称，已使用**ADD BWMCONTROLLER**命令配置生成。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        DNBWMCTRLNAME1:
          name: '下行带宽管理控制器名称一'
          type: string
          maxLength: 31
          required: false
          description: '配置下行方向带宽管理控制器的名称，已使用**ADD BWMCONTROLLER**命令配置生成。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        BWMRULEPRI:
          name: '带宽管理规则优先级'
          type: integer
          minimum: 1
          maximum: 32768
          required: false
          description: '配置带宽管理规则的优先级，进行业务规则匹配时，优先匹配优先级高的规则，优先级的值越小，优先级越高。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_filter_list:
      type: items
      properties:
        FILTERNAME:
          name: '过滤器名字'
          type: string
          maxLength: 63
          required: true
          description: '配置三四层Filter，对命中APP IP地址的业务流进行上下行带宽控制。'
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
        SVRIPMODE:
          name: '服务器IP地址配置模式'
          type: string
          enum:
          - HOSTNAME
          - IP
          - IPLIST
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        SVRIP:
          name: '服务器IP地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        SVRIPMASKTYPE:
          name: '服务器IP地址掩码类型'
          type: string
          enum:
          - IPTYPE
          - LENGTHTYPE
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        SVRIPMASK:
          name: '服务器IP地址反掩码'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_flowfilter_list:
      type: items
      properties:
        FLOWFILTERNAME:
          name: '流过滤器名称'
          type: string
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
          maxLength: 63
          required: true
          description: '已通过**ADD FLOWFILTER**命令配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        FILTERNAME:
          name: '过滤器名字'
          type: string
          maxLength: 63
          required: true
          description: '已通过**ADD FILTER**命令配置。'
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
          description: '刷新Filter配置。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_rule_list:
      type: items
      properties:
        RULENAME:
          name: '规则名称'
          type: string
          maxLength: 63
          required: true
          description: '设置带宽管理的Rule。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        POLICYTYPE:
          name: '策略类型'
          type: string
          enum:
          - BWM
          - MTP
          - WEBPROXY
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
          maximum: 65535
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: 65535
        POLICYNAME:
          name: '策略名称'
          type: string
          maxLength: 63
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_userprofile_list:
      type: items
      properties:
        USERPROFILENAME:
          name: '用户模板名称'
          type: string
          maxLength: 63
          required: true
          description: '配置User Profile。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_upbindbwmusrg_list:
      type: items
      properties:
        USERGROUPNAME:
          name: '用户组名称'
          type: string
          maxLength: 31
          required: true
          description: '已使用**ADD BWMUSERGROUP**命令配置生成。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        USERPROFILENAME:
          name: '用户模板名称'
          type: string
          maxLength: 63
          required: true
          description: '已使用**ADD USERPROFILE**命令配置生成。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_localuserprof_list:
      type: items
      properties:
        USERPROFILENAME:
          name: '用户模板名称'
          type: string
          maxLength: 63
          required: true
          description: '将User Profile配置为全局User Profile。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_rulebinding_list:
      type: items
      properties:
        USERPROFILENAME:
          name: '用户模板名称'
          type: string
          maxLength: 63
          required: true
          description: '已通过**ADD USERPROFILE**命令配置完成。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        RULENAME:
          name: '规则名称'
          type: string
          maxLength: 63
          required: true
          description: 'User Profile绑定的业务规则，已通过**ADD RULE**命令配置完成。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_bwmcontroller_list_2:
      type: items
      properties:
        BWMCNAME:
          name: '带宽管理控制器名称'
          type: string
          maxLength: 31
          required: true
          description: '配置一个BWM控制器，设置保证带宽、峰值速率、五元组个数等相关参数。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        CTRLTYPE:
          name: '带宽管理控制类型'
          type: string
          enum:
          - CAR
          required: false
          description: 'BWM控制器的类型为流量监管。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        CIR:
          name: '承诺信息速率（千比特/秒）'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: false
          description: '保证带宽。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PIR:
          name: '峰值信息速率（千比特/秒）'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: false
          description: '上下行峰值速率带宽。'
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
          description: '入口速率小于或等于保证带宽的报文被标记为绿色，对标记的报文采取通过动作。'
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
          description: '入口速率大于保证带宽，但小于或等于峰值速率带宽的报文被标记为黄色，对标记的报文采取通过动作。'
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
          description: '入口速率大于峰值速率带宽的报文被标记为红色，对标记的报文采取丢弃动作。'
          data_source: '本端规划'
          pattern: ''
          default: DISCARD
    set_bandwidthmng_list_1:
      type: items
      properties:
        RANGE:
          name: '带宽管理生效范围'
          type: string
          enum:
          - CPU
          - SYSTEM
          required: false
          description: '设置带宽控制器中用户组级业务带宽和连接数是整机生效。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_bwmusergroup_list_1:
      type: items
      properties:
        USERGROUPTYPE:
          name: '用户组类型'
          type: string
          enum:
          - DEFAULT_GROUP
          - SPECIFIC_GROUP
          required: true
          description: '对某一类用户访问的业务进行带宽控制。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        USERGLEVSRVTYPE:
          name: '用户组级业务类型'
          type: string
          enum:
          - NONTOS
          - TOS
          required: false
          description: '非TOS类型有分类属性、7层协议和协议组，MPF上通过分类属性实现。'
          data_source: '本端规划'
          pattern: ''
          default: TOS
    add_bwmrule_list_1:
      type: items
      properties:
        USERGROUPTYPE:
          name: '用户组类型'
          type: string
          enum:
          - DEFAULT_GROUP
          - SPECIFIC_GROUP
          required: true
          description: '特定用户组。'
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
          description: '用户组级别特定规则。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        UPBWMCTRLNAME1:
          name: '上行带宽管理控制器名称一'
          type: string
          maxLength: 31
          required: false
          description: '配置上行方向带宽管理控制器的名称，已使用**ADD BWMCONTROLLER**命令配置生成。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        DNBWMCTRLNAME1:
          name: '下行带宽管理控制器名称一'
          type: string
          maxLength: 31
          required: false
          description: '配置下行方向带宽管理控制器的名称，已使用**ADD BWMCONTROLLER**命令配置生成。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
  examples:
    add_categoryprop_list:
    - CATEPROPNAME: 'cp_category'
    add_bwmservice_list:
    - BWMSERVICENAME: 'bwm-service'
      BWMSERVICETYPE: NONTOS
      NONTOSSRVTYPE: CATEGORY_PROP
      CATEPROPNAME: 'cp_category'
    add_bwmcontroller_list:
    - BWMCNAME: 'bc-global-up'
      CTRLTYPE: CAR
      CIR: 100
      PIR: 700
      GREEN: PASS
      YELLOW: PASS
      RED: DISCARD
    set_bandwidthmng_list:
    - RANGE: SYSTEM
    add_bwmusergroup_list:
    - USERGROUPTYPE: SPECIFIC_GROUP
      USERGROUPNAME: 'ug_test'
      USERGROUPPRI: 1
      USERGLEVSRVTYPE: NONTOS
    add_bwmrule_list:
    - USERGROUPTYPE: SPECIFIC_GROUP
      USERGROUPNAME: 'ug_test'
      BWMRULETYPE: GROUP_SPECIFIC
      BWMRULENAME: 'bwm_rule_test'
      BWMSERVICENAME: 'bwm-service'
      UPBWMCTRLNAME1: 'bc-global-up'
      DNBWMCTRLNAME1: 'bc-global-down'
      BWMRULEPRI: 1
    add_filter_list:
    - FILTERNAME: 'filter_test'
      L34PROTTYPE: STRING
      L34PROTOCOL: ANY
      SVRIPMODE: IP
      SVRIP: '10.1.1.1'
      SVRIPMASKTYPE: IPTYPE
      SVRIPMASK: '0.0.0.0'
    add_flowfilter_list:
    - FLOWFILTERNAME: 'flow-l34'
    add_fltbindflowf_list:
    - FLOWFILTERNAME: 'flow-l34'
      FILTERNAME: 'filter_test'
    set_refreshsrv_list:
    - REFRESHTYPE: ALL
    add_rule_list:
    - RULENAME: 'rule_bwm'
      POLICYTYPE: BWM
      FILTERINGMODE: FLOWFILTER
      FLOWFILTERNAME: 'flow-l34'
      PRIORITY: 1
      POLICYNAME: 'cp_category'
    add_userprofile_list:
    - USERPROFILENAME: 'up_test'
    add_upbindbwmusrg_list:
    - USERGROUPNAME: 'ug_test'
      USERPROFILENAME: 'up_test'
    add_localuserprof_list:
    - USERPROFILENAME: 'up_test'
    add_rulebinding_list:
    - USERPROFILENAME: 'up_test'
      RULENAME: 'rule_bwm'
    add_bwmcontroller_list_2:
    - BWMCNAME: 'bc-global-up'
      CTRLTYPE: CAR
      CIR: 100
      PIR: 700
      GREEN: PASS
      YELLOW: PASS
      RED: DISCARD
    set_bandwidthmng_list_1:
    - RANGE: SYSTEM
    add_bwmusergroup_list_1:
    - USERGROUPTYPE: DEFAULT_GROUP
      USERGLEVSRVTYPE: NONTOS
    add_bwmrule_list_1:
    - USERGROUPTYPE: DEFAULT_GROUP
      BWMRULETYPE: GROUP_DEFAULT
      UPBWMCTRLNAME1: 'bc-global-up'
      DNBWMCTRLNAME1: 'bc-global-down'
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 配置基于APP的带宽控制，对访问该APP的所有业务进行带宽管理。

#### 1.1 配置BWM业务。

##### 1.1.1 设置分类属性。

```jinja2
{%- if is_scenario_app_based -%}
    {%- for item in add_categoryprop_list -%}
        ADD CATEGORYPROP:
        {#- --- 必选参数 --- -#}
        CATEPROPNAME="{{item.CATEPROPNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 1.1.2 设置基于分类属性的BWM业务，MPF仅支持非TOS业务，采用三四层的过滤规则进行识别。

```jinja2
{%- if is_scenario_app_based -%}
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
{%- endif -%}
```

##### 1.1.3 配置BWM控制器，设置CAR参数。

```jinja2
{%- if is_scenario_app_based -%}
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
{%- endif -%}
```

##### 1.1.4 配置BWM控制器中的用户组级业务带宽和连接数等配置数据是基于业务处理单元生效还是整机生效。

```jinja2
{%- if is_scenario_app_based -%}
    {%- for item in set_bandwidthmng_list -%}
        SET BANDWIDTHMNG:
        {#- --- 可选参数 --- -#}
        {%- if item.RANGE is not none -%}
            RANGE={{item.RANGE}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 1.1.5 定义带宽管理用户组，配置优先级和业务类型。

```jinja2
{%- if is_scenario_app_based -%}
    {%- for item in add_bwmusergroup_list -%}
        ADD BWMUSERGROUP:
        {#- --- 必选参数 --- -#}
        USERGROUPTYPE={{item.USERGROUPTYPE}},
        {#- --- 可选参数 --- -#}
        {%- if item.USERGLEVSRVTYPE is not none -%}
            USERGLEVSRVTYPE={{item.USERGLEVSRVTYPE}},
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
{%- endif -%}
```

##### 1.1.6 配置用户组级带宽控制规则。

```jinja2
{%- if is_scenario_app_based -%}
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
{%- endif -%}
```

#### 1.2 配置三四层过滤条件。

##### 1.2.1 配置三四层过滤条件，IP地址为APP的IP地址。

```jinja2
{%- if is_scenario_app_based -%}
    {%- for item in add_filter_list -%}
        ADD FILTER:
        {#- --- 必选参数 --- -#}
        FILTERNAME="{{item.FILTERNAME}}",
        L34PROTTYPE={{item.L34PROTTYPE}},
        {#- --- 可选参数 --- -#}
        {%- if item.SVRIPMODE is not none -%}
            SVRIPMODE={{item.SVRIPMODE}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：L34PROTTYPE=STRING 时必选 --- -#}
        {%- if item.L34PROTTYPE == 'STRING' -%}
            L34PROTOCOL={{item.L34PROTOCOL}},
        {%- endif -%}
        {#- --- 条件必选：SVRIPMODE=IP 时必选 --- -#}
        {%- if item.SVRIPMODE == 'IP' -%}
            SVRIP="{{item.SVRIP}}",
        {%- endif -%}
        {#- --- 条件必选：SVRIPMODE=IP 时必选 --- -#}
        {%- if item.SVRIPMODE == 'IP' -%}
            SVRIPMASKTYPE={{item.SVRIPMASKTYPE}},
        {%- endif -%}
        {#- --- 条件必选：SVRIPMASKTYPE=IPTYPE 时必选 --- -#}
        {%- if item.SVRIPMASKTYPE == 'IPTYPE' -%}
            SVRIPMASK="{{item.SVRIPMASK}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 1.2.2 配置FlowFilter。

```jinja2
{%- if is_scenario_app_based -%}
    {%- for item in add_flowfilter_list -%}
        ADD FLOWFILTER:
        {#- --- 必选参数 --- -#}
        FLOWFILTERNAME="{{item.FLOWFILTERNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 1.2.3 将Filter绑定到FlowFilter。

```jinja2
{%- if is_scenario_app_based -%}
    {%- for item in add_fltbindflowf_list -%}
        ADD FLTBINDFLOWF:
        {#- --- 必选参数 --- -#}
        FLOWFILTERNAME="{{item.FLOWFILTERNAME}}",
        FILTERNAME="{{item.FILTERNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 1.2.4 刷新Filter配置。

```jinja2
{%- if is_scenario_app_based -%}
    {%- for item in set_refreshsrv_list -%}
        SET REFRESHSRV:
        {#- --- 必选参数 --- -#}
        REFRESHTYPE={{item.REFRESHTYPE}},
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 1.3 配置带宽管理使用的业务策略组合。

##### 1.3.1 配置带宽管理使用的规则，当根据CategoryProp区分业务时，BWM Rule与Rule通过策略名称关联。

```jinja2
{%- if is_scenario_app_based -%}
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
        {#- --- 条件必选：POLICYTYPE=MTP/BWM/WEBPROXY 时必选 --- -#}
        {%- if item.POLICYTYPE in ['MTP', 'BWM', 'WEBPROXY'] -%}
            POLICYNAME="{{item.POLICYNAME}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 1.3.2 配置User Profile。

```jinja2
{%- if is_scenario_app_based -%}
    {%- for item in add_userprofile_list -%}
        ADD USERPROFILE:
        {#- --- 必选参数 --- -#}
        USERPROFILENAME="{{item.USERPROFILENAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 1.3.3 增加带宽管理用户组User Profile绑定。

```jinja2
{%- if is_scenario_app_based -%}
    {%- for item in add_upbindbwmusrg_list -%}
        ADD UPBINDBWMUSRG:
        {#- --- 必选参数 --- -#}
        USERGROUPNAME="{{item.USERGROUPNAME}}",
        USERPROFILENAME="{{item.USERPROFILENAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 1.3.4 将User Profile指定为全局User Profile。

```jinja2
{%- if is_scenario_app_based -%}
    {%- for item in add_localuserprof_list -%}
        ADD LOCALUSERPROF:
        {#- --- 必选参数 --- -#}
        USERPROFILENAME="{{item.USERPROFILENAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

##### **ADD LOCALUSERPROF**命令的“USERPROFILENAME”和**ADD USERPROFILE**命令的“USERPROFILENAME”必须配置为相同值。

##### 1.3.5 将配置的Rule绑定到User Profile。

```jinja2
{%- if is_scenario_app_based -%}
    {%- for item in add_rulebinding_list -%}
        ADD RULEBINDING:
        {#- --- 必选参数 --- -#}
        USERPROFILENAME="{{item.USERPROFILENAME}}",
        RULENAME="{{item.RULENAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

### 2 配置全局带宽规则，对MPF上所有用户的所有业务进行带宽管理。

#### 2.1 配置BWM控制器，设置CAR参数。

```jinja2
{%- if is_scenario_global -%}
    {%- for item in add_bwmcontroller_list_2 -%}
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
{%- endif -%}
```

#### 2.2 配置BWM控制器中的用户组级业务带宽和连接数等配置数据是基于业务处理单元生效还是整机生效。

```jinja2
{%- if is_scenario_global -%}
    {%- for item in set_bandwidthmng_list_1 -%}
        SET BANDWIDTHMNG:
        {#- --- 可选参数 --- -#}
        {%- if item.RANGE is not none -%}
            RANGE={{item.RANGE}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 2.3 定义带宽管理用户组，配置优先级和业务类型。

```jinja2
{%- if is_scenario_global -%}
    {%- for item in add_bwmusergroup_list_1 -%}
        ADD BWMUSERGROUP:
        {#- --- 必选参数 --- -#}
        USERGROUPTYPE={{item.USERGROUPTYPE}},
        {#- --- 可选参数 --- -#}
        {%- if item.USERGLEVSRVTYPE is not none -%}
            USERGLEVSRVTYPE={{item.USERGLEVSRVTYPE}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 2.4 配置用户组级带宽控制规则。

```jinja2
{%- if is_scenario_global -%}
    {%- for item in add_bwmrule_list_1 -%}
        ADD BWMRULE:
        {#- --- 必选参数 --- -#}
        USERGROUPTYPE={{item.USERGROUPTYPE}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：USERGROUPTYPE=DEFAULT_GROUP/SPECIFIC_GROUP 时必选 --- -#}
        {%- if item.USERGROUPTYPE in ['DEFAULT_GROUP', 'SPECIFIC_GROUP'] -%}
            BWMRULETYPE={{item.BWMRULETYPE}},
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
{%- endif -%}
```


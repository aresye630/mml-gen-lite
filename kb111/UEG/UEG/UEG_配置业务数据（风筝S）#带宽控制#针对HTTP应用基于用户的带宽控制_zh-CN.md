---
id: ''
name: 针对HTTP应用基于用户的带宽控制
ne_type: UEG
type: feature
description: 为了保护带宽资源不被HTTP流量吞噬，确保应用公平分享带宽资源，UEG基于用户对HTTP流量进行流量监管。  适用于PGW-U、UPF。
tags: []
risk_level: ''
doc_source: ["网络部署","地市共享式（仅连接）","5GC toB 部署边缘站点（站点为“风筝S”，共享式）","配置业务数据（风筝S）","带宽控制","针对HTTP应用基于用户的带宽控制"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
为了保护带宽资源不被HTTP流量吞噬，确保应用公平分享带宽资源，UEG基于用户对HTTP流量进行流量监管。适用于PGW-U、UPF。

## 必备事项
前提条件

* 请仔细阅读GWFD-022701 基于业务感知的带宽控制。
* UEG与网络实体之间的网络环境已经构建完成。
* 完成SIG知识库加载。
* 知名端口已经配置完成。
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
    add_bwmservice_list:
      type: items
      properties:
        BWMSERVICENAME:
          name: '带宽控制业务名称'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: '-'
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
        PROTOCOLNAME:
          name: '协议名称'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: ''
          data_source: '本端规划'
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
          description: '推荐配置：  * CIR = 0.5 \* PIR （最大带宽建议为保证带宽的2倍） * CBS >= CIR \* 1.5 \* 1000 / 8 （保证1.5秒数据的队列缓存能力） * PBS >= PIR \* 1.5 \* 1000 / 8 （保证1.5秒数据的队列缓存能力）'
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
        CBS:
          name: '承诺突发能缓存信息的数量（字节）'
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
        PBS:
          name: '峰值突发能缓存信息的数量（字节）'
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
        PRIORITYISAWARE:
          name: 'BWM CAR优先级是否敏感'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: DISABLE
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
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV3G5TCSA01'
      SWITCH: ENABLE
    add_bwmservice_list:
    - BWMSERVICENAME: 'bs_test'
      BWMSERVICETYPE: NONTOS
      NONTOSSRVTYPE: PROTOCOL
      PROTOCOLNAME: 'http'
    add_bwmcontroller_list:
    - BWMCNAME: 'bc-up'
      CTRLTYPE: CAR
      CIR: 300
      CBS: 10000
      PIR: 500
      PBS: 12000
      GREEN: PASS
      YELLOW: PASS
      RED: DISCARD
      PRIORITYISAWARE: DISABLE
    add_bwmusergroup_list:
    - USERGROUPTYPE: SPECIFIC_GROUP
      USERGROUPNAME: 'ug_test'
      USERGROUPPRI: 1
      USERLEVSRVTYPE: NONTOS
    add_bwmrule_list:
    - USERGROUPTYPE: SPECIFIC_GROUP
      USERGROUPNAME: 'ug_test'
      BWMRULETYPE: SUBSCRIBER_SPECIFIC
      BWMRULENAME: 'br_test'
      BWMSERVICENAME: 'bs_test'
      UPBWMCTRLNAME1: 'bc-up'
      DNBWMCTRLNAME1: 'bc-down'
      BWMRULEPRI: 1
    add_apnbindbwmusrg_list:
    - USERGROUPNAME: 'ug_test'
      APN: 'apn-test'
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

#### 2.1 用HTTP协议定义BWM业务。

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
    {#- --- 条件必选：NONTOSSRVTYPE=PROTOCOL 时必选 --- -#}
    {%- if item.NONTOSSRVTYPE == 'PROTOCOL' -%}
        PROTOCOLNAME="{{item.PROTOCOLNAME}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 2.2 配置两个BWM控制器，设置CAR参数并配置带宽控制算法。

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
        {%- if item.CBS is not none -%}
            CBS={{item.CBS}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：CTRLTYPE=CAR 时可选 --- -#}
    {%- if item.CTRLTYPE == 'CAR' -%}
        {%- if item.PIR is not none -%}
            PIR={{item.PIR}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：CTRLTYPE=CAR 时可选 --- -#}
    {%- if item.CTRLTYPE == 'CAR' -%}
        {%- if item.PBS is not none -%}
            PBS={{item.PBS}},
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
    {#- --- 条件可选：CTRLTYPE=CAR 时可选 --- -#}
    {%- if item.CTRLTYPE == 'CAR' -%}
        {%- if item.PRIORITYISAWARE is not none -%}
            PRIORITYISAWARE={{item.PRIORITYISAWARE}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 进行用户级/用户组级/整机级带宽控制时，如果要优先保证用户组内标识为绿色的用户流量，则需要配置**ADD BWMCONTROLLER**“COLORISAWARE”为“ENABLE”。

#### 进行用户级/用户组级/整机级带宽控制时，如果要对不同业务区分优先级时，则需要配置**ADD BWMCONTROLLER**“PRIORITYISAWARE”为“ENABLE”，且通过**ADD BWMRULE**命令参数“BWMRULEPRI”为不同的业务配置不同的优先级。

### 3 配置带宽管理用户组。

#### 3.1 定义带宽管理用户组，配置优先级和业务类型。

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

#### 3.2 配置一条用户级带宽控制规则。

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

#### 3.3 将APN下的用户包含到该用户组。

```jinja2
{%- for item in add_apnbindbwmusrg_list -%}
    ADD APNBINDBWMUSRG:
    {#- --- 必选参数 --- -#}
    USERGROUPNAME="{{item.USERGROUPNAME}}",
    APN="{{item.APN}}",
    ;
{%- endfor -%}
```


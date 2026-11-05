---
id: ''
name: 基于时间段的带宽控制
ne_type: UEG
type: feature
description: 在不同的时间段，对P2P流量进行不同规则的流量控制。  适用于PGW-U、UPF。
tags: []
risk_level: ''
doc_source: ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（火电专网，入驻式）","部署配置指导","子园区部署入驻式UEG-M","配置业务数据（风筝M）","配置业务数据（UEG）","带宽控制配置","基于时间段的带宽控制"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
在不同的时间段，对P2P流量进行不同规则的流量控制。适用于PGW-U、UPF。

## 必备事项
前提条件

* 请仔细阅读GWFD-022701 基于业务感知的带宽控制。
* UEG与网络实体之间的网络环境已经构建完成。
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
        TOSCFGTYPE:
          name: 'Tos配置类型'
          type: string
          enum:
          - CLASS
          - TOS_VALUE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        TOSCLASSTYPE:
          name: 'Tos分类类型'
          type: string
          enum:
          - AF1
          - AF2
          - AF3
          - AF4
          - BE
          - CS6
          - CS7
          - EF
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
        YELLOWREMARKT:
          name: '黄色重标记类型'
          type: string
          enum:
          - DSCPCLASS
          - DSCPVALUE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        YELLOWREMARKV:
          name: '黄色重标记值'
          type: integer
          minimum: 0
          maximum: 63
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
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
    add_timerange_list:
      type: items
      properties:
        TIMERANGENAME:
          name: '时间段名称'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_peritimerange_list:
      type: items
      properties:
        TIMERANGENAME:
          name: '时间段名称'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PERITMRANGESEQ:
          name: '周期时间段序号'
          type: integer
          minimum: 1
          maximum: 32
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        PERITIMETYPE:
          name: '周期时间段配置方式'
          type: string
          enum:
          - DAYSOFWEEK
          - STARTTOEND
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        DAYOFWEEK:
          name: '周日期'
          type: string
          enum:
          - DAILY
          - FRIDAY
          - MONDAY
          - OFFDAY
          - SATURDAY
          - SUNDAY
          - THURSDAY
          - TUESDAY
          - WEDNESDAY
          - WORKINGDAY
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        STARTTIME:
          name: '起始时间，格式HH:MM'
          type: string
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: 'HH&MM'
        ENDTIME:
          name: '结束时间，格式HH:MM'
          type: string
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: 'HH&MM'
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
        USERGLEVSRVTYPE:
          name: '用户组级业务类型'
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
          description: 'BwmService已通过**ADD BWMSERVICE**命令配置；  BwmController已通过  **ADD BWMCONTROLLER**命令配置。  绑定的时间段已通过**ADD TIMERANGE**命令配置。'
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
        TIMERANGENAME1:
          name: '时间段名称一'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        UPBWMCTRLNAME2:
          name: '上行带宽管理控制器名称二'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        DNBWMCTRLNAME2:
          name: '下行带宽管理控制器名称二'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        TIMERANGENAME2:
          name: '时间段名称二'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        UPBWMCTRLNAME3:
          name: '上行带宽管理控制器名称三'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        DNBWMCTRLNAME3:
          name: '下行带宽管理控制器名称三'
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
          description: '通过**ADD UPAPN**命令配置，可以使用**LST UPAPN**命令进行查询。'
          data_source: '本端规划'
          pattern: ''
          default: ''
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV3G5TCSA01'
      SWITCH: ENABLE
    add_bwmservice_list:
    - BWMSERVICENAME: 'my-bwm-service8'
      BWMSERVICETYPE: TOS
      TOSCFGTYPE: CLASS
      TOSCLASSTYPE: CS7
    add_bwmcontroller_list:
    - BWMCNAME: 'bc1'
      CTRLTYPE: CAR
      CIR: 30
      CBS: 1000
      PIR: 50
      PBS: 1200
      GREEN: PASS
      YELLOW: REMARK
      YELLOWREMARKT: DSCPVALUE
      YELLOWREMARKV: 10
      RED: DISCARD
    add_timerange_list:
    - TIMERANGENAME: 'timerange1'
    add_peritimerange_list:
    - TIMERANGENAME: 'timerange1'
      PERITMRANGESEQ: 1
      PERITIMETYPE: DAYSOFWEEK
      DAYOFWEEK: DAILY
      STARTTIME: '8&30'
      ENDTIME: '10&00'
    add_bwmusergroup_list:
    - USERGROUPTYPE: SPECIFIC_GROUP
      USERGROUPNAME: 'ugroup8'
      USERGROUPPRI: 1
      USERGLEVSRVTYPE: TOS
    add_bwmrule_list:
    - USERGROUPTYPE: SPECIFIC_GROUP
      USERGROUPNAME: 'ugroup8'
      BWMRULETYPE: GROUP_SPECIFIC
      BWMRULENAME: 'my-bw-rule8'
      BWMSERVICENAME: 'my-bwm-service8'
      UPBWMCTRLNAME1: 'bc2'
      DNBWMCTRLNAME1: 'bc2'
      TIMERANGENAME1: 'timerange1'
      UPBWMCTRLNAME2: 'bc3'
      DNBWMCTRLNAME2: 'bc3'
      TIMERANGENAME2: 'timerange2'
      UPBWMCTRLNAME3: 'bc1'
      DNBWMCTRLNAME3: 'bc1'
      BWMRULEPRI: 1
    add_apnbindbwmusrg_list:
    - USERGROUPNAME: 'ugroup8'
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

#### 2.1 用TOS定义BWM业务。

```jinja2
{%- for item in add_bwmservice_list -%}
    ADD BWMSERVICE:
    {#- --- 必选参数 --- -#}
    BWMSERVICENAME="{{item.BWMSERVICENAME}}",
    BWMSERVICETYPE={{item.BWMSERVICETYPE}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：BWMSERVICETYPE=TOS 时必选 --- -#}
    {%- if item.BWMSERVICETYPE == 'TOS' -%}
        TOSCFGTYPE={{item.TOSCFGTYPE}},
    {%- endif -%}
    {#- --- 条件必选：TOSCFGTYPE=CLASS 时必选 --- -#}
    {%- if item.TOSCFGTYPE == 'CLASS' -%}
        TOSCLASSTYPE={{item.TOSCLASSTYPE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 2.2 配置两个BWM控制器，设置CAR参数。

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
    {#- --- 条件必选：YELLOW=REMARK 时必选 --- -#}
    {%- if item.YELLOW == 'REMARK' -%}
        YELLOWREMARKT={{item.YELLOWREMARKT}},
    {%- endif -%}
    {#- --- 条件必选：YELLOWREMARKT=DSCPVALUE 时必选 --- -#}
    {%- if item.YELLOWREMARKT == 'DSCPVALUE' -%}
        YELLOWREMARKV={{item.YELLOWREMARKV}},
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
    ;
{%- endfor -%}
```

### 3 配置多个时间段。

```jinja2
{%- for item in add_timerange_list -%}
    ADD TIMERANGE:
    {#- --- 必选参数 --- -#}
    TIMERANGENAME="{{item.TIMERANGENAME}}",
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_peritimerange_list -%}
    ADD PERITIMERANGE:
    {#- --- 必选参数 --- -#}
    TIMERANGENAME="{{item.TIMERANGENAME}}",
    PERITMRANGESEQ={{item.PERITMRANGESEQ}},
    PERITIMETYPE={{item.PERITIMETYPE}},
    STARTTIME={{item.STARTTIME}},
    ENDTIME={{item.ENDTIME}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：PERITIMETYPE=DAYSOFWEEK 时必选 --- -#}
    {%- if item.PERITIMETYPE == 'DAYSOFWEEK' -%}
        DAYOFWEEK={{item.DAYOFWEEK}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 配置带宽管理用户组。

#### 4.1 定义带宽管理用户组，配置优先级和业务类型。

```jinja2
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
```

#### 4.2 配置带宽控制规则,设置不同时间段的带宽控制器。

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
    {#- --- 条件可选：BWMRULETYPE=GROUP_SPECIFIC/SUBSCRIBER_SPECIFIC 时可选 --- -#}
    {%- if item.BWMRULETYPE in ['GROUP_SPECIFIC', 'SUBSCRIBER_SPECIFIC'] -%}
        {%- if item.TIMERANGENAME1 is not none -%}
            TIMERANGENAME1="{{item.TIMERANGENAME1}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：BWMRULETYPE=GROUP_SPECIFIC/SUBSCRIBER_SPECIFIC 时可选 --- -#}
    {%- if item.BWMRULETYPE in ['GROUP_SPECIFIC', 'SUBSCRIBER_SPECIFIC'] -%}
        {%- if item.UPBWMCTRLNAME2 is not none -%}
            UPBWMCTRLNAME2="{{item.UPBWMCTRLNAME2}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：BWMRULETYPE=GROUP_SPECIFIC/SUBSCRIBER_SPECIFIC 时可选 --- -#}
    {%- if item.BWMRULETYPE in ['GROUP_SPECIFIC', 'SUBSCRIBER_SPECIFIC'] -%}
        {%- if item.DNBWMCTRLNAME2 is not none -%}
            DNBWMCTRLNAME2="{{item.DNBWMCTRLNAME2}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：BWMRULETYPE=GROUP_SPECIFIC/SUBSCRIBER_SPECIFIC 时可选 --- -#}
    {%- if item.BWMRULETYPE in ['GROUP_SPECIFIC', 'SUBSCRIBER_SPECIFIC'] -%}
        {%- if item.TIMERANGENAME2 is not none -%}
            TIMERANGENAME2="{{item.TIMERANGENAME2}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：BWMRULETYPE=GROUP_SPECIFIC/SUBSCRIBER_SPECIFIC 时可选 --- -#}
    {%- if item.BWMRULETYPE in ['GROUP_SPECIFIC', 'SUBSCRIBER_SPECIFIC'] -%}
        {%- if item.UPBWMCTRLNAME3 is not none -%}
            UPBWMCTRLNAME3="{{item.UPBWMCTRLNAME3}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：BWMRULETYPE=GROUP_SPECIFIC/SUBSCRIBER_SPECIFIC 时可选 --- -#}
    {%- if item.BWMRULETYPE in ['GROUP_SPECIFIC', 'SUBSCRIBER_SPECIFIC'] -%}
        {%- if item.DNBWMCTRLNAME3 is not none -%}
            DNBWMCTRLNAME3="{{item.DNBWMCTRLNAME3}}",
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 4.3 将APN下的用户包含到该用户组。

```jinja2
{%- for item in add_apnbindbwmusrg_list -%}
    ADD APNBINDBWMUSRG:
    {#- --- 必选参数 --- -#}
    USERGROUPNAME="{{item.USERGROUPNAME}}",
    APN="{{item.APN}}",
    ;
{%- endfor -%}
```


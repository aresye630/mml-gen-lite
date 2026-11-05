---
id: GWFD-110311
name: 基于切片的带宽控制
ne_type: UDG
type: feature
description: 当运营商希望对特定切片下的用户组进行带宽控制时，可参考本章节进行配置。  适用于PGW-U、UPF。
risk_level: ''
doc_source: ["特性部署","特性指南","UDG特性指南","智能策略控制功能","GWFD-110311 基于业务感知的带宽控制","激活基于业务感知的带宽控制","基于切片的带宽控制"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
当运营商希望对特定切片下的用户组进行带宽控制时，可参考本章节进行配置。适用于PGW-U、UPF。

## 必备事项
前提条件

* 请仔细阅读GWFD-110311 基于业务感知的带宽控制。
* UDG与网络实体之间的网络环境已经构建完成。
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
        OSTYPE:
          name: '操作系统类型'
          type: string
          enum:
          - ANDROID
          - IOS
          - OTHERS
          - WINDOWS
          required: false
          description: ''
          data_source: ''
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
          data_source: ''
          pattern: ''
          default: ''
        CATEPROPNAME:
          name: '分类属性名称'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PROTGROUPNAME:
          name: '协议组名称'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: ''
          data_source: ''
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
          data_source: ''
          pattern: ''
          default: DISABLE
        COLORISAWARE:
          name: 'BWM CAR颜色是否敏感'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
        QUEDEPTH:
          name: '队列深度（包）'
          type: integer
          minimum: 1
          maximum: 9600000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RATE:
          name: '速率（千比特/秒）'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SRVLEVELSPEC:
          name: '业务等级规格'
          type: integer
          minimum: 1
          maximum: 30
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 2
        USERFAIREN:
          name: '用户公平调度'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
        WORKMODE:
          name: '控制模式'
          type: string
          enum:
          - MANUAL
          - AUTO
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: MANUAL
        GREENREMARKT:
          name: '绿色重标记类型'
          type: string
          enum:
          - DSCPCLASS
          - DSCPVALUE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        REDREMARKT:
          name: '红色重标记类型'
          type: string
          enum:
          - DSCPCLASS
          - DSCPVALUE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        YELLOWREMARKT:
          name: '黄色重标记类型'
          type: string
          enum:
          - DSCPCLASS
          - DSCPVALUE
          required: false
          description: ''
          data_source: ''
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
        DNBWMCTRLNAME2:
          name: '下行带宽管理控制器名称二'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DNBWMCTRLNAME3:
          name: '下行带宽管理控制器名称三'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DNBWMCTRLNAME4:
          name: '下行带宽管理控制器名称四'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RATTYPE:
          name: 'RAT'
          type: string
          enum:
          - EUTRAN
          - GAN
          - GERAN
          - HSPA
          - LTEM
          - NONE
          - UTRAN
          - WLAN
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ROAMINGTYPE:
          name: '漫游'
          type: string
          enum:
          - HOME
          - NONE
          - ROAMING
          - VISITING
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TIMERANGENAME1:
          name: '时间段名称一'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TIMERANGENAME2:
          name: '时间段名称二'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TIMERANGENAME3:
          name: '时间段名称三'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TIMERANGENAME4:
          name: '时间段名称四'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        UPBWMCTRLNAME2:
          name: '上行带宽管理控制器名称二'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        UPBWMCTRLNAME3:
          name: '上行带宽管理控制器名称三'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        UPBWMCTRLNAME4:
          name: '上行带宽管理控制器名称四'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_snssai_list:
      type: items
      properties:
        SST:
          name: '切片/服务类型'
          type: integer
          minimum: 0
          maximum: 255
          required: true
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        SD:
          name: '切片区分码'
          type: string
          minLength: 6
          maxLength: 6
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_snssaiupintf_list:
      type: items
      properties:
        SST:
          name: '切片/服务类型'
          type: integer
          minimum: 0
          maximum: 255
          required: true
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        SD:
          name: '切片区分码'
          type: string
          minLength: 0
          maxLength: 6
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        N3LOGICINF:
          name: 'N3逻辑接口名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_snssaibwmusrg_list:
      type: items
      properties:
        USERGROUPNAME:
          name: '用户组名称'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: 'USERGROUPNAME已通过**ADD BWMUSERGROUP**命令配置。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SST:
          name: '切片/服务类型'
          type: integer
          minimum: 0
          maximum: 255
          required: true
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        SD:
          name: '切片区分码'
          type: string
          minLength: 0
          maxLength: 6
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
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
          description: '* CPU：当前已经有用户组级带宽配置的前提下，建议配置该参数。 * SYSTEM：如果是新建局点，建议配置该参数。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        CIRMINTHRES:
          name: '承诺信息速率最低保护值（千比特每秒）'
          type: integer
          minimum: 0
          maximum: 629145600
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PIRMINTHRES:
          name: '峰值信息速率最低保护值（千比特每秒）'
          type: integer
          minimum: 0
          maximum: 629145600
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        BWMSUBSCRCTRL:
          name: '用户级业务带宽控制选项'
          type: string
          enum:
          - BWM_RULE_IGNORE
          - PCC_RULE_IGNORE
          - PCC_RULE_PRIOR
          required: false
          description: '基于切片的用户带宽管理规则使用BWM rule规则，因此该参数配置为PCC\_RULE\_IGNORE。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        ADJUSTVALUE:
          name: '调整系数'
          type: integer
          minimum: 0
          maximum: 100
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PERIOD:
          name: '统计周期（秒）'
          type: integer
          minimum: 5
          maximum: 60
          required: false
          description: ''
          data_source: ''
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
      PROTOCOLNAME: 'bt'
      OSTYPE: ''
      TOSCFGTYPE: ''
      CATEPROPNAME: ''
      PROTGROUPNAME: ''
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
      COLORISAWARE: DISABLE
      QUEDEPTH: ''
      RATE: ''
      SRVLEVELSPEC: 2
      USERFAIREN: DISABLE
      WORKMODE: MANUAL
      GREENREMARKT: ''
      REDREMARKT: ''
      YELLOWREMARKT: ''
    add_bwmusergroup_list:
    - USERGROUPTYPE: SPECIFIC_GROUP
      USERGROUPNAME: 'ug_test'
      USERGROUPPRI: 1
      USERGLEVSRVTYPE: NONTOS
    add_bwmrule_list:
    - USERGROUPTYPE: SPECIFIC_GROUP
      USERGROUPNAME: 'ug_test'
      BWMRULETYPE: GROUP_SPECIFIC
      BWMRULENAME: 'br_test'
      BWMSERVICENAME: 'bs_test'
      UPBWMCTRLNAME1: 'bc-up'
      DNBWMCTRLNAME1: 'bc-down'
      BWMRULEPRI: 1
      DNBWMCTRLNAME2: ''
      DNBWMCTRLNAME3: ''
      DNBWMCTRLNAME4: ''
      RATTYPE: ''
      ROAMINGTYPE: ''
      TIMERANGENAME1: ''
      TIMERANGENAME2: ''
      TIMERANGENAME3: ''
      TIMERANGENAME4: ''
      UPBWMCTRLNAME2: ''
      UPBWMCTRLNAME3: ''
      UPBWMCTRLNAME4: ''
    add_snssai_list:
    - SST: 1
      SD: '123456'
    add_snssaiupintf_list:
    - SST: 1
      SD: '123456'
      N3LOGICINF: 'n3if1/1/1'
    add_snssaibwmusrg_list:
    - USERGROUPNAME: 'ug_test'
      SST: 1
      SD: '123456'
    set_bandwidthmng_list:
    - RANGE: SYSTEM
      CIRMINTHRES: 300000
      PIRMINTHRES: 500000
      BWMSUBSCRCTRL: PCC_RULE_IGNORE
      ADJUSTVALUE: ''
      PERIOD: ''
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

### 2 配置BWM业务。

#### 2.1 用NONTOS定义BWM业务。

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
    {#- --- 条件必选：NONTOSSRVTYPE=CATEGORY_PROP 时必选 --- -#}
    {%- if item.NONTOSSRVTYPE == 'CATEGORY_PROP' -%}
        CATEPROPNAME="{{item.CATEPROPNAME}}",
    {%- endif -%}
    {#- --- 条件必选：NONTOSSRVTYPE=PROTOCOLGROUP 时必选 --- -#}
    {%- if item.NONTOSSRVTYPE == 'PROTOCOLGROUP' -%}
        PROTGROUPNAME="{{item.PROTGROUPNAME}}",
    {%- endif -%}
    {#- --- 条件必选：BWMSERVICETYPE=TOS 时必选 --- -#}
    {%- if item.BWMSERVICETYPE == 'TOS' -%}
        TOSCFGTYPE={{item.TOSCFGTYPE}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：BWMSERVICETYPE=NONTOS 时可选 --- -#}
    {%- if item.BWMSERVICETYPE == 'NONTOS' -%}
        {%- if item.OSTYPE is not none -%}
            OSTYPE={{item.OSTYPE}},
        {%- endif -%}
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
    {#- --- 条件必选：GREEN=REMARK 时必选 --- -#}
    {%- if item.GREEN == 'REMARK' -%}
        GREENREMARKT={{item.GREENREMARKT}},
    {%- endif -%}
    {#- --- 条件必选：CTRLTYPE=SHAPING 时必选 --- -#}
    {%- if item.CTRLTYPE == 'SHAPING' -%}
        QUEDEPTH={{item.QUEDEPTH}},
    {%- endif -%}
    {#- --- 条件必选：CTRLTYPE=SHAPING 时必选 --- -#}
    {%- if item.CTRLTYPE == 'SHAPING' -%}
        RATE={{item.RATE}},
    {%- endif -%}
    {#- --- 条件必选：RED=REMARK 时必选 --- -#}
    {%- if item.RED == 'REMARK' -%}
        REDREMARKT={{item.REDREMARKT}},
    {%- endif -%}
    {#- --- 条件必选：YELLOW=REMARK 时必选 --- -#}
    {%- if item.YELLOW == 'REMARK' -%}
        YELLOWREMARKT={{item.YELLOWREMARKT}},
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
    {#- --- 条件可选：CTRLTYPE=CAR 时可选 --- -#}
    {%- if item.CTRLTYPE == 'CAR' -%}
        {%- if item.COLORISAWARE is not none -%}
            COLORISAWARE={{item.COLORISAWARE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：CTRLTYPE=CAR/SHAPING 时可选 --- -#}
    {%- if item.CTRLTYPE in ['CAR', 'SHAPING'] -%}
        {%- if item.SRVLEVELSPEC is not none -%}
            SRVLEVELSPEC={{item.SRVLEVELSPEC}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：CTRLTYPE=SHAPING 时可选 --- -#}
    {%- if item.CTRLTYPE == 'SHAPING' -%}
        {%- if item.USERFAIREN is not none -%}
            USERFAIREN={{item.USERFAIREN}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：CTRLTYPE=SHAPING 时可选 --- -#}
    {%- if item.CTRLTYPE == 'SHAPING' -%}
        {%- if item.WORKMODE is not none -%}
            WORKMODE={{item.WORKMODE}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 进行用户级/用户组级/整机级带宽控制时，如果要优先保证用户组内标识为绿色的用户流量，则需要配置**ADD BWMCONTROLLER**“COLORISAWARE”为“ENABLE”。

### 3 配置带宽管理用户组。

#### 3.1 定义带宽管理用户组，配置优先级和业务类型。

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

#### 3.2 配置用户组级带宽控制规则。

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
        {%- if item.DNBWMCTRLNAME2 is not none -%}
            DNBWMCTRLNAME2="{{item.DNBWMCTRLNAME2}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：BWMRULETYPE=GROUP_SPECIFIC/SUBSCRIBER_SPECIFIC 时可选 --- -#}
    {%- if item.BWMRULETYPE in ['GROUP_SPECIFIC', 'SUBSCRIBER_SPECIFIC'] -%}
        {%- if item.DNBWMCTRLNAME3 is not none -%}
            DNBWMCTRLNAME3="{{item.DNBWMCTRLNAME3}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：BWMRULETYPE=GROUP_SPECIFIC/SUBSCRIBER_SPECIFIC 时可选 --- -#}
    {%- if item.BWMRULETYPE in ['GROUP_SPECIFIC', 'SUBSCRIBER_SPECIFIC'] -%}
        {%- if item.DNBWMCTRLNAME4 is not none -%}
            DNBWMCTRLNAME4="{{item.DNBWMCTRLNAME4}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：BWMRULETYPE=GROUP_SPECIFIC/SUBSCRIBER_SPECIFIC 时可选 --- -#}
    {%- if item.BWMRULETYPE in ['GROUP_SPECIFIC', 'SUBSCRIBER_SPECIFIC'] -%}
        {%- if item.RATTYPE is not none -%}
            RATTYPE={{item.RATTYPE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：BWMRULETYPE=GROUP_SPECIFIC/SUBSCRIBER_SPECIFIC 时可选 --- -#}
    {%- if item.BWMRULETYPE in ['GROUP_SPECIFIC', 'SUBSCRIBER_SPECIFIC'] -%}
        {%- if item.ROAMINGTYPE is not none -%}
            ROAMINGTYPE={{item.ROAMINGTYPE}},
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
        {%- if item.TIMERANGENAME2 is not none -%}
            TIMERANGENAME2="{{item.TIMERANGENAME2}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：BWMRULETYPE=GROUP_SPECIFIC/SUBSCRIBER_SPECIFIC 时可选 --- -#}
    {%- if item.BWMRULETYPE in ['GROUP_SPECIFIC', 'SUBSCRIBER_SPECIFIC'] -%}
        {%- if item.TIMERANGENAME3 is not none -%}
            TIMERANGENAME3="{{item.TIMERANGENAME3}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：BWMRULETYPE=GROUP_SPECIFIC/SUBSCRIBER_SPECIFIC 时可选 --- -#}
    {%- if item.BWMRULETYPE in ['GROUP_SPECIFIC', 'SUBSCRIBER_SPECIFIC'] -%}
        {%- if item.TIMERANGENAME4 is not none -%}
            TIMERANGENAME4="{{item.TIMERANGENAME4}}",
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
        {%- if item.UPBWMCTRLNAME3 is not none -%}
            UPBWMCTRLNAME3="{{item.UPBWMCTRLNAME3}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：BWMRULETYPE=GROUP_SPECIFIC/SUBSCRIBER_SPECIFIC 时可选 --- -#}
    {%- if item.BWMRULETYPE in ['GROUP_SPECIFIC', 'SUBSCRIBER_SPECIFIC'] -%}
        {%- if item.UPBWMCTRLNAME4 is not none -%}
            UPBWMCTRLNAME4="{{item.UPBWMCTRLNAME4}}",
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 配置网络切片和带宽管理用户组的绑定关系。

#### 4.1 添加一个新的网络切片选择标识。

```jinja2
{%- for item in add_snssai_list -%}
    ADD SNSSAI:
    {#- --- 必选参数 --- -#}
    SST={{item.SST}},
    {#- --- 可选参数 --- -#}
    {%- if item.SD is not none -%}
        SD="{{item.SD}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 4.2 增加网络切片和逻辑接口绑定关系。

```jinja2
{%- for item in add_snssaiupintf_list -%}
    ADD SNSSAIUPINTF:
    {#- --- 必选参数 --- -#}
    SST={{item.SST}},
    N3LOGICINF="{{item.N3LOGICINF}}",
    {#- --- 可选参数 --- -#}
    {%- if item.SD is not none -%}
        SD="{{item.SD}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 4.3 绑定网络切片到带宽管理用户组。

```jinja2
{%- for item in add_snssaibwmusrg_list -%}
    ADD SNSSAIBWMUSRG:
    {#- --- 必选参数 --- -#}
    USERGROUPNAME="{{item.USERGROUPNAME}}",
    SST={{item.SST}},
    {#- --- 可选参数 --- -#}
    {%- if item.SD is not none -%}
        SD="{{item.SD}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 5 配置BWM控制器中的用户组级业务带宽和连接数的生效范围（CPU、整机），以及配置基于切片的带宽控制规则使用BWM Rule。

```jinja2
{%- for item in set_bandwidthmng_list -%}
    SET BANDWIDTHMNG:
    {#- --- 可选参数 --- -#}
    {%- if item.RANGE is not none -%}
        RANGE={{item.RANGE}},
    {%- endif -%}
    {%- if item.BWMSUBSCRCTRL is not none -%}
        BWMSUBSCRCTRL={{item.BWMSUBSCRCTRL}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：RANGE=SYSTEM 时可选 --- -#}
    {%- if item.RANGE == 'SYSTEM' -%}
        {%- if item.CIRMINTHRES is not none -%}
            CIRMINTHRES={{item.CIRMINTHRES}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：RANGE=SYSTEM 时可选 --- -#}
    {%- if item.RANGE == 'SYSTEM' -%}
        {%- if item.PIRMINTHRES is not none -%}
            PIRMINTHRES={{item.PIRMINTHRES}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：RANGE=SYSTEM 时可选 --- -#}
    {%- if item.RANGE == 'SYSTEM' -%}
        {%- if item.ADJUSTVALUE is not none -%}
            ADJUSTVALUE={{item.ADJUSTVALUE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：RANGE=SYSTEM 时可选 --- -#}
    {%- if item.RANGE == 'SYSTEM' -%}
        {%- if item.PERIOD is not none -%}
            PERIOD={{item.PERIOD}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```


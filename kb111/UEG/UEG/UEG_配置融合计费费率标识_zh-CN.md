---
id: ''
name: 配置融合计费费率标识
ne_type: UEG
type: feature
description: 费率标识可以是费率组（Rating Group，RG）；也可以是费率组（Rating Group，RG）+业务ID（Service ID，SID）即（RG，SID）。使用（RG，SID）做费率标识可以进行更细粒度的配额管理。SMF支持内容计费，即按用户使用的业务粒度进行计费。对应内容计费的不同的业务，对应的费率标识不同。  适用于SMF。
tags: []
risk_level: ''
doc_source: ["网络部署","园区入驻+地市共享（连接+计算）","5GC toB 部署边缘站点（站点为“风筝M”，带计算）","配置业务数据（风筝M）","配置业务数据（UEG）","计费功能配置","部署应急SMF","配置融合计费费率标识"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
费率标识可以是费率组（Rating Group，RG）；也可以是费率组（Rating Group，RG）+业务ID（Service ID，SID）即（RG，SID）。使用（RG，SID）做费率标识可以进行更细粒度的配额管理。SMF支持内容计费，即按用户使用的业务粒度进行计费。对应内容计费的不同的业务，对应的费率标识不同。适用于SMF。

## 必备事项
前提条件

* 请详细阅读融合计费原理。
* 使用内容计费时，已申请内容计费的License项。
* 完成加载License。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    add_cpurr_list:
      type: items
      properties:
        URRNAME:
          name: '使用量上报规则名称'
          type: string
          maxLength: 31
          required: true
          description: '配置业务在线计费URR。  URRID、USAGERPTMODE、ONLMETERINGTYPE在SMF和UPF上的配置需要保持一致。'
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
          data_source: '全网规划'
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
          data_source: '全网规划'
          pattern: ''
          default: ''
        ONLCOMPOUNDTYPE:
          name: '在线计费标识组成类型'
          type: string
          enum:
          - ONLYRG
          - RGSID
          required: false
          description: '根据业务套餐情况，确定使用RG还是（RG，SID）作为费率标识。  此处以使用RG作为费率标识为例。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        ONLINERG:
          name: '在线计费组'
          type: integer
          minimum: 0
          maximum: 4294967294
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
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
          description: '根据业务套餐情况，确定使用免费、按时长计费、按流量计费，还是按照流量+时长计费。  此处以按流量计费为例。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        OFFCOMPOUNDTYPE:
          name: '离线计费标识组成类型'
          type: string
          enum:
          - ONLYRG
          - ONLYSID
          - RGSID
          - UPDOWNSID
          required: false
          description: '根据业务套餐情况，确定使用RG还是（RG，SID）作为费率标识。  此处以使用RG作为费率标识为例。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        RG:
          name: '离线计费组'
          type: integer
          minimum: 0
          maximum: 4294967294
          required: false
          description: '-'
          data_source: '本端规划'
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
          description: '根据业务套餐情况，确定使用免费、按时长计费、按流量计费，还是按照流量+时长计费。  此处以按流量计费为例。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_cpurrgroup_list:
      type: items
      properties:
        URRGROUPNAME:
          name: '使用量上报规则组名称'
          type: string
          maxLength: 31
          required: true
          description: '配置URRGROUP。  说明：  * 当**SET USRPROFCHARGE** 、**SET APNCHARGECTRL**、**ADD CHARGEMETHOD**命令的“RGAPPLIED”配置为“DEFAULT”时，URRGROUP下不能同时配置离线和在线URR。 * 当“RGAPPLIED”配置为“ONLINERGONLY”或“OFFLINERGONLY”时，URRGROUP下建议同时配置离线和在线URR。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        UPURRNAME1:
          name: '上行发起URR名称1'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        DOWNURRNAME1:
          name: '下行发起URR名称1'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        UPURRNAME2:
          name: '上行发起URR名称2'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        DOWNURRNAME2:
          name: '下行发起URR名称2'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_cppccpolicygrp_list:
      type: items
      properties:
        PCCPOLICYGRPNM:
          name: 'PCC策略组名称'
          type: string
          maxLength: 63
          required: true
          description: '配置PCC业务策略组。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        URRGROUPNAME:
          name: 'URR组名称'
          type: string
          maxLength: 31
          required: false
          description: '使用**ADD CPURRGROUP**命令定义的“URRGROUPNAME”。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_cprule_list:
      type: items
      properties:
        RULENAME:
          name: '规则名称'
          type: string
          maxLength: 63
          required: true
          description: '配置规则，并绑定已配置的PCC策略组。  SMF、UPF上RULENAME以及RULE下配置的POLICYTYPE、POLICYNAME需要保持一致。'
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
          - FUP
          - HEADEN
          - IPREDIR
          - LBO
          - NON_SPECIFIC_TYPE
          - PCC
          - QOS
          - REMARK_FPI
          - SMARTREDIRECT
          - SRV_TRIGGER
          - TRAFFICCLASS
          - ULCL
          - WEBPROXY
          required: true
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: ''
        PRIORITY:
          name: '全局优先级'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: false
          description: '取值越小，优先级越高。'
          data_source: '本端规划'
          pattern: ''
          default: 4294967295
        POLICYNAME:
          name: '策略名称'
          type: string
          maxLength: 63
          required: false
          description: '使用**ADD CPPCCPOLICYGRP**命令定义的“PCCPOLICYGRPNM”。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_cpuserprofile_list:
      type: items
      properties:
        USERPROFILENAME:
          name: '用户模板名称'
          type: string
          maxLength: 63
          required: true
          description: '添加User Profile。  USERPROFILE的名称统一规划，保证在PCF、SMF、UPF间名称一致。不一致时PCF下发的策略无法生效。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        UPTYPE:
          name: '用户模板类型'
          type: string
          enum:
          - PCC
          - ULCL
          - UPSELECT
          required: true
          description: '指定PCC类型用户模板。'
          data_source: '全网规划'
          pattern: ''
          default: PCC
    set_cpurrgrpbinding_list:
      type: items
      properties:
        USERPROFILENAME:
          name: '用户模板名称'
          type: string
          maxLength: 63
          required: true
          description: '设置用户模板的计费属性绑定关系。如果UserProfile下不绑定默认计费属性，用户的数据包按全局计费属性计费。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        DFTURRGRPNAME:
          name: '缺省URR组名称'
          type: string
          maxLength: 31
          required: false
          description: '指定缺省URR组名称，使用**ADD CPURRGROUP**命令配置生成。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_cprulebinding_list:
      type: items
      properties:
        USERPROFILENAME:
          name: '用户模板名称'
          type: string
          maxLength: 63
          required: true
          description: '使用**ADD CPUSERPROFILE**命令定义的“USERPROFILENAME”。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        RULENAME:
          name: '规则名称'
          type: string
          maxLength: 63
          required: true
          description: '使用**ADD CPRULE**命令定义的**RULENAME**。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_usrprofgroup_list:
      type: items
      properties:
        USERPROFGNAME:
          name: '用户模板组名称'
          type: string
          maxLength: 63
          required: true
          description: '配置一个用户模板组。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_upbindupg_list:
      type: items
      properties:
        USERPROFGNAME:
          name: '用户模板组名称'
          type: string
          maxLength: 63
          required: true
          description: '使用**ADD USRPROFGROUP**命令定义的“USERPROFGNAME”。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        UPBINDTYPE:
          name: '用户模板绑定类型'
          type: string
          enum:
          - DEFAULT
          - SPECIFIC
          - ULCL
          required: true
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: ''
        PRIORITY:
          name: '优先级'
          type: integer
          minimum: 1
          maximum: 65534
          required: false
          description: '取值越小，优先级越高。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        USERPROFILENAME:
          name: '用户模板名称'
          type: string
          maxLength: 63
          required: false
          description: '使用**ADD CPUSERPROFILE**命令定义的“USERPROFILENAME”。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_cpapn_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        HASVPN:
          name: '绑定VPN'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
        HASVPNIPV6:
          name: '绑定IPv6 VPN'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
        RESTORPGWSWITCH:
          name: '故障重启业务恢复功能PGW开关'
          type: string
          enum:
          - ENABLE
          - INHERIT
          - DISABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: INHERIT
    add_apnusrprofg_list:
      type: items
      properties:
        APN:
          name: 'APN'
          type: string
          maxLength: 63
          required: true
          description: '使用**ADD CPAPN**命令定义的“APN”。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        USERPROFGNAME:
          name: '用户模板组名称'
          type: string
          maxLength: 63
          required: true
          description: '使用**ADD USRPROFGROUP**命令定义的“USERPROFGNAME”。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
  examples:
    add_cpurr_list:
    - URRNAME: 'urr_online_URL'
      URRID: 2300
      USAGERPTMODE: ONLINE
      ONLCOMPOUNDTYPE: ONLYRG
      ONLINERG: 100
      ONLMETERINGTYPE: VOLUME
      OFFCOMPOUNDTYPE: ONLYRG
      RG: 1100
      OFFMETERINGTYPE: VOLUME
    add_cpurrgroup_list:
    - URRGROUPNAME: 'UrrGp_URL'
      UPURRNAME1: 'urr_online_URL'
      DOWNURRNAME1: 'urr_online_URL'
      UPURRNAME2: 'urr_offline_URL'
      DOWNURRNAME2: 'urr_offline_URL'
    add_cppccpolicygrp_list:
    - PCCPOLICYGRPNM: 'pccpolicy_URL'
      URRGROUPNAME: 'UrrGp_URL'
    add_cprule_list:
    - RULENAME: 'Rule001_dns'
      POLICYTYPE: PCC
      PRIORITY: 100
      POLICYNAME: 'pccpolicy_URL'
    add_cpuserprofile_list:
    - USERPROFILENAME: 'userprofile001'
      UPTYPE: PCC
    set_cpurrgrpbinding_list:
    - USERPROFILENAME: 'userprofile001'
      DFTURRGRPNAME: 'UrrGp_abnormal'
    add_cprulebinding_list:
    - USERPROFILENAME: 'userprofile001'
      RULENAME: 'Rule001_dns'
    add_usrprofgroup_list:
    - USERPROFGNAME: 'upg_test'
    add_upbindupg_list:
    - USERPROFGNAME: 'upg_test'
      UPBINDTYPE: SPECIFIC
      PRIORITY: 10
      USERPROFILENAME: 'userprofile001'
    add_cpapn_list:
    - APN: 'apn-test'
      HASVPN: DISABLE
      HASVPNIPV6: DISABLE
      RESTORPGWSWITCH: INHERIT
    add_apnusrprofg_list:
    - APN: 'apn-test'
      USERPROFGNAME: 'upg_test'
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 配置内容计费费率标识。

#### 1.1 配置内容计费使用的URR组及相应URR。

##### 1.1.1 配置URR。

```jinja2
{%- for item in add_cpurr_list -%}
    ADD CPURR:
    {#- --- 必选参数 --- -#}
    URRNAME="{{item.URRNAME}}",
    URRID={{item.URRID}},
    USAGERPTMODE={{item.USAGERPTMODE}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：USAGERPTMODE=ONLINE 时必选 --- -#}
    {%- if item.USAGERPTMODE == 'ONLINE' -%}
        ONLCOMPOUNDTYPE={{item.ONLCOMPOUNDTYPE}},
    {%- endif -%}
    {#- --- 条件必选：ONLCOMPOUNDTYPE=RGSID/ONLYRG 时必选 --- -#}
    {%- if item.ONLCOMPOUNDTYPE in ['RGSID', 'ONLYRG'] -%}
        ONLINERG={{item.ONLINERG}},
    {%- endif -%}
    {#- --- 条件必选：USAGERPTMODE=OFFLINE 时必选 --- -#}
    {%- if item.USAGERPTMODE == 'OFFLINE' -%}
        OFFCOMPOUNDTYPE={{item.OFFCOMPOUNDTYPE}},
    {%- endif -%}
    {#- --- 条件必选：OFFCOMPOUNDTYPE=ONLYRG/RGSID 时必选 --- -#}
    {%- if item.OFFCOMPOUNDTYPE in ['ONLYRG', 'RGSID'] -%}
        RG={{item.RG}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：USAGERPTMODE=ONLINE 时可选 --- -#}
    {%- if item.USAGERPTMODE == 'ONLINE' -%}
        {%- if item.ONLMETERINGTYPE is not none -%}
            ONLMETERINGTYPE={{item.ONLMETERINGTYPE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：USAGERPTMODE=OFFLINE 时可选 --- -#}
    {%- if item.USAGERPTMODE == 'OFFLINE' -%}
        {%- if item.OFFMETERINGTYPE is not none -%}
            OFFMETERINGTYPE={{item.OFFMETERINGTYPE}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

##### 1.1.2 配置URR组，将URR绑定到URR组上。

```jinja2
{%- for item in add_cpurrgroup_list -%}
    ADD CPURRGROUP:
    {#- --- 必选参数 --- -#}
    URRGROUPNAME="{{item.URRGROUPNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.UPURRNAME1 is not none -%}
        UPURRNAME1="{{item.UPURRNAME1}}",
    {%- endif -%}
    {%- if item.DOWNURRNAME1 is not none -%}
        DOWNURRNAME1="{{item.DOWNURRNAME1}}",
    {%- endif -%}
    {%- if item.UPURRNAME2 is not none -%}
        UPURRNAME2="{{item.UPURRNAME2}}",
    {%- endif -%}
    {%- if item.DOWNURRNAME2 is not none -%}
        DOWNURRNAME2="{{item.DOWNURRNAME2}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 1.2 配置内容计费使用的Rule，将URR组绑定到对应的Rule上。

##### 1.2.1 配置PCC策略组，将URR组绑定到PCC策略组。

```jinja2
{%- for item in add_cppccpolicygrp_list -%}
    ADD CPPCCPOLICYGRP:
    {#- --- 必选参数 --- -#}
    PCCPOLICYGRPNM="{{item.PCCPOLICYGRPNM}}",
    {#- --- 可选参数 --- -#}
    {%- if item.URRGROUPNAME is not none -%}
        URRGROUPNAME="{{item.URRGROUPNAME}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

##### 1.2.2 配置Rule，将PCC策略组绑定到Rule上。

```jinja2
{%- for item in add_cprule_list -%}
    ADD CPRULE:
    {#- --- 必选参数 --- -#}
    RULENAME="{{item.RULENAME}}",
    POLICYTYPE={{item.POLICYTYPE}},
    {#- --- 可选参数 --- -#}
    {%- if item.PRIORITY is not none -%}
        PRIORITY={{item.PRIORITY}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：POLICYTYPE=PCC/ULCL/QOS 时必选 --- -#}
    {%- if item.POLICYTYPE in ['PCC', 'ULCL', 'QOS'] -%}
        POLICYNAME="{{item.POLICYNAME}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 1.3 配置UserProfile，将Rule绑定到UserProfile上。

##### 1.3.1 配置UserProfile。

```jinja2
{%- for item in add_cpuserprofile_list -%}
    ADD CPUSERPROFILE:
    {#- --- 必选参数 --- -#}
    USERPROFILENAME="{{item.USERPROFILENAME}}",
    UPTYPE={{item.UPTYPE}},
    ;
{%- endfor -%}
```

##### 1.3.2 绑定该UserProfile的缺省URR组，建议每个UserProfile都绑定缺省费率URR组。

```jinja2
{%- for item in set_cpurrgrpbinding_list -%}
    SET CPURRGRPBINDING:
    {#- --- 必选参数 --- -#}
    USERPROFILENAME="{{item.USERPROFILENAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.DFTURRGRPNAME is not none -%}
        DFTURRGRPNAME="{{item.DFTURRGRPNAME}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

##### 1.3.3 将Rule绑定到UserProfile上。

```jinja2
{%- for item in add_cprulebinding_list -%}
    ADD CPRULEBINDING:
    {#- --- 必选参数 --- -#}
    USERPROFILENAME="{{item.USERPROFILENAME}}",
    RULENAME="{{item.RULENAME}}",
    ;
{%- endfor -%}
```

#### 1.4 配置UserProfile组及DNN实例。

##### 1.4.1 配置UserProfile组，将UserProfile绑定到UserProfile组。

```jinja2
{%- for item in add_usrprofgroup_list -%}
    ADD USRPROFGROUP:
    {#- --- 必选参数 --- -#}
    USERPROFGNAME="{{item.USERPROFGNAME}}",
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_upbindupg_list -%}
    ADD UPBINDUPG:
    {#- --- 必选参数 --- -#}
    USERPROFGNAME="{{item.USERPROFGNAME}}",
    UPBINDTYPE={{item.UPBINDTYPE}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：UPBINDTYPE=SPECIFIC 时必选 --- -#}
    {%- if item.UPBINDTYPE == 'SPECIFIC' -%}
        PRIORITY={{item.PRIORITY}},
    {%- endif -%}
    {#- --- 条件必选：UPBINDTYPE=SPECIFIC/DEFAULT/ULCL 时必选 --- -#}
    {%- if item.UPBINDTYPE in ['SPECIFIC', 'DEFAULT', 'ULCL'] -%}
        USERPROFILENAME="{{item.USERPROFILENAME}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

##### 1.4.2 配置DNN实例，将UserProifle组绑定到DNN实例。

```jinja2
{%- for item in add_cpapn_list -%}
    ADD CPAPN:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    {#- --- 可选参数 --- -#}
    {%- if item.HASVPN is not none -%}
        HASVPN={{item.HASVPN}},
    {%- endif -%}
    {%- if item.HASVPNIPV6 is not none -%}
        HASVPNIPV6={{item.HASVPNIPV6}},
    {%- endif -%}
    {%- if item.RESTORPGWSWITCH is not none -%}
        RESTORPGWSWITCH={{item.RESTORPGWSWITCH}},
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_apnusrprofg_list -%}
    ADD APNUSRPROFG:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    USERPROFGNAME="{{item.USERPROFGNAME}}",
    ;
{%- endfor -%}
```

##### 每个DNN实例只能绑定一个UserProfile组。如UserProfile组和DNN实例已配置且已绑定，本步骤只需执行**ADD UPBINDUPG**命令，将UserProfile绑定到UserProfile组即可。


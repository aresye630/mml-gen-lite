---
id: ''
name: 配置融合计费费率标识
ne_type: UNC
type: feature
description: 本操作描述融合计费使用的费率标识的配置过程。  SMF与NCG/CHF(OCS)交互需要用到费率标识。费率标识可以是费率组（Rating Group，RG）；也可以是费率组（Rating Group，RG）+业务ID（Service ID，SID）即（RG，SID）。使用（RG，SID）做费率标识可以进行更细粒度的配额管理。UNC支持内容计费，即按用户使用的业务粒度进行计费。对应内容计费的不同的业务，对应的费率标识不同。
risk_level: ''
doc_source: ["网络部署","业务专题","5G Core 计费解决方案","计费解决方案概述","计费方案部署与调测","方案三：部署NCG且基于服务化接口的纯离线计费组网方案","SMF配置","配置融合计费费率标识"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本操作描述融合计费使用的费率标识的配置过程。SMF与NCG/CHF(OCS)交互需要用到费率标识。费率标识可以是费率组（Rating Group，RG）；也可以是费率组（Rating Group，RG）+业务ID（Service ID，SID）即（RG，SID）。使用（RG，SID）做费率标识可以进行更细粒度的配额管理。UNC支持内容计费，即按用户使用的业务粒度进行计费。对应内容计费的不同的业务，对应的费率标识不同。

## 必备事项
前提条件

* 请详细阅读融合计费原理。
* 使用内容计费时，已申请内容计费的License项。
* 完成加载License。
* 本操作任务涉及的APN/DNN、User Profile、User Profile group已经创建完成，并完成User Profile group与APN/DNN的绑定。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    add_urr_list:
      type: items
      properties:
        URRNAME:
          name: '使用量上报规则名称'
          type: string
          maxLength: 31
          required: true
          description: '配置业务在线计费URR。  说明：  URRID、USAGERPTMODE、OFFMETERINGTYPE需要与UPF上的配置保持一致。'
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
        DOWNSID:
          name: '离线下行业务标识'
          type: integer
          minimum: 0
          maximum: 4294967294
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SID:
          name: '离线业务标识'
          type: integer
          minimum: 0
          maximum: 4294967294
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        UPSID:
          name: '离线上行业务标识'
          type: integer
          minimum: 0
          maximum: 4294967294
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ONLINESID:
          name: '在线业务标识'
          type: integer
          minimum: 0
          maximum: 4294967294
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        EVENTRSUVALUE:
          name: '事件配额值（次）'
          type: integer
          minimum: 0
          maximum: 5000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 0
        TIMERSUVALUE:
          name: '时间配额值（秒）'
          type: integer
          minimum: 0
          maximum: 3600000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VOLUMERSUVALUE:
          name: '流量配额值（字节）'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MONITORINGKEY:
          name: '监控属性值'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        N40AGESW:
          name: 'N40接口场景下是否允许老化'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ENABLE
        OFCSRVTMPLNAME:
          name: '离线业务模板名'
          type: string
          maxLength: 63
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        REDIRENDTOKEN:
          name: 'Gy重定向结束Token'
          type: string
          maxLength: 31
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
          maxLength: 31
          required: true
          description: '配置URRGROUP。  说明：  * 当**SET USRPROFCHARGE** 、**SET APNCHARGECTRL**、**ADD CHARGEMETHOD**命令的“RGAPPLIED”配置为“DEFAULT”时，不能同时配置RG相同的离线和在线URR。 * 当“RGAPPLIED”配置为“ONLINERGONLY”或“OFFLINERGONLY”时，建议同时配置离线和在线URR。'
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
    add_pccpolicygrp_list:
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
          description: '使用**ADD URRGROUP**命令定义的“URRGROUPNAME”。'
          data_source: '已配置数据中获取'
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
          description: '配置规则，并绑定已配置的PCC策略组。  说明：  SMF、UPF上RULENAME以及RULE下配置的POLICYTYPE、POLICYNAME需要保持一致。'
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
          description: '表示该规则可以配置PCC策略，用于实现计费和策略控制功能。'
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
          description: '使用**ADD PCCPOLICYGRP**命令定义的“PCCPOLICYGRPNM”。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        FLOWFILTERNAME:
          name: '流过滤器名称'
          type: string
          maxLength: 63
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PROTODESCDL:
          name: '下行协议描述参数'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PROTODESCUL:
          name: '上行协议描述参数'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RULERANGE:
          name: '规则生效范围'
          type: string
          enum:
          - ALL
          - CENTRAL
          - LOCAL
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ALL
    set_urrgrpbinding_list:
      type: items
      properties:
        USERPROFILENAME:
          name: '用户模板名称'
          type: string
          maxLength: 63
          required: true
          description: '设置用户模板和URR Group的绑定关系。如果User Profile下不绑定默认URR Group，用户的数据包按全局URR Group计费，否则不计费。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        DFTURRGRPNAME:
          name: '缺省URR组名称'
          type: string
          maxLength: 31
          required: false
          description: '指定缺省URR组名称，使用**ADD URRGROUP**命令配置生成。'
          data_source: '已配置数据中获取'
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
          description: '使用**ADD USERPROFILE**命令定义的“USERPROFILENAME”。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        RULENAME:
          name: '规则名称'
          type: string
          maxLength: 63
          required: true
          description: '使用**ADD RULE**命令定义的**RULENAME**。  说明：  SMF、UPF上USERPROFILE下绑定的RULENAME、POLICYTYPE需要保持一致。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_quotaexhaustact_list:
      type: items
      properties:
        CCTMPLTNAME:
          name: '融合计费模板名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    add_urr_list:
    - URRNAME: 'urr_online_URL'
      URRID: 2300
      USAGERPTMODE: ONLINE
      ONLCOMPOUNDTYPE: ONLYRG
      ONLINERG: 100
      ONLMETERINGTYPE: VOLUME
      OFFCOMPOUNDTYPE: ONLYRG
      RG: 1100
      OFFMETERINGTYPE: VOLUME
      DOWNSID: ''
      SID: ''
      UPSID: ''
      ONLINESID: ''
      EVENTRSUVALUE: ''
      TIMERSUVALUE: ''
      VOLUMERSUVALUE: ''
      MONITORINGKEY: ''
      N40AGESW: ENABLE
      OFCSRVTMPLNAME: ''
      REDIRENDTOKEN: ''
    add_urrgroup_list:
    - URRGROUPNAME: 'UrrGp_URL'
      UPURRNAME1: 'urr_online_URL'
      DOWNURRNAME1: 'urr_online_URL'
      UPURRNAME2: 'urr_offline_URL'
      DOWNURRNAME2: 'urr_offline_URL'
    add_pccpolicygrp_list:
    - PCCPOLICYGRPNM: 'PPG_URL'
      URRGROUPNAME: 'UrrGp_URL'
    add_rule_list:
    - RULENAME: 'Rule001_url'
      POLICYTYPE: PCC
      PRIORITY: 100
      POLICYNAME: 'PPG_URL'
      FLOWFILTERNAME: ''
      PROTODESCDL: ''
      PROTODESCUL: ''
      RULERANGE: ALL
    set_urrgrpbinding_list:
    - USERPROFILENAME: 'userprofile001'
      DFTURRGRPNAME: 'UrrGp_abnormal'
    add_rulebinding_list:
    - USERPROFILENAME: 'userprofile001'
      RULENAME: 'Rule001_url'
    add_quotaexhaustact_list:
    - CCTMPLTNAME: ''
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 配置内容计费费率标识。

#### 1.1 配置内容计费使用的URR组及相应URR。

##### 1.1.1 配置URR。

```jinja2
{%- for item in add_urr_list -%}
    ADD URR:
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
    {#- --- 条件必选：OFFCOMPOUNDTYPE=UPDOWNSID 时必选 --- -#}
    {%- if item.OFFCOMPOUNDTYPE == 'UPDOWNSID' -%}
        DOWNSID={{item.DOWNSID}},
    {%- endif -%}
    {#- --- 条件必选：USAGERPTMODE=MONITORINGKEY 时必选 --- -#}
    {%- if item.USAGERPTMODE == 'MONITORINGKEY' -%}
        MONITORINGKEY="{{item.MONITORINGKEY}}",
    {%- endif -%}
    {#- --- 条件必选：ONLCOMPOUNDTYPE=RGSID 时必选 --- -#}
    {%- if item.ONLCOMPOUNDTYPE == 'RGSID' -%}
        ONLINESID={{item.ONLINESID}},
    {%- endif -%}
    {#- --- 条件必选：OFFCOMPOUNDTYPE=ONLYSID/RGSID 时必选 --- -#}
    {%- if item.OFFCOMPOUNDTYPE in ['ONLYSID', 'RGSID'] -%}
        SID={{item.SID}},
    {%- endif -%}
    {#- --- 条件必选：OFFCOMPOUNDTYPE=UPDOWNSID 时必选 --- -#}
    {%- if item.OFFCOMPOUNDTYPE == 'UPDOWNSID' -%}
        UPSID={{item.UPSID}},
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
    {#- --- 条件可选：ONLMETERINGTYPE=EVENT/EVENT_TIME/EVENT_VOLUME/EVENT_VOLUME_TIME 时可选 --- -#}
    {%- if item.ONLMETERINGTYPE in ['EVENT', 'EVENT_TIME', 'EVENT_VOLUME', 'EVENT_VOLUME_TIME'] -%}
        {%- if item.EVENTRSUVALUE is not none -%}
            EVENTRSUVALUE={{item.EVENTRSUVALUE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：USAGERPTMODE=OFFLINE/ONLINE 时可选 --- -#}
    {%- if item.USAGERPTMODE in ['OFFLINE', 'ONLINE'] -%}
        {%- if item.N40AGESW is not none -%}
            N40AGESW={{item.N40AGESW}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：USAGERPTMODE=OFFLINE 时可选 --- -#}
    {%- if item.USAGERPTMODE == 'OFFLINE' -%}
        {%- if item.OFCSRVTMPLNAME is not none -%}
            OFCSRVTMPLNAME="{{item.OFCSRVTMPLNAME}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：USAGERPTMODE=ONLINE 时可选 --- -#}
    {%- if item.USAGERPTMODE == 'ONLINE' -%}
        {%- if item.REDIRENDTOKEN is not none -%}
            REDIRENDTOKEN="{{item.REDIRENDTOKEN}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：ONLMETERINGTYPE=TIME/VOLUME_TIME/EVENT_TIME/EVENT_VOLUME_TIME 时可选 --- -#}
    {%- if item.ONLMETERINGTYPE in ['TIME', 'VOLUME_TIME', 'EVENT_TIME', 'EVENT_VOLUME_TIME'] -%}
        {%- if item.TIMERSUVALUE is not none -%}
            TIMERSUVALUE={{item.TIMERSUVALUE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：ONLMETERINGTYPE=VOLUME/VOLUME_TIME/EVENT_VOLUME/EVENT_VOLUME_TIME 时可选 --- -#}
    {%- if item.ONLMETERINGTYPE in ['VOLUME', 'VOLUME_TIME', 'EVENT_VOLUME', 'EVENT_VOLUME_TIME'] -%}
        {%- if item.VOLUMERSUVALUE is not none -%}
            VOLUMERSUVALUE={{item.VOLUMERSUVALUE}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

##### 1.1.2 配置URR组，将URR绑定到URR组上。

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

##### 1.2.2 配置Rule，将PCC策略组绑定到Rule上。

```jinja2
{%- for item in add_rule_list -%}
    ADD RULE:
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
    {#- --- 条件必选：POLICYTYPE=ULCL 时必选 --- -#}
    {%- if item.POLICYTYPE == 'ULCL' -%}
        FLOWFILTERNAME="{{item.FLOWFILTERNAME}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：POLICYTYPE=PCC/QOS 时可选 --- -#}
    {%- if item.POLICYTYPE in ['PCC', 'QOS'] -%}
        {%- if item.PROTODESCDL is not none -%}
            PROTODESCDL="{{item.PROTODESCDL}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：POLICYTYPE=PCC/QOS 时可选 --- -#}
    {%- if item.POLICYTYPE in ['PCC', 'QOS'] -%}
        {%- if item.PROTODESCUL is not none -%}
            PROTODESCUL="{{item.PROTODESCUL}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：POLICYTYPE=PCC/QOS 时可选 --- -#}
    {%- if item.POLICYTYPE in ['PCC', 'QOS'] -%}
        {%- if item.RULERANGE is not none -%}
            RULERANGE={{item.RULERANGE}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 1.3 配置User Profile，将Rule绑定到User Profile上。

##### 1.3.1 绑定该User Profile的缺省URR组，建议每个User Profile都绑定缺省费率URR组。

```jinja2
{%- for item in set_urrgrpbinding_list -%}
    SET URRGRPBINDING:
    {#- --- 必选参数 --- -#}
    USERPROFILENAME="{{item.USERPROFILENAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.DFTURRGRPNAME is not none -%}
        DFTURRGRPNAME="{{item.DFTURRGRPNAME}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

##### 1.3.2 将Rule绑定到User Profile上。

```jinja2
{%- for item in add_rulebinding_list -%}
    ADD RULEBINDING:
    {#- --- 必选参数 --- -#}
    USERPROFILENAME="{{item.USERPROFILENAME}}",
    RULENAME="{{item.RULENAME}}",
    ;
{%- endfor -%}
```

#### 1.4 **可选：**配置在线RG配额耗尽后的默认动作。

```jinja2
{%- if is_optional_online_rg_quota_exhaust_action -%}
    {%- for item in add_quotaexhaustact_list -%}
        ADD QUOTAEXHAUSTACT:
        {#- --- 必选参数 --- -#}
        CCTMPLTNAME="{{item.CCTMPLTNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 当计费事件触发SMF发起Charging Data Request[Update]更新消息申请配额，Total Volume到达后仍未收到NCG/CHF(OCS)响应消息，且SMF本地通过**SET FAILHANDLING**命令配置的TXTIMER超时时长未到达时，RG配额耗尽后的默认动作根据“ACTION”参数配置生效。

##### 1.4.1 当参数配置为“BLOCK”时，SMF在N4接口下发的该业务的URR绑定的FAR动作为drop，即在线RG配额耗尽后阻塞业务，使业务不能继续进行。

##### 1.4.2 当参数配置为“REDIRECT”时，SMF在N4接口下发的该业务的URR绑定的FAR动作为Redirect Information，即在线RG配额耗尽后将当前业务重定向到指定的地址。

##### 1.4.3 当参数配置为“FORWARD”时，SMF在N4接口下发的该业务的URR绑定的FAR动作为FORW，即在线RG配额耗尽后允许继续转发业务。


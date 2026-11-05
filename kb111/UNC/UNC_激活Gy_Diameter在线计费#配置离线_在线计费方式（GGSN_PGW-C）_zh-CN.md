---
id: ''
name: 配置离线/在线计费方式（GGSN/PGW-C）
ne_type: UNC
type: feature
description: 用户进行在线/离线计费的方式可以通过其他对接网元下发，也可以在GGSN/PGW-C本地配置，本文描述在GGSN/PGW-C上如何配置在线/离线计费的开关。  * GGSN/PGW-C的离线计费方式选择有PCRF下发、本地配置，本地配置有三种粒度：UserProfile、APN和计费属性CC，这些方式的优先级依次降低。如图1所示为GGSN/PGW-C的离线计费方式选择图。    **图1** 离线计费方式选择图 * GGSN/PGW-C的在线计费方式选择有PCRF下发、RADIUS Server下发、本地配置，本地配置有三种粒度：UserProfile、APN和计费属性CC，如图2所示为GGSN/PGW-C的在线计费方式选择图。    **图2** 在线计费方式选择图    + 如果网络中部署了PCRF控制在线计费方式，则PCRF在CCA-I消息中携带Online AVP指示IP-CAN会话是否使能在线计费。   + 如果网络中未部署PCRF，且RADIUS Server支持下发OCS-ID，则RADIUS Server在鉴权响应消息Access-Accept消息中携带OCS-ID，且该OCS在GGSN/PGW-C本地已配置，则使能在线计费。   + 如果网络中未部署PCRF，且RADIUS Server不支持下发OCS-ID，则使用本地配置的在线计费方式。  其中，根据用户归属属性配置的开关**SET CHARGECTRL**是控制在线/离线计费的总开关，是进行相应方式计费的前提和基础，它控制GGSN/PGW-C本地配置的计费开关和RADIUS server下发的计费方式是否有效，PCRF下发计费方式不受此控制。即当总开关使能了在线/离线计费，其他开关的配置才能生效。默认情况下，总开关同时使能在线/离线计费。  基于此，在线/离线计费选择开关的优先级从高到低依次是：PCRF下发的参数–〉GGSN/PGW-C本地总开关–〉RADIUS下发的参数–〉UserProfile下的配置–〉APN下的配置-〉用户计费属性下的配置。对于GGSN/PGW-C本地配置的各级开关来说，如果高级别的参数没有配置，则依次向下继承低一级别的参数取值。  适用于PGW-C、GGSN。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","计费管理功能","WSFD-109001 Gy/Diameter在线计费","激活Gy/Diameter在线计费","配置离线/在线计费方式（GGSN/PGW-C）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
用户进行在线/离线计费的方式可以通过其他对接网元下发，也可以在GGSN/PGW-C本地配置，本文描述在GGSN/PGW-C上如何配置在线/离线计费的开关。* GGSN/PGW-C的离线计费方式选择有PCRF下发、本地配置，本地配置有三种粒度：UserProfile、APN和计费属性CC，这些方式的优先级依次降低。如图1所示为GGSN/PGW-C的离线计费方式选择图。  **图1** 离线计费方式选择图* GGSN/PGW-C的在线计费方式选择有PCRF下发、RADIUS Server下发、本地配置，本地配置有三种粒度：UserProfile、APN和计费属性CC，如图2所示为GGSN/PGW-C的在线计费方式选择图。  **图2** 在线计费方式选择图  + 如果网络中部署了PCRF控制在线计费方式，则PCRF在CCA-I消息中携带Online AVP指示IP-CAN会话是否使能在线计费。  + 如果网络中未部署PCRF，且RADIUS Server支持下发OCS-ID，则RADIUS Server在鉴权响应消息Access-Accept消息中携带OCS-ID，且该OCS在GGSN/PGW-C本地已配置，则使能在线计费。  + 如果网络中未部署PCRF，且RADIUS Server不支持下发OCS-ID，则使用本地配置的在线计费方式。其中，根据用户归属属性配置的开关**SET CHARGECTRL**是控制在线/离线计费的总开关，是进行相应方式计费的前提和基础，它控制GGSN/PGW-C本地配置的计费开关和RADIUS server下发的计费方式是否有效，PCRF下发计费方式不受此控制。即当总开关使能了在线/离线计费，其他开关的配置才能生效。默认情况下，总开关同时使能在线/离线计费。基于此，在线/离线计费选择开关的优先级从高到低依次是：PCRF下发的参数–〉GGSN/PGW-C本地总开关–〉RADIUS下发的参数–〉UserProfile下的配置–〉APN下的配置-〉用户计费属性下的配置。对于GGSN/PGW-C本地配置的各级开关来说，如果高级别的参数没有配置，则依次向下继承低一级别的参数取值。适用于PGW-C、GGSN。

## 必备事项
前提条件

前提条件

* 请仔细阅读Ga/Gy接口离线/在线计费。
* 完成配置到CG的数据（GGSN/SGW-C/PGW-C）。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    set_chargectrl_list:
      type: items
      properties:
        HOMEOFFLINE:
          name: '归属地离线用户计费控制'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '用来控制是否基于用户漫游、拜访、本地属性来提供离线计费。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        VISITOFFLINE:
          name: '拜访地离线计费用户计费控制'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        ROAMOFFLINE:
          name: '漫游离线计费用户计费控制'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        HOMEONLINE:
          name: '归属地在线用户计费控制'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '用来控制是否基于用户漫游、拜访、本地属性来提供在线计费。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        VISITONLINE:
          name: '拜访地在线计费用户计费控制'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        ROAMONLINE:
          name: '漫游在线计费用户计费控制'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    set_usrprofcharge_list:
      type: items
      properties:
        USRPROFNAME:
          name: '用户模板名称'
          type: string
          maxLength: 63
          required: true
          description: '配置User Profile实例的计费方式。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        OFFLINESW:
          name: '离线计费开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          - INHERIT
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        ONLINESW:
          name: '在线计费开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          - INHERIT
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_apn_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '配置APN。可通过**LST APN**命令查询已经配置的APN。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    set_apnchargectrl_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          maxLength: 63
          required: true
          description: '配置APN实例得离线计费方式。   * OFFLINESW默认值都是INHERIT。 * 在APN中配置INHERIT则计费方式继承基于计费属性的配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        OFFLINESW:
          name: '离线计费开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          - INHERIT
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        ONLINESW:
          name: '在线计费开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          - INHERIT
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_chargemethod_list:
      type: items
      properties:
        CHARGECHARACT:
          name: '计费属性'
          type: string
          enum:
          - DEFAULT
          - FLAT_BILLING
          - HOT_BILLING
          - NORMAL
          - PREPAID
          - SPECIFIC_VALUE
          required: true
          description: '基于用户计费属性配置离线计费。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        CCVALUE:
          name: '计费属性值'
          type: string
          maxLength: 6
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        MASK:
          name: '计费属性掩码'
          type: string
          maxLength: 6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PRIORITY:
          name: '计费属性优先级'
          type: integer
          minimum: 1
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        OFFLINE:
          name: '离线计费开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ENABLE
        ONLINE:
          name: '在线计费开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: DISABLE
    add_urr_list:
      type: items
      properties:
        URRNAME:
          name: '使用量上报规则名称'
          type: string
          maxLength: 31
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        URRID:
          name: 'URR标识'
          type: integer
          minimum: 0
          maximum: 2147483646
          required: true
          description: ''
          data_source: ''
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
        OFFCOMPOUNDTYPE:
          name: '离线计费标识组成类型'
          type: string
          enum:
          - ONLYRG
          - ONLYSID
          - RGSID
          - UPDOWNSID
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
          default: ''
        ONLCOMPOUNDTYPE:
          name: '在线计费标识组成类型'
          type: string
          enum:
          - ONLYRG
          - RGSID
          required: false
          description: ''
          data_source: ''
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
    add_userprofile_list:
      type: items
      properties:
        USERPROFILENAME:
          name: '用户模板名称'
          type: string
          maxLength: 63
          required: true
          description: '配置UserProflie。'
          data_source: '全网规划'
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
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: PCC
        PROFILERANGE:
          name: '模板生效范围'
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
  examples:
    set_chargectrl_list:
    - HOMEOFFLINE: ENABLE
      VISITOFFLINE: ENABLE
      ROAMOFFLINE: ENABLE
      HOMEONLINE: ENABLE
      VISITONLINE: ENABLE
      ROAMONLINE: ENABLE
    set_usrprofcharge_list:
    - USRPROFNAME: 'up-test'
      OFFLINESW: ENABLE
      ONLINESW: ENABLE
    add_apn_list:
    - APN: 'apn-test'
    set_apnchargectrl_list:
    - APN: 'apn-test'
      OFFLINESW: ENABLE
      ONLINESW: ENABLE
    add_chargemethod_list:
    - CHARGECHARACT: SPECIFIC_VALUE
      CCVALUE: '0x0400'
      MASK: '0x0400'
      PRIORITY: 2
      OFFLINE: ENABLE
      ONLINE: ENABLE
    add_urr_list:
    - URRNAME: ''
      URRID: ''
      USAGERPTMODE: ''
      MONITORINGKEY: ''
      N40AGESW: ENABLE
      OFCSRVTMPLNAME: ''
      OFFCOMPOUNDTYPE: ''
      OFFMETERINGTYPE: ''
      ONLCOMPOUNDTYPE: ''
      ONLMETERINGTYPE: ''
      REDIRENDTOKEN: ''
    add_userprofile_list:
    - USERPROFILENAME: 'up-test'
      UPTYPE: PCC
      PROFILERANGE: ALL
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 基于用户归属属性（本地用户、漫游用户、拜访用户）使能GGSN/PGW-C的离线/在线计费方式。

```jinja2
{%- for item in set_chargectrl_list -%}
    SET CHARGECTRL:
    {#- --- 可选参数 --- -#}
    {%- if item.HOMEOFFLINE is not none -%}
        HOMEOFFLINE={{item.HOMEOFFLINE}},
    {%- endif -%}
    {%- if item.VISITOFFLINE is not none -%}
        VISITOFFLINE={{item.VISITOFFLINE}},
    {%- endif -%}
    {%- if item.ROAMOFFLINE is not none -%}
        ROAMOFFLINE={{item.ROAMOFFLINE}},
    {%- endif -%}
    {%- if item.HOMEONLINE is not none -%}
        HOMEONLINE={{item.HOMEONLINE}},
    {%- endif -%}
    {%- if item.VISITONLINE is not none -%}
        VISITONLINE={{item.VISITONLINE}},
    {%- endif -%}
    {%- if item.ROAMONLINE is not none -%}
        ROAMONLINE={{item.ROAMONLINE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 针对同一个用户，不同属性下规划的计费方式要一致，否则用户计费会出错。例如，针对CC取值为NORMAL的本地用户，如果设置NORMAL用户进行离线计费，又设置本地用户进行在线计费，则最终用户计费将出错。

### 2 基于UserProfile配置计费方式。

```jinja2
{%- for item in set_usrprofcharge_list -%}
    SET USRPROFCHARGE:
    {#- --- 必选参数 --- -#}
    USRPROFNAME="{{item.USRPROFNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.OFFLINESW is not none -%}
        OFFLINESW={{item.OFFLINESW}},
    {%- endif -%}
    {%- if item.ONLINESW is not none -%}
        ONLINESW={{item.ONLINESW}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 基于APN使能GGSN/PGW-C的离线/在线计费方式。

```jinja2
{%- for item in add_apn_list -%}
    ADD APN:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    ;
{%- endfor -%}
```

```jinja2
{%- for item in set_apnchargectrl_list -%}
    SET APNCHARGECTRL:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    {#- --- 可选参数 --- -#}
    {%- if item.OFFLINESW is not none -%}
        OFFLINESW={{item.OFFLINESW}},
    {%- endif -%}
    {%- if item.ONLINESW is not none -%}
        ONLINESW={{item.ONLINESW}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 基于用户计费属性使能GGSN/PGW-C的离线/在线计费方式。

```jinja2
{%- for item in add_chargemethod_list -%}
    ADD CHARGEMETHOD:
    {#- --- 必选参数 --- -#}
    CHARGECHARACT={{item.CHARGECHARACT}},
    {#- --- 可选参数 --- -#}
    {%- if item.OFFLINE is not none -%}
        OFFLINE={{item.OFFLINE}},
    {%- endif -%}
    {%- if item.ONLINE is not none -%}
        ONLINE={{item.ONLINE}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：CHARGECHARACT=SPECIFIC_VALUE 时必选 --- -#}
    {%- if item.CHARGECHARACT == 'SPECIFIC_VALUE' -%}
        CCVALUE="{{item.CCVALUE}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：CHARGECHARACT=SPECIFIC_VALUE 时可选 --- -#}
    {%- if item.CHARGECHARACT == 'SPECIFIC_VALUE' -%}
        {%- if item.MASK is not none -%}
            MASK="{{item.MASK}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：CHARGECHARACT=SPECIFIC_VALUE 时可选 --- -#}
    {%- if item.CHARGECHARACT == 'SPECIFIC_VALUE' -%}
        {%- if item.PRIORITY is not none -%}
            PRIORITY={{item.PRIORITY}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 5 配置免费业务的计费方式。

#### 5.1 配置免费业务的计费模式。

```jinja2
{%- for item in add_urr_list -%}
    ADD URR:
    {#- --- 必选参数 --- -#}
    URRID={{item.URRID}},
    URRNAME="{{item.URRNAME}}",
    USAGERPTMODE={{item.USAGERPTMODE}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：USAGERPTMODE=MONITORINGKEY 时必选 --- -#}
    {%- if item.USAGERPTMODE == 'MONITORINGKEY' -%}
        MONITORINGKEY="{{item.MONITORINGKEY}}",
    {%- endif -%}
    {#- --- 条件必选：USAGERPTMODE=OFFLINE 时必选 --- -#}
    {%- if item.USAGERPTMODE == 'OFFLINE' -%}
        OFFCOMPOUNDTYPE={{item.OFFCOMPOUNDTYPE}},
    {%- endif -%}
    {#- --- 条件必选：USAGERPTMODE=ONLINE 时必选 --- -#}
    {%- if item.USAGERPTMODE == 'ONLINE' -%}
        ONLCOMPOUNDTYPE={{item.ONLCOMPOUNDTYPE}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
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
    {#- --- 条件可选：USAGERPTMODE=ONLINE 时可选 --- -#}
    {%- if item.USAGERPTMODE == 'ONLINE' -%}
        {%- if item.REDIRENDTOKEN is not none -%}
            REDIRENDTOKEN="{{item.REDIRENDTOKEN}}",
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 离线计费：参数“USAGERPTMODE”设置为“OFFIINE”，“OFFMETERINGTYPE”设置为“FREE”。

#### 在线计费：参数“USAGERPTMODE”设置为“ONLINE”，“ONLMETERINGTYPE”设置为**“FREE”**。

#### 5.2 配置UserProfile免费业务的计费方式。

```jinja2
{%- for item in add_userprofile_list -%}
    ADD USERPROFILE:
    {#- --- 必选参数 --- -#}
    USERPROFILENAME="{{item.USERPROFILENAME}}",
    UPTYPE={{item.UPTYPE}},
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：UPTYPE=PCC 时可选 --- -#}
    {%- if item.UPTYPE == 'PCC' -%}
        {%- if item.PROFILERANGE is not none -%}
            PROFILERANGE={{item.PROFILERANGE}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 对于UserProfile中计费属性的“FREESERONLCHG”或“FREESEROFFCHG”配置为“ENABLE”的业务即免费业务，如果要想在CG离线话单或在线计费配额上报消息中观察到这些业务的计费信息，则必须在其所在的UserProfile下用**ADD USERPROFILE**命令使能offline或online计费，系统缺省已经使能online和offline计费。


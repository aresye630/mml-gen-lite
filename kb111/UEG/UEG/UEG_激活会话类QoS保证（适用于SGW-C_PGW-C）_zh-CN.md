---
id: GWFD-022301
name: 激活会话类QoS保证（适用于SGW-C/PGW-C）
ne_type: UEG
type: feature
description: 当移动IP网络中部署了具有实时性特点的会话类业务时，要求移动IP网络转发时延低、抖动小，因此需要提供端到端的QoS保证。  适用于SGW-C、PGW-C。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝L","MEC 特性指南（风筝L）","GW-C&SMF特性指南","GWFD-022300 智能QoS管理增强","GWFD-022301 会话类QoS保证","激活会话类QoS保证（适用于SGW-C/PGW-C）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
当移动IP网络中部署了具有实时性特点的会话类业务时，要求移动IP网络转发时延低、抖动小，因此需要提供端到端的QoS保证。适用于SGW-C、PGW-C。

## 必备事项
前提条件

* 完成配置普通APN **ADD CPAPN**。
* 完成加载License。
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
    set_cpqosglobal_list:
      type: items
      properties:
        QOSPROFILENAME:
          name: 'QoS Profile名'
          type: string
          minLength: 1
          maxLength: 63
          required: false
          description: '配置全局的QoS信息。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        BINDEPSSUBQOS:
          name: 'EPS用户QOS'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        EPSSUBQOS:
          name: 'EPS用户QOS索引'
          type: integer
          minimum: 0
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_defepsqos_list:
      type: items
      properties:
        QOSCLASSID:
          name: 'QCI值'
          type: integer
          minimum: 1
          maximum: 255
          required: false
          description: '配置EPS QoS缺省QoS参数。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        ARPVALUE:
          name: 'ARP值'
          type: integer
          minimum: 1
          maximum: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GBRDL:
          name: '下行GBR(千比特/秒)'
          type: integer
          minimum: 0
          maximum: 2000000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GBRUL:
          name: '上行保证带宽'
          type: integer
          minimum: 0
          maximum: 2000000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MBRDL:
          name: '下行最大带宽'
          type: integer
          minimum: 0
          maximum: 2000000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MBRUL:
          name: '上行最大带宽'
          type: integer
          minimum: 0
          maximum: 2000000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        APNAMBRDL:
          name: '下行APN AMBR'
          type: integer
          minimum: 0
          maximum: 2000000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        APNAMBRUL:
          name: '上行APN AMBR'
          type: integer
          minimum: 0
          maximum: 2000000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_qosprofile_list:
      type: items
      properties:
        QOSPROFILENAME:
          name: 'QoS Profile名'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '配置QosProfile的配置信息。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_epsqosaction_list:
      type: items
      properties:
        QOSPROFILENAME:
          name: 'QoS Profile名'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '配置QoS上下行保证带宽门限、最高带宽门限以及带宽超过门限值时对QoS用户的处理动作。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        QCI:
          name: 'QCI值'
          type: integer
          minimum: 1
          maximum: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GBRDL:
          name: '下行保证带宽'
          type: integer
          minimum:
          - 0
          - 4294967295
          maximum:
          - 20000000
          - 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GBRDLACTION:
          name: '超过下行GBR的处理'
          type: string
          enum:
          - DEGRADE
          - REJECT
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GBRUL:
          name: '上行保证带宽'
          type: integer
          minimum:
          - 0
          - 4294967295
          maximum:
          - 20000000
          - 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GBRULACTION:
          name: '超过上行GBR的处理'
          type: string
          enum:
          - DEGRADE
          - REJECT
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MBRDL:
          name: '下行最大带宽'
          type: integer
          minimum:
          - 0
          - 4294967295
          maximum:
          - 20000000
          - 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MBRDLACTION:
          name: '超过下行MBR的处理'
          type: string
          enum:
          - DEGRADE
          - REJECT
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MBRUL:
          name: '上行最大带宽'
          type: integer
          minimum:
          - 0
          - 4294967295
          maximum:
          - 20000000
          - 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MBRULACTION:
          name: '超过上行MBR的处理'
          type: string
          enum:
          - DEGRADE
          - REJECT
          required: false
          description: ''
          data_source: ''
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
          description: '指定APN实例。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_cpapnqosattr_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '为APN实例绑定QosProfile。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        HASQOSPROFILE:
          name: '是否配置QosProfile'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        QOSPROFILENAME:
          name: 'QoS Profile名'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_qosremark_list:
      type: items
      properties:
        DOWNLINK:
          name: '下行标记'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '整机上下行QosRemark功能开关。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        UPLINK:
          name: '上行标记'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_qosprofile_list_1:
      type: items
      properties:
        QOSPROFILENAME:
          name: 'QoS Profile名'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '配置QosProfile的配置信息。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_epsremark_list:
      type: items
      properties:
        QOSPROFILENAME:
          name: 'QoS Profile名'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '配置EPS QoS到DSCP或者TOS的映射规则。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        QCI:
          name: 'QCI值'
          type: integer
          minimum: 1
          maximum: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ARPPL:
          name: 'ARP的优先级别'
          type: integer
          minimum: 0
          maximum: 15
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        REMARKTYPE:
          name: '标记类型'
          type: string
          enum:
          - DSCP
          - TOS
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DSCP:
          name: 'DSCP'
          type: string
          enum:
          - EF
          - AF
          - BE
          - CS6
          - CS7
          - DSCP_VALUE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        S1UDSCPSWITCH:
          name: 'S1-U DSCP配置开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
        S1UDSCP:
          name: 'S1-U DSCP'
          type: string
          enum:
          - EF
          - AF
          - BE
          - CS6
          - CS7
          - DSCP_VALUE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        S1UDSCPVALUE:
          name: 'S1-U DSCP值'
          type: integer
          minimum: 0
          maximum: 63
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        S5SDSCPSWITCH:
          name: 'SGW S5 DSCP配置开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
        S5SDSCP:
          name: 'SGW S5 DSCP'
          type: string
          enum:
          - EF
          - AF
          - BE
          - CS6
          - CS7
          - DSCP_VALUE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        S5SDSCPVALUE:
          name: 'SGW S5 DSCP值'
          type: integer
          minimum: 0
          maximum: 63
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        S5PDSCPSWITCH:
          name: 'PGW S5 DSCP配置开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
        S5PDSCP:
          name: 'PGW S5 DSCP'
          type: string
          enum:
          - EF
          - AF
          - BE
          - CS6
          - CS7
          - DSCP_VALUE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        S5PDSCPVALUE:
          name: 'PGW S5 DSCP值'
          type: integer
          minimum: 0
          maximum: 63
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        S8SDSCPSWITCH:
          name: 'SGW S8 DSCP配置开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
        S8SDSCP:
          name: 'SGW S8 DSCP'
          type: string
          enum:
          - EF
          - AF
          - BE
          - CS6
          - CS7
          - DSCP_VALUE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        S8SDSCPVALUE:
          name: 'SGW S8 DSCP值'
          type: integer
          minimum: 0
          maximum: 63
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        S8PDSCPSWITCH:
          name: 'PGW S8 DSCP配置开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
        S8PDSCP:
          name: 'PGW S8 DSCP'
          type: string
          enum:
          - EF
          - AF
          - BE
          - CS6
          - CS7
          - DSCP_VALUE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        S8PDSCPVALUE:
          name: 'PGW S8 DSCP值'
          type: integer
          minimum: 0
          maximum: 63
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SGIDSCPSWITCH:
          name: 'PGW SGi DSCP配置开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
        SGIDSCP:
          name: 'PGW SGi DSCP'
          type: string
          enum:
          - EF
          - AF
          - BE
          - CS6
          - CS7
          - DSCP_VALUE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SGIDSCPVALUE:
          name: 'PGW SGi DSCP值'
          type: integer
          minimum: 0
          maximum: 63
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_ifdscp_list:
      type: items
      properties:
        MSGCLS:
          name: '消息类别'
          type: string
          enum:
          - DATA
          - SIGNALLING
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        INTFTP_SHOW:
          name: '接口类型'
          type: string
          enum:
          - DEFAULT
          - DNS
          - Diameter_PROTOCOL
          - GTP_PROTOCOL_SIGNALING
          - Ga
          - Gb_SIGNALING
          - Iu_SIGNALING
          - M3
          - M3UA_PROTOCOL
          - S102
          - S1_MME
          - SBc
          - SGs
          - SLs
          - Tm
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DSCPV:
          name: 'DSCP值'
          type: integer
          minimum: 0
          maximum: 63
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CCDSCP:
          name: '会话类数据的DSCP值'
          type: string
          enum:
          - AF11
          - AF12
          - AF13
          - AF21
          - AF22
          - AF23
          - AF31
          - AF32
          - AF33
          - AF41
          - AF42
          - AF43
          - BE
          - EF
          - NC
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DATAPOLICY:
          name: '数据DSCP使用策略'
          type: string
          enum:
          - MODIFY
          - TRANSFER
          required: false
          description: ''
          data_source: ''
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
          description: '配置用户模板组User Profile Group'
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
          description: '将UserProfile绑定到用户模板组'
          data_source: '全网规划'
          pattern: ''
          default: ''
        UPBINDTYPE:
          name: 'UPBINDTYPE'
          type: string
          enum:
          - DEFAULT
          - SPECIFIC
          - ULCL
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        USERPROFILENAME:
          name: '用户模板名称'
          type: string
          maxLength: 63
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_cpapn_list_1:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '指定APN实例。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_apnusrprofg_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          maxLength: 63
          required: true
          description: '将UserProfile Group绑定到APN'
          data_source: '全网规划'
          pattern: ''
          default: ''
        USERPROFGNAME:
          name: '用户模板组名称'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_cpapnqosattr_list_1:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '为APN实例绑定QosProfile。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        HASQOSPROFILE:
          name: '是否配置QosProfile'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        QOSPROFILENAME:
          name: 'QoS Profile名'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_qosctrl_list:
      type: items
      properties:
        USERTYPE:
          name: '用户漫游类型'
          type: string
          enum:
          - ROAMING
          - VISITING
          - HOME
          required: true
          description: '配置用户带宽控制的全局开关'
          data_source: '全网规划'
          pattern: ''
          default: ''
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV3W9TCQS11'
      SWITCH: ENABLE
    set_cpqosglobal_list:
    - QOSPROFILENAME: 'qos1'
      BINDEPSSUBQOS: ENABLE
      EPSSUBQOS: 1
    set_defepsqos_list:
    - QOSCLASSID: 1
      ARPVALUE: 1
      GBRDL: 200
      GBRUL: 230
      MBRDL: 300
      MBRUL: 300
      APNAMBRDL: 1000
      APNAMBRUL: 1000
    add_qosprofile_list:
    - QOSPROFILENAME: 'qos2'
    add_epsqosaction_list:
    - QOSPROFILENAME: 'qos2'
      QCI: 1
      GBRDL: 256
      GBRDLACTION: DEGRADE
      GBRUL: 128
      GBRULACTION: DEGRADE
      MBRDL: 384
      MBRDLACTION: DEGRADE
      MBRUL: 192
      MBRULACTION: DEGRADE
    add_cpapn_list:
    - APN: 'apn1'
    set_cpapnqosattr_list:
    - APN: 'apn1'
      HASQOSPROFILE: ENABLE
      QOSPROFILENAME: 'qos2'
    set_qosremark_list:
    - DOWNLINK: ENABLE
      UPLINK: ENABLE
    add_qosprofile_list_1:
    - QOSPROFILENAME: 'gp1'
    add_epsremark_list:
    - QOSPROFILENAME: 'qosprofile1'
      QCI: 1
      ARPPL: 1
      REMARKTYPE: DSCP
      DSCP: EF
      S1UDSCPSWITCH: ENABLE
      S1UDSCP: DSCP_VALUE
      S1UDSCPVALUE: 22
      S5SDSCPSWITCH: ENABLE
      S5SDSCP: DSCP_VALUE
      S5SDSCPVALUE: 23
      S5PDSCPSWITCH: ENABLE
      S5PDSCP: DSCP_VALUE
      S5PDSCPVALUE: 24
      S8SDSCPSWITCH: ENABLE
      S8SDSCP: DSCP_VALUE
      S8SDSCPVALUE: 25
      S8PDSCPSWITCH: ENABLE
      S8PDSCP: DSCP_VALUE
      S8PDSCPVALUE: 26
      SGIDSCPSWITCH: ENABLE
      SGIDSCP: DSCP_VALUE
      SGIDSCPVALUE: 27
    set_ifdscp_list:
    - MSGCLS: SIGNALLING
      INTFTP_SHOW: GTP_PROTOCOL_SIGNALING
      DSCPV: 63
      CCDSCP: EF
      DATAPOLICY: ''
    add_usrprofgroup_list:
    - USERPROFGNAME: 'usrg'
    add_upbindupg_list:
    - USERPROFGNAME: 'usrg'
      UPBINDTYPE: DEFAULT
      USERPROFILENAME: 'profile1'
    add_cpapn_list_1:
    - APN: 'apn1'
    add_apnusrprofg_list:
    - APN: 'apn1'
      USERPROFGNAME: 'usrg'
    set_cpapnqosattr_list_1:
    - APN: 'apn1'
      HASQOSPROFILE: ENABLE
      QOSPROFILENAME: 'gp1'
    set_qosctrl_list:
    - USERTYPE: VISITING
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 进入“MML命令行-UEG”窗口。

### 2 打开License配置开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

### 3 设置全局的QoS信息。

```jinja2
{%- for item in set_cpqosglobal_list -%}
    SET CPQOSGLOBAL:
    {#- --- 可选参数 --- -#}
    {%- if item.QOSPROFILENAME is not none -%}
        QOSPROFILENAME="{{item.QOSPROFILENAME}}",
    {%- endif -%}
    {%- if item.BINDEPSSUBQOS is not none -%}
        BINDEPSSUBQOS={{item.BINDEPSSUBQOS}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：BINDEPSSUBQOS=ENABLE 时必选 --- -#}
    {%- if item.BINDEPSSUBQOS == 'ENABLE' -%}
        EPSSUBQOS={{item.EPSSUBQOS}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 配置EPS QoS缺省QoS参数。

```jinja2
{%- for item in set_defepsqos_list -%}
    SET DEFEPSQOS:
    {#- --- 可选参数 --- -#}
    {%- if item.QOSCLASSID is not none -%}
        QOSCLASSID={{item.QOSCLASSID}},
    {%- endif -%}
    {%- if item.ARPVALUE is not none -%}
        ARPVALUE={{item.ARPVALUE}},
    {%- endif -%}
    {%- if item.GBRDL is not none -%}
        GBRDL={{item.GBRDL}},
    {%- endif -%}
    {%- if item.GBRUL is not none -%}
        GBRUL={{item.GBRUL}},
    {%- endif -%}
    {%- if item.MBRDL is not none -%}
        MBRDL={{item.MBRDL}},
    {%- endif -%}
    {%- if item.MBRUL is not none -%}
        MBRUL={{item.MBRUL}},
    {%- endif -%}
    {%- if item.APNAMBRDL is not none -%}
        APNAMBRDL={{item.APNAMBRDL}},
    {%- endif -%}
    {%- if item.APNAMBRUL is not none -%}
        APNAMBRUL={{item.APNAMBRUL}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 5 配置EPS QoS协商控制。

#### 5.1 进入“MML命令行-UEG”窗口。

#### 5.2 配置指定APN实例下的QosProfile名称（非全局），并进入QoS实例。

```jinja2
{%- for item in add_qosprofile_list -%}
    ADD QOSPROFILE:
    {#- --- 必选参数 --- -#}
    QOSPROFILENAME="{{item.QOSPROFILENAME}}",
    ;
{%- endfor -%}
```

#### 5.3 配置会话类QoS上下行最高带宽门限、会话类QoS上下行保证带宽门限以及带宽超过门限值时对此类QoS用户的处理动作。

```jinja2
{%- for item in add_epsqosaction_list -%}
    ADD EPSQOSACTION:
    {#- --- 必选参数 --- -#}
    QOSPROFILENAME="{{item.QOSPROFILENAME}}",
    QCI={{item.QCI}},
    {#- --- 可选参数 --- -#}
    {%- if item.GBRDL is not none -%}
        GBRDL={{item.GBRDL}},
    {%- endif -%}
    {%- if item.GBRDLACTION is not none -%}
        GBRDLACTION={{item.GBRDLACTION}},
    {%- endif -%}
    {%- if item.GBRUL is not none -%}
        GBRUL={{item.GBRUL}},
    {%- endif -%}
    {%- if item.GBRULACTION is not none -%}
        GBRULACTION={{item.GBRULACTION}},
    {%- endif -%}
    {%- if item.MBRDL is not none -%}
        MBRDL={{item.MBRDL}},
    {%- endif -%}
    {%- if item.MBRDLACTION is not none -%}
        MBRDLACTION={{item.MBRDLACTION}},
    {%- endif -%}
    {%- if item.MBRUL is not none -%}
        MBRUL={{item.MBRUL}},
    {%- endif -%}
    {%- if item.MBRULACTION is not none -%}
        MBRULACTION={{item.MBRULACTION}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 5.4 配置APN实例。

```jinja2
{%- for item in add_cpapn_list -%}
    ADD CPAPN:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    ;
{%- endfor -%}
```

#### 5.5 为APN实例绑定QoS profile。

```jinja2
{%- for item in set_cpapnqosattr_list -%}
    SET CPAPNQOSATTR:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    {#- --- 可选参数 --- -#}
    {%- if item.HASQOSPROFILE is not none -%}
        HASQOSPROFILE={{item.HASQOSPROFILE}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：HASQOSPROFILE=ENABLE 时必选 --- -#}
    {%- if item.HASQOSPROFILE == 'ENABLE' -%}
        QOSPROFILENAME="{{item.QOSPROFILENAME}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 6 配置EPS QoS到DSCP的映射关系。

#### 6.1 配置用户的上下行remark功能开关

```jinja2
{%- for item in set_qosremark_list -%}
    SET QOSREMARK:
    {#- --- 可选参数 --- -#}
    {%- if item.DOWNLINK is not none -%}
        DOWNLINK={{item.DOWNLINK}},
    {%- endif -%}
    {%- if item.UPLINK is not none -%}
        UPLINK={{item.UPLINK}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 6.2 配置指定APN实例下的QosProfile名称（非全局），并进入QoS实例。

```jinja2
{%- for item in add_qosprofile_list_1 -%}
    ADD QOSPROFILE:
    {#- --- 必选参数 --- -#}
    QOSPROFILENAME="{{item.QOSPROFILENAME}}",
    ;
{%- endfor -%}
```

#### 6.3 配置EPS QoS到DSCP的映射规则。

```jinja2
{%- for item in add_epsremark_list -%}
    ADD EPSREMARK:
    {#- --- 必选参数 --- -#}
    QOSPROFILENAME="{{item.QOSPROFILENAME}}",
    QCI={{item.QCI}},
    ARPPL={{item.ARPPL}},
    REMARKTYPE={{item.REMARKTYPE}},
    {#- --- 可选参数 --- -#}
    {%- if item.S1UDSCPSWITCH is not none -%}
        S1UDSCPSWITCH={{item.S1UDSCPSWITCH}},
    {%- endif -%}
    {%- if item.S5SDSCPSWITCH is not none -%}
        S5SDSCPSWITCH={{item.S5SDSCPSWITCH}},
    {%- endif -%}
    {%- if item.S5PDSCPSWITCH is not none -%}
        S5PDSCPSWITCH={{item.S5PDSCPSWITCH}},
    {%- endif -%}
    {%- if item.S8SDSCPSWITCH is not none -%}
        S8SDSCPSWITCH={{item.S8SDSCPSWITCH}},
    {%- endif -%}
    {%- if item.S8PDSCPSWITCH is not none -%}
        S8PDSCPSWITCH={{item.S8PDSCPSWITCH}},
    {%- endif -%}
    {%- if item.SGIDSCPSWITCH is not none -%}
        SGIDSCPSWITCH={{item.SGIDSCPSWITCH}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：REMARKTYPE=DSCP 时必选 --- -#}
    {%- if item.REMARKTYPE == 'DSCP' -%}
        DSCP={{item.DSCP}},
    {%- endif -%}
    {#- --- 条件必选：S1UDSCPSWITCH=ENABLE 时必选 --- -#}
    {%- if item.S1UDSCPSWITCH == 'ENABLE' -%}
        S1UDSCP={{item.S1UDSCP}},
    {%- endif -%}
    {#- --- 条件必选：S1UDSCP=DSCP_VALUE 时必选 --- -#}
    {%- if item.S1UDSCP == 'DSCP_VALUE' -%}
        S1UDSCPVALUE={{item.S1UDSCPVALUE}},
    {%- endif -%}
    {#- --- 条件必选：S5SDSCPSWITCH=ENABLE 时必选 --- -#}
    {%- if item.S5SDSCPSWITCH == 'ENABLE' -%}
        S5SDSCP={{item.S5SDSCP}},
    {%- endif -%}
    {#- --- 条件必选：S5SDSCP=DSCP_VALUE 时必选 --- -#}
    {%- if item.S5SDSCP == 'DSCP_VALUE' -%}
        S5SDSCPVALUE={{item.S5SDSCPVALUE}},
    {%- endif -%}
    {#- --- 条件必选：S5PDSCPSWITCH=ENABLE 时必选 --- -#}
    {%- if item.S5PDSCPSWITCH == 'ENABLE' -%}
        S5PDSCP={{item.S5PDSCP}},
    {%- endif -%}
    {#- --- 条件必选：S5PDSCP=DSCP_VALUE 时必选 --- -#}
    {%- if item.S5PDSCP == 'DSCP_VALUE' -%}
        S5PDSCPVALUE={{item.S5PDSCPVALUE}},
    {%- endif -%}
    {#- --- 条件必选：S8SDSCPSWITCH=ENABLE 时必选 --- -#}
    {%- if item.S8SDSCPSWITCH == 'ENABLE' -%}
        S8SDSCP={{item.S8SDSCP}},
    {%- endif -%}
    {#- --- 条件必选：S8SDSCP=DSCP_VALUE 时必选 --- -#}
    {%- if item.S8SDSCP == 'DSCP_VALUE' -%}
        S8SDSCPVALUE={{item.S8SDSCPVALUE}},
    {%- endif -%}
    {#- --- 条件必选：S8PDSCPSWITCH=ENABLE 时必选 --- -#}
    {%- if item.S8PDSCPSWITCH == 'ENABLE' -%}
        S8PDSCP={{item.S8PDSCP}},
    {%- endif -%}
    {#- --- 条件必选：S8PDSCP=DSCP_VALUE 时必选 --- -#}
    {%- if item.S8PDSCP == 'DSCP_VALUE' -%}
        S8PDSCPVALUE={{item.S8PDSCPVALUE}},
    {%- endif -%}
    {#- --- 条件必选：SGIDSCPSWITCH=ENABLE 时必选 --- -#}
    {%- if item.SGIDSCPSWITCH == 'ENABLE' -%}
        SGIDSCP={{item.SGIDSCP}},
    {%- endif -%}
    {#- --- 条件必选：SGIDSCP=DSCP_VALUE 时必选 --- -#}
    {%- if item.SGIDSCP == 'DSCP_VALUE' -%}
        SGIDSCPVALUE={{item.SGIDSCPVALUE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in set_ifdscp_list -%}
    SET IFDSCP:
    {#- --- 可选参数 --- -#}
    {%- if item.MSGCLS is not none -%}
        MSGCLS={{item.MSGCLS}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：MSGCLS=SIGNALLING 时必选 --- -#}
    {%- if item.MSGCLS == 'SIGNALLING' -%}
        INTFTP_SHOW={{item.INTFTP_SHOW}},
    {%- endif -%}
    {#- --- 条件必选：MSGCLS=SIGNALLING 时必选 --- -#}
    {%- if item.MSGCLS == 'SIGNALLING' -%}
        DSCPV={{item.DSCPV}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：DATAPOLICY=MODIFY 时可选 --- -#}
    {%- if item.DATAPOLICY == 'MODIFY' -%}
        {%- if item.CCDSCP is not none -%}
            CCDSCP={{item.CCDSCP}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 6.4 配置用户模板组User Profile Group。

```jinja2
{%- for item in add_usrprofgroup_list -%}
    ADD USRPROFGROUP:
    {#- --- 必选参数 --- -#}
    USERPROFGNAME="{{item.USERPROFGNAME}}",
    ;
{%- endfor -%}
```

#### 6.5 将UserProfile绑定到用户模板组UserProfileGroup。

```jinja2
{%- for item in add_upbindupg_list -%}
    ADD UPBINDUPG:
    {#- --- 必选参数 --- -#}
    USERPROFGNAME="{{item.USERPROFGNAME}}",
    UPBINDTYPE={{item.UPBINDTYPE}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：UPBINDTYPE=SPECIFIC/DEFAULT/ULCL 时必选 --- -#}
    {%- if item.UPBINDTYPE in ['SPECIFIC', 'DEFAULT', 'ULCL'] -%}
        USERPROFILENAME="{{item.USERPROFILENAME}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 6.6 配置APN实例。

```jinja2
{%- for item in add_cpapn_list_1 -%}
    ADD CPAPN:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    ;
{%- endfor -%}
```

#### 6.7 将UserProfile Group绑定到APN。

```jinja2
{%- for item in add_apnusrprofg_list -%}
    ADD APNUSRPROFG:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    USERPROFGNAME="{{item.USERPROFGNAME}}",
    ;
{%- endfor -%}
```

#### 6.8 为APN实例绑定QoS profile。

```jinja2
{%- for item in set_cpapnqosattr_list_1 -%}
    SET CPAPNQOSATTR:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    {#- --- 可选参数 --- -#}
    {%- if item.HASQOSPROFILE is not none -%}
        HASQOSPROFILE={{item.HASQOSPROFILE}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：HASQOSPROFILE=ENABLE 时必选 --- -#}
    {%- if item.HASQOSPROFILE == 'ENABLE' -%}
        QOSPROFILENAME="{{item.QOSPROFILENAME}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 7 配置QoS带宽控制。

```jinja2
{%- for item in set_qosctrl_list -%}
    SET QOSCTRL:
    {#- --- 必选参数 --- -#}
    USERTYPE={{item.USERTYPE}},
    ;
{%- endfor -%}
```


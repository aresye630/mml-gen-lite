---
id: ''
name: 激活LTE一键通（适用于PGW-C/SGW-C）
ne_type: UNC
type: feature
description: 本操作指导介绍在运行网络中激活LTE一键通特性的操作过程。  适用于SGW-C、PGW-C。  **图1** 操作过程
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","语音功能","WSFD-102600 Push to Talk（适用于PGW-C/SGW-C）","WSFD-102602 LTE一键通（适用于PGW-C/SGW-C）","激活LTE一键通（适用于PGW-C/SGW-C）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本操作指导介绍在运行网络中激活LTE一键通特性的操作过程。适用于SGW-C、PGW-C。**图1** 操作过程

## 必备事项
前提条件

* 请仔细阅读WSFD-102601 LTE一键通基础功能（适用于PGW-C/SGW-C）和WSFD-102602 LTE一键通特性概述（适用于PGW-C/SGW-C）。

* 已完成加载License。
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
    set_pttfunc_list:
      type: items
      properties:
        LTEPTTSWITCH:
          name: 'LTE一键通功能开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '基于全局的PTT业务配置开关。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_epsqci2prer8_list:
      type: items
      properties:
        QCI:
          name: 'QCI值'
          type: integer
          minimum: 1
          maximum: 255
          required: true
          description: 'PTT QCI到Pre-R8 QoS参数traffic class的映射关系。  说明：  用户通过GnGp SGSN接入UNC，由于GnGp SGSN和UNC之间交互的是GTPv0和GTPv1信令，故UNC需将R8 QoS中的QCI信息映射至Pre Rel-8 QoS参数，保证系统正常运行。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        TRAFFICCLASS:
          name: '业务类型'
          type: string
          enum:
          - CONVERSATIONAL
          - STREAMING
          - INTERACTIVE
          - BACKGROUND
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        THP:
          name: '通信处理优先级'
          type: string
          enum:
          - NA
          - HIGH
          - NORMAL
          - LOW
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SIGNALIND:
          name: '信令传输优化'
          type: string
          enum:
          - DONT_OPTIMIZE
          - OPTIMIZE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SRCSTATDESC:
          name: '源统计描述'
          type: string
          enum:
          - UNKNOWN
          - SPEECH
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_qci2arp_list:
      type: items
      properties:
        QCI:
          name: '标准QCI'
          type: integer
          minimum:
          - 1
          - 65
          - 69
          maximum:
          - 9
          - 66
          - 70
          required: true
          description: 'PTT QCI和ARP之间的映射关系，从而通过标准QCI来映射出相应的承载ARP取值。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        ARPPL:
          name: 'ARP的优先级别'
          type: integer
          minimum: 1
          maximum: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ARPPVI:
          name: 'QCI的被抢占能力'
          type: integer
          minimum: 0
          maximum: 1
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_epsremark_list:
      type: items
      properties:
        QOSPROFILENAME:
          name: 'QoS Profile名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '增加EPS QoS到TOS/DSCP的映射规则。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        QCI:
          name: 'QCI'
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
        AFCLASS:
          name: 'AF级别'
          type: integer
          minimum: 1
          maximum: 4
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AFDROPPREC:
          name: 'AF丢弃优先级'
          type: integer
          minimum: 1
          maximum: 3
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DSCPVALUE:
          name: 'DSCP值'
          type: integer
          minimum: 0
          maximum: 63
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TOSVALUE:
          name: 'TOS值'
          type: integer
          minimum: 0
          maximum: 7
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
          description: '配置EPS本地QoS策略下缺省QoS参数，PGW-C根据协议检查用户携带的QoS参数的合法性，如果参数非法，则根据该命令配置的缺省QoS参数进行纠错和替换。'
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
          name: '下行保证带宽'
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
    add_epssubqos_list:
      type: items
      properties:
        SUBQOSINDEX:
          name: '用户QOS索引'
          type: integer
          minimum: 0
          maximum: 255
          required: true
          description: '配置用户的签约QoS属性支持PTT QCI。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        QCI:
          name: 'QCI'
          type: integer
          minimum:
          - 5
          - 69
          maximum:
          - 9
          - 70
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ARPPL:
          name: 'ARP的优先级别'
          type: integer
          minimum: 1
          maximum: 15
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AMBRDL:
          name: '下行APN AMBRR'
          type: integer
          minimum: 1
          maximum: 2000000
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AMBRUL:
          name: '上行APN AMBRR'
          type: integer
          minimum: 1
          maximum: 2000000
          required: true
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
          description: 'QosProfile的配置信息。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        BINDEPSSUBQOS:
          name: '绑定EPS用户QoS'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
        EPSSUBQOS:
          name: 'EPS用户QoS索引'
          type: integer
          minimum: 0
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_qosprop_list:
      type: items
      properties:
        QOSPROPNAME:
          name: 'QoS属性名称'
          type: string
          maxLength: 31
          required: true
          description: '配置PCC预定义规则的QoS参数。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        QCIVALUE:
          name: 'QoS等级标识'
          type: integer
          minimum: 1
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        QOSTYPE:
          name: 'QoS属性类型'
          type: string
          enum:
          - QOS_BEARER_PARA
          - QOS_FLOW_PARA
          - QOS_L2_PARA
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        EMPCAP:
          name: 'QoS抢占能力'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
        ARPVALUE:
          name: '分配保留优先级'
          type: integer
          minimum: 1
          maximum: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        FQI:
          name: '5G QoS标识'
          type: integer
          minimum: 1
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        QOSURRNAME:
          name: 'QoS使用量上报规则名称'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RQI:
          name: '反射QoS指示'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
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
          minLength: 1
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_apnpttfunc_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '基于APN的PTT业务配置开关。  APN名称必须已经通过命令**ADD APN**配置。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        LTEPTTSWITCH:
          name: 'LTE一键通功能开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
    add_epssubqos_list_1:
      type: items
      properties:
        SUBQOSINDEX:
          name: '用户QOS索引'
          type: integer
          minimum: 0
          maximum: 255
          required: true
          description: '配置用户的签约QoS属性支持PTT QCI。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        QCI:
          name: 'QCI'
          type: integer
          minimum:
          - 5
          - 69
          maximum:
          - 9
          - 70
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ARPPL:
          name: 'ARP的优先级别'
          type: integer
          minimum: 1
          maximum: 15
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AMBRDL:
          name: '下行APN AMBRR'
          type: integer
          minimum: 1
          maximum: 2000000
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AMBRUL:
          name: '上行APN AMBRR'
          type: integer
          minimum: 1
          maximum: 2000000
          required: true
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
          description: 'QosProfile的配置信息。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        BINDEPSSUBQOS:
          name: '绑定EPS用户QoS'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
        EPSSUBQOS:
          name: 'EPS用户QoS索引'
          type: integer
          minimum: 0
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_apnqosattr_list:
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
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV2QPPT02'
      SWITCH: ENABLE
    set_pttfunc_list:
    - LTEPTTSWITCH: ENABLE
    set_epsqci2prer8_list:
    - QCI: 65  66  69  70
      TRAFFICCLASS: CONVERSATIONAL
      THP: HIGH
      SIGNALIND: OPTIMIZE
      SRCSTATDESC: SPEECH
    set_qci2arp_list:
    - QCI: 65  66  69  70
      ARPPL: 7
      ARPPVI: 0
    add_epsremark_list:
    - QOSPROFILENAME: 'qos1'
      QCI: 65  66  69  70
      ARPPL: 2
      REMARKTYPE: DSCP
      DSCP: EF
      AFCLASS: ''
      AFDROPPREC: ''
      DSCPVALUE: ''
      TOSVALUE: ''
    set_defepsqos_list:
    - QOSCLASSID: 69
      ARPVALUE: 1
      GBRDL: 200bit/s
      GBRUL: 230bit/s
      MBRDL: 300bit/s
      MBRUL: 300bit/s
      APNAMBRDL: 1000bit/s
      APNAMBRUL: 1000bit/s
    add_epssubqos_list:
    - SUBQOSINDEX: 1
      QCI: 65  66  69  70
      ARPPL: 7
      AMBRDL: 22
      AMBRUL: 33
    add_qosprofile_list:
    - QOSPROFILENAME: 'qos1'
      BINDEPSSUBQOS: ENABLE（使能）
      EPSSUBQOS: 200
    add_qosprop_list:
    - QOSPROPNAME: 'qos3'
      QCIVALUE: 65  66  69  70
      QOSTYPE: QOS_BEARER_PARA
      EMPCAP: ENABLE
      ARPVALUE: ''
      FQI: ''
      QOSURRNAME: ''
      RQI: ''
    add_apn_list:
    - APN: 'apn1'
    add_apnpttfunc_list:
    - APN: 'apn1'
      LTEPTTSWITCH: ENABLE
    add_epssubqos_list_1:
    - SUBQOSINDEX: 1
      QCI: 65  66  69  70
      ARPPL: 7
      AMBRDL: 22
      AMBRUL: 33
    add_qosprofile_list_1:
    - QOSPROFILENAME: 'qos1'
      BINDEPSSUBQOS: ENABLE（使能）
      EPSSUBQOS: 200
    set_apnqosattr_list:
    - APN: 'apn1'
      HASQOSPROFILE: ENABLE
      QOSPROFILENAME: 'qos1'
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 进入“MML命令行-UNC”窗口。

### 2 打开LTE一键通功能特性的License配置开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

### 3 基于全局的一键通业务配置：

#### 3.1 查询PTT业务QCI是否已经配置为标准QCI。

#### 3.2 开启基于全局的PTT业务配置开关。

```jinja2
{%- for item in set_pttfunc_list -%}
    SET PTTFUNC:
    {#- --- 可选参数 --- -#}
    {%- if item.LTEPTTSWITCH is not none -%}
        LTEPTTSWITCH={{item.LTEPTTSWITCH}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 3.3 （可选）增加PTT业务QoS参数到Pre-R8 QoS参数映射规则。

```jinja2
{%- if is_optional_ptt_qos_prer8_mapping -%}
    {%- for item in set_epsqci2prer8_list -%}
        SET EPSQCI2PRER8:
        {#- --- 必选参数 --- -#}
        QCI={{item.QCI}},
        TRAFFICCLASS={{item.TRAFFICCLASS}},
        {#- --- 可选参数 --- -#}
        {%- if item.SIGNALIND is not none -%}
            SIGNALIND={{item.SIGNALIND}},
        {%- endif -%}
        {%- if item.SRCSTATDESC is not none -%}
            SRCSTATDESC={{item.SRCSTATDESC}},
        {%- endif -%}
        {%- if item.THP is not none -%}
            THP={{item.THP}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 3.4 （可选）配置PTT QCI和ARP的映射规则。

```jinja2
{%- if is_optional_ptt_qci_arp_mapping -%}
    {%- for item in set_qci2arp_list -%}
        SET QCI2ARP:
        {#- --- 必选参数 --- -#}
        QCI={{item.QCI}},
        {#- --- 可选参数 --- -#}
        {%- if item.ARPPL is not none -%}
            ARPPL={{item.ARPPL}},
        {%- endif -%}
        {%- if item.ARPPVI is not none -%}
            ARPPVI={{item.ARPPVI}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 3.5 （可选）配置PTT QCI到TOS/DSCP的映射规则。

```jinja2
{%- if is_optional_ptt_qci_tos_dscp_mapping -%}
    {%- for item in add_epsremark_list -%}
        ADD EPSREMARK:
        {#- --- 必选参数 --- -#}
        ARPPL={{item.ARPPL}},
        QCI={{item.QCI}},
        QOSPROFILENAME="{{item.QOSPROFILENAME}}",
        REMARKTYPE={{item.REMARKTYPE}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：DSCP=AF 时必选 --- -#}
        {%- if item.DSCP == 'AF' -%}
            AFCLASS={{item.AFCLASS}},
        {%- endif -%}
        {#- --- 条件必选：DSCP=AF 时必选 --- -#}
        {%- if item.DSCP == 'AF' -%}
            AFDROPPREC={{item.AFDROPPREC}},
        {%- endif -%}
        {#- --- 条件必选：REMARKTYPE=DSCP 时必选 --- -#}
        {%- if item.REMARKTYPE == 'DSCP' -%}
            DSCP={{item.DSCP}},
        {%- endif -%}
        {#- --- 条件必选：DSCP=DSCP_VALUE 时必选 --- -#}
        {%- if item.DSCP == 'DSCP_VALUE' -%}
            DSCPVALUE={{item.DSCPVALUE}},
        {%- endif -%}
        {#- --- 条件必选：REMARKTYPE=TOS 时必选 --- -#}
        {%- if item.REMARKTYPE == 'TOS' -%}
            TOSVALUE={{item.TOSVALUE}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 3.6 （可选）配置EPS本地QoS策略下缺省QoS参数，用于纠错。

```jinja2
{%- if is_optional_eps_default_qos -%}
    {%- for item in set_defepsqos_list -%}
        SET DEFEPSQOS:
        {#- --- 可选参数 --- -#}
        {%- if item.APNAMBRDL is not none -%}
            APNAMBRDL={{item.APNAMBRDL}},
        {%- endif -%}
        {%- if item.APNAMBRUL is not none -%}
            APNAMBRUL={{item.APNAMBRUL}},
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
        {%- if item.QOSCLASSID is not none -%}
            QOSCLASSID={{item.QOSCLASSID}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 3.7 （可选）配置用户的签约QoS属性支持PTT QCI。

```jinja2
{%- if is_optional_subscribed_qos_ptt_qci -%}
    {%- for item in add_epssubqos_list -%}
        ADD EPSSUBQOS:
        {#- --- 必选参数 --- -#}
        AMBRDL={{item.AMBRDL}},
        AMBRUL={{item.AMBRUL}},
        ARPPL={{item.ARPPL}},
        QCI={{item.QCI}},
        SUBQOSINDEX={{item.SUBQOSINDEX}},
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 3.8 （可选）配置QosProfile信息。

```jinja2
{%- if is_optional_qosprofile -%}
    {%- for item in add_qosprofile_list -%}
        ADD QOSPROFILE:
        {#- --- 必选参数 --- -#}
        QOSPROFILENAME="{{item.QOSPROFILENAME}}",
        {#- --- 可选参数 --- -#}
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
{%- endif -%}
```

#### 3.9 （可选）配置PCC预定义规则的QoS参数。

```jinja2
{%- if is_optional_pcc_qos_params -%}
    {%- for item in add_qosprop_list -%}
        ADD QOSPROP:
        {#- --- 必选参数 --- -#}
        QOSPROPNAME="{{item.QOSPROPNAME}}",
        QOSTYPE={{item.QOSTYPE}},
        {#- --- 可选参数 --- -#}
        {%- if item.EMPCAP is not none -%}
            EMPCAP={{item.EMPCAP}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：QOSTYPE=QOS_FLOW_PARA/QOS_L2_PARA 时必选 --- -#}
        {%- if item.QOSTYPE in ['QOS_FLOW_PARA', 'QOS_L2_PARA'] -%}
            FQI={{item.FQI}},
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：QOSTYPE=QOS_BEARER_PARA 时可选 --- -#}
        {%- if item.QOSTYPE == 'QOS_BEARER_PARA' -%}
            {%- if item.QCIVALUE is not none -%}
                QCIVALUE={{item.QCIVALUE}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOSTYPE=QOS_BEARER_PARA/QOS_FLOW_PARA 时可选 --- -#}
        {%- if item.QOSTYPE in ['QOS_BEARER_PARA', 'QOS_FLOW_PARA'] -%}
            {%- if item.QOSURRNAME is not none -%}
                QOSURRNAME="{{item.QOSURRNAME}}",
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOSTYPE=QOS_FLOW_PARA 时可选 --- -#}
        {%- if item.QOSTYPE == 'QOS_FLOW_PARA' -%}
            {%- if item.RQI is not none -%}
                RQI={{item.RQI}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件必选/可选参数 --- -#}
        {#- --- 分配保留优先级: 条件必选(QoS属性类型=QOS_FLOW_PARA|QOS_L2_PARA) / 条件可选(QoS属性类型=QOS_BEARER_PARA) --- -#}
        {%- if (item.QOSTYPE in ['QOS_FLOW_PARA', 'QOS_L2_PARA']) -%}
            ARPVALUE={{item.ARPVALUE}},
        {%- elif (item.QOSTYPE == 'QOS_BEARER_PARA') -%}
            {%- if item.ARPVALUE is not none -%}
                ARPVALUE={{item.ARPVALUE}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 4 基于APN的一键通业务配置：

#### 4.1 查询PTT业务QCI是否已经配置为标准QCI。

#### 4.2 开启基于APN的PTT业务配置开关。

```jinja2
{%- for item in add_apn_list -%}
    ADD APN:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_apnpttfunc_list -%}
    ADD APNPTTFUNC:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    {#- --- 可选参数 --- -#}
    {%- if item.LTEPTTSWITCH is not none -%}
        LTEPTTSWITCH={{item.LTEPTTSWITCH}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 4.3 （可选）配置用户的签约QoS属性支持PTT QCI。

```jinja2
{%- if is_optional_subscribed_qos_ptt_qci -%}
    {%- for item in add_epssubqos_list_1 -%}
        ADD EPSSUBQOS:
        {#- --- 必选参数 --- -#}
        AMBRDL={{item.AMBRDL}},
        AMBRUL={{item.AMBRUL}},
        ARPPL={{item.ARPPL}},
        QCI={{item.QCI}},
        SUBQOSINDEX={{item.SUBQOSINDEX}},
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 4.4 （可选）配置QosProfile信息。

```jinja2
{%- if is_optional_qosprofile -%}
    {%- for item in add_qosprofile_list_1 -%}
        ADD QOSPROFILE:
        {#- --- 必选参数 --- -#}
        QOSPROFILENAME="{{item.QOSPROFILENAME}}",
        {#- --- 可选参数 --- -#}
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
{%- endif -%}
```

#### 4.5 （可选）为APN实例绑定QosProfile。

```jinja2
{%- if is_optional_apn_bind_qosprofile -%}
    {%- for item in set_apnqosattr_list -%}
        SET APNQOSATTR:
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
{%- endif -%}
```


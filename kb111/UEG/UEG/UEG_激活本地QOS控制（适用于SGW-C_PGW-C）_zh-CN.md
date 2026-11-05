---
id: GWFD-022303
name: 激活本地QOS控制（适用于SGW-C/PGW-C）
ne_type: UEG
type: feature
description: 运营商根据UEG本地配置的QoS参数对用户数据进行控制。  适用于SGW-C、PGW-C。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝L","MEC 特性指南（风筝L）","GW-C&SMF特性指南","GWFD-022300 智能QoS管理增强","GWFD-022303 本地QOS控制","激活本地QOS控制（适用于SGW-C/PGW-C）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
运营商根据UEG本地配置的QoS参数对用户数据进行控制。适用于SGW-C、PGW-C。

## 必备事项
前提条件

* 请仔细阅读GWFD-022303 本地QOS控制特性概述。
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
          name: 'LICITEM'
          type: string
          minLength: 0
          maxLength: 255
          required: true
          description: '配置License配置开关'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SWITCH:
          name: 'SWITCH'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: true
          description: ''
          data_source: ''
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
          description: ''
          data_source: ''
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
          description: '可选：配置ARP和QCI的对应关系'
          data_source: '本端规划'
          pattern: ''
          default: ''
        ARPPCI:
          name: 'ARP的可抢占能力'
          type: integer
          minimum: 0
          maximum: 1
          required: false
          description: ''
          data_source: ''
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
    add_epssubqos_list:
      type: items
      properties:
        SUBQOSINDEX:
          name: '用户QOS索引'
          type: integer
          minimum: 0
          maximum: 255
          required: true
          description: ''
          data_source: ''
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
          description: '配置4G用户的签约QoS属性。'
          data_source: '本端规划'
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
    set_defepsqos_list:
      type: items
      properties:
        QOSCLASSID:
          name: 'QCI值'
          type: integer
          minimum: 1
          maximum: 255
          required: false
          description: '配置EPS本地缺省QoS参数，用于纠错。'
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
          name: '绑定EPS用户QoS'
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
          name: 'EPS用户QoS索引'
          type: integer
          minimum: 0
          maximum: 255
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
          name: '超过下行保证带宽的处理'
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
          name: '超过上行保证带宽的处理'
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
          name: '超过下行最大带宽的处理'
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
          name: '超过上行最大带宽的处理'
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
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV3W9LQOS12'
      SWITCH: ENABLE
    set_epsqci2prer8_list:
    - QCI: 4
      TRAFFICCLASS: CONVERSATIONAL
      THP: NORMAL
      SIGNALIND: OPTIMIZE
      SRCSTATDESC: SPEECH
    set_qci2arp_list:
    - QCI: 1
      ARPPCI: 0
      ARPPL: 1
      ARPPVI: 0
    add_epssubqos_list:
    - SUBQOSINDEX: 200
      QCI: 5
      ARPPL: 10
      AMBRDL: 564110
      AMBRUL: 300000
    set_defepsqos_list:
    - QOSCLASSID: 1
      ARPVALUE: 1
      GBRDL: 200
      GBRUL: 230
      MBRDL: 300
      MBRUL: 300
      APNAMBRDL: 1000
      APNAMBRUL: 1000
    set_cpqosglobal_list:
    - QOSPROFILENAME: 'qos2'
      BINDEPSSUBQOS: ENABLE
      EPSSUBQOS: 200
    add_qosprofile_list:
    - QOSPROFILENAME: 'qos1'
      BINDEPSSUBQOS: ENABLE
      EPSSUBQOS: 200
    add_epsqosaction_list:
    - QOSPROFILENAME: 'qos1'
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
      QOSPROFILENAME: 'qos1'
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 进入“MML命令行-UEG”窗口。

### 2 打开本特性的License配置开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

### 3 **可选**：配置EPC网络中的QoS参数和R99，R98 QoS参数的映射规则。缺省使用默认值

```jinja2
{%- if is_optional_qos_parameter_mapping_rule -%}
    {%- for item in set_epsqci2prer8_list -%}
        SET EPSQCI2PRER8:
        {#- --- 必选参数 --- -#}
        QCI={{item.QCI}},
        TRAFFICCLASS={{item.TRAFFICCLASS}},
        {#- --- 可选参数 --- -#}
        {%- if item.THP is not none -%}
            THP={{item.THP}},
        {%- endif -%}
        {%- if item.SIGNALIND is not none -%}
            SIGNALIND={{item.SIGNALIND}},
        {%- endif -%}
        {%- if item.SRCSTATDESC is not none -%}
            SRCSTATDESC={{item.SRCSTATDESC}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 4 **可选**：更改缺省的ARP和标准QCI的对应关系

```jinja2
{%- if is_optional_arp_qci_mapping -%}
    {%- for item in set_qci2arp_list -%}
        SET QCI2ARP:
        {#- --- 必选参数 --- -#}
        QCI={{item.QCI}},
        {#- --- 可选参数 --- -#}
        {%- if item.ARPPCI is not none -%}
            ARPPCI={{item.ARPPCI}},
        {%- endif -%}
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

### 5 **可选**：配置本地签约的QoS信息。

```jinja2
{%- if is_optional_local_subscribed_qos -%}
    {%- for item in add_epssubqos_list -%}
        ADD EPSSUBQOS:
        {#- --- 必选参数 --- -#}
        SUBQOSINDEX={{item.SUBQOSINDEX}},
        QCI={{item.QCI}},
        ARPPL={{item.ARPPL}},
        AMBRDL={{item.AMBRDL}},
        AMBRUL={{item.AMBRUL}},
        ;
    {%- endfor -%}
{%- endif -%}
```

### 6 配置EPS QoS缺省QoS参数（用于纠错）。

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

### 7 设置全局的QoS信息。

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

### 8 配置基于APN的QoS策略。

#### 8.1 配置指定APN实例下的QosProfile名称，并进入QoS实例。

```jinja2
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
```

#### 8.2 配置QoS上下行保证带宽门限、最高带宽门限以及带宽超过门限值时对QoS用户的处理动作。

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

#### 8.3 配置APN实例。

```jinja2
{%- for item in add_cpapn_list -%}
    ADD CPAPN:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    ;
{%- endfor -%}
```

#### 8.4 为APN实例绑定QoS profile。

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


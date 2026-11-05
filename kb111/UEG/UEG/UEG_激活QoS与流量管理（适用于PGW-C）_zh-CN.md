---
id: GWFD-021201
name: 激活QoS与流量管理（适用于PGW-C）
ne_type: UEG
type: feature
description: 通过配置QoS与流量管理，可实现以下需求：  * 为了保证在资源紧缺时，运营商能够为高优先级用户优先分配资源。 * 在资源相对富余时，更充分地发挥网络资源的效益，提高客户满意度。  QoS与流量管理指UEG支持3GPP QoS，按照QoS等级对用户报文进行分类，还可以提供DiffServ，从而支持流量监管、拥塞管理、拥塞避免等多种QoS实现技术。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝L","MEC 特性指南（风筝L）","GW-C&SMF特性指南","GWFD-021200 QoS与流量管理","GWFD-021201 QoS与流量管理","激活QoS与流量管理（适用于PGW-C）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
通过配置QoS与流量管理，可实现以下需求：* 为了保证在资源紧缺时，运营商能够为高优先级用户优先分配资源。* 在资源相对富余时，更充分地发挥网络资源的效益，提高客户满意度。QoS与流量管理指UEG支持3GPP QoS，按照QoS等级对用户报文进行分类，还可以提供DiffServ，从而支持流量监管、拥塞管理、拥塞避免等多种QoS实现技术。

## 必备事项
前提条件

* 完成配置普通APN。
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
          description: '配置整机使能用户的上下行Remark功能。'
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
    set_cpqosglobal_list:
      type: items
      properties:
        QOSPROFILENAME:
          name: 'Qos Profile名'
          type: string
          minLength: 1
          maxLength: 63
          required: false
          description: '配置基于全局的QoS Profile。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_epsremark_list:
      type: items
      properties:
        QOSPROFILENAME:
          name: 'Qos Profile名'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '配置在EPC架构下，QoS参数到IP报文头中的DSCP/ToS的映射规则。'
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
        S1UDSCPSWITCH:
          name: 'S1U DSCP配置开关'
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
    set_licenseswitch_list_1:
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
    set_qosremark_list_1:
      type: items
      properties:
        DOWNLINK:
          name: '下行标记'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '配置整机使能用户的上下行Remark功能。'
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
    add_qosprofile_list:
      type: items
      properties:
        QOSPROFILENAME:
          name: 'QoS名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '配置QosProfile，并进入Qos实例。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_epsremark_list_1:
      type: items
      properties:
        QOSPROFILENAME:
          name: 'Qos Profile名'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '配置在EPC架构下，QoS参数到IP报文头中的DSCP/ToS的映射规则。'
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
        S1UDSCPSWITCH:
          name: 'S1U DSCP配置开关'
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
    add_cpapn_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '配置指定APN实例。'
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
          description: '为该APN实例绑定QOSPROFILE。  如果APN配置了QosProfile，则该APN上全局下的QosProfile不会生效。'
          data_source: '从已配置数据中获取'
          pattern: ''
          default: ''
        HASQOSPROFILE:
          name: '有Qos Profile'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '从已配置数据中获取'
          pattern: ''
          default: ''
        QOSPROFILENAME:
          name: 'Qos Profile名'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: ''
          data_source: '本端规划'
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
          description: '配置QCI和ARP的对应关系。'
          data_source: '全网规划'
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
    set_defepsqos_list:
      type: items
      properties:
        QOSCLASSID:
          name: 'QCI值'
          type: integer
          minimum: 1
          maximum: 255
          required: false
          description: '配置EPS QoS纠错参数。'
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
        GBRUL:
          name: '上行保证带宽(千比特/秒)'
          type: integer
          minimum: 0
          maximum: 2000000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GBRDL:
          name: '下行保证带宽(千比特/秒)'
          type: integer
          minimum: 0
          maximum: 2000000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MBRDL:
          name: '下行最大带宽(千比特/秒)'
          type: integer
          minimum: 0
          maximum: 2000000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MBRUL:
          name: '上行最大带宽(千比特/秒)'
          type: integer
          minimum: 0
          maximum: 2000000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        APNAMBRDL:
          name: '下行APN AMBR(千比特/秒)'
          type: integer
          minimum: 0
          maximum: 2000000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        APNAMBRUL:
          name: '上行APN AMBR(千比特/秒)'
          type: integer
          minimum: 0
          maximum: 2000000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV3W9TCQS11'
      SWITCH: ENABLE
    set_qosremark_list:
    - DOWNLINK: ENABLE
      UPLINK: ENABLE
    set_cpqosglobal_list:
    - QOSPROFILENAME: 'gp1'
    add_epsremark_list:
    - QOSPROFILENAME: 'globalqos'
      QCI: 1
      ARPPL: 1
      REMARKTYPE: DSCP
      DSCP: EF
      S1UDSCPSWITCH: ENABLE
      S1UDSCP: EF
    set_licenseswitch_list_1:
    - LICITEM: 'LKV3W9TCQS11'
      SWITCH: ENABLE
    set_qosremark_list_1:
    - DOWNLINK: ENABLE
      UPLINK: ENABLE
    add_qosprofile_list:
    - QOSPROFILENAME: 'gp1'
    add_epsremark_list_1:
    - QOSPROFILENAME: 'gp1'
      QCI: 1
      ARPPL: 1
      REMARKTYPE: DSCP
      DSCP: EF
      S1UDSCPSWITCH: ENABLE
      S1UDSCP: EF
    add_cpapn_list:
    - APN: 'apn'
    set_cpapnqosattr_list:
    - APN: 'apn'
      HASQOSPROFILE: ENABLE
      QOSPROFILENAME: 'gp1'
    set_qci2arp_list:
    - QCI: 9
      ARPPCI: 0
      ARPPL: 1
      ARPPVI: 1
    set_defepsqos_list:
    - QOSCLASSID: 6
      ARPVALUE: 1
      GBRUL: 230
      GBRDL: 200
      MBRDL: 300
      MBRUL: 300
      APNAMBRDL: 1000
      APNAMBRUL: 1000
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 配置基于全局的EPS QoS到DSCP/ToS的映射关系。

#### 1.1 进入“MML命令行-UEG”窗口。

#### 1.2 配置整机使能用户的上下行Remark功能。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

#### ****SET QOSREMARK****

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

#### 1.3 配置基于全局的QoS Profile。

```jinja2
{%- for item in set_cpqosglobal_list -%}
    SET CPQOSGLOBAL:
    {#- --- 可选参数 --- -#}
    {%- if item.QOSPROFILENAME is not none -%}
        QOSPROFILENAME="{{item.QOSPROFILENAME}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 1.4 配置在EPC架构下，QoS参数到IP报文头中的DSCP/ToS的映射规则。

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
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：REMARKTYPE=DSCP 时必选 --- -#}
    {%- if item.REMARKTYPE == 'DSCP' -%}
        DSCP={{item.DSCP}},
    {%- endif -%}
    {#- --- 条件必选：S1UDSCPSWITCH=ENABLE 时必选 --- -#}
    {%- if item.S1UDSCPSWITCH == 'ENABLE' -%}
        S1UDSCP={{item.S1UDSCP}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 2 * **可选：**配置基于APN的EPS QoS到DSCP/ToS的映射关系。

#### 2.1 进入“MML命令行-UEG”窗口。

#### 2.2 配置整机使能用户的上下行Remark功能。

```jinja2
{%- if is_optional_apn_eps_qos_dscp_tos_mapping -%}
    {%- for item in set_licenseswitch_list_1 -%}
        SET LICENSESWITCH:
        {#- --- 必选参数 --- -#}
        LICITEM="{{item.LICITEM}}",
        SWITCH={{item.SWITCH}},
        ;
    {%- endfor -%}
{%- endif -%}
```

#### ****SET QOSREMARK****

```jinja2
{%- if is_optional_apn_eps_qos_dscp_tos_mapping -%}
    {%- for item in set_qosremark_list_1 -%}
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
{%- endif -%}
```

#### 2.3 配置QosProfile。

```jinja2
{%- if is_optional_apn_eps_qos_dscp_tos_mapping -%}
    {%- for item in add_qosprofile_list -%}
        ADD QOSPROFILE:
        {#- --- 必选参数 --- -#}
        QOSPROFILENAME="{{item.QOSPROFILENAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 2.4 配置在EPC架构下，QoS参数到IP报文头中的DSCP/ToS的映射规则。

#### ****ADD EPSREMARK****

```jinja2
{%- if is_optional_apn_eps_qos_dscp_tos_mapping -%}
    {%- for item in add_epsremark_list_1 -%}
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
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：REMARKTYPE=DSCP 时必选 --- -#}
        {%- if item.REMARKTYPE == 'DSCP' -%}
            DSCP={{item.DSCP}},
        {%- endif -%}
        {#- --- 条件必选：S1UDSCPSWITCH=ENABLE 时必选 --- -#}
        {%- if item.S1UDSCPSWITCH == 'ENABLE' -%}
            S1UDSCP={{item.S1UDSCP}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 2.5 配置指定AP实例。

```jinja2
{%- if is_optional_apn_eps_qos_dscp_tos_mapping -%}
    {%- for item in add_cpapn_list -%}
        ADD CPAPN:
        {#- --- 必选参数 --- -#}
        APN="{{item.APN}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 2.6 为该APN实例绑定QOSPROFILE。

```jinja2
{%- if is_optional_apn_eps_qos_dscp_tos_mapping -%}
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
{%- endif -%}
```

### 3 配置QCI和ARP的对应关系。

#### 3.1 进入“MML命令行-UEG”窗口。

#### 3.2 配置QCI和ARP的对应关系。

```jinja2
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
```

### 4 配置EPS QoS纠错参数。

#### 4.1 进入“MML命令行-UEG”窗口。

#### 4.2 配置EPS QoS纠错参数。

```jinja2
{%- for item in set_defepsqos_list -%}
    SET DEFEPSQOS:
    {#- --- 可选参数 --- -#}
    {%- if item.ARPVALUE is not none -%}
        ARPVALUE={{item.ARPVALUE}},
    {%- endif -%}
    {%- if item.MBRDL is not none -%}
        MBRDL={{item.MBRDL}},
    {%- endif -%}
    {%- if item.GBRDL is not none -%}
        GBRDL={{item.GBRDL}},
    {%- endif -%}
    {%- if item.APNAMBRDL is not none -%}
        APNAMBRDL={{item.APNAMBRDL}},
    {%- endif -%}
    {%- if item.APNAMBRUL is not none -%}
        APNAMBRUL={{item.APNAMBRUL}},
    {%- endif -%}
    {%- if item.QOSCLASSID is not none -%}
        QOSCLASSID={{item.QOSCLASSID}},
    {%- endif -%}
    {%- if item.GBRUL is not none -%}
        GBRUL={{item.GBRUL}},
    {%- endif -%}
    {%- if item.MBRUL is not none -%}
        MBRUL={{item.MBRUL}},
    {%- endif -%}
    ;
{%- endfor -%}
```


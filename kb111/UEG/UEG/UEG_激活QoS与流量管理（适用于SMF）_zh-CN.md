---
id: GWFD-021201
name: 激活QoS与流量管理（适用于SMF）
ne_type: UEG
type: feature
description: 通过配置QoS与流量管理，可实现以下需求：  * 保证在资源紧缺时，运营商能够为高优先级用户优先分配资源。 * 在资源相对富余时，更充分地发挥网络资源的效益，提高客户满意度。  QoS与流量管理指UEG支持3GPP QoS，按照QoS等级对用户报文进行分类，还可以提供DiffServ，从而支持流量监管、拥塞管理、拥塞避免等多种QoS实现技术。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝L","MEC 特性指南（风筝L）","GW-C&SMF特性指南","GWFD-021200 QoS与流量管理","GWFD-021201 QoS与流量管理","激活QoS与流量管理（适用于SMF）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
通过配置QoS与流量管理，可实现以下需求：* 保证在资源紧缺时，运营商能够为高优先级用户优先分配资源。* 在资源相对富余时，更充分地发挥网络资源的效益，提高客户满意度。QoS与流量管理指UEG支持3GPP QoS，按照QoS等级对用户报文进行分类，还可以提供DiffServ，从而支持流量监管、拥塞管理、拥塞避免等多种QoS实现技术。

## 必备事项
前提条件

* 完成配置普通APN。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
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
          name: 'QoS Profile名'
          type: string
          minLength: 1
          maxLength: 63
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_5gcremark_list:
      type: items
      properties:
        QOSPROFILENAME:
          name: 'Qos Profile名'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '配置在5GC架构下，QoS参数到IP报文头中的DSCP/ToS的映射规则。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        FIVEQI:
          name: '5QI'
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
        N3DSCPSWITCH:
          name: 'N3 DSCP配置开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        N3DSCP:
          name: 'N3 DSCP'
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
    add_5gcremark_list_1:
      type: items
      properties:
        QOSPROFILENAME:
          name: 'Qos Profile名'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '配置在5GC架构下，QoS参数到IP报文头中的DSCP/ToS的映射规则。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        FIVEQI:
          name: '5QI'
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
        N3DSCPSWITCH:
          name: 'N3 DSCP配置开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        N3DSCP:
          name: 'N3 DSCP'
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
          data_source: '本端规划'
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
          description: '配置5QI和ARP的对应关系。'
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
    set_5gcqoscorrt_list:
      type: items
      properties:
        AMBRDL:
          name: '下行Session AMBR(千比特/秒)'
          type: integer
          minimum: 0
          maximum: 20000000
          required: false
          description: '配置5G QoS纠错参数。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        AMBRUL:
          name: '上行Session AMBR(千比特/秒)'
          type: integer
          minimum: 0
          maximum: 20000000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        FIVEQI:
          name: '5QI值'
          type: integer
          minimum: 1
          maximum: 255
          required: false
          description: ''
          data_source: ''
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
        GFBRUL:
          name: '上行保证带宽(千比特/秒)'
          type: integer
          minimum: 0
          maximum: 20000000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GFBRDL:
          name: '下行保证带宽(千比特/秒)'
          type: integer
          minimum: 0
          maximum: 20000000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MFBRDL:
          name: '下行最大带宽(千比特/秒)'
          type: integer
          minimum: 0
          maximum: 20000000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MFBRUL:
          name: '上行最大带宽(千比特/秒)'
          type: integer
          minimum: 0
          maximum: 20000000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        QOS5QIPL:
          name: '5QI优先级'
          type: integer
          minimum: 1
          maximum: 127
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    set_qosremark_list:
    - DOWNLINK: ENABLE
      UPLINK: ENABLE
    set_cpqosglobal_list:
    - QOSPROFILENAME: 'globalqos'
    add_5gcremark_list:
    - QOSPROFILENAME: 'globalqos'
      FIVEQI: 1
      ARPPL: 1
      REMARKTYPE: DSCP
      DSCP: EF
      N3DSCPSWITCH: ENABLE
      N3DSCP: EF
    set_qosremark_list_1:
    - DOWNLINK: ENABLE
      UPLINK: ENABLE
    add_qosprofile_list:
    - QOSPROFILENAME: 'gp1'
    add_5gcremark_list_1:
    - QOSPROFILENAME: 'gp1'
      FIVEQI: 1
      ARPPL: 1
      REMARKTYPE: DSCP
      DSCP: EF
      N3DSCPSWITCH: ENABLE
      N3DSCP: EF
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
    set_5gcqoscorrt_list:
    - AMBRDL: 20000
      AMBRUL: 20000
      FIVEQI: 5
      ARPVALUE: 3
      GFBRUL: 4000
      GFBRDL: 4000
      MFBRDL: 5000
      MFBRUL: 5000
      QOS5QIPL: 10
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 配置基于全局的3GPP QoS到DSCP/ToS的映射关系。

#### 1.1 进入“MML命令行-UEG”窗口。

#### 1.2 配置整机使能用户的上下行Remark功能。

#### ****SET QOSREMARK****

```jinja2
{%- if is_scenario_global_qos_mapping -%}
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
{%- endif -%}
```

#### 1.3 配置基于全局的QoS Profile。

```jinja2
{%- if is_scenario_global_qos_mapping -%}
    {%- for item in set_cpqosglobal_list -%}
        SET CPQOSGLOBAL:
        {#- --- 可选参数 --- -#}
        {%- if item.QOSPROFILENAME is not none -%}
            QOSPROFILENAME="{{item.QOSPROFILENAME}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 1.4 配置在5GC架构下，QoS参数到IP报文头中的DSCP/ToS的映射规则。

```jinja2
{%- if is_scenario_global_qos_mapping -%}
    {%- for item in add_5gcremark_list -%}
        ADD 5GCREMARK:
        {#- --- 必选参数 --- -#}
        QOSPROFILENAME="{{item.QOSPROFILENAME}}",
        FIVEQI={{item.FIVEQI}},
        ARPPL={{item.ARPPL}},
        REMARKTYPE={{item.REMARKTYPE}},
        {#- --- 可选参数 --- -#}
        {%- if item.N3DSCPSWITCH is not none -%}
            N3DSCPSWITCH={{item.N3DSCPSWITCH}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：REMARKTYPE=DSCP 时必选 --- -#}
        {%- if item.REMARKTYPE == 'DSCP' -%}
            DSCP={{item.DSCP}},
        {%- endif -%}
        {#- --- 条件必选：N3DSCPSWITCH=ENABLE 时必选 --- -#}
        {%- if item.N3DSCPSWITCH == 'ENABLE' -%}
            N3DSCP={{item.N3DSCP}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 2 配置基于APN的3GPP QoS到DSCP/ToS的映射关系。

#### 2.1 进入“MML命令行-UEG”窗口。

#### 2.2 配置整机使能用户的上下行Remark功能。

#### ****SET QOSREMARK****

```jinja2
{%- if is_scenario_apn_qos_mapping -%}
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
{%- if is_scenario_apn_qos_mapping -%}
    {%- for item in add_qosprofile_list -%}
        ADD QOSPROFILE:
        {#- --- 必选参数 --- -#}
        QOSPROFILENAME="{{item.QOSPROFILENAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 2.4 配置在5GC架构下，QoS参数到IP报文头中的DSCP/ToS的映射规则。

#### ****ADD 5GCREMARK****

```jinja2
{%- if is_scenario_apn_qos_mapping -%}
    {%- for item in add_5gcremark_list_1 -%}
        ADD 5GCREMARK:
        {#- --- 必选参数 --- -#}
        QOSPROFILENAME="{{item.QOSPROFILENAME}}",
        FIVEQI={{item.FIVEQI}},
        ARPPL={{item.ARPPL}},
        REMARKTYPE={{item.REMARKTYPE}},
        {#- --- 可选参数 --- -#}
        {%- if item.N3DSCPSWITCH is not none -%}
            N3DSCPSWITCH={{item.N3DSCPSWITCH}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：REMARKTYPE=DSCP 时必选 --- -#}
        {%- if item.REMARKTYPE == 'DSCP' -%}
            DSCP={{item.DSCP}},
        {%- endif -%}
        {#- --- 条件必选：N3DSCPSWITCH=ENABLE 时必选 --- -#}
        {%- if item.N3DSCPSWITCH == 'ENABLE' -%}
            N3DSCP={{item.N3DSCP}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 2.5 配置指定APN实例。

```jinja2
{%- if is_scenario_apn_qos_mapping -%}
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
{%- if is_scenario_apn_qos_mapping -%}
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

### 3 配置5QI和ARP的对应关系。

#### 3.1 进入“MML命令行-UEG”窗口。

#### 3.2 配置5QI和ARP的对应关系。

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

### 4 配置5G QoS纠错参数。

#### 4.1 进入“MML命令行-UEG”窗口。

#### 4.2 配置5G QoS纠错参数。

#### ****SET 5GCQOSCORRT****

```jinja2
{%- for item in set_5gcqoscorrt_list -%}
    SET 5GCQOSCORRT:
    {#- --- 可选参数 --- -#}
    {%- if item.FIVEQI is not none -%}
        FIVEQI={{item.FIVEQI}},
    {%- endif -%}
    {%- if item.QOS5QIPL is not none -%}
        QOS5QIPL={{item.QOS5QIPL}},
    {%- endif -%}
    {%- if item.ARPVALUE is not none -%}
        ARPVALUE={{item.ARPVALUE}},
    {%- endif -%}
    {%- if item.AMBRDL is not none -%}
        AMBRDL={{item.AMBRDL}},
    {%- endif -%}
    {%- if item.AMBRUL is not none -%}
        AMBRUL={{item.AMBRUL}},
    {%- endif -%}
    {%- if item.GFBRUL is not none -%}
        GFBRUL={{item.GFBRUL}},
    {%- endif -%}
    {%- if item.GFBRDL is not none -%}
        GFBRDL={{item.GFBRDL}},
    {%- endif -%}
    {%- if item.MFBRUL is not none -%}
        MFBRUL={{item.MFBRUL}},
    {%- endif -%}
    {%- if item.MFBRDL is not none -%}
        MFBRDL={{item.MFBRDL}},
    {%- endif -%}
    ;
{%- endfor -%}
```


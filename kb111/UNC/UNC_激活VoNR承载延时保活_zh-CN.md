---
id: ''
name: 激活VoNR承载延时保活
ne_type: UNC
type: feature
description: 用户在VoNR通话过程中，当连接态的UE进入没有无线信号的区域后（例如：电梯、隧道或者山洞），短时间内SMF保留VoNR承载（包括5QI=1（语音）和5QI=2（视频）等等），当用户可以接入网络后，原VoNR不会掉话，提升用户业务体验。  适用于SMF。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","语音功能","WSFD-221001 VoNR承载延时保活","激活VoNR承载延时保活"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
用户在VoNR通话过程中，当连接态的UE进入没有无线信号的区域后（例如：电梯、隧道或者山洞），短时间内SMF保留VoNR承载（包括5QI=1（语音）和5QI=2（视频）等等），当用户可以接入网络后，原VoNR不会掉话，提升用户业务体验。适用于SMF。

## 必备事项
前提条件

* 请仔细阅读WSFD-221001 VoNR承载延时保活特性概述。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    add_deactqfplcy_list:
      type: items
      properties:
        NGAPCAUSEGROUP:
          name: 'NgApCause组'
          type: string
          enum:
          - RADIO_NETWORK
          - TRANSPORT
          - NAS
          - PROTOCOL
          - MISC
          - INVALID
          required: true
          description: '配置整系统粒度专有QoS Flow去活策略。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        NGAPCAUSEVALUE:
          name: 'NgApCause值'
          type: integer
          minimum: 0
          maximum: 255
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        QFPLCY:
          name: '专有GBR类型QoS Flow处理策略'
          type: string
          enum:
          - RELEASE
          - DELAY_RELEASE
          - NOT_RELEASE
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        DELAYTIMER:
          name: '延迟释放专有GBR类型QoS Flow时长(秒)'
          type: integer
          minimum: 10
          maximum: 100
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: 60
    add_apndeactqfplcy_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '配置APN粒度专有QoS Flow去活策略。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        NGAPCAUSEGROUP:
          name: 'NgApCause组'
          type: string
          enum:
          - RADIO_NETWORK
          - TRANSPORT
          - NAS
          - PROTOCOL
          - MISC
          - INVALID
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        NGAPCAUSEVALUE:
          name: 'NgApCause值'
          type: integer
          minimum: 0
          maximum: 255
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        QFPLCY:
          name: '专有GBR类型QoS Flow处理策略'
          type: string
          enum:
          - RELEASE
          - DELAY_RELEASE
          - NOT_RELEASE
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        DELAYTIMER:
          name: '延迟释放专有GBR类型QoS Flow时长(秒)'
          type: integer
          minimum: 10
          maximum: 100
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: 60
    set_qosflowfunc_list:
      type: items
      properties:
        EPSTO5GSQFPLCY:
          name: 'EPS切换到5GS专有GBR类型QoS Flow策略'
          type: string
          enum:
          - RELEASE
          - DELAY_RELEASE
          - NOT_RELEASE
          required: false
          description: '配置EPS切换到5GS专有GBR类型QoS Flow策略。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        ISMFQFPLCY:
          name: '插入删除I-SMF专有GBR类型QoS Flow策略'
          type: string
          enum:
          - RELEASE
          - DELAY_RELEASE
          - NOT_RELEASE
          required: false
          description: '配置插入I-SMF场景下QoS Flow去活策略。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        DELAYTIMER:
          name: '延迟释放专有GBR类型QoS Flow时长(秒)'
          type: integer
          minimum: 10
          maximum: 100
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
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
  examples:
    add_deactqfplcy_list:
    - NGAPCAUSEGROUP: RADIO_NETWORK
      NGAPCAUSEVALUE: 21
      QFPLCY: DELAY_RELEASE
      DELAYTIMER: 60
    add_apndeactqfplcy_list:
    - APN: 'ims'
      NGAPCAUSEGROUP: RADIO_NETWORK
      NGAPCAUSEVALUE: 21
      QFPLCY: DELAY_RELEASE
      DELAYTIMER: 60
    set_qosflowfunc_list:
    - EPSTO5GSQFPLCY: DELAY_RELEASE
      ISMFQFPLCY: DELAY_RELEASE
      DELAYTIMER: 60
    set_licenseswitch_list:
    - LICITEM: 'LKV2VCHSM01'
      SWITCH: ENABLE
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 进入“MML命令行-UNC”窗口。

### 2 **可选：**配置整系统粒度专有QoS Flow去活策略。

```jinja2
{%- if is_optional_system_level_qosflow_deactivation -%}
    {%- for item in add_deactqfplcy_list -%}
        ADD DEACTQFPLCY:
        {#- --- 必选参数 --- -#}
        NGAPCAUSEGROUP={{item.NGAPCAUSEGROUP}},
        NGAPCAUSEVALUE={{item.NGAPCAUSEVALUE}},
        QFPLCY={{item.QFPLCY}},
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：QFPLCY=DELAY_RELEASE 时可选 --- -#}
        {%- if item.QFPLCY == 'DELAY_RELEASE' -%}
            {%- if item.DELAYTIMER is not none -%}
                DELAYTIMER={{item.DELAYTIMER}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 3 **可选：**配置APN粒度专有QoS Flow去活策略。

```jinja2
{%- if is_optional_apn_level_qosflow_deactivation -%}
    {%- for item in add_apndeactqfplcy_list -%}
        ADD APNDEACTQFPLCY:
        {#- --- 必选参数 --- -#}
        APN="{{item.APN}}",
        NGAPCAUSEGROUP={{item.NGAPCAUSEGROUP}},
        NGAPCAUSEVALUE={{item.NGAPCAUSEVALUE}},
        QFPLCY={{item.QFPLCY}},
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：QFPLCY=DELAY_RELEASE 时可选 --- -#}
        {%- if item.QFPLCY == 'DELAY_RELEASE' -%}
            {%- if item.DELAYTIMER is not none -%}
                DELAYTIMER={{item.DELAYTIMER}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 4 **可选：**配置插入或删除I-SMF场景下QoS Flow去活策略。

```jinja2
{%- if is_optional_ismf_qosflow_deactivation -%}
    {%- for item in set_qosflowfunc_list -%}
        SET QOSFLOWFUNC:
        {#- --- 可选参数 --- -#}
        {%- if item.EPSTO5GSQFPLCY is not none -%}
            EPSTO5GSQFPLCY={{item.EPSTO5GSQFPLCY}},
        {%- endif -%}
        {%- if item.ISMFQFPLCY is not none -%}
            ISMFQFPLCY={{item.ISMFQFPLCY}},
        {%- endif -%}
        {%- if item.DELAYTIMER is not none -%}
            DELAYTIMER={{item.DELAYTIMER}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 5 打开本特性的License配置开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```


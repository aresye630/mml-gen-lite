---
id: ''
name: 激活QoS与流量管理（适用于GGSN）
ne_type: UNC
type: feature
description: 通过配置QoS与流量管理，可实现以下需求：  * 为了保证在资源紧缺时，运营商能够为高优先级用户优先分配资源。 * 在资源相对富余时，更充分地发挥网络资源的效益，提高客户满意度。  QoS与流量管理指UNC支持3GPP QoS，按照QoS等级对用户报文进行分类，还可以提供DiffServ，从而支持流量监管、拥塞管理、拥塞避免等多种QoS实现技术。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","QoS功能","WSFD-010701 QoS与流量管理","激活QoS与流量管理（适用于GGSN）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
通过配置QoS与流量管理，可实现以下需求：* 为了保证在资源紧缺时，运营商能够为高优先级用户优先分配资源。* 在资源相对富余时，更充分地发挥网络资源的效益，提高客户满意度。QoS与流量管理指UNC支持3GPP QoS，按照QoS等级对用户报文进行分类，还可以提供DiffServ，从而支持流量监管、拥塞管理、拥塞避免等多种QoS实现技术。

## 必备事项
前提条件

前提条件

* 请仔细阅读WSFD-010701 QoS与流量管理特性概述。
* 完成配置普通APN。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    add_prer8subqos_list:
      type: items
      properties:
        SUBQOSINDEX:
          name: '用户QOS索引'
          type: integer
          minimum: 0
          maximum: 255
          required: true
          description: '配置签约QoS属性。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        ARP:
          name: 'ARP值'
          type: string
          enum:
          - HIGH
          - NORMAL
          - LOW
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CONVGBRDL:
          name: '会话类下行保证带宽'
          type: integer
          minimum: 0
          maximum: 256000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CONVGBRUL:
          name: '会话类上行保证带宽'
          type: integer
          minimum: 0
          maximum: 256000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CONVMBRDL:
          name: '会话类下行最大带宽'
          type: integer
          minimum: 0
          maximum: 256000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CONVMBRUL:
          name: '会话类上行最大带宽'
          type: integer
          minimum: 0
          maximum: 256000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        HIGHESTTC:
          name: '最高业务级别'
          type: string
          enum:
          - CONVERSATIONAL
          - STREAMING
          - INTERACTIVE
          - BACKGROUND
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: CONVERSATIONAL
        ACTION:
          name: '超过最高业务级别时的处理'
          type: string
          enum:
          - DEGRADE
          - REJECT
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DEGRADE
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
    set_qosglobal_list:
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
    add_prer8remark_list:
      type: items
      properties:
        QOSPROFILENAME:
          name: 'QoS Profile名'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '配置GPRS/UMTS QoS到DSCP或者TOS的映射规则。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SERVICELEVEL:
          name: '业务级别'
          type: string
          enum:
          - CONVERSATIONAL
          - STM_GBR_MORE25K
          - STM_GBR_LESS25K
          - INT_TC_PRI1
          - INT_TC_PRI2
          - INT_TC_PRI3
          - BACKGROUND
          - GENERAL
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        USERPRIORITY:
          name: '用户级别'
          type: string
          enum:
          - GENERAL
          - HIGH
          - NORMAL
          - LOW
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
          data_source: '全网规划'
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
    add_prer8remark_list_1:
      type: items
      properties:
        QOSPROFILENAME:
          name: 'QoS Profile名'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '配置GPRS/UMTS QoS到DSCP或者TOS的映射规则。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SERVICELEVEL:
          name: '业务级别'
          type: string
          enum:
          - CONVERSATIONAL
          - STM_GBR_MORE25K
          - STM_GBR_LESS25K
          - INT_TC_PRI1
          - INT_TC_PRI2
          - INT_TC_PRI3
          - BACKGROUND
          - GENERAL
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        USERPRIORITY:
          name: '用户级别'
          type: string
          enum:
          - GENERAL
          - HIGH
          - NORMAL
          - LOW
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
          data_source: '全网规划'
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
    add_apn_list:
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
    set_apnqosattr_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '为该APN实例绑定QOSPROFILE。  如果APN配置了QosProfile，则该APN上全局下的QosProfile不会生效。'
          data_source: '全网规划'
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
    set_qosremark_list_2:
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
    add_qosprofile_list_1:
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
    add_5gcremark_list:
      type: items
      properties:
        QOSPROFILENAME:
          name: 'QoS Profile名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: ''
          data_source: ''
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
    add_prer8remark_list_2:
      type: items
      properties:
        QOSPROFILENAME:
          name: 'QoS Profile名'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '配置GPRS/UMTS QoS到DSCP或者TOS的映射规则。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SERVICELEVEL:
          name: '业务级别'
          type: string
          enum:
          - CONVERSATIONAL
          - STM_GBR_MORE25K
          - STM_GBR_LESS25K
          - INT_TC_PRI1
          - INT_TC_PRI2
          - INT_TC_PRI3
          - BACKGROUND
          - GENERAL
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        USERPRIORITY:
          name: '用户级别'
          type: string
          enum:
          - GENERAL
          - HIGH
          - NORMAL
          - LOW
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
          data_source: '全网规划'
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
    add_apn_list_1:
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
    set_apnqosattr_list_1:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '为该APN实例绑定QOSPROFILE。  如果APN配置了QosProfile，则该APN上全局下的QosProfile不会生效。'
          data_source: '全网规划'
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
    set_defprer8qos_list:
      type: items
      properties:
        ARPVALUE:
          name: 'ARP值'
          type: string
          enum:
          - HIGH
          - NORMAL
          - LOW
          required: false
          description: '配置PreR8 QoS纠错。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        GBRUL:
          name: '上行保证带宽(千比特/秒)'
          type: integer
          minimum: 0
          maximum: 256000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GBRDL:
          name: '下行保证带宽(千比特/秒)'
          type: integer
          minimum: 0
          maximum: 256000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MBRDL:
          name: '下行最大带宽(千比特/秒)'
          type: integer
          minimum: 0
          maximum: 256000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MBRUL:
          name: '上行最大带宽(千比特/秒)'
          type: integer
          minimum: 0
          maximum: 256000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    add_prer8subqos_list:
    - SUBQOSINDEX: 1
      ARP: HIGH（高）
      CONVGBRDL: 200
      CONVGBRUL: 230
      CONVMBRDL: 300
      CONVMBRUL: 300
      HIGHESTTC: CONVERSATIONAL
      ACTION: DEGRADE
    set_qosremark_list:
    - DOWNLINK: ENABLE
      UPLINK: ENABLE
    set_qosglobal_list:
    - QOSPROFILENAME: 'gp1'
    add_prer8remark_list:
    - QOSPROFILENAME: 'globalqos'
      SERVICELEVEL: CONVERSATIONAL
      USERPRIORITY: HIGH
      REMARKTYPE: DSCP
      DSCP: EF
      AFCLASS: ''
      AFDROPPREC: ''
      DSCPVALUE: ''
      TOSVALUE: ''
    set_qosremark_list_1:
    - DOWNLINK: ENABLE
      UPLINK: ENABLE
    add_qosprofile_list:
    - QOSPROFILENAME: 'gp1'
    add_prer8remark_list_1:
    - QOSPROFILENAME: 'gp1'
      SERVICELEVEL: CONVERSATIONAL
      USERPRIORITY: HIGH
      REMARKTYPE: DSCP
      DSCP: EF
      AFCLASS: ''
      AFDROPPREC: ''
      DSCPVALUE: ''
      TOSVALUE: ''
    add_apn_list:
    - APN: 'apn'
    set_apnqosattr_list:
    - APN: 'apn'
      HASQOSPROFILE: ENABLE
      QOSPROFILENAME: 'gp1'
    set_qosremark_list_2:
    - DOWNLINK: ENABLE
      UPLINK: ENABLE
    add_qosprofile_list_1:
    - QOSPROFILENAME: 'gp1'
    add_5gcremark_list:
    - QOSPROFILENAME: ''
      FIVEQI: ''
      ARPPL: ''
      REMARKTYPE: ''
      DSCP: ''
      TOSVALUE: ''
    add_prer8remark_list_2:
    - QOSPROFILENAME: 'gp1'
      SERVICELEVEL: CONVERSATIONAL
      USERPRIORITY: HIGH
      REMARKTYPE: DSCP
      DSCP: EF
      AFCLASS: ''
      AFDROPPREC: ''
      DSCPVALUE: ''
      TOSVALUE: ''
    add_apn_list_1:
    - APN: 'apn'
    set_apnqosattr_list_1:
    - APN: 'apn'
      HASQOSPROFILE: ENABLE
      QOSPROFILENAME: 'gp1'
    set_defprer8qos_list:
    - ARPVALUE: '1'
      GBRUL: 230
      GBRDL: 200
      MBRDL: 300
      MBRUL: 300
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 配置签约QoS属性。

#### 1.1 进入“MML命令行-UNC”窗口。

#### 1.2 配置签约QoS。

```jinja2
{%- for item in add_prer8subqos_list -%}
    ADD PRER8SUBQOS:
    {#- --- 必选参数 --- -#}
    SUBQOSINDEX={{item.SUBQOSINDEX}},
    {#- --- 可选参数 --- -#}
    {%- if item.ACTION is not none -%}
        ACTION={{item.ACTION}},
    {%- endif -%}
    {%- if item.ARP is not none -%}
        ARP={{item.ARP}},
    {%- endif -%}
    {%- if item.CONVGBRDL is not none -%}
        CONVGBRDL={{item.CONVGBRDL}},
    {%- endif -%}
    {%- if item.CONVGBRUL is not none -%}
        CONVGBRUL={{item.CONVGBRUL}},
    {%- endif -%}
    {%- if item.CONVMBRDL is not none -%}
        CONVMBRDL={{item.CONVMBRDL}},
    {%- endif -%}
    {%- if item.CONVMBRUL is not none -%}
        CONVMBRUL={{item.CONVMBRUL}},
    {%- endif -%}
    {%- if item.HIGHESTTC is not none -%}
        HIGHESTTC={{item.HIGHESTTC}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 2 配置基于全局的3GPP QoS到DSCP/ToS的映射关系。

#### 2.1 进入“MML命令行-UNC”窗口。

#### 2.2 配置整机使能用户的上下行Remark功能。

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

#### 2.3 配置基于全局的QoS Profile。

```jinja2
{%- for item in set_qosglobal_list -%}
    SET QOSGLOBAL:
    {#- --- 可选参数 --- -#}
    {%- if item.QOSPROFILENAME is not none -%}
        QOSPROFILENAME="{{item.QOSPROFILENAME}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 2.4 配置PreR8 QoS参数到IP报文头中的DSCP/ToS的映射规则。

```jinja2
{%- for item in add_prer8remark_list -%}
    ADD PRER8REMARK:
    {#- --- 必选参数 --- -#}
    QOSPROFILENAME="{{item.QOSPROFILENAME}}",
    SERVICELEVEL={{item.SERVICELEVEL}},
    USERPRIORITY={{item.USERPRIORITY}},
    REMARKTYPE={{item.REMARKTYPE}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：REMARKTYPE=DSCP 时必选 --- -#}
    {%- if item.REMARKTYPE == 'DSCP' -%}
        DSCP={{item.DSCP}},
    {%- endif -%}
    {#- --- 条件必选：DSCP=AF 时必选 --- -#}
    {%- if item.DSCP == 'AF' -%}
        AFCLASS={{item.AFCLASS}},
    {%- endif -%}
    {#- --- 条件必选：DSCP=AF 时必选 --- -#}
    {%- if item.DSCP == 'AF' -%}
        AFDROPPREC={{item.AFDROPPREC}},
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
```

### 3 **可选：**配置基于APN的3GPP QoS到DSCP/ToS的映射关系。

#### 3.1 进入“MML命令行-UNC”窗口。

#### 3.2 配置整机使能用户的上下行Remark功能。

```jinja2
{%- if is_optional_apn_qos_mapping -%}
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

#### 3.3 配置QosProfile。

```jinja2
{%- if is_optional_apn_qos_mapping -%}
    {%- for item in add_qosprofile_list -%}
        ADD QOSPROFILE:
        {#- --- 必选参数 --- -#}
        QOSPROFILENAME="{{item.QOSPROFILENAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 3.4 配置PreR8 QoS参数到IP报文头中的DSCP/ToS的映射规则。

```jinja2
{%- if is_optional_apn_qos_mapping -%}
    {%- for item in add_prer8remark_list_1 -%}
        ADD PRER8REMARK:
        {#- --- 必选参数 --- -#}
        QOSPROFILENAME="{{item.QOSPROFILENAME}}",
        SERVICELEVEL={{item.SERVICELEVEL}},
        USERPRIORITY={{item.USERPRIORITY}},
        REMARKTYPE={{item.REMARKTYPE}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：REMARKTYPE=DSCP 时必选 --- -#}
        {%- if item.REMARKTYPE == 'DSCP' -%}
            DSCP={{item.DSCP}},
        {%- endif -%}
        {#- --- 条件必选：DSCP=AF 时必选 --- -#}
        {%- if item.DSCP == 'AF' -%}
            AFCLASS={{item.AFCLASS}},
        {%- endif -%}
        {#- --- 条件必选：DSCP=AF 时必选 --- -#}
        {%- if item.DSCP == 'AF' -%}
            AFDROPPREC={{item.AFDROPPREC}},
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

#### 3.5 配置指定AP实例。

```jinja2
{%- if is_optional_apn_qos_mapping -%}
    {%- for item in add_apn_list -%}
        ADD APN:
        {#- --- 必选参数 --- -#}
        APN="{{item.APN}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 3.6 为该APN实例绑定QOSPROFILE。

```jinja2
{%- if is_optional_apn_qos_mapping -%}
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

### 4 置基于APN的3GPP QoS到DSCP/ToS的映射关系。

#### 4.1 进入“MML命令行-UNC”窗口。

#### 4.2 配置整机使能用户的上下行Remark功能。

```jinja2
{%- if is_scenario_5gc -%}
    {%- for item in set_qosremark_list_2 -%}
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

#### 4.3 配置QosProfile。

```jinja2
{%- if is_scenario_5gc -%}
    {%- for item in add_qosprofile_list_1 -%}
        ADD QOSPROFILE:
        {#- --- 必选参数 --- -#}
        QOSPROFILENAME="{{item.QOSPROFILENAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 4.4 配置在5GC架构下，QoS参数到IP报文头中的DSCP/ToS的映射规则。

```jinja2
{%- if is_scenario_5gc -%}
    {%- for item in add_5gcremark_list -%}
        ADD 5GCREMARK:
        {#- --- 必选参数 --- -#}
        ARPPL={{item.ARPPL}},
        FIVEQI={{item.FIVEQI}},
        QOSPROFILENAME="{{item.QOSPROFILENAME}}",
        REMARKTYPE={{item.REMARKTYPE}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：REMARKTYPE=DSCP 时必选 --- -#}
        {%- if item.REMARKTYPE == 'DSCP' -%}
            DSCP={{item.DSCP}},
        {%- endif -%}
        {#- --- 条件必选：REMARKTYPE=TOS 时必选 --- -#}
        {%- if item.REMARKTYPE == 'TOS' -%}
            TOSVALUE={{item.TOSVALUE}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_5gc -%}
    {%- for item in add_prer8remark_list_2 -%}
        ADD PRER8REMARK:
        {#- --- 必选参数 --- -#}
        QOSPROFILENAME="{{item.QOSPROFILENAME}}",
        SERVICELEVEL={{item.SERVICELEVEL}},
        USERPRIORITY={{item.USERPRIORITY}},
        REMARKTYPE={{item.REMARKTYPE}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：REMARKTYPE=DSCP 时必选 --- -#}
        {%- if item.REMARKTYPE == 'DSCP' -%}
            DSCP={{item.DSCP}},
        {%- endif -%}
        {#- --- 条件必选：DSCP=AF 时必选 --- -#}
        {%- if item.DSCP == 'AF' -%}
            AFCLASS={{item.AFCLASS}},
        {%- endif -%}
        {#- --- 条件必选：DSCP=AF 时必选 --- -#}
        {%- if item.DSCP == 'AF' -%}
            AFDROPPREC={{item.AFDROPPREC}},
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

#### 4.5 配置指定APN实例。

```jinja2
{%- if is_scenario_5gc -%}
    {%- for item in add_apn_list_1 -%}
        ADD APN:
        {#- --- 必选参数 --- -#}
        APN="{{item.APN}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 4.6 为该APN实例绑定QOSPROFILE。

```jinja2
{%- if is_scenario_5gc -%}
    {%- for item in set_apnqosattr_list_1 -%}
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

### 5 配置PreR8 QoS纠错参数。

#### 5.1 进入“MML命令行-UNC”窗口。

#### 5.2 配置PreR8 QoS纠错参数。

```jinja2
{%- for item in set_defprer8qos_list -%}
    SET DEFPRER8QOS:
    {#- --- 可选参数 --- -#}
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
    ;
{%- endfor -%}
```


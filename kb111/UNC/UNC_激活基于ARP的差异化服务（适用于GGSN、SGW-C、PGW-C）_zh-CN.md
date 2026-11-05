---
id: ''
name: 激活基于ARP的差异化服务（适用于GGSN、SGW-C、PGW-C）
ne_type: UNC
type: feature
description: 通过配置差异化服务功能，可实现以下需求：  * 在资源紧缺时，运营商为高优先级用户优先分配资源。 * 在资源相对富余时，更充分地发挥网络资源的效益，提高客户满意度。  适用于GGSN、SGW-C、PGW-C。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","差异化服务管理","WSFD-106303 基于ARP的差异化服务","WSFD-106303 基于ARP的差异化服务（适用于GGSN、SGW-C、PGW-C）","激活基于ARP的差异化服务（适用于GGSN、SGW-C、PGW-C）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
通过配置差异化服务功能，可实现以下需求：* 在资源紧缺时，运营商为高优先级用户优先分配资源。* 在资源相对富余时，更充分地发挥网络资源的效益，提高客户满意度。适用于GGSN、SGW-C、PGW-C。

## 必备事项
前提条件

前提条件

* 请仔细阅读WSFD-106303 基于ARP的差异化服务特性概述（适用于GGSN、SGW-C、PGW-C）。
* 完成加载License。
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
          description: '打开本特性的License配置开关。'
          data_source: '本端规划'
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
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_userpriorarp_list:
      type: items
      properties:
        ROAMHIGHESTARP:
          name: '漫游用户ARP级别限制'
          type: string
          enum:
          - LOW
          - NORMAL
          - HIGH
          required: false
          description: '配置漫游以及拜访用户的级别限制。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        VISITHIGHESTARP:
          name: '拜访用户ARP级别限制'
          type: string
          enum:
          - LOW
          - NORMAL
          - HIGH
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        ROAMARPSWITCH:
          name: '漫游用户级别限制开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        VISITARPSWITCH:
          name: '拜访用户级别限制开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '本端规划'
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
          description: '基于带宽的接入优先级。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_bandwidtharp_list:
      type: items
      properties:
        QOSPROFILENAME:
          name: 'QoS Profile名'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        USERPRIORITY:
          name: '用户级别'
          type: string
          enum:
          - HIGH
          - NORMAL
          - LOW
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        SERVICELEVEL:
          name: '业务级别'
          type: string
          enum:
          - GENERAL
          - CONVERSATIONAL
          - STM_GBR_MORE25K
          - STM_GBR_LESS25K
          - INT_TC_PRI1
          - INT_TC_PRI2
          - INT_TC_PRI3
          - BACKGROUND
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        REJECTLIMIT:
          name: '拒绝告警门限'
          type: integer
          minimum: 2
          maximum: 100
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        RESTORELIMIT:
          name: '恢复告警门限'
          type: integer
          minimum: 1
          maximum: 99
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_pdpnumberarp_list:
      type: items
      properties:
        QOSPROFILENAME:
          name: 'QoS Profile名'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        USERPRIORITY:
          name: '用户级别'
          type: string
          enum:
          - HIGH
          - NORMAL
          - LOW
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        SERVICELEVEL:
          name: '业务级别'
          type: string
          enum:
          - GENERAL
          - CONVERSATIONAL
          - STM_GBR_MORE25K
          - STM_GBR_LESS25K
          - INT_TC_PRI1
          - INT_TC_PRI2
          - INT_TC_PRI3
          - BACKGROUND
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        REJECTLIMIT:
          name: '拒绝告警门限'
          type: integer
          minimum: 2
          maximum: 100
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        RESTORELIMIT:
          name: '恢复告警门限'
          type: integer
          minimum: 1
          maximum: 99
          required: true
          description: ''
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
          description: '为APN实例绑定qos-profile。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        HASQOSPROFILE:
          name: '有QoS Profile'
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
          name: 'QoS Profile名'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_apnaccessctrl_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '设置APN访问控制策略相关参数信息。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        MAXPDBNUMBER:
          name: '最大PDP数目'
          type: integer
          minimum: 0
          maximum: 16000000
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        MAXBANDWIDTH:
          name: '最大带宽'
          type: integer
          minimum: 0
          maximum: 250000
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV2DIFFSEC01'
      SWITCH: ENABLE
    set_userpriorarp_list:
    - ROAMHIGHESTARP: LOW
      VISITHIGHESTARP: HIGH
      ROAMARPSWITCH: ENABLE
      VISITARPSWITCH: ENABLE
    add_qosprofile_list:
    - QOSPROFILENAME: 'profilename'
    add_bandwidtharp_list:
    - QOSPROFILENAME: 'profilename'
      USERPRIORITY: NORMAL
      SERVICELEVEL: GENERAL
      REJECTLIMIT: 30
      RESTORELIMIT: 20
    add_pdpnumberarp_list:
    - QOSPROFILENAME: 'profilename'
      USERPRIORITY: HIGH
      SERVICELEVEL: GENERAL
      REJECTLIMIT: 40
      RESTORELIMIT: 30
    set_apnqosattr_list:
    - APN: 'huawei.com'
      HASQOSPROFILE: ENABLE
      QOSPROFILENAME: 'profilename'
    set_apnaccessctrl_list:
    - APN: 'huawei.com'
      MAXPDBNUMBER: 10
      MAXBANDWIDTH: 200
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 打开本特性的License配置开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

### 2 **可选：**配置拜访或漫游用户的级别限制功能，以及限制级别。

```jinja2
{%- if is_optional_visit_roam_arp_level_limit -%}
    {%- for item in set_userpriorarp_list -%}
        SET USERPRIORARP:
        {#- --- 可选参数 --- -#}
        {%- if item.ROAMARPSWITCH is not none -%}
            ROAMARPSWITCH={{item.ROAMARPSWITCH}},
        {%- endif -%}
        {%- if item.VISITARPSWITCH is not none -%}
            VISITARPSWITCH={{item.VISITARPSWITCH}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：ROAMARPSWITCH=ENABLE 时必选 --- -#}
        {%- if item.ROAMARPSWITCH == 'ENABLE' -%}
            ROAMHIGHESTARP={{item.ROAMHIGHESTARP}},
        {%- endif -%}
        {#- --- 条件必选：VISITARPSWITCH=ENABLE 时必选 --- -#}
        {%- if item.VISITARPSWITCH == 'ENABLE' -%}
            VISITHIGHESTARP={{item.VISITHIGHESTARP}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 3 为指定APN配置带宽和PDP数的接入优先级。

#### 3.1 配置QoS Profile名称。

```jinja2
{%- for item in add_qosprofile_list -%}
    ADD QOSPROFILE:
    {#- --- 必选参数 --- -#}
    QOSPROFILENAME="{{item.QOSPROFILENAME}}",
    ;
{%- endfor -%}
```

#### 3.2 为指定APN配置带宽的接入优先级，即为不同的用户、业务级别配置不同的拒绝、恢复告警门限。

```jinja2
{%- for item in add_bandwidtharp_list -%}
    ADD BANDWIDTHARP:
    {#- --- 必选参数 --- -#}
    QOSPROFILENAME="{{item.QOSPROFILENAME}}",
    USERPRIORITY={{item.USERPRIORITY}},
    SERVICELEVEL={{item.SERVICELEVEL}},
    REJECTLIMIT={{item.REJECTLIMIT}},
    RESTORELIMIT={{item.RESTORELIMIT}},
    ;
{%- endfor -%}
```

#### 3.3 为指定APN配置PDP数的接入优先级，即为不同的用户、业务级别配置不同的拒绝、恢复告警门限。

```jinja2
{%- for item in add_pdpnumberarp_list -%}
    ADD PDPNUMBERARP:
    {#- --- 必选参数 --- -#}
    QOSPROFILENAME="{{item.QOSPROFILENAME}}",
    USERPRIORITY={{item.USERPRIORITY}},
    SERVICELEVEL={{item.SERVICELEVEL}},
    REJECTLIMIT={{item.REJECTLIMIT}},
    RESTORELIMIT={{item.RESTORELIMIT}},
    ;
{%- endfor -%}
```

#### 3.4 为APN实例绑定qos-profile。

```jinja2
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
```

#### 3.5 设置APN访问控制策略相关参数信息。

```jinja2
{%- for item in set_apnaccessctrl_list -%}
    SET APNACCESSCTRL:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    {#- --- 可选参数 --- -#}
    {%- if item.MAXPDBNUMBER is not none -%}
        MAXPDBNUMBER={{item.MAXPDBNUMBER}},
    {%- endif -%}
    {%- if item.MAXBANDWIDTH is not none -%}
        MAXBANDWIDTH={{item.MAXBANDWIDTH}},
    {%- endif -%}
    ;
{%- endfor -%}
```


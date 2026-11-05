---
id: ''
name: 激活NB-IoT UE状态上报功能
ne_type: UNC
type: feature
description: 本操作指导介绍在运行网络中激活NB-IoT UE状态上报功能的操作过程。  适用于MME。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","NB-IOT业务功能","WSFD-011603 NB-IoT UE状态上报功能","激活NB-IoT UE状态上报功能"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本操作指导介绍在运行网络中激活NB-IoT UE状态上报功能的操作过程。适用于MME。

## 必备事项
前提条件

* 操作人员已经登录U2020\MAE-Access。
* eNodeB的订阅已经具备，具体请参见该特性页面的应用场景部分描述。
* 已经加载支持该特性的License，对应的License项为“82208412 LKV2USRF01 NB-IoT UE状态上报功能”。
* 请仔细阅读WSFD-011603 NB-IoT UE状态上报功能特性概述。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    set_dmcmpt_list:
      type: items
      properties:
        SF2:
          name: '特性列表2'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        NBIOTSTAT:
          name: '支持上报的状态列表'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        T6SF:
          name: 'T6A接口特性列表'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_dmcmptbyimsi_list:
      type: items
      properties:
        SUBRANGE:
          name: '用户范围'
          type: string
          enum:
          - FOREIGN_USER
          - HOME_USER
          - IMSI_PREFIX
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NOID:
          name: '运营商标识'
          type: integer
          minimum:
          - 0
          - 128
          maximum:
          - 64
          - 254
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SF2:
          name: '特性列表2'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NBIOTSTAT:
          name: '支持上报的状态列表'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        T6SF:
          name: 'T6A接口特性列表'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IMSIPRE:
          name: 'IMSI前缀'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_dmcmptbyimsi_list_2:
      type: items
      properties:
        SUBRANGE:
          name: '用户范围'
          type: string
          enum:
          - FOREIGN_USER
          - HOME_USER
          - IMSI_PREFIX
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NOID:
          name: '运营商标识'
          type: integer
          minimum:
          - 0
          - 128
          maximum:
          - 64
          - 254
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SF2:
          name: '特性列表2'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NBIOTSTAT:
          name: '支持上报的状态列表'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        T6SF:
          name: 'T6A接口特性列表'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IMSIPRE:
          name: 'IMSI前缀'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_dmcmptbyimsi_list_3:
      type: items
      properties:
        SUBRANGE:
          name: '用户范围'
          type: string
          enum:
          - FOREIGN_USER
          - HOME_USER
          - IMSI_PREFIX
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        IMSIPRE:
          name: 'IMSI前缀'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SF2:
          name: '特性列表2'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NBIOTSTAT:
          name: '支持上报的状态列表'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        T6SF:
          name: 'T6A接口特性列表'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NOID:
          name: '运营商标识'
          type: integer
          minimum:
          - 0
          - 128
          maximum:
          - 64
          - 254
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_mmecharact_list:
      type: items
      properties:
        RANGE:
          name: '对端设备范围'
          type: string
          enum:
          - ALL_MME
          - COMB_AMF
          - SPECIAL_MME
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPTYPE:
          name: 'IP地址类型'
          type: string
          enum:
          - IPV4
          - IPV6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV4:
          name: 'MME IPv4信令面地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MASKV4:
          name: 'IPv4掩码'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MNTREVTINFO:
          name: 'NB-IoT状态上报订阅信息'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NO
        IPV6:
          name: 'MME IPv6信令面地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MASKV6:
          name: 'IPv6子网前缀长度'
          type: integer
          minimum: 1
          maximum: 128
          required: false
          description: ''
          data_source: ''
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
    set_dmcmpt_list:
    - SF2: FLSTID2_BIT19-1
      NBIOTSTAT: UEREACH-1&UELOC-1&UELOSTCONN-1&AVAILAFTDDNFAIL-1
      T6SF: T6FLID_BIT0-1
    add_dmcmptbyimsi_list:
    - SUBRANGE: HOME\_USER
      NOID: 运营商标识
      SF2: FLSTID2_BIT19-1
      NBIOTSTAT: UEREACH-1&UELOC-1&UELOSTCONN-1&AVAILAFTDDNFAIL-1
      T6SF: T6FLID_BIT0-1
      IMSIPRE: '123123'
    add_dmcmptbyimsi_list_2:
    - SUBRANGE: FOREIGN\_USER
      NOID: 运营商标识
      SF2: FLSTID2_BIT19-1
      NBIOTSTAT: UEREACH-1&UELOC-1&UELOSTCONN-1&AVAILAFTDDNFAIL-1
      T6SF: T6FLID_BIT0-1
      IMSIPRE: '123123'
    add_dmcmptbyimsi_list_3:
    - SUBRANGE: IMSI\_PREFIX
      IMSIPRE: '123123'
      SF2: FLSTID2_BIT19-1
      NBIOTSTAT: UEREACH-1&UELOC-1&UELOSTCONN-1&AVAILAFTDDNFAIL-1
      T6SF: T6FLID_BIT0-1
      NOID: ''
    add_mmecharact_list:
    - RANGE: SPECIAL_MME
      IPTYPE: '123033601'
      IPV4: 'ON'
      MASKV4: 'YES'
      MNTREVTINFO: YES
      IPV6: ''
      MASKV6: ''
    set_licenseswitch_list:
    - LICITEM: 'LKV2USRF01'
      SWITCH: ENABLE
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 配置支持NB-IoT UE状态上报功能特性。

#### 1.1 查询系统中Diameter兼容性配置

#### 命令**ADD DMCMPTBYIMSI**与**SET DMCMPT**中除“用户范围”、“运营商标识”以及“IMSI前缀”外的其余参数功能均相同，且若系统中同时存在这两条命令的配置，系统会优先匹配命令**ADD DMCMPTBYIMSI**的配置。因此在配置**ADD DMCMPTBYIMSI**前需先执行**LST DMCMPT**查询系统中**SET DMCMPT**的配置记录，确保命令**ADD DMCMPTBYIMSI**的配置记录中所携带的参数默认值不影响系统已有配置。

#### 1.2 根据HSS是否支持本特性，配置NB-IoT UE状态上报功能的兼容性。

##### 1.2.1 所有HSS都支持此特性：

```jinja2
{%- if is_scenario_all_hss_support -%}
    {%- for item in set_dmcmpt_list -%}
        SET DMCMPT:
        {#- --- 可选参数 --- -#}
        {%- if item.SF2 is not none -%}
            SF2={{item.SF2}},
        {%- endif -%}
        {%- if item.NBIOTSTAT is not none -%}
            NBIOTSTAT={{item.NBIOTSTAT}},
        {%- endif -%}
        {%- if item.T6SF is not none -%}
            T6SF={{item.T6SF}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 1.2.2 本网所有的HSS支持此特性，外网所有HSS不支持此特性：

```jinja2
{%- if is_scenario_home_hss_support -%}
    {%- for item in add_dmcmptbyimsi_list -%}
        ADD DMCMPTBYIMSI:
        {#- --- 必选参数 --- -#}
        SUBRANGE={{item.SUBRANGE}},
        {#- --- 可选参数 --- -#}
        {%- if item.SF2 is not none -%}
            SF2={{item.SF2}},
        {%- endif -%}
        {%- if item.NBIOTSTAT is not none -%}
            NBIOTSTAT={{item.NBIOTSTAT}},
        {%- endif -%}
        {%- if item.T6SF is not none -%}
            T6SF={{item.T6SF}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：SUBRANGE=FOREIGN_USER/HOME_USER 时必选 --- -#}
        {%- if item.SUBRANGE in ['FOREIGN_USER', 'HOME_USER'] -%}
            NOID={{item.NOID}},
        {%- endif -%}
        {#- --- 条件必选：SUBRANGE=IMSI_PREFIX 时必选 --- -#}
        {%- if item.SUBRANGE == 'IMSI_PREFIX' -%}
            IMSIPRE="{{item.IMSIPRE}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 1.2.3 本网所有的HSS不支持此特性，外网所有HSS支持此特性：

```jinja2
{%- if is_scenario_foreign_hss_support -%}
    {%- for item in add_dmcmptbyimsi_list_2 -%}
        ADD DMCMPTBYIMSI:
        {#- --- 必选参数 --- -#}
        SUBRANGE={{item.SUBRANGE}},
        {#- --- 可选参数 --- -#}
        {%- if item.SF2 is not none -%}
            SF2={{item.SF2}},
        {%- endif -%}
        {%- if item.NBIOTSTAT is not none -%}
            NBIOTSTAT={{item.NBIOTSTAT}},
        {%- endif -%}
        {%- if item.T6SF is not none -%}
            T6SF={{item.T6SF}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：SUBRANGE=FOREIGN_USER/HOME_USER 时必选 --- -#}
        {%- if item.SUBRANGE in ['FOREIGN_USER', 'HOME_USER'] -%}
            NOID={{item.NOID}},
        {%- endif -%}
        {#- --- 条件必选：SUBRANGE=IMSI_PREFIX 时必选 --- -#}
        {%- if item.SUBRANGE == 'IMSI_PREFIX' -%}
            IMSIPRE="{{item.IMSIPRE}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 1.2.4 特定IMSI前缀的用户注册的HSS支持此特性：

```jinja2
{%- if is_scenario_imsi_prefix_support -%}
    {%- for item in add_dmcmptbyimsi_list_3 -%}
        ADD DMCMPTBYIMSI:
        {#- --- 必选参数 --- -#}
        SUBRANGE={{item.SUBRANGE}},
        {#- --- 可选参数 --- -#}
        {%- if item.SF2 is not none -%}
            SF2={{item.SF2}},
        {%- endif -%}
        {%- if item.NBIOTSTAT is not none -%}
            NBIOTSTAT={{item.NBIOTSTAT}},
        {%- endif -%}
        {%- if item.T6SF is not none -%}
            T6SF={{item.T6SF}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：SUBRANGE=IMSI_PREFIX 时必选 --- -#}
        {%- if item.SUBRANGE == 'IMSI_PREFIX' -%}
            IMSIPRE="{{item.IMSIPRE}}",
        {%- endif -%}
        {#- --- 条件必选：SUBRANGE=FOREIGN_USER/HOME_USER 时必选 --- -#}
        {%- if item.SUBRANGE in ['FOREIGN_USER', 'HOME_USER'] -%}
            NOID={{item.NOID}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 2 （可选）若对端MME支持NB-IoT能力开放订阅信息信元传递，需要配置对端MME的属性信息。

```jinja2
{%- if is_optional_peer_mme_attribute -%}
    {%- for item in add_mmecharact_list -%}
        ADD MMECHARACT:
        {#- --- 必选参数 --- -#}
        RANGE={{item.RANGE}},
        {#- --- 可选参数 --- -#}
        {%- if item.MNTREVTINFO is not none -%}
            MNTREVTINFO={{item.MNTREVTINFO}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：RANGE=SPECIAL_MME 时必选 --- -#}
        {%- if item.RANGE == 'SPECIAL_MME' -%}
            IPTYPE={{item.IPTYPE}},
        {%- endif -%}
        {#- --- 条件必选：IPTYPE=IPV4 时必选 --- -#}
        {%- if item.IPTYPE == 'IPV4' -%}
            IPV4="{{item.IPV4}}",
        {%- endif -%}
        {#- --- 条件必选：IPTYPE=IPV4 时必选 --- -#}
        {%- if item.IPTYPE == 'IPV4' -%}
            MASKV4="{{item.MASKV4}}",
        {%- endif -%}
        {#- --- 条件必选：IPTYPE=IPV6 时必选 --- -#}
        {%- if item.IPTYPE == 'IPV6' -%}
            IPV6="{{item.IPV6}}",
        {%- endif -%}
        {#- --- 条件必选：IPTYPE=IPV6 时必选 --- -#}
        {%- if item.IPTYPE == 'IPV6' -%}
            MASKV6={{item.MASKV6}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 3 打开本功能的License配置开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```


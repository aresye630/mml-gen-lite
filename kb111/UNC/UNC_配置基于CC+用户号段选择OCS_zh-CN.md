---
id: ''
name: 配置基于CC+用户号段选择OCS
ne_type: UNC
type: feature
description: OCS的选择满足以下要求：  1. 基于计费属性CC（Charge Characteristics）区分Postpaid和Prepaid用户。 2. 基于用户号段进行OCS的选择。  适用于GGSN、PGW-C。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","计费管理功能","WSFD-109001 Gy/Diameter在线计费","激活Gy/Diameter在线计费","配置OCS组网可靠性配置实例","配置基于CC+用户号段选择OCS"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
OCS的选择满足以下要求：1. 基于计费属性CC（Charge Characteristics）区分Postpaid和Prepaid用户。2. 基于用户号段进行OCS的选择。适用于GGSN、PGW-C。

## 必备事项
前提条件

* 请仔细阅读Ga/Gy接口离线/在线计费。
* 完成配置到OCS的数据(静态路由+BFD组网)。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    add_diamlocinfo_list:
      type: items
      properties:
        HOSTNAME:
          name: '本端主机名'
          type: string
          maxLength: 127
          required: true
          description: 'GGSN/PGW-C信息。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        REALMNAME:
          name: '本端域名'
          type: string
          maxLength: 127
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        PRODUCTNAME:
          name: '产品名称'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_ocs_list:
      type: items
      properties:
        OCSHOSTNAME:
          name: 'Ocs主机名称'
          type: string
          maxLength: 127
          required: true
          description: '配置OCS。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        REALMNAME:
          name: 'Ocs域名'
          type: string
          maxLength: 127
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_diampeeraddr_list:
      type: items
      properties:
        HOSTNAME:
          name: '主机名称'
          type: string
          maxLength: 127
          required: true
          description: 'OCS信息。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        ADDRTYPE:
          name: '地址类型'
          type: string
          enum:
          - IPv4
          - IPv6
          - SCTP
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPV4ADDRESS:
          name: 'IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        PORT:
          name: '端口号'
          type: integer
          minimum: 1
          maximum: 65534
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: 3868
        IPV6ADDRESS:
          name: 'IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SCTPENDPOINT:
          name: 'SCTP端点名称'
          type: string
          maxLength: 63
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_imsimsisdnseg_list:
      type: items
      properties:
        SEGMENTNAME:
          name: 'IMSI/MSISDN号段名称'
          type: string
          maxLength: 31
          required: true
          description: '配置MSISDN号码段。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SEGMENTTYPE:
          name: 'IMSI/MSISDN号段类型'
          type: string
          enum:
          - IMSI
          - IMSIWILDCARD
          - MSISDN
          - MSISDNWILDCARD
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        SEGSTART:
          name: '号段起始字符串'
          type: string
          maxLength: 17
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        SEGEND:
          name: '号段结束字符串'
          type: string
          maxLength: 17
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        WILDCARDSEG:
          name: '通配号段字符串'
          type: string
          maxLength: 47
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_subscriberidseggrp_list:
      type: items
      properties:
        SEGGROUPNAME:
          name: 'IMSI/MSISDN/IMEISV号段组名称'
          type: string
          maxLength: 31
          required: true
          description: '配置IMSIMSISDN号码段组。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SEGMENTNAME:
          name: 'IMSI/MSISDN/IMEISV号段名称'
          type: string
          maxLength: 31
          required: true
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        SEGMENTTYPE:
          name: '号段类型'
          type: string
          enum:
          - IMEISV
          - IMSIMSISDN
          required: true
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_ocsgroup_list:
      type: items
      properties:
        OCSGRPNAME:
          name: 'Ocs组名称'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_ocsbinding_list:
      type: items
      properties:
        OCSGRPNAME:
          name: 'Ocs组名称'
          type: string
          maxLength: 63
          required: true
          description: '增加OCS绑定关系。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        OCSHOSTNAME:
          name: 'Ocs主机名称'
          type: string
          maxLength: 127
          required: true
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        SEGGROUPNAME:
          name: 'IMSI/MSISDN号码段组名称'
          type: string
          maxLength: 31
          required: false
          description: 'OCS组绑定IMSI/MSISDN号段。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        IMSIPRIORITY:
          name: 'IMSI/MSISDN号码段组优先级'
          type: integer
          minimum: 1
          maximum: 65535
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_dcctemplate_list:
      type: items
      properties:
        DCCTMPLTNAME:
          name: 'DCC模板名称'
          type: string
          maxLength: 63
          required: true
          description: '主从OCS组。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PRIOCSGRPNAME:
          name: '主OCS组名称'
          type: string
          maxLength: 63
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        SECOCSGRPNAME:
          name: '备OCS组名称'
          type: string
          maxLength: 63
          required: false
          description: ''
          data_source: '已配置数据中获取'
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
          description: '虚拟APN。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        VIRTUALAPN:
          name: '虚拟APN'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: DISABLE
        RESTORPGWSWITCH:
          name: '故障重启业务恢复功能PGW开关'
          type: string
          enum:
          - ENABLE
          - INHERIT
          - DISABLE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: INHERIT
        PDTNSWITCH:
          name: 'PDTN功能开关'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
    add_virtualapnrule_list:
      type: items
      properties:
        VIRTUALAPN:
          name: '虚拟APN名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        MAPPINGTYPE:
          name: '映射方式'
          type: string
          enum:
          - IMSI
          - MSISDN
          - RAT
          - PCO
          - RADIUS
          - LOAD_BALANCE
          - CHARGE_CHAR
          - REDUNDANCY
          - VDEFAULT_APN
          - IMEI
          - LAC_GROUP
          - TAC_GROUP
          - RAC_GROUP
          - PLMN
          - SERVING_GROUP
          - ROAMING
          - MULTIPARA
          - SELECTION_MODE
          - NS
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        CCMODE:
          name: '计费属性模式'
          type: string
          enum:
          - Normal
          - Hotbilling
          - Prepaid
          - FlatBilling
          - Specific
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        REALAPN:
          name: '真实APN名称'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        REALAPNSWITCH:
          name: '真实APN开关'
          type: string
          enum:
          - Disable
          - Enable
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CCMASKPRIORITY:
          name: '计费特征掩码和优先级开关'
          type: string
          enum:
          - Disable
          - Enable
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CCVALUE:
          name: '计费属性值'
          type: string
          minLength: 4
          maxLength: 6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IMEI:
          name: 'IMEI'
          type: string
          minLength: 1
          maxLength: 16
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IMSI:
          name: 'IMSI'
          type: string
          minLength: 1
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LACGROUP:
          name: 'LAC组名'
          type: string
          minLength: 0
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MAPPINGVALUE:
          name: '映射值'
          type: string
          minLength: 0
          maxLength: 95
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MSISDN:
          name: 'MSISDN'
          type: string
          minLength: 1
          maxLength: 17
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PCOSWITCH:
          name: 'PCO开关'
          type: string
          enum:
          - Disable
          - Enable
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PLMN:
          name: 'PLMN'
          type: string
          minLength: 5
          maxLength: 6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PRIORITY:
          name: '优先级'
          type: integer
          minimum: 1
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RACGROUP:
          name: 'RAC组名'
          type: string
          minLength: 0
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RATTYPE:
          name: '无线接入类型'
          type: string
          enum:
          - Utran
          - Geran
          - Wlan
          - Gan
          - Eutran
          - EutranNbIoT
          - Ngran
          - Redcap
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ROAMING:
          name: '漫游状态'
          type: string
          enum:
          - Home
          - Roaming
          - Visiting
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SD:
          name: '切片细分标识'
          type: string
          minLength: 6
          maxLength: 6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SELECTIONMODE:
          name: '选择模式'
          type: string
          enum:
          - MsNetProApn
          - MsProApn
          - NetProApn
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SRVNODEGROUP:
          name: 'Serving Node组名称'
          type: string
          minLength: 0
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SST:
          name: '切片业务类型'
          type: integer
          minimum: 0
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TACGROUP:
          name: 'TAC组名'
          type: string
          minLength: 0
          maxLength: 32
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
          description: '配置APN，可以使用命令**LST APN**查询。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        RESTORPGWSWITCH:
          name: '故障重启业务恢复功能PGW开关'
          type: string
          enum:
          - ENABLE
          - INHERIT
          - DISABLE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: INHERIT
        PDTNSWITCH:
          name: 'PDTN功能开关'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
    set_apnchargectrl_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          maxLength: 63
          required: true
          description: 'APN实例绑定DCC Template模板。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        DCCTEMPLATE:
          name: 'DCC模板名称'
          type: string
          maxLength: 63
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
  examples:
    add_diamlocinfo_list:
    - HOSTNAME: 'pgw1'
      REALMNAME: 'huawei.com'
      PRODUCTNAME: 'unc@huawei.com'
    add_ocs_list:
    - OCSHOSTNAME: 'ocs_host1'
      REALMNAME: 'ocs_realm'
    add_diampeeraddr_list:
    - HOSTNAME: 'ocs_host1'
      ADDRTYPE: IPv4
      IPV4ADDRESS: '192.168.40.10'
      PORT: 3868
      IPV6ADDRESS: ''
      SCTPENDPOINT: ''
    add_imsimsisdnseg_list:
    - SEGMENTNAME: 'testmsisdn1'
      SEGMENTTYPE: MSISDN
      SEGSTART: '13900100100'
      SEGEND: '13900100199'
      WILDCARDSEG: ''
    add_subscriberidseggrp_list:
    - SEGGROUPNAME: 'testmsisdngr1'
      SEGMENTNAME: 'testmsisdn1'
      SEGMENTTYPE: IMSIMSISDN
    add_ocsgroup_list:
    - OCSGRPNAME: 'ocs-gra'
    add_ocsbinding_list:
    - OCSGRPNAME: 'ocs-gra'
      OCSHOSTNAME: 'ocs_host1'
      SEGGROUPNAME: 'testmsisdngr1'
      IMSIPRIORITY: 30
    add_dcctemplate_list:
    - DCCTMPLTNAME: 'dcctemp01'
      PRIOCSGRPNAME: 'ocs-gra'
      SECOCSGRPNAME: 'ocs-grb'
    add_apn_list:
    - APN: 'apn1'
      VIRTUALAPN: ENABLE
      RESTORPGWSWITCH: INHERIT
      PDTNSWITCH: DISABLE
    add_virtualapnrule_list:
    - VIRTUALAPN: 'apn1'
      MAPPINGTYPE: CHARGE_CHAR
      CCMODE: Prepaid
      REALAPN: 'apn2'
      REALAPNSWITCH: ''
      CCMASKPRIORITY: ''
      CCVALUE: ''
      IMEI: ''
      IMSI: ''
      LACGROUP: ''
      MAPPINGVALUE: ''
      MSISDN: ''
      PCOSWITCH: ''
      PLMN: ''
      PRIORITY: ''
      RACGROUP: ''
      RATTYPE: ''
      ROAMING: ''
      SD: ''
      SELECTIONMODE: ''
      SRVNODEGROUP: ''
      SST: ''
      TACGROUP: ''
    add_apn_list_1:
    - APN: 'apn2'
      RESTORPGWSWITCH: INHERIT
      PDTNSWITCH: DISABLE
    set_apnchargectrl_list:
    - APN: 'apn2'
      DCCTEMPLATE: 'dcctemp01'
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 配置在线计费中GGSN/PGW-C的设备标识。

### UNC的Gx应用和Gy应用的本端主机名可以相同，但是同时要求“REALMNAME”参数和“PRODUCTNAME”也必须相同。

```jinja2
{%- for item in add_diamlocinfo_list -%}
    ADD DIAMLOCINFO:
    {#- --- 必选参数 --- -#}
    HOSTNAME="{{item.HOSTNAME}}",
    REALMNAME="{{item.REALMNAME}}",
    PRODUCTNAME="{{item.PRODUCTNAME}}",
    ;
{%- endfor -%}
```

### 2 配置基于用户号段进行OCS负荷分担。

#### 2.1 配置OCS信息。重复执行本步骤可增加多个OCS信息。

```jinja2
{%- for item in add_ocs_list -%}
    ADD OCS:
    {#- --- 必选参数 --- -#}
    OCSHOSTNAME="{{item.OCSHOSTNAME}}",
    REALMNAME="{{item.REALMNAME}}",
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_diampeeraddr_list -%}
    ADD DIAMPEERADDR:
    {#- --- 必选参数 --- -#}
    HOSTNAME="{{item.HOSTNAME}}",
    ADDRTYPE={{item.ADDRTYPE}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：ADDRTYPE=IPv4 时必选 --- -#}
    {%- if item.ADDRTYPE == 'IPv4' -%}
        IPV4ADDRESS="{{item.IPV4ADDRESS}}",
    {%- endif -%}
    {#- --- 条件必选：ADDRTYPE=IPv6 时必选 --- -#}
    {%- if item.ADDRTYPE == 'IPv6' -%}
        IPV6ADDRESS="{{item.IPV6ADDRESS}}",
    {%- endif -%}
    {#- --- 条件必选：ADDRTYPE=SCTP 时必选 --- -#}
    {%- if item.ADDRTYPE == 'SCTP' -%}
        SCTPENDPOINT="{{item.SCTPENDPOINT}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：ADDRTYPE=IPv4/IPv6 时可选 --- -#}
    {%- if item.ADDRTYPE in ['IPv4', 'IPv6'] -%}
        {%- if item.PORT is not none -%}
            PORT={{item.PORT}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 2.2 配置IMSI及MSISDN号码段。

```jinja2
{%- for item in add_imsimsisdnseg_list -%}
    ADD IMSIMSISDNSEG:
    {#- --- 必选参数 --- -#}
    SEGMENTNAME="{{item.SEGMENTNAME}}",
    SEGMENTTYPE={{item.SEGMENTTYPE}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：SEGMENTTYPE=IMSI/MSISDN 时必选 --- -#}
    {%- if item.SEGMENTTYPE in ['IMSI', 'MSISDN'] -%}
        SEGSTART="{{item.SEGSTART}}",
    {%- endif -%}
    {#- --- 条件必选：SEGMENTTYPE=IMSI/MSISDN 时必选 --- -#}
    {%- if item.SEGMENTTYPE in ['IMSI', 'MSISDN'] -%}
        SEGEND="{{item.SEGEND}}",
    {%- endif -%}
    {#- --- 条件必选：SEGMENTTYPE=IMSIWILDCARD/MSISDNWILDCARD 时必选 --- -#}
    {%- if item.SEGMENTTYPE in ['IMSIWILDCARD', 'MSISDNWILDCARD'] -%}
        WILDCARDSEG="{{item.WILDCARDSEG}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 2.3 配置IMSI及MSISDN号码段组。

```jinja2
{%- for item in add_subscriberidseggrp_list -%}
    ADD SUBSCRIBERIDSEGGRP:
    {#- --- 必选参数 --- -#}
    SEGGROUPNAME="{{item.SEGGROUPNAME}}",
    SEGMENTNAME="{{item.SEGMENTNAME}}",
    SEGMENTTYPE={{item.SEGMENTTYPE}},
    ;
{%- endfor -%}
```

#### 2.4 配置OCS组。

```jinja2
{%- for item in add_ocsgroup_list -%}
    ADD OCSGROUP:
    {#- --- 必选参数 --- -#}
    OCSGRPNAME="{{item.OCSGRPNAME}}",
    ;
{%- endfor -%}
```

#### 2.5 配置基于用户号段IMSI/MSISDN选择在线计费系统的OCS。

```jinja2
{%- for item in add_ocsbinding_list -%}
    ADD OCSBINDING:
    {#- --- 必选参数 --- -#}
    OCSGRPNAME="{{item.OCSGRPNAME}}",
    OCSHOSTNAME="{{item.OCSHOSTNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.SEGGROUPNAME is not none -%}
        SEGGROUPNAME="{{item.SEGGROUPNAME}}",
    {%- endif -%}
    {%- if item.IMSIPRIORITY is not none -%}
        IMSIPRIORITY={{item.IMSIPRIORITY}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 配置主从OCS组。

```jinja2
{%- for item in add_dcctemplate_list -%}
    ADD DCCTEMPLATE:
    {#- --- 必选参数 --- -#}
    DCCTMPLTNAME="{{item.DCCTMPLTNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.PRIOCSGRPNAME is not none -%}
        PRIOCSGRPNAME="{{item.PRIOCSGRPNAME}}",
    {%- endif -%}
    {%- if item.SECOCSGRPNAME is not none -%}
        SECOCSGRPNAME="{{item.SECOCSGRPNAME}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 配置虚拟APN。

#### 4.1 使能虚拟APN功能。

```jinja2
{%- for item in add_apn_list -%}
    ADD APN:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    {#- --- 可选参数 --- -#}
    {%- if item.VIRTUALAPN is not none -%}
        VIRTUALAPN={{item.VIRTUALAPN}},
    {%- endif -%}
    {%- if item.RESTORPGWSWITCH is not none -%}
        RESTORPGWSWITCH={{item.RESTORPGWSWITCH}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：RESTORPGWSWITCH=ENABLE 时可选 --- -#}
    {%- if item.RESTORPGWSWITCH == 'ENABLE' -%}
        {%- if item.PDTNSWITCH is not none -%}
            PDTNSWITCH={{item.PDTNSWITCH}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 4.2 配置虚拟APN映射规则。

```jinja2
{%- for item in add_virtualapnrule_list -%}
    ADD VIRTUALAPNRULE:
    {#- --- 必选参数 --- -#}
    VIRTUALAPN="{{item.VIRTUALAPN}}",
    MAPPINGTYPE={{item.MAPPINGTYPE}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：MAPPINGTYPE=CHARGE_CHAR/IMSI/IMEI/MSISDN/LAC_GROUP/TAC_GROUP/RAC_GROUP/PLMN/SERVING_GROUP/SELECTION_MODE/MULTIPARA/RAT/LOAD_BALANCE/ROAMING/REDUNDANCY/VDEFAULT_APN/NS 时必选 --- -#}
    {%- if item.MAPPINGTYPE in ['CHARGE_CHAR', 'IMSI', 'IMEI', 'MSISDN', 'LAC_GROUP', 'TAC_GROUP', 'RAC_GROUP', 'PLMN', 'SERVING_GROUP', 'SELECTION_MODE', 'MULTIPARA', 'RAT', 'LOAD_BALANCE', 'ROAMING', 'REDUNDANCY', 'VDEFAULT_APN', 'NS'] -%}
        REALAPN="{{item.REALAPN}}",
    {#- --- 条件必选：REALAPNSWITCH=Enable 时必选 --- -#}
    {%- elif item.REALAPNSWITCH == 'Enable' -%}
        REALAPN="{{item.REALAPN}}",
    {%- endif -%}
    {#- --- 条件必选：CCMODE=Specific 时必选 --- -#}
    {%- if item.CCMODE == 'Specific' -%}
        CCMASKPRIORITY={{item.CCMASKPRIORITY}},
    {%- endif -%}
    {#- --- 条件必选：CCMODE=Specific 时必选 --- -#}
    {%- if item.CCMODE == 'Specific' -%}
        CCVALUE="{{item.CCVALUE}}",
    {%- endif -%}
    {#- --- 条件必选：MAPPINGTYPE=IMSI/IMEI/MSISDN/LAC_GROUP/TAC_GROUP/RAC_GROUP/PLMN/SERVING_GROUP 时必选 --- -#}
    {%- if item.MAPPINGTYPE in ['IMSI', 'IMEI', 'MSISDN', 'LAC_GROUP', 'TAC_GROUP', 'RAC_GROUP', 'PLMN', 'SERVING_GROUP'] -%}
        MAPPINGVALUE="{{item.MAPPINGVALUE}}",
    {%- endif -%}
    {#- --- 条件必选：MAPPINGTYPE=PCO 时必选 --- -#}
    {%- if item.MAPPINGTYPE == 'PCO' -%}
        REALAPNSWITCH={{item.REALAPNSWITCH}},
    {%- endif -%}
    {#- --- 条件必选：MAPPINGTYPE=NS 时必选 --- -#}
    {%- if item.MAPPINGTYPE == 'NS' -%}
        SST={{item.SST}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：MAPPINGTYPE=MULTIPARA 时可选 --- -#}
    {%- if item.MAPPINGTYPE == 'MULTIPARA' -%}
        {%- if item.IMEI is not none -%}
            IMEI="{{item.IMEI}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：MAPPINGTYPE=MULTIPARA 时可选 --- -#}
    {%- if item.MAPPINGTYPE == 'MULTIPARA' -%}
        {%- if item.IMSI is not none -%}
            IMSI="{{item.IMSI}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：MAPPINGTYPE=MULTIPARA 时可选 --- -#}
    {%- if item.MAPPINGTYPE == 'MULTIPARA' -%}
        {%- if item.LACGROUP is not none -%}
            LACGROUP="{{item.LACGROUP}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：MAPPINGTYPE=MULTIPARA 时可选 --- -#}
    {%- if item.MAPPINGTYPE == 'MULTIPARA' -%}
        {%- if item.MSISDN is not none -%}
            MSISDN="{{item.MSISDN}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：MAPPINGTYPE=MULTIPARA 时可选 --- -#}
    {%- if item.MAPPINGTYPE == 'MULTIPARA' -%}
        {%- if item.PCOSWITCH is not none -%}
            PCOSWITCH={{item.PCOSWITCH}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：MAPPINGTYPE=MULTIPARA 时可选 --- -#}
    {%- if item.MAPPINGTYPE == 'MULTIPARA' -%}
        {%- if item.PLMN is not none -%}
            PLMN="{{item.PLMN}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：MAPPINGTYPE=MULTIPARA 时可选 --- -#}
    {%- if item.MAPPINGTYPE == 'MULTIPARA' -%}
        {%- if item.RACGROUP is not none -%}
            RACGROUP="{{item.RACGROUP}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：MAPPINGTYPE=NS 时可选 --- -#}
    {%- if item.MAPPINGTYPE == 'NS' -%}
        {%- if item.SD is not none -%}
            SD="{{item.SD}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：MAPPINGTYPE=MULTIPARA 时可选 --- -#}
    {%- if item.MAPPINGTYPE == 'MULTIPARA' -%}
        {%- if item.SRVNODEGROUP is not none -%}
            SRVNODEGROUP="{{item.SRVNODEGROUP}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：MAPPINGTYPE=MULTIPARA 时可选 --- -#}
    {%- if item.MAPPINGTYPE == 'MULTIPARA' -%}
        {%- if item.TACGROUP is not none -%}
            TACGROUP="{{item.TACGROUP}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件必选/可选参数 --- -#}
    {#- --- 计费属性模式: 条件必选(映射方式=CHARGE_CHAR) / 条件可选(映射方式=MULTIPARA) --- -#}
    {%- if (item.MAPPINGTYPE == 'CHARGE_CHAR') -%}
        CCMODE={{item.CCMODE}},
    {%- elif (item.MAPPINGTYPE == 'MULTIPARA') -%}
        {%- if item.CCMODE is not none -%}
            CCMODE={{item.CCMODE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 优先级: 条件必选(映射方式=MULTIPARA) / 条件可选(映射方式=RADIUS|CHARGE_CHAR|IMSI|IMEI|MSISDN|LAC_GROUP|TAC_GROUP|RAC_GROUP|PLMN|SERVING_GROUP|PCO|SELECTION_MODE|RAT|LOAD_BALANCE|ROAMING|REDUNDANCY) --- -#}
    {%- if (item.MAPPINGTYPE == 'MULTIPARA') -%}
        PRIORITY={{item.PRIORITY}},
    {%- elif (item.MAPPINGTYPE in ['RADIUS', 'CHARGE_CHAR', 'IMSI', 'IMEI', 'MSISDN', 'LAC_GROUP', 'TAC_GROUP', 'RAC_GROUP', 'PLMN', 'SERVING_GROUP', 'PCO', 'SELECTION_MODE', 'RAT', 'LOAD_BALANCE', 'ROAMING', 'REDUNDANCY']) -%}
        {%- if item.PRIORITY is not none -%}
            PRIORITY={{item.PRIORITY}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 无线接入类型: 条件必选(映射方式=RAT) / 条件可选(映射方式=MULTIPARA) --- -#}
    {%- if (item.MAPPINGTYPE == 'RAT') -%}
        RATTYPE={{item.RATTYPE}},
    {%- elif (item.MAPPINGTYPE == 'MULTIPARA') -%}
        {%- if item.RATTYPE is not none -%}
            RATTYPE={{item.RATTYPE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 漫游状态: 条件必选(映射方式=ROAMING) / 条件可选(映射方式=MULTIPARA) --- -#}
    {%- if (item.MAPPINGTYPE == 'ROAMING') -%}
        ROAMING={{item.ROAMING}},
    {%- elif (item.MAPPINGTYPE == 'MULTIPARA') -%}
        {%- if item.ROAMING is not none -%}
            ROAMING={{item.ROAMING}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 选择模式: 条件必选(映射方式=SELECTION_MODE) / 条件可选(映射方式=MULTIPARA) --- -#}
    {%- if (item.MAPPINGTYPE == 'SELECTION_MODE') -%}
        SELECTIONMODE={{item.SELECTIONMODE}},
    {%- elif (item.MAPPINGTYPE == 'MULTIPARA') -%}
        {%- if item.SELECTIONMODE is not none -%}
            SELECTIONMODE={{item.SELECTIONMODE}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 5 配置真实APN。

#### 5.1 配置真实APN实例。

```jinja2
{%- for item in add_apn_list_1 -%}
    ADD APN:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    {#- --- 可选参数 --- -#}
    {%- if item.RESTORPGWSWITCH is not none -%}
        RESTORPGWSWITCH={{item.RESTORPGWSWITCH}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：RESTORPGWSWITCH=ENABLE 时可选 --- -#}
    {%- if item.RESTORPGWSWITCH == 'ENABLE' -%}
        {%- if item.PDTNSWITCH is not none -%}
            PDTNSWITCH={{item.PDTNSWITCH}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 5.2 绑定DCC模板。

```jinja2
{%- for item in set_apnchargectrl_list -%}
    SET APNCHARGECTRL:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    {#- --- 可选参数 --- -#}
    {%- if item.DCCTEMPLATE is not none -%}
        DCCTEMPLATE="{{item.DCCTEMPLATE}}",
    {%- endif -%}
    ;
{%- endfor -%}
```


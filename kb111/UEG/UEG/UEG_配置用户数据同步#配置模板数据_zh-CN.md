---
id: ''
name: 配置模板数据
ne_type: UEG
type: feature
description: 该操作指导工程师在开局阶段，新建UDM网元时，完成4G/5G模板数据的配置。
tags: []
risk_level: ''
doc_source: ["网络部署","园区入驻式（仅连接）","5GC toB 部署边缘站点（站点为“风筝L”，入驻式）","UEG初始配置（风筝L）","参考：详细配置指导","配置UDM/HSS","配置用户数据同步","配置模板数据"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
该操作指导工程师在开局阶段，新建UDM网元时，完成4G/5G模板数据的配置。

## 必备事项
前提条件

具备管理员权限的操作人员已经登录华为操作维护系统（登录MAE客户端或登录OM Portal）。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    add_ngcqostpl_list:
      type: items
      properties:
        HLRSN:
          name: 'HLR序列号'
          type: integer
          minimum: 1
          maximum: 255
          required: true
          description: '与对端（中心UDM）一致。'
          data_source: '从对端获取'
          pattern: ''
          default: ''
        TPLID:
          name: '模板ID'
          type: integer
          minimum: 1
          maximum: 2147483646
          required: true
          description: '存在多条记录时，该参数不能重复。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        TPLNAME:
          name: '模板名'
          type: string
          maxLength: 60
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NGQI:
          name: '5QI'
          type: integer
          minimum: 0
          maximum: 255
          required: true
          description: '与对端（中心UDM）一致。'
          data_source: '从对端获取'
          pattern: ''
          default: ''
        ARPPRILEVEL:
          name: '优先级'
          type: integer
          minimum: 1
          maximum: 15
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PREEMPTIONCAP:
          name: '是否允许抢占低优先级业务的资源'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PREEMPTIONVUL:
          name: '是否允许资源被高优先级业务抢占'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NGQIPRILEVEL:
          name: '5QI优先级'
          type: integer
          minimum: 1
          maximum: 127
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_dnnqostpl_list:
      type: items
      properties:
        HLRSN:
          name: 'HLR序列号'
          type: integer
          minimum: 1
          maximum: 255
          required: true
          description: '与对端（中心UDM）一致。'
          data_source: '从对端获取'
          pattern: ''
          default: ''
        TPLID:
          name: 'QoS模板ID'
          type: integer
          minimum: 1
          maximum: 2147483646
          required: true
          description: '存在多条记录时，该参数不能重复。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        TPLNAME:
          name: 'QoS模板名'
          type: string
          maxLength: 60
          required: false
          description: '存在多条记录时，该参数不能重复。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PDUTYPE:
          name: '默认PDU类型'
          type: string
          enum:
          - IPV4V6
          - IPV4
          - IPV6
          - UNSTR
          - ETHER
          required: true
          description: '与对端（中心UDM）一致。  支持5G LAN以太通信时，允许的PDU类型需包含“ETHER”。'
          data_source: '从对端获取'
          pattern: ''
          default: ''
        ALLOWEDPDUTYPE:
          name: '其它允许的PDU类型'
          type: string
          enum:
          - IPV4V6
          - IPV4
          - IPV6
          - UNSTR
          - ETHER
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SSCMODE:
          name: '默认SSC模式'
          type: string
          enum:
          - SSC_MODE_1
          - SSC_MODE_2
          - SSC_MODE_3
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ALLOWEDSCCMODE:
          name: '其它允许的SSC模式'
          type: string
          enum:
          - SSC_MODE_1
          - SSC_MODE_2
          - SSC_MODE_3
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NGCQOSTPLID:
          name: '5GC QoS模板ID'
          type: integer
          minimum: 1
          maximum: 2147483646
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AMBRUP:
          name: 'DNN级别上行速率'
          type: integer
          minimum: 1
          maximum: 9223372036854775807
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        UPUNIT:
          name: 'DNN级别上行速率单位'
          type: string
          enum:
          - bps
          - Kbps
          - Mbps
          - Gbps
          - Tbps
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AMBRDW:
          name: 'DNN级别下行速率'
          type: integer
          minimum: 1
          maximum: 9223372036854775807
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DWUNIT:
          name: 'DNN级别下行速率单位'
          type: string
          enum:
          - bps
          - Kbps
          - Mbps
          - Gbps
          - Tbps
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CHARGE:
          name: '计费特性'
          type: string
          maxLength: 4
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        UPINTEGR:
          name: '用户面完整性保护策略'
          type: string
          enum:
          - NOT_NEEDED
          - REQUIRED
          - PREFERRED
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        UPCONFID:
          name: '用户面机密性保护策略'
          type: string
          enum:
          - NOT_NEEDED
          - REQUIRED
          - PREFERRED
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_dnnqostpl_list_1:
      type: items
      properties:
        HLRSN:
          name: 'HLR序列号'
          type: integer
          minimum: 1
          maximum: 255
          required: true
          description: '与对端（中心UDM）一致。'
          data_source: '从对端获取'
          pattern: ''
          default: ''
        TPLID:
          name: 'QoS模板ID'
          type: integer
          minimum: 1
          maximum: 2147483646
          required: true
          description: '存在多条记录时，该参数不能重复。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        TPLNAME:
          name: 'QoS模板名'
          type: string
          maxLength: 60
          required: false
          description: '存在多条记录时，该参数不能重复。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PDUTYPE:
          name: '默认PDU类型'
          type: string
          enum:
          - IPV4V6
          - IPV4
          - IPV6
          - UNSTR
          - ETHER
          required: true
          description: '与对端（中心UDM）一致。  支持5G LAN以太通信时，允许的PDU类型需包含“ETHER”。'
          data_source: '从对端获取'
          pattern: ''
          default: ''
        ALLOWEDPDUTYPE:
          name: '其它允许的PDU类型'
          type: string
          enum:
          - IPV4V6
          - IPV4
          - IPV6
          - UNSTR
          - ETHER
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SSCMODE:
          name: '默认SSC模式'
          type: string
          enum:
          - SSC_MODE_1
          - SSC_MODE_2
          - SSC_MODE_3
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ALLOWEDSCCMODE:
          name: '其它允许的SSC模式'
          type: string
          enum:
          - SSC_MODE_1
          - SSC_MODE_2
          - SSC_MODE_3
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NGCQOSTPLID:
          name: '5GC QoS模板ID'
          type: integer
          minimum: 1
          maximum: 2147483646
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AMBRUP:
          name: 'DNN级别上行速率'
          type: integer
          minimum: 1
          maximum: 9223372036854775807
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        UPUNIT:
          name: 'DNN级别上行速率单位'
          type: string
          enum:
          - bps
          - Kbps
          - Mbps
          - Gbps
          - Tbps
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AMBRDW:
          name: 'DNN级别下行速率'
          type: integer
          minimum: 1
          maximum: 9223372036854775807
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DWUNIT:
          name: 'DNN级别下行速率单位'
          type: string
          enum:
          - bps
          - Kbps
          - Mbps
          - Gbps
          - Tbps
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CHARGE:
          name: '计费特性'
          type: string
          maxLength: 4
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        UPINTEGR:
          name: '用户面完整性保护策略'
          type: string
          enum:
          - NOT_NEEDED
          - REQUIRED
          - PREFERRED
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        UPCONFID:
          name: '用户面机密性保护策略'
          type: string
          enum:
          - NOT_NEEDED
          - REQUIRED
          - PREFERRED
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_epsqostpl_list:
      type: items
      properties:
        HLRSN:
          name: 'HLR序列号'
          type: string
          required: false
          description: '与对端（中心UDM）一致。'
          data_source: '从对端获取'
          pattern: ''
          default: ''
        TPLID:
          name: 'QoS模板ID'
          type: string
          required: false
          description: '存在多条记录时，该参数不能重复。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        TPLNAME:
          name: 'QoS模板名'
          type: string
          required: false
          description: '存在多条记录时，该参数不能重复。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        QOSCLASUID:
          name: 'QoS分类ID'
          type: string
          required: false
          description: '与对端（中心UDM）一致。   * “AMBRMAXREQBWUL”和“AMBRNRUL”必须且只能配置一个。 * “AMBRMAXREQBWDL”和“AMBRNRDL”必须且只能配置一个。'
          data_source: '从对端获取'
          pattern: ''
          default: ''
        PRILEVEL:
          name: '分配/保留优先级数据'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PREEMPTIONCAP:
          name: '业务数据流是否能够占有能力'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PREEMPTIONVUL:
          name: '业务数据流是否能够被占有'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AMBRMAXREQBWUL:
          name: '最大请求上行带宽'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AMBRMAXREQBWDL:
          name: '最大请求下行带宽'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AMBRNRUL:
          name: 'NR上行速率'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AMBRNRDL:
          name: 'NR下行速率'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_apntpl_list:
      type: items
      properties:
        HLRSN:
          name: 'HLR序列号'
          type: integer
          minimum: 1
          maximum: 255
          required: true
          description: '与系统管理MML命令界面上的**ADD HLRSN**命令配置的“HLRSN”的取值相同。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        TPLID:
          name: '模板ID'
          type: integer
          minimum: 0
          maximum: 65534
          required: true
          description: '存在多条记录时，该参数不能重复。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        APN:
          name: '接入点名称'
          type: string
          maxLength: 63
          required: true
          description: '与对端（中心UDM）一致。'
          data_source: '从对端获取'
          pattern: ''
          default: ''
        PDNGWALLOCTYPE:
          name: 'PDN GW地址分配类型'
          type: string
          enum:
          - STATIC
          - DYNAMIC
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DYNAMIC
        MIPHAHOST:
          name: 'PDN GW 主机名称'
          type: string
          minLength: 1
          maxLength: 127
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MIPHAREALM:
          name: 'PDN GW 域名名称'
          type: string
          minLength: 1
          maxLength: 127
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MIPHAADDRIPV4:
          name: 'PDN GW IPV4地址'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MIPHAADDRIPV6:
          name: 'PDN GW IPV6地址'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NONIPDATADELMECH:
          name: 'Non-IP传输模式'
          type: string
          enum:
          - SGi_BASED_DATA_DELIVERY
          - SCEF_BASED_DATA_DELIVERY
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: SGi_BASED_DATA_DELIVERY
        APNOI:
          name: 'APN运营商标识符'
          type: string
          minLength: 1
          maxLength: 63
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_apnoitpl_list:
      type: items
      properties:
        HLRSN:
          name: 'HLR序列号'
          type: string
          required: false
          description: '与对端（中心UDM）一致。'
          data_source: '从对端获取'
          pattern: ''
          default: ''
        TPLID:
          name: '模板ID'
          type: string
          required: false
          description: '存在多条记录时，该参数不能重复。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        TPLNAME:
          name: '模板名'
          type: string
          required: false
          description: '存在多条记录时，该参数不能重复。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        APNOI:
          name: 'APN运营商标识符'
          type: string
          required: false
          description: '与对端（中心UDM）一致。'
          data_source: '从对端获取'
          pattern: ''
          default: ''
  examples:
    add_ngcqostpl_list:
    - HLRSN: 1
      TPLID: 1
      TPLNAME: 'test'
      NGQI: 1
      ARPPRILEVEL: 1
      PREEMPTIONCAP: FALSE
      PREEMPTIONVUL: FALSE
      NGQIPRILEVEL: 1
    add_dnnqostpl_list:
    - HLRSN: 1
      TPLID: 1
      TPLNAME: 'test'
      PDUTYPE: IPV4
      ALLOWEDPDUTYPE: IPV6
      SSCMODE: SSC_MODE_1
      ALLOWEDSCCMODE: SSC_MODE_2
      NGCQOSTPLID: 1
      AMBRUP: 100
      UPUNIT: Mbps
      AMBRDW: 1
      DWUNIT: Mbps
      CHARGE: '1111'
      UPINTEGR: NOT_NEEDED
      UPCONFID: NOT_NEEDED
    add_dnnqostpl_list_1:
    - HLRSN: 1
      TPLID: 1
      TPLNAME: 'test'
      PDUTYPE: IPV4
      ALLOWEDPDUTYPE: IPV6&ETHER
      SSCMODE: SSC_MODE_1
      ALLOWEDSCCMODE: SSC_MODE_2
      NGCQOSTPLID: 1
      AMBRUP: 100
      UPUNIT: Mbps
      AMBRDW: 1
      DWUNIT: Mbps
      CHARGE: '1111'
      UPINTEGR: NOT_NEEDED
      UPCONFID: NOT_NEEDED
    add_epsqostpl_list:
    - HLRSN: '1'
      TPLID: '1'
      TPLNAME: test_EPS
      QOSCLASUID: '5'
      PRILEVEL: '1'
      PREEMPTIONCAP: DISABLE
      PREEMPTIONVUL: DISABLE
      AMBRMAXREQBWUL: '10000'
      AMBRMAXREQBWDL: '200000'
      AMBRNRUL: '100000'
      AMBRNRDL: '200000'
    add_apntpl_list:
    - HLRSN: 1
      TPLID: 1
      APN: 'APN1'
      PDNGWALLOCTYPE: STATIC
      MIPHAHOST: 'PDN-GW'
      MIPHAREALM: 'huawei.com'
      MIPHAADDRIPV4: '10.144.98.135'
      MIPHAADDRIPV6: 'FC00:0:0:0:10:144:98:135'
      NONIPDATADELMECH: SGi_BASED_DATA_DELIVERY
      APNOI: 'huawei.com'
    add_apnoitpl_list:
    - HLRSN: '1'
      TPLID: '1'
      TPLNAME: test_apnoi
      APNOI: huawei.com
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 登录“UDM业务管理”窗口。

#### 1.1 同步5G用户数据时，请执行2~3。

#### 1.2 同步4G用户数据时，请执行4~6。

### 2 增加5G QoS模板。

#### 2.1 //5G QoS模板需要与中心UDM保持一致。

```jinja2
{%- if is_scenario_5g_user_data -%}
    {%- for item in add_ngcqostpl_list -%}
        ADD NGCQOSTPL:
        {#- --- 必选参数 --- -#}
        HLRSN={{item.HLRSN}},
        TPLID={{item.TPLID}},
        NGQI={{item.NGQI}},
        ARPPRILEVEL={{item.ARPPRILEVEL}},
        {#- --- 可选参数 --- -#}
        {%- if item.TPLNAME is not none -%}
            TPLNAME="{{item.TPLNAME}}",
        {%- endif -%}
        {%- if item.PREEMPTIONCAP is not none -%}
            PREEMPTIONCAP={{item.PREEMPTIONCAP}},
        {%- endif -%}
        {%- if item.PREEMPTIONVUL is not none -%}
            PREEMPTIONVUL={{item.PREEMPTIONVUL}},
        {%- endif -%}
        {%- if item.NGQIPRILEVEL is not none -%}
            NGQIPRILEVEL={{item.NGQIPRILEVEL}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 3 增加5G DNN QoS模板。

#### 3.1 //5G DNN QoS模板需要与中心UDM保持一致。不支持5G LAN时：

```jinja2
{%- if is_scenario_5g_user_data and is_scenario_non_5g_lan -%}
    {%- for item in add_dnnqostpl_list -%}
        ADD DNNQOSTPL:
        {#- --- 必选参数 --- -#}
        HLRSN={{item.HLRSN}},
        TPLID={{item.TPLID}},
        PDUTYPE={{item.PDUTYPE}},
        SSCMODE={{item.SSCMODE}},
        NGCQOSTPLID={{item.NGCQOSTPLID}},
        AMBRUP={{item.AMBRUP}},
        UPUNIT={{item.UPUNIT}},
        AMBRDW={{item.AMBRDW}},
        DWUNIT={{item.DWUNIT}},
        {#- --- 可选参数 --- -#}
        {%- if item.TPLNAME is not none -%}
            TPLNAME="{{item.TPLNAME}}",
        {%- endif -%}
        {%- if item.ALLOWEDPDUTYPE is not none -%}
            ALLOWEDPDUTYPE={{item.ALLOWEDPDUTYPE}},
        {%- endif -%}
        {%- if item.ALLOWEDSCCMODE is not none -%}
            ALLOWEDSCCMODE={{item.ALLOWEDSCCMODE}},
        {%- endif -%}
        {%- if item.CHARGE is not none -%}
            CHARGE="{{item.CHARGE}}",
        {%- endif -%}
        {%- if item.UPINTEGR is not none -%}
            UPINTEGR={{item.UPINTEGR}},
        {%- endif -%}
        {%- if item.UPCONFID is not none -%}
            UPCONFID={{item.UPCONFID}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 3.2 //5G DNN QoS模板需要与中心UDM保持一致。支持5G LAN时：

```jinja2
{%- if is_scenario_5g_user_data and is_scenario_5g_lan -%}
    {%- for item in add_dnnqostpl_list_1 -%}
        ADD DNNQOSTPL:
        {#- --- 必选参数 --- -#}
        HLRSN={{item.HLRSN}},
        TPLID={{item.TPLID}},
        PDUTYPE={{item.PDUTYPE}},
        SSCMODE={{item.SSCMODE}},
        NGCQOSTPLID={{item.NGCQOSTPLID}},
        AMBRUP={{item.AMBRUP}},
        UPUNIT={{item.UPUNIT}},
        AMBRDW={{item.AMBRDW}},
        DWUNIT={{item.DWUNIT}},
        {#- --- 可选参数 --- -#}
        {%- if item.TPLNAME is not none -%}
            TPLNAME="{{item.TPLNAME}}",
        {%- endif -%}
        {%- if item.ALLOWEDPDUTYPE is not none -%}
            ALLOWEDPDUTYPE={{item.ALLOWEDPDUTYPE}},
        {%- endif -%}
        {%- if item.ALLOWEDSCCMODE is not none -%}
            ALLOWEDSCCMODE={{item.ALLOWEDSCCMODE}},
        {%- endif -%}
        {%- if item.CHARGE is not none -%}
            CHARGE="{{item.CHARGE}}",
        {%- endif -%}
        {%- if item.UPINTEGR is not none -%}
            UPINTEGR={{item.UPINTEGR}},
        {%- endif -%}
        {%- if item.UPCONFID is not none -%}
            UPCONFID={{item.UPCONFID}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 4 配置EPS QoS模板。

#### 4.1 //EPS QoS模板需要与中心UDM保持一致。此处以配置“AMBRMAXREQBWUL”和“AMBRMAXREQBWDL”为例。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_epsqostpl_list的变量区（command: ADD EPSQOSTPL） -#}
<!-- MISSING_MACRO: command=ADD EPSQOSTPL list_name=add_epsqostpl_list step_id=4.1 -->
```

### 5 配置4G APN模板。

#### 5.1 //APN模板需要与中心UDM保持一致。

```jinja2
{%- if is_scenario_4g_user_data -%}
    {%- for item in add_apntpl_list -%}
        ADD APNTPL:
        {#- --- 必选参数 --- -#}
        HLRSN={{item.HLRSN}},
        TPLID={{item.TPLID}},
        APN="{{item.APN}}",
        {#- --- 可选参数 --- -#}
        {%- if item.PDNGWALLOCTYPE is not none -%}
            PDNGWALLOCTYPE={{item.PDNGWALLOCTYPE}},
        {%- endif -%}
        {%- if item.NONIPDATADELMECH is not none -%}
            NONIPDATADELMECH={{item.NONIPDATADELMECH}},
        {%- endif -%}
        {%- if item.APNOI is not none -%}
            APNOI="{{item.APNOI}}",
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：PDNGWALLOCTYPE=STATIC 时可选 --- -#}
        {%- if item.PDNGWALLOCTYPE == 'STATIC' -%}
            {%- if item.MIPHAHOST is not none -%}
                MIPHAHOST="{{item.MIPHAHOST}}",
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PDNGWALLOCTYPE=STATIC 时可选 --- -#}
        {%- if item.PDNGWALLOCTYPE == 'STATIC' -%}
            {%- if item.MIPHAREALM is not none -%}
                MIPHAREALM="{{item.MIPHAREALM}}",
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PDNGWALLOCTYPE=STATIC 时可选 --- -#}
        {%- if item.PDNGWALLOCTYPE == 'STATIC' -%}
            {%- if item.MIPHAADDRIPV4 is not none -%}
                MIPHAADDRIPV4="{{item.MIPHAADDRIPV4}}",
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PDNGWALLOCTYPE=STATIC 时可选 --- -#}
        {%- if item.PDNGWALLOCTYPE == 'STATIC' -%}
            {%- if item.MIPHAADDRIPV6 is not none -%}
                MIPHAADDRIPV6="{{item.MIPHAADDRIPV6}}",
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 6 配置APN运营商标识符模板。

#### 6.1 //APN运营商标识符模板需要与中心UDM保持一致。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_apnoitpl_list的变量区（command: ADD APNOITPL） -#}
<!-- MISSING_MACRO: command=ADD APNOITPL list_name=add_apnoitpl_list step_id=6.1 -->
```


---
id: ''
name: 配置模板数据
ne_type: UEG
type: feature
description: 该操作指导工程师在开局阶段，新建UDM网元时，完成5G模板数据的配置。
tags: []
risk_level: ''
doc_source: ["网络部署","园区入驻+地市共享（连接+计算）","5GC toB 部署边缘站点（站点为“风筝M”，带计算）","UEG初始配置（风筝M）","参考：详细配置指导","配置UDM","配置模板数据"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
该操作指导工程师在开局阶段，新建UDM网元时，完成5G模板数据的配置。

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
          description: '与系统管理MML命令界面上的**ADD VHLRSN**命令配置的“HLRSN”的取值相同。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        TPLID:
          name: '模板ID'
          type: integer
          minimum: 1
          maximum: 2147483646
          required: true
          description: '统一规划。'
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
          description: 'NGQI（即：5G QoS的特定参数）与无线/UNC对齐后配置。'
          data_source: '与对端协商'
          pattern: ''
          default: ''
        ARPPRILEVEL:
          name: '优先级'
          type: integer
          minimum: 1
          maximum: 15
          required: true
          description: '用户的优先级分为15个等级，数值越小，优先级越高。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PREEMPTIONCAP:
          name: '是否允许抢占低优先级业务的资源'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: '统一规划。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PREEMPTIONVUL:
          name: '是否允许资源被高优先级业务抢占'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: '统一规划。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        NGQIPRILEVEL:
          name: '5QI优先级'
          type: integer
          minimum: 1
          maximum: 127
          required: false
          description: '统一规划。'
          data_source: '本端规划'
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
          description: '与系统管理MML命令界面上的**ADD HLRSN**命令配置的“HLRSN”的取值相同。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        TPLID:
          name: 'QoS模板ID'
          type: integer
          minimum: 1
          maximum: 2147483646
          required: true
          description: '统一规划。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        TPLNAME:
          name: 'QoS模板名'
          type: string
          maxLength: 60
          required: false
          description: '统一规划。'
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
          description: '统一规划。'
          data_source: '本端规划'
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
          description: '统一规划。  支持5G LAN以太通信时，允许的PDU类型需包含“ETHER”。'
          data_source: '本端规划'
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
          description: '统一规划。'
          data_source: '本端规划'
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
          description: '统一规划。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        NGCQOSTPLID:
          name: '5GC QoS模板ID'
          type: integer
          minimum: 1
          maximum: 2147483646
          required: true
          description: '统一规划。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        AMBRUP:
          name: 'DNN级别上行速率'
          type: integer
          minimum: 1
          maximum: 9223372036854775807
          required: true
          description: '表示DNN级最大请求上行带宽，需与SMF侧配置一致。从SMF侧获取进行配置。'
          data_source: '与对端协商'
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
          description: '表示DNN级最大请求上行带宽的单位。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        AMBRDW:
          name: 'DNN级别下行速率'
          type: integer
          minimum: 1
          maximum: 9223372036854775807
          required: true
          description: '表示DNN级最大请求下行带宽，需与SMF侧配置一致。从SMF侧获取进行配置。'
          data_source: '与对端协商'
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
          description: '表示DNN级最大请求下行带宽的单位。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        CHARGE:
          name: '计费特性'
          type: string
          maxLength: 4
          required: false
          description: '统一规划。'
          data_source: '本端规划'
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
          description: '统一规划。'
          data_source: '本端规划'
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
          description: '统一规划。'
          data_source: '本端规划'
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
          description: '与系统管理MML命令界面上的**ADD HLRSN**命令配置的“HLRSN”的取值相同。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        TPLID:
          name: 'QoS模板ID'
          type: integer
          minimum: 1
          maximum: 2147483646
          required: true
          description: '统一规划。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        TPLNAME:
          name: 'QoS模板名'
          type: string
          maxLength: 60
          required: false
          description: '统一规划。'
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
          description: '统一规划。'
          data_source: '本端规划'
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
          description: '统一规划。  支持5G LAN以太通信时，允许的PDU类型需包含“ETHER”。'
          data_source: '本端规划'
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
          description: '统一规划。'
          data_source: '本端规划'
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
          description: '统一规划。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        NGCQOSTPLID:
          name: '5GC QoS模板ID'
          type: integer
          minimum: 1
          maximum: 2147483646
          required: true
          description: '统一规划。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        AMBRUP:
          name: 'DNN级别上行速率'
          type: integer
          minimum: 1
          maximum: 9223372036854775807
          required: true
          description: '表示DNN级最大请求上行带宽，需与SMF侧配置一致。从SMF侧获取进行配置。'
          data_source: '与对端协商'
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
          description: '表示DNN级最大请求上行带宽的单位。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        AMBRDW:
          name: 'DNN级别下行速率'
          type: integer
          minimum: 1
          maximum: 9223372036854775807
          required: true
          description: '表示DNN级最大请求下行带宽，需与SMF侧配置一致。从SMF侧获取进行配置。'
          data_source: '与对端协商'
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
          description: '表示DNN级最大请求下行带宽的单位。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        CHARGE:
          name: '计费特性'
          type: string
          maxLength: 4
          required: false
          description: '统一规划。'
          data_source: '本端规划'
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
          description: '统一规划。'
          data_source: '本端规划'
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
          description: '统一规划。'
          data_source: '本端规划'
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
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 登录“UDM业务管理”窗口。

### 2 增加5G QoS模板。

#### 2.1 //5G QoS模板需要与中心UDM保持一致。

```jinja2
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
```

### 3 增加5G DNN QoS模板。

#### 3.1 //5G DNN QoS模板需要与中心UDM保持一致。不支持5G LAN时：

```jinja2
{%- if is_scenario_non_5g_lan -%}
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
{%- if is_scenario_5g_lan -%}
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


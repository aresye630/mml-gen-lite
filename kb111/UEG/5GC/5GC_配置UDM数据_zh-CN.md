---
id: ''
name: 配置UDM数据
ne_type: UEG
type: feature
description: 该任务旨在指导操作人员在5G网络中配置5G LAN群组管理特性。
tags: []
risk_level: ''
doc_source: ["原子能力&行业场景","原子能力","5GC toB 原子能力-5G LAN","网络部署","运营商","配置5GC网元","配置UDM数据"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
该任务旨在指导操作人员在5G网络中配置5G LAN群组管理特性。

## 必备事项
前提条件

* 请仔细阅读WHFD-800030 5G LAN群组管理特性概述。
* 操作人员具有数据配置权限。
* 操作人员具有PGW Web LMT的操作权限。
* 需要加入5G虚拟网络组的用户已参考配置实例开户，并且签约的5GS DNN QoS模板中“默认PDU类型”参数取值要设置为“ETHER”。
* 阅读配置前的必读信息如表1所示。

  **表1** 阅读配置前必读

  | 参数颜色 | 来源 |
  | --- | --- |
  |  | 信息收集参数，指工程设计、部署前需要向客户收集的参数。 |
  |  | 网设决定参数，指根据运营商现网的不同方案，选择不同的参数配置。 |
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
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TPLID:
          name: '模板ID'
          type: integer
          minimum: 1
          maximum: 2147483646
          required: true
          description: ''
          data_source: ''
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
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ARPPRILEVEL:
          name: 'ARP优先级'
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
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TPLID:
          name: '模板ID'
          type: integer
          minimum: 1
          maximum: 2147483646
          required: true
          description: ''
          data_source: ''
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
    add_smdata_list:
      type: items
      properties:
        IMSI:
          name: 'IMSI'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SNSSAI:
          name: 'SNSSAI'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DNN:
          name: 'DNN'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DEFAULT:
          name: 'DEFAULT'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DNNQOSTPLID:
          name: 'DNNQOSTPLID'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_vngroup_list:
      type: items
      properties:
        HLRSN:
          name: 'HLR序列号'
          type: integer
          minimum: 1
          maximum: 255
          required: true
          description: '用于标识一个HLR序列号。该参数必须先由**ADD HLRSN**命令定义，然后才能在此处引用。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        INGROUPID:
          name: '内部组ID'
          type: string
          minLength: 10
          maxLength: 38
          required: true
          description: '用于标识移动网络内部设备之间通信时互相传递的组ID。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        EXTGROUPID:
          name: '外部组ID'
          type: string
          minLength: 3
          maxLength: 128
          required: true
          description: '用于标识移动网络对外能力开放接口中提供的组ID。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SHAREDID:
          name: '共享数据ID'
          type: string
          maxLength: 64
          required: true
          description: '用于标识为内部组创建的共享数据的ID。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SNSSAI:
          name: '切片标识'
          type: string
          minLength: 1
          maxLength: 10
          required: true
          description: '用于标识5G系统中的网络切片。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        DNN:
          name: '数据网名称'
          type: string
          maxLength: 64
          required: true
          description: '用于标识数据网名称。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PDUTYPES:
          name: '允许的PDU类型'
          type: string
          enum:
          - IPV4V6
          - IPV4
          - IPV6
          - UNSTR
          - ETHER
          required: true
          description: '用于标识允许的PDU类型。  层二5G LAN组时，使用样例值。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        GROUPNAME:
          name: '组名称'
          type: string
          maxLength: 32
          required: false
          description: '用于标识5G虚拟网络组名称。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SECONDARYAUTH:
          name: '是否需要二次认证'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: '用于标识SMF在用户PDU会话建立时是否需要二次认证授权。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        AAAIPV4ADDR:
          name: 'DN-AAA的IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: '用于标识二次认证授权的DN-AAA服务器IPv4地址。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        AAAIPV6ADDR:
          name: 'DN-AAA的IPv6地址'
          type: string
          maxLength: 43
          required: false
          description: '用于标识二次认证授权的DN-AAA服务器IPv6地址。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_groupid_list:
      type: items
      properties:
        IMSI:
          name: 'IMSI'
          type: string
          required: false
          description: '用于标识需要加入5G虚拟网络组的用户的IMSI号码。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        INGROUPID:
          name: '内部组ID'
          type: string
          required: false
          description: '用于标识移动网络内部设备之间通信时互相传递的组ID。该参数必须由**ADD VNGROUP**命令定义后才能在此处引用。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
  examples:
    add_ngcqostpl_list:
    - HLRSN: 1
      TPLID: 1
      TPLNAME: 'tp5glan01'
      NGQI: 9
      ARPPRILEVEL: 1
      PREEMPTIONCAP: TRUE
      PREEMPTIONVUL: FALSE
      NGQIPRILEVEL: 1
    add_dnnqostpl_list:
    - HLRSN: 1
      TPLID: 1
      TPLNAME: 'tp5glan01'
      PDUTYPE: ETHER
      SSCMODE: SSC_MODE_1
      NGCQOSTPLID: 1
      AMBRUP: 5
      UPUNIT: Gbps
      AMBRDW: 5
      DWUNIT: Gbps
    add_smdata_list:
    - IMSI: '460081000000001'
      SNSSAI: 1-010101
      DNN: dnn5glan01
      DEFAULT: TRUE
      DNNQOSTPLID: '1'
    add_vngroup_list:
    - HLRSN: 1
      INGROUPID: '1001-46008-01'
      EXTGROUPID: 'group01@huawei.com'
      SHAREDID: '46008-huawei01'
      SNSSAI: '1-010101'
      DNN: 'dnn5glan01'
      PDUTYPES: ETHER
      GROUPNAME: 'Huawei'
      SECONDARYAUTH: TRUE
      AAAIPV4ADDR: '10.20.30.100'
      AAAIPV6ADDR: '2001:0db8::1234'
    add_groupid_list:
    - IMSI: '460081000000001'
      INGROUPID: 1001-46008-01
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 配置5G LAN使用的DNN信息。

#### 1.1 //创建5G QoS模板。

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

#### 1.2 //创建DNN QoS模板。

```jinja2
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
    ;
{%- endfor -%}
```

### 2 签约会话管理数据。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_smdata_list的变量区（command: ADD SMDATA） -#}
<!-- MISSING_MACRO: command=ADD SMDATA list_name=add_smdata_list step_id=2 -->
```

### 3 创建5G LAN组。

#### 3.1 //如下以配置2个5G LAN组为例。规划多个5G LAN组时，“INGROUPID”、“EXTGROUPID”、“SHAREDID”取值必须不同。

```jinja2
{%- for item in add_vngroup_list -%}
    ADD VNGROUP:
    {#- --- 必选参数 --- -#}
    HLRSN={{item.HLRSN}},
    INGROUPID="{{item.INGROUPID}}",
    EXTGROUPID="{{item.EXTGROUPID}}",
    SHAREDID="{{item.SHAREDID}}",
    SNSSAI="{{item.SNSSAI}}",
    DNN="{{item.DNN}}",
    PDUTYPES={{item.PDUTYPES}},
    {#- --- 可选参数 --- -#}
    {%- if item.GROUPNAME is not none -%}
        GROUPNAME="{{item.GROUPNAME}}",
    {%- endif -%}
    {%- if item.SECONDARYAUTH is not none -%}
        SECONDARYAUTH={{item.SECONDARYAUTH}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：SECONDARYAUTH=TRUE 时可选 --- -#}
    {%- if item.SECONDARYAUTH == 'TRUE' -%}
        {%- if item.AAAIPV4ADDR is not none -%}
            AAAIPV4ADDR="{{item.AAAIPV4ADDR}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SECONDARYAUTH=TRUE 时可选 --- -#}
    {%- if item.SECONDARYAUTH == 'TRUE' -%}
        {%- if item.AAAIPV6ADDR is not none -%}
            AAAIPV6ADDR="{{item.AAAIPV6ADDR}}",
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 增加5G LAN组成员。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_groupid_list的变量区（command: ADD GROUPID） -#}
<!-- MISSING_MACRO: command=ADD GROUPID list_name=add_groupid_list step_id=4 -->
```


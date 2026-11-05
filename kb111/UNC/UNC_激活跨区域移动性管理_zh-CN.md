---
id: ''
name: 激活跨区域移动性管理
ne_type: UNC
type: feature
description: 本操作指导介绍在运行网络中，UE进行跨区域移动，所在区域的（R）AN超出了原来UPF的服务范围的场景下，保证UE会话业务连续性的操作过程。  适用于SMF。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","漫游管理功能","WSFD-104512 跨区域移动性管理","激活跨区域移动性管理"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本操作指导介绍在运行网络中，UE进行跨区域移动，所在区域的（R）AN超出了原来UPF的服务范围的场景下，保证UE会话业务连续性的操作过程。适用于SMF。

## 必备事项
前提条件

请仔细阅读WSFD-104512 跨区域移动性管理特性概述。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    add_pnfsmfserarea_list:
      type: items
      properties:
        NFINSTANCEID:
          name: 'NF实例标识'
          type: string
          minLength: 0
          maxLength: 50
          required: true
          description: '指定某UPF支持的为SMF提供的服务区域。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        SMFSERVINGAREA:
          name: 'SMF服务区域'
          type: string
          minLength: 1
          maxLength: 255
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_uparea_list:
      type: items
      properties:
        AREANAME:
          name: 'UPF服务区名称'
          type: string
          minLength: 1
          maxLength: 255
          required: true
          description: '增加UPF服务区。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        AREATYPE:
          name: 'UPF服务区类型'
          type: string
          enum:
          - S1TAI
          - N2TAI
          - LAI
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_upareabindn2tai_list:
      type: items
      properties:
        AREANAME:
          name: 'UPF服务区名称'
          type: string
          minLength: 0
          maxLength: 255
          required: true
          description: '增加UP服务区名称绑定的5G TAI范围。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        N2BEGINTAI:
          name: 'UPF服务区名称支持的5G TAI范围的起始值'
          type: string
          minLength: 11
          maxLength: 12
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        N2ENDTAI:
          name: 'UPF服务区名称支持的5G TAI范围的结束值'
          type: string
          minLength: 11
          maxLength: 12
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    set_iupfselfail_list:
      type: items
      properties:
        SWITCH:
          name: '开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: true
          description: '配置I-UPF选择失败处理方式。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        FAILPROC:
          name: '失败处理方式'
          type: string
          enum:
          - RELEASE_SESSION
          - KEEP_SESSION
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RELCAUSE:
          name: '释放会话时携带的NAS原因值'
          type: string
          enum:
          - NETWORK_FAILURE
          - REACTIVATION_REQUEST
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    add_pnfsmfserarea_list:
    - NFINSTANCEID: '12e4567-e89b-12d3-a456-112233440012'
      SMFSERVINGAREA: 'area01'
    add_uparea_list:
    - AREANAME: 'area01'
      AREATYPE: N2TAI
    add_upareabindn2tai_list:
    - AREANAME: 'area01'
      N2BEGINTAI: '12345000001'
      N2ENDTAI: '12345123456'
    set_iupfselfail_list:
    - SWITCH: ENABLE
      FAILPROC: KEEP_SESSION
      RELCAUSE: ''
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 进入“MML命令行-UNC”窗口。

### 2 配置规划的UPF为SMF提供的服务区域。

```jinja2
{%- for item in add_pnfsmfserarea_list -%}
    ADD PNFSMFSERAREA:
    {#- --- 必选参数 --- -#}
    NFINSTANCEID="{{item.NFINSTANCEID}}",
    SMFSERVINGAREA="{{item.SMFSERVINGAREA}}",
    ;
{%- endfor -%}
```

### UNC支持规划某些UPF仅作为分流UPF使用，不支持当前特性，因此配置规划此特性中的UPF时，需要执行**LST UPNODE**命令，确保当前规划的UPF对应的“是否仅支持作为分流UPF”取值为“不使能”。

### 3 配置此UPF的服务区。

```jinja2
{%- for item in add_uparea_list -%}
    ADD UPAREA:
    {#- --- 必选参数 --- -#}
    AREANAME="{{item.AREANAME}}",
    AREATYPE={{item.AREATYPE}},
    ;
{%- endfor -%}
```

### 4 配置此UPF服务区服务的TAI范围。

```jinja2
{%- for item in add_upareabindn2tai_list -%}
    ADD UPAREABINDN2TAI:
    {#- --- 必选参数 --- -#}
    AREANAME="{{item.AREANAME}}",
    N2BEGINTAI="{{item.N2BEGINTAI}}",
    N2ENDTAI="{{item.N2ENDTAI}}",
    ;
{%- endfor -%}
```

### 5 配置I-UPF选择失败处理方式。

```jinja2
{%- for item in set_iupfselfail_list -%}
    SET IUPFSELFAIL:
    {#- --- 必选参数 --- -#}
    SWITCH={{item.SWITCH}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：SWITCH=ENABLE 时必选 --- -#}
    {%- if item.SWITCH == 'ENABLE' -%}
        FAILPROC={{item.FAILPROC}},
    {%- endif -%}
    {#- --- 条件必选：FAILPROC=RELEASE_SESSION 时必选 --- -#}
    {%- if item.FAILPROC == 'RELEASE_SESSION' -%}
        RELCAUSE={{item.RELCAUSE}},
    {%- endif -%}
    ;
{%- endfor -%}
```


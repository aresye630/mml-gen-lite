---
id: ''
name: 配置归属地智能分流SMF
ne_type: UNC
type: feature
description: 本操作用于指导在智能分流SMF上基于专用DNN配置园区内专网UPF分流功能。
risk_level: ''
doc_source: ["网络部署","业务专题","5G Core 一跳入家解决方案","一跳入家解决方案（基于3GPP接入方案）","业务初始部署与调测","部署移动VPN","配置专用DNN数据","配置用户在园区内专网UPF分流（可选）","基于专用DNN配置","配置归属地智能分流SMF"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本操作用于指导在智能分流SMF上基于专用DNN配置园区内专网UPF分流功能。

## 必备事项
前提条件

已参考运营商配置规范完成网元的基本配置。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    add_apnarea_list:
      type: items
      properties:
        AREANAME:
          name: 'APN相关服务区域'
          type: string
          minLength: 1
          maxLength: 255
          required: true
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        AREATYPE:
          name: 'APN服务区域类型'
          type: string
          enum:
          - N2TAI
          required: true
          description: '通用DNN漫游分流方案仅支持5G会话专网UPF分流，服务区域类型需为5G TAI类型。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_apnareabndn2tai_list:
      type: items
      properties:
        AREANAME:
          name: '服务区域名称'
          type: string
          minLength: 1
          maxLength: 255
          required: true
          description: '一个AREANAME可以绑定多个5G TAI区域范围。同一个AREANAME下TAI区域不能有交叠，不同AREANAME下TAI区域不做限制。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        N2BEGINTAI:
          name: '服务区名称支持5GTAI范围的起始值'
          type: string
          minLength: 11
          maxLength: 12
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        N2ENDTAI:
          name: '服务区名称支持5GTAI范围的结束值'
          type: string
          minLength: 11
          maxLength: 12
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_muldnnbindarea_list:
      type: items
      properties:
        DEDDNN:
          name: '智能分流专网DNN'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        AREANAME:
          name: '服务区域名称'
          type: string
          minLength: 1
          maxLength: 255
          required: true
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_muldnnulclmode_list:
      type: items
      properties:
        DEDDNN:
          name: '智能分流专网DNN'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        ULCLDEPLOYMODE:
          name: 'ULCL部署模式'
          type: string
          enum:
          - PSASHUNTMUST
          - AREADEDUPFPREFER
          required: false
          description: '指定区域优先专网UPF分流。'
          data_source: '全网规划'
          pattern: ''
          default: PSASHUNTMUST
    add_virtualupfid_list:
      type: items
      properties:
        UPFINSTANCEID:
          name: 'UPF实例标识'
          type: string
          minLength: 1
          maxLength: 36
          required: true
          description: '该实例为智能分流UPF与专网UPF合一部署的实例ID。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        VUPFINSTANCEID:
          name: '虚拟UPF实例标识'
          type: string
          minLength: 1
          maxLength: 36
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_vupfidbindfunc_list:
      type: items
      properties:
        VUPFINSTANCEID:
          name: '虚拟UPF实例标识'
          type: string
          minLength: 1
          maxLength: 36
          required: true
          description: '该参数通过**LST VIRTUALUPFID**查询。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        FUNCNAME:
          name: '功能名称'
          type: string
          enum:
          - MULDNN
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
  examples:
    add_apnarea_list:
    - AREANAME: 'dnarea1'
      AREATYPE: N2TAI
    add_apnareabndn2tai_list:
    - AREANAME: 'dnarea1'
      N2BEGINTAI: '123003000001'
      N2ENDTAI: '123003123456'
    add_muldnnbindarea_list:
    - DEDDNN: 'stjwt.gd'
      AREANAME: 'dnarea1'
    add_muldnnulclmode_list:
    - DEDDNN: 'stjwt.gd'
      ULCLDEPLOYMODE: AREADEDUPFPREFER
    add_virtualupfid_list:
    - UPFINSTANCEID: '5EA7F228-47CC-2032-03A3-0E1313000001'
      VUPFINSTANCEID: '5EA7F228-47CC-2032-03A3-0E131300000A'
    add_vupfidbindfunc_list:
    - VUPFINSTANCEID: '5EA7F228-47CC-2032-03A3-0E131300000A'
      FUNCNAME: MulDNN
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 增加5G类型的TAI服务区域。

```jinja2
{%- for item in add_apnarea_list -%}
    ADD APNAREA:
    {#- --- 必选参数 --- -#}
    AREANAME="{{item.AREANAME}}",
    AREATYPE={{item.AREATYPE}},
    ;
{%- endfor -%}
```

### 2 增加服务区域的TAI绑定范围。

```jinja2
{%- for item in add_apnareabndn2tai_list -%}
    ADD APNAREABNDN2TAI:
    {#- --- 必选参数 --- -#}
    AREANAME="{{item.AREANAME}}",
    N2BEGINTAI="{{item.N2BEGINTAI}}",
    N2ENDTAI="{{item.N2ENDTAI}}",
    ;
{%- endfor -%}
```

### 3 绑定专网DNN和服务区域。

```jinja2
{%- for item in add_muldnnbindarea_list -%}
    ADD MULDNNBINDAREA:
    {#- --- 必选参数 --- -#}
    DEDDNN="{{item.DEDDNN}}",
    AREANAME="{{item.AREANAME}}",
    ;
{%- endfor -%}
```

### 4 配置智能分流专网DNN的ULCL部署模式。

```jinja2
{%- for item in add_muldnnulclmode_list -%}
    ADD MULDNNULCLMODE:
    {#- --- 必选参数 --- -#}
    DEDDNN="{{item.DEDDNN}}",
    {#- --- 可选参数 --- -#}
    {%- if item.ULCLDEPLOYMODE is not none -%}
        ULCLDEPLOYMODE={{item.ULCLDEPLOYMODE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 5 配置UPF虚拟实例标识。请使用LST VIRTUALUPFID查询UPF是否有配置虚拟实例ID，“UPFINSTANCEID”为智能分流UPF和专网UPF的实例ID。

### 若未配置虚拟实例ID则执行ADD VIRTUALUPFID和ADD VUPFIDBINDFUNC配置虚拟实例ID和开启多DNN开关。

### 若已配置虚拟实例ID则执行ADD VUPFIDBINDFUNC开启多DNN开关，虚拟实例ID请使用LST VIRTUALUPFID命令查询到的“虚拟UPF实例标识”。

```jinja2
{%- if is_scenario_vupf_unconfigured -%}
    {%- for item in add_virtualupfid_list -%}
        ADD VIRTUALUPFID:
        {#- --- 必选参数 --- -#}
        UPFINSTANCEID="{{item.UPFINSTANCEID}}",
        VUPFINSTANCEID="{{item.VUPFINSTANCEID}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- for item in add_vupfidbindfunc_list -%}
    ADD VUPFIDBINDFUNC:
    {#- --- 必选参数 --- -#}
    VUPFINSTANCEID="{{item.VUPFINSTANCEID}}",
    FUNCNAME={{item.FUNCNAME}},
    ;
{%- endfor -%}
```


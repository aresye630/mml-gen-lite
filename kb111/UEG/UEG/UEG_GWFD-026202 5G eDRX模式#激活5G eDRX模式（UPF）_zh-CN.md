---
id: GWFD-026202
name: 激活5G eDRX模式（UPF）
ne_type: UEG
type: feature
description: 本操作指导介绍在5G网络下激活eDRX功能的操作过程。  适用于UPF。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝S","MEC 特性指南（风筝S）","UEG特性指南","RedCap基本功能","GWFD-026202 5G eDRX模式","激活5G eDRX模式（UPF）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
本操作指导介绍在5G网络下激活eDRX功能的操作过程。适用于UPF。

## 必备事项
前提条件

* 请仔细阅读GWFD-026202 5G eDRX模式。
* 完成加载License（如果有需求，请联系华为技术支持工程师处理）。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
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
    add_apn_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '开启5G eDRX模式用户所使用的APN。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_apndlbuftime_list:
      type: items
      properties:
        APN:
          name: 'APN'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '已通过**ADD APN**命令配置，可以使用**LST APN**命令查询。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        REDCAPNRUSER:
          name: 'RedCap-NR用户下行数据缓存时长'
          type: integer
          minimum: 3
          maximum: 200
          required: false
          description: '如果SMF没有下发DL Buffering Duration信元，使用该参数配置作为用户下行数据缓存时长。如果SMF下发DL Buffering Duration信元，取DL Buffering Duration值作为用户下行数据缓存时长。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_apndlltbuffer_list:
      type: items
      properties:
        APN:
          name: 'APN'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '已通过**ADD APN**命令配置，可以使用**LST APN**命令查询。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        MAXBUFFERNUM:
          name: '最大缓存个数'
          type: integer
          minimum: 1
          maximum: 64
          required: true
          description: '取该参数配置值与SMF下发的DL Buffering Packet Count两者中最小值作为系统实际缓存的最大个数; 如果SMF没有下发DL Buffering Packet Count，使用该参数配置作为系统实际缓存的最大个数。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        BUFFERMODE:
          name: '储存方式'
          type: string
          enum:
          - BUFF_MODE_CHAIN
          - BUFF_MODE_RING
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_glbdlbuftime_list:
      type: items
      properties:
        REDCAPNRUSER:
          name: 'RedCap-NR用户下行数据缓存时长'
          type: integer
          minimum: 3
          maximum: 200
          required: false
          description: '如果SMF没有下发DL Buffering Duration信元，使用该参数配置作为用户下行数据缓存时长。如果SMF下发DL Buffering Duration信元，取DL Buffering Duration值作为用户下行数据缓存时长。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_glbdlltbuffer_list:
      type: items
      properties:
        MAXBUFFERNUM:
          name: '最大缓存个数'
          type: integer
          minimum: 1
          maximum: 64
          required: true
          description: '取该参数配置值与SMF下发的DL Buffering Packet Count两者中最小值作为系统实际缓存的最大个数; 如果SMF没有下发DL Buffering Packet Count，使用该参数配置作为系统实际缓存的最大个数。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        BUFFERMODE:
          name: '储存方式'
          type: string
          enum:
          - BUFF_MODE_CHAIN
          - BUFF_MODE_RING
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV3G5EDRX01'
      SWITCH: ENABLE
    add_apn_list:
    - APN: 'apn-test'
    set_apndlbuftime_list:
    - APN: 'apn-test'
      REDCAPNRUSER: 10
    set_apndlltbuffer_list:
    - APN: 'apn-test'
      MAXBUFFERNUM: 4
      BUFFERMODE: BUFF_MODE_RING
    set_glbdlbuftime_list:
    - REDCAPNRUSER: 20
    set_glbdlltbuffer_list:
    - MAXBUFFERNUM: 16
      BUFFERMODE: BUFF_MODE_RING
```

## 3 命令模板定义
<!-- @mml:block= commands -->

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

### 2 配置5G eDRX模式所使用的APN。

```jinja2
{%- for item in add_apn_list -%}
    ADD APN:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    ;
{%- endfor -%}
```

### 3 **可选：**配置APN下的5G eDRX参数。

#### 3.1 配置APN的下行数据缓存时长。

```jinja2
{%- if is_optional_apn_5g_edrx_param -%}
    {%- for item in set_apndlbuftime_list -%}
        SET APNDLBUFTIME:
        {#- --- 必选参数 --- -#}
        APN="{{item.APN}}",
        {#- --- 可选参数 --- -#}
        {%- if item.REDCAPNRUSER is not none -%}
            REDCAPNRUSER={{item.REDCAPNRUSER}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 3.2 配置APN的下行数据长时间缓存配置。

```jinja2
{%- if is_optional_apn_5g_edrx_param -%}
    {%- for item in set_apndlltbuffer_list -%}
        SET APNDLLTBUFFER:
        {#- --- 必选参数 --- -#}
        APN="{{item.APN}}",
        MAXBUFFERNUM={{item.MAXBUFFERNUM}},
        BUFFERMODE={{item.BUFFERMODE}},
        ;
    {%- endfor -%}
{%- endif -%}
```

### 4 **可选：**配置全局的5G eDRX参数。

#### 4.1 配置全局下行数据缓存时长。

```jinja2
{%- if is_optional_global_5g_edrx_param -%}
    {%- for item in set_glbdlbuftime_list -%}
        SET GLBDLBUFTIME:
        {#- --- 可选参数 --- -#}
        {%- if item.REDCAPNRUSER is not none -%}
            REDCAPNRUSER={{item.REDCAPNRUSER}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 4.2 配置全局下行数据长时间缓存配置。

```jinja2
{%- if is_optional_global_5g_edrx_param -%}
    {%- for item in set_glbdlltbuffer_list -%}
        SET GLBDLLTBUFFER:
        {#- --- 必选参数 --- -#}
        MAXBUFFERNUM={{item.MAXBUFFERNUM}},
        BUFFERMODE={{item.BUFFERMODE}},
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 如果全局和APN下同时配置了缓存时长和长时间缓存配置参数，生效优先级：APN>全局。


---
id: GWFD-026104
name: 激活NB-IoT eDRX模式
ne_type: UEG
type: feature
description: 本操作指导介绍在4G网络下激活NB-IoT eDRX模式特性的操作过程。  适用于SGW-U。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝S","MEC 特性指南（风筝S）","UEG特性指南","物联网功能","NB-IoT","GWFD-026104 NB-IoT eDRX模式","激活NB-IoT eDRX模式"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
本操作指导介绍在4G网络下激活NB-IoT eDRX模式特性的操作过程。适用于SGW-U。

## 必备事项
前提条件

* 请仔细阅读GWFD-026104 NB-IoT eDRX模式。
* 已开启NB-IoT基本接入功能（详见激活NB-IoT终端标准接入）。
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
    add_pool_list:
      type: items
      properties:
        POOLNAME:
          name: '地址池名称'
          type: string
          minLength: 1
          maxLength: 79
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
          description: ''
          data_source: ''
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
          description: '可以使用**LST POOL**命令进行查询。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        NBIOTUSER:
          name: 'NB-IoT用户下行数据缓存时长'
          type: integer
          minimum: 3
          maximum: 200
          required: false
          description: '-'
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
          description: '可以使用**LST POOL**命令进行查询。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        MAXBUFFERNUM:
          name: '最大缓存个数'
          type: integer
          minimum: 1
          maximum: 64
          required: true
          description: '-'
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
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_glbdlbuftime_list:
      type: items
      properties:
        NBIOTUSER:
          name: 'NB-IoT用户下行数据缓存时长'
          type: integer
          minimum: 3
          maximum: 200
          required: false
          description: '-'
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
          description: '该参数与DDN Ack消息携带的缓存个数取最小值作为系统实际缓存的最大个数; 如果DDN Ack消息没有携带缓存个数，使用该参数配置作为系统实际缓存的最大个数。'
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
    - LICITEM: 'LKV3G5NDRX01'
      SWITCH: ENABLE
    add_pool_list:
    - POOLNAME: ''
    add_apn_list:
    - APN: 'apnnb'
    set_apndlbuftime_list:
    - APN: 'apnnb'
      NBIOTUSER: 10
    set_apndlltbuffer_list:
    - APN: 'apnnb'
      MAXBUFFERNUM: 4
      BUFFERMODE: BUFF_MODE_RING
    set_glbdlbuftime_list:
    - NBIOTUSER: 20
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

### 2 配置eDRX模式所使用的APN。

```jinja2
{%- for item in add_pool_list -%}
    ADD POOL:
    {#- --- 必选参数 --- -#}
    POOLNAME="{{item.POOLNAME}}",
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_apn_list -%}
    ADD APN:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    ;
{%- endfor -%}
```

### 3 **可选：**配置APN下的NB-IoT eDRX参数。

#### 3.1 配置APN的下行数据缓存时长。

```jinja2
{%- if is_optional_apn_edrx_params -%}
    {%- for item in set_apndlbuftime_list -%}
        SET APNDLBUFTIME:
        {#- --- 必选参数 --- -#}
        APN="{{item.APN}}",
        {#- --- 可选参数 --- -#}
        {%- if item.NBIOTUSER is not none -%}
            NBIOTUSER={{item.NBIOTUSER}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 3.2 配置APN的下行数据长时间缓存配置。

```jinja2
{%- if is_optional_apn_edrx_params -%}
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

### 4 **可选：**配置全局的NB-IoT eDRX参数。

#### 4.1 配置全局下行数据缓存时长。

```jinja2
{%- if is_optional_global_edrx_params -%}
    {%- for item in set_glbdlbuftime_list -%}
        SET GLBDLBUFTIME:
        {#- --- 可选参数 --- -#}
        {%- if item.NBIOTUSER is not none -%}
            NBIOTUSER={{item.NBIOTUSER}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 4.2 配置全局下行数据长时间缓存配置。

```jinja2
{%- if is_optional_global_edrx_params -%}
    {%- for item in set_glbdlltbuffer_list -%}
        SET GLBDLLTBUFFER:
        {#- --- 必选参数 --- -#}
        MAXBUFFERNUM={{item.MAXBUFFERNUM}},
        BUFFERMODE={{item.BUFFERMODE}},
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 对于缓存时长和长时间缓存配置：

#### 如果SGW-U/PGW-U和MME上都配置了缓存时长和长时间缓存配置参数，当MME通过DDN ACK下发这些参数时，最大缓存个数取两者最小值，NB-IoT用户下行数据缓存时长取MME下发值。

#### 如果全局和APN下同时配置了缓存时长和长时间缓存配置参数，生效优先级：APN>全局。


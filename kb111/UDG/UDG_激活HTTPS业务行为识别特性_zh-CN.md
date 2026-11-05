---
id: GWFD-110404
name: 激活HTTPS业务行为识别特性
ne_type: UDG
type: feature
description: 当前加密协议的业务识别主要基于SNI和Domain进行，对于未携带SNI的场景无法准确识别业务。在UDG开启HTTPS业务行为识别功能后，UDG会对HTTPS业务报文做TLS指纹识别，提升识别精度。  适用于PGW-U、UPF。
risk_level: ''
doc_source: ["特性部署","特性指南","UDG特性指南","计费防欺诈功能","GWFD-110404 HTTPS业务行为识别","激活HTTPS业务行为识别特性"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
当前加密协议的业务识别主要基于SNI和Domain进行，对于未携带SNI的场景无法准确识别业务。在UDG开启HTTPS业务行为识别功能后，UDG会对HTTPS业务报文做TLS指纹识别，提升识别精度。适用于PGW-U、UPF。

## 必备事项
前提条件

* 请仔细阅读GWFD-110404 HTTPS业务行为识别。
* 完成加载license（如果有需求，请联系华为技术支持工程师处理）。
* 完成业务感知配置。
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
    lod_signaturedb_list:
      type: items
      properties:
        LOADMODE:
          name: '特征库加载模式'
          type: string
          enum:
          - LATEST
          - REFRESH
          - SPECIFIC
          required: true
          description: '该参数用于指定特征库的加载模式。   * SPECIFIC：指定特定的特征库版本加载。 * LATEST：指定最新的特征库版本加载。 * REFRESH：指定最新的特征库版本更新，但不改变配置保存方式。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        VERSION:
          name: '特征库版本号'
          type: string
          minLength: 0
          maxLength: 16
          required: false
          description: '该参数在“LOADMODE”配置为“SPECIFIC”时为必选参数。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_fingerident_list:
      type: items
      properties:
        CFGPROTMODE:
          name: '协议配置方式'
          type: string
          enum:
          - ALL
          - SPECIFIC
          required: true
          description: '该参数用于设置SA指纹识别功能协议的配置方式。   * ALL：所有协议。 * SPECIFIC：指定协议。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        CFGDOMAINNAME:
          name: '配置域名称'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PROTOCOLNAME:
          name: '协议名称'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV3G5HSBI01'
      SWITCH: ENABLE
    lod_signaturedb_list:
    - LOADMODE: SPECIFIC
      VERSION: '01.0002.1061.01'
    add_fingerident_list:
    - CFGPROTMODE: ALL
      CFGDOMAINNAME: ''
      PROTOCOLNAME: ''
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 打开本特性的License特性配置开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

### 2 加载特定的完整的特征库文件。指纹库内置在特征库中。如果已经加载特征库，则升级新特征库文件。

```jinja2
{%- for item in lod_signaturedb_list -%}
    LOD SIGNATUREDB:
    {#- --- 必选参数 --- -#}
    LOADMODE={{item.LOADMODE}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：LOADMODE=SPECIFIC 时必选 --- -#}
    {%- if item.LOADMODE == 'SPECIFIC' -%}
        VERSION="{{item.VERSION}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 开启HTTPS业务行为识别功能。

```jinja2
{%- for item in add_fingerident_list -%}
    ADD FINGERIDENT:
    {#- --- 必选参数 --- -#}
    CFGPROTMODE={{item.CFGPROTMODE}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：CFGPROTMODE=SPECIFIC 时必选 --- -#}
    {%- if item.CFGPROTMODE == 'SPECIFIC' -%}
        PROTOCOLNAME="{{item.PROTOCOLNAME}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：CFGPROTMODE=SPECIFIC 时可选 --- -#}
    {%- if item.CFGPROTMODE == 'SPECIFIC' -%}
        {%- if item.CFGDOMAINNAME is not none -%}
            CFGDOMAINNAME="{{item.CFGDOMAINNAME}}",
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 可通过**LST SUPPFINGERIDEN**命令查询系统内哪些协议支持指纹识别功能。


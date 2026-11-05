---
id: GWFD-030205
name: 激活通用DNN漫游分流
ne_type: UEG
type: feature
description: 在UEG上部署通用DNN漫游分流功能，需要开启通用DNN漫游分流功能开关。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝S","MEC 特性指南（风筝S）","UEG特性指南","本地分流功能","GWFD-030205 通用DNN漫游分流","激活通用DNN漫游分流"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
在UEG上部署通用DNN漫游分流功能，需要开启通用DNN漫游分流功能开关。

## 必备事项
前提条件

前提条件

* 请仔细阅读GWFD-030205 通用DNN漫游分流。
* UEG完成与周边网元的对接。
* 已完成分流业务相关的部署。
* 完成**License****加载**（如果有需求，请联系华为技术支持工程师处理）。
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
          description: '该参数用于指定“移动VPN园区接入”License项。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        SWITCH:
          name: '开关'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: true
          description: '该参数用于表示License项的配置开关是否已经打开。'
          data_source: '固定取值'
          pattern: ''
          default: ''
    set_rtsdnnpara_list:
      type: items
      properties:
        PRIVATENETSW:
          name: '专网通用DNN漫游分流开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '用于指定系统是否开启专网的通用DNN漫游分流功能。'
          data_source: '固定取值'
          pattern: ''
          default: ''
    set_rtsdnnpara_list_1:
      type: items
      properties:
        NATALGPROTV4:
          name: 'IPv4 NAT ALG协议'
          type: string
          required: false
          description: '用于指定系统是否开启通用DNN漫游分流特定协议类型NAT ALG的IPv4地址替换。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        NATALGPROTV6:
          name: 'IPv6 NAT ALG协议'
          type: string
          required: false
          description: '用于指定系统是否开启通用DNN漫游分流特定协议类型NAT ALG的IPv6 地址替换。'
          data_source: '本端规划'
          pattern: ''
          default: ''
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV3G5MVCA01'
      SWITCH: ENABLE
    set_rtsdnnpara_list:
    - PRIVATENETSW: ENABLE
    set_rtsdnnpara_list_1:
    - NATALGPROTV4: FTP-1&RTSP-1
      NATALGPROTV6: FTP-1
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 在专网UPF上打开特性License开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

### 2 在专网UPF上配置通用DNN漫游分流开关。

```jinja2
{%- for item in set_rtsdnnpara_list -%}
    SET RTSDNNPARA:
    {#- --- 可选参数 --- -#}
    {%- if item.PRIVATENETSW is not none -%}
        PRIVATENETSW={{item.PRIVATENETSW}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 （可选）在专网UPF上配置针对指定协议的地址替换。

```jinja2
{%- if is_optional_protocol_address_replacement -%}
    {%- for item in set_rtsdnnpara_list_1 -%}
        SET RTSDNNPARA:
        {#- --- 可选参数 --- -#}
        {%- if item.NATALGPROTV4 is not none -%}
            NATALGPROTV4={{item.NATALGPROTV4}},
        {%- endif -%}
        {%- if item.NATALGPROTV6 is not none -%}
            NATALGPROTV6={{item.NATALGPROTV6}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```


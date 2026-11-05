---
id: ''
name: 配置UPF
ne_type: UDG
type: feature
description: 本操作用于指导在专网UPF上开启通用DNN漫游分流特性。
risk_level: ''
doc_source: ["特性部署","业务专题","5G Core 一跳入家解决方案","一跳入家解决方案（基于3GPP接入方案）","业务初始部署与调测","部署移动VPN","配置专用DNN数据","配置通用DNN漫游分流","配置UPF"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本操作用于指导在专网UPF上开启通用DNN漫游分流特性。

## 必备事项
前提条件

已参考运营商配置规范完成网元的基本配置。
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
          description: '该参数用于指定需要开通的License项。'
          data_source: '本端规划'
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
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_rtsdnnpara_list:
      type: items
      properties:
        NATALGPROTV4:
          name: 'IPv4 NAT ALG协议'
          type: string
          required: false
          description: '该参数用于指定系统是否开启通用DNN漫游分流特定协议类型NAT ALG的IPv4地址替换。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        NATALGPROTV6:
          name: 'IPv6 NAT ALG协议'
          type: string
          required: false
          description: '该参数用于指定系统是否开启通用DNN漫游分流特定协议类型NAT ALG的IPv6 地址替换。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_licenseswitch_list_1:
      type: items
      properties:
        LICITEM:
          name: 'License项'
          type: string
          minLength: 0
          maxLength: 255
          required: true
          description: '该参数用于指定需要开通的License项。'
          data_source: '本端规划'
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
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_rtsdnnpara_list_1:
      type: items
      properties:
        PRIVATENETSW:
          name: '专网通用DNN漫游分流开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '该参数用于指定系统是否开启专网的通用DNN漫游分流功能。'
          data_source: '本端规划'
          pattern: ''
          default: ''
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV3G5LALG01'
      SWITCH: ENABLE
    set_rtsdnnpara_list:
    - NATALGPROTV4: FTP-1&RTSP-1
      NATALGPROTV6: FTP-1
    set_licenseswitch_list_1:
    - LICITEM: 'LKV3G5MVCA01'
      SWITCH: ENABLE
    set_rtsdnnpara_list_1:
    - PRIVATENETSW: ENABLE
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 （可选）当需要使用FTP访问、下载业务，或者RTSP协议类视频相关业务时，并已申请了该license，则需要开启轻量化ALG license开关。

```jinja2
{%- if is_optional_lightweight_alg_license_switch -%}
    {%- for item in set_licenseswitch_list -%}
        SET LICENSESWITCH:
        {#- --- 必选参数 --- -#}
        LICITEM="{{item.LICITEM}}",
        SWITCH={{item.SWITCH}},
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_optional_lightweight_alg_license_switch -%}
    {%- for item in set_rtsdnnpara_list -%}
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

### 2 专网UPF是UEG产品时，需要开启通用DNN漫游分流的license开关。

```jinja2
{%- if is_scenario_ueg_product -%}
    {%- for item in set_licenseswitch_list_1 -%}
        SET LICENSESWITCH:
        {#- --- 必选参数 --- -#}
        LICITEM="{{item.LICITEM}}",
        SWITCH={{item.SWITCH}},
        ;
    {%- endfor -%}
{%- endif -%}
```

### 3 打开专网的通用DNN漫游分流功能开关。

```jinja2
{%- for item in set_rtsdnnpara_list_1 -%}
    SET RTSDNNPARA:
    {#- --- 可选参数 --- -#}
    {%- if item.PRIVATENETSW is not none -%}
        PRIVATENETSW={{item.PRIVATENETSW}},
    {%- endif -%}
    ;
{%- endfor -%}
```


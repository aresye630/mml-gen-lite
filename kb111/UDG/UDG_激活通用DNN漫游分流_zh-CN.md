---
id: GWFD-020531
name: 激活通用DNN漫游分流
ne_type: UDG
type: feature
description: 在UDG上部署通用DNN漫游分流功能，需要开启通用DNN漫游分流功能开关。
risk_level: ''
doc_source: ["特性部署","特性指南","UDG特性指南","超级互联功能","GWFD-020531 通用DNN漫游分流","激活通用DNN漫游分流"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
在UDG上部署通用DNN漫游分流功能，需要开启通用DNN漫游分流功能开关。

## 必备事项
前提条件

* 请仔细阅读GWFD-020531 通用DNN漫游分流。
* UDG完成与周边网元的对接。
* 已完成分流业务相关的部署。
* 完成**License****加载**（如果有需求，请联系华为技术支持工程师处理）。
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
          description: '该参数用于指定“移动VPN智能分流园区接入”License项。'
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
        PUBLICNETSW:
          name: '公网通用DNN漫游分流开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '该参数用于指定系统是否开启公网的通用DNN漫游分流功能。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        UEIPCONFLICTCHK:
          name: 'UE IP地址冲突检测开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '该参数用于指定是否开启UE IP地址和园区服务器IP地址冲突的检测。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        UEIPREALLOC:
          name: 'UE IP地址重分配开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '该参数用于指定系统当UE IP地址和园区服务器IP地址冲突时是否开启UE IP地址重分配。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        UEIPREALLOCNUM:
          name: 'UE IP地址重分配次数'
          type: integer
          minimum: 0
          maximum: 3000
          required: false
          description: '该参数用于指定当分配的UE IP地址和园区服务器的IP地址列表冲突时，系统在空闲地址列表中获取非冲突IP地址的最大的尝试次数。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        UEIPCONFLICTPLY:
          name: 'UE IP地址冲突处理策略'
          type: string
          enum:
          - BYPASS
          - FAIL
          required: false
          description: '该参数用于指定系统出现分配的UE IP地址和园区服务器IP地址冲突时是否继续激活用户。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        N4RPTSW:
          name: 'N4上报通用DNN漫游分流的锚点功能开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '该参数用于指定系统是否在N4偶联消息中上报系统当前配置的公网通用DNN漫游分流特性功能开关。'
          data_source: '与对端协商'
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
          description: '用于指定系统是否开启专网的通用DNN漫游分流功能。'
          data_source: '固定取值'
          pattern: ''
          default: ''
    set_rtsdnnpara_list_2:
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
    - LICITEM: 'LKV3G5STCA01'
      SWITCH: ENABLE
    set_rtsdnnpara_list:
    - PUBLICNETSW: ENABLE
      UEIPCONFLICTCHK: ENABLE
      UEIPREALLOC: ENABLE
      UEIPREALLOCNUM: 1000
      UEIPCONFLICTPLY: BYPASS
      N4RPTSW: ENABLE
    set_rtsdnnpara_list_1:
    - PRIVATENETSW: ENABLE
    set_rtsdnnpara_list_2:
    - NATALGPROTV4: FTP-1&RTSP-1
      NATALGPROTV6: FTP-1
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 在公网UPF上打开特性License开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

### 2 在公网UPF上配置通用DNN漫游分流开关。

```jinja2
{%- for item in set_rtsdnnpara_list -%}
    SET RTSDNNPARA:
    {#- --- 可选参数 --- -#}
    {%- if item.PUBLICNETSW is not none -%}
        PUBLICNETSW={{item.PUBLICNETSW}},
    {%- endif -%}
    {%- if item.UEIPCONFLICTCHK is not none -%}
        UEIPCONFLICTCHK={{item.UEIPCONFLICTCHK}},
    {%- endif -%}
    {%- if item.N4RPTSW is not none -%}
        N4RPTSW={{item.N4RPTSW}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：UEIPCONFLICTCHK=ENABLE 时必选 --- -#}
    {%- if item.UEIPCONFLICTCHK == 'ENABLE' -%}
        UEIPREALLOC={{item.UEIPREALLOC}},
    {%- endif -%}
    {#- --- 条件必选：UEIPREALLOC=ENABLE 时必选 --- -#}
    {%- if item.UEIPREALLOC == 'ENABLE' -%}
        UEIPREALLOCNUM={{item.UEIPREALLOCNUM}},
    {%- endif -%}
    {#- --- 条件必选：UEIPCONFLICTCHK=ENABLE 时必选 --- -#}
    {%- if item.UEIPCONFLICTCHK == 'ENABLE' -%}
        UEIPCONFLICTPLY={{item.UEIPCONFLICTPLY}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 在专网UPF上配置通用DNN漫游分流开关。

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

### 4 （可选）在专网UPF上配置针对指定协议的地址替换。

```jinja2
{%- if is_optional_protocol_address_replacement -%}
    {%- for item in set_rtsdnnpara_list_2 -%}
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


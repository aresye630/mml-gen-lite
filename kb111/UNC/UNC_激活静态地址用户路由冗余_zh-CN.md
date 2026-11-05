---
id: ''
name: 激活静态地址用户路由冗余
ne_type: UNC
type: feature
description: 当需要保证静态IP地址网段内的用户选择到UPF的可靠性时，激活静态地址用户路由冗余功能。  适用于GGSN、PGW-C、SMF。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","分布式网络功能","WSFD-107021 静态地址用户路由冗余","激活静态地址用户路由冗余"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
当需要保证静态IP地址网段内的用户选择到UPF的可靠性时，激活静态地址用户路由冗余功能。适用于GGSN、PGW-C、SMF。

## 必备事项
前提条件

* 请仔细阅读WSFD-107021 静态地址用户路由冗余特性概述。
* 本特性与UDG配合使用生效，要求UNC上配置的用户静态地址网段信息必须在包含在UDG上配置的地址池内，请参考UDG中的**GWFD-010104 地址分配方式**。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    add_addrpool_list:
      type: items
      properties:
        POOLNAME:
          name: '地址池名称'
          type: string
          minLength: 1
          maxLength: 79
          required: true
          description: '为采用静态地址分配方式的用户配置对应的地址池。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPVERSION:
          name: 'IP地址类型'
          type: string
          enum:
          - IPv4
          - IPv6
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: IPv4
        POOLTYPE:
          name: '地址池类型'
          type: string
          enum:
          - Local
          - UDM
          - Radius
          - DHCP
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: Local
        CHECKIPVALID:
          name: '检查地址合法性'
          type: string
          enum:
          - Disable
          - Enable
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: Disable
        IMSSW:
          name: 'IMS开关'
          type: string
          enum:
          - Disable
          - Enable
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: Enable
        IPLEASE:
          name: '地址租约使能标志'
          type: string
          enum:
          - Disable
          - Enable
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: Disable
        OVERLAP:
          name: '是否允许地址重叠'
          type: string
          enum:
          - Disable
          - Enable
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: Disable
        RELEASETIME:
          name: '地址租期(秒)'
          type: integer
          minimum: 0
          maximum: 86400
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 10
        SINGLEIPFLAG:
          name: '子池类型'
          type: string
          enum:
          - Enable
          - Disable
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: Disable
    add_section_list:
      type: items
      properties:
        POOLNAME:
          name: 'Pool名称'
          type: string
          minLength: 1
          maxLength: 79
          required: true
          description: '配置本地地址池里的地址段'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SECTIONNUM:
          name: 'Section序号'
          type: integer
          minimum: 0
          maximum: 63
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPVERSION:
          name: 'IP类型'
          type: string
          enum:
          - IPv4
          - IPv6
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        V4STARTIP:
          name: 'IPV4开始地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        V4ENDIP:
          name: 'IPV4结束地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        V6PREFIXEND:
          name: 'IPv6前缀结束地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        V6PREFIXLENGTH:
          name: 'IPv6前缀长度'
          type: integer
          minimum: 49
          maximum: 64
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        V6PREFIXSTART:
          name: 'IPv6前缀起始地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_addrpoolgrp_list:
      type: items
      properties:
        POOLGRPNAME:
          name: '地址池组名称'
          type: string
          minLength: 1
          maxLength: 79
          required: true
          description: '配置地址池组。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        POOLGRPTYPE:
          name: '地址池类型'
          type: string
          enum:
          - Local
          - UDM
          - Radius
          - DHCP
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: Local
    add_poolbindgrp_list:
      type: items
      properties:
        POOLGRPNAME:
          name: '地址池组名称'
          type: string
          minLength: 1
          maxLength: 79
          required: true
          description: '已通过**ADD ADDRPOOLGRP**配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        POOLNAME:
          name: '地址池名称'
          type: string
          minLength: 1
          maxLength: 79
          required: true
          description: '已通过**ADD ADDRPOOL**配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_upnode_list:
      type: items
      properties:
        NFINSTANCENAME:
          name: 'UPF实例名称'
          type: string
          minLength: 0
          maxLength: 255
          required: true
          description: '配置静态地址用户使用的UPF。  已通过**ADD PNFPROFILE**配置。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        ADDRALLOCMODE:
          name: '地址分配属性'
          type: string
          enum:
          - INHERIT
          - SMF_ALLOC
          - UPF_FIRST
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: INHERIT
    add_addrupgroup_list:
      type: items
      properties:
        UPFGRPNAME:
          name: 'UPF组名称'
          type: string
          minLength: 1
          maxLength: 32
          required: true
          description: '配置静态地址用户使用的UPF组。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        UPFGRPTYPE:
          name: 'UPF组类型'
          type: string
          enum:
          - Local
          - UDM
          - Radius
          - DHCP
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: Local
    add_upfbindgrp_list:
      type: items
      properties:
        UPFGRPNAME:
          name: 'UPF组名称'
          type: string
          minLength: 1
          maxLength: 32
          required: true
          description: '已通过**ADD ADDRUPGROUP**配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        UPFID:
          name: 'UPF实例标识'
          type: string
          minLength: 0
          maxLength: 255
          required: true
          description: '已通过**ADD UPNODE**配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        PRIORITY:
          name: '优先级'
          type: integer
          minimum: 0
          maximum: 255
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: 255
    add_poolgrpmap_list:
      type: items
      properties:
        MAPPINGNAME:
          name: '映射名称'
          type: string
          minLength: 1
          maxLength: 79
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        POOLGRPNAME:
          name: '地址池组名称'
          type: string
          minLength: 1
          maxLength: 79
          required: true
          description: '已通过**ADD ADDRPOOLGRP**配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        UPFGRPNAME:
          name: 'UPF组名称'
          type: string
          minLength: 1
          maxLength: 32
          required: false
          description: '已通过**ADD ADDRUPGROUP**配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
  examples:
    add_addrpool_list:
    - POOLNAME: 'pool01'
      IPVERSION: IPv4
      POOLTYPE: UDM
      CHECKIPVALID: Enable
      IMSSW: Enable
      IPLEASE: Disable
      OVERLAP: Disable
      RELEASETIME: 10
      SINGLEIPFLAG: Disable
    add_section_list:
    - POOLNAME: 'pool01'
      SECTIONNUM: 1
      IPVERSION: IPv4
      V4STARTIP: '10.0.0.0'
      V4ENDIP: '10.1.2.3'
      V6PREFIXEND: ''
      V6PREFIXLENGTH: ''
      V6PREFIXSTART: ''
    add_addrpoolgrp_list:
    - POOLGRPNAME: 'poolgroup1'
      POOLGRPTYPE: UDM
    add_poolbindgrp_list:
    - POOLGRPNAME: 'poolgroup1'
      POOLNAME: 'pool01'
    add_upnode_list:
    - NFINSTANCENAME: 'UPF_Instance_1'
      ADDRALLOCMODE: INHERIT
    add_addrupgroup_list:
    - UPFGRPNAME: 'upfgroup1'
      UPFGRPTYPE: UDM
    add_upfbindgrp_list:
    - UPFGRPNAME: 'upfgroup1'
      UPFID: 'UPF_Instance_1'
      PRIORITY: 0
    add_poolgrpmap_list:
    - MAPPINGNAME: 'mapping01'
      POOLGRPNAME: 'poolgroup1'
      UPFGRPNAME: 'upfgroup1'
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 进入“MML命令行-UNC”窗口。

### 2 创建本地静态地址地址池。

```jinja2
{%- for item in add_addrpool_list -%}
    ADD ADDRPOOL:
    {#- --- 必选参数 --- -#}
    POOLNAME="{{item.POOLNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.IPVERSION is not none -%}
        IPVERSION={{item.IPVERSION}},
    {%- endif -%}
    {%- if item.POOLTYPE is not none -%}
        POOLTYPE={{item.POOLTYPE}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：POOLTYPE=UDM/Radius 时可选 --- -#}
    {%- if item.POOLTYPE in ['UDM', 'Radius'] -%}
        {%- if item.CHECKIPVALID is not none -%}
            CHECKIPVALID={{item.CHECKIPVALID}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：POOLTYPE=Local 时可选 --- -#}
    {%- if item.POOLTYPE == 'Local' -%}
        {%- if item.IMSSW is not none -%}
            IMSSW={{item.IMSSW}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：POOLTYPE=Local 时可选 --- -#}
    {%- if item.POOLTYPE == 'Local' -%}
        {%- if item.IPLEASE is not none -%}
            IPLEASE={{item.IPLEASE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：POOLTYPE=Local 时可选 --- -#}
    {%- if item.POOLTYPE == 'Local' -%}
        {%- if item.OVERLAP is not none -%}
            OVERLAP={{item.OVERLAP}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：POOLTYPE=Local 时可选 --- -#}
    {%- if item.POOLTYPE == 'Local' -%}
        {%- if item.RELEASETIME is not none -%}
            RELEASETIME={{item.RELEASETIME}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：POOLTYPE=Local 时可选 --- -#}
    {%- if item.POOLTYPE == 'Local' -%}
        {%- if item.SINGLEIPFLAG is not none -%}
            SINGLEIPFLAG={{item.SINGLEIPFLAG}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 配置本地地址池里的地址段。

```jinja2
{%- for item in add_section_list -%}
    ADD SECTION:
    {#- --- 必选参数 --- -#}
    POOLNAME="{{item.POOLNAME}}",
    SECTIONNUM={{item.SECTIONNUM}},
    IPVERSION={{item.IPVERSION}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPVERSION=IPv4 时必选 --- -#}
    {%- if item.IPVERSION == 'IPv4' -%}
        V4STARTIP="{{item.V4STARTIP}}",
    {%- endif -%}
    {#- --- 条件必选：IPVERSION=IPv4 时必选 --- -#}
    {%- if item.IPVERSION == 'IPv4' -%}
        V4ENDIP="{{item.V4ENDIP}}",
    {%- endif -%}
    {#- --- 条件必选：IPVERSION=IPv6 时必选 --- -#}
    {%- if item.IPVERSION == 'IPv6' -%}
        V6PREFIXEND="{{item.V6PREFIXEND}}",
    {%- endif -%}
    {#- --- 条件必选：IPVERSION=IPv6 时必选 --- -#}
    {%- if item.IPVERSION == 'IPv6' -%}
        V6PREFIXLENGTH={{item.V6PREFIXLENGTH}},
    {%- endif -%}
    {#- --- 条件必选：IPVERSION=IPv6 时必选 --- -#}
    {%- if item.IPVERSION == 'IPv6' -%}
        V6PREFIXSTART="{{item.V6PREFIXSTART}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 本地地址池：本地负责分配地址的地址池。本地地址池下需要配置地址段，一个本地地址池最多可以配置64个地址段。

### 配置地址池后，必须配置地址段。如果不配置地址段，将导致用户激活失败。

### 4 配置地址池组名称。

```jinja2
{%- for item in add_addrpoolgrp_list -%}
    ADD ADDRPOOLGRP:
    {#- --- 必选参数 --- -#}
    POOLGRPNAME="{{item.POOLGRPNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.POOLGRPTYPE is not none -%}
        POOLGRPTYPE={{item.POOLGRPTYPE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 5 配置地址池与地址池组绑定。

```jinja2
{%- for item in add_poolbindgrp_list -%}
    ADD POOLBINDGRP:
    {#- --- 必选参数 --- -#}
    POOLGRPNAME="{{item.POOLGRPNAME}}",
    POOLNAME="{{item.POOLNAME}}",
    ;
{%- endfor -%}
```

### 6 配置静态地址用户使用的主、备UPF。

```jinja2
{%- for item in add_upnode_list -%}
    ADD UPNODE:
    {#- --- 必选参数 --- -#}
    NFINSTANCENAME="{{item.NFINSTANCENAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.ADDRALLOCMODE is not none -%}
        ADDRALLOCMODE={{item.ADDRALLOCMODE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 7 配置静态地址用户使用的UPF组。

```jinja2
{%- for item in add_addrupgroup_list -%}
    ADD ADDRUPGROUP:
    {#- --- 必选参数 --- -#}
    UPFGRPNAME="{{item.UPFGRPNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.UPFGRPTYPE is not none -%}
        UPFGRPTYPE={{item.UPFGRPTYPE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 8 配置主、备UPF与UPF组绑定。

```jinja2
{%- for item in add_upfbindgrp_list -%}
    ADD UPFBINDGRP:
    {#- --- 必选参数 --- -#}
    UPFGRPNAME="{{item.UPFGRPNAME}}",
    UPFID="{{item.UPFID}}",
    {#- --- 可选参数 --- -#}
    {%- if item.PRIORITY is not none -%}
        PRIORITY={{item.PRIORITY}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 9 配置地址池组与UPF组绑定。

```jinja2
{%- for item in add_poolgrpmap_list -%}
    ADD POOLGRPMAP:
    {#- --- 必选参数 --- -#}
    MAPPINGNAME="{{item.MAPPINGNAME}}",
    POOLGRPNAME="{{item.POOLGRPNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.UPFGRPNAME is not none -%}
        UPFGRPNAME="{{item.UPFGRPNAME}}",
    {%- endif -%}
    ;
{%- endfor -%}
```


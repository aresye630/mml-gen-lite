---
id: GWFD-020804
name: 配置静态IP地址网段与UPF的绑定
ne_type: UEG
type: feature
description: 可以在本地配置静态IP地址网段与UPF的绑定关系，当用户接入网络时，对静态IP地址用户、Radius分配IP地址用户可以基于配置的网段绑定关系为用户选择指定的UPF。  适用于PGW-C、SMF。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝L","MEC 特性指南（风筝L）","GW-C&SMF特性指南","GWFD-020800 基本业务","GWFD-020804 地址分配方式","配置静态IP地址网段与UPF的绑定"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
可以在本地配置静态IP地址网段与UPF的绑定关系，当用户接入网络时，对静态IP地址用户、Radius分配IP地址用户可以基于配置的网段绑定关系为用户选择指定的UPF。适用于PGW-C、SMF。

## 必备事项
前提条件

* 请仔细阅读GWFD-020804 地址分配方式特性概述。
* 本特性与UEG配合使用生效，要求UEG上配置的用户静态地址网段信息必须在包含在UEG上配置的地址池内，请参考UEG中的**GWFD-010104 地址分配方式**。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    add_cpaddrpool_list:
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
    add_poolbindapn_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
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
    add_cpsection_list:
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
          description: '已通过 **ADD CPADDRPOOL**配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    set_edgesmcommfunc_list:
      type: items
      properties:
        RDSSTATICIPSW:
          name: 'Raidus静态IP功能开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '配置Raidus静态IP功能开关。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_rdsstaticippara_list:
      type: items
      properties:
        IMSI:
          name: '用户IMSI号'
          type: string
          minLength: 5
          maxLength: 15
          required: true
          description: '配置Radius静态IP地址。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        APN:
          name: 'APN名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        ADDRTYPE:
          name: '地址类型'
          type: string
          enum:
          - IPV4
          - IPV6
          - IPV4V6
          - Ethernet
          required: true
          description: ''
          data_source: '对端协商'
          pattern: ''
          default: ''
        IPV4ADDRESS:
          name: '静态IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '对端协商'
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
    add_cppoolgrpmap_list:
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
    add_cpaddrpool_list:
    - POOLNAME: 'pool01'
      IPVERSION: IPv4
      POOLTYPE: UDM
      CHECKIPVALID: Enable
    add_poolbindapn_list:
    - APN: 'huawei.com'
      POOLNAME: 'pool01'
    add_cpsection_list:
    - POOLNAME: 'pool01'
      SECTIONNUM: 1
      IPVERSION: IPv4
      V4STARTIP: '10.0.0.0'
      V4ENDIP: '10.1.2.3'
    add_addrpoolgrp_list:
    - POOLGRPNAME: 'poolgroup1'
      POOLGRPTYPE: UDM
    add_poolbindgrp_list:
    - POOLGRPNAME: 'poolgroup1'
      POOLNAME: 'pool01'
    set_edgesmcommfunc_list:
    - RDSSTATICIPSW: ENABLE
    add_rdsstaticippara_list:
    - IMSI: '123456789012345'
      APN: 'huawei.com'
      ADDRTYPE: IPv4
      IPV4ADDRESS: '192.168.10.10'
    add_upnode_list:
    - NFINSTANCENAME: 'UPF_Instance_1'
      ADDRALLOCMODE: INHERIT
    add_addrupgroup_list:
    - UPFGRPNAME: 'upfgroup1'
      UPFGRPTYPE: UDM
    add_upfbindgrp_list:
    - UPFGRPNAME: 'upfgroup1'
      UPFID: 'UPF_Instance_1'
    add_cppoolgrpmap_list:
    - MAPPINGNAME: 'mapping01'
      POOLGRPNAME: 'poolgroup1'
      UPFGRPNAME: 'upfgroup1'
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 进入“MML命令行-UEG”窗口。

### 2 创建本地静态地址地址池。

```jinja2
{%- for item in add_cpaddrpool_list -%}
    ADD CPADDRPOOL:
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
    ;
{%- endfor -%}
```

### 3 如果需要开启静态地址用户的白名单检查功能，需要配置地址池与APN的绑定关系。接入该APN的静态地址用户激活时，根据用户地址查找对应的地址池，然后根据地址池为用户选择对应的UPF。

```jinja2
{%- for item in add_poolbindapn_list -%}
    ADD POOLBINDAPN:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    POOLNAME="{{item.POOLNAME}}",
    ;
{%- endfor -%}
```

### 4 配置本地地址池里的地址段。

```jinja2
{%- for item in add_cpsection_list -%}
    ADD CPSECTION:
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
    ;
{%- endfor -%}
```

### 本地地址池：本地负责分配地址的地址池。本地地址池下需要配置地址段，一个本地地址池最多可以配置64个地址段。

### 配置地址池后，必须配置地址段。如果不配置地址段，将导致用户激活失败。

### 5 配置地址池组名称。

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

### 6 配置地址池与地址池组绑定。

```jinja2
{%- for item in add_poolbindgrp_list -%}
    ADD POOLBINDGRP:
    {#- --- 必选参数 --- -#}
    POOLGRPNAME="{{item.POOLGRPNAME}}",
    POOLNAME="{{item.POOLNAME}}",
    ;
{%- endfor -%}
```

### 7 （可选）打开Raidus静态IP功能开关。

```jinja2
{%- if is_optional_raidus_static_ip_switch -%}
    {%- for item in set_edgesmcommfunc_list -%}
        SET EDGESMCOMMFUNC:
        {#- --- 可选参数 --- -#}
        {%- if item.RDSSTATICIPSW is not none -%}
            RDSSTATICIPSW={{item.RDSSTATICIPSW}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 8 （可选）配置Radius静态IP地址。

```jinja2
{%- if is_optional_radius_static_ip_address -%}
    {%- for item in add_rdsstaticippara_list -%}
        ADD RDSSTATICIPPARA:
        {#- --- 必选参数 --- -#}
        IMSI="{{item.IMSI}}",
        APN="{{item.APN}}",
        ADDRTYPE={{item.ADDRTYPE}},
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：ADDRTYPE=IPV4/IPV4V6 时可选 --- -#}
        {%- if item.ADDRTYPE in ['IPV4', 'IPV4V6'] -%}
            {%- if item.IPV4ADDRESS is not none -%}
                IPV4ADDRESS="{{item.IPV4ADDRESS}}",
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 当UDM和Radius未向用户分配有效IP地址时，可通过SMF本地配置的IP地址为用户分配地址，此时可以执行步骤7、8。

### 9 配置静态地址用户使用的UPF。

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

### 10 配置静态地址用户使用的UPF组。

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

### 11 配置UPF与UPF组绑定。

```jinja2
{%- for item in add_upfbindgrp_list -%}
    ADD UPFBINDGRP:
    {#- --- 必选参数 --- -#}
    UPFGRPNAME="{{item.UPFGRPNAME}}",
    UPFID="{{item.UPFID}}",
    ;
{%- endfor -%}
```

### 12 配置地址池组与UPF组绑定。

```jinja2
{%- for item in add_cppoolgrpmap_list -%}
    ADD CPPOOLGRPMAP:
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

### 会话建立流程中，当静态IP地址网段绑定的UPF与SMF选择的主锚点UPF不一致时，优先使用SMF选择的主锚点UPF建立会话。

### 如果已有会话的主锚点UPF与静态IP地址绑定的UPF不一致时，可以根据**SET STATICADDRPARA**命令中的开关配置时间扫描会话去活。


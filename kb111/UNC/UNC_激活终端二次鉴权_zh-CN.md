---
id: ''
name: 激活终端二次鉴权
ne_type: UNC
type: feature
description: 需要使用终端二次鉴权时，进行终端二次鉴权激活。  适用于SMF。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","MEC解决方案","WSFD-108007 终端二次鉴权","激活终端二次鉴权"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
需要使用终端二次鉴权时，进行终端二次鉴权激活。适用于SMF。

## 必备事项
前提条件

* 请仔细阅读二次鉴权特性概述。
* 完成Radius鉴权接入配置。
* 完成Radius功能配置。

  **UPLIST4RDS**、**UPFRDSCLIENTIP**、**UPFRDSSVR**命令配置中的**UPLISTNAME**参数建议统一用小写。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    add_uplogicintf_list:
      type: items
      properties:
        UPFINSTANCEID:
          name: 'UPFINSTANCEID'
          type: string
          minLength: 0
          maxLength: 36
          required: true
          description: '指定UPF实例标识。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        ITFTYPE:
          name: 'ITFTYPE'
          type: string
          enum:
          - S1U
          - N4U
          - S11U
          - GNU
          - S2AU
          - S2BU
          - N3
          - N9C
          - N9A
          - S5SU
          - S8SU
          - S5PU
          - S8PU
          - GPU
          required: true
          description: '指定逻辑接口类型。'
          data_source: ''
          pattern: ''
          default: ''
        NETWORKINSTNAME:
          name: 'NETWORKINSTNAME'
          type: string
          minLength: 1
          maxLength: 128
          required: true
          description: '指定网络实例名称。'
          data_source: ''
          pattern: ''
          default: ''
        IPVERSION:
          name: 'IPVERSION'
          type: string
          enum:
          - IPV4V6
          - IPV4
          - IPV6
          required: true
          description: '指定IP地址类型。'
          data_source: ''
          pattern: ''
          default: ''
        CPN4UIPTYPE:
          name: 'CPN4UIPTYPE'
          type: string
          enum:
          - IPV4_PRIOR
          - ACCORDING_PEER
          required: false
          description: '当需要基于指定的NETWORKINSTNAME建立GTP-U隧道时，需将此参数配置为ACCORDING\_PEER。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_cpgtpuaddr_list:
      type: items
      properties:
        IPVERSION:
          name: 'IPVERSION'
          type: string
          enum:
          - IPV4
          - IPV6
          required: true
          description: '指定IP地址类型。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV4ADDR:
          name: 'IPV4ADDR'
          type: string
          maxLength: 15
          required: false
          description: '用于指定与UPF对接的本端GTP-U IPv4地址。(该参数在"IPVERSION"配置为"IPV4"时为条件必选参数。)  本特性中该参数取值是与UPF共同规划，是由SMF下发的分装GTPU报文的IP地址。'
          data_source: ''
          pattern: ''
          default: ''
        VPN:
          name: 'VPN'
          type: string
          minLength: 1
          maxLength: 31
          required: false
          description: '指定与UPF对接的本端GTP-U接口的VPN名称。'
          data_source: ''
          pattern: ''
          default: '_public_'
        IPV6ADDR:
          name: 'IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_uplist4rds_list:
      type: items
      properties:
        UPLISTNAME:
          name: 'UPLISTNAME'
          type: string
          maxLength: 63
          required: true
          description: 'UP列表名称，用于指定UP列表名称。  取值范围：字符串类型，输入长度范围为1～63。长度1到63的非空格字符串。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        UPINSTANCEID:
          name: 'UPINSTANCEID'
          type: string
          maxLength: 36
          required: true
          description: 'UP实例标识，用于指定UP实例标识。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_rdsupfctrl_list:
      type: items
      properties:
        UPLISTNAME:
          name: 'UP列表名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        UPINSTANCEID:
          name: 'UP实例标识'
          type: string
          minLength: 1
          maxLength: 36
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PREFERENCE:
          name: '优先级'
          type: integer
          minimum: 0
          maximum: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LOCKED:
          name: '锁定'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_upfrdssvr_list:
      type: items
      properties:
        SERVERTYPE:
          name: 'SERVERTYPE'
          type: string
          enum:
          - AUTHENTICATION
          - ACCOUNTING
          required: true
          description: '指定RADIUS服务器类型。  取值范围：   * “AUTHENTICATION（鉴权服务器）”：表示鉴权服务器。 * “ACCOUNTING（计费服务器）”：表示计费服务器。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPVERSION:
          name: '服务器IP版本'
          type: string
          enum:
          - IPV4
          - IPV6
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SERVERIPV4:
          name: 'SERVERIPV4'
          type: string
          maxLength: 15
          required: false
          description: 'RADIUS服务器IPv4地址。DN-AAA的IP地址。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        UPLISTNAME:
          name: 'UP列表名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SERVERIPV6:
          name: 'IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_upfrdsclientip_list:
      type: items
      properties:
        CLIENTYPE:
          name: 'CLIENTYPE'
          type: string
          enum:
          - AUTHENTICATION
          - ACCOUNTING
          - ACCT_AND_AUTH
          required: true
          description: '指定RADIUS客户端类型。  取值范围：   * “AUTHENTICATION（鉴权客户端）”：表示鉴权客户端。 * “ACCOUNTING（计费客户端）”：表示计费客户端。 * “ACCT\_AND\_AUTH（计费和鉴权客户端）”：表示计费和鉴权客户端。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPVERSION:
          name: '客户端IP版本'
          type: string
          enum:
          - IPV4
          - IPV6
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        UPLISTNAME:
          name: 'UP列表名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VPNINSTANCE:
          name: 'VPNINSTANCE'
          type: string
          minLength: 1
          maxLength: 31
          required: false
          description: '指定VPN实例。本参数由UPF和DN-AAA共同规划，是UPF与DN-AAA对接的VPN。  取值范围：字符串类型，输入长度范围是1~31。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        CLIENTIPV4:
          name: 'CLIENTIPV4'
          type: string
          maxLength: 15
          required: false
          description: '用于指定RADIUS客户端IPv4地址。SMF下发至UPF，经UPF转发的ClientIP。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        CLIENTIPV6:
          name: 'IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    add_uplogicintf_list:
    - UPFINSTANCEID: 'up1'
      ITFTYPE: N4U
      NETWORKINSTNAME: 'n4u-vpn'
      IPVERSION: IPV4
      CPN4UIPTYPE: ACCORDING_PEER
    add_cpgtpuaddr_list:
    - IPVERSION: IPV4
      IPV4ADDR: '192.168.0.20'
      VPN: 'n4u-vpn'
      IPV6ADDR: ''
    add_uplist4rds_list:
    - UPLISTNAME: 'uplist1'
      UPINSTANCEID: 'up1'
    add_rdsupfctrl_list:
    - UPLISTNAME: 'uplist1'
      UPINSTANCEID: 'up1'
      PREFERENCE: 1
      LOCKED: ENABLE
    add_upfrdssvr_list:
    - SERVERTYPE: AUTHENTICATION
      IPVERSION: IPV4
      SERVERIPV4: '192.168.10.2'
      UPLISTNAME: 'uplist1'
      SERVERIPV6: ''
    add_upfrdsclientip_list:
    - CLIENTYPE: AUTHENTICATION
      IPVERSION: IPV4
      UPLISTNAME: 'uplist1'
      VPNINSTANCE: 'vpnInstance1'
      CLIENTIPV4: '192.168.10.1'
      CLIENTIPV6: ''
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 进入“MML命令行-UNC”窗口。

### 2 可选：当SMF存在多个本端GTP-U地址，增加UPF逻辑接口。

```jinja2
{%- if is_optional_add_upf_logic_interface -%}
    {%- for item in add_uplogicintf_list -%}
        ADD UPLOGICINTF:
        {#- --- 必选参数 --- -#}
        UPFINSTANCEID="{{item.UPFINSTANCEID}}",
        ITFTYPE={{item.ITFTYPE}},
        NETWORKINSTNAME="{{item.NETWORKINSTNAME}}",
        IPVERSION={{item.IPVERSION}},
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：ITFTYPE=N4U 时可选 --- -#}
        {%- if item.ITFTYPE == 'N4U' -%}
            {%- if item.CPN4UIPTYPE is not none -%}
                CPN4UIPTYPE={{item.CPN4UIPTYPE}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 3 增加与UPF对接的本端GTP-U地址。

```jinja2
{%- for item in add_cpgtpuaddr_list -%}
    ADD CPGTPUADDR:
    {#- --- 必选参数 --- -#}
    IPVERSION={{item.IPVERSION}},
    {#- --- 可选参数 --- -#}
    {%- if item.VPN is not none -%}
        VPN="{{item.VPN}}",
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPVERSION=IPV4 时必选 --- -#}
    {%- if item.IPVERSION == 'IPV4' -%}
        IPV4ADDR="{{item.IPV4ADDR}}",
    {%- endif -%}
    {#- --- 条件必选：IPVERSION=IPV6 时必选 --- -#}
    {%- if item.IPVERSION == 'IPV6' -%}
        IPV6ADDR="{{item.IPV6ADDR}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 增加中转使用的UP到RADIUS服务器使用的UPF列表。

```jinja2
{%- for item in add_uplist4rds_list -%}
    ADD UPLIST4RDS:
    {#- --- 必选参数 --- -#}
    UPLISTNAME="{{item.UPLISTNAME}}",
    UPINSTANCEID="{{item.UPINSTANCEID}}",
    ;
{%- endfor -%}
```

### 5 可选配置：增加RADIUS服务器使用的UPF列表中指定UPF的功能属性。

```jinja2
{%- if is_optional_add_upf_function_attribute -%}
    {%- for item in add_rdsupfctrl_list -%}
        ADD RDSUPFCTRL:
        {#- --- 必选参数 --- -#}
        UPLISTNAME="{{item.UPLISTNAME}}",
        UPINSTANCEID="{{item.UPINSTANCEID}}",
        PREFERENCE={{item.PREFERENCE}},
        LOCKED={{item.LOCKED}},
        ;
    {%- endfor -%}
{%- endif -%}
```

### 6 新增中转UPF与Radius服务器的绑定关系。

```jinja2
{%- for item in add_upfrdssvr_list -%}
    ADD UPFRDSSVR:
    {#- --- 必选参数 --- -#}
    SERVERTYPE={{item.SERVERTYPE}},
    IPVERSION={{item.IPVERSION}},
    UPLISTNAME="{{item.UPLISTNAME}}",
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPVERSION=IPV4 时必选 --- -#}
    {%- if item.IPVERSION == 'IPV4' -%}
        SERVERIPV4="{{item.SERVERIPV4}}",
    {%- endif -%}
    {#- --- 条件必选：IPVERSION=IPV6 时必选 --- -#}
    {%- if item.IPVERSION == 'IPV6' -%}
        SERVERIPV6="{{item.SERVERIPV6}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 7 增加中转UPF与Radius客户端的绑定关系。

```jinja2
{%- for item in add_upfrdsclientip_list -%}
    ADD UPFRDSCLIENTIP:
    {#- --- 必选参数 --- -#}
    CLIENTYPE={{item.CLIENTYPE}},
    IPVERSION={{item.IPVERSION}},
    UPLISTNAME="{{item.UPLISTNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.VPNINSTANCE is not none -%}
        VPNINSTANCE="{{item.VPNINSTANCE}}",
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPVERSION=IPV4 时必选 --- -#}
    {%- if item.IPVERSION == 'IPV4' -%}
        CLIENTIPV4="{{item.CLIENTIPV4}}",
    {%- endif -%}
    {#- --- 条件必选：IPVERSION=IPV6 时必选 --- -#}
    {%- if item.IPVERSION == 'IPV6' -%}
        CLIENTIPV6="{{item.CLIENTIPV6}}",
    {%- endif -%}
    ;
{%- endfor -%}
```


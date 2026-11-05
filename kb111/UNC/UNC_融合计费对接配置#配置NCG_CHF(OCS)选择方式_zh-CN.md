---
id: ''
name: 配置NCG/CHF(OCS)选择方式
ne_type: UNC
type: feature
description: 当UNC部署融合计费功能时需要对接NCG/CHF（OCS），本指导用于描述对接NCG/CHF（OCS）的配置操作过程。  UNC支持基于IMSI选择NCG/CHF(OCS)、基于IMSI号段选择NCG/CHF(OCS)、基于PCF下发的FQDN选择NCG/CHF(OCS)、基于用户的计费属性Charging Characteristics（CC）选择NCG/CHF(OCS)，也支持基于标准化服务发现选择NCG/CHF(OCS)。  UNC选择NCG/CHF(OCS)的优先级从高到低依次是：基于IMSI选择NCG/CHF(OCS) > 基于IMSI号段选择NCG/CHF(OCS) > 基于PCF下发的信息选择NCG/CHF(OCS) > 基于从UDM获取的签约CC选择NCG/CHF(OCS) > 基于标准化服务发现选择NCG/CHF(OCS) > 基于SMF本地配置的CC选择NCG/CHF(OCS)。如果无法通过高优先级的方式选择NCG/CHF(OCS)，则依次向下使用低一级别的方式进行选择。  其中，通过**ADD SELCHFGBYIMSI**命令配置基于IMSI选择NCG/CHF(OCS)方式一般用于测试场景，将指定IMSI的用户的计费信息发送到指定NCG/CHF(OCS)上，测试NCG/CHF(OCS)的基本功能。  * 当通过NRF服务发现NCG/CHF（OCS），不需要在UNC上配置NCG/CHF（OCS）。通过本地NRF方式发现NCG/CHF（OCS）操作参考UNC产品文档的“网络部署 > 初始配置 > UNC初始配置与调测 > 组网对接配置 > 配置SMF&PGW-C&SGW-C&GGSN > 配置SMF > 配置和NF直连”中的配置到CHF的数据完成相关配置。 * 如果已参考UNC产品文档的“网络部署 > 初始配置 > UNC初始配置与调测 > 组网对接配置 > 配置SMF&PGW-C&SGW-C&GGSN > 公共配置 > （可选）配置到计费系统和策略控制网元的对接（Ga/Gy/N40/Gx/N7） > （可选）配置到CHF的数据（GGSN/PGW-C/SMF）”完成相关配置，则无需再执行本来章节。
risk_level: ''
doc_source: ["网络部署","业务专题","5G Core 计费解决方案","计费解决方案概述","计费方案部署与调测","方案五：部署NCG且融合接口计费组网方案","SMF配置","融合计费配置","融合计费对接配置","配置NCG/CHF(OCS)选择方式"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
当UNC部署融合计费功能时需要对接NCG/CHF（OCS），本指导用于描述对接NCG/CHF（OCS）的配置操作过程。UNC支持基于IMSI选择NCG/CHF(OCS)、基于IMSI号段选择NCG/CHF(OCS)、基于PCF下发的FQDN选择NCG/CHF(OCS)、基于用户的计费属性Charging Characteristics（CC）选择NCG/CHF(OCS)，也支持基于标准化服务发现选择NCG/CHF(OCS)。UNC选择NCG/CHF(OCS)的优先级从高到低依次是：基于IMSI选择NCG/CHF(OCS) > 基于IMSI号段选择NCG/CHF(OCS) > 基于PCF下发的信息选择NCG/CHF(OCS) > 基于从UDM获取的签约CC选择NCG/CHF(OCS) > 基于标准化服务发现选择NCG/CHF(OCS) > 基于SMF本地配置的CC选择NCG/CHF(OCS)。如果无法通过高优先级的方式选择NCG/CHF(OCS)，则依次向下使用低一级别的方式进行选择。其中，通过**ADD SELCHFGBYIMSI**命令配置基于IMSI选择NCG/CHF(OCS)方式一般用于测试场景，将指定IMSI的用户的计费信息发送到指定NCG/CHF(OCS)上，测试NCG/CHF(OCS)的基本功能。* 当通过NRF服务发现NCG/CHF（OCS），不需要在UNC上配置NCG/CHF（OCS）。通过本地NRF方式发现NCG/CHF（OCS）操作参考UNC产品文档的“网络部署 > 初始配置 > UNC初始配置与调测 > 组网对接配置 > 配置SMF&PGW-C&SGW-C&GGSN > 配置SMF > 配置和NF直连”中的配置到CHF的数据完成相关配置。* 如果已参考UNC产品文档的“网络部署 > 初始配置 > UNC初始配置与调测 > 组网对接配置 > 配置SMF&PGW-C&SGW-C&GGSN > 公共配置 > （可选）配置到计费系统和策略控制网元的对接（Ga/Gy/N40/Gx/N7） > （可选）配置到CHF的数据（GGSN/PGW-C/SMF）”完成相关配置，则无需再执行本来章节。

## 必备事项
前提条件

* 请仔细阅读融合计费原理。
* 完成加载License。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    add_tnfins_list:
      type: items
      properties:
        TNFINSINDEX:
          name: '目标NF实例索引'
          type: integer
          minimum: 0
          maximum: 2047
          required: true
          description: '增加主备NCG/CHF(OCS)。  “FQDN”要与PCF下发的FQDN名称保持一致。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        TNFTYPE:
          name: '目标NF类型'
          type: string
          enum:
          - CHF
          - UPF
          - PCSCF
          - PCF
          required: true
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
        TNFINSNAME:
          name: '目标NF实例名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        SCHEMA:
          name: '协议模式'
          type: string
          enum:
          - UriSchemeINVALID
          - http
          - https
          - UriSchemeMAX
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        FQDN:
          name: '域名'
          type: string
          minLength: 0
          maxLength: 127
          required: false
          description: ''
          data_source: '从对端获取'
          pattern: ''
          default: ''
    add_tnfinsip_list:
      type: items
      properties:
        TNFINSINDEX:
          name: '目标NF实例索引'
          type: integer
          minimum: 0
          maximum: 2047
          required: true
          description: '增加主备NCG/CHF(OCS)的IP地址。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPTYPE:
          name: 'IP地址类型'
          type: string
          enum:
          - IPV4
          - IPV6
          - NONEIP
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV4ADDR:
          name: 'IPV4类型地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PORT:
          name: '端口号'
          type: integer
          minimum: 1
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6ADDR:
          name: 'IPV6类型地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_tnfgrp_list:
      type: items
      properties:
        TNFGRPINDEX:
          name: '目标NF组索引'
          type: integer
          minimum: 0
          maximum: 511
          required: true
          description: '配置NCG/CHF(OCS) 组。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        TNFTYPE:
          name: '目标NF类型'
          type: string
          enum:
          - CHF
          - UPF
          - PCSCF
          - PCF
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        TNFGRPNAME:
          name: '目标NF组名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_tnfbindgrp_list:
      type: items
      properties:
        TNFGRPINDEX:
          name: '目标NF组索引'
          type: integer
          minimum: 0
          maximum: 511
          required: true
          description: '将NCG/CHF(OCS)实例绑定到NCG/CHF(OCS)组上。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        TNFINSINDEX:
          name: '目标NF实例索引'
          type: integer
          minimum: 0
          maximum: 2047
          required: true
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    set_chfselectmode_list:
      type: items
      properties:
        FIRSTMODE:
          name: '首选模式'
          type: string
          enum:
          - MODE3GPP
          - PCF
          - NRF
          - LOCAL
          required: true
          description: '设置用户激活和在线恢复场景NCG/CHF(OCS)的选择模式。  说明：  此示例首选模式为使用本地配置的NCG/CHF(OCS)，此时没有备选模式。如果首选模式为使用PCF指定的NCG/CHF(OCS)或者使用NRF发现的NCG/CHF(OCS)时，可以配置备选模式。  请根据业务实际需要进行配置。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        SECONDMODE:
          name: '备选模式'
          type: string
          enum:
          - NRF
          - LOCAL
          - NOCONFIG
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_glbdftchfgroup_list:
      type: items
      properties:
        PRIMARYCHFGRP:
          name: '主CHF组'
          type: string
          minLength: 1
          maxLength: 63
          required: false
          description: '配置系统缺省的NCG/CHF(OCS)组。建议配置缺省的NCG/CHF(OCS)组，避免选择不到NCG/CHF(OCS)。  说明：  “PRIMARYCHFGRP”和“SECONDARYCHFGRP”使用**ADD TNFGRP**命令配置生成。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        SECONDARYCHFGRP:
          name: '备CHF组'
          type: string
          minLength: 1
          maxLength: 63
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_selectchfgbycc_list:
      type: items
      properties:
        CCTYPE:
          name: 'Charge Characteristic类型'
          type: string
          enum:
          - DEFAULT
          - VALUE
          required: true
          description: '配置计费属性和NCG/CHF(OCS)组的关联关系，基于计费属性选择使用的NCG/CHF(OCS)组。  说明：  * “PRIORITY”数值越小，优先级越高。 * “PRIMARYCHFGRP”和“SECONDARYCHFGRP”使用**ADD TNFGRP**命令配置生成。 * 本示例以计费属性0x0100举例，请根据业务实际需要进行配置。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        CCVALUE:
          name: 'Charge Characteristic值'
          type: string
          minLength: 1
          maxLength: 6
          required: false
          description: ''
          data_source: '已配置数据中获取/从对端获取'
          pattern: ''
          default: ''
        MASK:
          name: 'Charge Characteristic特定值掩码'
          type: string
          minLength: 1
          maxLength: 6
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        PRIORITY:
          name: 'Charge Characteristic优先级'
          type: integer
          minimum: 1
          maximum: 65535
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        PRIMARYCHFGRP:
          name: '主CHF组'
          type: string
          minLength: 1
          maxLength: 63
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        SECONDARYCHFGRP:
          name: '备CHF组'
          type: string
          minLength: 1
          maxLength: 63
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_selchfgbimsiseg_list:
      type: items
      properties:
        SEGSTART:
          name: '号段起始字符串'
          type: string
          minLength: 5
          maxLength: 15
          required: true
          description: '(可选)配置号段与和NCG/CHF(OCS)组的关联关系，基于号段选择使用的NCG/CHF(OCS)组。  说明：  * “PRIMARYCHFGRP”和“SECONDARYCHFGRP”使用**ADD TNFGRP**命令配置生成。 * 本示例取值为举例，请根据业务实际需要进行配置。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SEGEND:
          name: '号段结束字符串'
          type: string
          minLength: 5
          maxLength: 15
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        PRIMARYCHFGRP:
          name: '主CHF组'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        SECONDARYCHFGRP:
          name: '备CHF组'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
  examples:
    add_tnfins_list:
    - TNFINSINDEX: 1
      TNFTYPE: CHF
      TNFINSNAME: 'target_chf_0'
      SCHEMA: http
      FQDN: 'chf1.hw.com'
    add_tnfinsip_list:
    - TNFINSINDEX: 1
      IPTYPE: IPV4
      IPV4ADDR: '192.168.94.2'
      PORT: 3220
      IPV6ADDR: ''
    add_tnfgrp_list:
    - TNFGRPINDEX: 1
      TNFTYPE: CHF
      TNFGRPNAME: 'ChfGroup1'
    add_tnfbindgrp_list:
    - TNFGRPINDEX: 1
      TNFINSINDEX: 1
    set_chfselectmode_list:
    - FIRSTMODE: LOCAL
      SECONDMODE: LOCAL
    set_glbdftchfgroup_list:
    - PRIMARYCHFGRP: 'ChfGroup1'
      SECONDARYCHFGRP: 'ChfGroup2'
    add_selectchfgbycc_list:
    - CCTYPE: VALUE
      CCVALUE: '0x0100'
      MASK: '0xFFFF'
      PRIORITY: 1
      PRIMARYCHFGRP: 'ChfGroup1'
      SECONDARYCHFGRP: 'ChfGroup2'
    add_selchfgbimsiseg_list:
    - SEGSTART: '12345678901'
      SEGEND: '12345678905'
      PRIMARYCHFGRP: 'ChfGroup1'
      SECONDARYCHFGRP: 'ChfGroup2'
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 配置目标NCG/CHF(OCS)。

```jinja2
{%- for item in add_tnfins_list -%}
    ADD TNFINS:
    {#- --- 必选参数 --- -#}
    TNFINSINDEX={{item.TNFINSINDEX}},
    TNFTYPE={{item.TNFTYPE}},
    TNFINSNAME="{{item.TNFINSNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.SCHEMA is not none -%}
        SCHEMA={{item.SCHEMA}},
    {%- endif -%}
    {%- if item.FQDN is not none -%}
        FQDN="{{item.FQDN}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 2 配置目标NCG/CHF(OCS)的IP地址信息。

```jinja2
{%- for item in add_tnfinsip_list -%}
    ADD TNFINSIP:
    {#- --- 必选参数 --- -#}
    TNFINSINDEX={{item.TNFINSINDEX}},
    IPTYPE={{item.IPTYPE}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPTYPE=IPV4 时必选 --- -#}
    {%- if item.IPTYPE == 'IPV4' -%}
        IPV4ADDR="{{item.IPV4ADDR}}",
    {%- endif -%}
    {#- --- 条件必选：IPTYPE=IPV6 时必选 --- -#}
    {%- if item.IPTYPE == 'IPV6' -%}
        IPV6ADDR="{{item.IPV6ADDR}}",
    {%- endif -%}
    {#- --- 条件必选/可选参数 --- -#}
    {#- --- 端口号: 条件必选(IP地址类型=NONEIP) / 条件可选(IP地址类型=IPV4|IPV6) --- -#}
    {%- if (item.IPTYPE == 'NONEIP') -%}
        PORT={{item.PORT}},
    {%- elif (item.IPTYPE in ['IPV4', 'IPV6']) -%}
        {%- if item.PORT is not none -%}
            PORT={{item.PORT}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 配置NCG/CHF(OCS)组。

```jinja2
{%- for item in add_tnfgrp_list -%}
    ADD TNFGRP:
    {#- --- 必选参数 --- -#}
    TNFGRPINDEX={{item.TNFGRPINDEX}},
    TNFTYPE={{item.TNFTYPE}},
    TNFGRPNAME="{{item.TNFGRPNAME}}",
    ;
{%- endfor -%}
```

### 4 将目标NCG/CHF(OCS)绑定到NCG/CHF(OCS)组。

```jinja2
{%- for item in add_tnfbindgrp_list -%}
    ADD TNFBINDGRP:
    {#- --- 必选参数 --- -#}
    TNFGRPINDEX={{item.TNFGRPINDEX}},
    TNFINSINDEX={{item.TNFINSINDEX}},
    ;
{%- endfor -%}
```

### 5 设置用户激活和在线恢复场景NCG/CHF(OCS)的选择模式。

```jinja2
{%- for item in set_chfselectmode_list -%}
    SET CHFSELECTMODE:
    {#- --- 必选参数 --- -#}
    FIRSTMODE={{item.FIRSTMODE}},
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：FIRSTMODE=PCF/NRF 时可选 --- -#}
    {%- if item.FIRSTMODE in ['PCF', 'NRF'] -%}
        {%- if item.SECONDMODE is not none -%}
            SECONDMODE={{item.SECONDMODE}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 6 配置系统缺省的NCG/CHF(OCS)组。

```jinja2
{%- for item in set_glbdftchfgroup_list -%}
    SET GLBDFTCHFGROUP:
    {#- --- 可选参数 --- -#}
    {%- if item.PRIMARYCHFGRP is not none -%}
        PRIMARYCHFGRP="{{item.PRIMARYCHFGRP}}",
    {%- endif -%}
    {%- if item.SECONDARYCHFGRP is not none -%}
        SECONDARYCHFGRP="{{item.SECONDARYCHFGRP}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 7 配置计费属性和NCG/CHF(OCS)组的关联关系，基于计费属性选择使用的NCG/CHF(OCS)组。

```jinja2
{%- for item in add_selectchfgbycc_list -%}
    ADD SELECTCHFGBYCC:
    {#- --- 必选参数 --- -#}
    CCTYPE={{item.CCTYPE}},
    {#- --- 可选参数 --- -#}
    {%- if item.PRIMARYCHFGRP is not none -%}
        PRIMARYCHFGRP="{{item.PRIMARYCHFGRP}}",
    {%- endif -%}
    {%- if item.SECONDARYCHFGRP is not none -%}
        SECONDARYCHFGRP="{{item.SECONDARYCHFGRP}}",
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：CCTYPE=VALUE 时必选 --- -#}
    {%- if item.CCTYPE == 'VALUE' -%}
        CCVALUE="{{item.CCVALUE}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：CCTYPE=VALUE 时可选 --- -#}
    {%- if item.CCTYPE == 'VALUE' -%}
        {%- if item.MASK is not none -%}
            MASK="{{item.MASK}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：CCTYPE=VALUE 时可选 --- -#}
    {%- if item.CCTYPE == 'VALUE' -%}
        {%- if item.PRIORITY is not none -%}
            PRIORITY={{item.PRIORITY}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 8 配置号段与和NCG/CHF(OCS)组的关联关系，基于号段选择使用的NCG/CHF(OCS)组。

```jinja2
{%- for item in add_selchfgbimsiseg_list -%}
    ADD SELCHFGBIMSISEG:
    {#- --- 必选参数 --- -#}
    SEGSTART="{{item.SEGSTART}}",
    SEGEND="{{item.SEGEND}}",
    {#- --- 可选参数 --- -#}
    {%- if item.PRIMARYCHFGRP is not none -%}
        PRIMARYCHFGRP="{{item.PRIMARYCHFGRP}}",
    {%- endif -%}
    {%- if item.SECONDARYCHFGRP is not none -%}
        SECONDARYCHFGRP="{{item.SECONDARYCHFGRP}}",
    {%- endif -%}
    ;
{%- endfor -%}
```


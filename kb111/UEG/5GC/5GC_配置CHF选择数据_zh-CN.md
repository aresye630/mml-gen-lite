---
id: ''
name: 配置CHF选择数据
ne_type: UEG
type: feature
description: 应急SMF不对接大网CHF，但是应急SMF的缓存数据功能是在CHF故障场景下的可靠性机制，在不配置CHF场景下用户不能进行业务，因此，本章节完成SMF本地配置对接虚拟的CHF，SMF支持基于SMF本地配置的CC选择CHF。  适用于SMF。
tags: []
risk_level: ''
doc_source: ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（火电专网，入驻式）","部署配置指导","子园区部署入驻式UEG-M","配置业务数据（风筝M）","配置业务数据（UEG）","计费功能配置","部署应急SMF","配置CHF选择数据"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
应急SMF不对接大网CHF，但是应急SMF的缓存数据功能是在CHF故障场景下的可靠性机制，在不配置CHF场景下用户不能进行业务，因此，本章节完成SMF本地配置对接虚拟的CHF，SMF支持基于SMF本地配置的CC选择CHF。适用于SMF。

## 必备事项
前提条件

* 请仔细阅读融合计费原理。
* 完成加载License。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
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
          description: '增加主备CHF实例。'
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
          description: '-'
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
          data_source: ''
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
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        FQDN:
          name: '域名'
          type: string
          minLength: 0
          maxLength: 127
          required: false
          description: '-'
          data_source: '本端规划'
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
          description: '增加主备CHF实例的IP地址。'
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
    add_tnfgrp_list:
      type: items
      properties:
        TNFGRPINDEX:
          name: '目标NF组索引'
          type: integer
          minimum: 0
          maximum: 511
          required: true
          description: '配置CHF Group。'
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
          description: '将CHF实例绑定到CHF组上。'
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
          description: '配置CC和CHF Group的关联关系。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        CCVALUE:
          name: 'Charge Characteristic值'
          type: string
          minLength: 1
          maxLength: 6
          required: false
          description: '* 本地CC时，从已配置数据中**ADD CHARGECHAR**的拜访用户计费属性获取。 * 从UDM获取签约CC时，从对端获取。'
          data_source: '已配置数据中获取/从对端获取'
          pattern: ''
          default: ''
        MASK:
          name: 'Charge Characteristic特定值掩码'
          type: string
          minLength: 1
          maxLength: 6
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PRIORITY:
          name: 'Charge Characteristic优先级'
          type: integer
          minimum: 1
          maximum: 65535
          required: false
          description: '数值越小，优先级越高。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        PRIMARYCHFGRP:
          name: '主CHF组'
          type: string
          minLength: 1
          maxLength: 63
          required: false
          description: '-'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        SECONDARYCHFGRP:
          name: '备CHF组'
          type: string
          minLength: 1
          maxLength: 63
          required: false
          description: '-'
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
    add_tnfgrp_list:
    - TNFGRPINDEX: 1
      TNFTYPE: CHF
      TNFGRPNAME: 'ChfGroup1'
    add_tnfbindgrp_list:
    - TNFGRPINDEX: 1
      TNFINSINDEX: 1
    add_selectchfgbycc_list:
    - CCTYPE: VALUE
      CCVALUE: '0x1111'
      MASK: '0xffff'
      PRIORITY: 2
      PRIMARYCHFGRP: 'ChfGroup1'
      SECONDARYCHFGRP: 'ChfGroup2'
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 配置计费属性。计费属性信息都能从UDM获取时，请跳过该步骤。

### 请参见配置计费属性CC。

### 2 配置CHF Group。

#### 2.1 配置目标CHF实例。

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

#### 2.2 配置目标CHF实例的IP地址信息。

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

#### 2.3 配置CHF组。

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

#### 2.4 将目标CHF绑定到CHF组。

```jinja2
{%- for item in add_tnfbindgrp_list -%}
    ADD TNFBINDGRP:
    {#- --- 必选参数 --- -#}
    TNFGRPINDEX={{item.TNFGRPINDEX}},
    TNFINSINDEX={{item.TNFINSINDEX}},
    ;
{%- endfor -%}
```

### 3 配置基于CC选择CHF组。

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


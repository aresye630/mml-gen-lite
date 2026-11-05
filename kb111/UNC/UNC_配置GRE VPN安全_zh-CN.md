---
id: ''
name: 配置GRE VPN安全
ne_type: UNC
type: feature
description: 采用GRE VPN方案时，使能识别关键字、端到端报文验证、Keepalive功能，提升数据传输安全性。
risk_level: ''
doc_source: ["网络部署","安全配置","UNC安全配置","安全配置建议","可选配置","网络安全配置","配置网络隔离功能","配置GRE VPN安全"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
采用GRE VPN方案时，使能识别关键字、端到端报文验证、Keepalive功能，提升数据传输安全性。

## 必备事项
前提条件

请仔细阅读VPN。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    add_gretunnel_list:
      type: items
      properties:
        TNLNAME:
          name: '隧道名称'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TNLTYPE:
          name: '隧道类型'
          type: string
          enum:
          - gre
          - gre6
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SRCTYPE:
          name: 'IPv4源类型'
          type: string
          enum:
          - if_name
          - ip_address
          - no_type
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: no_type
        SRCIPADDR:
          name: '源IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DSTIPADDR:
          name: '目的IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        KEEPALVEN:
          name: '使能Keepalive功能'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        GREKEYEN:
          name: '使能识别关键字功能'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        GREKEY:
          name: '识别关键字'
          type: string
          maxLength: 268
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CHECKSUMEN:
          name: '使能端到端校验功能'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        KEEPALVPERIOD:
          name: 'Keepalive报文发送周期'
          type: integer
          minimum: 1
          maximum: 32767
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 5
        KEEPALVRETRYCNT:
          name: '不可达计数器参数'
          type: integer
          minimum: 1
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 3
        SRCIFNAME:
          name: '源接口名称'
          type: string
          maxLength: 63
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DSTIPV6ADDR:
          name: '目的IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        REDUNDANCYEN:
          name: '使能备份隧道功能'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        SRCTYPE6:
          name: 'IPv6源类型'
          type: string
          enum:
          - if_name
          - ip_address
          - no_type
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: no_type
  examples:
    add_gretunnel_list:
    - TNLNAME: '隧道名称'
      TNLTYPE: 隧道类型
      SRCTYPE: 源类型
      SRCIPADDR: '源IP地址'
      DSTIPADDR: '目的IP地址'
      KEEPALVEN: TRUE
      GREKEYEN: TRUE
      GREKEY: '识别关键字'
      CHECKSUMEN: TRUE
      KEEPALVPERIOD: 5
      KEEPALVRETRYCNT: 3
      SRCIFNAME: ''
      DSTIPV6ADDR: ''
      REDUNDANCYEN: FALSE
      SRCTYPE6: no_type
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 配置GRE隧道，并使能识别关键字功能、Keepalive功能、端到端校验功能。

### 在“MML命令行-UNC”窗口上执行：

```jinja2
{%- for item in add_gretunnel_list -%}
    ADD GRETUNNEL:
    {#- --- 必选参数 --- -#}
    TNLNAME="{{item.TNLNAME}}",
    TNLTYPE={{item.TNLTYPE}},
    {#- --- 可选参数 --- -#}
    {%- if item.KEEPALVEN is not none -%}
        KEEPALVEN={{item.KEEPALVEN}},
    {%- endif -%}
    {%- if item.GREKEYEN is not none -%}
        GREKEYEN={{item.GREKEYEN}},
    {%- endif -%}
    {%- if item.CHECKSUMEN is not none -%}
        CHECKSUMEN={{item.CHECKSUMEN}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：TNLTYPE=gre 时必选 --- -#}
    {%- if item.TNLTYPE == 'gre' -%}
        SRCTYPE={{item.SRCTYPE}},
    {%- endif -%}
    {#- --- 条件必选：SRCTYPE=ip_address 时必选 --- -#}
    {%- if item.SRCTYPE == 'ip_address' -%}
        SRCIPADDR="{{item.SRCIPADDR}}",
    {%- endif -%}
    {#- --- 条件必选：GREKEYEN=TRUE 时必选 --- -#}
    {%- if item.GREKEYEN == 'TRUE' -%}
        GREKEY="{{item.GREKEY}}",
    {%- endif -%}
    {#- --- 条件必选：SRCTYPE=if_name 时必选 --- -#}
    {%- if item.SRCTYPE == 'if_name' -%}
        SRCIFNAME="{{item.SRCIFNAME}}",
    {#- --- 条件必选：SRCTYPE6=if_name 时必选 --- -#}
    {%- elif item.SRCTYPE6 == 'if_name' -%}
        SRCIFNAME="{{item.SRCIFNAME}}",
    {%- endif -%}
    {#- --- 条件必选：TNLTYPE=gre6 时必选 --- -#}
    {%- if item.TNLTYPE == 'gre6' -%}
        SRCTYPE6={{item.SRCTYPE6}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：TNLTYPE=gre 时可选 --- -#}
    {%- if item.TNLTYPE == 'gre' -%}
        {%- if item.DSTIPADDR is not none -%}
            DSTIPADDR="{{item.DSTIPADDR}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：TNLTYPE=gre6 时可选 --- -#}
    {%- if item.TNLTYPE == 'gre6' -%}
        {%- if item.DSTIPV6ADDR is not none -%}
            DSTIPV6ADDR="{{item.DSTIPV6ADDR}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：KEEPALVEN=TRUE 时可选 --- -#}
    {%- if item.KEEPALVEN == 'TRUE' -%}
        {%- if item.KEEPALVPERIOD is not none -%}
            KEEPALVPERIOD={{item.KEEPALVPERIOD}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：KEEPALVEN=TRUE 时可选 --- -#}
    {%- if item.KEEPALVEN == 'TRUE' -%}
        {%- if item.KEEPALVRETRYCNT is not none -%}
            KEEPALVRETRYCNT={{item.KEEPALVRETRYCNT}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：TNLTYPE=gre/gre6 时可选 --- -#}
    {%- if item.TNLTYPE in ['gre', 'gre6'] -%}
        {%- if item.REDUNDANCYEN is not none -%}
            REDUNDANCYEN={{item.REDUNDANCYEN}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```


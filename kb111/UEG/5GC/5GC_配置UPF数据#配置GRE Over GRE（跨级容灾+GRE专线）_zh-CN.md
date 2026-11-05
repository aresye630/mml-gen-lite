---
id: ''
name: 配置GRE Over GRE（跨级容灾+GRE专线）
ne_type: UEG
type: feature
description: 跨级容灾场景下，当地市与园区之间通过GRE专线打通，且存在静态地址路由冗余情况下，从主锚点UPF2看，存在GRE over GRE（外层GRE专线中有GRE路由冗余隧道）的情况，需要将内层GRE路由冗余隧道的报文路由到外层的GRE专线中，组网规划如图1所示，数据规划如图2所示。  **图1** 组网图  **图2** 数据规划图
tags: []
risk_level: ''
doc_source: ["专网（仅连接，园区入驻式）","业务发放","5GC toB DNN业务发放（专网，入驻式）","通过OMC发放","UEG虚机容器","DNN发放操作","发放入驻式UPF+GRE专线","入驻式UPF+GRE专线+主锚点UPF（跨级）+主备+静态签约地址（GRE冗余备份）","配置数据","配置UPF数据","配置GRE Over GRE（跨级容灾+GRE专线）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
跨级容灾场景下，当地市与园区之间通过GRE专线打通，且存在静态地址路由冗余情况下，从主锚点UPF2看，存在GRE over GRE（外层GRE专线中有GRE路由冗余隧道）的情况，需要将内层GRE路由冗余隧道的报文路由到外层的GRE专线中，组网规划如图1所示，数据规划如图2所示。**图1** 组网图**图2** 数据规划图

## 必备事项
前提条件

无。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    add_srroute_list:
      type: items
      properties:
        AFTYPE:
          name: '地址族'
          type: string
          enum:
          - ipv4unicast
          required: true
          description: '增加静态路由，使得内层的GRE路由冗余隧道的报文路由到外层的GRE专线中。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        PREFIX:
          name: '路由前缀'
          type: string
          maxLength: 15
          required: true
          description: '内层GRE路由冗余隧道UPF1侧GRE地址。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        MASKLENGTH:
          name: '路由掩码长度'
          type: integer
          minimum: 0
          maximum: 32
          required: true
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: false
          description: '-'
          data_source: '从已配置数据中获取'
          pattern: ''
          default: '_public_'
        DESTVRFNAME:
          name: '下一跳VPN名字'
          type: string
          maxLength: 31
          required: false
          description: '-'
          data_source: '从已配置数据中获取'
          pattern: ''
          default: ''
        IFNAME:
          name: '路由出接口名字'
          type: string
          maxLength: 63
          required: false
          description: '外层GRE专线UPF2侧隧道接口。'
          data_source: '从已配置数据中获取'
          pattern: ''
          default: ''
  examples:
    add_srroute_list:
    - AFTYPE: ipv4unicast
      PREFIX: '10.10.0.1'
      MASKLENGTH: 32
      VRFNAME: 'VRF_N6_Local_2B'
      DESTVRFNAME: 'VRF_N6_Local_2B_001'
      IFNAME: 'Tunnel12'
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 配置静态路由。

```jinja2
{%- for item in add_srroute_list -%}
    ADD SRROUTE:
    {#- --- 必选参数 --- -#}
    AFTYPE={{item.AFTYPE}},
    PREFIX="{{item.PREFIX}}",
    MASKLENGTH={{item.MASKLENGTH}},
    {#- --- 可选参数 --- -#}
    {%- if item.VRFNAME is not none -%}
        VRFNAME="{{item.VRFNAME}}",
    {%- endif -%}
    {%- if item.DESTVRFNAME is not none -%}
        DESTVRFNAME="{{item.DESTVRFNAME}}",
    {%- endif -%}
    {%- if item.IFNAME is not none -%}
        IFNAME="{{item.IFNAME}}",
    {%- endif -%}
    ;
{%- endfor -%}
```


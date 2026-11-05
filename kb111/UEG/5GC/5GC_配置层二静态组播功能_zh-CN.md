---
id: GWFD-030705
name: 配置层二静态组播功能
ne_type: UEG
type: feature
description: 5G LAN业务存在静态组播业务时，请参考本页面配置静态组播功能。  UPF收到组播报文后，根据5G LAN组ID+组播目的MAC匹配组播组，匹配到静态组播组后，根据配置的静态组播组及静态组播组成员的映射关系建立层二组播转发表项，控制组播数据报文仅在该组播组内转发。  仅适用于层二5G LAN场景。
tags: []
risk_level: ''
doc_source: ["原子能力&行业场景","原子能力","5GC toB 原子能力-5G LAN","特性指南","UEG特性指南","可选功能","GWFD-030705 支持层二静态组播","配置层二静态组播功能"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
5G LAN业务存在静态组播业务时，请参考本页面配置静态组播功能。UPF收到组播报文后，根据5G LAN组ID+组播目的MAC匹配组播组，匹配到静态组播组后，根据配置的静态组播组及静态组播组成员的映射关系建立层二组播转发表项，控制组播数据报文仅在该组播组内转发。仅适用于层二5G LAN场景。

## 必备事项
前提条件

* 已完成配置5G LAN基本功能。
* 完成**加载License**（如果有需求，请联系华为技术支持工程师处理）。
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
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SWITCH:
          name: '开关'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_multicastgrp_list:
      type: items
      properties:
        MCASTGRPNAME:
          name: '组播组名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '5G LAN终端发送组播报文时，报文中的目的MAC必须与此处配置的组播MAC一致。  UPF收到该目的MAC的报文，则认为是组播报文，会向该组播组内的所有成员转发该组播报文。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        MCASTMACADDR:
          name: '组播MAC地址'
          type: string
          minLength: 0
          maxLength: 17
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_ngbindmcastgrp_list:
      type: items
      properties:
        VNINSTANCE:
          name: '5G LAN实例名称'
          type: string
          minLength: 0
          maxLength: 37
          required: true
          description: '采用**ADD NGVNINSTANCE**命令定义的VNINSTANCE。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        MCASTGRPNAME:
          name: '组播组名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '采用**ADD MULTICASTGRP**命令定义的MCASTGRPNAME。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_mcastgrpmem_list:
      type: items
      properties:
        MCASTGRPNAME:
          name: '组播组名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '采用**ADD MULTICASTGRP**命令定义的组播组名称。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        MEMTYPE:
          name: '成员类型'
          type: string
          enum:
          - IMSI
          - VTEP
          - DFSRPAIR
          - ETHERNETPDN
          required: false
          description: '根据局点需要，规划组播组成员类型。'
          data_source: '本端规划'
          pattern: ''
          default: IMSI
        IMSI:
          name: 'IMSI'
          type: string
          minLength: 0
          maxLength: 16
          required: false
          description: '“MEMTYPE”设置为“IMSI”时需要规划。  静态组播组成员的IMSI。一个IMSI可以加入多个组播组。  IMSI长度范围1～15，每个字符必须为0~9的数字。'
          data_source: '与对端协商'
          pattern: ''
          default: ''
        VTEPNAME:
          name: 'VXLAN隧道端点名称'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: '采用**ADD VTEP**命令定义的“VTEPNAME”。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV3G5L2SMUL'
      SWITCH: ENABLE
    add_multicastgrp_list:
    - MCASTGRPNAME: 'MCASTGRP01'
      MCASTMACADDR: '11-11-11-11-11-fc'
    add_ngbindmcastgrp_list:
    - VNINSTANCE: '000003e9-460-08-01'
      MCASTGRPNAME: 'MCASTGRP01'
    add_mcastgrpmem_list:
    - MCASTGRPNAME: 'MCASTGRP01'
      MEMTYPE: IMSI
      IMSI: '460123123456789'
      VTEPNAME: 'VTEP1'
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 打开本特性的License配置开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

### 2 增加静态组播组。

```jinja2
{%- for item in add_multicastgrp_list -%}
    ADD MULTICASTGRP:
    {#- --- 必选参数 --- -#}
    MCASTGRPNAME="{{item.MCASTGRPNAME}}",
    MCASTMACADDR="{{item.MCASTMACADDR}}",
    ;
{%- endfor -%}
```

### 3 配置静态组播组和5G LAN组的绑定关系。

```jinja2
{%- for item in add_ngbindmcastgrp_list -%}
    ADD NGBINDMCASTGRP:
    {#- --- 必选参数 --- -#}
    VNINSTANCE="{{item.VNINSTANCE}}",
    MCASTGRPNAME="{{item.MCASTGRPNAME}}",
    ;
{%- endfor -%}
```

### 4 增加静态组播组成员。

```jinja2
{%- for item in add_mcastgrpmem_list -%}
    ADD MCASTGRPMEM:
    {#- --- 必选参数 --- -#}
    MCASTGRPNAME="{{item.MCASTGRPNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.MEMTYPE is not none -%}
        MEMTYPE={{item.MEMTYPE}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：MEMTYPE=IMSI 时必选 --- -#}
    {%- if item.MEMTYPE == 'IMSI' -%}
        IMSI="{{item.IMSI}}",
    {%- endif -%}
    {#- --- 条件必选：MEMTYPE=VTEP 时必选 --- -#}
    {%- if item.MEMTYPE == 'VTEP' -%}
        VTEPNAME="{{item.VTEPNAME}}",
    {%- endif -%}
    ;
{%- endfor -%}
```


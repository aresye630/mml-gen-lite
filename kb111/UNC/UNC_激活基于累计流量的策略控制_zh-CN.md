---
id: ''
name: 激活基于累计流量的策略控制
ne_type: UNC
type: feature
description: 为了保证用户公平使用流量，需要配置基于会话级的累计流量的策略控制。  * PGW-C/SMF与PCF之间通过N7接口交互时，会话级的累计流量仅需在PCF上进行配置，本端PGW-C/SMF不需要专有配置。 * GGSN/PGW-C与PCRF之间通过Gx接口交互时，需要参考本页面进行配置。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","智能PCC解决方案","WSFD-109104 基于累计流量的策略控制","激活基于累计流量的策略控制"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
为了保证用户公平使用流量，需要配置基于会话级的累计流量的策略控制。* PGW-C/SMF与PCF之间通过N7接口交互时，会话级的累计流量仅需在PCF上进行配置，本端PGW-C/SMF不需要专有配置。* GGSN/PGW-C与PCRF之间通过Gx接口交互时，需要参考本页面进行配置。

## 必备事项
前提条件

前提条件

* 请仔细阅读WSFD-109104 基于累计流量的策略控制。
* 请仔细阅读PCC基本功能（2G/3G/4G，基于Gx接口）。
* 完成激活PCC基本功能。
* 完成加载License（如果有需求，请联系华为技术支持工程师处理）。
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
    set_pccfunc_list:
      type: items
      properties:
        MKPARSEFORMAT:
          name: 'Monitoring-Key的解析方式'
          type: string
          enum:
          - ASCII
          - SELFADAPT
          - UNSIGNED32
          required: false
          description: '该参数需要与PCRF保持一致。'
          data_source: '与对端协商'
          pattern: ''
          default: ''
    mod_pcrf_list:
      type: items
      properties:
        HOSTNAME:
          name: 'PCRF主机名'
          type: string
          maxLength: 127
          required: true
          description: '使用**ADD PCRF**定义的PCRF主机名。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        SUPFEANEGOSW:
          name: 'Supported-Features动态协商开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '使用样例值。'
          data_source: '与对端协商'
          pattern: ''
          default: ''
        FEATURELIST:
          name: 'Feature列表'
          type: string
          required: false
          description: 'PCRF需要支持UMCH功能。'
          data_source: '与对端协商'
          pattern: ''
          default: ''
        CARRYSUPFEASW:
          name: 'Supported-Feature AVP携带开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_pccpolicygrp_list:
      type: items
      properties:
        PCCPOLICYGRPNM:
          name: 'PCC策略组名称'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        FUPSESSIONEXC:
          name: 'Session级FUP累计标识'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV3W9PCBT12'
      SWITCH: ENABLE
    set_pccfunc_list:
    - MKPARSEFORMAT: UNSIGNED32
    mod_pcrf_list:
    - HOSTNAME: 'pcrf_01'
      SUPFEANEGOSW: ENABLE
      FEATURELIST: UMCH-1
      CARRYSUPFEASW: ''
    add_pccpolicygrp_list:
    - PCCPOLICYGRPNM: 'pccpolicygrp_01'
      FUPSESSIONEXC: ENABLE
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 进入“MML命令行-UNC”窗口。

### 2 打开本特性的License配置开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

### 3 设置累计流量的上报方式。

```jinja2
{%- for item in set_pccfunc_list -%}
    SET PCCFUNC:
    {#- --- 可选参数 --- -#}
    {%- if item.MKPARSEFORMAT is not none -%}
        MKPARSEFORMAT={{item.MKPARSEFORMAT}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 与PCRF通过Gx接口交互时，使能流量监控拥塞处理（UMCH）功能。

```jinja2
{%- for item in mod_pcrf_list -%}
    MOD PCRF:
    {#- --- 必选参数 --- -#}
    HOSTNAME="{{item.HOSTNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.SUPFEANEGOSW is not none -%}
        SUPFEANEGOSW={{item.SUPFEANEGOSW}},
    {%- endif -%}
    {%- if item.FEATURELIST is not none -%}
        FEATURELIST={{item.FEATURELIST}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：SUPFEANEGOSW=DISABLE 时可选 --- -#}
    {%- if item.SUPFEANEGOSW == 'DISABLE' -%}
        {%- if item.CARRYSUPFEASW is not none -%}
            CARRYSUPFEASW={{item.CARRYSUPFEASW}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 5 配置将某类业务/应用的流量不统计到会话级流量。

```jinja2
{%- for item in add_pccpolicygrp_list -%}
    ADD PCCPOLICYGRP:
    {#- --- 必选参数 --- -#}
    PCCPOLICYGRPNM="{{item.PCCPOLICYGRPNM}}",
    {#- --- 可选参数 --- -#}
    {%- if item.FUPSESSIONEXC is not none -%}
        FUPSESSIONEXC={{item.FUPSESSIONEXC}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### “Session级FUP累计标识（FUPSESSIONEXC）”默认值为“DISABLE”，表示该PCC策略组对应的业务计入Session级流量。


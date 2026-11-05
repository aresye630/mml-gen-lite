---
id: ''
name: 激活基于服务区域的SMF选择特性
ne_type: UNC
type: feature
description: 本操作指导介绍在运行网络中激活基于服务区域的SMF选择操作过程。  适用于AMF。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","网关选择功能","WSFD-205010 基于服务区域的SMF选择","激活基于服务区域的SMF选择特性"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本操作指导介绍在运行网络中激活基于服务区域的SMF选择操作过程。适用于AMF。

## 必备事项
前提条件

* 请仔细阅读WSFD-205010 基于服务区域的SMF选择特性概述。
* SMF已规划和配置完成对应支持的servingScope，UNC中的配置命令为**ADD NFSRVSCOPE**。
* 完成加载License。
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
    add_dnngrp_list:
      type: items
      properties:
        DNNGRPID:
          name: 'DNN群组标识'
          type: string
          minLength: 1
          maxLength: 32
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        DESC:
          name: '描述信息'
          type: string
          minLength: 0
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_dnngrpmem_list:
      type: items
      properties:
        DNNGRPID:
          name: 'DNN群组标识'
          type: string
          minLength: 1
          maxLength: 32
          required: true
          description: '已经通过**ADD DNNGRP**配置。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        DNN:
          name: 'DNN'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_smfselplcy_list:
      type: items
      properties:
        SUBRANGE:
          name: '用户范围'
          type: string
          enum:
          - ALL_USER
          - HOME_USER
          - FOREIGN_USER
          - IMSI_PREFIX
          required: true
          description: '本地SMF重选策略。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        DNNGRPID:
          name: 'DNN群组标识'
          type: string
          minLength: 1
          maxLength: 32
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        SSSW:
          name: '是否携带Serving Scope'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        SERVINGSCOPE:
          name: '服务范围'
          type: string
          minLength: 0
          maxLength: 64
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        IMSIPRE:
          name: 'IMSI前缀'
          type: string
          minLength: 5
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LOCDISCOPTSW:
          name: '本地服务发现SMF调优开关'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV2SDSC01'
      SWITCH: ENABLE
    add_dnngrp_list:
    - DNNGRPID: 'GRP_DNN1'
      DESC: 'for SMF Selection'
    add_dnngrpmem_list:
    - DNNGRPID: 'GRP_DNN1'
      DNN: 'Huawei1'
    add_smfselplcy_list:
    - SUBRANGE: HOME_USER
      DNNGRPID: 'GRP_DNN1'
      SSSW: YES
      SERVINGSCOPE: 'A'
      IMSIPRE: ''
      LOCDISCOPTSW: ''
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

### 3 配置相同策略的SMF选择的DNN。

```jinja2
{%- for item in add_dnngrp_list -%}
    ADD DNNGRP:
    {#- --- 必选参数 --- -#}
    DNNGRPID="{{item.DNNGRPID}}",
    {#- --- 可选参数 --- -#}
    {%- if item.DESC is not none -%}
        DESC="{{item.DESC}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_dnngrpmem_list -%}
    ADD DNNGRPMEM:
    {#- --- 必选参数 --- -#}
    DNNGRPID="{{item.DNNGRPID}}",
    DNN="{{item.DNN}}",
    ;
{%- endfor -%}
```

### 4 针对DNN群组对应的本网用户进行特定服务范围的SMF选择。

```jinja2
{%- for item in add_smfselplcy_list -%}
    ADD SMFSELPLCY:
    {#- --- 必选参数 --- -#}
    SUBRANGE={{item.SUBRANGE}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：SSSW=YES 时必选 --- -#}
    {%- if item.SSSW == 'YES' -%}
        DNNGRPID="{{item.DNNGRPID}}",
    {%- endif -%}
    {#- --- 条件必选：SUBRANGE=IMSI_PREFIX 时必选 --- -#}
    {%- if item.SUBRANGE == 'IMSI_PREFIX' -%}
        IMSIPRE="{{item.IMSIPRE}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：SUBRANGE=ALL_USER/HOME_USER/FOREIGN_USER/IMSI_PREFIX 时可选 --- -#}
    {%- if item.SUBRANGE in ['ALL_USER', 'HOME_USER', 'FOREIGN_USER', 'IMSI_PREFIX'] -%}
        {%- if item.SSSW is not none -%}
            SSSW={{item.SSSW}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SSSW=YES 时可选 --- -#}
    {%- if item.SSSW == 'YES' -%}
        {%- if item.SERVINGSCOPE is not none -%}
            SERVINGSCOPE="{{item.SERVINGSCOPE}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SUBRANGE=IMSI_PREFIX 时可选 --- -#}
    {%- if item.SUBRANGE == 'IMSI_PREFIX' -%}
        {%- if item.LOCDISCOPTSW is not none -%}
            LOCDISCOPTSW={{item.LOCDISCOPTSW}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```


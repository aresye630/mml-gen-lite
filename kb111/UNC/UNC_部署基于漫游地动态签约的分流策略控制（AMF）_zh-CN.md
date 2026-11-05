---
id: ''
name: 部署基于漫游地动态签约的分流策略控制（AMF）
ne_type: UNC
type: feature
description: 本操作用于指导配置本地专网业务场景下AMF侧对接入用户范围的控制机制以及本地专网业务DNN判断机制的过程。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","MEC解决方案","WSFD-223003 基于漫游地动态签约的分流策略控制","特性部署","部署基于漫游地动态签约的分流策略控制（AMF）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本操作用于指导配置本地专网业务场景下AMF侧对接入用户范围的控制机制以及本地专网业务DNN判断机制的过程。

## 必备事项
前提条件

* 请仔细阅读WSFD-223003 基于漫游地动态签约的分流策略控制特性概述。
* 已完成本特性License加载，可以通过**DSP LICENSE**命令查询确认，如果本特性的License在查询列表中可见，即可认为本特性License已加载成功。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    add_ngusrgrp_list:
      type: items
      properties:
        USRGRPID:
          name: '用户群组标识'
          type: integer
          minimum: 0
          maximum: 4294967294
          required: true
          description: '配置专网业务适用的用户群标识。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        DESC:
          name: '描述信息'
          type: string
          minLength: 0
          maxLength: 32
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_ngusrgrpmem_list:
      type: items
      properties:
        USRGRPID:
          name: '用户群组标识'
          type: integer
          minimum: 0
          maximum: 4294967294
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        IMSIPRE:
          name: 'IMSI前缀'
          type: string
          minLength: 5
          maxLength: 15
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        DESC:
          name: '描述信息'
          type: string
          minLength: 0
          maxLength: 32
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_amueplcyctrl_list:
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
          - MSISDN_PREFIX
          required: true
          description: '配置AM策略。'
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
          data_source: '全网规划'
          pattern: ''
          default: ''
        ISUEASSOC:
          name: '是否建立UE策略偶联'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NO
        ISAMASSOC:
          name: '是否建立AM策略偶联'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: NO
        MSISDNPRE:
          name: 'MSISDN前缀'
          type: string
          minLength: 1
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NSGRPID:
          name: '网络切片群组标识'
          type: integer
          minimum: 0
          maximum: 16
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 0
    add_pcfselplcy_list:
      type: items
      properties:
        SUBRANGE:
          name: '用户范围'
          type: string
          enum:
          - ALL_USER
          - HOME_USER
          - FOREIGN_USER
          - USER_GROUP
          - IMSI_PREFIX
          required: true
          description: '配置AM-PCF的选择策略。USRGRPID参数需要通过命令**ADD NGUSRGRP**预先配置好。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        USRGRPID:
          name: '用户群组标识'
          type: integer
          minimum: 0
          maximum: 4294967294
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        CTRLMODE:
          name: '控制模式'
          type: string
          enum:
          - WHITELIST
          - BLACKLIST
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
        DESC:
          name: '描述信息'
          type: string
          minLength: 0
          maxLength: 32
          required: false
          description: ''
          data_source: '本端规划'
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
    add_allowdnn_list:
      type: items
      properties:
        REQDNN:
          name: 'UE请求DNN'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '配置允许进行专网业务的DNN。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        REPLDNN:
          name: 'PDU会话替换DNN'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    add_ngusrgrp_list:
    - USRGRPID: 20
      DESC: 'for roaming user'
    add_ngusrgrpmem_list:
    - USRGRPID: 20
      IMSIPRE: '123456'
      DESC: 'for roaming user'
    add_amueplcyctrl_list:
    - SUBRANGE: IMSI_PREFIX
      IMSIPRE: '123456'
      ISUEASSOC: YES
      ISAMASSOC: YES
      MSISDNPRE: ''
      NSGRPID: ''
    add_pcfselplcy_list:
    - SUBRANGE: USER_GROUP
      USRGRPID: 20
      CTRLMODE: WHITELIST
      SSSW: YES
      SERVINGSCOPE: 'YES'
      DESC: 'for roaming user'
      IMSIPRE: ''
    add_allowdnn_list:
    - REQDNN: 'Huawei.com'
      REPLDNN: 'dnn-ar'
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 //配置专网业务适用的用户群。

```jinja2
{%- for item in add_ngusrgrp_list -%}
    ADD NGUSRGRP:
    {#- --- 必选参数 --- -#}
    USRGRPID={{item.USRGRPID}},
    {#- --- 可选参数 --- -#}
    {%- if item.DESC is not none -%}
        DESC="{{item.DESC}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_ngusrgrpmem_list -%}
    ADD NGUSRGRPMEM:
    {#- --- 必选参数 --- -#}
    USRGRPID={{item.USRGRPID}},
    IMSIPRE="{{item.IMSIPRE}}",
    {#- --- 可选参数 --- -#}
    {%- if item.DESC is not none -%}
        DESC="{{item.DESC}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 2 //配置用户群的AM策略。

```jinja2
{%- for item in add_amueplcyctrl_list -%}
    ADD AMUEPLCYCTRL:
    {#- --- 必选参数 --- -#}
    SUBRANGE={{item.SUBRANGE}},
    {#- --- 可选参数 --- -#}
    {%- if item.ISUEASSOC is not none -%}
        ISUEASSOC={{item.ISUEASSOC}},
    {%- endif -%}
    {%- if item.ISAMASSOC is not none -%}
        ISAMASSOC={{item.ISAMASSOC}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：SUBRANGE=IMSI_PREFIX 时必选 --- -#}
    {%- if item.SUBRANGE == 'IMSI_PREFIX' -%}
        IMSIPRE="{{item.IMSIPRE}}",
    {%- endif -%}
    {#- --- 条件必选：SUBRANGE=MSISDN_PREFIX 时必选 --- -#}
    {%- if item.SUBRANGE == 'MSISDN_PREFIX' -%}
        MSISDNPRE="{{item.MSISDNPRE}}",
    {%- endif -%}
    {#- --- 条件必选：SUBRANGE=ALL_USER 时必选 --- -#}
    {%- if item.SUBRANGE == 'ALL_USER' -%}
        NSGRPID={{item.NSGRPID}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 //配置AM-PCF的选择策略。

```jinja2
{%- for item in add_pcfselplcy_list -%}
    ADD PCFSELPLCY:
    {#- --- 必选参数 --- -#}
    SUBRANGE={{item.SUBRANGE}},
    {#- --- 可选参数 --- -#}
    {%- if item.DESC is not none -%}
        DESC="{{item.DESC}}",
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：SUBRANGE=USER_GROUP 时必选 --- -#}
    {%- if item.SUBRANGE == 'USER_GROUP' -%}
        USRGRPID={{item.USRGRPID}},
    {%- endif -%}
    {#- --- 条件必选：SUBRANGE=USER_GROUP/IMSI_PREFIX 时必选 --- -#}
    {%- if item.SUBRANGE in ['USER_GROUP', 'IMSI_PREFIX'] -%}
        CTRLMODE={{item.CTRLMODE}},
    {%- endif -%}
    {#- --- 条件必选：SUBRANGE=IMSI_PREFIX 时必选 --- -#}
    {%- if item.SUBRANGE == 'IMSI_PREFIX' -%}
        IMSIPRE="{{item.IMSIPRE}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：SUBRANGE=USER_GROUP/IMSI_PREFIX 时可选 --- -#}
    {%- if item.SUBRANGE in ['USER_GROUP', 'IMSI_PREFIX'] -%}
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
    ;
{%- endfor -%}
```

### 4 //配置允许进行专网业务的DNN。

```jinja2
{%- for item in add_allowdnn_list -%}
    ADD ALLOWDNN:
    {#- --- 必选参数 --- -#}
    REQDNN="{{item.REQDNN}}",
    REPLDNN="{{item.REPLDNN}}",
    ;
{%- endfor -%}
```


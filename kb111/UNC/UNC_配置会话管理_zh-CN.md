---
id: ''
name: 配置会话管理
ne_type: UNC
type: feature
description: 本操作指导介绍在运行网络中配置会话管理特性的操作过程。  会话管理功能是MME的基本功能，是用户与外部PDN建立连接，进行数据业务的基础。MME的会话管理功能包括网络侧发起的会话管理和UE发起的会话管理。
risk_level: ''
doc_source: ["网络部署","初始配置","UNC初始配置与调测","组网对接配置","配置AMF&MME&SGSN","配置MME","配置会话管理"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本操作指导介绍在运行网络中配置会话管理特性的操作过程。会话管理功能是MME的基本功能，是用户与外部PDN建立连接，进行数据业务的基础。MME的会话管理功能包括网络侧发起的会话管理和UE发起的会话管理。

## 必备事项
前提条件

前提条件

* 具备管理员权限的操作人员已经登录华为操作维护系统（登录U2020客户端或登录OM Portal）。

* UNC软件安装已完成。

* EPS网络中各网元系统及操作维护台运行正常。
* 用户在HSS中已签约EPS业务。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    set_esm_list:
      type: items
      properties:
        T3485:
          name: 'T3485（s）'
          type: integer
          minimum: 1
          maximum: 86400
          required: false
          description: '此命令中的所有参数均有系统初始值，如果用户使用初始值，就不必执行此命令  当使用NB-IoT业务时，需通过****SET NBESM****来配置会话管理。'
          data_source: '参见“水平网设LLD文档 ”。'
          pattern: ''
          default: ''
        N3485:
          name: 'N3485（times）'
          type: integer
          minimum: 0
          maximum: 5
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        T3486:
          name: 'T3486（s）'
          type: integer
          minimum: 1
          maximum: 86400
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        N3486:
          name: 'N3486（times）'
          type: integer
          minimum: 0
          maximum: 5
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        T3489:
          name: 'T3489（s）'
          type: integer
          minimum: 1
          maximum: 86400
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        N3489:
          name: 'N3489（times）'
          type: integer
          minimum: 0
          maximum: 5
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        T3495:
          name: 'T3495（s）'
          type: integer
          minimum: 1
          maximum: 86400
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        N3495:
          name: 'N3495（times）'
          type: integer
          minimum: 0
          maximum: 5
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TSAEBRSETUP:
          name: 'SAE承载建立定时器（s）'
          type: integer
          minimum: 0
          maximum: 30
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TSAEBRMOD:
          name: 'SAE承载修改定时器（s）'
          type: integer
          minimum: 0
          maximum: 30
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TSAEBRREL:
          name: 'SAE承载释放定时器（s）'
          type: integer
          minimum: 0
          maximum: 30
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_smfunc_list:
      type: items
      properties:
        INDFWD:
          name: '强制启动间接转发方式'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: '设置会话管理扩展功能。'
          data_source: ''
          pattern: ''
          default: ''
        TOPSELCFG:
          name: '拓扑选择开关'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        APNRES:
          name: 'APN限制功能开关'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PDPRMD:
          name: 'APN限制的去激活方式'
          type: string
          enum:
          - MAX
          - MIN
          - RANDOM
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PDPTYPE:
          name: 'PDP/PDN Type策略'
          type: string
          enum:
          - IPv4
          - IPv4v6
          - IPv6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DUALFLAG:
          name: 'IPv4v6双栈'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_r8qosmap_list:
      type: items
      properties:
        QCI:
          name: 'QoS级别标识'
          type: integer
          minimum: 1
          maximum: 254
          required: true
          description: '设置EPS QoS参数到Pre-R8 QoS参数映射规则'
          data_source: ''
          pattern: ''
          default: ''
        TC:
          name: '流量等级'
          type: string
          enum:
          - BC
          - CC
          - IC
          - SC
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MAXSDU:
          name: '最大SDU长度'
          type: integer
          minimum: 1
          maximum: 153
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DO:
          name: '发送次序'
          type: string
          enum:
          - NORDER
          - ORDER
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RBER:
          name: '保留BER'
          type: string
          enum:
          - E_RESIDUAL_BIT_ERR_RATIO_1
          - E_RESIDUAL_BIT_ERR_RATIO_2
          - E_RESIDUAL_BIT_ERR_RATIO_3
          - E_RESIDUAL_BIT_ERR_RATIO_4
          - E_RESIDUAL_BIT_ERR_RATIO_5
          - E_RESIDUAL_BIT_ERR_RATIO_6
          - E_RESIDUAL_BIT_ERR_RATIO_7
          - E_RESIDUAL_BIT_ERR_RATIO_8
          - E_RESIDUAL_BIT_ERR_RATIO_9
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DESDU:
          name: '发送错误SDU'
          type: string
          enum:
          - ERR_SDU_DELIVERED
          - ERR_SDU_NOT_DELIVERED
          - NOT_DETECT
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SDUER:
          name: 'SDU误码率'
          type: string
          enum:
          - SDUER1
          - SDUER2
          - SDUER3
          - SDUER4
          - SDUER5
          - SDUER6
          - SDUER7
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TD:
          name: '传递时延'
          type: integer
          minimum: 1
          maximum: 62
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        THPRI:
          name: '发送控制优先级'
          type: string
          enum:
          - THPRI1
          - THPRI2
          - THPRI3
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_compatibility_list:
      type: items
      properties:
        HARP:
          name: 'H值'
          type: integer
          minimum: 1
          maximum: 13
          required: false
          description: '设置QoS兼容性配置。'
          data_source: ''
          pattern: ''
          default: ''
        MARP:
          name: 'M值'
          type: integer
          minimum: 2
          maximum: 14
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    set_esm_list:
    - T3485: 10
      N3485: 3
      T3486: 10
      N3486: 2
      T3489: 10
      N3489: 1
      T3495: 10
      N3495: 3
      TSAEBRSETUP: 10
      TSAEBRMOD: 10
      TSAEBRREL: 10
    set_smfunc_list:
    - INDFWD: YES
      TOPSELCFG: YES
      APNRES: NO
      PDPRMD: MAX
      PDPTYPE: IPv4
      DUALFLAG: ''
    set_r8qosmap_list:
    - QCI: 1
      TC: CC
      MAXSDU: 150
      DO: ORDER
      RBER: E_RESIDUAL_BIT_ERR_RATIO_1
      DESDU: NOT_DETECT
      SDUER: SDUER4
      TD: 10
      THPRI: ''
    set_compatibility_list:
    - HARP: 1
      MARP: 14
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 进入“MML命令行-UNC”窗口。

### 2 **可选：**设置S1模式SM协议参数。

```jinja2
{%- if is_optional_s1_mode_sm_protocol_params -%}
    {%- for item in set_esm_list -%}
        SET ESM:
        {#- --- 可选参数 --- -#}
        {%- if item.T3485 is not none -%}
            T3485={{item.T3485}},
        {%- endif -%}
        {%- if item.N3485 is not none -%}
            N3485={{item.N3485}},
        {%- endif -%}
        {%- if item.T3486 is not none -%}
            T3486={{item.T3486}},
        {%- endif -%}
        {%- if item.N3486 is not none -%}
            N3486={{item.N3486}},
        {%- endif -%}
        {%- if item.T3489 is not none -%}
            T3489={{item.T3489}},
        {%- endif -%}
        {%- if item.N3489 is not none -%}
            N3489={{item.N3489}},
        {%- endif -%}
        {%- if item.T3495 is not none -%}
            T3495={{item.T3495}},
        {%- endif -%}
        {%- if item.N3495 is not none -%}
            N3495={{item.N3495}},
        {%- endif -%}
        {%- if item.TSAEBRSETUP is not none -%}
            TSAEBRSETUP={{item.TSAEBRSETUP}},
        {%- endif -%}
        {%- if item.TSAEBRMOD is not none -%}
            TSAEBRMOD={{item.TSAEBRMOD}},
        {%- endif -%}
        {%- if item.TSAEBRREL is not none -%}
            TSAEBRREL={{item.TSAEBRREL}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 3 **可选：**设置会话管理扩展功能。

```jinja2
{%- if is_optional_session_management_ext_funcs -%}
    {%- for item in set_smfunc_list -%}
        SET SMFUNC:
        {#- --- 可选参数 --- -#}
        {%- if item.INDFWD is not none -%}
            INDFWD={{item.INDFWD}},
        {%- endif -%}
        {%- if item.TOPSELCFG is not none -%}
            TOPSELCFG={{item.TOPSELCFG}},
        {%- endif -%}
        {%- if item.APNRES is not none -%}
            APNRES={{item.APNRES}},
        {%- endif -%}
        {%- if item.PDPRMD is not none -%}
            PDPRMD={{item.PDPRMD}},
        {%- endif -%}
        {%- if item.DUALFLAG is not none -%}
            DUALFLAG={{item.DUALFLAG}},
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：DUALFLAG=NO 时可选 --- -#}
        {%- if item.DUALFLAG == 'NO' -%}
            {%- if item.PDPTYPE is not none -%}
                PDPTYPE={{item.PDPTYPE}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 4 **可选：**设置EPS QoS参数到Pre-R8 QoS参数映射规则。

```jinja2
{%- if is_optional_eps_qos_prer8_mapping_rules -%}
    {%- for item in set_r8qosmap_list -%}
        SET R8QOSMAP:
        {#- --- 必选参数 --- -#}
        QCI={{item.QCI}},
        {#- --- 可选参数 --- -#}
        {%- if item.TC is not none -%}
            TC={{item.TC}},
        {%- endif -%}
        {%- if item.MAXSDU is not none -%}
            MAXSDU={{item.MAXSDU}},
        {%- endif -%}
        {%- if item.DO is not none -%}
            DO={{item.DO}},
        {%- endif -%}
        {%- if item.RBER is not none -%}
            RBER={{item.RBER}},
        {%- endif -%}
        {%- if item.DESDU is not none -%}
            DESDU={{item.DESDU}},
        {%- endif -%}
        {%- if item.SDUER is not none -%}
            SDUER={{item.SDUER}},
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：TC=CC/SC 时可选 --- -#}
        {%- if item.TC in ['CC', 'SC'] -%}
            {%- if item.TD is not none -%}
                TD={{item.TD}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：TC=IC 时可选 --- -#}
        {%- if item.TC == 'IC' -%}
            {%- if item.THPRI is not none -%}
                THPRI={{item.THPRI}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 5 **可选：**设置QoS兼容性配置。

```jinja2
{%- if is_optional_qos_compatibility_config -%}
    {%- for item in set_compatibility_list -%}
        SET COMPATIBILITY:
        {#- --- 可选参数 --- -#}
        {%- if item.HARP is not none -%}
            HARP={{item.HARP}},
        {%- endif -%}
        {%- if item.MARP is not none -%}
            MARP={{item.MARP}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```


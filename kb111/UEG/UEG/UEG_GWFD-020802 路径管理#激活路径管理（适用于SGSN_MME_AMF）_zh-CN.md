---
id: GWFD-020802
name: 激活路径管理（适用于SGSN/MME/AMF）
ne_type: UEG
type: feature
description: 本操作指导介绍在运行网络中激活路径管理特性的操作过程。  路径管理是指本端向对端发送相关信令，通过检查对端是否响应的方法来判断路径是否正常，从而及时清除无效路径的一种机制。  适用于SGSN、MME、AMF。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝L","MEC 特性指南（风筝L）","MME特性指南","GWFD-020800 基本业务","GWFD-020802 路径管理","激活路径管理（适用于SGSN/MME/AMF）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
本操作指导介绍在运行网络中激活路径管理特性的操作过程。路径管理是指本端向对端发送相关信令，通过检查对端是否响应的方法来判断路径是否正常，从而及时清除无效路径的一种机制。适用于SGSN、MME、AMF。

## 必备事项
前提条件

请仔细阅读WSFD-010600 路径管理特性概述。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    set_gtppub_list:
      type: items
      properties:
        ECHOSIG:
          name: '发送ECHO Request的路径'
          type: string
          enum:
          - ALL
          - NONE
          - SPECIFIED
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        EI:
          name: '发送Echo请求间隔（s）'
          type: integer
          minimum: 60
          maximum: 3600
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        POTHD:
          name: '路径数过载门限（%）'
          type: integer
          minimum: 0
          maximum: 100
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PNTHD:
          name: '路径数过载恢复（%）'
          type: integer
          minimum: 0
          maximum: 100
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PCTHD:
          name: '路径数拥塞门限（%）'
          type: integer
          minimum: 0
          maximum: 100
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PRTHD:
          name: '路径数拥塞恢复（%）'
          type: integer
          minimum: 0
          maximum: 100
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_t3n3_list:
      type: items
      properties:
        GTPVER:
          name: 'GTP版本'
          type: string
          enum:
          - GTPv0
          - GTPv1
          - GTPv2
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        V0MSGCLS:
          name: 'V0消息分类'
          type: string
          enum:
          - LM
          - MM
          - PM
          - TM
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        V0SPMMSGTYPE:
          name: 'V0 PM消息类型'
          type: string
          enum:
          - ECHO_REQ
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        T3RES:
          name: 'T3-RESPONSE（s）'
          type: integer
          minimum: 1
          maximum: 20
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        N3REQ:
          name: 'N3-REQUEST（times）'
          type: integer
          minimum: 1
          maximum: 6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_ugtp_list:
      type: items
      properties: {}
    add_gtpcpathdp_list:
      type: items
      properties:
        RANGE:
          name: '路径范围'
          type: string
          enum:
          - ROAMING
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PAS_COE:
          name: '故障判定钝化系数'
          type: integer
          minimum: 1
          maximum: 20
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GP_ALMID:
          name: '漫游路径告警ID控制'
          type: string
          enum:
          - COMMON
          - INDEP
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: INDEP
    set_gtpupara_list:
      type: items
      properties:
        GTPUUPECHO:
          name: 'GTPU 上游接口发送Echo信令'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GTPUDNECHO:
          name: 'GTPU下游接口发送Echo信令'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GTPUEI:
          name: 'GTPU路径Echo探测发送间隔'
          type: integer
          minimum: 120
          maximum: 3600
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GTPUT3:
          name: 'GTPU路径的Echo探测的T3 Response时长'
          type: integer
          minimum: 1
          maximum: 20
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GTPUN3:
          name: 'GTPU路径的Echo探测的消息发送次数'
          type: integer
          minimum: 1
          maximum: 6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        POTHD:
          name: '路径数过载门限（%）'
          type: integer
          minimum: 0
          maximum: 100
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PNTHD:
          name: '路径数过载恢复（%）'
          type: integer
          minimum: 0
          maximum: 100
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PCTHD:
          name: '路径数拥塞门限（%）'
          type: integer
          minimum: 0
          maximum: 100
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PRTHD:
          name: '路径数拥塞恢复（%）'
          type: integer
          minimum: 0
          maximum: 100
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_gtpuctrl_list:
      type: items
      properties: {}
    add_gtpupathdp_list:
      type: items
      properties:
        RANGE:
          name: '路径范围'
          type: string
          enum:
          - ROAMING
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PAS_COE:
          name: '故障判定钝化系数'
          type: integer
          minimum: 1
          maximum: 20
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GP_ALMID:
          name: '漫游路径告警ID控制'
          type: string
          enum:
          - COMMON
          - INDEP
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: INDEP
    set_gtpcfuncpara_list:
      type: items
      properties: {}
    add_gtpct3n3_list:
      type: items
      properties:
        NODETYPE:
          name: '网元类型'
          type: string
          enum:
          - SGW
          - PGW
          - GGSN
          - AMF
          - SPGW
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        T3:
          name: '请求消息重发间隔'
          type: integer
          minimum: 1
          maximum: 20
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        N3:
          name: '请求消息发送次数'
          type: integer
          minimum: 1
          maximum: 6
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_gtpcpathmp_list:
      type: items
      properties:
        RANGE:
          name: '路径范围'
          type: string
          enum:
          - E_HOME
          - E_FOREIGN
          - E_SPECI_INTF
          - E_SPECI_IP
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    set_gtppub_list:
    - ECHOSIG: ALL
      EI: 60
      POTHD: 80
      PNTHD: 75
      PCTHD: 90
      PRTHD: 85
    set_t3n3_list:
    - GTPVER: GTPv0
      V0MSGCLS: PM
      V0SPMMSGTYPE: ECHO_REQ
      T3RES: 7
      N3REQ: 2
    set_ugtp_list:
    - {}
    add_gtpcpathdp_list:
    - RANGE: ROAMING
      PAS_COE: 3
      GP_ALMID: INDEP
    set_gtpupara_list:
    - GTPUUPECHO: ON
      GTPUDNECHO: ON
      GTPUEI: 240
      GTPUT3: 6
      GTPUN3: 2
      POTHD: 80
      PNTHD: 75
      PCTHD: 90
      PRTHD: 85
    set_gtpuctrl_list:
    - {}
    add_gtpupathdp_list:
    - RANGE: ROAMING
      PAS_COE: 3
      GP_ALMID: INDEP
    set_gtpcfuncpara_list:
    - {}
    add_gtpct3n3_list:
    - NODETYPE: ''
      T3: ''
      N3: ''
    add_gtpcpathmp_list:
    - RANGE: ''
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 配置SGSN/MME GTP-C路径管理。GTP-C路径是用于在UEG与对端之间传输信令消息的路径。

#### 1.1 配置GTP-C路径管理参数。

```jinja2
{%- for item in set_gtppub_list -%}
    SET GTPPUB:
    {#- --- 可选参数 --- -#}
    {%- if item.ECHOSIG is not none -%}
        ECHOSIG={{item.ECHOSIG}},
    {%- endif -%}
    {%- if item.EI is not none -%}
        EI={{item.EI}},
    {%- endif -%}
    {%- if item.POTHD is not none -%}
        POTHD={{item.POTHD}},
    {%- endif -%}
    {%- if item.PNTHD is not none -%}
        PNTHD={{item.PNTHD}},
    {%- endif -%}
    {%- if item.PCTHD is not none -%}
        PCTHD={{item.PCTHD}},
    {%- endif -%}
    {%- if item.PRTHD is not none -%}
        PRTHD={{item.PRTHD}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 1.2 配置T3N3参数。

```jinja2
{%- for item in set_t3n3_list -%}
    SET T3N3:
    {#- --- 必选参数 --- -#}
    GTPVER={{item.GTPVER}},
    {#- --- 可选参数 --- -#}
    {%- if item.T3RES is not none -%}
        T3RES={{item.T3RES}},
    {%- endif -%}
    {%- if item.N3REQ is not none -%}
        N3REQ={{item.N3REQ}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：GTPVER=GTPv0 时可选 --- -#}
    {%- if item.GTPVER == 'GTPv0' -%}
        {%- if item.V0MSGCLS is not none -%}
            V0MSGCLS={{item.V0MSGCLS}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：V0MSGCLS=PM 时可选 --- -#}
    {%- if item.V0MSGCLS == 'PM' -%}
        {%- if item.V0SPMMSGTYPE is not none -%}
            V0SPMMSGTYPE={{item.V0SPMMSGTYPE}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 1.3 配置GTP信息表中管控GTP-C路径状态的时间参数。 一般不要设置，均存在系统初始设置值。

```jinja2
SET UGTP:
;
```

#### 1.4 配置GTP-C路径自定义配置策略参数。

```jinja2
{%- for item in add_gtpcpathdp_list -%}
    ADD GTPCPATHDP:
    {#- --- 必选参数 --- -#}
    RANGE={{item.RANGE}},
    PAS_COE={{item.PAS_COE}},
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：RANGE=ROAMING 时可选 --- -#}
    {%- if item.RANGE == 'ROAMING' -%}
        {%- if item.GP_ALMID is not none -%}
            GP_ALMID={{item.GP_ALMID}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 2 配置SGSN GTP-U路径管理。GTP-U路径是用于在UEG与对端之间传输用户数据的路径。

#### 2.1 配置GTP-U路径管理参数。

```jinja2
{%- for item in set_gtpupara_list -%}
    SET GTPUPARA:
    {#- --- 可选参数 --- -#}
    {%- if item.GTPUUPECHO is not none -%}
        GTPUUPECHO={{item.GTPUUPECHO}},
    {%- endif -%}
    {%- if item.GTPUDNECHO is not none -%}
        GTPUDNECHO={{item.GTPUDNECHO}},
    {%- endif -%}
    {%- if item.GTPUEI is not none -%}
        GTPUEI={{item.GTPUEI}},
    {%- endif -%}
    {%- if item.GTPUT3 is not none -%}
        GTPUT3={{item.GTPUT3}},
    {%- endif -%}
    {%- if item.GTPUN3 is not none -%}
        GTPUN3={{item.GTPUN3}},
    {%- endif -%}
    {%- if item.POTHD is not none -%}
        POTHD={{item.POTHD}},
    {%- endif -%}
    {%- if item.PNTHD is not none -%}
        PNTHD={{item.PNTHD}},
    {%- endif -%}
    {%- if item.PCTHD is not none -%}
        PCTHD={{item.PCTHD}},
    {%- endif -%}
    {%- if item.PRTHD is not none -%}
        PRTHD={{item.PRTHD}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 2.2 配置用户面控制参数。

```jinja2
SET GTPUCTRL:
;
```

#### 2.3 配置GTP-U路径自定义配置策略参数。

```jinja2
{%- for item in add_gtpupathdp_list -%}
    ADD GTPUPATHDP:
    {#- --- 必选参数 --- -#}
    RANGE={{item.RANGE}},
    PAS_COE={{item.PAS_COE}},
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：RANGE=ROAMING 时可选 --- -#}
    {%- if item.RANGE == 'ROAMING' -%}
        {%- if item.GP_ALMID is not none -%}
            GP_ALMID={{item.GP_ALMID}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 配置AMF GTP-C路径管理。

#### 3.1 配置GTP-C路径管理参数。

```jinja2
SET GTPCFUNCPARA:
;
```

#### 3.2 配置T3N3参数。

```jinja2
{%- for item in add_gtpct3n3_list -%}
    ADD GTPCT3N3:
    {#- --- 必选参数 --- -#}
    T3={{item.T3}},
    NODETYPE={{item.NODETYPE}},
    N3={{item.N3}},
    ;
{%- endfor -%}
```

#### 3.3 配置GTP-C路径自定义配置策略参数。

```jinja2
{%- for item in add_gtpcpathmp_list -%}
    ADD GTPCPATHMP:
    {#- --- 必选参数 --- -#}
    RANGE={{item.RANGE}},
    ;
{%- endfor -%}
```


---
id: GWFD-020911
name: 激活区域漫游限制特性（适用于AMF）
ne_type: UEG
type: feature
description: 本操作指导介绍在运行网络中激活区域漫游限制特性的操作过程。
tags: []
risk_level: ''
doc_source:
  - ["业务配置","风筝L","MEC 特性指南（风筝L）","AMF特性指南","GWFD-020900 接入管理","GWFD-020911 区域漫游限制（适用于AMF/UDM）","激活区域漫游限制特性（适用于AMF）"]
  - ["业务配置","风筝L","MEC 特性指南（风筝L）","HSS&UDM特性指南","GWFD-020900 接入管理","GWFD-020911 区域漫游限制","GWFD-020911 区域漫游限制（适用于AMF/UDM）","激活区域漫游限制特性（适用于AMF）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
本操作指导介绍在运行网络中激活区域漫游限制特性的操作过程。

## 必备事项
前提条件

* 请仔细阅读GWFD-020911 区域漫游限制特性概述（适用于AMF/UDM）。
* 已完成加载License，对应的License项为“82206572 LKV2RRR02 区域漫游限制”。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    add_areacode_list:
      type: items
      properties:
        AREACODE:
          name: '区域编码'
          type: string
          minLength: 1
          maxLength: 128
          required: true
          description: '设置区域编码，唯一标识AMF服务的某个区域。'
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
          data_source: ''
          pattern: ''
          default: ''
    add_areamem_list:
      type: items
      properties:
        AREACODE:
          name: '区域编码'
          type: string
          minLength: 1
          maxLength: 128
          required: true
          description: '一个区域由若干个跟踪区组成，该命令用于为指定的区域增加跟踪区成员。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        BGNTAC:
          name: '跟踪区编码起始值'
          type: string
          minLength: 6
          maxLength: 6
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ENDTAC:
          name: '跟踪区编码结束值'
          type: string
          minLength: 6
          maxLength: 6
          required: false
          description: ''
          data_source: ''
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
        MCC:
          name: 'MCC'
          type: string
          minLength: 3
          maxLength: 3
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MNC:
          name: 'MNC'
          type: string
          minLength: 2
          maxLength: 3
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
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
    set_ngmmfunc_list:
      type: items
      properties:
        AREARSTENSW:
          name: '区域漫游限制功能增强开关'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: '该参数用于表示AMF区域漫游限制功能增强开关。当开关打开时周期性注册更新、服务请求、切换流程中做区域接入限制检查。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    set_amfsoftparaofbit_list:
      type: items
      properties:
        DT:
          name: '数据类型'
          type: string
          enum:
          - Dw
          - Byte
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DWORDNUM:
          name: 'Dword索引'
          type: integer
          minimum: 1
          maximum: 1500
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VALUE:
          name: '软参记录值'
          type: string
          enum:
          - VALUE_0
          - VALUE_1
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        POSITION:
          name: '比特位'
          type: integer
          minimum: 1
          maximum: 32
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_areacode_list_1:
      type: items
      properties:
        AREACODE:
          name: '区域编码'
          type: string
          minLength: 1
          maxLength: 128
          required: true
          description: '设置区域编码，唯一标识AMF服务的某个区域。'
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
          data_source: ''
          pattern: ''
          default: ''
    add_areamem_list_1:
      type: items
      properties:
        AREACODE:
          name: '区域编码'
          type: string
          minLength: 1
          maxLength: 128
          required: true
          description: '一个区域由若干个跟踪区组成，该命令用于为指定的区域增加跟踪区成员。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        BGNTAC:
          name: '跟踪区编码起始值'
          type: string
          minLength: 6
          maxLength: 6
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ENDTAC:
          name: '跟踪区编码结束值'
          type: string
          minLength: 6
          maxLength: 6
          required: false
          description: ''
          data_source: ''
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
        MCC:
          name: 'MCC'
          type: string
          minLength: 3
          maxLength: 3
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MNC:
          name: 'MNC'
          type: string
          minLength: 2
          maxLength: 3
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_ngusrgrp_list:
      type: items
      properties:
        USRGRPID:
          name: '用户群组标识'
          type: integer
          minimum: 0
          maximum: 4294967294
          required: true
          description: '设置5G用户群信息，同一个用户群中的用户具有相同的策略。'
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
          data_source: ''
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
          description: '该命令用于为5G用户群增加用户群成员。'
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
          data_source: ''
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
    set_ngmmfunc_list_1:
      type: items
      properties:
        AREARSTENSW:
          name: '区域漫游限制功能增强开关'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: '该参数用于表示AMF区域漫游限制功能增强开关。当开关打开时周期性注册更新、服务请求、切换流程中做区域接入限制检查。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    set_ngmmproctrl_list:
      type: items
      properties:
        PROT:
          name: '流程类型'
          type: string
          enum:
          - AUSF_DISCOVERY
          - AIR
          - AUTHENTICATION
          - SMC
          - CHECK_IMEI
          - UDM_DISCOVERY
          - UDM_REGISTRATION
          - UDM_GET_SUBSCRIBER_DATA
          - UDM_SUBSCIBE
          - PCF_DISCOVERY
          - PCF_POLICY
          - OTHER_PROC
          - CAG
          required: true
          description: '由用户签约的“禁止区域（ForbiddenArea）”控制用户的接入，拒绝的原因值根据**SET NGMMPROCTRL**的整系统配置进行设置。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        AREARST:
          name: '区域限制拒绝原因值'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_ngaccarealst_list:
      type: items
      properties:
        AREARANGE:
          name: '区域范围'
          type: string
          enum:
          - ALL_AREA
          - AREA_CODE
          required: true
          description: 'AMF本地配置限制区域信息、用户信息、控制模式以及拒绝原因值。  由AMF本地配置的接入限制区域控制用户的接入，拒绝原因值根据**ADD NGACCAREALST**的配置进行设置。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        AREACODE:
          name: '区域编码'
          type: string
          minLength: 1
          maxLength: 128
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SUBRANGE:
          name: '用户范围'
          type: string
          enum:
          - ALL_USER
          - HOME_USER
          - FOREIGN_USER
          - USER_GROUP
          - SPECIAL_USER_RANGE
          - MSISDN_PREFIX
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SUBGRPID:
          name: '用户群组标识'
          type: integer
          minimum: 0
          maximum: 4294967294
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CTRLMODE:
          name: '控制模式'
          type: string
          enum:
          - WHITELIST
          - BLACKLIST
          required: true
          description: ''
          data_source: ''
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
        REJCAUSE:
          name: '拒绝原因值'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 15
  examples:
    add_areacode_list:
    - AREACODE: 'MyTown'
      DESC: 'for mytown'
    add_areamem_list:
    - AREACODE: 'MyTown'
      BGNTAC: '010101'
      ENDTAC: '010102'
      DESC: 'areamember of mytown'
      MCC: '123'
      MNC: '456'
    set_licenseswitch_list:
    - LICITEM: 'LKV2RRR02'
      SWITCH: ENABLE
    set_ngmmfunc_list:
    - AREARSTENSW: ON
    set_amfsoftparaofbit_list:
    - DT: Dw
      DWORDNUM: 11
      VALUE: VALUE_1
      POSITION: 2
    add_areacode_list_1:
    - AREACODE: 'MyTown'
      DESC: 'for mytown'
    add_areamem_list_1:
    - AREACODE: 'MyTown'
      BGNTAC: '010101'
      ENDTAC: '010102'
      DESC: 'areamember of mytown'
      MCC: '123'
      MNC: '456'
    add_ngusrgrp_list:
    - USRGRPID: 888
      DESC: 'for usergroup'
    add_ngusrgrpmem_list:
    - USRGRPID: 888
      IMSIPRE: '123456'
      DESC: 'sometown'
    set_ngmmfunc_list_1:
    - AREARSTENSW: ON
    set_ngmmproctrl_list:
    - PROT: OTHER_PROC
      AREARST: 0
    add_ngaccarealst_list:
    - AREARANGE: AREA_CODE
      AREACODE: 'MyTown'
      SUBRANGE: USER_GROUP
      SUBGRPID: 888
      CTRLMODE: WHITELIST
      DESC: 'for employees'
      REJCAUSE: 15
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 **根据用户接入和移动签约数据中的“禁止区域（Forbidden Area）”信息控制用户的接入。**

#### 1.1 进入“MML命令行-UEG”窗口。

#### 1.2 配置某个区域信息，以及AreaCode与TAI之间的映射关系。

##### 1.2.1 配置区域编码

```jinja2
{%- for item in add_areacode_list -%}
    ADD AREACODE:
    {#- --- 必选参数 --- -#}
    AREACODE="{{item.AREACODE}}",
    {#- --- 可选参数 --- -#}
    {%- if item.DESC is not none -%}
        DESC="{{item.DESC}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

##### 1.2.2 为指定的区域增加跟踪区成员

```jinja2
{%- for item in add_areamem_list -%}
    ADD AREAMEM:
    {#- --- 必选参数 --- -#}
    AREACODE="{{item.AREACODE}}",
    MCC="{{item.MCC}}",
    MNC="{{item.MNC}}",
    BGNTAC="{{item.BGNTAC}}",
    {#- --- 可选参数 --- -#}
    {%- if item.ENDTAC is not none -%}
        ENDTAC="{{item.ENDTAC}}",
    {%- endif -%}
    {%- if item.DESC is not none -%}
        DESC="{{item.DESC}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 2 **AMF针对指定的区域在本地配置用户接入的策略，然后基于策略控制用户的接入。**

#### 2.1 进入“MML命令行-UEG”窗口。

#### 2.2 开启本特性的功能控制开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

#### 2.3 开启区域漫游限制功能增强开关，将“AREARSTENSW”设置为“ON”。

```jinja2
{%- for item in set_ngmmfunc_list -%}
    SET NGMMFUNC:
    {#- --- 可选参数 --- -#}
    {%- if item.AREARSTENSW is not none -%}
        AREARSTENSW={{item.AREARSTENSW}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 2.4 需要限制用户在禁止区域内进行Xn切换以及周期性注册流程时，设置DWORD11中BIT2的取值为“1”。如果用户在禁止区域内发起Xn切换或者周期性注册，AMF会拒绝该流程。

```jinja2
{%- for item in set_amfsoftparaofbit_list -%}
    SET AMFSOFTPARAOFBIT:
    {#- --- 必选参数 --- -#}
    DT={{item.DT}},
    VALUE={{item.VALUE}},
    POSITION={{item.POSITION}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：DT=Dw 时必选 --- -#}
    {%- if item.DT == 'Dw' -%}
        DWORDNUM={{item.DWORDNUM}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 2.5 配置某个区域信息，以及AreaCode与TAI之间的映射关系。

##### 2.5.1 配置区域编码

```jinja2
{%- for item in add_areacode_list_1 -%}
    ADD AREACODE:
    {#- --- 必选参数 --- -#}
    AREACODE="{{item.AREACODE}}",
    {#- --- 可选参数 --- -#}
    {%- if item.DESC is not none -%}
        DESC="{{item.DESC}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

##### 2.5.2 为指定的区域增加跟踪区成员

```jinja2
{%- for item in add_areamem_list_1 -%}
    ADD AREAMEM:
    {#- --- 必选参数 --- -#}
    AREACODE="{{item.AREACODE}}",
    MCC="{{item.MCC}}",
    MNC="{{item.MNC}}",
    BGNTAC="{{item.BGNTAC}}",
    {#- --- 可选参数 --- -#}
    {%- if item.ENDTAC is not none -%}
        ENDTAC="{{item.ENDTAC}}",
    {%- endif -%}
    {%- if item.DESC is not none -%}
        DESC="{{item.DESC}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 2.6 配置某个用户群组信息。

##### 2.6.1 配置5G用户群标识

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

##### 2.6.2 配置用户群成员

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

#### 2.7 （可选）配置区域漫游限制增强功能，当开关打开时周期性注册更新、服务请求、切换流程中AMF根据本地配置做区域接入限制检查。

```jinja2
{%- if is_optional_area_roaming_restriction_enhancement -%}
    {%- for item in set_ngmmfunc_list_1 -%}
        SET NGMMFUNC:
        {#- --- 可选参数 --- -#}
        {%- if item.AREARSTENSW is not none -%}
            AREARSTENSW={{item.AREARSTENSW}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 2.8 配置拒绝的原因值（由用户签约的“禁止区域（ForbiddenArea）”控制用户的接入）。

```jinja2
{%- for item in set_ngmmproctrl_list -%}
    SET NGMMPROCTRL:
    {#- --- 必选参数 --- -#}
    PROT={{item.PROT}},
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：PROT=OTHER_PROC 时可选 --- -#}
    {%- if item.PROT == 'OTHER_PROC' -%}
        {%- if item.AREARST is not none -%}
            AREARST={{item.AREARST}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 2.9 AMF本地配置限制区域信息、用户信息、控制模式以及拒绝原因值（由AMF本地配置的接入限制区域控制用户的接入）。

```jinja2
{%- for item in add_ngaccarealst_list -%}
    ADD NGACCAREALST:
    {#- --- 必选参数 --- -#}
    AREARANGE={{item.AREARANGE}},
    CTRLMODE={{item.CTRLMODE}},
    SUBRANGE={{item.SUBRANGE}},
    {#- --- 可选参数 --- -#}
    {%- if item.DESC is not none -%}
        DESC="{{item.DESC}}",
    {%- endif -%}
    {%- if item.REJCAUSE is not none -%}
        REJCAUSE={{item.REJCAUSE}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：AREARANGE=AREA_CODE 时必选 --- -#}
    {%- if item.AREARANGE == 'AREA_CODE' -%}
        AREACODE="{{item.AREACODE}}",
    {%- endif -%}
    {#- --- 条件必选：SUBRANGE=USER_GROUP 时必选 --- -#}
    {%- if item.SUBRANGE == 'USER_GROUP' -%}
        SUBGRPID={{item.SUBGRPID}},
    {%- endif -%}
    ;
{%- endfor -%}
```

##### 2.9.1 限制区域之间不允许存在交叉和重叠，“所有区域”例外。

##### 2.9.2 当同时存在“指定区域”和“所有区域”时，以“指定区域”的策略为准，除非UE当前不在“指定区域”。

##### 2.9.3 对于同一个用户，可能匹配“指定区域”内的多个用户号段，该场景下，AMF按照最长匹配的方式优选。


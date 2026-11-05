---
id: ''
name: 在大网UNC（AMF/MME）上配置接入限制区域列表
ne_type: UEG
type: feature
description: 本操作指导介绍在大网UNC（AMF/MME）下配置接入限制区域列表（配置黑名单），使得园区终端接入大网时，返回#15失败原因值，园区终端把当前TAI记录为禁止TAI，搜索同覆盖下的其他TAI接入，最终接入园区网络。
tags: []
risk_level: ''
doc_source: ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（一号通专网核电场景，入驻式）","配置接入限制区域列表","在大网UNC（AMF/MME）上配置接入限制区域列表"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
本操作指导介绍在大网UNC（AMF/MME）下配置接入限制区域列表（配置黑名单），使得园区终端接入大网时，返回#15失败原因值，园区终端把当前TAI记录为禁止TAI，搜索同覆盖下的其他TAI接入，最终接入园区网络。

## 必备事项
前提条件

* 已完成加载License，对应的License项为“82206572 LKV2RRR02 区域漫游限制”。
* 详细原理请参考UNC产品文档中“**WSFD-105003 区域漫游限制**”特性。
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
          description: 'AMF本地配置限制区域信息、用户信息、控制模式以及拒绝原因值。由AMF本地配置的接入限制区域控制用户的接入，拒绝原因值根据**ADD NGACCAREALST**的配置进行设置。'
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
    set_licenseswitch_list_1:
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
    add_areagp_list:
      type: items
      properties:
        AREAID:
          name: '区域群标识'
          type: integer
          minimum: 1
          maximum: 50
          required: true
          description: '以位置区域为对象，控制该区域不同用户的接入策略。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        AREAN:
          name: '区域群名称'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'noname'
    add_areagpmem_list:
      type: items
      properties:
        AREAID:
          name: '区域群标识'
          type: integer
          minimum: 1
          maximum: 50
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IDTYPE:
          name: '标识类型'
          type: string
          enum:
          - LA
          - RA
          - TA
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MCC:
          name: '移动国家码'
          type: string
          maxLength: 3
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MNC:
          name: '移动网号'
          type: string
          maxLength: 3
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TAC:
          name: '跟踪区域码'
          type: string
          maxLength: 6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TACRANGE:
          name: '跟踪区域码范围'
          type: string
          maxLength: 6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_subgp_list:
      type: items
      properties:
        SUBID:
          name: '用户群标识'
          type: integer
          minimum: 1
          maximum: 100
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        SUBN:
          name: '用户群名称'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_subgpmem_list:
      type: items
      properties:
        SUBID:
          name: '用户群标识'
          type: integer
          minimum: 1
          maximum: 100
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        IMSIPRE:
          name: 'IMSI前缀'
          type: string
          maxLength: 15
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_s1accarealst_list:
      type: items
      properties:
        AREA:
          name: '区域范围'
          type: string
          enum:
          - AG
          - OTHER
          - TA
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        AREAID:
          name: '区域群标识'
          type: integer
          minimum: 1
          maximum: 50
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
          - FOREIGN_USER
          - HOME_USER
          - SPECIAL_IMSIPRE
          - SPECIAL_IMSI_RANGE
          - UE_TYPE
          - USER_GROUP
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SUBID:
          name: '用户群标识'
          type: integer
          minimum: 1
          maximum: 100
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CTRLTYPE:
          name: '控制类型'
          type: string
          enum:
          - ALLOW
          - REJECT
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CAUSE:
          name: '原因值'
          type: string
          enum:
          - CUSTOMER_DEFINED
          - EPS_NONEPS_SRV_NOT_ALLOWED
          - EPS_SERVICE_NOT_ALLOWED
          - EPS_SRV_NOT_ALLOWED_IN_PLMN
          - NO_SUITABLE_CELLS_IN_TA
          - PLMN_NOT_ALLOWED
          - ROAMING_NOT_ALLOWED_IN_TA
          - TA_NOT_ALLOWED
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NO_SUITABLE_CELLS_IN_TA
        SDCAUSE:
          name: '自定义原因值'
          type: integer
          minimum: 1
          maximum: 254
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV2RRR02'
      SWITCH: ENABLE
    set_ngmmfunc_list:
    - AREARSTENSW: ON
    add_areacode_list:
    - AREACODE: 'nuclear power.area1'
      DESC: 'nuclear power'
    add_areamem_list:
    - AREACODE: 'nuclear power.area1'
      MCC: '123'
      MNC: '456'
      BGNTAC: '010101'
      ENDTAC: '010102'
      DESC: 'areamember of nuclear power'
    add_ngusrgrp_list:
    - USRGRPID: 1
      DESC: 'for usergroup'
    add_ngusrgrpmem_list:
    - USRGRPID: 1
      IMSIPRE: '123456'
    add_ngaccarealst_list:
    - AREARANGE: AREA_CODE
      AREACODE: 'nuclear power.area1'
      SUBRANGE: USER_GROUP
      SUBGRPID: 1
      CTRLMODE: BLACKLIST
      REJCAUSE: 15
    set_licenseswitch_list_1:
    - LICITEM: 'LKV2RRR02'
      SWITCH: ENABLE
    add_areagp_list:
    - AREAID: 1
      AREAN: 'nuclear power'
    add_areagpmem_list:
    - AREAID: 1
      IDTYPE: TA
      MCC: '123'
      MNC: '456'
      TAC: '0x7603'
      TACRANGE: '0x7614'
    add_subgp_list:
    - SUBID: 1
      SUBN: 'for usergroup'
    add_subgpmem_list:
    - SUBID: 1
      IMSIPRE: '12345'
    add_s1accarealst_list:
    - AREA: AG
      AREAID: 1
      SUBRANGE: USER_GROUP
      SUBID: 1
      CTRLTYPE: REJECT
      CAUSE: CUSTOMER_DEFINED
      SDCAUSE: 15
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 //开启区域漫游限制功能开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

### 2 //开启区域漫游限制功能增强开关。

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

### 3 //配置区域范围。

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

### 4 //配置用户群组。

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
    ;
{%- endfor -%}
```

### 5 //AMF本地配置限制区域信息、控制模式（黑名单）以及拒绝原因值。

```jinja2
{%- for item in add_ngaccarealst_list -%}
    ADD NGACCAREALST:
    {#- --- 必选参数 --- -#}
    AREARANGE={{item.AREARANGE}},
    CTRLMODE={{item.CTRLMODE}},
    SUBRANGE={{item.SUBRANGE}},
    {#- --- 可选参数 --- -#}
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

### 6 //开启区域漫游限制功能开关。

```jinja2
{%- for item in set_licenseswitch_list_1 -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

### 7 //配置区域范围。

```jinja2
{%- for item in add_areagp_list -%}
    ADD AREAGP:
    {#- --- 必选参数 --- -#}
    AREAID={{item.AREAID}},
    {#- --- 可选参数 --- -#}
    {%- if item.AREAN is not none -%}
        AREAN="{{item.AREAN}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_areagpmem_list -%}
    ADD AREAGPMEM:
    {#- --- 必选参数 --- -#}
    AREAID={{item.AREAID}},
    IDTYPE={{item.IDTYPE}},
    MCC="{{item.MCC}}",
    MNC="{{item.MNC}}",
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IDTYPE=TA 时必选 --- -#}
    {%- if item.IDTYPE == 'TA' -%}
        TAC="{{item.TAC}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：IDTYPE=TA 时可选 --- -#}
    {%- if item.IDTYPE == 'TA' -%}
        {%- if item.TACRANGE is not none -%}
            TACRANGE="{{item.TACRANGE}}",
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 8 //配置用户群组。

```jinja2
{%- for item in add_subgp_list -%}
    ADD SUBGP:
    {#- --- 必选参数 --- -#}
    SUBID={{item.SUBID}},
    {#- --- 可选参数 --- -#}
    {%- if item.SUBN is not none -%}
        SUBN="{{item.SUBN}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_subgpmem_list -%}
    ADD SUBGPMEM:
    {#- --- 必选参数 --- -#}
    SUBID={{item.SUBID}},
    IMSIPRE="{{item.IMSIPRE}}",
    ;
{%- endfor -%}
```

### 9 //MME本地配置限制区域信息、控制模式（拒绝）以及拒绝原因值。

```jinja2
{%- for item in add_s1accarealst_list -%}
    ADD S1ACCAREALST:
    {#- --- 必选参数 --- -#}
    AREA={{item.AREA}},
    SUBRANGE={{item.SUBRANGE}},
    CTRLTYPE={{item.CTRLTYPE}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：AREA=AG 时必选 --- -#}
    {%- if item.AREA == 'AG' -%}
        AREAID={{item.AREAID}},
    {%- endif -%}
    {#- --- 条件必选：SUBRANGE=USER_GROUP 时必选 --- -#}
    {%- if item.SUBRANGE == 'USER_GROUP' -%}
        SUBID={{item.SUBID}},
    {%- endif -%}
    {#- --- 条件必选：CAUSE=CUSTOMER_DEFINED 时必选 --- -#}
    {%- if item.CAUSE == 'CUSTOMER_DEFINED' -%}
        SDCAUSE={{item.SDCAUSE}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：CTRLTYPE=REJECT 时可选 --- -#}
    {%- if item.CTRLTYPE == 'REJECT' -%}
        {%- if item.CAUSE is not none -%}
            CAUSE={{item.CAUSE}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```


---
id: ''
name: 激活多时区业务特性（适用于AMF）
ne_type: UNC
type: feature
description: 本操作指导介绍在运行网络中激活AMF的多时区功能的操作过程。  适用于AMF。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","基本接入功能","WSFD-106009 多时区业务","激活多时区业务特性（适用于AMF）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本操作指导介绍在运行网络中激活AMF的多时区功能的操作过程。适用于AMF。

## 必备事项
前提条件

* 请仔细阅读WSFD-106009 多时区业务特性概述。
* 该操作不需要开启License。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    set_ngmmfunc_list:
      type: items
      properties:
        SNDNETINFO:
          name: '发送网络信息'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: '用于控制AMF是否向UE发送运营商名称和时区信息。'
          data_source: '本端规划'
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
    add_areacode_list:
      type: items
      properties:
        AREACODE:
          name: '区域编码'
          type: string
          minLength: 1
          maxLength: 128
          required: true
          description: '设置区域编码，唯一标识AMF服务的某个区域，可支持中文名称。'
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
          description: '设置5G用户群信息，同一个用户群中的用户具有相同的策略'
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
    add_nitzplcy_list:
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
          description: '为指定区域和指定用户群配置网络名称。'
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
        AREARANGE:
          name: '区域范围'
          type: string
          enum:
          - ALL_AREA
          - AREA_CODE
          required: true
          description: ''
          data_source: ''
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
        USRGRPID:
          name: '用户群组标识'
          type: integer
          minimum: 0
          maximum: 4294967294
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        FULLNAME:
          name: '运营商全称'
          type: string
          minLength: 0
          maxLength: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SHORTNAME:
          name: '运营商简称'
          type: string
          minLength: 0
          maxLength: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_ngtzlst_list:
      type: items
      properties:
        TZID:
          name: '时区标识'
          type: integer
          minimum: 1
          maximum: 24
          required: true
          description: '配置时区和夏令时信息。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        TZONE:
          name: '时区'
          type: string
          enum:
          - E0000
          - E0100
          - E0200
          - E0300
          - E0330
          - E0400
          - E0430
          - E0500
          - E0530
          - E0545
          - E0600
          - E0630
          - E0700
          - E0800
          - E0845
          - E0900
          - E0930
          - E1000
          - E1030
          - E1100
          - E1130
          - E1200
          - E1245
          - E1300
          - E1400
          - W0100
          - W0200
          - W0300
          - W0330
          - W0400
          - W0430
          - W0500
          - W0600
          - W0700
          - W0800
          - W0900
          - W0930
          - W1000
          - W1100
          - W1200
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DST:
          name: '是否实行夏令时'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SM:
          name: '开始日期输入方式'
          type: string
          enum:
          - DATE
          - WEEK
          - DATEWEEK
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SMONTH:
          name: '开始月份'
          type: string
          enum:
          - JAN
          - FEB
          - MAR
          - APR
          - MAY
          - JUN
          - JUL
          - AUG
          - SEP
          - OCT
          - NOV
          - DEC
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SDAY:
          name: '开始日'
          type: integer
          minimum: 1
          maximum: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ST:
          name: '开始时间'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'HH&MM&SS'
        EM:
          name: '结束日期输入方式'
          type: string
          enum:
          - DATE
          - WEEK
          - DATEWEEK
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        EMONTH:
          name: '结束月份'
          type: string
          enum:
          - JAN
          - FEB
          - MAR
          - APR
          - MAY
          - JUN
          - JUL
          - AUG
          - SEP
          - OCT
          - NOV
          - DEC
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        EDAY:
          name: '结束日'
          type: integer
          minimum: 1
          maximum: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ET:
          name: '结束时间'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'HH&MM&SS'
        TO:
          name: '时间偏移量(小时)'
          type: integer
          minimum: 0
          maximum: 2
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        EWEEK:
          name: '结束星期'
          type: string
          enum:
          - SUN
          - MON
          - TUE
          - WED
          - THU
          - FRI
          - SAT
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        EWSEQ:
          name: '第几个星期(结束)'
          type: string
          enum:
          - FIRST
          - SECOND
          - THIRD
          - FOURTH
          - LAST
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SWEEK:
          name: '开始星期'
          type: string
          enum:
          - SUN
          - MON
          - TUE
          - WED
          - THU
          - FRI
          - SAT
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SWSEQ:
          name: '第几个星期(开始)'
          type: string
          enum:
          - FIRST
          - SECOND
          - THIRD
          - FOURTH
          - LAST
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_ngareatz_list:
      type: items
      properties:
        MCC:
          name: 'MCC'
          type: string
          minLength: 3
          maxLength: 3
          required: true
          description: '为指定区域的用户配置时区标识。'
          data_source: '全网规划'
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
        TZID:
          name: '时区标识'
          type: integer
          minimum: 1
          maximum: 24
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
  examples:
    set_ngmmfunc_list:
    - SNDNETINFO: YES
    set_amfsoftparaofbit_list:
    - DT: Dw
      DWORDNUM: 5
      VALUE: VALUE_1
      POSITION: 15
    add_areacode_list:
    - AREACODE: 'MyTown'
      DESC: 'for mytown'
    add_areamem_list:
    - AREACODE: 'MyTown'
      MCC: '123'
      MNC: '456'
      BGNTAC: '010101'
      ENDTAC: '010102'
      DESC: 'areamember of mytown'
    add_ngusrgrp_list:
    - USRGRPID: 20
      DESC: 'for usergroup'
    add_ngusrgrpmem_list:
    - USRGRPID: 20
      IMSIPRE: '123456'
      DESC: 'sometown'
    add_nitzplcy_list:
    - SUBRANGE: USER_GROUP
      DESC: 'NITZ'
      IMSIPRE: '123456'
      AREARANGE: AREA_CODE
      AREACODE: 'MyTown'
      USRGRPID: 20
      FULLNAME: 'Ch Mobile'
      SHORTNAME: 'CM'
    add_ngtzlst_list:
    - TZID: 1
      TZONE: E0000
      DST: YES
      SM: DATE
      SMONTH: JAN
      SDAY: 15
      ST: '18&10&02'
      EM: DATE
      EMONTH: MAR
      EDAY: 1
      ET: '23&10&56'
      TO: 1
      EWEEK: ''
      EWSEQ: ''
      SWEEK: ''
      SWSEQ: ''
    add_ngareatz_list:
    - MCC: '123'
      MNC: '456'
      BGNTAC: '010101'
      ENDTAC: '010102'
      TZID: 1
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 进入“MML命令行-UNC”窗口。

### 2 配置UNC是否可以向UE发送网络信息。

```jinja2
{%- for item in set_ngmmfunc_list -%}
    SET NGMMFUNC:
    {#- --- 可选参数 --- -#}
    {%- if item.SNDNETINFO is not none -%}
        SNDNETINFO={{item.SNDNETINFO}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 如果此处配置UNC不可以向UE发送网络信息，则在AMF无法通过Configuration Update Command消息向UE下发网络标识、时区和夏令时等信息。

### 3 **可选：**配置NITZ下发时间时的本地时间根据UTC时间获取，避免向UE发送的时区不符合协议。

```jinja2
{%- if is_optional_nitz_utc_time -%}
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
{%- endif -%}
```

### 4 基于区域范围和用户群组组合的粒度来灵活设置不同的网络名称。

#### 4.1 配置区域编码

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

#### 4.2 为指定的区域增加跟踪区成员

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

#### 4.3 配置5G用户群标识

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

#### 4.4 配置用户群成员

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

### 5 为指定区域和指定用户群配置网络名称。

```jinja2
{%- for item in add_nitzplcy_list -%}
    ADD NITZPLCY:
    {#- --- 必选参数 --- -#}
    AREARANGE={{item.AREARANGE}},
    SUBRANGE={{item.SUBRANGE}},
    {#- --- 可选参数 --- -#}
    {%- if item.FULLNAME is not none -%}
        FULLNAME="{{item.FULLNAME}}",
    {%- endif -%}
    {%- if item.SHORTNAME is not none -%}
        SHORTNAME="{{item.SHORTNAME}}",
    {%- endif -%}
    {%- if item.DESC is not none -%}
        DESC="{{item.DESC}}",
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：AREARANGE=AREA_CODE 时必选 --- -#}
    {%- if item.AREARANGE == 'AREA_CODE' -%}
        AREACODE="{{item.AREACODE}}",
    {%- endif -%}
    {#- --- 条件必选：SUBRANGE=USER_GROUP 时必选 --- -#}
    {%- if item.SUBRANGE == 'USER_GROUP' -%}
        USRGRPID={{item.USRGRPID}},
    {%- endif -%}
    {#- --- 条件必选：SUBRANGE=IMSI_PREFIX 时必选 --- -#}
    {%- if item.SUBRANGE == 'IMSI_PREFIX' -%}
        IMSIPRE="{{item.IMSIPRE}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### UNC整系统的网络名称（运营商名称）已在**ADD NGMNO**命令中配置。当需要匹配的区域范围为所有区域，用户群组为所有用户时，则优先使用**ADD NGMNO**配置的移动网络运营商名称，其次使用**ADD NITZPLCY**配置的网络名称。

### 对于区域范围，网络名称与区域范围的匹配优先级从高到低依次为：“AREA\_CODE(指定区域编码)”，“ALL\_AREA(所有区域)”。

### 对于指定的用户（群），网络名称的优先级从高到低依次为：“USER\_GROUP(用户群)/IMSI\_PREFIX(指定IMSI前缀)”，“FOREIGN\_USER(外网用户)”或“HOME\_USER(本网用户)”，“ALL\_USER(所有用户)”。

### USER\_GROUP(用户群)与IMSI\_PREFIX(指定IMSI前缀)为互斥关系。

### 同一个区域编码中，可以配置不同的USRGRPID，但是不同的USRGRPID在**ADD NGUSRGRPMEM**中不能有相同的IMSIPRE成员。

### 当配多个指定区域编码时，不同指定区域编码对应的区域成员在**ADD AREAMEM**中不允许交叠。

### 6 配置时区和夏令时信息。

```jinja2
{%- for item in add_ngtzlst_list -%}
    ADD NGTZLST:
    {#- --- 必选参数 --- -#}
    TZID={{item.TZID}},
    TZONE={{item.TZONE}},
    {#- --- 可选参数 --- -#}
    {%- if item.DST is not none -%}
        DST={{item.DST}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：DST=YES 时必选 --- -#}
    {%- if item.DST == 'YES' -%}
        SM={{item.SM}},
    {%- endif -%}
    {#- --- 条件必选：DST=YES 时必选 --- -#}
    {%- if item.DST == 'YES' -%}
        SMONTH={{item.SMONTH}},
    {%- endif -%}
    {#- --- 条件必选：SM=DATE/DATEWEEK 时必选 --- -#}
    {%- if item.SM in ['DATE', 'DATEWEEK'] -%}
        SDAY={{item.SDAY}},
    {%- endif -%}
    {#- --- 条件必选：DST=YES 时必选 --- -#}
    {%- if item.DST == 'YES' -%}
        ST={{item.ST}},
    {%- endif -%}
    {#- --- 条件必选：DST=YES 时必选 --- -#}
    {%- if item.DST == 'YES' -%}
        EM={{item.EM}},
    {%- endif -%}
    {#- --- 条件必选：DST=YES 时必选 --- -#}
    {%- if item.DST == 'YES' -%}
        EMONTH={{item.EMONTH}},
    {%- endif -%}
    {#- --- 条件必选：EM=DATE/DATEWEEK 时必选 --- -#}
    {%- if item.EM in ['DATE', 'DATEWEEK'] -%}
        EDAY={{item.EDAY}},
    {%- endif -%}
    {#- --- 条件必选：DST=YES 时必选 --- -#}
    {%- if item.DST == 'YES' -%}
        ET={{item.ET}},
    {%- endif -%}
    {#- --- 条件必选：DST=YES 时必选 --- -#}
    {%- if item.DST == 'YES' -%}
        TO={{item.TO}},
    {%- endif -%}
    {#- --- 条件必选：EM=WEEK/DATEWEEK 时必选 --- -#}
    {%- if item.EM in ['WEEK', 'DATEWEEK'] -%}
        EWEEK={{item.EWEEK}},
    {%- endif -%}
    {#- --- 条件必选：EM=WEEK 时必选 --- -#}
    {%- if item.EM == 'WEEK' -%}
        EWSEQ={{item.EWSEQ}},
    {%- endif -%}
    {#- --- 条件必选：SM=WEEK/DATEWEEK 时必选 --- -#}
    {%- if item.SM in ['WEEK', 'DATEWEEK'] -%}
        SWEEK={{item.SWEEK}},
    {%- endif -%}
    {#- --- 条件必选：SM=WEEK 时必选 --- -#}
    {%- if item.SM == 'WEEK' -%}
        SWSEQ={{item.SWSEQ}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 7 为指定区域的用户配置时区标识。

```jinja2
{%- for item in add_ngareatz_list -%}
    ADD NGAREATZ:
    {#- --- 必选参数 --- -#}
    MCC="{{item.MCC}}",
    MNC="{{item.MNC}}",
    BGNTAC="{{item.BGNTAC}}",
    TZID={{item.TZID}},
    {#- --- 可选参数 --- -#}
    {%- if item.ENDTAC is not none -%}
        ENDTAC="{{item.ENDTAC}}",
    {%- endif -%}
    ;
{%- endfor -%}
```


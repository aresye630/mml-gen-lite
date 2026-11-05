---
id: GWFD-020914
name: 激活基站重定向
ne_type: UEG
type: feature
description: 本操作指导用于指导开启AMF重定向特性。  本特性是指在大网和园区共享基站场景下，大网AMF可以将园区用户通过基站重定向给园区UEG L的AMF、园区UEG L的AMF可以将大网用户通过基站重定向给大网AMF以及园区之间共享基站场景下，园区和大网失联时UEG L、UEG M上的AMF可以将用户通过基站重定向到对应的UEG L、UEG M上的AMF处理业务。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝L","MEC 特性指南（风筝L）","AMF特性指南","GWFD-021100 移动性管理","GWFD-020914 基站重定向","激活基站重定向"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
本操作指导用于指导开启AMF重定向特性。本特性是指在大网和园区共享基站场景下，大网AMF可以将园区用户通过基站重定向给园区UEG L的AMF、园区UEG L的AMF可以将大网用户通过基站重定向给大网AMF以及园区之间共享基站场景下，园区和大网失联时UEG L、UEG M上的AMF可以将用户通过基站重定向到对应的UEG L、UEG M上的AMF处理业务。

## 必备事项
前提条件

* 请仔细阅读GWFD-020914 基站重定向特性概述。
* 完成加载License。
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
    set_ngareareselctrl_list:
      type: items
      properties:
        AREARERT:
          name: '区域重路由开关'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: '设置AMF区域重选功能控制参数。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        MULTIRERT:
          name: '重复重路由开关'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RERTVOICEPRE:
          name: '重路由语音优先开关'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_reselareacode_list:
      type: items
      properties:
        RESELAREACODE:
          name: 'AMF重选功能区域编码'
          type: string
          minLength: 1
          maxLength: 128
          required: true
          description: '基于运营商规划的区域进行AMF重选功能的差异化控制。'
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
    add_reselareamem_list:
      type: items
      properties:
        RESELAREACODE:
          name: 'AMF重选功能区域编码'
          type: string
          minLength: 1
          maxLength: 128
          required: true
          description: ''
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
    add_ngareareselplcy_list:
      type: items
      properties:
        AREARANGE:
          name: '区域范围'
          type: string
          enum:
          - ALL_AREA
          - AREA_CODE
          required: true
          description: '增加AMF区域重选功能控制策略。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        RESELAREACODE:
          name: 'AMF重选功能区域编码'
          type: string
          minLength: 1
          maxLength: 128
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CTRLOBJECT:
          name: '控制对象'
          type: string
          enum:
          - USER_GROUP
          - SUB_NS
          - NO_SUB
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SUBGRPID:
          name: '用户群组标识'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CTRLMODE:
          name: '控制模式'
          type: string
          enum:
          - RE_ROUTE
          - ALLOW
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TGTAMFSET:
          name: '目标AMFSET'
          type: string
          minLength: 3
          maxLength: 3
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV2AREARERT'
      SWITCH: ENABLE
    set_ngareareselctrl_list:
    - AREARERT: ON
      MULTIRERT: OFF
      RERTVOICEPRE: ON
    add_reselareacode_list:
    - RESELAREACODE: 'ReSelZone'
      DESC: 'for zone1'
    add_reselareamem_list:
    - RESELAREACODE: 'ReSelZone'
      MCC: '123'
      MNC: '45'
      BGNTAC: '120101'
    add_ngareareselplcy_list:
    - AREARANGE: AREA_CODE
      RESELAREACODE: 'ReSelZone'
      CTRLOBJECT: USER_GROUP
      SUBGRPID: 1
      CTRLMODE: RE_ROUTE
      TGTAMFSET: '111'
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 进入“MML命令行-UEG”窗口。

### 2 打开本特性的License配置开关。

#### 2.1 //打开本特性的License配置开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

### 3 设置AMF区域重选功能控制参数。

#### 3.1 //设置AMF区域重选功能控制参数。

```jinja2
{%- for item in set_ngareareselctrl_list -%}
    SET NGAREARESELCTRL:
    {#- --- 可选参数 --- -#}
    {%- if item.AREARERT is not none -%}
        AREARERT={{item.AREARERT}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：AREARERT=ON 时可选 --- -#}
    {%- if item.AREARERT == 'ON' -%}
        {%- if item.MULTIRERT is not none -%}
            MULTIRERT={{item.MULTIRERT}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：AREARERT=ON 时可选 --- -#}
    {%- if item.AREARERT == 'ON' -%}
        {%- if item.RERTVOICEPRE is not none -%}
            RERTVOICEPRE={{item.RERTVOICEPRE}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 基于运营商规划的区域进行AMF重选功能的差异化控制。

#### 4.1 //基于运营商规划的区域进行AMF重选功能的差异化控制。

```jinja2
{%- for item in add_reselareacode_list -%}
    ADD RESELAREACODE:
    {#- --- 必选参数 --- -#}
    RESELAREACODE="{{item.RESELAREACODE}}",
    {#- --- 可选参数 --- -#}
    {%- if item.DESC is not none -%}
        DESC="{{item.DESC}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_reselareamem_list -%}
    ADD RESELAREAMEM:
    {#- --- 必选参数 --- -#}
    RESELAREACODE="{{item.RESELAREACODE}}",
    MCC="{{item.MCC}}",
    MNC="{{item.MNC}}",
    BGNTAC="{{item.BGNTAC}}",
    ;
{%- endfor -%}
```

### 5 增加AMF区域重选功能控制策略。

#### 5.1 //增加AMF区域重选功能控制策略。

```jinja2
{%- for item in add_ngareareselplcy_list -%}
    ADD NGAREARESELPLCY:
    {#- --- 必选参数 --- -#}
    AREARANGE={{item.AREARANGE}},
    CTRLOBJECT={{item.CTRLOBJECT}},
    TGTAMFSET="{{item.TGTAMFSET}}",
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：AREARANGE=AREA_CODE 时必选 --- -#}
    {%- if item.AREARANGE == 'AREA_CODE' -%}
        RESELAREACODE="{{item.RESELAREACODE}}",
    {%- endif -%}
    {#- --- 条件必选：CTRLOBJECT=USER_GROUP 时必选 --- -#}
    {%- if item.CTRLOBJECT == 'USER_GROUP' -%}
        SUBGRPID={{item.SUBGRPID}},
    {%- endif -%}
    {#- --- 条件必选：CTRLOBJECT=USER_GROUP 时必选 --- -#}
    {%- if item.CTRLOBJECT == 'USER_GROUP' -%}
        CTRLMODE={{item.CTRLMODE}},
    {%- endif -%}
    ;
{%- endfor -%}
```


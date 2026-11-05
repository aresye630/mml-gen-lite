---
id: ''
name: 配置切片选择可选功能
ne_type: UNC
type: feature
description: 本章节用于配置以下可选功能：  * 是否由初始AMF决策网络切片。 * 是否使能区域切片功能，并配置TA级限制切片。 * 切片选择中AMF重定向方式。 * 拒绝UE注册请求时是否携带Rejected S-NSSAI信元。
risk_level: ''
doc_source: ["网络部署","业务专题","5G Core NSSF解决方案","NSSF功能部署","NSSF非容灾组网","AMF配置","可选功能配置","配置切片选择可选功能"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本章节用于配置以下可选功能：* 是否由初始AMF决策网络切片。* 是否使能区域切片功能，并配置TA级限制切片。* 切片选择中AMF重定向方式。* 拒绝UE注册请求时是否携带Rejected S-NSSAI信元。

## 必备事项
前提条件

* 具备管理员权限的操作人员已经登录华为操作维护系统（登录U2020/MAE客户端或登录OM Portal）。

* UNC软件安装已完成。
* 已经获取网设LLD文档。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    set_nsselpara_list:
      type: items
      properties:
        SELFDETERMINE:
          name: '自行决策能否为UE服务'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: '判断是否由初始AMF决策网络切片。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_nsselpara_list_1:
      type: items
      properties:
        SYNSW:
          name: '同步开关'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: '如果NSSF的**SET NSSFFUNCPARA**命令中“DATASOURCETYPEAMF”设置为  “ReportData”，需要将此开关打开。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        INTERVAL:
          name: '间隔(min)'
          type: integer
          minimum: 1
          maximum: 1440
          required: false
          description: '配置AMF到NSSF的网络切片可用性信息的同步间隔。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    opr_nsavlinfo_list:
      type: items
      properties:
        OPTYPE:
          name: '操作类型'
          type: string
          enum:
          - SYNCHRONIZE
          - DELETE
          - SUBSCRIBE
          - CANCEL
          required: true
          description: '配置AMF向NSSF订阅网络切片的可用性。  说明：  如果当前AMF已有基站接入，或新基站接入到AMF时，AMF都需要向NSSF订阅网络切片可用性信息。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_nsselpara_list_2:
      type: items
      properties:
        CAMPUSNSSW:
          name: '园区网络切片开关'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: '配置AMF使能区域切片限制功能。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_rstrnsareacode_list:
      type: items
      properties:
        AREACODE:
          name: '区域编码'
          type: string
          minLength: 1
          maxLength: 128
          required: true
          description: '配置TA级限制切片。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_rstrnsareamem_list:
      type: items
      properties:
        AREACODE:
          name: '区域编码'
          type: string
          minLength: 1
          maxLength: 128
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        MCC:
          name: '移动国家码'
          type: string
          minLength: 3
          maxLength: 3
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        MNC:
          name: '移动网号'
          type: string
          minLength: 2
          maxLength: 3
          required: true
          description: ''
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
    add_amfrstrnssai_list:
      type: items
      properties:
        RSTRAREARANGE:
          name: '限制区域范围'
          type: string
          enum:
          - ALL_AREA
          - AREA_CODE
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        SUBRANGE:
          name: '用户范围'
          type: string
          enum:
          - ALL_USER
          - HOME_USER
          - FOREIGN_USER
          - IMSI_PREFIX
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        SST:
          name: '切片业务类型'
          type: integer
          minimum: 0
          maximum: 255
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        SD:
          name: '切片细分标识'
          type: string
          minLength: 6
          maxLength: 6
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        RSTRAREACODE:
          name: '限制区域编码'
          type: string
          minLength: 1
          maxLength: 128
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IMSIPRE:
          name: 'IMSI前缀'
          type: string
          minLength: 1
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_ngmmfunc_list:
      type: items
      properties:
        RESELTYPE:
          name: 'AMF重选方式'
          type: string
          enum:
          - RE_ROUTE
          - RE_DIRECT
          required: false
          description: '配置初始AMF通过重路由还是重定向流程接入到目标AMF。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    set_nascmpt_list:
      type: items
      properties:
        NASMSGTYPE:
          name: 'NAS消息类型'
          type: string
          enum:
          - REGISTRATION_REJECT
          required: true
          description: '拒绝UE注册请求时是否携带Rejected S-NSSAI信元。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        SNDREJNS:
          name: '是否携带拒绝切片信元'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
  examples:
    set_nsselpara_list:
    - SELFDETERMINE: YES
    set_nsselpara_list_1:
    - SYNSW: ON
      INTERVAL: 5
    opr_nsavlinfo_list:
    - OPTYPE: SUBSCRIBE
    set_nsselpara_list_2:
    - CAMPUSNSSW: ON
    add_rstrnsareacode_list:
    - AREACODE: 'jq001.pd006.sh.mcc123.mnc45'
    add_rstrnsareamem_list:
    - AREACODE: 'jq001.pd006.sh.mcc123.mnc45'
      MCC: '123'
      MNC: '45'
      BGNTAC: '120101'
    add_amfrstrnssai_list:
    - RSTRAREARANGE: ALL_AREA
      SUBRANGE: FOREIGN_USER
      SST: 1
      SD: '010101'
      RSTRAREACODE: ''
      IMSIPRE: ''
    set_ngmmfunc_list:
    - RESELTYPE: RE_DIRECT
    set_nascmpt_list:
    - NASMSGTYPE: REGISTRATION_REJECT
      SNDREJNS: YES
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 **配置由初始AMF决策网络切片**

### 判断是否由初始AMF决策网络切片。

```jinja2
{%- for item in set_nsselpara_list -%}
    SET NSSELPARA:
    {#- --- 可选参数 --- -#}
    {%- if item.SELFDETERMINE is not none -%}
        SELFDETERMINE={{item.SELFDETERMINE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 2 **配置AMF到NSSF的网络切片可用性信息的自动同步功能**

### 配置AMF到NSSF的网络切片可用性信息的自动同步。

```jinja2
{%- for item in set_nsselpara_list_1 -%}
    SET NSSELPARA:
    {#- --- 可选参数 --- -#}
    {%- if item.SYNSW is not none -%}
        SYNSW={{item.SYNSW}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：SYNSW=ON 时必选 --- -#}
    {%- if item.SYNSW == 'ON' -%}
        INTERVAL={{item.INTERVAL}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 **使能区域切片功能，并配置TA级限制切片**

### 5分钟（AMF到NSSF的网络切片可用性信息的同步间隔时间）之后配置由AMF携带其服务的TAI列表向NSSF订阅网络切片可用性信息。

```jinja2
{%- for item in opr_nsavlinfo_list -%}
    OPR NSAVLINFO:
    {#- --- 必选参数 --- -#}
    OPTYPE={{item.OPTYPE}},
    ;
{%- endfor -%}
```

### 4 配置AMF是否使能区域切片功能。

```jinja2
{%- for item in set_nsselpara_list_2 -%}
    SET NSSELPARA:
    {#- --- 可选参数 --- -#}
    {%- if item.CAMPUSNSSW is not none -%}
        CAMPUSNSSW={{item.CAMPUSNSSW}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 5 增加TA级切片限制区域码。

```jinja2
{%- for item in add_rstrnsareacode_list -%}
    ADD RSTRNSAREACODE:
    {#- --- 必选参数 --- -#}
    AREACODE="{{item.AREACODE}}",
    ;
{%- endfor -%}
```

### 6 增加TA级限制切片所属跟踪区成员

```jinja2
{%- for item in add_rstrnsareamem_list -%}
    ADD RSTRNSAREAMEM:
    {#- --- 必选参数 --- -#}
    AREACODE="{{item.AREACODE}}",
    MCC="{{item.MCC}}",
    MNC="{{item.MNC}}",
    BGNTAC="{{item.BGNTAC}}",
    ;
{%- endfor -%}
```

### 7 增加TA级限制切片。

```jinja2
{%- for item in add_amfrstrnssai_list -%}
    ADD AMFRSTRNSSAI:
    {#- --- 必选参数 --- -#}
    RSTRAREARANGE={{item.RSTRAREARANGE}},
    SUBRANGE={{item.SUBRANGE}},
    SST={{item.SST}},
    {#- --- 可选参数 --- -#}
    {%- if item.SD is not none -%}
        SD="{{item.SD}}",
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：SUBRANGE=IMSI_PREFIX 时必选 --- -#}
    {%- if item.SUBRANGE == 'IMSI_PREFIX' -%}
        IMSIPRE="{{item.IMSIPRE}}",
    {%- endif -%}
    {#- --- 条件必选：RSTRAREARANGE=AREA_CODE 时必选 --- -#}
    {%- if item.RSTRAREARANGE == 'AREA_CODE' -%}
        RSTRAREACODE="{{item.RSTRAREACODE}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 8 **配置切片选择中AMF重定向方式**

### 配置初始AMF通过重定向流程接入到目标AMF。

```jinja2
{%- for item in set_ngmmfunc_list -%}
    SET NGMMFUNC:
    {#- --- 可选参数 --- -#}
    {%- if item.RESELTYPE is not none -%}
        RESELTYPE={{item.RESELTYPE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 9 **配置拒绝UE注册请求时携带Rejected S-NSSAI信元**

### 配置拒绝UE注册请求时携带Rejected S-NSSAI信元。

```jinja2
{%- for item in set_nascmpt_list -%}
    SET NASCMPT:
    {#- --- 必选参数 --- -#}
    NASMSGTYPE={{item.NASMSGTYPE}},
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：NASMSGTYPE=REGISTRATION_REJECT 时可选 --- -#}
    {%- if item.NASMSGTYPE == 'REGISTRATION_REJECT' -%}
        {%- if item.SNDREJNS is not none -%}
            SNDREJNS={{item.SNDREJNS}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```


---
id: ''
name: 配置2G移动性管理
ne_type: UNC
type: feature
description: 本操作指导介绍在运行网络中配置移动性管理特性的操作过程。  2G移动性管理能使2G MS附着到SGSN，是MS获取网络服务的前提。SGSN对其天然支持。在3G没有完全替代2G时，每台SGSN均需要支持2G移动性管理功能。  系统为移动性管理通用参数提供了默认值，这些默认值为推荐值。用户也可以根据实际网络情况针对部分选项进行调整，使SGSN在本网络中更高效工作。
risk_level: ''
doc_source: ["网络部署","初始配置","UNC初始配置与调测","组网对接配置","配置AMF&MME&SGSN","配置SGSN","配置移动性管理","配置2G移动性管理"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本操作指导介绍在运行网络中配置移动性管理特性的操作过程。2G移动性管理能使2G MS附着到SGSN，是MS获取网络服务的前提。SGSN对其天然支持。在3G没有完全替代2G时，每台SGSN均需要支持2G移动性管理功能。系统为移动性管理通用参数提供了默认值，这些默认值为推荐值。用户也可以根据实际网络情况针对部分选项进行调整，使SGSN在本网络中更高效工作。

## 必备事项
前提条件

* 具备管理员权限的操作人员已经登录华为操作维护系统（登录U2020客户端或登录OM Portal）。

* UNC软件安装已完成。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    add_hplmn_list:
      type: items
      properties:
        MCC:
          name: '移动国家码'
          type: string
          maxLength: 3
          required: true
          description: '增加归属PLMN配置信息。'
          data_source: '参见“水平网设LLD文档 ”。'
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
        CC:
          name: '国家码'
          type: string
          maxLength: 6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SM:
          name: '是否允许（SM业务）'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: YES
        MAXSMNUM:
          name: '最大承载数'
          type: integer
          minimum: 1
          maximum: 11
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 11
        SMS:
          name: '是否允许（SMS业务）'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: YES
        S5S8TYPE:
          name: '协议类型'
          type: string
          enum:
          - GTP
          - PMIP
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: GTP
        PLMNN:
          name: '运营商名称'
          type: string
          maxLength: 50
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'noname'
        SMSCR:
          name: '是否允许纠正短消息中心'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NO
    set_gmm_list:
      type: items
      properties:
        T3322:
          name: 'T3322（s）'
          type: integer
          minimum: 3
          maximum: 12
          required: false
          description: '配置2G移动性管理定时器参数。'
          data_source: ''
          pattern: ''
          default: ''
        N3322:
          name: 'N3322（times）'
          type: integer
          minimum: 0
          maximum: 5
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        T3350:
          name: 'T3350（s）'
          type: integer
          minimum: 3
          maximum: 12
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        N3350:
          name: 'N3350（times）'
          type: integer
          minimum: 0
          maximum: 5
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        T3360:
          name: 'T3360（s）'
          type: integer
          minimum: 3
          maximum: 12
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        N3360:
          name: 'N3360（times）'
          type: integer
          minimum: 0
          maximum: 5
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        T3370:
          name: 'T3370（s）'
          type: integer
          minimum: 3
          maximum: 12
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        N3370:
          name: 'N3370（times）'
          type: integer
          minimum: 0
          maximum: 5
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        T3313:
          name: 'T3313（s）'
          type: integer
          minimum: 4
          maximum: 20
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        N3313:
          name: 'N3313（times）'
          type: integer
          minimum: 0
          maximum: 5
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PAGINGDELTA:
          name: '重寻呼间隔递增值（s）'
          type: integer
          minimum: 0
          maximum: 20
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RDYTMR:
          name: '准备定时器（s）'
          type: integer
          minimum: 1
          maximum: 11160
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PRDTMR:
          name: '周期路由更新定时器（min）'
          type: integer
          minimum: 1
          maximum: 186
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MSRCHTMR:
          name: 'MS可达定时器（min）'
          type: integer
          minimum: 7
          maximum: 198
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IMDTCHTMR:
          name: '保留参数'
          type: integer
          minimum: 0
          maximum: 198
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        T3:
          name: 'T3定时器（s）'
          type: integer
          minimum: 3
          maximum: 60
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PRT:
          name: '优先级'
          type: integer
          minimum: 0
          maximum: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RDTDELTA:
          name: '保留参数2'
          type: integer
          minimum: 0
          maximum: 5
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_gbauthciph_list:
      type: items
      properties:
        IMSIPRE:
          name: 'IMSI前缀'
          type: string
          maxLength: 15
          required: true
          description: '启用鉴权和加密功能。'
          data_source: ''
          pattern: ''
          default: ''
        SECPLC:
          name: '安全策略'
          type: string
          enum:
          - AUTHANDPROTECTED
          - AUTHONLY
          - NEVER
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: AUTHANDPROTECTED
        CIPHALG:
          name: '加密算法'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ATTSAUTH:
          name: '是否支持附着流程的二次鉴权功能'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NO
        AUTHEVENT:
          name: '鉴权事件'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AUTHEVENTTHRESHOLD:
          name: '鉴权事件上限'
          type: integer
          minimum: 0
          maximum: 1023
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 1
        AUTHPERIOD:
          name: '鉴权周期'
          type: integer
          minimum: 0
          maximum: 24
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 24
        AUTHSETSNUMBER:
          name: '鉴权集数量'
          type: integer
          minimum: 1
          maximum: 5
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 5
        AUTHSETV2:
          name: '是否支持V2取鉴权集功能'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NO
        CAFTIMES:
          name: '用户鉴权失败次数临界值'
          type: integer
          minimum: 3
          maximum: 20
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 3
        GETAUTHADVTH:
          name: '预先取鉴权集门限值'
          type: integer
          minimum: 0
          maximum: 4
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 0
        NCIPH:
          name: '版本协商失败允许不加密'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: YES
        PREGETAUTHSETS:
          name: '是否预取鉴权集'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: YES
        RAUSAUTH:
          name: '是否支持路由更新流程的二次鉴权功能'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NO
        RNUM:
          name: '鉴权集重用次数'
          type: integer
          minimum: 0
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 0
        XIDRESET:
          name: 'Rau Accept无响应后是否启用XID Reset流程'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NO
  examples:
    add_hplmn_list:
    - MCC: '460'
      MNC: '00'
      CC: '86'
      SM: YES
      MAXSMNUM: 11
      SMS: YES
      S5S8TYPE: GTP
      PLMNN: 'name'
      SMSCR: NO
    set_gmm_list:
    - T3322: 6
      N3322: 4
      T3350: 6
      N3350: 4
      T3360: 6
      N3360: 4
      T3370: 6
      N3370: 4
      T3313: 6
      N3313: 2
      PAGINGDELTA: 0
      RDYTMR: 44
      PRDTMR: 54
      MSRCHTMR: 58
      IMDTCHTMR: 0
      T3: 10
      PRT: 0
      RDTDELTA: 0
    add_gbauthciph_list:
    - IMSIPRE: '460001'
      SECPLC: AUTHANDPROTECTED
      CIPHALG: GEA_3-1&GEA_2-1&GEA_1-1
      ATTSAUTH: NO
      AUTHEVENT: ''
      AUTHEVENTTHRESHOLD: 1
      AUTHPERIOD: 24
      AUTHSETSNUMBER: 5
      AUTHSETV2: NO
      CAFTIMES: 3
      GETAUTHADVTH: ''
      NCIPH: YES
      PREGETAUTHSETS: YES
      RAUSAUTH: NO
      RNUM: ''
      XIDRESET: NO
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 进入“MML命令行-UNC”窗口。

### 2 增加归属PLMN配置信息。

```jinja2
{%- for item in add_hplmn_list -%}
    ADD HPLMN:
    {#- --- 必选参数 --- -#}
    MCC="{{item.MCC}}",
    MNC="{{item.MNC}}",
    {#- --- 可选参数 --- -#}
    {%- if item.CC is not none -%}
        CC="{{item.CC}}",
    {%- endif -%}
    {%- if item.SM is not none -%}
        SM={{item.SM}},
    {%- endif -%}
    {%- if item.SMS is not none -%}
        SMS={{item.SMS}},
    {%- endif -%}
    {%- if item.S5S8TYPE is not none -%}
        S5S8TYPE={{item.S5S8TYPE}},
    {%- endif -%}
    {%- if item.PLMNN is not none -%}
        PLMNN="{{item.PLMNN}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：SM=YES 时可选 --- -#}
    {%- if item.SM == 'YES' -%}
        {%- if item.MAXSMNUM is not none -%}
            MAXSMNUM={{item.MAXSMNUM}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SMS=YES 时可选 --- -#}
    {%- if item.SMS == 'YES' -%}
        {%- if item.SMSCR is not none -%}
            SMSCR={{item.SMSCR}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 **可选：**配置2G移动性管理定时器参数。

```jinja2
{%- if is_optional_2g_mobility_timer_parameter -%}
    {%- for item in set_gmm_list -%}
        SET GMM:
        {#- --- 可选参数 --- -#}
        {%- if item.T3322 is not none -%}
            T3322={{item.T3322}},
        {%- endif -%}
        {%- if item.N3322 is not none -%}
            N3322={{item.N3322}},
        {%- endif -%}
        {%- if item.T3350 is not none -%}
            T3350={{item.T3350}},
        {%- endif -%}
        {%- if item.N3350 is not none -%}
            N3350={{item.N3350}},
        {%- endif -%}
        {%- if item.T3360 is not none -%}
            T3360={{item.T3360}},
        {%- endif -%}
        {%- if item.N3360 is not none -%}
            N3360={{item.N3360}},
        {%- endif -%}
        {%- if item.T3370 is not none -%}
            T3370={{item.T3370}},
        {%- endif -%}
        {%- if item.N3370 is not none -%}
            N3370={{item.N3370}},
        {%- endif -%}
        {%- if item.T3313 is not none -%}
            T3313={{item.T3313}},
        {%- endif -%}
        {%- if item.N3313 is not none -%}
            N3313={{item.N3313}},
        {%- endif -%}
        {%- if item.PAGINGDELTA is not none -%}
            PAGINGDELTA={{item.PAGINGDELTA}},
        {%- endif -%}
        {%- if item.RDYTMR is not none -%}
            RDYTMR={{item.RDYTMR}},
        {%- endif -%}
        {%- if item.PRDTMR is not none -%}
            PRDTMR={{item.PRDTMR}},
        {%- endif -%}
        {%- if item.MSRCHTMR is not none -%}
            MSRCHTMR={{item.MSRCHTMR}},
        {%- endif -%}
        {%- if item.IMDTCHTMR is not none -%}
            IMDTCHTMR={{item.IMDTCHTMR}},
        {%- endif -%}
        {%- if item.T3 is not none -%}
            T3={{item.T3}},
        {%- endif -%}
        {%- if item.PRT is not none -%}
            PRT={{item.PRT}},
        {%- endif -%}
        {%- if item.RDTDELTA is not none -%}
            RDTDELTA={{item.RDTDELTA}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 4 **可选：**启用鉴权和加密功能。

```jinja2
{%- if is_optional_auth_cipher -%}
    {%- for item in add_gbauthciph_list -%}
        ADD GBAUTHCIPH:
        {#- --- 必选参数 --- -#}
        IMSIPRE="{{item.IMSIPRE}}",
        {#- --- 可选参数 --- -#}
        {%- if item.SECPLC is not none -%}
            SECPLC={{item.SECPLC}},
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：SECPLC=AUTHANDPROTECTED 时可选 --- -#}
        {%- if item.SECPLC == 'AUTHANDPROTECTED' -%}
            {%- if item.CIPHALG is not none -%}
                CIPHALG={{item.CIPHALG}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：SECPLC=AUTHONLY/AUTHANDPROTECTED 时可选 --- -#}
        {%- if item.SECPLC in ['AUTHONLY', 'AUTHANDPROTECTED'] -%}
            {%- if item.ATTSAUTH is not none -%}
                ATTSAUTH={{item.ATTSAUTH}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：SECPLC=AUTHONLY/AUTHANDPROTECTED 时可选 --- -#}
        {%- if item.SECPLC in ['AUTHONLY', 'AUTHANDPROTECTED'] -%}
            {%- if item.AUTHEVENT is not none -%}
                AUTHEVENT={{item.AUTHEVENT}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：SECPLC=AUTHONLY/AUTHANDPROTECTED 时可选 --- -#}
        {%- if item.SECPLC in ['AUTHONLY', 'AUTHANDPROTECTED'] -%}
            {%- if item.AUTHEVENTTHRESHOLD is not none -%}
                AUTHEVENTTHRESHOLD={{item.AUTHEVENTTHRESHOLD}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：SECPLC=AUTHONLY/AUTHANDPROTECTED 时可选 --- -#}
        {%- if item.SECPLC in ['AUTHONLY', 'AUTHANDPROTECTED'] -%}
            {%- if item.AUTHPERIOD is not none -%}
                AUTHPERIOD={{item.AUTHPERIOD}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：SECPLC=AUTHONLY/AUTHANDPROTECTED 时可选 --- -#}
        {%- if item.SECPLC in ['AUTHONLY', 'AUTHANDPROTECTED'] -%}
            {%- if item.AUTHSETSNUMBER is not none -%}
                AUTHSETSNUMBER={{item.AUTHSETSNUMBER}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：SECPLC=AUTHONLY/AUTHANDPROTECTED 时可选 --- -#}
        {%- if item.SECPLC in ['AUTHONLY', 'AUTHANDPROTECTED'] -%}
            {%- if item.AUTHSETV2 is not none -%}
                AUTHSETV2={{item.AUTHSETV2}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：SECPLC=AUTHONLY/AUTHANDPROTECTED 时可选 --- -#}
        {%- if item.SECPLC in ['AUTHONLY', 'AUTHANDPROTECTED'] -%}
            {%- if item.CAFTIMES is not none -%}
                CAFTIMES={{item.CAFTIMES}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：SECPLC=AUTHONLY/AUTHANDPROTECTED 时可选 --- -#}
        {%- if item.SECPLC in ['AUTHONLY', 'AUTHANDPROTECTED'] -%}
            {%- if item.GETAUTHADVTH is not none -%}
                GETAUTHADVTH={{item.GETAUTHADVTH}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：SECPLC=AUTHANDPROTECTED 时可选 --- -#}
        {%- if item.SECPLC == 'AUTHANDPROTECTED' -%}
            {%- if item.NCIPH is not none -%}
                NCIPH={{item.NCIPH}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：SECPLC=AUTHONLY/AUTHANDPROTECTED 时可选 --- -#}
        {%- if item.SECPLC in ['AUTHONLY', 'AUTHANDPROTECTED'] -%}
            {%- if item.PREGETAUTHSETS is not none -%}
                PREGETAUTHSETS={{item.PREGETAUTHSETS}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：SECPLC=AUTHONLY/AUTHANDPROTECTED 时可选 --- -#}
        {%- if item.SECPLC in ['AUTHONLY', 'AUTHANDPROTECTED'] -%}
            {%- if item.RAUSAUTH is not none -%}
                RAUSAUTH={{item.RAUSAUTH}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：SECPLC=AUTHONLY/AUTHANDPROTECTED 时可选 --- -#}
        {%- if item.SECPLC in ['AUTHONLY', 'AUTHANDPROTECTED'] -%}
            {%- if item.RNUM is not none -%}
                RNUM={{item.RNUM}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：SECPLC=AUTHANDPROTECTED 时可选 --- -#}
        {%- if item.SECPLC == 'AUTHANDPROTECTED' -%}
            {%- if item.XIDRESET is not none -%}
                XIDRESET={{item.XIDRESET}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```


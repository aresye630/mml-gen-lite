---
id: ''
name: 配置运营商信息
ne_type: UNC
type: feature
description: 配置SMF/PGW-C/SGW-C/GGSN本局数据的基本流程包括：开始→配置移动运营商信息→配置PLMN和切片→配置本端NFUUID→配置NF信息→结束。国漫相关配置请参见5GC国际漫游解决方案功能部署。运营商信息详细原理请参见运营商信息是什么。
risk_level: ''
doc_source: ["网络部署","初始配置","UNC初始配置与调测","组网对接配置","配置SMF&PGW-C&SGW-C&GGSN","公共配置","配置本局数据","配置运营商信息"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
配置SMF/PGW-C/SGW-C/GGSN本局数据的基本流程包括：开始→配置移动运营商信息→配置PLMN和切片→配置本端NFUUID→配置NF信息→结束。国漫相关配置请参见5GC国际漫游解决方案功能部署。运营商信息详细原理请参见运营商信息是什么。

## 必备事项
前提条件

前提条件

* 具备管理员权限的操作人员已经登录华为操作维护系统（登录U2020/MAE客户端或登录OM Portal）。

* 已经获取网设LLD文档。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    mod_ngmno_list:
      type: items
      properties:
        NOID:
          name: '运营商标识'
          type: integer
          minimum: 0
          maximum: 0
          required: true
          description: '配置运营商信息。  当前UNC中默认配置一条“NOID”为0的默认记录。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        FULLNAME:
          name: '运营商全称'
          type: string
          minLength: 0
          maxLength: 255
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        SHORTNAME:
          name: '运营商简称'
          type: string
          minLength: 0
          maxLength: 255
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
    add_nghplmn_list:
      type: items
      properties:
        NOID:
          name: '运营商标识'
          type: integer
          minimum: 0
          maximum: 0
          required: true
          description: '配置运营商签约用户的Home PLMN信息。  其中NOID通过**ADD NGMNO**命令配置，可以通过**LST NGMNO**命令查询。当前UNC中默认配置一条“NOID”为0的默认记录，不需单独配置。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        MCC:
          name: '移动国家码'
          type: string
          minLength: 3
          maxLength: 3
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        MNC:
          name: '移动网号'
          type: string
          minLength: 2
          maxLength: 3
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_ngsrvplmn_list:
      type: items
      properties:
        PLMNIDX:
          name: 'PLMN索引'
          type: integer
          minimum: 0
          maximum: 127
          required: true
          description: '配置运营商的Serving PLMN信息。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        NOID:
          name: '运营商标识'
          type: integer
          minimum: 0
          maximum: 0
          required: true
          description: '已通过**ADD NGMNO**命令配置，可以通过**LST NGMNO**命令查询。当前UNC中默认配置一条“NOID”为0的默认记录，不需单独配置。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        MCC:
          name: '移动国家码'
          type: string
          minLength: 3
          maxLength: 3
          required: true
          description: '-'
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
    add_mnclen_list:
      type: items
      properties:
        MCC:
          name: '移动国家码'
          type: string
          minLength: 3
          maxLength: 3
          required: true
          description: '配置各MCC值所对应的MNC长度。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        MNCLEN:
          name: '对应MCC的MNC长度'
          type: integer
          minimum: 2
          maximum: 3
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: 2
    add_plmnns_list:
      type: items
      properties:
        NSIDX:
          name: '网络切片索引'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: true
          description: '配置运营商支持的网络切片。  说明：  如果部署了SMF需要配置该命令；如果仅部署了PGW-C/SGW-C/GGSN则无需配置该命令。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PLMNIDX:
          name: 'PLMN索引'
          type: integer
          minimum: 0
          maximum: 127
          required: true
          description: '已通过**ADD NGSRVPLMN**命令配置，可以通过**LST NGSRVPLMN**命令查询。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SST:
          name: '切片业务类型'
          type: integer
          minimum: 0
          maximum: 255
          required: true
          description: '-'
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
          data_source: ''
          pattern: ''
          default: ''
        STATE:
          name: '状态'
          type: string
          enum:
          - INACTIVE
          - ACTIVE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    mod_ngmno_list:
    - NOID: 0
      FULLNAME: 'Operator A'
      SHORTNAME: 'OA'
      DESC: 'Operator A'
    add_nghplmn_list:
    - NOID: 0
      MCC: '123'
      MNC: '03'
    add_ngsrvplmn_list:
    - PLMNIDX: 0
      NOID: 0
      MCC: '123'
      MNC: '03'
    add_mnclen_list:
    - MCC: '123'
      MNCLEN: 2
    add_plmnns_list:
    - NSIDX: 0
      PLMNIDX: 0
      SST: 1
      SD: '010101'
      STATE: ACTIVE
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 进入“MML命令行-UNC”窗口。

### 2 配置运营商基础信息。当前UNC中默认配置一条“NOID”为0的默认记录，不需单独配置。

#### 2.1 增加运营商信息。

```jinja2
{%- for item in mod_ngmno_list -%}
    MOD NGMNO:
    {#- --- 必选参数 --- -#}
    NOID={{item.NOID}},
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
    ;
{%- endfor -%}
```

#### 2.2 配置运营商签约用户的Home PLMN信息。

```jinja2
{%- for item in add_nghplmn_list -%}
    ADD NGHPLMN:
    {#- --- 必选参数 --- -#}
    NOID={{item.NOID}},
    MCC="{{item.MCC}}",
    MNC="{{item.MNC}}",
    ;
{%- endfor -%}
```

#### 2.3 配置运营商的Serving PLMN信息。

```jinja2
{%- for item in add_ngsrvplmn_list -%}
    ADD NGSRVPLMN:
    {#- --- 必选参数 --- -#}
    PLMNIDX={{item.PLMNIDX}},
    NOID={{item.NOID}},
    MCC="{{item.MCC}}",
    MNC="{{item.MNC}}",
    ;
{%- endfor -%}
```

#### 2.4 配置各MCC值所对应的MNC长度。

```jinja2
{%- for item in add_mnclen_list -%}
    ADD MNCLEN:
    {#- --- 必选参数 --- -#}
    MCC="{{item.MCC}}",
    {#- --- 可选参数 --- -#}
    {%- if item.MNCLEN is not none -%}
        MNCLEN={{item.MNCLEN}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 2.5 配置运营商支持的网络切片。如有多个切片，请依次配置多条记录。

#### 如果部署了SMF需要配置该命令；如果仅部署了PGW-C/SGW-C/GGSN则无需配置该命令。

```jinja2
{%- if is_scenario_smf_deployed -%}
    {%- for item in add_plmnns_list -%}
        ADD PLMNNS:
        {#- --- 必选参数 --- -#}
        NSIDX={{item.NSIDX}},
        PLMNIDX={{item.PLMNIDX}},
        SST={{item.SST}},
        {#- --- 可选参数 --- -#}
        {%- if item.SD is not none -%}
            SD="{{item.SD}}",
        {%- endif -%}
        {%- if item.STATE is not none -%}
            STATE={{item.STATE}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```


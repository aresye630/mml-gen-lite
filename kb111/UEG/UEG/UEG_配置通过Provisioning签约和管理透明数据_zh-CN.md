---
id: ''
name: 配置通过Provisioning签约和管理透明数据
ne_type: UEG
type: feature
description: 本任务旨在指导操作人员通过业务发放系统在IMS-HSS上配置和查询透明数据。  本配置实例在PGW Web LMT客户端上为IMPU（“sip:impu\_test\_01@huawei.com”）增加透明数据和别名透明数据。  配置前需要确保“IMPU别名组ID”为“1”的别名IMPU组已经存在，且“sip:impu\_test\_01@huawei.com”属于此别名IMPU组。请参考**配置别名IMPU组**页面配置别名组。
tags: []
risk_level: ''
doc_source: ["网络部署","园区入驻式（仅连接）","5GC toB 部署边缘站点（站点为“风筝L”，入驻式）","配置业务数据（风筝L）","语音功能配置","HSS&UDM配置","配置通过Provisioning签约和管理透明数据"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
本任务旨在指导操作人员通过业务发放系统在IMS-HSS上配置和查询透明数据。本配置实例在PGW Web LMT客户端上为IMPU（“sip:impu\_test\_01@huawei.com”）增加透明数据和别名透明数据。配置前需要确保“IMPU别名组ID”为“1”的别名IMPU组已经存在，且“sip:impu\_test\_01@huawei.com”属于此别名IMPU组。请参考**配置别名IMPU组**页面配置别名组。

## 必备事项
前提条件

* 操作人员已完全了解GWFD-025802 通过Provisioning签约和管理透明数据特性概述。
* 操作人员具有OM Portal权限。
* 操作人员具有PGW Web LMT客户端业务发放权限。
* 已经完成IMPU为“sip:impu\_test\_01@huawei.com”的用户开户。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    set_dmpecap_list:
      type: items
      properties:
        PEERNAME:
          name: '实体名称'
          type: string
          maxLength: 127
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        OPTYPE:
          name: '操作类型'
          type: string
          enum:
          - ADD
          - MOD
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PEERTYPE:
          name: 'Diameter对端实体类型'
          type: string
          enum:
          - OTHER
          - AS
          - S-CSCF
          - I-CSCF
          - GGSN
          - SAE
          - BSF
          - IMS-HSS
          - E-CSCF
          - P-GW
          - ePDG
          - HSGW
          - Non-3GPP
          - AP
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PR:
          name: '允许Sh-pull的数据类型'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        UR:
          name: '允许Sh-update的数据类型'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NR:
          name: '允许Sh-sub-notify的数据类型'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        HN:
          name: '主机名'
          type: string
          maxLength: 127
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DN:
          name: '域名'
          type: string
          maxLength: 127
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_hsystempara_list:
      type: items
      properties:
        SH_ALIASREPDATA_SUPPORT_DATAREFERENCE0:
          name: 'SH_ALIASREPDATA_SUPPORT_DATAREFERENCE0'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_hrepdata_list:
      type: items
      properties:
        IMPU:
          name: 'IMPU'
          type: string
          required: false
          description: '指定需要设置透明数据的IMPU，输入的IMPU值须符合SIP URI或TEL URI格式。'
          data_source: ''
          pattern: ''
          default: ''
        REPDATA:
          name: 'REPDATA'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        REPTYPE:
          name: 'REPTYPE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_hrepdata_list_1:
      type: items
      properties:
        IMPU:
          name: 'IMPU'
          type: string
          required: false
          description: '指定需要设置透明数据的IMPU，输入的IMPU值须符合SIP URI或TEL URI格式。'
          data_source: ''
          pattern: ''
          default: ''
        REPDATA:
          name: 'REPDATA'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        REPTYPE:
          name: 'REPTYPE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    set_dmpecap_list:
    - PEERNAME: 'HSS_AS'
      OPTYPE: ADD
      PEERTYPE: AS
      PR: REPOSITORYDATA-1&ALIASREPOSITORY-1
      UR: REPOSITORYDATA-1&ALIASREPOSITORY-1
      NR: REPOSITORYDATA-1&ALIASREPOSITORY-1
      HN: 'as111.huawei.com'
      DN: 'huawei.com'
    set_hsystempara_list:
    - SH_ALIASREPDATA_SUPPORT_DATAREFERENCE0: TRUE
    set_hrepdata_list:
    - IMPU: sip:impu_test_01@huawei.com
      REPDATA: <?xml version\=\"1.0\"?><Sh-Data><RepositoryData><ServiceIndication>SI_01</ServiceIndication><SequenceNumber>0</SequenceNumber><ServiceData><any>SH_RSI_DATA</any></ServiceData></RepositoryData></Sh-Data>
      REPTYPE: REPDATA
    set_hrepdata_list_1:
    - IMPU: sip:impu_test_01@huawei.com
      REPDATA: <?xml version\=\"1.0\"?><Sh-Data><Sh-Data-Extension><AliasesRepositoryData><ServiceIndication>ALIASI_SI_01</ServiceIndication><SequenceNumber>0</SequenceNumber><ServiceData><any>alias_repositdata_01</any></ServiceData></AliasesRepositoryData></Sh-Data-Extension></Sh-Data>
      REPTYPE: ALIASREPDATA
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 登录“UEG MML命令”界面。

### 2 执行**SET DMPECAP**命令设置对端AS的实体能力。

```jinja2
{%- for item in set_dmpecap_list -%}
    SET DMPECAP:
    {#- --- 必选参数 --- -#}
    PEERNAME="{{item.PEERNAME}}",
    PEERTYPE={{item.PEERTYPE}},
    {#- --- 可选参数 --- -#}
    {%- if item.OPTYPE is not none -%}
        OPTYPE={{item.OPTYPE}},
    {%- endif -%}
    {%- if item.HN is not none -%}
        HN="{{item.HN}}",
    {%- endif -%}
    {%- if item.DN is not none -%}
        DN="{{item.DN}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：PEERTYPE=AS 时可选 --- -#}
    {%- if item.PEERTYPE == 'AS' -%}
        {%- if item.PR is not none -%}
            PR={{item.PR}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：PEERTYPE=AS 时可选 --- -#}
    {%- if item.PEERTYPE == 'AS' -%}
        {%- if item.UR is not none -%}
            UR={{item.UR}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：PEERTYPE=AS 时可选 --- -#}
    {%- if item.PEERTYPE == 'AS' -%}
        {%- if item.NR is not none -%}
            NR={{item.NR}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 登录“IMS-HSS业务管理”窗口。

### 4 执行**SET HSYSTEMPARA**设置系统支持通过“datareference”取值为“0”来处理别名透明数据。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_hsystempara_list的变量区（command: SET HSYSTEMPARA） -#}
<!-- MISSING_MACRO: command=SET HSYSTEMPARA list_name=set_hsystempara_list step_id=4 -->
```

### Sh接口所有消息对透明数据和别名透明数据的处理，通过该命令中的参数“别名透明数据是否支持datareference为0”来设置。

### TRUE：IMS-HSS支持通过“datareference”取值为“0”来处理别名透明数据。

### FALSE：IMS-HSS不支持通过“datareference”取值为“0”来处理别名透明数据，只能通过“datareference”取值为“20”来处理。

### 5 执行**SET HREPDATA**命令为IMPU（sip:impu\_test\_01@huawei.com）增加一个透明数据。 参数“REPTYPE”取值为“REPDATA”。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_hrepdata_list的变量区（command: SET HREPDATA） -#}
<!-- MISSING_MACRO: command=SET HREPDATA list_name=set_hrepdata_list step_id=5 -->
```

### 6 执行**SET HREPDATA**命令，给别名IMPU组新增一个别名透明数据。参数“REPTYPE”取值为“ALIASREPDATA”。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_hrepdata_list_1的变量区（command: SET HREPDATA） -#}
<!-- MISSING_MACRO: command=SET HREPDATA list_name=set_hrepdata_list_1 step_id=6 -->
```


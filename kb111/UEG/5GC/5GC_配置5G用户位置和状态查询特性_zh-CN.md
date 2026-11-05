---
id: ''
name: 配置5G用户位置和状态查询特性
ne_type: UEG
type: feature
description: 该任务指导操作人员配置5G用户位置与状态查询功能。
tags: []
risk_level: ''
doc_source: ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（火电专网，入驻式）","部署配置指导","中心园区部署入驻式UEG-L","配置业务数据（风筝L）","语音功能配置","HSS&UDM配置","配置5G用户位置和状态查询特性"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
该任务指导操作人员配置5G用户位置与状态查询功能。

## 必备事项
前提条件

* 请仔细阅读WHFD-460503 5G用户位置和状态查询特性概述功能。
* 5G用户已开通VoLTE业务。
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
          description: '该参数必须先由**ADD DMPE**命令的参数“EN”定义，然后才能在此处引用。'
          data_source: '本端规划'
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
          data_source: '固定取值。'
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
          data_source: '固定取值。'
          pattern: ''
          default: ''
        PR:
          name: '允许Sh-pull的数据类型'
          type: string
          required: false
          description: '用于在UDM的配置数据库中定义一个AS设备能够从UDM读取（sh-pull）操作的数据类型。  LOCATIONINFORMATION为位置信息。  USERSTATE为状态信息。  该参数为一个位域型数据，每一位对应于一种数据类型的操作标志：  * 置为“1”，表示允许。 * 置为“0”，表示禁止。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        HN:
          name: '主机名'
          type: string
          maxLength: 127
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        DN:
          name: '域名'
          type: string
          maxLength: 127
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    set_hsystempara_list:
      type: items
      properties:
        NGC_LOC_USERSTATE_TAG_CTRL:
          name: '控制在Sh接口的5G位置和5G用户状态的XML标签格式'
          type: string
          required: false
          description: '用于设置5G用户位置和5G用户状态的XML标签为5GSLocationInformation和5GSUserState。'
          data_source: '本端规划'
          pattern: ''
          default: ''
  examples:
    set_dmpecap_list:
    - PEERNAME: 'AS_0'
      OPTYPE: ADD
      PEERTYPE: AS
      PR: LOCATIONINFORMATION-1&USERSTATE-1
      HN: 'as.huawei.com'
      DN: 'huawei.com'
    set_hsystempara_list:
    - NGC_LOC_USERSTATE_TAG_CTRL: TRUE
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 登录“UEG MML命令”界面。

### 2 执行**SET DMPECAP**命令，配置支持AS读取5G用户的位置与状态信息功能。

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
    ;
{%- endfor -%}
```

### 3 登录“IMS-HSS业务管理”窗口。

### 4 执行**SET HSYSTEMPARA**命令，配置Sh接口的5G用户位置和5G用户状态的XML标签格式。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_hsystempara_list的变量区（command: SET HSYSTEMPARA） -#}
<!-- MISSING_MACRO: command=SET HSYSTEMPARA list_name=set_hsystempara_list step_id=4 -->
```


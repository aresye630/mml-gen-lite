---
id: ''
name: 配置5G UE可达性订阅和通知特性
ne_type: UEG
type: feature
description: 该任务指导操作人员配置UEG支持UE可达性订阅和通知特性。
tags: []
risk_level: ''
doc_source:
  - ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（一号通专网煤矿场景，入驻式）","配置基础业务","在UEG上配置业务数据","语音功能配置","HSS&UDM配置","配置5G UE可达性订阅和通知特性"]
  - ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（一号通专网核电场景，入驻式）","配置基础业务","在UEG上配置业务数据","语音功能配置","HSS&UDM配置","配置5G UE可达性订阅和通知特性"]
  - ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（一号通专网通用场景，入驻式）","配置基础业务","在UEG上配置业务数据","语音功能配置","HSS&UDM配置","配置5G UE可达性订阅和通知特性"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
该任务指导操作人员配置UEG支持UE可达性订阅和通知特性。

## 必备事项
前提条件

请仔细阅读GWFD-025809 5G UE可达性订阅和通知。
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
          description: '该参数必须先由**ADD DMPE**命令定义，然后才能在此处引用。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        OPTYPE:
          name: '操作类型'
          type: string
          enum:
          - ADD
          - MOD
          required: false
          description: '-'
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
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: ''
        NR:
          name: '允许Sh-sub-notify的数据类型'
          type: string
          required: false
          description: '表示允许订阅终端IP可达性数据。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        HN:
          name: '主机名'
          type: string
          maxLength: 127
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        DN:
          name: '域名'
          type: string
          maxLength: 127
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
  examples:
    set_dmpecap_list:
    - PEERNAME: 'AS'
      OPTYPE: ADD
      PEERTYPE: AS
      NR: UEREACHABILITYFORIP-1
      HN: 'as.huawei.com'
      DN: 'huawei.com'
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 登录“UEG MML命令”界面。

### 2 执行**SET DMPECAP**命令配置对端AS可获取数据权限。

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
        {%- if item.NR is not none -%}
            NR={{item.NR}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```


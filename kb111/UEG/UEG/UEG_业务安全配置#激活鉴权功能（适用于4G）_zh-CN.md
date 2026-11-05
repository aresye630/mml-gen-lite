---
id: ''
name: 激活鉴权功能（适用于4G）
ne_type: UEG
type: feature
description: 本操作指导介绍在运行网络中激活鉴权功能特性的操作过程。  鉴权功能实现对用户的身份识别和鉴权以及密钥的同步，该功能对用户身份有效性的判断，使合法用户能使用网络提供的业务。鉴权过程和移动性管理相关过程关联发生。  适用于MME。
tags: []
risk_level: ''
doc_source:
  - ["网络部署","园区入驻式（仅连接）","5GC toB 部署边缘站点（站点为“风筝L”，入驻式）","配置安全数据（风筝L）","安全配置（虚机容器）","安全配置建议","必选配置","业务安全配置","激活鉴权功能（适用于4G）"]
  - ["网络部署","园区入驻式（仅连接）","5GC toB 部署边缘站点（站点为“风筝L”，入驻式）","配置安全数据（风筝L）","安全配置（裸机容器）","安全配置建议","必选配置","业务安全配置","激活鉴权功能（适用于4G）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
本操作指导介绍在运行网络中激活鉴权功能特性的操作过程。鉴权功能实现对用户的身份识别和鉴权以及密钥的同步，该功能对用户身份有效性的判断，使合法用户能使用网络提供的业务。鉴权过程和移动性管理相关过程关联发生。适用于MME。

## 必备事项
前提条件

* 请仔细阅读GWFD-021503 鉴权功能特性概述（适用于4G）。

* EPS网络中各网元系统及操作维护台运行正常。
* 用户在HSS中已签约EPS业务。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    mod_s1usrsecpara_list:
      type: items
      properties:
        USRRANGE:
          name: '用户范围'
          type: string
          enum:
          - DEFAULT
          - SPECIAL
          required: true
          description: '修改用户的安全配置'
          data_source: '全网规划'
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
          data_source: '全网规划'
          pattern: ''
          default: ''
        SUPTCIPHAGTH:
          name: '加密算法'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        SUPTINTAGTH:
          name: '完整性算法'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
  examples:
    mod_s1usrsecpara_list:
    - USRRANGE: DEFAULT
      SECPLC: AUTHANDPROTECTED
      SUPTCIPHAGTH: EEA2-1
      SUPTINTAGTH: EIA2-1
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 进入“MML命令行-UEG”窗口。

### 2 打开鉴权加密开关。

```jinja2
{%- for item in mod_s1usrsecpara_list -%}
    MOD S1USRSECPARA:
    {#- --- 必选参数 --- -#}
    USRRANGE={{item.USRRANGE}},
    {#- --- 可选参数 --- -#}
    {%- if item.SECPLC is not none -%}
        SECPLC={{item.SECPLC}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：SECPLC=AUTHANDPROTECTED 时可选 --- -#}
    {%- if item.SECPLC == 'AUTHANDPROTECTED' -%}
        {%- if item.SUPTCIPHAGTH is not none -%}
            SUPTCIPHAGTH={{item.SUPTCIPHAGTH}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SECPLC=AUTHANDPROTECTED 时可选 --- -#}
    {%- if item.SECPLC == 'AUTHANDPROTECTED' -%}
        {%- if item.SUPTINTAGTH is not none -%}
            SUPTINTAGTH={{item.SUPTINTAGTH}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### “用户范围”固定选择“DEFAULT”（缺省）

### “安全策略”固定选择“AUTHANDPROTECTED”(鉴权并保护)


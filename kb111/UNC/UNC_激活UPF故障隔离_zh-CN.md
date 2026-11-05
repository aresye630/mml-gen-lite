---
id: ''
name: 激活UPF故障隔离
ne_type: UNC
type: feature
description: 当网络中存在基站与UPF链路故障或者N4接口故障时，可以参考本章节激活UPF故障隔离特性，使SMF在选择UPF时屏蔽故障的用户面网元。  适用于SMF。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","容灾功能","WSFD-213005 UPF故障隔离","激活UPF故障隔离"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
当网络中存在基站与UPF链路故障或者N4接口故障时，可以参考本章节激活UPF故障隔离特性，使SMF在选择UPF时屏蔽故障的用户面网元。适用于SMF。

## 必备事项
前提条件

* 请仔细阅读WSFD-213005 UPF故障隔离特性概述。
* 已在SMF侧通过**ADD UPNODE**增加故障的UPF。
* 已激活WSFD-107010 UPF选择特性，详细操作请参考WSFD-107010 UPF选择。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    add_faultrangrp_list:
      type: items
      properties:
        RANGRPNAME:
          name: 'RAN组名'
          type: string
          minLength: 1
          maxLength: 32
          required: true
          description: '增加故障RAN组。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_faultranbindgrp_list:
      type: items
      properties:
        PLMN:
          name: 'PLMN'
          type: string
          minLength: 5
          maxLength: 6
          required: true
          description: '在故障RAN组中增加故障基站。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        RANNODETYPE:
          name: 'RAN基站类型'
          type: string
          enum:
          - MACROENB
          - SHORTENB
          - LONGENB
          - GNB
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        RANNODEID:
          name: 'RAN基站标识'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        NODEIDLEN:
          name: 'RAN基站标识长度(比特)'
          type: integer
          minimum: 18
          maximum: 32
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        RANGRPNAME:
          name: 'RAN组名称'
          type: string
          minLength: 1
          maxLength: 32
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_faultupgrp_list:
      type: items
      properties:
        UPFGRPNAME:
          name: 'UPF组名'
          type: string
          minLength: 1
          maxLength: 32
          required: true
          description: '增加故障UPF组。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_faultupbindgrp_list:
      type: items
      properties:
        UPFID:
          name: 'UPF实例标识'
          type: string
          minLength: 1
          maxLength: 36
          required: true
          description: '在故障UPF组中增加故障UPF。  “UPF实例标识（UPFID）”可以通过**LST UPNODE**查询。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        UPFGRPNAME:
          name: 'UPF组名'
          type: string
          minLength: 1
          maxLength: 32
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_faultupbindran_list:
      type: items
      properties:
        RANGRPNAME:
          name: 'RAN组名'
          type: string
          minLength: 1
          maxLength: 32
          required: true
          description: '绑定故障的RAN组和UPF组。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        UPFGRPNAME:
          name: 'UPF组名'
          type: string
          minLength: 1
          maxLength: 32
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_t1n1para_list:
      type: items
      properties:
        MSGTYPE:
          name: '消息类型'
          type: string
          enum:
          - AssocSetUp
          - AssocUpdate
          - AssocRelease
          - SessionEstablish
          - SessionModify
          - SessionDelete
          required: true
          description: '配置不同类型消息的超时间隔和发送次数阈值。此处理以PFCP Modification Request消息为例。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        T1:
          name: '超时间隔'
          type: integer
          minimum: 1
          maximum: 20
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        N1:
          name: '发送次数阈值'
          type: integer
          minimum: 1
          maximum: 6
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_pfcppara_list:
      type: items
      properties:
        HBINTERVAL:
          name: '心跳间隔(秒)'
          type: integer
          minimum: 15
          maximum: 300
          required: false
          description: '配置PFCP路径管理参数，使能PFCP修改请求消息重发优化开关。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        HBT1:
          name: '心跳消息超时间隔(秒)'
          type: integer
          minimum: 1
          maximum: 20
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        HBN1:
          name: '心跳消息发送次数阈值'
          type: integer
          minimum: 1
          maximum: 6
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        DEACTIVEFLAG:
          name: '去活用户开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        DACTINTERVAL:
          name: '去活间隔(秒)'
          type: integer
          minimum: 0
          maximum: 1800
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        MODREQRSOPTSW:
          name: 'PFCP修改请求消息重发优化开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
  examples:
    add_faultrangrp_list:
    - RANGRPNAME: 'RANGRP1'
    add_faultranbindgrp_list:
    - PLMN: '12399'
      RANNODETYPE: GNB
      RANNODEID: 327697
      NODEIDLEN: 24
      RANGRPNAME: 'RANGRP1'
    add_faultupgrp_list:
    - UPFGRPNAME: 'UPFGRP1'
    add_faultupbindgrp_list:
    - UPFID: 'UPF1'
      UPFGRPNAME: 'UPFGRP1'
    add_faultupbindran_list:
    - RANGRPNAME: 'RANGRP1'
      UPFGRPNAME: 'UPFGRP1'
    set_t1n1para_list:
    - MSGTYPE: SessionModify
      T1: 2
      N1: 2
    set_pfcppara_list:
    - HBINTERVAL: 30
      HBT1: 3
      HBN1: 5
      DEACTIVEFLAG: ENABLE
      DACTINTERVAL: 900
      MODREQRSOPTSW: ENABLE
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 增加故障RAN组。

```jinja2
{%- for item in add_faultrangrp_list -%}
    ADD FAULTRANGRP:
    {#- --- 必选参数 --- -#}
    RANGRPNAME="{{item.RANGRPNAME}}",
    ;
{%- endfor -%}
```

### 2 在故障RAN组中增加故障基站。

```jinja2
{%- for item in add_faultranbindgrp_list -%}
    ADD FAULTRANBINDGRP:
    {#- --- 必选参数 --- -#}
    PLMN="{{item.PLMN}}",
    RANNODETYPE={{item.RANNODETYPE}},
    RANNODEID={{item.RANNODEID}},
    NODEIDLEN={{item.NODEIDLEN}},
    RANGRPNAME="{{item.RANGRPNAME}}",
    ;
{%- endfor -%}
```

### 3 增加故障UPF组。

```jinja2
{%- for item in add_faultupgrp_list -%}
    ADD FAULTUPGRP:
    {#- --- 必选参数 --- -#}
    UPFGRPNAME="{{item.UPFGRPNAME}}",
    ;
{%- endfor -%}
```

### 4 在故障UPF组中增加故障UPF。

```jinja2
{%- for item in add_faultupbindgrp_list -%}
    ADD FAULTUPBINDGRP:
    {#- --- 必选参数 --- -#}
    UPFID="{{item.UPFID}}",
    UPFGRPNAME="{{item.UPFGRPNAME}}",
    ;
{%- endfor -%}
```

### 5 绑定故障的RAN组和UPF组。

```jinja2
{%- for item in add_faultupbindran_list -%}
    ADD FAULTUPBINDRAN:
    {#- --- 必选参数 --- -#}
    RANGRPNAME="{{item.RANGRPNAME}}",
    UPFGRPNAME="{{item.UPFGRPNAME}}",
    ;
{%- endfor -%}
```

### 6 配置不同类型消息的超时间隔和发送次数阈值。

```jinja2
{%- for item in set_t1n1para_list -%}
    SET T1N1PARA:
    {#- --- 必选参数 --- -#}
    MSGTYPE={{item.MSGTYPE}},
    {#- --- 可选参数 --- -#}
    {%- if item.T1 is not none -%}
        T1={{item.T1}},
    {%- endif -%}
    {%- if item.N1 is not none -%}
        N1={{item.N1}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 7 配置PFCP路径管理参数，使能PFCP修改请求消息重发优化开关。

```jinja2
{%- for item in set_pfcppara_list -%}
    SET PFCPPARA:
    {#- --- 可选参数 --- -#}
    {%- if item.HBINTERVAL is not none -%}
        HBINTERVAL={{item.HBINTERVAL}},
    {%- endif -%}
    {%- if item.HBT1 is not none -%}
        HBT1={{item.HBT1}},
    {%- endif -%}
    {%- if item.HBN1 is not none -%}
        HBN1={{item.HBN1}},
    {%- endif -%}
    {%- if item.DEACTIVEFLAG is not none -%}
        DEACTIVEFLAG={{item.DEACTIVEFLAG}},
    {%- endif -%}
    {%- if item.MODREQRSOPTSW is not none -%}
        MODREQRSOPTSW={{item.MODREQRSOPTSW}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：DEACTIVEFLAG=ENABLE 时可选 --- -#}
    {%- if item.DEACTIVEFLAG == 'ENABLE' -%}
        {%- if item.DACTINTERVAL is not none -%}
            DACTINTERVAL={{item.DACTINTERVAL}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```


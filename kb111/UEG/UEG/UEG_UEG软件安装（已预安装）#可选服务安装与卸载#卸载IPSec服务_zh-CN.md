---
id: ''
name: 卸载IPSec服务
ne_type: UEG
type: feature
description: 当运营商不需要IPSec服务或IPSec服务动态上线失败时，可以单独卸载IPSec pod，从而下线IPSec服务。
tags: []
risk_level: ''
doc_source: ["网络部署","园区入驻式（仅连接）","5GC toB 部署边缘站点（站点为“风筝L”，入驻式）","UEG软件安装（风筝L）","基于生产预安装（裸机容器）","UEG软件安装（已预安装）","可选服务安装与卸载","卸载IPSec服务"]
refs: []
metadata:
  DepOnLiveCfg: true
allowed-tools:
- getParameterValue('LST FWSOFTPARA')
---
<!-- @mml:block= annotations -->
```text
## 操作场景
当运营商不需要IPSec服务或IPSec服务动态上线失败时，可以单独卸载IPSec pod，从而下线IPSec服务。

## 必备事项
前提条件

* 已经完成网络设计，已规划下线IPSec pod的类型和数量。
* 已经规划IPSec pod关联的其他组件的类型和数量，例如CSLB、CSDB、IPU、SDU，卸载IPSec服务后，请联系华为技术支持工程师缩容关联组件。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    set_fwsoftpara_list:
      type: items
      properties:
        PARAMETERSTYPE:
          name: '参数类型'
          type: string
          enum:
          - DWORD
          - DWORD_EX
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DWORDINDEX:
          name: 'DWORD索引'
          type: integer
          minimum: 1
          maximum: 2048
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DWORDVALUE:
          name: 'DWORD取值'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    opr_featuredisable_list:
      type: items
      properties:
        PODTYPE:
          name: 'Pod类型列表'
          type: string
          minLength: 0
          maxLength: 1024
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        DISABLETYPE:
          name: '下线方式'
          type: string
          enum:
          - Normal
          - Force
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: Normal
        FUNCTIONSETNAME:
          name: '网络功能集名称'
          type: string
          minLength: 0
          maxLength: 1024
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
    set_fwsoftpara_list_1:
      type: items
      properties:
        PARAMETERSTYPE:
          name: '参数类型'
          type: string
          enum:
          - DWORD
          - DWORD_EX
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DWORDINDEX:
          name: 'DWORD索引'
          type: integer
          minimum: 1
          maximum: 2048
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DWORDVALUE:
          name: 'DWORD取值'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    set_fwsoftpara_list:
    - PARAMETERSTYPE: DWORD
      DWORDINDEX: 521
      DWORDVALUE: 1
    opr_featuredisable_list:
    - PODTYPE: 'ipsecexec-c4-pod/ipsecctl-pod'
      DISABLETYPE: Normal
      FUNCTIONSETNAME: 'IPSec'
    set_fwsoftpara_list_1:
    - PARAMETERSTYPE: DWORD
      DWORDINDEX: 521
      DWORDVALUE: 0
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 登录OM Portal。

### 2 执行**SET FWSOFTPARA**命令（UEG-M和UEG-L在UEG视图），开启Service Fabric软参。

```jinja2
{%- for item in set_fwsoftpara_list -%}
    SET FWSOFTPARA:
    {#- --- 必选参数 --- -#}
    PARAMETERSTYPE={{item.PARAMETERSTYPE}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：PARAMETERSTYPE=DWORD 时必选 --- -#}
    {%- if item.PARAMETERSTYPE == 'DWORD' -%}
        DWORDINDEX={{item.DWORDINDEX}},
    {%- endif -%}
    {#- --- 条件必选：PARAMETERSTYPE=DWORD 时必选 --- -#}
    {%- if item.PARAMETERSTYPE == 'DWORD' -%}
        DWORDVALUE={{item.DWORDVALUE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 执行**LST FWSOFTPARA**命令（UEG-M和UEG-L在UEG视图），确认Service Fabric软参值是否为1。

### 如果软参值为1，请执行后续步骤。如果软参值不是1，请联系华为技术支持。

### 3 执行命令（UEG-M和UEG-L在UEG视图），动态下线IPSec pod。

```jinja2
{%- set LST_FWSOFTPARA=getParameterValue('LST FWSOFTPARA') -%}
{%- if LST_FWSOFTPARA=='1' -%}
    {%- for item in opr_featuredisable_list -%}
        OPR FEATUREDISABLE:
        {#- --- 必选参数 --- -#}
        PODTYPE="{{item.PODTYPE}}",
        {#- --- 可选参数 --- -#}
        {%- if item.DISABLETYPE is not none -%}
            DISABLETYPE={{item.DISABLETYPE}},
        {%- endif -%}
        {%- if item.FUNCTIONSETNAME is not none -%}
            FUNCTIONSETNAME="{{item.FUNCTIONSETNAME}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 4 执行命令（UEG-M和UEG-L在UEG视图），确认已经成功下线IPSec pod。

### 回显为“处理结果=处理成功”。

### 执行命令（UEG-M和UEG-L在CSP视图），确认POD已下线。

### 回显为“查询Pod不存在”。

### 5 执行**SET FWSOFTPARA**命令（UEG-M和UEG-L在UEG视图），关闭Service Fabric软参。

```jinja2
{%- if LST_FWSOFTPARA=='1' -%}
    {%- for item in set_fwsoftpara_list_1 -%}
        SET FWSOFTPARA:
        {#- --- 必选参数 --- -#}
        PARAMETERSTYPE={{item.PARAMETERSTYPE}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：PARAMETERSTYPE=DWORD 时必选 --- -#}
        {%- if item.PARAMETERSTYPE == 'DWORD' -%}
            DWORDINDEX={{item.DWORDINDEX}},
        {%- endif -%}
        {#- --- 条件必选：PARAMETERSTYPE=DWORD 时必选 --- -#}
        {%- if item.PARAMETERSTYPE == 'DWORD' -%}
            DWORDVALUE={{item.DWORDVALUE}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 执行**LST FWSOFTPARA**命令（UEG-M和UEG-L在UEG视图），确认Service Fabric软参值是否为0。

### 如果软参值为0，请执行后续步骤。如果软参值不是0，请联系华为技术支持。


---
id: ''
name: 一键式下线IPSec服务
ne_type: UEG
type: feature
description: 当运营商不需要IPSec服务或IPSec服务一键式动态上线失败时，可以单独卸载IPSec pod，从而一键式下线IPSec服务。
tags: []
risk_level: ''
doc_source:
  - ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（电力专网，入驻式）","软件安装与初始配置","部署UEG","电力专网采用风筝S部署模式","UEG软件安装","裸机容器模式UEG软件安装（已预安装）","UEG软件安装（已预安装）","可选服务安装与卸载","一键式下线IPSec服务"]
  - ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（火电专网，入驻式）","部署配置指导","子园区部署入驻式UEG-S","子园区UEG-S软件安装","裸机容器模式UEG软件安装（已预安装）","UEG软件安装（已预安装）","可选服务安装与卸载","一键式下线IPSec服务"]
refs: []
metadata:
  DepOnLiveCfg: true
allowed-tools:
- getParameterValue('LST FWSOFTPARA')
---
<!-- @mml:block= annotations -->
```text
## 操作场景
当运营商不需要IPSec服务或IPSec服务一键式动态上线失败时，可以单独卸载IPSec pod，从而一键式下线IPSec服务。

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
    opr_oneclickdeploy_list:
      type: items
      properties:
        OPRTYPE:
          name: '操作类型'
          type: string
          enum:
          - INDEPSTACKENABLE
          - INDEPSTACKDISABLE
          - FEATUREENABLE
          - FEATUREDISABLE
          - SCALEOUT
          - SCALEIN
          - DELETE
          - RETRY
          - ROLLBACK
          required: true
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
        FUNCTIONSETNAME:
          name: '方法集名称'
          type: string
          minLength: 0
          maxLength: 256
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
        PROCESSTYPE:
          name: '处理方式'
          type: string
          enum:
          - Normal
          - Force
          required: false
          description: ''
          data_source: '本端规划'
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
    opr_oneclickdeploy_list:
    - OPRTYPE: FEATUREDISABLE
      FUNCTIONSETNAME: 'IPSec'
      PROCESSTYPE: Normal
    set_fwsoftpara_list_1:
    - PARAMETERSTYPE: DWORD
      DWORDINDEX: 521
      DWORDVALUE: 0
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 登录OM Portal。

### 2 执行**SET FWSOFTPARA**命令，开启Service Fabric软参。

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

### 执行**LST FWSOFTPARA**命令，确认Service Fabric软参值是否为1。

### 如果软参值为1，请执行后续步骤。如果软参值不是1，请联系华为技术支持。

### 3 执行**OPR ONECLICKDEPLOY**命令，一键式下线IPSec服务。

```jinja2
{%- set LST_FWSOFTPARA=getParameterValue('LST FWSOFTPARA') -%}
{%- if LST_FWSOFTPARA=='1' -%}
    {%- for item in opr_oneclickdeploy_list -%}
        OPR ONECLICKDEPLOY:
        {#- --- 必选参数 --- -#}
        OPRTYPE={{item.OPRTYPE}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：OPRTYPE=INDEPSTACKENABLE/FEATUREENABLE/FEATUREDISABLE 时必选 --- -#}
        {%- if item.OPRTYPE in ['INDEPSTACKENABLE', 'FEATUREENABLE', 'FEATUREDISABLE'] -%}
            FUNCTIONSETNAME="{{item.FUNCTIONSETNAME}}",
        {%- endif -%}
        {#- --- 条件必选：OPRTYPE=FEATUREDISABLE 时必选 --- -#}
        {%- if item.OPRTYPE == 'FEATUREDISABLE' -%}
            PROCESSTYPE={{item.PROCESSTYPE}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 4 执行**DSP ONECLICKDEPLOYHIST**命令，确认一键式下线IPSec服务的回显为“处理结果=处理成功”。

### 5 执行命令，确认POD已下线。

### 回显为“查询Pod不存在”。

### 6 执行**SET FWSOFTPARA**命令，关闭Service Fabric软参。

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

### 执行**LST FWSOFTPARA**命令，确认Service Fabric软参值是否为0。

### 如果软参值为0，请执行后续步骤。如果软参值不是0，请联系华为技术支持。


---
id: ''
name: 卸载IPsec服务（UPF）
ne_type: UEG
type: feature
description: 当运营商不需要IPsec服务或IPsec服务动态上线失败时，可以单独卸载IPsec pod，从而下线IPsec服务。
tags: []
risk_level: ''
doc_source: ["网络部署","园区入驻式（仅连接）","5GC toB 部署边缘站点（站点为“风筝M”，入驻式）","UEG软件安装（风筝M）","基于中心VNF LCM安装UEG（虚机容器）","VNF LCM安装UEG","卸载UEG","卸载IPsec服务（UPF）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
当运营商不需要IPsec服务或IPsec服务动态上线失败时，可以单独卸载IPsec pod，从而下线IPsec服务。

## 必备事项
前提条件

* 已经完成网络设计，已规划下线IPsec pod的类型和数量。
* 已经规划IPsec pod关联的其他组件的类型和数量，卸载IPsec服务后，请联系华为技术支持工程师缩容关联组件。
* 如果动态下线失败，只能继续重新触发动态下线任务。
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
      FUNCTIONSETNAME: 'IPsec'
    set_fwsoftpara_list_1:
    - PARAMETERSTYPE: DWORD
      DWORDINDEX: 521
      DWORDVALUE: 0
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 登录UEG OM Portal。

### 2 执行**SET FWSOFTPARA**命令（UEG-M和UEG-L在UEG视图），开启Service Fabric的**DWORD\_521**软参，即系统故障时不触发容灾导致的联动复位。

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

### 3 执行命令（UEG-M和UEG-L在UEG视图），动态下线IPsec pod。

```jinja2
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
```

### 4 执行命令（UEG-M和UEG-L在UEG视图），确认已经成功下线IPsec pod。

### 回显为“处理结果=处理成功”。

### 执行命令（UEG-M和UEG-L在CSP视图），确认pod已下线。

### 回显为“查询Pod不存在”。

### 5 执行**SET FWSOFTPARA**命令（UEG-M和UEG-L在UEG视图），关闭Service Fabric的**DWORD\_521**软参，即系统故障时触发容灾导致的联动复位。

```jinja2
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
```

### 执行**LST FWSOFTPARA**命令（UEG-M和UEG-L在UEG视图），确认Service Fabric软参值是否为0。

### 如果软参值为0，请执行后续步骤。如果软参值不是0，请联系华为技术支持。

### 6 若动态下线IPsec服务后，不再上线IPsec服务，则需要缩容IPsec自身VM（PBU\_P-I\_C4），释放VM资源。

### 若后续还需要上线IPsec服务，则不必缩容IPsec自身VM。

### **缩容VM**：请参见《UEG扩缩容指导书》。


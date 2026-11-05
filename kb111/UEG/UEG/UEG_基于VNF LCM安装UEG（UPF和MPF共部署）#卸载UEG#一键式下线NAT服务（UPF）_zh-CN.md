---
id: ''
name: 一键式下线NAT服务（UPF）
ne_type: UEG
type: feature
description: 当运营商不需要NAT服务或NAT服务一键式动态上线失败时，可以单独卸载NAT pod，从而一键式下线NAT服务。
tags: []
risk_level: ''
doc_source: ["网络部署","园区入驻+地市共享（连接+计算）","5GC toB 部署边缘站点（站点为“风筝S”，带计算）","UEG软件安装（风筝S）","安装UPF和MPF（共部署）","基于VNF LCM安装UEG（UPF和MPF共部署）","卸载UEG","一键式下线NAT服务（UPF）"]
refs: []
metadata:
  DepOnLiveCfg: true
allowed-tools:
- getParameterValue('LST FWSOFTPARA')
---
<!-- @mml:block= annotations -->
```text
## 操作场景
当运营商不需要NAT服务或NAT服务一键式动态上线失败时，可以单独卸载NAT pod，从而一键式下线NAT服务。

## 必备事项
前提条件

* LCM版本不低于V100R024C10。
* 已经完成网络设计，已规划下线NAT pod的类型和数量。
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
        NODETYPELIST:
          name: '节点类型列表'
          type: string
          minLength: 0
          maxLength: 256
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        STACKNAME:
          name: '堆栈名称'
          type: string
          minLength: 0
          maxLength: 1024
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
    - OPRTYPE: INDEPSTACKDISABLE
      NODETYPELIST: 'PBU_E-N_C6_ARM:0'
      STACKNAME: 'ueg-nat-xx'
    set_fwsoftpara_list_1:
    - PARAMETERSTYPE: DWORD
      DWORDINDEX: 521
      DWORDVALUE: 0
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 登录UEG OM Portal。

### 2 执行**SET FWSOFTPARA**命令，开启Service Fabric的**DWORD\_521**软参，即系统故障时不触发容灾导致的联动复位。

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

### 3 执行**DSP VNFSTACKNAMES**命令，查询出前缀为“ueg-nat”的NAT堆栈名称。

### 4 执行**OPR ONECLICKDEPLOY**命令，一键式下线NAT的VM和Pod。以PBU\_E-N\_C6\_ARM虚拟机为例，其他虚拟机请替换为配套pod。

```jinja2
{%- set LST_FWSOFTPARA=getParameterValue('LST FWSOFTPARA') -%}
{%- if LST_FWSOFTPARA=='1' -%}
    {%- for item in opr_oneclickdeploy_list -%}
        OPR ONECLICKDEPLOY:
        {#- --- 必选参数 --- -#}
        OPRTYPE={{item.OPRTYPE}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：OPRTYPE=INDEPSTACKDISABLE 时必选 --- -#}
        {%- if item.OPRTYPE == 'INDEPSTACKDISABLE' -%}
            STACKNAME="{{item.STACKNAME}}",
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：OPRTYPE=INDEPSTACKENABLE/INDEPSTACKDISABLE/FEATUREENABLE/FEATUREDISABLE/SCALEOUT/SCALEIN 时可选 --- -#}
        {%- if item.OPRTYPE in ['INDEPSTACKENABLE', 'INDEPSTACKDISABLE', 'FEATUREENABLE', 'FEATUREDISABLE', 'SCALEOUT', 'SCALEIN'] -%}
            {%- if item.NODETYPELIST is not none -%}
                NODETYPELIST="{{item.NODETYPELIST}}",
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 5 执行**DSP ONECLICKDEPLOYHIST**命令，确认一键式下线NAT服务的回显为“处理结果=处理成功”。

### 6 执行命令，确认POD已下线。

#### 6.1 **X86场景：**

#### 6.2 **ARM场景：**

#### 回显为“查询Pod不存在”。

### 7 执行**SET FWSOFTPARA**命令，关闭Service Fabric的**DWORD\_521**软参，即系统故障时触发容灾导致的联动复位。

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


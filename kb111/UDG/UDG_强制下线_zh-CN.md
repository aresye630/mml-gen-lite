---
id: ''
name: 强制下线
ne_type: UDG
type: feature
description: 上线可选VNFC失败和加载补丁失败时，需要强制下线可选VNFC并清理相关残留数据，请务必在研发人员指导下参考本章节进行操作。
risk_level: ''
doc_source: ["网络部署","软件安装","基于VNF LCM安装UDG（非SDN）","参考及FAQ","强制下线"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
上线可选VNFC失败和加载补丁失败时，需要强制下线可选VNFC并清理相关残留数据，请务必在研发人员指导下参考本章节进行操作。

## 必备事项
前提条件

前提条件

* 可选VNFC功能上线失败。
* 已通过U2020/MAE或UDG OM portal登录华为操作维护系统。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
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
          data_source: ''
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
          data_source: ''
          pattern: ''
          default: Normal
        FUNCTIONSETNAME:
          name: '网络功能集名称'
          type: string
          minLength: 0
          maxLength: 1024
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    opr_featuredisable_list:
    - PODTYPE: 'IPsecexec-c4-pod/IPsecctl-pod'
      DISABLETYPE: Force
      FUNCTIONSETNAME: 'IPsec'
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 登录UDG OM Portal。

### 2 执行命令**DSP PODINFO**，查询当前已上线的可选VNFC的Pod。

### 3 执行命令，强制下线可选VNFC，此处以IPsec为例。

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

### 参数DISABLETYPE的取值必须为Force，即强制下线。

### 参数PODTYPE的取值为实际已上线的可选VNFC的Pod。

### 4 请务必联系研发人员，在指导下进行相关残留数据的清理。


---
id: ''
name: 配置基于TA的网络选择切片
ne_type: UNC
type: feature
description: 本操作指导介绍在运行网络中配置支持基于TA选择切片的操作过程。  当现网完成切片部署后，切片TAIs变更或切片部署改变时，NSSF会根据可用性配置信息选择本地配置或者AMF上报的切片可用性信息（切片部署的AMF SET、TAIs以及TAIs支持的切片）为UE完成切片选择业务。  适用于AMF、NSSF。
risk_level: ''
doc_source: ["网络部署","业务专题","5G Core NSSF解决方案","NSSF功能部署","NSSF非容灾组网","NSSF配置","配置NSSF可选功能","配置基于TA的网络选择切片"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本操作指导介绍在运行网络中配置支持基于TA选择切片的操作过程。当现网完成切片部署后，切片TAIs变更或切片部署改变时，NSSF会根据可用性配置信息选择本地配置或者AMF上报的切片可用性信息（切片部署的AMF SET、TAIs以及TAIs支持的切片）为UE完成切片选择业务。适用于AMF、NSSF。

## 必备事项
前提条件

* 请仔细阅读切片可用性信息上报流程。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    set_nssffuncpara_list:
      type: items
      properties:
        DATASOURCETYPE:
          name: '数据源设置'
          type: string
          enum:
          - LocalConfigData
          - ReportData
          required: false
          description: '配置NSSF在所有业务流程中使用的数据源。'
          data_source: '本端规划'
          pattern: ''
          default: ''
  examples:
    set_nssffuncpara_list:
    - DATASOURCETYPE: LocalConfigData
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 进入“MML命令行-UNC”窗口。

### 2 配置NSSF在业务流程中所使用的数据源。

```jinja2
{%- for item in set_nssffuncpara_list -%}
    SET NSSFFUNCPARA:
    {#- --- 可选参数 --- -#}
    {%- if item.DATASOURCETYPE is not none -%}
        DATASOURCETYPE={{item.DATASOURCETYPE}},
    {%- endif -%}
    ;
{%- endfor -%}
```


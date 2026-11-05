---
id: ''
name: 卸载VPROBE服务
ne_type: UNC
type: feature
description: 当运营商不需要VPROBE服务或VPROBE服务动态上线失败时，可以单独卸载VPROBE pod，从而下线VPROBE服务。
risk_level: ''
doc_source: ["网络部署","软件安装","基于NFVO安装UNC（非SDN）","卸载UNC","卸载VPROBE服务"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
当运营商不需要VPROBE服务或VPROBE服务动态上线失败时，可以单独卸载VPROBE pod，从而下线VPROBE服务。

## 必备事项
前提条件

* 已经完成网络设计，已规划下线VPROBE pod的类型和数量。
* 如果动态下线失败，只能继续重新触发动态下线任务。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    rmv_vprobeip_list:
      type: items
      properties:
        INDEX:
          name: '索引号'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    rmv_vprobesvrip_list:
      type: items
      properties:
        ACCESSNAME:
          name: '接入点名称'
          type: string
          minLength: 0
          maxLength: 32
          required: true
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
          data_source: '固定取值'
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
  examples:
    rmv_vprobeip_list:
    - INDEX: 3
    rmv_vprobesvrip_list:
    - ACCESSNAME: 'ACCESS1'
    opr_featuredisable_list:
    - PODTYPE: 'All Pod'
      DISABLETYPE: Normal
      FUNCTIONSETNAME: 'VPROBE'
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 登录UNC OM Portal。

### 2 执行命令**RMV VPROBEIP**和**RMV VPROBESVRIP**，删除配置数据。

### 避免由于残留配置数据的导致再次上线本服务失败。

```jinja2
{%- for item in rmv_vprobeip_list -%}
    RMV VPROBEIP:
    {#- --- 必选参数 --- -#}
    INDEX={{item.INDEX}},
    ;
{%- endfor -%}
```

```jinja2
{%- for item in rmv_vprobesvrip_list -%}
    RMV VPROBESVRIP:
    {#- --- 必选参数 --- -#}
    ACCESSNAME="{{item.ACCESSNAME}}",
    ;
{%- endfor -%}
```

### 3 执行命令，动态下线VPROBE pod。

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

### 4 执行命令，确认已经成功下线VPROBE pod。

### 回显为“处理结果=处理成功”。

### 回显“查询Pod不存在”。

### 5 执行命令，确认已经下线VPROBE服务。

### 回显为中没有VPROBE服务。


---
id: ''
name: 卸载SAPO服务
ne_type: UDG
type: feature
description: 当运营商不需要SAPO服务或SAPO服务动态上线失败时，可以单独卸载SAPO的pod，从而下线SAPO服务。
risk_level: ''
doc_source: ["网络部署","软件安装","基于VNF LCM安装UDG（非SDN）","卸载UDG","卸载SAPO服务"]
refs: []
metadata:
  DepOnLiveCfg: true
allowed-tools:
- getParameterValue('LST AIFUNCPARA')
---
<!-- @mml:block=annotations -->
```text
## 操作场景
当运营商不需要SAPO服务或SAPO服务动态上线失败时，可以单独卸载SAPO的pod，从而下线SAPO服务。

## 必备事项
前提条件

已经完成网络设计，已规划下线SAPO的pod类型和数量。
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
          description: 'pod类型，用/分割。不要带空格。'
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
    set_aifuncpara_list:
      type: items
      properties:
        SAAIENABLER:
          name: 'SA Intelligence功能开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    opr_featuredisable_list:
    - PODTYPE: 'aipo-pod/aipoctrl-pod'
      DISABLETYPE: Normal
      FUNCTIONSETNAME: 'AIPO'
    set_aifuncpara_list:
    - SAAIENABLER: DISABLE
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 登录UDG OM Portal。

### 2 执行命令，动态下线SAPO的pod。

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

### 在异构场景下，由于SAPO服务的X86虚拟机和ARM虚拟机不会同时存在，SAPO服务对应的POD只有aipoctrl-pod和aipo-pod。

### 3 执行命令，确认已经成功下线SAPO的pod。

### 回显为“处理结果=处理成功”。

### 回显为“查询Pod不存在”。

### 4 如果无法通过人工导入方式维护SA性能优化库，则建议关闭Intelligence加速功能。

### 执行命令查询Intelligence加速是否开启。

### 当查询结果为“SA AI 功能开关  =  不使能（关闭）”时，无需进行关闭，直接进行步骤5。

### 当查询结果为“SA AI 功能开关  =  使能（开启）”时，需要执行命令关闭Intelligence加速。

```jinja2
{%- set LST_AIFUNCPARA=getParameterValue('LST AIFUNCPARA') -%}
{%- if LST_AIFUNCPARA=='使能（开启）' -%}
    {%- for item in set_aifuncpara_list -%}
        SET AIFUNCPARA:
        {#- --- 可选参数 --- -#}
        {%- if item.SAAIENABLER is not none -%}
            SAAIENABLER={{item.SAAIENABLER}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 5 若动态下线SAPO服务后，不再上线SAPO服务，则需要缩容SAPO自身VM（PBU\_AI），释放VM资源。

### 若后续还需要上线SAPO服务，则不必缩容SAPO自身VM。

### **缩容VM**：请参见《UDG中心侧扩缩容指导书(基于LCM)》或《UDG中心侧扩缩容指导书(基于NFVO)》


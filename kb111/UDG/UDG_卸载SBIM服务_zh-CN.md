---
id: ''
name: 卸载SBIM服务
ne_type: UDG
type: feature
description: 当运营商不需要SBIM服务或SBIM服务动态上线失败时，可以单独卸载SBIM pod，从而下线SBIM服务。
risk_level: ''
doc_source: ["网络部署","软件安装","基于NFVO安装UDG（SDN）","卸载UDG","卸载SBIM服务"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
当运营商不需要SBIM服务或SBIM服务动态上线失败时，可以单独卸载SBIM pod，从而下线SBIM服务。

## 必备事项
前提条件

已经完成网络设计，已规划下线SBIM pod的类型和数量。
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
    opr_featuredisable_list:
    - PODTYPE: 'httpctrl-pod/sbim-pod'
      DISABLETYPE: Normal
      FUNCTIONSETNAME: 'SBIM'
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 登录UDG OM Portal。

### 2 执行命令，动态下线SBIM pod。

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

### 3 执行命令，确认已经成功下线SBIM pod。

### 回显为“处理结果=处理成功”。

### 回显“查询Pod不存在”。

### 4 若动态下线SBIM服务后，不再上线SBIM服务，则需要缩容SBIM自身VM（X86为：PBU\_P-S；ARM为：PBU\_P-S\_ARM），释放VM资源。

### 若后续还需要上线SBIM服务，则不必缩容SBIM自身VM。

### **缩容VM**：请参见《UDG中心侧扩缩容指导书(基于LCM)》或《UDG中心侧扩缩容指导书(基于NFVO)》。


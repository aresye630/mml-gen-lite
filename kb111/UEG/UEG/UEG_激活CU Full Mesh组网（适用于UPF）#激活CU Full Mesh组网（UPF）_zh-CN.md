---
id: GWFD-021701
name: 激活CU Full Mesh组网（UPF）
ne_type: UEG
type: feature
description: 运营商考虑可靠性，规划SMF和UPF采用Full Mesh组网时，可激活本特性。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝S","MEC 特性指南（风筝S）","UEG特性指南","分布式网络功能","GWFD-021701 CU Full Mesh组网","SMF&UPF容灾方案","新建部署","激活CU Full Mesh组网（适用于UPF）","激活CU Full Mesh组网（UPF）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
运营商考虑可靠性，规划SMF和UPF采用Full Mesh组网时，可激活本特性。

## 必备事项
前提条件

* 请仔细阅读SMF&UPF容灾方案。
* UEG本端已完成数据面逻辑接口（Sa/Sc/Pa）和N4逻辑接口的配置。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    set_licenseswitch_list:
      type: items
      properties:
        LICITEM:
          name: 'License项'
          type: string
          minLength: 0
          maxLength: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SWITCH:
          name: '开关'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_cpteidualloc_list:
      type: items
      properties:
        SWITCH:
          name: 'UP分配开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: true
          description: '在Full Mesh组网下，该参数必须配置为DISABLE。'
          data_source: '本端规划'
          pattern: ''
          default: ''
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV3G5CUFM01'
      SWITCH: ENABLE
    set_cpteidualloc_list:
    - SWITCH: DISABLE
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 打开本特性的License配置开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

### 2 配置用户面支持分配F-TEID。

```jinja2
{%- for item in set_cpteidualloc_list -%}
    SET CPTEIDUALLOC:
    {#- --- 必选参数 --- -#}
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```


---
id: ''
name: 激活网络拥塞的实时检测
ne_type: UNC
type: feature
description: 当运营商需要了解无线侧网络拥塞情况，配合UPF及NWDAF进行拥塞网络优化时，需要开启本特性。  适用于MME、SGW-C、PGW-C、AMF、SMF。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","位置业务管理","WSFD-205013 网络拥塞的实时检测","激活网络拥塞的实时检测"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
当运营商需要了解无线侧网络拥塞情况，配合UPF及NWDAF进行拥塞网络优化时，需要开启本特性。适用于MME、SGW-C、PGW-C、AMF、SMF。

## 必备事项
前提条件

请仔细阅读WSFD-205013 网络拥塞的实时检测。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    set_smfunc_list:
      type: items
      properties:
        MMULI:
          name: '移动性管理流程ULI上报开关'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: '该参数用于控制UNC在移动性管理流程中发送的Create Session Request/Modify Bearer Request消息是否携带ULI信元。'
          data_source: '本端规划'
          pattern: ''
          default: ''
  examples:
    set_smfunc_list:
    - MMULI: ON
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 进入“MML命令行-UNC”窗口。

### 2 开启移动性管理流程ULI上报开关。

```jinja2
{%- for item in set_smfunc_list -%}
    SET SMFUNC:
    {#- --- 可选参数 --- -#}
    {%- if item.MMULI is not none -%}
        MMULI={{item.MMULI}},
    {%- endif -%}
    ;
{%- endfor -%}
```


---
id: GWFD-010296
name: 激活NB-IoT终端标准接入
ne_type: UDG
type: feature
description: 本操作指导介绍在4G网络UDG上开启NB-IoT终端标准接入功能。  适用于SGW-U、PGW-U。
risk_level: ''
doc_source: ["特性部署","特性指南","UDG特性指南","物联网功能","NB-IoT","GWFD-010296 NB-IoT终端标准接入","激活NB-IoT终端标准接入"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本操作指导介绍在4G网络UDG上开启NB-IoT终端标准接入功能。适用于SGW-U、PGW-U。

## 必备事项
前提条件

请仔细阅读GWFD-010296 NB-IoT终端标准接入。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    set_iotcapability_list:
      type: items
      properties:
        NBIOT:
          name: 'NB-IoT接入能力上报'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '使能NB-IoT终端标准接入功能。'
          data_source: '本端规划'
          pattern: ''
          default: ''
  examples:
    set_iotcapability_list:
    - NBIOT: ENABLE
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 设置NB-IoT终端标准接入功能。

### 完整的NB-IoT功能需要用户面、控制面共同配置完成，控制面配置请参考SGW-C、PGW-C上NB-IoT相关章节。

#### 1.1 //开启NB-IoT接入功能开关。

```jinja2
{%- for item in set_iotcapability_list -%}
    SET IOTCAPABILITY:
    {#- --- 可选参数 --- -#}
    {%- if item.NBIOT is not none -%}
        NBIOT={{item.NBIOT}},
    {%- endif -%}
    ;
{%- endfor -%}
```


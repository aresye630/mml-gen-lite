---
id: GWFD-026101
name: 激活NB-IoT终端标准接入
ne_type: UEG
type: feature
description: 本操作指导介绍在4G网络UEG上开启NB-IoT终端标准接入功能。  适用于SGW-U、PGW-U。
tags: []
risk_level: ''
doc_source: ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（一号通专网通用场景，入驻式）","相关参考","NB-IoT","GWFD-026101 NB-IoT终端标准接入","激活NB-IoT终端标准接入"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
本操作指导介绍在4G网络UEG上开启NB-IoT终端标准接入功能。适用于SGW-U、PGW-U。

## 必备事项
前提条件

请仔细阅读GWFD-026101 NB-IoT终端标准接入。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
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
<!-- @mml:block= commands -->

### 1 设置NB-IoT终端标准接入功能。

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

### 完整的NB-IoT功能需要用户面、控制面共同配置完成，控制面配置请参考SGW-C、PGW-C上NB-IoT相关章节。


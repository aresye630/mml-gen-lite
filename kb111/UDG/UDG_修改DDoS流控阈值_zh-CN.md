---
id: GWFD-010253
name: 修改DDoS流控阈值
ne_type: UDG
type: feature
description: 网络调整需要修改DDoS流控阈值。  适用于SGW-U、PGW-U、UPF。
risk_level: ''
doc_source: ["特性部署","特性指南","UDG特性指南","安全管理功能","GWFD-010253 防DDoS功能","调整DDoS Check数据","修改DDoS流控阈值"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
网络调整需要修改DDoS流控阈值。适用于SGW-U、PGW-U、UPF。

## 必备事项
前提条件

请仔细阅读GWFD-010253 防DDoS功能。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    set_ddos_list:
      type: items
      properties:
        THRESHOLD:
          name: 'DDos防护阈值'
          type: integer
          minimum: 1
          maximum: 10000
          required: true
          description: '每个用户每秒允许转发的TCP建链请求包的个数'
          data_source: '本端规划'
          pattern: ''
          default: ''
  examples:
    set_ddos_list:
    - THRESHOLD: 150
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 修改DDoS流控阈值。

#### 1.1 //修改DDoS流控阈值。

```jinja2
{%- for item in set_ddos_list -%}
    SET DDOS:
    {#- --- 必选参数 --- -#}
    THRESHOLD={{item.THRESHOLD}},
    ;
{%- endfor -%}
```


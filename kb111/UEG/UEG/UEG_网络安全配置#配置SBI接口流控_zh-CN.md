---
id: ''
name: 配置SBI接口流控
ne_type: UEG
type: feature
description: 通过配置SBI接口流控功能保护UEG。
tags: []
risk_level: ''
doc_source:
  - ["网络部署","园区入驻式（仅连接）","5GC toB 部署边缘站点（站点为“风筝M”，入驻式）","配置安全数据（风筝M）","安全配置（虚机容器）","安全配置建议","可选配置","网络安全配置","配置SBI接口流控"]
  - ["网络部署","园区入驻式（仅连接）","5GC toB 部署边缘站点（站点为“风筝M”，入驻式）","配置安全数据（风筝M）","安全配置（裸机容器）","安全配置建议","可选配置","网络安全配置","配置SBI接口流控"]
  - ["网络部署","园区入驻式（仅连接）","5GC toB 部署边缘站点（站点为“风筝L”，入驻式）","配置安全数据（风筝L）","安全配置（虚机容器）","安全配置建议","可选配置","网络安全配置","配置SBI接口流控"]
  - ["网络部署","园区入驻式（仅连接）","5GC toB 部署边缘站点（站点为“风筝L”，入驻式）","配置安全数据（风筝L）","安全配置（裸机容器）","安全配置建议","可选配置","网络安全配置","配置SBI接口流控"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
通过配置SBI接口流控功能保护UEG。

## 必备事项
前提条件

请仔细阅读防攻击。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    set_sbitcppara_list:
      type: items
      properties:
        SYNPKTFCTHD:
          name: 'SYN包流控阈值(pps)'
          type: integer
          minimum: 1000
          maximum: 50000
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        PEERIPCONNLIMIT:
          name: '单个对端IP连接限制数'
          type: integer
          minimum:
          - 0
          - 64
          maximum:
          - 0
          - 1024
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
  examples:
    set_sbitcppara_list:
    - SYNPKTFCTHD: 20000
      PEERIPCONNLIMIT: 500
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 （可选）使能SBI接口TCP SYN包流控和连接限制

### 在“MML命令行-UEG”窗口执行命令

```jinja2
{%- if is_optional_sbi_tcp_syn_flow_control -%}
    {%- for item in set_sbitcppara_list -%}
        SET SBITCPPARA:
        {#- --- 可选参数 --- -#}
        {%- if item.SYNPKTFCTHD is not none -%}
            SYNPKTFCTHD={{item.SYNPKTFCTHD}},
        {%- endif -%}
        {%- if item.PEERIPCONNLIMIT is not none -%}
            PEERIPCONNLIMIT={{item.PEERIPCONNLIMIT}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```


---
id: GWFD-110281
name: 修改IPFarm的心跳检测参数
ne_type: UDG
type: feature
description: 修改心跳检测成功与失败转换的次数以及心跳检测的间隔。  适用于PGW-U、UPF。
risk_level: ''
doc_source: ["特性部署","特性指南","UDG特性指南","智能策略控制功能","GWFD-110281 用户Portal","调整用户Portal参数","修改IPFarm的心跳检测参数"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
修改心跳检测成功与失败转换的次数以及心跳检测的间隔。适用于PGW-U、UPF。

## 必备事项
前提条件

前提条件

* 请仔细阅读GWFD-110281 用户Portal。
* 完成配置用户Portal。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    set_ipfarmglobal_list:
      type: items
      properties:
        SERVERTYPE:
          name: '服务器类型'
          type: string
          enum:
          - IPMS
          - PCSCF
          - REDIRECT
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        TIMETHRESHOLD:
          name: '时间阈值（秒）'
          type: integer
          minimum: 6
          maximum: 60
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        HEALTHSUCCLIMIT:
          name: '健康检查成功次数'
          type: integer
          minimum: 1
          maximum: 10
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        HEALTHFAILLIMIT:
          name: '健康检查失败次数'
          type: integer
          minimum: 1
          maximum: 10
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        LBMETHOD:
          name: '负载均衡模式'
          type: string
          enum:
          - INVAILD
          - LEAST_LOAD
          - LEAST_RECENTLY_USED
          - ROUND_ROBIN
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TIMEOUT:
          name: 'Ping探测超时时长（秒）'
          type: integer
          minimum: 1
          maximum: 59
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    set_ipfarmglobal_list:
    - SERVERTYPE: REDIRECT
      TIMETHRESHOLD: 6
      HEALTHSUCCLIMIT: 3
      HEALTHFAILLIMIT: 2
      LBMETHOD: ''
      TIMEOUT: ''
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 配置整机的IPFarm心跳检测功能的相关参数。

```jinja2
{%- for item in set_ipfarmglobal_list -%}
    SET IPFARMGLOBAL:
    {#- --- 必选参数 --- -#}
    SERVERTYPE={{item.SERVERTYPE}},
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：SERVERTYPE=REDIRECT/IPMS/PCSCF 时可选 --- -#}
    {%- if item.SERVERTYPE in ['REDIRECT', 'IPMS', 'PCSCF'] -%}
        {%- if item.TIMETHRESHOLD is not none -%}
            TIMETHRESHOLD={{item.TIMETHRESHOLD}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SERVERTYPE=REDIRECT/IPMS/PCSCF 时可选 --- -#}
    {%- if item.SERVERTYPE in ['REDIRECT', 'IPMS', 'PCSCF'] -%}
        {%- if item.HEALTHSUCCLIMIT is not none -%}
            HEALTHSUCCLIMIT={{item.HEALTHSUCCLIMIT}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SERVERTYPE=REDIRECT/IPMS/PCSCF 时可选 --- -#}
    {%- if item.SERVERTYPE in ['REDIRECT', 'IPMS', 'PCSCF'] -%}
        {%- if item.HEALTHFAILLIMIT is not none -%}
            HEALTHFAILLIMIT={{item.HEALTHFAILLIMIT}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SERVERTYPE=REDIRECT 时可选 --- -#}
    {%- if item.SERVERTYPE == 'REDIRECT' -%}
        {%- if item.LBMETHOD is not none -%}
            LBMETHOD={{item.LBMETHOD}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SERVERTYPE=REDIRECT/IPMS/PCSCF 时可选 --- -#}
    {%- if item.SERVERTYPE in ['REDIRECT', 'IPMS', 'PCSCF'] -%}
        {%- if item.TIMEOUT is not none -%}
            TIMEOUT={{item.TIMEOUT}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```


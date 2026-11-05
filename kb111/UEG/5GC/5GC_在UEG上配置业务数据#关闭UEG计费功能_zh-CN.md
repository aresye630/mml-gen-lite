---
id: ''
name: 关闭UEG计费功能
ne_type: UEG
type: feature
description: 风筝L模式下，不支持计费功能，需要在UEG的SMF上关闭计费功能开关。若已在UEG初始配置 > 配置SMF服务化接口数据（N10/N11/N7）中执行关闭计费功能开关，则无需执行本任务。
tags: []
risk_level: ''
doc_source: ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（一号通专网通用场景，入驻式）","配置基础业务","在UEG上配置业务数据","关闭UEG计费功能"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
风筝L模式下，不支持计费功能，需要在UEG的SMF上关闭计费功能开关。若已在UEG初始配置 > 配置SMF服务化接口数据（N10/N11/N7）中执行关闭计费功能开关，则无需执行本任务。

## 必备事项
前提条件

具备管理员权限的操作人员已经登录华为操作维护系统（登录U2020/MAE客户端或登录OM Portal）。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    set_chargectrl_list:
      type: items
      properties:
        HOMEONLINE:
          name: '归属地在线用户计费控制'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '风筝L模式下不进行计费，需要关闭计费开关。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        HOMECONVERGED:
          name: '归属地融合用户计费控制'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        HOMEOFFLINE:
          name: '归属地离线用户计费控制'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VISITONLINE:
          name: '拜访地在线用户计费控制'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VISITCONVERGED:
          name: '拜访地融合用户计费控制'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VISITOFFLINE:
          name: '拜访地离线用户计费控制'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ROAMONLINE:
          name: '漫游在线用户计费控制'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ROAMCONVERGED:
          name: '漫游融合用户计费控制'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ROAMOFFLINE:
          name: '漫游离线用户计费控制'
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
    set_chargectrl_list:
    - HOMEONLINE: DISABLE
      HOMECONVERGED: DISABLE
      HOMEOFFLINE: DISABLE
      VISITONLINE: DISABLE
      VISITCONVERGED: DISABLE
      VISITOFFLINE: DISABLE
      ROAMONLINE: DISABLE
      ROAMCONVERGED: DISABLE
      ROAMOFFLINE: DISABLE
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 **关闭计费功能**

### 园区风筝方案不进行计费，需要关闭计费功能。

#### 1.1 关闭计费功能。

```jinja2
{%- for item in set_chargectrl_list -%}
    SET CHARGECTRL:
    {#- --- 可选参数 --- -#}
    {%- if item.HOMEONLINE is not none -%}
        HOMEONLINE={{item.HOMEONLINE}},
    {%- endif -%}
    {%- if item.HOMECONVERGED is not none -%}
        HOMECONVERGED={{item.HOMECONVERGED}},
    {%- endif -%}
    {%- if item.HOMEOFFLINE is not none -%}
        HOMEOFFLINE={{item.HOMEOFFLINE}},
    {%- endif -%}
    {%- if item.VISITONLINE is not none -%}
        VISITONLINE={{item.VISITONLINE}},
    {%- endif -%}
    {%- if item.VISITCONVERGED is not none -%}
        VISITCONVERGED={{item.VISITCONVERGED}},
    {%- endif -%}
    {%- if item.ROAMONLINE is not none -%}
        ROAMONLINE={{item.ROAMONLINE}},
    {%- endif -%}
    {%- if item.ROAMOFFLINE is not none -%}
        ROAMOFFLINE={{item.ROAMOFFLINE}},
    {%- endif -%}
    {%- if item.ROAMCONVERGED is not none -%}
        ROAMCONVERGED={{item.ROAMCONVERGED}},
    {%- endif -%}
    {%- if item.VISITOFFLINE is not none -%}
        VISITOFFLINE={{item.VISITOFFLINE}},
    {%- endif -%}
    ;
{%- endfor -%}
```


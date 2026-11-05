---
id: ''
name: 开启5G LAN用户本地签约功能开关
ne_type: UEG
type: feature
description: 部署本地运维5G LAN用户签约的5G LAN组ID时，运营商需要在SMF（UEG-L）上开启5G LAN本地签约功能开关。  关闭5G LAN本地签约功能开关时，无法本地调整用户所属的5G LAN组ID。
tags: []
risk_level: ''
doc_source: ["原子能力&行业场景","原子能力","5GC toB 原子能力-5G LAN","特性指南","UEG特性指南","可选功能","本地调整5G LAN组ID","5G LAN用户本地签约配置（风筝L，通过WebPortal或MML调整）","开启5G LAN用户本地签约功能开关"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
部署本地运维5G LAN用户签约的5G LAN组ID时，运营商需要在SMF（UEG-L）上开启5G LAN本地签约功能开关。关闭5G LAN本地签约功能开关时，无法本地调整用户所属的5G LAN组ID。

## 必备事项
前提条件

操作员拥有配置权限。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    set_edgesmcommfunc_list:
      type: items
      properties:
        LOCVNSUBSW:
          name: '5G LAN本地签约功能开关'
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
    set_edgesmcommfunc_list:
    - LOCVNSUBSW: ENABLE
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 登录OM Portal。

### 2 进入“MML命令行-UEG”窗口。

### 3 执行**SET EDGESMCOMMFUNC**命令，开启5G LAN用户本地签约功能。

```jinja2
{%- for item in set_edgesmcommfunc_list -%}
    SET EDGESMCOMMFUNC:
    {#- --- 可选参数 --- -#}
    {%- if item.LOCVNSUBSW is not none -%}
        LOCVNSUBSW={{item.LOCVNSUBSW}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 调整5G LAN用户本地签约的5G LAN组ID后，运营商可通过**LST RDSSTATICIPPARA**查询多个用户本地签约的5G LAN组ID。


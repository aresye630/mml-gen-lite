---
id: GWFD-110281
name: 修改Captive模式时间的间隔
ne_type: UDG
type: feature
description: captive模式时间的间隔需要修改。  适用于PGW-U、UPF。
risk_level: ''
doc_source: ["特性部署","特性指南","UDG特性指南","智能策略控制功能","GWFD-110281 用户Portal","调整用户Portal参数","修改Captive模式时间的间隔"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
captive模式时间的间隔需要修改。适用于PGW-U、UPF。

## 必备事项
前提条件

该操作无需具备特殊条件。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    mod_userprofile_list:
      type: items
      properties:
        USERPROFILENAME:
          name: '用户模板名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '用户模板名称，已通过**ADD USERPROFILE**配置完成，可以通过**LST USERPROFILE**命令查询。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        CAPMODETHRES:
          name: 'Captive模式时间阈值（分）'
          type: integer
          minimum: 0
          maximum: 60
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
  examples:
    mod_userprofile_list:
    - USERPROFILENAME: 'up_test'
      CAPMODETHRES: 5
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 配置Captive模式时间阈值。

#### 1.1 //配置Captive模式时间阈值。

```jinja2
{%- for item in mod_userprofile_list -%}
    MOD USERPROFILE:
    {#- --- 必选参数 --- -#}
    USERPROFILENAME="{{item.USERPROFILENAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.CAPMODETHRES is not none -%}
        CAPMODETHRES={{item.CAPMODETHRES}},
    {%- endif -%}
    ;
{%- endfor -%}
```


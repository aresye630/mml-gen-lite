---
id: ''
name: 配置USCDB管理弱口令
ne_type: UEG
type: feature
description: 在用户创建或修改口令时，为了防止口令过于简单而被盗窃和破解，系统会对其进行检查，如果当前设置的口令与某条被设置的弱口令信息相匹配，则不允许用户设置该弱口令。  弱口令是禁止使用的口令，它通常包括：系统默认的口令、简单数字组合、和用户名相同的口令、长度很短的口令等。  弱口令检查只影响新设置的账号口令，不影响已经存在的账号口令。例如：先设置一个账号口令，再将该口令设置为弱口令，此时不会影响已经设置的账号口令的使用。
tags: []
risk_level: ''
doc_source: ["网络部署","园区入驻式（仅连接）","5GC toB 部署边缘站点（站点为“风筝L”，入驻式）","配置安全数据（风筝L）","安全配置（虚机容器）","安全配置建议","可选配置","运维安全配置","配置USCDB管理弱口令"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
在用户创建或修改口令时，为了防止口令过于简单而被盗窃和破解，系统会对其进行检查，如果当前设置的口令与某条被设置的弱口令信息相匹配，则不允许用户设置该弱口令。弱口令是禁止使用的口令，它通常包括：系统默认的口令、简单数字组合、和用户名相同的口令、长度很短的口令等。弱口令检查只影响新设置的账号口令，不影响已经存在的账号口令。例如：先设置一个账号口令，再将该口令设置为弱口令，此时不会影响已经设置的账号口令的使用。

## 必备事项
前提条件

已登录OM Portal。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    add_weakpwd_list:
      type: items
      properties:
        PWD:
          name: '弱口令'
          type: string
          maxLength: 128
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    add_weakpwd_list:
    - PWD: '规划的弱口令信息'
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 使用admin账号登录“USCDB MML命令”界面。

### 2 执行**ADD WEAKPWD**命令新增弱口令信息。

```jinja2
{%- for item in add_weakpwd_list -%}
    ADD WEAKPWD:
    {#- --- 必选参数 --- -#}
    PWD="{{item.PWD}}",
    ;
{%- endfor -%}
```

### 3 执行**LST WEAKPWD**命令查询已添加的弱口令信息是否符合预期。


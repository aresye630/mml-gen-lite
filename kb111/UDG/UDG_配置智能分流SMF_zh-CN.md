---
id: ''
name: 配置智能分流SMF
ne_type: UDG
type: feature
description: 该任务旨在指导操作人员在智能分流SMF上配置单用户多园区开关参数。当现网需要支持单用户多园区业务时，参考此页面内容配置。
risk_level: ''
doc_source: ["特性部署","业务专题","5G Core 一跳入家解决方案","一跳入家解决方案（基于非3GPP接入方案）","业务初始部署与调测","部署一跳入家","配置智能分流SMF"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
该任务旨在指导操作人员在智能分流SMF上配置单用户多园区开关参数。当现网需要支持单用户多园区业务时，参考此页面内容配置。

## 必备事项
前提条件

已完成一跳入家要求的移动VPN相关配置。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    set_multidnnctrl_list:
      type: items
      properties:
        MULSESSIONSW:
          name: '是否支持创建多个专网会话'
          type: string
          required: false
          description: '支持单用户多园区时，需要设置此开关参数为“ENABLE”。'
          data_source: '本端规划'
          pattern: ''
          default: ''
  examples:
    set_multidnnctrl_list:
    - MULSESSIONSW: ENABLE
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 配置智能分流SMF支持单用户多园区。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_multidnnctrl_list的变量区（command: SET MULTIDNNCTRL） -#}
<!-- MISSING_MACRO: command=SET MULTIDNNCTRL list_name=set_multidnnctrl_list step_id=1 -->
```


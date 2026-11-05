---
id: ''
name: 配置归属地专网UPF
ne_type: UNC
type: feature
description: 通用DNN漫游分流场景中，可选园区内专网UPF分流。如果专网UPF已经开启了动态分流功能，无需重复配置。
risk_level: ''
doc_source: ["网络部署","业务专题","5G Core 一跳入家解决方案","一跳入家解决方案（基于3GPP接入方案）","业务初始部署与调测","部署移动VPN","配置专用DNN数据","配置用户在园区内专网UPF分流（可选）","开启园区内专网分流","配置归属地专网UPF"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
通用DNN漫游分流场景中，可选园区内专网UPF分流。如果专网UPF已经开启了动态分流功能，无需重复配置。

## 必备事项
前提条件

已参考运营商配置规范完成网元的基本配置。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    set_dedicatedlbo_list:
      type: items
      properties:
        ULCLSWITCH:
          name: '专网UPF动态分流功能开关'
          type: string
          required: false
          description: '该参数用于指定系统是否开启专网UPF动态分流功能。'
          data_source: '本端规划'
          pattern: ''
          default: ''
  examples:
    set_dedicatedlbo_list:
    - ULCLSWITCH: ENABLE
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 打开用户在园区内由专网UPF动态分流的功能开关。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_dedicatedlbo_list的变量区（command: SET DEDICATEDLBO） -#}
<!-- MISSING_MACRO: command=SET DEDICATEDLBO list_name=set_dedicatedlbo_list step_id=1 -->
```


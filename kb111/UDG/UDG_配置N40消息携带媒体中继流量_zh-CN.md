---
id: ''
name: 配置N40消息携带媒体中继流量
ne_type: UDG
type: feature
description: 在N40计费场景下，当运营商需要核对话单流量时，请参考本章节进行配置。
risk_level: ''
doc_source: ["特性部署","业务专题","5G Core 媒体中继解决方案","媒体中继业务配置","新建媒体中继基础配置","配置SMF","配置N40消息携带媒体中继流量"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
在N40计费场景下，当运营商需要核对话单流量时，请参考本章节进行配置。

## 必备事项
前提条件

* 请提前了解话单流量核对方案。
* SMF已升级到20.16.2及后续版本。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    set_n40msgctrl_list:
      type: items
      properties:
        RELAYREPORTSW:
          name: 'N40消息支持携带媒体中继流量开关'
          type: string
          required: false
          description: '配置在N40消息中携带媒体中继上下行流量。'
          data_source: '全网规划'
          pattern: ''
          default: ''
  examples:
    set_n40msgctrl_list:
    - RELAYREPORTSW: ENABLE
```

## 3 命令模板定义
<!-- @mml:block=commands -->

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_n40msgctrl_list的变量区（command: SET N40MSGCTRL） -#}
<!-- MISSING_MACRO: command=SET N40MSGCTRL list_name=set_n40msgctrl_list step_id=1 -->
```


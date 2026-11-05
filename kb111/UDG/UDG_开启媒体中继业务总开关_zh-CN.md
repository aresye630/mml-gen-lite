---
id: ''
name: 开启媒体中继业务总开关
ne_type: UDG
type: feature
description: 在完成上述配置后，需要参考本章节在媒体中继UPF上开启媒体中继业务总开关。开启此开关后，媒体中继UPF会对配置进行校验，如果配置存在缺失会上报**ALM-81203 媒体中继配置不完整**告警。
risk_level: ''
doc_source: ["特性部署","业务专题","5G Core 媒体中继解决方案","媒体中继业务配置","新建媒体中继基础配置","配置UPF","开启媒体中继业务总开关"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
在完成上述配置后，需要参考本章节在媒体中继UPF上开启媒体中继业务总开关。开启此开关后，媒体中继UPF会对配置进行校验，如果配置存在缺失会上报**ALM-81203 媒体中继配置不完整**告警。

## 必备事项
前提条件

已完成媒体中继业务增加媒体中继全局配置~增加媒体服务商配置（基于OTT应用）的相关配置。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    set_relayfunc_list:
      type: items
      properties:
        RELAYSW:
          name: '媒体中继功能开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: true
          description: '此开关为全局开关。'
          data_source: '固定取值'
          pattern: ''
          default: ''
  examples:
    set_relayfunc_list:
    - RELAYSW: ENABLE
```

## 3 命令模板定义
<!-- @mml:block=commands -->

```jinja2
{%- for item in set_relayfunc_list -%}
    SET RELAYFUNC:
    {#- --- 必选参数 --- -#}
    RELAYSW={{item.RELAYSW}},
    ;
{%- endfor -%}
```


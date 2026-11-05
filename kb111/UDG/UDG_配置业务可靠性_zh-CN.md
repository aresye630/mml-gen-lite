---
id: ''
name: 配置业务可靠性
ne_type: UDG
type: feature
description: 传统UPF容灾时，主倒备，然后主恢复，SMF会通知备UPF去活所有IKE会话，但在异常场景下，家庭侧仍然与备UPF保持连接，或家庭侧新接入的IKE会话仍然接到备UPF上，这会导致UE侧会话和家庭侧会话不在同一个UPF上，业务不通。此时只能通过UPF定时核查去活家庭会话，业务恢复不及时。  该任务旨在解决此问题，在备UPF上开启智家APN主备状态动态管理功能，确保主UPF恢复场景下，备UPF通过N4接口的信令交互感知到主UPF恢复，然后主动把当前备UPF上的IKE会话踢下线后触发IKE重新激活到主UPF上，达到业务自动及时恢复的目的。
risk_level: ''
doc_source: ["特性部署","业务专题","5G Core 一跳入家解决方案","一跳入家解决方案（基于非3GPP接入方案）","业务初始部署与调测","部署一跳入家","配置一跳入家专网UPF","配置业务可靠性"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
传统UPF容灾时，主倒备，然后主恢复，SMF会通知备UPF去活所有IKE会话，但在异常场景下，家庭侧仍然与备UPF保持连接，或家庭侧新接入的IKE会话仍然接到备UPF上，这会导致UE侧会话和家庭侧会话不在同一个UPF上，业务不通。此时只能通过UPF定时核查去活家庭会话，业务恢复不及时。该任务旨在解决此问题，在备UPF上开启智家APN主备状态动态管理功能，确保主UPF恢复场景下，备UPF通过N4接口的信令交互感知到主UPF恢复，然后主动把当前备UPF上的IKE会话踢下线后触发IKE重新激活到主UPF上，达到业务自动及时恢复的目的。

## 必备事项
前提条件

无
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    set_upnon3gpppara_list:
      type: items
      properties:
        AGINGTIME:
          name: 'ToH SESSION的老化时长'
          type: integer
          minimum:
          - 0
          - 1440
          maximum:
          - 0
          - 10080
          required: false
          description: '* 用于配置ToH SESSION的老化时长。配置为0时，表示不开启老化。 * 主UPF不配置老化时长，备UPF配置老化时长为1440分钟。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        FASTRECOVERYSW:
          name: '智家业务快速恢复开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '* 用于配置一跳入家主备UPF部署场景下，主UPF恢复后，备UPF上启动家庭侧会话快速核查的处理。 * 只需在备UPF上开启此功能。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_apndynstatesw_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SWITCH:
          name: '开关标识'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: true
          description: '* 用于配置主备状态动态管理功能。 * 只需在备UPF上开启此功能。'
          data_source: '本端规划'
          pattern: ''
          default: ''
  examples:
    set_upnon3gpppara_list:
    - AGINGTIME: 1440
      FASTRECOVERYSW: ENABLE
    set_apndynstatesw_list:
    - APN: 'home.area1.dnn'
      SWITCH: ENABLE
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 备UPF开启家庭侧会话快速核查功能。

```jinja2
{%- for item in set_upnon3gpppara_list -%}
    SET UPNON3GPPPARA:
    {#- --- 可选参数 --- -#}
    {%- if item.AGINGTIME is not none -%}
        AGINGTIME={{item.AGINGTIME}},
    {%- endif -%}
    {%- if item.FASTRECOVERYSW is not none -%}
        FASTRECOVERYSW={{item.FASTRECOVERYSW}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 2 备UPF开启智家APN主备状态动态管理功能。

```jinja2
{%- for item in set_apndynstatesw_list -%}
    SET APNDYNSTATESW:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```


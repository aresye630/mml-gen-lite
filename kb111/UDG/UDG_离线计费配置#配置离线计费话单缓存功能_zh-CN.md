---
id: ''
name: 配置离线计费话单缓存功能
ne_type: UDG
type: feature
description: 本指导描述离线计费话单缓存功能的相关配置过程。  开启离线计费后，当CG发生故障或者UNC与CG之间链路异常导致无法发送话单时，为避免造成计费损失，UNC支持将话单消息暂时缓存在本地。待CG状态恢复正常后，再将缓存的话单重新发送到CG。  当UNC本地有缓存话单文件时，会上报**ALM-81025 话单缓存**告警；当本地不再有缓存话单文件时，告警恢复。当缓存话单文件长期未处理，缓存时长超过配置的超时时长则会上报**ALM-81059 超期缓存话单**告警，提示维护人员处理缓存话单，以免造成计费损失；当本地没有已配置话单版本的超期缓存话单文件时，告警恢复。
risk_level: ''
doc_source: ["特性部署","业务专题","5G Core 计费解决方案","计费解决方案概述","计费方案部署与调测","方案五：部署NCG且融合接口计费组网方案（N40接口+传统Ga/Gy接口）","SMF配置","离线计费配置","配置离线计费话单缓存功能"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本指导描述离线计费话单缓存功能的相关配置过程。开启离线计费后，当CG发生故障或者UNC与CG之间链路异常导致无法发送话单时，为避免造成计费损失，UNC支持将话单消息暂时缓存在本地。待CG状态恢复正常后，再将缓存的话单重新发送到CG。当UNC本地有缓存话单文件时，会上报**ALM-81025 话单缓存**告警；当本地不再有缓存话单文件时，告警恢复。当缓存话单文件长期未处理，缓存时长超过配置的超时时长则会上报**ALM-81059 超期缓存话单**告警，提示维护人员处理缓存话单，以免造成计费损失；当本地没有已配置话单版本的超期缓存话单文件时，告警恢复。

## 必备事项
前提条件

请仔细阅读Ga/Gy接口离线/在线计费。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    set_cdrstoragectrl_list:
      type: items
      properties:
        CDREXPIREDAY:
          name: '话单缓存超期天数'
          type: string
          required: false
          description: '配置缓存话单文件的超期时间。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        CDREXPIREWEEK:
          name: '话单缓存超期周数'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_ofccdrpara_list:
      type: items
      properties:
        STGENCRYPT:
          name: '话单缓存加密开关'
          type: string
          required: false
          description: '配置是否对离线计费缓存话单进行加密。此处以不对离线计费缓存话单加密举例，请根据业务需要配置。'
          data_source: '本端规划'
          pattern: ''
          default: ''
  examples:
    set_cdrstoragectrl_list:
    - CDREXPIREDAY: '3'
      CDREXPIREWEEK: '3'
    set_ofccdrpara_list:
    - STGENCRYPT: DISABLE
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 配置缓存话单文件的超期时间。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_cdrstoragectrl_list的变量区（command: SET CDRSTORAGECTRL） -#}
<!-- MISSING_MACRO: command=SET CDRSTORAGECTRL list_name=set_cdrstoragectrl_list step_id=1 -->
```

### 2 配置是否对离线计费缓存话单进行加密。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_ofccdrpara_list的变量区（command: SET OFCCDRPARA） -#}
<!-- MISSING_MACRO: command=SET OFCCDRPARA list_name=set_ofccdrpara_list step_id=2 -->
```


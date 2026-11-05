---
id: ''
name: 配置NSSF数据
ne_type: UEG
type: feature
description: 同一区域内，不是所有AMF都支持5G LAN业务切片时，需配置NSSF数据。  初始AMF收到5G LAN业务报文后，如本AMF未配置5G LAN业务切片信息，则可通过与NSSF交互实现AMF重定向，即将5G LAN业务报文重定向到配置了5G LAN业务切片信息的AMF上。
tags: []
risk_level: ''
doc_source: ["原子能力&行业场景","原子能力","5GC toB 原子能力-5G LAN","网络部署","运营商","配置5GC网元","配置NSSF数据"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
同一区域内，不是所有AMF都支持5G LAN业务切片时，需配置NSSF数据。初始AMF收到5G LAN业务报文后，如本AMF未配置5G LAN业务切片信息，则可通过与NSSF交互实现AMF重定向，即将5G LAN业务报文重定向到配置了5G LAN业务切片信息的AMF上。

## 必备事项
前提条件

无。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    add_cfgsnssai_list:
      type: items
      properties:
        INDEX:
          name: '索引'
          type: string
          required: false
          description: '存在多条记录时，该参数不能重复。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        MCC:
          name: '移动国家码'
          type: string
          required: false
          description: 'MCC和MNC。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        MNC:
          name: '移动网号'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        SST:
          name: '切片服务类型'
          type: string
          required: false
          description: '5G LAN业务的切片信息。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        SD:
          name: '切片细分标识'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        ISACTIVE:
          name: '激活状态'
          type: string
          required: false
          description: '采用样例值。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        DESC:
          name: '描述'
          type: string
          required: false
          description: '该参数为可选参数，在运维中起助记作用。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_tacgroupinnssf_list:
      type: items
      properties:
        INDEX:
          name: '索引'
          type: string
          required: false
          description: '存在多条记录时，该参数不能重复。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        TACGROUPNAME:
          name: '跟踪区域码分组名称'
          type: string
          required: false
          description: '该参数用于标识跟踪区域码分组名称。  推荐采用SST-SD格式命名。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        TACSTART:
          name: 'TAC起始字符'
          type: string
          required: false
          description: '跟踪区域码范围。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        TACEND:
          name: 'TAC结束字符'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_amfsetid_list:
      type: items
      properties:
        INDEX:
          name: '索引'
          type: string
          required: false
          description: '存在多条记录时，该参数不能重复。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SST:
          name: '切片服务类型'
          type: string
          required: false
          description: '5G LAN业务的切片信息、MCC和MNC。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        SD:
          name: '切片细分标识'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MCC:
          name: '移动国家码'
          type: string
          required: false
          description: 'MCC和MNC。'
          data_source: ''
          pattern: ''
          default: ''
        MNC:
          name: '移动网号'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        REGIONID:
          name: '区域ID'
          type: string
          required: false
          description: 'AMF区域ID。'
          data_source: ''
          pattern: ''
          default: ''
        AMFSETID:
          name: 'AMF集合标识'
          type: string
          required: false
          description: 'AMF集合标识。'
          data_source: ''
          pattern: ''
          default: ''
        TACGROUPNAME:
          name: '跟踪区域码分组名称'
          type: string
          required: false
          description: '采用**ADD TACGROUPINNSSF**命令中定义的“TACGROUPNAME”参数值。'
          data_source: ''
          pattern: ''
          default: ''
  examples:
    add_cfgsnssai_list:
    - INDEX: '1'
      MCC: '123'
      MNC: '03'
      SST: '1'
      SD: '010101'
      ISACTIVE: TRUE
      DESC: 5G_LAN
    add_tacgroupinnssf_list:
    - INDEX: '1'
      TACGROUPNAME: 1-010101
      TACSTART: '290100'
      TACEND: '290110'
    add_amfsetid_list:
    - INDEX: '1'
      SST: '1'
      SD: '010101'
      MCC: '123'
      MNC: '03'
      REGIONID: 08
      AMFSETID: 088
      TACGROUPNAME: 1-010101
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 在NSSF上增加5G LAN业务切片信息。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_cfgsnssai_list的变量区（command: ADD CFGSNSSAI） -#}
<!-- MISSING_MACRO: command=ADD CFGSNSSAI list_name=add_cfgsnssai_list step_id=1 -->
```

### 2 在跟踪区域码分组中增加跟踪区域码。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_tacgroupinnssf_list的变量区（command: ADD TACGROUPINNSSF） -#}
<!-- MISSING_MACRO: command=ADD TACGROUPINNSSF list_name=add_tacgroupinnssf_list step_id=2 -->
```

### 3 将切片、AMF、TAC组进行绑定。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_amfsetid_list的变量区（command: ADD AMFSETID） -#}
<!-- MISSING_MACRO: command=ADD AMFSETID list_name=add_amfsetid_list step_id=3 -->
```


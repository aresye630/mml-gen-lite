---
id: ''
name: 配置切片业务数据（NSSF）
ne_type: UEG
type: feature
description: 本场景用于在NSSF上配置切片相关的业务数据。
tags: []
risk_level: ''
doc_source:
  - ["专网（仅连接，园区入驻式）","业务发放","5GC toB 网络切片发放（专网，入驻式）","通过CN NSSMF发放","切片发放操作","普通创建（复用NSSI）","制作切片业务脚本","配置切片业务数据（风筝S）","配置切片业务数据（NSSF）"]
  - ["专线（仅连接，地市共享式）","业务发放","5GC toB 网络切片发放（专线，共享式）","通过CN NSSMF发放","切片发放操作","普通创建（复用NSSI）","制作切片业务脚本","配置切片业务数据（风筝S）","配置切片业务数据（NSSF）"]
  - ["云网（连接+计算，入驻式或共享式）","业务发放","5GC toB 网络切片发放（云网，带计算）","通过CN NSSMF发放","切片发放操作","普通创建（复用NSSI）","制作切片业务脚本","配置切片业务数据（风筝S）","配置切片业务数据（NSSF）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
本场景用于在NSSF上配置切片相关的业务数据。

## 必备事项
前提条件

无。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    add_tacgroupinnssf_list:
      type: items
      properties:
        INDEX:
          name: '索引'
          type: string
          required: false
          description: '配置NSSF包含的AMF的TAC分组。仅当新部署的AMF切片所在TAC分组与已有TAC分组不同时需要配置。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        TACGROUPNAME:
          name: '跟踪区域码分组名称'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        TACSTART:
          name: 'TAC起始字符'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        TACEND:
          name: 'TAC结束字符'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_candidateamf_list:
      type: items
      properties:
        INDEX:
          name: '索引'
          type: string
          required: false
          description: '配置候选AMF。仅当新配置的AMF集合与已有的AMF集合不同时需要配置。   * 参数“AMFINSTANCEID”通过**LST NFUUID**查询。 * 参数“REGIONID”和参数“AMFSETID”由**LST GUAMI**查询。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        AMFINSTANCEID:
          name: 'AMF实例标识'
          type: string
          required: false
          description: ''
          data_source: '已有配置中获取'
          pattern: ''
          default: ''
        MCC:
          name: '移动国家码'
          type: string
          required: false
          description: ''
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
        REGIONID:
          name: '区域ID'
          type: string
          required: false
          description: ''
          data_source: '已有配置中获取'
          pattern: ''
          default: ''
        AMFSETID:
          name: 'AMF集合标识'
          type: string
          required: false
          description: ''
          data_source: '已有配置中获取'
          pattern: ''
          default: ''
    add_cfgsnssai_list:
      type: items
      properties:
        INDEX:
          name: '索引'
          type: string
          required: false
          description: '配置NSSF支持的切片。   * 参数“SST”在**ADD PLMNS**的参数“SST”中定义，此处引用。 * 参数“SD”在**ADD PLMNS**的参数“SD”中定义，此处引用。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        MCC:
          name: '移动国家码'
          type: string
          required: false
          description: ''
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
          description: ''
          data_source: '已有配置中获取'
          pattern: ''
          default: ''
        SD:
          name: '切片细分标识'
          type: string
          required: false
          description: ''
          data_source: '已有配置中获取'
          pattern: ''
          default: ''
        ISACTIVE:
          name: '激活状态'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_amfsetid_list:
      type: items
      properties:
        INDEX:
          name: '索引'
          type: string
          required: false
          description: '配置切片与AMF集间的关系。   * 参数“SST”在**ADD PLMNS**的参数“SST”中定义，此处引用。 * 参数“SD”在**ADD PLMNS**的参数“SD”中定义，此处引用。  * 参数“REGIONID”在**ADD CANDIDATEAMF**的参数“REGIONID”中定义，此处引用。 * 参数“AMFSETID”在**ADD CANDIDATEAMF**的参数“AMFSETID”中定义，此处引用。 * 参数“TACGROUPNAME”在**ADD TACGROUPINNSSF**的参数“TACGROUPNAME”中定义，此处引用。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SST:
          name: '切片服务类型'
          type: string
          required: false
          description: ''
          data_source: '已有配置中获取'
          pattern: ''
          default: ''
        SD:
          name: '切片细分标识'
          type: string
          required: false
          description: ''
          data_source: '已有配置中获取'
          pattern: ''
          default: ''
        MCC:
          name: '移动国家码'
          type: string
          required: false
          description: ''
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
        REGIONID:
          name: '区域ID'
          type: string
          required: false
          description: ''
          data_source: '已有配置中获取'
          pattern: ''
          default: ''
        AMFSETID:
          name: 'AMF集合标识'
          type: string
          required: false
          description: ''
          data_source: '已有配置中获取'
          pattern: ''
          default: ''
        TACGROUPNAME:
          name: '跟踪区域码分组名称'
          type: string
          required: false
          description: ''
          data_source: '已有配置中获取'
          pattern: ''
          default: ''
  examples:
    add_tacgroupinnssf_list:
    - INDEX: '0'
      TACGROUPNAME: TACGROUP0
      TACSTART: 00138d
      TACEND: 00138d
    add_candidateamf_list:
    - INDEX: '0'
      AMFINSTANCEID: a671e53f-115f-4969-be66-f89fb301d718
      MCC: '460'
      MNC: '02'
      REGIONID: '00'
      AMFSETID: '001'
    add_cfgsnssai_list:
    - INDEX: '0'
      MCC: '460'
      MNC: '02'
      SST: '1'
      SD: '131313'
      ISACTIVE: FALSE
    add_amfsetid_list:
    - INDEX: '0'
      SST: '1'
      SD: '131313'
      MCC: '460'
      MNC: '02'
      REGIONID: '00'
      AMFSETID: '001'
      TACGROUPNAME: TACGROUP0
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 （可选）配置区域分组。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_tacgroupinnssf_list的变量区（command: ADD TACGROUPINNSSF） -#}
<!-- MISSING_MACRO: command=ADD TACGROUPINNSSF list_name=add_tacgroupinnssf_list step_id=1 -->
```

### 2 （可选）配置候选AMF。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_candidateamf_list的变量区（command: ADD CANDIDATEAMF） -#}
<!-- MISSING_MACRO: command=ADD CANDIDATEAMF list_name=add_candidateamf_list step_id=2 -->
```

### 3 配置NSSF支持的切片信息。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_cfgsnssai_list的变量区（command: ADD CFGSNSSAI） -#}
<!-- MISSING_MACRO: command=ADD CFGSNSSAI list_name=add_cfgsnssai_list step_id=3 -->
```

### 4 配置AMF集与切片的关系。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_amfsetid_list的变量区（command: ADD AMFSETID） -#}
<!-- MISSING_MACRO: command=ADD AMFSETID list_name=add_amfsetid_list step_id=4 -->
```


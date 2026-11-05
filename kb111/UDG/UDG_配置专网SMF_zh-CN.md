---
id: ''
name: 配置专网SMF
ne_type: UDG
type: feature
description: 该任务旨在指导操作人员完成专网SMF一跳入家解决方案的配置。
risk_level: ''
doc_source: ["特性部署","业务专题","5G Core 一跳入家解决方案","一跳入家解决方案（基于非3GPP接入方案）","业务初始部署与调测","部署一跳入家","配置专网SMF"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
该任务旨在指导操作人员完成专网SMF一跳入家解决方案的配置。

## 必备事项
前提条件

前提条件

* 已完成一跳入家依赖功能的License加载。
* 已经完成与专网UPF的基础对接配置。
* 已完成一跳入家要求的移动VPN相关配置。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    mod_upnode_list:
      type: items
      properties:
        NFINSTANCENAME:
          name: 'UPF实例名称'
          type: string
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        TOHPSASW:
          name: '是否支持作为智家随行场景To Home会话主锚点'
          type: string
          required: false
          description: '主UPF需要配置此开关参数为“ENABLE”。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    set_apnupselply_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          required: false
          description: '开通一跳入家业务的Home DNN。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        PRIORITYFLAG:
          name: '基于优先级优选UPF开关'
          type: string
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
    mod_pnfdnn_list:
      type: items
      properties:
        INDEX:
          name: '索引'
          type: string
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PRISWITCH:
          name: '优先级功能开关'
          type: string
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PRIORITY:
          name: '优先级'
          type: string
          required: false
          description: '值越小优先级越高。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_apnuprecover_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          required: false
          description: '开通一跳入家业务的Home DNN。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        MASTERUPFID:
          name: '主UPF实例名称'
          type: string
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        HANDLINGMODE:
          name: 'UP链路故障恢复处理模式'
          type: string
          required: false
          description: '设置为“BACKMIGRATION”，SMF检测到主UPF故障恢复后将Home DNN下的会话从备UPF回迁到主UPF。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        BACKUPFID:
          name: '备UPF实例名称'
          type: string
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_apntohctrl_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          required: false
          description: '开通一跳入家业务的Home DNN。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        TOHSW:
          name: '智家随行会话开关'
          type: string
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_smffunc_list:
      type: items
      properties:
        VNGROUPDATASW:
          name: '5G LAN会话是否向UDM查询VnGroupData'
          type: string
          required: false
          description: '当“智家随行会话开关”配置为“ENABLE”时，此开关参数必须设置为“Support”。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_pfcppvtext_list:
      type: items
      properties:
        FEATURE:
          name: '特性名称'
          type: string
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SWITCH:
          name: '私有信元携带开关'
          type: string
          required: false
          description: '当“UP链路故障恢复处理模式”配置为“BACKMIGRATION”时，此开关参数必须设置为“ENABLE”。'
          data_source: '本端规划'
          pattern: ''
          default: ''
  examples:
    mod_upnode_list:
    - NFINSTANCENAME: upf_instance_1
      TOHPSASW: ENABLE
    set_apnupselply_list:
    - APN: home.area1.dnn
      PRIORITYFLAG: ENABLE;//设置Home DNN下支持基于优先级选择UPF。
    mod_pnfdnn_list:
    - INDEX: '1'
      PRISWITCH: SPECIFIC
      PRIORITY: 1;//设置upf_instance_1为主UPF。“PRIORITY”参数取值越小，优先级越高。
    add_apnuprecover_list:
    - APN: home.area1.dnn
      MASTERUPFID: upf_instance_1
      HANDLINGMODE: BACKMIGRATION
      BACKUPFID: upf_instance_2
    add_apntohctrl_list:
    - APN: home.area1.dnn
      TOHSW: ENABLE
    set_smffunc_list:
    - VNGROUPDATASW: Support
    set_pfcppvtext_list:
    - FEATURE: Session_Delete_Cause
      SWITCH: ENABLE;//配置PFCP Session Deletion Request消息中携带Session级私有信元Session Delete Cause（指示删除备UPF的会话）。
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 在SMF上使能专网UPF的一跳入家功能：设置upf\_instance\_1和upf\_instance\_2“是否支持作为智家随行场景To Home会话主锚点”参数为“使能”。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该mod_upnode_list的变量区（command: MOD UPNODE） -#}
<!-- MISSING_MACRO: command=MOD UPNODE list_name=mod_upnode_list step_id=1 -->
```

### 2 配置SMF进行UPF选择时，优先选择主UPF：设置upf\_instance\_1和upf\_instance\_2“优先级功能开关”参数为“指定”，且upf\_instance\_1的“优先级”取值比upf\_instance\_2的小。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_apnupselply_list的变量区（command: SET APNUPSELPLY） -#}
<!-- MISSING_MACRO: command=SET APNUPSELPLY list_name=set_apnupselply_list step_id=2 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该mod_pnfdnn_list的变量区（command: MOD PNFDNN） -#}
<!-- MISSING_MACRO: command=MOD PNFDNN list_name=mod_pnfdnn_list step_id=2 -->
```

### 3 配置主UPF故障恢复后，SMF回迁业务会话至主UPF。**注意此处的主备UPF务必和2中定义的主备UPF保持一致，否则会导致无法回迁。**

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_apnuprecover_list的变量区（command: ADD APNUPRECOVER） -#}
<!-- MISSING_MACRO: command=ADD APNUPRECOVER list_name=add_apnuprecover_list step_id=3 -->
```

### 4 打开SMF上的一跳入家功能开关。注意“APN”值已经在**ADD APN**中配置。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_apntohctrl_list的变量区（command: ADD APNTOHCTRL） -#}
<!-- MISSING_MACRO: command=ADD APNTOHCTRL list_name=add_apntohctrl_list step_id=4 -->
```

### 5 设置SMF向UDM查询家庭组ID对应的VnGroupData。用户会话建立时，当UDM返回的签约数据中包括家庭组ID和SharedDataID，SMF会基于SharedDataID向UDM发送一次查询消息来再次确认该家庭组ID对应的VnGroupData，以确保家庭组ID的准确性。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_smffunc_list的变量区（command: SET SMFFUNC） -#}
<!-- MISSING_MACRO: command=SET SMFFUNC list_name=set_smffunc_list step_id=5 -->
```

### 6 打开SMF上一跳入家相关的私有信元开关。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_pfcppvtext_list的变量区（command: SET PFCPPVTEXT） -#}
<!-- MISSING_MACRO: command=SET PFCPPVTEXT list_name=set_pfcppvtext_list step_id=6 -->
```


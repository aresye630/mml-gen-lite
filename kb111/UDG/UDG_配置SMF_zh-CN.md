---
id: ''
name: 配置SMF
ne_type: UDG
type: feature
description: 本操作用于指导在专网SMF上开启通用DNN漫游分流特性。
risk_level: ''
doc_source: ["特性部署","业务专题","5G Core 一跳入家解决方案","一跳入家解决方案（基于3GPP接入方案）","业务初始部署与调测","部署移动VPN","配置专用DNN数据","配置通用DNN漫游分流","配置SMF"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本操作用于指导在专网SMF上开启通用DNN漫游分流特性。

## 必备事项
前提条件

已参考运营商配置规范完成网元的基本配置。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    set_smffunc_list:
      type: items
      properties:
        N16AUEIPSW:
          name: '通用DNN会话UE IP地址处理开关'
          type: string
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
    set_smfsoftparaofbit_list:
      type: items
      properties:
        DT:
          name: '数据类型'
          type: string
          required: false
          description: '软参DWORD1039 BIT21用于控制5G用户接入时是否将左侧携带的selectedDNN作为用户请求DNN使用。取值为1时，将selectedDNN作为用户请求DNN使用。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        DWORDNUM:
          name: 'Dword索引'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        VALUE:
          name: '软参记录值'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        POSITION:
          name: '比特位'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    mod_upnode_list:
      type: items
      properties:
        NFINSTANCENAME:
          name: 'UPF实例标识'
          type: string
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        UEIPNATFUNC:
          name: '是否支持UE IP地址NAT转换功能'
          type: string
          required: false
          description: '专网SMF会基于此参数的配置判定专网UPF是否支持NAT转换功能（对UE IP地址1：1替换），并基于该能力选择专网UPF。'
          data_source: '全网规划'
          pattern: ''
          default: ''
  examples:
    set_smffunc_list:
    - N16AUEIPSW: Support
    set_smfsoftparaofbit_list:
    - DT: Dw
      DWORDNUM: '1039'
      VALUE: VALUE_1
      POSITION: '21'
    mod_upnode_list:
    - NFINSTANCENAME: 5EA7F228-47CC-2032-03A3-0E1313000001
      UEIPNATFUNC: ENABLE
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 打开“公网会话UE IP地址处理开关。当N16a口携带了公网会话的UE IP地址（扩展私有字段），专网SMF会将公网会话的UE IP地址下发给专网会话的锚点UPF，指示专网UPF做UE IP地址NAT转换。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_smffunc_list的变量区（command: SET SMFFUNC） -#}
<!-- MISSING_MACRO: command=SET SMFFUNC list_name=set_smffunc_list step_id=1 -->
```

### 2 配置左侧AMF或I-SMF携带的selectedDNN作为用户请求DNN使用。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_smfsoftparaofbit_list的变量区（command: SET SMFSOFTPARAOFBIT） -#}
<!-- MISSING_MACRO: command=SET SMFSOFTPARAOFBIT list_name=set_smfsoftparaofbit_list step_id=2 -->
```

### 3 配置UPF支持UE IP地址NAT转换功能。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该mod_upnode_list的变量区（command: MOD UPNODE） -#}
<!-- MISSING_MACRO: command=MOD UPNODE list_name=mod_upnode_list step_id=3 -->
```


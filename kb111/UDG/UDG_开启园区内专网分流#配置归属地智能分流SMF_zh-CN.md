---
id: ''
name: 配置归属地智能分流SMF
ne_type: UDG
type: feature
description: 本操作用于指导当智能分流SMF与专网UPF未建立连接时，配置智能分流SMF对接专网UPF。当专网UPF已在智能分流SMF上配置时，无需进行此操作。
risk_level: ''
doc_source: ["特性部署","业务专题","5G Core 一跳入家解决方案","一跳入家解决方案（基于3GPP接入方案）","业务初始部署与调测","部署移动VPN","配置专用DNN数据","配置用户在园区内专网UPF分流（可选）","开启园区内专网分流","配置归属地智能分流SMF"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本操作用于指导当智能分流SMF与专网UPF未建立连接时，配置智能分流SMF对接专网UPF。当专网UPF已在智能分流SMF上配置时，无需进行此操作。

## 必备事项
前提条件

无。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    add_pnfprofile_list:
      type: items
      properties:
        NFINSTANCEID:
          name: 'NF实例标识'
          type: string
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        NFTYPE:
          name: 'NF类型'
          type: string
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        NFSTATUS:
          name: 'NF状态'
          type: string
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        FQDN:
          name: '域名'
          type: string
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPADDRESSTYPE:
          name: 'IP地址类型'
          type: string
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV4ADDRESS1:
          name: 'IPV4地址1'
          type: string
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        PORT:
          name: '端口号'
          type: string
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_pnfns_list:
      type: items
      properties:
        INDEX:
          name: '索引'
          type: string
          required: false
          description: '配置用户面支持的服务切片信息。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        NFINSTANCEID:
          name: 'NF实例标识'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        SST:
          name: '切片/服务类型'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        SD:
          name: '切片分类器'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_pnfdnn_list:
      type: items
      properties:
        INDEX:
          name: '索引'
          type: string
          required: false
          description: '配置用户面节点支持的DNN及其归属切片的信息。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        NFINSTANCEID:
          name: 'NF实例标识'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        DNN:
          name: '数据网络名称'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        PNFNSINDEX:
          name: '对端NF的切片索引'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_upnode_list:
      type: items
      properties:
        NFINSTANCENAME:
          name: 'UP唯一标识'
          type: string
          required: false
          description: '已通过命令ADD PNFPROFILE配置。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        LOCATION:
          name: 'UP位置特性'
          type: string
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        UPFUNCTION:
          name: 'UP支持功能'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        LOCK:
          name: 'LOCK'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VPNNAME:
          name: 'Vpn名称'
          type: string
          required: false
          description: 'UPF的“**VPNNAME**”与**LST CPPOINT**中的查询结果一致。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        PDUESTWITHOUTN9:
          name: 'PDUESTWITHOUTN9'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_pnfupfinfo_list:
      type: items
      properties:
        NFINSTANCEID:
          name: 'NF实例标识'
          type: string
          required: false
          description: '配置用户面节点与EPS的互通以及支持的PDU会话类型。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        IWKEPSIND:
          name: 'IWKEPSIND'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PDUSESSIONTYPE:
          name: 'PDU会话类型'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_upfpfcppara_list:
      type: items
      properties:
        UPFINSTANCEID:
          name: 'UPF实例标识'
          type: string
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        DACTINTERVAL:
          name: 'DACTINTERVAL'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MIGINTERVAL:
          name: '迁移间隔(秒)'
          type: string
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_upcscanrate_list:
      type: items
      properties:
        SCANTYPE:
          name: '扫描任务类型'
          type: string
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        RATE:
          name: '扫描速率(个/秒)'
          type: string
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
  examples:
    add_pnfprofile_list:
    - NFINSTANCEID: 5EA7F228-47CC-2032-03A3-0E1313000001
      NFTYPE: NfUPF
      NFSTATUS: Registered
      FQDN: upf01.node.mnc003.mcc123.3gppnetwork.org
      IPADDRESSTYPE: IPTypeV4
      IPV4ADDRESS1: 192.168.126.11
      PORT: '8080'
    add_pnfns_list:
    - INDEX: '3'
      NFINSTANCEID: 5EA7F228-47CC-2032-03A3-0E1313000001
      SST: '1'
      SD: '000000'
    add_pnfdnn_list:
    - INDEX: '3'
      NFINSTANCEID: 5EA7F228-47CC-2032-03A3-0E1313000001
      DNN: stjwt.gd
      PNFNSINDEX: '3'
    add_upnode_list:
    - NFINSTANCENAME: 5EA7F228-47CC-2032-03A3-0E1313000001
      LOCATION: Central
      UPFUNCTION: None
      LOCK: FALSE
      VPNNAME: VRF_CP
      PDUESTWITHOUTN9: ENABLE
    add_pnfupfinfo_list:
    - NFINSTANCEID: 5EA7F228-47CC-2032-03A3-0E1313000001
      IWKEPSIND: TRUE
      PDUSESSIONTYPE: IPV4-1&IPV6-1&IPV4V6-1
    add_upfpfcppara_list:
    - UPFINSTANCEID: 5EA7F228-47CC-2032-03A3-0E1313000001
      DACTINTERVAL: '100'
      MIGINTERVAL: '60'
    set_upcscanrate_list:
    - SCANTYPE: MIGRATE
      RATE: '6'
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 配置Profile实例。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_pnfprofile_list的变量区（command: ADD PNFPROFILE） -#}
<!-- MISSING_MACRO: command=ADD PNFPROFILE list_name=add_pnfprofile_list step_id=1 -->
```

### 2 配置用户面节点支持的切片与DNN信息。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_pnfns_list的变量区（command: ADD PNFNS） -#}
<!-- MISSING_MACRO: command=ADD PNFNS list_name=add_pnfns_list step_id=2 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_pnfdnn_list的变量区（command: ADD PNFDNN） -#}
<!-- MISSING_MACRO: command=ADD PNFDNN list_name=add_pnfdnn_list step_id=2 -->
```

### 3 配置用户面节点的位置特征和分流能力。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_upnode_list的变量区（command: ADD UPNODE） -#}
<!-- MISSING_MACRO: command=ADD UPNODE list_name=add_upnode_list step_id=3 -->
```

### 4 配置用户面支持的PDU会话类型。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_pnfupfinfo_list的变量区（command: ADD PNFUPFINFO） -#}
<!-- MISSING_MACRO: command=ADD PNFUPFINFO list_name=add_pnfupfinfo_list step_id=4 -->
```

### 5 配置UPF的迁移间隔为60s，控制用户面迁移任务的扫描速率为6个/秒。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_upfpfcppara_list的变量区（command: ADD UPFPFCPPARA） -#}
<!-- MISSING_MACRO: command=ADD UPFPFCPPARA list_name=add_upfpfcppara_list step_id=5 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_upcscanrate_list的变量区（command: SET UPCSCANRATE） -#}
<!-- MISSING_MACRO: command=SET UPCSCANRATE list_name=set_upcscanrate_list step_id=5 -->
```


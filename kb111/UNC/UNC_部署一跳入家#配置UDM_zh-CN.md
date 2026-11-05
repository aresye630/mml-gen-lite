---
id: ''
name: 配置UDM
ne_type: UNC
type: feature
description: 该任务旨在指导操作人员给用户配置一跳入家签约数据。  完成了一跳入家基础的业务部署，网络就具备了为用户开通一跳入家的能力。当用户有开通业务诉求时，可以通过如下方式完成数据签约和业务开通。  * 家庭成员和家庭CPE在运营商BOSS系统进行签约。签约完成后BOSS系统通过运维接口下发签约信息到UDM上 。 * 如果BOSS系统和UDM之间的运维接口尚未支持，请参考本章节在UDM上人工配置签约数据。
risk_level: ''
doc_source: ["网络部署","业务专题","5G Core 一跳入家解决方案","一跳入家解决方案（基于3GPP接入方案）","业务初始部署与调测","部署一跳入家","配置UDM"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
该任务旨在指导操作人员给用户配置一跳入家签约数据。完成了一跳入家基础的业务部署，网络就具备了为用户开通一跳入家的能力。当用户有开通业务诉求时，可以通过如下方式完成数据签约和业务开通。* 家庭成员和家庭CPE在运营商BOSS系统进行签约。签约完成后BOSS系统通过运维接口下发签约信息到UDM上 。* 如果BOSS系统和UDM之间的运维接口尚未支持，请参考本章节在UDM上人工配置签约数据。

## 必备事项
前提条件

* 操作人员具有PGW Web LMT的操作权限。
* 已完成**5G LAN签约用户数**和**一跳入家3GPP接入签约用户数**的License加载。
* 一跳入家家庭CPE的IMSI号码已开户。用户A和用户B已分别完成5G开户。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    add_ngcqostpl_list:
      type: items
      properties:
        HLRSN:
          name: 'HLR序列号'
          type: string
          required: false
          description: '用于标识一个HLR序列号。该参数必须先由**ADD HLRSN**命令定义，然后才能在此处引用。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        TPLID:
          name: '模板ID'
          type: string
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        TPLNAME:
          name: '模板名'
          type: string
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        NGQI:
          name: '5QI'
          type: string
          required: false
          description: 'QoS参数（5QI、ARP等）仅用于举例，实际请根据具体业务模型规划。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        ARPPRILEVEL:
          name: 'ARP优先级'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        PREEMPTIONCAP:
          name: 'PREEMPTIONCAP'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PREEMPTIONVUL:
          name: 'PREEMPTIONVUL'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NGQIPRILEVEL:
          name: 'NGQIPRILEVEL'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_dnnqostpl_list:
      type: items
      properties:
        HLRSN:
          name: 'HLR序列号'
          type: string
          required: false
          description: '该参数必须先由**ADD HLRSN**命令定义。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        TPLID:
          name: '模板ID'
          type: string
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        TPLNAME:
          name: '模板名'
          type: string
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PDUTYPE:
          name: '默认PDU类型'
          type: string
          required: false
          description: '用于标识允许的PDU类型。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SSCMODE:
          name: '默认SSC模式'
          type: string
          required: false
          description: '配置默认会话和业务连续性模式。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        NGCQOSTPLID:
          name: '5GC QoS模板ID'
          type: string
          required: false
          description: '该参数必须先由**ADD NGCQOSTPL**命令定义。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        AMBRUP:
          name: 'DNN级别上行速率'
          type: string
          required: false
          description: '配置上下行速率，仅用于举例，实际请根据具体业务模型规划。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        UPUNIT:
          name: 'DNN级别上行速率单位'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        AMBRDW:
          name: 'DNN级别下行速率'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        DWUNIT:
          name: 'DNN级别下行速率单位'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        CHARGE:
          name: '计费特性'
          type: string
          required: false
          description: '配置计费属性值，仅用于举例，按需规划。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_snssai_list:
      type: items
      properties:
        IMSI:
          name: 'IMSI'
          type: string
          required: false
          description: '用于标识待签约一跳入家业务的终端和CPE的IMSI号码。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SNSSAI:
          name: '切片标识'
          type: string
          required: false
          description: '5G系统中的网络切片。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        DEFAULT:
          name: '是否默认S-NSSAI'
          type: string
          required: false
          description: '签约的S-NSSAI数据是否为默认S-NSSAI数据。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_smdata_list:
      type: items
      properties:
        IMSI:
          name: 'IMSI'
          type: string
          required: false
          description: '用于标识待签约一跳入家业务的终端和CPE的IMSI号码。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SNSSAI:
          name: '切片标识'
          type: string
          required: false
          description: '该参数必须由**ADD SNSSAI**命令定义。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        DNN:
          name: '数据网名称'
          type: string
          required: false
          description: '开通一跳入家业务的Home DNN。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        DEFAULT:
          name: '是否默认DNN'
          type: string
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        DNNQOSTPLID:
          name: '5GS DNNQoS模板ID'
          type: string
          required: false
          description: '该参数必须由**ADD DNNQOSTPL**命令定义。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        MOBILE_HOME:
          name: '一跳入家'
          type: string
          required: false
          description: '标识给用户签约一跳入家DNN扩展属性，该参数只需给CPE签约，无需给UE签约。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_vngroup_list:
      type: items
      properties:
        HLRSN:
          name: 'HLR序列号'
          type: string
          required: false
          description: '用于标识一个HLR序列号。该参数必须先由**ADD HLRSN**命令定义，然后才能在此处引用。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        INGROUPID:
          name: '内部组ID'
          type: string
          required: false
          description: '用于标识移动网络内部设备之间通信时互相传递的组ID。在该特性中，该参数指的是家庭群组ID。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        EXTGROUPID:
          name: '外部组ID'
          type: string
          required: false
          description: '用于标识移动网络对外能力开放接口中提供的组ID。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SHAREDID:
          name: '共享数据ID'
          type: string
          required: false
          description: '用于标识为内部组创建的共享数据的ID。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SNSSAI:
          name: '切片标识'
          type: string
          required: false
          description: '用于标识5G系统中的网络切片。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        DNN:
          name: '数据网名称'
          type: string
          required: false
          description: '用于标识数据网名称。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PDUTYPES:
          name: '允许的PDU类型'
          type: string
          required: false
          description: '用于标识允许的PDU类型。'
          data_source: '固定配置'
          pattern: ''
          default: ''
    add_groupid_list:
      type: items
      properties:
        IMSI:
          name: 'IMSI'
          type: string
          required: false
          description: '用于标识需要加入5G虚拟网络组的终端和CPE的IMSI号码。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        INGROUPID:
          name: '内部组ID'
          type: string
          required: false
          description: '用于标识移动网络内部设备之间通信时互相传递的组ID。该参数必须由**ADD VNGROUP**命令定义后才能在此处引用。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
  examples:
    add_ngcqostpl_list:
    - HLRSN: '1'
      TPLID: '1'
      TPLNAME: tphome01
      NGQI: '9'
      ARPPRILEVEL: '1'
      PREEMPTIONCAP: TRUE
      PREEMPTIONVUL: FALSE
      NGQIPRILEVEL: '1'
    add_dnnqostpl_list:
    - HLRSN: '1'
      TPLID: '2'
      TPLNAME: tphome01
      PDUTYPE: IPV4
      SSCMODE: SSC_MODE_1
      NGCQOSTPLID: '1'
      AMBRUP: '5'
      UPUNIT: Gbps
      AMBRDW: '5'
      DWUNIT: Gbps
      CHARGE: 0800
    add_snssai_list:
    - IMSI: '460081000000001'
      SNSSAI: 1-010101
      DEFAULT: TRUE
    add_smdata_list:
    - IMSI: '460081000000001'
      SNSSAI: 1-010101
      DNN: home.dnn
      DEFAULT: TRUE
      DNNQOSTPLID: '2'
      MOBILE_HOME: TRUE
    add_vngroup_list:
    - HLRSN: '1'
      INGROUPID: 1001-46008-01
      EXTGROUPID: group01@huawei.com
      SHAREDID: 46008-huawei01
      SNSSAI: 1-010101
      DNN: home.dnn
      PDUTYPES: IPV4
    add_groupid_list:
    - IMSI: '460081000000001'
      INGROUPID: 1001-46008-01
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 登录UDM的“UDM业务管理”窗口。

### 2 配置使用的DNN信息。

#### 2.1 //创建5G QoS模板。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_ngcqostpl_list的变量区（command: ADD NGCQOSTPL） -#}
<!-- MISSING_MACRO: command=ADD NGCQOSTPL list_name=add_ngcqostpl_list step_id=2.1 -->
```

#### 2.2 //创建DNN QoS模板。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_dnnqostpl_list的变量区（command: ADD DNNQOSTPL） -#}
<!-- MISSING_MACRO: command=ADD DNNQOSTPL list_name=add_dnnqostpl_list step_id=2.2 -->
```

### 3 //签约切片数据。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_snssai_list的变量区（command: ADD SNSSAI） -#}
<!-- MISSING_MACRO: command=ADD SNSSAI list_name=add_snssai_list step_id=3 -->
```

### 4 签约会话管理数据。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_smdata_list的变量区（command: ADD SMDATA） -#}
<!-- MISSING_MACRO: command=ADD SMDATA list_name=add_smdata_list step_id=4 -->
```

### 5 增加一跳入家使用的5G LAN群组（家庭组）。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_vngroup_list的变量区（command: ADD VNGROUP） -#}
<!-- MISSING_MACRO: command=ADD VNGROUP list_name=add_vngroup_list step_id=5 -->
```

### 6 增加5G LAN组成员（家庭成员和CPE）。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_groupid_list的变量区（command: ADD GROUPID） -#}
<!-- MISSING_MACRO: command=ADD GROUPID list_name=add_groupid_list step_id=6 -->
```


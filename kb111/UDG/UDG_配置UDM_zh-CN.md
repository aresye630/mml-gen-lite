---
id: ''
name: 配置UDM
ne_type: UDG
type: feature
description: 该任务旨在指导操作人员配置一跳入家网关全局数据。
risk_level: ''
doc_source: ["特性部署","业务专题","5G Core 一跳入家解决方案","一跳入家解决方案（基于非3GPP接入方案）","业务初始部署与调测","部署一跳入家","配置UDM"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
该任务旨在指导操作人员配置一跳入家网关全局数据。

## 必备事项
前提条件

操作人员具有PGW Web LMT的操作权限。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    set_udmserv_list:
      type: items
      properties:
        SUPP_TOHOME:
          name: '支持智家随行业务'
          type: string
          required: false
          description: '用于标识UDM是否支持一跳入家业务。'
          data_source: '本端规划'
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
    set_udmserv_list_1:
      type: items
      properties:
        SUPP_TOHOME:
          name: '支持智家随行业务'
          type: string
          required: false
          description: '用于标识UDM是否支持一跳入家业务。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        GROUPID_MULTIDNNSILCE:
          name: '5GLAN支持签约相同的DNN和切片'
          type: string
          required: false
          description: '用于标识当执行**ADD GROUPID**命令给用户签约5G LAN群组时，是否可以签约多个数据网名称和切片标识相同的群组。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_vngroup_list_1:
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
    set_udmserv_list_2:
      type: items
      properties:
        GROUPID_MULTIDNNSILCE:
          name: '5GLAN支持签约相同的DNN和切片'
          type: string
          required: false
          description: '用于标识当执行**ADD GROUPID**命令给用户签约5G LAN群组时，是否可以签约多个数据网名称和切片标识相同的群组。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_vngroup_list_2:
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
  examples:
    set_udmserv_list:
    - SUPP_TOHOME: TRUE
    add_vngroup_list:
    - HLRSN: '1'
      INGROUPID: 1001-46008-01
      EXTGROUPID: group01@huawei.com
      SHAREDID: 46008-huawei02
      SNSSAI: 1-010101
      DNN: home.area1.dnn
      PDUTYPES: IPV4
    set_udmserv_list_1:
    - SUPP_TOHOME: TRUE
      GROUPID_MULTIDNNSILCE: FALSE
    add_vngroup_list_1:
    - HLRSN: '1'
      INGROUPID: 1001-46008-01
      EXTGROUPID: group01@huawei.com
      SHAREDID: 46008-huawei02
      SNSSAI: 1-010101
      DNN: home.area1.dnn
      PDUTYPES: IPV4
    set_udmserv_list_2:
    - GROUPID_MULTIDNNSILCE: FALSE
    add_vngroup_list_2:
    - HLRSN: '1'
      INGROUPID: 1001-46008-01
      EXTGROUPID: group01@huawei.com
      SHAREDID: 46008-huawei02
      SNSSAI: 1-010101
      DNN: home.area1.dnn
      PDUTYPES: IPV4
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 **任务1脚本：**

#### 1.1 登录“UDM业务管理”窗口。

#### 1.2 执行**SET UDMSERV**命令设置UDM支持一跳入家功能。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_udmserv_list的变量区（command: SET UDMSERV） -#}
<!-- MISSING_MACRO: command=SET UDMSERV list_name=set_udmserv_list step_id=1.2 -->
```

#### 1.3 执行**ADD VNGROUP**命令增加一跳入家使用的5G LAN群组（家庭组）。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_vngroup_list的变量区（command: ADD VNGROUP） -#}
<!-- MISSING_MACRO: command=ADD VNGROUP list_name=add_vngroup_list step_id=1.3 -->
```

### 2 **任务2脚本：**

#### 2.1 登录一跳入家UDM的“UDM业务管理”窗口。

#### 2.2 执行**SET UDMSERV**命令设置UDM业务数据。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_udmserv_list_1的变量区（command: SET UDMSERV） -#}
<!-- MISSING_MACRO: command=SET UDMSERV list_name=set_udmserv_list_1 step_id=2.2 -->
```

#### 2.3 执行**ADD VNGROUP**命令增加一跳入家使用的5G LAN群组（家庭组）。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_vngroup_list_1的变量区（command: ADD VNGROUP） -#}
<!-- MISSING_MACRO: command=ADD VNGROUP list_name=add_vngroup_list_1 step_id=2.3 -->
```

#### 大网UDM和一跳入家UDM分离部署场景下，该步骤在大网UDM和一跳入家UDM配置的数据需要保持一致。

#### 2.4 登录大网UDM的“UDM业务管理”窗口。

#### 2.5 执行**SET UDMSERV**命令设置UDM业务数据。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_udmserv_list_2的变量区（command: SET UDMSERV） -#}
<!-- MISSING_MACRO: command=SET UDMSERV list_name=set_udmserv_list_2 step_id=2.5 -->
```

#### 2.6 执行**ADD VNGROUP**命令增加一跳入家使用的5G LAN群组。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_vngroup_list_2的变量区（command: ADD VNGROUP） -#}
<!-- MISSING_MACRO: command=ADD VNGROUP list_name=add_vngroup_list_2 step_id=2.6 -->
```


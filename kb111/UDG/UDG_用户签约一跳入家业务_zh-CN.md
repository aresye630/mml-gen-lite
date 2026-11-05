---
id: ''
name: 用户签约一跳入家业务
ne_type: UDG
type: feature
description: 该任务旨在指导操作人员给用户配置一跳入家网关签约数据。  完成了一跳入家基础的业务部署与调测，网络就具备了为家庭用户开通一跳入家的能力。当家庭用户有开通业务诉求时，可以通过如下方式完成数据签约和业务开通。  * 家庭成员和家庭网关在运营商BOSS系统进行签约。签约完成后BOSS系统通过运维接口下发签约信息到UDM上 。 * 如果BOSS系统和UDM之间的运维接口尚未支持，请参考本章节在UDM上人工配置签约数据。
risk_level: ''
doc_source: ["特性部署","业务专题","5G Core 一跳入家解决方案","一跳入家解决方案（基于非3GPP接入方案）","一跳入家业务开通","用户签约一跳入家业务"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
该任务旨在指导操作人员给用户配置一跳入家网关签约数据。完成了一跳入家基础的业务部署与调测，网络就具备了为家庭用户开通一跳入家的能力。当家庭用户有开通业务诉求时，可以通过如下方式完成数据签约和业务开通。* 家庭成员和家庭网关在运营商BOSS系统进行签约。签约完成后BOSS系统通过运维接口下发签约信息到UDM上 。* 如果BOSS系统和UDM之间的运维接口尚未支持，请参考本章节在UDM上人工配置签约数据。

## 必备事项
前提条件

* 操作人员具有PGW Web LMT的操作权限。
* 一跳入家家庭网关IMSI号码已开户。用户A和用户B已分别完成5G开户。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    add_grpmember_list:
      type: items
      properties:
        ISDN:
          name: '智家随行家庭网关MSISDN号码'
          type: string
          required: false
          description: '用于标识待签约一跳入家家庭网关的MSISDN号码。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        GRPNAME:
          name: '智家随行家庭网关名称'
          type: string
          required: false
          description: '用于标识一跳入家家庭网关名称。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        INGROUPID:
          name: '智家随行内部群组号'
          type: string
          required: false
          description: '用于标识一跳入家内部群组号，指的是一跳入家群组使用的5G LAN群组号。该参数必须由**ADD VNGROUP**命令定义后才能在此处引用。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        EXTID:
          name: '智家随行家庭网关扩展ID'
          type: string
          required: false
          description: '用于标识一跳入家群组中家庭网关的扩展ID。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_grpmember_list_1:
      type: items
      properties:
        ISDN:
          name: '智家随行家庭网关MSISDN号码'
          type: string
          required: false
          description: '用于标识待签约一跳入家家庭网关的MSISDN号码。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        GRPNAME:
          name: '智家随行家庭网关名称'
          type: string
          required: false
          description: '用于标识一跳入家家庭网关名称。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        INGROUPID:
          name: '智家随行内部群组号'
          type: string
          required: false
          description: '用于标识一跳入家内部群组号，指的是一跳入家群组使用的5G LAN群组号。该参数必须由**ADD VNGROUP**命令定义后才能在此处引用。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_groupid_list:
      type: items
      properties:
        ISDN:
          name: 'MSISDN'
          type: string
          required: false
          description: '用于标识需要加入5G虚拟网络组的用户的MSISDN号码。'
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
    add_groupid_list_1:
      type: items
      properties:
        ISDN:
          name: 'MSISDN'
          type: string
          required: false
          description: '用于标识需要加入5G虚拟网络组的用户的MSISDN号码。'
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
    add_grpmember_list_2:
      type: items
      properties:
        ISDN:
          name: '智家随行家庭网关MSISDN号码'
          type: string
          required: false
          description: '用于标识待签约一跳入家家庭网关的MSISDN号码。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        GRPNAME:
          name: '智家随行家庭网关名称'
          type: string
          required: false
          description: '用于标识一跳入家家庭网关名称。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        INGROUPID:
          name: '智家随行内部群组号'
          type: string
          required: false
          description: '用于标识一跳入家内部群组号，指的是一跳入家群组使用的5G LAN群组号。该参数必须由**ADD VNGROUP**命令定义后才能在此处引用。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        EXTID:
          name: '智家随行家庭网关扩展ID'
          type: string
          required: false
          description: '用于标识一跳入家群组中家庭网关的扩展ID。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_grpmember_list_3:
      type: items
      properties:
        ISDN:
          name: '智家随行家庭网关MSISDN号码'
          type: string
          required: false
          description: '用于标识待签约一跳入家家庭网关的MSISDN号码。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        GRPNAME:
          name: '智家随行家庭网关名称'
          type: string
          required: false
          description: '用于标识一跳入家家庭网关名称。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        INGROUPID:
          name: '智家随行内部群组号'
          type: string
          required: false
          description: '用于标识一跳入家内部群组号，指的是一跳入家群组使用的5G LAN群组号。该参数必须由**ADD VNGROUP**命令定义后才能在此处引用。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_groupid_list_2:
      type: items
      properties:
        ISDN:
          name: 'MSISDN'
          type: string
          required: false
          description: '用于标识需要加入5G虚拟网络组的用户的MSISDN号码。'
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
    add_groupid_list_3:
      type: items
      properties:
        ISDN:
          name: 'MSISDN'
          type: string
          required: false
          description: '用于标识需要加入5G虚拟网络组的用户的MSISDN号码。'
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
    add_grpmember_list:
    - ISDN: '13310911003'
      GRPNAME: home1
      INGROUPID: 1001-46008-01
      EXTID: '460030913121003_85617813'
    add_grpmember_list_1:
    - ISDN: '13310911003'
      GRPNAME: home2
      INGROUPID: 1001-46008-01
    add_groupid_list:
    - ISDN: '13310911003'
      INGROUPID: 1001-46008-01
    add_groupid_list_1:
    - ISDN: '13310911005'
      INGROUPID: 1001-46008-01
    add_grpmember_list_2:
    - ISDN: '13310911001'
      GRPNAME: home1
      INGROUPID: 1001-46008-01
      EXTID: '460030913121001_85617811'
    add_grpmember_list_3:
    - ISDN: '13310911001'
      GRPNAME: home2
      INGROUPID: 1001-46008-01
    add_groupid_list_2:
    - ISDN: '13310911003'
      INGROUPID: 1001-46008-01
    add_groupid_list_3:
    - ISDN: '13310911005'
      INGROUPID: 1001-46008-01
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 **任务1脚本：**

#### 1.1 登录“UDM业务管理”窗口。

#### 1.2 执行**ADD GRPMEMBER**命令将家庭网关设备加入群组，以下两种方案二选一。

##### 1.2.1 营业厅直接分配家庭网关扩展ID

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_grpmember_list的变量区（command: ADD GRPMEMBER） -#}
<!-- MISSING_MACRO: command=ADD GRPMEMBER list_name=add_grpmember_list step_id=1.2.1 -->
```

##### 1.2.2 UDM分配家庭网关扩展ID

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_grpmember_list_1的变量区（command: ADD GRPMEMBER） -#}
<!-- MISSING_MACRO: command=ADD GRPMEMBER list_name=add_grpmember_list_1 step_id=1.2.2 -->
```

#### “智家随行家庭网关IMSI号码”为“460030913121003”，“智家随行家庭网关MSISDN号码”为“13310911003”。

#### 一个家庭网关只能被一个一跳入家家庭网关IMSI号码管理。

#### 1.3 执行**ADD GROUPID**命令给成员A（已经完成5G开户，ISDN为13310911003）签约住宅所在5G LAN群组。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_groupid_list的变量区（command: ADD GROUPID） -#}
<!-- MISSING_MACRO: command=ADD GROUPID list_name=add_groupid_list step_id=1.3 -->
```

#### 1.4 执行**ADD GROUPID**命令给成员B（已经完成5G开户，ISDN为13310911005）签约住宅所在5G LAN群组。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_groupid_list_1的变量区（command: ADD GROUPID） -#}
<!-- MISSING_MACRO: command=ADD GROUPID list_name=add_groupid_list_1 step_id=1.4 -->
```

### 2 **任务2脚本：**

#### 2.1 登录一跳入家UDM的“UDM业务管理”窗口。

#### 2.2 执行**ADD GRPMEMBER**命令将家庭网关设备加入群组，以下两种方案二选一。

##### 2.2.1 营业厅直接分配家庭网关扩展ID

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_grpmember_list_2的变量区（command: ADD GRPMEMBER） -#}
<!-- MISSING_MACRO: command=ADD GRPMEMBER list_name=add_grpmember_list_2 step_id=2.2.1 -->
```

##### 2.2.2 UDM分配家庭网关扩展ID

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_grpmember_list_3的变量区（command: ADD GRPMEMBER） -#}
<!-- MISSING_MACRO: command=ADD GRPMEMBER list_name=add_grpmember_list_3 step_id=2.2.2 -->
```

#### “智家随行家庭网关IMSI号码”为“460030913121001”，“智家随行家庭网关MSISDN号码”为“13310911001”。

#### 一个家庭网关只能被一个一跳入家家庭网关IMSI号码管理。

#### 2.3 登录大网UDM的“UDM业务管理”窗口。

#### 2.4 执行**ADD GROUPID**命令给成员A（已经完成5G开户，ISDN为13310911003）签约住宅所在5G LAN群组。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_groupid_list_2的变量区（command: ADD GROUPID） -#}
<!-- MISSING_MACRO: command=ADD GROUPID list_name=add_groupid_list_2 step_id=2.4 -->
```

#### 2.5 执行**ADD GROUPID**命令给成员B（已经完成5G开户，ISDN为13310911005）签约住宅所在5G LAN群组。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_groupid_list_3的变量区（command: ADD GROUPID） -#}
<!-- MISSING_MACRO: command=ADD GROUPID list_name=add_groupid_list_3 step_id=2.5 -->
```


---
id: ''
name: 配置NCG/CHF(OCS)选择方式
ne_type: UDG
type: feature
description: 当UNC部署融合计费功能时需要对接NCG/CHF（OCS），本指导用于描述对接NCG/CHF（OCS）的配置操作过程。  UNC支持基于IMSI选择NCG/CHF(OCS)、基于IMSI号段选择NCG/CHF(OCS)、基于PCF下发的FQDN选择NCG/CHF(OCS)、基于用户的计费属性Charging Characteristics（CC）选择NCG/CHF(OCS)，也支持基于标准化服务发现选择NCG/CHF(OCS)。  UNC选择NCG/CHF(OCS)的优先级从高到低依次是：基于IMSI选择NCG/CHF(OCS) > 基于IMSI号段选择NCG/CHF(OCS) > 基于PCF下发的信息选择NCG/CHF(OCS) > 基于从UDM获取的签约CC选择NCG/CHF(OCS) > 基于标准化服务发现选择NCG/CHF(OCS) > 基于SMF本地配置的CC选择NCG/CHF(OCS)。如果无法通过高优先级的方式选择NCG/CHF(OCS)，则依次向下使用低一级别的方式进行选择。  其中，通过**ADD SELCHFGBYIMSI**命令配置基于IMSI选择NCG/CHF(OCS)方式一般用于测试场景，将指定IMSI的用户的计费信息发送到指定NCG/CHF(OCS)上，测试NCG/CHF(OCS)的基本功能。  * 当通过NRF服务发现NCG/CHF（OCS），不需要在UNC上配置NCG/CHF（OCS）。通过本地NRF方式发现NCG/CHF（OCS）操作参考UNC产品文档的“网络部署 > 初始配置 > UNC初始配置与调测 > 组网对接配置 > 配置SMF&PGW-C&SGW-C&GGSN > 配置SMF > 配置和NF直连”中的配置到CHF的数据完成相关配置。 * 如果已参考UNC产品文档的“网络部署 > 初始配置 > UNC初始配置与调测 > 组网对接配置 > 配置SMF&PGW-C&SGW-C&GGSN > 公共配置 > （可选）配置到计费系统和策略控制网元的对接（Ga/Gy/N40/Gx/N7） > （可选）配置到CHF的数据（GGSN/PGW-C/SMF）”完成相关配置，则无需再执行本来章节。
risk_level: ''
doc_source: ["特性部署","业务专题","5G Core 计费解决方案","计费解决方案概述","计费方案部署与调测","方案四：部署NCG且基于服务化接口的离线+在线计费组网方案（N40接口）","SMF配置","融合计费对接配置（N40接口）","配置NCG/CHF(OCS)选择方式"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
当UNC部署融合计费功能时需要对接NCG/CHF（OCS），本指导用于描述对接NCG/CHF（OCS）的配置操作过程。UNC支持基于IMSI选择NCG/CHF(OCS)、基于IMSI号段选择NCG/CHF(OCS)、基于PCF下发的FQDN选择NCG/CHF(OCS)、基于用户的计费属性Charging Characteristics（CC）选择NCG/CHF(OCS)，也支持基于标准化服务发现选择NCG/CHF(OCS)。UNC选择NCG/CHF(OCS)的优先级从高到低依次是：基于IMSI选择NCG/CHF(OCS) > 基于IMSI号段选择NCG/CHF(OCS) > 基于PCF下发的信息选择NCG/CHF(OCS) > 基于从UDM获取的签约CC选择NCG/CHF(OCS) > 基于标准化服务发现选择NCG/CHF(OCS) > 基于SMF本地配置的CC选择NCG/CHF(OCS)。如果无法通过高优先级的方式选择NCG/CHF(OCS)，则依次向下使用低一级别的方式进行选择。其中，通过**ADD SELCHFGBYIMSI**命令配置基于IMSI选择NCG/CHF(OCS)方式一般用于测试场景，将指定IMSI的用户的计费信息发送到指定NCG/CHF(OCS)上，测试NCG/CHF(OCS)的基本功能。* 当通过NRF服务发现NCG/CHF（OCS），不需要在UNC上配置NCG/CHF（OCS）。通过本地NRF方式发现NCG/CHF（OCS）操作参考UNC产品文档的“网络部署 > 初始配置 > UNC初始配置与调测 > 组网对接配置 > 配置SMF&PGW-C&SGW-C&GGSN > 配置SMF > 配置和NF直连”中的配置到CHF的数据完成相关配置。* 如果已参考UNC产品文档的“网络部署 > 初始配置 > UNC初始配置与调测 > 组网对接配置 > 配置SMF&PGW-C&SGW-C&GGSN > 公共配置 > （可选）配置到计费系统和策略控制网元的对接（Ga/Gy/N40/Gx/N7） > （可选）配置到CHF的数据（GGSN/PGW-C/SMF）”完成相关配置，则无需再执行本来章节。

## 必备事项
前提条件

* 请仔细阅读融合计费原理。
* 完成加载License。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    add_tnfins_list:
      type: items
      properties:
        TNFINSINDEX:
          name: '目标NF实例索引'
          type: string
          required: false
          description: '增加主备NCG/CHF(OCS)。  “FQDN”要与PCF下发的FQDN名称保持一致。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        TNFTYPE:
          name: '目标NF类型'
          type: string
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
        TNFINSNAME:
          name: '目标NF实例名称'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        SCHEMA:
          name: '协议模式'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        FQDN:
          name: '域名'
          type: string
          required: false
          description: ''
          data_source: '从对端获取'
          pattern: ''
          default: ''
    add_tnfinsip_list:
      type: items
      properties:
        TNFINSINDEX:
          name: '目标NF实例索引'
          type: string
          required: false
          description: '增加主备NCG/CHF(OCS)的IP地址。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPTYPE:
          name: 'IP地址类型'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV4ADDR:
          name: 'IPV4类型地址'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PORT:
          name: '端口号'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_tnfgrp_list:
      type: items
      properties:
        TNFGRPINDEX:
          name: '目标NF组索引'
          type: string
          required: false
          description: '配置NCG/CHF(OCS) 组。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        TNFTYPE:
          name: '目标NF类型'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        TNFGRPNAME:
          name: '目标NF组名称'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_tnfbindgrp_list:
      type: items
      properties:
        TNFGRPINDEX:
          name: '目标NF组索引'
          type: string
          required: false
          description: '将NCG/CHF(OCS)实例绑定到NCG/CHF(OCS)组上。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        TNFINSINDEX:
          name: '目标NF实例索引'
          type: string
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    set_chfselectmode_list:
      type: items
      properties:
        FIRSTMODE:
          name: '首选模式'
          type: string
          required: false
          description: '设置用户激活和在线恢复场景NCG/CHF(OCS)的选择模式。  说明：  此示例首选模式为使用本地配置的NCG/CHF(OCS)，此时没有备选模式。如果首选模式为使用PCF指定的NCG/CHF(OCS)或者使用NRF发现的NCG/CHF(OCS)时，可以配置备选模式。  请根据业务实际需要进行配置。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        SECONDMODE:
          name: '备选模式'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    set_glbdftchfgroup_list:
      type: items
      properties:
        PRIMARYCHFGRP:
          name: '主CHF组'
          type: string
          required: false
          description: '配置系统缺省的NCG/CHF(OCS)组。建议配置缺省的NCG/CHF(OCS)组，避免选择不到NCG/CHF(OCS)。  说明：  “PRIMARYCHFGRP”和“SECONDARYCHFGRP”使用**ADD TNFGRP**命令配置生成。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        SECONDARYCHFGRP:
          name: '备CHF组'
          type: string
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_selectchfgbycc_list:
      type: items
      properties:
        CCTYPE:
          name: 'Charge Characteristic类型'
          type: string
          required: false
          description: '配置计费属性和NCG/CHF(OCS)组的关联关系，基于计费属性选择使用的NCG/CHF(OCS)组。  说明：  * “PRIORITY”数值越小，优先级越高。 * “PRIMARYCHFGRP”和“SECONDARYCHFGRP”使用**ADD TNFGRP**命令配置生成。 * 本示例以计费属性0x0100举例，请根据业务实际需要进行配置。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        CCVALUE:
          name: 'Charge Characteristic值'
          type: string
          required: false
          description: ''
          data_source: '已配置数据中获取/从对端获取'
          pattern: ''
          default: ''
        MASK:
          name: 'Charge Characteristic特定值掩码'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        PRIORITY:
          name: 'Charge Characteristic优先级'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        PRIMARYCHFGRP:
          name: '主CHF组'
          type: string
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        SECONDARYCHFGRP:
          name: '备CHF组'
          type: string
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_selchfgbimsiseg_list:
      type: items
      properties:
        SEGSTART:
          name: '号段起始字符串'
          type: string
          required: false
          description: '(可选)配置号段与和NCG/CHF(OCS)组的关联关系，基于号段选择使用的NCG/CHF(OCS)组。  说明：  * “PRIMARYCHFGRP”和“SECONDARYCHFGRP”使用**ADD TNFGRP**命令配置生成。 * 本示例取值为举例，请根据业务实际需要进行配置。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SEGEND:
          name: '号段结束字符串'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        PRIMARYCHFGRP:
          name: '主CHF组'
          type: string
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        SECONDARYCHFGRP:
          name: '备CHF组'
          type: string
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
  examples:
    add_tnfins_list:
    - TNFINSINDEX: '1'
      TNFTYPE: CHF
      TNFINSNAME: target_chf_0
      SCHEMA: http
      FQDN: chf1.hw.com
    add_tnfinsip_list:
    - TNFINSINDEX: '1'
      IPTYPE: IPV4
      IPV4ADDR: 192.168.94.2
      PORT: '3220'
    add_tnfgrp_list:
    - TNFGRPINDEX: '1'
      TNFTYPE: CHF
      TNFGRPNAME: ChfGroup1
    add_tnfbindgrp_list:
    - TNFGRPINDEX: '1'
      TNFINSINDEX: '1'
    set_chfselectmode_list:
    - FIRSTMODE: LOCAL
      SECONDMODE: '-'
    set_glbdftchfgroup_list:
    - PRIMARYCHFGRP: ChfGroup1
      SECONDARYCHFGRP: ChfGroup2
    add_selectchfgbycc_list:
    - CCTYPE: VALUE
      CCVALUE: '0x0100'
      MASK: '0xFFFF'
      PRIORITY: '1'
      PRIMARYCHFGRP: ChfGroup1
      SECONDARYCHFGRP: ChfGroup2
    add_selchfgbimsiseg_list:
    - SEGSTART: '12345678901'
      SEGEND: '12345678905'
      PRIMARYCHFGRP: ChfGroup1
      SECONDARYCHFGRP: ChfGroup2
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 配置目标NCG/CHF(OCS)。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_tnfins_list的变量区（command: ADD TNFINS） -#}
<!-- MISSING_MACRO: command=ADD TNFINS list_name=add_tnfins_list step_id=1 -->
```

### 2 配置目标NCG/CHF(OCS)的IP地址信息。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_tnfinsip_list的变量区（command: ADD TNFINSIP） -#}
<!-- MISSING_MACRO: command=ADD TNFINSIP list_name=add_tnfinsip_list step_id=2 -->
```

### 3 配置NCG/CHF(OCS)组。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_tnfgrp_list的变量区（command: ADD TNFGRP） -#}
<!-- MISSING_MACRO: command=ADD TNFGRP list_name=add_tnfgrp_list step_id=3 -->
```

### 4 将目标NCG/CHF(OCS)绑定到NCG/CHF(OCS)组。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_tnfbindgrp_list的变量区（command: ADD TNFBINDGRP） -#}
<!-- MISSING_MACRO: command=ADD TNFBINDGRP list_name=add_tnfbindgrp_list step_id=4 -->
```

### 5 设置用户激活和在线恢复场景NCG/CHF(OCS)的选择模式。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_chfselectmode_list的变量区（command: SET CHFSELECTMODE） -#}
<!-- MISSING_MACRO: command=SET CHFSELECTMODE list_name=set_chfselectmode_list step_id=5 -->
```

### 6 配置系统缺省的NCG/CHF(OCS)组。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_glbdftchfgroup_list的变量区（command: SET GLBDFTCHFGROUP） -#}
<!-- MISSING_MACRO: command=SET GLBDFTCHFGROUP list_name=set_glbdftchfgroup_list step_id=6 -->
```

### 7 配置计费属性和NCG/CHF(OCS)组的关联关系，基于计费属性选择使用的NCG/CHF(OCS)组。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_selectchfgbycc_list的变量区（command: ADD SELECTCHFGBYCC） -#}
<!-- MISSING_MACRO: command=ADD SELECTCHFGBYCC list_name=add_selectchfgbycc_list step_id=7 -->
```

### 8 配置号段与和NCG/CHF(OCS)组的关联关系，基于号段选择使用的NCG/CHF(OCS)组。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_selchfgbimsiseg_list的变量区（command: ADD SELCHFGBIMSISEG） -#}
<!-- MISSING_MACRO: command=ADD SELCHFGBIMSISEG list_name=add_selchfgbimsiseg_list step_id=8 -->
```


---
id: ''
name: 配置专用DNN基础数据
ne_type: UNC
type: feature
description: 本操作用于指导专用DNN上线时，如何修改PCF向NRF注册的网元信息配置。
risk_level: ''
doc_source: ["网络部署","业务专题","5G Core 一跳入家解决方案","一跳入家解决方案（基于3GPP接入方案）","业务初始部署与调测","部署移动VPN","配置专用DNN数据","配置PCF","配置专用DNN数据","配置专用DNN基础数据"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本操作用于指导专用DNN上线时，如何修改PCF向NRF注册的网元信息配置。

## 必备事项
前提条件

已按照运营商配置规范完成PCF网元的基本配置，并与周边网元完成对接。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    add_nfdnngrp_list:
      type: items
      properties:
        GRPNAME:
          name: '组名称'
          type: string
          required: false
          description: '用于标识一个网元DNN组信息所属组的信息。  取值范围：长度不超过32的字符串，只允许输入0～9，a～z，A～Z，“-”和“\_”。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        INDEX:
          name: 'INDEX'
          type: string
          required: false
          description: '用于标识一个网元DNN组信息在组内的唯一一条记录。  取值范围：1~10240  配置原则：该参数在不同的组名称下可以重复，但和组名称组合以后成为全局唯一对象关键字段，组合不能重复。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        DNN:
          name: 'DNN'
          type: string
          required: false
          description: '用于标识DNN。  取值范围：长度不超过64的字符串。  说明：  * 如果对端SMF不区分大小写，PCF上需要配置为小写。 * 如果对端SMF区分大小写，需和对端SMF协商保持一致。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_nfinfo_list:
      type: items
      properties:
        NFINFOID:
          name: 'NFINFOID'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NFTYPE:
          name: 'NFTYPE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NFDNNGRP:
          name: 'NFDNNGRP'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DNNLIST:
          name: 'DNNLIST'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    mod_nfinfo_list:
      type: items
      properties:
        NFINFOID:
          name: '网元信息标识'
          type: string
          required: false
          description: '标识网元数据记录的关键字段之一，可以使用**LST NFINFO**命令查询获得。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        NFTYPE:
          name: '网元类型'
          type: string
          required: false
          description: '标识网元数据记录的关键字段之一，可以使用**LST NFINFO**命令查询获得。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        DNNLIST:
          name: 'DNN列表'
          type: string
          required: false
          description: '可选参数，用于指定网元的DNN列表。  取值范围：长度不超过4096的字符串，字符串由数字、字母、“-”，“.”或“,”组成，开头和结尾不能含有“-”、“.”或“,”，多值之间用“,”分隔，但不能连续使用两个“,”。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        NFDNNGRP:
          name: 'DNN组'
          type: string
          required: false
          description: '可选参数，用于指定本端网元的DNN组。通过**ADD NFDNNGRP**命令配置。  取值范围：长度不超过32的字符串，只允许输入0～9，a～z，A～Z，“-”和“\_”。'
          data_source: '本端规划'
          pattern: ''
          default: ''
  examples:
    add_nfdnngrp_list:
    - GRPNAME: NFDNNGRP-PCF01
      INDEX: '1'
      DNN: stjwt.gd
    add_nfinfo_list:
    - NFINFOID: Group-HNGZgdPCF015PCF001BHW
      NFTYPE: PCF
      NFDNNGRP: NFDNNGRP-PCF01
      DNNLIST: stjwt.gd
    mod_nfinfo_list:
    - NFINFOID: Group-HNGZgdPCF015PCF001BHW
      NFTYPE: PCF
      DNNLIST: stjwt.gd
      NFDNNGRP: NFDNNGRP-PCF01
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 执行命令**ADD NFDNNGRP**增加网元DNN组信息，添加专用DNN（以stjwt.gd为例）至DNN组。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_nfdnngrp_list的变量区（command: ADD NFDNNGRP） -#}
<!-- MISSING_MACRO: command=ADD NFDNNGRP list_name=add_nfdnngrp_list step_id=1 -->
```

### 2 执行**LST NFINFO**查询网元信息，查看是否已配置“DNNLIST”。

#### 2.1 是=>4=>结束

#### 2.2 否=>3=>结束

### 3 执行命令**ADD NFINFO**添加网元信息，配置DNN组。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_nfinfo_list的变量区（command: ADD NFINFO） -#}
<!-- MISSING_MACRO: command=ADD NFINFO list_name=add_nfinfo_list step_id=3 -->
```

### 4 执行命令**MOD NFINFO**修改网元信息，配置DNN组。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该mod_nfinfo_list的变量区（command: MOD NFINFO） -#}
<!-- MISSING_MACRO: command=MOD NFINFO list_name=mod_nfinfo_list step_id=4 -->
```


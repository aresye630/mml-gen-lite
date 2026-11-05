---
id: ''
name: 删除VPN组（VNRS_VNFC）
ne_type: UEG
type: feature
description: 本操作指导介绍在运行网络中删除VPN组的基本操作过程。支持删除VPN组或仅删除VPN组成员。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝S","MEC 特性指南（风筝S）","UEG特性指南","IP基本特性","IPFD-020400 IP可靠性","IPFD-020401 QoS","特性配置","复杂流分类配置（VNRS_VNFC）","删除VPN组（VNRS_VNFC）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
本操作指导介绍在运行网络中删除VPN组的基本操作过程。支持删除VPN组或仅删除VPN组成员。

## 必备事项
前提条件

前提条件

* 设备加电并正常启动
* 该接口在设备上存在
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    rmv_sqosvpngroup_list:
      type: items
      properties:
        VPNGROUPNAME:
          name: 'VPN组名称'
          type: string
          maxLength: 31
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    rmv_sqosvpngroupmem_list:
      type: items
      properties:
        VPNGROUPNAME:
          name: 'VPN组名称'
          type: string
          maxLength: 31
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        VPNNAME:
          name: 'VPN名称'
          type: string
          maxLength: 31
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        VPNPRIORITY:
          name: 'VPN优先级'
          type: integer
          minimum: 1
          maximum: 16
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
  examples:
    rmv_sqosvpngroup_list:
    - VPNGROUPNAME: 'test1'
    rmv_sqosvpngroupmem_list:
    - VPNGROUPNAME: 'test1'
      VPNNAME: 'vpn1'
      VPNPRIORITY: 2
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 删除已经创建的VPN组

### 在“MML命令行-UEG”窗口上执行：

```jinja2
{%- for item in rmv_sqosvpngroup_list -%}
    RMV SQOSVPNGROUP:
    {#- --- 必选参数 --- -#}
    VPNGROUPNAME="{{item.VPNGROUPNAME}}",
    ;
{%- endfor -%}
```

### 2 删除VPN组成员

### 在“MML命令行-UEG”窗口上执行：

```jinja2
{%- for item in rmv_sqosvpngroupmem_list -%}
    RMV SQOSVPNGROUPMEM:
    {#- --- 必选参数 --- -#}
    VPNGROUPNAME="{{item.VPNGROUPNAME}}",
    VPNNAME="{{item.VPNNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.VPNPRIORITY is not none -%}
        VPNPRIORITY={{item.VPNPRIORITY}},
    {%- endif -%}
    ;
{%- endfor -%}
```


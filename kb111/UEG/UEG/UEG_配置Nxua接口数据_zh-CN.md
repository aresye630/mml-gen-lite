---
id: ''
name: 配置Nxua接口数据
ne_type: UEG
type: feature
description: UEG作为MPF，与UPF对接时，需要配置Nxua接口与UPF互通。
tags: []
risk_level: ''
doc_source:
  - ["网络部署","园区入驻+地市共享（连接+计算）","5GC toB 部署边缘站点（站点为“风筝S”，带计算）","UEG初始配置（风筝S）","初始配置与调测（MPF）","初始配置与调测（MPF，非SDN）","参考：详细配置指导","配置MPF","配置Nxua接口数据"]
  - ["网络部署","园区入驻+地市共享（连接+计算）","5GC toB 部署边缘站点（站点为“风筝S”，带计算）","UEG初始配置（风筝S）","初始配置与调测（MPF）","初始配置与调测（MPF，SDN）","参考：详细配置指导","配置MPF","配置Nxua接口数据"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
UEG作为MPF，与UPF对接时，需要配置Nxua接口与UPF互通。

## 必备事项
前提条件

* 具备管理员权限的操作人员已经登录华为操作维护系统（登录MAE客户端或登录OM Portal）。
* 请了解UEG各类接口的类型及命名规范，具体内容请参见逻辑接口介绍（MPF）。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    add_vpninst_list:
      type: items
      properties:
        VPNINSTANCE:
          name: 'VPN实例名'
          type: string
          maxLength: 31
          required: true
          description: '逻辑接口的VPN一定要与其对应的外联口的VPN相同，否则从逻辑接口发出去的报文会查询路由失败。'
          data_source: '参见“5G Core LLD文档 > 路由设计 > 5G Core路由设计 > VRF设计 > VRF名称(VNF)”。'
          pattern: ''
          default: ''
    add_logicinf_list:
      type: items
      properties:
        NAME:
          name: '逻辑接口名称'
          type: string
          maxLength: 63
          required: true
          description: '一个VNF上最多可以配置32个Nxua接口，最后一个数字取值范围是0～31。'
          data_source: '参见“5G Core LLD文档 > 业务IP对接设计 > 业务IP设计 > 逻辑接口”。'
          pattern: ''
          default: ''
        IPVERSION:
          name: '逻辑接口的IP版本'
          type: string
          enum:
          - IPV4
          - IPV6
          - IPVER_ALL
          required: true
          description: '如果规划逻辑接口使用IPv4v6双栈组网，则该参数取值为“IPVER\_ALL”，分别配置IPv4和IPv6地址。'
          data_source: '-'
          pattern: ''
          default: ''
        IPV4ADDRESS1:
          name: '逻辑接口的IPv4地址1'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '参见“5G Core LLD文档 > 业务IP对接设计 > 业务IP设计 > 逻辑接口IP”。'
          pattern: ''
          default: ''
        IPV4MASK1:
          name: '逻辑接口的IPv4掩码1'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
        VPNINSTANCE:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: false
          description: '-'
          data_source: '参见“5G Core LLD文档 > 路由设计 > 5G Core路由设计 > VRF设计 > VRF名称(VNF)”。'
          pattern: ''
          default: ''
    add_vnivpnmap_list:
      type: items
      properties:
        VNI:
          name: 'VNI'
          type: integer
          minimum: 0
          maximum: 16777215
          required: true
          description: '该映射关系用于将从VXLAN隧道接收的报文中的VNI映射成VPN实例名称。  与UPF上配置的VNI相同。  如需了解VXLAN-GPE报文格式，请跳转到VXLAN-GPE。'
          data_source: '与对端协商'
          pattern: ''
          default: ''
        VPNINSTANCE:
          name: 'VPN实例'
          type: string
          maxLength: 31
          required: true
          description: '与N6x外联口绑定的VPN实例相同。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
  examples:
    add_vpninst_list:
    - VPNINSTANCE: 'VRF_Nxua'
    add_logicinf_list:
    - NAME: 'Nxuaif1/1/0'
      IPVERSION: IPV4
      IPV4ADDRESS1: '10.1.9.1'
      IPV4MASK1: '255.255.255.255'
      VPNINSTANCE: 'VRF_Nxua'
    add_vnivpnmap_list:
    - VNI: 1
      VPNINSTANCE: 'VRF_N6x'
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 进入“MML命令行-UEG”窗口。

### 2 配置Nxua逻辑接口所属的VPN实例。

```jinja2
{%- for item in add_vpninst_list -%}
    ADD VPNINST:
    {#- --- 必选参数 --- -#}
    VPNINSTANCE="{{item.VPNINSTANCE}}",
    ;
{%- endfor -%}
```

### 逻辑接口的VPN一定要与其对应的外联口的VPN相同，否则从逻辑接口发出去的报文会查询路由失败。

### 3 配置Nxua逻辑接口。

```jinja2
{%- for item in add_logicinf_list -%}
    ADD LOGICINF:
    {#- --- 必选参数 --- -#}
    NAME="{{item.NAME}}",
    IPVERSION={{item.IPVERSION}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPVERSION=IPV4/IPVER_ALL 时必选 --- -#}
    {%- if item.IPVERSION in ['IPV4', 'IPVER_ALL'] -%}
        IPV4ADDRESS1="{{item.IPV4ADDRESS1}}",
    {%- endif -%}
    {#- --- 条件必选：IPVERSION=IPV4/IPVER_ALL 时必选 --- -#}
    {%- if item.IPVERSION in ['IPV4', 'IPVER_ALL'] -%}
        IPV4MASK1="{{item.IPV4MASK1}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：IPVERSION=IPV4/IPV6/IPVER_ALL 时可选 --- -#}
    {%- if item.IPVERSION in ['IPV4', 'IPV6', 'IPVER_ALL'] -%}
        {%- if item.VPNINSTANCE is not none -%}
            VPNINSTANCE="{{item.VPNINSTANCE}}",
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 配置VNI到VPN的映射。

```jinja2
{%- for item in add_vnivpnmap_list -%}
    ADD VNIVPNMAP:
    {#- --- 必选参数 --- -#}
    VNI={{item.VNI}},
    VPNINSTANCE="{{item.VPNINSTANCE}}",
    ;
{%- endfor -%}
```


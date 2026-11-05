---
id: ''
name: 配置Sc/N9c/S5-S/S8-S接口数据
ne_type: UEG
type: feature
description: 运营商在部署5G或4G/5G互操作的分组交换网时新增ULCL UPF/BP UPF/I-UPF/SGW-U中的任一独立设备或融合设备，在完成配置UEG到PSA UPF/PGW-U的路由数据后，可在UEG上配置Sc/N9c/S5-S/S8-S接口数据使UEG与PSA UPF/PGW-U建立逻辑连接。
tags: []
risk_level: ''
doc_source: ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（一号通专网煤矿场景，入驻式）","软件安装与开站","UEG软件安装与开站","UEG初始配置","参考：详细配置指导","配置主锚点UPF","配置Sc/N9c/S5-S/S8-S接口数据"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
运营商在部署5G或4G/5G互操作的分组交换网时新增ULCL UPF/BP UPF/I-UPF/SGW-U中的任一独立设备或融合设备，在完成配置UEG到PSA UPF/PGW-U的路由数据后，可在UEG上配置Sc/N9c/S5-S/S8-S接口数据使UEG与PSA UPF/PGW-U建立逻辑连接。

## 必备事项
前提条件

* 具备管理员权限的操作人员已经登录华为操作维护系统（登录MAE客户端或登录OM Portal）。
* 请了解UEG各类接口的类型及命名规范，具体内容请参见逻辑接口介绍（UPF）（风筝S）/逻辑接口介绍（风筝M）/逻辑接口介绍（风筝L）。
* 请阅读并熟悉特性GWFD-021312 Single IP。
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
          minLength: 0
          maxLength: 31
          required: true
          description: '逻辑接口的VPN一定要与其对应的外联口的VPN相同，否则从逻辑接口发出去的报文会查询路由失败。'
          data_source: '参见“5G Core LLD文档 > 业务IP对接设计 > VRF”。  请选中“虚拟机类型”为“ISU”/“ISU\_Cxx”且“子端口”为“group\_isu\_xxxx”的所有行，查找指定“逻辑接口”对应的“VRF”。  已配置数据中获取'
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
          description: 'N9c、S5/S8-S接口可独立配置，也可使用抽象接口Sc进行合一配置（推荐使用合一配置）。两种方式不可同时配置，如已配置独立接口，则配置抽象接口时系统会提示失败；如已配置抽象接口，则配置独立接口时系统会提示失败。  最后一位数字取值范围是0~31。'
          data_source: '参见“5G Core LLD文档 > 业务IP对接设计 > 逻辑接口”。  本端规划'
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
          data_source: '参见“5G Core LLD文档 > 业务IP对接设计 > 逻辑接口IP”。  全网规划'
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
          data_source: '参见“5G Core LLD文档 > 业务IP对接设计 > VRF”。  请选中“虚拟机类型”为“ISU”/“ISU\_Cxx”且“子端口”为“group\_isu\_xxxx”的所有行，查找指定“逻辑接口”对应的“VRF”。  已配置数据中获取'
          pattern: ''
          default: ''
  examples:
    add_vpninst_list:
    - VPNINSTANCE: 'VPN_Sc'
    add_logicinf_list:
    - NAME: 'Scif1/1/0'
      IPVERSION: IPV4
      IPV4ADDRESS1: '10.1.1.2'
      IPV4MASK1: '255.255.255.255'
      VPNINSTANCE: 'VPN_Sc'
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 进入“MML命令行-UEG”窗口。

### 2 配置Sc/N9c/S5-S/S8-S逻辑接口所属的VPN实例。

```jinja2
{%- for item in add_vpninst_list -%}
    ADD VPNINST:
    {#- --- 必选参数 --- -#}
    VPNINSTANCE="{{item.VPNINSTANCE}}",
    ;
{%- endfor -%}
```

### 逻辑接口的VPN一定要与其对应的外联口的VPN相同，否则从逻辑接口发出去的报文会查询路由失败。

### 3 配置Sc/N9c/S5-S/S8-S逻辑接口。

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

### UEG支持N9c、S5/S8-S接口独立配置，也支持使用抽象接口Sc进行合一配置（推荐使用合一配置），两种方式不可同时配置，配置第二种方式时系统会提示失败。


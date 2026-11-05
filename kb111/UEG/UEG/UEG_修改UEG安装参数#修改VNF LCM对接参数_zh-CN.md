---
id: ''
name: 修改VNF LCM对接参数
ne_type: UEG
type: feature
description: 场景一：VNF采用VNF LCM安装，然后安装VNFM Agent。此时要将VNF对接到VNFM Agent，参考本文操作。  场景二：已预安装VNF和VNFM Agent。当设备上电后，VNFM Agent和中心侧管理面 VNF LCM对接，VNF LCM会将VNF LCM的IP地址自动传递给VNFM Agent，VNFM Agent将VNF LCM的IP地址传递给VNF。此过程无需人工操作。仅当VNFM Agent自动传递给VNF的流程故障时，才需要参考本文将VNF对接到VNFM Agent。
tags: []
risk_level: ''
doc_source:
  - ["网络部署","园区入驻式（仅连接）","5GC toB 部署边缘站点（站点为“风筝M”，入驻式）","UEG软件安装（风筝M）","基于生产预安装UEG（虚机容器）","修改UEG安装参数","修改VNF LCM对接参数"]
  - ["网络部署","园区入驻+地市共享（连接+计算）","5GC toB 部署边缘站点（站点为“风筝M”，带计算）","UEG软件安装（风筝M）","安装UPF（独立部署）","基于生产预安装UEG（虚机容器）","修改UEG安装参数","修改VNF LCM对接参数"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
场景一：VNF采用VNF LCM安装，然后安装VNFM Agent。此时要将VNF对接到VNFM Agent，参考本文操作。场景二：已预安装VNF和VNFM Agent。当设备上电后，VNFM Agent和中心侧管理面 VNF LCM对接，VNF LCM会将VNF LCM的IP地址自动传递给VNFM Agent，VNFM Agent将VNF LCM的IP地址传递给VNF。此过程无需人工操作。仅当VNFM Agent自动传递给VNF的流程故障时，才需要参考本文将VNF对接到VNFM Agent。

## 必备事项
前提条件

* 已经完成硬件设备安装和相关网络配置。

* 已经确认现场网络规划的网元对接MAE-VNF LCM/U2020 VNF LCM帐户信息与VNF生产预安装的预设参数值不同。

* 已经修改VNF LCM Agent的IP地址为局方的规划值。

* 已经完成配置调测PC与OMU操作维护IP互通，确保调测使用的PC与VNF OMU操作维护IP可以正常通信。

* 已通过MAE或UEG OMPortal登录华为操作维护系统。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    mod_vnfminfo_list:
      type: items
      properties:
        MASTERIP:
          name: '主节点IP'
          type: string
          maxLength: 80
          required: true
          description: 'UEG上的命令：  **MOD VNFMINFO**'
          data_source: '对端获取'
          pattern: ''
          default: ''
        USER:
          name: '用户名'
          type: string
          maxLength: 60
          required: true
          description: ''
          data_source: '对端获取'
          pattern: ''
          default: ''
        PWD:
          name: '密码'
          type: string
          minLength: 6
          maxLength: 32
          required: true
          description: ''
          data_source: '对端获取'
          pattern: ''
          default: ''
        SLAVEIP:
          name: '备节点IP'
          type: string
          maxLength: 80
          required: false
          description: ''
          data_source: '对端获取'
          pattern: ''
          default: ''
    mod_vnfminfo_list_1:
      type: items
      properties:
        MASTERIP:
          name: '主节点IP'
          type: string
          maxLength: 80
          required: true
          description: 'UEG上的命令：  **MOD VNFMINFO**'
          data_source: '对端获取'
          pattern: ''
          default: ''
        USER:
          name: '用户名'
          type: string
          maxLength: 60
          required: true
          description: ''
          data_source: '对端获取'
          pattern: ''
          default: ''
        PWD:
          name: '密码'
          type: string
          minLength: 6
          maxLength: 32
          required: true
          description: ''
          data_source: '对端获取'
          pattern: ''
          default: ''
  examples:
    mod_vnfminfo_list:
    - MASTERIP: '10.10.10.10'
      USER: 'nerestuser'
      PWD: '******'
      SLAVEIP: '空白，不用填写。'
    mod_vnfminfo_list_1:
    - MASTERIP: '10.10.10.10'
      USER: 'user'
      PWD: '******'
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 登录UEG OMPortal，选择“应用管理 > MML”。

### 2 进入“MML命令行-UEG”窗口。

### 3 修改MAE-VNF LCM/U2020 VNF LCM对接信息。

```jinja2
{%- for item in mod_vnfminfo_list -%}
    MOD VNFMINFO:
    {#- --- 必选参数 --- -#}
    MASTERIP="{{item.MASTERIP}}",
    USER="{{item.USER}}",
    PWD="{{item.PWD}}",
    {#- --- 可选参数 --- -#}
    {%- if item.SLAVEIP is not none -%}
        SLAVEIP="{{item.SLAVEIP}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### **任务描述**

### 修改MAE-VNF LCM/U2020 VNF LCM对接参数。

### **脚本**

### 修改MAE-VNF LCM/U2020 VNF LCM对接参数。

```jinja2
{%- for item in mod_vnfminfo_list_1 -%}
    MOD VNFMINFO:
    {#- --- 必选参数 --- -#}
    MASTERIP="{{item.MASTERIP}}",
    USER="{{item.USER}}",
    PWD="{{item.PWD}}",
    ;
{%- endfor -%}
```


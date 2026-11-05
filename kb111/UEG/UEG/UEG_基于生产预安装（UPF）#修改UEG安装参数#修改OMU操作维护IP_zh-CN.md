---
id: ''
name: 修改OMU操作维护IP
ne_type: UEG
type: feature
description: 如果生产发货时VNF已做过预安装，基于现场的网络规划，需要调整OMU操作维护管理接口IP（即OMU浮动IP）。  UEG上OMU的操作维护IP需要与OSS(MAE)上配置的该IP信息一致，如果修改了UEG的OMU操作维护IP，需要在OSS(MAE)上同步修改该IP地址参数。
tags: []
risk_level: ''
doc_source:
  - ["网络部署","园区入驻式（仅连接）","5GC toB 部署边缘站点（站点为“风筝S”，入驻式）","虚机容器模式","UEG软件安装（风筝S）","基于生产预安装（UPF）","修改UEG安装参数","修改OMU操作维护IP"]
  - ["网络部署","地市共享式（仅连接）","5GC toB 部署边缘站点（站点为“风筝S”，共享式）","UEG软件安装（风筝S）","基于生产预安装（UPF）","修改UEG安装参数","修改OMU操作维护IP"]
  - ["网络部署","园区入驻+地市共享（连接+计算）","5GC toB 部署边缘站点（站点为“风筝S”，带计算）","UEG软件安装（风筝S）","安装UPF（独立部署）","基于生产预安装（UPF）","修改UEG安装参数","修改OMU操作维护IP"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
如果生产发货时VNF已做过预安装，基于现场的网络规划，需要调整OMU操作维护管理接口IP（即OMU浮动IP）。UEG上OMU的操作维护IP需要与OSS(MAE)上配置的该IP信息一致，如果修改了UEG的OMU操作维护IP，需要在OSS(MAE)上同步修改该IP地址参数。

## 必备事项
前提条件

* 已经确认现场网络规划的OMU操作维护IP（MNG\_IP）与VNF生产预安装的预设参数值不同。
* 已经完成配置调测PC与OMU操作维护IP互通，确保调测使用的PC与VNF OMU操作维护IP可以正常通信。
* 已通过OSS(MAE)或UEG OMPortal登录华为操作维护系统。本文以UEG OMPortal为例说明调整过程。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    mod_virtualip_list:
      type: items
      properties:
        IPTYPE:
          name: '浮动IP类型'
          type: string
          enum:
          - IPv4
          - IPv6
          required: true
          description: 'UEG上的命令：  **MOD VIRTUALIP**'
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPV4ADDR:
          name: 'IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPV4GW:
          name: 'IPv4网关'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        NETMASK:
          name: '子网掩码'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
  examples:
    mod_virtualip_list:
    - IPTYPE: IPv4(IPv4)
      IPV4ADDR: '10.145.27.7'
      IPV4GW: '10.145.27.1'
      NETMASK: '255.255.255.0'
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 登录UEG OMPortal。在浏览器地址栏中输入https://UEG的OMU操作维护IP地址:31943/，后按回车键。

### 首次登录使用的UEG的OMU操作维护IP地址的出厂安装值。

### 由华为员工登录网站https://humep.huawei.com/ipreinstall/report，输入合同号，从LLD文档中的“账号管理设计”获取出厂安装值。

### 请参见《UEG安全配置》，对系统进行安全配置，修改系统默认帐号密码。

### **任务描述**

### **脚本**

### 登录UEG OMPortal。

### 2 进入“MML命令行-UEG”窗口。

### 3 修改OMU操作维护管理接口IP。

```jinja2
{%- for item in mod_virtualip_list -%}
    MOD VIRTUALIP:
    {#- --- 必选参数 --- -#}
    IPTYPE={{item.IPTYPE}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPTYPE=IPv4 时必选 --- -#}
    {%- if item.IPTYPE == 'IPv4' -%}
        IPV4ADDR="{{item.IPV4ADDR}}",
    {%- endif -%}
    {#- --- 条件必选：IPTYPE=IPv4 时必选 --- -#}
    {%- if item.IPTYPE == 'IPv4' -%}
        IPV4GW="{{item.IPV4GW}}",
    {%- endif -%}
    {#- --- 条件必选：IPTYPE=IPv4 时必选 --- -#}
    {%- if item.IPTYPE == 'IPv4' -%}
        NETMASK="{{item.NETMASK}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 执行该命令会导致OSS(MAE)或UEG OMPortal的连接中断。

### 此时需要调整本地PC IP，与新的UEG的OMU操作维护IP正常通信后，再重新登录UEG OMPortal。

### 对于同网段IP，可以使用MOD VIRTUALIP/SET OMIP修改OM IP；对于不同网段的OM IP调整，请联系华为技术支持工程师处理或参考《修改OMU IP指导书》。

### 修改OMU操作维护IP。

### 4 修改MAE-VNF LCM/U2020 VNF LCM中的VNFD模板。

#### 4.1 登录MAE-VNF LCM/U2020 VNF LCM，在MAE主界面的“应用”区域，单击“VNF-LCM”，进入MAE-VNF LCM主界面。在主菜单中选择“VNF生命周期管理 > VNF总览 ”。

#### 4.2 在“VNF总览”页面中，单击VNF“操作”列的，手动更新VNFD。

#### 4.3 在参数输入区域修改VNFD参数，例如“**浮动IP**(MNG\_IP)、**网关**(MNG\_GWIP)、**子网掩码**(MNG\_Netmask)”。

#### 4.4 单击“确定”。

#### 4.5 在弹出的高危提示对话框中，勾选“我已明确该操作的风险。”，单击“确定”。

### 5 登录OSS(MAE)客户端。

### 登录OSS(MAE)业务面客户端。

#### 5.1 在浏览器地址栏中输入**https://OSS(MAE)业务的IP地址:端口号/**，按回车键，弹出OSS(MAE)客户端界面。

#### 5.2 输入用户名和密码。

#### 默认用户名和密码是“admin/Changeme\_123”，如果已被修改，请使用新设置的用户名和密码。

#### 5.3 单击“登录”。

### 6 修改OSS(MAE)上配置的UEG OMU操作维护IP。

### 请参见MAE产品文档，操作与维护 > MAE-Access操作与维护 > 拓扑管理 > 维护拓扑对象 > 修改拓扑对象。


---
id: ''
name: 修改网元名称
ne_type: UEG
type: feature
description: 如果生产发货时VNF已做过预安装，发货到一线设备上电后，一线工程师要修改网元名称为实际现网的值。
tags: []
risk_level: ''
doc_source:
  - ["网络部署","园区入驻式（仅连接）","5GC toB 部署边缘站点（站点为“风筝S”，入驻式）","虚机容器模式","UEG软件安装（风筝S）","基于生产预安装（UPF）","修改UEG安装参数","修改网元名称"]
  - ["网络部署","地市共享式（仅连接）","5GC toB 部署边缘站点（站点为“风筝S”，共享式）","UEG软件安装（风筝S）","基于生产预安装（UPF）","修改UEG安装参数","修改网元名称"]
  - ["网络部署","园区入驻+地市共享（连接+计算）","5GC toB 部署边缘站点（站点为“风筝S”，带计算）","UEG软件安装（风筝S）","安装UPF（独立部署）","基于生产预安装（UPF）","修改UEG安装参数","修改网元名称"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
如果生产发货时VNF已做过预安装，发货到一线设备上电后，一线工程师要修改网元名称为实际现网的值。

## 必备事项
前提条件

* 已经确认现场网络规划的网元名称与UEG生产预安装的预设参数值不同。
* 已通过OSS(MAE)或UEG OMPortal登录华为操作维护系统。本文以UEG OMPortal为例说明调整过程。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    mod_me_list:
      type: items
      properties:
        MEID:
          name: '网元ID'
          type: integer
          minimum: 0
          maximum: 65535
          required: true
          description: 'UEG上的命令：  **MOD ME**'
          data_source: '本端规划'
          pattern: ''
          default: ''
        MELN:
          name: '网元本地名称'
          type: string
          maxLength: 80
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        MENAME:
          name: '网元名称'
          type: string
          maxLength: 64
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
  examples:
    mod_me_list:
    - MEID: 20
      MELN: 'UEGABC'
      MENAME: 'UEG123'
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 登录UEG OMPortal，选择“应用管理 > MML”。

### 2 进入“MML命令行-UEG”窗口。

### 3 修改网元名称。

```jinja2
{%- for item in mod_me_list -%}
    MOD ME:
    {#- --- 必选参数 --- -#}
    MEID={{item.MEID}},
    {#- --- 可选参数 --- -#}
    {%- if item.MELN is not none -%}
        MELN="{{item.MELN}}",
    {%- endif -%}
    {%- if item.MENAME is not none -%}
        MENAME="{{item.MENAME}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 修改MAE-VNF LCM/U2020 VNF LCM中的VNFD模板。

#### 4.1 登录MAE-VNF LCM/U2020 VNF LCM，在MAE主界面的“应用”区域，单击“VNF-LCM”，进入MAE-VNF LCM主界面。在主菜单中选择“VNF生命周期管理 > VNF总览 ”。

#### 4.2 在“VNF总览”页面中，单击VNF“操作”列的，手动更新VNFD。

#### 4.3 在参数输入区域修改VNFD参数，例如“VNF\_Name”。

#### 4.4 单击“确定”。

#### 4.5 在弹出的高危提示对话框中，勾选“我已明确该操作的风险。”，单击“确定”。

### **任务描述**

### **脚本**


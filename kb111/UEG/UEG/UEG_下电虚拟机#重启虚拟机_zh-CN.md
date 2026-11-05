---
id: ''
name: 重启虚拟机
ne_type: UEG
type: feature
description: 当需要通过重启虚拟机进行业务恢复时，可以参考本章节进行操作。  重启虚拟机可以通过在MANO上选择“VNF生命周期管理 > 自愈管理 > VNF自愈”，单击“重启”，进行操作。也可以通过在网元OM Portal上执行MML，本章节主要介绍在网元OM Portal上进行重启的操作。  扩展域不支持该功能。
tags: []
risk_level: ''
doc_source: ["日常维护","UEG 基础运维操作（风筝S，虚机容器）","下电虚拟机","重启虚拟机"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
当需要通过重启虚拟机进行业务恢复时，可以参考本章节进行操作。重启虚拟机可以通过在MANO上选择“VNF生命周期管理 > 自愈管理 > VNF自愈”，单击“重启”，进行操作。也可以通过在网元OM Portal上执行MML，本章节主要介绍在网元OM Portal上进行重启的操作。扩展域不支持该功能。

## 必备事项
前提条件

已登录OM Portal。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    rst_node_list:
      type: items
      properties:
        APPID:
          name: '网元ID'
          type: integer
          minimum: 0
          maximum: 65535
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NODENAME:
          name: '节点名称'
          type: string
          maxLength: 128
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RESETTYPE:
          name: '复位类型'
          type: string
          enum:
          - soft
          - hard
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    rst_node_list:
    - APPID: 0
      NODENAME: '192.168.101.179'
      RESETTYPE: soft
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 选择“应用管理 > MML”。

### 2 执行**DSP NODE**，查看待复位虚拟机的“节点名称”，示例如下。

### RETCODE = 0  操作成功

### 操作结果如下

### ------------

### 网元ID  节点名称         节点IP           虚拟机名称                 主机名称     运行状态  管理状态

### 0       192.168.101.236  192.168.101.236  zcyuyu_ch_v4_0316_CSP_C_0  M107-Slot11  Normal    Active

### 0       192.168.101.171  192.168.101.171  zcyuyu_ch_v4_0316_CSP_A_0  M107-Slot2   Normal    Active

### 0       192.168.101.179  192.168.101.179  zcyuyu_ch_v4_0316_CSP_B_0  M107-Slot5   Normal    Active

### (结果个数 = 3)

### 3 执行**RST NODE**，输入待重启虚拟机对应的“节点名称”，“复位类型”选择“软复位”，示例如下。

```jinja2
{%- for item in rst_node_list -%}
    RST NODE:
    {#- --- 必选参数 --- -#}
    APPID={{item.APPID}},
    NODENAME="{{item.NODENAME}}",
    RESETTYPE={{item.RESETTYPE}},
    ;
{%- endfor -%}
```

### 如果需要批量重启虚拟机，可以执行**RST NODEBATCH**，复位网元下的所有节点。

### 如果需要复位某个Pod，可以执行**RST POD**。


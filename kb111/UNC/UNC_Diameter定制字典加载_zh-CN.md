---
id: ''
name: Diameter定制字典加载
ne_type: UNC
type: feature
description: 当系统启动后，Diameter接口应用会自动加载一套标准字典。如果用户有定制规范的需要，而现有标准Diameter字典无法满足定制需求，则需要通过定制字典方式进行适配。  该章节主要介绍定制字典文件的加载方式。若不需要加载定制字典，请跳过本章节。
risk_level: ''
doc_source: ["网络部署","业务专题","5G Core 一跳入家解决方案","一跳入家解决方案（基于非3GPP接入方案）","业务初始部署与调测","部署一跳入家","配置一跳入家专网UPF","Diameter定制字典加载"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
当系统启动后，Diameter接口应用会自动加载一套标准字典。如果用户有定制规范的需要，而现有标准Diameter字典无法满足定制需求，则需要通过定制字典方式进行适配。该章节主要介绍定制字典文件的加载方式。若不需要加载定制字典，请跳过本章节。

## 必备事项
前提条件

前提条件

* UPF软件安装已完成。
* UPF初始配置已完成。
* 已完成一跳入家依赖功能的License加载。
* 已联系华为技术工程师获取定制字典文件。”
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    mod_updiamdictpath_list:
      type: items
      properties:
        APPLICATION:
          name: '应用'
          type: string
          required: false
          description: '该参数用于指定字典的Diameter应用。固定为SWM。'
          data_source: '固定值'
          pattern: ''
          default: ''
        DICTNO:
          name: '字典序号'
          type: string
          required: false
          description: '该参数用于指定字典编号。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        DICTPATH:
          name: '字典加载路径'
          type: string
          required: false
          description: '该参数用于指定字典加载路径。CUSTOM1是指定制字典路径。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    lod_updiamdict_list:
      type: items
      properties:
        DICTFILESELECT:
          name: '字典文件选择'
          type: string
          required: false
          description: '该参数用于指定Diameter字典类型。'
          data_source: '本端规划'
          pattern: ''
          default: ''
  examples:
    mod_updiamdictpath_list:
    - APPLICATION: SWM
      DICTNO: '1'
      DICTPATH: CUSTOM1
    lod_updiamdict_list:
    - DICTFILESELECT: ALL
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 OM Portal上传定制字典文件。

### 将定制字典文件custom\_signed.zip，上传到OM Portal界面中的“系统 -> 文件传输 -> Diameter字典 Custom”路径下。

### **图1** 定制字典文件目录

### **图2** OM Portal上传定制字典文件

### 2 修改定制字典路径。

### 在“MML命令行 - UDG”窗口上执行**MOD UPDIAMDICTPATH**命令将SWm应用的字典设置为“CUSTOM1”。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该mod_updiamdictpath_list的变量区（command: MOD UPDIAMDICTPATH） -#}
<!-- MISSING_MACRO: command=MOD UPDIAMDICTPATH list_name=mod_updiamdictpath_list step_id=2 -->
```

### 3 加载字典文件。

### 执行**LOD UPDIAMDICT**命令，加载SWm应用配置的定制字典路径下的Diameter字典文件。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该lod_updiamdict_list的变量区（command: LOD UPDIAMDICT） -#}
<!-- MISSING_MACRO: command=LOD UPDIAMDICT list_name=lod_updiamdict_list step_id=3 -->
```

### 4 查看字典加载路径和字典加载状态。

### 执行**LOD UPDIAMDICT**命令后，等待10-20秒，执行**DSP UPDIAMDICTSTAT**命令查看字典加载路径和字典加载状态。


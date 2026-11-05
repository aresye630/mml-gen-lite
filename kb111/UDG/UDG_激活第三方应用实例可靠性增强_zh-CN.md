---
id: ''
name: 激活第三方应用实例可靠性增强
ne_type: UDG
type: feature
description: 当运营商为保障终端用户更好的享受增值业务时，会根据检测周期定时对第三方app进行故障检测，开启激活第三方实例可靠性增强功能。
risk_level: ''
doc_source: ["特性部署","业务专题","UDG SFIP功能专题","功能描述","第三方应用实例可靠性增强","激活第三方应用实例可靠性增强"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
当运营商为保障终端用户更好的享受增值业务时，会根据检测周期定时对第三方app进行故障检测，开启激活第三方实例可靠性增强功能。

## 必备事项
前提条件

* 请仔细阅读第三方应用实例可靠性增强。
* 已通过OM Portal登录“第三方应用操作维护入口”界面。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    set_licenseswitch_list:
      type: items
      properties:
        LICITEM:
          name: 'License项'
          type: string
          minLength: 0
          maxLength: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SWITCH:
          name: '开关'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV4RETAPP01'
      SWITCH: ENABLE
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 在“MML命令行 - UDG”窗口上执行**SET LICENSESWITCH**打开license开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

### 2 在“第三方应用操作维护入口”界面，选择“操作管理 > 配置管理 > 应用健康检查”，进入“应用健康检查”的配置界面。

### 3 在“应用健康检查设置”区域框下面设置第三方实例可靠性增强功能。

#### 3.1 开启“应用健康检查”。

#### 按钮显示蓝色背景状态，表示第三方实例可靠性增强功能已开启。

#### 按钮显示白色背景状态，表示第三方实例可靠性增强功能已关闭。

#### 3.2 设置“健康检查周期”，参数范围为1~60s，默认值为2s。

### 4 （可选）当存在串接在业务链上的Server类型的app时，设置其健康检查功能：单击“APP健康检查服务配置”按钮。

#### 4.1 在弹出的“APP健康检查服务配置”页面，单击“添加”，在“VNF名称”列选择对应的VNF，“VDU名称”列选择对应VDU，“IP类型”列选择“ipv4”或者“ipv6”，“IP地址列”根据网络规划输入Server app对外提供服务的IP地址，“端口”列输入Server app对外提供服务的端口。

#### 4.2 单击“确定”，完成串接在业务链上的Server类型的app的健康检查功能的设置。

### 5 在“检查结果”区域框下面查询健康检查结果，查询结果可以根据VM名称和ID进行检索。激活的操作步骤如图1所示。

### **图1** 激活第三方app实例可靠性增强

### 6 在“第三方应用操作维护入口”界面，选择“操作管理 > 配置管理 > 配置”，进入“配置”的界面。双击“Unipath Check”下的“Unipath Check Switch”。将“Unipath Check Switch”设置为“ON”，激活app单通检测，如图2所示。App单通检测其它参数的配置请参见参数说明：单通检测配置。

### **图2** 激活app单通检测


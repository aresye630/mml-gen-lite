---
id: ''
name: 配置向第三方app开放用户信息服务
ne_type: UDG
type: feature
description: 当用户信息发生变化时，SFIP为了及时获取最新用户信息并为第三方app提供用户信息开放服务，需要配置订阅用户信息后发送给第三方app。
risk_level: ''
doc_source: ["特性部署","业务专题","UDG SFIP功能专题","安装部署","部署后数据配置","配置向第三方app开放用户信息服务"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
当用户信息发生变化时，SFIP为了及时获取最新用户信息并为第三方app提供用户信息开放服务，需要配置订阅用户信息后发送给第三方app。

## 必备事项
前提条件

* 已登录“OM Portal”。
* 已登录MAE。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    set_rptratelt_list:
      type: items
      properties:
        SSGUSRRSDSW:
          name: 'SSG主动定时重发用户信息功能开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '通过**SET RPTRATELT**命令打开UDG主动定时重发用户信息功能开关。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SSGUSRRSDPERIOD:
          name: 'SSG主动定时重发用户信息时间间隔'
          type: integer
          minimum: 300
          maximum: 86400
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    set_rptratelt_list:
    - SSGUSRRSDSW: ENABLE
      SSGUSRRSDPERIOD: ''
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 配置FG和APN的关联。

#### 1.1 登录OM Portal，依次单击“应用管理 > 第三方应用操作维护入口 > 业务链”，弹出“业务链”窗口。

#### 1.2 单击左侧目录“APN”。

#### 1.3 单击“创建APN”，弹出“创建APN”界面。

#### 1.4 输入“APN名称”,根据网络规划，选择需要获取用户信息的“FG名称”。

### “APN名称”需与上业务链的第三方app所接入的APN保持一致。

#### 1.5 单击“确定”，完成FG和APN的关联配置。

### **图1** 配置FG与APN的关联关系

### 2 配置“carbon-copy mode shared secret”。

#### 2.1 在“第三方应用操作维护入口”界面，单击“操作管理”，进入“操作管理”界面。

#### 2.2 单击左侧“配置管理 > 配置”，进入“配置”界面。

#### 2.3 单击“Carbon Copy Mode Shared Secret”，显示“Carbon Copy Mode Shared Secret”内容，如图2所示。详细参数配置参见参数说明：设置Radius抄送模式共享密钥。

### **图2** Carbon Copy Mode Shared Secret

#### 2.4 双击“Carbon Copy Mode Shared Secret”弹出配置对话框，输入“共享密钥”，单击“确定”，完成配置。如图3所示。完成后，“配置”界面“Value”显示输入的共享密钥。

### **图3** 配置“Carbon Copy Mode Shared Secret”

### 3 查询获取uis-pod的IP地址提供给第三方app，供第三方app与SFIP对接时使用。

### uis-pod的IP地址可根据解析TOSCA模板中已配置的UIS起始IP地址+pod id进行计算获取。如图4所示，UIS起始IP地址即“UIS\_LOCAL\_IP\_SRART”为“192.168.22.191”，按照uis的pod-Id依次加1后即为uis-pod的IP地址：

### uis-pod-0的IP地址：192.168.22.191

### uis-pod-1的IP地址：192.168.22.192

### uis-pod-2的IP地址：192.168.22.193

### ……省略号以此类推

### **图4** 查询UIS起始IP地址示意图

### 解析VNFD压缩包后即可获取TOSCA模板，VNFD模板包请从路径： 技术支持 > 产品软件 > 云核心网 > Mobile Packet Core > CloudMSE > CloudMSE > CloudEPSN > CloudEPSN VxxxRxxxCxx下获取。

### 4 在“MML命令行 - UDG”窗口上执行**SET RPTRATELT**打开UDG主动定时重发用户信息功能开关。

```jinja2
{%- for item in set_rptratelt_list -%}
    SET RPTRATELT:
    {#- --- 可选参数 --- -#}
    {%- if item.SSGUSRRSDSW is not none -%}
        SSGUSRRSDSW={{item.SSGUSRRSDSW}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：SSGUSRRSDSW=ENABLE 时可选 --- -#}
    {%- if item.SSGUSRRSDSW == 'ENABLE' -%}
        {%- if item.SSGUSRRSDPERIOD is not none -%}
            SSGUSRRSDPERIOD={{item.SSGUSRRSDPERIOD}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```


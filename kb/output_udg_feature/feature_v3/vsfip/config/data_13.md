# 配置向第三方app开放用户信息服务

* 操作场景
* 必备事项
* 操作步骤

## 操作场景

当用户信息发生变化时，SFIP为了及时获取最新用户信息并为第三方app提供用户信息开放服务，需要配置订阅用户信息后发送给第三方app。

## 必备事项

前提条件

* 已登录“OM Portal”。
* 已登录MAE。

数据

| 参数名称/包名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- |
| APN名称 | 3gwap | 已配置数据中获取 | 通过在“第三方应用操作维护入口”界面配置。  与**ADD APN**命令中配置的“APN名称”参数值保持一致 |
| FG名称 | FG1 | 已配置数据中获取 | 通过在“第三方应用操作维护入口”界面配置。  根据网络规划，配置需要获取用户信息的FG。 |
| SSG主动定时重发用户信息功能开关（SSGUSRRSDSW） | ENABLE | 本端规划 | 通过**SET RPTRATELT**命令打开UDG主动定时重发用户信息功能开关。 |
| 用户信息扩展包 | 5G-UP-VASs-CloudEPSN-SFIP\_UserInfoPlg\_VxxxRxxxCxx\_PLUGIN\_ARM.zip | Support上获取 | 登录https://support.huawei.com，进入“技术支持 > 产品软件 > 云核心网 > Mobile Packet Core > CloudMSE > CloudMSE > 5G UP VASs”路径选择所需版本号后下载5G-UP-VASs-CloudEPSN-SFIP\_UserInfoPlg\_VxxxRxxxCxx\_PLUGIN\_ARM.zip插件包，或直接搜索关键字“UserInfoPlg”进行查找下载。 |

## 操作步骤

1. 配置FG和APN的关联。
   1. 登录OM Portal，依次单击“应用管理 > 第三方应用操作维护入口 > 业务链”，弹出“业务链”窗口。
   2. 单击左侧目录“APN”。
   3. 单击“创建APN”，弹出“创建APN”界面。
   4. 输入“APN名称”,根据网络规划，选择需要获取用户信息的“FG名称”。

      “APN名称”需与上业务链的第三方app所接入的APN保持一致。
   5. 单击“确定”，完成FG和APN的关联配置。

   **图1** 配置FG与APN的关联关系
2. 配置“carbon-copy mode shared secret”。
   1. 在“第三方应用操作维护入口”界面，单击“操作管理”，进入“操作管理”界面。
   2. 单击左侧“配置管理 > 配置”，进入“配置”界面。
   3. 单击“Carbon Copy Mode Shared Secret”，显示“Carbon Copy Mode Shared Secret”内容，如图2所示。详细参数配置参见参数说明：设置Radius抄送模式共享密钥。

      **图2** Carbon Copy Mode Shared Secret
   4. 双击“Carbon Copy Mode Shared Secret”弹出配置对话框，输入“共享密钥”，单击“确定”，完成配置。如图3所示。完成后，“配置”界面“Value”显示输入的共享密钥。

      **图3** 配置“Carbon Copy Mode Shared Secret”
3. 查询获取uis-pod的IP地址提供给第三方app，供第三方app与SFIP对接时使用。

   uis-pod的IP地址可根据解析TOSCA模板中已配置的UIS起始IP地址+pod id进行计算获取。如图4所示，UIS起始IP地址即“UIS\_LOCAL\_IP\_SRART”为“192.168.22.191”，按照uis的pod-Id依次加1后即为uis-pod的IP地址：

   uis-pod-0的IP地址：192.168.22.191

   uis-pod-1的IP地址：192.168.22.192

   uis-pod-2的IP地址：192.168.22.193

   ……省略号以此类推

   **图4** 查询UIS起始IP地址示意图

   解析VNFD压缩包后即可获取TOSCA模板，VNFD模板包请从路径： 技术支持 > 产品软件 > 云核心网 > Mobile Packet Core > CloudMSE > CloudMSE > CloudEPSN > CloudEPSN VxxxRxxxCxx下获取。
4. 在“MML命令行 - UDG”窗口上执行**SET RPTRATELT**打开UDG主动定时重发用户信息功能开关。

   **SET RPTRATELT**: SSGUSRRSDSW=ENABLE;

版权所有 © 华为技术有限公司

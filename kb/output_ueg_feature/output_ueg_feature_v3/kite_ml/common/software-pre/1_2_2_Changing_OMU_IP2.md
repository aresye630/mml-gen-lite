# 修改OMU操作维护IP

* 操作场景
* 必备事项
* 操作步骤
* 任务实例

#### 操作场景

如果生产发货时VNF已做过预安装，基于现场的网络规划，需要调整OMU操作维护管理接口IP（即OMU浮动IP）。

UEG上OMU的操作维护IP需要与OSS(MAE)上配置的该IP信息一致，如果修改了UEG的OMU操作维护IP，需要在OSS(MAE)上同步修改该IP地址参数。

#### 必备事项

**前提条件**

* 已经确认现场网络规划的OMU操作维护IP（MNG\_IP）与VNF生产预安装的预设参数值不同。
* 已经完成配置调测PC与OMU操作维护IP互通，确保调测使用的PC与VNF OMU操作维护IP可以正常通信。
* 已通过OSS(MAE)或UEG OMPortal登录华为操作维护系统。本文以UEG OMPortal为例说明调整过程。

**数据**

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| UEG操作维护接口信息 | 浮动IP类型（IPTYPE） | IPv4(IPv4) | 本端规划 | UEG上的命令：  **MOD VIRTUALIP** |
|  | IPv4地址（IPV4ADDR） | 10.145.27.7 | 本端规划 |  |
|  | IPv4网关（IPV4GW） | 10.145.27.1 | 本端规划 |  |
|  | 子网掩码（NETMASK） | 255.255.255.0 | 本端规划 |  |
| OSS(MAE)客户端账号信息 | 用户名 | admin | 对端获取 | 默认用户名和密码分别是“admin”和“Changeme\_123”。 |
|  | 密码 | Changeme\_123 | 对端获取 |  |
|  | 业务IP地址 | 10.50.12.104 | 对端获取 |  |
|  | 端口号 | 31943 | 对端获取 |  |

#### 操作步骤

1. 登录UEG OMPortal。在浏览器地址栏中输入https://UEG的OMU操作维护IP地址:31943/，后按回车键。

   首次登录使用的UEG的OMU操作维护IP地址的出厂安装值。

   由华为员工登录网站https://humep.huawei.com/ipreinstall/report，输入合同号，从LLD文档中的“账号管理设计”获取出厂安装值。

   请参见《UEG安全配置》，对系统进行安全配置，修改系统默认帐号密码。
2. 进入“MML命令行-UEG”窗口。
3. 修改OMU操作维护管理接口IP。

   ```
   MOD VIRTUALIP: IPTYPE=IPv4(IPv4), IPV4ADDR="10.145.27.7", IPV4GW="10.145.27.1", NETMASK="255.255.255.0";
   ```

   执行该命令会导致OSS(MAE)或UEG OMPortal的连接中断。

   此时需要调整本地PC IP，与新的UEG的OMU操作维护IP正常通信后，再重新登录UEG OMPortal。

   对于同网段IP，可以使用MOD VIRTUALIP/SET OMIP修改OM IP；对于不同网段的OM IP调整，请联系华为技术支持工程师处理或参考《修改OMU IP指导书》。
4. 修改MAE-VNF LCM/U2020 VNF LCM中的VNFD模板。
   1. 登录MAE-VNF LCM/U2020 VNF LCM，在MAE主界面的“应用”区域，单击“VNF-LCM”，进入MAE-VNF LCM主界面。在主菜单中选择“VNF生命周期管理 > VNF总览 ”。
   2. 在“VNF总览”页面中，单击VNF“操作”列的，手动更新VNFD。
   3. 在参数输入区域修改VNFD参数，例如“**浮动IP**(MNG\_IP)、**网关**(MNG\_GWIP)、**子网掩码**(MNG\_Netmask)”。
   4. 单击“确定”。
   5. 在弹出的高危提示对话框中，勾选“我已明确该操作的风险。”，单击“确定”。
5. 登录OSS(MAE)客户端。

   1. 在浏览器地址栏中输入**https://OSS(MAE)业务的IP地址:端口号/**，按回车键，弹出OSS(MAE)客户端界面。
   2. 输入用户名和密码。

      默认用户名和密码是“admin/Changeme\_123”，如果已被修改，请使用新设置的用户名和密码。
   3. 单击“登录”。
6. 修改OSS(MAE)上配置的UEG OMU操作维护IP。

   请参见MAE产品文档，操作与维护 > MAE-Access操作与维护 > 拓扑管理 > 维护拓扑对象 > 修改拓扑对象。

#### 任务实例

**任务描述**

修改OMU操作维护IP。

**脚本**

1. 登录UEG OMPortal。
2. 修改OMU操作维护IP。

   ```
   MOD VIRTUALIP: IPTYPE=IPv4(IPv4), IPV4ADDR="10.145.27.7", IPV4GW="10.145.27.1", NETMASK="255.255.255.0";
   ```
3. 修改MAE-VNF LCM/U2020 VNF LCM中的VNFD模板。
   1. 登录MAE-VNF LCM/U2020 VNF LCM，在MAE主界面的“应用”区域，单击“VNF-LCM”，进入MAE-VNF LCM主界面。在主菜单中选择“VNF生命周期管理 > VNF总览 ”。
   2. 在“VNF总览”页面中，单击VNF“操作”列的，手动更新VNFD。
   3. 在参数输入区域修改VNFD参数，例如“**浮动IP**(MNG\_IP)、**网关**(MNG\_GWIP)、**子网掩码**(MNG\_Netmask)”。
   4. 单击“确定”。
   5. 在弹出的高危提示对话框中，勾选“我已明确该操作的风险。”，单击“确定”。
4. 登录OSS(MAE)业务面客户端。

   请参见MAE产品文档，操作与维护 > MAE-Access操作与维护 > 拓扑管理 > 维护拓扑对象 > 修改拓扑对象。

版权所有 © 华为技术有限公司

# 激活支持Routing Behind MS（SGW-C/PGW-C/SMF）

- 操作场景
- 必备事项
- 操作步骤
- 任务示例

## 操作场景

当运营商需要开展移动VPN业务，使多台终端设备（PC）可以通过一个MS/UE接入PDN或Intranet网络，并使用独立的IP地址与网络侧设备进行双向数据业务时，需要激活UEG的Routing Behind MS功能。

**说明** 

适用于SGW-C、PGW-C、SMF。

## 必备事项

前提条件

- 请仔细阅读GWFD-024101 支持Routing Behind MS特性概述。
- 完成加载License。
- 本特性与UDG配合使用生效，请参考UDG中的**GWFD-110910 支持Routing Behind MS**。
- 如若本特性部署在新APN上，请参考章节配置会话管理参数完成APN信息配置。

数据

| 类别                   | 参数名称                     | 取值样例            | 获取方法     | 说明                                                                  |
|:---------------------|:-------------------------|:----------------|:---------|:--------------------------------------------------------------------|
| SET CPAPNADDRESSATTR | APN名称（APN）               | huawei.com      | 已配置数据中获取 | 规划使能Routing Behind MS功能的APN实例，已通过ADD CPAPN命令配置，可以使用LST CPAPN命令进行查询。 |
| SET CPAPNADDRESSATTR | 手机后路由（FRAMEDROUTE）       | ENABLE          | 本端规划     | 配置指定APN是否允许手机后路由用户接入。                                               |
| SET SMCOMMFUNC       | 手机后路由功能开关（RTBEHINDMSSW）  | ENABLE          | 本端规划     | 支持从本地配置中获取后路由。                                                      |
| ADD ROUTINGBEHINDMS  | 用户IMSI号（IMSI）            | 123000123456789 | 本端规划     | 本地配置手机后路由信息。AAA不返回后路由信息或未部署AAA服务器时，可使用本地配置的后路由信息。                   |
| ADD ROUTINGBEHINDMS  | APN名称（APN）               | huawei.com      | 本端规划     | 本地配置手机后路由信息。AAA不返回后路由信息或未部署AAA服务器时，可使用本地配置的后路由信息。                   |
| ADD ROUTINGBEHINDMS  | 后路由IPv4地址（FRAMEDROUTEIP） | 192.168.1.0     | 本端规划     | 本地配置手机后路由信息。AAA不返回后路由信息或未部署AAA服务器时，可使用本地配置的后路由信息。                   |
| ADD ROUTINGBEHINDMS  | 后路由掩码（FRAMEDROUTEMASK）   | 255.255.255.0   | 本端规划     | 本地配置手机后路由信息。AAA不返回后路由信息或未部署AAA服务器时，可使用本地配置的后路由信息。                   |

## 操作步骤

1. 进入“MML命令行-UEG”窗口。
2. 打开本特性的License开关。

   **SET LICENSESWITCH**
3. 使能该APN的Routing Behind MS功能。

   **SET CPAPNADDRESSATTR**

   **说明** 

   - 如果APN使能了L2TP功能，则无需开启Routing Behind MS功能。
   - 在功能开启前，需要在AAA Server上配置好分配给终端设备使用的IP地址段。
4. 支持从本地配置中获取后路由。

   **SET SMCOMMFUNC**
5. 本地配置手机后路由信息。AAA不返回后路由信息或未部署AAA服务器时，可使用本地配置的后路由信息。

   **ADD ROUTINGBEHINDMS**

## 任务示例

任务描述

使能APN“huawei.com”的Routing Behind MS功能。

脚本

//打开本特性的License配置开关。

```
SET LICENSESWITCH:LICITEM="LKV3W9RBMS12",SWITCH=ENABLE;
```

//使能该APN的Routing Behind MS功能。

```
SET CPAPNADDRESSATTR:APN="huawei.com",FRAMEDROUTE=ENABLE;
```

//支持从本地配置中获取后路由。

```
SET SMCOMMFUNC: RTBEHINDMSSW=ENABLE;
```

//本地配置手机后路由信息。

```
ADD ROUTINGBEHINDMS: IMSI="123000123456789", APN="huawei.com", FRAMEDROUTEIP="192.168.1.0", FRAMEDROUTEMASK="255.255.255.0";
```
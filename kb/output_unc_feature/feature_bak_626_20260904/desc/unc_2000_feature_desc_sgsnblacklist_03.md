# 激活SGSN的黑白名单

- 操作场景
- 必备事项
- 操作步骤
- 任务示例

## 操作场景

当需要对SGSN/MME/SGW-C进行接入控制时，激活SGSN的黑白名单。

**说明** 

适用于GGSN、SGW-C、PGW-C。

## 必备事项

前提条件

- 请仔细阅读WSFD-104509 SGSN的黑白名单特性概述。
- 完成加载License。

数据

| 类别                 | 参数名称                          | 取值样例      | 获取方法   | 说明                                                                               |
|:-------------------|:------------------------------|:----------|:-------|:---------------------------------------------------------------------------------|
| SET ACCESSLISTFUNC | 设置系统是否支持接入控制名单的功能（LISTSWITCH） | ENABLE    | 本端规划   | GGSN/PGW-C支持两种SGSN/MME/SGW-C接入的控制名单类型：BLACK：黑名单使能。 WHITE：白名单使能。 配置时只能根据需要选择一种名单。 |
| SET ACCESSLISTFUNC | 黑白名单类型（LISTTYPE）              | BLACK     | 本端规划   | 接入控制名单类型。                                                                        |
| ADD ACCESSLISTIP   | IP地址版本类型（IPVERSION）           | IPV4      | 本端规划   | 接入控制的SGSN/MME/SGW-C IP地址段。                                                       |
| ADD ACCESSLISTIP   | IPv4地址段的地址（SRVNODEIPV4）       | 10.20.0.2 | 本端规划   | 接入控制的SGSN/MME/SGW-C IP地址段。                                                       |
| ADD ACCESSLISTIP   | 掩码长度（SRVNODEIPV4MASK）         | 27        | 本端规划   | 接入控制的SGSN/MME/SGW-C IP地址段。                                                       |

## 操作步骤

1. 进入“MML命令行-UNC”窗口。
2. 打开本特性的License开关。

   **SET LICENSESWITCH**
3. 使能黑白名单控制开关并配置SGSN/MME/SGW-C接入控制名单类型。

   **SET ACCESSLISTFUNC**
4. 配置接入控制名单的SGSN/MME/SGW-C的IP地址段。

   **ADD ACCESSLISTIP**

## 任务示例

任务描述

根据运营商规划，需要禁止IP地址范围在10.20.0.2/27网段内的SGSN/MME/SGW-C接入。

脚本

//打开本特性的License配置开关。

```
SET LICENSESWITCH:LICITEM="LKV3W9SBWL11",SWITCH=ENABLE;
```

//使能黑白名单控制开关并配置接入控制名单类型为黑名单。

```
SET ACCESSLISTFUNC:LISTSWITCH=ENABLE,LISTTYPE=BLACK;
```

//配置接入控制名单的IP地址与掩码。

```
ADD ACCESSLISTIP:IPVERSION=IPV4,SRVNODEIPV4="10.20.0.2",SRVNODEIPV4MASK=27;
```
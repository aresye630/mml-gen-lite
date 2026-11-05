# 激活Radius鉴权接入

- 操作场景
- 必备事项
- 操作步骤
- 任务示例

## 操作场景

本操作指导介绍在运行网络中激活Radius鉴权接入特性的操作过程。

**说明** 

适用于GGSN、PGW-C、SMF。

## 必备事项

前提条件

- 请仔细阅读WSFD-011305 Radius鉴权接入特性概述。
- 已经完成配置普通DNN。

数据

| 类别              | 参数名称                    | 取值样例       | 获取方法   | 说明                                                                                                                                                                                                                                                        |
|:----------------|:------------------------|:-----------|:-------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SET APNAUTHATTR | 接入模式（ACCESSMODE）        | TRANS_AUTH | 本端规划   | 可选的接入模式包括： TRANS_AUTH（透明鉴权）：指定为透明并需要鉴权。这种鉴权方式对用户是透明的，不需要用户感知，鉴权使用的用户名和密码一般由UNC配置。 TRANS_NON_AUTH（透明不鉴权）：指定为透明不需要鉴权。这种接入方式不需要去RADIUS服务器鉴权。 NON_TRANS（不透明）：指定为不透明接入，需要鉴权。这种鉴权方式可以继续配置鉴权使用的用户名和密码。 LOC_AUTH（本地鉴权）：指定为本地鉴权。这种接入方式不需要去RADIUS服务器鉴权，通过UNC完成鉴权功能。 |
| SET APNAUTHATTR | 公用用户名（COMMONUSERNAME）   | huawei123  | 本端规划   | -                                                                                                                                                                                                                                                         |
| SET APNAUTHATTR | 公用密码（COMMONUSERPASS）    | 123        | 本端规划   | -                                                                                                                                                                                                                                                         |
| SET APNAUTHATTR | 确认公共密码（CFMCOMMUSERPASS） | 123        | 本端规划   | 该参数需要与“COMMONUSERPASS”保持一致。                                                                                                                                                                                                                               |
| SET APNAUTHATTR | APN名称（APN）              | huawei.com | 本端规划   | 已通过命令ADD APN 配置。                                                                                                                                                                                                                                          |

## 操作步骤

1. 进入“MML命令行-UNC”窗口。
2. 配置APN鉴权属性。

   **SET APNAUTHATTR**

## 任务示例

任务描述

配置APN为huawei.com的鉴权属性，接入模式为透明鉴权接入，公用的用户名和密码分别为huawei123和123。当用户以该APN接入时，UNC直接使用该APN下配置的公用的用户名和密码为用户的用户名和密码，到Radius服务器进行鉴权。

脚本

//配置APN鉴权属性。

```
SET APNAUTHATTR: APN="huawei.com", ACCESSMODE=TRANS_AUTH, COMMONUSERNAME="huawei123", COMMONUSERPASS="123", CFMCOMMUSERPASS="123";
```
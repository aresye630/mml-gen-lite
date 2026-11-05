# 激活鉴权功能（适用于5G）

- 操作场景
- 必备事项
- 操作步骤
- 任务示例

## 操作场景

对于建议强制鉴权的流程（包括初始注册、移动性INTER注册、空闲态EPS到5GS注册流程），系统默认开启鉴权功能。新建部署或运维阶段，可以执行本操作对所需流程开启强制鉴权功能，或者修改强制鉴权的流程。

**说明** 

适用于AMF。

## 必备事项

前提条件

请仔细阅读GWFD-021503 鉴权功能特性概述（适用于5G）。

数据

| 类别               | 参数名称    | 取值样例                                                                                                                                                                             | 获取方法   | 说明   |
|:-----------------|:--------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------|:-----|
| ADD NGUSRSECPARA | 用户范围    | ALL_USER                                                                                                                                                                         | 全网规划   | -    |
| ADD NGUSRSECPARA | 鉴权事件    | INIT_REG-1&MOBL_INTRA_REG-0&MOBL_INTER_REG-1&PROD_REG-0&REG_AFT_INTRAHO-0&REG_AFT_INTERHO-0&IDLE_SYSCHG_REG-1&CONN_SYSCHG_REG-0&DEREGISTRATION-0&SERVICE_REQUEST-0&CONNECT_MOD-0 | 全网规划   | -    |
| ADD NGUSRSECPARA | 鉴权周期(h) | 0                                                                                                                                                                                | 全网规划   | -    |

## 操作步骤

1. 进入“MML命令行-UEG”窗口。
2. 设置需要强制鉴权的流程。

   **ADD NGUSRSECPARA**

## 任务示例

任务描述

配置所有用户在服务请求流程中需要强制鉴权。

脚本

//配置所有用户在服务请求流程中需要鉴权。

```
ADD NGUSRSECPARA: SUBRANGE=ALL_USER,AUTHEVENT= INIT_REG-1&MOBL_INTRA_REG-0&MOBL_INTER_REG-1&PROD_REG-0&REG_AFT_INTRAHO-0&REG_AFT_INTERHO-0&IDLE_SYSCHG_REG-1&CONN_SYSCHG_REG-0&DEREGISTRATION-0&SERVICE_REQUEST-0&CONNECT_MOD-0, AUTHPERIOD=0;
```
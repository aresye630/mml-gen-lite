# 激活接入控制

* 操作场景
* 必备事项
* 操作步骤
* 任务示例

## 操作场景

当在线用户已用带宽过大，超出协商的最大带宽时，设置带宽接入的控制方式。

适用于SGW-U、PGW-U。

## 必备事项

前提条件

请仔细阅读GWFD-020901 接入控制。

数据

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| **ADD APN** | APN名称（APN） | apn | 本端规划 | - |
| **SET APNQOSATTR** | APN名称（APN） | apn | 本端规划 | - |
|  | 上行CAR/SHAPE开关（CARSHAPEUL） | CAR | 本端规划 | - |
|  | 下行CAR/SHAPE开关（CARSHAPEDL） | CAR | 本端规划 | - |

## 操作步骤

1. 增加APN实例。

   **ADD APN**:APN=APN名称;
2. 将带宽控制方式绑定到APN用例下。

   **SET APNQOSATTR**:APN=APN名称,CARSHAPEUL=上行CAR/SHAPE开关,CARSHAPEDL=下行CAR/SHAPE开关;

## 任务示例

任务描述

本实例中，操作员在UEG上进行数据配置实现以下要求：

当在线用户使用带宽超协商的带宽资源时，上下行采用CAR方式对带宽进行控制，即对超出的带宽数据包进行丢弃。

脚本

//增加APN示例。

```
ADD APN:APN="apn";
```

//配置上下行带宽控制方式。

```
SET APNQOSATTR:APN="apn",CARSHAPEUL=CAR,CARSHAPEDL=CAR;
```

版权所有 © 华为技术有限公司

# 修改AAA鉴权的可选鉴权消息属性

- 操作场景
- 对系统的影响
- 必备事项
- 操作步骤
- 任务示例

## 操作场景

根据要求在UEG 上修改AAA的可选鉴权消息属性。

**说明** 

适用于PGW-C、SMF

## 对系统的影响

修改的数据，对配置后激活的用户生效。

## 必备事项

前提条件

完成配置RADIUS功能。

数据

| 类别               | 参数名称                         | 取值样例   | 获取方法   | 说明                |
|:-----------------|:-----------------------------|:-------|:-------|:------------------|
| AAA鉴权请求携带的私有扩展属性 | RADIUS服务器组名称（RDSSVRGRPNAME）  | ss     | 本端规划   | SET RDSAUTHREQVSA |
| AAA鉴权请求携带的私有扩展属性 | 3GPP私有扩展属性开关（THREEGPP）       | ENABLE | 本端规划   | SET RDSAUTHREQVSA |
| AAA鉴权请求携带的私有扩展属性 | 3GPP-Charging-ID（CHARGINGID） | ENABLE | 本端规划   | SET RDSAUTHREQVSA |

## 操作步骤

1. 进入“MML命令行-UEG”窗口。
2. 修改AAA鉴权消息中携带的3GPP扩展属性。

   **SET RDSACCTREQATTR**

## 任务示例

任务描述

将“鉴权请求消息不携带3GPP-Charging-ID属性”修改为“携带3GPP-Charging-ID属性”。

脚本

//修改AAA鉴权消息中携带的3GPP扩展属性。

```
SET RDSAUTHREQATTR: RDSSVRGRPNAME="ss",CHARGINGID=ENABLE;
```
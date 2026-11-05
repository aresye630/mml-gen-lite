# 查询API GW路由（DSP APIGWROUTES）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用NF：UPF、MPF**

查询服务注册到API GW的路由。

#### 注意事项

该命令执行后立即生效。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识         | 参数名称   | 参数说明                                                                              |
|:-------------|:-------|:----------------------------------------------------------------------------------|
| APP_ID       | 应用实例ID | 可选必选说明：可选参数 参数含义：要查询的路由所属的应用实例ID。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～100。 默认值：无 配置原则：无 |
| SERVICE_NAME | 服务名    | 可选必选说明：可选参数 参数含义：要查询的路由所属的服务名。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～100。 默认值：无 配置原则：无    |
| ROUTE_ID     | 路由ID   | 可选必选说明：可选参数 参数含义：要查询的路由所属的路由ID。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～100。 默认值：无 配置原则：无   |

#### 使用实例

查询所有API GW路由信息：

```
DSP APIGWROUTES:;
```

```
RETCODE = 0  操作成功

已注册服务的路由信息
-----------------------------------------
路由信息 

{"serInfo":{"serName":"asr","uris":null,"addresses":null},"appId":"0","netType":"CSE_SERVICE","interfaces":[{"protocol":"https","path":"/mep/mec_service_mgmt/v1/services","methods":["GET","POST","DELETE","PUT"],"description":"","mchMode":"Prefix","priority":0,"pfmMetrics":"service_discover"},{"protocol":"https","path":"/mep/mec_app_support/v1/timing","methods":["GET","POST","DELETE","PUT"],"description":"","mchMode":"Prefix","priority":0,"pfmMetrics":"timing"},{"protocol":"https","path":"/mep/mec_service_mgmt/v1/applications/[^/]+/subscriptions","methods":["GET","POST","DELETE","PUT"],"description":"","mchMode":"Regular","priority":0,"pfmMetrics":"subscription"},{"protocol":"https","path":"/mep/mec_service_mgmt/v1/applications/[^/]+/services","methods":["GET","POST","DELETE","PUT"],"description":"","mchMode":"Regular","priority":0,"pfmMetrics":"service_register"}]}
(结果个数 = 4)

---    END
```

#### 输出结果说明

| 输出项名称   | 输出项解释      |
|:--------|:-----------|
| 路由信息    | 查询返回的路由信息。 |
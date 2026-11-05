# 查询网元适配包信息（CHECK ADAPTER）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

查询网元适配包信息（CHECK ADAPTER）命令用于维护人员通过前台快速查询CSP OM节点的适配包信息，包括磁盘目录与数据库数据。

若要查询全部网元适配包信息，请不要输入任何参数。

若要查询某个网元适配包信息，请在请求路径中添加appid参数。

#### 注意事项

- 本命令通过在浏览器中输入指定url方式执行。
- 本命令只允许admin角色前台登录后执行。

#### 参数说明

| 参数标识   | 参数名称   | 参数说明                                                                                |
|:-------|:-------|:------------------------------------------------------------------------------------|
| appid  | 网元ID   | 可选必选说明：可选参数 参数含义：用于指示系统需要按照哪个网元ID来查询适配包信息。 取值范围：0~65535。 默认值：无。 配置原则：若不输入，则表示所有的网元。 |

#### 使用实例

1. 查询0网元适配包信息，在浏览器中输入如下url。

   ```
   https://{ip}:{port}/om/v1/modulekeeper/adapterCheck?appid=0
   ```
2. 查询所有网元适配包信息，在浏览器中输入如下url。

   ```
   https://{ip}:{port}/om/v1/modulekeeper/adapterCheck
   ```

#### 输出结果说明

命令执行正常，返回结果示例如下。

```
{
"result":"success",
"data":{
"adapterFile_01":"[Demo_0_demo, , Demo_0_demo/20.2.0, Demo_0_demo/20.2.0/20.2.0]",
"adapterFile_02":"[Demo_0_demo, , Demo_0_demo/20.2.0, Demo_0_demo/20.2.0/20.2.0]",
"adapterData":"[{"appid":"0","version":[{"appversion":"20.2.0","baseversion":"20.2.0"}]}]"
"packageData":"[0's appName is demo， apptype is Demo，appversion is 20.2.0, baseversion is 20.2.0, omip1 is 10.123.0.81, omip2 is 10.123.0.65]"
 }
}
```

输出项解释如下。

| 输出项名称          | 输出项解释                                   |
|:---------------|:----------------------------------------|
| result         | 用于返回命令执行状态。 取值范围：success：成功。 failed：失败。 |
| adapterFile_01 | 用于返回CSP01节点适配包目录。                       |
| adapterFile_02 | 用于返回CSP02节点适配包目录。                       |
| adapterData    | 用于返回CSP服务adapter表数据。                    |
| packageData    | 用于返回CSP服务apppackage表数据。                 |
# 查询APP ID IMSI/MSISDN号段组绑定（LST APPIDSEGBIND）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用NF：PGW-U、UPF**

该命令用于查询APP ID和IMSI/MSISDN号段组与本地APP ID的绑定关系。

#### 注意事项

如果不输入APP ID名称，表示查询所有APP ID和IMSI/MSISDN号段组与本地APP ID的绑定关系。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识   | 参数名称     | 参数说明                                                                                            |
|:-------|:---------|:------------------------------------------------------------------------------------------------|
| APPID  | APP ID名称 | 可选必选说明：可选参数 参数含义：该参数用于指定要绑定的APP ID。 数据来源：全网规划 取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。 默认值：无 配置原则：无 |

#### 使用实例

- 假如运营商需要查询名为testappid绑定的本地APP ID：

  ```
  LST APPIDSEGBIND: APPID="testappid";
  ```

  ```
  RETCODE = 0  操作成功。

  APP ID绑定IMSI/MSISDN号段组
  ---------------------------
             APP ID名称  =  testappid
  IMSI/MSISDN号段组名称  =  testgroup
         本地APP ID名称  =  testlocalappid
             配置域名称  =  NULL
  (结果个数 = 1)

  ---    END
  ```
- 假如运营商需要查询所有APP ID绑定的本地APP ID：

  ```
  LST APPIDSEGBIND:;
  ```

  ```
  RETCODE = 0  操作成功。

  APP ID绑定IMSI/MSISDN号段组
  ---------------------------
  APP ID名称    IMSI/MSISDN号段组名称    本地APP ID名称    配置域名称  

  testappid     testgroup                testlocalappid    NULL           
  testappid1    testgroup1               testlocalappid1   NULL           
  (结果个数 = 2)

  ---    END
  ```

#### 输出结果说明

参见ADD APPIDSEGBIND的参数说明。
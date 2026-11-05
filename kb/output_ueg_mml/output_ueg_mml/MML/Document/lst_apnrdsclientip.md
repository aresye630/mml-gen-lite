# 查询APN Radius Client IP接口（LST APNRDSCLIENTIP）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用NF：PGW-C、SMF**

该命令用于查看APN实例下绑定的radius client ip信息。如果指定可选参数APN，则该命令将显示该APN下配置的radius client ip信息，否则该命令将显示所有配置了radius client ip的APN实例的radius client ip的信息。

#### 注意事项

无。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识       | 参数名称   | 参数说明                                                                                                                                                                                                                                                                                |
|:-----------|:-------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| APN        | APN名称  | 可选必选说明：可选参数 参数含义：该参数用于指定radius client ip需要绑定的APN名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～63。不支持空格及部分特殊字符。可以支持的特殊字符有“.”和“-”，“.”不可以是第一个字符且不可以连续出现。 默认值：无 配置原则：无                                                                                                                              |
| AUTHORACCT | 鉴权或计费  | 可选必选说明：可选参数 参数含义：该参数用于指定是鉴权时的radius client ip还是计费时的radius client ip。 数据来源：本端规划 取值范围：枚举类型。 ACCOUNTING：表示指定的Gi接口的IP地址是计费时的radius client ip。AUTHENTICATION：表示指定的Gi接口的IP地址是鉴权时的radius client ip。ACCT_AND_AUTH：表示指定的Gi接口的IP地址既是鉴权时的radius client ip，也是计费时的radius client ip。 默认值：无 配置原则：无 |
| INTFNAME   | 接口名称   | 可选必选说明：可选参数 参数含义：该参数用于指定该radius client ip配置在哪个接口上。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～13。 默认值：无 配置原则：无                                                                                                                                                                                   |

#### 使用实例

- 当需要查看APN huawei.com下的计费时的radius client ip的配置信息时，可按如下进行配置：

  ```
  LST APNRDSCLIENTIP:APN="huawei.com",AUTHORACCT=ACCOUNTING,INTFNAME="giif1/0/0";
  ```

  ```
  RETCODE = 0  操作成功。

  APN Radius Client 接口绑定
  --------------------------
     APN名称  =  huawei.com
  鉴权或计费  =  计费
    接口名称  =  giif1/0/0
  (结果个数 = 1)
  ---    END
  ```
- 当需要查看APN huawei.com下的鉴权时的radius client ip的配置信息时，可按如下进行配置：

  ```
  LST APNRDSCLIENTIP:APN="huawei.com",AUTHORACCT=AUTHENTICATION,INTFNAME="giif1/0/0";
  ```

  ```
  RETCODE = 0  操作成功。

  APN Radius Client 接口绑定
  --------------------------
     APN名称  =  huawei.com
  鉴权或计费  =  鉴权
    接口名称  =  giif1/0/0
  (结果个数 = 1)
  ---    END
  ```
- 显示所有配置了radius client ip的APN实例的radius client ip的信息。可按如下进行配置：

  ```
  LST APNRDSCLIENTIP:;
  ```

  ```
  RETCODE = 0  操作成功。

  APN Radius Client 接口绑定
  --------------------------
  APN名称    鉴权或计费    接口名称 

  huawei.com    计费          giif1/0/0
  huawei.com    鉴权          giif1/0/0
  (结果个数 = 2)
  ---    END
  ```

#### 输出结果说明

参见ADD APNRDSCLIENTIP的参数说明。
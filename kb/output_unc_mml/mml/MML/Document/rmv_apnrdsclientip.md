# 删除APN Radius Client IP接口（RMV APNRDSCLIENTIP）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例

#### 命令功能

**适用NF：PGW-C、SMF**

**须知** 

本命令属于高危命令，删除Gi接口与APN实例的绑定关系，可能会导致发送鉴权或计费请求消息失败。

该命令用于解除APN实例所配置的radius client ip。当更改该APN实例下的配置时需要解除该APN与Gi接口的绑定关系，使用此命令。

#### 注意事项

- 该命令执行后立即生效。
- 该命令属于高危命令，不允许批量删除操作。如果需要执行此类操作，应将BYTE976的值设置为169。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

#### 参数说明

| 参数标识       | 参数名称   | 参数说明                                                                                                                                                                                                                                                                                |
|:-----------|:-------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| APN        | APN名称  | 可选必选说明：必选参数 参数含义：该参数用于指定radius client ip需要绑定的APN名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～63。不支持空格及部分特殊字符。可以支持的特殊字符有“.”和“-”，“.”不可以是第一个字符且不可以连续出现。 默认值：无 配置原则：无                                                                                                                              |
| AUTHORACCT | 鉴权或计费  | 可选必选说明：必选参数 参数含义：该参数用于指定是鉴权时的radius client ip还是计费时的radius client ip。 数据来源：本端规划 取值范围：枚举类型。 ACCOUNTING：表示指定的Gi接口的IP地址是计费时的radius client ip。AUTHENTICATION：表示指定的Gi接口的IP地址是鉴权时的radius client ip。ACCT_AND_AUTH：表示指定的Gi接口的IP地址既是鉴权时的radius client ip，也是计费时的radius client ip。 默认值：无 配置原则：无 |
| INTFNAME   | 接口名称   | 可选必选说明：可选参数 参数含义：该参数用于指定该radius client ip配置在哪个接口上。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～13。 默认值：无 配置原则：无                                                                                                                                                                                   |

#### 使用实例

- 当更改APN huawei.com下的配置时需要解绑定APN huawei.com下的鉴权请求消息的radius client ip，可按如下配置：

  ```
  RMV APNRDSCLIENTIP:APN="huawei.com",AUTHORACCT=AUTHENTICATION,INTFNAME="giif1/0/0";
  ```
- 当更改APN huawei.com下的配置时需要解绑定APN huawei.com下的计费请求消息的radius client ip，可按如下配置：

  ```
  RMV APNRDSCLIENTIP:APN="huawei.com",AUTHORACCT=ACCOUNTING,INTFNAME="giif1/0/0";
  ```
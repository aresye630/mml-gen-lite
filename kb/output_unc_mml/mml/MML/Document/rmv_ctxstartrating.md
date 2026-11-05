# 删除给OCS/CHF发送的消息初始携带的计费属性（RMV CTXSTARTRATING）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例

#### 命令功能

**适用NF：PGW-C、SMF**

该命令用于删除当前USERPROFILE下指定名字或者所有的计费属性。

#### 注意事项

该命令执行后立即生效。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

#### 参数说明

| 参数标识            | 参数名称         | 参数说明                                                                                                                                                 |
|:----------------|:-------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------|
| USERPROFILENAME | 用户模板名称       | 可选必选说明：必选参数 参数含义：该参数用于指定用户模板名称。 数据来源：全网规划 取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。 默认值：无 配置原则：无                                                          |
| CTXCHGPRMVT     | 初始请求URR组删除类型 | 可选必选说明：必选参数 参数含义：指定CCR-Initial计费属性删除类型。 数据来源：本端规划 取值范围：枚举类型。 ALL：删除绑定的所有CCR-Initial计费属性。SPECIFIC：删除绑定的特定CCR-Initial计费属性。 默认值：无 配置原则：无                |
| CTXRURRGRPNAME  | 初始请求URR组名称   | 可选必选说明：条件必选参数 前提条件：该参数在“CTXCHGPRMVT”配置为“SPECIFIC”时为必选参数。 参数含义：该参数用于指定CCR-Initial URR组名称。 数据来源：全网规划 取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。 默认值：无 配置原则：无 |

#### 使用实例

删除给OCS/CHF发送的消息初始携带的计费属性: USERPROFILENAME为TestUserProfileName，CTXCHGPRMVT为SPECIFIC，CTXRURRGRPNAME为TestCtxRChgProName：

```
RMV CTXSTARTRATING:USERPROFILENAME="TestUserProfileName", CTXCHGPRMVT=SPECIFIC, CTXRURRGRPNAME="TestCtxRChgProName";
```
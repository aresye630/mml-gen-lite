# 增加UE USAGE TYPE群组成员(ADD UEUSGTYPEGPMEM)

- 命令功能
- 注意事项
- 本地用户权限
- 网管用户权限
- 参数说明
- 使用实例

#### 命令功能

**适用网元：MME**

此命令用于为UE USAGE TYPE群组添加一条成员记录。MME为该群组范围内的用户通过DNS查找到对应网元。

#### 注意事项

- 该命令执行后立即生效。
- 此命令最大记录数为1024。

#### 本地用户权限

manage-ug；system-ug

#### 网管用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

#### 参数说明

| 参数标识          | 参数名称              | 参数说明                                                                                                                                                                                                                                                |
|:--------------|:------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| UEUSGTYPEGPID | UE USAGE TYPE群组标识 | 可选必选说明：必选参数 参数含义：该参数用于指定UE USAGE TYPE群组标识。 数据来源：本端规划 取值范围：0~1023 默认值：无 配置原则：此参数已通过ADD UEUSGTYPEGP配置。同一个“UE USAGE TYPE群组标识”可配置多条记录。                                                                                                                  |
| BGNUEUSGTYPE  | 起始UE USAGE TYPE   | 可选必选说明：必选参数 参数含义：该参数用于指定UE USAGE TYPE范围的起始值。 数据来源：本端规划 取值范围：0~255 默认值：无                                                                                                                                                                             |
| ENDUEUSGTYPE  | 终止UE USAGE TYPE   | 可选必选说明：可选参数 参数含义：该参数用于指定UE USAGE TYPE的终止值。 数据来源：本端规划 取值范围：0~255 默认值：无 配置原则：该参数的取值需要大于或者等于“起始UE USAGE TYPE”。  说明： 该参数与“起始UE USAGE TYPE”参数构成一个UE USAGE TYPE范围，方便维护人员配置连续的UE USAGE TYPE区段。该值如果不输入，默认与“起始UE USAGE TYPE”相同。同一个群组标识下的UE USAGE TYPE范围不可重叠。 |

#### 使用实例

运营商为“eMtc”专网规划一个“UE USAGE TYPE群组标识”为“1”的UE USAGE TYPE群组，对于UE USAGE TYPE在“100”至“120”范围内的用户，MME能够通过DNS查询找到对应网元：

- ADD UEUSGTYPEGP: UEUSGTYPEGPID=1, DESC="eMtc";
- ADD UEUSGTYPEGPMEM: UEUSGTYPEGPID=1, BGNUEUSGTYPE=100, ENDUEUSGTYPE=120;
# 修改全局离线计费模板（MOD GLBOFCTEMPLATE）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例

#### 命令功能

**适用NF：SGW-C、PGW-C、SMF**

此命令用来修改离线计费模板绑定到全局离线计费模板配置，以及修改Charge Characteristic绑定离线计费模板中配置信息。

#### 注意事项

- 该命令执行后立即生效。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

#### 参数说明

| 参数标识         | 参数名称                       | 参数说明                                                                                                                                                                                                                                               |
|:-------------|:---------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| GLOBALFLAG   | 全局记录                       | 可选必选说明：必选参数 参数含义：可以为计费属性绑定离线计费模板，也可以为全局绑定离线计费模板。 数据来源：本端规划 取值范围：枚举类型。 GLOBAL：指定计费属性为缺省全局计费属性。CHARGE_CHARACT：指定计费属性为配置的特殊计费属性值。 默认值：无 配置原则：无                                                                                                        |
| CCVALUE      | Charge Characteristic值     | 可选必选说明：条件必选参数 前提条件：该参数在“GLOBALFLAG”配置为“CHARGE_CHARACT”时为必选参数。 参数含义：指定Charge Characteristic值。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～6。该参数为十六进制数据类型，仅支持输入0x/X、a-f/A-F 、0-9，允许不输入0x前缀，字母不区分大小写，取值范围0x0000~0xFFFF。 默认值：无 配置原则：无                                |
| CCMASK       | Charge Characteristic特定值掩码 | 可选必选说明：条件可选参数 前提条件：该参数在“GLOBALFLAG”配置为“CHARGE_CHARACT”时为可选参数。 参数含义：指定Charge Characteristic的掩码，通过配置掩码可以实现全匹配CC值，还是只匹配部分bit位。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～6。该参数为十六进制数据类型，仅支持输入0x/X、a-f/A-F 、0-9，允许不输入0x前缀，字母不区分大小写，取值范围0x0000~0xFFFF。 默认值：无 配置原则：无 |
| CCPRIORITY   | Charge Characteristic优先级   | 可选必选说明：条件可选参数 前提条件：该参数在“GLOBALFLAG”配置为“CHARGE_CHARACT”时为可选参数。 参数含义：设置优先级，配置mask时必须指定优先级。 数据来源：本端规划 取值范围：整数类型，取值范围为0～65535。 默认值：无 配置原则：无                                                                                                            |
| PGWTEMPLATE  | PGW离线计费模板名                 | 可选必选说明：条件可选参数 前提条件：该参数在“GLOBALFLAG”配置为“GLOBAL” 或 “CHARGE_CHARACT”时为可选参数。 参数含义：指定template名称，为指定的charge characteristic或全局离线计费配置绑定PGW形态取用的离线计费模板。离线计费模板可以通过ADD OFCTEMPLATE命令配置。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～63。不支持空格。 默认值：无 配置原则：无                  |
| SGWTEMPLATE  | SGW离线计费模板名                 | 可选必选说明：条件可选参数 前提条件：该参数在“GLOBALFLAG”配置为“GLOBAL” 或 “CHARGE_CHARACT”时为可选参数。 参数含义：指定template名称，为指定的charge characteristic或全局离线计费配置绑定SGW形态取用的离线计费模板。离线计费模板可以通过ADD OFCTEMPLATE命令配置。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～63。不支持空格。 默认值：无 配置原则：无                  |
| GGSNTEMPLATE | GGSN离线计费模板名                | 可选必选说明：条件可选参数 前提条件：该参数在“GLOBALFLAG”配置为“GLOBAL” 或 “CHARGE_CHARACT”时为可选参数。 参数含义：指定模板名称，为指定的charge characteristic或全局离线计费配置绑定GGSN形态取用的离线计费模板。离线计费模板可以通过ADD OFCTEMPLATE命令配置。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～63。不支持空格。 默认值：无 配置原则：无                       |

#### 使用实例

- 修改离线计费模板绑定到全局中的配置。PGWTEMPLATE修改为ofc3，SGWTEMPLATE修改为ofc4：

  ```
  MOD GLBOFCTEMPLATE:GLOBALFLAG=GLOBAL,PGWTEMPLATE="ofc3",SGWTEMPLATE="ofc4",GGSNTEMPLATE="ofc3";
  ```
- 修改Charge Characteristic绑定离线计费模板中的配置信息。CCVALUE修改为0x0004，CCMASK修改为0x0004，CCPRIORITY修改为3：

  ```
  MOD GLBOFCTEMPLATE:GLOBALFLAG=CHARGE_CHARACT,CCVALUE="0x3",CCMASK="0x3",CCPRIORITY=1,PGWTEMPLATE="ofc1",SGWTEMPLATE="ofc2",GGSNTEMPLATE="ofc4";
  ```
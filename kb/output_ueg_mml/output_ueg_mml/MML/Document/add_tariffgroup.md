# 配置费率切换组（ADD TARIFFGROUP）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例

#### 命令功能

**适用NF：SGW-C、PGW-C、SMF**

该命令用来配置费率切换点。如果费率切换点所在的费率切换组不存在，则新建一个费率切换组。

#### 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1000。
- 每个费率切换组可以支持144个费率切换时间段。
- 整系统一共可以支持1000个费率切换组和Charging Characteristic的组合。
- 整系统一共可以支持2000个费率切换点。一个与其它费率点不重复的费率切换段对应两个费率切换点。
- 要求配置CCVALUE和CCMASK取与操作后的值等于CCVALUE。
- 当GlobalFlg为CHARGE\_CHARACR且CCMASK变化时，不允许配置CCVALUE和CCMASK取与后的值与当前已有配置CCVALUE和CCMASK取与后的值相等。
- 同一费率切组下相同计费属性和费率类型的配置只有前24个生效。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

#### 参数说明

| 参数标识          | 参数名称                     | 参数说明                                                                                                                                                                                                                                                                     |
|:--------------|:-------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TARIFFGRPNAME | 费率切换组名                   | 可选必选说明：必选参数 参数含义：指定费率切换组名。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～31。 默认值：无 配置原则：无                                                                                                                                                                                                |
| GLOBALFLG     | 全局配置                     | 可选必选说明：必选参数 参数含义：指定全局配置。 数据来源：本端规划 取值范围：枚举类型。 GLOBAL：指定计费属性为缺省全局计费属性。CHARGE_CHARACT：指定计费属性为配置的特殊计费属性值。 默认值：无 配置原则： GLOBAL：全局。CHARGE_CHARACT：计费属性。                                                                                                                        |
| CCVALUE       | Charge Characteristic值   | 可选必选说明：条件必选参数 前提条件：该参数在“GLOBALFLG”配置为“CHARGE_CHARACT”时为必选参数。 参数含义：指定Charge Characteristic（计费属性）值。当“GLOBALFLG”设置为“CHARGE_CHARACT”时，该参数必须设置。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～6。该参数为十六进制数据类型，仅支持输入0x/X、a-f/A-F 、0-9，允许不输入0x前缀，字母不区分大小写，取值范围0x0000~0xFFFF。 默认值：无 配置原则：无        |
| CCMASK        | Charge Characteristic掩码  | 可选必选说明：条件可选参数 前提条件：该参数在“GLOBALFLG”配置为“CHARGE_CHARACT”时为可选参数。 参数含义：指定Charge Characteristic(计费属性)掩码值。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～6。该参数为十六进制数据类型，仅支持输入0x/X、a-f/A-F 、0-9，允许不输入0x前缀，字母不区分大小写，取值范围0x0001~0xFFFF。 默认值：无 配置原则：当GLOBALFLG值为CHARGE_CHARACT时，掩码的初始值为65535。       |
| CCPRIORITY    | Charge Characteristic优先级 | 可选必选说明：条件可选参数 前提条件：该参数在“GLOBALFLG”配置为“CHARGE_CHARACT”时为可选参数。 参数含义：设置优先级。当CCVALUE不相同时，不允许指定相同的优先级。如果输入了合法CCMASK（配置的CCMASK和CCVALUE相与后的值等于CCVALUE），必须输入CCPRIORITY，否则返回失败。 数据来源：本端规划 取值范围：整数类型，取值范围为1～65535。 默认值：无 配置原则： 当GLOBALFLG值为CHARGE_CHARACT时，优先级的初始值为0。不配置此参数时值默认为0。 |
| TARIFFTYPE    | 费率类型                     | 可选必选说明：必选参数 参数含义：指定配置费率类型为工作日、节假日或者周末。 数据来源：本端规划 取值范围：枚举类型。 WORKDAYWEEKENDFESTIVAL 默认值：无 配置原则：无                                                                                                                                                                          |
| STARTTIME     | 费率切换起始时间                 | 可选必选说明：必选参数 参数含义：指定费率切换起始时间。 数据来源：本端规划 取值范围：时间类型，输入格式是HH:MM。 默认值：无 配置原则：无                                                                                                                                                                                                |
| ENDTIME       | 费率切换终止时间                 | 可选必选说明：必选参数 参数含义：费率切换结束时间。 数据来源：本端规划 取值范围：时间类型，输入格式是HH:MM。 默认值：无 配置原则：无                                                                                                                                                                                                  |

#### 使用实例

配置费率切换组，TARIFFGRPNAME为“huawei”，GLOBALFLG为“CHARGE\_CHARACT”，CCVALUE为“0x0100”，CCMASK为“0x0100”，CCPRIORITY为“2”，TARIFFTYPE为“WORKDAY”，STARTTIME为“09:00”，ENDTIME为“17:00”，命令为：

```
ADD TARIFFGROUP:TARIFFGRPNAME="huawei",GLOBALFLG=CHARGE_CHARACT,CCVALUE="0x100",CCMASK="0x100",CCPRIORITY=2,TARIFFTYPE=WORKDAY,STARTTIME=09&00,ENDTIME=17&00;
```
# 修改Diameter本端信息（MOD UPDIAMLOCINFO）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例

#### 命令功能

**适用NF：UPF**

**须知** 

本命令属于高危命令，修改Diameter本端信息可能导致Diameter链路重建或中断，进而影响用户使用业务，比如用户被去活等。

此命令用来修改Diameter本端信息。

#### 注意事项

- 该命令执行后立即生效。
- 修改后，将导致所有使用该LocalInfo的所有链路断开并重建。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

#### 参数说明

| 参数标识            | 参数名称                        | 参数说明                                                                                                                                                                                                  |
|:----------------|:----------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| HOSTNAME        | 本端主机名                       | 可选必选说明：必选参数 参数含义：该参数用于指定本端主机名。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～127。不支持空格。 默认值：无 配置原则：无                                                                                                                  |
| REALMNAME       | 本端域名                        | 可选必选说明：可选参数 参数含义：该参数用于指定本端域名。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～127。不支持空格。 默认值：无 配置原则：无                                                                                                                   |
| PRODUCTNAME     | 产品名称                        | 可选必选说明：可选参数 参数含义：该参数用于指定产品名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～63。不支持空格。 默认值：无 配置原则：无                                                                                                                    |
| VENDORID        | Vendor-Id AVP值              | 可选必选说明：可选参数 参数含义：该参数用于指定Vendor-Id AVP值。 数据来源：本端规划 取值范围：整数类型，取值范围为0～4294967295。 默认值：无 配置原则：无                                                                                                           |
| FIRMWAREREV     | Firmware-Revision AVP值      | 可选必选说明：可选参数 参数含义：该参数用于指定Firmware-Revision AVP值。 数据来源：本端规划 取值范围：整数类型，取值范围为0～4294967295。 默认值：无 配置原则：如果配置为4294967295，表示Diameter消息不携带Firmware-Revision AVP。                                               |
| ORIGINSTATEID   | Origin-State-Id AVP使能开关     | 可选必选说明：可选参数 参数含义：该参数用于指定Origin-State-Id AVP。 数据来源：本端规划 取值范围：枚举类型。 DISABLE：不使能。ENABLE：使能。 默认值：无 配置原则： DISABLE：表示Diameter消息不携带Origin-State-Id AVP。ENABLE：表示Diameter消息携带Origin-State-Id AVP。             |
| SUPPORTVENDORID | Supported-Vendor-Id AVP使能开关 | 可选必选说明：可选参数 参数含义：该参数用于指定Supported-Vendor-Id AVP。 数据来源：本端规划 取值范围：枚举类型。 DISABLE：不使能。ENABLE：使能。 默认值：无 配置原则： DISABLE：表示Diameter消息不携带Supported-Vendor-Id AVP。ENABLE：表示Diameter消息携带Supported-Vendor-Id AVP。 |

#### 使用实例

修改Diameter本端信息，HOSTNAME为“test”，REALMNAME为“test”，PRODUCTNAME为“product”，VENDORID为0,FIRMWAREREV为1，ORIGINSTATEID为DISABLE，SUPPORTVENDORID为DISABLE：

```
MOD UPDIAMLOCINFO:HOSTNAME="test",REALMNAME="test",PRODUCTNAME="product",VENDORID=0,FIRMWAREREV=1,ORIGINSTATEID=DISABLE,SUPPORTVENDORID=DISABLE;
```
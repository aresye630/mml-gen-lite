# 设置ApnQosAttr配置（SET APNQOSATTR）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例

#### 命令功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用于设置指定APN的带宽控制功能开关。

#### 注意事项

- 该命令执行后只对新激活用户生效。
- 系统最多支持配置10000条ApnQosAttr。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识   | CARSHAPESWUL   |   CARSHAPEUL | CARSHAPESWDL   |   CARSHAPEDL |
|:-------|:---------------|-------------:|:---------------|-------------:|
| 初始值    | INHERIT        |          nan | INHERIT        |          nan |

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

#### 参数说明

| 参数标识         | 参数名称          | 参数说明                                                                                                                                                                                                                                                          |
|:-------------|:--------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| APN          | APN名称         | 可选必选说明：必选参数 参数含义：该参数用来指定APN名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“ ” ”、“ ` ”特殊字符，不区分大小写。 默认值：无 配置原则：该参数使用ADD APN命令配置生成。                                       |
| CARSHAPESWUL | 上行Qos开关       | 可选必选说明：可选参数 参数含义：该参数用于配置上行Qos使能开关。 数据来源：本端规划 取值范围：枚举类型。 INHERIT：继承全局。ENABLE：使能。DISABLE：不使能。 默认值：无 配置原则： INHERIT：继承SET QOSSHAPE/QOSCAR配置的上行带宽QoS控制，SET QOSSHAPE配置优先级高于SET QOSCAR。先继承SET QOSSHAPE的配置，若无配置再继承SET QOSCAR。ENABLE：上行带宽使用QoS控制。DISABLE：上行带宽不使用QoS控制。 |
| CARSHAPEUL   | 上行CAR/SHAPE开关 | 可选必选说明：条件必选参数 前提条件：该参数在“CARSHAPESWUL”配置为“ENABLE”时为必选参数。 参数含义：该参数用于配置上行使能CAR或SHAPE。 数据来源：本端规划 取值范围：枚举类型。 CAR：使能CAR。SHAPE：使能SHAPE。 默认值：无 配置原则：无                                                                                                                 |
| CARSHAPESWDL | 下行Qos开关       | 可选必选说明：可选参数 参数含义：该参数用于配置下行Qos使能开关。 数据来源：本端规划 取值范围：枚举类型。 INHERIT：继承全局。ENABLE：使能。DISABLE：不使能。 默认值：无 配置原则： INHERIT：继承SET QOSSHAPE/QOSCAR配置的下行带宽QoS控制，SET QOSSHAPE配置优先级高于SET QOSCAR。先继承SET QOSSHAPE的配置，若无配置再继承SET QOSCAR。ENABLE：下行带宽使用QoS控制。DISABLE：下行带宽不使用QoS控制。 |
| CARSHAPEDL   | 下行CAR/SHAPE开关 | 可选必选说明：条件必选参数 前提条件：该参数在“CARSHAPESWDL”配置为“ENABLE”时为必选参数。 参数含义：该参数用于配置下行使能CAR或SHAPE。 数据来源：本端规划 取值范围：枚举类型。 CAR：使能CAR。SHAPE：使能SHAPE。 默认值：无 配置原则：无                                                                                                                 |

#### 使用实例

配置APN为apn1.com，用户的下行CARSHAPE继承全局功能。上行CARSHAPE使能CAR功能：

```
SET APNQOSATTR: APN="apn1.com", CARSHAPESWUL=ENABLE, CARSHAPEUL=CAR, CARSHAPESWDL=INHERIT;
```
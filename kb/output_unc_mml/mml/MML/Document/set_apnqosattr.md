# 设置指定APN的QoS属性配置信息（SET APNQOSATTR）

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

**适用NF：PGW-C、SGW-C、SMF、GGSN**

该命令用于设置指定APN的QoS属性配置信息。

## 注意事项

- 该命令执行后只对新激活用户生效。

- 在每次执行ADD APN命令时会自动为本命令增加一条记录，记录中参数的初始设置值如下：HASQOSPROFILE：DISABLE，QOSPROFILENAME：NULL，RDSANDPCCNEGO：DISABLE，BWCTRL：INHERIT。
- 当APN不存在指定Qos Profile时，使用全局Qos Profile。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

## 参数说明

| 参数标识           | 参数名称            | 参数说明                                                                                                                                                                                                                                  |
|:---------------|:----------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| APN            | APN名称           | 可选必选说明：必选参数  参数含义：该参数用来指定APN名称。  数据来源：本端规划  取值范围：字符串类型，输入长度范围是1~63。  默认值：无。  配置原则：  该参数使用ADD APN命令配置生成。                                                                                                                               |
| HASQOSPROFILE  | 有QoS Profile    | 可选必选说明：可选参数  参数含义：该参数用来指定是否配置QoS Profile。  数据来源：本端规划 取值范围： DISABLE（不使能）ENABLE（使能）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST APNQOSATTR查询当前参数配置值。  配置原则：无                                                                               |
| QOSPROFILENAME | QoS Profile名    | 可选必选说明：该参数在"HASQOSPROFILE"配置为"ENABLE"时为条件必选参数。  参数含义：该参数用来指定QoS Profile名称。  数据来源：本端规划  取值范围：字符串类型，输入长度范围是0~63。不区分大小写。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST APNQOSATTR查询当前参数配置值。  配置原则：  该参数需要先通过ADD QOSPROFILE命令配置。               |
| RDSANDPCCNEGO  | AAA和PCRF共同协商QoS | 可选必选说明：可选参数  参数含义：该参数用于指示是否允许AAA和PCRF共同协商QoS。  数据来源：本端规划 取值范围： DISABLE（不使能）ENABLE（使能）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST APNQOSATTR查询当前参数配置值。  配置原则：无                                                                           |
| BWCTRL         | 带宽控制开关          | 可选必选说明：可选参数  参数含义：该参数用于配置带宽控制开关。  数据来源：本端规划 取值范围： INHERIT（继承全局）DISABLE（不使能）ENABLE（使能）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST APNQOSATTR查询当前参数配置值。  配置原则：  当BWCTRL为INHERIT时，根据用户的接入类型和用户属性（本地/漫游/拜访）获取全局配置QosCtrl；使能做带宽控制；不使能不做带宽控制。 |

## 使用实例

配置APN为huawei.com，用户的带宽控制不使能，不配置Qos Profile：

```
SET APNQOSATTR:APN="huawei.com",BWCTRL=DISABLE,HASQOSPROFILE=DISABLE;
```
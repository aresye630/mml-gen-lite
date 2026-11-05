# 增加本地Common Policy配置（ADD LOCCOMMPOLICY）

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

**适用NF：SMF、PGW-C、GGSN**

该命令用于增加本地Common Policy配置。在激活时，根据PCF下发的多个PccRule与SMF本地配置的UserProfile和LocalCommPolicy选择优先级最高的UserProfile作为最终的Common Policy携带给UDG。

## 注意事项

- 该命令执行后立即生效。

- 1、需要预先配置USERPROFILE，使用ADD USERPROFILE命令配置。

- 最多可输入5000条记录。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

## 参数说明

| 参数标识            | 参数名称   | 参数说明                                                                                                                                                                                                                                            |
|:----------------|:-------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| USERPROFILENAME | 用户模板名称 | 可选必选说明：必选参数  参数含义：该参数用于指定用户模板名称。  数据来源：本端规划  取值范围：字符串类型，输入长度范围是1~63。不支持空格，不区分大小写。  默认值：无  配置原则：  该参数使用ADD USERPROFILE命令配置生成。                                                                                                                    |
| PRIORITY        | 优先级    | 可选必选说明：可选参数  参数含义：该参数用于指定UserProfile的全局优先级。  数据来源：本端规划  取值范围：整数类型，取值范围是1~65535。值越小优先级越高。  默认值：65535  配置原则：  设置的PRIORITY仅用于在PCF/PCRF下发的多个UserProfile和本命令配置的UserProfile的交集结果有多个时使用，用于选择出高优先级的UserProfile作为Common Policy。建议不同的UserProfile配置不同的优先级。 |

## 使用实例

- 增加LOCCOMMPOLICY配置，USERPROFILENAME为testuserprofilename1，PRIORITY为10。

  ```
  ADD LOCCOMMPOLICY: USERPROFILENAME= "testuserprofilename1", PRIORITY= 10;
  ```
- 增加LOCCOMMPOLICY配置，USERPROFILENAME为testuserprofilename2，PRIORITY为1。

  ```
  ADD LOCCOMMPOLICY: USERPROFILENAME= "testuserprofilename2", PRIORITY= 1;
  ```
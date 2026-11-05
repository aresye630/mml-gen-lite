# 设置NB-IoT用户的RAT值（SET NBIOTRATVALUE）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例

#### 命令功能

**适用NF：SGW-C、PGW-C、SMF**

该命令用于设置NB-IoT终端接入时UNC给周边网元发送消息时RAT信元中填写的值。

#### 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识   | OCS           | CG            | AAAACCT       | AAAAUTH       | PCRF          | PGW           | CHF           | PCF           | UPF           |
|:-------|:--------------|:--------------|:--------------|:--------------|:--------------|:--------------|:--------------|:--------------|:--------------|
| 初始值    | EUTRAN_NB_IOT | EUTRAN_NB_IOT | EUTRAN_NB_IOT | EUTRAN_NB_IOT | EUTRAN_NB_IOT | EUTRAN_NB_IOT | EUTRAN_NB_IOT | EUTRAN_NB_IOT | EUTRAN_NB_IOT |

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

#### 参数说明

| 参数标识    | 参数名称               | 参数说明                                                                                                                                                                                                     |
|:--------|:-------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| OCS     | 和OCS交互使用的RAT值      | 可选必选说明：可选参数 参数含义：和OCS交互使用的RAT值。 数据来源：对端协商 取值范围：枚举类型。 EUTRAN：表示RAT类型为EUTRAN类型。EUTRAN_NB_IOT：表示RAT类型为EUTRAN-NB-IoT类型。 默认值：无 配置原则：无                                                                         |
| CG      | 和CG交互使用的RAT值       | 可选必选说明：可选参数 参数含义：和CG交互使用的RAT值。 数据来源：对端协商 取值范围：枚举类型。 EUTRAN：表示RAT类型为EUTRAN类型。EUTRAN_NB_IOT：表示RAT类型为EUTRAN-NB-IoT类型。 默认值：无 配置原则：无                                                                          |
| AAAACCT | 和AAA计费服务器交互使用的RAT值 | 可选必选说明：可选参数 参数含义：和AAA计费服务器交互使用的RAT值。 数据来源：对端协商 取值范围：枚举类型。 EUTRAN：表示RAT类型为EUTRAN类型。EUTRAN_NB_IOT：表示RAT类型为EUTRAN-NB-IoT类型。 默认值：无 配置原则：无                                                                    |
| AAAAUTH | 和AAA鉴权服务器交互使用的RAT值 | 可选必选说明：可选参数 参数含义：和AAA鉴权服务器交互使用的RAT值。 数据来源：对端协商 取值范围：枚举类型。 EUTRAN：表示RAT类型为EUTRAN类型。EUTRAN_NB_IOT：表示RAT类型为EUTRAN-NB-IoT类型。 默认值：无 配置原则：无                                                                    |
| PCRF    | 和PCRF交互使用的RAT值     | 可选必选说明：可选参数 参数含义：和PCRF交互使用的RAT值。 数据来源：对端协商 取值范围：枚举类型。 EUTRAN：表示RAT类型为EUTRAN类型。EUTRAN_NB_IOT：表示RAT类型为EUTRAN-NB-IoT类型。 默认值：无 配置原则：当NB-IOT升级优化功能License使能时，此参数配置值为EUTRAN才能生效。                               |
| PGW     | SGW发送给PGW使用的RAT值   | 可选必选说明：可选参数 参数含义：SGW发送给PGW使用的RAT值。 数据来源：对端协商 取值范围：枚举类型。 EUTRAN：表示RAT类型为EUTRAN类型。EUTRAN_NB_IOT：表示RAT类型为EUTRAN-NB-IoT类型。 默认值：无 配置原则：无                                                                      |
| CHF     | 和CHF交互使用的RAT值      | 可选必选说明：可选参数 参数含义：和CHF交互使用的RAT值。 数据来源：对端协商 取值范围：枚举类型。 EUTRAN：表示RAT类型为EUTRAN类型。EUTRAN_NB_IOT：表示RAT类型为EUTRAN-NB-IoT类型。 默认值：无 配置原则：本参数新建场景的默认值为EUTRAN_NB_IOT;升级前版本早于UNC20.6.1时，升级场景的默认值与升级前本命令OCS参数的取值保持一致。  |
| PCF     | 和PCF交互使用的RAT值      | 可选必选说明：可选参数 参数含义：和PCF交互使用的RAT值。 数据来源：对端协商 取值范围：枚举类型。 EUTRAN：表示RAT类型为EUTRAN类型。EUTRAN_NB_IOT：表示RAT类型为EUTRAN-NB-IoT类型。 默认值：无 配置原则：本参数新建场景的默认值为EUTRAN_NB_IOT;升级前版本早于UNC20.6.1时，升级场景的默认值与升级前本命令PCRF参数的取值保持一致。 |
| UPF     | 和UPF交互使用的RAT值      | 可选必选说明：可选参数 参数含义：和UPF交互使用的RAT值。 数据来源：对端协商 取值范围：枚举类型。 EUTRAN：表示RAT类型为EUTRAN类型。EUTRAN_NB_IOT：表示RAT类型为EUTRAN-NB-IoT类型。 默认值：无 配置原则：无                                                                         |

#### 使用实例

此命令用来设置NB-IoT终端接入UNC时，UNC给周边网元发送的消息中RAT信元填写的值：

```
SET NBIOTRATVALUE: OCS=EUTRAN, CG=EUTRAN_NB_IOT;
```
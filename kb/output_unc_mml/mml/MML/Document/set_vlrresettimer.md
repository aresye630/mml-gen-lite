# 设置VLR向MME发送SGsAP-RESET-INDICATION消息定时器配置（SET VLRRESETTIMER）

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

**适用NF：SMSF**

该命令用于设置VLR向MME发送SGsAP-RESET-INDICATION消息后，等待接收MME返回的SGsAP-RESET-ACK响应的定时器配置。

## 注意事项

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| RESNDSW   |   RESNDNUM |   SNDRESETTIMER |
|:----------|-----------:|----------------:|
| FUNC_ON   |          2 |               5 |

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

## 参数说明

| 参数标识          | 参数名称                            | 参数说明                                                                                                                                                                                                                                       |
|:--------------|:--------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| RESNDSW       | 重发开关                            | 可选必选说明：可选参数  参数含义：该参数用于设置VLR向MME发送SGsAP-RESET-INDICATION消息定时器超时后，重发SGsAP-RESET-INDICATION消息的开关。  数据来源：本端规划 取值范围： “FUNC_ON（打开）”：功能开关打开“FUNC_OFF（关闭）”：功能开关关闭  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST VLRRESETTIMER查询当前参数配置值。  配置原则：无        |
| RESNDNUM      | 重发次数                            | 可选必选说明：可选参数  参数含义：该参数用于设置VLR向MME发送SGsAP-RESET-INDICATION消息定时器超时后，可重发的最大次数。  数据来源：本端规划  取值范围：整数类型，取值范围是0~14。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST VLRRESETTIMER查询当前参数配置值。  配置原则：  该参数的取值加1后与SNDRESETTIMER的取值的乘积不得超过14。                  |
| SNDRESETTIMER | VLR等待接收MME SGsAP-RESET-ACK响应(秒) | 可选必选说明：可选参数  参数含义：该参数用于设置VLR向MME发送SGsAP-RESET-INDICATION消息后，等待接收MME返回的SGsAP-RESET-ACK响应的定时器超时时长。  数据来源：本端规划  取值范围：整数类型，取值范围是1~14。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST VLRRESETTIMER查询当前参数配置值。  配置原则：  RESNDNUM的取值加1后与该参数的取值的乘积不得超过14。 |

## 使用实例

运营商希望设置VLR向MME发送SGsAP-RESET-INDICATION消息后，等待接收MME返回的SGsAP-RESET-ACK响应的定时器配置，执行如下命令：

```
SET VLRRESETTIMER: RESNDSW=FUNC_ON, RESNDNUM=2, SNDRESETTIMER=5;
```
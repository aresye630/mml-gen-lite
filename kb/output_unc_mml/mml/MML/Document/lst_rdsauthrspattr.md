# 查询支持的Radius鉴权响应消息私有属性（LST RDSAUTHRSPATTR）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

**适用NF：PGW-C、GGSN、SMF**

该命令用于查询PGW/GGSN是否支持解析RADIUS服务器在鉴权响应消息中返回的运营商私有属性。

## 注意事项

无

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

## 参数说明

| 参数标识          | 参数名称         | 参数说明                                                                                                                          |
|:--------------|:-------------|:------------------------------------------------------------------------------------------------------------------------------|
| RDSSVRGRPNAME | RADIUS服务器组名称 | 可选必选说明：可选参数  参数含义：该参数用于指定RADIUS服务器组名。  数据来源：本端规划  取值范围：字符串类型，输入长度范围是1~31。  默认值：无  配置原则：  需要确保RADIUS服务器组名称已经通过ADD RDSSVRGRP配置。 |

## 使用实例

查看RADIUS服务器组“rds”的鉴权应答消息中运营商私有属性是否支持解析：

```
LST RDSAUTHRSPATTR:RDSSVRGRPNAME="rds";
RETCODE = 0 操作成功。

支持的Radius鉴权响应消息私有属性
--------------------------------
Radius Server Group名称 = rds
Operator-Charging-Rule-Base-Name = 禁止
Event-Charging-Function-Name = 禁止
Operator-Vpn-Name = 允许
(结果个数 = 1)
--- END
```

## 输出结果说明

| 输出项名称                            | 输出项解释                                                                                                              |
|:---------------------------------|:-------------------------------------------------------------------------------------------------------------------|
| RADIUS服务器组名称                     | 该参数用于指定RADIUS服务器组名。                                                                                                |
| Operator-Charging-Rule-Base-Name | 该参数用于配置是否支持解析鉴权回应消息中的Operator-Charging-Rule-Base-Name信元。                                                           |
| Event-Charging-Function-Name     | 该参数用于配置是否支持解析鉴权回应消息中的Operator-Primary-Event-Charging-Function-Name和Operator-Second-Event-Charging-Function-Name信元。 |
| Operator-Vpn-Name                | 该参数用于配置是否支持解析鉴权回应消息中的Operator-Vpn-Name信元。                                                                          |
| 会话时长和空闲上下文时长开关                   | 该参数用于设置最大会话在线时长和空闲上下文时长功能开关。                                                                                       |
| DNS服务器信元取值优先级                    | 该参数用于控制UNC使用Access-Accept消息中的DNS服务器地址优先从Access-Accept消息的标准属性中获取还是从Vendor-Specific扩展属性中获取。                          |
# 设置TCPIP报文以及应用层、黑名单、白名单防御机制使能（SET SECPOLICYSWITCH）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 参考信息

#### 命令功能

该命令用于设置非法报文防御机制使能。

#### 注意事项

- 该命令执行后立即生效。
- 该命令的设定值可通过LST SECPOLICYSWITCH命令进行查询。
- 该命令仅适用于非NP卡场景和NP卡非加速模式场景。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

#### 参数说明

| 参数标识            | 参数名称        | 参数说明                                                                                                                                                                             |
|:----------------|:------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SECPOLICYID     | 安全策略编号      | 可选必选说明：必选参数 参数含义：策略编号。 数据来源：本端规划 取值范围：整数类型，取值范围为1～30。 默认值：无                                                                                                                      |
| SECPOLICYTYPE   | 安全策略类型      | 可选必选说明：必选参数 参数含义：安全策略类型。 数据来源：本端规划 取值范围：枚举类型。 Tcpip：TCP/IP策略。WhiteList：白名单策略。BlackList：黑名单策略。APP：应用策略。 默认值：无                                                                     |
| SECPOLICYTYPEID | 安全策略类型编号    | 可选必选说明：条件必选参数 前提条件：该参数在“SECPOLICYTYPE”配置为“Tcpip”、“WhiteList”、“BlackList” 或 “APP”时为必选参数。 参数含义：安全策略类型编号。 数据来源：本端规划 取值范围：整数类型，取值范围为0～65535。 默认值：无 配置原则：如果SECPOLICYTYPE选择APP，则本选项为0。 |
| SECPOLICYENABLE | 安全策略使能标记    | 可选必选说明：条件必选参数 前提条件：该参数在“SECPOLICYTYPE”配置为“Tcpip”、“WhiteList”、“BlackList” 或 “APP”时为必选参数。 参数含义：协议类型。 数据来源：本端规划 取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。 默认值：无                               |
| SUBTCPIPTYPE    | TCP/IP防攻击类型 | 可选必选说明：条件必选参数 前提条件：该参数在“SECPOLICYTYPE”配置为“Tcpip”时为必选参数。 参数含义：TCP/IP防攻击类型。 数据来源：本端规划 取值范围：枚举类型。 ABNORMAL：非法报文。UDPFLOOD：UDP泛洪报文。TCPSYN：TCPSYN报文。FRAGMENT：分片报文。 默认值：无               |

#### 使用实例

设置非法报文防御机制使能：

```
SET SECPOLICYSWITCH: SECPOLICYID=1, SECPOLICYTYPE=Tcpip, SECPOLICYTYPEID=3, SECPOLICYENABLE=FALSE, SUBTCPIPTYPE=TCPSYN;
```

#### 参考信息

需要先添加安全策略。
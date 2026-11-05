# 修改安全策略告警配置（MOD SECPOLICYALARM）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例

#### 命令功能

该命令用来修改上送CPU报文产生告警参数的配置。

#### 注意事项

- 该命令执行后立即生效。
- 该命令仅适用于非NP卡场景和NP卡非加速模式场景。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

#### 参数说明

| 参数标识            | 参数名称        | 参数说明                                                                                                                                                                                                            |
|:----------------|:------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SECPOLICYID     | 安全策略编号      | 可选必选说明：必选参数 参数含义：安全策略编号。 数据来源：本端规划 取值范围：整数类型，取值范围为1～30。 默认值：无                                                                                                                                                   |
| SECPOLICYTYPE   | 安全策略类型      | 可选必选说明：必选参数 参数含义：策略类型，如应用层联动、TCP/IP防攻击、黑白名单等。 数据来源：本端规划 取值范围：枚举类型。 Tcpip：TCP/IP策略。TotalPkt：所有报文。WhiteList：白名单策略。BlackList：黑名单策略。Index：索引策略。UserFlow：用户自定义流策略。APP：APP应用策略。Urpf：URPF策略。WhiteListV6：IPv6白名单。 默认值：无 |
| SECPOLICYTYPEID | 安全策略类型编号    | 可选必选说明：条件必选参数 前提条件：该参数在“SECPOLICYTYPE”配置为“Index” 或 “UserFlow”时为必选参数。 参数含义：安全策略类型编号。 数据来源：本端规划 取值范围：整数类型，取值范围为0～65535。 默认值：无                                                                                     |
| SECALARMFLAG    | 安全告警使能      | 可选必选说明：条件必选参数 前提条件：该参数在“SECPOLICYTYPE”配置为“WhiteList”、“Index”、“APP”、“UserFlow”、“BlackList”、“Urpf”、“Tcpip”、“WhiteListV6” 或 “TotalPkt”时为必选参数。 参数含义：策略告警是否使能。 数据来源：本端规划 取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。 默认值：无       |
| SECALARMTHLD    | 安全告警阈值      | 可选必选说明：条件必选参数 前提条件：该参数在“SECPOLICYTYPE”配置为“WhiteList”、“Index”、“APP”、“UserFlow”、“BlackList”、“Urpf”、“Tcpip”、“WhiteListV6” 或 “TotalPkt”时为必选参数。 参数含义：告警阈值。 数据来源：本端规划 取值范围：整数类型，取值范围为1～1000000。 默认值：无                 |
| SECALARMINT     | 安全告警时间间隔（秒） | 可选必选说明：条件必选参数 前提条件：该参数在“SECPOLICYTYPE”配置为“WhiteList”、“Index”、“APP”、“UserFlow”、“BlackList”、“Urpf”、“Tcpip”、“WhiteListV6” 或 “TotalPkt”时为必选参数。 参数含义：告警时间间隔。 数据来源：本端规划 取值范围：整数类型，取值范围为60～3600，单位是秒。 默认值：无            |

#### 使用实例

修改上送CPU报文产生告警参数的配置：

```
MOD SECPOLICYALARM:SECPOLICYID=1,SECPOLICYTYPE=WhiteList,SECALARMFLAG=TRUE,SECALARMTHLD=1,SECALARMINT=60;
```
# 配置UDP环回功能（SET LOOPUDP）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例

#### 命令功能

**适用NF：SGW-U、PGW-U、UPF**

该命令为配置类命令，用于配置UDP还回功能的端口及IP地址信息。

#### 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 使能该命令，并在udp环回功能验证完成后，需要关闭该功能。如果未关闭，系统将在凌晨时分删除该命令的数据，下次使用时需要重新使能该命令。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识   | S1ULOOPUDPSW   | S1USRCIPV4ADDR   |   S1USRCPORT | S1UDSTIPV4ADDR   |   S1UDSTPORT | TXULOOPUDPSW   | TXUSRCIPV4ADDR   |   TXUSRCPORT | TXUDSTIPV4ADDR   |   TXUDSTPORT |
|:-------|:---------------|:-----------------|-------------:|:-----------------|-------------:|:---------------|:-----------------|-------------:|:-----------------|-------------:|
| 初始值    | DISABLE        | 0.0.0.0          |            0 | 0.0.0.0          |            0 | DISABLE        | 0.0.0.0          |            0 | 0.0.0.0          |            0 |

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

#### 参数说明

| 参数标识           | 参数名称                | 参数说明                                                                                                                                                                                            |
|:---------------|:--------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| S1ULOOPUDPSW   | S1-U接口UDP环回开关       | 可选必选说明：可选参数 参数含义：该参数用于配置是否使能S1-U接口UDP报文环回功能。 数据来源：对端协商 取值范围： DISABLE：不使能。ENABLE：使能。 默认值：无 配置原则：无                                                                                                |
| S1USRCIPV4ADDR | S1-U接口UDP环回源IPv4地址  | 可选必选说明：条件必选参数 前提条件：该参数在“S1ULOOPUDPSW”配置为“ENABLE”时为必选参数。 参数含义：接口IPv4地址。 数据来源：对端协商 取值范围：NA。 默认值：无 配置原则：无                                                                                          |
| S1USRCPORT     | S1-U接口UDP环回源端口      | 可选必选说明：条件必选参数 前提条件：该参数在“S1ULOOPUDPSW”配置为“ENABLE”时为必选参数。 参数含义：接口端口。 数据来源：对端协商 取值范围：0-65535。 默认值：无 配置原则：无                                                                                         |
| S1UDSTIPV4ADDR | S1-U接口UDP环回目的IPv4地址 | 可选必选说明：条件必选参数 前提条件：该参数在“S1ULOOPUDPSW”配置为“ENABLE”时为必选参数。 参数含义：接口IPv4地址。 数据来源：本端规划 取值范围：NA。 默认值：无 配置原则：无                                                                                          |
| S1UDSTPORT     | S1-U接口UDP环回目的端口     | 可选必选说明：条件必选参数 前提条件：该参数在“S1ULOOPUDPSW”配置为“ENABLE”时为必选参数。 参数含义：接口端口。 数据来源：本端规划 取值范围：14000-14099。 默认值：无 配置原则：无                                                                                     |
| S1UVPNINSTANCE | S1-U接口VPN实例名称       | 可选必选说明：条件可选参数 前提条件：该参数在“S1ULOOPUDPSW”配置为“ENABLE”时为可选参数。 参数含义：该参数用于指定S1-U接口VPN实例名称。 数据来源：全网规划 取值范围：字符串类型，输入长度范围为1～31。不支持空格，区分大小写。 默认值：无 配置原则： 输入单空格将删除该参数已有配置项。绑定VPN时需要确保该VPN已经配置（ADD VPNINST）。  |
| TXULOOPUDPSW   | Tx-U接口UDP环回开关       | 可选必选说明：可选参数 参数含义：该参数用于配置是否使能Tx-U接口UDP报文环回功能。 数据来源：对端协商 取值范围： DISABLE：不使能。ENABLE：使能。 默认值：无 配置原则：无                                                                                                |
| TXUSRCIPV4ADDR | Tx-U接口UDP环回源IPv4地址  | 可选必选说明：条件必选参数 前提条件：该参数在“TXULOOPUDPSW”配置为“ENABLE”时为必选参数。 参数含义：接口IPv4地址。 数据来源：对端协商 取值范围：NA。 默认值：无 配置原则：无                                                                                          |
| TXUSRCPORT     | Tx-U接口UDP环回源端口      | 可选必选说明：条件必选参数 前提条件：该参数在“TXULOOPUDPSW”配置为“ENABLE”时为必选参数。 参数含义：接口端口。 数据来源：对端协商 取值范围：0-65535。 默认值：无 配置原则：无                                                                                         |
| TXUDSTIPV4ADDR | Tx-U接口UDP环回目的IPv4地址 | 可选必选说明：条件必选参数 前提条件：该参数在“TXULOOPUDPSW”配置为“ENABLE”时为必选参数。 参数含义：接口IPv4地址。 数据来源：本端规划 取值范围：NA。 默认值：无 配置原则：无                                                                                          |
| TXUDSTPORT     | Tx-U接口UDP环回目的端口     | 可选必选说明：条件必选参数 前提条件：该参数在“TXULOOPUDPSW”配置为“ENABLE”时为必选参数。 参数含义：接口端口。 数据来源：本端规划 取值范围：14000-14099。 默认值：无 配置原则：无                                                                                     |
| TXUVPNINSTANCE | Tx-U接口VPN实例名称       | 可选必选说明：条件可选参数 前提条件：该参数在“TXULOOPUDPSW”配置为“ENABLE”时为可选参数。 参数含义：该参数用于指定Tx-U接口的VPN实例名称。 数据来源：全网规划 取值范围：字符串类型，输入长度范围为1～31。不支持空格，区分大小写。 默认值：无 配置原则： 输入单空格将删除该参数已有配置项。绑定VPN时需要确保该VPN已经配置（ADD VPNINST）。 |

#### 使用实例

将S1ULOOPUDPSW和TXULOOPUDPSW设为ENABLE，S1USRCIPV4ADDR设为10.10.10.10，S1USRCPORT设为119，S1UDSTIPV4ADDR设为10.10.10.20，S1UDSTPORT设为14098，S1UVPNINSTANCE设为vpn1，将TXUSRCIPV4ADDR设为10.10.20.10，TXUSRCPORT设为255，TXUDSTIPV4ADDR设为10.10.20.20，TXUDSTPORT设为14099，TXUVPNINSTANCE设为vpn1：

```
SET LOOPUDP: S1ULOOPUDPSW=ENABLE, S1USRCIPV4ADDR="10.10.10.10", S1USRCPORT=119, S1UDSTIPV4ADDR="10.10.10.20", S1UDSTPORT=14098, S1UVPNINSTANCE="vpn1", TXULOOPUDPSW=ENABLE, TXUSRCIPV4ADDR="10.10.20.10", TXUSRCPORT=225, TXUDSTIPV4ADDR="10.10.20.20", TXUDSTPORT=14099, TXUVPNINSTANCE="vpn1";
```
# 设置APN的DNS属性（SET UEDNSBINDAPN）

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

**适用NF：PGW-C、SMF、GGSN**

该命令用来配置指定APN实例的DNS属性和DNS64属性。用户需要配置APN下的主、备DNS地址或者主、备DNS64地址时，使用该命令。

## 注意事项

- 该命令执行后立即生效。

- 每个APN支持一条DNS属性配置。
- 配置的主、备DNS服务器地址不能相同。
- 在每次执行ADD APN命令时会自动为本命令增加一条记录，记录中参数的初始设置值如下：FIRMODEV4：DHCP，SECMODEV4：RADIUS，FIRMODEV6：DHCP，SECMODEV6：RADIUS，THIRDMODEV4：LOCAL，FOURTHMODEV4：PCRF，THIRDMODEV6：LOCAL，FOURTHMODEV6：PCRF。
- 配置DNS属性的优先级由高到低为：ADD UEDNSBINDUPGRP，SET UEDNSBINDAPN，SET GLOBALDNS。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

## 参数说明

| 参数标识         | 参数名称            | 参数说明                                                                                                                                                                                                                                                                         |
|:-------------|:----------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| APN          | APN名称           | 可选必选说明：必选参数  参数含义：该参数用于指定APN实例名。  数据来源：本端规划  取值范围：字符串类型，输入长度范围是0~63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”特殊字符，不区分大小写。  默认值：无。  配置原则：  该参数使用ADD APN命令配置生成。                                                 |
| MDNSSERVERV4 | IPv4主DNS服务器IP   | 可选必选说明：可选参数  参数含义：该参数用于配置IPv4主DNS服务器地址。  数据来源：本端规划  取值范围：IPv4地址类型。点分十进制。只允许配置A、B、C类地址。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST UEDNSBINDAPN查询当前参数配置值。  配置原则：无                                                                                                               |
| BDNSSERVERV4 | IPv4备DNS服务器IP   | 可选必选说明：可选参数  参数含义：该参数用于配置IPv4备DNS服务器地址。  数据来源：本端规划  取值范围：IPv4地址类型。点分十进制。只允许配置A、B、C类地址。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST UEDNSBINDAPN查询当前参数配置值。  配置原则：无                                                                                                               |
| MDNSSERVERV6 | IPv6主DNS服务器IP   | 可选必选说明：可选参数  参数含义：该参数用于配置IPv6主DNS服务器地址。  数据来源：本端规划  取值范围：IPv6地址类型。冒号十六进制。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST UEDNSBINDAPN查询当前参数配置值。  配置原则：无                                                                                                                            |
| BDNSSERVERV6 | IPv6备DNS服务器IP   | 可选必选说明：可选参数  参数含义：该参数用于配置IPv6备DNS服务器地址。  数据来源：本端规划  取值范围：IPv6地址类型。冒号十六进制。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST UEDNSBINDAPN查询当前参数配置值。  配置原则：无                                                                                                                            |
| MDNSSERVER64 | IPv6主DNS64服务器IP | 可选必选说明：可选参数  参数含义：该参数用于PDP类型为IPv6时配置主DNS64地址。  数据来源：本端规划  取值范围：IPv6地址类型。冒号十六进制。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST UEDNSBINDAPN查询当前参数配置值。  配置原则：无                                                                                                                      |
| BDNSSERVER64 | IPv6备DNS64服务器IP | 可选必选说明：可选参数  参数含义：该参数用于PDP类型为IPv6时配置备DNS64地址。  数据来源：本端规划  取值范围：IPv6地址类型。冒号十六进制。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST UEDNSBINDAPN查询当前参数配置值。  配置原则：无                                                                                                                      |
| FIRMODEV4    | IPv4 第一优先级服务器属性 | 可选必选说明：可选参数  参数含义：该参数用于指定IPv4第一优先级选择模式。  数据来源：本端规划 取值范围： “LOCAL（local）”：指定本地配置优先。即本命令配置的DNS地址。“RADIUS（radius）”：指定RADIUS服务器返回的DNS属性优先。“DHCP（dhcp）”：指定DHCP服务器返回的DNS属性优先。“PCRF（pcrf）”：指定PCRF返回的DNS属性优先。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST UEDNSBINDAPN查询当前参数配置值。  配置原则：无 |
| SECMODEV4    | IPv4 第二优先级服务器属性 | 可选必选说明：可选参数  参数含义：该参数用于指定IPv4第二优先级选择模式。  数据来源：本端规划 取值范围： “LOCAL（local）”：指定本地配置优先。即本命令配置的DNS地址。“RADIUS（radius）”：指定RADIUS服务器返回的DNS属性优先。“DHCP（dhcp）”：指定DHCP服务器返回的DNS属性优先。“PCRF（pcrf）”：指定PCRF返回的DNS属性优先。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST UEDNSBINDAPN查询当前参数配置值。  配置原则：无 |
| FIRMODEV6    | IPv6 第一优先级服务器属性 | 可选必选说明：可选参数  参数含义：该参数用于指定IPv6第一优先级选择模式。  数据来源：本端规划 取值范围： “LOCAL（local）”：指定本地配置优先。即本命令配置的DNS地址。“RADIUS（radius）”：指定RADIUS服务器返回的DNS属性优先。“DHCP（dhcp）”：指定DHCP服务器返回的DNS属性优先。“PCRF（pcrf）”：指定PCRF返回的DNS属性优先。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST UEDNSBINDAPN查询当前参数配置值。  配置原则：无 |
| SECMODEV6    | IPv6 第二优先级服务器属性 | 可选必选说明：可选参数  参数含义：该参数用于指定IPv6第二优先级选择模式。  数据来源：本端规划 取值范围： “LOCAL（local）”：指定本地配置优先。即本命令配置的DNS地址。“RADIUS（radius）”：指定RADIUS服务器返回的DNS属性优先。“DHCP（dhcp）”：指定DHCP服务器返回的DNS属性优先。“PCRF（pcrf）”：指定PCRF返回的DNS属性优先。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST UEDNSBINDAPN查询当前参数配置值。  配置原则：无 |
| THIRDMODEV4  | IPv4第三优先级服务器属性  | 可选必选说明：可选参数  参数含义：该参数用于指定IPv4第三优先级选择模式。  数据来源：本端规划 取值范围： “LOCAL（local）”：指定本地配置优先。即本命令配置的DNS地址。“RADIUS（radius）”：指定RADIUS服务器返回的DNS属性优先。“DHCP（dhcp）”：指定DHCP服务器返回的DNS属性优先。“PCRF（pcrf）”：指定PCRF返回的DNS属性优先。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST UEDNSBINDAPN查询当前参数配置值。  配置原则：无 |
| FOURTHMODEV4 | IPv4第四优先级服务器属性  | 可选必选说明：可选参数  参数含义：该参数用于指定IPv4第四优先级选择模式。  数据来源：本端规划 取值范围： “LOCAL（local）”：指定本地配置优先。即本命令配置的DNS地址。“RADIUS（radius）”：指定RADIUS服务器返回的DNS属性优先。“DHCP（dhcp）”：指定DHCP服务器返回的DNS属性优先。“PCRF（pcrf）”：指定PCRF返回的DNS属性优先。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST UEDNSBINDAPN查询当前参数配置值。  配置原则：无 |
| THIRDMODEV6  | IPv6第三优先级服务器属性  | 可选必选说明：可选参数  参数含义：该参数用于指定IPv6第三优先级选择模式。  数据来源：本端规划 取值范围： “LOCAL（local）”：指定本地配置优先。即本命令配置的DNS地址。“RADIUS（radius）”：指定RADIUS服务器返回的DNS属性优先。“DHCP（dhcp）”：指定DHCP服务器返回的DNS属性优先。“PCRF（pcrf）”：指定PCRF返回的DNS属性优先。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST UEDNSBINDAPN查询当前参数配置值。  配置原则：无 |
| FOURTHMODEV6 | IPv6第四优先级服务器属性  | 可选必选说明：可选参数  参数含义：该参数用于指定IPv6第四优先级选择模式。  数据来源：本端规划 取值范围： “LOCAL（local）”：指定本地配置优先。即本命令配置的DNS地址。“RADIUS（radius）”：指定RADIUS服务器返回的DNS属性优先。“DHCP（dhcp）”：指定DHCP服务器返回的DNS属性优先。“PCRF（pcrf）”：指定PCRF返回的DNS属性优先。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST UEDNSBINDAPN查询当前参数配置值。  配置原则：无 |

## 使用实例

配置APN实例huawei.com的DNS属性和DNS64属性：

```
SET UEDNSBINDAPN: APN="huawei.com", MDNSSERVERV4="10.1.1.1", BDNSSERVERV4="10.2.2.2", MDNSSERVERV6="2001:0DB8:0:1::", BDNSSERVERV6="2001:0DB8:0:2::", MDNSSERVER64="2001:0DB8:0:3::", BDNSSERVER64="2001:0DB8:0:4::";
```
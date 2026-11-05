# 添加MEP HTTP客户端（ADD MEPHTTPCLIENT）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例

#### 命令功能

**适用NF：UPF、MPF**

该命令用于添加MEP HTTP客户端对象。

#### 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为128。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

#### 参数说明

| 参数标识               | 参数名称          | 参数说明                                                                                                                                                                                                                                                                         |
|:-------------------|:--------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CLIENTNAME         | MEP HTTP客户端名称 | 可选必选说明：必选参数 参数含义：该参数用于指定MEP HTTP客户端名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～63。由大小写字母，数字，“-”，“.”组成，且只能以字母或者数字开头。 默认值：无 配置原则：无                                                                                                                                                       |
| MEPHTTPCLIENTGRP   | MEP HTTP客户端组  | 可选必选说明：必选参数 参数含义：该参数用于指定本MEP HTTP客户端所属MEP HTTP客户端组的名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～63。 默认值：无 配置原则：该参数使用ADD MEPHTTPCLIENTGRP命令配置生成。                                                                                                                                         |
| CLIENTTYPE         | MEP HTTP客户端类型 | 可选必选说明：必选参数 参数含义：该参数用于指定MEP HTTP客户端的类型。 数据来源：本端规划 取值范围： TO_CONNECT_EXTERNAL_NE：连接外部网元的客户端。TO_CONNECT_INTERNAL_MES：连接内部服务的客户端。 默认值：无 配置原则： 当服务端处于本网元外部时，选择“TO_CONNECT_EXTERNAL_NE”。当服务端处于本网元内部时，选择“TO_CONNECT_INTERNAL_MES”。                                                  |
| IPV4               | IPv4地址        | 可选必选说明：可选参数 参数含义：该参数用于指定IPv4地址。 数据来源：全网规划 取值范围：IPv4地址类型。0.0.0.0～255.255.255.255。 默认值：无 配置原则：对于“TO_CONNECT_EXTERNAL_NE”类型的MEP HTTP客户端而言IPV4和IPV6最少配置一个，地址配置必须通过运行ADD MPFLOGICINF命令来完成。其余场景不需要配置IP。                                                                            |
| IPV6               | IPv6地址        | 可选必选说明：可选参数 参数含义：该参数用于指定IPv6地址。 数据来源：全网规划 取值范围：IPv6地址类型。冒号分十六进制，格式为X:X:X:X:X:X:X:X。除了组播地址、链路本地地址、环回地址或未指定的地址为非法地址外，其他都为合法地址。 默认值：无 配置原则：对于“TO_CONNECT_EXTERNAL_NE”类型的MEP HTTP客户端而言IPV4和IPV6最少配置一个，地址配置必须通过运行ADD MPFLOGICINF命令来完成。其余场景不需要配置IP。                                |
| TLSFLG             | 是否启用TLS       | 可选必选说明：必选参数 参数含义：该参数用于指定MEP HTTP客户端是否启用加密传输功能。 数据来源：对端协商 取值范围： ENABLE：使能TLS。DISABLE：不使能TLS。 默认值：无 配置原则：建议设置为ENABLE。如果设置为DISABLE，则报文将会以明文进行传输，存在信息泄露的风险，请谨慎设置。                                                                                                                |
| TLSPARANAME        | TLS参数名称       | 可选必选说明：条件必选参数 前提条件：该参数在“TLSFLG”配置为“ENABLE”时为必选参数。 参数含义：该参数用于指定MEP HTTP客户端所使用的TLS参数名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～63。由大小写字母，数字，“-”，“.”组成，且只能以字母或者数字开头。 默认值：无 配置原则：该参数使用ADD MEPTLSPARA命令配置生成。                                                                               |
| CLIENTCOMMPARANAME | HTTP客户端通信参数名称 | 可选必选说明：可选参数 参数含义：该参数用于指定本客户端所使用的HTTP客户端通信参数的名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～63。由大小写字母，数字，“-”，“.”组成，且只能以字母或者数字开头。 默认值：无 配置原则：该参数使用ADD MEPCLIENTCOMMPARA命令配置生成。                                                                                                              |
| PEERSERVICETAG     | 对端服务标签        | 可选必选说明：可选参数 参数含义：该参数用于指定对端服务标签。 数据来源：本端规划 取值范围： MP1SERVICE：通过Mp1接口注册的服务。MEPSERVICE：MEP平台提供的服务。MM5SERVICE：通过MM5接口注册的服务。LESERVICE：通过Le接口开放的服务。MP2SERVICE：通过Mp2接口开放的服务。 默认值：0 配置原则：存在同时部署多个TO_CONNECT_EXTERNAL_NE类型的客户端场景时必须配置该参数，根据MEP平台作为客户端对接服务时所使用的接口类型配置，建议添加客户端对象时即配置该参数。 |

#### 使用实例

添加MEPHTTPCLIENT对象，添加的MEPHTTPCLIENT对象名称为"client"，隶属的客户端组名为"clientgrp"，客户端类型为"TO\_CONNECT\_EXTERNAL\_NE"，IPV4地址配置为"192.168.1.1"，TLS参数是否使用配置为"ENABLE"，使用的TLS参数名配置为"tls"，配置HTTP客户端通信参数为"DefaultClientPara"，配置对端服务标签为"MEPSERVICE"：

```
ADD MEPHTTPCLIENT: CLIENTNAME="client", MEPHTTPCLIENTGRP="clientgrp", CLIENTTYPE=TO_CONNECT_EXTERNAL_NE, IPV4="192.168.1.1", TLSFLG=ENABLE, TLSPARANAME="tls", CLIENTCOMMPARANAME="DefaultClientPara", PEERSERVICETAG=MEPSERVICE;
```
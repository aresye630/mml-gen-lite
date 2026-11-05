# 增加SLF路由(ADD SLFROUTE)

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

该命令用于在配置数据库中增加一条SLF(Subscription Locator Function)路由的数据记录。在运营商拥有多个HSS数据库的情况下，I-CSCF在登记注册及事务建立过程中通过SLF获得用户签约数据所在的HSS域名。

**说明** 

该命令暂不支持。

## 注意事项

当UDM作为SLF部署且添加记录条数超过5000时，执行该命令耗时会超过1s小于20s。

## 参数说明

| 参数标识   | 参数名称         | 参数说明                                                                                                                                                       |
|:-------|:-------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| RTNAME | 路由名称         | 用于标识路由信息的名称，路由信息的名称唯一。 取值范围：长度不超过127位的字符串。 默认值：无。                                                                                                          |
| RTTYPE | Route信息的类型   | 用于标识在UDM的配置数据库中定义SLF路由信息的类型，即可以对哪些用户标识进行路由匹配。 取值范围： “SIPSUFFIX(Sip后缀)”“TELPREFIX(Tel前缀)”“MSISDNPREFIX(Msisdn前缀)”“NUMBERSEGPREFIX(Number Segment前缀)” 默认值：无。 |
| USERID | 用户标识的前后缀     | 用于标识在UDM的配置数据库中定义SLF路由匹配信息。即以下各种用户标识的前后缀信息: Sip后缀、Tel前缀、Msisdn前缀和Number Segment前缀。 取值范围：长度不超过127位的字符串。 默认值：无。                                              |
| DN     | 用户所在的域       | 用于标识在UDM的配置数据库中定义用户所在的域。 取值范围：长度不超过127位的字符串。 默认值：无。                                                                                                        |
| HN     | 用户归属的HSS地址   | 用于标识在UDM的配置数据库中定义用户归属的HSS地址。 取值范围：长度不超过127位的字符串。 默认值：无。                                                                                                    |
| HN2    | 用户归属的备选HSS地址 | 用于标识在UDM的配置数据库中定义用户归属的备选HSS地址。 取值范围：长度不超过127位的字符串。 默认值：无。                                                                                                  |

## 使用实例

1. 在UDM的配置数据库中增加一条SLF路由信息。Route信息的名称为SLFROUTENAME，Route信息的类型为SIPSUFFIX，用户标识的前后缀为"huawei.com"，用户所在的域为"huawei.com"，用户归属的HSS主机名为"hss.huawei.com"。

   `ADD SLFROUTE: RTNAME="SLFROUTENAME", RTTYPE=SIPSUFFIX, USERID="huawei.com", DN="huawei.com", HN="hss.huawei.com";`
2. 在UDM的配置数据库中增加一条SLF路由信息。Route信息的名称为SLFROUTENAME，Route信息的类型为TELPREFIX，用户标识的前后缀为"tel:+123"，用户所在的域为"huawei.com"，用户归属的HSS主机名为"hss.huawei.com"。

   `ADD SLFROUTE: RTNAME="SLFROUTENAME", RTTYPE=TELPREFIX, USERID="tel:+123", DN="huawei.com", HN="hss.huawei.com";`
3. 在UDM的配置数据库中增加一条SLF路由信息。Route信息的名称为SLFROUTENAME，Route信息的类型为MSISDNPREFIX，用户标识的前后缀为"1234"，用户所在的域为"huawei.com"，用户归属的HSS主机名为"hss.huawei.com"。

   `ADD SLFROUTE: RTNAME="SLFROUTENAME", RTTYPE=MSISDNPREFIX, USERID="1234", DN="huawei.com", HN="hss.huawei.com";`
4. 在UDM的配置数据库中增加一条SLF路由信息。Route信息的名称为SLFROUTENAME，Route信息的类型为NUMBERSEGPREFIX，用户标识的前后缀为"7777"，用户所在的域为"huawei.com"，用户归属的HSS主机名为"hss.huawei.com"。

   `ADD SLFROUTE: RTNAME="SLFROUTENAME", RTTYPE=NUMBERSEGPREFIX, USERID="7777", DN="huawei.com", HN="hss.huawei.com";`
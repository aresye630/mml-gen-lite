# 增加NRF公钥（ADD NRFKEY）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于增加NRF的公钥配置。客户端和服务端需要进行公钥认证时，使用该命令配置公钥信息。

当要启用Oauth 2.0特性功能时，需要配置本命令。

## 注意事项

系统支持NRF公钥配置的最大记录数为32条，添加时勿超过此上限值。

## 参数说明

| 参数标识          | 参数名称    | 参数说明                                                                                                                                                                                                                      |
|:--------------|:--------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| NRFKEYID      | 公钥ID    | 可选必选说明：必选参数。 参数含义：用于指定公钥在系统内的唯一标识。 取值范围：1～32 默认值：无。 配置原则：无。                                                                                                                                                               |
| NRFINSTANCEID | NRF实例ID | 可选必选说明：必选参数。 参数含义：用于标识需要加载公钥的NRF实例。 取值范围：长度不超过127位的字符串。 默认值：无。 配置原则：由对端NF提供。                                                                                                                                              |
| NRFKEY        | 公钥      | 可选必选说明：必选参数 参数含义：用于标识对token进行签名校验使用的NRF的公钥。 取值范围：长度不超过2048的字符串，允许输入：“A-Z”、“a-z”、“0-9”、“-”、“+”，“/”和“=”。 默认值：无。 配置原则：公钥以“-----BEGIN PUBLIC KEY-----”作为开头，以“-----END PUBLIC KEY-----”作为结尾，同时公钥正文每64个字符换行。在MML中填写时，需要去掉所有换行符。 |
| SNDKEYID      | NRF密钥ID | 可选必选说明：可选参数 参数含义：该参数表示NRF上配置的密钥ID，用于在TOKEN管理中标识当前生效的密钥。 数据来源：对端规划 取值范围：长度不超过128位的字符串，区分大小写。 默认值：无 配置原则：当需要在TOKEN校验时检查接收报文中当前生效的NRF密钥ID信息时配置此字段                                                                            |

## 使用实例

增加一个NRF公钥配置信息。其中为公钥ID“11”，“NRF实例标识”为“0221f24ed04”，“公钥”为“-----BEGIN PUBLIC KEY-----MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAqLN3xmUoBeozpev3cF+sMtealu22AukFrLIjatB9TQV+ZIXN1/8hzCJXcvvOerBghzci7E/ZIHgpG595CiN8XwwyaFBJpBNLPMFK1xpkjvt/mAnRLrRGwcs5S7911Egsgi8JKsAHpXbMC6Ji5qAsIRhLvV7hr7j0ptd3l6g7Kpp4m0Ypp9K4bSnIQjVhMe160BZ7Iy4E4xVPzYc3lXLE2atCc1acAi3inOKt+Vi8Uaw5NqcpiCl4BiAwjJVkzBIjQw/Py1yFLrPWBZmXvQ1u8Ry520AM7pbUB03xisUdSpfGJtj7UATRmS5HLcVVkH+w4dwmcR9ZS13rSdg4VlDUURvkQEDD98y5TNgpr9sTNXKb4mgb9eEymkrSb/erHCsbnUDmDrwWIO5LF3hY/OjWDkns8fId2pmWYyXSOv9Nb7I6h/rkvSxt1zEuYmP7GKusJqcMiQqTUUYLZuQMJDpCdO2BCtPNoWlhX4MUNBpMsq5IB0KuA27NwKtSrOsafJs4/L/+IDl0sCbHg49uYKXVP2z3o9RSY3luPJcfR9VNF9lmmK0lqSxAB1eNvSlzoDHzgx2H/NjuIkP8WUh+/qxvWIgoR+nmL86c7PjF5kDNf5XgnKCxuDVa3yb4ZkAooEVwceQkxz2+GZssOsHEu48L4jFGctwCBmapPb666h0CAwEAAQ==-----END PUBLIC KEY-----”

```
ADD NRFKEY: NRFKEYID=11, NRFINSTANCEID="0221f24ed04", NRFKEY="-----BEGIN PUBLIC KEY-----MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAqLN3xmUoBeozpev3cF+sMtealu22AukFrLIjatB9TQV+ZIXN1/8hzCJXcvvOerBghzci7E/ZIHgpG595CiN8XwwyaFBJpBNLPMFK1xpkjvt/mAnRLrRGwcs5S7911Egsgi8JKsAHpXbMC6Ji5qAsIRhLvV7hr7j0ptd3l6g7Kpp4m0Ypp9K4bSnIQjVhMe160BZ7Iy4E4xVPzYc3lXLE2atCc1acAi3inOKt+Vi8Uaw5NqcpiCl4BiAwjJVkzBIjQw/Py1yFLrPWBZmXvQ1u8Ry520AM7pbUB03xisUdSpfGJtj7UATRmS5HLcVVkH+w4dwmcR9ZS13rSdg4VlDUURvkQEDD98y5TNgpr9sTNXKb4mgb9eEymkrSb/erHCsbnUDmDrwWIO5LF3hY/OjWDkns8fId2pmWYyXSOv9Nb7I6h/rkvSxt1zEuYmP7GKusJqcMiQqTUUYLZuQMJDpCdO2BCtPNoWlhX4MUNBpMsq5IB0KuA27NwKtSrOsafJs4/L/+IDl0sCbHg49uYKXVP2z3o9RSY3luPJcfR9VNF9lmmK0lqSxAB1eNvSlzoDHzgx2H/NjuIkP8WUh+/qxvWIgoR+nmL86c7PjF5kDNf5XgnKCxuDVa3yb4ZkAooEVwceQkxz2+GZssOsHEu48L4jFGctwCBmapPb666h0CAwEAAQ==-----END PUBLIC KEY-----";
```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息。

该命令执行异常，会返回对应的错误码。常见错误码如表1所示。

|   错误码 | 错误码解释                        | 原因分析                          | 处理建议                                                                      |
|------:|:-----------------------------|:------------------------------|:--------------------------------------------------------------------------|
| 57918 | NRF实例ID已经存在。                 | 本次操作输入的“公钥ID”在数据库中已存在。        | 通过执行LST NRFKEY命令查询系统已有公钥ID，避免重复配置。                                        |
| 58223 | 同一NRF实例下已有相同“SNDKEYID”。      | 本次输入的“SNDKEYID”已在存在。          | 通过执行LST NRFKEY命令查询系统已有“SNDKEYID”，避免重复配置。                                  |
| 58224 | 同一NRF实例下不能有两条“SNDKEYID”为空记录。 | 不允许同一NRF实例下有两条“SNDKEYID”为空记录。 | 通过执行LST NRFKEY命令查询系统NRF实例，若已有一条“SNDKEYID”为空的记录，则剩余记录执行本命令时需要添加“SNDKEYID”。 |
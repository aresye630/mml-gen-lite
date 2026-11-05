# 修改NRF公钥配置 (MOD PUBLICKEY)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

本命令用于修改一条NRF公钥配置信息。在该命令中，系统通过“NRF实例标识”参数来唯一标识一条NRF公钥配置信息。

## 注意事项

无。

## 参数说明

| 参数标识      | 参数名称    | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|:----------|:--------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| NRFINSID  | NRF实例标识 | 可选必选说明：必选参数 参数含义：标识一条NRF公钥配置记录的关键字段（其取值不能被修改），用于指定需要对哪个NRF实例标识对应的NRF公钥配置记录进行修改或调整，操作员可以使用LST PUBLICKEY命令查询获得。 取值范围：有效的UUIDv4格式，只允许输入0～9，a～f，A～F，“-”。 默认值：无。 配置原则：无。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| PUBLICKEY | 公钥      | 可选必选说明：必选参数 参数含义：用于标识修改后的NRF公钥。 取值范围：长度不超过2048的字符串，允许输入0～9，a～z，A～Z，“+”，“-”，“/”、“=”和空格。 默认值：无。 配置原则：公钥使用“-----BEGIN PUBLIC KEY-----”开头，使用“-----END PUBLIC KEY-----”结尾，同时公钥正文每64个字符换行。在MML中填写时，需要去掉所有换行符，样例如下。 -----BEGIN PUBLIC KEY-----MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAqLN3xmUoBeozpev3cF+sMtealu22AukFrLIjatB9TQV+ZIXN1/8hzCJXcvvOerBghzci7E/ZIHgpG595CiN8XwwyaFBJpBNLPMFK1xpkjvt/mAnRLrRGwcs5S7911Egsgi8JKsAHpXbMC6Ji5qAsIRhLvV7hr7j0ptd3l6g7Kpp4m0Ypp9K4bSnIQjVhMe160BZ7Iy4E4xVPzYc3lXLE2atCc1acAi3inOKt+Vi8Uaw5NqcpiCl4BiAwjJVkzBIjQw/Py1yFLrPWBZmXvQ1u8Ry520AM7pbUB03xisUdSpfGJtj7UATRmS5HLcVVkH+w4dwmcR9ZS13rSdg4VlDUURvkQEDD98y5TNgpr9sTNXKb4mgb9eEymkrSb/erHCsbnUDmDrwWIO5LF3hY/OjWDkns8fId2pmWYyXSOv9Nb7I6h/rkvSxt1zEuYmP7GKusJqcMiQqTUUYLZuQMJDpCdO2BCtPNoWlhX4MUNBpMsq5IB0KuA27NwKtSrOsafJs4/L/+IDl0sCbHg49uYKXVP2z3o9RSY3luPJcfR9VNF9lmmK0lqSxAB1eNvSlzoDHzgx2H/NjuIkP8WUh+/qxvWIgoR+nmL86c7PjF5kDNf5XgnKCxuDVa3yb4ZkAooEVwceQkxz2+GZssOsHEu48L4jFGctwCBmapPb666h0CAwEAAQ==-----END PUBLIC KEY----- |

## 使用实例

修改“NRF实例标识”为“8a6bd00f-c9af-4ebe-9184-0221f24ed04”的“公钥”为“-----BEGIN-PUBLIC-KEY-----MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAqLN3xmUoBeozpev3cF+sMtealu22AukFrLIjatB9TQV+ZIXN1/8hzCJXcvvOerBghzci7E/ZIHgpG6a58iN8XwwyaFBJpBNLPMFK1xpkjvt/mAnRLrRGwcs5S7911Egsgi8JKsAHpXbMC6Ji5qAsIRhLvV7hr7j0ptd3l6g7Kpp4m0Ypp9K4bSnIQjVhMe160BZ7Iy4E4xVPzYc3lXLE2atCc1acAi3inOKt+Vi8Uaw5NqcpiCl4BiAwjJVkzBIjQw/Py1yFLrPWBZmXvQ1u8Ry520AM7pbUB03xisUdSpfGJtj7UATRmS5HLcVVkH+w4dwmcR9ZS13rSdg4VlDUURvkQEDD98y5TNgpr9sTNXKb4mgb9eEymkrSb/erHCsbnUDmDrwWIO5LF3hY/OjWDkns8fId2pmWYyXSOv9Nb7I6h/rkvSxt1zEuYmP7GKusJqcMiQqTUUYLZuQMJDpCdO2BCtPNoWlhX4MUNBpMsq5IB0KuA27NwKtSrOsafJs4/L/+IDl0sCbHg49uYKXVP2z3o9RSY3luPJcfR9VNF39mmK0lqSxAB1eNvSlzoDHzgx2H/NjuIkP8WUh+/qxvWIgoR+nmL86c7PjF5kDNf5XgnKCxuDVa3yb4ZkAooEVwceQkxz2+GZssOsHEu48L4jFGctwCBmapPb666h0CAwEAAQ==-----END-PUBLIC-KEY-----”：

```
MOD PUBLICKEY: NRFINSID="8a6bd00f-c9af-4ebe-9184-0221f24ed04", PUBLICKEY="-----BEGIN-PUBLIC-KEY-----MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAqLN3xmUoBeozpev3cF+sMtealu22AukFrLIjatB9TQV+ZIXN1/8hzCJXcvvOerBghzci7E/ZIHgpG6a58iN8XwwyaFBJpBNLPMFK1xpkjvt/mAnRLrRGwcs5S7911Egsgi8JKsAHpXbMC6Ji5qAsIRhLvV7hr7j0ptd3l6g7Kpp4m0Ypp9K4bSnIQjVhMe160BZ7Iy4E4xVPzYc3lXLE2atCc1acAi3inOKt+Vi8Uaw5NqcpiCl4BiAwjJVkzBIjQw/Py1yFLrPWBZmXvQ1u8Ry520AM7pbUB03xisUdSpfGJtj7UATRmS5HLcVVkH+w4dwmcR9ZS13rSdg4VlDUURvkQEDD98y5TNgpr9sTNXKb4mgb9eEymkrSb/erHCsbnUDmDrwWIO5LF3hY/OjWDkns8fId2pmWYyXSOv9Nb7I6h/rkvSxt1zEuYmP7GKusJqcMiQqTUUYLZuQMJDpCdO2BCtPNoWlhX4MUNBpMsq5IB0KuA27NwKtSrOsafJs4/L/+IDl0sCbHg49uYKXVP2z3o9RSY3luPJcfR9VNF39mmK0lqSxAB1eNvSlzoDHzgx2H/NjuIkP8WUh+/qxvWIgoR+nmL86c7PjF5kDNf5XgnKCxuDVa3yb4ZkAooEVwceQkxz2+GZssOsHEu48L4jFGctwCBmapPb666h0CAwEAAQ==-----END-PUBLIC-KEY-----";
```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息。

该命令执行异常，会返回对应的错误码。常见错误码如表1所示。

|   错误码 | 错误码解释        | 原因分析               | 处理建议                                                  |
|------:|:-------------|:-------------------|:------------------------------------------------------|
|   505 | 当前操作的配置数据不存在 | 需要修改的“NRF实例标识”不存在。 | 执行LST PUBLICKEY命令查询已配置的“NRF实例标识”，输入正确的取值后重新执行本命令进行修改。 |
# 增加NRF公钥配置 (ADD PUBLICKEY)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于增加NRF公钥配置信息，用于验证token数字签名的完整性。

## 注意事项

NRF公钥配置的最大记录数为100条，添加时勿超过此上限值。

## 参数说明

| 参数标识      | 参数名称    | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|:----------|:--------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| NRFINSID  | NRF实例标识 | 可选必选说明：必选参数 参数含义：用于标识NRF在系统中的序号，该参数为UUIDv4格式。 UUIDv4格式为“xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx”，例如：4947a69a-f61b-4bc1-b9da-47c9c5d14b64。 取值范围：有效的UUIDv4格式，只允许输入0～9，a～f，A～F，“-”。 默认值：无。 配置原则：该参数是NRF公钥数据的唯一索引。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| PUBLICKEY | 公钥      | 可选必选说明：必选参数 参数含义：用于标识对token进行签名校验使用的NRF的公钥。 取值范围：长度不超过2048的字符串，允许输入0～9，a～z，A～Z，“+”，“-”，“/”、“=”和空格。 默认值：无。 配置原则：公钥使用“-----BEGIN PUBLIC KEY-----”开头，使用“-----END PUBLIC KEY-----”结尾，同时公钥正文每64个字符换行。在MML中填写时，需要去掉所有换行符，样例如下。 -----BEGIN PUBLIC KEY-----MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAqLN3xmUoBeozpev3cF+sMtealu22AukFrLIjatB9TQV+ZIXN1/8hzCJXcvvOerBghzci7E/ZIHgpG595CiN8XwwyaFBJpBNLPMFK1xpkjvt/mAnRLrRGwcs5S7911Egsgi8JKsAHpXbMC6Ji5qAsIRhLvV7hr7j0ptd3l6g7Kpp4m0Ypp9K4bSnIQjVhMe160BZ7Iy4E4xVPzYc3lXLE2atCc1acAi3inOKt+Vi8Uaw5NqcpiCl4BiAwjJVkzBIjQw/Py1yFLrPWBZmXvQ1u8Ry520AM7pbUB03xisUdSpfGJtj7UATRmS5HLcVVkH+w4dwmcR9ZS13rSdg4VlDUURvkQEDD98y5TNgpr9sTNXKb4mgb9eEymkrSb/erHCsbnUDmDrwWIO5LF3hY/OjWDkns8fId2pmWYyXSOv9Nb7I6h/rkvSxt1zEuYmP7GKusJqcMiQqTUUYLZuQMJDpCdO2BCtPNoWlhX4MUNBpMsq5IB0KuA27NwKtSrOsafJs4/L/+IDl0sCbHg49uYKXVP2z3o9RSY3luPJcfR9VNF9lmmK0lqSxAB1eNvSlzoDHzgx2H/NjuIkP8WUh+/qxvWIgoR+nmL86c7PjF5kDNf5XgnKCxuDVa3yb4ZkAooEVwceQkxz2+GZssOsHEu48L4jFGctwCBmapPb666h0CAwEAAQ==-----END PUBLIC KEY----- |

## 使用实例

UDM配置5G信令支持Oauth 2.0鉴权时需要增加NRF公钥配置信息。其中“NRF实例标识”为“8a6bd00f-c9af-4ebe-9184-0221f24ed048”，“公钥”为“-----BEGIN-PUBLIC-KEY-----MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAqLN3xmUoBeozpev3cF+sMtealu22AukFrLIjatB9TQV+ZIXN1/8hzCJXcvvOerBghzci7E/ZIHgpG595CiN8XwwyaFBJpBNLPMFK1xpkjvt/mAnRLrRGwcs5S7911Egsgi8JKsAHpXbMC6Ji5qAsIRhLvV7hr7j0ptd3l6g7Kpp4m0Ypp9K4bSnIQjVhMe160BZ7Iy4E4xVPzYc3lXLE2atCc1acAi3inOKt+Vi8Uaw5NqcpiCl4BiAwjJVkzBIjQw/Py1yFLrPWBZmXvQ1u8Ry520AM7pbUB03xisUdSpfGJtj7UATRmS5HLcVVkH+w4dwmcR9ZS13rSdg4VlDUURvkQEDD98y5TNgpr9sTNXKb4mgb9eEymkrSb/erHCsbnUDmDrwWIO5LF3hY/OjWDkns8fId2pmWYyXSOv9Nb7I6h/rkvSxt1zEuYmP7GKusJqcMiQqTUUYLZuQMJDpCdO2BCtPNoWlhX4MUNBpMsq5IB0KuA27NwKtSrOsafJs4/L/+IDl0sCbHg49uYKXVP2z3o9RSY3luPJcfR9VNF39mmK0lqSxAB1eNvSlzoDHzgx2H/NjuIkP8WUh+/qxvWIgoR+nmL86c7PjF5kDNf5XgnKCxuDVa3yb4ZkAooEVwceQkxz2+GZssOsHEu48L4jFGctwCBmapPb666h0CAwEAAQ==-----END-PUBLIC-KEY-----”：

```
ADD PUBLICKEY: NRFINSID="8a6bd00f-c9af-4ebe-9184-0221f24ed048", PUBLICKEY="-----BEGIN-PUBLIC-KEY-----MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAqLN3xmUoBeozpev3cF+sMtealu22AukFrLIjatB9TQV+ZIXN1/8hzCJXcvvOerBghzci7E/ZIHgpG595CiN8XwwyaFBJpBNLPMFK1xpkjvt/mAnRLrRGwcs5S7911Egsgi8JKsAHpXbMC6Ji5qAsIRhLvV7hr7j0ptd3l6g7Kpp4m0Ypp9K4bSnIQjVhMe160BZ7Iy4E4xVPzYc3lXLE2atCc1acAi3inOKt+Vi8Uaw5NqcpiCl4BiAwjJVkzBIjQw/Py1yFLrPWBZmXvQ1u8Ry520AM7pbUB03xisUdSpfGJtj7UATRmS5HLcVVkH+w4dwmcR9ZS13rSdg4VlDUURvkQEDD98y5TNgpr9sTNXKb4mgb9eEymkrSb/erHCsbnUDmDrwWIO5LF3hY/OjWDkns8fId2pmWYyXSOv9Nb7I6h/rkvSxt1zEuYmP7GKusJqcMiQqTUUYLZuQMJDpCdO2BCtPNoWlhX4MUNBpMsq5IB0KuA27NwKtSrOsafJs4/L/+IDl0sCbHg49uYKXVP2z3o9RSY3luPJcfR9VNF39mmK0lqSxAB1eNvSlzoDHzgx2H/NjuIkP8WUh+/qxvWIgoR+nmL86c7PjF5kDNf5XgnKCxuDVa3yb4ZkAooEVwceQkxz2+GZssOsHEu48L4jFGctwCBmapPb666h0CAwEAAQ==-----END-PUBLIC-KEY-----";
```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息。

该命令执行异常，会返回对应的错误码。常见错误码如下表1所示。

|   错误码 | 错误码解释       | 原因分析                     | 处理建议                                                  |
|------:|:------------|:-------------------------|:------------------------------------------------------|
|   503 | 配置数据已存在     | 待增加的NRF公钥配置记录已存在，无法重复添加。 | 使用LST PUBLICKEY查询已存在的NRF公钥配置信息，重新添加一条不在记录中的NRF公钥配置数据。 |
|   504 | 当前配置记录数达到上限 | NRF公钥配置数据已达上限，无法新增。      | 使用LST PUBLICKEY查询已存在的NRF公钥配置信息，删除无效数据并重新添加。           |
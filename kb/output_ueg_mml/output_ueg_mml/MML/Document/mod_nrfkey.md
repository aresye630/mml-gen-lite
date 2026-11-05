# 修改NRF公钥 （MOD NRFKEY）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

**须知** 

此命令是高此命令，如果执行不当会导致业务处理受损，需联系华为技术支持确认后再执行。

本命令用于修改一条NRF公钥配置信息。在该命令中，系统通过“公钥ID”关键参数来唯一标识一条NRF公钥配置信息。

## 注意事项

无。

## 参数说明

| 参数标识     | 参数名称    | 参数说明                                                                                                                                                                                                                       |
|:---------|:--------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| NRFKEYID | 公钥ID    | 可选必选说明：必选参数 参数含义：指定一条NRF公钥在系统内的唯一标识，用于指定需要对哪一条NRF公钥配置记录进行修改或调整，操作员可以使用LST NRFKEY命令查询获得。 取值范围：1～32 默认值：无。 配置原则：无。                                                                                                           |
| NRFKEY   | 公钥      | 可选必选说明：必选参数 参数含义：用于标识修改后的NRF公钥。 取值范围：长度不超过2048的字符串，由数字、字母和下划线组成。允许输入：“A-Z”、“a-z”、“0-9”、“-”、“+”，“/”和“=”。 默认值：无。 配置原则：公钥以“-----BEGIN PUBLIC KEY-----”作为开头，以“-----END PUBLIC KEY-----”作为结尾，同时公钥正文每64个字符换行。在MML中填写时，需要去掉所有换行符。 |
| SNDKEYID | NRF密钥ID | 可选必选说明：可选参数 参数含义：该参数表示NRF上配置的密钥ID，用于在TOKEN管理中标识当前生效的密钥。 数据来源：对端规划 取值范围：长度不超过128位的字符串，区分大小写。 默认值：无 配置原则：当需要在TOKEN校验时检查接收报文中当前生效的NRF密钥ID信息时配置此字段。                                                                            |

## 使用实例

修改“公钥ID”为“11”的“公钥”为“-----BEGIN PUBLIC KEY-----MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAqLN3xmUoBeozpev3cF+sMtealu22AukFrLIjatB9TQV+ZIXN1/8hzCJXcvvOerBghzci7E/ZIHgpG595CiN8XwwyaFBJpBNLPMFK1xpkjvt/mAnRLrRGwcs5S7911Egsgi8JKsAHpXbMC6Ji5qAsIRhLvV7hr7j0ptd3l6g7Kpp4m0Ypp9K4bSnIQjVhMe160BZ7Iy4E4xVPzYc3lXLE2atCc1acAi3inOKt+Vi8Uaw5NqcpiCl4BiAwjJVkzBIjQw/Py1yFLrPWBZmXvQ1u8Ry520AM7pbUB03xisUdSpfGJtj7UATRmS5HLcVVkH+w4dwmcR9ZS13rSdg4VlDUURvkQEDD98y5TNgpr9sTNXKb4mgb9eEymkrSb/erHCsbnUDmDrwWIO5LF3hY/OjWDkns8fId2pmWYyXSOv9Nb7I6h/rkvSxt1zEuYmP7GKusJqcMiQqTUUYLZuQMJDpCdO2BCtPNoWlhX4MUNBpMsq5IB0KuA27NwKtSrOsafJs4/L/+IDl0sCbHg49uYKXVP2z3o9RSY3luPJcfR9VNF9lmmK0lqSxAB1eNvSlzoDHzgx2H/NjuIkP8WUh+/qxvWIgoR+nmL86c7PjF5kDNf5XgnKCxuDVa3yb4ZkAooEVwceQkxz2+GZssOsHEu48L4jFGctwCBmapPb666h0CAwEAAQ==-----END PUBLIC KEY-----”：

```
MOD NRFKEY: NRFKEYID=11, NRFKEY="-----BEGIN PUBLIC KEY-----MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAqLN3xmUoBeozpev3cF+sMtealu22AukFrLIjatB9TQV+ZIXN1/8hzCJXcvvOerBghzci7E/ZIHgpG595CiN8XwwyaFBJpBNLPMFK1xpkjvt/mAnRLrRGwcs5S7911Egsgi8JKsAHpXbMC6Ji5qAsIRhLvV7hr7j0ptd3l6g7Kpp4m0Ypp9K4bSnIQjVhMe160BZ7Iy4E4xVPzYc3lXLE2atCc1acAi3inOKt+Vi8Uaw5NqcpiCl4BiAwjJVkzBIjQw/Py1yFLrPWBZmXvQ1u8Ry520AM7pbUB03xisUdSpfGJtj7UATRmS5HLcVVkH+w4dwmcR9ZS13rSdg4VlDUURvkQEDD98y5TNgpr9sTNXKb4mgb9eEymkrSb/erHCsbnUDmDrwWIO5LF3hY/OjWDkns8fId2pmWYyXSOv9Nb7I6h/rkvSxt1zEuYmP7GKusJqcMiQqTUUYLZuQMJDpCdO2BCtPNoWlhX4MUNBpMsq5IB0KuA27NwKtSrOsafJs4/L/+IDl0sCbHg49uYKXVP2z3o9RSY3luPJcfR9VNF9lmmK0lqSxAB1eNvSlzoDHzgx2H/NjuIkP8WUh+/qxvWIgoR+nmL86c7PjF5kDNf5XgnKCxuDVa3yb4ZkAooEVwceQkxz2+GZssOsHEu48L4jFGctwCBmapPb666h0CAwEAAQ==-----END PUBLIC KEY-----";
```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息。
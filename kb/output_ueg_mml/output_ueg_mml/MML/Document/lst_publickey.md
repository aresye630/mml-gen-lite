# 查询NRF公钥配置 (LST PUBLICKEY)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

本命令用于查询已配置的NRF公钥配置信息。

- 若需要查询所有配置的NRF公钥配置信息，请不要输入任何参数。
- 若需要查询某个NRF公钥配置信息，请输入“NRF实例标识”。

## 注意事项

无。

## 参数说明

| 参数标识     | 参数名称    | 参数说明                                                                                                                                       |
|:---------|:--------|:-------------------------------------------------------------------------------------------------------------------------------------------|
| NRFINSID | NRF实例标识 | 可选必选说明：可选参数 参数含义：用于指定系统按照哪个NRF实例标识查询NRF公钥配置信息；若不输入，则表示查询所有的NRF公钥配置信息。 取值范围：有效的UUIDv4格式，只允许输入0～9，a～f，A～F，“-”。 默认值：无。 配置原则：该参数是NRF公钥数据的唯一索引。 |

## 使用实例

1. 查询所有的NRF公钥配置信息：

   ```
   LST PUBLICKEY:;
   ```

   ```
   %%LST PUBLICKEY:;%%
   RETCODE = 0  操作成功

   操作结果如下: 
   -------------
   NRF实例标识                           公钥                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
   1111-2222-3333                        ---333---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
   4947a69a-f61b-4bc1-b9da-47c9c5d14b38  -----BEGIN-PUBLIC-KEY-----MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAqLN3xmUoBeozpev3cF+sMtealu38AukFrLIjatB9TQV+ZIXN1/8hzCJXcvvOerBghzci7E/ZIHgpG595CiN8XwwyaFBJpBNLPMFK1xpkjvt/mAnRLrRGwcs5S7911Egsgi8JKsAHpXbMC6Ji5qAsIRhLvV7hr7j0ptd3l6g7Kpp4m0Ypp9K4bSnIQjVhMe160BZ7Iy4E4xVPzYc3lXLE2atCc1acAi3inOKt+Vi8Uaw5NqcpiCl4BiAwjJVkzBIjQw/Py1yFLrPWBZmXvQ1u8Ry520AM7pbUB03xisUdSpfGJtj7UATRmS5HLcVVkH+w4dwmcR9ZS13rSdg4VlDUURvkQEDD98y5TNgpr9sTNXKb4mgb9eEymkrSb/erHCsbnUDmDrwWIO5LF3hY/OjWDkns8fId2pmWYyXSOv9Nb7I6h/rkvSxt1zEuYmP7GKusJqcMiQqTUUYLZuQMJDpCdO2BCtPNoWlhX4MUNBpMsq5IB0KuA27NwKtSrOsafJs4/L/+IDl0sCbHg49uYKXVP2z3o9RSY3luPJcfR9VNF9lmmK0lqSxAB1eNvSlzoDHzgx2H/NjuIkP8WUh+/qxvWIgoR+nmL86c7PjF5kDNf5XgnKCxuDVa3yb4ZkAooEVwceQkxz2+GZssOsHEu48L4jFGctwCBmapPb666h0CAwEAAQ==-----END-PUBLIC-KEY-----  
   4947a69a-f61b-4bc1-b9da-47c9c5d14b64  -----BEGIN-PUBLIC-KEY-----MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAqLN3xmUoBeozpev3cF+sMtealu22AukFrLIjatB9TQV+ZIXN1/8hzCJXcvvOerBghzci7E/ZIHgpG595CiN8XwwyaFBJpBNLPMFK1xpkjvt/mAnRLrRGwcs5S7911Egsgi8JKsAHpXbMC6Ji5qAsIRhLvV7hr7j0ptd3l6g7Kpp4m0Ypp9K4bSnIQjVhMe160BZ7Iy4E4xVPzYc3lXLE2atCc1acAi3inOKt+Vi8Uaw5NqcpiCl4BiAwjJVkzBIjQw/Py1yFLrPWBZmXvQ1u8Ry520AM7pbUB03xisUdSpfGJtj7UATRmS5HLcVVkH+w4dwmcR9ZS13rSdg4VlDUURvkQEDD98y5TNgpr9sTNXKb4mgb9eEymkrSb/erHCsbnUDmDrwWIO5LF3hY/OjWDkns8fId2pmWYyXSOv9Nb7I6h/rkvSxt1zEuYmP7GKusJqcMiQqTUUYLZuQMJDpCdO2BCtPNoWlhX4MUNBpMsq5IB0KuA27NwKtSrOsafJs4/L/+IDl0sCbHg49uYKXVP2z3o9RSY3luPJcfR9VNF9lmmK0lqSxAB1eNvSlzoDHzgx2H/NjuIkP8WUh+/qxvWIgoR+nmL86c7PjF5kDNf5XgnKCxuDVa3yb4ZkAooEVwceQkxz2+GZssOsHEu48L4jFGctwCBmapPb666h0CAwEAAQ==-----END-PUBLIC-KEY-----  
   8a6bd00f-c9af-4ebe-9184-0221f24ed04   -----BEGIN-PUBLIC-KEY-----MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAqLN3xmUoBeozpev3cF+sMtealu22AukFrLIjatB9TQV+ZIXN1/8hzCJXcvvOerBghzci7E/ZIHgpG6a58iN8XwwyaFBJpBNLPMFK1xpkjvt/mAnRLrRGwcs5S7911Egsgi8JKsAHpXbMC6Ji5qAsIRhLvV7hr7j0ptd3l6g7Kpp4m0Ypp9K4bSnIQjVhMe160BZ7Iy4E4xVPzYc3lXLE2atCc1acAi3inOKt+Vi8Uaw5NqcpiCl4BiAwjJVkzBIjQw/Py1yFLrPWBZmXvQ1u8Ry520AM7pbUB03xisUdSpfGJtj7UATRmS5HLcVVkH+w4dwmcR9ZS13rSdg4VlDUURvkQEDD98y5TNgpr9sTNXKb4mgb9eEymkrSb/erHCsbnUDmDrwWIO5LF3hY/OjWDkns8fId2pmWYyXSOv9Nb7I6h/rkvSxt1zEuYmP7GKusJqcMiQqTUUYLZuQMJDpCdO2BCtPNoWlhX4MUNBpMsq5IB0KuA27NwKtSrOsafJs4/L/+IDl0sCbHg49uYKXVP2z3o9RSY3luPJcfR9VNF39mmK0lqSxAB1eNvSlzoDHzgx2H/NjuIkP8WUh+/qxvWIgoR+nmL86c7PjF5kDNf5XgnKCxuDVa3yb4ZkAooEVwceQkxz2+GZssOsHEu48L4jFGctwCBmapPb666h0CAwEAAQ==-----END-PUBLIC-KEY-----  
   AAAA-aaaa-bbbb                        --22 a 00--                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
   (结果个数 = 5)

   ---    END
   ```
2. 查询“NRF实例标识”为“4947a69a-f61b-4bc1-b9da-47c9c5d14b64”配置信息：

   ```
   LST PUBLICKEY: NRFINSID="4947a69a-f61b-4bc1-b9da-47c9c5d14b64";
   ```

   ```
   %%LST PUBLICKEY: NRFINSID="4947a69a-f61b-4bc1-b9da-47c9c5d14b64";%%
   RETCODE = 0  操作成功

   操作结果如下: 
   -------------

   NRF实例标识  =  4947a69a-f61b-4bc1-b9da-47c9c5d14b64
          公钥  =  -----BEGIN-PUBLIC-KEY-----MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAqLN3xmUoBeozpev3cF+sMtealu22AukFrLIjatB9TQV+ZIXN1/8hzCJXcvvOerBghzci7E/ZIHgpG595CiN8XwwyaFBJpBNLPMFK1xpkjvt/mAnRLrRGwcs5S7911Egsgi8JKsAHpXbMC6Ji5qAsIRhLvV7hr7j0ptd3l6g7Kpp4m0Ypp9K4bSnIQjVhMe160BZ7Iy4E4xVPzYc3lXLE2atCc1acAi3inOKt+Vi8Uaw5NqcpiCl4BiAwjJVkzBIjQw/Py1yFLrPWBZmXvQ1u8Ry520AM7pbUB03xisUdSpfGJtj7UATRmS5HLcVVkH+w4dwmcR9ZS13rSdg4VlDUURvkQEDD98y5TNgpr9sTNXKb4mgb9eEymkrSb/erHCsbnUDmDrwWIO5LF3hY/OjWDkns8fId2pmWYyXSOv9Nb7I6h/rkvSxt1zEuYmP7GKusJqcMiQqTUUYLZuQMJDpCdO2BCtPNoWlhX4MUNBpMsq5IB0KuA27NwKtSrOsafJs4/L/+IDl0sCbHg49uYKXVP2z3o9RSY3luPJcfR9VNF9lmmK0lqSxAB1eNvSlzoDHzgx2H/NjuIkP8WUh+/qxvWIgoR+nmL86c7PjF5kDNf5XgnKCxuDVa3yb4ZkAooEVwceQkxz2+GZssOsHEu48L4jFGctwCBmapPb666h0CAwEAAQ==-----END-PUBLIC-KEY-----
   (结果个数 = 1)

   ---    END
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各参数含义请参见**ADD PUBLICKEY**命令的参数说明。